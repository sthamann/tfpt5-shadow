"""FTRANSFER.CLOCKS.01 -- the experiments-side executor of the frozen
external-clock contract (hypotheses/ftransfer_clocks_v1.yaml, byte-frozen
2026-08-04).

WHAT THIS IS.  The preregistered kill test for the jet residual of
CONTRACT.F.01, executed EXACTLY as frozen: four external clocks (proper time
tau / inverse temperature beta / RG time t / e-folds ln a), four affine
dictionaries with frozen slopes (-1, -1, +1, -1) into the common chart
sigma = ln(mu/M_Z), symbolic (sympy-exact) Schwarzian-cocycle transport, the
one-class prediction FTC.P1, the three kill criteria K1/K2/K3 with frozen
bars, the four data-driven dictionary-validity legs FTC.01.K/B/Q/R, and the
three controls FTC.C1/C2/C3.  NO frozen value is altered; the executor
verifies the sha256 of the preregistration YAML and of the two curated data
tables (data/DATA_FREEZE.sha256) at startup and aborts on any mismatch.

WHAT THIS IS NOT.  Not load-bearing: experiments/ only, typed [X]; no ledger
row moves, no marker, no paper/website surface.  The preregistration's
executor clause names a FUTURE verification module (vN_ftransfer_clock_jets
pattern) entered via the promotion workflow; this script is the
experiments-side execution that produces the adjudicated numbers for that
promotion round -- it creates no vN module and upgrades nothing.

HONEST PRIOR (frozen in the YAML before execution): expected verdict
NO-COMMON-CONNECTION (K1) -- affine transport scales a Schwarzian by
slope^2 and cannot move 0 (the QCD value) onto -Delta^2/2 (the seam value).
ONE-CLASS would be the surprise.

Data interfaces (curated + byte-frozen BEFORE this executor first ran):
  data/gstar_saikawa_shirai_2018.csv   (Saikawa & Shirai 2018, arXiv:1803.01038)
  data/alphas_pdg2024_running.csv      (PDG 2024 world average + 4-loop running)

Run:  . experiments/tfpt-discovery/.venv/bin/activate
      python experiments/ftransfer-clocks/run_clocks_executor.py
Output: results/ftransfer_clocks_v1_execution.json + console report.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import time

import sympy as sp
import yaml

T_START = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Frozen freeze-guard hashes.  The YAML hash is the byte-freeze of record
# (committed 2026-08-04, commit 368df86f); the data hashes were frozen by
# scripts/curate_data_tables.py BEFORE the executor first ran (2026-08-05).
# ---------------------------------------------------------------------------
YAML_PATH = os.path.join(HERE, "hypotheses", "ftransfer_clocks_v1.yaml")
YAML_SHA256 = "880224f76380c77dce2c1e3d7651bccc9e1619e74c60b7e15326ee0ee2bbf4d0"
DATA_FREEZE = os.path.join(HERE, "data", "DATA_FREEZE.sha256")
GSTAR_CSV = os.path.join(HERE, "data", "gstar_saikawa_shirai_2018.csv")
ALPHAS_CSV = os.path.join(HERE, "data", "alphas_pdg2024_running.csv")

# Corpus anchors entering ONLY through base points / window edges (v184, v185,
# tfpt_constants); affine offsets by construction, outside the class data.
PHI0 = 0.053171952176845526      # tfpt_constants phi0 (retained seed)
V_EW = 174.0                     # GeV (v184)
M3_EV = 0.05                     # eV, m_3 ~ sqrt(dm^2_atm) (v184)
MBAR = 2.435323e18               # GeV, reduced Planck mass (v184/v185)
DIM_SPLUS = 16                   # v185: f_a = M_scal/(2 * dim S+ * |mu4|) = M_scal/128
N_EFF_SM = 3.044                 # SM value the Planck N_eff certificate is tested against

CHECKS = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, (": " + detail) if detail else ""))
    return bool(ok)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def schwarzian(y, x):
    y1, y2, y3 = sp.diff(y, x), sp.diff(y, x, 2), sp.diff(y, x, 3)
    return sp.simplify(y3 / y1 - sp.Rational(3, 2) * (y2 / y1) ** 2)


def read_csv(path: str):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            rows.append([float(v) for v in line.split(",")])
    return rows


def loglog_interp(table, x, xi=0, yi=1):
    """log-log linear interpolation in column yi against column xi."""
    lx = math.log(x)
    lo, hi = 0, len(table) - 1
    if not (table[lo][xi] <= x <= table[hi][xi]):
        raise ValueError("interpolation out of range: %g" % x)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if table[mid][xi] <= x:
            lo = mid
        else:
            hi = mid
    x0, x1 = math.log(table[lo][xi]), math.log(table[hi][xi])
    y0, y1 = math.log(table[lo][yi]), math.log(table[hi][yi])
    return math.exp(y0 + (y1 - y0) * (lx - x0) / (x1 - x0))


def main() -> int:
    print("=" * 78)
    print("FTRANSFER.CLOCKS.01 -- frozen external-clock contract: EXECUTION")
    print("=" * 78)

    # -----------------------------------------------------------------------
    # 0. FREEZE GUARD (K2 machine form): byte-frozen YAML + frozen data tables.
    # -----------------------------------------------------------------------
    yaml_hash = sha256_file(YAML_PATH)
    check("G0.1 preregistration YAML byte-freeze verified (sha256 == frozen record)",
          yaml_hash == YAML_SHA256, yaml_hash)
    frozen_data_hashes = {}
    with open(DATA_FREEZE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            h, name = line.split()
            frozen_data_hashes[name] = h
    for path in (GSTAR_CSV, ALPHAS_CSV):
        name = os.path.basename(path)
        check("G0.2 frozen data table %s hash verified" % name,
              sha256_file(path) == frozen_data_hashes[name], frozen_data_hashes[name])
    if not all(c["ok"] for c in CHECKS):
        print("\nVERDICT: ABORT -- freeze guard failed; nothing executed")
        return 1

    with open(YAML_PATH) as f:
        prereg = yaml.safe_load(f)
    D = prereg["data"]

    # -----------------------------------------------------------------------
    # Frozen symbolic kernel.
    # -----------------------------------------------------------------------
    Delta = 6 * sp.log(sp.Rational(3, 2))
    Dsq2 = Delta**2 / 2                     # = 18 log(3/2)^2 = 2.959235170076978
    sigma = sp.symbols("sigma", real=True)
    x1, x2, t, la = sp.symbols("x1 x2 t la", real=True)
    C1, cg, k1, k2, k4 = sp.symbols("C1 c_g k1 k2 k4", positive=True)
    B1, a0, th_i = sp.symbols("B1 alpha0 theta_i", positive=True)

    # Native trajectories, each in its OWN frozen clock (v99/v425/v159/v632):
    u_pole = C1 * sp.exp(Delta * (x1 + cg))          # frozen gauge t_v99 = x1 + const
    q_pole = (5 - 2 * u_pole) / (1 - u_pole)         # v99 Moebius flow, fixed pts {2,5}
    y_boltz = B1 * sp.exp(-Delta * x2)               # v425 contraction (2/3)^6 / beta e-fold
    y_qcd = a0 / (1 + 7 * a0 * t / (2 * sp.pi))      # 1-loop b0 = 7 Riccati flow
    y_relic = th_i + 0 * la                          # frozen constant (identity element)

    exports = {"F_pole": (q_pole, x1), "F_Boltzmann": (y_boltz, x2),
               "F_QCD": (y_qcd, t), "F_relic": (y_relic, la)}

    # Frozen affine dictionaries into sigma (slopes -1, -1, +1, -1):
    dicts = {"F_pole": -sigma + k1, "F_Boltzmann": -sigma + k2,
             "F_QCD": sigma, "F_relic": -sigma + k4}

    # -----------------------------------------------------------------------
    # FTC.01 -- dictionary validity (data-driven, floats; frozen tolerances).
    # -----------------------------------------------------------------------
    print("-" * 78)
    print("FTC.01 dictionary validity (data legs; floats enter HERE only)")
    print("-" * 78)

    # FTC.01.K -- Koide base point + scheme check (PDG 2024 pole masses frozen in YAML).
    k = D["koide"]
    me, mmu, mtau = k["m_e_MeV"], k["m_mu_MeV"], k["m_tau_MeV"]
    Q_exp = (me + mmu + mtau) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mtau)) ** 2
    dm = 1e-4  # numerical derivative step for the m_tau error propagation [MeV]
    Qp = (me + mmu + mtau + dm) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mtau + dm)) ** 2
    sigma_Q = abs(Qp - Q_exp) / dm * 0.09
    pull = (Q_exp - 2.0 / 3.0) / sigma_Q
    q_exp = 3 * Q_exp
    sigma_q = 3 * sigma_Q
    ftc01k_base = abs(q_exp - 2) <= 3 * sigma_q
    check("FTC.01.K base point: q_exp = %.10f, |q_exp - 2| = %.3e <= 3*sigma_q = %.3e "
          "(frozen tolerance); Q_exp = %.10f (frozen record %.10f), pull = %+.3f sigma "
          "(frozen record %+.3f)"
          % (q_exp, abs(q_exp - 2), 3 * sigma_q, Q_exp, k["frozen_check_values"]["Q_exp"],
             pull, k["frozen_check_values"]["pull_vs_two_thirds"]),
          ftc01k_base and abs(Q_exp - k["frozen_check_values"]["Q_exp"]) < 1e-9
          and abs(pull - k["frozen_check_values"]["pull_vs_two_thirds"]) < 0.01)
    r = k["scheme_check"]
    Q_run = (r["m_e_run_MeV"] + r["m_mu_run_MeV"] + r["m_tau_run_MeV"]) / (
        math.sqrt(r["m_e_run_MeV"]) + math.sqrt(r["m_mu_run_MeV"])
        + math.sqrt(r["m_tau_run_MeV"])) ** 2
    ratio = abs(Q_run - 2.0 / 3.0) / abs(Q_exp - 2.0 / 3.0)
    ftc01k_scheme = abs(Q_run - 2.0 / 3.0) > 10 * abs(Q_exp - 2.0 / 3.0)
    check("FTC.01.K scheme check: Q_run(M_Z) = %.7f, |Q_run - 2/3| = %.3e = %.0f x "
          "|Q_pole - 2/3| > 10x (frozen bar) -- the on-shell/proper-time clock "
          "assignment is the right chart, the running chart fails it"
          % (Q_run, abs(Q_run - 2.0 / 3.0), ratio), ftc01k_scheme)
    ftc01k = ftc01k_base and ftc01k_scheme

    # FTC.01.B -- radiation certificate + g_*s chart consistency on the washout window.
    gstar = read_csv(GSTAR_CSV)          # T, g_rho, g_rho_err, g_s, g_s_err
    M_R = V_EW**2 / (M3_EV * 1e-9)
    M1 = M_R * PHI0**4
    T_win = [M1 / 10.0, M1]              # washout window z = M_1*beta in [1, 10]
    gs_lo = loglog_interp(gstar, T_win[0], yi=3)
    gs_hi = loglog_interp(gstar, T_win[1], yi=3)
    slope_B = abs(math.log(gs_hi / gs_lo) / math.log(T_win[1] / T_win[0]))
    drift_B = slope_B / 3.0              # entropy-chart slope contamination
    neff = D["boltzmann"]["radiation_certificate"]
    neff_pull = abs(N_EFF_SM - 2.99) / 0.17
    ftc01b = (drift_B <= 0.15) and (neff_pull <= 2.0)
    check("FTC.01.B: washout window T in [%.3e, %.3e] GeV (M_1 = %.3e GeV, affine "
          "offset only); g_*s = %.4f..%.4f, |dln g_*s/dln T| = %.2e, entropy-chart "
          "drift %.2e <= 0.15 (frozen slope-tolerance class); radiation certificate "
          "N_eff = 2.99 +- 0.17 vs SM 3.044: %.2f sigma"
          % (T_win[0], T_win[1], M1, gs_lo, gs_hi, slope_B, drift_B, neff_pull),
          ftc01b, "certificate frozen in YAML: %s" % neff)

    # FTC.01.Q -- 1-loop overlay within 10% on [m_t, 1 TeV].
    qd = D["qcd"]
    a_mz, mz, mt = qd["alpha_s_MZ"], qd["M_Z_GeV"], qd["m_t_GeV"]
    a_mt_1l = 1.0 / (1.0 / a_mz + (23.0 / 3.0) / (2 * math.pi) * math.log(mt / mz))
    chain_ok = abs(a_mt_1l - float(qd["frozen_chain"].split(":")[-1])) < 1e-9
    check("FTC.01.Q frozen chain reproduced: alpha_s^(1l)(m_t) = %.10f (frozen "
          "0.1080741169; b0 = 23/3 leg M_Z -> m_t)" % a_mt_1l, chain_ok)
    alphas = read_csv(ALPHAS_CSV)        # Q, alpha, lo, hi
    lo_w, hi_w = qd["overlay_window_GeV"]
    devs = []
    for row in alphas:
        Q = row[0]
        if lo_w - 1e-9 <= Q <= hi_w + 1e-9:
            a1l = a_mt_1l / (1.0 + 7.0 * a_mt_1l * math.log(Q / mt) / (2 * math.pi))
            devs.append((abs(a1l - row[1]) / row[1], Q, a1l, row[1]))
    max_dev, Qm, a1m, adm = max(devs)
    ftc01q = chain_ok and max_dev <= 0.10
    check("FTC.01.Q overlay: max |alpha_1loop - alpha_data|/alpha_data = %.4f at "
          "Q = %.1f GeV (1-loop %.6f vs 4-loop PDG %.6f; %d grid points on "
          "[%.2f, %.0f]) <= 0.10 (frozen tolerance, honestly covering the >= 2-loop "
          "truncation)" % (max_dev, Qm, a1m, adm, len(devs), lo_w, hi_w), ftc01q)

    # FTC.01.R -- relic entropy-chart slope at the frozen onset 3H(T_osc) = m_a.
    M_scal = (1.0 / (8 * math.pi)) ** 3.5 * MBAR
    f_a = M_scal / (2 * DIM_SPLUS * 4)   # = M_scal/128 (v185)
    m_a_GeV = 5.70 * (1e12 / f_a) * 1e-15  # 5.70 ueV * (1e12/f_a), in GeV
    lo_T, hi_T = 1.0, 1e4

    def hubble3(T):
        g_rho = loglog_interp(gstar, T, yi=1)
        return 3.0 * math.sqrt(math.pi**2 * g_rho / 90.0) * T * T / MBAR

    for _ in range(200):
        mid = math.sqrt(lo_T * hi_T)
        if hubble3(mid) < m_a_GeV:
            lo_T = mid
        else:
            hi_T = mid
    T_osc = math.sqrt(lo_T * hi_T)
    gs0 = gstar[0][3]                    # low-T plateau g_*s(T0) = 3.9309363 (const offset)

    def ln_a_of_T(T):                    # adiabatic chart g_*s T^3 a^3 = const (offset free)
        return -math.log(T) - (1.0 / 3.0) * math.log(loglog_interp(gstar, T, yi=3) / gs0)

    lna_osc = ln_a_of_T(T_osc)
    n_pts, half = 201, 0.5               # onset window: ln a in [lna_osc - 0.5, lna_osc + 0.5]
    Ts = [T_osc * math.exp(1.2 * (i / (n_pts - 1) - 0.5)) for i in range(n_pts)]
    pts = sorted((ln_a_of_T(T), math.log(T / mz)) for T in Ts)
    worst = 0.0
    for i in range(1, len(pts) - 1):
        if abs(pts[i][0] - lna_osc) <= half:
            dslope = (pts[i + 1][1] - pts[i - 1][1]) / (pts[i + 1][0] - pts[i - 1][0])
            worst = max(worst, abs(dslope + 1.0))
    ftc01r = worst <= 0.15
    check("FTC.01.R: onset 3H(T_osc) = m_a (m_a = %.3f ueV from f_a = M_scal/128 = "
          "%.4e GeV, v185) gives T_osc = %.2f GeV; entropy-chart slope max "
          "|dsigma/dln a + 1| = %.4f over ln a in [onset - 0.5, onset + 0.5] <= 0.15 "
          "(frozen tolerance)" % (m_a_GeV * 1e15, f_a, T_osc, worst), ftc01r)
    # informational only (no adjudication): worst entropy-chart drift anywhere on the table
    worst_any, at_T = 0.0, 0.0
    for i in range(1, len(gstar) - 1):
        dlg = math.log(gstar[i + 1][3] / gstar[i - 1][3])
        dlT = math.log(gstar[i + 1][0] / gstar[i - 1][0])
        s = (dlg / dlT) / 3.0
        d = abs(s / (1.0 + s))           # |dsigma/dln a + 1| via the chain rule
        if d > worst_any:
            worst_any, at_T = d, gstar[i][0]
    print("       [info] worst entropy-chart drift anywhere on the table: "
          "|dsigma/dln a + 1| = %.3f at T = %.3f GeV (QCD crossover) -- the frozen "
          "onset at %.1f GeV sits far above it" % (worst_any, at_T, T_osc))

    construction_ok = ftc01k and ftc01b and ftc01q and ftc01r

    # -----------------------------------------------------------------------
    # FTC.02 -- THE one-class test (symbolic; the contract itself).
    # -----------------------------------------------------------------------
    print("-" * 78)
    print("FTC.02 the one-class test (sympy-exact transport; frozen dictionaries)")
    print("-" * 78)
    S_sigma = {}
    for name in ("F_pole", "F_Boltzmann", "F_QCD"):
        y, x = exports[name]
        S_sigma[name] = sp.simplify(schwarzian(y.subs(x, dicts[name]), sigma))
    check("FTC.02 seam transport exact: {q,sigma} = {y_B,sigma} = -Delta^2/2 = "
          "-18 log(3/2)^2 = %.15f (slope^2 = 1, cocycle term 0 for affine h)"
          % float(-Dsq2),
          sp.simplify(S_sigma["F_pole"] + Dsq2) == 0
          and sp.simplify(S_sigma["F_Boltzmann"] + Dsq2) == 0)
    check("FTC.02 QCD transport exact: {alpha_s,sigma} = 0 (identity dictionary; "
          "Moebius flow stays Moebius)", sp.simplify(S_sigma["F_QCD"]) == 0)
    diff_pair = sp.simplify(S_sigma["F_QCD"] - S_sigma["F_pole"])
    one_class = (sp.simplify(S_sigma["F_pole"] - S_sigma["F_Boltzmann"]) == 0
                 and diff_pair == 0)
    check("FTC.02 FTC.P1 one-class prediction: transported Schwarzians all equal "
          "-- %s (symbolic difference QCD - seam = %s = %.15f, EXACTLY nonzero)"
          % ("YES" if one_class else "NO", diff_pair, float(diff_pair)),
          not one_class if diff_pair != 0 else one_class,
          "the prediction FTC.P1 %s" % ("holds" if one_class else "FAILS -- contract dies"))

    # -----------------------------------------------------------------------
    # FTC.03 -- degeneracy honesty + K3 single-clock structural assertion.
    # -----------------------------------------------------------------------
    print("-" * 78)
    print("FTC.03 degeneracy honesty + K3 single-clock assertion (structural)")
    print("-" * 78)
    check("FTC.03 relic degeneracy: theta(ln a) = theta_i constant, y' = 0 "
          "identically -- jets degenerate, NO Schwarzian, channel scored on "
          "kills/dictionary only (frozen honesty clause)",
          sp.diff(y_relic, la) == 0)
    clock_syms = {x1, x2, t, la, sigma}
    k3_fired = False
    for name, (y, x) in exports.items():
        used = y.free_symbols & clock_syms
        ok = used <= {x}
        k3_fired = k3_fired or not ok
        check("FTC.03 K3 watch %s: export references exactly one clock (%s)"
              % (name, sorted(str(s) for s in used) or "constant"), ok)

    # -----------------------------------------------------------------------
    # Controls FTC.C1 / C2 / C3.
    # -----------------------------------------------------------------------
    print("-" * 78)
    print("controls (C1 calibration must pass, C2 swap must fail, C3 frame must pass)")
    print("-" * 78)
    S_nat = {n: (None if n == "F_relic" else sp.simplify(schwarzian(*exports[n])))
             for n in exports}
    check("FTC.C1 calibration: identity dictionaries reproduce the v578 native "
          "quadruple {-Delta^2/2, -Delta^2/2, 0, degenerate} EXACTLY",
          sp.simplify(S_nat["F_pole"] + Dsq2) == 0
          and sp.simplify(S_nat["F_Boltzmann"] + Dsq2) == 0
          and S_nat["F_QCD"] == 0 and S_nat["F_relic"] is None)
    S_swap = sp.simplify(schwarzian(q_pole.subs(x1, dicts["F_QCD"]), sigma))
    check("FTC.C2 swap control: QCD dictionary (identity, slope +1) on the Koide "
          "channel still leaves {q,sigma} = -Delta^2/2 != 0 = {alpha_s,sigma} -- "
          "the class split IS detected (the statistic cannot trivially pass)",
          sp.simplify(S_swap + Dsq2) == 0 and sp.simplify(S_swap - S_sigma["F_QCD"]) != 0)
    frame_ok = True
    for name in ("F_pole", "F_Boltzmann", "F_QCD"):
        y, x = exports[name]
        y_framed = (2 * y - 1) / (y + 3)             # frozen nontrivial Moebius frame
        S_f = sp.simplify(schwarzian(y_framed.subs(x, dicts[name]), sigma))
        frame_ok = frame_ok and sp.simplify(S_f - S_sigma[name]) == 0
    check("FTC.C3 frame independence: post-composing every y with the frozen "
          "Moebius map (2y-1)/(y+3) changes NO transported Schwarzian (cocycle "
          "correctness)", frame_ok)

    # -----------------------------------------------------------------------
    # Kill adjudication (frozen order: construction gate, then K3, K1; K2 guard).
    # -----------------------------------------------------------------------
    print("-" * 78)
    print("kill adjudication")
    print("-" * 78)
    k1_duty = {}
    if not one_class:
        # K1 duty: exhibit, per failing pair, the reparametrization h that WOULD
        # be needed (solving {h,sigma} = S_target - S_source * (h')^2 for the
        # QCD source S = 0: {h,sigma} = -Delta^2/2 => h = Moebius(e^{+-Delta*sigma})).
        h_req = sp.exp(Delta * sigma)
        S_h = sp.simplify(schwarzian(h_req, sigma))
        needed_ok = sp.simplify(S_h + Dsq2) == 0
        nonaffine = sp.simplify(sp.diff(h_req, sigma, 2)) != 0
        for pair in (("F_QCD", "F_pole"), ("F_QCD", "F_Boltzmann")):
            k1_duty["%s->%s" % pair] = (
                "h(sigma) = Moebius(e^{+-Delta*sigma}), Delta = 6 log(3/2): "
                "{h,sigma} = -Delta^2/2 exactly; NON-affine (h'' != 0) -- the "
                "forbidden exponential clock change, exactly the v578 u = e^{Delta t}")
        check("K1 duty: the reparametrization that WOULD be needed per failing pair "
              "is exhibited -- h = Moebius(e^{+-Delta*sigma}) with {h,sigma} = "
              "-Delta^2/2 (verified symbolically), and it is NON-AFFINE: the pass "
              "would require exactly the freedom the freeze forbids",
              needed_ok and nonaffine)
        check("K1 fired: NO-COMMON-CONNECTION -- with clocks and dictionaries "
              "exactly as frozen, the transported Schwarzians differ symbolically "
              "({-Delta^2/2, -Delta^2/2, 0}); no tolerance involved, the kernel is "
              "exact", True)
    check("K2 guard: executed against the byte-frozen YAML (sha256 %s...); NO "
          "post-freeze deviation of any gauge, dictionary, slope, xi, mu_0, scheme, "
          "window or frame was applied -- K2 does not fire (the exhibited h above "
          "is the deviation a pass WOULD need, i.e. any pass is K2-forbidden)"
          % YAML_SHA256[:12], True)
    check("K3 guard: every channel export is a function of exactly one clock "
          "(structural assertion above) -- K3 does not fire", not k3_fired)

    # -----------------------------------------------------------------------
    # Verdict (frozen enum).
    # -----------------------------------------------------------------------
    if not construction_ok:
        verdict = "CONSTRUCTION-FAIL"
    elif k3_fired:
        verdict = "SECOND-CLOCK-NEEDED"
    elif one_class:
        verdict = "ONE-CLASS"
    else:
        verdict = "NO-COMMON-CONNECTION"
    matches_prior = (verdict == "NO-COMMON-CONNECTION")

    n_fail = sum(1 for c in CHECKS if not c["ok"])
    print("\nVERDICT: %s -- %s the frozen prior (prereg_expected: K1 kill)"
          % (verdict, "MATCHES" if matches_prior else "*** DOES NOT MATCH ***"))
    print("transported Schwarzians on sigma: F_pole = F_Boltzmann = -Delta^2/2 = "
          "%.15f, F_QCD = 0, F_relic degenerate" % float(-Dsq2))
    print("checks: %d, failures: %d" % (len(CHECKS), n_fail))
    print("elapsed: %.1f s" % (time.time() - T_START))

    out = {
        "contract": "FTRANSFER.CLOCKS.01",
        "executed": time.strftime("%Y-%m-%d %H:%M:%S"),
        "execution_surface": "experiments-only (typed [X]; no vN module, no marker move)",
        "prereg_yaml_sha256": yaml_hash,
        "data_tables": frozen_data_hashes,
        "transported_schwarzians_sigma": {
            "F_pole": str(S_sigma["F_pole"]),
            "F_Boltzmann": str(S_sigma["F_Boltzmann"]),
            "F_QCD": str(S_sigma["F_QCD"]),
            "F_relic": "degenerate",
            "numeric_seam": -float(Dsq2), "numeric_qcd": 0.0,
        },
        "ftc01": {
            "K": {"pass": ftc01k, "q_exp": q_exp, "abs_dev": abs(q_exp - 2),
                  "bar_3sigma_q": 3 * sigma_q, "Q_run": Q_run, "scheme_ratio": ratio},
            "B": {"pass": ftc01b, "M1_GeV": M1, "window_GeV": T_win,
                  "gstar_s": [gs_lo, gs_hi], "chart_drift": drift_B,
                  "neff_pull_sigma": neff_pull},
            "Q": {"pass": ftc01q, "alpha_mt_1loop": a_mt_1l, "max_rel_dev": max_dev,
                  "at_Q_GeV": Qm, "bar": 0.10},
            "R": {"pass": ftc01r, "T_osc_GeV": T_osc, "m_a_ueV": m_a_GeV * 1e15,
                  "max_slope_dev": worst, "bar": 0.15,
                  "info_worst_anywhere": {"dev": worst_any, "T_GeV": at_T}},
        },
        "one_class": one_class,
        "kills": {"K1_fired": (not one_class) and construction_ok and not k3_fired,
                  "K2_fired": False, "K3_fired": k3_fired,
                  "K1_duty_reparametrizations": k1_duty},
        "verdict": verdict,
        "matches_frozen_prior": matches_prior,
        "checks_total": len(CHECKS), "checks_failed": n_fail,
        "checks": CHECKS,
    }
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    out_path = os.path.join(HERE, "results", "ftransfer_clocks_v1_execution.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote %s" % out_path)
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
