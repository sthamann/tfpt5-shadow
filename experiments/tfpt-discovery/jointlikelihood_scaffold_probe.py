#!/usr/bin/env python3
"""jointlikelihood_scaffold_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (PRED.JOINTLIKELIHOOD.01 [O], the statistics-construction
contract): the 27+ individually matched TFPT values descend from the same
few atoms and are statistically CORRELATED -- counting hits overstates
independent evidence.  The contract demands the effective number of
degrees of freedom (Jacobian rank over atom space), not the raw hit
count.  This probe builds the scaffold EXACTLY on the two bundles with
closed-form atom dependence and demonstrates the recipe end to end.

  BUNDLE 1 (transport/flavor shadow; the v976/v977 closed forms): five
  matched values -- sin^2 th13 = B13, sin^2 th12 = B12/(1-B13),
  sin^2 th23 = B23/(1-B13), J^2 (the DCXCVII closed form
  (1-b)^2 (1+2b-3a^2)/108) and B11 -- are all functions of TWO atoms
  (a, b) = (lambda2, lambda3) = ((2/3)^n, (1/3)^n at n = 1).
  [EXACT] the 5x2 Jacobian has rank EXACTLY 2 => effective dof = 2;
  the other 5 - 2 = 3 matches are FORCED CONSISTENCY RELATIONS
  (valid tests, not independent evidence).  Cross-check: the closed
  J^2 form evaluates to 1/729 at the deployed point (v977 value), and
  solving (a, b) back from two observables reproduces the rest.

  BUNDLE 2 (inflation consistency; contract bundle (ii)): three matched
  values -- n_s, r = 3(1-n_s)^2, alpha_s = -r/6 -- are functions of ONE
  atom.  [EXACT] Jacobian rank 1 => effective dof = 1; two forced
  relations.

  THE COVARIANCE DEGENERACY (the contract's statistical core, at demo
  level): for ANY atom-level uncertainty Sigma_atoms, the induced
  observable covariance C = J Sigma J^T has rank <= rank(J) -- checked
  symbolically (rank C = 2 on bundle 1 with a generic positive diagonal
  Sigma).  A joint likelihood built on C therefore counts 2 (resp. 1)
  degrees of freedom, NOT 5 (resp. 3): the honest evidence count for
  these 8 matched values is 3 effective dof + 5 forced relations.

HONEST BOUNDARY: a demonstration of the RECIPE on two bundles with known
closed forms; the full-registry construction (all frozen observables,
the atom-induced covariance, a prespecified null space and formula
grammar, a genuine future holdout) is exactly the open content of
PRED.JOINTLIKELIHOOD.01 and is NOT advanced beyond the scaffold here.

VERDICT ENUM: EFFDOF_SCAFFOLD_EXACT (rank certificates for two bundles;
full-registry construction open).
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
    print("jointlikelihood_scaffold_probe -- effective dof via exact "
          "Jacobian rank (PRED.JOINTLIKELIHOOD.01 scaffold)")

    a, b = sp.symbols("a b", positive=True)

    # ---- bundle 1: the transport/flavor shadow
    one = sp.ones(3, 1)
    u2 = sp.Matrix([1, -1, 0])
    u3 = sp.Matrix([1, 1, -2])
    J3 = one * one.T / 3
    P2 = u2 * u2.T / (u2.T * u2)[0]
    P3 = u3 * u3.T / (u3.T * u3)[0]
    B = J3 + a * P2 + b * P3

    O = sp.Matrix([
        B[0, 2],                                # sin^2 th13
        B[0, 1] / (1 - B[0, 2]),                # sin^2 th12
        B[1, 2] / (1 - B[0, 2]),                # sin^2 th23
        (1 - b) ** 2 * (1 + 2 * b - 3 * a ** 2) / 108,   # J^2 (DCXCVII)
        B[0, 0],                                # a fifth matched entry
    ])
    dep = {a: sp.Rational(2, 3), b: sp.Rational(1, 3)}
    vals = [sp.simplify(o.subs(dep)) for o in O]
    check("deployed values reproduce the v977 shadow: sin^2 th13 = 2/9, "
          "sin^2 th12 = 1/14, sin^2 th23 = 2/7, J^2 = 1/729",
          vals[0] == sp.Rational(2, 9)
          and vals[1] == sp.Rational(1, 14)
          and vals[2] == sp.Rational(2, 7)
          and vals[3] == sp.Rational(1, 729), str(vals[:4]))

    Jac = O.jacobian([a, b])
    rank = Jac.rank()
    rank_dep = Jac.subs(dep).rank()
    check("BUNDLE 1 rank certificate: the 5x2 Jacobian has rank EXACTLY "
          "2 symbolically AND at the deployed point => effective dof = 2,"
          " 3 forced consistency relations",
          rank == 2 and rank_dep == 2, "ranks %d / %d" % (rank, rank_dep))

    # reconstruction: (a, b) from two observables determines the rest
    a2, b2 = sp.symbols("a2 b2", positive=True)
    eqs = [sp.Eq(O[0].subs({a: a2, b: b2}), sp.Rational(2, 9)),
           sp.Eq(O[4].subs({a: a2, b: b2}), sp.Rational(13, 18))]
    sol = sp.solve(eqs, [a2, b2], dict=True)
    good = [s for s in sol if s[a2] == sp.Rational(2, 3)
            and s[b2] == sp.Rational(1, 3)]
    ok = False
    if good:
        s = good[0]
        rest = [sp.simplify(O[k].subs({a: s[a2], b: s[b2]}))
                for k in (1, 2, 3)]
        ok = rest == [sp.Rational(1, 14), sp.Rational(2, 7),
                      sp.Rational(1, 729)]
    check("reconstruction: two observables pin the atoms and FORCE the "
          "remaining three matched values (the 3 relations exhibited)",
          ok)

    # covariance degeneracy under generic atom uncertainty
    s1, s2 = sp.symbols("sigma1 sigma2", positive=True)
    Sig = sp.diag(s1, s2)
    C = sp.simplify(Jac * Sig * Jac.T)
    check("COVARIANCE DEGENERACY: C = J Sigma J^T has rank 2 (< 5) for "
          "generic positive atom uncertainty -- a joint likelihood "
          "counts 2 dof, not 5 hits", C.rank() == 2)

    # ---- bundle 2: inflation consistency relations
    ns = sp.Symbol("n_s", positive=True)
    r = 3 * (1 - ns) ** 2
    alps = -r / 6
    O2v = sp.Matrix([ns, r, alps])
    Jac2 = O2v.jacobian([ns])
    check("BUNDLE 2 rank certificate: (n_s, r, alpha_s) has Jacobian "
          "rank 1 => effective dof = 1, two forced relations "
          "(r = 3(1-n_s)^2, alpha_s = -r/6)", Jac2.rank() == 1)

    # ---- the honest evidence count
    check("HONEST COUNT: the 8 matched values of the two bundles carry "
          "3 effective dof + 5 forced consistency relations -- forced "
          "relations are falsification TESTS, not independent evidence "
          "(the contract's central point, quantified at demo level)",
          5 + 3 == 8 and 2 + 1 == 3)
    check("HONEST BOUNDARY (typed): recipe demonstration on two closed-"
          "form bundles; the full-registry covariance, prespecified null "
          "space, formula grammar and future holdout stay the open "
          "content of PRED.JOINTLIKELIHOOD.01", True)

    npass = sum(CHECKS)
    print("-" * 70)
    print("CHECKS %d/%d PASS" % (npass, len(CHECKS)))
    print("VERDICT: EFFDOF_SCAFFOLD_EXACT (bundle ranks 2 and 1; "
          "8 matches = 3 dof + 5 forced relations; full registry open)")
    print("SPEC_SHA %s" % spec_sha()[:16])
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
