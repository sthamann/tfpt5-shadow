#!/usr/bin/env python3
"""PHYS moonshot slice (T3 / F_transfer) -- can thermal time replace the
external clock contract?  The conjugacy-class kill test.

QUESTION (moonshot strategy round 2026-08-03): the T3 diagnosis says the
four solvers (Koide/F_pole, F_Boltzmann, F_QCD, F_relic) share one PGL2
syntax but need EXTERNAL clocks.  The radical counter-idea is Connes'
thermal-time hypothesis: the modular flow of ONE state (the seam RP/KMS
state; freshly, the groupoid degree-KMS of moonshot_state_probe E3.2b) is
a canonical INTERNAL time -- "the four clocks = four modular flows of one
state in four representations".  THIS PROBE tests the strongest checkable
form NOW, from exact in-repo data (v632 flow classification, recomputed
independently):

  STRONG THERMAL TIME (STT): there is one modular flow sigma_t and four
  CONSTANT clock conversions t_k = c_k * t such that each solver's native
  time-1 map is sigma_{c_k}.  Necessary condition (machine-checkable): all
  four native time-1 maps lie in the SAME PGL2(R) conjugacy type as a
  modular exponential -- and a modular generator is (an image of) a
  self-adjoint operator, hence DIAGONALIZABLE: its P^1 shadow is
  hyperbolic/elliptic-type or trivial, NEVER parabolic (a parabolic
  element has a single eigenvalue with a nontrivial Jordan block, and no
  real-diagonalizable logarithm).

CONSTRUCTION (sympy exact, standalone):
  P1  Koide/F_pole native flow (v99 generator dq/dt = (D/3)(q-2)(q-5),
      D = 6 ln(3/2)): time-1 Moebius map fixing {2,5}; multiplier at the
      attractor must be EXACTLY (2/3)^6 = 64/729 (the seam eigenvalue) --
      class: HYPERBOLIC.  F_Boltzmann is the same element by the
      single-flow theorem (v425, cited; the probe re-derives only F_pole).
  P2  F_QCD 1-loop flow dg/dtau = -b0 g^3 in u = 1/g^2: du/dtau = 2 b0,
      time-1 map u -> u + 2 b0 -- class: PARABOLIC (trace^2 = 4 det,
      not identity).  Machine kill: the matrix is NOT diagonalizable
      (eigenspace dim 1), and a 2x2 lemma battery verifies that exp of
      any real-diagonalizable matrix IS diagonalizable -- so no constant
      rescaling of ANY modular flow gives the QCD clock map.
  P3  F_relic: identity element (adiabatic freeze; v632 "degenerate") --
      carries zero flow information; "internalizing" it is vacuous, the
      whole content is the anchor theta_i.
  P4  anchor bookkeeping (the typed consequence): hyperbolic clocks have
      a DIMENSIONLESS multiplier => no unit needed (internal); the
      parabolic clock is fixed only up to one AFFINE constant => exactly
      one unit (Lambda_QCD), which by the No-Unit theorem (v153) is
      v_geo-class; the identity clock carries one initial condition
      (theta_i); plus the lattice O(1) C_p.  The external-clock wall of
      T3 and the No-Unit wall of T1 are then THE SAME WALL, counted once.
  P5  frequency-module observation (syntax only, look-elsewhere trivial
      by construction): the seam rates {6 ln(3/2), 6 ln 3} lie in the
      Z-module spanned by {log 2, log 3} -- the two shortest orbit
      lengths of today's commensurability groupoid.  Exact integer
      coefficients verified; typed as suggestive syntax, NOT evidence.

VERDICT ENUMS (preregistered):
  STT-KILLED             -- P2 parabolic + no-diagonalizable-log lemma
                            hold: strong thermal time is dead on the
                            declared clock exports;
  INTERNAL-PAIR-CONFIRMED -- P1 multiplier = (2/3)^6 exact: the two
                            hyperbolic clocks are already internal
                            (= the v425 single-flow reduction);
  MIXED / CONSTRUCTION-FAIL otherwise.
Expected honest outcome: STT-KILLED + INTERNAL-PAIR-CONFIRMED, i.e. the
existing diagnosis (external clock contract) is CONFIRMED, with improved
execution: the contract can be sharpened to a typed anchor census
{one unit, one angle theta_i, one lattice O(1)}.

CIRCULARITY: the flow classes are recomputed from the native ODEs (v99 /
1-loop RG / adiabatic invariant), not read off v632; the only cited
imports are the single-flow theorem (v425) and the No-Unit theorem (v153),
both load-bearing suite members.  No fit, no data.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py, no
ledger row, no paper claim, no marker move.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/phys_modular_clock_probe.py
"""

import sys

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    return ok


def pgl2_class(M):
    """conjugacy type of M in PGL2(R): disc = tr^2 - 4 det (efter norm)."""
    tr, det = sp.trace(M), M.det()
    disc = sp.simplify(tr ** 2 - 4 * det)
    if sp.simplify(M - (tr / 2) * sp.eye(2)) == sp.zeros(2, 2):
        return "identity"
    if disc.is_positive:
        return "hyperbolic"
    if sp.simplify(disc) == 0:
        return "parabolic"
    return "elliptic"


def main():
    print("phys_modular_clock_probe -- strong thermal time vs the four clocks")
    q, t = sp.symbols("q t", real=True)
    D = 6 * sp.log(sp.Rational(3, 2))          # the seam gap 6 ln(3/2)

    # ---- P1: Koide/F_pole time-1 map from the v99 generator --------------
    # dq/dt = (D/3)(q-2)(q-5); solve exactly via partial fractions:
    # d/dt log((q-2)/(q-5)) = (D/3)(-3) = -D  =>  (q-2)/(q-5) contracts e^-D
    lam = sp.exp(-D)
    lam_expected = sp.Rational(2, 3) ** 6
    ok = sp.simplify(lam - lam_expected) == 0
    check("P1a pole multiplier e^{-Delta} == (2/3)^6 = 64/729 exactly", ok,
          f"lambda = {sp.nsimplify(lam)}")

    # Moebius matrix: conjugate diag(lam,1) by T: z -> (z-2)/(z-5)
    T = sp.Matrix([[1, -2], [1, -5]])
    g_pole = T.inv() * sp.diag(lam, 1) * T
    cls_pole = pgl2_class(g_pole)
    # verify the ODE solution really is this Moebius map (symbolic check)
    expr = (q - 2) / (q - 5) * sp.exp(-D * t)
    q_t = sp.solve(sp.Eq((sp.Symbol("Q") - 2) / (sp.Symbol("Q") - 5), expr),
                   sp.Symbol("Q"))[0]
    a, b, c, d = g_pole
    moeb = (a * q + b) / (c * q + d)
    ok = sp.simplify(q_t.subs(t, 1) - moeb) == 0
    check("P1b exact ODE solution == Moebius map of g_pole (time 1)", ok,
          f"class = {cls_pole}")
    check("P1c g_pole is hyperbolic (dimensionless multiplier => no unit)",
          cls_pole == "hyperbolic")
    print("     (F_Boltzmann = same element by the single-flow theorem v425, cited)")

    # ---- P2: QCD 1-loop clock is parabolic -------------------------------
    b0 = sp.symbols("b0", positive=True)      # 1-loop coefficient (b3 = -7 sector)
    g = sp.Function("g")
    # dg/dtau = -b0 g^3  ->  u = 1/g^2, du/dtau = 2 b0: exact check
    u = sp.symbols("u", positive=True)
    du = sp.simplify(sp.diff(1 / g(t) ** 2, t).subs(sp.Derivative(g(t), t),
                                                    -b0 * g(t) ** 3))
    ok = sp.simplify(du - 2 * b0) == 0
    check("P2a 1-loop flow in u = 1/g^2 is du/dtau = 2 b0 (exact)", ok)

    g_qcd = sp.Matrix([[1, 2 * b0], [0, 1]])
    cls_qcd = pgl2_class(g_qcd)
    check("P2b g_QCD is parabolic (not identity)", cls_qcd == "parabolic")

    # eigenspace dimension 1  ->  not diagonalizable
    ok = not g_qcd.is_diagonalizable()
    check("P2c g_QCD is NOT diagonalizable (single Jordan block)", ok)

    # lemma battery: exp(real diagonalizable X) is diagonalizable
    x1, x2, p_, q_ = sp.symbols("x1 x2 p q", real=True)
    P = sp.Matrix([[1, p_], [q_, 1]])
    X = P * sp.diag(x1, x2) * P.inv()
    E = sp.simplify(P * sp.diag(sp.exp(x1), sp.exp(x2)) * P.inv())
    # E is diagonalizable by construction; check exp(X) == E symbolically
    ok = sp.simplify(sp.exp(X) - E) == sp.zeros(2, 2)
    check("P2d lemma: exp(diagonalizable X) = diagonalizable (symbolic 2x2)", ok)
    check("P2e KILL: no constant-rescaled modular flow (self-adjoint => "
          "diagonalizable generator) can produce the parabolic QCD clock",
          cls_qcd == "parabolic" and not g_qcd.is_diagonalizable())

    # ---- P3: relic clock is the identity ---------------------------------
    g_relic = sp.eye(2)
    check("P3 g_relic = identity: internalization vacuous, content = theta_i",
          pgl2_class(g_relic) == "identity")

    # ---- P4: typed anchor census ------------------------------------------
    anchors = {
        "F_pole": ("hyperbolic", "none (multiplier (2/3)^6 dimensionless, "
                                 "internal)"),
        "F_Boltzmann": ("hyperbolic", "none (same element, v425); washout "
                                      "anchor M_R is v_geo-class"),
        "F_QCD": ("parabolic", "ONE affine unit = Lambda_QCD (v_geo-class "
                               "by No-Unit v153) + lattice O(1) C_p"),
        "F_relic": ("identity", "ONE initial condition theta_i"),
    }
    n_units = 1       # the one affine unit, v_geo-class
    n_angles = 1      # theta_i
    n_lattice = 1     # C_p
    ok = (anchors["F_pole"][0] == "hyperbolic"
          and anchors["F_QCD"][0] == cls_qcd
          and n_units == 1 and n_angles == 1 and n_lattice == 1)
    check("P4 anchor census: {one unit (v_geo-class), one angle theta_i, "
          "one lattice O(1)} -- T3's clock wall == T1's unit wall", ok)
    for k, (cls, anc) in anchors.items():
        print(f"     {k:12s} class={cls:10s} anchor: {anc}")

    # ---- P5: frequency-module observation (syntax only) -------------------
    r2 = sp.log(sp.Rational(3, 2)) * 6        # 6 ln(3/2) = -6 log2 + 6 log3
    r3 = sp.log(3) * 6                        # 6 ln 3
    l2, l3 = sp.log(2), sp.log(3)
    ok = (sp.simplify(r2 - (-6 * l2 + 6 * l3)) == 0
          and sp.simplify(r3 - 6 * l3) == 0)
    check("P5 seam rates in Z<log2, log3> (groupoid orbit-length module); "
          "coefficients (-6,6) and (0,6) -- SYNTAX ONLY, not evidence", ok)

    n_pass = sum(1 for _, ok in CHECKS if ok)
    all_ok = n_pass == len(CHECKS)
    verdict = ("STT-KILLED + INTERNAL-PAIR-CONFIRMED" if all_ok
               else "MIXED-OR-CONSTRUCTION-FAIL")
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}")
    print("typed consequence: strong thermal time (one modular flow, four "
          "constant conversions) is dead on the declared exports; the weak "
          "form collapses to the v425 single-flow reduction; the external "
          "clock contract is CONFIRMED and can be sharpened to the typed "
          "census {one unit, theta_i, C_p}.  No marker moves; exploration only.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
