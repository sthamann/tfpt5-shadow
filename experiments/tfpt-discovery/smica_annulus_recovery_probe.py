#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""smica_annulus_recovery_probe -- OBS.ANNULUS.RECOVERY.01 (exploratory)
(signature-bundle round 2026-08-27): FIRST exploratory implementation of
the Markov/annulus-recovery signature (#7 of the external bundle) on
the LOCALLY PRESENT Planck PR3 SMICA temperature map: Gaussian
conditional mutual information I(A : C | B) between an inner cap A and
an outer annulus C conditioned on a buffer annulus B, scanned over the
buffer width, confronted with (i) a single-rate decay and (ii) a
two-rate decay at the FROZEN kernel ratio Delta_-/Delta_+ = 2.709511
(ccc freeze v1, SHA 1df51166d0a2ef5b, frozen 2026-08-24 BEFORE any CMB
data contact), against a Gaussian null battery with the same C_ell.

HONEST SCOPE (read first):
  * EXPLORATORY, not preregistered YAML-grade: the pipeline below is
    frozen IN-CODE before the data load of THIS probe, but the map was
    already contacted 2026-08-24 (ccc-crossover-disc, logged there).
  * A generic Markov-like decay of I(A:C|B) is NOT TFPT-specific (any
    quasi-Gaussian field with smooth C_ell gives one); the ONLY
    TFPT-specific target is a TWO-rate structure at the frozen ratio
    ABOVE the Gaussian null.  A null here is a well-powered honest
    outcome, damages nothing (the cyclic reading is [C]).
  * Per doubletone_character_transduction_probe the temperature channel
    is parity-even: under the FAITHFUL bridge the even-sector rates are
    {Delta_-, 2 Delta_-, 2 Delta_+} -- the ratio of the two slowest
    even rates is 2 Delta_+ / Delta_- = 0.738 or Delta_-/... typed:
    the RAW frozen target stays the v1 ratio 2.709511 (rate pair
    (Delta_+, Delta_-)); the even-sector variant 2Delta_+/Delta_- is
    RECORDED as a secondary read-off, not a second trial.

FROZEN PIPELINE (before data load):
  map: field 0 (I_STOKES, K_CMB -> muK), field 3 (TMASK); NSIDE 128
  (ud_grade; mask threshold 0.9), lmax 383, alm iter 1.
  bands: ell in [2,64], [65,128], [129,256], [257,383] (4 features).
  centers: NSIDE=4 pixel centers with |b| >= 30 deg and >= 95 %
  coverage of the 5.5-deg envelope; regions per center:
  A = cap(1.0 deg), B = annulus [1.0, 1.0+w], C = [1.0+w, 2.5+w] deg,
  w in {0.5, 1.0, 1.5, 2.0, 2.5, 3.0} deg.
  features: mask-weighted band means per region (z-scored across
  centers); statistic: Gaussian CMI from the center-sample covariance.
  fits in w: F1 log-linear single rate (2 par); F2 two-exponential
  with RATE RATIO FIXED at 2.709511 (3 par); F3 free-ratio (4 par,
  record only).  sigma(w) from the null spread.
  nulls: 60 synfast skies from the masked pseudo-C_ell/fsky, seed
  20260827, identical pipeline.
  DECISION (frozen): p_two = P_null(dchi2_F1->F2 >= data);
  verdict = hint iff p_two < 0.01 AND F3 ratio in [2.0, 3.5];
  else null (well-powered) / data_limited (pipeline degenerate).

KILLS: K-C1 self-test of the fitter fails (INSTRUMENT-DEAD); K-C2
data integrity (SHA-256 prefix 60952c64, NSIDE 2048) fails
(DATA-DEAD); K-C3 < 80 usable centers (COVERAGE-DEAD).

TYPING: search target of the [C] cyclic/recovery reading -- residual
boundary-recovery pattern, NOT direct Hawking emission, NOT new
gravity; no marker moves; promotion only via promote-to-verification.

FIREWALL: experiments/-Probe; schreibt results-JSON NUR nach
experiments/tfpt-discovery/ (smica_annulus_recovery_results.json);
kein verification/-, Paper-, Ledger-, Changelog- oder Website-Surface.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/smica_annulus_recovery_probe.py
"""

import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np

T0 = time.time()
CHECKS = []
KILLS = []

# ---------------------------- FROZEN CONSTANTS (before any data load)
MAP_PATH = (Path(__file__).resolve().parents[1] / "ccc-crossover-disc"
            / "data" / "COM_CMB_IQU-smica_2048_R3.00_full.fits")
SHA_PREFIX = "60952c64"                      # ccc data-contact log
NSIDE = 128
LMAX = 383
BANDS = [(2, 64), (65, 128), (129, 256), (257, 383)]
NSIDE_CENTERS = 4
B_MIN_DEG = 30.0
COVERAGE_MIN = 0.95
R_A_DEG = 1.0
W_LIST_DEG = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
C_WIDTH_DEG = 1.5
N_NULLS = 60
SEED = 20260827
RATIO_FROZEN = 2.709511                      # Delta_-/Delta_+ (ccc v1)
P_HINT = 0.01
RATIO_BAND = (2.0, 3.5)
MIN_CENTERS = 80


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ------------------------------------------------------------ fitting
def fit_single(w, y, sig):
    """log-linear single-exponential fit; returns (chi2, rate)."""
    ly = np.log(np.clip(y, 1e-300, None))
    A = np.vstack([np.ones_like(w), -w]).T
    wt = y / sig                              # d(ln y) approx dy/y
    coef, *_ = np.linalg.lstsq(A * wt[:, None], ly * wt, rcond=None)
    model = np.exp(A @ coef)
    chi2 = float(np.sum(((y - model) / sig) ** 2))
    return chi2, float(coef[1])


def fit_two(w, y, sig, ratio):
    """I = a1 e^{-r w} + a2 e^{-ratio r w}, grid+lsq over r; returns
    (chi2, r, a1, a2)."""
    best = (np.inf, np.nan, np.nan, np.nan)
    for r in np.geomspace(0.05, 10.0, 240):
        X = np.vstack([np.exp(-r * w), np.exp(-ratio * r * w)]).T
        Xw = X / sig[:, None]
        a, *_ = np.linalg.lstsq(Xw, y / sig, rcond=None)
        chi2 = float(np.sum((y / sig - Xw @ a) ** 2))
        if chi2 < best[0]:
            best = (chi2, float(r), float(a[0]), float(a[1]))
    return best


def fit_two_free(w, y, sig):
    """free-ratio two-exponential (record only); returns (chi2, ratio)."""
    best = (np.inf, np.nan)
    for ratio in np.geomspace(1.05, 12.0, 90):
        chi2, r, a1, a2 = fit_two(w, y, sig, ratio)
        if chi2 < best[0]:
            best = (chi2, float(ratio))
    return best


def cmi(xa, xc, xb):
    """Gaussian conditional mutual information I(A:C|B) from samples
    (rows = centers)."""
    def cond_cov(x, z):
        cxx = np.cov(x.T)
        czz = np.cov(z.T)
        cxz = (x - x.mean(0)).T @ (z - z.mean(0)) / (len(x) - 1)
        return cxx - cxz @ np.linalg.solve(czz, cxz.T)

    xac = np.hstack([xa, xc])
    sa = cond_cov(xa, xb)
    sc = cond_cov(xc, xb)
    sac = cond_cov(xac, xb)
    (_, lda) = np.linalg.slogdet(sa)
    (_, ldc) = np.linalg.slogdet(sc)
    (_, ldac) = np.linalg.slogdet(sac)
    return 0.5 * (lda + ldc - ldac)


# ------------------------------------------------------------- main
def main():
    import healpy as hp

    section("OBS.ANNULUS.RECOVERY.01 -- SMICA-Annulus-Recovery "
            "(exploratorisch, Kernel-Ratio 2.709511 gefroren)")

    # G0: instrument self-test (no sky): fitter must recover a known
    # two-rate curve and prefer F2 there, and NOT prefer F2 on a pure
    # single-rate curve.
    rng = np.random.default_rng(SEED)
    w = np.array(W_LIST_DEG)
    y_two = 1.0 * np.exp(-0.8 * w) + 0.6 * np.exp(-RATIO_FROZEN * 0.8 * w)
    y_one = 1.4 * np.exp(-1.1 * w)
    sig0 = 0.01 * np.ones_like(w)
    c1a, _ = fit_single(w, y_two, sig0)
    c2a, r_rec, _, _ = fit_two(w, y_two, sig0, RATIO_FROZEN)
    c1b, _ = fit_single(w, y_one, sig0)
    c2b, *_ = fit_two(w, y_one, sig0, RATIO_FROZEN)
    ok0 = check("G0 Selbsttest Fitter: Zwei-Raten-Kurve -> F2 gewinnt "
                "deutlich (dchi2 = %.1f), Rate 0.8 rekonstruiert "
                "(%.3f); Ein-Raten-Kurve -> kein falscher F2-Gewinn "
                "(dchi2 = %.2f)" % (c1a - c2a, r_rec, c1b - c2b),
                (c1a - c2a) > 5.0 and abs(r_rec - 0.8) < 0.05
                and (c1b - c2b) < 1.0, kill="INSTRUMENT-DEAD")
    if not ok0:
        return finish(None)

    # G1: data integrity (first data touch of THIS probe)
    h = hashlib.sha256()
    with open(MAP_PATH, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 24), b""):
            h.update(chunk)
    sha = h.hexdigest()
    ok1 = check("G1 Datenintegritaet: SHA-256 = %s... (Praefix %s), "
                "Groesse %.3f GB" % (sha[:16], SHA_PREFIX,
                                     MAP_PATH.stat().st_size / 1e9),
                sha.startswith(SHA_PREFIX), kill="DATA-DEAD")
    if not ok1:
        return finish(None)

    t_map, t_mask = hp.read_map(str(MAP_PATH), field=(0, 3),
                                dtype=np.float64)
    t_map = hp.ud_grade(t_map * 1e6, NSIDE)          # K -> muK
    mask = (hp.ud_grade(t_mask.astype(np.float64), NSIDE) > 0.9)
    fsky = float(mask.mean())
    print("  map @ NSIDE %d, fsky(TMASK>0.9) = %.3f" % (NSIDE, fsky))

    # centers + region pixel sets (frozen geometry)
    npix_c = hp.nside2npix(NSIDE_CENTERS)
    centers = []
    for p in range(npix_c):
        th, ph = hp.pix2ang(NSIDE_CENTERS, p)
        b_gal = 90.0 - math.degrees(th)
        if abs(b_gal) < B_MIN_DEG:
            continue
        vec = hp.ang2vec(th, ph)
        env = hp.query_disc(NSIDE, vec,
                            math.radians(R_A_DEG + max(W_LIST_DEG)
                                         + C_WIDTH_DEG + 1.0))
        if mask[env].mean() < COVERAGE_MIN:
            continue
        centers.append(vec)
    ok3 = check("G2 Zentren: %d nutzbare (|b| >= %.0f deg, Coverage "
                ">= %.2f)" % (len(centers), B_MIN_DEG, COVERAGE_MIN),
                len(centers) >= MIN_CENTERS, kill="COVERAGE-DEAD")
    if not ok3:
        return finish(None)

    regions = []          # per center: (A, per-w list of (B, C))
    for vec in centers:
        disc_a = hp.query_disc(NSIDE, vec, math.radians(R_A_DEG))
        per_w = []
        for wd in W_LIST_DEG:
            d_ab = hp.query_disc(NSIDE, vec, math.radians(R_A_DEG + wd))
            d_abc = hp.query_disc(
                NSIDE, vec, math.radians(R_A_DEG + wd + C_WIDTH_DEG))
            bpix = np.setdiff1d(d_ab, disc_a, assume_unique=True)
            cpix = np.setdiff1d(d_abc, d_ab, assume_unique=True)
            per_w.append((bpix[mask[bpix]], cpix[mask[cpix]]))
        regions.append((disc_a[mask[disc_a]], per_w))

    def band_maps(m):
        alm = hp.map2alm(m * mask, lmax=LMAX, iter=1)
        out = []
        for lo, hi in BANDS:
            fl = np.zeros(LMAX + 1)
            fl[lo:hi + 1] = 1.0
            out.append(hp.alm2map(hp.almxfl(alm, fl), NSIDE, verbose=False)
                       if "verbose" in hp.alm2map.__code__.co_varnames
                       else hp.alm2map(hp.almxfl(alm, fl), NSIDE))
        return out

    def cmi_curve(m):
        bm = band_maps(m)
        feats_a = np.array([[bmk[a].mean() for bmk in bm]
                            for a, _ in regions])
        curve = []
        for iw in range(len(W_LIST_DEG)):
            xb = np.array([[bmk[pw[iw][0]].mean() for bmk in bm]
                           for _, pw in regions])
            xc = np.array([[bmk[pw[iw][1]].mean() for bmk in bm]
                           for _, pw in regions])
            z = lambda x: (x - x.mean(0)) / x.std(0)
            curve.append(cmi(z(feats_a), z(xc), z(xb)))
        return np.array(curve)

    print("  computing data CMI curve ...", flush=True)
    i_data = cmi_curve(t_map)
    print("  I(A:C|B)(w) data =",
          np.array2string(i_data, precision=4), flush=True)

    # null battery
    cl = hp.anafast(t_map * mask, lmax=LMAX) / fsky
    np.random.seed(SEED)
    i_nulls = []
    for k in range(N_NULLS):
        sky = hp.synfast(cl, NSIDE, lmax=LMAX, verbose=False) \
            if "verbose" in hp.synfast.__code__.co_varnames \
            else hp.synfast(cl, NSIDE, lmax=LMAX)
        i_nulls.append(cmi_curve(sky))
        if (k + 1) % 20 == 0:
            print("  null %d/%d (%.0f s)" % (k + 1, N_NULLS,
                                             time.time() - T0), flush=True)
    i_nulls = np.array(i_nulls)
    sig = i_nulls.std(0, ddof=1)
    ok4 = check("G3 Kurven: Daten-CMI positiv und (broadly) fallend; "
                "Null-Streuung nichtdegeneriert",
                np.all(i_data > 0) and i_data[0] > i_data[-1]
                and np.all(sig > 0))

    # frozen decision statistics
    c1d, rate1 = fit_single(w, i_data, sig)
    c2d, r2d, a1d, a2d = fit_two(w, i_data, sig, RATIO_FROZEN)
    dchi_data = c1d - c2d
    c3d, ratio_free = fit_two_free(w, i_data, sig)
    dchi_null = []
    for row in i_nulls:
        cn1, _ = fit_single(w, row, sig)
        cn2, *_ = fit_two(w, row, sig, RATIO_FROZEN)
        dchi_null.append(cn1 - cn2)
    dchi_null = np.array(dchi_null)
    p_two = float((np.sum(dchi_null >= dchi_data) + 1)
                  / (len(dchi_null) + 1))
    excess = (i_data - i_nulls.mean(0)) / sig
    print("  F1 rate = %.3f/deg, chi2 = %.2f | F2(ratio 2.7095): "
          "rate = %.3f, amps = (%.3g, %.3g), chi2 = %.2f" %
          (rate1, c1d, r2d, a1d, a2d, c2d))
    print("  dchi2(F1->F2) data = %.3f ; null mean = %.3f ; "
          "p_two = %.3f" % (dchi_data, dchi_null.mean(), p_two))
    print("  F3 free ratio = %.3f (chi2 = %.2f) ; CMI excess vs null "
          "(sigma) = %s" % (ratio_free, c3d,
                            np.array2string(excess, precision=2)))

    hint = (p_two < P_HINT and RATIO_BAND[0] <= ratio_free
            <= RATIO_BAND[1])
    verdict = "hint" if hint else "null"
    ok5 = check("G4 eingefrorene Entscheidung: p_two = %.3f (Gate "
                "< %.2f), free ratio = %.2f (Band [%.1f, %.1f]) -> "
                "VERDIKT %s" % (p_two, P_HINT, ratio_free,
                                RATIO_BAND[0], RATIO_BAND[1],
                                verdict.upper()), True)

    out = {
        "frozen": {"nside": NSIDE, "lmax": LMAX, "bands": BANDS,
                   "r_A_deg": R_A_DEG, "w_deg": W_LIST_DEG,
                   "c_width_deg": C_WIDTH_DEG, "n_nulls": N_NULLS,
                   "seed": SEED, "ratio": RATIO_FROZEN,
                   "p_hint": P_HINT, "ratio_band": RATIO_BAND},
        "data_sha256": sha, "fsky": fsky, "n_centers": len(centers),
        "I_data": i_data.tolist(), "I_null_mean": i_nulls.mean(0).tolist(),
        "I_null_std": sig.tolist(),
        "fit_single": {"chi2": c1d, "rate_per_deg": rate1},
        "fit_two_frozen": {"chi2": c2d, "rate": r2d,
                           "amps": [a1d, a2d]},
        "fit_two_free": {"chi2": c3d, "ratio": ratio_free},
        "dchi2_data": dchi_data, "dchi2_null_mean": float(dchi_null.mean()),
        "p_two": p_two, "verdict": verdict,
        "excess_sigma": excess.tolist(),
    }
    Path(__file__).with_name("smica_annulus_recovery_results.json") \
        .write_text(json.dumps(out, indent=2), encoding="utf-8")
    return finish(verdict)


def finish(verdict):
    section("VERDIKT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("gates: %d/%d PASS; kills: %s" % (n_pass, len(CHECKS),
                                            KILLS or "keine"))
    if verdict is None:
        print("VERDIKT: ABGEBROCHEN (%s)" % KILLS)
        code = 1
    else:
        print("VERDIKT: %s (exploratorisch; ein Null ist gut gepowert "
              "und beschaedigt nichts -- [C]-Lesart)" % verdict.upper())
        code = 0
    print("total %.1f s" % (time.time() - T0))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
