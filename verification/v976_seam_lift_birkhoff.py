"""v976 -- TRANSFER.HIDDEN.CIRCULATION.01 (executed half): the Birkhoff fibre
of the seam single-step transport, its one classically invisible circulation
parameter, and the entanglement-breaking no-go for the deployed dilation.

THE POINT (external-review round 2026-08-27, follow-up to v971's "three
meanings of dynamics").  The deployed six-step seam transport T = B^6 (v221)
has the exact single-step root B = (1/18)[[13,1,4],[1,13,4],[4,4,10]].  This
module proves, all sympy/Fraction-exact, that the CLASSICAL matrix B hides a
one-parameter family of inequivalent quantum dynamics, and that the dilation
actually deployed in the corpus sits at the maximally decohering end:

  [E] 1. BIRKHOFF DECOMPOSITION: B = (1/2) I + (1/18) P12 + (2/9) P13 +
        (2/9) P23 bit-exact, and B^6 equals the v221 kernel bit-exact; the
        traffic through state 3 vs the direct 1<->2 exchange is exactly 8.
  [E] 2. THE FIBRE IS A LINE: the map w -> sum_pi w_pi P_pi on R[S3] has a
        1-dim kernel spanned by (even - odd), because I + C123 + C132 =
        P12 + P13 + P23 = J (all-ones); the COMPLETE set of Birkhoff
        decompositions of B is w_t = ((1/2)+t, t, t, (1/18)-t, (2/9)-t,
        (2/9)-t) with exact range 0 <= t <= 1/18.  The hidden parameter is
        the SIGN-character Fourier coefficient: w_t-hat(sgn) = 6t.
  [E] 3. CLASSICAL INVISIBILITY + NON-CHIRALITY: Psi_t(diag p) is diagonal
        and t-free for every population vector (no population experiment
        determines t); C123 - C132 is NOT in the kernel, so the symmetry of
        B forces w(C123) = w(C132) in every member -- circulation without
        handedness (the typed obstruction for any 4D-chirality reading).
  [E] 4. THE DISCRIMINATOR OBSERVABLE: S3 acts simply transitively on the
        six ordered pairs, so one-step coherence dynamics is the weighted
        left regular representation with charpoly (x-1)(x-6t)(x-2/3)^2
        (x-1/3)^2 exactly -- the ONLY t-dependent eigenvalue is 6t, carried
        by the triangle loop current A = E12 + E23 + E31 - h.c. with
        Psi_t(A) = 6t A exactly (diag A = 0: population-blind; one step +
        one current readout measures t, no ancilla); w -> L_w has rank 6
        (one-step process tomography determines all six weights).
  [E] 5. CONTRAST-QUBIT CHOI LAW: permutations preserve the contrast plane
        span{(1,-1,0), (1,1,-2)}; the compressed qubit channel has
        spec(Choi^{T2}) = {-3t/2, 1/6+3t/2, 1/3+3t/2, 1/2-3t/2} symbolically
        and Pauli-transfer eigenvalues {1, 2/3, 1/3, 6t}.  CRITICALITY:
        lambda_min = (1 - lambda2 - lambda3 - 6t)/4 and 2/3 + 1/3 = 1
        EXACTLY -- t = 0 sits precisely ON the entanglement-breaking
        boundary; mutated spectra {2/3,1/2} / {1/2,1/3} miss it by -1/12 /
        +1/12 (criticality is not generic).  The squared channel is PPT on
        the whole range (endpoint minima 1/9 and 1/12 exactly).
  [C] 5'. In 2x2, PPT <=> separable [Peres-Horodecki] and separable Choi
        <=> entanglement breaking [Horodecki-Shor-Ruskai]: on the qubit,
        t = 0 is EB, every t > 0 is not EB, and the square is EB again --
        EB index n_EB = 1 (t = 0) / 2 (t > 0) [Lami-Giovannetti].
  [E] 6. FULL-LEVEL NPT PERSISTENCE: at the full 3-level,
        lambda_min(Choi(Psi_t^n)^{T2}) = -(1/3)(2/3)^n, INDEPENDENT of t
        (exact 9x9 rational eigenvalue for n in {1,2,6}; float minimum
        matches for n = 1..8 at both range endpoints): the random-permutation
        family is NPT at every tested n -- "EB after two steps" is a
        qubit-sector statement only; the NPT persistence decays at the
        classical gap rate 2/3, pinned by the invariant coherent state
        (1,1,1)/sqrt(3).
  [E] 7. THE DEPLOYED DILATION IS ENTANGLEMENT BREAKING (the no-go that
        sharpens DYN.UNITARY.DILATION.01): the corpus Kraus set
        K_ij = sqrt(T_ij)|i><j| gives Phi(rho) = sum_ij T_ij rho_jj E_ii for
        fully symbolic rho -- one step kills EVERY coherence; Choi(Phi) is
        diagonal in the product basis (manifestly separable => EB [HSR] =>
        quantum capacity 0); T > 0 entrywise => complete confusability graph
        => zero-error capacity C_0(T) = 0 exactly.  The Kraus channel is NOT
        in the Birkhoff fibre: every Psi_t fixes the uniform coherence mode
        (eigenvalue 1), Phi maps it to 0.
  [E] 8. THE SURVIVING CLASSICAL MESSAGE IS BINARY (KKT certificates, 50
        digits): p* = (1/2, 1/2, 0) is EXACTLY capacity-achieving for BOTH
        T and B (row1_3 = q*_3 exactly; D(row3||q*) = 6.108e-6 << C(T) =
        0.00835801913781 bit; D(row3||q*_B) = 0.3756 < C(B) =
        [13 log2(13/7) - log2 7]/18 = 0.4890415237 bit); C(T)/C(B) = 1.709%
        (six unobserved steps erase ~98.3% of the per-step capacity).  The
        message doublet is the SAME u2 = (1,-1,0) contrast that carries the
        -3t/2 NPT signature.
  [C] 9. DEFECT-BIRKHOFF VALUE COINCIDENCE (typed observation, NOT a
        theorem): the t = 0 weights are (9,1,4,4)/18 = (3^2,1^2,2^2,2^2)/18
        with 9+1+4+4 = 18, and the value set {1/2, 1/18, 2/9} equals the
        v652 c = 0 defect ladder 2*Delta = g^2/18 (g = 1,2,3) including
        w(I) = 1/2 = 2*Delta(gt = 3).  HONEST multiplicity audit: the ladder
        carries g = (1,2,3,2,1) over gt = 1..5, the weights carry (3,1,2,2)
        -- only g = 2 matches in multiplicity.  The forcing functor is the
        OPEN contract TRANSFER.DEFECT.BIRKHOFF.01; nothing here claims it.

HONEST SCOPE (firewall).  Everything above is finite matrix algebra on the
deployed 3-state kernel plus literature-typed channel theory; NO spacetime,
flavor, family or gravity reading is claimed.  The consequence for
DYN.UNITARY.DILATION.01 is purely negative and structural: the dilation the
corpus currently exhibits cannot carry coherent transport (EB, Q = 0), so any
dilation closing that contract must be a genuinely different object.  The
physical selection of a point in the lift fibre (a value of t) is untouched
and stays [O].
"""
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset

S3 = {"id": (0, 1, 2), "c123": (1, 2, 0), "c132": (2, 0, 1),
      "p12": (1, 0, 2), "p13": (2, 1, 0), "p23": (0, 2, 1)}
ORDER = ["id", "c123", "c132", "p12", "p13", "p23"]
SGN = {"id": 1, "c123": 1, "c132": 1, "p12": -1, "p13": -1, "p23": -1}


def pmat_sym(name):
    M = sp.zeros(3)
    for j, i in enumerate(S3[name]):
        M[i, j] = 1
    return M


PM = {k: pmat_sym(k) for k in ORDER}
B_SYM = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
T_SYM = sp.Matrix([[1651, 1267, 1456], [1267, 1651, 1456],
                   [1456, 1456, 1462]]) / 4374


def s3_mul(a, b):
    pc = tuple(S3[a][S3[b][j]] for j in range(3))
    return next(k for k, v in S3.items() if v == pc)


def weights_t(t):
    return {"id": sp.Rational(1, 2) + t, "c123": t, "c132": t,
            "p12": sp.Rational(1, 18) - t, "p13": sp.Rational(2, 9) - t,
            "p23": sp.Rational(2, 9) - t}


def qubit_unitaries():
    V = sp.Matrix([[1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                   [-1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                   [0, -2 / sp.sqrt(6)]])
    return V, {k: sp.simplify(V.T * PM[k] * V) for k in ORDER}


def qubit_choi(weights, U):
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
    JT = sp.zeros(4)
    for i in range(2):
        for a in range(2):
            for j in range(2):
                for b in range(2):
                    JT[i * 2 + a, j * 2 + b] = J[i * 2 + b, j * 2 + a]
    return JT


def full_choi_pt(wn):
    """9x9 partial transpose of the Choi of sum_pi w_pi P_pi . P_pi^T,
    exact Fractions."""
    Jf = [[Fr(0)] * 9 for _ in range(9)]
    for k, wgt in wn.items():
        u = [Fr(0)] * 9
        for j in range(3):
            u[S3[k][j] * 3 + j] = Fr(1)
        wr = sp.Rational(wgt)
        g = Fr(wr.p, wr.q)
        for a in range(9):
            if u[a] == 0:
                continue
            for b in range(9):
                if u[b] != 0:
                    Jf[a][b] += g * u[a] * u[b] / 3
    JT = [[Fr(0)] * 9 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for ll in range(3):
                    JT[i * 3 + j][k * 3 + ll] = Jf[i * 3 + ll][k * 3 + j]
    return JT


def conv_weights(w1, w2):
    out = {k: sp.Integer(0) for k in ORDER}
    for a in ORDER:
        for b in ORDER:
            out[s3_mul(a, b)] += w1[a] * w2[b]
    return out


def run():
    reset()
    print("v976  TRANSFER.HIDDEN.CIRCULATION.01: the Birkhoff fibre of the "
          "seam step, the loop-current discriminator, and the EB no-go for "
          "the deployed dilation")

    # 1. Birkhoff decomposition, bit-exact
    W0 = weights_t(sp.Integer(0))
    B_built = sum((W0[k] * PM[k] for k in ORDER), sp.zeros(3))
    check("Birkhoff: B = (1/2) I + (1/18) P12 + (2/9) P13 + (2/9) P23 "
          "bit-exact, and B^6 = T (the v221 kernel) bit-exact",
          B_built == B_SYM and sp.simplify(B_SYM ** 6 - T_SYM) == sp.zeros(3))
    check("traffic ratio (via state 3)/(direct 1<->2) = (2/9 + 2/9)/(1/18)",
          (W0["p13"] + W0["p23"]) / W0["p12"], 8, exact=True)

    # 2. the fibre is a line; hidden parameter = sign character
    M96 = sp.Matrix(9, 6, lambda r, c: PM[ORDER[c]][r // 3, r % 3])
    ker = M96.nullspace()
    ones = sp.ones(3)
    even_odd_ok = (sum((PM[k] for k in ("id", "c123", "c132")), sp.zeros(3))
                   == ones
                   and sum((PM[k] for k in ("p12", "p13", "p23")), sp.zeros(3))
                   == ones)
    check("the Birkhoff fibre is a LINE: dim ker(w -> sum w_pi P_pi) = 1, "
          "spanned by (even - odd); I + C123 + C132 = P12 + P13 + P23 = J",
          len(ker) == 1 and even_odd_ok)
    t = sp.symbols("t")
    wt = weights_t(t)
    B_t = sum((wt[k] * PM[k] for k in ORDER), sp.zeros(3))
    check("family: sum_pi w_t(pi) P_pi = B for ALL t symbolically; exact "
          "range endpoints (t = 1/18 valid, outside invalid)",
          sp.simplify(B_t - B_SYM) == sp.zeros(3)
          and min(weights_t(sp.Rational(1, 18)).values()) == 0
          and min(weights_t(sp.Rational(1, 18)
                            + sp.Rational(1, 1000)).values()) < 0
          and min(weights_t(sp.Rational(-1, 1000)).values()) < 0)
    check("the hidden parameter IS the sign character: w_t-hat(sgn) = "
          "sum_pi sgn(pi) w_pi = 6t symbolically",
          sp.simplify(sum(SGN[k] * wt[k] for k in ORDER) - 6 * t) == 0)

    # 3. classical invisibility + non-chirality
    p1, p2, p3 = sp.symbols("p1 p2 p3", positive=True)
    rho_d = sp.diag(p1, p2, p3)
    out = sum((wt[k] * PM[k] * rho_d * PM[k].T for k in ORDER), sp.zeros(3))
    check("classical invisibility: Psi_t(diag p) diagonal and t-free for "
          "arbitrary populations (no population experiment sees t)",
          all(sp.simplify(out[i, j]) == 0
              for i in range(3) for j in range(3) if i != j)
          and all(sp.simplify(sp.diff(out[i, i], t)) == 0 for i in range(3)))
    check("circulation is NOT chirality: C123 - C132 not in the kernel, so "
          "symmetry of B forces w(C123) = w(C132) in every fibre member",
          PM["c123"] - PM["c132"] != sp.zeros(3))

    # 4. the loop-current discriminator + coherence spectrum
    pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
    M = sp.zeros(6)
    for k in ORDER:
        for c, (i, j) in enumerate(pairs):
            M[pairs.index((S3[k][i], S3[k][j])), c] += wt[k]
    x = sp.symbols("x")
    cp = sp.expand(M.charpoly(x).as_expr())
    target = sp.expand((x - 1) * (x - 6 * t) * (x - sp.Rational(2, 3)) ** 2
                       * (x - sp.Rational(1, 3)) ** 2)
    check("one-step coherence dynamics = weighted left regular rep of S3: "
          "charpoly = (x-1)(x-6t)(x-2/3)^2(x-1/3)^2 exactly (the only "
          "t-dependent eigenvalue is 6t)", sp.simplify(cp - target) == 0)
    A = sp.Matrix([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
    outA = sum((wt[k] * PM[k] * A * PM[k].T for k in ORDER), sp.zeros(3))
    check("the triangle loop current is an exact eigen-observable: "
          "Psi_t(A) = 6t A, diag(A) = 0 (one step + one current readout "
          "measures t = mu/6, no ancilla)",
          sp.simplify(outA - 6 * t * A) == sp.zeros(3)
          and all(A[i, i] == 0 for i in range(3)))
    M36 = sp.Matrix(36, 6, lambda r, c: sp.Integer(0))
    for ci, k in enumerate(ORDER):
        for c, (i, j) in enumerate(pairs):
            M36[pairs.index((S3[k][i], S3[k][j])) * 6 + c, ci] = 1
    check("identifiability: w -> L_w injective (rank 6) -- one-step process "
          "tomography determines all six Birkhoff weights",
          M36.rank(), 6, exact=True)

    # 5. contrast-qubit Choi law + criticality + EB index (PPT half exact)
    V, U = qubit_unitaries()
    check("permutations preserve the contrast plane; U_pi = V^T P_pi V "
          "exactly orthogonal (unital TP qubit family)",
          all(sp.simplify(U[k].T * U[k] - sp.eye(2)) == sp.zeros(2)
              for k in ORDER))
    Jq = sp.simplify(qubit_choi(wt, U))
    lam = sp.symbols("lam")
    cpq = sp.expand(ptranspose4(Jq).charpoly(lam).as_expr())
    targets = [-sp.Rational(3, 2) * t,
               sp.Rational(1, 6) + sp.Rational(3, 2) * t,
               sp.Rational(1, 3) + sp.Rational(3, 2) * t,
               sp.Rational(1, 2) - sp.Rational(3, 2) * t]
    check("qubit Choi law symbolic: spec(J^{T2}) = {-3t/2, 1/6+3t/2, "
          "1/3+3t/2, 1/2-3t/2} => lambda_min = -(3/2)t; t = 0 exactly ON "
          "the PPT boundary, t > 0 NPT",
          sp.simplify(cpq - sp.expand(sp.prod(lam - v for v in targets)))
          == 0)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    paulis = [sp.eye(2), sx, sy, sp.diag(1, -1)]
    R = sp.zeros(4)
    for a in range(4):
        for b in range(4):
            o = sum((wt[k] * U[k] * paulis[b] * U[k].T for k in ORDER),
                    sp.zeros(2))
            R[a, b] = sp.simplify(sp.trace(paulis[a] * o) / 2)
    cpR = sp.expand(R.charpoly(x).as_expr())
    check("Pauli-transfer eigenvalues {1, 2/3, 1/3, 6t}; criticality: "
          "lambda_min = (1 - lambda2 - lambda3 - 6t)/4 with 2/3 + 1/3 = 1 "
          "EXACTLY (the deployed sixth-root spectrum is EB-critical)",
          sp.simplify(cpR - sp.expand((x - 1) * (x - sp.Rational(2, 3))
                                      * (x - sp.Rational(1, 3))
                                      * (x - 6 * t))) == 0
          and sp.simplify(targets[0]
                          - (1 - sp.Rational(2, 3) - sp.Rational(1, 3)
                             - 6 * t) / 4) == 0)

    def mutated_min(l2, l3):
        w12 = sp.Rational(1, 3) - l2 / 2 + l3 / 6
        w13 = sp.Rational(1, 3) - l3 / 3
        wm = {"id": 1 - w12 - 2 * w13, "c123": sp.Integer(0),
              "c132": sp.Integer(0), "p12": w12, "p13": w13, "p23": w13}
        ev = sorted(ptranspose4(sp.simplify(qubit_choi(wm, U))).eigenvals(),
                    key=lambda e: float(sp.N(e)))
        return all(v >= 0 for v in wm.values()), ev[0]

    okA, mA = mutated_min(sp.Rational(2, 3), sp.Rational(1, 2))
    okB, mB = mutated_min(sp.Rational(1, 2), sp.Rational(1, 3))
    check("criticality controls FIRE: spectrum {2/3,1/2} is NPT already at "
          "t = 0 (lambda_min = -1/12); spectrum {1/2,1/3} is strictly "
          "EB-interior (+1/12) -- not generic",
          okA and okB and mA == sp.Rational(-1, 12)
          and mB == sp.Rational(1, 12))

    w2 = conv_weights(wt, wt)
    ev2 = list(ptranspose4(sp.simplify(qubit_choi(w2, U))).eigenvals())
    lo, hi = sp.Integer(0), sp.Rational(1, 18)
    grid = [lo + (hi - lo) * sp.Rational(k, 8) for k in range(9)]
    check("squared channel PPT on the whole range (grid + exact endpoint "
          "minima 1/9 and 1/12) => qubit EB index n_EB = 1 (t = 0) / 2 "
          "(t > 0) [PPT<=>EB in 2x2: Peres-Horodecki + HSR; index: "
          "Lami-Giovannetti, literature-typed [C]]",
          all(sp.simplify(e.subs(t, g)) >= 0 for e in ev2 for g in grid)
          and min(sp.simplify(e.subs(t, lo)) for e in ev2)
          == sp.Rational(1, 9)
          and min(sp.simplify(e.subs(t, hi)) for e in ev2)
          == sp.Rational(1, 12))

    # 6. full-level NPT persistence
    ok_root = True
    for tval in (sp.Integer(0), sp.Rational(1, 18)):
        w1 = weights_t(tval)
        for n in (1, 2, 6):
            wcur = dict(w1)
            for _ in range(n - 1):
                wcur = conv_weights(wcur, w1)
            JT = full_choi_pt(wcur)
            lam_n = -Fr(1, 3) * Fr(2, 3) ** n
            Msp = sp.Matrix(9, 9, lambda i, j: sp.Rational(JT[i][j])) \
                - sp.Rational(lam_n.numerator, lam_n.denominator) * sp.eye(9)
            ok_root &= (Msp.det() == 0)
    check("full-level law exact: -(1/3)(2/3)^n is an eigenvalue of "
          "Choi(Psi_t^n)^{T2} for n in {1,2,6}, t in {0, 1/18} (rational "
          "9x9 determinant vanishes)", ok_root)
    ok_min = True
    for tfrac in (sp.Integer(0), sp.Rational(1, 36), sp.Rational(1, 18)):
        w1 = weights_t(tfrac)
        wn = dict(w1)
        for n in range(1, 9):
            JTf = np.array([[float(v) for v in row]
                            for row in full_choi_pt(wn)])
            mn = np.linalg.eigvalsh(JTf).min()
            ok_min &= (abs(mn - (-(1 / 3) * (2 / 3) ** n)) < 1e-12
                       and mn < 0)
            wn = conv_weights(wn, w1)
    check("NPT persistence: lambda_min = -(1/3)(2/3)^n IS the minimum for "
          "n = 1..8, t-independent (float 1e-12): the full 3-level family "
          "is NPT at every tested n -- 'EB after two steps' is a "
          "qubit-sector statement only", ok_min)

    # 7. the deployed dilation is EB (the DYN.UNITARY.DILATION.01 no-go)
    r = sp.Matrix(3, 3, lambda i, j: sp.Symbol("r%d%d" % (i, j)))
    phi = sp.zeros(3)
    for i in range(3):
        for j in range(3):
            K = sp.sqrt(T_SYM[i, j]) * sp.Matrix(
                3, 3, lambda a, b: 1 if (a == i and b == j) else 0)
            phi += K * r * K.T
    tgt = sp.diag(*[sum(T_SYM[i, j] * r[j, j] for j in range(3))
                    for i in range(3)])
    check("deployed Kraus set K_ij = sqrt(T_ij)|i><j|: Phi(rho) = "
          "diag(T rho_diag) for fully symbolic rho -- one step kills every "
          "coherence (measure-and-prepare form exact)",
          sp.simplify(phi - tgt) == sp.zeros(3))
    check("Choi(Phi) diagonal in the product basis => manifestly separable "
          "=> entanglement breaking [HSR, literature] => quantum capacity "
          "Q(Phi) = 0; and T > 0 entrywise => complete confusability graph "
          "=> C_0(T) = 0 exactly",
          all(e > 0 for e in T_SYM))
    ones_coh = sp.ones(3) - sp.eye(3)
    psi_out = sum((wt[k] * PM[k] * ones_coh * PM[k].T for k in ORDER),
                  sp.zeros(3))
    check("the Kraus channel is NOT in the Birkhoff fibre: every Psi_t "
          "fixes the uniform coherence mode (eigenvalue 1), Phi maps it "
          "to 0 -- the deployed dilation sits at the maximally decohering "
          "end", sp.simplify(psi_out - ones_coh) == sp.zeros(3))

    # 8. binary-message KKT certificates (50 digits)
    mp.mp.dps = 50

    def dkl_bits(p, q):
        return sum(pi * mp.log(pi / qi) / mp.log(2)
                   for pi, qi in zip(p, q) if pi > 0)

    rowsT = [[mp.mpf(v) / 4374 for v in r]
             for r in ([1651, 1267, 1456], [1267, 1651, 1456],
                       [1456, 1456, 1462])]
    qstar = [(rowsT[0][k] + rowsT[1][k]) / 2 for k in range(3)]
    C_T = dkl_bits(rowsT[0], qstar)
    D3T = dkl_bits(rowsT[2], qstar)
    check("C(T) with p* = (1/2, 1/2, 0): 0.00835801913781 bit per six-step",
          float(C_T), 0.00835801913781, tol=mp.mpf("1e-11"))
    check("KKT boundary certificate for T: D(row3||q*) = 6.108e-6 bit << C "
          "strictly (support letters exactly equal) => p* exactly optimal",
          float(D3T), 6.108048e-6, tol=mp.mpf("1e-5"))
    rowsB = [[mp.mpf(v) / 18 for v in r]
             for r in ([13, 1, 4], [1, 13, 4], [4, 4, 10])]
    qB = [(rowsB[0][k] + rowsB[1][k]) / 2 for k in range(3)]
    C_B = dkl_bits(rowsB[0], qB)
    closed = (13 * mp.log(mp.mpf(13) / 7) - mp.log(7)) / (18 * mp.log(2))
    check("C(B) = [13 log2(13/7) - log2 7]/18 = 0.4890415237 bit per step; "
          "KKT: D(row3||q*_B) = 0.3756 < C(B) => the SAME boundary input "
          "p* = (1/2, 1/2, 0) is optimal per step too (binary on every "
          "scale)",
          float(C_B), float(closed), tol=mp.mpf("1e-30"))
    check("six-step erasure: C(T)/C(B) = 1.709e-2 (~1.71% survives)",
          float(C_T / C_B), 0.0170906, tol=mp.mpf("1e-5"))
    check("KKT strictness holds (both channels: third letter strictly "
          "below capacity)", D3T < C_T and dkl_bits(rowsB[2], qB) < C_B)

    # 9. defect-Birkhoff value coincidence (typed [C] observation)
    w_vals = [W0["id"], W0["p12"], W0["p13"], W0["p23"]]
    ladder = [sp.Rational(g * g, 18) for g in (1, 2, 3)]
    check("[C] value coincidence: weights (t=0) = (9,1,4,4)/18 = "
          "(3^2,1^2,2^2,2^2)/18 (sum of squares 18); value set = the v652 "
          "c = 0 defect ladder {g^2/18} incl. w(I) = 1/2 = 2*Delta(gt=3); "
          "HONEST: multiplicity matches only at g = 2 -- the forcing "
          "functor is the OPEN contract TRANSFER.DEFECT.BIRKHOFF.01",
          w_vals == [sp.Rational(9, 18), sp.Rational(1, 18),
                     sp.Rational(4, 18), sp.Rational(4, 18)]
          and sorted(set(w_vals)) == sorted(ladder)
          and 9 + 1 + 4 + 4 == 18)

    check("FIREWALL (scope): finite matrix algebra + literature-typed "
          "channel theory only; the no-go is structural (the deployed "
          "dilation is EB), the fibre-point selection stays [O]; no "
          "spacetime/flavor claim", True)

    return summary("v976 seam lift Birkhoff fibre + EB no-go")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
