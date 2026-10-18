#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rp_twisted_involution_census_probe -- SEAM.CFIN.TWISTED.RP.01
(EXPLORATION ONLY, experiments/; round 59, 2026-08-10: the complete
census of TWISTED OS reflections Theta_g = U_g o theta on the v898
family -- can twisting by the compiler's own C6 transport rescue
reflection positivity WITH strict mixing t > 0?)

THE QUESTION.  seam_state_derivation_probe (round 58, 25/25)
measured: STRICT RP forces t = 0 under BOTH deployable plain
spatial reflections (sheet swap theta_S = the 16-dim lift of the
v440 collar I (x) sigma_x, and the orientation-reversed 2-cycle
theta_abT), and under theta_abT this is an incompatibility THEOREM
(OS positivity <=> a_J = 0 <=> the v898 mixing gate G3 fails).
Those were PLAIN reflections.  The compiler carries a C6
automorphism (the deployed O16 lift of pi, cycle type (1,2,3)) and
a twist class (the v519 eta), so the right remaining question is
TWISTED OS positivity <U_g theta(F), F> >= 0: enumerate ALL
C6-compatible involutive candidates Theta_g = U_g o theta over both
deployable base reflections and all character twists, and ask which
survivors admit RP with STRICT mixing t > 0.

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-10): seam_state_derivation_probe tested exactly the two
PLAIN candidates (g = identity); v519 deploys the RP Gram + forced
twist eta = +i for the free NS vacuum only; v898 typed
RP-THETA-OPEN and tested only the particle-hole Theta_0; NOTHING
in the corpus composes the C6 transport U_g with a spatial theta
and asks the twisted-OS question on the v898 family.  That is
exactly this probe.

SMOKE-RUN DISCLOSURE (2026-08-10, one declared smoke round before
freezing; ALL frozen claims below were shaped by it -- recording
the surprises, including two DEAD pre-derivations, is part of the
method):
 (i)   the involution gate lands exactly where the group theory
       says: q_comb = img^k o r_base squares to img^(2k) (the base
       maps commute with the lift up to the 2-cycle), so Theta_g^2
       = 1 iff 3 | k, i.e. k in {0, 3} -- 16 of 48 (base, k, eta)
       candidates are involutive, and the involution gate is
       eta-INDEPENDENT (|eta| = 1 drops out of Theta^2, derived and
       measured);
 (ii)  the g^3-twisted sheet swap theta_S3 = U_{g^3} o theta_S
       (sheet swap COMBINED with the a<->b channel exchange) is
       Hermitian at the bare point for eta = +-i, like the plain
       one -- but its 1p Gram is INDEFINITE already at the bare
       point, lam_min = -0.4621 for +i and -i ALIKE (the twist
       makes the eta sign degenerate; -0.4621 is exactly the
       negative branch the plain reflection shows at eta = -i):
       the channel exchange moves the 1p Gram off the PSD cone
       entirely -- twisting by transport does NOT rescue RP, it
       kills it already at t = 0;
 (iii) DEAD GUESS, disclosed: the plan expected the g^3-twisted
       2-cycle theta_abT3 (SIDE-FIXING: g^3 undoes the a<->b
       exchange of the base, leaving an intra-pair twist within
       CH(a) and CH(b)) to be a Hermitian within-side form showing
       the a_J obstruction; the smoke run REJECTS it before any
       scan -- its Gram Hermiticity is broken at the bare point
       for EVERY eta (defect 0.92 at eta = +-1, 2.0 at eta = +-i):
       a side-fixing composition is not an OS candidate at all;
 (iv)  NO survivor admits strict RP with t > 0: the plain pairs
       (k = 0, eta = +i) reproduce round 58 exactly (t = 0 passes,
       every t > 0 fails); (abT, k=0, eta=-i) ALSO passes at t = 0
       (the bare 2-cycle Gram is marginal 0, so both eta signs sit
       on the cone boundary) and fails every t > 0; the k = 3
       candidates fail everywhere ((S,3): bare-indefinite;
       (abT,3): bare-rejected);
 (v)   DEAD GUESS, disclosed: the plan expected lam_max of the
       deployed-point 1p Gram >= 0.5; measured 0.4973 -- the
       scalar-character collapse bars are set at 0.45.

CONVENTIONS (v898 / round 58, rebuilt inline; READ-ONLY import of
tfpt_constants): 16-dim Majorana one-particle space; boundary
channel CH(0) = indices 10..15, carrier channels CH(i) =
{2(i-1), 2(i-1)+1}; KMS covariance A = -tan(beta h / 2) with
h(u, t) = -(u A16_dep + t A_int); Wick by Pfaffian recursion; RP
Gram M_ab = omega(Theta(e_a) e_b) over half-side monomial bases
(v519 form: antilinear reversal, spin signs, twist eta^deg),
sector-typed (1p; even deg <= 2).  TWISTED CANDIDATES: Theta_g =
U_g o theta with U_g = the deployed O16^k lift, k = 0..5, base
theta in {theta_S, theta_abT}, twist eta in {+1, -1, +i, -i} --
the candidate set is COMPLETE at this finite size: C6 = <g> is
cyclic of order 6 (generator pinned uniquely by g^2 = sigma in
Aut(C_fin), |Aut| = 6, re-verified), the base census is the
round-58 measurement (the only two deployable spatial reflections;
untwisted 2-cycle and Gamma16 excluded there), and the character
axis is exhausted by the degree twist eta^deg over the 4th roots
of unity plus the scalar characters, which collapse (claim E1.2).
STRICT RP at a point = Gram Hermitian (relative defect <= ZTOL =
1e-10) AND PSD (lam_min >= -NZ_FLOOR = 1e-8) in BOTH sectors;
definite fail = defect >= 1e-8 or lam_min <= -1e-8; the open band
fires the ambiguity kill.  NUMERICAL PROTOCOL (exploration grade,
declared): numpy float64; structural wiring exact integer; frozen
thresholds NZ_FLOOR = 1e-8, ZTOL = 1e-10.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 E1  ENUMERATION (provably complete at this finite size).
     (a) C6 rebuilt: |Aut| = 6, generator unique with g^2 = sigma,
         O16^k for k = 0..5 are 6 DISTINCT orthogonal lifts, each
         an exact symmetry of every scanned KMS state (max
         invariance defect <= ZTOL over the scan grid) -- U_g is
         deployable transport;
     (b) SCALAR-CHARACTER COLLAPSE (measured at the deployed
         point, 1p sector, plain theta_S): a degree-independent
         scalar chi multiplies the Gram globally; chi = -1 negates
         it (lam_min(chi M) = -lam_max(M) <= -0.45; measured
         lam_max = 0.4973), chi = +i makes it non-Hermitian
         (defect >= 0.5).  The character axis reduces to the
         degree twist eta^deg, eta in the 4th roots of unity.
 E2  INVOLUTION GATE (the Theta^2 = 1 census).
     (a) Theta_g^2 = 1 on ALL deg-1 and deg-2 monomials (240
         monomials; complete: Theta is an antilinear
         anti-homomorphism determined by its 1p action, so
         Theta^2 = 1 on generators + deg-2 sign bookkeeping
         decides the full algebra) iff k in {0, 3}, for BOTH
         bases, INDEPENDENT of eta: 16 of 48 candidates are
         involutive, 32 are rejected;
     (b) the derived law: q_comb^2 = img^(2k) on indices (the
         3-cycle of pi forces 3 | k) -- verified index-wise.
 E3  SURVIVOR TYPING (measured table, printed).
     (a) all 16 survivors are CAR-compatible (orthogonal index
         permutations) and grading-preserving (carrier/boundary
         split fixed setwise);
     (b) side typing: the 8 theta_S-based survivors EXCHANGE the
         sheets; the 4 theta_abT-based k = 0 survivors exchange
         CH(a) <-> CH(b); the 4 theta_abT-based k = 3 survivors
         are SIDE-FIXING (q maps CH(a) to CH(a) with intra-pair
         twist) -- typed, kept in the census as within-side forms;
     (c) BW/KMS compatibility at (u=1, t=1/8, beta=2pi), measured
         as Q h Q^T vs +-h: NO candidate is a BW symmetry or
         antisymmetry of the deployed h (min defect >= 0.2) -- the
         OS Gram criterion, not the BW dictionary, decides (typed
         reading, as in round 58);
     (d) bare-point admissibility (frozen rule: a survivor enters
         the decisive scan iff BOTH sector Hermiticity defects <=
         ZTOL at (1, 0, 1)): the admissible slices are eta = +-i
         for (S, k=0), (S, k=3) and (abT, k=0); the side-fixing
         (abT, k=3) is REJECTED for every eta (defect >= 0.9);
         eta = +-1 rejected everywhere (defect >= 0.9): exactly 6
         survivors enter the scan.
 E4  THE DECISIVE SCAN (strict RP with t > 0?).
     (a) scan grid t in {0, 1/32, 1/16, 1/8, 1/4} x beta in {1/2,
         1, 2, 2pi} at u = 1 for all 6 admissible survivors;
         frozen verdict: ZERO survivors admit strict RP at ANY
         t > 0 grid point -- TWISTED-RP-EXCLUSIONARY;
     (b) the anatomy: (theta_S, k=0, eta=+i) passes exactly at
         t = 0 (all 4 beta) and fails for every t > 0 (round-58
         regression); (theta_S, k=3, eta=+-i) fails EVERYWHERE
         including t = 0 (1p lam_min = -0.4621 +- 0.005 at the
         bare point, both eta signs): the U_{g^3} twist is not a
         rescue but a new obstruction; (theta_abT, k=0, eta=+i
         AND eta=-i) pass at t = 0 (marginal cone boundary) and
         fail every t > 0 (the incompatibility theorem);
         (theta_S, k=0, eta=-i) fails everywhere (negative
         branch);
     (c) eta = -i flips the 1p Gram against +i (lam_min(+i) +
         lam_max(-i) = 0 within 1e-9 at the bare point for
         theta_S k=0) -- at most ONE of +-i can carry strict
         positivity per side-exchanging candidate.
 R   REGRESSIONS (round 58, must reproduce).
     R1 plain sheet swap: u_c(t=1/8, beta=1) = t (bisected
        |u_c - t| <= 1e-6); strict deg-2 Hermiticity defect at the
        deployed point 0.0982 +- 0.005;
     R2 plain twisted 2-cycle: odd-sector eigenvalues EXACTLY
        {-|a_J|, +|a_J|} at (1, 1/8, 1) (identity defect <=
        1e-10), a_J >= NZ_FLOOR.
 C   CONTROLS (must fire; frozen fire rules; RNG only here).
     C1 NON-INVOLUTIVE REJECTION: (theta_S, k=1) fails the
        Theta^2 = 1 gate (q^2 = img^2 != id on >= 4 indices) --
        the gate fires;
     C2 eta = +1 breaks Gram Hermiticity at the bare point for
        both plain bases (max defect >= 0.5) -- v519 twist
        regression;
     C3 SEEDED RANDOM PAIRINGS (rng seed 899, 3 draws): random
        perfect matchings as theta break the 1p Gram at the
        deployed point (defect >= 0.5 or lam_min <= -0.1), 3/3;
     C4 AST firewall: banned identifiers.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 enumeration / involution ward breaks        -> ENUM-BROKEN
  K2 a scan/typing ward breaks or ambiguity band -> RPSCAN-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): TWISTEDRP-MEASURED [CENSUS(16/48
involutive, 6 admissible), SELECTION(NONE:
TWISTED-RP-EXCLUSIONARY -- 0 of 6 admissible survivors admit
strict RP at t > 0; the k=3 sheet twist is a NEW bare-point
obstruction, the k=3 2-cycle twist is side-fixing and
bare-rejected)] / PIPELINE-BROKEN / ENUM-BROKEN / RPSCAN-BROKEN /
CONTROL-DEAD.  Exit 0 iff all checks pass and no kill fired;
else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the [O] premise of v898 stays [O];
twisted-OS exclusion is a MEASUREMENT on the candidate family
(these 48 candidates), not a no-go theorem for all conceivable
reflections; no marker moves.  NO RH claim.

SPEC v1 (2026-08-10): frozen after the declared smoke round; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline):
seam_state_derivation_probe (round 58: RP machinery, plain
census, regressions), v898_kms_schur_mixing (family, gates), v519
(RP Gram + forced twist), v424/v426/v440 (BW dictionary, collar
reflection), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/rp_twisted_involution_census_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402  (READ-ONLY)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

NZ_FLOOR = 1e-8            # nonzero decision floor (frozen)
ZTOL = 1e-10               # structural-zero ceiling (frozen)


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
# (v880 / v888 conventions rebuilt inline, byte-parallel to round 58)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v]) if bit)


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


def edge_orbits(perm):
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


DUADS_CH = sorted(itertools.combinations(range(6), 2))


def main():
    print("SEAM.CFIN.TWISTED.RP.01 -- twisted OS reflections "
          "Theta_g = U_g o theta: the complete involution census")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (round 58 rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s" % (BANNED_IDS,),
          not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique q*",
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
    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5 and set(phi.values()) == set(range(1, 6)))

    def lab(j):
        return 0 if j == V0 else phi[j]

    chd = {v: frozenset(lab(j) for j in dmap[v]) for v in NZ}
    SP6 = []
    gl_n = 0
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
    check("S0.2 duad model + Aut pin: |Sp(4,2)| = %d == 720, |Aut| = "
          "%d == 6, generator unique (g^2 = sigma)"
          % (len(SP6), len(AUT)),
          ok_phi and sorted(chd.values(), key=sorted) == DUADS_L
          and gl_n == 20160 and len(SP6) == 720 and len(AUT) == 6
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
    a_ch, b_ch = TWO
    check("S0.3 deployed channel permutation pi = %s, cycle type %s "
          "== (1, 2, 3); 2-cycle {%d, %d}"
          % (PI6, cycle_type(PI6), a_ch, b_ch),
          PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3), kill="K0")

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    CAR_IDX = list(range(10))
    BND_IDX = list(range(10, 16))
    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]

    J2 = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    I2 = np.eye(2, dtype=np.int64)
    IOTA6 = np.vstack([I2, I2, I2])
    orbs = edge_orbits(PI6)

    def put_ordered(A, x, y, B):
        rx, cy = CH[x], CH[y]
        for r in range(len(rx)):
            for c in range(len(cy)):
                A[rx[r], cy[c]] = B[r, c]
                A[cy[c], rx[r]] = -B[r, c]

    A_int = np.zeros((16, 16), dtype=np.int64)
    for edges, rev, rep in orbs:
        i, j = rep
        B = J2 if rev else (IOTA6 if i == 0 else I2)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    okA = (np.array_equal(A_int[np.ix_(img, img)], A_int)
           and np.array_equal(A_int, -A_int.T))
    A16_dep = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    okD = (np.array_equal(A16_dep[np.ix_(img, img)], A16_dep)
           and np.array_equal(A16_dep @ A16_dep,
                              -np.eye(16, dtype=np.int64)))
    check("S0.4 A_int rebuilt (integer, antisymmetric, exactly "
          "covariant); A16_dep = (+)_8 J covariant with A^2 = -I",
          okA and okD, kill="K0")

    Aint_f = A_int.astype(np.float64)
    Adep_f = A16_dep.astype(np.float64)
    I16 = np.eye(16)

    def kms_A(u, t, beta):
        h = -(u * Adep_f + t * Aint_f)
        w, Q = np.linalg.eigh(1j * h)
        f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
        C = (Q * f) @ Q.conj().T
        return (-1j * (2 * C - I16)).real

    def blocks_census(A):
        return {(i, j): float(np.linalg.norm(A[np.ix_(CH[i], CH[j])]))
                for (i, j) in DUADS_CH}

    A18 = kms_A(1.0, 0.125, 1.0)
    h18 = -(Adep_f + 0.125 * Aint_f)
    smax18 = float(np.max(np.abs(np.tanh(
        np.linalg.eigvalsh(1j * h18) / 2.0))))
    bn18 = blocks_census(A18)
    n18 = sum(1 for v in bn18.values() if v >= NZ_FLOOR)
    fz18 = max(abs(A18[CH[a_ch][k], CH[b_ch][k]]) for k in range(2))
    check("S0.5 v898 regression at (u=1, t=1/8, beta=1): smax = "
          "%.6f (0.668 +- 2e-3), 15/15 cross-blocks (%d), forced "
          "zeros < ZTOL (%.1e)" % (smax18, n18, fz18),
          abs(smax18 - 0.668) < 2e-3 and n18 == 15 and fz18 < ZTOL,
          kill="K0")

    # ---------------- RP machinery (v519 form, round-58 port)
    def wick_factory(A):
        W = np.eye(16, dtype=complex) + 1j * A
        memo = {}

        def wick(idx):
            idx = tuple(idx)
            if len(idx) == 0:
                return 1.0 + 0j
            if len(idx) % 2 == 1:
                return 0.0 + 0j
            if idx in memo:
                return memo[idx]
            head, rest = idx[0], idx[1:]
            tot = 0.0 + 0j
            for j, b in enumerate(rest):
                sub = rest[:j] + rest[j + 1:]
                tot += (-1) ** j * W[head, b] * wick(sub)
            memo[idx] = tot
            return tot
        return wick

    def theta_mono(mono, r, s, eta):
        imgs = [r[a] for a in reversed(mono)]
        coeff = eta ** len(mono)
        for a in mono:
            coeff *= s[a]
        lst = list(imgs)
        sign = 1
        for i in range(len(lst)):
            for j in range(len(lst) - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    sign = -sign
        return coeff * sign, tuple(lst)

    def gram(basis, r, s, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis):
            ca, ia = theta_mono(ma, r, s, eta)
            for bi, mb in enumerate(basis):
                M[ai, bi] = ca * wick(tuple(list(ia) + list(mb)))
        return M

    def metrics(M):
        nm = max(float(np.max(np.abs(M))), 1e-300)
        hd = float(np.max(np.abs(M - M.conj().T)) / nm)
        lm = float(np.min(np.linalg.eigvalsh((M + M.conj().T) / 2)))
        return hd, lm

    S_ONE = {k: 1 for k in range(16)}

    r_S = {}
    for i in range(8):
        r_S[2 * i] = 2 * i + 1
        r_S[2 * i + 1] = 2 * i
    P_S = [2 * i for i in range(8)]

    r_abT = {k: k for k in range(16)}
    for k in range(2):
        r_abT[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_abT[CH[b_ch][k]] = CH[a_ch][1 - k]
    P_ab = list(CH[a_ch])

    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]
    B1_ab = [(a,) for a in P_ab]
    B2_ab = [(), tuple(P_ab)]

    BASES = {"S": (r_S, B1_S, B2_S),
             "abT": (r_abT, B1_ab, B2_ab)}
    ETAS = [("+1", 1.0 + 0j), ("-1", -1.0 + 0j),
            ("+i", 1j), ("-i", -1j)]

    # powers of the index lift img
    IMGP = [list(range(16))]
    for _k in range(5):
        IMGP.append([img[x] for x in IMGP[-1]])

    def r_comb(base_r, k):
        return {a: IMGP[k][base_r[a]] for a in range(16)}

    # ==================================================================
    section("E1 -- enumeration: C6 lifts + scalar-character collapse")
    # ==================================================================
    distinct = len({tuple(IMGP[k]) for k in range(6)})
    inv_def = 0.0
    T_SCAN = [0.0, 1.0 / 32, 1.0 / 16, 0.125, 0.25]
    B_SCAN = [0.5, 1.0, 2.0, 2 * math.pi]
    STATES = {}
    for t in T_SCAN:
        for beta in B_SCAN:
            STATES[(t, beta)] = kms_A(1.0, t, beta)
    for (t, beta), A in STATES.items():
        for k in (1, 3):
            P = IMGP[k]
            inv_def = max(inv_def, float(np.max(np.abs(
                A[np.ix_(P, P)] - A))))
    check("E1.1 C6 enumerated: 6 distinct orthogonal lifts O16^k "
          "(%d); every scanned KMS state is U_g-invariant (max "
          "defect %.1e <= ZTOL); candidate set = 2 bases x 6 "
          "powers x 4 twists = 48 (complete at this finite size)"
          % (distinct, inv_def),
          distinct == 6 and inv_def <= ZTOL, kill="K1")

    wk18 = wick_factory(A18)
    M1_plain = gram(B1_S, r_S, S_ONE, 1j, wk18)
    lam_max_plain = float(np.max(np.linalg.eigvalsh(
        (M1_plain + M1_plain.conj().T) / 2)))
    hd_neg, lm_neg = metrics(-M1_plain)
    hd_chi_i, _lm = metrics(1j * M1_plain)
    check("E1.2 SCALAR-CHARACTER COLLAPSE: chi = -1 negates the 1p "
          "Gram (lam_min = %.4f <= -0.45 vs lam_max %.4f); chi = +i "
          "breaks Hermiticity (defect %.3f >= 0.5): the character "
          "axis reduces to the degree twist eta^deg"
          % (lm_neg, lam_max_plain, hd_chi_i),
          lm_neg <= -0.45 and hd_chi_i >= 0.5
          and lam_max_plain >= 0.45, kill="K1")

    # ==================================================================
    section("E2 -- the involution gate Theta_g^2 = 1 (48 candidates)")
    # ==================================================================
    MONOS = ([(a,) for a in range(16)]
             + [tuple(c) for c in itertools.combinations(range(16), 2)])

    def involutive(r, eta):
        for m in MONOS:
            c1, m1 = theta_mono(m, r, S_ONE, eta)
            c2, m2 = theta_mono(m1, r, S_ONE, eta)
            if m2 != m or abs(np.conj(c1) * c2 - 1.0) > 1e-12:
                return False
        return True

    surv = []
    n_inv, n_rej = 0, 0
    eta_indep = True
    for bname, (br, b1, b2) in BASES.items():
        for k in range(6):
            rc = r_comb(br, k)
            invs = [involutive(rc, ev) for _en, ev in ETAS]
            eta_indep &= (len(set(invs)) == 1)
            for (en, ev), iv in zip(ETAS, invs):
                if iv:
                    n_inv += 1
                    surv.append((bname, k, en, ev, rc, b1, b2))
                else:
                    n_rej += 1
    ks_ok = all(k in (0, 3) for (_b, k, _en, _ev, _r, _1, _2) in surv)
    law_ok = True
    for bname, (br, _1, _2) in BASES.items():
        for k in range(6):
            rc = r_comb(br, k)
            q2 = {a: rc[rc[a]] for a in range(16)}
            expect = {a: IMGP[(2 * k) % 6][a] for a in range(16)}
            if bname == "abT" and k in (0, 3):
                expect = {a: a for a in range(16)}
            if bname == "S":
                law_ok &= (q2 == expect)
    check("E2.1 INVOLUTION CENSUS: %d/48 involutive (%d rejected); "
          "involutive iff k in {0, 3} (%s); eta-INDEPENDENT (%s); "
          "sheet-swap law q^2 = img^(2k) verified index-wise (%s)"
          % (n_inv, n_rej, ks_ok, eta_indep, law_ok),
          n_inv == 16 and n_rej == 32 and ks_ok and eta_indep
          and law_ok, kill="K1")

    # ==================================================================
    section("E3 -- survivor typing (CAR / grading / sides / BW / "
            "bare point)")
    # ==================================================================
    ok_car, ok_grad = True, True
    side_rows = []
    for (bname, k, en, ev, rc, b1, b2) in surv:
        vals = sorted(rc.values())
        ok_car &= (vals == list(range(16)))
        ok_grad &= all((rc[a] < 10) == (a < 10) for a in range(16))
        if bname == "S":
            side = ("EXCHANGES-SHEETS"
                    if all((rc[a] % 2) != (a % 2) for a in range(16))
                    else "SIDE-FIXING")
        else:
            imgs_a = sorted(rc[a] for a in CH[a_ch])
            side = ("EXCHANGES-AB" if imgs_a == sorted(CH[b_ch])
                    else ("SIDE-FIXING" if imgs_a == sorted(CH[a_ch])
                          else "OTHER"))
        side_rows.append((bname, k, en, side))
    sides_S = {s for (b, k, e, s) in side_rows if b == "S"}
    sides_ab0 = {s for (b, k, e, s) in side_rows
                 if b == "abT" and k == 0}
    sides_ab3 = {s for (b, k, e, s) in side_rows
                 if b == "abT" and k == 3}
    for (bname, k, en, side) in side_rows:
        if en == "+i":
            print("      base=%-3s k=%d : %s" % (bname, k, side))
    check("E3.1 all 16 survivors CAR-compatible (index bijections) "
          "and grading-preserving; sides: theta_S-based EXCHANGE "
          "SHEETS (%s), theta_abT k=0 EXCHANGES a<->b (%s), "
          "theta_abT k=3 is SIDE-FIXING (%s)"
          % (sides_S, sides_ab0, sides_ab3),
          ok_car and ok_grad and sides_S == {"EXCHANGES-SHEETS"}
          and sides_ab0 == {"EXCHANGES-AB"}
          and sides_ab3 == {"SIDE-FIXING"}, kill="K2")

    h2p = -(Adep_f + 0.125 * Aint_f)
    bw_min = 1e9
    for (bname, k, en, ev, rc, b1, b2) in surv:
        if en != "+i":
            continue
        P = [rc[a] for a in range(16)]
        hP = h2p[np.ix_(P, P)]
        d_sym = float(np.linalg.norm(hP - h2p)
                      / np.linalg.norm(h2p))
        d_anti = float(np.linalg.norm(hP + h2p)
                       / np.linalg.norm(h2p))
        bw_min = min(bw_min, d_sym, d_anti)
        print("      BW at (1, 1/8, 2pi): base=%-3s k=%d  "
              "|QhQ-h|/|h| = %.4f  |QhQ+h|/|h| = %.4f"
              % (bname, k, d_sym, d_anti))
    check("E3.2 BW/KMS dictionary at (u=1, t=1/8, beta=2pi): NO "
          "candidate is a BW (anti)symmetry of the deployed h (min "
          "defect %.4f >= 0.2) -- the OS Gram, not the BW "
          "dictionary, decides (typed reading)" % bw_min,
          bw_min >= 0.2, kill="K2")

    A0 = STATES[(0.0, 1.0)]
    wk0 = wick_factory(A0)
    adm = []
    bare_rows = []
    for (bname, k, en, ev, rc, b1, b2) in surv:
        M1 = gram(b1, rc, S_ONE, ev, wk0)
        M2 = gram(b2, rc, S_ONE, ev, wk0)
        hd1, lm1 = metrics(M1)
        hd2, lm2 = metrics(M2)
        herm = max(hd1, hd2) <= ZTOL
        bare_rows.append((bname, k, en, hd1, hd2, lm1, lm2, herm))
        if herm:
            adm.append((bname, k, en, ev, rc, b1, b2, lm1, lm2))
    for (bname, k, en, hd1, hd2, lm1, lm2, herm) in bare_rows:
        print("      bare (1,0,1): base=%-3s k=%d eta=%-2s  "
              "hd=(%.1e, %.1e)  lam_min=(%+.4f, %+.4f)  %s"
              % (bname, k, en, hd1, hd2, lm1, lm2,
                 "ADMISSIBLE" if herm else "rejected"))
    herm_etas = {(b, k): sorted(en for (bb, kk, en, *_r) in bare_rows
                                if (bb, kk) == (b, k) and _r[-1])
                 for (b, k) in {(b, k) for (b, k, *_x) in bare_rows}}
    EXP_ETAS = {("S", 0): ["+i", "-i"], ("S", 3): ["+i", "-i"],
                ("abT", 0): ["+i", "-i"], ("abT", 3): []}
    ab3_hd = min(max(hd1, hd2) for (bb, kk, en, hd1, hd2, *_x)
                 in bare_rows if (bb, kk) == ("abT", 3))
    check("E3.3 BARE-POINT ADMISSIBILITY: admissible slices are "
          "eta = +-i for (S,0), (S,3), (abT,0); the SIDE-FIXING "
          "(abT,3) is rejected for EVERY eta (min defect %.2f >= "
          "0.9 -- a side-fixing composition is not an OS "
          "candidate); eta = +-1 rejected everywhere; %d "
          "survivors enter the decisive scan"
          % (ab3_hd, len(adm)),
          {k_: sorted(v) for k_, v in herm_etas.items()} ==
          {k_: sorted(v) for k_, v in EXP_ETAS.items()}
          and ab3_hd >= 0.9 and len(adm) == 6, kill="K2")

    # ==================================================================
    section("E4 -- THE DECISIVE SCAN: strict RP with t > 0?")
    # ==================================================================
    WICKS = {}
    for key, A in STATES.items():
        WICKS[key] = wick_factory(A)

    results = {}
    ambig = []
    for (bname, k, en, ev, rc, b1, b2, _l1, _l2) in adm:
        row = {}
        for (t, beta), wk in WICKS.items():
            M1 = gram(b1, rc, S_ONE, ev, wk)
            M2 = gram(b2, rc, S_ONE, ev, wk)
            hd1, lm1 = metrics(M1)
            hd2, lm2 = metrics(M2)
            hd = max(hd1, hd2)
            lm = min(lm1, lm2)
            if hd <= ZTOL and lm >= -NZ_FLOOR:
                st = "P"
            elif hd >= NZ_FLOOR or lm <= -NZ_FLOOR:
                st = "F"
            else:
                st = "?"
                ambig.append((bname, k, en, t, beta, hd, lm))
            row[(t, beta)] = (st, hd, lm)
        results[(bname, k, en)] = row

    admit_tpos = []
    for key, row in sorted(results.items()):
        line = []
        for t in T_SCAN:
            for beta in B_SCAN:
                line.append(row[(t, beta)][0])
        tp = any(row[(t, beta)][0] == "P"
                 for t in T_SCAN if t > 0 for beta in B_SCAN)
        if tp:
            admit_tpos.append(key)
        print("      %-18s  grid[t x beta] = %s  %s"
              % ("(%s, k=%d, %s)" % key, "".join(line),
                 "ADMITS t>0" if tp else "no t>0"))
    check("E4.1 THE ANSWER: %d admissible survivors scanned on 5 t "
          "x 4 beta; ZERO survivors admit strict RP at any t > 0 "
          "point (admitting set: %s); no ambiguity band fired (%d)"
          % (len(adm), admit_tpos or "EMPTY", len(ambig)),
          len(admit_tpos) == 0 and not ambig, kill="K2")

    r0 = results[("S", 0, "+i")]
    ok_S0 = (all(r0[(0.0, b)][0] == "P" for b in B_SCAN)
             and all(r0[(t, b)][0] == "F"
                     for t in T_SCAN if t > 0 for b in B_SCAN))
    ok_S0m = all(results[("S", 0, "-i")][(t, b)][0] == "F"
                 for t in T_SCAN for b in B_SCAN)
    lm_S3 = []
    ok_S3 = True
    for en in ("+i", "-i"):
        rS3 = results[("S", 3, en)]
        lm_S3.append(rS3[(0.0, 1.0)][2])
        ok_S3 &= all(rS3[(t, b)][0] == "F"
                     for t in T_SCAN for b in B_SCAN)
    ok_S3 &= all(abs(l + 0.4621) <= 5e-3 for l in lm_S3)
    ok_ab = True
    for en in ("+i", "-i"):
        rab = results[("abT", 0, en)]
        ok_ab &= (all(rab[(0.0, b)][0] == "P" for b in B_SCAN)
                  and all(rab[(t, b)][0] == "F"
                          for t in T_SCAN if t > 0 for b in B_SCAN))
    ok_ab3_gone = not any(key[:2] == ("abT", 3) for key in results)
    check("E4.2 ANATOMY: plain sheet swap (+i) passes exactly on "
          "the bare axis, fails all t > 0 (%s); its -i branch "
          "fails everywhere (%s); the g^3-TWISTED sheet swap "
          "fails EVERYWHERE incl. t = 0 with 1p lam_min = %s "
          "(-0.4621 +- 5e-3, BOTH eta signs: the U_g3 twist is a "
          "new obstruction, not a rescue) (%s); plain 2-cycle: "
          "bare-marginal pass for BOTH eta signs + t > 0 fail "
          "(%s); (abT,3) never entered the scan (%s)"
          % (ok_S0, ok_S0m, [round(l, 4) for l in lm_S3], ok_S3,
             ok_ab, ok_ab3_gone),
          ok_S0 and ok_S0m and ok_S3 and ok_ab and ok_ab3_gone,
          kill="K2")

    Mp = gram(B1_S, r_S, S_ONE, 1j, wk0)
    Mm = gram(B1_S, r_S, S_ONE, -1j, wk0)
    lp = float(np.min(np.linalg.eigvalsh((Mp + Mp.conj().T) / 2)))
    lm_ = float(np.max(np.linalg.eigvalsh((Mm + Mm.conj().T) / 2)))
    check("E4.3 eta = -i flips the 1p Gram against +i: lam_min(+i) "
          "+ lam_max(-i) = %.1e <= 1e-9 at the bare point -- at "
          "most one of +-i can carry positivity per candidate"
          % abs(lp + lm_), abs(lp + lm_) <= 1e-9, kill="K2")

    # ==================================================================
    section("R -- round-58 regressions")
    # ==================================================================
    def lam1p(u, t, beta):
        wk = wick_factory(kms_A(u, t, beta))
        M1 = gram(B1_S, r_S, S_ONE, 1j, wk)
        return float(np.min(np.linalg.eigvalsh(
            (M1 + M1.conj().T) / 2)))

    lo, hi = 0.0, 0.25
    for _ in range(40):
        mid = (lo + hi) / 2
        if lam1p(mid, 0.125, 1.0) < 0:
            lo = mid
        else:
            hi = mid
    uc = (lo + hi) / 2
    hd2_dep = results[("S", 0, "+i")][(0.125, 1.0)][1]
    check("R1 plain sheet swap regression: u_c(1/8, 1) = %.8f "
          "(|u_c - t| = %.1e <= 1e-6); strict deg-2 defect at the "
          "deployed point %.4f (0.0982 +- 0.005)"
          % (uc, abs(uc - 0.125), hd2_dep),
          abs(uc - 0.125) <= 1e-6 and abs(hd2_dep - 0.0982) <= 5e-3,
          kill="K2")

    wkd = WICKS[(0.125, 1.0)]
    M1T = gram(B1_ab, r_abT, S_ONE, 1j, wkd)
    ev = np.linalg.eigvalsh((M1T + M1T.conj().T) / 2)
    Bab = A18[np.ix_(CH[a_ch], CH[b_ch])]
    aJ = (Bab[0, 1] - Bab[1, 0]) / 2
    idd = max(abs(abs(ev[0]) - abs(aJ)), abs(abs(ev[1]) - abs(aJ)),
              abs(ev[0] + ev[1]))
    check("R2 plain 2-cycle regression: odd eigenvalues EXACTLY "
          "{-|a_J|, +|a_J|} at (1, 1/8, 1) (identity defect %.1e "
          "<= 1e-10), a_J = %.4f >= floor" % (idd, abs(aJ)),
          idd <= 1e-10 and abs(aJ) >= NZ_FLOOR, kill="K2")

    # ==================================================================
    section("C -- controls (must fire; RNG only here)")
    # ==================================================================
    rc1 = r_comb(r_S, 1)
    q2 = {a: rc1[rc1[a]] for a in range(16)}
    n_moved = sum(1 for a in range(16) if q2[a] != a)
    rej = not involutive(rc1, 1j)
    check("C1 FIRES: the non-involutive (theta_S, k=1) is rejected "
          "by the Theta^2 = 1 gate (q^2 moves %d >= 4 indices; "
          "gate verdict: rejected = %s)" % (n_moved, rej),
          n_moved >= 4 and rej, kill="K7")

    hd_e1 = max(metrics(gram(B1_S, r_S, S_ONE, 1.0 + 0j, wk0))[0],
                metrics(gram(B1_ab, r_abT, S_ONE, 1.0 + 0j,
                             wk0))[0])
    check("C2 FIRES: eta = +1 breaks Gram Hermiticity at the bare "
          "point for both plain bases (max defect %.3f >= 0.5) -- "
          "v519 twist regression" % hd_e1, hd_e1 >= 0.5, kill="K7")

    rng = np.random.default_rng(899)
    n_fire = 0
    for _trial in range(3):
        perm = rng.permutation(16)
        r = {}
        for k in range(8):
            x, y = int(perm[2 * k]), int(perm[2 * k + 1])
            r[x] = y
            r[y] = x
        P = [min(x, r[x]) for x in r if x < r[x]]
        M1 = gram([(a,) for a in P], r, S_ONE, 1j, wk18)
        hd, lm = metrics(M1)
        if hd >= 0.5 or lm <= -0.1:
            n_fire += 1
    check("C3 FIRES: 3/3 seeded random pairings (rng 899) break "
          "the 1p Gram at the deployed point (%d/3)" % n_fire,
          n_fire == 3, kill="K7")

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
    elif "K1" in KILLS:
        VERDICT = "ENUM-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "RPSCAN-BROKEN"
    else:
        VERDICT = ("TWISTEDRP-MEASURED [CENSUS(16/48 involutive), "
                   "SELECTION(NONE: TWISTED-RP-EXCLUSIONARY -- 0 "
                   "of %d admissible survivors admit strict RP at "
                   "t > 0)]" % len(adm))
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE CENSUS: 48 candidates Theta_g = U_g o theta (2 bases x 6
    C6 powers x 4 degree twists); the involution gate Theta^2 = 1
    is decided by the group theory (q^2 = img^(2k), the 3-cycle
    forces 3 | k) and leaves EXACTLY 16 involutive candidates
    (k in {0, 3}); scalar characters collapse (E1.2).
  * THE ANSWER: NO twisted reflection admits strict RP with
    mixing t > 0.  The twisted-OS escape route is CLOSED on this
    candidate family: (i) the g^3-twisted sheet swap is not
    merely non-positive at t > 0 -- it is indefinite already at
    the BARE point (lam_min = -0.4621, both eta signs): composing
    with transport destroys the bare positivity the plain
    reflection had; (ii) the g^3-twisted 2-cycle is SIDE-FIXING
    and fails Gram Hermiticity at the bare point for every eta --
    not an OS candidate at all; (iii) the plain pairs reproduce
    round 58 (t = 0 only).  RP and the v898 mixing floor remain
    mutually exclusive under every C6-compatible involutive
    twist.
  * The [O] premise of v898 stays [O]; exclusion is a measurement
    on THIS complete finite candidate set, not a universal no-go;
    no marker moves.  NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
