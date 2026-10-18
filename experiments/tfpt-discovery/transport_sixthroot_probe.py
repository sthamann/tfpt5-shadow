#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""transport_sixthroot_probe -- TRANSPORT.SIXTHROOT.01 (Arf compiler
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
    print("Verdikt-Enum: %s" % verdict)
    print("Laufzeit: %.1f s" % (time.time() - T0))
    print("ALLE CHECKS BESTANDEN" if n_pass == n_all
          else "CHECKS FEHLGESCHLAGEN")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
