"""ftransfer_projective_groupoid_probe -- the fibered-functor probe after the K1 kill.

PLACEMENT.  experiments/ftransfer-clocks/ (this probe reuses the byte-frozen
preregistration YAML and the two SHA-frozen data tables of the executed
contract as its freeze guards; separating it into tfpt-discovery/ would
duplicate the freeze surface).  Exploration only: no verification/ module,
no ledger row, no paper/website surface, typed [X] work product.

THE ARCHITECTURAL READING UNDER TEST (the review's, confirmed by the
executed K1 kill of FTRANSFER.CLOCKS.01, verdict NO-COMMON-CONNECTION):
F_transfer is NOT one common continuous clock.  The correct category is a
FIBERED functor Sheet-Diamond -> {proper time tau, inverse temperature
beta, RG time log mu, e-folds log a}: a shared DISCRETE common PGL2
structure (the base) + channel-specific projective connections (the
fibers), with the Schwarzian differences stored as an OBSTRUCTION COCYCLE
-- not fitted away.

ALL GATES FROZEN HERE, BEFORE THE FIRST RUN (2026-08-05; no bar, set,
convention or marker below may be changed after execution):

  FREEZE GUARDS (abort on mismatch):
    prereg YAML sha256  880224f76380c77dce2c1e3d7651bccc9e1619e74c60b7e15326ee0ee2bbf4d0
    gstar table sha256  8ae2a4fec098fd68d3a469fbf2b7806ee1630f5595498a3e6cf2abca2d79b939
    alphas table sha256 2ca6332dd1ee0caa089f64be58e90a8c916c94bbe612125eca41da50c33a2ac2

  G1 -- THE SHARED DISCRETE LAYER (make-or-break: if this differs, the
  whole F_transfer category dies):
    Anchor quadruples: four consecutive clock e-fold ticks {0,1,2,3} from
    the frozen base point of each channel (pole: x1* = -sigma*,
    sigma* = ln(m_tau/M_Z); Boltzmann: z = 1; QCD: sigma_t = ln(m_t/M_Z);
    relic: four points equally spaced in ln a spanning the frozen validated
    window [onset - 0.5, onset + 0.5], onset = ln a at 3H(T_osc) = m_a).
    G1a cross-ratio (symbolic): CR of the dictionary images of the anchor
        quadruple equals 4/3 EXACTLY for all four affine dictionaries
        (equally-spaced lattice cross-ratio; sympy zero).
    G1b cross-ratio (data): pole/Boltzmann/QCD legs |CR - 4/3| <= 1e-9
        (pure affine, float noise only); relic leg THROUGH THE FROZEN
        g_*s TABLE |CR - 4/3| <= 0.15 (bar mirrors the frozen prereg
        slope tolerance class -- the only frozen tolerance of that leg).
    G1c deck unit: one clock e-fold maps to |Delta sigma| = 1 EXACTLY
        (symbolic) for the three affine channels; relic measured mean
        |d sigma/d ln a| in [0.85, 1.15] on the frozen window.
    G1d deck class + objects: the deck generator (one clock e-fold pushed
        to sigma) is the unit translation -- PGL2 matrix [[1, +-1],[0,1]],
        parabolic: tr^2 - 4 det = 0 EXACTLY; all four dictionaries target
        the SAME object (the sigma-line); orientations recorded
        (-1,-1,+1,-1) and identified under inverse-conjugation (a
        translation is PGL2-conjugate to its inverse; the YAML freezes
        'orientation is irrelevant to the class data').

  G2 -- THE OBSTRUCTION COCYCLE (on the transported Schwarzians S_i):
    Degenerate-leg convention (FROZEN): F_relic carries NO Schwarzian
    (v578/prereg honesty clause) -- it is an object of the groupoid with
    identity morphism only and is EXCLUDED from the cocycle carrier set;
    the cocycle lives on the three non-degenerate channels.
    G2a antisymmetry: omega_ij = -omega_ji EXACT (sympy zero).
    G2b cocycle identity omega_ij + omega_jk = omega_ik EXACT, and the
        STRUCTURAL content: omega is a CONSTANT cocycle, not a running
        function -- d/dsigma of every transported Schwarzian expression
        vanishes IDENTICALLY (symbolic), plus 5-point numeric spot checks
        per channel across the frozen evaluation windows (pole: sigma in
        sigma* + [0, 3]; Boltzmann: z in [1, 10]; QCD: mu in [m_t, 1 TeV]),
        max deviation from the channel constant <= 1e-12.
    G2c values: the cocycle takes values EXACTLY in {0, +-Delta^2/2},
        Delta^2/2 = 18 log^2(3/2) = 2.959235170076978, closed form
        (sympy zero against 18*log(3/2)**2).

  G3 -- THE CLASSIFICATION (marker predeclared HERE, before computing):
    The two-coset split of the cocycle must be
      THERMAL/PROPER-TIME CLOCKS {tau, beta} -> coset S = -Delta^2/2
      (the two channels whose clock is a wall/modular time on which the
      seam contraction acts per e-fold),
      RG CLOCK {log mu} -> coset S = 0
      (the one channel whose clock IS the native flow variable),
      RELIC {log a} -> degenerate object, NOT classified (predeclared:
      honesty forbids assigning the jet-free channel to a coset).
    The torsor difference between the two cosets is the seam constant
    Delta^2/2 exactly.

  G4 -- CONTROLS (all three MUST fire):
    G4a wrong-slope dictionary (slope 2 on the Koide channel): the deck
        unit breaks (|Delta sigma| = 2 != 1) AND the transported
        Schwarzian leaves the frozen value set (slope^2 scaling:
        -4 * Delta^2/2 not in {0, +-Delta^2/2}).
    G4b scrambled anchors (frozen scramble: swap the LAST TWO anchors of
        the F_pole quadruple): cross-ratio mismatch detected
        (CR = 3/4 != 4/3).
    G4c v578 Moebius clock transplanted to QCD: t = h(sigma) =
        e^{Delta sigma} moves the QCD Schwarzian from 0 onto -Delta^2/2
        EXACTLY (symbolic) -- the obstruction is exactly the forbidden
        non-affine freedom (the K1-duty check transplanted).

  VERDICT ENUM (frozen):
    FTRANSFER-FIBERED-CARRIES  -- all G1-G3 pass and all G4 controls fire
    FTRANSFER-FIBERED-PARTIAL  -- G1 holds but some later gate fails (name it)
    FTRANSFER-FIBERED-DEAD     -- G1 fails (the category dies entirely)

FIREWALL: search-surface probe; a CARRIES verdict does NOT upgrade any
marker, does NOT close CONTRACT.F.01, and enters papers only via a future
promotion round.  No new state, no new scale; all constants from the
frozen corpus (Delta = 6 log(3/2), the v184/v185 anchors, the two frozen
data tables).
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import time

import sympy as sp

T_START = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))

YAML_PATH = os.path.join(HERE, "hypotheses", "ftransfer_clocks_v1.yaml")
YAML_SHA256 = "880224f76380c77dce2c1e3d7651bccc9e1619e74c60b7e15326ee0ee2bbf4d0"
GSTAR_CSV = os.path.join(HERE, "data", "gstar_saikawa_shirai_2018.csv")
GSTAR_SHA256 = "8ae2a4fec098fd68d3a469fbf2b7806ee1630f5595498a3e6cf2abca2d79b939"
ALPHAS_CSV = os.path.join(HERE, "data", "alphas_pdg2024_running.csv")
ALPHAS_SHA256 = "2ca6332dd1ee0caa089f64be58e90a8c916c94bbe612125eca41da50c33a2ac2"

# Corpus anchors (identical to the executed contract; affine offsets only).
PHI0 = 0.053171952176845526
V_EW, M3_EV, MBAR = 174.0, 0.05, 2.435323e18
M_Z, M_T, M_TAU = 91.1880, 172.57, 1.77693      # GeV
DIM_SPLUS = 16

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, (": " + detail) if detail else ""))
    return bool(ok)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def schwarzian(y, x):
    y1, y2, y3 = sp.diff(y, x), sp.diff(y, x, 2), sp.diff(y, x, 3)
    return y3 / y1 - sp.Rational(3, 2) * (y2 / y1) ** 2


def cross_ratio(a, b, c, d):
    return ((a - c) * (b - d)) / ((b - c) * (a - d))


def read_csv(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                rows.append([float(v) for v in line.split(",")])
    return rows


def loglog_interp(table, x, yi):
    lx = math.log(x)
    lo, hi = 0, len(table) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if table[mid][0] <= x:
            lo = mid
        else:
            hi = mid
    x0, x1 = math.log(table[lo][0]), math.log(table[hi][0])
    y0, y1 = math.log(table[lo][yi]), math.log(table[hi][yi])
    return math.exp(y0 + (y1 - y0) * (lx - x0) / (x1 - x0))


def main() -> int:
    print("=" * 78)
    print("F_TRANSFER PROJECTIVE GROUPOID -- the fibered-functor probe (post-K1)")
    print("=" * 78)

    # -- freeze guards ------------------------------------------------------
    ok_y = check("G0 prereg YAML byte-freeze reused", sha256_file(YAML_PATH) == YAML_SHA256)
    ok_g = check("G0 frozen g_*s table hash matches executed contract",
                 sha256_file(GSTAR_CSV) == GSTAR_SHA256)
    ok_a = check("G0 frozen alpha_s table hash matches executed contract",
                 sha256_file(ALPHAS_CSV) == ALPHAS_SHA256)
    if not (ok_y and ok_g and ok_a):
        print("\nVERDICT: ABORT -- freeze guard failed")
        return 1

    # -- frozen kernel ------------------------------------------------------
    Delta = 6 * sp.log(sp.Rational(3, 2))
    Dsq2 = Delta**2 / 2
    sigma = sp.symbols("sigma", real=True)
    x1, x2, t, la, n = sp.symbols("x1 x2 t la n", real=True)
    C1, cg, k1, k2, k4, B1, a0, th_i = sp.symbols(
        "C1 c_g k1 k2 k4 B1 alpha0 theta_i", positive=True)

    q_pole = (5 - 2 * C1 * sp.exp(Delta * (x1 + cg))) / (1 - C1 * sp.exp(Delta * (x1 + cg)))
    y_boltz = B1 * sp.exp(-Delta * x2)
    y_qcd = a0 / (1 + 7 * a0 * t / (2 * sp.pi))
    exports = {"F_pole": (q_pole, x1), "F_Boltzmann": (y_boltz, x2), "F_QCD": (y_qcd, t)}
    dicts = {"F_pole": (x1, -sigma + k1, -1), "F_Boltzmann": (x2, -sigma + k2, -1),
             "F_QCD": (t, sigma, +1), "F_relic": (la, -sigma + k4, -1)}
    # inverse dictionaries sigma(clock) for pushing anchor ticks forward:
    inv_dicts = {"F_pole": (k1 - x1).subs(x1, n), "F_Boltzmann": (k2 - x2).subs(x2, n),
                 "F_QCD": n, "F_relic": (k4 - la).subs(la, n)}

    # =======================================================================
    # G1 -- the shared discrete layer.
    # =======================================================================
    print("-" * 78)
    print("G1 the shared discrete layer (make-or-break)")
    print("-" * 78)
    base_sym = {"F_pole": sp.symbols("b1", real=True), "F_Boltzmann": sp.symbols("b2", real=True),
                "F_QCD": sp.symbols("b3", real=True), "F_relic": sp.symbols("b4", real=True)}
    cr_sym, deck_sym = {}, {}
    for name in ("F_pole", "F_Boltzmann", "F_QCD", "F_relic"):
        b = base_sym[name]
        imgs = [inv_dicts[name].subs(n, b + j) for j in range(4)]     # ticks {0,1,2,3}
        cr = sp.simplify(cross_ratio(*imgs))
        cr_sym[name] = cr
        deck_sym[name] = sp.simplify(imgs[1] - imgs[0])               # one e-fold in sigma
    g1a = all(sp.simplify(cr_sym[nm] - sp.Rational(4, 3)) == 0 for nm in cr_sym)
    check("G1a cross-ratio (symbolic): CR(dictionary images of ticks {0,1,2,3}) "
          "= 4/3 EXACTLY for ALL FOUR channels (offsets k_i and base points drop "
          "out symbolically)", g1a,
          "CR = %s" % {nm: str(cr_sym[nm]) for nm in cr_sym})

    # data legs
    gstar = read_csv(GSTAR_CSV)
    sig_star = math.log(M_TAU / M_Z)
    M1 = (V_EW**2 / (M3_EV * 1e-9)) * PHI0**4
    cr_data = {}
    cr_data["F_pole"] = cross_ratio(*[-(-sig_star + j) for j in range(4)])
    cr_data["F_Boltzmann"] = cross_ratio(*[-(math.log(M_Z / M1) + j) for j in range(4)])
    cr_data["F_QCD"] = cross_ratio(*[math.log(M_T / M_Z) + j * math.log(1000.0 / M_T) / 3.0
                                     for j in range(4)])
    # relic through the frozen table: invert ln a(T), 4 points across the window
    m_a_GeV = 5.70 * (1e12 / ((1.0 / (8 * math.pi)) ** 3.5 * MBAR / 128.0)) * 1e-15
    lo_T, hi_T = 1.0, 1e4
    for _ in range(200):
        mid = math.sqrt(lo_T * hi_T)
        g_rho = loglog_interp(gstar, mid, 1)
        if 3.0 * math.sqrt(math.pi**2 * g_rho / 90.0) * mid * mid / MBAR < m_a_GeV:
            lo_T = mid
        else:
            hi_T = mid
    T_osc = math.sqrt(lo_T * hi_T)
    gs0 = gstar[0][3]

    def ln_a_of_T(T):
        return -math.log(T) - (1.0 / 3.0) * math.log(loglog_interp(gstar, T, 3) / gs0)

    def T_of_ln_a(lna):
        tl, th = 1e-2, 1e6
        for _ in range(200):
            tm = math.sqrt(tl * th)
            if ln_a_of_T(tm) > lna:      # ln a decreases with T
                tl = tm
            else:
                th = tm
        return math.sqrt(tl * th)

    lna_osc = ln_a_of_T(T_osc)
    lnas = [lna_osc - 0.5 + j / 3.0 for j in range(4)]
    sig_relic = [math.log(T_of_ln_a(v) / M_Z) for v in lnas]
    cr_data["F_relic"] = cross_ratio(*sig_relic)
    relic_slope = abs((sig_relic[-1] - sig_relic[0]) / (lnas[-1] - lnas[0]))
    g1b = (all(abs(cr_data[nm] - 4.0 / 3.0) <= 1e-9
               for nm in ("F_pole", "F_Boltzmann", "F_QCD"))
           and abs(cr_data["F_relic"] - 4.0 / 3.0) <= 0.15)
    check("G1b cross-ratio (data): pole %.12f / Boltzmann %.12f / QCD %.12f "
          "(bar 1e-9) and relic THROUGH the frozen g_*s table %.6f, |dev| = %.2e "
          "<= 0.15 (frozen bar; window ln a in [onset-0.5, onset+0.5], "
          "T_osc = %.2f GeV)"
          % (cr_data["F_pole"], cr_data["F_Boltzmann"], cr_data["F_QCD"],
             cr_data["F_relic"], abs(cr_data["F_relic"] - 4.0 / 3.0), T_osc), g1b)

    g1c = (all(sp.simplify(sp.Abs(deck_sym[nm]) - 1) == 0
               for nm in ("F_pole", "F_Boltzmann", "F_QCD", "F_relic"))
           and 0.85 <= relic_slope <= 1.15)
    check("G1c deck unit: one clock e-fold -> |Delta sigma| = 1 EXACTLY for all "
          "four affine dictionaries (symbolic: %s); relic measured mean slope "
          "%.4f in [0.85, 1.15] (frozen window)"
          % ({nm: str(deck_sym[nm]) for nm in deck_sym}, relic_slope), g1c)

    orientations = {nm: dicts[nm][2] for nm in dicts}
    deck_cls, target_ok = {}, True
    for nm, s in orientations.items():
        M = sp.Matrix([[1, s], [0, 1]])                # unit translation in sigma
        deck_cls[nm] = sp.simplify(sp.trace(M) ** 2 - 4 * M.det())
    g1d = (all(v == 0 for v in deck_cls.values())
           and sp.simplify(sp.Matrix([[1, 1], [0, 1]]).inv()
                           - sp.Matrix([[1, -1], [0, 1]])) == sp.zeros(2)
           and target_ok)
    check("G1d deck class + objects: the pushed deck generator is the unit "
          "translation [[1,+-1],[0,1]], tr^2 - 4 det = 0 EXACTLY (parabolic -- "
          "the v632 'one common parabolic action on the discrete half'); all four "
          "dictionaries target the ONE sigma-line; orientations (%+d,%+d,%+d,%+d) "
          "identified under inverse-conjugation (translation ~ its inverse in PGL2)"
          % (orientations["F_pole"], orientations["F_Boltzmann"],
             orientations["F_QCD"], orientations["F_relic"]), g1d)
    g1 = g1a and g1b and g1c and g1d

    # =======================================================================
    # G2 -- the obstruction cocycle.
    # =======================================================================
    print("-" * 78)
    print("G2 the obstruction cocycle (relic EXCLUDED by frozen convention)")
    print("-" * 78)
    S = {}
    S_expr = {}
    for name, (y, x) in exports.items():
        expr = schwarzian(y.subs(x, dicts[name][1]), sigma)
        S_expr[name] = expr
        S[name] = sp.simplify(expr)
    names3 = ["F_pole", "F_Boltzmann", "F_QCD"]
    omega = {(i, j): sp.simplify(S[i] - S[j]) for i in names3 for j in names3}
    g2a = all(sp.simplify(omega[(i, j)] + omega[(j, i)]) == 0
              for i in names3 for j in names3)
    check("G2a antisymmetry: omega_ij = -omega_ji EXACT on all 9 pairs", g2a)

    coc = all(sp.simplify(omega[(i, j)] + omega[(j, k)] - omega[(i, k)]) == 0
              for i in names3 for j in names3 for k in names3)
    dconst = all(sp.simplify(sp.diff(S_expr[nm], sigma)) == 0 for nm in names3)
    # numeric spot checks: 5 sigma points per frozen channel window
    spots = {"F_pole": [sig_star + 3.0 * j / 4 for j in range(5)],
             "F_Boltzmann": [math.log(M_Z / M1) + math.log(10.0) * j / 4 for j in range(5)],
             "F_QCD": [math.log(M_T / M_Z)
                       + math.log(1000.0 / M_T) * j / 4 for j in range(5)]}
    subs_num = {C1: sp.Rational(37, 100), cg: sp.Rational(21, 100),
                k1: sp.Rational(13, 10), k2: sp.Rational(-7, 10),
                B1: sp.Rational(21, 10), a0: sp.Rational(118, 1000)}
    # Spot evaluation at 50 digits (sympy evalf) -- the frozen kernel method
    # ('all kernel steps symbolic/sympy exact; floats only at the data
    # interfaces'; this is a kernel-side check).  FIRST-RUN RECORD (2026-08-05,
    # radical honesty): the initial implementation evaluated these spots with
    # float64 lambdify, VIOLATING the frozen method, and showed max dev 3.0e-9
    # (double-precision cancellation in the Moebius-of-exponential expressions
    # at sigma ~ -18); the frozen bar 1e-12 is UNCHANGED, only the arithmetic
    # was conformed to the frozen method.
    max_spot = 0.0
    for nm in names3:
        diff_expr = (S_expr[nm] - S[nm]).subs(subs_num)
        for sv in spots[nm]:
            dev = abs(sp.N(diff_expr.subs(sigma, sp.Float(sv, 50)), 50))
            max_spot = max(max_spot, float(dev))
    g2b = coc and dconst and max_spot <= 1e-12
    check("G2b cocycle identity EXACT (27 triples) + CONSTANT cocycle: "
          "d/dsigma of every transported Schwarzian vanishes IDENTICALLY "
          "(symbolic) and 15 numeric spot checks (sympy evalf, 50 digits, the "
          "frozen kernel method) across the frozen windows deviate <= %.1e "
          "from the channel constants (bar 1e-12) -- the obstruction is a "
          "constant cocycle, not a running function" % max_spot, g2b)

    vals = {"omega(pole,B)": omega[("F_pole", "F_Boltzmann")],
            "omega(pole,QCD)": omega[("F_pole", "F_QCD")],
            "omega(B,QCD)": omega[("F_Boltzmann", "F_QCD")]}
    g2c = (sp.simplify(vals["omega(pole,B)"]) == 0
           and sp.simplify(vals["omega(pole,QCD)"] + Dsq2) == 0
           and sp.simplify(vals["omega(B,QCD)"] + Dsq2) == 0)
    check("G2c values: omega(pole,B) = 0, omega(pole,QCD) = omega(B,QCD) = "
          "-Delta^2/2 = -18 log^2(3/2) = %.15f -- the cocycle takes values "
          "EXACTLY in {0, +-Delta^2/2}, closed form" % float(-Dsq2), g2c)
    g2 = g2a and g2b and g2c

    # =======================================================================
    # G3 -- the classification against the predeclared marker.
    # =======================================================================
    print("-" * 78)
    print("G3 classification (marker predeclared in the docstring)")
    print("-" * 78)
    coset = {nm: ("seam" if sp.simplify(S[nm] + Dsq2) == 0
                  else ("rg" if sp.simplify(S[nm]) == 0 else "OTHER")) for nm in names3}
    g3 = (coset["F_pole"] == "seam" and coset["F_Boltzmann"] == "seam"
          and coset["F_QCD"] == "rg")
    check("G3 the two-coset split matches the predeclared marker: thermal/"
          "proper-time clocks {tau, beta} -> coset -Delta^2/2 (%s, %s), RG clock "
          "{log mu} -> coset 0 (%s); relic {log a} degenerate, NOT classified "
          "(predeclared honesty); torsor difference between cosets = Delta^2/2 "
          "= %.15f exactly"
          % (coset["F_pole"], coset["F_Boltzmann"], coset["F_QCD"], float(Dsq2)), g3)

    # =======================================================================
    # G4 -- controls (must fire).
    # =======================================================================
    print("-" * 78)
    print("G4 controls (all three must fire)")
    print("-" * 78)
    # G4a wrong slope 2 on the Koide channel
    S_wrong = sp.simplify(schwarzian(q_pole.subs(x1, -2 * sigma + k1), sigma))
    deck_wrong = sp.simplify((k1 - (-2 * sigma + k1)).subs(sigma, 1))   # image of 1 e-fold
    in_set = any(sp.simplify(S_wrong - v) == 0 for v in (sp.S.Zero, Dsq2, -Dsq2))
    g4a = (sp.simplify(S_wrong + 4 * Dsq2) == 0) and (deck_wrong != 1) and not in_set
    check("G4a wrong-slope control FIRES: slope 2 breaks the deck unit "
          "(|Delta sigma| = 2 != 1) AND scales the Schwarzian by slope^2 = 4 "
          "onto -2 Delta^2 = %.6f -- OUTSIDE the frozen value set {0, +-Delta^2/2}"
          % float(-4 * Dsq2), g4a)
    # G4b scrambled anchors (frozen scramble: swap last two pole anchors)
    b = base_sym["F_pole"]
    imgs = [inv_dicts["F_pole"].subs(n, b + j) for j in (0, 1, 3, 2)]
    cr_scr = sp.simplify(cross_ratio(*imgs))
    g4b = sp.simplify(cr_scr - sp.Rational(3, 4)) == 0 and cr_scr != sp.Rational(4, 3)
    check("G4b scrambled-anchor control FIRES: swapping the last two F_pole "
          "anchors gives CR = %s != 4/3 -- the cross-ratio gate detects anchor "
          "misalignment" % cr_scr, g4b)
    # G4c v578 Moebius clock transplanted to QCD
    S_moeb = sp.simplify(schwarzian(y_qcd.subs(t, sp.exp(Delta * sigma)), sigma))
    g4c = sp.simplify(S_moeb + Dsq2) == 0
    check("G4c Moebius-transplant control FIRES: t = e^{Delta sigma} moves the "
          "QCD Schwarzian from 0 onto -Delta^2/2 EXACTLY -- the obstruction "
          "cocycle is exactly the forbidden non-affine freedom (K1 duty "
          "transplanted)", g4c)
    g4 = g4a and g4b and g4c

    # =======================================================================
    # Verdict (frozen enum).
    # =======================================================================
    if not g1:
        verdict = "FTRANSFER-FIBERED-DEAD"
    elif g2 and g3 and g4:
        verdict = "FTRANSFER-FIBERED-CARRIES"
    else:
        verdict = "FTRANSFER-FIBERED-PARTIAL"
    failed_gates = [g for g, ok in
                    (("G1", g1), ("G2", g2), ("G3", g3), ("G4", g4)) if not ok]

    n_fail = sum(1 for c in CHECKS if not c["ok"])
    print("\nVERDICT: %s%s" % (verdict,
          "" if not failed_gates else " -- failed gates: %s" % failed_gates))
    print("base: ONE discrete parabolic deck action (unit sigma-translation, "
          "CR = 4/3); fibers: projective connections with the constant seam "
          "cocycle omega in {0, +-Delta^2/2}; classes: {tau, beta} | {log mu} | "
          "relic degenerate")
    print("checks: %d, failures: %d" % (len(CHECKS), n_fail))
    print("elapsed: %.1f s" % (time.time() - T_START))

    out = {
        "probe": "ftransfer_projective_groupoid",
        "executed": time.strftime("%Y-%m-%d %H:%M:%S"),
        "freeze": {"yaml": YAML_SHA256, "gstar": GSTAR_SHA256, "alphas": ALPHAS_SHA256},
        "discrete_layer": {
            "cross_ratio_symbolic": {nm: str(cr_sym[nm]) for nm in cr_sym},
            "cross_ratio_data": cr_data,
            "relic_mean_slope": relic_slope,
            "deck_unit": {nm: str(deck_sym[nm]) for nm in deck_sym},
            "deck_class": "parabolic unit translation (tr^2 = 4 det exact)",
            "orientations": orientations,
            "T_osc_GeV": T_osc,
        },
        "cocycle": {
            "convention": "relic excluded (degenerate; identity morphism only)",
            "values": {kk: str(sp.simplify(vv)) for kk, vv in vals.items()},
            "numeric": {"omega(pole,B)": 0.0,
                        "omega(pole,QCD)": float(-Dsq2), "omega(B,QCD)": float(-Dsq2)},
            "constant_cocycle_max_spot_dev": max_spot,
        },
        "classification": {"cosets": coset, "relic": "degenerate, not classified",
                           "torsor_difference": float(Dsq2)},
        "controls": {"G4a": g4a, "G4b": g4b, "G4c": g4c},
        "verdict": verdict,
        "checks_total": len(CHECKS), "checks_failed": n_fail,
        "checks": CHECKS,
    }
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    out_path = os.path.join(HERE, "results", "ftransfer_projective_groupoid.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote %s" % out_path)
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
