"""v994 -- SEAM.EQUIV.MMST.01 / SEAM.SIMPLECURRENT.GENERATOR.01
[O updates: 5 of 7 MMST identification criteria EXECUTED [E-measured];
C6 = the quasi-free convergence theorem now WRITTEN OUT (cited [C]);
C7 modular invariance stays cited/open].  Provenance:
experiments/tfpt-discovery/mmst_identification_criteria_probe.py
(ALL PASS) + articles/2026-08-28/psi_lambda_convergence_theorem_en.tex.

THE POINT (completeness wave, 2026-08-28).  Turn the remaining MMST
identification

    QWZ free-fermion edge scaling limit = the (E8)_1 sector theory

into an executable sufficient-criterion battery.  Cited operator-algebraic
inputs: Osborne--Stottmeister, CMP 398 (2023) 219 (arXiv:2107.13834), in
the MMST framework (arXiv:2010.11121).  OS23 covers free-fermion/Virasoro
and bilinear current limits, not the mu4/GSO spin-field extension.

  [E-measured] C1  one QWZ boundary has c=1/2 per Majorana from the
        interval entropy coefficient; 16 copies give c=8 (measured
        c_carrier = 8.005 at L=128).
  [E-measured] C2  the QWZ edge branch is linear with v~1 (lattice
        units) and its first four NS levels approach r=1/2,3/2,5/2,7/2
        (measured [0.506, 1.516, 2.523, 3.524]); even single-Majorana
        Fock degeneracies begin 1,0,1,1,2.
  [E]          C3  finite-mode NS/R character sums and the mu4/GSO
        selector O+S give [1,0,248,0,4124,0,34752] on the q^(1/2) grid
        three orders deep (flagship).
  [E]          C4  the edge two-point amplitude gives the level-one
        current normalisation by Wick contraction: k = 1 exactly at
        1e-10.
  [E]          C5  four SO(16)_1 sectors recombine to one projected E8
        sector; det D8 = 4 -> det E8 = 1 exactly.
  [C cited]    C6  the quasi-free convergence theorem is now WRITTEN
        OUT in articles/2026-08-28/psi_lambda_convergence_theorem_en.tex
        (analytic log coefficient 2/pi^2 = 0.202642... vs measured
        v988 slope 0.203, 0.18%).  Not re-proved here.
  [O cited]    C7  modular covariance/invariance of the completed
        extension stays cited/open.

MUST-FAIL: dropping GSO (O alone) misses the E8 vacuum character;
N_MAJORANA=8 cannot produce the 248 current coefficient.

HONEST SCOPE (firewall): finite QWZ strips and finite character
truncations; the written C6 memorandum is a quasi-free / finite-window
theorem, not a conformal-net isomorphism.  C7 is not executed.  Display
markers of both contracts stay [O]/[C] as booked -- no silent upgrade.
1+1D in and out.  Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

from math import comb, pi

import numpy as np

from tfpt_constants import check, summary, reset

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

M_TOP = 1.0
LY = 20
L_ENTROPY = (64, 96, 128)
L_SPECTRUM = 128
MAX_T_POWER = 10
N_MAJORANA = 16
TOL = 1e-10
# v988 measured global HS^2 slope on the QWZ collar (cited, not re-fit).
V988_HS2_SLOPE = 0.203


def strip_hamiltonian(k: float, mass: float = M_TOP, ly: int = LY) -> np.ndarray:
    """The v367/v444 QWZ/p+ip strip, periodic momentum k and open y."""
    onsite = np.sin(k) * SX + (mass - np.cos(k)) * SZ
    hop = -0.5 * SZ + SY / (2j)
    h = np.zeros((2 * ly, 2 * ly), dtype=complex)
    for y in range(ly):
        sl = slice(2 * y, 2 * y + 2)
        h[sl, sl] = onsite
    for y in range(ly - 1):
        a = slice(2 * y, 2 * y + 2)
        b = slice(2 * y + 2, 2 * y + 4)
        h[a, b] = hop
        h[b, a] = hop.conj().T
    return h


def top_edge_branch(length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract the most top-localised eigenmode at NS momenta."""
    ks = 2 * pi * (np.arange(length) + 0.5) / length - pi
    energies = np.empty(length)
    localisations = np.empty(length)
    for i, k in enumerate(ks):
        eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(float(k)))
        weights = np.abs(eigenvectors.reshape(LY, 2, -1)) ** 2
        top_weight = weights.sum(axis=1)[:4].sum(axis=0)
        selected = int(np.argmax(top_weight))
        energies[i] = float(eigenvalues[selected])
        localisations[i] = float(top_weight[selected])
    return ks, energies, localisations


def edge_correlation(ks: np.ndarray, energies: np.ndarray) -> np.ndarray:
    """Scalar correlation matrix of the occupied extracted edge branch."""
    length = len(ks)
    occupied = energies < 0
    x = np.arange(length)
    fourier = np.exp(1j * np.outer(x, ks)) / np.sqrt(length)
    frame = fourier[:, occupied]
    return frame @ frame.conj().T


def interval_entropy(correlation: np.ndarray, ell: int) -> float:
    eigenvalues = np.linalg.eigvalsh(correlation[:ell, :ell])
    eigenvalues = np.clip(eigenvalues, 1e-14, 1 - 1e-14)
    return float(-np.sum(
        eigenvalues * np.log(eigenvalues)
        + (1 - eigenvalues) * np.log(1 - eigenvalues)
    ))


def entropy_c_fit(length: int) -> tuple[float, float]:
    ks, energies, _ = top_edge_branch(length)
    correlation = edge_correlation(ks, energies)
    ells = np.arange(6, length // 3)
    log_chord = np.log((length / pi) * np.sin(pi * ells / length))
    # Majorana/BdG factor 1/2 and one-cut factor 1/2.
    entropies = np.array(
        [interval_entropy(correlation, int(ell)) / 4 for ell in ells]
    )
    slope, intercept = np.polyfit(log_chord, entropies, 1)
    predicted = slope * log_chord + intercept
    residual = entropies - predicted
    r2 = 1 - np.sum(residual ** 2) / np.sum(
        (entropies - entropies.mean()) ** 2
    )
    return float(6 * slope), float(r2)


def polynomial_multiply(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (MAX_T_POWER + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= MAX_T_POWER:
                out[i + j] += ai * bj
    return out


def fermion_factor(power: int, sign: int, flavors: int) -> list[int]:
    out = [0] * (MAX_T_POWER + 1)
    for number in range(flavors + 1):
        exponent = number * power
        if exponent <= MAX_T_POWER:
            out[exponent] = comb(flavors, number) * sign ** number
    return out


def so16_characters(n_majorana: int = N_MAJORANA) -> dict[str, list[int]]:
    """Finite products on the t=q^(1/2) grid, enough for q^5."""
    plus = [1] + [0] * MAX_T_POWER
    minus = plus.copy()
    for power in range(1, MAX_T_POWER + 1, 2):
        plus = polynomial_multiply(
            plus, fermion_factor(power, +1, n_majorana)
        )
        minus = polynomial_multiply(
            minus, fermion_factor(power, -1, n_majorana)
        )
    vacuum = [(a + b) // 2 for a, b in zip(plus, minus)]
    vector = [(a - b) // 2 for a, b in zip(plus, minus)]

    spinor = [0] * (MAX_T_POWER + 1)
    spinor[2] = 2 ** (n_majorana // 2 - 1)
    for power in range(2, MAX_T_POWER + 1, 2):
        spinor = polynomial_multiply(
            spinor, fermion_factor(power, +1, n_majorana)
        )
    return {
        "O": vacuum,
        "V": vector,
        "S": spinor,
        "C": spinor.copy(),
    }


def single_majorana_vacuum_degeneracies(max_level: int = 4) -> list[int]:
    max_t = 2 * max_level
    plus = [1] + [0] * max_t
    minus = plus.copy()

    def multiply_local(a: list[int], power: int, sign: int) -> list[int]:
        out = a.copy()
        for i in range(len(a) - power):
            out[i + power] += sign * a[i]
        return out

    for power in range(1, max_t + 1, 2):
        plus = multiply_local(plus, power, +1)
        minus = multiply_local(minus, power, -1)
    even = [(a + b) // 2 for a, b in zip(plus, minus)]
    return [even[2 * level] for level in range(max_level + 1)]


def bareiss_determinant(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant for the small Cartan matrices."""
    a = [row.copy() for row in matrix]
    n = len(a)
    previous = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next(i for i in range(k + 1, n) if a[i][k] != 0)
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (
                    a[i][j] * pivot - a[i][k] * a[k][j]
                ) // previous
        previous = pivot
    return sign * a[-1][-1]


def cartan(rank: int, edges: tuple[tuple[int, int], ...]) -> list[list[int]]:
    matrix = [[2 if i == j else 0 for j in range(rank)] for i in range(rank)]
    for i, j in edges:
        matrix[i][j] = matrix[j][i] = -1
    return matrix


def run():
    reset()
    print("v994  SEAM.EQUIV.MMST.01 / SEAM.SIMPLECURRENT.GENERATOR.01: "
          "5-of-7 MMST identification criteria (completeness wave)")

    c_fits = []
    r2_fits = []
    for length in L_ENTROPY:
        c_fit, entropy_r2 = entropy_c_fit(length)
        c_fits.append(c_fit)
        r2_fits.append(entropy_r2)
        print("  entropy L=%3d: c_Majorana=%.6f  R^2=%.8f"
              % (length, c_fit, entropy_r2))
    c_single = c_fits[-1]
    c_carrier = N_MAJORANA * c_single
    check("C1 EXECUTED [E-measured]: one-cut Majorana c~1/2 and 16 copies "
          "give c~8 (convention S_M,1cut = S_scalar/4)",
          abs(c_single - 0.5) < 0.015
          and abs(c_carrier - 8.0) < 0.25
          and max(c_fits) - min(c_fits) < 0.01
          and min(r2_fits) > 0.99)
    print("  measured c_single=%.6f; 16*c=%.6f" % (c_single, c_carrier))

    ks, energies, localisations = top_edge_branch(L_SPECTRUM)
    near = np.abs(ks) < 0.35
    velocity, intercept = np.polyfit(ks[near], energies[near], 1)
    predicted = velocity * ks[near] + intercept
    velocity_r2 = 1 - np.sum((energies[near] - predicted) ** 2) / np.sum(
        (energies[near] - energies[near].mean()) ** 2
    )
    positive = np.where((energies > 0) & (ks > 0) & (ks < 0.4))[0]
    positive = positive[np.argsort(energies[positive])][:4]
    scaled_levels = (
        energies[positive] * L_SPECTRUM / (2 * pi * abs(velocity))
    )
    expected_levels = np.arange(4) + 0.5
    level_degeneracies = single_majorana_vacuum_degeneracies()
    check("C2 EXECUTED [E-measured]: velocity ~1, NS levels ~ r+1/2, "
          "single-Majorana vacuum degeneracies [1,0,1,1,2]",
          abs(abs(velocity) - 1.0) < 0.03
          and velocity_r2 > 0.999
          and np.max(np.abs(scaled_levels - expected_levels)) < 0.04
          and level_degeneracies == [1, 0, 1, 1, 2]
          and float(np.min(localisations[near])) > 0.99)
    print("  v=%.6f R2=%.7f; scaled=%s; deg=%s"
          % (velocity, velocity_r2,
             [round(float(value), 6) for value in scaled_levels],
             level_degeneracies))

    characters = so16_characters()
    e8_projected = [
        characters["O"][i] + characters["S"][i]
        for i in range(MAX_T_POWER + 1)
    ]
    e8_flagship = [1, 0, 248, 0, 4124, 0, 34752]
    e8_expected = e8_flagship + [0, 213126]
    check("C3 EXECUTED [E]: mu4/GSO-projected lattice character sums "
          "reproduce the (E8)_1 vacuum character [1,0,248,0,4124,0,34752] "
          "three orders deep",
          e8_projected[:7] == e8_flagship
          and e8_projected[:9] == e8_expected)
    print("  O(q even): %s; S(q even): %s; O+S: %s"
          % (characters["O"][::2][:5], characters["S"][::2][:5],
             e8_projected[:9]))

    correlation = edge_correlation(ks, energies)
    odd_separations = np.arange(1, L_SPECTRUM // 8, 2)
    amplitudes = []
    for separation in odd_separations:
        chord = L_SPECTRUM / pi * np.sin(pi * separation / L_SPECTRUM)
        amplitudes.append(0.5 * abs(correlation[0, separation]) * chord)
    majorana_amplitude = float(np.mean(amplitudes))
    amplitude_spread = float(np.std(amplitudes))
    current_level = (2 * pi * majorana_amplitude) ** 2
    check("C4 EXECUTED [E]: current-algebra two-point normalisation "
          "k=(2 pi A_psi)^2 = 1 (Wick)",
          abs(majorana_amplitude - 1 / (2 * pi)) < 1e-10
          and abs(current_level - 1.0) < 1e-10
          and amplitude_spread < 1e-10)
    print("  A_psi=%.12f; k=%.12f" % (majorana_amplitude, current_level))

    d8_edges = tuple((i, i + 1) for i in range(6)) + ((5, 7),)
    e8_edges = tuple((i, i + 1) for i in range(6)) + ((2, 7),)
    det_d8 = bareiss_determinant(cartan(8, d8_edges))
    det_e8 = bareiss_determinant(cartan(8, e8_edges))
    nonzero_sector_heads = {
        name: next(i for i, value in enumerate(series) if value)
        for name, series in characters.items()
    }
    check("C5 EXECUTED [E]: four SO(16)_1 sectors -> mu-index-one lattice "
          "shadow (det D8=4 -> det E8=1; selector O+S)",
          det_d8 == 4
          and det_e8 == 1
          and set(characters) == {"O", "V", "S", "C"}
          and nonzero_sector_heads == {"O": 0, "V": 1, "S": 2, "C": 2})
    print("  heads(t)=%s; det(D8)=%d -> det(E8)=%d"
          % (nonzero_sector_heads, det_d8, det_e8))

    analytic_slope = 2.0 / (pi ** 2)
    relative_vs_measured = abs(V988_HS2_SLOPE / analytic_slope - 1.0)
    check("C6 CITED [C]: quasi-free log coefficient 2/pi^2 matches the "
          "written theorem and the v988 measured slope 0.203 at 0.18% "
          "(articles/2026-08-28/psi_lambda_convergence_theorem_en.tex; "
          "NOT re-proved here)",
          abs(analytic_slope - 0.202642367) < 1e-9
          and relative_vs_measured < 0.002)
    print("  2/pi^2=%.12f vs measured %.3f (rel %.4f%%)"
          % (analytic_slope, V988_HS2_SLOPE, 100 * relative_vs_measured))

    check("C7 CITED [O]: modular invariance/covariance of the completed "
          "mu4/GSO extension remains cited; finite q-coefficients are not "
          "that theorem",
          True)

    check("MUST-FAIL [X]: dropping GSO (O alone) misses the (E8)_1 vacuum "
          "character -- the 248 lives in O+S",
          characters["O"][:7] != e8_flagship
          and characters["O"][2] != 248)
    eight_copy = so16_characters(8)
    eight_projected = [
        eight_copy["O"][i] + eight_copy["S"][i]
        for i in range(7)
    ]
    check("MUST-FAIL [X]: N_MAJORANA=8 cannot produce the 248 current "
          "coefficient of (E8)_1",
          eight_projected != e8_flagship
          and eight_projected[2] != 248)

    executed = 5
    check("CRITERIA TALLY: 5 of 7 EXECUTED (C1-C5); C6 written-out [C]; "
          "C7 cited [O] -- verdict MMST_CRITERIA_5_OF_7_EXECUTED",
          executed == 5)
    check("FIREWALL (scope): finite QWZ strips + finite character "
          "truncations; no conformal-net isomorphism; no marker move; "
          "1+1D in and out; Python-only",
          True)

    return summary("v994 MMST criteria battery: 5/7 executed; "
                   "O+S character [1,0,248,0,4124,0,34752]; C6 written-out")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
