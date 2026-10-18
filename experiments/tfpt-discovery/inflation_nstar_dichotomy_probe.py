#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""inflation_nstar_dichotomy_probe -- PHYS.INFLATION.NSTAR.DICHOTOMY.01

FROZEN SPEC v1 (2026-09-02).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.

=======================================================================
HYPOTHESIS
=======================================================================
Under P-ACT-LB (n_s = 0.9743 +/- 0.0034) the ENTIRE scalaron
(Starobinsky-branch) is disfavoured at >= 3 sigma independent of
reheating (because N_star <= 55.7 even for instantaneous reheating
gives n_s <= 0.9641), while under SPT-3G+Planck (0.9647 +/- 0.0037)
the A_s-preferred N_star ~ 56 is fine and the reheating N_star =
51.44 is ~1 sigma.  The dataset split, not the compiler, decides.

=======================================================================
FROZEN DATA TABLE
=======================================================================
  D1 Planck 2018 (TT,TE,EE+lowE+lensing): n_s = 0.9649 ± 0.0042 ; ln(10^10 A_s) = 3.044 ± 0.014 (A_s = 2.100e-9 ± 0.030e-9)
  D2 P-ACT (Planck+ACT DR6): n_s = 0.9709 ± 0.0038
  D3 P-ACT-LB (Planck+ACT DR6+DESI BAO+lensing): n_s = 0.9743 ± 0.0034 ; running alpha_s = +0.0062 ± 0.0052 ; r < 0.038 (95 %, with BK18)
  D4 SPT-3G D1 + Planck (2025): n_s = 0.9647 ± 0.0037
  D5 BICEP/Keck BK18: r < 0.036 (95 %)
  TFPT N_star candidates: C1 = 51.44 (reheating, v86) ; C2 = 55.42 (algebraic 3/phi0 - 1, v340 archive) ; C3 = 56.20 (A_s-preferred, v86) ; C4 = 55.7 (instantaneous-reheating ceiling, v86) ; band [50, 60].

=======================================================================
STAROBINSKY LO (frozen; c3 = 1/(8 pi))
=======================================================================
  n_s = 1 - 2/N ;  r = 12/N^2 ;  alpha_s = -2/N^2
  A_s = N^2 c3^7 / (24 pi^2)
  phi0 = (4/3) c3 + 48 c3^4
  C2 exact = 3/phi0 - 1 ;  C3 exact = sqrt(A_s_v86 * 24 pi^2 / c3^7)
  A_s_v86 = 2.105e-9  (v86/v340 Planck pivot used to define C3)
  physical reheating window N in [50, 55.7]  (instantaneous ceiling)

=======================================================================
PULL / VERDICT RULES (frozen)
=======================================================================
  pull = (TFPT - data) / sigma
  branch-level pull = min_{N in [50, 55.7]} |(1-2/N) - n_s_data|/sigma
    (0 if the dataset central lies inside the physical n_s interval)
  per dataset:
    BRANCH_CONSISTENT   iff branch-level pull < 2
    BRANCH_TENSION      iff 2 <= branch-level pull < 3
    BRANCH_DISFAVOURED  iff branch-level pull >= 3
  global: DATASET_SPLIT if D1..D4 verdicts are not all equal,
          else the common verdict.
  Honest note (appended): TFPT has no compiler-side N_star (the
  [50, 60] band is an external reheating input); the decision
  belongs to the CMB datasets converging.

=======================================================================
GATES
=======================================================================
G01 re-derive the v86 numbers 0.9611 / 0.00454 / 1.764e-9 / 56.20
    to 3 significant digits (N=51.44, A_s formula, A_s_v86).
G02 all reported pulls finite.
G03 two in-process evaluations byte-identical.
G04 verdict enum frozen (per-dataset in the three BRANCH_* values;
    global DATASET_SPLIT or the common BRANCH_*).
"""

import hashlib
import math
import sys

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

C3 = 1.0 / (8.0 * math.pi)
PHI0 = (4.0 / 3.0) * C3 + 48.0 * C3 ** 4
PI2 = math.pi ** 2
AS_PREFAC = (C3 ** 7) / (24.0 * PI2)

N_C1 = 51.44
N_C2 = 3.0 / PHI0 - 1.0
AS_V86 = 2.105e-9
SIG_AS_V86 = 0.030e-9
N_C3 = math.sqrt(AS_V86 / AS_PREFAC)
N_C4 = 55.7
N_LO, N_HI_BAND, N_CEIL = 50.0, 60.0, 55.7
KILL_NS = 0.967

CANDS = (
    ("C1", N_C1),
    ("C2", N_C2),
    ("C3", N_C3),
    ("C4", N_C4),
    ("B50", N_LO),
    ("B60", N_HI_BAND),
)

# (id, n_s, sigma_n_s)
DATA_NS = (
    ("D1", 0.9649, 0.0042),
    ("D2", 0.9709, 0.0038),
    ("D3", 0.9743, 0.0034),
    ("D4", 0.9647, 0.0037),
)
AS_D1, SIG_AS_D1 = 2.100e-9, 0.030e-9
R_D3, R_D5 = 0.038, 0.036

VERDICTS_OK = (
    "BRANCH_CONSISTENT",
    "BRANCH_TENSION",
    "BRANCH_DISFAVOURED",
)

CHECKS = []


def gate(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))


def pred(N):
    ns = 1.0 - 2.0 / N
    r = 12.0 / (N * N)
    al = -2.0 / (N * N)
    As = (N * N) * AS_PREFAC
    return ns, r, al, As


def n_from_ns(ns):
    return 2.0 / (1.0 - ns)


def n_from_as(As):
    return math.sqrt(As / AS_PREFAC)


def branch_pull(ns_data, sig):
    ns_lo, ns_hi = pred(N_LO)[0], pred(N_CEIL)[0]
    if ns_lo <= ns_data <= ns_hi:
        return 0.0
    if ns_data > ns_hi:
        return abs(ns_hi - ns_data) / sig
    return abs(ns_lo - ns_data) / sig


def classify(bp):
    if bp < 2.0:
        return "BRANCH_CONSISTENT"
    if bp < 3.0:
        return "BRANCH_TENSION"
    return "BRANCH_DISFAVOURED"


def finite(xs):
    return all(math.isfinite(x) for x in xs)


def payload():
    """Pure numbers; no printing.  Two calls must be bit-identical."""
    s1 = tuple((lab, N) + pred(N) for lab, N in CANDS)
    pulls = []
    for lab, N in CANDS:
        ns, r, _al, As = pred(N)
        ns_p = tuple((ns - mu) / sig for _d, mu, sig in DATA_NS)
        as_p = (As - AS_D1) / SIG_AS_D1
        r_d3 = r < R_D3
        r_d5 = r < R_D5
        pulls.append((lab, N, ns_p, as_p, r_d3, r_d5))
    implied = []
    for d, mu, sig in DATA_NS:
        n0 = n_from_ns(mu)
        n_lo = n_from_ns(mu - sig)
        n_hi = n_from_ns(mu + sig)
        implied.append((d, n0, n_lo, n_hi, n0 <= N_CEIL,
                        n_lo <= N_CEIL <= n_hi or n_lo <= N_LO <= n_hi
                        or (n_lo >= N_LO and n_hi <= N_CEIL)))
    n_as = n_from_as(AS_D1)
    n_as_lo = n_from_as(AS_D1 - SIG_AS_D1)
    n_as_hi = n_from_as(AS_D1 + SIG_AS_D1)
    bps = tuple(branch_pull(mu, sig) for _d, mu, sig in DATA_NS)
    kst = []
    for d, mu, sig in DATA_NS:
        z = (mu - KILL_NS) / sig
        kst.append((d, mu >= KILL_NS, z))
    ratio = N_C3 / N_C2 - 1.0
    need = tuple(n_from_ns(mu) for _d, mu, sig in DATA_NS)
    ns_2s = DATA_NS[2][1] - 2.0 * DATA_NS[2][2]
    n_2s = n_from_ns(ns_2s)
    any_phys = pred(N_CEIL)[0] >= ns_2s
    any_band = pred(N_HI_BAND)[0] >= ns_2s
    per = tuple(classify(bp) for bp in bps)
    glob = per[0] if all(v == per[0] for v in per) else "DATASET_SPLIT"
    return (s1, tuple(pulls), tuple(implied),
            (n_as, n_as_lo, n_as_hi), bps, tuple(kst),
            ratio, need, ns_2s, n_2s, any_phys, any_band, per, glob)


def main():
    a = payload()
    b = payload()
    (s1, pulls, implied, as_imp, bps, kst,
     ratio, need, ns_2s, n_2s, any_phys, any_band, per, glob) = a

    ns_c1, r_c1, _al_c1, as_c1 = pred(N_C1)
    g01 = (abs(ns_c1 - 0.9611) < 1e-4
           and abs(r_c1 - 0.00454) < 1e-5
           and abs(as_c1 - 1.764e-9) < 5e-12
           and abs(N_C3 - 56.20) < 0.01)
    gate("G01 v86 numbers 0.9611 / 0.00454 / 1.764e-9 / 56.20",
         g01,
         "ns=%.4f r=%.5f As=%.4e N3=%.2f" % (ns_c1, r_c1, as_c1, N_C3))

    pull_vals = []
    for _lab, _N, ns_p, as_p, _r3, _r5 in pulls:
        pull_vals.extend(ns_p)
        pull_vals.append(as_p)
    pull_vals.extend(bps)
    gate("G02 pulls finite", finite(pull_vals))
    gate("G03 two evaluations byte-identical", a == b)
    enum_ok = (all(v in VERDICTS_OK for v in per)
               and (glob == "DATASET_SPLIT" or glob in VERDICTS_OK)
               and ((glob == "DATASET_SPLIT") == (len(set(per)) > 1)))
    gate("G04 verdict enum frozen", enum_ok)

    print("S1 candidates + band edges")
    print("  %4s %8s %8s %9s %11s %11s" %
          ("id", "N", "n_s", "r", "alpha_s", "A_s"))
    for lab, N, ns, r, al, As in s1:
        print("  %4s %8.4f %8.5f %9.5f %11.4e %11.4e" %
              (lab, N, ns, r, al, As))

    print("S2 pull matrix  pull=(TFPT-data)/sigma ; r vs 95% bounds")
    print("  %4s %7s %7s %7s %7s %8s %6s %6s" %
          ("id", "D1_ns", "D2_ns", "D3_ns", "D4_ns", "D1_As", "r<D3", "r<D5"))
    for lab, _N, ns_p, as_p, r_d3, r_d5 in pulls:
        print("  %4s %+7.2f %+7.2f %+7.2f %+7.2f %+8.2f %6s %6s" %
              (lab, ns_p[0], ns_p[1], ns_p[2], ns_p[3], as_p,
               "PASS" if r_d3 else "FAIL", "PASS" if r_d5 else "FAIL"))

    print("S3 implied N_star  N=2/(1-n_s)  [1 sigma]; A_s D1 N=sqrt(A_s*24*pi^2/c3^7)")
    for (d, n0, n_lo, n_hi, cen_ok, iv_ok) in implied:
        print("  %s n_s: N=%.2f [%.2f, %.2f]  central<=55.7? %s  "
              "1s-interval hits [50,55.7]? %s"
              % (d, n0, n_lo, n_hi, "YES" if cen_ok else "NO",
                 "YES" if iv_ok else "NO"))
    n_as, n_as_lo, n_as_hi = as_imp
    print("  D1 A_s: N=%.2f [%.2f, %.2f]  central<=55.7? %s"
          % (n_as, n_as_lo, n_as_hi, "YES" if n_as <= N_CEIL else "NO"))
    print("  branch-level |pull| N in [50,55.7]: D1=%.3f D2=%.3f D3=%.3f D4=%.3f"
          % bps)
    print("  n_s(N=55.7)=%.5f  n_s(N=50)=%.5f  any n_s-central N inside ceiling? %s"
          % (pred(N_CEIL)[0], pred(N_LO)[0],
             "YES" if any(row[4] for row in implied) else "NO"))

    print("S4 kill-statement  v86: n_s>=0.967 falsifies the scalaron-reheating chain")
    for (d, trig, z) in kst:
        excl2 = z > 2.0
        if trig:
            status = ("kill-line HIT; 0.967 is %.2f sigma below central; "
                      "2s-excluded? %s" % (z, "YES" if excl2 else "NO"))
        else:
            status = ("kill-line MISS; 0.967 is %.2f sigma above central; "
                      "ALLOWED" % (-z))
        print("  %s central>=0.967? %s  z=(n_s-0.967)/sig=%+.2f  %s"
              % (d, "YES" if trig else "NO", z, status))

    print("S5 dichotomy")
    print("  (C3/C2 - 1) = %.4f%%  (C2=%.4f algebraic, C3=%.4f A_s-preferred)"
          % (100.0 * ratio, N_C2, N_C3))
    print("  n_s-needed N_star: D1=%.2f D2=%.2f D3=%.2f D4=%.2f" % need)
    print("  P-ACT-LB 2-sigma floor n_s=%.4f => N>=%.2f" % (ns_2s, n_2s))
    print("  ANY physical N<=55.7 satisfy P-ACT-LB within 2 sigma? %s"
          % ("YES" if any_phys else "NO"))
    print("  ANY frozen-band N<=60 satisfy P-ACT-LB within 2 sigma? %s"
          % ("YES" if any_band else "NO"))

    print("S6 VERDICT")
    print("  D1=%s D2=%s D3=%s D4=%s" % per)
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("GATES %d/%d" % (n_pass, len(CHECKS)))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("VERDICT: %s  NOTE: TFPT has no compiler-side N_star "
          "(band [50,60] is external); the decision belongs to the "
          "CMB datasets converging." % glob)
    sys.exit(0 if n_pass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
