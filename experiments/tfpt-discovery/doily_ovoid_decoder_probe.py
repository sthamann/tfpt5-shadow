#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""doily_ovoid_decoder_probe -- OVOID.DECODER.01: the integral
five-mode kernel of the Cremona-Richmond incidence and the explicit
closed-form decoder.  The six ovoid vectors v_a = 3*1_{O_a} - 1 span
ker N^T over Q with Gram 36I - 6J; the Smith normal form of N is
diag(1^10, 0^5) (NO hidden torsion, with an exhibited det-+-1 10x10
minor); the Moore-Penrose inverse has the closed form N+ = (1/4)N^T -
(1/36)J; the carrier projector P5 = (1/36) sum v_a v_a^T equals
(1/2)I - (1/4)B + (1/12)J; the mod-2 shadow of the kernel is the code
A_q = [15,5,6]; and the visible part of any point message is decoded
exactly from the 15 context reads (finite-geometry module 2 of the
2026-08-07 evening code-complex round).

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; exact
integer / Fraction arithmetic throughout; the only RNG is the
frozen-seed LCG of the minor search, the decoder test vector t6 and
control C1):

 S1  THE DOILY: N = the 15 duads x 15 synthemes incidence of the
     6-set (duad in syntheme), 3-regular in rows and columns
     (DOILY.PASCAL.RANK.01 S1 rebuilt read-only); the K6 duad model:
     16 refinements of the corpus form hb (2^16 census), Arf census
     6 + 10, D(v) = {a : q_a(v) = 0} is a 2-set for every nonzero v
     and v <-> D(v) is a bijection onto the 15 duads (v774 S8).

 S2  (a) THE KERNEL FACTS: the six ovoid vectors v_a = 3*1_{O_a} - 1
     (transported to duad indexing; ALSO equal to the combinatorial
     vector 3*[a in d] - 1 -- the transport identity) satisfy
     N^T 1_{O_a} = 1 (every syntheme covers the letter a exactly
     once: a perfect matching covers each point once) and N^T 1 =
     3*1, hence N^T v_a = 0; sum_a v_a = 0; ANY five of the six are
     linearly independent (all 6 five-subsets have rank 5).

 S3  (b) THE GRAM: V^T V = 36I - 6J entrywise on all 36 cells
     (diag 30 = 5*4 + 10*1, offdiag -6 = 4 - 8 - 8 + 6).

 S4  (c) THE INTEGRAL STRUCTURE: SNF(N) = diag(1^10, 0^5) exact over
     Z -- rank 10 = C(g_car,2), kernel 5 = g_car, ALL invariant
     factors 1 (no hidden torsion; F2-rank == Q-rank == 10 as the
     corollary); a 10x10 minor with det +-1 is EXHIBITED (greedy
     F2-pivot candidate first, then frozen-seed LCG search; the
     found row/column sets and the determinant are printed).

 S5  (d) THE MOORE-PENROSE CLOSED FORM: N+ = (1/4)N^T - (1/36)J
     satisfies the four Penrose axioms EXACTLY in Q:
     N N+ N = N, N+ N N+ = N+, (N N+)^T = N N+, (N+ N)^T = N+ N.

 S6  (e) THE CARRIER PROJECTOR: P5 = (1/36) sum_a v_a v_a^T equals
     (1/2)I - (1/4)B + (1/12)J entrywise, where B is the point-side
     symplectic incidence (B[x][y] = [hb(x,y) = 0]) transported by
     the duad bijection (the bridge N N^T = B + 2I re-verified on
     all 225 cells first); P5^2 = P5 = P5^T, P5 N = 0, tr P5 = 5 =
     g_car, and N N+ = I - P5 (the visible-part projector).

 S7  (f) THE MOD-2 SHADOW (three rings): v_a mod 2 = q_a (the odd
     refinement indicator) entrywise under the duad bijection;
     ker_F2(N^T) = A_q = C_0 + <q*> transported = [15,5,6] with
     weight enumerator 1 + 10z^6 + 15z^8 + 6z^10 (32 words, set
     equality BOTH against the transported point-side code and
     against the span of the six shadows); the three-ring
     correspondence as checked assertions: R/Q (six ovoid vectors
     span the rank-5 kernel), Z (SNF diag(1^10, 0^5), no torsion),
     F2 (kernel = A_q).

 S8  (g) THE DECODER DEMO: reads y = N^T m (the 15 syntheme context
     sums); the closed-form decoder mhat = (1/4)N y - (1/36)J y
     reconstructs the VISIBLE part (I - P5)m EXACTLY on the
     predeclared test set
       t1 = e_0, t2 = all-ones, t3 = v_0 (first ovoid vector),
       t4 = e_3 - e_7, t5 = N u5 with u5[k] = ((3k) mod 7) - 3,
       t6 = frozen-LCG integer vector (entries in [-5,5]);
     with the typed expectations: t3 decodes to 0 (kernel mode
     invisible), t2 decodes to t2 and t5 to t5 (both fully visible).

 S9  THE S6 IDENTIFICATION (the representation check): the S6 action
     on duads/synthemes commutes with N (equivariance N[pd(i)][ps(j)]
     = N[i][j] for the generators (01) and (012345)); the six ovoid
     vectors are PERMUTED (Pi_D v_a = v_{pi(a)}); and ker N^T is the
     STANDARD 5-dim representation: tr(P5 Pi_D(pi)) == fix_6(pi) - 1
     for one representative of EACH of the 11 conjugacy classes of
     S6 (exact Fractions; identity gives tr P5 = 5).

 C   CONTROL (must fire): the frozen-seed LCG wrong pairing (sum of
     3 pairwise-disjoint random permutation matrices; row/col sums 3
     -- same regularity) does NOT reproduce the doily triple: at
     least one of {SNF = diag(1^10,0^5), ker_F2 = A_q, N'^T v_a = 0
     for all six} FAILS (each sub-outcome measured and printed).

KILLS (any one fires => typed failure):
  K1  doily / duad model breaks              -> DOILY-BROKEN
  K2  a kernel fact of S2 breaks             -> KERNEL-BROKEN
  K3  the 36I - 6J Gram breaks               -> GRAM-BROKEN
  K4  SNF != diag(1^10, 0^5)                 -> SNF-TORSION
  K5  no det-+-1 minor found in budget       -> MINOR-NOT-EXHIBITED
  K6  a Penrose axiom fails                  -> PENROSE-BROKEN
  K7  a projector identity fails             -> PROJECTOR-BROKEN
  K8  the mod-2 shadow / A_q equality fails  -> SHADOW-BROKEN
  K9  the decoder demo fails                 -> DECODER-BROKEN
  K10 an S6 character/equivariance fails     -> REP-MISMATCH
  K11 the control does not fire              -> CONTROL-DEAD

VERDICT (frozen enum): OVOID-DECODER-EXACT / <typed kill above> /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact integer/Fraction/sympy arithmetic; no
floats; the only RNG is the frozen-seed LCG (minor search, t6, C1).
NO physics claim.

Sources (read-only, machinery rebuilt inline):
doily_pascal_rank_probe.py (N, bridge, charpoly context; its C2
control pairing reused with the same frozen seed),
v774_arf_spinor_compiler (S8 duad model, S9 doily Gram),
v811/v815 (doily Kraus corpus), v819 (A_q neighborhood [15,5,-]),
finite_compiler_normal_form_probe.py (q* conventions),
tfpt_constants (g_car, N_fam).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/doily_ovoid_decoder_probe.py
"""
import hashlib
import itertools
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "verification"))
from tfpt_constants import N_fam, g_car  # noqa: E402  (read-only import)

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


print("OVOID.DECODER.01 -- integral five-mode kernel + closed-form "
      "decoder")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ------------------------------------------------------- helpers
def pc(v):
    return bin(v).count("1")


def hb(v, w):
    return ((pc(v) & 1) & (pc(w) & 1)) ^ (pc(v & w) & 1)


def frac_rank(rows_):
    M = [[Fr(e) for e in r] for r in rows_]
    rank = 0
    nrows, ncols = len(M), len(M[0])
    for col in range(ncols):
        piv = next((r for r in range(rank, nrows) if M[r][col] != 0),
                   None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = 1 / M[rank][col]
        M[rank] = [e * inv for e in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [e - f * g for e, g in zip(M[r], M[rank])]
        rank += 1
        if rank == nrows:
            break
    return rank


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[sum(A[i][t] * Bt[j][t] for t in range(k))
             for j in range(m)] for i in range(n)]


def mat_eq(A, B):
    return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))


def transpose(A):
    return [list(r) for r in zip(*A)]


def det_int(M0):
    """Bareiss fraction-free determinant, exact integers."""
    n = len(M0)
    M = [row[:] for row in M0]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            piv = next((r for r in range(k + 1, n) if M[r][k]), None)
            if piv is None:
                return 0
            M[k], M[piv] = M[piv], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k]
                           - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


_LCG = [20260807]


def lcg():
    _LCG[0] = (6364136223846793005 * _LCG[0]
               + 1442695040888963407) % (1 << 64)
    return _LCG[0]


# ======================================================================
section("S1: the doily N + the K6 duad model (rebuilt read-only)")
# ======================================================================
DUADS = [frozenset(p) for p in itertools.combinations(range(6), 2)]
SYNTHEMES = []
for m in itertools.permutations(range(6)):
    s = frozenset(frozenset({m[2 * k], m[2 * k + 1]}) for k in range(3))
    if s not in SYNTHEMES:
        SYNTHEMES.append(s)
N = [[1 if DUADS[i] in SYNTHEMES[j] else 0 for j in range(15)]
     for i in range(15)]
rows = [sum(r) for r in N]
cols = [sum(N[i][j] for i in range(15)) for j in range(15)]
check("S1.1 15 duads, %d synthemes; N 3-regular in rows and columns "
      "(3 = N_fam)" % len(SYNTHEMES),
      len(SYNTHEMES) == 15 and rows == [3] * 15 == [N_fam] * 15
      and cols == [3] * 15, kill="K1")

PTS = list(range(16))
NZ = list(range(1, 16))
HBT = [[hb(v, w) for w in PTS] for v in PTS]
REFS = []
for mask in range(1 << 16):
    q = [(mask >> i) & 1 for i in range(16)]
    ok = True
    for i in range(16):
        qi = q[i]
        row = HBT[i]
        for j in range(16):
            if q[i ^ j] ^ qi ^ q[j] != row[j]:
                ok = False
                break
        if not ok:
            break
    if ok:
        REFS.append(tuple(q))
ARF1 = sorted(q for q in REFS if sum(1 for i in PTS if q[i] == 0) == 6)
duad_of = {}
ok_two = True
for v in NZ:
    dv = frozenset(a for a in range(6) if ARF1[a][v] == 0)
    if len(dv) != 2:
        ok_two = False
    duad_of[v] = dv
didx = {d: i for i, d in enumerate(DUADS)}
point_of = {didx[duad_of[v]]: v for v in NZ}
check("S1.2 16 refinements of hb (2^16 census), Arf census 6 + 10; "
      "K6 duad model: D(v) 2-sets, v <-> D(v) bijective onto the 15 "
      "duads (v774 S8)",
      len(REFS) == 16 and len(ARF1) == 6 and ok_two
      and len(set(duad_of.values())) == 15
      and len(point_of) == 15, kill="K1")

# ======================================================================
section("S2: (a) the kernel facts -- N^T v_a = 0 from matchings")
# ======================================================================
OV = []                                 # geometric ovoid vectors
OVC = []                                # combinatorial 3*[a in d] - 1
for a in range(6):
    O_a = {v for v in NZ if ARF1[a][v] == 0}
    u = [0] * 15
    for v in NZ:
        u[didx[duad_of[v]]] = 3 * (1 if v in O_a else 0) - 1
    OV.append(u)
    OVC.append([3 * (1 if a in DUADS[i] else 0) - 1 for i in range(15)])
check("S2.1 TRANSPORT IDENTITY: v_a = 3*1_{O_a} - 1 transported == "
      "the combinatorial vector 3*[a in d] - 1 (all 6 x 15 entries); "
      "|O_a| = 5 for all a",
      all(OV[a] == OVC[a] for a in range(6))
      and all(sum(1 for v in NZ if ARF1[a][v] == 0) - 1 == 5 - 1
              for a in range(6))
      and all(sum(1 for x in OV[a] if x == 2) == 5 for a in range(6)),
      kill="K2")


def NT_apply(vec):
    return [sum(N[i][j] * vec[i] for i in range(15)) for j in range(15)]


ok_match = all(NT_apply([1 if a in DUADS[i] else 0
                         for i in range(15)]) == [1] * 15
               for a in range(6))
check("S2.2 N^T 1_{O_a} = 1 for ALL six a (every syntheme = perfect "
      "matching covers the letter a exactly once) and N^T 1 = 3*1",
      ok_match and NT_apply([1] * 15) == [3] * 15, kill="K2")
check("S2.3 N^T v_a = 0 for ALL six a; sum_a v_a = 0 (vector)",
      all(NT_apply(OV[a]) == [0] * 15 for a in range(6))
      and [sum(OV[a][i] for a in range(6))
           for i in range(15)] == [0] * 15, kill="K2")
ok_five = all(frac_rank([OV[a] for a in range(6) if a != skip]) == 5
              for skip in range(6))
check("S2.4 ANY five of the six ovoid vectors are independent (all 6 "
      "five-subsets have rank 5); full set has rank 5",
      ok_five and frac_rank(OV) == 5 == g_car, kill="K2")

# ======================================================================
section("S3: (b) the Gram V^T V = 36I - 6J")
# ======================================================================
G = [[sum(OV[a][i] * OV[b][i] for i in range(15)) for b in range(6)]
     for a in range(6)]
check("S3.1 V^T V == 36I - 6J ENTRYWISE (diag %d == 30, offdiag %d "
      "== -6, all 36 cells)" % (G[0][0], G[0][1]),
      all(G[a][b] == (30 if a == b else -6) for a in range(6)
          for b in range(6)), kill="K3")

# ======================================================================
section("S4: (c) SNF(N) = diag(1^10, 0^5) + the det-+-1 minor")
# ======================================================================
S = smith_normal_form(sp.Matrix(N))
diag = [int(S[i, i]) for i in range(15)]
offdiag_zero = all(S[i, j] == 0 for i in range(15) for j in range(15)
                   if i != j)
check("S4.1 SNF(N) = diag(%s) == diag(1^10, 0^5) exact over Z -- "
      "rank 10 = C(g_car,2) = %d, kernel 5 = g_car, NO torsion "
      "(all invariant factors 1)"
      % ("1^10, 0^5" if diag == [1] * 10 + [0] * 5 else str(diag),
         g_car * (g_car - 1) // 2),
      diag == [1] * 10 + [0] * 5 and offdiag_zero
      and g_car * (g_car - 1) // 2 == 10, kill="K4")
check("S4.2 corollary ranks agree: rank_Q(N) = %d == 10 == rank_F2(N)"
      % frac_rank(N),
      frac_rank(N) == 10
      and frac_rank([[e % 2 for e in r] for r in N]) == 10, kill="K4")


def f2_independent_subset(vectors_as_masks, want):
    """Greedy: first `want` F2-independent indices."""
    basis, chosen = [], []
    for idx, v in enumerate(vectors_as_masks):
        w = v
        for b in basis:
            w = min(w, w ^ b)
        if w:
            basis.append(w)
            basis.sort(reverse=True)
            chosen.append(idx)
            if len(chosen) == want:
                break
    return chosen


row_masks = [sum(N[i][j] << j for j in range(15)) for i in range(15)]
grows = f2_independent_subset(row_masks, 10)
col_masks_sub = [sum(N[grows[k]][j] << k for k in range(10))
                 for j in range(15)]
gcols = f2_independent_subset(col_masks_sub, 10)
found = None
cand = [[N[i][j] for j in gcols] for i in grows]
d0 = det_int(cand)
trials = 0
if abs(d0) == 1:
    found = (grows, gcols, d0)
else:
    while trials < 40000 and found is None:
        trials += 1
        rr = sorted(lcg() % 15 for _ in range(20))
        rset = []
        for x in rr:
            if x not in rset:
                rset.append(x)
            if len(rset) == 10:
                break
        if len(rset) < 10:
            continue
        cc = []
        for x in (lcg() % 15 for _ in range(30)):
            if x not in cc:
                cc.append(x)
            if len(cc) == 10:
                break
        if len(cc) < 10:
            continue
        d = det_int([[N[i][j] for j in cc] for i in rset])
        if abs(d) == 1:
            found = (sorted(rset), sorted(cc), d)
check("S4.3 det-+-1 10x10 MINOR EXHIBITED: rows %s, cols %s, det = "
      "%s (greedy F2-pivot candidate det = %d, LCG trials used = %d)"
      % (found[0] if found else None, found[1] if found else None,
         found[2] if found else None, d0, trials),
      found is not None, kill="K5")

# ======================================================================
section("S5: (d) the Moore-Penrose closed form N+ = N^T/4 - J/36")
# ======================================================================
NF = [[Fr(N[i][j]) for j in range(15)] for i in range(15)]
NT = transpose(NF)
JF = [[Fr(1)] * 15 for _ in range(15)]
IF = [[Fr(1) if i == j else Fr(0) for j in range(15)]
      for i in range(15)]
NP = [[NT[i][j] / 4 - Fr(1, 36) for j in range(15)] for i in range(15)]
NNP = mmul(NF, NP)
NPN = mmul(NP, NF)
check("S5.1 Penrose 1+2: N N+ N == N and N+ N N+ == N+ (exact Q)",
      mat_eq(mmul(NNP, NF), NF) and mat_eq(mmul(NPN, NP), NP),
      kill="K6")
check("S5.2 Penrose 3+4: (N N+)^T == N N+ and (N+ N)^T == N+ N "
      "(exact Q)",
      mat_eq(transpose(NNP), NNP) and mat_eq(transpose(NPN), NPN),
      kill="K6")

# ======================================================================
section("S6: (e) the carrier projector P5 = (1/2)I - (1/4)B + (1/12)J")
# ======================================================================
NZS = sorted(NZ)
B = [[1 if HBT[x][y] == 0 else 0 for y in NZS] for x in NZS]
NNt = [[sum(N[i][k] * N[j][k] for k in range(15)) for j in range(15)]
       for i in range(15)]
ok_bridge = all(
    NNt[didx[duad_of[x]]][didx[duad_of[y]]]
    == B[xi][yi] + (2 if xi == yi else 0)
    for xi, x in enumerate(NZS) for yi, y in enumerate(NZS))
check("S6.1 BRIDGE re-verified: N N^T == B + 2I under the duad "
      "bijection (all 225 cells; DOILY.PASCAL.RANK.01 S3.3)",
      ok_bridge, kill="K7")

P5 = [[sum(Fr(OV[a][i] * OV[a][j], 36) for a in range(6))
       for j in range(15)] for i in range(15)]
Bd = [[Fr(0)] * 15 for _ in range(15)]
for xi, x in enumerate(NZS):
    for yi, y in enumerate(NZS):
        Bd[didx[duad_of[x]]][didx[duad_of[y]]] = Fr(B[xi][yi])
P5_closed = [[IF[i][j] / 2 - Bd[i][j] / 4 + Fr(1, 12)
              for j in range(15)] for i in range(15)]
check("S6.2 P5 = (1/36) sum_a v_a v_a^T == (1/2)I - (1/4)B + (1/12)J "
      "ENTRYWISE (all 225 cells, exact Q)",
      mat_eq(P5, P5_closed), kill="K7")
trP5 = sum(P5[i][i] for i in range(15))
check("S6.3 P5^2 == P5 == P5^T; P5 N == 0; tr P5 = %s == 5 = g_car; "
      "N N+ == I - P5 (the visible-part projector)" % trP5,
      mat_eq(mmul(P5, P5), P5) and mat_eq(transpose(P5), P5)
      and all(e == 0 for r in mmul(P5, NF) for e in r)
      and trP5 == 5 == g_car
      and mat_eq(NNP, [[IF[i][j] - P5[i][j] for j in range(15)]
                       for i in range(15)]), kill="K7")

# ======================================================================
section("S7: (f) the mod-2 shadow -- ker_F2(N^T) = A_q = [15,5,6]")
# ======================================================================
ok_shadow = all((OV[a][i] % 2) == ARF1[a][point_of[i]]
                for a in range(6) for i in range(15))
check("S7.1 v_a mod 2 == q_a (the odd refinement indicator) "
      "entrywise under the duad bijection (all 6 x 15)",
      ok_shadow, kill="K8")

col_full = [sum(N[i][j] << i for i in range(15)) for j in range(15)]
KER = [y for y in range(1 << 15)
       if all(pc(y & c) % 2 == 0 for c in col_full)]


def span_bits(gens):
    S_ = {0}
    for g in gens:
        S_ |= {s ^ g for s in S_}
    return S_


sh_masks = [sum((OV[a][i] % 2) << i for i in range(15))
            for a in range(6)]
A_INT, FSIG_INT = 8, 7


# selector (canonical q*, NORMALFORM.CFIN.01 convention)
def sig_int(v):
    b = [(v >> k) & 1 for k in range(4)]
    w = (b[2], b[0], b[1], b[3])
    return sum(w[k] << k for k in range(4))


siginv = [q for q in REFS if all(q[sig_int(v)] == q[v] for v in PTS)]
cand = [q for q in siginv if q[A_INT] == 1 and q[FSIG_INT] == 0]
QS = cand[0]
pidx = {v: i for i, v in enumerate(NZS)}


def transport_pointword(mask_pt):
    out = 0
    for i in range(15):
        if (mask_pt >> i) & 1:
            out |= 1 << didx[duad_of[NZS[i]]]
    return out


c0_gens_pt = [sum((1 << pidx[x]) for x in NZS if HBT[v][x] == 1)
              for v in (1, 2, 4, 8)]
q_pt = sum((1 << pidx[x]) for x in NZS if QS[x] == 1)
AQ_duad = span_bits([transport_pointword(g)
                     for g in c0_gens_pt + [q_pt]])
we_ker = Counter(pc(y) for y in KER)
check("S7.2 ker_F2(N^T): %d words == 32 (dim 5); == span of the six "
      "shadows (set equality); == A_q = C_0 + <q*> transported (set "
      "equality); weight enumerator %s == 1 + 10z^6 + 15z^8 + 6z^10, "
      "min distance 6 -> [15,5,6]"
      % (len(KER), dict(sorted(we_ker.items()))),
      len(KER) == 32 and set(KER) == span_bits(sh_masks)
      and set(KER) == AQ_duad
      and dict(we_ker) == {0: 1, 6: 10, 8: 15, 10: 6}, kill="K8")
check("S7.3 THREE RINGS: R/Q -- six ovoid vectors span the rank-5 "
      "kernel (S2.4 + rank_Q N = 10); Z -- SNF diag(1^10,0^5), no "
      "torsion (S4.1); F2 -- kernel = A_q (S7.2): one object in "
      "three rings", True,
      "checked assertions bundled: S2.4, S4.1, S7.2", kill=None)

# ======================================================================
section("S8: (g) the decoder demo -- visible part from context reads")
# ======================================================================
u5 = [((3 * k) % 7) - 3 for k in range(15)]
t5 = [sum(N[i][j] * u5[j] for j in range(15)) for i in range(15)]
t6 = [int(lcg() % 11) - 5 for _ in range(15)]
TESTS = [
    ("t1 = e_0", [1] + [0] * 14),
    ("t2 = all-ones", [1] * 15),
    ("t3 = v_0 (ovoid)", OV[0][:]),
    ("t4 = e_3 - e_7", [0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0]),
    ("t5 = N u5", t5),
    ("t6 = LCG vector", t6),
]
NPT = transpose(NP)                      # (N^T)+ = (N+)^T = N/4 - J/36
ok_dec = True
notes = []
for name, m in TESTS:
    mf = [Fr(x) for x in m]
    y = [sum(NF[i][j] * mf[i] for i in range(15)) for j in range(15)]
    mhat = [sum(NPT[i][j] * y[j] for j in range(15)) for i in range(15)]
    vis = [mf[i] - sum(P5[i][j] * mf[j] for j in range(15))
           for i in range(15)]
    if mhat != vis:
        ok_dec = False
    notes.append((name, mhat == vis))
check("S8.1 CLOSED-FORM DECODER: mhat = (1/4)N y - (1/36)J y == "
      "(I - P5)m EXACTLY on the predeclared test set (%s)"
      % ", ".join("%s: %s" % (n, "ok" if o else "FAIL")
                  for n, o in notes), ok_dec, kill="K9")
mhat3 = [sum(NPT[i][j] * sum(NF[k][j] * Fr(OV[0][k])
                             for k in range(15))
             for j in range(15)) for i in range(15)]
mhat2 = [sum(NPT[i][j] * sum(NF[k][j] for k in range(15))
             for j in range(15)) for i in range(15)]
mhat5 = [sum(NPT[i][j] * sum(NF[k][j] * Fr(t5[k]) for k in range(15))
             for j in range(15)) for i in range(15)]
check("S8.2 typed expectations: t3 (kernel mode) decodes to 0 "
      "(invisible); t2 = all-ones and t5 in im(N) decode to "
      "THEMSELVES (fully visible)",
      mhat3 == [Fr(0)] * 15 and mhat2 == [Fr(1)] * 15
      and mhat5 == [Fr(x) for x in t5], kill="K9")

# ======================================================================
section("S9: the S6 identification -- standard representation")
# ======================================================================
sidx = {s: j for j, s in enumerate(SYNTHEMES)}


def perm_from_cycles(cycs):
    p = list(range(6))
    for cyc in cycs:
        for k in range(len(cyc)):
            p[cyc[k]] = cyc[(k + 1) % len(cyc)]
    return p


def duad_perm(p):
    return [didx[frozenset({p[a] for a in DUADS[i]})]
            for i in range(15)]


def syn_perm(p):
    return [sidx[frozenset(frozenset({p[a] for a in d}) for d in
                           SYNTHEMES[j])] for j in range(15)]


ok_equi = True
ok_permov = True
for gen in ([(0, 1)], [(0, 1, 2, 3, 4, 5)]):
    p = perm_from_cycles(gen)
    pd, ps = duad_perm(p), syn_perm(p)
    if not all(N[pd[i]][ps[j]] == N[i][j]
               for i in range(15) for j in range(15)):
        ok_equi = False
    for a in range(6):
        w = [0] * 15
        for i in range(15):
            w[pd[i]] = OV[a][i]
        if w != OV[p[a]]:
            ok_permov = False
check("S9.1 S6-EQUIVARIANCE: N[pd(i)][ps(j)] == N[i][j] for the "
      "generators (01) and (012345); Pi_D v_a == v_{pi(a)} (the six "
      "ovoid vectors are permuted)", ok_equi and ok_permov,
      kill="K10")

CLASS_REPS = [
    ((), 6), (((0, 1),), 4), (((0, 1), (2, 3)), 2),
    (((0, 1), (2, 3), (4, 5)), 0), (((0, 1, 2),), 3),
    (((0, 1, 2), (3, 4)), 1), (((0, 1, 2), (3, 4, 5)), 0),
    (((0, 1, 2, 3),), 2), (((0, 1, 2, 3), (4, 5)), 0),
    (((0, 1, 2, 3, 4),), 1), (((0, 1, 2, 3, 4, 5),), 0),
]
char_rows = []
ok_char = True
for cycs, fix in CLASS_REPS:
    p = perm_from_cycles(list(cycs))
    pd = duad_perm(p)
    tr = sum(P5[i][pd[i]] for i in range(15))
    char_rows.append((cycs if cycs else "id", str(tr), fix - 1))
    if tr != Fr(fix - 1):
        ok_char = False
check("S9.2 STANDARD REPRESENTATION: tr(P5 Pi_D(pi)) == fix_6(pi) - 1 "
      "for representatives of ALL 11 conjugacy classes of S6 "
      "(identity: tr P5 = 5) -- ker N^T is the 5-dim standard rep",
      ok_char and trP5 == 5, kill="K10")
print("    class traces: %s"
      % "; ".join("%s: %s (=%d)" % (str(c), t, x)
                  for c, t, x in char_rows))

# ======================================================================
section("C: control (must fire) -- frozen-LCG wrong pairing")
# ======================================================================
_LCG[0] = 20260807                      # re-freeze (parent C2 seed)


def rand_perm():
    p = list(range(15))
    for i in range(14, 0, -1):
        j = lcg() % (i + 1)
        p[i], p[j] = p[j], p[i]
    return p


perms = []
while len(perms) < 3:
    c = rand_perm()
    if all(all(c[i] != q[i] for i in range(15)) for q in perms):
        perms.append(c)
N2 = [[sum(1 for q in perms if q[i] == j) for j in range(15)]
      for i in range(15)]
S2m = smith_normal_form(sp.Matrix(N2))
diag2 = [int(S2m[i, i]) for i in range(15)]
col2 = [sum(N2[i][j] << i for i in range(15)) for j in range(15)]
KER2 = [y for y in range(1 << 15)
        if all(pc(y & c) % 2 == 0 for c in col2)]
ov_ok2 = all([sum(N2[i][j] * OV[a][i] for i in range(15))
              for j in range(15)] == [0] * 15 for a in range(6))
same_snf = diag2 == [1] * 10 + [0] * 5
same_ker = set(KER2) == set(KER)
check("C1 FIRES: LCG wrong pairing (3 disjoint permutations, row/col "
      "sums 3): SNF diag = %s (same: %s), |ker_F2| = %d (== A_q: %s), "
      "N'^T v_a = 0 for all six: %s -- the doily triple is NOT "
      "reproduced"
      % (diag2, same_snf, len(KER2), same_ker, ov_ok2),
      all(sum(r) == 3 for r in N2)
      and all(sum(N2[i][j] for i in range(15)) == 3
              for j in range(15))
      and not (same_snf and same_ker and ov_ok2), kill="K11")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C1"))
if not controls_ok:
    VERDICT = "CONTROL-DEAD"
elif KILLS:
    VERDICT = {"K1": "DOILY-BROKEN", "K2": "KERNEL-BROKEN",
               "K3": "GRAM-BROKEN", "K4": "SNF-TORSION",
               "K5": "MINOR-NOT-EXHIBITED", "K6": "PENROSE-BROKEN",
               "K7": "PROJECTOR-BROKEN", "K8": "SHADOW-BROKEN",
               "K9": "DECODER-BROKEN",
               "K10": "REP-MISMATCH"}.get(KILLS[0], "CONTROL-DEAD")
else:
    VERDICT = "OVOID-DECODER-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
print("  * DOILY.PASCAL.RANK.01 gave the SPECTRUM (sing(N) = "
      "{3, 2^9, 0^5}); this")
print("    probe adds the INTEGRAL layer: SNF diag(1^10, 0^5) (no "
      "hidden torsion,")
print("    det-+-1 minor exhibited), the CLOSED FORMS N+ = N^T/4 - "
      "J/36 and")
print("    P5 = I/2 - B/4 + J/12, and the exact decoder mhat = "
      "(I - P5) m -- the")
print("    recovery channel now has an explicit integral inverse, "
      "not just a spectrum.")
print("  * v774 S9's ovoid (-2)-eigenspace: identified as the S6 "
      "STANDARD 5-dim")
print("    representation (11/11 class characters fix - 1), Gram "
      "36I - 6J, any five")
print("    of six a basis -- the five-slot carrier is the "
      "sixth-root-free shadow of")
print("    six ovoid modes with one relation sum v_a = 0.")
print("  * NEW three-ring statement: the SAME kernel is (R) the "
      "ovoid span, (Z)")
print("    torsion-free rank 5, (F2) the code A_q = [15,5,6] -- the "
      "mod-2 shadow")
print("    v_a mod 2 = q_a ties the doily channel to the Arf/bent "
      "layer of probe 3.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT == "OVOID-DECODER-EXACT") else 1)
