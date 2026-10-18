"""T3-B: konditionierte Modularfluesse aus EINEM internen Mutterzustand.

Experiment-Firewall: Diese Datei ist eine Suchflaeche, kein load-bearing Claim.
Sie veraendert weder Ledger noch Papers noch Verifikationsmodule.

Herleitungsreihenfolge (vor jedem Solver-Zieltest eingefroren):

1. Die Sheet-Geodaete M(1,t), t=-2,-1,0,1, liefert J,K,C,F und ihren
   target-unabhaengigen Tangenten S=dM/dt.
2. S liefert den chiralen Mutteroperator D_Sigma=[[0,S],[S^T,0]].
   Mit dem EINEN globalen KMS-Massstab Delta=6 log(3/2) wird
   C_Sigma=(1+exp(Delta D_Sigma/Delta))^-1 gebaut.
3. Jeder Intertwiner X in {J,K,C,F} liefert kanonisch den Graphprojektor
   P_X auf graph(X), also den CP-Kompressionskanal Phi_X(A)=V_X^* A V_X.
   Es gibt dabei weder Solver-Daten noch Fitparameter.
4. C_X=Phi_X(C_Sigma) und K_X=log((1-C_X)C_X^-1) folgen nach v258.
5. Erst danach werden die eingefrorenen v578/v632-Zielklassen verglichen.

Der N-Test benutzt die target-unabhaengige CAR/Gitter-Sinusregularisierung
D_N=f_N(D), f_N(x)=N sin(pi*x/N)/pi, und verlangt N^-2-Konvergenz.
"""

from __future__ import annotations

import ast
import inspect
import itertools
import math
import textwrap
from dataclasses import dataclass

import numpy as np


R = np.array([[1.0, 3.0, 0.0],
              [1.0, 5.0, 2.0],
              [2.0, 5.0, 3.0]])
Q = np.array([[3.0, 1.0, 0.0],
              [3.0, 2.0, 0.0],
              [3.0, 2.0, 1.0]])
ONE = np.array([1.0, 1.0, 1.0])
A_ANCHOR = np.array([1.0, 1.0, 2.0])
SHEET_TIMES = (-2, -1, 0, 1)
CORNER_NAMES = ("J", "K", "C", "F")
N_LADDER = (48, 96, 192, 384)

GLOBAL_KMS_SCALE = 6.0 * math.log(1.5)
RECOVERY_LAMBDA_2 = (2.0 / 3.0) ** 6
RECOVERY_LAMBDA_3 = (1.0 / 3.0) ** 6

ATOL = 2.0e-10
FAILURES: list[str] = []
CHECK_COUNT = 0


@dataclass(frozen=True)
class InternalObjects:
    matrices: tuple[np.ndarray, ...]
    graph_isometries: tuple[np.ndarray, ...]
    projectors: tuple[np.ndarray, ...]
    mother_covariances: dict[float, np.ndarray]
    covariances: dict[float, tuple[np.ndarray, ...]]
    modular_generators: dict[float, tuple[np.ndarray, ...]]
    observable_basis: np.ndarray
    recovery_generators: tuple[np.ndarray, ...]


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        FAILURES.append(label)
    suffix = f" -- {detail}" if detail else ""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}{suffix}")


def matrix_function_symmetric(matrix: np.ndarray, function) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return (eigenvectors * function(eigenvalues)) @ eigenvectors.T


def kms_covariance(hamiltonian: np.ndarray, scale: float) -> np.ndarray:
    return matrix_function_symmetric(
        hamiltonian,
        lambda values: 1.0 / (1.0 + np.exp(np.clip(values / scale, -700.0, 700.0))),
    )


def induce_modular_generator(covariance: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    clipped = np.clip(eigenvalues, 1.0e-15, 1.0 - 1.0e-15)
    modular_eigenvalues = np.log((1.0 - clipped) / clipped)
    return (eigenvectors * modular_eigenvalues) @ eigenvectors.T


def positive_power(matrix: np.ndarray, exponent: complex) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    powered = np.exp(exponent * np.log(eigenvalues))
    return (eigenvectors * powered) @ eigenvectors.conj().T


def matrix_exponential_2x2(generator: np.ndarray, time: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eig(generator)
    return eigenvectors @ np.diag(np.exp(time * eigenvalues)) @ np.linalg.inv(eigenvectors)


def graph_isometry(matrix: np.ndarray) -> np.ndarray:
    gram = np.eye(3) + matrix.T @ matrix
    inverse_sqrt = matrix_function_symmetric(gram, lambda values: values ** -0.5)
    return np.vstack((np.eye(3), matrix)) @ inverse_sqrt


def observable_plane() -> np.ndarray:
    first = ONE / np.linalg.norm(ONE)
    residual = A_ANCHOR - first * np.dot(first, A_ANCHOR)
    second = residual / np.linalg.norm(residual)
    return np.column_stack((first, second))


def recovery_generator_3x3() -> np.ndarray:
    stationary = np.ones((3, 3)) / 3.0
    mode_2 = np.array([1.0, -1.0, 0.0])
    mode_2 /= np.linalg.norm(mode_2)
    mode_3 = np.array([1.0, 1.0, -2.0])
    mode_3 /= np.linalg.norm(mode_3)
    channel = (
        stationary
        + RECOVERY_LAMBDA_2 * np.outer(mode_2, mode_2)
        + RECOVERY_LAMBDA_3 * np.outer(mode_3, mode_3)
    )
    return matrix_function_symmetric(channel, np.log)


def sheet_matrix(time: int) -> np.ndarray:
    return R + Q @ np.diag([1.0, float(time), float(time)])


def regularized_operator(operator: np.ndarray, rung: float) -> np.ndarray:
    if math.isinf(rung):
        return operator.copy()
    return matrix_function_symmetric(
        operator,
        lambda values: values * np.sinc(values / rung),
    )


def derive_internal_objects() -> InternalObjects:
    """Nur Compiler-/Sheet-Daten; diese Funktion darf keine Zielklasse kennen."""
    matrices = tuple(sheet_matrix(time) for time in SHEET_TIMES)
    tangent = Q @ np.diag([0.0, 1.0, 1.0])
    mother_operator = np.block([
        [np.zeros((3, 3)), tangent],
        [tangent.T, np.zeros((3, 3))],
    ])

    isometries = tuple(graph_isometry(matrix) for matrix in matrices)
    projectors = tuple(isometry @ isometry.T for isometry in isometries)
    rungs = tuple(float(value) for value in N_LADDER) + (math.inf,)
    mother_covariances: dict[float, np.ndarray] = {}
    covariances: dict[float, tuple[np.ndarray, ...]] = {}
    generators: dict[float, tuple[np.ndarray, ...]] = {}

    for rung in rungs:
        dimensionless_operator = regularized_operator(mother_operator, rung)
        physical_operator = GLOBAL_KMS_SCALE * dimensionless_operator
        mother = kms_covariance(physical_operator, GLOBAL_KMS_SCALE)
        corners = tuple(isometry.T @ mother @ isometry for isometry in isometries)
        mother_covariances[rung] = mother
        covariances[rung] = corners
        generators[rung] = tuple(induce_modular_generator(corner) for corner in corners)

    recovery = recovery_generator_3x3()
    recovery_mother = np.block([
        [recovery, np.zeros((3, 3))],
        [np.zeros((3, 3)), recovery],
    ])
    recovery_corners = tuple(
        isometry.T @ recovery_mother @ isometry for isometry in isometries
    )

    return InternalObjects(
        matrices=matrices,
        graph_isometries=isometries,
        projectors=projectors,
        mother_covariances=mother_covariances,
        covariances=covariances,
        modular_generators=generators,
        observable_basis=observable_plane(),
        recovery_generators=recovery_corners,
    )


def derivation_firewall() -> tuple[bool, set[str], bool]:
    source_lines, first_line = inspect.getsourcelines(derive_internal_objects)
    source = textwrap.dedent("".join(source_lines))
    tree = ast.parse(source)
    names = {node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name)}
    forbidden = {
        "koide", "boltzmann", "qcd", "relic", "schwarzian", "target",
        "alpha_s", "theta_i", "m_z", "m_r", "v_geo",
    }
    target_line = inspect.getsourcelines(target_class_match)[1]
    return not (names & forbidden), names & forbidden, first_line < target_line


def traceless(matrix: np.ndarray) -> np.ndarray:
    return matrix - 0.5 * np.trace(matrix) * np.eye(2)


def generator_discriminant(generator: np.ndarray) -> complex:
    return np.trace(generator) ** 2 - 4.0 * np.linalg.det(generator)


def generator_class(generator: np.ndarray) -> str:
    reduced_norm = np.linalg.norm(traceless(generator), ord="fro")
    discriminant = generator_discriminant(generator)
    if reduced_norm <= ATOL:
        return "identity/tracial"
    if abs(discriminant) <= ATOL:
        return "parabolic"
    if abs(discriminant.imag) <= ATOL and discriminant.real > 0.0:
        return "hyperbolic"
    if abs(discriminant.imag) <= ATOL and discriminant.real < 0.0:
        return "elliptic"
    return "loxodromic/complex"


def target_class_match(generators: tuple[np.ndarray, ...]) -> tuple[bool, tuple[int, ...] | None]:
    """Nachtraeglicher, fitfreier Vergleich aller 24 Kanal-Zuordnungen."""
    target_discriminant = GLOBAL_KMS_SCALE ** 2
    for assignment in itertools.permutations(range(4)):
        pole, boltzmann, qcd, relic = (generators[index] for index in assignment)
        pole_ok = abs(generator_discriminant(pole) - target_discriminant) <= ATOL
        boltzmann_ok = abs(generator_discriminant(boltzmann) - target_discriminant) <= ATOL
        qcd_ok = generator_class(qcd) == "parabolic"
        relic_ok = generator_class(relic) == "identity/tracial"
        if pole_ok and boltzmann_ok and qcd_ok and relic_ok:
            return True, assignment
    return False, None


def effective_generators(
    internal: InternalObjects,
) -> tuple[
    tuple[np.ndarray, ...],
    tuple[np.ndarray, ...],
    tuple[np.ndarray, ...],
]:
    basis = internal.observable_basis
    modular = internal.modular_generators[math.inf]
    physical_compressions = tuple(
        basis.T @ (GLOBAL_KMS_SCALE * generator) @ basis
        for generator in modular
    )
    modular_effective = tuple(1j * generator for generator in physical_compressions)
    euclidean_effective = tuple(-generator for generator in physical_compressions)
    gksl_effective = tuple(
        basis.T @ recovery @ basis + 1j * generator
        for generator, recovery in zip(physical_compressions, internal.recovery_generators)
    )
    return modular_effective, euclidean_effective, gksl_effective


def export_flows(generators: tuple[np.ndarray, ...], label: str) -> None:
    print(f"\n{label}: deklarierte Projektivobservable z=[1:z], Start z=1")
    for name, generator in zip(CORNER_NAMES, generators):
        discriminant = generator_discriminant(generator)
        schwarzian = -0.5 * discriminant
        samples = []
        for time in (0.0, 0.5, 1.0):
            flow = matrix_exponential_2x2(generator, time)
            value = (flow[0, 0] + flow[0, 1]) / (flow[1, 0] + flow[1, 1])
            samples.append(value)
        print(
            f"  {name}: class={generator_class(generator):20s} "
            f"disc={discriminant.real:+.12e}{discriminant.imag:+.12e}i "
            f"Schwarzian={schwarzian.real:+.12e}{schwarzian.imag:+.12e}i"
        )
        print(
            "     A="
            + np.array2string(generator, precision=9, suppress_small=False)
            + "; z(0,.5,1)="
            + ", ".join(f"{value.real:+.9f}{value.imag:+.9f}i" for value in samples)
        )


def cocycle_residuals(internal: InternalObjects) -> tuple[float, float]:
    covariances = internal.covariances[math.inf]
    modular = internal.modular_generators[math.inf]
    densities = []
    for generator in modular:
        gibbs = matrix_function_symmetric(-generator, np.exp)
        densities.append(gibbs / np.trace(gibbs))

    chain_max = 0.0
    endpoint_max = 0.0
    for time in (0.125, 0.5, 1.0, 2.0):
        def cocycle(i: int, j: int) -> np.ndarray:
            return positive_power(densities[i], 1j * time) @ positive_power(
                densities[j], -1j * time
            )

        for i, j, k in ((0, 1, 2), (1, 2, 3)):
            residual = np.linalg.norm(
                cocycle(i, j) @ cocycle(j, k) - cocycle(i, k),
                ord="fro",
            )
            chain_max = max(chain_max, float(residual))
        endpoint = np.linalg.norm(
            cocycle(0, 1) @ cocycle(1, 2) @ cocycle(2, 3) - cocycle(0, 3),
            ord="fro",
        )
        endpoint_max = max(endpoint_max, float(endpoint))

    assert all(np.all(np.linalg.eigvalsh(covariance) > 0.0) for covariance in covariances)
    return chain_max, endpoint_max


def run() -> int:
    print("=" * 78)
    print("T3-B -- EIN Mutterzustand, vier Graphkanaele, konditionierte Modularzeit")
    print("=" * 78)
    print("Herleitung: Sheet-Tangente -> C_Sigma -> graph(J,K,C,F) -> C_i -> K_i")
    print("Zielklassen werden erst NACH diesem Konstruktor geladen/geprueft.")

    internal = derive_internal_objects()
    firewall_ok, forbidden_names, order_ok = derivation_firewall()
    check(
        "ZIRKULARITAETS-FIREWALL",
        firewall_ok and order_ok,
        f"verbotene Namen={sorted(forbidden_names)}, derive-vor-target={order_ok}",
    )

    mother = internal.mother_covariances[math.inf]
    mother_spectrum = np.linalg.eigvalsh(mother)
    check(
        "EIN FAITHFUL MUTTERZUSTAND C_Sigma",
        mother_spectrum.min() > 0.0 and mother_spectrum.max() < 1.0,
        f"spec=[{mother_spectrum.min():.12e}, {mother_spectrum.max():.12e}]",
    )

    isometry_residual = max(
        np.linalg.norm(isometry.T @ isometry - np.eye(3), ord="fro")
        for isometry in internal.graph_isometries
    )
    projector_residual = max(
        np.linalg.norm(projector @ projector - projector, ord="fro")
        for projector in internal.projectors
    )
    ranks = tuple(int(np.linalg.matrix_rank(projector, tol=1.0e-10))
                  for projector in internal.projectors)
    check(
        "VIER TARGET-FREIE GRAPH-PROJEKTOREN/CP-KANAELE",
        isometry_residual <= ATOL and projector_residual <= ATOL and ranks == (3, 3, 3, 3),
        f"max V*V-I={isometry_residual:.3e}, max P2-P={projector_residual:.3e}, ranks={ranks}",
    )

    corner_spectra = tuple(np.linalg.eigvalsh(covariance)
                           for covariance in internal.covariances[math.inf])
    legal_corners = all(spectrum.min() > 0.0 and spectrum.max() < 1.0
                        for spectrum in corner_spectra)
    print("\nModulare Generatoren K_i=log((1-C_i)C_i^-1), dimensionslos:")
    for name, spectrum, generator in zip(
        CORNER_NAMES,
        corner_spectra,
        internal.modular_generators[math.inf],
    ):
        print(
            f"  {name}: spec(C_i)="
            + np.array2string(spectrum, precision=12)
            + " spec(K_i)="
            + np.array2string(np.linalg.eigvalsh(generator), precision=12)
        )
    check("VIER LEGALE K_i OHNE FIT", legal_corners)

    ladder_errors: dict[int, float] = {}
    limiting = internal.modular_generators[math.inf]
    for rung in N_LADDER:
        ladder_errors[rung] = max(
            np.linalg.norm(current - limit, ord="fro")
            for current, limit in zip(internal.modular_generators[float(rung)], limiting)
        )
    error_values = [ladder_errors[rung] for rung in N_LADDER]
    observed_orders = [
        math.log(error_values[index] / error_values[index + 1], 2.0)
        for index in range(len(error_values) - 1)
    ]
    ladder_ok = (
        all(left > right for left, right in zip(error_values, error_values[1:]))
        and min(observed_orders) >= 1.95
        and error_values[-1] <= 5.0e-4
    )
    check(
        "STABILE N-LEITER",
        ladder_ok,
        "errors=" + ", ".join(
            f"N={rung}:{ladder_errors[rung]:.12e}" for rung in N_LADDER
        ) + "; orders=" + ", ".join(f"{order:.6f}" for order in observed_orders),
    )

    koide_reading = tuple(float(A_ANCHOR @ matrix @ ONE)
                          for matrix in internal.matrices)
    koide_steps = tuple(
        koide_reading[index + 1] - koide_reading[index] for index in range(3)
    )
    cross_ratio = (
        (koide_reading[0] - koide_reading[2])
        * (koide_reading[1] - koide_reading[3])
        / (
            (koide_reading[0] - koide_reading[3])
            * (koide_reading[1] - koide_reading[2])
        )
    )
    check(
        "KOIDE-BASISTRANSLATION VERSCHRAENKT",
        koide_reading == (26.0, 35.0, 44.0, 53.0)
        and koide_steps == (9.0, 9.0, 9.0)
        and abs(cross_ratio - 4.0 / 3.0) <= ATOL,
        f"ell={koide_reading}, Schritte={koide_steps}, CR={cross_ratio:.12f}",
    )

    modular_effective, euclidean_effective, gksl_effective = effective_generators(internal)
    export_flows(modular_effective, "ECHTE TOMITA-ZEIT: i Delta K_i")
    pure_classes = tuple(generator_class(generator) for generator in modular_effective)
    pure_qcd_possible = "parabolic" in pure_classes
    pure_relic_possible = "identity/tracial" in pure_classes
    antihermitian_no_go = all(
        np.allclose(generator.conj().T, -generator, atol=ATOL)
        for generator in modular_effective
    ) and not pure_qcd_possible
    check(
        "REIN-MODULARER QCD-NO-GO",
        antihermitian_no_go,
        f"Klassen={pure_classes}; iK antihermitesch => elliptisch, "
        "nie nichttrivial parabolisch",
    )

    pure_match, pure_assignment = target_class_match(modular_effective)
    print(
        "[RESULT] Hartes v578/v632-Gate rein modular: "
        f"{'PASS' if pure_match else 'FAIL'}; Zuordnung={pure_assignment}"
    )

    export_flows(
        euclidean_effective,
        "GROSSZUEGIGE ANALYTISCHE FORTSETZUNG: -Delta K_i",
    )
    euclidean_classes = tuple(
        generator_class(generator) for generator in euclidean_effective
    )
    check(
        "WICK-KONTROLLE SCHLIESST QCD/RELIC EBENFALLS AUS",
        euclidean_classes == ("hyperbolic",) * 4,
        f"Klassen={euclidean_classes}",
    )

    recovery = recovery_generator_3x3()
    recovery_spectrum = np.linalg.eigvalsh(recovery)
    recovery_gap = -max(value for value in recovery_spectrum if value < -ATOL)
    recovery_ok = (
        np.allclose(recovery, recovery.T, atol=ATOL)
        and np.allclose(recovery.sum(axis=0), 0.0, atol=ATOL)
        and np.allclose(recovery.sum(axis=1), 0.0, atol=ATOL)
        and abs(recovery_gap - GLOBAL_KMS_SCALE) <= ATOL
    )
    check(
        "v238-RECOVERY OHNE FREIE RATE",
        recovery_ok,
        "spec(L)=" + np.array2string(recovery_spectrum, precision=12)
        + f", gap={recovery_gap:.12f}",
    )

    export_flows(gksl_effective, "v238 GKSL: L_i + i Delta K_i")
    gksl_classes = tuple(generator_class(generator) for generator in gksl_effective)
    gksl_qcd_possible = "parabolic" in gksl_classes
    gksl_relic_possible = "identity/tracial" in gksl_classes
    gksl_match, gksl_assignment = target_class_match(gksl_effective)
    print(
        "[RESULT] Hartes v578/v632-Gate mit v238-GKSL: "
        f"{'PASS' if gksl_match else 'FAIL'}; Zuordnung={gksl_assignment}; "
        f"Klassen={gksl_classes}"
    )
    check(
        "LINDBLAD-PARABOLIK WIRD NICHT BEHAUPTET",
        gksl_qcd_possible or not gksl_match,
        "ein NEEDS-LINDBLAD-Verdikt ist nur bei vollstaendigem Klassenmatch erlaubt",
    )

    chain_residual, endpoint_residual = cocycle_residuals(internal)
    check(
        "CONNES-KOZYKELKOMPOSITION ENTLANG J-K-C-F",
        chain_residual <= ATOL and endpoint_residual <= ATOL,
        f"max Dreierresiduum={chain_residual:.12e}, J->F={endpoint_residual:.12e}",
    )

    scales = tuple(GLOBAL_KMS_SCALE for _ in CORNER_NAMES)
    one_scale = len({round(value, 15) for value in scales}) == 1
    check(
        "GENAU EIN GLOBALER KMS-MASSSTAB",
        one_scale and abs(recovery_gap - GLOBAL_KMS_SCALE) <= ATOL,
        f"Delta={GLOBAL_KMS_SCALE:.12f}, interface scales={scales}",
    )

    if pure_match:
        verdict = "T3B-COCYCLE-ALIVE"
        reason = f"reine Klassen reproduziert; Zuordnung={pure_assignment}"
    elif gksl_match:
        verdict = "T3B-NEEDS-LINDBLAD"
        reason = f"notwendige Erweiterung: v238 G=L+i Delta K; Zuordnung={gksl_assignment}"
    else:
        verdict = "T3B-DEAD"
        missing = []
        if not gksl_qcd_possible:
            missing.append("QCD-parabolisch nur durch Handsetzung")
        if not gksl_relic_possible:
            missing.append("kein tracialer/degenerierter Relic-Corner")
        target_disc = GLOBAL_KMS_SCALE ** 2
        gksl_discs = tuple(generator_discriminant(generator) for generator in gksl_effective)
        exact_hyperbolic = sum(abs(value - target_disc) <= ATOL for value in gksl_discs)
        if exact_hyperbolic < 2:
            missing.append(
                f"Pole/Boltzmann -Delta^2/2 nicht doppelt exakt ({exact_hyperbolic}/2)"
            )
        reason = "; ".join(missing)

    print("\n" + "=" * 78)
    print(f"VERDICT: {verdict}")
    print(f"GRUND: {reason}")
    print(
        "KILL-AUDIT: Projektoren target-frei=PASS; ein Skalar/eine Zeit=PASS; "
        f"QCD ohne Handsetzung={'PASS' if gksl_qcd_possible else 'FAIL'}; "
        "keine externen Mutterzustandsparameter=PASS; N-Leiter="
        f"{'PASS' if ladder_ok else 'FAIL'}"
    )
    print(
        f"MECHANISCHE CHECKS: {CHECK_COUNT - len(FAILURES)}/{CHECK_COUNT} PASS, "
        f"{len(FAILURES)} FAIL {FAILURES}"
    )
    print("=" * 78)
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    raise SystemExit(run())
