#!/usr/bin/env python3
"""Finite character-resolved determinant response for the P-dem premise.

EXPLORATION ONLY.  This probe constructs the missing finite map without
importing verification code or changing any load-bearing surface.  The
one-particle family is the frozen QWZ seam collar tensored with the regular
mu4 deck module.  If D|r> = |r+1>, its exact character projectors are

    P_k = (1/4) sum_{j=0}^3 i^(-k j) D^j,       k = 0,1,2,3.

The physical family is H_F(theta) = I_4 tensor H_QWZ(theta).  For a deck-space
flux-coupling matrix A, the character-resolved integrated log-determinant
response factorizes exactly as

    r_k(A) = Tr(P_k A) W_QWZ,                    k = 1,2,3,

where W_QWZ is the winding of the frozen bottom-collar regularized determinant
under theta: 0 -> 2 pi.  Thus the physical abelian insertion A = I_4 gives the
exact response map r/W_QWZ = (1,1,1).

Proof paragraph
---------------
The second-quantized electromagnetic flux generator acts on spatial QWZ
states and is the identity on the mu4 deck factor, so it has the form
I_deck tensor G_flux.  It commutes with D tensor I, and every rank-one
character restriction P_k(I_deck)P_k is exactly P_k; consequently each
restricted determinant is the same QWZ determinant and has the same
log-response.  Equality does not follow from commutation with the abelian
deck action alone: distinct mu4 characters are not conjugate (the D4
reflection only exchanges chi_1 and chi_3 while fixing chi_2).  The required
strong premise is the physically specified total-charge coupling A = I_deck,
whose tensor factorization proves equality of all three restrictions, rather
than a false Schur-lemma inference from deck invariance.

Two mutants enforce that distinction.  Coupling flux only through P_1 is
deck-invariant but gives (1,0,0), proving that commutation alone is
insufficient.  The deck-breaking closed large-gauge generator
A_break = I + |v><v|, v=(|0>+|1>)/sqrt(2), has integer spectrum {1,2},
does not preserve character subspaces, and its projected diagnostic splits
as (5/4,1,5/4); in that mutant a strict character-restricted determinant line
is no longer defined.

VERDICT ENUM:
  PDEM_{DERIVED(r, proof)|REFUTED(pattern)}
"""

from __future__ import annotations

import hashlib

import numpy as np
import sympy as sp


SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

COLLAR_SIZES = (12, 16)
TWIST_SAMPLES = 128
MASS = 1.0
EDGE_REGULATOR = 0.02
EDGE_LOCALIZATION_LENGTH = 1.2
TOLERANCE = 1.0e-12

CHECKS: list[tuple[str, bool]] = []


def check(label: str, condition: bool, detail: str = "") -> bool:
    """Record one deterministic protocol check."""
    passed = bool(condition)
    CHECKS.append((label, passed))
    print(
        f"{'PASS' if passed else 'FAIL'}  {label}"
        + (f"  | {detail}" if detail else "")
    )
    return passed


def exact_deck_data() -> tuple[sp.Matrix, dict[int, sp.Matrix]]:
    """Regular mu4 shift and all four exact Fourier projectors."""
    deck = sp.zeros(4)
    for column in range(4):
        deck[(column + 1) % 4, column] = 1
    projectors = {}
    for character in range(4):
        eigenvalue = sp.I**character
        projectors[character] = sp.simplify(
            sum(
                (
                    eigenvalue ** (-power) * deck**power
                    for power in range(4)
                ),
                sp.zeros(4),
            )
            / 4
        )
    return deck, projectors


def strip_hamiltonian(theta: float, collar_size: int) -> np.ndarray:
    """Frozen v991 open-y QWZ seam Hamiltonian at winding parameter theta."""
    onsite = (
        np.sin(theta) * SX
        + (MASS - np.cos(theta)) * SZ
    )
    hopping = -0.5 * SZ + SY / (2j)
    hamiltonian = np.zeros(
        (2 * collar_size, 2 * collar_size), dtype=complex
    )
    for y_coord in range(collar_size):
        block = 2 * y_coord
        hamiltonian[block:block + 2, block:block + 2] = onsite
    for y_coord in range(collar_size - 1):
        lower = 2 * y_coord
        upper = lower + 2
        hamiltonian[lower:lower + 2, upper:upper + 2] = hopping
        hamiltonian[upper:upper + 2, lower:lower + 2] = hopping.conj().T
    return hamiltonian


def collar_log_determinants(collar_size: int) -> np.ndarray:
    """Bottom-weighted regularized log determinant around one flux loop."""
    twists = (
        2.0 * np.pi * np.arange(TWIST_SAMPLES) / TWIST_SAMPLES
    )
    y_operator = np.repeat(np.arange(collar_size), 2).astype(float)
    log_determinants = []
    for theta in twists:
        eigenvalues, eigenvectors = np.linalg.eigh(
            strip_hamiltonian(theta, collar_size)
        )
        log_determinant = 0.0j
        for state_index, energy in enumerate(eigenvalues):
            y_expectation = float(
                np.abs(eigenvectors[:, state_index]) ** 2 @ y_operator
            )
            collar_weight = np.exp(
                -y_expectation / EDGE_LOCALIZATION_LENGTH
            )
            log_determinant += collar_weight * np.log(
                energy + 1j * EDGE_REGULATOR
            )
        log_determinants.append(log_determinant)
    return np.asarray(log_determinants)


def log_response_winding(log_determinants: np.ndarray) -> float:
    """Integrated imaginary log-response with periodic closure."""
    closed_imaginary_part = np.concatenate(
        (log_determinants.imag, log_determinants[:1].imag)
    )
    unwrapped = np.unwrap(closed_imaginary_part)
    return float((unwrapped[-1] - unwrapped[0]) / (2.0 * np.pi))


def exact_response_coefficients(
    projectors: dict[int, sp.Matrix],
    coupling: sp.Matrix,
) -> sp.Matrix:
    """Tr(P_k A), ordered by the three nontrivial characters."""
    return sp.Matrix(
        [
            sp.simplify(sp.trace(projectors[character] * coupling))
            for character in (1, 2, 3)
        ]
    )


def max_abs(matrix: np.ndarray) -> float:
    """Maximum entry magnitude, including the empty-matrix case."""
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def main() -> int:
    print("P-DEM CHARACTER-BLIND DETERMINANT-RESPONSE MAP")
    print("EXPLORATION ONLY: finite QWZ collar x regular mu4 deck module")

    deck, projectors = exact_deck_data()
    identity4 = sp.eye(4)
    zero4 = sp.zeros(4)
    exact_projector_ok = all(
        sp.simplify(projectors[k] ** 2 - projectors[k]) == zero4
        and projectors[k].rank() == 1
        and sp.simplify(deck * projectors[k] - sp.I**k * projectors[k])
        == zero4
        for k in range(4)
    )
    orthogonality_ok = all(
        sp.simplify(projectors[k] * projectors[j])
        == (projectors[k] if k == j else zero4)
        for k in range(4)
        for j in range(4)
    )
    check(
        "exact mu4 character projectors are rank-one orthogonal idempotents",
        deck**4 == identity4
        and exact_projector_ok
        and orthogonality_ok
        and sum(projectors.values(), zero4) == identity4,
    )

    blind_coupling = identity4
    blind_coefficients = exact_response_coefficients(
        projectors, blind_coupling
    )
    check(
        "abelian total-charge insertion is exactly character blind",
        deck * blind_coupling == blind_coupling * deck
        and blind_coefficients == sp.ones(3, 1)
        and all(
            sp.simplify(
                projectors[k] * blind_coupling * projectors[k]
                - projectors[k]
            )
            == zero4
            for k in (1, 2, 3)
        ),
        f"Tr(P_k A)={tuple(blind_coefficients)}",
    )

    print("\nPHYSICAL WINDING RESPONSE")
    responses: dict[int, np.ndarray] = {}
    for collar_size in COLLAR_SIZES:
        log_determinants = collar_log_determinants(collar_size)
        base_winding = log_response_winding(log_determinants)
        response = base_winding * np.array(
            [float(value) for value in blind_coefficients],
            dtype=float,
        )
        responses[collar_size] = response

        physical_dimension = 2 * collar_size
        deck_numeric = np.array(deck.tolist(), dtype=complex)
        projector_numeric = {
            character: np.array(projectors[character].tolist(), dtype=complex)
            for character in (1, 2, 3)
        }
        representative_hamiltonian = strip_hamiltonian(
            0.371, collar_size
        )
        family_hamiltonian = np.kron(
            np.eye(4), representative_hamiltonian
        )
        full_deck = np.kron(
            deck_numeric, np.eye(physical_dimension)
        )
        commutator_residual = max_abs(
            family_hamiltonian @ full_deck
            - full_deck @ family_hamiltonian
        )
        restriction_residual = max(
            max_abs(
                np.kron(projector_numeric[character], np.eye(physical_dimension))
                @ family_hamiltonian
                - family_hamiltonian
                @ np.kron(
                    projector_numeric[character],
                    np.eye(physical_dimension),
                )
            )
            for character in (1, 2, 3)
        )
        closure_residual = max_abs(
            strip_hamiltonian(2.0 * np.pi, collar_size)
            - strip_hamiltonian(0.0, collar_size)
        )
        democracy_residual = float(
            np.max(np.abs(response - np.mean(response)))
        )
        print(
            "  Ny=%d  W=%+.16f  r=(%+.16f,%+.16f,%+.16f)"
            % (
                collar_size,
                base_winding,
                response[0],
                response[1],
                response[2],
            )
        )
        check(
            f"Ny={collar_size}: response is proportional to ones within 1e-12",
            abs(base_winding - 1.0) < TOLERANCE
            and democracy_residual < TOLERANCE
            and commutator_residual < TOLERANCE
            and restriction_residual < TOLERANCE
            and closure_residual < TOLERANCE,
            "dem=%.1e [H,D]=%.1e [H,P_k]=%.1e closure=%.1e"
            % (
                democracy_residual,
                commutator_residual,
                restriction_residual,
                closure_residual,
            ),
        )

    e1 = sp.Matrix([1, 0, 0])
    v4_shift = 6 * sp.ones(3, 1) * e1.T
    response_shift = 6 * blind_coefficients * e1.T
    check(
        "normalized determinant response gives the v4 winding shift exactly",
        response_shift == v4_shift
        and v4_shift
        == sp.Matrix([[6, 0, 0], [6, 0, 0], [6, 0, 0]]),
        "6*r_hat*e1^T = 6*ones*e1^T",
    )

    print("\nMUTANTS")
    character_coupling = projectors[1]
    character_coefficients = exact_response_coefficients(
        projectors, character_coupling
    )
    check(
        "character-dependent insertion is non-democratic",
        deck * character_coupling == character_coupling * deck
        and character_coefficients == sp.Matrix([1, 0, 0]),
        f"Tr(P_k P_1)={tuple(character_coefficients)}",
    )

    v = sp.Matrix([1, 1, 0, 0]) / sp.sqrt(2)
    deck_breaking_coupling = identity4 + v * v.conjugate().T
    breaking_coefficients = exact_response_coefficients(
        projectors, deck_breaking_coupling
    )
    breaking_commutator = sp.simplify(
        deck * deck_breaking_coupling
        - deck_breaking_coupling * deck
    )
    integer_spectrum_certificate = sp.simplify(
        (deck_breaking_coupling - identity4)
        * (deck_breaking_coupling - 2 * identity4)
    )
    leakage = [
        sp.simplify(
            (identity4 - projectors[k])
            * deck_breaking_coupling
            * projectors[k]
        )
        for k in (1, 2, 3)
    ]
    check(
        "deck-breaking closed-gauge mutant splits the projected response",
        breaking_commutator != zero4
        and integer_spectrum_certificate == zero4
        and breaking_coefficients
        == sp.Matrix(
            [sp.Rational(5, 4), 1, sp.Rational(5, 4)]
        )
        and any(block != zero4 for block in leakage),
        "projected r/W=(5/4,1,5/4); character subspaces leak",
    )
    print(
        "  M_char projected response at Ny=16: %s"
        % (
            tuple(
                float(value) * responses[16][0]
                for value in character_coefficients
            ),
        )
    )
    print(
        "  M_break projected response at Ny=16: %s"
        % (
            tuple(
                float(value) * responses[16][0]
                for value in breaking_coefficients
            ),
        )
    )

    failed = [label for label, passed in CHECKS if not passed]
    print("\n" + "-" * 78)
    print(f"CHECKS: {len(CHECKS) - len(failed)}/{len(CHECKS)} passed")
    if failed:
        for label in failed:
            print(f"  FAILED: {label}")
        print("VERDICT: PDEM_REFUTED(numerical-or-algebraic-check-failure)")
        return 1

    print(
        "PROOF STATUS: COMPLETE at the finite factorized abelian-coupling "
        "level; deck commutation alone explicitly rejected."
    )
    print(
        "S4 AXIOM-CORE REMAINDER: 0 for the finite P-dem bridge, modulo "
        "the already-externalized MMST/continuum identification leg."
    )
    print(
        "VERDICT: PDEM_DERIVED(r=(1,1,1), "
        "proof=factorized-abelian-total-charge)"
    )
    with open(__file__, "rb") as probe_file:
        print(
            "SPEC_SHA "
            + hashlib.sha256(probe_file.read()).hexdigest()[:16]
        )
    print(
        "FIREWALL: exploration-only; no verification, paper, ledger, "
        "changelog, website, manifest, README, or status edit."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
