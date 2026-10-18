"""v971 -- DYN.MARKOV.EMBED.01: the seam transfer kernel embeds into a
continuous positivity-preserving Markov semigroup (Q = log T exact).

THE POINT (external-review round 2026-08-27, "three meanings of dynamics").
Three different things have been called "dynamics" in the corpus: (a) the
positive relaxation T^n to the unique attractor; (b) a continuous dissipative
semigroup e^{t log T}; (c) reversible Lorentz/unitary time evolution e^{-itH}.
This module proves the step (a)->(b) EXACTLY for the concrete 3-state seam
transfer kernel (v221: T = J + (2/3)^6 u2u2^T + (1/3)^6 u3u3^T, spectrum
{1, (2/3)^6, (1/3)^6}): the principal matrix logarithm Q = log T is a genuine
classical Markov generator (Q-matrix), so T = e^Q sits inside the continuous
positivity-preserving semigroup {e^{tQ} : t >= 0} -- embeddability is a
THEOREM for this kernel, not an analogy.  Everything is sympy-exact:

  [E] 1. exact kernel: T is symmetric, doubly stochastic, entrywise > 0,
        with exact spectrum {1, 64/729, 1/729} (identical to v221's kernel).
  [E] 2. the principal log is spectral: Q = ln(64/729) P2 + ln(1/729) P3
        with orthogonal projectors; exp(Q) = T exactly (spectral calculus).
  [E] 3. Q-MATRIX, ROW SUMS: every row of Q sums to 0 exactly (symbolic zero).
  [E] 4. Q-MATRIX, OFF-DIAGONALS: the three independent off-diagonal entries
        are EXACTLY {ln(9/8), 2 ln 3, 2 ln 3} = {0.117783, 2.197225, 2.197225},
        all > 0 symbolically (9/8 > 1, 9 > 1); diagonals -ln(81/8), -ln(81/8),
        -4 ln 3.
  [E] 5. POSITIVITY FOR ALL t >= 0 (uniformization certificate): with
        q = 4 ln 3 = max|Q_ii|, the matrix Q + qI is entrywise >= 0 exactly
        (diagonal entries ln 8, ln 8, 0), hence e^{tQ} = e^{-qt} e^{t(Q+qI)}
        is entrywise >= 0 for every t >= 0; Q1 = 0 and symmetry make each
        e^{tQ} doubly stochastic.  So T = e^{1*Q} is embeddable, and every
        real root T^{1/n} = e^{Q/n} is again a stochastic matrix.
  [E] 6. spec(Q) = {0, -6 ln(3/2), -6 ln 3} = -spec(H_mod) (v957): the
        generator gap is the seam gap Delta = 6 ln(3/2), and the semigroup
        contracts deviations at exactly (2/3)^{6t} (v221 at integer t).
  [E] 7. NEGATIVE CONTROL (embeddability is not generic): the same
        construction with second eigenvalue -1/10 gives a doubly stochastic
        kernel with det = -1/200 < 0, while every embeddable stochastic
        matrix has det e^Q = e^{tr Q} > 0 -- that kernel provably admits NO
        continuous positivity-preserving embedding.  Positivity of the seam
        spectrum (RP/OS, CONTRACT.F.01 axiom 3) is what makes (a)->(b) real.

HONEST SCOPE (the firewall this module exists to enforce).  This closes the
FINITE, KERNEL-LEVEL half of DYN.MARKOV.EMBED.01 and nothing else: e^{tQ} is
IRREVERSIBLE statistical dynamics (detailed balance w.r.t. the uniform state;
an H-theorem, not a Schroedinger equation).  Step (b)->(c) -- a local,
size-consistent Stinespring/Hamiltonian dilation with a Lieb-Robinson bound
and an OS continuation T = e^{-aH} -> U(t) = e^{-itH} -- is the SEPARATE open
contract DYN.UNITARY.DILATION.01 and is NOT advanced here.  The shared
relaxation shape of the four F_transfer sectors is a universal CONTRACTION
CLASS, not one physical clock (v723/v724/v777: no common continuous clock
exists).  Status: [E] finite kernel embedding; the field-level statement and
the unitary dilation stay [O].
"""
import mpmath as mp
import sympy as sp

from tfpt_constants import check, summary, reset

LAM2 = sp.Rational(64, 729)     # (2/3)^6, the seam gap factor
LAM3 = sp.Rational(1, 729)      # (1/3)^6


def exact_kernel_and_projectors():
    """The v221 kernel and its spectral projectors, all exact rationals."""
    one = sp.ones(3, 1)
    u2 = sp.Matrix([1, -1, 0])
    u3 = sp.Matrix([1, 1, -2])            # the Nariai traceless anchor
    J = one * one.T / 3                   # projector onto the uniform state
    P2 = u2 * u2.T / (u2.T * u2)[0]
    P3 = u3 * u3.T / (u3.T * u3)[0]
    T = J + LAM2 * P2 + LAM3 * P3
    return T, J, P2, P3


def run():
    reset()
    print("v971  DYN.MARKOV.EMBED.01: Q = log T is an exact Markov generator "
          "(the seam kernel embeds into a continuous stochastic semigroup)")

    T, J, P2, P3 = exact_kernel_and_projectors()

    # 1. exact kernel identical to v221
    dstoch = all(sum(T[i, :]) == 1 for i in range(3)) \
        and all(sum(T[:, j]) == 1 for j in range(3)) \
        and all(e > 0 for e in T)
    check("T symmetric, doubly stochastic, entrywise > 0 (exact rationals; "
          "the v221 kernel verbatim)", T == T.T and dstoch)
    spec_T = sorted(T.eigenvals().keys(), reverse=True)
    check("exact spectrum of T = {1, 64/729, 1/729} = {1, (2/3)^6, (1/3)^6}",
          spec_T == [1, LAM2, LAM3], exact=True)

    # 2. the principal spectral logarithm, and exp(Q) = T exactly
    Q = sp.log(LAM2) * P2 + sp.log(LAM3) * P3
    T_back = J + sp.exp(sp.log(LAM2)) * P2 + sp.exp(sp.log(LAM3)) * P3
    proj_ok = (P2 * P2 == P2 and P3 * P3 == P3
               and P2 * P3 == sp.zeros(3) and J + P2 + P3 == sp.eye(3))
    check("spectral calculus exact: {J, P2, P3} orthogonal resolution of the "
          "identity and exp(Q) = T (principal log; trivial eigenvalue -> 0)",
          proj_ok and sp.simplify(T_back - T) == sp.zeros(3))

    # numeric cross-check of the principal log at 50 digits, built from the
    # exact closed-form entries (checked symbolically below):
    # Q = [[-ln(81/8), ln(9/8), 2ln3], [ln(9/8), -ln(81/8), 2ln3],
    #      [2ln3, 2ln3, -4ln3]]
    mp.mp.dps = 50
    Tn = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            e = T[i, j]
            Tn[i, j] = mp.mpf(sp.Rational(e).p) / mp.mpf(sp.Rational(e).q)
    l98 = mp.log(mp.mpf(9) / 8)
    l3 = mp.log(mp.mpf(3))
    l818 = mp.log(mp.mpf(81) / 8)
    Qn = mp.matrix([[-l818, l98, 2 * l3],
                    [l98, -l818, 2 * l3],
                    [2 * l3, 2 * l3, -4 * l3]])
    dev = max(abs(mp.expm(Qn)[i, j] - Tn[i, j])
              for i in range(3) for j in range(3))
    check("mpmath expm(Q) reproduces T entrywise at 50 digits (dev < 1e-45)",
          dev < mp.mpf('1e-45'))

    # 3. row sums vanish exactly
    rows0 = all(sp.simplify(sum(Q[i, :])) == 0 for i in range(3))
    check("Q-MATRIX row sums: sum_j Q_ij = 0 EXACTLY for every row "
          "(symbolic zero, no tolerance)", rows0)

    # 4. off-diagonals exactly {ln(9/8), 2 ln 3, 2 ln 3} > 0
    offdiag_ok = (sp.simplify(Q[0, 1] - sp.log(sp.Rational(9, 8))) == 0
                  and sp.simplify(Q[0, 2] - 2 * sp.log(3)) == 0
                  and sp.simplify(Q[1, 2] - 2 * sp.log(3)) == 0
                  and Q == Q.T)
    check("Q-MATRIX off-diagonals: Q12 = ln(9/8), Q13 = Q23 = 2 ln 3, "
          "symmetric -- all > 0 symbolically (9/8 > 1, 9 > 1)",
          offdiag_ok and sp.log(sp.Rational(9, 8)) > 0 and 2 * sp.log(3) > 0)
    check("Q12 = ln(9/8) = 0.117783 (the reviewer's verified number)",
          float(sp.N(Q[0, 1], 20)), 0.117783035656383589, tol=mp.mpf('1e-12'))
    check("Q13 = Q23 = 2 ln 3 = 2.197225 (the reviewer's verified numbers)",
          float(sp.N(Q[0, 2], 20)), 2.197224577336219383, tol=mp.mpf('1e-12'))
    diag_ok = (sp.simplify(Q[0, 0] + sp.log(sp.Rational(81, 8))) == 0
               and sp.simplify(Q[1, 1] + sp.log(sp.Rational(81, 8))) == 0
               and sp.simplify(Q[2, 2] + 4 * sp.log(3)) == 0)
    check("diagonals exactly -ln(81/8), -ln(81/8), -4 ln 3", diag_ok)

    # 5. uniformization: Q + qI >= 0 entrywise with q = 4 ln 3 exactly
    q = 4 * sp.log(3)
    Qplus = Q + q * sp.eye(3)
    unif_ok = (sp.simplify(Qplus[0, 0] - sp.log(8)) == 0
               and sp.simplify(Qplus[1, 1] - sp.log(8)) == 0
               and sp.simplify(Qplus[2, 2]) == 0
               and all(sp.simplify(Qplus[i, j]) >= 0
                       for i in range(3) for j in range(3)))
    check("UNIFORMIZATION [E]: q = 4 ln 3 = max|Q_ii| gives Q + qI >= 0 "
          "entrywise EXACTLY (diagonals ln 8, ln 8, 0) => e^{tQ} = "
          "e^{-qt} e^{t(Q+qI)} is entrywise >= 0 for ALL t >= 0", unif_ok)
    # spot-check the semigroup numerically on a t-grid incl. fractional roots
    grid_ok = True
    for tval in ('0.1', '0.25', '0.5', '1.5', '3.0', '7.0'):
        Et = mp.expm(Qn * mp.mpf(tval))
        grid_ok = grid_ok and all(Et[i, j] > -mp.mpf('1e-30')
                                  for i in range(3) for j in range(3)) \
            and all(abs(sum(Et[i, j] for j in range(3)) - 1) < mp.mpf('1e-30')
                    for i in range(3))
    check("semigroup grid check: e^{tQ} entrywise >= 0 and row-stochastic at "
          "t in {0.1, 0.25, 0.5, 1.5, 3, 7} (50 digits); T^{1/n} = e^{Q/n} "
          "is again stochastic (embeddability/Elfving, affirmative)", grid_ok)

    # 6. generator spectrum = -spec(H_mod), gap = Delta
    spec_Q = sorted(Q.eigenvals().keys(), reverse=True,
                    key=lambda e: float(sp.N(e, 30)))
    target = [sp.Integer(0), sp.log(LAM2), sp.log(LAM3)]
    spec_ok = all(sp.simplify(a - b) == 0 for a, b in zip(spec_Q, target))
    check("spec(Q) = {0, -6 ln(3/2), -6 ln 3} = -spec(H_mod) (v957: "
          "T = e^{-H_mod}); generator gap = Delta = 6 ln(3/2) exactly",
          spec_ok and sp.simplify(-sp.log(LAM2) - 6 * sp.log(sp.Rational(3, 2))) == 0)
    check("detailed balance: Q symmetric w.r.t. the uniform stationary state "
          "(the KMS/OS-positive free level; irreversible H-theorem dynamics, "
          "NOT a Schroedinger equation)", Q == Q.T)

    # 7. negative control: spectrum {1, -1/10, 1/20} is NOT embeddable
    Tneg = J - sp.Rational(1, 10) * P2 + sp.Rational(1, 20) * P3
    neg_dstoch = all(sum(Tneg[i, :]) == 1 for i in range(3)) \
        and all(e > 0 for e in Tneg)
    detneg = Tneg.det()
    check("NEG control [E]: the same construction with eigenvalue -1/10 is "
          "still a doubly stochastic kernel but det = -1/200 < 0, while "
          "det e^Q = e^{tr Q} > 0 always -- provably NOT embeddable; "
          "spectral positivity (RP/OS) is what makes (a)->(b) real",
          neg_dstoch and detneg == sp.Rational(-1, 200) and detneg < 0)

    check("FIREWALL (scope): this module closes the FINITE KERNEL half of "
          "DYN.MARKOV.EMBED.01 only -- e^{tQ} is dissipative statistical "
          "dynamics; the unitary/local dilation (b)->(c) is the separate "
          "open contract DYN.UNITARY.DILATION.01, untouched here", True)

    return summary("v971 Markov embedding generator (Q = log T exact)")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
