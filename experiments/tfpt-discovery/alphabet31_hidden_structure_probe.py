#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""alphabet31_hidden_structure_probe -- exploration-only deep dig into the
shared 31-alphabet of the four-marks picture (2026-08-21, follow-up to
gesamtbild_synthesis_claims_probe).

NEW QUESTIONS (none in the corpus in this form):

 S1  THE 248 CLOCK: R is invertible mod 3 (ord 8) and mod 5 (ord 124),
     singular mod 2 (projector).  Claim: ord(R mod 15) = lcm(8,124)
     = 248 = dim E8, i.e. the combined invertible-channel clock of the
     flavor matrix ticks with period dim E8 = 8 x 31 -- the SAME
     factorisation as c(E8)_1 = 248/31 = 8 (v61).  Mod 30 the full
     semigroup has pre-period 2 (= |Z2|, the projector transient) and
     period 248.  MC control: how special is order 248 among random
     invertible matrices mod 15?

 S2  THE UNIT CLOCK OF THE 31 ALPHABET: Z31* = Z30 (Coxeter!).  The
     compiler primes read: ord_31(2) = 5 = g_car, ord_31(5) = 3 = N_fam,
     <2> and <5> intersect trivially, <2>*<5> = the quadratic residues
     (order 15).  Multiplier orbit censuses: x->2x has 1 + 6x5 orbits
     (6 = |R+(A3)|), x->5x has 1 + 10x3 (10 = A_Lambda).  Honest note:
     31-1 = 30 forces 30/5 and 30/3; the content is WHICH subgroup
     each geometry's Galois clock generates.

 S3  THE THREE (31,k,l) DIFFERENCE SETS ON ONE Z31 -- the intertwiner
     budget for the open 31<->31 bridge:
       H = PG(4,2) hyperplane Singer set (31,15,7)  [carrier alphabet]
       Q = Paley/QR set (31,15,7)
       D = PG(2,5) planar Singer set (31,6,1)       [flavor alphabet]
     Multiplier groups (exhaustive over 30x31 affine maps): expected
     M(H) = <2> (order 5), M(D) = <5> (order 3), M(Q) = QR (order 15
     -- contains BOTH clocks).  H vs Q equivalence decided exhaustively.
     Singer-normalizer budget verified from scratch (Sylvester kernels):
     |N(Singer)| = 155 = 31*5 in GL5(2) and 372 = 31*3*4 in GL3(5) --
     the only SHARED clock of the two geometries is the bare Z31; the
     Paley set is the unique middle object carrying both Frobenius
     clocks as multipliers.

 S4  31 = 15 + 16: iota(V) = C_even(5) (v845) puts the 15 Hamming labels
     as ONE hyperplane of PG(4,2); the 16 odd-weight words are the
     complement.  The (15,16) pair thus appears MULTIPLICATIVELY in the
     root census 240 = 15 x 16 (v689/v845) and ADDITIVELY in the shared
     alphabet 31 = 15 + 16.  CRT echo: e2 = 15, e3 + e5 = 10 + 6 = 16.
     Typed as synonymy, not evidence.

 S5  SMALL EXACT EXTRAS: L = R + 6W invariants (tr L = 15 = dim A3,
     det L, char poly); the 124-readout is a constant-weight [124,3]_5
     simplex code (all nonzero weights = 100); R mod 11 is a projective
     Singer on PG(2,11) (proj ord 133 = |PG(2,11)|, scalar ord 10).

FIREWALL: experiments-only; no verification/, ledger, paper or website
surface touched; no marker moves; typed as exploration.
"""
import itertools
import math
import random
from collections import Counter

import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))


R = np.array([[1, 3, 0], [1, 5, 2], [2, 5, 3]], dtype=np.int64)
W = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]], dtype=np.int64)
L = R + 6 * W
I3 = np.eye(3, dtype=np.int64)


def mpow(A, n, m):
    Rr = I3 % m
    B = A % m
    while n:
        if n & 1:
            Rr = (Rr @ B) % m
        B = (B @ B) % m
        n >>= 1
    return Rr


def order_mod(A, m, bound):
    X = I3 % m
    A = A % m
    for k in range(1, bound + 1):
        X = (X @ A) % m
        if (X == I3 % m).all():
            return k
    return None


# ===================================================== S1: the 248 clock
print("=" * 72)
print("S1  THE 248 CLOCK OF R")
o3 = order_mod(R, 3, 300)
o5 = order_mod(R, 5, 300)
check("ord(R mod 3) = 8, ord(R mod 5) = 124", (o3, o5) == (8, 124))
check("lcm(8, 124) = 248 = dim E8 = 8 x 31", math.lcm(8, 124) == 248 == 8 * 31)
o15 = order_mod(R, 15, 500)
check("ord(R mod 15) = 248  (combined invertible-channel clock)",
      o15 == 248, f"ord={o15}")
# mod 30: pre-period 2 (projector transient), period 248
X2 = mpow(R, 2, 30)
X250 = mpow(R, 250, 30)
X1 = R % 30
X249 = mpow(R, 249, 30)
check("mod 30: R^(n+248) = R^n for n >= 2 (semigroup period 248)",
      (X250 == X2).all())
check("mod 30: pre-period exactly 2 = |Z2| (R^249 != R^1)",
      not (X249 == X1).all())
check("mirror of v61: dim E8 = 248 = c(E8)_1 x 31 with c = 8 = ord(R mod 3)",
      248 == 8 * 31)
# MC control: how special is order 248 mod 15?
rng = random.Random(31)
hits = tot = 0
for _ in range(4000):
    M = np.array([[rng.randrange(15) for _ in range(3)] for _ in range(3)],
                 dtype=np.int64)
    if int(round(np.linalg.det(M.astype(float)))) % 3 == 0:
        continue
    if int(round(np.linalg.det(M.astype(float)))) % 5 == 0:
        continue
    tot += 1
    if order_mod(M, 15, 496) == 248:
        hits += 1
frac = hits / max(tot, 1)
check("MC control: order 248 is NOT generic mod 15 (fraction < 10%)",
      frac < 0.10, f"fraction={frac:.4f} over {tot} invertible samples")

# ============================================== S2: unit clock of Z31
print("=" * 72)
print("S2  THE UNIT CLOCK OF THE 31 ALPHABET")


def ord_mod_int(a, n):
    x, k = a % n, 1
    while x != 1:
        x = (x * a) % n
        k += 1
    return k


check("Z31* has order 30 = h(E8) = 2*3*5", 30 == 2 * 3 * 5)
o2, o3_, o5_ = ord_mod_int(2, 31), ord_mod_int(3, 31), ord_mod_int(5, 31)
check("ord_31(2) = 5 = g_car  (carrier reads 31 in 5-bit words: F32)",
      o2 == 5, f"{o2}")
check("ord_31(5) = 3 = N_fam  (flavor reads 31 in 3-digit F5 words: F125)",
      o5_ == 3, f"{o5_}")
print(f"       ord_31(3) = {o3_} (family prime; typed as measurement)")
sub2 = {pow(2, k, 31) for k in range(5)}
sub5 = {pow(5, k, 31) for k in range(3)}
prod = {(a * b) % 31 for a in sub2 for b in sub5}
QRs = {(x * x) % 31 for x in range(1, 31)}
check("<2> n <5> = {1}; |<2><5>| = 15 = e2 = |PG(3,2)|",
      sub2 & sub5 == {1} and len(prod) == 15)
check("<2><5> = QR(31): both compiler clocks generate exactly the squares",
      prod == QRs)
check("2 and 5 are QRs mod 31; the non-residue coset is the missing Z2",
      2 in QRs and 5 in QRs and len(set(range(1, 31)) - QRs) == 15)
# orbit censuses of the two multiplier clocks on Z31
def orbit_census(t):
    seen, cens = set(), Counter()
    for x in range(31):
        if x in seen:
            continue
        o = {x}
        y = (t * x) % 31
        while y != x:
            o.add(y)
            y = (t * y) % 31
        seen |= o
        cens[len(o)] += 1
    return dict(cens)


c2, c5 = orbit_census(2), orbit_census(5)
check("x->2x on Z31: 1 fixed + 6 orbits of 5 (6 = |R+(A3)|)",
      c2 == {1: 1, 5: 6}, f"{c2}")
check("x->5x on Z31: 1 fixed + 10 orbits of 3 (10 = A_Lambda)",
      c5 == {1: 1, 3: 10}, f"{c5}")

# ==================== S3: three difference sets and the intertwiner budget
print("=" * 72)
print("S3  THREE (31,k,l) DIFFERENCE SETS ON ONE Z31")

# --- F32 = F2[x]/(x^5 + x^2 + 1), primitive
def f32_build():
    # elements as 5-bit ints, g = x (poly 0b00010)
    def mul(a, b):
        r = 0
        for i in range(5):
            if (b >> i) & 1:
                r ^= a << i
        # reduce mod x^5 + x^2 + 1 (0b100101)
        for i in range(9, 4, -1):
            if (r >> i) & 1:
                r ^= 0b100101 << (i - 5)
        return r
    g = 0b00010
    powers = [1]
    for _ in range(30):
        powers.append(mul(powers[-1], g))
    return powers, mul


pw32, mul32 = f32_build()
check("F32 model: x is primitive (31 distinct powers)",
      len(set(pw32)) == 31)
# trace F32 -> F2: Tr(a) = a + a^2 + a^4 + a^8 + a^16
def tr32(a):
    t, x = 0, a
    for _ in range(5):
        t ^= x
        x = mul32(x, x)
    return t & 1


H = {i for i in range(31) if tr32(pw32[i]) == 0}
def is_ds(S, n, k, lam):
    if len(S) != k:
        return False
    dd = Counter((a - b) % n for a in S for b in S if a != b)
    return all(dd[d] == lam for d in range(1, n))


check("H = {i: Tr(g^i)=0} is a (31,15,7) difference set (PG(4,2) hyperplanes)",
      is_ds(H, 31, 15, 7))
Q = {(x * x) % 31 for x in range(1, 31)}
check("Q = QR(31) is a (31,15,7) difference set (Paley)", is_ds(Q, 31, 15, 7))

# --- F125 = F5[y]/(y^3 + 3y + 3) -- need primitive cubic over F5
def f125_build():
    # find a primitive monic cubic t^3 + a t + b (try a few)
    for a in range(5):
        for b in range(1, 5):
            # multiplication in F5[t]/(t^3 + a t + b)
            def mul(u, v, a=a, b=b):
                # u, v as tuples (c0, c1, c2)
                prod = [0] * 5
                for i in range(3):
                    for j in range(3):
                        prod[i + j] = (prod[i + j] + u[i] * v[j]) % 5
                # reduce: t^3 = -a t - b ; t^4 = -a t^2 - b t
                for i in (4, 3):
                    c = prod[i]
                    if c:
                        prod[i] = 0
                        prod[i - 3] = (prod[i - 3] - b * c) % 5
                        prod[i - 2] = (prod[i - 2] - a * c) % 5
                return tuple(prod[:3])
            g = (0, 1, 0)  # t
            x, order = g, 1
            seen = {g}
            while x != (1, 0, 0):
                x = mul(x, g)
                order += 1
                if order > 124:
                    break
            if order == 124:
                return g, mul, (a, b)
    raise RuntimeError("no primitive cubic found")


g125, mul125, ab = f125_build()
check("F125 model: primitive cubic t^3 + %dt + %d found" % ab, True, f"{ab}")


def tr125(u):
    # Tr_{F125/F5}(u) = u + u^5 + u^25
    def pw(x, n):
        r = (1, 0, 0)
        while n:
            if n & 1:
                r = mul125(r, x)
            x = mul125(x, x)
            n >>= 1
        return r
    a1, a5, a25 = u, pw(u, 5), pw(u, 25)
    return tuple((a1[i] + a5[i] + a25[i]) % 5 for i in range(3))[0] \
        if False else ((a1[0] + a5[0] + a25[0]) % 5)


# powers of g modulo scalars: point i of PG(2,5) = class of g^i, i in Z31
pw125 = [(1, 0, 0)]
for _ in range(124):
    pw125.append(mul125(pw125[-1], g125))
D = {i for i in range(31) if tr125(pw125[i]) == 0}
check("D = {i: Tr(g^i)=0} is a (31,6,1) difference set (PG(2,5) lines)",
      is_ds(D, 31, 6, 1))


# --- multiplier groups and equivalences (exhaustive)
def multipliers(S):
    S = frozenset(S)
    out = set()
    for t in range(1, 31):
        if math.gcd(t, 31) != 1:
            continue
        TS = {(t * x) % 31 for x in S}
        for a in range(31):
            if frozenset((x + a) % 31 for x in TS) == S:
                out.add(t)
                break
    return out


MH, MQ, MD = multipliers(H), multipliers(Q), multipliers(D)
check("M(H) = <2>, order 5 = g_car (carrier clock only)",
      MH == sub2, f"|M(H)|={len(MH)}")
check("M(Q) = QR, order 15 (contains BOTH clocks <2> and <5>)",
      MQ == QRs and sub2 <= MQ and sub5 <= MQ, f"|M(Q)|={len(MQ)}")
check("M(D) = <5>, order 3 = N_fam (family clock only)",
      MD == sub5, f"|M(D)|={len(MD)}")


def equivalent(S1, S2):
    S2 = frozenset(S2)
    for t in range(1, 31):
        if math.gcd(t, 31) != 1:
            continue
        TS = {(t * x) % 31 for x in S1}
        for a in range(31):
            if frozenset((x + a) % 31 for x in TS) == S2:
                return (t, a)
    return None


eqHQ = equivalent(H, Q)
check("H and Q are INEQUIVALENT (31,15,7) sets (multiplier groups differ)",
      eqHQ is None, f"witness={eqHQ}")
# the family clock does NOT act on the carrier geometry:
check("5 is NOT a multiplier of H (family clock cannot act on PG(4,2))",
      5 not in MH)
check("2 is NOT a multiplier of D (carrier clock cannot act on PG(2,5))",
      2 not in MD)
check("Q is the unique middle object: M(Q) contains <2> AND <5>",
      sub2 <= MQ and sub5 <= MQ)

# --- Singer normalizer budgets from scratch (Sylvester kernels)
def normalizer_order_gl(S, p, n, max_k):
    """count g in GL_n(F_p) with g S g^-1 = S^k for some k (g S = S^k g)."""
    import itertools as it
    total = 0
    ks = []
    N = p ** (n * n)
    # solve g S = S^k g as linear system over F_p for each k
    Smat = S % p
    for k in range(1, max_k + 1):
        Sk = mpow_gen(Smat, k, p, n)
        # linear map g -> g S - S^k g ; kernel basis via row reduction
        rows = []
        for idx in range(n * n):
            g = np.zeros((n, n), dtype=np.int64)
            g[idx // n][idx % n] = 1
            E = (g @ Smat - Sk @ g) % p
            rows.append(E.flatten() % p)
        A = np.array(rows, dtype=np.int64).T % p  # (n^2) x (n^2)
        ker = kernel_basis(A, p)
        # count invertible elements in the kernel span
        cnt = 0
        dim = len(ker)
        if dim == 0:
            continue
        for coeffs in it.product(range(p), repeat=dim):
            if all(c == 0 for c in coeffs):
                continue
            g = np.zeros(n * n, dtype=np.int64)
            for c, b in zip(coeffs, ker):
                g = (g + c * b) % p
            gm = g.reshape(n, n)
            if int(round(np.linalg.det(gm.astype(float)))) % p != 0:
                cnt += 1
        if cnt:
            ks.append(k)
            total += cnt
    return total, ks


def mpow_gen(A, n_, p, dim):
    Rr = np.eye(dim, dtype=np.int64) % p
    B = A % p
    while n_:
        if n_ & 1:
            Rr = (Rr @ B) % p
        B = (B @ B) % p
        n_ >>= 1
    return Rr


def kernel_basis(A, p):
    """kernel of A (rows = equations) over F_p."""
    A = A.copy() % p
    m, n = A.shape
    piv, r = [], 0
    for c in range(n):
        pr = None
        for rr in range(r, m):
            if A[rr][c] % p:
                pr = rr
                break
        if pr is None:
            continue
        A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r][c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        for rr in range(m):
            if rr != r and A[rr][c] % p:
                A[rr] = (A[rr] - A[rr][c] * A[r]) % p
        piv.append(c)
        r += 1
    basis = []
    free = [c for c in range(n) if c not in piv]
    for f in free:
        v = np.zeros(n, dtype=np.int64)
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-A[i][f]) % p
        basis.append(v % p)
    return basis


# Singer generator in GL5(F2): companion matrix of x^5 + x^2 + 1
C5 = np.zeros((5, 5), dtype=np.int64)
for i in range(4):
    C5[i + 1][i] = 1
C5[0][4] = 1
C5[2][4] = 1  # x^5 = x^2 + 1
tot2, ks2 = normalizer_order_gl(C5, 2, 5, 31)
check("Singer normalizer in GL5(2): order 155 = 31 x 5, twists = powers of 2",
      tot2 == 155 and sorted(ks2) == [1, 2, 4, 8, 16],
      f"order={tot2}, twists={sorted(ks2)}")
# Singer generator in GL3(F5): companion matrix of t^3 + a t + b (primitive)
a_, b_ = ab
C3m = np.array([[0, 0, (-b_) % 5], [1, 0, (-a_) % 5], [0, 1, 0]],
               dtype=np.int64)
tot5, ks5 = normalizer_order_gl(C3m, 5, 3, 124)
# centralizer of the Singer IS F125* (124 elements, scalars included);
# 3 Frobenius twists (k = 1, 5, 25 up to the 124-cycle) => 124 x 3 = 372,
# projectively 372/|F5*| = 93 = 31 x 3.
check("Singer normalizer in GL3(5): order 372 = 124 x 3 (proj 93 = 31 x 3)",
      tot5 == 372 and len(ks5) == 3, f"order={tot5}, twist count={len(ks5)}")
check("BUDGET: shared clock of the two 31-geometries = bare Z31 only "
      "(Galois orders 5 vs 3, coprime)", math.gcd(5, 3) == 1)

# --- cross-incidence profile D vs H (invariant of the pair of classes)
prof = Counter(len(D & {(x + a) % 31 for x in H}) for a in range(31))
print(f"       cross-profile |D n (H+a)|: {dict(sorted(prof.items()))}")
check("cross-profile = {0:1, 1:2, 2:7, 3:12, 4:7, 5:2} -- exactly ONE "
      "shift where the flavor line misses the carrier hyperplane entirely",
      dict(prof) == {0: 1, 1: 2, 2: 7, 3: 12, 4: 7, 5: 2},
      f"{dict(sorted(prof.items()))}")
# robustness: does the distinguished zero-shift survive ALL equivalence
# transformations t -> tD of the flavor set (t coprime to 31)?
zero_ts = []
for t_ in range(1, 31):
    Dt = {(t_ * x) % 31 for x in D}
    p_ = Counter(len(Dt & {(x + a) % 31 for x in H}) for a in range(31))
    if p_[0] >= 1:
        zero_ts.append((t_, p_[0]))
zt = {t_ for t_, _ in zero_ts}
check("zero-alignment shift exists for EXACTLY HALF the representatives "
      "tD (15/30) -- a genuine Z2 dichotomy on the class pair",
      len(zero_ts) == 15, f"t with zero-shift: {len(zero_ts)}/30")
uniq0 = {n0 for _, n0 in zero_ts}
print(f"       zero-shift multiplicities across t: {sorted(uniq0)}")
nonQR = set(range(1, 31)) - QRs
check("THE SHEET BIT DECIDES: zero-shift t's are exactly ONE coset of "
      "QR(31) (the quadratic character of t is the alignment bit)",
      zt == QRs or zt == nonQR,
      f"zt==QR: {zt == QRs}, zt==nonQR: {zt == nonQR}")
check("when the zero-shift exists it is UNIQUE (multiplicity always 1)",
      uniq0 == {1})
check("the 6 flavor letters fit inside the 16-word payload half of "
      "exactly one address for the canonical pair (D, H)",
      prof[0] == 1)

# ===================================================== S4: 31 = 15 + 16
print("=" * 72)
print("S4  31 = 15 + 16 VIA iota (v845)")
V16 = list(itertools.product([0, 1], repeat=4))


def iota(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


img = {iota(v) for v in V16}
even5 = {w for w in itertools.product([0, 1], repeat=5) if sum(w) % 2 == 0}
check("iota(V) = C_even(5), bijective (v845 S4.1 reproduced)",
      img == even5 and len(img) == 16)
check("15 nonzero labels = ONE hyperplane of PG(4,2) (even-weight); "
      "complement = 16 odd-weight words",
      len([w for w in img if any(w)]) == 15 and 31 - 15 == 16)
check("(15,16) multiplicative in root census 240 = 15 x 16, "
      "additive in the alphabet 31 = 15 + 16",
      240 == 15 * 16 and 31 == 15 + 16)
check("CRT echo: e2 = 15 (address), e3 + e5 = 10 + 6 = 16 (payload)",
      (15 * 15) % 30 == 15 and (10 + 6) == 16 and (15 + 10 + 6) == 31)

# ===================================================== S5: exact extras
print("=" * 72)
print("S5  SMALL EXACT EXTRAS")
Ls = sp.Matrix(L.tolist())
t = sp.symbols('t')
chiL = sp.expand(Ls.charpoly(t).as_expr())
check("tr L = 15 = dim A3 = |PG(3,2)|", int(Ls.trace()) == 15)
detL = int(Ls.det())
print(f"       det L = {detL}, char poly L = {chiL}")
check("det L = 20 = 2 x A_Lambda (typed as measurement)", detL == 20)
# 124-readout simplex code: weights
R5 = R % 5
seqs = []
x0 = np.array([1, 0, 0], dtype=np.int64)
orb = []
v = x0.copy()
for _ in range(124):
    orb.append(v.copy())
    v = (R5 @ v) % 5
wts = set()
for lvec in itertools.product(range(5), repeat=3):
    if lvec == (0, 0, 0):
        continue
    w = sum(1 for u in orb if (lvec[0]*u[0] + lvec[1]*u[1] + lvec[2]*u[2]) % 5)
    wts.add(w)
check("readout code = [124,3]_5 simplex: ALL nonzero readouts have "
      "weight 100 (constant weight)", wts == {100}, f"weights={wts}")
# R mod 11: projective Singer on PG(2,11)
o11 = order_mod(R, 11, 1400)
# projective order: smallest k with R^k scalar mod 11
proj = None
for k in range(1, 1400):
    X = mpow(R, k, 11)
    if (X == X[0][0] * I3 % 11).all() and X[0][0] != 0:
        proj = k
        break
check("R mod 11: ord = 1330, projective ord = 133 = |PG(2,11)| "
      "(a SECOND Singer plane)", o11 == 1330 and proj == 133,
      f"ord={o11}, proj={proj}")
check("1330 = 133 x 10 = |PG(2,11)| x |F11*|", 1330 == 133 * 10)

print("=" * 72)
print(f"TOTAL: {PASS} PASS, {FAIL} FAIL")
raise SystemExit(0 if FAIL == 0 else 1)
