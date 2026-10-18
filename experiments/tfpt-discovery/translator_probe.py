#!/usr/bin/env python3
"""The translator round: the corpus RP anti-automorphism IS the J-adjoint
twisted by an explicit inner element; the seam is 3-torsion at infinity;
the 81 survives frame-joining; the J_fix duality is certified.

Round 9 of the QGEO cover program (after v604).  Executes the follow-up
slate "omega-bar translator / seam-infinity bridge / 81-27 sequence /
Lean addendum":

  (T1) THE TRANSLATOR EXISTS [E, the centerpiece]: pulling the corpus RP
       anti-automorphism theta(X) = Sigma X^T Sigma back along the
       compiler conjugation and composing with the J-adjoint gives an
       algebra AUTOMORPHISM phi = Jadj o theta_pull -- and phi is INNER:
       the intertwiner space is 1-dimensional, its generator c is
       invertible, and phi(A) = c A c^-1 holds EXACTLY on the pair.
       Hence THE CORPUS RP STRUCTURE IS THE J-ADJOINT COMPOSED WITH THE
       INNER TWIST BY c: the RP anti-automorphism is fully expressed in
       curve language (polarization + one explicit element).  The
       normalization 14 c is Z[omega]-INTEGRAL (denominator 14 = 2 x 7,
       the parabolic dimension).  Honest scope: c is unique-up-to-scale
       by construction, but not Gamma-even and not in the word algebra
       -- its independent geometric identity is the named open.

  (T2) THE SEAM IS 3-TORSION AT INFINITY [E]: in the Smith coordinates
       of coker(1 - T_inf) = Z^2 + (Z/3)^3 (v604), the seam lift
       (-conj(omega), -conj(omega), 0, -omega) has FREE coordinates
       (0, 0) and torsion coordinates (2, 2, 0) mod 3: the seam line is
       a NONZERO pure-torsion class of the infinity monodromy cokernel
       -- the integral seam <-> infinity bridge.

  (T3) THE 81 SURVIVES FRAME-JOINING [E]: inside the frame-1 span, the
       order chain O_1 subset (O_joint intersect span_1) subset P_1 has
       indices 3^5 = 243 and 3^4 = 81: joining all four frames refines
       each frame's order by exactly 3^5, and the residual saturation
       defect is EXACTLY the v566 index 81.

  (T4) THE J_FIX DUALITY CERTIFIED [E]: C_V^T J_fix = J_fix C_Vdual with
       the explicit integer C_Vdual = [[1,0,0],[-2,0,0],[2,1,2]] (char
       x(x-1)(x-2), dual joint trace tr(C_U C_Vdual) = 3, char(C_U +
       C_Vdual) = x(x-2)(x-4)); Lean addendum in
       TfptCarrier/CoverEmbedding.lean (Jfix_symmetric, Jfix_det = 72,
       CV_dual_certificate, CVdual_cubic, dual_joint_trace; lake build
       green).

All checks exact (sympy).  Verdict enums (frozen): TRANSLATOR-LANDED
(all), TRANSLATOR-FAILS, MIXED.
"""

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

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


def zw_coords(e):
    e = sp.expand(e)
    b = sp.nsimplify(2 * sp.im(e) / sp.sqrt(3))
    a = sp.nsimplify(sp.re(e) + sp.im(e) / sp.sqrt(3))
    return a, b


I3 = sp.eye(3)
I4 = sp.eye(4)
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
V1J = sp.simplify(I3 + GJ[3] - GJ[1] * GJ[0])
Uc = sp.Matrix([[3, 0, 0], [3, 0, 0], [3, 0, 0]])
Vc = sp.Matrix([[0, 1, 0], [0, 2, 0], [0, 2, 1]])
Sig = sp.diag(1, -1, -1)

# ---------------------------------------------------------------- T1
print("=" * 72)
print("T1: the translator -- theta_corpus = Jadj o inner(c)")
print("=" * 72)

g_ = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (i, j)))
eqs = []
for E_ in [sp.expand(g_ * U1 - Uc * g_), sp.expand(g_ * V1J - Vc * g_)]:
    eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
sol = sp.solve(eqs, list(g_), dict=True)
gs = sp.simplify(g_.subs(sol[0]))
fs = sorted(gs.free_symbols, key=str)
g = sp.simplify(gs.subs({f: 1 for f in fs}))
gi = g.inv()


def theta_pull(A):
    return sp.simplify(gi * Sig * (g * A * gi).T * Sig * g)


def Jadj(A):
    return sp.simplify(Jinv * A.conjugate().T * J)


phiU = sp.simplify(Jadj(theta_pull(U1)))
phiV = sp.simplify(Jadj(theta_pull(V1J)))
check("T1.1 phi = Jadj o theta_pull preserves the spectra (algebra automorphism data)",
      sp.expand(sp.factor(sp.expand((x * I3 - phiU).det())) - x ** 2 * (x - 3)) == 0
      and sp.expand(sp.factor(sp.expand((x * I3 - phiV).det())) - x * (x - 1) * (x - 2)) == 0)

c_ = sp.Matrix(3, 3, lambda i, j: sp.Symbol("c%d%d" % (i, j)))
eqs = []
for A, phiA in [(U1, phiU), (V1J, phiV)]:
    E_ = sp.expand(c_ * A - phiA * c_)
    eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
solc = sp.solve(eqs, list(c_), dict=True)
cs = sp.simplify(c_.subs(solc[0]))
fsc = sorted(cs.free_symbols, key=str)
check("T1.2 the intertwiner space is 1-dimensional (c unique up to scale)",
      len(solc) == 1 and len(fsc) == 1)
cmat = sp.simplify(cs.subs({f: 1 for f in fsc}))
ok_inner = (sp.simplify(cmat.det()) != 0
            and sp.simplify(cmat * U1 * cmat.inv() - phiU) == sp.zeros(3, 3)
            and sp.simplify(cmat * V1J * cmat.inv() - phiV) == sp.zeros(3, 3))
check("T1.3 phi is INNER: phi(A) = c A c^-1 exactly -- the corpus RP structure "
      "IS Jadj twisted by c", ok_inner)
c14 = sp.simplify(14 * cmat)
ok_int = all(all(v.is_integer for v in zw_coords(e)) for e in c14)
check("T1.4 14 c is Z[omega]-INTEGRAL (denominator 14 = 2 x 7)", ok_int)


def Gamma(A):
    return sp.simplify(M0 * A.conjugate() * M0.inv())


words = [I3, U1, V1J, sp.simplify(U1 * V1J), sp.simplify(V1J * U1),
         sp.simplify(V1J * V1J), sp.simplify(V1J * U1 * V1J)]
Wm = sp.Matrix([[wd[i, j] for i in range(3) for j in range(3)] for wd in words])
vec = sp.Matrix(9, 1, [cmat[i, j] for i in range(3) for j in range(3)])
try:
    Wm.T.gauss_jordan_solve(vec)
    in_alg = True
except ValueError:
    in_alg = False
check("T1.5 honest scope: c not Gamma-even, not in the word algebra (identity open)",
      sp.simplify(Gamma(cmat) - cmat) != sp.zeros(3, 3) and not in_alg)

# ---------------------------------------------------------------- T2
print("=" * 72)
print("T2: the seam is 3-torsion at infinity")
print("=" * 72)

Su = [sp.simplify(burau_unred(i).subs({t: OMEGA})) for i in (1, 2, 3)]
ru = sp.simplify(Su[0] * Su[1] * Su[2])
Tinf = sp.simplify(ru ** 4)
D_ = sp.simplify(I4 - Tinf)
cols = []
for j in range(4):
    for mult in (1, OMEGA):
        v = sp.zeros(4, 1)
        v[j] = mult
        img = sp.expand(D_ * v)
        col = []
        for i in range(4):
            a, b = zw_coords(img[i])
            col.extend([a, b])
        cols.append([sp.Integer(e) for e in col])
Mz = sp.Matrix(cols).T


def snf_transforms(A):
    A = A.copy()
    m, n = A.shape
    U = sp.eye(m)
    V = sp.eye(n)
    k = 0
    while k < min(m, n):
        while True:
            best = None
            pos = None
            for i in range(k, m):
                for j in range(k, n):
                    if A[i, j] != 0 and (best is None or abs(A[i, j]) < best):
                        best = abs(A[i, j])
                        pos = (i, j)
            if pos is None:
                break
            pi, pj = pos
            A.row_swap(k, pi)
            U.row_swap(k, pi)
            A.col_swap(k, pj)
            V.col_swap(k, pj)
            done = True
            for i in range(k + 1, m):
                q = A[i, k] // A[k, k]
                if q != 0:
                    A[i, :] -= q * A[k, :]
                    U[i, :] -= q * U[k, :]
                if A[i, k] != 0:
                    done = False
            for j in range(k + 1, n):
                q = A[k, j] // A[k, k]
                if q != 0:
                    A[:, j] -= q * A[:, k]
                    V[:, j] -= q * V[:, k]
                if A[k, j] != 0:
                    done = False
            if done:
                break
        k += 1
    return A, U, V


D8, U8, V8 = snf_transforms(Mz.copy())
seam = sp.Matrix([-sp.conjugate(OMEGA), -sp.conjugate(OMEGA), 0, -OMEGA])
sv = []
for i in range(4):
    a, b = zw_coords(seam[i])
    sv.extend([a, b])
sv = sp.Matrix(8, 1, [sp.Integer(e) for e in sv])
y = sp.expand(U8 * sv)
free_ok = True
tor = []
for i in range(8):
    d = D8[i, i]
    if d == 0:
        if y[i] != 0:
            free_ok = False
    elif abs(d) == 3:
        tor.append(int(sp.Mod(y[i], 3)))
check("T2.1 seam lift has ZERO free coordinates in coker(1 - T_inf)", free_ok)
check("T2.2 seam lift is a NONZERO 3-torsion class (torsion coords (2,2,0) pattern)",
      sorted(tor) == [0, 2, 2], str(tor))

# ---------------------------------------------------------------- T3
print("=" * 72)
print("T3: the 81 survives frame-joining")
print("=" * 72)

pair0 = words
frames = [pair0]
rk = I3
for _ in range(3):
    rk = sp.simplify(r * rk)
    frames.append([sp.simplify(rk * wd * rk.inv()) for wd in pair0])


def to18(wd):
    out = []
    for mult in (1, OMEGA):
        rr = []
        for e in (mult * wd):
            a, b = zw_coords(e)
            rr.extend([a, b])
        out.append([sp.Integer(v_) for v_ in rr])
    return out


O1_vecs = []
for wd in pair0:
    O1_vecs.extend(to18(wd))
OJ_vecs = []
for fr in frames:
    for wd in fr:
        OJ_vecs.extend(to18(wd))
O1 = sp.Matrix(O1_vecs)
OJ = sp.Matrix(OJ_vecs)
HB = hermite_normal_form(sp.Matrix(OJ).T)
Bjoint = HB.T
Kcols = sp.Matrix.hstack(*O1.nullspace())
Cmat = sp.expand(Bjoint * Kcols)
ker = sp.Matrix.hstack(*(Cmat.T).nullspace())
den = sp.lcm([sp.fraction(sp.nsimplify(e))[1] for e in ker])
kerZ = sp.Matrix([[sp.Integer(e * den) for e in row] for row in ker.T.tolist()])
Dk, Uk, Vk = snf_transforms(kerZ.copy())
sat_rows = []
for i in range(14):
    rowv = sp.zeros(1, 18)
    rowv[0, i] = 1
    sat_rows.append(list(rowv * Vk.inv()))
kerSat = sp.Matrix([[sp.Integer(e) for e in row] for row in sat_rows])
Lbasis = sp.expand(kerSat * Bjoint)
X = sp.zeros(14, 14)
LT = Lbasis.T
ok_membership = True
for i in range(14):
    solx = LT.gauss_jordan_solve(O1[i, :].T)[0]
    for j in range(14):
        X[i, j] = sp.nsimplify(solx[j])
        if not X[i, j].is_integer:
            ok_membership = False
check("T3.1 O_1 sits inside O_joint^span_1 with integer transition", ok_membership)
check("T3.2 index [O_joint^span_1 : O_1] = 243 = 3^5, hence [P_1 : O_joint^span_1] = "
      "3^9/3^5 = 81 = 3^4: THE 81 SURVIVES", abs(X.det()) == 243,
      "|det| = %s" % abs(X.det()))

# ---------------------------------------------------------------- T4
print("=" * 72)
print("T4: the J_fix duality certificate")
print("=" * 72)

Jfix = sp.Matrix([[16, 2, 4], [2, -2, 2], [4, 2, -2]])
CU = sp.Matrix([[3, 0, 0], [-3, 0, 0], [0, 0, 0]])
CV = sp.Matrix([[2, 1, -1], [-2, -1, 2], [-2, -1, 2]])
CVd = sp.Matrix([[1, 0, 0], [-2, 0, 0], [2, 1, 2]])
check("T4.1 C_V^T J_fix = J_fix C_Vdual (explicit integer dual)",
      sp.simplify(CV.T * Jfix - Jfix * CVd) == sp.zeros(3, 3))
check("T4.2 dual carries the binary code: char C_Vdual = x(x-1)(x-2), tr(C_U C_Vdual) = 3, "
      "char(C_U + C_Vdual) = x(x-2)(x-4)",
      sp.expand(sp.factor(sp.expand((x * I3 - CVd).det())) - x * (x - 1) * (x - 2)) == 0
      and sp.trace(CU * CVd) == 3
      and sp.expand(sp.factor(sp.expand((x * I3 - (CU + CVd)).det())) - x * (x - 2) * (x - 4)) == 0)

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: TRANSLATOR-LANDED -- the corpus RP anti-automorphism is the")
    print("J-adjoint twisted by the explicit inner element c (14c integral); the")
    print("seam is nonzero 3-torsion at infinity; the 81 survives frame-joining as")
    print("the saturation defect; the J_fix duality is certified (Lean green).")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
