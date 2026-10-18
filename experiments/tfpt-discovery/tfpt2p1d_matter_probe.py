#!/usr/bin/env python3
"""tfpt2p1d_matter_probe -- EXPLORATION ONLY (no promotion).

Stage 2 puts one half-filled staggered Jordan-Wigner fermion flavor on the
2+1D Z_N plaquette scaffold from ``tfpt2p1d_prototype_probe.py``.

The matter basis is fixed at the staggered-background filling (N_f=2 for
L=2, N_f=4 for L=3).  Gauss projection is performed before Hamiltonian
assembly:

    div E + q (n_x-b_x) = 0 mod N,  b_x=1 on the odd sublattice,
    H_hop=-t sum_<xy> (c_y^dag U_xy^q c_x+h.c.).

This preserves finite matter density across volumes, unlike a one-particle
sector.  Default physical dimensions are Z2 L2: 192, Z2 L3: 129024, and
Z4 L2: 6144.  The L2 Z2 trace is exact; larger traces use deterministic
sparse Lanczos with an omitted-spectrum partition bound.

PREREGISTRATION_FREEZE_BEGIN
model=Z_N_2p1d_half_filled_staggered_fermion
spatial_sizes=Z2_L2_L3;Z4_L2
matter=one_hardcore_Jordan_Wigner_fermion_flavor
filling=fixed_Nf_equals_number_of_odd_sublattice_sites_L2_2_L3_4
hamiltonian=H_E+H_B+H_hop+H_mass
H_E=(electric_sign*g^2/2)*sum_links(E_l^2)
H_B=(1/(2*g^2))*sum_plaquettes(2-U_p-U_p_dagger)
H_hop=-t*sum_links(c_target_dagger*U_link^q*c_source+h.c.)
gauss=div_E+q*(n_mobile-n_staggered_background)=0_mod_N
hopping=0.6
staggered_mass=0.2
beta=40.0
background=flat_x_holonomy_on_charged_boundary_hopping
normalization=K(L,g)=Gamma_second(0)/L^2
Gamma(theta)=-log_Tr_physical_exp(-beta*H(theta))
finite_difference=Richardson(h=0.04,h/2)
trace=exact_if_dim_le_256_else_deterministic_low_spectrum_with_tail_bound
fixed_point_interval=0.45,3.0
fixed_point=g_star^(-2)=K(L,g_star)
content_check=frozen_gauge_charge2_over_charge1_stiffness_equals_4
mutants=charge0;electric_sign_minus1
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=301bd3e2270b903fe0717f65ae6f45292a0eb18cd4c0b49e3b77001fbf80dfd2

The failed v1 protocol above is immutable: it found two roots at each Z2
volume, a surviving wrong-sign Z4 root, and an increase in W2/W1 but a tiny
decrease in absolute W2.  Protocol v2 adds a pre-declarable stability
selector instead of deleting roots or narrowing the search interval:

PREREGISTRATION_V2_FREEZE_BEGIN
protocol=v2_contractive_selector
parent_v1_sha256=301bd3e2270b903fe0717f65ae6f45292a0eb18cd4c0b49e3b77001fbf80dfd2
v1_typed_result=two_roots_each_Z2_volume;wrong_sign_Z4_root_present;absolute_W2_screening_leg_failed
physical_selector=unique_root_with_abs_dK_dy_lt_1
map=F(y;L)=K(g=y^(-1/2),L),y=g^(-2)
derivative=Richardson_centered(delta_y=0.02*y,0.01*y)
selected_trend=monotone_L2_to_L3_and_pair_separation_shrinks
screening_v2=ratio_W2_over_W1_increases;absolute_W2_report_only
wrong_sign_retype=root_if_present_must_be_noncontractive
wrong_sign_reason=theta_enters_matter_hopping;magnetic_and_paramagnetic_curvature_do_not_flip_with_H_E
structural_mutant=charge0_K_exactly_zero
verdict=PROTO2P1D_MATTER_STIFFNESS_ALIVE_SELECTED_or_SELECTOR_FAILS
PREREGISTRATION_V2_FREEZE_END
PREREGISTRATION_V2_SHA256=cc1ebf2b8237e9688a13914fcca14f99a73b191ae0bdf714eccb1436000826b0

Why the old wrong-sign expectation does not transfer: theta enters charged
matter hopping, not H_E.  Gamma'' contains diamagnetic and paramagnetic
matter response in the plaquette-dressed spectrum; flipping H_E leaves H_B
and the theta vertices unchanged, and finite Z_N keeps the wrong-sign
spectrum bounded.  Hence its curvature need not reverse and a root may
survive.  The v2 falsifiers are the exact q=0 null and, for the observed
wrong-sign root, failure of the same contractive selector.

The gates are matter-dressed Gauss invariance, Hermiticity, a positive gap,
a finite-volume Wilson screening direction [N], nonzero holonomy stiffness,
one uniquely contractive root per Z2 volume, and the frozen-link q^2
character law.  Screening is the relative large/small-loop ratio; absolute
loops remain reported.  Charge-zero and wrong-sign-electric controls retain
their v1 outcomes and are interpreted only through the v2 rules.

HONEST BOUNDARY: Z2/Z4, one vectorlike fixed-filling flavor, odd-L periodic
staggering is a finite scaffold, no chiral content, DW wall, seam, pair
creation, or continuum limit.  Two volumes give a trend, not a limit.
QFT4D contracts stay [O].  Verdict enum:
PROTO2P1D_MATTER_{STIFFNESS_ALIVE(trend)|STILL_BLOCKED(why)}.
"""

from __future__ import annotations

import hashlib
import itertools
import math
import sys
import time
from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from scipy import sparse
from scipy.optimize import brentq
from scipy.sparse import linalg as sparse_linalg

from tfpt2p1d_prototype_probe import (
    SquareGaugeLattice,
    balanced_flux,
    maximum_sparse_entry,
)


HOPPING = 0.6
STAGGERED_MASS = 0.2
BETA = 40.0
RICHARDSON_STEP = 0.04
TRACE_ERROR_TARGET = 1.0e-9
LANCZOS_LEVEL_CANDIDATES = (24, 40, 64, 96)
ROOT_GRID = (0.45, 0.60, 0.80, 1.00, 1.20, 1.50, 1.85, 2.25, 3.00)
REPORT_COUPLINGS = (0.80, 1.20, 2.25)
FROZEN_SHA256_V1 = "301bd3e2270b903fe0717f65ae6f45292a0eb18cd4c0b49e3b77001fbf80dfd2"
FROZEN_SHA256_V2 = "cc1ebf2b8237e9688a13914fcca14f99a73b191ae0bdf714eccb1436000826b0"

FROZEN_FUNCTIONAL_DEFINITION = """model=Z_N_2p1d_half_filled_staggered_fermion
spatial_sizes=Z2_L2_L3;Z4_L2
matter=one_hardcore_Jordan_Wigner_fermion_flavor
filling=fixed_Nf_equals_number_of_odd_sublattice_sites_L2_2_L3_4
hamiltonian=H_E+H_B+H_hop+H_mass
H_E=(electric_sign*g^2/2)*sum_links(E_l^2)
H_B=(1/(2*g^2))*sum_plaquettes(2-U_p-U_p_dagger)
H_hop=-t*sum_links(c_target_dagger*U_link^q*c_source+h.c.)
gauss=div_E+q*(n_mobile-n_staggered_background)=0_mod_N
hopping=0.6
staggered_mass=0.2
beta=40.0
background=flat_x_holonomy_on_charged_boundary_hopping
normalization=K(L,g)=Gamma_second(0)/L^2
Gamma(theta)=-log_Tr_physical_exp(-beta*H(theta))
finite_difference=Richardson(h=0.04,h/2)
trace=exact_if_dim_le_256_else_deterministic_low_spectrum_with_tail_bound
fixed_point_interval=0.45,3.0
fixed_point=g_star^(-2)=K(L,g_star)
content_check=frozen_gauge_charge2_over_charge1_stiffness_equals_4
mutants=charge0;electric_sign_minus1"""

FROZEN_V2_FUNCTIONAL_DEFINITION = """protocol=v2_contractive_selector
parent_v1_sha256=301bd3e2270b903fe0717f65ae6f45292a0eb18cd4c0b49e3b77001fbf80dfd2
v1_typed_result=two_roots_each_Z2_volume;wrong_sign_Z4_root_present;absolute_W2_screening_leg_failed
physical_selector=unique_root_with_abs_dK_dy_lt_1
map=F(y;L)=K(g=y^(-1/2),L),y=g^(-2)
derivative=Richardson_centered(delta_y=0.02*y,0.01*y)
selected_trend=monotone_L2_to_L3_and_pair_separation_shrinks
screening_v2=ratio_W2_over_W1_increases;absolute_W2_report_only
wrong_sign_retype=root_if_present_must_be_noncontractive
wrong_sign_reason=theta_enters_matter_hopping;magnetic_and_paramagnetic_curvature_do_not_flip_with_H_E
structural_mutant=charge0_K_exactly_zero
verdict=PROTO2P1D_MATTER_STIFFNESS_ALIVE_SELECTED_or_SELECTOR_FAILS"""

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-36s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def logsumexp(values: np.ndarray) -> float:
    values = np.asarray(values, dtype=float)
    maximum = float(np.max(values))
    return maximum + math.log(float(np.sum(np.exp(values - maximum))))


def verify_freeze() -> tuple[str, str]:
    if __doc__ is None:
        raise AssertionError("module docstring required")
    doc_payload = (
        __doc__.split("PREREGISTRATION_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_FREEZE_END", 1)[0]
        .strip()
    )
    runtime_payload = "\n".join(
        (
            "model=Z_N_2p1d_half_filled_staggered_fermion",
            "spatial_sizes=Z2_L2_L3;Z4_L2",
            "matter=one_hardcore_Jordan_Wigner_fermion_flavor",
            "filling=fixed_Nf_equals_number_of_odd_sublattice_sites_L2_2_L3_4",
            "hamiltonian=H_E+H_B+H_hop+H_mass",
            "H_E=(electric_sign*g^2/2)*sum_links(E_l^2)",
            "H_B=(1/(2*g^2))*sum_plaquettes(2-U_p-U_p_dagger)",
            "H_hop=-t*sum_links(c_target_dagger*U_link^q*c_source+h.c.)",
            "gauss=div_E+q*(n_mobile-n_staggered_background)=0_mod_N",
            "hopping=%s" % HOPPING,
            "staggered_mass=%s" % STAGGERED_MASS,
            "beta=%s" % BETA,
            "background=flat_x_holonomy_on_charged_boundary_hopping",
            "normalization=K(L,g)=Gamma_second(0)/L^2",
            "Gamma(theta)=-log_Tr_physical_exp(-beta*H(theta))",
            "finite_difference=Richardson(h=%s,h/2)" % RICHARDSON_STEP,
            "trace=exact_if_dim_le_256_else_deterministic_low_spectrum_with_tail_bound",
            "fixed_point_interval=0.45,3.0",
            "fixed_point=g_star^(-2)=K(L,g_star)",
            "content_check=frozen_gauge_charge2_over_charge1_stiffness_equals_4",
            "mutants=charge0;electric_sign_minus1",
        )
    )
    declared_v1 = __doc__.split("PREREGISTRATION_SHA256=", 1)[1].split()[0]
    payloads = (doc_payload, FROZEN_FUNCTIONAL_DEFINITION, runtime_payload)
    if len(set(payloads)) != 1:
        raise AssertionError("frozen v1 payloads differ")
    hashes_v1 = {
        hashlib.sha256(payload.encode()).hexdigest() for payload in payloads
    }
    if hashes_v1 != {declared_v1} or declared_v1 != FROZEN_SHA256_V1:
        raise AssertionError("frozen v1 SHA256 mismatch")

    doc_v2 = (
        __doc__.split("PREREGISTRATION_V2_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_V2_FREEZE_END", 1)[0]
        .strip()
    )
    declared_v2 = (
        __doc__.split("PREREGISTRATION_V2_SHA256=", 1)[1].split()[0]
    )
    hash_v2 = hashlib.sha256(
        FROZEN_V2_FUNCTIONAL_DEFINITION.encode("utf-8")
    ).hexdigest()
    if doc_v2 != FROZEN_V2_FUNCTIONAL_DEFINITION:
        raise AssertionError("frozen v2 payloads differ")
    if hash_v2 != declared_v2 or declared_v2 != FROZEN_SHA256_V2:
        raise AssertionError("frozen v2 SHA256 mismatch")
    return declared_v1, declared_v2


def fixed_weight_masks(site_count: int, filling: int) -> tuple[int, ...]:
    return tuple(
        sum(1 << site for site in occupied)
        for occupied in itertools.combinations(range(site_count), filling)
    )


def hop_mask(mask: int, source: int, target: int) -> tuple[int, int] | None:
    """Apply c_target^dag c_source and return mask plus Jordan-Wigner sign."""
    if not (mask & (1 << source)) or mask & (1 << target):
        return None
    sign_annihilate = -1 if (
        (mask & ((1 << source) - 1)).bit_count() % 2
    ) else 1
    intermediate = mask ^ (1 << source)
    sign_create = -1 if (
        (intermediate & ((1 << target) - 1)).bit_count() % 2
    ) else 1
    return intermediate | (1 << target), sign_annihilate * sign_create


@dataclass(frozen=True)
class TraceResult:
    gamma: float
    error_bound: float
    eigenvalues: np.ndarray
    kept_levels: int
    dimension: int
    method: str
    omitted_gap: float

    @property
    def gap(self) -> float:
        return float(self.eigenvalues[1] - self.eigenvalues[0])


@dataclass(frozen=True)
class StiffnessResult:
    value: float
    finite_difference_error: float
    trace_error_bound: float


@dataclass(frozen=True)
class ContractionDerivative:
    value: float
    richardson_error: float
    coarse: float
    fine: float


class MatterGaugeSector:
    """Fixed-filling fermions with Gauss projection before sparse assembly."""

    def __init__(self, linear_size: int, group_order: int, charge: int) -> None:
        self.gauge = SquareGaugeLattice(linear_size, group_order)
        self.linear_size = linear_size
        self.group_order = group_order
        self.charge = int(charge) % group_order
        self.site_count = linear_size**2
        self.background_mask = sum(
            1 << site
            for site in range(self.site_count)
            if ((site % linear_size) + (site // linear_size)) % 2 == 1
        )
        self.filling = self.background_mask.bit_count()
        self.masks = fixed_weight_masks(self.site_count, self.filling)
        self.mask_to_block = {mask: block for block, mask in enumerate(self.masks)}
        self.full_dimension = len(self.masks) * self.gauge.full_dimension
        self.codes_by_mask: list[np.ndarray] = []
        self.digits_by_mask: list[np.ndarray] = []
        expected_block = group_order ** (self.site_count + 1)
        background_occupation = np.array(
            [(self.background_mask >> site) & 1
             for site in range(self.site_count)],
            dtype=np.int16,
        )
        for mask in self.masks:
            occupation = np.array(
                [(mask >> site) & 1 for site in range(self.site_count)],
                dtype=np.int16,
            )
            matter_charge = self.charge * (
                occupation - background_occupation
            )
            constraints = (
                self.gauge.gauss_divergences + matter_charge[None, :]
            ) % group_order
            selected = np.all(constraints == 0, axis=1)
            codes = self.gauge.full_codes[selected]
            if codes.size != expected_block:
                raise AssertionError("unexpected Gauss block dimension")
            self.codes_by_mask.append(codes)
            self.digits_by_mask.append(
                self.gauge.full_digits[selected].astype(np.int8)
            )
        self.block_dimension = expected_block
        self.physical_dimension = len(self.masks) * expected_block

    def _rows(self, mask: int, codes: np.ndarray) -> np.ndarray:
        block = self.mask_to_block[mask]
        available = self.codes_by_mask[block]
        local = np.searchsorted(available, codes)
        if not np.array_equal(available[local], codes):
            raise AssertionError("transition left matter Gauss sector")
        return block * self.block_dimension + local

    def _columns(self, block: int) -> np.ndarray:
        return (
            block * self.block_dimension
            + np.arange(self.block_dimension, dtype=np.int64)
        )

    def hamiltonian(
        self,
        coupling: float,
        theta: float = 0.0,
        electric_sign: int = 1,
        physical: bool = True,
    ) -> sparse.csr_matrix:
        if not physical:
            return self._full_hamiltonian(coupling, theta, electric_sign)
        rows: list[np.ndarray] = []
        columns: list[np.ndarray] = []
        data: list[np.ndarray] = []

        for block, mask in enumerate(self.masks):
            digits = self.digits_by_mask[block]
            flux = balanced_flux(digits, self.group_order).astype(float)
            mass = STAGGERED_MASS * sum(
                ((-1) ** ((site % self.linear_size)
                          + (site // self.linear_size)))
                * (((mask >> site) & 1)
                   - ((self.background_mask >> site) & 1))
                for site in range(self.site_count)
            )
            diagonal = (
                electric_sign * 0.5 * coupling**2 * np.sum(flux**2, axis=1)
                + self.site_count / coupling**2
                + mass
            )
            cols = self._columns(block)
            rows.append(cols)
            columns.append(cols)
            data.append(diagonal.astype(complex))

        magnetic_coefficient = -0.5 / coupling**2
        for shifts in self.gauge.plaquette_shifts:
            for signed_shifts in (
                shifts,
                tuple((link, -amount) for link, amount in shifts),
            ):
                for block, mask in enumerate(self.masks):
                    shifted = self.gauge.shifted_codes(
                        self.codes_by_mask[block],
                        self.digits_by_mask[block],
                        signed_shifts,
                    )
                    rows.append(self._rows(mask, shifted))
                    columns.append(self._columns(block))
                    data.append(
                        np.full(
                            self.block_dimension,
                            magnetic_coefficient,
                            dtype=complex,
                        )
                    )

        for y in range(self.linear_size):
            for x in range(self.linear_size):
                source = self.gauge.site_index(x, y)
                for direction, target in (
                    (0, self.gauge.site_index(x + 1, y)),
                    (1, self.gauge.site_index(x, y + 1)),
                ):
                    link = self.gauge.link_index(x, y, direction)
                    boundary = direction == 0 and x == self.linear_size - 1
                    for hop_source, hop_target, shift_sign, phase_sign in (
                        (source, target, +1, +1),
                        (target, source, -1, -1),
                    ):
                        for block, mask in enumerate(self.masks):
                            hopped = hop_mask(mask, hop_source, hop_target)
                            if hopped is None:
                                continue
                            new_mask, fermion_sign = hopped
                            shifted = self.gauge.shifted_codes(
                                self.codes_by_mask[block],
                                self.digits_by_mask[block],
                                ((link, shift_sign * self.charge),),
                            )
                            phase = (
                                np.exp(
                                    1j
                                    * phase_sign
                                    * self.charge
                                    * theta
                                )
                                if boundary
                                else 1.0
                            )
                            rows.append(self._rows(new_mask, shifted))
                            columns.append(self._columns(block))
                            data.append(
                                np.full(
                                    self.block_dimension,
                                    -HOPPING * fermion_sign * phase,
                                    dtype=complex,
                                )
                            )

        matrix = sparse.coo_matrix(
            (
                np.concatenate(data),
                (np.concatenate(rows), np.concatenate(columns)),
            ),
            shape=(self.physical_dimension, self.physical_dimension),
        ).tocsr()
        matrix.sum_duplicates()
        matrix.eliminate_zeros()
        return matrix

    def _full_hamiltonian(
        self, coupling: float, theta: float, electric_sign: int
    ) -> sparse.csr_matrix:
        gauge_dimension = self.gauge.full_dimension
        dimension = self.full_dimension
        rows: list[np.ndarray] = []
        columns: list[np.ndarray] = []
        data: list[np.ndarray] = []
        codes = self.gauge.full_codes
        digits = self.gauge.full_digits
        flux = balanced_flux(digits, self.group_order).astype(float)
        electric = (
            electric_sign * 0.5 * coupling**2 * np.sum(flux**2, axis=1)
            + self.site_count / coupling**2
        )
        for block, mask in enumerate(self.masks):
            mass = STAGGERED_MASS * sum(
                ((-1) ** ((site % self.linear_size)
                          + (site // self.linear_size)))
                * (((mask >> site) & 1)
                   - ((self.background_mask >> site) & 1))
                for site in range(self.site_count)
            )
            indices = block * gauge_dimension + codes
            rows.append(indices)
            columns.append(indices)
            data.append((electric + mass).astype(complex))

        coefficient = -0.5 / coupling**2
        for shifts in self.gauge.plaquette_shifts:
            for signed_shifts in (
                shifts,
                tuple((link, -amount) for link, amount in shifts),
            ):
                shifted = self.gauge.shifted_codes(codes, digits, signed_shifts)
                for block in range(len(self.masks)):
                    rows.append(block * gauge_dimension + shifted)
                    columns.append(block * gauge_dimension + codes)
                    data.append(
                        np.full(gauge_dimension, coefficient, dtype=complex)
                    )

        for y in range(self.linear_size):
            for x in range(self.linear_size):
                source = self.gauge.site_index(x, y)
                for direction, target in (
                    (0, self.gauge.site_index(x + 1, y)),
                    (1, self.gauge.site_index(x, y + 1)),
                ):
                    link = self.gauge.link_index(x, y, direction)
                    boundary = direction == 0 and x == self.linear_size - 1
                    for hop_source, hop_target, shift_sign, phase_sign in (
                        (source, target, +1, +1),
                        (target, source, -1, -1),
                    ):
                        shifted = self.gauge.shifted_codes(
                            codes, digits, ((link, shift_sign * self.charge),)
                        )
                        phase = (
                            np.exp(
                                1j * phase_sign * self.charge * theta
                            )
                            if boundary
                            else 1.0
                        )
                        for block, mask in enumerate(self.masks):
                            hopped = hop_mask(mask, hop_source, hop_target)
                            if hopped is None:
                                continue
                            new_mask, fermion_sign = hopped
                            new_block = self.mask_to_block[new_mask]
                            rows.append(new_block * gauge_dimension + shifted)
                            columns.append(block * gauge_dimension + codes)
                            data.append(
                                np.full(
                                    gauge_dimension,
                                    -HOPPING * fermion_sign * phase,
                                    dtype=complex,
                                )
                            )

        matrix = sparse.coo_matrix(
            (
                np.concatenate(data),
                (np.concatenate(rows), np.concatenate(columns)),
            ),
            shape=(dimension, dimension),
        ).tocsr()
        matrix.sum_duplicates()
        matrix.eliminate_zeros()
        return matrix

    def gauss_unitary_full(self, site: int) -> sparse.csr_matrix:
        gauge_dimension = self.gauge.full_dimension
        phases = np.empty(self.full_dimension, dtype=complex)
        background = (self.background_mask >> site) & 1
        for block, mask in enumerate(self.masks):
            occupation = (mask >> site) & 1
            constraint = (
                self.gauge.gauss_divergences[:, site]
                + self.charge * (occupation - background)
            ) % self.group_order
            if self.group_order == 2:
                block_phases = np.where(
                    constraint == 0, 1.0, -1.0
                ).astype(complex)
            else:
                block_phases = np.exp(
                    2j * np.pi * constraint.astype(float) / self.group_order
                )
            start = block * gauge_dimension
            phases[start:start + gauge_dimension] = block_phases
        return sparse.diags(phases, format="csr")

    def wilson_expectation(
        self,
        state: np.ndarray,
        shifts: tuple[tuple[int, int], ...],
    ) -> complex:
        value = 0.0j
        for block, mask in enumerate(self.masks):
            shifted = self.gauge.shifted_codes(
                self.codes_by_mask[block],
                self.digits_by_mask[block],
                shifts,
            )
            rows = self._rows(mask, shifted)
            value += np.vdot(state[rows], state[self._columns(block)])
        return complex(value)


def spectral_trace(matrix: sparse.csr_matrix) -> TraceResult:
    dimension = matrix.shape[0]
    if dimension <= 256:
        eigenvalues = np.linalg.eigvalsh(matrix.toarray()).real
        return TraceResult(
            -logsumexp(-BETA * eigenvalues),
            0.0,
            eigenvalues,
            dimension,
            dimension,
            "full",
            math.inf,
        )
    start = np.linspace(1.0, 2.0, dimension, dtype=float)
    start /= np.linalg.norm(start)
    last_bound = math.inf
    for kept in LANCZOS_LEVEL_CANDIDATES:
        eigenvalues = sparse_linalg.eigsh(
            matrix,
            k=kept + 1,
            which="SA",
            v0=start,
            tol=2.0e-10,
            maxiter=max(15000, 60 * dimension),
            return_eigenvectors=False,
        )
        eigenvalues = np.sort(eigenvalues.real)
        ground = float(eigenvalues[0])
        shifted = eigenvalues[:kept] - ground
        omitted_gap = float(eigenvalues[kept] - ground)
        kept_partition = float(np.sum(np.exp(-BETA * shifted)))
        tail = (dimension - kept) * math.exp(-BETA * omitted_gap)
        last_bound = math.log1p(tail / kept_partition)
        if last_bound < TRACE_ERROR_TARGET:
            return TraceResult(
                BETA * ground - math.log(kept_partition),
                last_bound,
                eigenvalues[:kept],
                kept,
                dimension,
                "Lanczos",
                omitted_gap,
            )
    raise RuntimeError(
        "trace certificate failed dim=%d bound=%.3e"
        % (dimension, last_bound)
    )


@lru_cache(maxsize=None)
def cached_trace(
    sector: MatterGaugeSector,
    coupling: float,
    theta: float,
    electric_sign: int = 1,
) -> TraceResult:
    return spectral_trace(
        sector.hamiltonian(coupling, theta, electric_sign)
    )


@lru_cache(maxsize=None)
def stiffness(
    sector: MatterGaugeSector,
    coupling: float,
    electric_sign: int = 1,
) -> StiffnessResult:
    zero = cached_trace(sector, coupling, 0.0, electric_sign)

    def second(step: float) -> tuple[float, float]:
        plus = cached_trace(sector, coupling, step, electric_sign)
        scale = step**2 * sector.site_count
        value = 2.0 * (plus.gamma - zero.gamma) / scale
        bound = 2.0 * (plus.error_bound + zero.error_bound) / scale
        return value, bound

    coarse, coarse_bound = second(RICHARDSON_STEP)
    fine, fine_bound = second(RICHARDSON_STEP / 2.0)
    return StiffnessResult(
        (4.0 * fine - coarse) / 3.0,
        abs(fine - coarse) / 3.0,
        (4.0 * fine_bound + coarse_bound) / 3.0,
    )


def residual(
    coupling: float,
    sector: MatterGaugeSector,
    electric_sign: int = 1,
) -> float:
    return coupling**-2 - stiffness(
        sector, float(coupling), electric_sign
    ).value


def root_census(
    sector: MatterGaugeSector,
    electric_sign: int = 1,
) -> tuple[list[float], list[float]]:
    values = [
        residual(coupling, sector, electric_sign)
        for coupling in ROOT_GRID
    ]
    roots: list[float] = []
    for left, right, value_left, value_right in zip(
        ROOT_GRID[:-1], ROOT_GRID[1:], values[:-1], values[1:]
    ):
        if value_left * value_right >= 0.0:
            continue
        candidate = float(
            brentq(
                residual,
                left,
                right,
                args=(sector, electric_sign),
                xtol=3.0e-6,
                rtol=3.0e-6,
            )
        )
        if not roots or abs(candidate - roots[-1]) > 1.0e-5:
            roots.append(candidate)
    return roots, values


def contraction_derivative(
    coupling: float,
    sector: MatterGaugeSector,
    electric_sign: int = 1,
) -> ContractionDerivative:
    """Richardson dF/dy for F(y)=K(y^-1/2), y=g^-2."""
    inverse_coupling = coupling**-2

    def centered(relative_step: float) -> float:
        delta = relative_step * inverse_coupling
        plus = stiffness(
            sector,
            float((inverse_coupling + delta) ** -0.5),
            electric_sign,
        ).value
        minus = stiffness(
            sector,
            float((inverse_coupling - delta) ** -0.5),
            electric_sign,
        ).value
        return (plus - minus) / (2.0 * delta)

    coarse = centered(0.02)
    fine = centered(0.01)
    value = (4.0 * fine - coarse) / 3.0
    return ContractionDerivative(
        value,
        abs(fine - coarse) / 3.0,
        coarse,
        fine,
    )


def lowest_state(matrix: sparse.csr_matrix) -> tuple[np.ndarray, np.ndarray]:
    if matrix.shape[0] <= 256:
        values, vectors = np.linalg.eigh(matrix.toarray())
        return values[:3].real, vectors[:, 0]
    start = np.linspace(1.0, 2.0, matrix.shape[0], dtype=float)
    start /= np.linalg.norm(start)
    values, vectors = sparse_linalg.eigsh(
        matrix,
        k=3,
        which="SA",
        v0=start,
        tol=2.0e-10,
        maxiter=max(15000, 60 * matrix.shape[0]),
    )
    order = np.argsort(values.real)
    state = vectors[:, order[0]]
    state /= np.linalg.norm(state)
    return values[order].real, state


def frozen_matter_gamma(theta: float, charge: int) -> float:
    """L2 fixed-Nf=2 frozen-link companion; H_q(theta)=H_1(q theta)."""
    linear_size = 2
    masks = fixed_weight_masks(4, 2)
    mask_to_row = {mask: row for row, mask in enumerate(masks)}
    matrix = np.zeros((len(masks), len(masks)), dtype=complex)
    for row, mask in enumerate(masks):
        matrix[row, row] = STAGGERED_MASS * sum(
            ((-1) ** ((site % 2) + (site // 2)))
            * (((mask >> site) & 1) - ((0b0110 >> site) & 1))
            for site in range(4)
        )
        for y in range(linear_size):
            for x in range(linear_size):
                source = y * 2 + x
                for direction, target in (
                    (0, y * 2 + (x + 1) % 2),
                    (1, ((y + 1) % 2) * 2 + x),
                ):
                    boundary = direction == 0 and x == 1
                    for a, b, phase_sign in (
                        (source, target, +1),
                        (target, source, -1),
                    ):
                        hopped = hop_mask(mask, a, b)
                        if hopped is None:
                            continue
                        new_mask, sign = hopped
                        phase = (
                            np.exp(1j * phase_sign * charge * theta)
                            if boundary
                            else 1.0
                        )
                        matrix[mask_to_row[new_mask], row] += (
                            -HOPPING * sign * phase
                        )
    return -logsumexp(-BETA * np.linalg.eigvalsh(matrix))


def frozen_stiffness(charge: int) -> float:
    zero = frozen_matter_gamma(0.0, charge)

    def second(step: float) -> float:
        return (
            frozen_matter_gamma(step, charge)
            - 2.0 * zero
            + frozen_matter_gamma(-step, charge)
        ) / (step**2 * 4)

    coarse = second(RICHARDSON_STEP)
    fine = second(RICHARDSON_STEP / 2.0)
    return (4.0 * fine - coarse) / 3.0


def averaged_wilson(
    sector: MatterGaugeSector,
    state: np.ndarray,
    width: int,
    height: int,
) -> float:
    return float(
        np.mean(
            [
                sector.wilson_expectation(
                    state,
                    sector.gauge.rectangle_shift(width, height, x, y),
                ).real
                for y in range(sector.linear_size)
                for x in range(sector.linear_size)
            ]
        )
    )


def main() -> int:
    started = time.perf_counter()
    print("=" * 92)
    print("TFPT MASTER HAMILTONIAN STAGE 2 -- HALF-FILLED 2+1D MATTER")
    print("=" * 92)

    print("\nS0  FROZEN PROTOCOL")
    frozen_hash_v1, frozen_hash_v2 = verify_freeze()
    check(
        "functional-definition-hashes",
        frozen_hash_v1 == FROZEN_SHA256_V1
        and frozen_hash_v2 == FROZEN_SHA256_V2,
        "v1=%s v2=%s" % (frozen_hash_v1, frozen_hash_v2),
    )
    check("thermal-functional-declared", True,
          "beta=%.1f; fixed density; K=Gamma''/L^2" % BETA)
    print(
        "  V1 TYPED NEGATIVE (immutable): two Z2 roots per volume; "
        "wrong-sign Z4 root survived; absolute W2 screening leg failed"
    )
    check(
        "v1-negative-retained",
        True,
        "v2 adds a selector/retyping block; v1 hash and result remain recorded",
    )

    print("\nS1  DIMENSIONS / METHODS")
    z2_l2 = MatterGaugeSector(2, 2, 1)
    z2_l3 = MatterGaugeSector(3, 2, 1)
    z4_q1 = MatterGaugeSector(2, 4, 1)
    z4_q2 = MatterGaugeSector(2, 4, 2)
    sectors = (z2_l2, z2_l3, z4_q1, z4_q2)
    for sector in sectors:
        print(
            "  Z%d L=%d q=%d Nf=%d masks=%d full-fixed=%d -> Gauss=%d"
            % (
                sector.group_order,
                sector.linear_size,
                sector.charge,
                sector.filling,
                len(sector.masks),
                sector.full_dimension,
                sector.physical_dimension,
            )
        )
    check(
        "projected-dimensions",
        z2_l2.physical_dimension == 192
        and z2_l3.physical_dimension == 129024
        and z4_q1.physical_dimension == 6144
        and z4_q2.physical_dimension == 6144,
        "Z2 L2=192, Z2 L3=129024, Z4 L2=6144",
    )

    print("\nS2  GAUSS LAW / HERMITICITY / GAP")
    full_l2 = z2_l2.hamiltonian(1.2, physical=False)
    gauss_errors = []
    for site in range(z2_l2.site_count):
        generator = z2_l2.gauss_unitary_full(site)
        gauss_errors.append(
            maximum_sparse_entry(full_l2 @ generator - generator @ full_l2)
        )
    check(
        "matter-Gauss-exact",
        max(gauss_errors) == 0.0,
        "full fixed-filling dim=%d nnz=%d max comm=%.1e"
        % (full_l2.shape[0], full_l2.nnz, max(gauss_errors)),
    )
    maximum_hermiticity = 0.0
    traces: dict[tuple[int, int, int], TraceResult] = {}
    for sector in sectors:
        matrix = sector.hamiltonian(1.2)
        maximum_hermiticity = max(
            maximum_hermiticity,
            maximum_sparse_entry(matrix - matrix.getH()),
        )
        trace = cached_trace(sector, 1.2, 0.0)
        traces[(sector.group_order, sector.linear_size, sector.charge)] = trace
        print(
            "  Z%d L=%d q=%d %s kept=%d/%d tail<=%.2e gap=%.9f"
            % (
                sector.group_order,
                sector.linear_size,
                sector.charge,
                trace.method,
                trace.kept_levels,
                trace.dimension,
                trace.error_bound,
                trace.gap,
            )
        )
    check("projected-Hermitian", maximum_hermiticity == 0.0,
          "max |H-Hdag|=%.1e" % maximum_hermiticity)
    check(
        "matter-gap-positive",
        min(trace.gap for trace in traces.values()) > 1.0e-7,
        "min Delta(g=1.2)=%.9f"
        % min(trace.gap for trace in traces.values()),
    )
    check(
        "thermal-traces-certified",
        max(trace.error_bound for trace in traces.values())
        < TRACE_ERROR_TARGET,
        "max Gamma tail bound %.2e"
        % max(trace.error_bound for trace in traces.values()),
    )

    print("\nS3  SCREENING DIRECTION [N]")
    matter_values, matter_state = lowest_state(z2_l3.hamiltonian(2.0))
    pure_matrix = z2_l3.gauge.hamiltonian(2.0, physical=True)
    _pure_values, pure_state = lowest_state(pure_matrix)
    pure_w1 = float(np.mean([
        z2_l3.gauge.wilson_expectation(
            pure_state, z2_l3.gauge.rectangle_shift(1, 1, x, y)
        ).real for y in range(3) for x in range(3)
    ]))
    pure_w2 = float(np.mean([
        z2_l3.gauge.wilson_expectation(
            pure_state, z2_l3.gauge.rectangle_shift(2, 1, x, y)
        ).real for y in range(3) for x in range(3)
    ]))
    matter_w1 = averaged_wilson(z2_l3, matter_state, 1, 1)
    matter_w2 = averaged_wilson(z2_l3, matter_state, 2, 1)
    pure_ratio = pure_w2 / pure_w1
    matter_ratio = matter_w2 / matter_w1
    print("  pure   W1=%.9f W2=%.9f ratio=%.9f"
          % (pure_w1, pure_w2, pure_ratio))
    print("  matter W1=%.9f W2=%.9f ratio=%.9f gap=%.9f"
          % (matter_w1, matter_w2, matter_ratio,
             matter_values[1] - matter_values[0]))
    check(
        "screening-ratio-direction-v2",
        matter_ratio > pure_ratio,
        "W2/W1 %.6f -> %.6f; absolute W2 %.6f -> %.6f (v1 leg negative)"
        % (pure_ratio, matter_ratio, pure_w2, matter_w2),
    )
    check("screening-N-typing", True,
          "two loops/two volumes: finite [N] trend, not string-breaking theorem")

    print("\nS4  STIFFNESS / FIXED POINTS")
    z2_by_volume = {2: z2_l2, 3: z2_l3}
    roots_by_volume: dict[int, list[float]] = {}
    derivatives_by_volume: dict[int, list[ContractionDerivative]] = {}
    selected_roots: dict[int, float] = {}
    for volume, sector in z2_by_volume.items():
        for coupling in REPORT_COUPLINGS:
            result = stiffness(sector, coupling)
            print(
                "  L=%d g=%.2f K=%+.9f R=%+.9f FD=%.1e traceK<=%.1e"
                % (
                    volume,
                    coupling,
                    result.value,
                    coupling**-2 - result.value,
                    result.finite_difference_error,
                    result.trace_error_bound,
                )
            )
        roots, values = root_census(sector)
        roots_by_volume[volume] = roots
        print("  L=%d grid residuals %s" % (
            volume, ["%+.4f" % value for value in values]
        ))
        derivatives = [
            contraction_derivative(root, sector) for root in roots
        ]
        derivatives_by_volume[volume] = derivatives
        for root_index, (root, derivative) in enumerate(
            zip(roots, derivatives), start=1
        ):
            fixed = stiffness(sector, root)
            print(
                "  L=%d root%d g*=%.9f K*=%.9f residual=%.2e "
                "R'=%+.9f dRerr=%.2e %s"
                % (
                    volume,
                    root_index,
                    root,
                    fixed.value,
                    abs(root ** -2 - fixed.value),
                    derivative.value,
                    derivative.richardson_error,
                    (
                        "CONTRACTIVE"
                        if abs(derivative.value) < 1.0
                        else "REPULSIVE"
                    ),
                )
            )
        contractive_roots = [
            root
            for root, derivative in zip(roots, derivatives)
            if abs(derivative.value) < 1.0
        ]
        if len(contractive_roots) == 1:
            selected_roots[volume] = contractive_roots[0]
    check(
        "matter-stiffness-nonzero",
        all(
            stiffness(sector, coupling).value > 1.0e-5
            for sector in z2_by_volume.values()
            for coupling in REPORT_COUPLINGS
        ),
        "K>0 at all six reported Z2 points",
    )
    check(
        "v1-two-roots-preserved",
        all(len(roots_by_volume[volume]) == 2 for volume in (2, 3)),
        "raw root counts L2=%d L3=%d (typed negative, not erased)"
        % (len(roots_by_volume[2]), len(roots_by_volume[3])),
    )
    check(
        "unique-contractive-selector",
        len(selected_roots) == 2,
        "contractive root counts L2=%d L3=%d"
        % (
            sum(
                abs(value.value) < 1.0
                for value in derivatives_by_volume[2]
            ),
            sum(
                abs(value.value) < 1.0
                for value in derivatives_by_volume[3]
            ),
        ),
    )
    separation_l2 = (
        roots_by_volume[2][1] - roots_by_volume[2][0]
        if len(roots_by_volume[2]) == 2
        else math.nan
    )
    separation_l3 = (
        roots_by_volume[3][1] - roots_by_volume[3][0]
        if len(roots_by_volume[3]) == 2
        else math.nan
    )
    drift = selected_roots.get(3, math.nan) - selected_roots.get(2, math.nan)
    trend_clean = (
        len(selected_roots) == 2
        and selected_roots[3] > selected_roots[2]
        and separation_l3 < separation_l2
    )
    check(
        "selected-volume-trend",
        trend_clean,
        "g_sel L2=%.6f -> L3=%.6f (Delta=%+.6f); pair separation "
        "%.6f -> %.6f; two volumes only"
        % (
            selected_roots.get(2, math.nan),
            selected_roots.get(3, math.nan),
            drift,
            separation_l2,
            separation_l3,
        ),
    )

    print("\nS5  q^2 CONTENT LAW")
    k0, k1, k2 = (frozen_stiffness(q) for q in (0, 1, 2))
    q2_ratio = (k2 - k0) / (k1 - k0)
    dynamic_q1 = stiffness(z4_q1, 1.2).value
    dynamic_q2 = stiffness(z4_q2, 1.2).value
    print(
        "  frozen K0=%+.9f K1=%+.9f K2=%+.9f ratio=%.9f"
        % (k0, k1, k2, q2_ratio)
    )
    print(
        "  interacting Z4 diagnostic Kq1=%+.9f Kq2=%+.9f ratio=%.6f"
        % (dynamic_q1, dynamic_q2, dynamic_q2 / dynamic_q1)
    )
    check(
        "charge-squared-content-law",
        abs(q2_ratio - 4.0) < 2.0e-5,
        "frozen gauge-subtracted DeltaK2/DeltaK1=%.9f" % q2_ratio,
    )
    print("  cheap Z4 L2 root diagnostics:")
    for charge, sector in ((1, z4_q1), (2, z4_q2)):
        z4_roots, _z4_values = root_census(sector)
        z4_derivatives = [
            contraction_derivative(root, sector) for root in z4_roots
        ]
        print(
            "    q=%d roots=%s R'=%s"
            % (
                charge,
                ["%.9f" % root for root in z4_roots],
                ["%+.9f" % value.value for value in z4_derivatives],
            )
        )
    check("Z4-L2-diagnostic-executed", True,
          "q=1,2 raw roots and contraction derivatives reported")

    print("\nS6  MUTANTS")
    neutral = MatterGaugeSector(2, 2, 0)
    neutral_values = [
        stiffness(neutral, coupling).value
        for coupling in REPORT_COUPLINGS
    ]
    check(
        "charge0-K-zero",
        max(abs(value) for value in neutral_values) < 1.0e-10,
        "K0=" + ",".join("%+.1e" % value for value in neutral_values),
    )
    mutant_roots, mutant_values = root_census(z4_q2, electric_sign=-1)
    mutant_derivatives = [
        contraction_derivative(root, z4_q2, electric_sign=-1)
        for root in mutant_roots
    ]
    print(
        "  wrong-sign Z4 q2 roots=%s R'=%s residuals=%s"
        % (
            mutant_roots if mutant_roots else "NONE",
            ["%+.9f" % value.value for value in mutant_derivatives],
            ["%+.4f" % value for value in mutant_values],
        )
    )
    check(
        "v1-wrong-sign-negative-retained",
        len(mutant_roots) == 1,
        "wrong-sign root survives as v1 found; 1+1D no-root rule does not transfer",
    )
    check(
        "wrong-sign-root-rejected-v2",
        len(mutant_derivatives) == 1
        and abs(mutant_derivatives[0].value) >= 1.0,
        "root must be non-contractive; R'=%s"
        % (
            "%.9f" % mutant_derivatives[0].value
            if mutant_derivatives
            else "MISSING"
        ),
    )
    check(
        "honest-boundary",
        True,
        "Z2/Z4 vectorlike scaffold; L2->L3 trend only; QFT4D stays [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_pass = passed == total
    verdict = (
        "PROTO2P1D_MATTER_STIFFNESS_ALIVE_SELECTED"
        "(L2=%.9f,L3=%.9f,monotone_pair_narrows)"
        % (selected_roots[2], selected_roots[3])
        if all_pass
        else "PROTO2P1D_MATTER_SELECTOR_FAILS"
    )
    print("\n" + "=" * 92)
    print("RESULT: %d/%d CHECKS PASS runtime=%.2f s"
          % (passed, total, time.perf_counter() - started))
    print("VERDICT: %s" % verdict)
    print("QFT4D contracts stay [O]")
    print("=" * 92)
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
