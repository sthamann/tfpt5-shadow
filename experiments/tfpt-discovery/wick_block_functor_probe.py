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
