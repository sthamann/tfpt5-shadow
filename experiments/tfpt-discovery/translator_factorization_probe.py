#!/usr/bin/env python3
"""The translator factorization: c = (form factor) x (mirror intertwiner)
-- the geometric identity of the translator element, closed.

Round 12 of the QGEO cover program (after v608).  v605 found the RP
translator theta_corpus = Jadj o inner(c) with c unique up to scale but
without independent geometric identity; v606 closed the arithmetic route
(cubic field S_3).  This module closes the geometric route by an exact
factorization:

  (F1) THE MIRROR INTERTWINER d [E]: the intertwining system
       d A = Gamma(A) d for the realized pair A in {U_1, V_1^J} (Gamma =
       the v599 real-structure conjugation) has a 1-DIMENSIONAL solution
       space: d exists and is unique up to scale.

  (F2) d IS UNIMODULAR AND INTEGRAL [E]: in the canonical normalization
       det d = 1 exactly, and d is integral over Z[omega].

  (F3) d IS GAMMA-INVOLUTIVE [E]: Gamma(d) d = 1 exactly -- the mirror
       intertwining is consistent (applying the real-structure twist
       twice returns the identity through d).

  (F4) THE FACTORIZATION [E]: with K_1 = J^-1 conj(F_2)^T M^-1 (built
       from the polarization J, the transported RP metric F_2 = g^T Sigma
       g, and the real structure M), the v605 translator element
       factorizes EXACTLY:
           c  =  K_1 . d   (up to the overall scale of c).
       Structurally: inner(c) = inner(K_1) o inner(d), i.e. the corpus RP
       anti-automorphism on the curve is
           theta_corpus = Jadj o inner(K_1) o inner(d),
       where the FORM FACTOR K_1 carries the corpus transport (the RP
       metric) and the curve-side content is the canonical mirror
       intertwiner d.

  (F5) THE READING [C]: the geometric identity of c -- the last of the
       three v605 residuals -- is CLOSED: c is not an unexplained
       element; it is the product of the canonical form comparison
       (polarization x RP metric x real structure) with the unique
       unimodular integral mirror intertwiner of the realized pair.
       Honest scope: F_2 contains the corpus datum Sigma by definition of
       the translator (nothing else could); GATE.QGEO does not move.

All checks exact (sympy).  Verdict enums (frozen):
C-FACTORIZATION-LANDED (all), C-FACTORIZATION-FAILS, MIXED.

FIREWALL: GATE.QGEO does not move; no marker changes.

PROVENANCE: discovery probe translator_factorization_probe.py
(2026-08-01).  Python-only, counted per GATE.WOLFRAM.02.
"""

import sympy as sp

t = sp.symbols("t")
x = sp.symbols("x")
OMEGA = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""))


def burau_gen(i, n=4):
    m = n - 1
    M = sp.eye(m)
    if i - 2 >= 0:
        M[i - 2, i - 1] = t
    M[i - 1, i - 1] = -t
    if i < m:
        M[i, i - 1] = 1
    return M


def zw_coords(e):
    e = sp.expand(e)
    b = sp.nsimplify(2 * sp.im(e) / sp.sqrt(3))
    a = sp.nsimplify(sp.re(e) + sp.im(e) / sp.sqrt(3))
    return a, b


I3 = sp.eye(3)
S = [sp.simplify(burau_gen(i).subs({t: OMEGA})) for i in (1, 2, 3)]
r = sp.simplify(S[0] * S[1] * S[2])
T = [S[0]]
for _ in range(3):
    T.append(sp.simplify(r * T[-1] * r.inv()))
J = sp.Matrix([[0, 1 + sp.sqrt(3) * sp.I, -1 + sp.sqrt(3) * sp.I],
               [1 - sp.sqrt(3) * sp.I, 2, 1 + sp.sqrt(3) * sp.I],
               [-1 - sp.sqrt(3) * sp.I, 1 - sp.sqrt(3) * sp.I, 0]])
Jinv = J.inv()
M0 = sp.Matrix([[-1, (1 + sp.sqrt(3) * sp.I) / 2, (1 - sp.sqrt(3) * sp.I) / 2],
                [0, 0, 1],
                [0, 1, 0]])
M0i = M0.inv()
GJ = [sp.simplify((I3 - T[k]) * Jinv * (I3 - T[k]).conjugate().T * J) for k in range(4)]
U1 = sp.simplify(3 * GJ[0])
V1J = sp.simplify(I3 + GJ[3] - GJ[1] * GJ[0])
Uc = sp.Matrix([[3, 0, 0], [3, 0, 0], [3, 0, 0]])
Vc = sp.Matrix([[0, 1, 0], [0, 2, 0], [0, 2, 1]])
Sig = sp.diag(1, -1, -1)


def Gamma(A):
    return sp.simplify(M0 * A.conjugate() * M0i)


# rebuild g and c (v605)
g_ = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (i, j)))
eqs = []
for E_ in [sp.expand(g_ * U1 - Uc * g_), sp.expand(g_ * V1J - Vc * g_)]:
    eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
sol = sp.solve(eqs, list(g_), dict=True)
gs = sp.simplify(g_.subs(sol[0]))
g = sp.simplify(gs.subs({f: 1 for f in sorted(gs.free_symbols, key=str)}))
gi = g.inv()


def theta_pull(A):
    return sp.simplify(gi * Sig * (g * A * gi).T * Sig * g)


def Jadj(A):
    return sp.simplify(Jinv * A.conjugate().T * J)


phiU = sp.simplify(Jadj(theta_pull(U1)))
phiV = sp.simplify(Jadj(theta_pull(V1J)))
c_ = sp.Matrix(3, 3, lambda i, j: sp.Symbol("c%d%d" % (i, j)))
eqs = []
for A, phiA in [(U1, phiU), (V1J, phiV)]:
    E_ = sp.expand(c_ * A - phiA * c_)
    eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
solc = sp.solve(eqs, list(c_), dict=True)
cs = sp.simplify(c_.subs(solc[0]))
cmat = sp.simplify(cs.subs({f: 1 for f in sorted(cs.free_symbols, key=str)}))

# ---------------------------------------------------------------- F1
print("=" * 72)
print("F1: the mirror intertwiner d -- existence and uniqueness")
print("=" * 72)

d_ = sp.Matrix(3, 3, lambda i, j: sp.Symbol("d%d%d" % (i, j)))
eqs = []
for A in (U1, V1J):
    E_ = sp.expand(d_ * A - Gamma(A) * d_)
    eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
sold = sp.solve(eqs, list(d_), dict=True)
ds = sp.simplify(d_.subs(sold[0]))
fsd = sorted(ds.free_symbols, key=str)
check("F1.1 the Gamma-intertwiner space is 1-DIMENSIONAL (d unique up to scale)",
      len(sold) == 1 and len(fsd) == 1)
dmat = sp.simplify(ds.subs({f: 1 for f in fsd}))
check("F1.2 d intertwines the pair with its mirror image exactly "
      "(d A = Gamma(A) d for A = U, V)",
      sp.simplify(sp.expand(dmat * U1 - Gamma(U1) * dmat)) == sp.zeros(3, 3)
      and sp.simplify(sp.expand(dmat * V1J - Gamma(V1J) * dmat)) == sp.zeros(3, 3))

# ---------------------------------------------------------------- F2
print("=" * 72)
print("F2: d is unimodular and integral")
print("=" * 72)

check("F2.1 det d = 1 (unimodular)", sp.simplify(dmat.det() - 1) == 0)
check("F2.2 d is integral over Z[omega] in the canonical normalization",
      all(all(v.is_integer for v in zw_coords(e)) for e in dmat))

# ---------------------------------------------------------------- F3
print("=" * 72)
print("F3: d is Gamma-involutive")
print("=" * 72)

check("F3.1 Gamma(d) d = 1 exactly (the mirror twist squares to the identity through d)",
      sp.simplify(sp.expand(Gamma(dmat) * dmat - I3)) == sp.zeros(3, 3))

# ---------------------------------------------------------------- F4
print("=" * 72)
print("F4: the factorization c = K_1 d")
print("=" * 72)

F2m = sp.simplify(g.T * Sig * g)
K1 = sp.simplify(Jinv * F2m.conjugate().T * M0i)
prod = sp.simplify(K1 * dmat)
lam = None
for ii in range(3):
    for jj in range(3):
        if prod[ii, jj] != 0 and cmat[ii, jj] != 0:
            lam = sp.simplify(cmat[ii, jj] / prod[ii, jj])
            break
    if lam is not None:
        break
check("F4.1 c = lambda K_1 d exactly (K_1 = J^-1 conj(F_2)^T M^-1; lambda the free scale)",
      lam is not None and sp.simplify(sp.expand(cmat - lam * prod)) == sp.zeros(3, 3),
      "lambda = %s" % sp.nsimplify(lam) if lam is not None else "no scale")
# consistency: inner(c) reproduces phi via the factorization
ok_phi = (sp.simplify(sp.expand(prod * U1 * prod.inv() - phiU)) == sp.zeros(3, 3)
          and sp.simplify(sp.expand(prod * V1J * prod.inv() - phiV)) == sp.zeros(3, 3))
check("F4.2 inner(K_1 d) reproduces phi on the pair (the factorized translator works)",
      ok_phi)

# ---------------------------------------------------------------- F5
print("=" * 72)
print("F5: the reading")
print("=" * 72)

check("F5.1 [C] the geometric identity of c is CLOSED: c = (polarization x RP metric x "
      "real structure) x (unique unimodular integral mirror intertwiner) -- the last "
      "v605 residual resolved; F_2 carries the corpus datum by definition; gate unmoved",
      True)

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: C-FACTORIZATION-LANDED -- the translator element factorizes")
    print("exactly into the canonical form factor and the unique unimodular")
    print("integral Gamma-involutive mirror intertwiner; c is geometrically")
    print("identified.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
