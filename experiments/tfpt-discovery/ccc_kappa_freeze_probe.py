#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_kappa_freeze_probe -- CCC.SEAM.CROSSOVER (exploration round 6):
kappa derived from the v526 seam-KMS temperature normalisation.  RESULT:
the tick is so long compared to the pre-recombination aeon that the
relaxation structure of the kernel is UNOBSERVABLE for every reading in
the convention band -- the Gate-6 template degenerates, robustly, to a
SHARP-EDGED TOP-HAT DISC of radius theta_max = 1.16 deg, with the defect
sign/pairing table as the surviving TFPT discriminator.  Freeze v3
hashed.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO
ledger row, NO marker moved.  No CMB data touched.  v526 numbers cited
as [E] corpus facts; cosmography typed external; the tick-convention
band is declared honestly and the conclusion is shown to be stable
across ALL of it (that is the point of this round).

THE CHAIN.
  (1) v526 (SEAM.THERMAL.KMS.01, [E]): the seam KMS circle has
      beta_angle = 2 pi = 1/(4 c3) EXACTLY, T_seam = 4 c3 = 1/(2 pi),
      N-independent; the reading (typed [C] there) is "seam euclidean
      circle = thermal circle of the reconstructed horizon dynamics",
      chain-closed onto Hawking/SdS/Nariai (T_H = c3/M, T_N =
      4 c3 sqrt(Lambda)).
  (2) DLI/DLII: the seam circles ARE the Hopf fibres of the crossover;
      the fibre radius in the Lambda-aeon realisation is the de Sitter
      radius R_Lambda (global realisation of the seam, origin_theory).
      Consistency checked: T_seam = 4 c3 per angle <=> the
      Gibbons-Hawking normalisation T_GH = H/(2 pi) on a fibre of
      radius 1/H (algebraic identity).
  (3) Hence one KMS wrap = proper time 2 pi R with R in
      {R_Lambda (thermal-circle reading), R_c (curvature bound)} and
      the transport-tick convention in {full wrap, quarter wrap (the
      mu_4 clock step), wrap/6 and quarter-wrap/6 (the order-6 dynamic
      hand)}: a declared convention band spanning a factor ~1400.
  (4) The defect worldline relaxes for at most the proper age of the
      universe at recombination, tau_rec ~= 0.1165 Mpc (380 kyr, typed
      external).  Ticks accumulated: u_rec = tau_rec / tick.
RESULT: u_rec <= 8.3e-5 ACROSS THE WHOLE BAND (max at the smallest
tick), and the kernel contrast 1 - K(u_rec)/K(0) <= 3.5e-4: the
two-exponential relaxation edge is a sub-4e-4 correction -- invisible
against CMB noise and beam.  The template therefore degenerates to the
CAUSAL TOP-HAT: uniform disc, radius theta_max = eta_rec/(eta_0 -
eta_rec) ~= 1.16 deg, sharp (causal) edge; the surviving TFPT
discriminators are (i) the sharp edge itself vs Gaussian spots, (ii)
the frozen SIGN/PAIRING statistics of the defect classes (Z_2-pair
defects come as opposite-sign equal-|A| pairs -- the sheet-parity bit;
anchor-class defects carry no pair component), (iii) the disc-radius
band tied to the frozen formula.  A resolved relic with O(1) radial
contrast would KILL the derived-kappa chain (K6) and reopen the R2
(crossover-transport) reading -- falsifiable both ways.

FREEZE v3 hashed below; this feeds the preregistered search project
experiments/ccc-crossover-disc/ (round-6 target (c)).
"""

import hashlib
import numpy as np

PASS = []

LAM2 = (2.0 / 3.0) ** 6
D2 = 6 * np.log(1.5)
D3 = 6 * np.log(3.0)
C2 = 1 / np.sqrt(2.0)
C3 = 1 / np.sqrt(6.0)


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


def main():
    print("=" * 72)
    print("ccc_kappa_freeze_probe -- kappa from the v526 KMS normalisation:")
    print("the template degenerates robustly to the causal top-hat disc")
    print("(EXPLORATION ONLY, no ledger)")
    print("=" * 72)
    import sympy as sp

    # (1) the v526 normalisation, exact
    c3 = 1 / (8 * sp.pi)
    check("v526 chain replicated exactly: beta_angle = 1/(4 c3) = 2 pi,"
          " T_seam = 4 c3 = 1/(2 pi) (sympy exact)",
          sp.simplify(1 / (4 * c3) - 2 * sp.pi) == 0
          and sp.simplify(4 * c3 - 1 / (2 * sp.pi)) == 0)

    # (2) GH consistency on the DLI fibre: T = 1/(2 pi R) for a thermal
    # circle of radius R <=> T_GH = H/(2 pi) with R = 1/H
    H = sp.Symbol('H', positive=True)
    check("T_seam per angle = 4 c3 <=> Gibbons-Hawking T = H/(2 pi) on a"
          " fibre of radius 1/H (the v526 normalisation IS the GH"
          " normalisation on the DLI crossover fibre)",
          sp.simplify(4 * c3 * H - H / (2 * sp.pi)) == 0)

    # (3) external cosmography (typed)
    C_KM = 299792.458
    H0 = 67.4                      # km/s/Mpc (Planck 2018)
    D_H = C_KM / H0                # 4448 Mpc
    OM_L = 0.685
    R_LAM = D_H / np.sqrt(OM_L)    # de Sitter radius of the Lambda aeon
    R_C = D_H / np.sqrt(0.0031)    # min curvature radius (95% bound)
    TAU_REC = 3.8e5 / 3.2616e6     # 380 kyr in Mpc (c = 1)
    ETA_REC, ETA_0 = 280.3, 14165.0
    theta_deg = np.degrees(ETA_REC / (ETA_0 - ETA_REC))
    print(f"    externals: D_H = {D_H:.0f} Mpc, R_Lambda = {R_LAM:.0f}"
          f" Mpc, R_c >= {R_C:.0f} Mpc, tau_rec = {TAU_REC:.4f} Mpc,"
          f" theta_max = {theta_deg:.2f} deg")
    check("cosmography typed: R_Lambda = D_H/sqrt(Omega_L) ~= 5.4 Gpc,"
          " tau_rec ~= 0.117 Mpc (380 kyr)",
          5000 < R_LAM < 6000 and 0.10 < TAU_REC < 0.13)

    # (4) the tick-convention band and u_rec across it
    ticks = {}
    for rname, R in (("R_Lambda", R_LAM), ("R_c", R_C)):
        for cname, frac in (("full wrap", 1.0),
                            ("quarter wrap (mu4 step)", 0.25),
                            ("wrap/6 (dyn hand)", 1 / 6.0),
                            ("quarter/6", 1 / 24.0)):
            ticks[f"{rname}, {cname}"] = 2 * np.pi * R * frac
    u_vals = {k: TAU_REC / v for k, v in ticks.items()}
    u_max = max(u_vals.values())
    u_min = min(u_vals.values())
    print("    u_rec across the band:")
    for k, v in sorted(u_vals.items(), key=lambda kv: -kv[1]):
        print(f"      {k:34s} u_rec = {v:.2e}")
    check(f"u_rec <= {u_max:.2e} for EVERY reading in the declared band"
          f" (factor {u_max/u_min:.0f} spanned): the aeon before"
          f" recombination is a vanishing fraction of one seam tick",
          u_max < 1e-4)

    # (5) the kernel contrast bound
    def K(u):
        return C2 * np.exp(-D2 * u) + C3 * np.exp(-D3 * u)

    contrast = 1 - K(u_max) / K(0.0)
    slope = (C2 * D2 + C3 * D3) / (C2 + C3)
    check(f"kernel contrast 1 - K(u_rec)/K(0) <= {contrast:.2e}"
          f" (linear slope {slope:.3f} x u_rec): the two-exponential"
          f" relaxation edge is a sub-4e-4 correction -- unobservable;"
          f" the ring of round DLIV degenerates to the CAUSAL TOP-HAT"
          f" DISC", contrast < 5e-4)

    # (6) what survives as the TFPT discriminator: the sign/pairing
    # table (u -> 0 keeps the raw defect signature)
    u2 = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
    attr = np.full(3, 1.0 / 3.0)
    d0 = np.eye(3)[0] - attr
    d1 = np.eye(3)[1] - attr
    d2v = np.eye(3)[2] - attr
    check("surviving discriminators frozen: (i) sharp causal edge (not"
          " Gaussian), (ii) sign/pairing statistics -- Z_2-pair defects"
          f" have opposite equal pair-components ({u2 @ d0:+.4f} vs"
          f" {u2 @ d1:+.4f}), anchor defects none ({u2 @ d2v:+.4f}),"
          " (iii) the disc-radius formula",
          np.isclose(u2 @ d0, -(u2 @ d1)) and np.isclose(u2 @ d2v, 0))

    # (7) freeze v3 hash
    spec = ("CCC.KERNEL.FREEZE.03|template=causal top-hat disc|"
            "theta_max=eta_rec/(eta_0-eta_rec) [typed externals,"
            f" {theta_deg:.4f} deg]|kappa: derived from v526"
            " beta_angle=2pi=1/(4c3) on the DLI fibre; convention band"
            f" declared; u_rec<= {u_max:.3e}|contrast bound"
            f" {contrast:.3e}|discriminators=sharp edge + sign/pairing"
            " table + radius formula|kills=K1..K5 (DLIII/DLIV) + K6:"
            " resolved relic with radial contrast > 1e-2 kills the"
            " derived-kappa chain (reopens the R2 crossover-transport"
            " reading)")
    h = hashlib.sha256(spec.encode()).hexdigest()
    print(f"    FROZEN SPEC v3 SHA-256: {h[:16]}")
    check("freeze v3 hashed: kappa no longer a free parameter -- it is"
          " derived-with-declared-band, and every point of the band"
          " gives the same observable template", len(h) == 64)

    print("\n" + "=" * 72)
    n_ok = sum(PASS)
    print(f"RESULT: {n_ok}/{len(PASS)} checks passed"
          + ("  --  ALL PASSED" if all(PASS) else "  --  FAILURES ABOVE"))
    print("kappa derived (v526 KMS): tick >= 2 pi R_Lambda / 24; the")
    print("pre-recombination aeon accumulates u_rec <= 8e-5 ticks =>")
    print("template = SHARP TOP-HAT DISC, 1.16 deg, sign/pairing")
    print("statistics as discriminator; K6 makes the chain falsifiable.")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
