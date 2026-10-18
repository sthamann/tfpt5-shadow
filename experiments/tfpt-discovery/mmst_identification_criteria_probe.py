#!/usr/bin/env python3
"""mmst_identification_criteria_probe -- EXPLORATION ONLY.

Purpose
-------
Turn the remaining MMST identification

    QWZ free-fermion edge scaling limit = the (E8)_1 sector theory

into the smallest executable sufficient-criterion checklist.  The cited
operator-algebraic inputs are Osborne--Stottmeister, CMP 398 (2023) 219
(arXiv:2107.13834), in the MMST renormalisation framework
(arXiv:2010.11121).  OS23 proves the free-fermion/Virasoro and bilinear
current limits, but not the mu4/GSO spin-field extension.  Accordingly:

  C1 EXECUTED  one QWZ boundary has c=1/2 per Majorana from the interval
     entropy coefficient; 16 copies give c=8.
  C2 EXECUTED  the QWZ edge branch is linear with v=1 (lattice units)
     and its first four NS levels approach r=1/2,3/2,5/2,7/2; the even
     single-Majorana Fock degeneracies begin 1,0,1,1,2.
  C3 EXECUTED  finite-mode NS/R character sums and the mu4/GSO selector
     O+S give [1,0,248,0,4124,...] on the q^(1/2) grid.
  C4 EXECUTED  the edge two-point amplitude gives the level-one current
     normalisation by Wick contraction.
  C5 EXECUTED  four SO(16)_1 sectors recombine to one projected E8
     sector; det D8=4 and det E8=1 exactly.
  C6 CITED/REDUCED  strong operator convergence on the finite-energy
     core (OS23 for bilinears; the spin-field implementer leg is reduced
     by psi_lambda_lemma_reduction_probe.py, not re-proved here).
  C7 CITED  modular covariance/invariance of the completed extension.

The entropy instrument is stated without hiding its factors.  The scalar
edge band is a complex two-endpoint interval.  A BdG Majorana is one half
of that complex mode and the requested cylinder cut is one of the two
interval endpoints, hence S_Majorana,one-cut = S_scalar,interval/4.  The
fit is then S=(c/6) log[(L/pi)sin(pi ell/L)]+const.

Firewall: finite QWZ strips and finite character truncations only.  This
does not prove a conformal-net isomorphism, modular invariance, or the
spin-field scaling limit; no status move and no promotion.

Verdict enum: MMST_CRITERIA_{N}_OF_{M}_EXECUTED.
"""

from __future__ import annotations

from math import comb, pi

import numpy as np


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

ok_all = True


def rep(name: str, ok: bool, detail: str = "") -> None:
    global ok_all
    ok_all &= bool(ok)
    suffix = "  | " + detail if detail else ""
    print(("PASS " if ok else "FAIL ") + name + suffix)


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
    log_chord = np.log(
        (length / pi) * np.sin(pi * ells / length)
    )
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


def so16_characters() -> dict[str, list[int]]:
    """Finite products on the t=q^(1/2) grid, enough for q^5."""
    plus = [1] + [0] * MAX_T_POWER
    minus = plus.copy()
    for power in range(1, MAX_T_POWER + 1, 2):
        plus = polynomial_multiply(
            plus, fermion_factor(power, +1, N_MAJORANA)
        )
        minus = polynomial_multiply(
            minus, fermion_factor(power, -1, N_MAJORANA)
        )
    vacuum = [(a + b) // 2 for a, b in zip(plus, minus)]
    vector = [(a - b) // 2 for a, b in zip(plus, minus)]

    spinor = [0] * (MAX_T_POWER + 1)
    spinor[2] = 2 ** (N_MAJORANA // 2 - 1)
    for power in range(2, MAX_T_POWER + 1, 2):
        spinor = polynomial_multiply(
            spinor, fermion_factor(power, +1, N_MAJORANA)
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


print("=" * 78)
print("MMST IDENTIFICATION -- minimal 7-criterion chain")
print("=" * 78)

# C1: entropy central charge.
c_fits = []
for length in L_ENTROPY:
    c_fit, entropy_r2 = entropy_c_fit(length)
    c_fits.append(c_fit)
    print(
        "  entropy L=%3d: c_Majorana=%.6f  R^2=%.8f"
        % (length, c_fit, entropy_r2)
    )
c_single = c_fits[-1]
c_carrier = N_MAJORANA * c_single
c1 = (
    abs(c_single - 0.5) < 0.015
    and abs(c_carrier - 8.0) < 0.25
    and max(c_fits) - min(c_fits) < 0.01
)
rep(
    "C1 EXECUTED central charge",
    c1,
    "c_single=%.6f; 16*c=%.6f; convention S_M,1cut=S_scalar/4"
    % (c_single, c_carrier),
)

# C2: velocity, NS levels, and first vacuum-character degeneracies.
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
c2 = (
    abs(abs(velocity) - 1.0) < 0.03
    and velocity_r2 > 0.999
    and np.max(np.abs(scaled_levels - expected_levels)) < 0.04
    and level_degeneracies == [1, 0, 1, 1, 2]
    and float(np.min(localisations[near])) > 0.99
)
rep(
    "C2 EXECUTED velocity + Virasoro spectrum shadow",
    c2,
    "v=%.6f R2=%.7f; scaled=%s; deg=%s"
    % (
        velocity,
        velocity_r2,
        [round(float(value), 6) for value in scaled_levels],
        level_degeneracies,
    ),
)

# C3: four finite-mode characters and GSO projection.
characters = so16_characters()
e8_projected = [
    characters["O"][i] + characters["S"][i]
    for i in range(MAX_T_POWER + 1)
]
e8_expected = [1, 0, 248, 0, 4124, 0, 34752, 0, 213126]
c3 = e8_projected[:9] == e8_expected
rep(
    "C3 EXECUTED NS/R character + mu4/GSO projection",
    c3,
    "O(q): %s; S(q): %s; O+S on t=q^1/2: %s"
    % (
        characters["O"][::2][:5],
        characters["S"][::2][:5],
        e8_projected[:9],
    ),
)

# C4: current two-point normalisation from the same extracted branch.
correlation = edge_correlation(ks, energies)
odd_separations = np.arange(1, L_SPECTRUM // 8, 2)
amplitudes = []
for separation in odd_separations:
    chord = (
        L_SPECTRUM
        / pi
        * np.sin(pi * separation / L_SPECTRUM)
    )
    # Majorana/Nambu normalisation is one half of the scalar band.
    amplitudes.append(
        0.5 * abs(correlation[0, separation]) * chord
    )
majorana_amplitude = float(np.mean(amplitudes))
amplitude_spread = float(np.std(amplitudes))
current_level = (2 * pi * majorana_amplitude) ** 2
c4 = (
    abs(majorana_amplitude - 1 / (2 * pi)) < 1e-10
    and abs(current_level - 1.0) < 1e-10
    and amplitude_spread < 1e-10
)
rep(
    "C4 EXECUTED current-algebra two-point normalisation",
    c4,
    "A_psi=%.12f target=1/(2pi); Wick level k=(2pi A)^2=%.12f"
    % (majorana_amplitude, current_level),
)

# C5: exact sector/mu-index shadow.
d8_edges = tuple((i, i + 1) for i in range(6)) + ((5, 7),)
e8_edges = tuple((i, i + 1) for i in range(6)) + ((2, 7),)
det_d8 = bareiss_determinant(cartan(8, d8_edges))
det_e8 = bareiss_determinant(cartan(8, e8_edges))
nonzero_sector_heads = {
    name: next(i for i, value in enumerate(series) if value)
    for name, series in characters.items()
}
c5 = (
    det_d8 == 4
    and det_e8 == 1
    and set(characters) == {"O", "V", "S", "C"}
    and nonzero_sector_heads == {"O": 0, "V": 1, "S": 2, "C": 2}
)
rep(
    "C5 EXECUTED four sectors -> mu-index-one lattice shadow",
    c5,
    "heads(t)=%s; det(D8)=%d -> det(E8)=%d; selector O+S"
    % (nonzero_sector_heads, det_d8, det_e8),
)

criteria = [
    ("C1", "central charge match", "EXECUTED", c1),
    ("C2", "velocity and conformal spectrum", "EXECUTED", c2),
    ("C3", "vacuum character / partition sum", "EXECUTED", c3),
    ("C4", "current two-point normalisation", "EXECUTED", c4),
    ("C5", "sector count / mu-index shadow", "EXECUTED", c5),
    (
        "C6",
        "operator convergence on finite-energy core",
        "CITED/REDUCED",
        None,
    ),
    ("C7", "modular invariance of completed extension", "CITED", None),
]

print()
print("CRITERIA TABLE")
for code, criterion, status, passed in criteria:
    measured = "-" if passed is None else ("PASS" if passed else "FAIL")
    print("  %-3s  %-45s %-14s %s" % (code, criterion, status, measured))

executed = sum(
    status == "EXECUTED" and bool(passed)
    for _, _, status, passed in criteria
)
total = len(criteria)
verdict = "MMST_CRITERIA_%d_OF_%d_EXECUTED" % (executed, total)

print()
print("CITED BOUNDARY")
print("  C6: OS23 strong limits cover Virasoro and SO(16)_1 bilinears;")
print("      the odd spin-field implementer is reduced to cited quasi-free")
print("      continuity plus measured Cauchy data, not proved here.")
print("  C7: modular invariance/covariance of the completed mu4/GSO")
print("      extension remains cited; finite q-coefficients are not that theorem.")
print()
print("VERDICT: " + verdict)
print("PROBE " + ("ALL PASS" if ok_all else "HAS FINDINGS/FAILURES"))
raise SystemExit(0 if ok_all else 1)
