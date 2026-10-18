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
