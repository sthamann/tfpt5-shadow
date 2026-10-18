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
