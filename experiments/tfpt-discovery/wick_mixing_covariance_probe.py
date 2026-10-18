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
