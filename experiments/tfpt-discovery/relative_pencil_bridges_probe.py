#!/usr/bin/env python3
"""Independent exact audit of four proposed relative-pencil bridges.

EXPLORATION ONLY.  The probe rebuilds every algebraic object inline, uses
SymPy exact arithmetic, and writes only to stdout.  Corpus files are inspected
only to establish provenance; no verification module is imported.
"""

from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[2]
CHECKS: list[tuple[str, bool]] = []

EXACT_VERIFIED = "EXACT_VERIFIED"
EXACT_VERIFIED_PROVENANCE_UNVERIFIED = (
    "EXACT_VERIFIED_PROVENANCE_UNVERIFIED"
)
INTERPRETIVE_C = "INTERPRETIVE[C]"
REFUTED = "REFUTED"
VERDICT_ENUM = {
    EXACT_VERIFIED,
    EXACT_VERIFIED_PROVENANCE_UNVERIFIED,
    INTERPRETIVE_C,
    REFUTED,
}


def check(label: str, condition: bool) -> None:
    """Record and print one deterministic check."""
    passed = bool(condition)
    CHECKS.append((label, passed))
    print(f"{'PASS' if passed else 'FAIL'}  {label}")


def positive_snf_diagonal(matrix: sp.Matrix) -> tuple[int, ...]:
    """Return positive Smith invariant factors, including no zero padding."""
    smith = smith_normal_form(matrix, domain=sp.ZZ)
    return tuple(
        abs(int(smith[index, index]))
        for index in range(min(smith.shape))
        if smith[index, index] != 0
    )


def primitive_integer_vector(vector: sp.Matrix) -> sp.Matrix:
    """Clear denominators and divide by the gcd, fixing the first sign."""
    denominator = sp.ilcm(*(sp.denom(entry) for entry in vector))
    integral = sp.Matrix([int(entry * denominator) for entry in vector])
    divisor = sp.igcd(*(abs(entry) for entry in integral if entry))
    primitive = integral.applyfunc(lambda entry: entry // divisor)
    first_nonzero = next(entry for entry in primitive if entry)
    return -primitive if first_nonzero < 0 else primitive


def source_contains(relative_path: str, *needles: str) -> bool:
    """Check provenance without executing or importing a corpus module."""
    source = (ROOT / relative_path).read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


def claim_1_relative_pencil() -> str:
    print("\nCLAIM 1 — RELATIVE PENCIL")
    t, lam = sp.symbols("t lam")
    epsilon = sp.ones(3, 1)
    q_t = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, t, 1]])
    center = sp.Matrix([[4, 3, 0], [4, 5, 2], [5, 5, 3]])
    transfer_t = sp.simplify(q_t.inv() * center)
    augmentation = sp.simplify(epsilon.T * transfer_t)
    expected_augmentation = sp.Matrix(
        [[sp.Rational(7, 3), sp.Rational(19, 3) - 2 * t,
          sp.Rational(19, 3) - 2 * t]]
    )
    check("epsilon^T Q_t^-1 C has the claimed symbolic form",
          augmentation == expected_augmentation)

    eigen_equations = [
        sp.expand(entry)
        for entry in augmentation - lam * epsilon.T
    ]
    eigen_solutions = sp.solve(eigen_equations, (t, lam), dict=True)
    check("augmentation eigencondition uniquely gives t=2, lambda=7/3",
          eigen_solutions == [{lam: sp.Rational(7, 3), t: 2}])
    check("the genuine t=0 twin fails the augmentation eigencondition",
          len(set(augmentation.subs(t, 0))) != 1)

    q_2 = q_t.subs(t, 2)
    transfer = transfer_t.subs(t, 2)
    pencil = sp.expand((lam * q_2 - center).det())
    expected_pencil = 3 * lam**3 - 13 * lam**2 + 20 * lam - 14
    check("det(lambda Q_2-C)=3 lambda^3-13 lambda^2+20 lambda-14",
          pencil == expected_pencil)
    check("pencil factors as (3 lambda-7)(lambda^2-2 lambda+2)",
          sp.factor(pencil)
          == (3 * lam - 7) * (lam**2 - 2 * lam + 2))
    check("Spec(Q_2^-1 C)={7/3,1+i,1-i}",
          transfer.eigenvals()
          == {
              sp.Rational(7, 3): 1,
              1 + sp.I: 1,
              1 - sp.I: 1,
          })

    residue = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
    winding = residue + 6 * sp.ones(3, 1) * sp.Matrix([[1, 0, 0]])
    sheet = q_2 * sp.diag(0, 1, 1)
    delta_q = (epsilon.T * sheet**2 * epsilon)[0]
    check("coefficient tuple equals (N_fam,Delta_Q,det L,det C)",
          (3, delta_q, winding.det(), center.det()) == (3, 13, 20, 14))

    radial = primitive_integer_vector(
        (3 * transfer - 7 * sp.eye(3)).nullspace()[0]
    )
    cm_operator = sp.simplify(
        transfer**2 - 2 * transfer + 2 * sp.eye(3)
    )
    cm_basis_1 = sp.Matrix([-1, 1, 0])
    cm_basis_2 = sp.Matrix([0, -1, 1])
    cm_basis = sp.Matrix.hstack(cm_basis_1, cm_basis_2)
    block = (cm_basis.T * cm_basis).inv() * cm_basis.T * transfer * cm_basis
    expected_block = sp.Matrix([[1, 1], [-1, 1]])
    check("primitive radial lattice is Z(4,18,3)",
          radial == sp.Matrix([4, 18, 3]))
    check("CM plane is exactly x+y+z=0",
          cm_operator.rref()[0]
          == sp.Matrix([[1, 1, 1], [0, 0, 0], [0, 0, 0]]))
    check("chosen saturated CM basis gives A=[[1,1],[-1,1]]",
          block == expected_block)

    j_zero = expected_block - sp.eye(2)
    block_mod_2 = expected_block.applyfunc(lambda entry: entry % 2)
    check("J0=A-I satisfies J0^2=-I",
          j_zero**2 == -sp.eye(2))
    check("A mod 2 is the all-one block and squares to zero",
          block_mod_2 == sp.ones(2)
          and (block_mod_2**2).applyfunc(lambda entry: entry % 2)
          == sp.zeros(2))

    basis_change = sp.Matrix.hstack(radial, cm_basis_1, cm_basis_2)
    saturated_index = abs(int(basis_change.det()))
    check("radial plus saturated CM lattice has index 25",
          saturated_index == 25
          and positive_snf_diagonal(basis_change) == (1, 1, 25))
    alternate_saturated = sp.Matrix.hstack(
        radial, cm_basis_1 + cm_basis_2, cm_basis_2
    )
    nonsaturated = sp.Matrix.hstack(
        radial, 2 * cm_basis_1, cm_basis_2
    )
    check("saturated basis changes preserve 25; arbitrary choices do not",
          abs(int(alternate_saturated.det())) == 25
          and abs(int(nonsaturated.det())) == 50
          and positive_snf_diagonal(nonsaturated) == (1, 1, 50))

    check("Q_2 provenance: corpus Q(c) family and 0/2 twins",
          source_contains(
              "verification/v568_bit_selector_ladder.py",
              "def Qc(c):",
              "return sp.Matrix([[3, 1, 0], [3, 2, 0], [3, c, 1]])",
              "order_coords(Qc(0))",
              "order_coords(Qc(2))",
          ))
    check("C provenance: corpus centered flavor operator",
          source_contains(
              "verification/v95_centered_diamond.py",
              "C = R + Q * sp.diag(1, 0, 0)",
              "C == sp.Matrix([[4, 3, 0], [4, 5, 2], [5, 5, 3]])",
          ))
    check("Delta_Q=13 and det L=20 are genuine corpus quantities",
          source_contains(
              "verification/v410_sheet_generator_binary.py",
              "DELTA_Q = 13",
              "(ONE.T * V**2 * ONE)[0] == DELTA_Q",
          )
          and source_contains(
              "verification/v135_det_surface.py",
              "(det R, det C, det L) = (8, 14,",
              "20)",
          ))

    q_snf = positive_snf_diagonal(q_2)
    center_snf = positive_snf_diagonal(center)
    check("circularity audit invariants are exact",
          tuple(epsilon.T * q_2) == (9, 5, 1)
          and tuple(epsilon.T * center) == (13, 13, 5)
          and q_2.det() == 3 and q_snf == (1, 1, 3)
          and center.det() == 14 and center_snf == (1, 1, 14))

    perturbed_center = center + sp.diag(0, 0, 1)
    perturbed_pencil = sp.factor((lam * q_2 - perturbed_center).det())
    check("mutant C+E33 breaks the claimed factorization",
          perturbed_pencil
          != (3 * lam - 7) * (lam**2 - 2 * lam + 2))

    print("  PROVENANCE: Q_t/Q_0/Q_2 are corpus objects at "
          "verification/v568_bit_selector_ladder.py:91-92,175-184; "
          "C is corpus at verification/v95_centered_diamond.py:45-56,80-82.")
    print("  INDEX: 25 is intrinsic only for the primitive radial line plus "
          "the saturated CM-plane lattice; nonsaturated generators give "
          "multiples such as 50.")
    print("  CIRCULARITY: carrier 5 is already visible in the column sums of "
          "both Q_2 and C.  Their determinants/SNFs do not recover 5.  A "
          "P2 replacement therefore requires independent proofs that Q, C, "
          "Q^-1 C, and epsilon are canonically forced by seam geometry "
          "without using the carrier selector.")
    return INTERPRETIVE_C


def claim_2_anchor_moments() -> str:
    print("\nCLAIM 2 — ANCHOR MOMENTS")
    n = sp.symbols("n", integer=True, nonnegative=True)

    def moment(index: sp.Expr) -> sp.Expr:
        return 2 + 2**index

    check("p_n=2*1^n+1*2^n is the measure 2 delta_1+delta_2",
          sp.simplify(moment(n) - (2 * 1**n + 2**n)) == 0)
    hankel_2 = sp.simplify(
        moment(n) * moment(n + 2) - moment(n + 1)**2
    )
    check("symbolic 2x2 Hankel identity is 2^(n+1)",
          sp.simplify(hankel_2 - 2**(n + 1)) == 0)
    check("2x2 Hankel identity holds numerically for n=0..12",
          all(
              moment(index) * moment(index + 2)
              - moment(index + 1)**2 == 2**(index + 1)
              for index in range(13)
          ))
    hankel_3 = sp.Matrix(
        3, 3, lambda row, column: moment(n + row + column)
    )
    check("all shifted 3x3 Hankel determinants vanish symbolically",
          sp.simplify(hankel_3.det()) == 0)
    check("moments satisfy p_(n+2)=3p_(n+1)-2p_n",
          sp.simplify(
              moment(n + 2) - 3 * moment(n + 1) + 2 * moment(n)
          ) == 0)

    mass = sp.Integer(3)
    alpha_0 = sp.Rational(1, mass) * (2 * 1 + 1 * 2)
    variance_numerator = (
        2 * (1 - alpha_0)**2 + (2 - alpha_0)**2
    )
    beta_1 = sp.sqrt(variance_numerator / mass)
    phi_0 = {1: 1 / sp.sqrt(mass), 2: 1 / sp.sqrt(mass)}
    phi_1 = {
        point: (point - alpha_0) / sp.sqrt(variance_numerator)
        for point in (1, 2)
    }
    alpha_1 = sp.simplify(
        sum(
            weight * point * phi_1[point]**2
            for point, weight in ((1, 2), (2, 1))
        )
    )
    beta_from_inner_product = sp.simplify(
        sum(
            weight * point * phi_0[point] * phi_1[point]
            for point, weight in ((1, 2), (2, 1))
        )
    )
    jacobi = sp.Matrix([[alpha_0, beta_1], [beta_1, alpha_1]])
    expected_jacobi = sp.Matrix([
        [sp.Rational(4, 3), sp.sqrt(2) / 3],
        [sp.sqrt(2) / 3, sp.Rational(5, 3)],
    ])
    check("orthonormalization derives the claimed Jacobi matrix",
          beta_1 == beta_from_inner_product
          and jacobi == expected_jacobi)
    check("Jacobi spectrum={1,2}, trace=3, determinant=2",
          jacobi.eigenvals() == {1: 1, 2: 1}
          and jacobi.trace() == 3 and jacobi.det() == 2)

    anchor = (1, 1, 2)
    e_1 = sum(anchor)
    e_2 = sum(
        anchor[left] * anchor[right]
        for left, right in ((0, 1), (0, 2), (1, 2))
    )
    check("Jacobi diagonal is (e1(a)/p0,e2(a)/p0)=(4/3,5/3)",
          (jacobi[0, 0], jacobi[1, 1])
          == (sp.Rational(e_1, 3), sp.Rational(e_2, 3)))
    check("anchor-moment and normalized-ratio provenance is in corpus",
          source_contains(
              "verification/v106_review_validation.py",
              "def p_sum(n):",
              "p_n(a) = 2 + 2^n",
          )
          and source_contains(
              "verification/v119_review_validation_2.py",
              "ANCHOR RATIO TRIAD",
              "sp.Rational(4, 3)",
              "sp.Rational(5, 3)",
          ))

    mutant = lambda index: 2 + 3**index
    check("mutant p_n=2+3^n breaks the 2^(n+1) Hankel law",
          mutant(0) * mutant(2) - mutant(1)**2 != 2)
    print("  PROVENANCE: p_n=2+2^n is corpus at "
          "verification/v106_review_validation.py:70-94; the normalized "
          "anchor ratios (e1,e2)/p0=(4/3,5/3) are corpus at "
          "verification/v119_review_validation_2.py:60-92.")
    return EXACT_VERIFIED


def claim_3_winding_spectrum() -> str:
    print("\nCLAIM 3 — WINDING SPECTRUM")
    residue = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
    one = sp.ones(3, 1)
    e_1_row = sp.Matrix([[1, 0, 0]])
    winding = residue + 6 * one * e_1_row
    relative = residue.inv() * winding
    expected_relative = sp.Matrix([
        [sp.Rational(5, 2), 0, 0],
        [sp.Rational(3, 2), 1, 0],
        [sp.Rational(-3, 2), 0, 1],
    ])
    check("true corpus R and L give the claimed R^-1 L",
          relative == expected_relative)
    check("Spec(R^-1 L)={5/2,1,1}",
          relative.eigenvals() == {sp.Rational(5, 2): 1, 1: 2})
    x_1, x_2, x_3 = sp.symbols("x_1 x_2 x_3")
    vector = sp.Matrix([x_1, x_2, x_3])
    fixed_residual = sp.simplify((relative - sp.eye(3)) * vector)
    check("fixed plane is exactly x_1=0",
          fixed_residual == sp.Matrix([
              sp.Rational(3, 2) * x_1,
              sp.Rational(3, 2) * x_1,
              sp.Rational(-3, 2) * x_1,
          ]))
    check("5/2 equals det L / det R",
          sp.Rational(winding.det(), residue.det())
          == sp.Rational(20, 8) == sp.Rational(5, 2))
    check("R and winding-shifted L provenance is genuine",
          source_contains(
              "verification/v4_flavor_matrix.py",
              "R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])",
              "L = R + 6 * W",
              "anchor = first column of R = (1,1,2)",
          ))
    print("  PROVENANCE: R and L=R+6*1*e1^T are corpus objects at "
          "verification/v4_flavor_matrix.py:22-24; R's first column is "
          "the anchor a=(1,1,2) at lines 57-59.")
    return EXACT_VERIFIED


def claim_4_dual_frame_klein_four() -> str:
    print("\nCLAIM 4 — DUAL FRAME KLEIN FOUR")
    residue = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
    anchor = sp.Matrix([1, 1, 2])
    one = sp.ones(3, 1)
    d = anchor.T * residue.inv()
    n = sp.Matrix([[5, -9, 6]])
    evaluation_frame = sp.Matrix.hstack(one, anchor)
    literal_block = sp.Matrix.vstack(d, n) * evaluation_frame
    integral_d = 2 * d
    integral_block = sp.Matrix.vstack(integral_d, n) * evaluation_frame
    expected_block = sp.Matrix([[0, 2], [2, 8]])

    check("d=a^T R^-1=(-1/2,-1/2,1) and n=(5,-9,6)",
          d == sp.Matrix([[
              sp.Rational(-1, 2), sp.Rational(-1, 2), 1
          ]])
          and n == sp.Matrix([[5, -9, 6]]))
    check("literal evaluations with d give [[0,1],[2,8]], not B",
          literal_block == sp.Matrix([[0, 1], [2, 8]])
          and literal_block != expected_block)
    check("primitive integral covector D=2d reconstructs reviewer B",
          integral_d == sp.Matrix([[-1, -1, 2]])
          and integral_block == expected_block)
    check("det B=-4 and SNF(B)=diag(2,2)",
          integral_block.det() == -4
          and positive_snf_diagonal(integral_block) == (2, 2))
    check("cokernel is Z2 x Z2, not Z4",
          positive_snf_diagonal(integral_block) == (2, 2)
          and integral_block.applyfunc(lambda entry: entry % 2)
          == sp.zeros(2))
    check("d and n provenance is genuine",
          source_contains(
              "verification/v225_dual_normal_frame.py",
              "d = (A.T * R.inv())",
              "n = sp.Matrix([[5, -9, 6]])",
              "list(n * L) == [L.det(), 0, 0] == [20, 0, 0]",
          ))
    check("a corpus side-blind null exists",
          source_contains(
              "verification/v521_seam_bit_rp_blind.py",
              "RP/Theta battery is side-blind",
              "EIGHTH",
          ))
    print("  PROVENANCE: d and n are corpus objects at "
          "verification/v225_dual_normal_frame.py:32-39,48-62; an explicit "
          "side-blind null is verification/v521_seam_bit_rp_blind.py:1-10.")
    print("  NORMALIZATION AUDIT: the advertised B is not the literal "
          "(d,n)-evaluation matrix.  It uses the denominator-cleared "
          "primitive integral normal D=2d; hence determinant 4 and the "
          "Klein-four cokernel are exact only after that extra normalization.")
    print("  CONCLUSION: determinant-4/Smith data cannot select cyclic mu4 "
          "gluing; its cokernel is Z2 x Z2, consistent with the corpus "
          "side-blind nulls.")
    return INTERPRETIVE_C


def main() -> int:
    verdicts = {
        "relative_pencil": claim_1_relative_pencil(),
        "anchor_moments": claim_2_anchor_moments(),
        "winding_spectrum": claim_3_winding_spectrum(),
        "dual_frame_klein_four": claim_4_dual_frame_klein_four(),
    }
    check("all claim verdicts use the frozen enum",
          set(verdicts.values()) <= VERDICT_ENUM)

    failed = [label for label, passed in CHECKS if not passed]
    print("\nCLAIM VERDICTS")
    for claim, verdict in verdicts.items():
        print(f"  {claim}: {verdict}")
    print(f"\nCHECKS: {len(CHECKS) - len(failed)}/{len(CHECKS)} passed")
    if failed:
        print("FAILED:")
        for label in failed:
            print(f"  - {label}")
        print("VERDICT: REFUTED")
        return 1
    print("ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
