#!/usr/bin/env python3
"""v1028 -- exact Gauss residues and a selected-pair-space D4 cap.

The Gauss part uses the full P^12 exterior character of 192 fermion modes,
Higgs and seam factors.  Frobenius reduction in characteristic five is exact:
the one-site Gauss dimension is 3 mod 5, while the open 2x2x2 cube with the
specified nine-irrep link truncation is 0 mod 5.  Its site character retains
all 192 fermion modes.  An independent CAR-signed raising-generator calculation checks the
one-copy singlet conventions with ranks 500 and 1256.

The cap is an ordinary D4 representation only on the pre-existing selected
12-dimensional even one-pair space.  It gives an entangled rank-one ground ray
and an order-five unitary with only two eigenvalues; it is not a D4 action on
the full lifted one-fermion Fock space, not a canonical five-state clock or
Weyl pair, and does not select an orientation.  T6, T8 and TOE remain open.
No observed targets are loaded.  NO RH CLAIM.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
import numpy as np
import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


ZERO = (0, 0, 0, 0)
COLORS = ((1, 0), (0, 1), (-1, -1))
WEIGHTS = tuple(
    [(a, b, weak, 1) for a, b in COLORS for weak in (-1, 1)]
    + [(-a, -b, 0, -4) for a, b in COLORS]
    + [(-a, -b, 0, 2) for a, b in COLORS]
    + [(0, 0, weak, -3) for weak in (-1, 1)]
    + [(0, 0, 0, 6), ZERO]
)
HIGGS = (ZERO, (0, 0, -1, 3), (0, 0, 1, 3))
POSITIVE_ROOTS = ((1, -1, 0, 0), (2, 1, 0, 0),
                  (1, 2, 0, 0), (0, 0, 2, 0))
PATH_EXPECTED = [3, 4, 3, 0, 0, 1, 4, 0, 0, 1, 4, 3,
                 4, 4, 2, 2, 3, 0, 4, 1, 0, 1, 0, 4]


def check(name: str, condition: bool, detail: object = "") -> None:
    label = name if detail == "" else f"{name} -- {detail}"
    suite_check(label, bool(condition))


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a+b for a, b in zip(left, right, strict=True))


def exterior_character(copies: int, modulus: int | None = None) -> dict[tuple[int, ...], int]:
    polynomial = {ZERO: 1}
    for weight in WEIGHTS*copies:
        output = defaultdict(int, polynomial)
        for exponent, coefficient in polynomial.items():
            output[add(exponent, weight)] += coefficient
        polynomial = {
            exponent: coefficient if modulus is None else coefficient % modulus
            for exponent, coefficient in output.items()
            if modulus is None or coefficient % modulus
        }
    return polynomial


def weyl_denominator() -> dict[tuple[int, ...], int]:
    polynomial = {ZERO: 1}
    for root in POSITIVE_ROOTS:
        output = defaultdict(int, polynomial)
        for exponent, coefficient in polynomial.items():
            output[add(exponent, root)] -= coefficient
        polynomial = {exponent: coefficient for exponent, coefficient in output.items() if coefficient}
    return polynomial


def gauss_count(polynomial: dict[tuple[int, ...], int], with_higgs: bool = True) -> int:
    return sum(
        sign*polynomial.get(tuple(-entry for entry in add(root, higgs)), 0)
        for root, sign in weyl_denominator().items()
        for higgs in (HIGGS if with_higgs else (ZERO,))
    )


def frobenius_gauss_count_mod5(polynomial2: dict[tuple[int, ...], int],
                               insertions: tuple[tuple[int, ...], ...] | list[tuple[int, ...]] | None = None) -> int:
    """CT[P^12 I Delta] mod 5 through P^2(z)P^2(z^5)."""
    insertions = HIGGS if insertions is None else insertions
    offsets: dict[tuple[int, ...], int] = defaultdict(int)
    for root, sign in weyl_denominator().items():
        for insertion in insertions:
            offsets[add(root, insertion)] += sign
    residues: dict[tuple[int, ...], list[tuple[tuple[int, ...], int]]] = defaultdict(list)
    for exponent, coefficient in polynomial2.items():
        residues[tuple(entry % 5 for entry in exponent)].append((exponent, coefficient))
    total = 0
    for offset, sign in offsets.items():
        if sign:
            for exponent, coefficient in residues[tuple(-entry % 5 for entry in offset)]:
                second = tuple((-a-b)//5 for a, b in zip(exponent, offset, strict=True))
                total += sign*coefficient*polynomial2.get(second, 0)
    return total % 5


def link_representations() -> dict[str, list[tuple[int, ...]] | tuple[tuple[int, ...], ...]]:
    adjoint3 = [
        add((a, b, 0, 0), (-c, -d, 0, 0))
        for a, b in COLORS for c, d in COLORS if (a, b) != (c, d)
    ] + [ZERO, ZERO]
    return {
        "0": [ZERO], "Q": list(WEIGHTS[:6]), "uc": list(WEIGHTS[6:9]),
        "dc": list(WEIGHTS[9:12]), "L": list(WEIGHTS[12:14]),
        "ec": [WEIGHTS[14]], "H": list(HIGGS[1:]), "Adj3": adjoint3,
        "Adj2": [(0, 0, -2, 0), ZERO, (0, 0, 2, 0)],
    }


def path_transfer(polynomial2: dict[tuple[int, ...], int]) -> tuple[list[str], list[list[int]]]:
    representations = link_representations()
    labels = list(representations)
    matrix = []
    for left in labels:
        row = []
        for right in labels:
            insertion = [
                add(add(higgs, a), tuple(-entry for entry in b))
                for higgs in HIGGS for a in representations[left] for b in representations[right]
            ]
            row.append(frobenius_gauss_count_mod5(polynomial2, insertion))
        matrix.append(row)
    return labels, matrix


def path_counts(matrix: list[list[int]], maximum: int = 24) -> list[int]:
    vector = [1]+[0]*(len(matrix)-1)
    output = []
    for length in range(1, maximum+1):
        vector = [sum(vector[i]*matrix[i][j] for i in range(len(matrix))) % 5
                  for j in range(len(matrix))]
        output.append(pow(4, length, 5)*vector[0] % 5)
    return output


class FullCharacterMod5:
    def __init__(self, polynomial2: dict[tuple[int, ...], int]):
        self.polynomial2 = polynomial2
        self.residues: dict[tuple[int, ...], list[tuple[tuple[int, ...], int]]] = defaultdict(list)
        for exponent, coefficient in polynomial2.items():
            self.residues[tuple(entry % 5 for entry in exponent)].append((exponent, coefficient))

    @lru_cache(maxsize=None)
    def constant_term(self, offset: tuple[int, ...]) -> int:
        total = 0
        for exponent, coefficient in self.residues[tuple(-entry % 5 for entry in offset)]:
            second = tuple((-a-b)//5 for a, b in zip(exponent, offset, strict=True))
            total += coefficient*self.polynomial2.get(second, 0)
        return total % 5

    @lru_cache(maxsize=None)
    def gauss_shift(self, offset: tuple[int, ...]) -> int:
        return sum(
            sign*self.constant_term(add(add(offset, higgs), root))
            for root, sign in weyl_denominator().items() for higgs in HIGGS
        ) % 5

    def invariant(self, insertions: list[tuple[int, ...]]) -> int:
        return sum(self.gauss_shift(weight) for weight in insertions) % 5


def cube_count_mod5(polynomial2: dict[tuple[int, ...], int]) -> dict[str, int | bool]:
    full = FullCharacterMod5(polynomial2)
    representations = list(link_representations().values())
    label_count = len(representations)
    tensors = []
    for incoming_count in range(4):
        tensor = np.zeros((label_count, label_count, label_count), dtype=np.int64)
        for labels in product(range(label_count), repeat=3):
            signed = [
                representations[label] if slot < incoming_count
                else [tuple(-entry for entry in weight) for weight in representations[label]]
                for slot, label in enumerate(labels)
            ]
            weights = [add(add(a, b), c) for a, b, c in product(*signed)]
            tensor[labels] = full.invariant(weights)
        tensors.append(tensor)
    vertices = list(product(range(2), repeat=3))
    edges = [
        (vertex, tuple(entry+(axis == index) for index, entry in enumerate(vertex)))
        for vertex in vertices for axis in range(3) if vertex[axis] == 0
    ]
    entries, strings = [], []
    for vertex in vertices:
        incoming = [i for i, (_, target) in enumerate(edges) if target == vertex]
        outgoing = [i for i, (source, _) in enumerate(edges) if source == vertex]
        entries.append(tensors[len(incoming)])
        strings.append("".join(chr(97+i) for i in incoming+outgoing))
    bound_ok = label_count**len(edges)*4**len(vertices) < 2**63
    expression = ",".join(strings)+"->"
    path, _ = np.einsum_path(expression, *entries, optimize=("greedy", 9**6))
    pairwise = len(path) == 8 and all(len(step) == 2 for step in path[1:])
    raw = int(np.einsum(expression, *entries, optimize=path))
    reverse_expression = ",".join(strings[::-1])+"->"
    reverse_path, _ = np.einsum_path(reverse_expression, *entries[::-1], optimize=("greedy", 9**6))
    raw_reverse = int(np.einsum(reverse_expression, *entries[::-1], optimize=reverse_path))
    return {"vertices": len(vertices), "edges": len(edges),
            "contraction_raw_reduced_entries": raw,
            "full_gauss_dim_mod5": raw % 5*pow(4, len(vertices), 5) % 5,
            "cached_P12_coefficients": full.constant_term.cache_info().currsize,
            "int64_bound_ok": bound_ok, "pairwise_path": pairwise,
            "reverse_order_agrees": raw == raw_reverse}


def action(state: int, target: int, source: int) -> tuple[int, int] | None:
    if not (state >> source) & 1 or (state >> target) & 1:
        return None
    sign = (-1)**((state & ((1 << source)-1)).bit_count())
    removed = state ^ (1 << source)
    sign *= (-1)**((removed & ((1 << target)-1)).bit_count())
    return removed | (1 << target), sign


def generator_hops() -> list[list[tuple[int, int, int]]]:
    return [
        [(0, 2, 1), (1, 3, 1), (7, 6, -1), (10, 9, -1)],
        [(2, 4, 1), (3, 5, 1), (8, 7, -1), (11, 10, -1)],
        [(1, 0, 1), (3, 2, 1), (5, 4, 1), (13, 12, 1)],
    ]


def rational_rank(columns: list[dict[tuple[int, ...], int]]) -> int:
    basis: dict[tuple[int, ...], dict[tuple[int, ...], Fraction]] = {}
    for column in columns:
        reduced = {row: Fraction(value) for row, value in column.items() if value}
        while reduced:
            pivot = min(reduced)
            if pivot not in basis:
                scale = reduced[pivot]
                basis[pivot] = {row: value/scale for row, value in reduced.items()}
                break
            scale = reduced[pivot]
            for row, value in basis[pivot].items():
                updated = reduced.get(row, 0)-scale*value
                if updated:
                    reduced[row] = updated
                else:
                    reduced.pop(row, None)
    return len(basis)


def independent_gauss_count(with_higgs: bool) -> dict[str, int]:
    higgs = HIGGS if with_higgs else (ZERO,)
    state_weights = [ZERO]*(1 << 16)
    for state in range(1, 1 << 16):
        bit = state & -state
        state_weights[state] = add(state_weights[state ^ bit], WEIGHTS[bit.bit_length()-1])
    zero_states = [
        (state, h) for state in range(1 << 16) for h in range(len(higgs))
        if add(state_weights[state], higgs[h]) == ZERO
    ]
    columns = []
    for state, h in zero_states:
        column: dict[tuple[int, ...], int] = defaultdict(int)
        for generator, hops in enumerate(generator_hops()):
            for target, source, coefficient in hops:
                acted = action(state, target, source)
                if acted:
                    result, sign = acted
                    column[(generator, result, h)] += coefficient*sign
            if with_higgs and generator == 2 and h == 1:
                column[(generator, state, 2)] += 1
        columns.append(column)
    rank = rational_rank(columns)
    return {"zero_weight_states": len(zero_states), "raising_rank_over_Q": rank,
            "Gauss_invariants": len(zero_states)-rank}


def gauss_certificate() -> dict[str, object]:
    from math import comb

    p1 = exterior_character(1)
    p2 = exterior_character(2)
    p2mod = exterior_character(2, 5)
    check("SM16 weight list has sixteen fermion modes", len(WEIGHTS) == 16)
    check("one-copy exterior character has total dimension 2^16", sum(p1.values()) == 2**16)
    check("two-copy exterior character has total dimension 2^32", sum(p2.values()) == 2**32)
    check("mod-five character is the exact coefficient reduction",
          {key: value % 5 for key, value in p2.items() if value % 5} == p2mod)
    frobenius_ok = all(
        comb(12, degree) % 5 == sum(
            comb(2, a)*comb(2, b) for a in range(3) for b in range(3) if a+5*b == degree
        ) % 5 for degree in range(13)
    )
    check("factorwise P^12=P^2 P(z^5)^2 Frobenius certificate", frobenius_ok)
    no_higgs = gauss_count(p1, False)
    one = gauss_count(p1)
    two = gauss_count(p2)
    check("one-copy Gauss singlets without Higgs equal 56", no_higgs == 56)
    check("one-copy Gauss singlets with Higgs equal 120", one == 120)
    check("two-copy Gauss singlets with Higgs equal 561848", two == 561848)
    full_one = 4*frobenius_gauss_count_mod5(p2mod) % 5
    check("full one-site 192-fermion Gauss dimension is 3 mod 5", full_one == 3)
    unprojected = 12*pow(2, 192, 5) % 5
    check("full one-site unprojected dimension is 2 mod 5", unprojected == 2)
    labels, transfer = path_transfer(p2mod)
    check("one-site transfer entry reproduces the full one-site residue",
          transfer[0][0]*4 % 5 == full_one)
    cached = FullCharacterMod5(p2mod)
    representations = list(link_representations().values())
    check("cached P^12 invariant agrees with all 81 transfer entries",
          all(cached.invariant([add(a, tuple(-entry for entry in b)) for a in left for b in right]) == transfer[i][j]
              for i, left in enumerate(representations) for j, right in enumerate(representations)))
    check("nine retained link representations have total dimension 137",
          sum(len(rep)**2 for rep in representations) == 137)
    path = path_counts(transfer)
    check("open-path residues n=1..24 match the exact recurrence", path == PATH_EXPECTED)
    check("path lengths four and five reject a universal nondivisibility claim",
          path[3] == path[4] == 0)
    cube = cube_count_mod5(p2mod)
    check("cube contraction stays below exact int64 bound", cube["int64_bound_ok"])
    check("cube contraction optimizer uses only pairwise steps", cube["pairwise_path"])
    check("independent reversed cube contraction order agrees", cube["reverse_order_agrees"])
    check("cube reduced raw contraction matches exact regression",
          cube["contraction_raw_reduced_entries"] == 48_544_377_696_195)
    check("192-mode open 2x2x2 Gauss dimension with nine-irrep links is 0 mod 5", cube["full_gauss_dim_mod5"] == 0)

    independent_without = independent_gauss_count(False)
    independent_with = independent_gauss_count(True)
    check("independent raising kernel without Higgs is 556-500=56",
          independent_without == {"zero_weight_states": 556,
                                  "raising_rank_over_Q": 500,
                                  "Gauss_invariants": 56})
    check("independent raising kernel with Higgs is 1376-1256=120",
          independent_with == {"zero_weight_states": 1376,
                               "raising_rank_over_Q": 1256,
                               "Gauss_invariants": 120})
    return {
        "weights": 16, "p1_support": len(p1), "p2_support": len(p2),
        "p2_mod5_support": len(p2mod), "weyl_terms": len(weyl_denominator()),
        "one_copy_singlets_without_higgs": no_higgs,
        "one_copy_singlets_with_higgs": one,
        "two_copy_singlets_with_higgs": two,
        "full_one_site_192_modes_higgs_seam_gauss_dim_mod5": full_one,
        "full_one_site_unprojected_dim_mod5": unprojected,
        "path_transfer_labels": labels, "full_path_gauss_dims_mod5_n1_to_n24": path,
        "full_2x2x2_cube": cube,
        "independent_without_higgs": independent_without,
        "independent_with_higgs": independent_with,
    }


def d4_cap_certificate() -> dict[str, object]:
    imaginary = sp.I
    seam_rotation = sp.diag(1, -imaginary, -1, imaginary)
    family_rotation = sp.diag(-imaginary, -1, imaginary)
    seam_reflection = sp.zeros(4)
    for momentum in range(4):
        seam_reflection[(-momentum) % 4, momentum] = 1
    family_reflection = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    rotation = sp.kronecker_product(seam_rotation, family_rotation)
    reflection = sp.kronecker_product(seam_reflection, family_reflection)
    check("ordinary D4 relations hold on the selected even one-pair space",
          rotation**4 == sp.eye(12) and reflection**2 == sp.eye(12)
          and reflection*rotation*reflection == rotation.H)
    group = [rotation**power*reflection**toggle for power in range(4) for toggle in range(2)]
    psi = sp.zeros(12, 1)
    for momentum, family in ((1, 3), (2, 2), (3, 1)):
        psi[3*momentum+family-1] = 1
    projector = psi*psi.H/3
    cap = sp.eye(12)-projector
    check("equal-intertwiner projector is D4 invariant",
          projector*projector == projector and rotation*projector == projector
          and reflection*projector == projector)
    check("selected-space cap has unique ground ray and exact gap one",
          cap*cap == cap and cap.rank() == 11)
    psi_matrix = sp.Matrix(4, 3, list(psi))
    check("cap ground ray has Schmidt rank three", psi_matrix.rank() == 3)
    rho_seam = psi_matrix*psi_matrix.H/3
    rho_family = psi_matrix.H*psi_matrix/3
    residual_squared = 1-sp.trace(rho_seam**2)/3-sp.trace(rho_family**2)/4+sp.Rational(1, 12)
    check("nonadditive Hilbert-Schmidt norm squared is exactly 8/9",
          residual_squared == sp.Rational(8, 9))
    invariant_dimension = len(sp.Matrix.vstack(rotation-sp.eye(12), reflection-sp.eye(12)).nullspace())
    check("D4 invariant-ray space is two-dimensional, so orientation is not selected",
          invariant_dimension == 2)
    check("ordinary selected-pair Hermitian commutant has dimension two",
          len(sp.Matrix.vstack(
              sp.kronecker_product(sp.eye(3), family_rotation)-sp.kronecker_product(family_rotation.T, sp.eye(3)),
              sp.kronecker_product(sp.eye(3), family_reflection)-sp.kronecker_product(family_reflection.T, sp.eye(3)),
          ).nullspace()) == 2)
    phases = [sp.exp(-imaginary*sp.pi*family/4) for family in (1, 2, 3)]
    majorana_factors = [sp.simplify(phases[i]*phases[j]-1) for i in range(3) for j in range(i, 3)]
    check("actual projective one-fermion lift forbids every invariant Majorana entry",
          all(factor != 0 for factor in majorana_factors))

    omega4 = np.exp(2j*np.pi/4)
    fourier = np.array([[omega4**(row*column)/2 for column in range(4)] for row in range(4)])
    basis_change = np.kron(fourier, np.eye(3))
    indices = [0, 4, 8, 9, 1]
    p5 = np.zeros((12, 12), complex)
    x5 = np.zeros((12, 12), complex)
    for position, index in enumerate(indices):
        p5[index, index] = 1
        x5[indices[(position+1) % 5], index] = 1
    old = (2/7)*(p5-(x5+x5.conj().T)/2)+(3/5)*(np.eye(12)-p5)
    old = basis_change.conj().T@old@basis_change
    numeric_group = [np.array(element, dtype=complex) for element in group]
    twirled = sum(element@old@element.conj().T for element in numeric_group)/8
    eigenvalues, eigenvectors = np.linalg.eigh(twirled)
    multiplicity = int(sum(abs(eigenvalues-eigenvalues[0]) < 1e-9))
    check("twirled old cap mutant retains fourfold ground degeneracy", multiplicity == 4)

    numeric_projector = np.array(projector, dtype=complex)
    numeric_cap = np.array(cap, dtype=complex)
    phase5 = np.exp(2j*np.pi/5)
    order5 = numeric_projector+phase5*numeric_cap
    check("internal cap unitary has exact numerical order five",
          np.linalg.norm(np.linalg.matrix_power(order5, 5)-np.eye(12)) < 1e-10)
    check("internal order-five operator is unitary",
          np.linalg.norm(order5.conj().T@order5-np.eye(12)) < 1e-10)
    cap_from_order5 = (2*np.eye(12)-order5-order5.conj().T)/(2-2*np.cos(2*np.pi/5))
    check("order-five parent formula reproduces the symmetric cap",
          np.linalg.norm(cap_from_order5-numeric_cap) < 1e-10)
    check("order-five cap unitary has only two eigenvalues, not a five-state clock",
          len({complex(round(value.real, 9), round(value.imag, 9)) for value in np.linalg.eigvals(order5)}) == 2)
    tensor = numeric_cap.reshape(4, 3, 4, 3)
    trace_family = np.einsum("abcb->ac", tensor)
    trace_seam = np.einsum("abad->bd", tensor)
    interaction = (numeric_cap-np.kron(trace_family/3, np.eye(3))
                   -np.kron(np.eye(4), trace_seam/4)
                   +np.trace(numeric_cap)*np.eye(12)/12)
    check("numeric interaction residual realizes exact squared norm 8/9",
          abs(np.linalg.norm(interaction)**2-8/9) < 1e-10)
    return {
        "representation_scope": "ordinary D4 only on selected 12D even one-pair space",
        "D4_invariant_vector_dimension": invariant_dimension,
        "cap_rank": int(cap.rank()), "cap_ground_degeneracy": 1,
        "cap_gap_exact": 1, "ground_Schmidt_rank": int(psi_matrix.rank()),
        "nonadditive_Hilbert_Schmidt_norm_squared_exact": str(residual_squared),
        "actual_lift_invariant_Majorana_matrix": "zero",
        "twirled_old_cap_ground_degeneracy": multiplicity,
        "twirled_old_cap_ground_energy": float(eigenvalues[0]),
        "twirled_old_cap_gap": float(eigenvalues[multiplicity]-eigenvalues[0]),
        "twirled_old_cap_ground_Schmidt_rank": int(np.linalg.matrix_rank(eigenvectors[:, 0].reshape(4, 3), tol=1e-8)),
        "order5_is_canonical_clock_or_Weyl_pair": False,
    }


def run() -> int:
    reset()
    print("v1028 -- full Gauss residues and selected-pair-space D4 cap")
    report = {
        "Gauss": gauss_certificate(),
        "D4_cap": d4_cap_certificate(),
        "claim_boundary": {
            "proved": ["full one-site Gauss residue 3 mod 5",
                       "192-mode open 2x2x2 cube with nine-irrep links: Gauss residue 0 mod 5",
                       "independent one-copy raising-kernel conventions",
                       "entangled unique cap within the selected 12D pair space"],
            "not_proved": ["universal Gauss nondivisibility",
                           "canonical local or refinement-compatible Weyl pair",
                           "ordinary D4 on the full lifted one-fermion Fock space",
                           "canonical clock or oriented global rho0",
                           "physical neutrino texture, T6, T8 or TOE"],
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("VERDICT: EXACT_GAUSS_RESIDUES_AND_SELECTED_PAIR_CAP_PROVED; T6_T8_AND_TOE_OPEN")
    return summary("v1028 Gauss residues and D4 cap")


if __name__ == "__main__":
    raise SystemExit(run())
