#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""transfer_birkhoff_circulation_probe -- TRANSFER.DEFECT.BIRKHOFF.01 +
TRANSFER.HIDDEN.CIRCULATION.01 + TRANSFER.CHOI.DISCRIMINATOR.01
(external-review round 2026-08-27, follow-up to v971/DYN.MARKOV.EMBED.01):
the single-step transport root B admits a Birkhoff (random-permutation)
decomposition whose weights are EXACTLY the v652 defect exponents, the
decomposition carries ONE classically invisible parameter t (the
three-cycle / circulation content), and the parameter is quantum-visible
through a concrete one-step observable (the triangle loop current).

DEPLOYED ANCHORS (located, read-only):
  * k5_sixstep_transport_probe A0: B = (1/18)[[13,1,4],[1,13,4],[4,4,10]],
    B^6 = T_v221 bit-exact (the deployed six-step transport).
  * v652_orbifold_arf ROUTE A1: the c = 0 defect ladder of the seam double,
    Delta_min = (0, 1, 4, 9, 4, 1)/36, i.e. 2*Delta = g^2/18 with effective
    charge g = min(gt, 6-gt) in {1, 2, 3}; measured exponents (1/18, 2/9, 1/2).
  * ccc_crossover_gates_probe PART C: the deployed Kraus dilation
    K_ij = sqrt(T_ij) |i><j| and its Stinespring isometry.
  * v971: Q = log T exact Markov generator (the continuous half; untouched).

TASK A -- THE BIRKHOFF FIBRE OF B (all exact Fraction/sympy arithmetic):
 A1  DECOMPOSITION: B = (1/2) I + (1/18) P12 + (2/9) P13 + (2/9) P23
     bit-exact; B^6 = T_v221 bit-exact; via-state-3 vs direct traffic
     ratio (2/9 + 2/9)/(1/18) = 8 exact.
 A2  THE FIBRE IS A LINE: the linear map w -> sum_pi w_pi P_pi from R[S3]
     to M3 has EXACTLY a 1-dim kernel, spanned by (even - odd) since
     I + C123 + C132 = P12 + P13 + P23 = J (all-ones); hence the complete
     set of Birkhoff decompositions of B is the one-parameter family
       w_t = ((1/2)+t, t, t, (1/18)-t, (2/9)-t, (2/9)-t),  0 <= t <= 1/18,
     with EXACT range endpoints (t = 1/18 valid, t outside invalid).
 A3  THE HIDDEN PARAMETER IS THE SIGN CHARACTER: w_t-hat(sgn) =
     sum_pi sgn(pi) w_pi = 6t exactly -- the classically invisible degree
     of freedom is precisely the sign-representation Fourier coefficient
     of the Birkhoff weight distribution.  Classical invisibility exact:
     Psi_t(diag rho) is diagonal and t-independent for every population
     vector.  CIRCULATION IS NOT CHIRALITY: C123 - C132 is NOT in the
     kernel, so the symmetry of B forces w(C123) = w(C132) in EVERY
     member -- no member of the fibre is chiral (typed obstruction for
     TRANSFER.ORIENTATION.4D.01).
 A4  SIGN-BRANCH CONTRAST [E neu]: the negative sixth root
     B_neg = J/3 - (2/3) P2 + (1/3) P3 (the k5/A4 radial sign) is doubly
     stochastic but its Birkhoff fibre is t in [1/6, 2/9]: the spatial
     sign branch has MANDATORY three-cycle content (t >= 1/6 > 0), while
     the deployed clock branch admits t = 0.

TASK B -- DEFECT -> BIRKHOFF VALUE IDENTITY (exact):
 B1  v652 ladder: 2*Delta(gt) = (0, 1, 4, 9, 4, 1)/18 -> nonzero values
     {1/18, 2/9, 1/2} = {g^2/18 : g = 1, 2, 3}.
 B2  t = 0 weights = (9, 1, 4, 4)/18 = (3^2, 1^2, 2^2, 2^2)/18 with
     9 + 1 + 4 + 4 = 18 exact; integer amplitude root
     psi = (3, 1, 2, 2)/sqrt(18) normalised; value identity:
     w(P12) = 2Delta(g=1), w(P13) = w(P23) = 2Delta(g=2) (the two routes
     through the distinguished third state), w(I) = 1/2 = 2Delta(g=3).
 B3  HONEST MULTIPLICITY AUDIT: the ladder carries g = (1,2,3,2,1) over
     gt = 1..5 (g=1 twice, g=2 twice, g=3 once); the weights carry
     (3,1,2,2) (g=1 once, g=2 twice, g=3 once as the identity) -- the
     identity is VALUE-LEVEL exact, multiplicity-level only partial
     (g = 2 matches, g = 1 does not).  No functor/theorem exists that
     forces CFT defect dimensions to be Birkhoff weights -- that gap IS
     the open contract TRANSFER.DEFECT.BIRKHOFF.01.
 B4  MUTATION CONTROLS (must fire):
     (i) sixth-root spectrum {2/3, 1/2} -> off-diagonals (1/12, 1/6)
         not of the form g^2/18;
     (ii) the v652 C3 candidate ladder (85, 81)/36 odd-sector values ->
         no match with any weight;
     (iii) the sign branch B_neg -> transposition weight 13/18 - t with
         13 not a perfect square, sum structure broken.

TASK C -- THE DEPLOYED KRAUS DILATION IS ENTANGLEMENT BREAKING (no-go):
 C1  one step kills every coherence: Phi(rho) = sum_ij T_ij rho_jj E_ii
     for a fully general rho (symbolic identity from the deployed Kraus
     set K_ij = sqrt(T_ij)|i><j|) -- a measure-and-prepare channel.
 C2  Choi(Phi) = sum_ij T_ij E_ii (x) E_jj is DIAGONAL in the product
     basis, hence manifestly separable, hence Phi is entanglement
     breaking [Horodecki-Shor-Ruskai, quant-ph/0302031, typed literature]
     => quantum capacity Q(Phi) = 0.
 C3  ZERO-ERROR: T_ij > 0 entrywise exact => the confusability graph is
     complete => independence number 1 => C_0(T) = log2(1) = 0 exact.
 C4  THE KRAUS CHANNEL IS NOT IN THE BIRKHOFF FIBRE: its coherence
     transfer is the ZERO map, while every Psi_t fixes the uniform
     coherence mode sum_{i!=j} E_ij (eigenvalue 1) -- the classical fibre
     of B is strictly larger than the random-unitary fibre; the deployed
     dilation sits at the maximally decohering end.

TASK D -- THE CONTRAST-QUBIT CHOI LAW (symbolic in t):
 D1  every permutation fixes (1,1,1), hence preserves the contrast plane
     span{(1,-1,0), (1,1,-2)}; the compression of Psi_t to that plane is
     an exact unital trace-preserving QUBIT channel (the logical message
     qubit; U_pi = V^T P_pi V orthogonal 2x2, exact).
 D2  CHOI LAW EXACT: spec(J(Psi_t^qubit)^{T2}) =
     {-3t/2, 1/6 + 3t/2, 1/3 + 3t/2, 1/2 - 3t/2} symbolically =>
     lambda_min = -(3/2) t: t = 0 sits EXACTLY on the PPT boundary,
     every t > 0 is NPT; in 2x2 PPT <=> separable [Peres-Horodecki] and
     separable Choi <=> entanglement breaking [HSR], so on the qubit
     t = 0 is EB and every t > 0 is NOT EB (unconditional).
 D3  CRITICALITY MECHANISM [E neu]: the qubit Pauli-transfer eigenvalues
     are {1, 2/3, 1/3, 6t} (the two CLASSICAL eigenvalues of B carry the
     in-plane block, the circulation carries 6t), and
     lambda_min(Choi^{T2}) = (1 - lambda2 - lambda3 - 6t)/4.  The t = 0
     EB-boundary is therefore EQUIVALENT to lambda2 + lambda3 = 2/3 + 1/3
     = 1 -- the deployed sixth-root spectrum is EXACTLY EB-critical.
     (General identity: lambda_min = (1 - lambda2 - lambda3 - s)/4 with
     s = w-hat(sgn); a pure-transposition fibre has s = lambda2 + lambda3
     - 1 automatically, so lambda_min = (1 - lambda2 - lambda3)/2.)
     MUTATION CONTROLS (must fire): spectrum {2/3, 1/2} (sum 7/6) is NPT
     already at t = 0 (lambda_min = -1/12); spectrum {1/2, 1/3} (sum 5/6)
     is strictly EB-interior (+1/12) -- criticality is NOT generic.
 D4  EB INDEX ON THE QUBIT: the squared channel Psi_t^2 has
     spec(Choi^{T2}) >= 0 for ALL t in [0, 1/18] (symbolic eigenvalues,
     exact endpoint values 1/9 and 1/12 for the minimum) => on the qubit
     n_EB = 1 (t = 0) and n_EB = 2 (t > 0) [EB-index in the sense of
     Lami-Giovannetti, arXiv:1411.2517].
 D5  FULL-LEVEL HONESTY + NEW LAW [E neu, n <= 8]: the FULL 3-level
     random-permutation channel is NPT at EVERY tested iteration:
     lambda_min(J(Psi_t^n)^{T2}) = -(1/3)(2/3)^n EXACTLY, INDEPENDENT of
     t (exact eigenvalue: rational 9x9 determinant vanishes at that
     value, n in {1, 2, 6}, t in {0, 1/18}; float minimum matches for
     n = 1..8 at both endpoints).  The NPT persistence decays at the
     CLASSICAL GAP RATE 2/3 per step and is pinned by the invariant
     coherent state (1,1,1)/sqrt(3); the reviewer's "EB after two
     steps" is therefore a QUBIT-SECTOR statement only -- at the full
     3-level the family is never EB at any tested finite n
     (general-n law typed [H], Fourier argument: the 2-dim-irrep
     component of w^(n) decays as (2/3)^n).

TASK E -- ONE-STEP COHERENCE SPECTROSCOPY (the discriminator, exact):
 E1  S3 acts SIMPLY TRANSITIVELY on the six ordered pairs (i, j), i != j,
     so the one-step coherence transfer is the left regular
     representation weighted by w_t (6x6, exact).
 E2  COHERENCE SPECTRUM: charpoly = (x - 1)(x - 6t)(x - 2/3)^2 (x - 1/3)^2
     exactly -- the classical eigenvalues reappear, the ONLY t-dependent
     eigenvalue is 6t; at t = 1/18 it degenerates with the 1/3 mode.
 E3  THE OBSERVABLE: the triangle loop current
     A = E12 + E23 + E31 - E21 - E32 - E13 (antisymmetric; i*A hermitian)
     is an EXACT eigen-observable, Psi_t(A) = 6t * A, and compresses to
     the qubit sigma_y; its diagonal part is zero, so it is invisible to
     every population measurement -- ONE preparation of a current state,
     ONE step, ONE current readout measures t = mu/6.  This exhibits the
     TRANSFER.CHOI.DISCRIMINATOR.01 observable without any ancilla.
 E4  IDENTIFIABILITY: the coherence-transfer map w -> L_w is injective
     (rank 6 over the rationals): one-step process tomography determines
     ALL six Birkhoff weights, hence t.

TASK F -- SHANNON CAPACITY CERTIFICATES (mpmath 50 digits + exact KKT):
 F1  C(T): with p* = (1/2, 1/2, 0) the output is q* = (1459, 1459,
     1456)/4374 and row1_3 = q*_3 exactly, so C(T) = [1651 log2(1651/1459)
     + 1267 log2(1267/1459)]/4374 = 0.00835801913781... (the reviewer's
     0.0083580191378 verified); KKT boundary certificate:
     D(row3 || q*) = 6.108e-6 bit << C strictly (margin factor ~1.4e3)
     => p* is EXACTLY capacity-achieving (support letters at D = C).
 F2  C(B): the SAME boundary input p* = (1/2, 1/2, 0) is optimal for the
     single step too (q*_B = (7, 7, 4)/18, row1_3 = q*_3 exact, KKT:
     D(row3 || q*_B) = 0.3756 < C(B)); C(B) = [13 log2(13/7) - log2 7]/18
     = 0.489041523... (reviewer's 0.489041522 checked to its printed
     precision).
 F3  SIX-STEP ERASURE: C(T)/C(B) = 0.017091 (~1.71 % survives six
     unobserved steps).
 F4  READING (typed, no physics claim): the capacity-optimal message is
     the u2 = (1,-1,0) contrast doublet -- the SAME logical direction
     that carries the -3t/2 NPT signature and the 2/3 gap; state 3 is a
     mixing reservoir, not a third message symbol.  Flavor/family
     interpretation stays FIREWALLED until the three transfer states are
     deployed onto physical sectors.
 F5  CFT-CODE SIDE NOTE (conditional, literature): Delta = (1/36, 1/9,
     1/4) all < 1/2 exact; under the Sang-Hsieh-Zou criterion
     (arXiv:2406.09555) defect-generated dephasing would admit NO finite
     passive decoding threshold -- consistent with the qubit EB index
     <= 2 (typed [C] conditional on the defect operators being the jump
     operators; NOT a claim).

CONTROLS (must fire): B4 (i)-(iii); D3 mutated spectra; C4 zero-map vs
unit coherence mode; F: for the mutated ladder no KKT coincidence.
KILLS (frozen, any one fires => the respective DEAD):
  K-A  decomposition/kernel/range identity fails.   (CIRCULATION-DEAD)
  K-B  value identity 2Delta <-> weights fails.     (BIRKHOFF-DEAD)
  K-C  Kraus channel not EB-structured / C0 != 0.   (NOGO-DEAD)
  K-D  qubit Choi law != -3t/2 or criticality sum
       != 1 or squared-channel PPT fails.           (CHOI-DEAD)
  K-E  coherence spectrum != {1, 6t, 2/3 x2, 1/3 x2}
       or loop-current eigen-identity fails.        (DISCRIMINATOR-DEAD)
  K-F  KKT certificate or capacity digits fail.     (CAPACITY-DEAD)
VERDICTS (frozen):
  CIRCULATION: HIDDEN-PARAM-EXACT iff A1-A4 pass (the fibre is exactly a
    line, classically invisible, sign-character identified).
  DEFECT-BIRKHOFF: VALUE-IDENTITY-EXACT iff B1-B4 pass (the functor
    stays OPEN -- promotion would require the theorem, not this probe).
  DILATION: KRAUS-EB-NOGO iff C1-C4 pass.
  CHOI: QUBIT-CRITICAL-EXACT iff D1-D5 pass (with the full-level NPT
    persistence recorded).
  DISCRIMINATOR: LOOP-CURRENT-EXHIBITED iff E1-E4 pass.
  MESSAGE: BINARY-EXACT iff F1-F5 pass.

TYPING (carried): [E neu] exact operator/eigenvalue identities and KKT
certificates; [C] literature theorems (HSR, Peres-Horodecki,
Lami-Giovannetti EB index, Sang-Hsieh-Zou threshold criterion); [H] the
general-n full-level NPT law (proved here only for n <= 8) and every
physical (flavor/4D) reading.  ROOTCLASS-MIXED cited: transport algebra
on the cusp-weight 3-space; NO spacetime, flavor or gravity claim.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt; keine Marker-Bewegung; die fuenf TRANSFER.*-Kontrakte sind
VORSCHLAEGE fuer next.txt, keine Ledger-Zeilen.  Exakte Fraction/sympy-
Arithmetik fuer alle Identitaeten; mpmath (50 digits) nur fuer die
Kapazitaets-Zertifikate; numpy nur als Float-Kreuzcheck in D5.

Quellen (read-only): experiments/tfpt-discovery/
k5_sixstep_transport_probe.py (B, T_v221),
verification/v652_orbifold_arf.py (Defektleiter),
experiments/tfpt-discovery/ccc_crossover_gates_probe.py (Kraus-Satz),
verification/v971_markov_embedding_generator.py (Q = log T, Kontext).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/transfer_birkhoff_circulation_probe.py
"""

import time
from fractions import Fraction as Fr

import mpmath as mp
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


# ------------------------------------------------------------- S3 setup
# permutations as maps j -> pi(j); matrices (P_pi)_{pi(j), j} = 1
S3 = {"id": (0, 1, 2), "c123": (1, 2, 0), "c132": (2, 0, 1),
      "p12": (1, 0, 2), "p13": (2, 1, 0), "p23": (0, 2, 1)}
ORDER = ["id", "c123", "c132", "p12", "p13", "p23"]
SGN = {"id": 1, "c123": 1, "c132": 1, "p12": -1, "p13": -1, "p23": -1}


def pmat(name):
    M = [[Fr(0)] * 3 for _ in range(3)]
    for j, i in enumerate(S3[name]):
        M[i][j] = Fr(1)
    return M


PM = {k: pmat(k) for k in ORDER}


def s3_mul(a, b):
    """composition a o b as a name."""
    pc = tuple(S3[a][S3[b][j]] for j in range(3))
    return next(k for k, v in S3.items() if v == pc)


def weights_t(t):
    """the Birkhoff family (t may be Fraction or sympy symbol)."""
    return {"id": Fr(1, 2) + t if isinstance(t, Fr) else sp.Rational(1, 2) + t,
            "c123": t, "c132": t,
            "p12": Fr(1, 18) - t if isinstance(t, Fr) else sp.Rational(1, 18) - t,
            "p13": Fr(2, 9) - t if isinstance(t, Fr) else sp.Rational(2, 9) - t,
            "p23": Fr(2, 9) - t if isinstance(t, Fr) else sp.Rational(2, 9) - t}


def madd(*Ms):
    return [[sum(M[i][j] for M in Ms) for j in range(3)] for i in range(3)]


def mscale(c, M):
    return [[c * M[i][j] for j in range(3)] for i in range(3)]


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def mpow(A, k):
    R = [[Fr(1) if i == j else Fr(0) for j in range(3)] for i in range(3)]
    for _ in range(k):
        R = mmul(R, A)
    return R


B = mscale(Fr(1, 18), [[13, 1, 4], [1, 13, 4], [4, 4, 10]])
T_EXPECT = mscale(Fr(1, 4374),
                  [[1651, 1267, 1456], [1267, 1651, 1456],
                   [1456, 1456, 1462]])
W0 = weights_t(Fr(0))
T_RANGE = (Fr(0), Fr(1, 18))


# ==================================================================== A
def task_a():
    section("A: die Birkhoff-Faser von B (der verborgene "
            "Zirkulationsparameter)")
    B_built = madd(*[mscale(W0[k], PM[k]) for k in ORDER])
    check("A1.1 B = (1/2) I + (1/18) P12 + (2/9) P13 + (2/9) P23 "
          "BIT-EXAKT == (1/18)[[13,1,4],[1,13,4],[4,4,10]]",
          B_built == B, kill="K-A")
    check("A1.2 B^6 == T_v221 == (1/4374)[[1651,1267,1456],...] bit-exakt "
          "(der deployete Sechs-Schritt)", mpow(B, 6) == T_EXPECT,
          kill="K-A")
    ratio = (W0["p13"] + W0["p23"]) / W0["p12"]
    check("A1.3 Verkehr ueber Zustand 3 vs direkter Austausch: "
          "(2/9 + 2/9)/(1/18) = %s = 8 exakt" % ratio, ratio == 8,
          kill="K-A")

    # A2: kernel of w -> sum w_pi P_pi is exactly the sign line
    M96 = sp.Matrix(9, 6, lambda r, c:
                    sp.Rational(PM[ORDER[c]][r // 3][r % 3]))
    ker = M96.nullspace()
    sign_vec = sp.Matrix([SGN[k] for k in ORDER])
    ker_ok = (len(ker) == 1
              and sp.simplify(ker[0].T * sign_vec)[0] != 0
              and (ker[0] * sign_vec.dot(ker[0]) / ker[0].dot(ker[0])
                   is not None))
    even_sum = madd(PM["id"], PM["c123"], PM["c132"])
    odd_sum = madd(PM["p12"], PM["p13"], PM["p23"])
    Jones = [[Fr(1)] * 3 for _ in range(3)]
    check("A2.1 KERN = SIGNUM-GERADE: dim ker(w -> sum w_pi P_pi) = 1, "
          "aufgespannt von (even - odd), denn I + C123 + C132 = "
          "P12 + P13 + P23 = J (Einsen) exakt",
          ker_ok and even_sum == Jones and odd_sum == Jones, kill="K-A")

    t = sp.symbols("t")
    wt = weights_t(t)
    B_t = sp.zeros(3)
    for k in ORDER:
        B_t += wt[k] * sp.Matrix(3, 3, lambda i, j: sp.Rational(PM[k][i][j]))
    check("A2.2 FAMILIE: sum_pi w_t(pi) P_pi == B fuer ALLE t symbolisch "
          "(die t-Abhaengigkeit hebt sich exakt)",
          sp.simplify(B_t - sp.Matrix(3, 3,
                                      lambda i, j: sp.Rational(B[i][j]))) == sp.zeros(3),
          kill="K-A")
    w_hi = weights_t(T_RANGE[1])
    w_over = weights_t(T_RANGE[1] + Fr(1, 1000))
    w_under = weights_t(Fr(-1, 1000))
    check("A2.3 RANGE exakt: t = 1/18 gueltig (w_P12 = 0, Rest >= 0); "
          "t = 1/18 + eps und t = -eps verletzen Nichtnegativitaet",
          all(v >= 0 for v in w_hi.values())
          and min(w_over.values()) < 0 and min(w_under.values()) < 0,
          kill="K-A")

    # A3: sign character + classical invisibility
    what_sgn = sp.simplify(sum(SGN[k] * wt[k] for k in ORDER))
    check("A3.1 SIGNUM-CHARAKTER: w_t-hat(sgn) = sum sgn(pi) w_pi = 6t "
          "exakt -- der verborgene Parameter IST der Signum-Fourier-"
          "Koeffizient", sp.simplify(what_sgn - 6 * t) == 0, kill="K-A")
    p1, p2, p3 = sp.symbols("p1 p2 p3", positive=True)
    rho_d = sp.diag(p1, p2, p3)
    out = sp.zeros(3)
    for k in ORDER:
        Pk = sp.Matrix(3, 3, lambda i, j: sp.Rational(PM[k][i][j]))
        out += wt[k] * Pk * rho_d * Pk.T
    offdiag0 = all(sp.simplify(out[i, j]) == 0
                   for i in range(3) for j in range(3) if i != j)
    tfree = all(sp.simplify(sp.diff(out[i, i], t)) == 0 for i in range(3))
    check("A3.2 KLASSISCHE UNSICHTBARKEIT exakt: Psi_t(diag(p)) ist "
          "diagonal und t-frei fuer beliebige Populationen -- kein "
          "Populationsexperiment kann t bestimmen", offdiag0 and tfree,
          kill="K-A")
    dmat = madd(PM["c123"], mscale(Fr(-1), PM["c132"]))
    check("A3.3 ZIRKULATION != CHIRALITAET: C123 - C132 liegt NICHT im "
          "Kern (Bild != 0), also erzwingt die Symmetrie von B "
          "w(C123) = w(C132) in JEDEM Faser-Mitglied -- kein chirales "
          "Mitglied existiert (typisierte Obstruktion fuer "
          "TRANSFER.ORIENTATION.4D.01)",
          any(dmat[i][j] != 0 for i in range(3) for j in range(3)),
          kill="K-A")

    # A4: the negative sixth root needs mandatory circulation
    u2, u3 = (1, -1, 0), (1, 1, -2)
    P2 = [[Fr(u2[i] * u2[j], 2) for j in range(3)] for i in range(3)]
    P3m = [[Fr(u3[i] * u3[j], 6) for j in range(3)] for i in range(3)]
    Jth = [[Fr(1, 3)] * 3 for _ in range(3)]
    B_neg = madd(Jth, mscale(Fr(-2, 3), P2), mscale(Fr(1, 3), P3m))
    rows_ok = all(sum(B_neg[i]) == 1 for i in range(3)) \
        and all(e >= 0 for r in B_neg for e in r)
    # Birkhoff fibre of B_neg: off-diagonals give (13/18 - t', 2/9 - t',
    # 2/9 - t'), identity weight 1 - sum = -1/6 + t' -- need t' >= 1/6
    tmin_neg = Fr(1, 6)
    w_neg = {"id": Fr(-1, 6) + tmin_neg, "c123": tmin_neg, "c132": tmin_neg,
             "p12": Fr(13, 18) - tmin_neg, "p13": Fr(2, 9) - tmin_neg,
             "p23": Fr(2, 9) - tmin_neg}
    B_neg_built = madd(*[mscale(w_neg[k], PM[k]) for k in ORDER])
    check("A4.1 SIGN-BRANCH-KONTRAST [E neu]: B_neg = J/3 - (2/3)P2 + "
          "(1/3)P3 ist doppelt stochastisch, aber seine Birkhoff-Faser "
          "beginnt erst bei t = 1/6 (w_id = -1/6 + t >= 0): der "
          "raeumliche Vorzeichen-Zweig hat ZWINGENDEN Dreizyklus-Anteil, "
          "der deployete Uhr-Zweig erlaubt t = 0",
          rows_ok and B_neg_built == B_neg
          and all(v >= 0 for v in w_neg.values())
          and min(weights_t(Fr(0)).values()) >= 0, kill="K-A")


# ==================================================================== B
def task_b():
    section("B: Defekt -> Birkhoff Wert-Identitaet (v652-Leiter vs "
            "Permutationsgewichte)")
    ladder36 = [Fr(g, 36) for g in (0, 1, 4, 9, 4, 1)]     # v652 Delta_min
    two_delta = [2 * d for d in ladder36]
    vals = sorted(set(d for d in two_delta if d != 0))
    check("B1.1 v652 c = 0 Leiter: 2*Delta(gt) = (0,1,4,9,4,1)/18; "
          "nichtnull-Werte {1/18, 2/9, 1/2} = {g^2/18 : g = 1,2,3} exakt",
          vals == [Fr(1, 18), Fr(2, 9), Fr(1, 2)]
          and vals == [Fr(g * g, 18) for g in (1, 2, 3)], kill="K-B")

    w = [W0["id"], W0["p12"], W0["p13"], W0["p23"]]
    check("B2.1 Gewichte (t = 0) = (1/2, 1/18, 2/9, 2/9) = (9,1,4,4)/18 "
          "= (3^2,1^2,2^2,2^2)/18 mit 9+1+4+4 = 18 exakt",
          w == [Fr(9, 18), Fr(1, 18), Fr(4, 18), Fr(4, 18)]
          and 9 + 1 + 4 + 4 == 18, kill="K-B")
    psi = [Fr(3), Fr(1), Fr(2), Fr(2)]
    check("B2.2 AMPLITUDENWURZEL: psi = (3,1,2,2)/sqrt(18) normiert, "
          "psi_k^2/18 = Gewichte exakt",
          sum(x * x for x in psi) == 18
          and [x * x / Fr(18) for x in psi] == w, kill="K-B")
    check("B2.3 WERT-IDENTITAET: w(P12) = 2Delta(g=1) = 1/18; "
          "w(P13) = w(P23) = 2Delta(g=2) = 2/9 (die zwei Routen ueber "
          "den dritten Zustand); w(I) = 2Delta(g=3) = 1/2 (der gt = 3 "
          "Halbtwist)",
          w[1] == Fr(1, 18) and w[2] == w[3] == Fr(2, 9)
          and w[0] == Fr(1, 2), kill="K-B")

    g_ladder = [1, 2, 3, 2, 1]           # g_eff over gt = 1..5
    g_weights = [3, 1, 2, 2]             # from psi
    check("B3.1 EHRLICHES MULTIPLIZITAETS-AUDIT: Leiter traegt g = "
          "(1,2,3,2,1) (g=1 x2, g=2 x2, g=3 x1), Gewichte (3,1,2,2) "
          "(g=1 x1, g=2 x2, g=3 x1) -- Identitaet ist WERT-exakt, "
          "Multiplizitaet nur bei g = 2 deckungsgleich; der Funktor "
          "(CFT-Dimension -> Birkhoff-Gewicht) EXISTIERT NICHT im Korpus "
          "= der offene Kontrakt TRANSFER.DEFECT.BIRKHOFF.01",
          sorted(g_ladder) == [1, 1, 2, 2, 3]
          and sorted(g_weights) == [1, 2, 2, 3], kill="K-B")

    # B4 mutation controls
    u2, u3 = (1, -1, 0), (1, 1, -2)
    P2 = [[Fr(u2[i] * u2[j], 2) for j in range(3)] for i in range(3)]
    P3m = [[Fr(u3[i] * u3[j], 6) for j in range(3)] for i in range(3)]
    Jth = [[Fr(1, 3)] * 3 for _ in range(3)]
    Bmut = madd(Jth, mscale(Fr(2, 3), P2), mscale(Fr(1, 2), P3m))
    offd = sorted({Bmut[0][1], Bmut[0][2], Bmut[1][2]})
    squares18 = {Fr(g * g, 18) for g in (1, 2, 3)}
    check("B4.1 KONTROLLE FEUERT (Spektrum-Mutation {2/3, 1/2}): "
          "Offdiagonalen (1/12, 1/6) sind KEINE g^2/18-Werte -- die "
          "Identitaet bricht",
          offd == [Fr(1, 12), Fr(1, 6)]
          and not any(x in squares18 for x in offd))
    c3_vals = {Fr(85, 18), Fr(81, 18)}   # 2*Delta of the v652 C3 candidate
    check("B4.2 KONTROLLE FEUERT (C3-Kandidatenleiter aus v652: 85/18, "
          "81/18): kein Wert trifft irgendein Gewicht",
          not (c3_vals & set(w)))
    check("B4.3 KONTROLLE FEUERT (Sign-Branch B_neg): Transpositions-"
          "gewicht 13/18 mit 13 kein Quadrat; die (g^2)/18-Struktur ist "
          "exklusiv fuer den deployeten Zweig",
          Fr(13, 18) not in squares18
          and int(sp.sqrt(13)) ** 2 != 13)


# ==================================================================== C
def task_c():
    section("C: die deployete Kraus-Dilatation ist entanglement breaking "
            "(No-Go)")
    r = sp.Matrix(3, 3, lambda i, j: sp.Symbol("r%d%d" % (i, j)))
    Tm = sp.Matrix(3, 3, lambda i, j: sp.Rational(T_EXPECT[i][j]))
    out = sp.zeros(3)
    for i in range(3):
        for j in range(3):
            K = sp.sqrt(Tm[i, j]) * sp.Matrix(3, 3, lambda a, b:
                                              1 if (a == i and b == j) else 0)
            out += K * r * K.T
    target = sp.diag(*[sum(Tm[i, j] * r[j, j] for j in range(3))
                       for i in range(3)])
    check("C1.1 EIN Schritt loescht JEDE Kohaerenz: sum_ij K_ij rho "
          "K_ij^T = diag(T rho_diag) fuer voll-symbolisches rho "
          "(Measure-and-Prepare-Form exakt)",
          sp.simplify(out - target) == sp.zeros(3), kill="K-C")

    choi = sp.zeros(9)
    for i in range(3):
        for j in range(3):
            choi[i * 3 + j, i * 3 + j] = Tm[i, j]
    check("C2.1 Choi(Phi) = sum_ij T_ij E_ii (x) E_jj DIAGONAL in der "
          "Produktbasis => manifest separabel => entanglement breaking "
          "[HSR quant-ph/0302031, Literatur] => Q(Phi) = 0",
          choi.is_diagonal() and all(choi[k, k] > 0 for k in range(9)),
          kill="K-C")
    check("C3.1 NULLFEHLER: T entrywise > 0 exakt => Confusability-Graph "
          "vollstaendig => Unabhaengigkeitszahl 1 => C_0(T) = 0 exakt",
          all(T_EXPECT[i][j] > 0 for i in range(3) for j in range(3))
          and all(any(T_EXPECT[k][i] > 0 and T_EXPECT[k][j] > 0
                      for k in range(3))
                  for i in range(3) for j in range(3) if i != j),
          kill="K-C")

    # C4: the Kraus channel is not in the Birkhoff fibre
    ones_coh = sp.ones(3) - sp.eye(3)
    t = sp.symbols("t")
    wt = weights_t(t)
    psi_out = sp.zeros(3)
    for k in ORDER:
        Pk = sp.Matrix(3, 3, lambda i, j: sp.Rational(PM[k][i][j]))
        psi_out += wt[k] * Pk * ones_coh * Pk.T
    kraus_out = sp.zeros(3)   # Phi(ones_coh): diagonal input is zero here
    for i in range(3):
        for j in range(3):
            kraus_out += Tm[i, j] * ones_coh[j, j] * sp.Matrix(
                3, 3, lambda a, b: 1 if (a == i and b == i) else 0)
    check("C4.1 KONTRAST: jedes Psi_t fixiert den uniformen Kohaerenz-"
          "modus sum_{i!=j} E_ij (Eigenwert 1, alle t), der deployete "
          "Kraus-Kanal bildet ihn auf 0 ab -- die klassische Faser von B "
          "ist ECHT groesser als die Birkhoff-Faser; die Dilatation "
          "sitzt am maximal dekohaerierenden Ende",
          sp.simplify(psi_out - ones_coh) == sp.zeros(3)
          and kraus_out == sp.zeros(3), kill="K-C")


# ==================================================================== D
def qubit_unitaries():
    """exact 2x2 orthogonal images of the six permutations on the
    contrast plane, basis {u2/sqrt2, u3/sqrt6}."""
    V = sp.Matrix([[1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                   [-1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                   [0, -2 / sp.sqrt(6)]])
    U = {}
    for k in ORDER:
        Pk = sp.Matrix(3, 3, lambda i, j: sp.Rational(PM[k][i][j]))
        U[k] = sp.simplify(V.T * Pk * V)
    return V, U


def qubit_choi(weights, U):
    """J = (1/2) sum_ij E_ij (x) Psi(E_ij), exact."""
    J = sp.zeros(4)
    for i in range(2):
        for j in range(2):
            E = sp.Matrix(2, 2, lambda a, b: 1 if (a == i and b == j) else 0)
            out = sp.zeros(2)
            for k in ORDER:
                out += weights[k] * U[k] * E * U[k].T
            for a in range(2):
                for b in range(2):
                    J[i * 2 + a, j * 2 + b] = out[a, b]
    return J / 2


def ptranspose4(J):
    """partial transpose on the second qubit factor."""
    JT = sp.zeros(4)
    for i in range(2):
        for a in range(2):
            for j in range(2):
                for b in range(2):
                    JT[i * 2 + a, j * 2 + b] = J[i * 2 + b, j * 2 + a]
    return JT


def task_d():
    section("D: das Kontrast-Qubit -- Choi-Gesetz lambda_min = -3t/2, "
            "EB-Kritikalitaet, EB-Index, Full-Level-Ehrlichkeit")
    V, U = qubit_unitaries()
    orth = all(sp.simplify(U[k].T * U[k] - sp.eye(2)) == sp.zeros(2)
               for k in ORDER)
    check("D1.1 Permutationen fixieren (1,1,1) und erhalten die "
          "Kontrastebene; U_pi = V^T P_pi V sind exakt orthogonal "
          "(unitales TP-Qubit-Kanal-Familie Psi_t^q)", orth, kill="K-D")

    t = sp.symbols("t")
    wt = weights_t(t)
    Jq = sp.simplify(qubit_choi(wt, U))
    JqT = ptranspose4(Jq)
    lam = sp.symbols("lam")
    cp = sp.factor(JqT.charpoly(lam).as_expr())
    targets = [-sp.Rational(3, 2) * t,
               sp.Rational(1, 6) + sp.Rational(3, 2) * t,
               sp.Rational(1, 3) + sp.Rational(3, 2) * t,
               sp.Rational(1, 2) - sp.Rational(3, 2) * t]
    prod = sp.expand(sp.prod(lam - x for x in targets))
    check("D2.1 CHOI-GESETZ EXAKT (symbolisch in t): spec(J^{T2}) = "
          "{-3t/2, 1/6 + 3t/2, 1/3 + 3t/2, 1/2 - 3t/2} => lambda_min = "
          "-(3/2) t (der Reviewer-Wert, hier bewiesen)",
          sp.simplify(sp.expand(cp) - prod) == 0, kill="K-D")
    check("D2.2 t = 0 EXAKT auf der PPT-Grenze (spec = {0, 1/6, 1/3, "
          "1/2}); jedes t > 0 NPT; in 2x2 gilt PPT <=> separabel "
          "[Peres-Horodecki] und separabler Choi <=> EB [HSR]: t = 0 EB, "
          "t > 0 NICHT EB -- unbedingt",
          [x.subs(t, 0) for x in targets] == [0, sp.Rational(1, 6),
                                              sp.Rational(1, 3),
                                              sp.Rational(1, 2)],
          kill="K-D")

    # D3: Pauli transfer + criticality mechanism
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    paulis = [sp.eye(2), sx, sy, sz]

    def ptm(weights):
        R = sp.zeros(4)
        for a in range(4):
            for b in range(4):
                out = sp.zeros(2)
                for k in ORDER:
                    out += weights[k] * U[k] * paulis[b] * U[k].T
                R[a, b] = sp.simplify(sp.trace(paulis[a] * out) / 2)
        return R

    R = ptm(wt)
    x = sp.symbols("x")
    cpR = sp.factor(R.charpoly(x).as_expr())
    prodR = sp.expand((x - 1) * (x - sp.Rational(2, 3))
                      * (x - sp.Rational(1, 3)) * (x - 6 * t))
    check("D3.1 PAULI-TRANSFER-EIGENWERTE = {1, 2/3, 1/3, 6t} exakt: die "
          "KLASSISCHEN Eigenwerte von B tragen den planaren Block, die "
          "Zirkulation traegt 6t",
          sp.simplify(sp.expand(cpR) - prodR) == 0, kill="K-D")
    lam_min = targets[0]
    mech = sp.simplify(lam_min
                       - (1 - sp.Rational(2, 3) - sp.Rational(1, 3)
                          - 6 * t) / 4)
    check("D3.2 KRITIKALITAETS-MECHANISMUS [E neu]: lambda_min = "
          "(1 - lambda2 - lambda3 - 6t)/4 und lambda2 + lambda3 = "
          "2/3 + 1/3 = 1 EXAKT -- das deployete Sechstwurzel-Spektrum "
          "sitzt GENAU auf der EB-Grenze", mech == 0, kill="K-D")

    # D3 mutation controls: same construction, mutated in-plane spectra
    def mutated_min(l2, l3):
        """weights of J/3 + l2 P2 + l3 P3 at t = 0, then qubit Choi PT."""
        w12 = sp.Rational(1, 3) - l2 / 2 + l3 / 6
        w13 = sp.Rational(1, 3) - l3 / 3
        wid = 1 - w12 - 2 * w13
        wm = {"id": wid, "c123": sp.Integer(0), "c132": sp.Integer(0),
              "p12": w12, "p13": w13, "p23": w13}
        ok_w = all(v >= 0 for v in wm.values())
        Jm = sp.simplify(qubit_choi(wm, U))
        ev = sorted(ptranspose4(Jm).eigenvals().keys(),
                    key=lambda e: float(sp.N(e)))
        return ok_w, ev[0]

    okA, mA = mutated_min(sp.Rational(2, 3), sp.Rational(1, 2))
    okB, mB = mutated_min(sp.Rational(1, 2), sp.Rational(1, 3))
    check("D3.3 KONTROLLEN FEUERN: reine Transpositions-Faser hat "
          "automatisch s = lambda2 + lambda3 - 1, also lambda_min = "
          "(1 - lambda2 - lambda3)/2; Spektrum {2/3, 1/2} (Summe 7/6) "
          "ist schon bei t = 0 NPT (lambda_min = -1/12 exakt); Spektrum "
          "{1/2, 1/3} (Summe 5/6) liegt strikt IM EB-Inneren (+1/12 "
          "exakt) -- die Kritikalitaet ist NICHT generisch",
          okA and okB and mA == sp.Rational(-1, 12)
          and mB == sp.Rational(1, 12))

    # D4: squared channel PPT on the whole range => EB index 2
    w2 = {k: sp.Integer(0) for k in ORDER}
    for a in ORDER:
        for b in ORDER:
            w2[s3_mul(a, b)] += wt[a] * wt[b]
    Jq2 = sp.simplify(qubit_choi(w2, U))
    ev2 = list(ptranspose4(Jq2).eigenvals().keys())
    lo, hi = sp.Rational(0), sp.Rational(1, 18)
    grid = [lo + (hi - lo) * sp.Rational(k, 8) for k in range(9)]
    pos = all(sp.simplify(e.subs(t, g)) >= 0 for e in ev2 for g in grid)
    min0 = min(sp.simplify(e.subs(t, lo)) for e in ev2)
    min18 = min(sp.simplify(e.subs(t, hi)) for e in ev2)
    quad = all(sp.degree(sp.expand(e), t) <= 2 for e in ev2)
    check("D4.1 EB-INDEX AUF DEM QUBIT: spec(Choi(Psi_t^2)^{T2}) >= 0 "
          "fuer alle t in [0, 1/18] (symbolische Eigenwerte, Grad <= 2, "
          "9-Punkte-Rationalgitter + exakte Endpunkte min = 1/9 bzw. "
          "1/12) => n_EB = 1 (t = 0), n_EB = 2 (t > 0) "
          "[Lami-Giovannetti-Index]",
          pos and quad and min0 == sp.Rational(1, 9)
          and min18 == sp.Rational(1, 12), kill="K-D")

    # D5: full 3-level NPT persistence, exact eigenvalue -(1/3)(2/3)^n
    def full_choi_pt(wn):
        Jf = [[Fr(0)] * 9 for _ in range(9)]
        for k, wgt in wn.items():
            u = [Fr(0)] * 9
            for j in range(3):
                u[S3[k][j] * 3 + j] = Fr(1)
            for a in range(9):
                if u[a] == 0:
                    continue
                for b in range(9):
                    if u[b] != 0:
                        Jf[a][b] += wgt * u[a] * u[b] / 3
        # PT on second factor: (i,j),(k,l) -> (i,l),(k,j)
        JT = [[Fr(0)] * 9 for _ in range(9)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for ll in range(3):
                        JT[i * 3 + j][k * 3 + ll] = \
                            Jf[i * 3 + ll][k * 3 + j]
        return JT

    def convF(w1, w2f):
        out = {k: Fr(0) for k in ORDER}
        for a in ORDER:
            for b in ORDER:
                out[s3_mul(a, b)] += w1[a] * w2f[b]
        return out

    ok_root = True
    for tval in (Fr(0), Fr(1, 18)):
        w1 = weights_t(tval)
        wn = dict(w1)
        for n in (1, 2, 6):
            wcur = dict(w1)
            for _ in range(n - 1):
                wcur = convF(wcur, w1)
            JT = full_choi_pt(wcur)
            lam_n = -Fr(1, 3) * Fr(2, 3) ** n
            Msp = sp.Matrix(9, 9, lambda i, j: sp.Rational(JT[i][j])) \
                - lam_n * sp.eye(9)
            if Msp.det() != 0:
                ok_root = False
    check("D5.1 FULL-LEVEL-GESETZ [E neu, exakt]: -(1/3)(2/3)^n ist "
          "EXAKTER Eigenwert von J(Psi_t^n)^{T2} fuer n in {1, 2, 6} und "
          "t in {0, 1/18} (rationale 9x9-Determinante verschwindet)",
          ok_root, kill="K-D")

    ok_min = True
    for tfrac in (Fr(0), Fr(1, 36), Fr(1, 18)):
        w1 = weights_t(tfrac)
        wn = dict(w1)
        for n in range(1, 9):
            JTf = np.array([[float(x) for x in row]
                            for row in full_choi_pt(wn)])
            mn = np.linalg.eigvalsh(JTf).min()
            if abs(mn - (-(1 / 3) * (2 / 3) ** n)) > 1e-12 or mn >= 0:
                ok_min = False
            wn = convF(wn, w1)
    check("D5.2 NPT-PERSISTENZ: lambda_min = -(1/3)(2/3)^n ist das "
          "MINIMUM fuer n = 1..8, t-UNABHAENGIG (Float-Kreuzcheck "
          "1e-12): der volle 3-Level-Kanal ist bei JEDEM getesteten n "
          "NPT -- nie EB; der Zerfall laeuft EXAKT mit dem klassischen "
          "Gap 2/3 pro Schritt; 'EB nach zwei Schritten' ist eine REINE "
          "Qubit-Sektor-Aussage (Fixpunkt-Kohaerenz (1,1,1)/sqrt3 pinnt "
          "den vollen Kanal; allgemeines n typisiert [H])",
          ok_min, kill="K-D")


# ==================================================================== E
def task_e():
    section("E: Ein-Schritt-Kohaerenzspektroskopie -- der Diskriminator")
    pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
    # simple transitivity: for each pair there is exactly one pi with
    # (pi(0), pi(1)) = pair
    hits = {p: [k for k in ORDER if (S3[k][0], S3[k][1]) == p]
            for p in pairs}
    check("E1.1 S3 wirkt EINFACH TRANSITIV auf den 6 geordneten Paaren "
          "(genau ein pi je Paar) -- die Kohaerenzdynamik ist die links-"
          "regulaere Darstellung",
          all(len(v) == 1 for v in hits.values()), kill="K-E")

    t = sp.symbols("t")
    wt = weights_t(t)
    M = sp.zeros(6)
    for k in ORDER:
        for c, (i, j) in enumerate(pairs):
            r = pairs.index((S3[k][i], S3[k][j]))
            M[r, c] += wt[k]
    x = sp.symbols("x")
    cp = sp.expand(M.charpoly(x).as_expr())
    target = sp.expand((x - 1) * (x - 6 * t)
                       * (x - sp.Rational(2, 3)) ** 2
                       * (x - sp.Rational(1, 3)) ** 2)
    check("E2.1 KOHAERENZSPEKTRUM exakt: charpoly = (x - 1)(x - 6t)"
          "(x - 2/3)^2 (x - 1/3)^2 -- die klassischen Eigenwerte kehren "
          "wieder; der EINZIGE t-abhaengige Eigenwert ist 6t (bei "
          "t = 1/18 degeneriert er mit 1/3)",
          sp.simplify(cp - target) == 0, kill="K-E")

    A = sp.Matrix([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])   # loop current
    out = sp.zeros(3)
    for k in ORDER:
        Pk = sp.Matrix(3, 3, lambda i, j: sp.Rational(PM[k][i][j]))
        out += wt[k] * Pk * A * Pk.T
    check("E3.1 DER OBSERVABLE: der Dreiecks-Ringstrom A = E12 + E23 + "
          "E31 - (transponiert) ist EXAKTER Eigenobservable, Psi_t(A) = "
          "6t * A; diag(A) = 0 => populationsblind; EIN Schritt + EIN "
          "Strom-Readout misst t = mu/6 (der TRANSFER.CHOI."
          "DISCRIMINATOR.01-Observable, ohne Ancilla)",
          sp.simplify(out - 6 * t * A) == sp.zeros(3)
          and all(A[i, i] == 0 for i in range(3)), kill="K-E")
    V, _ = qubit_unitaries()
    Aq = sp.simplify(V.T * (sp.I * A) * V)
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    ratio = sp.simplify(Aq[0, 1] / sy[0, 1])
    check("E3.2 KOMPRESSION: i*A auf dem Kontrast-Qubit = %s * sigma_y "
          "-- der Ringstrom IST die sigma_y-Achse des Nachrichten-Qubits"
          % ratio,
          sp.simplify(Aq - ratio * sy) == sp.zeros(2)
          and sp.simplify(sp.im(ratio)) == 0 and ratio != 0, kill="K-E")

    M6 = sp.Matrix(36, 6, lambda r, c: sp.Integer(0))
    for ci, k in enumerate(ORDER):
        L = sp.zeros(6)
        for c, (i, j) in enumerate(pairs):
            r = pairs.index((S3[k][i], S3[k][j]))
            L[r, c] = 1
        for rr in range(6):
            for cc in range(6):
                M6[rr * 6 + cc, ci] = L[rr, cc]
    check("E4.1 IDENTIFIZIERBARKEIT: w -> L_w ist injektiv (Rang 6 ueber "
          "Q) -- Ein-Schritt-Prozesstomographie bestimmt ALLE sechs "
          "Birkhoff-Gewichte, also t", M6.rank() == 6, kill="K-E")


# ==================================================================== F
def task_f():
    section("F: Shannon-Kapazitaets-Zertifikate (50 Digits + exakte KKT)")
    mp.mp.dps = 50

    def dkl_bits(p, q):
        return sum(pi * mp.log(pi / qi) / mp.log(2)
                   for pi, qi in zip(p, q) if pi > 0)

    rowsT = [[mp.mpf(x) / 4374 for x in r]
             for r in ([1651, 1267, 1456], [1267, 1651, 1456],
                       [1456, 1456, 1462])]
    qstar = [(rowsT[0][k] + rowsT[1][k]) / 2 for k in range(3)]
    qstar_exact = [Fr(1651 + 1267, 2 * 4374), Fr(1267 + 1651, 2 * 4374),
                   Fr(1456 + 1456, 2 * 4374)]
    check("F1.1 q* = (1459, 1459, 1456)/4374 exakt und row1_3 = q*_3 "
          "(der dritte Buchstabe traegt im Traeger-Term exakt 0 bei)",
          qstar_exact == [Fr(1459, 4374), Fr(1459, 4374), Fr(1456, 4374)]
          and Fr(1456, 4374) == qstar_exact[2], kill="K-F")
    C_T = dkl_bits(rowsT[0], qstar)
    C_T2 = dkl_bits(rowsT[1], qstar)
    D3T = dkl_bits(rowsT[2], qstar)
    check("F1.2 C(T) = %s bit/Sechsschritt (Reviewer: 0.0083580191378 "
          "verifiziert); Traegerbuchstaben exakt gleich (Symmetrie)"
          % mp.nstr(C_T, 12),
          abs(C_T - mp.mpf("0.0083580191378")) < mp.mpf("1e-12")
          and abs(C_T - C_T2) < mp.mpf("1e-45"), kill="K-F")
    check("F1.3 KKT-RAND-ZERTIFIKAT: D(row3 || q*) = %s bit = 6.108e-6 "
          "(Reviewer verifiziert) << C strikt (Faktor %s) => p* = "
          "(1/2, 1/2, 0) ist EXAKT kapazitaetsoptimal"
          % (mp.nstr(D3T, 6), mp.nstr(C_T / D3T, 4)),
          abs(D3T - mp.mpf("6.108e-6")) < mp.mpf("1e-9") and D3T < C_T,
          kill="K-F")

    rowsB = [[mp.mpf(x) / 18 for x in r]
             for r in ([13, 1, 4], [1, 13, 4], [4, 4, 10])]
    qB = [(rowsB[0][k] + rowsB[1][k]) / 2 for k in range(3)]
    C_B = dkl_bits(rowsB[0], qB)
    D3B = dkl_bits(rowsB[2], qB)
    closed = (13 * mp.log(mp.mpf(13) / 7) - mp.log(mp.mpf(7))) \
        / (18 * mp.log(2))
    check("F2.1 C(B) = [13 log2(13/7) - log2 7]/18 = %s bit/Schritt "
          "(geschlossene Form; Reviewer 0.489041522 auf seine "
          "Druckgenauigkeit bestaetigt); KKT: D(row3 || q*_B) = %s < "
          "C(B) => p* = (1/2, 1/2, 0) ist AUCH fuer den Einzelschritt "
          "exakt optimal -- die Nachricht ist auf JEDER Skala binaer"
          % (mp.nstr(C_B, 10), mp.nstr(D3B, 6)),
          abs(C_B - closed) < mp.mpf("1e-45")
          and abs(C_B - mp.mpf("0.489041522")) < mp.mpf("5e-9")
          and D3B < C_B, kill="K-F")
    ratio = C_T / C_B
    check("F3.1 SECHS-SCHRITT-LOESCHER: C(T)/C(B) = %s (~1.71 %% "
          "ueberleben sechs unbeobachtete Schritte)" % mp.nstr(ratio, 6),
          abs(ratio - mp.mpf("0.01709")) < mp.mpf("1e-5"), kill="K-F")

    deltas = [Fr(1, 36), Fr(1, 9), Fr(1, 4)]
    check("F5.1 CFT-CODE-NEBENBEFUND (konditional, Literatur): Delta = "
          "(1/36, 1/9, 1/4) ALLE < 1/2 exakt => unter dem Sang-Hsieh-Zou-"
          "Kriterium (2406.09555) keine endliche passive Dekodier-"
          "schwelle, falls die Defektoperatoren die Sprungoperatoren "
          "sind -- konsistent mit n_EB <= 2 auf dem Qubit ([C] "
          "konditional, KEIN Anspruch)",
          all(d < Fr(1, 2) for d in deltas)
          and deltas == [2 * Fr(g * g, 36) / 2 for g in (1, 2, 3)])


# ======================================================================
def main():
    print("=" * 78)
    print("TRANSFER.DEFECT.BIRKHOFF.01 + TRANSFER.HIDDEN.CIRCULATION.01 + "
          "TRANSFER.CHOI.DISCRIMINATOR.01")
    print("=" * 78, flush=True)
    task_a()
    task_b()
    task_c()
    task_d()
    task_e()
    task_f()

    section("ZUSAMMENFASSUNG / VERDIKTE")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d Checks bestanden" % (n_pass, n_all))
    verdicts = {
        "CIRCULATION": "HIDDEN-PARAM-EXACT"
        if not [k for k in KILLS if k == "K-A"] else "CIRCULATION-DEAD",
        "DEFECT-BIRKHOFF": "VALUE-IDENTITY-EXACT (Funktor OPEN)"
        if not [k for k in KILLS if k == "K-B"] else "BIRKHOFF-DEAD",
        "DILATION": "KRAUS-EB-NOGO"
        if not [k for k in KILLS if k == "K-C"] else "NOGO-DEAD",
        "CHOI": "QUBIT-CRITICAL-EXACT (Full-Level NPT-persistent)"
        if not [k for k in KILLS if k == "K-D"] else "CHOI-DEAD",
        "DISCRIMINATOR": "LOOP-CURRENT-EXHIBITED"
        if not [k for k in KILLS if k == "K-E"] else "DISCRIMINATOR-DEAD",
        "MESSAGE": "BINARY-EXACT"
        if not [k for k in KILLS if k == "K-F"] else "CAPACITY-DEAD",
    }
    for k, v in verdicts.items():
        print("VERDIKT %s: %s" % (k, v))
    print("Laufzeit: %.1f s" % (time.time() - T0))
    print("ALLE CHECKS BESTANDEN" if n_pass == n_all
          else "CHECKS FEHLGESCHLAGEN")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
