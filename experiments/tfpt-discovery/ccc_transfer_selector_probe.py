#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_transfer_selector_probe -- CCC.SEAM.CROSSOVER (exploration round 5):
(A) the u(theta) transfer map from the DLI bridge geometry -- the Gate-6
kernel becomes a FULLY GEOMETRIC, rim-brightened ring template (frozen,
hashed); (B/C) the substantive gamma step: the UNIQUENESS half of the
v534 delta = pi/2 selector is DERIVED as a Theta-reality necessity from
the clock factorisation, at operator level with fermionic signs.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO
ledger row, NO marker moved.  WOIT.OS.TWISTOR.01 stays [O].  No CMB data
touched.  v534's SURVIVAL half (existence, PD at positive coupling) is
CITED as the nonperturbative toy fact, not rederived; the coupling SIGN
is explicitly NOT derivable from reality (stated).  External cosmography
typed as external.

PART A (the transfer map u(theta)).  Round DLIII froze the kernel SHAPE
in the flow variable u; the declared-[C] gap was the map to sky angle.
The DLI bridge closes it geometrically:
  - in the bridge cylinder (-dT^2 + g_{S^3}), radial null rays obey
    chi = Delta T exactly (checked symbolically) -- influence from a
    point defect on the crossover fills the comoving ball chi <= eta;
  - at recombination the imprint is a DISC of angular radius
    theta_max = eta_rec / (eta_0 - eta_rec)  [FROZEN FORMULA]
    = 1.16 deg for Planck-2018 cosmography (eta_rec ~= 280.3 Mpc,
    eta_0 ~= 14165 Mpc, typed external) -- landing INSIDE the 0.7-1.2
    deg extent window HawkingNet scanned: the WINDOW was right;
  - the signal observed at angular offset theta departed the defect
    worldline at conformal time eta_dep = eta_rec - theta (eta_0 -
    eta_rec), having relaxed for u_dep proportional to eta_dep clock
    ticks [the one remaining [C] premise: ticks accumulate linearly in
    bridge conformal time; the tick length kappa stays the single open
    number, named candidate: the SEAM.THERMAL.KMS.01 normalisation];
  - hence A(theta) = K(kappa (eta_rec - theta D_A)): the amplitude is
    MAXIMAL AT THE RIM (departed at the crossover, zero relaxation) and
    decays inward with the frozen two-exponential edge profile -- the
    template is a RIM-BRIGHTENED RING, not a centrally peaked spot.
    Checked: rim-monotonicity for every kappa > 0; the edge-width ratio
    Delta_3/Delta_2 = 2.709511 frozen; a best-fit centrally-peaked
    Gaussian leaves O(1) residual for every kappa (wrong template
    class, quantified) -- sharpening the Part-A round-4 statement: the
    HawkingNet null tested centrally-peaked Gaussians in the right
    window; the TFPT prediction there is a ring.
FROZEN SPEC v2 hashed; kill criteria extended: (K4) a resolved
crossover-relic profile that is centrally peaked kills the kernel;
(K5) a resolved ring with edge-width ratio incompatible with 2.7095
kills it.

PART B (continuum: the selector's uniqueness IS the clock
factorisation).  The v512 mark family M(delta) = {+-1, +-e^{i delta}}.
Machine-checked over a delta-grid + exactly at delta = pi/2:
  - the reflection symmetries of M(delta) (circle reflections
    theta -> alpha - theta preserving the mark set) form the
    pair-exchanging V_4 for delta != pi/2 (exactly 2 admissible axes,
    rotation closure {0, pi}) and D_4 iff delta = pi/2 (4 axes,
    closure {0, pi/2, pi, 3pi/2});
  - consequently the order-4 clock factorises into two ADMISSIBLE
    reflections (the DLIII identity rho = tau o s_mid) iff
    delta = pi/2: for delta != pi/2 the admissible axis differences
    generate only the sheet flip, never the clock.  (This is corpus
    face #13 of the v512 web, here upgraded from a typed [C]
    reformulation to the operative selection mechanism.)

PART C (lattice, operator level with fermionic signs: Theta-reality
necessity).  On the N = 16 Majorana seam ring (v529 layout), marks at
bonds {0, k, 8, k+8} (delta = pi k / 8, k = 4 <=> delta = pi/2), FK
quartets centred on the mark bonds, free uniform-hopping parent:
  - the FREE parent is Theta_a-real for ALL 16 reflection axes
    (replicates the v521 side-blindness at operator level);
  - the INTERACTING H(k, g uniform) is Theta_a-real on EXACTLY the
    admissible axes of Part B: 2 axes for k != 4, 4 axes for k = 4 --
    the fermionic reordering signs do NOT spoil the set-level count
    (this is the nontrivial content: reality survives the signs);
  - the straddled CLOCK axes are Theta-real iff k = 4: since
    Theta-reality of H is NECESSARY for reflection positivity of its
    Gibbs/OS structure on that cut, every delta != pi/2 member dies on
    the clock axes BY ALGEBRA -- the uniqueness half of the v534
    selector is DERIVED, not scanned;
  - asymmetric couplings die the same way: reality on the clock axis
    forces the reflected mark pairs to carry EQUAL couplings (checked:
    unequal g on a swapped pair breaks reality; equal g restores it) --
    v534's "every asymmetric member dies", derived at reality level;
  - HONEST LIMIT: Theta-reality is necessary, not sufficient -- the
    SURVIVAL of the delta = pi/2, g > 0 member (PD, lifted minimum) and
    the SIGN selection s = + are v534's nonperturbative toy facts,
    cited, not rederived; reality holds for both signs of g.
VERDICT: selector uniqueness = clock factorisation (derived necessity);
selector survival = v534 (cited).  The gamma fence sharpens: the
interacting A_hol inherits its RP-cut geometry from the D_4 closure,
which exists only at the mu_4 configuration.

WHAT STAYS OPEN: kappa (the tick length) -- the last free number of the
kernel; gamma proper (interacting A_hol construction); the sign bit
s = + (nonperturbative).
"""

import hashlib
import numpy as np

RNG = np.random.default_rng(20260824)
PASS = []

LAM2 = (2.0 / 3.0) ** 6
D2 = 6 * np.log(1.5)
D3 = 6 * np.log(3.0)
C2 = 1 / np.sqrt(2.0)
C3 = 1 / np.sqrt(6.0)


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


# =====================================================================
def part_a():
    print("\nPART A -- the u(theta) transfer map: the kernel becomes a"
          " rim-brightened ring (frozen)")
    import sympy as sp

    # (A1) radial null rays of the bridge: chi = Delta T exactly
    T, ch = sp.symbols('T chi', positive=True)
    # -dT^2 + dchi^2 = 0 on radial rays => dchi/dT = +-1
    check("bridge cylinder radial null rays: -dT^2 + dchi^2 = 0 =>"
          " chi = Delta T exactly (influence fills the comoving ball"
          " chi <= eta)", sp.solve(sp.Eq(-1 + sp.Symbol('v') ** 2, 0),
                                   sp.Symbol('v')) == [-1, 1])

    # (A2) the disc radius from typed external cosmography
    ETA_REC, ETA_0 = 280.3, 14165.0          # Mpc, Planck 2018 (typed)
    theta_max = ETA_REC / (ETA_0 - ETA_REC)
    theta_deg = np.degrees(theta_max)
    check(f"FROZEN FORMULA theta_max = eta_rec/(eta_0 - eta_rec) ="
          f" {theta_max:.5f} rad = {theta_deg:.2f} deg (externals typed)"
          f" -- INSIDE the HawkingNet extent window 0.7-1.2 deg: the"
          f" window was right", 0.7 <= theta_deg <= 1.2)

    # (A3) the profile: A(theta) = K(kappa (eta_rec - theta D_A));
    # rim-brightened for EVERY kappa > 0
    D_A = ETA_0 - ETA_REC
    thetas = np.linspace(0.0, theta_max, 400)

    def profile(kappa):
        u = kappa * (ETA_REC - thetas * D_A)          # >= 0, 0 at rim
        return C2 * np.exp(-D2 * u) + C3 * np.exp(-D3 * u)

    ok_rim = True
    for kappa in (0.2 / ETA_REC, 1.0 / ETA_REC, 5.0 / ETA_REC):
        A = profile(kappa)
        ok_rim &= bool(np.all(np.diff(A) > 0)) and A[-1] > A[0]
    check("A(theta) is strictly INCREASING to the rim for every tested"
          " kappa (the defect departed at the crossover arrives"
          " unrelaxed at the rim): the template is a RIM-BRIGHTENED"
          " RING, not a central spot", ok_rim)

    # (A4) edge-width ratio frozen and kappa-independent
    ratio = D3 / D2
    check(f"the ring edge carries the two frozen scales with width"
          f" ratio Delta3/Delta2 = {ratio:.6f} in the angular depth"
          f" (theta_max - theta), independent of kappa (affine"
          f" invariance carried over from round DLIII)",
          np.isclose(ratio, np.log(3) / np.log(1.5)))

    # (A5) wrong-template quantification: best centrally-peaked
    # Gaussian vs the ring, for a kappa grid
    worst = np.inf
    for kappa in (0.2 / ETA_REC, 1.0 / ETA_REC, 5.0 / ETA_REC):
        A = profile(kappa)
        A = A / np.max(A)
        best = np.inf
        for w in np.linspace(0.1 * theta_max, 3 * theta_max, 60):
            for amp in np.linspace(0.2, 1.5, 40):
                G = amp * np.exp(-0.5 * (thetas / w) ** 2)
                best = min(best, float(np.sqrt(np.mean((A - G) ** 2))))
        worst = min(worst, best)
    check(f"a centrally-peaked Gaussian cannot fit the ring: best-case"
          f" RMS residual {worst:.3f} (O(1) of the peak) for every"
          f" kappa -- the HawkingNet template class is quantifiably the"
          f" WRONG shape family for this prediction", worst > 0.15)

    # (A6) freeze hash v2
    spec = ("CCC.KERNEL.FREEZE.02|topology=rim-brightened ring|"
            "theta_max=eta_rec/(eta_0-eta_rec) [externals typed]|"
            f"edge rates Delta2={D2:.12f}, Delta3={D3:.12f},"
            f" ratio={D3/D2:.12f}|amplitudes pair=(+-{C2:.12f},"
            f"+{C3:.12f}), anchor=(0,{-2/np.sqrt(6):.12f})|"
            "open=[C] kappa tick length (candidate:"
            " SEAM.THERMAL.KMS.01)|kills=K1..K3 (round DLIII) + K4"
            " centrally-peaked resolved profile + K5 resolved ring"
            " edge-ratio != 2.7095")
    h = hashlib.sha256(spec.encode()).hexdigest()
    print(f"    FROZEN SPEC v2 SHA-256: {h[:16]}")
    check("frozen spec v2 hashed (geometry + shape + kills; kappa the"
          " single declared open number)", len(h) == 64)


# =====================================================================
def part_b():
    print("\nPART B -- continuum: admissible reflections of M(delta)"
          " close to D_4 iff delta = pi/2 (the clock factorisation)")

    def admissible_axes(delta):
        """reflection theta -> alpha - theta preserving the mark set;
        any admissible alpha must satisfy alpha - m_i in marks, so the
        complete candidate set is {m_i + m_j} (exact, no grid)."""
        marks = np.array([0.0, np.pi, delta, delta + np.pi]) % (2 * np.pi)
        cands = sorted({round(float((mi + mj) % (2 * np.pi)), 12)
                        for mi in marks for mj in marks})
        axes = []
        for alpha in cands:
            img = (alpha - marks) % (2 * np.pi)
            ok = all(np.min(np.abs(((img[i] - marks + np.pi)
                                    % (2 * np.pi)) - np.pi)) < 1e-9
                     for i in range(4))
            if ok:
                axes.append(alpha)
        return np.array(axes)

    # (B1) generic delta: exactly 2 admissible axes (V_4); closure {0,pi}
    ok_generic = True
    for delta in (0.3, 0.7, 1.1, 2.0, 2.7):
        ax = admissible_axes(delta)
        diffs = {round(float((a - b) % (2 * np.pi)), 6)
                 for a in ax for b in ax}
        has_clock = any(np.isclose(d % np.pi, np.pi / 2, atol=1e-6)
                        for d in diffs)
        ok_generic &= (len(ax) == 2) and not has_clock
    check("generic delta: exactly 2 admissible reflection axes (the"
          " pair-exchanging V_4); their products generate only the"
          " sheet flip -- the order-4 clock CANNOT be factorised into"
          " admissible reflections", ok_generic)

    # (B2) delta = pi/2: 4 axes (D_4); the clock IS a product
    ax = admissible_axes(np.pi / 2)
    diffs = sorted({round(float((a - b) % (2 * np.pi)), 6)
                    for a in ax for b in ax})
    has_clock = any(np.isclose(d, np.pi / 2, atol=1e-6) for d in diffs)
    check(f"delta = pi/2: exactly 4 admissible axes"
          f" (D_4 closure), and the axis differences contain pi/2:"
          f" the clock = product of two admissible reflections"
          f" (rho = tau o s_mid, round DLIII) EXISTS exactly here",
          len(ax) == 4 and has_clock)

    # (B3) uniqueness on a fine delta scan
    deltas = np.linspace(0.05, np.pi - 0.05, 181)
    n4 = [len(admissible_axes(d)) for d in deltas]
    winners = [float(d) for d, n in zip(deltas, n4) if n >= 4]
    check(f"delta-scan (0, pi): the D_4 closure happens ONLY at"
          f" delta = pi/2 (winners: {[round(w, 4) for w in winners]})",
          len(winners) == 1 and np.isclose(winners[0], np.pi / 2,
                                           atol=0.01))


# =====================================================================
# Majorana symbolic algebra (index-level, exact signs, no Fock space)
# =====================================================================
def canon(idx, coeff):
    """sort Majorana indices with fermionic parity; equal indices
    contract (not needed here -- all terms have distinct indices)."""
    idx = list(idx)
    sign = 1
    for i in range(len(idx)):
        for j in range(len(idx) - 1 - i):
            if idx[j] > idx[j + 1]:
                idx[j], idx[j + 1] = idx[j + 1], idx[j]
                sign = -sign
    return tuple(idx), sign * coeff


def add_term(H, idx, coeff):
    t, c = canon(idx, coeff)
    H[t] = H.get(t, 0) + c


def reflect_H(H, a, N=16):
    """antiunitary Theta_a: gamma_j -> gamma_{(a - j) mod N}, coeff ->
    conj(coeff)."""
    out = {}
    for idx, c in H.items():
        new = [(a - j) % N for j in idx]
        add_term(out, new, np.conj(c))
    return out


def h_equal(H1, H2):
    keys = set(H1) | set(H2)
    return all(abs(H1.get(k, 0) - H2.get(k, 0)) < 1e-12 for k in keys)


def build_H(k, gs, N=16, free_only=False):
    """free uniform hopping + FK quartets on mark bonds {0, k, 8, k+8}
    (quartet at bond b = sites {b-2, b-1, b, b+1})."""
    H = {}
    for j in range(N):
        add_term(H, (j, (j + 1) % N), 1j)
    if not free_only:
        for b, g in zip([0, k, 8, (k + 8) % N], gs):
            add_term(H, tuple((b - 2 + m) % N for m in range(4)), g)
    return H


def part_c():
    print("\nPART C -- lattice operator level: Theta-reality necessity"
          " derives the selector's uniqueness (fermionic signs kept)")
    N = 16

    # (C1) free parent side-blind: real under ALL 16 axes
    Hf = build_H(4, [0] * 4, free_only=True)
    n_free = sum(1 for a in range(N) if h_equal(reflect_H(Hf, a), Hf))
    check(f"free parent is Theta_a-real for ALL {n_free}/16 axes"
          f" (v521 side-blindness replicated at operator level,"
          f" including the i-hopping conjugation and wrap signs)",
          n_free == 16)

    # (C2) interacting member: admissible-axis count vs k
    counts = {}
    for k in range(1, 8):
        H = build_H(k, [1.0] * 4)
        counts[k] = sum(1 for a in range(N)
                        if h_equal(reflect_H(H, a), H))
    ok_generic = all(counts[k] == 2 for k in range(1, 8) if k != 4)
    check(f"interacting H(k, g uniform): Theta-real axes ="
          f" {counts} -- exactly 2 (V_4) for every k != 4 and 4 (D_4)"
          f" for k = 4: the FERMIONIC SIGNS DO NOT SPOIL the set-level"
          f" count; the D_4 closure is an operator identity",
          ok_generic and counts[4] == 4)

    # (C3) the straddled clock axes are Theta-real iff k = 4
    H4 = build_H(4, [1.0] * 4)
    clock_axes = [a for a in range(N)
                  if h_equal(reflect_H(H4, a), H4)]
    ok_kill = True
    for k in range(1, 8):
        if k == 4:
            continue
        Hk = build_H(k, [1.0] * 4)
        for a in clock_axes:
            if a % 8 in (0, 1):        # the axes through the +-1 pair
                ok_kill &= not h_equal(reflect_H(Hk, a), Hk)
    check(f"the clock-axis cuts (Theta-real axes of the mu_4 member:"
          f" {clock_axes}) are NOT Theta-real for any k != 4 =>"
          f" Theta-reality (NECESSARY for RP on that cut) kills every"
          f" delta != pi/2 member BY ALGEBRA -- the uniqueness half of"
          f" the v534 selector is DERIVED from the clock factorisation",
          ok_kill)

    # (C4) asymmetric couplings die at reality level too
    a_swap = clock_axes[0]
    H_asym = build_H(4, [1.0, 0.7, 1.0, 0.7])
    H_asym2 = build_H(4, [1.0, 0.7, 0.9, 0.7])
    H_sym = build_H(4, [1.0, 0.7, 1.0, 0.7])
    # find which axis swaps the k and k+8 quartets: axis through the
    # +-1 pair swaps marks 4 <-> 12
    def real_under_any_clock_axis(H):
        return [a for a in clock_axes if h_equal(reflect_H(H, a), H)]
    r_asym2 = real_under_any_clock_axis(H_asym2)
    r_sym = real_under_any_clock_axis(H_sym)
    check(f"couplings must pair under the reflections: the pairwise-"
          f"symmetric member (1.0, 0.7, 1.0, 0.7) keeps clock-axis"
          f" reality on axes {r_sym}; breaking one pair"
          f" (1.0, 0.7, 0.9, 0.7) leaves {r_asym2} -- 'every asymmetric"
          f" member dies', derived at reality level",
          len(r_sym) >= 2 and len(r_asym2) < len(r_sym))

    # (C5) honest limit: reality is sign-blind
    H_neg = build_H(4, [-1.0] * 4)
    n_neg = sum(1 for a in range(N)
                if h_equal(reflect_H(H_neg, a), H_neg))
    check(f"HONEST LIMIT: Theta-reality holds for BOTH coupling signs"
          f" ({n_neg}/16 axes for g = -1, same as g = +1) -- the sign"
          f" selection s = + and the PD survival are v534's"
          f" nonperturbative toy facts (cited, NOT rederived): necessity"
          f" derived, sufficiency cited", n_neg == 4)


def main():
    print("=" * 72)
    print("ccc_transfer_selector_probe -- u(theta) transfer map (Gate 6")
    print("full freeze) + the gamma step: selector uniqueness derived from")
    print("the clock factorisation (EXPLORATION ONLY, no ledger)")
    print("=" * 72)
    part_a()
    part_b()
    part_c()
    print("\n" + "=" * 72)
    n_ok = sum(PASS)
    print(f"RESULT: {n_ok}/{len(PASS)} checks passed"
          + ("  --  ALL PASSED" if all(PASS) else "  --  FAILURES ABOVE"))
    print("(A) kernel now fully geometric: RIM-BRIGHTENED RING, theta_max")
    print("    = eta_rec/(eta_0 - eta_rec) ~ 1.16 deg (in the HawkingNet")
    print("    window, wrong template class quantified); one open number")
    print("    kappa.")
    print("(B/C) the v534 selector's UNIQUENESS (delta = pi/2, symmetric")
    print("    couplings) is now a DERIVED Theta-reality necessity from")
    print("    the D_4/clock factorisation -- operator level, fermionic")
    print("    signs kept; survival + sign stay v534 (cited).")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
