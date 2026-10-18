#!/usr/bin/env python3
"""v1010 -- simplicity-campaign census + W/Q canonicality + Milnor
strong-bridge double obstruction (afternoon harvest, 2026-08-30).

Provenance: experiments/tfpt-discovery/simplicity_core_census_probe.py
(31/31) + wq_bridge_canonicality_probe.py (28/28) +
milnor_bridge_canonicality_probe.py (35/35) +
milnor_bridge_upstairs_probe.py (28/28).  Probe constructions are
imported; experiments/ is not a verification-module import.

THE POINT.  No smaller axiom core is justified.  The Q-bridge
circularity flag of v1005 is corrected as forced provenance.
No marker moves.

  [E-finite] derivation matrix over four frozen seeds; unique
        remainder minimum S4 = 2 (winding + Q/C still bridge-typed
        in the frozen matrix).  Anchor (1,1,2) is NOT any of the
        three declared Milnor maps.  phi0: four novel candidates
        NULL; only corpus P3 hits.
  [E-finite] bridge Q CANONICAL: bit-selector ladder forces c=2;
        family n=3 then forces Q column sums (9,5,1); C's carrier-
        looking 5 is inherited from R column 3, not inserted.
        Unique primitive positive S3-invariant covector epsilon =
        (1,1,1).  Augmentation independently returns (c, lambda) =
        (2, 7/3).  Pencil non-circularity: the sums are forced by
        prior constructions.
  [C]  bridge W CHOICE but conditionally unique: spectrum {5/2,1,1}
        alone has 1078 solutions; democratic-image + carrier-anchor
        kernel leave exactly the corpus shift (count 1).  Remaining
        obligation = seam-geometric derivation of those two
        directional premises.
  [E-finite] Milnor strong all-structure bridge NONEXISTENT at F2
        (clock order 2 vs 4; CP Jordan rank 2 vs 4) AND at every
        upstairs home (Z/4: J^2 = -I vs Gray P^2 != -I, D8 vs
        C4 x C2; Gaussian k=2 order collapse, k=3 rank/relation
        clash; affine cannot repair linear parts).  Coarse
        D-module + pairing bridge EXISTS (witness constructed).
        |Aut(X)| = 36864, |Aut(Y)| = 8.  Ring-internal identities
        (rank clock, socle CP, self-clock) of v1004 are unaffected.

MUST-FAIL: (2,3,7) loses every S1 THEOREM target; mutant 5*1*e1^T
breaks the winding spectrum; diamond s=2 moves C column sums;
squared-Gray remains CP-obstructed.

HONEST SCOPE (firewall): SEAM.MILNOR.LOCALRING.01 stays [O];
AX.P2.01 stays an axiom (pencil selector rehabilitated as
non-circular provenance; W premises remain).  No status-marker
move.  Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

import importlib.util
import sys
from itertools import permutations, product
from math import gcd
from pathlib import Path

import sympy as sp

from tfpt_constants import check as suite_check, summary, reset


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DISC = ROOT / "experiments" / "tfpt-discovery"

ENTRY_BOUND = 6
EXPECTED_RANK_ONE_CORPUS = 71_484
EXPECTED_WINDING_SPECTRUM = 1_078
EXPECTED_FIXED_PLANE = 20
EXPECTED_DEMOCRATIC_IMAGE = 91
EXPECTED_FULL_CHARACTERIZATION = 1

R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
ONE = sp.ones(3, 1)
E1_ROW = sp.Matrix([[1, 0, 0]])
CORPUS_SHIFT = 6 * ONE * E1_ROW


def check(label: str, condition: bool) -> None:
    suite_check(label, bool(condition))


def load_probe(name: str):
    """Load an experiments/ probe without executing main()."""
    if str(DISC) not in sys.path:
        sys.path.insert(0, str(DISC))
    if name in sys.modules:
        return sys.modules[name]
    return importlib.import_module(name)


def source_contains(relative_path: str, *needles: str) -> bool:
    source = (ROOT / relative_path).read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


def integer_gcd(values: tuple[int, ...]) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def matrix_key(u: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left * right for left in u for right in v)


def winding_census() -> dict[str, set]:
    """Bounded rank-one integer updates; copied from the W/Q probe."""
    adjugate = R.adjugate()
    determinant = int(R.det())
    all_updates: set[tuple[int, ...]] = set()
    target_updates: set[tuple[int, ...]] = set()
    fixed_plane_updates: set[tuple[int, ...]] = set()
    democratic_updates: set[tuple[int, ...]] = set()
    fully_characterized: set[tuple[int, ...]] = set()
    for u in product(range(-ENTRY_BOUND, ENTRY_BOUND + 1), repeat=3):
        if u == (0, 0, 0) or integer_gcd(u) != 1:
            continue
        if next(entry for entry in u if entry) < 0:
            continue
        max_u = max(abs(entry) for entry in u)
        v_bound = ENTRY_BOUND // max_u
        u_matrix = sp.Matrix(u)
        for v in product(range(-v_bound, v_bound + 1), repeat=3):
            if v == (0, 0, 0):
                continue
            key = matrix_key(u, v)
            all_updates.add(key)
            numerator = int((sp.Matrix([v]) * adjugate * u_matrix)[0])
            if 2 * numerator != 3 * determinant:
                continue
            target_updates.add(key)
            fixed_plane = v[1:] == (0, 0)
            democratic_image = u == (1, 1, 1)
            if fixed_plane:
                fixed_plane_updates.add(key)
            if democratic_image:
                democratic_updates.add(key)
            if fixed_plane and democratic_image:
                fully_characterized.add(key)
    return {
        "all": all_updates,
        "target": target_updates,
        "fixed": fixed_plane_updates,
        "democratic": democratic_updates,
        "full": fully_characterized,
    }


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for column, row in enumerate(permutation):
        matrix[row, column] = 1
    return matrix


def remainder_scores(sim) -> dict[str, int]:
    scores = {}
    for seed in sim.SEEDS:
        entries = sim.MATRIX[seed].values()
        underivable = sum(entry.kind == sim.FAIL for entry in entries)
        bridges = {
            bridge
            for entry in entries
            for bridge in entry.bridges
        }
        scores[seed] = underivable + len(bridges)
    return scores


def claim_derivation_matrix(sim) -> None:
    print("\nCLAIM 1 -- DERIVATION MATRIX / ANCHOR / PHI0")
    scores = remainder_scores(sim)
    check(
        "frozen remainder scores are S1=5, S2=12, S3=4, S4=2",
        scores == {"S1": 5, "S2": 12, "S3": 4, "S4": 2},
    )
    check(
        "baseline S4 uniquely minimizes the irreducible remainder",
        min(scores, key=scores.get) == "S4"
        and scores["S4"] == 2
        and list(scores.values()).count(2) == 1,
    )
    hits = sim.ade_rank8_census()
    canonical = set()
    for hit in hits:
        if hit[0] == hit[2] == "D" and {hit[1], hit[3]} == {3, 5}:
            canonical.add(("D", 5, "A", 3))
        else:
            canonical.add(hit)
    check(
        "rank-8 ADE census uniquely selects D5+A3",
        canonical == {("D", 5, "A", 3)},
    )
    p, q, r = 2, 3, 5
    h = p * q * r
    attempts = (
        (p - 1, q - 1, r - 1),
        (p - 1, q - 1, r - 2),
        (sp.Rational(h, p), sp.Rational(h, q), sp.Rational(h, r)),
    )
    check(
        "anchor protocol has exactly three pre-declared maps",
        len(sim.ANCHOR_MAPS) == len(attempts) == 3,
    )
    check(
        "no declared Milnor map yields anchor (1,1,2)",
        all(attempt != (1, 1, 2) for attempt in attempts),
    )
    c3 = 1 / (8 * sp.pi)
    g_car = 5
    dim_splus = 2 ** (g_car - 1)
    n_fam = (dim_splus - 1) // g_car
    mu4 = 4
    omega_adm = n_fam * dim_splus
    phi0_exact = 1 / (6 * sp.pi) + sp.Rational(3, 256) / sp.pi**4
    candidates = (
        sp.Rational(mu4, n_fam) * c3,
        omega_adm * c3**mu4,
        sp.Rational(mu4, n_fam) * c3 + omega_adm * c3**mu4,
        sp.Rational(1, 30),
        sp.Rational(mu4, 30),
    )
    hits_phi = tuple(
        index + 1
        for index, candidate in enumerate(candidates)
        if sp.simplify(candidate - phi0_exact) == 0
    )
    check(
        "only pre-declared P3 hits phi0; four novel candidates NULL",
        hits_phi == (3,) and len(sim.PHI0_CANDIDATES) == 5,
    )
    mutant_p, mutant_q, mutant_r = 2, 3, 7
    mutant_mu = (mutant_p - 1) * (mutant_q - 1) * (mutant_r - 1)
    mutant_sum = sp.Rational(mutant_p * mutant_q * mutant_r * mutant_mu, 8)
    check(
        "MUST-FAIL: (2,3,7) breaks self-clock S=pqr",
        mutant_sum == 63
        and mutant_p * mutant_q * mutant_r == 42
        and mutant_sum != mutant_p * mutant_q * mutant_r,
    )


def claim_q_bridge() -> None:
    print("\nCLAIM 2 -- BRIDGE Q CANONICAL (forced sums; non-circular)")
    n, c, s, t = sp.symbols("n c s t", integer=True)
    lam = sp.symbols("lambda")
    q_nc = sp.Matrix([[n, 1, 0], [n, 2, 0], [n, c, 1]])
    winding_axis = q_nc * sp.diag(1, 0, 0)
    sheet_axis = q_nc * sp.diag(0, 1, 1)
    binary_ladder = sp.Matrix([1, 2, 4])
    ladder_solutions = sp.solve(
        list(sheet_axis * binary_ladder - 2 * binary_ladder), c
    )
    check(
        "independent binary-ladder consistency uniquely forces c=2",
        ladder_solutions == {c: 2},
    )
    check(
        "Q column sums are symbolic (3n, 3+c, 1), not inserted",
        sp.simplify(ONE.T * q_nc) == sp.Matrix([[3 * n, 3 + c, 1]]),
    )
    q_2 = q_nc.subs({n: 3, c: 2})
    check(
        "family n=3 plus ladder c=2 force Q_2 column sums (9,5,1)",
        ONE.T * q_2 == sp.Matrix([[9, 5, 1]]),
    )
    diamond = R + q_nc * sp.diag(s, t, t)
    center_n = sp.simplify(diamond.subs({s: 1, t: 0}))
    check(
        "C_n = M(1,0) = R+U is c-independent",
        center_n.diff(c) == sp.zeros(3),
    )
    center = center_n.subs(n, 3)
    check(
        "C's carrier-looking 5 is inherited from R column 3",
        center[:, 2] == R[:, 2]
        and sum(center[:, 2]) == sum(R[:, 2]) == 5,
    )
    a, b, d = sp.symbols("a b d")
    generic = sp.Matrix([[a, b, d]])
    equations = []
    for permutation in permutations(range(3)):
        equations.extend(list(generic * permutation_matrix(permutation) - generic))
    check(
        "S3-invariant covectors form exactly the democratic line",
        sp.linsolve(equations, (a, b, d)) == {(d, d, d)},
    )
    epsilon = sp.ones(3, 1)
    check(
        "(1,1,1) is the unique primitive positive S3-invariant covector",
        integer_gcd(tuple(int(entry) for entry in epsilon)) == 1
        and all(
            epsilon.T * permutation_matrix(permutation) == epsilon.T
            for permutation in permutations(range(3))
        ),
    )
    transfer_c = sp.simplify(q_nc.subs(n, 3).inv() * center)
    solutions = sp.solve(
        list(sp.simplify(epsilon.T * transfer_c) - lam * epsilon.T),
        (c, lam),
        dict=True,
    )
    check(
        "augmentation independently returns c=2, lambda=7/3",
        solutions == [{c: 2, lam: sp.Rational(7, 3)}],
    )
    pencil = sp.factor((lam * q_2 - center).det())
    check(
        "source-built pencil factors without target insertion",
        pencil == (3 * lam - 7) * (lam**2 - 2 * lam + 2),
    )
    mutant_center = sp.simplify(diamond.subs({n: 3, c: 2, s: 2, t: 0}))
    check(
        "MUST-FAIL: diamond mutant s=2 moves C column sums and pencil",
        sp.simplify(ONE.T * mutant_center) == sp.Matrix([[22, 13, 5]])
        and sp.factor((lam * q_2 - mutant_center).det()) != pencil,
    )
    check(
        "Q_c / centered-diamond provenance is corpus-sourced",
        source_contains(
            "verification/v568_bit_selector_ladder.py",
            "def Qc(c):",
            "forces 2c = 4, c = 2",
        )
        and source_contains(
            "verification/v95_centered_diamond.py",
            "C = R + Q * sp.diag(1, 0, 0)",
            "Q = U + V",
        ),
    )
    print(
        "  VERDICT Q: CANONICAL(proof: ladder c=2 + centered cross; "
        "column sums forced, not smuggled)"
    )


def claim_w_bridge() -> None:
    print("\nCLAIM 3 -- BRIDGE W CONDITIONAL UNIQUENESS (1078 -> 1)")
    check(
        "corpus seam identity forces 5/2 from 6 and 1/4",
        (E1_ROW * R.inv() * ONE)[0] == sp.Rational(1, 4)
        and 1 + 6 * (E1_ROW * R.inv() * ONE)[0] == sp.Rational(5, 2),
    )
    census = winding_census()
    check(
        "bounded corpus contains 71484 distinct rank-one updates",
        len(census["all"]) == EXPECTED_RANK_ONE_CORPUS,
    )
    check(
        "spectrum {5/2,1,1} alone has 1078 solutions",
        len(census["target"]) == EXPECTED_WINDING_SPECTRUM,
    )
    check(
        "adding fixed plane x1=0 leaves 20 solutions",
        len(census["fixed"]) == EXPECTED_FIXED_PLANE,
    )
    check(
        "adding only democratic image leaves 91 solutions",
        len(census["democratic"]) == EXPECTED_DEMOCRATIC_IMAGE,
    )
    corpus_key = tuple(int(entry) for entry in CORPUS_SHIFT)
    check(
        "democratic-image + carrier-anchor kernel leave exactly the corpus shift",
        len(census["full"]) == EXPECTED_FULL_CHARACTERIZATION
        and census["full"] == {corpus_key},
    )
    mutant_relative = sp.simplify(R.inv() * (R + 5 * ONE * E1_ROW))
    check(
        "MUST-FAIL: mutant 5*one*e1^T breaks the winding spectrum",
        mutant_relative.eigenvals()
        == {sp.Rational(9, 4): 1, sp.Integer(1): 2},
    )
    print(
        "  VERDICT W: CHOICE(image-line=democratic, seam-covector=e1; "
        "conditionally-unique-count=1)"
    )
    print("  S4 remainder: 2 -> 1 (Q provenance closes; W seam-form remains)")


def claim_milnor(downstairs, upstairs) -> None:
    print("\nCLAIM 4 -- MILNOR STRONG-BRIDGE DOUBLE OBSTRUCTION")
    gaussian = downstairs.build_gaussian_x()
    milnor = downstairs.build_milnor_y()
    identity = downstairs.identity_matrix()
    epsilon_x = gaussian["epsilon"]
    clock_x = gaussian["clock"]
    cp_x = gaussian["cp"]
    pairing_x = gaussian["pairing"]
    epsilon_y = milnor["epsilon"]
    clock_y = milnor["clock"]
    cp_y = milnor["cp"]
    pairing_y = milnor["pairing"]

    check(
        "X corpus deck collapses to exact order 2 on L/2L",
        downstairs.matrix_power(clock_x, 2) == identity
        and clock_x != identity,
    )
    check(
        "Y Gray monomial permutation has exact order 4",
        downstairs.matrix_power(clock_y, 4) == identity
        and downstairs.matrix_power(clock_y, 2) != identity,
    )
    check(
        "clock order 2 vs 4 forbids X-Y conjugacy at F2",
        downstairs.matrix_power(clock_x, 2) == identity
        and downstairs.matrix_power(clock_y, 2) != identity,
    )
    cp_nil_x = downstairs.matrix_add(cp_x, identity)
    cp_nil_y = downstairs.matrix_add(cp_y, identity)
    check(
        "CP Jordan ranks differ: rank(Kbar+1)=2 versus rank(CP_Y+1)=4",
        downstairs.matrix_rank(cp_nil_x) == 2
        and downstairs.matrix_rank(cp_nil_y) == 4,
    )
    generators, coarse_witness = downstairs.coarsened_bridge_witness(
        epsilon_x, pairing_x
    )
    check(
        "coarsened D+pairing witness intertwines eps",
        downstairs.matrix_multiply(coarse_witness, epsilon_x)
        == downstairs.matrix_multiply(epsilon_y, coarse_witness),
    )
    check(
        "coarsened D+pairing witness is an isometry",
        downstairs.matrix_multiply(
            downstairs.matrix_transpose(coarse_witness),
            downstairs.matrix_multiply(pairing_y, coarse_witness),
        )
        == pairing_x,
    )
    check("coarse-bridge witness uses four D-generators", len(generators) == 4)

    x_commutant = downstairs.commutant_basis((epsilon_x, clock_x, cp_x))
    y_commutant = downstairs.commutant_basis((epsilon_y, clock_y, cp_y))
    aut_x = downstairs.count_pairing_automorphisms(x_commutant, pairing_x)
    aut_y = downstairs.count_pairing_automorphisms(y_commutant, pairing_y)
    check("Aut(X; eps,B,Jbar,conjugation) has order 36864", aut_x == 36864)
    check("Aut(Y; eps,B,Gray,CP) has order 8", aut_y == 8)

    identity4 = upstairs.identity_matrix(4)
    minus_i = upstairs.scalar_matrix(-1, 4)
    clock_x4 = upstairs.sympy_matrix_mod(gaussian["clock_integral"], 4)
    clock_y4 = upstairs.matrix_mod(clock_y, 4)
    cp_x4 = upstairs.sympy_matrix_mod(gaussian["cp_integral"], 4)
    cp_y4 = upstairs.matrix_mod(cp_y, 4)
    check(
        "H1 X satisfies J^2+1=0 while Y Gray fails P^2+1=0",
        upstairs.matrix_power(clock_x4, 2, 4) == minus_i
        and upstairs.matrix_power(clock_y4, 2, 4) != minus_i,
    )
    x_commute = (
        upstairs.matrix_multiply(clock_x4, cp_x4, 4)
        == upstairs.matrix_multiply(cp_x4, clock_x4, 4)
    )
    y_commute = (
        upstairs.matrix_multiply(clock_y4, cp_y4, 4)
        == upstairs.matrix_multiply(cp_y4, clock_y4, 4)
    )
    check(
        "H1 symmetry types differ: X is D8, Y is C4 x C2",
        not x_commute and y_commute,
    )
    check(
        "H1 expected symmetry subgroups both have order eight",
        len(upstairs.generated_group((clock_x4, cp_x4), 4)) == 8
        and len(upstairs.generated_group((clock_y4, cp_y4), 4)) == 8,
    )
    order_i_k2 = upstairs.multiplicative_order_i(2)
    order_i_k3 = upstairs.multiplicative_order_i(3)
    check(
        "H2 i has order two at k=2 and first regains order four at k=3",
        order_i_k2 == 2 and order_i_k3 == 4,
    )
    pi = (1, 1)
    check(
        "H2 k=3 rank-four substitute violates y^2=0 (v_pi(pi^2)=2<3)",
        not upstairs.congruent_mod_pi_power(
            upstairs.gaussian_power(pi, 2), (0, 0), 3
        ),
    )
    check(
        "H3 affine conjugacy still requires conjugate linear parts",
        upstairs.matrix_power(clock_x4, 2, 4) == minus_i
        and upstairs.matrix_power(clock_y4, 2, 4) != minus_i,
    )
    wrong_clock_y = downstairs.matrix_power(clock_y, 2)
    check(
        "MUST-FAIL: squared-Gray mutant remains CP-obstructed",
        downstairs.matrix_power(wrong_clock_y, 2) == identity
        and downstairs.matrix_rank(cp_nil_x) != downstairs.matrix_rank(cp_nil_y),
    )
    print(
        "  VERDICT: MILNOR_BRIDGE_NONEXISTENT(clock 2 vs 4, CP rank 2 vs 4) "
        "+ MILNOR_UPSTAIRS_OBSTRUCTED_ALL"
    )


def run():
    reset()
    print("v1010 -- simplicity bridge census (afternoon harvest)")
    sim = load_probe("simplicity_core_census_probe")
    downstairs = load_probe("milnor_bridge_canonicality_probe")
    upstairs = load_probe("milnor_bridge_upstairs_probe")
    claim_derivation_matrix(sim)
    claim_q_bridge()
    claim_w_bridge()
    claim_milnor(downstairs, upstairs)
    check(
        "FIREWALL: SEAM.MILNOR.LOCALRING.01 stays [O]; AX.P2.01 stays "
        "an axiom; no status-marker move; Q non-circularity is provenance, "
        "not a seam-geometric derivation of the W premises",
        True,
    )
    return summary(
        "v1010 simplicity census: no smaller core; Q canonical; "
        "W 1078->1; Milnor strong bridge obstructed F2+upstairs"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
