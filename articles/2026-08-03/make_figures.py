#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figures for the two Medium/LinkedIn articles of August 3, 2026 (English).

Generates all PNGs in articles/2026-08-03/figures/ with a consistent dark
design. All numbers come from the big-picture memo
(big_picture_2026-08-02_de.tex, August-3 chapters), the README and
website/lib/discipline.ts (generated suite statistics).

Run:  experiments/tfpt-discovery/.venv/bin/python make_figures.py
"""

import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

# ----------------------------------------------------------------------------
# Design system (dark, consistent)
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

FOOTER = "Source: TFPT verification suite · fixpoint-theory.com · as of August 3, 2026"


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
# Helper data
# ----------------------------------------------------------------------------
# First 30 zero ordinates of the Riemann zeta function (classical).
ZEROS = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
         37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
         52.970321, 56.446248, 58.347475, 60.831779, 65.112544,
         67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
         79.337375, 82.910381, 84.735493, 87.425275, 88.809111,
         92.491899, 94.651344, 95.870634, 98.831194, 101.317851]


def sigma3(n):
    return sum(d ** 3 for d in range(1, n + 1) if n % d == 0)


def lambda_geo(nmax):
    """Von Mangoldt reconstruction from the E8 shell counts r(2n) = 240*sigma3(n).

    Normalized coefficients c(n) = sigma3(n); Dirichlet recursion
    c(n) log n = sum_{d | n} Lam_L(d) c(n/d);  Lambda_geo = Lam_L / (1 + n^3).
    """
    c = {n: sigma3(n) for n in range(1, nmax + 1)}
    lam_l = {1: 0.0}
    for n in range(2, nmax + 1):
        s = sum(lam_l[d] * c[n // d]
                for d in range(2, n) if n % d == 0)
        lam_l[n] = c[n] * math.log(n) - s
    return {n: lam_l[n] / (1 + n ** 3) for n in range(2, nmax + 1)}


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, int(n ** 0.5) + 1))


def prime_power(n):
    """(p, k) if n = p^k, else None."""
    for p in range(2, n + 1):
        if is_prime(p):
            m, k = n, 0
            while m % p == 0:
                m //= p
                k += 1
            if m == 1:
                return p, k
    return None


# ============================================================================
# Article 1 / Figure 1: The compiler chain
# ============================================================================
def fig_a1_compiler_kette():
    fig, ax = new_canvas(12.8, 7.2)
    title(ax, "The compiler chain: from a boundary with four marks to the Standard Model",
          "Every stage is a machine-checked identity — no parameter fitting.")

    # Input: sphere with four marks
    ax.add_patch(FancyBboxPatch((3, 30), 22, 44,
                                boxstyle="round,pad=0.6,rounding_size=1.6",
                                fc=PANEL, ec=CYAN, lw=1.6))
    ax.text(14, 69.5, "The boundary", fontsize=13, fontweight="bold",
            color=CYAN, ha="center")
    circ_cx, circ_cy, r = 14.0, 53.0, 8.4
    ax.add_patch(Circle((circ_cx, circ_cy), r, fc="none", ec=TXT, lw=1.8))
    for k in range(4):
        angx = circ_cx + r * math.cos(math.pi / 2 * k)
        angy = circ_cy + r * math.sin(math.pi / 2 * k) * (100 / 100)
        ax.add_patch(Circle((angx, angy), 1.1, fc=AMBER, ec="none"))
    ax.text(14, 40.5, "sphere with four marks (μ₄)", fontsize=10.5,
            color=TXT, ha="center")
    ax.text(14, 36.6, "the only ℤ₄-symmetric\nconfiguration (conformally rigid)",
            fontsize=9, color=MUT, ha="center", linespacing=1.3)

    # Axioms below
    chip(ax, 3.5, 21.5, 10.4, "Axiom P1\nc₃ = 1/(8π)", CYAN, fs=9, h=7)
    chip(ax, 14.9, 21.5, 10.4, "Axiom P2\ng_car = 5", CYAN, fs=9, h=7)

    # Arrow 1
    arrow(ax, 26.5, 52, 32.5, 52)

    # Building blocks
    box(ax, 33, 40, 20, 24, [
        "two lattice building",
        "blocks, glued by the",
        "four-mark clock μ₄",
    ], title_line="D₅ ⊕ A₃  + μ₄", title_color=TXT, fs=10)

    arrow(ax, 54.5, 52, 60.5, 52)

    # E8
    box(ax, 61, 40, 16.5, 24, [
        "240 roots",
        "glue index 4",
        "the consistency hull",
    ], title_line="E₈", title_color=GREEN, ec=GREEN, fs=10)

    arrow(ax, 78.5, 52, 83.5, 52, color=GREEN)

    # Readouts
    outs = [
        ("SM gauge group", "(SU(3)×SU(2)×U(1))/ℤ₆"),
        ("3 generations", "exact within the compiler"),
        ("α⁻¹ = 137.0359992", "1.9σ from CODATA-2022"),
        ("27 predictions", "frozen before the data"),
    ]
    y0 = 71
    for name, sub in outs:
        ax.add_patch(FancyBboxPatch((84, y0 - 9.5), 13.2, 10.6,
                                    boxstyle="round,pad=0.45,rounding_size=1.6",
                                    fc=PANEL2, ec=GRID, lw=1.2))
        ax.text(90.6, y0 - 3.2, name, fontsize=9.6, fontweight="bold",
                color=TXT, ha="center")
        ax.text(90.6, - 6.8 + y0, sub, fontsize=8.2, color=MUT, ha="center")
        y0 -= 13.4

    ax.text(43, 30.5, "“compile”", fontsize=10, color=MUT,
            ha="center", style="italic")
    ax.text(69.2, 30.5, "“read out”", fontsize=10, color=MUT,
            ha="center", style="italic")

    ax.text(4, 12.5, "New since August 2/3: the seam axioms force the carrier curve y³ = x⁴ − 1 uniquely (v617) —",
            fontsize=10, color=TXT)
    ax.text(4, 8.8, "the curve is no longer a choice but the only solution. The boundary degree d = 4 is forced three independent ways (v624).",
            fontsize=10, color=TXT)
    footer(ax)
    fig.savefig(os.path.join(FIGDIR, "a1_compiler_kette.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 1 / Figure 2: Marks -> bits -> E8 code (Gaussian code bridge)
# ============================================================================
def fig_a1_marken_bits_code():
    fig, ax = new_canvas(12.8, 7.2)
    title(ax, "The Gaussian code bridge: the four marks are the four information bits",
          "E₈ over the Gaussian integers, reduced at the prime (1+i):  E₈(ℤ[i]) / (1+i)  ≅  𝔽₂⁴   —   freshly proven (v689) and formalized in Lean 4.")

    # Left: circle with four marks = bits
    ax.add_patch(FancyBboxPatch((3, 22), 26, 54,
                                boxstyle="round,pad=0.6,rounding_size=1.6",
                                fc=PANEL, ec=CYAN, lw=1.5))
    ax.text(16, 71.5, "Geometry", fontsize=12.5, fontweight="bold",
            color=CYAN, ha="center")
    cx, cy, r = 16, 50, 9.5
    ax.add_patch(Circle((cx, cy), r, fc="none", ec=TXT, lw=1.8))
    marks = [("1", GREEN, 90), ("2", GREEN, 180), ("3", GREEN, 270),
             ("4", AMBER, 0)]
    for label, col, deg in marks:
        mx = cx + r * math.cos(math.radians(deg))
        my = cy + r * math.sin(math.radians(deg))
        ax.add_patch(Circle((mx, my), 1.6, fc=col, ec="none"))
        lx = cx + (r - 3.6) * math.cos(math.radians(deg))
        ly = cy + (r - 3.6) * math.sin(math.radians(deg))
        ax.text(lx, ly, label, fontsize=11, fontweight="bold", color=col,
                ha="center", va="center")
    ax.text(16, 33.5, "four marks on the boundary — one bit per μ₄ pair",
            fontsize=9.2, color=TXT, ha="center")
    ax.text(16, 29.8, "bits 1–3: the three families", fontsize=9.2, color=GREEN,
            ha="center")
    ax.text(16, 26.4, "bit 4: the anchor", fontsize=9.2, color=AMBER,
            ha="center")

    # Middle: arrow
    arrow(ax, 30.5, 49, 39.5, 49, color=VIOLET, lw=3)
    ax.text(35, 54, "geometry", fontsize=10.5, color=VIOLET, ha="center",
            fontweight="bold")
    ax.text(35, 50.6, "mod 2", fontsize=10.5, color=VIOLET, ha="center",
            fontweight="bold")
    ax.text(35, 43.5, "reduction at the\nGaussian prime (1+i)", fontsize=8.6,
            color=MUT, ha="center", linespacing=1.3)

    # Right: 4x4 grid of the 16 classes
    ax.add_patch(FancyBboxPatch((41, 22), 33, 54,
                                boxstyle="round,pad=0.6,rounding_size=1.6",
                                fc=PANEL, ec=VIOLET, lw=1.5))
    ax.text(57.5, 71.5, "Information: 𝔽₂⁴ — 16 classes", fontsize=12.5,
            fontweight="bold", color=VIOLET, ha="center")
    gx0, gy0, cw, chh, gap = 44.5, 27.5, 6.4, 8.8, 0.9
    idx = 0
    for row in range(4):
        for col in range(4):
            x = gx0 + col * (cw + gap)
            y = gy0 + (3 - row) * (chh + gap)
            if idx == 0:
                ax.add_patch(Rectangle((x, y), cw, chh, fc=BG, ec=GRID, lw=1.1))
                ax.text(x + cw / 2, y + chh / 2 + 1.2, "0000", fontsize=8,
                        color=MUT, ha="center")
                ax.text(x + cw / 2, y + chh / 2 - 2.0, "empty\n(proven)",
                        fontsize=6.8, color=MUT, ha="center", linespacing=1.15)
            else:
                ax.add_patch(Rectangle((x, y), cw, chh, fc=PANEL2, ec=VIOLET,
                                       lw=1.0))
                ax.text(x + cw / 2, y + chh / 2 + 1.2, format(idx, "04b"),
                        fontsize=8, color=TXT, ha="center")
                ax.text(x + cw / 2, y + chh / 2 - 2.2, "16 roots",
                        fontsize=6.8, color=GREEN, ha="center")
            idx += 1
    ax.text(57.5, 24.6, "all 240 E₈ roots fall exactly 15 × 16 across the classes",
            fontsize=9.2, color=MUT, ha="center")

    # Right column: consequences
    consequences = [
        ("= Hamming code [8,4,4] / RM(1,3)",
         "the v638 dictionary, now a residue-class\nmap instead of a table comparison"),
        ("every 1-bit error uniquely correctable",
         "error correction is a theorem of the\ngeometry, not a metaphor (v626)"),
        ("formalized in Lean 4",
         "GaussianCodeBridge.lean — kernel-checked,\nno “sorry”"),
    ]
    y0 = 66
    for head, sub in consequences:
        ax.add_patch(FancyBboxPatch((76.5, y0 - 11), 21, 12.6,
                                    boxstyle="round,pad=0.5,rounding_size=1.6",
                                    fc=PANEL2, ec=GREEN, lw=1.2))
        ax.text(87, y0 - 1.8, head, fontsize=8.8, fontweight="bold", color=TXT,
                ha="center")
        ax.text(87, y0 - 7.2, sub, fontsize=7.7, color=MUT, ha="center",
                linespacing=1.3)
        y0 -= 15.6

    ax.text(4, 12, "Why it matters: a lattice over the integers carries a binary structure — because the binary structure IS the geometry mod 2.",
            fontsize=10, color=TXT)
    footer(ax, y=6.5)
    fig.savefig(os.path.join(FIGDIR, "a1_marken_bits_code.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 1 / Figure 3: The three-fields pattern
# ============================================================================
def fig_a1_drei_felder():
    fig, ax = new_canvas(12.8, 7.2)
    title(ax, "One pattern, three fields: the continuum forces the discrete datum",
          "The same figure of thought — smooth consistency conditions leave exactly one discrete outcome.")

    cols = [
        ("Physics constants", CYAN,
         ["seam axioms +", "reflection positivity", "(analytic consistency)"],
         ["E₈ · 3 generations", "α⁻¹ = 137.0359992"],
         "The curve y³ = x⁴ − 1 is the only\nsolution of the seam axioms (v617)."),
        ("Code / information", VIOLET,
         ["geometry of the curve", "over the Gaussian", "integers ℤ[i] (μ₄ clock)"],
         ["4 information bits", "= Hamming [8,4,4]"],
         "Reduction mod (1+i): the four marks\nare the four bits (v689 + Lean)."),
        ("Prime numbers", AMBER,
         ["Γ-flow of the cover", "(divergence avoidance", "in the background)"],
         ["prime masses and", "positions in the corridor"],
         "masses: unique counterterms (0.11%);\npositions forced; corridor point ≈ 0.53."),
    ]
    x0 = 4
    w = 29.5
    for name, col, top, bottom, note in cols:
        # heading
        ax.text(x0 + w / 2, 79, name, fontsize=13.5, fontweight="bold",
                color=col, ha="center")
        # continuum box
        box(ax, x0, 55.5, w, 19, top, fc=PANEL, ec=col, fs=10,
            title_line="Continuous side", title_color=MUT)
        # arrow
        arrow(ax, x0 + w / 2, 53.5, x0 + w / 2, 47, color=col, lw=2.8)
        ax.text(x0 + w / 2 + 1.2, 50.2, "forces", fontsize=9.5, color=col,
                ha="left", style="italic")
        # datum box
        box(ax, x0, 31, w, 15, bottom, fc=PANEL2, ec=col, fs=10.5,
            title_line="Discrete datum", title_color=MUT)
        ax.text(x0 + w / 2, 24.5, note, fontsize=8.6, color=MUT, ha="center",
                linespacing=1.35)
        x0 += w + 2.6

    ax.text(50, 13.5, "Five languages, one object:  code · lattice · Weil form · orbifold · Hodge form  —  the transitions are machine-checked identities, not analogies.",
            fontsize=10.5, color=TXT, ha="center")
    footer(ax, y=6.5)
    fig.savefig(os.path.join(FIGDIR, "a1_drei_felder.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 1 / Figure 4: Lambda from pure lattice counting
# ============================================================================
def fig_a1_lambda_gitter():
    lam = lambda_geo(40)

    fig = plt.figure(figsize=(12.8, 7.2))
    ax_head = fig.add_axes([0, 0.82, 1, 0.18])
    ax_head.set_xlim(0, 100)
    ax_head.set_ylim(0, 100)
    ax_head.axis("off")
    ax_head.text(4, 62, "Primes as the shadow of the geometry",
                 fontsize=19, fontweight="bold", color=TXT)
    ax_head.text(4, 30, "E₈ lattice  →  count shells: r(2n) = 240·σ₃(n)  →  Dirichlet recursion  →  Λ_geo(n) = Λ(n)  exactly,",
                 fontsize=11.5, color=MUT)
    ax_head.text(4, 4, "no ζ, no prime input — machine-checked up to n = 20,000 (v686/v695).",
                 fontsize=11.5, color=MUT)

    ax = fig.add_axes([0.07, 0.14, 0.88, 0.62])
    ax.set_facecolor(BG)
    ns = list(range(2, 41))
    for n in ns:
        v = lam[n]
        if v < 1e-9:
            continue
        pp = prime_power(n)
        col = GREEN if (pp and pp[1] == 1) else AMBER
        ax.bar(n, v, width=0.72, color=col, edgecolor="none")
        if pp:
            p, k = pp
            lbl = str(p) if k == 1 else f"{p}^{k}"
            ax.text(n, v + 0.11, lbl, fontsize=8.6, color=TXT, ha="center")
    # hint the zero line for non-prime-powers
    for n in ns:
        if lam[n] < 1e-9:
            ax.plot([n], [0.035], marker="o", ms=2.4, color=GRID)

    ax.set_xlim(1, 41)
    ax.set_ylim(0, 4.35)
    ax.set_xlabel("n", fontsize=11)
    ax.set_ylabel("reconstructed weight  Λ_geo(n)", fontsize=11)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID)
    ax.grid(axis="y", color=GRID, lw=0.6, alpha=0.5)

    ax.text(3, 4.0, "bars only on prime powers — exactly the von Mangoldt function Λ(n) = log p",
            fontsize=10.5, color=TXT)
    ax.text(3, 3.68, "green: primes · amber: higher prime powers (4, 8, 9, 16, 25, 27, 32) · dots: exactly zero",
            fontsize=9.2, color=MUT)

    ax_foot = fig.add_axes([0, 0, 1, 0.07])
    ax_foot.set_xlim(0, 100)
    ax_foot.set_ylim(0, 100)
    ax_foot.axis("off")
    ax_foot.text(4, 50, FOOTER + " · bars computed live via the σ₃ recursion (identical to Λ)",
                 fontsize=8.5, color=MUT)
    fig.savefig(os.path.join(FIGDIR, "a1_lambda_gitter.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 1 / Figure 5: Honesty dashboard
# ============================================================================
def fig_a1_ehrlichkeit():
    fig, ax = new_canvas(12.8, 7.6)
    title(ax, "The honesty dashboard",
          "What is proven, what is measured, what is open — per the theory's own status ledger (771 rows; “the ledger wins”).")

    colw = 30.0
    colh = 46
    ytop = 82

    # [E] proven
    box(ax, 4, ytop - colh, colw, colh, [], fc=PANEL, ec=GREEN, lw=1.6)
    ax.text(4 + colw / 2, ytop - 4, "[E] exactly proven", fontsize=13,
            fontweight="bold", color=GREEN, ha="center")
    e_items = [
        "E₈ closure from two axioms",
        "Gaussian code bridge (4 marks = 4 bits)",
        "Λ from pure E₈ lattice counting",
        "W1: window form = Weil operator",
        "det S > 0 on the whole surface",
        "error correction: 1-bit error ↦ unique",
    ]
    yy = ytop - 10
    for it in e_items:
        ax.text(6.2, yy, "✓", fontsize=11, color=GREEN, ha="left")
        ax.text(9.2, yy, it, fontsize=9.6, color=TXT, ha="left")
        yy -= 6.0

    # [M] measured
    box(ax, 35.5, ytop - colh, colw, colh, [], fc=PANEL, ec=AMBER, lw=1.6)
    ax.text(35.5 + colw / 2, ytop - 4, "[M] measured / reproducible",
            fontsize=13, fontweight="bold", color=AMBER, ha="center")
    m_items = [
        "α⁻¹ = 137.0359992 (1.9σ, CODATA-22)",
        "C = 1 on all 67 complete windows",
        "window census: 60/70 closed*",
        "mass law: shooting median 0.11%",
        "corridor position 0.53 (IQR 0.51–0.56)",
        "*modulo cited classical bounds",
    ]
    yy = ytop - 10
    for i, it in enumerate(m_items):
        mark = "•" if i < 5 else " "
        ax.text(37.7, yy, mark, fontsize=11, color=AMBER, ha="left")
        ax.text(40.7, yy, it, fontsize=9.4,
                color=TXT if i < 5 else MUT, ha="left")
        yy -= 6.0

    # [O] open
    box(ax, 67, ytop - colh, colw, colh, [], fc=PANEL, ec=RED, lw=1.6)
    ax.text(67 + colw / 2, ytop - 4, "[O] honestly open", fontsize=13,
            fontweight="bold", color=RED, ha="center")
    o_items = [
        "NO proof of the Riemann Hypothesis",
        "NO confirmed physical prediction yet",
        "gate 1: v_geo — the one metrology unit",
        "gate 2: seam identification (SEAM.EQUIV)",
        "gate 3: F_transfer (four interfaces)",
        "Z1 operator (Hilbert–Pólya) — wanted",
    ]
    yy = ytop - 10
    for it in o_items:
        ax.text(69.2, yy, "○", fontsize=10, color=RED, ha="left")
        ax.text(72.2, yy, it, fontsize=9.4, color=TXT, ha="left")
        yy -= 6.0

    # Bottom band: suite statistics
    box(ax, 4, 12, 93, 17, [], fc=PANEL2, ec=GRID)
    ax.text(50.5, 25.2, "The checking machinery (openly reproducible: python verification/run_all.py)",
            fontsize=11, fontweight="bold", color=TXT, ha="center")
    stats = [
        ("694", "modules (up to v700)"),
        ("6,847", "automated checks"),
        ("1,698", "negative controls"),
        ("243", "documented kills"),
        ("57", "Lean 4 proof modules"),
        ("27", "frozen predictions"),
    ]
    x = 9
    for num, lab in stats:
        ax.text(x, 20.2, num, fontsize=15, fontweight="bold", color=CYAN,
                ha="center")
        ax.text(x, 15.6, lab, fontsize=8.6, color=MUT, ha="center")
        x += 15.6

    footer(ax, y=5.5)
    fig.savefig(os.path.join(FIGDIR, "a1_ehrlichkeit_dashboard.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 2 / Figure 1: Zeros on the line + the music of the primes
# ============================================================================
def fig_a2_nullstellen():
    fig = plt.figure(figsize=(12.8, 7.2))

    axh = fig.add_axes([0, 0.86, 1, 0.14])
    axh.set_xlim(0, 100)
    axh.set_ylim(0, 100)
    axh.axis("off")
    axh.text(3.2, 55, "The music of the primes", fontsize=19,
             fontweight="bold", color=TXT)
    axh.text(3.2, 10, "Left: the critical strip — every known zero sits exactly on the center line.   Right: their frequencies trace out the primes.",
             fontsize=11, color=MUT)

    # Left: critical strip
    ax1 = fig.add_axes([0.06, 0.12, 0.30, 0.68])
    ax1.set_facecolor(BG)
    ax1.axvspan(0, 1, color=PANEL, alpha=1.0)
    ax1.axvline(0.5, color=GREEN, lw=2.0)
    ax1.axvspan(0, 1, ymin=0, ymax=14.134725 / 105, color=PANEL2, alpha=0.9)
    for g in ZEROS:
        ax1.plot([0.5], [g], marker="o", ms=5.5, color=CYAN,
                 mec=BG, mew=0.8, zorder=5)
    ax1.set_xlim(-0.25, 1.25)
    ax1.set_ylim(0, 105)
    ax1.set_xticks([0, 0.5, 1])
    ax1.set_xticklabels(["0", "½", "1"])
    ax1.set_xlabel("real part", fontsize=10)
    ax1.set_ylabel("height t", fontsize=10)
    for spine in ax1.spines.values():
        spine.set_color(GRID)
    ax1.annotate("first zero\nγ₁ = 14.13", xy=(0.5, 14.13),
                 xytext=(0.72, 22), fontsize=9, color=TXT,
                 arrowprops=dict(arrowstyle="->", color=MUT, lw=1.2))
    ax1.text(0.5, 6.5, "zero-free zone\n(classical, ~100 years old)",
             fontsize=8, color=MUT, ha="center", linespacing=1.3)
    ax1.text(0.5, 101.5, "critical line Re(s) = ½", fontsize=9,
             color=GREEN, ha="center")
    ax1.set_title("Where the zeros live", fontsize=11.5, color=TXT, pad=10)

    # Right: superposition
    ax2 = fig.add_axes([0.45, 0.12, 0.51, 0.68])
    ax2.set_facecolor(BG)
    xs = [1.5 + i * 0.002 for i in range(int((10.5 - 1.5) / 0.002) + 1)]
    ys = [-sum(math.cos(g * math.log(x)) for g in ZEROS) for x in xs]
    ax2.plot(xs, ys, color=CYAN, lw=1.4)
    for pp in [2, 3, 4, 5, 7, 8, 9]:
        ax2.axvline(pp, color=AMBER, lw=1.1, ls="--", alpha=0.85)
        ax2.text(pp, 13.6, str(pp), fontsize=10, color=AMBER, ha="center")
    ax2.set_xlim(1.5, 10.5)
    ax2.set_ylim(-7, 15.2)
    ax2.set_xlabel("x", fontsize=10)
    ax2.set_ylabel("superposition of the zero waves", fontsize=10)
    for spine in ("top", "right"):
        ax2.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax2.spines[spine].set_color(GRID)
    ax2.grid(color=GRID, lw=0.5, alpha=0.4)
    ax2.set_title("The first 30 zeros as an orchestra: the peaks sit on prime powers",
                  fontsize=11.5, color=TXT, pad=10)
    ax2.text(9.0, -5.9, "−Σ cos(γₖ·log x), k = 1…30", fontsize=9, color=MUT,
             ha="center")

    axf = fig.add_axes([0, 0, 1, 0.06])
    axf.set_xlim(0, 100)
    axf.set_ylim(0, 100)
    axf.axis("off")
    axf.text(3.2, 50, FOOTER, fontsize=8.5, color=MUT)
    fig.savefig(os.path.join(FIGDIR, "a2_nullstellen_linie.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 2 / Figure 2: The detector / falsifier
# ============================================================================
def fig_a2_detektor():
    fig, ax = new_canvas(12.8, 7.4)
    title(ax, "The detector: a machine that could not stay silent about a false RH",
          "The window form proves positivity on the surface — and would constructively flag any off-line zero in the resolved band (v688/v694).")

    # Pipeline
    box(ax, 3.5, 62, 19, 16, ["prime data inside a", "window of depth α"],
        title_line="Input", title_color=CYAN, ec=CYAN, fs=9.6)
    arrow(ax, 23.5, 70, 28.5, 70)
    box(ax, 29, 62, 21, 16, ["window form (matrix)", "= discrete Weil operator"],
        title_line="Test bench", title_color=CYAN, fs=9.6)
    arrow(ax, 51, 70, 56, 70)
    box(ax, 56.5, 62, 16.5, 16, ["smallest eigenvalue", "λ_min ≥ 0 ?"],
        title_line="Readout", title_color=CYAN, fs=9.6)

    # Green output
    arrow(ax, 74, 74, 80.5, 76, color=GREEN)
    box(ax, 81, 71, 15.5, 13.5, ["the case on every", "window tested"],
        title_line="positive ✓", title_color=GREEN, ec=GREEN, fs=8.8)
    # Red output
    arrow(ax, 74, 66, 80.5, 62, color=RED)
    box(ax, 81, 53.5, 15.5, 13.5, ["explicit test vector", "swings negative"],
        title_line="alarm ✗", title_color=RED, ec=RED, fs=8.8)

    # Mechanism card
    box(ax, 3.5, 29, 45, 19, [
        "A zero off the line (½ + δ) couples with cosh",
        "amplification; the matched filter is a closed formula.",
        "Window deep enough (2αδ ≥ 1.97) → guaranteed alarm.",
    ], title_line="The mechanism (constructive, no eigensolver)",
        title_color=TXT, fs=9.2, align="left")

    box(ax, 51.5, 29, 45.5, 19, [
        "46 of 48 adversarial conspiracy scenarios: alarm anyway.",
        "The remaining 2: provably below resolution — deeper",
        "windows settle them. Closing tally: 0 exceptions in 97 tests.",
    ], title_line="Can the detector be fooled? (masking test)",
        title_color=TXT, fs=9.2, align="left")

    # Calibration
    ax.text(4.5, 23.5, "Calibrated on systems where the answer is known:",
            fontsize=11, fontweight="bold", color=TXT)
    chip(ax, 4.5, 12, 28, "Ramanujan graphs (RH analogue proven):\npasses ✓", GREEN, fs=9, h=8.4)
    chip(ax, 35, 12, 29, "Epstein zeta (no Euler product):\nbreaks — 12 off-line zeros found ✗", RED, fs=9, h=8.4)
    chip(ax, 66.5, 12, 30.5, "scrambled primes:\nbreaks — by ~13 orders of magnitude ✗", RED, fs=9, h=8.4)

    footer(ax, y=4.5)
    fig.savefig(os.path.join(FIGDIR, "a2_detektor_schema.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 2 / Figure 3: The window map 60/70
# ============================================================================
def fig_a2_fensterkarte():
    fig, ax = new_canvas(12.8, 7.2)
    title(ax, "The window map: 60 of 70 closed unconditionally",
          "T-B census (v692/v693): one determinant inequality decides per window — the remainder carries an exact target height T*.")

    # Waffle: 70 squares, 10 columns x 7 rows
    open_windows = ["1359", "1721", "1868", "2018", "2093",
                    "2472", "2475", "2630", "2656", "5690"]
    gx0, gy0 = 6, 26
    cw, chh, gap = 5.6, 6.6, 1.15
    k = 0
    for row in range(7):
        for col in range(10):
            x = gx0 + col * (cw + gap)
            y = gy0 + (6 - row) * (chh + gap)
            if k < 60:
                ax.add_patch(Rectangle((x, y), cw, chh, fc=GREEN, ec=BG,
                                       lw=1.0, alpha=0.88))
            else:
                ax.add_patch(Rectangle((x, y), cw, chh, fc=AMBER, ec=BG,
                                       lw=1.0, alpha=0.95))
                ax.text(x + cw / 2, y + chh / 2, open_windows[k - 60],
                        fontsize=7.6, color=BG, ha="center", va="center",
                        fontweight="bold")
            k += 1
    ax.text(6, 20.8, "green: closed unconditionally-modulo-citations (Platt–Trudgian 2021 · Hasanalizade–Shen–Wong 2022 · explicit Ingham form 2025)",
            fontsize=9.2, color=GREEN)
    ax.text(6, 16.8, "amber: open — labeled with the window depth h; layout schematic, count exact",
            fontsize=9.2, color=AMBER)

    # Right info card
    box(ax, 76, 24, 21, 50, [], fc=PANEL, ec=GRID)
    ax.text(86.5, 69.5, "The remainder is", fontsize=11.5, fontweight="bold",
            color=TXT, ha="center")
    ax.text(86.5, 65.9, "a list of numbers", fontsize=11.5, fontweight="bold",
            color=TXT, ha="center")
    rest = [
        ("9 windows", "T* ≈ 1–3 × 10¹³"),
        ("1 window (h = 5690)", "T* ≈ 8.5 × 10¹⁴"),
        ("today's computing reach", "3 × 10¹²"),
    ]
    yy = 59
    for a, b in rest:
        ax.text(86.5, yy, a, fontsize=9.4, color=TXT, ha="center")
        ax.text(86.5, yy - 3.8, b, fontsize=9.6, color=CYAN, ha="center")
        yy -= 10.2
    ax.text(86.5, 28.6, "no diffuse “too tight”\nanymore — named targets",
            fontsize=8.6, color=MUT, ha="center", linespacing=1.35)

    footer(ax, y=8)
    fig.savefig(os.path.join(FIGDIR, "a2_fensterkarte.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 2 / Figure 4: The Ihara blueprint
# ============================================================================
def fig_a2_ihara():
    fig, ax = new_canvas(12.8, 7.4)
    title(ax, "The Ihara blueprint: an identically built machine — one part missing",
          "In the graph lab the RH analogue is proven — and the target factorization exists there exactly (v691).")

    # Left machine: graph world
    ax.text(26, 79.5, "Graph world (Ihara) — proven", fontsize=13,
            fontweight="bold", color=GREEN, ha="center")
    box(ax, 8, 62, 36, 14, ["adjacency operator A of the graph"],
        title_line="Engine: present ✓", title_color=GREEN, ec=GREEN, fs=10)
    arrow(ax, 26, 60.5, 26, 55, color=GREEN)
    box(ax, 8, 39.5, 36, 14, ["Chebyshev sum of squares (always ≥ 0)",
                              "+ defect term"],
        title_line="Factorization: exact", title_color=TXT, fs=9.6)
    arrow(ax, 26, 38, 26, 32.5, color=GREEN)
    box(ax, 8, 17, 36, 14, ["defect ≥ 0  ⟺  Ramanujan property",
                            "— the RH analogue: a theorem"],
        title_line="Result: positive ✓", title_color=GREEN, ec=GREEN, fs=9.6)

    # Right machine: zeta world
    ax.text(74, 79.5, "ζ world (primes) — open", fontsize=13,
            fontweight="bold", color=AMBER, ha="center")
    box(ax, 56, 62, 36, 14, ["Z1: a self-adjoint geometric operator",
                             "whose traces are the window moments"],
        title_line="Engine: WANTED ? (Hilbert–Pólya)", title_color=RED,
        ec=RED, fs=9.2, ls="--")
    arrow(ax, 74, 60.5, 74, 55, color=AMBER)
    box(ax, 56, 39.5, 36, 14, ["index lemma (exact): our window form is",
                               "the sine defect half of the same scheme"],
        title_line="Factorization: exact ✓", title_color=TXT, fs=9.2)
    arrow(ax, 74, 38, 74, 32.5, color=AMBER)
    box(ax, 56, 17, 36, 14, ["defect ≥ 0 for all windows  ⟺  RH core (W3)",
                             "— the norm bound Z2 would be RH itself"],
        title_line="Result: open ○", title_color=AMBER, ec=AMBER, fs=9.2)

    # Connecting arrow
    arrow(ax, 45, 46.5, 55, 46.5, color=CYAN, lw=2.0, ls="--")
    ax.text(50, 50, "identically built", fontsize=9.5, color=CYAN, ha="center",
            style="italic")

    ax.text(50, 10.5, "Now measurable: snap the prime positions onto an artificial grid (“fake primes”) and positivity breaks exactly at the resonance grid —",
            fontsize=9.6, color=TXT, ha="center")
    ax.text(50, 7.0, "Euler product on: positivity. Euler product off: resonance break. The factorization localizes the conjecture in the missing part — it does not bypass it.",
            fontsize=9.6, color=MUT, ha="center")
    footer(ax, y=2.4)
    fig.savefig(os.path.join(FIGDIR, "a2_ihara_blaupause.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 2 / Figure 5: The corridor with the point at 0.53
# ============================================================================
def fig_a2_korridor():
    fig = plt.figure(figsize=(12.8, 7.2))
    axh = fig.add_axes([0, 0.85, 1, 0.15])
    axh.set_xlim(0, 100)
    axh.set_ylim(0, 100)
    axh.axis("off")
    axh.text(3.2, 55, "The positivity corridor: arithmetic picks an interior point",
             fontsize=19, fontweight="bold", color=TXT)
    axh.text(3.2, 8, "For every prime-power slot the admissible mass interval is exactly computable. The true mass does not sit at the edge — it sits at ≈ 0.53.",
             fontsize=11, color=MUT)

    ax = fig.add_axes([0.095, 0.14, 0.60, 0.63])
    ax.set_facecolor(BG)

    slots = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32,
             37, 41, 43, 47, 49, 53, 59, 61, 64, 67, 71, 73, 79, 81, 83, 89, 97]
    xpos = list(range(len(slots)))

    # Corridor 0..1 as a band
    ax.axhspan(0, 1, color=PANEL, alpha=1.0)
    ax.axhline(0, color=GRID, lw=1.2)
    ax.axhline(1, color=GRID, lw=1.2)
    ax.text(0.2, 0.93, "upper edge (closed resolvent formula)",
            fontsize=8.6, color=MUT, ha="left")
    ax.text(0.2, 0.035, "lower edge (closed resolvent formula)",
            fontsize=8.6, color=MUT, ha="left")

    # IQR band + median (measured distribution over 200 slot-window pairs)
    ax.axhspan(0.511, 0.559, color=CYAN, alpha=0.28)
    ax.axhline(0.534, color=CYAN, lw=2.2)
    ax.text(0.2, 0.585, "measured: median 0.534 · IQR [0.511 – 0.559]\n(200 slot-window pairs; rendering schematic)",
            fontsize=9.0, color=CYAN, linespacing=1.3)

    # drift-to-center hint
    ax.annotate("drifts toward the center with log n",
                xy=(len(slots) - 3, 0.52), xytext=(len(slots) - 14.5, 0.30),
                fontsize=9, color=MUT,
                arrowprops=dict(arrowstyle="->", color=MUT, lw=1.1))

    # outlier slots of the energy functional
    for s in (16, 64, 81):
        i = slots.index(s)
        ax.plot([i], [0.945], marker="v", ms=9, color=RED, zorder=6)
        ax.text(i, 1.05, str(s), fontsize=9.4, color=RED, ha="center",
                fontweight="bold")

    ax.set_xticks(xpos[::2])
    ax.set_xticklabels([str(slots[i]) for i in range(0, len(slots), 2)],
                       fontsize=8)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0 (edge)", "0.25", "0.5", "0.75", "1 (edge)"])
    ax.set_xlabel("prime-power slots  n = p^k  (the “comb”)", fontsize=10.5)
    ax.set_ylabel("position inside the admissible corridor", fontsize=10.5)
    ax.set_xlim(-0.8, len(slots) - 0.2)
    ax.set_ylim(-0.14, 1.16)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID)

    # Right info card
    ax2 = fig.add_axes([0.73, 0.10, 0.25, 0.70])
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis("off")
    ax2.add_patch(FancyBboxPatch((2, 2), 96, 96,
                                 boxstyle="round,pad=1.2,rounding_size=2.4",
                                 fc=PANEL, ec=GRID, lw=1.3))
    ax2.text(50, 90, "The chase in numbers", fontsize=12.5, fontweight="bold",
             color=TXT, ha="center")
    entries = [
        ("corridor edge", "closed formula\n(resolvent eigenvalues)", GREEN),
        ("best flow functional", "Levinson energy extremum:\nmedian error 0.14%", CYAN),
        ("outliers", "exactly on 16, 64, 81 —\nthe prime-power fingerprint", RED),
        ("new question", "“explain the selection\ninside the corridor”", AMBER),
    ]
    yy = 78
    for head, body, col in entries:
        ax2.text(50, yy, head, fontsize=10.5, fontweight="bold", color=col,
                 ha="center")
        ax2.text(50, yy - 9.5, body, fontsize=9, color=TXT, ha="center",
                 linespacing=1.35)
        yy -= 19.5

    axf = fig.add_axes([0, 0, 1, 0.06])
    axf.set_xlim(0, 100)
    axf.set_ylim(0, 100)
    axf.axis("off")
    axf.text(3.2, 50, FOOTER, fontsize=8.5, color=MUT)
    fig.savefig(os.path.join(FIGDIR, "a2_korridor.png"), dpi=170)
    plt.close(fig)


# ============================================================================
# Article 2 / Figure 6: The day's timeline
# ============================================================================
def fig_a2_timeline():
    fig, ax = new_canvas(12.8, 7.4)
    title(ax, "One day at the front: August 3, 2026",
          "From measuring to mechanism — the question transforms three times. By evening: suite at 694 modules, all green, no RH claim.")

    # Time axis
    yline = 52
    ax.plot([5, 95], [yline, yline], color=GRID, lw=2.5)
    stations = [
        ("Early morning", CYAN, True,
         ["the 11.7% pinch breaks", "(a bookkeeping artifact);", "the W2 hole closes", "(223,949 certified", "zeros) — v680/v681"]),
        ("Morning", GREEN, False,
         ["five proof offensives:", "surface theorem det S > 0;", "Gaussian code bridge;", "Ihara blueprint;", "falsifier — 2 honest deaths"]),
        ("Midday", VIOLET, True,
         ["promotion v682–v691", "(182 checks, all green);", "master contract “Uniform", "Positivity” registered"]),
        ("Afternoon", AMBER, False,
         ["T-B census: 60/70 windows;", "Z1 series: engine exists,", "runs as a test bench;", "the chase →", "corridor point 0.53"]),
        ("Evening", CYAN, True,
         ["promotion v692–v700", "(140 checks); 2 new", "Lean modules; suite:", "694 modules — no", "RH statement, anywhere"]),
    ]
    x = 10
    for name, col, above, lines in stations:
        ax.add_patch(Circle((x, yline), 1.3, fc=col, ec=BG, lw=1.5, zorder=5))
        if above:
            ty = yline + 7
            ax.plot([x, x], [yline + 1.5, ty - 1.2], color=col, lw=1.4)
            name_y = ty + 1.8 + len(lines) * 3.8 + 3.2
            ax.text(x, name_y, name, fontsize=11.5, fontweight="bold",
                    color=col, ha="center")
            yy = name_y - 5.2
            for ln in lines:
                ax.text(x, yy, ln, fontsize=8.6, color=TXT, ha="center")
                yy -= 3.8
        else:
            ty = yline - 8
            ax.plot([x, x], [yline - 1.5, ty + 2.0], color=col, lw=1.4)
            ax.text(x, ty - 1.5, name, fontsize=11.5, fontweight="bold",
                    color=col, ha="center")
            yy = ty - 6.2
            for ln in lines:
                ax.text(x, yy, ln, fontsize=8.6, color=TXT, ha="center")
                yy -= 3.8
        x += 20

    # Transformation of the question
    box(ax, 5, 6, 90, 11.5, [], fc=PANEL2, ec=GRID)
    ax.text(50, 14.2, "The transformation of the question — three times smaller in two days:",
            fontsize=10.5, fontweight="bold", color=TXT, ha="center")
    ax.text(50, 9.6, "“Prove one inequality for ALL windows”  →  “Find ONE geometric object with the right traces”  →  “Explain ONE selection principle inside an explicit corridor”",
            fontsize=9.4, color=CYAN, ha="center")

    footer(ax, y=2.2)
    fig.savefig(os.path.join(FIGDIR, "a2_timeline.png"), dpi=170)
    plt.close(fig)


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Self-test of the Lambda reconstruction (compute honestly, don't paint)
    lam = lambda_geo(64)
    for n in range(2, 65):
        pp = prime_power(n)
        want = math.log(pp[0]) if pp else 0.0
        assert abs(lam[n] - want) < 1e-9, (n, lam[n], want)

    fig_a1_compiler_kette()
    fig_a1_marken_bits_code()
    fig_a1_drei_felder()
    fig_a1_lambda_gitter()
    fig_a1_ehrlichkeit()
    fig_a2_nullstellen()
    fig_a2_detektor()
    fig_a2_fensterkarte()
    fig_a2_ihara()
    fig_a2_korridor()
    fig_a2_timeline()
    print("OK — 11 figures written to", FIGDIR)
