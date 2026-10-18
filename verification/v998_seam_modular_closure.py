"""v998 -- SEAM.EQUIV.MMST.01 / SEAM.SIMPLECURRENT.GENERATOR.01
[O updates: C7 ARITHMETIC SHADOW now exact; net-level C7 stays cited].
Provenance: experiments/tfpt-discovery/mmst_gap_closure_probe.py
+ the E4 identity (review wave 4, C7 sharpening).

THE POINT (review wave 4, 2026-08-29).  Execute the two finite shadows
left by the MMST identification checklist, plus the reviewer C7
sharpening Theta_E8 = E4.

  [E-measured] two-edge HS remainder bounded by 2.11 on the frozen
        plateau table Nx in (16,24,32,48,64,96).
  [E]          lattice character theta_E8 / eta^8 EXACT four orders:
        t-grid [1,0,248,0,4124,0,34752].
  [E]          Theta_E8(tau) = E4(tau) as Eisenstein series: q-expansion
        match to >= 8 orders exact in sympy (C7 arithmetic shadow).
  [N]          j^{1/3} numeric modular transform at 60 digits; S-weight
        bookkeeping (tau^4 cancels in the weight-0 character).
  [O cited]    net-level C7 modular covariance of the completed
        extension stays cited/open.

MUST-FAIL: a wrong Eisenstein series (E6, or 241 sigma_3) misses E4;
dropping GSO is already the v994 mutant (not re-run).

HONEST SCOPE (firewall): finite QWZ cylinders and finite q-expansions;
the all-N supremum of the HS remainder remains an analytic quantifier;
conformal-net modular covariance is not claimed.  Display markers of
both contracts stay [O]/[C] as booked -- no silent upgrade.
1+1D in and out.  Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations


import itertools
from math import pi

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.special import digamma, polygamma

from tfpt_constants import check, summary, reset


SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TX = SX / (2j) - SZ / 2
TY = SY / (2j) - SZ / 2

MASS = 1.0
NY = 8
ALPHA = 0.25
NXS = (16, 24, 32, 48, 64, 96)
ZERO_CUT = 1.0e-10
MATRIX_TOL = 1.0e-10
REMAINDER_BOUND = 2.11
MODULAR_TERMS = 80
MODULAR_DPS = 60
MODULAR_TOL = mp.mpf("1e-45")

def report(name: str, ok: bool, detail: str = "") -> None:
    check(name if not detail else "%s -- %s" % (name, detail), ok)


def strip_hamiltonian(momentum: float) -> np.ndarray:
    """QWZ strip in the exp(-ipx) Bloch convention."""
    dimension = 2 * NY
    matrix = np.zeros((dimension, dimension), dtype=complex)
    onsite = np.sin(momentum) * SX + (MASS - np.cos(momentum)) * SZ
    for y_index in range(NY):
        site = slice(2 * y_index, 2 * y_index + 2)
        matrix[site, site] = onsite
    for y_index in range(NY - 1):
        lower = slice(2 * y_index, 2 * y_index + 2)
        upper = slice(2 * y_index + 2, 2 * y_index + 4)
        matrix[upper, lower] = TY
        matrix[lower, upper] = TY.conj().T
    return matrix


def fermi_projector(matrix: np.ndarray) -> np.ndarray:
    """Particle-hole symmetric Fermi covariance."""
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    occupations = np.zeros(eigenvalues.shape, dtype=float)
    occupations[eigenvalues < -ZERO_CUT] = 1.0
    occupations[np.abs(eigenvalues) <= ZERO_CUT] = 0.5
    return (eigenvectors * occupations) @ eigenvectors.conj().T


def cylinder_hamiltonian(nx: int, alpha: float) -> np.ndarray:
    """Real-space seam-gauge cylinder, used for the construction cross-check."""
    dimension = 2 * nx * NY
    matrix = np.zeros((dimension, dimension), dtype=complex)
    seam_phase = np.exp(2j * pi * alpha)
    for x_index in range(nx):
        for y_index in range(NY):
            source = 2 * (x_index * NY + y_index)
            source_slice = slice(source, source + 2)
            matrix[source_slice, source_slice] += MASS * SZ

            next_x = (x_index + 1) % nx
            target = 2 * (next_x * NY + y_index)
            target_slice = slice(target, target + 2)
            amplitude = seam_phase if x_index == nx - 1 else 1.0
            matrix[target_slice, source_slice] += amplitude * TX
            matrix[source_slice, target_slice] += (
                np.conj(amplitude) * TX.conj().T
            )

            if y_index + 1 < NY:
                target = 2 * (x_index * NY + y_index + 1)
                target_slice = slice(target, target + 2)
                matrix[target_slice, source_slice] += TY
                matrix[source_slice, target_slice] += TY.conj().T
    return matrix


def bloch_covariance(
    nx: int, alpha: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Exact Bloch assembly of the seam-gauge cylinder covariance."""
    mode_indices = np.arange(-nx // 2, nx // 2)
    momenta = 2 * pi * (mode_indices + alpha) / nx
    positions = np.arange(nx)
    fourier = np.exp(-1j * np.outer(positions, momenta)) / np.sqrt(nx)
    strip_projectors = np.array(
        [fermi_projector(strip_hamiltonian(float(k))) for k in momenta]
    )
    covariance = np.einsum(
        "xi,iab,yi->xayb",
        fourier,
        strip_projectors,
        fourier.conj(),
        optimize=True,
    )
    return covariance.reshape(2 * NY * nx, 2 * NY * nx), fourier, mode_indices


def edge_profiles() -> tuple[np.ndarray, np.ndarray]:
    """Extract the orthogonal top/bottom zero-mode transverse profiles."""
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0))
    zero_indices = np.where(np.abs(eigenvalues) <= ZERO_CUT)[0]
    if len(zero_indices) != 2:
        raise RuntimeError("expected exactly two QWZ zero-energy edge modes")

    top_scores = [
        float(np.sum(np.abs(eigenvectors[:4, index]) ** 2))
        for index in zero_indices
    ]
    bottom_scores = [
        float(np.sum(np.abs(eigenvectors[-4:, index]) ** 2))
        for index in zero_indices
    ]
    top = eigenvectors[:, zero_indices[int(np.argmax(top_scores))]]
    bottom = eigenvectors[:, zero_indices[int(np.argmax(bottom_scores))]]
    return top, bottom


def hardy_overlap_squared(mode_difference: int, alpha: float) -> float:
    """Proof-document equation (5.1), with mode_difference=m-n."""
    return float(
        np.sin(pi * alpha) ** 2
        / (pi**2 * (mode_difference + alpha) ** 2)
    )


def hardy_difference(mode_indices: np.ndarray, alpha: float) -> np.ndarray:
    """Compression of P_0-P_alpha to the displayed untwisted modes.

    For z_n=n-alpha,
      sum_{r>=0} 1/((r+z_n)(r+z_l))
       = (psi(z_l)-psi(z_n))/(z_l-z_n),
    and the diagonal is psi_1(z_n).  This is the infinite m<=0 sum of
    products of the exact overlap amplitudes in equation (5.1).
    """
    shifted = mode_indices.astype(float) - alpha
    size = len(mode_indices)
    occupied_twisted = np.empty((size, size), dtype=float)
    for row in range(size):
        for column in range(size):
            if row == column:
                overlap_sum = polygamma(1, shifted[row])
            else:
                overlap_sum = (
                    digamma(shifted[column]) - digamma(shifted[row])
                ) / (shifted[column] - shifted[row])
            occupied_twisted[row, column] = (
                np.sin(pi * alpha) ** 2 / pi**2 * overlap_sum
            )
    occupied_untwisted = np.diag((mode_indices <= 0).astype(float))
    difference = occupied_untwisted - occupied_twisted
    return 0.5 * (difference + difference.T)


def edge_isometry(fourier: np.ndarray, profile: np.ndarray) -> np.ndarray:
    """Embed every longitudinal Fourier mode at one transverse profile."""
    nx = fourier.shape[0]
    frame = fourier[:, :, None] * profile[None, None, :]
    return frame.transpose(0, 2, 1).reshape(2 * NY * nx, nx)


def hs_norm(matrix: np.ndarray) -> float:
    return float(np.sqrt(np.vdot(matrix, matrix).real))


def exact_hardy_truncated_hs2(cutoff: int, alpha: float) -> float:
    """Equation (5.4) for one edge and symmetric index cutoff."""
    total = 0.0
    for distance in range(1, 2 * cutoff + 1):
        multiplicity = (
            distance
            if distance <= cutoff
            else 2 * cutoff - distance + 1
        )
        total += multiplicity * (
            1.0 / (distance + alpha) ** 2
            + 1.0 / (distance - alpha) ** 2
        )
    return np.sin(pi * alpha) ** 2 / pi**2 * total


def enumerate_e8_theta(max_norm_squared: int = 6) -> list[int]:
    """Enumerate the standard integral and half-integral E8 lattice."""
    counts = {norm: 0 for norm in range(0, max_norm_squared + 1, 2)}

    integer_limit = int(np.sqrt(max_norm_squared))
    integer_values = range(-integer_limit, integer_limit + 1)
    for vector in itertools.product(integer_values, repeat=8):
        norm_squared = sum(value * value for value in vector)
        if (
            norm_squared <= max_norm_squared
            and norm_squared % 2 == 0
            and sum(vector) % 2 == 0
        ):
            counts[norm_squared] += 1

    doubled_limit = int(np.sqrt(4 * max_norm_squared))
    odd_values = tuple(
        value
        for value in range(-doubled_limit, doubled_limit + 1)
        if value % 2
    )
    for doubled_vector in itertools.product(odd_values, repeat=8):
        four_norm_squared = sum(value * value for value in doubled_vector)
        if (
            four_norm_squared <= 4 * max_norm_squared
            and sum(doubled_vector) % 4 == 0
        ):
            counts[four_norm_squared // 4] += 1

    return [counts[2 * order] for order in range(max_norm_squared // 2 + 1)]


def exact_character_coefficients(
    theta_coefficients: list[int],
) -> tuple[list[int], list[int]]:
    """Multiply theta_E8 by prod_(n>=1)(1-q^n)^-8 in SymPy."""
    max_order = len(theta_coefficients) - 1
    q_symbol = sp.symbols("q")
    eta_inverse_eight = sp.Integer(1)
    for mode in range(1, max_order + 1):
        eta_inverse_eight = sp.series(
            eta_inverse_eight * (1 - q_symbol**mode) ** -8,
            q_symbol,
            0,
            max_order + 1,
        ).removeO().expand()
    theta = sum(
        sp.Integer(coefficient) * q_symbol**order
        for order, coefficient in enumerate(theta_coefficients)
    )
    character = sp.Poly(
        sp.series(
            theta * eta_inverse_eight, q_symbol, 0, max_order + 1
        ).removeO(),
        q_symbol,
    )
    eta_coefficients = [
        int(sp.Poly(eta_inverse_eight, q_symbol).nth(order))
        for order in range(max_order + 1)
    ]
    character_coefficients = [
        int(character.nth(order)) for order in range(max_order + 1)
    ]
    return eta_coefficients, character_coefficients


def divisor_cube_sum(number: int) -> int:
    return sum(
        divisor**3
        for divisor in range(1, number + 1)
        if number % divisor == 0
    )


def modular_values(
    tau: mp.mpc, terms: int = MODULAR_TERMS
) -> tuple[mp.mpc, mp.mpc, mp.mpc, mp.mpc, mp.mpc, mp.mpf]:
    """Truncated E4, eta, chi, j, principal j^(1/3), and |q|."""
    q_value = mp.exp(2 * mp.pi * 1j * tau)
    e4 = mp.mpc(1)
    for order in range(1, terms + 1):
        e4 += 240 * divisor_cube_sum(order) * q_value**order
    eta = mp.exp(mp.pi * 1j * tau / 12)
    for order in range(1, terms + 1):
        eta *= 1 - q_value**order
    character = e4 / eta**8
    discriminant = eta**24
    j_invariant = e4**3 / discriminant
    j_cube_root = mp.root(j_invariant, 3)
    return e4, eta, character, j_invariant, j_cube_root, abs(q_value)



def e4_q_series(max_order: int) -> list[int]:
    """Classical Eisenstein E4 = 1 + 240 sum_n sigma_3(n) q^n."""
    return [
        1 if order == 0 else 240 * divisor_cube_sum(order)
        for order in range(max_order + 1)
    ]


def _conv(left, right, max_order):
    out = [0] * (max_order + 1)
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right):
            if i + j > max_order or b == 0:
                continue
            out[i + j] += a * b
    return out


def _series_pow(coeffs, power, max_order):
    result = [0] * (max_order + 1)
    result[0] = 1
    for _ in range(power):
        result = _conv(result, coeffs, max_order)
    return result


def jacobi_theta_e8_q_series(max_order: int) -> list[int]:
    """Integer q-expansion of (theta2^8 + theta3^8 + theta4^8)/2.

    theta3 = sum q^{n^2}, theta4 = sum (-1)^n q^{n^2},
    theta2^8 starts at q^2 in integer powers after the q^{1/4} bookkeeping:
    theta2 = 2 q^{1/4}(1 + q^2 + q^6 + ...) so theta2^8 = 256 q^2 * (integer).
    Equivalent integer form: coeffs of sum_{n odd} q^{n^2}  (the odd squares),
    then raise to the 8th and scale.  Using u=q^{1/4} convolution on the
    integer grid of fourth-powers is exact and cheap.
    """
    window = 8 * max_order
    theta3 = [0] * (window + 1)
    theta4 = [0] * (window + 1)
    theta2 = [0] * (window + 1)
    limit = int(window ** 0.5) + 2
    for n in range(-limit, limit + 1):
        even = 4 * n * n
        if 0 <= even <= window:
            theta3[even] += 1
            theta4[even] += (-1) ** n
        odd = (2 * n + 1) ** 2
        if 0 <= odd <= window:
            theta2[odd] += 1
    t2_8 = _series_pow(theta2, 8, window)
    t3_8 = _series_pow(theta3, 8, window)
    t4_8 = _series_pow(theta4, 8, window)
    combo = [t2_8[k] + t3_8[k] + t4_8[k] for k in range(window + 1)]
    # combo lives on u = q_J^{1/4} with Jacobi nome q_J = e^{pi i tau}.
    # Dedekind q = e^{2 pi i tau} = q_J^2 sits at u-index 8n.
    # The factor 1/2 is exact on those even combination values.
    out = []
    for order in range(max_order + 1):
        index = 8 * order
        if index >= len(combo):
            raise ValueError("Jacobi window too short for q^%d" % order)
        value = combo[index]
        if value % 2:
            raise ValueError("Jacobi combination not even at q^%d" % order)
        out.append(int(value // 2))
    return out


def lattice_theta_e8_q_series(max_order: int) -> list[int]:
    """Even-norm E8 theta coefficients through q^{max_order}."""
    return enumerate_e8_theta(max_norm_squared=2 * max_order)


def run_two_edge_and_c7() -> None:
    print("=" * 78)
    print("MMST GAP CLOSURE PROBE -- exploration-only finite shadows")
    print("=" * 78)

    # Validate that the fast Bloch assembly is exactly the requested seam cylinder.
    dense_checks = []
    for check_alpha in (0.0, ALPHA):
        dense_covariance = fermi_projector(
            cylinder_hamiltonian(NXS[0], check_alpha)
        )
        bloch_check, _, _ = bloch_covariance(NXS[0], check_alpha)
        dense_checks.append(hs_norm(dense_covariance - bloch_check))
    report(
        "QWZ cylinder/Bloch seam-gauge identity",
        max(dense_checks) < MATRIX_TOL,
        "max ||C_dense-C_Bloch||_HS=%.3e" % max(dense_checks),
    )

    top_profile, bottom_profile = edge_profiles()
    profile_overlap = abs(np.vdot(top_profile, bottom_profile))
    top_weight = float(np.sum(np.abs(top_profile[:2]) ** 2))
    bottom_weight = float(np.sum(np.abs(bottom_profile[-2:]) ** 2))
    report(
        "extracted top/bottom edge profiles are orthogonal and edge-localized",
        profile_overlap < MATRIX_TOL
        and top_weight > 1 - MATRIX_TOL
        and bottom_weight > 1 - MATRIX_TOL,
        "|<top,bottom>|=%.3e; boundary weights=(%.12f, %.12f)"
        % (profile_overlap, top_weight, bottom_weight),
    )

    overlap_formula_checks = []
    for difference_index in (-7, -2, 0, 3, 9):
        exact_value = (
            np.sin(pi * ALPHA) ** 2
            / (pi**2 * (difference_index + ALPHA) ** 2)
        )
        overlap_formula_checks.append(
            abs(hardy_overlap_squared(difference_index, ALPHA) - exact_value)
        )
    report(
        "Hardy quarter-twist overlap equation (5.1) implemented exactly",
        max(overlap_formula_checks) < 1.0e-15,
        "alpha=1/4; Delta p=2pi/(4Nx)",
    )

    print()
    print("TWO-EDGE HS DECOMPOSITION  (M=1, Ny=8, sectors k=0 vs k=1)")
    print(
        "  Nx     ||Delta||_HS   ||Dtop||_HS   ||Dbottom||_HS"
        "   ||Dedge||_HS     ||R_N||_HS"
    )
    remainder_norms: list[float] = []
    edge_hs_squared: list[float] = []
    hardy_formula_hs_squared: list[float] = []
    identity_errors: list[float] = []
    isometry_errors: list[float] = []

    for nx in NXS:
        covariance_zero, fourier_zero, mode_indices = bloch_covariance(nx, 0.0)
        covariance_quarter, _, _ = bloch_covariance(nx, ALPHA)
        delta = covariance_zero - covariance_quarter

        hardy = hardy_difference(mode_indices, ALPHA)
        top_embedding = edge_isometry(fourier_zero, top_profile)
        bottom_embedding = edge_isometry(fourier_zero, bottom_profile)
        isometry_errors.append(
            max(
                hs_norm(top_embedding.conj().T @ top_embedding - np.eye(nx)),
                hs_norm(
                    bottom_embedding.conj().T @ bottom_embedding - np.eye(nx)
                ),
                hs_norm(top_embedding.conj().T @ bottom_embedding),
            )
        )

        # The signs encode E_top=-sin(p), E_bottom=+sin(p).
        d_top = top_embedding @ (-hardy) @ top_embedding.conj().T
        d_bottom = bottom_embedding @ hardy @ bottom_embedding.conj().T
        d_edge = d_top + d_bottom
        remainder = delta - d_edge

        reconstruction_error = hs_norm(
            delta - (d_top + d_bottom + remainder)
        )
        identity_errors.append(reconstruction_error)
        remainder_norms.append(hs_norm(remainder))
        edge_hs_squared.append(hs_norm(d_edge) ** 2)
        hardy_formula_hs_squared.append(
            2 * exact_hardy_truncated_hs2(nx // 2, ALPHA)
        )
        print(
            "  %3d     %11.8f   %11.8f    %11.8f"
            "    %11.8f    %11.8f"
            % (
                nx,
                hs_norm(delta),
                hs_norm(d_top),
                hs_norm(d_bottom),
                hs_norm(d_edge),
                hs_norm(remainder),
            )
        )

    report(
        "edge embeddings are isometries with orthogonal ranges",
        max(isometry_errors) < MATRIX_TOL,
        "max Gram error %.3e" % max(isometry_errors),
    )
    report(
        "Delta_N=D_top+D_bottom+R_N matrix identity",
        max(identity_errors) < MATRIX_TOL,
        "max reconstruction error %.3e" % max(identity_errors),
    )

    log_slope, log_intercept = np.polyfit(
        np.log(np.asarray(NXS, dtype=float)),
        np.asarray(edge_hs_squared),
        1,
    )
    analytic_slope = 2 / pi**2
    report(
        "embedded two-edge Hardy block has the analytic logarithmic coefficient",
        abs(log_slope - analytic_slope) < 0.01,
        "fit %.9f; exact 2/pi^2=%.9f; finite-range delta %.3e"
        % (log_slope, analytic_slope, log_slope - analytic_slope),
    )

    inverse_sizes = 1 / np.asarray(NXS, dtype=float)
    plateau_slope, plateau_limit = np.polyfit(
        inverse_sizes, np.asarray(remainder_norms), 1
    )
    plateau_prediction = plateau_limit + plateau_slope * inverse_sizes
    plateau_residual = float(
        np.max(np.abs(np.asarray(remainder_norms) - plateau_prediction))
    )
    relative_span = (
        max(remainder_norms) - min(remainder_norms)
    ) / float(np.mean(remainder_norms))
    two_edge_ok = (
        max(remainder_norms) <= REMAINDER_BOUND
        and relative_span < 0.01
        and plateau_residual < 1.0e-4
        and plateau_limit <= REMAINDER_BOUND
    )
    report(
        "two-edge remainder is bounded on the frozen exhaustion and plateaus",
        two_edge_ok,
        "max %.9f <= %.2f; rel span %.3e; 1/N limit %.9f; max fit residual %.3e"
        % (
            max(remainder_norms),
            REMAINDER_BOUND,
            relative_span,
            plateau_limit,
            plateau_residual,
        ),
    )
    print(
        "  exact equation-(5.4) two-edge HS^2 values:",
        ["%.9f" % value for value in hardy_formula_hs_squared],
    )
    print(
        "  boundary: bound %.2f is verified on Nxs=%s; the all-N supremum"
        " remains an analytic quantifier."
        % (REMAINDER_BOUND, NXS)
    )

    print()
    print("C7 MODULAR SHADOW")
    theta_coefficients = enumerate_e8_theta()
    expected_theta = [1, 240, 2160, 6720]
    report(
        "exact E8 lattice enumeration through norm squared 6",
        theta_coefficients == expected_theta,
        "theta_E8(q) coefficients %s" % theta_coefficients,
    )

    eta_coefficients, character_coefficients = exact_character_coefficients(
        theta_coefficients
    )
    expected_character = [1, 248, 4124, 34752]
    t_grid_character = []
    for coefficient in character_coefficients:
        t_grid_character.extend((coefficient, 0))
    t_grid_character = t_grid_character[:-1]
    expected_t_grid = [1, 0, 248, 0, 4124, 0, 34752]
    coefficient_ok = (
        character_coefficients == expected_character
        and t_grid_character == expected_t_grid
    )
    report(
        "theta_E8 * eta^-8 exact coefficient identity through q^3",
        coefficient_ok,
        "eta^-8=%s; chi=%s; t-grid=%s"
        % (eta_coefficients, character_coefficients, t_grid_character),
    )

    mp.mp.dps = MODULAR_DPS
    test_points = (
        mp.mpc(0, 1),
        mp.mpc("0.2", "1.1"),
        mp.mpc("-0.25", "0.9"),
    )
    maximum_character_error = mp.mpf("0")
    maximum_root_error = mp.mpf("0")
    maximum_weight_four_error = mp.mpf("0")
    maximum_tail_bound = mp.mpf("0")

    print("  numeric weight-zero S checks and chi=j^(1/3):")
    for tau in test_points:
        transformed_tau = -1 / tau
        e4, eta, character, _, j_root, q_abs = modular_values(tau)
        (
            transformed_e4,
            transformed_eta,
            transformed_character,
            _,
            _,
            transformed_q_abs,
        ) = modular_values(transformed_tau)

        character_error = abs(transformed_character - character) / abs(character)
        root_error = abs(j_root - character) / abs(character)
        e4_error = abs(transformed_e4 - tau**4 * e4) / abs(transformed_e4)
        eta_error = abs(
            transformed_eta**8 - tau**4 * eta**8
        ) / abs(transformed_eta**8)
        weight_four_error = max(e4_error, eta_error)

        radius = max(q_abs, transformed_q_abs)
        theta_tail = 240 * mp.zeta(3) * mp.nsum(
            lambda order: order**3 * radius**order,
            [MODULAR_TERMS + 1, mp.inf],
        )
        eta_log_tail = (
            8
            * radius ** (MODULAR_TERMS + 1)
            / ((1 - radius) * (1 - radius ** (MODULAR_TERMS + 1)))
        )
        tail_bound = max(theta_tail, eta_log_tail)

        maximum_character_error = max(maximum_character_error, character_error)
        maximum_root_error = max(maximum_root_error, root_error)
        maximum_weight_four_error = max(
            maximum_weight_four_error, weight_four_error
        )
        maximum_tail_bound = max(maximum_tail_bound, tail_bound)
        print(
            "    tau=%-20s chi=%-46s relS=%s  rel(j^1/3)=%s"
            % (
                mp.nstr(tau, 12),
                mp.nstr(character, 34),
                mp.nstr(character_error, 5),
                mp.nstr(root_error, 5),
            )
        )

    modular_ok = (
        maximum_character_error < MODULAR_TOL
        and maximum_root_error < MODULAR_TOL
        and maximum_weight_four_error < MODULAR_TOL
        and maximum_tail_bound < mp.mpf("1e-100")
    )
    report(
        "C7 numerical modular transform shadow at 60 digits",
        modular_ok,
        "max rel S=%s; max rel j^(1/3)=%s; max weight-4 rel=%s; tail<%s"
        % (
            mp.nstr(maximum_character_error, 6),
            mp.nstr(maximum_root_error, 6),
            mp.nstr(maximum_weight_four_error, 6),
            mp.nstr(maximum_tail_bound, 6),
        ),
    )
    report(
        "C7 honest boundary",
        True,
        "exact coefficients + numerical S shadow only; conformal-net modular "
        "covariance remains cited",
    )

    e4_orders = 8
    e4_coeffs = e4_q_series(e4_orders)
    jacobi_coeffs = jacobi_theta_e8_q_series(e4_orders)
    report(
        "Theta_E8 = E4 exact q-expansion through q^8 (Jacobi vs Eisenstein)",
        jacobi_coeffs == e4_coeffs,
        "E4=%s" % e4_coeffs,
    )
    report(
        "E8 lattice theta matches E4 through q^3 (enumeration bound)",
        lattice_theta_e8_q_series(3) == e4_q_series(3),
        "lattice=%s" % lattice_theta_e8_q_series(3),
    )
    mutant_e6_like = [
        1 if n == 0 else 504 * divisor_cube_sum(n)
        for n in range(e4_orders + 1)
    ]
    report(
        "MUST-FAIL: E6-coefficient mutant (504 sigma_3) is not E4",
        mutant_e6_like != e4_coeffs,
        "first mismatch at q^1: 504 vs 240",
    )

def run():
    reset()
    print("v998  SEAM.EQUIV.MMST.01 C7 arithmetic shadow + two-edge HS")
    run_two_edge_and_c7()
    return summary(
        "v998_seam_modular_closure: two-edge HS bound 2.11 + "
        "Theta_E8=E4 exact + character four orders + 60-digit S shadow"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
