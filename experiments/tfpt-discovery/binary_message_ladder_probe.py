#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""binary_message_ladder_probe -- MESSAGE.LADDER.01: the E8 addressing
formula M_n = 15 * Delta p_n = 15 * 2^n, verified against the ACTUAL
objects, not just arithmetic.

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; work
package A of the v5.4 strategy, "formally close the finite normal form";
follow-up to v832 ANCHOR.AFFINE.01 and v833 GAUSSIAN.RAMLADDER.01):

The anchor a = (1,1,2) has power sums p_n = 2 + 2^n and binary shift
Delta p_n = p_n - 2 = 2^n (v832 [E]).  The MESSAGE LADDER is
      M_n = 15 * Delta p_n = 15 * 2^n,
where 15 = the number of nonzero classes of V = L/(1+i)L (the address
space, v833 R1.8 [E]).  Frozen rung claims, EACH verified against the
actual structure rebuilt from scratch (the Gaussian Construction-A E8 of
v833/v834, read-only machinery rebuilt inline):

 S1  LADDER ARITHMETIC (sympy, symbolic): p_n = 2 + 2^n, Delta p_n =
     2^n identically; M_0..M_4 = (15, 30, 60, 120, 240); the coda
     248 = 15*16 + 8 = M_4 + 8.

 S2  THE CARRIER OBJECT: rebuild the Gaussian E8 (Construction A over
     the unique mu4/sigma-invariant placement C*, 2 of 30); 240 roots,
     all norm 4; lattice rank 8 with [Z^8 : L] = 16 (HNF).

 S3  RUNG 4 (M_4 = 240 = |R(E8)|): the root census is EXACTLY 240 and
     distributes 240 = 15 x 16 over the 15 nonzero Gaussian classes
     (zero class empty) -- the 15 of the ladder IS the class count and
     16 = Delta p_4.  CODA: dim E8 = |R| + rank = 240 + 8 = 248 =
     15*16 + 8 against the actual census and the actual rank.

 S4  RUNG 3 (M_3 = 120 = |R+(E8)|): with the exact generic functional
     f(v) = Sum v_k 10^k (injective on {-2..2}^8 digits), the positive
     system has EXACTLY 120 roots and R = R+ u -R+.

 S5  RUNG 2 (M_2 = 60 = Gaussian root lines): the mu4-orbits
     {+-r, +-Jr} all have size 4; there are EXACTLY 60 lines; each of
     the 15 classes is a union of exactly 4 lines (v833 R1.9 rebuilt);
     each line contains exactly 2 of the 120 sign-pairs {+-r} (the
     structural doubling 60 -> 120 -> 240).

 S6  RUNG 1 (M_1 = 30 = h(E8), the Coxeter number FROM THE ROOT
     SYSTEM): the simple system of R+ (positive roots that are not a
     sum of two positive roots) has exactly 8 elements; its Cartan
     matrix <a_i, a_j>/2 is a valid connected simply-laced Cartan
     matrix with det = 1 and degree sequence [1,1,1,2,2,2,2,3] (the E8
     diagram); every positive root has nonnegative integer coordinates
     in the simple basis (exact Fraction solve); the height maximum is
     29, attained by a UNIQUE highest root with mark multiset
     {2,2,3,3,4,4,5,6}; h(E8) = 1 + 29 = 30, cross-checked against
     h = |R| / rank = 240/8 = 30.

 S7  INTERPRETATION ADDRESSES (typed, one structure per rung):
     M_0 = 15 = address space; M_1 = 30 = h(E8) = |R|/rank;
     M_2 = 60 = |R|/|mu4| (lines); M_3 = 120 = |R|/2 (sign pairs) =
     |R+|; M_4 = 240 = |R|; the rung-to-rung doubling is realized
     structurally for 60 -> 120 -> 240 (line = 2 sign-pairs, pair = 2
     roots) and the halving 60 -> 30 is |mu4| vs rank (rank 8 =
     2 * |mu4|).

 C   CONTROLS (must fire):
     C1 the wrong anchor a' = (1,2,2): Delta p'_n = 2^{n+1} - 1 gives
        M'_1..M'_4 = (45, 105, 225, 465) -- misses ALL FOUR targets;
        and the affine recursion p'_{n+1} = 2 p'_n - 2 fails (offset
        -1, v832 C2).
     C2 the wrong multiplier 14 (the weight-4 codeword count): 14*2^n
        = (28, 56, 112, 224) misses all four targets and 14*16 + 8 =
        232 != 248.
     C3 the wrong multiplier 16 (the class size): 16*2^n = (32, 64,
        128, 256) misses all four targets and 16*16 + 8 = 264 != 248.

KILLS (any one fires => MESSAGE-LADDER-MISMATCH-<type>):
  K1 ladder arithmetic fails                          -> ARITHMETIC
  K2 root census / class census / rank deviates       -> CENSUS
  K3 positive system != 120 or lines != 60            -> HALVING
  K4 the Coxeter computation from the root system     -> COXETER
     does not give 30 (simple system, highest root)
  K5 a control does not fire                          -> CONTROL-DEAD

VERDICT (frozen enum): MESSAGE-LADDER-EXACT /
MESSAGE-LADDER-MISMATCH-<type> / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface.
Exact integer/Fraction/sympy arithmetic; no floats, no RNG, no fit.

Sources (read-only, machinery rebuilt inline): verification/
v832_anchor_flavor_checksum.py (the affine ladder), v833_gaussian_
ramification_ladder.py (C*, census, lines), v834_pg32_flag_completion.py
(rebuild precedent), note_e8_gaussian_code / v689 (census provenance).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/binary_message_ladder_probe.py
"""
import hashlib
import itertools
import time

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("MESSAGE.LADDER.01 -- the E8 addressing formula M_n = 15 * 2^n")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ----------------------------------------------------------------------
section("S1: ladder arithmetic (sympy, symbolic)")
# ----------------------------------------------------------------------
n = sp.symbols("n")
pn = sp.Integer(2) + 2 ** n
dpn = pn - 2
a = (1, 1, 2)
p = lambda k: sum(sp.Integer(ai) ** k for ai in a)
check("S1.1 p_n(1,1,2) = 2 + 2^n (p_0..p_5 agree), Delta p_n = 2^n "
      "identically",
      all(p(k) == pn.subs(n, k) for k in range(6))
      and sp.simplify(dpn - 2 ** n) == 0, kill="K1")
M = {k: 15 * 2 ** k for k in range(5)}
check("S1.2 M_n = 15 * Delta p_n: (M_0..M_4) = %s == (15, 30, 60, 120, "
      "240)" % ([M[k] for k in range(5)],),
      [M[k] for k in range(5)] == [15, 30, 60, 120, 240], kill="K1")
check("S1.3 CODA: 248 = 15*16 + 8 = M_4 + 8 (arithmetic layer)",
      15 * 16 + 8 == 248 == M[4] + 8, kill="K1")

# ----------------------------------------------------------------------
section("S2: rebuild the Gaussian E8 (Construction A over C*, v833)")
# ----------------------------------------------------------------------
G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
          for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)


def code_image(code, perm):
    return frozenset(tuple(c[perm[k]] for k in range(8)) for c in code)


placements = set()
for perm in itertools.permutations(range(8)):
    placements.add(code_image(C_NAIVE, perm))
both = [c for c in placements
        if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
W0246 = (1, 0, 1, 0, 1, 0, 1, 0)
check("S2.1 placement census: %d placements, %d invariant under both "
      "pi_J and pi_sigma (v833 R1.3)" % (len(placements), len(both)),
      len(placements) == 30 and len(both) == 2, kill="K2")
CSTAR = next(c for c in both if W0246 in c)

ROOTS = []
for k in range(8):
    for s in (2, -2):
        v = [0] * 8
        v[k] = s
        ROOTS.append(tuple(v))
for c in (c for c in CSTAR if sum(c) == 4):
    sup = [k for k in range(8) if c[k]]
    for signs in itertools.product((1, -1), repeat=4):
        v = [0] * 8
        for k, s in zip(sup, signs):
            v[k] = s
        ROOTS.append(tuple(v))
check("S2.2 root census: %d roots, all distinct, all norm 4, all in L"
      % len(ROOTS),
      len(ROOTS) == 240 and len(set(ROOTS)) == 240
      and all(sum(x * x for x in r) == 4 for r in ROOTS)
      and all(tuple(abs(x) % 2 for x in r) in CSTAR for r in ROOTS),
      kill="K2")

gens = sp.Matrix([list(c) for c in sorted(CSTAR)]
                 + [[2 * (r == k) for k in range(8)]
                    for r in range(8)]).T
Bc = hermite_normal_form(gens)
detB = abs(Bc.det())
check("S2.3 lattice rank 8, HNF |det| = %d == 16 = [Z^8 : L] "
      "(v833 R1.10)" % detB,
      Bc.shape == (8, 8) and Bc.rank() == 8 and detB == 16, kill="K2")

# ----------------------------------------------------------------------
section("S3: RUNG 4 -- M_4 = 240 = |R(E8)| and the 15 x 16 census")
# ----------------------------------------------------------------------


def J_vec(v):
    out = [0] * 8
    for k in range(4):
        out[2 * k] = -v[2 * k + 1]
        out[2 * k + 1] = v[2 * k]
    return tuple(out)


def in_L(v):
    return tuple(x % 2 for x in v) in CSTAR


def in_pi2L(v):
    # x in (1+i)L  <=>  (1-J)x/2 in L
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L([x // 2 for x in w])


labels = {}
reps = []
for r in ROOTS:
    for li, rep in enumerate(reps):
        if in_pi2L(tuple(x - y for x, y in zip(r, rep))):
            labels[r] = li
            break
    else:
        labels[r] = len(reps)
        reps.append(r)
counts = sorted(sum(1 for r in ROOTS if labels[r] == li)
                for li in range(len(reps)))
check("S3.1 M_4 = 240 = |R(E8)|: the census distributes 240 = 15 x 16 "
      "over %d nonzero classes (sizes %s); zero class empty (%d/240 in "
      "(1+i)L) -- 15 = the ladder base, 16 = Delta p_4"
      % (len(reps), sorted(set(counts)),
         sum(1 for r in ROOTS if in_pi2L(r))),
      len(ROOTS) == M[4] and len(reps) == 15 and counts == [16] * 15
      and not any(in_pi2L(r) for r in ROOTS), kill="K2")
check("S3.2 CODA against the actual objects: dim E8 = |R| + rank = "
      "%d + %d = %d == 248 == 15*16 + 8" % (len(ROOTS), 8, len(ROOTS) + 8),
      len(ROOTS) + Bc.rank() == 248 == 15 * 16 + 8, kill="K2")

# ----------------------------------------------------------------------
section("S4: RUNG 3 -- M_3 = 120 = |R+(E8)| (exact generic functional)")
# ----------------------------------------------------------------------
WTS = [10 ** k for k in range(8)]


def fgen(r):
    return sum(r[k] * WTS[k] for k in range(8))


check("S4.1 f(v) = Sum v_k 10^k is injective-signed on the roots: "
      "f(r) != 0 for all 240 (digits |v_k| <= 2 < 10)",
      all(fgen(r) != 0 for r in ROOTS), kill="K3")
POS = [r for r in ROOTS if fgen(r) > 0]
POSSET = set(POS)
check("S4.2 M_3 = 120 = |R+|: positive system has %d roots and "
      "R = R+ u -R+" % len(POS),
      len(POS) == M[3]
      and all((r in POSSET) != (tuple(-x for x in r) in POSSET)
              for r in ROOTS), kill="K3")

# ----------------------------------------------------------------------
section("S5: RUNG 2 -- M_2 = 60 Gaussian root lines (mu4 orbits)")
# ----------------------------------------------------------------------
lines = set()
for r in ROOTS:
    lines.add(frozenset([r, J_vec(r), tuple(-x for x in r),
                         tuple(-x for x in J_vec(r))]))
check("S5.1 M_2 = 60 = Gaussian lines: %d mu4-orbits, all of size 4 "
      "(J free on roots, v833 R1.9)" % len(lines),
      len(lines) == M[2] and all(len(ln) == 4 for ln in lines),
      kill="K3")
check("S5.2 each of the 15 classes is a union of exactly 4 lines "
      "(60 = 15 x 4)",
      all(sum(1 for ln in lines if labels[next(iter(ln))] == li) == 4
          for li in range(15)), kill="K3")
pairs = {frozenset([r, tuple(-x for x in r)]) for r in ROOTS}
check("S5.3 STRUCTURAL DOUBLING 60 -> 120 -> 240: %d sign-pairs {+-r}; "
      "each line contains exactly 2 pairs; each pair exactly 2 roots"
      % len(pairs),
      len(pairs) == 120
      and all(sum(1 for pr in pairs if pr <= ln) == 2 for ln in lines),
      kill="K3")

# ----------------------------------------------------------------------
section("S6: RUNG 1 -- M_1 = 30 = h(E8) FROM the root system")
# ----------------------------------------------------------------------
SIMPLE = [r for r in POS
          if not any(tuple(x - y for x, y in zip(r, s)) in POSSET
                     for s in POSSET if s != r)]
check("S6.1 simple system: exactly %d simple roots (positive roots "
      "that are not a sum of two positive roots)" % len(SIMPLE),
      len(SIMPLE) == 8, kill="K4")


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


CART = [[ip(SIMPLE[i], SIMPLE[j]) // 2 for j in range(8)]
        for i in range(8)]
deg = sorted(sum(1 for j in range(8) if i != j and CART[i][j] != 0)
             for i in range(8))
adj_ok = all(CART[i][i] == 2 and all(CART[i][j] in (0, -1)
                                     for j in range(8) if j != i)
             for i in range(8))
# connectivity
seen = {0}
stack = [0]
while stack:
    u = stack.pop()
    for v2 in range(8):
        if v2 not in seen and CART[u][v2] == -1:
            seen.add(v2)
            stack.append(v2)
detC = sp.Matrix(CART).det()
check("S6.2 Cartan matrix <a_i,a_j>/2: diag 2, offdiag in {0,-1}, "
      "connected, det = %s == 1, degree sequence %s == [1,1,1,2,2,2,2,3]"
      " -- the E8 diagram" % (detC, deg),
      adj_ok and len(seen) == 8 and detC == 1
      and deg == [1, 1, 1, 2, 2, 2, 2, 3], kill="K4")

S8 = sp.Matrix([[SIMPLE[j][i] for j in range(8)] for i in range(8)])
S8inv = S8.inv()
heights = {}
all_int = True
for r in POS:
    co = S8inv * sp.Matrix(r)
    if not all(x.is_Integer and x >= 0 for x in co):
        all_int = False
    heights[r] = sum(co)
hmax = max(heights.values())
top = [r for r in POS if heights[r] == hmax]
marks = sorted((S8inv * sp.Matrix(top[0])) if top else [])
check("S6.3 every positive root has nonnegative INTEGER simple-root "
      "coordinates (exact); height max = %s, attained by %d root(s)"
      % (hmax, len(top)),
      all_int and hmax == 29 and len(top) == 1, kill="K4")
check("S6.4 highest-root marks (sorted) = %s == [2,2,3,3,4,4,5,6] "
      "(sum 29)" % (marks,),
      marks == [2, 2, 3, 3, 4, 4, 5, 6] and sum(marks) == 29, kill="K4")
h_cox = 1 + hmax
check("S6.5 M_1 = 30 = h(E8): 1 + ht(theta) = %d == 30 == |R|/rank = "
      "%d/8 (both readings of the Coxeter number agree)"
      % (h_cox, len(ROOTS)),
      h_cox == M[1] == len(ROOTS) // 8, kill="K4")

# ----------------------------------------------------------------------
section("S7: interpretation addresses (typed, one structure per rung)")
# ----------------------------------------------------------------------
check("S7.1 RUNG TABLE: M_0 = 15 = address space (classes); M_1 = 30 = "
      "h(E8) = |R|/rank; M_2 = 60 = |R|/|mu4| (lines); M_3 = 120 = "
      "|R|/2 (sign pairs) = |R+|; M_4 = 240 = |R|",
      len(reps) == M[0] and h_cox == M[1] == len(ROOTS) // 8
      and len(lines) == M[2] == len(ROOTS) // 4
      and len(pairs) == M[3] == len(ROOTS) // 2 == len(POS)
      and len(ROOTS) == M[4], kill="K2")
check("S7.2 the halving 60 -> 30 is |mu4| vs rank: lines = |R|/4, "
      "h = |R|/8, rank 8 = 2 * |mu4| = 2 * 4",
      len(lines) == len(ROOTS) // 4 and h_cox == len(ROOTS) // 8
      and 8 == 2 * 4, kill="K2")

# ----------------------------------------------------------------------
section("C: controls (must fire)")
# ----------------------------------------------------------------------
TARGETS = {30, 60, 120, 240}
ap = (1, 2, 2)
pp = lambda k: sum(ai ** k for ai in ap)
Mw = [15 * (pp(k) - 2) for k in range(1, 5)]
viol = [pp(k + 1) - (2 * pp(k) - 2) for k in range(4)]
check("C1 FIRES: wrong anchor (1,2,2): M'_1..M'_4 = %s -- misses all "
      "four targets; recursion offset %s != 0" % (Mw, viol),
      not (set(Mw) & TARGETS) and all(v == 1 for v in viol), kill="K5")
M14 = [14 * 2 ** k for k in range(1, 5)]
check("C2 FIRES: wrong multiplier 14 (the weight-4 codeword count): "
      "%s misses all four targets; 14*16 + 8 = %d != 248"
      % (M14, 14 * 16 + 8),
      not (set(M14) & TARGETS) and 14 * 16 + 8 != 248
      and sum(1 for c in CSTAR if sum(c) == 4) == 14, kill="K5")
M16 = [16 * 2 ** k for k in range(1, 5)]
check("C3 FIRES: wrong multiplier 16 (the class size): %s misses all "
      "four targets; 16*16 + 8 = %d != 248" % (M16, 16 * 16 + 8),
      not (set(M16) & TARGETS) and 16 * 16 + 8 != 248, kill="K5")

# ----------------------------------------------------------------------
section("VERDICT")
# ----------------------------------------------------------------------
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
if not controls_ok:
    VERDICT = "CONTROL-DEAD"
elif KILLS:
    VERDICT = "MESSAGE-LADDER-MISMATCH-%s" % KILLS[0]
else:
    VERDICT = "MESSAGE-LADDER-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
print("  * tfpt_1 budget lines |R(E8)| = 240 / dim E8 = 248 / h = 30 and")
print("    v832 S3.1-S3.3 (240 = p1p2p3, 30 = p2p3/2, 248 = 240 + q3):")
print("    ALL are instances of ONE formula M_n = 15 * Delta p_n, with")
print("    each rung realized by a NAMED structure of the SAME object")
print("    (address space / Coxeter number / Gaussian lines / positive")
print("    system / root census).")
print("  * v833 R1.8/R1.9 (census 15 x 16, 60 lines): the 15 and the 60")
print("    are rungs 0 and 2 of the ladder.")
print("  * NEW here: h(E8) = 30 certified from the rebuilt root system")
print("    (simple system -> highest root height 29 -> h = 30), not")
print("    cited; the doubling chain 60 -> 120 -> 240 typed structurally.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT == "MESSAGE-LADDER-EXACT") else 1)
