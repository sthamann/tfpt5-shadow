#!/usr/bin/env python3
r"""spin2_formfactor_ghostfree_probe -- EXPLORATION ONLY.

Quadratic question
------------------
Let z=p^2 be the Lorentzian pole variable and A=Mbar^2/4.  In the
Biswas--Gerwick--Koivisto--Mazumdar (BGKM) normalization, an equivalent
three-form-factor curvature basis is

  S = (1/2) int d^4x sqrt(-g) [
        Mbar^2 R
        + R F_1(Box) R
        + R_{mu nu} F_2(Box) R^{mu nu}
        + C_{mu nu rho sigma} F_3(Box) C^{mu nu rho sigma} ].

After expansion about a stationary flat background and diffeomorphism
quotienting, its complete source-saturated physical quadratic action is

  S_phys^(2) = (1/2) int_p h(-p) A z [
      a(z) P^(2) + (a(z)-3 c(z)) P_s^(0) ] h(p),

and

  Pi(z) = A^(-1) [ P^(2)/(z a(z))
                   + P_s^(0)/(z (a(z)-3 c(z))) ].

This is Eq. (26) of Biswas--Koivisto--Mazumdar, arXiv:1302.0532, derived
from Biswas--Gerwick--Koivisto--Mazumdar, Phys. Rev. Lett. 108, 031101
(2012), arXiv:1110.5249.  P^(2) is the TT projector; P_s^(0) is the
transverse scalar projector.  The spin-1 and longitudinal scalar blocks
vanish by the linearized diffeomorphism Ward identities.

The minimal factorized R+R^2 completion tested here is

  a(z) = exp(-z/M^2),
  c(z) = a(z) [1 - 2 z/(3 M_scal^2)],

so a-3c = -2 a(z)(1-z/M_scal^2).  It dresses BOTH physical blocks by
the same entire factor while preserving the corpus Starobinsky IR
kernel.  Therefore the TT and scalar inverse propagators are

  P_TT(z) = A z exp(-z/M^2),
  P_0(z)  = -2 A z (1-z/M_scal^2) exp(-z/M^2).

The form-factor scale M and the scalaron mass M_scal are kept logically
distinct; setting M=M_scal is used only for dimensionless numerical
contours.  The factorized completion is a candidate quadratic Hessian,
not something established merely by knowing the spectral cutoff.

Read-only corpus provenance
---------------------------
v253 fixes M_scal=c3^(7/2) Mbar.  v255 supplies the local a2+a4
Einstein/R^2/Weyl^2 truncation.  v259 proves that the spectral-action
cutoff itself is the seam KMS weight f(u)=exp(-u), with f0=f2=f4=1.
But v304 correctly warns that the trace regulator f(D^2/Lambda^2) is
not, without an off-shell Hessian derivation, identical to a(Box).
Thus CUTOFF_CORPUS_FROZEN is true while the map cutoff -> the specific
factorized BGKM Hessian remains open.

Reflection-positivity scope
---------------------------
The literal one-dimensional zero-spatial-momentum transform

  int dp exp(i p t) exp(-p^2/M^2)/p^2

is infrared divergent.  A valid finite test of full OS positivity fixes
nonzero spatial momentum k.  At M=k=1 its time covariance is

  G_k(t) = int dp/(2 pi) exp(i p t)
           exp(-(p^2+k^2))/(p^2+k^2)
         = [e^(-kt) erfc(k-t/2)+e^(kt) erfc(k+t/2)]/(4k).

Full Gaussian OS positivity requires [G_k(t_i+t_j)] to be positive
semidefinite for every positive-time grid.  The probe finds an explicit
negative eigenvalue.  Christodoulou--Modesto, arXiv:1803.08843, proves
only positivity in the coincidence limit and explicitly calls that a
necessary, not sufficient, test; it does not override this matrix
counterexample.

Expected complete/named-dead verdict:

  FORMFACTOR_GHOSTFREE_FAILS(RP_SHADOW)
  SCALARON_SHIFT(1)
  CUTOFF_CORPUS_FROZEN

The pole spectrum is exactly graviton + scalaron, but the requested
quadratic OS-positive conclusion is false for this exponential
covariance.  No paper, ledger, verification, or website status follows
from this exploration probe.
"""

import sys

import mpmath as mp
import sympy as sp


MP_DPS = 60
COUNT_TOL = mp.mpf("1e-14")
RP_NEGATIVE_TOL = mp.mpf("1e-10")
TT_RADII = ("0.1", "0.5", "2", "10", "100")
SCALAR_RADII = ("0.5", "0.9", "1.1", "2", "10", "100")
COSH_RADII = ("2", "3", "25", "100")
OS_TIME_GRID = ("0.1", "0.2", "0.4", "0.8", "1.6")
CHECKS = []


def check(name, condition, detail):
    """Record one executable assertion."""
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-36s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def argument_principle_count(log_derivative, radius):
    """Numerically evaluate (2 pi i)^-1 integral f'/f dz on |z|=radius."""
    radius = mp.mpf(radius)

    def integrand(theta):
        point = radius * mp.exp(1j * theta)
        return log_derivative(point) * point

    raw_count = mp.quad(integrand, [0, 2 * mp.pi]) / (2 * mp.pi)
    nearest = int(mp.nint(mp.re(raw_count)))
    reliable = (abs(mp.re(raw_count) - nearest) < COUNT_TOL
                and abs(mp.im(raw_count)) < COUNT_TOL)
    return nearest, raw_count, reliable


def count_table(log_derivative, radii):
    """Return integer contour counts and their numerical reliability."""
    rows = []
    for radius in radii:
        count, raw_count, reliable = argument_principle_count(
            log_derivative, radius)
        rows.append((mp.mpf(radius), count, raw_count, reliable))
    return rows


def format_counts(rows):
    return ", ".join(
        "R=%s:%d" % (mp.nstr(radius, 4), count)
        for radius, count, _, _ in rows)


def euclidean_time_covariance(time, spatial_momentum=mp.mpf(1)):
    """Closed form of the exponentially dressed fixed-|k| covariance."""
    time = abs(mp.mpf(time))
    spatial_momentum = mp.mpf(spatial_momentum)
    return (
        mp.exp(-spatial_momentum * time)
        * mp.erfc(spatial_momentum - time / 2)
        + mp.exp(spatial_momentum * time)
        * mp.erfc(spatial_momentum + time / 2)
    ) / (4 * spatial_momentum)


def main():
    mp.mp.dps = MP_DPS
    print("=" * 88)
    print("spin2_formfactor_ghostfree_probe -- entire poles plus full OS-2 witness")
    print("EXPLORATION ONLY; no contract or status move")
    print("=" * 88)

    z = sp.symbols("z")
    A, M2, m_scal2 = sp.symbols(
        "A M2 M_scal_sq", positive=True, finite=True)
    a = sp.exp(-z / M2)
    c = sp.factor(a * (1 - 2 * z / (3 * m_scal2)))
    tt_kernel = sp.factor(A * z * a)
    scalar_kernel = sp.factor(A * z * (a - 3 * c))

    no_finite_singularities = sp.singularities(a, z) == sp.EmptySet
    nowhere_zero = (
        sp.solve(a, z) == []
        and sp.simplify(a * sp.exp(z / M2)) == 1
    )
    check(
        "exponential entire/nonzero",
        no_finite_singularities and nowhere_zero,
        "singularities=%s, solve(a=0)=%s, a*exp(z/M^2)=1"
        % (sp.singularities(a, z), sp.solve(a, z)),
    )

    expected_scalar_kernel = -2 * A * z * (1 - z / m_scal2) * a
    check(
        "full BGKM block factorization",
        sp.simplify(scalar_kernel - expected_scalar_kernel) == 0,
        "a-3c=%s; P_TT=%s; P_0=%s"
        % (sp.factor(a - 3 * c), tt_kernel, scalar_kernel),
    )

    tt_rows = count_table(lambda point: 1 / point - 1, TT_RADII)
    tt_counts_ok = (
        all(count == 1 and reliable
            for _, count, _, reliable in tt_rows)
        and tt_rows[-1][0] == 100
    )
    check(
        "TT argument-principle counts",
        tt_counts_ok,
        "%s (M^2=1; exactly one zero through 100 M^2)"
        % format_counts(tt_rows),
    )

    tt_residue = sp.simplify(sp.limit(z / tt_kernel, z, 0))
    check(
        "massless TT residue positive",
        tt_residue == 1 / A and tt_residue.is_positive,
        "Res[1/P_TT,z=0]=%s > 0 (correct-sign graviton)" % tt_residue,
    )

    scalar_roots = sp.solve(z * (1 - z / m_scal2), z)
    scalaron_root = m_scal2
    scalaron_mass_ratio = sp.sqrt(scalaron_root) / sp.sqrt(m_scal2)
    scalaron_residue = sp.simplify(
        sp.limit((z - scalaron_root) / scalar_kernel, z, scalaron_root)
    )
    check(
        "scalaron roots and shift",
        set(scalar_roots) == {sp.Integer(0), m_scal2}
        and sp.simplify(scalaron_mass_ratio - 1) == 0
        and scalaron_residue.is_positive,
        "roots={0,M_scal^2}; M_pole/M_scal=%s; scalaron residue=%s > 0"
        % (scalaron_mass_ratio, scalaron_residue),
    )

    scalar_rows = count_table(
        lambda point: 1 / point - 1 / (1 - point) - 1,
        SCALAR_RADII,
    )
    scalar_counts_ok = (
        [count for _, count, _, _ in scalar_rows] == [1, 1, 2, 2, 2, 2]
        and all(reliable for _, _, _, reliable in scalar_rows)
    )
    check(
        "scalar argument-principle counts",
        scalar_counts_ok,
        "%s (M=M_scal=1; second zero crosses at R=1)"
        % format_counts(scalar_rows),
    )

    ghost2 = sp.symbols("M_ghost_sq", positive=True, finite=True)
    local_kernel = sp.factor(A * z * (1 - z / ghost2))
    local_residue_zero = sp.simplify(sp.limit(z / local_kernel, z, 0))
    local_residue_ghost = sp.simplify(
        sp.limit((z - ghost2) / local_kernel, z, ghost2))
    local_rows = count_table(
        lambda point: 1 / point - 1 / (1 - point), ("2", "10", "100"))
    check(
        "local-truncation ghost mutant",
        all(count == 2 and reliable
            for _, count, _, reliable in local_rows)
        and local_residue_zero == 1 / A
        and local_residue_ghost == -1 / A,
        "%s; poles={0,M_ghost^2}, residues={+1/A,-1/A}"
        % format_counts(local_rows),
    )

    cosh_first_zero = -sp.pi ** 2 / 4
    cosh_zero_exact = sp.simplify(
        sp.cosh(sp.I * sp.pi / 2)) == 0
    cosh_rows = count_table(
        lambda point: (
            1 / point
            + mp.tanh(mp.sqrt(point)) / (2 * mp.sqrt(point))
        ),
        COSH_RADII,
    )
    check(
        "zero-carrying entire mutant",
        cosh_zero_exact
        and [count for _, count, _, _ in cosh_rows] == [1, 2, 3, 4]
        and all(reliable for _, _, _, reliable in cosh_rows),
        "cosh(sqrt(z)) is entire but has first zero z=%s; %s"
        % (cosh_first_zero, format_counts(cosh_rows)),
    )

    u = sp.symbols("u", nonnegative=True)
    cutoff = sp.exp(-u)
    f0 = cutoff.subs(u, 0)
    f2 = sp.integrate(cutoff, (u, 0, sp.oo))
    f4 = sp.integrate(u * cutoff, (u, 0, sp.oo))
    cutoff_verdict = "CUTOFF_CORPUS_FROZEN"
    check(
        "v259 KMS cutoff reproduced",
        (f0, f2, f4) == (1, 1, 1),
        "f(u)=exp(-u), (f0,f2,f4)=(%s,%s,%s); cutoff frozen, "
        "cutoff-to-Hessian map still open" % (f0, f2, f4),
    )

    # The requested k=0 transform diverges as int dp/p^2.  Full OS positivity
    # would imply positivity after spatial Fourier transform at every k != 0,
    # so one negative fixed-k matrix is a decisive counterexample.
    times = [mp.mpf(value) for value in OS_TIME_GRID]
    os_matrix = mp.matrix([
        [euclidean_time_covariance(left + right)
         for right in times]
        for left in times
    ])
    eigenvalues, eigenvectors = mp.eigsy(os_matrix)
    minimum_eigenvalue = eigenvalues[0]
    negative_vector = eigenvectors[:, 0]
    negative_quadratic_form = (
        negative_vector.T * os_matrix * negative_vector)[0]
    diagonal_positive = all(os_matrix[index, index] > 0
                            for index in range(len(times)))
    rp_fails = (
        diagonal_positive
        and minimum_eigenvalue < -RP_NEGATIVE_TOL
        and negative_quadratic_form < -RP_NEGATIVE_TOL
    )
    check(
        "full OS-2 counterexample",
        rp_fails,
        "k=M, t=%s: diag>0 but lambda_min=%s, witness q=%s"
        % (
            list(OS_TIME_GRID),
            mp.nstr(minimum_eigenvalue, 14),
            mp.nstr(negative_quadratic_form, 14),
        ),
    )
    check(
        "RP witness coefficients",
        abs(mp.fsum(value * value for value in negative_vector) - 1)
        < COUNT_TOL,
        "normalized c=%s"
        % [mp.nstr(negative_vector[index], 10)
           for index in range(len(times))],
    )

    pole_sector_clean = all(CHECKS[:8])
    all_diagnostics_reproduced = all(CHECKS)
    if not all_diagnostics_reproduced:
        verdict = "FORMFACTOR_GHOSTFREE_FAILS(PROBE_ALGEBRA)"
    elif rp_fails:
        verdict = "FORMFACTOR_GHOSTFREE_FAILS(RP_SHADOW)"
    elif pole_sector_clean:
        verdict = "FORMFACTOR_GHOSTFREE_PROVED_QUADRATIC"
    else:
        verdict = "FORMFACTOR_GHOSTFREE_FAILS(POLE_STRUCTURE)"

    print("\nQUADRATIC RESULT")
    print("  TT zeros:       exactly {0}; contour count 1 through R=100 M^2")
    print("  scalar zeros:   exactly {0,M_scal^2}; M_pole/M_scal = 1")
    print("  residue signs:  TT massless +; scalaron +; local mutant (+,-)")
    print("  RP witness:     FAIL, lambda_min=%s at fixed |k|=M"
          % mp.nstr(minimum_eigenvalue, 14))
    print("  v259 finding:   f(u)=e^-u and moments (1,1,1), but no automatic "
          "f -> BGKM Hessian identity")
    print("\nVERDICT: %s" % verdict)
    print("SCALARON_SHIFT(%s)" % scalaron_mass_ratio)
    print(cutoff_verdict)
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("BOUNDARY: pole ghost-freedom passes for the factorized candidate; "
          "full quadratic reflection positivity is explicitly false. "
          "GRAV.SPIN2.EMERGENCE.01 remains [O].")
    print("=" * 88)

    expected_named_dead = (
        verdict == "FORMFACTOR_GHOSTFREE_FAILS(RP_SHADOW)"
        and scalaron_mass_ratio == 1
        and cutoff_verdict == "CUTOFF_CORPUS_FROZEN"
    )
    return 0 if all_diagnostics_reproduced and expected_named_dead else 1


if __name__ == "__main__":
    sys.exit(main())
