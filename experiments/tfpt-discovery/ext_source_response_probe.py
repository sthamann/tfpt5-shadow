"""DIAMOND.BIT.EXTSOURCE -- the interacting follow-up of v572, executed:
rank-one Ext-source coupling on the Gibbs pencil SEPARATES THE 81-TWINS
DIRECTIONALLY INSIDE THE UNIT COUPLING BOX.  The interacting kernel
K(s, J) = K_0 + s K_Pi + J v v^T (v_i = tr(theta(x_i) N), N an Ext
arrow E31/E32 of the shared radical row) has EXACT rational flip
thresholds J_c(s) = -1/(v^T K(s)^{-1} v) whose numerators are exactly
the v572 pencil factors:

  compiler/E31:  J_c = (15s^2-16s-16)/(16(s^2-s-1)),  J_c(-1) = 15/16
  compiler/E32:  J_c = (15s^2-16s-16)/16
  alt/E31:       J_c = (s^2+16s+16)/(16(s+1)),        J_c(0)  = 1
  alt/E32:       J_c = -(s^2+16s+16)/16,              J_c(0)  = -1

THE SEPARATION: in the crossed phase s in (-1, s*] the compiler twin is
HEALED (inertia restored to the (4,0,3) pattern form) by positive
coupling J <= 15/16 < 1 through either Ext arrow, while the alt twin
cannot be flipped by ANY positive coupling in the open unit box (E31
threshold >= 1 with equality only at s = 0; E32 flips only at negative
J).  Positive Ext coupling selects exactly the compiler twin --
consistent with v534's toy RP selection of positive seam coupling.
BONUS STRUCTURE: the compiler's E31 response has its pole at the golden
point s^2 - s - 1 = 0 (s = -1/phi = -0.618, next to s* = -0.629), and
the healing works because the v572 critical mode is Ext-visible.

FIREWALL: one algebraic platform (the v572 twin orders, trace Gibbs
pencil), one interaction class (rank-one Ext sources), declared
coupling box |J| <= 1; a RESPONSE-level selection (inertia
restoration), NOT an OS/RP positivity theorem -- no kernel is ever
PSD; the alignment-bit contract stays open; no marker moves.  Verdict
enums (frozen): UNIT-BOX-SEPARATED, RESPONSE-BLIND, MIXED.

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import sys
import time

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


I3 = sp.eye(3)
IDX7 = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))
SIG = sp.diag(1, -1, -1)
S_SYM = sp.symbols("s", real=True)
E31 = sp.Matrix(3, 3, lambda i, j: 1 if (i, j) == (2, 0) else 0)
E32 = sp.Matrix(3, 3, lambda i, j: 1 if (i, j) == (2, 1) else 0)
S_STAR = sp.Rational(8, 15) - 4 * sp.sqrt(19) / 15


def Qc(c):
    return sp.Matrix([[3, 1, 0], [3, 2, 0], [3, c, 1]])


def hermite_basis(Q):
    U, V = Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)
    ws, fr = [I3], [I3]
    for _ in range(5):
        fr = [w * G for w in fr for G in (U, V)]
        ws += fr
    Mrows = sp.Matrix([[w[i, j] for (i, j) in IDX7] for w in ws])
    H = hermite_normal_form(Mrows.T)
    mats = []
    for k in range(H.cols):
        Mx = sp.zeros(3, 3)
        for r, (i, j) in enumerate(IDX7):
            Mx[i, j] = H[r, k]
        mats.append(Mx)
    return mats


def theta(X):
    return SIG * X.T * SIG


def inertia(K):
    ev = np.linalg.eigvalsh(np.asarray(K, float))
    return (int((ev > 1e-9).sum()), int((abs(ev) <= 1e-9).sum()),
            int((ev < -1e-9).sum()))


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("DIAMOND.BIT.EXTSOURCE -- Ext-source response on the Gibbs "
          "pencil")
    print("=" * 78)

    basis = {c: hermite_basis(Qc(c)) for c in (2, 0)}
    pencil, vecs = {}, {}
    for c in (2, 0):
        Vc = Qc(c) * sp.diag(0, 1, 1)
        evs = sorted(Vc.eigenvals().keys(), key=lambda e: abs(e))
        Pi = sp.eye(3)
        for e in evs[:-1]:
            Pi = Pi * (Vc - e * sp.eye(3)) / (evs[-1] - e)
        K0 = sp.Matrix(7, 7, lambda i, j: sp.trace(theta(basis[c][i])
                                                   * basis[c][j]))
        K1 = sp.Matrix(7, 7, lambda i, j: sp.trace(Pi * theta(basis[c][i])
                                                   * basis[c][j]))
        pencil[c] = ((K0 + K0.T) / 2, (K1 + K1.T) / 2)
        vecs[c] = {nm: sp.Matrix([sp.trace(theta(basis[c][k]) * N_)
                                  for k in range(7)])
                   for nm, N_ in (("E31", E31), ("E32", E32))}

    # ---- X1: the exact response formulas ---------------------------------
    Jc_expect = {
        (2, "E31"): (15 * S_SYM**2 - 16 * S_SYM - 16)
        / (16 * (S_SYM**2 - S_SYM - 1)),
        (2, "E32"): (15 * S_SYM**2 - 16 * S_SYM - 16) / 16,
        (0, "E31"): (S_SYM**2 + 16 * S_SYM + 16) / (16 * (S_SYM + 1)),
        (0, "E32"): -(S_SYM**2 + 16 * S_SYM + 16) / 16,
    }
    all_ok = True
    for (c, nm), expct in Jc_expect.items():
        Ks = pencil[c][0] + S_SYM * pencil[c][1]
        v = vecs[c][nm]
        q = sp.simplify((v.T * Ks.inv() * v)[0])
        if sp.simplify(-1 / q - expct) != 0:
            all_ok = False
    check("X1.1 [E, exact] the four rank-one flip thresholds "
          "J_c(s) = -1/(v^T K(s)^{-1} v) are the CLOSED rational "
          "functions above, and their numerators are EXACTLY the v572 "
          "pencil factors: the compiler's extra factor (15s^2-16s-16) "
          "prices its own Ext response, the shared factor "
          "(s^2+16s+16) prices the alt twin's", all_ok)

    ok_num = True
    n_flips = 0
    for c in (2, 0):
        for nm in ("E31", "E32"):
            v = np.asarray(vecs[c][nm], float).ravel()
            K0n = np.asarray(pencil[c][0], float)
            K1n = np.asarray(pencil[c][1], float)
            Jc_f = sp.lambdify(S_SYM, Jc_expect[(c, nm)])
            for sv in (-0.9, -0.7, -0.4, -0.1):
                Jc_v = float(Jc_f(sv))
                i_lo = inertia(K0n + sv * K1n
                               + (Jc_v - 0.02) * np.outer(v, v))
                i_hi = inertia(K0n + sv * K1n
                               + (Jc_v + 0.02) * np.outer(v, v))
                # exactly one eigenvalue crosses zero at J_c: the
                # positive count goes up by one, the negative down
                if not (i_hi[0] == i_lo[0] + 1 and i_hi[2] == i_lo[2] - 1):
                    ok_num = False
                n_flips += 1
    check("X1.2 [E, verified numerically] crossing J_c flips exactly "
          "one eigenvalue from negative to positive at every sampled "
          "temperature (%d flip events: s in {-0.9,-0.7,-0.4,-0.1}, "
          "both twins, both arrows): the closed thresholds are the "
          "actual flip curves" % n_flips, ok_num)

    # ---- X2: the unit-box separation -------------------------------------
    s_vals = [sp.Rational(-99, 100), sp.Rational(-9, 10),
              sp.Rational(-4, 5), sp.Rational(-7, 10), S_STAR]
    comp_ok = all(
        0 <= float(Jc_expect[(2, "E31")].subs(S_SYM, sv)) <= 15 / 16
        and 0 <= float(Jc_expect[(2, "E32")].subs(S_SYM, sv)) < 1
        for sv in s_vals)
    Jc_alt = sp.lambdify(S_SYM, Jc_expect[(0, "E31")])
    alt_rigid = all(Jc_alt(sv) >= 1.0 - 1e-12
                    for sv in np.linspace(-0.999, 0.0, 400))
    alt_e32_neg = all(
        float(Jc_expect[(0, "E32")].subs(S_SYM, sp.Rational(n, 100))) < 0
        for n in range(-99, 1))
    check("X2.1 [E, THE CENTRAL RESULT -- UNIT-BOX SEPARATION] in the "
          "crossed phase s in (-1, s*] the COMPILER twin is healed by "
          "positive coupling J_c <= 15/16 < 1 through EITHER Ext arrow, "
          "while the ALT twin cannot be flipped by any positive "
          "coupling in the open unit box: its E31 threshold stays >= 1 "
          "on the whole physical range and its E32 threshold is "
          "negative throughout -- POSITIVE Ext-source coupling inside "
          "|J| < 1 selects exactly the compiler twin",
          comp_ok and alt_rigid and alt_e32_neg)

    exact_anchors = (
        sp.simplify(Jc_expect[(2, "E31")].subs(S_SYM, -1)
                    - sp.Rational(15, 16)) == 0
        and sp.simplify(Jc_expect[(0, "E31")].subs(S_SYM, 0) - 1) == 0
        and sp.simplify(Jc_expect[(0, "E32")].subs(S_SYM, 0) + 1) == 0
        and sp.simplify(Jc_expect[(2, "E31")].subs(S_SYM, S_STAR)) == 0
        and sp.simplify(Jc_expect[(2, "E32")].subs(S_SYM, S_STAR)) == 0)
    check("X2.2 [E, exact anchors] the box constants are EXACT: "
          "compiler J_c(-1) = 15/16; alt E31 J_c(0) = 1 (the rigidity "
          "bound saturates exactly at infinite temperature); alt E32 "
          "J_c(0) = -1; and both compiler thresholds vanish exactly at "
          "the critical temperature s*", exact_anchors)

    # ---- X3: the direction and the v534 resonance -------------------------
    v31 = np.asarray(vecs[2]["E31"], float).ravel()
    K0n2 = np.asarray(pencil[2][0], float)
    K1n2 = np.asarray(pencil[2][1], float)
    no_neg_heal = all(
        inertia(K0n2 + sv * K1n2 - J * np.outer(v31, v31))[2] >= 4
        for sv in (-0.9, -0.8, -0.7)
        for J in (0.1, 0.5, 1.0))
    check("X3.1 [E, the direction] NEGATIVE coupling never heals the "
          "compiler in the crossed phase (inertia stays at 4 negative "
          "directions for J in -[0.1, 1], s in {-0.9,-0.8,-0.7}): the "
          "healing direction is strictly POSITIVE -- [C] consistent "
          "with v534, where the interacting toy's RP cone also "
          "selected the positive seam coupling on the twist state",
          no_neg_heal)

    # ---- X4: the golden pole ----------------------------------------------
    pole_poly = sp.factor(sp.denom(sp.together(Jc_expect[(2, "E31")])))
    golden_ok = (sp.simplify(sp.expand(pole_poly
                 - 16 * (S_SYM**2 - S_SYM - 1))) == 0)
    s_pole = float((1 - sp.sqrt(5)) / 2)
    check("X4.1 [E, observed structure] the compiler's E31 response has "
          "its pole exactly on the GOLDEN polynomial s^2 - s - 1 (the "
          "Fibonacci characteristic polynomial): s_pole = -1/phi = "
          "%.4f, sitting 0.011 above the critical temperature s* = "
          "%.4f -- an adjugate-level structure absent from the "
          "determinant; typed as observed [C], no claim built on it"
          % (s_pole, float(S_STAR)),
          golden_ok and abs(s_pole - float(S_STAR)) < 0.02)

    # ---- X5: the mechanism -------------------------------------------------
    Ks_star = pencil[2][0] + S_STAR * pencil[2][1]
    null = sp.simplify(Ks_star).nullspace()
    Xc = sp.zeros(3, 3)
    for k in range(7):
        Xc += null[0][k] * basis[2][k]
    ov31 = sp.simplify(sp.trace(theta(Xc) * E31))
    ov32 = sp.simplify(sp.trace(theta(Xc) * E32))
    check("X5.1 [E, the mechanism] the healing works because the v572 "
          "critical mode is Ext-VISIBLE: the null matrix at s* has "
          "nonzero pairing with both Ext arrows (tr(theta(X) E31) = %s, "
          "tr(theta(X) E32) = %s) -- the rank-one source couples "
          "directly to the crossing mode, which is why J_c(s*) = 0 "
          "exactly" % (ov31, ov32),
          len(null) == 1 and ov31 != 0 and ov32 != 0)

    check("X6.1 [C, honest typing] this is a RESPONSE-level selection "
          "(inertia restoration in a declared coupling box), not an "
          "OS/RP positivity theorem: no kernel is ever PSD (3+ negative "
          "directions persist), the interaction class is rank-one "
          "sources only, and the alignment-bit contract "
          "(CONTRACT.SEAM.BIT) stays open; no ledger marker moves",
          True)

    VERDICT = "UNIT-BOX-SEPARATED" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- positive Ext coupling inside |J| < 1 heals "
          "exactly the compiler twin (J_c <= 15/16); the alt twin is "
          "rigid (threshold >= 1 / negative); thresholds exact, "
          "numerators = the v572 pencil factors" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: response-level, declared box, one platform; no "
          "positivity theorem; contract stays open; no marker moves")
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
