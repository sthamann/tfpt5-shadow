#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v911 -- SEAM.STATE.WIRING.SELECTOR.01 (the v908-registered contract) + SEAM.STATE.THETA.SELECTOR.01 + SEAM.STATE.WIRING.GAUGE.RP.01: THE WIRING FREEDOM THEOREM -- the seam wiring question of round 60 (CXXXIX: "is the deployed PURE-I wiring compiler-forced?") is CLOSED as a compiler-freedom theorem, ONE module from three probes (30/30 + 26/26 + 21/21 checks, zero fails; verdicts WIRING-DEGENERATE + THETA-CONVENTIONAL + RP-FRAME-COVARIANT; discovery probes seam_wiring_groebner_probe.py (Spec-SHA 251a9a80.., note CCXIII), theta_frame_selector_probe.py (Spec-SHA c042726f.., note CCXV), wiring_gauge_rp_audit_probe.py (Spec-SHA 58a9d445.., note CCXXI), rounds 69-71, 2026-08-12, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~90 s).

THE CANONICAL SENTENCE (frozen verbatim in the RP audit, sha256 79950314..): "The exact Groebner census determines a single admissible three-dimensional wiring orbit (the rotation cell C_rot); Z- and X-wirings are excluded by orientation propagation, and this exclusion is rule-gauge-invariant.  Pure-I and pure-J are connected by an integer rule-gauge element and lie on one orbit: pure-I is a deployment representative, not a compiler theorem.  Strict collar reflection positivity is covariant under the rule gauge and depends only on the relative angle delta between collar frame and wiring: strict Hermiticity in the theta_S frame would select pure-J; the same demand in the integer-conjugated frame selects pure-I.  A canonical wiring selection requires an additionally derived physical frame."  FORBIDDEN (equally frozen): "pure-I is compiler-forced"; "the compiler derives the pure-I wiring"; "strict collar RP excludes the J-wiring" (without the frame qualifier).

(1) THE GROEBNER CENSUS (seam_wiring_groebner, 30/30, WIRING-DEGENERATE): the C6-equivariant commutant of the 10x6 coupling space is EXACTLY {2 channel orbits} x {3 boundary seats} x M2(R) = 24-dim (the boundary C6 action is the IDENTITY, O_B = I6); the IOTA seat-stack rule subspace W is 8-dim and contains the deployed PURE-I point (-1,0,0,0|-1,0,0,0); the constraint classes E1 (unit law {ab+cd, ad-bc}), E2 (CAR/KMS, 16/16 exact leading minors at the frozen (1/2, 1/2, 1/20) parent), E3 (Pfaffian pencil, 3 cross quadrics, anchored by the SYMBOLIC Schur identity A_eff = kappa A_CC + (m/(1-m^2)) t^2 V J3 V^T on all of W; within-orbit automatic via u J2 u^T = det(u) J2), E4 (orientation propagation det u > 0) and E5 (covariance + seat stack) are ALL warded exactly at the deployed point (census 10/10, J coordinate exactly +1/200; S_I = 3J = S_J -- the pencil does not distinguish I from J at all); the Groebner basis (7 quadrics, grevlex, 21 elements) decomposes the real variety CERTIFIED into C_rot = V(b2, d2, b3, d3, a2 c3 - c2 a3) and C_refl = V(a2, c2, a3, c3, b2 d3 - d2 b3) (each dim 3; cofactor certificates; mixed branches have no nondegenerate real points; the complex residue is real-point-free); THE CENSUS: exactly ONE admissible component mod rule gauge (C_rot, witnesses pure-I, pure-J and the INTERIOR rational point (3/5, 4/5)); pure-I is an INTERIOR POINT, not a vertex, and the INTEGER gauge g_int = (+)_5 J2 (+) I6 (preserving A_CC, C6, W and the ideal) maps pure-I onto the pure-J ray -- I and J are rule-gauge-equivalent; C_refl (contains V_Z, census 10/10, -1/200) falls at EXACTLY ONE class: orientation (det u = -(b^2 + d^2) < 0 identically) -- Z/X are edge-illegal; SELECTOR THEOREM: the strict-collar two-seat law (rank 12 / kernel 12 reproduced exactly) cuts C_rot EXACTLY in the pure-(+-J) ray -- rules + collar Hermiticity would force PURE-J uniquely (up to flips/scale), and pure-I sits at the MAXIMALLY obstructed angle (defect 2t, the round-60 regression); the secondary relaxation without the IOTA seat rule stays degenerate (one signature-(6,6) quadric, SOS identity).

(2) THE COLLAR-FRAME DECISION (theta_frame_selector, 26/26, THETA-CONVENTIONAL): NO compiler-side demand distinguishes the theta_S sheet-swap frame inside the 9-dim rule-gauge algebra -- the frame orbit tangent is 7 of 9 (isotropy 2), the torus generators K_C = (+)_5 J2 and K_B = (+)_3 J2 lie exactly in the stabilizer and move theta_S (the reflection circle cos(2 gamma) X + sin(2 gamma) Z per pair is rule-gauge reachable); the DEMAND CENSUS over five exact demand classes: D1 mu4/C6 COMPATIBLE-NOT-FORCING (family-defining, cuts nothing inside), D2 CAR/state SILENT (A0 = tanh(beta u/2) A16 exactly torus-invariant; coupled h(V) excluded by anti-circularity -- theta h(V) theta = -h(V) IS the relative-angle selector, not a frame demand), D3 pencil/orientation SILENT (no frame variable; det u' = det u exact), D4 doily/edge combinatorics COMPATIBLE-NOT-FORCING (refined stabilizer 9 OF 9 -- the bit level lives on channel labels, never the within-pair basis), D5 the round-59 census property SILENT-ON-ANGLE (bare-point strict RP spectra IDENTICAL on all four frames, closed forms lam_min 1p = tanh(1/2), deg-2 = tanh^2(1/2); the angle of theta_S is v440 LINEAGE, i.e. deployment); THE CLOSURE: the deployed parent (pure-I) PASSES strict collar RP EXACTLY in the integer frame theta' = g_int theta_S g_int^T (Grams exactly Hermitian, PD by exact LDL, float lam_min 0.3064/0.1532 = the round-60 V_J numbers transported) and fails at theta_S with raw defect 0.1 = 2t -- the round-58/59 strict-collar obstruction is FRAME-RELATIVE; equivariant selection map exact: frame (gamma, y) selects the ray (a_o, c_o) = lambda_o (-sin delta, cos delta), delta = y - gamma.

(3) THE GAUGE-COVARIANCE AUDIT (wiring_gauge_rp_audit, 21/21, RP-FRAME-COVARIANT; ordered by the program lead): CONJUGATION EXACT both directions (theta' = g_int theta_S g_int^{-1} AND theta_S = g_int theta' g_int^{-1}; g_int^2 lies in the isotropy of theta_S); the generic rule element acts as a delta-circle rotation (symbolic angle addition); THE KERNEL-COVARIANCE LAW symbolic on the full torus with generic wiring: g^T g = I16 and g^T A(V) g = A(g_C^T V g_B) IDENTICALLY, hence Gram(g theta g^T, gF, A(V)) = Gram(theta, F, A(V')) ENTRYWISE -- strict-collar RP is a function of the RELATIVE datum (frame, wiring) mod gauge only; exact Gram covariance at the witnesses (sympy expand == 0, 1p + deg-2); the witness table: (theta_S, pure-J), (theta', pure-I), (theta_r, (4/5, 3/5)) pass strict collar RP EXACTLY, the SAME pure-I fails at theta_S (defect 0.1) and the SAME pure-J fails at theta' (0.1, the mirror witness) -- the lead's OPTION (2) holds: the RP exclusion of pure-I is a statement AT THE FIXED FRAME theta_S, not a gauge-invariant wiring no-go; the Z/X exclusion IS genuinely orbit-invariant (det u = a^2 + c^2 - b^2 - d^2 frame-transport-invariant, C_refl has det <= 0 identically; the only orthogonal element that would flip det u flips the vacuum and leaves the rule gauge).

STATUS: closes the v908-registered contract SEAM.STATE.WIRING.SELECTOR.01 -- the answer is DEPLOYMENT-CHOICE, not compiler theorem; the CXXXIX question is closed as a compiler-freedom theorem (freedom group = the rule-gauge frame orbit, selection quotient = the delta-circle, the only gauge-invariant datum of (frame, wiring) is the relative angle).  The census covers the FIVE enumerated demand classes; a compiler demand OUTSIDE the list is not excluded; whether the actual seam physics derives a specific collar frame remains outside the formalized rules; the v898/v903 [O] premise stays [O].  Zero RH content.  No marker moves beyond this measured closure.

PROVENANCE: discovery probes re-run identically at promotion (30/30 in 1.3 s, 26/26 in 14.4 s, 21/21 in 69.6 s on 2026-08-12); ROUND-31 EMBEDDING CONVENTION: frozen sources embedded BYTE-EXACT, executed verbatim in isolated namespaces; printed Spec SHAs 251a9a80.. / c042726f.. / 58a9d445.. reproduce; byte-equality ward vs experiments/tfpt-discovery/ inside the pattern gates.  FIREWALL: exact integer/rational sympy census; float64 only in disclosed wards; RNG only in the declared scramble controls; no zeros, no prime oracles (AST firewalls inside the probes).  Python-only per GATE.WOLFRAM.02.
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

# ------------- frozen probe source seam_wiring_groebner_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
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
'''

# ------------- frozen probe source theta_frame_selector_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""theta_frame_selector_probe -- SEAM.STATE.THETA.SELECTOR.01
(EXPLORATION ONLY, experiments/; 2026-08-12 -- the collar-frame
decision named at the end of the wiring census, entry CCXIII: does
any compiler-side demand distinguish the theta_S sheet-swap frame
within the 9-dim rule-gauge algebra?  Only then does the selector
theorem (rules + strict collar => pure-J) become a compiler
statement about the deployed pure-I wiring.)

THE QUESTION (the CCXIII residual, verbatim scope).  The wiring
census (seam_wiring_groebner_probe, 30/30, WIRING-DEGENERATE)
proved: the orbit/edge rules E1-E5 leave EXACTLY ONE admissible
component C_rot (dim 3) modulo the rule gauge; pure-I is an
interior point, gauge-connected to pure-(-J) by the INTEGER gauge
g_int = (+)_5 J2 (+) I6; the frozen theta_S collar frame breaks
the gauge discretely, and the strict-collar two-seat law
intersects C_rot exactly in the pure-(+-J) ray (the SELECTOR
THEOREM).  Everything therefore hinges on ONE question: is the
theta_S frame itself compiler-FORCED, or is it a convention --
exactly formulable as the question whether any compiler-side
demand cuts the orbit of theta_S under the 9-dim rule-gauge
algebra down to a point (or subfamily).

FEASIBILITY / REDUNDANCY CHECK (against the corpus, 2026-08-12):
round 58 (seam_state_derivation) deployed theta_S BY HAND as the
16-dim lift of the v440 collar I (x) sigma_x and censused only the
two index-permutation reflections; round 59
(rp_twisted_involution_census) censused the 48 TWIST candidates
U_g^k o theta -- never the inner rule-gauge conjugates; the wiring
census (CCXIII) measured the frame-breaking (P1.5) but did not
parametrize the frame ORBIT nor test any demand ON frames.  That
is exactly this probe.

SMOKE-RUN DISCLOSURE (2026-08-12, declared smoke rounds before
freezing; fail-first preserved -- smoke-1 corrected FOUR
hand-predictions by measurement, none inverting the verdict
logic, and the machinery itself rejected one wrong guess):
 (i)   the orbit tangent space {[G, theta_S] : G in the 9-dim
       rule stabilizer} has dimension EXACTLY 7 (hand prediction
       was 6; isotropy 2, not 3 -- even the diagonal torus
       rotates the reflection, [J2, X] = 2Z != 0);
 (ii)  the refined D4 stabilizer is 9 OF 9 (hand prediction 8):
       EVERY rule-stabilizer direction already commutes with the
       deployed carrier-carrier interior A_int[C, C] exactly --
       the doily demand cuts NOTHING, stronger than predicted;
 (iii) the bare collar Gram spectra have exact closed forms
       lam_min(1p) = tanh(1/2) = 0.4621 and lam_min(deg-2) =
       tanh(1/2)^2 = 0.2136 (hand predictions 1 - tanh(1/2) and
       0.2311 were WRONG; the cross-frame equality ward <= 1e-10
       is the decisive statement and was correct);
 (iv)  the selection-map sign convention: with J = [[0,1],[-1,0]]
       a rotation R(t) = cos t I - sin t J, so the transported
       deg-2 seat reads a' = a C + c S (not a C - c S) and the
       selected ray is (a_o, c_o) = lambda_o (-S, C); the smoke
       run itself REJECTED the wrongly-signed theta_r ray
       (-4/5, 3/5) via a broken deg-2 Hermiticity -- the correct
       selected ray is (4/5, 3/5), fixed and re-verified (the
       float defect ward 0.06 was correct throughout);
 (v)   implementation-level: the D2 float route for
       A0 = -tan(beta h0 / 2) is evaluated through the Hermitian
       eigenbasis of i h0 (the first smoke attempt double-counted
       the -i rotation); C2's exact pencil violation is -4/5
       (sign from R^T J = (3/5) J - (4/5) I), magnitude as
       predicted.

CONVENTIONS (round-58/59/60 + census wiring rebuilt inline;
READ-ONLY import of tfpt_constants): 16-dim Majorana space,
carrier C = 0..9 (channels 1..5, pairs), boundary B = 10..15
(channel 0, three seats); A_CC = (+)_5 J2, J3 = A16_dep[B, B];
deployed wiring V_dep = A_int[C, B] (PURE-I); parent family
A(kappa, m, t, V) = [[kappa A_CC, t V], [-t V^T, m J3]] at the
frozen probe-7 point (1/2, 1/2, 1/20).  THETA_S = the pair swap
r_S: 2i <-> 2i+1 (Pauli X per Majorana pair, all 8 pairs) = the
16-dim lift of the v440 collar reflection; half-side = even
indices; twist eta = +i (v519, forced).  THE FRAME SPACE: the
orbit {g theta_S g^{-1}} of theta_S under the group generated by
the 9-dim rule stabilizer (elements of the structure gauge g0
preserving the rule subspace W and the constraint ideal -- the
census P1.4 object, rebuilt and re-warded here).  Its
selection-relevant coordinate is the TORUS pair (gamma, y):
g(gamma, y) = R(gamma) per carrier pair (+) R(y) per boundary
pair; per pair R(gamma) X R(-gamma) = cos(2 gamma) X +
sin(2 gamma) Z, so the orbit sweeps the full reflection circle;
the selected ray depends only on delta = y - gamma.  RP GRAMS for
a GENERAL orthogonal frame theta with half-side vectors f_p:
Theta(f_{p1}...f_{pk}) = eta^k phi(theta f_{pk})...phi(theta
f_{p1}) (v519 reversal + degree twist), M[a, b] =
omega(Theta(m_a) m_b) by vector-Wick (Pfaffian recursion on
kernel dot products u^T (I + iA) v); for permutation frames this
REPRODUCES the round-60 index machinery entrywise (warded).
DEMAND CENSUS (each demand = an exact constraint tested on the
frame orbit; anti-circularity rule: no demand may consume the
deployed wiring V_dep -- the wiring is the object in question;
the carrier-carrier interior A_int[C, C], the vacuum A16_dep, the
C6 action and the bare state are wiring-free and admissible):
 D1 mu4 step / C6 equivariance: [theta, O16] = 0 and
    theta A16_dep theta = -A16_dep (the order-4 vacuum step
    |mu4| = 4 must be REVERSED: antiunitarity w.r.t. the deployed
    complex structure) and det theta = +1;
 D2 CAR / quasi-free state structure: the bare KMS covariance
    A0(u, beta) = tanh(beta u / 2) A16_dep (exact closed form,
    tan(xJ) = tanh(x) J for J^2 = -I) and every state-canonical
    object built from it (modular flow generated by h0 prop.
    A16_dep; the Majorana real structure Theta_0 = entrywise
    conjugation, v898 R1.2) -- does any of it prefer a frame?
    Coupled-point modular data h(V) is EXCLUDED by
    anti-circularity (it consumes V; and theta h(V) theta = -h(V)
    is exactly the relative-angle selector, not a frame demand);
 D3 Pfaffian pencil / orientation propagation: the census
    constraint classes E1/E3/E4 as functions on frames;
 D4 doily / orbit-combinatorics seat: the wiring-free deployed
    structure {O16, A_CC, J3, A_int[C, C]} -- which rule-gauge
    directions preserve ALL of it (the refined stabilizer), and
    does the refinement cut the delta-circle?;
 D5 the twisted-involution census (round 59): the property that
    selected theta_S there (bare-point strict RP with DEFINITE
    collar Grams at eta = +i; theta_abT is marginal-0) --
    constant or not on the frame orbit?
Per-demand verdict enum: FORCED / COMPATIBLE-NOT-FORCING /
SILENT.  NUMERICAL PROTOCOL (declared): frame algebra, orbit
tangents, stabilizer, ideal reductions, selection map, closure
Grams at the integer and rational witnesses are EXACT
(integer/rational sympy); float64 ONLY in disclosed wards
(general-Gram machinery wards, bare-point spectra, defect
regressions); RNG only in controls.

FROZEN CLAIMS (2026-08-12, frozen + SHA-hashed before the frozen
run):

 P1  THE FRAME SPACE (exact).
     (a) theta_S wards: integer involution, orthogonal,
         [theta_S, O16] = 0, theta_S A16_dep theta_S = -A16_dep,
         det = +1, exchanges the sheets (evens <-> odds),
         preserves the carrier/boundary split;
     (b) the census gauge objects REPRODUCED: g0 dim 16, rule
         stabilizer dim 9 (exact nullspaces, same construction);
     (c) the frame orbit: tangent dim {[G, theta_S]} = 7 of 9
         (isotropy 2); the torus generators K_C = (+)_5 J2 (+) 0
         and K_B = 0 (+) (+)_3 J2 are IN the stabilizer (exact
         span membership) and act on theta_S with NONZERO
         commutators -- the reflection circle is rule-gauge
         reachable; the RELATIVE carrier rotation stays CUT
         (census regression, nonzero ideal remainder);
     (d) frame witnesses are rule-gauge legal (exact): the
         INTEGER frame theta' = g_int theta_S g_int^T
         (g_int = exp((pi/2) K_C) = (+)_5 J2 (+) I6; per carrier
         pair -X, boundary X), the rational carrier frame
         theta_r = g_r theta_S g_r^T (g_r = R(3/5, 4/5) per
         carrier pair (+) I6) and the rational boundary frame
         theta_b (I10 (+) R(3/5, 4/5) per boundary pair): each an
         involution, in the O16 commutant, A16_dep-reversing;
         g_int preserves A_CC, O16, W and the ideal (census P4.3
         re-warded).
 P2  THE EQUIVARIANT SELECTOR (the base ward).
     (a) the general-theta vector-Wick Gram machinery REPRODUCES
         the round-60 index machinery entrywise (<= 1e-12, 1p +
         deg-2) at the deployed parent, and reproduces the
         round-60 strict theta_S regression: raw deg-2 defect
         0.1 = 2t with 30 entries;
     (b) equivariance transport (exact mechanism, float ward
         <= 1e-12): for g in {g_int, g_r, g_b} and wirings
         {pure-I, interior (3/5, 4/5)}: Gram in frame
         g theta_S g^T with half-side g F == Gram in frame
         theta_S at the transported wiring V' = g_C^T V g_B --
         and the bare state is EXACTLY gauge-invariant
         (g A0 g^T = A0, torus);
     (c) the transported two-seat law in closed form (symbolic):
         on W, frame (gamma, y) reads deg-2 seat = 2 a'_o with
         a'_o = a_o C + c_o S, C = cos(y - gamma), S =
         sin(y - gamma) (u'_o = R(-gamma) u_o R(y)); on C_rot the
         1p seat vanishes IDENTICALLY in EVERY orbit frame; float
         ward: theta_r deg-2 defect at the deployed parent =
         2t * 3/5 = 0.06 exactly (<= 1e-12);
     (d) THE SELECTION MAP (exact): in frame (gamma, y) the
         strict-collar law cuts C_rot exactly in the ray
         (a_o, c_o) = lambda_o (-S, C), delta = y - gamma:
         delta = 0 reproduces the census selector (pure-(+-J));
         the integer frame theta' selects pure-(+-I); theta_r
         selects the (4/5, 3/5) ray (all exact); EQUIVARIANCE
         COROLLARY: selected_ray(g.frame) = g.selected_ray(frame)
         = g_C (c J2) g_B^T -- the selector transports with the
         frame.
 P3  THE DEMAND CENSUS (per-demand verdicts, exact).
     (a) D1 mu4/C6: [g theta_S g^{-1}, O16] = g [theta_S, O16]
         g^{-1} = 0 and (g theta_S g^{-1}) A16_dep
         (g theta_S g^{-1}) = -A16_dep IDENTICALLY on the orbit
         ([G_k, A16_dep] = 0 for all 9 stabilizer directions,
         exact); det invariant under conjugation.  D1 defines the
         FAMILY (controls: a non-commutant frame fails the first,
         theta = I16 fails the second) but cuts NOTHING inside:
         COMPATIBLE-NOT-FORCING;
     (b) D2 state/modular: the bare covariance A0 = tanh(beta u/2)
         A16_dep (closed form warded <= 1e-12 against the KMS
         construction -tan(beta h0 / 2)) is invariant under every
         stabilizer direction; hence the modular flow intertwining
         theta e^{s h0} theta = e^{-s h0} holds at EVERY orbit
         point iff at one (all reduce to D1's anticommutation);
         Theta_0 (real structure) commutes with every real gauge
         element identically.  No state-canonical object moves on
         the orbit: SILENT (coupled h(V) excluded by
         anti-circularity, typed);
     (c) D3 pencil/orientation: the constraint classes E1-E5
         contain NO frame variable; their gauge stability IS the
         stabilizer definition (re-warded); orientation is
         frame-transport-invariant: det u'_o = det u_o exactly
         (det R = 1).  On frames: SILENT;
     (d) D4 doily/edge combinatorics: the refined stabilizer
         {G in stab : [G_C, A_int[C, C]] = 0} is ALL 9 OF 9
         (measured: NO direction is cut -- every rule-gauge
         direction already preserves the deployed carrier-carrier
         interior exactly), containing K_C and K_B -- the
         (gamma, y) torus and with it the FULL delta-circle
         survive the strongest wiring-free structure-preservation
         demand: the doily/bit-level data (q*, duads, PI6, orbit
         lengths, reversal flags) live on channel labels and
         never reference the within-pair basis.
         COMPATIBLE-NOT-FORCING (cuts nothing at all);
     (e) D5 the round-59 census property: bare-point strict RP at
         eta = +i with DEFINITE Grams holds at theta_S, theta',
         theta_r, theta_b with IDENTICAL spectra (<= 1e-10;
         closed forms lam_min 1p = tanh(1/2) = 0.4621, deg-2 =
         tanh(1/2)^2 = 0.2136) -- the property that distinguished
         theta_S in
         round 59 is CONSTANT on the frame orbit; what it does
         distinguish is the FAMILY (theta_abT bare 1p Gram = 0
         exactly, marginal -- reproduced); the specific angle of
         theta_S is v440 LINEAGE (deployment), not a census
         output: SILENT-ON-ANGLE.
 P4  THE CLOSURE (the verdict payload; exact).
     (a) STRICT COLLAR RP OF THE DEPLOYED PARENT HOLDS IN THE
         INTEGER FRAME: at (1/2, 1/2, 1/20) with V = V_dep
         (pure-I), the theta' Grams (1p + deg-2, eta = +i,
         half-side g_int . evens) are EXACTLY Hermitian and PD by
         exact rational LDL (float lam_min 0.3064 / 0.1532 = the
         round-60 V_J numbers, transported); the SAME parent
         fails strict theta_S RP with raw defect 2t (P2.a) -- the
         round-58/59 obstruction is FRAME-RELATIVE;
     (b) second exact closure witness at a generic angle: the
         rational frame theta_r with its selected wiring
         u_o = (4/5) I + (3/5) J passes strict RP exactly
         (rational Grams Hermitian + PD by exact LDL);
     (c) the composed statement (assembled from P3): NO
         enumerated compiler-side demand distinguishes a point on
         the delta-circle -> THETA-CONVENTIONAL: the collar frame
         is a gauge/deployment choice; the compiler forces the
         admissible component C_rot and the frame FAMILY (D1),
         and the gauge-invariant content of (frame, wiring) is
         ONLY the relative angle; the deployed pair
         (theta_S, pure-I) sits at maximal relative obstruction,
         the SAME wiring at ZERO obstruction relative to theta'
         -- both frames rule-gauge legal.  The CXXXIX/CCXIII
         wiring question is CLOSED as a compiler-freedom theorem
         with freedom group = the rule-gauge frame orbit (7-dim
         tangent; D4-refinement cuts nothing; selection-relevant
         quotient = the delta-circle).
 C   CONTROLS (must fire; frozen fire rules; RNG only in C4).
     C1 NON-COMMUTANT FRAME: rotating channel 1's pair only
        (g_1 outside the commutant) gives [theta_c, O16] != 0
        (>= 4 nonzero integer entries) -- D1 fires off-orbit;
     C2 RELATIVE-ROTATION FRAME (g0 but NOT rule stabilizer,
        rotate 2-cycle carrier channels only, rational 3/5-4/5):
        the transported pure-J wiring VIOLATES the pencil quadric
        (a2 c3 - c2 a3 = -4/5 != 0 exact) -- selector transport
        breaks outside the rule gauge;
     C3 eta = +1 at the bare point breaks collar Gram
        Hermiticity (raw defect >= 0.4; v519/round-58 twist
        regression);
     C4 SEEDED RANDOM PAIRINGS (rng 907, 3 draws) as frames:
        each fails D1 (A16_dep-reversal broken, integer check)
        or breaks bare Gram Hermiticity (defect >= 0.1) -- 3/3;
     C5 theta = I16 fails side-exchange AND D1 reversal
        (I A16 I = +A16): the mu4-step demand is non-vacuous;
     C6 CENSUS REGRESSION GATE: pure-I passes E1 + pencil + E4 +
        canonical census 10/10 with J-coordinate exactly +1/200,
        V_Z fails EXACTLY orientation E4 (dets -1) -- the census
        constraints reproduce.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 frame-space / orbit / stabilizer ward       -> FRAMESPACE-BROKEN
  K2 an equivariance / machinery ward breaks     -> EQUIVARIANCE-BROKEN
  K3 a demand-census computation breaks          -> DEMAND-CENSUS-BROKEN
  K4 a closure Gram / verdict computation breaks -> CLOSURE-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): THETA-CONVENTIONAL [FRAME-ORBIT-MEASURED
(tangent 7/9, torus legal), EQUIVARIANT-SELECTOR (transport ward;
selected ray = g . (+-J)), ALL-DEMANDS-SILENT-ON-ANGLE (D1
family-defining, D2 silent, D3 silent, D4 not-forcing 9/9, D5
constant-on-orbit), DEPLOYED-STRICT-RP-IN-INTEGER-FRAME (exact
Grams), WIRING-QUESTION-CLOSED (compiler-freedom theorem; freedom
group = rule-gauge frame orbit, selection quotient = the
delta-circle)] / THETA-FORCED / THETA-PARTIAL / PIPELINE-BROKEN /
FRAMESPACE-BROKEN / EQUIVARIANCE-BROKEN / DEMAND-CENSUS-BROKEN /
CLOSURE-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the demand census is over the FIVE
ENUMERATED demand classes (each warded to be non-vacuous by a
firing control); a compiler demand OUTSIDE this list could still
exist and is not excluded here; the v440 collar lineage of theta_S
is typed as DEPLOYMENT, not derived; RP remains sector-typed; the
v898/v903 [O] premise is unmoved; no marker moves.  NO RH claim.

SPEC v1 (2026-08-12): frozen after the declared smoke rounds; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline):
seam_wiring_groebner_probe (CCXIII: census, gauge, selector),
seam_ness_parent_probe (round 60: Gram machinery, V_J strict-RP
numbers), rp_twisted_involution_census_probe (round 59: census
property), seam_state_derivation_probe (round 58: theta_S, bare
point), v898_kms_schur_mixing (Theta_0), v519 (eta = +i),
tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/theta_frame_selector_probe.py
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


def pauli_coords(M):
    return (sp.expand((M[0, 0] + M[1, 1]) / 2),
            sp.expand((M[0, 1] + M[1, 0]) / 2),
            sp.expand((M[0, 1] - M[1, 0]) / 2),
            sp.expand((M[0, 0] - M[1, 1]) / 2))


def main():
    print("SEAM.STATE.THETA.SELECTOR.01 -- the collar-frame decision: "
          "does any compiler demand pin the theta_S frame?")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (census rebuild)")
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
    check("S0.4 canonical G_c Pf4 signs rebuilt: 15 nonzero, all "
          "negative",
          all(abs(v) > 1e-16 for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ==================================================================
    section("P1 -- the frame space: theta_S, gauge, orbit")
    # ==================================================================
    # theta_S = pair swap (X per pair), integer
    T0i = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        T0i[2 * i, 2 * i + 1] = 1
        T0i[2 * i + 1, 2 * i] = 1
    okT_inv = np.array_equal(T0i @ T0i, np.eye(16, dtype=np.int64))
    okT_orth = np.array_equal(T0i @ T0i.T, np.eye(16, dtype=np.int64))
    okT_c6 = np.array_equal(T0i @ O16, O16 @ T0i)
    okT_rev = np.array_equal(T0i @ A16_dep @ T0i, -A16_dep)
    okT_det = int(round(np.linalg.det(T0i.astype(np.float64)))) == 1
    P_S = [2 * i for i in range(8)]
    okT_side = all(T0i[2 * i + 1, 2 * i] == 1 for i in range(8))
    okT_split = all(T0i[r, c] == 0
                    for r in CAR_IDX for c in BND_IDX)
    check("P1.1 theta_S wards (integer): involution %s, orthogonal "
          "%s, [theta_S, O16] = 0 %s, mu4-step reversal theta A16 "
          "theta = -A16 %s, det = +1 %s, side-exchanging %s, "
          "split-preserving %s"
          % (okT_inv, okT_orth, okT_c6, okT_rev, okT_det, okT_side,
             okT_split),
          okT_inv and okT_orth and okT_c6 and okT_rev and okT_det
          and okT_side and okT_split, kill="K1")

    # ---- gauge algebra g0 and rule stabilizer (census rebuild)
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

    UT2 = sp.expand(u2.T * u2)
    UT3 = sp.expand(u3.T * u3)
    g1_2 = sp.expand(UT2[0, 1])
    g2_2 = sp.expand(UT2[0, 0] - UT2[1, 1])
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
        for symx, val in zip((a2, b2, c2, d2), pauli_coords(du2)):
            d_coords[symx] = val
        for symx, val in zip((a3, b3, c3, d3), pauli_coords(du3)):
            d_coords[symx] = val
        condsI = []
        for f in IDEAL_GENS:
            df = sp.expand(sum(sp.diff(f, x) * d_coords[x]
                               for x in GENS8))
            condsI.append(sp.expand(rem(df)))
        per_elem.append((condsW, condsI, d_coords))
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
    # stabilizer basis as 60-dim coordinate vectors
    stab_vecs = []
    for base in stab_basis:
        v = sp.zeros(nv, 1)
        for k in range(dim_g0):
            v += base[k] * g0_basis[k]
        stab_vecs.append(sp.expand(v))
    check("P1.2 census gauge objects reproduced: dim g0 = %d == 16, "
          "rule stabilizer dim = %d == 9" % (dim_g0, dim_stab),
          dim_g0 == 16 and dim_stab == 9, kill="K1")

    # ---- orbit tangent {[G, theta_S]}
    T0s = sp.Matrix(T0i.tolist())

    def G16_of(vec):
        G = sp.zeros(16, 16)
        G[0:10, 0:10] = XC_of(list(vec))
        G[10:16, 10:16] = XB_of(list(vec))
        return G

    tang_rows = []
    for v in stab_vecs:
        G = G16_of(v)
        Cm = sp.expand(G * T0s - T0s * G)
        tang_rows.append([Cm[r, c] for r in range(16)
                          for c in range(16)])
    Mtang = sp.Matrix(tang_rows)
    d_orb = Mtang.rank()
    d_iso = dim_stab - d_orb

    # torus generators K_C, K_B: membership in the stabilizer span
    vKC = [sp.Integer(0)] * nv
    for i in range(5):
        vKC[pairsC.index((2 * i, 2 * i + 1))] = sp.Integer(1)
    vKB = [sp.Integer(0)] * nv
    for i in range(3):
        vKB[len(pairsC) + pairsB.index((2 * i, 2 * i + 1))] = \
            sp.Integer(1)
    Mspan = sp.Matrix([[v[k, 0] for k in range(nv)]
                       for v in stab_vecs])
    rk0 = Mspan.rank()
    inKC = sp.Matrix(Mspan.tolist() + [vKC]).rank() == rk0
    inKB = sp.Matrix(Mspan.tolist() + [vKB]).rank() == rk0
    KC16 = G16_of(sp.Matrix(nv, 1, vKC))
    KB16 = G16_of(sp.Matrix(nv, 1, vKB))
    movesKC = sp.expand(KC16 * T0s - T0s * KC16) != sp.zeros(16, 16)
    movesKB = sp.expand(KB16 * T0s - T0s * KB16) != sp.zeros(16, 16)

    # census regression: the RELATIVE carrier rotation stays cut
    vrel = [sp.Integer(0)] * nv
    for i in TWO:
        r0 = 2 * (i - 1)
        vrel[pairsC.index((r0, r0 + 1))] = sp.Integer(1)
    Xrel = XC_of(vrel)
    dVrel = sp.expand(Xrel * V_sym)
    du2r = dVrel[2 * (rep2 - 1):2 * rep2, 0:2]
    du3r = dVrel[2 * (rep3 - 1):2 * rep3, 0:2]
    dcr = {}
    for symx, val in zip((a2, b2, c2, d2), pauli_coords(du2r)):
        dcr[symx] = val
    for symx, val in zip((a3, b3, c3, d3), pauli_coords(du3r)):
        dcr[symx] = val
    rel_rems = [sp.expand(rem(sp.expand(
        sum(sp.diff(f, x) * dcr[x] for x in GENS8))))
        for f in IDEAL_GENS]
    rel_cut = any(r != 0 for r in rel_rems)
    check("P1.3 THE FRAME ORBIT: tangent dim {[G, theta_S]} = %d "
          "== 7 of 9 (isotropy %d == 2); torus generators K_C, K_B "
          "in the stabilizer span (%s, %s) and BOTH move theta_S "
          "(%s, %s) -- the reflection circle is rule-gauge "
          "reachable; the relative carrier rotation stays CUT "
          "(census regression: %s)"
          % (d_orb, d_iso, inKC, inKB, movesKC, movesKB, rel_cut),
          d_orb == 7 and d_iso == 2 and inKC and inKB and movesKC
          and movesKB and rel_cut, kill="K1")

    # ---- frame witnesses (exact)
    # g_int = (+)_5 J2 (+) I6 = exp((pi/2) K_C)
    g_int = sp.zeros(16, 16)
    for i in range(5):
        g_int[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Js
    g_int[10:16, 10:16] = sp.eye(6)
    # g_r = R(3/5, 4/5) per carrier pair (+) I6
    Rr = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                    [sp.Rational(4, 5), sp.Rational(3, 5)]])
    g_r = sp.zeros(16, 16)
    for i in range(5):
        g_r[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Rr
    g_r[10:16, 10:16] = sp.eye(6)
    # g_b = I10 (+) R(3/5, 4/5) per boundary pair
    g_b = sp.zeros(16, 16)
    g_b[0:10, 0:10] = sp.eye(10)
    for i in range(3):
        g_b[10 + 2 * i:12 + 2 * i, 10 + 2 * i:12 + 2 * i] = Rr

    O16s = sp.Matrix(O16.tolist())
    A16s = sp.Matrix(A16_dep.tolist())

    def frame_of(g):
        return sp.expand(g * T0s * g.T)

    th_int = frame_of(g_int)
    th_r = frame_of(g_r)
    th_b = frame_of(g_b)

    def frame_legal(th):
        inv = sp.expand(th * th) == sp.eye(16)
        c6 = sp.expand(th * O16s - O16s * th) == sp.zeros(16, 16)
        rev = sp.expand(th * A16s * th + A16s) == sp.zeros(16, 16)
        return inv, c6, rev

    leg_int = frame_legal(th_int)
    leg_r = frame_legal(th_r)
    leg_b = frame_legal(th_b)
    # g_int census-P4.3 re-ward: preserves A_CC, O16, ideal
    gC10 = g_int[0:10, 0:10]
    okg1 = sp.expand(gC10 * A_CCs * gC10.T - A_CCs) == sp.zeros(10, 10)
    okg2 = sp.expand(gC10 * O_Cs - O_Cs * gC10) == sp.zeros(10, 10)
    gsub = {a2: -c2, b2: -d2, c2: a2, d2: b2,
            a3: -c3, b3: -d3, c3: a3, d3: b3}
    okg4 = all(rem(g.subs(gsub, simultaneous=True)) == 0
               for g in IDEAL_GENS)
    # theta' per carrier pair = -X, boundary = X (integer identity)
    okg5 = all(
        th_int[2 * i:2 * i + 2, 2 * i:2 * i + 2] == -Xs
        for i in range(5)) and all(
        th_int[10 + 2 * i:12 + 2 * i, 10 + 2 * i:12 + 2 * i] == Xs
        for i in range(3))
    check("P1.4 frame witnesses legal (exact): theta' integer "
          "(involution/C6/A16-reversal %s; per carrier pair -X, "
          "boundary X: %s; g_int preserves A_CC %s, O16 %s, ideal "
          "%s), theta_r rational %s, theta_b rational %s"
          % (leg_int, okg5, okg1, okg2, okg4, leg_r, leg_b),
          all(leg_int) and okg5 and okg1 and okg2 and okg4
          and all(leg_r) and all(leg_b), kill="K1")

    # ==================================================================
    section("P2 -- the equivariant selector (base ward)")
    # ==================================================================
    # ---- round-60 index machinery (verbatim conventions)
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

    def gram_idx(basis, r, eta, wick):
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
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]
    # positional bases (same order) for the general machinery
    POS1 = [(p,) for p in range(8)]
    POS2 = [()] + [tuple(c) for c in
                   itertools.combinations(range(8), 2)]

    # ---- general-theta vector-Wick machinery (float)
    def gram_gen(theta_f, F_f, eta, A, basis_pos):
        W = np.eye(16, dtype=complex) + 1j * A
        imgs_ = [theta_f @ F_f[p] for p in range(len(F_f))]

        def wickv(vecs):
            k = len(vecs)
            if k % 2 == 1:
                return 0.0 + 0j
            if k == 0:
                return 1.0 + 0j
            K = [[vecs[p] @ W @ vecs[q] for q in range(k)]
                 for p in range(k)]

            def rec(idxs):
                if not idxs:
                    return 1.0 + 0j
                head, rest = idxs[0], idxs[1:]
                tot = 0.0 + 0j
                for j, bpos in enumerate(rest):
                    sub = rest[:j] + rest[j + 1:]
                    tot += (-1) ** j * K[head][bpos] * rec(sub)
                return tot
            return rec(list(range(k)))

        n = len(basis_pos)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis_pos):
            va = [imgs_[p] for p in reversed(ma)]
            coeff = eta ** len(ma)
            for bi, mb in enumerate(basis_pos):
                vb = [F_f[p] for p in mb]
                M[ai, bi] = coeff * wickv(va + vb)
        return M

    A_CCf = A_CC.astype(np.float64)
    J3f = J3.astype(np.float64)

    def parentV_f(kap, m, tt, V):
        A = np.zeros((16, 16))
        A[np.ix_(CAR_IDX, CAR_IDX)] = kap * A_CCf
        A[np.ix_(BND_IDX, BND_IDX)] = m * J3f
        A[np.ix_(CAR_IDX, BND_IDX)] = tt * V
        A[np.ix_(BND_IDX, CAR_IDX)] = -tt * V.T
        return A

    T0f = T0i.astype(np.float64)
    F_S = [np.eye(16)[:, a] for a in P_S]
    A_dep = parentV_f(0.5, 0.5, 0.05, Vdep.astype(np.float64))
    wk_dep = wick_factory(A_dep)
    M1_idx = gram_idx(B1_S, r_S, 1j, wk_dep)
    M2_idx = gram_idx(B2_S, r_S, 1j, wk_dep)
    M1_gen = gram_gen(T0f, F_S, 1j, A_dep, POS1)
    M2_gen = gram_gen(T0f, F_S, 1j, A_dep, POS2)
    dev_m = max(float(np.max(np.abs(M1_idx - M1_gen))),
                float(np.max(np.abs(M2_idx - M2_gen))))
    D2S = M2_gen - M2_gen.conj().T
    defS = float(np.max(np.abs(D2S)))
    nentS = int(np.sum(np.abs(D2S) > 1e-12))
    check("P2.1 general-theta machinery == round-60 index machinery "
          "entrywise (max dev %.1e <= 1e-12); strict theta_S "
          "regression at the deployed parent: raw deg-2 defect "
          "%.4f == 2t = 0.1, %d == 30 entries"
          % (dev_m, defS, nentS),
          dev_m <= 1e-12 and abs(defS - 0.1) <= 1e-12
          and nentS == 30, kill="K2")

    # ---- equivariance transport ward
    def wiring(u2v, u3v):
        return {a2: u2v[0], b2: u2v[1], c2: u2v[2], d2: u2v[3],
                a3: u3v[0], b3: u3v[1], c3: u3v[2], d3: u3v[3]}

    wI = wiring((-1, 0, 0, 0), (-1, 0, 0, 0))
    wP = wiring((sp.Rational(3, 5), 0, sp.Rational(4, 5), 0),
                (sp.Rational(3, 5), 0, sp.Rational(4, 5), 0))
    V_I = np.array(V_sym.subs(wI).tolist(), dtype=np.float64)
    V_P = np.array(V_sym.subs(wP).tolist(), dtype=np.float64)

    gauges = {"g_int": g_int, "g_r": g_r, "g_b": g_b}
    dev_eq = 0.0
    for gnm, g in gauges.items():
        gf = np.array(g.tolist(), dtype=np.float64)
        thf = gf @ T0f @ gf.T
        Fg = [gf @ f for f in F_S]
        for V in (V_I, V_P):
            A = parentV_f(0.5, 0.5, 0.05, V)
            Vp = gf[0:10, 0:10].T @ V @ gf[10:16, 10:16]
            Ap = parentV_f(0.5, 0.5, 0.05, Vp)
            for bp in (POS1, POS2):
                Mg = gram_gen(thf, Fg, 1j, A, bp)
                Ms = gram_gen(T0f, F_S, 1j, Ap, bp)
                dev_eq = max(dev_eq,
                             float(np.max(np.abs(Mg - Ms))))
    # bare-state gauge invariance (exact)
    ok_bare_inv = all(
        sp.expand(g * A16s * g.T - A16s) == sp.zeros(16, 16)
        for g in (g_int, g_r, g_b))
    check("P2.2 equivariance transport: Gram(frame g theta g^T, "
          "half-side gF, A(V)) == Gram(theta_S, F, A(g_C^T V g_B)) "
          "on 3 gauges x 2 wirings x 2 sectors (max dev %.1e <= "
          "1e-12); bare state exactly gauge-invariant "
          "(g A16_dep g^T = A16_dep: %s)"
          % (dev_eq, ok_bare_inv),
          dev_eq <= 1e-12 and ok_bare_inv, kill="K2")

    # ---- transported two-seat law, symbolic closed form
    cg, sg, cy, sy = sp.symbols("cg sg cy sy", real=True)
    Rg = sp.Matrix([[cg, -sg], [sg, cg]])
    Ry = sp.Matrix([[cy, -sy], [sy, cy]])
    relg = [cg ** 2 + sg ** 2 - 1, cy ** 2 + sy ** 2 - 1]

    def redrel(e):
        return sp.expand(sp.reduced(sp.expand(e),
                                    relg, cg, sg, cy, sy)[1])

    up2 = sp.expand(Rg.T * u2 * Ry)
    up3 = sp.expand(Rg.T * u3 * Ry)
    a2p, b2p, c2p, d2p = [redrel(x) for x in pauli_coords(up2)]
    a3p, b3p, c3p, d3p = [redrel(x) for x in pauli_coords(up3)]
    # closed form: a' = a C + c S, C = cos(y-gamma), S = sin(y-gamma)
    # (J = [[0,1],[-1,0]] means R(t) = cos t I - sin t J)
    Cd = cg * cy + sg * sy
    Sd = sy * cg - cy * sg
    rot_sub = {b2: 0, d2: 0, b3: 0, d3: 0}
    ok_cf2 = redrel(a2p.subs(rot_sub) - (a2 * Cd + c2 * Sd)) == 0
    ok_cf3 = redrel(a3p.subs(rot_sub) - (a3 * Cd + c3 * Sd)) == 0
    ok_1p = (redrel(b2p.subs(rot_sub)) == 0
             and redrel(b3p.subs(rot_sub)) == 0)
    # gamma = y = 0 reproduces the census law coordinates
    sub0 = {cg: 1, sg: 0, cy: 1, sy: 0}
    ok_00 = (sp.expand(a2p.subs(sub0) - a2) == 0
             and sp.expand(b2p.subs(sub0) - b2) == 0)
    # float ward: theta_r deg-2 defect at the deployed parent
    gf_r = np.array(g_r.tolist(), dtype=np.float64)
    th_rf = gf_r @ T0f @ gf_r.T
    F_r = [gf_r @ f for f in F_S]
    M2r = gram_gen(th_rf, F_r, 1j, A_dep, POS2)
    D2r = M2r - M2r.conj().T
    defR = float(np.max(np.abs(D2r)))
    # predicted: 2t * |a'| with a' = a cos(-gamma... ) = -3/5
    check("P2.3 transported two-seat law: on C_rot deg-2 seat = "
          "2(a_o C + c_o S), C = cos(y-gamma), S = sin(y-gamma) "
          "(%s, %s); 1p seat IDENTICALLY zero on C_rot in every "
          "orbit frame (%s); frame (0,0) reproduces the census law "
          "(%s); float ward theta_r: deg-2 defect %.4f == "
          "2t*3/5 = 0.06 (<= 1e-12)"
          % (ok_cf2, ok_cf3, ok_1p, ok_00, defR),
          ok_cf2 and ok_cf3 and ok_1p and ok_00
          and abs(defR - 0.06) <= 1e-12, kill="K2")

    # ---- THE SELECTION MAP (exact)
    lam2, lam3 = sp.symbols("lam2 lam3", real=True)
    ray_sub = {a2: -lam2 * Sd, c2: lam2 * Cd,
               a3: -lam3 * Sd, c3: lam3 * Cd}
    ok_ray_in = (redrel(sp.expand(
        (a2 * Cd + c2 * Sd).subs(ray_sub))) == 0
        and redrel(sp.expand(
            (a3 * Cd + c3 * Sd).subs(ray_sub))) == 0)
    minor_rot = sp.expand(a2 * c3 - c2 * a3)
    ok_ray_pen = redrel(sp.expand(minor_rot.subs(ray_sub))) == 0
    # uniqueness: the (C, S) kernel is 1-dim per orbit (C^2+S^2=1)
    ok_unit = redrel(sp.expand(Cd ** 2 + Sd ** 2 - 1)) == 0
    # corollaries: theta_S (delta = 0: S = 0, C = 1) -> pure-(+-J);
    # theta' (gamma = pi/2, y = 0: C = 0, S = -1) -> pure-(+-I);
    # theta_r (cg = 3/5, sg = 4/5, y = 0: C = 3/5, S = -4/5)
    #   -> ray (a, c) prop. (4/5, 3/5)
    ok_sel_S = (sp.expand((-lam2 * Sd).subs(sub0)) == 0
                and sp.expand((lam2 * Cd).subs(sub0)) == lam2)
    sub_int = {cg: 0, sg: 1, cy: 1, sy: 0}
    ok_sel_int = (sp.expand((-lam2 * Sd).subs(sub_int)) == lam2
                  and sp.expand((lam2 * Cd).subs(sub_int)) == 0)
    sub_r = {cg: sp.Rational(3, 5), sg: sp.Rational(4, 5),
             cy: 1, sy: 0}
    ok_sel_r = (sp.expand((-lam2 * Sd).subs(sub_r))
                == sp.Rational(4, 5) * lam2
                and sp.expand((lam2 * Cd).subs(sub_r))
                == sp.Rational(3, 5) * lam2)
    # equivariance corollary: selected(g.frame) = g.selected(frame):
    # u_sel = R(gamma) (c J) R(y)^T = c (-sin(y-gamma) I + cos(.) J)
    usel = sp.expand(Rg * (Js) * Ry.T)
    aI_sel, _bX, cJ_sel, _dZ = [redrel(x) for x in
                                pauli_coords(usel)]
    ok_cor = (redrel(aI_sel + Sd) == 0
              and redrel(cJ_sel - Cd) == 0)
    check("P2.4 THE SELECTION MAP (exact): in frame (gamma, y) the "
          "strict-collar law cuts C_rot exactly in the ray "
          "(a_o, c_o) = lambda_o (-S, C), delta = y - gamma "
          "(membership %s/%s, pencil automatic %s, unit %s); "
          "corollaries: theta_S -> pure-(+-J) (%s), theta' -> "
          "pure-(+-I) (%s), theta_r -> (4/5, 3/5) ray (%s); "
          "equivariance corollary selected(g.frame) = "
          "g.selected(frame) = g_C (c J2) g_B^T (%s)"
          % (ok_ray_in, ok_ray_pen, ok_ray_pen, ok_unit, ok_sel_S,
             ok_sel_int, ok_sel_r, ok_cor),
          ok_ray_in and ok_ray_pen and ok_unit and ok_sel_S
          and ok_sel_int and ok_sel_r and ok_cor,
          kill="K2")

    # ==================================================================
    section("P3 -- the demand census (per-demand verdicts)")
    # ==================================================================
    # D1 mu4 / C6 equivariance
    ok_A16_all = all(
        sp.expand(G16_of(v) * A16s - A16s * G16_of(v))
        == sp.zeros(16, 16) for v in stab_vecs)
    ok_D1_wit = all(frame_legal(th)[1] and frame_legal(th)[2]
                    for th in (th_int, th_r, th_b))
    det_wits = [sp.det(th) for th in (th_int, th_r, th_b)]
    ok_D1_det = all(d == 1 for d in det_wits)
    check("P3.1 D1 mu4-step/C6 demand: [G_k, A16_dep] = 0 for all "
          "9 stabilizer directions (%s) => C6-equivariance AND "
          "A16-reversal hold IDENTICALLY on the orbit (witnesses "
          "%s); det theta = +1 invariant (%s).  VERDICT "
          "COMPATIBLE-NOT-FORCING (family-defining, cuts nothing "
          "inside; teeth: controls C1/C5)"
          % (ok_A16_all, ok_D1_wit, ok_D1_det),
          ok_A16_all and ok_D1_wit and ok_D1_det, kill="K3")

    # D2 state / modular data
    # closed form A0 = tanh(beta u / 2) A16_dep vs -tan(beta h0 / 2)
    # via the Hermitian eigenbasis of i h0: h0 = Q diag(-i w) Q^*,
    # so -tan(beta h0 / 2) = i Q diag(tanh(beta w / 2)) Q^*
    h0 = -A16_dep.astype(np.float64)          # u = 1
    wH, QH = np.linalg.eigh(1j * h0)
    A0_dir = (1j * QH @ np.diag(np.tanh(wH / 2))
              @ QH.conj().T).real              # beta = 1
    A0_cf = np.tanh(0.5) * A16_dep.astype(np.float64)
    dev_cf = float(np.max(np.abs(A0_dir - A0_cf)))
    # torus invariance of A0 (follows from D1 exactness); Theta_0
    # = entrywise conjugation commutes with every REAL g: identical
    ok_D2 = dev_cf <= 1e-12 and ok_A16_all
    check("P3.2 D2 CAR/state demand: bare KMS covariance closed "
          "form A0 = tanh(beta u/2) A16_dep (dev %.1e <= 1e-12) is "
          "EXACTLY invariant under every stabilizer direction "
          "(P3.1) => modular flow intertwining and Theta_0 "
          "(entrywise conjugation, real-gauge-invariant) are "
          "CONSTANT on the orbit; coupled-point h(V) EXCLUDED by "
          "anti-circularity (typed: theta h(V) theta = -h(V) is "
          "the relative-angle selector, not a frame demand).  "
          "VERDICT SILENT" % dev_cf,
          ok_D2, kill="K3")

    # D3 pencil / orientation on frames
    # (i) no frame variable in E1..E5 (structural: generators in
    # Q[a2..d3] only); (ii) gauge stability of the ideal is the
    # stabilizer definition -- re-warded along stab_vecs;
    # (iii) det u' = det u exactly
    stab_id_ok = True
    for v in stab_vecs:
        XCk = XC_of([v[k, 0] for k in range(len(pairsC))])
        XBk = XB_of([0] * len(pairsC)
                    + [v[len(pairsC) + k, 0]
                       for k in range(len(pairsB))])
        dV = sp.expand(XCk * V_sym - V_sym * XBk)
        du2k = dV[2 * (rep2 - 1):2 * rep2, 0:2]
        du3k = dV[2 * (rep3 - 1):2 * rep3, 0:2]
        dck = {}
        for symx, val in zip((a2, b2, c2, d2), pauli_coords(du2k)):
            dck[symx] = val
        for symx, val in zip((a3, b3, c3, d3), pauli_coords(du3k)):
            dck[symx] = val
        for f in IDEAL_GENS:
            df = sp.expand(sum(sp.diff(f, x) * dck[x]
                               for x in GENS8))
            if sp.expand(rem(df)) != 0:
                stab_id_ok = False
    det_inv = redrel(sp.expand(up2.det() - u2.det())) == 0
    ok_novar = all(
        set(sp.Poly(f, *GENS8).gens) == set(GENS8)
        for f in IDEAL_GENS)
    check("P3.3 D3 pencil/orientation demand: the constraint "
          "classes contain NO frame variable (generators in "
          "Q[a2..d3]: %s); ideal stability along all 9 stabilizer "
          "directions re-warded (%s); orientation frame-transport-"
          "invariant det u' = det u exactly (%s).  VERDICT SILENT"
          % (ok_novar, stab_id_ok, det_inv),
          ok_novar and stab_id_ok and det_inv, kill="K3")

    # D4 doily / edge-combinatorics: refined stabilizer
    AintCC = sp.Matrix(A_int[np.ix_(CAR_IDX, CAR_IDX)].tolist())
    ref_rows = []
    for v in stab_vecs:
        XCk = XC_of([v[k, 0] for k in range(len(pairsC))])
        Cm = sp.expand(XCk * AintCC - AintCC * XCk)
        ref_rows.append([Cm[r, c] for r in range(10)
                         for c in range(10)])
    Mref = sp.Matrix(ref_rows)
    d_cut = Mref.rank()
    d_ref = dim_stab - d_cut
    # K_C, K_B pass the refined demand exactly
    okKC_ref = sp.expand(KC16[0:10, 0:10] * AintCC
                         - AintCC * KC16[0:10, 0:10]) \
        == sp.zeros(10, 10)
    okKB_ref = True   # K_B does not touch [C, C]; A_int[B, B] = 0
    okBB0 = np.array_equal(A_int[np.ix_(BND_IDX, BND_IDX)],
                           np.zeros((6, 6), dtype=np.int64))
    check("P3.4 D4 doily/edge-combinatorics demand (wiring-free "
          "structure preservation incl. A_int[C, C]): refined "
          "stabilizer dim = %d == 9 of 9 (NO direction cut: every "
          "rule-gauge direction preserves the deployed "
          "carrier-carrier interior exactly); K_C commutes with "
          "A_int[C, C] (%s), K_B untouched (A_int[B, B] = 0: %s) "
          "=> the (gamma, y) torus and the FULL delta-circle "
          "survive.  VERDICT COMPATIBLE-NOT-FORCING (cuts nothing)"
          % (d_ref, okKC_ref, okBB0),
          d_ref == 9 and okKC_ref and okKB_ref and okBB0,
          kill="K3")

    # D5 the round-59 census property on the orbit
    A0f = np.tanh(0.5) * A16_dep.astype(np.float64)
    frames_f = {"theta_S": (T0f, F_S)}
    for gnm, g in gauges.items():
        gf = np.array(g.tolist(), dtype=np.float64)
        frames_f["g" + gnm] = (gf @ T0f @ gf.T,
                               [gf @ f for f in F_S])
    spec1, spec2 = {}, {}
    herm_bare = 0.0
    for nm, (thf, Ff) in frames_f.items():
        M1 = gram_gen(thf, Ff, 1j, A0f, POS1)
        M2 = gram_gen(thf, Ff, 1j, A0f, POS2)
        herm_bare = max(herm_bare,
                        float(np.max(np.abs(M1 - M1.conj().T))),
                        float(np.max(np.abs(M2 - M2.conj().T))))
        spec1[nm] = np.sort(np.linalg.eigvalsh(
            (M1 + M1.conj().T) / 2))
        spec2[nm] = np.sort(np.linalg.eigvalsh(
            (M2 + M2.conj().T) / 2))
    dev_sp = max(
        float(np.max(np.abs(spec1[nm] - spec1["theta_S"])))
        for nm in frames_f)
    dev_sp2 = max(
        float(np.max(np.abs(spec2[nm] - spec2["theta_S"])))
        for nm in frames_f)
    lm1 = float(spec1["theta_S"][0])
    lm2 = float(spec2["theta_S"][0])
    lm1_cf = float(np.tanh(0.5))
    lm2_cf = float(np.tanh(0.5) ** 2)
    # theta_abT marginal-0 regression (bare 1p Gram identically 0)
    r_abT = {k: k for k in range(16)}
    for k in range(2):
        r_abT[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_abT[CH[b_ch][k]] = CH[a_ch][1 - k]
    B1_ab = [(a,) for a in CH[a_ch]]
    wk0 = wick_factory(A0f)
    M1T = gram_idx(B1_ab, r_abT, 1j, wk0)
    marg = float(np.max(np.abs(M1T)))
    check("P3.5 D5 round-59 census property on the orbit: bare "
          "strict RP (eta = +i) holds at ALL 4 frames with "
          "IDENTICAL spectra (Herm %.1e, spec dev %.1e/%.1e <= "
          "1e-10); closed forms lam_min 1p %.4f == tanh(1/2) = "
          "%.4f, deg-2 %.4f == tanh(1/2)^2 = %.4f; theta_abT bare "
          "1p Gram marginal-0 (%.1e): the census property "
          "distinguishes the FAMILY, is CONSTANT on the angle; "
          "theta_S's angle is v440 LINEAGE (deployment).  VERDICT "
          "SILENT-ON-ANGLE"
          % (herm_bare, dev_sp, dev_sp2, lm1, lm1_cf, lm2, lm2_cf,
             marg),
          herm_bare <= 1e-10 and dev_sp <= 1e-10
          and dev_sp2 <= 1e-10 and abs(lm1 - lm1_cf) <= 1e-10
          and abs(lm2 - lm2_cf) <= 1e-10 and lm1 > 0 and lm2 > 0
          and marg <= 1e-12, kill="K3")

    # ==================================================================
    section("P4 -- the closure (exact strict RP in orbit frames)")
    # ==================================================================
    def wickv_exact_factory(Aex):
        Wm = sp.eye(16) + sp.I * Aex

        def wickv(vecs):
            k = len(vecs)
            if k % 2 == 1:
                return sp.Integer(0)
            if k == 0:
                return sp.Integer(1)
            K = [[sp.expand((vecs[p].T * Wm * vecs[q])[0, 0])
                  for q in range(k)] for p in range(k)]

            def rec(idxs):
                if not idxs:
                    return sp.Integer(1)
                head, rest = idxs[0], idxs[1:]
                tot = sp.Integer(0)
                for j, bpos in enumerate(rest):
                    w = K[head][bpos]
                    if w != 0:
                        sub = rest[:j] + rest[j + 1:]
                        tot += sp.Integer(-1) ** j * w * rec(sub)
                return tot
            return rec(list(range(k)))
        return wickv

    def gram_gen_exact(theta_s, F_cols, eta, wickv, basis_pos):
        imgs_ = [sp.expand(theta_s * f) for f in F_cols]
        n = len(basis_pos)
        M = sp.zeros(n, n)
        for ai, ma in enumerate(basis_pos):
            va = [imgs_[p] for p in reversed(ma)]
            coeff = eta ** len(ma)
            for bi, mb in enumerate(basis_pos):
                vb = [F_cols[p] for p in mb]
                M[ai, bi] = sp.expand(coeff * wickv(va + vb))
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

    def exact_parent(Vm):
        kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                        sp.Rational(1, 20))
        A_ex = sp.zeros(16, 16)
        A_ex[0:10, 0:10] = kapQ * A_CCs
        A_ex[10:16, 10:16] = mQ * J3s
        A_ex[0:10, 10:16] = tQ * Vm
        A_ex[10:16, 0:10] = -tQ * Vm.T
        return A_ex

    # (a) deployed parent (pure-I) in the INTEGER frame theta'
    Vdep_s = sp.Matrix(Vdep.tolist())
    A_ex_dep = exact_parent(Vdep_s)
    wv_dep = wickv_exact_factory(A_ex_dep)
    F_int = [g_int * sp.eye(16)[:, a] for a in P_S]
    M1i = gram_gen_exact(th_int, F_int, sp.I, wv_dep, POS1)
    M2i = gram_gen_exact(th_int, F_int, sp.I, wv_dep, POS2)
    h1i = herm_exact(M1i)
    h2i = herm_exact(M2i)
    p1i, piv1 = psd_exact(M1i)
    p2i, piv2 = psd_exact(M2i)
    pd1 = p1i and all(p > 0 for p in piv1)
    pd2 = p2i and all(p > 0 for p in piv2)
    l1i = float(np.min(np.linalg.eigvalsh(np.array(
        M1i.evalf(16), dtype=complex))))
    l2i = float(np.min(np.linalg.eigvalsh(np.array(
        M2i.evalf(16), dtype=complex))))
    check("P4.1 THE CLOSURE HEADLINE: strict collar RP of the "
          "DEPLOYED parent (pure-I, (1/2,1/2,1/20)) in the INTEGER "
          "frame theta' PASSES EXACTLY: Grams Hermitian (%s, %s), "
          "PD by exact LDL (%s, %s); float lam_min %.4f == 0.3064 "
          "+- 0.005 (1p), %.4f == 0.1532 +- 0.005 (deg-2) -- the "
          "round-60 V_J numbers transported; the SAME parent fails "
          "strict theta_S with raw defect 0.1 (P2.1): the "
          "round-58/59 obstruction is FRAME-RELATIVE"
          % (h1i, h2i, pd1, pd2, l1i, l2i),
          h1i and h2i and pd1 and pd2
          and abs(l1i - 0.3064) <= 5e-3
          and abs(l2i - 0.1532) <= 5e-3, kill="K4")

    # (b) generic-angle closure: theta_r with its selected wiring
    w_sel = wiring((sp.Rational(4, 5), 0, sp.Rational(3, 5), 0),
                   (sp.Rational(4, 5), 0, sp.Rational(3, 5), 0))
    V_sel = V_sym.subs(w_sel)
    A_ex_sel = exact_parent(V_sel)
    wv_sel = wickv_exact_factory(A_ex_sel)
    F_rr = [g_r * sp.eye(16)[:, a] for a in P_S]
    M1r = gram_gen_exact(th_r, F_rr, sp.I, wv_sel, POS1)
    M2r_e = gram_gen_exact(th_r, F_rr, sp.I, wv_sel, POS2)
    h1r = herm_exact(M1r)
    h2r = herm_exact(M2r_e)
    p1r, piv1r = psd_exact(M1r)
    p2r, piv2r = psd_exact(M2r_e)
    pd1r = p1r and all(p > 0 for p in piv1r)
    pd2r = p2r and all(p > 0 for p in piv2r)
    # E1-E5 admissibility of the selected wiring (exact)
    selE1 = [sp.expand(g.subs(w_sel)) for g in
             (g1_2, g2_2, g1_3, g2_3)]
    selPen = [sp.expand(g.subs(w_sel)) for g in (pI, pX, pZ)]
    selDet = (sp.expand(u2.det().subs(w_sel)),
              sp.expand(u3.det().subs(w_sel)))
    check("P4.2 generic-angle closure witness: theta_r with its "
          "selected wiring u = (4/5) I + (3/5) J: E1 %s == 0, "
          "pencil %s == 0, dets %s > 0; strict RP EXACT (Hermitian "
          "%s/%s, PD %s/%s) -- at a NON-integer interior angle the "
          "frame + its selected ray are strict-collar clean"
          % (selE1, selPen, selDet, h1r, h2r, pd1r, pd2r),
          all(e == 0 for e in selE1)
          and all(e == 0 for e in selPen)
          and all(d > 0 for d in selDet)
          and h1r and h2r and pd1r and pd2r, kill="K4")

    print("\n      THE DEMAND CENSUS TABLE (frame orbit of theta_S "
          "under the 9-dim rule gauge):")
    print("        D1 mu4-step / C6 equivariance:  "
          "COMPATIBLE-NOT-FORCING (family-defining)")
    print("        D2 CAR / quasi-free modular:    SILENT "
          "(state exactly torus-invariant)")
    print("        D3 Pf pencil / orientation:     SILENT "
          "(no frame variable; gauge-stable)")
    print("        D4 doily / edge combinatorics:  "
          "COMPATIBLE-NOT-FORCING (refined 9/9, cuts nothing)")
    print("        D5 twisted-involution census:   SILENT-ON-ANGLE "
          "(constant on orbit; family-selecting)")
    print("      => NO demand pins a point on the delta-circle: "
          "the collar frame is CONVENTIONAL;")
    print("         the compiler forces the component C_rot and "
          "the frame FAMILY, and the invariant")
    print("         content of (frame, wiring) is ONLY the "
          "relative angle -- the deployed pure-I is")
    print("         maximally obstructed relative to theta_S and "
          "EXACTLY clean relative to theta'.")

    # ==================================================================
    section("P5 -- controls (must fire)")
    # ==================================================================
    # C1 non-commutant frame: rotate channel 1's pair only
    g_1 = sp.eye(16)
    g_1[0:2, 0:2] = Rr
    th_c = frame_of(g_1)
    commC1 = sp.expand(th_c * O16s - O16s * th_c)
    n_nzC1 = sum(1 for e in commC1 if e != 0)
    check("C1 non-commutant frame (channel-1 rotation): "
          "[theta_c, O16] has %d >= 4 nonzero entries -- D1 fires "
          "off-orbit" % n_nzC1, n_nzC1 >= 4, kill="K7")

    # C2 relative-rotation frame: transported pure-J fails the pencil
    g_relm = sp.eye(16)
    for i in TWO:
        r0 = 2 * (i - 1)
        g_relm[r0:r0 + 2, r0:r0 + 2] = Rr
    VJ_s = V_sym.subs(wiring((0, 0, 1, 0), (0, 0, 1, 0)))
    Vp_rel = sp.expand(g_relm[0:10, 0:10].T * VJ_s)
    u2rel = Vp_rel[2 * (rep2 - 1):2 * rep2, 0:2]
    u3rel = Vp_rel[2 * (rep3 - 1):2 * rep3, 0:2]
    a2r_, _b, c2r_, _d = pauli_coords(u2rel)
    a3r_, _b3x, c3r_, _d3x = pauli_coords(u3rel)
    minor_val = sp.expand(a2r_ * c3r_ - c2r_ * a3r_)
    check("C2 relative-rotation frame (g0, NOT rule stabilizer): "
          "transported pure-J violates the pencil quadric "
          "a2 c3 - c2 a3 = %s == -4/5 != 0 -- selector transport "
          "breaks outside the rule gauge" % minor_val,
          minor_val == -sp.Rational(4, 5), kill="K7")

    # C3 eta = +1 breaks bare Hermiticity
    M1e = gram_gen(T0f, F_S, 1.0, A0f, POS1)
    defE = float(np.max(np.abs(M1e - M1e.conj().T)))
    check("C3 eta = +1 at the bare point: 1p Gram Hermiticity "
          "defect %.4f >= 0.4 (v519/round-58 twist regression)"
          % defE, defE >= 0.4, kill="K7")

    # C4 seeded random pairings as frames
    rng = np.random.default_rng(907)
    n_fire = 0
    for _ in range(3):
        perm = rng.permutation(16)
        mt = np.zeros((16, 16), dtype=np.int64)
        for k in range(0, 16, 2):
            mt[perm[k], perm[k + 1]] = 1
            mt[perm[k + 1], perm[k]] = 1
        rev_ok = np.array_equal(mt @ A16_dep @ mt, -A16_dep)
        if not rev_ok:
            n_fire += 1
            continue
        Fm = [np.eye(16)[:, a] for a in P_S]
        M1m = gram_gen(mt.astype(np.float64), Fm, 1j, A0f, POS1)
        if float(np.max(np.abs(M1m - M1m.conj().T))) >= 0.1:
            n_fire += 1
    check("C4 seeded random pairings (rng 907, 3 draws): each "
          "fails D1 A16-reversal or breaks bare Hermiticity -- "
          "%d/3 fire" % n_fire, n_fire == 3, kill="K7")

    # C5 theta = I16
    okC5 = (not np.array_equal(
        np.eye(16, dtype=np.int64) @ A16_dep, -A16_dep))
    check("C5 theta = I16 fails the mu4-step reversal "
          "(I A16 I = +A16 != -A16) and is not side-exchanging -- "
          "the D1 demand is non-vacuous", okC5, kill="K7")

    # C6 census regression gate
    def eval_E1(sub):
        return [sp.expand(g.subs(sub)) for g in
                (g1_2, g2_2, g1_3, g2_3)]

    def eval_pencil(sub):
        return [sp.expand(g.subs(sub)) for g in (pI, pX, pZ)]

    def eval_dets(sub):
        return (sp.expand(u2.det().subs(sub)),
                sp.expand(u3.det().subs(sub)))

    def census_exact(sub):
        kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                        sp.Rational(1, 20))
        lamQ = mQ / (1 - mQ ** 2)
        Vm = V_sym.subs(sub)
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
    E1I = eval_E1(wI)
    penI = eval_pencil(wI)
    detI = eval_dets(wI)
    nzI, sigI, JcoI = census_exact(wI)
    wZ = wiring((0, 0, 0, 1), (0, 0, 0, 1))
    detZ = eval_dets(wZ)
    E1Z = eval_E1(wZ)
    penZ = eval_pencil(wZ)
    check("C6 census regression gate: pure-I passes E1 %s == 0, "
          "pencil %s == 0, dets %s > 0, census %d/10 canonical "
          "%d/10, J-coordinate %s == 1/200; V_Z passes E1/pencil "
          "(%s, %s) but fails EXACTLY orientation (dets %s == "
          "(-1, -1))"
          % (E1I, penI, detI, nzI, sigI, JcoI,
             all(e == 0 for e in E1Z), all(e == 0 for e in penZ),
             detZ),
          all(e == 0 for e in E1I) and all(e == 0 for e in penI)
          and all(d > 0 for d in detI) and nzI == 10 and sigI == 10
          and JcoI == sp.Rational(1, 200)
          and all(e == 0 for e in E1Z)
          and all(e == 0 for e in penZ)
          and all(d == -1 for d in detZ), kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    all_ok = (n_pass == n_tot) and not KILLS
    if all_ok:
        verdict = ("THETA-CONVENTIONAL [FRAME-ORBIT-MEASURED"
                   "(tangent 7/9, torus legal), "
                   "EQUIVARIANT-SELECTOR(selected ray = g.(+-J)), "
                   "ALL-DEMANDS-SILENT-ON-ANGLE(D1 family, D2 "
                   "silent, D3 silent, D4 not-forcing 9/9, D5 "
                   "constant-on-orbit), "
                   "DEPLOYED-STRICT-RP-IN-INTEGER-FRAME(exact), "
                   "WIRING-QUESTION-CLOSED(freedom group = "
                   "rule-gauge frame orbit; selection quotient = "
                   "the delta-circle)]")
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
'''

# ------------- frozen probe source wiring_gauge_rp_audit_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wiring_gauge_rp_audit_probe -- SEAM.STATE.WIRING.GAUGE.RP.01
(EXPLORATION ONLY, experiments/; 2026-08-12 -- the mandatory
gauge-covariance audit of the reflection-positivity exclusion,
ordered by the program lead on top of CCXIII (wiring census) and
CCXV (theta-frame decision).  Two exact questions, one corrected
canonical sentence.)

THE LEAD'S TWO QUESTIONS (verbatim scope).
 (a) CONJUGATION: is Theta_S^(J) = g Theta_S^(I) g^{-1} -- i.e.
     are the collar reflections attached to the pure-J and pure-I
     representatives exact rule-gauge conjugates under the integer
     element g_int = (+)_5 J2 (+) I6, and how does the relation
     extend to a generic rule-gauge element?
 (b) COVARIANCE OF THE RP GRAM FORMS: do the strict-collar RP
     Grams transform covariantly under the rule-gauge orbit, so
     that RP(theta, wiring) depends only on the RELATIVE angle
     delta(frame, wiring) -- and hence: is the RP exclusion of a
     wiring (1) gauge-invariant (an orbit statement) or (2) valid
     only at fixed Theta_S (a frame statement, NOT a wiring
     no-go)?

CONVENTIONS (identical to theta_frame_selector_probe / CCXV;
machinery rebuilt inline; READ-ONLY import of tfpt_constants):
16-dim Majorana space, carrier C = 0..9 (channels 1..5, pairs),
boundary B = 10..15 (channel 0, three seats); A_CC = (+)_5 J2,
J3 = A16_dep[B, B]; deployed wiring V_dep = A_int[C, B] (PURE-I,
census point (-1,0,0,0|-1,0,0,0)); parent family A(kappa, m, t, V)
at the frozen probe-7 point (1/2, 1/2, 1/20).  theta_S = pair swap
(X per Majorana pair, v440 lift); half-side = even indices; twist
eta = +i (v519).  Frames: theta' = g_int theta_S g_int^T (integer),
theta_r = g_r theta_S g_r^T with g_r = R(3/5, 4/5) per carrier
pair (+) I6 (rational generic angle).  Wirings on C_rot: pure-I
(u = -I), pure-J (u = J2), the theta_r-selected ray
u = (4/5) I + (3/5) J.  Wiring transport under a gauge g:
V' = g_C^T V g_B (theta-selector convention, CCXV P2.b).  RP
Grams for a frame theta with half-side vectors f_p:
Theta(f_{p1}..f_{pk}) = eta^k phi(theta f_{pk})..phi(theta f_{p1})
(v519 reversal + degree twist), M[a, b] = omega(Theta(m_a) m_b) by
vector-Wick (Pfaffian recursion on kernel dot products
u^T (I + iA) v).  NUMERICAL PROTOCOL (declared): conjugation
relations, torus identities, kernel-covariance law, Gram
covariance at the witnesses, PD decisions (LDL) and the
orientation invariance are EXACT (integer/rational/symbolic
sympy); float64 ONLY in disclosed wards (machinery regression,
defect-law wards, spectra); RNG nowhere (all controls
deterministic).

SMOKE-RUN DISCLOSURE (2026-08-12, one declared smoke round before
freezing; fail-first preserved): smoke-1 ran 20/21 and corrected
EXACTLY ONE hand-prediction by measurement, not inverting any
verdict logic: the reflection-circle SIGN -- with the deployed
convention J = [[0,1],[-1,0]], R(t) = cos t I - sin t J, the
conjugated per-carrier-pair block is cos(2 gamma) X -
sin(2 gamma) Z (NOT +; the CCXV "+" statement is the same circle
traversed with the opposite orientation -- a pure convention),
and the angle-addition target was rebuilt with the corrected
sign.  Two further hand-DERIVATIONS were pre-registered in this
spec before the smoke and CONFIRMED unchanged by it: (i) the
g_int wiring transport sends pure-J to pure-(+I)
(u' = J2^T J2 I = +I) and pure-I to pure-(+J)
(u' = J2^T (-I) = +J2) -- the CCXIII map "pure-I -> pure-(-J)"
used the inverse transport direction; both are the same orbit
statement (signs are flips inside the selected +-ray); (ii) the
strict-collar deg-2 defect law max|M2 - M2^dagger| = 2t|a'| with
a' = a cos(delta) + c sin(delta) at all three equal-orbit witness
configurations.

FROZEN CLAIMS (2026-08-12, frozen + SHA-hashed before the frozen
run):

 P1  THE CONJUGATION ANSWER (question a; exact).
     (a) theta_S wards reproduced (integer involution, orthogonal,
         [theta_S, O16] = 0, theta_S A16_dep theta_S = -A16_dep,
         det +1, side-exchanging, split-preserving); census gauge
         objects reproduced: dim g0 = 16, rule stabilizer = 9;
     (b) THE RELATION HOLDS, BOTH DIRECTIONS, EXACTLY:
         theta^(I) := theta' = g_int theta_S g_int^{-1} AND
         theta_S = g_int theta' g_int^{-1} (g_int^2 = (+)_5(-I2)
         (+) I6 lies in the isotropy of theta_S, so conjugation
         by g_int is an involution on the frame pair); theta' =
         per carrier pair -X, boundary X (integer identity);
     (c) the attached-wiring correspondence transports with the
         frame (exact): the selection map sends theta_S ->
         pure-(+-J) and theta' -> pure-(+-I); g_int transports
         the pure-J wiring to pure-(+I) and pure-I to pure-(+J)
         (u' = g_C^T u g_B per pair; smoke-disclosed signs);
     (d) GENERIC EXTENSION (symbolic): the rule-gauge torus
         g(gamma, y) conjugates theta_S to the frame with
         per-carrier-pair block cos(2 gamma) X - sin(2 gamma) Z
         (boundary: 2y; smoke-corrected sign, see disclosure),
         frame legality (involution, C6 commutant, A16-reversal)
         holds IDENTICALLY on the torus, and conjugation
         composes by angle addition:
         g(g0) . frame(gamma) = frame(gamma + g0) exactly -- the
         generic rule element acts as a rotation of the
         delta-circle.
 P2  THE COVARIANCE ANSWER (question b; exact).
     (a) machinery regression (float): the general-theta
         vector-Wick Grams reproduce the round-60 index machinery
         entrywise (<= 1e-12); strict theta_S regression at the
         deployed parent: raw deg-2 defect 0.1 = 2t, 30 entries;
     (b) THE KERNEL-COVARIANCE LAW (symbolic, the proof): on the
         full symbolic torus with the symbolic wiring W,
         g(gamma, y)^T g(gamma, y) = I16 and
         g^T A(V) g = A(g_C^T V g_B) IDENTICALLY (256 entries
         each, reduced by cos^2 + sin^2 = 1); since every Gram
         entry is a polynomial in kernel dot products
         u^T (I + iA) v of vectors {theta f_p, f_p}, and the
         frame/half-side transport multiplies every vector by g,
         Gram(g theta g^T, gF, A(V)) = Gram(theta, F, A(V'))
         ENTRYWISE -- strict-collar RP is a function of the
         RELATIVE datum (frame, wiring) mod gauge only;
     (c) EXACT GRAM COVARIANCE AT THE WITNESSES: for
         (g, V) in {(g_int, pure-I), (g_int, pure-J),
         (g_r, pure-I)}: LHS Gram(g theta_S g^T, gF, A(V)) ==
         RHS Gram(theta_S, F, A(g_C^T V g_B)) with EXACT
         entrywise equality (sympy expand == 0), 1p and deg-2;
     (d) THE DELTA REDUCTION (symbolic + float wards): the
         transported two-seat law a'_o = a_o cos(delta) +
         c_o sin(delta), delta = y - gamma, with the 1p seat
         identically zero on C_rot; defect-law wards: raw deg-2
         defect = 2t |a'| at (theta_S, pure-I) = 0.1,
         (theta_r, pure-I) = 0.06, (theta', pure-J) = 0.1
         (mirror witness), all <= 1e-12;
     (e) THE WITNESS TABLE AND THE OPTION VERDICT: strict collar
         RP passes EXACTLY (Hermitian + PD by exact LDL) at
         (theta_S, pure-J), (theta', pure-I) and
         (theta_r, (4/5, 3/5)); the 1p/deg-2 spectra of
         (theta_S, pure-J) and (theta', pure-I) agree <= 1e-10
         (covariance corollary; the round-60 V_J numbers
         lam_min 0.3064 / 0.1532); the SAME pure-I wiring fails
         at theta_S (defect 0.1) and the SAME pure-J wiring
         fails at theta' (defect 0.1).  HENCE OPTION (2): the RP
         exclusion of pure-I is a statement AT THE FIXED FRAME
         theta_S -- a frame statement, NOT a gauge-invariant
         wiring no-go; the orbit-invariant content is the
         covariance law itself: EVERY frame's strict collar
         selects exactly its delta = 0 ray, and the pair
         (frame, wiring) enters only through the delta-circle
         coordinate.
 P3  THE ORBIT-INVARIANT PART: THE Z/X EXCLUSION (exact).
     (a) orientation is frame-transport-invariant, symbolically:
         det(R(-gamma) u R(y)) = det u identically, and
         det u = a^2 + c^2 - b^2 - d^2 in Pauli coordinates;
     (b) the Z- and X-wirings have det u = -1 identically, and
         the whole reflection component C_refl has det u =
         -(b^2 + d^2) <= 0 -- so the orientation-propagation
         exclusion E4 fires in EVERY orbit frame: the Z/X
         exclusion IS genuinely rule-gauge-orbit-invariant
         (CONFIRMED, as the lead expected).
 P4  THE CORRECTED CANONICAL SENTENCE (frozen verbatim in this
     log, SHA-hashed).  PERMITTED: "The exact Groebner census
     determines a single admissible three-dimensional wiring
     orbit (the rotation cell C_rot); Z- and X-wirings are
     excluded by orientation propagation, and this exclusion is
     rule-gauge-invariant.  Pure-I and pure-J are connected by an
     integer rule-gauge element and lie on one orbit: pure-I is a
     deployment representative, not a compiler theorem.  Strict
     collar reflection positivity is covariant under the rule
     gauge and depends only on the relative angle delta between
     collar frame and wiring: strict Hermiticity in the theta_S
     frame would select pure-J; the same demand in the
     integer-conjugated frame selects pure-I.  A canonical wiring
     selection requires an additionally derived physical frame."
     FORBIDDEN (equally frozen): "pure-I is compiler-forced";
     "the compiler derives the pure-I wiring"; "strict collar RP
     excludes the J-wiring" (without the frame qualifier).
 C   CONTROLS (must fire; frozen fire rules; NO RNG).
     C1 NON-ORTHOGONAL ELEMENT BREAKS THE KERNEL LAW: the shear
        N = I16 + (1/2) e_0 e_1^T (det 1, not orthogonal) gives
        max|N^T (I + iA) N - (I + i N^T A N)| >= 1/4 exactly
        (the real part N^T N - I != 0) -- orthogonality is
        load-bearing for the covariance;
     C2 NON-RULE GAUGE ELEMENT BREAKS RULE-COVARIANCE: the
        relative-rotation element (g0 but NOT rule stabilizer,
        2-cycle carrier channels only, rational 3/5-4/5)
        transports pure-J OFF the admissible variety: pencil
        quadric a2 c3 - c2 a3 = -4/5 != 0 exact -- the covariance
        orbit statement lives on the RULE gauge only;
     C3 ORIENTATION-FLIP CONTROL: s = (+)_5 Z (+) I6 is
        orthogonal and WOULD legalize the Z-wiring
        (det(Z u) = -det u symbolically) -- but it is NOT
        rule-gauge: s A_CC s^T = -A_CC != A_CC exactly (the bare
        vacuum flips) -- the only way to undo the Z/X exclusion
        leaves the rule gauge: the P3 orbit-invariance is
        non-vacuous;
     C4 eta = +1 at the bare point breaks collar Gram
        Hermiticity (raw defect >= 0.4; v519 twist regression);
     C5 CENSUS REGRESSION GATE: pure-I passes E1 + pencil + E4 +
        canonical census 10/10 with J-coordinate exactly +1/200;
        V_Z passes E1/pencil but fails EXACTLY orientation E4
        (dets == -1).

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 a conjugation / frame ward breaks           -> CONJUGATION-BROKEN
  K2 a covariance / machinery ward breaks        -> COVARIANCE-BROKEN
  K3 an orbit-invariance computation breaks      -> ORIENTATION-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): RP-FRAME-COVARIANT
[CONJUGATION-EXACT(theta' = g_int theta_S g_int^{-1}, both
directions; generic element = delta-circle rotation),
KERNEL-COVARIANCE-EXACT(symbolic torus + exact Gram witnesses),
DELTA-ONLY(defect = 2t|a cos delta + c sin delta|),
EXCLUSION-IS-FRAME-STATEMENT(option 2: fixed-Theta_S statement,
not a wiring no-go), Z-X-EXCLUSION-ORBIT-INVARIANT(det u
gauge-invariant), CANONICAL-SENTENCE-FROZEN] / RP-GAUGE-INVARIANT
/ COVARIANCE-PARTIAL / PIPELINE-BROKEN / CONJUGATION-BROKEN /
COVARIANCE-BROKEN / ORIENTATION-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the covariance statement is over the
rule-gauge orbit as constructed in CCXIII/CCXV (torus symbolic +
integer/rational witnesses); whether the actual seam physics
derives a specific collar frame remains outside the formalized
rules; the v898/v903 [O] premise is unmoved; no marker moves.
NO RH claim.

SPEC v1 (2026-08-12): frozen after the declared smoke round; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline):
theta_frame_selector_probe (CCXV: frame orbit, transport,
selection map), seam_wiring_groebner_probe (CCXIII: census,
g_int, C_refl), seam_ness_parent_probe (round 60: Gram
machinery), v519 (eta = +i), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wiring_gauge_rp_audit_probe.py
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

PERMITTED_SENTENCE = (
    "The exact Groebner census determines a single admissible "
    "three-dimensional wiring orbit (the rotation cell C_rot); "
    "Z- and X-wirings are excluded by orientation propagation, "
    "and this exclusion is rule-gauge-invariant.  Pure-I and "
    "pure-J are connected by an integer rule-gauge element and "
    "lie on one orbit: pure-I is a deployment representative, "
    "not a compiler theorem.  Strict collar reflection "
    "positivity is covariant under the rule gauge and depends "
    "only on the relative angle delta between collar frame and "
    "wiring: strict Hermiticity in the theta_S frame would "
    "select pure-J; the same demand in the integer-conjugated "
    "frame selects pure-I.  A canonical wiring selection "
    "requires an additionally derived physical frame.")
FORBIDDEN_SENTENCES = (
    "pure-I is compiler-forced",
    "the compiler derives the pure-I wiring",
    "strict collar RP excludes the J-wiring "
    "(without the frame qualifier)")


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


def pauli_coords(M):
    return (sp.expand((M[0, 0] + M[1, 1]) / 2),
            sp.expand((M[0, 1] + M[1, 0]) / 2),
            sp.expand((M[0, 1] - M[1, 0]) / 2),
            sp.expand((M[0, 0] - M[1, 1]) / 2))


def main():
    print("SEAM.STATE.WIRING.GAUGE.RP.01 -- gauge-covariance audit "
          "of the RP wiring exclusion")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (census rebuild)")
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
    check("S0.4 canonical G_c Pf4 signs rebuilt: 15 nonzero, all "
          "negative",
          all(abs(v) > 1e-16 for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ==================================================================
    section("P1 -- question (a): the conjugation relation")
    # ==================================================================
    T0i = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        T0i[2 * i, 2 * i + 1] = 1
        T0i[2 * i + 1, 2 * i] = 1
    okT_inv = np.array_equal(T0i @ T0i, np.eye(16, dtype=np.int64))
    okT_orth = np.array_equal(T0i @ T0i.T, np.eye(16, dtype=np.int64))
    okT_c6 = np.array_equal(T0i @ O16, O16 @ T0i)
    okT_rev = np.array_equal(T0i @ A16_dep @ T0i, -A16_dep)
    okT_det = int(round(np.linalg.det(T0i.astype(np.float64)))) == 1
    P_S = [2 * i for i in range(8)]
    okT_side = all(T0i[2 * i + 1, 2 * i] == 1 for i in range(8))
    okT_split = all(T0i[r, c] == 0
                    for r in CAR_IDX for c in BND_IDX)

    # census gauge algebra: g0 and rule stabilizer (dims reproduced)
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

    UT2 = sp.expand(u2.T * u2)
    UT3 = sp.expand(u3.T * u3)
    g1_2 = sp.expand(UT2[0, 1])
    g2_2 = sp.expand(UT2[0, 0] - UT2[1, 1])
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
        for symx, val in zip((a2, b2, c2, d2), pauli_coords(du2)):
            d_coords[symx] = val
        for symx, val in zip((a3, b3, c3, d3), pauli_coords(du3)):
            d_coords[symx] = val
        condsI = []
        for f in IDEAL_GENS:
            df = sp.expand(sum(sp.diff(f, x) * d_coords[x]
                               for x in GENS8))
            condsI.append(sp.expand(rem(df)))
        per_elem.append((condsW, condsI, d_coords))
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
    check("P1.1 theta_S wards + census gauge reproduced: theta_S "
          "involution/orthogonal/C6/A16-reversal/det+1/side/split "
          "all exact; dim g0 = %d == 16, rule stabilizer = %d == 9"
          % (dim_g0, dim_stab),
          okT_inv and okT_orth and okT_c6 and okT_rev and okT_det
          and okT_side and okT_split and dim_g0 == 16
          and dim_stab == 9, kill="K1")

    # ---- the integer conjugation relation, both directions (exact)
    T0s = sp.Matrix(T0i.tolist())
    g_int = sp.zeros(16, 16)
    for i in range(5):
        g_int[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Js
    g_int[10:16, 10:16] = sp.eye(6)
    g_int_inv = g_int.T          # orthogonal
    ok_orth_gi = sp.expand(g_int * g_int.T) == sp.eye(16)
    th_int = sp.expand(g_int * T0s * g_int_inv)
    # forward: theta^(I) = g_int theta_S g_int^{-1}
    ok_fw = all(
        th_int[2 * i:2 * i + 2, 2 * i:2 * i + 2] == -Xs
        for i in range(5)) and all(
        th_int[10 + 2 * i:12 + 2 * i, 10 + 2 * i:12 + 2 * i] == Xs
        for i in range(3))
    # backward: theta_S = g_int theta' g_int^{-1} (conjugation by
    # g_int is an involution on the frame pair, since g_int^2 is
    # in the isotropy of theta_S)
    ok_bw = sp.expand(g_int * th_int * g_int_inv - T0s) \
        == sp.zeros(16, 16)
    gsq = sp.expand(g_int * g_int)
    ok_iso = sp.expand(gsq * T0s * gsq.T - T0s) == sp.zeros(16, 16)
    O16s = sp.Matrix(O16.tolist())
    A16s = sp.Matrix(A16_dep.tolist())

    def frame_legal(th):
        inv = sp.expand(th * th) == sp.eye(16)
        c6 = sp.expand(th * O16s - O16s * th) == sp.zeros(16, 16)
        rev = sp.expand(th * A16s * th + A16s) == sp.zeros(16, 16)
        return inv and c6 and rev

    check("P1.2 THE CONJUGATION RELATION (exact, both directions): "
          "theta^(I) = g_int theta_S g_int^{-1} (per carrier pair "
          "-X, boundary X: %s) AND theta_S = g_int theta^(I) "
          "g_int^{-1} (%s; g_int^2 in the isotropy of theta_S: "
          "%s); g_int orthogonal (%s); both frames rule-legal "
          "(%s, %s)"
          % (ok_fw, ok_bw, ok_iso, ok_orth_gi,
             frame_legal(T0s), frame_legal(th_int)),
          ok_fw and ok_bw and ok_iso and ok_orth_gi
          and frame_legal(T0s) and frame_legal(th_int), kill="K1")

    # ---- attached-wiring correspondence under g_int (exact)
    def wiring(u2v, u3v):
        return {a2: u2v[0], b2: u2v[1], c2: u2v[2], d2: u2v[3],
                a3: u3v[0], b3: u3v[1], c3: u3v[2], d3: u3v[3]}

    wI = wiring((-1, 0, 0, 0), (-1, 0, 0, 0))
    wJ = wiring((0, 0, 1, 0), (0, 0, 1, 0))
    V_I = V_sym.subs(wI)
    V_J = V_sym.subs(wJ)
    ok_VI = sp.expand(V_I - sp.Matrix(Vdep.tolist())) \
        == sp.zeros(10, 6)
    gC = g_int[0:10, 0:10]
    gB = g_int[10:16, 10:16]
    V_J_tr = sp.expand(gC.T * V_J * gB)
    V_I_tr = sp.expand(gC.T * V_I * gB)
    # smoke-disclosed signs: pure-J -> pure-(+I), pure-I -> pure-(+J)
    ok_JtoI = sp.expand(V_J_tr - V_sym.subs(
        wiring((1, 0, 0, 0), (1, 0, 0, 0)))) == sp.zeros(10, 6)
    ok_ItoJ = sp.expand(V_I_tr - V_J) == sp.zeros(10, 6)
    # selected-ray transport: g_C (lam J2) g_B^T per pair = -lam I
    lam = sp.symbols("lam", real=True)
    sel_tr = sp.expand(Js * (lam * Js) * sp.eye(2))
    ok_sel = sel_tr == sp.expand(-lam * sp.eye(2))
    check("P1.3 attached-wiring correspondence under g_int "
          "(exact): pure-J transports to pure-(+I) (%s), pure-I "
          "to pure-(+J) (%s) [smoke-disclosed signs; same +-ray "
          "orbit as CCXIII's pure-(-J)]; selected-ray transport "
          "g_C (lam J2) g_B^T = -lam I per pair (%s): the frame "
          "and its selected wiring move together"
          % (ok_JtoI, ok_ItoJ, ok_sel),
          ok_JtoI and ok_ItoJ and ok_sel, kill="K1")

    # ---- generic extension: the symbolic torus (exact)
    cg, sg, cy, sy = sp.symbols("cg sg cy sy", real=True)
    cg0, sg0 = sp.symbols("cg0 sg0", real=True)
    Rg = sp.Matrix([[cg, -sg], [sg, cg]])
    Ry = sp.Matrix([[cy, -sy], [sy, cy]])
    Rg0 = sp.Matrix([[cg0, -sg0], [sg0, cg0]])
    relg = [cg ** 2 + sg ** 2 - 1, cy ** 2 + sy ** 2 - 1,
            cg0 ** 2 + sg0 ** 2 - 1]

    def redrel(e):
        return sp.expand(sp.reduced(sp.expand(e), relg,
                                    cg, sg, cy, sy, cg0, sg0)[1])

    def redrel_mat(M):
        return sp.Matrix(M.rows, M.cols,
                         lambda i, j: redrel(M[i, j]))

    g_tor = sp.zeros(16, 16)
    for i in range(5):
        g_tor[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Rg
    for i in range(3):
        g_tor[10 + 2 * i:12 + 2 * i, 10 + 2 * i:12 + 2 * i] = Ry
    th_tor = sp.expand(g_tor * T0s * g_tor.T)
    # smoke-corrected sign: R X R^T = cos(2g) X - sin(2g) Z in
    # the deployed J/R convention
    pair_form = sp.expand((cg ** 2 - sg ** 2) * Xs
                          - 2 * cg * sg * Zs)
    ok_pair = all(
        redrel_mat(th_tor[2 * i:2 * i + 2, 2 * i:2 * i + 2]
                   - pair_form) == sp.zeros(2, 2)
        for i in range(5))
    ok_inv_t = redrel_mat(sp.expand(th_tor * th_tor) - sp.eye(16)) \
        == sp.zeros(16, 16)
    ok_c6_t = redrel_mat(sp.expand(th_tor * O16s - O16s * th_tor)) \
        == sp.zeros(16, 16)
    ok_rev_t = redrel_mat(sp.expand(th_tor * A16s * th_tor + A16s)) \
        == sp.zeros(16, 16)
    # angle addition: R(g0) [pair_form(gamma)] R(g0)^T =
    # pair_form(gamma + g0)
    Cc = cg * cg0 - sg * sg0
    Ss = sg * cg0 + cg * sg0
    added = sp.expand((Cc ** 2 - Ss ** 2) * Xs - 2 * Cc * Ss * Zs)
    conj = sp.expand(Rg0 * pair_form * Rg0.T)
    ok_add = redrel_mat(conj - added) == sp.zeros(2, 2)
    check("P1.4 GENERIC EXTENSION (symbolic torus): "
          "g(gamma, y) theta_S g^T has per-carrier-pair block "
          "cos(2g) X - sin(2g) Z (%s); frame legality IDENTICAL "
          "on the torus (involution %s, C6 %s, A16-reversal %s); "
          "conjugation composes by angle addition (%s): a generic "
          "rule element acts as a delta-circle rotation"
          % (ok_pair, ok_inv_t, ok_c6_t, ok_rev_t, ok_add),
          ok_pair and ok_inv_t and ok_c6_t and ok_rev_t and ok_add,
          kill="K1")

    # ==================================================================
    section("P2 -- question (b): covariance of the RP Gram forms")
    # ==================================================================
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

    def gram_idx(basis, r, eta, wick):
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
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]
    POS1 = [(p,) for p in range(8)]
    POS2 = [()] + [tuple(c) for c in
                   itertools.combinations(range(8), 2)]

    def gram_gen(theta_f, F_f, eta, A, basis_pos):
        W = np.eye(16, dtype=complex) + 1j * A
        imgs_ = [theta_f @ F_f[p] for p in range(len(F_f))]

        def wickv(vecs):
            k = len(vecs)
            if k % 2 == 1:
                return 0.0 + 0j
            if k == 0:
                return 1.0 + 0j
            K = [[vecs[p] @ W @ vecs[q] for q in range(k)]
                 for p in range(k)]

            def rec(idxs):
                if not idxs:
                    return 1.0 + 0j
                head, rest = idxs[0], idxs[1:]
                tot = 0.0 + 0j
                for j, bpos in enumerate(rest):
                    sub = rest[:j] + rest[j + 1:]
                    tot += (-1) ** j * K[head][bpos] * rec(sub)
                return tot
            return rec(list(range(k)))

        n = len(basis_pos)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis_pos):
            va = [imgs_[p] for p in reversed(ma)]
            coeff = eta ** len(ma)
            for bi, mb in enumerate(basis_pos):
                vb = [F_f[p] for p in mb]
                M[ai, bi] = coeff * wickv(va + vb)
        return M

    A_CCf = A_CC.astype(np.float64)
    J3f = J3.astype(np.float64)

    def parentV_f(kap, m, tt, V):
        A = np.zeros((16, 16))
        A[np.ix_(CAR_IDX, CAR_IDX)] = kap * A_CCf
        A[np.ix_(BND_IDX, BND_IDX)] = m * J3f
        A[np.ix_(CAR_IDX, BND_IDX)] = tt * V
        A[np.ix_(BND_IDX, CAR_IDX)] = -tt * V.T
        return A

    T0f = T0i.astype(np.float64)
    F_S = [np.eye(16)[:, a] for a in P_S]
    A_dep = parentV_f(0.5, 0.5, 0.05, Vdep.astype(np.float64))
    wk_dep = wick_factory(A_dep)
    M1_idx = gram_idx(B1_S, r_S, 1j, wk_dep)
    M2_idx = gram_idx(B2_S, r_S, 1j, wk_dep)
    M1_gen = gram_gen(T0f, F_S, 1j, A_dep, POS1)
    M2_gen = gram_gen(T0f, F_S, 1j, A_dep, POS2)
    dev_m = max(float(np.max(np.abs(M1_idx - M1_gen))),
                float(np.max(np.abs(M2_idx - M2_gen))))
    D2S = M2_gen - M2_gen.conj().T
    defS = float(np.max(np.abs(D2S)))
    nentS = int(np.sum(np.abs(D2S) > 1e-12))
    check("P2.1 machinery regression: general-theta == round-60 "
          "index machinery entrywise (max dev %.1e <= 1e-12); "
          "strict theta_S at the deployed parent: raw deg-2 "
          "defect %.4f == 2t = 0.1, %d == 30 entries"
          % (dev_m, defS, nentS),
          dev_m <= 1e-12 and abs(defS - 0.1) <= 1e-12
          and nentS == 30, kill="K2")

    # ---- THE KERNEL-COVARIANCE LAW (symbolic torus; the proof)
    kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                    sp.Rational(1, 20))

    def exact_parent(Vm):
        A_ex = sp.zeros(16, 16)
        A_ex[0:10, 0:10] = kapQ * A_CCs
        A_ex[10:16, 10:16] = mQ * J3s
        A_ex[0:10, 10:16] = tQ * Vm
        A_ex[10:16, 0:10] = -tQ * Vm.T
        return A_ex

    gC_tor = g_tor[0:10, 0:10]
    gB_tor = g_tor[10:16, 10:16]
    ok_orth_tor = redrel_mat(
        sp.expand(g_tor.T * g_tor) - sp.eye(16)) == sp.zeros(16, 16)
    A_of_V = exact_parent(V_sym)
    V_tr_sym = sp.expand(gC_tor.T * V_sym * gB_tor)
    A_of_Vtr = exact_parent(V_tr_sym)
    E_cov = redrel_mat(sp.expand(g_tor.T * A_of_V * g_tor)
                       - A_of_Vtr)
    ok_cov_law = E_cov == sp.zeros(16, 16)
    check("P2.2 THE KERNEL-COVARIANCE LAW (symbolic, generic "
          "wiring, full torus): g^T g = I16 (%s) and "
          "g^T A(V) g = A(g_C^T V g_B) IDENTICALLY (%s) => every "
          "kernel dot product u^T (I + iA) v, hence EVERY Gram "
          "entry, is invariant under (theta, F, V) -> "
          "(g theta g^T, gF, V) with V -> g_C^T V g_B: strict-"
          "collar RP is a function of the RELATIVE (frame, "
          "wiring) datum only"
          % (ok_orth_tor, ok_cov_law),
          ok_orth_tor and ok_cov_law, kill="K2")

    # ---- exact Gram machinery
    def wickv_exact_factory(Aex):
        Wm = sp.eye(16) + sp.I * Aex

        def wickv(vecs):
            k = len(vecs)
            if k % 2 == 1:
                return sp.Integer(0)
            if k == 0:
                return sp.Integer(1)
            K = [[sp.expand((vecs[p].T * Wm * vecs[q])[0, 0])
                  for q in range(k)] for p in range(k)]

            def rec(idxs):
                if not idxs:
                    return sp.Integer(1)
                head, rest = idxs[0], idxs[1:]
                tot = sp.Integer(0)
                for j, bpos in enumerate(rest):
                    w = K[head][bpos]
                    if w != 0:
                        sub = rest[:j] + rest[j + 1:]
                        tot += sp.Integer(-1) ** j * w * rec(sub)
                return tot
            return rec(list(range(k)))
        return wickv

    def gram_gen_exact(theta_s, F_cols, eta, wickv, basis_pos):
        imgs_ = [sp.expand(theta_s * f) for f in F_cols]
        n = len(basis_pos)
        M = sp.zeros(n, n)
        for ai, ma in enumerate(basis_pos):
            va = [imgs_[p] for p in reversed(ma)]
            coeff = eta ** len(ma)
            for bi, mb in enumerate(basis_pos):
                vb = [F_cols[p] for p in mb]
                M[ai, bi] = sp.expand(coeff * wickv(va + vb))
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

    eye16 = sp.eye(16)
    F_S_sym = [eye16[:, a] for a in P_S]
    Rr = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                    [sp.Rational(4, 5), sp.Rational(3, 5)]])
    g_r = sp.zeros(16, 16)
    for i in range(5):
        g_r[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Rr
    g_r[10:16, 10:16] = sp.eye(6)
    th_r = sp.expand(g_r * T0s * g_r.T)

    def exact_grams(th, F_cols, Vm):
        wv = wickv_exact_factory(exact_parent(Vm))
        M1 = gram_gen_exact(th, F_cols, sp.I, wv, POS1)
        M2 = gram_gen_exact(th, F_cols, sp.I, wv, POS2)
        return M1, M2

    def transported(g, Vm):
        return sp.expand(g[0:10, 0:10].T * Vm * g[10:16, 10:16])

    # covariance witness pairs (LHS in the conjugated frame,
    # RHS at theta_S with the transported wiring)
    cov_pairs = [("g_int, pure-I", g_int, th_int, V_I),
                 ("g_int, pure-J", g_int, th_int, V_J),
                 ("g_r,   pure-I", g_r, th_r, V_I)]
    lhs_store = {}
    ok_cov_all = True
    for nm, g, th, Vm in cov_pairs:
        F_g = [sp.expand(g * f) for f in F_S_sym]
        L1, L2 = exact_grams(th, F_g, Vm)
        R1, R2 = exact_grams(T0s, F_S_sym, transported(g, Vm))
        eq1 = sp.expand(L1 - R1) == sp.zeros(*L1.shape)
        eq2 = sp.expand(L2 - R2) == sp.zeros(*L2.shape)
        lhs_store[nm] = (L1, L2)
        ok_cov_all &= (eq1 and eq2)
        print("      cov witness (%s): 1p exact-equal %s, deg-2 "
              "exact-equal %s" % (nm, eq1, eq2), flush=True)
    check("P2.3 EXACT GRAM COVARIANCE at the witnesses: "
          "Gram(g theta_S g^T, gF, A(V)) == Gram(theta_S, F, "
          "A(g_C^T V g_B)) with exact entrywise equality on all "
          "3 (gauge, wiring) pairs, 1p and deg-2", ok_cov_all,
          kill="K2")

    # ---- the delta reduction (symbolic two-seat law + defect wards)
    def redrel4(e):
        return sp.expand(sp.reduced(
            sp.expand(e), relg[:2], cg, sg, cy, sy)[1])

    up2 = sp.expand(Rg.T * u2 * Ry)
    up3 = sp.expand(Rg.T * u3 * Ry)
    a2p, b2p, c2p, d2p = [redrel4(x) for x in pauli_coords(up2)]
    a3p, b3p, c3p, d3p = [redrel4(x) for x in pauli_coords(up3)]
    Cd = cg * cy + sg * sy
    Sd = sy * cg - cy * sg
    rot_sub = {b2: 0, d2: 0, b3: 0, d3: 0}
    ok_cf2 = redrel4(a2p.subs(rot_sub) - (a2 * Cd + c2 * Sd)) == 0
    ok_cf3 = redrel4(a3p.subs(rot_sub) - (a3 * Cd + c3 * Sd)) == 0
    ok_1p = (redrel4(b2p.subs(rot_sub)) == 0
             and redrel4(b3p.subs(rot_sub)) == 0)
    # defect-law float wards: raw deg-2 defect = 2t|a'| at three
    # equal-orbit configurations
    gf_r = np.array(g_r.tolist(), dtype=np.float64)
    th_rf = gf_r @ T0f @ gf_r.T
    F_rf = [gf_r @ f for f in F_S]
    M2r_f = gram_gen(th_rf, F_rf, 1j, A_dep, POS2)
    defR = float(np.max(np.abs(M2r_f - M2r_f.conj().T)))
    gf_i = np.array(g_int.tolist(), dtype=np.float64)
    th_if = gf_i @ T0f @ gf_i.T
    F_if = [gf_i @ f for f in F_S]
    V_Jf = np.array(V_J.tolist(), dtype=np.float64)
    A_J = parentV_f(0.5, 0.5, 0.05, V_Jf)
    M2iJ = gram_gen(th_if, F_if, 1j, A_J, POS2)
    defIJ = float(np.max(np.abs(M2iJ - M2iJ.conj().T)))
    check("P2.4 THE DELTA REDUCTION: transported two-seat law "
          "a' = a cos(delta) + c sin(delta) (%s, %s), 1p seat "
          "identically 0 on C_rot (%s); defect-law wards "
          "2t|a'|: (theta_S, pure-I) %.4f == 0.1, "
          "(theta_r, pure-I) %.4f == 0.06, (theta', pure-J) "
          "%.4f == 0.1 (mirror witness), all <= 1e-12"
          % (ok_cf2, ok_cf3, ok_1p, defS, defR, defIJ),
          ok_cf2 and ok_cf3 and ok_1p
          and abs(defS - 0.1) <= 1e-12
          and abs(defR - 0.06) <= 1e-12
          and abs(defIJ - 0.1) <= 1e-12, kill="K2")

    # ---- the witness table and the option verdict
    M1_SJ, M2_SJ = exact_grams(T0s, F_S_sym, V_J)
    h_SJ = herm_exact(M1_SJ) and herm_exact(M2_SJ)
    p1, piv1 = psd_exact(M1_SJ)
    p2, piv2 = psd_exact(M2_SJ)
    pd_SJ = (p1 and all(p > 0 for p in piv1)
             and p2 and all(p > 0 for p in piv2))
    L1_iI, L2_iI = lhs_store["g_int, pure-I"]
    h_iI = herm_exact(L1_iI) and herm_exact(L2_iI)
    q1, qiv1 = psd_exact(L1_iI)
    q2, qiv2 = psd_exact(L2_iI)
    pd_iI = (q1 and all(p > 0 for p in qiv1)
             and q2 and all(p > 0 for p in qiv2))
    # spectra corollary
    s1a = np.sort(np.linalg.eigvalsh(np.array(
        M1_SJ.evalf(16), dtype=complex)))
    s1b = np.sort(np.linalg.eigvalsh(np.array(
        L1_iI.evalf(16), dtype=complex)))
    s2a = np.sort(np.linalg.eigvalsh(np.array(
        M2_SJ.evalf(16), dtype=complex)))
    s2b = np.sort(np.linalg.eigvalsh(np.array(
        L2_iI.evalf(16), dtype=complex)))
    dev_sp = max(float(np.max(np.abs(s1a - s1b))),
                 float(np.max(np.abs(s2a - s2b))))
    lm1, lm2 = float(s1a[0]), float(s2a[0])
    # theta' + pure-J fails (exact anti-Hermitian defect)
    _L1_iJ, L2_iJ = lhs_store["g_int, pure-J"]
    D_iJ = sp.expand(L2_iJ - L2_iJ.conjugate().T)
    def_iJ = float(max(abs(complex(x)) for x in
                       np.array(D_iJ.evalf(16),
                                dtype=complex).flatten()))
    # theta_r + its selected ray passes exactly
    w_sel = wiring((sp.Rational(4, 5), 0, sp.Rational(3, 5), 0),
                   (sp.Rational(4, 5), 0, sp.Rational(3, 5), 0))
    V_sel = V_sym.subs(w_sel)
    F_r_sym = [sp.expand(g_r * f) for f in F_S_sym]
    M1_rs, M2_rs = exact_grams(th_r, F_r_sym, V_sel)
    h_rs = herm_exact(M1_rs) and herm_exact(M2_rs)
    r1, riv1 = psd_exact(M1_rs)
    r2, riv2 = psd_exact(M2_rs)
    pd_rs = (r1 and all(p > 0 for p in riv1)
             and r2 and all(p > 0 for p in riv2))
    check("P2.5 THE WITNESS TABLE => OPTION (2): strict RP passes "
          "EXACTLY at (theta_S, pure-J) (%s/%s), (theta', pure-I) "
          "(%s/%s) and (theta_r, (4/5,3/5)) (%s/%s); spectra of "
          "the first two agree (dev %.1e <= 1e-10; lam_min %.4f "
          "== 0.3064 +- 0.005, %.4f == 0.1532 +- 0.005); the SAME "
          "pure-I fails at theta_S (0.1) and the SAME pure-J "
          "fails at theta' (%.4f == 0.1): the RP exclusion is a "
          "FIXED-FRAME statement, NOT a gauge-invariant wiring "
          "no-go"
          % (h_SJ, pd_SJ, h_iI, pd_iI, h_rs, pd_rs, dev_sp,
             lm1, lm2, def_iJ),
          h_SJ and pd_SJ and h_iI and pd_iI and h_rs and pd_rs
          and dev_sp <= 1e-10 and abs(lm1 - 0.3064) <= 5e-3
          and abs(lm2 - 0.1532) <= 5e-3
          and abs(def_iJ - 0.1) <= 1e-12, kill="K2")

    # ==================================================================
    section("P3 -- the orbit-invariant part: the Z/X exclusion")
    # ==================================================================
    det_u = sp.expand(u2.det())
    ok_detform = sp.expand(
        det_u - (a2 ** 2 + c2 ** 2 - b2 ** 2 - d2 ** 2)) == 0
    det_tr = redrel4(sp.expand(up2.det()) - det_u)
    ok_detinv = det_tr == 0
    detZ = det_u.subs({a2: 0, b2: 0, c2: 0, d2: 1})
    detX = det_u.subs({a2: 0, b2: 1, c2: 0, d2: 0})
    # C_refl: a = c = 0 => det = -(b^2 + d^2)
    det_refl = sp.expand(det_u.subs({a2: 0, c2: 0}))
    ok_refl = sp.expand(det_refl + b2 ** 2 + d2 ** 2) == 0
    check("P3.1 THE Z/X EXCLUSION IS ORBIT-INVARIANT (exact): "
          "det u = a^2 + c^2 - b^2 - d^2 (%s) is frame-transport-"
          "invariant det(R(-g) u R(y)) = det u identically (%s); "
          "det = -1 for Z (%s) and X (%s) in EVERY orbit frame, "
          "and the whole reflection component has det = "
          "-(b^2 + d^2) <= 0 (%s): orientation propagation E4 "
          "fires on the entire rule-gauge orbit -- CONFIRMED "
          "genuinely gauge-invariant"
          % (ok_detform, ok_detinv, detZ, detX, ok_refl),
          ok_detform and ok_detinv and detZ == -1 and detX == -1
          and ok_refl, kill="K3")

    # ==================================================================
    section("P4 -- the corrected canonical sentence (frozen)")
    # ==================================================================
    sent_sha = hashlib.sha256(
        PERMITTED_SENTENCE.encode("utf-8")).hexdigest()
    print("      PERMITTED (verbatim, sha256 %s):" % sent_sha[:16])
    print("      | " + PERMITTED_SENTENCE.replace(".  ", ".\n      | "))
    print("      FORBIDDEN (verbatim):")
    for s in FORBIDDEN_SENTENCES:
        print("      | " + s)
    check("P4.1 canonical sentence frozen (permitted sha256 %s...; "
          "%d forbidden formulations recorded)"
          % (sent_sha[:16], len(FORBIDDEN_SENTENCES)),
          len(PERMITTED_SENTENCE) > 0
          and len(FORBIDDEN_SENTENCES) == 3)

    # ==================================================================
    section("P5 -- controls (must fire; deterministic)")
    # ==================================================================
    # C1 non-orthogonal element breaks the kernel law
    N_sh = sp.eye(16)
    N_sh[0, 1] = sp.Rational(1, 2)
    A_I_ex = exact_parent(V_I)
    E_C1 = sp.expand(N_sh.T * (sp.eye(16) + sp.I * A_I_ex) * N_sh
                     - (sp.eye(16)
                        + sp.I * sp.expand(N_sh.T * A_I_ex * N_sh)))
    max_C1 = float(max(abs(complex(x)) for x in
                       np.array(E_C1.evalf(16),
                                dtype=complex).flatten()))
    check("C1 non-orthogonal shear N = I + (1/2) e0 e1^T breaks "
          "the kernel law: max|N^T (I+iA) N - (I + i N^T A N)| = "
          "%.4f >= 0.25 (the real part N^T N - I != 0) -- "
          "orthogonality is load-bearing" % max_C1,
          max_C1 >= 0.25, kill="K7")

    # C2 non-rule gauge element: transported pure-J leaves the variety
    g_relm = sp.eye(16)
    for i in TWO:
        r0 = 2 * (i - 1)
        g_relm[r0:r0 + 2, r0:r0 + 2] = Rr
    Vp_rel = sp.expand(g_relm[0:10, 0:10].T * V_J)
    u2rel = Vp_rel[2 * (rep2 - 1):2 * rep2, 0:2]
    u3rel = Vp_rel[2 * (rep3 - 1):2 * rep3, 0:2]
    a2r_, _b, c2r_, _d = pauli_coords(u2rel)
    a3r_, _b3x, c3r_, _d3x = pauli_coords(u3rel)
    minor_val = sp.expand(a2r_ * c3r_ - c2r_ * a3r_)
    check("C2 relative-rotation element (g0, NOT rule stabilizer): "
          "transported pure-J violates the pencil quadric "
          "a2 c3 - c2 a3 = %s == -4/5 != 0 -- the covariance "
          "orbit statement lives on the RULE gauge only"
          % minor_val, minor_val == -sp.Rational(4, 5), kill="K7")

    # C3 orientation-flip control
    s_fl = sp.zeros(16, 16)
    for i in range(5):
        s_fl[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Zs
    s_fl[10:16, 10:16] = sp.eye(6)
    ok_orth_s = sp.expand(s_fl * s_fl.T) == sp.eye(16)
    flip_vac = sp.expand(s_fl[0:10, 0:10] * A_CCs
                         * s_fl[0:10, 0:10].T + A_CCs) \
        == sp.zeros(10, 10)
    det_flip = sp.expand(sp.expand(Zs * u2).det() + det_u) == 0
    check("C3 orientation-flip control s = (+)_5 Z (+) I6: "
          "orthogonal (%s) and WOULD legalize Z "
          "(det(Z u) = -det u: %s) -- but s A_CC s^T = -A_CC "
          "(vacuum flips: %s): the only way to undo the Z/X "
          "exclusion leaves the rule gauge"
          % (ok_orth_s, det_flip, flip_vac),
          ok_orth_s and det_flip and flip_vac, kill="K7")

    # C4 eta = +1 breaks bare Hermiticity
    A0f = np.tanh(0.5) * A16_dep.astype(np.float64)
    M1e = gram_gen(T0f, F_S, 1.0, A0f, POS1)
    defE = float(np.max(np.abs(M1e - M1e.conj().T)))
    check("C4 eta = +1 at the bare point: 1p Gram Hermiticity "
          "defect %.4f >= 0.4 (v519 twist regression)" % defE,
          defE >= 0.4, kill="K7")

    # C5 census regression gate
    def eval_E1(sub):
        return [sp.expand(g.subs(sub)) for g in
                (g1_2, g2_2, g1_3, g2_3)]

    def eval_pencil(sub):
        return [sp.expand(g.subs(sub)) for g in (pI, pX, pZ)]

    def eval_dets(sub):
        return (sp.expand(u2.det().subs(sub)),
                sp.expand(u3.det().subs(sub)))

    def census_exact(sub):
        lamQ = mQ / (1 - mQ ** 2)
        Vm = V_sym.subs(sub)
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

    E1I = eval_E1(wI)
    penI = eval_pencil(wI)
    detI = eval_dets(wI)
    nzI, sigI, JcoI = census_exact(wI)
    wZ = wiring((0, 0, 0, 1), (0, 0, 0, 1))
    detZc = eval_dets(wZ)
    E1Z = eval_E1(wZ)
    penZ = eval_pencil(wZ)
    check("C5 census regression gate: pure-I passes E1 %s == 0, "
          "pencil %s == 0, dets %s > 0, census %d/10 canonical "
          "%d/10, J-coordinate %s == 1/200; V_Z passes E1/pencil "
          "(%s, %s) but fails EXACTLY orientation (dets %s == "
          "(-1, -1))"
          % (E1I, penI, detI, nzI, sigI, JcoI,
             all(e == 0 for e in E1Z), all(e == 0 for e in penZ),
             detZc),
          all(e == 0 for e in E1I) and all(e == 0 for e in penI)
          and all(d > 0 for d in detI) and nzI == 10 and sigI == 10
          and JcoI == sp.Rational(1, 200)
          and all(e == 0 for e in E1Z)
          and all(e == 0 for e in penZ)
          and all(d == -1 for d in detZc), kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    all_ok = (n_pass == n_tot) and not KILLS
    if all_ok:
        verdict = ("RP-FRAME-COVARIANT [CONJUGATION-EXACT"
                   "(theta' = g_int theta_S g_int^{-1}, both "
                   "directions; generic element = delta-circle "
                   "rotation), KERNEL-COVARIANCE-EXACT(symbolic "
                   "torus + exact Gram witnesses), DELTA-ONLY"
                   "(defect = 2t|a cos delta + c sin delta|), "
                   "EXCLUSION-IS-FRAME-STATEMENT(option 2: "
                   "fixed-Theta_S statement, not a wiring no-go), "
                   "Z-X-EXCLUSION-ORBIT-INVARIANT(det u "
                   "gauge-invariant), CANONICAL-SENTENCE-FROZEN]")
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
    ('seam_wiring_groebner_probe', _SRC_0, 30, (), 'WIRING-DEGENERATE', 0),
    ('theta_frame_selector_probe', _SRC_1, 26, (), 'THETA-CONVENTIONAL', 0),
    ('wiring_gauge_rp_audit_probe', _SRC_2, 21, (), 'RP-FRAME-COVARIANT', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v911 -- SEAM.STATE.WIRING.SELECTOR.01 (closes the v908-registered contract) + THETA.SELECTOR.01 + WIRING.GAUGE.RP.01: THE WIRING FREEDOM THEOREM -- the compiler determines the wiring ORBIT (one admissible 3-dim component C_rot; Z/X excluded gauge-invariantly by orientation propagation); pure-I is a DEPLOYMENT REPRESENTATIVE, not a compiler theorem (integer gauge connects pure-I and pure-J); no compiler demand pins the theta_S collar frame (THETA-CONVENTIONAL, five demand classes silent-on-angle); strict-collar RP is exactly rule-gauge covariant and depends only on the relative angle delta (RP-FRAME-COVARIANT, the pure-I exclusion is a frame statement, not a wiring no-go)')
    print("(frozen probes embedded byte-exact and executed verbatim; zero RH content)")
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
    print("v911: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the wiring question is closed as a compiler-freedom theorem: freedom group = rule-gauge frame orbit, selection quotient = the delta-circle; a canonical wiring selection requires an additionally derived physical frame; "pure-I is compiler-forced" is a FORBIDDEN sentence')
    print("[%s] v911 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
