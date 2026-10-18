"""Frozen kernel of the CCC crossover-disc search.

Everything here is DERIVED from TFPT corpus objects + typed external
cosmography and was frozen BEFORE any data contact (rounds DLIII-DLV of
the CCC.SEAM.CROSSOVER exploration thread, 2026-08-24; provenance
probes in experiments/tfpt-discovery/: ccc_kernel_gamma_kms_probe.py,
ccc_transfer_selector_probe.py, ccc_kappa_freeze_probe.py).

The three freeze stages and their SHA-256 prefixes (recomputed and
guarded by tests/test_frozen_kernel.py):

  v1  shape freeze      1df51166d0a2ef5b  (two modes, ratio, sign table)
  v2  geometry freeze   a795401accbebdb4  (rim-ring, theta_max formula)
  v3  kappa freeze      4cafe0457e0e89a1  (derived kappa => causal
                                           top-hat disc template)

No fitted exponents anywhere: the decay constants are exact logarithms
of the seam-transport rationals (2/3)^6 = 64/729 and (1/3)^6 = 1/729.
"""

import hashlib

import numpy as np

# ---------------------------------------------------------------------
# exact seam-transport constants (axiom-derived, v221/v54)
# ---------------------------------------------------------------------
LAM2 = (2.0 / 3.0) ** 6            # 64/729
LAM3 = (1.0 / 3.0) ** 6            # 1/729
DELTA2 = 6 * np.log(1.5)           # ln(729/64)
DELTA3 = 6 * np.log(3.0)           # ln 729
RATE_RATIO = DELTA3 / DELTA2       # ln3/ln(3/2) = 2.709511...

# frozen defect-class overlap table (cusp-weight point defects)
C2_PAIR = 1 / np.sqrt(2.0)         # lambda_2 component, Z2-pair defect
C3_PAIR = 1 / np.sqrt(6.0)         # lambda_3 component, Z2-pair defect
C2_ANCHOR = 0.0                    # Nariai-anchor defect
C3_ANCHOR = -2 / np.sqrt(6.0)

# ---------------------------------------------------------------------
# typed external cosmography (Planck 2018; NOT TFPT outputs)
# ---------------------------------------------------------------------
ETA_REC_MPC = 280.3                # conformal time at recombination
ETA_0_MPC = 14165.0                # conformal time today
H0_KM_S_MPC = 67.4
OMEGA_L = 0.685
OMK_95 = 0.0031                    # closed-side 95% curvature bound
TAU_REC_MPC = 3.8e5 / 3.2616e6    # proper age at recombination (380 kyr)

C_KM_S = 299792.458
D_H_MPC = C_KM_S / H0_KM_S_MPC
R_LAMBDA_MPC = D_H_MPC / np.sqrt(OMEGA_L)
R_CURV_MIN_MPC = D_H_MPC / np.sqrt(OMK_95)


def theta_max_rad():
    """FROZEN FORMULA: causal disc radius of a crossover point defect."""
    return ETA_REC_MPC / (ETA_0_MPC - ETA_REC_MPC)


def theta_max_deg():
    return float(np.degrees(theta_max_rad()))


def kernel_K(u):
    """two-mode relaxation kernel in the flow variable u >= 0."""
    return C2_PAIR * np.exp(-DELTA2 * u) + C3_PAIR * np.exp(-DELTA3 * u)


def u_rec_band():
    """ticks accumulated before recombination, over the declared
    tick-convention band (v526 KMS normalisation, round DLV)."""
    out = {}
    for rname, R in (("R_Lambda", R_LAMBDA_MPC), ("R_c", R_CURV_MIN_MPC)):
        for cname, frac in (("full wrap", 1.0),
                            ("quarter wrap (mu4 step)", 0.25),
                            ("wrap/6 (dyn hand)", 1 / 6.0),
                            ("quarter/6", 1 / 24.0)):
            out[f"{rname}, {cname}"] = TAU_REC_MPC / (2 * np.pi * R * frac)
    return out


def contrast_bound():
    """max radial kernel contrast of the disc across the band."""
    u_max = max(u_rec_band().values())
    return float(1 - kernel_K(u_max) / kernel_K(0.0))


# ---------------------------------------------------------------------
# the three frozen specs (verbatim from the freezing probes)
# ---------------------------------------------------------------------
def spec_v1():
    D2, D3 = DELTA2, DELTA3
    ratio = D3 / D2
    return ("CCC.KERNEL.FREEZE.01|modes=2|"
            f"Delta2=ln(729/64)={D2:.12f}|Delta3=ln(729)={D3:.12f}|"
            f"ratio={ratio:.12f}|pair=(+-{1/np.sqrt(2):.12f},"
            f"+{1/np.sqrt(6):.12f})|anchor=(0,{-2/np.sqrt(6):.12f})|"
            "signrule=c3>0 for pair, sign(c2)=sheet bit|"
            "kills=K1 single-Gaussian, K2 ratio!=sqrt3:1 or 0:-2,"
            " K3 negative c3 for paired defect|"
            "declared_open=u(theta) transfer [C]")


def spec_v2():
    D2, D3, C2, C3 = DELTA2, DELTA3, C2_PAIR, C3_PAIR
    return ("CCC.KERNEL.FREEZE.02|topology=rim-brightened ring|"
            "theta_max=eta_rec/(eta_0-eta_rec) [externals typed]|"
            f"edge rates Delta2={D2:.12f}, Delta3={D3:.12f},"
            f" ratio={D3/D2:.12f}|amplitudes pair=(+-{C2:.12f},"
            f"+{C3:.12f}), anchor=(0,{-2/np.sqrt(6):.12f})|"
            "open=[C] kappa tick length (candidate:"
            " SEAM.THERMAL.KMS.01)|kills=K1..K3 (round DLIII) + K4"
            " centrally-peaked resolved profile + K5 resolved ring"
            " edge-ratio != 2.7095")


def spec_v3():
    theta_deg = theta_max_deg()
    u_max = max(u_rec_band().values())
    contrast = 1 - kernel_K(u_max) / kernel_K(0.0)
    return ("CCC.KERNEL.FREEZE.03|template=causal top-hat disc|"
            "theta_max=eta_rec/(eta_0-eta_rec) [typed externals,"
            f" {theta_deg:.4f} deg]|kappa: derived from v526"
            " beta_angle=2pi=1/(4c3) on the DLI fibre; convention band"
            f" declared; u_rec<= {u_max:.3e}|contrast bound"
            f" {contrast:.3e}|discriminators=sharp edge + sign/pairing"
            " table + radius formula|kills=K1..K5 (DLIII/DLIV) + K6:"
            " resolved relic with radial contrast > 1e-2 kills the"
            " derived-kappa chain (reopens the R2 crossover-transport"
            " reading)")


EXPECTED_SHA16 = {
    "v1": "1df51166d0a2ef5b",
    "v2": "a795401accbebdb4",
    "v3": "4cafe0457e0e89a1",
}


def sha16(spec):
    return hashlib.sha256(spec.encode()).hexdigest()[:16]


def freeze_status():
    """recompute all three freeze hashes and compare to the frozen
    prefixes; returns dict name -> (recomputed, expected, ok)."""
    out = {}
    for name, fn in (("v1", spec_v1), ("v2", spec_v2), ("v3", spec_v3)):
        got = sha16(fn())
        out[name] = (got, EXPECTED_SHA16[name],
                     got == EXPECTED_SHA16[name])
    return out
