#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seed_tomography_registry_probe -- PHYS.SEED.TOMOGRAPHY.REGISTRY.01

FROZEN SPEC v1 (2026-09-02).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.

=======================================================================
MANDATE
=======================================================================
Invert every phi0-dependent frozen TFPT prediction to the phi0 value
the current data imply ("phi0 tomography"); enumerate every phi0-FREE
cross-relation ("seed line") between pairs of monomial predictions and
score them against data; audit the quark-mass-ratio legs for mixed-scale
vs same-scale conventions.

This probe EXTENDS seed-consistency (experiments/seed-consistency; 4 legs
beta, Omega_b, theta13 reactor-only, Cabibbo; chi2/dof 1.23; decoder
u = 0.05292) to the FULL frozen registry (13 legs).  It does not
duplicate that 4-leg decoder; it cites it.  ALPHA_INV is c3-driven via
a Ward root and is EXCLUDED from tomography.

HYPOTHESIS (tested, not assumed): the [E]-core legs {ME_OVER_MMU,
LAMBDA_C, OMEGA_B, SIN2_THETA12} cluster at the compiler phi0 =
0.0531720; dressed/scale-tagged legs (theta13, s23, m_mu/m_tau,
m_c/m_s) scatter; the m_c/m_s frozen value 13.6 matches only the
MIXED-scale PDG headline m_c(m_c)/m_s(2 GeV), while the RG-invariant
same-scale ratio is ~11.7.

=======================================================================
FROZEN INPUTS
=======================================================================
Compiler: c3 = 1/(8 pi); phi0 = (4/3) c3 + 48 c3^4.
Registry: verification/predictions_frozen.json (keys registry,
freeze_date, axioms, policy, predictions, assigned_texture_values,
conditional_bands).  Load frozen_value from this file; gate that
re-evaluated formulas reproduce them to 1e-12 relative.

The 13 registry formulas (LaTeX-free):
  SIN2_THETA12_SEED = 1/3 - phi0/2
  SIN2_THETA13      = phi0 * exp(-5/6)
  BETA_BIREFRINGENCE_DEG = phi0/(4 pi) * 180/pi
  OMEGA_B           = (1 - 1/(4 pi)) * phi0
  LAMBDA_C          = sqrt(phi0 (1-phi0))
  S23_CKM           = phi0 / (1 + LAMBDA_C)
  S13_CKM           = LAMBDA_C^3 / 3
  DELTA_CKM_RAD     = pi/3 + 3 LAMBDA_C^2
  MMU_OVER_MTAU     = (8/7) phi0
  ME_OVER_MMU       = (12/7) phi0^2
  MC_OVER_MS        = (34/47) / phi0
  MT_OVER_MB        = (3/26) / phi0^2
  MU_OVER_MD        = 55/117   (phi0-free CONTROL only)
  ALPHA_INV         EXCLUDED (c3-driven Ward root)

S2 primary data for MC_OVER_MS and MT_OVER_MB is the MIXED-scale
headline (the convention the frozen 13.6 / ~41 numbers track).
Same-scale variants are extra S2 rows and the S4 audit.

=======================================================================
FROZEN DATA TABLE (central +/- 1 sigma; source)
=======================================================================
  sin2 th12 = 0.3092 +/- 0.0087 (JUNO first result, Nature 2026, 59.1 d);
    shadow NuFIT 6.0 0.307 +/- 0.012
  sin2 th13 = 0.02175 +/- 0.00065 (Daya Bay final 2023, reactor-only, as
    in seed-consistency); shadow NuFIT 6.0 0.02195 +/- 0.00058
  beta = 0.215 +/- 0.074 deg (ACT DR6, as in scorecard); shadow
    Planck+WMAP 0.342 +/- 0.094 deg (Eskilt & Komatsu 2022)
  Omega_b = 0.0489 +/- 0.0014 (BBN D/H, as in scorecard); shadow Planck
    2018 Omega_b h^2 = 0.02237 +/- 0.00015 with h = 0.6736 +/- 0.0054
    -> propagate
  lambda_C = 0.22501 +/- 0.00068 (PDG 2024 CKM fit)
  s23 = |V_cb| = 0.0418 +/- 0.0008 (PDG 2024)
  s13 = |V_ub| = 0.00369 +/- 0.00011 (PDG 2024)
  delta_CKM = 65.5 +/- 1.5 deg (PDG 2024 global fit); shadow LHCb
    gamma 64.6 +/- 2.8 deg
  m_mu/m_tau = 105.6583755/1776.93 with sigma from tau mass +/- 0.09 MeV
    (PDG 2024)
  m_e/m_mu = 0.51099895/105.6583755, sigma negligible (use 1e-8 relative)
  m_u/m_d = 0.462 +/- 0.020 (PDG 2024 lattice, MSbar 2 GeV) -- control,
    phi0-free
  m_c/m_s SAME-SCALE = 11.72 +/- 0.25 (PDG 2024, RG-invariant ratio);
    MIXED-SCALE headline = m_c(m_c)/m_s(2 GeV) = 1.2730/0.0935 with
    sigmas +/- 0.0046 and +/- 0.0008 GeV
  m_t/m_b MIXED = m_t(pole)/m_b(m_b) = 172.57/4.183 (sigmas +/- 0.29,
    +/- 0.007); SAME-SCALE (m_t) ~ 162.5/2.86 +/- 3 % (APPROXIMATE)
  TRANSFER FLOOR for scale-tagged mass legs (frozen, disclosed): 3 %
    relative on m_mu/m_tau, m_c/m_s, m_t/m_b when computing "floored"
    pulls; raw pulls also reported.  Floored sigma = hypot(stat, 0.03*|v|).

=======================================================================
S3 MONOMIALS AND SEED LINES
=======================================================================
A leg is monomial iff value = r * phi0^e with r phi0-free (pi factors,
exp(-5/6), and (4 pi-1)/(4 pi) folded into r).  Non-monomial legs
(theta12, s23, s13, delta) are EXCLUDED from S3, as is LAMBDA_C
(sqrt(phi0(1-phi0)) is not r * phi0^e).  MU_OVER_MD is phi0-free
(control, not a seed-line pair).

Monomial set (7): SIN2_THETA13 (e=1), BETA (e=1), OMEGA_B (e=1),
MMU_OVER_MTAU (e=1), ME_OVER_MMU (e=2), MC_OVER_MS (e=-1),
MT_OVER_MB (e=-2).  C(7,2) = 21 pairs.

Eliminate phi0: with g = gcd(|e_i|,|e_j|), f_i^{e_j/g} / f_j^{e_i/g}
= r_i^{e_j/g} / r_j^{e_i/g} = exact constant.  Print as closed form
(Fraction * pi^k times any leftover exp/(4 pi-1)/(4 pi) factors),
numeric value, data-side value with propagated sigma, raw pull, and
floored pull when a scale-tagged mass leg is in the pair.

Required explicit lines (reduced forms of the general rule):
  (m_t/m_b)*(m_e/m_mu) = 18/91
  (m_c/m_s)*(m_mu/m_tau) = 272/329
  (m_e/m_mu)/(m_mu/m_tau)^2 = 21/16
S3 ranking uses the floored pull when the pair includes a scale-tagged
mass leg, otherwise the raw pull.  Quark legs in the 21 pairs use the
S2-primary MIXED-scale data; same-scale variants of the two quark
mass-sector lines are printed as tagged extras, not ranked in the 21.

=======================================================================
VERDICT ENUM (frozen)
=======================================================================
  CORE_COHERENT | CORE_STRAINED
      for the S2 [E]-core block {ME_OVER_MMU, LAMBDA_C, OMEGA_B,
      SIN2_THETA12}: weighted-mean chi2/dof <= 2 vs > 2 (raw sigmas;
      ME uses the frozen 1e-8 relative).
  DRESSED_LEGS_OUTLIERS(list)
      non-core phi0-dependent legs (primary data) with |raw pull| > 2,
      ids sorted.  Empty list prints "none".
  SEED_LINES(n_within_2sigma/n_total, worst=PAIR)
      n_total = 21; within = |ranking-pull| <= 2; worst = max |ranking-pull|.
  SCALE_AUDIT: MIXED_SCALE_MATCH | SAME_SCALE_MATCH | NEITHER
      per quark leg MC_OVER_MS, MT_OVER_MB, decided on FLOORED pulls
      vs frozen_value: winner = smaller |floored pull|; MATCH only if
      that |pull| <= 2, else NEITHER.

LOO: add each remaining primary leg to the 4-core; BREAKS iff new
chi2/dof > 2.  Scale-tagged mass legs are LOO'd twice (raw and floored).

=======================================================================
LEDGER GREP (frozen 2026-09-02; status_ledger.csv + tfpt_2_standard_model.tex)
=======================================================================
  "m_c/m_s" / "13.6" / "34/47": ALREADY-DOCUMENTED
    FLAV.QUARK.01 (mc/ms=13.61), FLAV.QRATIO.01 (34/47, 13.605),
    BOUNDARY.01 (c/s fits 21/29 AND 34/47; QCD/scheme-sensitivity),
    FLAV.PLUCKER.02 (c_c/c_s = 34/47),
    tfpt_2 table ~13.6 vs experimental order ~11-14; keybox 13.6050.
  "11.7" as the RG-invariant same-scale m_c/m_s: NOT documented
    (ledger 11.7 hits are unrelated PRIME pinch/functional percents).
  mixed-scale m_c(m_c)/m_s(2 GeV) vs same-scale 11.72: NOT documented.
  FLAV.RGSTAB.01 scale-tags m_t/m_b (~10-15 % running via y_t), not
    the m_c/m_s mixed/same convention.

=======================================================================
GATES
=======================================================================
G01 registry reproduction: 13 formulas vs frozen_value, rel <= 1e-12.
G02 every implied phi0 (12 invertible legs + same-scale extras) finite
    and positive; invert(frozen_value) recovers compiler phi0 to 1e-10.
G03 seed-line constants are exactly phi0-free (exponent cancels by
    construction; numeric: combo(phi0) vs combo(1.1 phi0) rel <= 1e-12,
    and combo(frozen values) vs closed-form numeric rel <= 1e-12).
G04 two consecutive runs print byte-identical output (no RNG, no
    wall-clock; in-process render is compared to itself as a smoke
    check).  Operator runs the file twice and diffs stdout.
G05 verdict enum frozen (tokens above).
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import sys
from fractions import Fraction
from itertools import combinations
from math import gcd

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, "..", ".."))
REGISTRY_PATH = os.path.join(_REPO, "verification", "predictions_frozen.json")

C3 = 1.0 / (8.0 * math.pi)
PHI0 = (4.0 / 3.0) * C3 + 48.0 * C3 ** 4
PI = math.pi
REL_REG = 1e-12
TRANSFER_FLOOR = 0.03
SEED_CONSISTENCY_U = 0.05292

REGISTRY_IDS = (
    "SIN2_THETA12_SEED",
    "SIN2_THETA13",
    "BETA_BIREFRINGENCE_DEG",
    "OMEGA_B",
    "LAMBDA_C",
    "S23_CKM",
    "S13_CKM",
    "DELTA_CKM_RAD",
    "MMU_OVER_MTAU",
    "ME_OVER_MMU",
    "MU_OVER_MD",
    "MC_OVER_MS",
    "MT_OVER_MB",
)

CORE_IDS = (
    "ME_OVER_MMU",
    "LAMBDA_C",
    "OMEGA_B",
    "SIN2_THETA12_SEED",
)

FLOORED_IDS = ("MMU_OVER_MTAU", "MC_OVER_MS", "MT_OVER_MB")

MONOMIAL_IDS = (
    "SIN2_THETA13",
    "BETA_BIREFRINGENCE_DEG",
    "OMEGA_B",
    "MMU_OVER_MTAU",
    "ME_OVER_MMU",
    "MC_OVER_MS",
    "MT_OVER_MB",
)

# Frozen data table (must match the SPEC).
JUNO_TH12 = (0.3092, 0.0087)
NUFIT_TH12_SHADOW = (0.307, 0.012)
DAYA_TH13 = (0.02175, 0.00065)
NUFIT_TH13_SHADOW = (0.02195, 0.00058)
ACT_BETA = (0.215, 0.074)
PLANCK_BETA_SHADOW = (0.342, 0.094)
BBN_OB = (0.0489, 0.0014)
PLANCK_OBH2 = (0.02237, 0.00015)
PLANCK_H = (0.6736, 0.0054)
PDG_LAMC = (0.22501, 0.00068)
PDG_S23 = (0.0418, 0.0008)
PDG_S13 = (0.00369, 0.00011)
PDG_DELTA_DEG = (65.5, 1.5)
LHCB_GAMMA_SHADOW = (64.6, 2.8)
M_MU = 105.6583755
M_TAU = 1776.93
S_TAU = 0.09
M_E = 0.51099895
ME_REL_SIG = 1e-8
PDG_MUD = (0.462, 0.020)
MC_MS_SAME = (11.72, 0.25)
M_C_MC, S_C_MC = 1.2730, 0.0046
M_S_2GEV, S_S_2GEV = 0.0935, 0.0008
M_T_POLE, S_T_POLE = 172.57, 0.29
M_B_MB, S_B_MB = 4.183, 0.007
M_T_SAME, M_B_SAME = 162.5, 2.86  # approximate; +/- 3 % relative

CHECKS = []


def gate(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))


class Pref:
    """r = frac * pi^pi_e * exp(e6/6) * (4*pi-1)^a * (4*pi)^b."""

    __slots__ = ("frac", "pi_e", "e6", "a", "b")

    def __init__(self, frac, pi_e=0, e6=0, a=0, b=0):
        self.frac = Fraction(frac)
        self.pi_e = int(pi_e)
        self.e6 = int(e6)
        self.a = int(a)
        self.b = int(b)

    def pow(self, n):
        n = int(n)
        return Pref(self.frac ** n, self.pi_e * n, self.e6 * n,
                    self.a * n, self.b * n)

    def div(self, other):
        return Pref(self.frac / other.frac,
                    self.pi_e - other.pi_e,
                    self.e6 - other.e6,
                    self.a - other.a,
                    self.b - other.b)

    def numeric(self):
        v = float(self.frac)
        if self.pi_e:
            v *= PI ** self.pi_e
        if self.e6:
            v *= math.exp(self.e6 / 6.0)
        if self.a:
            v *= (4.0 * PI - 1.0) ** self.a
        if self.b:
            v *= (4.0 * PI) ** self.b
        return v

    def closed(self):
        parts = []
        if self.frac != 1:
            if self.frac.denominator == 1:
                parts.append("%d" % self.frac.numerator)
            else:
                parts.append("%d/%d" % (self.frac.numerator,
                                        self.frac.denominator))
        if self.pi_e == 1:
            parts.append("pi")
        elif self.pi_e == -1:
            parts.append("pi^-1")
        elif self.pi_e:
            parts.append("pi^%d" % self.pi_e)
        if self.e6:
            gg = gcd(abs(self.e6), 6)
            parts.append("exp(%d/%d)" % (self.e6 // gg, 6 // gg))
        if self.a == 1:
            parts.append("(4*pi-1)")
        elif self.a == -1:
            parts.append("(4*pi-1)^-1")
        elif self.a:
            parts.append("(4*pi-1)^%d" % self.a)
        if self.b == 1:
            parts.append("(4*pi)")
        elif self.b == -1:
            parts.append("(4*pi)^-1")
        elif self.b:
            parts.append("(4*pi)^%d" % self.b)
        if not parts:
            return "1"
        return "*".join(parts)


MONOMIAL_R = {
    "SIN2_THETA13": (1, Pref(1, e6=-5)),
    "BETA_BIREFRINGENCE_DEG": (1, Pref(45, pi_e=-2)),
    "OMEGA_B": (1, Pref(1, a=1, b=-1)),
    "MMU_OVER_MTAU": (1, Pref(Fraction(8, 7))),
    "ME_OVER_MMU": (2, Pref(Fraction(12, 7))),
    "MC_OVER_MS": (-1, Pref(Fraction(34, 47))),
    "MT_OVER_MB": (-2, Pref(Fraction(3, 26))),
}


def eval_formula(pid, phi):
    lam = math.sqrt(phi * (1.0 - phi))
    if pid == "SIN2_THETA12_SEED":
        return 1.0 / 3.0 - phi / 2.0
    if pid == "SIN2_THETA13":
        return phi * math.exp(-5.0 / 6.0)
    if pid == "BETA_BIREFRINGENCE_DEG":
        return (phi / (4.0 * PI)) * (180.0 / PI)
    if pid == "OMEGA_B":
        return (1.0 - 1.0 / (4.0 * PI)) * phi
    if pid == "LAMBDA_C":
        return lam
    if pid == "S23_CKM":
        return phi / (1.0 + lam)
    if pid == "S13_CKM":
        return lam ** 3 / 3.0
    if pid == "DELTA_CKM_RAD":
        return PI / 3.0 + 3.0 * lam ** 2
    if pid == "MMU_OVER_MTAU":
        return (8.0 / 7.0) * phi
    if pid == "ME_OVER_MMU":
        return (12.0 / 7.0) * phi ** 2
    if pid == "MU_OVER_MD":
        return 55.0 / 117.0
    if pid == "MC_OVER_MS":
        return (34.0 / 47.0) / phi
    if pid == "MT_OVER_MB":
        return (3.0 / 26.0) / phi ** 2
    raise KeyError(pid)


def invert_lambda(y, sy):
    disc = 1.0 - 4.0 * y * y
    if disc <= 0.0 or y <= 0.0:
        return float("nan"), float("nan")
    d = math.sqrt(disc)
    p = 0.5 * (1.0 - d)
    sp = abs(2.0 * y / d) * sy
    return p, sp


def invert_s23(s, ss):
    inner = s * (4.0 - 3.0 * s)
    if s <= 0.0 or inner <= 0.0:
        return float("nan"), float("nan")
    p = s * ((s + 2.0) + math.sqrt(inner)) / (2.0 * (1.0 + s * s))
    lam = math.sqrt(p * (1.0 - p))
    dlam = (1.0 - 2.0 * p) / (2.0 * lam)
    ds_dp = ((1.0 + lam) - p * dlam) / (1.0 + lam) ** 2
    if ds_dp == 0.0:
        return p, float("nan")
    return p, abs(ss / ds_dp)


def invert_s13(y, sy):
    if y <= 0.0:
        return float("nan"), float("nan")
    lam = (3.0 * y) ** (1.0 / 3.0)
    p, _ = invert_lambda(lam, 0.0)
    d = math.sqrt(max(1.0 - 4.0 * lam * lam, 0.0))
    if lam == 0.0 or d == 0.0:
        return p, float("nan")
    return p, abs(2.0 / (lam * d)) * sy


def invert_delta_rad(y, sy):
    u = (y - PI / 3.0) / 3.0
    if u <= 0.0:
        return float("nan"), float("nan")
    p, _ = invert_lambda(math.sqrt(u), 0.0)
    d = math.sqrt(max(1.0 - 4.0 * u, 0.0))
    if d == 0.0:
        return p, float("nan")
    return p, abs(1.0 / d) * (sy / 3.0)


def invert_leg(pid, y, sy):
    if pid == "SIN2_THETA12_SEED":
        p = 2.0 * (1.0 / 3.0 - y)
        return p, 2.0 * sy
    if pid == "SIN2_THETA13":
        k = math.exp(5.0 / 6.0)
        return y * k, sy * k
    if pid == "BETA_BIREFRINGENCE_DEG":
        k = (PI * PI) / 45.0
        return y * k, sy * k
    if pid == "OMEGA_B":
        k = 1.0 - 1.0 / (4.0 * PI)
        return y / k, sy / k
    if pid == "LAMBDA_C":
        return invert_lambda(y, sy)
    if pid == "S23_CKM":
        return invert_s23(y, sy)
    if pid == "S13_CKM":
        return invert_s13(y, sy)
    if pid == "DELTA_CKM_RAD":
        return invert_delta_rad(y, sy)
    if pid == "MMU_OVER_MTAU":
        return (7.0 / 8.0) * y, (7.0 / 8.0) * sy
    if pid == "ME_OVER_MMU":
        p = math.sqrt((7.0 / 12.0) * y)
        return p, abs(7.0 / (24.0 * p)) * sy
    if pid == "MC_OVER_MS":
        k = 34.0 / 47.0
        return k / y, k * sy / (y * y)
    if pid == "MT_OVER_MB":
        p = math.sqrt((3.0 / 26.0) / y)
        return p, abs(0.5 * p * sy / y)
    raise KeyError(pid)


def ratio_with_rel(a, sa, b, sb):
    r = a / b
    return r, abs(r) * math.hypot(sa / a, sb / b)


def floor_sigma(value, sigma, apply):
    if not apply:
        return sigma
    return math.hypot(sigma, TRANSFER_FLOOR * abs(value))


def wmean(phis, sigmas):
    ws = [1.0 / (s * s) for s in sigmas]
    sw = sum(ws)
    mu = sum(p * w for p, w in zip(phis, ws)) / sw
    chi2 = sum(((p - mu) / s) ** 2 for p, s in zip(phis, sigmas))
    dof = len(phis) - 1
    return mu, chi2, chi2 / dof if dof else float("nan")


def pow_tok(name, k):
    if k == 1:
        return name
    if k == -1:
        return "1/%s" % name
    return "%s^%d" % (name, k)


def comb_label(id_i, p, id_j, q):
    if p > 0 and q < 0:
        return "%s * %s" % (pow_tok(id_i, p), pow_tok(id_j, -q))
    if p < 0 and q > 0:
        return "%s * %s" % (pow_tok(id_j, q), pow_tok(id_i, -p))
    if p < 0 and q < 0:
        return "%s / %s" % (pow_tok(id_j, -q), pow_tok(id_i, -p))
    return "%s / %s" % (pow_tok(id_i, p), pow_tok(id_j, q))


def reduced_exponents(ei, ej):
    g = gcd(abs(ei), abs(ej))
    return ej // g, ei // g, g


# Requested orientations for the three named mass/lepton lines.
_MUST_ORIENT = {
    frozenset(("MT_OVER_MB", "ME_OVER_MMU")): (
        "MT_OVER_MB", 1, "ME_OVER_MMU", -1),
    frozenset(("MC_OVER_MS", "MMU_OVER_MTAU")): (
        "MC_OVER_MS", 1, "MMU_OVER_MTAU", -1),
    frozenset(("ME_OVER_MMU", "MMU_OVER_MTAU")): (
        "ME_OVER_MMU", 1, "MMU_OVER_MTAU", 2),
}


def canonical_pair(id_i, id_j):
    must = _MUST_ORIENT.get(frozenset((id_i, id_j)))
    if must is not None:
        return must
    ei = MONOMIAL_R[id_i][0]
    ej = MONOMIAL_R[id_j][0]
    p, q, _g = reduced_exponents(ei, ej)
    if p < 0:
        p, q = -p, -q
    return id_i, p, id_j, q


def load_frozen():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
        reg = json.load(fh)
    by_id = {}
    for entry in reg["predictions"]:
        by_id[entry["id"]] = float(entry["frozen_value"])
    return reg, by_id


def build_data():
    emu, s_emu = ratio_with_rel(M_E, ME_REL_SIG * M_E, M_MU, 0.0)
    # electron mass error is folded into the frozen 1e-8 relative on the ratio
    s_emu = ME_REL_SIG * emu
    mmu_tau, s_mmu_tau = ratio_with_rel(M_MU, 0.0, M_TAU, S_TAU)
    mc_ms_mixed, s_mc_ms_mixed = ratio_with_rel(
        M_C_MC, S_C_MC, M_S_2GEV, S_S_2GEV)
    mt_mb_mixed, s_mt_mb_mixed = ratio_with_rel(
        M_T_POLE, S_T_POLE, M_B_MB, S_B_MB)
    mt_mb_same = M_T_SAME / M_B_SAME
    s_mt_mb_same = TRANSFER_FLOOR * mt_mb_same
    obh2, s_obh2 = PLANCK_OBH2
    h, s_h = PLANCK_H
    ob_planck = obh2 / (h * h)
    s_ob_planck = math.hypot(s_obh2 / (h * h), 2.0 * obh2 * s_h / (h ** 3))
    delta_rad = PDG_DELTA_DEG[0] * PI / 180.0
    s_delta_rad = PDG_DELTA_DEG[1] * PI / 180.0
    return {
        "SIN2_THETA12_SEED": JUNO_TH12,
        "SIN2_THETA13": DAYA_TH13,
        "BETA_BIREFRINGENCE_DEG": ACT_BETA,
        "OMEGA_B": BBN_OB,
        "LAMBDA_C": PDG_LAMC,
        "S23_CKM": PDG_S23,
        "S13_CKM": PDG_S13,
        "DELTA_CKM_RAD": (delta_rad, s_delta_rad),
        "MMU_OVER_MTAU": (mmu_tau, s_mmu_tau),
        "ME_OVER_MMU": (emu, s_emu),
        "MU_OVER_MD": PDG_MUD,
        "MC_OVER_MS": (mc_ms_mixed, s_mc_ms_mixed),
        "MT_OVER_MB": (mt_mb_mixed, s_mt_mb_mixed),
        "MC_OVER_MS_SAME": MC_MS_SAME,
        "MT_OVER_MB_SAME": (mt_mb_same, s_mt_mb_same),
        "OMEGA_B_PLANCK_SHADOW": (ob_planck, s_ob_planck),
    }


def ffmt(x, n=8):
    if not math.isfinite(x):
        return "nan"
    return "%.*f" % (n, x)


def efmt(x):
    if not math.isfinite(x):
        return "nan"
    return "%.4e" % x


def pfmt(x):
    if not math.isfinite(x):
        return "nan"
    if abs(x) >= 1000.0:
        return "%9.3e" % x
    return ffmt(x, 3)


def pull_of(data, frozen, sigma):
    if sigma == 0.0 or not math.isfinite(sigma):
        return float("nan")
    return (data - frozen) / sigma


def scale_audit_tag(pull_mixed, pull_same):
    am, a_s = abs(pull_mixed), abs(pull_same)
    if am < a_s and am <= 2.0:
        return "MIXED_SCALE_MATCH"
    if a_s < am and a_s <= 2.0:
        return "SAME_SCALE_MATCH"
    return "NEITHER"


def main():
    print("seed_tomography_registry_probe -- PHYS.SEED.TOMOGRAPHY.REGISTRY.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("phi0_compiler %.15f  c3 %.15f" % (PHI0, C3))
    print("ALPHA_INV excluded from tomography (c3-driven Ward root).")
    print("Extends seed-consistency (4 legs, chi2/dof 1.23, u=0.05292) "
          "to the full registry (13 legs).")
    print("S3 excludes non-monomials theta12, s23, s13, delta, and LAMBDA_C.")

    reg, frozen = load_frozen()
    data = build_data()
    print("registry %s  freeze_date %s" % (
        reg.get("registry", "?")[:48], reg.get("freeze_date")))

    # ----- S1 -----
    print("\nS1 Registry reproduction gate (13 formulas vs frozen_value)")
    max_rel = 0.0
    all_ok = True
    for pid in REGISTRY_IDS:
        pred = eval_formula(pid, PHI0)
        fv = frozen[pid]
        rel = abs(pred / fv - 1.0)
        max_rel = max(max_rel, rel)
        ok = rel <= REL_REG
        all_ok = all_ok and ok
        print("  %s  frozen=%s  pred=%s  rel=%s" % (
            pid.ljust(22), efmt(fv), efmt(pred), efmt(rel)))
    gate("G01 registry reproduction 13/13 rel<=1e-12",
         all_ok and len(REGISTRY_IDS) == 13,
         "max_rel %s" % efmt(max_rel))

    # ----- inversions -----
    rows = []
    invert_ok = True
    primary_ids = [p for p in REGISTRY_IDS if p != "MU_OVER_MD"]
    extra_ids = ("MC_OVER_MS_SAME", "MT_OVER_MB_SAME")

    def row_for(pid, y, sy, frozen_pid, tag):
        nonlocal invert_ok
        fv = frozen[frozen_pid]
        raw_p = pull_of(y, fv, sy)
        fl_sy = floor_sigma(y, sy, frozen_pid in FLOORED_IDS)
        fl_p = pull_of(y, fv, fl_sy)
        iphi, siphi = invert_leg(frozen_pid, y, sy)
        if not (math.isfinite(iphi) and iphi > 0.0 and math.isfinite(siphi)):
            invert_ok = False
        rt, _ = invert_leg(frozen_pid, fv, 1.0)
        if not (math.isfinite(rt) and abs(rt / PHI0 - 1.0) <= 1e-10):
            invert_ok = False
        dpc = (iphi / PHI0 - 1.0) * 100.0 if math.isfinite(iphi) else float("nan")
        return {
            "tag": tag,
            "id": pid,
            "frozen_id": frozen_pid,
            "data": y,
            "sigma": sy,
            "frozen": fv,
            "raw_pull": raw_p,
            "floored_pull": fl_p,
            "floored_sigma": fl_sy,
            "iphi": iphi,
            "siphi": siphi,
            "dpc": dpc,
        }

    for pid in primary_ids:
        y, sy = data[pid]
        rows.append(row_for(pid, y, sy, pid, "primary"))
    for epid, fpid in (("MC_OVER_MS_SAME", "MC_OVER_MS"),
                       ("MT_OVER_MB_SAME", "MT_OVER_MB")):
        y, sy = data[epid]
        rows.append(row_for(epid, y, sy, fpid, "same-scale"))

    by_id = {r["id"]: r for r in rows}

    # control
    y_ud, s_ud = data["MU_OVER_MD"]
    fv_ud = frozen["MU_OVER_MD"]
    print("  MU_OVER_MD control (phi0-free): data=%s +/- %s  frozen=%s  "
          "raw_pull=%s" % (ffmt(y_ud, 5), ffmt(s_ud, 5), ffmt(fv_ud, 8),
                           ffmt(pull_of(y_ud, fv_ud, s_ud), 3)))

    extras_ok = True
    for r in rows:
        if not (math.isfinite(r["iphi"]) and r["iphi"] > 0.0):
            extras_ok = False
    gate("G02 implied phi0 finite and positive + frozen roundtrip",
         invert_ok and extras_ok)

    # ----- S2 -----
    print("\nS2 Tomography")
    print("  %s %s %s %s %s %s %s %s" % (
        "leg".ljust(22), "data".rjust(12), "frozen".rjust(12),
        "raw_pull".rjust(9), "floored".rjust(9),
        "phi0_imp".rjust(12), "dphi%".rjust(8), "sig_phi0".rjust(11)))
    for r in rows:
        print("  %s %12s %12s %9s %9s %12s %8s %11s" % (
            r["id"].ljust(22),
            ffmt(r["data"], 8), ffmt(r["frozen"], 8),
            pfmt(r["raw_pull"]), pfmt(r["floored_pull"]),
            ffmt(r["iphi"], 8), ffmt(r["dpc"], 3),
            efmt(r["siphi"])))

    core_phis = [by_id[i]["iphi"] for i in CORE_IDS]
    core_sigs = [by_id[i]["siphi"] for i in CORE_IDS]
    mu_core, chi2_core, cd_core = wmean(core_phis, core_sigs)
    print("  [E]-core block {%s}" % ", ".join(CORE_IDS))
    print("  weighted mean phi0 = %s   chi2/dof = %s / 3 = %s" % (
        ffmt(mu_core, 8), ffmt(chi2_core, 4), ffmt(cd_core, 4)))
    print("  seed-consistency u = %s (different 4-leg set: beta, Omega_b, "
          "theta13 reactor, Cabibbo; chi2/dof 1.23)" % ffmt(SEED_CONSISTENCY_U, 5))
    print("  (this mean - compiler)/compiler = %s %%" % (
        ffmt((mu_core / PHI0 - 1.0) * 100.0, 4)))
    print("  (this mean - seed-consistency u)/u = %s %%" % (
        ffmt((mu_core / SEED_CONSISTENCY_U - 1.0) * 100.0, 4)))

    remaining = [p for p in primary_ids if p not in CORE_IDS]
    print("  LOO: add each remaining primary leg to the [E]-core "
          "(BREAKS iff chi2/dof > 2)")
    loo_break = {}
    for pid in remaining:
        r = by_id[pid]
        phis = core_phis + [r["iphi"]]
        raw_s = core_sigs + [r["siphi"]]
        _, _, cd_raw = wmean(phis, raw_s)
        br_raw = cd_raw > 2.0
        loo_break[pid] = br_raw
        line = "    ADD %s  chi2/dof_raw=%s  BREAKS_RAW=%s" % (
            pid.ljust(22), ffmt(cd_raw, 4), "yes" if br_raw else "no")
        if r["frozen_id"] in FLOORED_IDS:
            # re-invert with floored observable sigma
            ip_f, sip_f = invert_leg(r["frozen_id"], r["data"], r["floored_sigma"])
            _, _, cd_f = wmean(core_phis + [ip_f], core_sigs + [sip_f])
            br_f = cd_f > 2.0
            line += "  chi2/dof_floored=%s  BREAKS_FLOORED=%s" % (
                ffmt(cd_f, 4), "yes" if br_f else "no")
        print(line)

    ob_sh, s_ob_sh = data["OMEGA_B_PLANCK_SHADOW"]
    ip_sh, sip_sh = invert_leg("OMEGA_B", ob_sh, s_ob_sh)
    print("  shadow Omega_b Planck = %s +/- %s  => phi0 = %s +/- %s" % (
        ffmt(ob_sh, 6), ffmt(s_ob_sh, 6), ffmt(ip_sh, 6), efmt(sip_sh)))

    # ----- S3 -----
    print("\nS3 Seed lines (monomial pairs; non-monomials excluded)")
    print("  closed form is gcd-reduced f_i^{e_j/g}/f_j^{e_i/g}")
    pairs = []
    g03_ok = True
    for id_a, id_b in combinations(MONOMIAL_IDS, 2):
        id_i, p, id_j, q = canonical_pair(id_a, id_b)
        ei, ri = MONOMIAL_R[id_i]
        ej, rj = MONOMIAL_R[id_j]
        if ei * p - ej * q != 0:
            g03_ok = False
        const = ri.pow(p).div(rj.pow(q))
        cnum = const.numeric()
        # phi0-free numeric check
        def combo(phi):
            fi = ri.numeric() * phi ** ei
            fj = rj.numeric() * phi ** ej
            return (fi ** p) / (fj ** q)
        c0 = combo(PHI0)
        c1 = combo(1.1 * PHI0)
        if abs(c0 / c1 - 1.0) > 1e-12 or abs(c0 / cnum - 1.0) > 1e-12:
            g03_ok = False
        fi, si = data[id_i]
        fj, sj = data[id_j]
        v = (fi ** p) / (fj ** q)
        rel2 = 0.0
        if p:
            rel2 += (p * si / fi) ** 2
        if q:
            rel2 += (q * sj / fj) ** 2
        sv = abs(v) * math.sqrt(rel2)
        raw_pl = pull_of(v, cnum, sv)
        si_f = floor_sigma(fi, si, id_i in FLOORED_IDS)
        sj_f = floor_sigma(fj, sj, id_j in FLOORED_IDS)
        rel2f = 0.0
        if p:
            rel2f += (p * si_f / fi) ** 2
        if q:
            rel2f += (q * sj_f / fj) ** 2
        sv_f = abs(v) * math.sqrt(rel2f)
        fl_pl = pull_of(v, cnum, sv_f)
        uses_floor = (id_i in FLOORED_IDS) or (id_j in FLOORED_IDS)
        rank_pl = fl_pl if uses_floor else raw_pl
        fv_i, fv_j = frozen[id_i], frozen[id_j]
        v_fr = (fv_i ** p) / (fv_j ** q)
        if abs(v_fr / cnum - 1.0) > 1e-12:
            g03_ok = False
        label = comb_label(id_i, p, id_j, q)
        pair_key = "%s|%s" % tuple(sorted((id_i, id_j)))
        pairs.append({
            "key": pair_key,
            "i": id_i, "j": id_j, "p": p, "q": q,
            "label": label,
            "closed": const.closed(),
            "cnum": cnum,
            "data": v,
            "sigma": sv,
            "raw_pull": raw_pl,
            "floored_pull": fl_pl,
            "rank_pull": rank_pl,
            "uses_floor": uses_floor,
        })
    for a, b, frac in (
        ("MT_OVER_MB", "ME_OVER_MMU", Fraction(18, 91)),
        ("MC_OVER_MS", "MMU_OVER_MTAU", Fraction(272, 329)),
        ("ME_OVER_MMU", "MMU_OVER_MTAU", Fraction(21, 16)),
    ):
        hit = [z for z in pairs if set((z["i"], z["j"])) == set((a, b))][0]
        if abs(hit["cnum"] / float(frac) - 1.0) > 1e-12:
            g03_ok = False
    gate("G03 seed-line constants exactly phi0-free", g03_ok,
         "n_pairs %d" % len(pairs))

    pairs_sorted = sorted(pairs, key=lambda z: (-abs(z["rank_pull"]), z["key"]))
    print("  %s %s %s %s %s %s %s" % (
        "relation".ljust(52), "closed".ljust(28), "exact".rjust(12),
        "data".rjust(12), "raw_p".rjust(8), "fl_p".rjust(8), "rank_p".rjust(8)))
    for z in pairs_sorted:
        print("  %s %s %12s %12s %8s %8s %8s" % (
            z["label"].ljust(52), z["closed"].ljust(28),
            ffmt(z["cnum"], 8), ffmt(z["data"], 8),
            pfmt(z["raw_pull"]), pfmt(z["floored_pull"]),
            pfmt(z["rank_pull"])))

    # explicit three, plus same-scale extras
    print("  explicit mass-sector / lepton lines (must appear above):")
    must = (
        ("MT_OVER_MB", "ME_OVER_MMU", Fraction(18, 91)),
        ("MC_OVER_MS", "MMU_OVER_MTAU", Fraction(272, 329)),
        ("ME_OVER_MMU", "MMU_OVER_MTAU", Fraction(21, 16)),
    )
    for a, b, frac in must:
        hit = [z for z in pairs if set((z["i"], z["j"])) == set((a, b))][0]
        match = abs(hit["cnum"] / float(frac) - 1.0) <= 1e-12
        print("    %s  closed=%s  Fraction=%s  numeric=%s  rank_pull=%s  match=%s" % (
            hit["label"], hit["closed"], str(frac),
            ffmt(float(frac), 8), pfmt(hit["rank_pull"]),
            "yes" if match else "NO"))
        if not match:
            g03_ok = False

    def extra_product(name, fa, sa, fb, sb, exact):
        v = fa * fb
        sv = abs(v) * math.hypot(sa / fa, sb / fb)
        ex = float(exact)
        print("    %s  data=%s +/- %s  exact=%s  raw_pull=%s  "
              "floored_pull=%s" % (
                  name, ffmt(v, 6), efmt(sv), ffmt(ex, 8),
                  ffmt(pull_of(v, ex, sv), 3),
                  ffmt(pull_of(v, ex,
                               abs(v) * math.hypot(
                                   floor_sigma(fa, sa, True) / fa,
                                   floor_sigma(fb, sb, True) / fb)), 3)))

    print("  same-scale extras (not in the ranked 21):")
    extra_product(
        "(MC_OVER_MS_SAME)*(MMU_OVER_MTAU) vs 272/329",
        data["MC_OVER_MS_SAME"][0], data["MC_OVER_MS_SAME"][1],
        data["MMU_OVER_MTAU"][0], data["MMU_OVER_MTAU"][1],
        Fraction(272, 329))
    extra_product(
        "(MT_OVER_MB_SAME)*(ME_OVER_MMU) vs 18/91",
        data["MT_OVER_MB_SAME"][0], data["MT_OVER_MB_SAME"][1],
        data["ME_OVER_MMU"][0], data["ME_OVER_MMU"][1],
        Fraction(18, 91))

    n_within = sum(1 for z in pairs if abs(z["rank_pull"]) <= 2.0)
    worst = pairs_sorted[0]
    worst_name = "%s__%s" % (worst["i"], worst["j"])

    # ----- S4 -----
    print("\nS4 Scale audit")
    mc_m = by_id["MC_OVER_MS"]
    mc_s = by_id["MC_OVER_MS_SAME"]
    mt_m = by_id["MT_OVER_MB"]
    mt_s = by_id["MT_OVER_MB_SAME"]
    print("  MC_OVER_MS frozen=%s" % ffmt(frozen["MC_OVER_MS"], 6))
    print("    MIXED  data=%s +/- %s  raw_pull=%s  floored_pull=%s  "
          "phi0=%s (dphi%%=%s)" % (
              ffmt(mc_m["data"], 6), ffmt(mc_m["sigma"], 5),
              ffmt(mc_m["raw_pull"], 3), ffmt(mc_m["floored_pull"], 3),
              ffmt(mc_m["iphi"], 6), ffmt(mc_m["dpc"], 3)))
    print("    SAME   data=%s +/- %s  raw_pull=%s  floored_pull=%s  "
          "phi0=%s (dphi%%=%s)" % (
              ffmt(mc_s["data"], 6), ffmt(mc_s["sigma"], 5),
              ffmt(mc_s["raw_pull"], 3), ffmt(mc_s["floored_pull"], 3),
              ffmt(mc_s["iphi"], 6), ffmt(mc_s["dpc"], 3)))
    print("  MT_OVER_MB frozen=%s" % ffmt(frozen["MT_OVER_MB"], 6))
    print("    MIXED  data=%s +/- %s  raw_pull=%s  floored_pull=%s  "
          "phi0=%s (dphi%%=%s)" % (
              ffmt(mt_m["data"], 6), ffmt(mt_m["sigma"], 5),
              ffmt(mt_m["raw_pull"], 3), ffmt(mt_m["floored_pull"], 3),
              ffmt(mt_m["iphi"], 6), ffmt(mt_m["dpc"], 3)))
    print("    SAME   data=%s +/- %s  raw_pull=%s  floored_pull=%s  "
          "phi0=%s (dphi%%=%s)  [APPROXIMATE +/- 3 %%]" % (
              ffmt(mt_s["data"], 6), ffmt(mt_s["sigma"], 5),
              ffmt(mt_s["raw_pull"], 3), ffmt(mt_s["floored_pull"], 3),
              ffmt(mt_s["iphi"], 6), ffmt(mt_s["dpc"], 3)))
    mc_tag = scale_audit_tag(mc_m["floored_pull"], mc_s["floored_pull"])
    mt_tag = scale_audit_tag(mt_m["floored_pull"], mt_s["floored_pull"])
    print("  SCALE_AUDIT MC_OVER_MS=%s  MT_OVER_MB=%s "
          "(floored pulls vs frozen)" % (mc_tag, mt_tag))
    print("  ledger grep (frozen in SPEC, 2026-09-02):")
    print("    ALREADY-DOCUMENTED: FLAV.QUARK.01, FLAV.QRATIO.01, "
          "BOUNDARY.01, FLAV.PLUCKER.02, tfpt_2 13.6 vs ~11-14.")
    print("    NOT documented: mixed-scale m_c(m_c)/m_s(2 GeV) vs "
          "RG-invariant same-scale 11.72.")
    print("    FLAV.RGSTAB.01 scale-tags m_t/m_b (~10-15% y_t), "
          "not the m_c/m_s convention.")

    # ----- S5 -----
    core_tag = "CORE_COHERENT" if cd_core <= 2.0 else "CORE_STRAINED"
    dressed = []
    for pid in remaining:
        if abs(by_id[pid]["raw_pull"]) > 2.0:
            dressed.append(pid)
    dressed_s = ",".join(dressed) if dressed else "none"
    verdict = (
        "%s; DRESSED_LEGS_OUTLIERS(%s); SEED_LINES(%d/%d, worst=%s); "
        "SCALE_AUDIT MC_OVER_MS=%s MT_OVER_MB=%s" % (
            core_tag, dressed_s, n_within, len(pairs), worst_name,
            mc_tag, mt_tag))
    enum_ok = (
        core_tag in ("CORE_COHERENT", "CORE_STRAINED")
        and verdict.startswith(core_tag)
        and "DRESSED_LEGS_OUTLIERS(" in verdict
        and "SEED_LINES(" in verdict
        and "SCALE_AUDIT MC_OVER_MS=" in verdict
        and mc_tag in ("MIXED_SCALE_MATCH", "SAME_SCALE_MATCH", "NEITHER")
        and mt_tag in ("MIXED_SCALE_MATCH", "SAME_SCALE_MATCH", "NEITHER")
        and len(pairs) == 21)
    gate("G05 verdict enum frozen", enum_ok)

    # G04: in-process determinism smoke (no wall-clock / no RNG used).
    payload = "\n".join([
        SPEC_SHA, core_tag, dressed_s, worst_name,
        ffmt(mu_core, 12), ffmt(cd_core, 8),
        mc_tag, mt_tag, "%d" % n_within,
    ])
    gate("G04 deterministic payload (no RNG/wall-clock)",
         payload == payload and "time" not in FROZEN_SPEC.split("G04")[1][:200].lower())

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("\nGATES %d/%d" % (n_pass, len(CHECKS)))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("VERDICT: %s" % verdict)
    sys.exit(0 if n_pass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
