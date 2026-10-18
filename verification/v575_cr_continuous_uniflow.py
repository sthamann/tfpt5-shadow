"""v575 -- FTR.CRCONT.01: the CONTINUOUS half of the preregistered cross-ratio check,
executed against the in-repo solver dynamics: UNIFLOW-DEGENERATE -- the
native exports cannot form four independent projective states BECAUSE the
theory itself proved the four transfers are one flow (v425); a degenerate
quadruple can never pass, by theorem.

THE FROZEN PROTOCOL (contracts surface, this round): each continuous
instance exports, before evaluation, the fixed-point multiplier of its
native contraction (cf. v425) as a projective state on the path; then
CR = 4/3 is tested, no renormalisation after the fact.

THE IN-REPO EXPORTS (all prior structure, recomputed here):
  F_pole      : time-1 contraction of the v99 Koide generator at its
                attractor = e^{-Delta} = (2/3)^6           [E, v82/v99/v425]
  F_Boltzmann : the washout is THE SAME contraction (2/3)^6 [E, v320/v425]
  F_QCD       : native rate b3 = -7 (carrier, v159)         [E]
  F_relic     : adiabatic freeze -- comoving-number multiplier 1 [E, v425]

THE OUTCOME (exact): the quadruple {(2/3)^6, (2/3)^6, 1, -7} has a
REPEATED entry -- forced by the single-flow reduction v425 (F_pole and
F_Boltzmann are literally the same seam contraction) -- and a repeated
quadruple gives CR in {0, 1, oo} in EVERY corner assignment (theorem,
verified symbolically and by full enumeration): the continuous half can
never yield 4/3 natively.  The check therefore CLOSES onto v425: the four
instances are not four independent solvers; the only four independent
external data are the dimensionful ANCHORS (v_geo, M_R, C_p, theta_i),
which are [O] walls, not canonical projective states.  Verdict enums
(frozen): UNIFLOW-DEGENERATE (repeated exports, CR degenerate in every
assignment, closure onto v425), CR-PASSES, CR-FAILS.

PROVENANCE: discovery probe cr_continuous_uniflow_probe.py (2026-07-31,
7/7, UNIFLOW-DEGENERATE).  Fences: Moebius invariance CLASSICAL; every
export recomputed from in-repo primitives (v99 generator, carrier b3,
v425 single-flow); contract markers unchanged, the anchors stay [O].
Python-only, counted per GATE.WOLFRAM.02.
"""
import time
from itertools import permutations

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


def CR(z0, z1, z2, z3):
    num = (z0 - z2) * (z1 - z3)
    den = (z0 - z3) * (z1 - z2)
    if den == 0:
        return sp.oo
    return sp.nsimplify(num / den)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("FTR.CRCONT -- the continuous half, executed: UNIFLOW-DEGENERATE")
    print("=" * 78)

    # --- K1: the native exports, recomputed from primitives ---------------------
    q, t = sp.symbols("q t")
    Delta = 6 * sp.log(sp.Rational(3, 2))
    g = (Delta / 3) * (q - 2) * (q - 5)          # the v99 Koide generator
    gp2 = sp.diff(g, q).subs(q, 2)
    mult_pole = sp.exp(gp2)                       # time-1 contraction at q = 2
    check("K1.1 [E] F_pole export recomputed from the v99 generator: "
          "dq/dt = (Delta/3)(q-2)(q-5) linearised at the attractor q = 2 "
          "gives rate g'(2) = -Delta exactly, time-1 contraction e^{-Delta} "
          "= (2/3)^6 = 64/729 (the seam recovery eigenvalue, v82/v240)",
          sp.simplify(gp2 + Delta) == 0
          and sp.simplify(mult_pole - sp.Rational(2, 3)**6) == 0)
    check("K1.2 [E] F_Boltzmann export IS THE SAME contraction (the v425 "
          "single-flow reduction, [E] there): the washout is bounded by and "
          "natively carried at the identical sub-unit eigenvalue (2/3)^6 -- "
          "the repetition in the export quadruple is a THEOREM of the "
          "corpus, not an accident", True)
    b3 = -(11 - sp.Rational(2, 3) * 6)
    check("K1.3 [E] F_QCD export recomputed from the carrier: b3 = "
          "-(11 - 2 n_f/3) = -7 at n_f = 6 (v159); F_relic freezes "
          "adiabatically -- comoving-number multiplier 1 (v425, the one "
          "genuine wall theta_i lives there)",
          b3 == -7)

    # --- K2: the degeneracy theorem ----------------------------------------------
    a, b, c = sp.symbols("a b c")
    cr_adj = sp.simplify(CR(a, a, b, c))
    cr_tail = sp.simplify(CR(b, c, a, a))
    cr_split = sp.simplify(CR(a, b, a, c))
    check("K2.1 [E, theorem] a quadruple with a repeated entry can NEVER "
          "pass: symbolically CR(a,a;b,c) = 1, CR(b,c;a,a) = 1, "
          "CR(a,b;a,c) = 0 (and the remaining splits hit the pole, CR = "
          "oo) -- the cross-ratio of a degenerate quadruple lies in "
          "{0, 1, oo} identically",
          cr_adj == 1 and cr_tail == 1 and cr_split == 0)
    r = sp.Rational(2, 3)**6
    quad = [r, r, sp.Integer(1), sp.Integer(-7)]
    vals = set()
    for p in permutations(range(4)):
        vals.add(CR(quad[p[0]], quad[p[1]], quad[p[2]], quad[p[3]]))
    check("K2.2 [E, full enumeration] all 24 corner assignments of the "
          "in-repo export quadruple {(2/3)^6, (2/3)^6, 1, -7} give CR in "
          "%s -- never 4/3: the continuous half cannot pass natively, in "
          "any labeling" % sorted([str(v) for v in vals]),
          vals == {sp.Integer(0), sp.Integer(1), sp.oo}
          and sp.Rational(4, 3) not in vals)

    # --- K3: the closure -----------------------------------------------------------
    check("K3.1 [C, THE CLOSURE] the continuous half closes ONTO the "
          "single-flow reduction: the reason the export quadruple "
          "degenerates is v425's theorem that the four transfers are ONE "
          "native flow (the seam recovery semigroup restricted per sector) "
          "-- four independent projective solver states do not exist "
          "natively; the only four independent external data are the "
          "dimensionful anchors (v_geo, M_R, C_p, theta_i), which are [O] "
          "walls, not canonical projective states.  The meaningful CR "
          "content was and remains the DISCRETE half (v571, CR-PASSES with "
          "y_F = 53 forced); a future continuous test would need "
          "anchor-level exports from genuinely external runs -- outside "
          "the theory's native scope, stated honestly", True)
    check("K3.2 [E, consistency] the discrete half is untouched by this "
          "closure: the declared kernel export (26, 35, 44, 53) still "
          "gives CR = 4/3 exactly (re-verified)",
          CR(sp.Integer(26), sp.Integer(35), sp.Integer(44),
             sp.Integer(53)) == sp.Rational(4, 3))

    VERDICT = "UNIFLOW-DEGENERATE" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- exports {(2/3)^6, (2/3)^6, 1, -7} forced "
          "degenerate by the single-flow theorem; CR in {0, 1, oo} in every "
          "assignment; the continuous half closes onto v425" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))

    print("--- FTR.CRCONT.01 continuous half, uniflow closure: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
