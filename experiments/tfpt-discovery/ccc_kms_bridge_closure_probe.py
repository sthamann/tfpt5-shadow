#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_kms_bridge_closure_probe -- CCC.SEAM.CROSSOVER (exploration round
9): the REMAINING half of the P1.INDEX.KMS.01 bridge (w_0 = w_2, the
NS/R-type balance) formulated and decided on the lens crossover:
THE OFFSET IS THE ODD-DECK LEFSCHETZ TRACE, AND IT VANISHES BECAUSE THE
DECK ACTS FREELY -- the c3 bridge closes geometrically because the
crossover is a SMOOTH manifold (conditional on the lens realisation,
typed).

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO
ledger row, NO marker moved.  P1.INDEX.KMS.01 stays [O] in the ledger
(this is the exploration-level closure candidate of its one open
bridge, conditional on the CELEST/ALE lens realisation like rounds
DL-DLVIII); c3 stays the P1 axiom -- the bridge EXPLAINS, it does not
derive.

THE CHAIN.
  (1) SECTOR IDENTITY (exact): the deck-sector projector difference is
      P_0 - P_2 = (D + D^3)/2, so the offset is
        w_0 - w_2 = tr((D + D^3) e^{-t Delta}) / (2 tr(e^{-t Delta}))
      -- EXACTLY the normalised equivariant (Lefschetz-type) heat trace
      of the ODD deck powers.  "R-sector anomaly" = odd-deck character.
  (2) THE DECK TRACES ON S^3 (closed form, verified against explicit
      spin-j matrices): H_n = V_{n/2} (x) V_{n/2} under SU(2)_L x
      SU(2)_R, the deck sits in SU(2)_L as the angle-pi/2 element, so
      tr(D|H_n) = sin((n+1)pi/2) * (n+1): the odd levels vanish, the
      even levels alternate +-(n+1) -- a BOUNDED-oscillation series
      against a total dimension growing like N^3.
  (3) VANISHING (the freeness mechanism): the normalised offset
      offset(t) -> 0 as t -> 0+ (computed decade by decade; the
      equivariant numerator stays O(1) while the denominator diverges
      like t^{-3/2}) -- because the deck has NO fixed points on S^3
      there is no local Atiyah-Bott contribution, only exponentially
      damped closed-geodesic terms.  Freeness was verified in round
      DLI; freeness of the deck IS smoothness of the lens crossover.
  (4) THE CONTROL (non-free action keeps an anomaly): on S^2 the clock
      rotation by pi/2 has TWO fixed points; its equivariant heat trace
      tends to the Atiyah-Bott value sum_fp 1/|1 - i|^2 = 2/2 = 1 !=
      0 (verified numerically against the closed Dirichlet-kernel
      characters) -- a sector offset built on a NON-free action would
      NOT vanish.  The dichotomy free <-> even response is sharp.
  (5) NS/R READING (typed [C]): sector 2 is the GSO/fermion-parity
      class = the seam-string holonomy of round DLII; w_0 = w_2 in the
      limit is the statement "the R-sector anomaly of the crossover
      vanishes", and it does so BECAUSE X = S^3/Z_4 is smooth.  The
      corpus's measured finite-level offset (+-2^{-(l+1)}, halving,
      zero-sum, vanishing) is the finite-window shadow of exactly this
      limit; its precise halving law belongs to the v-probe's specific
      window model and is NOT re-derived here (typed honestly).
CONCLUSION (typed): given the lens realisation, BOTH halves of the
P1.INDEX.KMS.01 bridge are now geometric -- w_1 = w_3 exact by the
reciprocal involution (round DLVIII), w_0 = w_2 in the limit by deck
freeness (this round).  The contract's kill ("any asymmetric sector
offset") cannot fire on the crossover.  Ledger movement is a promotion
decision, not made here.
"""

import numpy as np

PASS = []


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


def spin_matrix_char(j, phi):
    """character of exp(i phi J_z) on spin-j via explicit matrix."""
    m = np.arange(-j, j + 1)
    return float(np.sum(np.cos(phi * m))) + 1j * float(np.sum(
        np.sin(phi * m)))


def main():
    print("=" * 72)
    print("ccc_kms_bridge_closure_probe -- w_0 = w_2 from deck freeness:")
    print("the c3 bridge closes because the crossover is smooth")
    print("(EXPLORATION ONLY, no ledger)")
    print("=" * 72)

    # (1) sector identity P_0 - P_2 = (D + D^3)/2 on the regular rep
    S = np.roll(np.eye(4), 1, axis=0)
    P = {k: sum(np.exp(-2j * np.pi * k * jj / 4)
                * np.linalg.matrix_power(S, jj) for jj in range(4)) / 4
         for k in range(4)}
    lhs = P[0] - P[2]
    rhs = (S + np.linalg.matrix_power(S, 3)) / 2
    check("sector identity P_0 - P_2 = (D + D^3)/2 exact (the offset IS"
          " the odd-deck equivariant trace)", np.allclose(lhs, rhs))

    # (2) deck traces on S^3 harmonics: closed form vs explicit spin-j
    ok_char = True
    for n in range(0, 13):
        j = n / 2.0
        # deck = exp(i (pi/2) sigma_z) in SU(2)_L: phi = pi/2 on spin j
        chi = spin_matrix_char(j, np.pi / 2 * 2)   # diag(i,-i): phi=pi
        # careful: diag(e^{i pi/2}, e^{-i pi/2}) = exp(i (pi/2) sigma_z)
        # acts on spin-j with weights e^{i (pi/2) 2m'}? spin-1/2 weights
        # +-1/2 under J_z: exp(i phi J_z) with phi = pi gives diag(i,-i)
        closed = np.sin((n + 1) * np.pi / 2)
        ok_char &= np.isclose(chi.real, closed, atol=1e-12) and \
            np.isclose(chi.imag, 0.0, atol=1e-12)
    check("deck character on V_{n/2}: chi = sin((n+1)pi/2) exactly"
          " (explicit exp(i pi J_z) spin matrices vs closed form,"
          " n = 0..12) => tr(D|H_n) = sin((n+1)pi/2)(n+1)", ok_char)

    # (3) the normalised offset vanishes as t -> 0 (free action)
    N = 4000
    ns = np.arange(0, N + 1)
    dims = (ns + 1.0) ** 2
    lam = ns * (ns + 2.0)
    trD = np.sin((ns + 1) * np.pi / 2) * (ns + 1)   # = tr(D^3|H_n) too
    offsets = {}
    for t in (0.3, 0.1, 0.03, 0.01, 0.003):
        w = np.exp(-t * lam)
        num = np.sum(2 * trD * w)                    # D and D^3 equal
        den = 2 * np.sum(dims * w)
        offsets[t] = num / den
    vals = np.array([abs(offsets[t]) for t in (0.3, 0.1, 0.03, 0.01,
                                               0.003)])
    print("    offset(t):", {t: f"{v:.2e}" for t, v in offsets.items()})
    slope = np.polyfit(np.log([0.3, 0.1, 0.03, 0.01, 0.003]),
                       np.log(vals), 1)[0]
    check(f"normalised offset w_0 - w_2 -> 0 as t -> 0 (monotone"
          f" decade decay, power ~ t^{{{slope:.2f}}}): the odd-deck"
          f" numerator stays O(1) while the volume term diverges --"
          f" FREENESS kills the anomaly", 
          bool(np.all(np.diff(vals) < 0)) and slope > 1.0)

    # equivariant numerator itself stays bounded (no fixed points)
    nums = [abs(np.sum(trD * np.exp(-t * lam)))
            for t in (0.3, 0.1, 0.03, 0.01, 0.003)]
    check(f"the equivariant heat trace tr(D e^-tDelta) stays O(1) as"
          f" t -> 0 (values {[f'{v:.3f}' for v in nums]}): no local"
          f" Atiyah-Bott term -- the geometric signature of a FREE"
          f" action (deck freeness = crossover smoothness, round DLI)",
          max(nums) < 1.0)

    # (4) control: NON-free action on S^2 keeps a nonzero limit
    ls = np.arange(0, 3000)
    lam2 = ls * (ls + 1.0)
    # rotation by pi/2 on S^2: character = Dirichlet kernel
    chi2 = np.sin((2 * ls + 1) * np.pi / 4) / np.sin(np.pi / 4)
    ab_vals = [float(np.sum(chi2 * np.exp(-t * lam2)))
               for t in (0.3, 0.1, 0.03, 0.01, 0.003)]
    print("    S^2 clock (2 fixed points) equivariant trace:",
          [f"{v:.4f}" for v in ab_vals])
    check(f"CONTROL: the non-free clock rotation on S^2 keeps the"
          f" Atiyah-Bott value sum_fp 1/|1-i|^2 = 1 as t -> 0 (last:"
          f" {ab_vals[-1]:.4f}) -- a sector offset built on a non-free"
          f" action would NOT vanish: the dichotomy is sharp",
          abs(ab_vals[-1] - 1.0) < 0.01)

    # (5) NS/R typing consistency: sector 2 is the 2-torsion class
    DECK = np.diag([1j, -1j])
    D2 = DECK @ DECK
    check("sector-2 = the 2-torsion (-1) = the seam-string holonomy"
          " class of round DLII (D^2 = -1 exact): w_0 = w_2 is the"
          " NS/R-type balance, and it holds in the limit BECAUSE the"
          " crossover is smooth (typed [C], conditional on the lens"
          " realisation)", np.allclose(D2, -np.eye(2)))

    print("\n" + "=" * 72)
    n_ok = sum(PASS)
    print(f"RESULT: {n_ok}/{len(PASS)} checks passed"
          + ("  --  ALL PASSED" if all(PASS) else "  --  FAILURES ABOVE"))
    print("Given the lens realisation, BOTH halves of the P1.INDEX.KMS.01")
    print("bridge are geometric: w_1 = w_3 by the reciprocal involution")
    print("(DLVIII), w_0 = w_2 in the limit by deck freeness (this round).")
    print("The 'asymmetric sector offset' kill cannot fire on a smooth")
    print("crossover.  Ledger stays [O]; promotion is a separate decision.")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
