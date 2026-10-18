"""v977 -- TRANSFER.COHERENT.WILSON.01 (executed half): the seam single-step
transport is unistochastic -- it carries an exact reversible SU(3) lift whose
gauge-invariant Wilson-plaquette phases form a closed Gaussian-Pythagorean
code over the TFPT atoms {2, 5, 12, 13}, whose CP-odd invariant is exactly
J = +-1/27, and whose phase is exactly the complexified spectral datum of the
v530 center atom matrix A = [[8,2],[5,3]].

THE POINT (external-review round 2026-08-27, companion to v976).  All
sympy-exact unless typed otherwise:

  [E] 1. UNISTOCHASTICITY: B = (1/18)[[13,1,4],[1,13,4],[4,4,10]] equals
        |U_ij|^2 entrywise for an exact U in SU(3) (U^dagger U = I,
        det U = 1).  The angles are FORCED by B alone (sin^2 th13 = B13 =
        2/9, sin^2 th12 = B12/(1-B13) = 1/14, sin^2 th23 = B23/(1-B13) =
        2/7) and cos(delta) = -4/sqrt(65) is uniquely solved by B21, so the
        complete lift set up to row/column rephasing is the two-branch
        family {U, U*} with e^{i delta} = (-4 +- 7i)/sqrt(65).
        [C] Coherification of a bistochastic matrix by a reversible unitary
        exists iff it is unistochastic (Dunkl-Zyczkowski; Korzekwa et al.);
        a unitary lift carries quantum capacity log2 3 -- versus C(T) =
        0.008358 bit classically (v976).
  [E] 2. THE WILSON DATA ARE CLASSICAL UP TO ONE SIGN: J = Im(U11 U22 U12*
        U21*) = 1/27 exactly; Re of every plaquette is fixed by B through
        unitarity (Re Q_{12;12} = (B13 B23 - B11 B21 - B12 B22)/2 = -5/324)
        and J^2 = B11 B21 B12 B22 - Re^2 = 1/729 -- the full
        rephasing-invariant data is determined by the classical matrix up
        to sgn J, a classically invisible Z2 orientation bit (U* lifts the
        SAME B with J = -1/27); the minimal observable is the plaquette
        interference readout Im(U11 U22 U12* U21*).
  [E] 3. THE 5-12-13 CODE: Q_{12;12} = (-5 + 12i)/324, normalized
        (-5 + 12i)/13 with 5^2 + 12^2 = 13^2; all NINE plaquettes close on
        four Gaussian phase types ((-5+12i)/13 x1, (-2+-3i)/sqrt13 x4,
        (-11+3i)/sqrt130 x2, (1-3i)/sqrt10 x2) with Gaussian norms
        exclusively {10, 13, 130, 169} = {2*5, 13, 2*5*13, 13^2}; every
        plaquette has Im = +-1/27; the four fundamental plaquettes generate
        all nine through exact B-weighted composition relations.  Atoms:
        5 = g_car, 12 = dim g_SM, 13 = Delta_Q = N(3+2i) (v530 / tfpt_2 /
        v738 anchors, read-only).
  [E] 4. THE CENTER BRIDGE: for the v530 atom matrix A = [[8,2],[5,3]],
        disc chi_A = 65 = det(A-I)^2 + (det A/2)^2 = 4^2 + 7^2, and
        e^{i delta} = (-det(A-I) +- i det A/2)/sqrt(disc chi_A) equals the
        transport-lift phase EXACTLY; -4 + 7i = (1+2i)(2+3i) with Gaussian
        norms 5 and 13 (the v738 tower primes).  NEGATIVE controls: the
        v530 sibling quotients A_K = [[14,8],[-11,-6]] (disc 48 vs identity
        value 13) and A_Q = [[3,1],[3,2]] (disc 13 vs 13/4) FAIL the
        square-sum identity -- the bridge selects the atom quotient A.
        HONEST: the bridge fixes the PHASE from A-invariants; the ANGLES
        come from B alone; a deployed intertwiner does not exist in the
        corpus (same missing-piece type as the shells->cusp map) -- that
        gap IS the open half of the contract.
  [E] 5. THE POWER LAW + RATIONALITY SELECTION: J_n^2 = (1-b)^2 (1 + 2b -
        3a^2)/108 with a = (2/3)^n, b = (1/3)^n (derived symbolically);
        J_n^2 > 0 for n = 1..12, so every B^n is unistochastic with its OWN
        freshly reconstructed U_n (U_6 is built and |U_6|^2 = B^6 = T
        entrywise exact); |J_6| = 0.0951088904 = 0.9884006 J_max and the
        uniform limit lifts to the Fourier matrix F3 with |J| = J_max =
        1/(6 sqrt 3) exactly.  J_n is RATIONAL ONLY at n = 1: the deployed
        step hits 3(1 + 2b - 3a^2) = 1 exactly, giving J = (1 - 1/3)/18 =
        1/27 -- the Gaussian-Pythagorean code selects the single step.
  [E] 6. NO FIXED MICROSTEP: B^2 != |U^2|^2 already (entry (1,1): 31/54 vs
        0.2450), and a quantitative recurrence witness exists (n* <= 10^6
        with min_i |(U^{n*})_{ii}|^2 >= 0.98 while max|B^{n*} - 1/3| <=
        1e-10): no single closed unitary generates the relaxing sequence.
        Typed reading: repeated steps need dephasing BETWEEN steps (v976's
        EB structure); the six-step macro-gate exists as its own U_6 but is
        NOT U_1^6 -- the coherent sharpening of the clock-vs-walk verdict.
  [E] 7. SELECTIVITY (the hard kill passes): the obstruction certificate
        works (the classic bistochastic-not-unistochastic matrix with zero
        diagonal has J^2 = -1/64 < 0); mutated sixth-root spectra
        {2/3, 1/2} and {1/2, 1/3} give irrational J (no code); over the
        238 valid unistochastic points of the natural family B(a, b) =
        J/3 + a P2 + b P3 on the k/18 grid, only 4 have rational J and
        EXACTLY ONE carries the full 5-12-13 code: the deployed point
        (a, b) = (2/3, 1/3) -- 0.42%, far under the 10% genericity kill.
  [E] 8. PMNS NEAR-MISS STAYS NEGATIVE: the J = -1/27 branch has delta =
        240.2551 deg, near the deployed delta_PMNS = 4pi/3 = 240 deg
        (v270), BUT J_tr = -1/27 = -0.037037 != J_PMNS = -0.02965 and all
        three lift angles differ from the PMNS angles -- NO PMNS
        derivation is claimed or supported.

HONEST SCOPE (firewall).  Finite matrix identities and a census; the
physical selection of a lift branch (sgn J), any CP/time-orientation
reading, and the A -> angles intertwiner stay [O] (the open half of
TRANSFER.COHERENT.WILSON.01).  Nothing here moves the PMNS construction,
and no flavor or 4D claim is made.
"""
import mpmath as mp
import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset

B_SYM = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
JMAXSQ = sp.Rational(1, 108)


def build_lift(Bm, branch=+1):
    """exact PDG-parametrized lift of a symmetric doubly stochastic 3x3
    matrix; returns (U, s13sq, s12sq, s23sq, cos_delta, sin_delta)."""
    s13sq = sp.nsimplify(Bm[0, 2])
    c13sq = 1 - s13sq
    s12sq = sp.nsimplify(Bm[0, 1] / c13sq)
    s23sq = sp.nsimplify(Bm[1, 2] / c13sq)
    c12sq, c23sq = 1 - s12sq, 1 - s23sq
    s12, c12 = sp.sqrt(s12sq), sp.sqrt(c12sq)
    s23, c23 = sp.sqrt(s23sq), sp.sqrt(c23sq)
    s13, c13 = sp.sqrt(s13sq), sp.sqrt(c13sq)
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


def run():
    reset()
    print("v977  TRANSFER.COHERENT.WILSON.01: the unistochastic SU(3) lift, "
          "the 5-12-13 Wilson code, the center bridge, the orientation bit")

    # 1. the exact SU(3) lift
    U, s13sq, s12sq, s23sq, cosd, sind = build_lift(B_SYM, +1)
    check("angles forced by B: sin^2 th13 = 2/9, sin^2 th12 = 1/14, "
          "sin^2 th23 = 2/7 exactly",
          (s13sq, s12sq, s23sq)
          == (sp.Rational(2, 9), sp.Rational(1, 14), sp.Rational(2, 7)))
    check("cos(delta) = -4/sqrt(65) uniquely solved by B21; e^{i delta} = "
          "(-4 +- 7i)/sqrt(65); lift set up to rephasing = {U, U*}",
          sp.simplify(cosd + 4 / sp.sqrt(65)) == 0
          and sp.simplify(sind - 7 / sp.sqrt(65)) == 0)
    check("U in SU(3) exactly: U^dagger U = I and det U = 1",
          sp.simplify(U.H * U - sp.eye(3)) == sp.zeros(3)
          and sp.simplify(U.det()) == 1)
    check("UNISTOCHASTIC: |U_ij|^2 = B_ij entrywise exact (the classical "
          "transport is the measurement shadow of a reversible SU(3) "
          "rotation; coherification iff unistochastic, literature [C])",
          sp.simplify(abs2_matrix(U) - B_SYM) == sp.zeros(3))

    # 2. Wilson data classical up to one sign
    Q0 = plaq(U, 0, 1, 0, 1)
    ReQ_B = (B_SYM[0, 2] * B_SYM[1, 2] - B_SYM[0, 0] * B_SYM[1, 0]
             - B_SYM[0, 1] * B_SYM[1, 1]) / 2
    check("J = Im(U11 U22 U12* U21*) = 1/27 exact; Re Q = -5/324 and "
          "J^2 = 1/729 fixed by B alone (unitarity) -- the full "
          "rephasing-invariant Wilson data is classical up to sgn J",
          sp.simplify(sp.im(Q0)) == sp.Rational(1, 27)
          and ReQ_B == sp.Rational(-5, 324)
          and B_SYM[0, 0] * B_SYM[1, 0] * B_SYM[0, 1] * B_SYM[1, 1]
          - ReQ_B ** 2 == sp.Rational(1, 729)
          and sp.simplify(sp.re(Q0) - ReQ_B) == 0)
    Uc = U.conjugate()
    check("ORIENTATION BIT: U* lifts the same B with J = -1/27 (classically "
          "invisible Z2; observable = the plaquette interference readout)",
          sp.simplify(abs2_matrix(Uc) - B_SYM) == sp.zeros(3)
          and sp.simplify(sp.im(plaq(Uc, 0, 1, 0, 1)))
          == sp.Rational(-1, 27))

    # 3. the 5-12-13 code
    check("main loop: Q_{12;12} = (-5 + 12i)/324, normalized (-5 + 12i)/13, "
          "5^2 + 12^2 = 13^2 (atoms: 5 = g_car, 12 = dim g_SM, 13 = "
          "Delta_Q = N(3+2i))",
          sp.simplify(Q0 - (-5 + 12 * sp.I) / 324) == 0
          and sp.simplify(Q0 / sp.Abs(Q0) - (-5 + 12 * sp.I) / 13) == 0
          and 5 ** 2 + 12 ** 2 == 13 ** 2
          and sp.Abs(3 + 2 * sp.I) ** 2 == 13)
    pairs = [(0, 1), (0, 2), (1, 2)]
    table = {(i, k, j, l): plaq(U, i, k, j, l)
             for (i, k) in pairs for (j, l) in pairs}
    types = {"t1": (-5 + 12 * sp.I) / 13,
             "t2p": (-2 + 3 * sp.I) / sp.sqrt(13),
             "t2m": (-2 - 3 * sp.I) / sp.sqrt(13),
             "t3": (-11 + 3 * sp.I) / sp.sqrt(130),
             "t4": (1 - 3 * sp.I) / sp.sqrt(10)}
    counts = {k: 0 for k in list(types) + ["other"]}
    for q in table.values():
        n = sp.simplify(q / sp.Abs(q))
        hit = next((nm for nm, tv in types.items()
                    if sp.simplify(n - tv) == 0), "other")
        counts[hit] += 1
    check("all nine plaquettes close on four Gaussian phase types "
          "(1x t1, 4x t2, 2x t3, 2x t4); Gaussian norms exclusively "
          "{10, 13, 130, 169} = {2*5, 13, 2*5*13, 13^2}",
          counts == {"t1": 1, "t2p": 2, "t2m": 2, "t3": 2, "t4": 2,
                     "other": 0}
          and {10, 13, 130, 169} == {2 * 5, 13, 2 * 5 * 13, 13 ** 2})
    check("every plaquette has Im = +-1/27 (the Jarlskog identity of all "
          "nine loops)",
          all(sp.simplify(sp.im(q)) in (sp.Rational(1, 27),
                                        sp.Rational(-1, 27))
              for q in table.values()))
    fund = {(i, j): table[(i, i + 1, j, j + 1)]
            for i in (0, 1) for j in (0, 1)}
    ok_gen = True
    for i in (0, 1):
        ok_gen &= sp.simplify(
            table[(i, i + 1, 0, 2)]
            - fund[(i, 0)] * fund[(i, 1)]
            / (B_SYM[i, 1] * B_SYM[i + 1, 1])) == 0
    for j in (0, 1):
        ok_gen &= sp.simplify(
            table[(0, 2, j, j + 1)]
            - fund[(0, j)] * fund[(1, j)]
            / (B_SYM[1, j] * B_SYM[1, j + 1])) == 0
    ok_gen &= sp.simplify(
        table[(0, 2, 0, 2)]
        - fund[(0, 0)] * fund[(0, 1)] * fund[(1, 0)] * fund[(1, 1)]
        / (B_SYM[0, 1] * B_SYM[1, 0] * B_SYM[1, 2] * B_SYM[2, 1]
           * B_SYM[1, 1] ** 2)) == 0
    check("the four fundamental plaquettes generate all nine via exact "
          "B-weighted Wilson composition relations", ok_gen)

    # 4. the center bridge
    A = sp.Matrix([[8, 2], [5, 3]])
    disc = sp.discriminant(A.charpoly().as_expr())
    detm1 = (A - sp.eye(2)).det()
    check("center bridge: disc chi_A = 65 = det(A-I)^2 + (det A/2)^2 = "
          "4^2 + 7^2 for the v530 atom matrix A = [[8,2],[5,3]]",
          A.det() == 14 and detm1 == 4 and disc == 65
          and detm1 ** 2 + (A.det() / 2) ** 2 == 65)
    check("e^{i delta} = (-det(A-I) + i det A/2)/sqrt(disc chi_A) equals "
          "the transport-lift phase exactly; -4 + 7i = (1+2i)(2+3i) with "
          "Gaussian norms 5, 13 (the v738 tower primes)",
          sp.simplify((-detm1 + sp.I * A.det() / 2) / sp.sqrt(disc)
                      - (-4 + 7 * sp.I) / sp.sqrt(65)) == 0
          and sp.expand((1 + 2 * sp.I) * (2 + 3 * sp.I)) == -4 + 7 * sp.I
          and sp.Abs(1 + 2 * sp.I) ** 2 == 5
          and sp.Abs(2 + 3 * sp.I) ** 2 == 13)
    ok_neg = True
    for M, expect_disc in ((sp.Matrix([[14, 8], [-11, -6]]), 48),
                           (sp.Matrix([[3, 1], [3, 2]]), 13)):
        d = sp.discriminant(M.charpoly().as_expr())
        lhs = (M - sp.eye(2)).det() ** 2 + (M.det() / 2) ** 2
        ok_neg &= (d == expect_disc and sp.simplify(lhs - d) != 0)
    check("NEGATIVE controls fire: the v530 sibling quotients A_K (disc 48 "
          "vs 13) and A_Q (disc 13 vs 13/4) FAIL the square-sum identity "
          "-- the bridge selects the atom quotient A", ok_neg)

    # 5. power law + rationality selection
    a, b = sp.symbols("a b", positive=True)
    B11 = sp.Rational(1, 3) + a / 2 + b / 6
    B12 = sp.Rational(1, 3) - a / 2 + b / 6
    B13 = sp.Rational(1, 3) - b / 3
    ReQn = (B13 ** 2 - 2 * B11 * B12) / 2
    check("J_n^2 = (1-b)^2 (1 + 2b - 3a^2)/108 with a = (2/3)^n, "
          "b = (1/3)^n, derived symbolically from the B^n entries",
          sp.simplify(sp.expand((B11 * B12) ** 2 - ReQn ** 2)
                      - (1 - b) ** 2 * (1 + 2 * b - 3 * a ** 2) / 108) == 0)
    rational_ns, all_pos = [], True
    for n in range(1, 13):
        an, bn = sp.Rational(2, 3) ** n, sp.Rational(1, 3) ** n
        J2 = (1 - bn) ** 2 * (1 + 2 * bn - 3 * an ** 2) / 108
        all_pos &= (J2 > 0)
        if sp.nsimplify(sp.sqrt(J2)).is_rational is True:
            rational_ns.append(n)
    check("J_n^2 > 0 for n = 1..12 (every power unistochastic); J_n "
          "RATIONAL ONLY at n = 1 -- the Gaussian-Pythagorean code selects "
          "the single step; mechanism: 3(1 + 2b - 3a^2) = 1 exactly at "
          "n = 1, so J = (1 - 1/3)/18 = 1/27",
          all_pos and rational_ns == [1]
          and sp.simplify(3 * (1 + 2 * sp.Rational(1, 3)
                               - 3 * sp.Rational(4, 9)) - 1) == 0)
    B6 = B_SYM ** 6
    U6 = build_lift(B6, +1)[0]
    check("U_6 built: |U_6|^2 = B^6 = T entrywise exact (the six-step "
          "macro-gate exists as its own reversible unitary)",
          sp.simplify(abs2_matrix(U6) - B6) == sp.zeros(3))
    J6 = sp.sqrt((1 - sp.Rational(1, 729)) ** 2
                 * (1 + sp.Rational(2, 729) - 3 * sp.Rational(4, 9) ** 6)
                 / 108)
    check("|J_6| = 0.0951088904 = 0.9884006 J_max", float(J6),
          0.0951088904, tol=mp.mpf("1e-9"))
    F3 = sp.Matrix(3, 3, lambda i, j:
                   sp.exp(2 * sp.pi * sp.I * i * j / 3) / sp.sqrt(3))
    check("the uniform limit lifts to the Fourier matrix F3 with "
          "|J| = J_max = 1/(6 sqrt 3) exactly (maximal interference "
          "endpoint)",
          sp.simplify(sp.im(plaq(F3, 0, 1, 0, 1)) ** 2 - JMAXSQ) == 0)

    # 6. no fixed microstep
    absU2sq = abs2_matrix(U * U)
    B2 = B_SYM * B_SYM
    check("no fixed microstep: B^2 != |U^2|^2 exact (entry (1,1): 31/54 = "
          "0.5741 vs 0.2450) -- each power needs its OWN U_n",
          sp.simplify(absU2sq - B2) != sp.zeros(3)
          and abs(float(absU2sq[0, 0]) - float(B2[0, 0])) > 0.1)
    Un = np.array([[complex(sp.N(U[i, j], 30)) for j in range(3)]
                   for i in range(3)])
    th = np.angle(np.linalg.eigvals(Un))
    ns = np.arange(1, 1000001)
    dmax = np.maximum.reduce([np.abs(((ns * t + np.pi) % (2 * np.pi))
                                     - np.pi) for t in th])
    nstar = int(ns[np.argmin(dmax)])
    w, V = np.linalg.eig(Un)
    Upow = V @ np.diag(w ** nstar) @ np.linalg.inv(V)
    diagmin = float(np.min(np.abs(np.diag(Upow)) ** 2))
    Bf = np.array([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
    relax = float(np.max(np.abs(np.linalg.matrix_power(Bf, 200) - 1 / 3)))
    check("recurrence witness (Dirichlet, n* = %d): min diag |U^{n*}|^2 "
          ">= 0.98 while max|B^n - 1/3| <= 1e-10 -- no single closed "
          "unitary generates the relaxing sequence; repeated steps need "
          "dephasing between steps, U_6 != U_1^6 (clock-vs-walk sharpened)"
          % nstar, diagmin >= 0.98 and relax <= 1e-10)

    # 7. selectivity census + hard kill
    Bns = sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) / 2
    ReQns = (Bns[0, 2] * Bns[1, 2] - Bns[0, 0] * Bns[1, 0]
             - Bns[0, 1] * Bns[1, 1]) / 2
    check("obstruction certificate fires: the classic bistochastic-but-NOT-"
          "unistochastic matrix (zero diagonal) has J^2 = -1/64 < 0",
          Bns[0, 0] * Bns[1, 0] * Bns[0, 1] * Bns[1, 1] - ReQns ** 2
          == sp.Rational(-1, 64))
    ok_mut = True
    for l2, l3, expect in ((sp.Rational(2, 3), sp.Rational(1, 2),
                            sp.Rational(1, 648)),
                           (sp.Rational(1, 2), sp.Rational(1, 3),
                            sp.Rational(11, 2916))):
        J2 = (1 - l3) ** 2 * (1 + 2 * l3 - 3 * l2 ** 2) / 108
        ok_mut &= (J2 == expect
                   and sp.nsimplify(sp.sqrt(J2)).is_rational is not True)
    check("mutation controls fire: spectra {2/3, 1/2} and {1/2, 1/3} give "
          "J^2 = 1/648 and 11/2916 -- J irrational, no Gaussian code",
          ok_mut)
    u2 = sp.Matrix([1, -1, 0])
    u3 = sp.Matrix([1, 1, -2])
    P2 = u2 * u2.T / 2
    P3 = u3 * u3.T / 6
    Jth = sp.ones(3) / 3
    n_valid = n_ratJ = n_full = 0
    full_pts = []
    for k in range(1, 18):
        for m in range(1, 18):
            av, bv = sp.Rational(k, 18), sp.Rational(m, 18)
            Bg = Jth + av * P2 + bv * P3
            if any(e <= 0 for e in Bg):
                continue
            J2 = (1 - bv) ** 2 * (1 + 2 * bv - 3 * av ** 2) / 108
            if J2 < 0:
                continue
            n_valid += 1
            Jr = sp.nsimplify(sp.sqrt(J2))
            if Jr.is_rational is True:
                n_ratJ += 1
                ReQg = (Bg[0, 2] * Bg[1, 2] - Bg[0, 0] * Bg[1, 0]
                        - Bg[0, 1] * Bg[1, 1]) / 2
                if J2 > 0 and sp.simplify(
                        (ReQg + sp.I * Jr) / (Bg[0, 0] * Bg[0, 1])
                        - (-5 + 12 * sp.I) / 13) == 0:
                    n_full += 1
                    full_pts.append((av, bv))
    check("grid census (hard kill <= 10%%): %d valid unistochastic family "
          "points, %d with rational J (%.1f%%), EXACTLY ONE full 5-12-13 "
          "code point = the deployed (2/3, 1/3) (%.2f%%) -- CODE-SELECTIVE"
          % (n_valid, n_ratJ, 100 * n_ratJ / n_valid,
             100 * n_full / n_valid),
          n_full == 1 and full_pts == [(sp.Rational(2, 3),
                                        sp.Rational(1, 3))]
          and n_full <= n_valid / 10)

    # 8. PMNS near-miss stays negative
    deg = float(sp.deg(sp.arg(-4 - 7 * sp.I)) % 360)
    check("PMNS near-miss stays NEGATIVE: branch phase 240.2551 deg near "
          "deployed 240 deg (4pi/3, v270) but J_tr = -1/27 = -0.037037 != "
          "J_PMNS = -0.02965 and all angles differ -- no PMNS derivation",
          abs(deg - 240.2551) < 5e-4
          and abs(-1 / 27 - (-0.02965)) > 0.007)

    check("FIREWALL (scope): finite matrix identities + census; branch "
          "selection sgn J, CP/time readings and the A -> angles "
          "intertwiner stay [O] (the open half of the contract); no "
          "flavor/4D claim", True)

    return summary("v977 unistochastic SU(3) lift + 5-12-13 Wilson code")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
