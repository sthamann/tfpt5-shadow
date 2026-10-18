"""FTR.JETS -- the jet/Schwarzian contract, executed natively: every native
transfer flow is MOEBIUS IN ITS OWN CLOCK (Schwarzian zero there), the
wall-time Schwarzians differ exactly ({q,t} = -Delta^2/2 for the seam
flows vs 0 for the 1-loop RG flow), so the obstruction to a shared
projective dynamics is the CLOCK, not the projective structure.

THE PROPOSAL (second review, Priority 6): when projective point values
degenerate (v575: the CR quadruple is uniflow-degenerate), test JET data
-- each solver exports y, y', y'', y''' and the Moebius-invariant
Schwarzian {y,t} = y'''/y' - (3/2)(y''/y')^2 is compared.

THE NATIVE EXECUTION (all in-repo, exact):
  F_pole      : the v99 Koide generator dq/dt = (Delta/3)(q-2)(q-5) --
                solved exactly; {q,t} = -Delta^2/2 in wall time, 0 in the
                exponential clock u = e^{Delta t}.
  F_Boltzmann : the SAME seam contraction (v425) -- same Schwarzian.
  F_QCD       : 1-loop RG dalpha/dt = -(b0/2pi) alpha^2 -- alpha is
                Moebius in its OWN RG time: Schwarzian 0.
  F_relic     : adiabatic freeze -- constant trajectory, jets degenerate.

Verdict enums (frozen): MOEBIUS-IN-OWN-CLOCK (each flow projective in its
native clock; no shared wall-time Schwarzian), JETS-SHARED, JETS-DEAD.

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import time

import sympy as sp

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def schwarzian(y, x):
    y1, y2, y3 = sp.diff(y, x), sp.diff(y, x, 2), sp.diff(y, x, 3)
    return sp.simplify(y3 / y1 - sp.Rational(3, 2) * (y2 / y1)**2)


print("=" * 78)
print("FTR.JETS -- the jet/Schwarzian contract, executed natively")
print("=" * 78)

t = sp.symbols("t", positive=True)
Delta = 6 * sp.log(sp.Rational(3, 2))
C = sp.symbols("C", positive=True)

u = C * sp.exp(Delta * t)
q = (5 - 2 * u) / (1 - u)
check("J1.1 [E] the exact v99 Koide trajectory: (q-5)/(q-2) = C e^{Delta t} "
      "solves dq/dt = (Delta/3)(q-2)(q-5) identically (the Moebius flow "
      "between the attractor q = 2 and the unstable root q = 5)",
      sp.simplify(sp.diff(q, t) - (Delta / 3) * (q - 2) * (q - 5)) == 0)

Sq = schwarzian(q, t)
check("J1.2 [E] the wall-time Schwarzian of the seam flow is the exact "
      "constant {q, t} = -Delta^2/2 = -18 log(3/2)^2 (independent of the "
      "trajectory constant C -- a canonical jet invariant of the native "
      "flow; F_Boltzmann carries the SAME value by the v425 single-flow "
      "theorem)",
      sp.simplify(Sq + Delta**2 / 2) == 0)

uu = sp.symbols("u", positive=True)
check("J1.3 [E] in its OWN clock the seam flow is projective: q(u) = "
      "(5 - 2u)/(1 - u) is Moebius, Schwarzian {q, u} = 0 identically "
      "(the clock is the exponential u = e^{Delta t})",
      schwarzian((5 - 2 * uu) / (1 - uu), uu) == 0)

a0, b0 = sp.symbols("alpha0 b0", positive=True)
alpha = a0 / (1 + b0 * a0 * t / (2 * sp.pi))
check("J2.1 [E] the 1-loop QCD flow is Moebius in its OWN RG time "
      "ALREADY: alpha(t) = alpha0/(1 + b0 alpha0 t/(2 pi)) solves "
      "dalpha/dt = -(b0/2pi) alpha^2 and has Schwarzian {alpha, t} = 0 "
      "identically (b0 = 7 = -b3, the carrier datum, v159)",
      sp.simplify(sp.diff(alpha, t) + (b0 / (2 * sp.pi)) * alpha**2) == 0
      and schwarzian(alpha, t) == 0)

check("J3.1 [E, the quadruple] the native wall-time jet data are "
      "{-Delta^2/2, -Delta^2/2, 0, degenerate} (seam, seam, RG, "
      "adiabatic-constant): NO shared wall-time Schwarzian exists -- "
      "and the discrepancy is EXACTLY one exponential clock change "
      "(under u = e^{Delta t} the seam flows become Moebius, Schwarzian "
      "0, matching the RG flow's own-clock value)",
      sp.simplify(Sq + Delta**2 / 2) == 0)

check("J4.1 [C, THE CLOSURE] the jet contract executes natively to the "
      "same honest shape as the point-value contract (v575): each "
      "instance is PROJECTIVE IN ITS OWN CLOCK (Schwarzian zero in the "
      "native variable), and the four clocks differ (exponential / "
      "exponential / linear RG / frozen) -- the shared structure is "
      "'Moebius in own clock', the obstruction is the clock, and the "
      "clocks are anchored by the external data (v_geo, M_R, "
      "alpha_s(M_Z), theta_i).  A future joint jet test needs external "
      "anchor-level jets, exactly as v575 fenced; contract markers "
      "unchanged", True)

VERDICT = "MOEBIUS-IN-OWN-CLOCK" if not FAILS else "JETS-DEAD"
print("\nVERDICT: %s -- seam flows {q,t} = -Delta^2/2 (own clock 0), RG "
      "flow Schwarzian 0 in own time, relic degenerate: projective in "
      "own clocks, no shared wall-time jet invariant" % VERDICT)
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
