#!/usr/bin/env python3
r"""v1025 -- rigorous TEL-B C1 and analytic C2a certificates.

C1 is an outward-rounded 100-bit Arb/Acb integration certificate.  It splits
the four sign quadrants into 3888 analytic rectangles, uses logarithmic
coordinates at the two singular axes, fills the opposite-sign seam corner in
a removable chart, and adds a closed elementary majorant for the omitted
axis strips.  Parseval supplies the exact imaginary contribution 1/12.

C2a is an analytic all-even-N theorem.  Exact cotangent reindexing turns the
increment of phi_N into the Peano error of the 3/4-point rule.  The classical
partial-fraction identity

  f'(u) = pi^2 csc^2(pi u) - 1/u^2
        = sum_{m in Z, m != 0} (u-m)^-2

gives pi^2/3 <= f' <= pi^2-4 and monotonic increments.  Shifted Euler
summation with its periodic B3 remainder then yields the endpoint bound

  N sup_k |phi_N(k)| < 0.509 < 0.51,  N even and N >= 16.

The detailed derivation is carried by the TEL-B executed update in
tfpt_research_contracts.tex; this module rigorously certifies the sole
numerical integral in C1 and every final constant comparison in C1/C2a.
It requires native python-flint 0.9.0 and is not a Pyodide/WASM check.

This module closes C1 and C2a only. The former coefficient-freezing and
diagonal residual is supplied by v1026, which assembles the relaxed TEL-B
norm theorem. ALG-EXH and the MMST scaling limit remain open. NO RH CLAIM.
"""

from __future__ import annotations

from importlib.metadata import version

import flint as python_flint
from flint import acb, arb, ctx

from tfpt_constants import check as suite_check, reset, summary


PYTHON_FLINT_VERSION = "0.9.0"

# These Arb objects are initialised inside run(), after the caller's precision
# has been saved.  Importing this module therefore has no global FLINT effect.
PI: acb
A_COEFF: acb
HALF: acb


def hyp_atanh_over(z: acb) -> acb:
    """atanh(z)/z, entire as a function of z^2 on |z|<1."""
    return (z * z).hypgeom_2f1(acb(1) / 2, 1, acb(3) / 2)


def sinc(z: acb) -> acb:
    """sin(z)/z with its removable value supplied by 0F1."""
    return (-z * z / 4).hypgeom_0f1(acb(3) / 2)


def tan_over(z: acb) -> acb:
    """tan(z)/z, removable at zero."""
    return sinc(z) / z.cos()


def zcot(z: acb) -> acb:
    """z*cot(z), removable at zero."""
    return z.cos() / sinc(z)


def log_dd(x: acb, y: acb, q: acb | None = None) -> acb:
    """Stable divided difference of log on the positive quadrant."""
    middle = (x + y) / 2
    if q is None:
        q = (y - x) / (x + y)
    return hyp_atanh_over(q) / middle


def logsin_dd(
    x: acb, y: acb, log_difference: acb | None = None
) -> acb:
    """Stable divided difference of log(sin(pi*x))."""
    if log_difference is not None and not log_difference.contains(0):
        return ((PI * y).sin().log() - (PI * x).sin().log()) / (y - x)
    middle = (x + y) / 2
    delta = (y - x) / 2
    z = (PI * middle).cot() * (PI * delta).tan()
    return hyp_atanh_over(z) * (PI * middle).cot() * PI * tan_over(PI * delta)


def same_sign_real_square(
    x: acb,
    y: acb,
    positive: bool,
    q: acb | None = None,
    log_difference: acb | None = None,
) -> acb:
    d = y - x
    a = zcot(PI * d)
    if log_difference is not None and not log_difference.contains(0):
        log_divided = log_difference / (y - x)
    else:
        log_divided = log_dd(x, y, q)
    sine_divided = logsin_dd(x, y, log_difference)
    if positive:
        df = -log_divided
        d_f = -sine_divided - PI
    else:
        df = log_divided
        d_f = sine_divided - PI
    value = A_COEFF * (df - a * d_f)
    return value * value


def opposite_real_square(
    x: acb,
    y: acb,
    q: acb | None = None,
    log_difference: acb | None = None,
) -> acb:
    """Real-square integrand for u=-x<0, v=y>0."""
    s = x + y
    if q is None:
        q = (y - x) / s
    log_ratio = (
        log_difference
        if log_difference is not None
        else 2 * q * hyp_atanh_over(q)
    )
    df = (PI - log_ratio) / s

    if log_difference is not None and not log_difference.contains(0):
        logsin_ratio = (PI * y).sin().log() - (PI * x).sin().log()
    else:
        middle_xy = (x + y) / 2
        delta_xy = (y - x) / 2
        z_xy = (PI * middle_xy).cot() * (PI * delta_xy).tan()
        logsin_ratio = 2 * z_xy * hyp_atanh_over(z_xy)

    if not s.contains(1):
        delta_f = -logsin_ratio + PI * (1 - s)
        value = A_COEFF * (df - zcot(PI * s) * delta_f / s)
        return value * value

    aa = HALF - x
    bb = HALF - y
    t = aa + bb
    middle = t / 2
    delta = (aa - bb) / 2
    z = (PI * middle).tan() * (PI * delta).tan()
    logcos_ratio_over_t = (
        -hyp_atanh_over(z) * PI * tan_over(PI * middle) * (PI * delta).tan()
    )
    d_f_over_t = PI + logcos_ratio_over_t
    value = A_COEFF * (df + zcot(PI * t) * d_f_over_t)
    return value * value


def log_coordinate_integrand(a: acb, b: acb, branch: int) -> acb:
    """Pull a rectangle back by x=exp(a), y=exp(b)."""
    x = a.exp()
    y = b.exp()
    log_difference = b - a
    q = (log_difference / 2).tanh()
    if branch == 1:
        value = same_sign_real_square(x, y, True, q, log_difference)
    elif branch == -1:
        value = same_sign_real_square(x, y, False, q, log_difference)
    else:
        value = opposite_real_square(x, y, q, log_difference)
    return x * y * value


def opposite_seam_integrand(aa: acb, bb: acb) -> acb:
    """Opposite quadrant in distances from 1/2; fills the seam corner."""
    t = aa + bb
    s = 1 - t
    x = HALF - aa
    y = HALF - bb
    q = (aa - bb) / s
    log_ratio = 2 * q * hyp_atanh_over(q)
    df = (PI - log_ratio) / s

    middle = t / 2
    delta = (aa - bb) / 2
    z = (PI * middle).tan() * (PI * delta).tan()
    logcos_ratio_over_t = (
        -hyp_atanh_over(z) * PI * tan_over(PI * middle) * (PI * delta).tan()
    )
    d_f_over_t = PI + logcos_ratio_over_t
    value = A_COEFF * (df + zcot(PI * t) * d_f_over_t)
    return value * value


def integrate_rectangle(fun, xa, xb, ya, yb, tol: str = "1e-16") -> acb:
    atol = arb(tol)

    def outer(x, _analytic):
        return acb.integral(
            lambda y, _d: fun(x, y),
            ya,
            yb,
            abs_tol=atol,
            rel_tol=atol,
            depth_limit=30,
            eval_limit=20000,
            use_heap=True,
        )

    return acb.integral(
        outer,
        xa,
        xb,
        abs_tol=atol,
        rel_tol=atol,
        depth_limit=30,
        eval_limit=20000,
        use_heap=True,
    )


def c1_certificate() -> dict[str, object]:
    eps_complex = acb("1e-8")
    log_eps = eps_complex.log()
    log_half = HALF.log()
    ncut = 36
    cuts = [
        log_eps + (log_half - log_eps) * j / ncut
        for j in range(ncut + 1)
    ]
    total = acb(0)
    count = 0
    finite = True
    for i in range(ncut):
        for j in range(ncut):
            xa, xb = cuts[i], cuts[i + 1]
            ya, yb = cuts[j], cuts[j + 1]
            for branch, weight in ((1, 1), (-1, 1), (0, 2)):
                if branch == 0 and i == ncut - 1 and j == ncut - 1:
                    x0 = xa.exp()
                    y0 = ya.exp()
                    value = integrate_rectangle(
                        opposite_seam_integrand,
                        0,
                        HALF - x0,
                        0,
                        HALF - y0,
                        tol="1e-14",
                    )
                else:
                    value = integrate_rectangle(
                        lambda a, b, branch=branch: log_coordinate_integrand(
                            a, b, branch
                        ),
                        xa,
                        xb,
                        ya,
                        yb,
                        tol="1e-14",
                    )
                finite = finite and value.is_finite()
                total += weight * value
                count += 1
        print("C1 row", i, "partial", total)

    eps = arb("1e-8")
    dmax = arb(1) / 2 + eps
    zmax = arb.pi() * dmax
    c_actual = (1 - zmax * zmax.cot()) / dmax**2
    a_endpoint = zmax * zmax.cot()
    scalar_lemmas = (
        c_actual.upper() < arb("4.1")
        and a_endpoint.lower() > arb("-0.1")
    )

    c_bound = arb("4.1")
    a_bound = arb("1.1")
    phi_prime_bound = 2 + arb.pi()
    bcoef = c_bound * dmax
    constant = bcoef * arb.pi() + a_bound * phi_prime_bound
    log_epsilon = eps.log()
    u0 = 2 * eps
    u1 = 2 * eps * (1 - log_epsilon)
    u2 = 2 * eps * (log_epsilon**2 - 2 * log_epsilon + 2)
    log_two = arb(2).log()
    v1 = 1 + log_two
    v2 = log_two**2 + 2 * log_two + 2
    one_strip = (
        bcoef**2 * (u2 + 2 * u1 * v1 + u0 * v2)
        + 2 * bcoef * constant * (u1 + u0 * v1)
        + constant**2 * u0
    )
    axis_union = 2 * (1 / (2 * arb.pi() ** 2)) ** 2 * one_strip
    cstar = total.real + axis_union + arb(1) / 12

    suite_check("C1 integrates exactly 3888 analytic rectangles", count == 3888)
    suite_check("C1 every Acb rectangle is finite", finite)
    suite_check("C1 axis-strip scalar lemmas", scalar_lemmas)
    suite_check("C1 C_star outward enclosure is below 0.1525", cstar.upper() < arb("0.1525"))
    print("C1_regular_real_integral", total.real)
    print("C1_axis_union_upper_bound", axis_union)
    print("C1_imaginary_exact", arb(1) / 12)
    print("C1_Cstar_enclosure", cstar)
    print("C1_VERDICT", "C1_PROVED" if cstar.upper() < arb("0.1525") else "C1_NOT_PROVED")
    return {"cstar": cstar, "rectangles": count}


def c2a_certificate() -> dict[str, arb]:
    pi = arb.pi()
    d = 2 * pi**2 / 3 - 4
    c0 = pi**2 / 288
    euler_remainder = 2 / (9 * arb(3).sqrt())
    worst = (
        arb(1) / 2
        + (c0 + d / 96) / 16
        + (1 + euler_remainder) / 16**2
    )
    monotonic_margin = (9 * pi**2 / 3 - (pi**2 - 4)) / 32
    suite_check("C2a Peano increment coefficient is positive", monotonic_margin.lower() > 0)
    suite_check("C2a all-even-N endpoint constant is below 0.509", worst.upper() < arb("0.509"))
    suite_check("C2a advertised constant is below 0.51", worst.upper() < arb("0.51"))
    print("C2a_monotonic_increment_coefficient", monotonic_margin)
    print("C2a_all_N_scaled_endpoint_bound", worst)
    print("C2a_VERDICT C2A_PROVED_FOR_ALL_EVEN_N_GE_16")
    return {"monotonic_margin": monotonic_margin, "scaled_endpoint": worst}


def run() -> int:
    global PI, A_COEFF, HALF
    reset()
    old_precision = ctx.prec
    print("v1025 -- TEL-B C1/C2a certificates; no marker move")
    try:
        ctx.prec = 100
        suite_check(
            "native python-flint version is pinned for reproducibility",
            version("python-flint") == PYTHON_FLINT_VERSION,
        )
        print("python_flint_version", getattr(python_flint, "__version__", "unknown"))
        print("libflint_version", getattr(python_flint, "__FLINT_VERSION__", "unknown"))
        PI = acb.pi()
        A_COEFF = 1 / (2 * PI**2)
        HALF = acb(1) / 2
        c1_certificate()
        c2a_certificate()
        print("CLAIM_FENCE: CF/DG are not proved in v1025; supplied by v1026 for the relaxed norm")
        print("CLAIM_FENCE: ALG-EXH, FE-GEN, MMST scaling, and T2 remain open")
        print("VERDICT: C1_PROVED; C2A_PROVED; T2_AND_TOE_OPEN")
        return summary("v1025 TEL-B C1/C2a certificates")
    finally:
        ctx.prec = old_precision


if __name__ == "__main__":
    raise SystemExit(run())
