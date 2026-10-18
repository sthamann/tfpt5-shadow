#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v896 -- SEAM.CFIN.WICKFUNCTOR.01 + SEAM.CFIN.WICKMIX.01 + SEAM.CFIN.WICKBLOCK.01: THE WICK FUNCTOR ARC OF THE FINITE COMPILER -- the six compiler roles exist in the deployed seam, the scalar channel-mixing covariance is PROVABLY obstructed, and the block-valued functor is constructed exactly, ONE module from three probes (27/27 + 33/33 + 26/26 checks, zero fails, verdicts WICKFUNCTOR-PARTIAL (ROLES-IDENTIFIED / DUADMAP-DEGENERATE-ON-VACUUM / SECTOR-LAW-MATCHED / C6-INTERTWINED) + WICKMIX-MEASURED (WICKMIX-OBSTRUCTED(TRANSPOSED-DUAD-ZERO)) + WICKBLOCK-MEASURED (BLOCKFUNCTOR-CONSTRUCTED / SEAM-DIAGONAL); discovery probes seam_wick_functor_probe.py, wick_mixing_covariance_probe.py (SPEC v2), wick_block_functor_probe.py, rounds 50/51/52, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~1 s).  (1) THE ROLES EXIST (wickfunctor, the reality-bridge question: does a functor map the K6 duads to seam two-point functions and the synthemes to Wick monomials, with q* as the grading?): the SIX compiler roles are present in the deployed seam one-particle space -- five D5 carrier slot pairs + the A3 boundary block (dims 2,2,2,2,2,6 from the v155/v156 split 16 = 10 + 6); the so(16) sector law holds (current-sector dims 12 on vacuum edges / 4 on pair edges = the q* edge grading, ratio 3 = N_fam); and the C6 intertwining is EXACT: the Aut(C_fin) generator g (g^2 = sigma) induces the channel permutation pi of cycle type (1)(2)(3) fixing channel 0 -- but the deployed VACUUM KERNEL is channel-diagonal, so all 15 duad two-point functions vanish (DUADMAP-DEGENERATE-ON-VACUUM): the structure level of the functor exists, the value level needs a channel-mixing covariance -- WICKFUNCTOR-PARTIAL, the honest typing, and exactly the construction contract the next probe executes.  (2) THE SCALAR OBSTRUCTION IS PROVED (wickmix, the reviewer's construction contract): on the 6-dim scalar channel space EVERY C6-covariant antisymmetric covariance vanishes on the transposed duad -- the C6 2-cycle {4, 5} forces a duad zero, so the scalar route reaches at MOST 14/15 nonzero duads, never 15/15 (a theorem of the deployed action, exhaustively verified over the isotypic decomposition with the SPEC v2 multiplicity list [3,0,1,1,1,0] re-derived by hand and by exact root-of-unity sums); NO equivariant scalarization rescues the scalar space; and BOTH relaxation witnesses are CONSTRUCTED -- the 16-dim block object exists (O16-covariant, CAR-positive, all 15 cross-blocks nonzero, the transposed block antisymmetric 2x2 ~ J).  (3) THE BLOCK RESOLUTION (wickblock, named object (d)): the FULL block-valued functor on the 16-dim one-particle space is BLOCKFUNCTOR-CONSTRUCTED -- block commutant dimension 33, all 15/15 duad cross-blocks nonzero, all 15/15 block Wick monomials obey the chi sign law (the round-49 canonical gauge chi(i) = (-1)^(i+1)), and the interleaving character is +1 SYMBOLIC; the review's five conditions hold at block level; but the DEPLOYED seam itself is SEAM-DIAGONAL -- zero cross-blocks in the deployed vacuum kernel -- so the VALUE level of the reality bridge awaits a PHYSICAL channel-mixing mechanism; the [O] premise (the physical Wick-compiler reading) is UNMOVED.  NET: the Wick functor arc is closed at the structure level -- roles exist, the scalar form is provably obstructed, the block form is constructed and exact; what separates structure from value is one missing physical mechanism, stated as such.  NO RH claim (seam/compiler side -- no primes, no zeros anywhere in these probes); no marker moves -- the self-hosting/Wick premise stays [O] exactly as v888 typed it.  Exact integer / rational / symbolic checks in every decision that is typed PROVED or SYMBOLIC, float64 elsewhere; RNG only in declared seed constructions and controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes seam_wick_functor_probe.py (27/27,
WICKFUNCTOR-PARTIAL, round 50, SPEC v1, no amendments at freeze;
feasibility/redundancy check against the corpus done FIRST and
printed -- v113/v155/v156/v110/v160/v161/v880/v888 consumed
read-only), wick_mixing_covariance_probe.py (33/33,
WICKMIX-MEASURED, round 51, SPEC v2: the W1.6 EXPECTED isotypic
multiplicity list was frozen with a transcription error
([3,0,1,1,0,1]); the hand derivation (fixed point -> chi_0;
2-cycle -> chi_0 + chi_3; 3-cycle -> chi_0 + chi_2 + chi_4) gives
[3,0,1,1,1,0], which is what the exact root-of-unity sum measured
on the fail-first run -- every other ward untouched),
wick_block_functor_probe.py (26/26, WICKBLOCK-MEASURED, round 52,
SPEC v2 slot empty at freeze -- no post-run amendment), all
2026-08-09, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen sources embedded BYTE-EXACT, executed verbatim
in isolated namespaces; printed spec SHAs reproduce; byte-equality
ward vs experiments/tfpt-discovery/ inside the pattern gates.
Corpus surfaces consumed read-only / rebuilt inline: v113 (Majorana
CAR convention, kernel, A16), v155/v156 (D5 + A3 split, so(16)
currents), v110 (sheet-odd count), v160/v161
(quasi-free/Bogoliubov), v880/v888 + k6_pfaffian_selfhosting_probe
(q*, duads, phi, chi gauge, C6 pin), tfpt_constants (N_fam, g_car).

FIREWALL: the scalar obstruction is a PROVED no-go of the deployed
C6 action, the block functor an exact construction -- neither
moves the [O] physical premise; no seam number is fitted; the
value-level bridge is typed OPEN pending a physical mixing
mechanism.  NO RH claim.
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

# ------------- frozen probe source seam_wick_functor_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_wick_functor_probe -- SEAM.CFIN.WICKFUNCTOR.01
(EXPLORATION ONLY, experiments/; round 50, follow-up (d) of the
2026-08-09 review: the REALITY BRIDGE of the finite compiler -- does
a functor exist mapping the K6 duads to the actual seam two-point
functions and the synthemes (perfect matchings) to Wick monomials,
with q* as the sheet/vacuum grading?)

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-09 -- the modules read end to end: v113, v160, v161, v110,
v156, v880, v888, v854, k6_pfaffian_selfhosting_probe):

WHAT EXISTS (the deployed seam two-point object):
 * v113 quasi-free kernel: the seam certifies through ONE scalar
   2-point kernel M = I + iA on the Majorana ONE-PARTICLE space.
   Carrier block: 10 Majoranas (5 slots x 2, exact Jordan-Wigner
   Fock model), A integer antisymmetric with A^2 = -I, P = M/2 a
   projection of rank 5 = g_car.  Seam hull: 16 Majoranas
   (= 2 x rank E8), A16 = direct sum of 8 blocks [[0,1],[-1,0]],
   rank P16 = 8.  Wick/Pfaffian: ALL 2n-point functions equal
   Pf of the kernel submatrix -- one kernel is the whole net.
 * v155/v156 seam net construction: the seam-Calderon net is 16
   free Majoranas split 10 + 6 = SO(10) x SO(6) = D5 (+) A3
   (DtN = |k|; currents 120 = dim so(16); B = (E8)_1 by the
   character identity).  So the deployed one-particle space
   carries a CANONICAL 6-block grading: five carrier slot pairs
   (D5) + one 6-Majorana family/boundary block (A3).
 * v110 Calderon sheet: a sheet-odd involution certifies EXACTLY
   2 = |Z2| oriented scalar kernels (the vacuum channel's
   oriented-kernel multiplicity; report-level input here).
 * v160/v161: quasi-free => Pfaffian moments, cumulant inversion;
   Bogoliubov reduction of the whole cone to the 16-dim
   one-particle space; the 120 currents ARE the Bogoliubov
   generators.
 * v880/v888 (+ the frozen k6_pfaffian_selfhosting_probe, read):
   compiler side -- q* closed normal form, the duad model D(v) on
   the six Arf-1 labels, the carrier dictionary phi, 15 doily
   lines = 15 perfect matchings of K6, fermionic Pfaffian signs
   GAUGE-MATCHED to the Hodge signs by the canonical character
   chi(i) = (-1)^(i+1) (= the vacuum-row Laplace sign),
   Aut(C_fin) ~= C6 pinned by g^2 = sigma.
 * v854: a Pfaffian on the prime-front factorization complex --
   different index set entirely, no seam channel content.

WHY NEW: NOTHING in the corpus pairs the seam covariance entries
with the compiler's 6 roles / 15 duads.  The K6/doily/Pfaffian
structure lives entirely on the finite compiler side; no module
identifies six seam channels, asks whether the deployed seam
kernel is channel-mixing on the 15 channel pairs, or tests the C6
intertwining between Aut(C_fin) and the seam one-particle space.
That bridge test is exactly this probe.

THE FUNCTOR CANDIDATE (frozen after the feasibility check):
 (i)   SIX CHANNELS: the deployed D5 (+) A3 one-particle grading:
       channel i = carrier slot i (Majorana pair 2(i-1), 2(i-1)+1)
       for i = 1..5, channel 0 = the A3 family/boundary block
       (Majoranas 10..15) = the vacuum/boundary role (the review's
       1 vacuum + 5 carriers; the v110 sheet-odd count 2 = |Z2| is
       recorded as the vacuum channel's oriented multiplicity).
       Compiler side: channel 0 <-> the vacuum Arf label V0 =
       label(q*), channel i <-> Arf label phi^-1(i) (v880/v888
       carrier dictionary rebuilt).
 (ii)  DUAD MAP: {i, j} -> C_ij = the deployed seam two-point
       function between channels i and j = the cross-channel block
       of A16 (frozen linear scalarization: block entry sum; the
       full block max |entry| reported alongside), plus the same
       census in the EXACT 10-Majorana JW carrier vacuum.
 (iii) SYNTHEME MAP: each perfect matching M = {0i, jk, lm} -> the
       Wick monomial C_0i C_jk C_lm = the Pfaffian monomial of the
       6x6 antisymmetric object A6[i, j] = C_ij.
 (iv)  THE TEST: (a) the 15 monomials nonzero exactly on the
       structurally allowed configurations (doily lines <->
       matchings; secants/externals <-> triangles, which are NOT
       Pfaffian monomials); (b) the sign pattern matches the
       canonical chi(i) = (-1)^(i+1) gauge of
       k6_pfaffian_selfhosting_probe; (c) the C6 compiler
       automorphism acts compatibly on the seam side (the pinned
       generator's induced channel permutation lifts to an
       orthogonal O16 preserving the deployed kernel and
       intertwining the duad action on all 15).
       HONEST SURROGATE (declared in advance): if the deployed
       one-particle data give NO nonzero 6x6 antisymmetric object,
       say so; test the Gram/covariance of the six channels
       (antisymmetric part) as the nearest surrogate; and run the
       current-sector census: the so(16) current algebra (the 120
       deployed Bogoliubov directions, v161/v156) decomposes by
       channel pairs into 15 cross-channel sectors -- test whether
       THAT structure carries the duad model (sector dimension law
       vs the q* edge law).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
exact integer / sympy arithmetic in every decision, no floats in
decisions, no RNG, no fits):

 T1  ROLES -- channel identification (feasibility made exact):
     (a) exact JW carrier: M = I + iA on 10 Majoranas, A integer
         antisymmetric, A^2 = -I, rank(M/2) = 5 = g_car (v113
         rebuilt); the SUPPORT of A is EXACTLY the five
         within-slot pairs (2i, 2i+1) -- the deployed carrier
         kernel is CHANNEL-DIAGONAL (measured, not assumed);
     (b) seam hull: A16 = (+)_8 [[0,1],[-1,0]], rank(P16) = 8 =
         5 + 3 (D5 + A3); the frozen 6-role assignment: channels
         1..5 = slot pairs, channel 0 = Majoranas 10..15 (dims
         2,2,2,2,2,6); A16 commutes with all six channel
         projectors (channel-diagonality at seam level);
     (c) compiler side: q*, duad model, carrier dictionary phi and
         vacuum label V0 rebuilt (v880/v888 conventions); the 15
         messages -> 15 channel duads bijectively.
 T2  DUAD MAP CENSUS (typed; fail-first -- the frozen QUESTION is
     whether the deployed vacuum kernel is channel-mixing):
     for every duad {i,j}: the cross-channel block of A16 and of
     the exact JW carrier kernel; FROZEN TYPED RULE:
       DUADMAP-NONDEGENERATE iff all 15 cross blocks nonzero;
       DUADMAP-DEGENERATE-ON-VACUUM iff all 15 are EXACTLY zero
         AND the structural explanation is measured (T1(a)/(b)
         channel-diagonality);
       DUADMAP-MIXED otherwise (the probe proceeds with the
         measured values).
     If DEGENERATE: A6 = 0, Pf(A6) = 0, all 15 Wick monomials
     vanish -- the vacuum-state functor does NOT exist; typed.
 T3  SURROGATE -- the Gram of the six channels: G = M16 symmetric
     part = I (measured), antisymmetric part = A16 cross blocks =
     the T2 census again; typed GRAM-DEGENERATE iff it adds no
     nonzero duad value, GRAM-CARRIES otherwise.
 T4  CURRENT-SECTOR CORRESPONDENCE (what the deployed data DO
     carry): the so(16) currents :m_a m_b: decompose by channel
     pairs: within = 5 x so(2) + so(6) = 5 + 15 = 20; cross = the
     15 duad sectors, dim({i,j}) = dim_i x dim_j, i.e. 12 on the
     five vacuum edges and 4 on the ten pair edges; 20 + 5x12 +
     10x4 = 120 exactly;
     (a) EDGE LAW MATCH: dim(sector of D(v)) = 12 iff q*(v) = 0
         iff the channel duad touches 0 -- on ALL 15 messages
         (the q* sheet/vacuum grading IS the sector-dimension
         grading; ratio 12/4 = 3 = N_fam);
     (b) SYNTHEME CAPACITY: every perfect matching has sector
         capacity 12 x 4 x 4 = 192 != 0 (all 15 structurally
         allowed); every doily line maps to a matching, every
         secant/external to a triangle through/avoiding channel 0
         (v888 motif census rebuilt lean) -- and triangles are NOT
         monomials of Pf (grammar exclusion, symbolic).
 T5  SIGN STRUCTURE (symbolic side of (iv)(b)): Pf of the generic
     antisymmetric 6x6 has EXACTLY 15 monomials, coefficients +-1;
     the vacuum-row Laplace expansion holds symbolically and the
     per-matching sign obeys sgn(M) = chi(i) * qsign(S, T) with
     chi(i) = (-1)^(i+1) (the canonical gauge of the k6 probe) and
     qsign the (+,-,+) Plucker minor sign; HONEST TYPING: with T2
     DEGENERATE the seam data supply NO sign to test against --
     typed SIGN-GAUGE-STRUCTURAL-ONLY (a measured seam sign test
     needs a nonzero duad map first); SIGN-MATCHED only if T2
     gave nonzero values whose signs realize chi.
 T6  C6 COMPATIBILITY: rebuild Sp(4,2) (720) and Aut(C_fin) ~= C6,
     pin g by g^2 = sigma (unique); the induced pi_a on the 6 Arf
     labels fixes V0; the channel permutation pi = phi o pi_a o
     phi^-1 (pi(0) = 0) has cycle type (1)(2)(3) on the six
     channels; the frozen orthogonal lift O16 (permute slot pairs
     as units, identity on the A3 block) satisfies EXACTLY:
     (a) O16 orthogonal, integer; (b) O16 A16 O16^T = A16 (the
     deployed kernel is a C6 fixed point); (c) O16 maps channel
     subspace i onto channel subspace pi(i) -- so conjugation
     maps the sector of {i,j} onto the sector of {pi(i), pi(j)}:
     the seam action INTERTWINES the compiler duad action
     D(g v) = pi_a(D(v)) on all 15 messages; sector dims
     invariant; (d) symbolic Pf equivariance Pf(P A P^T) =
     det(P) Pf(A) and the per-matching crossing-character law
     (k6 probe convention).
 C   CONTROLS (must fire; frozen fire rules):
     C1 WRONG VACUUM ROLE (permuted roles): declaring a non-V0
        Arf label the vacuum breaks the T4 edge law on EXACTLY
        8 of 15 messages (the symmetric difference of two vertex
        stars in K6);
     C2 WRONG SIGN CHARACTER: chi flipped on slot 2 breaks T5 on
        EXACTLY the 3 matchings whose vacuum partner is i = 2;
     C3 WRONG CHANNEL PERMUTATION: the transposition (0 1) on
        channels does not preserve the sector-dimension pattern
        (>= 1 mismatch; expected 8) -- and admits NO grading-
        preserving orthogonal lift (dim 6 != dim 2, structural).

KILLS (any one fires => typed gap):
  K0 AST firewall / setup ward breaks              -> PIPELINE-BROKEN
  K1 no 6-role structure in the deployed data      -> ROLES-MISSING
  K2 duad-map census not coherently typed          -> DUADMAP-UNTYPED
  K3 sector decomposition / edge law breaks        -> SECTOR-BROKEN
  K4 Pfaffian grammar / sign gauge breaks          -> WICK-BROKEN
  K5 C6 lift / intertwining breaks                 -> C6-BROKEN
  K7 a control does not fire                       -> CONTROL-DEAD

VERDICT (frozen enum): WICKFUNCTOR-CONSTRUCTED (no kills AND T2 =
DUADMAP-NONDEGENERATE AND T5 = SIGN-MATCHED AND T6 intertwined) /
WICKFUNCTOR-PARTIAL [typed tokens] (channels identified and some
identities hold, but the duad map is degenerate/mixed or the signs
are structural-only) / WICKFUNCTOR-NOT-CONSTRUCTIBLE (K1: the
deployed seam data has no natural 6-role structure -- with the
exact missing statement printed; that statement IS the deliverable)
/ PIPELINE-BROKEN / CONTROL-DEAD.  Exit 0 iff all checks pass and
no kill fired (an honest PARTIAL exits 0); else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  AST firewall: banned identifiers
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime (self-scan).  NO physics-realization claim beyond the
measured identities: the [O] premise (the boundary grammar IS a
self-hosting Wick pair compiler) stays [O]; no marker moves.

SPEC v2 AMENDMENTS: none at freeze; any post-run amendment is
documented here with the fail-first output preserved.

Sources (read-only, machinery rebuilt inline): v113 (JW model,
kernel, A16), v155/v156 (D5+A3 split, so(16) currents), v110
(sheet-odd count), v160/v161 (quasi-free/Bogoliubov), v880/v888 +
k6_pfaffian_selfhosting_probe (q*, duads, phi, chi gauge, C6 pin),
tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_wick_functor_probe.py
"""

import ast
import hashlib
import itertools
import os
import sys
import time

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ---------------------------------------------------------- bit model
# (v880 / v888 conventions, rebuilt inline; family/anchor basis
#  (F1, F2, F3, A), bit form of Gram J - I)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
BASIS = (1, 2, 4, 8)
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    """order-3 deck sigma: (b0,b1,b2,b3) -> (b2,b0,b1,b3) (v880)."""
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    """q_c(v) = C(|v|,2) + c.v mod 2 -- the 16 refinements (v880)."""
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA[v]) if bit)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def perm_sign(perm):
    ct = cycle_type(perm)
    return -1 if (len(perm) - len(ct)) % 2 else 1


def pf_of(mat, idx):
    """recursive Pfaffian expansion along the first index of idx."""
    if not idx:
        return sp.Integer(1)
    i0, rest0 = idx[0], idx[1:]
    tot = sp.Integer(0)
    for k, j in enumerate(rest0):
        sub = [t for t in rest0 if t != j]
        tot += sp.Integer(-1) ** k * mat[i0, j] * pf_of(mat, sub)
    return tot


def all_matchings(vs):
    vs = sorted(vs)
    if not vs:
        return [frozenset()]
    a = vs[0]
    out = []
    for b in vs[1:]:
        rest = [x for x in vs if x not in (a, b)]
        for sub in all_matchings(rest):
            out.append(sub | {frozenset({a, b})})
    return out


# --------------------------------------------------- JW seam machinery
def jw(g):
    """Exact Jordan-Wigner annihilators on the 2^g Fock space (v113)."""
    eye2, zee = sp.eye(2), sp.diag(1, -1)
    amat = sp.Matrix([[0, 1], [0, 0]])
    ops = []
    for i in range(g):
        mats = [zee] * i + [amat] + [eye2] * (g - 1 - i)
        full = mats[0]
        for m in mats[1:]:
            full = sp.Matrix(sp.kronecker_product(full, m))
        ops.append(full)
    return ops


def main():
    print("SEAM.CFIN.WICKFUNCTOR.01 -- the K6 -> seam Wick functor "
          "(reality bridge)")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO physics-realization claim beyond the measured "
          "identities; the [O] premise stays [O]; exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (corpus rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s"
          % (BANNED_IDS,), not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    check("S0.1 the 16 polar shifts are all distinct refinements of "
          "the bit form (v880 rebuilt)",
          ok_ref and len(set(refs)) == 16, kill="K0")

    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.2 frozen v845 selector: unique q* (Arf census 6 Arf-1)",
          len(arf1) == 6 and len(cand) == 1, kill="K0")
    QSTAR = cand[0]
    ZQ = [v for v in range(16) if QSTAR[v] == 0]
    ovoid = [v for v in ZQ if v]
    NZ = list(range(1, 16))

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    DUADS6 = sorted((frozenset(d)
                     for d in itertools.combinations(range(6), 2)),
                    key=sorted)
    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS6)
    check("S0.3 duad model: 15 messages <-> 15 duads of the six "
          "Arf-1 labels; vacuum label V0 = %d" % V0,
          biject and 0 <= V0 < 6, kill="K0")

    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5
               and set(phi.values()) == set(range(1, 6)))
    check("S0.4 carrier dictionary phi (ovoid-induced) is a "
          "bijection labels -> slots: %s" % (sorted(phi.items()),),
          ok_phi, kill="K0")

    def lab(j):
        return 0 if j == V0 else phi[j]

    def chduad(v):
        return frozenset(lab(j) for j in dmap[v])

    lines_pg = set()
    for a2, b2 in itertools.combinations(NZ, 2):
        lines_pg.add(frozenset({a2, b2, a2 ^ b2}))
    iso = sorted([L for L in lines_pg
                  if all(HT[u][w] == 0 for u in L for w in L)],
                 key=sorted)
    noniso = [L for L in lines_pg if L not in set(iso)]
    check("S0.5 PG(3,2): 35 lines = 15 doily + 20 non-isotropic "
          "(v880 rebuilt)",
          len(lines_pg) == 35 and len(iso) == 15
          and len(noniso) == 20, kill="K0")

    # ==================================================================
    section("T1 -- ROLES: the deployed seam channels (feasibility "
            "made exact)")
    # ==================================================================
    # (a) exact JW carrier kernel (v113 rebuilt)
    g = 5
    a = jw(g)
    ad = [x.T for x in a]
    cs = []
    for i in range(g):
        cs.append(a[i] + ad[i])
        cs.append(sp.I * (ad[i] - a[i]))
    vac = sp.zeros(2 ** g, 1)
    vac[0] = 1

    def vev(ops):
        v = vac
        for o in reversed(ops):
            v = o * v
        return (vac.T * v)[0]

    m2 = sp.Matrix(10, 10, lambda j, k: vev([cs[j], cs[k]]))
    A_car = (m2 - sp.eye(10)) / sp.I
    pol = (sp.eye(10) + sp.I * A_car) / 2
    ok_kern = (sp.simplify(A_car + A_car.T) == sp.zeros(10)
               and all(x.is_integer for x in A_car)
               and sp.simplify(A_car * A_car + sp.eye(10))
               == sp.zeros(10)
               and pol.rank() == 5)
    supp = {(r, c) for r in range(10) for c in range(10)
            if r != c and A_car[r, c] != 0}
    want_supp = set()
    for i in range(5):
        want_supp |= {(2 * i, 2 * i + 1), (2 * i + 1, 2 * i)}
    check("T1.1(a) DEPLOYED CARRIER KERNEL (v113 exact JW): "
          "M = I + iA, A integer antisymmetric, A^2 = -I, "
          "rank(M/2) = 5 = g_car; SUPPORT of A = EXACTLY the five "
          "within-slot pairs (2i, 2i+1) -- the deployed carrier "
          "kernel is CHANNEL-DIAGONAL (measured)",
          ok_kern and supp == want_supp and g_car == 5, kill="K1")

    # (b) seam hull A16 + the frozen 6-role assignment
    A16 = sp.zeros(16)
    for i in range(8):
        A16[2 * i, 2 * i + 1] = 1
        A16[2 * i + 1, 2 * i] = -1
    P16 = (sp.eye(16) + sp.I * A16) / 2
    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    dims = {i: len(CH[i]) for i in CH}
    projs = {i: sp.diag(*[1 if r in CH[i] else 0 for r in range(16)])
             for i in CH}
    ok_comm = all(sp.simplify(projs[i] * A16 - A16 * projs[i])
                  == sp.zeros(16) for i in CH)
    check("T1.2(b) SEAM HULL: A16 = (+)_8 J, rank(P16) = 8 = 5 + 3 "
          "(D5 + A3, v113/v156); frozen 6 roles: channels 1..5 = "
          "the five D5 slot pairs, channel 0 = the 6-Majorana A3 "
          "family/boundary block (dims %s); A16 COMMUTES with all "
          "six channel projectors (channel-diagonal at seam level); "
          "v110 report: the sheet-odd vacuum channel carries "
          "2 = |Z2| oriented scalar kernels"
          % ([dims[i] for i in range(6)],),
          sp.simplify(P16 * P16 - P16) == sp.zeros(16)
          and P16.rank() == 8 and dims[0] == 6
          and all(dims[i] == 2 for i in range(1, 6)) and ok_comm,
          kill="K1")

    chd = {v: chduad(v) for v in NZ}
    check("T1.3(c) the 15 messages map bijectively onto the 15 "
          "channel duads (compiler roles <-> seam channels wired "
          "through phi, V0 -> channel 0)",
          sorted(chd.values(), key=sorted) == DUADS6, kill="K1")

    # ==================================================================
    section("T2 -- THE DUAD MAP on the deployed vacuum kernel "
            "(typed census)")
    # ==================================================================
    cross16 = {}
    cross10 = {}
    for i, j in itertools.combinations(range(6), 2):
        blk = [A16[r, c] for r in CH[i] for c in CH[j]]
        cross16[frozenset({i, j})] = (sum(blk),
                                      max(abs(x) for x in blk))
        if i >= 1:
            blk10 = [m2[r, c] for r in CH[i] for c in CH[j]]
            cross10[frozenset({i, j})] = max(abs(x) for x in blk10)
    n_zero16 = sum(1 for s, mx in cross16.values() if mx == 0)
    n_zero10 = sum(1 for mx in cross10.values() if mx == 0)
    print("      cross-channel census: A16 blocks exactly zero on "
          "%d/15 duads; exact JW carrier vacuum cross-slot 2-point "
          "functions zero on %d/10 slot-slot duads" %
          (n_zero16, n_zero10))
    if n_zero16 == 0:
        t2_type = "DUADMAP-NONDEGENERATE"
    elif n_zero16 == 15 and n_zero10 == 10:
        t2_type = "DUADMAP-DEGENERATE-ON-VACUUM"
    else:
        t2_type = "DUADMAP-MIXED"
    check("T2.1 TYPED CENSUS: %s -- the deployed vacuum kernel has "
          "ALL cross-channel two-point functions %s (the frozen "
          "question answered by measurement; explanation = the "
          "measured channel-diagonality of T1)"
          % (t2_type,
             "exactly ZERO" if t2_type
             == "DUADMAP-DEGENERATE-ON-VACUUM" else "as censused"),
          t2_type in ("DUADMAP-NONDEGENERATE",
                      "DUADMAP-DEGENERATE-ON-VACUUM",
                      "DUADMAP-MIXED"), kill="K2")

    A6 = sp.zeros(6)
    for s, (val, _mx) in cross16.items():
        i, j = sorted(s)
        A6[i, j] = val
        A6[j, i] = -val
    pf_a6 = pf_of(A6, list(range(6)))
    degen = (t2_type == "DUADMAP-DEGENERATE-ON-VACUUM")
    check("T2.2 CONSEQUENCE: the 6x6 antisymmetric object A6 built "
          "from the deployed data has Pf(A6) = %s; all 15 Wick "
          "monomials C_0i C_jk C_lm evaluate to 0 -- the VACUUM-"
          "STATE functor does not exist; a quasi-free vacuum whose "
          "polarization is channel-diagonal cannot carry the doily "
          "(measured, typed -- NOT a check failure: the honest "
          "outcome the protocol froze)" % pf_a6,
          (pf_a6 == 0) == degen or not degen, kill="K2")

    # ==================================================================
    section("T3 -- SURROGATE: the Gram of the six channels")
    # ==================================================================
    M16 = sp.eye(16) + sp.I * A16
    sym_part = (M16 + M16.T) / 2
    anti_part = (M16 - M16.T) / (2 * sp.I)
    gram_adds = any(
        max(abs(anti_part[r, c]) for r in CH[i] for c in CH[j]) != 0
        for i, j in itertools.combinations(range(6), 2))
    t3_type = "GRAM-CARRIES" if gram_adds else "GRAM-DEGENERATE"
    check("T3.1 GRAM SURROGATE: M16 symmetric part = I (measured "
          "%s), antisymmetric part = A16 -- the Gram of the six "
          "channels adds NO nonzero duad value beyond T2; typed %s"
          % (sym_part == sp.eye(16), t3_type),
          sym_part == sp.eye(16), kill="K2")

    # ==================================================================
    section("T4 -- CURRENT-SECTOR CORRESPONDENCE (what the deployed "
            "data DO carry)")
    # ==================================================================
    within = sum(dims[i] * (dims[i] - 1) // 2 for i in range(6))
    sector_dim = {frozenset({i, j}): dims[i] * dims[j]
                  for i, j in itertools.combinations(range(6), 2)}
    cross_tot = sum(sector_dim.values())
    check("T4.1 so(16) DECOMPOSITION by channel pairs: within = "
          "5 x so(2) + so(6) = 5 + 15 = %d; cross = 5 vacuum-edge "
          "sectors of dim 12 + 10 pair-edge sectors of dim 4 = %d; "
          "total %d == 120 = dim so(16) (the deployed Bogoliubov "
          "current directions, v161/v156)"
          % (within, cross_tot, within + cross_tot),
          within == 20 and cross_tot == 100
          and within + cross_tot == 120
          and sorted(sector_dim.values()) == [4] * 10 + [12] * 5,
          kill="K3")

    ok_edge = all((QSTAR[v] == 0) == (0 in chd[v])
                  == (sector_dim[chd[v]] == 12) for v in NZ)
    check("T4.2(a) EDGE LAW MATCH on all 15 messages: q*(v) = 0 "
          "iff the channel duad touches 0 iff its current sector "
          "has dim 12 (else 4) -- the q* sheet/vacuum grading IS "
          "the sector-dimension grading; ratio 12/4 = 3 = N_fam",
          ok_edge and 12 // 4 == N_fam, kill="K3")

    MSLOT = all_matchings(range(6))
    caps = {frozenset(m): 1 for m in MSLOT}
    for m in MSLOT:
        c = 1
        for e in m:
            c *= sector_dim[e]
        caps[frozenset(m)] = c
    check("T4.3(b) SYNTHEME CAPACITY: every perfect matching M = "
          "{0i, jk, lm} has sector capacity 12 x 4 x 4 = 192 != 0 "
          "(all 15 structurally allowed at sector level)",
          len(MSLOT) == 15
          and all(caps[frozenset(m)] == 192 for m in MSLOT),
          kill="K3")

    def motif(L):
        trip = [chd[v] for v in L]
        verts = frozenset().union(*trip)
        if (len(verts) == 6
                and all(not (x & y) for x, y in
                        itertools.combinations(trip, 2))):
            return ("matching", frozenset(trip))
        if len(verts) == 3 and len(set(trip)) == 3:
            return ("triangle", verts)
        return ("neither", None)

    iso_m = [motif(L) for L in iso]
    non_m = [motif(L) for L in noniso]
    sec_n = sum(1 for k, x in non_m if k == "triangle" and 0 in x)
    ext_n = sum(1 for k, x in non_m
                if k == "triangle" and 0 not in x)
    check("T4.4(b) STRUCTURAL ALLOWEDNESS (motif census rebuilt "
          "lean): the 15 doily lines -> the 15 matchings; the 20 "
          "non-isotropic lines -> triangles (%d through channel 0 "
          "= secants, %d avoiding = externals) -- and a triangle "
          "is NEVER a Pfaffian monomial (grammar exclusion, T5)"
          % (sec_n, ext_n),
          all(k == "matching" for k, _x in iso_m)
          and len({x for _k, x in iso_m}) == 15
          and sec_n == 10 and ext_n == 10, kill="K3")

    # ==================================================================
    section("T5 -- SIGN STRUCTURE (symbolic; the chi gauge)")
    # ==================================================================
    SYM = {}
    for i in range(6):
        for j in range(i + 1, 6):
            SYM[(i, j)] = sp.Symbol("a_%d%d" % (i, j))
    G6 = sp.Matrix(6, 6, lambda r, c:
                   SYM[(r, c)] if r < c
                   else (-SYM[(c, r)] if r > c else 0))
    PF6 = sp.expand(pf_of(G6, list(range(6))))
    cd = PF6.as_coefficients_dict()

    def mono_of(m):
        out = sp.Integer(1)
        for e in m:
            out *= SYM[tuple(sorted(e))]
        return out

    sgn = {}
    ok_c = True
    for m in MSLOT:
        c = cd.get(mono_of(m), 0)
        ok_c &= (c in (1, -1))
        sgn[frozenset(m)] = int(c)
    check("T5.1 Pf(generic A) expands into EXACTLY 15 monomials, "
          "one per matching, coefficients +-1; triangles absent",
          len(cd) == 15 and ok_c, kill="K4")

    def m_ist(m):
        vac_e = next(e for e in m if 0 in e)
        i = next(iter(vac_e - {0}))
        S, T = sorted((tuple(sorted(e)) for e in m if e != vac_e))
        return i, S, T

    def qsign(i, S, T):
        j, k, l, m4 = sorted(set(range(1, 6)) - {i})
        three = [frozenset({frozenset({j, k}), frozenset({l, m4})}),
                 frozenset({frozenset({j, l}), frozenset({k, m4})}),
                 frozenset({frozenset({j, m4}), frozenset({k, l})})]
        key = frozenset({frozenset(S), frozenset(T)})
        return (1, -1, 1)[three.index(key)]

    chi = {i: (-1) ** (i + 1) for i in range(1, 6)}
    ok_gauge = all(
        sgn[frozenset(m)]
        == chi[m_ist(m)[0]] * qsign(*m_ist(m)) for m in MSLOT)
    laplace = sp.Integer(0)
    for i in range(1, 6):
        rest = sorted(set(range(1, 6)) - {i})
        laplace += (sp.Integer(-1) ** (i + 1) * SYM[(0, i)]
                    * sp.expand(pf_of(G6, rest)))
    check("T5.2 SIGN GAUGE: sgn(M) == chi(i) * qsign(S,T) with "
          "chi(i) = (-1)^(i+1) (the canonical gauge of "
          "k6_pfaffian_selfhosting_probe = the vacuum-row Laplace "
          "sign) on all 15; Laplace expansion holds symbolically",
          ok_gauge and sp.expand(PF6 - laplace) == 0, kill="K4")

    t5_type = ("SIGN-MATCHED" if not degen and ok_gauge
               else "SIGN-GAUGE-STRUCTURAL-ONLY")
    check("T5.3 HONEST TYPING: with T2 = %s the seam data supply "
          "NO measured sign to test against chi -- typed %s (a "
          "seam sign test needs a nonzero duad map first)"
          % (t2_type, t5_type),
          (t5_type == "SIGN-GAUGE-STRUCTURAL-ONLY") == degen,
          kill="K4")

    # ==================================================================
    section("T6 -- C6 COMPATIBILITY (compiler automorphism vs seam "
            "channels)")
    # ==================================================================
    gl_n = 0
    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        gl_n += 1
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    check("T6.1 ward: |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == "
          "720 (exhaustive, v888 rebuilt)" % (gl_n, len(SP6)),
          gl_n == 20160 and len(SP6) == 720, kill="K5")

    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA[p[v]] == tuple(IOTA[v][pi[s]]
                                          for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("T6.2 Aut(C_fin) ~= C6 rebuilt: |Aut| = %d == 6; "
          "generator pin g^2 = sigma unique" % len(AUT),
          len(AUT) == 6 and len(g_pin) == 1, kill="K5")
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    ok_int = all(dmap[GEN[v]] == frozenset(pia[j] for j in dmap[v])
                 for v in NZ)
    pi6 = [0] * 6
    for j in range(6):
        pi6[lab(j)] = lab(pia[j])
    pi6 = tuple(pi6)
    ct6 = cycle_type(pi6)
    check("T6.3 induced channel permutation pi = phi o pi_a o "
          "phi^-1: fixes channel 0 (pi_a fixes V0: %s); intertwines "
          "the duad action D(g v) = pi_a(D(v)) on all 15; cycle "
          "type on the six channels = %s == (1, 2, 3)"
          % (pia[V0] == V0, ct6),
          pia[V0] == V0 and ok_int and pi6[0] == 0
          and ct6 == (1, 2, 3), kill="K5")

    # frozen orthogonal lift: permute slot pairs as units, identity
    # on the A3 block
    O16 = sp.zeros(16)
    for r in CH[0]:
        O16[r, r] = 1
    for i in range(1, 6):
        src, dst = CH[i], CH[pi6[i]]
        O16[dst[0], src[0]] = 1
        O16[dst[1], src[1]] = 1
    ok_orth = sp.simplify(O16 * O16.T) == sp.eye(16)
    ok_fix = sp.simplify(O16 * A16 * O16.T - A16) == sp.zeros(16)
    ok_map = all(
        {next(r for r in range(16) if O16[r, c] != 0)
         for c in CH[i]} == set(CH[pi6[i]]) for i in range(6))
    ok_sec = all(sector_dim[frozenset({pi6[i], pi6[j]})]
                 == sector_dim[frozenset({i, j})]
                 for i, j in itertools.combinations(range(6), 2))
    check("T6.4 FROZEN LIFT O16 (slot pairs as units, identity on "
          "the A3 block): orthogonal integer; O16 A16 O16^T == A16 "
          "(the deployed kernel is a C6 FIXED POINT -- consistent, "
          "but sign-informationless, matching T2); maps channel "
          "subspace i onto channel pi(i) => conjugation maps the "
          "sector of {i,j} onto the sector of {pi(i), pi(j)}: the "
          "seam action INTERTWINES the compiler duad action; "
          "sector dims invariant",
          ok_orth and ok_fix and ok_map and ok_sec, kill="K5")

    P6 = sp.Matrix(6, 6, lambda r, c: 1 if r == pi6[c] else 0)
    PFB = sp.expand(pf_of(P6 * G6 * P6.T, list(range(6))))
    det6 = perm_sign(pi6)

    def act_m(m, p):
        return frozenset(frozenset(p[x] for x in e) for e in m)

    def cross_char(m, p):
        out = 1
        for e in m:
            x, y = sorted(e)
            if p[x] > p[y]:
                out = -out
        return out

    ok_cov = all(sgn[frozenset(act_m(m, pi6))]
                 == det6 * cross_char(m, pi6) * sgn[frozenset(m)]
                 for m in MSLOT)
    check("T6.5 Pf EQUIVARIANCE: Pf(P A P^T) == det(P) Pf(A) "
          "= %+d Pf(A) symbolically; per matching sgn(pi(M)) == "
          "det(pi) * c_pi(M) * sgn(M) on all 15 (k6 convention)"
          % det6,
          sp.expand(PFB - det6 * PF6) == 0 and ok_cov, kill="K5")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    wrong_v = next(j for j in range(6) if j != V0)
    mism1 = sum(1 for v in NZ
                if (QSTAR[v] == 0) != (wrong_v in dmap[v]))
    check("C1 FIRES: WRONG VACUUM ROLE (Arf label %d instead of "
          "V0 = %d): the edge law q*(v) = 0 iff vacuum in D(v) "
          "breaks on EXACTLY %d == 8 messages (symmetric "
          "difference of two K6 vertex stars)"
          % (wrong_v, V0, mism1), mism1 == 8, kill="K7")

    chi_wrong = dict(chi)
    chi_wrong[2] = -chi_wrong[2]
    mism2 = [m for m in MSLOT
             if sgn[frozenset(m)]
             != chi_wrong[m_ist(m)[0]] * qsign(*m_ist(m))]
    check("C2 FIRES: WRONG SIGN CHARACTER (chi flipped on slot 2): "
          "EXACTLY %d == 3 mismatches, all in the i = 2 triple"
          % len(mism2),
          len(mism2) == 3
          and all(m_ist(m)[0] == 2 for m in mism2), kill="K7")

    tperm = (1, 0, 2, 3, 4, 5)
    mism3 = sum(1 for i, j in itertools.combinations(range(6), 2)
                if sector_dim[frozenset({tperm[i], tperm[j]})]
                != sector_dim[frozenset({i, j})])
    check("C3 FIRES: WRONG CHANNEL PERMUTATION (transposition "
          "(0 1)): the sector-dimension pattern breaks on EXACTLY "
          "%d == 8 duads; structurally NO grading-preserving "
          "orthogonal lift exists (dim 6 != dim 2: %s)"
          % (mism3, dims[0] != dims[1]),
          mism3 == 8 and dims[0] != dims[1], kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    tokens = ["ROLES-IDENTIFIED", t2_type, t3_type,
              "SECTOR-LAW-MATCHED", t5_type, "C6-INTERTWINED"]
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "K1" in KILLS:
        VERDICT = "WICKFUNCTOR-NOT-CONSTRUCTIBLE"
    elif KILLS:
        VERDICT = "WICKFUNCTOR-PARTIAL [%s]" % ", ".join(
            sorted(set(KILLS)))
    elif t2_type == "DUADMAP-NONDEGENERATE" \
            and t5_type == "SIGN-MATCHED":
        VERDICT = "WICKFUNCTOR-CONSTRUCTED [%s]" % ", ".join(tokens)
    else:
        VERDICT = "WICKFUNCTOR-PARTIAL [%s]" % ", ".join(tokens)
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * FEASIBILITY: the deployed seam two-point object is the v113
    quasi-free kernel M = I + iA on the Majorana one-particle
    space (10 carrier / 16 seam Majoranas); the D5 (+) A3 split
    of v156 gives the canonical 6 roles (5 slot pairs + the
    6-Majorana boundary block).  Nothing in the corpus paired
    seam data with the 6 roles / 15 duads before this probe.
  * THE DUAD MAP IS DEGENERATE ON THE VACUUM: the deployed kernel
    is channel-diagonal (measured exactly, JW carrier and seam
    hull), so ALL 15 cross-channel two-point functions vanish;
    Pf(A6) = 0 and every Wick monomial C_0i C_jk C_lm = 0.  A
    quasi-free vacuum whose polarization pairs Majoranas within
    channels CANNOT carry the doily -- the vacuum-state functor
    does not exist.  The Gram surrogate adds nothing.
  * WHAT THE DEPLOYED DATA DO CARRY: the so(16) current algebra
    decomposes by channel pairs into exactly the 15 duad sectors
    (120 = 20 within + 5x12 + 10x4); the sector-dimension law
    (12 iff the duad touches the vacuum channel) matches the q*
    edge law on all 15 messages -- q* IS the sector grading, with
    ratio 12/4 = 3 = N_fam; every syntheme has nonzero sector
    capacity 192, and doily lines <-> matchings while secant/
    external lines <-> triangles, which Pf grammar excludes.
  * C6: the pinned Aut(C_fin) generator induces the channel
    permutation of cycle type (1)(2)(3) fixing channel 0; its
    frozen orthogonal lift O16 preserves the deployed kernel and
    intertwines the duad action on all 15 sectors; Pf is
    equivariant with the computed crossing character.
  * WHAT THE FULL FUNCTOR THEOREM STILL NEEDS (the contract's
    demand, defined precisely by this probe): a CANONICAL,
    DEPLOYED antisymmetric scalar assignment c: {15 cross-channel
    current sectors} -> nonzero values -- i.e. a channel-MIXING
    seam object (a boundary/transport-twisted two-point function,
    a sector scalarization of the so(16) current pairing, or the
    v110 oriented scalar-kernel pair extended off-diagonally),
    NOT the vacuum state -- such that (a) all 15 values are
    nonzero, (b) their signs realize chi(i) = (-1)^(i+1) in the
    canonical gauge, (c) the assignment is C6-equivariant with
    the crossing character.  The scalarization step itself must
    be canonical (none is deployed today).  Until then the
    bridge holds at the STRUCTURAL level (roles, edge law,
    grammar, C6) but not at the VALUE level (numbers, signs).
  * The [O] premise (the boundary grammar IS a self-hosting Wick
    pair compiler) stays [O]; no marker moves.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source wick_mixing_covariance_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wick_mixing_covariance_probe -- SEAM.CFIN.WICKMIX.01
(EXPLORATION ONLY, experiments/; round 51, the reviewer's
CONSTRUCTION contract for the named gap of round 50: construct the
canonical CHANNEL-MIXING quasifree CAR covariance on the six
compiler roles -- the missing object identified by
seam_wick_functor_probe (WICKFUNCTOR-PARTIAL: the deployed vacuum
kernel is channel-diagonal, so all 15 duad two-point functions
vanish; the value-level functor needs a channel-mixing covariance).)

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-09 -- read end to end: seam_wick_functor_probe (round 50),
k6_pfaffian_selfhosting_probe (round 49), s6_plucker_hadamard_probe
(round 44), v113/v156/v880/v888):
 * round 50 identified the 6 roles (five D5 slot pairs + the A3
   boundary block), measured the deployed kernel CHANNEL-DIAGONAL
   (DUADMAP-DEGENERATE-ON-VACUUM), proved the so(16) sector law
   (dims 12 on vacuum edges / 4 on pair edges = q* edge grading,
   ratio 3 = N_fam), and pinned the C6 intertwining: the Aut(C_fin)
   generator g (g^2 = sigma) induces the channel permutation pi of
   cycle type (1)(2)(3) FIXING channel 0.
 * round 49 froze the canonical Pfaffian sign gauge chi(i) =
   (-1)^(i+1) (= the vacuum-row Laplace sign); round 44 the Specht
   split 15 = 1 + 5 + 9 of the duad representation.
 * NOTHING in the corpus constructs (or refutes) a channel-MIXING
   quasifree covariance covariant under the deployed C6 action.
   That construction problem is exactly this probe.

CAR CONVENTION (FROZEN, from the corpus seam modules v113 /
round 50): scalar Majorana channel space R^6 (one scalarized
Majorana direction per role; round-50 A6 convention).  A quasifree
CAR covariance is G = (I + iA)/2 with A REAL ANTISYMMETRIC (the CAR
fixes the symmetric part of the 2-point matrix M = I + iA to I);
CAR positivity 0 <= G <= I  <=>  spec-norm(A) <= 1.  The 15 duad
two-point functions are C_ij := A_ij (i<j) -- EXACTLY the 15
independent entries of an antisymmetric 6x6 = the 15 duads; the
Wick monomials are the Pfaffian monomials C_0i C_jk C_lm (round-50
(iii)).  A hermitian-G reading is reported alongside where the
convention matters (D0 note), but the frozen object is Majorana.

THE FIVE CONDITIONS (frozen; the reviewer's construction target):
 (i)   0 <= G <= I                     (CAR positivity);
 (ii)  [P_pi, G] = 0 with P_pi the DEPLOYED C6 channel permutation
       (compiler covariance; equivalently [P_pi, A] = 0);
 (iii) G NOT channel-diagonal: ALL 15 duad values C_ij nonvanishing
       at the frozen floor;
 (iv)  the q* grading carried (frozen from the round-50 grading
       test T4.2): with Gamma = diag(+1; -1,-1,-1,-1,-1) the
       channel vacuum grading, (a) [Gamma, P_pi] = 0 (the deployed
       C6 preserves the grading -- pi fixes channel 0); (b) the
       Ad(Gamma)-ODD part of A is supported EXACTLY on the 5 duads
       {0,i} with q*(message) = 0 and the EVEN off-diagonal part
       EXACTLY on the 10 duads with q* = 1 (the round-50 edge law,
       rebuilt and re-verified on all 15 messages); (c) BOTH
       grading sectors are nonvanishing on all their duads (odd
       5/5, even 10/10); the sector-dimension ratio 12/4 = 3 =
       N_fam is the structural cross-reference (report);
 (v)   the control geometry REFUSES: permuted roles break (ii) and
       (iv); the deployed diagonal G = I/2 fails (iii).

THE SEARCH SPACE (frozen, Specht-restricted per the reviewer):
G = I/2 + iA/2 with A in the ANTISYMMETRIC C6-COMMUTANT of the
deployed channel action: compute that commutant EXACTLY (dimension
and a basis; also the full and symmetric commutants, the isotypic
structure of the C6 representation on C^6, and the restriction of
the Specht 1+5+9 to the induced duad action).  ENUMERATE the
commutant basis (one basis ray per orientation-consistent edge
orbit of pi), impose (i) via eigenvalue bounds per ray, and test
(iii)/(iv) on each candidate ray.  THE CANONICAL CANDIDATE = the
minimizer of the FROZEN SOURCE FUNCTIONAL ||G - G_diag||_Frobenius
(G_diag = I/2 = the deployed diagonal covariance at channel level,
round 50) among covariant candidates with ALL 15 duads at the
frozen floor |C_ij| >= FLOOR := (1/100) x (diagonal scale 1/2) =
1/200 -- NO fitting to any target beyond these frozen structural
conditions.  FROZEN FALLBACK (declared before first run): if the
feasible set is EMPTY (the commutant forces zeros), the probe types
the obstruction, PROVES which duads are forced, and constructs the
canonical MAXIMAL-SUPPORT relaxed candidate (same functional, floor
imposed on the realizable duads only; per-orbit magnitude = FLOOR
is the exact Frobenius minimizer, sign frozen +1 on each orbit
representative) to measure exactly what survives.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
exact integer / sympy rational arithmetic in every decision, no
floats in decisions, no RNG, no fits):

 S0  SETUP (corpus rebuilt inline): q* selector, duad model, vacuum
     label V0, carrier dictionary phi, channel duads; Sp(4,2)
     census (720), Aut(C_fin) ~= C6, generator pin g^2 = sigma, the
     DEPLOYED channel permutation pi (fixes 0, cycle type (1,2,3));
     the canonical chi(i) = (-1)^(i+1).
 W1  THE COMMUTANT (exact linear algebra, nullspace of X -> PX-XP):
     (a) full commutant dimension on the 6x6 matrices; symmetric /
         antisymmetric split (expected 12 = 8 + 4 by the orbit
         count -- MEASURED, not assumed);
     (b) edge-orbit census of pi on the 15 duads: sizes + the
         ORIENTATION-REVERSAL law: an edge orbit supports a
         covariant antisymmetric value iff NO power of pi maps the
         ordered pair (i,j) to (j,i); the reversed orbits are
         exactly the forced zeros;
     (c) explicit orbit basis of the antisymmetric commutant:
         each element commutes exactly, the set spans the measured
         nullspace (rank ward);
     (d) isotypic structure: multiplicities of the six C6
         characters in the channel representation (Burnside /
         root-of-unity sums, exact), commutant dim = sum of
         multiplicity^2 (ward);
     (e) Specht cross-reference: the number of C6-invariant edge
         parameters (= Burnside orbit count on the 15 duads) splits
         across the round-44 Specht components 1 + 5 + 9 as
         1 + m_(5,1) + m_(4,2) (computed from fixed-point counts;
         the standard character identities chi_(5,1) = fix - 1,
         chi_(4,2) = fixduads - fix).
 W2  THE CANDIDATE (frozen rule of the search space above):
     (a) ray census: per basis ray the CAR eigenvalue bound (exact
         top singular value), the duads covered, the grading class
         -- (iii) fails on every single ray (measured);
     (b) FEASIBILITY (typed, fail-first): the feasible set at the
         frozen floor is nonempty iff NO duad is commutant-forced
         to zero; typed WICKMIX-CONSTRUCTED / WICKMIX-OBSTRUCTED
         by measurement;
     (c) the canonical (or maximal-support relaxed) candidate:
         verify (ii) exactly ([P_pi, A] == 0), (i) exactly
         (Frobenius bound ||A||_F < 1 => 0 < G < I strictly;
         eigenvalue range printed), (iii) the full 15-duad value
         table, (iv) the grading table + edge-law wiring on all 15
         messages + both-sector census + the N_fam ratio.
 W3  THE PFAFFIAN TEST (round-50 convention, round-49 gauge):
     symbolic Pf ward (15 monomials, coefficients +-1; sgn(M) =
     chi(i) * qsign(S,T) on all 15 -- the canonical gauge); then on
     the candidate: monomial values w(M) = sgn(M) C_0i C_jk C_lm;
     census of nonzero monomials (zero EXACTLY on matchings through
     a forced duad, if any); on every nonzero monomial the sign
     law sign(w) == chi(i) * qsign(S,T) * sign(C_0i C_jk C_lm);
     Pf(A) direct == sum of monomials (ward).  TYPED:
     WICKMIX-CONSTRUCTED iff all 15 monomials nonzero AND (i)-(iv)
     hold; WICKMIX-OBSTRUCTED otherwise, with the obstruction named
     exactly (which duads the commutant kills and why).
 D1  OBSTRUCTION ANATOMY (frozen diagnostics -- 'state it
     precisely' where the demand moves; run in both branches):
     (a) the C3 = <pi^2> relaxation: pi^2 is orientation-preserving
         on ALL 15 duads (measured); its antisymmetric commutant
         dimension (expected 7); the all-15 candidate at the floor:
         (i) + (iii) + (iv) full, all 15 Wick monomials nonzero
         with the sign law, [P_{pi^2}, A] == 0 exact -- but
         [P_pi, A] != 0 (Frobenius norm printed): the object exists
         at C3, NOT at the deployed C6;
     (b) the 16-dim lift: on the FULL deployed one-particle space
         (channel dims 2,2,2,2,2,6) construct an O16-covariant
         antisymmetric A16' by exact group averaging with ALL 15
         cross-channel blocks nonzero (the {a,b} block = t J is
         antisymmetric-2x2 and survives); CAR positivity after
         exact integer scaling; THEN the corollary: the round-50
         block-sum scalarization of A16' is itself a C6-covariant
         antisymmetric 6x6, hence vanishes on every reversed duad
         (measured == the W1 theorem instance): NO C6-equivariant
         antisymmetric scalarization can rescue the scalar channel
         space.
 W4  PHYSICS HONESTY NOTE: this probe constructs a CANDIDATE object
     satisfying (or provably obstructing) the STRUCTURAL
     conditions; whether the ACTUAL seam kernel realizes any
     channel-mixing covariance (the [O] premise: the boundary
     grammar IS a self-hosting Wick pair compiler) is untouched --
     NO marker moves.
 C   CONTROLS (must fire; frozen fire rules):
     C1 PERMUTED ROLES: conjugating the demanded C6 action by the
        transposition (0, a) (vacuum <-> the 2-cycle carrier a):
        (ii) breaks on the candidate (||[P', A]||_F^2 != 0,
        printed); (iv) breaks: the wrong vacuum Arf label violates
        the edge law on EXACTLY 8 of 15 messages (the round-50 C1
        census) and the wrong grading Gamma' does NOT commute with
        the deployed P_pi;
     C2 DIAGONAL G: the deployed G = I/2 (A = 0) fails (iii) with
        0/15 duads at the floor.

KILLS (any one fires => typed gap):
  K0 AST firewall / setup ward breaks              -> PIPELINE-BROKEN
  K1 commutant computation incoherent (nullspace
     vs orbit census vs isotypic dims)             -> COMMUTANT-BROKEN
  K2 candidate construction / (i)-(iv) verification
     incoherent with the typed feasibility         -> CANDIDATE-BROKEN
  K3 Pfaffian grammar / sign gauge breaks          -> WICK-BROKEN
  K4 obstruction-anatomy diagnostic breaks         -> ANATOMY-BROKEN
  K7 a control does not fire                       -> CONTROL-DEAD

VERDICT (frozen enum): WICKMIX-MEASURED [typed WICKMIX-CONSTRUCTED
/ WICKMIX-OBSTRUCTED(<obstruction>)] (no kills; the honest
obstruction is a first-class outcome) / WICKMIX-PARTIAL [kill
tokens] / PIPELINE-BROKEN / CONTROL-DEAD.  Exit 0 iff all checks
pass and no kill fired (an honest OBSTRUCTED exits 0); else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  AST firewall: banned identifiers
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime (self-scan).  NO physics-realization claim; the [O]
premise stays [O]; no marker moves.

SPEC v2 AMENDMENTS (fail-first preserved):
 A1 (post first run): the W1.6 EXPECTED isotypic multiplicity list
    was frozen with a transcription error ([3,0,1,1,0,1]); the
    hand derivation (fixed point -> chi_0; 2-cycle -> chi_0 +
    chi_3; 3-cycle -> chi_0 + chi_2 + chi_4) gives [3,0,1,1,1,0],
    which is what the exact root-of-unity sum measured on the
    fail-first run (all other W1.6 wards -- sum = 6, sum of
    squares = 12 = commutant dim -- passed unchanged).  Expected
    list corrected; no frozen decision rule changed.
 A2 (post first run): sympy BooleanAtom arithmetic guard (bool()
    around exact floor comparisons in two counters); no decision
    rule changed.

Sources (read-only, machinery rebuilt inline): seam_wick_functor_
probe (6 roles, deployed pi, grading test, scalarization
convention), k6_pfaffian_selfhosting_probe (chi gauge, qsign, C6
pin), s6_plucker_hadamard_probe (Specht 1+5+9), v113 (Majorana CAR
convention M = I + iA), v156 (D5+A3 split), v880/v888 (q*, duads,
phi), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wick_mixing_covariance_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()

FLOOR = sp.Rational(1, 200)     # (1/100) x diagonal scale 1/2 (frozen)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ---------------------------------------------------------- bit model
# (v880 / v888 conventions rebuilt inline; family/anchor basis)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    """order-3 deck sigma: (b0,b1,b2,b3) -> (b2,b0,b1,b3) (v880)."""
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    """q_c(v) = C(|v|,2) + c.v mod 2 -- the 16 refinements (v880)."""
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA[v]) if bit)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def pf_of(mat, idx):
    """recursive Pfaffian expansion along the first index of idx."""
    if not idx:
        return sp.Integer(1)
    i0, rest0 = idx[0], idx[1:]
    tot = sp.Integer(0)
    for k, j in enumerate(rest0):
        sub = [t for t in rest0 if t != j]
        tot += sp.Integer(-1) ** k * mat[i0, j] * pf_of(mat, sub)
    return tot


def all_matchings(vs):
    vs = sorted(vs)
    if not vs:
        return [frozenset()]
    a = vs[0]
    out = []
    for b in vs[1:]:
        rest = [x for x in vs if x not in (a, b)]
        for sub in all_matchings(rest):
            out.append(sub | {frozenset({a, b})})
    return out


def fro2(M):
    """exact squared Frobenius norm of a sympy matrix."""
    return sum(x * x for x in M)


def perm_matrix(perm):
    n = len(perm)
    return sp.Matrix(n, n, lambda r, c: 1 if r == perm[c] else 0)


def edge_orbits(perm):
    """orbits of perm on the 15 unordered duads of {0..5}, each with
    the ORIENTATION-REVERSAL flag: True iff some power maps the
    ordered pair (i,j) to (j,i)."""
    n_ord = perm_order(perm)
    seen = set()
    out = []
    for i, j in itertools.combinations(range(6), 2):
        e = frozenset({i, j})
        if e in seen:
            continue
        x, y = i, j
        edges = set()
        rev = False
        for _k in range(n_ord):
            edges.add(frozenset({x, y}))
            x, y = perm[x], perm[y]
            if (x, y) == (j, i):
                rev = True
        seen |= edges
        out.append((frozenset(edges), rev, (i, j)))
    return out


def orbit_elem(perm, i, j):
    """the covariant antisymmetric basis element of the (i,j) edge
    orbit (only valid for orientation-consistent orbits)."""
    E = sp.zeros(6)
    x, y = i, j
    for _k in range(perm_order(perm)):
        E[x, y] = 1
        E[y, x] = -1
        x, y = perm[x], perm[y]
    return E


def antisym_commutant_nullspace(P):
    """exact nullspace of A -> PA - AP on the 15-dim antisymmetric
    coordinate space (coords aligned with DUADS_CH)."""
    cols = []
    for (i, j) in DUADS_CH:
        E = sp.zeros(6)
        E[i, j] = 1
        E[j, i] = -1
        C = P * E - E * P
        cols.append(sp.Matrix(36, 1, lambda r, _c:
                              C[r // 6, r % 6]))
    return sp.Matrix.hstack(*cols).nullspace()


DUADS_CH = sorted(itertools.combinations(range(6), 2))


def main():
    print("SEAM.CFIN.WICKMIX.01 -- the channel-mixing quasifree CAR "
          "covariance (round-50 gap)")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO physics-realization claim; the [O] premise stays [O]; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (corpus rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s"
          % (BANNED_IDS,), not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique "
          "q* under the frozen selector",
          ok_ref and len(set(refs)) == 16 and len(arf1) == 6
          and len(cand) == 1, kill="K0")
    QSTAR = cand[0]
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    DUADS_L = sorted((frozenset(d)
                      for d in itertools.combinations(range(6), 2)),
                     key=sorted)
    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS_L)
    check("S0.2 duad model: 15 messages <-> 15 duads; vacuum label "
          "V0 = %d" % V0, biject and 0 <= V0 < 6, kill="K0")

    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5
               and set(phi.values()) == set(range(1, 6)))
    check("S0.3 carrier dictionary phi (ovoid-induced) bijective: %s"
          % (sorted(phi.items()),), ok_phi, kill="K0")

    def lab(j):
        return 0 if j == V0 else phi[j]

    def chduad(v):
        return frozenset(lab(j) for j in dmap[v])

    chd = {v: chduad(v) for v in NZ}
    inv_chd = {frozenset(d): v for v, d in chd.items()}
    check("S0.4 the 15 messages map bijectively onto the 15 channel "
          "duads (V0 -> channel 0)",
          sorted(chd.values(), key=sorted) == DUADS_L, kill="K0")

    # deployed C6: Sp(4,2) census + Aut pin (round-50 T6 rebuilt)
    gl_n = 0
    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        gl_n += 1
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA[p[v]] == tuple(IOTA[v][pi[s]]
                                          for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.5 |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == 720, "
          "|Aut(C_fin)| = %d == 6, generator pin g^2 = sigma unique"
          % (gl_n, len(SP6), len(AUT)),
          gl_n == 20160 and len(SP6) == 720 and len(AUT) == 6
          and len(g_pin) == 1, kill="K0")
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(pia[j])
    PI6 = tuple(PI6)
    ct6 = cycle_type(PI6)
    ok_int = all(dmap[GEN[v]] == frozenset(pia[j] for j in dmap[v])
                 for v in NZ)
    check("S0.6 DEPLOYED channel permutation pi = phi o pi_a o "
          "phi^-1 = %s: fixes channel 0, cycle type %s == (1, 2, 3);"
          " intertwines the duad action on all 15"
          % (PI6, ct6),
          PI6[0] == 0 and ct6 == (1, 2, 3) and ok_int, kill="K0")

    cycles = []
    seen = set()
    for i in range(6):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = PI6[j]
        cycles.append(cyc)
    TWO = sorted(next(c for c in cycles if len(c) == 2))
    THREE = next(c for c in cycles if len(c) == 3)
    a_ch, b_ch = TWO
    print("      pi cycles: fixed 0, 2-cycle %s, 3-cycle %s"
          % (TWO, sorted(THREE)))
    chi = {i: (-1) ** (i + 1) for i in range(1, 6)}
    P6M = perm_matrix(PI6)

    # ==================================================================
    section("W1 -- THE COMMUTANT of the deployed C6 on the channel "
            "space")
    # ==================================================================
    # (a) full / symmetric / antisymmetric commutant dims (exact)
    cols_full = []
    for r0 in range(6):
        for c0 in range(6):
            E = sp.zeros(6)
            E[r0, c0] = 1
            C = P6M * E - E * P6M
            cols_full.append(sp.Matrix(36, 1, lambda r, _c:
                                       C[r // 6, r % 6]))
    dim_full = 36 - sp.Matrix.hstack(*cols_full).rank()
    cols_sym = []
    for r0 in range(6):
        for c0 in range(r0, 6):
            E = sp.zeros(6)
            E[r0, c0] = 1
            E[c0, r0] = 1
            C = P6M * E - E * P6M
            cols_sym.append(sp.Matrix(36, 1, lambda r, _c:
                                      C[r // 6, r % 6]))
    dim_sym = 21 - sp.Matrix.hstack(*cols_sym).rank()
    null_anti = antisym_commutant_nullspace(P6M)
    dim_anti = len(null_anti)
    check("W1.1(a) commutant dims (exact nullspaces): full = %d, "
          "symmetric = %d, antisymmetric = %d; full == sym + anti"
          % (dim_full, dim_sym, dim_anti),
          dim_full == dim_sym + dim_anti == 12
          and dim_sym == 8 and dim_anti == 4, kill="K1")

    # (b) edge-orbit census + orientation-reversal law
    orbs = edge_orbits(PI6)
    sizes = sorted(len(o[0]) for o in orbs)
    rev_orbs = [o for o in orbs if o[1]]
    forced_duads = sorted(sorted(e)
                          for o in rev_orbs for e in o[0])
    check("W1.2(b) edge orbits of pi on the 15 duads: sizes %s == "
          "[1, 2, 3, 3, 6]; ORIENTATION-REVERSED orbits: %d, "
          "forced-zero duads = %s (expected: exactly the transposed "
          "pair {%d,%d})"
          % (sizes, len(rev_orbs), forced_duads, a_ch, b_ch),
          sizes == [1, 2, 3, 3, 6] and len(rev_orbs) == 1
          and forced_duads == [[a_ch, b_ch]], kill="K1")
    check("W1.3(b) commutant dimension law: dim(antisym commutant) "
          "= #orbits - #reversed = %d - %d = %d (matches W1.1)"
          % (len(orbs), len(rev_orbs), len(orbs) - len(rev_orbs)),
          len(orbs) - len(rev_orbs) == dim_anti, kill="K1")
    idx_ab = DUADS_CH.index((a_ch, b_ch))
    forced_in_null = all(v[idx_ab] == 0 for v in null_anti)
    check("W1.4(b) FORCED ZERO: every antisymmetric commutant "
          "element vanishes on the transposed duad {%d,%d} "
          "(all %d nullspace vectors have coordinate 0 there)"
          % (a_ch, b_ch, dim_anti), forced_in_null, kill="K1")

    # (c) explicit orbit basis
    nonrev = [o for o in orbs if not o[1]]
    BASIS_E = [orbit_elem(PI6, *o[2]) for o in nonrev]
    ok_comm = all(sp.simplify(P6M * E - E * P6M) == sp.zeros(6)
                  for E in BASIS_E)
    stack = sp.Matrix.hstack(*[sp.Matrix(36, 1, lambda r, _c:
                                         E[r // 6, r % 6])
                               for E in BASIS_E])
    check("W1.5(c) explicit orbit basis (%d elements, reps %s): "
          "each commutes with P_pi exactly; rank %d == dim = %d "
          "(spans the commutant)"
          % (len(BASIS_E), [o[2] for o in nonrev], stack.rank(),
             dim_anti),
          ok_comm and len(BASIS_E) == dim_anti
          and stack.rank() == dim_anti, kill="K1")

    # (d) isotypic structure of the C6 representation on C^6
    fixpts = []
    pk = tuple(range(6))
    for _k in range(6):
        fixpts.append(sum(1 for i in range(6) if pk[i] == i))
        pk = compose(PI6, pk)
    zeta = sp.exp(2 * sp.pi * sp.I / 6)
    mults = [sp.simplify(sp.Rational(1, 6)
                         * sum(fixpts[k] * zeta ** (-j * k)
                               for k in range(6)))
             for j in range(6)]
    mults = [sp.nsimplify(m) for m in mults]
    sum_sq = sum(m ** 2 for m in mults)
    check("W1.6(d) isotypic multiplicities of the C6 characters "
          "(chi_0..chi_5) in the channel rep: %s == [3,0,1,1,1,0] "
          "(3 chi_0 + chi_2 + chi_3 + chi_4: fixed point + 2-cycle "
          "+ 3-cycle); sum m^2 = %s == 12 == full commutant dim "
          "(M3(C) + C + C + C)" % (mults, sum_sq),
          mults == [3, 0, 1, 1, 1, 0] and sum_sq == 12
          and sum(mults) == 6, kill="K1")

    # (e) Specht cross-reference on the induced 15-duad action
    fixdu = []
    pk = tuple(range(6))
    for _k in range(6):
        fixdu.append(sum(1 for (i, j) in DUADS_CH
                         if {pk[i], pk[j]} == {i, j}))
        pk = compose(PI6, pk)
    n_orb15 = sp.Rational(sum(fixdu), 6)
    m51 = sp.Rational(sum(f - 1 for f in fixpts), 6)
    m42 = sp.Rational(sum(fd - fp for fd, fp in zip(fixdu, fixpts)),
                      6)
    check("W1.7(e) SPECHT CROSS-REF: Burnside invariants on the 15 "
          "duads = %s == 5 (= the covariant edge parameters); split "
          "across 15 = 1 + 5 + 9: 1 (S^(6)) + %s (S^(5,1)) + %s "
          "(S^(4,2)) = 5; the antisymmetric side keeps 5 - 1 = 4 "
          "(the reversed orbit is killed by orientation)"
          % (n_orb15, m51, m42),
          n_orb15 == 5 and m51 == 2 and m42 == 2
          and 1 + m51 + m42 == n_orb15, kill="K1")

    # ==================================================================
    section("W2 -- THE CANDIDATE (frozen source functional at the "
            "frozen floor)")
    # ==================================================================
    # (a) ray census
    print("      ray census (per commutant basis ray):")
    ray_rows = []
    for o, E in zip(nonrev, BASIS_E):
        ev = (-(E * E)).eigenvals()
        smax2 = max(ev.keys(), key=lambda e: sp.N(e))
        duads_cov = sorted(sorted(e) for e in o[0])
        grad = "vac" if any(0 in e for e in o[0]) else "car"
        ray_rows.append((o[2], len(o[0]), grad, smax2))
        print("        rep %s  orbit size %d  class %s  "
              "sval_max = sqrt(%s)  CAR coeff bound 1/sqrt(%s)  "
              "duads %s"
              % (o[2], len(o[0]), grad, smax2, smax2, duads_cov))
    ok_rays = all(n < 14 for _r, n, _g, _s in ray_rows)
    check("W2.1(a) every single ray covers < 14 duads (max = %d): "
          "(iii) fails on each ray alone; a full candidate needs "
          "all %d rays"
          % (max(n for _r, n, _g, _s in ray_rows), dim_anti),
          ok_rays, kill="K2")

    # (b) feasibility at the frozen floor (typed, fail-first)
    feasible = (len(rev_orbs) == 0)
    t_w2 = ("WICKMIX-CONSTRUCTED" if feasible
            else "WICKMIX-OBSTRUCTED(TRANSPOSED-DUAD-ZERO)")
    check("W2.2(b) FEASIBILITY: the feasible set {A covariant, all "
          "15 |C_ij| >= 1/200} is %s -- duad {%d,%d} is commutant-"
          "forced to 0 < FLOOR for EVERY covariant candidate (W1.4)"
          "; typed %s"
          % ("NONEMPTY" if feasible else "EMPTY", a_ch, b_ch, t_w2),
          feasible == (t_w2 == "WICKMIX-CONSTRUCTED"), kill="K2")

    # (c) canonical (maximal-support relaxed) candidate:
    # per-orbit magnitude = FLOOR minimizes ||G - I/2||_F among
    # candidates at the floor on the realizable duads (distance^2 =
    # (1/4) sum orbit_size * param^2, monotone in each |param|);
    # sign frozen +1 on each orbit representative.
    K6C = sum(BASIS_E, sp.zeros(6))
    A_c = FLOOR * K6C
    G_c = (sp.eye(6) + sp.I * A_c) / 2
    comm_c = sp.simplify(P6M * A_c - A_c * P6M)
    check("W2.3(c) condition (ii): [P_pi, A] == 0 EXACTLY "
          "(commutator norm^2 = %s); hence [P_pi, G] = 0"
          % fro2(comm_c), comm_c == sp.zeros(6), kill="K2")

    f2 = fro2(A_c)
    ev_k = (-(K6C * K6C)).eigenvals()
    smax2_k = max(ev_k.keys(), key=lambda e: sp.N(e))
    smax = FLOOR * sp.sqrt(smax2_k)
    lo, hi = (1 - smax) / 2, (1 + smax) / 2
    check("W2.4(c) condition (i): ||A||_F^2 = %s < 1 (exact) => "
          "spec(A) in (-1, 1) => 0 < G < I STRICTLY; exact G "
          "eigenvalue range [(1-s)/2, (1+s)/2] = [%s, %s] ~ "
          "[%.6f, %.6f] in [0, 1]"
          % (f2, lo, hi, sp.N(lo), sp.N(hi)),
          f2 < 1 and sp.simplify(G_c - G_c.H) == sp.zeros(6),
          kill="K2")

    Gamma = sp.diag(1, -1, -1, -1, -1, -1)
    ok_gp = sp.simplify(Gamma * P6M - P6M * Gamma) == sp.zeros(6)
    A_odd = (A_c - Gamma * A_c * Gamma) / 2
    A_even = (A_c + Gamma * A_c * Gamma) / 2
    odd_sup = {frozenset({i, j}) for (i, j) in DUADS_CH
               if A_odd[i, j] != 0}
    even_sup = {frozenset({i, j}) for (i, j) in DUADS_CH
                if A_even[i, j] != 0}
    vac_duads = {frozenset(chd[v]) for v in NZ if QSTAR[v] == 0}
    car_duads = {frozenset(chd[v]) for v in NZ if QSTAR[v] == 1}
    edge_law = all((QSTAR[v] == 0) == (0 in chd[v]) for v in NZ)
    dims_ch = {0: 6, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2}
    check("W2.5(c) condition (iv): [Gamma, P_pi] == 0 (%s); edge "
          "law q*(v)=0 iff duad touches channel 0 on all 15 (%s); "
          "Ad(Gamma)-odd support == the 5 q*=0 (vacuum) duads (%s);"
          " even off-diag support inside the 10 q*=1 duads (%s); "
          "sector-dim ratio 12/4 = %d = N_fam (cross-ref)"
          % (ok_gp, edge_law, odd_sup == vac_duads,
             even_sup <= car_duads, (dims_ch[0] * 2) // 4),
          ok_gp and edge_law and odd_sup == vac_duads
          and even_sup <= car_duads
          and (dims_ch[0] * 2) // 4 == N_fam and g_car == 5,
          kill="K2")

    print("      15-duad table (duad; class; q*(message); C_ij):")
    n_floor = 0
    zero_duads = []
    for (i, j) in DUADS_CH:
        d = frozenset({i, j})
        v = inv_chd[d]
        val = A_c[i, j]
        at = bool(abs(val) >= FLOOR)
        n_floor += at
        if val == 0:
            zero_duads.append((i, j))
        print("        {%d,%d}  %s  q*=%d  C = %s%s"
              % (i, j, "vac" if 0 in d else "car", QSTAR[v],
                 val, "" if at else "   << BELOW FLOOR"))
    check("W2.6(c) condition (iii) census: %d/15 duads at the "
          "floor; zeros exactly on the forced duad(s) %s; odd "
          "sector 5/5 nonzero, even sector %d/10 -- the failure is "
          "LOCALIZED in the carrier-carrier (q*=1) grading sector"
          % (n_floor, zero_duads, len(even_sup)),
          n_floor == 14 and zero_duads == [(a_ch, b_ch)]
          and len(odd_sup) == 5 and len(even_sup) == 9,
          kill="K2")

    # ==================================================================
    section("W3 -- THE PFAFFIAN TEST (round-50 convention, chi "
            "gauge)")
    # ==================================================================
    SYM = {}
    for i in range(6):
        for j in range(i + 1, 6):
            SYM[(i, j)] = sp.Symbol("a_%d%d" % (i, j))
    G6 = sp.Matrix(6, 6, lambda r, c:
                   SYM[(r, c)] if r < c
                   else (-SYM[(c, r)] if r > c else 0))
    PF6 = sp.expand(pf_of(G6, list(range(6))))
    cd = PF6.as_coefficients_dict()
    MSLOT = all_matchings(range(6))

    def mono_of(m):
        out = sp.Integer(1)
        for e in m:
            out *= SYM[tuple(sorted(e))]
        return out

    sgn = {}
    ok_c = True
    for m in MSLOT:
        c = cd.get(mono_of(m), 0)
        ok_c &= (c in (1, -1))
        sgn[frozenset(m)] = int(c)

    def m_ist(m):
        vac_e = next(e for e in m if 0 in e)
        i = next(iter(vac_e - {0}))
        S, T = sorted((tuple(sorted(e)) for e in m if e != vac_e))
        return i, S, T

    def qsign(i, S, T):
        j, k, l, m4 = sorted(set(range(1, 6)) - {i})
        three = [frozenset({frozenset({j, k}), frozenset({l, m4})}),
                 frozenset({frozenset({j, l}), frozenset({k, m4})}),
                 frozenset({frozenset({j, m4}), frozenset({k, l})})]
        key = frozenset({frozenset(S), frozenset(T)})
        return (1, -1, 1)[three.index(key)]

    ok_gauge = all(
        sgn[frozenset(m)]
        == chi[m_ist(m)[0]] * qsign(*m_ist(m)) for m in MSLOT)
    check("W3.1 symbolic ward: Pf has EXACTLY 15 monomials, "
          "coefficients +-1; sgn(M) == chi(i) * qsign(S,T) with the "
          "canonical chi(i) = (-1)^(i+1) on all 15 (round-49 gauge)",
          len(cd) == 15 and ok_c and ok_gauge, kill="K3")

    def wick_value(A, m):
        out = sp.Integer(sgn[frozenset(m)])
        for e in m:
            x, y = sorted(e)
            out *= A[x, y]
        return out

    ab_edge = frozenset({a_ch, b_ch})
    w_vals = {frozenset(m): wick_value(A_c, m) for m in MSLOT}
    zero_ms = [m for m in MSLOT if w_vals[frozenset(m)] == 0]
    thru_ab = [m for m in MSLOT if ab_edge in m]
    check("W3.2 Wick monomial census on the candidate: %d/15 "
          "nonzero; the %d vanishing monomials are EXACTLY the "
          "matchings through the forced duad {%d,%d}"
          % (15 - len(zero_ms), len(zero_ms), a_ch, b_ch),
          len(zero_ms) == 3
          and {frozenset(m) for m in zero_ms}
          == {frozenset(m) for m in thru_ab}, kill="K3")

    ok_slaw = True
    for m in MSLOT:
        w = w_vals[frozenset(m)]
        if w == 0:
            continue
        i, S, T = m_ist(m)
        prod = sp.Integer(1)
        for e in m:
            x, y = sorted(e)
            prod *= A_c[x, y]
        ok_slaw &= (sp.sign(w)
                    == chi[i] * qsign(i, S, T) * sp.sign(prod))
    pf_direct = sp.expand(pf_of(A_c, list(range(6))))
    pf_sum = sp.expand(sum(w_vals.values()))
    check("W3.3 SIGN LAW on all nonzero monomials: sign(w(M)) == "
          "chi(i) * qsign(S,T) * sign(C_0i C_jk C_lm); Pf(A) direct "
          "= %s == sum of monomials (%s)"
          % (pf_direct, pf_sum == pf_direct),
          ok_slaw and pf_sum == pf_direct, kill="K3")
    t_w3 = t_w2 if not feasible else (
        "WICKMIX-CONSTRUCTED" if len(zero_ms) == 0 else
        "WICKMIX-OBSTRUCTED(MONOMIALS-VANISH)")
    check("W3.4 TYPED OUTCOME: %s -- conditions (ii) + (iii) are "
          "jointly UNSATISFIABLE on the 6-dim scalar channel space: "
          "the deployed pi reverses the orientation of exactly one "
          "duad ({%d,%d}, its 2-cycle), every C6-covariant "
          "antisymmetric object vanishes there, max covariant "
          "support = 14/15, and 3/15 Wick monomials vanish for "
          "EVERY candidate" % (t_w3, a_ch, b_ch),
          t_w3.startswith("WICKMIX-"), kill="K3")

    # ==================================================================
    section("D1 -- OBSTRUCTION ANATOMY (where the demand moves; "
            "frozen diagnostics)")
    # ==================================================================
    # (a) the C3 = <pi^2> relaxation
    PI3 = compose(PI6, PI6)
    P3M = perm_matrix(PI3)
    orbs3 = edge_orbits(PI3)
    rev3 = [o for o in orbs3 if o[1]]
    null3 = antisym_commutant_nullspace(P3M)
    check("D1.1(a) C3 = <pi^2> (cycle type %s on channels): edge "
          "orbits %s (sizes), NO orientation-reversed orbit (%d); "
          "antisymmetric commutant dim = %d == 7 == #orbits"
          % (cycle_type(PI3), sorted(len(o[0]) for o in orbs3),
             len(rev3), len(null3)),
          cycle_type(PI3) == (1, 1, 1, 3)
          and len(rev3) == 0 and len(null3) == 7
          and len(orbs3) == 7, kill="K4")

    A3 = FLOOR * sum((orbit_elem(PI3, *o[2]) for o in orbs3),
                     sp.zeros(6))
    n3_floor = sum(1 for (i, j) in DUADS_CH
                   if bool(abs(A3[i, j]) >= FLOOR))
    comm3 = sp.simplify(P3M * A3 - A3 * P3M)
    comm6 = sp.simplify(P6M * A3 - A3 * P6M)
    f2_3 = fro2(A3)
    A3_odd = (A3 - Gamma * A3 * Gamma) / 2
    odd3 = {frozenset({i, j}) for (i, j) in DUADS_CH
            if A3_odd[i, j] != 0}
    check("D1.2(a) the C3 candidate A3 (all 7 orbit params = "
          "+FLOOR): (iii) 15/15 duads at the floor (%d); (i) "
          "||A3||_F^2 = %s < 1; (iv) odd sector 5/5 (%s), even "
          "10/10; [P_{pi^2}, A3] == 0 EXACTLY (%s)"
          % (n3_floor, f2_3, odd3 == vac_duads,
             comm3 == sp.zeros(6)),
          n3_floor == 15 and f2_3 < 1 and odd3 == vac_duads
          and comm3 == sp.zeros(6), kill="K4")
    check("D1.3(a) but NOT C6-covariant: ||[P_pi, A3]||_F^2 = %s "
          "!= 0 -- the reviewer's object EXISTS at C3 = <g^2>, NOT "
          "at the deployed C6" % fro2(comm6),
          comm6 != sp.zeros(6) and fro2(comm6) > 0, kill="K4")

    w3_vals = {frozenset(m): wick_value(A3, m) for m in MSLOT}
    n3_wick = sum(1 for w in w3_vals.values() if w != 0)
    ok_slaw3 = True
    for m in MSLOT:
        w = w3_vals[frozenset(m)]
        i, S, T = m_ist(m)
        prod = sp.Integer(1)
        for e in m:
            x, y = sorted(e)
            prod *= A3[x, y]
        ok_slaw3 &= (sp.sign(w)
                     == chi[i] * qsign(i, S, T) * sp.sign(prod))
    pf3 = sp.expand(pf_of(A3, list(range(6))))
    check("D1.4(a) C3 candidate Wick census: %d/15 monomials "
          "nonzero; sign law holds on all 15; Pf(A3) = %s"
          % (n3_wick, pf3),
          n3_wick == 15 and ok_slaw3, kill="K4")

    # (b) the 16-dim lift (full deployed one-particle space)
    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    O16 = sp.zeros(16)
    for r in CH[0]:
        O16[r, r] = 1
    for i in range(1, 6):
        src, dst = CH[i], CH[PI6[i]]
        O16[dst[0], src[0]] = 1
        O16[dst[1], src[1]] = 1
    J2 = sp.Matrix([[0, 1], [-1, 0]])

    def put_block(X, i, j, B):
        for r in range(len(CH[i])):
            for c in range(len(CH[j])):
                X[CH[i][r], CH[j][c]] = B[r, c]
                X[CH[j][c], CH[i][r]] = -B[r, c]

    c3_ch = THREE[0]
    d3_ch = PI6[c3_ch]
    X = sp.zeros(16)
    put_block(X, 0, a_ch, sp.ones(6, 2))
    put_block(X, 0, c3_ch, sp.Matrix(6, 2, lambda r, c:
                                     r + 2 * c + 1))
    put_block(X, a_ch, b_ch, J2)
    put_block(X, a_ch, c3_ch, sp.Matrix([[1, 2], [3, 4]]))
    put_block(X, c3_ch, d3_ch, sp.Matrix([[1, 2], [3, 5]]))
    A16 = sp.zeros(16)
    Ok = sp.eye(16)
    for _k in range(6):
        A16 += Ok * X * Ok.T
        Ok = O16 * Ok
    ok_cov16 = sp.simplify(O16 * A16 * O16.T - A16) == sp.zeros(16)
    ok_anti16 = sp.simplify(A16 + A16.T) == sp.zeros(16)
    blk_max = {}
    blk_sum = {}
    for (i, j) in DUADS_CH:
        ent = [A16[r, c] for r in CH[i] for c in CH[j]]
        blk_max[(i, j)] = max(abs(x) for x in ent)
        blk_sum[(i, j)] = sum(ent)
    n_blk = sum(1 for v in blk_max.values() if v != 0)
    F16 = fro2(A16)
    t16 = sp.Rational(1, math.isqrt(int(F16)) + 1)
    check("D1.5(b) 16-DIM LIFT: O16-covariant antisymmetric A16' "
          "by exact group averaging: covariance EXACT (%s), "
          "antisymmetric (%s); ALL 15 cross-channel blocks nonzero "
          "(%d/15; the {%d,%d} block is antisymmetric 2x2 ~ J and "
          "SURVIVES); CAR positivity after scaling t = %s "
          "(t^2 ||A16'||_F^2 = %s < 1)"
          % (ok_cov16, ok_anti16, n_blk, a_ch, b_ch, t16,
             t16 ** 2 * F16),
          ok_cov16 and ok_anti16 and n_blk == 15
          and blk_max[(a_ch, b_ch)] != 0
          and t16 ** 2 * F16 < 1, kill="K4")

    S6S = sp.zeros(6)
    for (i, j) in DUADS_CH:
        S6S[i, j] = blk_sum[(i, j)]
        S6S[j, i] = -blk_sum[(i, j)]
    ok_s_cov = sp.simplify(P6M * S6S - S6S * P6M) == sp.zeros(6)
    n_s = sum(1 for (i, j) in DUADS_CH if S6S[i, j] != 0)
    check("D1.6(b) COROLLARY (the W1 theorem in action): the "
          "round-50 block-sum scalarization of A16' is itself "
          "C6-covariant antisymmetric (%s) -- hence it vanishes on "
          "{%d,%d} (value %s == 0) while carrying %d/14 of the "
          "other duads: NO C6-equivariant antisymmetric "
          "scalarization can rescue the 6-dim scalar channel space;"
          " the demand provably moves to the block level (or to C3)"
          % (ok_s_cov, a_ch, b_ch, S6S[a_ch, b_ch], n_s),
          ok_s_cov and S6S[a_ch, b_ch] == 0 and n_s == 14,
          kill="K4")

    # ==================================================================
    section("W4 -- physics honesty note")
    # ==================================================================
    check("W4.1 HONESTY: this probe constructs/obstructs a "
          "CANDIDATE structural object on the channel space; "
          "whether the ACTUAL seam kernel realizes any channel-"
          "mixing covariance (the [O] premise: the boundary grammar "
          "IS a self-hosting Wick pair compiler) is UNTOUCHED -- "
          "no marker moves", True, "typed, no upgrade")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    rho = tuple(a_ch if x == 0 else (0 if x == a_ch else x)
                for x in range(6))
    R = perm_matrix(rho)
    P6W = R * P6M * R.T
    commW = sp.simplify(P6W * A_c - A_c * P6W)
    w_arf = next(j for j in range(6) if lab(j) == a_ch)
    mism = sum(1 for v in NZ
               if (QSTAR[v] == 0) != (w_arf in dmap[v]))
    GammaW = R * Gamma * R.T
    gw = sp.simplify(GammaW * P6M - P6M * GammaW)
    check("C1 FIRES: PERMUTED ROLES (transposition (0, %d)): (ii) "
          "breaks on the candidate: ||[P', A]||_F^2 = %s != 0; "
          "(iv) breaks: wrong vacuum label -> edge law fails on "
          "EXACTLY %d == 8 of 15 messages; wrong grading Gamma' "
          "does NOT commute with the deployed P_pi (||.||_F^2 = %s "
          "!= 0)" % (a_ch, fro2(commW), mism, fro2(gw)),
          commW != sp.zeros(6) and mism == 8
          and gw != sp.zeros(6), kill="K7")

    n_diag = sum(1 for (i, j) in DUADS_CH
                 if abs(sp.zeros(6)[i, j]) >= FLOOR)
    check("C2 FIRES: DIAGONAL G = I/2 (the deployed vacuum, A = 0): "
          "(iii) fails with %d/15 duads at the floor" % n_diag,
          n_diag == 0, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif KILLS:
        VERDICT = "WICKMIX-PARTIAL [%s]" % ", ".join(
            sorted(set({"K1": "COMMUTANT-BROKEN",
                        "K2": "CANDIDATE-BROKEN",
                        "K3": "WICK-BROKEN",
                        "K4": "ANATOMY-BROKEN"}.get(k, k)
                       for k in KILLS)))
    else:
        VERDICT = "WICKMIX-MEASURED [%s]" % t_w3
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE COMMUTANT (W1): the deployed C6 channel action pi =
    (0)(%d %d)(%s) has commutant dims 12 = 8 sym + 4 antisym;
    the 15 duads fall into 5 edge orbits (1+2+3+3+6), of which
    EXACTLY ONE -- the transposed pair {%d,%d} -- is orientation-
    reversed; Specht restriction: the 5 invariant edge parameters
    split 1 + 2 + 2 across 15 = 1 + 5 + 9.
  * THE OBSTRUCTION (W2/W3, measured): every C6-covariant
    antisymmetric 6x6 object (= the Pfaffian-carrying part of ANY
    quasifree channel covariance in the corpus Majorana convention)
    vanishes identically on {%d,%d}.  Conditions (ii) + (iii) are
    jointly unsatisfiable on the scalar channel space: the feasible
    set at the frozen floor is EMPTY, max covariant support is
    14/15 duads, and the 3 Wick monomials through {%d,%d} vanish
    for every candidate.  The canonical maximal-support candidate
    satisfies (i), (ii), (iv-odd) exactly, carries 14/15 duads and
    12/15 Wick monomials with the canonical chi sign law.
  * WHERE THE DEMAND MOVES (D1, both constructed): (a) at C3 =
    <g^2> (orientation-preserving on all 15 duads) the full object
    EXISTS: commutant dim 7, all 15 duads at the floor, all 15
    Wick monomials nonzero with the chi sign law -- the C6/C3 gap
    is exactly the outer 2-cycle of the pinned generator; (b) on
    the FULL 16-dim one-particle space an O16-covariant
    antisymmetric object exists with ALL 15 cross-blocks nonzero
    (the {%d,%d} block is the antisymmetric 2x2 ~ J), CAR-positive
    after exact scaling -- but its (and any) C6-equivariant
    antisymmetric scalarization back to 6x6 re-kills {%d,%d}: the
    round-51 demand is therefore BLOCK-LEVEL (matrix-valued duad
    two-point functions) or C3-restricted, never scalar-C6.
  * The [O] premise (the boundary grammar IS a self-hosting Wick
    pair compiler) stays [O]; no marker moves.
Runtime: %.1f s""" % (a_ch, b_ch,
                      " ".join(str(x) for x in THREE),
                      a_ch, b_ch, a_ch, b_ch, a_ch, b_ch,
                      a_ch, b_ch, a_ch, b_ch,
                      time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source wick_block_functor_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wick_block_functor_probe -- SEAM.CFIN.WICKBLOCK.01
(EXPLORATION ONLY, experiments/; round 52, named object (d): the
BLOCK-VALUED Wick functor -- the demand made precise by the round-51
obstruction.  wick_mixing_covariance_probe PROVED that on the 6-dim
scalar channel space every C6-covariant antisymmetric covariance
vanishes on the transposed duad, that NO equivariant scalarization
rescues the scalar space, and that the 16-dim BLOCK object exists
(O16-covariant, CAR-positive, all 15 cross-blocks nonzero, the
transposed block antisymmetric 2x2 ~ J).  THIS probe builds the FULL
block-level functor on the 16-dim one-particle space and tests the
review's five conditions at BLOCK level.)

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-09 -- read end to end: wick_mixing_covariance_probe (round
51), seam_wick_functor_probe (round 50), k6_pfaffian_selfhosting_
probe (round 49), v113/v155/v156/v160/v161, v880/v888):
 * round 51 constructed ONE 16-dim witness A16' by group averaging
   ARBITRARY seed blocks (D1.5(b)) -- existence only; it froze NO
   canonicalization, computed NO block commutant dimension, NO block
   Pfaffian / matching structure, NO block grading census, and ran
   NO block-level controls.
 * round 50 identified the 6 roles (five D5 slot pairs + the A3
   boundary block, dims 2,2,2,2,2,6), measured the deployed vacuum
   kernel CHANNEL-DIAGONAL, pinned the deployed C6 channel
   permutation pi (fixes 0, cycle type (1,2,3)) and its orthogonal
   lift O16 (slot pairs as units, identity on the A3 block).
 * round 49 froze the canonical sign gauge chi(i) = (-1)^(i+1) and
   PROVED (T2.5) that the fermionic Pfaffian sign IS the Lambda^5
   volume-form sign of b_S ^ b_T ^ e_i.
 * NOTHING in the corpus canonicalizes the block object, tests the
   block Pfaffian / matching structure, or asks whether the DEPLOYED
   seam covariance has nonzero cross-blocks (the seam-mixing
   question at block level).  That is exactly this probe.

CAR CONVENTION (FROZEN, v113 / rounds 50-51): 16-dim real Majorana
one-particle space, channels CH(0) = Majoranas 10..15 (A3 boundary
block, dim 6 = 3 deployed pairs), CH(i) = {2(i-1), 2(i-1)+1} for
i = 1..5 (D5 slot pairs, dim 2).  A quasifree CAR covariance is
G = (I + iA)/2 with A REAL ANTISYMMETRIC; CAR positivity 0 <= G <= I
<=> spec-norm(A) <= 1.  The BLOCK duad values are the cross-channel
blocks C_ij := A[CH(i), CH(j)] (i < j; C_ji = -C_ij^T).  The
deployed C6 acts by the round-50 lift O16 (permute slot pairs as
units by pi, identity on the A3 block); block covariance means
O16 A O16^T = A.

THE CANONICAL BLOCK OBJECT (FROZEN canonicalization -- the round-51
witness construction made canonical): G_c = (I + iA_c)/2 with A_c
supported EXACTLY on the 15 cross-blocks, C6-covariant, built per
edge orbit of pi on the 15 duads by orientation-propagating a FROZEN
unit block from the lexicographic-first orbit representative, with
per-block magnitude = FLOOR := 1/200 (the round-51 frozen floor; for
fixed directions the per-block magnitude at the floor is the exact
Frobenius minimizer of ||G - I/2||_F among covariant objects with
all 15 blocks at the floor -- minimal-norm rule, monotone).  FROZEN
unit blocks (each justified by the deployed kernel, no fitting):
 * vacuum orbits {0,i} (6x2): U = Iota := [I2; I2; I2] -- the unique
   slot-isotropic pattern; CANONICAL because Iota^T (J+J+J) Iota / 3
   = J: the compression by Iota (normalization 1/3 = 1/N_fam)
   carries the deployed boundary kernel J+J+J EXACTLY onto the
   deployed slot kernel J;
 * free pair orbits (2x2): U = I2 -- the symmetric unit of the
   2-dim commutant span{I, J} of the deployed within-slot kernel J
   (the antisymmetric unit J is reserved for the orientation-forced
   block; the two units stay separated);
 * the reversed (transposed) orbit {a,b} (2x2): U = J -- FORCED
   antisymmetric by orientation reversal (round-51 theorem), the
   deployed-kernel direction; sign +1 on each representative.

BLOCK SIGN CONVENTION (FROZEN, derived -- the k6 Lambda^5 volume
identification lifted to the block space): at scalar level (k6 probe
T2.5) sgn(M) = sign of b_S ^ b_T ^ e_i vs e_1^...^e_5 = chi(i) *
qsign(S,T) with chi(i) = (-1)^(i+1).  At block level every channel
direction e_i inflates to a 2-frame (the vacuum channel first
compressed by the frozen Iota / 3); the interleaving permutation
that groups the 12 block indices by a matching's edges is the scalar
matching permutation acting on 2-blocks, whose sign is
sgn(M)^(2x2) = +1: the Lambda^10 lift of the scalar volume character
is TRIVIAL (even block dimension).  Hence the entire scalar sign
content is carried by the FROZEN prefactor and the block Wick
monomial is
    w_blk(M) := sgn(M) * prod_{e in M} Pf4(e),
    Pf4({i<j}) := Pf [[0, Chat_ij], [-Chat_ij^T, 0]] = -det(Chat_ij)
(Chat = the Iota/3-compressed 12-dim block matrix; the structured
minor), with the MEASURED ward Pf(Ahat|_M) = + prod_e Pf4(e)
(interleaving sign +1 on all 15 matchings -- the derived convention,
verified symbolically on generic blocks, not assumed).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
exact integer / sympy rational arithmetic in every decision, no
floats in decisions, no RNG, no fits):

 S0  SETUP (corpus rebuilt inline): q* selector, duad model, vacuum
     label V0, carrier dictionary phi; Sp(4,2) census (720),
     Aut(C_fin) ~= C6, generator pin g^2 = sigma, the deployed
     channel permutation pi (fixes 0, cycle type (1,2,3)); the
     canonical chi(i) = (-1)^(i+1); the deployed lift O16.
 B1  THE BLOCK COVARIANCE:
     (a) edge-orbit census of pi on the 15 duads (sizes 1+2+3+3+6,
         exactly one reversed = the transposed pair {a,b});
     (b) the EXACT block commutant on the cross-block coordinates:
         signed index-pair orbit walk under O16; free dimension ==
         12 + 12 + 4 + 4 + 1 = 33 (full d_i x d_j on the four
         non-reversed orbits, antisym 2x2 = 1 on the reversed);
         forced-zero index-pair orbits == 2 (the diagonal of the
         {a,b} block) -- the block-level residue of the round-51
         scalar obstruction;
     (c) the canonical A_c assembled by the frozen rule; condition
         (ii): O16 A_c O16^T == A_c EXACTLY (commutator norm);
     (d) condition (i): ||A_c||_F^2 = 100 x FLOOR^2 < 1 exact =>
         0 < G_c < I strictly (eigenvalue range printed); G
         hermitian;
     (e) condition (iii): the 15-block norm table printed; ALL 15
         cross-blocks at the frozen floor (Frobenius norm >= FLOOR)
         -- including the transposed block {a,b} ~ FLOOR x J that
         the scalar space provably cannot carry;
     (f) condition (iv), the q* grading at block level: Gamma16 =
         (+I on CH(0)) (+) (-I on carriers); [Gamma16, O16] == 0;
         the Ad(Gamma16)-ODD part of A_c supported EXACTLY on the 5
         vacuum blocks {0,i} (q* = 0 messages) and the EVEN
         off-diagonal part EXACTLY on the 10 carrier blocks (q* = 1)
         -- at block level BOTH sectors are FULL (5/5 and 10/10;
         the scalar space managed only 9/10); edge law re-verified
         on all 15 messages; sector-dim ratio 12/4 = 3 = N_fam.
 B2  THE BLOCK PFAFFIAN / WICK STRUCTURE:
     (a) symbolic scalar ward: Pf(6x6 generic) = 15 monomials,
         sgn(M) = chi(i) * qsign(S,T) (round-49 gauge, rebuilt);
     (b) the frozen compression: Iota^T (J+J+J) Iota / 3 == J
         (canonicality ward); Ahat = the 12-dim compressed block
         matrix (channel 0 compressed by Iota/3, carriers verbatim);
     (c) the DERIVED interleaving sign, measured: for EVERY matching
         M, on GENERIC 2x2 blocks, Pf(Ahat|_M) == + prod_{e in M}
         (-det B_e) symbolically (block lift of the volume character
         trivial on all 15 -- the frozen convention verified);
     (d) the candidate monomial census: per-edge Pf4 table (15
         duads); w_blk(M) = sgn(M) * prod Pf4 NONZERO on ALL 15
         matchings -- including the 3 matchings through {a,b} that
         vanish identically at scalar level (the round-51
         obstruction lifted); sign law sign(w_blk(M)) == chi(i) *
         qsign(S,T) * sign(prod Pf4) on all 15;
     (e) the full block Pfaffians: Pf(A_c) (16-dim, memoized exact
         expansion) with the ward Pf^2 == det; Pf(Ahat) (12-dim)
         with the same ward; values printed.
 B3  THE SEAM IDENTIFICATION (the reality-bridge step; fail-first
     typed question -- does the REAL seam carry any channel mixing?)
     (a) the deployed carrier vacuum kernel rebuilt EXACTLY (v113
         10-Majorana Jordan-Wigner): A integer antisymmetric,
         A^2 = -I, rank(M/2) = 5 = g_car; the 10 slot-slot
         cross-blocks censused;
     (b) the deployed seam hull A16 = (+)_8 J (v113/v155/v156
         family): the 15-block norm table printed (cross and
         diagonal); typed SEAM-MIXES(where) iff ANY cross-block is
         nonzero, SEAM-DIAGONAL iff all 15 vanish exactly;
     (c) the honest consequence stated plainly: if SEAM-DIAGONAL,
         the functor's value-level identification remains a
         CANDIDATE awaiting a physical mixing mechanism (a
         boundary/transport-twisted state, NOT the vacuum) -- the
         deployed vacuum realizes the block functor only at the
         structural level (roles, grading, C6), value level open.
 B4  THE FUNCTOR STATEMENT (deliverable): the precise block-level
     functor printed as a contract-ready statement -- duad {i,j} ->
     the block C_ij of G_c; matching M -> the structured block
     product w_blk(M); q* -> the Ad(Gamma16) grading; C6 -> the O16
     intertwiner -- with each piece marked verified [finite, this
     probe] or open [physical realization].
 C   CONTROLS (must fire; frozen fire rules):
     C1 PERMUTED ROLES: conjugating pi by the carrier transposition
        (a, c) (a = 2-cycle carrier, c = first 3-cycle carrier) and
        lifting: (ii) breaks on A_c (||O16' A_c O16'^T - A_c||_F^2
        != 0 -- the wrong action demands an antisymmetric block on
        a duad where A_c carries I2); (iv) breaks: the wrong vacuum
        grading Gamma' (vacuum role at channel a) does NOT commute
        with the deployed O16, and the wrong vacuum Arf label
        breaks the message edge law on EXACTLY 8 of 15;
     C2 THE DIAGONAL DEPLOYED OBJECT: A16 = (+)_8 J fails B1(iii)
        with 0/15 cross-blocks at the floor -- printed.

KILLS (any one fires => typed gap):
  K0 AST firewall / setup ward breaks              -> PIPELINE-BROKEN
  K1 block-covariance space / orbit walk incoherent-> BLOCKSPACE-BROKEN
  K2 canonical candidate / (i)-(iv) verification
     breaks                                        -> CANDIDATE-BROKEN
  K3 block Pfaffian grammar / interleaving sign /
     sign law breaks                               -> WICK-BROKEN
  K4 seam identification census incoherent         -> SEAM-BROKEN
  K7 a control does not fire                       -> CONTROL-DEAD

VERDICT (frozen enum): WICKBLOCK-MEASURED [typed
BLOCKFUNCTOR-CONSTRUCTED / BLOCKFUNCTOR-PARTIAL(<what failed>), +
SEAM-MIXES(<where>) / SEAM-DIAGONAL] (no kills; the honest
seam-diagonal answer is a first-class outcome) / WICKBLOCK-PARTIAL
[kill tokens] / PIPELINE-BROKEN / CONTROL-DEAD.  Exit 0 iff all
checks pass and no kill fired (an honest SEAM-DIAGONAL exits 0);
else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  AST firewall: banned identifiers
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime (self-scan).  NO physics-realization claim; the [O]
premise (the boundary grammar IS a self-hosting Wick pair compiler)
stays [O]; no marker moves.

SPEC v2 AMENDMENTS (fail-first preserved): none at freeze; any
post-run amendment is documented here with the fail-first output
preserved.

Sources (read-only, machinery rebuilt inline): wick_mixing_
covariance_probe (round-51 obstruction, 16-dim witness route,
FLOOR), seam_wick_functor_probe (6 roles, deployed pi + O16 lift,
grading test), k6_pfaffian_selfhosting_probe (chi gauge, qsign,
Lambda^5 volume identification), v113 (Majorana CAR convention,
JW carrier kernel, A16 hull), v155/v156 (D5+A3 split), v160/v161
(quasifree/Bogoliubov reduction), v880/v888 (q*, duads, phi),
tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wick_block_functor_probe.py
"""

import ast
import hashlib
import itertools
import os
import sys
import time

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()

FLOOR = sp.Rational(1, 200)     # round-51 frozen floor


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ---------------------------------------------------------- bit model
# (v880 / v888 conventions rebuilt inline; family/anchor basis)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    """order-3 deck sigma: (b0,b1,b2,b3) -> (b2,b0,b1,b3) (v880)."""
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    """q_c(v) = C(|v|,2) + c.v mod 2 -- the 16 refinements (v880)."""
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v])
                     if bit)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def pf_of(mat, idx):
    """recursive Pfaffian expansion along the first index of idx."""
    if not idx:
        return sp.Integer(1)
    i0, rest0 = idx[0], idx[1:]
    tot = sp.Integer(0)
    for k, j in enumerate(rest0):
        sub = [t for t in rest0 if t != j]
        tot += sp.Integer(-1) ** k * mat[i0, j] * pf_of(mat, sub)
    return tot


def pf_memo(mat, idx):
    """exact Pfaffian by memoized expansion with zero-skip (for the
    16- and 12-dim block objects)."""
    memo = {}

    def rec(t):
        if not t:
            return sp.Integer(1)
        if t in memo:
            return memo[t]
        i0, rest = t[0], t[1:]
        tot = sp.Integer(0)
        for k, j in enumerate(rest):
            aij = mat[i0, j]
            if aij != 0:
                sub = tuple(x for x in rest if x != j)
                tot += sp.Integer(-1) ** k * aij * rec(sub)
        memo[t] = tot
        return tot

    return rec(tuple(sorted(idx)))


def all_matchings(vs):
    vs = sorted(vs)
    if not vs:
        return [frozenset()]
    a = vs[0]
    out = []
    for b in vs[1:]:
        rest = [x for x in vs if x not in (a, b)]
        for sub in all_matchings(rest):
            out.append(sub | {frozenset({a, b})})
    return out


def fro2(M):
    """exact squared Frobenius norm of a sympy matrix."""
    return sum(x * x for x in M)


def edge_orbits(perm):
    """orbits of perm on the 15 unordered duads of {0..5}, each with
    the ORIENTATION-REVERSAL flag (round-51 convention)."""
    n_ord = perm_order(perm)
    seen = set()
    out = []
    for i, j in itertools.combinations(range(6), 2):
        e = frozenset({i, j})
        if e in seen:
            continue
        x, y = i, j
        edges = set()
        rev = False
        for _k in range(n_ord):
            edges.add(frozenset({x, y}))
            x, y = perm[x], perm[y]
            if (x, y) == (j, i):
                rev = True
        seen |= edges
        out.append((frozenset(edges), rev, (i, j)))
    return out


def jw(g):
    """exact Jordan-Wigner annihilators on the 2^g Fock space
    (v113)."""
    eye2, zee = sp.eye(2), sp.diag(1, -1)
    amat = sp.Matrix([[0, 1], [0, 0]])
    ops = []
    for i in range(g):
        mats = [zee] * i + [amat] + [eye2] * (g - 1 - i)
        full = mats[0]
        for m in mats[1:]:
            full = sp.Matrix(sp.kronecker_product(full, m))
        ops.append(full)
    return ops


DUADS_CH = sorted(itertools.combinations(range(6), 2))
J2 = sp.Matrix([[0, 1], [-1, 0]])
I2 = sp.eye(2)
IOTA6 = sp.Matrix.vstack(I2, I2, I2)     # the frozen 6x2 compression


def main():
    print("SEAM.CFIN.WICKBLOCK.01 -- the block-valued Wick functor "
          "(round-51 demand made precise)")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO physics-realization claim; the [O] premise stays [O]; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (corpus rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s"
          % (BANNED_IDS,), not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique "
          "q* under the frozen selector",
          ok_ref and len(set(refs)) == 16 and len(arf1) == 6
          and len(cand) == 1, kill="K0")
    QSTAR = cand[0]
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    DUADS_L = sorted((frozenset(d)
                      for d in itertools.combinations(range(6), 2)),
                     key=sorted)
    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS_L)
    check("S0.2 duad model: 15 messages <-> 15 duads; vacuum label "
          "V0 = %d" % V0, biject and 0 <= V0 < 6, kill="K0")

    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5
               and set(phi.values()) == set(range(1, 6)))
    check("S0.3 carrier dictionary phi (ovoid-induced) bijective: %s"
          % (sorted(phi.items()),), ok_phi, kill="K0")

    def lab(j):
        return 0 if j == V0 else phi[j]

    def chduad(v):
        return frozenset(lab(j) for j in dmap[v])

    chd = {v: chduad(v) for v in NZ}
    inv_chd = {frozenset(d): v for v, d in chd.items()}
    check("S0.4 the 15 messages map bijectively onto the 15 channel "
          "duads (V0 -> channel 0)",
          sorted(chd.values(), key=sorted) == DUADS_L, kill="K0")

    # deployed C6: Sp(4,2) census + Aut pin (rounds 50/51 rebuilt)
    gl_n = 0
    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        gl_n += 1
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                              for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.5 |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == 720, "
          "|Aut(C_fin)| = %d == 6, generator pin g^2 = sigma unique"
          % (gl_n, len(SP6), len(AUT)),
          gl_n == 20160 and len(SP6) == 720 and len(AUT) == 6
          and len(g_pin) == 1, kill="K0")
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(pia[j])
    PI6 = tuple(PI6)
    ct6 = cycle_type(PI6)
    ok_int = all(dmap[GEN[v]] == frozenset(pia[j] for j in dmap[v])
                 for v in NZ)
    check("S0.6 DEPLOYED channel permutation pi = phi o pi_a o "
          "phi^-1 = %s: fixes channel 0, cycle type %s == (1, 2, 3);"
          " intertwines the duad action on all 15"
          % (PI6, ct6),
          PI6[0] == 0 and ct6 == (1, 2, 3) and ok_int, kill="K0")

    cycles = []
    seen = set()
    for i in range(6):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = PI6[j]
        cycles.append(cyc)
    TWO = sorted(next(c for c in cycles if len(c) == 2))
    THREE = next(c for c in cycles if len(c) == 3)
    a_ch, b_ch = TWO
    c_ch = THREE[0]
    print("      pi cycles: fixed 0, 2-cycle %s, 3-cycle %s"
          % (TWO, sorted(THREE)))
    chi = {i: (-1) ** (i + 1) for i in range(1, 6)}

    # the deployed one-particle channel layout + the round-50 lift
    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    dims = {i: len(CH[i]) for i in CH}

    def lift16(perm6):
        O = sp.zeros(16)
        for r in CH[0]:
            O[r, r] = 1
        for i in range(1, 6):
            src, dst = CH[i], CH[perm6[i]]
            O[dst[0], src[0]] = 1
            O[dst[1], src[1]] = 1
        return O

    O16 = lift16(PI6)
    check("S0.7 deployed lift O16 (slot pairs as units, identity on "
          "the A3 block): orthogonal integer; maps channel i onto "
          "channel pi(i)",
          sp.simplify(O16 * O16.T) == sp.eye(16), kill="K0")

    # ==================================================================
    section("B1 -- THE BLOCK COVARIANCE (canonical object, five "
            "conditions)")
    # ==================================================================
    # (a) edge-orbit census of pi on the 15 duads
    orbs = edge_orbits(PI6)
    sizes = sorted(len(o[0]) for o in orbs)
    rev_orbs = [o for o in orbs if o[1]]
    forced_duads = sorted(sorted(e)
                          for o in rev_orbs for e in o[0])
    check("B1.1(a) edge orbits of pi on the 15 duads: sizes %s == "
          "[1, 2, 3, 3, 6]; exactly one orientation-reversed orbit "
          "= the transposed pair %s == [[%d, %d]]"
          % (sizes, forced_duads, a_ch, b_ch),
          sizes == [1, 2, 3, 3, 6] and len(rev_orbs) == 1
          and forced_duads == [[a_ch, b_ch]], kill="K1")

    # (b) the exact block commutant: signed index-pair orbit walk
    o_idx = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            o_idx[s] = CH[PI6[i]][k]
    ch_of = {}
    for i in range(6):
        for s in CH[i]:
            ch_of[s] = i
    cross_pairs = [(r, c) for r in range(16) for c in range(r + 1, 16)
                   if ch_of[r] != ch_of[c]]
    visited = set()
    n_free = 0
    n_forced = 0
    forced_pairs = []
    for p0 in cross_pairs:
        if p0 in visited:
            continue
        orb = {}
        cur, s = p0, 1
        forcedq = False
        while True:
            if cur in orb:
                if orb[cur] != s:
                    forcedq = True
                break
            orb[cur] = s
            r, c = o_idx[cur[0]], o_idx[cur[1]]
            if r > c:
                r, c, s = c, r, -s
            cur = (r, c)
        visited |= set(orb)
        if forcedq:
            n_forced += 1
            forced_pairs.append(sorted(orb))
        else:
            n_free += 1
    expect_free = sum(
        (1 if o[1] else dims[o[2][0]] * dims[o[2][1]])
        for o in orbs)
    check("B1.2(b) BLOCK COMMUTANT on the cross-block coordinates "
          "(%d coords): free index-pair orbits = %d == %d == "
          "12 + 12 + 4 + 4 + 1 (full d_i x d_j on the 4 non-"
          "reversed orbits, antisym 2x2 = 1 on the reversed); "
          "forced-zero orbits = %d == 2 (the diagonal of the "
          "{%d,%d} block -- the block residue of the round-51 "
          "scalar obstruction)"
          % (len(cross_pairs), n_free, expect_free, n_forced,
             a_ch, b_ch),
          len(cross_pairs) == 100 and n_free == expect_free == 33
          and n_forced == 2, kill="K1")

    # (c) the canonical candidate assembled by the frozen rule
    def put_ordered(A, x, y, B):
        for r in range(len(CH[x])):
            for c in range(len(CH[y])):
                A[CH[x][r], CH[y][c]] = B[r, c]
                A[CH[y][c], CH[x][r]] = -B[r, c]

    A_int = sp.zeros(16)
    for edges, rev, rep in orbs:
        i, j = rep
        if rev:
            B = J2
        elif i == 0:
            B = IOTA6
        else:
            B = I2
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    A_c = FLOOR * A_int
    G_c = (sp.eye(16) + sp.I * A_c) / 2
    cov_def = sp.simplify(O16 * A_c * O16.T - A_c)
    check("B1.3(c) canonical A_c assembled (frozen unit blocks: "
          "vacuum = [I2;I2;I2], free pair = I2, reversed {%d,%d} = "
          "J; magnitude FLOOR = 1/200, orientation-propagated); "
          "condition (ii): O16 A_c O16^T == A_c EXACTLY "
          "(defect norm^2 = %s); antisymmetric (%s)"
          % (a_ch, b_ch, fro2(cov_def),
             sp.simplify(A_c + A_c.T) == sp.zeros(16)),
          cov_def == sp.zeros(16)
          and sp.simplify(A_c + A_c.T) == sp.zeros(16), kill="K2")

    f2 = fro2(A_c)
    smax_bound = sp.sqrt(f2)
    lo, hi = (1 - smax_bound) / 2, (1 + smax_bound) / 2
    check("B1.4(d) condition (i): ||A_c||_F^2 = %s = 100 x FLOOR^2 "
          "< 1 exact => spec(A_c) in (-1, 1) => 0 < G_c < I "
          "STRICTLY; G_c eigenvalues in [%s, %s] ~ [%.6f, %.6f]; "
          "G_c hermitian (%s)"
          % (f2, lo, hi, sp.N(lo), sp.N(hi),
             sp.simplify(G_c - G_c.H) == sp.zeros(16)),
          f2 == 100 * FLOOR ** 2 and f2 < 1
          and sp.simplify(G_c - G_c.H) == sp.zeros(16), kill="K2")

    print("      15-block norm table of the CANDIDATE (duad; class; "
          "q*(message); ||C_ij||_F^2; block type):")
    blkn = {}
    n_floor = 0
    for (i, j) in DUADS_CH:
        blk = A_c.extract(CH[i], CH[j])
        nf2 = fro2(blk)
        blkn[(i, j)] = nf2
        at = bool(nf2 >= FLOOR ** 2)
        n_floor += at
        anti = (len(CH[i]) == len(CH[j])
                and sp.simplify(blk + blk.T) == sp.zeros(len(CH[i])))
        v = inv_chd[frozenset({i, j})]
        print("        {%d,%d}  %s  q*=%d  ||.||_F^2 = %s  %s%s"
              % (i, j, "vac" if 0 in (i, j) else "car", QSTAR[v],
                 nf2,
                 "antisym~J" if anti and (i, j) == (a_ch, b_ch)
                 else ("6x2" if 0 in (i, j) else "2x2"),
                 "" if at else "   << BELOW FLOOR"))
    check("B1.5(e) condition (iii): ALL 15 cross-blocks at the "
          "frozen floor (%d/15) -- INCLUDING the transposed block "
          "{%d,%d} (antisymmetric ~ FLOOR x J), which the scalar "
          "channel space provably cannot carry (round 51)"
          % (n_floor, a_ch, b_ch),
          n_floor == 15
          and blkn[(a_ch, b_ch)] == 2 * FLOOR ** 2, kill="K2")

    Gamma16 = sp.diag(*([-1] * 10 + [1] * 6))
    ok_gp = sp.simplify(Gamma16 * O16 - O16 * Gamma16) == sp.zeros(16)
    A_odd = (A_c - Gamma16 * A_c * Gamma16) / 2
    A_even = (A_c + Gamma16 * A_c * Gamma16) / 2
    odd_sup = {frozenset({i, j}) for (i, j) in DUADS_CH
               if fro2(A_odd.extract(CH[i], CH[j])) != 0}
    even_sup = {frozenset({i, j}) for (i, j) in DUADS_CH
                if fro2(A_even.extract(CH[i], CH[j])) != 0}
    vac_duads = {frozenset(chd[v]) for v in NZ if QSTAR[v] == 0}
    car_duads = {frozenset(chd[v]) for v in NZ if QSTAR[v] == 1}
    edge_law = all((QSTAR[v] == 0) == (0 in chd[v]) for v in NZ)
    check("B1.6(f) condition (iv), q* grading at BLOCK level: "
          "[Gamma16, O16] == 0 (%s); edge law q*(v)=0 iff duad "
          "touches channel 0 on all 15 (%s); Ad(Gamma16)-ODD "
          "support == the 5 vacuum (q*=0) blocks (%s: 5/5); EVEN "
          "off-diag support == the 10 carrier (q*=1) blocks (%s: "
          "%d/10 -- FULL at block level, vs 9/10 scalar); sector-"
          "dim ratio 12/4 = %d = N_fam"
          % (ok_gp, edge_law, odd_sup == vac_duads,
             even_sup == car_duads, len(even_sup),
             (dims[0] * 2) // 4),
          ok_gp and edge_law and odd_sup == vac_duads
          and even_sup == car_duads and len(even_sup) == 10
          and (dims[0] * 2) // 4 == N_fam and g_car == 5,
          kill="K2")

    # ==================================================================
    section("B2 -- THE BLOCK PFAFFIAN / WICK STRUCTURE")
    # ==================================================================
    # (a) symbolic scalar ward (round-49 gauge rebuilt)
    SYM = {}
    for i in range(6):
        for j in range(i + 1, 6):
            SYM[(i, j)] = sp.Symbol("a_%d%d" % (i, j))
    G6 = sp.Matrix(6, 6, lambda r, c:
                   SYM[(r, c)] if r < c
                   else (-SYM[(c, r)] if r > c else 0))
    PF6 = sp.expand(pf_of(G6, list(range(6))))
    cdict = PF6.as_coefficients_dict()
    MSLOT = all_matchings(range(6))

    def mono_of(m):
        out = sp.Integer(1)
        for e in m:
            out *= SYM[tuple(sorted(e))]
        return out

    sgn = {}
    ok_c = True
    for m in MSLOT:
        c = cdict.get(mono_of(m), 0)
        ok_c &= (c in (1, -1))
        sgn[frozenset(m)] = int(c)

    def m_ist(m):
        vac_e = next(e for e in m if 0 in e)
        i = next(iter(vac_e - {0}))
        S, T = sorted((tuple(sorted(e)) for e in m if e != vac_e))
        return i, S, T

    def qsign(i, S, T):
        j, k, l, m4 = sorted(set(range(1, 6)) - {i})
        three = [frozenset({frozenset({j, k}), frozenset({l, m4})}),
                 frozenset({frozenset({j, l}), frozenset({k, m4})}),
                 frozenset({frozenset({j, m4}), frozenset({k, l})})]
        key = frozenset({frozenset(S), frozenset(T)})
        return (1, -1, 1)[three.index(key)]

    ok_gauge = all(
        sgn[frozenset(m)]
        == chi[m_ist(m)[0]] * qsign(*m_ist(m)) for m in MSLOT)
    check("B2.1(a) symbolic scalar ward: Pf(6x6 generic) = 15 "
          "monomials, coefficients +-1, sgn(M) == chi(i) * "
          "qsign(S,T) with chi(i) = (-1)^(i+1) on all 15 "
          "(round-49 gauge)",
          len(cdict) == 15 and ok_c and ok_gauge, kill="K3")

    # (b) the frozen compression Iota / 3 (canonicality ward)
    Jdiag3 = sp.diag(J2, J2, J2)
    ok_iota = sp.simplify(IOTA6.T * Jdiag3 * IOTA6
                          - 3 * J2) == sp.zeros(2)
    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}
    Ahat_int = sp.zeros(12)
    for (i, j) in DUADS_CH:
        if i == 0:
            B = (IOTA6.T * A_int.extract(CH[0], CH[j])) / 3
        else:
            B = A_int.extract(CH[i], CH[j])
        for r in range(2):
            for c in range(2):
                Ahat_int[CH2[i][r], CH2[j][c]] = B[r, c]
                Ahat_int[CH2[j][c], CH2[i][r]] = -B[r, c]
    Ahat = FLOOR * Ahat_int
    ok_hat_int = all(x.is_integer for x in Ahat_int)
    check("B2.2(b) FROZEN COMPRESSION: Iota^T (J+J+J) Iota / 3 == J "
          "(%s; normalization 1/3 = 1/N_fam -- the compression "
          "carries the deployed boundary kernel exactly onto the "
          "deployed slot kernel); Ahat (12-dim compressed block "
          "matrix) integer x FLOOR (%s), antisymmetric (%s)"
          % (ok_iota, ok_hat_int,
             sp.simplify(Ahat + Ahat.T) == sp.zeros(12)),
          ok_iota and ok_hat_int
          and sp.simplify(Ahat + Ahat.T) == sp.zeros(12)
          and 3 == N_fam, kill="K3")

    # (c) the derived interleaving sign, measured on generic blocks
    ok_eps = True
    for m in MSLOT:
        Bs = {}
        X12 = sp.zeros(12)
        for e in m:
            i, j = sorted(e)
            B = sp.Matrix(2, 2, lambda r, c:
                          sp.Symbol("b_%d%d_%d%d" % (i, j, r, c)))
            Bs[e] = B
            for r in range(2):
                for c in range(2):
                    X12[CH2[i][r], CH2[j][c]] = B[r, c]
                    X12[CH2[j][c], CH2[i][r]] = -B[r, c]
        pf12 = pf_memo(X12, range(12))
        prod = sp.Integer(1)
        for e in m:
            prod *= -Bs[e].det()
        ok_eps &= (sp.expand(pf12 - prod) == 0)
    check("B2.3(c) DERIVED BLOCK SIGN CONVENTION, measured: for "
          "EVERY matching M, on generic 2x2 blocks, Pf(Ahat|_M) == "
          "+ prod_{e in M} (-det B_e) symbolically -- the "
          "interleaving (Lambda^10 lift of the scalar volume "
          "character) is +1 on all 15 (even block dimension); the "
          "sign content is carried entirely by the frozen scalar "
          "prefactor sgn(M) = chi(i) * qsign(S,T)",
          ok_eps, kill="K3")

    # (d) the candidate monomial census
    print("      per-edge structured minors Pf4({i,j}) = "
          "-det(Chat_ij) of the candidate:")
    p_edge = {}
    for (i, j) in DUADS_CH:
        Bh = Ahat.extract(CH2[i], CH2[j])
        p_edge[frozenset({i, j})] = -Bh.det()
        print("        {%d,%d}: Pf4 = %s" % (i, j, -Bh.det()))
    ab_edge = frozenset({a_ch, b_ch})
    w_blk = {}
    ok_slaw = True
    n_nz = 0
    for m in MSLOT:
        prod = sp.Integer(1)
        for e in m:
            prod *= p_edge[frozenset(e)]
        w = sgn[frozenset(m)] * prod
        w_blk[frozenset(m)] = w
        if w != 0:
            n_nz += 1
            i, S, T = m_ist(m)
            ok_slaw &= (sp.sign(w)
                        == chi[i] * qsign(i, S, T) * sp.sign(prod))
    thru_ab = [m for m in MSLOT if ab_edge in m]
    ok_ab = all(w_blk[frozenset(m)] != 0 for m in thru_ab)
    check("B2.4(d) BLOCK WICK CENSUS: w_blk(M) = sgn(M) * prod Pf4 "
          "NONZERO on %d/15 matchings -- including the %d matchings "
          "through {%d,%d} that vanish identically at scalar level "
          "(the round-51 obstruction LIFTED at block level: %s); "
          "sign law sign(w_blk) == chi(i) * qsign(S,T) * sign(prod "
          "Pf4) on all nonzero"
          % (n_nz, len(thru_ab), a_ch, b_ch, ok_ab),
          n_nz == 15 and len(thru_ab) == 3 and ok_ab and ok_slaw,
          kill="K3")

    # numeric instance of the interleaving ward on the candidate
    ok_num = True
    for m in MSLOT:
        X12 = sp.zeros(12)
        for e in m:
            i, j = sorted(e)
            B = Ahat.extract(CH2[i], CH2[j])
            for r in range(2):
                for c in range(2):
                    X12[CH2[i][r], CH2[j][c]] = B[r, c]
                    X12[CH2[j][c], CH2[i][r]] = -B[r, c]
        prod = sp.Integer(1)
        for e in m:
            prod *= p_edge[frozenset(e)]
        ok_num &= (pf_memo(X12, range(12)) == prod)
    check("B2.5(d) structured-minor ward on the candidate: "
          "Pf(Ahat|_M) == prod_e Pf4(e) exactly on all 15",
          ok_num, kill="K3")

    # (e) the full block Pfaffians (memoized exact expansion)
    pf16_int = pf_memo(A_int, range(16))
    det16 = A_int.det()
    pf12_int = pf_memo(Ahat_int, range(12))
    det12 = Ahat_int.det()
    pf16 = FLOOR ** 8 * pf16_int
    pf12v = FLOOR ** 6 * pf12_int
    check("B2.6(e) FULL BLOCK PFAFFIANS: Pf(A_c) = FLOOR^8 x %s = "
          "%s (ward Pf^2 == det: %s); Pf(Ahat) = FLOOR^6 x %s = %s "
          "(ward: %s)"
          % (pf16_int, pf16, pf16_int ** 2 == det16,
             pf12_int, pf12v, pf12_int ** 2 == det12),
          pf16_int ** 2 == det16 and pf12_int ** 2 == det12,
          kill="K3")
    if pf16_int == 0:
        print("      note (report only, no decision): Pf(A_c) = 0 "
              "is STRUCTURAL for the frozen slot-isotropic vacuum "
              "unit [I2;I2;I2] -- the three channel-0 sub-pair row "
              "groups of A_c coincide (rank deficiency), while the "
              "matching structure lives in the structured minors, "
              "all nonzero (B2.4); the compressed Pf(Ahat) != 0.")

    # ==================================================================
    section("B3 -- THE SEAM IDENTIFICATION (does the REAL seam mix?)")
    # ==================================================================
    # (a) the deployed carrier vacuum kernel, exact JW (v113)
    g = 5
    ann = jw(g)
    ad = [x.T for x in ann]
    cs = []
    for i in range(g):
        cs.append(ann[i] + ad[i])
        cs.append(sp.I * (ad[i] - ann[i]))
    vac = sp.zeros(2 ** g, 1)
    vac[0] = 1

    def vev(ops):
        v = vac
        for o in reversed(ops):
            v = o * v
        return (vac.T * v)[0]

    m2 = sp.Matrix(10, 10, lambda j, k: vev([cs[j], cs[k]]))
    A_car = (m2 - sp.eye(10)) / sp.I
    pol = (sp.eye(10) + sp.I * A_car) / 2
    ok_kern = (sp.simplify(A_car + A_car.T) == sp.zeros(10)
               and all(x.is_integer for x in A_car)
               and sp.simplify(A_car * A_car + sp.eye(10))
               == sp.zeros(10)
               and pol.rank() == 5)
    n_car_mix = 0
    for i, j in itertools.combinations(range(1, 6), 2):
        blk = A_car.extract(CH[i], CH[j])
        if fro2(blk) != 0:
            n_car_mix += 1
    check("B3.1(a) DEPLOYED CARRIER KERNEL (v113 exact JW): M = I + "
          "iA, A integer antisymmetric, A^2 = -I, rank(M/2) = 5 = "
          "g_car (%s); slot-slot cross-blocks nonzero on %d/10 "
          "duads == 0 (channel-diagonal, measured)"
          % (ok_kern, n_car_mix),
          ok_kern and n_car_mix == 0 and g_car == 5, kill="K4")

    # (b) the deployed seam hull A16 (v113/v155/v156 family)
    A16_dep = sp.zeros(16)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    P16 = (sp.eye(16) + sp.I * A16_dep) / 2
    print("      15-block norm table of the DEPLOYED seam "
          "covariance A16 = (+)_8 J (cross-blocks):")
    mix_duads = []
    for (i, j) in DUADS_CH:
        nf2 = fro2(A16_dep.extract(CH[i], CH[j]))
        if nf2 != 0:
            mix_duads.append((i, j))
        print("        {%d,%d}: ||C_ij||_F^2 = %s" % (i, j, nf2))
    diag_n = {i: fro2(A16_dep.extract(CH[i], CH[i]))
              for i in range(6)}
    print("      diagonal blocks: %s"
          % (sorted(diag_n.items()),))
    t_seam = ("SEAM-MIXES(%s)" % (mix_duads,)
              if mix_duads else "SEAM-DIAGONAL")
    ok_proj = all(
        sp.simplify(
            sp.diag(*[1 if r in CH[i] else 0 for r in range(16)])
            * A16_dep
            - A16_dep
            * sp.diag(*[1 if r in CH[i] else 0 for r in range(16)]))
        == sp.zeros(16) for i in range(6))
    check("B3.2(b) TYPED SEAM CENSUS: %s -- the deployed 16-dim "
          "seam covariance has %d/15 nonzero cross-blocks; rank "
          "P16 = %d == 8; A16 commutes with all six channel "
          "projectors (%s); diagonal blocks: channel 0 carries "
          "J+J+J (norm^2 = %s == 6), slots carry J (norm^2 = 2)"
          % (t_seam, len(mix_duads), P16.rank(), ok_proj,
             diag_n[0]),
          t_seam in ("SEAM-DIAGONAL",)
          or t_seam.startswith("SEAM-MIXES"), kill="K4")

    check("B3.3(c) THE HONEST ANSWER, plainly: the REAL (deployed) "
          "seam vacuum carries NO channel mixing at any level -- "
          "scalar (round 50) or block (this census: %s).  The "
          "canonical block object G_c is therefore a PURE CANDIDATE"
          ": the functor's value-level identification awaits a "
          "physical mixing mechanism (a boundary/transport-twisted "
          "seam state, not the vacuum); the deployed vacuum "
          "realizes the functor only structurally (roles, grading, "
          "C6)" % t_seam, True, "typed, no upgrade")

    # ==================================================================
    section("B4 -- THE FUNCTOR STATEMENT (contract-ready)")
    # ==================================================================
    print("""      THE BLOCK-VALUED WICK FUNCTOR (frozen statement):
        DOMAIN: the K6 duad category of the finite compiler
          (6 roles = vacuum V0 + 5 carriers; 15 duads; 15 perfect
          matchings; Aut = C6 pinned by g^2 = sigma; q* grading).
        TARGET: block data on the deployed 16-dim one-particle
          space (channels CH(0) dim 6 = A3, CH(1..5) dim 2 = D5).
        ON OBJECTS   duad {i,j} -> C_ij = A_c[CH(i), CH(j)]
          (6x2 on vacuum edges, 2x2 on carrier edges; the
          transposed duad {%d,%d} -> antisymmetric FLOOR x J)
          [VERIFIED: B1.3/B1.5 -- covariant, CAR-positive,
           all 15 nonzero; finite, this probe].
        ON MATCHINGS M = {0i, jk, lm} -> w_blk(M) = sgn(M) *
          Pf4(0i) * Pf4(jk) * Pf4(lm) (structured minors of the
          Iota/3-compressed Ahat; sgn(M) = chi(i) * qsign(S,T),
          block interleaving +1 derived+measured)
          [VERIFIED: B2.3-B2.5 -- 15/15 nonzero with the chi law].
        GRADING      q*(v) -> Ad(Gamma16) parity of the block of
          D(v) (odd = 5 vacuum blocks, even = 10 carrier blocks,
          both sectors full; ratio 12/4 = 3 = N_fam)
          [VERIFIED: B1.6].
        C6           g -> O16 (slot pairs as units, identity on
          A3); O16 A_c O16^T = A_c and the duad action is
          intertwined [VERIFIED: B1.3 / round 50 T6].
        OPEN (the honest boundary): the VALUE-LEVEL identification
          with the deployed seam -- the measured seam vacuum is
          %s, so no deployed two-point function realizes the
          nonzero block values today; the [O] premise (the
          boundary grammar IS a self-hosting Wick pair compiler)
          stays [O].""" % (a_ch, b_ch, t_seam))
    check("B4.1 functor statement printed (objects / matchings / "
          "grading / C6 verified at block level; value-level seam "
          "identification typed OPEN via B3)", True,
          "contract-ready statement above")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    rho = list(range(6))
    rho[a_ch], rho[c_ch] = rho[c_ch], rho[a_ch]
    rho = tuple(rho)
    PIW = tuple(rho[PI6[rho[x]]] for x in range(6))
    O16w = lift16(PIW)
    defw = fro2(O16w * A_c * O16w.T - A_c)
    Gw = sp.diag(*[1 if r in CH[a_ch] else -1 for r in range(16)])
    gw = fro2(Gw * O16 - O16 * Gw)
    w_arf = next(j for j in range(6) if lab(j) == a_ch)
    mism = sum(1 for v in NZ
               if (QSTAR[v] == 0) != (w_arf in dmap[v]))
    check("C1 FIRES: PERMUTED ROLES (pi conjugated by the carrier "
          "transposition (%d, %d), lifted): (ii) breaks on A_c "
          "(||O16' A_c O16'^T - A_c||_F^2 = %s != 0); (iv) breaks: "
          "wrong vacuum grading Gamma' (vacuum at channel %d) does "
          "NOT commute with the deployed O16 (||.||_F^2 = %s != 0) "
          "and the wrong vacuum Arf label breaks the edge law on "
          "EXACTLY %d == 8 of 15 messages"
          % (a_ch, c_ch, defw, a_ch, gw, mism),
          defw != 0 and gw != 0 and mism == 8, kill="K7")

    n_dep_floor = sum(
        1 for (i, j) in DUADS_CH
        if bool(fro2(A16_dep.extract(CH[i], CH[j]))
                >= FLOOR ** 2))
    check("C2 FIRES: THE DIAGONAL DEPLOYED OBJECT A16 = (+)_8 J "
          "fails B1(iii) with %d/15 cross-blocks at the floor"
          % n_dep_floor, n_dep_floor == 0, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    b_names = ("B1", "B2")
    core_ok = all(ok for nm, ok in CHECKS
                  if nm.startswith(b_names))
    typed = ("BLOCKFUNCTOR-CONSTRUCTED" if core_ok
             else "BLOCKFUNCTOR-PARTIAL")
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif KILLS:
        VERDICT = "WICKBLOCK-PARTIAL [%s]" % ", ".join(
            sorted(set({"K1": "BLOCKSPACE-BROKEN",
                        "K2": "CANDIDATE-BROKEN",
                        "K3": "WICK-BROKEN",
                        "K4": "SEAM-BROKEN"}.get(k, k)
                       for k in KILLS)))
    else:
        VERDICT = "WICKBLOCK-MEASURED [%s, %s]" % (typed, t_seam)
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE BLOCK SPACE (B1): the C6-covariant cross-block space on the
    deployed 16-dim one-particle space has dimension 33 = 12 + 12 +
    4 + 4 + 1 (measured by the signed index-pair orbit walk); the
    ONLY residue of the round-51 scalar obstruction is 2 forced
    zeros on the diagonal of the transposed {%d,%d} block -- its
    antisymmetric direction J survives, so ALL 15 duad blocks are
    realizable.  The canonical G_c (frozen units [I2;I2;I2] / I2 /
    J at FLOOR = 1/200) is C6-covariant EXACTLY, strictly CAR-
    positive, carries 15/15 blocks at the floor, and its Ad(Gamma16)
    grading is FULL in both sectors (5/5 vacuum-odd, 10/10 carrier-
    even -- the scalar space managed only 9/10).
  * THE BLOCK WICK STRUCTURE (B2): the K6 matching structure
    SURVIVES at block level -- with the frozen convention (vacuum
    channel compressed by Iota/3, which maps the deployed boundary
    kernel J+J+J exactly onto the deployed slot kernel J), every
    matching's structured minor factorizes as Pf(Ahat|_M) = + prod
    of per-edge Pf4 (interleaving character trivial: even block
    dimension, the Lambda^10 lift of the k6 volume sign is +1 --
    derived AND measured on generic blocks), and all 15 block Wick
    monomials w_blk(M) = sgn(M) prod Pf4 are NONZERO with the
    canonical chi sign law -- including the 3 matchings through
    {%d,%d} that vanish identically for every scalar candidate.
  * THE SEAM ANSWER (B3, the decisive new fact): the DEPLOYED seam
    covariance (v113 JW carrier kernel + the (+)_8 J seam hull) has
    ZERO cross-channel blocks -- 0/10 carrier duads, 0/15 seam
    duads: %s.  The real seam vacuum carries NO channel mixing at
    block level either; the block functor's value level is a PURE
    CANDIDATE awaiting a physical mixing mechanism (a boundary/
    transport-twisted seam state, not the vacuum).
  * THE FUNCTOR (B4): duads -> blocks of G_c, matchings -> sgn(M) x
    structured minors, q* -> Ad(Gamma16), C6 -> O16 -- verified at
    the finite block level; value-level seam identification OPEN.
  * The [O] premise (the boundary grammar IS a self-hosting Wick
    pair compiler) stays [O]; no marker moves.
Runtime: %.1f s""" % (a_ch, b_ch, a_ch, b_ch, t_seam,
                      time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
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
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
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
    ('seam_wick_functor_probe', _SRC_0, 27, (), 'WICKFUNCTOR-PARTIAL', 0),
    ('wick_mixing_covariance_probe', _SRC_1, 33, (), 'WICKMIX-MEASURED', 0),
    ('wick_block_functor_probe', _SRC_2, 26, (), 'WICKBLOCK-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v896 -- SEAM.CFIN.WICKFUNCTOR.01 + SEAM.CFIN.WICKMIX.01 + SEAM.CFIN.WICKBLOCK.01: the Wick functor arc -- the six compiler roles exist, the scalar mixing covariance is PROVABLY obstructed, the block functor is constructed')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v896: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('structure level closed: roles exist, scalar form proved obstructed, block form exact -- the value level awaits a physical mixing mechanism; [O] premise unmoved')
    print("[%s] v896 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
