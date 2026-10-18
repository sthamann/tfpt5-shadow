#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""doily_pascal_rank_probe -- DOILY.PASCAL.RANK.01: the Doily-Pascal
rank theorem -- the recovery value 2/3, the five-slot carrier and the
decuple sector are the singular values / kernel / rank of ONE incidence
map (the duad-syntheme incidence of the Cremona-Richmond doily).

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; work
package A of the v5.4 strategy; follow-up to v774 ARF.SPINORCOMPILER.01
S9, v814 K5.SIXSTEP.TRANSPORT.01 A1, v811/v815 doily machinery):

 S1  THE DOILY INCIDENCE: N = the 15 duads x 15 synthemes incidence of
     the 6-element set (duad in syntheme), built explicitly; N is
     3-regular in rows AND columns (each duad in 3 synthemes, each
     syntheme = 3 duads) -- the classical Cremona-Richmond / GQ(2,2)
     point-line structure.

 S2  THE SYMPLECTIC SIDE: on the 15 points of PG(3,2) = nonzero
     vectors of V = F2^4 with the corpus form hbar (Gram J - I in the
     family/anchor basis, v752/v774), B[x][y] = 1 iff hbar(x,y) = 0;
     row sums 7; B B^T = 4I + 3J ENTRYWISE; charpoly(B) =
     (x-7)(x-2)^9(x+2)^5 (v774 S9.2 rebuilt).

 S3  THE BRIDGE (the rank theorem's two sides are ONE object): via the
     K6 duad model D(v) = {q Arf-1 : q(v) = 0} (16 quadratic
     refinements by brute force over 2^16, Arf census 6 + 10, v774
     S2/S3/S8 rebuilt), the bijection point <-> duad carries
     N N^T onto B + 2I ENTRYWISE (all 225 cells) -- collinearity of
     duads = symplectic orthogonality of points.

 S4  THE RANK THEOREM (exact Fraction arithmetic):
     charpoly(N N^T) = (x-9)(x-4)^9 x^5, i.e. sing(N) = {3^1, 2^9,
     0^5}; rank N = 10 = A_Lambda = C(g_car, 2) (the decuple sector);
     dim ker N = dim ker N^T = 5 = g_car (the five-slot carrier);
     multiplicity 9 = N_fam^2; top value 3 = N_fam; the SIX ovoid
     indicator vectors 3*1_{O_q} - 1 (q Arf-1), transported to duad
     indexing, all lie in ker N^T and SPAN it (rank exactly 5).

 S5  THE RECOVERY VALUE: sing(N/3) = {1, 2/3 x9, 0 x5} exact
     (charpoly of (N/3)(N/3)^T = (x-1)(x-4/9)^9 x^5); 2/3 =
     (N_fam - 1)/N_fam = the corpus recovery survival (v327).

 S6  THE COMPILER CLOCK CROSS-CHECK: the deployed recovery spectrum is
     {1, (2/3)^6, (1/3)^6} (v330/v486; the sixth power is the compiler
     clock, v814 SIXSTEP-CLOCK-ONLY).  Verified here EXACTLY: the
     three PSD double-steps ((N/3)(N^T/3))^3 have charpoly
     (x-1)(x-64/729)^9 x^5 with 64/729 = (2/3)^6 = the deployed
     lambda_2 (the exponentiation identity); TYPED GAP re-affirmed:
     the doily channel has NO (1/3)^6 mode (1/729 is NOT an eigenvalue
     of the six-step alternation) -- the (1/3)^6 line of the deployed
     spectrum lives on the clock side (v814 [E], cited, consistent).

 C   CONTROLS (must fire; wrong pairing with the SAME row sums):
     C1 the circulant 3-regular bipartite pairing N'[i][j] = 1 iff
        (j - i) mod 15 in {0,1,2}: row/col sums 3, but rank != 10 and
        dim ker != 5 and charpoly(N'N'^T) != the doily target.
     C2 the frozen-seed LCG pairing (sum of 3 pairwise-disjoint random
        permutation matrices; row/col sums 3): (rank, charpoly) !=
        (10, doily target).

KILLS (any one fires => typed failure):
  K1 doily census / regularity breaks                -> DOILY-BROKEN
  K2 B B^T != 4I+3J or spectrum 7/2^9/(-2)^5 breaks  -> GRAM-BROKEN
  K3 N N^T != B + 2I in any cell                     -> BRIDGE-BROKEN
  K4 rank != 10 or kernel != 5 or spectrum deviates  -> RANK-MISMATCH
  K5 the (2/3)^6 exponentiation identity fails, or a
     spurious (1/3)^6 mode appears                   -> CLOCK-MISMATCH
  K6 a control does not fire                         -> CONTROL-DEAD

VERDICT (frozen enum): DOILY-PASCAL-RANK-EXACT / DOILY-BROKEN /
GRAM-BROKEN / BRIDGE-BROKEN / RANK-MISMATCH / CLOCK-MISMATCH /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface.
Exact integer/Fraction/sympy arithmetic; the only RNG is the frozen-
seed LCG of control C2 (v775 C2 precedent); no floats, no fit.

Sources (read-only): verification/v774_arf_spinor_compiler.py (S2/S3/
S8/S9 machinery rebuilt inline), v814_k5_sixstep_transport.py (A1 doily
route), v811/v815 (doily Kraus corpus), v330/v486 (deployed transfer
spectrum), v327 (2/3 recovery survival), tfpt_constants (g_car, N_fam).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/doily_pascal_rank_probe.py
"""
import hashlib
import itertools
import os
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

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


print("DOILY.PASCAL.RANK.01 -- rank/kernel/singular values of the "
      "duad-syntheme incidence")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

A_LAMBDA = g_car * (g_car - 1) // 2      # 10 = C(5,2), the decuple sector

# ----------------------------------------------------------------------
section("S1: the Cremona-Richmond doily incidence N (duads x synthemes)")
# ----------------------------------------------------------------------
DUADS = [frozenset(p) for p in itertools.combinations(range(6), 2)]
SYNTHEMES = []
for m in itertools.permutations(range(6)):
    s = frozenset(frozenset({m[2 * k], m[2 * k + 1]}) for k in range(3))
    if s not in SYNTHEMES:
        SYNTHEMES.append(s)
N = [[1 if DUADS[i] in SYNTHEMES[j] else 0 for j in range(len(SYNTHEMES))]
     for i in range(15)]
rows = [sum(N[i]) for i in range(15)]
cols = [sum(N[i][j] for i in range(15)) for j in range(len(SYNTHEMES))]
check("S1.1 15 duads, %d synthemes (perfect matchings of the 6-set); "
      "N is 3-regular in rows and columns" % len(SYNTHEMES),
      len(SYNTHEMES) == 15 and rows == [3] * 15 and cols == [3] * 15,
      kill="K1")

# ----------------------------------------------------------------------
section("S2: the symplectic point incidence B on PG(3,2) (v774 S9)")
# ----------------------------------------------------------------------
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]  # J - I


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


NZ15 = sorted(w for w in W16 if any(w))
B = [[1 if hb(x, y) == 0 else 0 for y in NZ15] for x in NZ15]
BBt = [[sum(B[i][k] * B[j][k] for k in range(15)) for j in range(15)]
       for i in range(15)]
ok_bbt = all(BBt[i][j] == (7 if i == j else 3)
             for i in range(15) for j in range(15))
x = sp.symbols("x")
cpB = sp.Matrix(B).charpoly(x).as_expr()
cpB_t = sp.expand((x - 7) * (x - 2) ** 9 * (x + 2) ** 5)
check("S2.1 hbar alternating + nondegenerate; B row sums all 7; "
      "B B^T == 4I + 3J ENTRYWISE (225 cells)",
      all(hb(v, v) == 0 for v in W16)
      and all(any(hb(v, w) for w in NZ15) for v in NZ15)
      and all(sum(r) == 7 for r in B) and ok_bbt, kill="K2")
check("S2.2 charpoly(B) = (x-7)(x-2)^9(x+2)^5 exact (spectrum "
      "7^1 2^9 (-2)^5, v774 S9.2)",
      sp.expand(cpB - cpB_t) == 0, kill="K2")

# ----------------------------------------------------------------------
section("S3: the bridge -- N N^T = B + 2I via the K6 duad model")
# ----------------------------------------------------------------------
refs = []
for mask in range(1 << 16):
    q = [(mask >> i) & 1 for i in range(16)]
    ok = True
    for i in range(16):
        qi = q[i]
        vi = W16[i]
        for j in range(16):
            vj = W16[j]
            vs = tuple((a + b) % 2 for a, b in zip(vi, vj))
            if q[WIDX[vs]] ^ qi ^ q[j] != hb(vi, vj):
                ok = False
                break
        if not ok:
            break
    if ok:
        refs.append(tuple(q))
arf1 = sorted(q for q in refs
              if sum(1 for i in range(16) if q[i] == 0) == 6)
check("S3.1 exactly 16 quadratic refinements of hbar (brute force over "
      "2^16); Arf census 6 + 10 (v774 S2/S3)",
      len(refs) == 16 and len(arf1) == 6
      and sum(1 for q in refs
              if sum(1 for i in range(16) if q[i] == 0) == 10) == 10,
      kill="K3")

duad_of = {}
ok_two = True
for v in NZ15:
    dv = frozenset(k for k, q in enumerate(arf1) if q[WIDX[v]] == 0)
    if len(dv) != 2:
        ok_two = False
    duad_of[v] = dv
check("S3.2 K6 duad model: D(v) = {q Arf-1 : q(v) = 0} is a 2-set for "
      "every v != 0 and v <-> D(v) is a bijection onto the 15 duads "
      "(v774 S8)",
      ok_two and len(set(duad_of.values())) == 15, kill="K3")

didx = {frozenset(p): i for i, p in enumerate(DUADS)}
NNt = [[sum(N[i][k] * N[j][k] for k in range(15)) for j in range(15)]
       for i in range(15)]
ok_bridge = True
for vi, v in enumerate(NZ15):
    for wi, w in enumerate(NZ15):
        lhs = NNt[didx[duad_of[v]]][didx[duad_of[w]]]
        rhs = B[vi][wi] + (2 if vi == wi else 0)
        if lhs != rhs:
            ok_bridge = False
check("S3.3 THE BRIDGE: N N^T == B + 2I ENTRYWISE under the duad "
      "bijection (all 225 cells) -- duad collinearity = symplectic "
      "orthogonality", ok_bridge, kill="K3")

# ----------------------------------------------------------------------
section("S4: the rank theorem -- rank 10 = A_Lambda, kernel 5 = g_car")
# ----------------------------------------------------------------------
cpNNt = sp.Matrix(NNt).charpoly(x).as_expr()
cpNNt_t = sp.expand((x - 9) * (x - 4) ** 9 * x ** 5)
check("S4.1 charpoly(N N^T) = (x-9)(x-4)^9 x^5 exact -- sing(N) = "
      "{3^1, 2^9, 0^5}", sp.expand(cpNNt - cpNNt_t) == 0, kill="K4")


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


rkN = frac_rank(N)
rkNT = frac_rank([[N[i][j] for i in range(15)] for j in range(15)])
check("S4.2 rank N = %d == 10 == A_Lambda = C(g_car,2) (the decuple "
      "sector); dim ker N = dim ker N^T = %d == 5 == g_car (the "
      "five-slot carrier)" % (rkN, 15 - rkN),
      rkN == rkNT == 10 == A_LAMBDA and 15 - rkN == 5 == g_car,
      kill="K4")
check("S4.3 multiplicity 9 = N_fam^2 = %d; top singular value 3 = "
      "N_fam (row regularity)" % (N_fam ** 2),
      N_fam ** 2 == 9 and N_fam == 3 and rows == [N_fam] * 15,
      kill="K4")

ovoid_rows = []
ok_ker = True
for q in arf1:
    u = [0] * 15
    for v in NZ15:
        u[didx[duad_of[v]]] = 3 * (1 if q[WIDX[v]] == 0 else 0) - 1
    ovoid_rows.append(u)
    Ntu = [sum(N[i][j] * u[i] for i in range(15)) for j in range(15)]
    if any(e != 0 for e in Ntu):
        ok_ker = False
rk_ov = frac_rank(ovoid_rows)
check("S4.4 the SIX ovoid indicators 3*1_{O_q} - 1 (q Arf-1) lie in "
      "ker N^T and SPAN it: rank = %d == 5 (v774 S9.4 transported)"
      % rk_ov, ok_ker and rk_ov == 5, kill="K4")

# ----------------------------------------------------------------------
section("S5: the recovery value -- sing(N/3) = {1, 2/3 x9, 0 x5}")
# ----------------------------------------------------------------------
X9 = sp.Matrix(NNt) / 9
cpX = X9.charpoly(x).as_expr()
cpX_t = sp.expand((x - 1) * (x - sp.Rational(4, 9)) ** 9 * x ** 5)
check("S5.1 charpoly((N/3)(N/3)^T) = (x-1)(x-4/9)^9 x^5 exact -- "
      "sing(N/3) = {1, 2/3 x9, 0 x5}: THE RECOVERY VALUE 2/3",
      sp.expand(cpX - cpX_t) == 0, kill="K4")
check("S5.2 2/3 = (N_fam - 1)/N_fam = %s (the corpus recovery "
      "survival, v327)" % Fr(N_fam - 1, N_fam),
      Fr(N_fam - 1, N_fam) == Fr(2, 3), kill="K4")

# ----------------------------------------------------------------------
section("S6: the compiler clock -- (2/3)^6 exponentiation identity")
# ----------------------------------------------------------------------
X3 = X9 ** 3        # three PSD double-steps = six channel legs
cpX3 = X3.charpoly(x).as_expr()
cpX3_t = sp.expand((x - 1) * (x - sp.Rational(64, 729)) ** 9 * x ** 5)
check("S6.1 EXPONENTIATION IDENTITY: charpoly(((N/3)(N^T/3))^3) = "
      "(x-1)(x-64/729)^9 x^5 exact, and 64/729 == (2/3)^6 == the "
      "deployed lambda_2 of {1, (2/3)^6, (1/3)^6} (v330/v486; the "
      "sixth power is the compiler clock, v814)",
      sp.expand(cpX3 - cpX3_t) == 0
      and Fr(2, 3) ** 6 == Fr(64, 729), kill="K5")
check("S6.2 TYPED GAP re-affirmed: NO (1/3)^6 mode in the doily "
      "channel -- 1/729 is NOT a root of the six-step charpoly (the "
      "deployed (1/3)^6 lives on the clock side, v814 "
      "SIXSTEP-CLOCK-ONLY [E], cited, consistent)",
      cpX3.subs(x, sp.Rational(1, 729)) != 0
      and Fr(1, 3) ** 6 == Fr(1, 729), kill="K5")

# ----------------------------------------------------------------------
section("C: controls (must fire; same row sums, wrong pairing)")
# ----------------------------------------------------------------------
TARGET_CP = cpNNt_t
N1 = [[1 if (j - i) % 15 in (0, 1, 2) else 0 for j in range(15)]
      for i in range(15)]
rk1 = frac_rank(N1)
N1N1t = [[sum(N1[i][k] * N1[j][k] for k in range(15))
          for j in range(15)] for i in range(15)]
cp1 = sp.Matrix(N1N1t).charpoly(x).as_expr()
check("C1 FIRES: circulant 3-regular pairing: row/col sums 3, but "
      "rank = %d != 10, dim ker = %d != 5, charpoly(N'N'^T) != target"
      % (rk1, 15 - rk1),
      all(sum(r) == 3 for r in N1)
      and all(sum(N1[i][j] for i in range(15)) == 3 for j in range(15))
      and rk1 != 10 and (15 - rk1) != 5
      and sp.expand(cp1 - TARGET_CP) != 0, kill="K6")

_LCG = [20260807]


def lcg():
    _LCG[0] = (6364136223846793005 * _LCG[0]
               + 1442695040888963407) % (1 << 64)
    return _LCG[0]


def rand_perm():
    p = list(range(15))
    for i in range(14, 0, -1):
        j = lcg() % (i + 1)
        p[i], p[j] = p[j], p[i]
    return p


perms = []
while len(perms) < 3:
    cand = rand_perm()
    if all(all(cand[i] != q[i] for i in range(15)) for q in perms):
        perms.append(cand)
N2 = [[sum(1 for q in perms if q[i] == j) for j in range(15)]
      for i in range(15)]
rk2 = frac_rank(N2)
N2N2t = [[sum(N2[i][k] * N2[j][k] for k in range(15))
          for j in range(15)] for i in range(15)]
cp2 = sp.Matrix(N2N2t).charpoly(x).as_expr()
check("C2 FIRES: frozen-seed LCG pairing (3 disjoint permutations, "
      "row/col sums 3): (rank, charpoly) = (%d, ...) != (10, doily "
      "target)" % rk2,
      all(sum(r) == 3 for r in N2)
      and all(sum(N2[i][j] for i in range(15)) == 3 for j in range(15))
      and not (rk2 == 10 and sp.expand(cp2 - TARGET_CP) == 0),
      kill="K6")

# ----------------------------------------------------------------------
section("VERDICT")
# ----------------------------------------------------------------------
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
if not controls_ok:
    VERDICT = "CONTROL-DEAD"
elif KILLS:
    VERDICT = {"K1": "DOILY-BROKEN", "K2": "GRAM-BROKEN",
               "K3": "BRIDGE-BROKEN", "K4": "RANK-MISMATCH",
               "K5": "CLOCK-MISMATCH"}.get(KILLS[0], "CONTROL-DEAD")
else:
    VERDICT = "DOILY-PASCAL-RANK-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
print("  * v774 S9 (B = I + A_KG(6,2), B B^T = 4I + 3J, spectrum")
print("    7/2^9/(-2)^5, ovoid (-2)-eigenspace) and v814 A1 (doily")
print("    route, sv(N/3) = {1, 2/3 x9, 0 x5}, six-step (2/3)^6):")
print("    both sides are ONE incidence map -- N N^T = B + 2I shifts")
print("    the spectrum 7/2/-2 -> 9/4/0, so v774's (-2)-eigenspace IS")
print("    v814's kernel.")
print("  * THE RANK THEOREM (new normal form): rank N = 10 = A_Lambda")
print("    (decuple), dim ker N = 5 = g_car (carrier), multiplicity")
print("    9 = N_fam^2, top 3 = N_fam, recovery 2/3 = (N_fam-1)/N_fam")
print("    -- the P2 integers are the singular-value data of the")
print("    Cremona-Richmond incidence.")
print("  * v330/v486 deployed transfer {1,(2/3)^6,(1/3)^6}: lambda_2")
print("    reproduced exactly by the six-leg alternation; the (1/3)^6")
print("    gap stays typed on the clock side (v814, no upgrade).")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT == "DOILY-PASCAL-RANK-EXACT") else 1)
