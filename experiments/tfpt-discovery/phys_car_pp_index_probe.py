#!/usr/bin/env python3
"""PHYS T2 main slice -- Pimsner-Popa / Watatani index 4 on the CAR ladder,
with the mu4 action DERIVED from the clock, the Ramond zero-mode test, and
the RAMIFIED (1+i) structure check (GNET.RAMIFIED.01 candidate).

QUESTION (both councils, 2026-08-03): measure the seam-glue index on the
lattice ladder N = 48/96/192/384 -- local CAR algebras, mu4-average
conditional expectation E_N, optimal Pimsner-Popa constant, explicit
quasi-basis / Watatani index, Ramond q-sector behaviour, and the
(1+i)-parity dictionary from phys_ramified_ns_r_probe (9/9 GO).

CONSTRUCTION (standalone, numpy only):
  *  chain: N-site free-fermion chain, shift S with NS boundary S^N = -1
     (v679 frame).  DERIVATION OF mu4 (circularity rule -- NOT inserted):
     clock L := S^{N/12} (the v679/arch-glue clock, order 12 spin-doubled:
     L^12 = S^N = -1); mu4 := the half-turn H = L^6 = S^{N/2}; its order 4
     is FORCED by the NS spin structure (H^2 = S^N = -1, H^4 = 1).  The
     deck Dk := L^4 = S^{N/3} commutes with H and is NOT used in E.
  *  state (declared): chiral Dirac sea of the seam-DtN |k| reading
     (GATE.METRIC.13): occupied = negative momentum.  C = f(S) commutes
     with H by construction => Takesaki holds; machine-checked anyway.
     The PP/index results are algebraic (state-independent); the state
     enters via Takesaki + sector weights.
  *  local slice: window W_k = {0..k-1} u {N/2..N/2+k-1} (the H-orbit of
     k sites); the H-restriction is the signed block swap, H_W^2 = -I.
     Fock rep of 2k modes (Jordan-Wigner), Gaussian density matrix from
     the compressed covariance, canonical implementer U = Gamma(H_W)
     (vacuum-fixing phase => charge of the vacuum is 0, no convention
     freedom).  E(x) = (1/4) sum_j U^j x U^{-j} = sum_q P_q x P_q.

HONEST SPEC CORRECTION (documented, machine-verified): for CHARGE-
HOMOGENEOUS x the element x*x is mu4-invariant, so E(x*x) = x*x and
lambda(x) = 1 identically -- the PP bound is invisible on homogeneous
bases.  The optimal constant is attained on maximally sector-MIXING
elements; the probe constructs the explicit rank-one minimizer
(v = equal-weight sum over one unit vector per charge sector) and proves
lambda(v v*) = 1/#sectors.  By the pinching theorem the optimum is exactly
1/#sectors at EVERY finite level, so the ladder content sits in
(i) #sectors = 4 (k >= 2; the k = 1 window sees only 3 sectors -- a real
boundary anomaly with teeth), (ii) the state: Takesaki + sector weights
w_q -> 1/4 with rates (the "no manual sector weighting" kill), and
(iii) the outerness witnesses |omega(U^j)| -> 0.

CHECKS:
  G0(N)  clock derivation: L^12 = -1, H = L^6, H^2 = -I, H^4 = I,
         Dk^3 = -1, [H, Dk] = 0.
  G1(N)  state: C pure, [C, H] = 0 exactly (Takesaki, one-particle).
  W(N,k) implementer correct (Ad U == H_W on modes); E group-average ==
         pinching; sector dims == (4^{k-1}+2^{k-1}, 4^{k-1},
         4^{k-1}-2^{k-1}, 4^{k-1}) (q = 0,1,2,3); lambda(homogeneous) == 1
         (identity); explicit minimizer lambda == 1/m to 1e-10; random
         battery min >= 1/m; [rho_W, U] == 0 (local Takesaki); weights
         w_q; |Tr rho U^j|.
  QB(k)  quasi-basis {1} u {|q,a><q',b| / sqrt(n_q')}: reconstruction
         x == sum v E(v* x) on a battery, and sum v v* == m * 1 EXACTLY
         (Watatani index m; = 4 for k >= 2).  Must-fail controls:
         uniform weights break scalarness (K4: the weights are FORCED,
         not chosen); Z2-only average gives lambda = 1/2, Ind = 2 (the
         probe distinguishes mu4 from mu2).
  R(N)   Ramond: momentum frame (zero mode is delocalized -- declared),
         H_R = S^{N/2} has order 2 (H_R^2 = +1): the mu4 action
         DEGENERATES undressed (m = 2, lambda = 1/2, Ind = 2 -- measured);
         the v679 Klein zero-mode dressing U' = Gamma(H_R) e^{i pi/2 n_0}
         restores order 4 (U'^2 = zero-mode parity), preserves the state
         EXACTLY ([rho, U'] = 0; the zero mode is maximally mixed,
         c_0 = 1/2), and restores m = 4, lambda = 1/4, Ind = 4.
  RAM    the (1+i) dictionary: E8 side re-verified compact ((1+i)L in
         the even sublattice; 15 x 16; purity 7 NS + 8 R); chain side:
         ALL NS momenta are half-integer => every window mode carries
         H-eigenvalue +-i (odd mu4 charge, chi = 1) and the sector-dim
         anomaly N_0 - N_2 = 2^k sits ONLY in ker(chi) = {0,2}; R momenta
         are integer => chi = 0, and the dressed zero mode is the unique
         chi = 1 carrier.  Same character mu4 -> mu4/mu2 = Z2 on both
         sides, half-integer labels <-> chi = 1 (momentum vs weight
         placement, spectral-flow dual); the ramified defect lives in
         ker(chi) on both sides ((1+i)L subset even part).

KILLS (preregistered, both councils):
  K1 optimal constant does not reach 1/4  -> measured;
  K2 Ramond destroys state preservation   -> measured ([rho, U']);
  K3 mu4 inner/trivial in the limit       -> witnesses w_q -> 1/4,
     |omega(U^j)| -> 0 (typed as witnesses, not proof);
  K4 index 4 only after manual sector weighting -> quasi-basis weights
     forced by the reconstruction identity; uniform-weight control must
     BREAK scalarness.

CONTRACT CANDIDATE (printed as text only; no ledger/paper/website edit):
GNET.RAMIFIED.01 -- see report.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py, no
ledger row, no paper claim, no marker move.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/phys_car_pp_index_probe.py
"""

import itertools
import sys

import numpy as np

TOL = 1e-9
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    return ok


# ===================================================================
# one-particle layer
# ===================================================================

def shift(N, ns=True):
    S = np.zeros((N, N))
    for j in range(N - 1):
        S[j + 1, j] = 1.0
    S[0, N - 1] = -1.0 if ns else 1.0
    return S


def momentum_frame(N, ns=True):
    sigma = 0.5 if ns else 0.0
    th = 2 * np.pi * (np.arange(N) + sigma) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi          # (-pi, pi]
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    return th, F


def covariance(N, ns=True):
    th, F = momentum_frame(N, ns)
    occ = (th < 0).astype(float)                        # chiral Dirac sea
    if not ns:
        occ[np.isclose(th, 0.0)] = 0.5                  # R zero mode mixed
    C = (F * occ) @ F.conj().T
    return C, th, occ


# ===================================================================
# Fock layer (Jordan-Wigner)
# ===================================================================

def jw_ops(n):
    sm = np.array([[0, 1], [0, 0]], dtype=complex)      # sigma^-  (c)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    ops = []
    for j in range(n):
        m = np.array([[1.0]], dtype=complex)
        for l in range(n):
            m = np.kron(m, sz if l < j else (sm if l == j else I2))
        ops.append(m)
    return ops                                          # annihilators c_j


def gaussian_rho(CW, cops):
    lam, V = np.linalg.eigh(CW)
    lam = np.clip(lam.real, 0.0, 1.0)
    dim = cops[0].shape[0]
    rho = np.eye(dim, dtype=complex)
    for i in range(len(cops)):
        d = sum(np.conj(V[j, i]) * cops[j] for j in range(len(cops)))
        n_i = d.conj().T @ d
        rho = rho @ ((1 - lam[i]) * np.eye(dim) + (2 * lam[i] - 1) * n_i)
    return rho


def gamma_unitary(HW, cops):
    """canonical implementer of the Bogoliubov unitary HW (vacuum fixed)."""
    M = 1j * HW                                          # Hermitian
    mu, V = np.linalg.eigh(M)
    dim = cops[0].shape[0]
    U = np.eye(dim, dtype=complex)
    for i in range(len(cops)):
        d = sum(np.conj(V[j, i]) * cops[j] for j in range(len(cops)))
        n_i = d.conj().T @ d
        ev = -1j * mu[i]                                 # HW eigenvalue
        U = U @ (np.eye(dim) + (ev - 1) * n_i)
    return U


def sector_projs(U):
    dim = U.shape[0]
    Ps = []
    for q in range(4):
        P = sum((1j ** (-q * j)) * np.linalg.matrix_power(U, j) for j in range(4)) / 4
        Ps.append(P)
    return Ps


def lam_of(B, Efun):
    """largest lambda with E(B) - lambda B >= 0, B PSD.
    Correct pencil form: lambda* = 1 / ||A^{+/2} B A^{+/2}|| with A = E(B);
    range(B) is contained in range(A) automatically because B <= 4 A
    (group average).  (First draft restricted to range(B) -- wrong.)"""
    A = Efun(B)
    a, W = np.linalg.eigh((A + A.conj().T) / 2)
    keep = a > 1e-11 * max(a.max(), 1.0)
    if not keep.any():
        return np.inf
    Ws = W[:, keep] / np.sqrt(a[keep])
    M = Ws.conj().T @ B @ Ws
    top = float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)
    return 1.0 / top if top > 0 else np.inf


def onb_of(P):
    w, W = np.linalg.eigh((P + P.conj().T) / 2)
    return W[:, w > 0.5]


def quasi_basis(Ps, uniform=False):
    onbs = [onb_of(P) for P in Ps]
    dims = [o.shape[1] for o in onbs]
    nbar = np.mean([d for d in dims if d > 0])
    vs = [np.eye(Ps[0].shape[0], dtype=complex)]
    for q in range(4):
        for qp in range(4):
            if q == qp or dims[q] == 0 or dims[qp] == 0:
                continue
            wgt = 1.0 / np.sqrt(nbar if uniform else dims[qp])
            for a in range(dims[q]):
                for b in range(dims[qp]):
                    vs.append(wgt * np.outer(onbs[q][:, a],
                                             onbs[qp][:, b].conj()))
    return vs, dims


# ===================================================================
# NS slice at (N, k)
# ===================================================================

def ns_slice(N, k, quasibasis=False, battery=6, rng=None):
    S = shift(N, ns=True)
    C, th, occ = covariance(N, ns=True)
    H = np.linalg.matrix_power(S, N // 2)
    win = list(range(k)) + list(range(N // 2, N // 2 + k))
    CW = C[np.ix_(win, win)]
    HW = H[np.ix_(win, win)]
    cops = jw_ops(2 * k)
    dim = 2 ** (2 * k)
    rho = gaussian_rho(CW, cops)
    U = gamma_unitary(HW, cops)
    Ps = sector_projs(U)
    dims = [int(round(np.trace(P).real)) for P in Ps]
    m = sum(1 for d in dims if d > 0)

    def E(x):
        return sum(P @ x @ P for P in Ps)

    out = {"dims": dims, "m": m}

    # implementer correctness
    dev = max(np.abs(U @ c @ U.conj().T
                     - sum(np.conj(HW[l, j]) * cops[l]
                           for l in range(2 * k))).max()
              for j, c in enumerate(cops))
    out["impl_dev"] = dev

    # E identities
    x = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
    Eavg = sum(np.linalg.matrix_power(U, j) @ x
               @ np.linalg.matrix_power(U, j).conj().T for j in range(4)) / 4
    out["pinch_dev"] = np.abs(Eavg - E(x)).max()

    # homogeneous identity lambda == 1: homogeneity lives in the
    # H_W-EIGENMODES d_i (site modes are mu4-inhomogeneous!)
    mu, V = np.linalg.eigh(1j * HW)
    dops = [sum(np.conj(V[j, i]) * cops[j] for j in range(2 * k))
            for i in range(2 * k)]
    homs = [dops[0].conj().T, dops[0].conj().T @ dops[0]]
    if 2 * k >= 2:
        homs.append(dops[0].conj().T @ dops[-1])
    lam_hom = [lam_of(xh.conj().T @ xh, E) for xh in homs]
    out["lam_hom_min"] = min(lam_hom)

    # explicit spread minimizer
    v = np.zeros(dim, dtype=complex)
    for P in Ps:
        o = onb_of(P)
        if o.shape[1]:
            v += o[:, 0]
    v /= np.linalg.norm(v)
    out["lam_star"] = lam_of(np.outer(v, v.conj()), E)

    # random battery lower bound
    lam_min = np.inf
    for _ in range(battery):
        x = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
        lam_min = min(lam_min, lam_of(x.conj().T @ x, E))
    out["lam_battery"] = lam_min

    # local Takesaki + weights + outerness witnesses
    out["takesaki_dev"] = np.abs(rho @ U - U @ rho).max()
    out["w"] = [float(np.trace(rho @ P).real) for P in Ps]
    out["absU"] = [abs(np.trace(rho @ np.linalg.matrix_power(U, j)))
                   for j in (1, 2, 3)]

    if quasibasis:
        vs, _ = quasi_basis(Ps)
        ind = sum(vv @ vv.conj().T for vv in vs)
        out["ind_dev"] = np.abs(ind - m * np.eye(dim)).max()
        rec_dev = 0.0
        for _ in range(4):
            x = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
            r = sum(vv @ E(vv.conj().T @ x) for vv in vs)
            rec_dev = max(rec_dev, np.abs(r - x).max())
        out["rec_dev"] = rec_dev
        vs_u, _ = quasi_basis(Ps, uniform=True)
        ind_u = sum(vv @ vv.conj().T for vv in vs_u)
        sc = np.trace(ind_u).real / dim
        out["uniform_dev"] = np.abs(ind_u - sc * np.eye(dim)).max()
        # Z2-only control
        def E2(xx):
            U2 = U @ U
            return (xx + U2 @ xx @ U2.conj().T) / 2
        out["lam_z2"] = lam_of(np.outer(v, v.conj()), E2)
    return out


def light_weights(N, k):
    """closed determinant formula for the mu4 sector weights of the
    Gaussian state on the window (one-particle only; valid because
    [C_W, H_W] = 0): Tr(rho U^j) = prod_i (1 - lam_i + lam_i h_i^j)
    in a simultaneous eigenbasis."""
    S = shift(N, True)
    C, _, _ = covariance(N, True)
    H = np.linalg.matrix_power(S, N // 2)
    win = list(range(k)) + list(range(N // 2, N // 2 + k))
    CW = C[np.ix_(win, win)]
    HW = H[np.ix_(win, win)]
    mu, V = np.linalg.eigh(1j * HW)
    Ct = V.conj().T @ CW @ V
    off = np.abs(Ct[np.ix_(mu > 0, mu < 0)]).max()
    lams, hs = [], []
    for sgn in (1, -1):
        idx = np.where(np.sign(mu) == sgn)[0]
        lam_blk = np.linalg.eigvalsh(Ct[np.ix_(idx, idx)]).real
        lams.extend(lam_blk)
        hs.extend([-1j * sgn * 1.0] * len(idx))
    tr = [np.prod([1 - l + l * h ** j for l, h in zip(lams, hs)])
          for j in range(4)]
    w = [float(np.real(sum((1j ** (-q * j)) * tr[j] for j in range(4)) / 4))
         for q in range(4)]
    return w, abs(tr[1]), off


# ===================================================================
# main
# ===================================================================

def main():
    rng = np.random.default_rng(20260803)
    print("phys_car_pp_index_probe -- PP/Watatani index on the CAR ladder\n")

    # ---------------- G0/G1 ladder ----------------
    for N in (48, 96, 192, 384):
        S = shift(N, True)
        L = np.linalg.matrix_power(S, N // 12)
        H = np.linalg.matrix_power(L, 6)
        Dk = np.linalg.matrix_power(L, 4)
        ok = (np.abs(np.linalg.matrix_power(L, 12) + np.eye(N)).max() < TOL
              and np.abs(H - np.linalg.matrix_power(S, N // 2)).max() < TOL
              and np.abs(H @ H + np.eye(N)).max() < TOL
              and np.abs(np.linalg.matrix_power(H, 4) - np.eye(N)).max() < TOL
              and np.abs(np.linalg.matrix_power(Dk, 3) + np.eye(N)).max() < TOL
              and np.abs(H @ Dk - Dk @ H).max() < TOL)
        C, th, occ = covariance(N, True)
        ok2 = (np.abs(C @ C - C).max() < 1e-8
               and np.abs(C @ H - H @ C).max() < 1e-8)
        check(f"G0/G1 N={N}: mu4 = L^6 derived (order 4 forced by NS), "
              f"deck commutes; C pure, [C,H] = 0", ok and ok2)

    # ---------------- k-ladder at N = 192 ----------------
    print("\n-- k-ladder at N = 192 (window = k sites + H-image) --")
    kl = {}
    for k in (1, 2, 3, 4, 5):
        r = ns_slice(192, k, quasibasis=(k <= 3), battery=6 if k <= 4 else 3,
                     rng=rng)
        kl[k] = r
        exp_dims = sorted([4 ** (k - 1) + 2 ** (k - 1), 4 ** (k - 1),
                           4 ** (k - 1) - 2 ** (k - 1), 4 ** (k - 1)])
        ok = sorted(r["dims"]) == exp_dims
        check(f"W k={k}: impl+pinch exact, sector dims {r['dims']} == "
              f"(4^(k-1)+-2^(k-1),4^(k-1),4^(k-1))",
              ok and r["impl_dev"] < 1e-8 and r["pinch_dev"] < 1e-8)
        check(f"W k={k}: lambda(homogeneous) == 1 (PP invisible on "
              f"charge-homogeneous x)", abs(r["lam_hom_min"] - 1) < 1e-8)
        target = 1.0 / r["m"]
        check(f"W k={k}: optimal PP constant == 1/{r['m']} "
              f"(explicit mixing minimizer)",
              abs(r["lam_star"] - target) < 1e-8,
              f"lambda* = {r['lam_star']:.12f}, battery min = "
              f"{r['lam_battery']:.6f} >= {target:.6f}")
        check(f"W k={k}: battery never undercuts 1/{r['m']}",
              r["lam_battery"] > target - 1e-8)
        check(f"W k={k}: local Takesaki [rho,U] = 0",
              r["takesaki_dev"] < 1e-8, f"dev = {r['takesaki_dev']:.2e}")
        if k <= 3:
            check(f"QB k={k}: quasi-basis reconstruction + Watatani index "
                  f"== {r['m']} * 1 scalar",
                  r["rec_dev"] < 1e-7 and r["ind_dev"] < 1e-7,
                  f"rec dev = {r['rec_dev']:.2e}, ind dev = {r['ind_dev']:.2e}")
            check(f"QB k={k}: K4 control fires (uniform weights break "
                  f"scalarness)" if k >= 2 else
                  f"QB k={k}: K4 control (k=1 window, 3 sectors)",
                  (r["uniform_dev"] > 1e-3) if k >= 2 else True,
                  f"uniform dev = {r['uniform_dev']:.3f}")
            check(f"QB k={k}: Z2-only control gives 1/2 (probe separates "
                  f"mu4 from mu2)", abs(r["lam_z2"] - 0.5) < 1e-8,
                  f"lambda_Z2 = {r['lam_z2']:.10f}")
    check("W k=1 boundary anomaly typed: only 3 sectors (charge 2 empty), "
          "lambda = 1/3, Ind = 3 -- the smallest window cannot see |mu4| = 4",
          kl[1]["m"] == 3 and abs(kl[1]["lam_star"] - 1 / 3) < 1e-8)

    # cross-validate the closed determinant formula against Fock
    ok = True
    for k in (2, 3, 4):
        wl, aU, off = light_weights(192, k)
        ok &= (max(abs(a - b) for a, b in zip(wl, kl[k]["w"])) < 1e-9
               and abs(aU - kl[k]["absU"][0]) < 1e-9 and off < 1e-10)
    check("weights: closed determinant formula == Fock computation "
          "(cross-validated k = 2..4)", ok)

    print("\n-- K3 witness: state weights balance as the WINDOW grows "
          "(N = 192, determinant formula to k = 20) --")
    print(f"{'k':>3} {'max|w_q-1/4|':>14} {'|<U>|':>10}")
    ks = list(range(1, 21))
    devk, absk = {}, {}
    for k in ks:
        wl, aU, _ = light_weights(192, k)
        devk[k] = max(abs(w - 0.25) for w in wl)
        absk[k] = aU
        print(f"{k:>3} {devk[k]:>14.6e} {aU:>10.4e}")
    even = [k for k in ks if k % 2 == 0]
    odd = [k for k in ks if k % 2 == 1]
    mono = (all(devk[even[i + 1]] < devk[even[i]] for i in range(len(even) - 1))
            and all(devk[odd[i + 1]] < devk[odd[i]] for i in range(len(odd) - 1))
            and all(absk[even[i + 1]] < absk[even[i]] for i in range(len(even) - 1))
            and all(absk[odd[i + 1]] < absk[odd[i]] for i in range(len(odd) - 1)))
    alpha = (np.log(devk[10] / devk[20]) / np.log(2.0))
    check("K3 witness: max|w_q - 1/4| and |<U>| strictly decreasing along "
          "BOTH window-parity subladders k = 1..20 (quasi-local sector "
          "balance; even/odd oscillation typed as half-filling artifact; "
          "no manual weighting anywhere)", mono,
          f"power-law rate alpha = {alpha:.3f} (dev ~ k^-alpha), "
          f"dev(k=20) = {devk[20]:.4f}")

    # ---------------- N-ladder at k = 3 ----------------
    print("\n-- N-ladder at k = 3: state weights + outerness witnesses --")
    print(f"{'N':>4} {'lambda*':>12} {'max|w_q-1/4|':>14} "
          f"{'|<U>|':>10} {'|<U^2>|':>10} {'|<U^3>|':>10}")
    nl = {}
    for N in (48, 96, 192, 384):
        r = ns_slice(N, 3, rng=rng, battery=3)
        nl[N] = r
        dw = max(abs(w - 0.25) for w in r["w"])
        print(f"{N:>4} {r['lam_star']:>12.10f} {dw:>14.6e} "
              f"{r['absU'][0]:>10.3e} {r['absU'][1]:>10.3e} {r['absU'][2]:>10.3e}")
    ok = all(abs(nl[N]["lam_star"] - 0.25) < 1e-8 for N in nl)
    check("K1 NOT triggered: lambda* == 1/4 exactly on the whole ladder "
          "(pinching theorem, finite-level exact)", ok)
    dws = [max(abs(w - 0.25) for w in nl[N]["w"]) for N in (48, 96, 192, 384)]
    steps = [abs(dws[i + 1] - dws[i]) for i in range(3)]
    check("N-ladder honesty: at FIXED window k the weights converge in N "
          "to a nonzero continuum value (finite window keeps finite "
          "mu4 coherence -- the balance axis is the window ladder, K3 "
          "above)", all(steps[i + 1] < steps[i] for i in range(2)),
          f"|w-dev| = {['%.6f' % d for d in dws]} (Cauchy in N)")

    # ---------------- Ramond ----------------
    print("\n-- Ramond sector (momentum frame; zero mode delocalized) --")
    for N in (48, 192):
        th, F = momentum_frame(N, ns=False)
        # window modes: m = 0 (zero), +-1 (H-charge 2), +2 (H-charge 0)
        mm = [0, 1, N - 1, 2]
        heig = np.array([np.exp(-1j * th[m] * N / 2) for m in mm])
        heig = np.round(heig.real).astype(float)
        occm = np.array([0.5, 0.0, 1.0, 0.0])
        cops = jw_ops(4)
        dim = 16
        rho = np.eye(dim, dtype=complex)
        for i in range(4):
            n_i = cops[i].conj().T @ cops[i]
            rho = rho @ ((1 - occm[i]) * np.eye(dim) + (2 * occm[i] - 1) * n_i)
        U = np.eye(dim, dtype=complex)
        for i in range(4):
            n_i = cops[i].conj().T @ cops[i]
            U = U @ (np.eye(dim) + (heig[i] - 1) * n_i)
        ok = (np.abs(U @ U - np.eye(dim)).max() < TOL
              and list(heig) == [1.0, -1.0, -1.0, 1.0])
        check(f"R N={N}: H_R^2 = +1 -- the mu4 action DEGENERATES to order 2 "
              f"undressed (NS spin doubling is load-bearing)", ok)
        Ps_u = sector_projs(U)
        dims_u = [int(round(np.trace(P).real)) for P in Ps_u]
        m_u = sum(1 for d in dims_u if d > 0)

        def Eu(x, Ps=Ps_u):
            return sum(P @ x @ P for P in Ps)

        v = np.zeros(dim, dtype=complex)
        for P in Ps_u:
            o = onb_of(P)
            if o.shape[1]:
                v += o[:, 0]
        v /= np.linalg.norm(v)
        lam_u = lam_of(np.outer(v, v.conj()), Eu)
        vs_u, _ = quasi_basis(Ps_u)
        ind_u = sum(vv @ vv.conj().T for vv in vs_u)
        ok = (m_u == 2 and abs(lam_u - 0.5) < 1e-8
              and np.abs(ind_u - 2 * np.eye(dim)).max() < 1e-7)
        check(f"R N={N}: undressed census m = 2, lambda = 1/2, Ind = 2 "
              f"(measured degeneration)", ok, f"dims = {dims_u}")

        n0 = cops[0].conj().T @ cops[0]
        Ud = U @ (np.eye(dim) + (1j - 1) * n0)          # v679 Klein dressing
        ok = (np.abs(np.linalg.matrix_power(Ud, 4) - np.eye(dim)).max() < TOL
              and np.abs(Ud @ Ud - (np.eye(dim) - 2 * n0)).max() < TOL)
        check(f"R N={N}: dressed U' = Gamma(H_R) e^(i pi/2 n_0): order 4, "
              f"U'^2 = zero-mode parity", ok)
        tak = np.abs(rho @ Ud - Ud @ rho).max()
        check(f"R N={N}: K2 NOT triggered -- state preservation exact "
              f"(zero mode maximally mixed, c_0 = 1/2)", tak < 1e-9,
              f"[rho,U'] dev = {tak:.2e}")
        Ps_d = sector_projs(Ud)
        dims_d = [int(round(np.trace(P).real)) for P in Ps_d]

        def Ed(x, Ps=Ps_d):
            return sum(P @ x @ P for P in Ps)

        v = np.zeros(dim, dtype=complex)
        for P in Ps_d:
            o = onb_of(P)
            if o.shape[1]:
                v += o[:, 0]
        v /= np.linalg.norm(v)
        lam_d = lam_of(np.outer(v, v.conj()), Ed)
        vs_d, _ = quasi_basis(Ps_d)
        ind_d = sum(vv @ vv.conj().T for vv in vs_d)
        ok = (all(d > 0 for d in dims_d) and abs(lam_d - 0.25) < 1e-8
              and np.abs(ind_d - 4 * np.eye(dim)).max() < 1e-7)
        check(f"R N={N}: dressed census m = 4, lambda = 1/4, Ind = 4 "
              f"restored", ok, f"dims = {dims_d}, lambda = {lam_d:.10f}")

    # ---------------- RAMIFIED dictionary ----------------
    print("\n-- RAMIFIED (1+i) dictionary (GNET.RAMIFIED.01 candidate) --")

    # chain side: NS momenta half-integer <=> all H-eigenvalues +-i (chi=1)
    ok = True
    for N in (48, 96, 192, 384):
        th, _ = momentum_frame(N, True)
        hev = np.exp(-1j * th * N / 2)
        ok &= bool(np.allclose(np.abs(hev.real), 0.0, atol=1e-9))
    check("RAM chain(NS): all momenta half-integer => every mode has "
          "H-eigenvalue +-i (chi = 1 on the whole NS one-particle space)", ok)
    th, _ = momentum_frame(48, False)
    hev = np.exp(-1j * th * 48 / 2)
    check("RAM chain(R): all momenta integer => H-eigenvalues +-1 "
          "(chi = 0); the dressed zero mode is the unique chi = 1 carrier",
          bool(np.allclose(np.abs(hev.imag), 0.0, atol=1e-9)))
    ok = True
    for k in (2, 3, 4, 5):
        d = kl[k]["dims"]
        ok &= (d[1] == d[3] == 4 ** (k - 1)) and (d[0] - d[2] == 2 ** k)
    check("RAM chain: sector-dim anomaly N_0 - N_2 = 2^k sits ONLY in "
          "ker(chi) = {0,2}; N_1 = N_3 exact", ok)

    # E8 side compact re-verification (phys_ramified_ns_r_probe logic)
    def in_E8(w):
        par = {wi % 2 for wi in w}
        return len(par) == 1 and sum(w) % 4 == 0

    def Jap(w):
        out = []
        for kk in range(4):
            a, b = w[2 * kk], w[2 * kk + 1]
            out.extend([-b, a])
        return tuple(out)

    def equiv(w, v):
        d = tuple(a - b for a, b in zip(w, v))
        u = tuple(a - b for a, b in zip(d, Jap(d)))
        return all(c % 2 == 0 for c in u) and in_E8(tuple(c // 2 for c in u))

    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (2, -2):
            for sj in (2, -2):
                w = [0] * 8
                w[i], w[j] = si, sj
                roots.append(tuple(w))
    for s in itertools.product((1, -1), repeat=8):
        if s.count(-1) % 2 == 0:
            roots.append(s)
    reps, classes = [], []
    for v in roots:
        for kk, r in enumerate(reps):
            if equiv(v, r):
                classes[kk].append(v)
                break
        else:
            reps.append(v)
            classes.append([v])
    pure = all(len({v[0] % 2 for v in c}) == 1 for c in classes)
    n_ns = sum(1 for c in classes if c[0][0] % 2 == 0)
    B = []
    for i in range(6):
        w = [0] * 8
        w[i], w[i + 1] = 2, -2
        B.append(tuple(w))
    w = [0] * 8
    w[6], w[7] = 2, 2
    B.append(tuple(w))
    B.append(tuple([1] * 8))
    even_img = all(all(c % 2 == 0 for c in tuple(a + b for a, b in
                                                 zip(bb, Jap(bb)))) for bb in B)
    check("RAM E8: (1+i)L in even sublattice; 15 x 16; purity 7 NS + 8 R "
          "(phys_ramified_ns_r re-verified compact)",
          even_img and len(classes) == 15 and pure and n_ns == 7)

    n_pass = sum(1 for _, ok in CHECKS if ok)
    all_ok = n_pass == len(CHECKS)
    verdict = "T2-SLICE-GO (PP-INDEX-4-ON-LADDER)" if all_ok else "MIXED"
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}")
    print("""
GNET.RAMIFIED.01 (contract CANDIDATE, text only -- no ledger/paper edit):
  the seam-Calderon inclusion A = B^{mu4} subset B (index 4, the
  GATE.METRIC.08 Q-system) is the ramified-place structure of the Z[i]-E8
  commensurability groupoid: (i) the mu4-average expectation is the
  (1+i)-pinching, Watatani index 4 = N((1+i))^2 = |mu4|, measured on the
  CAR ladder with the clock-derived action; (ii) the NS/R grading is the
  parity character chi: mu4 -> mu4/mu2 = Z2 of E8(Z[i])/(1+i) = F2^4
  (half-integer labels <-> chi = 1 on both sides, momentum vs weight
  placement); (iii) the ramified defect lives in ker(chi) on both sides
  ((1+i)L subset even part; chain anomaly N_0 - N_2 = 2^k in {0,2});
  (iv) the R sector needs the v679 Klein zero-mode dressing, which is
  state-preserving.  KILLS: Frobenius mismatch Q-system vs (1+i)-
  correspondence convolution; index != 4 on the state-preserving ladder;
  dressing incompatible with the groupoid sigma-descent.""")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
