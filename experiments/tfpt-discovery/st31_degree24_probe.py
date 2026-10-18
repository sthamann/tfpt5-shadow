#!/usr/bin/env python3
"""ST31 degree-24 probe -- the regular 24-clock vs the compiler clock.

Predecessor (read-only): st31_structure_probe.py established G31 =
<60 order-2 unitary reflections> on the 240 E8 roots, |G31| = 46080,
degrees (8,12,20,24), regular elements of orders 8/12/20/24 with free
root censuses {8:30}/{12:20}/{20:12}/{24:10}, and the HONEST kill: the
compiler clock c = J o sigma (order 12, sigma = c^4, J = c^9) is NOT
regular (census 19 x 12 + 3 x 4, |C(c)| = 72).

This probe drills into the 24-degree and the 20-degree:

S1  REGULAR 24-CLOCK: construct an explicit w with ord(w) = 24, free
    census {24:10}, |C(w)| = 24; census of its action on the 60 lines;
    EXACT 4x4 Z[i]-matrix, exact characteristic polynomial (Faddeev-
    LeVerrier over Q(i)), primitive-zeta24 test via exact divisibility;
    the relation of <w> to the mu4 center: w^12 =? -1, w^6 =? +-J.
S2  THE CLOCK QUESTION: is c = w^2 for an order-24 w (regular or not)?
    Cycle-type arithmetic: 12-cycles of any square come in PAIRS from
    24-cycles (and 4-cycles in pairs from 8-cycles); c has 19 and 3
    (both odd) -> impossible even in S_240.  Verified by an exhaustive
    scan of all order-24 censuses, plus the full power scan: for EVERY
    census in G31 and every exponent k, does census(x^k) = census(c)?
S3  THE 20-DEGREE: regular u with census {20:12}, |C(u)| = 20; u^5 =?
    +-J (central scalar, stronger than J-class); u^4 of order 5 with
    census {5:48} (48 = 240/5); |C(u^4)|; line censuses; exact char
    polynomial of u, primitive-zeta20 test.
S4  typing summary: what is exact/structural, what stays observation.

Cycle censuses are S_240 class invariants: census mismatch is a
rigorous conjugacy kill (in G31 and in S_240).  Sandbox: writes nothing.
"""

import itertools
import time
from collections import Counter
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
section("S0: roots, J, sigma, c, lines (doubled integer coordinates)")

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


cperm = comp(Jperm, sigperm)
cen_c, ord_c = census_order(cperm)
check("S0.2 compiler clock c = J o sigma: order %d, root census %s "
      "(v629: 19 x 12 + 3 x 4)" % (ord_c, dict(cen_c)),
      ord_c == 12 and dict(cen_c) == {4: 3, 12: 19})

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


# ============================================================ S0b group
section("S0b: the 60 reflections and G31 (BFS to 46080 elements)")

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
check("S0b.1 60 distinct order-2 reflections preserve the roots",
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
check("S0b.2 |G31| = %d (BFS, %.1f s)" % (len(Gset), time.time() - t),
      len(Gset) == 46080)
Eall = np.stack(list(Gset.values()))
check("S0b.3 J, sigma, c in G31",
      Jperm.tobytes() in Gset and sigperm.tobytes() in Gset
      and cperm.tobytes() in Gset)


def centralizer_order(x):
    x = np.asarray(x, dtype=np.int16)
    return int(np.sum(np.all(Eall[:, x] == x[Eall], axis=1)))


check("S0b.4 |C_G31(c)| = %d (v629/st31: 72)" % centralizer_order(cperm),
      centralizer_order(cperm) == 72)

# ------------------------- census + order pass over all 46080 elements
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
check("S0b.5 element orders computed for all 46080 elements "
      "(max order %d)" % max(spec), sum(spec.values()) == 46080)

# ==================================================== exact Q(i) algebra
GZ = (Fr(0), Fr(0))
G1 = (Fr(1), Fr(0))
GI = (Fr(0), Fr(1))


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
        return "%si" % a[1]
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


# exact Q(i)-basis among the roots (greedy rank)
basis_idx = []
ech = []
for i in range(N240):
    v = zvec(i)[:]
    for r in ech:
        pc = next(c for c in range(4) if not is0(r[c]))
        if not is0(v[pc]):
            f = gdiv(v[pc], r[pc])
            v = [gsub(v[c], gmul(f, r[c])) for c in range(4)]
    if any(not is0(x) for x in v):
        ech.append(v)
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


MJ = matrix_of(Jperm)
check("S0c.1 exact matrix machinery: M(J) = i * Id (verified on all "
      "240 roots: %s)" % verify_matrix(MJ, Jperm),
      all(MJ[r][c] == (GI if r == c else GZ)
          for r in range(4) for c in range(4))
      and verify_matrix(MJ, Jperm))


def charpoly(M):
    """Faddeev-LeVerrier: x^4 + c1 x^3 + c2 x^2 + c3 x + c4, exact."""
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
    return cs  # [c1, c2, c3, c4]


def poly_str(cs):
    names = ["x^3", "x^2", "x", ""]
    out = "x^4"
    for c, nm in zip(cs, names):
        if not is0(c):
            out += " + %s%s" % (gfmt(c), ("*" + nm) if nm else "")
    return out


def divides_xN_minus_1(cs, N):
    """does x^4 + c1 x^3 + ... + c4 divide x^N - 1 over Q(i)?"""
    rem = [GZ] * (N + 1)
    rem[N] = G1
    rem[0] = gsub(rem[0], G1)
    plow = [cs[3], cs[2], cs[1], cs[0]]        # degrees 0..3
    for d in range(N, 3, -1):
        cd = rem[d]
        if is0(cd):
            continue
        rem[d] = GZ
        for k in range(4):
            rem[d - 4 + k] = gsub(rem[d - 4 + k], gmul(cd, plow[k]))
    return all(is0(x) for x in rem[:4])


def gaussian_integral(cs):
    return all(c[0].denominator == 1 and c[1].denominator == 1
               for c in cs)


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


def perm_power(p, k):
    r = IDP
    b = p
    while k:
        if k & 1:
            r = comp(b, r)
        b = comp(b, b)
        k >>= 1
    return r


# =============================================================== S1
section("S1: the regular 24-clock w")

rows24 = np.where(ord_all == 24)[0]
cen24 = Counter(cens_all[i] for i in rows24)
print("      order-24 elements: %d; distinct root censuses:" % len(rows24))
for cen, cnt in sorted(cen24.items()):
    print("        %-28s x %d" % (dict(cen), cnt))
reg24_rows = [i for i in rows24 if dict(cens_all[i]) == {24: 10}]
check("S1.1 elements with FREE census {24:10}: %d (of %d order-24 "
      "elements)" % (len(reg24_rows), len(rows24)), len(reg24_rows) > 0)

wrow = reg24_rows[0]
w = Eall[wrow]
cw = centralizer_order(w)
check("S1.2 witness w: root census %s, |C_G31(w)| = %d = 24 "
      "(Springer: product of degrees divisible by 24) -> w is the "
      "regular 24-element; #free-census elements / class size 1920 = "
      "%d regular classes (S240-census level)"
      % (dict(cens_all[wrow]), cw, len(reg24_rows) // 1920),
      cw == 24 and len(reg24_rows) % 1920 == 0)

lc_w = line_census(w)
check("S1.3 w on the 60 lines: census %s = 10 free 6-orbits "
      "(60 = 6 x 10; the 24-clock reads on lines as a 6-clock)"
      % dict(lc_w), dict(lc_w) == {6: 10})

w6 = perm_power(w, 6)
w12 = perm_power(w, 12)
J2 = comp(Jperm, Jperm)
J3 = comp(J2, Jperm)
w6_is = ("J" if np.array_equal(w6, Jperm)
         else "J^3" if np.array_equal(w6, J3) else "OTHER")
check("S1.4 EXACT center relations: w^12 = -1 (= J^2): %s; w^6 = %s "
      "(scalar of order 4) -> <w> CONTAINS the mu4 center as <w^6>, "
      "mu4 = <w^6>, and <w>/mu4 = Z6 is exactly the line 6-clock of "
      "S1.3 (compare compiler clock: J = c^9, sigma = c^4)"
      % (np.array_equal(w12, J2), w6_is),
      np.array_equal(w12, J2) and w6_is in ("J", "J^3"))

MW = matrix_of(w)
check("S1.5 exact 4x4 matrix of w reproduces the root permutation "
      "(all 240 roots)", verify_matrix(MW, w))
cs_w = charpoly(MW)
sc6 = is_scalar(mat_pow(MW, 6))
sc12 = is_scalar(mat_pow(MW, 12))
print("      char poly chi_w(x) = %s" % poly_str(cs_w))
print("      M(w)^6 = %s * Id, M(w)^12 = %s * Id"
      % (gfmt(sc6) if sc6 else "-", gfmt(sc12) if sc12 else "-"))
target_plus = [GZ, GI, GZ, (Fr(-1), Fr(0))]
target_minus = [GZ, (Fr(0), Fr(-1)), GZ, (Fr(-1), Fr(0))]
form = ("x^4 + i x^2 - 1" if cs_w == target_plus
        else "x^4 - i x^2 - 1" if cs_w == target_minus else "OTHER")
div24 = divides_xN_minus_1(cs_w, 24)
div_proper = {d: divides_xN_minus_1(cs_w, d)
              for d in (1, 2, 3, 4, 6, 8, 12)}
check("S1.6 zeta24 structure EXACT: chi_w is Gaussian-integral (%s), "
      "equals %s (a Z[i]-quartic factor of Phi_24), divides x^24 - 1 "
      "(%s) and divides NO x^d - 1 for proper divisors d | 24 (%s) "
      "-> all four eigenvalues are PRIMITIVE 24th roots of unity "
      "(zeta24-regular spectrum {zeta^7, zeta^11, zeta^19, zeta^23} "
      "up to Galois)"
      % (gaussian_integral(cs_w), form, div24,
         not any(div_proper.values())),
      gaussian_integral(cs_w) and form != "OTHER" and div24
      and not any(div_proper.values())
      and sc12 == (Fr(-1), Fr(0)) and sc6 in (GI, (Fr(0), Fr(-1))))

w2 = comp(w, w)
cen_w2, _ = census_order(w2)
cw2 = centralizer_order(w2)
check("S1.7 the HALF-CLOCK w^2: root census %s = {12:20} (the free "
      "comb), |C_G31(w^2)| = %d = 288 = 12*24 -> w^2 is the REGULAR "
      "12-element of st31 S10.2, NOT the compiler clock (census/"
      "centralizer differ from 19x12+3x4 / 72)"
      % (dict(cen_w2), cw2),
      dict(cen_w2) == {12: 20} and cw2 == 288)

# =============================================================== S2
section("S2: THE CLOCK QUESTION -- is c a power of a (regular) "
        "24-element?")

# (a) exact parity theorem, verified over all order-24 censuses
sq_ok = True
sq_censuses = set()
for cen, cnt in sorted(cen24.items()):
    d = dict(cen)
    sq = Counter()
    for L, m in d.items():
        g = gcd(L, 2)
        sq[L // g] += m * g
    sq_censuses.add(tuple(sorted(sq.items())))
    n12 = sq.get(12, 0)
    n4 = sq.get(4, 0)
    if n12 % 2 or n4 % 2:
        sq_ok = False
    print("      census %-26s -> square census %s" % (d, dict(sq)))
check("S2.1 PARITY THEOREM verified: for EVERY order-24 census, the "
      "square census has an EVEN number of 12-cycles (pairs from "
      "24-cycles) and of 4-cycles (pairs from 8-cycles); c has 19 "
      "twelve-cycles and 3 four-cycles (both ODD) -> c = w^2 is "
      "impossible for ANY order-24 w, even in S_240", sq_ok)
check("S2.2 exhaustive: none of the %d distinct order-24 square "
      "censuses equals census(c) = {12:19, 4:3}" % len(sq_censuses),
      cen_c not in sq_censuses)

# (b) full power scan: census(x^k) = census(c) for ANY x in G31?
t = time.time()
distinct_cens = Counter(cens_all)
hits = []
for cen, cnt in distinct_cens.items():
    d = dict(cen)
    o = 1
    for L in d:
        o = lcm(o, L)
    for k in range(1, o):
        pw = Counter()
        for L, m in d.items():
            g = gcd(L, k)
            pw[L // g] += m * g
        if tuple(sorted(pw.items())) == cen_c:
            hits.append((o, cen, k, cnt))
hit_orders = sorted({h[0] for h in hits})
hit_all_c_census = all(h[1] == cen_c for h in hits)
hit_ks = sorted({h[2] for h in hits})
print("      power-census scan over %d distinct censuses (%.1f s): "
      "%d hits" % (len(distinct_cens), time.time() - t, len(hits)))
print("      hit element orders: %s, hit censuses all = census(c): %s, "
      "hit exponents: %s" % (hit_orders, hit_all_c_census, hit_ks))
check("S2.3 KILL, fully general: the ONLY (census, k) with "
      "census(x^k) = census(c) are order-12 elements with census(c) "
      "itself and k coprime to 12 (%s) -- c is NOT a power of any "
      "element of order 24, 20 or 8, and not of any FREE-acting "
      "element (uniform censuses stay uniform under powers; census(c) "
      "is mixed)"
      % (hit_orders == [12] and hit_all_c_census
         and hit_ks == [1, 5, 7, 11]),
      hit_orders == [12] and hit_all_c_census
      and hit_ks == [1, 5, 7, 11])

# =============================================================== S3
section("S3: the 20-degree -- u regular, u^5 central, u^4 and the 48")

rows20 = np.where(ord_all == 20)[0]
cen20 = Counter(cens_all[i] for i in rows20)
print("      order-20 elements: %d; distinct root censuses:" % len(rows20))
for cen, cnt in sorted(cen20.items()):
    print("        %-28s x %d" % (dict(cen), cnt))
reg20_rows = [i for i in rows20 if dict(cens_all[i]) == {20: 12}]
urow = reg20_rows[0] if reg20_rows else None
u = Eall[urow]
cu = centralizer_order(u)
check("S3.1 regular 20-witness u: %d free-census elements, root census "
      "%s, |C_G31(u)| = %d = 20 (Springer)"
      % (len(reg20_rows), dict(cens_all[urow]), cu),
      len(reg20_rows) > 0 and cu == 20)

u5 = perm_power(u, 5)
u5_is = ("J" if np.array_equal(u5, Jperm)
         else "J^3" if np.array_equal(u5, J3)
         else "-1" if np.array_equal(u5, J2) else "OTHER")
check("S3.2 u^5 = %s: an order-4 CENTRAL scalar (mu4 = <u^5>), i.e. "
      "STRONGER than 'J-class' -- the 20-clock also contains the "
      "center as a power" % u5_is, u5_is in ("J", "J^3"))

u4 = perm_power(u, 4)
cen_u4, ord_u4 = census_order(u4)
cu4 = centralizer_order(u4)
lc_u = line_census(u)
lc_u4 = line_census(u4)
check("S3.3 THE ORDER-5 CENSUS: u^4 has order %d, acts FREELY on the "
      "240 roots with census %s = {5:48}; 48 = 240/5 EXACTLY; line "
      "censuses: u -> %s, u^4 -> %s (both free 5-orbits, 60 = 5 x 12); "
      "|C_G31(u^4)| = %d = 20 (u^4 is zeta5-regular)"
      % (ord_u4, dict(cen_u4), dict(lc_u), dict(lc_u4), cu4),
      ord_u4 == 5 and dict(cen_u4) == {5: 48}
      and dict(lc_u) == {5: 12} and dict(lc_u4) == {5: 12} and cu4 == 20)

MU = matrix_of(u)
check("S3.4 exact 4x4 matrix of u verified on all 240 roots",
      verify_matrix(MU, u))
cs_u = charpoly(MU)
sc5 = is_scalar(mat_pow(MU, 5))
print("      char poly chi_u(x) = %s" % poly_str(cs_u))
print("      M(u)^5 = %s * Id" % (gfmt(sc5) if sc5 else "-"))
div20 = divides_xN_minus_1(cs_u, 20)
div_proper20 = {d: divides_xN_minus_1(cs_u, d)
                for d in (1, 2, 4, 5, 10)}
check("S3.5 zeta20 structure EXACT: chi_u Gaussian-integral (%s), "
      "divides x^20 - 1 (%s), divides NO x^d - 1 for proper d | 20 "
      "(%s) -> all four eigenvalues primitive 20th roots; M(u)^5 "
      "scalar %s" % (gaussian_integral(cs_u), div20,
                     not any(div_proper20.values()),
                     gfmt(sc5) if sc5 else "-"),
      gaussian_integral(cs_u) and div20
      and not any(div_proper20.values())
      and sc5 in (GI, (Fr(0), Fr(-1))))

# does c relate to the 20-tower at all? (census level, for completeness)
c_in_20tower = any(
    tuple(sorted(Counter(
        {(L // gcd(L, k)): m * gcd(L, k)
         for L, m in dict(cen).items()}).items())) == cen_c
    for cen in cen20 for k in range(1, 20))
check("S3.6 no power of any order-20 element has census(c) "
      "(already implied by S2.3): %s" % (not c_in_20tower),
      not c_in_20tower)

# =============================================================== S4
section("S4: typing summary")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print()
print("S1 (24er-Grad): STRUKTURELL/EXAKT -- die regulaere 24-Uhr w")
print("   existiert explizit (Zensus {24:10}, |C| = 24), chi_w = "
      "x^4 +- i x^2 - 1")
print("   (primitive zeta24-Eigenwerte, exakt), w^12 = -1, w^6 = +-J:")
print("   das mu4-Zentrum ist eine POTENZ der regulaeren 24-Uhr; auf den")
print("   60 Linien liest sie sich als freie 6-Uhr {6:10}.")
print("S2 (Uhr-Frage c = w^2): KILL -- Paritaetssatz: 12-Zyklen eines")
print("   Quadrats entstehen PAARWEISE aus 24-Zyklen (4-Zyklen paarweise")
print("   aus 8-Zyklen); census(c) = 19 x 12 + 3 x 4 hat UNGERADE")
print("   Anzahlen -> c ist fuer KEIN w der Ordnung 24 ein Quadrat, und")
print("   (Potenz-Scan) fuer kein Element ausser Ordnung-12-Elementen")
print("   mit c-Zensus selbst eine Potenz. Die nicht-regulaere Uhr ist")
print("   NICHT die Haelfte einer regulaeren 24-Uhr.")
print("S3 (20er-Grad): EXAKT -- u^5 = +-J (zentral, staerker als")
print("   J-Klasse), u^4 frei mit Zensus {5:48}, 48 = 240/5, Linien")
print("   {5:12}, |C(u^4)| = 20. Die GLEICHHEIT 48 = Naht-Sites bleibt")
print("   BEOBACHTUNG (Zahlen-Koinzidenz ohne strukturellen Brueckenschlag")
print("   in dieser Probe); g_car = 5 hat hier nur die Zensus-Seite.")
print("S4: Grad-Anker-Typisierung: 24er- und 20er-Uhr tragen exakte")
print("   Zentrums-Relationen (w^6, u^5 in mu4) -- struktureller Befund;")
print("   die Compiler-Uhr c bleibt in ihrer eigenen (nicht-regulaeren)")
print("   Klasse: Verbindung zu 24 via c = w^2 ist GETOETET.")
print()
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS)
      else "SOME CHECKS FAILED")
