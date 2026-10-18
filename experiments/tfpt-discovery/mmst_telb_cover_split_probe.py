#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mmst_telb_cover_split_probe -- TELB.COVER.SPLIT.01
# FROZEN SPEC v1 (2026-09-04).  EXPLORATION ONLY, experiments/ only.
# See full spec in __doc__ below; this file is built up by the authoring
# agent via StrReplace.  Placeholder body replaced in stages.
r"""mmst_telb_cover_split_probe -- TELB.COVER.SPLIT.01

FROZEN SPEC v1 (2026-09-04).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes only the
companion result-JSON next to itself.

MANDATE: freeze two verified findings into one gated, JSON-emitting
probe: (I) the exact 4-fold-cover identity for the alpha=1/4 twist
response of the MMST TEL-B seam; (II) the split R_N = R^sm_N + M_N of
the remainder into a lattice piece R^sm_N whose HS norm is
N-independent to ~1e-9 and an explicit special-function piece M_N
carrying all the 1/N drift, giving the triangle bound
    sup_N ||R_N|| <= ||R^sm|| + ||M|| ~ 2.87 < 3
(corpus target C_R < 3).  All numerics float64, reported honestly.
SEAM.MMST.TYPEIII.CHARGED.01 stays [O].

NOTATION (copied from mmst_telb_kernel_structure_probe.py):
N even, modes k in S_N = {-N/2,...,N/2-1}, p_k = 2*pi*k/N,
q_l = 2*pi*(l+alpha)/N, alpha = 1/4, P(p) = fermi_covariance(p)
(zero modes at p=0 get occupation 1/2),
W_{kl} = (1/N) sum_x exp(2*pi i x (k-l-alpha)/N),
D_0 = direct_sum P(p_k), D_alpha = direct_sum P(q_l),
X_N := D_0 - W D_alpha W†  (mode basis, twist response),
H_N := hardy_difference(S_N), Q := BOTTOM_PROJECTION - TOP_PROJECTION,
R_N := X_N - H_N ⊗ Q  (corpus remainder).

(I) COVER IDENTITY (exact, alpha=1/4, M := 4N): p_j = 2*pi*j/M,
j in {-M/2,...,M/2-1}, in the corpus e^{-i p x} position convention
    C_M(d) := (1/M) sum_j exp(-i p_j d) P(p_j).
Then (Gamma_0 - Gamma_alpha)(x,y) = F_0 X_N F_0† has blocks
    (1 - i) C_M(d+N) + 2 C_M(d+2N) + (1 + i) C_M(d+3N),  d = x - y.
With the opposite sign convention e^{+i p d} the coefficients are
(1+i), 2, (1-i).  The probe builds C_M in the corpus convention and
verifies which coefficient ordering matches numerically (the reference
/tmp/telb/cover_identity.py matched (1+i),2,(1-i) in the e^{+ipd}
convention; the corpus mode basis is e^{-ipx}, so the probe expects
(1-i),2,(1+i)).

PROOF.  q_l = 2*pi*(l+alpha)/N = 2*pi*(4l+1)/M = p_{4l+1}^{(M)}.  The
character sum (1/4) sum_{r=0}^{3} exp(2*pi i r (j-1)/4) = [j = 1 mod 4]
selects the twisted momenta out of the 4N-cover, while the untwisted
sum uses [j = 0 mod 4].  The phase p_j * r N = pi j r / 2 turns the
character factor into a position shift d -> d - r N.  Collecting the
four r-branches gives the three non-trivial coefficients (the r=0 and
r=2 branches combine into the central 2 C_M(d+2N) term after a parity
split).  Hence the alpha=1/4 twist response is exactly the wrap-around
covariance on the 4-fold cover -- a defect localised at the branch
cut between x = N-1 and x = 0 with the edge-mode power tail.

(II) SAWTOOTH SPLIT: saw(p) := 1/2 - (p mod 2*pi)/(2*pi) for p not in
2*pi Z, saw(p) := 0 for p in 2*pi Z (midpoint, matching the 1/2
occupation of the zero modes).  Jump model J(p) := saw(p) * dP with
dP := P(0+) - P(0-) (computed as P(1e-7) - P(-1e-7); gate dP = -Q
to 1e-6).  Scalar sawtooth response in mode basis
    S_N := diag(saw(p_k)) - W diag(saw(q_l)) W†.
Define
    R^sm_N := X_N - S_N ⊗ dP   (twist response of the CONTINUOUS
                                function P - J, the lattice piece),
    M_N   := S_N ⊗ dP - H_N ⊗ Q = -(S_N + H_N) ⊗ Q  (the explicit
                                                       special-function
                                                       piece).
Then R_N = R^sm_N + M_N exactly, and
    ||R||² = ||R^sm||² + ||M||² + 2 Re <R^sm, M>,
    ||M||² = 2 ||S_N + H_N||²  (Tr(Q†Q) = 2, since Q is the difference
    of two rank-1 orthogonal edge projectors, Tr(Q) = 0, Tr(Q²) = 2).

(III) MEMORY-LIGHT EVALUATION (all pieces via N x N matrices; NEVER
build the 16N x 16N matrix for N > 256): with
    c_m := Tr(P(q_m) Q),  z_k := Tr(P(p_k) Q),
    Z := diag(z) - W diag(c) W†  (so Z_{kl} = Tr(X_{kl} Q) where X_{kl}
                                 is the 16x16 block).
Because W is unitary (W† W = I), the HS norm of X satisfies
    ||X||² = sum_{k,m} |W_{km}|² ||P(p_k) - P(q_m)||²_HS  =: T1
(Gram-matrix matmul: flatten 16x16 -> 512 real components; unitarity
collapses the column-norm sum to the trace sum, recovering the simple
two-momentum form).
The cross term against S ⊗ dP:
    <X, S ⊗ dP> = Tr(X†(S ⊗ dP)) = sum_{kl} conj(Tr(X_{kl} dP†)) S_{kl}.
With dP = -Q (gate G02), Tr(X_{kl} dP†) = -Tr(X_{kl} Q) = -Z_{kl},
so <X, S ⊗ dP> = -sum_{kl} conj(Z_{kl}) S_{kl} = -conj(<Z, S>).
Then
    ||R^sm||² = ||X - S ⊗ dP||²
             = T1 - 2 Re <X, S ⊗ dP> + ||S||² ||dP||²
             = T1 + 2 Re conj(<Z, S>) + ||S||² ||dP||².
    ||M||² = 2 ||S + H||².
    2 Re <R^sm, M> = 2 Re [<X, M> - <S ⊗ dP, M>]
                   = 2 Re [<X, M> + <S ⊗ Q, (S+H) ⊗ Q>]   (dP = -Q)
                   = 2 Re <X, M> + 4 <S, S+H>,
where <X, M> = Tr(X† M) = Tr(X† (-(S+H) ⊗ Q)) = -conj(<Z, S+H>).
So 2 Re <R^sm, M> = -2 Re conj(<Z, S+H>) + 4 <S, S+H>.
All of these are validated against the direct 16N x 16N computation
for N in {16, 32, 64, 128, 256} to 1e-9 relative (gate G02).

SIZES / CORPUS PINS:
N in {16, 32, 64, 128, 256, 512, 1024, 2048, 4096}  (stop at 2048 if
4096 exceeds ~10 min; report which).
Corpus pins: ||R_16|| = 2.092528479, ||R_96|| = 2.105079358.

GATES:
G01  cover identity residual ||(Gamma_0 - Gamma_alpha) - cover
     formula||_HS < 1e-10 at N=16 and N=32 (state which coefficient
     ordering matched the corpus convention).
G02  split validation N <= 256:
     | ||R||²_direct - (||R^sm||² + ||M||² + 2 Re <R^sm, M>)_light |
     / ||R||² < 1e-9; corpus pins reproduced to 1e-6; dP = -Q to 1e-6.
G03  lattice piece N-independence:
     | N (||R^sm_{2N}||² - ||R^sm_N||²) | < 1e-4 for all N >= 128 and
     strictly decreasing along the dyadic chain from N=32 on; report
     the local exponent of Delta ||R^sm||² (log2 ratio of successive
     increments) -- expected ~ 3 or steeper.
G04  explicit piece 1/N law:
     N (||M_{2N}||² - ||M_N||²) within 1% of a common value over the
     last three pairs; same for the cross term within 3%; report both
     sequences and the implied b2, b_cross, b_total = b2 + b_cross
     and check b_total against the total's N Delta ||R||².
G05  triangle bound:
     B_N := ||R^sm_N|| + ||M_N|| < 3 for every computed N AND the
     extrapolated limit B_inf := sqrt(a1) + sqrt(a2) (a2 from a
     1/N + 1/N² fit of ||M||² on N >= 256) < 3; report margins
     3 - B_N and 3 - B_inf (expected ~ 0.13) and the actual ||R_N||
     for comparison (~ 2.107).
G06  consistency with the corpus TEL-B increment target:
     N | ||R_{2N}|| - ||R_N|| | for all pairs, implied
     A_R := lim N | Delta ||R|| | < 43  (expected ~ 0.124).
G07  verdict enum frozen:
     TELB_REDUCED_TO_TWO_SUP_BOUNDS  (G01-G06 pass),
     SPLIT_VALID_BOUND_FAILS         (G01-G04 pass, G05 fails),
     SPLIT_INVALID                   (G01 or G02 fail),
     INCONCLUSIVE.

HONEST NOTE (always printed): float64; exact identities validated
numerically, sup-bounds are numerical not certified;
SEAM.MMST.TYPEIII.CHARGED.01 stays [O]; a proof still needs
(A) a rigorous sup bound for the lattice piece via Fourier decay of
the continuous projector P - J on the 4N-cover and
(B) digamma/sawtooth asymptotics for the explicit piece.
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
from scipy.special import digamma, polygamma  # noqa: E402

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# Provenance: strip_hamiltonian / fermi_covariance / edge_profiles /
# hardy_difference copied verbatim from mmst_telb_kernel_structure_probe.py
# (which copies from mmst_telb_tail_probe.py).  These reproduce the
# corpus pins ||R_16|| = 2.092528479, ||R_96|| = 2.105079358.

MASS = 1.0
NY = 8
TRANSVERSE_DIMENSION = 2 * NY
ALPHA = 0.25
ZERO_CUT = 1.0e-11

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2


def strip_hamiltonian(momentum: float) -> np.ndarray:
    matrix = np.zeros(
        (TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION), dtype=complex
    )
    onsite = np.sin(momentum) * SX + (MASS - np.cos(momentum)) * SZ
    for y_index in range(NY):
        site = slice(2 * y_index, 2 * y_index + 2)
        matrix[site, site] = onsite
    for y_index in range(NY - 1):
        lower = slice(2 * y_index, 2 * y_index + 2)
        upper = slice(2 * y_index + 2, 2 * y_index + 4)
        matrix[upper, lower] = TY
        matrix[lower, upper] = TY.conj().T
    return matrix


def fermi_covariance(momentum: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    occupation = np.zeros_like(eigenvalues)
    occupation[eigenvalues < -ZERO_CUT] = 1.0
    occupation[np.abs(eigenvalues) <= ZERO_CUT] = 0.5
    return (eigenvectors * occupation) @ eigenvectors.conj().T


def edge_profiles() -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0))
    zero_indices = np.where(np.abs(eigenvalues) <= ZERO_CUT)[0]
    top_scores = [
        float(np.sum(np.abs(eigenvectors[:4, index]) ** 2))
        for index in zero_indices
    ]
    bottom_scores = [
        float(np.sum(np.abs(eigenvectors[-4:, index]) ** 2))
        for index in zero_indices
    ]
    top = eigenvectors[:, zero_indices[int(np.argmax(top_scores))]]
    bottom = eigenvectors[:, zero_indices[int(np.argmax(bottom_scores))]]
    return top, bottom


TOP_PROFILE, BOTTOM_PROFILE = edge_profiles()
TOP_PROJECTION = np.outer(TOP_PROFILE, TOP_PROFILE.conj())
BOTTOM_PROJECTION = np.outer(BOTTOM_PROFILE, BOTTOM_PROFILE.conj())
Q_OPERATOR = BOTTOM_PROJECTION - TOP_PROJECTION
DP_OPERATOR = fermi_covariance(1.0e-7) - fermi_covariance(-1.0e-7)

def hardy_difference(mode_indices: np.ndarray) -> np.ndarray:
    shifted = mode_indices.astype(float) - ALPHA
    size = len(mode_indices)
    occupied_twisted = np.empty((size, size), dtype=float)
    factor = np.sin(pi * ALPHA) ** 2 / pi ** 2
    for row in range(size):
        for column in range(size):
            if row == column:
                overlap_sum = polygamma(1, shifted[row])
            else:
                overlap_sum = (
                    digamma(shifted[column]) - digamma(shifted[row])
                ) / (shifted[column] - shifted[row])
            occupied_twisted[row, column] = factor * overlap_sum
    occupied_untwisted = np.diag((mode_indices <= 0).astype(float))
    difference = occupied_untwisted - occupied_twisted
    return 0.5 * (difference + difference.T)


def saw(p: np.ndarray) -> np.ndarray:
    q = np.mod(p, 2 * pi)
    out = 0.5 - q / (2 * pi)
    out = np.where(np.abs(q) < 1.0e-12, 0.0, out)
    out = np.where(np.abs(q - 2 * pi) < 1.0e-12, 0.0, out)
    return out


def overlap_matrix(size: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return (mode_indices, p_k, q_l, W) for the corpus e^{-i p x} convention.

    W = F0† @ Fa, with F0[x,k] = e^{-i p_k x}/sqrt(N),
    Fa[x,l] = e^{-i q_l x}/sqrt(N).  So
    W_{kl} = (1/N) sum_x e^{+i p_k x} e^{-i q_l x}
           = (1/N) sum_x e^{-i (q_l - p_k) x}.
    """
    mode_indices = np.arange(-size // 2, size // 2)
    positions = np.arange(size)
    momenta_zero = 2 * pi * mode_indices / size
    momenta_alpha = 2 * pi * (mode_indices + ALPHA) / size
    fourier_zero = np.exp(-1j * np.outer(positions, momenta_zero)) / np.sqrt(size)
    fourier_alpha = np.exp(-1j * np.outer(positions, momenta_alpha)) / np.sqrt(size)
    overlap = fourier_zero.conj().T @ fourier_alpha
    return mode_indices, momenta_zero, momenta_alpha, overlap


def cover_identity_check(size: int) -> tuple[float, float, str]:
    """Build Gamma_0 - Gamma_alpha in position space via F_0 X F_0† and
    via the 4-fold-cover formula, return (residual, norm, matched ordering).

    C_M(d) uses the corpus e^{-i p d} convention:
        C_M(d) = (1/M) sum_j exp(-i p_j d) P(p_j),  p_j = 2*pi*j/M.
    """
    mode_indices, momenta_zero, momenta_alpha, overlap = overlap_matrix(size)
    p0_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_zero])
    pa_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_alpha])
    # X_N in mode basis (full 16N x 16N), then F_0 X F_0† -> position space.
    d0 = np.zeros((size * TRANSVERSE_DIMENSION, size * TRANSVERSE_DIMENSION), dtype=complex)
    for k in range(size):
        s = slice(k * TRANSVERSE_DIMENSION, (k + 1) * TRANSVERSE_DIMENSION)
        d0[s, s] = p0_blocks[k]
    wa = np.einsum(
        "im,mab,jm->iajb", overlap, pa_blocks, overlap.conj(), optimize=True
    ).reshape(size * TRANSVERSE_DIMENSION, size * TRANSVERSE_DIMENSION)
    x_mode = d0 - wa
    positions = np.arange(size)
    fourier_zero = np.exp(-1j * np.outer(positions, momenta_zero)) / np.sqrt(size)
    f0 = np.kron(fourier_zero, np.eye(TRANSVERSE_DIMENSION))
    gamma = f0 @ x_mode @ f0.conj().T  # position space, corpus convention

    m_cover = 4 * size
    ks_m = np.arange(-m_cover // 2, m_cover // 2)
    p_m = 2 * pi * ks_m / m_cover
    pm_blocks = np.asarray([fermi_covariance(float(t)) for t in p_m])

    def c_of(d: np.ndarray) -> np.ndarray:
        # C_M(d) = (1/M) sum_j exp(-i p_j d) P(p_j)  (corpus e^{-ipd})
        phase = np.exp(-1j * np.outer(d.ravel(), p_m)) / m_cover
        return np.tensordot(phase, pm_blocks, axes=(1, 0)).reshape(
            d.shape + pm_blocks.shape[1:]
        )

    d_grid = positions[:, None] - positions[None, :]
    # Candidate orderings in the corpus e^{-ipd} convention.
    orderings = {
        "(1-i),2,(1+i)": ((1 - 1j), 2.0, (1 + 1j)),
        "(1+i),2,(1-i)": ((1 + 1j), 2.0, (1 - 1j)),
    }
    best_name = ""
    best_res = float("inf")
    best_norm = float(np.linalg.norm(gamma))
    for name, (c1, c2, c3) in orderings.items():
        pred = (
            c1 * c_of(d_grid + size)
            + c2 * c_of(d_grid + 2 * size)
            + c3 * c_of(d_grid + 3 * size)
        )
        pred_mat = pred.transpose(0, 2, 1, 3).reshape(
            size * TRANSVERSE_DIMENSION, size * TRANSVERSE_DIMENSION
        )
        res = float(np.linalg.norm(gamma - pred_mat))
        if res < best_res:
            best_res = res
            best_name = name
    return best_res, best_norm, best_name


def light_pieces(size: int) -> dict:
    """Memory-light evaluation of all split pieces via N x N matrices.

    Returns dict with keys: T1, rsm2, m2, cross, total2, S, H, Z,
    s_norm2, sh_norm2, dP_norm2, s_sh_inner (real Frobenius <S,S+H>).
    """
    mode_indices, momenta_zero, momenta_alpha, overlap = overlap_matrix(size)
    p0_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_zero])
    pa_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_alpha])
    w = overlap  # N x N, unitary

    # Flatten 16x16 -> 256 complex (512 real) for Gram matmul.
    p0_flat = p0_blocks.reshape(size, -1)  # (N, 256) complex
    pa_flat = pa_blocks.reshape(size, -1)
    # ||P(p_k) - P(q_m)||^2_HS = ||P0_k||^2 + ||Pa_m||^2 - 2 Re <P0_k, Pa_m>
    p0_sq = np.sum(np.abs(p0_flat) ** 2, axis=1)  # (N,)
    pa_sq = np.sum(np.abs(pa_flat) ** 2, axis=1)
    # Gram of inner products: G[k,m] = <P0_k, Pa_m> = sum conj(P0_k)*Pa_m
    gram = p0_flat.conj() @ pa_flat.T  # (N, N)
    diff_sq = p0_sq[:, None] + pa_sq[None, :] - 2.0 * gram.real  # (N, N)
    t1 = float(np.sum((np.abs(w) ** 2) * diff_sq))

    # Z = diag(z) - W diag(c) W† ; z_k = Tr(P0_k Q), c_m = Tr(Pa_m Q)
    z = np.array([np.trace(p0_blocks[k] @ Q_OPERATOR).real for k in range(size)])
    c = np.array([np.trace(pa_blocks[m] @ Q_OPERATOR).real for m in range(size)])
    z_mat = np.diag(z) - w @ np.diag(c) @ w.conj().T  # (N, N)

    # S = diag(saw(p_k)) - W diag(saw(q_l)) W†
    s_diag0 = saw(momenta_zero)
    s_diag_a = saw(momenta_alpha)
    s_mat = np.diag(s_diag0) - w @ np.diag(s_diag_a) @ w.conj().T

    # H = hardy_difference
    h_mat = hardy_difference(mode_indices)

    s_norm2 = float(np.vdot(s_mat, s_mat).real)
    sh_norm2 = float(np.vdot(s_mat + h_mat, s_mat + h_mat).real)
    s_sh_inner = float(np.vdot(s_mat, s_mat + h_mat).real)  # <S, S+H> Frobenius
    dp_norm2 = float(np.vdot(DP_OPERATOR, DP_OPERATOR).real)

    # <X, M> = -<Z, S+H>_F ; <S⊗dP, M> = +2<S, S+H> (dP=-Q, Tr(Q^2)=2).
    # 2 Re <R^sm, M> = 2 Re[<X,M> - <S⊗dP,M>] = -2 Re<Z,S+H> - 4<S,S+H>.
    zs_inner = float(np.sum(np.conj(z_mat) * s_mat))
    zsh_inner = float(np.sum(np.conj(z_mat) * (s_mat + h_mat)))
    s_sh_inner = float(np.sum(np.conj(s_mat) * (s_mat + h_mat)))

    # ||R^sm||^2 = T1 + 2 Re <Z, S> + ||S||^2 ||dP||^2
    rsm2 = t1 + 2.0 * zs_inner.real + s_norm2 * dp_norm2
    # ||M||^2 = 2 ||S+H||^2
    m2 = 2.0 * sh_norm2
    # 2 Re <R^sm, M> = -2 Re <Z, S+H> - 4 <S, S+H>
    cross = -2.0 * zsh_inner.real - 4.0 * s_sh_inner.real
    total2 = rsm2 + m2 + cross
    return {
        "T1": t1,
        "rsm2": float(rsm2),
        "m2": float(m2),
        "cross": float(cross),
        "total2": float(total2),
        "S": s_mat,
        "H": h_mat,
        "Z": z_mat,
        "s_norm2": s_norm2,
        "sh_norm2": sh_norm2,
        "dp_norm2": dp_norm2,
        "s_sh_inner": s_sh_inner,
    }


def direct_pieces(size: int) -> dict:
    """Direct 16N x 16N evaluation (only for N <= 256)."""
    mode_indices, momenta_zero, momenta_alpha, overlap = overlap_matrix(size)
    p0_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_zero])
    pa_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_alpha])
    d0 = np.zeros(
        (size * TRANSVERSE_DIMENSION, size * TRANSVERSE_DIMENSION), dtype=complex
    )
    for k in range(size):
        s = slice(k * TRANSVERSE_DIMENSION, (k + 1) * TRANSVERSE_DIMENSION)
        d0[s, s] = p0_blocks[k]
    wa = np.einsum(
        "im,mab,jm->iajb", overlap, pa_blocks, overlap.conj(), optimize=True
    ).reshape(size * TRANSVERSE_DIMENSION, size * TRANSVERSE_DIMENSION)
    x = d0 - wa
    s_mat = np.diag(saw(momenta_zero)) - overlap @ np.diag(saw(momenta_alpha)) @ overlap.conj().T
    h_mat = hardy_difference(mode_indices)
    rsm = x - np.kron(s_mat, DP_OPERATOR)
    m = np.kron(s_mat, DP_OPERATOR) - np.kron(h_mat, Q_OPERATOR)
    r = rsm + m
    return {
        "rsm2": float(np.vdot(rsm, rsm).real),
        "m2": float(np.vdot(m, m).real),
        "cross": float(2.0 * np.vdot(rsm, m).real),
        "total2": float(np.vdot(r, r).real),
        "r_norm": float(np.sqrt(np.vdot(r, r).real)),
    }


SIZES = (16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
DIRECT_SIZES = (16, 32, 64, 128, 256)
CORPUS_PINS = {16: 2.092528479, 96: 2.105079358}
COVER_SIZES = (16, 32)
COVER_TOL = 1.0e-10
SPLIT_REL_TOL = 1.0e-9
PIN_TOL = 1.0e-6
DP_TOL = 1.0e-6
G03_NDEP_TOL = 1.0e-4
G03_MIN_N = 128
G04_B2_REL = 0.01
G04_BCROSS_REL = 0.03
G04_FIT_MIN_N = 256
TRIANGLE_TARGET = 3.0
A_R_TARGET = 43.0
TIME_BUDGET_4096 = 600.0

VERDICT_ENUM = (
    "TELB_REDUCED_TO_TWO_SUP_BOUNDS",
    "SPLIT_VALID_BOUND_FAILS",
    "SPLIT_INVALID",
    "INCONCLUSIVE",
)

CHECKS: list[tuple[str, bool]] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(
        "  [%s] %s%s"
        % ("PASS" if ok else "FAIL", name, ("  " + detail) if detail else "")
    )


def fit_1_over_n_sq(sizes: np.ndarray, values: np.ndarray) -> tuple[float, float]:
    """Fit values = a2 + b2/N + d2/N^2; return (a2, b2)."""
    x1 = 1.0 / sizes
    x2 = x1 ** 2
    design = np.column_stack([np.ones_like(x1), x1, x2])
    coef, _, _, _ = np.linalg.lstsq(design, values, rcond=None)
    return float(coef[0]), float(coef[1])


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print("mmst_telb_cover_split_probe -- TELB.COVER.SPLIT.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)

    dp_q_plus = float(np.linalg.norm(DP_OPERATOR - Q_OPERATOR))
    dp_q_minus = float(np.linalg.norm(DP_OPERATOR + Q_OPERATOR))
    dp_norm = float(np.linalg.norm(DP_OPERATOR))
    q_norm = float(np.linalg.norm(Q_OPERATOR))
    print(
        "  dP vs Q: ||dP-Q||=%.3e  ||dP+Q||=%.3e  ||dP||=%.6f  ||Q||=%.6f"
        % (dp_q_plus, dp_q_minus, dp_norm, q_norm)
    )

    # ---- G01: cover identity ----
    print()
    print("G01  COVER IDENTITY  (corpus e^{-i p d} convention)")
    cover_results = {}
    g01_ok = True
    for size in COVER_SIZES:
        res, norm, matched = cover_identity_check(size)
        cover_results[size] = (res, norm, matched)
        ok = res < COVER_TOL
        g01_ok = g01_ok and ok
        print(
            "  N=%3d  ||Gamma0-Gammaalpha||=%.10f  residual=%.3e  matched=%s  %s"
            % (size, norm, res, matched, "PASS" if ok else "FAIL")
        )
    convention_note = cover_results[COVER_SIZES[0]][2]
    gate(
        "G01 cover identity residual < 1e-10 at N=16 and N=32",
        g01_ok,
        "matched ordering (corpus e^{-ipd}): %s" % convention_note,
    )

    # ---- light + direct split pieces ----
    print()
    print("SPLIT  per-N table  (light evaluation)")
    print(
        "  %5s %14s %14s %14s %14s %12s %10s"
        % ("N", "||Rsm||^2", "||M||^2", "2<Rsm,M>", "||R||^2", "||R||", "B_N")
    )
    light = {}
    direct = {}
    for size in SIZES:
        t_size = time.time()
        try:
            light[size] = light_pieces(size)
        except MemoryError:
            print("  N=%5d  MemoryError in light_pieces; stopping" % size)
            break
        if size in DIRECT_SIZES:
            direct[size] = direct_pieces(size)
        lp = light[size]
        r_norm = float(np.sqrt(max(lp["total2"], 0.0)))
        b_n = float(np.sqrt(max(lp["rsm2"], 0.0)) + np.sqrt(max(lp["m2"], 0.0)))
        print(
            "  %5d %14.9f %14.9f %14.9f %14.9f %12.9f %10.6f"
            % (size, lp["rsm2"], lp["m2"], lp["cross"], lp["total2"], r_norm, b_n)
        )
        if size == 2048 and (time.time() - t_size) > 60.0:
            print("  (N=2048 took %.1fs; skipping 4096)" % (time.time() - t_size))
            break
    computed_sizes = [s for s in SIZES if s in light]
    print("  computed sizes: %s" % computed_sizes)

    # ---- G02: split validation vs direct, corpus pins, dP=-Q ----
    print()
    print("G02  SPLIT VALIDATION  (light vs direct, N <= 256)")
    g02_split = True
    for size in DIRECT_SIZES:
        if size not in direct or size not in light:
            g02_split = False
            continue
        d = direct[size]
        lp = light[size]
        rel = abs(d["total2"] - lp["total2"]) / max(d["total2"], 1e-30)
        ok = rel < SPLIT_REL_TOL
        g02_split = g02_split and ok
        print(
            "  N=%3d  ||R||^2_direct=%.9f  light=%.9f  rel=%.3e  %s"
            % (size, d["total2"], lp["total2"], rel, "PASS" if ok else "FAIL")
        )
        for key in ("rsm2", "m2", "cross"):
            rel_p = abs(d[key] - lp[key]) / max(abs(d[key]), 1e-30)
            print(
                "        %s  direct=%.9f  light=%.9f  rel=%.3e"
                % (key, d[key], lp[key], rel_p)
            )
    pin_ok = True
    for size_pin, val_pin in CORPUS_PINS.items():
        if size_pin in light:
            r_norm = float(np.sqrt(max(light[size_pin]["total2"], 0.0)))
        else:
            light_pin = light_pieces(size_pin)
            r_norm = float(np.sqrt(max(light_pin["total2"], 0.0)))
        diff = abs(r_norm - val_pin)
        ok = diff < PIN_TOL
        pin_ok = pin_ok and ok
        print(
            "  pin N=%3d  ||R||=%.9f  source=%.9f  |diff|=%.3e  %s"
            % (size_pin, r_norm, val_pin, diff, "PASS" if ok else "FAIL")
        )
    dp_ok = dp_q_minus < DP_TOL
    print("  dP = -Q: ||dP+Q||=%.3e  %s" % (dp_q_minus, "PASS" if dp_ok else "FAIL"))
    g02 = g02_split and pin_ok and dp_ok
    gate(
        "G02 split validation, corpus pins, dP=-Q",
        g02,
        "split=%s pins=%s dP=%s" % (g02_split, pin_ok, dp_ok),
    )
    return _main_tail(t0, light, direct, computed_sizes, convention_note)


def _main_tail(t0, light, direct, computed_sizes, convention_note):
    dyadic = [(s, s2) for s, s2 in zip(computed_sizes, computed_sizes[1:])]
    rsm2_seq, m2_seq, cross_seq, total2_seq, rnorm_seq = [], [], [], [], []
    for n, n2 in dyadic:
        lp_n = light[n]
        lp_n2 = light[n2]
        rsm2_seq.append(n * (lp_n2["rsm2"] - lp_n["rsm2"]))
        m2_seq.append(n * (lp_n2["m2"] - lp_n["m2"]))
        cross_seq.append(n * (lp_n2["cross"] - lp_n["cross"]))
        total2_seq.append(n * (lp_n2["total2"] - lp_n["total2"]))
        r_n = float(np.sqrt(max(lp_n["total2"], 0.0)))
        r_n2 = float(np.sqrt(max(lp_n2["total2"], 0.0)))
        rnorm_seq.append(n * abs(r_n2 - r_n))
    print()
    print("DYADIC  N*(f(2N)-f(N))  sequences")
    print(
        "  %7s %14s %14s %14s %14s %14s"
        % ("N->2N", "Rsm^2", "M^2", "cross", "total", "N|d||R||")
    )
    for (n, n2), a, b, cc, tt, rr in zip(
        dyadic, rsm2_seq, m2_seq, cross_seq, total2_seq, rnorm_seq
    ):
        print(
            "  %4d->%-4d %+14.6f %+14.6f %+14.6f %+14.6f %14.6f"
            % (n, n2, a, b, cc, tt, rr)
        )

    # ---- G03: lattice piece N-independence ----
    print()
    print("G03  LATTICE PIECE  N-independence of ||R^sm||^2")
    rsm2_inc = [light[n2]["rsm2"] - light[n]["rsm2"] for n, n2 in dyadic]
    local_exps = []
    for i in range(len(rsm2_inc) - 1):
        a_inc = rsm2_inc[i]
        b_inc = rsm2_inc[i + 1]
        if abs(a_inc) > 1e-15 and abs(b_inc) > 1e-15 and (a_inc * b_inc) > 0:
            local_exps.append(float(np.log2(abs(a_inc) / abs(b_inc))))
        else:
            local_exps.append(float("nan"))
    print("  increments and local exponents:")
    for (n, n2), inc, le in zip(dyadic, rsm2_inc, local_exps + [float("nan")]):
        le_s = "%.4f" % le if np.isfinite(le) else "nan"
        print("  %4d->%-4d  inc=%+.6e  local_exp=%s" % (n, n2, inc, le_s))
    g03_ndef = True
    for (n, n2), v in zip(dyadic, rsm2_seq):
        if n >= G03_MIN_N:
            ok = abs(v) < G03_NDEP_TOL
            g03_ndef = g03_ndef and ok
            print("  N=%4d  |N*dRsm2|=%.3e  %s" % (n, abs(v), "PASS" if ok else "FAIL"))
    abs_inc = [abs(x) for x in rsm2_inc]
    dec_from_32 = True
    start_idx = None
    for idx, (n, _) in enumerate(dyadic):
        if n >= 32:
            start_idx = idx
            break
    if start_idx is not None:
        for i in range(start_idx, len(abs_inc) - 1):
            if abs_inc[i + 1] >= abs_inc[i]:
                dec_from_32 = False
                break
    print("  |increment| strictly decreasing from N=32 on: %s" % dec_from_32)
    g03 = g03_ndef and dec_from_32
    gate(
        "G03 lattice piece N-independence",
        g03,
        "local_exps=%s"
        % [("%.3f" % e) if np.isfinite(e) else "nan" for e in local_exps],
    )

    # ---- G04: explicit piece 1/N law ----
    print()
    print("G04  EXPLICIT PIECE  1/N law")
    last3 = list(range(max(0, len(dyadic) - 3), len(dyadic)))
    b2_vals = [m2_seq[i] for i in last3]
    bc_vals = [cross_seq[i] for i in last3]
    print("  last-three N*dM^2: %s" % ["%.6f" % v for v in b2_vals])
    print("  last-three N*dcross: %s" % ["%.6f" % v for v in bc_vals])
    b2_mean = float(np.mean(b2_vals))
    bc_mean = float(np.mean(bc_vals))
    b2_rel = float(max(abs(v - b2_mean) for v in b2_vals) / max(abs(b2_mean), 1e-30))
    bc_rel = float(max(abs(v - bc_mean) for v in bc_vals) / max(abs(bc_mean), 1e-30))
    b_total = b2_mean + bc_mean
    total_last3 = [total2_seq[i] for i in last3]
    total_mean = float(np.mean(total_last3))
    print(
        "  b2=%.6f (rel %.3e)  b_cross=%.6f (rel %.3e)  b_total=%.6f  total_mean=%.6f"
        % (b2_mean, b2_rel, bc_mean, bc_rel, b_total, total_mean)
    )
    g04_b2 = b2_rel < G04_B2_REL
    g04_bcross = bc_rel < G04_BCROSS_REL
    g04 = g04_b2 and g04_bcross
    gate(
        "G04 explicit piece 1/N law",
        g04,
        "b2=%s b_cross=%s b_total=%.6f"
        % ("PASS" if g04_b2 else "FAIL", "PASS" if g04_bcross else "FAIL", b_total),
    )

    # ---- fits + G05 triangle bound ----
    print()
    print("FITS  a1, a2  and triangle bound")
    a1 = float(light[computed_sizes[-1]]["rsm2"])
    print("  a1 = ||R^sm||^2 at largest N (%d) = %.9f" % (computed_sizes[-1], a1))
    fit_sizes = np.array(
        [s for s in computed_sizes if s >= G04_FIT_MIN_N], dtype=float
    )
    fit_m2 = np.array([light[int(s)]["m2"] for s in fit_sizes])
    a2, b2_fit = fit_1_over_n_sq(fit_sizes, fit_m2)
    print("  a2 = %.9f  b2 = %.9f  (fit on N>=%d)" % (a2, b2_fit, G04_FIT_MIN_N))
    b_inf = float(np.sqrt(max(a1, 0.0)) + np.sqrt(max(a2, 0.0)))
    margin_inf = TRIANGLE_TARGET - b_inf
    print("  B_inf = %.6f  margin 3-B_inf = %.6f" % (b_inf, margin_inf))
    g05 = True
    print("  per-N triangle bound B_N and margin:")
    for size in computed_sizes:
        lp = light[size]
        b_n = float(np.sqrt(max(lp["rsm2"], 0.0)) + np.sqrt(max(lp["m2"], 0.0)))
        margin = TRIANGLE_TARGET - b_n
        r_norm = float(np.sqrt(max(lp["total2"], 0.0)))
        ok = b_n < TRIANGLE_TARGET
        g05 = g05 and ok
        print(
            "  N=%5d  B_N=%.6f  margin=%.6f  ||R||=%.9f  %s"
            % (size, b_n, margin, r_norm, "PASS" if ok else "FAIL")
        )
    g05 = g05 and (b_inf < TRIANGLE_TARGET)
    gate(
        "G05 triangle bound B_N<3 and B_inf<3",
        g05,
        "B_inf=%.6f margin=%.6f" % (b_inf, margin_inf),
    )

    # ---- G06: corpus TEL-B increment target ----
    print()
    print("G06  corpus TEL-B increment target  A_R < 43")
    a_r_max = max(rnorm_seq) if rnorm_seq else float("nan")
    print("  N|d||R||| sequence: %s" % ["%.6f" % v for v in rnorm_seq])
    print("  max (implied A_R) = %.6f" % a_r_max)
    g06 = bool(np.isfinite(a_r_max) and a_r_max < A_R_TARGET)
    gate(
        "G06 A_R = lim N|d||R||| < 43",
        g06,
        "A_R_max=%.6f" % a_r_max,
    )

    # ---- G07: verdict ----
    g_names = [n for n, _ in CHECKS]
    g_flags = {n: ok for n, ok in CHECKS}
    g01 = g_flags.get("G01 cover identity residual < 1e-10 at N=16 and N=32", False)
    g02 = g_flags.get("G02 split validation, corpus pins, dP=-Q", False)
    g03 = g_flags.get("G03 lattice piece N-independence", False)
    g04 = g_flags.get("G04 explicit piece 1/N law", False)
    g05f = g_flags.get("G05 triangle bound B_N<3 and B_inf<3", False)
    g06f = g_flags.get("G06 A_R = lim N|d||R||| < 43", False)
    if (not g01) or (not g02):
        verdict = "SPLIT_INVALID"
    elif g03 and g04 and g05f and g06f:
        verdict = "TELB_REDUCED_TO_TWO_SUP_BOUNDS"
    elif g03 and g04 and (not g05f):
        verdict = "SPLIT_VALID_BOUND_FAILS"
    else:
        verdict = "INCONCLUSIVE"
    g07 = verdict in VERDICT_ENUM
    gate("G07 verdict enum frozen", g07, verdict)

    n_pass = sum(1 for _, ok in CHECKS if ok)
    rt = time.time() - t0
    file_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    print()
    print(
        "HONEST NOTE: float64; exact identities validated numerically, "
        "sup-bounds are numerical not certified; "
        "SEAM.MMST.TYPEIII.CHARGED.01 stays [O]; a proof still needs "
        "(A) a rigorous sup bound for the lattice piece via Fourier "
        "decay of the continuous projector P - J on the 4N-cover and "
        "(B) digamma/sawtooth asymptotics for the explicit piece."
    )
    print("GATES %d/%d" % (n_pass, len(CHECKS)))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha)
    print("runtime %.3f s" % rt)

    # ---- result JSON ----
    table = []
    for size in computed_sizes:
        lp = light[size]
        r_norm = float(np.sqrt(max(lp["total2"], 0.0)))
        b_n = float(np.sqrt(max(lp["rsm2"], 0.0)) + np.sqrt(max(lp["m2"], 0.0)))
        table.append(
            {
                "N": size,
                "rsm2": lp["rsm2"],
                "m2": lp["m2"],
                "cross": lp["cross"],
                "total2": lp["total2"],
                "r_norm": r_norm,
                "B_N": b_n,
                "margin": TRIANGLE_TARGET - b_n,
            }
        )
    result = {
        "contract": "TELB.COVER.SPLIT.01",
        "spec_sha": SPEC_SHA,
        "file_sha256": file_sha,
        "gates": {n: bool(ok) for n, ok in CHECKS},
        "verdict": verdict,
        "table": table,
        "fits": {
            "a1": a1,
            "a2": a2,
            "b2": b2_fit,
            "b_cross": bc_mean,
            "b_total": b_total,
            "B_inf": b_inf,
            "margin_inf": margin_inf,
        },
        "dyadic_sequences": {
            "N_dRsm2": rsm2_seq,
            "N_dM2": m2_seq,
            "N_dcross": cross_seq,
            "N_dtotal2": total2_seq,
            "N_dRnorm": rnorm_seq,
            "local_exponents": local_exps,
        },
        "convention_note": "corpus e^{-i p x} mode basis; matched cover ordering %s"
        % convention_note,
        "runtime_s": rt,
        "computed_sizes": computed_sizes,
        "honest_note": "float64; exact identities validated numerically, "
        "sup-bounds numerical not certified; "
        "SEAM.MMST.TYPEIII.CHARGED.01 stays [O].",
    }
    out_path = Path(__file__).with_name("mmst_telb_cover_split_result.json")
    with open(out_path, "w") as fh:
        json.dump(result, fh, indent=1)
    print("wrote %s" % out_path)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
