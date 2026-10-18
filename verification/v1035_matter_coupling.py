#!/usr/bin/env python3
"""Conditional certificate for first-order matter coupling of the tensor target.

The checker separates three claims:

1. In the inherited Fourier dictionary, a prescribed c-number source
   satisfying the two Ward equations couples exactly to the free constrained
   tensor algebra at every nonzero momentum.  The checker retains all factors
   of i, tests Fourier reality, and instantiates the declared three-axis mask
   gluing, but does not import a repository implementation.
2. Dynamical matter gives the same result only through first order in the
   coupling.  Its source terms must be added to the constraints; coupling only
   q_ij T_ij is an explicit constraint-propagation mutant.
3. A free scalar and a chiral fermion with nearest-neighbour one-particle
   Hamiltonian admit exact one-dimensional Ward complexes (embedded collinear
   tests only).  The fermion density/current/stress vertices have maximal
   hopping ranges one/two/three.  The naive scalar stress fails, and an onsite
   phi^4 interaction has a nonzero global momentum defect on a finite lattice.
   A projected inverse-divergence repair exists for nonzero gravitational
   modes, but it is nonlocal and is not nonlinear constraint closure.

All theorem-bearing checks are exact SymPy identities.  Floating-point checks
are labelled separately and are regressions only.

Port provenance: native verification port of
`toe_round7_matter_coupling/matter_coupling_checker.py`
(source SHA-256 c9bf48c55812b91379ed6e118de34ac915eae7ab6efed91e347b85d3aeab72e7).
The port changes only harness integration and execution lifecycle.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


@dataclass
class Counts:
    exact_pass: int = 0
    exact_total: int = 0
    float_pass: int = 0
    float_total: int = 0


COUNTS = Counts()


def is_zero(value: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def exact(name: str, condition: bool) -> None:
    COUNTS.exact_total += 1
    passed = suite_check(f"[exact] {name}", bool(condition))
    COUNTS.exact_pass += int(passed)


def floating(name: str, error: float, tolerance: float = 2.0e-11) -> None:
    COUNTS.float_total += 1
    passed = suite_check(
        f"[float] {name}: error={error:.3e}, tolerance={tolerance:.1e}",
        math.isfinite(error) and error < tolerance,
    )
    COUNTS.float_pass += int(passed)


def tensor_data(k: sp.Matrix) -> tuple[sp.Matrix, ...]:
    basis = []
    for index in range(3):
        element = sp.zeros(3)
        element[index, index] = 1
        basis.append(element)
    for left, right in ((1, 2), (0, 2), (0, 1)):
        element = sp.zeros(3)
        element[left, right] = element[right, left] = 1 / sp.sqrt(2)
        basis.append(element)
    b = sp.Matrix.hstack(*(element * k for element in basis))
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    r2 = (k.T * k)[0]
    v = b.T * k
    scalar = v - r2 * trace
    kp = sp.eye(6) - trace * trace.T / 2
    kq = (
        r2 * (sp.eye(6) - trace * trace.T)
        - 2 * b.T * b
        + trace * v.T
        + v * trace.T
    )
    return b, trace, scalar, kp, kq, r2


def external_source_certificate() -> None:
    print("\nEXTERNAL CONSERVED SOURCE: FULL COMPLEX FOURIER SIGNS")
    x, y, z = sp.symbols("x y z", real=True)
    coupling = sp.symbols("g", real=True, nonzero=True)
    rho = sp.symbols("rho")
    k = sp.Matrix([x, y, z])
    b, trace, scalar, kp, kq, r2 = tensor_data(k)
    c = kq * kp * kq
    tau = sp.Matrix(sp.symbols("tau0:6"))
    current = sp.Matrix(sp.symbols("j0:3"))
    q = sp.Matrix(sp.symbols("q0:6"))
    p = sp.Matrix(sp.symbols("p0:6"))

    exact("Kq annihilates momentum gauge directions", is_zero(kq * b.T))
    exact("Kp maps scalar direction to longitudinal momentum", is_zero(kp * scalar - b.T * k))
    exact("trace of E is minus the vacuum scalar constraint",
          is_zero(trace.T * kq - scalar.T))
    exact("curvature polynomial identity", is_zero(c - r2 * kq - scalar * scalar.T / 2))

    # Physical-position Fourier convention D -> i*k:
    # H = H0 + g q.tau, Psi0=-s.q+g rho, Psi=i*Bp-g*j.
    dot_q = kp * p
    dot_p = -kq * q - coupling * tau
    dot_rho = -sp.I * (k.T * current)[0]
    dot_current = -sp.I * b * tau
    psi0 = -(scalar.T * q)[0] + coupling * rho
    psi = sp.I * b * p - coupling * current
    dot_psi0 = -(scalar.T * dot_q)[0] + coupling * dot_rho
    dot_psi = sp.I * b * dot_p - coupling * dot_current
    exact("full-complex scalar constraint obeys dot(Psi0)=i*k.Psi",
          is_zero(dot_psi0 - sp.I * (k.T * psi)[0]))
    exact("full-complex vector constraint is preserved", is_zero(dot_psi))

    # If the old real-fibre scalar sign is retained while i is restored in the
    # vector divergence, even vacuum scalar propagation has the wrong sign.
    old_psi0 = (scalar.T * q)[0] + coupling * rho
    old_dot_psi0 = (scalar.T * dot_q)[0] + coupling * dot_rho
    exact("must-fail: old stripped-i scalar sign is inconsistent after restoring i",
          not is_zero(old_dot_psi0 - sp.I * (k.T * psi)[0]))

    # Explicit e^{-it+iz} plane wave: rho=j_z=tau_zz=g=1.  Both source Ward
    # equations and the repaired constraints hold at the displayed instant.
    kw = sp.Matrix([0, 0, 1])
    bw, _, sw, kpw, kqw, _ = tensor_data(kw)
    qw = sp.Matrix([-1, 0, 0, 0, 0, 0])
    pw = sp.Matrix([0, 0, -sp.I, 0, 0, 0])
    jw = sp.Matrix([0, 0, 1])
    tauw = sp.Matrix([0, 0, 1, 0, 0, 0])
    dot_rhow = -sp.I
    dot_jw = -sp.I * bw * tauw
    psi0w = -(sw.T * qw)[0] + 1
    psiw = sp.I * bw * pw - jw
    dot_psi0w = -(sw.T * (kpw * pw))[0] + dot_rhow
    dot_psiw = sp.I * bw * (-kqw * qw - tauw) - dot_jw
    exact("explicit conserved complex plane wave satisfies both Ward equations and repaired propagation",
          is_zero(dot_rhow + sp.I * (kw.T * jw)[0])
          and is_zero(dot_jw + sp.I * bw * tauw)
          and is_zero(psi0w) and is_zero(psiw)
          and is_zero(dot_psi0w - sp.I * (kw.T * psiw)[0])
          and is_zero(dot_psiw))

    vacuum_vector_mutant = sp.I * b * dot_p
    exact("q:T coupling with vacuum constraints has a nonzero vector residual",
          not is_zero(vacuum_vector_mutant))
    exact("mutant residual is exactly -i*g*B*tau",
          is_zero(vacuum_vector_mutant + sp.I * coupling * b * tau))

    alpha, beta, gamma = sp.symbols("alpha beta gamma")
    # H_int=gamma*g*q.tau, Psi0=-s.q+alpha*g*rho,
    # Psi=i*B*p+beta*g*j.
    coefficient_solution = sp.solve(
        [gamma + beta, alpha + beta], [alpha, beta], dict=True
    )
    exact("linear Ward cancellation uniquely fixes source-constraint coefficients",
          coefficient_solution == [{alpha: gamma, beta: -gamma}])

    # E=Kq q and F=Kq Kp p remain strongly gauge invariant at this order.
    exact("E commutes with the momentum constraint", is_zero(kq * b.T))
    exact("F commutes with the scalar constraint", is_zero(kq * kp * scalar))

    # On Psi0=0, E obeys E''+r^2 E=-g J with this local source J.
    drive = kq * kp * tau + scalar * rho / 2
    rho_ddot = -(k.T * b * tau)[0]
    exact("response drive is transverse", is_zero(b * drive))
    exact("response trace is minus rho_ddot+r^2 rho",
          is_zero((trace.T * drive)[0] + rho_ddot + r2 * rho))

    # Fourier reality: B is odd, while s, Kp, and Kq are even.  Therefore the
    # repaired complex constraints at -k are conjugates of those at +k.
    bm, _, sm, kpm, kqm, r2m = tensor_data(-k)
    exact("Fourier derivative parity is compatible with the real-space fields",
          is_zero(bm + b) and is_zero(sm - scalar)
          and is_zero(kpm - kp) and is_zero(kqm - kq) and is_zero(r2m - r2))
    qr = sp.Matrix(sp.symbols("qr0:6", real=True))
    qi = sp.Matrix(sp.symbols("qi0:6", real=True))
    pr = sp.Matrix(sp.symbols("pr0:6", real=True))
    pi_im = sp.Matrix(sp.symbols("pi0:6", real=True))
    tr = sp.Matrix(sp.symbols("tr0:6", real=True))
    ti = sp.Matrix(sp.symbols("ti0:6", real=True))
    jr = sp.Matrix(sp.symbols("jr0:3", real=True))
    ji = sp.Matrix(sp.symbols("ji0:3", real=True))
    rhor, rhoi = sp.symbols("rhor rhoi", real=True)
    q_plus, q_minus = qr + sp.I * qi, qr - sp.I * qi
    p_plus, p_minus = pr + sp.I * pi_im, pr - sp.I * pi_im
    tau_plus, tau_minus = tr + sp.I * ti, tr - sp.I * ti
    j_plus, j_minus = jr + sp.I * ji, jr - sp.I * ji
    rho_plus, rho_minus = rhor + sp.I * rhoi, rhor - sp.I * rhoi
    psi0_plus = -(scalar.T * q_plus)[0] + coupling * rho_plus
    psi0_minus = -(sm.T * q_minus)[0] + coupling * rho_minus
    psi_plus = sp.I * b * p_plus - coupling * j_plus
    psi_minus = sp.I * bm * p_minus - coupling * j_minus
    exact("repaired complex constraints obey k-to-minus-k Fourier reality",
          is_zero(psi0_minus - sp.conjugate(psi0_plus))
          and is_zero(psi_minus - sp.conjugate(psi_plus)))
    quadratic_pair = ((p_minus.T * kp * p_plus)[0]
                      + (q_minus.T * kq * q_plus)[0])
    source_pair = ((q_minus.T * tau_plus)[0] + (q_plus.T * tau_minus)[0]) / 2
    exact("paired complex Fourier quadratic and source Hamiltonians are real",
          is_zero(quadratic_pair - sp.conjugate(quadratic_pair))
          and is_zero(source_pair - sp.conjugate(source_pair)))

    # Declared staggered-mask gluing under k_i -> k_i + 2*pi/a.  In kappa
    # coordinates this reflects kappa_i.  Tensor masks are 0 for diagonals and
    # e_j xor e_l for off-diagonals; vector masks are e_i.
    tensor_pairs = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
    for axis in range(3):
        tensor_gluing = sp.diag(*[
            -1 if left != right and axis in (left, right) else 1
            for left, right in tensor_pairs
        ])
        vector_gluing = sp.diag(*[-1 if component == axis else 1
                                  for component in range(3)])
        shifted_k = vector_gluing * k
        bs, _, ss, kps, kqs, _ = tensor_data(shifted_k)
        exact(f"axis {axis}: B, s, Kp, Kq obey declared staggered Bloch gluing",
              is_zero(bs * tensor_gluing - vector_gluing * b)
              and is_zero(ss - tensor_gluing * scalar)
              and is_zero(kps - tensor_gluing * kp * tensor_gluing)
              and is_zero(kqs - tensor_gluing * kq * tensor_gluing))
        shifted_drive = kqs * kps * (tensor_gluing * tau) + ss * rho / 2
        shifted_psi0 = -(ss.T * (tensor_gluing * q))[0] + coupling * rho
        shifted_psi = (sp.I * bs * (tensor_gluing * p)
                       - coupling * vector_gluing * current)
        exact(f"axis {axis}: source drive, constraints, and q.tau pairing glue",
              is_zero(shifted_drive - tensor_gluing * drive)
              and is_zero(shifted_psi0 - psi0)
              and is_zero(shifted_psi - vector_gluing * psi)
              and is_zero((tensor_gluing * q).T * (tensor_gluing * tau)
                          - q.T * tau))

    # A TT step source gives an actual closed retarded response.
    r, time = sp.symbols("r time", positive=True, real=True)
    ba, ta, sa, kpa, kqa, r2a = tensor_data(sp.Matrix([0, 0, r]))
    plus = sp.Matrix([1, -1, 0, 0, 0, 0]) / sp.sqrt(2)
    step_response = -coupling * (1 - sp.cos(r * time)) * plus
    exact("axis plus polarization is TT", is_zero(ba * plus) and is_zero(ta.T * plus))
    exact("TT source drive is r^2 times the source", is_zero(kqa * kpa * plus - r2a * plus))
    exact("retarded TT step response solves the driven wave equation",
          is_zero(sp.diff(step_response, time, 2) + r2a * step_response + coupling * r2a * plus))
    exact("retarded TT step response has zero initial data",
          is_zero(step_response.subs(time, 0)) and is_zero(sp.diff(step_response, time).subs(time, 0)))

    # The removed k=0 gravity block cannot absorb total matter energy/momentum.
    rho0 = sp.symbols("rho0", real=True, nonzero=True)
    current0_component = sp.symbols("j0_nonzero", real=True, nonzero=True)
    current0 = sp.Matrix([current0_component, 0, 0])
    b0, _, s0, _, _, _ = tensor_data(sp.zeros(3, 1))
    exact("all vacuum gravitational constraints vanish at k=0", is_zero(b0) and is_zero(s0))
    exact("for g nonzero, nonzero total energy is incompatible with the deleted homogeneous block",
          sp.simplify(coupling * rho0).is_nonzero is True)
    exact("for g nonzero, a nonzero homogeneous current is likewise incompatible",
          sp.simplify((-coupling * current0)[0]).is_nonzero is True)


def scalar_matter_certificate() -> None:
    print("\nDYNAMICAL SCALAR: EXACT 1D COLLINEAR WARD COMPLEX")
    size = 4
    phi = sp.symbols(f"f0:{size}", real=True)
    mom = sp.symbols(f"p0:{size}", real=True)
    mass2, lam = sp.symbols("mass2 lam", real=True)
    grad = [phi[(site + 1) % size] - phi[site] for site in range(size)]
    lap = [
        phi[(site + 1) % size] - 2 * phi[site] + phi[(site - 1) % size]
        for site in range(size)
    ]

    def time_derivative(expression: sp.Expr, interaction: bool) -> sp.Expr:
        result = 0
        for site in range(size):
            force = lap[site] - mass2 * phi[site]
            if interaction:
                force -= lam * phi[site] ** 3 / 6
            result += sp.diff(expression, phi[site]) * mom[site]
            result += sp.diff(expression, mom[site]) * force
        return sp.expand(result)

    density = [
        mom[site] ** 2 / 2
        + mass2 * phi[site] ** 2 / 2
        + (grad[site] ** 2 + grad[(site - 1) % size] ** 2) / 4
        + lam * phi[site] ** 4 / 24
        for site in range(size)
    ]
    flux = [
        -(mom[site] + mom[(site + 1) % size]) * grad[site] / 2
        for site in range(size)
    ]

    for site in range(size):
        residual = (
            time_derivative(density[site], True)
            + flux[site]
            - flux[(site - 1) % size]
        )
        exact(f"scalar energy continuity at site {site}", is_zero(residual))

    repaired_stress = [
        mom[site] ** 2 / 2
        + grad[site] * grad[(site - 1) % size] / 2
        - mass2 * phi[site] ** 2 / 2
        for site in range(size)
    ]
    naive_stress = [
        mom[site] ** 2 / 2
        + (grad[site] ** 2 + grad[(site - 1) % size] ** 2) / 4
        - mass2 * phi[site] ** 2 / 2
        for site in range(size)
    ]
    for site in range(size):
        free_residual = (
            time_derivative(flux[site], False)
            + repaired_stress[(site + 1) % size]
            - repaired_stress[site]
        )
        exact(f"repaired free-scalar momentum Ward identity at link {site}", is_zero(free_residual))

    exact("local free-scalar repair is -one-quarter Laplacian-squared",
          all(is_zero(repaired_stress[s] - naive_stress[s] + lap[s] ** 2 / 4)
              for s in range(size)))

    sample = {
        phi[0]: 0, phi[1]: 1, phi[2]: 2, phi[3]: 4,
        mom[0]: 0, mom[1]: 0, mom[2]: 0, mom[3]: 0,
        mass2: 3,
    }
    naive_residuals = [
        sp.simplify(
            time_derivative(flux[site], False)
            + naive_stress[(site + 1) % size]
            - naive_stress[site]
        ).subs(sample)
        for site in range(size)
    ]
    exact("naive averaged-gradient scalar stress fails on rational data",
          naive_residuals == [sp.Rational(-25, 4), sp.Rational(1, 4),
                              sp.Rational(35, 4), sp.Rational(-11, 4)])

    def poisson(left: sp.Expr, right: sp.Expr) -> sp.Expr:
        return sp.expand(sum(
            sp.diff(left, phi[site]) * sp.diff(right, mom[site])
            - sp.diff(left, mom[site]) * sp.diff(right, phi[site])
            for site in range(size)
        ))

    bracket_sample = poisson(density[0].subs(lam, 0), flux[0]).subs({
        **sample,
        mom[0]: 1, mom[1]: 0, mom[2]: -1, mom[3]: 2,
    })
    exact("dynamical source densities give a nonzero order-g-squared constraint bracket",
          sp.simplify(bracket_sample - sp.Rational(1, 2)) == 0)

    interacting_stress = [
        repaired_stress[site] - lam * phi[site] ** 4 / 24
        for site in range(size)
    ]
    interaction_residuals = []
    for site in range(size):
        residual = sp.factor(
            time_derivative(flux[site], True)
            + interacting_stress[(site + 1) % size]
            - interacting_stress[site]
        )
        expected = (
            lam
            * (phi[site] + phi[(site + 1) % size])
            * (phi[(site + 1) % size] - phi[site]) ** 3
            / 24
        )
        exact(f"phi4 product-rule defect formula at link {site}", is_zero(residual - expected))
        interaction_residuals.append(residual)

    total_defect = sp.simplify(sum(interaction_residuals)).subs(sample)
    exact("phi4 defect has nonzero homogeneous component",
          is_zero(total_defect + sp.Rational(17, 2) * lam))

    # Any periodic divergence sums to zero, so only R-P0 R can be repaired.
    projected = [sp.simplify(value - sum(interaction_residuals) / size)
                 for value in interaction_residuals]
    correction = [sp.Integer(0)]
    for site in range(size - 1):
        correction.append(sp.simplify(correction[-1] - projected[site]))
    closure = [
        sp.simplify(correction[(site + 1) % size] - correction[site] + projected[site])
        for site in range(size)
    ]
    exact("projected inverse-divergence repair closes periodically", all(is_zero(x) for x in closure))
    exact("unprojected phi4 defect cannot be a periodic divergence", not is_zero(sum(interaction_residuals)))


def fermion_matter_certificate() -> None:
    print("\nDYNAMICAL FERMION: COLLINEAR WARD VERTICES (RANGES 1/2/3)")
    p, transfer = sp.symbols("p transfer", real=True)
    eps_in = sp.sin(p)
    eps_out = sp.sin(p + transfer)
    delta = eps_out - eps_in
    kappa = 2 * sp.sin(transfer / 2)
    average_energy = (eps_out + eps_in) / 2
    current_vertex = sp.cos(p + transfer / 2) * average_energy
    stress_vertex = sp.cos(p + transfer / 2) ** 2 * average_energy

    exact("nearest-neighbour dispersion divided difference",
          is_zero(sp.trigsimp(delta - kappa * sp.cos(p + transfer / 2))))
    exact("fermion energy Ward vertex", is_zero(sp.trigsimp(delta * average_energy - kappa * current_vertex)))
    exact("fermion momentum Ward vertex", is_zero(sp.trigsimp(delta * current_vertex - kappa * stress_vertex)))

    sample = {p: sp.pi / 6, transfer: sp.pi / 3}
    exact("fermion sample has rational exact energy vertex",
          sp.simplify(average_energy.subs(sample) - sp.Rational(3, 4)) == 0)
    exact("fermion sample has rational exact current vertex",
          sp.simplify(current_vertex.subs(sample) - sp.Rational(3, 8)) == 0)
    exact("naive continuum fermion vertex violates finite-spacing Ward identity",
          sp.simplify((delta * average_energy - kappa * average_energy).subs(sample))
          == -sp.Rational(3, 8))


def floating_regressions() -> None:
    print("\nFLOATING-POINT REGRESSIONS (NON-THEOREM-BEARING)")
    rng = np.random.default_rng(20260905)
    matrix_errors = []
    drive_errors = []
    for _ in range(8):
        k_np = rng.normal(size=3)
        k = sp.Matrix(k_np)
        b, trace, scalar, kp, kq, r2 = tensor_data(k)
        b = np.asarray(b, dtype=float)
        trace = np.asarray(trace, dtype=float).reshape(6)
        scalar = np.asarray(scalar, dtype=float).reshape(6)
        kp = np.asarray(kp, dtype=float)
        kq = np.asarray(kq, dtype=float)
        tau = rng.normal(size=6)
        c = kq @ kp @ kq
        matrix_errors.append(np.linalg.norm(c - float(r2) * kq - np.outer(scalar, scalar) / 2))
        drive = kq @ kp @ tau - scalar * rng.normal() / 2
        drive_errors.append(np.linalg.norm(b @ drive))
    floating("random-fibre curvature identity", max(matrix_errors), 2.0e-10)
    floating("random-source transverse drive", max(drive_errors), 2.0e-10)

    scalar_errors = []
    for _ in range(16):
        f = rng.normal(size=9)
        pi = rng.normal(size=9)
        grad = np.roll(f, -1) - f
        lap = np.roll(f, -1) - 2 * f + np.roll(f, 1)
        flux = -(pi + np.roll(pi, -1)) * grad / 2
        stress = pi**2 / 2 + grad * np.roll(grad, 1) / 2 - 0.7 * f**2 / 2
        dot_flux = -(
            (lap - 0.7 * f) + np.roll(lap - 0.7 * f, -1)
        ) * grad / 2 - (pi + np.roll(pi, -1)) * (np.roll(pi, -1) - pi) / 2
        scalar_errors.append(np.max(np.abs(dot_flux + np.roll(stress, -1) - stress)))
    floating("random free-scalar repaired Ward identity", max(scalar_errors), 2.0e-11)

    fermion_errors = []
    for _ in range(64):
        p = rng.uniform(-math.pi, math.pi)
        transfer = rng.uniform(-2.8, 2.8)
        delta = math.sin(p + transfer) - math.sin(p)
        kappa = 2 * math.sin(transfer / 2)
        rho = (math.sin(p + transfer) + math.sin(p)) / 2
        current = math.cos(p + transfer / 2) * rho
        fermion_errors.append(abs(delta * rho - kappa * current))
    floating("random fermion energy Ward vertex", max(fermion_errors), 2.0e-14)


def run() -> int:
    global COUNTS
    reset()
    COUNTS = Counts()
    print("matter_coupling_checker -- staggered tensor source and first-order matter gate")
    external_source_certificate()
    scalar_matter_certificate()
    fermion_matter_certificate()
    floating_regressions()
    all_pass = (
        COUNTS.exact_pass == COUNTS.exact_total
        and COUNTS.float_pass == COUNTS.float_total
    )
    print("\nCOUNTS")
    print(f"  exact: {COUNTS.exact_pass}/{COUNTS.exact_total} PASS")
    print(f"  float: {COUNTS.float_pass}/{COUNTS.float_total} PASS")
    print(
        "VERDICT: GENERIC_PRESCRIBED_SOURCE_DECLARED_STAGGERED_FOURIER_CONDITIONAL; "
        "COLLINEAR_FREE_MATTER_WARD_REPAIRS; PHI4_AND_HOMOGENEOUS_OBSTRUCTIONS_EXPLICIT; "
        "FULL_3D_MATTER_AND_QUANTUM_KUBO_OPEN"
        if all_pass
        else "VERDICT: CHECKER_FAILURE"
    )
    return summary("v1035 matter coupling")


if __name__ == "__main__":
    raise SystemExit(run())
