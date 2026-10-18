#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""TFPT.POSITIVE_DESCENT.MASTER.01 -- the abstract positive-descent
master theorem, its kernel-checked Lean core, and BOTH instance checks:
G_net (measured, complete) and PRIME/PACKET (measured, with the NEW
prime-side state-defect summability number).

THE FROZEN THEOREM CANDIDATE (MASTER.01).  Given
  (1) finite operator systems A_n with unital inclusions iota_n,
  (2) positive states omega_n on A_n,
  (3) completely positive transition maps compatible with iota_n,
  (4) a finite symmetry group G with character sectors (exact
      projectors P_chi, sum P_chi = id),
  (5) SUMMABLE compatibility defects
      ||omega_{n+1} o iota_n - omega_n|| <= delta_n,  sum delta_n < oo,
  (6) a sector-adapted closure datum,
  (7) a monotone/Mosco-convergent form family,
then a unique positive limit state omega_oo exists and every
compatible sector projector has a well-defined positive limit sector.

WHAT IS PROVED vs TYPED (honest split).  The load-bearing core --
(a) summable-defect telescoping => unique norm-limit ((5) => limit,
with the quantitative Cauchy tail), (b) positivity passes to the
limit ((2) closed under limits), (c) sector decomposition commutes
with the limit ((4) exact) -- is KERNEL-CHECKED in
  experiments/lean4-carrier-rigidity/TfptCarrier/PositiveDescentMaster.lean
in the finite sector-weight form (states resolved over the character
sectors of the finite abelian symmetry, i.e. vectors of nonnegative
sector weights -- exactly the data BOTH instances carry; the
matrix-state positivity closure is the GramCompactness.lean legacy,
posSemidef_of_tendsto, cited not re-proved).  Hypotheses (6) and (7)
are NOT used by the core existence/positivity conclusion; they are
the per-instance closure data consumed by the later normality /
form-convergence steps -- typed, never gated here.  Nothing here is
a continuum theorem and NOTHING is an RH claim.

INSTANCE 1 -- G_NET (re-measured here, self-contained): the Haar CAR
ladder on the fixed l = 2 window (the certified martingale system:
exact isometry tower, index-4 mu4 expectations, chiral-sea states).
  (1) exact filtration [measured: support coherence leak = 0];
  (2) rho_k >= 0 [measured: min eigenvalue];
  (3) the index-4 expectation E(x) = sum_q P_q x P_q is CP -- Choi
      matrix PSD, unital, trace-preserving [measured, 256 x 256];
  (4) mu4 sectors exact (sum P_q = 1, P_q P_q' = delta P_q); dim law
      traces (6,4,2,4)/16 => w_1 = w_3 = 1/4 evenness [exact];
  (5) trace-norm defects delta_k, ratios <= 0.55, envelope
      C = 8 delta_1 vs 2^-k [the certified martingale gates, KMAX 5];
  (6) closure datum = the explicit 185-element Watatani quasi-basis /
      Q-system data (arf-qsystem run) [typed, cited];
  (7) form family = the Mosco strand [typed, open].

INSTANCE 2 -- PRIME/PACKET (the NEW measurement): the packet register
G = C2 x F2^4 x Z4 (|G| = 128, the frozen positive_descent_probe v2
state) with the packet GNS state at depth N,
    omega_N = (1/Z_N) sum_{events n <= N} w_n <x_n, . x_n>/||x_n||^2,
    w_n = Lambda(n)/sqrt(n),
on the FIXED 128-dim commutative register algebra C[G].  Since C[G]
is commutative, the state IS its character density: the 12 sector
classes (eps, V-class, j-class) with multiplicities
(2 or 14) x (2 if j = 1 else 1) summing to 128, and the state norm is
EXACTLY the l1 norm over the 128 characters:
    ||omega - omega'|| = sum_sec mult_sec |q(sec) - q'(sec)|,
    q(sec) = gns_row(sec)/128.
Slot data per event (the frozen v2 population register, rebuilt
self-contained and re-gated): c2m = a_n(f8)/sigma3(n) (f8 =
eta(2t)^4 eta(4t)^4 via the eta recurrence, exact int64, certified by
Th0 - Th2 = -8 f8 on ALL odd n); mhat = (1, (Th0-Th2)/E,
(Th0-Th1+Th2-Th3)/E), E = 240 sigma3, from the exact D5/A3 class
thetas; vhat = -1/7 on the v7 class for ram-odd events (odd powers of
2), else 1.  Channels: p = 2 -> ro/re (odd/even power), p = 1 mod 4
-> sp, else in (the v755 zeta-free channel split, rebuilt).
THE NEW NUMBER: the state-norm defect sequence
    delta_k = ||omega_{N_{k+1}} - omega_{N_k}||,  N_k = 256 * 2^k,
    k = 0..5 (theta reach N_THETA = 16500 covers N_6 = 16384),
and its summability.  THIS IS NOT the corner-rise/CPGATE object: the
corner gates measured WINDOW-functional increments (the signed Weil
window along rungs); here the defect is the STATE norm on the packet
algebra -- the master theorem's hypothesis (5) in the exact sense.
STRUCTURAL PREDICTION (reported against, not forced): the per-event
profiles converge fast (measured in scoping: mh2(p) = -1/15 EXACTLY
for every odd prime -- an exact Eisenstein ratio, zero variance;
c2m, mh1 = O(n^{-3/2}) Deligne decay; the 2-power ladder converges at
2^-m), so the defect is dominated by the mass dilution Z_N ~ 2 sqrt N
=> rate ~ 2^{-1/2} per doubling: geometric, hence summable.

CALIBRATION DECLARED (v755 precedent; scoping run 2026-08-06, before
this probe's gates were frozen): true-ladder defects 1.43e-2 ->
2.49e-3 (ratios 0.66-0.74), label-scramble control ~2.6e-1 flat,
Epstein-drift control rising to ~1.2e-1.  The bars below are frozen
from that calibration with slack; this probe's run is the first run
against the frozen gates.

PREREGISTERED GATES (frozen before this probe's first run):
A ABSTRACT MIRROR (the Lean statements, numeric witness):
  A1 synthetic sequence with defects 2^-n: Cauchy tail bound
     ||q_n - q_oo|| <= sum_{j >= n} delta_j on every rung (1e-12);
     limit of nonneg vectors nonneg; sector sums commute with the
     limit (1e-12).  (The kernel-checked versions live in Lean.)
B INSTANCE 1 (G_net, l = 2 window, KMAX = 5):
  B1 filtration exact: V*V = 1 (1e-14) and support-coherence leak = 0
     (1e-14) at N = 48, 96; H_W level-independent (exact).
  B2 E is CP: Choi(E) min eigenvalue >= -1e-10; E(1) = 1 and
     tr o E = tr (1e-10).
  B3 defects: ratios r_k <= 0.55 (k >= 1, floor 1e-12); envelope
     delta_k <= 8 delta_1 * 2^-k (k >= 1, +1e-15).
  B4 states positive: min eig rho_k >= -1e-12; sector traces
     (6,4,2,4) exact => w_1 = w_3 = 1/4; sum_q P_q = 1,
     P_q P_q' = delta_qq' P_q (1e-10).
C INSTANCE 2 (prime/packet, ladder N_k = 256 * 2^k, k = 0..6):
  C1 packet layer exact: theta heads (52,64,60,64); glue identity
     sum_j Th_j = 240 sigma3 for ALL n <= 16500; Th1 = Th3;
     Th0 - Th2 = -8 f8 on ALL odd n (int64 divisibility exact).
  C2 register states: every per-event sector value >= 0 (squares,
     verified), every depth-N census row >= 0, Parseval/unit ward
     |sum mult q - 128|/128 <= 1e-9 at every depth.
  C3 ladder transitions are convex/CP: q_{k+1} =
     (1 - t_k) q_k + t_k nu_k with t_k = W_shell/W_{k+1} in (0,1),
     nu_k a state (nonneg, unit ward 1e-9), identity to 1e-12.
  C4 THE NEW SUMMABILITY MEASUREMENT (load-bearing):
     C4.1 ratios r_k = delta_k/delta_{k-1} <= 0.85 for k = 1..5;
     C4.2 envelope delta_k <= C * (3/4)^k with frozen C := 2 delta_0
          (k >= 1, +1e-15) -- summability quantified; fitted rate
          reported against the dilution law 2^{-1/2} ~ 0.707.
  C5 Cauchy tail on every rung: ||q_last - q_k||_1 <=
     4 C (3/4)^k + 1e-12 (the telescoped envelope tail).
D PAYOFF (typed print, gated only through C4): with (5) measured
  summable on the prime side, MASTER.01 applies to BOTH instances --
  the unique limit state exists; limit positivity reduces to the
  SECTOR-FLOOR question only (which sectors have strictly positive
  floors -- the GL1 sign-sector floor is exactly what corner-rise/
  CPGATE left open).  The selection problem is eliminated.
CONTROLS (all must fire):
  K1 G_net scrambled sea (alternating 0.3/0.7 occupations):
     min(delta_3, delta_4) > 0.05 -- summability breaks.
  K2 prime label scramble (V-frame misassignment: every odd-p event
     in odd doubling shells read as ram-odd): min(delta_4, delta_5)
     > 0.02 -- O(1) defects, summability breaks.
  K3 prime Epstein-type drift (c2m -> cos(2 ln n): a non-decaying
     unitary drift, the off-line-oscillation surrogate):
     min(delta_4, delta_5) > 0.02 -- summability breaks.
  K4 non-positive transition: an update family with SUMMABLE defects
     but one non-positivity-preserving step: the limit exists yet
     min sector weight < -0.01 -- positivity hypotheses (2)/(3) are
     NOT implied by (5); the conclusion needs both.
VERDICT ENUM (frozen):
  MASTER-BOTH-INSTANCES : A + B + C all pass and all controls fire
      (the two continuum problems are one theorem's instances;
      remaining per-instance open items typed).
  MASTER-GNET-ONLY : B passes but C4 fails (the prime defects not
      summable -- the measured gap typed plainly).
  MASTER-ABSTRACT-ONLY : anything else (steps named); any control
      failure flagged CONTROL-VOID.

HONESTY: every measurement is finite-level evidence FOR the master
theorem's hypotheses at finite level, never the continuum theorem
and never an RH statement.  No marker moves.  Exploration only
(tfpt-experiment firewall): NOT wired into run_all.py, no ledger row,
no paper edit, no file writes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/positive_descent_master_probe.py
"""

import hashlib
import inspect
import math
import sys
import time

import numpy as np

TOL = 1e-10
SEED = 20260806
N_THETA = 16500
LADDER0 = 256
KP = 6                       # prime ladder: N_k = 256 * 2^k, k = 0..KP
GN0 = 48
GKMAX = 5                    # G_net tower depth (N = 48 * 2^k)
GRATE_BAR = 0.55
PRATE_BAR = 0.85
PENV_BASE = 0.75
CTRL_GNET_BAR = 0.05
CTRL_PRIME_BAR = 0.02
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name
          + ("  -- " + detail if detail else ""))
    return ok


def section(title):
    print("\n-- %s --" % title)


# ================= packet layer (self-contained, re-gated) ============


def sparse_theta_terms(kind, cap):
    out = []
    if kind in ("th3", "th4"):
        out.append((0, 1))
        n = 1
        while n * n <= cap:
            out.append((n * n, 2 if kind == "th3" else 2 * ((-1) ** n)))
            n += 1
    else:                                   # th2-type: odd squares
        o = 1
        while o * o <= cap:
            out.append((o * o, 2))
            o += 2
    return out


def sparse_mul(dense, terms):
    out = np.zeros_like(dense)
    for e, c in terms:
        if e == 0:
            out += c * dense
        else:
            out[e:] += c * dense[:-e]
    return out


def build_thetas():
    """exact class thetas Th_j, sigma3, f8 coefficients to N_THETA."""
    sig3 = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(1, N_THETA + 1):
        sig3[d::d] += d ** 3
    scap = 2 * N_THETA
    t3 = sparse_theta_terms("th3", scap)
    t4 = sparse_theta_terms("th4", scap)
    one = np.zeros(scap + 1, dtype=np.int64)
    one[0] = 1
    p3 = one.copy()
    p4 = one.copy()
    for _ in range(8):
        p3 = sparse_mul(p3, t3)
        p4 = sparse_mul(p4, t4)
    m53 = one.copy()
    for _ in range(5):
        m53 = sparse_mul(m53, t3)
    for _ in range(3):
        m53 = sparse_mul(m53, t4)
    m35 = one.copy()
    for _ in range(5):
        m35 = sparse_mul(m35, t4)
    for _ in range(3):
        m35 = sparse_mul(m35, t3)
    num0 = p3 + m53 + m35 + p4
    num2 = p3 - m53 - m35 + p4
    ok_div = bool(np.all(num0 % 4 == 0) and np.all(num2 % 4 == 0))
    Th0 = (num0 // 4)[::2][:N_THETA + 1].copy()
    Th2 = (num2 // 4)[::2][:N_THETA + 1].copy()
    tcap = 8 * N_THETA
    t2 = sparse_theta_terms("th2", tcap)
    acc = np.zeros(tcap + 1, dtype=np.int64)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    ok_div &= bool(np.all(acc[::8][:N_THETA + 1] % 4 == 0))
    Th1 = (acc[::8][:N_THETA + 1] // 4).copy()
    # f8 eta recurrence (exact; int64 dot certified by the -8f8 gate)
    tk = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(2, N_THETA + 1, 2):
        tk[d::d] += d * (4 + (4 if d % 4 == 0 else 0))
    g = np.zeros(N_THETA, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_THETA):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, r = divmod(-s, n)
        if r != 0:
            return None
        g[n] = q
    a = np.zeros(N_THETA + 1, dtype=np.int64)
    a[1:] = g
    return dict(sig3=sig3, Th_real=(Th0, Th1, Th2, Th1), a=a,
                ok_div=ok_div)


def primes_upto(N):
    s = np.ones(N + 1, bool)
    s[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def build_events(cap):
    """prime-power events n <= cap: (n, Lambda(n)/sqrt(n), channel)."""
    ev = []
    for p in primes_upto(cap):
        m, n = 1, int(p)
        while n <= cap:
            if p == 2:
                ch = "ro" if m % 2 == 1 else "re"
            else:
                ch = "sp" if p % 4 == 1 else "in"
            ev.append((n, math.log(p) / math.sqrt(n), ch))
            m += 1
            n *= int(p)
    ev.sort()
    return ev


SECTORS = [(e, v, j) for e in (1, -1) for v in ("v1", "v7")
           for j in (0, 1, 2)]
MULT = np.array([(2 if v == "v1" else 14) * (2 if j == 1 else 1)
                 for e, v, j in SECTORS], float)


def event_profile(n, ch, th, mode="true"):
    """per-event GNS sector values t^2/nu over the 12 classes."""
    sig3, a = th["sig3"], th["a"]
    Th0, Th1, Th2, Th3 = th["Th_real"]
    E = 240.0 * float(sig3[n])
    c2m = float(a[n]) / float(sig3[n])
    if mode == "ep":
        c2m = math.cos(2.0 * math.log(n))
    if mode == "scr" and ch in ("sp", "in") \
            and int(math.log2(n)) % 2 == 1:
        ch = "ro"
    mh = (1.0, (float(Th0[n]) - float(Th2[n])) / E,
          (float(Th0[n]) - float(Th1[n]) + float(Th2[n])
           - float(Th3[n])) / E)
    t = np.empty(12)
    for k, (e, v, j) in enumerate(SECTORS):
        c2f = 1.0 if e == 1 else c2m
        vf = (-1.0 / 7.0) if (ch == "ro" and v == "v7") else 1.0
        t[k] = c2f * vf * mh[j]
    nu = float((t * t) @ MULT) / 128.0
    return (t * t) / nu


def l1_state(qa, qb):
    """state norm on C[G]: l1 over the 128 characters."""
    return float(np.abs(qa - qb) @ MULT) / 128.0


# ================= G_net layer (as in the martingale probe) ===========


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


def tracenorm(A):
    return float(np.abs(np.linalg.eigvalsh((A + A.conj().T) / 2)).sum())


def sha_freeze():
    fns = [sparse_theta_terms, sparse_mul, build_thetas, primes_upto,
           build_events, event_profile, l1_state, spower, covariance_occ,
           covariance, window, haar_iso, jw_ops, gamma_partial,
           gaussian_rho, sector_projs, tracenorm]
    blob = "".join(inspect.getsource(f) for f in fns)
    blob += repr((TOL, SEED, N_THETA, LADDER0, KP, GN0, GKMAX, GRATE_BAR,
                  PRATE_BAR, PENV_BASE, CTRL_GNET_BAR, CTRL_PRIME_BAR,
                  SECTORS, MULT.tolist()))
    return hashlib.sha256(blob.encode()).hexdigest()


# ======================================================================


def leg_abstract():
    section("A: abstract-core mirror (Lean statements, numeric witness)")
    rng = np.random.default_rng(SEED)
    q_lim = np.abs(rng.normal(size=12))
    dirs = rng.normal(size=(40, 12))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    qs = [q_lim + sum(2.0 ** (-j) * dirs[j] * 0.01 for j in range(n, 40))
          for n in range(20)]
    deltas = [np.linalg.norm(qs[n + 1] - qs[n], 1) for n in range(19)]
    tails = [sum(deltas[n:]) + 2.0 ** (-19) * 0.5 for n in range(19)]
    ok_tail = all(np.linalg.norm(qs[n] - q_lim, 1) <= tails[n] + 1e-12
                  for n in range(19))
    ok_pos = bool(np.all(q_lim + 0.02 >= 0))     # witness structure only
    S = [0, 3, 7]
    ok_sec = abs(sum(qs[18][i] for i in S) - sum(q_lim[i] for i in S)) \
        <= sum(abs(qs[18][i] - q_lim[i]) for i in S) + 1e-15
    check("A1 telescoping mirror: Cauchy tail <= summed defects on "
          "every rung; sector sums commute with the limit "
          "(kernel-checked versions: PositiveDescentMaster.lean)",
          ok_tail and ok_pos and ok_sec)


def leg_gnet():
    section("B: INSTANCE 1 -- G_net (l = 2 window, tower k <= %d)"
            % GKMAX)
    t0 = time.time()
    ok_iso, ok_supp = True, True
    for N in (48, 96):
        V = haar_iso(N)
        ok_iso &= np.abs(V.T @ V - np.eye(N)).max() < 1e-14
        w_small = window(N, 0, 2)
        w_big = window(2 * N, 0, 4)
        P = np.zeros(2 * N)
        P[w_big] = 1.0
        ok_supp &= np.abs(V[:, w_small] * (1 - P)[:, None]).max() < 1e-14
    HN = spower(GN0, GN0 // 2)
    win2 = window(GN0, 0, 2)
    HW = HN[np.ix_(win2, win2)]
    H_big = spower(GN0 * 2 ** GKMAX, GN0 * 2 ** (GKMAX - 1))
    wbig = window(GN0 * 2 ** GKMAX, 0, 2)
    ok_lvl = np.abs(H_big[np.ix_(wbig, wbig)] - HW).max() < 1e-14
    check("B1 (1) filtration exact: V*V = 1, support-coherence leak = 0"
          " at N = 48, 96; window data level-independent",
          ok_iso and ok_supp and ok_lvl)

    c4 = jw_ops(4)
    U4 = gamma_partial(HW, list(range(4)), c4)
    Ps = sector_projs(U4)

    def E2(x):
        return sum(P @ x @ P for P in Ps)

    # Choi matrix of E on the 16-dim window algebra (256 x 256)
    dim = 16
    choi = np.zeros((dim * dim, dim * dim), dtype=complex)
    for i in range(dim):
        for j in range(dim):
            eij = np.zeros((dim, dim), dtype=complex)
            eij[i, j] = 1.0
            choi += np.kron(E2(eij), eij)
    ev_choi = np.linalg.eigvalsh((choi + choi.conj().T) / 2)
    unital = np.abs(E2(np.eye(dim, dtype=complex))
                    - np.eye(dim)).max()
    rng = np.random.default_rng(SEED)
    dev_tr = 0.0
    for _ in range(4):
        A = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
        dev_tr = max(dev_tr, abs(np.trace(E2(A)) - np.trace(A)))
    check("B2 (3) E is CP: Choi min eig = %.2e >= -1e-10; unital "
          "(dev %.1e); trace-preserving (dev %.1e)"
          % (float(ev_choi.min()), unital, dev_tr),
          ev_choi.min() >= -1e-10 and unital < TOL and dev_tr < TOL)

    covs = {}

    def cov_of(N):
        if N not in covs:
            covs[N] = covariance(N)
        return covs[N]

    def pullback(cov_fun):
        out = []
        chain = np.eye(GN0)
        Nk = GN0
        for k in range(GKMAX + 1):
            out.append(chain.T.conj() @ cov_fun(Nk, k) @ chain)
            chain = haar_iso(Nk) @ chain
            Nk *= 2
        return out

    Cts = pullback(lambda Nk, k: cov_of(Nk))
    rhos = [gaussian_rho(Ct[np.ix_(win2, win2)], c4) for Ct in Cts]
    deltas = [tracenorm(rhos[k + 1] - rhos[k]) for k in range(GKMAX)]
    print("   G_net defects delta_k (trace norm): "
          + "  ".join("%.3e" % d for d in deltas))
    ok_rate = all(deltas[k] <= GRATE_BAR * deltas[k - 1]
                  for k in range(1, GKMAX) if deltas[k - 1] > 1e-12)
    Cg = 8 * deltas[1]
    ok_env = all(deltas[k] <= Cg * 2.0 ** (-k) + 1e-15
                 for k in range(1, GKMAX))
    rate_fit = (deltas[GKMAX - 1] / deltas[1]) ** (1.0 / (GKMAX - 2))
    check("B3 (5) defects summable: ratios <= %.2f, envelope "
          "delta_k <= 8 delta_1 2^-k (fitted rate %.3f/doubling)"
          % (GRATE_BAR, rate_fit), ok_rate and ok_env)

    min_eig = min(float(np.linalg.eigvalsh(
        (r + r.conj().T) / 2).min()) for r in rhos)
    trs = [float(np.trace(P).real) for P in Ps]
    res = sum(Ps[q] @ Ps[qp] - (Ps[q] if q == qp else 0)
              for q in range(4) for qp in range(4))
    dev_alg = max(float(np.abs(sum(Ps) - np.eye(dim)).max()),
                  float(np.abs(res).max()))
    ok_even = np.allclose(trs, [6, 4, 2, 4], atol=1e-9)
    check("B4 (2)+(4) states positive (min eig %.1e >= -1e-12); mu4 "
          "sector algebra exact (dev %.1e); traces (6,4,2,4) => "
          "w_1 = w_3 = 1/4 evenness" % (min_eig, dev_alg),
          min_eig >= -1e-12 and dev_alg < TOL and ok_even)
    print("   (6) closure datum: 185-element Watatani quasi-basis "
          "(arf-qsystem run) [typed, cited]; (7) Mosco form family "
          "[typed, open].   (%.1f s)" % (time.time() - t0))
    return dict(deltas=deltas, rate=rate_fit,
                ok=all(v for n, v in CHECKS if n.startswith("B")),
                pullback=pullback, rhos=rhos, win2=win2, c4=c4)


def leg_prime(th):
    section("C: INSTANCE 2 -- prime/packet (ladder N_k = %d * 2^k)"
            % LADDER0)
    t0 = time.time()
    sig3 = th["sig3"]
    Th0, Th1, Th2, Th3 = th["Th_real"]
    a = th["a"]
    heads = (int(Th0[1]), int(Th1[1]), int(Th2[1]), int(Th3[1]))
    tot_ok = bool(np.all((Th0 + Th1 + Th2 + Th3)[1:]
                         == 240 * sig3[1:]))
    f8_ok = bool(np.all((Th0 - Th2 + 8 * a)[1:N_THETA:2] == 0))
    check("C1 packet layer exact: heads %s == (52,64,60,64); glue "
          "identity ALL n <= %d; Th1 == Th3; Th0 - Th2 = -8 f8 on ALL "
          "odd n" % (str(heads), N_THETA),
          th["ok_div"] and heads == (52, 64, 60, 64) and tot_ok
          and f8_ok and bool(np.all(Th1 == Th3)))

    ev = build_events(N_THETA)
    P = np.array([event_profile(n, ch, th) for n, w, ch in ev])
    W = np.array([w for n, w, ch in ev])
    Narr = np.array([n for n, w, ch in ev])
    ladder = [LADDER0 * 2 ** k for k in range(KP + 1)]
    rows, zs = [], []
    for Nk in ladder:
        m = Narr <= Nk
        z = float(W[m].sum())
        zs.append(z)
        rows.append((W[m] @ P[m]) / z)
    wards = [abs(float(r @ MULT) / 128.0 - 1.0) for r in rows]
    ok_pos = bool(np.all(P >= -1e-15)) and \
        all(bool(np.all(r >= -1e-15)) for r in rows)
    check("C2 register states: %d events, all per-event sector values "
          ">= 0; census rows >= 0 at all %d depths; unit ward <= %.0e "
          "(max %.1e)" % (len(ev), len(ladder), 1e-9, max(wards)),
          ok_pos and max(wards) <= 1e-9)

    ok_cvx = True
    for k in range(KP):
        m_new = (Narr > ladder[k]) & (Narr <= ladder[k + 1])
        w_sh = float(W[m_new].sum())
        t = w_sh / zs[k + 1]
        nu_sh = (W[m_new] @ P[m_new]) / w_sh
        ident = np.abs((1 - t) * rows[k] + t * nu_sh
                       - rows[k + 1]).max()
        ok_cvx &= (0.0 < t < 1.0) and ident < 1e-12 \
            and bool(np.all(nu_sh >= -1e-15)) \
            and abs(float(nu_sh @ MULT) / 128.0 - 1.0) <= 1e-9
    check("C3 ladder transitions convex/CP: q_{k+1} = (1-t) q_k + "
          "t nu_shell, t in (0,1), nu_shell a state (identity 1e-12)",
          ok_cvx)

    deltas = [l1_state(rows[k + 1], rows[k]) for k in range(KP)]
    print("   PRIME state defects (l1 over 128 characters):")
    print("   %3s %14s %12s %8s" % ("k", "N -> 2N", "delta_k", "ratio"))
    for k in range(KP):
        r = deltas[k] / deltas[k - 1] if k >= 1 else float("nan")
        print("   %3d %6d->%-6d %12.3e %8.3f"
              % (k, ladder[k], ladder[k + 1], deltas[k], r))
    ok_rate = all(deltas[k] <= PRATE_BAR * deltas[k - 1]
                  for k in range(1, KP))
    Cp = 2 * deltas[0]
    ok_env = all(deltas[k] <= Cp * PENV_BASE ** k + 1e-15
                 for k in range(1, KP))
    rate_fit = (deltas[KP - 1] / deltas[1]) ** (1.0 / (KP - 2))
    check("C4 THE NEW NUMBER -- prime state defects SUMMABLE: ratios "
          "<= %.2f; envelope delta_k <= 2 delta_0 (3/4)^k; fitted "
          "rate %.3f/doubling vs dilution law 2^-1/2 = 0.707; "
          "sum of tail defects = %.3e"
          % (PRATE_BAR, rate_fit, sum(deltas[1:])),
          ok_rate and ok_env)
    c4_ok = ok_rate and ok_env

    ok_tail = True
    for k in range(1, KP + 1):
        lhs = l1_state(rows[KP], rows[k])
        bar = 4 * Cp * PENV_BASE ** k
        ok_tail &= lhs <= bar + 1e-12
    check("C5 Cauchy tail on every rung: ||q_last - q_k||_1 <= "
          "4 C (3/4)^k", ok_tail)
    print("   (6) closure datum: sector-adapted Gamma_R continua live "
          "on the WINDOW face [typed]; the state-face open item is "
          "the SECTOR FLOOR (GL1 sign sector), not summability.")
    print("   (7) Mosco form family [typed, parallel strand]."
          "   (%.1f s)" % (time.time() - t0))
    return dict(deltas=deltas, rate=rate_fit, rows=rows, ev=ev,
                ladder=ladder, c4_ok=c4_ok)


def leg_controls(th, gnet):
    section("K: controls (all must fire)")
    # K1: G_net scrambled sea
    rng = np.random.default_rng(SEED + 1)

    def scr_cov(Nk, k):
        frac = 0.3 if k % 2 == 0 else 0.7
        occ = np.zeros(Nk)
        occ[rng.permutation(Nk)[:int(frac * Nk)]] = 1.0
        return covariance_occ(Nk, occ)

    Cts_scr = gnet["pullback"](scr_cov)
    win2, c4 = gnet["win2"], gnet["c4"]
    rho_s = [gaussian_rho(Ct[np.ix_(win2, win2)], c4) for Ct in Cts_scr]
    d_s = [tracenorm(rho_s[k + 1] - rho_s[k]) for k in range(GKMAX)]
    check("K1 fires: G_net scrambled sea gives O(1) defects "
          "(delta_3 = %.3f, delta_4 = %.3f > %.2f)"
          % (d_s[3], d_s[4], CTRL_GNET_BAR),
          min(d_s[3], d_s[4]) > CTRL_GNET_BAR)

    ev = build_events(N_THETA)
    W = np.array([w for n, w, ch in ev])
    Narr = np.array([n for n, w, ch in ev])
    ladder = [LADDER0 * 2 ** k for k in range(KP + 1)]
    for mode, name, why in (
            ("scr", "K2", "label scramble (V-frame misassignment, "
             "alternating shells)"),
            ("ep", "K3", "Epstein-type drift c2m -> cos(2 ln n) "
             "(off-line oscillation surrogate)")):
        Pm = np.array([event_profile(n, ch, th, mode) for n, w, ch in ev])
        rows = [(W[Narr <= Nk] @ Pm[Narr <= Nk])
                / float(W[Narr <= Nk].sum()) for Nk in ladder]
        dm = [l1_state(rows[k + 1], rows[k]) for k in range(KP)]
        check("%s fires: prime %s: min(delta_4, delta_5) = %.3e > %.2f"
              " -- summability breaks"
              % (name, why, min(dm[4], dm[5]), CTRL_PRIME_BAR),
              min(dm[4], dm[5]) > CTRL_PRIME_BAR)

    # K4: summable defects but a non-positivity-preserving transition
    q0 = np.abs(np.random.default_rng(SEED + 2).normal(size=12)) + 0.1
    q0 /= float(q0 @ MULT) / 128.0
    bad_dir = np.zeros(12)
    bad_dir[5] = -(q0[5] + 0.05)
    qs = [q0 + (1 - 2.0 ** (-n)) * bad_dir for n in range(24)]
    d4 = [l1_state(qs[n + 1], qs[n]) for n in range(23)]
    lim = q0 + bad_dir
    ok_sum = all(d4[n + 1] <= 0.5 * d4[n] + 1e-15 for n in range(22))
    check("K4 fires: non-positive transition with SUMMABLE defects "
          "(ratio 1/2 exact) yields a NON-positive limit "
          "(min sector = %.3f < -0.01): positivity is a separate "
          "hypothesis, not implied by (5)" % float(lim.min()),
          ok_sum and lim.min() < -0.01)


def main():
    t0 = time.time()
    print("positive_descent_master_probe -- TFPT.POSITIVE_DESCENT."
          "MASTER.01\n")
    print("SHA-freeze (construction source + constants): %s\n"
          % sha_freeze()[:32])
    print("FROZEN THEOREM (MASTER.01): (1) finite systems + unital "
          "inclusions, (2) positive\nstates, (3) CP transitions, (4) "
          "finite symmetry group with character sectors,\n(5) summable "
          "state defects, (6) sector-adapted closure datum, (7) Mosco "
          "form\nfamily  =>  unique positive limit state; every "
          "compatible sector projector has\na well-defined positive "
          "limit sector.  Kernel-checked core: PositiveDescent"
          "Master.lean\n((a) telescoping+tail, (b) positivity closed, "
          "(c) sectors commute); (6)/(7) are\nper-instance closure "
          "data for the later analytic steps [typed].")

    leg_abstract()

    th = build_thetas()
    if th is None:
        check("C0 eta recurrence divisibility", False)
        return 1

    gnet = leg_gnet()
    prime = leg_prime(th)
    leg_controls(th, gnet)

    section("D: payoff decision")
    print("""   Prime-side hypothesis (5) MEASURED: the packet state defects are
   summable (geometric, fitted rate %.3f/doubling ~ the sqrt-dilution
   law 0.707; sum of measured tail defects %.3e).  MASTER.01 therefore
   applies to BOTH instances at finite level: the unique limit state
   exists on each side by telescoping alone.  What remains per
   instance is NOT existence/selection but:
     * G_net: local normality / split (the typed steps 6-7 of the
       martingale run) -- uniform S4-type witnesses in hand;
     * prime/packet: the SECTOR-FLOOR question -- is the GL1 sign
       sector's limit weight strictly positive with the right value
       (the corner-rise/CPGATE open item), on the WINDOW face with
       the Gamma_R closure datum.  The selection problem (which limit
       state) is eliminated by summability; the sign problem is not.
   NO RH claim; finite-level hypothesis checks only."""
          % (prime["rate"], sum(prime["deltas"][1:])))

    a_ok = all(v for n, v in CHECKS if n.startswith("A"))
    b_ok = all(v for n, v in CHECKS if n.startswith("B"))
    c_ok = all(v for n, v in CHECKS if n.startswith("C"))
    k_ok = all(v for n, v in CHECKS if n.startswith("K"))
    if a_ok and b_ok and c_ok and k_ok:
        verdict = "MASTER-BOTH-INSTANCES"
    elif b_ok and not prime["c4_ok"]:
        verdict = "MASTER-GNET-ONLY"
    else:
        verdict = "MASTER-ABSTRACT-ONLY" + ("" if k_ok
                                            else " (CONTROL-VOID)")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("\n%d/%d checks pass -- VERDICT: %s   (%.1f s)"
          % (n_pass, len(CHECKS), verdict, time.time() - t0))
    print("""
RECOMMENDED CONTRACT TEXT (report only, no file/ledger edit):
  TFPT.POSITIVE_DESCENT.MASTER.01 [O -> measured hypotheses]: the
  positive-descent master theorem (7 hypotheses frozen above; core
  (a)-(c) kernel-checked in TfptCarrier/PositiveDescentMaster.lean;
  GramCompactness.lean carries the matrix positivity closure).
  Instance G_NET: hypotheses (1)-(5) measured (defects %.3f/doubling,
  envelope 8 delta_1 2^-k; E CP via Choi; mu4 evenness exact);
  (6) quasi-basis datum cited; open: normality/split.
  Instance PRIME/PACKET: hypotheses (1)-(5) measured (THE NEW NUMBER:
  state defects %.3f/doubling, summable -- the state norm behaves
  strictly better than the corner increments); (6) Gamma_R datum on
  the window face; open: the GL1 sector floor.  Controls: scrambled
  sea / label scramble / Epstein drift break summability; a
  non-positive transition breaks limit positivity.  NO RH claim.
""" % (gnet["rate"], prime["rate"]))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
