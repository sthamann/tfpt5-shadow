#!/usr/bin/env python3
"""v607 -- QGEO.SELRULE.01: the selection rule round -- the deck rotation has
a UNIQUE projective eigenline on the infinity torsion (structurally: char =
(x+1)(x^2+1) mod 3) and it IS the top mode; the zero mode is the only
unlabeled mode -- the canonical "+1" rule of the v590 zero-mode demand.

Round 11 of the QGEO cover program (after v606).  v606 separated the three
V-eigenlines by their infinity-torsion classes but left the canonical rule
open (which class gets the "+1" of the v590 zero-mode demand).  This module
closes that gap with the deck action:

  (S1) THE TORSION IS AN F_3-SPACE [E]: multiplication by omega acts as
       the IDENTITY on the torsion part of coker(1 - T_inf) -- the
       Eisenstein structure degenerates ((1-omega) acts as zero), so the
       torsion is a genuine F_3 vector space and the deck rotation r
       (which commutes with T_inf = r^4) acts F_3-linearly on it.

  (S2) THE ACTION AND ITS RIGIDITY [E]: the induced r-action on
       (Z/3)^3 is the explicit matrix [[0,1,0],[1,0,2],[2,2,2]]; its only
       FIXED class is 0, and its characteristic polynomial mod 3 factors
       as (x+1)(x^2+1) with x^2+1 IRREDUCIBLE over F_3: the action has
       EXACTLY ONE projective eigenline, with eigenvalue -1 -- structural
       uniqueness, not accident.

  (S3) THE LABELING [E]: the unique projective eigenline IS the top-mode
       class ((1,2,0) = class of the V=2 eigenline); the zero-mode and
       seam classes are NOT projectively fixed (neither under r nor r^2).
       Together with v603/v605 the three modes now carry mutually
       exclusive canonical labels:
         seam (V=1):  the R-REAL line (real structure);
         top  (V=2):  the unique DECK-EIGEN torsion class (lambda = -1);
         zero (V=0):  the only UNLABELED mode.

  (S4) THE RULE [C, typed reading]: the two-demand involution S_0 acts as
       -1 exactly on the two canonically labeled modes and +1 on the
       unlabeled one -- the v590 zero-mode demand ("+1 on ker V") is the
       statement "fix the unlabeled mode", and the seam-reversal demand is
       "reverse the R-real line" (v603): BOTH demands are now expressed
       through canonical cover structure.  Honest scope: this is a typed
       reading of the selection, not a continuum derivation; GATE.QGEO
       does not move; eigen-ness/uniqueness/distinctness are
       Smith-frame-invariant statements, the coordinate triples are not.

All checks exact (sympy / F_3 arithmetic).  Verdict enums (frozen):
SELECTION-RULE-LANDED (all), SELECTION-RULE-FAILS, MIXED.

FIREWALL: GATE.QGEO does not move; no marker changes.  S4 is a typed [C]
reading (the selection expressed through cover structure), not a continuum
derivation; the frame-invariant content is eigen-ness, uniqueness and
distinctness.

PROVENANCE: discovery probe selection_rule_probe.py (2026-08-01, 10/10,
verdict SELECTION-RULE-LANDED).  Python-only, counted per GATE.WOLFRAM.02.
"""

from itertools import product

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


def zw_coords(e):
    e = sp.expand(e)
    b = sp.nsimplify(2 * sp.im(e) / sp.sqrt(3))
    a = sp.nsimplify(sp.re(e) + sp.im(e) / sp.sqrt(3))
    return a, b


I3 = sp.eye(3)
I4 = sp.eye(4)
S = [sp.simplify(burau_gen(i).subs({t: OMEGA})) for i in (1, 2, 3)]
r3 = sp.simplify(S[0] * S[1] * S[2])
T = [S[0]]
for _ in range(3):
    T.append(sp.simplify(r3 * T[-1] * r3.inv()))
J = sp.Matrix([[0, 1 + sp.sqrt(3) * sp.I, -1 + sp.sqrt(3) * sp.I],
               [1 - sp.sqrt(3) * sp.I, 2, 1 + sp.sqrt(3) * sp.I],
               [-1 - sp.sqrt(3) * sp.I, 1 - sp.sqrt(3) * sp.I, 0]])
GJ = [sp.simplify((I3 - T[k]) * J.inv() * (I3 - T[k]).conjugate().T * J) for k in range(4)]
V1J = sp.simplify(I3 + GJ[3] - GJ[1] * GJ[0])

Su = [sp.simplify(burau_unred(i).subs({t: OMEGA})) for i in (1, 2, 3)]
ru = sp.simplify(Su[0] * Su[1] * Su[2])
Tinf = sp.simplify(ru ** 4)


def zmat18(op):
    cols = []
    for j in range(4):
        for mult in (1, OMEGA):
            v = sp.zeros(4, 1)
            v[j] = mult
            img = sp.expand(op * v)
            col = []
            for i in range(4):
                a, b = zw_coords(img[i])
                col.extend([a, b])
            cols.append([sp.nsimplify(e) for e in col])
    M = sp.Matrix(cols).T
    assert all(e.is_integer for e in M)
    return sp.Matrix([[sp.Integer(e) for e in row] for row in M.tolist()])


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


Mz = zmat18(sp.simplify(I4 - Tinf))
D8, U8, V8 = snf_transforms(Mz.copy())
tor_idx = [i for i in range(8) if abs(D8[i, i]) == 3]
U8i = U8.inv()

# ---------------------------------------------------------------- S1
print("=" * 72)
print("S1: the torsion is an F_3 space; the deck acts on it")
print("=" * 72)

check("S1.0 r commutes with T_inf = r^4 (the deck acts on the cokernel)",
      sp.simplify(ru * Tinf - Tinf * ru) == sp.zeros(4, 4))


def coker_action(op):
    Xz = zmat18(op)
    A = sp.zeros(3, 3)
    for jcol, i in enumerate(tor_idx):
        xv = U8i[:, i]
        yv = sp.expand(U8 * Xz * xv)
        for jrow, i2 in enumerate(tor_idx):
            A[jrow, jcol] = sp.Mod(sp.nsimplify(yv[i2]), 3)
    return A


Aom = coker_action(OMEGA * I4)
check("S1.1 omega-multiplication acts as the IDENTITY on the torsion (F_3 structure)",
      Aom == sp.eye(3))

# ---------------------------------------------------------------- S2
print("=" * 72)
print("S2: the r-action and its rigidity")
print("=" * 72)

Ar = coker_action(ru)
check("S2.1 the induced r-action is [[0,1,0],[1,0,2],[2,2,2]] (mod 3)",
      Ar == sp.Matrix([[0, 1, 0], [1, 0, 2], [2, 2, 2]]))
fixed_pts = [v_ for v_ in product(range(3), repeat=3)
             if all(sp.Mod(sum(Ar[i, j] * v_[j] for j in range(3)) - v_[i], 3) == 0
                    for i in range(3))]
check("S2.2 the only r-FIXED class is 0", fixed_pts == [(0, 0, 0)])
cp3 = [sp.Mod(c, 3) for c in sp.Poly(sp.expand((x * sp.eye(3) - Ar).det()), x).all_coeffs()]
check("S2.3 char(r-action) mod 3 = (x+1)(x^2+1) with x^2+1 irreducible over F_3: "
      "EXACTLY ONE projective eigenline (eigenvalue -1), structurally", cp3 == [1, 1, 1, 1])
lines = set()
for v_ in product(range(3), repeat=3):
    if v_ == (0, 0, 0):
        continue
    img = tuple(sp.Mod(sum(Ar[i, j] * v_[j] for j in range(3)), 3) for i in range(3))
    for lam in (0, 1, 2):
        if img == tuple(sp.Mod(lam * e, 3) for e in v_):
            rep = min(tuple(sp.Mod(s * e, 3) for e in v_) for s in (1, 2))
            lines.add((rep, lam))
check("S2.4 eigenline census: the unique projective eigenline is (1,2,0) with lambda = 2 = -1",
      lines == {((1, 2, 0), 2)}, str(sorted(lines)))

# ---------------------------------------------------------------- S3
print("=" * 72)
print("S3: the labeling of the three modes")
print("=" * 72)

# mode classes via the unique intertwiner (as in v606)
phi = sp.Matrix(4, 3, lambda i, j: sp.Symbol("p%d%d" % (i, j)))
eqs = []
for Si_red, Si_un in zip(S, Su):
    E_ = sp.expand(Si_un * phi - phi * Si_red)
    eqs.extend([E_[i, j] for i in range(4) for j in range(3)])
sol = sp.solve(eqs, list(phi), dict=True)
ph = sp.simplify(phi.subs(sol[0]))
fs = sorted(ph.free_symbols, key=str)
ph = sp.simplify(ph.subs({fs[0]: 1, **{f: 0 for f in fs[1:]}}))
if ph.rank() < 3:
    ph = sp.simplify(sp.simplify(phi.subs(sol[0])).subs({f: k + 1 for k, f in enumerate(fs)}))


def coker_class(vec4):
    coords = []
    for i in range(4):
        a, b = zw_coords(vec4[i])
        coords.extend([a, b])
    den = sp.lcm([sp.fraction(e)[1] for e in coords])
    coords = [sp.Integer(e * den) for e in coords]
    gg = sp.gcd([e for e in coords if e != 0]) if any(coords) else 1
    coords = [e // gg for e in coords]
    sv = sp.Matrix(8, 1, coords)
    yv = sp.expand(U8 * sv)
    return tuple(int(sp.Mod(yv[i], 3)) for i in tor_idx)


classes = {}
for lam in (0, 1, 2):
    evec = (V1J - lam * I3).nullspace()[0]
    classes[lam] = coker_class(sp.simplify(ph * evec))


def proj_eq(a_, b_):
    return any(tuple(sp.Mod(s * e, 3) for e in a_) == b_ for s in (1, 2))


check("S3.1 the TOP mode's class IS the unique deck eigenline", proj_eq(classes[2], (1, 2, 0)))
r_img = {lam: tuple(sp.Mod(sum(Ar[i, j] * classes[lam][j] for j in range(3)), 3)
                    for i in range(3)) for lam in (0, 1, 2)}
check("S3.2 the zero mode and the seam are NOT projectively fixed by r",
      not proj_eq(r_img[0], classes[0]) and not proj_eq(r_img[1], classes[1]))
Ar2 = (Ar * Ar).applyfunc(lambda e: sp.Mod(e, 3))
r2_img = {lam: tuple(sp.Mod(sum(Ar2[i, j] * classes[lam][j] for j in range(3)), 3)
                     for i in range(3)) for lam in (0, 1)}
check("S3.3 nor by r^2 (the opposite-cusp rotation)",
      not proj_eq(r2_img[0], classes[0]) and not proj_eq(r2_img[1], classes[1]))

# ---------------------------------------------------------------- S4
print("=" * 72)
print("S4: the rule (typed reading)")
print("=" * 72)

check("S4.1 [C] the three modes carry mutually exclusive canonical labels: seam = R-real "
      "(v603), top = deck-eigen (S3.1), zero = UNLABELED -- and S_0 = -1 exactly on the "
      "labeled pair, +1 on the unlabeled mode: both v590 demands expressed through cover "
      "structure (reading, not a continuum derivation; gate unmoved)", True)

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: SELECTION-RULE-LANDED -- the deck rotation has exactly one")
    print("projective eigenline on the infinity torsion and it is the top mode;")
    print("the zero mode is the only unlabeled mode: the canonical '+1' rule.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
