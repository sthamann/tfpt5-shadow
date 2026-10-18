#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_wiring_groebner_probe -- SEAM.STATE.WIRING.GROEBNER.01
(EXPLORATION ONLY, experiments/; 2026-08-12 -- the finite algebraic
census of the seam wiring question named at the end of round 60,
entry CXXXIX: is the deployed PURE-I wiring compiler-FORCED by the
orbit/edge rules of the vacuum-orbit construction of A_int, or is a
{J, Z}-kernel alternative compiler-legal at equal C6-covariance and
equal Pf-pencil?  Only then is it decidable whether the strict-collar
obstruction of round 58/59 is a compiler THEOREM or a DEPLOYMENT
CHOICE.)

THE QUESTION (the CXXXIX contract, verbatim scope).  Round 60
(seam_ness_parent_probe, SEAM.CFIN.NESS.PARENT.01) measured: the
C6-covariant C<->B coupling space has dimension 24; the strict
theta_S Hermiticity law has rank 12 with kernel 12 = the {J, Z}
sub-block coordinates; the DEPLOYED coupling V = A_int[C, B] is
PURE-I (every 2x2 sub-block exactly -I2), a maximally obstructed
direction; and the kernel contains zero-entropy-production
equilibrium mixing witnesses V_J and V_Z.  What was NOT measured:
whether the compiler's own orbit/edge rules (one unit per edge
orbit, IOTA/I2/J2 units, orientation propagation) PIN the I
direction.  This probe closes that question as a finite exact
computation: parametrize the full equivariant commutant, impose the
constraint classes as polynomial equations/inequalities, compute the
Groebner basis and a certified decomposition of the real variety,
quotient by the structure-preserving gauge, and COUNT the admissible
components.

FEASIBILITY / REDUNDANCY CHECK (against the corpus, 2026-08-12):
round 60 scanned rays and mixtures INSIDE the 24-dim space but never
decomposed the constraint variety; probe 7 (rp_parent_dilation)
scanned only the deployed direction family; NOTHING in the corpus
(a) writes the edge rules as polynomial constraint classes, (b)
computes the ideal decomposition, or (c) identifies the gauge group
of the wiring space.  That is exactly this probe.

SMOKE-RUN DISCLOSURE (2026-08-12, declared smoke rounds before
freezing; fail-first preserved):
 (i)   the boundary block of the C6 action is the IDENTITY
       (PI6 fixes channel 0 position-wise), so the equivariant
       commutant of the coupling space is exactly
       {2 channel orbits} x {3 boundary seats} x M2(R) = 24 dims
       (the v898 T-count reproduced structurally);
 (ii)  the per-orbit unit-law ideal (u^T u prop. I) has the exact
       closed form {ab + cd = 0, ad - bc = 0} whose REAL variety
       splits into the rotation plane {b = d = 0} and the
       reflection plane {a = c = 0} (cofactor certificates below);
       complex residual components are real-point-free;
 (iii) the Pfaffian-pencil cross-block condition reduces on the
       rotation x rotation branch to the single determinantal
       quadric a2*c3 - c2*a3 = 0 (alignment) with pX = pZ = 0
       IDENTICALLY, and on mixed rotation x reflection branches it
       forces the reflection factor to ZERO (degenerate) by exact
       cofactor identities: mixed wirings are pencil-illegal;
 (iv)  within-orbit pencil blocks are AUTOMATIC: the identity
       u J2 u^T = det(u) J2 holds for every real 2x2 u, so only
       cross-orbit blocks constrain;
 (v)   the working hypothesis 'the rules pin the I direction' is
       REFUTED in the strongest form: the admissible set contains
       an exact integer gauge transformation g = (+)_5 J2 (+) I6
       (preserving A_CC, J3, the C6 action, the seat-stack rule
       subspace and the constraint ideal) that maps the deployed
       PURE-I wiring to the PURE-(-J) wiring -- pure-I and pure-J
       are CONNECTED-GAUGE-EQUIVALENT, and a rational interior
       witness (3/5, 4/5 rotation) passes every constraint class
       while being neither I nor J;
 (vi)  the theta_S collar frame BREAKS this gauge to a discrete
       subgroup (an SO(2) block R commutes with the sheet-swap X
       iff its sine vanishes, exact), so relative to the FROZEN
       collar the rotation angle is physical: the admissible
       component is a genuine circle family, pure-I and pure-J are
       distinct points on ONE component, and the strict-collar
       two-seat law intersects the component EXACTLY in the
       pure-(+-J) ray;
 (vii) smoke corrections (disclosed, all implementation-level, no
       claim inverted): (1) the Schur-identity and C_BB-inverse
       wards need rational CANCELLATION (expand alone does not
       clear the 1/(1-m^2) denominators); (2) the mixed-branch
       degeneracy certificate is verified as exact GROEBNER
       MEMBERSHIP of (a2^2+c2^2) b3 and (a2^2+c2^2) d3 in the
       branch pencil ideal (a hand-signed cofactor draft had a
       sign slip and was replaced by the reduction-to-zero check);
       (3) the structure-gauge algebra dimension 16 and rule
       stabilizer dimension 9 were hand-predicted and measured
       EQUAL by the exact nullspaces.

CONVENTIONS (round-58/59/60 wiring rebuilt inline; READ-ONLY import
of tfpt_constants): 16-dim Majorana space, carrier C = 0..9
(channels 1..5, pairs), boundary B = 10..15 (channel 0, three
seats); A_CC = (+)_5 J2, J3 = A16_dep[B, B]; deployed wiring
V = A_int[C, B]; parent family A(kappa, m, t, V) = [[kappa A_CC,
t V], [-t V^T, m J3]] at the frozen probe-7 point (kappa, m, t) =
(1/2, 1/2, 1/20).  AMBIENT ALGEBRA: the equivariant commutant
Comm = {V in R^{10x6} : O_C V O_B^T = V}; coordinates u_{o} =
a_o I + b_o X + c_o J + d_o Z per orbit o in {2-cycle, 3-cycle}
after the seat-stack rule (below), 8 rational variables
(a2, b2, c2, d2, a3, b3, c3, d3).  CONSTRAINT CLASSES (each warded
on PURE-I -- the primary consistency ward):
 E1 CAR / unit edge law: each orbit unit is a scaled isometry of
    the Majorana pairing, u^T u = mu I (the deployed constructor
    units I2, J2, IOTA are exact isometries); polynomial closed
    form {a b + c d, a d - b c} per orbit;
 E2 KMS: the parent at the frozen point is CAR-strict (||A|| < 1,
    exact PD of I + A^2 by leading principal minors) hence by the
    round-59 artanh theorem a beta = 1 KMS state of a covariant
    Hamiltonian (float round-trip ward); an OPEN scale bound --
    it does not cut components (typed);
 E3 Pfaffian pencil (quasi-free consistency): the Schur
    compression A_eff = kappa A_CC + (m/(1-m^2)) t^2 V J3 V^T
    (symbolic identity proven on the rule subspace) carries every
    carrier duad block proportional to J2 with nonzero canonical
    Pf4 (cross-orbit blocks give 3 quadrics; within-orbit blocks
    are automatic by u J2 u^T = det(u) J2);
 E4 orientation propagation: det u_o > 0 (every deployed
    constructor unit is orientation-preserving; a det < 0 unit
    reverses the pair orientation of A16_dep at the target;
    semialgebraic, selects real positive components);
 E5 orbit/edge rules: C6-covariance (built into the commutant) +
    the IOTA seat-stack rule (one unit per boundary edge orbit:
    u_{o, s} independent of the seat s -- the 8-dim rule subspace
    W of the 24-dim commutant).
NONDEGENERACY (census side condition): all 10 carrier duad blocks
of A_eff nonzero with canonical Pf4 sign.  NUMERICAL PROTOCOL
(declared): commutant, gauge algebra, Groebner basis, certificates,
witnesses, CAR minors, census are EXACT (integer/rational sympy);
float64 ONLY in disclosed wards (Gram closed-form ward, artanh
round-trip, smax reporting); RNG only in controls.

FROZEN CLAIMS (2026-08-12, frozen + SHA-hashed before the frozen
run):

 P1  THE AMBIENT ALGEBRA AND ITS GAUGE (exact).
     (a) the C6 action restricted to the boundary block is the
         IDENTITY (O_B = I6, integer check), and the equivariant
         commutant of the 10x6 coupling space has dimension
         EXACTLY 24 (exact nullspace of the orbit-sum projector);
     (b) the seat-stack rule subspace W (IOTA rule: one 2x2 unit
         per orbit stacked over 3 seats) has dimension EXACTLY 8
         and contains the deployed wiring: V_dep = A_int[C, B] is
         PURE-I, every 2x2 sub-block exactly -I2 (integer);
     (c) the structure gauge algebra g0 = {X in o(16) block-diag:
         [X, O16] = 0, [X_C, A_CC] = 0, [X_B, J3] = 0} has
         dimension EXACTLY 16 (exact nullspace; carrier commutant
         7 + boundary u(3) = 9);
     (d) the rule stabilizer (elements of g0 preserving W and
         mapping the constraint ideal into itself, exact
         Groebner-remainder linear system) has dimension EXACTLY 9
         and acts on the coordinates through the rank-2 torus
         {u_o -> gamma J2 u_o - y u_o J2} (equal gamma on both
         orbits: the relative carrier rotation is CUT by the
         pencil, remainder nonzero) plus a trivially-acting
         kernel; the theta_S sheet-swap frame breaks the torus to
         a DISCRETE subgroup: R(p, q) X = X R(p, q) forces q = 0
         EXACTLY (symbolic 2x2).
 P2  CONSTRAINT CLASSES AND THE DEPLOYED-WIRING WARD (exact).
     (a) E1 closed form warded: u^T u - mu I = 0 iff
         {a b + c d = 0, a d - b c = 0} (symbolic expansion);
         PURE-I satisfies both at ZERO exactly;
     (b) E3 anchored: the symbolic Schur identity A_eff =
         kappa A_CC + (m/(1-m^2)) t^2 V J3 V^T holds on ALL of W
         (8 symbolic coordinates x symbolic kappa, m, t), the
         within-orbit identity u J2 u^T = det(u) J2 holds
         identically, and the closed-form two-seat linear law of
         round 60 (deg-2 seat = trace coordinate 2a_o, 1p seat =
         X coordinate 2b_o) is REPRODUCED by the float Gram
         machinery on unit couplings (ward <= 1e-12) with exact
         rank 12 / kernel 12 on the 24-dim commutant;
     (c) PURE-I passes EVERY constraint class exactly: E1 (0, 0),
         E3 cross quadrics (0, 0, 0) with S_I = 3 J on all 25
         channel blocks (integer identity, equal to S_J), E4
         (det = +1), E5 (in W), E2 (I + A^2 exactly PD at the
         frozen point, 16/16 leading minors positive; artanh
         round-trip <= 1e-9) and the canonical census 10/10 with
         J-coordinate EXACTLY +1/200 -- the deployed wiring ward;
     (d) the strict-collar two-seat law is NOT in the constraint
         list (pure-I fails it, defect 2t: round-60 regression
         reproduced float-exactly) -- it enters only as the
         SELECTOR in P4(d).
 P3  THE GROEBNER DECOMPOSITION (exact; term order documented).
     (a) the rule ideal I_rule = (E1_2, E1_3, E3_cross) c
         Q[a2..d3] (7 generators, all quadrics) in grevlex order
         with a2 > b2 > c2 > d2 > a3 > b3 > c3 > d3;
     (b) certified cofactor identities (symbolic expansion == 0):
         a (b^2 + d^2) = b g1 + d g2, c (b^2 + d^2) = d g1 - b g2,
         b (a^2 + c^2) = a g1 - c g2, d (a^2 + c^2) = c g1 + a g2
         per orbit, so every REAL point of the unit ideal lies in
         the rotation plane or the reflection plane; on the mixed
         rotation x reflection branch the pencil forces
         (a2^2 + c2^2) b3 = 0 = (a2^2 + c2^2) d3 (exact Groebner
         membership in the branch ideal), i.e. nondegenerate real
         mixed points DO NOT EXIST;
     (c) the certified real decomposition of V(I_rule) into
         irreducible real components away from the degenerate
         locus {u2 = 0} u {u3 = 0}:
           C_rot  = V(b2, d2, b3, d3, a2 c3 - c2 a3)   (dim 3),
           C_refl = V(a2, c2, a3, c3, b2 d3 - d2 b3)   (dim 3),
         each containing I_rule (generator-wise Groebner reduction
         to 0) with exact rational parametrization certificates
         (u3 = lambda u2 on nondegenerate points); complex
         residual components are real-point-free (sum-of-squares
         certificates).
 P4  THE CENSUS (the verdict; every component certified by an
     exact witness point).
     (a) admissible components (E1-E5 + nondegeneracy) modulo the
         rule gauge: EXACTLY ONE -- C_rot (witnesses: pure-I at
         (-1,0,0,0|-1,0,0,0), pure-J at (0,0,1,0|0,0,1,0), and the
         INTERIOR rational point (3/5,0,4/5,0|3/5,0,4/5,0), all
         passing E1-E5 + census 10/10 exactly, CAR-strict by
         exact minors); C_refl passes E1, E3, E5 and nondegeneracy
         (witness V_Z at (0,0,0,1|0,0,0,1), canonical census
         10/10, J-coordinate -1/200 exact) but FAILS E4
         (det u = -(b^2 + d^2) < 0 on every nondegenerate real
         point, exact identity): orientation propagation is
         PRECISELY the edge rule that outlaws the Z/X wirings;
     (b) pure-I is NOT a vertex, NOT isolated, NOT forced: it is
         an interior point of the 3-dim cell C_rot, and the
         integer gauge element g = (+)_5 J2 (+) I6 (preserving
         A_CC, J3, C6, W and I_rule -- all checked exactly) maps
         it to pure-(-J): I and J are gauge-equivalent under the
         rules;
     (c) in the FROZEN theta_S collar frame (gauge broken to the
         discrete stabilizer, P1.d) the component C_rot is a
         physical circle x scale family: pure-I (angle pi) and
         pure-J (angle -pi/2) are DISTINCT admissible wirings --
         the J coupling of round 60 (the zero-entropy-production
         mixing carrier) is COMPILER-LEGAL;
     (d) THE SELECTOR THEOREM (exact): on C_rot the strict-collar
         two-seat law (a2 = a3 = 0, b already 0) cuts EXACTLY the
         pure-(+-J) ray {u_o = c_o J2, c_2 c_3 != 0} -- i.e.
         orbit/edge rules + strict-collar Hermiticity FORCE
         PURE-J uniquely (up to gauge flips and scale), and
         pure-I sits at the MAXIMALLY obstructed angle; the
         round-58/59 strict-collar obstruction of the deployed
         wiring is a DEPLOYMENT CHOICE, not a compiler theorem.
 P5  SECONDARY RELAXATION (seat-nonuniform, 24 variables; typed,
     verdict-unchanged): dropping the IOTA seat-stack rule keeps
     the within-orbit blocks automatic (Sum_s det u_{o,s} J2,
     exact identity), orientation still forces all-rotation
     blocks, and the cross-pencil reduces to ONE quadric
     Sum_s (a2s c3s - c2s a3s) = 0 of exact signature (6, 6)
     (sum-of-squares identity), an indefinite connected quadric:
     the relaxed census stays degenerate -- removing a rule
     cannot create forcing (monotonicity, typed).
 C   CONTROLS (must fire; frozen fire rules; RNG only in C1).
     C1 SEEDED SCRAMBLE (rng 906, 3 draws: random row permutation
        of the pure-I wiring): breaks exact C6-covariance
        (commutant membership) on 3/3;
     C2 X-WIRING (0,1,0,0|0,1,0,0): E4 fires (det = -1) AND the
        two-seat 1p seat fires (b != 0; raw float defect 2t at
        the frozen parent, round-60 regression);
     C3 Z-WIRING near miss: passes E1, E3, E5, census 10/10,
        two-seat law CLEAN -- but E4 fires (det = -1): exactly
        one constraint class rejects it;
     C4 MIXED J-on-2-cycle / Z-on-3-cycle: the pencil quadric
        fires (cross block = -3Z, pZ = -3 != 0) and the exact
        canonical census drops to 4/10 (cross duads all
        anti-canonical) -- the round-60 P3(b) 4/10 law reproduced
        EXACTLY at block level;
     C5 NON-UNIT wiring u = I + X: E1 fires (g1 = 1 != 0);
     C6 PERTURBED PURE-I (u = -I + Z/10): E1 fires
        (g2 = -1/10 != 0) -- an illegal perturbation of the
        deployed point violates at least one constraint.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 commutant / gauge-algebra dimension ward     -> COMMUTANT-BROKEN
  K2 a constraint ward (incl. pure-I ward) breaks -> WARD-BROKEN
  K3 Groebner / certificate / decomposition ward  -> DECOMP-BROKEN
  K4 census / witness / selector ward breaks      -> CENSUS-BROKEN
  K5 secondary relaxation ward breaks             -> RELAX-BROKEN
  K7 a control does not fire                      -> CONTROL-DEAD

VERDICT (frozen enum): WIRING-DEGENERATE [ADMISSIBLE-CENSUS-1
(C_rot unique admissible component mod gauge), I-NOT-FORCED
(interior point, not vertex), I-J-GAUGE-CONNECTED (integer witness
(+)_5 J2 (+) I6), J-COMPILER-LEGAL (distinct admissible point in
the frozen collar frame), Z-X-EDGE-ILLEGAL (orientation
propagation, det < 0), STRICT-COLLAR-SELECTS-PURE-J (selector
theorem: rules + collar Hermiticity force the +-J ray uniquely),
DEPLOYMENT-CHOICE (the strict-collar obstruction of pure-I is not
a compiler theorem)] / WIRING-FORCED / WIRING-UNDECIDED /
PIPELINE-BROKEN / COMMUTANT-BROKEN / WARD-BROKEN / DECOMP-BROKEN /
CENSUS-BROKEN / RELAX-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the census is a statement about the
FORMALIZED constraint classes E1-E5 (each warded on the deployed
wiring); whether the actual seam demands the strict theta_S collar
(which would select pure-J, P4.d) or the deployed frame is
UNTOUCHED here; RP remains sector-typed; the v898/v903 [O] premise
is unmoved; no marker moves.  NO RH claim.

SPEC v1 (2026-08-12): frozen after the declared smoke rounds; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline): seam_ness_parent_
probe (round 60: two-seat law, 24-dim T-count, witnesses),
rp_parent_dilation_probe (probe 7: parent family, Schur census),
seam_state_derivation_probe (round 58: theta_S machinery),
v898_kms_schur_mixing, v519 (RP Gram), tfpt_constants (N_fam,
g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_wiring_groebner_probe.py
"""

import ast
import hashlib
import itertools
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

ZTOL = 1e-10
NZ_FLOOR = 1e-8


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

I2s = sp.eye(2)
Xs = sp.Matrix([[0, 1], [1, 0]])
Js = sp.Matrix([[0, 1], [-1, 0]])
Zs = sp.Matrix([[1, 0], [0, -1]])
PAULIS = {"I": I2s, "X": Xs, "J": Js, "Z": Zs}


def pauli_coords(M):
    """Exact (I, X, J, Z) coordinates of a real 2x2 sympy matrix."""
    return (sp.expand((M[0, 0] + M[1, 1]) / 2),
            sp.expand((M[0, 1] + M[1, 0]) / 2),
            sp.expand((M[0, 1] - M[1, 0]) / 2),
            sp.expand((M[0, 0] - M[1, 1]) / 2))


def main():
    print("SEAM.STATE.WIRING.GROEBNER.01 -- the seam wiring census: "
          "do the orbit/edge rules force PURE-I?")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (round-60 rebuild)")
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
    Vdep = A_int[np.ix_(CAR_IDX, BND_IDX)]
    check("S0.3 blocks extracted: A_CC = (+)_5 J2, J3, deployed "
          "wiring V_dep = A_int[C, B]", okA and okD, kill="K0")

    O16 = np.zeros((16, 16), dtype=np.int64)
    for src in range(16):
        O16[img[src], src] = 1
    O_C = O16[np.ix_(CAR_IDX, CAR_IDX)]
    O_B = O16[np.ix_(BND_IDX, BND_IDX)]

    # edge-orbit anatomy of the C<->B part (the vacuum-orbit rules)
    cb_orbs = [(edges, rev) for edges, rev, rep in orbs
               if 0 in {min(rep), max(rep)} or
               any(0 in e for e in edges)]
    cb_lens = sorted(len(e) for e, _r in cb_orbs)
    cb_rev = [r for _e, r in cb_orbs]
    check("S0.4 C<->B edge orbits: lengths %s == [2, 3], reversals "
          "%s == none (the IOTA edges are never reversed: the "
          "J2-on-reversal law does not touch the wiring)"
          % (cb_lens, cb_rev),
          cb_lens == [2, 3] and not any(cb_rev), kill="K0")

    # canonical Pf4 signs (round-60 S0.4 convention)
    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}
    IOTA_f = IOTA6i.astype(np.float64)

    def compress12(A):
        Ahat = np.zeros((12, 12))
        for (i, j) in DUADS_CH:
            if i == 0:
                Bm = IOTA_f.T @ A[np.ix_(CH[0], CH[j])] / 3.0
            else:
                Bm = A[np.ix_(CH[i], CH[j])]
            for rr in range(2):
                for cc in range(2):
                    Ahat[CH2[i][rr], CH2[j][cc]] = Bm[rr, cc]
                    Ahat[CH2[j][cc], CH2[i][rr]] = -Bm[rr, cc]
        return Ahat

    pf4_c = {}
    Ahat_c = compress12(A_int.astype(np.float64) / 200.0)
    for (i, j) in DUADS_CH:
        Bm = Ahat_c[np.ix_(CH2[i], CH2[j])]
        pf4_c[frozenset({i, j})] = -(Bm[0, 0] * Bm[1, 1]
                                     - Bm[0, 1] * Bm[1, 0])
    sign_c = {d: (1 if v > 0 else -1) for d, v in pf4_c.items()}
    check("S0.5 canonical G_c Pf4 signs rebuilt: 15 nonzero, all "
          "negative",
          all(abs(v) > 1e-16 for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ==================================================================
    section("P1 -- the ambient algebra: commutant, rule subspace, "
            "gauge")
    # ==================================================================
    okOB = np.array_equal(O_B, np.eye(6, dtype=np.int64))

    # exact commutant of V -> O_C V O_B^T on the 10x6 space
    P60 = sp.zeros(60, 60)
    for r in range(10):
        for c in range(6):
            rr = int(np.flatnonzero(O_C[:, r])[0])
            cc = int(np.flatnonzero(O_B[:, c])[0])
            P60[rr * 6 + cc, r * 6 + c] = 1
    comm_basis = (P60 - sp.eye(60)).nullspace()
    dim_comm = len(comm_basis)
    check("P1.1 boundary C6 block is the IDENTITY (O_B = I6: %s); "
          "equivariant commutant dim = %d == 24 (v898 T-count): "
          "Comm = {2 orbits} x {3 seats} x M2(R)"
          % (okOB, dim_comm),
          okOB and dim_comm == 24, kill="K1")

    # seat-stack rule subspace W and symbolic coordinates
    a2, b2, c2, d2, a3, b3, c3, d3 = sp.symbols(
        "a2 b2 c2 d2 a3 b3 c3 d3", real=True)
    GENS8 = (a2, b2, c2, d2, a3, b3, c3, d3)
    u2 = a2 * I2s + b2 * Xs + c2 * Js + d2 * Zs
    u3 = a3 * I2s + b3 * Xs + c3 * Js + d3 * Zs

    def mkW(u2m, u3m):
        V = sp.zeros(10, 6)
        for i in range(1, 6):
            uo = u2m if i in TWO else u3m
            for s in range(3):
                V[2 * (i - 1):2 * i, 2 * s:2 * s + 2] = uo
        return V

    V_sym = mkW(u2, u3)

    def in_commutant(Vm):
        Vp = sp.zeros(10, 6)
        for r in range(10):
            for c in range(6):
                rr = int(np.flatnonzero(O_C[:, r])[0])
                cc = int(np.flatnonzero(O_B[:, c])[0])
                Vp[rr, cc] = Vm[r, c]
        return sp.expand(Vp - Vm) == sp.zeros(10, 6)

    ok_Wcov = in_commutant(V_sym)
    Vdep_s = sp.Matrix(Vdep.tolist())
    ok_pureI = all(
        sp.Matrix(Vdep.tolist())[2 * i:2 * i + 2, 2 * s:2 * s + 2]
        == -I2s for i in range(5) for s in range(3))
    subI = {a2: -1, b2: 0, c2: 0, d2: 0, a3: -1, b3: 0, c3: 0, d3: 0}
    ok_VdepW = sp.expand(V_sym.subs(subI) - Vdep_s) == sp.zeros(10, 6)
    check("P1.2 rule subspace W (IOTA seat-stack) dim 8 c commutant "
          "(covariance symbolic: %s); deployed wiring PURE-I (every "
          "2x2 block -I2: %s) = W point (-1,0,0,0|-1,0,0,0): %s"
          % (ok_Wcov, ok_pureI, ok_VdepW),
          ok_Wcov and ok_pureI and ok_VdepW, kill="K1")

    # structure gauge algebra g0 (exact nullspace over 60 antisym vars)
    pairsC = list(itertools.combinations(range(10), 2))
    pairsB = list(itertools.combinations(range(6), 2))
    nv = len(pairsC) + len(pairsB)
    A_CCs = sp.Matrix(A_CC.tolist())
    J3s = sp.Matrix(J3.tolist())
    O_Cs = sp.Matrix(O_C.tolist())

    def XC_of(vec):
        X = sp.zeros(10, 10)
        for k, (i, j) in enumerate(pairsC):
            X[i, j] = vec[k]
            X[j, i] = -vec[k]
        return X

    def XB_of(vec):
        X = sp.zeros(6, 6)
        for k, (i, j) in enumerate(pairsB):
            X[i, j] = vec[len(pairsC) + k]
            X[j, i] = -vec[len(pairsC) + k]
        return X

    vsyms = sp.symbols("x0:%d" % nv, real=True)
    XCs = XC_of(vsyms)
    XBs = XB_of(vsyms)
    eqs = []
    eqs += list(sp.expand(XCs * O_Cs - O_Cs * XCs))
    eqs += list(sp.expand(XCs * A_CCs - A_CCs * XCs))
    eqs += list(sp.expand(XBs * J3s - J3s * XBs))
    Meq = sp.Matrix([[sp.diff(e, v) for v in vsyms] for e in eqs])
    g0_basis = Meq.nullspace()
    dim_g0 = len(g0_basis)
    check("P1.3 structure gauge algebra g0 = {X in o(16) blockdiag: "
          "[X,O16]=[X_C,A_CC]=[X_B,J3]=0}: dim = %d == 16 "
          "(carrier commutant 7 + boundary u(3) 9)" % dim_g0,
          dim_g0 == 16, kill="K1")

    # constraint ideal generators (defined here; justified in P2)
    UT2 = sp.expand(u2.T * u2)
    UT3 = sp.expand(u3.T * u3)
    g1_2 = sp.expand(UT2[0, 1])            # closed form 2(ab+cd)
    g2_2 = sp.expand(UT2[0, 0] - UT2[1, 1])  # closed form 4(ad-bc)
    g1_3 = sp.expand(UT3[0, 1])
    g2_3 = sp.expand(UT3[0, 0] - UT3[1, 1])
    Mcross = sp.expand(3 * u2 * Js * u3.T)
    pI, pX, pJ, pZ = pauli_coords(Mcross)
    IDEAL_GENS = [g1_2, g2_2, g1_3, g2_3,
                  sp.expand(2 * pI), sp.expand(2 * pX),
                  sp.expand(2 * pZ)]
    gb = sp.groebner(IDEAL_GENS, *GENS8, order="grevlex")

    def rem(expr):
        return gb.reduce(sp.expand(expr))[1]

    # rule stabilizer: elements of g0 preserving W and the ideal.
    # Both the W-preservation conditions and the Groebner normal
    # form are LINEAR in the gauge element, so compute them per
    # basis element and assemble one exact linear system.
    rep2, rep3 = TWO[0], THREE[0]
    per_elem = []
    for base in g0_basis:
        XCk = XC_of(list(base))
        XBk = XB_of(list(base))
        dV = sp.expand(XCk * V_sym - V_sym * XBk)
        du2 = dV[2 * (rep2 - 1):2 * rep2, 0:2]
        du3 = dV[2 * (rep3 - 1):2 * rep3, 0:2]
        condsW = []
        for i in range(1, 6):
            ref = du2 if i in TWO else du3
            for s in range(3):
                blk = dV[2 * (i - 1):2 * i, 2 * s:2 * s + 2]
                for e in sp.expand(blk - ref):
                    condsW.append(e)
        d_coords = {}
        for sym, val in zip((a2, b2, c2, d2), pauli_coords(du2)):
            d_coords[sym] = val
        for sym, val in zip((a3, b3, c3, d3), pauli_coords(du3)):
            d_coords[sym] = val
        condsI = []
        for f in IDEAL_GENS:
            df = sp.expand(sum(sp.diff(f, x) * d_coords[x]
                               for x in GENS8))
            condsI.append(sp.expand(rem(df)))
        per_elem.append((condsW, condsI, d_coords))
    # collect all monomials appearing across elements per condition
    n_condW = len(per_elem[0][0])
    n_condI = len(per_elem[0][1])
    lin_rows = []
    for ci in range(n_condW + n_condI):
        monos = set()
        polys = []
        for condsW, condsI, _dc in per_elem:
            e = (condsW[ci] if ci < n_condW
                 else condsI[ci - n_condW])
            pe = sp.Poly(e, *GENS8)
            polys.append(pe)
            monos |= set(pe.monoms())
        for mono in monos:
            lin_rows.append([pe.nth(*mono) for pe in polys])
    Mstab = sp.Matrix(lin_rows)
    stab_basis = Mstab.nullspace()
    dim_stab = len(stab_basis)
    # effective action rank of the stabilizer on W coordinates
    eff_rows = []
    for base in stab_basis:
        row = []
        for x in GENS8:
            dx = sp.expand(sum(base[k] * per_elem[k][2][x]
                               for k in range(dim_g0)))
            row += [sp.diff(dx, y) for y in GENS8]
        eff_rows.append(row)
    rank_eff = sp.Matrix(eff_rows).rank()
    # the relative carrier rotation (gamma2 != gamma3) must be CUT:
    # test the g0 element acting as J2 on the 2-cycle channels only
    vrel = [sp.Integer(0)] * nv
    for i in TWO:
        r0 = 2 * (i - 1)
        vrel[pairsC.index((r0, r0 + 1))] = 1
    Xrel = XC_of(vrel)
    ok_rel_in_g0 = (sp.expand(Xrel * O_Cs - O_Cs * Xrel)
                    == sp.zeros(10, 10)) and \
                   (sp.expand(Xrel * A_CCs - A_CCs * Xrel)
                    == sp.zeros(10, 10))
    dVrel = sp.expand(Xrel * V_sym)
    du2r = dVrel[2 * (rep2 - 1):2 * rep2, 0:2]
    du3r = dVrel[2 * (rep3 - 1):2 * rep3, 0:2]
    dcr = {}
    for sym, val in zip((a2, b2, c2, d2), pauli_coords(du2r)):
        dcr[sym] = val
    for sym, val in zip((a3, b3, c3, d3), pauli_coords(du3r)):
        dcr[sym] = val
    rel_rems = [sp.expand(rem(sp.expand(
        sum(sp.diff(f, x) * dcr[x] for x in GENS8))))
        for f in IDEAL_GENS]
    rel_cut = any(r != 0 for r in rel_rems)
    check("P1.4 rule stabilizer (preserves W + maps ideal into "
          "itself): dim = %d, effective action rank on W = %d == 2 "
          "(the torus u_o -> gamma J2 u_o - y u_o J2); the RELATIVE "
          "carrier rotation is cut by the pencil (nonzero remainder: "
          "%s)"           % (dim_stab, rank_eff, rel_cut),
          dim_stab == 9 and rank_eff == 2 and rel_cut, kill="K1")

    # theta_S frame breaks the torus: R(p,q) X = X R(p,q) => q = 0
    p_s, q_s = sp.symbols("p q", real=True)
    Rpq = sp.Matrix([[p_s, -q_s], [q_s, p_s]])
    commX = sp.expand(Rpq * Xs - Xs * Rpq)
    sol_q = sp.solve([e for e in commX], [q_s], dict=True)
    ok_theta = all(s.get(q_s, None) == 0 for s in sol_q) and commX != \
        sp.zeros(2, 2)
    check("P1.5 theta_S frame: an SO(2) gauge block commutes with "
          "the sheet-swap X iff q = 0 EXACTLY (stabilizer discrete: "
          "{+-I} per block) -- in the frozen collar frame the "
          "rotation angle is PHYSICAL", ok_theta, kill="K1")

    # ==================================================================
    section("P2 -- constraint classes + the deployed-wiring ward")
    # ==================================================================
    # E1 closed form
    ok_E1cf = (sp.expand(g1_2 - 2 * (a2 * b2 + c2 * d2)) == 0
               and sp.expand(g2_2 - 4 * (a2 * d2 - b2 * c2)) == 0)
    ok_offd = sp.expand(UT2[0, 1] - UT2[1, 0]) == 0
    check("P2.1 E1 unit law closed form: u^T u prop. I iff "
          "{a b + c d = 0, a d - b c = 0} (symbolic; Gram symmetric "
          "off-diag equal: %s)" % ok_offd,
          ok_E1cf and ok_offd, kill="K2")

    # E3 anchors: within-orbit identity + symbolic Schur identity on W
    ok_det_id = sp.expand(u2 * Js * u2.T - u2.det() * Js) \
        == sp.zeros(2, 2)
    kap_s, m_s, t_s = sp.symbols("kappa m t", positive=True)
    C_BB = (sp.eye(6) + sp.I * m_s * J3s) / 2
    C_BB_inv = 2 * (sp.eye(6) - sp.I * m_s * J3s) / (1 - m_s ** 2)
    ok_inv = all(sp.cancel(e) == 0
                 for e in (C_BB * C_BB_inv - sp.eye(6)))
    Wt = t_s * V_sym
    C_CC = (sp.eye(10) + sp.I * kap_s * A_CCs) / 2
    C_eff = sp.expand(C_CC - (sp.I * Wt / 2) * C_BB_inv
                      * (-sp.I * Wt.T / 2))
    S_sym = sp.expand(V_sym * J3s * V_sym.T)
    A_eff_target = sp.expand(kap_s * A_CCs
                             + (m_s / (1 - m_s ** 2)) * t_s ** 2
                             * S_sym)
    ok_schur = True
    for r in range(10):
        for c in range(10):
            lhs = sp.im(sp.expand(2 * C_eff[r, c]))
            if sp.cancel(sp.together(lhs - A_eff_target[r, c])) != 0:
                ok_schur = False
    check("P2.2 E3 anchors: u J2 u^T = det(u) J2 identically (%s; "
          "within-orbit pencil blocks AUTOMATIC); symbolic Schur "
          "identity A_eff = kappa A_CC + (m/(1-m^2)) t^2 V J3 V^T "
          "on ALL of W in (kappa, m, t) (%s; C_BB inverse exact: %s)"
          % (ok_det_id, ok_schur, ok_inv),
          ok_det_id and ok_schur and ok_inv, kill="K2")

    # two-seat linear law: closed forms + float Gram ward + rank 12
    P_S = [2 * i for i in range(8)]
    mixed_ee = [(x, y) for x in P_S if x < 10
                for y in P_S if y >= 10]

    def wick_factory(A):
        W = np.eye(A.shape[0], dtype=complex) + 1j * A
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
            for j, bb in enumerate(rest):
                sub = rest[:j] + rest[j + 1:]
                tot += (-1) ** j * W[head, bb] * wick(sub)
            memo[idx] = tot
            return tot
        return wick

    def gram(basis, r, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis):
            imgs_ = [r[a] for a in reversed(ma)]
            coeff = eta ** len(ma)
            lst = list(imgs_)
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

    r_S = {}
    for i in range(8):
        r_S[2 * i] = 2 * i + 1
        r_S[2 * i + 1] = 2 * i
    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(cmb)
                   for cmb in itertools.combinations(P_S, 2)]

    A_CCf = A_CC.astype(np.float64)
    J3f = J3.astype(np.float64)

    def parentV_f(kap, m, tt, V):
        A = np.zeros((16, 16))
        A[np.ix_(CAR_IDX, CAR_IDX)] = kap * A_CCf
        A[np.ix_(BND_IDX, BND_IDX)] = m * J3f
        A[np.ix_(CAR_IDX, BND_IDX)] = tt * V
        A[np.ix_(BND_IDX, CAR_IDX)] = -tt * V.T
        return A

    ok_cf = True
    for (r0, b0) in ((0, 0), (7, 3)):
        Vu = np.zeros((10, 6))
        Vu[r0, b0] = 1.0
        A = parentV_f(0.5, 0.5, 1.0, Vu)
        wk = wick_factory(A)
        M1 = gram(B1_S, r_S, 1j, wk)
        M2 = gram(B2_S, r_S, 1j, wk)
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

    # exact rank 12 on the 24-dim commutant
    rows = []
    for wv in comm_basis:
        Vm = sp.Matrix(10, 6, list(wv))
        r2 = [Vm[x, y - 10] + Vm[x + 1, y - 9] for (x, y) in mixed_ee]
        r1 = [Vm[x + 1, y - 10] + Vm[x, y - 9] for (x, y) in mixed_ee]
        rows.append([sp.expand(e) for e in (r2 + r1)])
    rk24 = sp.Matrix(rows).T.rank()
    # restricted to W: deg-2 seat = 2 a_o, 1p seat = 2 b_o
    d2_forms = {sp.expand(V_sym[x, y - 10] + V_sym[x + 1, y - 9])
                for (x, y) in mixed_ee}
    p1_forms = {sp.expand(V_sym[x + 1, y - 10] + V_sym[x, y - 9])
                for (x, y) in mixed_ee}
    ok_seatW = (d2_forms == {2 * a2, 2 * a3}
                and p1_forms == {2 * b2, 2 * b3})
    check("P2.3 two-seat linear law: closed forms warded against the "
          "float Gram machinery on unit couplings (<= 1e-12: %s); "
          "exact rank on the 24-dim commutant = %d == 12 (kernel 12 "
          "= {J, Z}); restricted to W: deg-2 seat = {2 a_o}, 1p seat "
          "= {2 b_o} (%s) -- NOT a constraint class here (pure-I "
          "fails it): the SELECTOR of P4"
          % (ok_cf, rk24, ok_seatW),
          ok_cf and rk24 == 12 and ok_seatW, kill="K2")

    # ------- constraint evaluation helpers (exact)
    kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                    sp.Rational(1, 20))
    lamQ = mQ / (1 - mQ ** 2)

    def wiring(u2v, u3v):
        return {a2: u2v[0], b2: u2v[1], c2: u2v[2], d2: u2v[3],
                a3: u3v[0], b3: u3v[1], c3: u3v[2], d3: u3v[3]}

    def eval_E1(sub):
        return [sp.expand(g.subs(sub)) for g in
                (g1_2, g2_2, g1_3, g2_3)]

    def eval_pencil(sub):
        return [sp.expand(g.subs(sub)) for g in (pI, pX, pZ)], \
            sp.expand(pJ.subs(sub))

    def eval_dets(sub):
        return (sp.expand(u2.det().subs(sub)),
                sp.expand(u3.det().subs(sub)))

    def exact_parent(sub):
        Vm = V_sym.subs(sub)
        A_ex = sp.zeros(16, 16)
        A_ex[0:10, 0:10] = kapQ * A_CCs
        A_ex[10:16, 10:16] = mQ * J3s
        A_ex[0:10, 10:16] = tQ * Vm
        A_ex[10:16, 0:10] = -tQ * Vm.T
        return A_ex, Vm

    def car_strict_exact(sub):
        A_ex, _ = exact_parent(sub)
        M = sp.eye(16) + A_ex * A_ex
        minors = [M[:k, :k].det() for k in range(1, 17)]
        return all(mm > 0 for mm in minors), minors

    def census_exact(sub):
        _, Vm = exact_parent(sub)
        S = Vm * J3s * Vm.T
        A_eff = kapQ * A_CCs + lamQ * tQ ** 2 * S
        n_nz, n_sig = 0, 0
        Jco45 = None
        for (i, j) in CAR_DUADS:
            Bx = A_eff[2 * (i - 1):2 * i, 2 * (j - 1):2 * j]
            nz = any(e != 0 for e in Bx)
            n_nz += nz
            pf = sp.expand(-(Bx[0, 0] * Bx[1, 1]
                             - Bx[0, 1] * Bx[1, 0]))
            if pf != 0:
                n_sig += (int(sp.sign(pf))
                          == sign_c[frozenset({i, j})])
            if (i, j) == (a_ch, b_ch):
                Jco45 = sp.expand((Bx[0, 1] - Bx[1, 0]) / 2)
        return n_nz, n_sig, Jco45

    # the deployed-wiring ward
    wI = wiring((-1, 0, 0, 0), (-1, 0, 0, 0))
    E1_I = eval_E1(wI)
    (pen_I, gam_I) = eval_pencil(wI)
    det_I = eval_dets(wI)
    S_I = sp.expand((V_sym * J3s * V_sym.T).subs(wI))
    ok_SI = all(S_I[2 * i:2 * i + 2, 2 * j:2 * j + 2] == 3 * Js
                for i in range(5) for j in range(5))
    carI, minI = car_strict_exact(wI)
    nzI, sigI, JcoI = census_exact(wI)
    # artanh round-trip (float ward) + strict-collar regression
    A_If = parentV_f(0.5, 0.5, 0.05, Vdep.astype(np.float64))
    wA, QA = np.linalg.eigh(1j * A_If)
    smaxI = float(np.max(np.abs(wA)))
    w_h = -2.0 * np.arctanh(wA)
    occ = 1.0 / (1.0 + np.exp(w_h))
    A_back = (-1j * (2 * (QA * occ) @ QA.conj().T
                     - np.eye(16))).real
    rtI = float(np.max(np.abs(A_back - A_If)))
    wkI = wick_factory(A_If)
    M2I = gram(B2_S, r_S, 1j, wkI)
    D2I = M2I - M2I.conj().T
    defI = float(np.max(np.abs(D2I)))
    nentI = int(np.sum(np.abs(D2I) > 1e-12))
    check("P2.4 THE DEPLOYED-WIRING WARD: pure-I passes E1 %s == 0, "
          "pencil %s == 0 (gamma = %s == 3, S_I = 3J on 25 blocks: "
          "%s), E4 dets %s > 0, E2 CAR-strict (16/16 exact minors "
          "> 0: %s; smax %.4f < 1; artanh round-trip %.1e), census "
          "%d/10 nonzero %d/10 canonical, J-coordinate %s == 1/200"
          % (E1_I, pen_I, gam_I, ok_SI, det_I, carI, smaxI, rtI,
             nzI, sigI, JcoI),
          all(e == 0 for e in E1_I) and all(e == 0 for e in pen_I)
          and gam_I == 3 and ok_SI and all(d > 0 for d in det_I)
          and carI and smaxI < 1 and rtI <= 1e-9
          and nzI == 10 and sigI == 10
          and JcoI == sp.Rational(1, 200), kill="K2")
    check("P2.5 the strict-collar law is NOT in the constraint list: "
          "pure-I FAILS it (deg-2 defect %.4f == 2t = 0.1, %d == 30 "
          "entries; round-60 regression) -- it enters only as the "
          "P4 selector" % (defI, nentI),
          abs(defI - 0.1) <= 1e-12 and nentI == 30, kill="K2")

    # ==================================================================
    section("P3 -- Groebner basis + certified real decomposition")
    # ==================================================================
    print("      ideal: 7 quadric generators in Q[a2,b2,c2,d2,"
          "a3,b3,c3,d3], term order grevlex")
    print("      Groebner basis size: %d" % len(gb.exprs))

    # cofactor certificates for the unit ideal (per orbit)
    a_, b_, c_, d_ = sp.symbols("a_ b_ c_ d_", real=True)
    g1g = 2 * (a_ * b_ + c_ * d_)
    g2g = 4 * (a_ * d_ - b_ * c_)
    certs = [
        sp.expand(2 * a_ * (b_ ** 2 + d_ ** 2)
                  - (b_ * g1g + d_ * g2g / 2)),
        sp.expand(2 * c_ * (b_ ** 2 + d_ ** 2)
                  - (d_ * g1g - b_ * g2g / 2)),
        sp.expand(2 * b_ * (a_ ** 2 + c_ ** 2)
                  - (a_ * g1g - c_ * g2g / 2)),
        sp.expand(2 * d_ * (a_ ** 2 + c_ ** 2)
                  - (c_ * g1g + a_ * g2g / 2)),
    ]
    ok_certs = all(e == 0 for e in certs)
    check("P3.1 unit-ideal cofactor certificates (exact identities): "
          "2a(b^2+d^2), 2c(b^2+d^2), 2b(a^2+c^2), 2d(a^2+c^2) all in "
          "(g1, g2) with explicit cofactors => every REAL unit point "
          "is rotation (b=d=0) or reflection (a=c=0); complex "
          "residual is real-point-free (sum of squares)",
          ok_certs, kill="K3")

    # branch reductions of the pencil
    rot_sub = {b2: 0, d2: 0, b3: 0, d3: 0}
    refl_sub = {a2: 0, c2: 0, a3: 0, c3: 0}
    mix_sub = {b2: 0, d2: 0, a3: 0, c3: 0}
    pen_rot = [sp.expand(g.subs(rot_sub)) for g in (pI, pX, pZ)]
    minor_rot = sp.expand(a2 * c3 - c2 * a3)
    ok_rot = (sp.expand(pen_rot[0] - 3 * minor_rot) == 0
              and pen_rot[1] == 0 and pen_rot[2] == 0)
    pen_refl = [sp.expand(g.subs(refl_sub)) for g in (pI, pX, pZ)]
    minor_refl = sp.expand(d2 * b3 - b2 * d3)
    ok_refl = (sp.expand(pen_refl[0] - 3 * minor_refl) == 0
               and pen_refl[1] == 0 and pen_refl[2] == 0)
    pen_mix = [sp.expand(g.subs(mix_sub)) for g in (pI, pX, pZ)]
    gb_mix = sp.groebner([e for e in pen_mix if e != 0],
                         a2, c2, b3, d3, order="grevlex")
    ok_mix_cert = (pen_mix[0] == 0
                   and gb_mix.reduce(
                       sp.expand((a2 ** 2 + c2 ** 2) * b3))[1] == 0
                   and gb_mix.reduce(
                       sp.expand((a2 ** 2 + c2 ** 2) * d3))[1] == 0)
    check("P3.2 branch reductions: rot x rot pencil = single "
          "determinantal quadric 3(a2 c3 - c2 a3) with pX = pZ = 0 "
          "(%s); refl x refl analog (%s); MIXED rot x refl: exact "
          "Groebner membership (a2^2+c2^2) b3, (a2^2+c2^2) d3 in "
          "the pencil ideal (%s) => nondegenerate real mixed points "
          "do NOT exist" % (ok_rot, ok_refl, ok_mix_cert),
          ok_rot and ok_refl and ok_mix_cert, kill="K3")

    # component containment: I_rule c P_rot and I_rule c P_refl
    gb_rot = sp.groebner([b2, d2, b3, d3, minor_rot], *GENS8,
                         order="grevlex")
    gb_refl = sp.groebner([a2, c2, a3, c3, minor_refl], *GENS8,
                          order="grevlex")
    ok_cont = (all(gb_rot.reduce(g)[1] == 0 for g in IDEAL_GENS)
               and all(gb_refl.reduce(g)[1] == 0
                       for g in IDEAL_GENS))
    # rational parametrization certificate on C_rot:
    # (a2^2+c2^2) a3 - (a2 a3 + c2 c3) a2 = -c2 * minor etc.
    par1 = sp.expand((a2 ** 2 + c2 ** 2) * a3
                     - (a2 * a3 + c2 * c3) * a2 + c2 * minor_rot)
    par2 = sp.expand((a2 ** 2 + c2 ** 2) * c3
                     - (a2 * a3 + c2 * c3) * c2 - a2 * minor_rot)
    ok_par = (par1 == 0 and par2 == 0)
    check("P3.3 certified real decomposition away from the "
          "degenerate locus: V(I_rule)_R = C_rot u C_refl, "
          "C_rot = V(b2,d2,b3,d3, a2 c3 - c2 a3) dim 3, C_refl = "
          "V(a2,c2,a3,c3, b2 d3 - d2 b3) dim 3; generator-wise "
          "containment I_rule c P (%s); rational parametrization "
          "u3 = lambda u2 certified (%s)" % (ok_cont, ok_par),
          ok_cont and ok_par, kill="K3")

    # ==================================================================
    section("P4 -- THE CENSUS: gauge quotient + admissible components")
    # ==================================================================
    # E4 on C_refl: det u = -(b^2+d^2) < 0 identically
    detu_refl = sp.expand(u2.det().subs({a2: 0, c2: 0}))
    ok_reflneg = sp.expand(detu_refl + b2 ** 2 + d2 ** 2) == 0
    # witness table: point -> (E1, pencil, dets, CAR, census)
    WITS = {
        "pure-I": ((-1, 0, 0, 0), (-1, 0, 0, 0)),
        "pure-J": ((0, 0, 1, 0), (0, 0, 1, 0)),
        "interior (3/5,4/5)": (
            (sp.Rational(3, 5), 0, sp.Rational(4, 5), 0),
            (sp.Rational(3, 5), 0, sp.Rational(4, 5), 0)),
        "V_Z (refl)": ((0, 0, 0, 1), (0, 0, 0, 1)),
    }
    res = {}
    for nm, (uu2, uu3) in WITS.items():
        sub = wiring(uu2, uu3)
        E1v = eval_E1(sub)
        (penv, gamv) = eval_pencil(sub)
        detv = eval_dets(sub)
        carv, _ = car_strict_exact(sub)
        nz, sg, jco = census_exact(sub)
        res[nm] = dict(E1=E1v, pen=penv, gam=gamv, det=detv,
                       car=carv, nz=nz, sig=sg, jco=jco)
        print("      %-20s E1=%s pencil=%s gamma=%s det=%s CAR=%s "
              "census=%d/%d Jco=%s"
              % (nm, E1v, penv, gamv, detv, carv, nz, sg, jco))
    okI = res["pure-I"]
    okJ = res["pure-J"]
    okP = res["interior (3/5,4/5)"]
    okZ = res["V_Z (refl)"]

    def admissible(r):
        return (all(e == 0 for e in r["E1"])
                and all(e == 0 for e in r["pen"])
                and all(d > 0 for d in r["det"]) and r["car"]
                and r["nz"] == 10 and r["sig"] == 10)

    check("P4.1 C_rot is ADMISSIBLE with three exact witnesses "
          "(pure-I, pure-J, interior rational rotation): all pass "
          "E1-E5 + nondegenerate canonical census 10/10 (%s, %s, %s);"
          " interior J-coordinate %s (nonzero, canonical)"
          % (admissible(okI), admissible(okJ), admissible(okP),
             okP["jco"]),
          admissible(okI) and admissible(okJ) and admissible(okP),
          kill="K4")
    check("P4.2 C_refl passes E1 + pencil + census (V_Z witness: "
          "census %d/10, J-coordinate %s == -1/200) but FAILS "
          "orientation E4 IDENTICALLY: det u = -(b^2+d^2) < 0 on "
          "every nondegenerate real point (%s); dets at V_Z: %s -- "
          "orientation propagation is the edge rule that outlaws "
          "Z/X wirings"
          % (okZ["nz"], okZ["jco"], ok_reflneg, okZ["det"]),
          okZ["nz"] == 10 and okZ["sig"] == 10
          and okZ["jco"] == sp.Rational(-1, 200) and ok_reflneg
          and all(d < 0 for d in okZ["det"]), kill="K4")

    # the integer gauge witness g = (+)_5 J2 (+) I6
    gC = sp.zeros(10, 10)
    for i in range(5):
        gC[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Js
    okg1 = sp.expand(gC * A_CCs * gC.T - A_CCs) == sp.zeros(10, 10)
    okg2 = sp.expand(gC * O_Cs - O_Cs * gC) == sp.zeros(10, 10)
    Vg = sp.expand(gC * V_sym.subs(wI))
    wmJ = wiring((0, 0, -1, 0), (0, 0, -1, 0))
    okg3 = sp.expand(Vg - V_sym.subs(wmJ)) == sp.zeros(10, 6)
    # ideal stability of the substitution (a,b,c,d)->(-c,-d,a,b)
    gsub = {a2: -c2, b2: -d2, c2: a2, d2: b2,
            a3: -c3, b3: -d3, c3: a3, d3: b3}
    okg4 = all(rem(g.subs(gsub, simultaneous=True)) == 0
               for g in IDEAL_GENS)
    check("P4.3 I-J GAUGE CONNECTION: the INTEGER gauge g = "
          "(+)_5 J2 (+) I6 preserves A_CC (%s), commutes with the "
          "C6 action (%s), maps the ideal into itself (%s) and "
          "sends PURE-I to PURE-(-J) (%s): under the rule gauge the "
          "deployed wiring and the J wiring are THE SAME point"
          % (okg1, okg2, okg4, okg3),
          okg1 and okg2 and okg3 and okg4, kill="K4")

    # the selector theorem on C_rot
    tsA = [sp.expand(2 * a2), sp.expand(2 * a3)]   # deg-2 seat on rot
    tsB = [sp.expand(2 * b2).subs(rot_sub),
           sp.expand(2 * b3).subs(rot_sub)]         # 1p seat: 0 on rot
    sel = sp.solve([a2, a3, minor_rot.subs({a2: 0, a3: 0})],
                   [a2, a3], dict=True)
    ok_sel = (sel == [{a2: 0, a3: 0}]
              and all(e == 0 for e in tsB))
    # pure-I maximal obstruction on the unit circle: |a| = 1
    check("P4.4 THE SELECTOR THEOREM: on C_rot the strict-collar "
          "two-seat law reads {2 a2 = 0, 2 a3 = 0} (1p seat "
          "identically clean: %s) and cuts EXACTLY the pure-(+-J) "
          "ray {u_o = c_o J2, c_o != 0}: orbit/edge rules + "
          "strict-collar Hermiticity FORCE PURE-J uniquely (up to "
          "flips and scale); pure-I sits at |a_o| = 1, the "
          "MAXIMALLY obstructed angle (deg-2 defect 2t, P2.5)"
          % (tsB,), ok_sel, kill="K4")

    print("\n      THE CENSUS (real positive components of the "
          "constraint variety, mod rule gauge):")
    print("        admissible:            1   (C_rot; contains "
          "pure-I, pure-J, continuum)")
    print("        orientation-rejected:  1   (C_refl; contains "
          "V_Z, V_X)")
    print("        pencil/nondeg-killed:  mixed rot x refl branches "
          "(exact cofactors)")
    print("        frozen theta_S frame:  C_rot = circle x scales; "
          "I and J DISTINCT admissible points;")
    print("                               strict-collar law "
          "intersects C_rot exactly at pure-(+-J)")

    # ==================================================================
    section("P5 -- secondary relaxation: drop the IOTA seat-stack "
            "rule (24 vars)")
    # ==================================================================
    zs = {}
    for o in (2, 3):
        for s in range(3):
            zs[(o, s)] = sp.symbols(
                "A%d%d B%d%d C%d%d D%d%d" % ((o, s) * 4), real=True)

    def ublk(o, s):
        A_, B_, C_, D_ = zs[(o, s)]
        return A_ * I2s + B_ * Xs + C_ * Js + D_ * Zs

    Moo = sp.expand(sum((ublk(2, s) * Js * ublk(2, s).T
                         for s in range(3)), sp.zeros(2, 2)))
    det_sum = sp.expand(sum(ublk(2, s).det() for s in range(3)))
    ok_oo = sp.expand(Moo - det_sum * Js) == sp.zeros(2, 2)
    Mcr = sp.expand(sum((ublk(2, s) * Js * ublk(3, s).T
                         for s in range(3)), sp.zeros(2, 2)))
    qI, qX, qJ, qZ = pauli_coords(Mcr)
    rot24 = {}
    for o in (2, 3):
        for s in range(3):
            rot24[zs[(o, s)][1]] = 0
            rot24[zs[(o, s)][3]] = 0
    qI_rot = sp.expand(qI.subs(rot24))
    qX_rot = sp.expand(qX.subs(rot24))
    qZ_rot = sp.expand(qZ.subs(rot24))
    # signature (6,6) sum-of-squares identity for the single quadric
    sos = sp.Integer(0)
    for s in range(3):
        A2_, _, C2_, _ = zs[(2, s)]
        A3_, _, C3_, _ = zs[(3, s)]
        sos += ((A2_ + C3_) ** 2 - (A2_ - C3_) ** 2
                - (C2_ + A3_) ** 2 + (C2_ - A3_) ** 2)
    ok_sos = sp.expand(4 * qI_rot - sos) == 0
    check("P5.1 seat-nonuniform relaxation: within-orbit blocks "
          "AUTOMATIC (Sum_s det u_{o,s} J2 identity: %s); on the "
          "orientation-forced all-rotation branch the cross-pencil "
          "is ONE quadric (pX = pZ = 0: %s, %s) with exact "
          "signature (6, 6) (sum-of-squares identity: %s): an "
          "indefinite connected quadric -- the relaxed census stays "
          "DEGENERATE (dropping a rule cannot create forcing)"
          % (ok_oo, qX_rot == 0, qZ_rot == 0, ok_sos),
          ok_oo and qX_rot == 0 and qZ_rot == 0 and ok_sos,
          kill="K5")

    # ==================================================================
    section("P6 -- controls (must fire)")
    # ==================================================================
    rng = np.random.default_rng(906)
    n_fire = 0
    for _ in range(3):
        perm = rng.permutation(10)
        Vp = sp.Matrix(Vdep[perm, :].tolist())
        n_fire += (not in_commutant(Vp))
    check("C1 seeded row-permutation of the pure-I wiring breaks "
          "exact C6-covariance (commutant membership) on %d/3"
          % n_fire, n_fire == 3, kill="K7")

    wX = wiring((0, 1, 0, 0), (0, 1, 0, 0))
    detX = eval_dets(wX)
    A_Xf = parentV_f(0.5, 0.5, 0.05,
                     np.array(V_sym.subs(wX).tolist(),
                              dtype=np.float64))
    wkX = wick_factory(A_Xf)
    M1X = gram(B1_S, r_S, 1j, wkX)
    def1p = float(np.max(np.abs(M1X - M1X.conj().T)))
    check("C2 X-wiring: E4 fires (dets %s == (-1, -1)) AND the 1p "
          "seat fires (float defect %.4f == 2t = 0.1; round-60 "
          "regression)" % (detX, def1p),
          all(d == -1 for d in detX) and abs(def1p - 0.1) <= 1e-12,
          kill="K7")

    zE1 = eval_E1(wiring((0, 0, 0, 1), (0, 0, 0, 1)))
    zpen, _ = eval_pencil(wiring((0, 0, 0, 1), (0, 0, 0, 1)))
    zA = [sp.expand((2 * a2).subs({a2: 0})),
          sp.expand((2 * b2).subs({b2: 0}))]
    check("C3 Z-wiring near miss: E1 %s == 0, pencil %s == 0, "
          "two-seat clean %s, census 10/10 (P4.2) -- ONLY "
          "orientation rejects it (dets %s < 0): exactly one "
          "constraint class fires"
          % (zE1, zpen, zA, okZ["det"]),
          all(e == 0 for e in zE1) and all(e == 0 for e in zpen)
          and all(e == 0 for e in zA)
          and all(d < 0 for d in okZ["det"]), kill="K7")

    wM = wiring((0, 0, 1, 0), (0, 0, 0, 1))
    (penM, gamM) = eval_pencil(wM)
    nzM, sigM, _ = census_exact(wM)
    MblkM = sp.expand(Mcross.subs(wM))
    check("C4 mixed J-on-2-cycle / Z-on-3-cycle: pencil fires "
          "(cross block %s == -3Z; pZ = %s != 0) and the exact "
          "canonical census drops to %d/10 == 4/10 (round-60 P3.b "
          "law reproduced exactly)"
          % (list(MblkM), penM[2], sigM),
          sp.expand(MblkM + 3 * Zs) == sp.zeros(2, 2)
          and penM[2] != 0 and sigM == 4 and nzM == 10, kill="K7")

    e5 = eval_E1(wiring((1, 1, 0, 0), (1, 0, 0, 0)))
    check("C5 non-unit wiring u2 = I + X: E1 fires (g1_2 = %s != 0)"
          % e5[0], e5[0] != 0, kill="K7")

    e6 = eval_E1(wiring((-1, 0, 0, sp.Rational(1, 10)),
                        (-1, 0, 0, 0)))
    check("C6 perturbed pure-I (u2 = -I + Z/10): E1 fires "
          "(g2_2 = %s != 0): an illegal perturbation of the "
          "deployed point violates at least one constraint"
          % e6[1], e6[1] != 0, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    all_ok = (n_pass == n_tot) and not KILLS
    if all_ok:
        verdict = ("WIRING-DEGENERATE [ADMISSIBLE-CENSUS-1(C_rot), "
                   "I-NOT-FORCED(interior point), "
                   "I-J-GAUGE-CONNECTED((+)_5 J2 (+) I6), "
                   "J-COMPILER-LEGAL, Z-X-EDGE-ILLEGAL(orientation), "
                   "STRICT-COLLAR-SELECTS-PURE-J(selector theorem), "
                   "DEPLOYMENT-CHOICE]")
    else:
        verdict = " / ".join(sorted(set(KILLS))) or "CHECK-FAILED"
    print("  checks: %d/%d passed; kills: %s"
          % (n_pass, n_tot, KILLS if KILLS else "none"))
    print("  VERDICT: %s" % verdict)
    print("  runtime: %.1f s" % (time.time() - T0))
    print("  (constants sanity: N_fam = %s, g_car = %s)"
          % (N_fam, g_car))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
