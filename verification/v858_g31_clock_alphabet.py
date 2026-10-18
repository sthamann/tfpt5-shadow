#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v858 -- E8.G31.CLOCK_ALPHABET.01: the E8 audits, part II -- the compiler clock alphabet is a NORMAL FORM of G31: Deg(G31)/4 = {2, 3, 5, 6} = {|Z2|, N_fam, g_car, |R+(A3)|} with the audit identity (sum d/4)(sum (d-1)/4) = 16 x 15 = 240 REALIZED on the roots, (8, 12, 20, 24) the UNIQUE integer quadruple with product 46080 and sum 64, the 607-group rank-4 kill scan typed (G31 the SOLE full-battery passer; weak-triple and raw-sum-64 impostors named), and the W(D5) x W(A3) fence re-killed with COMPUTED centers 4 vs 1, ONE module from one probe (19/19 checks, zero fails, verdict CLOCK-ALPHABET-SELECTIVE; discovery probe g31_clock_alphabet_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~4 s).  THE REBUILD (warded against v634): 240 doubled-integer E8 roots, J free of order 4 with EXACTLY 60 Gaussian lines, 60 order-2 reflections (one per line, all distinct), BFS closure |G| = 46080 = 8 x 12 x 20 x 24 = prod Deg(G31), every element complex-linear (commutes with J), the base certified by an exact adjugate identity (det = -512), and the EXACT reflection census: 60 elements with rank(M - I) = 2, all order 2, all generators -- ZERO quasi-reflections (v634 TEST2 reproduced; sum (d-1) = 60 anchors the degrees; the Molien uniqueness CITED, not recomputed).  THE NORMAL FORM: Deg(G31) = |mu4| x {2, 3, 5, 6} with gcd = 4 = |mu4|, lcm = 120 = |R+(E8)|, lcm/gcd = 30 = h(E8); sum d/4 = 16 (the class size) and sum (d-1)/4 = 15 (the classes) with 16 x 15 = 240 = |R(E8)| -- and the 60/4 = 15 line is REALIZED on the roots (the 15 classes at 4 lines per class, the same 15 x 16 census as the package-A code side); the alphabet {2, 3, 5, 6} = {|Z2|, N_fam, g_car, |R+(A3)|} is EXACTLY the compiler clock alphabet; the Springer footprint is typed (exponents (7, 11, 19, 23) all = 3 mod 4; the d/4-clock realization x^{d/4} in {J, J^3} cited v654).  THE ARITHMETIC PIN (measured): the integer-quadruple census with product 46080 and sum 64 returns EXACTLY [(8, 12, 20, 24)].  THE KILL SCAN (the selectivity theorem, 607 groups): the full rank-4 Shephard-Todd catalog (integrity: prod(degrees) = |G| for every entry -- a table second-source check) is run through the seven-gate battery (product, raw sum 64, gcd normalization, alphabet set, lcm, lcm/gcd = 30, audit identity): G31 is the SOLE full-battery passer; the weak-triple (gcd/lcm/30) impostors are typed by name (G(20,10,4), G(20,20,4), G29) and the raw-sum-64 coincidences too (G(8,2,4), G(10,10,4), G30 = W(H4)); the family boundary is verified in range (no G(m,p,4) matches the alphabet for any 2 <= m <= 120, with the typed argument: 3m/g <= 6 forces g >= m/2, then {d/g} contains 1 or 4); THE HONESTY LINE (typed, no kill): degree-only audits cannot separate G31 from the reducible torus Z8 x Z12 x Z20 x Z24 (identical degrees by construction) -- the frozen scope is the irreducible rank-4 list; the controls fire (the perturbed quadruple (8,12,20,28) fails the battery; the wrong normalization gcd 2 breaks the alphabet).  THE FENCE (re-killed with a computed one-number invariant): |W(D5)| x |W(A3)| = 1920 x 24 = 46080 = |G31| stays NUMEROLOGY -- the computed |Z(G31)| = 4 with Z = <J> = mu4, versus |Z(W(D5) x W(A3))| = 1 x 1 = 1 (odd-rank D5: -1 not in W(D5); Z(S4) = 1): NOT isomorphic, NOT a decomposition (v634 T1.3/T1.4/T1.5 CITED for the full structural refutation: G = (Z4 o 2^{1+4}).Sp4(2) and W(D5) embeds in NO rank-4 group).  The module is an exact-arithmetic corpus compression and a selectivity audit of a DEPLOYED object (v634/v654) -- a normal form plus an armed kill rule, no new physical claim, no marker moves.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe g31_clock_alphabet_probe.py (19/19,
verdict CLOCK-ALPHABET-SELECTIVE), 2026-08-08, re-run identically
at promotion.  ROUND-31 EMBEDDING CONVENTION: the frozen source is
embedded BYTE-EXACT (raw string below) and executed verbatim in an
isolated module namespace registered under its canonical import
name -- the printed FROZEN_SPEC SHA-256 reproduces exactly, and
when the original file is present the harness verifies
byte-equality (provenance ward inside the pattern gate).  The
original probe file lives verbatim in experiments/tfpt-discovery/.

FIREWALL: exact integer / Fraction arithmetic in every load-bearing
identity (the group closure over exact integer matrices; the
catalog censuses in integers); no zeros, no prime tables.
NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source (embedded BYTE-EXACT, raw string)
_SRC_G31 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""g31_clock_alphabet_probe -- E8.G31.CLOCK_ALPHABET.01 (audit package B
of the 2026-08-08 morning analysis): the G31 degree normal form
Deg(G31) = 4 x {2,3,5,6}, its checksum battery, the kill scan over ALL
rank-4 complex reflection groups, and the fence on the numerological
|G31| = |W(D5)| x |W(A3)|.

FROZEN CLAIMS (2026-08-08, frozen + SHA-hashed before first run):

 S1  REBUILD FROM FIRST PRINCIPLES (v634 S0/S1 machinery rebuilt
     inline; exact integer arithmetic): the 240 standard-model E8
     roots (doubled coordinates), J free of order 4, EXACTLY 60
     Gaussian lines; the 60 order-2 unitary reflections R_v generate a
     group G with |G| = 46080 (BFS closure, exact); every element of G
     commutes with J (complex-linear); the EXACT reflection census:
     the elements with real rank(M - I) = 2 (= complex rank 1: all
     reflections AND quasi-reflections) number EXACTLY 60, all of
     order 2 and all equal to the 60 generators (zero zeta = i
     quasi-reflections -- v634 TEST2 reproduced exactly, here by
     integer-trace prefilter + fraction-free integer rank, no floats).
     Shephard-Todd anchors against the claimed degrees (8,12,20,24):
     prod d_i = 46080 = |G| and sum (d_i - 1) = 60 = #reflections.
     The degrees themselves are CITED from the deployed Molien
     computation (v634 TEST2: (8,12,20,24) unique via Molien); as an
     arithmetic pin the census of ALL integer quadruples
     2 <= d1 <= d2 <= d3 <= d4 with product 46080 and sum 64 is
     computed exactly and reported (uniqueness measured, not assumed).
 S2  THE NORMAL FORM + CHECKSUMS (exact): Deg(G31) = (8,12,20,24) =
     4 x (2,3,5,6); gcd = 4 = |mu4|; lcm = 120 = |R+(E8)| (cross-
     checked as 240/2 against the S1 root census); lcm/gcd = 30 =
     h(E8); sum d_i / 4 = 16 (the Gaussian class size); sum (d_i-1)/4
     = 15 (the nonzero classes; realized structurally: the 60
     reflections = the 60 lines distribute 4 per class over the 15
     classes of L/(1+i)L, computed on the SAME roots); the audit
     identity (sum d_i/4) x (sum (d_i-1)/4) = 16 x 15 = 240 = |R(E8)|
     (the package-A census law); the alphabet {2,3,5,6} =
     {|Z2|, N_fam, g_car, |R+(A3)|}; the Springer footprint: exponents
     (7,11,19,23) all = 3 mod 4 (the v654 uniform reason; the d/4
     Springer clock theorem x^(d/4) in {J, J^3} is CITED [v654], its
     arithmetic footprint d/4 = the alphabet re-verified here).
 S3  THE CONTROL SCAN (the kill test; degrees tabulated, hard-coded
     with citations -- Shephard-Todd 1954 Table VII / Lehrer-Taylor):
     ALL rank-4 irreducible complex reflection groups:
       - the imprimitive family G(m,p,4), p | m, 2 <= m <= 120,
         degrees (m, 2m, 3m, 4m/p); |G| = 24 m^4 / p;
       - G(1,1,5) = W(A4) = S5, degrees (2,3,4,5);
       - exceptional: G28 = W(F4) (2,6,8,12) order 1152;
         G29 (4,8,12,20) order 7680; G30 = W(H4) (2,12,20,30) order
         14400; G31 (8,12,20,24) order 46080; G32 (12,18,24,30) order
         155520.  Table integrity: prod d_i = |G| for every entry.
     THE BATTERY (all exact Fractions): B1 gcd = 4; B2 lcm = 120;
     B3 lcm/gcd = 30; B4 sum d/gcd = 16; B5 sum(d-1)/gcd = 15;
     B6 (sum d/g)(sum(d-1)/g) = 240; B7 quotient alphabet multiset
     {d/g} = {2,3,5,6}.
     KILL RULE: if ANY foreign group passes the FULL battery, the
     package is a weak audit -> CLOCK-ALPHABET-WEAK with the impostors
     typed.  The partial-pass census is reported honestly either way
     (expected near-misses to be measured: the weak triple B1-B3 and
     the raw-sum-64 coincidence of W(H4)).  FAMILY BOUNDARY (typed
     argument + verified in range): no G(m,p,4) can ever pass B7 --
     the alphabet forces 3m/g <= 6, so g >= m/2, and then the quotient
     multiset contains 1 or 4; the finite scan bound 120 is therefore
     only a reporting bound, not a completeness gap.
     HONESTY LINE (typed, no kill): a degree-multiset audit is
     tautologically blind to the REDUCIBLE rank-4 torus
     Z8 x Z12 x Z20 x Z24 (identical degrees by construction); the
     frozen scan scope is the irreducible Shephard-Todd list.
     MUST-BREAK CONTROLS: X1 the perturbed quadruple (8,12,20,28)
     fails the battery; X2 the wrong normalization (divide by 2:
     alphabet (4,6,10,12)) fails B7.
 S4  THE FENCE (the checked negative, no recompute of the group
     theory): |G31| = 46080 = 1920 x 24 = |W(D5)| x |W(A3)| with
     1920 = 2^4 5! and 24 = 4! (arithmetic re-verified) -- but NOT a
     group decomposition: the center of G computed HERE exactly
     |Z(G31)| = 4 (= <J> = mu4), while |Z(W(D5) x W(A3))| = 1
     (W(D5): -1 has an odd number of sign flips, so -1 is not in
     W(D5) and Z(W(D5)) = 1 for odd rank; Z(S4) = 1) -- an invariant
     kill reproduced with one computed number; the deployed structural
     refutation CITED: v634 T1.3 (order spectrum/abelianization
     kills), T1.4 (true structure G = (Z4 o 2^{1+4}).Sp4(2), computed
     not cited there), T1.5 (W(D5) has NO faithful complex rep of
     dim <= 4, so it embeds in NO rank-4 reflection group).

KILLS (any one fires => typed failure):
  K1 rebuild / closure / reflection census breaks   -> G31-REBUILD-BROKEN
  K2 a checksum of S2 fails                         -> CHECKSUM-BROKEN
  K4 a must-break control does not fire             -> CONTROL-DEAD
  K5 the fence arithmetic / center kill breaks      -> FENCE-BROKEN

VERDICT (frozen enum): CLOCK-ALPHABET-SELECTIVE (G31 unique on the full
battery in the scanned list) / CLOCK-ALPHABET-WEAK (typed impostor
census) / typed failure (G31-REBUILD-BROKEN, CHECKSUM-BROKEN,
CONTROL-DEAD, FENCE-BROKEN).

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact integer/Fraction arithmetic in every
decision (numpy int16/int64 permutation/trace algebra is exact); no
floats, no RNG, no fits.  NO physics claim.  Runtime cap: minutes.

Sources (read-only, machinery rebuilt inline): verification/
v634_st31_structure.py (S0/S1 root+reflection machinery, Molien
degrees, T1.2-T1.5 fence), v654_st31_degree8.py (d/4 Springer clock
theorem, exponents mod 4), v647_st31_degree24.py (Springer method),
v649_discipline_audit.py (degree citation), v833/v844 (class census),
Shephard-Todd 1954 / Lehrer-Taylor 2009 (degree tables).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/g31_clock_alphabet_probe.py
"""
import hashlib
import itertools
import time
from collections import Counter
from fractions import Fraction as Fr
from math import gcd, lcm

import numpy as np

T0 = time.time()
CHECKS = []
KILLS = []
N240 = 240

# compiler integers (P1/P2 derived; tfpt_constants read-only values)
Z2 = 2          # |Z_2| sheet
N_FAM = 3       # families
G_CAR = 5       # carrier rank (P2)
RP_A3 = 6       # |R+(A3)|
MU4 = 4         # |mu4|
H_E8 = 30       # Coxeter number
RP_E8 = 120     # |R+(E8)|
R_E8 = 240      # |R(E8)|
DEG31 = (8, 12, 20, 24)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("=" * 74)
print("E8.G31.CLOCK_ALPHABET.01 -- Deg(G31) = 4 x {2,3,5,6}: normal form,")
print("checksum battery, rank-4 kill scan, and the W(D5) x W(A3) fence")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ======================================================================
section("S1: rebuild -- roots, J, 60 reflections, BFS closure, census")
# ======================================================================
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
check("S1.1 240 doubled-integer E8 roots reconstructed (v634 S0)",
      RD.shape == (240, 8), kill="K1")


def J_vec(x):
    out = np.empty_like(x)
    out[0::2] = -x[1::2]
    out[1::2] = x[0::2]
    return out


def perm_from_map(f):
    return np.array([ridx[tuple(int(a) for a in f(RD[i]))]
                     for i in range(N240)], dtype=np.int16)


Jperm = perm_from_map(J_vec)
IDP = np.arange(N240, dtype=np.int16)
JRD = np.array([J_vec(RD[i]) for i in range(N240)], dtype=np.int64)

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
check("S1.2 J free of order 4; EXACTLY 60 Gaussian lines",
      not np.any(Jperm == IDP) and len(line_reps) == 60, kill="K1")

refl_perms = []
for a in range(60):
    vi = line_reps[a]
    re4, im4 = RD @ RD[vi], RD @ JRD[vi]
    assert np.all(re4 % 4 == 0) and np.all(im4 % 4 == 0)
    re, im = re4 // 4, im4 // 4
    Y = RD - re[:, None] * RD[vi][None, :] - im[:, None] * JRD[vi][None, :]
    refl_perms.append(np.array([ridx[tuple(int(t) for t in Y[i])]
                                for i in range(N240)], dtype=np.int16))
ok_inv = all(np.array_equal(p[p], IDP) and not np.array_equal(p, IDP)
             for p in refl_perms)
distinct60 = len({p.tobytes() for p in refl_perms}) == 60
check("S1.3 60 order-2 reflections built (one per line), all distinct",
      ok_inv and distinct60, kill="K1")

pool = [IDP.copy()]
seen = {IDP.tobytes(): 0}
frontier = [IDP]
while frontier:
    nxt = []
    for p in frontier:
        for g in refl_perms:
            q = g[p]
            key = q.tobytes()
            if key not in seen:
                seen[key] = len(pool)
                pool.append(q)
                nxt.append(q)
    frontier = nxt
NG = len(pool)
check("S1.4 BFS closure: |G| = %d == 46080 == 8*12*20*24 = prod Deg(G31)"
      % NG, NG == 46080 == 8 * 12 * 20 * 24, kill="K1")

POOL = np.stack(pool)                       # 46080 x 240 int16
lhs = POOL[:, Jperm]                        # g o J
rhs = Jperm[POOL]                           # J o g
check("S1.5 EVERY element commutes with J (complex-linear): %s"
      % bool(np.all(lhs == rhs)), bool(np.all(lhs == rhs)), kill="K1")
del lhs, rhs


def int_rank(rows):
    """fraction-free (Bareiss) integer rank; exact divisions asserted."""
    M = [list(map(int, r)) for r in rows]
    n, m = len(M), len(M[0])
    rank = 0
    prev = 1
    for col in range(m):
        if rank >= n:
            break
        piv = next((r for r in range(rank, n) if M[r][col] != 0), None)
        if piv is None:
            continue
        if piv != rank:
            M[rank], M[piv] = M[piv], M[rank]
        p = M[rank][col]
        for r in range(rank + 1, n):
            f = M[r][col]
            if f == 0 and prev == 1:
                continue
            for c in range(m):
                num = M[r][c] * p - f * M[rank][c]
                q, rmd = divmod(num, prev)
                assert rmd == 0
                M[r][c] = q
        prev = p
        rank += 1
    return rank


basis_idx = []
for i in range(N240):
    if int_rank([RD[j] for j in basis_idx] + [RD[i]]) > len(basis_idx):
        basis_idx.append(i)
    if len(basis_idx) == 8:
        break
B = np.array([RD[j] for j in basis_idx], dtype=np.int64)     # rows
detB = int(round(np.linalg.det(B.astype(float))))
Badj = np.array(
    [[(-1) ** (i + j)
      * int(round(np.linalg.det(np.delete(np.delete(B, j, 0), i, 1)
                                .astype(float))))
      for j in range(8)] for i in range(8)], dtype=np.int64)
# exact integrity of the float-assisted adjugate: B @ adj == detB * I
check("S1.6 basis of 8 spanning roots; adjugate certified exactly: "
      "Badj . B == det(B) I with det(B) = %d != 0" % detB,
      len(basis_idx) == 8 and detB != 0
      and np.array_equal(Badj @ B, detB * np.eye(8, dtype=np.int64)),
      kill="K1")

X_all = RD[POOL[:, basis_idx]].astype(np.int64)       # NG x 8 x 8 (rows)
# real trace of M_g: rows transform X = M-action; tr(M) = tr(Badj @ X)/detB
tr_num = np.einsum("ij,nji->n", Badj, X_all)
assert np.all(tr_num % detB == 0)
traces = tr_num // detB
cand = np.nonzero((traces >= 4) & (traces <= 7))[0]
refl_found = []
for i in cand:
    if int_rank((X_all[i] - B).tolist()) == 2:
        refl_found.append(int(i))
orders_ok = all(np.array_equal(POOL[i][POOL[i]], IDP) for i in refl_found)
refl_keys = {POOL[i].tobytes() for i in refl_found}
gen_keys = {p.tobytes() for p in refl_perms}
check("S1.7 EXACT reflection census: %d elements with rank(M - I) = 2 "
      "(trace prefilter %d candidates), all order 2, and they ARE the "
      "60 generators => zero quasi-reflections (v634 TEST2 reproduced); "
      "sum(d-1) = 60 anchors the degrees"
      % (len(refl_found), len(cand)),
      len(refl_found) == 60 and orders_ok and refl_keys == gen_keys
      and sum(d - 1 for d in DEG31) == 60, kill="K1")

quads = []
divs = [d for d in range(2, 46081) if 46080 % d == 0]
for d1 in divs:
    if d1 ** 4 > 46080 or d1 > 16:
        continue
    for d2 in divs:
        if d2 < d1 or 46080 % (d1 * d2) != 0:
            continue
        rest = 46080 // (d1 * d2)
        for d3 in divs:
            if d3 < d2 or rest % d3 != 0:
                continue
            d4 = rest // d3
            if d4 >= d3 and d1 + d2 + d3 + d4 == 64:
                quads.append((d1, d2, d3, d4))
check("S1.8 arithmetic pin (measured): integer quadruples with product "
      "46080 and sum 64: %s -- (8,12,20,24) %s; the Molien uniqueness "
      "is CITED (v634 TEST2)"
      % (quads, "unique" if quads == [DEG31] else "NOT unique (typed)"),
      DEG31 in quads, kill="K1")

# ======================================================================
section("S2: normal form + checksum battery + structural realization")
# ======================================================================
g31_gcd = gcd(*DEG31)
g31_lcm = lcm(*DEG31)
alpha = tuple(d // g31_gcd for d in DEG31)
check("S2.1 Deg(G31) = 4 x (2,3,5,6): quotients %s; gcd = %d == |mu4|; "
      "lcm = %d == |R+(E8)| == 240/2 (census cross-check); lcm/gcd = %d "
      "== h(E8)" % (alpha, g31_gcd, g31_lcm, g31_lcm // g31_gcd),
      alpha == (2, 3, 5, 6) and g31_gcd == MU4 and g31_lcm == RP_E8
      and g31_lcm == N240 // 2 and g31_lcm // g31_gcd == H_E8, kill="K2")
check("S2.2 sums: sum d/4 = %d == 16 (class size); sum(d-1)/4 = %d == 15 "
      "(classes); AUDIT IDENTITY 16 x 15 = %d == 240 = |R(E8)|"
      % (sum(DEG31) // 4, sum(d - 1 for d in DEG31) // 4,
         (sum(DEG31) // 4) * (sum(d - 1 for d in DEG31) // 4)),
      sum(DEG31) // 4 == 16 and sum(d - 1 for d in DEG31) // 4 == 15
      and 16 * 15 == R_E8, kill="K2")


def in_L_std(v):
    if all(t % 2 == 0 for t in v):
        return sum(t // 2 for t in v) % 2 == 0
    if all(t % 2 == 1 for t in v):
        return sum(v) % 4 == 0
    return False


def in_pi2L_std(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L_std([x // 2 for x in w])


reps = []
label = {}
for i in range(N240):
    r = tuple(int(t) for t in RD[i])
    for li, rep in enumerate(reps):
        if in_pi2L_std(tuple(x - y for x, y in zip(r, rep))):
            label[i] = li
            break
    else:
        label[i] = len(reps)
        reps.append(r)
cls_sizes = sorted(Counter(label.values()).values())
lines_per_class = Counter()
for a in range(60):
    lines_per_class[label[line_reps[a]]] += 1
line_class_ok = (len(reps) == 15 and cls_sizes == [16] * 15
                 and sorted(lines_per_class.values()) == [4] * 15
                 and not any(in_pi2L_std(tuple(int(t) for t in RD[i]))
                             for i in range(N240)))
check("S2.3 STRUCTURAL REALIZATION on the same roots: 15 classes x 16 "
      "(zero empty); the 60 reflections = the 60 lines, 4 per class "
      "=> sum(d-1)/|mu4| = 60/4 = 15 IS the class count",
      line_class_ok, kill="K2")

check("S2.4 alphabet {2,3,5,6} == {|Z2|, N_fam, g_car, |R+(A3)|} = "
      "{%d,%d,%d,%d}; Springer footprint: exponents (7,11,19,23) all "
      "= 3 mod 4 (v654 uniform reason; d/4-clock x^(d/4) in {J,J^3} "
      "CITED v654)" % (Z2, N_FAM, G_CAR, RP_A3),
      set(alpha) == {Z2, N_FAM, G_CAR, RP_A3}
      and all((d - 1) % 4 == 3 for d in DEG31), kill="K2")

# ======================================================================
section("S3: the kill scan over ALL rank-4 complex reflection groups")
# ======================================================================
# Degrees: Shephard-Todd 1954 Table VII / Lehrer-Taylor 2009 App. D.
CATALOG = []
for m in range(2, 121):
    for p in range(1, m + 1):
        if m % p == 0:
            degs = tuple(sorted((m, 2 * m, 3 * m, 4 * m // p)))
            CATALOG.append(("G(%d,%d,4)" % (m, p), degs, 24 * m ** 4 // p))
CATALOG.append(("G(1,1,5)=W(A4)=S5", (2, 3, 4, 5), 120))
CATALOG.append(("G28=W(F4)", (2, 6, 8, 12), 1152))
CATALOG.append(("G29", (4, 8, 12, 20), 7680))
CATALOG.append(("G30=W(H4)", (2, 12, 20, 30), 14400))
CATALOG.append(("G31", DEG31, 46080))
CATALOG.append(("G32", (12, 18, 24, 30), 155520))
table_ok = all(d[0] * d[1] * d[2] * d[3] == order
               for _, d, order in CATALOG)
check("S3.1 catalog integrity: %d groups; prod(degrees) == |G| for "
      "every entry (table second-source check)" % len(CATALOG),
      table_ok, kill="K2")


def battery(degs):
    g = gcd(*degs)
    l = lcm(*degs)
    S = sum(degs)
    return (g == MU4,
            l == RP_E8,
            Fr(l, g) == H_E8,
            Fr(S, g) == 16,
            Fr(S - 4, g) == 15,
            Fr(S, g) * Fr(S - 4, g) == R_E8,
            sorted(Fr(d, g) for d in degs) == [2, 3, 5, 6])


results = {name: battery(d) for name, d, _ in CATALOG}
full = [name for name, v in results.items() if all(v)]
weak3 = [name for name, v in results.items()
         if v[0] and v[1] and v[2] and name != "G31"]
sum64 = [name for name, d, _ in CATALOG
         if sum(d) == 64 and name != "G31"]
fam_alpha = [name for name, d, _ in CATALOG
             if name.startswith("G(") and name.endswith(",4)")
             and results[name][6]]
print("      full-battery passers: %s" % full)
print("      weak-triple (B1&B2&B3) foreign passers: %s" % weak3)
print("      raw-sum-64 foreign coincidences: %s" % sum64)
check("S3.2 SELECTIVITY CENSUS: G31 passes the full battery; foreign "
      "full-battery passers: %d; weak-triple impostors typed: %s; "
      "raw-sum-64 coincidence typed: %s"
      % (len(full) - 1, weak3, sum64),
      "G31" in full, kill="K2")
check("S3.3 FAMILY BOUNDARY verified in range: no G(m,p,4) matches the "
      "alphabet B7 for any 2 <= m <= 120 (found: %s); typed argument: "
      "3m/g <= 6 forces g >= m/2, then {d/g} contains 1 or 4"
      % fam_alpha, fam_alpha == [], kill="K2")
print("      HONESTY LINE (typed, no kill): degree-only audits cannot")
print("      separate G31 from the reducible torus Z8 x Z12 x Z20 x Z24")
print("      (identical degrees by construction); frozen scope = the")
print("      irreducible Shephard-Todd rank-4 list.")

X1 = battery((8, 12, 20, 28))
X2 = sorted(Fr(d, 2) for d in DEG31)
check("X1 FIRES: perturbed quadruple (8,12,20,28) fails the battery "
      "(pass vector %s)" % (X1,), not all(X1), kill="K4")
check("X2 FIRES: wrong normalization (gcd 2): alphabet %s != [2,3,5,6]"
      % X2, X2 != [2, 3, 5, 6], kill="K4")

# ======================================================================
section("S4: the fence -- |G31| = |W(D5)| x |W(A3)| is NOT a decomposition")
# ======================================================================
wd5 = 2 ** 4 * 120
wa3 = 24
check("S4.1 order identity re-verified: |W(D5)| x |W(A3)| = %d x %d = "
      "%d == 46080 == |G| == prod Deg(G31)" % (wd5, wa3, wd5 * wa3),
      wd5 * wa3 == 46080 == NG, kill="K5")

GEN_ARRS = refl_perms
alive = np.ones(NG, dtype=bool)
for g in GEN_ARRS:
    idx = np.nonzero(alive)[0]
    if len(idx) == 0:
        break
    lhs = POOL[idx][:, g]
    rhs = g[POOL[idx]]
    alive[idx] &= np.all(lhs == rhs, axis=1)
center_idx = np.nonzero(alive)[0]
center_keys = {POOL[i].tobytes() for i in center_idx}
mu4_keys = {IDP.tobytes(), Jperm.tobytes(), Jperm[Jperm].tobytes(),
            Jperm[Jperm[Jperm]].tobytes()}
check("S4.2 CENTER KILL (computed): |Z(G31)| = %d == 4 and Z = <J> = "
      "mu4; |Z(W(D5) x W(A3))| = 1 x 1 = 1 (odd-rank D5: -1 not in "
      "W(D5); Z(S4) = 1) => 4 != 1: NOT isomorphic, NOT a "
      "decomposition; v634 T1.3/T1.4/T1.5 CITED for the full "
      "structural refutation (G = (Z4 o 2^{1+4}).Sp4(2); W(D5) embeds "
      "in NO rank-4 group)" % len(center_idx),
      len(center_idx) == 4 and center_keys == mu4_keys, kill="K5")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
foreign_full = [n for n in full if n != "G31"]
if any(k in KILLS for k in ("K1",)):
    VERDICT = "G31-REBUILD-BROKEN"
elif any(k in KILLS for k in ("K2",)):
    VERDICT = "CHECKSUM-BROKEN"
elif any(k in KILLS for k in ("K4",)):
    VERDICT = "CONTROL-DEAD"
elif any(k in KILLS for k in ("K5",)):
    VERDICT = "FENCE-BROKEN"
elif foreign_full:
    VERDICT = "CLOCK-ALPHABET-WEAK (impostors: %s)" % foreign_full
else:
    VERDICT = "CLOCK-ALPHABET-SELECTIVE"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION NOTES (report only -- no promotion, no edits):")
print("  * NORMAL FORM: Deg(G31) = |mu4| x {|Z2|, N_fam, g_car, |R+(A3)|}")
print("    with lcm = |R+(E8)|, lcm/gcd = h(E8), and the audit identity")
print("    (sum d/4)(sum(d-1)/4) = 16 x 15 = 240 = the package-A census;")
print("    the 60/4 = 15 line is REALIZED on the roots (4 lines/class).")
print("  * SELECTIVITY: the kill scan censuses every rank-4 ST group;")
print("    impostors on the weak triple (gcd/lcm/30) and the raw-sum-64")
print("    coincidence (W(H4)) are typed; the full battery is expected")
print("    to pin G31 uniquely -- measured above, kill rule armed.")
print("  * FENCE re-checked: 46080 = 1920 x 24 stays numerology; the")
print("    computed center 4 vs 1 is a one-number invariant kill; the")
print("    deployed refutation (v634) is cited, not recomputed.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ("g31_clock_alphabet_probe", _SRC_G31, 19, (),
     "CLOCK-ALPHABET-SELECTIVE", 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v858 -- E8.G31.CLOCK_ALPHABET.01")
    print("(Deg(G31)/4 = {2,3,5,6} = the compiler clock alphabet as a "
          "normal form;")
    print("the unique product-46080/sum-64 quadruple; the 607-group "
          "kill scan; the")
    print("W(D5) x W(A3) fence re-killed with computed centers 4 vs 1; "
          "NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v858: %d/%d probe pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print("A normal form plus an armed kill rule for a deployed "
          "object (v634/v654);")
    print("the honesty line kept (degree-only audits cannot see the "
          "reducible torus);")
    print("no new physical claim; no marker moves.")
    print("[%s] v858 VERDICT GATE: CLOCK-ALPHABET-SELECTIVE"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
