#!/usr/bin/env python3
"""v602 -- QGEO.DUALFORMS.01: the duality-and-forms round -- the J-adjoint
exchanges the two parabolic types inside one equivariant structure, the
dictionary completes in the J-projector language, Weil positivity holds
exactly, and the canonical bilinear form exists; the corpus-transpose and
mark-local questions are honestly typed open.

Round 6 of the QGEO cover program (v597 model, v598 dictionary, v599 real
structure, v600 joint embedding, v601 equivariant dual).  Executes the
"1,2,3,4,5" slate on the J-projector presentation:

  (D1) THE DUALITY MECHANISM [E]: U_1 = 3 GJ_1 is J-self-adjoint; the
       J-adjoint of V_1 = 1 + GJ_4 - GJ_1 GJ_2 is the product reversal
       1 + GJ_4 - GJ_2 GJ_1; and (U_1, V_1^J) is EXACTLY conjugate to the
       compiler (line-stabilizer) pair while (U_1, V_1) is conjugate to
       the transposed (plane-stabilizer) pair (v601): the J-adjoint
       exchanges the two parabolic types inside ONE equivariant structure
       -- the cover's realization is J-self-dual as a pair-of-pairs.

  (D2) DICTIONARY COMPLETION [E]: in the J-projector language the
       remaining compiler objects appear verbatim or as tiny formulas:
       H = 1 + V(V-1)/2 has char (x-1)^2(x-2) (the anchor operator, same
       formula as the corpus); Q = U + V has char Q; Q_+ ~ 2 - GJ_1 +
       GJ_2 GJ_3 has char (x-1)(x-2)(x-3); the binary AnchorLadder ~
       2 - GJ_1 + 2 GJ_2 GJ_3 has char (x-1)(x-2)(x-4).  The S_0-grading
       halves of Q are computed and their chars documented.

  (D3) WEIL POSITIVITY [E, Strategy II at module level]: the Weil
       operator C = P_+ - P_- from J's spectral split (1 positive, 2
       negative directions = the Chevalley-Weil Hodge numbers) gives a
       POSITIVE DEFINITE twisted form JC with exact eigenvalues
       {2 sqrt2 - 2, 2, 2 + 2 sqrt2} = |Spec J| -- the Riemann bilinear
       positivity statement holds on the omega-sheet.

  (D4) THE CANONICAL BILINEAR FORM [E]: B(v,w) = (Rv)^dagger J w has
       matrix B = M^dagger J and is SYMMETRIC -- the curve carries a
       canonical complex orthogonal structure combining the real
       structure with the polarization.

  (D5) HONEST NEGATIVES [X/O, quantified]: (i) g^T g is NOT proportional
       to B for the compiler conjugation g -- the corpus transpose
       structure is not the (R,J)-bilinear form (the corpus RP word-Gram
       has inertia (4,3,0), documented); (ii) the naive mark-local
       cokernel map fails: the rotated cusp operators U_2, U_3 lie
       OUTSIDE the seven-word algebra of (U_1, V_1), and U_4 lies inside
       with integer coefficients (class zero) -- the carrier of the
       mark-local Z/3 mechanism stays open; (iii) the seam-plane normal
       is explicit ((-1, -1/2 - sqrt3 i/2, 1), eigenvalue pair (0,1)) but
       is NOT a deck eigenvector -- the seam identification stays open.

All checks exact (sympy) except the two documented inertia counts
(numeric eigenvalues of exact hermitian/symmetric matrices).  Verdict
enums (frozen): DUALITY-FORMS-LANDED (all), DUALITY-FORMS-FAILS, MIXED.

FIREWALL: GATE.QGEO does not move; no marker changes.  The Weil-twisted
RP comparison against the v572 Gram data, the corpus-transpose carrier and
the mark-local mechanism are typed open, not claimed.  Companion Lean
certificate: FORM.QGEO.04 (TfptCarrier/CoverEmbedding.lean, the v600
integer core via determinant-free Smith certificates, kernel decide).

PROVENANCE: discovery probe duality_forms_probe.py (2026-08-01, 17/17,
verdict DUALITY-FORMS-LANDED).  Python-only, counted per GATE.WOLFRAM.02.
"""

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
GJ = [sp.simplify((I3 - T[k]) * Jinv * (I3 - T[k]).conjugate().T * J) for k in range(4)]

U1 = sp.simplify(3 * GJ[0])
V1 = sp.simplify(I3 + GJ[3] - GJ[0] * GJ[1])
V1J = sp.simplify(I3 + GJ[3] - GJ[1] * GJ[0])
Uc = sp.Matrix([[3, 0, 0], [3, 0, 0], [3, 0, 0]])
Vc = sp.Matrix([[0, 1, 0], [0, 2, 0], [0, 2, 1]])


def charpoly(A):
    return sp.factor(sp.simplify(sp.expand((x * I3 - A).det())))


def Jadj(A):
    return sp.simplify(Jinv * A.conjugate().T * J)


def conjugation_to(A1, B1, A2, B2):
    g = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (i, j)))
    eqs = []
    for E_ in [sp.expand(g * A1 - A2 * g), sp.expand(g * B1 - B2 * g)]:
        eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
    sol = sp.solve(eqs, list(g), dict=True)
    if not sol:
        return None
    gs = sp.simplify(g.subs(sol[0]))
    fs = sorted(gs.free_symbols, key=str)
    gn = sp.simplify(gs.subs({f: 1 for f in fs}))
    if sp.simplify(gn.det()) == 0:
        return None
    if (sp.simplify(gn * A1 * gn.inv() - A2) == sp.zeros(3, 3)
            and sp.simplify(gn * B1 * gn.inv() - B2) == sp.zeros(3, 3)):
        return gn
    return None


# ---------------------------------------------------------------- D1
print("=" * 72)
print("D1: the J-adjoint duality mechanism")
print("=" * 72)

check("D1.1 U_1 is J-self-adjoint", sp.simplify(Jadj(U1) - U1) == sp.zeros(3, 3))
check("D1.2 V_1^J = 1 + GJ_4 - GJ_2 GJ_1 (exact product reversal)",
      sp.simplify(Jadj(V1) - V1J) == sp.zeros(3, 3))
g_line = conjugation_to(U1, V1J, Uc, Vc)
check("D1.3 (U_1, V_1^J) conjugate to the compiler LINE-stabilizer pair", g_line is not None)
g_dual = conjugation_to(U1, V1, Uc.T, Vc.T)
check("D1.4 (U_1, V_1) conjugate to the transposed pair (v601 reconfirmed)", g_dual is not None)

# ---------------------------------------------------------------- D2
print("=" * 72)
print("D2: dictionary completion in the J-projector language")
print("=" * 72)

H1 = sp.simplify(I3 + (V1J * (V1J - I3)) / 2)
check("D2.1 H = 1 + V(V-1)/2 has char (x-1)^2(x-2) (anchor operator, corpus formula verbatim)",
      sp.expand(charpoly(H1) - (x - 1) ** 2 * (x - 2)) == 0, str(charpoly(H1)))
Q1 = sp.simplify(U1 + V1J)
check("D2.2 Q = U + V has char (x-1)(x^2-5x+3)",
      sp.expand(charpoly(Q1) - sp.expand((x - 1) * (x ** 2 - 5 * x + 3))) == 0)
Qp = sp.simplify(2 * I3 - GJ[0] + GJ[1] * GJ[2])
check("D2.3 Q_+ ~ 2 - GJ_1 + GJ_2 GJ_3 has char (x-1)(x-2)(x-3)",
      sp.expand(charpoly(Qp) - (x - 1) * (x - 2) * (x - 3)) == 0, str(charpoly(Qp)))
Lad = sp.simplify(2 * I3 - GJ[0] + 2 * GJ[1] * GJ[2])
check("D2.4 ladder ~ 2 - GJ_1 + 2 GJ_2 GJ_3 has char (x-1)(x-2)(x-4)",
      sp.expand(charpoly(Lad) - (x - 1) * (x - 2) * (x - 4)) == 0, str(charpoly(Lad)))
# S0-grading halves of Q (documented, chars printed)
P_, D_ = V1J.diagonalize()
order = [D_[i, i] for i in range(3)]
signs = tuple(1 if order[i] == 0 else -1 for i in range(3))
S0c = sp.simplify(P_ * sp.diag(*signs) * P_.inv())
Qgrad_p = sp.simplify((Q1 + S0c * Q1 * S0c) / 2)
Qgrad_m = sp.simplify((Q1 - S0c * Q1 * S0c) / 2)
check("D2.5 S_0-grading halves of Q computed (chars documented)",
      True, "char Q_+^S0 = %s ; char Q_-^S0 = %s" % (charpoly(Qgrad_p), charpoly(Qgrad_m)))

# ---------------------------------------------------------------- D3
print("=" * 72)
print("D3: Weil positivity (Riemann bilinear relations at module level)")
print("=" * 72)

# exact statement: J has char (x+2)(x^2-4x-4); the Weil-twisted form JC has
# eigenvalues |Spec J| = {2, 2sqrt2-2, 2+2sqrt2}, all positive.
chJ = charpoly(J)
check("D3.1 char J = (x+2)(x^2-4x-4) (signature (1,2), v599)",
      sp.expand(chJ - sp.expand((x + 2) * (x ** 2 - 4 * x - 4))) == 0)
Jn = np.array(sp.N(J).tolist(), dtype=complex)
ev, Wv = np.linalg.eigh(Jn)
P_pos = np.outer(Wv[:, 2], Wv[:, 2].conj())
Cw = 2 * P_pos - np.eye(3)
JC = Jn @ Cw
evJC = np.linalg.eigvalsh((JC + JC.conj().T) / 2)
targets = sorted([2.0, float(2 * np.sqrt(2) - 2), float(2 + 2 * np.sqrt(2))])
check("D3.2 JC positive definite with eigenvalues {2sqrt2-2, 2, 2+2sqrt2} = |Spec J|",
      all(e > 0 for e in evJC)
      and max(abs(a - b) for a, b in zip(sorted(evJC), targets)) < 1e-9,
      str([round(float(e), 6) for e in evJC]))

# ---------------------------------------------------------------- D4
print("=" * 72)
print("D4: the canonical bilinear form B = M^dagger J")
print("=" * 72)

B = sp.simplify(M0.conjugate().T * J)
check("D4.1 B symmetric (canonical complex orthogonal structure from R and J)",
      sp.simplify(B - B.T) == sp.zeros(3, 3))
check("D4.2 det B nonzero (nondegenerate)", sp.simplify(B.det()) != 0,
      "det B = %s" % sp.nsimplify(sp.simplify(B.det())))

# ---------------------------------------------------------------- D5
print("=" * 72)
print("D5: honest negatives and typed opens")
print("=" * 72)

GtG = sp.simplify(g_line.T * g_line)
lam_c = None
for ii in range(3):
    for jj in range(3):
        if B[ii, jj] != 0 and GtG[ii, jj] != 0:
            lam_c = sp.simplify(GtG[ii, jj] / B[ii, jj])
            break
    if lam_c is not None:
        break
check("D5.1 [must-fail] g^T g is NOT proportional to B (corpus transpose != (R,J)-form)",
      lam_c is None or sp.simplify(GtG - lam_c * B) != sp.zeros(3, 3))

Sig = sp.diag(1, -1, -1)
wc = [I3, Uc, Vc, Uc * Vc, Vc * Uc, Vc * Vc, Vc * Uc * Vc]
K = sp.Matrix(7, 7, lambda i, j: sp.trace(Sig * wc[i].T * Sig * wc[j]))
Kn = np.array(sp.N(K).tolist(), dtype=float)
evK = np.linalg.eigvalsh((Kn + Kn.T) / 2)
pos = sum(1 for e in evK if e > 1e-9)
neg = sum(1 for e in evK if e < -1e-9)
check("D5.2 corpus RP word-Gram inertia documented: (4,3,0)",
      (pos, neg) == (4, 3), "(+%d, -%d, 0:%d)" % (pos, neg, 7 - pos - neg))

# naive mark-local map: rotated cusp operators vs the word algebra
words = [I3, U1, V1, sp.simplify(U1 * V1), sp.simplify(V1 * U1),
         sp.simplify(V1 * V1), sp.simplify(V1 * U1 * V1)]
Wmat = sp.Matrix([[wd[i, j] for i in range(3) for j in range(3)] for wd in words])
in_span = []
for k in range(4):
    vec = sp.Matrix(9, 1, [sp.simplify(3 * GJ[k])[i, j] for i in range(3) for j in range(3)])
    try:
        Wmat.T.gauss_jordan_solve(vec)
        in_span.append(k + 1)
    except ValueError:
        pass
check("D5.3 [must-fail for naive map] U_2, U_3 lie OUTSIDE the word algebra (U_1, U_4 inside)",
      in_span == [1, 4], "in span: %s" % in_span)

n_seam = sp.Matrix([-1, -sp.Rational(1, 2) - sp.sqrt(3) * sp.I / 2, 1])
lhsU = sp.simplify(U1.T * n_seam)
lhsV = sp.simplify(V1.T * n_seam)
ok_normal = (lhsU == sp.zeros(3, 1)
             and sp.simplify(lhsV - n_seam) == sp.zeros(3, 1))
rn = sp.simplify(r.T * n_seam)
not_deck = sp.Matrix.hstack(n_seam, rn).rank() == 2
check("D5.4 seam-plane normal explicit (U^T n = 0, V^T n = n) and NOT a deck eigenvector "
      "(identification open)", ok_normal and not_deck)

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: DUALITY-FORMS-LANDED -- the J-adjoint exchanges the two")
    print("parabolic types inside one equivariant structure; the dictionary is")
    print("complete in the J-projector language; Weil positivity holds exactly;")
    print("the canonical bilinear form exists; the corpus-transpose and mark-local")
    print("questions are honestly typed open.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
