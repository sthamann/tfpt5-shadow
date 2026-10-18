#!/usr/bin/env python3
"""The canonical equivariant realization: J-projectors, duality, Klein group.

Round 5 of the QGEO cover program (v597 model, v598 dictionary, v599 real
structure, v600 joint embedding).  v600 established EXISTENCE of the compiler
pair on the mu3-cover but left canonicity open, and the naive cusp-Gram
presentation failed D4 equivariance (the standard hermitian dagger is
basis-dependent; the Burau image preserves J, not the standard form).
This probe repairs both with the J-adapted building blocks

  GJ_k = (1 - T_k) J^{-1} (1 - T_k)^dagger J,

and lands four results:

  (C1) CANONICAL PROJECTORS [E]: the four GJ_k are IDEMPOTENT rank-1
       J-self-adjoint projectors (char x^2(x-1)) and rotate exactly:
       r GJ_k r^{-1} = GJ_{k+1} -- manifest D4 equivariance.  Opposite
       cusps are J-orthogonal (tr(GJ_1 GJ_3) = 0); neighbors overlap with
       trace 1.

  (C2) THE EQUIVARIANT PAIR [E]: U_k = 3 GJ_k and
       V_k = 1 + GJ_{k-1} - GJ_k GJ_{k+1} are Z[omega]-integral with the
       compiler spectra (x^2(x-3), x(x-1)(x-2)), the compiler joint data
       (char(U+V) = charQ, tr(UV) = 3, tr(UV^2) = 6) and seven-word rank 7;
       the whole family is D4-equivariant BY CONSTRUCTION and verified:
       r^k (U_1, V_1) r^{-k} = (U_{k+1}, V_{k+1}) for all marks.  The
       mark choice IS the compiler's winding choice.

  (C3) THE DUALITY [E]: the equivariant pair is NOT conjugate to the
       compiler pair (the intertwiner space to (U_c, V_c) is 1-dimensional
       with identically singular solutions) but IS exactly conjugate to the
       TRANSPOSED pair (U_c^T, V_c^T) (det g = -h^3, invertible, exact):
       the equivariant realization is the DUAL (plane-stabilizer) parabolic,
       while the v600 Gamma-even pair realizes the line-stabilizer.  The
       cover carries BOTH parabolic types, exchanged by duality.

  (C4) THE KLEIN GROUP ON THE CURVE [E]: all EIGHT spectral-sign
       involutions of V_1 are Z[omega]-integral (the v590 rigidity
       reproduced on the curve); the two v590 demands (+1 on ker V, flip
       the sheet pair {1,2}) select the explicit integral S_0 with trace
       -1, and the single-pair flips A, B are integral with A B = S_0 --
       the v590/Lean Klein four-group lives on the cover.

  (C5) HONEST NEGATIVES/OPENS: the naive J-word Gram tr(J^{-1} w_i^dag J
       w_j) on the seven words is hermitian with inertia (3,2,2) -- NOT
       the corpus v572 RP-kernel pattern (4,0,3); the Hodge-positivity
       comparison (Strategy II) needs the Weil-twisted polarization, named
       as the next step, not claimed.  The seam-line geometric
       identification (which canonical curve object is ker V / the flag
       line) stays open.

All checks exact (sympy) except the inertia count (numeric eigenvalues of
an exact hermitian matrix).  Verdict enums (frozen):
EQUIVARIANT-DUAL-LANDED (all), EQUIVARIANT-DUAL-FAILS, MIXED.
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
GJ = [sp.simplify((I3 - T[k]) * Jinv * (I3 - T[k]).conjugate().T * J) for k in range(4)]


def charpoly(A):
    return sp.factor(sp.simplify(sp.expand((x * I3 - A).det())))


def zw_coords(e):
    e = sp.expand(e)
    b = sp.nsimplify(2 * sp.im(e) / sp.sqrt(3))
    a = sp.nsimplify(sp.re(e) + sp.im(e) / sp.sqrt(3))
    return a, b


def zw_integral(A):
    return all(all(c.is_integer for c in zw_coords(e)) for e in A)


# ---------------------------------------------------------------- C1
print("=" * 72)
print("C1: the four J-projectors -- idempotent, equivariant, orthogonality")
print("=" * 72)

ok_idem = all(sp.simplify(GJ[k] * GJ[k] - GJ[k]) == sp.zeros(3, 3) for k in range(4))
ok_char = all(sp.expand(charpoly(GJ[k]) - x ** 2 * (x - 1)) == 0 for k in range(4))
check("C1.1 GJ_k idempotent with char x^2(x-1) (rank-1 projectors)", ok_idem and ok_char)
ok_rot = all(sp.simplify(r * GJ[k] * r.inv() - GJ[(k + 1) % 4]) == sp.zeros(3, 3) for k in range(4))
check("C1.2 exact D4 rotation: r GJ_k r^-1 = GJ_(k+1)", ok_rot)
check("C1.3 opposite cusps J-orthogonal: tr(GJ1 GJ3) = 0 = tr(GJ2 GJ4); neighbors tr = 1",
      sp.simplify(sp.trace(GJ[0] * GJ[2])) == 0
      and sp.simplify(sp.trace(GJ[1] * GJ[3])) == 0
      and sp.simplify(sp.trace(GJ[0] * GJ[1])) == 1
      and sp.simplify(sp.trace(GJ[1] * GJ[2])) == 1)

# ---------------------------------------------------------------- C2
print("=" * 72)
print("C2: the equivariant pair family")
print("=" * 72)


def pair(k):
    return (sp.simplify(3 * GJ[k % 4]),
            sp.simplify(I3 + GJ[(k + 3) % 4] - GJ[k % 4] * GJ[(k + 1) % 4]))


U1, V1 = pair(0)
check("C2.1 U_1, V_1 integral over Z[omega]", zw_integral(U1) and zw_integral(V1))
check("C2.2 chars: x^2(x-3) and x(x-1)(x-2)",
      sp.expand(charpoly(U1) - x ** 2 * (x - 3)) == 0
      and sp.expand(charpoly(V1) - x * (x - 1) * (x - 2)) == 0)
check("C2.3 joint data: char(U+V) = (x-1)(x^2-5x+3), tr(UV) = 3, tr(UV^2) = 6",
      sp.expand(charpoly(sp.simplify(U1 + V1)) - sp.expand((x - 1) * (x ** 2 - 5 * x + 3))) == 0
      and sp.simplify(sp.trace(U1 * V1) - 3) == 0
      and sp.simplify(sp.trace(U1 * V1 * V1) - 6) == 0)
words = [I3, U1, V1, sp.simplify(U1 * V1), sp.simplify(V1 * U1),
         sp.simplify(V1 * V1), sp.simplify(V1 * U1 * V1)]
check("C2.4 seven-word rank 7",
      sp.Matrix([[W_[i, j] for i in range(3) for j in range(3)] for W_ in words]).rank() == 7)

rk = I3
ok_eq = True
for k in (1, 2, 3):
    rk = sp.simplify(r * rk)
    Uk, Vk = pair(k)
    ok_eq = (ok_eq
             and sp.simplify(rk * U1 * rk.inv() - Uk) == sp.zeros(3, 3)
             and sp.simplify(rk * V1 * rk.inv() - Vk) == sp.zeros(3, 3))
check("C2.5 full D4 equivariance: r^k (U_1,V_1) r^-k = (U_(k+1),V_(k+1)) for all marks", ok_eq)

# ---------------------------------------------------------------- C3
print("=" * 72)
print("C3: the duality -- conjugate to the TRANSPOSED compiler pair")
print("=" * 72)

Uc = sp.Matrix([[3, 0, 0], [3, 0, 0], [3, 0, 0]])
Vc = sp.Matrix([[0, 1, 0], [0, 2, 0], [0, 2, 1]])


def intertwiner(A1, B1, A2, B2):
    g = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (i, j)))
    eqs = []
    for E_ in [sp.expand(g * A1 - A2 * g), sp.expand(g * B1 - B2 * g)]:
        eqs.extend([E_[i, j] for i in range(3) for j in range(3)])
    sol = sp.solve(eqs, list(g), dict=True)
    if not sol:
        return None, None
    gs = sp.simplify(g.subs(sol[0]))
    return gs, sp.factor(sp.simplify(gs.det()))


gs_direct, det_direct = intertwiner(U1, V1, Uc, Vc)
check("C3.1 [must-fail] intertwiner to (U_c, V_c) is identically singular",
      gs_direct is not None and det_direct == 0, "det = %s" % det_direct)

gs_dual, det_dual = intertwiner(U1, V1, Uc.T, Vc.T)
ok_dual = False
if gs_dual is not None and det_dual != 0:
    fs = sorted(gs_dual.free_symbols, key=str)
    gn = sp.simplify(gs_dual.subs({f: 1 for f in fs}))
    if sp.simplify(gn.det()) != 0:
        ok_dual = (sp.simplify(gn * U1 * gn.inv() - Uc.T) == sp.zeros(3, 3)
                   and sp.simplify(gn * V1 * gn.inv() - Vc.T) == sp.zeros(3, 3))
check("C3.2 conjugation to (U_c^T, V_c^T) exact: the DUAL parabolic realized", ok_dual,
      "det g = %s" % det_dual)

# ---------------------------------------------------------------- C4
print("=" * 72)
print("C4: the Klein group on the curve")
print("=" * 72)

P, D = V1.diagonalize()
order = [D[i, i] for i in range(3)]
sign_invs = {}
n_int = 0
for signs in itertools.product([1, -1], repeat=3):
    Sx = sp.simplify(P * sp.diag(*signs) * P.inv())
    if zw_integral(Sx):
        n_int += 1
        sign_invs[signs] = Sx
check("C4.1 all eight spectral-sign involutions of V_1 are Z[omega]-integral (v590 rigidity)",
      n_int == 8, "%d/8" % n_int)

want_S0 = tuple(1 if order[i] == 0 else -1 for i in range(3))
want_A = tuple(-1 if order[i] == 1 else 1 for i in range(3))
want_B = tuple(-1 if order[i] == 2 else 1 for i in range(3))
S0c = sign_invs.get(want_S0)
Ac = sign_invs.get(want_A)
Bc = sign_invs.get(want_B)
ok_S0 = (S0c is not None and sp.simplify(S0c * S0c) == I3
         and sp.simplify(S0c * V1 - V1 * S0c) == sp.zeros(3, 3)
         and sp.simplify(S0c.trace() + 1) == 0)
check("C4.2 curve-side S_0 (two-demand selection): integral involution, [S0,V] = 0, trace -1", ok_S0)
check("C4.3 Klein closure on the curve: A, B integral with A B = S_0",
      Ac is not None and Bc is not None
      and sp.simplify(Ac * Bc - S0c) == sp.zeros(3, 3))

# ---------------------------------------------------------------- C5
print("=" * 72)
print("C5: honest opens (typed, not claimed)")
print("=" * 72)

K = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        K[i, j] = sp.simplify(sp.trace(Jinv * words[i].conjugate().T * J * words[j]))
herm = sp.simplify(K - K.conjugate().T) == sp.zeros(7, 7)
Kn = np.array(sp.N(K).tolist(), dtype=complex)
ev = np.linalg.eigvalsh(Kn)
pos = sum(1 for e in ev if e > 1e-9)
neg = sum(1 for e in ev if e < -1e-9)
zer = 7 - pos - neg
check("C5.1 naive J-word Gram hermitian with inertia (3,2,2) -- NOT the v572 (4,0,3); "
      "Weil-twisted comparison stays open", herm and (pos, neg, zer) == (3, 2, 2),
      "inertia (+%d, -%d, 0:%d)" % (pos, neg, zer))

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: EQUIVARIANT-DUAL-LANDED -- the J-projector presentation is")
    print("D4-equivariant by construction, realizes the DUAL parabolic exactly,")
    print("and carries the v590 Klein group integrally; the mark choice is the")
    print("winding choice; RP/Hodge comparison and seam identification stay open.")
else:
    print("SOME CHECKS FAILED")
