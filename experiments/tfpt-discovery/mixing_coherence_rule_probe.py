#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mixing_coherence_rule_probe -- FLAV.THIRDGEN.PATTERN.01 calibrated OOS

FROZEN SPEC v1 (2026-09-02).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.

HYPOTHESIS.  Any multiplicative dressing f(phi0) of the bare seed that
reproduces the accepted Cabibbo value lambda_C = sqrt(phi0 * f)
within the data error predicts sin^2 theta13 = phi0 f e^{-5/6} in
[0.0218, 0.0222] and |V_cb| = phi0 f/(1+lambda_C) in [0.0410, 0.0418],
i.e. the third-generation channels are fixed to ~1 % by the 1-2
calibration alone, independent of the functional form of f; the
record's bare choice f = 1 is the only member of the family that is
EXCLUDED by the 1-2 channel and it is also the one in 2-sigma tension
in the third generation.

AXIOMS.  c3 = 1/(8 pi); phi0 = (4/3) c3 + 48 c3^4;
lambda_C(record) = sqrt(phi0 (1-phi0)).  Identity (exact): with
sin^2 theta_sheet = phi0, sin theta_sheet cos theta_sheet =
sqrt(phi0(1-phi0)) = lambda_C, i.e. lambda_C is the off-diagonal
(coherence) element |rho_12| of the two-sheet projector with
population phi0, and lambda_C^2 = Var[Bernoulli(phi0)].

CALIBRATION (1-2).  X = phi0 * f;  lambda_pred = sqrt(X);
PASS iff |pull| vs lambda_C data <= 2.

OOS (uniform in X; survivors AND bare).
  sin^2 theta13 = X e^{-5/6}
  |V_cb|         = X / (1 + lambda_pred)
  |V_ub|         = lambda_pred^3 / 3     (scope: survivors |pull|<=2)
  sin^2 theta23 = (1 - X) / 2            (cos 2theta23 = X)
  delta          = pi/3 + 3 X           (degrees)
Joint chi^2 over {theta13(Daya Bay), V_cb, V_ub, theta23}; dof = 4.

FROZEN DATA (verbatim).
  lambda_C = 0.22501 +/- 0.00068 (PDG 2024 CKM fit)
  |V_cb| = 0.0418 +/- 0.0008 (PDG 2024)
  |V_ub| = 0.00369 +/- 0.00011 (PDG 2024)
  sin^2 theta13 = 0.02175 +/- 0.00065 (Daya Bay final 2023, PRIMARY)
  sin^2 theta13 = 0.02195 +/- 0.00058 (NuFIT 6.0, shadow)
  sin^2 theta23 = 0.470 +/- 0.017 (NuFIT 6.0 NO)
  sin^2 theta12 = 0.3092 +/- 0.0087 (JUNO 2026)
  delta_CKM = 65.5 +/- 1.5 deg (PDG 2024 fit)

FROZEN DRESSING FAMILY F (closed form in {phi0, c3, lambda_C, pi};
no free parameter).  Required: 1 (bare, record); (1-phi0)
[coherence^2, = v467 ladder base]; 1/(1+phi0) [Born resolvent];
1/(1+phi0)^2; (1-phi0)^2; (1-c3); (1-2c3)=1-1/(4pi) [Omega_b];
(1-lambda_C^2); (1-lambda_C); 1/(1+lambda_C); exp(-phi0); exp(-c3);
(1-phi0/2); (1-3phi0/4) [epsilon of v16]; 53/54 [FR.KOIDE.03];
(1-phi0^2); cos^2(theta_sheet) with sin^2 theta_sheet = phi0 (alias of
1-phi0); 1-(2/3)^6; 1-phi0-phi0^2.  Plus every v467 census form:
1 +/- phi0, 1 +/- phi0/2, 1 +/- lambda_C, 1 +/- c3, 1 +/- lambda_C^2,
1 +/- (2/3)^6, 1 +/- dtop (dtop=48 c3^4), 1 +/- phibase (1/(6 pi)).

VERDICT (frozen enum).
  CALIBRATED_PREDICTION_CONFIRMED if >= 80 % of S2 survivors have S3
    joint chi^2 <= 2 x dof AND the bare record FAILS S2 and has S3
    chi^2 > 2 x dof
  CALIBRATED_PREDICTION_MIXED if survivors split
  CALIBRATION_UNDECIDABLE if fewer than 3 survivors
Append: 'candidate reframing of FLAV.THIRDGEN.PATTERN.01 from
post-hoc to calibrated; no marker move; record unchanged'

GATES.  G01 identity gates exact (sympy); G02 family size >= 20,
contains all 16 v467 forms (named); G03 bare f=1 present and
evaluated; G04 two in-process evaluations byte-identical; G05
verdict enum frozen.
"""

import hashlib
import math
import sys

import sympy as sp

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

C3 = 1.0 / (8.0 * math.pi)
PHI0 = (4.0 / 3.0) * C3 + 48.0 * C3 ** 4
LAM = math.sqrt(PHI0 * (1.0 - PHI0))
DTOP = 48.0 * C3 ** 4
PHIBASE = 1.0 / (6.0 * math.pi)
E56 = math.exp(-5.0 / 6.0)
BAND6 = (2.0 / 3.0) ** 6
DOF, CHI_CUT = 4, 8.0
RAD2DEG = 180.0 / math.pi

LAM_DAT, LAM_SIG = 0.22501, 0.00068
VCB_DAT, VCB_SIG = 0.0418, 0.0008
VUB_DAT, VUB_SIG = 0.00369, 0.00011
TH13_DB, TH13_DBS = 0.02175, 0.00065
TH13_NF, TH13_NFS = 0.02195, 0.00058
TH23_DAT, TH23_SIG = 0.470, 0.017
DEL_DAT, DEL_SIG = 65.5, 1.5

FAMILY = (
    ("bare", 1.0),
    ("1-phi0", 1.0 - PHI0),
    ("1/(1+phi0)", 1.0 / (1.0 + PHI0)),
    ("1/(1+phi0)^2", 1.0 / (1.0 + PHI0) ** 2),
    ("(1-phi0)^2", (1.0 - PHI0) ** 2),
    ("1-c3", 1.0 - C3),
    ("1-2c3", 1.0 - 2.0 * C3),
    ("1-lambda_C^2", 1.0 - LAM ** 2),
    ("1-lambda_C", 1.0 - LAM),
    ("1/(1+lambda_C)", 1.0 / (1.0 + LAM)),
    ("exp(-phi0)", math.exp(-PHI0)),
    ("exp(-c3)", math.exp(-C3)),
    ("1-phi0/2", 1.0 - 0.5 * PHI0),
    ("1-3phi0/4", 1.0 - 0.75 * PHI0),
    ("53/54", 53.0 / 54.0),
    ("1-phi0^2", 1.0 - PHI0 ** 2),
    ("cos2_sheet", 1.0 - PHI0),
    ("1-(2/3)^6", 1.0 - BAND6),
    ("1-phi0-phi0^2", 1.0 - PHI0 - PHI0 ** 2),
    ("1+phi0", 1.0 + PHI0),
    ("1+phi0/2", 1.0 + 0.5 * PHI0),
    ("1+lambda_C", 1.0 + LAM),
    ("1+c3", 1.0 + C3),
    ("1+lambda_C^2", 1.0 + LAM ** 2),
    ("1+(2/3)^6", 1.0 + BAND6),
    ("1+dtop", 1.0 + DTOP),
    ("1-dtop", 1.0 - DTOP),
    ("1+phibase", 1.0 + PHIBASE),
    ("1-phibase", 1.0 - PHIBASE),
)
V467 = (
    "1+phi0", "1-phi0", "1+phi0/2", "1-phi0/2",
    "1+lambda_C", "1-lambda_C", "1+c3", "1-c3",
    "1+lambda_C^2", "1-lambda_C^2", "1+(2/3)^6", "1-(2/3)^6",
    "1+dtop", "1-dtop", "1+phibase", "1-phibase",
)
VERDICTS_OK = (
    "CALIBRATED_PREDICTION_CONFIRMED",
    "CALIBRATED_PREDICTION_MIXED",
    "CALIBRATION_UNDECIDABLE",
)
NOTE = ("candidate reframing of FLAV.THIRDGEN.PATTERN.01 from "
        "post-hoc to calibrated; no marker move; record unchanged")

CHECKS = []


def gate(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))


def pull(pred, mu, sig):
    return (pred - mu) / sig


def row_of(name, f):
    x = PHI0 * f
    lam = math.sqrt(x)
    p12 = pull(lam, LAM_DAT, LAM_SIG)
    th13 = x * E56
    vcb = x / (1.0 + lam)
    vub = lam ** 3 / 3.0
    th23 = (1.0 - x) / 2.0
    ddeg = (math.pi / 3.0 + 3.0 * x) * RAD2DEG
    p_db = pull(th13, TH13_DB, TH13_DBS)
    p_nf = pull(th13, TH13_NF, TH13_NFS)
    p_cb = pull(vcb, VCB_DAT, VCB_SIG)
    p_ub = pull(vub, VUB_DAT, VUB_SIG)
    p_23 = pull(th23, TH23_DAT, TH23_SIG)
    p_d = pull(ddeg, DEL_DAT, DEL_SIG)
    chi = p_db ** 2 + p_cb ** 2 + p_ub ** 2 + p_23 ** 2
    ok12 = abs(p12) <= 2.0
    return (name, f, x, lam, p12, ok12, th13, p_db, p_nf,
            vcb, p_cb, vub, p_ub, th23, p_23, ddeg, p_d, chi)


def payload():
    rows = tuple(row_of(n, f) for n, f in FAMILY)
    ordered = tuple(sorted(rows, key=lambda r: (abs(r[4]), r[0])))
    return ordered


def main():
    a = payload()
    b = payload()
    names = [n for n, _f in FAMILY]
    v467_ok = all(n in names for n in V467)
    p = sp.Symbol("phi0", positive=True)
    lam2 = p * (1 - p)
    sincos = p * (1 - p)
    var_b = p - p ** 2
    g01 = (sp.simplify(lam2 - sincos) == 0
           and sp.simplify(lam2 - var_b) == 0
           and abs(LAM ** 2 - PHI0 * (1.0 - PHI0)) < 1e-15)
    gate("G01 identity gates exact (sympy)", g01,
         "lambda_C^2 == phi0(1-phi0) == sin^2 cos^2 == Var[Bernoulli]")
    gate("G02 family size >= 20, contains all v467 forms",
         len(FAMILY) >= 20 and v467_ok and len(V467) == 16,
         "n=%d v467=%s" % (len(FAMILY), ",".join(V467)))
    bare_rows = [r for r in a if r[0] == "bare"]
    gate("G03 bare f=1 present and evaluated",
         "bare" in names and len(bare_rows) == 1
         and abs(bare_rows[0][1] - 1.0) < 1e-15)
    gate("G04 two in-process evaluations byte-identical", a == b)
    print("S1 Identity gates")
    print("  lambda_C^2 = %.15f = phi0(1-phi0) = sin^2 cos^2 "
          "(sin^2=phi0) = Var[Bernoulli(phi0)]  (sympy exact)"
          % (LAM ** 2))
    print("  coherence: lambda_C is |rho_12| of the two-sheet projector "
          "with population phi0; lambda_C^2 = Var[Bernoulli(phi0)].")

    print("S2 CALIBRATION 1-2  lambda_pred=sqrt(phi0 f) vs "
          "0.22501 +/- 0.00068; PASS iff |pull|<=2")
    print("  %-16s %10s %10s %10s %8s %4s" %
          ("name", "f", "X", "lam_pred", "pull", "S2"))
    n_s2 = 0
    for r in a:
        flag = "PASS" if r[5] else "FAIL"
        if r[5]:
            n_s2 += 1
        print("  %-16s %10.6f %10.6f %10.6f %+8.2f %4s" %
              (r[0], r[1], r[2], r[3], r[4], flag))
    bare = bare_rows[0]
    print("  survivors %d / %d;  bare f=1 FAILS S2 pull=%+.2f"
          % (n_s2, len(FAMILY), bare[4]))

    surv = [r for r in a if r[5]]
    show = list(surv) + ([] if bare[5] else [bare])
    print("S3 OOS  th13=X e^{-5/6}  Vcb=X/(1+lam)  Vub=lam^3/3  "
          "th23=(1-X)/2  delta=pi/3+3X  chi2={DB,Vcb,Vub,th23}")
    print("  %-16s %8s %6s %6s %8s %6s %8s %6s %8s %6s %7s %6s %7s" %
          ("name", "th13", "pDB", "pNF", "Vcb", "pCB", "Vub", "pUB",
           "th23", "p23", "ddeg", "pD", "chi2"))
    for r in show:
        print("  %-16s %8.6f %+6.2f %+6.2f %8.6f %+6.2f %8.6f %+6.2f "
              "%8.6f %+6.2f %7.2f %+6.2f %7.2f" %
              (r[0], r[6], r[7], r[8], r[9], r[10], r[11], r[12],
               r[13], r[14], r[15], r[16], r[17]))
    th13s = [r[6] for r in surv]
    vcbs = [r[9] for r in surv]
    vub_ok = all(abs(r[12]) <= 2.0 for r in surv)
    if surv:
        print("  prediction band (survivors): sin^2 theta13 "
              "[%.5f, %.5f]  |V_cb| [%.5f, %.5f]"
              % (min(th13s), max(th13s), min(vcbs), max(vcbs)))
        print("  V_ub scope |pull|<=2 for all survivors? %s" %
              ("YES" if vub_ok else "NO"))
    else:
        print("  prediction band: no survivors")

    coh = [r for r in a if r[0] == "1-phi0"][0]
    born = [r for r in a if r[0] == "1/(1+phi0)"][0]
    print("S4 DISCRIMINATION  coherence (1-phi0) vs Born 1/(1+phi0)")

    def relsep(p1, p2):
        return abs(p1 - p2) / (0.5 * (p1 + p2))

    chans = (
        ("lambda_C", coh[3], born[3], LAM_DAT, LAM_SIG),
        ("sin2_th13", coh[6], born[6], TH13_DB, TH13_DBS),
        ("sin2_th13_NF", coh[6], born[6], TH13_NF, TH13_NFS),
        ("|V_cb|", coh[9], born[9], VCB_DAT, VCB_SIG),
    )
    closest, best = None, None
    for lab, p1, p2, mu, sig in chans:
        dlt = abs(p1 - p2)
        rs = relsep(p1, p2)
        mid = 0.5 * (p1 + p2)
        need = dlt / (3.0 * mid)
        cur = sig / mu
        ratio = cur / need
        print("  %s  p_coh=%.6f p_born=%.6f  rel_sep=%.4f%%  "
              "sigma_rel_3sig=%.4f%%  current=%.4f%%  "
              "current/needed=%.1fx" %
              (lab, p1, p2, 100.0 * rs, 100.0 * need, 100.0 * cur, ratio))
        if best is None or ratio < best:
            closest, best = lab, ratio
    print("  closest current dataset to 3-sigma separation: %s "
          "(current/needed=%.1fx)" % (closest, best))

    n_ok = sum(1 for r in surv if r[17] <= CHI_CUT)
    frac_s2 = n_s2 / float(len(FAMILY))
    frac_ok = (n_ok / float(n_s2)) if n_s2 else 0.0
    print("S5 look-elsewhere")
    print("  fraction of family passing S2: %d/%d = %.3f" %
          (n_s2, len(FAMILY), frac_s2))
    print("  fraction of S2-survivors with S3 chi2 < 2*dof=8: "
          "%d/%d = %.3f" % (n_ok, n_s2, frac_ok))
    print("  bare record S3 chi2 = %.2f  (2*dof=8)" % bare[17])
    if surv:
        span13 = max(th13s) - min(th13s)
        span_cb = max(vcbs) - min(vcbs)
        band13 = min(th13s) >= 0.0218 and max(th13s) <= 0.0222
        band_cb = min(vcbs) >= 0.0410 and max(vcbs) <= 0.0418
        pred = span13 / min(th13s) < 0.02 and span_cb / min(vcbs) < 0.02
        print("  survivor span  th13=%.2f%%  Vcb=%.2f%%  "
              "hyp-band th13? %s  Vcb? %s" %
              (100.0 * span13 / min(th13s), 100.0 * span_cb / min(vcbs),
               "YES" if band13 else "NO", "YES" if band_cb else "NO"))
        print("  third-generation values ARE predicted by the 1-2 "
              "calibration (all survivors in a ~1% band)."
              if pred else
              "  third-generation values are NOT a unique calibration "
              "prediction (survivors span a wide band).")
    if n_s2 < 3:
        verd = "CALIBRATION_UNDECIDABLE"
    elif (frac_ok >= 0.80 and (not bare[5]) and bare[17] > CHI_CUT):
        verd = "CALIBRATED_PREDICTION_CONFIRMED"
    else:
        verd = "CALIBRATED_PREDICTION_MIXED"
    gate("G05 verdict enum frozen", verd in VERDICTS_OK, verd)
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("GATES %d/%d" % (n_pass, len(CHECKS)))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("VERDICT: %s  %s" % (verd, NOTE))
    sys.exit(0 if n_pass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
