"""DIAMOND.BIT.RPFORM -- the RP-form probe of the reconstruction bit: the
corpus reflection form is SPECTRALLY blind to the 81-twins but INTEGRALLY
anchor-visible -- the bit shows only through anchor-coupled states.

THE QUESTION (the RP-slot follow-up of v568): v534 showed reflection
positivity dynamically selects the alignment bit at toy level; the
reconstruction bit (q32 = 2 vs 0, the 81-twins) sits in the SAME structural
slot.  Does an RP-style positivity built from corpus data distinguish the
twins?

THE DESIGN (declared before the run, all prior structure): reflection
theta(X) = Sigma X^T Sigma (the v10 sheet involution as the corpus adjoint);
states omega in {trace, anchor a = (1,1,2), ladder v = (1,2,4), unit 1}
(each load-bearing elsewhere: v23, v568, v183); RP kernel K(x, y) =
omega(theta(x) y) on the Hermite basis of each twin's integral order O_c.
Verdict enums (frozen): RP-SELECTS (a positivity distinction), RP-BLIND
(no distinction anywhere), ANCHOR-VISIBLE (spectrally blind but integrally
separated through declared states).

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import time

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, \
    smith_normal_form

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
A = sp.Matrix([1, 1, 2])
LAD = sp.Matrix([1, 2, 4])
ONE = sp.Matrix([1, 1, 1])


def Qc(c):
    return sp.Matrix([[3, 1, 0], [3, 2, 0], [3, c, 1]])


def hermite_basis(Q):
    U, V = Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)
    ws = [I3]
    fr = [I3]
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


STATES = {
    "trace": lambda Mx: sp.trace(Mx),
    "anchor": lambda Mx: (A.T * Mx * A)[0],
    "ladder": lambda Mx: (LAD.T * Mx * LAD)[0],
    "unit": lambda Mx: (ONE.T * Mx * ONE)[0],
}


def gram(mats, omega):
    K = sp.Matrix(len(mats), len(mats),
                  lambda i, j: omega(theta(mats[i]) * mats[j]))
    return (K + K.T) / 2


def inertia(K):
    ev = np.linalg.eigvalsh(np.array(K.tolist(), float))
    return (int((ev > 1e-9).sum()), int((abs(ev) <= 1e-9).sum()),
            int((ev < -1e-9).sum()))


def snf_divs(K):
    K2 = (2 * K).applyfunc(sp.Integer)      # integral (half-int entries)
    s_ = smith_normal_form(K2)
    return [abs(s_[i, i]) for i in range(min(s_.shape))]


print("=" * 78)
print("DIAMOND.BIT.RPFORM -- the RP form on the 81-twins")
print("=" * 78)

basis = {c: hermite_basis(Qc(c)) for c in (2, 0)}
res = {}
for c in (2, 0):
    res[c] = {}
    for nm, om in STATES.items():
        K = gram(basis[c], om)
        res[c][nm] = (inertia(K), snf_divs(K), sp.nsimplify(K.det()))

# --- R1: spectral blindness -------------------------------------------------
same_inertia = all(res[2][nm][0] == res[0][nm][0] for nm in STATES)
check("R1.1 [E, honest negative -- SPECTRALLY BLIND] the RP kernel "
      "K(x,y) = omega(theta(x) y) has IDENTICAL inertia on both twins "
      "for every declared state (trace (4,0,3); anchor/ladder/unit "
      "(3,1,3) with a one-dimensional kernel): no positivity or "
      "signature distinction exists -- consistent with v567 (every "
      "classical certificate coincides on the pair) and with v534's "
      "lesson that RP selection is nonperturbative",
      same_inertia
      and res[2]["trace"][0] == (4, 0, 3)
      and res[2]["anchor"][0] == (3, 1, 3))
check("R1.2 [E] neither twin's kernel is PSD for any declared state "
      "(3 negative directions everywhere): the kinematic form CANNOT "
      "run a v534-style positivity selection at all -- the RP-slot "
      "question stays with the interacting/dynamical level",
      all(res[c][nm][0][2] == 3 for c in (2, 0) for nm in STATES))

# --- R2: the integral level SEES the bit -----------------------------------
an2, an0 = res[2]["anchor"][1], res[0]["anchor"][1]
ld2, ld0 = res[2]["ladder"][1], res[0]["ladder"][1]
check("R2.1 [E, the central positive result -- ANCHOR-VISIBLE] the "
      "INTEGRAL Smith towers of the anchor-state Gram SEPARATE the "
      "twins: q32 = 2 gives %s, q32 = 0 gives %s -- they differ in "
      "exactly one slot (18 vs 2, a factor 9 = N_fam^2): the compiler "
      "twin carries an EXTRA 3^2 of divisibility in its anchor Gram"
      % (an2, an0),
      an2 != an0 and an2 == [2, 2, 18, 18, 18, 18, 0]
      and an0 == [2, 2, 2, 18, 18, 18, 0])
check("R2.2 [E] the ladder state (1,2,4) separates the same way "
      "(q32 = 2: %s vs q32 = 0: %s), while the ANONYMOUS states are "
      "blind -- trace and unit give identical towers on both twins: "
      "the bit is visible to the RP form ONLY through anchor-coupled "
      "states" % (ld2, ld0),
      ld2 != ld0
      and res[2]["trace"][1] == res[0]["trace"][1]
      and res[2]["unit"][1] == res[0]["unit"][1])
check("R2.3 [E, consistency] the trace-state Gram determinant is "
      "-6561 = -81^2 = -(saturation index)^2 on BOTH twins (the index-"
      "square appears as the RP discriminant; forced by [P_Z : O] = 81 "
      "and the pattern form of signature (4,3))",
      res[2]["trace"][2] == -6561 and res[0]["trace"][2] == -6561)

# --- R2b: the blindness is robust under the compiler's own flow -------------
flow_blind = True
for c in (2, 0):
    pass
V2 = Qc(2) * sp.diag(0, 1, 1)
V0 = Qc(0) * sp.diag(0, 1, 1)
for n_ in (1, 2, 3):
    for nm, om in STATES.items():
        Ka = gram_flow = sp.Matrix(
            7, 7, lambda i, j: om(theta(basis[2][i]) * V2**n_
                                  * basis[2][j]))
        Kb = sp.Matrix(
            7, 7, lambda i, j: om(theta(basis[0][i]) * V0**n_
                                  * basis[0][j]))
        ia = inertia((Ka + Ka.T) / 2)
        ib = inertia((Kb + Kb.T) / 2)
        if ia != ib:
            flow_blind = False
check("R2.4 [E, honest negative extended] the spectral blindness is "
      "ROBUST under the compiler's own flow: the V-semigroup-deformed "
      "kernels K_n(x,y) = omega(theta(x) V^n y), n = 1..3, have "
      "IDENTICAL inertia on both twins for every declared state (the "
      "deformation shifts the inertia -- vector states move (3,1,3) -> "
      "(2,3,2) at n >= 1 -- but never differentially): a dynamical "
      "selection, if any, needs genuine interaction, not a semigroup "
      "weighting", flow_blind)

# --- R2c: the Gibbs pencil of the anchor Hamiltonian -- DYNAMICAL separation
s_ = sp.symbols("s")
pencil = {}
for c in (2, 0):
    Vc = Qc(c) * sp.diag(0, 1, 1)
    evs = sorted(Vc.eigenvals().keys(), key=lambda e: abs(e))
    domc = evs[-1]
    Pi = sp.eye(3)
    for e in evs[:-1]:
        Pi = Pi * (Vc - e * sp.eye(3)) / (domc - e)
    K0 = sp.Matrix(7, 7, lambda i, j: sp.trace(theta(basis[c][i])
                                               * basis[c][j]))
    K1 = sp.Matrix(7, 7, lambda i, j: sp.trace(Pi * theta(basis[c][i])
                                               * basis[c][j]))
    K0 = (K0 + K0.T) / 2
    K1 = (K1 + K1.T) / 2
    detp = sp.factor(sp.expand((K0 + s_ * K1).det()))
    pencil[c] = (K1.rank(), detp)
shared = (s_**2 + 16 * s_ + 16)
extra = (15 * s_**2 - 16 * s_ - 16)
ok2 = sp.simplify(pencil[2][1]
                  - sp.Rational(6561, 4096) * shared**2 * extra) == 0
ok0 = sp.simplify(pencil[0][1]
                  + sp.Rational(6561, 4096) * shared**3) == 0
check("R2.5 [E, THE DYNAMICAL SEPARATION -- the Gibbs pencil] along the "
      "anchor-Hamiltonian Gibbs family omega_g ~ tr(e^{-gH} .), H = I + "
      "Pi_dom (v566), the pencil determinant det(K_0 + s K_Pi) "
      "(s = e^{-g} - 1) FACTORS DIFFERENTLY on the twins: compiler "
      "(6561/4096)(s^2+16s+16)^2 (15s^2-16s-16) vs alt "
      "-(6561/4096)(s^2+16s+16)^3 -- the compiler carries an EXTRA "
      "quadratic factor; the constant is 6561 = 81^2, the saturation "
      "index squared; both K_Pi have rank 6", ok2 and ok0
      and pencil[2][0] == 6 and pencil[0][0] == 6)
r_crit = sp.Rational(8, 15) - 4 * sp.sqrt(19) / 15
in_range = (-1 < float(r_crit) <= 0)
shared_roots_out = all(not (-1 < float(rr) <= 0)
                       for rr in (-8 - 4 * sp.sqrt(3),
                                  -8 + 4 * sp.sqrt(3)))
check("R2.6 [E, THE CRITICAL TEMPERATURE] the compiler twin's extra "
      "factor has the root s* = (8 - 4 sqrt(19))/15 = %.4f INSIDE the "
      "physical Gibbs range s in (-1, 0] (a finite critical temperature "
      "g* = -log(1 + s*)), while the shared roots -8 +- 4 sqrt(3) lie "
      "OUTSIDE it: the COMPILER twin is the one whose RP kernel "
      "degenerates along the Gibbs flow, the alt twin never does -- "
      "the first ONE-PARAMETER-DYNAMICAL distinction of the bit "
      "(honest: a rank-drop marker, not a positivity selection)"
      % float(r_crit),
      in_range and shared_roots_out)

# --- R2d: the critical mode identified ---------------------------------------
Vc2 = Qc(2) * sp.diag(0, 1, 1)
evs2 = sorted(Vc2.eigenvals().keys(), key=lambda e: abs(e))
Pi2 = sp.eye(3)
for e in evs2[:-1]:
    Pi2 = Pi2 * (Vc2 - e * sp.eye(3)) / (evs2[-1] - e)
K0c = sp.Matrix(7, 7, lambda i, j: sp.trace(theta(basis[2][i])
                                            * basis[2][j]))
K1c = sp.Matrix(7, 7, lambda i, j: sp.trace(Pi2 * theta(basis[2][i])
                                            * basis[2][j]))
K0c = (K0c + K0c.T) / 2
K1c = (K1c + K1c.T) / 2
s_star = sp.Rational(8, 15) - 4 * sp.sqrt(19) / 15
null = sp.simplify(K0c + s_star * K1c).nullspace()
Xc = sp.zeros(3, 3)
for k in range(7):
    Xc += null[0][k] * basis[2][k]
Xc = sp.simplify(Xc)
e3 = sp.Matrix([0, 0, 1])
top_rows_zero = all(sp.simplify(Xc[i, j]) == 0 for i in (0, 1)
                    for j in range(3))
check("R2.7 [E, THE CRITICAL MODE IDENTIFIED] the compiler twin's "
      "kernel at the critical temperature is ONE-dimensional and "
      "structurally canonical: the null matrix X is rank 1, supported "
      "ENTIRELY on the seam row (the radical / A2-Ext-carrier row of "
      "v566 S5), fixes the seam line (X e3 = e3), is a FIXED POINT of "
      "the sheet flow (V X = X, left eigenvalue 1) and is annihilated "
      "by the dominant projector (Pi X = 0): the Gibbs criticality "
      "lives exactly in the Ext-carrier slot -- the typed resonance "
      "with the alignment bit deepens to a shared carrier",
      len(null) == 1 and Xc.rank() == 1 and top_rows_zero
      and sp.simplify(Xc * e3 - e3) == sp.zeros(3, 1)
      and sp.simplify(Vc2 * Xc - Xc) == sp.zeros(3, 3)
      and sp.simplify(Pi2 * Xc) == sp.zeros(3, 3))

# --- R2e: the half-sided restrictions stay blind ------------------------------
LEVI = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 2))
RAD = ((2, 0), (2, 1))


def sublattice(mats, pattern):
    out_idx = [k for k, (i, j) in enumerate(IDX7) if (i, j) not in pattern]
    Mcoef = sp.Matrix([[m[IDX7[r][0], IDX7[r][1]] for m in mats]
                       for r in out_idx])
    base = []
    for vv in Mcoef.nullspace():
        d = sp.lcm([sp.denom(x) for x in vv])
        vv = sp.expand(vv * d)
        g = sp.gcd(list(vv))
        vv = sp.Matrix([sp.cancel(x / g) for x in vv])
        X = sp.zeros(3, 3)
        for k in range(7):
            X += vv[k] * mats[k]
        base.append(X)
    return base


half_blind = True
for c in (2, 0):
    Vc_ = Qc(c) * sp.diag(0, 1, 1)
    evs_ = sorted(Vc_.eigenvals().keys(), key=lambda e: abs(e))
    Pi_ = sp.eye(3)
    for e in evs_[:-1]:
        Pi_ = Pi_ * (Vc_ - e * sp.eye(3)) / (evs_[-1] - e)
    res = {}
    for name, pattern in (("levi", LEVI), ("rad", RAD)):
        base = sublattice(basis[c], pattern)
        for sv in (sp.Rational(0), sp.Rational(-1, 2),
                   sp.Rational(-63, 100), sp.Rational(-99, 100)):
            K = sp.Matrix(len(base), len(base),
                          lambda i, j: sp.trace((sp.eye(3) + sv * Pi_)
                                                * theta(base[i])
                                                * base[j]))
            evn = np.linalg.eigvalsh(np.array(sp.N((K + K.T) / 2).tolist(),
                                              float))
            res[(name, sv)] = (int((evn > 1e-9).sum()),
                               int((evn < -1e-9).sum()))
    if c == 2:
        ref = res
    else:
        if res != ref:
            half_blind = False
expect = all(ref[("levi", sv)] == (3, 2) and ref[("rad", sv)] == (1, 1)
             for sv in (sp.Rational(0), sp.Rational(-1, 2),
                        sp.Rational(-63, 100), sp.Rational(-99, 100)))
check("R2.8 [E, honest negative -- the half-sided restrictions stay "
      "blind] restricting the Gibbs kernels to the LEVI sublattice "
      "(dim 5, inertia (3,2)) and to the RADICAL sublattice (dim 2, "
      "inertia (1,1)) gives IDENTICAL inertia on both twins across the "
      "whole sampled Gibbs range -- no positivity anywhere and no "
      "differential change: the RP-positivity selection resists every "
      "kinematic and half-sided design tried (full kernel, V-flow, "
      "Gibbs family, Levi/radical restriction); what remains is the "
      "genuinely INTERACTING construction (the v534 FK-quartet "
      "analogue), typed open", half_blind and expect)

# --- R3: the excluded member ------------------------------------------------
mats1 = hermite_basis(Qc(1))
check("R3.1 [E, control] the excluded member q32 = 1 (the split point) "
      "has a %d-dimensional order (< 7): the v568 collapse reproduces "
      "in this construction -- the RP-form question does not even pose "
      "on the split geometry" % len(mats1), len(mats1) == 5)

VERDICT = ("ANCHOR-VISIBLE" if not FAILS else "MIXED")
print("\nVERDICT: %s -- spectrally blind (same inertia everywhere), "
      "integrally separated exactly through the anchor/ladder states "
      "(Smith slot 18 vs 2, factor 9 = N_fam^2); trace discriminant "
      "-81^2 on both" % VERDICT)
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
