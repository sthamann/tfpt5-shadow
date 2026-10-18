#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v852 -- ARF.VACUUM.SYNDROME.01 + OVOID.DECODER.01: the Arf-vacuum syndrome theorem and the integral five-mode decoder -- the corpus's flat counts, orbit splits, Hecke matches and code enumerators compress into ONE two-bit syndrome table on the Hamming code, and the doily recovery channel gains an explicit integral inverse with the S6 standard representation identified, ONE module from two probes (24/24 + 23/23 checks, zero fails, verdicts ARF-VACUUM-SYNDROME-EXACT and OVOID-DECODER-EXACT; discovery probes affine_arf_vacuum_probe.py and doily_ovoid_decoder_probe.py, 2026-08-07, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, exact integer/Fraction/sympy arithmetic, <1 s).  PART A, THE ARF-VACUUM SYNDROME: (a) THE ARF BIT THEOREM -- for every affine flat t+U of (F_2^4, hb) the Arf bit a(t+U) = sum_{x in t+U} q*(x) mod 2 equals the direction bit hb(u,v) of the underlying plane U for ALL 140 flats (position independence: all 4 cosets agree; the direction bit is well-defined on all 35 planes); (b) THE TWO-BIT SYNDROME CENSUS -- (s_vac, s_Arf) = (origin bit, direction bit) splits the 140 flats EXACTLY into 15/20/45/60 (doily lines / non-isotropic lines / isotropic off-planes / non-isotropic off-planes), reproducing v821's 35 = 15 + 20 and v834's 105 = 45 + 60 as rows of ONE table; (c) THE LOCAL HECKE THEOREM -- at EVERY nonzero point x: 3 isotropic + 4 non-isotropic directions through x with the isotropic ones in bijection with the points of x^perp/<x>, and the 28 off-origin flats through x split 12 + 16 with A_3 + B_3 = 28 = sigma_3(3) and A_3 - B_3 = -4 = a_3 (the eta-product Hecke eigenvalue, v820/v535 rebuilt LOCALLY at all 15 points; 28 - (-4) = 32 = 2^5 the pi_cusp denominator, v785); (d) THE CODE PENCIL -- H = ker X = [15,11,3] (weight-3 words == the 35 lines, weight-4 == the 105 off-origin flats, SET EQUALITIES), H^perp = the simplex code, and the CANONICITY LEMMA: all 16 refinements differ from q* by simplex words, hence induce ONE Arf functional on H; below H sit D = [15,10,4] (v819's enumerator EXACT), C_iso and C_non = [15,10,3] (weight-3 words == the 15 doily lines resp. the 20 non-isotropic lines), all pairwise intersections == K = [15,9,4], all pairwise sums == H, and the syndrome map H -> F_2^2 is surjective with four fibers of 512; (e) RM(2,4) RESTORED -- puncturing RM(2,4) = [16,11,4] at the vacuum coordinate gives H, shortening gives D, and c -> (p.c, c) is a bijection H -> RM(2,4): THE VACUUM BIT IS THE PARITY BIT, and on the 140 flat words the restored coordinate == s_vac exactly.  Controls fire: the dot form admits 0 refinements and an ill-defined direction bit; an Arf-0 refinement leaves the table invariant but breaks the labeling (zero set 10 != 6, not an ovoid); a frozen-LCG column permutation preserves [15,11,3] but destroys the line labeling (31/35 weight-3 supports not lines).  PART B, THE OVOID DECODER: the Cremona-Richmond incidence N (15 duads x 15 synthemes) and the six ovoid vectors v_a = 3*1_{O_a} - 1 satisfy (a) N^T v_a = 0 for ALL six a (every syntheme covers each letter exactly once -- the kernel facts from perfect matchings), any five of the six are independent, sum_a v_a = 0; (b) the Gram V^T V = 36I - 6J ENTRYWISE; (c) SNF(N) = diag(1^10, 0^5) EXACT over Z -- rank 10 = C(g_car, 2), kernel 5 = g_car, NO TORSION, with a det-+-1 10x10 minor exhibited; (d) the Moore-Penrose closed form N+ = N^T/4 - J/36 verified against all four Penrose axioms in exact Q; (e) the carrier projector P5 = I/2 - B/4 + J/12 == (1/36) sum_a v_a v_a^T entrywise, P5^2 = P5 = P5^T, P5 N = 0, tr P5 = 5 = g_car, N N+ = I - P5 (the visible-part projector); (f) THE MOD-2 SHADOW: v_a mod 2 == q_a entrywise and ker_F2(N^T) == A_q = [15,5,6] (weight enumerator 1 + 10z^6 + 15z^8 + 6z^10) -- THE THREE-RING CORRESPONDENCE: the same kernel is (R) the ovoid span, (Z) torsion-free rank 5, (F_2) the code A_q; (g) THE DECODER DEMO: mhat = (1/4)N y - (1/36)J y == (I - P5) m EXACTLY on the predeclared 6-vector test set (kernel modes invisible, im(N) modes fully visible) -- the recovery channel of DOILY.PASCAL.RANK.01 now has an explicit integral inverse, not just a spectrum; (h) THE S6 IDENTIFICATION: N is S6-equivariant and tr(P5 Pi(pi)) == fix(pi) - 1 for representatives of ALL 11 conjugacy classes -- ker N^T IS the 5-dimensional standard representation: the five-slot carrier is the sixth-root-free shadow of six ovoid modes with one relation.  Control fires: a frozen-LCG wrong pairing (same row/col sums 3) breaks SNF (torsion 3 appears), the F_2 kernel (4 != 32) and the ovoid kernel property.  The P2 integers remain the singular-value data of the doily; no marker moves -- the compression is a normal form plus an inverse, not a new claim.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes affine_arf_vacuum_probe.py (24/24,
verdict ARF-VACUUM-SYNDROME-EXACT) and doily_ovoid_decoder_probe.py
(23/23, verdict OVOID-DECODER-EXACT), both 2026-08-07, re-run
identically at promotion.  ROUND-31 EMBEDDING CONVENTION: both frozen
probe sources are embedded BYTE-EXACT (raw strings below) and
executed verbatim in isolated module namespaces -- the printed
FROZEN_SPEC SHA-256 values reproduce exactly, and when the original
files are present the harness verifies byte-equality (provenance ward
inside the pattern gate).  The pattern gates encode the frozen
expected censuses (24 + 23 checks, zero FAILs, both verdicts, exit
0).  The original probe files live verbatim in
experiments/tfpt-discovery/.

FIREWALL: pure finite algebra over F_2 / Z / Q (both probes rebuild
their carriers from scratch and import only tfpt_constants); the only
RNG is the frozen-seed LCG of the declared wrong-pairing /
wrong-labeling controls (v775 C2 precedent).  NO RH claim.
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

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_ARF = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""affine_arf_vacuum_probe -- ARF.VACUUM.SYNDROME.01: the Arf-vacuum
syndrome theorem.  Every affine 2-flat A = t + U of V = F2^4 carries a
POSITION-INDEPENDENT Arf bit a(A) = sum_{x in A} q*(x) mod 2 equal to
the symplectic pairing of its direction plane U; together with the
vacuum bit o(A) = [0 in A] it grades the 140 flats into the
15/20/45/60 census, localizes the Hecke pair (A_3, B_3) = (12, 16) at
EVERY point, and realizes the whole table as the syndrome table of a
two-functional code pencil inside the Hamming code [15,11,3]
(finite-geometry module 1 of the 2026-08-07 evening code-complex
round).

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; all
statements verified over ALL objects, never samples; exact F2/integer
arithmetic; the only RNG is the frozen-seed LCG of control C3):

 S1  CARRIER: corpus form hb(v,w) = (sum v)(sum w) - v.w mod 2 (the
     J - I Gram, v774/v752 convention) is alternating + nondegenerate;
     brute force over 2^16 gives EXACTLY 16 quadratic refinements,
     Arf census 6 + 10; the frozen selector (sigma-invariant -> 4,
     q(A)=1 -> 2, q(F_Sigma)=0 -> 1) picks the UNIQUE q* (Arf 1), and
     q* == the iota-weight rule wt(iota(v))/2 mod 2 on all 16 labels
     (NORMALFORM.CFIN.01 S4.3 anchor); {q*=0}\{0} = the 5 = g_car
     carrier points (the ovoid), {q*=1} = the 10; PG(3,2): 15 points,
     35 lines, 15 isotropic (doily) + 20 non-isotropic; the 5bar
     meets every isotropic line exactly once.

 S2  (a) THE ARF BIT IS A DIRECTION INVARIANT: the derivation
     identity q*(x+y) = q*(x) + q*(y) + hb(x,y) holds on ALL 256
     pairs; for every 2-dim U = {0,u,v,u+v} the pairing hb over all
     3 basis pairs is CONSTANT (the direction bit a(U) is
     well-defined); for ALL 140 flats t + U the Arf bit
     sum_{x in t+U} q*(x) mod 2 == a(U) -- position-independent (all
     4 cosets of each U agree; one-line proof: expand the four terms
     by the derivation identity, everything cancels except hb(u,v)).

 S3  (b) THE TWO-BIT SYNDROME TABLE: (o, a) in F2^2 splits the 140
     flats EXACTLY as
        (o,a) = (1,0) isotropic through origin      15
        (o,a) = (1,1) non-isotropic through origin  20
        (o,a) = (0,0) isotropic off-origin          45
        (o,a) = (0,1) non-isotropic off-origin      60
     with the identities 35 = 15 + 20, 105 = 45 + 60 (v834/PG32.FLAGS
     45/60 split re-derived) and the a-grading 140 = 60 + 80
     (60 isotropic = 15 + 45, 80 non-isotropic = 20 + 60).

 S4  (c) THE LOCAL HECKE COUNT THEOREM (all 15 points, no samples):
     for every nonzero x: exactly 7 lines through x; EXACTLY 3
     isotropic directions contain x, in bijection with the 3 nonzero
     points of x^perp/<x>, and 4 non-isotropic; 35 flats through x =
     7 linear + 28 off-origin (v821 S2 counting lemma re-derived);
     the off-origin planes through x split 12 isotropic + 16
     non-isotropic:  A_3 = 12 = 15 - 3, B_3 = 16 = 20 - 4,
     A_3 + B_3 = 28 = sigma3(3), A_3 - B_3 = -4 = a_3 (the eta
     product q prod(1-q^{2m})^4(1-q^{4m})^4 rebuilt inline to q^10).
     CORPUS CROSS-CHECK (cited, re-verified): v820 S4.2 (G3)
     PLANEFRAMES A_3 = 12 / B_3 = 16 plane-count Hecke match; v535
     HECKE.GEOM.01 a_3 = -4; v785 CHECK32: 28 - (-4) = 32 = 2^5 = the
     cusp projector denominator (28 - T_3)/32.  NEW content here: the
     count is uniform at EVERY point and the isotropic count is the
     point census of x^perp/<x>.

 S5  (d) THE CODE PENCIL: X = the 4 x 15 matrix of nonzero column
     vectors (column i = point i+1), p = all-ones, q = (q*(x)):
       H     = ker X                    = [15,11,3] Hamming
       D     = H  n  ker p              = [15,10,4]
       C_iso = H  n  ker q              = [15,10,3]
       C_non = H  n  ker(p+q)           = [15,10,3]
       K     = H  n  ker p  n  ker q    = [15, 9,4]
     with (i) weight-3 words of H == the 35 lines and weight-4 words
     == the 105 off-origin flats (set equalities, the explicit
     bijections); (ii) H^perp == the simplex code {hb(v,.)} u {0} and
     THE CANONICITY LEMMA: all 16 refinements induce the SAME
     functional on H (any two differ by a simplex word), so the Arf
     syndrome is refinement-independent on H; (iii) D carries the
     v819 S4 enumerator 1 + 105z^4 + 280z^6 + 435z^8 + 168z^10 +
     35z^12; C_iso has weight-3 words == the 15 doily lines and
     weight-4 words == the 45 isotropic off-origin flats; C_non has
     weight-3 words == the 20 non-isotropic lines; K = [15,9,4] with
     weight-4 words == the same 45; (iv) the intersection identities:
     ALL pairwise intersections of {D, C_iso, C_non} equal K and ALL
     pairwise sums equal H (the pencil over K); the syndrome map
     H -> F2^2, c -> (p.c, q.c) is surjective with four fibers of
     size 512; (v) the 140-WORD SYNDROME TABLE: every flat word
     (origin flats punctured at 0 -> weight 3, off-origin -> weight
     4) lies in H and its syndrome (s_vac, s_Arf) = (p.c, q.c)
     REPRODUCES the geometric class of S3 exactly: (1,0) x15 doily
     lines, (1,1) x20, (0,0) x45, (0,1) x60.

 S6  PUNCTURE / SHORTEN / VACUUM BIT: RM(2,4) = [16,11,4] rebuilt;
     puncture at the vacuum coordinate == H (set equality), shorten
     == D (set equality); the parity extension c -> (p.c, c) is a
     bijection H -> RM(2,4) -- THE VACUUM BIT IS THE PARITY BIT that
     restores RM(2,4), and on the 140 flat words the restored
     coordinate equals s_vac (origin membership) exactly.

 C   CONTROLS (must fire; frozen fire rules):
     C1 DOT FORM (no Arf grading): the non-alternating dot form
        admits ZERO quadratic refinements (2^16 census) AND the
        direction bit is ILL-DEFINED (witness U = <e1,e2>: pair
        values dot(e1,e2) = 0 != 1 = dot(e1,e1+e2)) -- no table.
     C2 WRONG q (Arf 0), frozen prediction: the syndrome TABLE is
        INVARIANT (an Arf-0 refinement induces the same functional
        on H -- the canonicity lemma corollary, measured), but the
        VACUUM/OVOID LABELING breaks: |{q0=0}| = 10 != 6, the zero
        set minus 0 (9 points) is NOT an ovoid (doily-line meeting
        census != all-1), and the pencil vector has weight 6 != 10.
        FIRE = labeling breaks AND invariance measured as stated.
     C3 RANDOM COLUMN PERMUTATION (frozen-seed LCG): parameters are
        PRESERVED (same weight enumerator, [15,11,3]) but the
        geometric labeling BREAKS: the permuted code differs as a
        set, and some weight-3 supports are no longer lines (not
        closed under XOR) -- typed PARAMS-KEPT-LABELS-BROKEN.

KILLS (any one fires => typed failure):
  K1 carrier / selector / derivation identity / position
     independence breaks                             -> ARF-BIT-BROKEN
  K2 the 15/20/45/60 census or an identity breaks    -> SYNDROME-CENSUS-BROKEN
  K3 a local Hecke count (3/4, 12/16, 28, -4) breaks -> HECKE-COUNT-MISMATCH
  K4 a code parameter / set equality / pencil
     identity / canonicity lemma breaks              -> CODE-PENCIL-BROKEN
  K5 puncture / shorten / parity restoration breaks  -> PUNCTURE-BROKEN
  K6 a control does not fire                         -> CONTROL-DEAD

VERDICT (frozen enum): ARF-VACUUM-SYNDROME-EXACT / ARF-BIT-BROKEN /
SYNDROME-CENSUS-BROKEN / HECKE-COUNT-MISMATCH / CODE-PENCIL-BROKEN /
PUNCTURE-BROKEN / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact F2/integer arithmetic; no floats; the only
RNG is the frozen-seed LCG of control C3.  NO physics claim.

Sources (read-only, machinery rebuilt inline):
finite_compiler_normal_form_probe.py + cfin_uniqueness_probe.py (q*,
selector, iota), pg32_flag_completion_probe.py / v834 (140 = 105 + 35,
45/60 split), v819_prime_packet_rm14 (D enumerator), v820 S4.2 (G3)
(A_3/B_3 plane-count Hecke match), v821 S2 (35/7/28 counting lemmas),
v535 HECKE.GEOM.01 + v785 CHECK32 (a_3 = -4, 32 = 28 + 4),
v774/v752 (form + refinements), tfpt_constants (g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/affine_arf_vacuum_probe.py
"""
import hashlib
import itertools
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "verification"))
from tfpt_constants import g_car  # noqa: E402  (read-only import)

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


print("ARF.VACUUM.SYNDROME.01 -- the Arf-vacuum syndrome theorem")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ------------------------------------------------------- bit machinery
PTS = list(range(16))                   # F2^4 as ints, bit k = coord k
NZ = list(range(1, 16))


def pc(v):
    return bin(v).count("1")


def hb(v, w):
    # corpus form (v774 GJI = J - I): (sum v)(sum w) - v.w mod 2
    return ((pc(v) & 1) & (pc(w) & 1)) ^ (pc(v & w) & 1)


HBT = [[hb(v, w) for w in PTS] for v in PTS]
DOT = [[pc(v & w) & 1 for w in PTS] for v in PTS]


def refinements_of(tab):
    """All q: V -> F2 with q(x+y)+q(x)+q(y) = tab[x][y] (2^16 census)."""
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            qi = q[i]
            row = tab[i]
            for j in range(16):
                if q[i ^ j] ^ qi ^ q[j] != row[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


def sig_int(v):
    b = [(v >> k) & 1 for k in range(4)]
    w = (b[2], b[0], b[1], b[3])        # family 3-cycle, anchor fixed
    return sum(w[k] << k for k in range(4))


# ======================================================================
section("S1: carrier -- form, refinements, selector, q*, doily")
# ======================================================================
check("S1.1 hb alternating (16/16 diag zero) + nondegenerate (empty "
      "radical)",
      all(HBT[v][v] == 0 for v in PTS)
      and all(any(HBT[v][w] for w in NZ) for v in NZ), kill="K1")

REFS = refinements_of(HBT)
ARF1 = sorted(q for q in REFS if sum(1 for i in PTS if q[i] == 0) == 6)
ARF0 = sorted(q for q in REFS if sum(1 for i in PTS if q[i] == 0) == 10)
A_INT, FSIG_INT = 8, 7                  # (0,0,0,1) and (1,1,1,0)
siginv = [q for q in REFS if all(q[sig_int(v)] == q[v] for v in PTS)]
cand_a = [q for q in siginv if q[A_INT] == 1]
cand = [q for q in cand_a if q[FSIG_INT] == 0]
check("S1.2 EXACTLY 16 refinements; Arf census 6 + 10; selector "
      "16 -> %d -> %d -> %d == 1 (unique q*, Arf 1)"
      % (len(siginv), len(cand_a), len(cand)),
      len(REFS) == 16 and len(ARF1) == 6 and len(ARF0) == 10
      and len(siginv) == 4 and len(cand_a) == 2 and len(cand) == 1
      and cand[0] in ARF1, kill="K1")
QS = cand[0]

qwt = tuple(((pc(v) + (pc(v) & 1)) // 2) % 2 for v in PTS)
check("S1.3 q* == the iota-weight rule wt(iota(v))/2 mod 2 on all 16 "
      "labels (NORMALFORM.CFIN.01 S4.3 anchor)", qwt == QS, kill="K1")

FIVE = [v for v in NZ if QS[v] == 0]
TEN = [v for v in NZ if QS[v] == 1]
SUBS = sorted({frozenset({0, u, v, u ^ v})
               for u, v in itertools.combinations(NZ, 2)}, key=sorted)
UBIT = {}
well_defined = True
for U in SUBS:
    nz = sorted(U - {0})
    vals = {HBT[a][b] for a, b in itertools.combinations(nz, 2)}
    if len(vals) != 1:
        well_defined = False
    UBIT[U] = min(vals)
ISO = [U for U in SUBS if UBIT[U] == 0]
NONISO = [U for U in SUBS if UBIT[U] == 1]
check("S1.4 PG(3,2): 15 points, %d lines = 35; doily split %d "
      "isotropic + %d non-isotropic; {q*=0}\\{0} = %d == g_car = %d "
      "points; ovoid: the 5bar meets every isotropic line exactly once"
      % (len(SUBS), len(ISO), len(NONISO), len(FIVE), g_car),
      len(SUBS) == 35 and len(ISO) == 15 and len(NONISO) == 20
      and len(FIVE) == 5 == g_car and len(TEN) == 10
      and all(sum(1 for x in U - {0} if x in FIVE) == 1 for U in ISO),
      kill="K1")

# ======================================================================
section("S2: (a) the Arf bit is a position-independent direction bit")
# ======================================================================
check("S2.1 derivation identity q*(x+y) = q*(x) + q*(y) + hb(x,y) on "
      "ALL 256 pairs",
      all(QS[x ^ y] == (QS[x] + QS[y] + HBT[x][y]) % 2
          for x in PTS for y in PTS), kill="K1")
check("S2.2 the direction bit is WELL-DEFINED: for all 35 planes U "
      "the pairing hb(u,v) is constant over the 3 basis pairs",
      well_defined, kill="K1")

FLATS = []
for U in SUBS:
    for cs in sorted({frozenset(t ^ u for u in U) for t in PTS},
                     key=sorted):
        FLATS.append((U, cs))
ok_arf = all(sum(QS[x] for x in cs) % 2 == UBIT[U] for U, cs in FLATS)
ok_cosets = all(len({sum(QS[x] for x in cs) % 2
                     for U2, cs in FLATS if U2 == U}) == 1
                for U in SUBS)
check("S2.3 ARF BIT THEOREM: a(t+U) = sum_{x in t+U} q*(x) mod 2 == "
      "hb(u,v) for ALL 140 flats; all 4 cosets of each U agree "
      "(position independence)",
      len(FLATS) == 140 and ok_arf and ok_cosets, kill="K1")

# ======================================================================
section("S3: (b) the two-bit syndrome census 15/20/45/60")
# ======================================================================
cls = Counter(((1 if 0 in cs else 0), UBIT[U]) for U, cs in FLATS)
check("S3.1 (o,a) census: (1,0)=%d==15, (1,1)=%d==20, (0,0)=%d==45, "
      "(0,1)=%d==60"
      % (cls[(1, 0)], cls[(1, 1)], cls[(0, 0)], cls[(0, 1)]),
      cls[(1, 0)] == 15 and cls[(1, 1)] == 20
      and cls[(0, 0)] == 45 and cls[(0, 1)] == 60, kill="K2")
check("S3.2 identities: 35 = 15 + 20 (origin), 105 = 45 + 60 (off, "
      "v834 split), a-graded 140 = 60 + 80 (iso 15+45, non-iso 20+60)",
      cls[(1, 0)] + cls[(1, 1)] == 35
      and cls[(0, 0)] + cls[(0, 1)] == 105
      and cls[(1, 0)] + cls[(0, 0)] == 60
      and cls[(1, 1)] + cls[(0, 1)] == 80
      and 60 + 80 == 140, kill="K2")

# ======================================================================
section("S4: (c) the local Hecke count theorem at ALL 15 points")
# ======================================================================
ok_local = True
ok_quot = True
ok_off = True
for x in NZ:
    iso_x = [U for U in ISO if x in U]
    non_x = [U for U in NONISO if x in U]
    xperp = [v for v in PTS if HBT[x][v] == 0]
    quot_nz = {frozenset({y, y ^ x}) for y in xperp if y not in (0, x)}
    img = {frozenset(U - {0, x}) for U in iso_x}
    if not (len(iso_x) == 3 and len(non_x) == 4
            and len(xperp) == 8 and len(quot_nz) == 3
            and img == quot_nz):
        ok_local = False
    thr = [(U, cs) for U, cs in FLATS if x in cs]
    lin = [(U, cs) for U, cs in thr if 0 in cs]
    off = [(U, cs) for U, cs in thr if 0 not in cs]
    off_iso = [(U, cs) for U, cs in off if UBIT[U] == 0]
    if not (len(thr) == 35 and len(lin) == 7 and len(off) == 28):
        ok_quot = False
    if not (len(off_iso) == 12 and len(off) - len(off_iso) == 16):
        ok_off = False
check("S4.1 for EVERY nonzero x: 3 isotropic + 4 non-isotropic "
      "directions contain x, and the isotropic ones are in bijection "
      "with the 3 nonzero points of x^perp/<x> (all 15 points)",
      ok_local, kill="K3")
check("S4.2 for EVERY x: 35 flats through x = 7 linear + 28 "
      "off-origin (v821 S2 lemma); the 28 split 12 isotropic + 16 "
      "non-isotropic = (15-3) + (20-4) (all 15 points)",
      ok_quot and ok_off, kill="K3")


def eta_f8_a(n_max):
    """f8 = q prod (1-q^{2m})^4 (1-q^{4m})^4; returns a[1..n_max+1]."""
    c = [0] * (n_max + 1)
    c[0] = 1
    for step in (2, 4):
        for m in range(step, n_max + 1, step):
            for _ in range(4):
                for j in range(n_max, m - 1, -1):
                    c[j] -= c[j - m]
    a = [0] * (n_max + 2)
    for n in range(1, n_max + 2):
        if n - 1 <= n_max:
            a[n] = c[n - 1]
    return a


A3 = eta_f8_a(10)[3]
SIG33 = sum(d ** 3 for d in (1, 3))
check("S4.3 HECKE MATCH: A_3 + B_3 = 12 + 16 = 28 == sigma3(3) = %d; "
      "A_3 - B_3 = 12 - 16 = -4 == a_3 = %d (eta product rebuilt); "
      "corpus: v820 S4.2 (G3) A_3 = 12 / B_3 = 16, v535 a_3 = -4, "
      "v785: 28 - (-4) = 32 = 2^5 = pi_cusp denominator"
      % (SIG33, A3),
      SIG33 == 28 == 12 + 16 and A3 == -4 == 12 - 16
      and 28 - A3 == 32 == 2 ** 5, kill="K3")

# ======================================================================
section("S5: (d) the code pencil H > {D, C_iso, C_non} > K")
# ======================================================================


def xor_pts(m):
    s = 0
    while m:
        b = m & -m
        s ^= b.bit_length()             # bit i <-> point i+1
        m ^= b
    return s


def wmask(pts_set):
    return sum(1 << (x - 1) for x in pts_set)


H = [m for m in range(1 << 15) if xor_pts(m) == 0]
TENM = wmask(TEN)
LINES3 = {wmask(U - {0}) for U in SUBS}
FLAT4 = {wmask(cs) for U, cs in FLATS if 0 not in cs}
weH = Counter(pc(m) for m in H)
check("S5.1 H = ker X = [15,11,3]: |H| = %d == 2048; weight-3 words "
      "== the 35 lines (set equality) and weight-4 words == the 105 "
      "off-origin flats (set equality); enumerator %s"
      % (len(H), dict(sorted(weH.items()))),
      len(H) == 2048 and min(pc(m) for m in H if m) == 3
      and {m for m in H if pc(m) == 3} == LINES3
      and {m for m in H if pc(m) == 4} == FLAT4
      and weH[3] == 35 and weH[4] == 105 and weH[5] == 168
      and weH[6] == 280 and weH[7] == 435, kill="K4")


def bit_basis(vs):
    basis = []
    for v in vs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
    return basis


HBASIS = bit_basis(H)
DUAL = [w for w in range(1 << 15)
        if all(pc(w & b) % 2 == 0 for b in HBASIS)]
SIMP = {0} | {wmask({x for x in NZ if HBT[v][x] == 1}) for v in NZ}
QVEC = {q: wmask({x for x in NZ if q[x] == 1}) for q in REFS}
check("S5.2 H^perp == the simplex code {hb(v,.)} u {0} (16 words, "
      "set equality); CANONICITY LEMMA: all 16 refinements differ "
      "from q* by a simplex word => ONE Arf functional on H",
      len(HBASIS) == 11 and set(DUAL) == SIMP and len(SIMP) == 16
      and all((QVEC[q] ^ QVEC[QS]) in SIMP for q in REFS), kill="K4")

D = [m for m in H if pc(m) % 2 == 0]
CISO = [m for m in H if pc(m & TENM) % 2 == 0]
CNON = [m for m in H if (pc(m) + pc(m & TENM)) % 2 == 0]
K = [m for m in H if pc(m) % 2 == 0 and pc(m & TENM) % 2 == 0]
weD = Counter(pc(m) for m in D)
ISO3 = {wmask(U - {0}) for U in ISO}
NON3 = {wmask(U - {0}) for U in NONISO}
ISO4 = {wmask(cs) for U, cs in FLATS if 0 not in cs and UBIT[U] == 0}
check("S5.3a D = [15,10,4]: dims (%d,%d,%d,%d) == (1024,1024,1024,"
      "512); v819 S4 enumerator 1 + 105z^4 + 280z^6 + 435z^8 + "
      "168z^10 + 35z^12 EXACT"
      % (len(D), len(CISO), len(CNON), len(K)),
      len(D) == len(CISO) == len(CNON) == 1024 and len(K) == 512
      and dict(weD) == {0: 1, 4: 105, 6: 280, 8: 435, 10: 168,
                        12: 35}, kill="K4")
check("S5.3b C_iso = [15,10,3]: weight-3 words == the 15 doily lines "
      "(set equality), weight-4 == the 45 isotropic off-origin flats "
      "(set equality)",
      {m for m in CISO if pc(m) == 3} == ISO3 and len(ISO3) == 15
      and {m for m in CISO if pc(m) == 4} == ISO4 and len(ISO4) == 45,
      kill="K4")
check("S5.3c C_non = [15,10,3]: weight-3 words == the 20 "
      "non-isotropic lines (set equality); K = [15,9,4]: no weight-3, "
      "weight-4 words == the same 45 isotropic off flats",
      {m for m in CNON if pc(m) == 3} == NON3 and len(NON3) == 20
      and not any(pc(m) == 3 for m in K)
      and {m for m in K if pc(m) == 4} == ISO4
      and min(pc(m) for m in K if m) == 4, kill="K4")

sD, sI, sN, sK, sH = set(D), set(CISO), set(CNON), set(K), set(H)
ok_int = (sD & sI == sK and sD & sN == sK and sI & sN == sK)
ok_sum = (len(bit_basis(D + CISO)) == 11
          and len(bit_basis(D + CNON)) == 11
          and len(bit_basis(CISO + CNON)) == 11)
fib = Counter((pc(m) & 1, pc(m & TENM) & 1) for m in H)
check("S5.4 PENCIL IDENTITIES: all pairwise intersections == K, all "
      "pairwise sums == H (rank 11); syndrome map H -> F2^2 "
      "surjective, four fibers of 512 (%s)"
      % dict(sorted(fib.items())),
      ok_int and ok_sum and sD < sH and sI < sH and sN < sH
      and all(fib[s] == 512 for s in
              ((0, 0), (0, 1), (1, 0), (1, 1))), kill="K4")

table = Counter()
ok_words = True
for U, cs in FLATS:
    m = wmask(cs - {0}) if 0 in cs else wmask(cs)
    if m not in sH:
        ok_words = False
    s_vac, s_arf = pc(m) & 1, pc(m & TENM) & 1
    if s_vac != (1 if 0 in cs else 0) or s_arf != UBIT[U]:
        ok_words = False
    table[(s_vac, s_arf)] += 1
check("S5.5 THE 140-WORD SYNDROME TABLE: every flat word lies in H; "
      "(s_vac, s_Arf) == (origin bit, direction bit) for ALL 140; "
      "classes (1,0)=%d, (1,1)=%d, (0,0)=%d, (0,1)=%d == 15/20/45/60"
      % (table[(1, 0)], table[(1, 1)], table[(0, 0)], table[(0, 1)]),
      ok_words and table[(1, 0)] == 15 and table[(1, 1)] == 20
      and table[(0, 0)] == 45 and table[(0, 1)] == 60, kill="K4")
print("    syndrome table: (s_vac,s_Arf)=(1,0) doily lines x15 | "
      "(1,1) non-iso lines x20 |")
print("                    (0,0) iso off-planes x45 | (0,1) non-iso "
      "off-planes x60")

# ======================================================================
section("S6: puncture / shorten -- the vacuum bit restores RM(2,4)")
# ======================================================================


def m16(pts_set):
    return sum(1 << v for v in pts_set)


gens16 = ([0xFFFF]
          + [m16({v for v in PTS if (v >> k) & 1}) for k in range(4)]
          + [m16({v for v in PTS if ((v >> k) & 1) and ((v >> l) & 1)})
             for k, l in itertools.combinations(range(4), 2)])
RM = {0}
for g in gens16:
    RM |= {w ^ g for w in RM}
PUNC = {w >> 1 for w in RM}
SHORT = {w >> 1 for w in RM if not (w & 1)}
REST = {(c << 1) | (pc(c) & 1) for c in H}
check("S6.1 RM(2,4) = [16,11,4] (|RM| = %d == 2048, min wt 4); "
      "puncture at the vacuum coordinate == H (set equality); "
      "shorten == D (set equality)" % len(RM),
      len(RM) == 2048 and min(pc(w) for w in RM if w) == 4
      and len(PUNC) == 2048 and PUNC == sH and SHORT == sD, kill="K5")
ok_flat16 = all((m16(cs) in RM) and ((m16(cs) & 1) == (1 if 0 in cs
                                                       else 0))
                for U, cs in FLATS)
check("S6.2 VACUUM BIT = PARITY BIT: c -> (p.c, c) is a bijection "
      "H -> RM(2,4) (set equality); on the 140 flat words the "
      "restored coordinate == s_vac (origin membership) exactly",
      REST == RM and ok_flat16, kill="K5")

# ======================================================================
section("C: controls (must fire)")
# ======================================================================
refs_dot = refinements_of(DOT)
w_pair = (DOT[1][2], DOT[1][3])         # e1.e2 vs e1.(e1+e2)
check("C1 FIRES: dot form: %d == 0 refinements (2^16 census) AND the "
      "direction bit is ill-defined on U = <e1,e2> (pair values %s "
      "differ) -- no Arf grading, no table"
      % (len(refs_dot), str(w_pair)),
      len(refs_dot) == 0 and w_pair == (0, 1), kill="K6")

Q0 = ARF0[0]                            # frozen: first Arf-0 refinement
TEN0M = wmask({x for x in NZ if Q0[x] == 1})
same_table = all((pc(w & TEN0M) & 1) == (pc(w & TENM) & 1)
                 for w in ({wmask(cs - {0}) if 0 in cs else wmask(cs)
                            for U, cs in FLATS}))
z0 = [v for v in PTS if Q0[v] == 0]
meets = sorted(sum(1 for x in U - {0} if x in z0 and x != 0)
               for U in ISO)
check("C2 FIRES (label level; frozen prediction): Arf-0 q0 leaves the "
      "syndrome TABLE invariant (canonicity lemma: %s) but the "
      "labeling breaks: |{q0=0}| = %d != 6, zero set NOT an ovoid "
      "(doily meets %s != all-1), pencil vector weight %d != 10"
      % (same_table, len(z0), meets[:5] + ["..."], pc(TEN0M)),
      same_table and len(z0) == 10 and meets != [1] * 15
      and pc(TEN0M) == 6 and pc(TENM) == 10, kill="K6")

_LCG = [20260807]


def lcg():
    _LCG[0] = (6364136223846793005 * _LCG[0]
               + 1442695040888963407) % (1 << 64)
    return _LCG[0]


perm = list(range(15))
for i in range(14, 0, -1):
    j = lcg() % (i + 1)
    perm[i], perm[j] = perm[j], perm[i]


def apply_perm(m):
    out = 0
    for i in range(15):
        if (m >> i) & 1:
            out |= 1 << perm[i]
    return out


HP = {apply_perm(m) for m in H}
weHP = Counter(pc(m) for m in HP)
w3P = {m for m in HP if pc(m) == 3}
nonlines = sum(1 for m in w3P if m not in LINES3)
check("C3 FIRES: frozen-LCG column permutation: parameters PRESERVED "
      "(same enumerator, [15,11,3]) but H^pi != H and %d/35 weight-3 "
      "supports are NOT lines (labeling broken)" % nonlines,
      weHP == weH and len(HP) == 2048 and HP != sH
      and nonlines > 0, kill="K6")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
if not controls_ok:
    VERDICT = "CONTROL-DEAD"
elif KILLS:
    VERDICT = {"K1": "ARF-BIT-BROKEN", "K2": "SYNDROME-CENSUS-BROKEN",
               "K3": "HECKE-COUNT-MISMATCH", "K4": "CODE-PENCIL-BROKEN",
               "K5": "PUNCTURE-BROKEN"}.get(KILLS[0], "CONTROL-DEAD")
else:
    VERDICT = "ARF-VACUUM-SYNDROME-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
print("  * v820 S4.2 (G3) plane-count Hecke match (A_3, B_3) = "
      "(12, 16): now a LOCAL")
print("    theorem, uniform at every point, with the isotropic count "
      "= the point")
print("    census of x^perp/<x>; v535/v785 a_3 = -4 and 32 = 28 + 4 "
      "echoed exactly.")
print("  * v821 S2 counting lemmas (35/7/28 through a point) and "
      "v834's 45/60 orbit")
print("    split: both are rows of ONE two-bit syndrome table "
      "(s_vac, s_Arf) on the")
print("    Hamming code -- the Arf bit is position-independent "
      "(the theorem), the")
print("    vacuum bit is the parity bit that restores RM(2,4).")
print("  * v819 S4's [15,10,4] enumerator = the D member of the "
      "pencil; NEW: the")
print("    canonicity lemma (all 16 refinements induce ONE Arf "
      "functional on H,")
print("    because refinements differ by simplex = H^perp words) and "
      "the pencil")
print("    normal form H > {D, C_iso, C_non} > K = "
      "[15,11,3] > 3x[15,10,-] > [15,9,4].")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT == "ARF-VACUUM-SYNDROME-EXACT") else 1)
'''

_SRC_OVOID = r'''
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
    canonical import name (cross-probe READ-ONLY imports resolve to
    the embedded copies); capture and re-emit stdout; return
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
    ("affine_arf_vacuum_probe", _SRC_ARF, 24, (),
     "ARF-VACUUM-SYNDROME-EXACT", 0),
    ("doily_ovoid_decoder_probe", _SRC_OVOID, 23, (),
     "OVOID-DECODER-EXACT", 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v852 -- ARF.VACUUM.SYNDROME.01 + OVOID.DECODER.01")
    print("(the two-bit syndrome table (s_vac, s_Arf) on the Hamming "
          "code: 15/20/45/60;")
    print("the local Hecke theorem 12/16 -> 28/-4 at all 15 points; "
          "the code pencil")
    print("H > {D, C_iso, C_non} > K with the vacuum bit as RM(2,4) "
          "parity bit; the")
    print("integral decoder N+ = N^T/4 - J/36 with SNF diag(1^10, 0^5) "
          "and the S6")
    print("standard representation; frozen protocols embedded byte-"
          "exact; NO RH claim)")
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
    print("v852: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print("Exact algebra throughout; the compression is a normal form "
          "plus an integral")
    print("inverse -- no marker moves, no new physical claim.")
    print("[%s] v852 VERDICT GATE: ARF-VACUUM-SYNDROME-EXACT + "
          "OVOID-DECODER-EXACT" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
