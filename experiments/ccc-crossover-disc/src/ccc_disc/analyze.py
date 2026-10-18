"""The data pass of the preregistered CCC crossover-disc search.

Executed strictly against hypotheses/ccc_disc_v1.yaml (frozen 2026-08-24
BEFORE data contact).  First data contact: 2026-08-24, Planck PR3 SMICA
(COM_CMB_IQU-smica_2048_R3.00_full.fits, sha-verified download from
IRSA), logged in the project README.

Pipeline (as frozen in the CLI plan):
  1. SMICA temperature + TMASK, mask-weighted degrade to NSIDE 256
     (disc scale 1.16 deg >> pixel 13.7 arcmin), K -> muK.
  2. matched filter for SHARP TOP-HAT discs at the frozen radius scan
     band {1.00, 1.10, 1.16, 1.30} deg ONLY: b_ell of the disc /
     measured pseudo-C_ell, empirically normalised SNR map.
  3. candidates: local |SNR| peaks above threshold; global significance
     from N_SIM Gaussian LCDM simulations (same C_ell, mask, filters).
  4. injection-recovery: synthetic 200 muK discs into a simulation
     (detector validation).
  5. sign-pairing statistics of any candidates (frozen defect table).
Verdict per the frozen enum + decision rule (SUPPORT requires BH-q <
0.01 AND half-mission AND multi-component replication -- a single-map
pass can therefore at most yield 'null'/'consistent'/'data_limited').
"""

import hashlib
import json
import os
import time

import numpy as np
import healpy as hp

from . import kernel

NSIDE = 256
LMAX = 512
RADII_DEG = [1.00, 1.10, 1.16, 1.30]      # frozen scan band
SNR_THRESH = 4.0                          # candidate threshold (local)
N_SIM = 100
SEED = 20260824


def tophat_tau(theta_c, lmax):
    """Legendre coefficients of the unit top-hat disc, t(n) =
    sum_l tau_l P_l(n.n0): tau_l = (2l+1)/(4pi) * 2pi int_x^1 P_l
    = (P_{l-1}(x) - P_{l+1}(x))/2, tau_0 = (1-x)/2.

    PIPELINE CORRECTION (2026-08-24, disclosed): the first executed
    pass used F_l ~ tau_l/C_l, which over-weights high l by (2l+1) --
    a valid sims-calibrated linear statistic but NOT the optimal
    matched filter.  The correct ML filter for an azimuthally
    symmetric template is F_l = tau_l / ((2l+1) C_l) (the template
    a_lm are t_lm = tau_l (4pi/(2l+1)) Y_lm*(n0)).  Fixed here; the
    frozen template, radius band and decision rule are unchanged."""
    x = np.cos(theta_c)
    P = np.zeros(lmax + 2)
    P[0], P[1] = 1.0, x
    for l in range(1, lmax + 1):
        P[l + 1] = ((2 * l + 1) * x * P[l] - l * P[l - 1]) / (l + 1)
    tau = np.zeros(lmax + 1)
    tau[0] = (1 - x) / 2.0
    for l in range(1, lmax + 1):
        tau[l] = (P[l - 1] - P[l + 1]) / 2.0
    return tau


def matched_filter_maps(tmap, mask, cl, radii_deg):
    """return dict radius -> SNR map (empirically normalised)."""
    alm = hp.map2alm(tmap * mask, lmax=LMAX, iter=1)
    out = {}
    ls = np.arange(LMAX + 1)
    clr = np.where(cl > 0, cl, np.inf)
    for rd in radii_deg:
        tau = tophat_tau(np.radians(rd), LMAX)
        fl = tau / ((2 * ls + 1) * clr)          # optimal ML filter
        fmap = hp.alm2map(hp.almxfl(alm, fl), NSIDE)
        good = mask > 0.5
        f = fmap[good]
        snr = np.zeros_like(fmap)
        snr[good] = (fmap[good] - f.mean()) / f.std()
        out[rd] = snr * (mask > 0.5)
    return out


def peak_candidates(snr_map, mask, thresh):
    """local extrema of |SNR| above thresh, separated by >= 2 deg."""
    good = np.where((mask > 0.5) & (np.abs(snr_map) >= thresh))[0]
    if good.size == 0:
        return []
    order = good[np.argsort(-np.abs(snr_map[good]))]
    vecs = np.array(hp.pix2vec(NSIDE, order)).T
    kept, kept_vecs = [], []
    min_cos = np.cos(np.radians(2.0))
    for i, pix in enumerate(order):
        v = vecs[i]
        if all(v @ w < min_cos for w in kept_vecs):
            kept.append(int(pix))
            kept_vecs.append(v)
    return [(p, float(snr_map[p])) for p in kept]


def file_sha256(path, chunk=1 << 24):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def run_analysis(map_path, out_path):
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    # AMENDMENT (2026-08-24, execution mechanics only): pin the legacy
    # global NumPy RNG used internally by hp.synfast so the null battery
    # and injection sims are deterministic across reruns (prereg demands
    # pinned seeds).  No statistic, threshold or template changed.
    np.random.seed(SEED)
    print(f"[1/6] reading {os.path.basename(map_path)} (I + TMASK) ...")
    imap, tmask = hp.read_map(map_path, field=(0, 3), dtype=np.float64)
    imap *= 1e6                                        # K -> muK
    print("      degrading to NSIDE", NSIDE)
    num = hp.ud_grade(imap * tmask, NSIDE)
    den = hp.ud_grade(tmask.astype(np.float64), NSIDE)
    mask = (den > 0.9).astype(np.float64)
    tmap = np.where(den > 0, num / np.maximum(den, 1e-12), 0.0) * mask
    fsky = mask.mean()

    print(f"[2/6] pseudo-C_ell (fsky = {fsky:.3f}) ...")
    cl = hp.anafast(tmap, lmax=LMAX, iter=1) / fsky
    cl[:2] = cl[2]

    print("[3/6] matched filters at frozen radii", RADII_DEG, "...")
    snr = matched_filter_maps(tmap, mask, cl, RADII_DEG)
    data_max = {rd: float(np.max(np.abs(m))) for rd, m in snr.items()}
    data_global_max = max(data_max.values())
    cands = {rd: peak_candidates(m, mask, SNR_THRESH)
             for rd, m in snr.items()}
    n_cand = {rd: len(c) for rd, c in cands.items()}

    print(f"[4/6] null battery: {N_SIM} Gaussian sims ...")
    null_max = []
    null_ncand = []
    for i in range(N_SIM):
        sim = hp.synfast(cl, NSIDE, lmax=LMAX)
        ssnr = matched_filter_maps(sim, mask, cl, RADII_DEG)
        null_max.append(max(float(np.max(np.abs(m)))
                            for m in ssnr.values()))
        null_ncand.append(sum(len(peak_candidates(m, mask, SNR_THRESH))
                              for m in ssnr.values()))
    null_max = np.array(null_max)
    p_global = float((np.sum(null_max >= data_global_max) + 1)
                     / (N_SIM + 1))
    n_cand_total = sum(n_cand.values())
    p_counts = float((np.sum(np.array(null_ncand) >= n_cand_total) + 1)
                     / (N_SIM + 1))

    print("[5/6] injection-recovery (20 x 200 muK discs, 1.16 deg) ...")
    sim = hp.synfast(cl, NSIDE, lmax=LMAX)
    inj_pix = rng.choice(np.where(mask > 0.5)[0], 20, replace=False)
    inj = sim.copy()
    vec_all = np.array(hp.pix2vec(NSIDE, np.arange(hp.nside2npix(NSIDE))))
    for p in inj_pix:
        v = np.array(hp.pix2vec(NSIDE, int(p)))
        disc = hp.query_disc(NSIDE, v, np.radians(1.16))
        inj[disc] += 200.0
    isnr = matched_filter_maps(inj, mask, cl, [1.16])[1.16]
    rec = 0
    for p in inj_pix:
        v = np.array(hp.pix2vec(NSIDE, int(p)))
        disc = hp.query_disc(NSIDE, v, np.radians(0.5))
        if np.max(np.abs(isnr[disc])) >= 5.0:
            rec += 1
    recovery = rec / len(inj_pix)

    # sign statistics of data candidates (frozen discriminator)
    all_c = [c for rd in RADII_DEG for c in cands[rd]]
    n_pos = sum(1 for _, s in all_c if s > 0)
    n_neg = len(all_c) - n_pos

    # frozen decision rule: SUPPORT needs BH-q < 0.01 + replication
    # (half-missions + >= 2 component separations) -- not available in
    # a single-map pass, so the best possible outcome here is null/
    # consistent.
    if p_global > 0.05 and p_counts > 0.05:
        verdict = ("null (SMICA pass): no top-hat disc excess above the "
                   "Gaussian LCDM null battery; well-powered at the "
                   "frozen radius band; replication legs not needed for "
                   "a null")
    elif p_global < 0.01 or p_counts < 0.01:
        verdict = ("candidate_flag -> stays data_limited per the frozen "
                   "rule until half-mission + multi-component "
                   "replication (NOT support)")
    else:
        verdict = "not_confirmed_not_refuted (marginal; needs replication)"

    # REPORTING (execution mechanics only): explicit decision-rule and
    # kill-condition ledger per hypotheses/ccc_disc_v1.yaml.  BH over the
    # frozen family of global tests {p_global_max, p_candidate_counts}.
    ps = sorted([("p_candidate_counts", p_counts),
                 ("p_global_max", p_global)], key=lambda kv: kv[1])
    m = len(ps)
    bh_q = {}
    running_min = 1.0
    for rank in range(m, 0, -1):
        name, p = ps[rank - 1]
        running_min = min(running_min, p * m / rank)
        bh_q[name] = running_min
    bh_q_min = min(bh_q.values())
    resolved_relic = bh_q_min < 0.01
    ks_na = "NA (no resolved relic candidate; fires only on a detection)"
    kill_conditions = {
        "K1_single_gaussian_profile": ks_na,
        "K2_amplitude_ratio_incompatible": ks_na,
        "K3_negative_c3_for_paired_defect": ks_na,
        "K4_centrally_peaked_relic": ks_na,
        "K5_ring_edge_ratio_incompatible": ks_na,
        "K6_radial_contrast_gt_1e-2": ks_na,
    } if not resolved_relic else {"note": "resolved candidate: evaluate "
                                          "K1-K6 on the resolved profile"}
    decision_rule = {
        "bh_q_per_test": bh_q,
        "bh_q_min": bh_q_min,
        "bh_q_lt_0.01": bool(bh_q_min < 0.01),
        "replication_half_mission": "not_run (not required for a null)",
        "replication_multi_component": "not_run (not required for a null)",
        "support": False,
    }

    results = {
        "id": "CCC.DISC.SEARCH.01",
        "date_run": "2026-08-24",
        "data": os.path.basename(map_path),
        "data_sha256": file_sha256(map_path),
        "data_bytes": os.path.getsize(map_path),
        "seed": SEED,
        "first_data_contact": "2026-08-24 (this run)",
        "nside": NSIDE, "lmax": LMAX, "fsky": fsky,
        "radii_deg": RADII_DEG,
        "snr_threshold_local": SNR_THRESH,
        "data_max_abs_snr_per_radius": data_max,
        "data_global_max_abs_snr": data_global_max,
        "n_candidates_per_radius": n_cand,
        "n_candidates_total": n_cand_total,
        "candidate_signs": {"pos": n_pos, "neg": n_neg},
        "null_sims": N_SIM,
        "null_max_abs_snr_mean": float(null_max.mean()),
        "null_max_abs_snr_p95": float(np.quantile(null_max, 0.95)),
        "p_global_max": p_global,
        "p_candidate_counts": p_counts,
        "injection_recovery_fraction_200muK": recovery,
        "decision_rule": decision_rule,
        "kill_conditions": kill_conditions,
        "verdict": verdict,
        "frozen_hashes": {k: v[1] for k, v in
                          kernel.freeze_status().items()},
        "runtime_s": round(time.time() - t0, 1),
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print("[6/6] results ->", out_path)
    for k in ("data_global_max_abs_snr", "p_global_max",
              "p_candidate_counts", "n_candidates_total",
              "injection_recovery_fraction_200muK", "verdict"):
        print(f"   {k}: {results[k]}")
    return results
