#!/usr/bin/env python3
"""nu-scalaron-falsification -- leptogenesis pass (declared follow-up).

Sends the FROZEN candidate chain (M_R = 3 c3^{7/2} Mbar -> m3 = 0.05124 eV,
hypotheses/nu_scalaron_v1.yaml, SHA 4941b396729636de) through the corpus
BDP Boltzmann solver (verbatim v372 network: D, W_ID, LSODA) and asks the
question the corpus could not ask before the candidate existed:

    The corpus carries TWO M1 conventions --
      (i)  the v212/v372 decuple route   M1 = M_scal phi0^2 / A_Lambda
      (ii) the v184 scenario route       M1 = M_R  phi0^4
    Under the OLD one-parameter window they could not be separated (M_R
    free).  Under the FROZEN candidate M_R = 3 M_scal both are numbers
    with zero dials -- eta_B discriminates them.

Outputs results/leptogenesis.json.  Deterministic (no RNG).

HONEST SCOPE (firewall): the BDP network, the Davidson-Ibarra epsilon with
the predicted delta_CP = 4pi/3, and the washout anchor m~1 = m3/A_Lambda
are the frozen corpus tools (v372, [C] transfer); nothing here is a
compiler output; the candidate stays [C]/[N]; no marker moves.
"""
import json
import math
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import kn

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(ROOT))
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import c3, Mbar, phi0, g_car, N_fam  # noqa: E402

# frozen chain values (must match results/results.json of the v1 pass)
C3, MBARF, PHI0 = float(c3), float(Mbar), float(phi0)
M_SCAL = C3 ** 3.5 * MBARF
M_R = N_fam * M_SCAL
M3_EV = 0.05124                      # candidate-chain m3 (frozen v1 pass)
A_LAMBDA = 2 * g_car                 # 10
MT1_EV = M3_EV / A_LAMBDA            # washout anchor, 5.124 meV
M_STAR_EV = 1.08e-3
A_SPH = 0.96e-2
V_EW = 174.0
ETAB_OBS = 6.1e-10
SIN_EFF = abs(math.sin(4 * math.pi / 3))

K_WASH = MT1_EV / M_STAR_EV


def N1eq(z):
    return 0.5 * z * z * kn(2, z)


def rhs(z, y, K):
    N1, NBL = y
    k1, k2 = kn(1, z), kn(2, z)
    D = K * z * k1 / k2
    W = 0.25 * K * z ** 3 * k1
    src = -D * (N1 - N1eq(z))
    return [src, src - W * NBL]


def kappa_f(K, z0=0.1, z1=25.0):
    sol = solve_ivp(rhs, (z0, z1), [N1eq(z0), 0.0], args=(K,),
                    method="LSODA", rtol=1e-8, atol=1e-12)
    return float(abs(sol.y[1, -1]))


def eps1(M1):
    return (3.0 / (16.0 * math.pi)) * M1 * (M3_EV * 1e-9) / V_EW ** 2 * SIN_EFF


def main():
    kf = kappa_f(K_WASH)
    routes = {
        "v212_decuple  M1 = M_scal phi0^2 / A_Lambda":
            M_SCAL * PHI0 ** 2 / A_LAMBDA,
        "v184_scenario M1 = M_R phi0^4":
            M_R * PHI0 ** 4,
    }
    out = {"project": "nu-scalaron-falsification",
           "pass": "leptogenesis (declared follow-up)",
           "frozen": {"M_R_GeV": M_R, "M_scal_GeV": M_SCAL,
                      "m3_eV": M3_EV, "washout_m1_eV": MT1_EV,
                      "K": K_WASH, "kappa_f_ODE": kf,
                      "delta_CP": "4pi/3 (|sin| = 0.866)"},
           "routes": {}}
    print("BDP ODE: K = %.3f -> kappa_f = %.4f" % (K_WASH, kf))
    for name, M1 in routes.items():
        eta = A_SPH * eps1(M1) * kf
        ratio = eta / ETAB_OBS
        band = 1 / 3.2 <= ratio <= 3.2
        out["routes"][name] = {
            "M1_GeV": M1, "eps1": eps1(M1), "eta_B": eta,
            "eta_over_obs": ratio,
            "inside_band_obs/3..3obs": bool(band),
            "verdict": "consistent" if band else "tension"}
        print("%s: M1 = %.3e GeV -> eta_B = %.2e (x%.2f of obs) %s"
              % (name, M1, eta, ratio,
                 "INSIDE [obs/3, 3 obs]" if band else "OUTSIDE band"))

    # discriminator statement
    r1 = out["routes"]["v212_decuple  M1 = M_scal phi0^2 / A_Lambda"]
    r2 = out["routes"]["v184_scenario M1 = M_R phi0^4"]
    out["discriminator"] = {
        "M1_ratio_decuple_over_scenario": r1["M1_GeV"] / r2["M1_GeV"],
        "statement": ("under the frozen candidate M_R = 3 M_scal the two "
                      "corpus M1 conventions become zero-dial numbers; "
                      "eta_B selects: decuple %s, scenario %s"
                      % (r1["verdict"], r2["verdict"]))}

    # the M1 reproducing the observation exactly (with the ODE efficiency)
    M1_hit = brentq(lambda m: A_SPH * eps1(m) * kf - ETAB_OBS, 1e7, 1e13)
    out["M1_reproducing_obs_GeV"] = M1_hit
    out["M1_hit_over_decuple"] = M1_hit / r1["M1_GeV"]
    out["M1_hit_over_scenario"] = M1_hit / r2["M1_GeV"]
    print("M1 reproducing eta_B_obs exactly: %.3e GeV "
          "(decuple off by x%.2f, scenario off by x%.2f)"
          % (M1_hit, r1["M1_GeV"] / M1_hit, r2["M1_GeV"] / M1_hit))

    out["honest_scope"] = (
        "BDP network + DI epsilon + washout anchor are the frozen v372 "
        "[C] tools; single-flavor, hierarchical N1; no marker move. "
        "HONESTY: v372 already sat at factor 1.07 with its own frozen "
        "inputs -- the candidate chain PRESERVES that hit (1.06), it "
        "does not improve it; the NEW content is the discriminator: "
        "under the frozen M_R the v184 scenario relation M1 = M_R phi0^4 "
        "lands ~11x LOW (outside the band) while the v212 decuple route "
        "stays on target -- the candidate selects the decuple convention")

    path = os.path.join(ROOT, "results", "leptogenesis.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", path)


if __name__ == "__main__":
    main()
