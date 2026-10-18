#!/usr/bin/env python3
"""tfpt4d_content_candidate_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (TFPT4D.LATTICE.ACTION.01 [O] + FTRANSFER.GENERATING.01 [O]):
today's Hamiltonian route cleared T2 with a Z4 staggered ring that had
NO Standard-Model content.  This probe is the first Hamiltonian
candidate that carries a TFPT-CONTENT SHADOW (the Z6 centre of
G_SM = SU(3)xSU(2)xU(1)/Z6, with the actual 6Y charge table) AND
executes a finite generating functional W[J] from which the transfer
readouts derive.

MODEL (content Hilbert space, Hamiltonian route):
    2-site ring, structure group Z6 (SM centre),
    1 quantum Z6 link (flux basis |k>, Z = diag(ω^k), X = flux shift,
    X Z X^dag = ω^{-1} Z, ω = exp(2πi/6)) plus 1 FROZEN closing link,
    5 Jordan-Wigner fermion species = one representative per SM
    multiplet of a single generation, each species = 2 sites = 2 qubits.
    Color/weak multiplicities are T4 WEIGHTS, not extra qubits
    (15 Weyl components would be 30 qubits).
    dim = 6 * 2^{10} = 6144.
    Discrete charges q = 6Y mod 6:
        Q -> 1,  u^c -> -4 ≡ 2,  d^c -> 2,  L -> -3 ≡ 3,  e^c -> 0.
    H_open = -lam_E (X + X^dag)
             + w sum_s (psi^dag_{s,0} Z^{q_s} psi_{s,1} + h.c.)
             + m sum_{s,x} (-1)^x n_{s,x}
    (open-chain Gauss: both sites touch the frozen seam, so the seam
    hopping is NOT in H_open -- see T3.  T = e^{-a H} positive by
    construction.)

  T1  GAUSS LAW with the ACTUAL 6Y table: V_x = X^{±1} * prod_s
      ω^{q_s n_{s,x}} commute with H_open to machine precision.
      MUTANT: a wrong charge table (Q charge 0 instead of 1) fails.
  T2  H = H^dag exactly, so T = e^{-aH} is SPD.
  T3  mu4 SEAM TWIST as a background phase on the FROZEN closing link
      acting on the fermions.  Honest typing: the seam clock is a
      boundary MODULE, not the Z6 gauge group -- with a dynamical
      closing link the background relabels (today's Hamiltonian-route
      lesson), so the closer is frozen by construction.  In the
      frozen-gauge fermion ring the mu4 sample i^k splits E0, with
      the conjugate pair k = 1, 3 degenerate.
  T4  exact rational anomaly sums of one SM generation with the 6Y
      table and color/weak multiplicities (Fractions), plus Witten
      evenness.  MUTANT: drop L, three sums break and Witten goes odd.
  T7  determinantal-law Gaussianity: <prod n> vs det[G], G = <psi^dag
      psi>.  Interacting ground state (full 6144) violates it; free
      control on the FERMION factor alone (dim 1024, no link
      degeneracy) satisfies it to machine precision.

W[J] (FTRANSFER.GENERATING mechanism, reduced so exact eigh works):
    same Hamiltonian class, 2 sites, 1 quantum Z6, frozen seam angle θ,
    2 species (Q with q=1, e^c with q=0) -- dim 6 * 2^4 = 96.
    W(J, θ) = log Tr exp(-β H(θ) + sum_a J_a O_a) at fixed small β,
    O = (Q-charge, (Z+Z^dag)/2, e^c-charge).  With a dynamical
    link the seam is absorbed into the flux for fermion bilinears
    (today's T3a lesson): mixed ∂²W/∂J_N∂θ ~ 0 for Q-charge, while
    the link operator transduces.  A frozen-link companion W at
    dim 16 shows the complementary half: staggered Q-charge
    transduces once the closer cannot relabel.  e^c is θ-blind
    in both.
    (a) ∂W/∂J_a |_{J=0} = thermal <O_a>
    (b) ∂²W/∂J_a∂J_b = Kubo connected correlator <O_a; O_b>_c
    (c) mixed ∂²W/∂J_a∂θ = connected seam-response: nonzero for
        the link (dynamical) and for staggered Q-charge (frozen
        companion), machine-zero for the decoupled e^c control
        -- OBS.TRANSDUCTION.01 executable from ONE W.

HONEST BOUNDARY (dimension-uplift firewall): Z6-centre / hypercharge
SHADOW of one generation, 1+1D, 2 sites, vectorlike staggered measure,
multiplicities as weights not as extra qubits, W[J] at reduced species
content.  NOTHING closes TFPT4D.LATTICE.ACTION.01 or
FTRANSFER.GENERATING.01.

VERDICT ENUM: CONTENT_SHADOW_CANDIDATE_PASSES + WJ_MECHANISM_EXECUTED
(contracts stay [O]).
"""
import time
from fractions import Fraction as F

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

T0 = time.perf_counter()
ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name
          + ("  | " + extra if extra else ""))


def maxabs_sp(A):
    if A.nnz == 0:
        return 0.0
    return float(np.max(np.abs(A.data)))


def maxabs(A):
    return float(np.max(np.abs(A)))


# =====================================================================
# Species table (actual TFPT one-generation content)
# =====================================================================
# (name, color dim, SU2 dim, hypercharge Y) -- left-handed Weyl
GEN = [
    ("Q",   3, 2, F(1, 6)),
    ("u^c", 3, 1, F(-2, 3)),
    ("d^c", 3, 1, F(1, 3)),
    ("L",   1, 2, F(-1, 2)),
    ("e^c", 1, 1, F(1, 1)),
]
# representative JW species: one per multiplet; weight = color*weak
NAMES = [g[0] for g in GEN]
WEIGHTS = [g[1] * g[2] for g in GEN]
CHARGES = [int(6 * g[3]) % 6 for g in GEN]   # 6Y mod 6
# Q:1, u^c:-4≡2, d^c:2, L:-3≡3, e^c:0
CHARGES_MUTANT = list(CHARGES)
CHARGES_MUTANT[0] = 0                         # Q treated as Z6-neutral

NS = 2
NSPC = len(CHARGES)                           # 5
NMODES = NSPC * NS                            # 10
DL = 6
DF = 2 ** NMODES                              # 1024
D = DL * DF                                   # 6144
OMEGA = np.exp(2j * np.pi / 6)
Z1 = np.diag(OMEGA ** np.arange(6)).astype(complex)
X1 = np.roll(np.eye(6), 1, axis=0).astype(complex)
Z1_SP = sparse.csr_matrix(Z1)
X1_SP = sparse.csr_matrix(X1)
I_L = sparse.eye(DL, dtype=complex, format="csr")
I_F = sparse.eye(DF, dtype=complex, format="csr")
I2 = sparse.eye(2, dtype=complex, format="csr")
SZ = sparse.diags([1.0, -1.0], format="csr", dtype=complex)
ANN = sparse.csr_matrix(np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex))

LAM_E, W_HOP, MASS = 1.0, 0.7, 0.5


def ferm_mode(alpha, n_modes):
    """Jordan-Wigner annihilator on mode alpha."""
    parts = []
    for j in range(n_modes):
        if j < alpha:
            parts.append(SZ)
        elif j == alpha:
            parts.append(ANN)
        else:
            parts.append(I2)
    out = parts[0]
    for p in parts[1:]:
        out = sparse.kron(out, p, format="csr")
    return out


def mode_index(s, x):
    return s * NS + x


print("=== content shadow: Z6 centre, 6Y table, dim %d ===" % D)
print("   species   Y        6Y mod 6   color  weak  weight (T4 only)")
for g, q, wgt in zip(GEN, CHARGES, WEIGHTS):
    print("   %-5s   %6s     %d          %d      %d     %d"
          % (g[0], str(g[3]), q, g[1], g[2], wgt))
print("   Hilbert: 1 quantum Z6 link x %d JW qubits = %d x %d = %d"
      % (NMODES, DL, DF, D))
print("   u^c and d^c share Z6 charge 2 -- the centre does not "
      "distinguish them (honest shadow)")
rep("charge table [exact]: 6Y mod 6 = [Q:1, u^c:2, d^c:2, L:3, e^c:0]",
    CHARGES == [1, 2, 2, 3, 0])

xzx = X1 @ Z1 @ X1.conj().T
rep("Z6 Weyl [exact]: X Z X^dag = ω^{-1} Z (maxdev %.1e)"
    % maxabs(xzx - (OMEGA ** (-1)) * Z1),
    maxabs(xzx - (OMEGA ** (-1)) * Z1) < 1e-14)


# fermion ops on the DF factor
PSI_F = [ferm_mode(a, NMODES) for a in range(NMODES)]
NUM_F = [P.conj().T @ P for P in PSI_F]
HOP_F = []  # species-s hopping site0 -> site1, on DF
for s in range(NSPC):
    a0, a1 = mode_index(s, 0), mode_index(s, 1)
    HOP_F.append(PSI_F[a0].conj().T @ PSI_F[a1])


def lift_L(M6):
    return sparse.kron(M6 if sparse.issparse(M6) else sparse.csr_matrix(M6),
                       I_F, format="csr")


def lift_F(F):
    return sparse.kron(I_L, F, format="csr")


def z_power(q):
    q = int(q) % 6
    if q == 0:
        return I_L
    return sparse.csr_matrix(np.linalg.matrix_power(Z1, q))


def build_H_open(charges, lam_e=LAM_E, w=W_HOP, m=MASS):
    """Open 2-site chain: quantum-link hopping + electric + staggered
    mass.  Frozen closer is absent -- both sites would touch it."""
    H = -lam_e * (lift_L(X1_SP) + lift_L(X1_SP.conj().T))
    for s, q in enumerate(charges):
        hop = sparse.kron(z_power(q), HOP_F[s], format="csr")
        H = H + w * (hop + hop.conj().T)
        n0 = lift_F(NUM_F[mode_index(s, 0)])
        n1 = lift_F(NUM_F[mode_index(s, 1)])
        H = H + m * (n0 - n1)
    return H.tocsr()


def omega_phase(q, num_op_full):
    """ω^{q n} = I + (ω^q - 1) n  for n a 0-1 projector."""
    ph = OMEGA ** (int(q) % 6)
    return sparse.eye(D, dtype=complex, format="csr") + (ph - 1.0) * num_op_full


def gauss_unitary(site, charges):
    """V_0 = X * Φ_0,  V_1 = X^{-1} * Φ_1,  Φ = prod_s ω^{q_s n_{s,site}}."""
    if site == 0:
        V = lift_L(X1_SP)
    elif site == 1:
        V = lift_L(X1_SP.conj().T)          # X^{-1} = X^dag
    else:
        raise ValueError(site)
    for s, q in enumerate(charges):
        n = lift_F(NUM_F[mode_index(s, site)])
        V = V @ omega_phase(q, n)
    return V.tocsr()


def comm_dev(H, V):
    return maxabs_sp(H @ V - V @ H)


# ---------------------------------------------------------------- T1
print("=== T1: Z6 Gauss law with the 6Y table ===")
H = build_H_open(CHARGES)
devs = [comm_dev(H, gauss_unitary(x, CHARGES)) for x in (0, 1)]
print("   Gauss commutators (sites 0,1):", ["%.1e" % d for d in devs])
rep("T1 [exact]: both Z6 Gauss unitaries (per-species 6Y phases) "
    "commute with H_open (maxdev %.1e) -- local gauge invariance "
    "with the actual charge table" % max(devs),
    max(devs) < 1e-10)

devs_m = [comm_dev(H, gauss_unitary(x, CHARGES_MUTANT)) for x in (0, 1)]
print("   MUTANT Gauss commutators:", ["%.1e" % d for d in devs_m])
rep("T1 MUTANT FIRES: wrong charge table (Q: 1 -> 0) fails to commute "
    "(maxdev %.1e)" % max(devs_m),
    max(devs_m) > 1e-4)

# ---------------------------------------------------------------- T2
print("=== T2: hermiticity / positivity by construction ===")
herm = maxabs_sp(H - H.conj().T)
rep("T2 [BY CONSTRUCTION]: H = H^dag exactly (dev %.1e), so "
    "T = e^{-aH} is symmetric positive definite -- Hamiltonian route"
    % herm, herm < 1e-12)

# ---------------------------------------------------------------- T3
print("=== T3: mu4 seam module on the FROZEN closer ===")
print("   typing: bulk gauge group = Z6 (SM centre); seam clock = mu4")
print("   boundary MODULE, not an element of the gauge group.  The")
print("   closer is frozen so the background cannot relabel through a")
print("   dynamical link (today's T3a trap).")


def ferm_dense(alpha, n_modes):
    out = np.array([[1.0]], dtype=complex)
    sz = np.diag([1.0, -1.0])
    a = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    for j in range(n_modes):
        if j < alpha:
            out = np.kron(out, sz)
        elif j == alpha:
            out = np.kron(out, a)
        else:
            out = np.kron(out, np.eye(2))
    return out


def build_H_frozen_mu4(k_mu4, charges=CHARGES, n_modes=None):
    """Fermion ring, both links background: U_01 = 1, U_10 = i^k
    (mu4 module).  No quantum link -- dim 2^{n_modes}."""
    if n_modes is None:
        n_modes = NMODES
    nspc = n_modes // NS
    Df = 2 ** n_modes
    ps = [ferm_dense(a, n_modes) for a in range(n_modes)]
    Hb = np.zeros((Df, Df), dtype=complex)
    seam = 1j ** int(k_mu4)
    for s in range(nspc):
        q = int(charges[s]) % 6
        a0, a1 = s * NS + 0, s * NS + 1
        hop01 = ps[a0].conj().T @ ps[a1]              # U=1
        hop10 = (seam ** q) * (ps[a1].conj().T @ ps[a0])
        Hb += W_HOP * (hop01 + hop01.conj().T)
        Hb += W_HOP * (hop10 + hop10.conj().T)
        Hb += MASS * (ps[a0].conj().T @ ps[a0]
                      - ps[a1].conj().T @ ps[a1])
    return Hb


E0bg = {}
for k in range(4):
    Hb = build_H_frozen_mu4(k)
    E0bg[k] = float(np.linalg.eigvalsh(Hb)[0])
print("   frozen-field E0(k_mu4):", {k: "%.6f" % E0bg[k] for k in E0bg})
spread_bg = max(E0bg.values()) - min(E0bg.values())
rep("T3 [seam pinning physical in the frozen-link limit]: mu4 clock "
    "SPLITS the fermion ground energies (spread %.4f > 0) with the "
    "conjugate pair k = 1, 3 degenerate (|dE| = %.1e) -- seam is a "
    "genuine boundary-module observable, not a Z6 gauge element"
    % (spread_bg, abs(E0bg[1] - E0bg[3])),
    spread_bg > 1e-6 and abs(E0bg[1] - E0bg[3]) < 1e-10
    and abs(E0bg[0] - E0bg[1]) > 1e-6)

# ---------------------------------------------------------------- T4
print("=== T4: anomaly bookkeeping (exact, actual TFPT content) ===")


def anomaly_sums(fields):
    y3 = sum(c * w * y ** 3 for _, c, w, y in fields)
    su2y = sum(c * y for _, c, w, y in fields if w == 2)
    su3y = sum(w * y for _, c, w, y in fields if c == 3)
    grav = sum(c * w * y for _, c, w, y in fields)
    witten = sum(c for _, c, w, y in fields if w == 2)
    return y3, su2y, su3y, grav, witten


y3, su2y, su3y, grav, witten = anomaly_sums(GEN)
print("   [U(1)]^3=%s  [SU(2)]^2U(1)=%s  [SU(3)]^2U(1)=%s  grav^2U(1)=%s  "
      "Witten=%d  (weights %s)" % (y3, su2y, su3y, grav, witten, WEIGHTS))
rep("T4 [exact]: [U(1)]^3 = %s, [SU(2)]^2U(1) = %s, [SU(3)]^2U(1) = %s, "
    "grav^2 U(1) = %s -- all vanish, with color/weak multiplicities as "
    "weights (Hilbert space uses one JW representative per multiplet)"
    % (y3, su2y, su3y, grav),
    y3 == su2y == su3y == grav == 0)
rep("T4 WITTEN [exact]: %d SU(2) doublets per generation (3 color + 1 "
    "lepton) -- even" % witten, witten % 2 == 0)
y3m, su2ym, su3ym, gravm, wittenm = anomaly_sums(
    [f for f in GEN if f[0] != "L"])
rep("T4 MUTANT FIRES: dropping L breaks [U(1)]^3, [SU(2)]^2U(1), grav "
    "and makes the Witten count odd",
    y3m != 0 and su2ym != 0 and gravm != 0 and wittenm % 2 == 1)

# ---------------------------------------------------------------- T7
print("=== T7: determinantal-law Gaussianity (fermion factor control) ===")
# four modes: Q0, Q1, L0, L1 -- two species, two sites (mirrors the
# 4-site product of today's Hamiltonian-route probe)
T7_MODES = [mode_index(0, 0), mode_index(0, 1),
            mode_index(3, 0), mode_index(3, 1)]


def gaussianity_full(Hsp, modes):
    """<prod n> vs det G on the full (link x fermion) space.
    Ground state via ARPACK; operators lifted sparsely."""
    Hs = ((Hsp + Hsp.conj().T) * 0.5).tocsr()
    wv, vv = eigsh(Hs, k=3, which="SA", tol=1e-10)
    order = np.argsort(wv.real)
    g = vv[:, order[0]]
    g = g / np.linalg.norm(g)
    gap = float(wv[order[1]].real - wv[order[0]].real)
    nmod = len(modes)
    G = np.zeros((nmod, nmod), dtype=complex)
    for i, ai in enumerate(modes):
        for j, aj in enumerate(modes):
            op = lift_F(PSI_F[ai].conj().T @ PSI_F[aj])
            G[i, j] = complex(np.vdot(g, op @ g))
    prod = np.ones(D, dtype=complex)
    for a in modes:
        # n = psi^dag psi is diagonal 0/1 on the fermion factor
        n_diag = np.array(NUM_F[a].diagonal()).ravel()
        n_full = np.tile(n_diag, DL)
        prod = prod * n_full
    lhs = complex(np.vdot(g, prod * g))
    rhs = np.linalg.det(G)
    return abs(lhs - rhs), gap, float(wv[order[0]].real)


dev_int, gap_int, e0_int = gaussianity_full(H, T7_MODES)
print("   interacting: |<prod n> - det G| = %.3e  gap = %.3f  E0 = %.4f"
      % (dev_int, gap_int, e0_int))


def free_control_fermion(modes):
    """Open staggered chain on the FERMION factor alone (dim 1024)."""
    Df = DF
    ps = [ferm_dense(a, NMODES) for a in range(NMODES)]
    Hb = np.zeros((Df, Df), dtype=complex)
    for s in range(NSPC):
        a0, a1 = mode_index(s, 0), mode_index(s, 1)
        hop = ps[a0].conj().T @ ps[a1]
        Hb += W_HOP * (hop + hop.conj().T)
        Hb += MASS * (ps[a0].conj().T @ ps[a0]
                      - ps[a1].conj().T @ ps[a1])
    wv, vv = np.linalg.eigh(Hb)
    g = vv[:, 0]
    nmod = len(modes)
    G = np.zeros((nmod, nmod), dtype=complex)
    for i, ai in enumerate(modes):
        for j, aj in enumerate(modes):
            G[i, j] = complex(g.conj() @ ((ps[ai].conj().T @ ps[aj]) @ g))
    prod = np.eye(Df, dtype=complex)
    for a in modes:
        prod = prod @ (ps[a].conj().T @ ps[a])
    lhs = complex(g.conj() @ (prod @ g))
    return abs(lhs - np.linalg.det(G)), float(wv[1] - wv[0])


dev_free, gap_free = free_control_fermion(T7_MODES)
print("   free fermion control: |<prod n> - det G| = %.1e  gap = %.3f"
      % (dev_free, gap_free))
rep("T7 [not generalized-free]: interacting GS VIOLATES the fermionic "
    "determinantal law by %.3e != 0 (gap %.3f), free control on the "
    "fermion factor satisfies det[G] to %.1e (gap %.3f) -- no "
    "link-degeneracy trap" % (dev_int, gap_int, dev_free, gap_free),
    dev_int > 1e-6 and dev_free < 1e-10 and gap_free > 1e-6)


# =====================================================================
# W[J] -- FTRANSFER.GENERATING at finite size (dim 96)
# =====================================================================
print("=== W[J]: generating functional at dim 96 (Q + e^c) ===")
W_CHARGES = [1, 0]                # Q, e^c
W_NSPC = 2
W_NMODES = W_NSPC * NS            # 4
W_DF = 2 ** W_NMODES              # 16
W_D = DL * W_DF                   # 96
BETA = 0.35
THETA0 = 0.7
MU_Q = 0.5          # breaks <N_Q>=1 particle-hole pinning so charge sees θ
EPS_J = 1.0e-4
EPS_TH = 1.0e-4

W_SZ = np.diag([1.0, -1.0])
W_ANN = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)


def w_ferm(alpha):
    out = np.array([[1.0]], dtype=complex)
    for j in range(W_NMODES):
        if j < alpha:
            out = np.kron(out, W_SZ)
        elif j == alpha:
            out = np.kron(out, W_ANN)
        else:
            out = np.kron(out, np.eye(2))
    return np.kron(np.eye(DL), out)


def w_link(M6):
    return np.kron(M6, np.eye(W_DF))


W_PSI = [w_ferm(a) for a in range(W_NMODES)]
W_NUM = [p.conj().T @ p for p in W_PSI]
W_X = w_link(X1)
W_Z = w_link(Z1)


def build_H_W(theta, lam_e=LAM_E, w=W_HOP, m=MASS, mu_q=MU_Q):
    """2-site, 1 quantum Z6, frozen closer e^{iθ}, species Q (q=1)
    and e^c (q=0).  mu_q N_Q breaks particle-hole pinning of <N_Q>."""
    Hm = -lam_e * (W_X + W_X.conj().T)
    for s, q in enumerate(W_CHARGES):
        a0, a1 = s * NS + 0, s * NS + 1
        Zq = np.linalg.matrix_power(W_Z, int(q) % 6)
        hop = W_PSI[a0].conj().T @ Zq @ W_PSI[a1]
        Hm = Hm + w * (hop + hop.conj().T)
        seam = (np.exp(1j * theta) ** q) * (
            W_PSI[a1].conj().T @ W_PSI[a0])
        Hm = Hm + w * (seam + seam.conj().T)
        Hm = Hm + m * (W_NUM[a0] - W_NUM[a1])
    Hm = Hm + mu_q * (W_NUM[0] + W_NUM[1])
    return Hm


def dH_dtheta(theta, w=W_HOP):
    """∂H/∂θ from the Q (q=1) seam hopping; e^c is θ-blind."""
    q = 1
    a0, a1 = 0, 1
    phase = np.exp(1j * theta) ** q
    # seam = w (e^{i q θ} ψ†_1 ψ_0 + e^{-i q θ} ψ†_0 ψ_1)
    dseam = (1j * q) * phase * (W_PSI[a1].conj().T @ W_PSI[a0])
    return w * (dseam + dseam.conj().T)


O_Q = W_NUM[0] + W_NUM[1]
O_Z = 0.5 * (W_Z + W_Z.conj().T)
O_C = W_NUM[2] + W_NUM[3]          # e^c charge, decoupled control
O_NAMES = ["Q-charge", "link (Z+Zdag)/2", "e^c-charge CONTROL"]
OPS = [O_Q, O_Z, O_C]
N_O = len(OPS)

H_W0 = build_H_W(THETA0)
herm_w = maxabs(H_W0 - H_W0.conj().T)
rep("W[J] H hermitian at θ0 (dev %.1e, dim %d)" % (herm_w, W_D),
    herm_w < 1e-12)


def log_tr_exp(A):
    ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
    m = float(ev.max())
    return m + float(np.log(np.sum(np.exp(ev - m))))


def W_gen(Js, theta):
    A = -BETA * build_H_W(theta)
    for j, O in zip(Js, OPS):
        A = A + j * O
    return log_tr_exp(A)


def thermal_pack(Hm):
    evals, evecs = np.linalg.eigh(0.5 * (Hm + Hm.conj().T))
    lam = -BETA * evals
    lam_s = lam - lam.max()
    ww = np.exp(lam_s)
    p = ww / ww.sum()
    return evals, evecs, p


def kubo_connected(Xe, Ye, p, evals):
    """Duhamel / Kubo inner product of X,Y in the energy basis of H,
    equal to ∂² log Tr exp(-βH + xX + yY) / ∂x∂y at 0.
    Xe[n,m] = <n|X|m>,  lam_n = -β E_n."""
    lam = -BETA * evals
    dlam = lam[None, :] - lam[:, None]          # λ_m - λ_n
    psi = np.ones_like(dlam, dtype=complex)
    mask = np.abs(dlam) > 1e-12
    psi[mask] = (np.exp(dlam[mask]) - 1.0) / dlam[mask]
    x_mean = complex(np.dot(p, np.diag(Xe)))
    y_mean = complex(np.dot(p, np.diag(Ye)))
    acc = np.sum(p[:, None] * psi * Xe * Ye.T)
    return acc - x_mean * y_mean


evals0, evecs0, p0 = thermal_pack(H_W0)
# observables in the energy basis
Oe = [evecs0.conj().T @ O @ evecs0 for O in OPS]
means = [complex(np.dot(p0, np.diag(Oe[a]))) for a in range(N_O)]

# (a) first derivatives
print("   --- (a) ∂W/∂J_a |_{J=0} vs thermal <O_a> ---")
print("   %-22s  %12s  %12s  %10s" % ("observable", "FD dW/dJ",
                                       "<O> direct", "|diff|"))
for a in range(N_O):
    Jp = [0.0] * N_O
    Jm = [0.0] * N_O
    Jp[a] = EPS_J
    Jm[a] = -EPS_J
    dW = (W_gen(Jp, THETA0) - W_gen(Jm, THETA0)) / (2.0 * EPS_J)
    diff = abs(dW - means[a].real)
    print("   %-22s  %12.6f  %12.6f  %10.2e"
          % (O_NAMES[a], dW, means[a].real, diff))
    rep("W(a) ∂W/∂J[%s] = <O> (diff %.1e)" % (O_NAMES[a], diff),
        diff < 1e-6)

# (b) Hessian vs Kubo connected correlators
print("   --- (b) ∂²W/∂J_a∂J_b vs Kubo <O_a; O_b>_c ---")
print("   %-22s %-22s  %12s  %12s  %10s"
      % ("O_a", "O_b", "FD Hess", "Kubo_c", "|diff|"))
for a in range(N_O):
    for b in range(a, N_O):
        if a == b:
            hess = (W_gen([EPS_J if i == a else 0.0 for i in range(N_O)],
                          THETA0)
                    - 2.0 * W_gen([0.0] * N_O, THETA0)
                    + W_gen([-EPS_J if i == a else 0.0 for i in range(N_O)],
                            THETA0)) / (EPS_J ** 2)
        else:
            def Jpair(sa, sb):
                Js = [0.0] * N_O
                Js[a] = sa * EPS_J
                Js[b] = sb * EPS_J
                return W_gen(Js, THETA0)
            hess = (Jpair(1, 1) - Jpair(1, -1) - Jpair(-1, 1)
                    + Jpair(-1, -1)) / (4.0 * EPS_J * EPS_J)
        kub = kubo_connected(Oe[a], Oe[b], p0, evals0)
        diff = abs(hess - kub.real)
        print("   %-22s %-22s  %12.6f  %12.6f  %10.2e"
              % (O_NAMES[a], O_NAMES[b], hess, kub.real, diff))
        rep("W(b) Hess[%s, %s] = Kubo_c (diff %.1e)"
            % (O_NAMES[a], O_NAMES[b], diff),
            diff < 5e-5)

# (c) mixed ∂²W/∂J_a∂θ vs Kubo(O, -β ∂H/∂θ)
print("   --- (c) mixed ∂²W/∂J_a∂θ  (transduction shadow) ---")
Kseam = -BETA * dH_dtheta(THETA0)
Ke = evecs0.conj().T @ Kseam @ evecs0
print("   %-22s  %12s  %12s  %10s  %s" % ("observable", "FD mixed",
                                           "Kubo seam", "|diff|",
                                           "shadow"))
mixed_vals = []
for a in range(N_O):
    def Wm(j, th, aa=a):
        Js = [0.0] * N_O
        Js[aa] = j
        return W_gen(Js, th)
    mixed = (Wm(EPS_J, THETA0 + EPS_TH) - Wm(EPS_J, THETA0 - EPS_TH)
             - Wm(-EPS_J, THETA0 + EPS_TH) + Wm(-EPS_J, THETA0 - EPS_TH)
             ) / (4.0 * EPS_J * EPS_TH)
    kub = kubo_connected(Oe[a], Ke, p0, evals0)
    diff = abs(mixed - kub.real)
    is_ctrl = (a == 2)
    tag = ("CONTROL ~ 0" if is_ctrl
           else ("FLUX-ABSORBED (N_Q)" if a == 0 else "SEAM-COUPLED"))
    mixed_vals.append((mixed, kub.real, diff, is_ctrl))
    print("   %-22s  %12.6e  %12.6e  %10.2e  %s"
          % (O_NAMES[a], mixed, kub.real, diff, tag))
    rep("W(c) mixed ∂²W/∂J[%s]∂θ = Kubo seam-response (diff %.1e)"
        % (O_NAMES[a], diff),
        diff < 5e-5)

m_Q, _, _, _ = mixed_vals[0]
m_Z, _, _, _ = mixed_vals[1]
m_C, _, _, _ = mixed_vals[2]
rep("W(c) dynamical-link TRANSDUCTION: link mixed = %.3e != 0, "
    "e^c CONTROL = %.3e = 0, Q-charge mixed = %.3e ~ 0 (fermion "
    "bilinear absorbed into the dynamical flux -- T3a lesson)"
    % (m_Z, m_C, m_Q),
    abs(m_Z) > 1e-6 and abs(m_C) < 1e-8 and abs(m_Q) < 1e-6)

# frozen-link companion: no quantum Z6, dim 16 -- seam is physical
# for fermion observables (T3b / boundary-module half)
print("   --- frozen-link companion W (dim 16): fermion transduction ---")
F_NMODES = 4
F_D = 2 ** F_NMODES


def f_ferm(alpha):
    out = np.array([[1.0]], dtype=complex)
    for j in range(F_NMODES):
        if j < alpha:
            out = np.kron(out, W_SZ)
        elif j == alpha:
            out = np.kron(out, W_ANN)
        else:
            out = np.kron(out, np.eye(2))
    return out


F_PSI = [f_ferm(a) for a in range(F_NMODES)]
F_NUM = [p.conj().T @ p for p in F_PSI]
F_STAG = F_NUM[0] - F_NUM[1]       # Q staggered density
F_C = F_NUM[2] + F_NUM[3]          # e^c charge
F_OPS = [F_STAG, F_C]
F_NAMES = ["Q-staggered", "e^c-charge CONTROL"]


def build_H_frozen_W(theta, w=W_HOP, m=MASS, mu_q=MU_Q):
    Hm = np.zeros((F_D, F_D), dtype=complex)
    for s, q in enumerate((1, 0)):
        a0, a1 = s * NS + 0, s * NS + 1
        hop = F_PSI[a0].conj().T @ F_PSI[a1]
        Hm = Hm + w * (hop + hop.conj().T)
        seam = (np.exp(1j * theta) ** q) * (F_PSI[a1].conj().T @ F_PSI[a0])
        Hm = Hm + w * (seam + seam.conj().T)
        Hm = Hm + m * (F_NUM[a0] - F_NUM[a1])
    Hm = Hm + mu_q * (F_NUM[0] + F_NUM[1])
    return Hm


def dH_frozen_dtheta(theta, w=W_HOP):
    phase = np.exp(1j * theta)
    dseam = 1j * phase * (F_PSI[1].conj().T @ F_PSI[0])
    return w * (dseam + dseam.conj().T)


def W_frozen(Js, theta):
    A = -BETA * build_H_frozen_W(theta)
    for j, O in zip(Js, F_OPS):
        A = A + j * O
    return log_tr_exp(A)


Hf0 = build_H_frozen_W(THETA0)
fevals, fevecs, fp = thermal_pack(Hf0)
FOe = [fevecs.conj().T @ O @ fevecs for O in F_OPS]
Kef = fevecs.conj().T @ (-BETA * dH_frozen_dtheta(THETA0)) @ fevecs
f_mixed = []
for a in range(2):
    def Wfm(j, th, aa=a):
        Js = [0.0, 0.0]
        Js[aa] = j
        return W_frozen(Js, th)
    mixed = (Wfm(EPS_J, THETA0 + EPS_TH) - Wfm(EPS_J, THETA0 - EPS_TH)
             - Wfm(-EPS_J, THETA0 + EPS_TH) + Wfm(-EPS_J, THETA0 - EPS_TH)
             ) / (4.0 * EPS_J * EPS_TH)
    kub = kubo_connected(FOe[a], Kef, fp, fevals)
    diff = abs(mixed - kub.real)
    print("   frozen %-18s  FD mixed = %12.6e  Kubo = %12.6e  "
          "|diff| = %.1e" % (F_NAMES[a], mixed, kub.real, diff))
    rep("W(c-frozen) mixed ∂²W/∂J[%s]∂θ = Kubo (diff %.1e)"
        % (F_NAMES[a], diff),
        diff < 5e-5)
    f_mixed.append(mixed)

rep("W(c-frozen) TRANSDUCTION SHADOW: with the closer FROZEN, "
    "Q-staggered mixed = %.3e != 0 while e^c CONTROL = %.3e = 0 "
    "-- the boundary-module half of OBS.TRANSDUCTION.01 from ONE W"
    % (f_mixed[0], f_mixed[1]),
    abs(f_mixed[0]) > 1e-6 and abs(f_mixed[1]) < 1e-8)


# =====================================================================
elapsed = time.perf_counter() - T0
print()
print("dims: content D = %d (Z6 x 5 species x 2 sites); "
      "T3 frozen DF = %d; W[J] dynamical D = %d; W[J] frozen D = %d; "
      "runtime %.2f s"
      % (D, DF, W_D, F_D, elapsed))
print("VERDICT: CONTENT_SHADOW_CANDIDATE_PASSES + WJ_MECHANISM_EXECUTED")
print("  Z6-centre / 6Y SHADOW of one SM generation on a 1+1D 2-site")
print("  Hamiltonian ring, plus a finite W[J] whose first two "
      "derivatives")
print("  reproduce thermal moments / connected correlators and whose")
print("  mixed seam derivative is the transduction shadow.  "
      "TFPT4D.LATTICE.ACTION.01")
print("  and FTRANSFER.GENERATING.01 stay [O] -- nothing closes.")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
