#!/usr/bin/env python3
"""Exact canonicality audit for the winding (W) and Q/C-pencil (Q) bridges.

EXPLORATION ONLY.  This probe imports no verification module and writes only
to stdout.  Matrix constructions are copied from their named corpus sources.

Anti-numerology protocol (declared before calculation)
-------------------------------------------------------
W uses at most these three candidate characterizations:
  W1. the update has democratic image Z*(1,1,1), the uniform family coupling;
  W2. the rank-one determinant identity gives det(L)/det(R)=5/2;
  W3. its pointwise fixed plane is x1=0, the carrier-anchor covector kernel.
The exhaustive corpus is every distinct nonzero rank-one integer 3x3 update
whose matrix entries lie in [-6,6].  No matrix is constructed from 5/2.

Q uses the source constructions, with their own parameters left symbolic:
  Q_c = U + V_c from the bit-selector ladder, and
  C = R + U = M(1,0) from the centered diamond.
Neither 7/3 nor a column-sum target is used to construct Q_c, C, or epsilon.

The stored census totals are regression guards obtained from the exhaustive
integer scan; they are not filters or selection inputs.
"""

from fractions import Fraction
from itertools import permutations, product
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
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

CHECKS: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    """Record one deterministic exact check."""
    passed = bool(condition)
    CHECKS.append((label, passed))
    print(f"{'PASS' if passed else 'FAIL'}  {label}")


def source_contains(relative_path: str, *needles: str) -> bool:
    """Check textual provenance without importing a corpus module."""
    source = (ROOT / relative_path).read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


def integer_gcd(values: tuple[int, ...]) -> int:
    """Greatest common divisor of an integer tuple."""
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def matrix_key(u: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    """Flatten the outer product u v^T in row-major order."""
    return tuple(left * right for left in u for right in v)


def winding_census() -> dict[str, object]:
    """Enumerate every bounded rank-one integer update exactly once.

    Every nonzero rank-one integer matrix has a unique factorization u v^T
    when u is primitive and the first nonzero entry of u is positive.  The
    bound on entries then gives |v_j| <= floor(B/max_i |u_i|).
    """
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
            check_new = key not in all_updates
            if not check_new:
                raise AssertionError("canonical rank-one factorization duplicated")
            all_updates.add(key)

            # v^T R^-1 u = 3/2, cleared using det(R)=8.  This is exactly
            # the nontrivial eigenvalue condition 1 + v^T R^-1 u = 5/2.
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


def bridge_w() -> str:
    """Audit the winding shift and return its honest verdict."""
    print("\nBRIDGE W — WINDING REALIZATION")
    lam = sp.symbols("lambda")
    u1, u2, u3, v1, v2, v3 = sp.symbols(
        "u1 u2 u3 v1 v2 v3", integer=True
    )
    u = sp.Matrix([u1, u2, u3])
    v = sp.Matrix([[v1, v2, v3]])
    gain = sp.expand((v * R.inv() * u)[0])
    relative = sp.eye(3) + R.inv() * u * v

    check(
        "rank-one characteristic identity is symbolic",
        sp.factor(
            relative.charpoly(lam).as_expr()
            - (lam - 1) ** 2 * (lam - 1 - gain)
        )
        == 0,
    )
    check(
        "matrix-determinant lemma is symbolic",
        sp.expand((R + u * v).det() - R.det() * (1 + gain)) == 0,
    )
    check(
        "corpus seam identity forces 5/2 from 6 and 1/4",
        (E1_ROW * R.inv() * ONE)[0] == sp.Rational(1, 4)
        and 6 == 2 * 3
        and 1 + 6 * (E1_ROW * R.inv() * ONE)[0]
        == sp.Rational(5, 2),
    )

    census = winding_census()
    check(
        "bounded corpus contains 71,484 distinct rank-one updates",
        len(census["all"]) == EXPECTED_RANK_ONE_CORPUS,
    )
    check(
        "spectrum {5/2,1,1} alone has 1,078 solutions",
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
        "all three characterizations leave exactly the corpus shift",
        len(census["full"]) == EXPECTED_FULL_CHARACTERIZATION
        and census["full"] == {corpus_key},
    )

    relative_corpus = sp.simplify(R.inv() * (R + CORPUS_SHIFT))
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    check(
        "corpus update has exact fixed plane x1=0",
        sp.simplify(
            (relative_corpus - sp.eye(3)) * sp.Matrix([x1, x2, x3])
        )
        == sp.Matrix(
            [
                sp.Rational(3, 2) * x1,
                sp.Rational(3, 2) * x1,
                -sp.Rational(3, 2) * x1,
            ]
        ),
    )

    mutant_shift = 5 * ONE * E1_ROW
    mutant_relative = sp.simplify(R.inv() * (R + mutant_shift))
    check(
        "mutant 5*one*e1^T breaks the winding spectrum",
        mutant_relative.eigenvals()
        == {sp.Rational(9, 4): 1, sp.Integer(1): 2},
    )

    check(
        "v4 and paper provenance fix R, the shift, and scalar 6",
        source_contains(
            "verification/v4_flavor_matrix.py",
            "W = sp.Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])",
            "L = R + 6 * W",
            "anchor = first column of R = (1,1,2)",
        )
        and source_contains(
            "tfpt_3_e8_audit_bootstrap.tex",
            r"L=R+6\,\mathbf 1 e_1^\top",
            r"\tfrac{|R^+(A_3)|}{|\mu_4|}",
        ),
    )
    check(
        "later provenance explicitly leaves winding FORM declared",
        source_contains(
            "verification/v574_stageb_winding.py",
            "exactly ONE is uniform: (3,3,3), the compiler",
            "the winding FORM",
            "remaining",
        ),
    )

    verdict = (
        "CHOICE(image-line=democratic,seam-covector=e1; "
        "conditionally-unique-count=1)"
    )
    print(f"  SOLUTION COUNTS: target={len(census['target'])}, "
          f"+fixed-plane={len(census['fixed'])}, "
          f"+democratic={len(census['democratic'])}, "
          f"all-three={len(census['full'])}")
    print("  RESULT: 6 is forced as 2*N_fam=|R^+(A3)| and the determinant "
          "ratio then follows; the spectrum does not derive the two lines.")
    print(f"  VERDICT W: {verdict}")
    return verdict


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    """Return the 3x3 permutation matrix for a coordinate permutation."""
    matrix = sp.zeros(3)
    for column, row in enumerate(permutation):
        matrix[row, column] = 1
    return matrix


def bridge_q() -> str:
    """Symbolically reconstruct Q_c, C, and the democratic augmentation."""
    print("\nBRIDGE Q — Q/C PENCIL CANONICALITY")
    n, c, s, t = sp.symbols("n c s t", integer=True)
    lam = sp.symbols("lambda")

    # Source construction, with its own parameters left symbolic.
    q_nc = sp.Matrix([[n, 1, 0], [n, 2, 0], [n, c, 1]])
    winding_axis = q_nc * sp.diag(1, 0, 0)
    sheet_axis = q_nc * sp.diag(0, 1, 1)
    dominant = sp.Matrix([1, 2, 2 * c])
    binary_ladder = sp.Matrix([1, 2, 4])

    check(
        "V_c dominant mode (1,2,2c) has eigenvalue 2 identically",
        sp.simplify(sheet_axis * dominant - 2 * dominant) == sp.zeros(3, 1),
    )
    ladder_solutions = sp.solve(
        list(sheet_axis * binary_ladder - 2 * binary_ladder), c
    )
    check(
        "independent binary-ladder consistency uniquely forces c=2",
        ladder_solutions == {c: 2},
    )

    q_column_sums = sp.simplify(ONE.T * q_nc)
    check(
        "Q column sums are symbolic (3n,3+c,1), not inserted",
        q_column_sums == sp.Matrix([[3 * n, 3 + c, 1]]),
    )
    q_2 = q_nc.subs({n: 3, c: 2})
    check(
        "family n=3 plus ladder c=2 force Q_2 column sums (9,5,1)",
        ONE.T * q_2 == sp.Matrix([[9, 5, 1]]),
    )

    diamond = R + q_nc * sp.diag(s, t, t)
    center_n = sp.simplify(diamond.subs({s: 1, t: 0}))
    expected_center_n = sp.Matrix(
        [[n + 1, 3, 0], [n + 1, 5, 2], [n + 2, 5, 3]]
    )
    check(
        "center C_n=M(1,0)=R+U is symbolic and independent of c",
        center_n == expected_center_n
        and center_n.diff(c) == sp.zeros(3),
    )
    center_column_sums = sp.simplify(ONE.T * center_n)
    check(
        "C_n column sums are forced as (3n+4,13,5)",
        center_column_sums == sp.Matrix([[3 * n + 4, 13, 5]]),
    )
    center = center_n.subs(n, 3)
    check(
        "C's carrier-looking 5 is inherited unchanged from R column 3",
        center[:, 2] == R[:, 2]
        and sum(center[:, 2]) == sum(R[:, 2]) == 5,
    )
    check(
        "single centered-cross formulas reconstruct Q=U+V and C=R+U",
        q_nc == winding_axis + sheet_axis
        and center_n == R + winding_axis,
    )

    # Epsilon is reconstructed independently as the primitive positive
    # covector invariant under every permutation of the three family rows.
    a, b, d = sp.symbols("a b d")
    generic_covector = sp.Matrix([[a, b, d]])
    invariance_equations = []
    for permutation in permutations(range(3)):
        permuter = permutation_matrix(permutation)
        invariance_equations.extend(
            list(generic_covector * permuter - generic_covector)
        )
    invariant_solution = sp.linsolve(invariance_equations, (a, b, d))
    epsilon = sp.ones(3, 1)
    check(
        "S3-invariant covectors form exactly the democratic line",
        invariant_solution == {(d, d, d)},
    )
    check(
        "primitive positive democratic covector is epsilon=(1,1,1)",
        all(
            epsilon.T * permutation_matrix(permutation) == epsilon.T
            for permutation in permutations(range(3))
        )
        and integer_gcd(tuple(int(entry) for entry in epsilon)) == 1,
    )

    transfer_c = sp.simplify(q_nc.subs(n, 3).inv() * center)
    augmentation_c = sp.simplify(epsilon.T * transfer_c)
    augmentation_solutions = sp.solve(
        list(augmentation_c - lam * epsilon.T), (c, lam), dict=True
    )
    check(
        "augmentation eigencondition independently returns c=2, lambda=7/3",
        augmentation_solutions
        == [{c: 2, lam: sp.Rational(7, 3)}],
    )
    pencil = sp.factor((lam * q_2 - center).det())
    check(
        "source-built pencil factors without target insertion",
        pencil == (3 * lam - 7) * (lam**2 - 2 * lam + 2),
    )

    mutant_center = sp.simplify(diamond.subs({n: 3, c: 2, s: 2, t: 0}))
    mutant_column_sums = sp.simplify(ONE.T * mutant_center)
    check(
        "diamond mutant s=2 moves the center column sums and pencil",
        mutant_column_sums == sp.Matrix([[22, 13, 5]])
        and mutant_column_sums != ONE.T * center
        and sp.factor((lam * q_2 - mutant_center).det()) != pencil,
    )

    check(
        "Q_c source exposes c as its only displayed ladder parameter",
        source_contains(
            "verification/v568_bit_selector_ladder.py",
            "def Qc(c):",
            "return sp.Matrix([[3, 1, 0], [3, 2, 0], [3, c, 1]])",
            "forces 2c = 4, c = 2",
            "THE PHYSICAL SELECTION IS NOT DERIVED",
        ),
    )
    check(
        "centered-diamond source fixes C as the affine midpoint",
        source_contains(
            "verification/v95_centered_diamond.py",
            "C := M(1,0) = (R+L)/2 = (K+F)/2",
            "C = R + Q * sp.diag(1, 0, 0)",
            "Q = U + V",
            "R = C - U",
        ),
    )
    check(
        "independent corpus provenance contains the democratic object",
        source_contains(
            "verification/v574_stageb_winding.py",
            "exactly ONE is uniform: (3,3,3), the compiler",
        )
        and source_contains(
            "verification/v96_branch_kernel_selection.py",
            "right kernel w = 1 = (1,1,1)",
            "democratic vector",
        ),
    )

    verdict = (
        "CANONICAL(proof: ladder c=2 + centered cross; "
        "column sums forced, not smuggled)"
    )
    print("  SYMBOLIC Q SUMS: (3n,3+c,1); n=3 and independent ladder "
          "c=2 force (9,5,1).")
    print("  SYMBOLIC C SUMS: (3n+4,13,5); C is c-independent and its "
          "third-column 5 is inherited from R.")
    print("  AUGMENTATION: epsilon is the unique primitive positive "
          "S3-invariant family covector.")
    print("  LIMIT: v568 itself types the physical ladder-selection reason "
          "as conditional; this proof closes provenance, not seam realization.")
    print(f"  VERDICT Q: {verdict}")
    return verdict


def main() -> int:
    """Run both exact bridge audits."""
    print("W/Q BRIDGE CANONICALITY PROBE")
    print("Arithmetic: exact ZZ/QQ/SymPy only; no fitting or target-built matrices")
    verdict_w = bridge_w()
    verdict_q = bridge_q()

    failed = [label for label, passed in CHECKS if not passed]
    print("\nFINAL VERDICTS")
    print(f"  W: {verdict_w}")
    print(f"  Q: {verdict_q}")
    print("  S4 remainder: 2 -> 1 (Q provenance closes; W seam-form remains)")
    print(f"\nCHECKS: {len(CHECKS) - len(failed)}/{len(CHECKS)} passed")
    if failed:
        print("FAILED:")
        for label in failed:
            print(f"  - {label}")
        return 1
    print("ALL PASS")
    print("FIREWALL: exploration-only; no status, paper, ledger, or contract edit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
