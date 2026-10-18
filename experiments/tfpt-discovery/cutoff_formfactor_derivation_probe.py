#!/usr/bin/env python3
r"""cutoff_formfactor_derivation_probe -- EXPLORATION ONLY.

Question and scope
------------------
This probe asks what follows from the frozen spectral cutoff

    S_f(D) = Tr f(D^2/Lambda^2),             f(u) = exp(-u).

It is important to distinguish the universal Barvinsky--Vilkovisky (BV)
*basic heat-kernel structure function* derived below from the normalized TT
inverse-propagator form factor of a particular gravitational Hessian.  The
former is fixed by the cutoff.  The latter additionally requires the precise
Laplace-type operator (bundle trace, endomorphism E, connection curvature,
finite-triple multiplicities), all local a_2 terms, and projection of the
complete curvature basis onto TT/scalar metric perturbations.  Consequently,
the often-made identification a_TT = phi is tested here as a candidate; it is
not silently promoted to a theorem.

Proper-time chain
-----------------
For a cutoff admitting a Laplace representation,

    f(y) = integral_0^infinity ds f_tilde(s) exp(-s y),

functional calculus gives

    Tr f(D^2/Lambda^2)
      = integral_0^infinity ds f_tilde(s)
          Tr exp[-s D^2/Lambda^2].

For the frozen KMS cutoff f(y)=exp(-y), f_tilde(s)=delta(s-1), so there is no
proper-time integration left:

    S_f(D) = Tr exp[-D^2/Lambda^2] = Tr K(t),  t=Lambda^(-2).

Write a Laplace-type operator in the BV convention as

    D^2 = -Box + E,       P = -E + R/6,
    calR_{mu nu} = [nabla_mu,nabla_nu].

On an asymptotically flat, boundaryless 2 omega-dimensional manifold, the
complete BV expansion through second order in generalized curvatures is

 Tr K(t) = (4 pi t)^(-omega) integral d^(2 omega)x sqrt(g) tr {
     1 + t P
     + t^2 [
         R_{mu nu} F1(x) R^{mu nu}
       + R F2(x) R
       + P F3(x) R
       + P F4(x) P
       + calR_{mu nu} F5(x) calR^{mu nu}
     ] + O(curvature^3) },                    x = -t Box,

where

    phi(x) = integral_0^1 dxi exp[-xi(1-xi)x],
    F1(x) = [phi(x)-1+x/6]/x^2,
    F2(x) = (1/8){phi(x)/36 + [phi(x)-1]/(3x)
                         - [phi(x)-1+x/6]/x^2},
    F3(x) = phi(x)/12 + [phi(x)-1]/(2x),
    F4(x) = phi(x)/2,
    F5(x) = -[phi(x)-1]/(2x).

The apparent singularities are removable because

    phi(x) = 1-x/6+x^2/60-x^3/840+... .

This is the second-order covariant perturbation theory formula of
A. O. Barvinsky and G. A. Vilkovisky, "Beyond the Schwinger-DeWitt
Technique: Converting Loops into Trees and In-In Currents",
Nucl. Phys. B 282 (1987) 163--188, DOI 10.1016/0550-3213(87)90681-X.
The displayed five-form-factor convention is the standard BV P-basis.

At t=Lambda^(-2), a plane wave with Euclidean p^2 has x=z=p^2/Lambda^2,
and the universal function is therefore exactly

    a_BV(z) := phi(z)
             = integral_0^1 dxi exp[-xi(1-xi)z]
             = sqrt(pi/z) exp(-z/4) erfi(sqrt(z)/2).

For a general cutoff g, the same basic structure is

    a_g(z) = integral_0^1 dxi g(xi(1-xi)z).

This proves the cutoff-to-BV-master-function map.  It does NOT by itself prove
that the complete TT Hessian multiplier equals a_BV: F1 is already a different
combination of phi, and E/calR traces mix the five displayed companions.

Comparison with the review exponential
--------------------------------------
Both exp(-z) and a_BV(z) are entire, but only exp(-z) is zero-free.  The
argument-principle computation below finds complex zeros of a_BV.  On the
positive real axis,

    a_BV(z) = 2/z + 4/z^2 + 24/z^3 + O(z^-4),

whereas exp(-z) is exponentially suppressed.  If one nevertheless uses
1/[p^2 a_BV(p^2/Lambda^2)] as a candidate propagator, it approaches the
contact value 1/(2 Lambda^2), rather than being UV suppressed.  Matching the
half-height to exp[-p^2/M_eff^2] gives

    M_eff/Lambda = sqrt(z_half/log 2).

Corpus v253 fixes M_scal=c3^(7/2) Mbar and says M_scal/Lambda is a
dimensionless finite-triple heat-kernel factor; v259 fixes f2/f0=1 but does
not compute that trace factor.  Hence this probe can give M_eff/Lambda
exactly numerically, but an exact Lambda/M_scal number is not in the cited
corpus and is not invented here.

Reflection-positive shadow
--------------------------
At fixed |k|=Lambda the candidate Euclidean covariance is

    C(p0,k) = 1 / [(p0^2+k^2) a_BV((p0^2+k^2)/Lambda^2)].

In Lambda=1 units C tends to 1/2.  That constant is a delta(t) contact term
and vanishes in an OS matrix C(t_i+t_j) for strictly positive times, so the
probe Fourier-transforms C-1/2.  A negative matrix eigenvalue is a decisive
finite reflection-positivity counterexample.

Mutants and anchor
------------------
The non-KMS Gaussian and sharp cutoffs induce, on the positive real axis,

 a_G(z)     = integral_0^1 dxi exp(-[xi(1-xi)z]^2),
 a_sharp(z) = 1                                      (0 <= z <= 4),
              1-sqrt(1-4/z)                          (z > 4).

They differ from a_BV; the sharp result is not even analytic at z=4.  The
frozen KMS moment anchor is reproduced exactly:

    (f0,f2,f4) = (f(0), integral f, integral u f) = (1,1,1).

Expected named-dead verdict:

 CUTOFF_INDUCES_BV_FORMFACTOR_GHOSTFREE_NO_RP_FAILS_SCALE_ID(2.5537329354)

No paper, ledger, verification, scorecard, or website status follows from
this exploration-only result.
"""

import sys

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import dawsn


MP_DPS = 50
CONTOUR_SAMPLES = 32768
GAUSS_LEGENDRE_ORDER = 192
ZERO_COUNT_RADII = (10.0, 20.0, 50.0, 100.0)
EXPECTED_ZERO_COUNTS = (0, 0, 4, 8)
OS_TIME_GRID = (0.1, 0.2, 0.4, 0.8, 1.6)
RP_NEGATIVE_TOL = 1.0e-8
SCALE_TOL = 5.0e-10
UV_CANCELLATION_SWITCH = 1.0e8
CHECKS = []


def check(name, condition, detail):
    """Record and print one executable assertion."""
    passed = bool(condition)
    CHECKS.append(passed)
    print("  [%s] %-38s %s" % (
        "PASS" if passed else "FAIL", name, detail))
    return passed


def phi_real(z):
    """Stable positive-real evaluation of the BV master function."""
    z = float(z)
    if z == 0.0:
        return 1.0
    return 2.0 * dawsn(np.sqrt(z) / 2.0) / np.sqrt(z)


def make_complex_phi_quadrature():
    """Return a vectorized Gauss--Legendre evaluator for complex contours."""
    nodes, weights = leggauss(GAUSS_LEGENDRE_ORDER)
    xi = (nodes + 1.0) / 2.0
    normalized_weights = weights / 2.0
    xi_width = xi * (1.0 - xi)

    def evaluate(z):
        return np.sum(normalized_weights * np.exp(-xi_width * z))

    return evaluate


def winding_zero_count(phi_complex, radius):
    """Count zeros inside |z|=radius from the phase winding of phi."""
    angles = np.linspace(
        0.0, 2.0 * np.pi, CONTOUR_SAMPLES + 1, endpoint=True)
    values = np.array([
        phi_complex(radius * np.exp(1j * angle)) for angle in angles
    ])
    unwrapped_phase = np.unwrap(np.angle(values))
    winding = (unwrapped_phase[-1] - unwrapped_phase[0]) / (2.0 * np.pi)
    return int(np.rint(winding)), float(np.min(np.abs(values)))


def regularized_candidate_covariance(momentum, spatial_momentum=1.0):
    """C(p,k)-1/2 in Lambda=1 units; the subtraction is a contact term."""
    spectral_value = momentum * momentum + spatial_momentum * spatial_momentum
    if spectral_value > UV_CANCELLATION_SWITCH:
        # From phi(s)=2/s+4/s^2+O(s^-3):
        # 1/[s phi(s)]-1/2 = -1/s+O(s^-2).
        return -1.0 / spectral_value
    return 1.0 / (spectral_value * phi_real(spectral_value)) - 0.5


def euclidean_time_covariance(time):
    """Cosine transform of the non-contact candidate covariance."""
    value, error = quad(
        regularized_candidate_covariance,
        0.0,
        np.inf,
        weight="cos",
        wvar=float(time),
        epsabs=2.0e-11,
        epsrel=2.0e-11,
        limit=1000,
        limlst=1000,
    )
    return value / np.pi, error / np.pi


def main():
    mp.mp.dps = MP_DPS
    print("=" * 96)
    print("cutoff_formfactor_derivation_probe -- frozen cutoff to BV master function")
    print("EXPLORATION ONLY; requested TT identification is tested, not assumed")
    print("=" * 96)

    z, xi, u = sp.symbols("z xi u", nonnegative=True)
    phi_series = sum(
        (-z) ** order * sp.factorial(order)
        / sp.factorial(2 * order + 1)
        for order in range(8)
    )
    expected_series = (
        1 - z / 6 + z ** 2 / 60 - z ** 3 / 840
        + z ** 4 / 15120 - z ** 5 / 332640
    )
    check(
        "BV xi-integral Taylor series",
        sp.expand(phi_series - expected_series).coeff(z, 0) == 0
        and all(
            sp.expand(phi_series - expected_series).coeff(z, power) == 0
            for power in range(6)
        ),
        "phi(z)=1-z/6+z^2/60-z^3/840+z^4/15120-...",
    )

    closed_phi = (
        sp.sqrt(sp.pi / z) * sp.exp(-z / 4)
        * sp.erfi(sp.sqrt(z) / 2)
    )
    closed_series = sp.series(closed_phi, z, 0, 6).removeO()
    check(
        "closed BV form factor",
        sp.simplify(closed_series - expected_series) == 0,
        "phi(z)=sqrt(pi/z) exp(-z/4) erfi(sqrt(z)/2)",
    )

    # Full BV scalar/bundle companions in the P-basis.  The truncated series
    # suffices to verify every removable origin limit exactly.
    phi_symbolic = phi_series
    f1 = sp.cancel((phi_symbolic - 1 + z / 6) / z ** 2)
    f2 = sp.cancel(sp.Rational(1, 8) * (
        phi_symbolic / 36
        + (phi_symbolic - 1) / (3 * z)
        - (phi_symbolic - 1 + z / 6) / z ** 2
    ))
    f3 = sp.cancel(phi_symbolic / 12 + (phi_symbolic - 1) / (2 * z))
    f4 = phi_symbolic / 2
    f5 = sp.cancel(-(phi_symbolic - 1) / (2 * z))
    companion_limits = tuple(
        sp.limit(form_factor, z, 0)
        for form_factor in (f1, f2, f3, f4, f5)
    )
    check(
        "five BV companion limits",
        companion_limits == (
            sp.Rational(1, 60),
            -sp.Rational(1, 180),
            0,
            sp.Rational(1, 2),
            sp.Rational(1, 12),
        ),
        "(F1,F2,F3,F4,F5)(0)=%s; all apparent poles removable"
        % (companion_limits,),
    )

    phi_complex = make_complex_phi_quadrature()
    zero_rows = [
        (radius,) + winding_zero_count(phi_complex, radius)
        for radius in ZERO_COUNT_RADII
    ]
    counts = tuple(row[1] for row in zero_rows)
    contours_clear = all(row[2] > 1.0e-5 for row in zero_rows)
    check(
        "argument-principle zero counts",
        counts == EXPECTED_ZERO_COUNTS and contours_clear,
        ", ".join(
            "R=%g: N=%d, min|phi|=%.3e" % row for row in zero_rows
        ),
    )
    check(
        "BV candidate is not zero-free",
        counts[-1] == 8,
        "entire phi has 8 complex zeros in |z|<100; ghost-free test fails",
    )

    large_z = mp.mpf("1000000")
    exact_large = mp.hyp1f1(1, mp.mpf(3) / 2, -large_z / 4)
    asymptotic_large = (
        2 / large_z + 4 / large_z ** 2 + 24 / large_z ** 3
    )
    relative_asymptotic_error = abs(
        exact_large / asymptotic_large - 1)
    check(
        "algebraic BV ultraviolet tail",
        relative_asymptotic_error < mp.mpf("1e-15"),
        "phi(z)=2/z+4/z^2+24/z^3+...; rel.err at 10^6=%s"
        % mp.nstr(relative_asymptotic_error, 8),
    )
    check(
        "not the review exponential",
        abs(phi_real(10.0) - np.exp(-10.0)) > 0.25,
        "phi(10)=%.12f while exp(-10)=%.12e; candidate propagator tends "
        "1/(2 Lambda^2)" % (phi_real(10.0), np.exp(-10.0)),
    )

    half_height_z = brentq(
        lambda value: phi_real(value) - 0.5, 0.0, 100.0)
    half_height_momentum = np.sqrt(half_height_z)
    effective_mass_ratio = np.sqrt(half_height_z / np.log(2.0))
    check(
        "half-height scale identification",
        abs(half_height_z - 4.520395315987465) < SCALE_TOL
        and abs(effective_mass_ratio - 2.553732935377702) < SCALE_TOL,
        "z_1/2=%.15f, p_1/2/Lambda=%.12f, M_eff/Lambda=%.12f"
        % (half_height_z, half_height_momentum, effective_mass_ratio),
    )

    times = np.array(OS_TIME_GRID)
    time_sums = sorted(set(float(left + right)
                           for left in times for right in times))
    covariance_values = {
        time: euclidean_time_covariance(time)[0] for time in time_sums
    }
    os_matrix = np.array([
        [covariance_values[float(left + right)] for right in times]
        for left in times
    ])
    eigenvalues, eigenvectors = np.linalg.eigh(os_matrix)
    minimum_eigenvalue = float(eigenvalues[0])
    witness = eigenvectors[:, 0]
    witness_quadratic_form = float(witness @ os_matrix @ witness)
    rp_fails = (
        np.all(np.diag(os_matrix) > 0.0)
        and minimum_eigenvalue < -RP_NEGATIVE_TOL
        and witness_quadratic_form < -RP_NEGATIVE_TOL
    )
    check(
        "finite OS reflection witness",
        rp_fails,
        "k=Lambda, t=%s: lambda_min=%.12f, q=%.12f"
        % (list(OS_TIME_GRID), minimum_eigenvalue,
           witness_quadratic_form),
    )
    check(
        "OS witness normalization",
        abs(float(witness @ witness) - 1.0) < 1.0e-12,
        "c=%s" % [float("%.9g" % coefficient) for coefficient in witness],
    )

    gaussian_series_quadratic = -sp.integrate(
        (xi * (1 - xi)) ** 2, (xi, 0, 1))
    check(
        "Gaussian cutoff mutant differs",
        gaussian_series_quadratic == -sp.Rational(1, 30)
        and abs(
            quad(
                lambda value: np.exp(
                    -(value * (1.0 - value) * 4.0) ** 2),
                0.0,
                1.0,
            )[0] - phi_real(4.0)
        ) > 0.08,
        "a_G(z)=1-z^2/30+... (no linear term); "
        "a_G(4)=0.623541564238 != phi(4)=%.12f" % phi_real(4.0),
    )
    sharp_at_ten = 1.0 - np.sqrt(1.0 - 4.0 / 10.0)
    check(
        "sharp cutoff mutant differs",
        abs(sharp_at_ten - phi_real(10.0)) > 0.03,
        "a_sharp=1 for z<=4 and 1-sqrt(1-4/z) for z>4; "
        "a_sharp(10)=%.12f != phi(10)=%.12f; kink at z=4"
        % (sharp_at_ten, phi_real(10.0)),
    )

    kms_cutoff = sp.exp(-u)
    moments = (
        kms_cutoff.subs(u, 0),
        sp.integrate(kms_cutoff, (u, 0, sp.oo)),
        sp.integrate(u * kms_cutoff, (u, 0, sp.oo)),
    )
    gaussian_moments = (
        sp.Integer(1),
        sp.integrate(sp.exp(-u ** 2), (u, 0, sp.oo)),
        sp.integrate(u * sp.exp(-u ** 2), (u, 0, sp.oo)),
    )
    check(
        "v259 KMS moment anchor",
        moments == (1, 1, 1),
        "f=e^-u gives (f0,f2,f4)=%s exactly" % (moments,),
    )
    check(
        "cutoff moment mutant control",
        gaussian_moments == (
            1, sp.sqrt(sp.pi) / 2, sp.Rational(1, 2)),
        "e^-u^2 gives (f0,f2,f4)=%s, distinct from (1,1,1)"
        % (gaussian_moments,),
    )

    all_checks_pass = all(CHECKS)
    ghostfree = counts[-1] == 0
    rp_label = "PASSES" if not rp_fails else "FAILS"
    verdict = (
        "CUTOFF_INDUCES_BV_FORMFACTOR_GHOSTFREE_%s_RP_%s_"
        "SCALE_ID(%.10f)"
        % ("YES" if ghostfree else "NO", rp_label, effective_mass_ratio)
    )

    print("\nDERIVED RESULT")
    print("  a_BV(z)       = integral_0^1 exp[-xi(1-xi)z] dxi")
    print("  closed form   = sqrt(pi/z) exp(-z/4) erfi(sqrt(z)/2)")
    print("  complex zeros = %s for radii %s"
          % (list(counts), list(ZERO_COUNT_RADII)))
    print("  asymptotics   = 2/z+4/z^2+24/z^3+..., not exp(-z)")
    print("  RP shadow     = FAIL, lambda_min=%.12f" % minimum_eigenvalue)
    print("  scale         = M_eff/Lambda=%.10f; Lambda/M_scal not fixed "
          "by v253/v259" % effective_mass_ratio)
    print("\nVERDICT: %s" % verdict)
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("\nFIVE-SENTENCE CONCLUSION")
    print("1. The frozen KMS cutoff exactly induces the universal BV master "
          "function phi, not the review exponential.")
    print("2. Phi is entire but has complex zeros, so the candidate "
          "zero-free ghost criterion fails.")
    print("3. Its algebraic 2/z tail leaves a contact UV propagator rather "
          "than exponential suppression.")
    print("4. The finite fixed-momentum OS matrix has a negative eigenvalue, "
          "so the candidate also fails the RP shadow.")
    print("5. Therefore the corpus gravity sector is not shown quadratically "
          "healthy by its frozen cutoff alone and still needs a complete "
          "Hessian or Hamiltonian construction.")
    print("=" * 96)

    expected_verdict = (
        "CUTOFF_INDUCES_BV_FORMFACTOR_GHOSTFREE_NO_RP_FAILS_"
        "SCALE_ID(2.5537329354)"
    )
    return 0 if all_checks_pass and verdict == expected_verdict else 1


if __name__ == "__main__":
    sys.exit(main())
