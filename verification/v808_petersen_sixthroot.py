#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v808 -- CARRIER.PETERSEN.RADIAL.01 (+ TRANSPORT.SIXTHROOT.01): the K5 edge machine, the Petersen carrier geometry with the radial dynamics whose sixth power IS the deployed transport spectrum, + the bit-exact decider on the PSD sixth root, ONE module from two probes (19/19 + 16/16 checks, ~1 s; discovery probes carrier_petersen_radial_probe.py PETERSEN-RADIAL-EXACT and transport_sixthroot_probe.py SIXTHROOT-SPECTRAL-ONLY, both 2026-08-06).  PART 1, THE K5 EDGE MACHINE (all exact integer/Fraction): X = (-2,-2,-2,3,3) is the UNIQUE primitive traceless block-constant charge for the F|W = 3+2 split (sign pinned by the certified v774 table); E(K5) = 10 pairs carry the charge census {-4: 3, +1: 6, +6: 1} = the SU(5) decuple 3_{-4} + 6_{+1} + 1_{+6}, every pair cross-checked against the certified v774 hypercharge table (classes u_c/Q_up/Q_dn/e_c); under disjointness the pairs form the PETERSEN graph SRG(10,3,0,1) (charpoly (x-3)(x-1)^5(x+2)^4 exact, girth 5, |Aut| = 120 by full backtracking census = the faithful S5); the distance shells around the W vertex are (1, 3, 6) and CHARGE-PURE (+6/-4/+1 = e^c/u^c/Q), and the distance-2 shell induces a C6 -- THE FLAVOR HEXAGON AS GRAPH GEOMETRY [E neu] (explicit cycle verified edge by edge; 6 = |R+(A3)| = the transfer exponent, v124); the shell partition is EQUITABLE with quotient [[0,3,0],[1,0,2],[0,1,2]] whose eigenvector (6,-4,1) -> -2 IS the hypercharge vector, and P = Q_Pet/3 has spec(P^6) = {1, 64/729, 1/729} == the deployed TFPT transport spectrum EXACTLY (v54/v56/v171/v317; v124 lambda_n = (1-n/3)^6; GATE.METRIC.18).  THE PREDICTION [H neu]: the full 10-dim Petersen walk has spec(P10^6) = {1, (1/3)^6 x5, (2/3)^6 x4} -- fast mode multiplicity 5 = g_car, slow hypercharge mode 4 = |mu4| (trace crosscheck 990 = 729 + 5 + 256); NO corpus 10-dim operator exists (T is 3-dim on the cusp space) -- a prediction, not a verification.  PART 2, THE SIXTH ROOT (exact Fractions): B = (1/18)[[13,1,4],[1,13,4],[4,4,10]] -- every entry a compiler number (18 = p4(anchor), 13 = N_fam^2 + |Z2|^2, 4 = |mu4|, 10 = A_Lambda, 1 = N_Phi) -- is the UNIQUE symmetric doubly stochastic PSD sixth root with the frozen corpus-basis eigen-assignment ((1,1,1) -> 1, (1,-1,0) -> 2/3, (1,1,-2) -> 1/3; spectral reconstruction entry-exact; exactly 2 assignments in the corpus basis, a 1-parameter circle without the pin); B^6 carries the deployed spectrum exactly BUT the decider lands SPECTRAL-ONLY: B^6 is GL(3,Q)-conjugate to v486's lazy-walk M^6 (exact rational W and orthogonal O conjugations verified) and to the cusp-diagonal canonical form, yet bit-equal to NEITHER -- the corpus freezes the SPECTRUM, not the basis; the stochastic types differ (doubly vs sub-stochastic with absorbing channel).  Controls fire in both parts (wrong edge 4+1 kills the (1,3,6) structure; Johnson complement kills the hexagon; both matrix perturbations break the spectrum).  Typed carrier representation geometry -- ROOTCLASS-MIXED (v775) cited, no particle semantics.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes carrier_petersen_radial_probe.py (2026-08-06, 19/19, ~0.2 s, PETERSEN-RADIAL-EXACT) + transport_sixthroot_probe.py (2026-08-06, 16/16, ~0.3 s, SIXTHROOT-SPECTRAL-ONLY); both re-run identically at promotion.  Promoted verbatim, part 2 wrapped in a function scope (v789/v795 precedent); the v774/tfpt_constants imports resolve against the verification directory (path swap, v795 precedent); module-level _LAST1/_LAST2 verdict captures inserted (v791 precedent); numbers unchanged; run() encodes both patterns (v757 precedent).

Original carrier_petersen_radial_probe.py docstring (verbatim):
carrier_petersen_radial_probe -- CARRIER.PETERSEN.RADIAL.01 (Arf
compiler programme, follow-up module 1): the K5 edge machine, the
Petersen carrier geometry, and the radial dynamics whose sixth power
is the deployed TFPT transport spectrum.

THEOREM CANDIDATE (preregistered).  The five carrier slots of
S+_{D5} = Lambda^even C^5 split canonically F = {f1,f2,f3} |
W = {w1,w2} (the distinguished edge).  On E(K5) = the 10 pairs (the
SU(5) decuple, = the {q*=1} words of v774), the unique primitive
traceless block-constant charge X = (-2,-2,-2,3,3) induces the charge
decomposition 3_{-4} + 6_{+1} + 1_{+6} (Y = X/6: -2/3, 1/6, 1).
Under disjointness the 10 pairs form the PETERSEN graph KG(5,2); the
distance shells around the W vertex are (1, 3, 6) = exactly the
charge classes (e^c, u^c, Q), and the distance-2 shell is a 6-cycle
-- the flavor hexagon as graph geometry [E neu].  The equitable
radial quotient Q_Pet = [[0,3,0],[1,0,2],[0,1,2]] has eigenpairs
(1,1,1)->3, (6,-4,1)->-2 (the HYPERCHARGE VECTOR, ordered
(e^c, u^c, Q)), (3,1,-1)->1; the radial walk P = Q_Pet/3 has
spec {1, -2/3, 1/3} and spec(P^6) = {1, (2/3)^6, (1/3)^6} -- the
deployed TFPT boundary transport spectrum, exactly.

THE STEPS (all exact integer/Fraction; sympy gated to charpolys):
 P1  K5 EDGE MACHINE: X = (-2,-2,-2,3,3) is the UNIQUE primitive
     traceless block-constant charge for the 3+2 split (3x+2y=0 =>
     (x,y) = t(-2,3), primitive iff t = +-1; sign frozen by the
     certified v774 table X5); E(K5) = 10 pairs decompose 3+6+1
     with pair charges (-4, +1, +6) = the SU(5) decuple
     3_{-4} + 6_{+1} + 1_{+6}, Y = X/6 = (-2/3, 1/6, 1);
     cross-check EVERY pair against the certified v774 hypercharge
     table (read-only import: the weight-2 words of C_even(5) ARE
     E(K5), classes u_c/Q_up/Q_dn/e_c); Stab_{S5}(W) = S3 x S2
     (order census 12 over all 120 permutations).
 P2  PETERSEN: pairs under disjointness = KG(5,2); verify
     SRG(10,3,0,1), exact spectrum 3^1 1^5 (-2)^4 (charpoly),
     girth 5, diameter 2, |Aut| = 120 (full backtracking census)
     = the faithful S5 image, betti = 15 - 10 + 1 = 6; distance
     shells around W: sizes (1, 3, 6), each CHARGE-PURE
     (+6, -4, +1); THE HEXAGON: the 6 distance-2 vertices induce a
     C6 (2-regular, connected, girth 6), explicit cycle
     (f1w1, f2w2, f3w1, f1w2, f2w1, f3w2) verified edge by edge --
     the flavor hexagon as the distance-2 shell [E neu]; crosslink:
     6 = |R+(A3)| = p2 = the transfer exponent (v124).
 P3  RADIAL DYNAMICS: the shell partition is EQUITABLE (every
     vertex checked); quotient == [[0,3,0],[1,0,2],[0,1,2]];
     eigenpairs exact: (1,1,1)->3, (6,-4,1)->-2 with the exact
     identification eigvec == (X(WW), X(FF), X(FW)) = the
     hypercharge vector ordered (e^c, u^c, Q), (3,1,-1)->1;
     P = Q_Pet/3 row-stochastic, spec(P) = {1, -2/3, 1/3},
     spec(P^6) = {1, 64/729, 1/729} exact.
 P4  TRANSPORT COMPARISON: the deployed TFPT transport operator T
     is identified in the corpus as (i) the FROZEN SPECTRUM
     {1, (2/3)^6, (1/3)^6} on the 3-dim cusp space (v54/v56 --
     v56's explicit matrix is a float demonstration conjugate, not
     a frozen matrix; v171 OS moments; v317; v124: lambda_n =
     (1-n/3)^6; v82: Koide multiplier), with GATE.METRIC.18 forcing
     the mu4-equivariant generator DIAGONAL in the cusp basis, and
     (ii) the explicit local sixth-root generator of v486 (lazy
     Z2-pair walk [[1,0,0],[0,1/2,1/6],[0,1/6,1/2]], spectrum
     {1, 2/3, 1/3}, sub-stochastic; v327's uniform rule is the
     superseded degenerate case {1, 2/3, 0}).  GATES:
     spec(P^6) == the frozen spectrum EXACTLY; lambda_n = (1-n/3)^6
     re-verified; the deployed T lives on the 3-DIM QUOTIENT (cusp
     space) -- the corpus provides NO 10-dim transfer operator, so
     the FULL Petersen prediction is stated as [H neu]: P10 =
     A_Pet/3 has spec {1, (1/3)^5, (-2/3)^4} and spec(P10^6) =
     {1^1, (1/3)^6 x5, (2/3)^6 x4} -- fast mode x5 = g_car, slow
     hypercharge mode x4 = |mu4| (multiplicity identities verified
     exactly on the Petersen side; trace crosscheck
     tr A^6 = 990 = 729 + 5 + 4*64).  HONEST SIGN NOTE: the radial
     sixth root has subleading eigenvalue -2/3 (negative); the sign
     is invisible in the deployed sixth-power spectrum (the PSD
     sixth root is the sibling probe TRANSPORT.SIXTHROOT.01).
 C   MUST-FAIL CONTROLS: (C1) the wrong edge choice F|W = 4+1 has
     NO intra-W pair (no distinguished Petersen vertex) and only 2
     pair-charge classes (6+4) -- the (1,3,6) charge/shell
     structure breaks; (C2) scrambled adjacency (the Johnson
     complement "share one slot") makes the former hexagon
     3-regular -- the C6 breaks.

KILLS (frozen, any one fires => PETERSEN-RADIAL-DEAD):
  K1  X not unique/primitive/traceless, or pair-charge census !=
      {-4:3, +1:6, +6:1}, or Y != (-2/3, 1/6, 1), or any pair
      disagrees with the certified v774 table, or |Stab(W)| != 12.
  K2  Petersen structure fails: not SRG(10,3,0,1), spectrum !=
      3^1 1^5 (-2)^4, girth != 5, diameter != 2, |Aut| != 120,
      betti != 6.
  K3  shells != (1,3,6), or a shell is not charge-pure, or the
      distance-2 shell is not a C6 (incl. the stated cycle order).
  K4  the shell partition is not equitable, or the quotient !=
      [[0,3,0],[1,0,2],[0,1,2]], or an eigenpair deviates (incl.
      the hypercharge-vector identification (6,-4,1) <-> -2).
  K5  spec(P^6) != {1, 64/729, 1/729}, or the corpus spectrum
      identification fails, or a multiplicity identity (5 = g_car,
      4 = |mu4|, trace 990) breaks.
VERDICTS (frozen): PETERSEN-RADIAL-EXACT (all checks pass, controls
fire) / PETERSEN-RADIAL-PARTIAL (no kill fired, but a non-kill check
failed) / PETERSEN-RADIAL-DEAD (a kill fired OR a must-fail control
does not fire).

TYPING (carried): [E neu] exact finite algebra/graph identities;
[H neu] the 10-dim multiplicity reading and the hexagon=shell
reading as transport semantics.  ROOTCLASS-MIXED cited: the pair
charges are CARRIER REPRESENTATION GEOMETRY (SU(5) decuple labels on
E(K5)); NO particle semantics is claimed -- the matter-classifier
reading remains Priority 2's separate kill test.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt.  Exakte Ganzzahl/Fraction-Arithmetik; sympy nur fuer
charakteristische Polynome; keine Floats, kein RNG, kein Fit.

Quellen (read-only): verification/v774_arf_spinor_compiler.py (X5,
iota, class_of, xval -- die zertifizierte Hyperladungs-Tafel),
verification/v54_seam_horizon_keystones.py + v56_unique_attractor.py
(frozen transfer spectrum), v124_resummed_clock.py (lambda_n =
(1-n/3)^6, p2 = 6), v486_transfer_full_rule.py (lazy Z2-pair walk),
v327_hypergraph_rewrite.py (uniform rule), v212_leptogenesis_decuple
(A_Lambda = 10 = |E(K5)|), tfpt_constants (g_car, N_fam).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/carrier_petersen_radial_probe.py

Original transport_sixthroot_probe.py docstring (verbatim):
transport_sixthroot_probe -- TRANSPORT.SIXTHROOT.01 (Arf compiler
programme, follow-up module 2): the bit-exact test of the candidate
PSD sixth root B of the deployed TFPT transport spectrum, and the
DECIDER bit-exact vs spectral-only.

THE CANDIDATE (preregistered, frozen):
    B = (1/18) [[13,  1,  4],
                [ 1, 13,  4],
                [ 4,  4, 10]]
with the compiler-number identifications
    18 = p4(1,1,2) = 1 + 1 + 16   (4th power sum of the anchor triple;
                                   crosslink: p1 = 4 = |mu4|,
                                   p2 = 6 = |R+(A3)| = the hand,
                                   p3 = 10 = A_Lambda -- v397/v394),
    13 = 3^2 + 2^2                (the (b,s) = (3,2) split, v14),
     4 = |mu4|,
    10 = A_Lambda = |E(K5)| = |Z2| * g_car   (v212/v397),
     1 = N_Phi                    (EM budget 41 = sum L + N_Phi, v159),
and the frozen eigen-assignment in the corpus basis
    (1,1,1) -> 1,   (1,-1,0) -> 2/3,   (1,1,-2) -> 1/3.

THE STEPS (all exact Fractions; sympy gated to charpolys/radicals):
 S1  COMPILER NUMBERS: verify every entry identification against
     tfpt_constants (g_car, N_fam) and the corpus atoms (Z2 = g_car -
     N_fam = 2, mu4 = 4, A_Lambda = 10 = Z2*g_car, N_Phi = 1,
     anchor power sums p1..p4(1,1,2) = (4, 6, 10, 18), 13 = 3^2+2^2);
     row-sum consistency 13 + 1 + 4 = 18 = p4.
 S2  MATRIX LAWS: B symmetric, doubly stochastic (rows AND columns
     sum to 1), PSD (symmetric + eigenvalues > 0; leading principal
     minors 13/18, 14/27, 2/9 > 0; det B = 1*(2/3)*(1/3) = 2/9);
     eigenvalues EXACTLY {1, 2/3, 1/3} (exact charpoly
     (x-1)(x-2/3)(x-1/3)) with the frozen eigenvectors verified by
     exact matvec.
 S3  UNIQUENESS / FREEDOM CENSUS: the eigenvectors are mutually
     orthogonal, so the spectral sum
        B = J/3 + (2/3) vv^T/2 + (1/3) ww^T/6,
     v = (1,-1,0), w = (1,1,-2), reconstructs B ENTRY-EXACTLY =>
     B is the UNIQUE symmetric matrix with this eigen-assignment
     (double stochasticity is then automatic).  FREEDOM: (a) swapping
     the two non-Perron eigenvalues gives the OTHER solution
     B_swap = (1/18)[[11,5,2],[5,11,2],[2,2,14]] != B (census in the
     corpus basis: exactly 2 assignments); (b) without pinning the
     eigenvectors there is a 1-parameter circle family B_theta =
     J/3 + (2/3) P_theta + (1/3)(I - J/3 - P_theta), symmetric and
     doubly stochastic for every theta (verified symbolically) --
     the corpus basis pins the circle to the 2 points, the stated
     assignment to B alone.
 S4  SIXTH POWER, BIT-EXACT: B^6 computed by exact Fraction matrix
     power AND by the spectral formula; both agree:
        B^6 = (1/4374) [[1651, 1267, 1456],
                        [1267, 1651, 1456],
                        [1456, 1456, 1462]],
     spec(B^6) = {1, 64/729, 1/729} = the deployed transport
     spectrum (v54/v56/v171/v317).
 S5  THE DECIDER: compare B^6 bit-exactly against the two deployed
     corpus surfaces:
       (i)  the canonical cusp-diagonal form D = diag(1, 64/729,
            1/729) (GATE.METRIC.18: mu4-equivariance forces the
            generator diagonal in the cusp basis; v54/v56 freeze the
            spectrum, not an off-diagonal matrix) -- exact difference
            B^6 - D printed; B^6 = U D U^{-1} with the RATIONAL
            eigenbasis U = [[1,1,1],[1,-1,1],[1,0,-2]] verified
            exactly;
       (ii) the v486 lazy Z2-pair walk M = [[1,0,0],[0,1/2,1/6],
            [0,1/6,1/2]] (the corpus's own sixth-root generator,
            SUB-stochastic, row sums {1, 2/3, 2/3}); M^6 computed
            exactly; B^6 != M^6 bit-exact (different row sums);
            exact conjugations verified: RATIONAL W = U V^{-1} with
            W M^6 W^{-1} = B^6, and the ORTHOGONAL eigenvector map
            O (entries in Q(sqrt2, sqrt3, sqrt6)) with O M^6 O^T =
            B^6 (sympy exact radicals).
     TYPE of the relation: spectral equivalence via rational GL(3,Q)
     conjugation (also orthogonal-irrational); the stochastic TYPES
     differ (B doubly stochastic vs M sub-stochastic with absorbing
     channel) => bit-exact identity fails for every deployed corpus
     matrix.
 C   MUST-FAIL CONTROLS: (C1) the doubly-stochastic perturbation
     B' = (1/18)[[12,2,4],[2,12,4],[4,4,10]] shifts the (1,-1,0)
     eigenvalue to 10/18 = 5/9 != 2/3; (C2) the raw single-entry
     perturbation B''_00 = 14/18 breaks stochasticity and the
     spectrum ({1, 2/3, 1/3} is no longer contained in spec).

KILLS (frozen, any one fires => SIXTHROOT-DEAD):
  K1  a compiler-number identification fails against
      tfpt_constants/corpus atoms.
  K2  B not symmetric/doubly stochastic/PSD, or eigenvalues !=
      {1, 2/3, 1/3}, or an eigenvector assignment fails.
  K3  the spectral reconstruction does not reproduce B entry-exactly
      (uniqueness given the assignment fails).
  K4  B^6 (Fraction power) != spectral formula, or spec(B^6) !=
      {1, 64/729, 1/729}.
  K5  a claimed exact conjugation identity fails.
DECIDER (frozen, data decides): SIXTHROOT-BITEXACT if B^6 equals a
deployed corpus matrix bit-exactly; SIXTHROOT-SPECTRAL-ONLY if all
kills pass but no bit-exact match exists (the exact difference and
conjugation type are then the deliverable); SIXTHROOT-DEAD if a kill
fires OR a must-fail control does not fire.

TYPING (carried): [E neu] exact matrix identities and censuses;
[H neu] the sixth-root reading as transport semantics.
ROOTCLASS-MIXED cited: carrier representation geometry, no particle
semantics.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt.  Exakte Fraction-Arithmetik; sympy nur fuer charpolys und
die orthogonale Radikal-Konjugation; keine Floats, kein RNG, kein Fit.

Quellen (read-only): tfpt_constants (g_car, N_fam),
verification/v54_seam_horizon_keystones.py + v56_unique_attractor.py
(frozen spectrum {1, (2/3)^6, (1/3)^6}; v56's Matrix ist eine Float-
Demonstration, keine eingefrorene Matrix), v486_transfer_full_rule.py
(lazy Z2-pair walk, die Korpus-Sechstwurzel), v327_hypergraph_rewrite
(uniforme Regel, degeneriert), v212/v397 (A_Lambda), v159 (N_Phi),
v14_carrier_uniqueness (13 = 3^2 + 2^2 Kontext), GATE.METRIC.18
(Cusp-diagonale kanonische Form; status_ledger.csv, read-only).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/transport_sixthroot_probe.py
"""

_LAST1 = {}
_LAST2 = {}


import itertools
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from math import gcd

_VERIFY = os.path.dirname(os.path.abspath(__file__))
_DISCOVERY = os.path.abspath(os.path.join(_VERIFY, "..", "experiments",
                                          "tfpt-discovery"))
sys.path.insert(0, _DISCOVERY)
sys.path.insert(0, _VERIFY)

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


# ---------------------------------------------------------------- setup
F_SLOTS = (0, 1, 2)          # f1, f2, f3
W_SLOTS = (3, 4)             # w1, w2  (the distinguished edge)
X5 = (-2, -2, -2, 3, 3)

PAIRS = [frozenset(p) for p in itertools.combinations(range(5), 2)]
PIDX = {p: i for i, p in enumerate(PAIRS)}
W_VERTEX = frozenset(W_SLOTS)


def pair_charge(p, X=X5):
    return sum(X[i] for i in p)


def adjacency(pairs, rule):
    n = len(pairs)
    return [[1 if i != j and rule(pairs[i], pairs[j]) else 0
             for j in range(n)] for i in range(n)]


ADJ = adjacency(PAIRS, lambda a, b: not (a & b))          # Petersen


def frac_charpoly_check(A, factors):
    """exact charpoly comparison via sympy (gated)."""
    from sympy import Matrix, symbols, expand, prod
    x = symbols("x")
    cp = Matrix(A).charpoly(x).as_expr()
    target = expand(prod((x - r) ** m for r, m in factors))
    return expand(cp - target) == 0


# ==================================================================== P1
def p1_edge_machine():
    section("P1: die K5-Kantenmaschine (F|W = 3+2, X, Dekuple, Stab)")
    # uniqueness of X: block-constant (x,x,x,y,y), traceless, primitive
    sols = [(x, y) for x in range(-12, 13) for y in range(-12, 13)
            if 3 * x + 2 * y == 0 and (x, y) != (0, 0)
            and gcd(abs(x), abs(y)) == 1]
    # algebra: 3x+2y=0 => (x,y) = t(-2,3); primitive iff |t| = 1
    check("P1.1 EINDEUTIGKEIT: block-konstant + spurfrei => (x,y) = "
          "t(-2,3); primitiv nur t = +-1: Zensus [-12,12]^2 = %s; "
          "Vorzeichen durch die zertifizierte v774-Tafel X5 fixiert => "
          "X = (-2,-2,-2,3,3)" % sols,
          sorted(sols) == [(-2, 3), (2, -3)], kill="K1")

    import v774_arf_spinor_compiler as v774   # read-only certified table
    check("P1.2 v774-Anker: X5 == (-2,-2,-2,3,3) (die zertifizierte "
          "Tafel waehlt den Repraesentanten)", v774.X5 == X5, kill="K1")

    cen = Counter(pair_charge(p) for p in PAIRS)
    ys = {c: Fr(c, 6) for c in cen}
    check("P1.3 DEKUPLE: E(K5) = 10 Paare, Ladungszensus {-4: 3, +1: 6,"
          " +6: 1} = 3_{-4} + 6_{+1} + 1_{+6}; Y = X/6 = (-2/3, 1/6, 1)",
          len(PAIRS) == 10 and dict(cen) == {-4: 3, 1: 6, 6: 1}
          and ys[-4] == Fr(-2, 3) and ys[1] == Fr(1, 6)
          and ys[6] == Fr(1), kill="K1")

    # pair -> v774 word (the weight-2 words of C_even(5) ARE E(K5))
    def word_of_pair(p):
        s = sorted(p)
        if set(s) <= set(F_SLOTS):
            return tuple(1 if k in s else 0 for k in range(3)) + (0,)
        if s == [3, 4]:
            return (0, 0, 0, 1)                       # A
        i = s[0]
        if s[1] == 3:                                 # a-slot => F_i + A
            return tuple(1 if k == i else 0 for k in range(3)) + (1,)
        return tuple(1 if k == i else 0 for k in range(3)) + (0,)  # F_i

    ok_tab = True
    names = Counter()
    for p in PAIRS:
        w = word_of_pair(p)
        support = tuple(k for k in range(5) if v774.iota(w)[k])
        if sum(v774.iota(w)) != 2 or support != tuple(sorted(p)):
            ok_tab = False
        if v774.xval(w) != pair_charge(p):
            ok_tab = False
        names[v774.class_of(w)] += 1
    check("P1.4 v774-KREUZCHECK: jedes Paar = Traeger eines Gewicht-2-"
          "Worts (iota-Support == Paar), Ladung == v774.xval, Klassen "
          "%s == {u_c: 3, Q_up: 3, Q_dn: 3, e_c: 1} (die 10 = {q*=1})"
          % dict(names),
          ok_tab and dict(names) == {"u_c": 3, "Q_up": 3, "Q_dn": 3,
                                     "e_c": 1}, kill="K1")

    stab = [pi for pi in itertools.permutations(range(5))
            if {pi[3], pi[4]} == set(W_SLOTS)]
    ok_struct = all({pi[0], pi[1], pi[2]} == set(F_SLOTS) for pi in stab)
    check("P1.5 Stab_{S5}(W): Ordnungszensus %d == 12 = |S3 x S2| "
          "(F-Block und W-Block separat permutiert)" % len(stab),
          len(stab) == 12 and ok_struct, kill="K1")
    return stab


# ==================================================================== P2
def petersen_aut_count(A):
    """full backtracking census of adjacency-preserving bijections."""
    n = len(A)
    count = [0]

    def extend(mapping, used):
        k = len(mapping)
        if k == n:
            count[0] += 1
            return
        for cand in range(n):
            if used[cand]:
                continue
            ok = True
            for j in range(k):
                if A[k][j] != A[cand][mapping[j]]:
                    ok = False
                    break
            if ok:
                mapping.append(cand)
                used[cand] = True
                extend(mapping, used)
                mapping.pop()
                used[cand] = False

    extend([], [False] * n)
    return count[0]


def p2_petersen():
    section("P2: Petersen KG(5,2) -- SRG, Spektrum, Aut, Schalen, "
            "das Hexagon")
    n = 10
    deg = [sum(ADJ[i]) for i in range(n)]
    ok_srg = all(d == 3 for d in deg)
    for i in range(n):
        for j in range(i + 1, n):
            common = sum(ADJ[i][k] * ADJ[j][k] for k in range(n))
            if ADJ[i][j] == 1 and common != 0:
                ok_srg = False
            if ADJ[i][j] == 0 and common != 1:
                ok_srg = False
    check("P2.1 SRG(10, 3, 0, 1): 3-regulaer, adjazent -> 0 gemeinsame "
          "Nachbarn, nicht-adjazent -> 1", ok_srg, kill="K2")

    check("P2.2 SPEKTRUM exakt: charpoly = (x-3)(x-1)^5(x+2)^4",
          frac_charpoly_check(ADJ, [(3, 1), (1, 5), (-2, 4)]),
          kill="K2")

    tri = sum(ADJ[i][j] * ADJ[j][k] * ADJ[k][i]
              for i in range(n) for j in range(n) for k in range(n))
    quad = 0
    for quadv in itertools.combinations(range(n), 4):
        for perm in itertools.permutations(quadv[1:]):
            cyc = (quadv[0],) + perm
            if all(ADJ[cyc[a]][cyc[(a + 1) % 4]] for a in range(4)):
                quad += 1
    has5 = any(
        all(ADJ[cyc[a]][cyc[(a + 1) % 5]] for a in range(5))
        for sub in itertools.combinations(range(n), 5)
        for tail in itertools.permutations(sub[1:])
        for cyc in ((sub[0],) + tail,))
    # diameter 2: I + A + A^2 > 0 entrywise
    A2 = [[sum(ADJ[i][k] * ADJ[k][j] for k in range(n))
           for j in range(n)] for i in range(n)]
    diam2 = all(ADJ[i][j] + A2[i][j] + (1 if i == j else 0) > 0
                for i in range(n) for j in range(n))
    m_edges = sum(deg) // 2
    check("P2.3 Taillenweite 5 (0 Dreiecke, 0 Viererzyklen, ein "
          "5-Zyklus existiert), Durchmesser 2, betti = 15 - 10 + 1 = 6",
          tri == 0 and quad == 0 and has5 and diam2
          and m_edges == 15 and m_edges - n + 1 == 6, kill="K2")

    naut = petersen_aut_count(ADJ)
    s5_maps = set()
    ok_s5 = True
    for pi in itertools.permutations(range(5)):
        vperm = tuple(PIDX[frozenset(pi[i] for i in PAIRS[k])]
                      for k in range(10))
        s5_maps.add(vperm)
        for a in range(10):
            for b in range(10):
                if ADJ[a][b] != ADJ[vperm[a]][vperm[b]]:
                    ok_s5 = False
    check("P2.4 |Aut| = %d == 120 (voller Backtracking-Zensus) = die "
          "treue S5-Wirkung (120 verschiedene induzierte "
          "Automorphismen): Aut(Petersen) = S5" % naut,
          naut == 120 and len(s5_maps) == 120 and ok_s5, kill="K2")

    # distance shells around the W vertex
    w = PIDX[W_VERTEX]
    dist = {w: 0}
    frontier = [w]
    while frontier:
        nxt = []
        for u in frontier:
            for v2 in range(n):
                if ADJ[u][v2] and v2 not in dist:
                    dist[v2] = dist[u] + 1
                    nxt.append(v2)
        frontier = nxt
    shells = {d: [i for i in range(n) if dist[i] == d]
              for d in set(dist.values())}
    sizes = tuple(len(shells[d]) for d in sorted(shells))
    charges = {d: {pair_charge(PAIRS[i]) for i in shells[d]}
               for d in shells}
    check("P2.5 SCHALEN um W: Groessen %s == (1, 3, 6), LADUNGSREIN: "
          "d=0 -> {+6} (e^c), d=1 -> {-4} (u^c), d=2 -> {+1} (Q)"
          % (sizes,),
          sizes == (1, 3, 6) and charges[0] == {6}
          and charges[1] == {-4} and charges[2] == {1}, kill="K3")

    hexa = shells[2]
    degs_in = {i: sum(ADJ[i][j] for j in hexa) for i in hexa}
    # connectivity of the induced subgraph
    seen = {hexa[0]}
    stack = [hexa[0]]
    while stack:
        u = stack.pop()
        for v2 in hexa:
            if ADJ[u][v2] and v2 not in seen:
                seen.add(v2)
                stack.append(v2)
    tri_in = sum(ADJ[a][b] * ADJ[b][c] * ADJ[c][a]
                 for a in hexa for b in hexa for c in hexa)
    quad_in = 0
    for qv in itertools.combinations(hexa, 4):
        for perm in itertools.permutations(qv[1:]):
            cyc = (qv[0],) + perm
            if all(ADJ[cyc[x]][cyc[(x + 1) % 4]] for x in range(4)):
                quad_in += 1
    stated = [frozenset(s) for s in
              ({0, 3}, {1, 4}, {2, 3}, {0, 4}, {1, 3}, {2, 4})]
    ok_cycle = all(ADJ[PIDX[stated[k]]][PIDX[stated[(k + 1) % 6]]]
                   for k in range(6))
    check("P2.6 DAS HEXAGON [E neu]: die 6 Distanz-2-Knoten induzieren "
          "einen C6 (2-regulaer, zusammenhaengend, keine 3-/4-Zyklen); "
          "explizite Ordnung (f1w1, f2w2, f3w1, f1w2, f2w1, f3w2) "
          "Kante fuer Kante verifiziert; Crosslink: 6 = |R+(A3)| = p2 "
          "= der Transfer-Exponent (v124)",
          all(d == 2 for d in degs_in.values()) and len(seen) == 6
          and tri_in == 0 and quad_in == 0 and ok_cycle
          and len(hexa) == 6, kill="K3")
    return shells


# ==================================================================== P3
QPET = [[0, 3, 0], [1, 0, 2], [0, 1, 2]]


def p3_radial(shells):
    section("P3: die radiale Dynamik (aequitable Partition, Quotient, "
            "Hyperladungs-Eigenvektor)")
    cells = [shells[0], shells[1], shells[2]]
    ok_eq = True
    for ci, cell in enumerate(cells):
        for u in cell:
            row = [sum(ADJ[u][v] for v in cells[cj]) for cj in range(3)]
            if row != QPET[ci]:
                ok_eq = False
    check("P3.1 AEQUITABEL: jeder Knoten der Zelle i hat exakt "
          "Q[i][j] Nachbarn in Zelle j; Quotient == "
          "[[0,3,0],[1,0,2],[0,1,2]]", ok_eq, kill="K4")

    def matvec(M, v):
        return tuple(sum(M[i][j] * v[j] for j in range(3))
                     for i in range(3))

    ones, hyp, third_v = (1, 1, 1), (6, -4, 1), (3, 1, -1)
    ok_e1 = matvec(QPET, ones) == (3, 3, 3)
    ok_e2 = matvec(QPET, hyp) == (-12, 8, -2)
    ok_e3 = matvec(QPET, third_v) == (3, 1, -1)
    xw = (pair_charge(W_VERTEX),
          pair_charge(PAIRS[shells[1][0]]),
          pair_charge(PAIRS[shells[2][0]]))
    check("P3.2 EIGENPAARE exakt: (1,1,1)->3; (6,-4,1)->-2 == DER "
          "HYPERLADUNGS-VEKTOR (X(WW), X(FF), X(FW)) = %s geordnet "
          "(e^c, u^c, Q); (3,1,-1)->1; charpoly(Q_Pet) = "
          "(x-3)(x+2)(x-1)" % (xw,),
          ok_e1 and ok_e2 and ok_e3 and hyp == xw
          and frac_charpoly_check(QPET, [(3, 1), (-2, 1), (1, 1)]),
          kill="K4")

    P = [[Fr(QPET[i][j], 3) for j in range(3)] for i in range(3)]
    ok_stoch = all(sum(P[i]) == 1 for i in range(3))
    specP = sorted((Fr(1), Fr(-2, 3), Fr(1, 3)))
    specP6 = sorted(x ** 6 for x in specP)
    check("P3.3 P = Q_Pet/3 zeilenstochastisch; spec(P) = "
          "{1, -2/3, 1/3}; spec(P^6) = {1, 64/729, 1/729} = "
          "{1, (2/3)^6, (1/3)^6}",
          ok_stoch
          and frac_charpoly_check(P, [(Fr(1), 1), (Fr(-2, 3), 1),
                                      (Fr(1, 3), 1)])
          and specP6 == sorted([Fr(1), Fr(64, 729), Fr(1, 729)]),
          kill="K4")


# ==================================================================== P4
def p4_transport():
    section("P4: der Transport-Vergleich (die deployete T-Spektrum-"
            "Identifikation)")
    from tfpt_constants import g_car, N_fam
    FROZEN_SPEC = sorted([Fr(1), Fr(64, 729), Fr(1, 729)])
    specP6 = sorted(x ** 6 for x in (Fr(1), Fr(-2, 3), Fr(1, 3)))
    check("P4.1 GATE: spec(P_radial^6) == das eingefrorene Transport-"
          "Spektrum {1, (2/3)^6, (1/3)^6} EXAKT (v54/v56/v171/v317; "
          "v124: lambda_n = (1 - n/3)^6; GATE.METRIC.18: Generator "
          "diagonal in der Cusp-Basis)",
          specP6 == FROZEN_SPEC
          and [Fr(3 - nn, 3) ** 6 for nn in range(3)]
          == [Fr(1), Fr(64, 729), Fr(1, 729)], kill="K5")

    # v486 sixth-root generator (read-only re-derivation, exact)
    s0, h0 = Fr(1, 2), Fr(1, 6)
    M = [[Fr(1), Fr(0), Fr(0)], [Fr(0), s0, h0], [Fr(0), h0, s0]]
    specM = sorted([Fr(1), s0 + h0, s0 - h0])
    check("P4.2 KORPUS-SECHSTE-WURZEL: v486's lazy Z2-pair walk "
          "[[1,0,0],[0,1/2,1/6],[0,1/6,1/2]] hat spec {1, 2/3, 1/3} "
          "(sub-stochastisch, Zeilensummen {1, 2/3, 2/3}); v327's "
          "uniforme Regel {1, 2/3, 0} ist der degenerierte Fall -- "
          "T ist im Korpus 3-DIM (Quotient/Cusp-Raum), KEIN 10-dim "
          "Operator deployed",
          specM == sorted([Fr(1), Fr(2, 3), Fr(1, 3)])
          and [sum(r) for r in M] == [1, Fr(2, 3), Fr(2, 3)])

    # full 10-dim Petersen prediction [H neu]
    P10 = [[Fr(ADJ[i][j], 3) for j in range(10)] for i in range(10)]
    ok_p10 = frac_charpoly_check(
        P10, [(Fr(1), 1), (Fr(1, 3), 5), (Fr(-2, 3), 4)])
    # sixth-power multiplicities via the exact eigenvalue map
    mult6 = {Fr(1): 1, Fr(1, 729): 5, Fr(64, 729): 4}
    trA6 = 3 ** 6 * 1 + 1 * 5 + 64 * 4
    A6 = ADJ
    for _ in range(5):
        A6 = [[sum(A6[i][k] * ADJ[k][j] for k in range(10))
               for j in range(10)] for i in range(10)]
    check("P4.3 VOLLE PETERSEN-VORHERSAGE [H neu]: spec(P10) = "
          "{1, (1/3)^5, (-2/3)^4}; spec(P10^6) = {1^1, (1/3)^6 x5, "
          "(2/3)^6 x4} -- schneller Modus x5 = g_car = %d, langsamer "
          "Hyperladungs-Modus x4 = |mu4| = 4; Spur-Kreuzcheck "
          "tr A^6 = %d == 990 = 729 + 5 + 4*64; KEIN Korpus-"
          "Gegenstueck (T ist 3-dim) -- Vorhersage, nicht Verifikation"
          % (g_car, sum(A6[i][i] for i in range(10))),
          ok_p10 and mult6[Fr(1, 729)] == g_car == 5
          and mult6[Fr(64, 729)] == 4
          and sum(A6[i][i] for i in range(10)) == trA6 == 990,
          kill="K5")

    print("    HONEST SIGN NOTE: der radiale Unterleit-Eigenwert ist "
          "-2/3 (negativ); das Vorzeichen ist im deployeten Sechst-"
          "Potenz-Spektrum unsichtbar. Die PSD-Sechstwurzel ist "
          "TRANSPORT.SIXTHROOT.01 (Schwester-Probe).")
    print("    N_fam-Kreuzcheck: %d Zellen = N_fam = %d Cusp-Stufen"
          % (3, N_fam))


# ==================================================================== C
def c_controls():
    section("C: Must-fail-Kontrollen")
    # C1: wrong edge F|W = 4+1
    Xbad_sols = [(x, y) for x in range(-12, 13) for y in range(-12, 13)
                 if 4 * x + y == 0 and (x, y) != (0, 0)
                 and gcd(abs(x), abs(y)) == 1]
    xb, yb = -1, 4
    Xbad = (xb, xb, xb, xb, yb)
    cen_bad = Counter(sum(Xbad[i] for i in p) for p in PAIRS)
    w_pairs = [p for p in PAIRS if p <= {4}]
    check("C1 KONTROLLE FEUERT (falsche Kante F|W = 4+1): primitive "
          "Loesung (-1,4); Paar-Ladungszensus %s hat nur 2 Klassen "
          "(6+4), KEIN intra-W-Paar existiert (%d) -- die (1,3,6)-"
          "Struktur bricht" % (dict(cen_bad), len(w_pairs)),
          sorted(Xbad_sols) == [(-1, 4), (1, -4)]
          and len(cen_bad) == 2
          and sorted(cen_bad.values()) == [4, 6] and not w_pairs)

    # C2: scrambled adjacency (Johnson complement: share exactly one)
    ADJ_J = adjacency(PAIRS, lambda a, b: len(a & b) == 1)
    hexa = [PIDX[frozenset(s)] for s in
            ({0, 3}, {1, 4}, {2, 3}, {0, 4}, {1, 3}, {2, 4})]
    degs = {i: sum(ADJ_J[i][j] for j in hexa) for i in hexa}
    check("C2 KONTROLLE FEUERT (verwuerfelte Adjazenz = Johnson-"
          "Komplement): das Hexagon wird %s-regulaer statt 2-regulaer "
          "-- der C6 bricht" % sorted(set(degs.values())),
          set(degs.values()) == {3})


# ======================================================================
def main():
    print("=" * 78)
    print("CARRIER.PETERSEN.RADIAL.01 -- die K5-Kantenmaschine, "
          "Petersen, radiale Dynamik")
    print("=" * 78, flush=True)
    p1_edge_machine()
    shells = p2_petersen()
    p3_radial(shells)
    p4_transport()
    c_controls()

    section("ZUSAMMENFASSUNG / VERDIKT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    print("%d/%d Checks bestanden" % (n_pass, n_all))
    if KILLS or not controls_ok:
        verdict = "PETERSEN-RADIAL-DEAD"
        print("VERDIKT: PETERSEN-RADIAL-DEAD -- Kills: %s%s"
              % (sorted(set(KILLS)),
                 "" if controls_ok else " (+ Kontrolle feuert nicht)"))
    elif n_pass == n_all:
        verdict = "PETERSEN-RADIAL-EXACT"
        print("VERDIKT: PETERSEN-RADIAL-EXACT -- X eindeutig, Dekuple "
              "3_{-4}+6_{+1}+1_{+6} == v774-Tafel, Petersen SRG(10,3,"
              "0,1) mit Aut = S5, Schalen (1,3,6) ladungsrein, das "
              "Hexagon = die Distanz-2-Schale, Quotient aequitabel "
              "mit Hyperladungs-Eigenvektor (6,-4,1) -> -2, "
              "spec(P^6) == das deployete Transport-Spektrum exakt; "
              "10-dim Multiplizitaeten (x5 = g_car, x4 = |mu4|) als "
              "[H neu]-Vorhersage.")
    else:
        verdict = "PETERSEN-RADIAL-PARTIAL"
        print("VERDIKT: PETERSEN-RADIAL-PARTIAL -- kein Kill, aber "
              "Nicht-Kill-Checks gescheitert; siehe FAIL-Zeilen.")
    _LAST1["verdict"] = verdict
    print("Verdikt-Enum: %s" % verdict)
    print("Laufzeit: %.1f s" % (time.time() - T0))
    print("ALLE CHECKS BESTANDEN" if n_pass == n_all
          else "CHECKS FEHLGESCHLAGEN")
    return 0 if n_pass == n_all else 1


_run_part1 = main


def _run_part2():
    """Part 2: transport_sixthroot_probe.py, promoted verbatim in a function scope (v789/v795 precedent)."""

    import os
    import sys
    import time
    from fractions import Fraction as Fr

    _VERIFY = os.path.dirname(os.path.abspath(__file__))
    _DISCOVERY = os.path.abspath(os.path.join(_VERIFY, "..", "experiments",
                                              "tfpt-discovery"))
    sys.path.insert(0, _DISCOVERY)
    sys.path.insert(0, _VERIFY)

    T0 = time.time()
    CHECKS = []
    KILLS = []
    BITEXACT_HITS = []


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


    def matvec(A, v):
        return tuple(sum(A[i][j] * v[j] for j in range(len(v)))
                     for i in range(len(A)))


    def outer(v, w):
        return [[Fr(v[i] * w[j]) for j in range(len(w))]
                for i in range(len(v))]


    def madd(*Ms):
        n = len(Ms[0])
        return [[sum(M[i][j] for M in Ms) for j in range(n)]
                for i in range(n)]


    def mscale(c, M):
        return [[c * M[i][j] for j in range(len(M[0]))]
                for i in range(len(M))]


    def fmt(M):
        return "[" + "; ".join(",".join(str(x) for x in r) for r in M) + "]"


    B = mat([[Fr(13, 18), Fr(1, 18), Fr(4, 18)],
             [Fr(1, 18), Fr(13, 18), Fr(4, 18)],
             [Fr(4, 18), Fr(4, 18), Fr(10, 18)]])
    V1, V2, V3 = (1, 1, 1), (1, -1, 0), (1, 1, -2)
    EIG = {V1: Fr(1), V2: Fr(2, 3), V3: Fr(1, 3)}


    # ==================================================================== S1
    def s1_compiler_numbers():
        section("S1: Compiler-Zahlen-Identifikationen gegen tfpt_constants")
        from tfpt_constants import g_car, N_fam
        Z2 = g_car - N_fam
        mu4 = 4
        A_Lambda = Z2 * g_car
        N_Phi = 1
        anchor = (1, 1, 2)
        p = [sum(a ** k for a in anchor) for k in range(1, 5)]
        check("S1.1 Anker-Potenzsummen p1..p4(1,1,2) = %s == (4, 6, 10, 18)"
              ": p1 = |mu4|, p2 = 6 = |R+(A3)| (die Hand, v486), "
              "p3 = A_Lambda (v397), p4 = 18 = der Nenner" % (p,),
              p == [4, 6, 10, 18] and p[0] == mu4 and p[2] == A_Lambda,
              kill="K1")
        check("S1.2 13 = 3^2 + 2^2 = N_fam^2 + Z2^2 (der (b,s) = (3,2)-"
              "Split, v14); 4 = |mu4|; 10 = A_Lambda = |E(K5)| = |Z2|*"
              "g_car = %d (v212/v397); 1 = N_Phi (EM-Budget 41 = 40 + "
              "N_Phi, v159)" % A_Lambda,
              13 == N_fam ** 2 + Z2 ** 2 and mu4 == 4
              and A_Lambda == 10 and N_Phi == 1, kill="K1")
        check("S1.3 Zeilensummen-Konsistenz: 13 + 1 + 4 = 18 = p4 und "
              "4 + 4 + 10 = 18; Eintraege = {13, 1, 4, 10} = "
              "{3^2+2^2, N_Phi, |mu4|, A_Lambda} / 18",
              13 + 1 + 4 == 18 and 4 + 4 + 10 == 18, kill="K1")


    # ==================================================================== S2
    def s2_matrix_laws():
        section("S2: Matrixgesetze (symmetrisch, doppelt-stochastisch, "
                "PSD, Eigensystem exakt)")
        sym = all(B[i][j] == B[j][i] for i in range(3) for j in range(3))
        rows = [sum(B[i]) for i in range(3)]
        cols = [sum(B[i][j] for i in range(3)) for j in range(3)]
        check("S2.1 B symmetrisch; doppelt-stochastisch (Zeilen %s, "
              "Spalten %s); alle Eintraege > 0"
              % (rows, cols),
              sym and rows == [1, 1, 1] and cols == [1, 1, 1]
              and all(B[i][j] > 0 for i in range(3) for j in range(3)),
              kill="K2")

        ok_vec = all(matvec(B, v) == tuple(lam * x for x in v)
                     for v, lam in EIG.items())
        from sympy import Matrix, Rational, symbols, expand
        x = symbols("x")
        cp = Matrix(3, 3, lambda i, j: Rational(B[i][j].numerator,
                                                B[i][j].denominator)
                    ).charpoly(x).as_expr()
        target = expand((x - 1) * (x - Rational(2, 3)) * (x - Rational(1, 3)))
        check("S2.2 EIGENSYSTEM exakt: (1,1,1)->1, (1,-1,0)->2/3, "
              "(1,1,-2)->1/3 (exakter Matvec); charpoly = "
              "(x-1)(x-2/3)(x-1/3)",
              ok_vec and expand(cp - target) == 0, kill="K2")

        m1 = B[0][0]
        m2 = B[0][0] * B[1][1] - B[0][1] * B[1][0]
        det = (B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1])
               - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0])
               + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]))
        check("S2.3 PSD: fuehrende Hauptminoren (%s, %s, %s) > 0; "
              "det B = 2/9 = 1*(2/3)*(1/3); Spur = 2 = 1 + 2/3 + 1/3"
              % (m1, m2, det),
              m1 > 0 and m2 > 0 and det == Fr(2, 9) == Fr(1) * Fr(2, 3)
              * Fr(1, 3) and sum(B[i][i] for i in range(3)) == 2,
              kill="K2")


    # ==================================================================== S3
    def s3_uniqueness():
        section("S3: Eindeutigkeit gegeben die Zuordnung / Freiheits-Zensus")
        ortho = (sum(a * b for a, b in zip(V2, V3)) == 0
                 and sum(a * b for a, b in zip(V1, V2)) == 0
                 and sum(a * b for a, b in zip(V1, V3)) == 0)
        B_rec = madd(mscale(Fr(1, 3), outer(V1, V1)),
                     mscale(Fr(2, 3) / 2, outer(V2, V2)),
                     mscale(Fr(1, 3) / 6, outer(V3, V3)))
        check("S3.1 EINDEUTIG: Basis orthogonal; Spektralsumme J/3 + "
              "(2/3) vv^T/2 + (1/3) ww^T/6 == B EINTRAG-EXAKT => B ist "
              "die einzige symmetrische Matrix mit dieser Zuordnung "
              "(doppelte Stochastik folgt)",
              ortho and B_rec == B, kill="K3")

        B_swap = madd(mscale(Fr(1, 3), outer(V1, V1)),
                      mscale(Fr(1, 3) / 2, outer(V2, V2)),
                      mscale(Fr(2, 3) / 6, outer(V3, V3)))
        swap_expect = mat([[Fr(11, 18), Fr(5, 18), Fr(2, 18)],
                           [Fr(5, 18), Fr(11, 18), Fr(2, 18)],
                           [Fr(2, 18), Fr(2, 18), Fr(14, 18)]])
        rows_sw = [sum(B_swap[i]) for i in range(3)]
        check("S3.2 ZENSUS in der Korpus-Basis: die getauschte Zuordnung "
              "gibt B_swap = (1/18)[[11,5,2],[5,11,2],[2,2,14]] != B "
              "(ebenfalls symmetrisch doppelt-stochastisch) -- genau 2 "
              "Zuordnungen, die angegebene waehlt B",
              B_swap == swap_expect and B_swap != B
              and rows_sw == [1, 1, 1], kill="K3")

        # (b) the theta-circle: without the eigenvector pin, a 1-parameter
        # family of symmetric doubly stochastic solutions exists
        from sympy import (Matrix, Rational, cos, sin, symbols, simplify,
                           eye, ones)
        th = symbols("theta", real=True)
        u2 = Matrix([1, -1, 0]) / Matrix([1, -1, 0]).norm()
        u3 = Matrix([1, 1, -2]) / Matrix([1, 1, -2]).norm()
        e = cos(th) * u2 + sin(th) * u3
        P_th = e * e.T
        J3 = ones(3, 3) / 3
        B_th = J3 + Rational(2, 3) * P_th \
            + Rational(1, 3) * (eye(3) - J3 - P_th)
        rowsums = [simplify(sum(B_th[i, j] for j in range(3)))
                   for i in range(3)]
        symm = all(simplify(B_th[i, j] - B_th[j, i]) == 0
                   for i in range(3) for j in range(3))
        at0 = all(simplify(B_th[i, j].subs(th, 0)
                           - Rational(B[i][j].numerator,
                                      B[i][j].denominator)) == 0
                  for i in range(3) for j in range(3))
        check("S3.3 FREIHEIT ohne Eigenvektor-Pin: B_theta = J/3 + (2/3) "
              "P_theta + (1/3)(I - J/3 - P_theta) ist fuer JEDES theta "
              "symmetrisch mit Zeilensummen 1 (symbolisch verifiziert; "
              "1-Parameter-Kreis) und B_0 == B -- die Korpus-Basis pinnt "
              "auf 2 Punkte, die Zuordnung auf B allein",
              all(r == 1 for r in rowsums) and symm and at0)


    # ==================================================================== S4
    def s4_sixth_power():
        section("S4: B^6 bit-exakt (Fraction-Potenz == Spektralformel)")
        B6 = mpow(B, 6)
        B6_spec = madd(mscale(Fr(1, 3), outer(V1, V1)),
                       mscale(Fr(64, 729) / 2, outer(V2, V2)),
                       mscale(Fr(1, 729) / 6, outer(V3, V3)))
        expect = mat([[Fr(1651, 4374), Fr(1267, 4374), Fr(1456, 4374)],
                      [Fr(1267, 4374), Fr(1651, 4374), Fr(1456, 4374)],
                      [Fr(1456, 4374), Fr(1456, 4374), Fr(1462, 4374)]])
        check("S4.1 B^6 = (1/4374)[[1651,1267,1456],[1267,1651,1456],"
              "[1456,1456,1462]]: direkte Fraction-Potenz == "
              "Spektralformel == erwartete Matrix",
              B6 == B6_spec == expect, kill="K4")

        ok_vec6 = all(matvec(B6, v) == tuple(lam ** 6 * x for x in v)
                      for v, lam in EIG.items())
        check("S4.2 spec(B^6) = {1, 64/729, 1/729} = das deployete "
              "Transport-Spektrum (v54/v56/v171/v317); B^6 doppelt-"
              "stochastisch (Zeilensummen %s)"
              % [sum(B6[i]) for i in range(3)],
              ok_vec6 and [sum(B6[i]) for i in range(3)] == [1, 1, 1],
              kill="K4")
        return B6


    # ==================================================================== S5
    def s5_decider(B6):
        section("S5: DER ENTSCHEIDER -- bit-exakt vs. nur spektral")
        D = mat([[1, 0, 0], [0, Fr(64, 729), 0], [0, 0, Fr(1, 729)]])
        hit_diag = (B6 == D)
        if hit_diag:
            BITEXACT_HITS.append("cusp-diagonal D")
        diff = [[B6[i][j] - D[i][j] for j in range(3)] for i in range(3)]
        print("    B^6 - D (exakt): %s" % fmt(diff))
        U = mat([[1, 1, 1], [1, -1, 1], [1, 0, -2]])
        # U columns = (1,1,1), (1,-1,0), (1,1,-2)
        UD = mmul(U, D)
        B6U = mmul(B6, U)
        check("S5.1 (i) Cusp-diagonale kanonische Form (GATE.METRIC.18): "
              "B^6 %s D = diag(1, 64/729, 1/729) bit-exakt; exakte "
              "RATIONALE Konjugation B^6 U = U D mit U = [[1,1,1],"
              "[1,-1,1],[1,0,-2]] (Spalten = die Eigenbasis)"
              % ("==" if hit_diag else "!="),
              B6U == UD, kill="K5")

        # (ii) v486 lazy walk, re-derived exactly
        M = mat([[1, 0, 0],
                 [0, Fr(1, 2), Fr(1, 6)],
                 [0, Fr(1, 6), Fr(1, 2)]])
        M6 = mpow(M, 6)
        a = (Fr(64, 729) + Fr(1, 729)) / 2
        b = (Fr(64, 729) - Fr(1, 729)) / 2
        M6_expect = mat([[1, 0, 0], [0, a, b], [0, b, a]])
        rows_m6 = [sum(M6[i]) for i in range(3)]
        hit_lazy = (B6 == M6)
        if hit_lazy:
            BITEXACT_HITS.append("v486 lazy walk M^6")
        check("S5.2 (ii) v486 lazy Z2-pair walk: M^6 = [[1,0,0],[0,65/1458,"
              "63/1458],[0,63/1458,65/1458]] exakt (a,b = %s, %s); "
              "Zeilensummen %s (SUB-stochastisch) => B^6 %s M^6 bit-exakt"
              % (a, b, rows_m6, "==" if hit_lazy else "!="),
              M6 == M6_expect and not hit_lazy, kill="K5")

        # exact rational conjugation W = U V^{-1}, W M^6 W^{-1} = B^6
        V = mat([[1, 0, 0], [0, 1, 1], [0, 1, -1]])
        # V columns = M eigenvectors (1,0,0), (0,1,1), (0,1,-1) for 1, 2/3, 1/3
        ok_v = all(matvec(M, (V[0][k], V[1][k], V[2][k]))
                   == tuple(lam * x for x in (V[0][k], V[1][k], V[2][k]))
                   for k, lam in enumerate([Fr(1), Fr(2, 3), Fr(1, 3)]))
        from sympy import Matrix, Rational, sqrt, simplify

        def to_sym(A):
            return Matrix(3, 3, lambda i, j: Rational(A[i][j].numerator,
                                                      A[i][j].denominator))

        Us, Vs, Ms6, Bs6 = to_sym(U), to_sym(V), to_sym(M6), to_sym(B6)
        W = Us * Vs.inv()
        ok_rat = simplify(W * Ms6 * W.inv() - Bs6) == Matrix.zeros(3, 3)
        # orthogonal conjugation from unit eigenvectors
        bvecs = [Matrix(v) / Matrix(v).norm() for v in (V1, V2, V3)]
        mvecs = [Matrix(v) / Matrix(v).norm()
                 for v in ((1, 0, 0), (0, 1, 1), (0, 1, -1))]
        O = sum((bvecs[k] * mvecs[k].T for k in range(3)),
                Matrix.zeros(3, 3))
        ok_orth = (simplify(O * O.T - Matrix.eye(3)) == Matrix.zeros(3, 3)
                   and simplify(O * Ms6 * O.T - Bs6) == Matrix.zeros(3, 3))
        check("S5.3 EXAKTE KONJUGATIONEN: rationales W = U V^{-1} in "
              "GL(3,Q) mit W M^6 W^{-1} = B^6; orthogonales O (Eintraege "
              "in Q(sqrt2, sqrt3, sqrt6)) mit O O^T = I und O M^6 O^T = "
              "B^6 -- TYP: spektrale Aequivalenz, KEINE bit-exakte "
              "Identitaet; stochastische Typen verschieden (doppelt- vs. "
              "sub-stochastisch mit absorbierendem Kanal)",
              ok_v and ok_rat and ok_orth, kill="K5")

        print("    KORPUS-IDENTIFIKATION von T: eingefrorenes SPEKTRUM "
              "{1, (2/3)^6, (1/3)^6} auf dem 3-dim Cusp-Raum "
              "(v54_seam_horizon_keystones, v56_unique_attractor [Matrix "
              "dort nur Float-Demonstration], v171_os_moment_cluster, "
              "v317_galois_family, v124_resummed_clock); expliziter "
              "Sechstwurzel-Generator: v486_transfer_full_rule (lazy "
              "Z2-pair walk); degeneriert: v327_hypergraph_rewrite; "
              "kanonische Form: cusp-diagonal (GATE.METRIC.18).")


    # ==================================================================== C
    def c_controls():
        section("C: Must-fail-Kontrollen")
        Bp = mat([[Fr(12, 18), Fr(2, 18), Fr(4, 18)],
                  [Fr(2, 18), Fr(12, 18), Fr(4, 18)],
                  [Fr(4, 18), Fr(4, 18), Fr(10, 18)]])
        lam_v2 = matvec(Bp, V2)
        fired1 = lam_v2 == tuple(Fr(5, 9) * x for x in V2)
        check("C1 KONTROLLE FEUERT (doppelt-stochastische Stoerung "
              "13->12, 1->2): der (1,-1,0)-Eigenwert wird 5/9 != 2/3 -- "
              "das Spektrum bricht",
              fired1 and Fr(5, 9) != Fr(2, 3))

        Bpp = [row[:] for row in B]
        Bpp[0][0] = Fr(14, 18)
        rows_pp = [sum(Bpp[i]) for i in range(3)]
        from sympy import Matrix, Rational, symbols
        x = symbols("x")
        cp = Matrix(3, 3, lambda i, j: Rational(Bpp[i][j].numerator,
                                                Bpp[i][j].denominator)
                    ).charpoly(x)
        still = all(cp.eval(Rational(v.numerator, v.denominator)) == 0
                    for v in (Fr(1), Fr(2, 3), Fr(1, 3)))
        check("C2 KONTROLLE FEUERT (rohe Eintrags-Stoerung B_00 -> 14/18):"
              " Zeilensummen %s != (1,1,1) und {1, 2/3, 1/3} ist NICHT "
              "mehr im Spektrum enthalten" % (rows_pp,),
              rows_pp != [1, 1, 1] and not still)


    # ======================================================================
    def main():
        print("=" * 78)
        print("TRANSPORT.SIXTHROOT.01 -- der bit-exakte Test der PSD-"
              "Sechstwurzel B")
        print("=" * 78, flush=True)
        s1_compiler_numbers()
        s2_matrix_laws()
        s3_uniqueness()
        B6 = s4_sixth_power()
        s5_decider(B6)
        c_controls()

        section("ZUSAMMENFASSUNG / VERDIKT")
        n_pass = sum(1 for _, ok in CHECKS if ok)
        n_all = len(CHECKS)
        controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
        print("%d/%d Checks bestanden" % (n_pass, n_all))
        if KILLS or not controls_ok:
            verdict = "SIXTHROOT-DEAD"
            print("VERDIKT: SIXTHROOT-DEAD -- Kills: %s%s"
                  % (sorted(set(KILLS)),
                     "" if controls_ok else " (+ Kontrolle feuert nicht)"))
        elif BITEXACT_HITS:
            verdict = "SIXTHROOT-BITEXACT"
            print("VERDIKT: SIXTHROOT-BITEXACT -- Treffer: %s"
                  % BITEXACT_HITS)
        else:
            verdict = "SIXTHROOT-SPECTRAL-ONLY"
            print("VERDIKT: SIXTHROOT-SPECTRAL-ONLY -- B ist die "
                  "eindeutige symmetrische doppelt-stochastische "
                  "PSD-Sechstwurzel in der Korpus-Basis mit der "
                  "angegebenen Zuordnung; B^6 traegt exakt das deployete "
                  "Spektrum, aber KEINE deployete Korpus-Matrix ist "
                  "bit-exakt B^6 (der Korpus friert das Spektrum ein, "
                  "nicht die Basis); Konjugationstyp: rational GL(3,Q) "
                  "(auch orthogonal-irrational) auf v486's M^6 bzw. die "
                  "cusp-diagonale Form.")
        _LAST2["verdict"] = verdict
        print("Verdikt-Enum: %s" % verdict)
        print("Laufzeit: %.1f s" % (time.time() - T0))
        print("ALLE CHECKS BESTANDEN" if n_pass == n_all
              else "CHECKS FEHLGESCHLAGEN")
        return 0 if n_pass == n_all else 1


    rc = main()
    return rc, list(CHECKS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 19/19
    (PETERSEN-RADIAL-EXACT), part 2 must be 16/16
    (SIXTHROOT-SPECTRAL-ONLY)."""
    rc1 = _run_part1()
    fails1 = [n for (n, ok) in CHECKS if not ok]
    v1 = _LAST1.get("verdict", "")
    part1_ok = (rc1 == 0 and not fails1 and len(CHECKS) == 19
                and v1 == "PETERSEN-RADIAL-EXACT")
    print("\n[%s] PART-1 PATTERN GATE: expected 19/19 "
          "(PETERSEN-RADIAL-EXACT) -- got %d checks, fails: %s, "
          "verdict: %s"
          % ("PASS" if part1_ok else "FAIL", len(CHECKS),
             fails1 or "none", v1))
    rc2, chks2 = _run_part2()
    fails2 = [n for (n, ok) in chks2 if not ok]
    v2 = _LAST2.get("verdict", "")
    part2_ok = (rc2 == 0 and not fails2 and len(chks2) == 16
                and v2 == "SIXTHROOT-SPECTRAL-ONLY")
    print("\n[%s] PART-2 PATTERN GATE: expected 16/16 "
          "(SIXTHROOT-SPECTRAL-ONLY) -- got %d checks, fails: %s, "
          "verdict: %s"
          % ("PASS" if part2_ok else "FAIL", len(chks2),
             fails2 or "none", v2))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- PETERSEN-RADIAL-EXACT + "
          "SIXTHROOT-SPECTRAL-ONLY: the K5 edge machine is exact (the "
          "charge X unique, the decuple 3_{-4}+6_{+1}+1_{+6} == the "
          "certified v774 table, Petersen SRG(10,3,0,1) with Aut = S5, "
          "shells (1,3,6) charge-pure, the flavor hexagon = the "
          "distance-2 shell, equitable quotient with hypercharge "
          "eigenvector (6,-4,1) -> -2, spec(P^6) == the deployed "
          "transport spectrum exactly; the 10-dim multiplicity reading "
          "x5 = g_car / x4 = |mu4| stays an [H neu] prediction); B is "
          "the unique symmetric doubly stochastic PSD sixth root in the "
          "corpus basis, B^6 carries the deployed spectrum exactly but "
          "is bit-equal to NO deployed corpus matrix (GL(3,Q)-conjugate "
          "to v486's M^6 and the cusp-diagonal form) -- the corpus "
          "freezes the spectrum, not the basis.  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
