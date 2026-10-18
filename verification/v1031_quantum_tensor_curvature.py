#!/usr/bin/env python3
"""Exact and finite regression checks for the free quantum curvature target.

Standalone isolated artifact: no repository imports, no TFPT parent, T7, TOE,
or RH claim.  Universal statements are proved in PROOF.tex; floating-point
checks below are implementation regressions, not substitutes for those proofs.

Port provenance: native verification port of
`toe_round6_tensor_quantum/tensor_quantum_curvature.py`
(source SHA-256 1d681300577db5a13411ed8878cdab419b3d20974f760b190553e6164824f56f).
The port changes only harness integration and execution lifecycle.
"""
from __future__ import annotations

import itertools
import math
import time

import numpy as np
import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


COUNT = 0
FAILURES = 0
PAIRS = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
MASKS = ((0, 0, 0), (0, 0, 0), (0, 0, 0),
         (0, 1, 1), (1, 0, 1), (1, 1, 0))


def check(label: str, condition: bool) -> None:
    global COUNT, FAILURES
    COUNT += 1
    passed = suite_check(label, bool(condition))
    FAILURES += int(not passed)


def zero(matrix) -> bool:
    if isinstance(matrix, sp.MatrixBase):
        return all(sp.simplify(sp.expand(entry)) == 0 for entry in matrix)
    return bool(np.max(np.abs(np.asarray(matrix))) < 2.0e-9)


def symbolic_tensor_data(k: sp.Matrix):
    basis = []
    for i, j in PAIRS:
        element = sp.zeros(3)
        element[i, j] = element[j, i] = 1 if i == j else 1/sp.sqrt(2)
        basis.append(element)
    b = sp.Matrix.hstack(*(element*k for element in basis))
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    r2 = (k.T*k)[0]
    v = b.T*k
    scalar = v-r2*trace
    kp = sp.eye(6)-trace*trace.T/2
    kq = r2*(sp.eye(6)-trace*trace.T)-2*b.T*b+trace*v.T+v*trace.T
    c = sp.expand(kq*kp*kq)
    return basis, b, trace, scalar, kp, kq, c, r2


def explicit_ptt(k: sp.Matrix, basis: list[sp.Matrix], r2: sp.Expr) -> sp.Matrix:
    projector = sp.eye(3)-k*k.T/r2
    columns = []
    for element in basis:
        image = projector*element*projector
        image -= projector*sp.trace(projector*element)/2
        columns.append(sp.Matrix([sp.trace(test.T*image) for test in basis]))
    return sp.Matrix.hstack(*columns)


def universal_symbolic_checks():
    x, y, z = sp.symbols("x y z", real=True)
    k = sp.Matrix([x, y, z])
    basis, b, trace, scalar, kp, kq, c, r2 = symbolic_tensor_data(k)
    ptt = explicit_ptt(k, basis, r2)

    check("all-momentum Kq square identity",
          zero(kq*kq-r2*kq-scalar*scalar.T))
    check("all-momentum curvature bracket identity",
          zero(c-r2*kq-scalar*scalar.T/2))
    check("polynomial C equals r^4 times separate index-form TT projector",
          zero(c-r2**2*ptt))
    check("TT projector is symmetric and idempotent",
          zero(ptt-ptt.T) and zero(ptt*ptt-ptt))
    check("C is symmetric", zero(c-c.T))
    check("C squared equals r^4 C", zero(c*c-r2**2*c))
    check("C trace fixes rank two away from zero",
          sp.simplify(sp.trace(c)-2*r2**2) == 0)
    check("C is transverse and traceless on both slots",
          zero(b*c) and zero(trace.T*c) and zero(c*b.T) and zero(c*trace))
    check("TT projector has the same transverse-traceless range",
          zero(b*ptt) and zero(trace.T*ptt))
    check("C is a degree-four polynomial with no zero-momentum residue",
          max(sp.Poly(entry, x, y, z).total_degree() for entry in c) == 4
          and zero(c.subs({x: 0, y: 0, z: 0})))
    return (x, y, z), kq, c


def rational_fibre_checks():
    momenta = (
        (sp.Rational(1), sp.Rational(0), sp.Rational(0)),
        (sp.Rational(1), sp.Rational(2), sp.Rational(2)),
        (sp.Rational(-2), sp.Rational(3), sp.Rational(6)),
        (sp.Rational(1, 2), sp.Rational(-2, 3), sp.Rational(5, 6)),
    )
    lam = sp.symbols("lambda")
    for momentum in momenta:
        k = sp.Matrix(momentum)
        _, b, trace, _, _, kq, c, r2 = symbolic_tensor_data(k)
        r = sp.sqrt(r2)
        r4 = r2**2
        charpoly = sp.expand(c.charpoly(lam).as_expr())
        expected = sp.expand(lam**4*(lam-r4)**2)
        physical = sp.Matrix.hstack(*b.col_join(trace.T).nullspace())
        check(f"exact rational fibre {momentum}: characteristic polynomial rank two",
              sp.simplify(charpoly-expected) == 0 and c.rank() == 2)
        check(f"exact rational fibre {momentum}: TT action and constraint kernel",
              physical.cols == 2 and zero(kq*physical-r2*physical)
              and zero(c*physical-r4*physical)
              and zero(b*physical) and zero(trace.T*physical))

        # V+i Omega/2 = Q Q^*/(2r), avoiding numerical eigenvalue inference.
        z6 = sp.zeros(6)
        omega = sp.BlockMatrix([[z6, c], [-c, z6]]).as_explicit()
        covariance = sp.diag(c/(2*r), r*c/2)
        csqrt = c/r2
        qfactor = sp.Matrix.vstack(csqrt, -sp.I*r*csqrt)
        uncertainty = covariance+sp.I*omega/2
        check(f"exact rational fibre {momentum}: uncertainty factorization",
              zero(uncertainty-qfactor*qfactor.conjugate().T/(2*r)))
        check(f"exact rational fibre {momentum}: pure two-polarization saturation",
              qfactor.rank() == 2 and uncertainty.rank() == 2)
        check(f"exact rational fibre {momentum}: symmetric EF covariance is zero",
              zero(covariance[:6, 6:]) and zero(covariance[6:, :6]))


def bloch_and_real_mode_checks(symbolic_data):
    symbols, kq, c = symbolic_data
    for axis, variable in enumerate(symbols):
        gluing = sp.diag(*(
            -1 if MASKS[component][axis] else 1 for component in range(6)
        ))
        reflected = {variable: -variable}
        check(f"Bloch gluing of Kq under kappa_{axis} sign reversal",
              zero(kq.subs(reflected)-gluing*kq*gluing))
        check(f"Bloch gluing of C and both vacuum covariance blocks axis {axis}",
              zero(c.subs(reflected)-gluing*c*gluing))
    check("reality involution C(-kappa)=C(kappa)",
          zero(c.subs(dict(zip(symbols, (-symbols[0], -symbols[1], -symbols[2]))))-c))

    # At a self-conjugate Brillouin corner z=G conjugate(z).  D maps six real
    # coordinates to that fixed real form.  D^{-1} C D is real and rank two.
    for bits in itertools.product((0, 1), repeat=3):
        if bits == (0, 0, 0):
            continue
        kappa = sp.Matrix([2*entry for entry in bits])
        _, _, _, _, _, _, corner_c, _ = symbolic_tensor_data(kappa)
        signs = [(-1)**sum(MASKS[a][i]*bits[i] for i in range(3)) for a in range(6)]
        gluing = sp.diag(*signs)
        real_form = sp.diag(*(1 if sign == 1 else sp.I for sign in signs))
        transformed = sp.simplify(real_form.inv()*corner_c*real_form)
        check(f"self-conjugate corner {bits}: covariance preserves Bloch real form",
              zero(gluing*corner_c*gluing-corner_c)
              and all(sp.im(entry) == 0 for entry in transformed)
              and transformed.rank() == 2)

    for size in (3, 4, 5, 6, 8):
        self_conjugate = 0 if size % 2 else 7
        conjugate_pairs = (size**3-1-self_conjugate)//2
        real_oscillators = 2*self_conjugate+4*conjugate_pairs
        check(f"L={size} reality/Bloch count gives 2(V-1) oscillators",
              real_oscillators == 2*(size**3-1))


def numeric_tensor_data(kappa: np.ndarray):
    basis = []
    for i, j in PAIRS:
        element = np.zeros((3, 3), dtype=float)
        element[i, j] = element[j, i] = 1.0 if i == j else 1/math.sqrt(2)
        basis.append(element)
    b = np.column_stack([element@kappa for element in basis])
    trace = np.array([1, 1, 1, 0, 0, 0], dtype=float)
    r2 = float(kappa@kappa)
    v = b.T@kappa
    kp = np.eye(6)-np.outer(trace, trace)/2
    kq = r2*(np.eye(6)-np.outer(trace, trace))-2*b.T@b
    kq += np.outer(trace, v)+np.outer(v, trace)
    c = kq@kp@kq
    return c, r2


def finite_volume_regressions():
    for size in (3, 4, 5, 6):
        frequencies = 2*math.pi*np.fft.fftfreq(size)
        fibres = 0
        min_positive_frequency = float("inf")
        worst_projector = 0.0
        worst_uncertainty = 0.0
        for k in itertools.product(frequencies, repeat=3):
            kappa = 2*np.sin(np.asarray(k)/2)
            c, r2 = numeric_tensor_data(kappa)
            if r2 < 1.0e-14:
                continue
            fibres += 1
            r = math.sqrt(r2)
            r4 = r2**2
            eigen_c = np.linalg.eigvalsh(c)
            expected = np.array([0, 0, 0, 0, r4, r4], dtype=float)
            worst_projector = max(worst_projector,
                                  float(np.max(np.abs(eigen_c-expected))))
            omega = np.block([[np.zeros((6, 6)), c], [-c, np.zeros((6, 6))]])
            covariance = np.block([
                [c/(2*r), np.zeros((6, 6))],
                [np.zeros((6, 6)), r*c/2],
            ])
            uncertainty = covariance+0.5j*omega
            worst_uncertainty = min(worst_uncertainty,
                                    float(np.min(np.linalg.eigvalsh(uncertainty))))
            min_positive_frequency = min(min_positive_frequency, r)
        check(f"L={size} all nonzero fibres have two projector eigenvalues",
              fibres == size**3-1 and worst_projector < 3.0e-11)
        check(f"L={size} complete finite-volume uncertainty matrix is positive",
              worst_uncertainty > -3.0e-11)
        check(f"L={size} homogeneous block removal leaves a positive gap",
              min_positive_frequency > 0)


def thermodynamic_regression():
    # Trace(V_EE)=r^3.  The periodic smooth weight prevents a constant-function
    # coincidence.  The theorem is analytic; this only catches normalization.
    def estimate(size: int) -> float:
        k = 2*math.pi*np.fft.fftfreq(size)
        kx = k[:, None, None]
        ky = k[None, :, None]
        kz = k[None, None, :]
        r2 = (2*np.sin(kx/2))**2+(2*np.sin(ky/2))**2+(2*np.sin(kz/2))**2
        weight = np.exp(np.cos(kx)+np.cos(ky)+np.cos(kz)-3)
        return float(np.mean(weight*r2**1.5))

    values = {size: estimate(size) for size in (12, 24, 48, 96)}
    reference = values[96]
    errors = {size: abs(values[size]-reference) for size in (12, 24, 48)}
    check("fixed-spacing thermodynamic Riemann sums converge",
          errors[48] < errors[24] < errors[12] and errors[48] < 2.0e-5)
    print("  thermodynamic trace(V_EE) weighted values:", values, flush=True)


def continuum_regressions():
    # Gauss-Hermite integrates exp(-|p|^2) times trace(V_EE).  Comparing the
    # lattice and continuum multipliers on identical nodes isolates a->0.
    nodes, weights = np.polynomial.hermite.hermgauss(36)
    px = nodes[:, None, None]
    py = nodes[None, :, None]
    pz = nodes[None, None, :]
    measure = (weights[:, None, None]*weights[None, :, None]
               * weights[None, None, :])/(2*math.pi)**3
    continuum_r = np.sqrt(px*px+py*py+pz*pz)
    continuum_quadrature = float(np.sum(measure*continuum_r**3))
    exact_continuum = 1/(2*math.pi**2)
    check("Gaussian continuum covariance quadrature matches analytic radial integral",
          abs(continuum_quadrature-exact_continuum) < 2.0e-4)

    lattice_values = {}
    for spacing in (0.4, 0.2, 0.1):
        kx = 2*np.sin(spacing*px/2)/spacing
        ky = 2*np.sin(spacing*py/2)/spacing
        kz = 2*np.sin(spacing*pz/2)/spacing
        lattice_r = np.sqrt(kx*kx+ky*ky+kz*kz)
        inside = ((np.abs(px) <= math.pi/spacing)
                  & (np.abs(py) <= math.pi/spacing)
                  & (np.abs(pz) <= math.pi/spacing))
        lattice_values[spacing] = float(np.sum(measure*lattice_r**3*inside))
    errors = [abs(lattice_values[a]-continuum_quadrature) for a in (0.4, 0.2, 0.1)]
    check("a->0 Gaussian-smeared EE covariance multiplier converges",
          errors[2] < errors[1] < errors[0] and errors[2] < 8.0e-4)
    print("  continuum trace(V_EE) values:", lattice_values,
          "quadrature limit", continuum_quadrature, flush=True)

    # Pointwise dynamic multiplier regression at a generic physical momentum.
    p = np.array([0.7, -1.1, 1.6])
    time_value = 0.73
    continuum_c, r2 = numeric_tensor_data(p)
    continuum_dynamic = continuum_c*math.sin(math.sqrt(r2)*time_value)/math.sqrt(r2)
    dynamic_errors = []
    for spacing in (0.4, 0.2, 0.1):
        kappa = 2*np.sin(spacing*p/2)/spacing
        lattice_c, lattice_r2 = numeric_tensor_data(kappa)
        lattice_dynamic = (lattice_c*math.sin(math.sqrt(lattice_r2)*time_value)
                           / math.sqrt(lattice_r2))
        dynamic_errors.append(float(np.linalg.norm(lattice_dynamic-continuum_dynamic)))
    check("a->0 polynomial Pauli-Jordan multiplier converges pointwise",
          dynamic_errors[2] < dynamic_errors[1] < dynamic_errors[0])


def finite_ccr_no_go():
    for dimension in (2, 3, 5, 8):
        annihilator = sp.zeros(dimension)
        for level in range(1, dimension):
            annihilator[level-1, level] = sp.sqrt(level)
        q = (annihilator+annihilator.T)/sp.sqrt(2)
        p = (annihilator-annihilator.T)/(sp.I*sp.sqrt(2))
        top = sp.zeros(dimension)
        top[dimension-1, dimension-1] = 1
        defect = q*p-p*q-sp.I*sp.eye(dimension)
        check(f"finite-dimensional CCR negative control d={dimension}",
              zero(defect+sp.I*dimension*top)
              and sp.trace(q*p-p*q) == 0
              and sp.trace(defect) == -sp.I*dimension)


def run() -> int:
    global COUNT, FAILURES
    reset()
    COUNT = 0
    FAILURES = 0
    started = time.perf_counter()
    print("free quantum curvature target: exact certificate + finite regressions")
    symbolic_data = universal_symbolic_checks()
    rational_fibre_checks()
    bloch_and_real_mode_checks(symbolic_data)
    finite_volume_regressions()
    thermodynamic_regression()
    continuum_regressions()
    finite_ccr_no_go()
    elapsed = time.perf_counter()-started
    print(f"VERDICT: {COUNT-FAILURES}/{COUNT} checks passed "
          f"(53 exact, 16 floating regressions) in {elapsed:.3f}s; "
          "FREE_ZERO_MEAN_CURVATURE_WEYL_FOCK_STATE_AND_DISTRIBUTION_LIMIT_CERTIFIED; "
          "MICROSCOPIC_TFPT_PARENT_NONLINEAR_COUPLING_T7_AND_TOE_OPEN")
    return summary("v1031 quantum tensor curvature")


if __name__ == "__main__":
    raise SystemExit(run())
