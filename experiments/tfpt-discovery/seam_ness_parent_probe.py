#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_ness_parent_probe -- SEAM.CFIN.NESS.PARENT.01
(EXPLORATION ONLY, experiments/; round 60, 2026-08-10, Probe 10 --
named in round 59, built here for the STRICT route: does the
strict-collar (sheet-swap theta_S) mixing need a NESS parent --
two reservoirs, positive entropy production -- or is the round-59
family obstruction cheaper to dissolve?)

THE QUESTION.  Probe 7 (rp_parent_dilation_probe; promoted in
v903) measured the strict-collar route EXACTLY OBSTRUCTED on the
five-parameter family: 30 deg-2 Gram Hermiticity defect entries,
all of magnitude 2t, linear in the coupling.  Round 59 named the
NESS-parent test: construct two-reservoir / two-temperature (or
modular-drive) quasi-free parents on the 10 (+) 6 split with
C6-covariant coupling, define what RP can mean for a NESS, and
measure the minimal entropy production at which the mixing gates
open ('the price of the mixing'), typing FORCED / TRADE-OFF /
IMPOSSIBLE.

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-10): probe 7 scanned ONLY the deployed coupling direction
t1 W1 + t2 W2 (the A_int rows) and typed the obstruction 'a
measurement on THIS parametrized family, not a universal no-go';
v898 counts the covariant C<->B mixing block at 24 dimensions but
never intersects it with RP; round 58 deployed theta_S but only on
the KMS family; NOTHING in the corpus (a) writes the Hermiticity
defect as a LINEAR functional of the coupling, (b) scans the FULL
24-dim covariant coupling space against it, or (c) constructs
driven/two-temperature parents.  That is exactly this probe.

SMOKE-RUN DISCLOSURE (2026-08-10, declared smoke rounds before
freezing; the smoke INVERTED the working hypothesis and the frozen
claims record what was measured -- fail-first preserved):
 (i)   THE TWO-SEAT LINEAR LAW: strict theta_S Hermiticity is
       obstructed at LINEAR order by exactly two families of
       entries -- the 1p seat A_{a+1, b} + A_{a, b+1} (a in C,
       b in B, both even; kills the X sub-block coordinates of
       the coupling) and the deg-2 (empty <-> mixed-pair) seat
       A_{a, b} + A_{a+1, b+1} (kills the I coordinates); on the
       24-dim covariant coupling space the combined law has rank
       12, kernel 12 = the {J, Z} sub-block coordinates;
 (ii)  the DEPLOYED coupling V = A_int[C, B] has every 2x2
       sub-block EXACTLY -I2: it is PURE-I, i.e. it lies entirely
       in the defect row space -- the deployed seam wiring is a
       maximally strict-collar-obstructed covariant direction
       (this explains the round-59 '30 entries, magnitude 2t'
       law: 15 mixed pairs x 2 Gram positions, defect 2t each);
 (iii) THE INVERSION: the kernel contains EQUILIBRIUM witnesses.
       The uniform J-coupling parent (kappa = m = 1/2, t = 1/20)
       passes STRICT theta_S RP (exactly Hermitian Grams, PD)
       while its Schur compression carries the FULL canonical
       Pfaffian mixing with S_J = V_J J3 V_J^T = 3J on ALL 25
       channel blocks and the {4,5} J-coordinate EXACTLY
       t^2 3m/(1-m^2) = 1/200 -- the same rational identity as
       the deployed-direction witness; the uniform Z-coupling is
       a second witness (S_Z = -3J, J-coordinate -1/200).  So the
       minimal entropy production at which the mixing gates open
       is ZERO: no NESS is needed;
 (iv)  the kernel is NOT sufficient: the uniform X-coupling is
       covariant but fails at the 1p seat (raw defect exactly
       2t = 0.1), and J/Z-MIXTURES pass Hermiticity + PD but
       break the canonical SIGN census (4/10) -- the canonical
       gate selects the uniform J (or Z) ray;
 (v)   the NESS side collapses honestly at finite size: an
       exactly stationary quasi-free state has [h, A] = 0, hence
       every block flux Phi_r = (1/4) tr(h0_r [h, A]) vanishes
       and sigma = sum_r beta_r Phi_r == 0 -- positive entropy
       production is CATEGORY-INAPPLICABLE to a finite stationary
       state; the two-temperature Cesaro (dephasing) states are
       stationary, covariant, CAR-valid, carry the 15/15 block
       mixing ALREADY AT ZERO DRIVE, keep the Hermiticity defect
       PINNED near the deployed-direction value (0.0982-0.1062)
       and only DEGRADE the hermitized PSD margin as the drive
       grows (0.1884 -> 0.0155): drive buys NO RP;
 (vi)  transient entropy production from the product initial
       state is exactly 0 at t = 0 (block-diagonal initial state,
       off-diagonal commutator), positive through t ~ 2
       (sigma(1) = 0.0626 at beta_C = 1, beta_B = 1/4), and
       oscillates in sign later (finite recurrence -- no true
       NESS at finite size; typed, not hidden).

CONVENTIONS (probe 7 / round 58 wiring rebuilt inline; READ-ONLY
import of tfpt_constants): 16-dim Majorana space, carrier C = 0..9
(channels 1..5), boundary B = 10..15; A_CC = (+)_5 J, J3 =
A16_dep[B, B]; coupled parents A_parV(kappa, m, t, V) =
[[kappa A_CC, t V], [-t V^T, m J3]]; theta_S = sheet swap
(eta = +i), sector Grams 1p (8 half-side Majoranas) + even deg-2
(29 monomials), strict RP = Hermiticity <= ZTOL and lam_min >=
-NZ_FLOOR in both sectors (sector statement, probe-7 convention).
Covariant coupling space = fixed points of V -> O_C V O_B^T
(integer orbit sums).  Compression + census: probe-7 form
(A_eff, 10 carrier duads, canonical Pf4 signs); state-level
census: v898 12-dim Iota/3 compression, 15 duads.  ENTROPY
PRODUCTION (documented formula): with h = h0 + coupling split
h0 = h_C (+) h_B, H_r = (i/4) sum_{ij in r} h0_ij c_i c_j,
E_r(A) = <H_r> = (1/4) tr(h0_r A), Phi_r(A) = dE_r/dt =
(1/4) tr(h0_r [h, A]), sigma = beta_C Phi_C + beta_B Phi_B;
dynamics A(t) = e^{th} A e^{-th} (dA/dt = [h, A]); total-energy
identity tr(h [h, A]) == 0 (cyclic).  Two-temperature parents:
A_0(beta_C, beta_B) = KMS_{beta_C}(h_C) (+) KMS_{beta_B}(h_B);
NESS analogue = the Cesaro / dephasing average of A_0 over the
spectrum of the coupled h (the long-time average, exactly
stationary).  RP FOR A NESS (defined per the round-59 demand):
strict RP is category-inapplicable to 'stationary + positive
entropy production' at finite size (P4.1 proves sigma == 0 for
stationary states), so the weakest meaningful positivity is RP of
the TIME-ZERO (stationary) covariance -- that is what is tested.
NUMERICAL PROTOCOL (declared): the two-seat law, its rank/kernel,
the deployed-coupling decomposition, the witnesses (Grams, LDL,
Schur, census) are EXACT (integer/rational sympy); drive scans and
transients are float64 with frozen tolerances; RNG only in
controls.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 P1  THE TWO-SEAT LINEAR LAW (exact).
     (a) CLOSED FORMS warded against the Gram machinery (float
         <= 1e-12 on unit couplings): the 1p Gram Hermiticity
         defect entries are (M1 - M1+)_{xy} = -(A_{x+1, y} +
         A_{x, y+1}) for even x != y in the half-side basis, and
         the deg-2 (empty <-> pair) defect entries are
         i (A_{x, y} + A_{x+1, y+1});
     (b) the covariant coupling space has dimension EXACTLY 24
         (integer orbit-sum basis; the v898 T-count); the combined
         two-seat law on it has EXACT rank 12 and kernel dimension
         12; coordinate identification (exact, uniform unit
         couplings): I -> deg-2 seat fires, 1p clean; X -> 1p
         seat fires, deg-2-empty clean; J and Z -> BOTH seats
         clean;
     (c) the DEPLOYED coupling V = A_int[C, B] has every 2x2
         sub-block EXACTLY -I2 (integer): PURE-I, entirely inside
         the defect row space; its parent reproduces the probe-7
         law (raw deg-2 empty-seat defect 2t = 0.1, 30 entries).
 P2  THE EQUILIBRIUM WITNESS (exact rationals end to end -- the
     answer to the NESS question).
     (a) V_J (J on all 15 sub-blocks) is exactly covariant and in
         the kernel; the parent A_J(1/2, 1/2, 1/20) is CAR-strict
         (smax = 0.694 +- 0.005 < 0.95) and by the artanh theorem
         a beta = 1 KMS state of a covariant Hamiltonian
         (round-trip ward <= 1e-12): EQUILIBRIUM, sigma = 0;
     (b) STRICT theta_S RP PASSES EXACTLY: 1p and deg-2 Grams
         exactly Hermitian (sympy) and PD by exact LDL pivots;
         float lam_min = 0.3064 +- 0.005 (1p) and 0.1532 +- 0.005
         (deg-2);
     (c) the compression carries the FULL canonical mixing:
         S_J := V_J J3 V_J^T = 3J on ALL 25 channel blocks
         (integer identity); A_eff = kappa A_CC + (m/(1-m^2)) t^2
         S_J (symbolic Schur identity in kappa, m, t); every
         carrier duad block EXACTLY (3 m t^2/(1-m^2)) J with
         J-coordinate = 1/200 at the witness (the round-51/52
         floor as the SAME exact fraction), per-edge Pf4 < 0
         canonical on 10/10, compressed CAR valid;
     (d) V_Z is a SECOND exact witness: S_Z = -3J uniform
         (integer), strict theta_S RP passes (float lam_min
         0.2383 +- 0.005), J-coordinate EXACTLY -1/200, Pf4
         canonical 10/10;
     (e) the 2-cycle side is UNTOUCHED: theta_abT stays marginal
         at the V_J witness (1p Gram identically 0, exact) and
         the compressed state fails effective 2-cycle RP with odd
         eigenvalues exactly -+1/200 -- the strict-collar gate
         opens while the round-58 2-cycle exclusion stands.
 P3  KERNEL != SUFFICIENT (the honest boundary of the win).
     (a) the uniform X-coupling (in NO seat... in the covariant
         space but OUTSIDE the kernel) fails at the 1p seat with
         raw defect EXACTLY 2t = 0.1 (empty deg-2 seat clean
         <= 1e-14, pair-pair defect 0.05 +- 0.005): the law is
         sharp in both directions;
     (b) J/Z-MIXTURES (frozen members: J-on-2-cycle/Z-on-3-cycle;
         mixed amplitudes) pass exact Hermiticity and PD but the
         canonical SIGN census drops to 4/10: the canonical gate
         selects the uniform J (or uniform Z) ray -- Hermiticity
         kernel and canonical-mixing ray are DIFFERENT strata
         (typed);
     (c) orbit selectivity in the kernel (regression of probe-7
         P2.4): J-on-2-cycle-orbit only mixes 1/10, J-on-3-cycle
         only 3/10, single-boundary-pair J (both orbits) 10/10
         with J-coordinate EXACTLY lam t^2 = 1/600;
     (d) amplitude anatomy (report, not gate): uniform J passes
         at t = 1/10 (lam_min 0.056, smax 0.887), t >= 0.15 is
         CAR-invalid (smax > 1).
 P4  THE NESS SIDE (constructed; the exact no-go + the price
     curve).
     (a) FINITE-NESS-NOGO (exact): stationarity [h, A] = 0
         implies EVERY block flux Phi_r = (1/4) tr(h0_r [h, A])
         = 0, hence sigma == 0 IDENTICALLY: 'NESS with positive
         entropy production' is category-inapplicable at this
         finite size; the total-energy identity tr(h [h, A]) == 0
         holds exactly (cyclic; float ward <= 1e-12); the weakest
         meaningful positivity = RP of the stationary covariance
         (tested in (c));
     (b) the two-temperature Cesaro states on the frozen drive
         grid (beta_C, beta_B) in {(1, 1), (1, 1/2), (1, 1/4),
         (2, 1/2)} at the deployed h(1, 1/8): exactly stationary
         (<= 1e-12), real antisymmetric, C6-covariant, CAR-valid
         (smax <= 0.85); the t = 0 fluxes from the product
         initial state vanish EXACTLY (<= 1e-14); the transient
         sigma(t) at (1, 1/4) is positive at t = 1 (0.0626 +-
         0.01) and NEGATIVE at t = 4 (finite recurrence, typed:
         no true NESS at finite size);
     (c) THE PRICE CURVE IS FLAT-OPEN: the state-level mixing
         census is 15/15 canonical at EVERY drive point INCLUDING
         zero drive; the strict theta_S Hermiticity defect stays
         PINNED (0.0982 +- 0.005 at the three beta_C = 1 points,
         0.1062 +- 0.005 at (2, 1/2)) and the hermitized PSD
         margin DEGRADES monotonically with the drive (0.1884 ->
         0.0600 -> 0.0155 along beta_B = 1 -> 1/2 -> 1/4): the
         minimal entropy production at which the mixing gates
         open is EXACTLY ZERO, and drive buys NO RP;
     (d) TYPED CONCLUSION (the round-59 enum): NESS-NOT-FORCED --
         the strict-collar mixing needs the coupling DIRECTION
         (the two-seat kernel), which is equilibrium-compatible;
         the round-59 obstruction is DIRECTION-level (the
         deployed PURE-I wiring), not equilibrium-level; on this
         tested class a NESS is neither forced nor helpful.
 C   CONTROLS (must fire; frozen fire rules; RNG only in C2).
     C1 ZERO-DRIVE REGRESSION: the global KMS state (u = 1,
        t = 1/8, beta = 1) is exactly stationary and FAILS strict
        theta_S with Hermiticity defect 0.0982 +- 0.005 (the
        round-58/59 equilibrium obstruction reproduced);
     C2 SEEDED SCRAMBLE (rng 904, 3 draws: random row permutation
        of V_J): breaks the exact C6-covariance ward on 3/3 AND
        breaks the canonical Pfaffian census on 3/3 (sign census
        <= 1/10; the Hermiticity defect also switches ON, 0.1);
     C3 DEPLOYED-COUPLING REGRESSION: the PURE-I parent (V = the
        deployed -I2 wiring, kappa = m = 1/2, t = 1/20) fails
        strict theta_S with raw empty-seat defect 2t = 0.1 and
        exactly 30 defect entries (probe-7 law);
     C4 I-ORBIT SWITCH-ON: adding one covariant I-orbit direction
        to V_J turns the deg-2 empty-seat defect ON (raw defect
        > 0.01) while covariance stays EXACT -- the law bites
        inside the covariant class.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 two-seat law / rank / deployed decomposition -> LAW-BROKEN
  K2 equilibrium witness ward breaks             -> WITNESS-BROKEN
  K3 kernel honesty ward breaks                  -> KERNEL-BROKEN
  K4 NESS construction / no-go / price ward      -> NESS-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): NESSPARENT-MEASURED [PRICE-ZERO(equilibrium
strict-collar witnesses V_J / V_Z: exact Hermitian + PD + 10/10
canonical + J-coordinate +-1/200), TWO-SEAT-LAW(rank 12, kernel 12
= the {J, Z} coordinates; deployed coupling PURE-I),
CANONICAL-SELECTS-UNIFORM-RAY(mixtures 4/10),
FINITE-NESS-NOGO(stationary => sigma == 0, exact),
DRIVE-RP-NEUTRAL(defect pinned, margin degrades, gates open at
zero drive), NESS-NOT-FORCED] / PIPELINE-BROKEN / LAW-BROKEN /
WITNESS-BROKEN / KERNEL-BROKEN / NESS-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the equilibrium witnesses are
CANDIDATE parents on a DIFFERENT covariant coupling direction than
the deployed A_int wiring -- whether the actual seam allows that
direction is untouched; the finite-NESS no-go is a finite-size
statement, not a claim about infinite-volume NESS; RP remains
sector-typed; the v898/v903 [O] premise is unmoved; no marker
moves.  NO RH claim.

SPEC v1 (2026-08-10): frozen after the declared smoke rounds; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline): rp_parent_dilation_
probe (probe 7: family, strict-collar obstruction, census),
seam_state_derivation_probe (round 58: theta_S, RP machinery),
v903_seam_rp_exclusion (promoted composite), v898_kms_schur_mixing
(24-dim T-count, state gates), v519 (RP Gram + twist),
tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_ness_parent_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import numpy as np
import sympy as sp

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

NZ_FLOOR = 1e-8
ZTOL = 1e-10
PF_FLOOR = 1e-16


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
CAR_DUADS = sorted(itertools.combinations(range(1, 6), 2))

PAULI = {"I": np.eye(2), "J": np.array([[0., 1.], [-1., 0.]]),
         "X": np.array([[0., 1.], [1., 0.]]),
         "Z": np.array([[1., 0.], [0., -1.]])}


def main():
    print("SEAM.CFIN.NESS.PARENT.01 -- the price of the "
          "strict-collar mixing: NESS parents vs the coupling "
          "direction")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (probe 7 rebuilt)")
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
    QSTAR = cand[0] if cand else None
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
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
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
    check("S0.1 compiler rebuilt: unique q*, |Aut| = %d == 6, "
          "generator pin unique" % len(AUT),
          ok_ref and len(cand) == 1 and ok_phi and len(AUT) == 6
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
    THREE = sorted(next(c for c in cycles if len(c) == 3))
    a_ch, b_ch = TWO
    check("S0.2 deployed pi = %s, cycle type %s == (1, 2, 3); "
          "2-cycle {%d,%d}, 3-cycle %s"
          % (PI6, cycle_type(PI6), a_ch, b_ch, THREE),
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

    J2i = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    I2i = np.eye(2, dtype=np.int64)
    IOTA6i = np.vstack([I2i, I2i, I2i])
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
        B = J2i if rev else (IOTA6i if i == 0 else I2i)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    A16_dep = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    okA = (np.array_equal(A_int[np.ix_(img, img)], A_int)
           and np.array_equal(A_int, -A_int.T))
    okD = np.array_equal(A16_dep[np.ix_(img, img)], A16_dep)

    A_CC = A16_dep[np.ix_(CAR_IDX, CAR_IDX)]
    J3 = A16_dep[np.ix_(BND_IDX, BND_IDX)]
    Vc = A_int[np.ix_(CAR_IDX, BND_IDX)]
    check("S0.3 blocks extracted: A_CC = (+)_5 J, J3, deployed "
          "coupling V = A_int[C, B]", okA and okD, kill="K0")

    O16 = np.zeros((16, 16), dtype=np.int64)
    for src in range(16):
        O16[img[src], src] = 1
    O_C = O16[np.ix_(CAR_IDX, CAR_IDX)]
    O_B = O16[np.ix_(BND_IDX, BND_IDX)]

    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}
    IOTA_f = IOTA6i.astype(np.float64)

    def compress12(A):
        Ahat = np.zeros((12, 12))
        for (i, j) in DUADS_CH:
            if i == 0:
                B = IOTA_f.T @ A[np.ix_(CH[0], CH[j])] / 3.0
            else:
                B = A[np.ix_(CH[i], CH[j])]
            for rr in range(2):
                for cc in range(2):
                    Ahat[CH2[i][rr], CH2[j][cc]] = B[rr, cc]
                    Ahat[CH2[j][cc], CH2[i][rr]] = -B[rr, cc]
        return Ahat

    def pf4_of(Ahat):
        out = {}
        for (i, j) in DUADS_CH:
            B = Ahat[np.ix_(CH2[i], CH2[j])]
            out[frozenset({i, j})] = -(B[0, 0] * B[1, 1]
                                       - B[0, 1] * B[1, 0])
        return out

    pf4_c = pf4_of(compress12(A_int.astype(np.float64) / 200.0))
    sign_c = {d: (1 if v > 0 else -1) for d, v in pf4_c.items()}
    check("S0.4 canonical G_c Pf4 signs rebuilt: 15 nonzero, all "
          "negative", all(abs(v) > PF_FLOOR for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ---------------- RP machinery (v519 / probe-7 form)
    def wick_factory(A):
        n = A.shape[0]
        W = np.eye(n, dtype=complex) + 1j * A
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

    def gram(basis, r, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis):
            imgs = [r[a] for a in reversed(ma)]
            coeff = eta ** len(ma)
            lst = list(imgs)
            sgn = 1
            for i in range(len(lst)):
                for j in range(len(lst) - 1 - i):
                    if lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                        sgn = -sgn
            ca = coeff * sgn
            ia = tuple(lst)
            for bi, mb in enumerate(basis):
                M[ai, bi] = ca * wick(tuple(list(ia) + list(mb)))
        return M

    def metrics(M):
        nm = max(float(np.max(np.abs(M))), 1e-300)
        hd = float(np.max(np.abs(M - M.conj().T)) / nm)
        lm = float(np.min(np.linalg.eigvalsh((M + M.conj().T) / 2)))
        return hd, lm

    r_S = {}
    for i in range(8):
        r_S[2 * i] = 2 * i + 1
        r_S[2 * i + 1] = 2 * i
    P_S = [2 * i for i in range(8)]
    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]

    r_abT = {k: k for k in range(16)}
    for k in range(2):
        r_abT[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_abT[CH[b_ch][k]] = CH[a_ch][1 - k]
    B1_ab = [(a,) for a in CH[a_ch]]
    B2_ab = [(), tuple(CH[a_ch])]

    def strict_S(A):
        wk = wick_factory(A)
        M1 = gram(B1_S, r_S, 1j, wk)
        M2 = gram(B2_S, r_S, 1j, wk)
        hd = max(metrics(M1)[0], metrics(M2)[0])
        lm = min(metrics(M1)[1], metrics(M2)[1])
        ok = (hd <= ZTOL and lm >= -NZ_FLOOR)
        return ok, hd, lm, (M1, M2)

    A_CCf = A_CC.astype(np.float64)
    J3f = J3.astype(np.float64)

    def parentV(kap, m, tt, V):
        A = np.zeros((16, 16))
        A[np.ix_(CAR_IDX, CAR_IDX)] = kap * A_CCf
        A[np.ix_(BND_IDX, BND_IDX)] = m * J3f
        A[np.ix_(CAR_IDX, BND_IDX)] = tt * V
        A[np.ix_(BND_IDX, CAR_IDX)] = -tt * V.T
        return A

    def schur_Aeff(A):
        C = (np.eye(16, dtype=complex) + 1j * A) / 2
        CCC = C[np.ix_(CAR_IDX, CAR_IDX)]
        CCB = C[np.ix_(CAR_IDX, BND_IDX)]
        CBB = C[np.ix_(BND_IDX, BND_IDX)]
        CBC = C[np.ix_(BND_IDX, CAR_IDX)]
        Ceff = CCC - CCB @ np.linalg.inv(CBB) @ CBC
        return 2 * Ceff.imag

    def census10(Aeff):
        n_nz, n_sig = 0, 0
        aJ45 = 0.0
        for (i, j) in CAR_DUADS:
            B = Aeff[np.ix_(CH[i], CH[j])]
            n_nz += float(np.linalg.norm(B)) >= NZ_FLOOR
            pf = -(B[0, 0] * B[1, 1] - B[0, 1] * B[1, 0])
            if abs(pf) >= PF_FLOOR:
                n_sig += ((pf > 0) == (sign_c[frozenset({i, j})] > 0))
            if (i, j) == (a_ch, b_ch):
                aJ45 = (B[0, 1] - B[1, 0]) / 2
        return n_nz, n_sig, aJ45

    def cov_defect(A):
        return float(np.max(np.abs(A[np.ix_(img, img)] - A)))

    def mkV(spec):
        V = np.zeros((10, 6))
        for (orb, s), (nm, amp) in spec.items():
            chans = [a_ch, b_ch] if orb == "two" else THREE
            for c in chans:
                V[2 * (c - 1):2 * c, 2 * s:2 * s + 2] = \
                    amp * PAULI[nm]
        return V

    V_J = mkV({(o, s): ("J", 1.0) for o in ("two", "three")
               for s in range(3)})
    V_Z = mkV({(o, s): ("Z", 1.0) for o in ("two", "three")
               for s in range(3)})
    V_X = mkV({(o, s): ("X", 1.0) for o in ("two", "three")
               for s in range(3)})

    # ==================================================================
    section("P1 -- the two-seat linear law (exact)")
    # ==================================================================
    # (a) closed-form ward on two unit couplings
    ok_cf = True
    for (r0, b0) in ((0, 0), (7, 3)):
        Vu = np.zeros((10, 6))
        Vu[r0, b0] = 1.0
        A = parentV(0.5, 0.5, 1.0, Vu)
        _ok, _hd, _lm, (M1, M2) = strict_S(A)
        D1 = M1 - M1.conj().T
        for xi, x in enumerate(P_S):
            for yi, y in enumerate(P_S):
                if x == y:
                    continue
                pred = -(A[x + 1, y] + A[x, y + 1])
                ok_cf &= abs(D1[xi, yi] - pred) <= 1e-12
        D2 = M2 - M2.conj().T
        for mi, mono in enumerate(B2_S):
            if len(mono) != 2:
                continue
            x, y = mono
            if (x < 10) == (y < 10):
                continue
            pred = 1j * (A[x, y] + A[x + 1, y + 1])
            ok_cf &= abs(D2[0, mi] - pred) <= 1e-12
    check("P1.1 CLOSED FORMS warded against the Gram machinery on "
          "unit couplings: 1p seat (M1 - M1+)_{xy} = -(A_{x+1,y} + "
          "A_{x,y+1}); deg-2 empty seat i (A_{x,y} + A_{x+1,y+1}) "
          "(<= 1e-12)", ok_cf, kill="K1")

    # (b) covariant basis + exact rank
    seen_o = set()
    cov_basis = []
    for r in range(10):
        for b in range(6):
            v0 = np.zeros((10, 6))
            v0[r, b] = 1.0
            w = np.zeros((10, 6))
            cur = v0
            for _k in range(6):
                w += cur
                cur = O_C.astype(float) @ cur @ O_B.astype(float).T
            key = tuple(np.flatnonzero(w.flatten() > 0.5).tolist())
            if key in seen_o or not key:
                continue
            seen_o.add(key)
            cov_basis.append(np.rint(w).astype(np.int64))
    rows = []
    mixed_ee = [(x, y) for x in P_S if x < 10
                for y in P_S if y >= 10]
    for w in cov_basis:
        r2 = [int(w[x, y - 10] + w[x + 1, y - 9])
              for (x, y) in mixed_ee]
        r1 = [int(w[x + 1, y - 10] + w[x, y - 9])
              for (x, y) in mixed_ee]
        rows.append(r2 + r1)
    Lmat = sp.Matrix(rows).T
    rkL = Lmat.rank()
    seat_id_ok = True
    for nm, Vt, fire1, fire2 in (("I", mkV({(o, s): ("I", 1.0)
                                            for o in ("two", "three")
                                            for s in range(3)}),
                                  False, True),
                                 ("X", V_X, True, False),
                                 ("J", V_J, False, False),
                                 ("Z", V_Z, False, False)):
        d2v = max(abs(Vt[x, y - 10] + Vt[x + 1, y - 9])
                  for (x, y) in mixed_ee)
        d1v = max(abs(Vt[x + 1, y - 10] + Vt[x, y - 9])
                  for (x, y) in mixed_ee)
        seat_id_ok &= ((d1v > 0.5) == fire1 and (d2v > 0.5) == fire2)
    check("P1.2 the covariant coupling space has dim %d == 24 (v898 "
          "T-count); the combined two-seat law has EXACT rank %d "
          "== 12, kernel dim 12 = the {J, Z} coordinates (I fires "
          "deg-2 only, X fires 1p only, J/Z clean: %s)"
          % (len(cov_basis), rkL, seat_id_ok),
          len(cov_basis) == 24 and rkL == 12 and seat_id_ok,
          kill="K1")

    ok_pureI = all(np.array_equal(
        Vc[2 * i:2 * i + 2, 2 * s:2 * s + 2],
        -np.eye(2, dtype=np.int64))
        for i in range(5) for s in range(3))
    A_dep_par = parentV(0.5, 0.5, 0.05, Vc.astype(float))
    okD, hdD, lmD, (M1D, M2D) = strict_S(A_dep_par)
    D2D = M2D - M2D.conj().T
    n_def = int(np.sum(np.abs(D2D) > 1e-12))
    raw_def = float(np.max(np.abs(D2D)))
    check("P1.3 the DEPLOYED coupling is PURE-I (every 2x2 "
          "sub-block exactly -I2: %s) -- entirely inside the "
          "defect row space; its parent fails strict theta_S with "
          "raw empty-seat defect %.4f == 2t = 0.1 and %d == 30 "
          "defect entries (probe-7 law reproduced)"
          % (ok_pureI, raw_def, n_def),
          ok_pureI and (not okD) and abs(raw_def - 0.1) <= 1e-12
          and n_def == 30, kill="K1")

    # ==================================================================
    section("P2 -- the equilibrium witness (exact rationals)")
    # ==================================================================
    A_Jf = parentV(0.5, 0.5, 0.05, V_J)
    smaxJ = float(np.max(np.abs(np.linalg.eigvalsh(1j * A_Jf))))
    wA, QA = np.linalg.eigh(1j * A_Jf)
    w_h = -2.0 * np.arctanh(wA)
    H_herm = (QA * w_h) @ QA.conj().T
    h_r = H_herm.imag
    occ = 1.0 / (1.0 + np.exp(w_h))
    A_back = (-1j * (2 * (QA * occ) @ QA.conj().T
                     - np.eye(16))).real
    rt = float(np.max(np.abs(A_back - A_Jf)))
    h_cov = float(np.max(np.abs(h_r[np.ix_(img, img)] - h_r)))
    check("P2.1 the V_J parent (1/2, 1/2, 1/20) is covariant "
          "(defect %.1e), CAR-strict (smax %.4f = 0.694 +- 0.005 "
          "< 0.95) and a beta = 1 KMS state of a covariant "
          "Hamiltonian (artanh round-trip %.1e, h covariant %.1e "
          "<= 1e-12): EQUILIBRIUM, sigma = 0"
          % (cov_defect(A_Jf), smaxJ, rt, h_cov),
          cov_defect(A_Jf) <= ZTOL and abs(smaxJ - 0.694) <= 5e-3
          and rt <= 1e-12 and h_cov <= 1e-12, kill="K2")

    def wick_exact_factory(Aex):
        n = Aex.shape[0]
        Wm = sp.eye(n) + sp.I * Aex
        memo = {}

        def wick(idx):
            idx = tuple(idx)
            if len(idx) == 0:
                return sp.Integer(1)
            if len(idx) % 2 == 1:
                return sp.Integer(0)
            if idx in memo:
                return memo[idx]
            head, rest = idx[0], idx[1:]
            tot = sp.Integer(0)
            for j, b in enumerate(rest):
                w = Wm[head, b]
                if w != 0:
                    sub = rest[:j] + rest[j + 1:]
                    tot += sp.Integer(-1) ** j * w * wick(sub)
            memo[idx] = tot
            return tot
        return wick

    def gram_exact(basis, r, eta, wick):
        n = len(basis)
        M = sp.zeros(n, n)
        for ai, ma in enumerate(basis):
            imgs = [r[a] for a in reversed(ma)]
            coeff = eta ** len(ma)
            lst = list(imgs)
            sgn = 1
            for i in range(len(lst)):
                for j in range(len(lst) - 1 - i):
                    if lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                        sgn = -sgn
            ca = coeff * sgn
            ia = tuple(lst)
            for bi, mb in enumerate(basis):
                M[ai, bi] = sp.expand(
                    ca * wick(tuple(list(ia) + list(mb))))
        return M

    def herm_exact(M):
        return sp.expand(M - M.conjugate().T) == sp.zeros(*M.shape)

    def psd_exact(M):
        n = M.shape[0]
        M = sp.Matrix(M)
        pivots = []
        for k in range(n):
            d = sp.nsimplify(sp.re(M[k, k]))
            pivots.append(d)
            if d == 0:
                if any(sp.expand(M[k, j]) != 0 for j in range(k, n)):
                    return False, pivots
                continue
            if d < 0:
                return False, pivots
            for i in range(k + 1, n):
                if M[i, k] != 0:
                    f = M[i, k] / d
                    for j in range(k, n):
                        M[i, j] = sp.expand(M[i, j] - f * M[k, j])
        return True, pivots

    def exact_parent(kapQ, mQ, tQ, Vint):
        A_ex = sp.zeros(16)
        for r in range(10):
            for c in range(10):
                A_ex[r, c] = kapQ * sp.Integer(int(A_CC[r, c]))
        for r in range(6):
            for c in range(6):
                A_ex[10 + r, 10 + c] = mQ * sp.Integer(int(J3[r, c]))
        for r in range(10):
            for c in range(6):
                val = tQ * sp.Integer(int(round(Vint[r, c])))
                A_ex[r, 10 + c] = val
                A_ex[10 + c, r] = -val
        return A_ex

    kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                    sp.Rational(1, 20))
    res_wit = {}
    for nm, Vw, lm_exp in (("J", V_J, (0.3064, 0.1532)),
                           ("Z", V_Z, (None, 0.2383))):
        A_ex = exact_parent(kapQ, mQ, tQ, Vw)
        wk = wick_exact_factory(A_ex)
        M1S = gram_exact(B1_S, r_S, sp.I, wk)
        M2S = gram_exact(B2_S, r_S, sp.I, wk)
        h1 = herm_exact(M1S)
        h2 = herm_exact(M2S)
        p1, piv1 = psd_exact(M1S)
        p2, piv2 = psd_exact(M2S)
        pd1 = p1 and all(p > 0 for p in piv1)
        pd2 = p2 and all(p > 0 for p in piv2)
        l1 = float(np.min(np.linalg.eigvalsh(np.array(
            M1S.evalf(16), dtype=complex))))
        l2 = float(np.min(np.linalg.eigvalsh(np.array(
            M2S.evalf(16), dtype=complex))))
        res_wit[nm] = (h1, h2, pd1, pd2, l1, l2)
        print("      V_%s witness: Hermitian (%s, %s), PD by exact "
              "LDL (%s, %s), float lam_min %.4f / %.4f"
              % (nm, h1, h2, pd1, pd2, l1, l2))
    okJ = res_wit["J"]
    okZ = res_wit["Z"]
    check("P2.2 STRICT theta_S RP PASSES EXACTLY at the V_J "
          "witness: Grams exactly Hermitian, PD by exact LDL; "
          "float lam_min %.4f = 0.3064 +- 0.005 (1p), %.4f = "
          "0.1532 +- 0.005 (deg-2)" % (okJ[4], okJ[5]),
          all(okJ[:4]) and abs(okJ[4] - 0.3064) <= 5e-3
          and abs(okJ[5] - 0.1532) <= 5e-3, kill="K2")

    # S_J identity + symbolic Schur + exact census
    S_J = V_J.astype(np.int64) @ J3 @ V_J.astype(np.int64).T
    okSJ = all(np.array_equal(S_J[2 * i:2 * i + 2, 2 * j:2 * j + 2],
                              3 * J2i)
               for i in range(5) for j in range(5))
    S_Z = V_Z.astype(np.int64) @ J3 @ V_Z.astype(np.int64).T
    okSZ = all(np.array_equal(S_Z[2 * i:2 * i + 2, 2 * j:2 * j + 2],
                              -3 * J2i)
               for i in range(5) for j in range(5))
    kap_s, m_s, t_s = sp.symbols("kappa m t", real=True)
    A_CCs = sp.Matrix(A_CC.tolist())
    J3s = sp.Matrix(J3.tolist())
    VJs = sp.Matrix(np.rint(V_J).astype(int).tolist())
    Ws = t_s * VJs
    C_CC = (sp.eye(10) + sp.I * kap_s * A_CCs) / 2
    C_CB = sp.I * Ws / 2
    C_BC = -sp.I * Ws.T / 2
    C_BB_inv = 2 * (sp.eye(6) - sp.I * m_s * J3s) / (1 - m_s ** 2)
    C_eff = sp.expand(C_CC - C_CB * C_BB_inv * C_BC)
    A_eff_sym = sp.Matrix(10, 10, lambda r, c: sp.expand(
        sp.im(sp.expand(2 * C_eff[r, c]))))
    SJs = sp.Matrix(S_J.tolist())
    A_eff_formula = (kap_s * A_CCs
                     + (m_s / (1 - m_s ** 2)) * t_s ** 2 * SJs)
    ok_schur = sp.simplify(A_eff_sym - A_eff_formula) == sp.zeros(10)
    lamQ = mQ / (1 - mQ ** 2)
    Jco = sp.Integer(3) * lamQ * tQ ** 2
    A_eff_ex = kapQ * A_CCs + lamQ * tQ ** 2 * SJs
    ok_cen = True
    for (i, j) in CAR_DUADS:
        Bx = A_eff_ex.extract(CH[i], CH[j])
        target = Jco * sp.Matrix([[0, 1], [-1, 0]])
        ok_cen &= (sp.expand(Bx - target) == sp.zeros(2))
        ok_cen &= (sp.sign(-Bx.det()) == sign_c[frozenset({i, j})])
    smax_eff = float(max(abs(x) for x in np.linalg.eigvalsh(
        1j * np.array(A_eff_ex.evalf(16), dtype=np.float64))))
    check("P2.3 THE COMPRESSION CARRIES THE FULL CANONICAL MIXING: "
          "S_J = 3J on ALL 25 blocks (integer: %s); A_eff = kappa "
          "A_CC + (m/(1-m^2)) t^2 S_J (symbolic: %s); every duad "
          "block = (3 m t^2/(1-m^2)) J with J-coordinate %s == "
          "1/200 EXACTLY, Pf4 canonical 10/10 (%s), compressed CAR "
          "valid (smax_eff %.4f < 1)"
          % (okSJ, ok_schur, Jco, ok_cen, smax_eff),
          okSJ and bool(ok_schur) and Jco == sp.Rational(1, 200)
          and ok_cen and smax_eff < 1, kill="K2")

    lamZ = mQ / (1 - mQ ** 2)
    JcoZ = -sp.Integer(3) * lamZ * tQ ** 2
    check("P2.4 V_Z SECOND WITNESS: S_Z = -3J uniform (integer: "
          "%s); strict theta_S passes exactly (Hermitian %s/%s, PD "
          "%s/%s, float lam_min %.4f = 0.2383 +- 0.005); "
          "J-coordinate %s == -1/200 exactly"
          % (okSZ, okZ[0], okZ[1], okZ[2], okZ[3], okZ[5], JcoZ),
          okSZ and all(okZ[:4]) and abs(okZ[5] - 0.2383) <= 5e-3
          and JcoZ == sp.Rational(-1, 200), kill="K2")

    A_exJ = exact_parent(kapQ, mQ, tQ, V_J)
    wkJ = wick_exact_factory(A_exJ)
    M1T = gram_exact(B1_ab, r_abT, sp.I, wkJ)
    ok_marg = (M1T == sp.zeros(2))
    B45e = A_eff_ex.extract(CH[a_ch], CH[b_ch])
    M1_eff = sp.Matrix([[B45e[0, 1], B45e[1, 1]],
                        [B45e[0, 0], B45e[1, 0]]])
    ev_eff = sorted(M1_eff.eigenvals().keys(), key=lambda z: sp.re(z))
    ok_eff = (ev_eff == [sp.Rational(-1, 200), sp.Rational(1, 200)])
    check("P2.5 THE 2-CYCLE SIDE IS UNTOUCHED: theta_abT 1p Gram "
          "identically 0 at the V_J witness (%s, marginal) and the "
          "compressed state fails effective 2-cycle RP with odd "
          "eigenvalues exactly {-1/200, +1/200} (%s) -- the "
          "strict-collar gate opens, the round-58 exclusion stands"
          % (ok_marg, ok_eff),
          ok_marg and ok_eff, kill="K2")

    # ==================================================================
    section("P3 -- kernel != sufficient (the honest boundary)")
    # ==================================================================
    A_Xf = parentV(0.5, 0.5, 0.05, V_X)
    okX, hdX, lmX, (M1X, M2X) = strict_S(A_Xf)
    raw1X = float(np.max(np.abs(M1X - M1X.conj().T)))
    D2X = M2X - M2X.conj().T
    row0X = float(np.max(np.abs(D2X[0, :])))
    ppX = float(np.max(np.abs(D2X[1:, 1:])))
    check("P3.1 the uniform X-coupling fails at the 1p seat: raw "
          "defect %.4f == 2t = 0.1 (empty deg-2 seat clean %.1e "
          "<= 1e-14, pair-pair %.4f = 0.05 +- 0.005) -- the law "
          "is sharp in both directions"
          % (raw1X, row0X, ppX),
          (not okX) and abs(raw1X - 0.1) <= 1e-12
          and row0X <= 1e-14 and abs(ppX - 0.05) <= 5e-3,
          kill="K3")

    mix_members = [
        ("J two / Z three", dict(
            [(("two", s), ("J", 1.0)) for s in range(3)]
            + [(("three", s), ("Z", 1.0)) for s in range(3)]),
         0.1861),
        ("mixed amps", {("two", 0): ("J", 1.0),
                        ("two", 1): ("Z", 0.5),
                        ("two", 2): ("J", -0.5),
                        ("three", 0): ("Z", 1.0),
                        ("three", 1): ("J", 0.7),
                        ("three", 2): ("Z", -0.3)}, 0.1848),
    ]
    ok_mix = True
    for nm, spec, lm_exp in mix_members:
        A = parentV(0.5, 0.5, 0.05, mkV(spec))
        okS, hdS, lmS, _g = strict_S(A)
        n_nz, n_sig, _a = census10(schur_Aeff(A))
        print("      %-16s hd=%.1e lm=%.4f mix nz=%d sig=%d"
              % (nm, hdS, lmS, n_nz, n_sig))
        ok_mix &= (hdS <= ZTOL and abs(lmS - lm_exp) <= 5e-3
                   and n_nz == 10 and n_sig == 4)
    check("P3.2 J/Z-MIXTURES pass exact Hermiticity + PD but the "
          "canonical SIGN census drops to 4/10 on both frozen "
          "members: the canonical gate selects the uniform J (or "
          "Z) ray -- Hermiticity kernel and canonical-mixing ray "
          "are different strata", ok_mix, kill="K3")

    sel_ok = True
    for nm, spec, exp_nz, exp_a in (
            ("two-orbit only", {("two", s): ("J", 1.0)
                                for s in range(3)}, 1, 0.005),
            ("three-orbit only", {("three", s): ("J", 1.0)
                                  for s in range(3)}, 3, 0.0),
            ("one pair both orbits", {("two", 0): ("J", 1.0),
                                      ("three", 0): ("J", 1.0)},
             10, 1.0 / 600.0)):
        A = parentV(0.5, 0.5, 0.05, mkV(spec))
        n_nz, n_sig, aJ45 = census10(schur_Aeff(A))
        sel_ok &= (n_nz == exp_nz and abs(aJ45 - exp_a) <= 1e-12)
    check("P3.3 orbit selectivity in the kernel (probe-7 P2.4 "
          "regression): 2-cycle-orbit only 1/10, 3-cycle only "
          "3/10, single boundary pair (both orbits) 10/10 with "
          "J-coordinate exactly lam t^2 = 1/600", sel_ok,
          kill="K3")

    A10 = parentV(0.5, 0.5, 0.1, V_J)
    ok10, hd10, lm10, _g = strict_S(A10)
    smax10 = float(np.max(np.abs(np.linalg.eigvalsh(1j * A10))))
    A15 = parentV(0.5, 0.5, 0.15, V_J)
    smax15 = float(np.max(np.abs(np.linalg.eigvalsh(1j * A15))))
    print("      amplitude anatomy: t=0.1 smax %.3f lm %.4f pass=%s"
          "; t=0.15 smax %.3f (CAR-invalid, report only)"
          % (smax10, lm10, ok10, smax15))
    check("P3.4 amplitude anatomy (report-gated loosely): uniform "
          "J passes at t = 1/10 (lm %.4f = 0.056 +- 0.01, smax "
          "%.3f < 0.95); t = 0.15 is CAR-invalid (smax %.3f > 1)"
          % (lm10, smax10, smax15),
          ok10 and abs(lm10 - 0.056) <= 0.01 and smax10 <= 0.95
          and smax15 > 1.0, kill="K3")

    # ==================================================================
    section("P4 -- the NESS side: exact no-go + the price curve")
    # ==================================================================
    h_full = -(A16_dep.astype(float) + 0.125 * A_int.astype(float))
    h_C16 = np.zeros((16, 16))
    h_C16[np.ix_(CAR_IDX, CAR_IDX)] = h_full[np.ix_(CAR_IDX,
                                                    CAR_IDX)]
    h_B16 = np.zeros((16, 16))
    h_B16[np.ix_(BND_IDX, BND_IDX)] = h_full[np.ix_(BND_IDX,
                                                    BND_IDX)]

    def kms_of(h, beta):
        w, Q = np.linalg.eigh(1j * h)
        f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
        return (-1j * (2 * (Q * f) @ Q.conj().T
                       - np.eye(len(h)))).real

    def two_temp_A0(bC, bB):
        A0 = np.zeros((16, 16))
        A0[np.ix_(CAR_IDX, CAR_IDX)] = kms_of(
            h_full[np.ix_(CAR_IDX, CAR_IDX)], bC)
        A0[np.ix_(BND_IDX, BND_IDX)] = kms_of(
            h_full[np.ix_(BND_IDX, BND_IDX)], bB)
        return A0

    wH, QH = np.linalg.eigh(1j * h_full)

    def cesaro(A0):
        Ac = QH.conj().T @ A0 @ QH
        mask = np.abs(wH[:, None] - wH[None, :]) < 1e-9
        return (QH @ np.where(mask, Ac, 0) @ QH.conj().T).real

    def evolve(A0, tt):
        R = (QH @ np.diag(np.exp(-1j * tt * wH)) @ QH.conj().T)
        ri = float(np.max(np.abs(R.imag)))
        R = R.real
        return R @ A0 @ R.T, ri

    def flux(hr, A):
        comm = h_full @ A - A @ h_full
        return 0.25 * float(np.sum(hr * comm))

    # (a) exact no-go, stated + total-energy ward
    A0_test = two_temp_A0(1.0, 0.25)
    At1, ri1 = evolve(A0_test, 1.0)
    e_tot = abs(0.25 * float(np.sum(h_full * (h_full @ At1
                                              - At1 @ h_full))))
    check("P4.1 FINITE-NESS-NOGO (exact): [h, A] = 0 => Phi_r = "
          "(1/4) tr(h0_r [h, A]) = 0 for every block => sigma == "
          "0 identically -- positive entropy production is "
          "category-inapplicable to a finite stationary state "
          "(algebraic implication; total-energy identity "
          "tr(h [h, A]) = %.1e <= 1e-12 warded; evolution real "
          "%.1e); the weakest meaningful positivity = RP of the "
          "stationary covariance (tested in P4.3)"
          % (e_tot, ri1), e_tot <= 1e-12 and ri1 <= 1e-12,
          kill="K4")

    DRIVES = ((1.0, 1.0), (1.0, 0.5), (1.0, 0.25), (2.0, 0.5))
    hd_seq = []
    lm_seq = []
    ok_ces = True
    ok_gates = True
    for (bC, bB) in DRIVES:
        A0 = two_temp_A0(bC, bB)
        Abar = cesaro(A0)
        stat = float(np.max(np.abs(h_full @ Abar - Abar @ h_full)))
        anti = float(np.max(np.abs(Abar + Abar.T)))
        smax = float(np.max(np.abs(np.linalg.eigvalsh(1j * Abar))))
        cd = cov_defect(Abar)
        f0C = abs(flux(h_C16, A0))
        f0B = abs(flux(h_B16, A0))
        okS, hdS, lmS, _g = strict_S(Abar)
        pf4_d = pf4_of(compress12(Abar))
        n_blk = sum(1 for dd in pf4_c
                    if abs(pf4_d[dd]) > PF_FLOOR
                    and (pf4_d[dd] > 0) == (pf4_c[dd] > 0))
        hd_seq.append(hdS)
        lm_seq.append(lmS)
        ok_ces &= (stat <= 1e-12 and anti <= 1e-12 and cd <= 1e-12
                   and smax <= 0.85 and max(f0C, f0B) <= 1e-14)
        ok_gates &= (n_blk == 15)
        print("      drive (%.1f, %.2f): stat %.1e smax %.3f | "
              "thetaS hd %.4f lm %.4f | blocks %d/15"
              % (bC, bB, stat, smax, hdS, lmS, n_blk))
    check("P4.2 the two-temperature Cesaro states: exactly "
          "stationary, real antisym, covariant, CAR-valid, t = 0 "
          "product fluxes EXACTLY zero on the whole frozen drive "
          "grid", ok_ces, kill="K4")

    sig1 = None
    sig4 = None
    for tt, tgt in ((1.0, None), (4.0, None)):
        At, _ri = evolve(two_temp_A0(1.0, 0.25), tt)
        s_val = 1.0 * flux(h_C16, At) + 0.25 * flux(h_B16, At)
        if tt == 1.0:
            sig1 = s_val
        else:
            sig4 = s_val
    check("P4.3 THE PRICE CURVE IS FLAT-OPEN: mixing census 15/15 "
          "canonical at EVERY drive point including zero drive "
          "(%s); Hermiticity defect PINNED (%.4f/%.4f/%.4f = "
          "0.0982 +- 0.005; %.4f = 0.1062 +- 0.005) while the PSD "
          "margin degrades (%.4f -> %.4f -> %.4f); transient "
          "sigma(1) = %.4f = 0.0626 +- 0.01 > 0, sigma(4) = %.4f "
          "< 0 (finite recurrence, typed): the minimal entropy "
          "production at which the mixing gates open is EXACTLY "
          "ZERO -- drive buys NO RP"
          % (ok_gates, hd_seq[0], hd_seq[1], hd_seq[2], hd_seq[3],
             lm_seq[0], lm_seq[1], lm_seq[2], sig1, sig4),
          ok_gates
          and all(abs(h - 0.0982) <= 5e-3 for h in hd_seq[:3])
          and abs(hd_seq[3] - 0.1062) <= 5e-3
          and lm_seq[0] > lm_seq[1] > lm_seq[2] > 0
          and abs(sig1 - 0.0626) <= 0.01 and sig4 < 0, kill="K4")

    check("P4.4 TYPED CONCLUSION: NESS-NOT-FORCED -- the "
          "strict-collar mixing needs the coupling DIRECTION (the "
          "two-seat kernel, equilibrium-compatible: P2), not a "
          "non-equilibrium source; the round-59 obstruction is "
          "DIRECTION-level (deployed PURE-I wiring, P1.3), not "
          "equilibrium-level; on this tested class a NESS is "
          "neither forced nor helpful (P4.3)", True,
          "typed by measurement")

    # ==================================================================
    section("C -- controls (must fire; RNG only in C2)")
    # ==================================================================
    A_kms = kms_of(h_full, 1.0)
    statK = float(np.max(np.abs(h_full @ A_kms - A_kms @ h_full)))
    okK, hdK, lmK, _g = strict_S(A_kms)
    check("C1 FIRES (zero-drive regression): the global KMS state "
          "(1, 1/8, 1) is exactly stationary (%.1e) and FAILS "
          "strict theta_S with defect %.4f = 0.0982 +- 0.005"
          % (statK, hdK),
          statK <= 1e-12 and (not okK)
          and abs(hdK - 0.0982) <= 5e-3, kill="K7")

    rng = np.random.default_rng(904)
    n_cov = 0
    n_gates = 0
    for _trial in range(3):
        pr = rng.permutation(10)
        Vb = V_J[pr, :]
        A_bad = parentV(0.5, 0.5, 0.05, Vb)
        if cov_defect(A_bad) >= NZ_FLOOR:
            n_cov += 1
        _n_nz, n_sig, _a = census10(schur_Aeff(A_bad))
        if n_sig <= 1:
            n_gates += 1
    check("C2 FIRES: 3/3 seeded row permutations of V_J break the "
          "covariance ward (%d/3) AND the canonical Pfaffian "
          "census (%d/3 with sign census <= 1/10)"
          % (n_cov, n_gates), n_cov == 3 and n_gates == 3,
          kill="K7")

    check("C3 FIRES (deployed-coupling regression): the PURE-I "
          "parent fails strict theta_S with raw defect 0.1 and 30 "
          "entries (P1.3 doubles as the control; fire rule "
          "re-read)", (not okD) and n_def == 30, kill="K7")

    v0 = np.zeros((10, 6))
    v0[2 * (a_ch - 1):2 * a_ch, 0:2] = PAULI["I"]
    wI = np.zeros((10, 6))
    cur = v0
    for _k in range(2):
        wI += cur
        cur = O_C.astype(float) @ cur @ O_B.astype(float).T
    A_c4 = parentV(0.5, 0.5, 0.05, V_J + 0.5 * wI)
    okC4, hdC4, lmC4, (M1C4, M2C4) = strict_S(A_c4)
    rawC4 = float(np.max(np.abs(M2C4[0, :]
                                - M2C4[:, 0].conj().T)))
    check("C4 FIRES (I-orbit switch-on): adding one covariant "
          "I-orbit to V_J turns the deg-2 empty-seat defect ON "
          "(raw %.4f > 0.01) while covariance stays exact (%.1e)"
          % (rawC4, cov_defect(A_c4)),
          (not okC4) and rawC4 > 0.01
          and cov_defect(A_c4) <= ZTOL, kill="K7")

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
        VERDICT = "LAW-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "WITNESS-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "KERNEL-BROKEN"
    elif "K4" in KILLS:
        VERDICT = "NESS-BROKEN"
    else:
        VERDICT = ("NESSPARENT-MEASURED [PRICE-ZERO(equilibrium "
                   "strict-collar witnesses V_J / V_Z: exact "
                   "Hermitian + PD + 10/10 canonical + "
                   "J-coordinate +-1/200), TWO-SEAT-LAW(rank 12, "
                   "kernel 12 = the {J, Z} coordinates; deployed "
                   "coupling PURE-I), CANONICAL-SELECTS-UNIFORM-"
                   "RAY(mixtures 4/10), FINITE-NESS-NOGO("
                   "stationary => sigma == 0, exact), "
                   "DRIVE-RP-NEUTRAL(defect pinned, margin "
                   "degrades, gates open at zero drive), "
                   "NESS-NOT-FORCED]")
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE HEADLINE ANSWER: the strict-collar mixing does NOT need a
    NESS.  The round-59 obstruction is a property of the coupling
    DIRECTION: strict theta_S Hermiticity is obstructed at linear
    order by exactly two seat families (1p kills the X sub-block
    coordinates, deg-2 kills the I coordinates; rank 12 on the
    24-dim covariant coupling space), and the DEPLOYED seam wiring
    is PURE-I -- maximally obstructed.  The 12-dim {J, Z} kernel
    contains EQUILIBRIUM witnesses: the uniform J- and Z-coupling
    parents pass strict theta_S RP in exact arithmetic while their
    Schur compressions carry the full canonical Pfaffian mixing
    with the J-coordinate EXACTLY +-1/200 (the same rational floor
    identity).  The minimal entropy production at which the mixing
    gates open is ZERO; typing: NESS-NOT-FORCED.
  * THE NESS SIDE, honestly: at this finite size an exactly
    stationary quasi-free state has zero currents and sigma == 0
    (exact) -- 'NESS with positive entropy production' is
    category-inapplicable; the two-temperature Cesaro states are
    stationary, covariant, mixing-open at ZERO drive, keep the
    deployed-direction Hermiticity defect PINNED (~0.098) and only
    lose PSD margin as the drive grows: drive buys NO RP.
  * THE BOUNDARY OF THE WIN: the kernel is necessary, not
    sufficient -- X-couplings fail the 1p seat (raw defect exactly
    2t), and J/Z mixtures pass Hermiticity but break the canonical
    sign census (4/10): the canonical gate selects the uniform J
    (or Z) ray.  The 2-cycle exclusion is untouched: the V_J
    witness stays theta_abT-MARGINAL and its compression fails
    effective 2-cycle RP at exactly -+1/200.
  * HONESTY: the witnesses live on a DIFFERENT covariant coupling
    direction than the deployed A_int wiring -- whether the actual
    seam allows that direction is untouched; finite-size no-go
    only; RP sector-typed; the [O] premise of v898/v903 is
    unmoved; no marker moves.  NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
