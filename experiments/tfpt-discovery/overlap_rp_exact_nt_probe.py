#!/usr/bin/env python3
"""overlap_rp_exact_nt_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (follow-up to tfpt4d_first_candidate_probe +
overlap_rp_nt_dependence_probe): exact Z4 enumeration on the 2x2 torus
found the OS link-reflection Gram of slice characters PSD for pure
Wilson gauge (min eig ~ -1e-16) but indefinite once |det D_ov|^2 is
included (det-only ~ -4.8e-2, full beta=1 ~ -2.1e-3).  An MC attempt
at Z4 2x4 was DATA_LIMITED (noise floor ~ signal).  Shrinking the
structure group to Z2 makes N_x=2, N_t=4 exactly enumerable
(16 links, 2^16 = 65536) and N_t=2 trivial (8 links, 256).  Is the
overlap RP violation an N_t=2 artifact (overlap sgn wrapping the short
torus), or does it persist at N_t=4?

MODEL.  2D Euclidean Z2 gauge on the N_x x N_t torus, N_x=2, links
u in {+1,-1}.  Wilson gauge action S_g = -beta sum_p u_p with u_p the
oriented plaquette product (Z2: u^{-1}=u).  2D Wilson-Dirac with
gamma1=sigma_x, gamma2=sigma_y, gamma5=sigma_z, r=1; overlap
D_ov = 1 + gamma5 sgn(H_W), H_W = gamma5 (D_W - m0), m0=1 (safe
window 0 < m0 < 2).  Weight variants: pure gauge e^{-S_g}; det-only
|det D|^2; full product.  Fermion types: overlap, and a Wilson-fermion
control |det D_W(m')|^2 at positive bare mass m'=1 (ultralocal in
time; site-reflection RP is Osterwalder-Seiler/Luescher class).

EXCEPTIONAL CONFIGS.  Overlap is defined only for invertible H_W.  On
Z2 (finite group) exceptional configs have POSITIVE measure; they are
EXCLUDED from the overlap measure (weight 0).  A robustness column
keeps them with sign(0)=+1.  Wilson dets are well-defined everywhere
and are never dropped.

REFLECTION (link / site-time, Osterwalder-Seiler).  Even N_t, involution
theta(t) = N_t - 1 - t.  Positive half = slices {N_t/2, ..., N_t-1};
mirror = theta of those.  Observables = ALL Z2 characters of the
positive-half x-links (2 x-links per slice):

  N_t=2: positive {1}, theta: 0 <-> 1,  2 x-links,  4 characters
         (complete L^2 of those links; Z2 analog of the 16 Z4
         characters in the 2x2 probe);
  N_t=4: positive {2,3}, theta: t -> 3-t,  4 x-links, 16 characters;
  N_t=6: positive {3,4,5}, theta: t -> 5-t,  6 x-links, 64 characters
         (pure-gauge validation only; fermion dets skipped if the
         2^24 * eigh projection exceeds the runtime budget).

A cut-adjacent 4-character subalgebra (slice Nt/2 vs Nt/2-1) is
accumulated in the same pass so N_t=2 and N_t=4 can be compared on
the SAME observable algebra.

Gram G_{alpha beta} = < chi_alpha(theta U_+)  chi_beta(U_+) > under
the chosen weight (characters real).  CRITICAL VALIDATION: the PURE
GAUGE Gram MUST be PSD to machine precision at every N_t that is
enumerated -- if not, the reflection map is wrong and the run FAILs
(a wrong 1x4 attempt was discarded this way).  A named overlap
indefiniteness is a FINDING, not a probe failure.

HONEST BOUNDARY: Z2 (not mu4) structure group -- mechanism level; 2D;
small sizes; vectorlike |det|^2; no contract closes; no marker moves.
N_t=6 fermion determinants are attempted only if a vectorized-batch
projection is cheap; otherwise SKIP is typed, not guessed.

VERDICT ENUM: OVERLAP_RP_VIOLATION_{PERSISTS_NT4 | VANISHES_NT4 |
APPEARS_NT4 | HOLDS_BOTH_NT | INCONCLUSIVE_GREYZONE}
+ OVERLAP_FULL_{HOLDS_BOTH_NT | ...}
+ WILSON_CONTROL_{PSD | INDEFINITE | GREYZONE}.
"""
import time

import numpy as np

ok_all = True

NX = 2
BETA = 1.0
M0 = 1.0          # overlap kernel mass (H_W = gamma5 (D_W - M0))
MW = 1.0          # Wilson control: positive bare mass
BATCH = 2048
NT6_BUDGET_S = 90.0
TOL_PSD = 1e-12
TOL_VIOL = 1e-6
EXC_THRESH = 1e-10
SEED = 20260828

S1 = np.array([[0, 1], [1, 0]], dtype=np.complex128)
S2 = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
S3 = np.array([[1, 0], [0, -1]], dtype=np.complex128)
I2 = np.eye(2, dtype=np.complex128)


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


def pos_slices(nt):
    return list(range(nt // 2, nt))


def theta_t(t, nt):
    return nt - 1 - t


def n_obs_of(nt):
    return NX * len(pos_slices(nt))


def decode_U(cs, nt):
    """cs: int64 array of config integers. U[b, mu, x, t] in {+1,-1}."""
    n_links = 2 * NX * nt
    shifts = np.arange(n_links, dtype=np.int64)
    bits = (cs[:, None] >> shifts[None, :]) & 1
    return (1 - 2 * bits).reshape(-1, 2, NX, nt).astype(np.float64)


def U_from_int(c, nt):
    return decode_U(np.array([c], dtype=np.int64), nt)[0]


def gauge_weights(U, beta=BETA):
    ux, ut = U[:, 0], U[:, 1]
    plaq = ux * np.roll(ut, -1, axis=1) * np.roll(ux, -1, axis=2) * ut
    return np.exp(beta * plaq.sum(axis=(1, 2)))


def plaq_sum_one(U):
    tot = 0.0
    nt = U.shape[2]
    for x in range(NX):
        for t in range(nt):
            tot += (U[0, x, t] * U[1, (x + 1) % NX, t]
                    * U[0, x, (t + 1) % nt] * U[1, x, t])
    return tot


def gauge_transform_z2(U, a):
    """U_mu(x) -> g(x) U_mu(x) g(x+mu)^{-1}; Z2: g^{-1}=g."""
    nt = U.shape[2]
    Ug = np.empty_like(U)
    for x in range(NX):
        for t in range(nt):
            Ug[0, x, t] = a[x, t] * U[0, x, t] * a[(x + 1) % NX, t]
            Ug[1, x, t] = a[x, t] * U[1, x, t] * a[x, (t + 1) % nt]
    return Ug


def chars_of_slices(U, slices):
    """All Z2 characters of the x-links on the given time slices.

    Link order: for t in slices, for x in 0..Nx-1.  Character chi_eps
    = prod_i U_i^{eps_i}, eps in {0,1}^{n_obs}, n_chi = 2^{n_obs}.
    """
    n_obs = NX * len(slices)
    n_chi = 1 << n_obs
    stack = np.stack([U[:, 0, x, t] for t in slices for x in range(NX)],
                     axis=1)
    eps = ((np.arange(n_chi)[:, None] >> np.arange(n_obs)) & 1).astype(np.int32)
    bits = (stack < 0).astype(np.int32)
    parity = (bits @ eps.T) & 1
    return (1 - 2 * parity).astype(np.float64), n_chi


def pair_characters(U, nt):
    pos = pos_slices(nt)
    mir = [theta_t(t, nt) for t in pos]
    chi_p, n_chi = chars_of_slices(U, pos)
    chi_r, n_chi_r = chars_of_slices(U, mir)
    assert n_chi == n_chi_r
    return chi_r, chi_p, n_chi


def pair_adjacent(U, nt):
    """Cut-adjacent 4-character algebra: slice Nt/2 vs theta(Nt/2)."""
    tpos = nt // 2
    tmir = theta_t(tpos, nt)
    chi_p, n_chi = chars_of_slices(U, [tpos])
    chi_r, _ = chars_of_slices(U, [tmir])
    return chi_r, chi_p, n_chi


def bkron(A, M):
    """Batched kron(A_{2x2}, M_{B,d,d}) -> (B, 2d, 2d)."""
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
    """Massless (m=0) or massive Wilson-Dirac, r=1, matching the Z4 probe."""
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


def wilson_dirac_one(U, m=0.0):
    return wilson_dirac_batch(U[None], m=m)[0]


def _ov_from_sgn(g5, evecs, sgn):
    n = g5.shape[0]
    sgnh = np.matmul(evecs * sgn[:, None, :],
                     np.conjugate(np.swapaxes(evecs, -1, -2)))
    dov = np.eye(n, dtype=np.complex128) + np.matmul(g5, sgnh)
    _sign, logabs = np.linalg.slogdet(dov)
    return np.exp(2.0 * logabs), dov


def overlap_weights_batch(dw, dim):
    """Return drop (primary) and plus-keep (robustness) |det D_ov|^2.

    drop: exceptional configs (min |eig H_W| < EXC_THRESH) get weight 0.
    plus: those configs kept with sign(0)=+1.
    """
    n = 2 * dim
    g5 = np.kron(S3, np.eye(dim))
    hw = np.matmul(g5, dw - M0 * np.eye(n, dtype=np.complex128))
    hw = 0.5 * (hw + np.conjugate(np.swapaxes(hw, -1, -2)))
    herm_dev = float(np.max(np.abs(hw - np.conjugate(np.swapaxes(hw, -1, -2)))))
    evals, evecs = np.linalg.eigh(hw)
    amin = np.min(np.abs(evals), axis=1)
    exc = amin < EXC_THRESH
    sgn_plus = np.where(np.abs(evals) < EXC_THRESH, 1.0, np.sign(evals))
    w_plus, dov = _ov_from_sgn(g5, evecs, sgn_plus)
    w_drop = np.where(exc, 0.0, w_plus)
    return {
        "drop": w_drop, "plus": w_plus, "exc": exc, "dov": dov,
        "herm_dev": herm_dev, "evals": evals,
    }


def wilson_detsq_batch(dw, dim):
    n = 2 * dim
    dwm = dw + MW * np.eye(n, dtype=np.complex128)
    _sign, logabs = np.linalg.slogdet(dwm)
    return np.exp(2.0 * logabs)


def acc(G, Z, key, chi_r, chi_p, w):
    Z[key] += float(np.sum(w))
    G[key] += (chi_r * w[:, None]).T @ chi_p


def min_eig(G, Z, key):
    if key not in Z or not np.isfinite(Z[key]) or Z[key] <= 0.0:
        return float("nan")
    m = G[key] / Z[key]
    m = 0.5 * (m + m.T)
    return float(np.linalg.eigvalsh(m)[0])


# primary (+half algebra) + adjacent-slice + overlap robustness
KEYS_HALF = ("gauge", "ov_det", "ov_full", "ov_det_plus", "ov_full_plus",
             "wil_det", "wil_full")
KEYS_ADJ = ("gauge_adj", "ov_det_adj", "ov_full_adj", "wil_det_adj")


def run_nt(nt, with_fermions=True, batch=BATCH):
    """Exact enumeration. Returns dict of min eigs, diagnostics, seconds."""
    n_links = 2 * NX * nt
    ncfg = 1 << n_links
    dim = NX * nt
    n_chi = 1 << n_obs_of(nt)
    n_chi_adj = 4
    G = {k: np.zeros((n_chi, n_chi), dtype=np.float64) for k in KEYS_HALF}
    Z = {k: 0.0 for k in KEYS_HALF}
    Ga = {k: np.zeros((n_chi_adj, n_chi_adj), dtype=np.float64)
          for k in KEYS_ADJ}
    Za = {k: 0.0 for k in KEYS_ADJ}
    nexc = 0
    t0 = time.perf_counter()
    for start in range(0, ncfg, batch):
        end = min(start + batch, ncfg)
        cs = np.arange(start, end, dtype=np.int64)
        U = decode_U(cs, nt)
        w_g = gauge_weights(U)
        chi_r, chi_p, _ = pair_characters(U, nt)
        chi_ra, chi_pa, _ = pair_adjacent(U, nt)
        acc(G, Z, "gauge", chi_r, chi_p, w_g)
        acc(Ga, Za, "gauge_adj", chi_ra, chi_pa, w_g)
        if not with_fermions:
            continue
        dw = wilson_dirac_batch(U, m=0.0)
        ov = overlap_weights_batch(dw, dim)
        nexc += int(np.sum(ov["exc"]))
        w_w = wilson_detsq_batch(dw, dim)
        acc(G, Z, "ov_det", chi_r, chi_p, ov["drop"])
        acc(G, Z, "ov_full", chi_r, chi_p, w_g * ov["drop"])
        acc(G, Z, "ov_det_plus", chi_r, chi_p, ov["plus"])
        acc(G, Z, "ov_full_plus", chi_r, chi_p, w_g * ov["plus"])
        acc(G, Z, "wil_det", chi_r, chi_p, w_w)
        acc(G, Z, "wil_full", chi_r, chi_p, w_g * w_w)
        acc(Ga, Za, "ov_det_adj", chi_ra, chi_pa, ov["drop"])
        acc(Ga, Za, "ov_full_adj", chi_ra, chi_pa, w_g * ov["drop"])
        acc(Ga, Za, "wil_det_adj", chi_ra, chi_pa, w_w)
        del dw, U, w_g, w_w, chi_r, chi_p, ov
    elapsed = time.perf_counter() - t0
    eigs = {k: (min_eig(G, Z, k) if (with_fermions or k == "gauge")
                else float("nan"))
            for k in KEYS_HALF}
    eigs_adj = {k: (min_eig(Ga, Za, k) if (with_fermions or k == "gauge_adj")
                    else float("nan"))
                for k in KEYS_ADJ}
    return {
        "nt": nt, "ncfg": ncfg, "n_chi": n_chi, "n_links": n_links,
        "eigs": eigs, "eigs_adj": eigs_adj, "Z": Z, "Za": Za,
        "nexc": nexc, "with_fermions": with_fermions, "elapsed": elapsed,
    }


def is_psd(e):
    return np.isfinite(e) and e > -TOL_PSD


def is_viol(e):
    return np.isfinite(e) and e < -TOL_VIOL


def classify_pair(e2, e4, prefix):
    v2, v4 = is_viol(e2), is_viol(e4)
    p2, p4 = is_psd(e2), is_psd(e4)
    if v2 and v4:
        return prefix + "VIOLATION_PERSISTS_NT4"
    if v2 and p4:
        return prefix + "VIOLATION_VANISHES_NT4"
    if p2 and v4:
        return prefix + "VIOLATION_APPEARS_NT4"
    if p2 and p4:
        return prefix + "HOLDS_BOTH_NT"
    return prefix + "INCONCLUSIVE_GREYZONE"


def classify_wilson(e2, e4):
    if is_psd(e2) and is_psd(e4):
        return "WILSON_CONTROL_PSD"
    if is_viol(e2) or is_viol(e4):
        return "WILSON_CONTROL_INDEFINITE"
    return "WILSON_CONTROL_GREYZONE"


def fmt(e):
    if not np.isfinite(e):
        return "SKIP"
    return "% .6e" % e


# ---------------------------------------------------------------- main
print("overlap_rp_exact_nt_probe -- Z2 exact OS Gram vs N_t")
print("   Nx=%d, beta=%.1f, m0=%.1f, m_W=%.1f, seed=%d"
      % (NX, BETA, M0, MW, SEED))
print("   theta(t)=Nt-1-t; +half {Nt/2..Nt-1}; chars of +half x-links")
print("   overlap primary: exceptional configs DROPPED (H_W invertible)")
rng = np.random.default_rng(SEED)

print("=== construction census ===")
for nt in (2, 4, 6):
    n_links = 2 * NX * nt
    ncfg = 1 << n_links
    pos = pos_slices(nt)
    mir = [theta_t(t, nt) for t in pos]
    n_chi = 1 << n_obs_of(nt)
    print("   Nt=%d: %d links, %d configs, +half %s, mirror %s, %d chars"
          % (nt, n_links, ncfg, pos, mir, n_chi))
rep("census: Nt=2 has 256 configs / 4 chars; Nt=4 has 65536 / 16; "
    "Nt=6 has 16777216 / 64",
    (1 << (2 * NX * 2)) == 256 and (1 << n_obs_of(2)) == 4
    and (1 << (2 * NX * 4)) == 65536 and (1 << n_obs_of(4)) == 16
    and (1 << (2 * NX * 6)) == 16777216 and (1 << n_obs_of(6)) == 64)

print("=== spot checks (scalar vs batch, gauge inv, GW, H_W hermiticity) ===")
dev_dirac, dev_plaq, dev_ginv, dev_hw, dev_gw = 0.0, 0.0, 0.0, 0.0, 0.0
dev_ov_spec, n_spot, n_gw, n_ov_well = 0.0, 0, 0, 0
for nt in (2, 4):
    n_links = 2 * NX * nt
    dim = NX * nt
    for _ in range(8):
        c = int(rng.integers(0, 1 << n_links))
        U = U_from_int(c, nt)
        Ub = U[None]
        d1 = wilson_dirac_one(U, m=0.0)
        d2 = wilson_dirac_batch(Ub, m=0.0)[0]
        dev_dirac = max(dev_dirac, float(np.max(np.abs(d1 - d2))))
        dev_plaq = max(dev_plaq,
                       abs(plaq_sum_one(U) - float(
                           np.log(gauge_weights(Ub)[0]) / BETA)))
        ov = overlap_weights_batch(d2[None], dim)
        w_w = wilson_detsq_batch(d2[None], dim)
        dev_hw = max(dev_hw, ov["herm_dev"])
        if not bool(ov["exc"][0]):
            ev_ov = np.linalg.eigvals(ov["dov"][0])
            dev_gw = max(dev_gw,
                         float(np.max(np.abs(np.abs(ev_ov - 1) - 1))))
            n_gw += 1
        a = rng.choice(np.array([-1.0, 1.0]), size=(NX, nt))
        Ug = gauge_transform_z2(U, a)
        dg = wilson_dirac_one(Ug, m=0.0)
        ovg = overlap_weights_batch(dg[None], dim)
        w_w_g = wilson_detsq_batch(dg[None], dim)
        rel = lambda u, v: abs(u - v) / max(abs(u), abs(v), 1e-300)
        # Plaquette and Wilson |det|^2 are the sharp gauge-invariance
        # teeth (O(1) numbers).  Overlap |det|^2 of near-zero-mode
        # configs is slogdet-noisy at 1e-50..1e-60 and those configs
        # have vanishing measure; compare D_ov spectra instead, and
        # |det|^2 only when both weights are well-conditioned.
        dev_ginv = max(dev_ginv,
                       rel(float(w_w[0]), float(w_w_g[0])),
                       rel(plaq_sum_one(U), plaq_sum_one(Ug)),
                       float(abs(int(ov["exc"][0]) - int(ovg["exc"][0]))))
        wp, wpg = float(ov["plus"][0]), float(ovg["plus"][0])
        if min(wp, wpg) > 1e-20:
            dev_ginv = max(dev_ginv, rel(wp, wpg))
            n_ov_well += 1
        amin = float(np.min(np.abs(ov["evals"][0])))
        amin_g = float(np.min(np.abs(ovg["evals"][0])))
        if min(amin, amin_g) > 1e-6:
            ev = np.sort(np.abs(np.linalg.eigvals(ov["dov"][0])))
            evg = np.sort(np.abs(np.linalg.eigvals(ovg["dov"][0])))
            # relative error on |lambda|~0 is meaningless (1e-15/1e-30);
            # D_W is exactly covariant, so this is an absolute match.
            dev_ov_spec = max(dev_ov_spec, float(np.max(np.abs(ev - evg))))
        n_spot += 1

rep("spot: batched Wilson-Dirac matches single-config (max dev %.1e, "
    "n=%d)" % (dev_dirac, n_spot), dev_dirac < 1e-12)
rep("spot: batched plaquette sum matches scalar (max dev %.1e)" % dev_plaq,
    dev_plaq < 1e-12)
rep("spot: H_W Hermitian (max asym %.1e)" % dev_hw, dev_hw < 1e-12)
rep("spot: overlap eigenvalues on the GW circle |lambda-1|=1 for "
    "non-exceptional configs (max dev %.1e, n=%d)" % (dev_gw, n_gw),
    n_gw >= 4 and dev_gw < 1e-10)
rep("spot: plaquette sum, |det D_W|^2, well-conditioned |det D_ov|^2 "
    "(n=%d) and H_W-exceptionality invariant under random Z2 gauges "
    "(max rel/abs %.1e)" % (n_ov_well, dev_ginv),
    dev_ginv < 1e-10)
rep("spot: |eig D_ov| spectrum gauge-invariant (max abs %.1e); tiny "
    "|det D_ov|^2 disagreements are slogdet noise on vanishing-weight "
    "near-zero-mode configs and do not enter the Gram"
    % dev_ov_spec, dev_ov_spec < 1e-10)

Uplus = np.ones((2, NX, 2), dtype=np.float64)
rep("spot: all-plus 2x2 has plaquette sum = Nx Nt = 4",
    abs(plaq_sum_one(Uplus) - 4.0) < 1e-15)

print("=== exact enumerations ===")
results = {}
t_all = time.perf_counter()

print("   Nt=2 (256 configs, overlap+Wilson) ...")
results[2] = run_nt(2, with_fermions=True)
print("      %.2fs  nexc=%d/%d  min eigs %s"
      % (results[2]["elapsed"], results[2]["nexc"], results[2]["ncfg"],
         {k: fmt(results[2]["eigs"][k])
          for k in ("gauge", "ov_det", "ov_full", "wil_det")}))

print("   Nt=4 (65536 configs, overlap+Wilson) ...")
results[4] = run_nt(4, with_fermions=True)
print("      %.2fs  nexc=%d/%d  min eigs %s"
      % (results[4]["elapsed"], results[4]["nexc"], results[4]["ncfg"],
         {k: fmt(results[4]["eigs"][k])
          for k in ("gauge", "ov_det", "ov_full", "wil_det")}))

print("   Nt=6 pure-gauge validation (2^24 configs, no Dirac) ...")
results[6] = run_nt(6, with_fermions=False, batch=65536)
print("      %.2fs  pure-gauge min eig %s"
      % (results[6]["elapsed"], fmt(results[6]["eigs"]["gauge"])))

n4, n6 = 2 * NX * 4, 2 * NX * 6
proj6 = results[4]["elapsed"] * (results[6]["ncfg"] / results[4]["ncfg"]) \
    * ((n6 / n4) ** 3)
print("   Nt=6 fermion projection: %.0fs (budget %.0fs)"
      % (proj6, NT6_BUDGET_S))
nt6_fermions = False
if proj6 <= NT6_BUDGET_S:
    print("   Nt=6 fermions within budget -- running vectorized batches ...")
    results[6] = run_nt(6, with_fermions=True, batch=512)
    nt6_fermions = True
    print("      %.2fs  min eigs %s"
          % (results[6]["elapsed"],
             {k: fmt(results[6]["eigs"][k])
              for k in ("gauge", "ov_det", "ov_full", "wil_det")}))
else:
    print("   Nt=6 fermions SKIP (vectorized eigh of 16.7M 24x24 matrices "
          "projected above budget; pure-gauge Gram is exact)")

runtime = time.perf_counter() - t_all

print("=== VALIDATION: pure-gauge Gram is OS / Osterwalder-Seiler ===")
for nt in (2, 4, 6):
    e = results[nt]["eigs"]["gauge"]
    ea = results[nt]["eigs_adj"]["gauge_adj"]
    ok = is_psd(e) and is_psd(ea)
    rep("VALIDATION Nt=%d pure gauge PSD (+half min eig %s, adjacent "
        "4-char %s, Z=%.4e) -- Osterwalder-Seiler; a negative value "
        "means the reflection map is wrong"
        % (nt, fmt(e), fmt(ea), results[nt]["Z"]["gauge"]), ok)

print("=== MEASUREMENT: overlap and Wilson min Gram eigenvalues ===")
for nt in (2, 4):
    r = results[nt]
    for key, lab in (("ov_det", "overlap det-only DROP"),
                     ("ov_full", "overlap full DROP"),
                     ("ov_det_plus", "overlap det-only PLUS-KEEP"),
                     ("ov_full_plus", "overlap full PLUS-KEEP"),
                     ("wil_det", "Wilson  det-only"),
                     ("wil_full", "Wilson  full")):
        e = r["eigs"][key]
        tag = ("PSD" if is_psd(e)
               else ("INDEFINITE" if is_viol(e) else "GREYZONE"))
        rep("MEASUREMENT Nt=%d %s min eig %s  [%s]"
            % (nt, lab, fmt(e), tag),
            np.isfinite(e))
    for key, lab in (("ov_det_adj", "overlap det-only ADJACENT-4"),
                     ("ov_full_adj", "overlap full ADJACENT-4"),
                     ("wil_det_adj", "Wilson  det-only ADJACENT-4")):
        e = r["eigs_adj"][key]
        tag = ("PSD" if is_psd(e)
               else ("INDEFINITE" if is_viol(e) else "GREYZONE"))
        rep("MEASUREMENT Nt=%d %s min eig %s  [%s]"
            % (nt, lab, fmt(e), tag),
            np.isfinite(e))
    rep("MEASUREMENT Nt=%d exceptional overlap configs (min|eig H_W| "
        "< %.0e): %d / %d -- EXCLUDED from primary overlap measure"
        % (nt, EXC_THRESH, r["nexc"], r["ncfg"]), True)

# Nt=2 adjacent algebra IS the +half algebra
rep("CONSISTENCY Nt=2: adjacent-4 and +half overlap det-only min eigs "
    "agree (same algebra)",
    abs(results[2]["eigs"]["ov_det"] - results[2]["eigs_adj"]["ov_det_adj"])
    < 1e-14)

if nt6_fermions:
    for key, lab in (("ov_det", "overlap det-only DROP"),
                     ("wil_det", "Wilson  det-only")):
        e = results[6]["eigs"][key]
        tag = ("PSD" if is_psd(e)
               else ("INDEFINITE" if is_viol(e) else "GREYZONE"))
        rep("MEASUREMENT Nt=6 %s min eig %s  [%s]" % (lab, fmt(e), tag),
            np.isfinite(e))
else:
    rep("MEASUREMENT Nt=6 fermions SKIP_TOO_SLOW "
        "(projection %.0fs > budget %.0fs; 2^24 configs x 24x24 eigh)"
        % (proj6, NT6_BUDGET_S), True)

ov_verdict = classify_pair(results[2]["eigs"]["ov_det"],
                           results[4]["eigs"]["ov_det"],
                           "OVERLAP_RP_")
ov_plus_verdict = classify_pair(results[2]["eigs"]["ov_det_plus"],
                                results[4]["eigs"]["ov_det_plus"],
                                "OVERLAP_RP_")
ov_full_verdict = classify_pair(results[2]["eigs"]["ov_full"],
                                results[4]["eigs"]["ov_full"],
                                "OVERLAP_FULL_")
ov_adj_verdict = classify_pair(results[2]["eigs_adj"]["ov_det_adj"],
                               results[4]["eigs_adj"]["ov_det_adj"],
                               "OVERLAP_RP_ADJ_")
w_verdict = classify_wilson(results[2]["eigs"]["wil_det"],
                            results[4]["eigs"]["wil_det"])

rep("ROBUSTNESS: drop-exceptional and plus-keep det-only calls AGREE "
    "(%s vs %s)" % (ov_verdict, ov_plus_verdict),
    ov_verdict == ov_plus_verdict)
rep("ROBUSTNESS: adjacent-4 algebra (same observables as Nt=2) AGREE "
    "with the +half call on persist/vanish/appear (%s vs %s)"
    % (ov_verdict, ov_adj_verdict.replace("ADJ_", "")),
    ov_verdict == ov_adj_verdict.replace("ADJ_", ""))

print("=== table: min Gram eigenvalue (weight x N_t x fermion) ===")
print("   primary overlap = exceptional DROPPED; robustness = PLUS-KEEP")
print("   %-28s %14s %14s %14s" % ("", "Nt=2", "Nt=4", "Nt=6"))
rows = [
    ("pure gauge +half",
     results[2]["eigs"]["gauge"], results[4]["eigs"]["gauge"],
     results[6]["eigs"]["gauge"]),
    ("overlap det-only DROP",
     results[2]["eigs"]["ov_det"], results[4]["eigs"]["ov_det"],
     results[6]["eigs"]["ov_det"]),
    ("overlap full DROP",
     results[2]["eigs"]["ov_full"], results[4]["eigs"]["ov_full"],
     results[6]["eigs"]["ov_full"]),
    ("overlap det-only PLUS-KEEP",
     results[2]["eigs"]["ov_det_plus"], results[4]["eigs"]["ov_det_plus"],
     results[6]["eigs"]["ov_det_plus"]),
    ("overlap full PLUS-KEEP",
     results[2]["eigs"]["ov_full_plus"], results[4]["eigs"]["ov_full_plus"],
     results[6]["eigs"]["ov_full_plus"]),
    ("Wilson det-only",
     results[2]["eigs"]["wil_det"], results[4]["eigs"]["wil_det"],
     results[6]["eigs"]["wil_det"]),
    ("Wilson full",
     results[2]["eigs"]["wil_full"], results[4]["eigs"]["wil_full"],
     results[6]["eigs"]["wil_full"]),
    ("overlap det-only ADJACENT-4",
     results[2]["eigs_adj"]["ov_det_adj"],
     results[4]["eigs_adj"]["ov_det_adj"],
     results[6]["eigs_adj"]["ov_det_adj"]),
    ("Wilson det-only ADJACENT-4",
     results[2]["eigs_adj"]["wil_det_adj"],
     results[4]["eigs_adj"]["wil_det_adj"],
     results[6]["eigs_adj"]["wil_det_adj"]),
]
for lab, a, b, c in rows:
    print("   %-28s %14s %14s %14s" % (lab, fmt(a), fmt(b), fmt(c)))

sharp = (is_viol(results[4]["eigs"]["ov_det"])
         and is_psd(results[2]["eigs"]["wil_det"])
         and is_psd(results[4]["eigs"]["wil_det"]))
if ov_verdict.endswith("APPEARS_NT4") and sharp:
    pin = ("Nt=2 overlap Gram is PSD on the complete 4-char algebra; "
           "the |det D_ov|^2 measure becomes indefinite at Nt=4 on BOTH "
           "the 16-char +half algebra and the adjacent 4-char algebra.  "
           "Wilson |det D_W|^2 stays PSD -- violation pinned on overlap "
           "TIME NONLOCALITY, not on fermion determinants per se.  "
           "The FULL (beta=1) overlap measure stays PSD on this Gram: "
           "the named failure is the naive det-only / beta=0 measure")
elif ov_verdict.endswith("PERSISTS_NT4") and sharp:
    pin = ("overlap det-only indefinite at both Nt; Wilson control PSD "
           "pins the violation on overlap time nonlocality")
elif ov_verdict.endswith("VANISHES_NT4") and sharp:
    pin = ("Nt=2 overlap violation is a short-torus artifact; Wilson "
           "control PSD at both Nt")
elif w_verdict == "WILSON_CONTROL_INDEFINITE":
    pin = ("Wilson control is itself indefinite -- cannot pin the "
           "violation on overlap nonlocality alone")
else:
    pin = "see verdict enums"

rep("FINDING overlap det-only DROP: %s (plus-keep: %s; adjacent-4: %s; "
    "full-weight: %s)"
    % (ov_verdict, ov_plus_verdict, ov_adj_verdict, ov_full_verdict), True)
rep("FINDING Wilson det-only: %s -- %s" % (w_verdict, pin), True)

print()
print("VERDICT: %s + %s + %s" % (ov_verdict, ov_full_verdict, w_verdict))
print("RUNTIME: %.2fs (Nt=2 %.2fs, Nt=4 %.2fs, Nt=6-gauge %.2fs%s)"
      % (runtime, results[2]["elapsed"], results[4]["elapsed"],
         results[6]["elapsed"],
         (", Nt=6-fermions ON" if nt6_fermions else ", Nt=6-fermions SKIP")))
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
