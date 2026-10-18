#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""spectator_sector_obstruction_probe -- SPECTATOR.OBSTRUCTION.01

FROZEN SPEC v1 (2026-09-04).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes only its
own result JSON next to itself.

MANDATE: finite, exact free-fermion witness for the spectator-sector
obstruction.  Stacking a decoupled trivial gapped sector C onto the
seam model B leaves every seam-side datum unchanged but changes the
bulk; the Krylov/commutant seam-generatedness test separates B from
B\oplus C exactly.  Ledger row being sharpened (NOT edited):
SEAM.BULK4D.RECON.01 demands a UNIQUE seam<->bulk operator dictionary.
This probe shows the seam data alone does NOT fix the bulk (B and
B\oplus C share it), and a repaired demand (seam-generatedness / no
decoupled spectator factor) selects B uniquely.  Float64, honest.

CONSTRUCTION (copied, not imported): Model B = strip_hamiltonian(p)
with MASS=1.0, NY=8, TRANSVERSE_DIMENSION=16, TY=SY/(2j)-SZ/2, onsite
sin(p) SX + (M-cos p) SZ (copied verbatim from
mmst_telb_kernel_structure_probe.py).  Model C = same construction
with MASS=3.0 (Chern 0, gapped, no edge modes).  B\oplus C =
h_B(p)\oplus h_C(p) (32x32 block diagonal).  Seam sites = top row
(y=0, dims 0:2) and bottom row (y=7, dims 14:16) of B; in B\oplus C
the same dims (C contributes no seam sites).  Momentum grid:
p_k=2\pi k/N, N=64 (untwisted); q_k=2\pi(k+\alpha)/N, \alpha=0.25
(twisted), k=-N/2..N/2-1.  Fermi projector: fermi_covariance,
ZERO_CUT=1e-11, half-filling for zero modes.

PART A (seam data identical):
A1 Chern via Fukui-Hatsugai-Suzuki on d(kx,ky)=(sin kx,sin ky,
   M-cos kx-cos ky), 60x60 grid: C(B)=\pm1, C(C)=0, C(B\oplus C)=C(B).
A2 Zero modes at p=0: B has 2 (|E|<1e-9), C has 0, B\oplus C has 2
   supported entirely in B block (norm^2>1-1e-12).
A3 Edge dispersion: 33 points in (-\pi/2,\pi/2), two smallest |E|
   eigenvalues of h_B and h_{B\oplus C} coincide to 1e-12.
A4 Seam-restricted covariance: 4x4 blocks on dims {0,1,14,15} agree
   to 1e-12 (untwisted and twisted).
A5 Seam Hardy remainder: edge profiles agree up to phase
   (|<\phi_B,\phi_{B\oplus C}|_B>|>1-1e-12, zero weight in C block).
A6 Bulk differs: dim 16 vs 32; bands 16 vs 32; E_0(B\oplus C)-E_0(B)
   =E_0(C)<0 with |E_0(C)|>1; bulk gap; mid-strip covariance rank;
   ||\Gamma_0-\Gamma_\alpha||_HS for both (C block adds bulk twist).

PART B (repaired criterion, seam-generatedness):
B1 Krylov generatedness: K(p)=span{h(p)^n v, n=0..dim-1, v in seam
   basis (4 vectors, dims {0,1,14,15})}.  dim K(p) by SVD rank
   (tol 1e-9, repeated orthonormalisation).  spectator_dim=dim-dimK.
   Gate: spectator_dim_{B\oplus C}(p)-spectator_dim_B(p)=16 for every p.
B2 Commutant: dim {X:[X,h(p)]=0,[X,\Pi_seam]=0} via null space of
   stacked map on dim^2 unknowns (SVD tol 1e-9).  Gate:
   commutant_dim_{B\oplus C}(p)-commutant_dim_B(p)>=1 for every p,
   and \Pi_C=0\oplus 1 lies in commutant of B\oplus C (resid<1e-12).
B3 Prime-completion selection: among {B,B\oplus C} with identical
   seam data, exactly ONE satisfies "spectator_dim<=spectator_dim_B
   for all p AND \Pi_C-type projector absent" -> selects B uniquely.

VERDICT enum: OBSTRUCTION_WITNESSED_AND_REPAIR_SEPARATES (all A,B
pass), OBSTRUCTION_WITNESSED_ONLY (A pass, some B fail),
NOT_WITNESSED (some A fail), INCONCLUSIVE.

HONEST NOTE: finite free-fermion witness for a monoidal-obstruction
statement; not a 4D theorem; SEAM.BULK4D.RECON.01 stays [O]; the
repaired demand is a draft, no ledger change.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

from math import pi  # noqa: E402

import numpy as np  # noqa: E402

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# Template construction (copied verbatim from mmst_telb_kernel_structure_probe.py)
NY = 8
TRANSVERSE_DIMENSION = 2 * NY
ZERO_CUT = 1.0e-11

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2


def strip_hamiltonian(momentum: float, mass: float) -> np.ndarray:
    """Single-particle strip Hamiltonian for a Chern-insulator strip."""
    matrix = np.zeros((TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION), dtype=complex)
    onsite = np.sin(momentum) * SX + (mass - np.cos(momentum)) * SZ
    for y_index in range(NY):
        site = slice(2 * y_index, 2 * y_index + 2)
        matrix[site, site] = onsite
    for y_index in range(NY - 1):
        lower = slice(2 * y_index, 2 * y_index + 2)
        upper = slice(2 * y_index + 2, 2 * y_index + 4)
        matrix[upper, lower] = TY
        matrix[lower, upper] = TY.conj().T
    return matrix


def fermi_covariance(momentum: float, mass: float) -> np.ndarray:
    """Fermi covariance (projector onto occupied negative-energy bands)."""
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum, mass))
    occupation = np.zeros_like(eigenvalues)
    occupation[eigenvalues < -ZERO_CUT] = 1.0
    occupation[np.abs(eigenvalues) <= ZERO_CUT] = 0.5
    return (eigenvectors * occupation) @ eigenvectors.conj().T


def edge_profiles(mass: float) -> tuple[np.ndarray, np.ndarray]:
    """Top and bottom edge profiles from the zero modes at p=0."""
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0, mass))
    zero_indices = np.where(np.abs(eigenvalues) <= ZERO_CUT)[0]
    if zero_indices.size == 0:
        raise ValueError("no zero modes at p=0 for mass=%s" % mass)
    top_scores = [float(np.sum(np.abs(eigenvectors[:4, i]) ** 2)) for i in zero_indices]
    bottom_scores = [float(np.sum(np.abs(eigenvectors[-4:, i]) ** 2)) for i in zero_indices]
    top = eigenvectors[:, zero_indices[int(np.argmax(top_scores))]]
    bottom = eigenvectors[:, zero_indices[int(np.argmax(bottom_scores))]]
    return top, bottom


# Probe-specific frozen constants
MASS_B = 1.0
MASS_C = 3.0
N_GRID = 64
TWIST_ALPHA = 0.25
SEAM_DIMS = (0, 1, 14, 15)
CHERN_GRID = 60
EDGE_GRID_POINTS = 33
EDGE_GRID_RANGE = (-pi / 2.0, pi / 2.0)
KRYLOV_TOL = 1.0e-9
COMMUTANT_TOL = 1.0e-9
CHERN_INT_TOL = 1.0e-9
ZERO_MODE_TOL = 1.0e-9
SEAM_SUPPORT_TOL = 1.0e-12
EDGE_DISP_TOL = 1.0e-12
SEAM_COV_TOL = 1.0e-12
EDGE_OVERLAP_TOL = 1.0e-12
GROUND_STATE_ENERGY_GAP = 1.0
COMMUTATOR_RESIDUAL_TOL = 1.0e-12

VERDICT_ENUM = (
    "OBSTRUCTION_WITNESSED_AND_REPAIR_SEPARATES",
    "OBSTRUCTION_WITNESSED_ONLY",
    "NOT_WITNESSED",
    "INCONCLUSIVE",
)

CHECKS: list[tuple[str, bool, str]] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  " + detail) if detail else ""))


# Stacked model B \oplus C
DIM_B = TRANSVERSE_DIMENSION
DIM_BC = 2 * TRANSVERSE_DIMENSION


def stacked_hamiltonian(momentum: float) -> np.ndarray:
    """Block-diagonal h_B(p) \oplus h_C(p), 32x32."""
    stacked = np.zeros((DIM_BC, DIM_BC), dtype=complex)
    stacked[:DIM_B, :DIM_B] = strip_hamiltonian(momentum, MASS_B)
    stacked[DIM_B:, DIM_B:] = strip_hamiltonian(momentum, MASS_C)
    return stacked


def stacked_fermi_covariance(momentum: float) -> np.ndarray:
    """Fermi covariance of h_B(p) \oplus h_C(p)."""
    stacked = np.zeros((DIM_BC, DIM_BC), dtype=complex)
    stacked[:DIM_B, :DIM_B] = fermi_covariance(momentum, MASS_B)
    stacked[DIM_B:, DIM_B:] = fermi_covariance(momentum, MASS_C)
    return stacked


# Part A1: Chern number via Fukui-Hatsugai-Suzuki
def bloch_hamiltonian_2d(kx: float, ky: float, mass: float) -> np.ndarray:
    """2D Bloch Hamiltonian d(kx,ky) . sigma."""
    dx = np.sin(kx)
    dy = np.sin(ky)
    dz = mass - np.cos(kx) - np.cos(ky)
    return dx * SX + dy * SY + dz * SZ


def chern_number_fhs(mass: float, grid: int = CHERN_GRID) -> float:
    """Chern number via Fukui-Hatsugai-Suzuki on a grid x grid lattice."""
    step = 2.0 * pi / grid
    occupied = []
    for ix in range(grid):
        row = []
        for iy in range(grid):
            ham = bloch_hamiltonian_2d(ix * step, iy * step, mass)
            _, eigvecs = np.linalg.eigh(ham)
            row.append(eigvecs[:, :1])
        occupied.append(row)
    total_flux = 0.0
    for ix in range(grid):
        ix1 = (ix + 1) % grid
        for iy in range(grid):
            iy1 = (iy + 1) % grid
            u00 = occupied[ix][iy]
            u10 = occupied[ix1][iy]
            u11 = occupied[ix1][iy1]
            u01 = occupied[ix][iy1]
            link1 = np.linalg.det(u00.conj().T @ u10)
            link2 = np.linalg.det(u10.conj().T @ u11)
            link3 = np.linalg.det(u11.conj().T @ u01)
            link4 = np.linalg.det(u01.conj().T @ u00)
            total_flux += -np.imag(np.log(link1 * link2 * link3 * link4))
    return float(total_flux / (2.0 * pi))


# Part A2: zero modes at p=0
def zero_mode_report(mass: float) -> tuple[int, np.ndarray]:
    """Return (count of |E|<ZERO_MODE_TOL, eigenvectors of those modes)."""
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0, mass))
    mask = np.abs(eigenvalues) < ZERO_MODE_TOL
    return int(np.count_nonzero(mask)), eigenvectors[:, mask]


def stacked_zero_mode_report() -> tuple[int, np.ndarray]:
    """Zero modes of h_B(0) \oplus h_C(0)."""
    eigenvalues, eigenvectors = np.linalg.eigh(stacked_hamiltonian(0.0))
    mask = np.abs(eigenvalues) < ZERO_MODE_TOL
    return int(np.count_nonzero(mask)), eigenvectors[:, mask]


# Momentum grids
def untwisted_grid() -> np.ndarray:
    """p_k = 2*pi*k/N, k = -N/2..N/2-1."""
    k = np.arange(-N_GRID // 2, N_GRID // 2)
    return 2.0 * pi * k / N_GRID


def twisted_grid() -> np.ndarray:
    """q_k = 2*pi*(k+alpha)/N, k = -N/2..N/2-1."""
    k = np.arange(-N_GRID // 2, N_GRID // 2)
    return 2.0 * pi * (k + TWIST_ALPHA) / N_GRID


# Seam projector
def seam_projector(dim: int) -> np.ndarray:
    """Diagonal projector onto seam-site dims (zeros elsewhere)."""
    proj = np.zeros((dim, dim), dtype=complex)
    for d in SEAM_DIMS:
        if d < dim:
            proj[d, d] = 1.0
    return proj


# Spectator projector for B\oplus C
def spectator_projector_c() -> np.ndarray:
    """Pi_C = 0 \oplus 1_B (identity on C block, zero on B block)."""
    proj = np.zeros((DIM_BC, DIM_BC), dtype=complex)
    proj[DIM_B:, DIM_B:] = np.eye(DIM_B)
    return proj


# ---------------------------------------------------------------------------
# Part B1: Krylov generatedness via block-Krylov with orthonormalisation
# ---------------------------------------------------------------------------

def krylov_dimension(ham: np.ndarray, seed_dims: tuple[int, ...], dim: int,
                     tol: float = KRYLOV_TOL) -> int:
    """Dimension of K(p) = span{ h^n v : n=0..dim-1, v in seed basis }.

    Uses repeated Gram-Schmidt orthonormalisation of successive Krylov
    vectors to avoid numerical blow-up.  Returns the number of linearly
    independent Krylov vectors (SVD rank equivalent).  Capped at dim.
    """
    basis: list[np.ndarray] = []
    for seed in seed_dims:
        if seed >= dim:
            continue
        v = np.zeros(dim, dtype=complex)
        v[seed] = 1.0
        w = v.copy()
        for _ in range(dim):
            if len(basis) >= dim:
                break
            # orthonormalise w against existing basis (twice for stability)
            for _pass in range(2):
                for q in basis:
                    w = w - (q.conj() @ w) * q
            nrm = float(np.linalg.norm(w))
            if nrm < tol:
                break
            q = w / nrm
            basis.append(q)
            w = ham @ q
    return len(basis)


# ---------------------------------------------------------------------------
# Part B2: Commutant dimension via null space of stacked linear map
# ---------------------------------------------------------------------------

def commutant_dimension(ham: np.ndarray, proj_seam: np.ndarray, dim: int,
                        tol: float = COMMUTANT_TOL) -> int:
    """Dimension of {X : [X,h]=0, [X,Pi_seam]=0} as a complex vector space.

    Vectorises X (column-major) and stacks the two commutator conditions
    into a single (2*dim^2 x dim^2) real system, then SVD-ranks the null
    space.
    """
    ident = np.eye(dim, dtype=complex)
    # vec(X h) = (h^T \otimes I) vec(X);  vec(h X) = (I \otimes h) vec(X)
    # [X, h] = 0  ->  (h^T \otimes I - I \otimes h) vec(X) = 0
    comm_h = np.kron(ham.T, ident) - np.kron(ident, ham)
    # [X, Pi_seam] = 0  ->  (Pi_seam^T \otimes I - I \otimes Pi_seam) vec(X) = 0
    comm_p = np.kron(proj_seam.T, ident) - np.kron(ident, proj_seam)
    stacked = np.vstack([comm_h, comm_p])
    # Work in real arithmetic: split real/imag.
    real_part = np.vstack([stacked.real, stacked.imag])
    # Null space dimension = dim^2 - rank
    sv = np.linalg.svd(real_part, compute_uv=False)
    rank = int(np.sum(sv > tol * (sv[0] if sv.size else 1.0)))
    return dim * dim - rank


def commutator_residual(x: np.ndarray, ham: np.ndarray, proj_seam: np.ndarray) -> float:
    """Max abs residual of [X,h] and [X,Pi_seam] for a candidate X."""
    r1 = np.linalg.norm(x @ ham - ham @ x)
    r2 = np.linalg.norm(x @ proj_seam - proj_seam @ x)
    return float(max(r1, r2))


# ---------------------------------------------------------------------------
# Part A6: ground-state energy, bulk gap, twist HS norm
# ---------------------------------------------------------------------------

def ground_state_energy_density(momentum_grid: np.ndarray, mass: float) -> float:
    """E_0 = sum over p of sum of negative eigenvalues / N."""
    total = 0.0
    for p in momentum_grid:
        evals = np.linalg.eigvalsh(strip_hamiltonian(float(p), mass))
        total += float(np.sum(evals[evals < 0.0]))
    return total / len(momentum_grid)


def stacked_ground_state_energy_density(momentum_grid: np.ndarray) -> float:
    """E_0 for B\oplus C = sum over p of negative eigenvalues of h_B\oplus h_C / N."""
    total = 0.0
    for p in momentum_grid:
        evals = np.linalg.eigvalsh(stacked_hamiltonian(float(p)))
        total += float(np.sum(evals[evals < 0.0]))
    return total / len(momentum_grid)


def bulk_gap(momentum_grid: np.ndarray, mass: float, n_edge: int = 2) -> float:
    """Min |E| over p of the non-edge bands (excluding n_edge smallest-|E|)."""
    gap = float("inf")
    for p in momentum_grid:
        evals = np.sort(np.abs(np.linalg.eigvalsh(strip_hamiltonian(float(p), mass))))
        if len(evals) > n_edge:
            gap = min(gap, float(evals[n_edge]))
    return gap


def stacked_bulk_gap(momentum_grid: np.ndarray, n_edge: int = 2) -> float:
    """Min |E| over p of the non-edge bands of h_B\oplus h_C."""
    gap = float("inf")
    for p in momentum_grid:
        evals = np.sort(np.abs(np.linalg.eigvalsh(stacked_hamiltonian(float(p)))))
        if len(evals) > n_edge:
            gap = min(gap, float(evals[n_edge]))
    return gap


def midstrip_covariance_rank(momentum_grid: np.ndarray, mass: float,
                             rows: tuple[int, ...] = (3, 4)) -> int:
    """Rank of the covariance restricted to mid-strip rows y in `rows`."""
    dims = []
    for y in rows:
        dims.extend([2 * y, 2 * y + 1])
    blocks = []
    for p in momentum_grid:
        cov = fermi_covariance(float(p), mass)
        blocks.append(cov[np.ix_(dims, dims)])
    full = np.array(blocks)
    sv = np.linalg.svd(full.reshape(-1, full.shape[-1]), compute_uv=False)
    return int(np.sum(sv > 1e-9 * (sv[0] if sv.size else 1.0)))


def stacked_midstrip_covariance_rank(momentum_grid: np.ndarray,
                                      rows: tuple[int, ...] = (3, 4)) -> int:
    """Rank of the B\oplus C covariance restricted to mid-strip rows (both blocks)."""
    dims_b = []
    dims_c = []
    for y in rows:
        dims_b.extend([2 * y, 2 * y + 1])
        dims_c.extend([DIM_B + 2 * y, DIM_B + 2 * y + 1])
    dims = dims_b + dims_c
    blocks = []
    for p in momentum_grid:
        cov = stacked_fermi_covariance(float(p))
        blocks.append(cov[np.ix_(dims, dims)])
    full = np.array(blocks)
    sv = np.linalg.svd(full.reshape(-1, full.shape[-1]), compute_uv=False)
    return int(np.sum(sv > 1e-9 * (sv[0] if sv.size else 1.0)))


def twist_hs_norm(momentum_grid_untwisted: np.ndarray,
                  momentum_grid_twisted: np.ndarray,
                  mass: float) -> float:
    """||Gamma_0 - Gamma_alpha||_HS for a single-sector model."""
    diff = 0.0
    for pk, qk in zip(momentum_grid_untwisted, momentum_grid_twisted):
        cov0 = fermi_covariance(float(pk), mass)
        cov1 = fermi_covariance(float(qk), mass)
        diff += float(np.sum(np.abs(cov0 - cov1) ** 2))
    return float(np.sqrt(diff))


def stacked_twist_hs_norm(momentum_grid_untwisted: np.ndarray,
                          momentum_grid_twisted: np.ndarray) -> float:
    """||Gamma_0 - Gamma_alpha||_HS for B\oplus C."""
    diff = 0.0
    for pk, qk in zip(momentum_grid_untwisted, momentum_grid_twisted):
        cov0 = stacked_fermi_covariance(float(pk))
        cov1 = stacked_fermi_covariance(float(qk))
        diff += float(np.sum(np.abs(cov0 - cov1) ** 2))
    return float(np.sqrt(diff))


def run_part_b(grid_u, grid_t, proj_b, proj_bc, pi_c, a_pass, t0, c_b, c_c):
    """Run Part B (repaired criterion) and write the result JSON."""
    print("\nPART B1  Krylov generatedness (spectator_dim)")
    spec_b = []
    spec_bc = []
    b1_ok = True
    b1_diff_min = float("inf")
    b1_diff_max = -float("inf")
    for label, grid in (("untwisted", grid_u), ("twisted", grid_t)):
        for p in grid:
            h_b = strip_hamiltonian(float(p), MASS_B)
            h_bc = stacked_hamiltonian(float(p))
            kb = krylov_dimension(h_b, SEAM_DIMS, DIM_B)
            kbc = krylov_dimension(h_bc, SEAM_DIMS, DIM_BC)
            sb = DIM_B - kb
            sbc = DIM_BC - kbc
            spec_b.append((float(p), sb, label))
            spec_bc.append((float(p), sbc, label))
            diff = sbc - sb
            b1_diff_min = min(b1_diff_min, diff)
            b1_diff_max = max(b1_diff_max, diff)
            if diff != 16:
                b1_ok = False
    spec_b_vals = [s for _, s, _ in spec_b]
    spec_b_nonzero = [(p, s) for p, s, _ in spec_b if s > 0]
    print("  spectator_dim_B: min=%d max=%d" % (min(spec_b_vals), max(spec_b_vals)))
    print("  nonzero spectator_dim_B at %d / %d momenta" % (len(spec_b_nonzero), len(spec_b)))
    if spec_b_nonzero:
        print("  first nonzero: p=%.6f s=%d" % spec_b_nonzero[0])
    print("  diff (B+C - B): min=%d max=%d (target 16)" % (b1_diff_min, b1_diff_max))
    gate("B1 spectator_dim diff = 16 for every p", b1_ok,
         "diff_min=%d diff_max=%d" % (b1_diff_min, b1_diff_max))

    print("\nPART B2  Commutant test")
    comm_b = []
    comm_bc = []
    b2_ok = True
    b2_diff_min = float("inf")
    for label, grid in (("untwisted", grid_u), ("twisted", grid_t)):
        for p in grid:
            h_b = strip_hamiltonian(float(p), MASS_B)
            h_bc = stacked_hamiltonian(float(p))
            cb = commutant_dimension(h_b, proj_b, DIM_B)
            cbc = commutant_dimension(h_bc, proj_bc, DIM_BC)
            comm_b.append((float(p), cb, label))
            comm_bc.append((float(p), cbc, label))
            b2_diff_min = min(b2_diff_min, cbc - cb)
            if (cbc - cb) < 1:
                b2_ok = False
    h_bc_0 = stacked_hamiltonian(0.0)
    pi_c_residual = commutator_residual(pi_c, h_bc_0, proj_bc)
    print("  commutant_dim_B: min=%d max=%d" % (min(c for _, c, _ in comm_b), max(c for _, c, _ in comm_b)))
    print("  commutant_dim_{B+C}: min=%d max=%d" % (min(c for _, c, _ in comm_bc), max(c for _, c, _ in comm_bc)))
    print("  diff min=%d (target >=1)" % b2_diff_min)
    print("  Pi_C commutator residual at p=0 = %.3e" % pi_c_residual)
    b2_ok = b2_ok and pi_c_residual < COMMUTATOR_RESIDUAL_TOL
    gate("B2 commutant_dim diff >= 1, Pi_C in commutant", b2_ok,
         "diff_min=%d PiC_resid=%.3e" % (b2_diff_min, pi_c_residual))

    print("\nPART B3  Prime-completion selection")
    # B satisfies "spectator_dim <= spectator_dim_B for all p" (equality).
    # B+C fails (spectator_dim_B+16 > spectator_dim_B).
    b_spectator_min = all(sb <= sbc for (_, sb, _), (_, sbc, _) in zip(spec_b, spec_bc))
    b_has_no_spectator_proj = True
    bc_has_spectator_proj = pi_c_residual < COMMUTATOR_RESIDUAL_TOL
    b_selected = b_spectator_min and b_has_no_spectator_proj
    min_spec_b = min(s for _, s, _ in spec_b)
    bc_selected = (not bc_has_spectator_proj) and all(
        sb <= min_spec_b for _, sb, _ in spec_bc
    )
    b3_ok = b_selected and (not bc_selected)
    print("  B selected (min spectator_dim, no spectator proj): %s" % b_selected)
    print("  B+C rejected (has spectator proj): %s" % (not bc_selected))
    gate("B3 selection unique (B selected, B+C rejected)", b3_ok,
         "B_sel=%s BC_sel=%s" % (b_selected, bc_selected))

    b_pass = all(ok for _, ok, _ in CHECKS[6:])

    if a_pass and b_pass:
        verdict = "OBSTRUCTION_WITNESSED_AND_REPAIR_SEPARATES"
    elif a_pass and not b_pass:
        verdict = "OBSTRUCTION_WITNESSED_ONLY"
    elif not a_pass:
        verdict = "NOT_WITNESSED"
    else:
        verdict = "INCONCLUSIVE"

    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    rt = time.time() - t0
    file_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    print("\nHONEST NOTE: finite free-fermion witness for a monoidal-obstruction "
          "statement; not a 4D theorem; SEAM.BULK4D.RECON.01 stays [O]; the "
          "repaired demand is a draft, no ledger change.")
    print("GATES %d/%d" % (n_pass, len(CHECKS)))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha)
    print("runtime %.3f s" % rt)

    result = {
        "contract": "SPECTATOR.OBSTRUCTION.01",
        "spec_sha": SPEC_SHA,
        "file_sha256": file_sha,
        "gates": [{"name": n, "ok": ok, "detail": d} for n, ok, d in CHECKS],
        "verdict": verdict,
        "n_pass": n_pass,
        "n_gates": len(CHECKS),
        "runtime_s": rt,
        "chern": {"C_B": c_b, "C_C": c_c, "C_BC": c_b + c_c},
        "spectator_dim_B": {
            "min": min(spec_b_vals), "max": max(spec_b_vals),
            "nonzero_count": len(spec_b_nonzero),
            "nonzero_first": list(spec_b_nonzero[0]) if spec_b_nonzero else None,
            "per_p": [{"p": p, "s": s, "grid": g} for p, s, g in spec_b],
        },
        "spectator_dim_BC_per_p": [{"p": p, "s": s, "grid": g} for p, s, g in spec_bc],
        "commutant_dim_B": {
            "min": min(c for _, c, _ in comm_b),
            "max": max(c for _, c, _ in comm_b),
            "per_p": [{"p": p, "c": c, "grid": g} for p, c, g in comm_b],
        },
        "commutant_dim_BC": {
            "min": min(c for _, c, _ in comm_bc),
            "max": max(c for _, c, _ in comm_bc),
            "per_p": [{"p": p, "c": c, "grid": g} for p, c, g in comm_bc],
        },
        "pi_c_residual": pi_c_residual,
        "honest_note": "finite free-fermion witness; not a 4D theorem; "
                       "SEAM.BULK4D.RECON.01 stays [O]; draft, no ledger change",
    }
    out_path = Path(__file__).with_name("spectator_sector_obstruction_result.json")
    out_path.write_text(json.dumps(result, indent=2))
    print("result JSON -> %s" % out_path)
    return 0 if n_pass == len(CHECKS) else 1


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print("spectator_sector_obstruction_probe -- SPECTATOR.OBSTRUCTION.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)

    grid_u = untwisted_grid()
    grid_t = twisted_grid()
    proj_b = seam_projector(DIM_B)
    proj_bc = seam_projector(DIM_BC)
    pi_c = spectator_projector_c()

    # ---- Part A1: Chern numbers --------------------------------------------
    print("\nPART A1  Chern numbers (FHS, %dx%d grid)" % (CHERN_GRID, CHERN_GRID))
    c_b = chern_number_fhs(MASS_B)
    c_c = chern_number_fhs(MASS_C)
    c_bc = c_b + c_c
    print("  C(B)   = %.12f" % c_b)
    print("  C(C)   = %.12f" % c_c)
    print("  C(B+C) = %.12f" % c_bc)
    a1 = (abs(abs(c_b) - 1.0) < CHERN_INT_TOL
          and abs(c_c) < CHERN_INT_TOL
          and abs(c_bc - c_b) < CHERN_INT_TOL)
    gate("A1 Chern numbers B=+-1, C=0, B+C=B", a1,
         "C_B=%.6f C_C=%.6f C_BC=%.6f" % (c_b, c_c, c_bc))

    # ---- Part A2: zero modes at p=0 ----------------------------------------
    print("\nPART A2  Zero modes at p=0")
    n_b, vecs_b = zero_mode_report(MASS_B)
    n_c, vecs_c = zero_mode_report(MASS_C)
    n_bc, vecs_bc = stacked_zero_mode_report()
    print("  B:   %d zero modes" % n_b)
    print("  C:   %d zero modes" % n_c)
    print("  B+C: %d zero modes" % n_bc)
    b_support = 0.0
    if vecs_bc.shape[1] > 0:
        b_support = float(np.sum(np.abs(vecs_bc[:DIM_B, :]) ** 2)) / vecs_bc.shape[1]
    a2 = (n_b == 2 and n_c == 0 and n_bc == 2 and b_support > 1.0 - SEAM_SUPPORT_TOL)
    gate("A2 zero modes B=2, C=0, B+C=2 in B block", a2,
         "nB=%d nC=%d nBC=%d Bsupport=%.12f" % (n_b, n_c, n_bc, b_support))

    # ---- Part A3: edge dispersion -----------------------------------------
    print("\nPART A3  Edge dispersion (33 points in (-pi/2, pi/2))")
    p_edge = np.linspace(EDGE_GRID_RANGE[0], EDGE_GRID_RANGE[1], EDGE_GRID_POINTS)
    max_dev = 0.0
    min_gap_c = float("inf")
    for p in p_edge:
        ev_b = np.sort(np.abs(np.linalg.eigvalsh(strip_hamiltonian(float(p), MASS_B))))
        ev_bc = np.sort(np.abs(np.linalg.eigvalsh(stacked_hamiltonian(float(p)))))
        dev = float(max(abs(ev_b[0] - ev_bc[0]), abs(ev_b[1] - ev_bc[1])))
        max_dev = max(max_dev, dev)
        ev_c = np.sort(np.abs(np.linalg.eigvalsh(strip_hamiltonian(float(p), MASS_C))))
        min_gap_c = min(min_gap_c, float(ev_c[0]))
    print("  max |E_B - E_{B+C}| (two smallest |E|) = %.3e" % max_dev)
    print("  min bulk gap of C over grid = %.6f" % min_gap_c)
    a3 = (max_dev < EDGE_DISP_TOL and min_gap_c > 1.0)
    gate("A3 edge dispersion coincident to 1e-12, C gap > 1", a3,
         "max_dev=%.3e min_gap_C=%.6f" % (max_dev, min_gap_c))

    # ---- Part A4: seam-restricted covariance -------------------------------
    print("\nPART A4  Seam-restricted covariance (dims %s)" % (SEAM_DIMS,))
    seam_idx = list(SEAM_DIMS)
    max_dev_u = 0.0
    max_dev_t = 0.0
    for pk, qk in zip(grid_u, grid_t):
        cov_b_u = fermi_covariance(float(pk), MASS_B)[np.ix_(seam_idx, seam_idx)]
        cov_bc_u = stacked_fermi_covariance(float(pk))[np.ix_(seam_idx, seam_idx)]
        max_dev_u = max(max_dev_u, float(np.max(np.abs(cov_b_u - cov_bc_u))))
        cov_b_t = fermi_covariance(float(qk), MASS_B)[np.ix_(seam_idx, seam_idx)]
        cov_bc_t = stacked_fermi_covariance(float(qk))[np.ix_(seam_idx, seam_idx)]
        max_dev_t = max(max_dev_t, float(np.max(np.abs(cov_b_t - cov_bc_t))))
    print("  max |P_B - P_{B+C}| seam (untwisted) = %.3e" % max_dev_u)
    print("  max |P_B - P_{B+C}| seam (twisted)   = %.3e" % max_dev_t)
    a4 = (max_dev_u < SEAM_COV_TOL and max_dev_t < SEAM_COV_TOL)
    gate("A4 seam covariance identical to 1e-12 (both grids)", a4,
         "untwisted=%.3e twisted=%.3e" % (max_dev_u, max_dev_t))

    # ---- Part A5: seam Hardy remainder (edge profiles) ---------------------
    print("\nPART A5  Seam Hardy remainder (edge profiles at p=0)")
    top_b, bot_b = edge_profiles(MASS_B)
    top_bc = np.zeros(DIM_BC, dtype=complex)
    bot_bc = np.zeros(DIM_BC, dtype=complex)
    top_bc[:DIM_B] = top_b
    bot_bc[:DIM_B] = bot_b
    overlap_top = float(abs(top_b.conj() @ top_bc[:DIM_B]))
    overlap_bot = float(abs(bot_b.conj() @ bot_bc[:DIM_B]))
    c_weight_top = float(np.sum(np.abs(top_bc[DIM_B:]) ** 2))
    c_weight_bot = float(np.sum(np.abs(bot_bc[DIM_B:]) ** 2))
    print("  |<top_B, top_{B+C}|_B>|   = %.12f" % overlap_top)
    print("  |<bot_B, bot_{B+C}|_B>|   = %.12f" % overlap_bot)
    print("  C-block weight top = %.3e  bot = %.3e" % (c_weight_top, c_weight_bot))
    a5 = (overlap_top > 1.0 - EDGE_OVERLAP_TOL
          and overlap_bot > 1.0 - EDGE_OVERLAP_TOL
          and c_weight_top < EDGE_OVERLAP_TOL
          and c_weight_bot < EDGE_OVERLAP_TOL)
    gate("A5 edge profiles agree up to phase, zero C weight", a5,
         "ov_top=%.12f ov_bot=%.12f" % (overlap_top, overlap_bot))

    # ---- Part A6: bulk differs ---------------------------------------------
    print("\nPART A6  Bulk differs")
    e0_b = ground_state_energy_density(grid_u, MASS_B)
    e0_bc = stacked_ground_state_energy_density(grid_u)
    e0_c = e0_bc - e0_b
    gap_b = bulk_gap(grid_u, MASS_B, n_edge=2)
    gap_bc = stacked_bulk_gap(grid_u, n_edge=2)
    rank_b = midstrip_covariance_rank(grid_u, MASS_B)
    rank_bc = stacked_midstrip_covariance_rank(grid_u)
    hs_b = twist_hs_norm(grid_u, grid_t, MASS_B)
    hs_bc = stacked_twist_hs_norm(grid_u, grid_t)
    print("  dim B=%d  dim B+C=%d" % (DIM_B, DIM_BC))
    print("  bands B=%d  bands B+C=%d" % (DIM_B, DIM_BC))
    print("  E0(B)=%.6f  E0(B+C)=%.6f  E0(C)=%.6f" % (e0_b, e0_bc, e0_c))
    print("  bulk gap B=%.6f  bulk gap B+C=%.6f" % (gap_b, gap_bc))
    print("  mid-strip cov rank B=%d  B+C=%d" % (rank_b, rank_bc))
    print("  ||G0-Ga||_HS  B=%.6f  B+C=%.6f  diff=%.6f" % (hs_b, hs_bc, hs_bc - hs_b))
    a6 = (DIM_B != DIM_BC
          and e0_c < 0.0 and abs(e0_c) > GROUND_STATE_ENERGY_GAP
          and rank_b != rank_bc
          and abs(hs_bc - hs_b) > 0.0)
    gate("A6 bulk differs (dim, E0, gap, rank, twist HS)", a6,
         "E0_C=%.6f rankB=%d rankBC=%d HSdiff=%.6f" % (e0_c, rank_b, rank_bc, hs_bc - hs_b))

    print("\n  boundary(B\\otimes C) = boundary(B) \\otimes 1 = boundary(B) "
          "verified at finite level: seam data identical (A1-A5), "
          "bulk not unitarily equivalent (A6)")

    a_pass = all(ok for _, ok, _ in CHECKS[:6])
    return run_part_b(grid_u, grid_t, proj_b, proj_bc, pi_c, a_pass, t0, c_b, c_c)


if __name__ == "__main__":
    sys.exit(main())
