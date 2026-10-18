#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_bfk_conical_det_probe -- ALPHA.QUILLEN.BFK_CONICAL.01 (strategy S7):
the Burghelea-Friedlander-Kappeler gluing formula (BFK, "Mayer-Vietoris type
formula for determinants of elliptic differential operators", J. Funct. Anal.
107 (1992) 34) made EXECUTABLE on the KMS seam circle with the four mu4
marks, and priced EXACTLY against the v484/v485 closed forms of the merged
ALPHA.QUILLEN.EXACT.01 + HYP.PHI0.PUNCTURE.01 analytic target.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO ledger
row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  v484 derived the finite CYCLE sector of the merged
target on the seam circle (mark-Green matrix G_marks = -4 c3 ln2 x
circ(0,1,2,1), spec {4,-2,0,-2}, Tr C^k = 4^k + 2(-2)^k); v485 settled the
DIAGONAL channel (G_reg(0; l) = (1/pi) ln(l/2pi), zero exactly at the KMS
circumference l = 2 pi = 1/(4 c3)) and resummed the mark determinant closed-
form (det(I - uC) = (1-4u)(1+2u)^2), naming the BFK/gluing route (v151
class) without EXECUTING it.  What was never done: cut the seam circle at
the four mu4 marks {0, pi/2, pi, 3pi/2}, write the ACTUAL BFK identity
det_zeta = C_glue x prod_j det_zeta(Dirichlet interval_j) x det(R) with the
Neumann-jump (Dirichlet-to-Neumann) matrix R at the marks, derive the 1D
gluing constant C_glue in closed form, and confront R with the v484 mark
circulant and the v485 scale channel.  This probe does exactly that, for
the LOCAL second-order operator Delta = -d^2/dx^2 = |D|^2 on the seam
circle (BFK applies to differential operators; the nonlocal |D| itself
enters only through its mark Green matrix and the scale dictionary --
typed honestly in P8/G19).

THE SETUP.  Circle S^1_l of circumference l, marks p_1..p_N cutting it into
intervals of lengths a_1..a_N (sum = l).  Conventions VERIFIED in-probe and
stated: zeta-determinants with the zero mode REMOVED are primed, det'; the
same zero-mode-removed convention is used by v484 (Green function of |D|
with n = 0 dropped) and v485 (G_reg zero mode removed).  Anchors:
det'_zeta(Delta on S^1_l) = l^2, det'_zeta(|D| on S^1_l) = l,
det_zeta(Dirichlet Delta on [0,a]) = 2a (no zero mode, unprimed).  Massive
regulator for the BFK step (Delta + m^2 is invertible, plain BFK applies):
det_zeta(Delta + m^2 on S^1_l) = 4 sinh^2(ml/2),
det_zeta(Dirichlet on [0,a] + m^2) = 2 sinh(ma)/m, interval DtN
Lambda_a(m) = (m/sinh ma) [[cosh ma, -1], [-1, cosh ma]], assembled jump
matrix R(m) = sum of interval DtN blocks (weighted-cycle structure), and
the m -> 0 limit performed with the exact zero-mode bookkeeping
(lambda_0(m) = m^2 l/N + O(m^4), Gram ratio l/N = ||1||^2_{L^2(S^1_l)} /
||1||^2_{C^N}).  All identities symbolic (sympy, exact q = e^{m a_j / 2}
Laurent-polynomial form) wherever feasible, mpmath 40-60 digits elsewhere;
deterministic fixed rational parameters, no randomness.

PRE-REGISTERED ADJUDICATION (frozen before the record runs):
  P1 CONVENTIONS/ANCHORS: det'_zeta(Delta_S1) = l^2, det'_zeta(|D|) = l
     (and (det'|D|)^2 = det' Delta), det_zeta(Dirichlet [0,a]) = 2a --
     symbolic via zeta_Delta(s) = 2 (l/2pi)^{2s} zeta_R(2s) etc. with
     zeta_R(0) = -1/2, zeta_R'(0) = -(1/2) ln 2pi, plus 30-digit numeric
     zeta'(0) cross-checks; massive closed forms recovered through the
     relative-Fredholm product prod_{n>=1}(1 + x^2/n^2) = sinh(pi x)/(pi x).
  P2 BFK IDENTITY + GLUING CONSTANT: for N = 4 with GENERAL symbolic
     lengths, det_zeta(Delta + m^2 on S^1) = 2^{-4} prod_j det_zeta(D_j +
     m^2) x det R(m) EXACTLY (Laurent-polynomial identity in q_j); the 1D
     gluing constant is derived, C_glue = 2^{-N} (one factor 1/2 per cut
     point), verified symbolically for N = 1, 2, 3, 4 and to 40 digits
     numerically.
  P3 ZERO-MODE (MASSLESS) BFK: det'_zeta(Delta_S1) = 2^{-N} prod_j (2 a_j)
     x (l/N) x det'(R_0) with R_0 the weighted cycle Laplacian
     (R_0 = graph Laplacian, weights 1/a_j), det'(R_0) = N l / prod a_j
     (charpoly + matrix-tree cross-check), and the l/N factor typed as the
     zero-mode Gram ratio.
  P4 DtN-GREEN DUALITY: R(m) = (G_m|_marks)^{-1} exactly (the jump matrix
     is the inverse of the mark-restricted Green matrix), and massless
     R_0 x G_Delta|_marks = I - J/4 (identity off the zero mode) with
     G_Delta(d) = d^2/2l - d/2 + l/12 verified as the zero-mode-removed
     Green function.
  P5 KMS c3-GRADING vs v484: at l = 2 pi = 1/(4 c3), a = pi/2 = 1/(16 c3):
     R_0 = 16 c3 x circ(2,-1,0,-1) =: 16 c3 B -- integer circulant times a
     pure c3 unit (16 c3 = |mu4| x 4 c3 = |mu4| x bare 1/(2pi)); v484's
     G_marks = -4 c3 ln2 x circ(0,1,2,1) =: -4 c3 ln2 C re-derived in-probe;
     GLOBAL matrix proportionality B ~ C is expected to FAIL (kernel
     channels swapped: B kills the mu4-trivial k=0 channel, C kills the
     mu4-sign k=2 channel), while the correspondence holds EXACTLY channel-
     wise: same mu4 Fourier eigenbasis, |spec B| = |spec C| = {0,2,2,4} as
     multisets, doublet channel (k = 1,3) R_0|_d = (4/ln2) G_marks|_d (c3
     CANCELS -- both matrices carry the same c3 grading), B + C = 2(I + S);
     cycle combinatorics Tr B^k = 4^k + 2(+2)^k vs v484's Tr C^k =
     4^k + 2(-2)^k (same {4, 2-doublet} magnitude law, sign flip = the
     kernel-channel swap); Tr B = 8 <> 0 vs Tr C = 0 typed via v485
     (C's diagonal renormalises to zero at KMS, B's diagonal is the
     Dirichlet jump -- nonzero by construction).
  P6 SCALE CHANNEL vs v485: d/dl log det'_zeta(Delta) = 2/l with the BFK
     factor decomposition 4/l - 3/l + 1/l (intervals - jump matrix + zero
     mode); the v485 diagonal is reproduced EXACTLY through the dictionary
     log det'Delta(l) - log det'Delta(1/(4c3)) = (1/(4 c3)) G_reg(0; l)
     and G_reg(0; l) = (1/pi)(log det'|D|(l) - log det'|D|(2pi)), i.e. the
     KMS unit 2 pi = 1/(4 c3) converts the glued log-det scale channel
     into the v485 closed form; derivative ratio exactly 2 pi.
  P7 MUTANTS CAUGHT: (A) moving one mark off mu4 (pi/2 -> 7pi/12) breaks
     the circulant property, the {0,2,4,2}/a spectrum and the Tr law
     (CAUGHT) while the BFK identity itself STILL holds (control: the
     identity is mark-position independent, the correspondence is mu4-
     specific); (B) a wrong gluing constant 2^{-3} breaks the anchor
     identity by an exact factor 2 (CAUGHT).
  P8 HONEST TYPING: this probe covers the U(1)-scalar SECOND-ORDER
     determinant face (Delta = |D|^2 on the seam circle with the four
     marks, BFK-glued); it does NOT cover the full pillowcase moduli
     variation, the 8 b1 / 41 = 10 b1 index-coefficient budget, or a BFK
     gluing of the nonlocal |D| itself.
EXPECTED VERDICT (pre-registered): MATCH_MODULO_LOCAL_FACTOR -- the gluing
identity is exact and the v485 scale channel is reproduced exactly, but the
mark-matrix correspondence to v484 is channel-graded (doublet factor 4/ln2,
kernel channels swapped by the operator order |D| vs |D|^2), NOT a global
matrix proportionality, so BFK_MATCH_EXACT is not available.

VERDICT ENUM: BFK_MATCH_EXACT (gluing identity verified + mark-matrix
correspondence exact with printed constant + scale channel reproduced) /
MATCH_MODULO_LOCAL_FACTOR (identity holds, correspondence holds up to a
mark-local/channel factor, quantified) / MISMATCH.

RECORD: two identical runs (seam_bfk_conical_det_probe.run1.log /
.run2.log, diff modulo the wall-clock line), runtime bar 180 s,
deterministic (fixed rational parameters, no RNG).
"""

import hashlib
import sys
import time

import mpmath as mp
import sympy as sp

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
RUNTIME_BAR = 180.0

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ---------------------------------------------------------------- constants
C3S = 1 / (8 * sp.pi)                       # c3 = 1/(8 pi), P1 axiom
ZP0 = -sp.log(2 * sp.pi) / 2                # zeta_R'(0) = -(1/2) ln 2pi
N_MARKS = 4                                 # |mu4|
LENS_GEN = [sp.Rational(7, 10), sp.Rational(13, 10),
            sp.Rational(11, 10), sp.Rational(9, 10)]   # generic lengths, l=4
M_VALUES = [sp.Rational(1, 3), sp.Integer(1), sp.Rational(7, 2)]


def circ(row):
    """4x4 (or NxN) circulant with given first row."""
    n = len(row)
    return sp.Matrix(n, n, lambda i, j: row[(j - i) % n])


def assemble_R_sym(qs):
    """Jump matrix R(m)/m from interval half-exponentials q_j = e^{m a_j/2}.

    Interval j joins marks j and j+1 (mod N); its DtN block is
    (1/s_j) [[c_j, -1], [-1, c_j]] with s_j = sinh(m a_j), c_j = cosh(m a_j).
    """
    n = len(qs)
    R = sp.zeros(n, n)
    for j, q in enumerate(qs):
        s = (q ** 2 - q ** -2) / 2
        c = (q ** 2 + q ** -2) / 2
        k = (j + 1) % n
        R[j, j] += c / s
        R[k, k] += c / s
        R[j, k] += -1 / s
        R[k, j] += -1 / s
    return R


def assemble_R0_sym(lens):
    """Massless jump matrix: weighted cycle Laplacian, weights 1/a_j."""
    n = len(lens)
    R = sp.zeros(n, n)
    for j, a in enumerate(lens):
        k = (j + 1) % n
        R[j, j] += 1 / a
        R[k, k] += 1 / a
        R[j, k] += -1 / a
        R[k, j] += -1 / a
    return R


def assemble_R_num(lens, m):
    """Numeric massive jump matrix (mpmath)."""
    n = len(lens)
    R = mp.zeros(n, n)
    for j, a in enumerate(lens):
        a = mp.mpf(a)
        s, c = mp.sinh(m * a), mp.cosh(m * a)
        k = (j + 1) % n
        R[j, j] += m * c / s
        R[k, k] += m * c / s
        R[j, k] += -m / s
        R[k, j] += -m / s
    return R


def bfk_poly_check(qs):
    """Massive BFK identity as an exact Laurent-polynomial identity.

    LHS = 4 sinh^2(ml/2) = (Q - 1/Q)^2, Q = prod q_j;
    RHS = 2^{-N} prod_j (2 s_j / m) x det R(m) = prod_j s_j x det(R/m)
    (the m^N factors cancel exactly).  Clearing denominators: multiplying
    row j of R/m by s_{j-1} s_j turns it polynomial and multiplies the
    determinant by prod s_j^2, so the identity is equivalent to
    D := det(cleared matrix) == (Q - 1/Q)^2 x prod s_j, checked by expand.
    """
    n = len(qs)
    svals = [(q ** 2 - q ** -2) / 2 for q in qs]
    R = assemble_R_sym(qs)
    M = sp.zeros(n, n)
    for j in range(n):
        f = svals[(j - 1) % n] * svals[j]
        for k in range(n):
            M[j, k] = sp.expand(sp.cancel(sp.together(R[j, k] * f)))
    D = M.det(method='berkowitz')
    Q = sp.prod(qs)
    return sp.expand(D - (Q - 1 / Q) ** 2 * sp.prod(svals)) == 0


def main() -> int:
    print("=" * 78)
    print("seam_bfk_conical_det_probe  ALPHA.QUILLEN.BFK_CONICAL.01  "
          "(strategy S7)")
    print("EXPLORATION ONLY (2026-08-27). experiments/ level: NO promotion, "
          "NO ledger row,")
    print("NO marker moved, NO gate closed or narrowed.")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    l, a, m, x = sp.symbols('l a m x', positive=True)

    # ================================================================ P1
    section("P1  CONVENTIONS AND ANCHORS (zero mode removed = primed det')")

    # G01 -- circle anchors, symbolic zeta computation
    # zeta_Delta(s) = 2 (l/2pi)^{2s} zeta_R(2s); eigenvalues (2 pi n/l)^2,
    # n <> 0 (zero mode REMOVED -- same convention as v484/v485).
    A = l / (2 * sp.pi)
    dlogdet_D2 = -(4 * sp.log(A) * sp.Rational(-1, 2) + 4 * ZP0)   # -zeta'(0)
    dlogdet_D1 = -(2 * sp.log(A) * sp.Rational(-1, 2) + 2 * ZP0)   # |D| case
    sym_circle = sp.simplify(sp.expand_log(dlogdet_D2 - 2 * sp.log(l),
                                           force=True)) == 0
    sym_absD = sp.simplify(sp.expand_log(dlogdet_D1 - sp.log(l),
                                         force=True)) == 0
    mp.mp.dps = 40
    lnum = mp.mpf(3)
    zder = mp.diff(lambda ss: 2 * (lnum / (2 * mp.pi)) ** (2 * ss)
                   * mp.zeta(2 * ss), mp.mpf(0))
    num_circle = abs(-zder - 2 * mp.log(lnum)) < mp.mpf('1e-25')
    check("G01-anchor-circle", sym_circle and sym_absD and num_circle,
          "det'_zeta(Delta on S^1_l) = l^2 and det'_zeta(|D|) = l "
          "(so (det'|D|)^2 = det'Delta), symbolic via zeta_R(0) = -1/2, "
          "zeta_R'(0) = -(1/2)ln 2pi + numeric -zeta'(0) = 2 ln l at l = 3 "
          "(err %.1e); CONVENTION: zero mode REMOVED (primed det'), the "
          "same zero-mode-removed convention as v484/v485"
          % float(abs(-zder - 2 * mp.log(lnum))))

    # G02 -- interval anchor det_zeta(Dirichlet [0,a]) = 2a
    B_ = a / sp.pi
    dlogdet_int = -(2 * sp.log(B_) * sp.Rational(-1, 2) + 2 * ZP0)
    sym_int = sp.simplify(sp.expand_log(dlogdet_int - sp.log(2 * a),
                                        force=True)) == 0
    anum = mp.mpf(5) / 4
    zder_i = mp.diff(lambda ss: (anum / mp.pi) ** (2 * ss) * mp.zeta(2 * ss),
                     mp.mpf(0))
    num_int = abs(-zder_i - mp.log(2 * anum)) < mp.mpf('1e-25')
    check("G02-anchor-interval", sym_int and num_int,
          "det_zeta(-d^2/dx^2 on [0,a], Dirichlet) = 2a (no zero mode, "
          "unprimed), symbolic + numeric at a = 5/4 (err %.1e)"
          % float(abs(-zder_i - mp.log(2 * anum))))

    # G03 -- massive closed forms via the relative-Fredholm product
    # gamma-reflection route: prod(1+x^2/n^2) = 1/(Gamma(1+ix)Gamma(1-ix))
    # (Weierstrass) and Gamma(1+ix)Gamma(1-ix) = pi x / sinh(pi x) (exact)
    refl_ok = sp.simplify(sp.gamma(1 + sp.I * x) * sp.gamma(1 - sp.I * x)
                          - sp.pi * x / sp.sinh(sp.pi * x)) == 0
    errs_p = []
    for xv in (mp.mpf(1) / 3, mp.mpf(1), mp.mpf(12) / 5):
        lhs_p = mp.nsum(lambda n: mp.log(1 + xv ** 2 / n ** 2), [1, mp.inf])
        errs_p.append(abs(lhs_p - mp.log(mp.sinh(mp.pi * xv)
                                         / (mp.pi * xv))))
    num_prod = max(errs_p) < mp.mpf('1e-25')
    X = m * l / 2
    chain_circ = sp.simplify(l ** 2 * m ** 2 * (sp.sinh(X) / X) ** 2
                             - 4 * sp.sinh(X) ** 2) == 0
    chain_int = sp.simplify(2 * a * (sp.sinh(m * a) / (m * a))
                            - 2 * sp.sinh(m * a) / m) == 0
    lim_circ = sp.limit(4 * sp.sinh(X) ** 2 / m ** 2, m, 0) == l ** 2
    lim_int = sp.limit(2 * sp.sinh(m * a) / m, m, 0) == 2 * a
    check("G03-massive-closed-forms",
          refl_ok and num_prod and chain_circ and chain_int
          and lim_circ and lim_int,
          "det_zeta(Delta+m^2 on S^1_l) = 4 sinh^2(ml/2) = det'Delta x m^2 "
          "x prod(1+ (ml/2 pi n)^2)^2 and det_zeta(D_a+m^2) = 2 sinh(ma)/m; "
          "product identity prod(1+x^2/n^2) = sinh(pi x)/(pi x): gamma-"
          "reflection Gamma(1+ix)Gamma(1-ix) = pi x/sinh(pi x) symbolic + "
          "25+ digit numeric (max err %.1e); m->0 recovers the G01/G02 "
          "anchors (symbolic limits)" % float(max(errs_p)))

    # ================================================================ P2
    section("P2  MASSIVE BFK GLUING (identity + gluing constant, exact)")

    # G04 -- interval DtN block
    f0, fa = sp.symbols('f0 fa')
    usol = (f0 * sp.sinh(m * (a - x)) + fa * sp.sinh(m * x)) / sp.sinh(m * a)
    ode_ok = sp.simplify(-sp.diff(usol, x, 2) + m ** 2 * usol) == 0
    bc_ok = (sp.simplify(usol.subs(x, 0) - f0) == 0
             and sp.simplify(usol.subs(x, a) - fa) == 0)
    n0 = sp.simplify(-sp.diff(usol, x).subs(x, 0)
                     - m * (f0 * sp.cosh(m * a) - fa) / sp.sinh(m * a)) == 0
    na = sp.simplify(sp.diff(usol, x).subs(x, a)
                     - m * (fa * sp.cosh(m * a) - f0) / sp.sinh(m * a)) == 0
    lam00 = sp.limit(m * sp.cosh(m * a) / sp.sinh(m * a), m, 0)
    lam01 = sp.limit(-m / sp.sinh(m * a), m, 0)
    check("G04-interval-DtN", ode_ok and bc_ok and n0 and na
          and lam00 == 1 / a and lam01 == -1 / a,
          "Lambda_a(m) = (m/sinh ma)[[cosh ma, -1],[-1, cosh ma]] derived "
          "from the explicit solution (ODE + boundary values + outward "
          "normal derivatives, symbolic); m->0 limit (1/a)[[1,-1],[-1,1]]")

    # G05 -- the BFK identity, N = 4, GENERAL symbolic lengths
    q1, q2, q3, q4 = sp.symbols('q1 q2 q3 q4', positive=True)
    sym_bfk4 = bfk_poly_check([q1, q2, q3, q4])
    mp.mp.dps = 50
    worst = mp.mpf(0)
    for mv in M_VALUES:
        mv = mp.mpf(sp.Rational(mv))
        lens_n = [mp.mpf(sp.Rational(av)) for av in LENS_GEN]
        ltot = mp.fsum(lens_n)
        lhs_n = 4 * mp.sinh(mv * ltot / 2) ** 2
        rhs_n = mp.mpf(2) ** -4
        for av in lens_n:
            rhs_n *= 2 * mp.sinh(mv * av) / mv
        rhs_n *= mp.det(assemble_R_num(lens_n, mv))
        worst = max(worst, abs(lhs_n / rhs_n - 1))
    check("G05-BFK-identity-N4", sym_bfk4 and worst < mp.mpf('1e-40'),
          "det_zeta(Delta+m^2 on S^1) = 2^{-4} prod_j det_zeta(D_j+m^2) x "
          "det R(m) EXACT for GENERAL lengths a_1..a_4 (Laurent-polynomial "
          "identity in q_j = e^{m a_j/2}, expand == 0) + 50-digit numeric "
          "at a = (7,13,11,9)/10, m in {1/3, 1, 7/2} (worst rel err %.1e)"
          % float(worst))

    # G06 -- the gluing constant, derived: C_glue = 2^{-N}, N = 1, 2, 3
    # bfk_poly_check verifies det_zeta(circle) = 2^{-N} prod det_D x det R
    # as an exact polynomial identity; passing it for each N IS the
    # derivation C_glue = 2^{-N} (any other constant fails, see G18).
    cs = [bfk_poly_check(syms)
          for syms in ([q1], [q1, q2], [q1, q2, q3])]
    check("G06-gluing-constant", all(cs),
          "C_glue DERIVED in closed form: det_zeta(circle) / "
          "[prod det_zeta(Dirichlet) x det R] = 2^{-N} exactly for "
          "N = 1, 2, 3 cut points (general symbolic lengths) -- one local "
          "factor 1/2 per cut point; with G05 this fixes C_glue = 2^{-N} "
          "for the mu4 case N = 4 as well")

    # ================================================================ P3
    section("P3  MASSLESS (ZERO-MODE) BFK -- det' Delta = l^2 reassembled")

    a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4', positive=True)
    lens_s = [a1, a2, a3, a4]
    ltot_s = sum(lens_s)

    # G07 -- det'(R_0) = N l / prod a_j  (weights w_j = 1/a_j, polynomial)
    ws = sp.symbols('w1 w2 w3 w4', positive=True)
    R0w = sp.zeros(4, 4)
    for j in range(4):
        k2 = (j + 1) % 4
        R0w[j, j] += ws[j]
        R0w[k2, k2] += ws[j]
        R0w[j, k2] += -ws[j]
        R0w[k2, j] += -ws[j]
    lam_ = sp.Symbol('lam_')
    coeffs = R0w.charpoly(lam_).all_coeffs()     # [1, c3, c2, c1, c0]
    c0_zero = sp.expand(coeffs[4]) == 0
    detp_w = -coeffs[3]                 # product of nonzero eigenvalues
    mtree_w = sum(sp.prod(ws[i] for i in range(4) if i != j)
                  for j in range(4))
    mtree_ok = sp.expand(detp_w - 4 * mtree_w) == 0
    # under w_j = 1/a_j: 4 sum_j prod_{i<>j} 1/a_i = 4 (sum a_j)/prod a_j
    detp = 4 * ltot_s / (a1 * a2 * a3 * a4)
    detp_ok = sp.simplify(
        detp_w.subs(dict(zip(ws, [1 / aj for aj in lens_s]))) - detp) == 0
    kernel_ok = sp.expand(R0w * sp.ones(4, 1)) == sp.zeros(4, 1)
    check("G07-detprime-R0", c0_zero and detp_ok and mtree_ok and kernel_ok,
          "R_0 = weighted cycle Laplacian (weights 1/a_j), kernel = "
          "constants exactly; det'(R_0) = N l / prod a_j (charpoly "
          "coefficient, general symbolic lengths) = N x weighted spanning-"
          "tree sum (matrix-tree cross-check)")

    # G08 -- zero-mode limit and the assembled massless identity
    rowsum = sum(2 * m * sp.tanh(m * aj / 2) for aj in lens_s)
    ser = sp.series(rowsum, m, 0, 4).removeO()
    ser_ok = sp.simplify(ser - m ** 2 * ltot_s) == 0
    mp.mp.dps = 60
    lens_n = [mp.mpf(sp.Rational(av)) for av in LENS_GEN]
    ltot_n = mp.fsum(lens_n)
    mtiny = mp.mpf('1e-10')
    detRm = mp.det(assemble_R_num(lens_n, mtiny))
    detp_n = mp.mpf(sp.Rational(
        sp.simplify(detp.subs(dict(zip(lens_s, LENS_GEN))))))
    lim_err = abs(detRm / (mtiny ** 2 * (ltot_n / 4) * detp_n) - 1)
    assembled = sp.simplify(
        sp.Rational(1, 16) * sp.prod([2 * aj for aj in lens_s])
        * (ltot_s / 4) * (4 * ltot_s / (a1 * a2 * a3 * a4))
        - ltot_s ** 2) == 0
    check("G08-massless-BFK", ser_ok and lim_err < mp.mpf('1e-15')
          and assembled,
          "<1|R(m)|1> = m^2 l + O(m^4) (symbolic series) => lambda_0(m) = "
          "m^2 l/N + O(m^4); det R(m)/m^2 -> (l/N) det'(R_0) verified to "
          "rel err %.1e at m = 1e-10 (60 dps); ASSEMBLED IDENTITY "
          "det'_zeta(Delta_S1) = 2^{-N} prod(2 a_j) x (l/N) x det'(R_0) = "
          "l^2 EXACT for general lengths; l/N = ||1||^2_{L^2(S^1_l)} / "
          "||1||^2_{C^N} is the zero-mode Gram ratio" % float(lim_err))

    # ================================================================ P4
    section("P4  DtN-GREEN DUALITY (jump matrix = inverse mark Green matrix)")

    # G09 -- massive duality R(m) = (G_m|marks)^{-1}
    t = sp.Symbol('t', positive=True)        # t = m a, equal marks, l = 4a
    Rsym = (1 / sp.sinh(t)) * circ([2 * sp.cosh(t), -1, 0, -1])
    Gsym = (sp.Rational(1, 2) / sp.sinh(2 * t)) * circ(
        [sp.cosh(2 * t), sp.cosh(t), 1, sp.cosh(t)])
    prod_RG = Rsym * Gsym
    sym_dual = all(
        sp.cancel(sp.together(
            (prod_RG[i, j] - (1 if i == j else 0)).rewrite(sp.exp))) == 0
        for i in range(4) for j in range(4))
    mp.mp.dps = 50
    marks_n = [mp.mpf(0), mp.mpf(9) / 10, mp.mpf(5) / 2, mp.mpf(22) / 5]
    ln_ = 2 * mp.pi
    lens_dual = [(marks_n[(j + 1) % 4] - marks_n[j]) % ln_ for j in range(4)]
    worst_d = mp.mpf(0)
    for mv in M_VALUES:
        mv = mp.mpf(sp.Rational(mv))
        Rn = assemble_R_num(lens_dual, mv)
        Gn = mp.zeros(4, 4)
        for i in range(4):
            for j in range(4):
                d = abs(marks_n[i] - marks_n[j])
                Gn[i, j] = mp.cosh(mv * (ln_ / 2 - d)) \
                    / (2 * mv * mp.sinh(mv * ln_ / 2))
        E = Rn * Gn
        for i in range(4):
            for j in range(4):
                worst_d = max(worst_d, abs(E[i, j] - (1 if i == j else 0)))
    check("G09-massive-duality", sym_dual and worst_d < mp.mpf('1e-40'),
          "R(m) x G_m|_marks = I EXACT: symbolic 4x4 at equal marks "
          "(G_m(d) = cosh(m(l/2-d))/(2m sinh(ml/2))) + 50-digit numeric at "
          "GENERAL marks (0, 9/10, 5/2, 22/5) on l = 2pi, m in "
          "{1/3, 1, 7/2} (worst |entry err| %.1e) -- the BFK jump matrix "
          "is the inverse of the mark-restricted Green matrix"
          % float(worst_d))

    # G10 -- massless Green function and R_0 G_Delta = I - J/4
    d_ = sp.Symbol('d_', positive=True)
    GD = d_ ** 2 / (2 * l) - d_ / 2 + l / 12
    ode2 = sp.simplify(-sp.diff(GD, d_, 2) + 1 / l) == 0
    jump = sp.simplify((sp.diff(GD, d_).subs(d_, 0)
                        - sp.diff(GD, d_).subs(d_, l)) + 1) == 0
    mean0 = sp.simplify(sp.integrate(GD, (d_, 0, l))) == 0
    symm = sp.simplify(GD - GD.subs(d_, l - d_)) == 0
    mp.mp.dps = 30
    lf = 2 * mp.pi
    errs_f = []
    for df in (mp.mpf(0), lf / 5, lf / 3, lf / 2):
        four = (lf / (2 * mp.pi ** 2)) * mp.re(
            mp.polylog(2, mp.e ** (1j * 2 * mp.pi * df / lf)))
        errs_f.append(abs(four - (df ** 2 / (2 * lf) - df / 2 + lf / 12)))
    four_ok = max(errs_f) < mp.mpf('1e-25')
    GDm = (l / 96) * circ([8, -1, -4, -1])
    marks_vals = [sp.simplify(GD.subs(d_, dv))
                  for dv in (0, l / 4, l / 2, l / 4)]
    marks_ok = all(sp.simplify(marks_vals[j] - GDm[0, j]) == 0
                   for j in range(4))
    R0eq = sp.Rational(4, 1) / l * circ([2, -1, 0, -1])
    proj = sp.simplify(R0eq * GDm - (sp.eye(4) - sp.ones(4, 4) / 4)) \
        == sp.zeros(4, 4)
    check("G10-massless-duality", ode2 and jump and mean0 and symm
          and four_ok and marks_ok and proj,
          "G_Delta(d) = d^2/2l - d/2 + l/12 is THE zero-mode-removed Green "
          "function (-G'' = delta - 1/l: ODE + unit derivative jump + zero "
          "mean + symmetry, symbolic; Fourier/polylog check to 25+ digits, "
          "max err %.1e); mark matrix (l/96) circ(8,-1,-4,-1); "
          "R_0 x G_Delta|_marks = I - J/4 EXACT (identity off the zero "
          "mode)" % float(max(errs_f)))

    # ================================================================ P5
    section("P5  KMS c3-GRADING AND THE v484 MARK-MATRIX CORRESPONDENCE")

    Bm = circ([2, -1, 0, -1])
    Cm = circ([0, 1, 2, 1])
    Sm = circ([0, 0, 1, 0])
    lkms = 2 * sp.pi                       # = 1/(4 c3), v239 KMS unit
    akms = lkms / 4                        # = pi/2 = 1/(16 c3)

    # G11 -- R_0 at the KMS marks is a pure c3-graded integer circulant
    R0kms = assemble_R0_sym([akms] * 4)
    r0_ok = sp.simplify(R0kms - 16 * C3S * Bm) == sp.zeros(4, 4)
    unit_ok = (sp.simplify(16 * C3S - 4 * (4 * C3S)) == 0
               and sp.simplify(4 * C3S - 1 / (2 * sp.pi)) == 0)
    detp_kms = sp.simplify(4 * lkms / akms ** 4)
    detp_c3 = sp.simplify(detp_kms - 2 ** 16 * C3S ** 3) == 0
    product_c3 = sp.simplify(
        sp.Rational(1, 16) * (2 * akms) ** 4 * (lkms / 4) * detp_kms
        - 1 / (16 * C3S ** 2)) == 0
    anchor_c3 = sp.simplify(lkms ** 2 - 1 / (16 * C3S ** 2)) == 0
    check("G11-KMS-c3-grading", r0_ok and unit_ok and detp_c3
          and product_c3 and anchor_c3,
          "at l = 2pi = 1/(4c3): R_0 = 16 c3 x circ(2,-1,0,-1) EXACT "
          "(proportionality constant 16 c3 = |mu4| x 4 c3 = |mu4| x bare "
          "1/(2pi) -- the v484 unit chain per interval); det'(R_0) = "
          "128/pi^3 = 2^16 c3^3; per-interval det_D = 2a = pi = 1/(8 c3); "
          "zero-mode factor l/N = pi/2 = 1/(16 c3); whole glued product = "
          "2^{-4} c3^{-2} = (2pi)^2 = det'Delta -- every BFK factor is a "
          "pure 2-power times a c3 power (NOTE: C_glue = 2^{-4} = |mu4|^{-2}"
          " holds only because N = |mu4| = 4; C_glue = 2^{-N} generally -- "
          "anti-numerology)")

    # G12 -- v484 mark matrix re-derived in-probe (not imported on trust)
    Gfun = lambda dd: -(1 / sp.pi) * sp.log(2 * sp.sin(dd / 2))
    g_adj = sp.simplify(Gfun(sp.pi / 2) / (C3S * sp.log(2)))
    g_opp = sp.simplify(Gfun(sp.pi) / (C3S * sp.log(2)))
    mp.mp.dps = 30
    errs_li = [abs(mp.re(mp.polylog(1, mp.e ** (1j * v)))
                   + mp.log(2 * mp.sin(v / 2)))
               for v in (mp.pi / 7, mp.pi / 2, mp.pi)]
    spec_C = dict(Cm.eigenvals()) == {4: 1, -2: 2, 0: 1}
    check("G12-v484-rederived", g_adj == -4 and g_opp == -8
          and max(errs_li) < mp.mpf('1e-25') and spec_C,
          "G_|D|(d) = -(1/pi) ln|2 sin(d/2)| (polylog identity to 25+ "
          "digits, max err %.1e); at the mu4 separations G(pi/2) = "
          "-4 c3 ln2, G(pi) = -8 c3 ln2 => G_marks = -4 c3 ln2 x "
          "circ(0,1,2,1) =: -4 c3 ln2 C, spec(C) = {4,-2,0,-2} -- the v484 "
          "mark matrix, re-derived in-probe" % float(max(errs_li)))

    # G13 -- the correspondence: NOT globally proportional; exact channel form
    one = sp.ones(4, 1)
    v2 = sp.Matrix([1, -1, 1, -1])
    ker_swap = (sp.simplify(Bm * one) == sp.zeros(4, 1)
                and sp.simplify(Cm * v2) == sp.zeros(4, 1)
                and sp.simplify(Cm * one - 4 * one) == sp.zeros(4, 1)
                and sp.simplify(Bm * v2 - 4 * v2) == sp.zeros(4, 1))
    # no scalar k gives B = k C: B[0,0] = 2 <> 0 while C[0,0] = 0, and the
    # kernels disagree (any B = k C with k <> 0 forces equal kernels)
    not_prop = (Bm[0, 0] == 2 and Cm[0, 0] == 0)
    I4 = sp.I
    F4 = sp.Matrix(4, 4, lambda i, j: I4 ** (i * j))
    diagB = sp.simplify(F4.inv() * Bm * F4)
    diagC = sp.simplify(F4.inv() * Cm * F4)
    shared_basis = diagB.is_diagonal() and diagC.is_diagonal()
    specB = dict(Bm.eigenvals())
    mults_ok = (sorted(abs(k2) for k2, v_ in specB.items()
                       for _ in range(v_))
                == sorted(abs(k2) for k2, v_ in dict(Cm.eigenvals()).items()
                          for _ in range(v_)) == [0, 2, 2, 4])
    Pd = (sp.eye(4) - Sm) / 2              # projector onto k = 1,3 doublet
    Gmarks = -4 * C3S * sp.log(2) * Cm
    doublet = sp.simplify(16 * C3S * Bm * Pd
                          - (4 / sp.log(2)) * Gmarks * Pd) == sp.zeros(4, 4)
    bc_sum = sp.simplify(Bm + Cm - 2 * (sp.eye(4) + Sm)) == sp.zeros(4, 4)
    check("G13-correspondence", ker_swap and not_prop and shared_basis
          and mults_ok and doublet and bc_sum,
          "GLOBAL proportionality R_0 ~ G_marks FAILS (kernel channels "
          "SWAPPED: B kills the mu4-TRIVIAL k=0 channel [gauge/zero mode], "
          "C kills the mu4-SIGN k=2 channel [ln 2 arithmetic of the square]"
          "); what holds EXACTLY: same mu4 Fourier eigenbasis (both "
          "diagonal in F4), |spec| multisets EQUAL {0,2,2,4}, doublet "
          "channel (k=1,3) R_0|_d = (4/ln2) x G_marks|_d -- the c3 grading "
          "CANCELS in the ratio (16 c3 vs 4 c3 ln2, both c3-graded, "
          "constant 4/ln2 = %.10f...), and B + C = 2(I + S)"
          % float(4 / mp.log(2)))

    # G14 -- cycle combinatorics through the BFK matrix powers
    trB_ok = all(sp.trace(Bm ** k2) == 4 ** k2 + 2 * 2 ** k2
                 for k2 in range(1, 9))
    trC_ok = all(sp.trace(Cm ** k2) == 4 ** k2 + 2 * (-2) ** k2
                 for k2 in range(1, 9))
    check("G14-cycle-combinatorics", trB_ok and trC_ok
          and sp.trace(Cm) == 0 and sp.trace(Bm) == 8,
          "Tr(B^k) = 4^k + 2(+2)^k and Tr(C^k) = 4^k + 2(-2)^k EXACT "
          "(k = 1..8): the BFK jump circulant reproduces the v484 "
          "{4, 2-doublet} magnitude law with the sign channel flipped "
          "(= the kernel swap of G13); Tr C = 0 <=> the v485 diagonal "
          "renormalises to ZERO at the KMS scale, Tr B = 8 <> 0 <=> the "
          "Dirichlet jump diagonal 2/a is nonzero by construction -- the "
          "absent linear term of det(I - uC) = (1-4u)(1+2u)^2 is a |D|-"
          "side statement, not a Delta-side one (typed)")

    # ================================================================ P6
    section("P6  THE SCALE CHANNEL vs v485")

    # G15 -- d/dl log det' through the BFK factors
    t1 = sp.diff(sp.log((l / 2) ** 4), l)          # intervals prod(2 l/4)
    t2 = sp.diff(sp.log(1024 / l ** 3), l)         # det'R_0 = 4l/(l/4)^4
    t3 = sp.diff(sp.log(l / 4), l)                 # zero-mode Gram factor
    dec_ok = (sp.simplify(t1 - 4 / l) == 0 and sp.simplify(t2 + 3 / l) == 0
              and sp.simplify(t3 - 1 / l) == 0
              and sp.simplify(t1 + t2 + t3
                              - sp.diff(sp.log(l ** 2), l)) == 0)
    check("G15-scale-decomposition", dec_ok,
          "d/dl log det'_zeta(Delta) = 2/l decomposes through the glued "
          "product as 4/l (four Dirichlet intervals) - 3/l (jump-matrix "
          "det', rank 3) + 1/l (zero-mode Gram factor l/N): 4 - 3 + 1 = 2 "
          "exactly, factor by factor")

    # G16 -- the v485 dictionary
    Greg = sp.log(l / (2 * sp.pi)) / sp.pi         # v485 closed form
    dict1 = sp.simplify(sp.log(l ** 2) - sp.log((2 * sp.pi) ** 2)
                        - (1 / (4 * C3S)) * Greg) == 0
    dict2 = sp.simplify(sp.log(l) - sp.log(2 * sp.pi)
                        - sp.pi * Greg) == 0
    ratio = sp.simplify(sp.diff(sp.log(l ** 2), l) / sp.diff(Greg, l)
                        - 2 * sp.pi) == 0
    kms_pt = (sp.simplify(Greg.subs(l, 2 * sp.pi)) == 0
              and sp.simplify(1 / (4 * C3S) - 2 * sp.pi) == 0)
    check("G16-v485-scale-channel", dict1 and dict2 and ratio and kms_pt,
          "log det'Delta(l) - log det'Delta(1/(4c3)) = (1/(4 c3)) x "
          "G_reg(0; l) EXACT, and G_reg(0; l) = (1/pi)[log det'|D|(l) - "
          "log det'|D|(2pi)] (v485 closed form (1/pi) ln(l/2pi) reproduced "
          "from the glued determinant); derivative ratio = 2 pi = 1/(4 c3) "
          "= the KMS unit exactly; at the seam point G_reg = 0 while "
          "det'Delta = (2pi)^2 (the log-det is ANCHORED, not zero -- "
          "honest print)")

    # ================================================================ P7
    section("P7  MUTANTS (must be CAUGHT)")

    # G17 -- MUTANT A: one mark moved off mu4: pi/2 -> 7 pi/12
    mp.mp.dps = 50
    lens_mut = [7 * mp.pi / 12, 5 * mp.pi / 12, mp.pi / 2, mp.pi / 2]
    R0mut = mp.zeros(4, 4)
    for j in range(4):
        k2 = (j + 1) % 4
        w = 1 / lens_mut[j]
        R0mut[j, j] += w
        R0mut[k2, k2] += w
        R0mut[j, k2] += -w
        R0mut[k2, j] += -w
    anom = mp.pi / 2
    not_circ = abs(R0mut[0, 1] - R0mut[1, 2]) * anom > mp.mpf('0.1')
    evs = sorted(mp.eigsy(R0mut, eigvals_only=True))
    evs_scaled = [float(anom * e) for e in evs]
    spec_dev = max(abs(anom * e - r) for e, r in zip(evs, [0, 2, 2, 4]))
    spec_broken = spec_dev > mp.mpf('0.01')
    tr2 = mp.fsum((anom * e) ** 2 for e in evs)
    tr_broken = abs(tr2 - 24) > mp.mpf('0.05')
    detp_mut = evs[1] * evs[2] * evs[3]
    ident_mut = mp.mpf(2) ** -4
    for av in lens_mut:
        ident_mut *= 2 * av
    ident_mut *= (2 * mp.pi / 4) * detp_mut
    ident_holds = abs(ident_mut / (2 * mp.pi) ** 2 - 1) < mp.mpf('1e-40')
    check("G17-mutant-off-mark", not_circ and spec_broken and tr_broken
          and ident_holds and abs(evs[0]) < mp.mpf('1e-45'),
          "marks (0, 7pi/12, pi, 3pi/2): R_0 NOT circulant "
          "(|R01-R12| a = %.3f), a x spec = (%.4f, %.4f, %.4f, %.4f) vs "
          "mu4 (0,2,2,4) (max dev %.3f), Tr((aR)^2) = %.4f vs 24 -- "
          "CAUGHT; CONTROL: the massless BFK identity STILL gives "
          "det' = (2pi)^2 (rel err < 1e-40): the identity is mark-"
          "independent, the mu4 correspondence is not"
          % (float(abs(R0mut[0, 1] - R0mut[1, 2]) * anom),
             evs_scaled[0], evs_scaled[1], evs_scaled[2], evs_scaled[3],
             float(spec_dev), float(tr2)))

    # G18 -- MUTANT B: wrong gluing constant 2^{-3}
    rhs_wrong = sp.Rational(1, 8) * sp.prod([2 * aj for aj in lens_s]) \
        * (ltot_s / 4) * (4 * ltot_s / (a1 * a2 * a3 * a4))
    factor2 = sp.simplify(rhs_wrong / ltot_s ** 2 - 2) == 0
    check("G18-mutant-wrong-constant", factor2,
          "replacing C_glue = 2^{-4} by 2^{-3} breaks the anchor identity "
          "by an EXACT factor 2 (symbolic, general lengths): "
          "RHS_wrong / det'Delta = 2 -- CAUGHT")

    # ================================================================ P8
    section("P8  HONEST TYPING + VERDICT")

    covered = (sym_bfk4 and assembled and r0_ok and dict1)
    check("G19-honest-typing", covered,
          "COVERED: the U(1)-scalar SECOND-ORDER determinant face of the "
          "ALPHA.QUILLEN diagonal target -- Delta = |D|^2 on the seam "
          "CIRCLE with the four mu4 marks, BFK-glued, all constants in "
          "closed form. NOT covered (stays with the keystone, v382/v485 "
          "typing): the full pillowcase MODULI variation, the 8 b1 / "
          "41 = 10 b1 index-coefficient budget, and a BFK gluing of the "
          "NONLOCAL |D| itself (|D| is order-1 pseudodifferential; it "
          "enters only via its mark Green matrix, G12, and the scale "
          "dictionary, G16). experiments/ level: nothing promoted")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    verdict_ok = (npass == len(CHECKS))
    check("G20-verdict", verdict_ok,
          "MATCH_MODULO_LOCAL_FACTOR: gluing identity EXACT (C_glue = "
          "2^{-N}, general lengths) + zero-mode BFK reassembles det' = l^2 "
          "+ jump matrix = inverse mark Green matrix + v485 scale channel "
          "reproduced EXACTLY via the KMS unit 2pi = 1/(4c3); the v484 "
          "mark-matrix correspondence is CHANNEL-GRADED, not global: "
          "doublet factor 4/ln2 (c3 cancels -- both matrices c3-graded: "
          "16 c3 vs 4 c3 ln2), kernel channels swapped (mu4-trivial vs "
          "mu4-sign) -- so NOT BFK_MATCH_EXACT, and nothing mismatched")

    return finish()


def finish() -> int:
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    if npass == len(CHECKS):
        print("ALL GATES PASSED %d/%d" % (npass, len(CHECKS)))
    else:
        print("GATES: %d/%d passed -- NOT all green" % (npass, len(CHECKS)))
    print("VERDICT: %s" % ("MATCH_MODULO_LOCAL_FACTOR"
                           if npass == len(CHECKS) else "MISMATCH"))
    print("RESULT: %d/%d gates PASS   SPEC_SHA %s"
          % (npass, len(CHECKS), SPEC_SHA[:16]))
    print("EXPLORATION ONLY: no promotion, no ledger row, no marker moved, "
          "no gate closed or narrowed.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
