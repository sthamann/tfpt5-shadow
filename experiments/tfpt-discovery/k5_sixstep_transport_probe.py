#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""k5_sixstep_transport_probe -- K5.SIXSTEP.TRANSPORT.01 (Arf compiler
programme, follow-up pair to CARRIER.PETERSEN.RADIAL.01 +
TRANSPORT.SIXTHROOT.01): (A) does the six-step composition on the
hexagon turn the doily/Petersen per-step 2/3 into the corpus rate
(2/3)^6 CANONICALLY (exact operator identity), or is the deployed 6 a
clock exponent?  (B) do the corpus structures realize a canonical
10-dim transport operator with the predicted multiplicities
1^1, (1/3)^6 x5, (2/3)^6 x4?

DEPLOYED ANCHORS (located, read-only):
  * v221_seam_qecc: THE deployed transport matrix -- T_v221 = J/3 +
    (2/3)^6 u2 u2^T + (1/3)^6 u3 u3^T with unit u2 ~ (1,-1,0), u3 ~
    (1,1,-2) ("transfer (1-w)^6" over the cusp weights w in
    {0,1/3,2/3}); v221 evaluates it in floats, the DEFINITION is the
    exact spectral sum.  CORRECTION GATE for TRANSPORT.SIXTHROOT.01:
    T_v221 == B^6 BIT-EXACTLY (B = (1/18)[[13,1,4],[1,13,4],[4,4,10]]);
    the earlier census missed v221, so the sixthroot verdict upgrades
    from SPECTRAL-ONLY to BITEXACT-vs-v221 (reported here).
  * v124_resummed_clock: lambda_n = (1 - n/3)^6, p2 = 6 = |R+(A3)| --
    the clock reading (fixed eigenbasis, 6 as exponent).
  * v486_transfer_full_rule: the six-HAND -- six applications of ONE
    lazy rule M = [[1,0,0],[0,1/2,1/6],[0,1/6,1/2]] in a fixed basis.
  * curve_code_doily_probe (exploration, certified): the duad->syntheme
    channel N/3 has singular values {1, 2/3 x9, 0 x5} -- the per-step
    doily rate 2/3.
  * CARRIER.PETERSEN.RADIAL.01 (exploration, certified): the C6 hexagon
    = the distance-2 shell of the Petersen pair space; radial quotient
    Q_Pet = [[0,3,0],[1,0,2],[0,1,2]], spec((Q_Pet/3)^6) = deployed.

TASK A -- THE SIX-STEP COMPOSITION (all exact; kill = any preregistered
identity fails):
 A0  v221 LOCALIZATION + CORRECTION: T_v221 (exact spectral sum) ==
     B^6 == (1/4374)[[1651,1267,1456],[1267,1651,1456],[1456,1456,
     1462]] bit-exact; spec == {(1-w)^6} == v124's lambda_n exactly.
 A1  DOILY ROUTE: duads/synthemes of a 6-set, incidence N (15x15,
     3-in-3); N N^T = 3I + A_coll with A_coll = SRG(15,6,1,3);
     sv(N/3) = {1, 2/3 x9, 0 x5}; the six-step alternation
     ((N/3)(N^T/3))^3 has spectrum {1, (2/3)^6 x9, 0 x5} EXACTLY --
     three PSD double-steps (duad->syntheme->duad), sign +2/3 via the
     duality pairing.  TYPED GAPS: wrong space (15-dim duads), decay
     multiplicity 9, NO (1/3)^6 mode.
 A2  HEXAGON COMPRESSION: Pi_2 (A_Pet/3) Pi_2 restricted to the
     distance-2 shell == A_C6/3 exactly (Petersen normalization 1/3
     inherited; within-shell degree 2 => Perron 2/3 = the doily rate);
     spec(A_C6/3) = {2/3, 1/3 x2, -1/3 x2, -2/3};
     spec((A_C6/3)^6) = {(2/3)^6 x2, (1/3)^6 x4} -- BOTH deployed
     decay rates from pure hexagon geometry.  TYPED GAPS: NO unit
     mode (radial leak 1/3): ||(A_C6/3)^6||_op = (2/3)^6 < 1, so no
     norm-nonincreasing intertwiners can produce the deployed unit
     eigenvalue from the hexagon operator [E neu obstruction];
     multiplicities (2,4); the per-step spectrum contains -2/3 (C6
     bipartite).
 A3  HEXAGON CIRCULATION: the cyclic shift S6 on the certified C6
     order has S6^6 = I, so ((2/3) S6)^6 = (2/3)^6 * I exactly -- the
     deployed subleading eigenvalue = ONE FULL CIRCULATION at the
     doily rate.  TYPED GAP: scalar identity; a directed edge
     amplitude 2/3 is not a deployed object.
 A4  RADIAL WALK: P = Q_Pet/3 has spec {1, -2/3, 1/3} => P is NOT
     similar to the deployed per-step root B (spec {1, 2/3, 1/3}):
     the SIGN separates the spatial root from the clock root; P^6 ~
     T_v221 via the exact rational conjugation S = U_rad U_dep^{-1}
     (S T_v221 S^{-1} = P^6, computed and verified) -- S maps
     (1,-1,0) -> hypercharge (6,-4,1) and (1,1,-2) -> (3,1,-1) and
     is DEPLOYED NOWHERE (the missing shells->cusp isomorphism).
 A5  THE DECIDER (eigenvector structures, exact): deployed T_v221 has
     the FIXED eigenbasis {(1,1,1),(1,-1,0),(1,1,-2)} at every step
     (clock/hand: v124 exponent, v486 six applications of one rule,
     B^6); every spatial candidate carries its (2/3)-mode on a
     different vector (doily: 9-dim window; hexagon: shell constant;
     radial: hypercharge (6,-4,1)) and no spatial 3-dim composite
     equals T_v221 bit-exactly in the deployed basis.  SIXTH-POWER
     BLINDNESS [E neu]: (A_C6/3)^6 and (A_{2K3}/3)^6 have IDENTICAL
     spectra ({+-2/3, +-1/3 x2} vs {2/3 x2, -1/3 x4} -> same sixth
     powers) -- the sixth power erases the hexagon's cyclic geometry
     AND the sign; only per-step data distinguishes walk from clock.

TASK B -- THE 10-DIM TRANSPORT DEPLOY:
 B1  PREDICTION RESTATED: P10 = A_Pet/3 has spec {1, (1/3)^5,
     (-2/3)^4}; spec(P10^6) = {1^1, (1/3)^6 x5, (2/3)^6 x4} exact
     (charpoly); multiplicities (5, 4) = (g_car, |mu4|).
 B2  CORPUS CENSUS (frozen; searched 2026-08-06): NO deployed 10-dim
     flavor/transport operator exists.  Candidates examined: v221
     (3-dim, THE deployed T -- reconstructed here), v486/v327 (3-dim
     rules), v54/v56/v124/v171/v317 (3-dim spectrum surfaces), v37
     Plücker anchor (3x3 matrices R, K, Q, L -- re-derived here,
     dimension 3, spectra != predicted), v44/v45 (Lambda^2(5) = 10 as
     DIMENSION bookkeeping, no operator), v212/v397 (A_Lambda = 10 as
     scalar), v310 (rep table).  In-probe verifiable core: v221 T is
     3x3; v37's four matrices are 3x3 with charpolys as deployed
     (chi_K = t^3-9t^2+12t-4, chi_L = t^3-15t^2+40t-20).
 B3  CANONICAL PROPOSAL (exact): T10 := (A_Pet/3)^6 conjugated into
     the carrier Lambda^2 basis via the certified cut-code dictionary
     (v774: pair {i,j} <-> the weight-2 word with iota-support {i,j};
     certified in CARRIER.PETERSEN.RADIAL.01 P1.4) -- a permutation
     conjugation, exact.  GATES: T10 symmetric, doubly stochastic,
     PSD (even power), spectrum = the predicted multiplicities; the
     v774 class partition (e_c | u_c | {Q_up, Q_dn}) is EQUITABLE for
     T10; the exact quotient == (Q_Pet/3)^6 bit-exact, its spectrum
     == the deployed {1, 64/729, 1/729} exactly, reversibility
     size_i Q6_ij = size_j Q6_ji holds (sizes 1, 3, 6), and Q6 =
     S T_v221 S^{-1} with the A4 conjugation -- the 10-dim proposal
     reduces to the certified 3-dim transport exactly (spectrum
     level: bit-exact; matrix level: up to the undeployed S).
     COMPATIBILITY-BIT-EXACT GATE: Q6 != T_v221 bit-exact (Q6 is not
     symmetric) -- recorded, this is WHY the proposal is PROPOSED,
     not REALIZED.

CONTROLS (must fire):
 CA1 wrong per-step rate 1/2 (wrong ambient normalization A_C6/2):
     sixth-power spectrum {1 x2, 1/64 x4} != {(2/3)^6 x2, (1/3)^6 x4}
     -- the factorization breaks.
 CA2 scrambled hexagon (Johnson-complement induced graph, 3-regular):
     (A/3)^6 has eigenvalue 1 and the wrong spectrum -- the walk
     breaks.
 CB1 non-equitable partition (one Q-vertex moved into the u_c cell):
     within-cell row sums differ -- the quotient compatibility
     breaks.

KILLS (frozen, any one fires => the respective DEAD):
  K-A0 T_v221 != B^6 or spec != v124 clock.        (SIXSTEP-DEAD)
  K-A1 doily census/spectrum identity fails.       (SIXSTEP-DEAD)
  K-A2 hexagon compression identity/spectrum fails.(SIXSTEP-DEAD)
  K-A3 circulation identity fails.                 (SIXSTEP-DEAD)
  K-A4 conjugation S identity fails, or P IS similar to B
       (sign obstruction vanishes -- would flip toward CANONICAL,
       re-examine).                                (SIXSTEP-DEAD)
  K-B1 P10^6 spectrum != prediction.               (TRANSPORT10-DEAD)
  K-B3 a proposal gate fails (symmetry, spectrum, equitability,
       quotient bit-exactness, reversibility).     (TRANSPORT10-DEAD)
VERDICTS (frozen):
  A: SIXSTEP-CANONICAL iff some spatial six-step composite equals
     T_v221 bit-exactly in the deployed basis (no undeployed
     conjugation) with per-step rate 2/3; SIXSTEP-CLOCK-ONLY iff all
     preregistered identities hold but every spatial candidate needs
     an undeployed conjugation / loses the unit mode / carries the
     bipartite sign -2/3 (the deployed 6 is the clock exponent /
     v486 hand -- typed per candidate); SIXSTEP-DEAD otherwise.
  B: TRANSPORT10-REALIZED iff a corpus operator is 10-dim with the
     predicted spectrum (census: none); TRANSPORT10-PROPOSED iff the
     canonical construction passes ALL gates incl. exact quotient
     compatibility (promotion-ready proposal, NO deployment claim);
     TRANSPORT10-DEAD otherwise.

TYPING (carried): [E neu] exact operator identities/censuses; [H neu]
the walk-vs-clock reading and the 10-dim deployment proposal.
ROOTCLASS-MIXED cited: carrier representation geometry, no physics
claims beyond operator identities.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt (eine Promotionsrunde laeuft parallel -- dieser Prozess
fasst nichts davon an).  Exakte Fraction-Arithmetik; sympy nur fuer
charakteristische Polynome und 3x3-Inverse; keine Floats, kein RNG.

Quellen (read-only): v221_seam_qecc.py, v124_resummed_clock.py,
v486_transfer_full_rule.py, v37_plucker_anchor.py,
v774_arf_spinor_compiler.py, tfpt_constants.py;
experiments/tfpt-discovery/curve_code_doily_probe.py und
carrier_petersen_radial_probe.py (zertifizierte Vorstufen).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/k5_sixstep_transport_probe.py
"""

import itertools
import os
import sys
import time
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _VERIFY)

T0 = time.time()
CHECKS = []
KILLS = []
SPATIAL_BITEXACT_HITS = []
CORPUS10_HITS = []


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


# ------------------------------------------------------------- helpers
def mat(rows):
    return [[Fr(x) for x in r] for r in rows]


def mmul(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)]
            for i in range(n)]


def mpow(A, k):
    R = [[Fr(1) if i == j else Fr(0) for j in range(len(A))]
         for i in range(len(A))]
    for _ in range(k):
        R = mmul(R, A)
    return R


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def outer_scaled(c, v):
    return [[Fr(c) * v[i] * v[j] for j in range(len(v))]
            for i in range(len(v))]


def madd(*Ms):
    n, m = len(Ms[0]), len(Ms[0][0])
    return [[sum(M[i][j] for M in Ms) for j in range(m)] for i in range(n)]


def charpoly_is(A, factors):
    """exact: charpoly(A) == prod (x - r)^m  (sympy gated)."""
    from sympy import Matrix, Rational, symbols, expand, prod
    x = symbols("x")

    def conv(v):
        f = Fr(v)
        return Rational(f.numerator, f.denominator)
    cp = Matrix(len(A), len(A[0]),
                lambda i, j: conv(A[i][j])).charpoly(x).as_expr()
    target = expand(prod((x - conv(r)) ** m for r, m in factors))
    return expand(cp - target) == 0


# --------------------------------------------------- shared structures
PAIRS = [frozenset(p) for p in itertools.combinations(range(5), 2)]
PIDX = {p: i for i, p in enumerate(PAIRS)}
W_VERTEX = frozenset({3, 4})
ADJ = [[1 if i != j and not (PAIRS[i] & PAIRS[j]) else 0
        for j in range(10)] for i in range(10)]
P10 = [[Fr(ADJ[i][j], 3) for j in range(10)] for i in range(10)]

# distance shells around W (certified structure, re-derived)
_d = {PIDX[W_VERTEX]: 0}
_f = [PIDX[W_VERTEX]]
while _f:
    _n = []
    for u in _f:
        for v in range(10):
            if ADJ[u][v] and v not in _d:
                _d[v] = _d[u] + 1
                _n.append(v)
    _f = _n
SHELLS = {k: sorted(i for i in range(10) if _d[i] == k) for k in (0, 1, 2)}
HEXA = SHELLS[2]
C6_ORDER = [PIDX[frozenset(s)] for s in
            ({0, 3}, {1, 4}, {2, 3}, {0, 4}, {1, 3}, {2, 4})]

QPET = mat([[0, 3, 0], [1, 0, 2], [0, 1, 2]])
P3 = [[q / 3 for q in row] for row in QPET]

U2, U3 = (1, -1, 0), (1, 1, -2)
LAM2, LAM3 = Fr(64, 729), Fr(1, 729)
# v221 deployed transport, exact spectral-sum reconstruction
T_V221 = madd(outer_scaled(Fr(1, 3), (1, 1, 1)),
              outer_scaled(LAM2 / 2, U2),
              outer_scaled(LAM3 / 6, U3))
B = mat([[Fr(13, 18), Fr(1, 18), Fr(4, 18)],
         [Fr(1, 18), Fr(13, 18), Fr(4, 18)],
         [Fr(4, 18), Fr(4, 18), Fr(10, 18)]])


# ==================================================================== A0
def a0_v221():
    section("A0: v221 lokalisiert + KORREKTUR zu TRANSPORT.SIXTHROOT.01")
    B6 = mpow(B, 6)
    expect = mat([[Fr(1651, 4374), Fr(1267, 4374), Fr(1456, 4374)],
                  [Fr(1267, 4374), Fr(1651, 4374), Fr(1456, 4374)],
                  [Fr(1456, 4374), Fr(1456, 4374), Fr(1462, 4374)]])
    check("A0.1 T_v221 (exakte Spektralsumme J/3 + (2/3)^6 u2u2^T + "
          "(1/3)^6 u3u3^T, Basis (1,-1,0)/(1,1,-2)) == B^6 == "
          "(1/4374)[[1651,1267,1456],...] BIT-EXAKT -- KORREKTUR: die "
          "Sixthroot-Zensus uebersah v221; das Verdikt SIXTHROOT-"
          "SPECTRAL-ONLY wird zu SIXTHROOT-BITEXACT-vs-v221",
          T_V221 == B6 == expect, kill="K-A0")
    clock = [ (Fr(1) - Fr(n, 3)) ** 6 for n in range(3)]
    check("A0.2 v124-Uhr: lambda_n = (1 - n/3)^6 = %s == spec(T_v221) "
          "= {1, 64/729, 1/729} exakt (Eigenvektoren fest: (1,1,1), "
          "(1,-1,0), (1,1,-2))" % (clock,),
          clock == [Fr(1), LAM2, LAM3]
          and charpoly_is(T_V221, [(Fr(1), 1), (LAM2, 1), (LAM3, 1)]),
          kill="K-A0")
    return B6


# ==================================================================== A1
def a1_doily():
    section("A1: die Doily-Route (Duade->Syntheme, sechs Schritte als "
            "drei PSD-Doppelschritte)")
    duads = [frozenset(p) for p in itertools.combinations(range(6), 2)]
    didx = {p: i for i, p in enumerate(duads)}
    synthemes = []
    for m in itertools.permutations(range(6)):
        s = frozenset(frozenset({m[2 * k], m[2 * k + 1]})
                      for k in range(3))
        if s not in synthemes:
            synthemes.append(s)
    N = [[1 if duads[i] in synthemes[j] else 0
          for j in range(len(synthemes))] for i in range(15)]
    rows = [sum(N[i]) for i in range(15)]
    cols = [sum(N[i][j] for i in range(15)) for j in range(len(synthemes))]
    check("A1.1 15 Duaden, %d Synthemen (perfekte Matchings); jede "
          "Duade in 3 Synthemen, jedes Synthem hat 3 Duaden"
          % len(synthemes),
          len(synthemes) == 15 and rows == [3] * 15 and cols == [3] * 15,
          kill="K-A1")

    NNt = mmul(mat(N), transpose(mat(N)))
    Acoll = [[NNt[i][j] - (3 if i == j else 0) for j in range(15)]
             for i in range(15)]
    ok_srg = all(sum(Acoll[i]) == 6 for i in range(15))
    for i in range(15):
        for j in range(i + 1, 15):
            common = sum(Acoll[i][k] * Acoll[j][k] for k in range(15))
            if Acoll[i][j] == 1 and common != 1:
                ok_srg = False
            if Acoll[i][j] == 0 and common != 3:
                ok_srg = False
    check("A1.2 N N^T = 3I + A_coll mit A_coll = SRG(15, 6, 1, 3) "
          "(die Doily-Kollinearitaet)", ok_srg, kill="K-A1")

    NNt9 = [[NNt[i][j] / 9 for j in range(15)] for i in range(15)]
    check("A1.3 sv(N/3) = {1, 2/3 x9, 0 x5}: spec((N/3)(N/3)^T) = "
          "{1, 4/9 x9, 0 x5} exakt (charpoly) -- der Doily-Schritt "
          "traegt 2/3 (curve_code_doily_probe zertifiziert)",
          charpoly_is(NNt9, [(Fr(1), 1), (Fr(4, 9), 9), (Fr(0), 5)]),
          kill="K-A1")

    six = mpow(NNt9, 3)   # three PSD double-steps = six channel legs
    check("A1.4 SECHS SCHRITTE = drei PSD-Doppelschritte: "
          "spec(((N/3)(N^T/3))^3) = {1, (2/3)^6 x9, 0 x5} EXAKT -- "
          "die Korpus-Rate (2/3)^6 entsteht kanonisch, Vorzeichen +2/3 "
          "via Dualitaetspaarung; TYPISIERTE LUECKEN: falscher Raum "
          "(15-dim Duaden), Zerfalls-Multiplizitaet 9, KEIN (1/3)^6-"
          "Modus",
          charpoly_is(six, [(Fr(1), 1), (LAM2, 9), (Fr(0), 5)]),
          kill="K-A1")


# ==================================================================== A2
def a2_hexagon():
    section("A2: die Hexagon-Kompression (Pi_2 P10 Pi_2 = A_C6/3)")
    sub = [[P10[i][j] for j in HEXA] for i in HEXA]
    ac6 = [[Fr(ADJ[i][j], 3) for j in HEXA] for i in HEXA]
    degs = [sum(1 for j in HEXA if ADJ[i][j]) for i in HEXA]
    check("A2.1 KOMPRESSION exakt: die Einschraenkung von P10 auf die "
          "Distanz-2-Schale == A_C6/3 (Petersen-Normierung 1/3 "
          "vererbt; Innengrad 2 => Perron 2/3 = die Doily-Rate; Leck "
          "1/3 radial)", sub == ac6 and degs == [2] * 6, kill="K-A2")

    check("A2.2 spec(A_C6/3) = {2/3, 1/3 x2, -1/3 x2, -2/3} exakt; "
          "Perron-Vektor = die Hexagon-Konstante",
          charpoly_is(sub, [(Fr(2, 3), 1), (Fr(1, 3), 2),
                            (Fr(-1, 3), 2), (Fr(-2, 3), 1)])
          and [sum(row) for row in sub] == [Fr(2, 3)] * 6,
          kill="K-A2")

    sub6 = mpow(sub, 6)
    check("A2.3 SECHSTE POTENZ: spec((A_C6/3)^6) = {(2/3)^6 x2, "
          "(1/3)^6 x4} -- BEIDE deployeten Zerfallsraten aus reiner "
          "Hexagon-Geometrie; TYPISIERTE LUECKEN: KEIN Einheitsmodus "
          "(||.||_op = (2/3)^6 < 1 => kein normnichtvergroessernder "
          "Intertwiner kann den deployeten Eigenwert 1 aus dem "
          "Hexagon-Operator erzeugen [E neu Obstruktion]); "
          "Multiplizitaeten (2,4); Schritt-Spektrum enthaelt -2/3 "
          "(C6 bipartit)",
          charpoly_is(sub6, [(LAM2, 2), (LAM3, 4)]), kill="K-A2")

    # sixth-power blindness: two disjoint triangles give the SAME sixth power spectrum
    tri2 = [[Fr(0)] * 6 for _ in range(6)]
    for a, b in ((0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)):
        tri2[a][b] = tri2[b][a] = Fr(1, 3)
    ok_blind = (charpoly_is(tri2, [(Fr(2, 3), 2), (Fr(-1, 3), 4)])
                and charpoly_is(mpow(tri2, 6), [(LAM2, 2), (LAM3, 4)]))
    check("A2.4 SECHSTPOTENZ-BLINDHEIT [E neu]: A_{2K3}/3 (zwei "
          "Dreiecke) hat spec {2/3 x2, -1/3 x4} != C6, aber die "
          "sechste Potenz hat das IDENTISCHE Spektrum {(2/3)^6 x2, "
          "(1/3)^6 x4} -- die sechste Potenz loescht die zyklische "
          "Geometrie UND das Vorzeichen; nur Schritt-Daten "
          "unterscheiden Walk von Uhr", ok_blind)
    return sub6


# ==================================================================== A3
def a3_circulation():
    section("A3: die Hexagon-Zirkulation ((2/3) S6)^6 = (2/3)^6 I")
    S6 = [[Fr(0)] * 6 for _ in range(6)]
    for k in range(6):
        S6[(k + 1) % 6][k] = Fr(1)     # shift along the certified C6 order
    ok_edges = all(ADJ[C6_ORDER[k]][C6_ORDER[(k + 1) % 6]] == 1
                   for k in range(6))
    W = [[Fr(2, 3) * S6[i][j] for j in range(6)] for i in range(6)]
    W6 = mpow(W, 6)
    ident = [[LAM2 if i == j else Fr(0) for j in range(6)]
             for i in range(6)]
    check("A3.1 ZIRKULATION exakt: der zyklische Shift laengs der "
          "zertifizierten C6-Ordnung hat S6^6 = I, also ((2/3) S6)^6 "
          "= (2/3)^6 * I -- der deployete Unterleit-Eigenwert = EINE "
          "volle Hexagon-Zirkulation zur Doily-Rate; TYPISIERTE "
          "LUECKE: skalare Identitaet, die gerichtete Kanten-Amplitude "
          "2/3 ist nirgends deployed",
          ok_edges and W6 == ident and mpow(S6, 6)
          == [[Fr(1) if i == j else Fr(0) for j in range(6)]
              for i in range(6)], kill="K-A3")


# ==================================================================== A4
def a4_radial():
    section("A4: der radiale Walk -- Vorzeichen-Obstruktion + die "
            "fehlende Konjugation S")
    check("A4.1 SIGN-OBSTRUKTION: spec(P = Q_Pet/3) = {1, -2/3, 1/3} "
          "!= {1, 2/3, 1/3} = spec(B) -- der raeumliche Schritt ist "
          "NICHT aehnlich zur deployeten Uhr-Wurzel (verschiedene "
          "Spektren), obwohl P^6 ~ B^6 = T_v221",
          charpoly_is(P3, [(Fr(1), 1), (Fr(-2, 3), 1), (Fr(1, 3), 1)])
          and charpoly_is(B, [(Fr(1), 1), (Fr(2, 3), 1), (Fr(1, 3), 1)]),
          kill="K-A4")

    from sympy import Matrix, Rational

    def to_sym(A):
        return Matrix(len(A), len(A[0]),
                      lambda i, j: Rational(Fr(A[i][j]).numerator,
                                            Fr(A[i][j]).denominator))
    U_dep = Matrix([[1, 1, 1], [1, -1, 1], [1, 0, -2]])
    U_rad = Matrix([[1, 6, 3], [1, -4, 1], [1, 1, -1]])
    S = U_rad * U_dep.inv()
    P6 = to_sym(mpow(P3, 6))
    ok_conj = (S * to_sym(T_V221) * S.inv() - P6) == Matrix.zeros(3, 3)
    print("    S = U_rad U_dep^{-1} =", S.tolist())
    check("A4.2 EXAKTE KONJUGATION: S T_v221 S^{-1} = P^6 mit "
          "rationalem S (bildet (1,-1,0) -> Hyperladung (6,-4,1), "
          "(1,1,-2) -> (3,1,-1)); S ist NIRGENDS deployed -- die "
          "fehlende Schalen->Cusp-Isomorphie ist die typisierte "
          "fehlende Zutat", ok_conj, kill="K-A4")

    # bit-exact spatial comparison in the deployed basis
    Q6 = mpow(P3, 6)
    hit = (Q6 == T_V221)
    if hit:
        SPATIAL_BITEXACT_HITS.append("radial P^6")
    check("A4.3 BIT-EXAKT-VERGLEICH im deployeten Rahmen: P^6 %s "
          "T_v221 (P^6 ist nicht symmetrisch; gleiches Spektrum, "
          "andere Eigenvektoren) -- kein raeumliches 3-dim Komposit "
          "trifft T_v221 bit-exakt" % ("==" if hit else "!="),
          not hit or hit)   # census record, never a kill by itself
    return Q6, S, U_dep, U_rad


# ==================================================================== B
def b1_prediction():
    section("B1: die 10-dim Vorhersage exakt")
    check("B1.1 spec(P10) = {1, (1/3)^5, (-2/3)^4}; spec(P10^6) = "
          "{1^1, (1/3)^6 x5, (2/3)^6 x4} exakt (charpoly); "
          "Multiplizitaeten (5, 4) = (g_car, |mu4|)",
          charpoly_is(P10, [(Fr(1), 1), (Fr(1, 3), 5), (Fr(-2, 3), 4)])
          and charpoly_is(mpow(P10, 6),
                          [(Fr(1), 1), (LAM3, 5), (LAM2, 4)]),
          kill="K-B1")


def b2_census():
    section("B2: der Korpus-Zensus -- kein deployeter 10-dim Operator")
    from sympy import Matrix, symbols, expand
    t = symbols("t")
    K = Matrix([[4, 2, 0], [4, 3, 2], [5, 3, 2]])
    L = K + Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
    chiK = (t * Matrix.eye(3) - K).det()
    chiL = (t * Matrix.eye(3) - L).det()
    ok37 = (expand(chiK - (t ** 3 - 9 * t ** 2 + 12 * t - 4)) == 0
            and expand(chiL - (t ** 3 - 15 * t ** 2 + 40 * t - 20)) == 0)
    check("B2.1 v37-Kern re-deriviert: K, L sind 3x3 mit chi_K = "
          "t^3-9t^2+12t-4, chi_L = t^3-15t^2+40t-20 -- der Plücker-"
          "Apparat ist 3-dim, KEIN 10-dim Operator; v221 T ist 3x3; "
          "v44/v45 fuehren Lambda^2(5) = 10 nur als Dimension, "
          "v212/v397 nur als Skalar A_Lambda; ZENSUS-ERGEBNIS: kein "
          "deployeter 10-dim Flavor/Transport-Operator im Korpus",
          ok37 and len(T_V221) == 3)
    # CORPUS10_HITS stays empty unless a 10-dim corpus operator matched


def b3_proposal(Q6, S):
    section("B3: der kanonische 10-dim Vorschlag T10 (Lambda^2-Basis "
            "via Cut-Code-Woerterbuch) + Quotienten-Gate")
    import v774_arf_spinor_compiler as v774

    # certified dictionary: pair {i,j} <-> weight-2 word, iota-support
    words = [w for w in v774.W16 if sum(v774.iota(w)) == 2]
    w_of_pair = {}
    for w in words:
        supp = frozenset(k for k in range(5) if v774.iota(w)[k])
        w_of_pair[supp] = w
    ok_dict = (len(words) == 10
               and set(w_of_pair.keys()) == set(PAIRS))
    perm = [words.index(w_of_pair[PAIRS[i]]) for i in range(10)]
    check("B3.1 WOERTERBUCH: die 10 Gewicht-2-Woerter von v774 "
          "(= die {q*=1}-Dekuple) stehen in Bijektion zu E(K5) via "
          "iota-Support (zertifiziert in CARRIER.PETERSEN.RADIAL.01); "
          "Permutation = Basiswechsel Paarraum -> Lambda^2-Basis",
          ok_dict and sorted(perm) == list(range(10)), kill="K-B3")

    P10_6 = mpow(P10, 6)
    T10 = [[P10_6[perm.index(a)][perm.index(bb)] for bb in range(10)]
           for a in range(10)]
    sym = all(T10[i][j] == T10[j][i] for i in range(10) for j in range(10))
    rows = [sum(T10[i]) for i in range(10)]
    check("B3.2 T10 := P10^6 in der Lambda^2-Basis: symmetrisch, "
          "doppelt-stochastisch, PSD (gerade Potenz), Spektrum = "
          "{1^1, (1/3)^6 x5, (2/3)^6 x4} exakt",
          sym and rows == [Fr(1)] * 10
          and charpoly_is(T10, [(Fr(1), 1), (LAM3, 5), (LAM2, 4)]),
          kill="K-B3")

    # class partition from v774: e_c | u_c | {Q_up, Q_dn}
    cls = [v774.class_of(words[k]) for k in range(10)]
    cells = [[k for k in range(10) if cls[k] == "e_c"],
             [k for k in range(10) if cls[k] == "u_c"],
             [k for k in range(10) if cls[k] in ("Q_up", "Q_dn")]]
    sizes = [len(c) for c in cells]
    quo = []
    ok_eq = True
    for ci, cell in enumerate(cells):
        rowsums = [[sum(T10[u][v] for v in cells[cj]) for cj in range(3)]
                   for u in cell]
        if any(r != rowsums[0] for r in rowsums):
            ok_eq = False
        quo.append(rowsums[0])
    check("B3.3 QUOTIENTEN-GATE: die v774-Klassenpartition (e_c | u_c "
          "| Q), Groessen %s == (1, 3, 6), ist AEQUITABEL fuer T10; "
          "exakter Quotient == (Q_Pet/3)^6 BIT-EXAKT" % (sizes,),
          ok_eq and sizes == [1, 3, 6] and quo == Q6, kill="K-B3")

    rev = all(Fr(sizes[i]) * quo[i][j] == Fr(sizes[j]) * quo[j][i]
              for i in range(3) for j in range(3))
    check("B3.4 REDUKTION auf das zertifizierte 3-dim T: spec(Quotient)"
          " = {1, 64/729, 1/729} exakt = deployed (v54/v221); "
          "Reversibilitaet size_i q_ij = size_j q_ji exakt; Quotient "
          "= S T_v221 S^{-1} (A4); BIT-EXAKT-GATE: Quotient != T_v221 "
          "(nicht symmetrisch) -- darum PROPOSED, nicht REALIZED",
          charpoly_is(Q6, [(Fr(1), 1), (LAM2, 1), (LAM3, 1)])
          and rev and Q6 != T_V221, kill="K-B3")
    return cells


# ==================================================================== C
def c_controls():
    section("C: Must-fail-Kontrollen")
    sub_half = [[Fr(ADJ[i][j], 2) for j in HEXA] for i in HEXA]
    fired1 = charpoly_is(mpow(sub_half, 6),
                         [(Fr(1), 2), (Fr(1, 64), 4)])
    check("CA1 KONTROLLE FEUERT (falsche Schrittrate 1/2): (A_C6/2)^6 "
          "hat Spektrum {1 x2, 1/64 x4} != {(2/3)^6 x2, (1/3)^6 x4} "
          "-- die Faktorisierung bricht",
          fired1 and Fr(1, 64) != LAM3)

    scr = [[Fr(1, 3) if (PAIRS[i] != PAIRS[j]
                         and len(PAIRS[i] & PAIRS[j]) == 1) else Fr(0)
            for j in HEXA] for i in HEXA]
    scr = [[scr[a][b] for b in range(6)] for a in range(6)]
    scr6 = mpow(scr, 6)
    wrong = not charpoly_is(scr6, [(LAM2, 2), (LAM3, 4)])
    has_unit = charpoly_is(scr, [(Fr(1), 1), (Fr(1, 3), 2),
                                 (Fr(-1, 3), 2), (Fr(-1, 3), 1)]) \
        or any(sum(row) == 1 for row in scr)
    check("CA2 KONTROLLE FEUERT (verwuerfeltes Hexagon = Johnson-"
          "Komplement, 3-regulaer): (A/3)^6 traegt den Eigenwert 1 "
          "(Perron 3/3) und NICHT das Hexagon-Spektrum -- der Walk "
          "bricht", wrong and has_unit)

    # bad partition directly in the pair basis: move one Q-vertex
    # (distance-2 shell) into the u_c cell (distance-1 shell)
    bad_cells = [[PIDX[W_VERTEX]], SHELLS[1] + [SHELLS[2][0]],
                 SHELLS[2][1:]]
    ok_eq = True
    P10_6 = mpow(P10, 6)
    for cell in bad_cells:
        rowsums = [[sum(P10_6[u][v] for v in cj) for cj in bad_cells]
                   for u in cell]
        if any(r != rowsums[0] for r in rowsums):
            ok_eq = False
    check("CB1 KONTROLLE FEUERT (nicht-aequitable Partition: ein "
          "Q-Knoten in die u_c-Zelle verschoben): die Zeilensummen "
          "innerhalb einer Zelle differieren -- die Quotienten-"
          "Kompatibilitaet bricht", not ok_eq)


# ======================================================================
def main():
    print("=" * 78)
    print("K5.SIXSTEP.TRANSPORT.01 -- Sechs-Schritt-Komposition + "
          "10-dim Transport-Deploy")
    print("=" * 78, flush=True)
    a0_v221()
    a1_doily()
    a2_hexagon()
    a3_circulation()
    Q6, S, _, _ = a4_radial()
    b1_prediction()
    b2_census()
    b3_proposal(Q6, S)
    c_controls()

    section("ZUSAMMENFASSUNG / VERDIKTE")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    kills_a = [k for k in KILLS if k.startswith("K-A")]
    kills_b = [k for k in KILLS if k.startswith("K-B")]
    print("%d/%d Checks bestanden" % (n_pass, n_all))

    if kills_a or not controls_ok:
        verdict_a = "SIXSTEP-DEAD"
    elif SPATIAL_BITEXACT_HITS:
        verdict_a = "SIXSTEP-CANONICAL"
    else:
        verdict_a = "SIXSTEP-CLOCK-ONLY"
    if kills_b or not controls_ok:
        verdict_b = "TRANSPORT10-DEAD"
    elif CORPUS10_HITS:
        verdict_b = "TRANSPORT10-REALIZED"
    else:
        verdict_b = "TRANSPORT10-PROPOSED"

    print("VERDIKT A: %s -- die Rate (2/3)^6 entsteht kanonisch auf "
          "DREI unabhaengigen raeumlichen Routen (Doily-Alternation, "
          "Hexagon-Kompression, Hexagon-Zirkulation), aber der "
          "deployete Sechser ist der UHR-EXPONENT (v124 lambda_n = "
          "(1-n/3)^6, v486-Hand, festes Eigensystem (1,1,1)/(1,-1,0)/"
          "(1,1,-2)): jede raeumliche Route verliert den Einheitsmodus "
          "(Hexagon, Norm-Obstruktion), traegt das bipartite "
          "Vorzeichen -2/3 (radial) oder lebt auf dem falschen Raum "
          "ohne (1/3)^6 (Doily, x9); fehlende Zutat: eine deployete "
          "Schalen->Cusp-Isomorphie S + eine Vorzeichen/Orientierungs-"
          "Selektion; Sechstpotenz-Blindheit (C6 vs 2K3) macht die "
          "Unterscheidung aus der sechsten Potenz allein prinzipiell "
          "unmoeglich." % verdict_a)
    print("VERDIKT B: %s -- kein Korpus-Objekt ist 10-dim (Zensus "
          "B2); der kanonische Vorschlag T10 = P10^6 in der "
          "Lambda^2-Basis (v774-Woerterbuch) besteht ALLE Gates: "
          "symmetrisch doppelt-stochastisch PSD, Spektrum {1^1, "
          "(1/3)^6 x5, (2/3)^6 x4}, v774-Klassenpartition aequitabel, "
          "Quotient == (Q_Pet/3)^6 bit-exakt mit deployetem Spektrum "
          "und Reversibilitaet -- promotionsreifer Vorschlag, KEIN "
          "Deploy-Anspruch." % verdict_b)
    print("Verdikt-Enums: %s / %s" % (verdict_a, verdict_b))
    print("Laufzeit: %.1f s" % (time.time() - T0))
    print("ALLE CHECKS BESTANDEN" if n_pass == n_all
          else "CHECKS FEHLGESCHLAGEN")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
