#!/usr/bin/env python3
r"""v1026 -- full round-4 TEL-B norm certificate (norm-only).

This promoted verifier executes the actual round-4 proof computations: the
all-even-N CF/DG and one-sided CROSS scalar certificates, 512 validated Acb
spectral eigensystems for Fourier modes 1..16, the analytic all-alias/high-mode
tails, and the final smooth-remainder/Bound-B assembly.  The original 66 CF/DG
and 88 CROSS floating checks run by default as independent regressions, never
as substitutes for the universal Arb proofs.

Frozen proved inputs are K3_TV_BOUND and POTENTIAL_BOUND from
verification/v1022_telb_round3_certificates.py and C1_BOUND from
verification/v1025_telb_c1_c2a_certificates.py.  The expensive round-3 TV
certificate is deliberately not rerun.  No work/, experiments/, generated,
or cwd file is imported.

Contract fence: this proves only the TEL-B norm estimate < 3 for every even
N>=16.  ALG-EXH, FE-GEN, T2, TOE, MMST identification, and RH remain open.
Native python-flint 0.9.0 is required.  NO RH CLAIM.
"""
from __future__ import annotations

from importlib.metadata import version

import flint as python_flint
from flint import acb, acb_mat, arb, ctx

from tfpt_constants import check as suite_check, reset, summary
from v1022_telb_round3_certificates import DIM, NY, derivative_enclosures, hs_upper

PYTHON_FLINT_VERSION = "0.9.0"
GRID = 512
LOW_MAX = 16
K3_TV_BOUND = "2.517464500835"          # proved by v1022
POTENTIAL_BOUND = "0.399224424139108"  # proved by v1022
C1_BOUND = "0.1525"                    # proved by v1025
RATIONAL_CAPS = (
    "0.872617451262", "0.119561574970", "0.036384250090",
    "0.013594203794", "0.005638853577", "0.002552800879",
    "0.001281003972", "0.000727535964", "0.000465728162",
    "0.000325832279", "0.000241157627", "0.000184924134",
    "0.000145312983", "0.000116348415", "0.000094610814",
    "0.000077965240",
)


def cf_dg_certificate() -> dict[str, arb]:
    """The nine final scalar checks of the all-even-N CF/DG proof."""
    pi = arb.pi()
    aa = 1 / (2 * pi**2)
    h = arb(1) / 16
    ell = pi + 2
    mphi = pi**2 - 4
    dconst = 2 * pi**2 / 3 - 4
    zeta2 = pi**2 / 6

    def cp(x: arb) -> arb:
        return pi**2 / (pi * x).sin()**2 - 1 / x**2

    def cpp(x: arb) -> arb:
        return -2 * pi**3 * (pi * x).cos() / (pi * x).sin()**3 + 2 / x**3

    # Central covariance/bias strip |j|<=N/2.
    vcell = (2 + zeta2 / 6).sqrt() + ell * (h / 12).sqrt()
    fdiff = (2 * zeta2).sqrt()
    central_fluct = aa * cp(arb(9) / 16) * h * vcell / arb(3).sqrt()
    central_bias = aa * cpp(arb(9) / 16) * h**arb("1.5") * fdiff / 12
    central = central_fluct + central_bias

    # Middle seam; n-1/n counts cancel the would-be singular cells.
    h7 = sum((arb(1) / j for j in range(1, 8)), arb(0))
    vmiddle = (h7 / 3).sqrt() + ell / arb(24).sqrt()
    middle_fluct = aa * cp(arb(13) / 16) * h**arb("1.5") * vmiddle / arb(6).sqrt()
    middle_bias = aa * cpp(arb(13) / 16) * h**arb("1.5") * fdiff / 12
    middle = middle_fluct + middle_bias

    # Far seam after c(d)=1/(1-d)+a(d).
    h4 = sum((arb(1) / j for j in range(1, 5)), arb(0))
    far_reciprocal = aa * (2 * pi**2) * h**arb("1.5") * (h4 / 72).sqrt()
    a1 = 1 / (arb(11) / 16)**2 + cp(arb(5) / 16)
    a2 = 2 / (arb(11) / 16)**3 + cpp(arb(5) / 16)
    far_fluct = aa * a1 * (2 * pi) * h**arb("1.5") / 6
    far_bias = aa * a2 * (2 * pi) * (arb(5) / 16) * h**arb("1.5") / 12
    far = far_reciprocal + far_fluct + far_bias

    phi_quotient = aa * mphi * h * (zeta2 / 72).sqrt()
    cf = (central**2 + middle**2 + far**2).sqrt() + phi_quotient
    diagonal_centering = aa * h * (2 + arb("1.5") * dconst)
    diagonal_secant = aa * mphi * h
    c_slope = (pi**2 / 3) / (1 - h**2)
    diagonal_log = aa * c_slope * (h / 2 + ell * h**2 / 6)
    dg = diagonal_centering + diagonal_secant + diagonal_log
    combined = ((arb(POTENTIAL_BOUND) + cf)**2 + dg**2).sqrt()

    for label, value in (
        ("CF central", central), ("CF middle seam", middle),
        ("CF far seam", far), ("CF Phi quotient", phi_quotient),
        ("DG centering", diagonal_centering), ("DG secant", diagonal_secant),
        ("DG logarithmic", diagonal_log),
    ):
        print(label, value)
    for label, passed in (
        ("CF all even N>=16 below 0.070", cf < arb("0.070")),
        ("DG all even N>=16 below 0.044", dg < arb("0.044")),
        ("CF report rounded bound 0.065697", cf < arb("0.065697")),
        ("DG report rounded bound 0.042959", dg < arb("0.042959")),
        ("CF requested budget 0.139", cf < arb("0.139")),
        ("DG requested budget 0.060", dg < arb("0.060")),
        ("C2b combined below 0.472", combined < arb("0.472")),
        ("C2b report rounded bound 0.466902", combined < arb("0.466902")),
        ("C2b requested budget 0.542702", combined < arb("0.542702")),
    ):
        suite_check(label, passed)
    print("CF", cf, "DG", dg, "C2b_combined", combined)
    print("CF_DG_ALL_EVEN_N_PROVED")
    return {"cf": cf, "dg": dg, "c2b": combined}


def cross_certificate(c2b: arb) -> dict[str, arb]:
    """The eight final scalar checks of the one-sided CROSS proof."""
    pi = arb.pi()
    aa = 1 / (2 * pi**2)
    h = arb(1) / 16
    dconst = 2 * pi**2 / 3 - 4
    mu = arb(64) / 675
    ntail = 4 * aa / (1 - (arb(3) / 32)**2)
    nr00 = aa * pi + aa * h * (2 + arb("1.5") * dconst)
    cross = nr00 - arb("0.5") + 2 * mu + 2 * (1 + h / 4) * ntail
    # C1 is the v1025 input; c2b has just been recomputed above.
    res2 = (arb(C1_BOUND).sqrt() + c2b / 4)**2
    ca = arb(5) / 4 - 8 / pi**2
    bound_b_squared = ca + res2 + cross / 16
    conditional = arb("1.7833") + (2 * bound_b_squared).sqrt()
    for label, passed in (
        ("one-sided CROSS all-N below 0.283", cross < arb("0.283")),
        ("one-sided CROSS report bound 0.282637", cross < arb("0.282637")),
        ("one-sided CROSS below prior allowance 0.382", cross < arb("0.382")),
        ("uniform residual squared below 0.258", res2 < arb("0.258")),
        ("uniform Bound-B squared below 0.716", bound_b_squared < arb("0.716")),
        ("Bound-B report rounded bound 0.714386", bound_b_squared < arb("0.714386")),
        ("conditional TEL-B below 2.98", conditional < arb("2.98")),
        ("conditional TEL-B report bound 2.978613", conditional < arb("2.978613")),
    ):
        suite_check(label, passed)
    print("signed_momentum_upper", mu)
    print("N_tail_upper", ntail)
    print("N_R00_upper", nr00)
    print("N_one_sided_cross_upper", cross)
    print("residual_squared_upper", res2)
    print("bound_B_squared_upper", bound_b_squared)
    print("ONE_SIDED_CROSS_ALL_EVEN_N_PROVED; ABSOLUTE_CROSS_NOT_CLAIMED")
    return {"cross": cross, "res2": res2, "bound_b_squared": bound_b_squared}


def low_fourier_certificate() -> dict[str, arb]:
    """Compute 512 validated Acb eigensystems and modes 1..16 plus all aliases."""
    saved_precision = ctx.prec
    try:
        ctx.prec = 256
        k3 = arb(K3_TV_BOUND)
        delta = acb_mat(DIM, DIM)
        delta[NY, NY] = 1
        delta[NY - 1, NY - 1] = -1
        dft = [acb_mat(DIM, DIM) for _ in range(LOW_MAX)]
        finite = True
        idempotent = True
        for j in range(GRID):
            p = arb.pi() * arb(2 * j + 1) / GRID
            # v1022 uses a validated Rump left/right eigensystem, excludes zero
            # from all eigenvalue intervals, and verifies exactly NY negatives.
            projector = derivative_enclosures(p, max_order=0)[0]
            finite = finite and all(z.is_finite() for z in projector.entries())
            idempotent = idempotent and all(
                z.contains(0) for z in (projector * projector - projector).entries()
            )
            saw = arb(1) / 2 - arb(2 * j + 1) / (2 * GRID)
            smooth = projector - saw * delta
            phase = acb(0, -p).exp()
            phase_m = acb(1)
            for m in range(1, LOW_MAX + 1):
                phase_m *= phase
                dft[m - 1] += phase_m * smooth
            if (j + 1) % 64 == 0:
                print(f"validated Acb eigensystem {j + 1}/{GRID}", flush=True)

        suite_check("Fourier grid has exactly 512 eigensystems", GRID == 512)
        suite_check("all Fourier projectors are finite", finite)
        suite_check("all Fourier projectors enclose P^2-P=0", idempotent)
        weighted = arb(0)
        print("m | DFT_HS_upper | all_alias_HS_upper | C_infinity_HS_upper")
        for m in range(1, LOW_MAX + 1):
            norm = hs_upper(dft[m - 1] / GRID)
            # Complete midpoint-DFT alias sum via the v1022 |mode|^-3 theorem.
            alias = k3 * arb(3).zeta() * (
                arb(GRID - m)**-3 + arb(GRID)**-3
            )
            upper = norm + alias
            suite_check(
                f"Fourier mode {m} plus all aliases below rational cap",
                upper.upper() < arb(RATIONAL_CAPS[m - 1]),
            )
            weighted += m * upper**2
            print(m, norm.upper(), alias.upper(), upper.upper(), sep=" | ")

        high_tail = k3**2 / (4 * arb(LOW_MAX)**4)
        actual_core = 2 * (weighted + high_tail).sqrt()
        cap_weighted = sum(
            (m * arb(x)**2 for m, x in enumerate(RATIONAL_CAPS, 1)), arb(0)
        )
        cap_core = 2 * (cap_weighted + high_tail).sqrt()
        suite_check("rational-cap core below 1.783260551", cap_core.upper() < arb("1.783260551"))
        suite_check("actual validated Fourier core below 1.7833", actual_core.upper() < arb("1.7833"))
        print("K3_v1022_input", k3)
        print("weighted_low_mode_sum_upper", weighted.upper())
        print("analytic_high_mode_tail_upper", high_tail.upper())
        print("actual_validated_Fourier_core_upper", actual_core.upper())
        print("rational_cap_core_upper", cap_core.upper())
        print("LOW_FOURIER_OUTWARD_CERTIFICATE_PASS")
        return {"actual_core": actual_core, "cap_core": cap_core, "high_tail": high_tail}
    finally:
        ctx.prec = saved_precision


def r_upper(t: arb, cutoff: int = 100) -> arb:
    """Complete affine alias envelope, including a rigorous infinite tail."""
    total = arb(0)
    for q in range(-cutoff, cutoff + 1):
        if q % 4 == 0 or q == 1:
            continue
        coefficient = arb(2) if q % 4 == 2 else arb(2).sqrt()
        total += coefficient / abs(arb(q - 1) + t)**3
    return total + arb(4) / cutoff**3 + arb(2) / cutoff**2


def rsm_assembly_certificate(fourier_core: arb, bound_b_squared: arb) -> dict[str, arb]:
    """Complete all-even-N alias and final TEL-B assembly."""
    a, b, c = r_upper(arb(0)), r_upper(arb(1) / 2), r_upper(arb(1))
    integral = a*a/24 + a*b/12 + b*b/3 + b*c/4 + 7*c*c/24
    derivative_difference = 4*b*b - 2*a*b - a*a + 5*c*c - 6*b*c
    trapezoid = integral + abs(derivative_difference) / (6 * 16**2)
    alias_norm = arb(K3_TV_BOUND) / 16**2 * trapezoid.sqrt()
    rsm_norm = fourier_core + alias_norm
    full_norm = rsm_norm + (2 * bound_b_squared).sqrt()
    for label, passed in (
        ("all-N alias remainder below 0.018", alias_norm < arb("0.018")),
        ("reported alias remainder bound 0.017333", alias_norm < arb("0.017333")),
        ("all-N smooth remainder below 1.802", rsm_norm < arb("1.802")),
        ("reported smooth remainder bound 1.800594", rsm_norm < arb("1.800594")),
        ("computed TEL-B norm below 2.995906", full_norm < arb("2.995906")),
        ("computed TEL-B norm below 3", full_norm < arb(3)),
    ):
        suite_check(label, passed)
    print("R(0), R(1/2), R(1)", a, b, c)
    print("weighted_affine_envelope_integral", integral)
    print("trapezoid_derivative_difference", derivative_difference)
    print("all_N_alias_remainder_norm", alias_norm)
    print("all_N_smooth_remainder_norm", rsm_norm)
    print("computed_TELB_norm", full_norm)
    print("RSM_ALL_EVEN_N_ASSEMBLY_PROVED_GIVEN_VALIDATED_FOURIER_CORE")
    return {"alias_norm": alias_norm, "rsm_norm": rsm_norm, "full_norm": full_norm}


def cf_dg_regressions() -> dict[str, object]:
    """Original 66 finite CF/DG regressions; independent of the all-N proof."""
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    from scipy.special import digamma, polygamma

    pi = np.pi
    aa = 1 / (2 * pi * pi)
    count = 0

    def close(actual, expected, tolerance, name):
        nonlocal count
        error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
        suite_check(f"CF/DG regression: {name}", error < tolerance)
        count += 1

    def less(actual, bound, name):
        nonlocal count
        suite_check(f"CF/DG regression: {name}", actual < bound)
        count += 1

    def phi(x):
        return -np.log(2 * pi) - np.log(np.sinc(x)) - pi * x

    def cfun(x):
        x = np.asarray(x)
        small = abs(x) < 1e-4
        safe = np.where(small, 0.1, x)
        direct = 1 / safe - pi / np.tan(pi * safe)
        series = pi*pi*x/3 + pi**4*x**3/45 + 2*pi**6*x**5/945
        return np.where(small, series, direct)

    def phipp(x):
        x = np.asarray(x)
        small = abs(x) < 1e-4
        safe = np.where(small, 0.1, x)
        direct = pi*pi / np.sin(pi * safe)**2 - 1 / safe**2
        series = pi*pi/3 + pi**4*x*x/15 + 2*pi**6*x**4/189
        return np.where(small, series, direct)

    def ffun(x):
        return -np.log(abs(x)) - pi * (x < 0)

    def fperiodic(x):
        return -np.log(2 * abs(np.sin(pi*x))) - pi*x - pi*(x < 0)

    def primitive_log(x):
        return 0.0 if x == 0 else x*np.log(abs(x)) - x

    def exact_f_means(n):
        return np.array([
            -n * (primitive_log((k+1)/n) - primitive_log(k/n)) - pi*(k < 0)
            for k in range(-n//2, n//2)
        ])

    def direct_remainder(n):
        k = np.arange(-n//2, n//2)
        overlap = (1 - np.exp(-2j*pi*.25))/n / (
            1 - np.exp(2j*pi*(k[:, None] - k[None, :] - .25)/n)
        )
        weights = np.mod((k + .25)/n, 1)
        finite = (overlap * weights[None, :]) @ overlap.conj().T
        d = k[None, :] - k[:, None]
        safe = np.where(d == 0, 1, d)
        psi = digamma(k + .75)
        infinite = (psi[None, :] - psi[:, None]) / safe
        np.fill_diagonal(infinite, polygamma(1, k + .75))
        return finite - np.diag(k/n) - aa*infinite

    def trace_formula(n):
        j = n/2

        def primitive(x):
            return (x-1)*polygamma(1, x) + digamma(x)

        tau = primitive(j+1.25) - primitive(j+.75)
        return aa*pi + aa*tau, tau

    def cell_rules(n, order, levels):
        gx, gw = leggauss(order)
        nodes, records, weights = [], [], []
        for row, k in enumerate(range(-n//2, n//2)):
            left, right = k/n, (k+1)/n
            if k in (-1, 0):
                intervals = []
                lo, hi = left, right
                for _ in range(levels):
                    mid = (lo+hi)/2
                    if k == 0:
                        intervals.append((mid, hi))
                        hi = mid
                    else:
                        intervals.append((lo, mid))
                        lo = mid
                intervals.append((lo, hi))
            else:
                intervals = [(left, right)]
            for lo, hi in intervals:
                for x, weight in zip(gx, gw):
                    nodes.append((lo+hi)/2 + (hi-lo)*x/2)
                    weights.append((hi-lo)*weight/2)
                    records.append(row)
        nodes = np.array(nodes)
        matrix = np.zeros((n, len(nodes)))
        matrix[np.array(records), np.arange(len(nodes))] = weights
        return nodes, matrix

    def cell_kernel(n, levels):
        u, wu = cell_rules(n, 8, levels)
        v, wv = cell_rules(n, 9, levels)
        d = v[None, :] - u[:, None]
        pu, pv = phi(u), phi(v)
        fdiff = fperiodic(v)[None, :] - fperiodic(u)[:, None]
        qphi = (pv[None, :] - pu[:, None]) / d
        qphi = np.where(
            abs(d) < 1e-8, cfun((u[:, None] + v[None, :])/2) - pi, qphi
        )
        kernel = aa * (cfun(d)*fdiff - qphi - 1j*pi*fdiff)
        cell = n * wu @ kernel @ wv.T

        x, w = leggauss(16)
        k = np.arange(-n//2, n//2)
        pbar = phi((k[:, None] + .5 + .5*x[None, :])/n) @ w / 2
        fb = exact_f_means(n) + pbar
        d0 = (k[None, :] - k[:, None])/n
        safe = np.where(d0 == 0, 1, d0)
        frozen = aa/n * (
            cfun(np.where(d0 == 0, .1, d0))*(fb[None, :] - fb[:, None])
            - (pbar[None, :] - pbar[:, None])/safe
            - 1j*pi*(fb[None, :] - fb[:, None])
        )
        return cell, frozen

    rows = []
    for n in (16, 18, 20, 32, 64, 128):
        k = np.arange(-n//2, n//2)
        remainder = direct_remainder(n)
        close(remainder, remainder.conj().T, 2e-13, f"R Hermitian N={n}")
        close(
            np.diff(np.diag(remainder)),
            -aa/n**2 * phipp((k[:-1]+.75)/n),
            2e-12,
            f"exact diagonal recurrence N={n}",
        )
        trace, tau = trace_formula(n)
        close(np.trace(remainder), trace, 2e-12, f"exact trace N={n}")
        less(-tau, 1e-14, f"tau positive N={n}")
        less(tau, 4/n, f"tau upper N={n}")
        q = n*np.diag(remainder) + aa*(cfun(k/n) - pi)
        close(np.mean(q), aa*(tau-2/n), 2e-12, f"exact q mean N={n}")
        less(
            np.max(abs(q)), aa/n*(2 + 1.5*(2*pi*pi/3-4)), f"q bound N={n}"
        )
        if n <= 32:
            kernel, frozen = cell_kernel(n, 14)
            coarse, _ = cell_kernel(n, 10)
            close(kernel, coarse, 5e-6, f"graded quadrature refinement N={n}")
            off = ~np.eye(n, dtype=bool)
            cf = np.sqrt(n)*np.linalg.norm((frozen-kernel)[off])
            dg = np.sqrt(n)*np.linalg.norm(np.diag(remainder-kernel))
            total = np.sqrt(n)*np.linalg.norm(remainder-kernel)
            less(cf, .065697, f"CF finite diagnostic N={n}")
            less(dg, .042959, f"DG finite diagnostic N={n}")
            less(total, .466902, f"C2b finite diagnostic N={n}")
            close(
                np.imag(frozen[off]-kernel[off]), 0, 5e-7,
                f"exact imaginary freezing N={n}",
            )
            rows.append({"N": n, "CF": float(cf), "DG": float(dg), "C2b": float(total)})

    for u, v in (
        (-1e-8, 2e-8), (-.5+1e-8, .5-2e-8), (.02, .021), (-.4, -.399)
    ):
        d = v-u
        lam = pi*d/np.tan(pi*d) + 1j*pi*d
        raw = aa*((1-lam)*(ffun(v)-ffun(u)) - lam*(phi(v)-phi(u)))/d
        rewritten = aa*(
            cfun(d)*(fperiodic(v)-fperiodic(u))
            - (phi(v)-phi(u))/d - 1j*pi*(fperiodic(v)-fperiodic(u))
        )
        close(raw, rewritten, 5e-8, f"kernel rewrite at {u},{v}")

    # Structural count is reported without inflating the original 66.
    if count != 66:
        raise AssertionError(f"CF/DG regression count {count} != 66")
    print("CF_DG_REGRESSION_CHECKS", count)
    print("CF_DG_REGRESSIONS_PASS; FLOAT_REGRESSIONS_ARE_NOT_THE_ALL_N_PROOF")
    return {"checks": count, "diagnostic_rows": rows}


def cross_regressions() -> dict[str, object]:
    """Original 88 finite CROSS regressions; independent of the all-N proof."""
    import numpy as np
    from scipy.special import digamma, polygamma

    pi = np.pi
    aa = 1 / (2*pi*pi)
    count = 0

    def close(x, y, tolerance, label):
        nonlocal count
        residual = float(np.max(abs(np.asarray(x)-np.asarray(y))))
        suite_check(f"CROSS regression: {label}", residual < tolerance)
        count += 1

    def leq(x, y, label):
        nonlocal count
        suite_check(f"CROSS regression: {label}", x <= y + 2e-12)
        count += 1

    rows = []
    for n in (16, 18, 20, 32, 64, 128, 256, 512):
        j = n//2
        k = np.arange(-j, j, dtype=float)
        overlap = (1-np.exp(-2j*pi*.25))/n / (
            1-np.exp(2j*pi*(k[:, None]-k[None, :]-.25)/n)
        )
        rho = np.mod((k+.25)/n, 1.)
        finite = (overlap*rho[None, :]) @ overlap.conj().T
        denominator = k[None, :]-k[:, None]
        safe = np.where(denominator == 0, 1., denominator)
        psi = digamma(k+.75)
        negative = aa*(psi[None, :]-psi[:, None])/safe
        np.fill_diagonal(negative, aa*polygamma(1, k+.75))
        remainder = -np.diag(k/n) + finite - negative
        w = np.exp(-1j*pi*.25)*np.sin(pi*.25)/(pi*(k-.25))
        tail = aa*(polygamma(1, j-.25)+polygamma(1, j+1.25))
        mu = float(np.sum(k*abs(w)**2))
        mu_pair = aa*(
            sum(q*q/(q*q-1/16)**2 for q in range(1, j))
            - j/(j+.25)**2
        )
        projection_form = float(np.vdot(w, negative@w).real)
        finite_form = float(np.vdot(w, finite@w).real)
        actual_form = float(np.vdot(w, remainder@w).real)
        lower = -mu/n + (1-tail)/(4*n) - tail
        cross = float(remainder[j, j].real - 2*actual_form)
        e = np.zeros(n, dtype=complex)
        e[j] = 1
        rank_two = .5*np.outer(e, e.conj()) - np.outer(w, w.conj())

        close(np.vdot(w, w).real, 1-tail, 5e-13, f"tail normalization N={n}")
        close(mu, mu_pair, 5e-13, f"paired signed moment N={n}")
        leq(mu, 64/675, f"signed moment upper N={n}")
        leq(n*tail, 4*aa/(1-(3/32)**2), f"tail bound N={n}")
        leq(0, projection_form, f"negative projection positivity N={n}")
        leq(projection_form, tail, f"projection leakage bound N={n}")
        leq((1-tail)/(4*n), finite_form, f"minimum-weight bound N={n}")
        leq(lower, actual_form, f"quadratic form lower bound N={n}")
        close(
            cross, 2*np.vdot(rank_two, remainder).real, 2e-12,
            f"rank-two cross identity N={n}",
        )
        leq(n*cross, .282637, f"one-sided CROSS envelope N={n}")
        # Deliberate witness that the absolute-value strengthening is false.
        leq(.283, n*abs(cross), f"absolute-vs-one-sided witness N={n}")
        rows.append({
            "N": n, "N_cross": n*cross, "N_tail": n*tail, "mu": mu,
            "projection_over_tail": projection_form/tail,
        })

    if count != 88:
        raise AssertionError(f"CROSS regression count {count} != 88")
    print("CROSS_REGRESSION_CHECKS", count)
    print("ONE_SIDED_CROSS_REGRESSIONS_PASS")
    print("ABSOLUTE_0_283_CROSS_BOUND_REFUTED_BY_FINITE_WITNESS")
    print("FINITE_CHECKS_ARE_NOT_THE_ALL_N_PROOF")
    return {"checks": count, "diagnostic_rows": rows}


def run(include_regressions: bool = True) -> int:
    """Run the full certificate and return tfpt_constants' failure count."""
    reset()
    old_precision = ctx.prec
    print("v1026 -- full round-4 TEL-B norm certificate; no marker move")
    try:
        ctx.prec = 192
        suite_check(
            "native python-flint version is pinned for reproducibility",
            version("python-flint") == PYTHON_FLINT_VERSION,
        )
        print("python_flint_version", getattr(python_flint, "__version__", "unknown"))
        print("libflint_version", getattr(python_flint, "__FLINT_VERSION__", "unknown"))
        print("FROZEN_INPUT v1022 K3_TV_BOUND", K3_TV_BOUND)
        print("FROZEN_INPUT v1022 POTENTIAL_BOUND", POTENTIAL_BOUND)
        print("FROZEN_INPUT v1025 C1_BOUND", C1_BOUND)

        cf_dg = cf_dg_certificate()
        cross = cross_certificate(cf_dg["c2b"])
        fourier = low_fourier_certificate()
        assembly = rsm_assembly_certificate(
            fourier["actual_core"], cross["bound_b_squared"]
        )
        if include_regressions:
            cf_dg_regressions()
            cross_regressions()
        else:
            print("FINITE_REGRESSIONS_SKIPPED_BY_EXPLICIT_CALLER_REQUEST")

        print("FINAL_COMPUTED_TELB_NORM", assembly["full_norm"])
        print("CLAIM_FENCE: norm only; ALG-EXH, FE-GEN, T2, TOE remain open")
        print("CLAIM_FENCE: no MMST identification and NO RH CLAIM")
        print("VERDICT: TELB_NORM_LT_3_FOR_ALL_EVEN_N_GE_16; T2_AND_TOE_OPEN")
        return summary("v1026 TEL-B round-4 norm certificate")
    finally:
        ctx.prec = old_precision


if __name__ == "__main__":
    raise SystemExit(run())
