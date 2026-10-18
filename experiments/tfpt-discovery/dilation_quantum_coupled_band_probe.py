#!/usr/bin/env python3
"""dilation_quantum_coupled_band_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (DYN.UNITARY.DILATION.01 [O], the genuinely QUANTUM
interacting leg after dilation_field_os_uniform_probe executed the FREE
collision band and dilation_interacting_os_probe executed classical
DIAGONAL couplings): does the collision band survive a non-diagonal,
translation-invariant nearest-neighbour coupling of the SYSTEM qutrits?
Construction (one Floquet family):

    W_theta = U_int(theta) * (x)_x V_x ,
    U_int(theta) = exp(-i theta sum_x h_{x,x+1}) ,
    h = SWAP on C^3 (x) C^3  (hermitian, non-diagonal, ring-NN),
    V_x = C (U_B (x) I) the v977/v984 collision on (S_x, A_x),
    C|j,k> = |j, j+k mod 3|.

Each cell is a system qutrit plus an ancilla qutrit.  L = 3 (dim 729)
is the workhorse; L = 2 (dim 81) for structure cross-checks; L = 4
(dim 6561) only for a matrix-free far-cell commutator (never
materializing the 6561 x 6561 Floquet matrix).

  (1) UNITARITY: W_theta is unitary at every tested (L, theta)
      (product of unitaries; verified numerically).
  (2) RE-ANCHOR: at theta = 0, U_int = I, and the reduced per-cell
      DIAGONAL dynamics is EXACTLY B, independent of the neighbour
      state -- the free collision band is the theta = 0 point of the
      family.
  (3) LIEB-ROBINSON WITH INTERACTION.  W = U_int Wcoll applies the
      collision FIRST then the interaction, so the Heisenberg picture
      is Ad_Wcoll o Ad_U_int: U_int spreads a cell-local system
      operator onto NN systems, then EACH reached cell's V_x tags
      that cell's ancilla.  Expected STRICT radius
        R = r_int + r_coll = 1 + 0  (counted in cells; ancilla of
            an in-cone cell is in-cone).
      On the L = 3 ring the graph diameter equals R, so the WHOLE
      band (every S and every A) is in-cone -- verified by a full
      729 x 729 commutator table.  L = 4 has diameter 2 > R: the
      opposite cell (S2, A2) is a BCH tail of the Hamiltonian
      exponential (O(theta^2) vs on-cone O(theta)), measured
      matrix-free.  A RANGE-1 even-bond matching layer of the SAME
      SWAP family (the strict-cone skeleton) makes (S2, A2) vanish
      at machine precision -- the feasible exact far-cell zero.
  (4) CLASSICAL SHADOW DEFORMATION: d(theta) = max entrywise
      |M(theta) - B| of the reduced diagonal per-cell kernel, with
      neighbours in I/3 (homogeneous ring; |jjj> is a SWAP eigenstate
      so the free-probe all-equal protocol would hide the coupling).
      d(0) = 0 exactly; d(theta) -> 0 continuously with a fitted
      leading power O(theta) or O(theta^2).
  (5) MARKOV/CPTP: the reduced per-cell channel (same environment
      convention) stays CPTP at theta > 0 -- Choi PSD, trace
      preservation numerical-exact.  Openness survives coupling.

HONEST BOUNDARY (firewall): finite L, discrete time, ONE coupling
family (SU(3) exchange / SWAP).  The OS continuation of the COUPLED
quantum band, any continuum/Hamiltonian-limit statement, and any 3+1D
reading stay [O].  No marker move; no promotion.

VERDICT ENUM: QUANTUM_COUPLED_BAND_CONTROLLED
"""
import numpy as np
import sympy as sp

ok_all = True

THETAS = (0.0, 0.05, 0.1, 0.2, 0.4)
BF = np.array([[13.0, 1.0, 4.0], [1.0, 13.0, 4.0], [4.0, 4.0, 10.0]]) / 18.0
KET0 = np.diag([1.0, 0.0, 0.0])
MMIX = np.eye(3) / 3.0
LAM1 = np.zeros((3, 3), dtype=complex)
LAM1[0, 1] = LAM1[1, 0] = 1.0
ZGEN = np.diag([1.0, -1.0, 0.0]).astype(complex)
GENS = (LAM1, ZGEN)


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


# ----------------------------------------------------------------------
# v977 lift (copied) and collision V
# ----------------------------------------------------------------------
def build_lift(Bm, branch=+1):
    """exact PDG-parametrized lift of a symmetric doubly stochastic 3x3
    matrix; returns (U, s13sq, s12sq, s23sq, cos_delta, sin_delta).
    Copied from verification/v977_transfer_unistochastic_wilson.py."""
    s13sq = sp.nsimplify(Bm[0, 2])
    c13sq = 1 - s13sq
    s12sq = sp.nsimplify(Bm[0, 1] / c13sq)
    s23sq = sp.nsimplify(Bm[1, 2] / c13sq)
    c12sq, c23sq = 1 - s12sq, 1 - s23sq
    s12, c12 = sp.sqrt(s12sq), sp.sqrt(c12sq)
    s23, c23 = sp.sqrt(s23sq), sp.sqrt(c23sq)
    s13, c13 = sp.sqrt(s13sq), sp.sqrt(c13sq)
    cross = 2 * s12 * c12 * s23 * c23 * s13
    cosd = sp.simplify((Bm[1, 0] - s12sq * c23sq
                        - c12sq * s23sq * s13sq) / cross)
    sind = branch * sp.sqrt(sp.simplify(1 - cosd ** 2))
    eid = cosd + sp.I * sind
    U = sp.Matrix([
        [c12 * c13, s12 * c13, s13 / eid],
        [-s12 * c23 - c12 * s23 * s13 * eid,
         c12 * c23 - s12 * s23 * s13 * eid, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * eid,
         -c12 * s23 - s12 * c23 * s13 * eid, c23 * c13]])
    return U, s13sq, s12sq, s23sq, cosd, sind


def collision_V():
    Bm = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
    U, _, _, _, _, _ = build_lift(Bm, +1)
    Un = np.array([[complex(sp.N(U[i, j], 20)) for j in range(3)]
                   for i in range(3)])
    Cn = np.zeros((9, 9))
    for j in range(3):
        for k in range(3):
            Cn[j * 3 + ((j + k) % 3), j * 3 + k] = 1.0
    return Cn @ np.kron(Un, np.eye(3))


Vn = collision_V()


def swap_ring_H(L):
    """H = sum_x SWAP_{x,x+1} on L qutrits (system space only)."""
    D = 3 ** L
    H = np.zeros((D, D), dtype=float)
    for x in range(L):
        a, b = x, (x + 1) % L
        for s in range(D):
            digits = []
            r = s
            for _ in range(L):
                digits.append(r % 3)
                r //= 3
            digits = digits[::-1]
            nd = digits[:]
            nd[a], nd[b] = nd[b], nd[a]
            t = 0
            for d in nd:
                t = t * 3 + d
            H[t, s] += 1.0
    return H


def U_int_sys(L, theta):
    H = swap_ring_H(L)
    w, v = np.linalg.eigh(H)
    return v @ np.diag(np.exp(-1j * theta * w)) @ v.T


def interleaved_to_sysanc(L):
    """p[interleaved_index] = sys-then-anc index.
    interleaved layout: S0 A0 S1 A1 ... ; sysanc: S0 S1 ... A0 A1 ..."""
    D = 3 ** (2 * L)
    p = np.empty(D, dtype=np.int64)
    for s in range(D):
        digits = []
        r = s
        for _ in range(2 * L):
            digits.append(r % 3)
            r //= 3
        digits = digits[::-1]
        sys_d = [digits[2 * x] for x in range(L)]
        anc_d = [digits[2 * x + 1] for x in range(L)]
        t = 0
        for d in sys_d + anc_d:
            t = t * 3 + d
        p[s] = t
    return p


def embed_U_int(L, theta):
    """U_int on the interleaved (S,A)^L space via U_sys (x) I_anc."""
    Us = U_int_sys(L, theta)
    U_sa = np.kron(Us, np.eye(3 ** L, dtype=complex))
    p = interleaved_to_sysanc(L)
    return U_sa[np.ix_(p, p)]


def Wcoll(L):
    W = np.array([[1.0]], dtype=complex)
    for _ in range(L):
        W = np.kron(W, Vn)
    return W


def floquet_W(L, theta):
    return embed_U_int(L, theta) @ Wcoll(L)


def op_on(L, factor, M):
    out = np.array([[1.0]], dtype=complex)
    for f in range(2 * L):
        out = np.kron(out, M if f == factor else np.eye(3))
    return out


def labels_of(L):
    lab = []
    for x in range(L):
        lab.extend(["S%d" % x, "A%d" % x])
    return lab


def product_rho(L, probe_rho, other_sys):
    rho = np.array([[1.0]], dtype=complex)
    for x in range(L):
        rho = np.kron(rho, probe_rho if x == 0 else other_sys)
        rho = np.kron(rho, KET0)
    return rho


def partial_trace_keep(rho, L, keep):
    dims = [3] * (2 * L)
    red = rho.reshape(dims + dims)
    for f in sorted((f for f in range(2 * L) if f != keep), reverse=True):
        n = red.ndim // 2
        red = np.trace(red, axis1=f, axis2=f + n)
    return red


def diag_kernel(W, L, other_sys=MMIX):
    """3x3 reduced diagonal kernel of cell 0: columns = images of |j><j|."""
    cols = []
    for j in range(3):
        rho = np.zeros((3, 3), dtype=complex)
        rho[j, j] = 1.0
        big = W @ product_rho(L, rho, other_sys) @ W.conj().T
        red = partial_trace_keep(big, L, 0)
        cols.append(np.real(np.diag(red)))
    return np.array(cols).T


def reduced_Phi(W, L, rho_in, other_sys=MMIX):
    big = W @ product_rho(L, rho_in, other_sys) @ W.conj().T
    return partial_trace_keep(big, L, 0)


def choi_of(W, L, other_sys=MMIX):
    J = np.zeros((9, 9), dtype=complex)
    for i in range(3):
        for j in range(3):
            rho = np.zeros((3, 3), dtype=complex)
            rho[i, j] = 1.0
            out = reduced_Phi(W, L, rho, other_sys)
            for a in range(3):
                for b in range(3):
                    J[i * 3 + a, j * 3 + b] = out[a, b]
    return J


def commutator_support(W, L, O0):
    O1 = W.conj().T @ O0 @ W
    support = []
    for f in range(2 * L):
        dev = max(np.max(np.abs(O1 @ op_on(L, f, g) - op_on(L, f, g) @ O1))
                  for g in GENS)
        support.append(float(dev))
    return support


# ----------------------------------------------------------------------
# L = 4 matrix-free apply (never form the 6561 x 6561 Floquet matrix)
# ----------------------------------------------------------------------
def _apply_on_axes(psi, axes, M, n_phys):
    k = len(axes)
    order = list(axes) + [i for i in range(n_phys) if i not in axes]
    if psi.ndim > n_phys:
        order = order + [n_phys]
    psi_p = np.transpose(psi, order)
    rest = psi_p.shape[k:]
    psi_p = M @ psi_p.reshape(3 ** k, -1)
    psi_p = psi_p.reshape([3] * k + list(rest))
    return np.transpose(psi_p, np.argsort(order))


def apply_W_batch(psi, L, Us, adjoint=False):
    """psi: (3,)*(2L) or (3,)*(2L)+(batch,).  W = U_int Wcoll.
    adjoint=True applies W^dag = Wcoll^dag U_int^dag."""
    n_phys = 2 * L
    Vgate = Vn.conj().T if adjoint else Vn
    Ugate = Us.conj().T if adjoint else Us
    sys_axes = [2 * x for x in range(L)]
    if adjoint:
        psi = _apply_on_axes(psi, sys_axes, Ugate, n_phys)
        for x in range(L):
            psi = _apply_on_axes(psi, [2 * x, 2 * x + 1], Vgate, n_phys)
    else:
        for x in range(L):
            psi = _apply_on_axes(psi, [2 * x, 2 * x + 1], Vgate, n_phys)
        psi = _apply_on_axes(psi, sys_axes, Ugate, n_phys)
    return psi


def swap9():
    S = np.zeros((9, 9), dtype=complex)
    for i in range(3):
        for j in range(3):
            S[j * 3 + i, i * 3 + j] = 1.0
    return S


def exp_iswap(theta):
    """exp(-i theta SWAP) = cos(theta) I - i sin(theta) SWAP on C3 x C3."""
    return np.cos(theta) * np.eye(9, dtype=complex) - 1j * np.sin(theta) * swap9()


def apply_W_even_batch(psi, L, theta, adjoint=False):
    """Range-1 matching layer: W = U_even Wcoll with
    U_even = prod_{x even} exp(-i theta SWAP_{S_x, S_{x+1}}).
    Even bonds are disjoint so they commute; L even."""
    n_phys = 2 * L
    Vgate = Vn.conj().T if adjoint else Vn
    U2 = exp_iswap(-theta if adjoint else theta)
    even = list(range(0, L, 2))

    def apply_even(state):
        for x in even:
            y = (x + 1) % L
            state = _apply_on_axes(state, [2 * x, 2 * y], U2, n_phys)
        return state

    if adjoint:
        psi = apply_even(psi)
        for x in range(L):
            psi = _apply_on_axes(psi, [2 * x, 2 * x + 1], Vgate, n_phys)
    else:
        for x in range(L):
            psi = _apply_on_axes(psi, [2 * x, 2 * x + 1], Vgate, n_phys)
        psi = apply_even(psi)
    return psi


def apply_local_batch(psi, L, factor, M):
    return _apply_on_axes(psi, [factor], M, 2 * L)


def commutator_dev_apply(L, apply_W, Oloc, factor_O, Gloc, factor_G,
                         n_haar=24, n_basis=81, seed=0):
    """max |([Ad_W(O), G] |psi>)_j| on a Haar batch plus the first
    `n_basis` computational-basis states.  Exhaustive 6561-column
    assembly would materialize a 6561 x 6561 operator (~688 MB) --
    this is the documented memory-efficient witness."""
    dim = 3 ** (2 * L)
    n_phys = 2 * L
    rng = np.random.default_rng(seed)

    def apply_Oprime(psi):
        psi = apply_W(psi, adjoint=False)
        psi = apply_local_batch(psi, L, factor_O, Oloc)
        return apply_W(psi, adjoint=True)

    def apply_G(psi):
        return apply_local_batch(psi, L, factor_G, Gloc)

    haar = rng.normal(size=(dim, n_haar)) + 1j * rng.normal(size=(dim, n_haar))
    haar /= np.linalg.norm(haar, axis=0, keepdims=True)
    n_b = min(n_basis, dim)
    basis = np.zeros((dim, n_b), dtype=complex)
    for i in range(n_b):
        basis[i, i] = 1.0
    B = np.concatenate([haar, basis], axis=1)
    psi = B.reshape([3] * n_phys + [B.shape[1]])
    OG = apply_Oprime(apply_G(psi)).reshape(dim, -1)
    GO = apply_G(apply_Oprime(psi)).reshape(dim, -1)
    return float(np.max(np.abs(OG - GO)))


# ======================================================================
print("=== (1) construction: SWAP-ring U_int and unitarity of W_theta ===")
H2 = swap_ring_H(2)
off = float(np.max(np.abs(H2 - np.diag(np.diag(H2)))))
rep("h = SWAP on C3 x C3 is hermitian and NON-DIAGONAL (max off-diag "
    "%.3f); H = sum_x h_{x,x+1} is translation-invariant on the ring"
    % off, np.allclose(H2, H2.T) and off > 0.5)

ok_U = True
unit_report = {}
for L in (2, 3):
    for th in (0.0, 0.1, 0.4):
        W = floquet_W(L, th)
        D = W.shape[0]
        err = float(np.max(np.abs(W.conj().T @ W - np.eye(D))))
        unit_report[(L, th)] = err
        ok_U &= err < 1e-10
rep("W_theta = U_int(theta) (x)_x V_x is unitary at L = 2,3 and "
    "theta in {0, 0.1, 0.4} (max ||W^dag W - I||_max = %.1e)"
    % max(unit_report.values()), ok_U,
    extra="errs " + str({k: "%.1e" % v for k, v in unit_report.items()}))

print("=== (2) re-anchor: theta = 0 reduced diagonal channel is B ===")
ok_B = True
for L in (2, 3):
    W0 = floquet_W(L, 0.0)
    for env, tag in ((MMIX, "mixed neighbours"),
                     (KET0, "neighbours |0>"),
                     (np.eye(3) / 3.0, "I/3")):
        M = diag_kernel(W0, L, other_sys=env)
        dev = float(np.max(np.abs(M - BF)))
        ok_B &= dev < 1e-10
        print("   L = %d, %s: max |M(0) - B| = %.1e" % (L, tag, dev))
rep("at theta = 0 the reduced per-cell diagonal dynamics is EXACTLY B "
    "at L = 2, 3 for every tested neighbour state -- the free collision "
    "band is the theta = 0 point of the family, not an isolated accident",
    ok_B)

print("=== (3) Lieb-Robinson with interaction ===")
print("   Heisenberg picture of W = U_int Wcoll: Ad_Wcoll o Ad_U_int")
print("   expected STRICT radius R = r_int + r_coll = 1 cell/step")
print("   (NN system coupling, then on-cell collision tags that ancilla)")
print("   L = 3 ring diameter = 1 = R: the WHOLE band is in-cone.")

L = 3
W0 = floquet_W(L, 0.0)
Wint = floquet_W(L, 0.2)
O0 = op_on(L, 0, LAM1)
sup0 = commutator_support(W0, L, O0)
supi = commutator_support(Wint, L, O0)
lab = labels_of(L)
print("   commutators after 1 step, theta = 0:  ",
      {lab[f]: "%.1e" % sup0[f] for f in range(2 * L)})
print("   commutators after 1 step, theta = 0.2:",
      {lab[f]: "%.1e" % supi[f] for f in range(2 * L)})

far0 = all(sup0[f] < 1e-10 for f in range(2 * L) if f not in (0, 1))
near0 = sup0[0] > 1e-6 and sup0[1] > 1e-6
rep("LR theta = 0 [L = 3]: S0-local operator stays on {S0, A0} "
    "(foreign factors < 1e-10) and the on-cell collision is STRICT "
    "(nonzero on S0 and A0) -- free-band cone recovered",
    far0 and near0)

filled = all(supi[f] > 1e-8 for f in range(2 * L))
rep("LR theta = 0.2 [L = 3, radius accounting]: every factor "
    "(S0,A0,S1,A1,S2,A2) is in the R = 1 cone on the 3-ring and "
    "lights up (min dev %.1e) -- diameter = R, no far cell exists; "
    "Ad_U_int reaches both neighbours, then each V_x tags that "
    "cell's ancilla" % min(supi), filled)

print("   L = 4 matrix-free commutators (dim 6561, Haar+basis matvec)...")
L4 = 4
Us4 = U_int_sys(L4, 0.2)
Us4_0 = U_int_sys(L4, 0.0)


def _W_ham(psi, adjoint=False, Us=None):
    return apply_W_batch(psi, L4, Us, adjoint=adjoint)


dev_S1 = commutator_dev_apply(
    L4, lambda p, adjoint=False: _W_ham(p, adjoint, Us4),
    LAM1, 0, LAM1, 2)
dev_A1 = commutator_dev_apply(
    L4, lambda p, adjoint=False: _W_ham(p, adjoint, Us4),
    LAM1, 0, LAM1, 3)
dev_S2 = commutator_dev_apply(
    L4, lambda p, adjoint=False: _W_ham(p, adjoint, Us4),
    LAM1, 0, LAM1, 4)
dev_A2 = commutator_dev_apply(
    L4, lambda p, adjoint=False: _W_ham(p, adjoint, Us4),
    LAM1, 0, LAM1, 5)
dev_A2_0 = commutator_dev_apply(
    L4, lambda p, adjoint=False: _W_ham(p, adjoint, Us4_0),
    LAM1, 0, LAM1, 5)
print("   L = 4 Hamiltonian theta = 0.2:")
print("      on-cone  S1 = %.1e  A1 = %.1e" % (dev_S1, dev_A1))
print("      opposite S2 = %.1e  A2 = %.1e  (BCH tails)" % (dev_S2, dev_A2))
print("      theta = 0 opposite A2 = %.1e" % dev_A2_0)
ratio = max(dev_S2, dev_A2) / max(dev_S1, 1e-30)
rep("LR L = 4 Hamiltonian: opposite cell (S2, A2) is a BCH tail "
    "(max %.1e) vs on-cone S1 = %.1e, ratio %.2f < 1; at theta = 0 "
    "the opposite cell is dark (A2 = %.1e) -- the R = 1 cone "
    "inequality holds; the tail is the honest price of exp(-i theta "
    "sum_x h)" % (max(dev_S2, dev_A2), dev_S1, ratio, dev_A2_0),
    dev_S1 > 1e-6 and dev_A1 > 1e-8
    and max(dev_S2, dev_A2) < 0.5 * dev_S1
    and dev_A2_0 < 1e-10)

print("   L = 4 RANGE-1 even-bond matching (strict cone skeleton)...")
TH_EVEN = 0.2


def _W_even(psi, adjoint=False):
    return apply_W_even_batch(psi, L4, TH_EVEN, adjoint=adjoint)


ev_S1 = commutator_dev_apply(L4, _W_even, LAM1, 0, LAM1, 2)
ev_A1 = commutator_dev_apply(L4, _W_even, LAM1, 0, LAM1, 3)
ev_S2 = commutator_dev_apply(L4, _W_even, LAM1, 0, LAM1, 4)
ev_A2 = commutator_dev_apply(L4, _W_even, LAM1, 0, LAM1, 5)
ev_S3 = commutator_dev_apply(L4, _W_even, LAM1, 0, LAM1, 6)
print("   even-layer theta = 0.2: S1 = %.1e A1 = %.1e | "
      "S2 = %.1e A2 = %.1e | S3 = %.1e"
      % (ev_S1, ev_A1, ev_S2, ev_A2, ev_S3))
rep("LR L = 4 STRICT far cell: the even-bond matching layer of the "
    "same SWAP family has cone radius 1, so opposite (S2, A2) AND "
    "the unmatched neighbour S3 vanish at machine precision "
    "(%.1e, %.1e, %.1e < 1e-10) while the matched neighbour (S1, A1) "
    "lights up -- this is the feasible exact far-cell zero on dim 6561"
    % (ev_S2, ev_A2, ev_S3),
    ev_S1 > 1e-6 and ev_A1 > 1e-8
    and ev_S2 < 1e-10 and ev_A2 < 1e-10 and ev_S3 < 1e-10)

print("=== (4) classical shadow deformation d(theta) ===")
L = 3
W_cache = {th: floquet_W(L, th) for th in THETAS}
dth = {}
kernels = {}
for th in THETAS:
    M = diag_kernel(W_cache[th], L, other_sys=MMIX)
    kernels[th] = M
    dth[th] = float(np.max(np.abs(M - BF)))
    print("   d(%.2f) = %.6e" % (th, dth[th]))

rep("d(0) = 0 exactly (max |M(0) - B| = %.1e)" % dth[0.0],
    dth[0.0] < 1e-10)

ths_pos = np.array([th for th in THETAS if th > 0.0])
ds_pos = np.array([dth[th] for th in ths_pos])
ok_deform = bool(np.all(ds_pos > 1e-8))
ok_cont = bool(dth[0.05] < dth[0.1] < dth[0.2])
# leading power from the three smallest positive thetas
fit_th = np.array([0.05, 0.1, 0.2])
fit_d = np.array([dth[th] for th in fit_th])
power = float(np.polyfit(np.log(fit_th), np.log(fit_d), 1)[0])
print("   fitted leading power (theta in {0.05,0.1,0.2}):  "
      "d(theta) ~ C theta^{%.3f}" % power)
# also report the four-point fit
power4 = float(np.polyfit(np.log(ths_pos), np.log(ds_pos), 1)[0])
print("   four-point fit including 0.4:                    "
      "d(theta) ~ C theta^{%.3f}" % power4)
rep("d(theta) -> 0 continuously (monotone on {0.05,0.1,0.2}; d(0.05) = "
    "%.3e) and the interacting band DEFORMS B at theta > 0 "
    "(min d = %.3e)" % (dth[0.05], float(np.min(ds_pos))),
    ok_deform and ok_cont)
rep("leading power in {1, 2} neighbourhood (fit %.3f; expect O(theta) "
    "or O(theta^2) -- the corpus transfer B is the theta = 0 point of "
    "a CONTROLLABLE family)" % power,
    0.6 <= power <= 2.8)

print("=== (5) Markov/CPTP: reduced per-cell channel stays open ===")
choi_eigs = {}
tp_devs = {}
ok_cptp = True
for th in (0.0, 0.1, 0.2, 0.4):
    J = choi_of(W_cache[th], L, other_sys=MMIX)
    Jh = 0.5 * (J + J.conj().T)
    eigs = np.linalg.eigvalsh(Jh)
    choi_eigs[th] = float(eigs[0])
    tp = 0.0
    for i in range(3):
        for j in range(3):
            s = 0.0
            for a in range(3):
                s += J[i * 3 + a, j * 3 + a]
            tp = max(tp, abs(s - (1.0 if i == j else 0.0)))
    tp_devs[th] = float(tp)
    herm = float(np.max(np.abs(J - J.conj().T)))
    ok_cptp &= eigs[0] > -1e-9 and tp < 1e-10 and herm < 1e-10
    print("   theta = %.2f:  min eig Choi = %.4e,  TP dev = %.1e,  "
          "herm dev = %.1e" % (th, eigs[0], tp, herm))
rep("reduced per-cell channel is CPTP at theta in {0, 0.1, 0.2, 0.4}: "
    "Choi PSD (min eig %.3e) and trace preservation exact (max TP "
    "dev %.1e) -- the collision openness SURVIVES the quantum coupling"
    % (min(choi_eigs.values()), max(tp_devs.values())),
    ok_cptp)

print()
print("VERDICT: QUANTUM_COUPLED_BAND_CONTROLLED -- W_theta is a "
      "unitary Floquet family whose theta = 0 slice is the free "
      "collision band (reduced diagonal = B); a SWAP-ring coupling "
      "deforms that shadow continuously (leading power %.2f) while "
      "keeping the reduced channel CPTP; the LR cone is R = 1 "
      "(L = 3 fills the ring; L = 4 Hamiltonian tails vs a range-1 "
      "matching layer with machine-zero far cell).  OS continuation "
      "of the COUPLED quantum band stays [O]; no promotion." % power)
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
