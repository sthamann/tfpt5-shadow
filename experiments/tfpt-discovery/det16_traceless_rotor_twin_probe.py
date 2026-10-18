#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""det16_traceless_rotor_twin_probe -- CHIRAL4D.MIRROR.DET16.01

FROZEN SPEC v1 (2026-09-03).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.

=======================================================================
MANDATE
=======================================================================
The uniform-charge twin in det16_dynamical_links_probe.py gauges
fermion number.  The DET (fully filled) 4-mode cluster then carries
charge 4, so Gauss invariance forces N | 4 and the N -> infinity
limit is not the physical rotor problem.  The physical DET16 operator
is the Spin(10) epsilon-invariant of the 16, hence neutral under every
gauged U(1) inside SO(10) (tr Y = 0 over the 16).

This probe is the minimal correct 4-mode analogue: replace the charge
vector (1,1,1,1) by the traceless assignment q = (+1,+1,-1,-1).  The
filled DET cluster then has charge 0 and lies in the Gauss sector for
every Z_N, including the exact open-chain U(1) rotor.

=======================================================================
MODEL (frozen; only the charge vector changes)
=======================================================================
Open chain of L four-mode clusters.  Mode charges cycle
q = (+1,+1,-1,-1).  Matter state |n>, n_i in {0,1}.
Cluster charge Q_x = sum_{i in x} q_i n_i.  Link flux on bond b
(between x and x+1) is the cumulative matter charge
e_b = sum_{y <= x} Q_y, represented in Z_N as e mod N centered in
(-N/2, N/2] by the source centered_electric_flux.  Electric term
exactly as the source:

    H_E = h_E * sum_b [centered_electric_flux(e_b, N)]^2

This is the compact U(1) Kogut-Susskind electric energy on an open
chain (no (2 pi / N)^2 factor).  Because |Q_x| <= 2, one has
|e_b| <= 2L, so for N > 4L the centered Z_N representative equals
the integer flux and the Z_N model is identical to the U(1) rotor.

Gauss sector: Q_tot ≡ 0 (mod N); U(1) uses Q_tot = 0.  The DET16
projector term and the product ground (empty/full per cluster) are
the source's toy_hamiltonian / product_ground.  Fermionic hopping is
the source gauge_hopping: a hop of mode i from cluster x to x+1
changes Q_x by -q_i and therefore shifts the intermediate flux by
-q_i (source had q_i = +1).  Total charge is preserved, so hopping
stays in the Gauss sector.  Low-sector gap = first excited minus
ground in the physical sector, via source analyze_grid_point /
deterministic_low_eigenpairs (fixed v0, tol).

=======================================================================
SCAN (frozen)
=======================================================================
N in (2, 3, 4, 5, 6, 8, 12, 16, 32); L in (2, 3);
t in {0.0, 0.05, 0.10, 0.20, 0.40}; h_E in {0.5, 1.0, 2.0}.
U(1) = no wrapping, Q_tot = 0.

DFP window used here: t <= 0.2.  The source sets
DFP_SCANNED_HOPPING_STRENGTH = 0.40 and audits that t = 0.4 lies
outside the cited Fröhlich-Pizzo window (tau_DFP is not numerical).
The portable finite-twin window is therefore t <= 0.2, matching
the projector-probe PASS_t<=0.2_toy language.  G4 uses
DFP_GAP_LOWER_BOUND = 0.5 on that window.

=======================================================================
GATES
=======================================================================
G1  DET empty/full product states lie in the Gauss sector for every
    scanned N (no KeyError).
G2  EXACT SATURATION: for all N > 4L, Delta(N) equals Delta(U(1))
    to 1e-12 at every grid point (Z_N = U(1) bit-identically).
G3  For N <= 4L, report how wrapping changes Delta versus U(1).
G4  U(1) gap >= 1/2 on every window point (t <= 0.2).  PASS/FAIL
    per point, honest.
G5  must-fail control 1: q = (1,1,1,1) reproduces the source Z2 and
    Z4 gaps to 1e-9 and KeyErrors for N = 8.
G6  must-fail control 2: remove the DET16 term at the source
    NO_DET_HOPPING_STRENGTH -> gap collapse.

VERDICT (frozen enum):
  ROTOR_LINKS_NOT_THE_OBSTRUCTION_1D
      G1 and G2 pass and U(1) gap >= 1/2 on the window: on open-chain
      twins, Gauss law makes the U(1) rotor model finite-dimensional;
      the remaining obstruction is >= 2D placement with
      magnetic/plaquette terms.
  ROTOR_GAP_FAILS_1D
      U(1) gap < 1/2 somewhere on the window.
  INCONCLUSIVE
      otherwise (controls fail, saturation fails, or numerics).

HONEST NOTE (printed verbatim):
  traceless-charge twin of the DET16 analogue; exact finite numerics;
  CHIRAL4D.MIRROR.DET16.01 stays [C]; the 16-mode physical case and
  >= 2D placement are not touched.
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np
import scipy.sparse as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from det16_dynamical_links_probe import (  # noqa: E402
    DFP_GAP_LOWER_BOUND,
    DFP_SCANNED_HOPPING_STRENGTH,
    ELECTRIC_STRENGTHS,
    HOPPING_STRENGTHS,
    NO_DET_HOPPING_STRENGTH,
    GaugeModel,
    analyze_grid_point,
    build_model as source_build_model,
    centered_electric_flux,
    deterministic_low_eigenpairs,
    gauge_hopping,
)
from spin10_det16_projector_probe import (  # noqa: E402
    EIG_TOL,
    PHI,
    TOY_CLUSTER_MODES,
    toy_hamiltonian,
)

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

GAUGE_ORDERS = (2, 3, 4, 5, 6, 8, 12, 16, 32)
CLUSTER_COUNTS = (2, 3)
CHARGES_TRACELESS = (1, 1, -1, -1)
CHARGES_UNIFORM = (1, 1, 1, 1)
U1_LABEL = 0
SATURATION_TOL = 1.0e-12
SOURCE_REPRO_TOL = 1.0e-9
WINDOW_HOPPING = tuple(
    strength
    for strength in HOPPING_STRENGTHS
    if strength <= 0.20 + 1.0e-15
)
HONEST_NOTE = (
    "traceless-charge twin of the DET16 analogue; exact finite numerics; "
    "CHIRAL4D.MIRROR.DET16.01 stays [C]; the 16-mode physical case and "
    ">= 2D placement are not touched"
)

CHECKS: list[tuple[str, bool]] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(
        "  [%s] %s%s"
        % ("PASS" if ok else "FAIL", name, ("  " + detail) if detail else "")
    )


def saturation_order(cluster_count: int) -> int:
    """Smallest N such that N > 4L (source-style |flux| <= 2L bound)."""
    return 4 * cluster_count + 1


def cluster_charges(
    state: int, cluster_count: int, charges: tuple[int, ...]
) -> tuple[int, ...]:
    """Signed cluster charges; provenance: cluster_occupations, q-weighted."""
    cluster_mask = (1 << TOY_CLUSTER_MODES) - 1
    result = []
    for cluster in range(cluster_count):
        chunk = (state >> (TOY_CLUSTER_MODES * cluster)) & cluster_mask
        charge = 0
        for bit, value in enumerate(charges):
            if chunk & (1 << bit):
                charge += value
        result.append(charge)
    return tuple(result)


def total_charge(
    state: int, cluster_count: int, charges: tuple[int, ...]
) -> int:
    return sum(cluster_charges(state, cluster_count, charges))


def link_fluxes_charged(
    state: int,
    cluster_count: int,
    gauge_order: int,
    charges: tuple[int, ...],
    wrap: bool,
) -> tuple[int, ...]:
    """Cumulative signed charge; provenance: source link_fluxes."""
    charges_per_cluster = cluster_charges(state, cluster_count, charges)
    cumulative = 0
    fluxes = []
    for charge in charges_per_cluster[:-1]:
        cumulative = cumulative + charge
        if wrap:
            cumulative = cumulative % gauge_order
        fluxes.append(cumulative)
    return tuple(fluxes)


def det_product_states(cluster_count: int) -> list[int]:
    """Empty/full product configurations of the source product_ground."""
    states = []
    for filled_pattern in range(1 << cluster_count):
        matter_state = 0
        for cluster in range(cluster_count):
            if filled_pattern & (1 << cluster):
                matter_state |= ((1 << TOY_CLUSTER_MODES) - 1) << (
                    TOY_CLUSTER_MODES * cluster
                )
        states.append(matter_state)
    return states


def build_charged_model(
    gauge_order: int,
    cluster_count: int,
    charges: tuple[int, ...],
    wrap: bool,
) -> GaugeModel:
    """Source build_model with signed charges and optional U(1) (no wrap)."""
    total_modes = TOY_CLUSTER_MODES * cluster_count
    full_dimension = 1 << total_modes
    if wrap:
        allowed_states = np.fromiter(
            (
                state
                for state in range(full_dimension)
                if total_charge(state, cluster_count, charges) % gauge_order
                == 0
            ),
            dtype=np.int64,
        )
    else:
        allowed_states = np.fromiter(
            (
                state
                for state in range(full_dimension)
                if total_charge(state, cluster_count, charges) == 0
            ),
            dtype=np.int64,
        )
    state_to_index = {
        int(state): index for index, state in enumerate(allowed_states)
    }

    full_mirror, full_projectors = toy_hamiltonian(
        cluster_count, (PHI,) * cluster_count
    )
    selector = np.ix_(allowed_states, allowed_states)
    mirror = full_mirror[selector].tocsr()
    projectors = tuple(
        projector[selector].tocsr() for projector in full_projectors
    )
    hopping = gauge_hopping(allowed_states, state_to_index, cluster_count)

    electric_energies = np.zeros(len(allowed_states), dtype=float)
    for index, state_value in enumerate(allowed_states):
        fluxes = link_fluxes_charged(
            int(state_value), cluster_count, gauge_order, charges, wrap
        )
        if wrap:
            electric_energies[index] = sum(
                centered_electric_flux(flux, gauge_order) ** 2
                for flux in fluxes
            )
        else:
            electric_energies[index] = sum(flux * flux for flux in fluxes)

    # Provenance: source build_model product_ground (KeyError if missing).
    product_ground = np.zeros(len(allowed_states), dtype=complex)
    normalization = 2.0 ** (-0.5 * cluster_count)
    for filled_pattern in range(1 << cluster_count):
        matter_state = 0
        filled_count = 0
        for cluster in range(cluster_count):
            if filled_pattern & (1 << cluster):
                matter_state |= ((1 << TOY_CLUSTER_MODES) - 1) << (
                    TOY_CLUSTER_MODES * cluster
                )
                filled_count += 1
        product_ground[state_to_index[matter_state]] = (
            normalization * np.exp(1j * PHI * filled_count)
        )

    return GaugeModel(
        gauge_order=gauge_order,
        cluster_count=cluster_count,
        allowed_states=allowed_states,
        state_to_index=state_to_index,
        mirror_hamiltonian=mirror,
        electric_energies=electric_energies,
        hopping_hamiltonian=hopping,
        projectors=projectors,
        product_ground=product_ground,
    )


def run_model_grid(model: GaugeModel) -> dict[tuple[float, float], object]:
    results = {}
    for electric_strength in ELECTRIC_STRENGTHS:
        for hopping_strength in HOPPING_STRENGTHS:
            results[(electric_strength, hopping_strength)] = analyze_grid_point(
                model, hopping_strength, electric_strength
            )
    return results


def no_det_splitting(model: GaugeModel) -> tuple[float, int, float]:
    """Source run_mutants no-DET Hamiltonian (h_E = 1 implicit)."""
    hamiltonian = (
        sp.diags(model.electric_energies, format="csr", dtype=complex)
        + NO_DET_HOPPING_STRENGTH * model.hopping_hamiltonian
    ).tocsr()
    eigenvalues, _vectors = deterministic_low_eigenpairs(hamiltonian, count=24)
    ground_splitting = float(eigenvalues[1] - eigenvalues[0])
    degeneracy = int(np.sum(np.abs(eigenvalues - eigenvalues[0]) < EIG_TOL))
    resolved = eigenvalues[eigenvalues > eigenvalues[0] + EIG_TOL]
    excitation = (
        float(resolved[0] - eigenvalues[0]) if len(resolved) else 0.0
    )
    return ground_splitting, degeneracy, excitation


def decide_verdict(g1: bool, g2: bool, g4: bool, controls: bool) -> str:
    if g1 and g2 and g4 and controls:
        return "ROTOR_LINKS_NOT_THE_OBSTRUCTION_1D"
    if g1 and g2 and controls and not g4:
        return "ROTOR_GAP_FAILS_1D"
    return "INCONCLUSIVE"


def main() -> int:
    print("=" * 78)
    print("det16_traceless_rotor_twin_probe -- CHIRAL4D.MIRROR.DET16.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print(
        "q=%s  N=%s  L=%s  t=%s  h_E=%s"
        % (
            CHARGES_TRACELESS,
            GAUGE_ORDERS,
            CLUSTER_COUNTS,
            HOPPING_STRENGTHS,
            ELECTRIC_STRENGTHS,
        )
    )
    print(
        "H_E = h_E * sum_b centered_electric_flux(e_b, N)^2  "
        "(source form; no (2 pi/N)^2)"
    )
    print(
        "DFP window: t<=0.2 (source DFP_SCANNED_HOPPING_STRENGTH=%.2f "
        "is outside the cited theorem window); gap floor %.1f"
        % (DFP_SCANNED_HOPPING_STRENGTH, DFP_GAP_LOWER_BOUND)
    )
    print("=" * 78)

    models: dict[tuple[int, int], GaugeModel] = {}
    u1_models: dict[int, GaugeModel] = {}
    dims: dict[tuple[int, int], int] = {}

    print("\nGAUSS-SECTOR DIMENSIONS  (traceless q; U(1) is Q_tot=0)")
    for cluster_count in CLUSTER_COUNTS:
        u1_models[cluster_count] = build_charged_model(
            U1_LABEL, cluster_count, CHARGES_TRACELESS, wrap=False
        )
        print(
            "  U(1) L=%d : %d"
            % (cluster_count, len(u1_models[cluster_count].allowed_states))
        )
        for gauge_order in GAUGE_ORDERS:
            model = build_charged_model(
                gauge_order, cluster_count, CHARGES_TRACELESS, wrap=True
            )
            models[(gauge_order, cluster_count)] = model
            dims[(gauge_order, cluster_count)] = len(model.allowed_states)
            print(
                "  Z%d L=%d : %d"
                % (gauge_order, cluster_count, dims[(gauge_order, cluster_count)])
            )

    print("\nG1 DET product states in Gauss sector")
    g1_ok = True
    for cluster_count in CLUSTER_COUNTS:
        product_states = det_product_states(cluster_count)
        for gauge_order in GAUGE_ORDERS:
            index = models[(gauge_order, cluster_count)].state_to_index
            missing = [state for state in product_states if state not in index]
            ok = not missing
            g1_ok = g1_ok and ok
            gate(
                "G1 Z%d L=%d DET product in sector" % (gauge_order, cluster_count),
                ok,
                "missing=%s" % (missing if missing else "none"),
            )
        u1_index = u1_models[cluster_count].state_to_index
        missing_u1 = [state for state in product_states if state not in u1_index]
        ok_u1 = not missing_u1
        g1_ok = g1_ok and ok_u1
        gate(
            "G1 U(1) L=%d DET product in sector" % cluster_count,
            ok_u1,
            "missing=%s" % (missing_u1 if missing_u1 else "none"),
        )

    print("\nSCAN Delta(N; t, h_E)  [traceless]")
    grids: dict[tuple[int, int], dict] = {}
    u1_grids: dict[int, dict] = {}
    for cluster_count in CLUSTER_COUNTS:
        u1_grids[cluster_count] = run_model_grid(u1_models[cluster_count])
        for gauge_order in GAUGE_ORDERS:
            grids[(gauge_order, cluster_count)] = run_model_grid(
                models[(gauge_order, cluster_count)]
            )

    print("\nG2 EXACT SATURATION  (N > 4L  =>  Z_N = U(1))")
    g2_ok = True
    for cluster_count in CLUSTER_COUNTS:
        threshold = saturation_order(cluster_count)
        saturated = [order for order in GAUGE_ORDERS if order >= threshold]
        print(
            "  L=%d saturation N>%d -> N in %s"
            % (cluster_count, 4 * cluster_count, saturated)
        )
        for gauge_order in saturated:
            zn = models[(gauge_order, cluster_count)]
            u1 = u1_models[cluster_count]
            states_equal = np.array_equal(zn.allowed_states, u1.allowed_states)
            energy_diff = (
                float(np.max(np.abs(zn.electric_energies - u1.electric_energies)))
                if states_equal
                else float("inf")
            )
            max_gap_diff = 0.0
            for key, u1_point in u1_grids[cluster_count].items():
                zn_point = grids[(gauge_order, cluster_count)][key]
                max_gap_diff = max(max_gap_diff, abs(zn_point.gap - u1_point.gap))
            ok = (
                states_equal
                and energy_diff == 0.0
                and max_gap_diff < SATURATION_TOL
            )
            g2_ok = g2_ok and ok
            gate(
                "G2 Z%d L=%d == U(1)" % (gauge_order, cluster_count),
                ok,
                "states_equal=%s dH_E=%.1e gap_ok_1e-12=%s"
                % (
                    states_equal,
                    energy_diff,
                    max_gap_diff < SATURATION_TOL,
                ),
            )

    print("\nG3 WRAPPING vs U(1)  (N <= 4L)")
    for cluster_count in CLUSTER_COUNTS:
        threshold = saturation_order(cluster_count)
        wrapping = [order for order in GAUGE_ORDERS if order < threshold]
        for gauge_order in wrapping:
            diffs = []
            for key, u1_point in u1_grids[cluster_count].items():
                zn_point = grids[(gauge_order, cluster_count)][key]
                raw = zn_point.gap - u1_point.gap
                diffs.append(0.0 if abs(raw) < SATURATION_TOL else raw)
            abs_diffs = [abs(value) for value in diffs]
            print(
                "  Z%d L=%d vs U(1): max|dDelta|=%.9f  "
                "min dDelta=%.9f  max dDelta=%.9f  dim=%d"
                % (
                    gauge_order,
                    cluster_count,
                    max(abs_diffs),
                    min(diffs),
                    max(diffs),
                    dims[(gauge_order, cluster_count)],
                )
            )

    print("\nU(1) GAP TABLE  (columns t=0,0.05,0.10,0.20,0.40)")
    for cluster_count in CLUSTER_COUNTS:
        for electric_strength in ELECTRIC_STRENGTHS:
            values = [
                u1_grids[cluster_count][(electric_strength, hopping)].gap
                for hopping in HOPPING_STRENGTHS
            ]
            print(
                "  U(1) L=%d hE=%3.1f : %s"
                % (
                    cluster_count,
                    electric_strength,
                    " ".join("%.9f" % value for value in values),
                )
            )

    print("\nG4 U(1) gap >= %.1f on t<=0.2 window" % DFP_GAP_LOWER_BOUND)
    g4_ok = True
    for cluster_count in CLUSTER_COUNTS:
        for electric_strength in ELECTRIC_STRENGTHS:
            for hopping_strength in WINDOW_HOPPING:
                point = u1_grids[cluster_count][
                    (electric_strength, hopping_strength)
                ]
                ok = point.gap + 1.0e-15 >= DFP_GAP_LOWER_BOUND
                g4_ok = g4_ok and ok
                gate(
                    "G4 U(1) L=%d hE=%.1f t=%.2f" % (
                        cluster_count,
                        electric_strength,
                        hopping_strength,
                    ),
                    ok,
                    "Delta=%.9f overlap=%.9f" % (point.gap, point.overlap),
                )

    print("\nG5 must-fail control q=(1,1,1,1) vs source")
    g5_ok = True
    for cluster_count in CLUSTER_COUNTS:
        for gauge_order in (2, 4):
            source_model = source_build_model(gauge_order, cluster_count)
            control_model = build_charged_model(
                gauge_order, cluster_count, CHARGES_UNIFORM, wrap=True
            )
            max_diff = 0.0
            for electric_strength in ELECTRIC_STRENGTHS:
                for hopping_strength in HOPPING_STRENGTHS:
                    source_point = analyze_grid_point(
                        source_model, hopping_strength, electric_strength
                    )
                    control_point = analyze_grid_point(
                        control_model, hopping_strength, electric_strength
                    )
                    max_diff = max(
                        max_diff, abs(source_point.gap - control_point.gap)
                    )
            ok = max_diff < SOURCE_REPRO_TOL
            g5_ok = g5_ok and ok
            gate(
                "G5 q=1111 matches source Z%d L=%d" % (gauge_order, cluster_count),
                ok,
                "max |dDelta|=%.3e" % max_diff,
            )
        keyerror = False
        try:
            build_charged_model(8, cluster_count, CHARGES_UNIFORM, wrap=True)
        except KeyError as error:
            keyerror = True
            detail = "KeyError %s" % (error,)
        else:
            detail = "built without KeyError"
        g5_ok = g5_ok and keyerror
        gate(
            "G5 q=1111 L=%d N=8 KeyError" % cluster_count,
            keyerror,
            detail,
        )

    print("\nG6 must-fail control: DET term removed")
    g6_ok = True
    for cluster_count in CLUSTER_COUNTS:
        splitting, degeneracy, excitation = no_det_splitting(
            u1_models[cluster_count]
        )
        reference = u1_grids[cluster_count][(1.0, NO_DET_HOPPING_STRENGTH)].gap
        ratio = splitting / reference if reference > 0.0 else 0.0
        collapsed = splitting < 0.05 and ratio < 0.05
        g6_ok = g6_ok and collapsed
        gate(
            "G6 U(1) L=%d no-DET collapse" % cluster_count,
            collapsed,
            "t=%.2f hE=1 splitting=%.3e (%.3e of DET gap) deg=%d next=%.9f"
            % (
                NO_DET_HOPPING_STRENGTH,
                splitting,
                ratio,
                degeneracy,
                excitation,
            ),
        )

    controls_ok = g5_ok and g6_ok
    verdict = decide_verdict(g1_ok, g2_ok, g4_ok, controls_ok)
    n_pass = sum(1 for _name, ok in CHECKS if ok)
    print("\nGATES %d/%d" % (n_pass, len(CHECKS)))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("VERDICT: %s" % verdict)
    print("HONEST: %s" % HONEST_NOTE)
    print("=" * 78)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
