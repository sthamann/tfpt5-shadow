#!/usr/bin/env python3
"""v654 -- E8.ST31D8.01: the ST31 degree-8 round -- the last census, plus
the unified d/4-theorem.

Predecessors (read-only):
  st31_structure_probe.py  G31 = <60 order-2 unitary reflections> on the
    240 E8 roots, |G31| = 46080, degrees (8,12,20,24), Springer regular
    elements of orders 8/12/20/24 with centralizers 192/288/20/24; the
    compiler clock c = J o sigma (order 12, sigma = c^4, J = c^9) is
    NOT regular (census 19 x 12 + 3 x 4, |C(c)| = 72).
  st31_degree24_probe.py   methodology: witness construction, exact
    charpolys via Faddeev-LeVerrier over Q(i), center relations
    w^6 = +-J (24), u^5 = +-J (20), parity kill for c = w^2.

MAIN FINDINGS of this probe (honesty first):

(1) FREE != REGULAR at degrees 8 and 12.  The task expectation "free
    census {8:30} => regular, |C| = 192" is WRONG: of the 4800 free
    order-8 elements only 480 (= 2 classes of 240, |C| = 192) are
    Springer-regular with chi = (x^2 +- i)^2 and x^2 = +-i Id; the
    other 4320 (3 classes, |C| = 32) have chi = Phi_8 = x^4 + 1
    (SIMPLE primitive spectrum), squares NON-central, no regular
    eigenvector.  Same at d = 12 (320 regular vs 960 free non-regular
    with chi = Phi_12).  At d = 20, 24 free <=> regular (phi(d) = 8:
    a quartic must be one Q(i)-factor of Phi_d; at phi(d) = 4 the
    non-Springer option chi = Phi_d exists and is realized).

(2) THE UNIFIED THEOREM (exact, class-exhaustive): every Springer-
    regular d-clock (d in {8,12,20,24}) contains the mu4 center as
    its d/4-th power: x^(d/4) in {J, J^3}, i.e. mu4 = <x^(d/4)>,
    with x^(d/4) a GENERATOR (+-i Id, never +-1) -- uniform reason:
    ALL exponents (7,11,19,23) of G31 are = 3 mod 4.  Regular
    classes per degree: exactly 2 (a Galois pair, one with sign J,
    one with J^3; sizes 240/160/2304/1920, |C| = 192/288/20/24).
    On the 60 lines every regular d-clock reads as a FREE d/4-clock
    {d/4 : 240/d}.

(3) THE CONVERSE AND THE COMPILER-CLOCK PUNCHLINE: at d = 8, 20, 24
    the converse holds: x^(d/4) central => regular.  At d = 12 there
    are EXACTLY two more classes with central cube: the class of the
    compiler clock c = J o sigma and its Galois twin <c^-1> (2 x 640,
    |C| = 72, census {12:19, 4:3}) -- c^3 = J^3 = -i Id exactly
    (sigma^3 = 1, [J,sigma] = 0), even though c is NOT regular.
    chi_c = (x - i)^2 (x^2 + i x - 1): the compiler clock carries
    HALF of the regular-12 Springer block (x^2 + i x - 1)^2 plus a
    doubled eigenvalue i; all eigenvalues satisfy lambda^3 = -i,
    which is exactly why its cube is central.  So the compiler-clock
    classes are the ONLY non-regular clocks in all of G31 whose
    d/4-th power generates the center.

(4) CONTROLS: full order census (max order 24); free-acting orders
    = exactly the divisors > 1 of the degrees; {8,12,20,24} are NOT
    the divisibility-maximal free orders (that is {20,24}) but the
    free orders divisible by 4 above 4; at order 4 freeness does not
    even imply x central (510 non-central free 4-elements, none
    regular).

Cycle censuses are S_240 class invariants; permutation identities and
Q(i) matrix identities are exact; Springer regularity is tested
numerically (eigenvector avoiding all 60 hyperplanes) on one
representative per conjugacy class.

FIREWALL: no marker moves; the 48 = seam sites equality stays a typed
observation (E8.ST31DEG.01); writes nothing.  Python-only (exact
Fraction/Z[i] arithmetic), counted per GATE.WOLFRAM.02.

PROVENANCE: discovery probe st31_degree8_probe.py (2026-08-02, 30/30,
ALL CHECKS PASSED).
"""

import itertools
import time
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from math import gcd, lcm

import numpy as np

T0 = time.time()
CHECKS = []
N240 = 240


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ================================================================ S0 roots
section("S0: roots, J, sigma, c, lines, reflections, G31, classes")

_roots = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        _roots.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        _roots.append(v)
RD = np.array(sorted(_roots), dtype=np.int64)
ridx = {tuple(int(a) for a in RD[i]): i for i in range(N240)}
check("S0.1 240 doubled-integer E8 roots reconstructed",
      RD.shape == (240, 8))


def J_vec(x):
    out = np.empty_like(x)
    out[0::2] = -x[1::2]
    out[1::2] = x[0::2]
    return out


def perm_from_map(f):
    return np.array([ridx[tuple(int(a) for a in f(RD[i]))]
                     for i in range(N240)], dtype=np.int16)


Jperm = perm_from_map(J_vec)
SIGMA_IDX = [4, 5, 0, 1, 2, 3, 6, 7]
sigperm = perm_from_map(lambda x: x[SIGMA_IDX])
IDP = np.arange(N240, dtype=np.int16)


def comp(p, q):
    """(p o q)[i] = p[q[i]] (apply q first, then p)."""
    return p[q]


def pinv(p):
    return np.argsort(p).astype(np.int16)


def census_order(p):
    pl = p.tolist()
    seen = bytearray(N240)
    cen = {}
    for s in range(N240):
        if seen[s]:
            continue
        ln, j = 0, s
        while not seen[j]:
            seen[j] = 1
            j = pl[j]
            ln += 1
        cen[ln] = cen.get(ln, 0) + 1
    o = 1
    for L in cen:
        o = lcm(o, L)
    return tuple(sorted(cen.items())), o


def perm_power(p, k):
    r = IDP
    b = p
    while k:
        if k & 1:
            r = comp(b, r)
        b = comp(b, b)
        k >>= 1
    return r


cperm = comp(Jperm, sigperm)
J2 = comp(Jperm, Jperm)
J3 = comp(J2, Jperm)
cen_c, ord_c = census_order(cperm)
check("S0.2 compiler clock c = J o sigma: order %d, root census %s"
      % (ord_c, dict(cen_c)), ord_c == 12 and dict(cen_c) == {4: 3, 12: 19})

line_of = np.full(N240, -1, dtype=np.int32)
line_reps = []
for i in range(N240):
    if line_of[i] >= 0:
        continue
    orb = [i, int(Jperm[i]), int(Jperm[Jperm[i]]),
           int(Jperm[Jperm[Jperm[i]]])]
    for j in orb:
        line_of[j] = len(line_reps)
    line_reps.append(i)
check("S0.3 60 J-lines", len(line_reps) == 60)
LREPS = np.array(line_reps, dtype=np.int64)


def line_census(p):
    lp = line_of[np.asarray(p)[LREPS]]
    seen = bytearray(60)
    cen = {}
    for s in range(60):
        if seen[s]:
            continue
        ln, j = 0, s
        while not seen[j]:
            seen[j] = 1
            j = int(lp[j])
            ln += 1
        cen[ln] = cen.get(ln, 0) + 1
    return tuple(sorted(cen.items()))


JRD = np.array([J_vec(RD[i]) for i in range(N240)], dtype=np.int64)


def herm4_rowvec(v_i):
    return RD @ RD[v_i], RD @ JRD[v_i]


refl_perms = []
for a in range(60):
    vi = line_reps[a]
    re4, im4 = herm4_rowvec(vi)
    re, im = re4 // 4, im4 // 4
    Y = RD - re[:, None] * RD[vi][None, :] - im[:, None] * JRD[vi][None, :]
    refl_perms.append(np.array([ridx[tuple(int(t) for t in Y[i])]
                                for i in range(N240)], dtype=np.int16))
check("S0.4 60 distinct order-2 reflections preserve the roots",
      len({p.tobytes() for p in refl_perms}) == 60
      and all(np.array_equal(comp(p, p), IDP) for p in refl_perms))

t = time.time()
Gset = {IDP.tobytes(): IDP}
frontier = [IDP]
while frontier:
    nxt = []
    for p in frontier:
        for g in refl_perms:
            q = p[g]
            b = q.tobytes()
            if b not in Gset:
                Gset[b] = q
                nxt.append(q)
    frontier = nxt
check("S0.5 |G31| = %d (BFS, %.1f s); J, sigma, c in G31"
      % (len(Gset), time.time() - t),
      len(Gset) == 46080 and Jperm.tobytes() in Gset
      and sigperm.tobytes() in Gset and cperm.tobytes() in Gset)
Eall = np.stack(list(Gset.values()))
byte2row = {Eall[i].tobytes(): i for i in range(len(Eall))}


def centralizer_order(x):
    x = np.asarray(x, dtype=np.int16)
    return int(np.sum(np.all(Eall[:, x] == x[Eall], axis=1)))


t = time.time()
cens_all = []
ord_all = np.empty(len(Eall), dtype=np.int32)
for i in range(len(Eall)):
    cen, o = census_order(Eall[i])
    cens_all.append(cen)
    ord_all[i] = o
spec = Counter(ord_all.tolist())
print("      order spectrum (%.1f s): %s"
      % (time.time() - t, dict(sorted(spec.items()))))
check("S0.6 order/census pass over all 46080 elements (max order %d)"
      % max(spec), sum(spec.values()) == 46080 and max(spec) == 24)

# conjugacy classes (reflections are involutions and generate G31,
# so conjugating by all 60 reflections sweeps out whole classes)
t = time.time()
class_id = np.full(len(Eall), -1, dtype=np.int32)
class_reps = []
for i in range(len(Eall)):
    if class_id[i] >= 0:
        continue
    cid = len(class_reps)
    class_reps.append(i)
    class_id[i] = cid
    stack = [Eall[i]]
    while stack:
        x = stack.pop()
        for g in refl_perms:
            y = g[x[g]]
            r = byte2row[y.tobytes()]
            if class_id[r] < 0:
                class_id[r] = cid
                stack.append(y)
n_classes = len(class_reps)
class_sizes = Counter(class_id.tolist())
check("S0.7 conjugacy classes of G31: %d (%.1f s), sizes sum to 46080"
      % (n_classes, time.time() - t),
      sum(class_sizes.values()) == 46080)

# ==================================================== exact Q(i) algebra
GZ = (Fr(0), Fr(0))
G1 = (Fr(1), Fr(0))
GI = (Fr(0), Fr(1))
GmI = (Fr(0), Fr(-1))
Gm1 = (Fr(-1), Fr(0))


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gdiv(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / d,
            (a[1] * b[0] - a[0] * b[1]) / d)


def is0(a):
    return a[0] == 0 and a[1] == 0


def gfmt(a):
    if a[1] == 0:
        return str(a[0])
    if a[0] == 0:
        return "%si" % ("" if a[1] == 1 else "-" if a[1] == -1 else a[1])
    return "(%s%+si)" % (a[0], a[1])


def zvec(i):
    r = RD[i]
    return [(Fr(int(r[2 * j]), 2), Fr(int(r[2 * j + 1]), 2))
            for j in range(4)]


def mat_mul(A, B):
    return [[
        (sum(gmul(A[r][k], B[k][c])[0] for k in range(4)),
         sum(gmul(A[r][k], B[k][c])[1] for k in range(4)))
        for c in range(4)] for r in range(4)]


def mat_inv(A):
    M = [[A[r][c] for c in range(4)] + [G1 if r == c else GZ
                                        for c in range(4)]
         for r in range(4)]
    for col in range(4):
        piv = next(r for r in range(col, 4) if not is0(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [gdiv(x, pv) for x in M[col]]
        for r in range(4):
            if r != col and not is0(M[r][col]):
                f = M[r][col]
                M[r] = [gsub(x, gmul(f, y))
                        for x, y in zip(M[r], M[col])]
    return [[M[r][4 + c] for c in range(4)] for r in range(4)]


basis_idx = []
ech = []
for i in range(N240):
    vv = zvec(i)[:]
    for r in ech:
        pc = next(c for c in range(4) if not is0(r[c]))
        if not is0(vv[pc]):
            f = gdiv(vv[pc], r[pc])
            vv = [gsub(vv[c], gmul(f, r[c])) for c in range(4)]
    if any(not is0(x) for x in vv):
        ech.append(vv)
        basis_idx.append(i)
    if len(basis_idx) == 4:
        break
BMAT = [[zvec(basis_idx[c])[r] for c in range(4)] for r in range(4)]
BINV = mat_inv(BMAT)


def matrix_of(p):
    img = [[zvec(int(p[basis_idx[c]]))[r] for c in range(4)]
           for r in range(4)]
    return mat_mul(img, BINV)


def verify_matrix(M, p):
    for i in range(N240):
        z = zvec(i)
        w = zvec(int(p[i]))
        for r in range(4):
            acc = GZ
            for k in range(4):
                acc = gadd(acc, gmul(M[r][k], z[k]))
            if acc != w[r]:
                return False
    return True


def charpoly(M):
    """Faddeev-LeVerrier: chi = x^4 + c1 x^3 + c2 x^2 + c3 x + c4."""
    def tr(A):
        return (sum(A[k][k][0] for k in range(4)),
                sum(A[k][k][1] for k in range(4)))

    def madd_scal(A, s):
        return [[gadd(A[r][c], s) if r == c else A[r][c]
                 for c in range(4)] for r in range(4)]

    cs = []
    Mk = M
    for k in range(1, 5):
        tk = tr(Mk)
        ck = (-tk[0] / k, -tk[1] / k)
        cs.append(ck)
        if k < 4:
            Mk = mat_mul(M, madd_scal(Mk, ck))
    return cs


def chi_asc(M):
    cs = charpoly(M)
    return [cs[3], cs[2], cs[1], cs[0], G1]


def mat_pow(M, k):
    R = [[G1 if r == c else GZ for c in range(4)] for r in range(4)]
    for _ in range(k):
        R = mat_mul(R, M)
    return R


def is_scalar(M):
    s = M[0][0]
    ok = all(M[r][c] == (s if r == c else GZ)
             for r in range(4) for c in range(4))
    return (s if ok else None)


MJ = matrix_of(Jperm)
check("S0.8 exact matrix machinery: M(J) = i * Id (verified on all 240 "
      "roots: %s)" % verify_matrix(MJ, Jperm),
      all(MJ[r][c] == (GI if r == c else GZ)
          for r in range(4) for c in range(4)) and verify_matrix(MJ, Jperm))

# ------------------------------ exact polynomial toolkit over Q(i)


def pstrip(P):
    P = list(P)
    while len(P) > 1 and is0(P[-1]):
        P.pop()
    return P


def peq(A, B):
    return pstrip(A) == pstrip(B)


def pmul(A, B):
    out = [GZ] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if is0(a):
            continue
        for j, b in enumerate(B):
            out[i + j] = gadd(out[i + j], gmul(a, b))
    return out


def ppow(P, k):
    R = [G1]
    for _ in range(k):
        R = pmul(R, P)
    return R


def pdivmod(A, B):
    """A = q*B + r with B MONIC; exact over Q(i)."""
    A = list(A)
    B = pstrip(B)
    dB = len(B) - 1
    assert B[-1] == G1
    q = [GZ] * max(1, len(A) - dB)
    for d in range(len(A) - 1, dB - 1, -1):
        cd = A[d]
        if is0(cd):
            continue
        q[d - dB] = cd
        for k in range(dB + 1):
            A[d - dB + k] = gsub(A[d - dB + k], gmul(cd, B[k]))
    return pstrip(q), pstrip(A[:dB] or [GZ])


def pconj(P):
    return [(c[0], -c[1]) for c in P]


def pfmt(P):
    P = pstrip(P)
    terms = []
    for k in range(len(P) - 1, -1, -1):
        c = P[k]
        if is0(c):
            continue
        if k == 0:
            terms.append(gfmt(c))
        else:
            xs = "x" if k == 1 else "x^%d" % k
            terms.append(xs if c == G1 else "%s*%s" % (gfmt(c), xs))
    return " + ".join(terms) if terms else "0"


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


_CYC = {}


def cyclotomic(d):
    if d in _CYC:
        return _CYC[d]
    P = [GZ] * (d + 1)
    P[d] = G1
    P[0] = Gm1
    for e in divisors(d):
        if e < d:
            P, r = pdivmod(P, cyclotomic(e))
            assert peq(r, [GZ])
    _CYC[d] = P
    return P


def phi_euler(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


known = {8: [G1, GZ, GZ, GZ, G1],                       # x^4 + 1
         12: [G1, GZ, Gm1, GZ, G1],                     # x^4 - x^2 + 1
         20: [G1, GZ, Gm1, GZ, G1, GZ, Gm1, GZ, G1],    # x^8-x^6+x^4-x^2+1
         24: [G1, GZ, GZ, GZ, Gm1, GZ, GZ, GZ, G1]}     # x^8 - x^4 + 1
check("S0.9 polynomial toolkit control: Phi_8, Phi_12, Phi_20, Phi_24 "
      "match their known forms",
      all(peq(cyclotomic(d), known[d]) for d in (8, 12, 20, 24)))

# numeric machinery for Springer-regularity (some eigenvector to a
# primitive-d eigenvalue avoids all 60 reflection hyperplanes)
Rc = (RD[:, 0::2] + 1j * RD[:, 1::2]) / 2.0
LINESC = np.conj(Rc[line_reps])
RNG = np.random.default_rng(123)


def mat_c(M):
    return np.array([[float(c[0]) + 1j * float(c[1]) for c in row]
                     for row in M])


def is_regular_numeric(Mc, d):
    lam_all = np.linalg.eigvals(Mc)
    for k in range(1, d):
        if gcd(k, d) != 1:
            continue
        z = np.exp(2j * np.pi * k / d)
        if np.min(np.abs(lam_all - z)) > 1e-6:
            continue
        A = Mc - z * np.eye(4)
        _, sv, vh = np.linalg.svd(A)
        dim = int(np.sum(sv < 1e-8))
        if dim == 0:
            continue
        Bas = vh[4 - dim:].conj().T
        for _ in range(60):
            e = Bas @ (RNG.normal(size=dim) + 1j * RNG.normal(size=dim))
            if np.min(np.abs(LINESC @ e)) > 1e-6 * np.linalg.norm(e):
                return True
    return False


DEGS = [8, 12, 20, 24]
EXP_CENT = {d: int(np.prod([e for e in DEGS if e % d == 0])) for d in DEGS}
Jb, J2b, J3b, IDb = (Jperm.tobytes(), J2.tobytes(), J3.tobytes(),
                     IDP.tobytes())


def classify_center(p):
    b = p.tobytes()
    return ("J" if b == Jb else "J^3" if b == J3b
            else "-1" if b == J2b else "1" if b == IDb else "noncentral")


# =============================================================== S1
section("S1: the degree-8 census -- free vs regular, the 8-clock v")

rows8 = np.where(ord_all == 8)[0]
cen8 = Counter(cens_all[i] for i in rows8)
print("      order-8 elements: %d; distinct root censuses:" % len(rows8))
for cen, cnt in sorted(cen8.items()):
    print("        %-28s x %d" % (dict(cen), cnt))
FREE8 = ((8, 30),)
free8_rows = [i for i in rows8 if cens_all[i] == FREE8]
reg8_rows = [i for i in rows8
             if classify_center(perm_power(Eall[i], 2)) in ("J", "J^3")]
check("S1.1 order-8 landscape: %d elements, %d with FREE census {8:30}, "
      "but only %d with x^2 in {J, J^3} -- NOT all order-8 elements "
      "are free, and NOT all free ones are regular (the task "
      "expectation 'free => |C| = 192' FAILS at d = 8)"
      % (len(rows8), len(free8_rows), len(reg8_rows)),
      len(rows8) == 10560 and len(free8_rows) == 4800
      and len(reg8_rows) == 480)

cls8 = 46080 // EXP_CENT[8]
vrow = reg8_rows[0]
v = Eall[vrow]
cv = centralizer_order(v)
check("S1.2 REGULAR witness v (taken from the x^2-central set): root "
      "census %s (free), |C_G31(v)| = %d = %d = product of the degrees "
      "divisible by 8 (8*24, Springer); the x^2-central set = %d "
      "elements = exactly 2 classes of size %d (the Galois pair)"
      % (dict(cens_all[vrow]), cv, EXP_CENT[8], len(reg8_rows), cls8),
      cv == EXP_CENT[8] and cens_all[vrow] == FREE8
      and len(reg8_rows) == 2 * cls8)

lc_v = line_census(v)
lines8_ok = all(line_census(Eall[i]) == ((2, 30),) for i in reg8_rows)
check("S1.3 v on the 60 lines: census %s = 30 free 2-orbits, and ALL "
      "480 regular 8-elements read as the free 2-clock {2:30} "
      "(kernel of the line action is mu4 = <v^2>)"
      % dict(lc_v), dict(lc_v) == {2: 30} and lines8_ok)

MV = matrix_of(v)
check("S1.4 exact 4x4 matrix of v reproduces the root permutation "
      "(all 240 roots)", verify_matrix(MV, v))
chi_v = chi_asc(MV)
q8p = ppow([GI, GZ, G1], 2)      # (x^2 + i)^2 = x^4 + 2i x^2 - 1
q8m = ppow([GmI, GZ, G1], 2)     # (x^2 - i)^2 = x^4 - 2i x^2 - 1
form8 = ("(x^2+i)^2" if peq(chi_v, q8p)
         else "(x^2-i)^2" if peq(chi_v, q8m) else "OTHER")
chichi8 = peq(pmul(chi_v, pconj(chi_v)), ppow(cyclotomic(8), 2))
print("      char poly chi_v(x) = %s" % pfmt(chi_v))
check("S1.5 zeta8 structure EXACT: chi_v = %s (DOUBLED primitive pair; "
      "Springer exponents 7,11,19,23 mod 8 = 7,3,3,7), chi_v * "
      "conj(chi_v) = Phi_8^2 (%s) -> all four eigenvalues primitive "
      "8th roots, multiplicity 2 each" % (form8, chichi8),
      form8 != "OTHER" and chichi8)

sc2 = is_scalar(mat_pow(MV, 2))
sc4 = is_scalar(mat_pow(MV, 4))
v2cls = classify_center(perm_power(v, 2))
v4cls = classify_center(perm_power(v, 4))
print("      M(v)^2 = %s * Id, M(v)^4 = %s * Id; perm level: v^2 = %s, "
      "v^4 = %s" % (gfmt(sc2) if sc2 else "-", gfmt(sc4) if sc4 else "-",
                    v2cls, v4cls))
check("S1.6 CENTER RELATIONS: v^2 = +-i Id, a GENERATOR of mu4 (not "
      "just +-1), v^4 = -1; so mu4 = <v^2> < <v> and <v>/mu4 = Z2 is "
      "the line 2-clock of S1.3",
      sc2 in (GI, GmI) and sc4 == Gm1 and v2cls in ("J", "J^3")
      and v4cls == "-1")

check("S1.7 witness v IS Springer-regular (numeric eigenvector test)",
      is_regular_numeric(mat_c(MV), 8))

# the free-but-NOT-regular order-8 elements (the honest surprise)
fnr8_rows = [i for i in free8_rows
             if classify_center(perm_power(Eall[i], 2)) == "noncentral"]
y = Eall[fnr8_rows[0]]
MY = matrix_of(y)
chi_y = chi_asc(MY)
cy = centralizer_order(y)
check("S1.8 HONEST KILL of 'free => regular' at d = 8: %d free order-8 "
      "elements have x^2 NONCENTRAL; witness: chi = %s = Phi_8 (SIMPLE "
      "primitive spectrum 1,3,5,7 instead of the Springer double "
      "7,3,3,7), |C| = %d (not 192), Springer-regular: %s -> free "
      "census {8:30} does NOT imply regularity"
      % (len(fnr8_rows), pfmt(chi_y), cy,
         is_regular_numeric(mat_c(MY), 8)),
      len(fnr8_rows) == 4320 and peq(chi_y, cyclotomic(8))
      and cy == 32 and not is_regular_numeric(mat_c(MY), 8))

# =============================================================== S2
section("S2: THE UNIFIED THEOREM -- mu4 = <x^(d/4)> for every regular "
        "d-clock; converse exact with ONE exception: the c-classes")

q12p = ppow([Gm1, GI, G1], 2)    # (x^2 + i x - 1)^2
q12m = ppow([Gm1, GmI, G1], 2)   # (x^2 - i x - 1)^2
q24p = [Gm1, GZ, GI, GZ, G1]     # x^4 + i x^2 - 1
q24m = [Gm1, GZ, GmI, GZ, G1]    # x^4 - i x^2 - 1
FORMS = {8: {"(x^2+i)^2": q8p, "(x^2-i)^2": q8m},
         12: {"(x^2+ix-1)^2": q12p, "(x^2-ix-1)^2": q12m},
         20: {},                 # the two Q(i)-quartic factors of Phi_20
         24: {"x^4+ix^2-1": q24p, "x^4-ix^2-1": q24m}}

theorem_rows = []
extra_by_d = {}
all_ok = True
for d in DEGS:
    k4 = d // 4
    rows_d = np.where(ord_all == d)[0]
    free_cen = ((d, 240 // d),)
    # element-exhaustive: the x^(d/4)-central set, split into the
    # regular part (free census) and the rest
    cen_rows = [i for i in rows_d
                if classify_center(perm_power(Eall[i], k4))
                in ("J", "J^3")]
    reg_rows = [i for i in cen_rows if cens_all[i] == free_cen]
    extra_by_d[d] = [i for i in cen_rows if cens_all[i] != free_cen]
    signs = Counter(classify_center(perm_power(Eall[i], k4))
                    for i in reg_rows)
    n_free = sum(1 for i in rows_d if cens_all[i] == free_cen)
    cls_size = 46080 // EXP_CENT[d]
    exp_line = ((k4, 240 // d),)
    lines_ok = all(line_census(Eall[i]) == exp_line for i in reg_rows)
    # witness: exact matrix facts
    x = Eall[reg_rows[0]]
    cx = centralizer_order(x)
    MX = matrix_of(x)
    ok_mat = verify_matrix(MX, x)
    chi_x = chi_asc(MX)
    form = next((nm for nm, P in FORMS[d].items() if peq(chi_x, P)),
                "quartic factor of Phi_%d" % d)
    e_chichi = 8 // phi_euler(d)
    chichi = peq(pmul(chi_x, pconj(chi_x)), ppow(cyclotomic(d), e_chichi))
    sc = is_scalar(mat_pow(MX, k4))
    reg_num = is_regular_numeric(mat_c(MX), d)
    ok = (len(reg_rows) == 2 * cls_size
          and signs["J"] == signs["J^3"] == cls_size
          and lines_ok and cx == EXP_CENT[d] and ok_mat
          and chichi and sc in (GI, GmI) and reg_num)
    all_ok = all_ok and ok
    theorem_rows.append((d, k4, len(reg_rows), len(extra_by_d[d]),
                         n_free, dict(signs), pfmt(chi_x),
                         gfmt(sc) if sc else "-"))
    check("S2.%d d=%d: REGULAR set (x^%d central AND free census) = %d "
          "elements = 2 classes of size %d (sign split %s), free line "
          "census {%d:%d} for all (%s); witness: |C| = %d (Springer "
          "%d), matrix exact (%s), chi = %s, chi*conj(chi) = Phi_%d^%d "
          "(%s), M^%d = %s * Id, Springer-regular (%s); x^%d-central "
          "elements beyond the regular set: %d"
          % (DEGS.index(d) + 1, d, k4, len(reg_rows), cls_size,
             dict(signs), k4, 240 // d, lines_ok, cx, EXP_CENT[d],
             ok_mat, form, d, e_chichi, chichi, k4,
             gfmt(sc) if sc else "-", reg_num, k4,
             len(extra_by_d[d])), ok)

# the converse: exact with ONE exception, the compiler-clock classes
cid_c = int(class_id[byte2row[cperm.tobytes()]])
cinv = perm_power(cperm, 11)
cid_ci = int(class_id[byte2row[cinv.tobytes()]])
extra12 = extra_by_d[12]
extra_cids = sorted({int(class_id[i]) for i in extra12})
extra_cen_ok = all(cens_all[i] == cen_c for i in extra12)
check("S2.5 CONVERSE: at d = 8, 20, 24 the x^(d/4)-central set IS the "
      "regular set (extras: %d, %d, %d); at d = 12 there are exactly "
      "%d extra elements = 2 classes of size 640 = the class of the "
      "COMPILER CLOCK c and of its Galois twin c^-1 (class ids %s = "
      "{class(c), class(c^-1)} = %s), all with c's census %s"
      % (len(extra_by_d[8]), len(extra_by_d[20]), len(extra_by_d[24]),
         len(extra12), extra_cids, sorted({cid_c, cid_ci}),
         dict(cen_c)),
      len(extra_by_d[8]) == 0 and len(extra_by_d[20]) == 0
      and len(extra_by_d[24]) == 0 and len(extra12) == 1280
      and extra_cids == sorted({cid_c, cid_ci}) and cid_c != cid_ci
      and class_sizes[cid_c] == 640 and class_sizes[cid_ci] == 640
      and extra_cen_ok)

# class-level: x^(d/4) central <=> Springer-regular OR c-class
print()
print("      conjugacy classes of orders 8/12/20/24 "
      "(size, |C| = 46080/size, census, x^(d/4), regular?):")
equiv_ok = True
reg_class_count = Counter()
for cid in range(n_classes):
    rep = class_reps[cid]
    d = int(ord_all[rep])
    if d not in DEGS:
        continue
    size = class_sizes[cid]
    powcls = classify_center(perm_power(Eall[rep], d // 4))
    Mrep = matrix_of(Eall[rep])
    reg = is_regular_numeric(mat_c(Mrep), d)
    chi_rep = chi_asc(Mrep)
    if (powcls in ("J", "J^3")) != (reg or cid in (cid_c, cid_ci)):
        equiv_ok = False
    if reg:
        reg_class_count[d] += 1
    tag = " <-- class(c)" if cid == cid_c else (
        " <-- class(c^-1)" if cid == cid_ci else "")
    print("      ord %2d  size %5d  |C| %4d  census %-22s x^(d/4)=%-10s "
          "regular=%-5s chi=%s%s"
          % (d, size, 46080 // size, dict(cens_all[rep]), powcls, reg,
             pfmt(chi_rep), tag))
check("S2.6 CLASS-LEVEL THEOREM (one numeric eigenvector test per "
      "class, all classes of orders 8/12/20/24): x^(d/4) in {J, J^3} "
      "<=> Springer-regular OR compiler-clock class; regular classes "
      "per degree: %s = exactly 2 each (the Galois pair J / J^3); "
      "the c-classes are the ONLY non-regular clocks in G31 whose "
      "d/4-th power generates the center"
      % dict(sorted(reg_class_count.items())),
      equiv_ok and all(reg_class_count[d] == 2 for d in DEGS))

expnts = [d - 1 for d in DEGS]
check("S2.7 EXPONENT SYSTEMATICS: exponents of G31 = %s, ALL = 3 mod 4 "
      "-- for a zeta_d^k-regular element the eigenvalues are "
      "zeta_d^(k*m_i), so x^(d/4) = i^(3k) Id = (-i)^k Id: ONE "
      "formula, x^(d/4) is a GENERATOR of mu4 (never +-1), uniformly "
      "for all four degrees; verified element-exhaustively above"
      % expnts, all(m % 4 == 3 for m in expnts) and all_ok)

print()
print("      exponent-systematics table (element-exhaustive):")
print("      %3s %4s %7s %7s %7s %-22s %-24s %s"
      % ("d", "d/4", "#reg", "#extra", "#free", "sign split (reg)",
         "chi (witness)", "x^(d/4)"))
for d, k4, nreg, nextra, nfree, signs, chi_s, sc_s in theorem_rows:
    print("      %3d %4d %7d %7d %7d %-22s %-24s %s * Id"
          % (d, k4, nreg, nextra, nfree, str(signs), chi_s, sc_s))

# =============================================================== S3
section("S3: controls -- non-regular 8s, the compiler clock, order "
        "census, sharpness")

# ---- sharpness scan: x^(o/4) for EVERY element of order divisible by 4
t = time.time()
sharp = defaultdict(Counter)
for i in range(len(Eall)):
    o = int(ord_all[i])
    if o % 4:
        continue
    sharp[(o, cens_all[i])][classify_center(perm_power(Eall[i],
                                                       o // 4))] += 1
print("      sharpness scan x^(ord/4) over all elements with 4 | ord "
      "(%.1f s):" % (time.time() - t))
print("      %3s %-34s %s" % ("ord", "root census", "x^(ord/4) lands in"))
for (o, cen), ctr in sorted(sharp.items()):
    print("      %3d %-34s %s" % (o, dict(cen), dict(ctr)))

# (a) non-regular order-8 elements: non-free ones
nonfree8 = {cen: ctr for (o, cen), ctr in sharp.items()
            if o == 8 and cen != FREE8}
n_nonfree8 = sum(sum(c.values()) for c in nonfree8.values())
nf8_all_noncentral = all(set(c) == {"noncentral"}
                         for c in nonfree8.values())
z8 = Eall[next(i for i in rows8 if cens_all[i] != FREE8)]
check("S3.1 (a) NON-free order-8 elements: %d in %d censuses (with "
      "fixed roots {1:4,...} or 2-cycles {2:2,...}) -- all their "
      "squares NONCENTRAL (%s); witness |C| = %d, regular: %s; "
      "together with S1.8: order-8 splits into 480 regular + 4320 "
      "free non-regular + 5760 non-free"
      % (n_nonfree8, len(nonfree8), nf8_all_noncentral,
         centralizer_order(z8),
         is_regular_numeric(mat_c(matrix_of(z8)), 8)),
      n_nonfree8 == 5760 and nf8_all_noncentral)

# (b) the compiler clock c
c3 = perm_power(cperm, 3)
Mc = matrix_of(cperm)
sc_c3 = is_scalar(mat_pow(Mc, 3))
sig3_ok = np.array_equal(perm_power(sigperm, 3), IDP)
comm_ok = np.array_equal(comp(Jperm, sigperm), comp(sigperm, Jperm))
c4_ok = np.array_equal(perm_power(cperm, 4), sigperm)
c9_ok = np.array_equal(perm_power(cperm, 9), Jperm)
check("S3.2 (b) COMPILER CLOCK: sigma^3 = 1 (%s), [J, sigma] = 0 (%s), "
      "so c^3 = (J sigma)^3 = J^3 -- exact: c^3 = %s at perm level, "
      "M(c)^3 = %s * Id; sigma = c^4 (%s), J = c^9 (%s)"
      % (sig3_ok, comm_ok, classify_center(c3),
         gfmt(sc_c3) if sc_c3 else "-", c4_ok, c9_ok),
      sig3_ok and comm_ok and classify_center(c3) == "J^3"
      and sc_c3 == GmI and c4_ok and c9_ok)

cc = centralizer_order(cperm)
c_reg = is_regular_numeric(mat_c(Mc), 12)
lc_c = line_census(cperm)
ctr_c_census = sharp[(12, cen_c)]
chi_c = chi_asc(Mc)
# (x - i)^2 (x^2 + i x - 1): half the regular-12 Springer block plus
# a doubled eigenvalue i; spectrum {i, i, zeta12^7, zeta12^11}, every
# eigenvalue satisfies lambda^3 = -i
chi_c_target = pmul(ppow([GmI, G1], 2), [Gm1, GI, G1])
chi_ci_target = pconj(chi_c_target)
chi_ci = chi_asc(matrix_of(cinv))
print("      chi_c(x) = %s = (x-i)^2 * (x^2+ix-1): %s"
      % (pfmt(chi_c), peq(chi_c, chi_c_target)))
check("S3.3 (b) THE PUNCHLINE, honestly bounded: c is NOT regular "
      "(census %s, |C| = %d, eigenvector test %s -- v629 kill "
      "reproduced), yet c^(12/4) = c^3 = J^3 IS a generator of mu4; "
      "EXACT reason: chi_c = (x-i)^2 (x^2+ix-1) -- HALF the "
      "regular-12 Springer block (x^2+ix-1)^2 plus doubled i, all "
      "eigenvalues satisfy lambda^3 = -i (%s; Galois twin conj: %s); "
      "census-level honesty: of the %d elements sharing c's census, "
      "only %d (= class(c) + class(c^-1), 2 x 640, |C| = 72) have "
      "central cubes: %s; on lines c acts as sigma, census %s "
      "(order 3 = 12/4 but NOT free)"
      % (dict(cen_c), cc, c_reg, peq(chi_c, chi_c_target),
         peq(chi_ci, chi_ci_target), sum(ctr_c_census.values()),
         ctr_c_census["J"] + ctr_c_census["J^3"], dict(ctr_c_census),
         dict(lc_c)),
      cc == 72 and (not c_reg) and classify_center(c3) == "J^3"
      and peq(chi_c, chi_c_target) and peq(chi_ci, chi_ci_target)
      and ctr_c_census["J"] == ctr_c_census["J^3"] == 640
      and dict(lc_c) == {1: 3, 3: 19})

# (c) full order census + free-action structure
print("      full order census of G31:")
print("      %5s %8s %10s" % ("ord", "#elems", "#free"))
free_orders = set()
for o in sorted(spec):
    nfree = sum(1 for i in np.where(ord_all == o)[0]
                if cens_all[i] == ((o, 240 // o),)) if 240 % o == 0 else 0
    if o > 1 and nfree > 0:
        free_orders.add(o)
    print("      %5d %8d %10d" % (o, spec[o], nfree))
div_degs = sorted({e for d in DEGS for e in divisors(d) if e > 1})
max_div = {o for o in free_orders
           if not any(o != o2 and o2 % o == 0 for o2 in free_orders)}
four_largest = set(sorted(free_orders)[-4:])
check("S3.4 (c) order census: sum %d = 46080, max order 24; orders with "
      "FREE elements: %s = exactly the divisors > 1 of the degrees "
      "(%s)" % (sum(spec.values()), sorted(free_orders),
                sorted(free_orders) == div_degs),
      sum(spec.values()) == 46080 and max(spec) == 24
      and sorted(free_orders) == div_degs)
check("S3.5 (c) HONEST: {8,12,20,24} are NOT the divisibility-maximal "
      "free orders (that is %s, since 8 | 24 and 12 | 24) and NOT the "
      "four largest (%s, order 10 acts freely via u^2); the correct "
      "characterization: degrees = free orders divisible by 4, above "
      "4: %s" % (sorted(max_div), sorted(four_largest),
                 sorted(o for o in free_orders if o % 4 == 0 and o > 4)),
      sorted(max_div) == [20, 24]
      and sorted(o for o in free_orders if o % 4 == 0 and o > 4) == DEGS)

# (d) the order-4 boundary: free does NOT imply x central
row4 = sharp.get((4, ((4, 60),)), Counter())
n4_noncentral = row4.get("noncentral", 0)
b_ok = row4.get("J", 0) == 1 and row4.get("J^3", 0) == 1
w4row = next(i for i in np.where(ord_all == 4)[0]
             if cens_all[i] == ((4, 60),)
             and classify_center(Eall[i]) == "noncentral")
w4_reg = is_regular_numeric(mat_c(matrix_of(Eall[w4row])), 4)
check("S3.6 (d) BOUNDARY at order 4: free order-4 elements are J, J^3 "
      "(%s) plus %d NONCENTRAL ones; a noncentral free-4 witness is "
      "NOT Springer-regular (%s) -> already at order 4 freeness does "
      "not imply regularity; the d/4-theorem lives on the DEGREE "
      "orders {8,12,20,24} (plus J as the trivial d = 4 case, plus c)"
      % (b_ok, n4_noncentral, not w4_reg),
      b_ok and n4_noncentral == 510 and not w4_reg)

# =============================================================== S4
section("S4: typing summary")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print()
print("SATZ (exakt; elementweise + klassenweise erschoepfend geprueft):")
print("  In G31 (|G31| = 46080, Grade 8,12,20,24, Zentrum mu4 = <i*Id>)")
print("  gilt: (A) JEDE Springer-regulaere d-Uhr x (d in {8,12,20,24})")
print("  enthaelt das Zentrum als d/4-te Potenz: x^(d/4) in {J, J^3},")
print("  mu4 = <x^(d/4)>, stets ein ERZEUGER (+-i*Id, nie +-1) --")
print("  einheitlicher Grund: alle Exponenten (7,11,19,23) sind = 3")
print("  mod 4, also x^(d/4) = (-i)^k * Id fuer zeta_d^k-regulaeres x.")
print("  Pro Grad genau 2 regulaere Klassen (Galois-Paar J/J^3,")
print("  Groessen 240/160/2304/1920, |C| = 192/288/20/24). Auf den 60")
print("  Linien liest sich jede regulaere d-Uhr als FREIE d/4-Uhr:")
print("  {2:30}/{3:20}/{5:12}/{6:10}.")
print("  (B) UMKEHRUNG: bei d = 8, 20, 24 ist die x^(d/4)-zentrale")
print("  Menge GENAU die regulaere Menge; bei d = 12 kommen exakt zwei")
print("  Klassen hinzu (2 x 640, |C| = 72): die Klasse der COMPILER-")
print("  UHR c = J o sigma und ihr Galois-Zwilling class(c^-1).")
print("POINTE (exakt): c^3 = J^3 = -i*Id (sigma^3 = 1, [J,sigma] = 0),")
print("  chi_c = (x-i)^2 (x^2+ix-1) = der HALBE regulaere-12er-")
print("  Springer-Block plus verdoppeltes i; alle Eigenwerte erfuellen")
print("  lambda^3 = -i. Die c-Klassen sind die EINZIGEN nicht-")
print("  regulaeren Uhren in ganz G31, deren d/4-te Potenz das Zentrum")
print("  erzeugt -- 'Zentrum = d/4-te Potenz' gilt fuer die vier")
print("  regulaeren Uhren UND (als einzige Ausnahme der Umkehrung) die")
print("  Compiler-Uhr. Zensus-ehrlich: 3840 Elemente mit c-Zensus")
print("  haben NICHT-zentrale dritte Potenz (Klassen-, nicht Zensus-")
print("  Eigenschaft).")
print("BEOBACHTUNG / EHRLICHE KILLS:")
print("  - 'frei => regulaer' ist bei d = 8 und d = 12 FALSCH:")
print("    4320 freie 8er (chi = Phi_8, |C| = 32) und 960 freie 12er")
print("    (chi = Phi_12, |C| = 48) sind NICHT regulaer, ihre d/4-te")
print("    Potenz ist nicht zentral. Bei d = 20, 24 gilt frei <=>")
print("    regulaer. Der Springer-Fingerabdruck ist das VERDOPPELTE")
print("    Spektrum ((x^2+-i)^2, (x^2+-ix-1)^2), nicht der Zensus.")
print("  - {8,12,20,24} sind NICHT die maximalen freien Ordnungen")
print("    (8|24, 12|24; Ordnung 10 wirkt frei): Grade = freie")
print("    Ordnungen mit 4 | d, d > 4.")
print("  - Ordnung-4-Grenze: 510 nichtzentrale freie 4-Elemente,")
print("    keines regulaer -- Freiheit impliziert keine Regularitaet.")
print()
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS)
      else "SOME CHECKS FAILED")


def run():
    """run_all entry point: the checks above already ran at import."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
