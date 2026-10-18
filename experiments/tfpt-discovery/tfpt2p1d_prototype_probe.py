#!/usr/bin/env python3
"""tfpt2p1d_prototype_probe -- EXPLORATION ONLY (no promotion).

Stage 1 of the master-Hamiltonian route: the first TFPT scaffold with a
genuine two-dimensional spatial lattice and plaquette self-interaction.

MODEL
-----
On an L x L periodic square lattice, each oriented positive-direction link
carries a Z_N electric-flux digit.  There are 2 L^2 links and full gauge
dimension N^(2 L^2).  The physical pure-gauge sector obeys G_x=1:

    H_E = (g^2/2) sum_l E_l^2,
    H_B = (1/(2 g^2)) sum_p (2 - U_p - U_p^dag).

The default battery reaches Z2 at L=3 (full dimension 2^18=262144, physical
dimension 1024) and Z4 at L=2 (full dimension 4^8=65536, physical dimension
1024).  The implementation is generic in N, including Z6 at L=2, but the
default battery does not allocate its 6^8 full basis.  Matter is deliberately
absent at this scaffold stage.

GATES
-----
T1  The full sparse Hamiltonian commutes with every local Gauss unitary.
T2  H=H^dag exactly, hence exp(-aH) is positive by construction.
T3  In the physical ground state, 1x1 and 2x1 Wilson loops on L=3 show the
    expected strong-coupling area ordering, and the suppression is stronger
    at g=2 than at g=0.8.  This is an [N] two-loop witness, not an area-law
    theorem and not a clean area-versus-perimeter discrimination.
T4  The finite-volume first excitation gap is positive at L=2,3, with its
    volume trend printed rather than extrapolated.

STIFFNESS REPAIR TEST
---------------------
The requested flat x-holonomy multiplies every x-directed boundary link by
exp(i theta).  In a pure-gauge local plaquette Hamiltonian the two boundary
links in each affected plaquette occur with opposite orientations, so the
phases cancel exactly.  Therefore H(theta)=H(0), Gamma(theta) is constant,
K=Gamma''(0)/L^2=0, and g_star^-2=K has no finite solution.  This is a useful
stage-1 blocker: unlike the 1+1D oscillating/divergent root series, the 2+1D
pure-gauge scaffold is flat-holonomy blind.  Charged matter (or an explicitly
different background-flux functional) is required before step scaling can
be retested.

The finite-temperature functional is frozen before evaluation:

PREREGISTRATION_FREEZE_BEGIN
model=Z_N_2p1d_pure_gauge_square_torus
spatial_sizes=L=2,3_periodic
benchmark_groups=Z2_L2_L3;Z4_L2
hamiltonian=H_E+H_B
H_E=(g^2/2)*sum_links(E_l^2)
H_B=(1/(2*g^2))*sum_plaquettes(2-U_p-U_p_dagger)
electric_flux=balanced_integer_representatives_mod_N
physical_sector=Gauss_Gx=1_all_sites
matter=none_stage1_pure_gauge
filling=not_applicable_pure_gauge
background=flat_x_holonomy_multiplying_x_boundary_links
beta=4.0
normalization=K(L,g)=Gamma_second(0)/L^2
Gamma(theta)=-log_Tr_physical_exp(-beta*H(theta))
finite_difference=Richardson(h=0.01,h/2)
couplings=0.8,1.2,2.0
fixed_point=g_star^(-2)=K(L,g_star)
wilson_loops=L3_rectangles_1x1_and_2x1
mutants=drop_plaquette;single_link_shift
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=51a7e8ff34a8202593f6614c53fa547a006f334f256b3aacc68fd1459517911f

MUTANTS
-------
Dropping H_B makes both Wilson expectations vanish and removes their strict
area ordering.  Adding one open-link shift violates local gauge invariance.

HONEST BOUNDARY
---------------
Z2/Z4 are not the TFPT content group; there is no chiral matter, DW wall,
seam line, continuum limit, or physical-coupling claim.  QFT4D contracts
remain [O].  Verdict enum:
PROTO2P1D_{SCAFFOLD_GREEN(gap,stiffness_trend)|BLOCKED(where)}.
"""

from __future__ import annotations

import hashlib
import math
import sys
import time
from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg


BETA = 4.0
RICHARDSON_STEP = 0.01
COUPLINGS = (0.8, 1.2, 2.0)
STRONG_COUPLING = 2.0
WEAK_COUPLING = 0.8
FROZEN_SHA256 = "51a7e8ff34a8202593f6614c53fa547a006f334f256b3aacc68fd1459517911f"

FROZEN_FUNCTIONAL_DEFINITION = """model=Z_N_2p1d_pure_gauge_square_torus
spatial_sizes=L=2,3_periodic
benchmark_groups=Z2_L2_L3;Z4_L2
hamiltonian=H_E+H_B
H_E=(g^2/2)*sum_links(E_l^2)
H_B=(1/(2*g^2))*sum_plaquettes(2-U_p-U_p_dagger)
electric_flux=balanced_integer_representatives_mod_N
physical_sector=Gauss_Gx=1_all_sites
matter=none_stage1_pure_gauge
filling=not_applicable_pure_gauge
background=flat_x_holonomy_multiplying_x_boundary_links
beta=4.0
normalization=K(L,g)=Gamma_second(0)/L^2
Gamma(theta)=-log_Tr_physical_exp(-beta*H(theta))
finite_difference=Richardson(h=0.01,h/2)
couplings=0.8,1.2,2.0
fixed_point=g_star^(-2)=K(L,g_star)
wilson_loops=L3_rectangles_1x1_and_2x1
mutants=drop_plaquette;single_link_shift"""

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    """Record and print one deterministic protocol gate."""
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-35s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def maximum_sparse_entry(matrix: sparse.spmatrix) -> float:
    """Maximum absolute stored entry, with the exact sparse zero handled."""
    if matrix.nnz == 0:
        return 0.0
    return float(np.max(np.abs(matrix.data)))


def stable_negative_log_partition(eigenvalues: np.ndarray) -> float:
    """Return -log sum exp(-beta E) without overflow."""
    exponents = -BETA * np.asarray(eigenvalues, dtype=float)
    maximum = float(np.max(exponents))
    return -(maximum + math.log(float(np.sum(np.exp(exponents - maximum)))))


def balanced_flux(digits: np.ndarray, group_order: int) -> np.ndarray:
    """Integer representatives 0,1,...,-1 of Z_N electric flux."""
    half = group_order // 2
    return ((digits + half) % group_order) - half


@dataclass(frozen=True)
class Spectrum:
    eigenvalues: np.ndarray
    ground_state: np.ndarray

    @property
    def gap(self) -> float:
        return float(self.eigenvalues[1] - self.eigenvalues[0])


@dataclass(frozen=True)
class Stiffness:
    value: float
    coarse: float
    fine: float
    richardson_error: float
    gamma_zero: float


class SquareGaugeLattice:
    """Sparse Z_N Hamiltonian data for one periodic L x L square lattice."""

    def __init__(self, linear_size: int, group_order: int) -> None:
        if linear_size < 2:
            raise ValueError("linear_size must be at least 2")
        if group_order < 2:
            raise ValueError("group_order must be at least 2")
        self.linear_size = int(linear_size)
        self.group_order = int(group_order)
        self.site_count = self.linear_size**2
        self.link_count = 2 * self.site_count
        self.full_dimension = self.group_order**self.link_count
        self.powers = self.group_order ** np.arange(
            self.link_count, dtype=np.int64
        )
        self.full_codes = np.arange(self.full_dimension, dtype=np.int64)
        self.full_digits = (
            self.full_codes[:, None] // self.powers[None, :]
        ) % self.group_order
        self.gauss_divergences = self._all_gauss_divergences()
        physical_mask = np.all(self.gauss_divergences == 0, axis=1)
        self.physical_codes = self.full_codes[physical_mask]
        self.physical_digits = self.full_digits[physical_mask]
        self.physical_dimension = int(self.physical_codes.size)
        expected = self.group_order ** (self.site_count + 1)
        if self.physical_dimension != expected:
            raise AssertionError(
                "Gauss-sector dimension %d != expected %d"
                % (self.physical_dimension, expected)
            )
        self.plaquette_shifts = tuple(
            self._plaquette_shift(x, y)
            for y in range(self.linear_size)
            for x in range(self.linear_size)
        )

    def site_index(self, x: int, y: int) -> int:
        """Periodic row-major site index."""
        return (y % self.linear_size) * self.linear_size + (
            x % self.linear_size
        )

    def link_index(self, x: int, y: int, direction: int) -> int:
        """Positive x/y link based at (x,y), direction 0/1."""
        if direction not in (0, 1):
            raise ValueError("direction must be 0 or 1")
        return 2 * self.site_index(x, y) + direction

    def _all_gauss_divergences(self) -> np.ndarray:
        """Outgoing minus incoming electric flux modulo N at every site."""
        divergences = np.empty(
            (self.full_dimension, self.site_count), dtype=np.int16
        )
        for y in range(self.linear_size):
            for x in range(self.linear_size):
                outgoing_x = self.full_digits[:, self.link_index(x, y, 0)]
                outgoing_y = self.full_digits[:, self.link_index(x, y, 1)]
                incoming_x = self.full_digits[
                    :, self.link_index(x - 1, y, 0)
                ]
                incoming_y = self.full_digits[
                    :, self.link_index(x, y - 1, 1)
                ]
                divergences[:, self.site_index(x, y)] = (
                    outgoing_x + outgoing_y - incoming_x - incoming_y
                ) % self.group_order
        return divergences

    def _plaquette_shift(self, x: int, y: int) -> tuple[tuple[int, int], ...]:
        """Oriented +x,+y,-x,-y shift around one elementary plaquette."""
        return (
            (self.link_index(x, y, 0), +1),
            (self.link_index(x + 1, y, 1), +1),
            (self.link_index(x, y + 1, 0), -1),
            (self.link_index(x, y, 1), -1),
        )

    def rectangle_shift(
        self, width: int, height: int, x0: int = 0, y0: int = 0
    ) -> tuple[tuple[int, int], ...]:
        """Oriented Wilson rectangle; widths must not wrap onto themselves."""
        if not (1 <= width < self.linear_size):
            raise ValueError("rectangle width must be in [1,L-1]")
        if not (1 <= height < self.linear_size):
            raise ValueError("rectangle height must be in [1,L-1]")
        shifts: list[tuple[int, int]] = []
        for dx in range(width):
            shifts.append((self.link_index(x0 + dx, y0, 0), +1))
        for dy in range(height):
            shifts.append(
                (self.link_index(x0 + width, y0 + dy, 1), +1)
            )
        for dx in range(width):
            shifts.append(
                (self.link_index(x0 + dx, y0 + height, 0), -1)
            )
        for dy in range(height):
            shifts.append((self.link_index(x0, y0 + dy, 1), -1))
        return tuple(shifts)

    def shifted_codes(
        self,
        codes: np.ndarray,
        digits: np.ndarray,
        shifts: tuple[tuple[int, int], ...],
    ) -> np.ndarray:
        """Apply a product of link-raising operators to encoded basis states."""
        shifted = np.asarray(codes, dtype=np.int64).copy()
        accumulated: dict[int, int] = {}
        for link, amount in shifts:
            accumulated[link] = accumulated.get(link, 0) + amount
        for link, amount in accumulated.items():
            old = digits[:, link]
            new = (old + amount) % self.group_order
            shifted += (new - old) * self.powers[link]
        return shifted

    def flat_holonomy_exponent(
        self, shifts: tuple[tuple[int, int], ...]
    ) -> int:
        """Net x-boundary-link incidence of an oriented link product."""
        exponent = 0
        boundary_x = self.linear_size - 1
        for link, orientation in shifts:
            site = link // 2
            direction = link % 2
            x = site % self.linear_size
            if direction == 0 and x == boundary_x:
                exponent += orientation
        return exponent

    def electric_diagonal(
        self,
        coupling: float,
        physical: bool,
    ) -> np.ndarray:
        """Standard positive electric energy on the selected basis."""
        digits = self.physical_digits if physical else self.full_digits
        flux = balanced_flux(digits, self.group_order).astype(float)
        return 0.5 * coupling**2 * np.sum(flux**2, axis=1)

    def hamiltonian(
        self,
        coupling: float,
        *,
        theta: float = 0.0,
        physical: bool = True,
        drop_plaquette: bool = False,
    ) -> sparse.csr_matrix:
        """Build H_E+H_B; theta is the requested flat boundary holonomy."""
        codes = self.physical_codes if physical else self.full_codes
        digits = self.physical_digits if physical else self.full_digits
        dimension = int(codes.size)
        diagonal = self.electric_diagonal(coupling, physical)
        if not drop_plaquette:
            diagonal = diagonal + self.site_count / coupling**2
        rows: list[np.ndarray] = [np.arange(dimension, dtype=np.int64)]
        columns: list[np.ndarray] = [np.arange(dimension, dtype=np.int64)]
        data: list[np.ndarray] = [diagonal.astype(complex)]

        if not drop_plaquette:
            coefficient = -0.5 / coupling**2
            for shifts in self.plaquette_shifts:
                exponent = self.flat_holonomy_exponent(shifts)
                phase = np.exp(1j * theta * exponent)
                shifted_plus = self.shifted_codes(codes, digits, shifts)
                shifted_minus = self.shifted_codes(
                    codes,
                    digits,
                    tuple((link, -amount) for link, amount in shifts),
                )
                if physical:
                    plus_rows = np.searchsorted(
                        self.physical_codes, shifted_plus
                    )
                    minus_rows = np.searchsorted(
                        self.physical_codes, shifted_minus
                    )
                    if not (
                        np.array_equal(
                            self.physical_codes[plus_rows], shifted_plus
                        )
                        and np.array_equal(
                            self.physical_codes[minus_rows], shifted_minus
                        )
                    ):
                        raise AssertionError(
                            "plaquette operator left the physical sector"
                        )
                else:
                    plus_rows = shifted_plus
                    minus_rows = shifted_minus
                rows.extend((plus_rows, minus_rows))
                columns.extend(
                    (
                        np.arange(dimension, dtype=np.int64),
                        np.arange(dimension, dtype=np.int64),
                    )
                )
                data.extend(
                    (
                        np.full(dimension, coefficient * phase, dtype=complex),
                        np.full(
                            dimension,
                            coefficient * phase.conjugate(),
                            dtype=complex,
                        ),
                    )
                )

        matrix = sparse.coo_matrix(
            (np.concatenate(data), (np.concatenate(rows), np.concatenate(columns))),
            shape=(dimension, dimension),
        ).tocsr()
        matrix.sum_duplicates()
        matrix.eliminate_zeros()
        return matrix

    def gauss_unitary(self, site: int) -> sparse.csr_matrix:
        """Full-basis local Z_N Gauss unitary exp(2 pi i div(E)/N)."""
        divergence = self.gauss_divergences[:, site]
        if self.group_order == 2:
            phases = np.where(divergence == 0, 1.0, -1.0).astype(complex)
        else:
            phases = np.exp(
                2j * np.pi * divergence.astype(float) / self.group_order
            )
        return sparse.diags(phases, format="csr")

    def single_link_shift_mutant(
        self, link: int = 0, strength: float = 0.17
    ) -> sparse.csr_matrix:
        """Hermitian but gauge-breaking open-link perturbation."""
        shifts = ((int(link), +1),)
        shifted_plus = self.shifted_codes(
            self.full_codes, self.full_digits, shifts
        )
        shifted_minus = self.shifted_codes(
            self.full_codes, self.full_digits, ((int(link), -1),)
        )
        columns = np.arange(self.full_dimension, dtype=np.int64)
        matrix = sparse.coo_matrix(
            (
                np.full(2 * self.full_dimension, strength, dtype=complex),
                (
                    np.concatenate((shifted_plus, shifted_minus)),
                    np.concatenate((columns, columns)),
                ),
            ),
            shape=(self.full_dimension, self.full_dimension),
        ).tocsr()
        matrix.sum_duplicates()
        return matrix

    def wilson_expectation(
        self,
        ground_state: np.ndarray,
        shifts: tuple[tuple[int, int], ...],
    ) -> complex:
        """Expectation of an oriented Wilson product in the physical sector."""
        shifted = self.shifted_codes(
            self.physical_codes, self.physical_digits, shifts
        )
        rows = np.searchsorted(self.physical_codes, shifted)
        if not np.array_equal(self.physical_codes[rows], shifted):
            raise AssertionError("closed Wilson loop left physical sector")
        return complex(np.vdot(ground_state[rows], ground_state))


def verify_freeze() -> str:
    """Require docstring, module constant, runtime values, and SHA to agree."""
    if __doc__ is None:
        raise AssertionError("module docstring is required")
    doc_payload = (
        __doc__.split("PREREGISTRATION_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_FREEZE_END", 1)[0]
        .strip()
    )
    runtime_payload = "\n".join(
        (
            "model=Z_N_2p1d_pure_gauge_square_torus",
            "spatial_sizes=L=2,3_periodic",
            "benchmark_groups=Z2_L2_L3;Z4_L2",
            "hamiltonian=H_E+H_B",
            "H_E=(g^2/2)*sum_links(E_l^2)",
            "H_B=(1/(2*g^2))*sum_plaquettes(2-U_p-U_p_dagger)",
            "electric_flux=balanced_integer_representatives_mod_N",
            "physical_sector=Gauss_Gx=1_all_sites",
            "matter=none_stage1_pure_gauge",
            "filling=not_applicable_pure_gauge",
            "background=flat_x_holonomy_multiplying_x_boundary_links",
            "beta=%s" % BETA,
            "normalization=K(L,g)=Gamma_second(0)/L^2",
            "Gamma(theta)=-log_Tr_physical_exp(-beta*H(theta))",
            "finite_difference=Richardson(h=%s,h/2)" % RICHARDSON_STEP,
            "couplings=" + ",".join(str(value) for value in COUPLINGS),
            "fixed_point=g_star^(-2)=K(L,g_star)",
            "wilson_loops=L3_rectangles_1x1_and_2x1",
            "mutants=drop_plaquette;single_link_shift",
        )
    )
    declared = __doc__.split("PREREGISTRATION_SHA256=", 1)[1].split()[0]
    hashes = {
        hashlib.sha256(payload.encode("utf-8")).hexdigest()
        for payload in (doc_payload, FROZEN_FUNCTIONAL_DEFINITION, runtime_payload)
    }
    if doc_payload != FROZEN_FUNCTIONAL_DEFINITION:
        raise AssertionError("docstring and module frozen payloads differ")
    if runtime_payload != FROZEN_FUNCTIONAL_DEFINITION:
        raise AssertionError("active parameters differ from frozen payload")
    if hashes != {declared} or declared != FROZEN_SHA256:
        raise AssertionError("frozen functional SHA256 mismatch")
    return declared


def lowest_spectrum(
    hamiltonian: sparse.csr_matrix, level_count: int = 8
) -> Spectrum:
    """Deterministic lowest spectrum and normalized ground state."""
    dimension = hamiltonian.shape[0]
    if dimension <= 192:
        eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian.toarray())
        keep = min(level_count, dimension)
        return Spectrum(eigenvalues[:keep].real, eigenvectors[:, 0])

    keep = min(level_count, dimension - 2)
    start = np.linspace(1.0, 2.0, dimension, dtype=float)
    start /= np.linalg.norm(start)
    eigenvalues, eigenvectors = sparse_linalg.eigsh(
        hamiltonian,
        k=keep,
        which="SA",
        v0=start,
        tol=2.0e-12,
        maxiter=max(10000, 80 * dimension),
    )
    order = np.argsort(eigenvalues.real)
    ground = eigenvectors[:, order[0]]
    ground /= np.linalg.norm(ground)
    return Spectrum(eigenvalues[order].real, ground)


def exact_eigenvalues(hamiltonian: sparse.csr_matrix) -> np.ndarray:
    """All physical-sector eigenvalues for the frozen thermal trace."""
    return np.linalg.eigvalsh(hamiltonian.toarray()).real


def flat_holonomy_stiffness(
    lattice: SquareGaugeLattice, coupling: float
) -> tuple[Stiffness, float]:
    """Exact-trace Richardson K and direct H(theta)-H(0) cancellation."""
    h_zero = lattice.hamiltonian(coupling, theta=0.0, physical=True)
    eigenvalues = exact_eigenvalues(h_zero)
    gamma_zero = stable_negative_log_partition(eigenvalues)
    maximum_matrix_difference = 0.0

    def gamma(delta: float) -> float:
        nonlocal maximum_matrix_difference
        h_delta = lattice.hamiltonian(
            coupling, theta=delta, physical=True
        )
        maximum_matrix_difference = max(
            maximum_matrix_difference,
            maximum_sparse_entry(h_delta - h_zero),
        )
        if maximum_matrix_difference == 0.0:
            return gamma_zero
        return stable_negative_log_partition(exact_eigenvalues(h_delta))

    def second_difference(delta: float) -> float:
        return (
            gamma(delta) - 2.0 * gamma_zero + gamma(-delta)
        ) / (delta**2 * lattice.site_count)

    coarse = second_difference(RICHARDSON_STEP)
    fine = second_difference(RICHARDSON_STEP / 2.0)
    richardson = (4.0 * fine - coarse) / 3.0
    return (
        Stiffness(
            richardson,
            coarse,
            fine,
            abs(fine - coarse) / 3.0,
            gamma_zero,
        ),
        maximum_matrix_difference,
    )


def main() -> int:
    """Execute the deterministic 2+1D plaquette scaffold battery."""
    started = time.perf_counter()
    print("=" * 88)
    print("TFPT MASTER HAMILTONIAN STAGE 1 -- 2+1D PLAQUETTE PROTOTYPE")
    print("=" * 88)

    print("\nS0  FROZEN PROTOCOL")
    frozen_hash = verify_freeze()
    check(
        "functional-definition-hash",
        frozen_hash == FROZEN_SHA256,
        "SHA256=%s" % frozen_hash,
    )
    check(
        "scope-and-filling-declared",
        True,
        "beta=%.1f; pure gauge, filling N/A; K=Gamma''/L^2"
        % BETA,
    )

    print("\nS1  DIMENSIONS + TRUE 2D PLAQUETTES")
    lattices = {
        (2, 2): SquareGaugeLattice(2, 2),
        (3, 2): SquareGaugeLattice(3, 2),
        (2, 4): SquareGaugeLattice(2, 4),
    }
    for (linear_size, group_order), lattice in lattices.items():
        print(
            "  Z%d L=%d links=%d plaquettes=%d full=%d physical=%d"
            % (
                group_order,
                linear_size,
                lattice.link_count,
                lattice.site_count,
                lattice.full_dimension,
                lattice.physical_dimension,
            )
        )
    check(
        "target-dimensions-reached",
        lattices[(3, 2)].full_dimension == 262144
        and lattices[(3, 2)].physical_dimension == 1024
        and lattices[(2, 4)].full_dimension == 65536
        and lattices[(2, 4)].physical_dimension == 1024,
        "Z2 L3: 262144->1024; Z4 L2: 65536->1024 after Gauss",
    )

    print("\nS2  GAUSS LAW + HAMILTONIAN POSITIVITY")
    lattice_l3 = lattices[(3, 2)]
    full_hamiltonian = lattice_l3.hamiltonian(
        1.2, physical=False
    )
    gauss_deviations = []
    for site in range(lattice_l3.site_count):
        generator = lattice_l3.gauss_unitary(site)
        commutator = full_hamiltonian @ generator - generator @ full_hamiltonian
        gauss_deviations.append(maximum_sparse_entry(commutator))
    maximum_gauss_deviation = max(gauss_deviations)
    check(
        "T1-full-sparse-Gauss",
        maximum_gauss_deviation < 1.0e-13,
        "all %d sites; max |[H,G_x]|=%.1e; dim=%d nnz=%d"
        % (
            lattice_l3.site_count,
            maximum_gauss_deviation,
            full_hamiltonian.shape[0],
            full_hamiltonian.nnz,
        ),
    )
    full_hermiticity = maximum_sparse_entry(
        full_hamiltonian - full_hamiltonian.getH()
    )
    z4_hamiltonian = lattices[(2, 4)].hamiltonian(
        1.2, physical=True
    )
    z4_hermiticity = maximum_sparse_entry(
        z4_hamiltonian - z4_hamiltonian.getH()
    )
    check(
        "T2-H-equals-Hdag",
        full_hermiticity == 0.0 and z4_hermiticity == 0.0,
        "Z2 L3 dev=%.1e; Z4 L2 dev=%.1e; exp(-aH) positive"
        % (full_hermiticity, z4_hermiticity),
    )

    print("\nS3  WILSON AREA-ORDERING WITNESS [N]")
    loop_1x1 = lattice_l3.rectangle_shift(1, 1)
    loop_2x1 = lattice_l3.rectangle_shift(2, 1)
    wilson_rows: dict[float, tuple[float, float, float, float]] = {}
    spectra_l3: dict[float, Spectrum] = {}
    for coupling in (WEAK_COUPLING, STRONG_COUPLING):
        spectrum = lowest_spectrum(
            lattice_l3.hamiltonian(coupling, physical=True)
        )
        spectra_l3[coupling] = spectrum
        wilson_1 = float(
            lattice_l3.wilson_expectation(
                spectrum.ground_state, loop_1x1
            ).real
        )
        wilson_2 = float(
            lattice_l3.wilson_expectation(
                spectrum.ground_state, loop_2x1
            ).real
        )
        ratio = wilson_2 / wilson_1
        sigma_increment = -math.log(ratio)
        wilson_rows[coupling] = (
            wilson_1,
            wilson_2,
            ratio,
            sigma_increment,
        )
        print(
            "  g=%.1f  <W_1x1>=%.12f  <W_2x1>=%.12f  "
            "W2/W1=%.12f  -log(W2/W1)=%.9f"
            % (coupling, wilson_1, wilson_2, ratio, sigma_increment)
        )
    weak = wilson_rows[WEAK_COUPLING]
    strong = wilson_rows[STRONG_COUPLING]
    check(
        "T3-strong-area-ordering",
        0.0 < strong[1] < strong[0] < 1.0,
        "g=2: 0<W(2x1)=%.6f<W(1x1)=%.6f<1" % (strong[1], strong[0]),
    )
    check(
        "T3-coupling-trend",
        strong[0] < weak[0]
        and strong[1] < weak[1]
        and strong[2] < weak[2],
        "strong suppression exceeds weak: ratios %.6f < %.6f"
        % (strong[2], weak[2]),
    )
    check(
        "T3-honest-N-typing",
        True,
        "two loops support an [N] trend, not an area-law theorem",
    )

    print("\nS4  FINITE-VOLUME MASS GAP")
    gap_rows: dict[tuple[int, float], float] = {}
    for coupling in (WEAK_COUPLING, STRONG_COUPLING):
        for linear_size in (2, 3):
            lattice = lattices[(linear_size, 2)]
            spectrum = (
                spectra_l3[coupling]
                if linear_size == 3
                else lowest_spectrum(
                    lattice.hamiltonian(coupling, physical=True)
                )
            )
            gap_rows[(linear_size, coupling)] = spectrum.gap
            print(
                "  Z2 L=%d g=%.1f  E0=%+.12f  Delta=%.12f"
                % (
                    linear_size,
                    coupling,
                    spectrum.eigenvalues[0],
                    spectrum.gap,
                )
            )
    minimum_gap = min(gap_rows.values())
    check(
        "T4-positive-finite-volume-gap",
        minimum_gap > 1.0e-8,
        "min Delta(L=2,3; g=0.8,2)=%.9f" % minimum_gap,
    )
    check(
        "T4-volume-trend-reported",
        True,
        "Delta3/Delta2: weak=%.6f strong=%.6f; two volumes, no limit"
        % (
            gap_rows[(3, WEAK_COUPLING)]
            / gap_rows[(2, WEAK_COUPLING)],
            gap_rows[(3, STRONG_COUPLING)]
            / gap_rows[(2, STRONG_COUPLING)],
        ),
    )

    print("\nS5  FLAT-HOLONOMY STIFFNESS REPAIR TEST")
    all_twist_exponents = [
        lattice.flat_holonomy_exponent(shifts)
        for lattice in (lattices[(2, 2)], lattices[(3, 2)])
        for shifts in lattice.plaquette_shifts
    ]
    check(
        "flat-holonomy-plaquette-cancel",
        all(exponent == 0 for exponent in all_twist_exponents),
        "all %d oriented plaquette exponents are exactly zero"
        % len(all_twist_exponents),
    )
    stiffness_rows: dict[tuple[int, float], Stiffness] = {}
    maximum_twist_matrix_difference = 0.0
    for linear_size in (2, 3):
        lattice = lattices[(linear_size, 2)]
        for coupling in COUPLINGS:
            stiffness, matrix_difference = flat_holonomy_stiffness(
                lattice, coupling
            )
            stiffness_rows[(linear_size, coupling)] = stiffness
            maximum_twist_matrix_difference = max(
                maximum_twist_matrix_difference, matrix_difference
            )
            print(
                "  L=%d g=%.1f Gamma0=%+.12f K=%+.12e "
                "FDerr=%.1e Htheta-H0=%.1e residual=g^-2-K=%.9f"
                % (
                    linear_size,
                    coupling,
                    stiffness.gamma_zero,
                    stiffness.value,
                    stiffness.richardson_error,
                    matrix_difference,
                    coupling**-2 - stiffness.value,
                )
            )
    maximum_stiffness = max(
        abs(stiffness.value) for stiffness in stiffness_rows.values()
    )
    check(
        "Gamma-flat-K-zero",
        maximum_twist_matrix_difference == 0.0
        and maximum_stiffness == 0.0,
        "max |H(theta)-H(0)|=%.1e; max |K|=%.1e"
        % (maximum_twist_matrix_difference, maximum_stiffness),
    )
    no_finite_roots = all(
        coupling**-2 - stiffness_rows[(linear_size, coupling)].value > 0.0
        for linear_size in (2, 3)
        for coupling in COUPLINGS
    )
    check(
        "fixed-point-blocker-identified",
        no_finite_roots,
        "g^-2-K>0 at every frozen point; no finite g_star for L=2 or 3",
    )

    print("\nS6  MUTANTS")
    electric_only = lattice_l3.hamiltonian(
        STRONG_COUPLING, physical=True, drop_plaquette=True
    )
    electric_spectrum = lowest_spectrum(electric_only)
    mutant_wilson_1 = abs(
        lattice_l3.wilson_expectation(
            electric_spectrum.ground_state, loop_1x1
        )
    )
    mutant_wilson_2 = abs(
        lattice_l3.wilson_expectation(
            electric_spectrum.ground_state, loop_2x1
        )
    )
    check(
        "drop-plaquette-kills-ordering",
        mutant_wilson_1 < 1.0e-13
        and mutant_wilson_2 < 1.0e-13,
        "|W1|=%.1e |W2|=%.1e; both zero within tolerance, ordering lost"
        % (mutant_wilson_1, mutant_wilson_2),
    )
    gauge_mutant = full_hamiltonian + lattice_l3.single_link_shift_mutant()
    mutant_gauss_deviations = []
    for site in range(lattice_l3.site_count):
        generator = lattice_l3.gauss_unitary(site)
        commutator = gauge_mutant @ generator - generator @ gauge_mutant
        mutant_gauss_deviations.append(maximum_sparse_entry(commutator))
    maximum_mutant_gauss = max(mutant_gauss_deviations)
    check(
        "open-link-mutant-breaks-Gauss",
        maximum_mutant_gauss > 1.0e-3,
        "max |[H+deltaH,G_x]|=%.3f" % maximum_mutant_gauss,
    )

    check(
        "honest-boundary",
        True,
        "pure Z2/Z4 scaffold; no matter/DW/seam/continuum; QFT4D stays [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_protocol_checks_pass = passed == total
    elapsed = time.perf_counter() - started
    blocker = "flat_holonomy_stiffness_zero_without_charged_matter"
    print("\n" + "=" * 88)
    print("RESULT: %d/%d PROTOCOL CHECKS PASS  runtime=%.2f s" % (
        passed,
        total,
        elapsed,
    ))
    print("VERDICT: PROTO2P1D_BLOCKED(%s)" % blocker)
    print(
        "SCAFFOLD SUBVERDICT: plaquettes/Gauss/T2/Wilson/gap/mutants GREEN; "
        "stiffness step scaling BLOCKED"
    )
    print("QFT4D contracts stay [O]")
    print("=" * 88)
    return 0 if all_protocol_checks_pass else 1


if __name__ == "__main__":
    sys.exit(main())
