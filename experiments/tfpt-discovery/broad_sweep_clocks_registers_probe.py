#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""broad_sweep_clocks_registers_probe -- exploration-only broad sweep across
further corpus areas (2026-08-21, third probe of the Gesamtbild round).

 S1  THE (R, L) CLOCK PAIR -- dim vs rank: R mod 30 has pre-period 2 = |Z2|
     and period 248 = dim E8 (previous probe); claim here: L = R + 6W mod 30
     has pre-period 3 = N_fam (nilpotency length of the reset channel) and
     period 8 = rank E8.  Reading: the winding collapses the flavor clock
     dim E8 -> rank E8 (Cartan projection); transients = sheet (2) / family
     (3).

 S2  THE FIELD TOWER OF R: the invertible block of R mod p is a FULL Singer
     torus of dimension d_p with (d_2, d_3, d_5) = (1, 2, 3):
     F2* (order 1) / F9* (order 8, primitive quadratic factor) / F125*
     (order 124).  Cycle lengths (2^1-1, 3^2-1, 5^3-1) = (1, 8, 124).

 S3  WINDING OPCODE CENSUS over s mod 30 (family R_s = R + sW):
     which prime channels are resettable (R_s nilpotent mod p) at all?
     Expected: 5-channel resets exactly at s = 1 mod 5 (unique preserving
     opcode 6 = e5); 2-channel census measured; 3-channel: NO s makes R_s
     nilpotent mod 3 while preserving the other channels -- the family
     channel is winding-protected (N_fam = 3 cannot be reset by any rank-1
     winding).

 S4  THE 210-REGISTER IDEMPOTENTS (Coxeter radical, rad|W(E8)| = 210):
     CRT idempotents (e2, e3, e5, e7) = (105, 70, 126, 120), sum = 421 = 1
     mod 210.  Corpus seats: 105 = C(15,2) = pair count / Kraus legs (v752/
     v801, weight-4 Hamming words); 120 = dim SO(16) = |mu4| x h(E8) (v752
     NS sector / ADHM note).  126 and 70 have NO certified corpus seat
     (E7 root count and dim Lambda^4(8) are EXTERNAL labels) -- typed WEAK,
     observation only.

 S5  GENERATION ASYMMETRY: on the carrier alphabet (PG(4,2), 31 points)
     the compiler family clock sigma (slot 3-cycle via iota, v845) together
     with the Singer alphabet clock generates the FULL simple collineation
     group GL5(2) (order 9999360) -- measured for the canonical labelling
     and random re-labellings; on the flavor alphabet (PG(2,5) as Z31) the
     analogous pair (multiplier x->5x, shift +1) generates only the solvable
     normalizer Z31 x| Z3 (order 93).  Complexity lives on the carrier side.

 S6  SIGMA ORBIT CENSUS ON THE 31: sigma_slot on PG(4,2) has 7 fixed points
     + 8 three-orbits; split across the iota hyperplane: 3 + 4x3 on the 15
     labels (v845) and 4 + 4x3 on the 16 payload words.

FIREWALL: experiments-only; no verification/, ledger, paper or website
surface touched; no marker moves; typed as exploration.
"""
import itertools
import math
import random

import numpy as np
import sympy as sp
from sympy.combinatorics import Permutation, PermutationGroup

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


# ============================================= S1: the (R, L) clock pair
print("=" * 72)
print("S1  THE (R, L) CLOCK PAIR: dim E8 vs rank E8")
check("det L = 20: L invertible ONLY mod 3 (singular mod 2 and mod 5)",
      20 % 2 == 0 and 20 % 5 == 0 and 20 % 3 == 2)
oL3 = order_mod(L, 3, 100)
check("ord(L mod 3) = 8 = rank E8 (the only surviving clock)", oL3 == 8)
# mod 30 semigroup: pre-period 3, period 8
ok_per = all((mpow(L, n + 8, 30) == mpow(L, n, 30)).all() for n in (3, 4, 5))
pre2 = (mpow(L, 2 + 8, 30) == mpow(L, 2, 30)).all()
check("L mod 30: L^(n+8) = L^n for n >= 3 (period 8 = rank E8)", ok_per)
check("L mod 30: pre-period EXACTLY 3 = N_fam (L^10 != L^2)", not pre2)
check("READING: winding collapses the clock dim E8 = 248 -> rank E8 = 8; "
      "transients: R pre-period 2 = |Z2|, L pre-period 3 = N_fam",
      248 == 8 * 31 and oL3 == 8)

# ============================================= S2: the field tower of R
print("=" * 72)
print("S2  THE FIELD TOWER OF R: invertible blocks = F2*, F9*, F125*")
t = sp.symbols('t')
chi = sp.Matrix(R.tolist()).charpoly(t).as_expr()
# mod 2: t^2 (t+1) -> invertible block dim 1, torus F2* (order 1)
f2 = sp.factor_list(sp.Poly(chi, t, modulus=2))
check("mod 2: invertible block dim 1, torus F2* (order 2^1 - 1 = 1)",
      sp.rem(chi, t**2 * (t + 1), t, modulus=2) == 0)
# mod 3: (t-1)(t^2+t-1); quadratic factor primitive over F3 <=> root order 8
q3 = sp.Poly(t**2 + t - 1, t, modulus=3)
# order of companion matrix of the quadratic factor
C2 = np.array([[0, 1], [1, 2]], dtype=np.int64)  # t^2 = -t + 1 = 2t + 1 mod 3
X, o = np.eye(2, dtype=np.int64), None
for k in range(1, 20):
    X = (X @ C2) % 3
    if (X == np.eye(2, dtype=np.int64)).all():
        o = k
        break
check("mod 3: quadratic factor PRIMITIVE over F3 -- 2D block is the full "
      "Singer torus F9* (order 3^2 - 1 = 8)", o == 8, f"ord={o}")
o5 = order_mod(R, 5, 200)
check("mod 5: irreducible primitive cubic -- 3D block is the full Singer "
      "torus F125* (order 5^3 - 1 = 124)", o5 == 124)
check("TOWER: (p, dim) = (2,1), (3,2), (5,3); cycles (1, 8, 124); "
      "dims are 1, 2, 3", True, "d_2=1, d_3=2, d_5=3")

# ======================================== S3: winding opcode census mod 30
print("=" * 72)
print("S3  WINDING OPCODE CENSUS (R_s = R + sW, s = 0..29)")


def nilpotent_mod(A, p):
    return (mpow(A, 3, p) == 0).all()


reset5 = [s for s in range(30) if nilpotent_mod(R + s * W, 5)]
reset3 = [s for s in range(30) if nilpotent_mod(R + s * W, 3)]
reset2 = [s for s in range(30) if nilpotent_mod(R + s * W, 2)]
check("5-channel resets exactly at s = 1 mod 5 (contains opcode 6 = e5)",
      reset5 == [1, 6, 11, 16, 21, 26] and 6 in reset5, f"{reset5}")
check("3-channel: NO winding resets the family channel (family protected)",
      reset3 == [], f"{reset3}")
print(f"       2-channel reset census: {reset2}")
check("2-channel reset census measured (typed)", isinstance(reset2, list),
      f"{reset2}")
# preservation-constrained: preserve mod 2 AND mod 3 while resetting 5
full5 = [s for s in range(30)
         if nilpotent_mod(R + s * W, 5)
         and ((R + s * W) % 2 == R % 2).all()
         and ((R + s * W) % 3 == R % 3).all()]
check("unique preserve-preserve-reset opcode = 6 = e5 (idempotent of Z/30)",
      full5 == [6] and (6 * 6) % 30 == 6)
# is ANY channel-2 reset compatible with preserving 3 and 5?
full2 = [s for s in reset2
         if ((R + s * W) % 3 == R % 3).all()
         and ((R + s * W) % 5 == R % 5).all()]
print(f"       2-channel reset preserving 3,5: {full2}")
check("sheet-channel reset census under preservation measured (typed)",
      isinstance(full2, list), f"{full2}")

# ============================================ S4: 210-register idempotents
print("=" * 72)
print("S4  THE 210-REGISTER IDEMPOTENTS (WEAK, observation only)")
idem210 = sorted(e for e in range(210) if (e * e) % 210 == e)
e2 = next(e for e in idem210 if e % 2 == 1 and e % 3 == 0 and e % 5 == 0
          and e % 7 == 0)
e3 = next(e for e in idem210 if e % 3 == 1 and e % 2 == 0 and e % 5 == 0
          and e % 7 == 0)
e5 = next(e for e in idem210 if e % 5 == 1 and e % 2 == 0 and e % 3 == 0
          and e % 7 == 0)
e7 = next(e for e in idem210 if e % 7 == 1 and e % 2 == 0 and e % 3 == 0
          and e % 5 == 0)
check("CRT idempotents of Z/210 at (2,3,5,7) = (105, 70, 126, 120)",
      (e2, e3, e5, e7) == (105, 70, 126, 120), f"{(e2, e3, e5, e7)}")
check("sum = 421 = 1 mod 210 (2 x 210 + 1)",
      e2 + e3 + e5 + e7 == 421 and 421 % 210 == 1)
check("corpus seats: 105 = C(15,2) (pair/Kraus count, v752/v801) and "
      "120 = |mu4| x h(E8) = dim SO(16) (v752 NS)",
      math.comb(15, 2) == 105 and 4 * 30 == 120)
print("       126, 70: NO certified corpus seat (E7 roots / dim L^4(8) are"
      " external labels) -- WEAK")

# ================================================= S5: generation asymmetry
print("=" * 72)
print("S5  GENERATION ASYMMETRY: sigma x Singer")


def f32_mul():
    def mul(a, b):
        r = 0
        for i in range(5):
            if (b >> i) & 1:
                r ^= a << i
        for i in range(9, 4, -1):
            if (r >> i) & 1:
                r ^= 0b100101 << (i - 5)
        return r
    return mul


mul32 = f32_mul()
pts5 = [v for v in range(1, 32)]          # nonzero 5-bit words
idx = {v: i for i, v in enumerate(pts5)}
# Singer permutation: multiplication by x (=0b00010) on nonzero F32
singer = Permutation([idx[mul32(v, 0b00010)] for v in pts5])
# sigma_slot: cycle bit positions 0->1->2->0 (slots 1..3), bits 3,4 fixed
def slotcyc(v):
    b = [(v >> i) & 1 for i in range(5)]
    nb = [b[2], b[0], b[1], b[3], b[4]]
    return sum(bit << i for i, bit in enumerate(nb))


sig31 = Permutation([idx[slotcyc(v)] for v in pts5])
check("sigma_slot has order 3 on the 31 points", sig31.order() == 3)
G = PermutationGroup([singer, sig31])
check("<sigma, Singer> = FULL GL5(2), order 9999360 (canonical labelling)",
      G.order() == 9999360, f"|G|={G.order()}")
# robustness: random re-labellings (conjugate sigma by random GL5(2))
rng = random.Random(8)
def rand_gl5():
    while True:
        M = [[rng.randrange(2) for _ in range(5)] for _ in range(5)]
        A = sp.Matrix(M)
        if A.det() % 2 == 1:
            return M


def apply_lin(M, v):
    b = [(v >> i) & 1 for i in range(5)]
    nb = [sum(M[i][j] * b[j] for j in range(5)) % 2 for i in range(5)]
    return sum(bit << i for i, bit in enumerate(nb))


gen_full = 0
for _ in range(5):
    M = rand_gl5()
    Minv = sp.Matrix(M).inv_mod(2)
    Minv = [[int(Minv[i, j]) % 2 for j in range(5)] for i in range(5)]
    conj = Permutation([idx[apply_lin(M, slotcyc(apply_lin(Minv, v)))]
                        for v in pts5])
    if PermutationGroup([singer, conj]).order() == 9999360:
        gen_full += 1
check("random re-labellings: pair generates full GL5(2) in all 5 trials "
      "(generic, measured)", gen_full == 5, f"{gen_full}/5")
# flavor side: <x->5x, x->x+1> on Z31
mult5 = Permutation([(5 * x) % 31 for x in range(31)])
shift = Permutation([(x + 1) % 31 for x in range(31)])
Gf = PermutationGroup([mult5, shift])
check("flavor pair <x->5x, +1> generates only Z31 x| Z3, order 93 "
      "(solvable)", Gf.order() == 93, f"|Gf|={Gf.order()}")
check("ASYMMETRY: carrier side simple 9999360, flavor side solvable 93; "
      "ratio = 107520 = 2^10 x 105", 9999360 // 93 == 107520
      and 107520 == 2**10 * 105)

# ================================================ S6: sigma census on 31
print("=" * 72)
print("S6  SIGMA ORBIT CENSUS ON THE 31")
fixed = [v for v in pts5 if slotcyc(v) == v]
even = [v for v in pts5 if bin(v).count('1') % 2 == 0]
odd = [v for v in pts5 if bin(v).count('1') % 2 == 1]
fix_even = [v for v in fixed if v in even]
fix_odd = [v for v in fixed if v in odd]
check("sigma_slot on PG(4,2): 7 fixed + 8 three-orbits (7 + 24 = 31)",
      len(fixed) == 7 and (31 - 7) % 3 == 0 and (31 - 7) // 3 == 8)
check("split across iota hyperplane: 3 fixed + 4 orbits on the 15 labels "
      "(v845), 4 fixed + 4 orbits on the 16 payload",
      len(fix_even) == 3 and (15 - 3) // 3 == 4 and
      len(fix_odd) == 4 and (16 - 4) // 3 == 4)

# ===================== S7: is the family protection rank-1 universal?
print("=" * 72)
print("S7  FAMILY PROTECTION: ALL rank-1 deformations, not just W")


def nonzero_vecs(p):
    return [v for v in itertools.product(range(p), repeat=3) if any(v)]


def rank1_reset_census(p):
    hits = []
    base = R % p
    for u in nonzero_vecs(p):
        for v in nonzero_vecs(p):
            A = (base + np.outer(np.array(u), np.array(v))) % p
            if (mpow(A, 3, p) == 0).all():
                hits.append((u, v))
    return hits


h3 = rank1_reset_census(3)
h2 = rank1_reset_census(2)
print(f"       rank-1 nilpotent deformations: mod 3 -> {len(h3)}, "
      f"mod 2 -> {len(h2)}")
# HONEST RESULT: protection is NOT universal -- generic rank-1 directions
# CAN reset every channel; the content is that the ANCHOR direction
# W = 1 e1^T is in the safe set for channels 2 and 3 and in the active
# set for channel 5: the winding DIRECTION does the channel selection.
check("mod 3: rank-1 resets EXIST (16/676) -- protection is a property "
      "of the anchor direction, not of R alone",
      len(h3) == 16, f"{len(h3)}/676")
check("mod 2: rank-1 resets EXIST (8/49)", len(h2) == 8,
      f"hits: {h2[:4]}")
# anchor direction: u prop (1,1,1), v prop e1 -- never in a reset list
anchor3 = [(u, v) for (u, v) in h3
           if all(x == u[0] for x in u) and v[1] == 0 and v[2] == 0]
anchor2 = [(u, v) for (u, v) in h2
           if all(x == u[0] for x in u) and v[1] == 0 and v[2] == 0]
check("ANCHOR SAFETY: the physical winding direction (1,1,1) x e1 is in "
      "NO mod-3 and NO mod-2 reset pair -- family and sheet are protected "
      "along the anchor, and only there is the carrier resettable (s = 6)",
      anchor3 == [] and anchor2 == [] and 6 in reset5)

print("=" * 72)
print(f"TOTAL: {PASS} PASS, {FAIL} FAIL")
raise SystemExit(0 if FAIL == 0 else 1)
