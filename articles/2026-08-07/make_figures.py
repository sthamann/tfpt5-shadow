#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figures for the two Medium/LinkedIn articles of August 7, 2026
(floor & detector; one-register compiler).

Generates all PNGs in articles/2026-08-07/figures/ with the same dark
design system as the 2026-08-03 set. All numbers come from the frozen
round-23..27 records (verification/v814-v836 module headers,
experiments/next.txt diary entries LXVII-LXXI) and
website/lib/discipline.ts (generated suite statistics). The two
afternoon figures (a3_zwei_giganten, a3_wand_karte) read the frozen
records of the eleven afternoon probes in experiments/tfpt-discovery/
(open-doors / level2 / expectation / position-carrier; gue_saturation /
gue_ablation / bootstrap_loop_gain / paircorr_bridge_map;
multiplicative_relation / relation_corner_ladder /
excess_certified_skeleton -- exploration level, report-only). Where a
layout is schematic (miss assignment, point placement inside an exact
band), the figure says so explicitly.

Run:  experiments/tfpt-discovery/.venv/bin/python make_figures.py
"""

import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

# ----------------------------------------------------------------------------
# Design system (dark, consistent -- identical to the 2026-08-03 set)
# ----------------------------------------------------------------------------
BG = "#0d1320"        # page background
PANEL = "#161f2e"     # card surface
PANEL2 = "#1c2740"    # lighter card
TXT = "#e9eef6"       # main text
MUT = "#93a1b5"       # muted text
GRID = "#2a3750"      # lines
CYAN = "#53c8f0"      # accent 1 (structure / geometry)
GREEN = "#3ddc97"     # accent 2 (proven / closed)
AMBER = "#f5b942"     # accent 3 (measured / named open)
RED = "#f06a6a"       # accent 4 (hard open / kill)
VIOLET = "#a78bfa"    # accent 5 (code / information)

FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(FIGDIR, exist_ok=True)

plt.rcParams.update({
    "figure.facecolor": BG,
    "savefig.facecolor": BG,
    "text.color": TXT,
    "axes.edgecolor": GRID,
    "axes.labelcolor": TXT,
    "xtick.color": MUT,
    "ytick.color": MUT,
    "font.family": "DejaVu Sans",
    "font.size": 11,
})

FOOTER = "Source: TFPT verification suite · fixpoint-theory.com · as of August 7, 2026"


def new_canvas(w=12.8, h=7.2):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    return fig, ax


def title(ax, text, sub=None, x=4, y=93.5):
    ax.text(x, y, text, fontsize=19, fontweight="bold", color=TXT,
            ha="left", va="center")
    if sub:
        ax.text(x, y - 5.2, sub, fontsize=11.5, color=MUT, ha="left", va="center")


def footer(ax, x=4, y=3.0):
    ax.text(x, y, FOOTER, fontsize=8.5, color=MUT, ha="left", va="center")


def box(ax, x, y, w, h, lines, fc=PANEL, ec=GRID, fs=11, title_line=None,
        title_color=TXT, lw=1.4, align="center", ls="-"):
    """Rounded card with an optional title line."""
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.6",
        fc=fc, ec=ec, lw=lw, linestyle=ls, mutation_aspect=100 / 100))
    cx = x + w / 2 if align == "center" else x + 2.2
    ha = "center" if align == "center" else "left"
    yy = y + h - 3.4
    if title_line:
        ax.text(cx, yy, title_line, fontsize=fs + 1.5, fontweight="bold",
                color=title_color, ha=ha, va="center")
        yy -= 4.6
    for ln in lines:
        ax.text(cx, yy, ln, fontsize=fs, color=TXT, ha=ha, va="center")
        yy -= 4.2


def arrow(ax, x1, y1, x2, y2, color=CYAN, lw=2.4, style="-|>", ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=18, lw=lw, color=color,
                                 linestyle=ls, shrinkA=0, shrinkB=0))


def chip(ax, x, y, w, text, color, fs=10, h=4.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.45,rounding_size=1.8",
                                fc=PANEL2, ec=color, lw=1.3))
    ax.text(x + w / 2, y + h / 2, text, fontsize=fs, color=TXT,
            ha="center", va="center")


# ----------------------------------------------------------------------------
# Frozen record data (rounds 23-27)
# ----------------------------------------------------------------------------
# Zero ordinates of the Riemann zeta function in (60, 120] (classical);
# exactly 25 -- the v828 window census (21 located + 4 typed misses,
# RvM main term 25.237 -> 25).
ZEROS_60_120 = [
    60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
    75.704691, 77.144840, 79.337375, 82.910381, 84.735493,
    87.425275, 88.809111, 92.491899, 94.651344, 95.870634,
    98.831194, 101.317851, 103.725539, 105.446623, 107.168611,
    111.029536, 111.874659, 114.320221, 116.226680, 118.790783,
]
assert len(ZEROS_60_120) == 25

# v829 depth-kill margins (X = 18.375 -> 25.5, six stations, frozen record).
KILL_MARGINS = [5.76, 6.24, 6.53, 7.16, 8.17, 8.92]
# v827 locator depth law (detection rate in %, frozen record).
DEPTH_LAW = [54, 62, 83]
# v830 certified envelope constant; v818 measured band on rho * h^{3/2}.
C_CERT = 4.335
BAND_LO, BAND_HI = 4.85, 24.2


# ============================================================================
# Article 3 / Figure 1: the certified envelope (v818 / v830)
# ============================================================================
def fig_a3_huellkurve():
    fig = plt.figure(figsize=(12.8, 7.2))

    axh = fig.add_axes([0, 0.84, 1, 0.16])
    axh.set_xlim(0, 100)
    axh.set_ylim(0, 100)
    axh.axis("off")
    axh.text(3.2, 60, "The certified envelope:  ρ ≥ 4.335 · h^(−3/2)  on 73 of 73 frames",
             fontsize=19, fontweight="bold", color=TXT)
    axh.text(3.2, 18, "One inequality is left: ρ(X) = τ/τ_pnt > 0 — the prime comb against its own density (PRIME.FLOOR.RATIO.01, open). "
                      "Band exact, point placement schematic.",
             fontsize=11, color=MUT)

    ax = fig.add_axes([0.08, 0.13, 0.56, 0.64])
    ax.set_facecolor(BG)

    hs = [120 * (1.35 ** k) for k in range(13)]
    lo = [BAND_LO * h ** -1.5 for h in hs]
    hi = [BAND_HI * h ** -1.5 for h in hs]
    cert = [C_CERT * h ** -1.5 for h in hs]

    ax.fill_between(hs, lo, hi, color=CYAN, alpha=0.20,
                    label="measured band ρ·h³ᐟ² ∈ [4.85, 24.2] (v818)")
    ax.plot(hs, cert, color=GREEN, lw=2.6,
            label="certified envelope 4.335·h^(−3/2) (v830, 73/73 frames)")
    # schematic sample points inside the exact band (log-uniform placement)
    import random
    rnd = random.Random(20260807)
    for h in [140 * (1.28 ** k) for k in range(14)]:
        c = math.exp(rnd.uniform(math.log(BAND_LO * 1.05), math.log(BAND_HI * 0.95)))
        ax.plot([h], [c * h ** -1.5], marker="o", ms=4.5, color=CYAN,
                mec=BG, mew=0.6, zorder=5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("window depth h", fontsize=10.5)
    ax.set_ylabel("floor ratio ρ", fontsize=10.5)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID)
    ax.grid(color=GRID, lw=0.5, alpha=0.4, which="both")
    leg = ax.legend(loc="lower left", fontsize=9, framealpha=0.0,
                    labelcolor=TXT)
    for t in leg.get_texts():
        t.set_color(TXT)

    # Right info card
    ax2 = fig.add_axes([0.68, 0.10, 0.29, 0.70])
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis("off")
    ax2.add_patch(FancyBboxPatch((2, 2), 96, 96,
                                 boxstyle="round,pad=1.2,rounding_size=2.4",
                                 fc=PANEL, ec=GRID, lw=1.3))
    ax2.text(50, 91, "Why “certified”, not “proven”", fontsize=12.5,
             fontweight="bold", color=TXT, ha="center")
    entries = [
        ("the skeleton", "exact Lagrange sum of squares;\npole × γ₁ pair a strict interval\n(14/14 rungs)", GREEN),
        ("the family", "top-100 pairs carry 97.7–98.1%\nof the floor at full sieve depth", CYAN),
        ("the tail", "closed for ALL h — explicit\nTrudgian constants, margins 10³–10⁶", GREEN),
        ("the blocker", "amplitudes, not phases: random-\nphase says h⁻¹, tower measures\nh^(−2.5) — see the wall triptych", AMBER),
    ]
    yy = 82
    for head, body, col in entries:
        ax2.text(50, yy, head, fontsize=10.5, fontweight="bold", color=col,
                 ha="center")
        ax2.text(50, yy - 10.5, body, fontsize=8.8, color=TXT, ha="center",
                 linespacing=1.35)
        yy -= 21

    axf = fig.add_axes([0, 0, 1, 0.06])
    axf.set_xlim(0, 100)
    axf.set_ylim(0, 100)
    axf.axis("off")
    axf.text(3.2, 50, FOOTER, fontsize=8.5, color=MUT)
    fig.savefig(os.path.join(FIGDIR, "a3_huellkurve.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 3 / Figure 2: family share + the played kill gates (v829)
# ============================================================================
def fig_a3_familien_anteil():
    fig = plt.figure(figsize=(12.8, 7.2))

    axh = fig.add_axes([0, 0.84, 1, 0.16])
    axh.set_xlim(0, 100)
    axh.set_ylim(0, 100)
    axh.axis("off")
    axh.text(3.2, 60, "The kill gates were played on purpose — and survived with growing margins",
             fontsize=19, fontweight="bold", color=TXT)
    axh.text(3.2, 18, "v829: sieve depth doubled (X = 18.375 → 25.5), dimension decoupled. If ρ were a depth law, the kill would have fired. It did not.",
             fontsize=11, color=MUT)

    ax = fig.add_axes([0.08, 0.14, 0.52, 0.62])
    ax.set_facecolor(BG)
    xs = list(range(len(KILL_MARGINS)))
    ax.bar(xs, KILL_MARGINS, width=0.62, color=GREEN, edgecolor="none",
           alpha=0.9)
    for i, m in enumerate(KILL_MARGINS):
        ax.text(i, m + 0.18, "×%.2f" % m, fontsize=9.6, color=TXT,
                ha="center")
    ax.axhline(1.0, color=RED, lw=2.0, ls="--")
    ax.set_xlim(-0.6, 8.6)
    ax.text(8.4, 1.45, "kill threshold ×1\n(envelope c = 4.85,\nno refit)",
            fontsize=8.8, color=RED, ha="right", linespacing=1.3)
    ax.set_xticks(xs)
    ax.set_xticklabels(["1", "2", "3", "4", "5", "6"], fontsize=9)
    ax.set_xlabel("depth station (X = 18.375 → 25.5)", fontsize=10.5)
    ax.set_ylabel("margin over kill gate K1", fontsize=10.5)
    ax.set_ylim(0, 10.2)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID)
    ax.grid(axis="y", color=GRID, lw=0.5, alpha=0.4)
    ax.text(0.0, 9.6, "margins grow monotonically — depth does not erode the floor",
            fontsize=10, color=GREEN)

    # Right column: the family takes over
    ax2 = fig.add_axes([0.64, 0.10, 0.33, 0.70])
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis("off")
    ax2.add_patch(FancyBboxPatch((2, 2), 96, 96,
                                 boxstyle="round,pad=1.2,rounding_size=2.4",
                                 fc=PANEL, ec=GRID, lw=1.3))
    ax2.text(50, 91, "The typed finding of the round", fontsize=12.5,
             fontweight="bold", color=TXT, ha="center")
    entries = [
        ("single pair collapses", "the pole × γ₁ gap grows\n×40 → ×673 in depth", RED),
        ("family takes over", "certified top-100 family carries\n97.7–98.1% of the floor", GREEN),
        ("angle gate K2", "min cos²θ = 0.849\n(kill threshold: < 0.5)", GREEN),
        ("still NOT a theorem", "battery-relative, necessary side,\nenvelope certified — not proven", AMBER),
    ]
    yy = 82
    for head, body, col in entries:
        ax2.text(50, yy, head, fontsize=10.5, fontweight="bold", color=col,
                 ha="center")
        ax2.text(50, yy - 9.5, body, fontsize=9, color=TXT, ha="center",
                 linespacing=1.35)
        yy -= 20

    axf = fig.add_axes([0, 0, 1, 0.06])
    axf.set_xlim(0, 100)
    axf.set_ylim(0, 100)
    axf.axis("off")
    axf.text(3.2, 50, FOOTER, fontsize=8.5, color=MUT)
    fig.savefig(os.path.join(FIGDIR, "a3_familien_anteil.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 3 / Figure 3: exclusion ladder -> locator -> window census
# ============================================================================
def fig_a3_ausschluss_detektor():
    fig = plt.figure(figsize=(12.8, 7.4))

    axh = fig.add_axes([0, 0.86, 1, 0.14])
    axh.set_xlim(0, 100)
    axh.set_ylim(0, 100)
    axh.axis("off")
    axh.text(3.2, 55, "A measuring device that finds zeros without knowing them",
             fontsize=19, fontweight="bold", color=TXT)
    axh.text(3.2, 8, "Certified positivity rungs (deepest: X = 25.5) invert into exclusion regions; the width profile peaks at true zeros (v825–v828). "
                     "No zero position is built in.",
             fontsize=10.5, color=MUT)

    # Left: depth law of the locator
    ax1 = fig.add_axes([0.06, 0.22, 0.24, 0.52])
    ax1.set_facecolor(BG)
    cols = [MUT, MUT, GREEN]
    ax1.bar([0, 1, 2], DEPTH_LAW, width=0.58,
            color=cols, edgecolor="none")
    for i, v in enumerate(DEPTH_LAW):
        ax1.text(i, v + 2.5, "%d%%" % v, fontsize=10.5, color=TXT, ha="center",
                 fontweight="bold" if i == 2 else "normal")
    ax1.set_xticks([0, 1, 2])
    ax1.set_xticklabels(["shallow", "mid", "deep"], fontsize=9)
    ax1.set_ylim(0, 112)
    ax1.set_yticks([0, 25, 50, 75, 100])
    ax1.set_ylabel("out-of-sample detection rate (%)", fontsize=10)
    for spine in ("top", "right"):
        ax1.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax1.spines[spine].set_color(GRID)
    ax1.grid(axis="y", color=GRID, lw=0.5, alpha=0.4)
    ax1.set_title("Locator v2 (preregistered):\n20/24 = 83% · 0% false positives",
                  fontsize=10.5, color=TXT, pad=8)
    ax1.text(-0.35, 105.5, "v1 failed honestly: 61% false peaks — on record",
             fontsize=7.8, color=MUT, ha="left")

    # Right: the window (60, 120] with the 25 true ordinates
    ax2 = fig.add_axes([0.37, 0.22, 0.59, 0.52])
    ax2.set_facecolor(BG)
    # typed misses: schematic assignment (1 pair merge + 3 prominence-limited)
    miss_idx = {13, 15, 20, 21}   # schematic; counts exact (21 + 4 = 25)
    for i, g in enumerate(ZEROS_60_120):
        if i in miss_idx:
            ax2.plot([g, g], [0.12, 0.78], color=AMBER, lw=2.0)
            ax2.plot([g], [0.86], marker="v", ms=7, color=AMBER)
        else:
            ax2.plot([g, g], [0.12, 0.78], color=GREEN, lw=2.0)
            ax2.plot([g], [0.86], marker="o", ms=5, color=GREEN, mec=BG,
                     mew=0.7)
    # pair-merge callout at the close pair 111.03 / 111.87
    ax2.annotate("pair merge below\ngrid resolution", xy=(111.45, 0.92),
                 xytext=(118.5, 1.16), fontsize=8.2, color=AMBER,
                 ha="center", linespacing=1.25,
                 arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.0))
    ax2.set_xlim(58, 126)
    ax2.set_ylim(0, 1.34)
    ax2.set_yticks([])
    ax2.set_xlabel("zero ordinate γ  —  window (60, 120]  at  X = 24.8125", fontsize=10)
    for spine in ("top", "right", "left"):
        ax2.spines[spine].set_visible(False)
    ax2.spines["bottom"].set_color(GRID)
    ax2.set_title("Window verification (v828): one certified object — location + exclusion + census",
                  fontsize=10.5, color=TXT, pad=8)
    ax2.text(59, 1.22, "green: located to ±0.25  (21 of 25 · max error 0.242 · zero unmatched peaks)",
             fontsize=9, color=GREEN)
    ax2.text(59, 0.02, "amber: 4 typed misses — 1 pair merge + 3 prominence-limited (assignment schematic, counts exact)",
             fontsize=8.4, color=AMBER)

    # bottom honesty strip
    axb = fig.add_axes([0, 0.0, 1, 0.15])
    axb.set_xlim(0, 100)
    axb.set_ylim(0, 100)
    axb.axis("off")
    axb.text(3.2, 82, "The census closes exactly: 21 hits + 4 typed misses = 25 = the rounded Riemann–von Mangoldt main term (25.237 → 25); "
                      "scrambled primes break all three axes at once.",
             fontsize=9.2, color=TXT)
    axb.text(3.2, 58, "Typed honestly: strictly weaker than classical verification (Turing proves the count exactly, δ = 0) — a necessity-side",
             fontsize=9.2, color=MUT)
    axb.text(3.2, 38, "consistency demonstration inside the verified strip, not an RH statement (PRIME.DETECTOR.WINDOW.01, open).",
             fontsize=9.2, color=MUT)
    axb.text(3.2, 12, FOOTER, fontsize=8.5, color=MUT)
    fig.savefig(os.path.join(FIGDIR, "a3_ausschluss_detektor.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 3 / Figure 4: the wall triptych (v831 / v835 / v836)
# ============================================================================
def fig_a3_wand_triptychon():
    fig, ax = new_canvas(12.8, 7.4)
    title(ax, "The wall, surveyed three ways — three closed routes, one named boundary",
          "Three independent attempts to prove the floor; three documented closures pointing at the same address.")

    cards = [
        ("Analytic route", CYAN, "v831 — ALIAS-CORRELATION-PAIRCORR",
         ["amplitudes carry the gap, not phases:",
          "tower law  −2.5 = −3.17 (amplitude)",
          "+ 0.67 (fading alignment)",
          "Guinand split: −994.15 + 995.15 cancel",
          "to 1% of random-comb scale;",
          "scramble explodes ×2·10⁶ – 1.7·10⁷"],
         "closed: bounding the comb at its own\n√-scale IS pair-correlation substance"),
        ("Structural route", VIOLET, "v835 — DOORS-CLOSED",
         ["the positive corner identity holds",
          "symbolically (free event weights) —",
          "and is therefore comb-blind:",
          "ĉ = −1 exact for all 136 events;",
          "all 128 characters censused:",
          "visibility  ⟺  identity defect"],
         "closed: positivity can be had, but it\ncannot see the primes"),
        ("Algebraic route", AMBER, "v836 — COMMUTANT-SOS-INFEASIBLE",
         ["degree-2 SOS over the canonical",
          "5-dim abelian subalgebra (39-dim",
          "commutant): SDP collapses to an LP",
          "with ONE feasible point (trivial);",
          "det form has signature (1, 2) —",
          "dual certificate q(0,1,0) = −1 < 0"],
         "closed: no positive algebraic\nrearrangement produces the floor"),
    ]
    x0 = 4
    w = 29.5
    for name, col, verdict, lines, closing in cards:
        ax.text(x0 + w / 2, 79.5, name, fontsize=13, fontweight="bold",
                color=col, ha="center")
        box(ax, x0, 42, w, 33, lines, fc=PANEL, ec=col, fs=8.8,
            title_line=verdict, title_color=col)
        ax.text(x0 + w / 2, 36.5, closing, fontsize=8.6, color=MUT,
                ha="center", linespacing=1.35)
        arrow(ax, x0 + w / 2, 31.5, 50, 24.5, color=col, lw=2.0)
        x0 += w + 2.6

    # the wall box
    box(ax, 22, 9, 56, 14.5, [
        "the floor–pair-correlation bridge: declared entry point, frozen kill criteria,",
        "explicitly promises NO unconditional proof — the arithmetic lives in the identification step",
    ], fc=PANEL2, ec=RED, fs=9.2,
        title_line="THE WALL:  PRIME.FLOOR.PAIRCORR.01  [O]", title_color=RED, lw=1.8)

    footer(ax, y=3.4)
    fig.savefig(os.path.join(FIGDIR, "a3_wand_triptychon.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 3 / Figure 5 (afternoon addendum): the two giants and the
# certified sliver (relation_corner_ladder_probe / excess_certified_
# skeleton_probe, frozen records)
# ============================================================================
# 12 of the 67 certified rungs (kz = 9, 14, 21, 28, 35, 45, 55, 71, 83,
# 97, 109, 121), verbatim from the frozen skeleton table: alpha, tau_X
# midpoint, lambda_min(S) (the structural giant), enclosure width.
GIANT_ALPHAS = [2.773, 3.296, 3.850, 4.263, 4.615, 4.920,
                5.198, 5.572, 5.802, 5.994, 6.146, 6.304]
GIANT_TAUS = [5.984e-04, 2.566e-04, 1.410e-04, 6.138e-05, 2.806e-05,
              1.152e-05, 8.228e-05, 9.993e-06, 7.599e-06, 6.405e-06,
              2.006e-05, 1.713e-05]
GIANT_LAMS = [-2.2847, -2.5676, -2.8330, -3.0119, -3.1532, -3.2674,
              -3.3673, -3.4891, -3.5600, -3.6168, -3.6604, -3.7038]
GIANT_WIDTHS = [5.38e-11, 8.49e-11, 2.63e-10, 6.00e-10, 1.21e-09,
                2.20e-09, 7.99e-10, 2.67e-09, 4.15e-09, 4.54e-09,
                4.10e-09, 6.61e-09]


def fig_a3_zwei_giganten():
    fig = plt.figure(figsize=(12.8, 7.4))

    axh = fig.add_axes([0, 0.86, 1, 0.14])
    axh.set_xlim(0, 100)
    axh.set_ylim(0, 100)
    axh.axis("off")
    axh.text(3.2, 55, "The two giants and the certified sliver:  τ_X = λ_min(S) + excess — positive, 67/67",
             fontsize=16.5, fontweight="bold", color=TXT)
    axh.text(3.2, 8, "Identified-corner coordinates (relation ladder + certified skeleton, frozen records): structure ≈ −3, comb ≈ +3 — "
                     "the sum is a sliver of 10⁻⁴..10⁻⁵, certified > 0 (12 of 67 rungs shown).",
             fontsize=9.5, color=MUT)

    # Top-left panel: the two giants (linear scale)
    ax1 = fig.add_axes([0.07, 0.50, 0.60, 0.32])
    ax1.set_facecolor(BG)
    bw = 0.10
    for a, t, s in zip(GIANT_ALPHAS, GIANT_TAUS, GIANT_LAMS):
        exc = t - s
        ax1.bar([a - bw / 2], [s], width=bw, color=CYAN, alpha=0.85)
        ax1.bar([a + bw / 2], [exc], width=bw, color=GREEN, alpha=0.9)
    ax1.axhline(0.0, color=TXT, lw=1.0, alpha=0.7)
    ax1.set_xlim(2.4, 8.1)
    ax1.set_ylim(-4.4, 4.4)
    ax1.set_ylabel("corner value", fontsize=10)
    ax1.set_xticks([3, 4, 5, 6])
    ax1.set_xticklabels([])
    for spine in ("top", "right"):
        ax1.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax1.spines[spine].set_color(GRID)
    ax1.grid(axis="y", color=GRID, lw=0.5, alpha=0.4)
    ax1.text(2.5, -3.9, "structural giant λ_min(S) — comb-blind, certifiable", fontsize=9, color=CYAN)
    ax1.text(2.5, 3.7, "comb giant (excess) — positive on all 67 rungs, +2.29 → +3.70", fontsize=9, color=GREEN)
    ax1.annotate("their sum:\nτ_X ~ 10⁻⁴..10⁻⁵\n(invisible at this scale —\nthe whole floor lives\nin the cancellation)",
                 xy=(6.36, 0.08), xytext=(7.35, 0.6), fontsize=8.4,
                 color=TXT, linespacing=1.35, ha="center",
                 arrowprops=dict(arrowstyle="->", color=TXT, lw=1.0,
                                 connectionstyle="arc3,rad=0.2"))

    # Bottom-left panel: margin vs certificate width (log scale)
    ax2 = fig.add_axes([0.07, 0.11, 0.60, 0.34])
    ax2.set_facecolor(BG)
    ax2.semilogy(GIANT_ALPHAS, GIANT_TAUS, color=GREEN, lw=2.2, marker="o",
                 ms=5, mec=BG, mew=0.6, label="certified margin τ_X (midpoint)")
    ax2.semilogy(GIANT_ALPHAS, GIANT_WIDTHS, color=AMBER, lw=2.0, marker="s",
                 ms=4.5, mec=BG, mew=0.6, label="enclosure width (5·10⁻¹¹ .. 7·10⁻⁹)")
    ax2.fill_between(GIANT_ALPHAS, GIANT_WIDTHS, GIANT_TAUS, color=GREEN,
                     alpha=0.10)
    ax2.set_xlim(2.4, 8.1)
    ax2.set_xlabel("window depth α  (ladder: 67 rungs, α = 2.77 → 6.30, masses to 3·10⁵)", fontsize=10)
    ax2.set_ylabel("log scale", fontsize=10)
    for spine in ("top", "right"):
        ax2.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax2.spines[spine].set_color(GRID)
    ax2.grid(color=GRID, lw=0.5, alpha=0.4, which="both")
    leg = ax2.legend(loc="upper right", fontsize=8.8, framealpha=0.0)
    for t in leg.get_texts():
        t.set_color(TXT)
    ax2.text(8.0, 1.6e-10, "gap: 3–5 orders of magnitude —\nevery enclosure strictly positive;\nextrapolated horizon α* ≈ 9.1,\nfar beyond the ladder end 6.30",
             fontsize=8.6, color=MUT, linespacing=1.35, ha="right")

    # Right card: the certified discriminator
    ax3 = fig.add_axes([0.70, 0.09, 0.28, 0.74])
    ax3.set_xlim(0, 100)
    ax3.set_ylim(0, 100)
    ax3.axis("off")
    ax3.add_patch(FancyBboxPatch((2, 2), 96, 96,
                                 boxstyle="round,pad=1.2,rounding_size=2.4",
                                 fc=PANEL, ec=GRID, lw=1.3))
    ax3.text(50, 92, "The certified discriminator", fontsize=12.5,
             fontweight="bold", color=TXT, ha="center")
    entries = [
        ("true prime comb", "τ_X enclosure strictly POSITIVE\non every rung (67/67)", GREEN),
        ("Epstein x²+5y² (h = 2)", "no Euler product — certificate\nFAILS: enclosure strictly negative\n(−0.79 / −1.10 / −1.23 on anchors)", RED),
        ("honest L-functions (h = 1)", "read exactly 0 by EXACT routing —\nSelberg-correct blindness", CYAN),
        ("scramble control", "enclosure disjoint from truth", AMBER),
        ("the wall, final form", "every finite instance proven;\nthe infinite quantifier open —\na uniform margin bound\n(finer-than-statistical)", TXT),
    ]
    yy = 85
    for head, body, col in entries:
        ax3.text(50, yy, head, fontsize=10, fontweight="bold", color=col,
                 ha="center")
        nl = body.count("\n") + 1
        ax3.text(50, yy - 3.8, body, fontsize=8.2, color=TXT,
                 ha="center", linespacing=1.35, va="top")
        yy -= 3.8 + 3.2 * nl + 4.4
    axf = fig.add_axes([0, 0, 1, 0.05])
    axf.set_xlim(0, 100)
    axf.set_ylim(0, 100)
    axf.axis("off")
    axf.text(3.2, 50, FOOTER + " · afternoon probes, exploration level, NO RH claim", fontsize=8.5, color=MUT)
    fig.savefig(os.path.join(FIGDIR, "a3_zwei_giganten.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 3 / Figure 6 (afternoon addendum): the wall map -- four doors
# closed, the GUE boundary, one door open
# ============================================================================
def fig_a3_wand_karte():
    fig, ax = new_canvas(12.8, 7.6)
    title(ax, "The wall map: four doors closed, one door open",
          "The afternoon of August 7 — four machine-checked impossibility theorems, the GUE boundary, and the relational input that passes every gate.")

    doors = [
        ("All corners", RED, "DOORS-CLOSED",
         ["128 characters collapse",
          "exactly to 18 classes;",
          "90-cell map: identity ⇒",
          "invisible, cell by cell"]),
        ("All tower levels", RED, "LEVEL2-CLOSED",
         ["m ≤ 3: 2,048 + 32,768",
          "characters; the jet refines",
          "the arithmetic — but reads",
          "position-blind at every level"]),
        ("All expectations", RED, "EXPECTATION-CLOSED",
         ["all 5,276 subgroups,",
          "74,259 components; pinching",
          "+ Stinespring: identity and",
          "placement never join"]),
        ("Position carriers", RED, "EXTREMAL PINNING",
         ["identity forces ĉ = −1:",
          "the whole mass locked;",
          "blind on EVERY self-",
          "consistent comb"]),
    ]
    x0 = 3.0
    w = 22.6
    for name, col, verdict, lines in doors:
        ax.text(x0 + w / 2, 81.5, name, fontsize=11.5, fontweight="bold",
                color=TXT, ha="center")
        box(ax, x0, 56, w, 23.0, lines, fc=PANEL, ec=col, fs=8.2,
            title_line=verdict, title_color=col)
        x0 += w + 1.6

    # GUE boundary strip
    box(ax, 3.0, 37.5, 94.0, 15.0, [
        "demand/GUE plateau 1.11 · band α ∈ 1–2 pinned in the unfolded coordinate · structural: 6/6 source-native variants land",
        "loop gain g = 1/(k²R²c_sup) = 0.53 < 1 — the wall conserves itself; flip side: GUE-rms closes only 39/73 rungs → finer-than-statistical",
    ], fc=PANEL2, ec=AMBER, fs=8.2,
        title_line="THE GUE BOUNDARY (saturation · ablation · loop gain · bridge map)", title_color=AMBER, lw=1.6)

    # the open door chain
    ax.text(3.0, 33.5, "The input the map dictated: MULTIPLICATIVITY (Λ = μ∗log) — relations BETWEEN events, the datum separating ζ from class-number-2 fakes:",
            fontsize=8.8, color=GREEN, fontweight="bold")
    chain = [
        ("RELATION-CARRIER-EXISTS", GREEN,
         ["all four gates pass — incl. the",
          "self-consistent null where every",
          "previous carrier died (14/70",
          "missing product relations)"]),
        ("EXCESS-NONNEGATIVE", GREEN,
         ["corner coordinates:",
          "τ_X = λ_min(S) + excess;",
          "excess > 0 on all 67 rungs,",
          "rising +2.29 → +3.70"]),
        ("SKELETON-CERTIFIED", GREEN,
         ["strict positive interval",
          "enclosures of τ_X, 67/67;",
          "the Epstein fake certified",
          "NEGATIVE on every anchor"]),
    ]
    x0 = 3.0
    w = 22.6
    for verdict, col, lines in chain:
        box(ax, x0, 10.0, w, 21.0, lines, fc=PANEL, ec=col, fs=8.2,
            title_line=verdict, title_color=col)
        arrow(ax, x0 + w + 0.2, 20.5, x0 + w + 1.5, 20.5, color=GREEN, lw=2.0)
        x0 += w + 1.6
    # the wall box (what stays open)
    box(ax, x0, 10.0, 97.0 - x0, 21.0, [
        "every finite instance proven;",
        "the INFINITE quantifier open:",
        "a uniform margin bound —",
        "finer-than-statistical · [O]",
    ], fc=PANEL2, ec=RED, fs=8.2,
        title_line="THE WALL, FINAL FORM", title_color=RED, lw=1.8)

    ax.text(3.0, 6.8, "PRIME.FLOOR.PAIRCORR.01 stays open — same address, sharpest coordinates so far.  All verdicts: frozen probes, exploration level (experiments/), machine-checked, report-only.  NO RH claim.",
            fontsize=8.6, color=MUT)
    footer(ax, y=2.8)
    fig.savefig(os.path.join(FIGDIR, "a3_wand_karte.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 4 / Figure 1: the shift register (v832 part A)
# ============================================================================
def fig_a4_schieberegister():
    fig, ax = new_canvas(12.8, 7.4)
    title(ax, "The shift register: the compiler budget from one affine rule",
          "T(x) = 2x − 2, proven symbolically (v832, 18/18 exact checks) — fixed point 2 = the sheet; the orbit of 4 is the compiler quintet.")

    # fixed point chip
    chip(ax, 3.5, 58, 13.5, "fixed point\nT(2) = 2 = |Z₂|\n(the sheet)", GREEN,
         fs=8.8, h=12)

    # orbit chain
    orbit = [("3", "11", "N_fam — prepended"),
             ("4", "100", "|μ₄| · the four marks"),
             ("6", "110", "|R⁺(A₃)|"),
             ("10", "1010", "anchor level A_L"),
             ("18", "10010", "3 families × 6"),
             ("34", "100010", "ℤ₆-lift")]
    x0 = 20
    w = 11.2
    for i, (val, binv, meaning) in enumerate(orbit):
        col = MUT if i == 0 else CYAN
        ax.add_patch(FancyBboxPatch((x0, 56), w, 16,
                                    boxstyle="round,pad=0.5,rounding_size=1.6",
                                    fc=PANEL, ec=col, lw=1.5))
        ax.text(x0 + w / 2, 67.5, val, fontsize=16, fontweight="bold",
                color=TXT, ha="center")
        ax.text(x0 + w / 2, 62.2, binv, fontsize=10.5, color=VIOLET,
                ha="center", family="monospace")
        ax.text(x0 + w / 2, 52.8, meaning, fontsize=7.6, color=MUT,
                ha="center")
        if i < len(orbit) - 1:
            arrow(ax, x0 + w + 0.3, 64, x0 + w + 2.0, 64, color=CYAN, lw=2.0)
        x0 += w + 2.4
    ax.text(56, 76.5, "each arrow:  x  ↦  2x − 2   (binary: shift left, subtract 10)",
            fontsize=10, color=CYAN, ha="center", style="italic")
    ax.text(56, 47.5, "the binary pattern makes the rule visible: a traveling leading 1, a standing bit at position 1 — the register shifts, the fixed-point remainder stays",
            fontsize=9, color=MUT, ha="center")

    # readout cards
    ax.text(4, 40.5, "The readout layer — every compiler budget is a word in the orbit (p₁..p₅ = 4, 6, 10, 18, 34):",
            fontsize=11, fontweight="bold", color=TXT)
    reads = [
        ("240", "roots of E₈\n= p₁·p₂·p₃ = 4·6·10"),
        ("248", "dim E₈ = 240 + (p₃−2);\np₄−p₃ = p₃−2 = 8 = rank"),
        ("30", "Coxeter number of E₈\n= p₂·p₃ / 2"),
        ("40", "roots of D₅\n= p₁·p₃"),
        ("48", "admissibility budget\n= 2·p₁·p₂"),
        ("41", "elementary layer: 10·b₁\n= e₁² + e₂² = 16 + 25"),
    ]
    x0 = 4
    for num, sub in reads:
        ax.add_patch(FancyBboxPatch((x0, 17), 14.2, 18,
                                    boxstyle="round,pad=0.5,rounding_size=1.6",
                                    fc=PANEL2, ec=GRID, lw=1.2))
        ax.text(x0 + 7.1, 29.5, num, fontsize=15, fontweight="bold",
                color=GREEN, ha="center")
        ax.text(x0 + 7.1, 23, sub, fontsize=7.8, color=TXT, ha="center",
                linespacing=1.3)
        x0 += 15.6

    ax.text(4, 10.5, "Before: a dozen separate corpus identities.  After: one rule, one seed, one readout table — exact integer/symbolic arithmetic, no floats, no fit.",
            fontsize=10, color=TXT)
    footer(ax, y=4.5)
    fig.savefig(os.path.join(FIGDIR, "a4_schieberegister.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 4 / Figure 2: the (1+i) ramification ladder (v833)
# ============================================================================
def fig_a4_verzweigungsleiter():
    fig, ax = new_canvas(12.8, 7.4)
    title(ax, "The ramification ladder: one Gaussian prime, four corpus roles",
          "v833 (33/33 exact checks): the four appearances of π₂ = 1+i are ONE object — a ladder of reductions of E₈ over ℤ[i].")

    # central chip
    ax.add_patch(Circle((50, 52), 7.2, fc=PANEL2, ec=VIOLET, lw=2.2))
    ax.text(50, 53.5, "1 + i", fontsize=17, fontweight="bold", color=VIOLET,
            ha="center")
    ax.text(50, 48.6, "N(1+i) = 2", fontsize=9, color=MUT, ha="center")

    roles = [
        ("Role 1 — norm doubling", GREEN, 5, 62,
         ["(1+J)ᵀ(1+J) = 2·I₈ exactly;",
          "elementary divisors (1⁴, 2⁴)",
          "announce the four bits"]),
        ("Role 2 — 4-bit address", CYAN, 68.5, 62,
         ["E₈ mod (1+i) = 𝔽₂⁴: the Gaussian",
          "code bridge — zero class empty,",
          "240 roots = 15 × 16 classes"]),
        ("Role 3 — non-splitting jet", AMBER, 5, 19,
         ["mod (1+i)²: ring iso UNIQUE among",
          "24 bijections; 0 of 65,536 sections",
          "deck-equivariant (full census);",
          "120 root pairs = the q=1 shell"]),
        ("Role 4 — metaplectic lift", RED, 68.5, 19,
         ["ζ₈ = (1+i)/√2:  (SH)³ = ζ₈·I;",
          "exact ℤ[ζ₈] census |C₂/μ₈| = 11,520,",
          "zero Galois-mixed elements"]),
    ]
    for name, col, x, y, lines in roles:
        h = 20 if y > 40 else 23
        box(ax, x, y, 26.5, h, lines, fc=PANEL, ec=col, fs=8.6,
            title_line=name, title_color=col)
    arrow(ax, 32.5, 70, 44.5, 57.5, color=GREEN, lw=1.8)
    arrow(ax, 68, 70, 55.5, 57.5, color=CYAN, lw=1.8)
    arrow(ax, 32.5, 34, 44.5, 47.5, color=AMBER, lw=1.8)
    arrow(ax, 68, 34, 55.5, 47.5, color=RED, lw=1.8)

    # tower strip
    box(ax, 5, 5.5, 90, 10.5, [], fc=PANEL2, ec=GRID)
    ax.text(50, 12.8, "The tower above (v835, structure-only): ℤ[i]/(1+i)^m, m = 1…5 — exact geometries 15·8^(m−1) / 35·16^(m−1) / 105·32^(m−1), "
                      "certified cb defect ≡ 0;",
            fontsize=9, color=TXT, ha="center")
    ax.text(50, 8.6, "honest scope: the level movement is the pure register dilution law 16^(1−m) — structure, no new arithmetic information.",
            fontsize=9, color=MUT, ha="center")

    footer(ax, y=1.8)
    fig.savefig(os.path.join(FIGDIR, "a4_verzweigungsleiter.png"), dpi=170)
    plt.close(fig)


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Self-test: the affine rule really generates the orbit and the budgets
    # (compute honestly, don't paint).
    orbit = [4]
    for _ in range(4):
        orbit.append(2 * orbit[-1] - 2)
    assert orbit == [4, 6, 10, 18, 34], orbit
    assert all(2 + 2 ** n == v for n, v in enumerate(orbit, start=1))
    p1, p2, p3, p4, p5 = orbit
    assert p1 * p2 * p3 == 240 and 240 + (p3 - 2) == 248
    assert p4 - p3 == p3 - 2 == 8
    assert p2 * p3 // 2 == 30 and p1 * p3 == 40 and 2 * p1 * p2 == 48
    assert bin(p5)[2:] == "100010"

    # Self-test for the two-giants data (frozen skeleton records): the
    # excess must be tau - lamS, positive, and the certificate width must
    # sit orders of magnitude below the margin on every shown rung.
    assert len(GIANT_ALPHAS) == len(GIANT_TAUS) == len(GIANT_LAMS) == len(GIANT_WIDTHS) == 12
    for t, s, wd in zip(GIANT_TAUS, GIANT_LAMS, GIANT_WIDTHS):
        assert t > 0 and s < 0 and (t - s) > 2.2, (t, s)
        assert wd < 1e-3 * t, (wd, t)

    fig_a3_huellkurve()
    fig_a3_familien_anteil()
    fig_a3_ausschluss_detektor()
    fig_a3_wand_triptychon()
    fig_a3_zwei_giganten()
    fig_a3_wand_karte()
    fig_a4_schieberegister()
    fig_a4_verzweigungsleiter()
    print("OK — 8 figures written to", FIGDIR)
