#!/usr/bin/env python3
"""v603 -- QGEO.SEAMMARKS.01: the seam-and-marks round -- the seam line is a
REAL line of the cover reversed by S_0 (the v590 demand, geometric), the
infinity cusp separates in the unreduced module, the first per-mark Z/3
witness lands (E_1, order 3), and the corpus-transpose translator negatives
are quantified.

Round 7 of the QGEO cover program (after v602).  Executes the follow-up
slate "form translator / infinity cusp / mark classes / two demands":

  (S1) THE SEAM LINE IS FOUND AND IT IS REAL [E]: the line-stabilizer pair
       (U_1, V_1^J) has a unique common eigenline v with U v = 0 and
       V v = v (the compiler seam, span(e_3), transported); explicitly
       v = (0, (sqrt3 - i)/(sqrt3 + i), 1).  The real structure FIXES this
       line (R v ~ v): THE SEAM IS A REAL LINE OF THE COVER.  The
       two-demand involution S_0 REVERSES it (S_0 v = -v): the v590 seam-
       reversal demand holds geometrically on the curve.  Honest scope:
       S_0 does NOT commute with R (the sheet involution is not
       Gamma-even), and the seam's identification with the infinity cusp
       stays open.

  (S2) THE INFINITY CUSP SEPARATED [E]: the UNREDUCED Burau of B_4 at
       t = omega (braid relations machine-verified) contains the invariant
       column (1,1,1,1) -- the trivial line -- and the full twist r^4 acts
       with eigenvalues {1, omega, omega, omega}: the infinity-cusp
       direction (eigenvalue 1) is canonically separated from the reduced
       omega-sheet (the v597 deck identity r^4 = omega restricted).  The
       invariant row is (1, omega, conj(omega), 1).

  (S3) THE FIRST MARK-LOCAL Z/3 WITNESS [E]: the Gamma-even cusp element
       E_1 = G_1 + Gamma(G_1) restricts to an INTEGER matrix on the
       saturated fixed lattice, lies in the seven-word algebra of
       (C_U, C_V) with coefficient denominators of lcm EXACTLY 3 -- an
       ORDER-THREE CLASS in the cokernel P/O of the word order: the first
       exact witness of the per-mark Z/3 mechanism (v566/v597).  Honest
       structure: E_4's class is trivial (integer coefficients) and
       E_2, E_3 lie OUTSIDE the mark-1-anchored algebra -- the naive
       global map fails; the equivariant per-mark framing (each mark's
       class lives in its own rotated frame) is the typed reading.

  (S4) TRANSLATOR NEGATIVES [X, quantified]: the pullback of the corpus
       RP transpose structure along the compiler conjugation is the
       symmetric bilinear form F_2 = g^T Sigma g; F_2 is NOT proportional
       to any member of the canonical menu (B, B*S_0, B*Klein, B*V-polys,
       B*H, ...), and neither B^-1 F_2 nor F_2 B^-1 lies in the word
       algebra -- the corpus-transpose translator genuinely needs a new
       canonical object, named open.

All checks exact (sympy).  Verdict enums (frozen): SEAM-REAL-LANDED
(all), SEAM-REAL-FAILS, MIXED.

FIREWALL: GATE.QGEO does not move; no marker changes.  The seam-infinity
identification, the equivariant completion of the mark map and the
transpose translator stay typed open.

PROVENANCE: discovery probe seam_marks_probe.py (2026-08-01, 15/15,
verdict SEAM-REAL-LANDED).  Python-only, counted per GATE.WOLFRAM.02.
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


def burau_unred(i, n=4):
    M = sp.eye(n)
    M[i - 1, i - 1] = 1 - t
    M[i - 1, i] = t
    M[i, i - 1] = 1
    M[i, i] = 0
    return M


I3 = sp.eye(3)
I4 = sp.eye(4)
S = [sp.simplify(burau_gen(i).subs({t: OMEGA})) for i in (1, 2, 3)]
r = sp.simplify(S[0] * S[1] * S[2])
T = [S[0]]
for _ in range(3):
    T.append(sp.simplify(r * T[-1] * r.inv()))
G = [sp.simplify((I3 - T[k]) * (I3 - T[k]).conjugate().T) for k in range(4)]
J = sp.Matrix([[0, 1 + sp.sqrt(3) * sp.I, -1 + sp.sqrt(3) * sp.I],
               [1 - sp.sqrt(3) * sp.I, 2, 1 + sp.sqrt(3) * sp.I],
               [-1 - sp.sqrt(3) * sp.I, 1 - sp.sqrt(3) * sp.I, 0]])
Jinv = J.inv()
M0 = sp.Matrix([[-1, (1 + sp.sqrt(3) * sp.I) / 2, (1 - sp.sqrt(3) * sp.I) / 2],
                [0, 0, 1],
                [0, 1, 0]])
GJ = [sp.simplify((I3 - T[k]) * Jinv * (I3 - T[k]).conjugate().T * J) for k in range(4)]
U1 = sp.simplify(3 * GJ[0])
V1J = sp.simplify(I3 + GJ[3] - GJ[1] * GJ[0])
Uc = sp.Matrix([[3, 0, 0], [3, 0, 0], [3, 0, 0]])
Vc = sp.Matrix([[0, 1, 0], [0, 2, 0], [0, 2, 1]])


def Gamma(A):
    return sp.simplify(M0 * A.conjugate() * M0.inv())


# ---------------------------------------------------------------- S1
print("=" * 72)
print("S1: the seam line -- real, S_0-reversed")
print("=" * 72)

Mst = sp.Matrix.vstack(U1, V1J - I3)
ns = Mst.nullspace()
check("S1.1 unique common eigenline: U v = 0, V v = v (dim 1)", len(ns) == 1)
v = sp.simplify(ns[0])
v = sp.simplify(v / v[2])
target = sp.Matrix([0, (sp.sqrt(3) - sp.I) / (sp.sqrt(3) + sp.I), 1])
check("S1.2 explicit seam vector v = (0, (sqrt3-i)/(sqrt3+i), 1)",
      sp.simplify(v - target) == sp.zeros(3, 1))
Rv = sp.simplify(M0 * v.conjugate())
check("S1.3 THE SEAM IS REAL: R fixes the seam line (R v ~ v)",
      sp.Matrix.hstack(v, Rv).rank() == 1)

P_, D_ = V1J.diagonalize()
order = [D_[i, i] for i in range(3)]
signs = tuple(1 if order[i] == 0 else -1 for i in range(3))
S0c = sp.simplify(P_ * sp.diag(*signs) * P_.inv())
check("S1.4 S_0 reverses the seam: S_0 v = -v (the v590 seam-reversal demand, geometric)",
      sp.simplify(S0c * v + v) == sp.zeros(3, 1))
check("S1.5 honest scope: S_0 does NOT commute with R (not Gamma-even)",
      sp.simplify(Gamma(S0c) - S0c) != sp.zeros(3, 3))

# ---------------------------------------------------------------- S2
print("=" * 72)
print("S2: the infinity cusp in the unreduced module")
print("=" * 72)

Su = [sp.simplify(burau_unred(i).subs({t: OMEGA})) for i in (1, 2, 3)]
ok_braid = (sp.simplify(Su[0] * Su[1] * Su[0] - Su[1] * Su[0] * Su[1]) == sp.zeros(4, 4)
            and sp.simplify(Su[0] * Su[2] - Su[2] * Su[0]) == sp.zeros(4, 4)
            and sp.simplify(Su[1] * Su[2] * Su[1] - Su[2] * Su[1] * Su[2]) == sp.zeros(4, 4))
check("S2.1 unreduced Burau braid relations at t = omega", ok_braid)
col = sp.Matrix([1, 1, 1, 1])
check("S2.2 invariant column (1,1,1,1): the trivial (infinity) line",
      all(sp.simplify(Su[i] * col - col) == sp.zeros(4, 1) for i in range(3)))
row = sp.Matrix([[1, OMEGA, sp.conjugate(OMEGA), 1]])
check("S2.3 invariant row (1, omega, conj omega, 1)",
      all(sp.simplify(row * Su[i] - row) == sp.zeros(1, 4) for i in range(3)))
ru = sp.simplify(Su[0] * Su[1] * Su[2])
full = sp.simplify(ru ** 4)
evs = {}
for ev, mult, _ in full.eigenvects():
    evs[sp.nsimplify(sp.simplify(ev))] = mult
check("S2.4 full twist r^4 eigenvalues {1 (x1), omega (x3)}: infinity line separated "
      "from the omega-sheet", evs.get(1) == 1 and evs.get(sp.nsimplify(OMEGA)) == 3,
      str(evs))

# ---------------------------------------------------------------- S3
print("=" * 72)
print("S3: the first mark-local Z/3 witness")
print("=" * 72)

Sat = sp.Matrix([[1, 2, 2, 0, 0, 0],
                 [0, 1, 1, -1, 0, 0],
                 [0, 0, 1, 1, -1, 1]])
Bs = [sp.Matrix([Sat[i, j] + OMEGA * Sat[i, 3 + j] for j in range(3)]) for i in range(3)]
Bfix = sp.Matrix.hstack(*Bs)
CU = sp.Matrix([[3, 0, 0], [-3, 0, 0], [0, 0, 0]])
CV = sp.Matrix([[2, 1, -1], [-2, -1, 2], [-2, -1, 2]])
words_int = [sp.eye(3), CU, CV, CU * CV, CV * CU, CV * CV, CV * CU * CV]
Wint = sp.Matrix([[wd[i, j] for i in range(3) for j in range(3)] for wd in words_int])


def mark_class(k):
    Ek = sp.simplify(G[k] + Gamma(G[k]))
    CEk = sp.simplify(Bfix.solve(sp.simplify(Ek * Bfix)))
    isint = all(sp.nsimplify(e).is_integer for e in CEk)
    vec = sp.Matrix(9, 1, [CEk[i, j] for i in range(3) for j in range(3)])
    try:
        coeffs, _ = Wint.T.gauss_jordan_solve(vec)
        coeffs = [sp.nsimplify(sp.simplify(c)) for c in coeffs.T]
        L = sp.lcm([sp.fraction(c)[1] for c in coeffs])
        return isint, True, L
    except ValueError:
        return isint, False, None


i1, in1, L1 = mark_class(0)
check("S3.1 E_1 restricts INTEGER, lies in the word algebra, class order = 3 "
      "(the first per-mark Z/3 witness)", i1 and in1 and L1 == 3, "lcm den = %s" % L1)
i4, in4, L4 = mark_class(3)
check("S3.2 E_4 in the algebra with trivial class (integer coefficients)",
      i4 and in4 and L4 == 1)
i2, in2, _ = mark_class(1)
i3, in3, _ = mark_class(2)
check("S3.3 [must-fail for the naive global map] E_2, E_3 lie OUTSIDE the "
      "mark-1-anchored algebra (equivariant per-mark framing typed)",
      i2 and i3 and (not in2) and (not in3))

# ---------------------------------------------------------------- S4
print("=" * 72)
print("S4: translator negatives, quantified")
print("=" * 72)

g_ = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (i, j)))
eqs = []
for E_ in [sp.expand(g_ * U1 - Uc * g_), sp.expand(g_ * V1J - Vc * g_)]:
    eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
sol = sp.solve(eqs, list(g_), dict=True)
gs = sp.simplify(g_.subs(sol[0]))
fs = sorted(gs.free_symbols, key=str)
g = sp.simplify(gs.subs({f: 1 for f in fs}))
Sig = sp.diag(1, -1, -1)
F2 = sp.simplify(g.T * Sig * g)
check("S4.1 pullback form F2 = g^T Sigma g is symmetric", sp.simplify(F2 - F2.T) == sp.zeros(3, 3))
B = sp.simplify(M0.conjugate().T * J)


def proportional(F, Fr):
    for ii in range(3):
        for jj in range(3):
            if Fr[ii, jj] != 0 and F[ii, jj] != 0:
                lam = sp.simplify(F[ii, jj] / Fr[ii, jj])
                return sp.simplify(F - lam * Fr) == sp.zeros(3, 3)
    return False


H1 = sp.simplify(I3 + (V1J * (V1J - I3)) / 2)
menu = [B, sp.simplify(B * S0c), sp.simplify(S0c.T * B), sp.simplify(B * V1J),
        sp.simplify(B * (V1J - I3)), sp.simplify(B * (I3 - 2 * GJ[0])), sp.simplify(B * H1)]
check("S4.2 [must-fail] F2 not proportional to any canonical menu form (7 tested)",
      not any(proportional(F2, Fr) for Fr in menu))

words_c = [I3, U1, V1J, sp.simplify(U1 * V1J), sp.simplify(V1J * U1),
           sp.simplify(V1J * V1J), sp.simplify(V1J * U1 * V1J)]
Wc = sp.Matrix([[wd[i, j] for i in range(3) for j in range(3)] for wd in words_c])


def in_algebra(X):
    vec = sp.Matrix(9, 1, [X[i, j] for i in range(3) for j in range(3)])
    try:
        Wc.T.gauss_jordan_solve(vec)
        return True
    except ValueError:
        return False


check("S4.3 [must-fail] neither B^-1 F2 nor F2 B^-1 lies in the word algebra "
      "(the translator needs a new canonical object -- named open)",
      not in_algebra(sp.simplify(B.inv() * F2)) and not in_algebra(sp.simplify(F2 * B.inv())))

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: SEAM-REAL-LANDED -- the seam line is a real line of the cover,")
    print("S_0 reverses it geometrically; the infinity cusp is separated in the")
    print("unreduced module; the first per-mark Z/3 witness lands (E_1, order 3);")
    print("the corpus-transpose translator stays honestly open.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
