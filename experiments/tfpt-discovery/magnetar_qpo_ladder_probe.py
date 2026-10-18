#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""magnetar_qpo_ladder_probe -- MAG.QPO.LADDER.01

FROZEN SPEC v1 (2026-08-15).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.

=======================================================================
MANDATE
=======================================================================
Owner directive: "Finde neue Muster, Beweise, Vorhersagen der Theorie."
This probe opens a NEW empirical bed that no experiment in the corpus
has touched (verified by grep 2026-08-15: no magnetar giant-flare QPO
test anywhere in experiments/): the quasi-periodic oscillations in the
decaying tails of the two well-measured magnetar giant flares.

FIREWALL (read first, S15 discipline):
  * The standing astrophysical explanation for these QPOs is torsional
    crustal / magneto-elastic oscillation modes of the neutron star
    (Duncan 1998; Israel+ 2005; Watts & Strohmayer 2006).  That
    explanation is the favorite and nothing here challenges it.
  * TFPT derives NO magnetar emission mechanism.  There is no named
    transduction B for this channel, so by the S15 gate this is an
    exploratory SURFACE-LEAKAGE probe, escalate-only: a null is a
    bridge-null, not a core-null; even a hit would be [C]-tier
    coincidence-risk until a mapping is derived.
  * Mirrors the hfqpo-ladder discipline: the TFPT reading tested is
    the geometric relaxation ladder with per-rung scale factor 3/2
    (from rate(n) = -6 ln(1 - n/3), N_fam = 3; frequency teeth at
    nu_0 * (3/2)^k).  A crustal mode spectrum has NO reason to sit on
    a geometric ladder; distinct mode families (l-overtones, radial
    overtones) predict different, roughly integer-flavored spacings.

=======================================================================
DATA (published tables only; hardcoded with references; frozen)
=======================================================================
SGR 1806-20, 2004-12-27 giant flare (RXTE + RHESSI):
    18, 26, 30, 92.5, 150, 625, 1840 Hz
    [Israel+ 2005 ApJ 628 L53; Watts & Strohmayer 2006 ApJ 637 L117;
     Strohmayer & Watts 2006 ApJ 653 593; QPO widths 1-5 Hz except
     the 150 Hz QPO with FWHM ~17 Hz]
SGR 1900+14, 1998-08-27 giant flare (RXTE):
    28, 53.5, 84, 155 Hz
    [Strohmayer & Watts 2005 ApJ 632 L111]
SGR 0526-66 (1979): single 43 Hz hint (Barat+ 1983) -- EXCLUDED
    (frozen rule: a source enters only with >= 3 published centroids).

=======================================================================
PREREGISTERED TEST (frozen before any statistic is computed)
=======================================================================
H1 LADDER TEST, per source.  For every unordered frequency pair
   (nu_i < nu_j) compute the rung coordinate
       r_ij = ln(nu_j/nu_i) / ln(3/2)
   and the tooth distance d_ij = |r_ij - round(r_ij)|, with
   round(r_ij) >= 1 enforced (a pair less than half a rung apart
   contributes its distance to rung 1; the ladder has no rung 0).
   Statistic: S = mean over pairs of d_ij.  Small S = pair ratios
   cluster on powers of 3/2.

   NULL (frozen): 20000 Monte-Carlo draws (seed 20260815) of the same
   number of frequencies, log-uniform on [min(nu), max(nu)] of that
   source, same statistic.  p = P(S_null <= S_obs), one-sided.

H2 BASE BATTERY (look-elsewhere control, mirrors the recovery-comb
   per-omega calibration).  Repeat H1 with placebo ladder bases
   lambda in {1.20, 1.25, ..., 2.00} (17 bases; 1.50 is the kernel
   base).  Report the rank of the kernel base's p among all bases
   (rank 1 = kernel base has the smallest p).

H3 JOINT: Fisher combination of the per-source kernel-base p-values
   (2 sources, 4 dof).

VERDICT RULES (frozen):
   LADDER-CONSISTENT  iff p_joint < 0.01 AND kernel-base rank <= 2
                      in BOTH sources.
   NULL               iff p_joint >= 0.05.
   WEAK-UNTYPED       otherwise (report, no escalation).
   DATA-LIMITED       per source with < 3 centroids (SGR 0526-66).

Typing note (frozen): any outcome is exploratory surface leakage.
A LADDER-CONSISTENT verdict would create a hypotheses/ YAML +
scorecard row via the regular pipeline in a LATER, separate step --
never from inside this probe.

=======================================================================
GATES
=======================================================================
G01 data integrity: 7 + 4 centroids, all positive, strictly increasing.
G02 rung coordinates finite; max rung <= 14 (1840/18 spans ~11.4 rungs).
G03 MC reproducibility: two independent generators with the frozen
    seed give identical S_null quantiles (bitwise).
G04 null sanity: planted ladder nu_0*(3/2)^{0..5} with 0.5% jitter
    yields p < 0.001 under the same machinery (power check).
G05 planted anti-ladder (integer harmonics 1..6 * nu_0) does NOT pass
    the ladder test at p < 0.001 with base 1.5 (specificity check;
    frozen bar: p_harmonics > 0.001).
G06 base battery complete: 17 bases, all p-values finite.
G07 verdict enum is one of the four frozen strings.
"""

import hashlib
import math
import sys
import time

import numpy as np

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

SEED = 20260815
N_MC = 20000
KERNEL_BASE = 1.5
BASES = [round(1.20 + 0.05 * k, 2) for k in range(17)]  # 1.20 .. 2.00

DATA = {
    "SGR1806-20": [18.0, 26.0, 30.0, 92.5, 150.0, 625.0, 1840.0],
    "SGR1900+14": [28.0, 53.5, 84.0, 155.0],
}

CHECKS = []


def gate(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))


def ladder_stat(freqs, base):
    """Mean tooth distance of all pair log-ratios, rung >= 1 enforced."""
    lb = math.log(base)
    n = len(freqs)
    ds = []
    for i in range(n):
        for j in range(i + 1, n):
            r = math.log(freqs[j] / freqs[i]) / lb
            k = max(1, int(round(r)))
            ds.append(abs(r - k))
    return float(np.mean(ds))


def mc_pvalue(freqs, base, rng):
    """One-sided p for the observed mean tooth distance vs log-uniform."""
    s_obs = ladder_stat(freqs, base)
    lo, hi = math.log(min(freqs)), math.log(max(freqs))
    n = len(freqs)
    count = 0
    s_null = np.empty(N_MC)
    for m in range(N_MC):
        draw = np.sort(np.exp(rng.uniform(lo, hi, n)))
        s = ladder_stat(list(draw), base)
        s_null[m] = s
        if s <= s_obs:
            count += 1
    p = (count + 1) / (N_MC + 1)
    return s_obs, p, s_null


def main():
    t0 = time.time()
    print("magnetar_qpo_ladder_probe -- MAG.QPO.LADDER.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("seed %d  N_MC %d  bases %d (kernel 1.5)" %
          (SEED, N_MC, len(BASES)))

    # G01 data integrity
    ok1 = (len(DATA["SGR1806-20"]) == 7 and len(DATA["SGR1900+14"]) == 4)
    for src, fr in DATA.items():
        ok1 &= all(f > 0 for f in fr) and fr == sorted(fr) \
            and len(set(fr)) == len(fr)
    gate("G01 data integrity (7+4 centroids, positive, increasing)", ok1)

    # G02 rung range
    max_rung = max(
        math.log(fr[-1] / fr[0]) / math.log(KERNEL_BASE)
        for fr in DATA.values())
    gate("G02 rung coordinates finite, max rung <= 14", max_rung <= 14.0,
         "max rung %.2f" % max_rung)

    # G03 MC reproducibility
    rng_a = np.random.default_rng(SEED)
    rng_b = np.random.default_rng(SEED)
    _, _, sn_a = mc_pvalue(DATA["SGR1900+14"], KERNEL_BASE, rng_a)
    _, _, sn_b = mc_pvalue(DATA["SGR1900+14"], KERNEL_BASE, rng_b)
    gate("G03 MC reproducibility (bitwise quantiles at frozen seed)",
         np.array_equal(sn_a, sn_b))

    # G04 power check: planted ladder must be detected
    rng = np.random.default_rng(SEED + 1)
    planted = [10.0 * KERNEL_BASE ** k * (1.0 + 0.005 * z)
               for k, z in zip(range(6), rng.standard_normal(6))]
    planted.sort()
    _, p_plant, _ = mc_pvalue(planted, KERNEL_BASE,
                              np.random.default_rng(SEED + 2))
    gate("G04 planted 3/2-ladder detected (p < 0.001)", p_plant < 1e-3,
         "p_plant %.5f" % p_plant)

    # G05 specificity: integer harmonics must NOT pass as a 3/2 ladder
    harmonics = [30.0 * k for k in range(1, 7)]
    _, p_harm, _ = mc_pvalue(harmonics, KERNEL_BASE,
                             np.random.default_rng(SEED + 3))
    gate("G05 integer-harmonic anti-ladder not detected (p > 0.001)",
         p_harm > 1e-3, "p_harm %.5f" % p_harm)

    # H1 + H2: per-source, full base battery
    print("\n  H1/H2 per-source base battery (mean tooth distance, MC p):")
    kernel_p = {}
    kernel_rank = {}
    for src, fr in DATA.items():
        rows = []
        for b_i, base in enumerate(BASES):
            rng_s = np.random.default_rng(SEED + 100 + b_i)
            s_obs, p, _ = mc_pvalue(fr, base, rng_s)
            rows.append((base, s_obs, p))
        ps = {b: p for (b, _, p) in rows}
        p_k = ps[KERNEL_BASE]
        rank = 1 + sum(1 for (b, _, p) in rows
                       if b != KERNEL_BASE and p < p_k)
        kernel_p[src] = p_k
        kernel_rank[src] = rank
        best = min(rows, key=lambda r: r[2])
        s_k = [r[1] for r in rows if r[0] == KERNEL_BASE][0]
        print("    %s: kernel base 1.5  S=%.4f  p=%.4f  rank %d/17 "
              "(best base %.2f p=%.4f)"
              % (src, s_k, p_k, rank, best[0], best[2]))
        ok6 = len(rows) == 17 and all(np.isfinite(r[2]) for r in rows)
        gate("G06 base battery complete for %s" % src, ok6)

    # H3 Fisher combination (kernel base)
    chi2 = -2.0 * sum(math.log(p) for p in kernel_p.values())
    # chi2 with 4 dof, survival function
    p_joint = math.exp(-chi2 / 2.0) * (1.0 + chi2 / 2.0)
    print("\n  H3 Fisher joint (kernel base): chi2=%.3f (4 dof)  "
          "p_joint=%.4f" % (chi2, p_joint))

    # Verdict (frozen rules)
    if p_joint < 0.01 and all(kernel_rank[s] <= 2 for s in DATA):
        verdict = "LADDER-CONSISTENT"
    elif p_joint >= 0.05:
        verdict = "NULL"
    else:
        verdict = "WEAK-UNTYPED"
    gate("G07 verdict enum frozen", verdict in
         ("LADDER-CONSISTENT", "NULL", "WEAK-UNTYPED", "DATA-LIMITED"))

    n_pass = sum(1 for _, ok in CHECKS if ok)
    rt = time.time() - t0
    print("\n  SGR 0526-66: DATA-LIMITED (single 43 Hz hint, frozen "
          "exclusion rule)")
    print("  GATES %d/%d  runtime %.1f s  SPEC_SHA %s"
          % (n_pass, len(CHECKS), rt, SPEC_SHA[:16]))
    print("  VERDICT: %s  (exploratory surface-leakage probe; no named "
          "transduction B; standing favorite remains torsional "
          "crustal/magneto-elastic modes)" % verdict)
    sys.exit(0 if n_pass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
