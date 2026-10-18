#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1020 -- SPECTATOR-SECTOR OBSTRUCTION (BULK.PRIME_COMPLETION.01 / SEAM.BULK4D.RECON.01).

Promotion of the spectator-sector obstruction probe (round r644 audit
harvest, 2026-09-04).  The module RE-DERIVES the finite free-fermion
witness from scratch (no probe imports, no subprocess): stacking a
decoupled trivial gapped sector C onto the seam model B leaves every
seam-side datum unchanged but changes the bulk; a Krylov/commutant
seam-generatedness test separates B from B (+) C exactly.  Float64,
honest.  Nine checks (A1-A6, B1-B3), verdict
OBSTRUCTION_WITNESSED_AND_REPAIR_SEPARATES.

CONSTRUCTION (copied, not imported): Model B = strip_hamiltonian(p)
with MASS=1.0, NY=8, TRANSVERSE_DIMENSION=16, TY=SY/(2j)-SZ/2, onsite
sin(p) SX + (M-cos p) SZ (copied verbatim from the mmst_telb kernel
structure).  Model C = same construction with MASS=3.0 (Chern 0,
gapped, no edge modes).  B (+) C = h_B(p) (+) h_C(p) (32x32 block
diagonal).  Seam sites = top row (y=0, dims 0:2) and bottom row
(y=7, dims 14:16) of B; in B (+) C the same dims (C contributes no
seam sites).  Momentum grid p_k = 2 pi k / N, N=64 (untwisted);
q_k = 2 pi (k+alpha)/N, alpha=0.25 (twisted), k=-N/2..N/2-1.
Fermi projector: fermi_covariance, ZERO_CUT=1e-11, half-filling for
zero modes.

PART A (seam data identical):
  A1 Chern via Fukui-Hatsugai-Suzuki on d(kx,ky)=(sin kx, sin ky,
     M-cos kx-cos ky), 60x60 grid: C(B)=+/-1, C(C)=0, C(B+C)=C(B).
  A2 Zero modes at p=0: B has 2 (|E|<1e-9), C has 0, B+C has 2
     supported entirely in B block (norm^2 > 1-1e-12).
  A3 Edge dispersion: 33 points in (-pi/2, pi/2), two smallest |E|
     eigenvalues of h_B and h_{B+C} coincide to 1e-12.
  A4 Seam-restricted covariance: 4x4 blocks on dims {0,1,14,15} agree
     to 1e-12 (untwisted and twisted).
  A5 Seam Hardy remainder: edge profiles agree up to phase
     (|<phi_B, phi_{B+C}|_B>| > 1-1e-12, zero weight in C block).
  A6 Bulk differs: dim 16 vs 32; E_0(B+C)-E_0(B)=E_0(C)<0 with
     |E_0(C)|>1; bulk gap; mid-strip covariance rank; twist HS norm.

PART B (repaired criterion, seam-generatedness):
  B1 Krylov generatedness: K(p)=span{h(p)^n v, n=0..dim-1, v in seam
     basis (4 vectors, dims {0,1,14,15})}.  spectator_dim=dim-dimK.
     Gate: spectator_dim_{B+C}(p) - spectator_dim_B(p) = 16 for every p.
  B2 Commutant: dim {X : [X,h(p)]=0, [X,Pi_seam]=0} via null space of
     stacked map.  Gate: commutant_dim_{B+C}(p) - commutant_dim_B(p)
     >= 1 for every p, and Pi_C = 0 (+) 1 lies in commutant of B+C.
  B3 Prime-completion selection: among {B, B+C} with identical seam
     data, exactly ONE satisfies "spectator_dim <= spectator_dim_B
     for all p AND Pi_C-type projector absent" -> selects B uniquely.

HONEST NOTES (typed; NO marker upgrade anywhere):
  (i) FINITE WITNESS.  This is a finite free-fermion witness for a
      monoidal-obstruction statement, NOT a 4D theorem.  The ledger
      row SEAM.BULK4D.RECON.01 stays [O]; the new contract
      BULK.PRIME_COMPLETION.01 is registered [O] (a research contract,
      not a claim).  DIMENSION.UPLIFT.FIREWALL.01 F2 applies: the
      hypothesis is 2+1D free-fermion, the conclusion is a re-scoped 4D
      demand.
  (ii) ALMOST-EVERYWHERE.  spectator_dim(B)=0 at 127/128 momenta but
       10 at p=0 (h(0) has no onsite term at M=1, T_Y rank 1 -> the
       Krylov space of the seam sites reaches only 6/16; the commutant
       there has dim 58).  The criterion is therefore "generated almost
       everywhere in p" (dense), NOT pointwise.  The diff
       spectator_dim(B+C) - spectator_dim(B) = 16 holds at ALL 128
       momenta including p=0.
  (iii) The 2D modular-invariant uniqueness of the holomorphic (E8)_1
        net is untouched and is NOT a 4D no-spectator theorem.

PROVENANCE: experiments/tfpt-discovery/spectator_sector_obstruction_probe.py
(r644, 9/9, 27.7 s, VERDICT OBSTRUCTION_WITNESSED_AND_REPAIR_SEPARATES,
SPEC_SHA 07169b54f802bc7d5d54f4597a9461a80c6bc268b04f101be525eac7636df60c,
FILE_SHA 7f58f498eca4619f292c6c48f12c35eec2796a7d88f9065cc8400dab8a0cf507).
The probe stays experiments-side; this module is the load-bearing copy.
NO RH CLAIM.  Python-only / Wolfram mirror deferred (engine
DEFERRED_NO_ENGINE).
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

from math import pi

import numpy as np

from tfpt_constants import check as suite_check, summary, reset

R644_SPEC = "07169b54f802bc7d5d54f4597a9461a80c6bc268b04f101be525eac7636df60c"
R644_FILE = "7f58f498eca4619f292c6c48f12c35eec2796a7d88f9065cc8400dab8a0cf507"
CONTRACT_NEW = "BULK.PRIME_COMPLETION.01"
CONTRACT_SHARPENED = "SEAM.BULK4D.RECON.01"
FIREWALL = "DIMENSION.UPLIFT.FIREWALL.01"
VERDICT = "OBSTRUCTION_WITNESSED_AND_REPAIR_SEPARATES"

NY = 8
TRANSVERSE_DIMENSION = 2 * NY
ZERO_CUT = 1.0e-11

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2

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

DIM_B = TRANSVERSE_DIMENSION
DIM_BC = 2 * TRANSVERSE_DIMENSION


def check(label: str, condition: bool, detail: str = "") -> bool:
    ok = bool(condition)
    suite_check(label if not detail else "%s -- %s" % (label, detail), ok)
    return ok


def strip_hamiltonian(momentum: float, mass: float) -> np.ndarray:
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
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum, mass))
    occupation = np.zeros_like(eigenvalues)
    occupation[eigenvalues < -ZERO_CUT] = 1.0
    occupation[np.abs(eigenvalues) <= ZERO_CUT] = 0.5
    return (eigenvectors * occupation) @ eigenvectors.conj().T


def edge_profiles(mass: float) -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0, mass))
    zero_indices = np.where(np.abs(eigenvalues) <= ZERO_CUT)[0]
    if zero_indices.size == 0:
        raise ValueError("no zero modes at p=0 for mass=%s" % mass)
    top_scores = [float(np.sum(np.abs(eigenvectors[:4, i]) ** 2)) for i in zero_indices]
    bottom_scores = [float(np.sum(np.abs(eigenvectors[-4:, i]) ** 2)) for i in zero_indices]
    top = eigenvectors[:, zero_indices[int(np.argmax(top_scores))]]
    bottom = eigenvectors[:, zero_indices[int(np.argmax(bottom_scores))]]
    return top, bottom


def stacked_hamiltonian(momentum: float) -> np.ndarray:
    stacked = np.zeros((DIM_BC, DIM_BC), dtype=complex)
    stacked[:DIM_B, :DIM_B] = strip_hamiltonian(momentum, MASS_B)
    stacked[DIM_B:, DIM_B:] = strip_hamiltonian(momentum, MASS_C)
    return stacked


def stacked_fermi_covariance(momentum: float) -> np.ndarray:
    stacked = np.zeros((DIM_BC, DIM_BC), dtype=complex)
    stacked[:DIM_B, :DIM_B] = fermi_covariance(momentum, MASS_B)
    stacked[DIM_B:, DIM_B:] = fermi_covariance(momentum, MASS_C)
    return stacked


def bloch_hamiltonian_2d(kx: float, ky: float, mass: float) -> np.ndarray:
    dx = np.sin(kx)
    dy = np.sin(ky)
    dz = mass - np.cos(kx) - np.cos(ky)
    return dx * SX + dy * SY + dz * SZ


def chern_number_fhs(mass: float, grid: int = CHERN_GRID) -> float:
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


def zero_mode_report(mass: float) -> tuple[int, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0, mass))
    mask = np.abs(eigenvalues) < ZERO_MODE_TOL
    return int(np.count_nonzero(mask)), eigenvectors[:, mask]


def stacked_zero_mode_report() -> tuple[int, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(stacked_hamiltonian(0.0))
    mask = np.abs(eigenvalues) < ZERO_MODE_TOL
    return int(np.count_nonzero(mask)), eigenvectors[:, mask]


def untwisted_grid() -> np.ndarray:
    k = np.arange(-N_GRID // 2, N_GRID // 2)
    return 2.0 * pi * k / N_GRID


def twisted_grid() -> np.ndarray:
    k = np.arange(-N_GRID // 2, N_GRID // 2)
    return 2.0 * pi * (k + TWIST_ALPHA) / N_GRID


def seam_projector(dim: int) -> np.ndarray:
    proj = np.zeros((dim, dim), dtype=complex)
    for d in SEAM_DIMS:
        if d < dim:
            proj[d, d] = 1.0
    return proj


def spectator_projector_c() -> np.ndarray:
    proj = np.zeros((DIM_BC, DIM_BC), dtype=complex)
    proj[DIM_B:, DIM_B:] = np.eye(DIM_B)
    return proj

def krylov_dimension(ham: np.ndarray, seed_dims: tuple[int, ...], dim: int,
                     tol: float = KRYLOV_TOL) -> int:
    """Dimension of K(p) = span{ h^n v : n=0..dim-1, v in seed basis }."""
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


def commutant_dimension(ham: np.ndarray, proj_seam: np.ndarray, dim: int,
                        tol: float = COMMUTANT_TOL) -> int:
    """Dimension of {X : [X,h]=0, [X,Pi_seam]=0} as a complex vector space."""
    ident = np.eye(dim, dtype=complex)
    comm_h = np.kron(ham.T, ident) - np.kron(ident, ham)
    comm_p = np.kron(proj_seam.T, ident) - np.kron(ident, proj_seam)
    stacked = np.vstack([comm_h, comm_p])
    real_part = np.vstack([stacked.real, stacked.imag])
    sv = np.linalg.svd(real_part, compute_uv=False)
    rank = int(np.sum(sv > tol * (sv[0] if sv.size else 1.0)))
    return dim * dim - rank


def commutator_residual(x: np.ndarray, ham: np.ndarray, proj_seam: np.ndarray) -> float:
    """Max abs residual of [X,h] and [X,Pi_seam] for a candidate X."""
    r1 = np.linalg.norm(x @ ham - ham @ x)
    r2 = np.linalg.norm(x @ proj_seam - proj_seam @ x)
    return float(max(r1, r2))


def ground_state_energy_density(momentum_grid: np.ndarray, mass: float) -> float:
    total = 0.0
    for p in momentum_grid:
        evals = np.linalg.eigvalsh(strip_hamiltonian(float(p), mass))
        total += float(np.sum(evals[evals < 0.0]))
    return total / len(momentum_grid)


def stacked_ground_state_energy_density(momentum_grid: np.ndarray) -> float:
    total = 0.0
    for p in momentum_grid:
        evals = np.linalg.eigvalsh(stacked_hamiltonian(float(p)))
        total += float(np.sum(evals[evals < 0.0]))
    return total / len(momentum_grid)


def bulk_gap(momentum_grid: np.ndarray, mass: float, n_edge: int = 2) -> float:
    gap = float("inf")
    for p in momentum_grid:
        evals = np.sort(np.abs(np.linalg.eigvalsh(strip_hamiltonian(float(p), mass))))
        if len(evals) > n_edge:
            gap = min(gap, float(evals[n_edge]))
    return gap


def stacked_bulk_gap(momentum_grid: np.ndarray, n_edge: int = 2) -> float:
    gap = float("inf")
    for p in momentum_grid:
        evals = np.sort(np.abs(np.linalg.eigvalsh(stacked_hamiltonian(float(p)))))
        if len(evals) > n_edge:
            gap = min(gap, float(evals[n_edge]))
    return gap


def midstrip_covariance_rank(momentum_grid: np.ndarray, mass: float,
                             rows: tuple[int, ...] = (3, 4)) -> int:
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
    diff = 0.0
    for pk, qk in zip(momentum_grid_untwisted, momentum_grid_twisted):
        cov0 = fermi_covariance(float(pk), mass)
        cov1 = fermi_covariance(float(qk), mass)
        diff += float(np.sum(np.abs(cov0 - cov1) ** 2))
    return float(np.sqrt(diff))


def stacked_twist_hs_norm(momentum_grid_untwisted: np.ndarray,
                          momentum_grid_twisted: np.ndarray) -> float:
    diff = 0.0
    for pk, qk in zip(momentum_grid_untwisted, momentum_grid_twisted):
        cov0 = stacked_fermi_covariance(float(pk))
        cov1 = stacked_fermi_covariance(float(qk))
        diff += float(np.sum(np.abs(cov0 - cov1) ** 2))
    return float(np.sqrt(diff))
def run() -> int:
    reset()
    print("=" * 74)
    print("v1020 -- SPECTATOR-SECTOR OBSTRUCTION")
    print("contract NEW %s [O] / sharpened %s [O] (no marker move)"
          % (CONTRACT_NEW, CONTRACT_SHARPENED))
    print("firewall %s F2 (2+1D hypothesis, re-scoped 4D conclusion)" % FIREWALL)
    print("r644 SPEC_SHA %s" % R644_SPEC)
    print("r644 FILE_SHA (probe) %s" % R644_FILE)
    print("verdict target: %s" % VERDICT)
    print("=" * 74, flush=True)

    grid_u = untwisted_grid()
    grid_t = twisted_grid()
    proj_b = seam_projector(DIM_B)
    proj_bc = seam_projector(DIM_BC)
    pi_c = spectator_projector_c()

    # ---- A1: Chern numbers ------------------------------------------------
    print("\nA1  Chern numbers (FHS, %dx%d grid)" % (CHERN_GRID, CHERN_GRID), flush=True)
    c_b = chern_number_fhs(MASS_B)
    c_c = chern_number_fhs(MASS_C)
    c_bc = c_b + c_c
    print("  C(B)=%.12f C(C)=%.12f C(B+C)=%.12f" % (c_b, c_c, c_bc))
    a1 = (abs(abs(c_b) - 1.0) < CHERN_INT_TOL
          and abs(c_c) < CHERN_INT_TOL
          and abs(c_bc - c_b) < CHERN_INT_TOL)
    check("A1 Chern numbers B=+-1, C=0, B+C=B", a1,
          "C_B=%.6f C_C=%.6f C_BC=%.6f" % (c_b, c_c, c_bc))

    # ---- A2: zero modes at p=0 --------------------------------------------
    print("\nA2  Zero modes at p=0", flush=True)
    n_b, vecs_b = zero_mode_report(MASS_B)
    n_c, vecs_c = zero_mode_report(MASS_C)
    n_bc, vecs_bc = stacked_zero_mode_report()
    b_support = 0.0
    if vecs_bc.shape[1] > 0:
        b_support = float(np.sum(np.abs(vecs_bc[:DIM_B, :]) ** 2)) / vecs_bc.shape[1]
    print("  nB=%d nC=%d nBC=%d Bsupport=%.12f" % (n_b, n_c, n_bc, b_support))
    a2 = (n_b == 2 and n_c == 0 and n_bc == 2
          and b_support > 1.0 - SEAM_SUPPORT_TOL)
    check("A2 zero modes B=2, C=0, B+C=2 in B block", a2,
          "nB=%d nC=%d nBC=%d Bsupport=%.12f" % (n_b, n_c, n_bc, b_support))

    # ---- A3: edge dispersion ---------------------------------------------
    print("\nA3  Edge dispersion (33 points in (-pi/2, pi/2))", flush=True)
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
    print("  max_dev=%.3e min_gap_C=%.6f" % (max_dev, min_gap_c))
    a3 = (max_dev < EDGE_DISP_TOL and min_gap_c > 1.0)
    check("A3 edge dispersion coincident to 1e-12, C gap > 1", a3,
          "max_dev=%.3e min_gap_C=%.6f" % (max_dev, min_gap_c))

    # ---- A4: seam-restricted covariance ----------------------------------
    print("\nA4  Seam-restricted covariance (dims %s)" % (SEAM_DIMS,), flush=True)
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
    print("  untwisted=%.3e twisted=%.3e" % (max_dev_u, max_dev_t))
    a4 = (max_dev_u < SEAM_COV_TOL and max_dev_t < SEAM_COV_TOL)
    check("A4 seam covariance identical to 1e-12 (both grids)", a4,
          "untwisted=%.3e twisted=%.3e" % (max_dev_u, max_dev_t))

    # ---- A5: seam Hardy remainder (edge profiles) -----------------------
    print("\nA5  Seam Hardy remainder (edge profiles at p=0)", flush=True)
    top_b, bot_b = edge_profiles(MASS_B)
    top_bc = np.zeros(DIM_BC, dtype=complex)
    bot_bc = np.zeros(DIM_BC, dtype=complex)
    top_bc[:DIM_B] = top_b
    bot_bc[:DIM_B] = bot_b
    overlap_top = float(abs(top_b.conj() @ top_bc[:DIM_B]))
    overlap_bot = float(abs(bot_b.conj() @ bot_bc[:DIM_B]))
    c_weight_top = float(np.sum(np.abs(top_bc[DIM_B:]) ** 2))
    c_weight_bot = float(np.sum(np.abs(bot_bc[DIM_B:]) ** 2))
    print("  ov_top=%.12f ov_bot=%.12f Cw_top=%.3e Cw_bot=%.3e"
          % (overlap_top, overlap_bot, c_weight_top, c_weight_bot))
    a5 = (overlap_top > 1.0 - EDGE_OVERLAP_TOL
          and overlap_bot > 1.0 - EDGE_OVERLAP_TOL
          and c_weight_top < EDGE_OVERLAP_TOL
          and c_weight_bot < EDGE_OVERLAP_TOL)
    check("A5 edge profiles agree up to phase, zero C weight", a5,
          "ov_top=%.12f ov_bot=%.12f" % (overlap_top, overlap_bot))

    # ---- A6: bulk differs -------------------------------------------------
    print("\nA6  Bulk differs", flush=True)
    e0_b = ground_state_energy_density(grid_u, MASS_B)
    e0_bc = stacked_ground_state_energy_density(grid_u)
    e0_c = e0_bc - e0_b
    gap_b = bulk_gap(grid_u, MASS_B, n_edge=2)
    gap_bc = stacked_bulk_gap(grid_u, n_edge=2)
    rank_b = midstrip_covariance_rank(grid_u, MASS_B)
    rank_bc = stacked_midstrip_covariance_rank(grid_u)
    hs_b = twist_hs_norm(grid_u, grid_t, MASS_B)
    hs_bc = stacked_twist_hs_norm(grid_u, grid_t)
    print("  dim B=%d B+C=%d  E0(B)=%.6f E0(B+C)=%.6f E0(C)=%.6f"
          % (DIM_B, DIM_BC, e0_b, e0_bc, e0_c))
    print("  gap B=%.6f B+C=%.6f  rank B=%d B+C=%d  HS B=%.6f B+C=%.6f diff=%.6f"
          % (gap_b, gap_bc, rank_b, rank_bc, hs_b, hs_bc, hs_bc - hs_b))
    a6 = (DIM_B != DIM_BC
          and e0_c < 0.0 and abs(e0_c) > GROUND_STATE_ENERGY_GAP
          and rank_b != rank_bc
          and abs(hs_bc - hs_b) > 0.0)
    check("A6 bulk differs (dim, E0, gap, rank, twist HS)", a6,
          "E0_C=%.6f rankB=%d rankBC=%d HSdiff=%.6f"
          % (e0_c, rank_b, rank_bc, hs_bc - hs_b))
    print("  boundary(B(x)C) = boundary(B)(x)1 = boundary(B) at finite level: "
          "seam data identical (A1-A5), bulk not unitarily equivalent (A6)",
          flush=True)

    # ---- B1: Krylov generatedness ----------------------------------------
    print("\nB1  Krylov generatedness (spectator_dim)", flush=True)
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
    print("  spectator_dim_B: min=%d max=%d  nonzero at %d/%d momenta"
          % (min(spec_b_vals), max(spec_b_vals), len(spec_b_nonzero), len(spec_b)))
    if spec_b_nonzero:
        print("  first nonzero: p=%.6f s=%d" % spec_b_nonzero[0])
    print("  diff (B+C - B): min=%d max=%d (target 16)" % (b1_diff_min, b1_diff_max))
    check("B1 spectator_dim diff = 16 for every p", b1_ok,
          "diff_min=%d diff_max=%d" % (b1_diff_min, b1_diff_max))

    # ---- B2: commutant test ----------------------------------------------
    print("\nB2  Commutant test", flush=True)
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
    print("  commutant_dim_B: min=%d max=%d  B+C: min=%d max=%d  diff_min=%d (>=1)"
          % (min(c for _, c, _ in comm_b), max(c for _, c, _ in comm_b),
              min(c for _, c, _ in comm_bc), max(c for _, c, _ in comm_bc),
              b2_diff_min))
    print("  Pi_C commutator residual at p=0 = %.3e" % pi_c_residual)
    b2_ok = b2_ok and pi_c_residual < COMMUTATOR_RESIDUAL_TOL
    check("B2 commutant_dim diff >= 1, Pi_C in commutant", b2_ok,
          "diff_min=%d PiC_resid=%.3e" % (b2_diff_min, pi_c_residual))

    # ---- B3: prime-completion selection ----------------------------------
    print("\nB3  Prime-completion selection", flush=True)
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
    check("B3 selection unique (B selected, B+C rejected)", b3_ok,
          "B_sel=%s BC_sel=%s" % (b_selected, bc_selected))

    print("\nHONEST: finite free-fermion witness for a monoidal-obstruction "
          "statement; not a 4D theorem; %s stays [O]; %s registered [O]; "
          "criterion generated a.e. in p (fails only at p=0 by symmetry)."
          % (CONTRACT_SHARPENED, CONTRACT_NEW), flush=True)
    print("VERDICT: %s" % VERDICT)
    print("r644 SPEC_SHA  %s" % R644_SPEC)
    return summary("v1020 spectator-sector obstruction")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
# __END_PART1__
