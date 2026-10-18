#!/usr/bin/env python3
"""G_net continuum strand -- GNET.MARTINGALE.LIMIT.01 (finite part):
the Haar ladder as a filtration with index-4 expectations, and the
noncommutative-martingale route to the GNS limit net, its finite
hypotheses MEASURED.

PROGRAMME.  Replace continuum heuristics by martingale convergence:
if the local-state defect sequence along the certified inductive
system is SUMMABLE in the state norm, the limit state exists uniquely
by elementary Banach telescoping; the operator-algebra content
(GNS, local normality, split, simple-current extension) is then a
typed list of analytic steps with finite-level evidence in hand.

INPUTS (certified upstream, read-only):
  * gnet_gns_limit_probe.py (GNS-PRECURSORS-COHERENT): exact Haar
    isometry tower, exact commuting index-4 expectation squares,
    geometric state convergence, duality census dim B'/dim A' = 4.
  * gnet_arf_qsystem_probe.py: the exact dim law
    d_c(l) = 4^{l-1} + 2^{l-1} cos(pi c/2), obstruction gap 2^{-l};
    uniform sector-resolved split bounds; 185-element quasi-basis at
    l = 2 with sum v v* = 4*1 exact.
  * GATE.QGEO majorant-lemma state (contracts 2026-08-04/05 notes):
    residue (a) grid-sup closed (v778); residues (b) "L2 uniform
    FH/RH [hard-technical]" and (c) "L3 uniformity [medium]" open.

THE FILTRATION (step 1, formalized).  A_k := iota^k(A(W)) for the
fixed base window W = win(48, 0, l) (doubled), iota = the Haar CAR
embedding (V_N: e_j -> (e_2j + e_2j+1)/sqrt2, an exact isometry whose
one-particle image of win(N,0,l) is EXACTLY win(2N,0,2l): support
coherence gate).  On the common 2^{2l}-dim representation the tower
states are the pullbacks omega_k = rho_k of the level-k chiral sea;
the index-4 Watatani expectations E (mu4 average, quasi-basis
explicit) are LITERALLY level-independent (window data identical at
every N: slim recheck).  DEPTH PREDECLARED: quasi-basis explicit at
l = 2 (185 elements) and l = 3 (3041 elements); tower depth k <= 6
(N = 48*2^k up to 3072); defect windows l = 1, 2, 3.
HONEST TYPING OF "MARTINGALE": the omega_k are an ALMOST-martingale
(approximate martingale with measured defects), not an exact one;
the exact E-compatibility at every level is the mu4 invariance
omega_k o E = omega_k (gated at 1e-8).  The convergence mechanism
used is norm convergence under summable defects -- elementary
completeness of the dual Banach space (telescoping); "martingale"
names the filtration + expectation structure (Umegaki conditional
expectations; cf. Cuculescu 1971 for the genuinely noncommutative
a.e. statements, cited as context, NOT used as a lemma here).

PREDECLARED NORM: the state norm on the finite-dimensional algebra =
trace norm of the density-matrix difference,
||omega - omega'|| := ||rho - rho'||_1 (dual of the operator norm;
= 2 x total variation).  All defect gates use this norm.

PREREGISTERED GATES (frozen before the first run):
S1 FILTRATION EXACT:
   S1.1 V*V = 1 exact and support coherence ||(1-P_{W'}) V P_W|| = 0
        (W' = the doubled window) at N = 48 and 96.
   S1.2 quasi-basis: 185 elements at l = 2 and 3041 at l = 3, each
        with sum v v* = 4*1 within 1e-6 (predeclared depth).
   S1.3 martingale compatibility: max_k ||[C_k(W), H_W]|| < 1e-10 and
        max_{k, battery} |tr(rho_k (E(a) - a))| < 1e-8 (omega_k o E =
        omega_k at every level).
   S1.4 window data (H_W) identical at N = 48 and N = 3072 (exact):
        one E for the whole tower (the commuting-square system).
S2 SUMMABLE DEFECT (load-bearing): delta_k := ||rho_{k+1} - rho_k||_1,
   k = 0..5, for l = 1, 2, 3.
   S2.1 geometric tail: r_k = delta_k/delta_{k-1} <= 0.55 for every
        k >= 1 with delta_{k-1} > 1e-12 (rate <= 1/2 + 10% slack --
        the dim-law rate 2^{-l} is the conjectured structural source;
        the fitted rate is REPORTED against 0.5, not forced).
   S2.2 envelope: delta_k <= C * 2^{-k} for all k >= 1 with the
        frozen anchor C := 4 * 2 * delta_1 (i.e. 2 x the k = 1
        envelope value; no tail fitting) -- summability quantified.
S3 TELESCOPING / UNIQUE LIMIT (l = 2 window):
   S3.1 tail bound on every rung: ||rho_proxy - rho_k||_1 <=
        min(2.25 * delta_k, 2 * C * 2^{-k}) + 1e-12 for k = 1..5,
        rho_proxy = Richardson extrapolant from the last two states
        (the exact comparison C*2^{-l}/(1 - 1/2) demanded by the
        programme, with the measured C).
   S3.2 frozen battery of 6 local observables: the gaps
        |tr((rho_k - rho_proxy) a)| fall with tail ratio <= 0.6
        (floor 1e-12).
   S3.3 uniqueness of the extrapolation: plain-last vs Richardson
        proxies differ by <= 2.25 * delta_5.
S4 SPLIT/NORMALITY PRECURSORS, uniform in the tower (k = 0..6):
   S4.1 sector-resolved cross-window profiles nu_cc'(k) (frozen
        battery of mu4-charge monomials, two disjoint l = 2 windows,
        sep = 6 base sites) stay <= max(2 max(nu(0), nu(1)), 1e-3)
        (the corrected two-level anchor of the arf-qsystem run) with
        shrinking tails.
   S4.2 determinant witness: D_k = det(1 - X_k X_k*) for the 4x4
        cross-covariance block X_k: D_k >= 0.5 for all k and
        |D_6 - D_5| <= |D_5 - D_4| + 1e-12 (the uniform determinant
        estimate a normality/split argument consumes).
STEPS 5-7 (typed, NOT executed; printed as the contract's analytic
remainder): GNS reconstruction of omega_inf; local normality
(nuclearity-type input = S4 witnesses); split property (standard
inclusion); mu4 simple-current extension (GATE.METRIC.11) on the
limit net.  Finite evidence for each is named; nothing is claimed.

CONTROLS (all must fire):
  C1 BOND SCRAMBLE: shifted-bond isometry e_j -> (e_{2j+1} +
     e_{2j+2})/sqrt2 (an isometry, but scale-incoherent): support
     leakage ||(1-P_{W'}) V_s P_W|| > 0.3 -- the filtration property
     A_k c A_{k+1} breaks.
  C2 Z2-ONLY average: lambda = 1/2 != 1/4 -- the expectations are
     not the index-4 system (martingale structure gone).
  C3 SCRAMBLED SEA (alternating 0.3/0.7 filling): defects O(1):
     min(delta_4, delta_5) > 0.05 -- summability breaks.
  C4 DECIMATION embedding: converges to the DEGENERATE limit:
     ||rho_dec(6) - 1/16||_1 < 1e-3 while ||rho_haar(6) - 1/16||_1 >
     0.1 -- a summable-defect filtration with the WRONG bond data
     forgets the sea (the coherent Haar bond is load-bearing).

RELATION TO GATE.QGEO (typed architectural note, no gate): the
majorant-lemma residues (b) L2 uniform FH/RH and (c) L3 uniformity
demand UNIFORM POINTWISE (sup-norm, uniform-in-refinement) control
of kernel majorants.  The martingale route needs NONE of that for
the existence/uniqueness of the limit state: summable STATE-NORM
defects (this probe's S2) close the limit by completeness of the
dual; uniformity enters only later, in the typed normality/split
step, where the S4 determinant witnesses are the finite input.  The
route thus bypasses (b)/(c) for the LIMIT-EXISTENCE step and
localizes them in the normality step -- an architectural
reallocation, not a proof of (b)/(c).

VERDICT ENUM (frozen):
  MARTINGALE-HYPOTHESES-MET : S1-S4 all pass and all controls fire
      (the continuum paper's section 4 upgrades from "tightness
      cited" to "unique limit via summable defects, hypotheses
      measured").
  MARTINGALE-DEAD : the defects are not summable (S2 tail ratios
      >= 0.9 or defects non-decreasing on the tail) -- the route
      dies, typed plainly.
  MARTINGALE-PARTIAL : anything else (steps named); any control
      failure flagged CONTROL-VOID.

HONESTY: every measurement is finite-level evidence FOR the cited
continuum steps, never the continuum theorem.  No marker moves.
Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no file writes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gnet_martingale_probe.py
"""

import hashlib
import inspect
import sys
import time

import numpy as np

TOL = 1e-10
SEED = 20260806
N0 = 48
KMAX = 6
RATE_BAR = 0.55
TAIL_FACTOR = 2.25          # >= 1/(1 - RATE_BAR)
DET_BAR = 0.5
CTRL_DEFECT_BAR = 0.05
LEAK_BAR = 0.3
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name
          + ("  -- " + detail if detail else ""))
    return ok


# ---------------- constructions (identical to the sibling probes) ----

def spower(N, k):
    P = np.zeros((N, N))
    for j in range(N):
        P[(j + k) % N, j] = (-1.0) ** ((j + k) // N)
    return P


def covariance_occ(N, occ):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    return (F * occ) @ F.conj().T


def covariance(N):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    return covariance_occ(N, (th < 0).astype(float))


def window(N, p, l):
    return [(p + i) % N for i in range(l)] + \
           [(p + N // 2 + i) % N for i in range(l)]


def haar_iso(N):
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = V[2 * j + 1, j] = 1.0 / np.sqrt(2.0)
    return V


def shift_iso(N):
    """C1 control: shifted-bond isometry (scale-incoherent)."""
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[(2 * j + 1) % (2 * N), j] = 1.0 / np.sqrt(2.0)
        V[(2 * j + 2) % (2 * N), j] = 1.0 / np.sqrt(2.0)
    return V


def decim_iso(N):
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = 1.0
    return V


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
    return 1.0 / float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)


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


def tracenorm(A):
    return float(np.abs(np.linalg.eigvalsh((A + A.conj().T) / 2)).sum())


def sha_freeze():
    fns = [spower, covariance_occ, covariance, window, haar_iso,
           shift_iso, decim_iso, jw_ops, gamma_partial, gaussian_rho,
           sector_projs, lam_of, onb_of, quasi_basis, tracenorm]
    blob = "".join(inspect.getsource(f) for f in fns)
    blob += repr((TOL, SEED, N0, KMAX, RATE_BAR, TAIL_FACTOR, DET_BAR,
                  CTRL_DEFECT_BAR, LEAK_BAR))
    return hashlib.sha256(blob.encode()).hexdigest()


# =====================================================================

def main():
    t0 = time.time()
    print("gnet_martingale_probe -- GNET.MARTINGALE.LIMIT.01 finite "
          "hypotheses\n")
    print(f"SHA-freeze (construction source + constants): "
          f"{sha_freeze()[:32]}\n")

    covs = {}

    def cov_of(N):
        if N not in covs:
            covs[N] = covariance(N)
        return covs[N]

    def pullback(iso_fun, cov_fun, kmax):
        out = []
        chain = np.eye(N0)
        Nk = N0
        for k in range(kmax + 1):
            out.append(chain.T.conj() @ cov_fun(Nk, k) @ chain)
            chain = iso_fun(Nk) @ chain
            Nk *= 2
        return out

    Cts = pullback(haar_iso, lambda Nk, k: cov_of(Nk), KMAX)

    wins = {l: window(N0, 0, l) for l in (1, 2, 3)}
    cops = {l: jw_ops(2 * l) for l in (1, 2, 3)}
    rhos = {l: [gaussian_rho(Ct[np.ix_(wins[l], wins[l])], cops[l])
                for Ct in Cts] for l in (1, 2, 3)}

    # ============ S1: the filtration, exact ===========================
    print("-- S1: the filtration (Haar embeddings + index-4 E) --")
    ok_iso, ok_supp = True, True
    for N in (48, 96):
        V = haar_iso(N)
        ok_iso &= np.abs(V.T @ V - np.eye(N)).max() < 1e-14
        w_small = window(N, 0, 2)
        w_big = window(2 * N, 0, 4)
        P = np.zeros(2 * N)
        P[w_big] = 1.0
        leak = np.abs(V[:, w_small] * (1 - P)[:, None]).max()
        ok_supp &= leak < 1e-14
    check("S1.1 Haar isometry exact (V*V = 1) and support coherence "
          "iota(win(N,0,2)) inside win(2N,0,4) EXACT (leak 0)",
          ok_iso and ok_supp)
    HN = spower(N0, N0 // 2)
    HW = {l: HN[np.ix_(wins[l], wins[l])] for l in (1, 2, 3)}
    U4 = {l: gamma_partial(HW[l], list(range(2 * l)), cops[l])
          for l in (1, 2, 3)}
    Ps = {l: sector_projs(U4[l]) for l in (1, 2, 3)}
    ok_qb = True
    for l, n_exp in ((2, 185), (3, 3041)):
        vs = quasi_basis(Ps[l])
        ind = sum(v @ v.conj().T for v in vs)
        ok_qb &= len(vs) == n_exp
        ok_qb &= float(np.abs(ind - 4 * np.eye(4 ** l)).max()) < 1e-6
    check("S1.2 Watatani quasi-basis explicit at predeclared depth: "
          "185 elements (l = 2) and 3041 (l = 3), sum v v* = 4*1",
          ok_qb)
    rng = np.random.default_rng(SEED)
    A_r = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16))
    A_r = (A_r + A_r.conj().T) / 2
    c2 = cops[2]
    batt = [c2[0].conj().T @ c2[0],
            c2[0].conj().T @ c2[1] + c2[1].conj().T @ c2[0],
            c2[0].conj().T @ c2[2].conj().T + c2[2] @ c2[0],
            Ps[2][0], Ps[2][2], A_r]

    def E2(x):
        return sum(P @ x @ P for P in Ps[2])

    dev_c = max(float(np.abs(Ct[np.ix_(wins[2], wins[2])] @ HW[2]
                             - HW[2] @ Ct[np.ix_(wins[2], wins[2])]).max())
                for Ct in Cts)
    dev_e = max(abs(np.trace(r @ (E2(a) - a)))
                for r in rhos[2] for a in batt)
    check("S1.3 martingale compatibility at every level: "
          "[C_k(W), H_W] = 0 and omega_k(E(a)) = omega_k(a)",
          dev_c < 1e-10 and dev_e < 1e-8,
          f"devs = {dev_c:.1e}, {dev_e:.1e}")
    H_big = spower(N0 * 2 ** KMAX, N0 * 2 ** KMAX // 2)
    w_big = window(N0 * 2 ** KMAX, 0, 2)
    check("S1.4 window data literally level-independent: H_W identical "
          f"at N = 48 and N = {N0 * 2 ** KMAX} (one E for the tower)",
          np.abs(H_big[np.ix_(w_big, w_big)] - HW[2]).max() < 1e-14)

    # ============ S2: the summable defect =============================
    print("\n-- S2: state defects  delta_k = ||rho_(k+1) - rho_k||_1 --")
    deltas = {l: [tracenorm(rhos[l][k + 1] - rhos[l][k])
                  for k in range(KMAX)] for l in (1, 2, 3)}
    print(f"{'k':>3} {'N->N*2':>12} {'l=1':>12} {'l=2':>12} {'l=3':>12}"
          f" {'r(l=2)':>8}")
    for k in range(KMAX):
        r = (deltas[2][k] / deltas[2][k - 1]) if k >= 1 else float("nan")
        print(f"{k:>3} {N0 * 2 ** k:>5}->{N0 * 2 ** (k + 1):<6}"
              f" {deltas[1][k]:>12.3e} {deltas[2][k]:>12.3e}"
              f" {deltas[3][k]:>12.3e} {r:>8.3f}")
    ok_rate, ok_env = True, True
    for l in (1, 2, 3):
        d = deltas[l]
        for k in range(1, KMAX):
            if d[k - 1] > 1e-12:
                ok_rate &= d[k] <= RATE_BAR * d[k - 1]
        C_l = 8 * d[1]                      # frozen anchor 4*2*delta_1
        ok_env &= all(d[k] <= C_l * 2.0 ** (-k) + 1e-15
                      for k in range(1, KMAX))
    rate_fit = {l: (deltas[l][KMAX - 1] / deltas[l][1]) ** (1 / (KMAX - 2))
                for l in (1, 2, 3)}
    check(f"S2.1 geometric tail: every ratio <= {RATE_BAR} (fitted "
          "rates per doubling: "
          + ", ".join(f"l={l}: {rate_fit[l]:.3f}" for l in (1, 2, 3))
          + " -- vs the dim-law 0.5; reported, not forced)", ok_rate)
    check("S2.2 envelope delta_k <= C 2^-k with frozen anchor "
          "C = 8 delta_1: summability quantified "
          f"(sum of tail defects l=2: {sum(deltas[2][1:]):.3e})", ok_env)
    s2_ok = ok_rate and ok_env

    # ============ S3: telescoping / unique limit ======================
    print("\n-- S3: telescoping to the unique limit (l = 2) --")
    r_last = deltas[2][KMAX - 1] / deltas[2][KMAX - 2]
    rho_last = rhos[2][KMAX]
    rho_prev = rhos[2][KMAX - 1]
    rho_proxy = rho_last + (rho_last - rho_prev) * r_last / (1 - r_last)
    C2m = 8 * deltas[2][1]
    ok_tail = True
    for k in range(1, KMAX):
        lhs = tracenorm(rho_proxy - rhos[2][k])
        bar = min(TAIL_FACTOR * deltas[2][k], 2 * C2m * 2.0 ** (-k))
        ok_tail &= lhs <= bar + 1e-12
        print(f"   k={k}: ||rho_proxy - rho_k||_1 = {lhs:.3e}  <=  "
              f"min(2.25 delta_k, 2C 2^-k) = {bar:.3e}")
    check("S3.1 Cauchy tail bound holds on every rung (exact "
          "comparison with the measured C)", ok_tail)
    ok_batt = True
    for a in batt:
        g = [abs(np.trace((rhos[2][k] - rho_proxy) @ a))
             for k in range(KMAX + 1)]
        for k in range(2, KMAX):
            if g[k - 1] > 1e-12:
                ok_batt &= g[k] <= 0.6 * g[k - 1] + 1e-12
    check("S3.2 frozen 6-observable battery: gaps to the limit fall "
          "with tail ratio <= 0.6 (floor 1e-12)", ok_batt)
    dev_prox = tracenorm(rho_proxy - rho_last)
    check("S3.3 extrapolation uniqueness: Richardson vs plain-last "
          f"proxies differ by {dev_prox:.2e} <= "
          f"2.25 delta_5 = {TAIL_FACTOR * deltas[2][KMAX - 1]:.2e}",
          dev_prox <= TAIL_FACTOR * deltas[2][KMAX - 1] + 1e-12)
    print("   TYPED: summable defects => norm-Cauchy => unique limit "
          "state is ELEMENTARY (dual-space completeness, telescoping);"
          "\n   the operator-algebra content (Umegaki expectations; "
          "Cuculescu-type a.e. results cited as context) sits in the"
          "\n   GNS/normality steps 5-7 below, typed not executed.")
    s3_ok = ok_tail and ok_batt \
        and dev_prox <= TAIL_FACTOR * deltas[2][KMAX - 1] + 1e-12

    # ============ S4: uniform split/normality precursors ==============
    print("\n-- S4: uniform split bounds + determinant witness --")
    winB = window(N0, 6, 2)
    joint = wins[2] + winB
    c8 = jw_ops(8)
    ww, WW = np.linalg.eig(HW[2])
    order = np.argsort(-np.imag(ww))
    ww, WW = ww[order], WW[:, order]
    i = 0
    while i < 4:
        j = i
        while j < 4 and abs(ww[j] - ww[i]) < 1e-9:
            j += 1
        Q, _ = np.linalg.qr(WW[:, i:j])
        WW[:, i:j] = Q
        i = j
    d1 = [sum(np.conj(WW[j, i]) * c8[j] for j in range(4))
          for i in range(4)]
    d2 = [sum(np.conj(WW[j, i]) * c8[4 + j] for j in range(4))
          for i in range(4)]

    def battc(d):
        return {0: [d[0].conj().T @ d[0], d[0].conj().T @ d[1]],
                1: [d[0].conj().T, d[2]],
                2: [d[0].conj().T @ d[1].conj().T,
                    d[0].conj().T @ d[2]],
                3: [d[0], d[2].conj().T]}

    b1, b2 = battc(d1), battc(d2)
    prof = {(c, cp): [] for c in range(4) for cp in range(4)}
    dets = []
    for k in range(KMAX + 1):
        Cj = Cts[k][np.ix_(joint, joint)]
        X = Cts[k][np.ix_(wins[2], winB)]
        dets.append(float(np.linalg.det(
            np.eye(4) - X @ X.conj().T).real))
        rho8 = gaussian_rho(Cj, c8)
        for c in range(4):
            for cp in range(4):
                m = 0.0
                for a in b1[c]:
                    for b in b2[cp]:
                        val = abs(np.trace(rho8 @ (a @ b))
                                  - np.trace(rho8 @ a)
                                  * np.trace(rho8 @ b))
                        m = max(m, float(val)
                                / (np.linalg.norm(a, 2)
                                   * np.linalg.norm(b, 2)))
                prof[(c, cp)].append(m)
    ok_bar, ok_tl, n_zero = True, True, 0
    for (c, cp), p in sorted(prof.items()):
        if max(p) < 1e-12:
            n_zero += 1
            continue
        bar = max(2 * max(p[0], p[1]), 1e-3)
        ok_bar &= all(v <= bar for v in p)
        ok_tl &= abs(p[KMAX] - p[KMAX - 1]) \
            <= abs(p[KMAX - 1] - p[KMAX - 2]) + 1e-12
        print(f"   nu({c},{cp}): " + " ".join(f"{v:.5f}" for v in p))
    check(f"S4.1 sector-resolved profiles uniform along the tower "
          f"(two-level anchor; {16 - n_zero} nonzero, {n_zero} exact "
          "conservation zeros) with shrinking tails", ok_bar and ok_tl)
    print("   D_k = det(1 - X X*): "
          + " ".join(f"{v:.6f}" for v in dets))
    ok_det = all(v >= DET_BAR for v in dets) and \
        abs(dets[KMAX] - dets[KMAX - 1]) \
        <= abs(dets[KMAX - 1] - dets[KMAX - 2]) + 1e-12
    check(f"S4.2 determinant witness D_k >= {DET_BAR} uniformly and "
          "stabilizing (the estimate a normality/split step consumes)",
          ok_det)
    s4_ok = ok_bar and ok_tl and ok_det

    # ============ steps 5-7 typed ====================================
    print("""
-- Steps 5-7 (typed, NOT executed): the analytic remainder --
  5. GNS RECONSTRUCTION of omega_inf on the quasi-local algebra
     (inductive-limit C*-algebra exists by S1 exactness; omega_inf
     exists uniquely by S2+S3).  Finite evidence: this probe.
  6. LOCAL NORMALITY of the GNS representation on each A(W)
     (nuclearity-type estimate; the uniform S4 witnesses -- sector
     profiles + determinant bound -- are the finite input).
  7. SPLIT PROPERTY (standard split inclusion) and the mu4
     SIMPLE-CURRENT EXTENSION (GATE.METRIC.11, [B:A] = 4 = |mu4|)
     on the limit net; finite evidence: S4 + the exact dim law
     d_c = 4^(l-1) + 2^(l-1) cos(pi c/2) with obstruction gap 2^-l
     (arf-qsystem run) as the asymptotic-crossed-product precursor.
""")

    # ============ Controls ============================================
    print("-- Controls (must fire) --")
    Vs = shift_iso(48)
    w_small = window(48, 0, 2)
    w_big4 = window(96, 0, 4)
    Pmask = np.zeros(96)
    Pmask[w_big4] = 1.0
    leak = float(np.linalg.norm(Vs[:, w_small] * (1 - Pmask)[:, None], 2))
    check(f"C1 fires: shifted-bond isometry leaks out of the doubled "
          f"window (leak {leak:.3f} > {LEAK_BAR}): the filtration "
          "A_k c A_(k+1) breaks", leak > LEAK_BAR)
    v2m = np.zeros(16, dtype=complex)
    for P in Ps[2]:
        o = onb_of(P)
        if o.shape[1]:
            v2m += o[:, 0]
    v2m /= np.linalg.norm(v2m)

    def EZ2(x):
        UU = U4[2] @ U4[2]
        return (x + UU @ x @ UU.conj().T) / 2

    lam2 = lam_of(np.outer(v2m, v2m.conj()), EZ2)
    check("C2 fires: Z2-only average has lambda = 1/2 != 1/4 (not the "
          "index-4 expectation system)", abs(lam2 - 0.5) < 1e-8,
          f"lambda = {lam2:.10f}")
    rng3 = np.random.default_rng(SEED + 1)

    def scr_cov(Nk, k):
        frac = 0.3 if k % 2 == 0 else 0.7
        occ = np.zeros(Nk)
        occ[rng3.permutation(Nk)[:int(frac * Nk)]] = 1.0
        return covariance_occ(Nk, occ)

    Cts_scr = pullback(haar_iso, scr_cov, KMAX)
    rho_scr = [gaussian_rho(Ct[np.ix_(wins[2], wins[2])], cops[2])
               for Ct in Cts_scr]
    d_scr = [tracenorm(rho_scr[k + 1] - rho_scr[k]) for k in range(KMAX)]
    check("C3 fires: scrambled sea gives O(1) defects "
          f"(delta_4 = {d_scr[4]:.3f}, delta_5 = {d_scr[5]:.3f} > "
          f"{CTRL_DEFECT_BAR}): summability breaks",
          min(d_scr[4], d_scr[5]) > CTRL_DEFECT_BAR)
    Cts_dec = pullback(decim_iso, lambda Nk, k: cov_of(Nk), KMAX)
    rho_dec = gaussian_rho(Cts_dec[KMAX][np.ix_(wins[2], wins[2])],
                           cops[2])
    dev_dec = tracenorm(rho_dec - np.eye(16) / 16)
    dev_haar = tracenorm(rhos[2][KMAX] - np.eye(16) / 16)
    check("C4 fires: decimation converges to the DEGENERATE limit "
          f"(||rho_dec - 1/16||_1 = {dev_dec:.1e} < 1e-3, Haar limit "
          f"{dev_haar:.3f} > 0.1): the coherent bond is load-bearing",
          dev_dec < 1e-3 and dev_haar > 0.1)

    # ============ QGEO note + verdict =================================
    print("""
-- GATE.QGEO relation (typed architectural note, no gate) --
The open majorant residues (b) 'L2 uniform FH/RH [hard-technical]'
and (c) 'L3 uniformity [medium]' demand uniform POINTWISE majorant
control (sup norms, uniform in grid refinement).  The martingale
route needs only SUMMABLE STATE-NORM defects (S2) for the existence
and uniqueness of the limit state -- dual-space completeness, no
uniform-in-refinement constant.  Uniformity re-enters only in the
typed normality/split step (6-7), where the S4 determinant witnesses
are the finite input.  The route bypasses (b)/(c) for limit
existence and localizes them in normality: an architectural
reallocation, not a proof of (b)/(c).""")

    names_ok = dict(CHECKS)
    ctrl = all(v for n, v in CHECKS if n.startswith("C"))
    s1_ok = all(v for n, v in CHECKS if n.startswith("S1"))
    dead = any(deltas[l][k] >= 0.9 * deltas[l][k - 1] - 1e-15
               and deltas[l][k - 1] > 1e-12
               for l in (1, 2, 3) for k in range(2, KMAX))
    if s1_ok and s2_ok and s3_ok and s4_ok and ctrl:
        verdict = "MARTINGALE-HYPOTHESES-MET"
    elif dead and not s2_ok:
        verdict = "MARTINGALE-DEAD"
    else:
        verdict = "MARTINGALE-PARTIAL" + ("" if ctrl else " (CONTROL-VOID)")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}"
          f"   ({time.time() - t0:.1f} s)")
    print(f"""
FLAGS: S1 = {s1_ok}, S2 = {s2_ok} (fitted rates {rate_fit[1]:.3f}/"""
          f"""{rate_fit[2]:.3f}/{rate_fit[3]:.3f} per doubling), S3 = {s3_ok},
S4 = {s4_ok}, controls = {ctrl}.
Typed: all finite-level evidence FOR the cited continuum steps; the
limit-net theorems (GNS, normality, split, extension) remain typed
steps 5-7.  No marker moves; exploration only.""")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
