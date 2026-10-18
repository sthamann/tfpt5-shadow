#!/usr/bin/env python3
r"""v1022 -- TEL-B round-3 certificates and ALG-EXH correction.

Rigorous Arb/Acb certificate for TV_p(F_pp), Ny=8 QWZ strip.

Run from the repository root with

  experiments/tfpt-discovery/.venv/bin/python \
    verification/v1022_telb_round3_certificates.py

All proof arithmetic is outward-rounded Arb/Acb arithmetic.  Binary floats are
not imported into a proof inequality.  The finite partition consists entirely
of rational endpoints and rational midpoints.  The same module certifies the
one-dimensional C2b potential bound and an exact minimal countermodel to the
old ALG2 Vandermonde implication.

For p != 0 the affine sawtooth has zero third derivative, hence the smooth
part of TV(F'') is integral ||P'''(p)||_HS dp.  The exact cut jump has HS norm
2.  Reflection of the eight-layer chain gives ||P'''(-p)||=||P'''(p)||.

At every rational midpoint, P^(j), j=3,...,8, is enclosed from the exact
commutator and idempotency recurrences in a validated Acb eigensystem.  On a
cell [c-h,c+h], Taylor's theorem in Hilbert--Schmidt norm gives

 integral ||P'''|| <= sum_{j=0}^5 2 h^(j+1)/((j+1)j!) ||P^(3+j)(c)||
                       + ||P^(9)||_cell h^7/2520.

The ninth derivative is bounded without numerical eigengaps.  If
spec(H) avoids (-g,g), differentiation of [H,P]=0 and P^2=P gives the operator
norm recurrence

 q_0=1,
 q_n <= g^-1 sum_{k=1}^n binom(n,k)q_{n-k}
        + sum_{k=1}^{n-1} binom(n,k)q_k q_{n-k}.

Here ||H^(k)||=1.  We use g>=sin(p) on (0,pi/2), and g>=1 on
(pi/2,pi), the latter from sigma_min(bI-S)>=b-1=-cos(p).

Contract boundary: this module closes the TV and potential inputs. The former
all-N CF/DG residual and relaxed TEL-B norm are supplied by v1026. ALG2 remains conditional on
FE-GEN or a precisely gauge/code-projected microscopic algebra.  Therefore
SEAM.MMST.TYPEIII.CHARGED.01 and TFPT.TOE.COMPLETE.01 remain [O].  The
certificate requires native python-flint 0.9.0; it is not a Pyodide/WASM
check.  Python-only / Wolfram mirror deferred.  NO RH CLAIM.

The tiny interval [0,1/20000] is bounded independently at the semisimple
crossing.  The seven negative bulk bands are enclosed by a radius-1/2 Riesz
circle around -1.  The central two-plane is the Riesz cluster of
K(b)=[[0,B],[B^T,0]] around zero.  Since det B=b^8, K R_c has a zero of order
eight.  A complex-disk Cauchy estimate makes the internal edge mixing
negligible; all explicit constants are recomputed below in Arb.
"""

from __future__ import annotations

from fractions import Fraction
from importlib.metadata import version
from math import comb, factorial

import flint as python_flint
from flint import acb_mat, arb, arb_mat, ctx
import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


NY = 8
DIM = 2 * NY
EPS = Fraction(1, 20000)
TARGET_TEXT = "15.928674"
K3_TARGET_TEXT = "2.517464500835"
PYTHON_FLINT_VERSION = "0.9.0"


def A(q: Fraction | int | str) -> arb:
    """Exact rational/decimal-to-Arb conversion (never through float)."""
    if isinstance(q, Fraction):
        return arb(q.numerator) / q.denominator
    return arb(q)


def hamiltonian_jets(p: arb, max_order: int) -> list[acb_mat]:
    """H^(j)(p), in the (+ then -) sigma_x basis, j=0..max_order."""
    s, c = p.sin(), p.cos()
    out: list[acb_mat] = []
    for order in range(max_order + 1):
        r = order % 4
        if order == 0:
            aa, bb = s, 1 - c
        elif r == 0:
            aa, bb = s, -c
        elif r == 1:
            aa, bb = c, s
        elif r == 2:
            aa, bb = -s, c
        else:
            aa, bb = -c, -s
        matrix = arb_mat(DIM, DIM)
        for y in range(NY):
            matrix[y, y] = aa
            matrix[NY + y, NY + y] = -aa
            matrix[y, NY + y] = bb
            matrix[NY + y, y] = bb
        if order == 0:
            # B=bI-S, with S the strict upper shift.
            for y in range(NY - 1):
                matrix[y, NY + y + 1] = -1
                matrix[NY + y + 1, y] = -1
        out.append(acb_mat(matrix))
    return out


def commutator(x: acb_mat, y: acb_mat) -> acb_mat:
    return x * y - y * x


def derivative_enclosures(p: arb, max_order: int = 8) -> list[acb_mat]:
    """Validated enclosures of P^(0),...,P^(max_order) at one point."""
    hs = hamiltonian_jets(p, max_order)
    eigenvalues, left, right = hs[0].eig(
        left=True, right=True, algorithm="rump"
    )
    occupied: list[int] = []
    for value in eigenvalues:
        if value.real.upper() < 0:
            occupied.append(1)
        elif value.real.lower() > 0:
            occupied.append(0)
        else:
            raise ArithmeticError("an eigenvalue enclosure meets zero")
    if sum(occupied) != NY:
        raise ArithmeticError("the negative spectral subspace has wrong rank")

    transformed_h = [left * item * right for item in hs]
    derivatives = [acb_mat(DIM, DIM)]
    for i in range(DIM):
        derivatives[0][i, i] = occupied[i]

    for order in range(1, max_order + 1):
        same_block = acb_mat(DIM, DIM)
        for k in range(1, order):
            same_block += comb(order, k) * (
                derivatives[k] * derivatives[order - k]
            )

        rhs = acb_mat(DIM, DIM)
        for k in range(1, order + 1):
            rhs -= comb(order, k) * commutator(
                transformed_h[k], derivatives[order - k]
            )

        derivative = acb_mat(DIM, DIM)
        for i in range(DIM):
            for j in range(DIM):
                if occupied[i] == occupied[j]:
                    derivative[i, j] = (
                        -same_block[i, j]
                        if occupied[i]
                        else same_block[i, j]
                    )
                else:
                    derivative[i, j] = rhs[i, j] / (
                        eigenvalues[i] - eigenvalues[j]
                    )
        derivatives.append(derivative)

    return [right * derivative * left for derivative in derivatives]


def hs_upper(matrix: acb_mat) -> arb:
    """An outward upper enclosure for the Hilbert--Schmidt norm."""
    square = arb(0)
    for value in matrix.entries():
        upper = abs(value).upper()
        square += arb(upper) * arb(upper)
    return square.sqrt()


def projector_derivative_majorant(gap: arb, order: int) -> arb:
    """Operator-norm q_order from the block Sylvester recurrence."""
    q = [arb(1)]
    for n in range(1, order + 1):
        cross = arb(0)
        for k in range(1, n + 1):
            cross += comb(n, k) * q[n - k]
        cross /= gap
        diagonal = arb(0)
        for k in range(1, n):
            diagonal += comb(n, k) * q[k] * q[n - k]
        q.append(cross + diagonal)
    return q[order]


def crossing_interval_bound() -> tuple[arb, dict[str, arb]]:
    """Uniform HS bound for ||P'''|| on 0<=p<=EPS."""
    eps = A(EPS)

    # Seven negative bulk bands: circle centre -1, radius 1/2.
    d_bulk = arb(1) / 2 - eps
    bulk_op = (arb(1) / 2) * (
        d_bulk ** -2 + 6 * d_bulk ** -3 + 6 * d_bulk ** -4
    )
    bulk_hs = 4 * bulk_op

    # Central two-plane R(b), with b<=p^2/2.  R_b derivatives follow from
    # the radius-1/2 Riesz circle around the two zero modes of K(0).
    d_central = arb(1) / 2 - eps**2 / 2
    rb1 = (arb(1) / 2) * d_central ** -2
    rb2 = (arb(1) / 2) * 2 * d_central ** -3
    rb3 = (arb(1) / 2) * 6 * d_central ** -4
    r_ppp_op = rb3 * eps**3 + 3 * rb2 * eps + rb1 * eps
    central_base_hs = 4 * r_ppp_op

    # Internal splitting correction.  G(b)=K(b)R(b) is operator-valued
    # holomorphic on |b|<1/2.  On the real axis, R is the orthogonal central
    # projector, so ||G(b)||=s_min(B(b)).  Since det B=b^8 and the seven
    # largest singular values are >=1-|b| (Weyl from B(0)=-S),
    # ||G(b)||<=|b|^8/(1-|b|)^7.  Entrywise holomorphy then forces the first
    # eight Taylor coefficients of G to vanish: G=b^8 W.  On |b|=1/4 the
    # Riesz-Neumann bounds ||R||<=2 and ||K||<=5/4 give, conservatively,
    # ||G||<=5/2 and hence ||W||<=(5/2)4^8.  Move to |p|=1/10.
    radius = arb(1) / 10
    b_circle = radius.cosh() - 1
    sin_circle_lower = 2 * radius - radius.sinh()
    kr_boundary_bound = arb(5) / 2
    t_sup = (
        kr_boundary_bound
        * arb(4) ** 8
        * b_circle**8
        / sin_circle_lower
    )
    scalar_factor = (1 - t_sup**2).rsqrt()
    r_circle_norm = (arb(1) / 2) / (arb(1) / 2 - b_circle)
    edge_error_sup = (
        t_sup * scalar_factor
        + r_circle_norm * (scalar_factor - 1)
    )
    edge_error_ppp_hs = (
        4 * factorial(3) * edge_error_sup / (radius - eps) ** 3
    )

    total = bulk_hs + central_base_hs + edge_error_ppp_hs
    return total, {
        "bulk_hs": bulk_hs,
        "central_base_hs": central_base_hs,
        "edge_mixing_hs": edge_error_ppp_hs,
        "t_complex_disk": t_sup,
        "kr_boundary_bound": kr_boundary_bound,
    }


# All endpoints are exact rationals.  Counts are deliberately fixed rather
# than selected from an inexact runtime heuristic.
SEGMENTS: tuple[tuple[Fraction, Fraction, int, str], ...] = (
    (Fraction(1, 20000), Fraction(1, 10000), 953, "sin-left"),
    (Fraction(1, 10000), Fraction(1, 5000), 757, "sin-left"),
    (Fraction(1, 5000), Fraction(1, 2500), 601, "sin-left"),
    (Fraction(1, 2500), Fraction(1, 1250), 477, "sin-left"),
    (Fraction(1, 1250), Fraction(1, 625), 379, "sin-left"),
    (Fraction(1, 625), Fraction(2, 625), 301, "sin-left"),
    (Fraction(2, 625), Fraction(4, 625), 239, "sin-left"),
    (Fraction(4, 625), Fraction(8, 625), 190, "sin-left"),
    (Fraction(8, 625), Fraction(16, 625), 151, "sin-left"),
    (Fraction(16, 625), Fraction(32, 625), 120, "sin-left"),
    (Fraction(32, 625), Fraction(64, 625), 96, "sin-left"),
    (Fraction(64, 625), Fraction(128, 625), 77, "sin-left"),
    (Fraction(128, 625), Fraction(256, 625), 103, "sin-left"),
    (Fraction(256, 625), Fraction(512, 625), 205, "sin-left"),
    (Fraction(512, 625), Fraction(3, 2), 341, "sin-left"),
    (Fraction(3, 2), Fraction(1570797, 1000000), 36, "gap-0.99"),
    (Fraction(1570797, 1000000), Fraction(3141593, 1000000), 786, "gap-one"),
)


def segment_gap(left: Fraction, mode: str) -> arb:
    if mode == "sin-left":
        return A(left).sin().lower()
    if mode == "gap-0.99":
        return arb("0.99")
    if mode == "gap-one":
        return arb(1)
    raise ValueError(mode)


def certify_segment(
    left: Fraction, right: Fraction, count: int, gap_mode: str
) -> tuple[arb, arb, arb]:
    length = right - left
    half_width_q = length / (2 * count)
    half_width = A(half_width_q)
    gap = arb(segment_gap(left, gap_mode))
    p9_hs = 4 * projector_derivative_majorant(gap, 9)

    midpoint_sum = arb(0)
    correction_sum = arb(0)
    for cell in range(count):
        center_q = left + Fraction(2 * cell + 1, 2 * count) * length
        derivatives = derivative_enclosures(A(center_q), 8)
        norms = [hs_upper(derivatives[n]) for n in range(3, 9)]
        midpoint_sum += 2 * half_width * norms[0]
        for j in range(1, 6):
            correction_sum += (
                2
                * half_width ** (j + 1)
                * norms[j]
                / ((j + 1) * factorial(j))
            )

    # count*h^7/2520 = length*h^6/5040.
    remainder = p9_hs * A(length) * half_width**6 / 5040
    return midpoint_sum, correction_sum, remainder


def tv_certificate() -> dict[str, object]:
    target = A(TARGET_TEXT)
    print("TV(F_pp) outward Arb/Acb certificate; Ny=8")
    print("precision_bits", ctx.prec)
    print("partition_cells", sum(row[2] for row in SEGMENTS))

    # Exact structural guards used in the proof.
    pi = arb.pi()
    structural = (
        A(Fraction(1570797, 1000000)).lower() > (pi / 2).upper()
        and A(Fraction(3141593, 1000000)).lower() > pi.upper()
        and A(Fraction(3141593, 1000000)).upper() < (3 * pi / 2).lower()
        and NY == 8
    )
    print("structural_guards", structural)

    low_actual_bound, low_parts = crossing_interval_bound()
    low_rounded_bound = arb(297)
    low_ok = low_actual_bound.upper() < low_rounded_bound
    print("crossing_bulk_hs", low_parts["bulk_hs"])
    print("crossing_central_base_hs", low_parts["central_base_hs"])
    print("crossing_edge_mixing_hs", low_parts["edge_mixing_hs"])
    print("crossing_KR_boundary_bound", low_parts["kr_boundary_bound"])
    print("crossing_t_complex_disk", low_parts["t_complex_disk"])
    print("crossing_total_hs", low_actual_bound)
    print("crossing_rounded_bound", low_rounded_bound, "ok", low_ok)

    positive_half = A(EPS) * low_rounded_bound
    midpoint_total = arb(0)
    correction_total = arb(0)
    remainder_total = arb(0)
    for index, (left, right, count, mode) in enumerate(SEGMENTS, start=1):
        midpoint, correction, remainder = certify_segment(
            left, right, count, mode
        )
        midpoint_total += midpoint
        correction_total += correction
        remainder_total += remainder
        print(
            "segment",
            index,
            str(left),
            str(right),
            "cells",
            count,
            "mid",
            midpoint,
            "corr",
            correction,
            "rem",
            remainder,
        )

    positive_half += midpoint_total + correction_total + remainder_total
    smooth_tv = 2 * positive_half
    # Exact cut jump: each end contributes the adjacent-site second
    # derivative |e1><e0|+|e0><e1|.  The two end blocks have disjoint
    # support, so the Hilbert--Schmidt square is 2+2=4.
    edge_jump = sp.Matrix([[0, 1], [1, 0]])
    cut_jump_matrix = sp.diag(edge_jump, edge_jump)
    jump_hs_square = sp.trace(cut_jump_matrix.T * cut_jump_matrix)
    suite_check("TV cut-jump Hilbert--Schmidt square is exactly 4",
                jump_hs_square == 4)
    jump_tv = arb(int(jump_hs_square)).sqrt()
    total_tv = smooth_tv + jump_tv
    k3_tv = total_tv / (2 * arb.pi())
    passed = structural and low_ok and total_tv.upper() < target

    print("midpoint_integral_positive", midpoint_total)
    print("taylor_correction_positive", correction_total)
    print("ninth_derivative_remainder_positive", remainder_total)
    print("crossing_interval_contribution_positive", A(EPS) * low_rounded_bound)
    print("smooth_TV_enclosure", smooth_tv)
    print("jump_TV_exact", jump_tv)
    print("TV_p_F_pp_enclosure", total_tv)
    print("K3_TV_enclosure", k3_tv)
    print("target", target)
    print("VERDICT", "TV_FPP_PROVED" if passed else "TV_FPP_NOT_PROVED")
    suite_check("TV uses exactly 5812 rational cells", sum(row[2] for row in SEGMENTS) == 5812)
    suite_check("TV structural spectral guards", structural)
    suite_check("TV crossing interval bound is below 297", low_ok)
    suite_check("TV cut jump is exactly 2", jump_tv == arb(2))
    suite_check("TV_p(F'') outward enclosure is below 15.928674", total_tv.upper() < target)
    suite_check("K3_TV outward enclosure is below 2.517464500835", k3_tv.upper() < A(K3_TARGET_TEXT))
    return {
        "passed": passed,
        "total_tv": total_tv,
        "smooth_tv": smooth_tv,
        "jump_tv": jump_tv,
        "k3_tv": k3_tv,
    }

def c2b_scalar_certificate() -> dict[str, object]:
    """Certify the scalar C2b terms; CF and DG are independently supplied by v1026."""
    # The all-n rational tail inequalities quoted in the analytic proof
    # reduce, after n=x+16, to positive-coefficient polynomials divided by
    # positive denominators.  This closes the only symbolic tail arithmetic
    # used below; the digamma/midpoint enclosure supplying these two
    # rational majorants is the standard analytic lemma stated in the paper.
    x = sp.symbols("x", nonnegative=True)
    n = x + 16
    positive_tail_margin = sp.factor(
        sp.Rational(26, 100) / n
        - sp.Rational(1, 4) / (n + sp.Rational(3, 4))
        - sp.Rational(1, 12) / (n + sp.Rational(3, 4)) ** 2
    )
    negative_tail_margin = sp.factor(
        sp.Rational(38, 100) / n
        - sp.Rational(3, 4) / (n - sp.Rational(1, 2))
        + sp.Rational(1, 2) / (n + sp.Rational(1, 4))
        - sp.Rational(1, 24) / (n - 1) ** 2
    )
    pos_num, pos_den = sp.fraction(positive_tail_margin)
    neg_num, neg_den = sp.fraction(negative_tail_margin)
    suite_check(
        "C2b epsilon-plus rational tail margin is positive for n>=16",
        all(value > 0 for value in sp.Poly(pos_num, x).all_coeffs())
        and all(value > 0 for value in sp.Poly(pos_den, x).all_coeffs()),
    )
    suite_check(
        "C2b epsilon-minus rational tail margin is positive for n>=16",
        all(value > 0 for value in sp.Poly(neg_num, x).all_coeffs())
        and all(value > 0 for value in sp.Poly(neg_den, x).all_coeffs()),
    )
    def q(text: str) -> arb:
        return arb(text)
    
    
    def assert_lt(x: arb, y: arb, label: str) -> None:
        suite_check(f"C2b {label}", x < y)
    
    
    def assert_gt(x: arb, y: arb, label: str) -> None:
        suite_check(f"C2b {label}", x > y)
    
    
    pi = arb.pi()
    A = 1 / (2 * pi**2)
    zeta2 = pi**2 / 6
    
    # Exact special entries of epsilon.  The remaining entries are
    #   eps_+(n) = int_n^{n+1} log(t)dt - psi(n+3/4),
    #   eps_-(n) = int_{n-1}^n log(t)dt - psi(n+1/4).
    eps_zero = -(q(3) / 4).digamma() - 1
    eps_minus_one = -1 - (q(5) / 4).digamma()
    assert_lt(abs(eps_zero), q("0.086"), "epsilon zero")
    assert_lt(abs(eps_minus_one), q("0.773"), "epsilon minus one")
    
    
    def eps_plus(n: int) -> arb:
        nn = arb(n)
        return (nn + 1) * (nn + 1).log() - nn * nn.log() - 1 - (
            nn + q(3) / 4
        ).digamma()
    
    
    def eps_minus(n: int) -> arb:
        nn = arb(n)
        integral = -1 if n == 1 else (
            nn * nn.log() - (nn - 1) * (nn - 1).log() - 1
        )
        return integral - (nn + q(1) / 4).digamma()
    
    
    # The finite exceptional range.  For n >= 16 the report proves the same
    # inequalities from the classical two-term digamma enclosure and midpoint
    # quadrature, using rational inequalities only.
    for n in range(1, 16):
        ep = eps_plus(n)
        em = eps_minus(n)
        assert_gt(ep, 0, f"epsilon plus sign n={n}")
        assert_lt(ep, q("0.26") / n, f"epsilon plus n={n}")
        assert_lt(em, 0, f"epsilon minus sign n={n}")
        if n == 1:
            assert_lt(-em, q("0.773"), "epsilon minus n=1")
        else:
            assert_lt(-em, q("0.38") / n, f"epsilon minus n={n}")
    
    # Uniform l2 estimate, including k=0.  The negative n=1 term is split off;
    # |eps_-(n)| <= .38/n for n>=2 and |eps_+(n)| <= .26/n.
    eps_l2_sq = (
        q("0.086") ** 2
        + q("0.773") ** 2
        + q("0.38") ** 2 * (zeta2 - 1)
        + q("0.26") ** 2 * zeta2
    )
    eps_l2 = eps_l2_sq.sqrt()
    assert_lt(eps_l2, q("0.900"), "epsilon l2")
    
    # Multiplier b(theta)=|1-lambda(theta)|/|theta|.  The partial-fraction
    # proof in the report gives b<=3.725 on |theta|<=1/2 and b<=5.5 on
    # |theta|<=3/4.  The latter is used only in the middle seam triangle.
    B_HALF = q("3.725")
    B_THREE_QUARTERS = q("5.5")
    
    # Interior epsilon contribution.  Sum_{k,l}|e_l-e_k|^2 <= 2N||e||_2^2.
    c_eps_interior = 2**q("0.5") * A * B_HALF * eps_l2
    
    # Middle seam, 1/2<|theta|<=3/4.  Its triangular cross-sign geometry gives
    # a harmonic rather than N-fold multiplicity.  H_m/m decreases, so N=16
    # (m=8) is the endpoint.
    H8 = sum((arb(1) / j for j in range(1, 9)), arb(0))
    c_eps_mid_sq = (
        4
        * A**2
        * B_THREE_QUARTERS**2
        * (q("0.38") ** 2 + q("0.26") ** 2)
        * H8
        / 16
    )
    c_eps_mid = c_eps_mid_sq.sqrt()
    
    # Far seam, |theta|>3/4.  If r=N-|l-k|, there are r cross-sign pairs per
    # orientation, both indices exceed N/4, and
    # b(1-r/N) <= 2 + pi*N/(2r).  Replacing R by N/4 and using monotonicity of
    # H_{N/4}/N gives the displayed N=16 envelope.
    H4 = sum((arb(1) / j for j in range(1, 5)), arb(0))
    far_sum_over_n3 = (
        1 / q(128)
        + 1 / q(512)
        + pi / 32
        + pi**2 * H4 / 64
    )
    c_eps_far_sq = (
        2 * A**2 * (4 * (q("0.38") + q("0.26"))) ** 2 * far_sum_over_n3
    )
    c_eps_far = c_eps_far_sq.sqrt()
    
    c_eps = (c_eps_interior**2 + c_eps_mid**2 + c_eps_far**2).sqrt()
    assert_lt(c_eps, q("0.289"), "complete epsilon multiplier term")
    
    # zeta_k = Phi(kh)-cellmean(Phi)+phi_N(k).  Convexity and the 3/4-rule
    # Peano kernel give a stronger increment estimate because the two pieces
    # have opposite sign.
    m = pi**2 / 3
    M = pi**2 - 4
    c_phi_low = (9 * m - M) / 32
    c_phi_high = (9 * M - m) / 32
    c_zeta_increment = M / 2 - c_phi_low
    assert_gt(m / 2, c_phi_high, "zeta increments have one sign")
    assert_lt(c_zeta_increment, q("2.193"), "zeta increment constant")
    
    # For |j|<=N/2 use sin(pi*j/N)>=2j/N and N>=16.  For the seam use
    # the r-pair count and H_{N/2}/N <= H_8/16.
    c_zeta_interior = A * pi * c_zeta_increment / 8
    c_zeta_seam_sq = A**2 * pi**2 * c_zeta_increment**2 * H8 / 32
    c_zeta_seam = c_zeta_seam_sq.sqrt()
    c_zeta = (c_zeta_interior**2 + c_zeta_seam**2).sqrt()
    assert_lt(c_zeta, q("0.111"), "complete zeta multiplier term")
    
    c_potential = c_eps + c_zeta
    assert_lt(c_potential, q("0.399224424139108"),
              "all one-dimensional potential terms: explicit v1026 input cap")
    
    # With an orthogonal diagonal bound c_diag<=.06, the historical
    # coefficient-freezing budget may be as large as the following number and
    # C2b would nevertheless close at .542702.
    target = q("0.542702")
    diag_budget = q("0.06")
    coefficient_budget = (target**2 - diag_budget**2).sqrt() - c_potential
    assert_gt(coefficient_budget, q("0.139"), "remaining coefficient budget")
    
    print("C2B_SCALAR_PART_PROVED")
    print(f"eps_zero                  = {eps_zero}")
    print(f"eps_minus_one             = {eps_minus_one}")
    print(f"epsilon_l2_upper          = {eps_l2}")
    print(f"c_epsilon_interior        = {c_eps_interior}")
    print(f"c_epsilon_middle_seam     = {c_eps_mid}")
    print(f"c_epsilon_far_seam        = {c_eps_far}")
    print(f"c_epsilon_total           = {c_eps}")
    print(f"c_zeta_increment          = {c_zeta_increment}")
    print(f"c_zeta_total              = {c_zeta}")
    print(f"c_potential_total         = {c_potential}")
    print(f"coefficient_budget_if_diag_0.06 = {coefficient_budget}")
    print("FULL_C2B_NOT_PROVED_BY_THIS_MODULE: CF/DG are supplied by v1026")
    
    print("CLAIM_FENCE: the former CF/DG residual is closed by v1026, not here")
    return {
        "c_epsilon": c_eps,
        "c_zeta": c_zeta,
        "c_potential": c_potential,
        "coefficient_budget": coefficient_budget,
    }
    


def alg2_countermodel() -> None:
    """Exact M2-versus-even-subalgebra countermodel to the old ALG2 step."""
    c = ((0, 1), (0, 0))

    def apply(matrix, vector):
        return tuple(
            sum(matrix[i][j] * vector[j] for j in range(2))
            for i in range(2)
        )

    vacuum = (1, 0)
    occupied = (0, 1)
    b = sp.Symbol("b", real=True)
    y = ((0, 0), (0, b))
    difference = tuple(
        apply(c, occupied)[i] - apply(y, occupied)[i]
        for i in range(2)
    )
    squared_norm = sum(entry * entry for entry in difference)
    suite_check(
        "ALG2 exact even-algebra compression distance is at least one",
        sp.simplify(squared_norm - (1 + b**2)) == 0,
    )
    suite_check("ALG2 full CAR contains the annihilator", apply(c, occupied) == vacuum)
    suite_check("ALG2 annihilator kills the vacuum", apply(c, vacuum) == (0, 0))
    print("ALG2_VANDERMONDE_IMPLICATION_REFUTED")
    print("Required replacement: FE-GEN compression-surjectivity for B_N^gen")


def run() -> int:
    reset()
    old_precision = ctx.prec
    print("v1022 -- TEL-B TV/C2b certificates + ALG2 correction; no marker move")
    try:
        ctx.prec = 256
        suite_check(
            "native python-flint version is pinned for reproducibility",
            version("python-flint") == PYTHON_FLINT_VERSION,
        )
        print("python_flint_version", getattr(python_flint, "__version__", "unknown"))
        print("libflint_version", getattr(python_flint, "__FLINT_VERSION__", "unknown"))
        tv_result = tv_certificate()
        c2b_result = c2b_scalar_certificate()
        alg2_countermodel()
        suite_check("TV verdict is proved", bool(tv_result["passed"]))
        print("CLAIM_FENCE: full C2b is not proved in v1022; supplied by v1026")
        print("CLAIM_FENCE: ALG2 remains conditional on FE-GEN/code projection")
        print("VERDICT: TV_FPP_PROVED; C2B_CF_DG_SUPPLIED_BY_V1026; "
              "ALG2_VANDERMONDE_IMPLICATION_REFUTED")
        return summary("v1022 TEL-B round-3 certificates")
    finally:
        ctx.prec = old_precision


if __name__ == "__main__":
    raise SystemExit(run())
