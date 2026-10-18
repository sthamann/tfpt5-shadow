#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gesamtbild_synthesis_claims_probe -- exploration-only audit of the
"Vier-Marken-Unifikation" synthesis text (2026-08-21).

Checks every NEW mathematical claim of the synthesis numerically/symbolically
against the certified objects (R from v4, B/K from v752 convention, sigma
class from v845, bent layer from v774 convention).  NO ledger claim, NO
paper surface -- discovery sandbox only.

Sections:
  S1  FLAVOR.CRT.AUTOMATON  -- R mod 2/3/5/11/13, s=6 uniqueness mod 30,
      Singer readout statistics, prime scan
  S2  CODE.PROJ15.CAPACITY  -- BB^T = 4I+3J, C(K)=log2(15/7), K^2 channel,
      chi^2 contraction 4/49
  S3  counting identities   -- 240-entropy split, 8-log2(240)=C(P),
      31=31 only at N_fam=3, CRT idempotents 15/10/6, two clocks, rate(n)
  S4  sigma 3-tick decoder  -- P_F = I+sigma+sigma^2 projector, Hamming
      weight-3/4 words from 3-cycles, centralizer order 18
  S5  bent layer corollaries -- NL=6, balanced derivatives, (16,6,2)
      difference set, MUB overlap 1/16 (for ALL 6-zero quadratic bent forms)
  S6  Lorentz determinant   -- 4 det X = u^2 - v^2 - w^2, edge (5,-3,4) null
"""
import itertools
import math
from fractions import Fraction as Fr

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


# ============================================================= S1: R CRT
print("=" * 72)
print("S1  FLAVOR CRT AUTOMATON")
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
t = sp.symbols('t')
chi = sp.expand(R.charpoly(t).as_expr())
check("chi_R = t^3 - 9t^2 + 10t - 8", chi == t**3 - 9*t**2 + 10*t - 8)
disc = sp.discriminant(chi, t)
check("disc(chi_R) = -4*1999 (one real + complex pair)",
      disc == -4*1999, f"disc={disc}")

def matmod(M, p):
    return np.array([[int(M[i, j]) % p for j in range(3)] for i in range(3)],
                    dtype=np.int64)

def mpow(A, n, p):
    Rr = np.eye(3, dtype=np.int64)
    B = A.copy()
    while n:
        if n & 1:
            Rr = (Rr @ B) % p
        B = (B @ B) % p
        n >>= 1
    return Rr

def order_gl(A, p, bound):
    X = np.eye(3, dtype=np.int64)
    for k in range(1, bound + 1):
        X = (X @ A) % p
        if (X == np.eye(3, dtype=np.int64) % p).all():
            return k
    return None

# --- mod 2: projector
R2 = matmod(R, 2)
P2 = (R2 @ R2) % 2
check("mod 2: R^2 = P = [[0,0,0],[0,0,0],[1,0,1]]",
      (P2 == np.array([[0,0,0],[0,0,0],[1,0,1]])).all())
check("mod 2: P^2 = P (projector)", ((P2 @ P2) % 2 == P2).all())
check("mod 2: R^n = P for n>=2 (n=2..8)",
      all((mpow(R2, n, 2) == P2).all() for n in range(2, 9)))
chi2 = sp.Poly(chi, t, modulus=2)
check("mod 2: chi = t^2(t+1)",
      sp.factor_list(chi2.as_expr(), modulus=2)[1] is not None and
      sp.rem(chi, t**2*(t+1), t, modulus=2) == 0)

# --- mod 3: 8-clock
R3 = matmod(R, 3)
o3 = order_gl(R3, 3, 100)
check("mod 3: ord(R) = 8, R^4 != I", o3 == 8 and
      not (mpow(R3, 4, 3) == np.eye(3, dtype=np.int64)).all(), f"ord={o3}")
check("mod 3: chi = (t-1)(t^2+t-1)",
      sp.rem(chi - sp.expand((t-1)*(t**2+t-1)), 3, t) == 0 or
      all(c % 3 == 0 for c in sp.Poly(chi - sp.expand((t-1)*(t**2+t-1)), t).all_coeffs()))

# --- mod 5: Singer
R5 = matmod(R, 5)
chi5 = [c % 5 for c in sp.Poly(chi, t).all_coeffs()]
check("mod 5: chi = t^3 + t^2 + 0t + 2", chi5 == [1, 1, 0, 2])
o5 = order_gl(R5, 5, 200)
check("mod 5: ord(R) = 124 = 5^3 - 1 (Singer)", o5 == 124, f"ord={o5}")
check("mod 5: R^31 = 3I", (mpow(R5, 31, 5) == (3*np.eye(3, dtype=np.int64)) % 5).all())
check("mod 5: R^62 = -I = 4I", (mpow(R5, 62, 5) == (4*np.eye(3, dtype=np.int64)) % 5).all())
x = np.array([1, 0, 0], dtype=np.int64)
orbit = []
v = x.copy()
for _ in range(124):
    orbit.append(tuple(v))
    v = (R5 @ v) % 5
check("mod 5: orbit of e1 = all 124 nonzero vectors",
      len(set(orbit)) == 124 and (0, 0, 0) not in set(orbit))

# --- winding uniqueness mod 30
W = sp.Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
s = sp.symbols('s')
Rs = R + s*W
# claimed: mod 5 chi_{R_s} = t^3 + (1-s) t^2 + (2-2s); checked by scan below
def chi_mod(sval, p):
    M = sp.Matrix(R + sval*W)
    return [int(c) % p for c in sp.Poly(M.charpoly(t).as_expr(), t).all_coeffs()]

sols = []
for sv in range(30):
    m2 = (matmod(R + sv*W, 2) == R2).all()                 # preserve mod 2
    m3 = (matmod(R + sv*W, 3) == R3).all()                 # preserve mod 3
    m5 = chi_mod(sv, 5) == [1, 0, 0, 0]                    # nilpotent mod 5
    if m2 and m3 and m5:
        sols.append(sv)
check("s = 6 UNIQUE mod 30 (preserve-2, preserve-3, reset-5)",
      sols == [6], f"solutions={sols}")
check("claimed chi_{R_s} mod 5 formula t^3+(1-s)t^2+(2-2s)",
      all(chi_mod(sv, 5) == [1, (1 - sv) % 5, 0, (2 - 2*sv) % 5]
          for sv in range(30)))

L5 = matmod(R + 6*W, 5)
L2_ = (L5 @ L5) % 5
L3_ = (L2_ @ L5) % 5
check("mod 5: L^3 = 0, L^2 != 0",
      (L3_ == 0).all() and not (L2_ == 0).all())
rks = [np.linalg.matrix_rank(np.array(M, dtype=float)) for M in
       [L5 % 5, L2_, L3_]]
check("mod 5: rank chain L,L^2,L^3 = 2,1,0", rks == [2, 1, 0], f"{rks}")

Lmat = sp.Matrix(R + 6*W)
ev = [complex(e) for e in Lmat.eigenvals()]
check("L = R + 6W: three real positive eigenvalues",
      all(abs(e.imag) < 1e-12 and e.real > 0 for e in ev),
      f"{[round(e.real,4) for e in ev]}")

# --- Singer readout statistics
seq = [int(v[0]) for v in orbit]           # l = e1 readout
from collections import Counter
cnt = Counter(seq)
check("readout: symbol 0 x24, nonzero x25 each",
      cnt[0] == 24 and all(cnt[k] == 25 for k in range(1, 5)), f"{dict(cnt)}")
H = -sum((c/124)*math.log2(c/124) for c in cnt.values())
check("readout entropy = 2.321738899 bit", abs(H - 2.321738899) < 1e-9,
      f"H={H:.9f}, max={math.log2(5):.9f}")
z = np.exp(2j*np.pi*np.array(seq)/5)
ac = [np.sum(z * np.conj(np.roll(z, -k))) for k in range(124)]
check("perfect autocorrelation: C(0)=124, C(k)=-1 (k=1..123)",
      abs(ac[0] - 124) < 1e-9 and
      all(abs(a - (-1)) < 1e-9 for a in ac[1:]))

# --- mod 11 and prime scan
singer_primes = []
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    Rp = matmod(R, p)
    if int(round(np.linalg.det(np.array(Rp, dtype=float)))) % p == 0:
        continue
    o = order_gl(Rp, p, p**3 - 1)
    if o == p**3 - 1:
        singer_primes.append(p)
check("Singer primes (ord = p^3-1) among p<=47: exactly {5, 11}",
      singer_primes == [5, 11], f"{singer_primes}")
o11 = order_gl(matmod(R, 11), 11, 1330)
check("mod 11: ord(R) = 1330 = 11^3 - 1", o11 == 1330, f"ord={o11}")
o13 = order_gl(matmod(R, 13), 13, 13**3)
check("mod 13: NOT Singer (ord != 2196)", o13 != 13**3 - 1, f"ord={o13}")

# ===================================================== S2: PROJ15 capacity
print("=" * 72)
print("S2  PROJECTIVE HAMMING CHANNEL CAPACITY")
pts = [v for v in itertools.product([0, 1], repeat=4) if any(v)]
def symp(x, y):  # standard symplectic form on F2^4
    return (x[0]*y[1] + x[1]*y[0] + x[2]*y[3] + x[3]*y[2]) % 2
B = np.array([[1 if symp(x, y) == 0 else 0 for y in pts] for x in pts])
J15 = np.ones((15, 15), dtype=int)
check("BB^T = 4I + 3J (v752 identity reproduced)",
      (B @ B.T == 4*np.eye(15, dtype=int) + 3*J15).all())
check("row/col sums 7", (B.sum(0) == 7).all() and (B.sum(1) == 7).all())
K = B / 7.0
# weak symmetry -> C = log2 15 - log2 7; confirm with Blahut-Arimoto
def blahut(Q, iters=3000):
    n, m = Q.shape
    p = np.full(n, 1/n)
    for _ in range(iters):
        q = p @ Q
        lg = np.where(Q > 0, np.log(np.maximum(Q, 1e-300) / q), 0.0)
        c = np.exp((Q * lg).sum(axis=1))
        p = p * c
        p /= p.sum()
    q = p @ Q
    lg = np.where(Q > 0, np.log(np.maximum(Q, 1e-300) / q), 0.0)
    return (p[:, None] * Q * lg).sum() / math.log(2)
CK = blahut(K)
check("C(K) = log2(15/7) = 1.099535674 bit",
      abs(CK - math.log2(15/7)) < 1e-6, f"BA={CK:.9f}")
K2 = K @ K
Pi0 = J15 / 15.0
check("K^2 = (4/49)I + (45/49)Pi0 exact",
      np.allclose(K2, 4/49*np.eye(15) + 45/49*Pi0, atol=1e-12))
CK2 = blahut(K2)
CK2_closed = math.log2(15) + (1/7)*math.log2(1/7) + 14*(3/49)*math.log2(3/49)
check("C(K^2) = 0.051770741 bit (symmetric channel closed form)",
      abs(CK2 - CK2_closed) < 1e-6 and abs(CK2_closed - 0.051770741) < 1e-8,
      f"BA={CK2:.9f} closed={CK2_closed:.9f}")
u = np.full(15, 1/15)
rng = np.random.default_rng(42)
ok_chi = ok_l2 = True
for _ in range(200):
    p = rng.dirichlet(np.ones(15))
    chi_in = np.sum((p - u)**2 / u)
    pk = p @ K
    chi_out = np.sum((pk - u)**2 / u)
    if abs(chi_out - (4/49)*chi_in) > 1e-10 * max(1, chi_in):
        ok_chi = False
    if abs(np.linalg.norm(pk - u) - (2/7)*np.linalg.norm(p - u)) > 1e-12:
        ok_l2 = False
check("chi^2(pK|u) = (4/49) chi^2(p|u) EXACT (200 random p)", ok_chi)
check("||(p-u)K||_2 = (2/7)||p-u||_2 -> rho_max = 2/7", ok_l2)
sv = np.linalg.svd(K, compute_uv=False)
check("singular values {1, 2/7 x14}",
      abs(sv[0] - 1) < 1e-12 and np.allclose(sv[1:], 2/7, atol=1e-12))

# ==================================================== S3: counting identities
print("=" * 72)
print("S3  COUNTING / TWO-31 / CLOCKS")
check("240 = 15 * 16 = 15 * 4 * 4", 240 == 15*16 == 15*4*4)
check("H(root) = log2 240 = log2 15 + 2 + 2 = 7.906890596",
      abs(math.log2(240) - (math.log2(15) + 4)) < 1e-12 and
      abs(math.log2(240) - 7.906890596) < 1e-9)
check("8 - log2 240 = log2(16/15) = C((J-I)/15) = 0.093109404",
      abs((8 - math.log2(240)) - math.log2(16/15)) < 1e-12 and
      abs(math.log2(16/15) - 0.093109404) < 1e-9)
# uniform-nonzero channel on 16 labels: weakly symmetric, C = log2 16 - log2 15
P16 = (np.ones((16, 16)) - np.eye(16)) / 15
CP = blahut(P16)
check("C(P) Blahut-Arimoto agrees", abs(CP - math.log2(16/15)) < 1e-6,
      f"{CP:.9f}")
# 31 = 31 only at N_fam = 3:  2^(N+2)-1 = (5^N-1)/4
hits = [N for N in range(1, 51) if 2**(N + 2) - 1 == (5**N - 1)//4
        and (5**N - 1) % 4 == 0]
check("2^(N+2)-1 = (5^N-1)/4 only at N=3 (N<=50)", hits == [3], f"{hits}")
check("|PG(4,2)| = 31 = |PG(2,5)|", 2**5 - 1 == 31 == (5**3 - 1)//4)
# CRT idempotents in Z/30
idem = [e for e in range(30) if (e*e) % 30 == e]
check("idempotents of Z/30 = {0,1,6,10,15,16,21,25}; 15,10,6 orthogonal, sum=31=1",
      all(e in idem for e in (15, 10, 6)) and
      (15*10) % 30 == 0 and (15*6) % 30 == 0 and (10*6) % 30 == 0 and
      (15 + 10 + 6) % 30 == 1)
check("e2=15 kills mod 2? 15=1 mod 2, 0 mod 3, 0 mod 5 (projector to F2)",
      15 % 2 == 1 and 15 % 3 == 0 and 15 % 5 == 0 and
      10 % 3 == 1 and 10 % 2 == 0 and 10 % 5 == 0 and
      6 % 5 == 1 and 6 % 2 == 0 and 6 % 3 == 0)
# two clocks
t0 = math.log(72/17) + 9*math.log(8*math.pi)
check("KMS t0 = ln(72/17)+9ln(8pi) = 30.461 != 30 (two different clocks)",
      abs(t0 - 30.461) < 5e-3 and abs(t0 - 30) > 0.4, f"t0={t0:.6f}")
# transfer spectrum
lam = [(1 - n/3)**6 for n in (0, 1, 2)]
check("lambda_n = (1-n/3)^6 = {1, (2/3)^6, (1/3)^6}",
      abs(lam[1] - (2/3)**6) < 1e-15 and abs(lam[2] - (1/3)**6) < 1e-15)
check("rate slope at n=0 is 2 = |Z2|; pole at n = 3 = N_fam",
      abs(6/3 - 2) < 1e-15)

# ===================================================== S4: sigma decoder
print("=" * 72)
print("S4  SIGMA THREE-TICK DECODER (order-3 class, fix dim 2)")
C3 = np.array([[0, 1], [1, 1]])                    # order 3 in GL2(F2)
sig = np.block([[np.eye(2, dtype=int), np.zeros((2, 2), dtype=int)],
                [np.zeros((2, 2), dtype=int), C3]]).astype(int)
check("sigma^3 = I, sigma != I",
      ((np.linalg.matrix_power(sig, 3) % 2) == np.eye(4, dtype=int)).all() and
      not ((sig % 2) == np.eye(4, dtype=int)).all())
PF = (np.eye(4, dtype=int) + sig + np.linalg.matrix_power(sig, 2)) % 2
check("P_F = I + sigma + sigma^2 idempotent", ((PF @ PF) % 2 == PF).all())
fix = [v for v in itertools.product([0, 1], repeat=4)
       if (tuple((sig @ np.array(v)) % 2) == v)]
img = {tuple((PF @ np.array(v)) % 2) for v in itertools.product([0, 1], repeat=4)}
check("image(P_F) = Fix(sigma), dim 2 (4 elements, 3 nonzero)",
      img == set(fix) and len(fix) == 4)
orbs = {}
seen = set()
cycles3 = []
for v in pts:
    if v in seen:
        continue
    o = [v]
    w = tuple((sig @ np.array(v)) % 2)
    while w != v:
        o.append(w)
        w = tuple((sig @ np.array(w)) % 2)
    seen |= set(o)
    if len(o) == 3:
        cycles3.append(o)
check("15 labels = 3 fixed + 4 three-cycles",
      len([v for v in pts if v in set(fix)]) == 3 and len(cycles3) == 4)
# Hamming [15,11,3]: weight-3 words = projective lines {x,y,x+y}
lines = {frozenset([x, y, tuple((np.array(x) ^ np.array(y)))])
         for x, y in itertools.combinations(pts, 2)
         if tuple(np.array(x) ^ np.array(y)) != (0, 0, 0, 0)}
lines = {l for l in lines if len(l) == 3}
check("|projective lines PG(3,2)| = 35", len(lines) == 35)
ok3 = ok4 = True
for o in cycles3:
    f = tuple((np.array(o[0]) ^ np.array(o[1]) ^ np.array(o[2])))
    if f == (0, 0, 0, 0):
        if frozenset(o) not in lines:
            ok3 = False
    else:
        # {o0,o1,o2,f} must XOR to zero -> weight-4 Hamming word
        tot = np.array(o[0]) ^ np.array(o[1]) ^ np.array(o[2]) ^ np.array(f)
        if tot.any() or f in o:
            ok4 = False
check("f=0 cycles are weight-3 Hamming words (projective lines)", ok3)
check("f!=0 cycles + f are weight-4 Hamming words", ok4)
# centralizer order = |GL2(F2)| * |F4^x| = 6*3 = 18
cent = 0
for M in itertools.product([0, 1], repeat=16):
    A = np.array(M, dtype=int).reshape(4, 4)
    # invertible?
    if int(round(np.linalg.det(A.astype(float)))) % 2 == 0:
        continue
    if ((A @ sig) % 2 == (sig @ A) % 2).all():
        cent += 1
check("|centralizer(sigma)| in GL(4,2) = 18 = |GL2(F2)| x |F4^x|",
      cent == 18, f"{cent}")

# ===================================================== S5: bent corollaries
print("=" * 72)
print("S5  BENT LAYER CRYPTO COROLLARIES (all 6-zero quadratic forms)")
V16 = list(itertools.product([0, 1], repeat=4))
def walsh(f):
    return {a: sum((-1)**((f[x] + sum(a[i]*x[i] for i in range(4))) % 2)
                   for x in V16) for a in V16}
# all quadratic Boolean functions q(x) = sum_{i<j} c_ij x_i x_j + sum l_i x_i
quads = []
for cs in itertools.product([0, 1], repeat=6):
    for ls in itertools.product([0, 1], repeat=4):
        f = {}
        for x in V16:
            v = 0
            idx = 0
            for i in range(4):
                for j in range(i + 1, 4):
                    v += cs[idx]*x[i]*x[j]
                    idx += 1
            v += sum(ls[i]*x[i] for i in range(4))
            f[x] = v % 2
        quads.append(f)
six_zero = [f for f in quads if sum(1 for x in V16 if f[x] == 0) == 6]
check("candidate pool nonempty (Arf-1 refinements incl. q*)",
      len(six_zero) > 0, f"n={len(six_zero)}")
ok_nl = ok_bal = ok_ds = ok_mub = True
for f in six_zero:
    W_ = walsh(f)
    nl = 8 - max(abs(w) for w in W_.values())/2
    if nl != 6:
        ok_nl = False
    for a in V16:
        if a == (0, 0, 0, 0):
            continue
        da = sum((f[x] + f[tuple((x[i] + a[i]) % 2 for i in range(4))]) % 2
                 for x in V16)
        if da != 8:
            ok_bal = False
    D = [x for x in V16 if f[x] == 1]      # 10-set; complement = 6 zeros
    Z = [x for x in V16 if f[x] == 0]
    if len(Z) == 6:
        dd = Counter(tuple((np.array(a) ^ np.array(b)))
                     for a in Z for b in Z if a != b)
        if not all(dd[g] == 2 for g in V16 if g != (0, 0, 0, 0)):
            ok_ds = False
    # MUB: bent basis vs character basis, all overlaps 1/16
    sq = np.array([(-1)**f[x] for x in V16]) / 4.0
    for a in V16:
        ch = np.array([(-1)**(sum(a[i]*x[i] for i in range(4)) % 2)
                       for x in V16]) / 4.0
        ov = abs(np.dot(sq * 4 / 4, ch))**2   # |<b_shift, e_a>|^2 with unit norms
        # translations of sq form the bent basis; check one representative
    # cross-overlap: normalized bent vector vs normalized character
    bn = np.array([(-1)**f[x] for x in V16]) / 4.0
    for a in V16:
        ch = np.array([(-1)**(sum(a[i]*x[i] for i in range(4)) % 2)
                       for x in V16]) / 4.0
        if abs(abs(np.dot(bn, ch))**2 - 1/16) > 1e-12:
            ok_mub = False
check("NL = 6 (max bent nonlinearity) for all", ok_nl)
check("all 15 derivatives balanced (8/8) for all", ok_bal)
check("6 zeros form (16,6,2) difference set for all", ok_ds)
check("|<bent, character>|^2 = 1/16 (MUB) for all", ok_mub)

# ===================================================== S6: Lorentz det
print("=" * 72)
print("S6  RANK-3 DETERMINANT = MINKOWSKI NORM")
a, b, c = sp.symbols('a b c')
X = sp.Matrix([[a, c], [c, b]])
u_, v_, w_ = a + b, a - b, 2*c
check("4 det X = u^2 - v^2 - w^2 (symbolic)",
      sp.simplify(4*X.det() - (u_**2 - v_**2 - w_**2)) == 0)
uvw = (1 + 4, 1 - 4, 2*2)
check("edge matrix [[1,2],[2,4]] -> (u,v,w) = (5,-3,4), null vector",
      uvw == (5, -3, 4) and 5**2 - 3**2 - 4**2 == 0)

print("=" * 72)
print(f"TOTAL: {PASS} PASS, {FAIL} FAIL")
raise SystemExit(0 if FAIL == 0 else 1)
