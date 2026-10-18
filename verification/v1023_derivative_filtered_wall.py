#!/usr/bin/env python3
"""v1023 -- derivative-filtered physical--mirror wall certificate.

Exact/numerical certificate for the derivative-filtered wall coupling.

The certificate addresses the conflict found by the full-rank onsite wall
term: a nonzero onsite pairing lifts every physical GW zero mode.  Replacing
the physical annihilator p by D_GW p makes the mixing vanish precisely on
ker(D_GW), while keeping a uniformly separated mirror-continuation band.
The canonical bare mirror operator is not itself an invariant sector: for
every nonzero singular value it has low-band weight tending to zero only as
O(s^2).  Thus the result does not establish a gap in the bare-mirror response
and the infrared branch is quadratic (z=2), not a Weyl cone.

This is a finite one-particle/quasi-free theorem.  It is deliberately not
advertised as a proof of an interacting Standard-Model continuum limit.

Contracts: CHIRAL4D.NOMIRROR.01 [O], CHIRAL4D.MIRROR.DET16.01 [C],
and TFPT.TOE.COMPLETE.01 [O].  No marker moves.  The exact algebra is
SymPy; the finite covariance/spectrum witnesses are deterministic float64.
Python-only / Wolfram mirror deferred.  NO RH CLAIM.
"""

from __future__ import annotations

import json
import math
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np
import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


TOL = 2.0e-10


def check(name: str, condition: bool, detail: str = "") -> None:
    label = name if not detail else f"{name} -- {detail}"
    suite_check(label, bool(condition))


def dagger(a: np.ndarray) -> np.ndarray:
    return a.conj().T


def wall_block(d: np.ndarray, delta: float, lam: float, g: float) -> np.ndarray:
    """Block on physical right-singular and mirror left-singular spaces."""
    n = d.shape[0]
    return np.block(
        [
            [lam * g * g * dagger(d) @ d, lam * g * dagger(d)],
            [lam * g * d, (delta + lam) * np.eye(n)],
        ]
    )


def symbolic_certificate() -> dict[str, str]:
    delta, lam, g, s = sp.symbols(
        "Delta lambda g s", positive=True, real=True
    )
    # charpoly intentionally wants an assumption-free indeterminate.
    mu = sp.Symbol("mu")
    block = sp.Matrix(
        [[lam * g**2 * s**2, lam * g * s], [lam * g * s, delta + lam]]
    )
    determinant = sp.factor(block.det())
    trace = sp.factor(sp.trace(block))
    characteristic = sp.factor(block.charpoly(mu).as_expr())
    expected_characteristic = sp.expand(
        mu**2 - trace * mu + lam * g**2 * delta * s**2
    )
    check("symbolic determinant", determinant == lam * g**2 * delta * s**2)
    check("symbolic characteristic polynomial", sp.expand(characteristic - expected_characteristic) == 0)

    block_zero = block.subs(s, 0)
    check("GW kernel is exactly preserved", block_zero.nullspace() == [sp.Matrix([1, 0])])
    check("mirror partner at a GW zero mode costs Delta+lambda", block_zero[1, 1] == delta + lam)
    check(
        "bare mirror direction is not invariant for nonzero singular value",
        sp.factor(block[0, 1]) == lam * g * s,
    )

    # Rationalised smaller eigenvalue; this avoids a branch-sensitive series.
    disc = sp.factor(trace**2 - 4 * determinant)
    mu_minus = sp.factor(2 * determinant / (trace + sp.sqrt(disc)))
    expected_ir = lam * g**2 * delta / (delta + lam)
    raw_ir_coefficient = sp.limit(mu_minus / s**2, s, 0, dir="+")
    # At s=0 the discriminant is (Delta+lambda)^2, whose positive square
    # root is Delta+lambda under the declarations above.
    discriminant_at_zero = sp.factor(disc.subs(s, 0))
    check(
        "IR coefficient is positive and exact",
        sp.expand(discriminant_at_zero - (delta + lam) ** 2) == 0
        and sp.simplify(
            raw_ir_coefficient.subs(
                sp.sqrt(sp.expand((delta + lam) ** 2)), delta + lam
            )
            - expected_ir
        )
        == 0,
    )
    ir_coefficient = expected_ir

    onsite = sp.Matrix([[lam * g**2, lam * g], [lam * g, delta + lam]])
    check("unfiltered onsite mutant lifts the zero mode", sp.factor(onsite.det()) == lam * g**2 * delta)
    return {
        "determinant": str(determinant),
        "trace": str(trace),
        "characteristic_polynomial": str(characteristic),
        "ir_coefficient": str(ir_coefficient),
        "kernel": "ker(H_wall)=ker(D_GW) on the physical summand",
    }


def covariance_certificate() -> dict[str, float]:
    # A deterministic normal D with one exact zero and three nonzero modes.
    phases = np.diag([1.0, 1j, -1.0, -1j])
    singulars = np.diag([0.0, 0.4, 0.9, 1.3])
    fourier = np.fft.fft(np.eye(4)) / 2.0
    d = fourier @ phases @ singulars @ dagger(fourier)

    # Deterministic unitary gauge transformation.
    raw = np.array(
        [[1, 1j, 0, 1], [1j, 2, 1, 0], [0, 1, 2j, 1], [1, 0, 1, -1j]],
        dtype=complex,
    )
    unitary, _ = np.linalg.qr(raw)
    d_prime = unitary @ d @ dagger(unitary)
    delta, lam, g = 3.0, 1.0, 0.5
    h = wall_block(d, delta, lam, g)
    h_prime = wall_block(d_prime, delta, lam, g)
    lifted_u = np.block(
        [[unitary, np.zeros_like(unitary)], [np.zeros_like(unitary), unitary]]
    )
    covariance_defect = float(np.linalg.norm(h_prime - lifted_u @ h @ dagger(lifted_u)))
    check("gauge covariance of the full wall block", covariance_defect < TOL, f"defect={covariance_defect:.3e}")

    evals = np.linalg.eigvalsh(h)
    zero_count = int(np.sum(np.abs(evals) < 1.0e-10))
    d_nullity = d.shape[0] - np.linalg.matrix_rank(d, tol=1.0e-10)
    check("finite block nullity equals nullity(D_GW)", zero_count == d_nullity == 1)

    # SVD reduction proves that the matrix is the direct sum of the 2x2
    # symbolic blocks.  Check the multiset explicitly.
    sv = np.linalg.svd(d, compute_uv=False)
    expected = []
    high = []
    low = []
    for value in sv:
        a = delta + lam + lam * g * g * value * value
        det = lam * g * g * delta * value * value
        pair = [(a - math.sqrt(max(0.0, a * a - 4 * det))) / 2,
                (a + math.sqrt(max(0.0, a * a - 4 * det))) / 2]
        low.append(pair[0])
        high.append(pair[1])
        expected.extend(pair)
    spectral_defect = float(np.max(np.abs(np.sort(evals) - np.sort(expected))))
    check("SVD block decomposition", spectral_defect < TOL, f"defect={spectral_defect:.3e}")
    check("mirror-continuation band is uniformly separated", min(high) >= delta + lam - TOL)
    check("all non-GW-kernel modes are positive", sum(x > 1.0e-12 for x in low) == 3)

    return {
        "gauge_covariance_defect": covariance_defect,
        "spectral_reduction_defect": spectral_defect,
        "zero_modes": zero_count,
        "smallest_high_band_energy": float(min(high)),
        "smallest_positive_low_band_energy": float(min(x for x in low if x > 1.0e-12)),
    }


def infrared_lattice_certificate() -> dict[str, object]:
    delta, lam, g = 3.0, 1.0, 0.5
    predicted = lam * g * g * delta / (delta + lam)
    rows = []
    for n in (8, 16, 32, 64, 128):
        # Singular value of a local first-difference GW surrogate at the
        # smallest nonzero lattice momentum.  Only the infrared scaling is
        # used here; this is not a numerical overlap-operator substitute.
        s = 2.0 * math.sin(math.pi / n)
        a = delta + lam + lam * g * g * s * s
        det = lam * g * g * delta * s * s
        mu_minus = 2.0 * det / (a + math.sqrt(a * a - 4.0 * det))
        ratio = mu_minus / (s * s)
        rows.append({"N": n, "s": s, "mu_minus": mu_minus, "mu_minus_over_s2": ratio})
    errors = [abs(row["mu_minus_over_s2"] - predicted) for row in rows]
    check("infrared coefficient converges", all(a > b for a, b in zip(errors[:-1], errors[1:])))
    check("infrared coefficient reaches 1e-4", errors[-1] < 1.0e-4)
    return {"predicted_coefficient": predicted, "rows": rows, "last_error": errors[-1]}


def rank_nullity_certificate() -> dict[str, str]:
    # Equal physical and mirror dimensions.  A full-rank constant pairing
    # has no physical kernel; a rank-deficient one leaves at least one
    # unpaired mirror direction as well.  The D filter evades this by being
    # full rank away from the protected physical kernel and zero on it.
    full = np.eye(4)
    deficient = np.diag([0.0, 1.0, 1.0, 1.0])
    check("constant full-rank pairing has no protected physical kernel", np.linalg.matrix_rank(full) == 4)
    check(
        "constant rank-deficient pairing leaves an unpaired direction",
        np.linalg.matrix_rank(deficient) == 3
        and deficient.shape[0] - np.linalg.matrix_rank(deficient) == 1,
    )
    return {
        "equal_dimension_bilinear_no_go": (
            "for B:C^n_phys->C^n_mir, surjectivity needed to pair every mirror "
            "direction implies rank(B)=n and hence ker(B)=0"
        ),
        "escape": "B=g*D_GW is zero only on the index-protected physical kernel",
    }


def run() -> int:
    reset()
    print("v1023 -- derivative-filtered wall; finite quasi-free subgate, no marker move")
    report = {
        "symbolic": symbolic_certificate(),
        "covariance_and_spectrum": covariance_certificate(),
        "infrared": infrared_lattice_certificate(),
        "rank_nullity": rank_nullity_certificate(),
        "claim_boundary": {
            "proved": [
                "nonzero derivative-filtered physical-mirror mixing",
                "exact preservation of ker(D_GW)",
                "uniform separation of the mirror-continuation band by at least Delta+lambda",
                "positive renormalised low-energy D_GW^dagger D_GW dispersion",
                "gauge covariance when D_GW is gauge covariant",
            ],
            "not_proved": [
                "a spectral gap in the canonical bare-mirror operator response",
                "a linear Weyl cone (the certified infrared branch is quadratic)",
                "a canonical DET16/DET32 realization of the mirror variable",
                "admissibility and quasilocality for an interacting many-body parent",
                "anomaly, index and measure control",
                "interacting anomaly-free chiral continuum limit",
                "Wilson universality or Lorentz restoration",
                "nonperturbative many-body stability under arbitrary extra interactions",
            ],
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("VERDICT: DERIVATIVE_FILTERED_WALL_SUBGATE_PROVED; "
          "INTERACTING_4D_CONTINUUM_OPEN")
    return summary("v1023 derivative-filtered physical--mirror wall")


if __name__ == "__main__":
    raise SystemExit(run())
