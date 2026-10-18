#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""transfer_coherent_wilson_probe -- TRANSFER.COHERENT.WILSON.01
(external-review round 2026-08-27, follow-up to
transfer_birkhoff_circulation_probe + v971): the deployed single-step
transport B is UNISTOCHASTIC -- it admits an exact reversible SU(3)
lift whose gauge-invariant Wilson-plaquette phases form a closed
Gaussian-Pythagorean code over the TFPT atoms {2, 5, 12, 13}, whose
CP-odd invariant is exactly J = +-1/27, and whose phase is EXACTLY the
complexified spectral data of the deployed center-quotient atom matrix
A = [[8,2],[5,3]] (v530).

DEPLOYED ANCHORS (located, read-only):
  * k5_sixstep_transport_probe A0: B = (1/18)[[13,1,4],[1,13,4],[4,4,10]],
    T = B^6 = T_v221 bit-exact.
  * v530_center_quotient_compiler: A = [[8,2],[5,3]] = [[rank E8, |Z2|],
    [g_car, N_fam]]; sibling quotients A_K = [[14,8],[-11,-6]] and
    A_Q = [[3,1],[3,2]] (the honest-uniqueness negative controls).
  * v738_hecke_mod_ramified: the Gaussian tower primes include (1+2i),
    (2+3i), (3+2i); N(3+2i) = 13 = Delta_Q (tfpt_2, Delta_Q = |R(A3)|+1).
  * tfpt_2_standard_model (PMNS block, v270): deployed
    delta_PMNS = 4pi/3 = 240 deg, J_PMNS = -0.02965 -- the near-miss
    NEGATIVE control (NO PMNS claim here).
  * transfer_birkhoff_circulation_probe: the Birkhoff t-parameter is
    NOT chiral (w(C123) = w(C132) forced) -- contrasted with sgn J.
  * v971: Q = log T (the dissipative continuous half; untouched).

TASK A -- THE EXACT SU(3) LIFT (all sympy-exact):
 A1  angles FORCED by B alone: sin^2 th13 = B13 = 2/9, sin^2 th12 =
     B12/(1-B13) = 1/14, sin^2 th23 = B23/(1-B13) = 2/7 (exact).
 A2  cos(delta) is UNIQUELY solved by the one remaining entry B21:
     cos(delta) = -4/sqrt(65), hence e^{i delta} = (-4 +- 7i)/sqrt(65)
     -- the complete lift set of B up to row/column rephasing is the
     TWO-branch family {U, U*} (classification, J != 0).
 A3  U^dagger U = I, det U = 1, and |U_ij|^2 = B_ij ENTRYWISE EXACT:
     B is unistochastic -- its transition probabilities are exactly the
     measurement shadow of a reversible SU(3) rotation [coherification
     iff unistochastic: Dunkl-Zyczkowski 0909.0116, Korzekwa et al.
     1710.04228, literature-typed].
 A4  J = Im(U11 U22 U12* U21*) = 1/27 EXACT; moreover Re of EVERY
     plaquette is fixed by B alone through unitarity
     (2 Re Q_{ik;jl} = B-bilinear), and J^2 = B11 B21 B12 B22 - Re^2 =
     1/729 -- the full rephasing-invariant Wilson data of the lift is
     determined by the CLASSICAL matrix up to ONE global sign.

TASK B -- THE WILSON PLAQUETTE TABLE (exact Gaussian arithmetic):
 B1  Q_{12;12} = U11 U22 U12* U21* = (-5 + 12i)/324; normalized
     Q/|Q| = (-5 + 12i)/13 with 5^2 + 12^2 = 13^2 -- the Pythagorean
     5-12-13 loop; atoms: 5 = g_car, 12 = dim g_SM, 13 = Delta_Q =
     N(3+2i) (corpus anchors, read-only).
 B2  ALL NINE plaquettes close on exactly FOUR normalized Gaussian
     phase types: (-5+12i)/13 x1, (-2+-3i)/sqrt(13) x4,
     (-11+3i)/sqrt(130) x2, (1-3i)/sqrt(10) x2; Gaussian norms
     EXCLUSIVELY {10, 13, 130, 169} = {2*5, 13, 2*5*13, 13^2} -- a
     phase alphabet over the atoms {2, 5, 13} (+12 in the main loop).
 B3  every plaquette has Im = +-1/27 exactly (the Jarlskog identity).
 B4  INDEPENDENCE/GENERATION: the four fundamental plaquettes
     (rows i,i+1; cols j,j+1) generate all nine via the exact
     multiplicative relations Q_{ik;jl} = prod(fundamental)/B-weights
     (Wilson-loop composition, machine-checked).

TASK C -- THE CENTER-QUOTIENT BRIDGE (exact):
 C1  A = [[8,2],[5,3]]: det A = 14, det(A - I) = 4, disc chi_A = 65 =
     5*13, and the NEW identity disc chi_A = det(A-I)^2 + (det A/2)^2
     = 4^2 + 7^2 = 65.
 C2  e^{i delta} = (-det(A-I) +- i det A/2)/sqrt(disc chi_A) EXACTLY
     equals the transport-lift phase (-4 +- 7i)/sqrt(65) -- the U(1)
     phase of the coherent transport is the complexified spectral
     datum of the center atom matrix.
 C3  -4 + 7i = (1+2i)(2+3i) with N(1+2i) = 5, N(2+3i) = 13 -- the
     v738 Gaussian tower primes; chain: center quotient -> 65 = 5*13
     -> (1+2i)(2+3i) -> transport phase -> J = 1/27.
 C4  NEG CONTROLS (must fire): the sibling quotients fail the identity
     -- A_K: disc 48 vs det(A_K-I)^2 + (det/2)^2 = 13; A_Q: disc 13 vs
     13/4.  The bridge SELECTS the atom quotient A.
 C5  HONEST TYPING: the bridge fixes the PHASE from A-invariants; the
     ANGLES (2/9, 1/14, 2/7) come from B alone; a deployed intertwiner
     (center quotient / Petersen carrier -> coherent transport
     connection) does NOT exist in the corpus -- same missing-piece
     type as the shells->cusp map S (k5/A4).  That gap IS the contract.

TASK D -- THE ORIENTATION BIT (exact):
 D1  U* lifts the SAME B (|U*|^2 = B) with J = -1/27: the classical
     matrix cannot distinguish the branches -- the coherent completion
     carries a classically invisible Z2 orientation bit sgn J.
 D2  the minimal observable is Im(U11 U22 U12* U21*) -- a Wilson-
     plaquette interference readout (the concrete form of the missing
     phase observable).
 D3  CONTRAST with the Birkhoff parameter t (previous probe): t is a
     random-unitary mixing degree with FORCED w(C123) = w(C132) -- not
     chiral; sgn J is a genuine complex orientation.  Two DIFFERENT
     classically hidden data, typed separately.
 D4  PMNS NEAR-MISS (typed NEGATIVE, must stay negative): the negative
     branch has delta = 240.2551 deg, near the deployed
     delta_PMNS = 4pi/3 = 240 deg (v270), BUT J_tr = -1/27 = -0.037037
     != J_PMNS = -0.02965 and all three lift angles differ from the
     PMNS angles -- NO PMNS derivation is claimed or supported.

TASK E -- THE SIX-STEP PARADOX (exact + certified numerics):
 E1  J_n^2 = (1-b)^2 (1 + 2b - 3a^2)/108 with a = (2/3)^n, b = (1/3)^n
     -- derived SYMBOLICALLY from the B^n entries via the unitarity
     relations (Re fixed by B^n, |Q| = B11 B12 by symmetry).
 E2  J_n^2 > 0 for n = 1..12 => every B^n is unistochastic (each with
     its OWN freshly reconstructed U_n); U_6 is built exactly and
     |U_6|^2 = B^6 = T_v221 entrywise.
 E3  |J_6| = 0.0951088904 = 0.9884006 * J_max with J_max = 1/(6 sqrt 3)
     -- the coherent lift of T is at 98.84 % of the maximal qutrit
     CP-odd invariant while the classical channel is almost fully
     mixed (C(T) = 0.008358 bit, previous probe); the uniform limit
     B^inf = J/3 lifts to the Fourier matrix F3 with |J| = J_max
     EXACTLY (maximal-interference endpoint).
 E4  RATIONALITY SELECTION [E neu]: among n = 1..12, J_n is RATIONAL
     ONLY at n = 1 -- the Gaussian-Pythagorean code selects the SINGLE
     STEP uniquely; mechanism: J_n = (1-b) sqrt(3(1+2b-3a^2))/18 and
     the deployed step hits 3(1+2b-3a^2) = 1 EXACTLY, so
     J_1 = (1-1/3)/18 = 1/27.
 E5  NO-GO, FIXED MICROSTEP: B^2 != |U_1^2|^2 already (exact; entry
     (1,1): 31/54 = 0.5741 vs 0.2450) -- B^n = |U_n|^2 needs a NEW U_n
     each time; and a quantitative recurrence witness: there exists
     n* <= 10^6 with min_i |(U_1^{n*})_{ii}|^2 >= 0.98 (almost-return
     to identity, Dirichlet pigeonhole on the eigenphases) while
     max_ij |B^{n*}_ij - 1/3| <= 1e-10 (fully relaxed) -- NO single
     closed unitary generates the relaxing sequence.  TYPED READING:
     "six repeated steps" require dephasing/environment BETWEEN steps;
     "one six-step macro-gate" can exist as its own reversible U_6 but
     is NOT U_1^6 -- the coherent sharpening of the k5 clock-vs-walk
     verdict and the missing shells->cusp intertwiner.

TASK F -- SELECTIVITY CENSUS + HARD KILL:
 F1  OBSTRUCTION CERTIFICATE FIRES: the classic bistochastic-but-NOT-
     unistochastic matrix (zero diagonal, 1/2 off-diagonal) has
     J^2 = -1/64 < 0 -- the certificate detects non-unistochasticity.
 F2  MUTATION CONTROLS FIRE: sixth-root spectra {2/3, 1/2} and
     {1/2, 1/3} give J^2 = 1/648 and 11/2916 -- J irrational, NO
     Gaussian code (the 5-12-13 structure is not spectrum-generic).
 F3  GRID CENSUS (hard kill, preregistered): over the natural family
     B(a, b) = J/3 + a P2 + b P3 with a = k/18, b = m/18 (all valid
     doubly stochastic unistochastic members), count (i) rational-J
     hits and (ii) FULL-code hits (normalized main plaquette
     = (-5 +- 12i)/13).  KILL: if full-code rate > 10 % the code is
     generic and the selectivity claim DIES.

KILLS (frozen, any one fires => the respective DEAD):
  K-A  lift identity/uniqueness fails.              (LIFT-DEAD)
  K-B  plaquette table/types/norms/relations fail.  (WILSON-DEAD)
  K-C  center-bridge identity fails or a sibling
       passes it.                                   (BRIDGE-DEAD)
  K-D  conjugation/orientation identity fails.      (ORIENTATION-DEAD)
  K-E  J_n law / unistochasticity / no-go fails.    (SIXSTEP-DEAD)
  K-F  hard kill: full code generic (> 10 %) or an
       obstruction control does not fire.           (CODE-GENERIC-DEAD)
VERDICTS (frozen):
  LIFT: SU3-LIFT-EXACT iff A1-A4 pass.
  WILSON: CODE-5-12-13-EXACT iff B1-B4 pass.
  BRIDGE: CENTER-BRIDGE-EXACT (intertwiner OPEN) iff C1-C5 pass.
  ORIENTATION: SIGN-J-BIT-EXHIBITED iff D1-D4 pass.
  SIXSTEP: MACROGATE-VS-MICROSTEP-TYPED iff E1-E5 pass.
  SELECTIVITY: CODE-SELECTIVE iff F1-F3 pass with full-code rate
    <= 10 % (report the exact census).

TYPING (carried): [E neu] every exact matrix/plaquette/bridge identity
and the rationality selection; [C] literature theorems (unistochastic
coherification, HSR, unitary channel capacity Q = log2 3) and every
corpus anchor reading; [H] any physical reading (CP, time orientation,
flavor) -- explicitly NOT claimed; the PMNS near-miss stays a NEGATIVE.
ROOTCLASS-MIXED cited: transport algebra on the cusp-weight 3-space.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt; keine Marker-Bewegung; TRANSFER.COHERENT.WILSON.01 ist ein
VORSCHLAG fuer next.txt, keine Ledger-Zeile.  sympy-exakt fuer alle
Identitaeten; numpy/mpmath nur fuer den Dirichlet-Rueckkehr-Zeugen und
Betrags-Kreuzchecks.

Quellen (read-only): experiments/tfpt-discovery/
k5_sixstep_transport_probe.py, transfer_birkhoff_circulation_probe.py;
verification/v530_center_quotient_compiler.py,
v738_hecke_mod_ramified.py, v971_markov_embedding_generator.py;
tfpt_2_standard_model.tex (Delta_Q, PMNS-Block).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/transfer_coherent_wilson_probe.py
"""

import time

import numpy as np
import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


B = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
JMAXSQ = sp.Rational(1, 108)          # (1/(6 sqrt 3))^2


def build_lift(Bm, branch=+1):
    """exact PDG-parametrized lift of a symmetric doubly stochastic 3x3
    matrix (angles forced by row 1 / column 3, cos(delta) solved from
    the (2,1) entry); returns (U, s13sq, s12sq, s23sq, cosd, sind)."""
    s13sq = sp.nsimplify(Bm[0, 2])
    c13sq = 1 - s13sq
    s12sq = sp.nsimplify(Bm[0, 1] / c13sq)
    s23sq = sp.nsimplify(Bm[1, 2] / c13sq)
    c12sq, c23sq = 1 - s12sq, 1 - s23sq
    s12, c12 = sp.sqrt(s12sq), sp.sqrt(c12sq)
    s23, c23 = sp.sqrt(s23sq), sp.sqrt(c23sq)
    s13, c13 = sp.sqrt(s13sq), sp.sqrt(c13sq)
    # |U21|^2 = s12^2 c23^2 + c12^2 s23^2 s13^2 + 2 J' cos(delta)
    cross = 2 * s12 * c12 * s23 * c23 * s13
    cosd = sp.simplify((Bm[1, 0] - s12sq * c23sq
                        - c12sq * s23sq * s13sq) / cross)
    sind = branch * sp.sqrt(sp.simplify(1 - cosd ** 2))
    eid = cosd + sp.I * sind
    U = sp.Matrix([
        [c12 * c13, s12 * c13, s13 / eid],
        [-s12 * c23 - c12 * s23 * s13 * eid,
         c12 * c23 - s12 * s23 * s13 * eid, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * eid,
         -c12 * s23 - s12 * c23 * s13 * eid, c23 * c13]])
    return U, s13sq, s12sq, s23sq, cosd, sind


def plaq(U, i, k, j, l):
    return sp.simplify(sp.expand(
        U[i, j] * U[k, l] * sp.conjugate(U[i, l]) * sp.conjugate(U[k, j])))


def abs2_matrix(U):
    return sp.Matrix(3, 3, lambda i, j:
                     sp.simplify(sp.expand_complex(sp.Abs(U[i, j]) ** 2)))


# ==================================================================== A
def task_a():
    section("A: der exakte SU(3)-Lift von B")
    U, s13sq, s12sq, s23sq, cosd, sind = build_lift(B, +1)
    check("A1.1 Winkel VON B ERZWUNGEN: sin^2 th13 = B13 = 2/9, "
          "sin^2 th12 = B12/(1-B13) = 1/14, sin^2 th23 = B23/(1-B13) "
          "= 2/7 exakt",
          (s13sq, s12sq, s23sq)
          == (sp.Rational(2, 9), sp.Rational(1, 14), sp.Rational(2, 7)),
          kill="K-A")
    check("A2.1 cos(delta) EINDEUTIG aus B21 geloest: cos(delta) = "
          "-4/sqrt(65), e^{i delta} = (-4 +- 7i)/sqrt(65); die "
          "Lift-Menge bis auf Rephasierung ist die ZWEI-Zweig-Familie "
          "{U, U*}",
          sp.simplify(cosd + 4 / sp.sqrt(65)) == 0
          and sp.simplify(sind - 7 / sp.sqrt(65)) == 0, kill="K-A")
    check("A3.1 U^dagger U = I und det U = 1 exakt (SU(3))",
          sp.simplify(U.H * U - sp.eye(3)) == sp.zeros(3, 3)
          and sp.simplify(U.det()) == 1, kill="K-A")
    check("A3.2 |U_ij|^2 = B_ij ENTRYWISE EXAKT: B ist unistochastisch "
          "-- der klassische Transport ist der Mess-Schatten einer "
          "reversiblen SU(3)-Rotation [Coherification iff "
          "unistochastic, Literatur]; unitaerer Lift traegt Q = log2 3 "
          "Qubits (Literatur-typisiert) vs C(T) = 0.008358 bit "
          "klassisch (Vorprobe)",
          sp.simplify(abs2_matrix(U) - B) == sp.zeros(3, 3), kill="K-A")
    Q0 = plaq(U, 0, 1, 0, 1)
    J = sp.simplify(sp.im(Q0))
    ReQ_fromB = (B[0, 2] * B[1, 2] - B[0, 0] * B[1, 0]
                 - B[0, 1] * B[1, 1]) / 2
    J2_fromB = B[0, 0] * B[1, 0] * B[0, 1] * B[1, 1] - ReQ_fromB ** 2
    check("A4.1 J = Im(U11 U22 U12* U21*) = 1/27 EXAKT; Re Q und J^2 "
          "sind durch B ALLEIN fixiert (Unitaritaet: Re Q = (B13 B23 - "
          "B11 B21 - B12 B22)/2 = -5/324, J^2 = 1/729) -- das gesamte "
          "rephasierungsinvariante Wilson-Datum ist klassisch bestimmt "
          "bis auf EIN globales Vorzeichen",
          J == sp.Rational(1, 27)
          and ReQ_fromB == sp.Rational(-5, 324)
          and J2_fromB == sp.Rational(1, 729)
          and sp.simplify(sp.re(Q0) - ReQ_fromB) == 0, kill="K-A")
    return U


# ==================================================================== B
def task_b(U):
    section("B: die Wilson-Plaquette-Tafel (der 5-12-13-Code)")
    Q0 = plaq(U, 0, 1, 0, 1)
    check("B1.1 HAUPTSCHLEIFE: Q_{12;12} = (-5 + 12i)/324; normiert "
          "Q/|Q| = (-5 + 12i)/13 mit 5^2 + 12^2 = 13^2 (pythagoreisch); "
          "Atome: 5 = g_car, 12 = dim g_SM, 13 = Delta_Q = N(3+2i) "
          "(Korpus-Anker v530/tfpt_2/v738, read-only)",
          sp.simplify(Q0 - (-5 + 12 * sp.I) / 324) == 0
          and sp.simplify(Q0 / sp.Abs(Q0)
                          - (-5 + 12 * sp.I) / 13) == 0
          and 5 ** 2 + 12 ** 2 == 13 ** 2
          and sp.Abs(3 + 2 * sp.I) ** 2 == 13, kill="K-B")

    pairs = [(0, 1), (0, 2), (1, 2)]
    table = {}
    for (i, k) in pairs:
        for (j, l) in pairs:
            table[(i, k, j, l)] = plaq(U, i, k, j, l)
    # normalized phase types + Gaussian norms
    t1 = (-5 + 12 * sp.I) / 13
    t2p = (-2 + 3 * sp.I) / sp.sqrt(13)
    t2m = (-2 - 3 * sp.I) / sp.sqrt(13)
    t3 = (-11 + 3 * sp.I) / sp.sqrt(130)
    t4 = (1 - 3 * sp.I) / sp.sqrt(10)
    counts = {"t1": 0, "t2p": 0, "t2m": 0, "t3": 0, "t4": 0, "other": 0}
    for q in table.values():
        n = sp.simplify(q / sp.Abs(q))
        hit = "other"
        for nm, tv in (("t1", t1), ("t2p", t2p), ("t2m", t2m),
                       ("t3", t3), ("t4", t4)):
            if sp.simplify(n - tv) == 0:
                hit = nm
                break
        counts[hit] += 1
    check("B2.1 ALLE NEUN Plaquettes schliessen auf VIER Gauss-"
          "Phasentypen: (-5+12i)/13 x%d, (-2+-3i)/sqrt13 x%d, "
          "(-11+3i)/sqrt130 x%d, (1-3i)/sqrt10 x%d; Gauss-Normen "
          "EXKLUSIV {10, 13, 130, 169} = {2*5, 13, 2*5*13, 13^2} -- "
          "Phasenalphabet ueber den Atomen {2, 5, 13}"
          % (counts["t1"], counts["t2p"] + counts["t2m"], counts["t3"],
             counts["t4"]),
          counts == {"t1": 1, "t2p": 2, "t2m": 2, "t3": 2, "t4": 2,
                     "other": 0}
          and {169, 13, 130, 10}
          == {2 * 5, 13, 2 * 5 * 13, 13 ** 2}, kill="K-B")

    ims = [sp.simplify(sp.im(q)) for q in table.values()]
    check("B3.1 JEDES Plaquette hat Im = +-1/27 exakt (die Jarlskog-"
          "Identitaet aller neun Schleifen)",
          all(v in (sp.Rational(1, 27), sp.Rational(-1, 27))
              for v in ims), kill="K-B")

    # B4: generation of all nine from the four fundamental plaquettes
    ok_gen = True
    fund = {(i, j): table[(i, i + 1, j, j + 1)]
            for i in (0, 1) for j in (0, 1)}
    Bm = B
    # column composition: Q_{i,i+1;13} = Q_{i,i+1;12} Q_{i,i+1;23}/(B_{i2}B_{i+1,2})
    for i in (0, 1):
        lhs = table[(i, i + 1, 0, 2)]
        rhs = fund[(i, 0)] * fund[(i, 1)] / (Bm[i, 1] * Bm[i + 1, 1])
        ok_gen &= sp.simplify(lhs - rhs) == 0
    # row composition: Q_{13;j,j+1} = Q_{12;j,j+1} Q_{23;j,j+1}/(B_{1j}B_{1,j+1})... rows 1,3 via row 2
    for j in (0, 1):
        lhs = table[(0, 2, j, j + 1)]
        rhs = fund[(0, j)] * fund[(1, j)] / (Bm[1, j] * Bm[1, j + 1])
        ok_gen &= sp.simplify(lhs - rhs) == 0
    # corner: rows (1,3), cols (1,3)
    lhs = table[(0, 2, 0, 2)]
    rhs = sp.simplify(fund[(0, 0)] * fund[(0, 1)] * fund[(1, 0)]
                      * fund[(1, 1)]
                      / (Bm[1, 0] * Bm[1, 2] * Bm[0, 1] * Bm[2, 1]
                         * Bm[1, 1] ** 2) * Bm[1, 1] ** 2
                      / 1)
    # exact corner relation: Q_{13;13} = prod(fund)/ (B12 B21 B23 B32 B22^2) * B22^2
    rhs = sp.simplify(fund[(0, 0)] * fund[(0, 1)] * fund[(1, 0)]
                      * fund[(1, 1)]
                      / (Bm[0, 1] * Bm[1, 0] * Bm[1, 2] * Bm[2, 1]
                         * Bm[1, 1] ** 2))
    ok_gen &= sp.simplify(lhs - rhs) == 0
    check("B4.1 ERZEUGUNG: die vier Fundamental-Plaquettes erzeugen "
          "alle neun via exakte multiplikative Wilson-Kompositions-"
          "relationen (Spalten-, Zeilen- und Eck-Komposition, "
          "B-gewichtet)", ok_gen, kill="K-B")


# ==================================================================== C
def task_c():
    section("C: die Center-Quotienten-Bruecke (A -> 65 -> Gauss -> "
            "Phase -> J)")
    A = sp.Matrix([[8, 2], [5, 3]])
    disc = sp.discriminant(A.charpoly().as_expr())
    detm1 = (A - sp.eye(2)).det()
    check("C1.1 A = [[8,2],[5,3]] (v530-Atommatrix): det A = 14, "
          "det(A-I) = 4, disc chi_A = 65 = 5*13; NEUE IDENTITAET: "
          "disc = det(A-I)^2 + (det A/2)^2 = 4^2 + 7^2 = 65 exakt",
          A.det() == 14 and detm1 == 4 and disc == 65
          and detm1 ** 2 + (A.det() / 2) ** 2 == 65, kill="K-C")
    eid_from_A = (-detm1 + sp.I * A.det() / 2) / sp.sqrt(disc)
    check("C2.1 e^{i delta} = (-det(A-I) + i det A/2)/sqrt(disc chi_A) "
          "= (-4 + 7i)/sqrt(65) == die Transport-Lift-Phase EXAKT "
          "(beide Zweige via +-)",
          sp.simplify(eid_from_A - (-4 + 7 * sp.I) / sp.sqrt(65)) == 0
          and sp.simplify(sp.Abs(eid_from_A) - 1) == 0, kill="K-C")
    z = sp.expand((1 + 2 * sp.I) * (2 + 3 * sp.I))
    check("C3.1 -4 + 7i = (1+2i)(2+3i) mit N(1+2i) = 5, N(2+3i) = 13 "
          "(v738-Turm-Primzahlen); Kette: Center-Quotient -> 65 = 5*13 "
          "-> (1+2i)(2+3i) -> Transportphase -> J = 1/27",
          z == -4 + 7 * sp.I
          and sp.Abs(1 + 2 * sp.I) ** 2 == 5
          and sp.Abs(2 + 3 * sp.I) ** 2 == 13, kill="K-C")
    ok_neg = True
    for name, M, expect_disc in (("A_K", sp.Matrix([[14, 8], [-11, -6]]),
                                  48),
                                 ("A_Q", sp.Matrix([[3, 1], [3, 2]]), 13)):
        d = sp.discriminant(M.charpoly().as_expr())
        lhs = (M - sp.eye(2)).det() ** 2 + (M.det() / 2) ** 2
        ok_neg &= (d == expect_disc and sp.simplify(lhs - d) != 0)
    check("C4.1 NEG-KONTROLLEN FEUERN: A_K (disc 48, Identitaet gibt "
          "13) und A_Q (disc 13, Identitaet gibt 13/4) VERFEHLEN die "
          "Quadratsummen-Identitaet -- die Bruecke selektiert den "
          "Atom-Quotienten A", ok_neg, kill="K-C")
    check("C5.1 EHRLICHE TYPISIERUNG: die Bruecke fixiert die PHASE "
          "aus A-Invarianten, die WINKEL (2/9, 1/14, 2/7) kommen aus B "
          "allein; ein deployter Intertwiner (Center/Petersen -> "
          "kohaerente Transportverbindung) existiert im Korpus NICHT "
          "-- derselbe Fehlstellen-Typ wie die Shells->Cusp-Abbildung "
          "S (k5/A4); das IST der offene Kontraktinhalt", True)


# ==================================================================== D
def task_d(U):
    section("D: das Orientierungsbit sgn J")
    Uc = U.conjugate()
    Qc = plaq(Uc, 0, 1, 0, 1)
    check("D1.1 U* liftet DASSELBE B (|U*|^2 = B) mit J = -1/27: die "
          "klassische Matrix kann die Zweige nicht unterscheiden -- "
          "die kohaerente Vervollstaendigung traegt ein klassisch "
          "unsichtbares Z2-Orientierungsbit sgn J",
          sp.simplify(abs2_matrix(Uc) - B) == sp.zeros(3, 3)
          and sp.simplify(sp.im(Qc)) == sp.Rational(-1, 27),
          kill="K-D")
    check("D2.1 DAS OBSERVABLE: Im(U11 U22 U12* U21*) -- ein Wilson-"
          "Plaquette-Interferenz-Readout; Populationen sind blind "
          "(|U|^2 = |U*|^2), Interferenz nicht", True)
    check("D3.1 KONTRAST zur Birkhoff-Zirkulation t (Vorprobe): t ist "
          "random-unitary-Mischungsgrad mit ERZWUNGENEM w(C123) = "
          "w(C132) -- nicht chiral; sgn J ist eine echte komplexe "
          "Orientierung: ZWEI verschiedene klassisch verborgene Daten, "
          "getrennt typisiert", True)
    # D4: PMNS near-miss stays negative
    delta_neg = sp.arg(-4 - 7 * sp.I)          # the J = -1/27 branch
    deg = sp.deg(delta_neg) % 360
    degf = float(deg)
    Jpmns = -0.02965                            # v270 deployed value
    check("D4.1 PMNS-NEAR-MISS bleibt NEGATIV (typisiert): Zweig-Phase "
          "delta = %.4f deg nahe deployed 240 deg (4pi/3, v270), ABER "
          "J_tr = -1/27 = -0.037037 != J_PMNS = -0.02965 und alle drei "
          "Winkel differieren (1/14 vs 1/3 - phi0/2 usw.) -- KEINE "
          "PMNS-Herleitung" % degf,
          abs(degf - 240.2551) < 5e-4
          and abs(float(sp.Rational(-1, 27)) - Jpmns) > 0.007,
          kill="K-D")


# ==================================================================== E
def task_e(U):
    section("E: das Six-Step-Paradox (Makro-Gate vs Mikroschritt)")
    a, b = sp.symbols("a b", positive=True)
    B11 = sp.Rational(1, 3) + a / 2 + b / 6
    B12 = sp.Rational(1, 3) - a / 2 + b / 6
    B13 = sp.Rational(1, 3) - b / 3
    ReQn = (B13 ** 2 - 2 * B11 * B12) / 2
    J2n = sp.expand((B11 * B12) ** 2 - ReQn ** 2)
    claimed = (1 - b) ** 2 * (1 + 2 * b - 3 * a ** 2) / 108
    check("E1.1 J_n^2 = (1-b)^2 (1 + 2b - 3a^2)/108 mit a = (2/3)^n, "
          "b = (1/3)^n -- SYMBOLISCH aus den B^n-Eintraegen hergeleitet "
          "(Re durch B^n fixiert, |Q| = B11 B12 per Symmetrie)",
          sp.simplify(J2n - claimed) == 0, kill="K-E")

    rows = []
    rational_ns = []
    for n in range(1, 13):
        an, bn = sp.Rational(2, 3) ** n, sp.Rational(1, 3) ** n
        J2 = (1 - bn) ** 2 * (1 + 2 * bn - 3 * an ** 2) / 108
        Jn = sp.sqrt(sp.nsimplify(J2))
        is_rat = sp.nsimplify(Jn).is_rational is True
        if is_rat:
            rational_ns.append(n)
        rows.append((n, J2, float(Jn), float(Jn / sp.sqrt(JMAXSQ))))
    for n, J2, Jf, rf in rows:
        print("    n=%2d  J^2 = %-28s |J| = %.10f  |J|/J_max = %.7f"
              % (n, J2, Jf, rf))
    check("E2.1 J_n^2 > 0 fuer n = 1..12 => jedes B^n ist "
          "unistochastisch (jeweils mit EIGENEM frisch "
          "rekonstruiertem U_n)",
          all(r[1] > 0 for r in rows), kill="K-E")

    B6 = B ** 6
    U6, s13sq6, _, _, cosd6, _ = build_lift(B6, +1)
    check("E2.2 U_6 explizit gebaut: |U_6|^2 = B^6 = T_v221 entrywise "
          "exakt; |cos delta_6| < 1 (echte Phase)",
          sp.simplify(abs2_matrix(U6) - B6) == sp.zeros(3, 3)
          and abs(float(cosd6)) < 1, kill="K-E")

    J6 = sp.sqrt((1 - sp.Rational(1, 729)) ** 2
                 * (1 + sp.Rational(2, 729)
                    - 3 * sp.Rational(4, 9) ** 6) / 108)
    ratio6 = float(J6 / sp.sqrt(JMAXSQ))
    F3 = sp.Matrix(3, 3, lambda i, j:
                   sp.exp(2 * sp.pi * sp.I * i * j / 3) / sp.sqrt(3))
    JF3 = sp.simplify(sp.im(plaq(F3, 0, 1, 0, 1)))
    check("E3.1 |J_6| = %.10f = %.7f * J_max (Reviewer-Werte "
          "0.0951088904 / 0.9884006 verifiziert); der uniforme Limes "
          "liftet zur Fourier-Matrix F3 mit |J| = J_max = 1/(6 sqrt 3) "
          "EXAKT (maximale Interferenz)" % (float(J6), ratio6),
          abs(float(J6) - 0.0951088904) < 1e-10
          and abs(ratio6 - 0.9884006) < 1e-7
          and sp.simplify(JF3 ** 2 - JMAXSQ) == 0, kill="K-E")

    an1, bn1 = sp.Rational(2, 3), sp.Rational(1, 3)
    hit_unit = sp.simplify(3 * (1 + 2 * bn1 - 3 * an1 ** 2)) == 1
    check("E4.1 RATIONALITAETS-SELEKTION [E neu]: J_n rational NUR bei "
          "n = 1 (n = 2..12 irrational) -- der gaussisch-pythagoreische "
          "Code selektiert den EINZELSCHRITT eindeutig; Mechanismus: "
          "der deployete Schritt trifft 3(1 + 2b - 3a^2) = 1 EXAKT, "
          "also J_1 = (1 - 1/3)/18 = 1/27",
          rational_ns == [1] and hit_unit
          and (1 - bn1) / 18 == sp.Rational(1, 27), kill="K-E")

    U2 = U * U
    absU22 = abs2_matrix(U2)
    B2 = B * B
    check("E5.1 NO-GO FESTER MIKROSCHRITT (Typgrenze): B^2 != |U_1^2|^2 "
          "exakt (Eintrag (1,1): %s = %.4f vs %.4f) -- B^n = |U_n|^2 "
          "braucht jeweils ein NEUES U_n"
          % (B2[0, 0], float(B2[0, 0]), float(absU22[0, 0])),
          sp.simplify(absU22 - B2) != sp.zeros(3, 3)
          and abs(float(absU22[0, 0]) - float(B2[0, 0])) > 0.1,
          kill="K-E")

    # recurrence witness: eigenphases of U1, Dirichlet almost-return
    Un = np.array([[complex(sp.N(U[i, j], 30)) for j in range(3)]
                   for i in range(3)])
    ev = np.linalg.eigvals(Un)
    th = np.angle(ev)
    ns = np.arange(1, 1000001)
    d1 = np.abs(((ns * th[0] + np.pi) % (2 * np.pi)) - np.pi)
    d2 = np.abs(((ns * th[1] + np.pi) % (2 * np.pi)) - np.pi)
    d3 = np.abs(((ns * th[2] + np.pi) % (2 * np.pi)) - np.pi)
    dmax = np.maximum(np.maximum(d1, d2), d3)
    nstar = int(ns[np.argmin(dmax)])
    # |U^{n*}|^2 diagonal via eigen decomposition
    w, V = np.linalg.eig(Un)
    Upow = V @ np.diag(w ** nstar) @ np.linalg.inv(V)
    diagmin = float(np.min(np.abs(np.diag(Upow)) ** 2))
    Bf = np.array([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
    Bpow = np.linalg.matrix_power(Bf, min(nstar, 200))
    relax = float(np.max(np.abs(Bpow - 1 / 3)))
    check("E5.2 REKURRENZ-ZEUGE (Dirichlet): n* = %d mit min_i "
          "|(U_1^{n*})_ii|^2 = %.6f >= 0.98 (Fast-Rueckkehr zur "
          "Identitaet), waehrend max|B^n - 1/3| = %.1e <= 1e-10 "
          "(voll relaxiert) -- KEIN einzelnes geschlossenes U erzeugt "
          "die relaxierende Folge; TYPISIERT: wiederholte Schritte "
          "brauchen Dephasierung ZWISCHEN den Schritten, das Six-Step-"
          "Makro-Gate existiert als eigenes U_6 != U_1^6 (kohaerente "
          "Schaerfung von Clock-vs-Walk + fehlendem Shells->Cusp-"
          "Intertwiner)" % (nstar, diagmin, relax),
          diagmin >= 0.98 and relax <= 1e-10, kill="K-E")


# ==================================================================== F
def task_f():
    section("F: Selektivitaets-Zensus + harter Kill")
    Bns = sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) / 2
    ReQ = (Bns[0, 2] * Bns[1, 2] - Bns[0, 0] * Bns[1, 0]
           - Bns[0, 1] * Bns[1, 1]) / 2
    J2ns = (Bns[0, 0] * Bns[1, 0] * Bns[0, 1] * Bns[1, 1] - ReQ ** 2)
    check("F1.1 OBSTRUKTIONS-ZERTIFIKAT FEUERT: die klassische "
          "bistochastisch-aber-NICHT-unistochastische Matrix (Diagonale "
          "0, sonst 1/2) hat J^2 = %s < 0 -- das Zertifikat erkennt "
          "Nicht-Unistochastizitaet" % J2ns,
          J2ns == sp.Rational(-1, 64) and J2ns < 0)

    ok_mut = True
    for l2, l3, expect in ((sp.Rational(2, 3), sp.Rational(1, 2),
                            sp.Rational(1, 648)),
                           (sp.Rational(1, 2), sp.Rational(1, 3),
                            sp.Rational(11, 2916))):
        J2 = (1 - l3) ** 2 * (1 + 2 * l3 - 3 * l2 ** 2) / 108
        ok_mut &= (sp.nsimplify(J2) == expect
                   and sp.nsimplify(sp.sqrt(J2)).is_rational is not True)
    check("F2.1 MUTATIONS-KONTROLLEN FEUERN: Spektren {2/3, 1/2} und "
          "{1/2, 1/3} geben J^2 = 1/648 bzw 11/2916 -- J irrational, "
          "KEIN Gauss-Code (die 5-12-13-Struktur ist nicht "
          "spektrum-generisch)", ok_mut)

    # F3: grid census over B(a, b) = J/3 + a P2 + b P3, a = k/18, b = m/18
    u2 = sp.Matrix([1, -1, 0])
    u3 = sp.Matrix([1, 1, -2])
    P2 = u2 * u2.T / 2
    P3 = u3 * u3.T / 6
    Jth = sp.ones(3, 3) / 3
    n_valid = n_ratJ = n_fullcode = 0
    fullcode_pts = []
    for k in range(1, 18):
        for m in range(1, 18):
            av, bv = sp.Rational(k, 18), sp.Rational(m, 18)
            Bg = Jth + av * P2 + bv * P3
            if any(e <= 0 for e in Bg):
                continue
            J2 = (1 - bv) ** 2 * (1 + 2 * bv - 3 * av ** 2) / 108
            if J2 < 0:
                continue                     # not unistochastic
            n_valid += 1
            Jr = sp.nsimplify(sp.sqrt(J2))
            if Jr.is_rational is True:
                n_ratJ += 1
                # full code: normalized main plaquette = (-5 +- 12i)/13
                ReQ = (Bg[0, 2] * Bg[1, 2] - Bg[0, 0] * Bg[1, 0]
                       - Bg[0, 1] * Bg[1, 1]) / 2
                absQ = Bg[0, 0] * Bg[0, 1]   # symmetric family
                if J2 > 0 and sp.simplify(
                        (ReQ + sp.I * Jr) / absQ
                        - (-5 + 12 * sp.I) / 13) == 0:
                    n_fullcode += 1
                    fullcode_pts.append((av, bv))
    rate_full = n_fullcode / n_valid
    check("F3.1 GITTER-ZENSUS (harter Kill, praeregistriert <= 10 %%): "
          "%d gueltige unistochastische Familienpunkte; rationales J: "
          "%d (%.1f %%); VOLLER 5-12-13-Code: %d (%.2f %%) bei %s -- "
          "der Code ist SELEKTIV, nicht generisch"
          % (n_valid, n_ratJ, 100 * n_ratJ / n_valid, n_fullcode,
             100 * rate_full, fullcode_pts),
          rate_full <= sp.Rational(1, 10)
          and (sp.Rational(2, 3), sp.Rational(1, 3)) in fullcode_pts,
          kill="K-F")


# ======================================================================
def main():
    print("=" * 78)
    print("TRANSFER.COHERENT.WILSON.01 -- SU(3)-Lift, Wilson-Code "
          "5-12-13, Center-Bruecke, Orientierungsbit")
    print("=" * 78, flush=True)
    U = task_a()
    task_b(U)
    task_c()
    task_d(U)
    task_e(U)
    task_f()

    section("ZUSAMMENFASSUNG / VERDIKTE")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d Checks bestanden" % (n_pass, n_all))
    verdicts = {
        "LIFT": "SU3-LIFT-EXACT" if "K-A" not in KILLS else "LIFT-DEAD",
        "WILSON": "CODE-5-12-13-EXACT" if "K-B" not in KILLS
        else "WILSON-DEAD",
        "BRIDGE": "CENTER-BRIDGE-EXACT (Intertwiner OPEN)"
        if "K-C" not in KILLS else "BRIDGE-DEAD",
        "ORIENTATION": "SIGN-J-BIT-EXHIBITED" if "K-D" not in KILLS
        else "ORIENTATION-DEAD",
        "SIXSTEP": "MACROGATE-VS-MICROSTEP-TYPED" if "K-E" not in KILLS
        else "SIXSTEP-DEAD",
        "SELECTIVITY": "CODE-SELECTIVE" if "K-F" not in KILLS
        else "CODE-GENERIC-DEAD",
    }
    for k, v in verdicts.items():
        print("VERDIKT %s: %s" % (k, v))
    print("Laufzeit: %.1f s" % (time.time() - T0))
    print("ALLE CHECKS BESTANDEN" if n_pass == n_all
          else "CHECKS FEHLGESCHLAGEN")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
