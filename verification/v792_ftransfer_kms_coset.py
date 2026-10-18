#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v792 -- FTRANSFER.KMSCOSET.01: the coset assignment of the fibered clock functor is a THEOREM from KMS/modular typing (18/18 checks incl. the three must-fire controls, ~3 s; discovery probe ftransfer_kms_coset_probe.py, 2026-08-05, verdict KMS-COSET-THEOREM; frozen before the first run).  THE THEOREM: S_transported = -(ln lambda)^2/2 with lambda the PGL2 multiplier of the flow's time-1 holonomy per clock e-fold -- the coset is COMPUTED from the typing datum lambda, never case-inspected.  THE CLASSIFIER uses NO Schwarzian and NO derivative of any order (non-circularity gate on its own source): (i) the holonomy grounded as an exact functional identity y(x+1) = T(y(x)), (ii) the PGL2 class of T (scalar -> degenerate; parabolic -> autonomous, lambda = 1; else hyperbolic candidate), (iii) the detailed-balance multiplier cross-ratio m(x) -- the discrete KMS signature -- exactly constant -> modular with lambda = m.  DERIVATION CHAIN sympy-exact: Lemma A {M(e^{ax}), x} = -a^2/2 identically for GENERIC Moebius M; Lemma B {M(x), x} = 0; Lemma C -a^2/2 = -Delta^2/2 iff a = +-Delta, affine dictionaries change nothing.  BLIND PROTOCOL: the four deployed clock charts classify F_pole/F_Boltzmann MODULAR with |ln lambda| = Delta = 6 log(3/2) exactly, F_QCD AUTONOMOUS (parabolic), F_relic DEGENERATE; unblinding: predicted cosets == transported Schwarzians EXACTLY (sympy zero) -- the fiber classification of the executed contract (v777, FTRANSFER-FIBERED-CARRIES) is now DERIVED.  CONTROLS: C1 fake-KMS witness caught (functional identity fails AND the ratio is non-constant); C2 affine reparametrization x -> -x + c leaves typing and |ln lambda| unchanged; C3 the v578 Moebius clock t = e^{Delta sigma} flips the QCD chart to modular and the theorem PREDICTS -Delta^2/2, confirmed by the transported Schwarzian -- the K1-duty transplant as the positive case.  Completes the three-probe chain executor -> fibered groupoid -> coset theorem: the CONTRACT.F.01 fibered refinement's clock-fiber classification is a derived statement.  Freeze guards: prereg YAML + both data tables byte-identical.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe ftransfer_kms_coset_probe.py (2026-08-05, 18 checks 0 failures, KMS-COSET-THEOREM); re-run identically at promotion (2026-08-06).  Promoted verbatim; transforms per the v777 precedent: the YAML/data freeze paths point read-only at experiments/ftransfer-clocks/ (abort-on-mismatch unchanged), the results-JSON write is DROPPED (the experiments-side probe remains the writer of record; its json import dropped with the write block), a module-level _LAST verdict capture is inserted at the single verdict assignment (v791 precedent), and run() encodes the frozen pattern (v757 precedent).  Numbers unchanged.

Original ftransfer_kms_coset_probe.py docstring (verbatim):
ftransfer_kms_coset_probe -- the coset assignment from KMS/modular typing.

PLACEMENT.  experiments/ftransfer-clocks/ (inherits the byte-frozen prereg
YAML and the two SHA-frozen data tables of the executed contract as freeze
guards).  Exploration only: no verification/ module, no ledger row, no
paper/website surface, typed [X] work product.

THE PROOF-GRADE STEP UNDER TEST (named by the executed fibered-groupoid
probe, verdict FTRANSFER-FIBERED-CARRIES): derive the coset assignment
  modular/thermal clocks {tau, beta} -> Schwarzian coset -Delta^2/2
  autonomous RG clock {log mu}      -> coset 0
from the clock's KMS/modular TYPING instead of case inspection.

THE THEOREM CANDIDATE (FROZEN in full before the first run, 2026-08-05; no
criterion, bar, control or verdict rule below may change after execution):

  A clock chart carries the seam Schwarzian -Delta^2/2 iff it is
  MODULAR/KMS-typed; an autonomous flow chart carries 0.  Unified form:
      S_transported = -(ln lambda)^2 / 2,
  where lambda is the PGL2 multiplier of the flow's time-1 holonomy per
  clock e-fold (hyperbolic: lambda != 1; parabolic/autonomous: lambda = 1;
  identity: no holonomy, unclassifiable).  With the frozen gauges (one
  clock e-fold = one seam unit, multiplier (2/3)^6 = e^{-Delta}, v99/v425)
  this gives -Delta^2/2 for the modular clocks and 0 for the RG clock --
  NO case inspection: the coset is COMPUTED from the typing datum lambda.

  THE OPERATIONAL TYPING CRITERION (frozen; must not reference the
  Schwarzian value).  For a flow y(x) in clock chart x, the classifier
  checks, in this order and using NO derivatives of any order:
    (i)  HOLONOMY: a candidate time-1 Moebius map T with
         y(x+1) = T(y(x)) verified as an exact functional identity in x
         (this grounds T in the flow; failure = witness-failed);
    (ii) CLASS: T scalar (proportional to identity) -> DEGENERATE /
         unclassifiable;  tr(T)^2 - 4 det(T) = 0 -> PARABOLIC ->
         AUTONOMOUS typing (lambda = 1);  tr(T)^2/det(T) - 4 > 0 ->
         hyperbolic candidate;
    (iii) KMS/DETAILED-BALANCE WITNESS (the discrete KMS signature): with
         p, p' the two fixed points of T, the multiplier cross-ratio
           m(x) = [(y(x+1)-p)(y(x)-p')] / [(y(x+1)-p')(y(x)-p)]
         must be EXACTLY constant in x and in the trajectory constants --
         the state-independent Boltzmann-type ratio per clock tick.
         Constant -> MODULAR/KMS typing with multiplier lambda = m;
         non-constant -> witness-failed (fake KMS caught).
  Physical reading (frozen as prose, interpretation layer only): tau is
  modular via the thermal-time/Unruh reading, beta IS the KMS parameter;
  log mu generates an autonomous gradient/beta-function flow with no KMS
  state; the machine criterion is the detailed-balance signature above.

  THE DERIVATION CHAIN (sympy exact, all identities symbolic):
    Lemma A: for GENERIC Moebius M (symbolic coefficients, det != 0),
             { M(e^{a x}), x } = -a^2/2 identically -- modular-typed
             charts (affine in the log of the multiplier coordinate)
             carry constant Schwarzian -(ln lambda)^2/2.
    Lemma B: { M(x), x } = 0 identically -- autonomous charts (affine in
             the projective coordinate itself) carry 0.
    Lemma C: -a^2/2 = -Delta^2/2 iff a = +-Delta (exact solve), and the
             affine sigma-dictionaries (slope +-1) change nothing: the
             coset is determined by lambda alone.
    The v578 Moebius clock h = e^{Delta sigma} is exactly the
    modular-to-affine transition (control C3 runs it as the POSITIVE case).

  BLIND PROTOCOL (frozen): section H2 classifies the four deployed clock
  charts using ONLY the criterion above (the classifier's source is gated
  to contain no Schwarzian reference and no derivative call -- the
  non-circularity gate); section H3 then unblinds and compares the
  theorem's predicted cosets -(ln lambda)^2/2 against the independently
  computed transported Schwarzians.  Expected blind assignment:
  F_pole modular (|ln lambda| = Delta), F_Boltzmann modular (Delta),
  F_QCD autonomous (lambda = 1), F_relic degenerate/unclassifiable.

  GATES:
    H1 non-circularity + derivation chain: classifier source free of
       Schwarzian/derivative references (code gate); Lemmas A, B, C exact.
    H2 blind assignment: the four deployed charts classify as expected
       above, all witnesses exact (functional identity + constancy),
       multipliers exact (|ln lambda| = Delta resp. 0).
    H3 unblinding: predicted cosets == transported Schwarzians EXACTLY
       (sympy zero), including the relic consistency (unclassifiable AND
       degenerate jets).
    H4 controls (all must fire):
       C1 fake KMS witness (frozen fake: w(x) = e^{-Delta x}(1+x^2) with
          the claimed seam holonomy): functional identity FAILS and the
          multiplier cross-ratio is NON-constant (m(0) != m(1) exact) --
          the witness gate catches the fake;
       C2 affine reparametrization of the clock (frozen: x -> -x + c, the
          deployed dictionary class |slope| = 1): typing AND |ln lambda|
          unchanged;
       C3 the v578 Moebius clock t = e^{Delta sigma} applied to the QCD
          chart: typing FLIPS to modular with |ln lambda| = Delta and the
          theorem then PREDICTS -Delta^2/2, confirmed by the transported
          Schwarzian (the K1-duty transplant as the positive case).

  VERDICT ENUM (frozen):
    KMS-COSET-THEOREM   -- H1-H4 all pass: the fiber classification of the
                           fibered functor is a theorem
    KMS-COSET-PARTIAL   -- some gate fails but H1 holds (name the gates)
    KMS-COSET-CIRCULAR  -- H1 fails: the only workable criterion secretly
                           references the Schwarzian (typed honestly)

FIREWALL: search-surface probe; no marker moves, nothing upgrades
CONTRACT.F.01 or FTRANSFER.CLOCKS.01 outside a future promotion round; all
constants from the frozen corpus (Delta = 6 log(3/2); the frozen YAML
gauges; no new number enters).
"""
from __future__ import annotations

import hashlib
import inspect
import os
import time

import sympy as sp

T_START = time.time()
HERE = os.path.abspath(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "..", "experiments", "ftransfer-clocks"))
_LAST = {}

YAML_PATH = os.path.join(HERE, "hypotheses", "ftransfer_clocks_v1.yaml")
YAML_SHA256 = "880224f76380c77dce2c1e3d7651bccc9e1619e74c60b7e15326ee0ee2bbf4d0"
GSTAR_CSV = os.path.join(HERE, "data", "gstar_saikawa_shirai_2018.csv")
GSTAR_SHA256 = "8ae2a4fec098fd68d3a469fbf2b7806ee1630f5595498a3e6cf2abca2d79b939"
ALPHAS_CSV = os.path.join(HERE, "data", "alphas_pdg2024_running.csv")
ALPHAS_SHA256 = "2ca6332dd1ee0caa089f64be58e90a8c916c94bbe612125eca41da50c33a2ac2"

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
    return sp.simplify(y3 / y1 - sp.Rational(3, 2) * (y2 / y1) ** 2)


def moebius(T, y):
    return (T[0, 0] * y + T[0, 1]) / (T[1, 0] * y + T[1, 1])


# ---------------------------------------------------------------------------
# THE CLASSIFIER (frozen criterion; the non-circularity gate inspects this
# function's source: NO Schwarzian reference, NO derivative of any order --
# only the functional identity at shifted arguments, the holonomy class,
# fixed points, and the multiplier cross-ratio).
# ---------------------------------------------------------------------------
def classify_clock(y, x, T):
    """Type a clock chart from its flow y(x) and candidate time-1 map T.
    Returns (typing, ln_mult_abs, witness_ok):
      typing in {"modular", "autonomous", "degenerate", "witness-failed"};
      ln_mult_abs = |ln lambda| of the holonomy multiplier (0 if parabolic,
      None if degenerate/failed)."""
    # (i) holonomy grounded in the flow: y(x+1) = T(y(x)) identically
    fe = sp.simplify(y.subs(x, x + 1) - moebius(T, y))
    if fe != 0:
        return "witness-failed", None, False
    # (ii) PGL2 class of T
    if T[0, 1] == 0 and T[1, 0] == 0 and sp.simplify(T[0, 0] - T[1, 1]) == 0:
        return "degenerate", None, True                      # scalar: identity in PGL2
    disc = sp.simplify(sp.trace(T) ** 2 / T.det() - 4)
    if disc == 0:
        return "autonomous", sp.S.Zero, True                 # parabolic: lambda = 1
    # (iii) hyperbolic candidate: fixed points ON P^1 (infinity included:
    # c w^2 + (d - a) w - b = 0; c = 0 puts one fixed point at infinity)
    # + multiplier cross-ratio witness
    a_T, b_T, c_T, d_T = T[0, 0], T[0, 1], T[1, 0], T[1, 1]
    yn, ys = y.subs(x, x + 1), y
    if sp.simplify(c_T) == 0:
        p = sp.simplify(b_T / (a_T - d_T))                   # finite fixed point
        m = sp.simplify((yn - p) / (ys - p))                 # cross-ratio with pp = oo
    else:
        w = sp.symbols("w_fp")
        fps = sp.solve(sp.Eq(c_T * w**2 + (d_T - a_T) * w - b_T, 0), w)
        if len(fps) != 2:
            return "witness-failed", None, False
        p, pp = fps
        m = sp.simplify(((yn - p) * (ys - pp)) / ((yn - pp) * (ys - p)))
    if m.has(x):                                             # constancy in x AND constants
        return "witness-failed", None, False
    lam = sp.simplify(m)
    return "modular", sp.Abs(sp.log(lam)), True


def main() -> int:
    print("=" * 78)
    print("F_TRANSFER KMS-COSET -- coset assignment from modular typing (post-fibered)")
    print("=" * 78)

    ok = all([
        check("H0 prereg YAML byte-freeze reused", sha256_file(YAML_PATH) == YAML_SHA256),
        check("H0 frozen g_*s table untouched", sha256_file(GSTAR_CSV) == GSTAR_SHA256),
        check("H0 frozen alpha_s table untouched", sha256_file(ALPHAS_CSV) == ALPHAS_SHA256),
    ])
    if not ok:
        print("\nVERDICT: ABORT -- freeze guard failed")
        return 1

    Delta = 6 * sp.log(sp.Rational(3, 2))
    Dsq2 = Delta**2 / 2
    x, sigma, a_sym = sp.symbols("x sigma a", real=True)
    C1, cg, B1, a0, th_i, c_off = sp.symbols("C1 c_g B1 alpha0 theta_i c", positive=True)
    ma, mb, mc, md = sp.symbols("m_a m_b m_c m_d", real=True)

    # The four deployed flows in their OWN frozen clocks (identical to the
    # executed contract) and their time-1 holonomies (verified against the
    # flow inside the classifier, gate (i)):
    lam_seam = sp.exp(Delta)
    F_pole_frame = sp.Matrix([[1, -5], [1, -2]])             # w = (q-5)/(q-2)
    T_pole = F_pole_frame.inv() * sp.diag(lam_seam, 1) * F_pole_frame
    q_pole = (5 - 2 * C1 * sp.exp(Delta * (x + cg))) / (1 - C1 * sp.exp(Delta * (x + cg)))
    y_boltz = B1 * sp.exp(-Delta * x)
    T_boltz = sp.diag(sp.exp(-Delta), 1)
    y_qcd = a0 / (1 + 7 * a0 * x / (2 * sp.pi))
    T_qcd = sp.Matrix([[1, 0], [7 / (2 * sp.pi), 1]])
    y_relic = th_i + 0 * x
    T_relic = sp.eye(2)

    # =======================================================================
    # H1 -- non-circularity + the derivation chain.
    # =======================================================================
    print("-" * 78)
    print("H1 non-circularity gate + derivation chain (sympy exact)")
    print("-" * 78)
    src = inspect.getsource(classify_clock)
    noncirc = ("schwarzian" not in src.lower() and ".diff" not in src
               and "Derivative" not in src and "diff(" not in src)
    check("H1 non-circularity: the classifier source contains NO Schwarzian "
          "reference and NO derivative call of any order -- typing uses only "
          "the functional identity, the holonomy class, fixed points and the "
          "multiplier cross-ratio", noncirc)

    M_gen = (ma * sp.exp(a_sym * x) + mb) / (mc * sp.exp(a_sym * x) + md)
    lemA = sp.simplify(schwarzian(M_gen, x) + a_sym**2 / 2)
    check("H1 Lemma A: {M(e^{a x}), x} = -a^2/2 identically for GENERIC Moebius "
          "M (symbolic coefficients) -- modular charts carry -(ln lambda)^2/2",
          lemA == 0, "residual = %s" % lemA)
    M_aff = (ma * x + mb) / (mc * x + md)
    lemB = schwarzian(M_aff, x) == 0
    check("H1 Lemma B: {M(x), x} = 0 identically -- autonomous charts carry 0", lemB)
    sols = sp.solve(sp.Eq(-a_sym**2 / 2, -Dsq2), a_sym)
    lemC = (len(sols) == 2
            and all(sp.simplify(s - Delta) == 0 or sp.simplify(s + Delta) == 0
                    for s in sols))
    check("H1 Lemma C: -a^2/2 = -Delta^2/2 iff a = +-Delta (exact solve: %s, "
          "each +-Delta symbolically); affine sigma-dictionaries (slope +-1) "
          "leave the value -- the coset is a FUNCTION of the typing datum "
          "lambda alone: S = -(ln lambda)^2/2" % sols, lemC)
    h1 = noncirc and lemA == 0 and lemB and lemC

    # =======================================================================
    # H2 -- BLIND assignment (no Schwarzian is computed in this section).
    # =======================================================================
    print("-" * 78)
    print("H2 blind assignment (classifier only; Schwarzians NOT computed here)")
    print("-" * 78)
    blind = {}
    for name, (y, T) in {"F_pole": (q_pole, T_pole), "F_Boltzmann": (y_boltz, T_boltz),
                         "F_QCD": (y_qcd, T_qcd), "F_relic": (y_relic, T_relic)}.items():
        typing, lnmult, wok = classify_clock(y, x, T)
        blind[name] = (typing, lnmult, wok)
    exp_types = {"F_pole": "modular", "F_Boltzmann": "modular",
                 "F_QCD": "autonomous", "F_relic": "degenerate"}
    h2 = True
    for name, want in exp_types.items():
        typing, lnmult, wok = blind[name]
        if want == "modular":
            good = typing == "modular" and wok and sp.simplify(lnmult - Delta) == 0
            det = "|ln lambda| = Delta = 6 log(3/2) exact, witness constant"
        elif want == "autonomous":
            good = typing == "autonomous" and wok and lnmult == 0
            det = "parabolic holonomy, lambda = 1"
        else:
            good = typing == "degenerate" and wok
            det = "identity holonomy -> unclassifiable (consistency with degenerate jets)"
        h2 = h2 and good
        check("H2 blind %s -> %s (%s)" % (name, typing, det), good)

    # =======================================================================
    # H3 -- unblinding: theorem prediction vs transported Schwarzians.
    # =======================================================================
    print("-" * 78)
    print("H3 unblinding: S_pred = -(ln lambda)^2/2 vs transported Schwarzians")
    print("-" * 78)
    k1s, k2s = sp.symbols("k1 k2", positive=True)
    S_meas = {"F_pole": schwarzian(q_pole.subs(x, -sigma + k1s), sigma),
              "F_Boltzmann": schwarzian(y_boltz.subs(x, -sigma + k2s), sigma),
              "F_QCD": schwarzian(y_qcd.subs(x, sigma), sigma)}
    h3 = True
    for name in ("F_pole", "F_Boltzmann", "F_QCD"):
        typing, lnmult, _ = blind[name]
        S_pred = -lnmult**2 / 2
        match = sp.simplify(S_meas[name] - S_pred) == 0
        h3 = h3 and match
        check("H3 %s: predicted %s = %.15f, transported Schwarzian %s -- EXACT match"
              % (name, S_pred, float(S_pred), sp.simplify(S_meas[name])), match)
    relic_consistent = blind["F_relic"][0] == "degenerate" and sp.diff(y_relic, x) == 0
    h3 = h3 and relic_consistent
    check("H3 relic consistency: criterion says unclassifiable (identity holonomy) "
          "AND the jets are degenerate (y' = 0 identically) -- no coset assigned, "
          "none exists", relic_consistent)

    # =======================================================================
    # H4 -- controls (must fire).
    # =======================================================================
    print("-" * 78)
    print("H4 controls (all three must fire)")
    print("-" * 78)
    # C1 fake KMS witness: claimed seam holonomy on a non-Moebius-exponential flow
    y_fake = sp.exp(-Delta * x) * (1 + x**2)
    typing_f, _, wok_f = classify_clock(y_fake, x, T_boltz)
    m0 = sp.simplify((y_fake.subs(x, 1) / y_fake.subs(x, 0)))
    m1 = sp.simplify((y_fake.subs(x, 2) / y_fake.subs(x, 1)))
    c1 = (typing_f == "witness-failed") and sp.simplify(m0 - m1) != 0
    check("H4.C1 fake-KMS control FIRES: scrambled detailed-balance data "
          "w(x) = e^{-Delta x}(1+x^2) with the claimed seam holonomy is caught "
          "(functional identity fails; ratio non-constant: m(0)/m(1) = %s vs %s)"
          % (m0, m1), c1)
    # C2 affine reparametrization x -> -x + c (deployed dictionary class)
    q_aff = q_pole.subs(x, -x + c_off)
    T_aff = F_pole_frame.inv() * sp.diag(sp.exp(-Delta), 1) * F_pole_frame
    typing_a, lnmult_a, wok_a = classify_clock(q_aff, x, T_aff)
    c2 = typing_a == "modular" and wok_a and sp.simplify(lnmult_a - Delta) == 0
    check("H4.C2 affine-invariance control: x -> -x + c leaves typing (modular) "
          "and |ln lambda| = Delta unchanged -- typing is affine-invariant, as "
          "the dictionary class requires", c2)
    # C3 the v578 Moebius clock on the QCD chart: the POSITIVE case
    y_moeb = y_qcd.subs(x, sp.exp(Delta * sigma))
    G = sp.Matrix([[-1, a0], [7 * a0 / (2 * sp.pi), 0]])     # w = (a0-y)*2pi/(7 a0 y)-frame
    T_moeb = G.inv() * sp.diag(lam_seam, 1) * G
    typing_m, lnmult_m, wok_m = classify_clock(y_moeb, sigma, T_moeb)
    S_moeb = schwarzian(y_moeb, sigma)
    c3 = (typing_m == "modular" and wok_m and sp.simplify(lnmult_m - Delta) == 0
          and sp.simplify(S_moeb + Dsq2) == 0)
    check("H4.C3 Moebius-clock control FIRES (the positive case): t = "
          "e^{Delta sigma} on the QCD chart flips typing to MODULAR with "
          "|ln lambda| = Delta, the theorem predicts -Delta^2/2, and the "
          "transported Schwarzian IS -Delta^2/2 exactly -- the K1-duty "
          "transplant as theorem confirmation", c3)
    h4 = c1 and c2 and c3

    # =======================================================================
    # Verdict (frozen enum).
    # =======================================================================
    if not h1:
        verdict = "KMS-COSET-CIRCULAR"
    elif h2 and h3 and h4:
        verdict = "KMS-COSET-THEOREM"
    else:
        verdict = "KMS-COSET-PARTIAL"
    failed = [g for g, okg in (("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)) if not okg]
    _LAST["verdict"] = verdict

    n_fail = sum(1 for c in CHECKS if not c["ok"])
    print("\nVERDICT: %s%s" % (verdict, "" if not failed else " -- failed: %s" % failed))
    print("theorem: S = -(ln lambda)^2/2 with lambda the time-1 holonomy multiplier "
          "per clock e-fold; modular clocks (tau, beta): lambda = e^{+-Delta} -> "
          "-Delta^2/2; autonomous RG clock: parabolic, lambda = 1 -> 0; relic: "
          "identity, unclassifiable")
    print("checks: %d, failures: %d" % (len(CHECKS), n_fail))
    print("elapsed: %.1f s" % (time.time() - T_START))

    # promoted module: results JSON not rewritten; writer of
    # record = experiments/ftransfer-clocks/ftransfer_kms_coset_probe.py
    print("(promoted module: results JSON not rewritten; writer of record\n"
          " = experiments/ftransfer-clocks/ftransfer_kms_coset_probe.py)")
    return 1 if n_fail else 0


def run():
    """run_all entry point (v757 precedent): expected pattern 18 checks,
    zero failures, verdict KMS-COSET-THEOREM."""
    rc = main()
    n_fail = sum(1 for c in CHECKS if not c["ok"])
    n_all = len(CHECKS)
    v = _LAST.get("verdict", "")
    ok = (rc == 0 and n_fail == 0 and n_all == 18
          and v == "KMS-COSET-THEOREM")
    print("\n[%s] PATTERN GATE: expected 18/18 with verdict "
          "KMS-COSET-THEOREM; got %d/%d, verdict: %s"
          % ("PASS" if ok else "FAIL", n_all - n_fail, n_all, v))
    print("\nCOMBINED ADJUDICATION: %s -- KMS-COSET-THEOREM: the clock "
          "coset is computed from the KMS/modular typing datum alone -- "
          "S = -(ln lambda)^2/2 with lambda the time-1 PGL2 holonomy "
          "multiplier per clock e-fold; modular clocks (tau, beta) carry "
          "-Delta^2/2, the autonomous RG clock carries 0, the relic chart "
          "is degenerate; blind assignment + exact unblinding + all three "
          "controls (fake KMS caught, affine invariance, Moebius-clock "
          "positive case).  The fiber classification of the fibered clock "
          "functor is a theorem, not case inspection.  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
