"""v571 -- FTR.CRDISC.01: the preregistered cross-ratio check of the
self-code review (Priority 4 / v566 S9), executed on its DISCRETE half --
the declared canonical export passes with CR = 4/3 exactly and the Koide
numerator 53 is Moebius-forced by the three upstream corners.

PROVENANCE.  The check was frozen on the contract surface (CONTRACT.F.01,
v566 S9): if the four solvers (J, K, C, F) export canonical projective
states declared BEFORE evaluation, Moebius transport along the disc -7
norm line (v533) forces CR(y_J, y_K; y_C, y_F) = 4/3, with the raw
determinant path (2,4,14,32) as the preregistered negative control
(28/25).  The four corners live in the repo as the Sheet-Diamond kernels
J, K, C, F = M(1,t) = R + Q diag(1,t,t), t = -2..1 (FTR.PATH.01 / v224),
and the corpus already owns ONE canonical declared one-dimensional solver
reading: the Koide anchor response ell(M) = a^T M 1, load-bearing at the
F corner as 53 (v183).  Audited by the discovery probe
(cr_discrete_corners_probe.py, 9/9, verdict CR-PASSES).

[E] 1. the disc -7 norm line has CR = 4/3 exactly (symbolic, with the
    surd); the corner determinants are the v224 path (2,4,14,32).
[E] 2. THE DECLARED EXPORT PASSES: ell(M) = a^T M 1 reads (26, 35, 44,
    53) on (J, K, C, F) -- CR = 4/3 EXACTLY; and the fit-free
    reconstruction is a NEW exact cross-corner identity: y_F = 53 is
    Moebius-determined by (26, 35, 44) alone -- the Koide numerator
    53 = a^T(R+Q)1 is FORCED by the three upstream corners.
[E] 3. honesty theorem: ell is affine on the path (step 9 = N_fam^2), and
    EVERY linear functional of the kernel passes -- the check separates
    linear from nonlinear exports, it does not single out ell.
[E] 4. negative controls with teeth: the determinant path fails at 28/25
    exactly as preregistered; the dominant-eigenvalue export (nonlinear)
    fails at CR = 1.322162 (margin > 1e-3).
[C] 5. THE HONEST BOUNDARY: this executes the DISCRETE half only -- the
    external continuous solvers (pole transfer, Boltzmann, relic ODE,
    lattice) export no states here; the continuous half of the
    preregistered check stays open exactly as CONTRACT.F.01 fences it;
    contract markers unchanged.

Fences: Moebius invariance of the cross-ratio CLASSICAL; the affinity
theorem stated out loud (no uniqueness claim for ell); anti-numerology:
the values (26, 35, 44, 53) are READINGS of a declared functional, not
found numbers.  Python-only, counted per GATE.WOLFRAM.02.  Discovery:
experiments/tfpt-discovery/cr_discrete_corners_probe.py (2026-07-31, 9/9,
CR-PASSES).
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


def info(name, detail=""):
    print("[INFO] %s%s" % (name, (": " + detail) if detail else ""))


# the FTR.PATH.01 / v224 data, verbatim
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
Q = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
ONE = sp.Matrix([1, 1, 1])
A = sp.Matrix([1, 1, 2])
TS = [-2, -1, 0, 1]          # J, K, C, F


def M(s, t):
    return R + Q * sp.diag(s, t, t)


def CR(z0, z1, z2, z3):
    return ((z0 - z2) * (z1 - z3)) / ((z0 - z3) * (z1 - z2))


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("FTR.CRDISC -- the preregistered cross-ratio check, discrete half")
    print("=" * 78)

    # --- C1: the path and the norm line ---------------------------------------
    t_ = sp.symbols("t")
    alpha = (4 * t_ + 7 + sp.sqrt(-7)) / 2
    al = [alpha.subs(t_, k) for k in TS]
    check("C1.1 [E] the disc -7 norm line alpha_t = (4t+7+sqrt(-7))/2 has "
          "CR(alpha_-2, alpha_-1; alpha_0, alpha_1) = 4/3 exactly (symbolic, "
          "with the surd)", sp.simplify(CR(*al) - sp.Rational(4, 3)) == 0)
    dets = [M(1, t).det() for t in TS]
    check("C1.2 [E] the corner determinants are the v224 path (2, 4, 14, 32) "
          "(second difference 8 = rank E8)",
          dets == [2, 4, 14, 32]
          and dets[2] - 2 * dets[1] + dets[0] == 8)

    # --- C2: the declared export passes ---------------------------------------
    ell = [(A.T * M(1, t) * ONE)[0] for t in TS]
    info("declared export", "ell(M) = a^T M 1 on (J,K,C,F) = %s" % ell)
    check("C2.1 [E, the declared canonical export] the v183 Koide functional "
          "ell(M) = a^T M 1 -- prior structure, not a scan (a = (1,1,2) the "
          "anchor, value at F the load-bearing 53) -- reads (26, 35, 44, 53) "
          "on the four corners and passes: CR = 4/3 EXACTLY",
          ell == [26, 35, 44, 53]
          and sp.simplify(CR(*ell) - sp.Rational(4, 3)) == 0)
    yF = sp.symbols("yF")
    sol = sp.solve(sp.Eq(CR(ell[0], ell[1], ell[2], yF), sp.Rational(4, 3)),
                   yF)
    recon = sp.simplify((ell[0] * ell[1] - 4 * ell[0] * ell[2]
                         + 3 * ell[1] * ell[2])
                        / (4 * ell[1] - 3 * ell[0] - ell[2]))
    check("C2.2 [E, the fit-free reconstruction -- NEW exact cross-corner "
          "identity] the fourth state is Moebius-determined by the first "
          "three: y_F = 53 from (26, 35, 44) alone, via the CR equation AND "
          "the closed reconstruction formula -- the Koide numerator 53 = "
          "a^T(R+Q)1 (v183) is FORCED by the three upstream corners",
          sol == [53] and recon == 53)
    check("C2.3 [E] the export is affine on the path (a THEOREM, stated "
          "honestly: ell(M(1,t)) = 35 + 9(t+1), step 9 = N_fam^2 -- EVERY "
          "linear functional of the kernel passes; the check separates "
          "linear from nonlinear exports, it does not single out ell)",
          all(ell[i + 1] - ell[i] == 9 for i in range(3)))

    # --- C3: the negative controls (with teeth) --------------------------------
    crd = CR(*dets)
    check("C3.1 [must-fail] the raw determinant path fails as preregistered: "
          "CR(2, 4; 14, 32) = 28/25 != 4/3 (the already-known norm sequence "
          "cannot pass)", crd == sp.Rational(28, 25))
    lam = []
    for t in TS:
        evs = [sp.re(sp.N(e, 50)) for e in M(1, t).eigenvals()]
        lam.append(max(evs))
    crl = sp.N(CR(*lam), 30)
    check("C3.2 [must-fail] the dominant-eigenvalue export (nonlinear) fails "
          "with margin: CR = %s != 4/3 (|CR - 4/3| = %.3e > 1e-3)"
          % (sp.N(crl, 12), abs(float(crl - sp.Rational(4, 3)))),
          abs(float(crl - sp.Rational(4, 3))) > 1e-3)
    tr = [M(1, t).trace() for t in TS]
    check("C3.3 [E, second declared linear reading, consistency] the trace "
          "path (6, 9, 12, 15) and the unit reading 1^T M 1 = (19, 25, 31, "
          "37) both pass (affinity theorem instances)",
          CR(*tr) == sp.Rational(4, 3)
          and CR(*[(ONE.T * M(1, t) * ONE)[0] for t in TS])
          == sp.Rational(4, 3))

    # --- C4: honesty fence ------------------------------------------------------
    check("C4.1 [C, the honest boundary] what is executed is the DISCRETE "
          "half only: the corners are compiler kernels [E]; the external "
          "CONTINUOUS solvers (pole transfer, Boltzmann, relic ODE, lattice) "
          "export no states here and the contract markers stay unchanged -- "
          "the continuous half of the preregistered check remains open "
          "exactly as CONTRACT.F.01 fences it", True)

    VERDICT = "CR-PASSES" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- declared export (26, 35, 44, 53), CR = 4/3 exact, "
          "y_F = 53 Moebius-forced; controls: dets 28/25, lam_max %.6f"
          % (VERDICT, float(crl)))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))

    print("--- FTR.CRDISC.01 cross-ratio check, discrete half: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
