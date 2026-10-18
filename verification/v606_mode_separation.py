#!/usr/bin/env python3
"""v606 -- QGEO.MODESEP.01: the mode-separation round -- the infinity torsion
separates the three V-eigenlines (pure torsion, pairwise distinct classes:
the selection carrier the real structure could not provide), and the cubic
field of c is honestly non-abelian (the arithmetic-identity route closed).

Round 10 of the QGEO cover program (after v605).  Executes the follow-up
slate "zero-mode selection via infinity torsion / arithmetic identity of c":

  (M1) ALL THREE MODES ARE PURE TORSION AT INFINITY [E]: the three
       eigenlines of the sheet operator V (eigenvalues 0, 1, 2), lifted to
       the unreduced integral module along the unique intertwiner, all have
       ZERO free part in coker(1 - T_inf) = Z^2 + (Z/3)^3 -- like the seam
       (v605), the zero mode and the top mode are pure 3-torsion classes at
       infinity.

  (M2) THE INFINITY TORSION SEPARATES THE MODES [E]: the three classes are
       PAIRWISE DISTINCT elements of (Z/3)^3 (in a fixed Smith frame:
       (2,0,2), (2,2,0), (1,2,0) for V = 0, 1, 2) -- and distinctness is
       frame-invariant.  This is the separation the real structure could
       NOT provide (only the seam line is R-fixed; the 0/2 lines are
       neither R-fixed nor R-swapped, v605-followup): the infinity-cusp
       torsion is a SELECTION CARRIER that distinguishes the zero mode
       from the top mode.  Honest scope [C]: the specific coordinate
       triples are Smith-frame-dependent; a canonical rule singling out
       the zero mode's class (the "+1" of the v590 demand) from the
       structure alone is the named remaining step.

  (M3) THE CUBIC FIELD OF c IS NOT ABELIAN [X, honest negative]: the
       canonical cubic invariant of the translator element
       (char(7 Gamma(c) c) = y^3 + 3y^2 + 6y - 1, integer monic,
       irreducible) has discriminant -783 = -3^3 x 29, NOT a square --
       Galois group S_3, hence NOT abelian, hence NO cyclotomic-subfield
       identity for c by Kronecker-Weber.  The arithmetic-identity route
       for c is closed; its geometric identity stays the named open.

All checks exact (sympy).  Verdict enums (frozen): MODES-SEPARATED (all),
MODES-SEPARATED-FAILS, MIXED.

FIREWALL: GATE.QGEO does not move; no marker changes.  The canonical
selection rule (which torsion class gets the "+1" of the v590 demand) and
the geometric identity of c stay typed open.

PROVENANCE: discovery probe mode_separation_probe.py (2026-08-01, 7/7,
verdict MODES-SEPARATED).  Python-only, counted per GATE.WOLFRAM.02.
"""

import sympy as sp

t = sp.symbols("t")
x = sp.symbols("x")
y = sp.symbols("y")
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
GJ = [sp.simplify((I3 - T[k]) * J.inv() * (I3 - T[k]).conjugate().T * J) for k in range(4)]
V1J = sp.simplify(I3 + GJ[3] - GJ[1] * GJ[0])

Su = [sp.simplify(burau_unred(i).subs({t: OMEGA})) for i in (1, 2, 3)]
ru = sp.simplify(Su[0] * Su[1] * Su[2])

# unique intertwiner reduced -> unreduced
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
check("M0.1 the reduced module embeds uniquely (rank-3 intertwiner, 1-param family)",
      len(sol) == 1 and len(fs) == 1 and ph.rank() == 3)

# infinity cokernel Smith machinery
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
    freep = []
    torp = []
    for i in range(8):
        d = D8[i, i]
        if d == 0:
            freep.append(sp.nsimplify(yv[i]))
        elif abs(d) == 3:
            torp.append(int(sp.Mod(yv[i], 3)))
    return freep, torp


# ---------------------------------------------------------------- M1 + M2
print("=" * 72)
print("M1/M2: the infinity-torsion classes of the three V-eigenlines")
print("=" * 72)

classes = {}
all_pure = True
for lam in (0, 1, 2):
    evec = (V1J - lam * I3).nullspace()[0]
    lift = sp.simplify(ph * evec)
    fr, tor = coker_class(lift)
    classes[lam] = tuple(tor)
    if any(f != 0 for f in fr):
        all_pure = False
    print("  V = %d: free %s | torsion %s" % (lam, fr, tor))
check("M1.1 all three eigenline lifts are PURE torsion (zero free part)", all_pure)
check("M1.2 fixed-frame signatures (2,0,2), (2,2,0), (1,2,0) for V = 0, 1, 2",
      classes[0] == (2, 0, 2) and classes[1] == (2, 2, 0) and classes[2] == (1, 2, 0))
check("M2.1 the classes are PAIRWISE DISTINCT (frame-invariant): the infinity torsion "
      "separates zero mode, seam and top mode",
      len({classes[0], classes[1], classes[2]}) == 3)
check("M2.2 none of the classes is trivial (all three modes are torsion-visible)",
      all(any(c != 0 for c in classes[lam]) for lam in (0, 1, 2)))

# ---------------------------------------------------------------- M3
print("=" * 72)
print("M3: the cubic field of c is not abelian [honest negative]")
print("=" * 72)

pc = y ** 3 + 3 * y ** 2 + 6 * y - 1
check("M3.1 char(7 Gamma(c) c) = y^3 + 3y^2 + 6y - 1 is irreducible over Q",
      sp.Poly(pc, y).is_irreducible)
disc = sp.discriminant(pc, y)
check("M3.2 discriminant -783 = -3^3 x 29, NOT a square: Galois S_3, not abelian -- "
      "no cyclotomic identity for c (Kronecker-Weber)",
      disc == -783 and not sp.sqrt(sp.Abs(disc)).is_integer,
      "disc = %s" % disc)

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: MODES-SEPARATED -- the infinity torsion separates the three")
    print("V-eigenlines (pure torsion, pairwise distinct classes); the canonical")
    print("selection rule stays open; the arithmetic-identity route for c is")
    print("closed (S_3, not abelian).")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
