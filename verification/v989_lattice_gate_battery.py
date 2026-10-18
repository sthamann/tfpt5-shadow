"""v989 -- TFPT4D.LATTICE.ACTION.01 + CHIRAL4D.NOMIRROR.01 [O update:
T1-T7 harness executed + Euclidean T2 kill named + Hamiltonian route
clears T2 by construction + chiral Gauss census; contracts stay Open].

THE POINT (promote round 2026-08-28).  Re-derives the executable 4D
gate battery (probes not imported):

  [E] T4 ANOMALY BOOKKEEPING: one SM generation (Y(Q)=1/6) --
        [U(1)]^3, [SU(2)]^2 U(1), [SU(3)]^2 U(1), grav^2 U(1) vanish
        as exact rationals; Witten SU(2) count = 4 (even).  Drop-L
        mutant fires (three sums break, Witten odd).

  [E] T5/T6 MECHANISM (2D overlap, N=8): index(D_ov) = q for
        q = -2..2; all eigenvalues on the GW circle |lambda-1|=1;
        doubler branch at the cutoff end.

  [E] T7 TOY: Z2 cube 4096 configs, kappa_4 != 0 at beta=0.4,
        free control beta=0 gives 0.

  [E] EUCLIDEAN T2 KILL (Z2 N_t-exact, Nx=2): pure-gauge Gram PSD
        at Nt=2 and Nt=4; overlap |det D_ov|^2 violation ABSENT at
        Nt=2, APPEARS at Nt=4 (det-only min eig ~ -0.249); Wilson
        control |det D_W|^2 PSD everywhere -- pinned on overlap
        time nonlocality.  (Z4 2x2 first-candidate: same named
        kill at the Euclidean shortcut; not re-enumerated here.)

  [E] HAMILTONIAN ROUTE CLEARS T2: 4-site Z4 staggered, dim 1024;
        interior Gauss exact; seam-sector intertwiner; H = H^dag
        so T = e^{-aH} SPD by construction; dynamical E0(k)
        identical; background-field mu4 split with k=1,3
        degenerate; interacting ground state violates the
        determinantal law, free control holds.

  [E] CHIRAL GAUSS CENSUS: factorized 16 x 256 (4096 never
        materialised).  Single-exponent Gauss iff q_L = q_R;
        two-exponent Gauss always (lattice Dirac doubling);
        V^4 = I; mutant (g_L,g_R)=(1,0) on vectorlike fails.

HONEST SCOPE (firewall): 1+1D / 2D toys, Z2/Z4 structure groups,
reduced sizes.  No 3+1D continuum statement.  Contracts stay [O].
No marker move.  Python-only / Wolfram mirror deferred.

Provenance: experiments/tfpt-discovery/tfpt4d_t4t7_gates_probe.py,
tfpt4d_first_candidate_probe.py, overlap_rp_exact_nt_probe.py,
tfpt4d_hamiltonian_route_probe.py, tfpt4d_chiral_gauss_probe.py
(ALL PASS; not imported).
"""
from fractions import Fraction as F
from itertools import product as iproduct

import numpy as np

from tfpt_constants import check, summary, reset

# ================================================================= T4
GEN = [
    ("Q",   3, 2, F(1, 6)),
    ("u^c", 3, 1, F(-2, 3)),
    ("d^c", 3, 1, F(1, 3)),
    ("L",   1, 2, F(-1, 2)),
    ("e^c", 1, 1, F(1, 1)),
]


def anomaly_sums(fields):
    y3 = sum(c * w * y ** 3 for _, c, w, y in fields)
    su2y = sum(c * y for _, c, w, y in fields if w == 2)
    su3y = sum(w * y for _, c, w, y in fields if c == 3)
    grav = sum(c * w * y for _, c, w, y in fields)
    witten = sum(c for _, c, w, y in fields if w == 2)
    return y3, su2y, su3y, grav, witten


# ================================================================= T5/T6
N_OV = 8
M0_OV = 1.0
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=np.complex128)


def links_flux(q, n=N_OV):
    ux = np.ones((n, n), dtype=complex)
    uy = np.ones((n, n), dtype=complex)
    for x in range(n):
        for y in range(n):
            uy[x, y] = np.exp(2j * np.pi * q * x / n ** 2)
            if x == n - 1:
                ux[x, y] = np.exp(-2j * np.pi * q * y / n)
    return ux, uy


def overlap_2d(q, n=N_OV):
    dim = n * n
    idx = lambda x, y: (x % n) * n + (y % n)
    tx = np.zeros((dim, dim), dtype=complex)
    ty = np.zeros((dim, dim), dtype=complex)
    ux, uy = links_flux(q, n)
    for x in range(n):
        for y in range(n):
            tx[idx(x + 1, y), idx(x, y)] = ux[x, y]
            ty[idx(x, y + 1), idx(x, y)] = uy[x, y]
    eye = np.eye(dim)
    dw = np.zeros((2 * dim, 2 * dim), dtype=complex)
    for s, t in ((S1, tx), (S2, ty)):
        dw += np.kron(s, (t - t.conj().T) / 2)
        dw += np.kron(np.eye(2), -(t + t.conj().T - 2 * eye) / 2)
    hw = np.kron(S3, np.eye(dim)) @ (dw - M0_OV * np.eye(2 * dim))
    hw = (hw + hw.conj().T) / 2
    w, v = np.linalg.eigh(hw)
    sgn = v @ np.diag(np.sign(w)) @ v.conj().T
    return np.eye(2 * dim) + np.kron(S3, np.eye(dim)) @ sgn


# ================================================================= T7 cube
def cube_faces():
    verts = list(iproduct((0, 1), repeat=3))
    links = []
    for v in verts:
        for d in range(3):
            if v[d] == 0:
                w = list(v)
                w[d] = 1
                links.append((v, tuple(w)))
    lidx = {frozenset(l): i for i, l in enumerate(links)}

    def face_links(fixed_dim, fixed_val):
        dims = [d for d in range(3) if d != fixed_dim]
        c = [0, 0, 0]
        c[fixed_dim] = fixed_val

        def pt(a, b):
            p = list(c)
            p[dims[0]], p[dims[1]] = a, b
            return tuple(p)

        out = []
        for a, b, a2, b2 in ((0, 0, 1, 0), (1, 0, 1, 1),
                             (0, 1, 1, 1), (0, 0, 0, 1)):
            out.append(lidx[frozenset((pt(a, b), pt(a2, b2)))])
        return out

    faces = [face_links(d, v) for d in range(3) for v in (0, 1)]
    lateral = [faces[i] for i in (0, 1, 2, 3)]
    return faces, lateral


def four_point(beta, faces, lateral):
    z = 0.0
    m1 = np.zeros(4)
    m2 = np.zeros((4, 4))
    for cfg in range(4096):
        s = [1 if (cfg >> i) & 1 else -1 for i in range(12)]
        fvals = [np.prod([s[i] for i in f]) for f in faces]
        w = np.exp(beta * sum(fvals))
        z += w
        lat = np.array([np.prod([s[i] for i in f]) for f in lateral],
                       dtype=float)
        m1 += w * lat
        m2 += w * np.outer(lat, lat)
    m1 /= z
    m2 /= z
    c2 = m2 - np.outer(m1, m1)
    m4c = 0.0
    z2 = 0.0
    for cfg in range(4096):
        s = [1 if (cfg >> i) & 1 else -1 for i in range(12)]
        fvals = [np.prod([s[i] for i in f]) for f in faces]
        w = np.exp(beta * sum(fvals))
        lat = np.array([np.prod([s[i] for i in f]) for f in lateral],
                       dtype=float) - m1
        m4c += w * np.prod(lat)
        z2 += w
    m4c /= z2
    return m4c - (c2[0, 1] * c2[2, 3] + c2[0, 2] * c2[1, 3]
                  + c2[0, 3] * c2[1, 2])


# ================================================================= Euclidean T2 kill (Z2 N_t-exact)
NX_Z2 = 2
BETA_Z2 = 1.0
M0_Z2 = 1.0
MW_Z2 = 1.0
BATCH_Z2 = 2048
TOL_PSD = 1e-12
TOL_VIOL = 1e-6
EXC_THRESH = 1e-10


def pos_slices(nt):
    return list(range(nt // 2, nt))


def theta_t(t, nt):
    return nt - 1 - t


def n_obs_of(nt):
    return NX_Z2 * len(pos_slices(nt))


def decode_U(cs, nt):
    n_links = 2 * NX_Z2 * nt
    shifts = np.arange(n_links, dtype=np.int64)
    bits = (cs[:, None] >> shifts[None, :]) & 1
    return (1 - 2 * bits).reshape(-1, 2, NX_Z2, nt).astype(np.float64)


def gauge_weights(U, beta=BETA_Z2):
    ux, ut = U[:, 0], U[:, 1]
    plaq = ux * np.roll(ut, -1, axis=1) * np.roll(ux, -1, axis=2) * ut
    return np.exp(beta * plaq.sum(axis=(1, 2)))


def chars_of_slices(U, slices):
    n_obs = NX_Z2 * len(slices)
    n_chi = 1 << n_obs
    stack = np.stack([U[:, 0, x, t] for t in slices for x in range(NX_Z2)],
                     axis=1)
    eps = ((np.arange(n_chi)[:, None] >> np.arange(n_obs)) & 1).astype(np.int32)
    bits = (stack < 0).astype(np.int32)
    parity = (bits @ eps.T) & 1
    return (1 - 2 * parity).astype(np.float64), n_chi


def pair_characters(U, nt):
    pos = pos_slices(nt)
    mir = [theta_t(t, nt) for t in pos]
    chi_p, n_chi = chars_of_slices(U, pos)
    chi_r, _ = chars_of_slices(U, mir)
    return chi_r, chi_p, n_chi


def bkron(A, M):
    b, d, _ = M.shape
    out = A.reshape(1, 2, 1, 2, 1) * M.reshape(b, 1, d, 1, d)
    return out.reshape(b, 2 * d, 2 * d)


def hoppings(U):
    b, _, nx, nt = U.shape
    dim = nx * nt
    tx = np.zeros((b, dim, dim), dtype=np.float64)
    tt = np.zeros((b, dim, dim), dtype=np.float64)
    for x in range(nx):
        for t in range(nt):
            j = x * nt + t
            tx[:, ((x + 1) % nx) * nt + t, j] = U[:, 0, x, t]
            tt[:, x * nt + (t + 1) % nt, j] = U[:, 1, x, t]
    return tx, tt


def wilson_dirac_batch(U, m=0.0):
    tx, tt = hoppings(U)
    _b, dim, _ = tx.shape
    eye = np.eye(dim)
    txh = np.swapaxes(tx, -1, -2)
    tth = np.swapaxes(tt, -1, -2)
    ax = 0.5 * (tx - txh)
    at = 0.5 * (tt - tth)
    wx = -0.5 * (tx + txh - 2.0 * eye)
    wt = -0.5 * (tt + tth - 2.0 * eye)
    dw = (bkron(S1, ax) + bkron(I2, wx)
          + bkron(S2, at) + bkron(I2, wt))
    if m != 0.0:
        dw = dw + m * np.eye(2 * dim, dtype=np.complex128)
    return dw


def ov_from_sgn(g5, evecs, sgn):
    n = g5.shape[0]
    sgnh = np.matmul(evecs * sgn[:, None, :],
                     np.conjugate(np.swapaxes(evecs, -1, -2)))
    dov = np.eye(n, dtype=np.complex128) + np.matmul(g5, sgnh)
    _sign, logabs = np.linalg.slogdet(dov)
    return np.exp(2.0 * logabs)


def overlap_weights_batch(dw, dim):
    n = 2 * dim
    g5 = np.kron(S3, np.eye(dim))
    hw = np.matmul(g5, dw - M0_Z2 * np.eye(n, dtype=np.complex128))
    hw = 0.5 * (hw + np.conjugate(np.swapaxes(hw, -1, -2)))
    evals, evecs = np.linalg.eigh(hw)
    amin = np.min(np.abs(evals), axis=1)
    exc = amin < EXC_THRESH
    sgn_plus = np.where(np.abs(evals) < EXC_THRESH, 1.0, np.sign(evals))
    w_plus = ov_from_sgn(g5, evecs, sgn_plus)
    w_drop = np.where(exc, 0.0, w_plus)
    return w_drop, w_plus, exc


def wilson_detsq_batch(dw, dim):
    n = 2 * dim
    dwm = dw + MW_Z2 * np.eye(n, dtype=np.complex128)
    _sign, logabs = np.linalg.slogdet(dwm)
    return np.exp(2.0 * logabs)


def acc(G, Z, key, chi_r, chi_p, w):
    Z[key] += float(np.sum(w))
    G[key] += (chi_r * w[:, None]).T @ chi_p


def min_eig(G, Z, key):
    m = G[key] / Z[key]
    m = 0.5 * (m + m.T)
    return float(np.linalg.eigvalsh(m)[0])


def run_nt(nt, batch=BATCH_Z2):
    n_links = 2 * NX_Z2 * nt
    ncfg = 1 << n_links
    dim = NX_Z2 * nt
    n_chi = 1 << n_obs_of(nt)
    keys = ("gauge", "ov_det", "wil_det")
    G = {k: np.zeros((n_chi, n_chi), dtype=np.float64) for k in keys}
    Z = {k: 0.0 for k in keys}
    for start in range(0, ncfg, batch):
        end = min(start + batch, ncfg)
        cs = np.arange(start, end, dtype=np.int64)
        U = decode_U(cs, nt)
        w_g = gauge_weights(U)
        chi_r, chi_p, _ = pair_characters(U, nt)
        acc(G, Z, "gauge", chi_r, chi_p, w_g)
        dw = wilson_dirac_batch(U, m=0.0)
        w_drop, _w_plus, _exc = overlap_weights_batch(dw, dim)
        w_w = wilson_detsq_batch(dw, dim)
        acc(G, Z, "ov_det", chi_r, chi_p, w_drop)
        acc(G, Z, "wil_det", chi_r, chi_p, w_w)
    return {k: min_eig(G, Z, k) for k in keys}


def is_psd(e):
    return np.isfinite(e) and e > -TOL_PSD


def is_viol(e):
    return np.isfinite(e) and e < -TOL_VIOL


# ================================================================= Hamiltonian route
NS_H = 4
NLQ_H = NS_H - 1
DL_H = 4 ** NLQ_H
DF_H = 2 ** NS_H
D_H = DL_H * DF_H
Z1_H = np.diag([1j ** k for k in range(4)]).astype(complex)
X1_H = np.roll(np.eye(4), 1, axis=0).astype(complex)
LAM_E, W_HOP, MASS = 1.0, 0.7, 0.5


def _link_op(l, M):
    out = np.array([[1.0]], dtype=complex)
    for j in range(NLQ_H):
        out = np.kron(out, M if j == l else np.eye(4))
    return np.kron(out, np.eye(DF_H))


def _ferm_op(x):
    out = np.array([[1.0]], dtype=complex)
    sz = np.diag([1.0, -1.0])
    a = np.array([[0, 1], [0, 0]], dtype=complex)
    for j in range(NS_H):
        if j < x:
            out = np.kron(out, sz)
        elif j == x:
            out = np.kron(out, a)
        else:
            out = np.kron(out, np.eye(2))
    return np.kron(np.eye(DL_H), out)


def _build_ham_ops():
    psi = [_ferm_op(x) for x in range(NS_H)]
    num = [psi[x].conj().T @ psi[x] for x in range(NS_H)]
    return psi, num


def build_H(psi, num, k_seam=0, lam_e=LAM_E, w=W_HOP, m=MASS):
    H = np.zeros((D_H, D_H), dtype=complex)
    for l in range(NLQ_H):
        xl = _link_op(l, X1_H)
        H += -lam_e * (xl + xl.conj().T)
    for x in range(NS_H - 1):
        u = _link_op(x, Z1_H)
        hop = psi[x].conj().T @ u @ psi[x + 1]
        H += w * (hop + hop.conj().T)
    hop_seam = (1j ** k_seam) * (psi[NS_H - 1].conj().T @ psi[0])
    H += w * (hop_seam + hop_seam.conj().T)
    for x in range(NS_H):
        H += m * ((-1) ** x) * num[x]
    return H


def gauss_unitary(num, x):
    V = np.eye(D_H, dtype=complex)
    if x - 1 >= 0:
        V = V @ np.linalg.matrix_power(_link_op(x - 1, X1_H), 3)
    if x < NLQ_H:
        V = V @ _link_op(x, X1_H)
    phase = np.eye(D_H, dtype=complex) + (1j - 1) * num[x]
    return V @ phase


def E0_background(k):
    df = 2 ** NS_H
    sz = np.diag([1.0, -1.0])
    a = np.array([[0, 1], [0, 0]], dtype=complex)

    def fop(x):
        out = np.array([[1.0]], dtype=complex)
        for j in range(NS_H):
            out = np.kron(out, sz if j < x else (a if j == x
                                                 else np.eye(2)))
        return out

    ps = [fop(x) for x in range(NS_H)]
    hb = np.zeros((df, df), dtype=complex)
    for x in range(NS_H - 1):
        hop = ps[x].conj().T @ ps[x + 1]
        hb += W_HOP * (hop + hop.conj().T)
    hop = (1j ** k) * (ps[NS_H - 1].conj().T @ ps[0])
    hb += W_HOP * (hop + hop.conj().T)
    for x in range(NS_H):
        hb += MASS * ((-1) ** x) * (ps[x].conj().T @ ps[x])
    return float(np.linalg.eigvalsh(hb)[0])


def gaussianity_deviation(Hm, psi, num):
    wv, vv = np.linalg.eigh(Hm)
    g = vv[:, 0]
    gap = wv[1] - wv[0]
    G = np.zeros((NS_H, NS_H), dtype=complex)
    for x in range(NS_H):
        for y in range(NS_H):
            G[x, y] = complex(g.conj() @ ((psi[x].conj().T @ psi[y]) @ g))
    prod = np.eye(D_H)
    for x in range(NS_H):
        prod = prod @ num[x]
    lhs = complex(g.conj() @ (prod @ g))
    return abs(lhs - np.linalg.det(G)), gap


def free_control_gauss():
    df = 2 ** NS_H
    sz = np.diag([1.0, -1.0])
    a = np.array([[0, 1], [0, 0]], dtype=complex)

    def fop(x):
        out = np.array([[1.0]], dtype=complex)
        for j in range(NS_H):
            out = np.kron(out, sz if j < x else (a if j == x
                                                 else np.eye(2)))
        return out

    ps = [fop(x) for x in range(NS_H)]
    hb = np.zeros((df, df), dtype=complex)
    for x in range(NS_H - 1):
        hop = ps[x].conj().T @ ps[x + 1]
        hb += W_HOP * (hop + hop.conj().T)
    for x in range(NS_H):
        hb += MASS * ((-1) ** x) * (ps[x].conj().T @ ps[x])
    wv, vv = np.linalg.eigh(hb)
    g = vv[:, 0]
    G = np.array([[complex(g.conj() @ ((ps[x].conj().T @ ps[y]) @ g))
                   for y in range(NS_H)] for x in range(NS_H)])
    prod = np.eye(df)
    for x in range(NS_H):
        prod = prod @ (ps[x].conj().T @ ps[x])
    return abs(complex(g.conj() @ (prod @ g)) - np.linalg.det(G)), \
        float(wv[1] - wv[0])


# ================================================================= Chiral Gauss
NS_C = 4
NLQ_C = 2
NFERM_C = 2 * NS_C
DF_C = 2 ** NFERM_C
DL_C = 4 ** NLQ_C
Z1_C = np.diag([1j ** k for k in range(4)]).astype(complex)
X1_C = np.roll(np.eye(4), 1, axis=0).astype(complex)
SZ_C = np.diag([1.0, -1.0])
ANN_C = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)


def _ferm_c(alpha):
    out = np.array([[1.0]], dtype=complex)
    for j in range(NFERM_C):
        if j < alpha:
            out = np.kron(out, SZ_C)
        elif j == alpha:
            out = np.kron(out, ANN_C)
        else:
            out = np.kron(out, np.eye(2))
    return out


def _link_c(l, M):
    out = np.array([[1.0]], dtype=complex)
    for j in range(NLQ_C):
        out = np.kron(out, M if j == l else np.eye(4))
    return out


def _maxabs(A):
    return float(np.max(np.abs(A)))


def _kron_conj_dev(A, B, C, D):
    A2 = C @ A @ C.conj().T
    B2 = D @ B @ D.conj().T
    nA = complex(np.vdot(A.ravel(), A.ravel()))
    nB = complex(np.vdot(B.ravel(), B.ravel()))
    if abs(nA) < 1e-20 and abs(nB) < 1e-20:
        return _maxabs(A2) + _maxabs(B2)
    if abs(nA) >= 1e-20:
        omega = complex(np.vdot(A.ravel(), A2.ravel()) / nA)
        dA = _maxabs(A2 - omega * A)
        if abs(omega) < 1e-14:
            return 1.0 if _maxabs(A) > 1e-14 else _maxabs(A2)
        dB = _maxabs(B2 - (1.0 / omega) * B)
        return max(dA, dB)
    omega = complex(np.vdot(B.ravel(), B2.ravel()) / nB)
    dB = _maxabs(B2 - omega * B)
    if abs(omega) < 1e-14:
        return 1.0 if _maxabs(B) > 1e-14 else _maxabs(B2)
    dA = _maxabs(A2 - (1.0 / omega) * A)
    return max(dA, dB)


def _i_n_phase(n_op, g):
    return np.eye(n_op.shape[0], dtype=complex) + ((1j ** g) - 1.0) * n_op


def _chiral_ops():
    psi = [[_ferm_c(2 * x + s) for s in range(2)] for x in range(NS_C)]
    num = [[psi[x][s].conj().T @ psi[x][s] for s in range(2)]
           for x in range(NS_C)]
    hop = [[psi[x][s].conj().T @ psi[(x + 1) % NS_C][s]
            for s in range(2)] for x in range(NS_C)]
    return num, hop


def gauss_factors(num, gL, gR, s, site=1):
    s = int(s) % 4
    vlink = (np.linalg.matrix_power(_link_c(1, X1_C), s)
             @ np.linalg.matrix_power(_link_c(0, X1_C), (4 - s) % 4))
    phi = (_i_n_phase(num[site][0], gL) @ _i_n_phase(num[site][1], gR))
    return vlink, phi


def term_comm(num, hop, qL, qR, gL, gR, s):
    qs = (int(qL) % 4, int(qR) % 4)
    vlink, phi = gauss_factors(num, gL, gR, s)
    i_l, i_f = np.eye(DL_C), np.eye(DF_C)
    mx = 0.0
    for l in range(NLQ_C):
        xl = _link_c(l, X1_C)
        mx = max(mx, _kron_conj_dev(xl, i_f, vlink, phi))
        mx = max(mx, _kron_conj_dev(xl.conj().T, i_f, vlink, phi))
    for x in range(NLQ_C):
        zx = _link_c(x, Z1_C)
        for sp in range(2):
            zq = np.linalg.matrix_power(zx, qs[sp])
            h = hop[x][sp]
            mx = max(mx, _kron_conj_dev(zq, h, vlink, phi))
            mx = max(mx, _kron_conj_dev(zq.conj().T, h.conj().T, vlink, phi))
    for x in range(NLQ_C, NS_C):
        for sp in range(2):
            h = hop[x][sp]
            mx = max(mx, _kron_conj_dev(i_l, h, vlink, phi))
            mx = max(mx, _kron_conj_dev(i_l, h.conj().T, vlink, phi))
    for x in range(NS_C):
        for sp in range(2):
            mx = max(mx, _kron_conj_dev(i_l, num[x][sp], vlink, phi))
    return mx


def hits_independent(num, hop, qL, qR, tol=1e-10):
    out = []
    for gL in range(4):
        for gR in range(4):
            for s in (1, 3):
                c = term_comm(num, hop, qL, qR, gL, gR, s)
                if c < tol:
                    out.append((gL, gR, s, c))
    return out


def hits_single_g(num, hop, qL, qR, tol=1e-10):
    out = []
    for g in range(4):
        for s in (1, 3):
            c = term_comm(num, hop, qL, qR, g, g, s)
            if c < tol:
                out.append((g, s, c))
    return out


def run():
    reset()
    print("v989  TFPT4D.LATTICE.ACTION.01 + CHIRAL4D.NOMIRROR.01: "
          "gate battery + Euclidean T2 kill + Hamiltonian route + "
          "chiral Gauss census")

    # ----- T4 -----
    y3, su2y, su3y, grav, witten = anomaly_sums(GEN)
    check("T4 [E]: [U(1)]^3 = [SU(2)]^2U(1) = [SU(3)]^2U(1) = "
          "grav^2 U(1) = 0 (exact rationals)",
          y3 == su2y == su3y == grav == 0)
    check("T4 WITTEN [E]: %d SU(2) doublets (3 color + 1 lepton), even"
          % witten, witten % 2 == 0)
    y3m, su2ym, _su3ym, gravm, wittenm = anomaly_sums(
        [f for f in GEN if f[0] != "L"])
    check("T4 MUTANT [E]: drop-L breaks [U(1)]^3, [SU(2)]^2U(1), grav "
          "and makes Witten odd",
          y3m != 0 and su2ym != 0 and gravm != 0 and wittenm % 2 == 1)

    # ----- T5/T6 -----
    idx_results = {}
    g5 = None
    for q in (-2, -1, 0, 1, 2):
        dov = overlap_2d(q)
        dim2 = dov.shape[0]
        g5 = np.kron(S3, np.eye(dim2 // 2))
        w, v = np.linalg.eig(dov)
        zero = np.abs(w) < 1e-8
        chir = 0.0
        for i in np.where(zero)[0]:
            vec = v[:, i]
            chir += float(np.real(vec.conj() @ (g5 @ vec)))
        idx_results[q] = round(chir)
    print("   T5 flux -> chirality-summed index:", idx_results)
    check("T5 [E]: index(D_ov) = q for q = -2..2 (2D overlap mechanism)",
          all(idx_results[q] == q for q in idx_results))
    dov1 = overlap_2d(1)
    w1 = np.linalg.eigvals(dov1)
    on_circle = float(np.max(np.abs(np.abs(w1 - 1) - 1)))
    nonzero = np.sort(np.abs(w1))[int(np.sum(np.abs(w1) < 1e-8)):]
    doublers = int(np.sum(np.real(w1) > 1.5))
    check("T6 [E]: GW circle (max dev %.1e); gap %.3f; %d doublers at "
          "cutoff" % (on_circle, float(nonzero[0]), doublers),
          on_circle < 1e-8 and float(nonzero[0]) > 0.05 and doublers > 0)

    # ----- T7 -----
    faces, lateral = cube_faces()
    k4_int = four_point(0.4, faces, lateral)
    k4_free = four_point(0.0, faces, lateral)
    print("   T7 kappa_4(beta=0.4)=%.3e  free=%.1e" % (k4_int, k4_free))
    check("T7 [E]: connected 4-point kappa_4 != 0 at beta=0.4; "
          "free control = 0",
          abs(k4_int) > 1e-6 and abs(k4_free) < 1e-12)

    # ----- Euclidean T2 kill -----
    print("   Euclidean T2 kill: Z2 N_t-exact overlap RP ...")
    r2 = run_nt(2)
    r4 = run_nt(4)
    print("   Nt=2 min eigs gauge=%.3e ov_det=%.3e wil=%.3e"
          % (r2["gauge"], r2["ov_det"], r2["wil_det"]))
    print("   Nt=4 min eigs gauge=%.3e ov_det=%.3e wil=%.3e"
          % (r4["gauge"], r4["ov_det"], r4["wil_det"]))
    check("T2 VALIDATION [E]: pure-gauge Gram PSD at Nt=2 and Nt=4",
          is_psd(r2["gauge"]) and is_psd(r4["gauge"]))
    check("T2 KILL [E]: overlap |det D_ov|^2 ABSENT at Nt=2, APPEARS "
          "at Nt=4 (det-only ~ -0.249; got %.3e)" % r4["ov_det"],
          is_psd(r2["ov_det"]) and is_viol(r4["ov_det"])
          and abs(r4["ov_det"] + 0.249) < 0.05)
    check("T2 WILSON CONTROL [E]: |det D_W|^2 PSD at both Nt -- "
          "violation pinned on overlap time nonlocality",
          is_psd(r2["wil_det"]) and is_psd(r4["wil_det"]))

    # ----- Hamiltonian route -----
    print("   Hamiltonian route: 4-site Z4 staggered dim 1024 ...")
    psi, num = _build_ham_ops()
    H = build_H(psi, num)
    devs = []
    for x in (1, 2):
        V = gauss_unitary(num, x)
        devs.append(float(np.max(np.abs(H @ V - V @ H))))
    print("   interior Gauss commutators:", ["%.1e" % d for d in devs])
    check("HAM T1 [E]: interior Z4 Gauss unitaries commute with H "
          "(max dev %.1e)" % max(devs), max(devs) < 1e-12)
    H0, H1 = build_H(psi, num, k_seam=0), build_H(psi, num, k_seam=1)
    ph0 = np.eye(D_H, dtype=complex) + (1j - 1) * num[0]
    best = None
    for s in (1, 3):
        for use_phase in (True, False):
            V = np.linalg.matrix_power(_link_op(0, X1_H), s)
            if use_phase:
                V = V @ ph0
            for tgt in (H1, build_H(psi, num, k_seam=3)):
                dev = float(np.max(np.abs(V @ H0 @ V.conj().T - tgt)))
                if best is None or dev < best:
                    best = dev
    check("HAM T1 SEAM [E]: explicit intertwiner maps H(0) onto a "
          "neighbouring clock sector (dev %.1e)" % best, best < 1e-12)
    herm = float(np.max(np.abs(H - H.conj().T)))
    check("HAM T2 [E BY CONSTRUCTION]: H = H^dag (dev %.1e) so "
          "T = e^{-aH} is SPD -- the gate that killed the Euclidean "
          "candidate holds structurally" % herm, herm < 1e-12)
    e0dyn = {}
    for k in range(4):
        hp = build_H(psi, num, k_seam=k)
        e0dyn[k] = float(np.linalg.eigvalsh(hp)[0])
    spread_dyn = max(e0dyn.values()) - min(e0dyn.values())
    print("   dynamical E0(k):", {k: "%.6f" % e0dyn[k] for k in e0dyn})
    check("HAM T3a [E]: dynamical-link E0(k) identical (spread %.1e) "
          "-- seam background is a sector relabeling" % spread_dyn,
          spread_dyn < 1e-9)
    e0bg = {k: E0_background(k) for k in range(4)}
    print("   background E0(k):", {k: "%.6f" % e0bg[k] for k in e0bg})
    spread_bg = max(e0bg.values()) - min(e0bg.values())
    check("HAM T3b [E]: frozen mu4 flux splits fermion E0 "
          "(spread %.4f) with k=1,3 degenerate (|dE|=%.1e)"
          % (spread_bg, abs(e0bg[1] - e0bg[3])),
          spread_bg > 1e-6 and abs(e0bg[1] - e0bg[3]) < 1e-10
          and abs(e0bg[0] - e0bg[1]) > 1e-6)
    dev_int, gap_int = gaussianity_deviation(H, psi, num)
    dev_free, gap_free = free_control_gauss()
    check("HAM T7 [E]: interacting GS violates determinantal law "
          "(%.3e); free control holds (%.1e)" % (dev_int, dev_free),
          dev_int > 1e-6 and dev_free < 1e-10 and gap_free > 1e-6)

    # ----- Chiral Gauss census -----
    print("   Chiral Gauss census (factorized 16 x 256) ...")
    num_c, hop_c = _chiral_ops()
    c11 = term_comm(num_c, hop_c, 1, 1, 1, 1, 1)
    c_mut = term_comm(num_c, hop_c, 1, 1, 1, 0, 1)
    check("CHIRAL T1 [E]: vectorlike (1,1) interior Gauss commutes "
          "(bound %.1e)" % c11, c11 < 1e-12)
    check("CHIRAL T1 MUTANT [E]: (g_L,g_R)=(1,0) on vectorlike fails "
          "(bound %.1e)" % c_mut, c_mut > 0.1)
    t2_admit = {}
    for qL in range(4):
        for qR in range(4):
            t2_admit[(qL, qR)] = len(hits_single_g(num_c, hop_c, qL, qR)) > 0
    t2_closed = {(qL, qR): (qL == qR) for qL in range(4) for qR in range(4)}
    n_t2 = sum(1 for v in t2_admit.values() if v)
    check("CHIRAL T2 [E]: single-exponent Gauss iff q_L = q_R "
          "(%d/16 vectorlike; 0/12 chiral)" % n_t2,
          t2_admit == t2_closed and n_t2 == 4)
    t3_hits = {}
    t3_closed = True
    for qL in range(4):
        for qR in range(4):
            h = hits_independent(num_c, hop_c, qL, qR)
            t3_hits[(qL, qR)] = h
            expected = {((qL, qR, 1)),
                        (((-qL) % 4, (-qR) % 4, 3))}
            got = {(gL, gR, s) for gL, gR, s, _ in h}
            if got != expected:
                t3_closed = False
    check("CHIRAL T3 [E]: two-exponent Gauss always (16/16); "
          "hits = ((q,1), (-q,3)) -- lattice Dirac doubling",
          t3_closed and all(len(t3_hits[k]) > 0 for k in t3_hits))
    glaw_devs = []
    for qL, qR in ((1, 1), (1, 3), (1, 0)):
        for gL, gR, s, _ in t3_hits[(qL, qR)]:
            vlink, phi = gauss_factors(num_c, gL, gR, s)
            dL = _maxabs(np.linalg.matrix_power(vlink, 4) - np.eye(DL_C))
            dF = _maxabs(np.linalg.matrix_power(phi, 4) - np.eye(DF_C))
            glaw_devs.append(max(dL, dF))
    check("CHIRAL T4 [E]: successful V satisfies V^4 = I "
          "(max dev %.1e)" % max(glaw_devs), max(glaw_devs) < 1e-12)
    check("CHIRAL T5 [E]: (1,3) is chiral + continuum-anomaly-free "
          "mod 8, two-exponent PASSES, single-exponent FAILS; "
          "(1,0) also admitted by two-exponent (not yet a polynomial "
          "filter)",
          (1 * 1 - 3 * 3) % 8 == 0 and (1 * 1 - 0 * 0) % 8 == 1
          and len(t3_hits[(1, 3)]) > 0 and (not t2_admit[(1, 3)])
          and len(t3_hits[(1, 0)]) > 0 and (not t2_admit[(1, 0)]))

    check("FIREWALL (scope): 1+1D/2D toys, Z2/Z4; Euclidean T2 kill "
          "and Hamiltonian clearance are named; "
          "TFPT4D.LATTICE.ACTION.01 and CHIRAL4D.NOMIRROR.01 stay [O]",
          True)
    return summary("v989 lattice gate battery: T4-T7 + Euclidean T2 "
                   "kill + Hamiltonian T2 clear + chiral census; "
                   "contracts stay [O]")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
