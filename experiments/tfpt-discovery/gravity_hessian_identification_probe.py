#!/usr/bin/env python3
r"""gravity_hessian_identification_probe -- EXPLORATION ONLY.

Question and honest outcome
---------------------------
This probe asks whether the corpus spectral action fixes, with no convention
left over, the leading flat-background transverse-traceless (TT) graviton
Hamiltonian used by ``spin2_hamiltonian_lattice_probe.py``.  The answer splits:
the two-derivative Einstein-Hilbert Hessian fixes the TT *shape*, two
polarizations, positivity after canonical normalization, and ``c^2=1``
exactly; but the corpus does not contain one compatible absolute coefficient.
Two independent frozen-normalization clashes therefore force the named
blocked verdict printed below rather than a silent choice of convention.

Frozen corpus chain
-------------------
1. ``v255_spectral_action_expansion.py`` uses

       S = 2 f_4 Lambda^4 a_0 + 2 f_2 Lambda^2 a_2 + f_0 a_4 + ...

   with ``f_4=int_0^inf u f(u)du``, ``f_2=int_0^inf f(u)du``,
   ``f_0=f(0)``.  For the KMS cutoff ``f(u)=exp(-u)``, v259 gives
   ``(f_4,f_2,f_0)=(1,1,1)`` exactly.  The finite triple in v252/v255 has
   ``N_F=96=2*(3*16)``: 48 particle Weyl states and their 48 antiparticles.

2. In the stated Dirac/Gilkey convention,

       a_2|_R = -(4 pi)^(-2) (N_F/12) int sqrt(g) R
               = -N_F/(192 pi^2) int sqrt(g) R.

   Reading the Euclidean minus sign as the positive Lorentzian
   Einstein-Hilbert coefficient, the *v255 doubled expansion* gives

       1/(16 pi G_ind) = 2 f_2 Lambda^2 N_F/(192 pi^2)
                       = f_2 Lambda^2 N_F/(96 pi^2).

   Since ``Mbar^2=1/(8 pi G)``, hence
   ``1/(16 pi G)=Mbar^2/2``, this branch gives

       Lambda/Mbar = pi sqrt(48/(f_2 N_F)) = pi/sqrt(2)

   for ``N_F=96`` and ``f_2=1``.  Combined with the cutoff probe's frozen
   ``M_eff/Lambda=2.553732935377702``, it conditionally gives the printed
   ``M_eff/Mbar``.

3. This is not a corpus-forced unique number.  ``v36`` writes the same
   expansion without the factors 2, while ``v68`` freezes

       1/(16 pi G) = f_2 Lambda^2 d/(192 pi^2),
       d in {16=dim S^+, 32=2^g_car},

   rather than ``N_F=96``.  The resulting four corpus-readable values are
   ``pi/sqrt(2)``, ``pi``, ``pi*sqrt(6)``, and ``pi*sqrt(3)``.  This probe
   displays all four and refuses to promote the v255 branch to a unique
   induced Planck normalization.

TT Hessian chain
----------------
Use ADM variables with lapse ``N=1``, shift ``N_i=0``, and
``gamma_ij=delta_ij+h_ij^TT``, where ``partial_i h_ij=0`` and ``h_ii=0``.
Then ``K_ij=(1/2) dot(h_ij)``, ``K=0`` to linear order, and

    [sqrt(g) R]^(2)_TT
      = (1/4) [dot(h_TT):dot(h_TT)
               - grad(h_TT):grad(h_TT)]

modulo a boundary term.  Therefore

    S_EH^(2) = (Mbar^2/8) int [dot(h_TT)^2-(grad h_TT)^2].

With Frobenius-orthonormal plus/cross tensors and canonical fields
``q_A=(Mbar/2) h_A``, ``A in {+,x}``, this becomes

    L_TT = (1/2) sum_A [dot(q_A)^2-(grad q_A)^2],
    p_A  = dot(q_A),
    H_TT = (1/2) sum_A [p_A^2+(grad q_A)^2].

The exact phase-space Hessian is ``diag(k^2,k^2,1,1)``.  Thus the leading
two-derivative shape is exactly the lattice witness, has two TT helicities,
and has ``c^2=1`` with no superluminal correction at this order.  Its
conversion from metric amplitude to canonical amplitude still inherits the
blocked absolute Einstein-Hilbert coefficient above.

Scalaron consistency cross-check
--------------------------------
``v253`` freezes ``M_scal/Mbar=c3^(7/2)``, ``c3=1/(8 pi)``.  ``v36`` freezes
the spectral-action matching

    M_scal^2/Mbar^2 = 6 (4 pi)^2/f_0.

But v259's KMS cutoff fixes ``f_0=1``.  It therefore predicts
``M_scal/Mbar=4 pi sqrt(6)``, not ``c3^(7/2)``.  Reproducing the latter would
require ``f_0=6(4 pi)^2/c3^7``, not one.  v259 removes the *ratio*
``f_2/f_0`` from the PS/grav kappa formula,
``kappa=sqrt(c_PS/c_grav)``, but that cancellation cannot repair this
absolute-``f_0`` clash.

Consistency triangle and mutants
--------------------------------
The one predeclared census comparison is the integer ``c3``-power ladder
``c3^n``, ``n=-8,...,8``.  The conditional v255 ratio
``M_eff/M_scal`` is compared only with that family; the nearest rung and its
relative mismatch are reported, with no post-hoc constants tried.

For the non-KMS mutant ``f(u)=exp(-u^2)``, v259's moment convention gives
``(f_4,f_2,f_0)=(1/2,sqrt(pi)/2,1)``.  Holding ``Mbar`` fixed shifts
``Lambda`` by ``sqrt(2/sqrt(pi))`` relative to the KMS branch.  Replacing the
full ``N_F=96`` trace by one state shifts it by ``sqrt(96)``.  Both controls
show that the cutoff and finite-triple multiplicity are load-bearing.

Scope
-----
This is an exploration-only consistency probe: leading two derivatives,
quadratic order, flat background, induced-gravity reading.  It does not
establish the nonlinear constraint algebra, diffeomorphism Ward identities,
or universal matter coupling, all of which remain [O].  No paper, ledger,
verification, scorecard, or website status follows from this result.
"""

import sys

import mpmath as mp
import sympy as sp


MP_DPS = 50
FINITE_TRIPLE_DIMENSION = 96
PARTICLE_WEYL_STATES = 48
GENERATIONS = 3
WEYL_STATES_PER_GENERATION = 16
V255_SPECTRAL_FACTOR_A2 = 2
FROZEN_M_EFF_OVER_LAMBDA = mp.mpf("2.553732935377702")
C3_LADDER_EXPONENTS = tuple(range(-8, 9))
EXACT_MATCH_TOLERANCE = mp.mpf("1e-12")
CHECKS = []


def check(name, condition, detail):
    """Record one deterministic executable assertion."""
    passed = bool(condition)
    CHECKS.append(passed)
    print("  [%s] %-42s %s" % (
        "PASS" if passed else "FAIL", name, detail))
    return passed


def frobenius(left, right):
    """Exact Frobenius inner product for two SymPy matrices."""
    return sp.simplify(sum(
        left[row, column] * right[row, column]
        for row in range(left.rows)
        for column in range(left.cols)
    ))


def main():
    mp.mp.dps = MP_DPS
    print("=" * 100)
    print("gravity_hessian_identification_probe -- spectral-action to TT Hessian")
    print("EXPLORATION ONLY; complete shape test plus named normalization blockers")
    print("=" * 100)

    pi = sp.pi
    u = sp.symbols("u", nonnegative=True)
    curvature = sp.symbols("R", real=True)
    cutoff_scale, reduced_planck_mass = sp.symbols(
        "Lambda Mbar", positive=True)

    kms_cutoff = sp.exp(-u)
    f0 = kms_cutoff.subs(u, 0)
    f2 = sp.integrate(kms_cutoff, (u, 0, sp.oo))
    f4 = sp.integrate(u * kms_cutoff, (u, 0, sp.oo))
    check(
        "KMS moments in v259 convention",
        (f4, f2, f0) == (1, 1, 1),
        "(f4,f2,f0)=%s" % ((f4, f2, f0),),
    )

    multiplicity_ok = (
        PARTICLE_WEYL_STATES
        == GENERATIONS * WEYL_STATES_PER_GENERATION
        and FINITE_TRIPLE_DIMENSION == 2 * PARTICLE_WEYL_STATES
    )
    check(
        "finite-triple multiplicity",
        multiplicity_ok,
        "N_F=96=2*(3*16): 48 particles + 48 antiparticles",
    )

    a2_density = -sp.Rational(
        FINITE_TRIPLE_DIMENSION, 192) * curvature / pi ** 2
    expected_a2_density = (
        -FINITE_TRIPLE_DIMENSION * curvature / (192 * pi ** 2))
    check(
        "exact Dirac/Gilkey a2 coefficient",
        sp.simplify(a2_density - expected_a2_density) == 0,
        "a2|R=-N_F R/(192 pi^2), N_F=%d"
        % FINITE_TRIPLE_DIMENSION,
    )

    v255_eh_coefficient = sp.simplify(
        -V255_SPECTRAL_FACTOR_A2 * f2 * cutoff_scale ** 2
        * a2_density / curvature)
    expected_v255_coefficient = (
        f2 * cutoff_scale ** 2 * FINITE_TRIPLE_DIMENSION
        / (96 * pi ** 2))
    check(
        "v255 doubled a2 prefactor",
        sp.simplify(
            v255_eh_coefficient - expected_v255_coefficient) == 0,
        "1/(16piG)=f2 Lambda^2 N_F/(96pi^2)",
    )

    lambda_over_mbar_v255 = sp.simplify(sp.sqrt(
        48 * pi ** 2 / (f2 * FINITE_TRIPLE_DIMENSION)))
    lambda_over_mbar_single_96 = sp.simplify(sp.sqrt(
        96 * pi ** 2 / (f2 * FINITE_TRIPLE_DIMENSION)))
    lambda_over_mbar_v68_d16 = sp.sqrt(96 * pi ** 2 / 16)
    lambda_over_mbar_v68_d32 = sp.sqrt(96 * pi ** 2 / 32)
    check(
        "conditional v255 Planck solve",
        sp.simplify(lambda_over_mbar_v255 - pi / sp.sqrt(2)) == 0,
        "Lambda/Mbar=pi/sqrt(2)=%.12f"
        % float(lambda_over_mbar_v255),
    )

    normalization_branches = (
        lambda_over_mbar_v255,
        lambda_over_mbar_single_96,
        lambda_over_mbar_v68_d16,
        lambda_over_mbar_v68_d32,
    )
    branches_distinct = len({
        round(float(value), 12) for value in normalization_branches
    }) == 4
    check(
        "corpus normalization clash exposed",
        branches_distinct,
        "v255/N96=%.9f; single/N96=%.9f; v68/d16=%.9f; v68/d32=%.9f"
        % tuple(float(value) for value in normalization_branches),
    )

    # Frobenius-orthonormal TT basis for a wave travelling along z.
    e_plus = sp.diag(1, -1, 0) / sp.sqrt(2)
    e_cross = sp.Matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0],
    ]) / sp.sqrt(2)
    gram = sp.Matrix([
        [frobenius(left, right) for right in (e_plus, e_cross)]
        for left in (e_plus, e_cross)
    ])
    check(
        "two orthonormal TT helicities",
        gram == sp.eye(2)
        and sp.trace(e_plus) == 0
        and sp.trace(e_cross) == 0
        and e_plus[:, 2] == sp.zeros(3, 1)
        and e_cross[:, 2] == sp.zeros(3, 1),
        "Gram(e_+,e_x)=I_2; trace=0 and k^i e_ij=0",
    )

    hp_dot, hx_dot, hp_grad, hx_grad = sp.symbols(
        "hdot_plus hdot_cross hgrad_plus hgrad_cross", real=True)
    h_dot = hp_dot * e_plus + hx_dot * e_cross
    h_grad = hp_grad * e_plus + hx_grad * e_cross
    adm_tt_density = sp.simplify(sp.Rational(1, 4) * (
        frobenius(h_dot, h_dot) - frobenius(h_grad, h_grad)))
    expected_adm_density = sp.Rational(1, 4) * (
        hp_dot ** 2 + hx_dot ** 2 - hp_grad ** 2 - hx_grad ** 2)
    check(
        "ADM TT quadratic density",
        sp.simplify(adm_tt_density - expected_adm_density) == 0,
        "[sqrt(g)R]TT^(2)=1/4[(dot h)^2-(grad h)^2]",
    )

    wave_number = sp.symbols("k", positive=True)
    q_plus, q_cross = sp.symbols("q_plus q_cross", real=True)
    qdot_plus, qdot_cross = sp.symbols(
        "qdot_plus qdot_cross", real=True)
    p_plus, p_cross = sp.symbols("p_plus p_cross", real=True)
    canonical_lagrangian = sp.Rational(1, 2) * (
        qdot_plus ** 2 + qdot_cross ** 2
        - wave_number ** 2 * (q_plus ** 2 + q_cross ** 2))
    momenta = (
        sp.diff(canonical_lagrangian, qdot_plus),
        sp.diff(canonical_lagrangian, qdot_cross),
    )
    hamiltonian = sp.simplify(
        p_plus * qdot_plus + p_cross * qdot_cross
        - canonical_lagrangian)
    hamiltonian = hamiltonian.subs({
        qdot_plus: p_plus,
        qdot_cross: p_cross,
    })
    expected_hamiltonian = sp.Rational(1, 2) * (
        p_plus ** 2 + p_cross ** 2
        + wave_number ** 2 * (q_plus ** 2 + q_cross ** 2))
    phase_variables = sp.Matrix((q_plus, q_cross, p_plus, p_cross))
    phase_hessian = sp.hessian(hamiltonian, phase_variables)
    check(
        "canonical TT Hamiltonian match",
        momenta == (qdot_plus, qdot_cross)
        and sp.simplify(hamiltonian - expected_hamiltonian) == 0
        and phase_hessian
        == sp.diag(wave_number ** 2, wave_number ** 2, 1, 1),
        "H=1/2[p_TT^2+k^2 q_TT^2], Hessian=diag(k^2,k^2,1,1)",
    )
    check(
        "luminal two-derivative propagation",
        sp.solve(
            sp.Eq(wave_number ** 2, sp.Symbol("omega") ** 2),
            sp.Symbol("omega"))[-1] == wave_number,
        "omega^2=k^2, hence c^2=1 exactly",
    )

    c3 = 1 / (8 * pi)
    scalaron_target = c3 ** sp.Rational(7, 2)
    scalaron_from_kms_a4 = sp.sqrt(6 * (4 * pi) ** 2 / f0)
    required_f0 = sp.simplify(6 * (4 * pi) ** 2 / c3 ** 7)
    scalaron_mismatch = sp.simplify(
        scalaron_from_kms_a4 / scalaron_target)
    check(
        "v253 scalaron target",
        abs(float(scalaron_target) / 1.256e-5 - 1.0) < 1.0e-3,
        "M_scal/Mbar=c3^(7/2)=%.12e" % float(scalaron_target),
    )
    check(
        "KMS scalaron clash exposed",
        f0 == 1
        and required_f0 != 1
        and float(scalaron_mismatch) > 1.0e6,
        "v36+f0=1 gives %.9f, target %.12e; ratio %.6e; "
        "required f0=%.6e"
        % (
            float(scalaron_from_kms_a4),
            float(scalaron_target),
            float(scalaron_mismatch),
            float(required_f0),
        ),
    )
    check(
        "v259 kappa boundary respected",
        sp.simplify(f2 / f0) == 1,
        "f2/f0=1 removes kappa's scheme ratio, not absolute f0",
    )

    lambda_v255_numeric = mp.mpf(str(sp.N(lambda_over_mbar_v255, MP_DPS)))
    scalaron_numeric = mp.mpf(str(sp.N(scalaron_target, MP_DPS)))
    m_eff_over_mbar = (
        FROZEN_M_EFF_OVER_LAMBDA * lambda_v255_numeric)
    m_eff_over_scalaron = m_eff_over_mbar / scalaron_numeric
    c3_numeric = mp.mpf(str(sp.N(c3, MP_DPS)))
    ladder = {
        exponent: c3_numeric ** exponent
        for exponent in C3_LADDER_EXPONENTS
    }
    nearest_exponent = min(
        ladder,
        key=lambda exponent: abs(
            mp.log(m_eff_over_scalaron / ladder[exponent])),
    )
    nearest_value = ladder[nearest_exponent]
    ladder_relative_mismatch = abs(
        m_eff_over_scalaron / nearest_value - 1)
    check(
        "predeclared c3-ladder comparison",
        nearest_exponent == -4
        and ladder_relative_mismatch > EXACT_MATCH_TOLERANCE,
        "M_eff/M_scal=%.9e; nearest c3^n is n=%d, rel.mismatch=%.6f"
        % (
            float(m_eff_over_scalaron),
            nearest_exponent,
            float(ladder_relative_mismatch),
        ),
    )

    gaussian_cutoff = sp.exp(-u ** 2)
    gaussian_moments = (
        sp.integrate(u * gaussian_cutoff, (u, 0, sp.oo)),
        sp.integrate(gaussian_cutoff, (u, 0, sp.oo)),
        gaussian_cutoff.subs(u, 0),
    )
    gaussian_lambda_shift = sp.simplify(
        sp.sqrt(f2 / gaussian_moments[1]))
    check(
        "Gaussian cutoff mutant",
        gaussian_moments
        == (sp.Rational(1, 2), sp.sqrt(pi) / 2, 1)
        and gaussian_lambda_shift == sp.sqrt(2 / sp.sqrt(pi))
        and gaussian_lambda_shift != 1,
        "(f4,f2,f0)=%s; Lambda shift=%.9f"
        % (gaussian_moments, float(gaussian_lambda_shift)),
    )

    multiplicity_drop_shift = sp.sqrt(FINITE_TRIPLE_DIMENSION)
    lambda_single_state = sp.simplify(
        lambda_over_mbar_v255 * multiplicity_drop_shift)
    check(
        "fermion-multiplicity mutant",
        multiplicity_drop_shift == 4 * sp.sqrt(6)
        and sp.simplify(lambda_single_state - 4 * sp.sqrt(3) * pi) == 0,
        "N_F:96->1 shifts Lambda by sqrt(96)=%.9f to %.9f Mbar"
        % (float(multiplicity_drop_shift), float(lambda_single_state)),
    )

    all_checks_pass = all(CHECKS)
    verdict = (
        "HESSIAN_IDENTIFICATION_BLOCKED("
        "CORPUS_NORMALIZATION_AND_SCALARON)"
        if all_checks_pass
        else "HESSIAN_IDENTIFICATION_BLOCKED(PROBE_CHECK_FAILURE)"
    )

    print("\nCONDITIONAL v255/N_F=96 BRANCH")
    print("  Lambda/Mbar      = pi/sqrt(2) = %.12f"
          % float(lambda_over_mbar_v255))
    print("  M_eff/Mbar       = %.12f" % float(m_eff_over_mbar))
    print("  M_scal/Mbar      = %.12e" % float(scalaron_target))
    print("  M_eff/M_scal     = %.12e" % float(m_eff_over_scalaron))
    print("  nearest c3 rung  = c3^%d; relative mismatch %.9f (NO MATCH)"
          % (nearest_exponent, float(ladder_relative_mismatch)))

    print("\nCORPUS COEFFICIENT BRANCHES")
    print("  v255 doubled a2, N_F=96 : %.12f" % float(
        lambda_over_mbar_v255))
    print("  v36/single a2, N_F=96   : %.12f" % float(
        lambda_over_mbar_single_96))
    print("  v68 single a2, d=16     : %.12f" % float(
        lambda_over_mbar_v68_d16))
    print("  v68 single a2, d=32     : %.12f" % float(
        lambda_over_mbar_v68_d32))

    print("\nHESSIAN AND SCALARON")
    print("  TT Hamiltonian   = 1/2 sum_A[p_A^2+(grad q_A)^2], A={+,x}")
    print("  phase Hessian    = diag(k^2,k^2,1,1); c^2=1 exactly")
    print("  canonical field  = q_A=(Mbar/2) h_A, conditional on EH matching")
    print("  v36 with f0=1    = M_scal/Mbar=%.12f" % float(
        scalaron_from_kms_a4))
    print("  v253 target      = c3^(7/2)=%.12e; mismatch factor %.6e"
          % (float(scalaron_target), float(scalaron_mismatch)))

    print("\nMUTANTS")
    print("  exp(-u^2)        : Lambda shift x %.12f"
          % float(gaussian_lambda_shift))
    print("  N_F=96 -> 1      : Lambda shift x %.12f"
          % float(multiplicity_drop_shift))

    print("\nVERDICT: %s" % verdict)
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("\nFIVE-SENTENCE CONCLUSION")
    print("1. The v255 doubled-a2 and N_F=96 branch conditionally gives "
          "Lambda/Mbar=pi/sqrt(2) and M_eff/Mbar=%.9f."
          % float(m_eff_over_mbar))
    print("2. Its exact ADM TT reduction gives two canonical helicities, a "
          "positive Hamiltonian, and c^2=1 at quadratic two-derivative order.")
    print("3. The corpus also supports three different Planck-normalization "
          "branches, so no single Lambda/Mbar is presently corpus-forced.")
    print("4. The KMS value f0=1 makes v36 predict M_scal/Mbar=4pi*sqrt(6), "
          "incompatible with v253's c3^(7/2), and kappa's ratio cancellation "
          "does not repair that absolute mismatch.")
    print("5. The cutoff and multiplicity mutants move Lambda as expected, so "
          "the honest result is the named blocked verdict while nonlinear "
          "constraints and universal matter coupling remain [O].")
    print("=" * 100)

    expected_verdict = (
        "HESSIAN_IDENTIFICATION_BLOCKED("
        "CORPUS_NORMALIZATION_AND_SCALARON)")
    return 0 if all_checks_pass and verdict == expected_verdict else 1


if __name__ == "__main__":
    sys.exit(main())
