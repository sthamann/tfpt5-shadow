#!/usr/bin/env python3
"""G_net continuum strand -- FINITE-LEVEL PRECURSORS of the GNS limit net.

Context (GNET.LOCALNET.01 / phys_gnet_local_functor_probe.py, promoted as
v746): the finite G_net functor I |-> (A(I-hat), E_I) on the mu4 quotient
circle is exact (isotony, graded locality, clock covariance), the local
Watatani index is exactly 4 for every interval l >= 2, and the Ramond
sector is a half-line/bond defect.  FIVE continuum theorems are NAMED,
NOT CLAIMED there: (1) GNS limit net, (2) index continuity along the
inductive limit, (3) identification with the Longo Q-system extension
(GATE.METRIC.08/11), (4) solitonic sector construction (twisted
DHR/Longo-Roberts), (5) Haag duality/split for the quotient-circle net.

THIS PROBE measures everything about the inductive limit that is
measurable NOW -- the finite-level precursors of (1), (2), (3), (5).
Theorem (4) (solitonic sectors) is NOT re-measured here; its finite
witness is the v746 bond-defect identity.

HONEST TYPING (firewall): every measurement below is FINITE-LEVEL
EVIDENCE FOR the cited continuum theorems, NEVER a continuum proof.
No continuum claim is gated.  Exploration only (tfpt-experiment
firewall): NOT wired into run_all.py, no ledger row, no paper claim,
no marker move.

THE TOWER: levels N = 48 * 2^k.  The inductive-limit embedding is the
Haar block ISOMETRY V_N : C^N -> C^2N, e_j |-> (e_2j + e_2j+1)/sqrt(2)
(the Osborne-Stottmeister/MMST real-space scaling map, second
quantized to the CAR embedding iota(c(f)) = c(Vf)).  The canonical
state is the one the finite functor carries: the declared chiral Dirac
sea (NS covariance C = f(S), as in v746 "state = declared chiral Dirac
sea"); mu4 = the clock-derived half-turn H = S^{N/2} (order 4 forced
by the NS spin structure, as in v726 -- not inserted).

PREREGISTERED GATES (frozen before the first run):

G1 INDUCTIVE-LIMIT COHERENCE  [precursor of theorem (1), and of (3)
   via the coherent expectation system]:
   G1a one-particle tower: V^T V = 1, V H_N = H_2N V, V L_N = L_2N V
       exactly (dev < 1e-10) for all adjacent pairs N = 48..768;
       V(window(N,p,l)) supported inside window(2N,2p,2l) exactly
       (positions p = 0 and the wrap p = N/2-1).
   G1b scale covariance of the tower data: the window matrices H_W
       (4x4 and 8x8) and the window isometry V_W (8x4) extracted at
       every level are IDENTICAL (dev < 1e-12) -- the coherence data
       is level-independent.
   G1c Fock coherence: iota . Ad(U^j) = Ad(U'^j) . iota on generators
       and on a monomial battery, hence iota(E(m)) = E'(iota(m)),
       all dev < 1e-10 (U = Gamma(H_W) on the small window, U' on the
       doubled window, iota from V_W).
   G1d commuting squares of the index-4 expectations (ambient Fock,
       N = 48, K-hat of 8 sites, I c J c K): restriction coherence
       E_K|A(I-hat) = E_J|A(I-hat) = E_I; commutation [E_I, E_J] = 0
       on an A(K-hat) battery; idempotency (E_I E_J)^2 = E_I E_J;
       and E_small = E_small . E_large on the A(I-hat) battery.
       All dev < 1e-10 (exact).

G2 STATE CONVERGENCE FOR GNS  [precursor of theorem (1), weak-*]:
   fixed local observables on the base window (N0 = 48, base l = 2,
   modes {0,1,24,25}), pulled back through the V-chain, levels
   N = 48..1536 (5 doublings).  Cauchy deltas d_k = max over the
   battery of |omega_k(x) - omega_k-1(x)| (battery: quadratic,
   quartic, E-processed, frozen random even combos).  Gates:
   d_5 < 5e-3, d_5/d_4 <= 0.85, d_4/d_3 <= 0.85 (oscillation-aware:
   max-over-battery, ratio gates on the LAST two steps only);
   parity-odd battery elements exactly 0 at every level (< 1e-12).

G3 INDEX STABILITY ALONG THE TOWER  [precursor of theorem (2),
   Pimsner-Popa/Longo heredity]: census over N = 48/96/192/384,
   l = 1..4, p = {0, 7, N/2-1}: for l >= 2 exactly 4 sectors,
   |lambda* - 1/4| < 1e-8, quasi-basis Watatani index = 4*1 with
   dev < 1e-7 (l <= 3); l = 1 anomaly stable (3 sectors,
   |lambda - 1/3| < 1e-8, index 3); local Takesaki [rho_W, U] = 0
   < 1e-8; PP pinching margin at the mixing minimizer
   min eig(E(vv*) - vv*/4) >= -1e-8.  NON-DEGRADATION: the per-level
   max deviations stay under the SAME absolute gates at EVERY level
   (profiles printed; no growth along the tower).

G4 SPLIT/DUALITY PRECURSORS  [precursors of theorem (5), and the
   index = statistical-dimension reading of (2)/(3)] -- measured,
   typed, never gated as continuum claims:
   G4a split witness: cross-covariance norm nu(sep) between separated
       doubled windows at FIXED angular geometry (base l = N/24,
       separations N/24, N/12, N/6), levels N = 48..768: per
       separation the tower deltas satisfy final |Delta nu| < 5e-3
       and last delta <= previous delta (stabilization); nu strictly
       decreasing in separation at the final level.
   G4b finite Haag-duality census (level-independent by G1b; computed
       once in the 6-mode ambient frame, I-hat = 4 modes, and the
       4-mode frame for l = 1): A(I-hat) spans its full 256-dim
       (resp. 16-dim) matrix factor (rank check); measured commutant
       dimension dim A' = 4^{n_c} EXACTLY; twisted-complement basis
       (even complement monomials + Klein_I * odd complement
       monomials) commutes with A (dev < 1e-10), is independent
       (Gram rank 4^{n_c}) => twisted-duality DEFECT = dim A' -
       4^{n_c} = 0; fixed-point census: dim B' = m * 4^{n_c} EXACTLY
       (m = sectors), so the relative-commutant EXCESS ratio
       dim B'/dim A' = m = 4 for l = 2 (= the local Watatani index)
       and = 3 for the l = 1 anomaly; kernel/nonzero eigengap of the
       commutant Gram operator >= 1e6 (clean count).
       [HONEST SPEC CORRECTION after run 1 (25/26): the B-commutant
       was first computed from a SMALL generating set (4 random
       E-images + sector projections); that set under-generates B
       (measured generated dim 70 < dim B = 72, so dim B' came out
       80 = 5 blocks instead of 64 = 4 blocks).  The generator
       specification is corrected to a measured SPANNING BASIS of
       B = E(A) (rank-reduction of the E-images of all 256 monomials;
       rank check dim B = sum d_q^2 gated), whose commutant IS B' by
       definition -- no generation assumption.  The GATE VALUES
       (dim B' = 64, ratio 4; l = 1: 48, ratio 3) are unchanged.]

G5 CONTROLS (all MUST fire):
   C1 scrambled bond data (same-arc pairing instead of the half-turn
      two-arc pairing): Fock tower coherence dev > 0.1.
   C2 broken twist (Z2-only average): lambda = 1/2 (dev < 1e-8) at
      N = 48 AND N = 384 -- the index census breaks (2 != 4).
   C3 scrambled state (random momentum occupation, filling fraction
      alternating 0.3/0.7 along the tower): final Cauchy delta
      > 10 * true d_5 AND > 0.05 -- convergence breaks.
   C4 scale-incoherent embedding (decimation e_j -> e_2j, isometric
      but not the scaling map): limiting window covariance max
      off-diagonal < 0.05 while the Haar value > 0.1 -- the block
      structure of the embedding is load-bearing.

VERDICT ENUM (frozen): 
  GNS-PRECURSORS-COHERENT : G1, G2, G3, G4 all pass AND all controls
                            C1-C4 fire.
  GNS-PRECURSORS-PARTIAL  : G1 and G3 pass, all controls fire, but
                            G2 or G4 fails (convergence/witness gap).
  GNS-PRECURSORS-DEAD     : G1 or G3 fails, or any control fails.

SHA-FREEZE: the construction source (all builder functions + frozen
constants) is hashed and printed before any gate runs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gnet_gns_limit_probe.py
"""

import hashlib
import inspect
import sys
import time

import numpy as np

TOL = 1e-10
SEED = 20260805
CHECKS = []

# frozen construction constants
N0 = 48                      # base level
K_STATE = 5                  # doublings for the state tower (48 -> 1536)
LEVELS_1P = (48, 96, 192, 384)          # one-particle tower pairs N -> 2N
LEVELS_IDX = (48, 96, 192, 384)         # index census levels
LEVELS_SPLIT = (48, 96, 192, 384, 768)  # split-witness levels
BASE_L = 2                   # base window length for the state tower


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    return ok


# ---------------- one-particle layer (constructions) ----------------

def spower(N, k):
    """S^k as an exact signed permutation (NS: -1 per wrap)."""
    P = np.zeros((N, N))
    for j in range(N):
        P[(j + k) % N, j] = (-1.0) ** ((j + k) // N)
    return P


def covariance(N):
    """the declared chiral Dirac sea (NS momenta, theta < 0 occupied)."""
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    occ = (th < 0).astype(float)
    return (F * occ) @ F.conj().T


def covariance_occ(N, occ):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    return (F * occ) @ F.conj().T


def window(N, p, l):
    return [(p + i) % N for i in range(l)] + \
           [(p + N // 2 + i) % N for i in range(l)]


def haar_iso(N):
    """the scaling isometry V_N : C^N -> C^2N, e_j -> (e_2j+e_2j+1)/sqrt2."""
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = V[2 * j + 1, j] = 1.0 / np.sqrt(2.0)
    return V


def decim_iso(N):
    """control C4: decimation e_j -> e_2j (isometric, scale-incoherent)."""
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = 1.0
    return V


# ---------------- Fock layer ----------------

def jw_ops(n):
    sm = np.array([[0, 1], [0, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    ops = []
    for j in range(n):
        m = np.array([[1.0]], dtype=complex)
        for l in range(n):
            m = np.kron(m, sz if l < j else (sm if l == j else I2))
        ops.append(m)
    return ops


def gamma_partial(Hsub, idx, cops):
    mu, V = np.linalg.eigh(1j * Hsub)
    dim = cops[0].shape[0]
    U = np.eye(dim, dtype=complex)
    for i in range(len(idx)):
        d = sum(np.conj(V[j, i]) * cops[idx[j]] for j in range(len(idx)))
        n_i = d.conj().T @ d
        ev = -1j * mu[i]
        U = U @ (np.eye(dim) + (ev - 1) * n_i)
    return U


def gaussian_rho(CW, cops):
    lam, V = np.linalg.eigh(CW)
    lam = np.clip(lam.real, 0.0, 1.0)
    dim = cops[0].shape[0]
    rho = np.eye(dim, dtype=complex)
    for i in range(len(cops)):
        d = sum(np.conj(V[j, i]) * cops[j] for j in range(len(cops)))
        rho = rho @ ((1 - lam[i]) * np.eye(dim)
                     + (2 * lam[i] - 1) * (d.conj().T @ d))
    return rho


def sector_projs(U):
    return [sum((1j ** (-q * j)) * np.linalg.matrix_power(U, j)
                for j in range(4)) / 4 for q in range(4)]


def lam_of(B, Efun):
    A = Efun(B)
    a, W = np.linalg.eigh((A + A.conj().T) / 2)
    keep = a > 1e-11 * max(a.max(), 1.0)
    Ws = W[:, keep] / np.sqrt(a[keep])
    M = Ws.conj().T @ B @ Ws
    top = float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)
    return 1.0 / top


def onb_of(P):
    w, W = np.linalg.eigh((P + P.conj().T) / 2)
    return W[:, w > 0.5]


def quasi_basis(Ps):
    onbs = [onb_of(P) for P in Ps]
    dims = [o.shape[1] for o in onbs]
    vs = [np.eye(Ps[0].shape[0], dtype=complex)]
    for q in range(4):
        for qp in range(4):
            if q == qp or dims[q] == 0 or dims[qp] == 0:
                continue
            for a in range(dims[q]):
                for b in range(dims[qp]):
                    vs.append(np.outer(onbs[q][:, a], onbs[qp][:, b].conj())
                              / np.sqrt(dims[qp]))
    return vs


def comm_kernel(gens, D):
    """dim of the commutant of the self-adjoint set gens in M_D:
    kernel of M = sum_g A_g^dag A_g with A_g the commutator superop,
    built term-by-term from single krons (pure numpy)."""
    M = np.zeros((D * D, D * D), dtype=complex)
    I = np.eye(D, dtype=complex)
    for g in gens:
        M += np.kron(I, np.conj(g @ g.conj().T))
        M += np.kron(g.conj().T @ g, I)
        M -= np.kron(g, np.conj(g))
        M -= np.kron(g.conj().T, g.T)
    ev = np.linalg.eigvalsh(M)
    tolz = 1e-9 * max(1.0, float(ev.max()))
    kdim = int(np.sum(ev < tolz))
    gap = float(ev[kdim] / max(abs(ev[kdim - 1]), 1e-300)) if kdim < len(ev) \
        else np.inf
    return kdim, gap, ev


def transport(U, cops):
    """extract T with Ad(U) c_i = sum_b T[b,i] c_b, verify residual."""
    n = len(cops)
    nrm = [float(np.vdot(c, c).real) for c in cops]
    T = np.zeros((n, n), dtype=complex)
    res = 0.0
    for i in range(n):
        A = U @ cops[i] @ U.conj().T
        for b in range(n):
            T[b, i] = np.vdot(cops[b], A) / nrm[b]
        R = A - sum(T[b, i] * cops[b] for b in range(n))
        res = max(res, float(np.abs(R).max()))
    return T, res


def rnd_elem(gens, rng, terms=6, maxdeg=3):
    dim = gens[0].shape[0]
    x = np.zeros((dim, dim), dtype=complex)
    for _ in range(terms):
        deg = rng.integers(1, maxdeg + 1)
        m = np.eye(dim, dtype=complex)
        for _ in range(deg):
            m = m @ gens[rng.integers(0, len(gens))]
        x += (rng.standard_normal() + 1j * rng.standard_normal()) * m
    return x


def sha_freeze():
    fns = [spower, covariance, covariance_occ, window, haar_iso, decim_iso,
           jw_ops, gamma_partial, gaussian_rho, sector_projs, lam_of,
           onb_of, quasi_basis, comm_kernel, transport, rnd_elem]
    blob = "".join(inspect.getsource(f) for f in fns)
    blob += repr((TOL, SEED, N0, K_STATE, LEVELS_1P, LEVELS_IDX,
                  LEVELS_SPLIT, BASE_L))
    return hashlib.sha256(blob.encode()).hexdigest()


# =====================================================================

def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    print("gnet_gns_limit_probe -- finite-level precursors of the GNS "
          "limit net\n")
    print(f"SHA-freeze (construction source + constants): "
          f"{sha_freeze()[:32]}\n")

    # ---------------- S0 sanity ----------------
    # comm_kernel on a known case: sz(x)I in M4 -> commutant M2(+)M2, dim 8
    sz = np.diag([1.0, -1.0]).astype(complex)
    g0 = np.kron(sz, np.eye(2, dtype=complex))
    kd, gap, _ = comm_kernel([g0], 4)
    check("S0 comm_kernel sanity: commutant of sz(x)1 in M4 has dim 8",
          kd == 8, f"dim = {kd}, gap = {gap:.1e}")

    # ================= G1 inductive-limit coherence =====================
    print("\n-- G1: inductive-limit coherence --")
    # G1a one-particle tower
    dev_a = 0.0
    ok_win = True
    for N in LEVELS_1P + (768,):
        V = haar_iso(N)
        HN, H2 = spower(N, N // 2), spower(2 * N, N)
        LN, L2 = spower(N, N // 12), spower(2 * N, 2 * N // 12)
        dev_a = max(dev_a, np.abs(V.T @ V - np.eye(N)).max())
        dev_a = max(dev_a, np.abs(V @ HN - H2 @ V).max())
        dev_a = max(dev_a, np.abs(V @ LN - L2 @ V).max())
        for (p, l) in ((0, 2), (N // 2 - 1, 2)):
            w, w2 = window(N, p, l), set(window(2 * N, 2 * p, 2 * l))
            for j in w:
                ok_win &= set(np.nonzero(V[:, j])[0]).issubset(w2)
    check("G1a tower: V isometric, V H_N = H_2N V, V L_N = L_2N V exact, "
          "N = 48..768", dev_a < TOL, f"max dev = {dev_a:.2e}")
    check("G1a tower: V(window(N,p,l)) inside window(2N,2p,2l) exactly "
          "(incl. wrap)", ok_win)

    # G1b scale covariance of the window data
    HW4_ref, HW8_ref, VW_ref = None, None, None
    dev_b = 0.0
    for N in LEVELS_1P + (768,):
        wN, w2N = window(N, 0, BASE_L), window(2 * N, 0, 2 * BASE_L)
        HN, H2 = spower(N, N // 2), spower(2 * N, N)
        HW4 = HN[np.ix_(wN, wN)]
        HW8 = H2[np.ix_(w2N, w2N)]
        VW = haar_iso(N)[np.ix_(w2N, wN)]
        if HW4_ref is None:
            HW4_ref, HW8_ref, VW_ref = HW4, HW8, VW
        dev_b = max(dev_b, np.abs(HW4 - HW4_ref).max(),
                    np.abs(HW8 - HW8_ref).max(), np.abs(VW - VW_ref).max())
    check("G1b scale covariance: H_W (4x4/8x8) and V_W (8x4) identical at "
          "every level", dev_b < 1e-12, f"max dev = {dev_b:.2e}")

    # G1c Fock coherence via the constant window data
    c4 = jw_ops(4)
    c8 = jw_ops(8)
    U4 = gamma_partial(HW4_ref, list(range(4)), c4)
    U8 = gamma_partial(HW8_ref, list(range(8)), c8)
    g_emb = [sum(VW_ref[a, i] * c8[a] for a in range(8)) for i in range(4)]
    # CAR sanity of the embedding
    dev_car = 0.0
    for i in range(4):
        for k in range(4):
            ac = g_emb[i] @ g_emb[k].conj().T + g_emb[k].conj().T @ g_emb[i]
            dev_car = max(dev_car, np.abs(
                ac - (1.0 if i == k else 0.0) * np.eye(256)).max())
    check("G1c iota is a CAR embedding: {g_i, g_k^dag} = delta exactly",
          dev_car < TOL, f"max dev = {dev_car:.2e}")
    T4, r4 = transport(U4, c4)
    T8, r8 = transport(U8, c8)
    dev_int = np.abs(VW_ref @ T4 - T8 @ VW_ref).max()
    check("G1c generator intertwining: V_W T4 = T8 V_W (transports "
          "extracted, residuals ~ 0)", max(r4, r8) < TOL and dev_int < TOL,
          f"res = {max(r4, r8):.1e}, dev = {dev_int:.2e}")

    # monomial battery: sequences of (mode, dag)
    monos = [[(0, 1)], [(0, 1), (1, 0)], [(0, 0), (1, 0)],
             [(0, 1), (2, 0)], [(0, 1), (1, 1), (2, 0), (3, 0)],
             [(0, 1), (0, 0)], [(2, 1), (3, 0)]]
    dev_c = 0.0
    for seq in monos:
        m_small = np.eye(16, dtype=complex)
        m_big = np.eye(256, dtype=complex)
        for (i, dag) in seq:
            f = c4[i].conj().T if dag else c4[i]
            m_small = m_small @ f
            m_big = m_big @ (g_emb[i].conj().T if dag else g_emb[i])
        # E(m) small: (1/4) sum_j Ad(U4^j); iota via rotated factors
        lhs = np.zeros((256, 256), dtype=complex)
        for j in range(4):
            term = np.eye(256, dtype=complex)
            Tj = np.linalg.matrix_power(T4, j)
            for (i, dag) in seq:
                co = Tj[:, i]
                if dag:
                    fac = sum(np.conj(co[b]) * g_emb[b].conj().T
                              for b in range(4))
                else:
                    fac = sum(co[b] * g_emb[b] for b in range(4))
                term = term @ fac
            lhs += term / 4
        rhs = sum(np.linalg.matrix_power(U8, j) @ m_big
                  @ np.linalg.matrix_power(U8, j).conj().T
                  for j in range(4)) / 4
        dev_c = max(dev_c, float(np.abs(lhs - rhs).max()))
        # also raw Ad coherence at j = 1
        ad_small_emb = np.zeros((256, 256), dtype=complex)
        term = np.eye(256, dtype=complex)
        for (i, dag) in seq:
            co = T4[:, i]
            if dag:
                fac = sum(np.conj(co[b]) * g_emb[b].conj().T for b in range(4))
            else:
                fac = sum(co[b] * g_emb[b] for b in range(4))
            term = term @ fac
        ad_small_emb = term
        ad_big = U8 @ m_big @ U8.conj().T
        dev_c = max(dev_c, float(np.abs(ad_small_emb - ad_big).max()))
    check("G1c Fock coherence: iota(E(m)) = E'(iota(m)) and "
          "iota(Ad(U)m) = Ad(U')iota(m) on the monomial battery",
          dev_c < TOL, f"max dev = {dev_c:.2e}")

    # G1d commuting squares in the ambient K window (N = 48, 8 sites)
    N = 48
    HN = spower(N, N // 2)
    ambK = window(N, 0, 4)
    copsK = jw_ops(8)
    pos = {s: i for i, s in enumerate(ambK)}

    def make_E(baseI):
        ambI = window(N, baseI[0], len(baseI))
        idxI = [pos[s] for s in ambI]
        HI = HN[np.ix_(ambI, ambI)]
        UI = gamma_partial(HI, idxI, copsK)

        def E(x, UI=UI):
            return sum(np.linalg.matrix_power(UI, j) @ x
                       @ np.linalg.matrix_power(UI, j).conj().T
                       for j in range(4)) / 4
        return E, idxI

    EI, idxI = make_E([0, 1])
    EJ, idxJ = make_E([0, 1, 2])
    EK, _ = make_E([0, 1, 2, 3])
    gensI = []
    for i in idxI:
        gensI += [copsK[i], copsK[i].conj().T]
    gensK = []
    for i in range(8):
        gensK += [copsK[i], copsK[i].conj().T]
    battI = [copsK[idxI[0]], copsK[idxI[0]].conj().T @ copsK[idxI[1]],
             copsK[idxI[0]] @ copsK[idxI[1]]] + \
            [rnd_elem(gensI, rng) for _ in range(4)]
    battK = [rnd_elem(gensK, rng) for _ in range(6)]
    d_restr = max(max(np.abs(EJ(x) - EI(x)).max(),
                      np.abs(EK(x) - EI(x)).max()) for x in battI)
    d_comm = max(np.abs(EI(EJ(x)) - EJ(EI(x))).max() for x in battK)
    d_idem = max(np.abs(EI(EJ(EI(EJ(x)))) - EI(EJ(x))).max() for x in battK)
    d_small = max(np.abs(EI(EJ(x)) - EI(x)).max() for x in battI)
    check("G1d commuting squares: E_K|A(I) = E_J|A(I) = E_I (restriction "
          "coherence)", d_restr < TOL, f"max dev = {d_restr:.2e}")
    check("G1d commuting squares: [E_I, E_J] = 0 on A(K-hat)",
          d_comm < TOL, f"max dev = {d_comm:.2e}")
    check("G1d commuting squares: (E_I E_J)^2 = E_I E_J (joint expectation)",
          d_idem < TOL, f"max dev = {d_idem:.2e}")
    check("G1d E_small = E_small . E_large on A(I-hat) (nested coherence)",
          d_small < TOL, f"max dev = {d_small:.2e}")

    # ================= G2 state convergence =============================
    print("\n-- G2: state convergence along the tower (Haar chain) --")
    win0 = window(N0, 0, BASE_L)

    def pullback_series(cov_fun, iso_fun, kmax):
        """window covariances of the pulled-back state, levels 0..kmax."""
        out = []
        chain = np.eye(N0)
        Nk = N0
        for k in range(kmax + 1):
            C = cov_fun(Nk, k)
            Ct = chain.T @ C @ chain
            out.append(Ct[np.ix_(win0, win0)])
            V = iso_fun(Nk)
            chain = V @ chain
            Nk *= 2
        return out

    cws = pullback_series(lambda Nk, k: covariance(Nk), haar_iso, K_STATE)

    # battery (frozen): even, odd, E-processed, random even combos
    n_ = [c4[i].conj().T @ c4[i] for i in range(4)]
    B_even = [n_[0], c4[0].conj().T @ c4[1], c4[0].conj().T @ c4[2],
              c4[0].conj().T @ c4[3], c4[1].conj().T @ c4[2],
              c4[0] @ c4[1], n_[0] @ n_[2],
              c4[0].conj().T @ c4[1].conj().T @ c4[2] @ c4[3]]
    r_pairs = [rnd_elem([c4[0].conj().T @ c4[1], c4[1].conj().T @ c4[2],
                         c4[2].conj().T @ c4[3], n_[0], n_[3]], rng)
               for _ in range(2)]
    B_even += r_pairs

    def E4(x):
        return sum(np.linalg.matrix_power(U4, j) @ x
                   @ np.linalg.matrix_power(U4, j).conj().T
                   for j in range(4)) / 4

    B_E = [E4(x) for x in (n_[0], c4[0].conj().T @ c4[2],
                           c4[0].conj().T @ c4[1].conj().T @ c4[2] @ c4[3])]
    B_odd = [c4[0], c4[0].conj().T @ c4[1] @ c4[2]]
    batt = B_even + B_E

    om = []
    odd_max = 0.0
    for k, CW in enumerate(cws):
        rho = gaussian_rho(CW, c4)
        om.append(np.array([np.trace(rho @ x) for x in batt]))
        odd_max = max(odd_max, max(abs(np.trace(rho @ x)) for x in B_odd))
    om = np.array(om)
    dd = [float(np.abs(om[k] - om[k - 1]).max()) for k in range(1, K_STATE + 1)]
    print("   Cauchy deltas d_k (max over battery):",
          " ".join(f"{d:.3e}" for d in dd))
    rat = [dd[i + 1] / dd[i] if dd[i] > 0 else 0.0 for i in range(len(dd) - 1)]
    print("   ratios:", " ".join(f"{r:.3f}" for r in rat))
    check(f"G2 Cauchy: d_5 = {dd[-1]:.3e} < 5e-3", dd[-1] < 5e-3)
    check(f"G2 contraction: d5/d4 = {rat[-1]:.3f} <= 0.85 and "
          f"d4/d3 = {rat[-2]:.3f} <= 0.85",
          rat[-1] <= 0.85 and rat[-2] <= 0.85)
    check("G2 parity: odd battery elements exactly 0 at every level",
          odd_max < 1e-12, f"max |omega(odd)| = {odd_max:.1e}")

    # ================= G3 index stability census ========================
    print("\n-- G3: index census along the tower --")
    print(f"{'N':>4} {'max|lam-1/4|':>14} {'max ind dev':>13} "
          f"{'max Takesaki':>13} {'anomaly':>9} {'PP margin':>11}")
    ok3 = True
    prof3 = []
    for NN in LEVELS_IDX:
        SS_H = spower(NN, NN // 2)
        CC = covariance(NN)
        dlam, dind, dtak, danom, pmargin = 0.0, 0.0, 0.0, 0.0, 0.0
        anom_ok = True
        for l in (1, 2, 3, 4):
            for p in (0, 7, NN // 2 - 1):
                win = window(NN, p, l)
                HW = SS_H[np.ix_(win, win)]
                CW = CC[np.ix_(win, win)]
                cs = jw_ops(2 * l)
                U = gamma_partial(HW, list(range(2 * l)), cs)
                Ps = sector_projs(U)
                dims = [int(round(np.trace(P).real)) for P in Ps]
                m = sum(1 for d in dims if d > 0)

                def E(x, Ps=Ps):
                    return sum(P @ x @ P for P in Ps)

                v = np.zeros(2 ** (2 * l), dtype=complex)
                for P in Ps:
                    o = onb_of(P)
                    if o.shape[1]:
                        v += o[:, 0]
                v /= np.linalg.norm(v)
                vv = np.outer(v, v.conj())
                lam = lam_of(vv, E)
                pm = float(np.linalg.eigvalsh(E(vv) - 0.25 * vv).min())
                rho = gaussian_rho(CW, cs)
                tak = float(np.abs(rho @ U - U @ rho).max())
                dtak = max(dtak, tak)
                if l >= 2:
                    dlam = max(dlam, abs(lam - 0.25))
                    anom_ok &= (m == 4)
                    pmargin = min(pmargin, pm)
                else:
                    danom = max(danom, abs(lam - 1.0 / 3.0))
                    anom_ok &= (m == 3)
                if l <= 3:
                    vs = quasi_basis(Ps)
                    ind = sum(x @ x.conj().T for x in vs)
                    dind = max(dind, float(
                        np.abs(ind - m * np.eye(2 ** (2 * l))).max()))
        prof3.append((NN, dlam, dind, dtak, danom, pmargin))
        ok3 &= (dlam < 1e-8 and dind < 1e-7 and dtak < 1e-8
                and danom < 1e-8 and anom_ok and pmargin > -1e-8)
        print(f"{NN:>4} {dlam:>14.2e} {dind:>13.2e} {dtak:>13.2e} "
              f"{danom:>9.2e} {pmargin:>11.2e}")
    grow = max(prof3[-1][1], prof3[-1][2]) <= max(
        10 * max(prof3[0][1], prof3[0][2]), 1e-8)
    check("G3 index census: lambda* = 1/4 exactly, Ind = 4*1, Takesaki = 0, "
          "l = 1 anomaly stable, PP margin >= -1e-8 at EVERY level", ok3)
    check("G3 non-degradation: deviations do not grow along the tower "
          "(final <= max(10x first, 1e-8))", grow)

    # ================= G4 split/duality precursors ======================
    print("\n-- G4a: split witness (cross-covariance norm, fixed angular "
          "geometry) --")
    seps = {}
    for NN in LEVELS_SPLIT:
        C = covariance(NN)
        l = NN // 24
        for i, d in enumerate((NN // 24, NN // 12, NN // 6)):
            W1 = window(NN, 0, l)
            W2 = window(NN, l + d, l)
            nu = float(np.linalg.norm(C[np.ix_(W1, W2)], 2))
            seps.setdefault(i, []).append(nu)
    ok4a = True
    for i, label in enumerate(("N/24", "N/12", "N/6")):
        vals = seps[i]
        dts = [abs(vals[k] - vals[k - 1]) for k in range(1, len(vals))]
        print(f"   sep {label}: nu = " + " ".join(f"{v:.5f}" for v in vals)
              + "  deltas: " + " ".join(f"{d:.1e}" for d in dts))
        ok4a &= dts[-1] < 5e-3 and dts[-1] <= dts[-2]
    ok4a &= seps[0][-1] > seps[1][-1] > seps[2][-1]
    check("G4a split witness: cross-norm stabilizes along the tower "
          "(final delta < 5e-3, non-increasing) and decreases with "
          "separation", ok4a)

    print("\n-- G4b: finite Haag-duality / commutant census --")
    # main config: I-hat = 4 modes first, complement = 2 modes (D = 64)
    c6 = jw_ops(6)
    D6 = 64
    gensA = []
    for i in range(4):
        gensA += [c6[i], c6[i].conj().T]
    # A spans its full factor (rank of the 256 monomials in 16-dim factor)
    mono_vecs = []
    for S in range(16):
        for Tm in range(16):
            op = np.eye(16, dtype=complex)
            for i in range(4):
                if (S >> i) & 1:
                    op = op @ c4[i].conj().T
            for i in range(4):
                if (Tm >> i) & 1:
                    op = op @ c4[i]
            mono_vecs.append(op.reshape(-1))
    rankA = np.linalg.matrix_rank(np.array(mono_vecs), tol=1e-8)
    check("G4b A(I-hat) spans its full 256-dim matrix factor",
          rankA == 256, f"rank = {rankA}")
    kdA, gapA, _ = comm_kernel(gensA, D6)
    check("G4b measured dim A' = 4^{n_c} = 16 exactly (clean eigengap)",
          kdA == 16 and gapA > 1e6, f"dim = {kdA}, gap = {gapA:.1e}")
    # twisted-complement basis: even comp monomials + Klein_I * odd
    KI = np.eye(64, dtype=complex)
    for i in range(4):
        KI = KI @ (np.eye(64) - 2 * c6[i].conj().T @ c6[i])
    cands, dev_tw = [], 0.0
    for S in range(4):
        for Tm in range(4):
            op = np.eye(64, dtype=complex)
            npar = 0
            for i in (4, 5):
                if (S >> (i - 4)) & 1:
                    op = op @ c6[i].conj().T
                    npar += 1
            for i in (4, 5):
                if (Tm >> (i - 4)) & 1:
                    op = op @ c6[i]
                    npar += 1
            cand = op if npar % 2 == 0 else KI @ op
            cands.append(cand)
            dev_tw = max(dev_tw, max(float(np.abs(cand @ g - g @ cand).max())
                                     for g in gensA))
    gram_rank = np.linalg.matrix_rank(
        np.array([x.reshape(-1) for x in cands]), tol=1e-8)
    defect = kdA - 16
    check("G4b twisted duality: the 16 twisted-complement elements commute "
          "with A, are independent, and exhaust A' -- defect = 0",
          dev_tw < TOL and gram_rank == 16 and defect == 0,
          f"dev = {dev_tw:.1e}, gram rank = {gram_rank}, defect = {defect}")
    # fixed-point census: B = A^{mu4} = range of E; use a measured
    # SPANNING BASIS of B (commutant of a spanning set = B' exactly)
    u4f = gamma_partial(HW4_ref, list(range(4)), c4)
    Ps4 = sector_projs(u4f)
    dims4 = [int(round(np.trace(P).real)) for P in Ps4]
    m4 = sum(1 for d in dims4 if d > 0)

    def E16(x):
        return sum(P @ x @ P for P in Ps4)

    def span_basis(Eims, dim_expect):
        M = np.array([x.reshape(-1) for x in Eims])
        _, s, Vh = np.linalg.svd(M, full_matrices=False)
        r = int(np.sum(s > 1e-9 * s[0]))
        n = Eims[0].shape[0]
        return [Vh[i].reshape(n, n) for i in range(r)], r

    Eims = [E16(m.reshape(16, 16)) for m in np.array(mono_vecs)]
    basB, dimB = span_basis(Eims, None)
    check("G4b dim B = sum d_q^2 (measured spanning basis of E(A))",
          dimB == sum(d * d for d in dims4),
          f"dim B = {dimB}, sector dims = {dims4}")
    gensB = [np.kron(b, np.eye(4, dtype=complex)) for b in basB]
    kdB, gapB, _ = comm_kernel(gensB, D6)
    ratio = kdB / kdA
    check("G4b fixed-point census: dim B' = m * 4^{n_c} = 64, excess ratio "
          "dim B'/dim A' = 4 = the local Watatani index",
          kdB == 64 and abs(ratio - 4.0) < 1e-12 and gapB > 1e6 and m4 == 4,
          f"dim B' = {kdB}, ratio = {ratio:.1f}, gap = {gapB:.1e}")
    # l = 1 anomaly config (D = 16): I = 2 modes, comp = 2 modes
    HW2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    c2 = jw_ops(2)
    gensA1 = []
    for i in range(2):
        gensA1 += [c4[i], c4[i].conj().T]      # inside jw_ops(4) frame
    kdA1, gapA1, _ = comm_kernel(gensA1, 16)
    u2 = gamma_partial(HW2, [0, 1], c2)
    Ps2 = sector_projs(u2)
    m2 = sum(1 for P in Ps2 if np.trace(P).real > 0.5)

    def E4f(x):
        return sum(P @ x @ P for P in Ps2)

    monos2 = []
    for S in range(4):
        for Tm in range(4):
            op = np.eye(4, dtype=complex)
            for i in range(2):
                if (S >> i) & 1:
                    op = op @ c2[i].conj().T
            for i in range(2):
                if (Tm >> i) & 1:
                    op = op @ c2[i]
            monos2.append(op)
    basB1, dimB1 = span_basis([E4f(m) for m in monos2], None)
    gensB1 = [np.kron(b, np.eye(4, dtype=complex)) for b in basB1]
    kdB1, gapB1, _ = comm_kernel(gensB1, 16)
    check("G4b l = 1 anomaly census: dim A' = 16, dim B' = 48, excess "
          "ratio = 3 (the 3-sector anomaly index)",
          kdA1 == 16 and kdB1 == 48 and m2 == 3
          and gapA1 > 1e6 and gapB1 > 1e6,
          f"dim A' = {kdA1}, dim B' = {kdB1}, m = {m2}")

    # ================= G5 controls ======================================
    print("\n-- G5: controls (must fire) --")
    # C1 scrambled bond data: same-arc pairing instead of the half-turn
    J2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    HW4s = np.kron(np.eye(2), J2)             # pairs (0,1),(2,3): same arc
    HW8s = np.kron(np.eye(4), J2)
    U4s = gamma_partial(HW4s, list(range(4)), c4)
    U8s = gamma_partial(HW8s, list(range(8)), c8)
    T4s, _ = transport(U4s, c4)
    T8s, _ = transport(U8s, c8)
    dev_c1 = float(np.abs(VW_ref @ T4s - T8s @ VW_ref).max())
    check("C1 fires: same-arc bond scramble breaks tower coherence "
          "(V_W T4s != T8s V_W)", dev_c1 > 0.1, f"dev = {dev_c1:.3f}")
    # C2 broken twist: Z2-only average
    ok_c2 = True
    for NN in (48, 384):
        win = window(NN, 0, 2)
        HWn = spower(NN, NN // 2)[np.ix_(win, win)]
        cs = jw_ops(4)
        U = gamma_partial(HWn, list(range(4)), cs)
        Ps = sector_projs(U)
        v = np.zeros(16, dtype=complex)
        for P in Ps:
            o = onb_of(P)
            if o.shape[1]:
                v += o[:, 0]
        v /= np.linalg.norm(v)

        def E2(x, U=U):
            U2 = U @ U
            return (x + U2 @ x @ U2.conj().T) / 2

        lam2 = lam_of(np.outer(v, v.conj()), E2)
        ok_c2 &= abs(lam2 - 0.5) < 1e-8
    check("C2 fires: Z2-only average gives lambda = 1/2 != 1/4 at N = 48 "
          "and 384 (index census breaks under broken twist)", ok_c2)
    # C3 scrambled state: random occupation, alternating filling
    rng3 = np.random.default_rng(SEED + 1)

    def scr_cov(Nk, k):
        frac = 0.3 if k % 2 == 0 else 0.7
        occ = np.zeros(Nk)
        occ[rng3.permutation(Nk)[:int(frac * Nk)]] = 1.0
        return covariance_occ(Nk, occ)

    cws_scr = pullback_series(scr_cov, haar_iso, K_STATE)
    om_s = []
    for CW in cws_scr:
        rho = gaussian_rho(CW, c4)
        om_s.append(np.array([np.trace(rho @ x) for x in batt]))
    om_s = np.array(om_s)
    d5s = float(np.abs(om_s[-1] - om_s[-2]).max())
    check("C3 fires: scrambled state breaks Cauchy convergence "
          f"(d5_scr = {d5s:.3f} > max(10*d5_true, 0.05))",
          d5s > max(10 * dd[-1], 0.05))
    # C4 decimation embedding: limit degenerates
    cws_dec = pullback_series(lambda Nk, k: covariance(Nk), decim_iso,
                              K_STATE)
    off_dec = float(np.abs(cws_dec[-1] - np.diag(np.diag(cws_dec[-1]))).max())
    off_haar = float(np.abs(cws[-1] - np.diag(np.diag(cws[-1]))).max())
    check("C4 fires: decimation embedding degenerates the limit "
          "(off-diag < 0.05) while the Haar chain does not (> 0.1)",
          off_dec < 0.05 and off_haar > 0.1,
          f"decim = {off_dec:.4f}, haar = {off_haar:.4f}")

    # ================= verdict ==========================================
    names = [n for n, _ in CHECKS]
    res = dict(CHECKS)
    g1 = all(res[n] for n in names if n.startswith("G1"))
    g2 = all(res[n] for n in names if n.startswith("G2"))
    g3 = all(res[n] for n in names if n.startswith("G3"))
    g4 = all(res[n] for n in names if n.startswith("G4"))
    ctrl = all(res[n] for n in names if n.startswith("C"))
    s0 = all(res[n] for n in names if n.startswith("S0"))
    if s0 and g1 and g2 and g3 and g4 and ctrl:
        verdict = "GNS-PRECURSORS-COHERENT"
    elif s0 and g1 and g3 and ctrl:
        verdict = "GNS-PRECURSORS-PARTIAL"
    else:
        verdict = "GNS-PRECURSORS-DEAD"
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}"
          f"   ({time.time() - t0:.1f} s)")
    print("""
PRECURSOR MAP (typed; finite evidence FOR the cited theorems, never a
continuum proof):
  G1 (coherence, commuting squares)  -> theorem (1) GNS limit net: the
     inductive system (A_N, iota_N, E) is exactly coherent -- the data
     whose GNS/inductive limit the theorem asserts; the coherent
     expectation system is also the finite half of (3) Longo Q-system.
  G2 (state Cauchy profiles)         -> theorem (1): weak-* convergence
     of the canonical chiral-sea state on fixed local observables =
     the GNS-limit precursor.
  G3 (index census + PP margins)     -> theorem (2) index continuity
     (Pimsner-Popa/Longo heredity): index exactly 4 at every level
     with non-degrading margins.
  G4a (split witness)                -> theorem (5) split property:
     the finite correlation bound between separated intervals.
  G4b (commutant census)             -> theorem (5) Haag duality
     (twisted/fermionic form, defect 0) and the index =
     statistical-dimension reading of (2)/(3): excess ratio = 4.
  Theorem (4) (solitonic R sectors) is NOT re-measured here; its
  finite witness stays the v746 bond-defect identity.
No marker moves; exploration only.""")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
