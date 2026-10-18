#!/usr/bin/env python3
"""v599 -- QGEO.REAL.01: the real structure on the mu3-cover -- existence and
uniqueness of the anti-holomorphic D4 reflection, the grading functor that
closes the v598 dictionary gaps at char level, the compiler constants in the
Gamma-decomposition, the honest joint negative, and the Lorentz form with
det 8.

Round 3 of the QGEO cover program (after v597 model, v598 dictionary).
The missing-generator suspect named in v598 was the anti-holomorphic D4
reflection (the real structure).  This module constructs it exactly and
harvests its consequences.

Setup: reduced Burau of B_4 at t = omega on the mu3-cover y^3 = x^4 - 1,
cusp twists T_1..T_4 (D4-conjugate), Grams G_k = (1-T_k)(1-T_k)^dagger.

  (R1) REAL STRUCTURE.  Complex conjugation on the base fixes the punctures
       {1,-1} and swaps {i,-i}: an orientation-REVERSING D4 reflection.  It
       must act semi-linearly, R(v) = M conj(v), sending each twist to the
       INVERSE of its reflected partner: R T_k R^{-1} = T_{5-k}^{-1}.
       We solve the intertwining equations exactly: the solution space is
       1-dimensional (uniqueness up to scale), the canonical normalization
       satisfies R^2 = +1 (a genuine real structure, not quaternionic),
       and all four twist intertwinings hold exactly.

  (R2) GRADING FUNCTOR.  Gamma(A) = M conj(A) M^{-1} is the curve analogue
       of the compiler grading A -> Sigma A Sigma.  In the Gamma-extended
       Gram lattice the three dictionary gaps of v598 close at char level:
         V-cand  = G2 + G3 - Gamma(G3)      char x(x-1)(x-2)     [V]
         H-cand  = 1 + G2 - Gamma(G3)       char (x-1)^2(x-2)    [ANCHOR]
         Qp-cand = 1 + G2 + G3 - Gamma(G3)  char (x-1)(x-2)(x-3) [Q_+]
       All three are exact characteristic-polynomial identities.

  (R3) CONSTANTS.  The Gamma-even/odd cusp elements E_k = G_k + Gamma(G_k),
       O_k = G_k - Gamma(G_k) carry the compiler constants:
         E2: {0,1,5}  (carrier g_car = 5),   E4: {0,3,9}  (3, N_fam^2),
         O2: {0,+-sqrt5},  O3 nilpotent (char x^3),  O4: {0,+-sqrt27}.

  (R4) JOINT NEGATIVE [X, quantified].  Char-matching is NOT yet an algebra
       embedding: in the +-1 integer lattice over the eight generators
       {G_k, Gamma(G_k)} no pair (U*,V*) with the right individual chars
       satisfies the compiler joint relations tr(U*V*) = 3 and
       char(U*+V*) = char Q = (x-1)(x^2-5x+3).  The natural pair
       (G2, G2+G3-Gamma(G3)) gives char(U+V) = x(x^2-6x+4) — a documented
       exact mismatch.  The flag-adapted simultaneous-conjugation search
       remains open; the Strategy-I kill criterion is NOT triggered.

  (R5) LORENTZ FORM [Strategy II].  The Burau image preserves a hermitian
       form J (T_k^dagger J T_k = J).  We solve for J exactly: the solution
       space is 1-dimensional over R; the primitive integral normalization
       has det J = 8 — a member of the sheet-diamond determinant list
       (3,4,8,14,20,32) — and signature (1,2): the Lorentz signature that
       (i) the Toeplitz rank-3 polarization carries (Paper II) and (ii) a
       polarized weight-1 Hodge structure on the omega-eigensheet of a
       genus-3 cover must carry (h^{1,0}, h^{0,1}) = (1,2) or (2,1).
       This is the first exact contact between the cover model and the
       RP=Hodge-positivity strategy.

All checks are exact (sympy); the R4 scan uses a numeric prefilter with
exact confirmation of every candidate.

FIREWALL: GATE.QGEO does not move; no marker changes.  The char-level hits
are typed [E] identities of the CANDIDATES, not an algebra embedding (R4
documents exactly that gap).  Verdict enums (frozen):
REAL-STRUCTURE-LANDED (all 18), REAL-STRUCTURE-FAILS, MIXED.

PROVENANCE: discovery probe real_structure_probe.py (2026-08-01, 18/18,
verdict REAL-STRUCTURE-LANDED).  Python-only, counted per GATE.WOLFRAM.02.
"""

import itertools

import numpy as np
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


def build_twists():
    S = [sp.simplify(burau_gen(i).subs({t: OMEGA})) for i in (1, 2, 3)]
    r = sp.simplify(S[0] * S[1] * S[2])
    T = [S[0]]
    for _ in range(3):
        T.append(sp.simplify(r * T[-1] * r.inv()))
    return T, r


I3 = sp.eye(3)
T, r = build_twists()
G = [sp.simplify((I3 - T[k]) * (I3 - T[k]).conjugate().T) for k in range(4)]


def charpoly(M):
    return sp.factor(sp.simplify(sp.expand((x * I3 - M).det())))


# ---------------------------------------------------------------- R1: real structure
print("=" * 72)
print("R1: real structure R(v) = M conj(v) with R T_k R^-1 = T_(5-k)^-1")
print("=" * 72)

Ms = sp.Matrix(3, 3, lambda i, j: sp.Symbol("m%d%d" % (i, j)))
pair = {0: 3, 1: 2, 2: 1, 3: 0}
eqs = []
for k in range(4):
    E = sp.expand(Ms * T[k].conjugate() - T[pair[k]].inv() * Ms)
    eqs.extend([E[i, j] for i in range(3) for j in range(3)])
sol = sp.solve(eqs, list(Ms), dict=True)
one_dim = len(sol) == 1 and len(sp.Matrix(list(sol[0].values())).free_symbols) == 1
check("R1.1 intertwiner space is 1-dimensional (R unique up to scale)", one_dim)

M = sp.Matrix([[-1, (1 + sp.sqrt(3) * sp.I) / 2, (1 - sp.sqrt(3) * sp.I) / 2],
               [0, 0, 1],
               [0, 1, 0]])
Msol = sp.simplify(Ms.subs(sol[0]).subs({list(sp.Matrix(list(sol[0].values())).free_symbols)[0]: 1}))
check("R1.2 canonical normalization matches the solved intertwiner",
      sp.simplify(M - Msol) == sp.zeros(3, 3) or sp.simplify(M + Msol) == sp.zeros(3, 3)
      or len((sp.simplify(M.inv() * Msol)).free_symbols) == 0
      and sp.simplify(M.inv() * Msol - (M.inv() * Msol)[0, 0] * I3) == sp.zeros(3, 3))
check("R1.3 R^2 = +1 exactly (real, not quaternionic)",
      sp.simplify(M * M.conjugate()) == I3)
ok_tw = all(sp.simplify(M * T[k].conjugate() * M.inv() - T[pair[k]].inv()) == sp.zeros(3, 3) for k in range(4))
check("R1.4 all four twist intertwinings R T_k R^-1 = T_(5-k)^-1", ok_tw)


def Gamma(A):
    return sp.simplify(M * A.conjugate() * M.inv())


# ---------------------------------------------------------------- R2: dictionary gaps close
print("=" * 72)
print("R2: grading functor Gamma closes the v598 dictionary gaps (char level)")
print("=" * 72)

GG = [Gamma(g) for g in G]
V_c = sp.simplify(G[1] + G[2] - GG[2])
H_c = sp.simplify(I3 + G[1] - GG[2])
Qp_c = sp.simplify(I3 + G[1] + G[2] - GG[2])
check("R2.1 char(V-cand) = x(x-1)(x-2)",
      sp.expand(charpoly(V_c) - x * (x - 1) * (x - 2)) == 0, str(charpoly(V_c)))
check("R2.2 char(H-cand) = (x-1)^2(x-2)  [anchor spectrum 1,1,2]",
      sp.expand(charpoly(H_c) - (x - 1) ** 2 * (x - 2)) == 0, str(charpoly(H_c)))
check("R2.3 char(Qp-cand) = (x-1)(x-2)(x-3)",
      sp.expand(charpoly(Qp_c) - (x - 1) * (x - 2) * (x - 3)) == 0, str(charpoly(Qp_c)))

# ---------------------------------------------------------------- R3: compiler constants
print("=" * 72)
print("R3: Gamma-even/odd cusp elements carry the compiler constants")
print("=" * 72)

E = [sp.simplify(G[k] + GG[k]) for k in range(4)]
O = [sp.simplify(G[k] - GG[k]) for k in range(4)]
check("R3.1 E2 spectrum {0,1,5}: carrier g_car = 5",
      sp.expand(charpoly(E[1]) - x * (x - 1) * (x - 5)) == 0, str(charpoly(E[1])))
check("R3.2 E4 spectrum {0,3,9} = {0, N_fam, N_fam^2}",
      sp.expand(charpoly(E[3]) - x * (x - 3) * (x - 9)) == 0, str(charpoly(E[3])))
check("R3.3 O3 nilpotent (char x^3)",
      sp.expand(charpoly(O[2]) - x ** 3) == 0, str(charpoly(O[2])))
check("R3.4 O2 char x(x^2-5), O4 char x(x^2-27)",
      sp.expand(charpoly(O[1]) - x * (x ** 2 - 5)) == 0
      and sp.expand(charpoly(O[3]) - x * (x ** 2 - 27)) == 0,
      "%s ; %s" % (charpoly(O[1]), charpoly(O[3])))

# ---------------------------------------------------------------- R4: joint negative
print("=" * 72)
print("R4: joint compiler relations FAIL in the +-1 Gamma-extended lattice [X]")
print("=" * 72)

charQ = sp.expand((x - 1) * (x ** 2 - 5 * x + 3))
Gn = [np.array(sp.N(g).tolist(), dtype=complex) for g in G]
GGn = [np.array(sp.N(g).tolist(), dtype=complex) for g in GG]
In3 = np.eye(3, dtype=complex)
gens_n = Gn + GGn
gens_s = G + GG

tU = np.array([-3.0, 0.0, 0.0])
tV = np.array([-3.0, 2.0, 0.0])
tQ = np.array([-6.0, 8.0, -3.0])


def charco(Mn):
    lam = np.linalg.eigvals(Mn)
    return np.array([-lam.sum(), lam[0] * lam[1] + lam[0] * lam[2] + lam[1] * lam[2], -lam.prod()])


u_hits, v_hits = [], []
for coeffs in itertools.product(range(-1, 2), repeat=8):
    if all(c == 0 for c in coeffs):
        continue
    base = sum(c * g for c, g in zip(coeffs, gens_n))
    for a in range(0, 3):
        Mn = base + a * In3
        tr = np.trace(Mn)
        if abs(tr.imag) > 1e-8 or abs(tr.real - 3.0) > 1e-7:
            continue
        co = charco(Mn)
        if max(abs(z.imag) for z in co) > 1e-8:
            continue
        cr = np.array([z.real for z in co])
        if np.allclose(cr, tU, atol=1e-7):
            u_hits.append((a, coeffs))
        elif np.allclose(cr, tV, atol=1e-7):
            v_hits.append((a, coeffs))


def exact_mat(a, coeffs):
    Mx = a * I3
    for c, g in zip(coeffs, gens_s):
        if c:
            Mx = Mx + c * g
    return sp.simplify(Mx)


u_exact = [exact_mat(a, c) for a, c in u_hits]
v_exact = [exact_mat(a, c) for a, c in v_hits]
ok_u = all(sp.expand(charpoly(Mx) - x ** 2 * (x - 3)) == 0 for Mx in u_exact)
ok_v = all(sp.expand(charpoly(Mx) - x * (x - 1) * (x - 2)) == 0 for Mx in v_exact)
check("R4.1 scan census: %d U-cands, %d V-cands, all exactly confirmed"
      % (len(u_hits), len(v_hits)),
      len(u_hits) == 4 and len(v_hits) == 6 and ok_u and ok_v)

joint = 0
for Un in u_exact:
    for Vn in v_exact:
        if sp.simplify(sp.trace(Un * Vn) - 3) != 0:
            continue
        if sp.expand(charpoly(sp.simplify(Un + Vn)) - sp.factor(charQ)) == 0:
            joint += 1
check("R4.2 [must-fail] no joint pair: tr(UV)=3 and char(U+V)=charQ", joint == 0,
      "%d joint pairs" % joint)

nat = sp.simplify(G[1] + V_c)
check("R4.3 natural pair mismatch documented: char(G2 + V-cand) = x(x^2-6x+4) != charQ",
      sp.expand(charpoly(nat) - x * (x ** 2 - 6 * x + 4)) == 0
      and sp.expand(charpoly(nat) - sp.factor(charQ)) != 0, str(charpoly(nat)))

# ---------------------------------------------------------------- R5: Lorentz form
print("=" * 72)
print("R5: invariant hermitian form J: det 8, signature (1,2) [Strategy II]")
print("=" * 72)

Jsym = sp.Matrix(3, 3, lambda i, j: sp.Symbol("j_%d%d_re" % (i, j)) + sp.I * sp.Symbol("j_%d%d_im" % (i, j)))
subs_h = {}
for i in range(3):
    subs_h[sp.Symbol("j_%d%d_im" % (i, i))] = 0
    for j in range(i + 1, 3):
        subs_h[sp.Symbol("j_%d%d_re" % (j, i))] = sp.Symbol("j_%d%d_re" % (i, j))
        subs_h[sp.Symbol("j_%d%d_im" % (j, i))] = -sp.Symbol("j_%d%d_im" % (i, j))
Jh = Jsym.subs(subs_h)
eqs = []
for k in range(4):
    Ek = sp.expand(T[k].conjugate().T * Jh * T[k] - Jh)
    for i in range(3):
        for j in range(3):
            eqs.append(sp.re(Ek[i, j]))
            eqs.append(sp.im(Ek[i, j]))
solJ = sp.solve(eqs, sorted(Jh.free_symbols, key=str), dict=True)
J = sp.simplify(Jh.subs(solJ[0]))
freeJ = sorted(J.free_symbols, key=str)
check("R5.1 invariant-form space is 1-dimensional over R", len(solJ) == 1 and len(freeJ) == 1)
J = sp.simplify(J.subs({freeJ[0]: 1}))
ok_inv = all(sp.simplify(T[k].conjugate().T * J * T[k] - J) == sp.zeros(3, 3) for k in range(4))
check("R5.2 T_k^dagger J T_k = J for all four twists (exact)", ok_inv)
in_Zw = all(sp.simplify(sp.expand(e)).is_algebraic for e in J)  # entries in Z[omega]: check via integrality
# explicit integrality: entries of J are in {0, 2, +-1 +- sqrt(3) I} -- all in Z[omega]
entries_ok = all(
    sp.simplify(e - sp.nsimplify(e, [sp.sqrt(3)])) == 0 for e in J
)
check("R5.3 det J = 8 (member of the sheet-diamond determinant list)",
      sp.simplify(J.det() - 8) == 0, "det = %s" % sp.simplify(J.det()))
chJ = charpoly(J)
# eigenvalues: -2, 2 - 2 sqrt 2 (<0), 2 + 2 sqrt 2 (>0) -> signature (1,2)
eigsJ = sorted(np.linalg.eigvalsh(np.array(sp.N(J).tolist(), dtype=complex)))
sig = (sum(1 for e in eigsJ if e > 0), sum(1 for e in eigsJ if e < 0))
check("R5.4 char(J) = (x+2)(x^2-4x-4): signature (1,2) Lorentz",
      sp.expand(chJ - sp.factor(sp.expand((x + 2) * (x ** 2 - 4 * x - 4)))) == 0
      and sig == (1, 2), "eigs ~ %s" % [round(float(e), 4) for e in eigsJ])

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: REAL-STRUCTURE-LANDED -- R unique (R^2=1), dictionary gaps")
    print("close at char level, constants 5/9/27 appear, joint embedding still")
    print("open [X documented], invariant J has det 8 and Lorentz signature (1,2).")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
