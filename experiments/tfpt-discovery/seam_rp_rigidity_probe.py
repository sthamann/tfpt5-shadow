#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_rp_rigidity_probe -- SEAM.RP.RIGIDITY.PROBE.01 (Strategy S1):
the v903 RP-vs-mixing exclusivity turned into a RIGIDITY CENSUS over
the FULL 33-dim C6-covariant mixing slice.

EXPLORATION ONLY (2026-08-27). experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  v903 (SEAM.STATE.DERIVATION.01) proved the
exclusivity RP <=> a_J = 0 on ONE family only -- the v898 KMS ray
h(u, t) = -(u A16_dep + t A_int), which moves ALL 33 covariant
mixing coordinates simultaneously with t.  Whether reflection
positivity + C6-covariance force the channel-diagonal (quasi-free-
diagonal) point on the WHOLE covariant mixing slice was never
measured: the v898 ray is a 1-dim curve inside a 33-dim slice, and
v911 (wiring freedom) already hints that the strict theta_S
Hermiticity law has a large kernel (rank 12 on the 24-dim coupling
block), i.e. that whole covariant subspaces may be RP-silent.  THIS
probe performs the census: parametrize covariances
    Gamma(s) = (I + i A(s))/2,   A(s) = A0 + sum_i s_i M_i,
    A0 = tanh(1/2) * A16_dep     (== the v898/v903 KMS state at
                                  (u=1, t=0, beta=1) EXACTLY, since
                                  A16_dep^2 = -I),
where {M_i} is the COMPLETE integer basis of the 33-dim C6-covariant
cross-block (mixing) slice of v896/v898 (signed orbit walk on index
pairs, deterministic lex order; the two forced zeros excluded by the
walk itself), demand CAR admissibility (spectral norm of A < 1,
i.e. 0 < Gamma < I), and adjudicate BOTH deployable OS reflections
of v903 -- theta_S (sheet swap, v440 collar lift; half side = the 8
even Majorana indices) and theta_abT (orientation-reversed 2-cycle
of the {4,5} carrier duad; half side = CH(4), whose FULL half-side
algebra is the 4 monomials {(), (6), (7), (6,7)}) -- with the v519
Gram criterion (antilinear reversal, forced twist eta = +i): RP
demands the Gram Hermitian AND PSD, sector-typed (theta_S: deg-1
8-dim + even deg<=2 29-dim, deep spot checks odd deg<=3 64-dim /
even deg<=4 99-dim; theta_abT: the COMPLETE 4-monomial algebra).

THE SETUP (all machinery rebuilt inline from the frozen v898/v903
conventions; tfpt_constants imported READ-ONLY).  The Gram of every
deg<=2 sector is a POLYNOMIAL of degree <= 2 in the slice coordinate
s along any fixed direction (each Wick entry W = I + iA is affine in
s; deg<=2 monomial Grams are Wick sums of <= 4 indices = sums of
products of <= 2 entries), so the decomposition G(s) = G0 + s G1 +
s^2 G2 is recovered EXACTLY (to float rounding) from evaluations at
s in {0, +1/2, -1/2}; first-order (G1) and second-order (G2)
obstructions are therefore exact objects, not finite-difference
approximations, and finite-s adjudication along a direction is exact
quadratic algebra.  Classification per (direction, reflection):
  KILLED-HERM1  nonherm(G1) >= NZ_FLOOR on some sector (Hermiticity
                broken at first order => RP fails for all s != 0);
  KILLED-PSD1   on the kernel of the base Gram the projected
                herm(G1) is indefinite/nonzero at floor (a marginal
                mode moves negative at first order);
  KILLED-PSD2   first-order neutral but the second-order kernel
                obstruction (Schur value v* herm(G2) v on the base
                kernel) <= -NZ_FLOOR (killed for BOTH signs of s);
  NEUTRAL       none of the above through second order; finite-s RP
                window measured by exact quadratic scan + bisection.
The joint reading follows the OS convention stated in v903/v911:
OS positivity w.r.t. AT LEAST ONE deployed reflection suffices; the
census reports each reflection separately AND the union.

PRE-REGISTERED ADJUDICATION (bars frozen BEFORE the record runs).
SMOKE DISCLOSURE: TWO structural smoke passes of this probe (same
machinery; the first with provisionally guessed census bars, the
second after the census fix described next) were run on 2026-08-27
before the freeze and informed the starred (*) numbers below -- the
theta_S census counts, the neutral-subspace dimension and its
NON-basis-aligned structure (the first smoke refuted the guessed
per-direction counts 16/17: per-direction kills are 32/33 while the
defect-map RANK is 16, i.e. the neutral cone is made of intra-family
combinations; the census gate and the window probes were rewritten
to measure the subspace honestly, plus one normalization fix in the
vacuum-J span check), the finite-s windows, the witness margins and
the mutant defect sizes; the smoke outputs were not retained as
files (workspace constraint: only this probe and its run logs may
be written); no anchor, threshold convention, basis order,
reflection, sector, witness point or verdict rule was changed after
the smokes.  Thresholds (v903 conventions): NZ_FLOOR = 1e-8, ZTOL =
1e-10, EXTOL = 1e-12.
 P1  ANCHOR REPRODUCTION (v903 R3.2 / R2.4 verbatim): on the v898
     KMS family at (u=1, beta=1), t in {0.01, 1/16, 1/8}: the
     theta_abT odd-sector Gram eigenvalues are EXACTLY {-|a_J|,
     +|a_J|} of the {4,5} carrier cross-block (identity defect and
     trace <= 1e-10), a_J >= NZ_FLOOR and lam_min <= -NZ_FLOOR for
     every scanned t > 0 (strict RP forces the v898 mixing floor to
     fall), marginal at t = 0 (|Gram| <= 1e-10); v898 regression
     smax = 0.667735 +- 2e-3, 15/15 blocks, forced zeros; theta_S
     even deg-2 relative Hermiticity defect at the deployed point =
     0.0982 +- 5e-3.
 P2  BASIS + BASE POINT: the signed orbit walk yields EXACTLY 33
     cross-block + 17 channel-diagonal free orbits + 2 forced zeros
     (v898 H1.2); every M_i integer, antisymmetric, EXACTLY
     C6-covariant (integer residual 0), supports pairwise disjoint;
     exactly ONE direction (the {4,5}-J coordinate a_J) has support
     inside the {4,5} block; the index-permutation involutions
     T_theta on the slice square to the identity (parity dims
     reported); base point A0: CAR strict (smax = tanh(1/2) +-
     1e-12), SEAM-DIAGONAL (0/15 cross-blocks), base Grams equal
     their CLOSED FORMS: theta_S odd = tanh(1/2) I_8, theta_S even
     = diag(1, tanh^2(1/2) I_28) (the v911 D5 values), theta_abT
     odd = 0, theta_abT even eigenvalues {0, 1 + tanh^2(1/2)}
     (marginal), all to 1e-12.
 P3  THE LINEARIZED CENSUS: (a) polynomial exactness ward:
     reconstruction of the Gram at s = 3/8 from (G0, G1, G2) to
     1e-10 on both reflections; (b) theta_abT: EXACTLY 1/33
     direction is visible -- the a_J direction, KILLED-PSD1 with
     odd-sector G1 eigenvalues EXACTLY {+1, -1} per unit s and
     even-sector second-order kernel value -1/(1 + tanh^2(1/2)) +-
     1e-10 (killed for both signs); the other 32/33 have G1 = G2 =
     0 IDENTICALLY on the complete 4-monomial algebra (theta_abT-
     INVISIBLE: neutral to ALL orders, sector-complete), confirmed
     at finite s = 1/4 on 3 sample directions (full Gram equal to
     the base Gram to 1e-12); (c) theta_S: per-direction first-
     order classification; (*) frozen counts: KILLED-HERM1 = 32 of
     33 COORDINATE directions (every entry-orbit direction except
     a_J breaks Gram Hermiticity at first order, defect O(1)), the
     ONLY basis-aligned neutral direction is a_J; but the
     Hermiticity defect is LINEAR in the slice coordinates and its
     stacked defect map has RANK 16 exactly => the first-order-
     neutral SUBSPACE has dimension 17 and is NOT basis-aligned:
     it consists of intra-family combinations (J/Z-type
     recombinations of the entry-orbit coordinates -- the v911
     rank-12/kernel-12 coupling law transported to the state
     slice, plus the carrier-carrier analogues and a_J); the
     frozen gate demands per-direction kills = 32, basis-aligned
     neutral = [a_J], rank = 16, nullspace dim = 17, and that the
     explicit vacuum-J stack direction [J2; J2; J2] (covariant,
     in-slice) has first-order defect <= 1e-10.
 P4  WITNESSES (explicit finite-s states; all CAR-admissible,
     C6-covariant, nonzero mixing):
     W_ab  the 32-coordinate theta_abT witness: s = 1/32 on ALL 32
           invisible directions; demands: CAR margin >= 1e-8 (*
           measured ~0.19), covariance EXACT (residual 0), the
           complete theta_abT Gram IDENTICAL to the base Gram
           (<= 1e-12), Hermitian, PSD with lam_min >= -ZTOL
           (MARGINAL: on the RP cone boundary, the v903 dilation-
           witness typing -- OS positivity is a closed condition,
           marginal PASSES), mixing census 14/15 duads >= NZ_FLOOR
           with the {4,5} block EXACTLY zero.
     W_S   the strict theta_S witness along the PURE a_J direction
           at s = 1/8: demands Hermitian <= 1e-8 on odd + even
           sectors AND lam_min >= 1e-8 (STRICT interior margin,
           * measured lam_min ~0.19 even / 0.46 odd), CAR margin
           >= 1e-8, a_J block norm >= 1e-8; the SAME point is
           REJECTED by theta_abT (odd lam_min <= -1e-8) -- the
           exclusivity is REFLECTION-RELATIVE.
     W_S2  the vacuum-J wiring witness (the v911 pure-J coupling
           transported to the state slice): the covariant direction
           with unit stack [J2; J2; J2] on both vacuum orbits, at
           s = 1/16: demands the same strict theta_S bars as W_S
           (* measured lam_min ~0.03 even), CAR margin >= 1e-8,
           5/5 vacuum duads lit.
     Deep-sector spot check: at the base point the theta_S deep
     sectors reproduce v903 R2.6 (odd deg<=3 lam_min = 0.0987 +-
     5e-3, even deg<=4 lam_min = 0.0456 +- 5e-3, Hermitian <=
     ZTOL); at W_S the deep sectors stay Hermitian <= 1e-8 with
     lam_min >= 1e-8 (* measured ~0.04).
 P5  SECOND ORDER on the theta_S neutral cone: G2 Hermiticity
     defect <= NZ_FLOOR on every probed neutral direction (no
     HERM2 kill; base Gram strictly PD with lam_min = tanh^2(1/2)
     > 0.05, so NO local PSD kill is possible -- rigidity along
     the neutral cone is a FINITE-s phenomenon); finite-s RP
     windows (exact quadratic scan to s = 2, bisection, with the
     CAR boundary computed separately and each window typed
     RP-limited vs CAR-limited) for the a_J direction, the
     vacuum-J direction and the first 4 SVD nullspace combination
     vectors (deterministic), BOTH signs; (*) frozen bar: every
     probed window >= 0.05, the a_J windows >= 0.4 (* measured:
     a_J 0.4621 both signs RP-limited, vacJ 0.1193, null combos
     0.267..0.539).
 P6  NEGATIVE CONTROLS (must fire): (a) the non-covariant direction
     E_{6,8} - E_{8,6} (the FORCED diagonal of the {4,5} block) is
     flagged: covariance residual >= 1, projection onto the slice
     EXACTLY 0; (b) the seeded random non-admissible Gamma (rng
     seed 903, antisymmetric, scaled to spectral norm 3/2) FAILS
     the CAR gate (smax >= 1).
 P7  JOINT ADJUDICATION + MUTANTS: per-reflection RP-compatible
     mixing dimensions reported separately and jointly (at-least-
     one-reflection OS convention, stated); THREE must-fail mutants
     are CAUGHT: (MUT-A) the UNTWISTED 2-cycle swap (drop the
     intra-pair twist) breaks the P1 anchor -- base Gram relative
     Hermiticity defect >= 0.3 (v903 R1.1); (MUT-B) twist eta = +1
     breaks base Hermiticity on both reflections (max defect >=
     0.3); (MUT-C) twist eta = -i flips the theta_S odd base Gram
     negative (lam_min <= -0.4).
VERDICT RULE (frozen): RP_FORCES_DIAGONAL iff NO CAR-admissible
C6-covariant finite-s witness with nonzero mixing passes the full
deployed Gram battery of at least one reflection AND every direction
is killed under both reflections; RP_ADMITS_MIXING iff at least one
witness passes (marginal witnesses count, typed MARGINAL vs STRICT);
PARTIAL_RIGIDITY (with dims) otherwise (neutral directions exist but
every finite-s witness fails).  EXPECTED (pre-registered from the
smokes): RP_ADMITS_MIXING -- theta_abT admits the FULL 32-dim
{a_J = 0} hyperplane marginally (its Gram is a 2-channel window:
sector-complete invisibility), theta_S admits a 17-dim first-order-
neutral subspace of intra-family combinations including the a_J
direction STRICTLY at finite s, and JOINTLY every one of the 33
covariant mixing coordinate directions is individually
RP-compatible under at least one deployed reflection:
RP + C6-covariance do NOT force the quasi-free-diagonal point; the
v903 exclusivity is a statement about the v898 RAY (which moves the
killed and the neutral coordinates together), not about the slice.

HONEST LIMITATIONS (typed): the theta_S census is sector-truncated
(deg <= 2 Grams + deg <= 4 spot checks; the full 256-monomial
half-side algebra is not exhausted -- a deeper sector could still
kill a neutral direction); theta_abT is sector-COMPLETE (4
monomials) but is a 2-channel window: invisibility means RP-SILENT,
not RP-certified-positive beyond the window; the census is
first+second order + finite-s along COORDINATE directions and the
two named combination witnesses -- the full 33-dim RP region
geometry (simultaneous multi-coordinate boundaries) is not mapped;
all statements are float64 measurements at the v903 exploration
grade with frozen thresholds, not exact-arithmetic theorems; the
v898/v903 [O] premise is UNMOVED; whether the actual seam realizes
any of these states is untouched.  NO RH claim (compiler side; no
zeros, no primes; AST firewall inside).

FIREWALL: experiments/ probe; writes nothing but stdout; no
verification/, paper, ledger, changelog or website surface; no .md,
no commits.  Deterministic: the ONLY RNG is the declared seeded
control (P6b, seed 903); numpy eigh/svd deterministic; runtime
gate < 180 s.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_rp_rigidity_probe.py
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

NZ_FLOOR = 1e-8            # nonzero decision floor (frozen, v903)
ZTOL = 1e-10               # structural-zero ceiling (frozen, v903)
EXTOL = 1e-12              # exact-identity tolerance (frozen)
H_STEP = 0.5               # polynomial extraction step (exact dyadic)
C_BASE = math.tanh(0.5)    # base point coefficient (v903 strict point)
S_MARG = 1.0 / 32          # W_ab witness coupling (frozen)
S_WIT = 0.125              # W_S witness coupling (frozen)
S_WIT2 = 1.0 / 16          # W_S2 witness coupling (frozen)
RNG_SEED = 903             # the ONLY RNG use (control P6b)

# frozen smoke-informed census bars (*):
FZ_KILLED_H1 = 32          # theta_S per-direction Hermiticity kills
FZ_NEUTRAL_DIRS = 1        # basis-aligned neutral directions (a_J)
FZ_RANK = 16               # rank of the Hermiticity-defect map
FZ_NULLDIM = 17            # first-order-neutral SUBSPACE dimension
FZ_WINDOW_MIN = 0.05       # minimal finite-s RP window (probed dirs)
FZ_WINDOW_AJ = 0.4         # minimal window along the a_J direction

GATES = []
T0 = time.time()


def gate(title, ok, detail=""):
    k = len(GATES) + 1
    GATES.append(bool(ok))
    print("GATE %d %s: %s ... %s"
          % (k, title, detail, "PASS" if ok else "FAIL"), flush=True)
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
# (v880 / v888 conventions rebuilt inline, byte-parallel to v903)
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
    print("SEAM.RP.RIGIDITY.PROBE.01 -- RP rigidity census on the "
          "full 33-dim C6-covariant mixing slice")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    print("SPEC_SHA = %s" % spec_sha[:16])
    print("exploration only; no promotion, no ledger row, no marker "
          "moved, no gate closed or narrowed.")

    # ==================================================================
    section("S0 -- firewall + compiler rebuild (v898/v903 verbatim)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    ok_qstar = (ok_ref and len(set(refs)) == 16 and len(arf1) == 6
                and len(cand) == 1)
    QSTAR = cand[0]
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

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
    ok_aut = (gl_n == 20160 and len(SP6) == 720 and len(AUT) == 6
              and len(g_pin) == 1)
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
    gate("S0.1 firewall + compiler rebuild",
         not bad and ok_qstar and ok_phi and ok_aut
         and PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3)
         and (a_ch, b_ch) == (4, 5)
         and N_fam == 3 and g_car == 5,
         "AST clean; unique q*; |Sp(4,2)|=%d==720, |Aut|=%d==6; "
         "pi=%s cycle type %s, 2-cycle {%d,%d}; N_fam=%d, g_car=%d"
         % (len(SP6), len(AUT), PI6, cycle_type(PI6), a_ch, b_ch,
            N_fam, g_car))

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]
    ch_of = {}
    for i in range(6):
        for s in CH[i]:
            ch_of[s] = i

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

    Aint_f = A_int.astype(np.float64)
    Adep_f = A16_dep.astype(np.float64)
    I16 = np.eye(16)

    def kms_A_gen(u, t, beta):
        h = -(u * Adep_f + t * Aint_f)
        w, Q = np.linalg.eigh(1j * h)
        f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
        C = (Q * f) @ Q.conj().T
        return (-1j * (2 * C - I16)).real, w

    def blocks_census(A):
        return {(i, j):
                float(np.linalg.norm(A[np.ix_(CH[i], CH[j])]))
                for (i, j) in DUADS_CH}

    A18, w18 = kms_A_gen(1.0, 0.125, 1.0)
    smax18 = float(np.max(np.abs(np.tanh(1.0 * w18 / 2.0))))
    bn18 = blocks_census(A18)
    n18 = sum(1 for v in bn18.values() if v >= NZ_FLOOR)
    fz18 = max(abs(A18[CH[a_ch][k], CH[b_ch][k]]) for k in range(2))
    gate("S0.2 kernels + v898 KMS regression",
         okA and okD and abs(smax18 - 0.667735) < 2e-3
         and n18 == 15 and fz18 < ZTOL,
         "A_int/A16_dep integer covariant; (u=1,t=1/8,beta=1): "
         "smax=%.6f (0.667735 +- 2e-3), blocks %d/15, forced zeros "
         "%.1e < ZTOL" % (smax18, n18, fz18))

    # ---------------- RP machinery (v519 form, v903 port, verbatim)
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

    r_ab = {k: k for k in range(16)}          # untwisted (MUT-A)
    for k in range(2):
        r_ab[CH[a_ch][k]] = CH[b_ch][k]
        r_ab[CH[b_ch][k]] = CH[a_ch][k]
    r_abT = {k: k for k in range(16)}
    for k in range(2):
        r_abT[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_abT[CH[b_ch][k]] = CH[a_ch][1 - k]
    P_ab = list(CH[a_ch])

    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]
    B1_ab = [(a,) for a in P_ab]
    B2_ab = [(), tuple(P_ab)]

    SPEC_S = {"name": "theta_S", "r": r_S,
              "sectors": {"odd1": B1_S, "even2": B2_S}}
    SPEC_T = {"name": "theta_abT", "r": r_abT,
              "sectors": {"odd1": B1_ab, "even2": B2_ab}}

    def grams(A, spec, eta=1j):
        wk = wick_factory(A)
        return {nm: gram(b, spec["r"], S_ONE, eta, wk)
                for nm, b in spec["sectors"].items()}

    # ==================================================================
    section("P1 -- anchor reproduction (v903 R3.2 / R2.4)")
    # ==================================================================
    worst_id = 0.0
    worst_hd = 0.0
    ok_anchor = True
    aJ_dep = None
    for t in (0.01, 1.0 / 16, 0.125):
        A, _w = kms_A_gen(1.0, t, 1.0)
        wk = wick_factory(A)
        M1 = gram(B1_ab, r_abT, S_ONE, 1j, wk)
        hd = float(np.max(np.abs(M1 - M1.conj().T)))
        ev = np.linalg.eigvalsh((M1 + M1.conj().T) / 2)
        B = A[np.ix_(CH[a_ch], CH[b_ch])]
        aJ = (B[0, 1] - B[1, 0]) / 2
        if t == 0.125:
            aJ_dep = aJ
        worst_hd = max(worst_hd, hd)
        worst_id = max(worst_id,
                       float(abs(abs(ev[0]) - abs(aJ))),
                       float(abs(abs(ev[1]) - abs(aJ))),
                       float(abs(ev[0] + ev[1])))
        ok_anchor &= (abs(aJ) >= NZ_FLOOR and ev[0] <= -NZ_FLOOR)
        print("      t=%-7s a_J=%+.8f  odd eigs (%.8f, %.8f)"
              % (round(t, 4), aJ, ev[0], ev[1]))
    A0_kms, _w0 = kms_A_gen(1.0, 0.0, 1.0)
    wk0 = wick_factory(A0_kms)
    M1_0 = gram(B1_ab, r_abT, S_ONE, 1j, wk0)
    marg0 = float(np.max(np.abs(M1_0)))
    gate("P1.1 anchor identity: theta_abT odd Gram eigs == +-|a_J|",
         worst_id <= 1e-10 and worst_hd <= 1e-10 and marg0 <= 1e-10,
         "worst identity defect %.1e <= 1e-10, Hermiticity %.1e, "
         "t=0 marginal %.1e" % (worst_id, worst_hd, marg0))
    gate("P1.2 strict RP forces the v898 floor to fall",
         ok_anchor,
         "every scanned t > 0: a_J >= NZ_FLOOR and lam_min <= "
         "-NZ_FLOOR (deployed a_J = %+.8f)" % aJ_dep)
    wk18 = wick_factory(A18)
    M2S_18 = gram(B2_S, r_S, S_ONE, 1j, wk18)
    hd_dep, _lm = metrics(M2S_18)
    gate("P1.3 theta_S even deg-2 defect at the deployed point",
         abs(hd_dep - 0.0982) <= 5e-3,
         "relative Hermiticity defect %.6f (0.0982 +- 5e-3, v903 "
         "R2.4)" % hd_dep)

    # ==================================================================
    section("P2 -- the covariant mixing basis + the base point")
    # ==================================================================
    all_pairs = [(r, c) for r in range(16) for c in range(r + 1, 16)]
    visited = set()
    basis = []          # (rep pair, orbit dict, matrix, duad set)
    n_diag_free = 0
    n_forced = 0
    for p0 in all_pairs:
        if p0 in visited:
            continue
        orb = {}
        cur, sgn = p0, 1
        forced = False
        while True:
            if cur in orb:
                if orb[cur] != sgn:
                    forced = True
                break
            orb[cur] = sgn
            r, c = img[cur[0]], img[cur[1]]
            if r > c:
                r, c, sgn = c, r, -sgn
            cur = (r, c)
        visited |= set(orb)
        cross = ch_of[p0[0]] != ch_of[p0[1]]
        if forced:
            n_forced += 1
        elif cross:
            M = np.zeros((16, 16))
            duads = set()
            for (r, c), sg in orb.items():
                M[r, c] = sg
                M[c, r] = -sg
                duads.add((min(ch_of[r], ch_of[c]),
                           max(ch_of[r], ch_of[c])))
            basis.append((p0, orb, M, frozenset(duads)))
        else:
            n_diag_free += 1
    n_cross = len(basis)
    ok_cov = all(np.array_equal(M[np.ix_(img, img)], M)
                 for (_p, _o, M, _d) in basis)
    supp = np.zeros((16, 16))
    for (_p, _o, M, _d) in basis:
        supp += np.abs(M)
    ok_disj = float(np.max(supp)) <= 1.0
    jdirs = [k for k, (_p, _o, _M, d) in enumerate(basis)
             if d == frozenset({(a_ch, b_ch)})]
    gate("P2.1 walk census: 33 cross + 17 diag + 2 forced",
         n_cross == 33 and n_diag_free == 17 and n_forced == 2
         and ok_cov and ok_disj and len(jdirs) == 1,
         "cross=%d, diag=%d, forced=%d; every M_i exactly "
         "C6-covariant (%s), supports disjoint (%s); unique "
         "{%d,%d}-support direction: index %s"
         % (n_cross, n_diag_free, n_forced, ok_cov, ok_disj,
            a_ch, b_ch, jdirs))
    JDIR = jdirs[0]
    M_J = basis[JDIR][2]

    def parity_matrix(perm16):
        T = np.zeros((33, 33))
        ok = True
        for k, (_rk, _ok, M, _dk) in enumerate(basis):
            Mt = M[np.ix_(perm16, perm16)]
            rec = np.zeros((16, 16))
            for jx, (rj, _oj, Mj, _dj) in enumerate(basis):
                r0, c0 = rj
                cf = Mt[r0, c0] * Mj[r0, c0]
                T[jx, k] = cf
                if cf != 0.0:
                    rec += cf * Mj
            ok &= np.array_equal(rec, Mt)
        return T, ok

    perm_S = [r_S[k] for k in range(16)]
    perm_T = [r_abT[k] for k in range(16)]
    T_S, okTS = parity_matrix(perm_S)
    T_T, okTT = parity_matrix(perm_T)
    inv_S = np.array_equal(T_S @ T_S, np.eye(33))
    inv_T = np.array_equal(T_T @ T_T, np.eye(33))
    nmin_S = int(round((33 - np.trace(T_S)) / 2))
    nmin_T = int(round((33 - np.trace(T_T)) / 2))
    aJ_par_T = float((T_T @ np.eye(33)[:, JDIR])[JDIR])
    gate("P2.2 slice involutions T_theta (index-permutation action)",
         okTS and okTT and inv_S and inv_T,
         "closed on the slice (%s/%s), T^2 = I (%s/%s); parity dims "
         "theta_S: (+%d, -%d), theta_abT: (+%d, -%d); a_J parity "
         "under theta_abT = %+.0f"
         % (okTS, okTT, inv_S, inv_T, 33 - nmin_S, nmin_S,
            33 - nmin_T, nmin_T, aJ_par_T))

    A0 = C_BASE * Adep_f
    smax0 = float(np.max(np.abs(np.linalg.eigvalsh(1j * A0))))
    n0 = sum(1 for v in blocks_census(A0).values() if v >= NZ_FLOOR)
    G0_S = grams(A0, SPEC_S)
    G0_T = grams(A0, SPEC_T)
    c2 = C_BASE * C_BASE
    dev_S1 = float(np.max(np.abs(G0_S["odd1"]
                                 - C_BASE * np.eye(8))))
    ref_S2 = np.diag([1.0] + [c2] * 28).astype(complex)
    dev_S2 = float(np.max(np.abs(G0_S["even2"] - ref_S2)))
    dev_T1 = float(np.max(np.abs(G0_T["odd1"])))
    ref_T2 = np.array([[1.0, 1j * C_BASE],
                       [-1j * C_BASE, c2]], dtype=complex)
    dev_T2 = float(np.max(np.abs(G0_T["even2"] - ref_T2)))
    ev_T2 = np.linalg.eigvalsh((G0_T["even2"]
                                + G0_T["even2"].conj().T) / 2)
    gate("P2.3 base point A0 = tanh(1/2) A16_dep: closed forms",
         abs(smax0 - C_BASE) <= EXTOL and n0 == 0
         and dev_S1 <= EXTOL and dev_S2 <= EXTOL
         and dev_T1 <= EXTOL and dev_T2 <= EXTOL
         and abs(ev_T2[0]) <= EXTOL
         and abs(ev_T2[1] - (1 + c2)) <= EXTOL,
         "CAR smax=%.12f==tanh(1/2), SEAM-DIAGONAL %d/15; "
         "theta_S odd == cI (%.1e), even == diag(1, c^2 I28) "
         "(%.1e, lam_min=c^2=%.6f); theta_abT odd == 0 (%.1e), "
         "even eigs {%.1e, %.6f} == {0, 1+c^2}"
         % (smax0, n0, dev_S1, dev_S2, c2, dev_T1, ev_T2[0],
            ev_T2[1]))

    # ==================================================================
    section("P3 -- the linearized census (exact quadratic algebra)")
    # ==================================================================
    def gram_poly(Mdir, spec, G0s):
        Gp = grams(A0 + H_STEP * Mdir, spec)
        Gm = grams(A0 - H_STEP * Mdir, spec)
        G1 = {nm: (Gp[nm] - Gm[nm]) / (2 * H_STEP) for nm in G0s}
        G2 = {nm: (Gp[nm] + Gm[nm] - 2 * G0s[nm])
              / (2 * H_STEP * H_STEP) for nm in G0s}
        return G1, G2

    # polynomial exactness ward at s = 3/8 on two directions
    ok_poly = True
    worst_rec = 0.0
    for k in (0, JDIR):
        Mdir = basis[k][2]
        for spec, G0s in ((SPEC_S, G0_S), (SPEC_T, G0_T)):
            G1, G2 = gram_poly(Mdir, spec, G0s)
            Gx = grams(A0 + 0.375 * Mdir, spec)
            for nm in G0s:
                rec = (G0s[nm] + 0.375 * G1[nm]
                       + 0.375 ** 2 * G2[nm])
                worst_rec = max(worst_rec,
                                float(np.max(np.abs(rec - Gx[nm]))))
    ok_poly = worst_rec <= 1e-10
    gate("P3.1 polynomial exactness ward (deg <= 2 in s)",
         ok_poly,
         "reconstruction at s = 3/8 from (G0, G1, G2): worst "
         "entry defect %.1e <= 1e-10" % worst_rec)

    def census_pass():
        """per-direction first/second-order data, both reflections
        (pure function of the frozen inputs; run twice for the
        determinism fingerprint)."""
        rows = []
        for k in range(33):
            Mdir = basis[k][2]
            G1S, G2S = gram_poly(Mdir, SPEC_S, G0_S)
            G1T, G2T = gram_poly(Mdir, SPEC_T, G0_T)
            hd1S = max(float(np.max(np.abs(G1S[nm]
                                           - G1S[nm].conj().T)))
                       for nm in G0_S)
            hd2S = max(float(np.max(np.abs(G2S[nm]
                                           - G2S[nm].conj().T)))
                       for nm in G0_S)
            visT = max(max(float(np.max(np.abs(G1T[nm]))),
                           float(np.max(np.abs(G2T[nm]))))
                       for nm in G0_T)
            rows.append((k, hd1S, hd2S, visT, G1S, G2S, G1T, G2T))
        return rows

    rows = census_pass()
    fp1 = hashlib.sha256(("|".join(
        "%d:%.12e:%.12e:%.12e" % (k, h1, h2, v)
        for (k, h1, h2, v, *_r) in rows)).encode()).hexdigest()

    # ---- theta_abT census
    vis_idx = [k for (k, _h1, _h2, v, *_r) in rows if v > EXTOL]
    invis_idx = [k for (k, _h1, _h2, v, *_r) in rows if v <= EXTOL]
    ok_vis = (vis_idx == [JDIR])
    G1T_J = rows[JDIR][6]
    G2T_J = rows[JDIR][7]
    evJ = np.linalg.eigvalsh((G1T_J["odd1"]
                              + G1T_J["odd1"].conj().T) / 2)
    dev_evJ = float(max(abs(evJ[0] + 1), abs(evJ[1] - 1)))
    # even-sector second-order kernel value on the base zero mode
    vker = np.array([-1j * C_BASE, 1.0], dtype=complex)
    vker /= np.linalg.norm(vker)
    H2 = (G2T_J["even2"] + G2T_J["even2"].conj().T) / 2
    q2 = float(np.real(vker.conj() @ H2 @ vker))
    q2_ref = -1.0 / (1.0 + c2)
    gate("P3.2 theta_abT census: 1 visible / 32 invisible",
         ok_vis and dev_evJ <= EXTOL and abs(q2 - q2_ref) <= 1e-10
         and len(invis_idx) == 32,
         "visible = %s == [a_J dir %d]; odd G1 eigs (%.12f, %.12f) "
         "== (-1, +1) per unit s [KILLED-PSD1 both signs]; even "
         "second-order kernel value %.10f == -1/(1+c^2) = %.10f "
         "[KILLED-PSD2]; invisible 32/33 with G1 = G2 = 0 exactly"
         % (vis_idx, JDIR, evJ[0], evJ[1], q2, q2_ref))

    ok_fin = True
    worst_fin = 0.0
    for k in invis_idx[:3]:
        Gx = grams(A0 + 0.25 * basis[k][2], SPEC_T)
        for nm in G0_T:
            worst_fin = max(worst_fin,
                            float(np.max(np.abs(Gx[nm]
                                                - G0_T[nm]))))
    ok_fin = worst_fin <= EXTOL
    gate("P3.3 theta_abT sector-complete invisibility at finite s",
         ok_fin,
         "3 sample invisible directions at s = 1/4: complete "
         "4-monomial Gram == base Gram, worst defect %.1e <= 1e-12 "
         "(the half-side algebra of CH(%d) is COMPLETE: 4 "
         "monomials)" % (worst_fin, a_ch))

    # ---- theta_S census
    killed_H1 = [k for (k, h1, *_r) in rows if h1 >= NZ_FLOOR]
    neutral_1 = [k for (k, h1, *_r) in rows if h1 < NZ_FLOOR]
    # nullspace of the Hermiticity-defect LINEAR map on the slice
    # (v -> sum v_k nonherm(G1_k)); null basis = left-singular
    # vectors of the stacked defect rows with zero singular value
    def_rows = []
    for (k, _h1, _h2, _v, G1S, _G2S, _G1T, _G2T) in rows:
        vec = np.concatenate(
            [np.concatenate([(G1S[nm] - G1S[nm].conj().T).real
                             .ravel(),
                             (G1S[nm] - G1S[nm].conj().T).imag
                             .ravel()]) for nm in ("odd1", "even2")])
        def_rows.append(vec)
    DEF = np.array(def_rows)
    U, sv, _Vh = np.linalg.svd(DEF, full_matrices=False)
    rank = int(np.sum(sv > 1e-8))
    nulldim = 33 - rank
    NULLB = U[:, rank:]                     # 33 x nulldim
    print("      theta_S per-direction first-order table "
          "(rep pair | duads | hd1 | class):")
    for (k, h1, _h2, _v, *_r) in rows:
        rep, _o, _M, dd = basis[k]
        print("        #%02d rep %-8s duads %-30s hd1 %.3e  %s"
              % (k, rep, sorted(dd), h1,
                 "KILLED-HERM1" if h1 >= NZ_FLOOR else "neutral"))
    # orbit-family support census of the neutral subspace (report)
    fams = {}
    for k in range(33):
        key = tuple(sorted(basis[k][3]))
        fams.setdefault(key, []).append(k)
    print("      neutral-subspace weight per duad-orbit family:")
    for key, idxs in sorted(fams.items()):
        w = float(np.sum(NULLB[idxs, :] ** 2))
        print("        family %-42s dims %2d  neutral weight %.4f"
              % (str(list(key)), len(idxs), w))
    gate("P3.4 theta_S first-order census (frozen counts)",
         len(killed_H1) == FZ_KILLED_H1
         and neutral_1 == [JDIR]
         and len(neutral_1) == FZ_NEUTRAL_DIRS
         and rank == FZ_RANK and nulldim == FZ_NULLDIM,
         "per-direction KILLED-HERM1 = %d/33 (frozen %d), basis-"
         "aligned neutral = %s == [a_J dir %d]; defect-map rank %d "
         "(frozen %d) => first-order-neutral SUBSPACE dim %d "
         "(frozen %d): the neutral cone is NOT basis-aligned -- it "
         "is made of intra-family COMBINATIONS (the v911 kernel "
         "transported); sv gap %.1e / %.1e"
         % (len(killed_H1), FZ_KILLED_H1, neutral_1, JDIR, rank,
            FZ_RANK, nulldim, FZ_NULLDIM,
            sv[rank - 1] if rank >= 1 else 0.0,
            sv[rank] if rank < 33 else 0.0))

    # ==================================================================
    section("P5 -- second order + finite-s windows (theta_S)")
    # ==================================================================
    base_pd = min(float(np.min(np.linalg.eigvalsh(
        (G0_S[nm] + G0_S[nm].conj().T) / 2))) for nm in G0_S)

    def car_smax(A):
        return float(np.max(np.abs(np.linalg.eigvalsh(1j * A))))

    def car_window(Mdir, sgn, s_hi=4.0):
        lo, hi = 0.0, s_hi
        if car_smax(A0 + sgn * s_hi * Mdir) < 1 - 1e-9:
            return s_hi
        for _ in range(50):
            mid = (lo + hi) / 2
            if car_smax(A0 + sgn * mid * Mdir) < 1 - 1e-9:
                lo = mid
            else:
                hi = mid
        return lo

    def rp_window(Mdir, sgn, s_hi=2.0):
        G1, G2 = gram_poly(Mdir, SPEC_S, G0_S)
        hd2 = max(float(np.max(np.abs(G2[nm] - G2[nm].conj().T)))
                  for nm in G0_S)

        def ok(s):
            if car_smax(A0 + sgn * s * Mdir) >= 1 - 1e-9:
                return False
            for nm in G0_S:
                G = (G0_S[nm] + (sgn * s) * G1[nm]
                     + (sgn * s) ** 2 * G2[nm])
                if float(np.max(np.abs(G - G.conj().T))) > NZ_FLOOR:
                    return False
                if float(np.min(np.linalg.eigvalsh(
                        (G + G.conj().T) / 2))) < -ZTOL:
                    return False
            return True

        s_ok, s_bad = 0.0, None
        for kk in range(1, 201):
            s = s_hi * kk / 200.0
            if ok(s):
                s_ok = s
            else:
                s_bad = s
                break
        if s_bad is None:
            return s_hi, hd2
        lo, hi = s_ok, s_bad
        for _ in range(40):
            mid = (lo + hi) / 2
            if ok(mid):
                lo = mid
            else:
                hi = mid
        return lo, hd2

    M_vacJ = np.zeros((16, 16))
    JSTACK = IOTA6 @ J2
    for edges, rev, rep in orbs:
        i, j = rep
        if i != 0:
            continue
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(M_vacJ, x, y, JSTACK)
            x, y = PI6[x], PI6[y]
    ok_vacJ = (np.array_equal(M_vacJ[np.ix_(img, img)], M_vacJ)
               and np.array_equal(M_vacJ, -M_vacJ.T))
    coef = np.array([np.sum(M_vacJ * basis[k][2])
                     / np.sum(basis[k][2] * basis[k][2])
                     for k in range(33)])
    resid = M_vacJ - sum(coef[k] * basis[k][2] for k in range(33))
    ok_span = float(np.max(np.abs(resid))) == 0.0
    # vacJ must lie in the first-order-neutral subspace
    hd1_vacJ = float(np.linalg.norm(DEF.T @ coef, ord=np.inf))

    win_tab = []
    probe_dirs = [("a_J", M_J), ("vacJ", M_vacJ)]
    for jn in range(min(4, nulldim)):
        Mn = sum(NULLB[k, jn] * basis[k][2] for k in range(33))
        probe_dirs.append(("null%d" % jn, Mn))
    ok_win = ok_vacJ and ok_span and hd1_vacJ <= 1e-10
    hd2_worst = 0.0
    for namew, Mdir in probe_dirs:
        wp, hd2p = rp_window(Mdir, +1)
        wm, hd2m = rp_window(Mdir, -1)
        cp = car_window(Mdir, +1)
        cm = car_window(Mdir, -1)
        hd2_worst = max(hd2_worst, hd2p, hd2m)
        win_tab.append((namew, wp, wm))
        bar = FZ_WINDOW_AJ if namew == "a_J" else FZ_WINDOW_MIN
        ok_win &= (wp >= bar and wm >= bar)
        typ_p = "CAR-limited" if wp >= cp - 1e-6 else "RP-limited"
        typ_m = "CAR-limited" if wm >= cm - 1e-6 else "RP-limited"
        print("      window %-6s s*_+ = %.6f (CAR %.6f, %s)   "
              "s*_- = %.6f (CAR %.6f, %s)"
              % (namew, wp, cp, typ_p, wm, cm, typ_m))
    gate("P5.1 second order on the neutral cone",
         hd2_worst <= NZ_FLOOR and base_pd > 0.05,
         "worst G2 Hermiticity defect over all probed neutral "
         "directions %.1e <= NZ_FLOOR (no HERM2 kill); base Gram "
         "strictly PD (lam_min %.6f == tanh^2(1/2) > 0.05) => no "
         "local PSD kill: rigidity along the neutral cone is a "
         "finite-s question" % (hd2_worst, base_pd))
    gate("P5.2 finite-s RP windows along the neutral cone",
         ok_win,
         "vacuum-J direction covariant / in-slice / first-order "
         "neutral (%s/%s/defect %.1e); every probed window >= "
         "%.2f, a_J windows >= %.2f (frozen bars)"
         % (ok_vacJ, ok_span, hd1_vacJ, FZ_WINDOW_MIN,
            FZ_WINDOW_AJ))

    # ==================================================================
    section("P4 -- witnesses (explicit finite-s states)")
    # ==================================================================
    M_mix = sum(basis[k][2] for k in invis_idx)
    A_wab = A0 + S_MARG * M_mix
    smax_ab = car_smax(A_wab)
    cov_ab = float(np.max(np.abs(A_wab[np.ix_(img, img)] - A_wab)))
    G_ab = grams(A_wab, SPEC_T)
    dev_ab = max(float(np.max(np.abs(G_ab[nm] - G0_T[nm])))
                 for nm in G0_T)
    hd_ab = max(float(np.max(np.abs(G_ab[nm]
                                    - G_ab[nm].conj().T)))
                for nm in G0_T)
    lm_ab = min(float(np.min(np.linalg.eigvalsh(
        (G_ab[nm] + G_ab[nm].conj().T) / 2))) for nm in G0_T)
    mix_ab = blocks_census(A_wab - A0)
    n_lit = sum(1 for v in mix_ab.values() if v >= NZ_FLOOR)
    ab_blk = mix_ab[(a_ch, b_ch)]
    gate("P4.1 witness W_ab (32-coordinate, theta_abT, MARGINAL)",
         smax_ab <= 1 - NZ_FLOOR and cov_ab == 0.0
         and dev_ab <= EXTOL and hd_ab <= EXTOL and lm_ab >= -ZTOL
         and n_lit == 14 and ab_blk == 0.0,
         "s = 1/32 on all 32 invisible dirs: CAR margin %.6f >= "
         "1e-8, covariance residual %.1f, complete theta_abT Gram "
         "== base (%.1e), Hermitian (%.1e), lam_min %.1e >= -ZTOL "
         "(ON-CONE marginal), mixing %d/15 duads lit, {%d,%d} "
         "block %.1f (exactly zero)"
         % (1 - smax_ab, cov_ab, dev_ab, hd_ab, lm_ab, n_lit,
            a_ch, b_ch, ab_blk))

    A_wS = A0 + S_WIT * M_J
    smax_S = car_smax(A_wS)
    cov_S = float(np.max(np.abs(A_wS[np.ix_(img, img)] - A_wS)))
    G_wS = grams(A_wS, SPEC_S)
    hd_wS = max(float(np.max(np.abs(G_wS[nm] - G_wS[nm].conj().T)))
                for nm in G0_S)
    lm_wS = min(float(np.min(np.linalg.eigvalsh(
        (G_wS[nm] + G_wS[nm].conj().T) / 2))) for nm in G0_S)
    aJ_wS = ((A_wS[np.ix_(CH[a_ch], CH[b_ch])][0, 1]
              - A_wS[np.ix_(CH[a_ch], CH[b_ch])][1, 0]) / 2)
    G_wS_T = grams(A_wS, SPEC_T)
    lm_wS_T = float(np.min(np.linalg.eigvalsh(
        (G_wS_T["odd1"] + G_wS_T["odd1"].conj().T) / 2)))
    gate("P4.2 witness W_S (pure a_J, theta_S, STRICT)",
         smax_S <= 1 - NZ_FLOOR and cov_S == 0.0
         and hd_wS <= NZ_FLOOR and lm_wS >= NZ_FLOOR
         and abs(aJ_wS - S_WIT) <= EXTOL
         and lm_wS_T <= -NZ_FLOOR,
         "s = 1/8 on the a_J direction: CAR margin %.6f, "
         "covariance %.1f, theta_S Hermitian %.1e <= 1e-8, "
         "lam_min %.6f >= 1e-8 (STRICT interior), a_J = %.6f; the "
         "SAME point is REJECTED by theta_abT (odd lam_min %.6f "
         "<= -1e-8): the exclusivity is REFLECTION-RELATIVE"
         % (1 - smax_S, cov_S, hd_wS, lm_wS, aJ_wS, lm_wS_T))

    A_w2 = A0 + S_WIT2 * M_vacJ
    smax_2 = car_smax(A_w2)
    cov_2 = float(np.max(np.abs(A_w2[np.ix_(img, img)] - A_w2)))
    G_w2 = grams(A_w2, SPEC_S)
    hd_w2 = max(float(np.max(np.abs(G_w2[nm] - G_w2[nm].conj().T)))
                for nm in G0_S)
    lm_w2 = min(float(np.min(np.linalg.eigvalsh(
        (G_w2[nm] + G_w2[nm].conj().T) / 2))) for nm in G0_S)
    mix_2 = blocks_census(A_w2 - A0)
    n_vac = sum(1 for (i, j), v in mix_2.items()
                if i == 0 and v >= NZ_FLOOR)
    gate("P4.3 witness W_S2 (vacuum-J wiring, theta_S, STRICT)",
         smax_2 <= 1 - NZ_FLOOR and cov_2 == 0.0
         and hd_w2 <= NZ_FLOOR and lm_w2 >= NZ_FLOOR
         and n_vac == 5,
         "s = 1/16 on the [J2;J2;J2] vacuum stack (the v911 pure-J "
         "coupling as a STATE direction): CAR margin %.6f, "
         "covariance %.1f, theta_S Hermitian %.1e, lam_min %.6f >= "
         "1e-8 (STRICT), vacuum duads lit %d/5"
         % (1 - smax_2, cov_2, hd_w2, lm_w2, n_vac))

    odd3_S = B1_S + [tuple(c)
                     for c in itertools.combinations(P_S, 3)]
    ev4_S = B2_S + [tuple(c)
                    for c in itertools.combinations(P_S, 4)]
    wkb = wick_factory(A0)
    Mo_b = gram(odd3_S, r_S, S_ONE, 1j, wkb)
    Me_b = gram(ev4_S, r_S, S_ONE, 1j, wkb)
    ho_b, lo_b = metrics(Mo_b)
    he_b, le_b = metrics(Me_b)
    wkw = wick_factory(A_wS)
    Mo_w = gram(odd3_S, r_S, S_ONE, 1j, wkw)
    Me_w = gram(ev4_S, r_S, S_ONE, 1j, wkw)
    ho_w = float(np.max(np.abs(Mo_w - Mo_w.conj().T)))
    he_w = float(np.max(np.abs(Me_w - Me_w.conj().T)))
    lo_w = float(np.min(np.linalg.eigvalsh(
        (Mo_w + Mo_w.conj().T) / 2)))
    le_w = float(np.min(np.linalg.eigvalsh(
        (Me_w + Me_w.conj().T) / 2)))
    gate("P4.4 deep sectors: base anchors (v903 R2.6) + W_S spot",
         abs(lo_b - 0.0987) <= 5e-3 and abs(le_b - 0.0456) <= 5e-3
         and ho_b <= ZTOL and he_b <= ZTOL
         and ho_w <= NZ_FLOOR and he_w <= NZ_FLOOR
         and lo_w >= NZ_FLOOR and le_w >= NZ_FLOOR,
         "base: odd deg<=3 lam_min %.6f (0.0987 +- 5e-3), even "
         "deg<=4 lam_min %.6f (0.0456 +- 5e-3), Hermitian (%.1e, "
         "%.1e); at W_S: Hermitian (%.1e, %.1e) <= 1e-8, lam_min "
         "(%.6f, %.6f) >= 1e-8 -- the strict witness survives the "
         "deep sectors" % (lo_b, le_b, ho_b, he_b, ho_w, he_w,
                           lo_w, le_w))

    # ==================================================================
    section("P6 -- negative controls (must fire)")
    # ==================================================================
    M_bad = np.zeros((16, 16))
    M_bad[CH[a_ch][0], CH[b_ch][0]] = 1.0
    M_bad[CH[b_ch][0], CH[a_ch][0]] = -1.0
    cov_bad = float(np.max(np.abs(M_bad[np.ix_(img, img)] - M_bad)))
    proj_bad = max(abs(float(np.sum(M_bad * basis[k][2])))
                   for k in range(33))
    gate("P6.1 CONTROL fires: non-covariant direction flagged",
         cov_bad >= 1.0 and proj_bad == 0.0,
         "E_{%d,%d} - E_{%d,%d} (the FORCED {%d,%d} diagonal): "
         "covariance residual %.1f >= 1, slice projection %.1f "
         "(exactly 0)" % (CH[a_ch][0], CH[b_ch][0], CH[b_ch][0],
                          CH[a_ch][0], a_ch, b_ch, cov_bad,
                          proj_bad))

    rng = np.random.default_rng(RNG_SEED)
    X = rng.standard_normal((16, 16))
    Xa = X - X.T
    A_bad = 1.5 * Xa / car_smax(Xa)
    smax_bad = car_smax(A_bad)
    gate("P6.2 CONTROL fires: non-admissible Gamma fails CAR",
         smax_bad >= 1.0,
         "seeded (seed %d) antisymmetric matrix scaled to spectral "
         "norm 3/2: smax = %.6f >= 1 => 0 <= Gamma <= I FAILS"
         % (RNG_SEED, smax_bad))

    # ==================================================================
    section("P7 -- mutants (must be CAUGHT) + joint adjudication")
    # ==================================================================
    A_dep_kms = A18
    wk_mut = wick_factory(A0)
    M1_unt = gram(B1_ab, r_ab, S_ONE, 1j, wk_mut)
    M2_unt = gram(B2_ab, r_ab, S_ONE, 1j, wk_mut)
    hd_unt = max(metrics(M1_unt)[0], metrics(M2_unt)[0])
    gate("P7.1 MUT-A CAUGHT: untwisted 2-cycle swap",
         hd_unt >= 0.3,
         "dropping the intra-pair twist (r_ab instead of r_abT): "
         "base Gram relative Hermiticity defect %.4f >= 0.3 -- the "
         "P1 anchor machinery rejects the mutated reflection"
         % hd_unt)

    hd_e1 = 0.0
    for spec in (SPEC_S, SPEC_T):
        Ge = grams(A_dep_kms, spec, eta=1.0)
        for nm in Ge:
            hd_e1 = max(hd_e1, metrics(Ge[nm])[0])
    gate("P7.2 MUT-B CAUGHT: twist eta = +1",
         hd_e1 >= 0.3,
         "max relative Hermiticity defect over both reflections at "
         "the deployed KMS point: %.4f >= 0.3 (the v519 twist is "
         "FORCED)" % hd_e1)

    Gm1 = grams(A0, SPEC_S, eta=-1j)
    lm_m1 = float(np.min(np.linalg.eigvalsh(
        (Gm1["odd1"] + Gm1["odd1"].conj().T) / 2)))
    gate("P7.3 MUT-C CAUGHT: twist eta = -i",
         lm_m1 <= -0.4,
         "theta_S odd base Gram flips negative: lam_min %.6f <= "
         "-0.4 (== -tanh(1/2))" % lm_m1)

    rows2 = census_pass()
    fp2 = hashlib.sha256(("|".join(
        "%d:%.12e:%.12e:%.12e" % (k, h1, h2, v)
        for (k, h1, h2, v, *_r) in rows2)).encode()).hexdigest()
    runtime = time.time() - T0
    gate("P7.4 determinism fingerprint + runtime",
         fp1 == fp2 and runtime < 180.0,
         "census fingerprint reproduces on a second pass "
         "(%s == %s: %s); runtime %.1f s < 180 s"
         % (fp1[:12], fp2[:12], fp1 == fp2, runtime))

    dim_T_adm = len(invis_idx)
    dim_S_neut = nulldim
    # witness validity flags (frozen rule)
    w_ab_valid = (smax_ab <= 1 - NZ_FLOOR and hd_ab <= EXTOL
                  and lm_ab >= -ZTOL and n_lit == 14)
    w_S_valid = (smax_S <= 1 - NZ_FLOOR and hd_wS <= NZ_FLOOR
                 and lm_wS >= NZ_FLOOR and abs(aJ_wS) >= NZ_FLOOR)
    w_S2_valid = (smax_2 <= 1 - NZ_FLOOR and hd_w2 <= NZ_FLOOR
                  and lm_w2 >= NZ_FLOOR and n_vac == 5)
    joint_all = (dim_T_adm == 32 and neutral_1 == [JDIR]
                 and w_S_valid)
    if w_ab_valid or w_S_valid or w_S2_valid:
        VERDICT = "RP_ADMITS_MIXING"
    elif dim_S_neut == 0 and dim_T_adm == 0:
        VERDICT = "RP_FORCES_DIAGONAL"
    else:
        VERDICT = "PARTIAL_RIGIDITY"
    gate("P7.5 joint adjudication (at-least-one-reflection OS)",
         w_ab_valid and w_S_valid and w_S2_valid and joint_all,
         "theta_abT admits the 32-dim {a_J = 0} hyperplane "
         "MARGINALLY (sector-complete window); theta_S admits a "
         "%d-dim first-order-neutral subspace with STRICT finite-s "
         "witnesses (incl. the a_J direction theta_abT kills); "
         "JOINTLY every one of the 33 coordinate directions is "
         "RP-compatible under >= 1 deployed reflection"
         % dim_S_neut)

    # ==================================================================
    section("REPORT (exploration only -- no promotion, no edits)")
    # ==================================================================
    print("""\
  * SLICE TESTED: the FULL 33-dim C6-covariant cross-block mixing
    slice of v896/v898 (24 vacuum C<->B + 9 carrier-carrier; the 2
    forced zeros excluded by the walk), base point A0 = tanh(1/2)
    A16_dep == the v898/v903 KMS state at (u=1, t=0, beta=1).
  * ANCHOR (P1): the v903 exclusivity reproduces exactly -- odd-
    sector theta_abT Gram eigenvalues == +-|a_J| (worst identity
    defect %.1e); strict RP on the v898 ray forces the mixing floor
    to fall; theta_S even-sector defect at the deployed point %.4f.
  * THE CENSUS: theta_abT (sector-COMPLETE, 4 monomials): its Gram
    is a 2-channel window seeing ONLY the {%d,%d}-J coordinate a_J:
    1/33 direction KILLED (PSD1 odd eigs +-s exactly; PSD2 even
    kernel value -1/(1+c^2)), 32/33 IDENTICALLY INVISIBLE => the
    theta_abT-RP region within the slice is EXACTLY the hyperplane
    {a_J = 0} (marginal, on-cone).  theta_S (deg <= 2 sectors +
    deg <= 4 spots): %d/33 COORDINATE directions KILLED-HERM1 at
    first order and only a_J basis-aligned neutral, but the defect
    map has rank %d: the first-order-neutral SUBSPACE is %d-dim and
    consists of intra-family COMBINATIONS (J/Z-type recombinations;
    the v911 kernel-12 transported to the state slice), NO second-
    order kill on it, finite-s RP windows on all probed neutral
    directions (a_J windows %.3f/%.3f).
  * WITNESSES: W_ab (32 coords at s=1/32, 14/15 duads lit, CAR
    margin %.4f, theta_abT-marginal lam_min %.1e); W_S (pure a_J at
    s=1/8: theta_S STRICT lam_min %.4f incl. deep sectors %.4f/%.4f
    -- the SAME point theta_abT rejects at lam_min %.4f); W_S2
    (vacuum-J wiring at s=1/16: theta_S STRICT lam_min %.4f, 5/5
    vacuum duads).
  * THE ANSWER TO THE ROUND QUESTION: RP + C6-covariance do NOT
    force the channel-diagonal point.  The RP region is NOT
    {theta-odd coordinates = 0} (theta_abT parity has %d odd dims
    but kills exactly 1): each reflection carves only the slice
    coordinates its half-side Gram can SEE, and the two deployable
    reflections see complementary windows; the v903 exclusivity is
    a statement about the v898 RAY (all coordinates move together),
    not about the slice.  Rigidity found: PARTIAL and reflection-
    relative -- hence the honest enum below.
  * LIMITATIONS: theta_S sector-truncated (deg <= 2 + deg <= 4
    spots, not the full 256-monomial algebra); theta_abT
    invisibility = RP-SILENT beyond its window, not certified
    positivity; coordinate-direction census + 2 named combination
    witnesses, not the full 33-dim region geometry; float64 at the
    v903 exploration grade; the v898/v903 [O] premise UNMOVED.
""" % (worst_id, hd_dep, a_ch, b_ch, len(killed_H1),
       rank, nulldim,
       win_tab[0][1], win_tab[0][2], 1 - smax_ab, lm_ab, lm_wS,
       lo_w, le_w, lm_wS_T, lm_w2, nmin_T))

    n_ok = sum(GATES)
    n_tot = len(GATES)
    if n_ok == n_tot:
        print("ALL GATES PASSED %d/%d" % (n_ok, n_tot))
    else:
        print("GATES PASSED %d/%d (FAILURES PRESENT)"
              % (n_ok, n_tot))
    print("VERDICT: %s [theta_abT: 32-dim marginal {a_J = 0}; "
          "theta_S: %d-dim neutral subspace, strict witnesses; "
          "joint: 33/33 directions admitted by >= 1 reflection]"
          % (VERDICT, dim_S_neut))
    print("SPEC_SHA = %s" % spec_sha[:16])
    print("runtime: %.1f s" % (time.time() - T0))
    return 0 if n_ok == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
