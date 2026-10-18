#!/usr/bin/env python3
"""twistor_flatdir_gauge_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (the registered kill test in TFPT4D.LATTICE.ACTION.01 and the
open reading of SEAM.EQUIV.TWISTOR.01 after v973): the twistor measure is
rigid on the computable sector up to EXACTLY ONE flat direction -- the
uniform sector-weight shift dv = (1, 1, 1, 1) (the sector-0/bulk-Okubo
admixture).  Is that direction a VACUUM-ENERGY / COUNTERTERM GAUGE (shifts
only the normalization of Z) or a GENUINE MODULUS (shifts normalized
observables)?  This probe answers the question EXACTLY at the level of the
DECLARED measure structure and types the rest honestly.

THE DECLARED STRUCTURE (v508/v515/v973): the partition sum is a weighted
sum over the four mu4 sectors, Z(v) = sum_j e^{-v_j} Z_j, with v_j the
declared sector weights and Z_j the fixed sector data; every normalized
sector observable is a ratio O_a(v) = (sum_j A_{aj} e^{-v_j} Z_j) / Z(v).

  [EXACT] 1. GAUGE HALF: under v -> v + eps*(1,1,1,1) every sector factor
        picks up the SAME e^{-eps}: Z -> e^{-eps} Z, log Z -> log Z - eps
        (an additive vacuum-energy shift), and EVERY normalized ratio
        O_a is invariant IDENTICALLY IN eps AND in the sector data --
        proved symbolically with fully generic Z_j, A_{aj}, v_j.
  [EXACT] 2. TEETH: a NON-uniform shift (any direction with two unequal
        components) changes some normalized ratio for generic data --
        the invariance is a property of the flat direction, not of the
        observable class.
  [EXACT] 3. CONSISTENCY with v973: the uniform direction is exactly the
        one-dimensional moduli kernel found there (annihilated by every
        executed certificate functional); here it is additionally
        annihilated by ALL normalized sector ratios -- the two
        statements agree on the same direction.
  [EXACT] 4. COUNTERTERM READING: the shift acts as Z -> e^{-eps} Z,
        i.e. as a constant shift of the action (a cosmological-constant/
        counterterm term); in the W[J] = log Z[J] language of
        FTRANSFER.GENERATING.01 it moves W by a J-independent constant,
        so EVERY connected correlator (functional derivative at J) is
        blind to it -- checked on a 2-sector toy generating functional
        with symbolic sources.

HONEST BOUNDARY: this decides the question for the DECLARED (product/
exponential-weight) measure structure only.  IF the interacting BCOV
completion couples the sector weights nonlinearly (weights entering
observables NOT through the common exponential), the question reopens --
that is exactly the [O] residual of SEAM.EQUIV.TWISTOR.01 (the global
BCOV integral).  The kill test 'the flat direction shifts normalized
observables' therefore does NOT fire at the declared level; it stays live
only at the interacting level.

VERDICT ENUM: FLATDIR_VACUUM_GAUGE_DECLARED (interacting level open).
"""
import hashlib
import sys

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def spec_sha():
    with open(__file__, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    print("twistor_flatdir_gauge_probe -- is the v973 flat direction a "
          "vacuum gauge? (declared-measure level, symbolic)")

    eps = sp.Symbol("epsilon", real=True)
    Zj = sp.symbols("Z0:4", positive=True)          # generic sector data
    vj = sp.symbols("v0:4", real=True)              # declared weights
    Aj = sp.symbols("A0:4", real=True)              # generic observable row

    Z = sum(sp.exp(-vj[j]) * Zj[j] for j in range(4))
    O = sum(Aj[j] * sp.exp(-vj[j]) * Zj[j] for j in range(4)) / Z

    # 1. the uniform shift
    subs_u = {vj[j]: vj[j] + eps for j in range(4)}
    Z_shift = Z.subs(subs_u)
    check("GAUGE: Z(v + eps*1) = e^(-eps) Z(v) identically (vacuum-energy "
          "shift of log Z by -eps)",
          sp.simplify(Z_shift - sp.exp(-eps) * Z) == 0)
    O_shift = O.subs(subs_u)
    check("GAUGE: every normalized sector ratio O_a is invariant "
          "IDENTICALLY in eps and in all generic data Z_j, A_aj, v_j",
          sp.simplify(O_shift - O) == 0)

    # 2. teeth: non-uniform shift moves the ratio for generic data
    subs_n = {vj[0]: vj[0] + eps}                   # shift sector 0 only
    O_non = O.subs(subs_n)
    diff = sp.simplify(O_non - O)
    check("TEETH: the non-uniform shift (eps, 0, 0, 0) changes the ratio "
          "for generic data (difference not identically zero)",
          diff != 0)
    dO = sp.simplify(sp.diff(O_non, eps).subs(eps, 0))
    check("TEETH: first-order response of O to the non-uniform shift is "
          "a nonzero rational function (the direction genuinely enters)",
          dO != 0)

    # 3. consistency with the v973 kernel statement: the uniform direction
    # annihilates the first-order response of EVERY normalized ratio:
    dO_u = sp.simplify(sp.diff(O.subs(subs_u), eps).subs(eps, 0))
    check("v973 CONSISTENCY: first-order response of every normalized "
          "ratio along (1,1,1,1) is EXACTLY zero (the same 1-dim kernel "
          "direction, now at observable level)", dO_u == 0)

    # 4. counterterm reading on a toy generating functional:
    # W[J] = log( sum_j e^{-v_j} Z_j(J) ) with generic J-dependence;
    # uniform shift => W -> W - eps => all d^n W/dJ^n at any J unchanged.
    J = sp.Symbol("J", real=True)
    Zfun = [sp.Function("Zf%d" % j)(J) for j in range(2)]
    v2 = sp.symbols("w0:2", real=True)
    W = sp.log(sum(sp.exp(-v2[j]) * Zfun[j] for j in range(2)))
    W_shift = sp.log(sum(sp.exp(-(v2[j] + eps)) * Zfun[j]
                         for j in range(2)))
    check("W[J] reading: W(v + eps*1) = W(v) - eps identically in J "
          "(a J-independent constant)",
          sp.simplify(W_shift - (W - eps)) == 0)
    conn2 = sp.simplify(sp.diff(W_shift - W, J, 2))
    check("W[J] reading: every connected correlator d^n W/dJ^n is blind "
          "to the shift (n = 2 shown symbolically; higher n follow since "
          "the difference is J-independent)", conn2 == 0)

    check("HONEST BOUNDARY (typed): decided for the DECLARED exponential-"
          "weight structure only; if the interacting BCOV completion "
          "couples weights nonlinearly, the question reopens -- exactly "
          "the [O] residual of SEAM.EQUIV.TWISTOR.01", True)

    npass = sum(CHECKS)
    print("-" * 70)
    print("CHECKS %d/%d PASS" % (npass, len(CHECKS)))
    print("VERDICT: FLATDIR_VACUUM_GAUGE_DECLARED (interacting level open;"
          " the TFPT4D kill test does NOT fire at the declared level)")
    print("SPEC_SHA %s" % spec_sha()[:16])
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
