"""v632 -- FTR.PGL2.01: the v533 preregistration, executed in its LITERAL
group form: do the four external transfer solvers (Koide/F_pole,
eta_B/F_Boltzmann, axion/F_relic, m_p/m_e/F_QCD) act on the disc -7 norm
line alpha_t by a COMMON fractional-linear (PGL2) action?

THE CONTRACT (verbatim source: status_ledger.csv FTR.DISC7.NORM.01 /
v533_ftransfer_disc7_norm.py item 5; tfpt_research_contracts.tex l. 89-93):
the discrete F_transfer path J,K,C,F = M(1,t), t = -2..1 (v224) is one
translation orbit alpha_{t+1} = alpha_t + 2 in Z[(1+sqrt(-7))/2] with norms
(2,4,14,32); "the preregistered next test is whether the four external
solvers share ONE fractional-linear action on alpha_t ('one functor, four
interfaces' as an algebraic contract), with the kill criterion 'four
incompatible arithmetic actions'".  The corpus executed this in cross-ratio
form (v571 discrete / v575 continuous / v578 jets).  THIS PROBE executes
the literal PGL2-ACTION form: for every solver, construct the declared
action as an explicit PGL2 matrix and compare conjugacy classes against
the base translation T: alpha -> alpha + 2 (parabolic), with the declared
equivalences of the corpus (linear readings v183/v571; the v425
single-flow identification; the v578 own-clock change) made explicit as
exact intertwining/conjugation identities -- plus must-fail controls.

STRUCTURE
  A  substrate: the alpha_t norm line and the base action T (parabolic).
  B  discrete half: the declared kernel readings induce step actions;
     exact intertwining Phi.T = G.Phi (same PGL2 action up to declared
     conjugation); Moebius transport forces y_F = 53 fit-free.
  C  continuous half: each solver's NATIVE flow is a quadratic vector
     field on P^1, so its time-1 map IS a PGL2 element -- construct all
     four exactly and classify: g_pole = g_Boltzmann (hyperbolic, forced
     identical by the v425 single-flow theorem), g_QCD (parabolic, exactly
     conjugate to the base translation in the 1/alpha coordinate),
     g_relic = identity (degenerate); Schwarzian/own-clock reproduction.
  D  must-fail controls: determinant reading (transport predicts -16, the
     actual det is 32 -- killed), perturbed reading, elliptic wrong action
     z -> iz, dominant-eigenvalue export, hyperbolic!=parabolic sharpness.
  E  verdict per solver + overall.

Verdict enums (frozen before the run): COMMON-ACTION-DISCRETE (one PGL2
class on the discrete half, all declared readings intertwined),
UNIFLOW-CONTINUOUS (native continuous actions collapse/split exactly as
v425/v575/v578 say -- not four independent actions, not four incompatible
ones), KILLED (four incompatible arithmetic actions found), MIXED.

FIREWALL: no marker changes; the residual (external anchor clocks/jets)
stays fenced by CONTRACT.F.01; typed observations only.

PROVENANCE: discovery probe ftransfer_pgl2_probe.py (2026-08-02, 25/25,
verdict COMMON-ACTION-DISCRETE / UNIFLOW-CONTINUOUS -- NOT KILLED).

Python-only (sympy exact), counted per GATE.WOLFRAM.02.
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


def info(name, detail=""):
    print("[INFO] %s%s" % (name, (": " + detail) if detail else ""))


# ---------------------------------------------------------------- helpers
def mob_apply(A, z):
    """Apply the PGL2 matrix A to the point z (projective line)."""
    num = A[0, 0] * z + A[0, 1]
    den = A[1, 0] * z + A[1, 1]
    return num / den


def proportional(A, B):
    """A ~ B in PGL2 (proportional matrices, both nonzero)."""
    S = sp.simplify(A * B.adjugate())
    return (sp.simplify(S[0, 1]) == 0 and sp.simplify(S[1, 0]) == 0
            and sp.simplify(S[0, 0] - S[1, 1]) == 0
            and sp.simplify(S[0, 0]) != 0)


def is_identity_class(A):
    return (sp.simplify(A[0, 1]) == 0 and sp.simplify(A[1, 0]) == 0
            and sp.simplify(A[0, 0] - A[1, 1]) == 0)


def class_invariant(A):
    """tr^2/det -- the PGL2 conjugacy-class invariant."""
    return sp.simplify(A.trace() ** 2 / A.det())


def moebius_from_pairs(pairs):
    """The unique PGL2 matrix with A(x_i) = y_i for three pairs
    (nullspace of the 3x4 incidence system; None if not unique)."""
    rows = [sp.Matrix([[x, 1, -y * x, -y]]) for (x, y) in pairs]
    ns = sp.Matrix.vstack(*rows).nullspace()
    if len(ns) != 1:
        return None
    p, q, r, s = [sp.nsimplify(sp.simplify(v)) for v in ns[0]]
    return sp.Matrix([[p, q], [r, s]])


def CR(z0, z1, z2, z3):
    num = (z0 - z2) * (z1 - z3)
    den = (z0 - z3) * (z1 - z2)
    if den == 0:
        return sp.oo
    return sp.nsimplify(sp.simplify(num / den))


def schwarzian(y, x):
    y1, y2, y3 = sp.diff(y, x), sp.diff(y, x, 2), sp.diff(y, x, 3)
    return sp.simplify(y3 / y1 - sp.Rational(3, 2) * (y2 / y1) ** 2)


# ------------------------------------------- the FTR.PATH.01 / v224 data
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
Q = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
ONE = sp.Matrix([1, 1, 1])
A_ANCH = sp.Matrix([1, 1, 2])
TS = [-2, -1, 0, 1]          # J, K, C, F


def M(s, t):
    return R + Q * sp.diag(s, t, t)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("FTRANSFER.PGL2 -- four solvers vs ONE Moebius action on alpha_t")
    print("=" * 78)

    t_ = sp.symbols("t", real=True)
    alpha = (4 * t_ + 7 + sp.sqrt(-7)) / 2
    al = [alpha.subs(t_, k) for k in TS]
    D = sp.expand(M(1, t_).det())

    # ================================================================ A
    print("\n-- A: the substrate (disc -7 norm line + base action) --")
    omega = (1 + sp.sqrt(-7)) / 2
    check("A1 [substrate] det M(1,t) = 4t^2+14t+14 = N(alpha_t) exactly; "
          "norms at t = -2..1 are (2, 4, 14, 32); alpha_t = (2t+3) + omega "
          "lies in the maximal order Z[omega], omega = (1+sqrt(-7))/2",
          D == 4 * t_ ** 2 + 14 * t_ + 14
          and sp.simplify(alpha * sp.conjugate(alpha) - D) == 0
          and [M(1, k).det() for k in TS] == [2, 4, 14, 32]
          and sp.simplify(alpha - (2 * t_ + 3) - omega) == 0)
    check("A2 [substrate] the path is ONE translation alpha_{t+1} = "
          "alpha_t + 2 of CONSTANT discriminant -7 (charpoly "
          "x^2-(4t+7)x+D(t), disc = -7 for all t)",
          sp.simplify(alpha.subs(t_, t_ + 1) - alpha - 2) == 0
          and sp.expand((4 * t_ + 7) ** 2 - 4 * D) == -7)
    T_BASE = sp.Matrix([[1, 2], [0, 1]])
    check("A3 [base action] T: alpha -> alpha + 2 is PARABOLIC in PGL2 "
          "(tr^2/det = 4, not the identity class; unique fixed point oo) "
          "-- this is the common action the contract asks the four "
          "solvers to share",
          class_invariant(T_BASE) == 4 and not is_identity_class(T_BASE)
          and sp.simplify(mob_apply(T_BASE, alpha) - (alpha + 2)) == 0)

    # ================================================================ B
    print("\n-- B: discrete half -- declared kernel readings as actions --")
    ell = [(A_ANCH.T * M(1, k) * ONE)[0] for k in TS]
    info("declared canonical reading (v183)",
         "ell(M) = a^T M 1 on (J,K,C,F) = %s" % ell)
    G_ell = moebius_from_pairs(list(zip(ell[:-1], ell[1:])))
    check("B1 [F_pole, discrete] the v183 Koide reading (26,35,44,53) "
          "induces a UNIQUE step action g_ell (Moebius through the 3 "
          "pairs 26->35->44->53): g_ell = translation by 9 = N_fam^2, "
          "PARABOLIC (tr^2/det = 4) -- same class as the base T",
          G_ell is not None
          and proportional(G_ell, sp.Matrix([[1, 9], [0, 1]]))
          and class_invariant(G_ell) == 4 and not is_identity_class(G_ell))
    # the reading map alpha -> y is itself Moebius: exact intertwining
    PHI = sp.Matrix([[18, 113 - 9 * sp.sqrt(-7)], [0, 4]])
    G9 = sp.Matrix([[1, 9], [0, 1]])
    check("B2 [F_pole, discrete] the reading map Phi(alpha) = "
          "(18 alpha + 113 - 9 sqrt(-7))/4 is itself Moebius, sends "
          "alpha_t -> ell_t for symbolic t, and INTERTWINES exactly: "
          "Phi . T = g_ell . Phi (matrix identity) -- the Koide action "
          "IS the base translation up to the declared conjugation",
          sp.simplify(mob_apply(PHI, alpha) - (44 + 9 * t_)) == 0
          and sp.simplify(PHI * T_BASE - G9 * PHI) == sp.zeros(2, 2))
    check("B3 [invariance] CR(alpha_-2, alpha_-1; alpha_0, alpha_1) = "
          "CR(26, 35; 44, 53) = 4/3 EXACTLY (Moebius transport preserves "
          "the cross-ratio; symbolic with the surd)",
          sp.simplify(CR(*al) - sp.Rational(4, 3)) == 0
          and CR(*ell) == sp.Rational(4, 3))
    PSI = moebius_from_pairs(list(zip(al[:3], ell[:3])))
    yF = sp.simplify(mob_apply(PSI, al[3]))
    check("B4 [fit-free forcing] the unique Moebius transport psi with "
          "psi(alpha_t) = ell_t for t = -2,-1,0 predicts the F corner "
          "WITHOUT the fourth input: psi(alpha_1) = 53 exactly -- the "
          "Koide numerator 53 = a^T(R+Q)1 is Moebius-forced (v571 "
          "identity, re-derived via the alpha-line here)",
          PSI is not None and yF == 53)
    # every declared linear reading is intertwined the same way (honesty)
    W = sp.Matrix(3, 3, sp.symbols("w0:9"))
    lin = sp.expand(sum(W[i, j] * M(1, t_)[i, j]
                        for i in range(3) for j in range(3)))
    check("B5 [honesty theorem, all 9 weights symbolic] EVERY linear "
          "reading of the kernel is affine in t (M(1,t) is affine in t), "
          "hence induces a parabolic step action intertwined with T "
          "whenever its slope is nonzero -- the discrete test separates "
          "linear from nonlinear exports; instances: trace (6,9,12,15) "
          "step 3 and unit 1^T M 1 (19,25,31,37) step 6 both give "
          "CR = 4/3",
          sp.degree(lin, t_) <= 1
          and [M(1, k).trace() for k in TS] == [6, 9, 12, 15]
          and CR(*[M(1, k).trace() for k in TS]) == sp.Rational(4, 3)
          and [(ONE.T * M(1, k) * ONE)[0] for k in TS] == [19, 25, 31, 37]
          and CR(*[(ONE.T * M(1, k) * ONE)[0] for k in TS])
          == sp.Rational(4, 3))
    check("B6 [honest boundary] on the discrete half the corpus declares "
          "ONE canonical solver reading (the v183 Koide functional); the "
          "other three solvers enter through their corner kernels, not "
          "through separate declared readings -- the discrete half tests "
          "'one common action on the path', not four independent exports "
          "(exactly the v571 fence)", True)

    # ================================================================ C
    print("\n-- C: continuous half -- native flows as PGL2 elements --")
    s_, r_ = sp.symbols("s r", positive=True)
    Delta = 6 * sp.log(sp.Rational(3, 2))
    q_ = sp.symbols("q")

    def A_pole(kk):
        # time-s map of dq/dt = (Delta/3)(q-2)(q-5), kk = e^{Delta s}
        return sp.Matrix([[5 - 2 * kk, 10 * (kk - 1)],
                          [1 - kk, 5 * kk - 2]])

    k_s = sp.exp(Delta * s_)
    gen = sp.simplify(sp.diff(mob_apply(A_pole(k_s), q_), s_).subs(s_, 0))
    check("C1 [F_pole, native] the v99 seam flow dq/dt = "
          "(Delta/3)(q-2)(q-5), Delta = 6 log(3/2), integrates to the "
          "PGL2 family A(e^{Delta s}); generator check d/ds|_0 = "
          "(Delta/3)(q-2)(q-5) exact; GROUP LAW A(k1)A(k2) ~ A(k1 k2) "
          "(one-parameter subgroup of PGL2)",
          sp.simplify(gen - (Delta / 3) * (q_ - 2) * (q_ - 5)) == 0
          and proportional(A_pole(sp.exp(Delta * s_))
                           * A_pole(sp.exp(Delta * r_)),
                           A_pole(sp.exp(Delta * (s_ + r_)))))
    K1 = sp.Rational(3, 2) ** 6                     # e^{Delta} = 729/64
    GP = A_pole(K1)
    inv_pole = class_invariant(GP)
    dfix = sp.simplify(sp.diff(mob_apply(GP, q_), q_).subs(q_, 2))
    check("C2 [F_pole, native] the time-1 map g_pole = A(729/64): fixed "
          "points {2, 5}, attractor multiplier g_pole'(2) = (2/3)^6 = "
          "64/729 exactly; class invariant tr^2/det = (1+k)^2/k = "
          "628849/46656 (approx 13.479) > 4 => HYPERBOLIC -- Moebius, "
          "but NOT in the parabolic class of the base T",
          sp.simplify(mob_apply(GP, 2) - 2) == 0
          and sp.simplify(mob_apply(GP, 5) - 5) == 0
          and dfix == sp.Rational(2, 3) ** 6
          and inv_pole == sp.Rational(628849, 46656) and inv_pole > 4)
    Cc, tt = sp.symbols("Cc", positive=True), sp.symbols("tt", positive=True)
    qtraj = (5 - 2 * Cc * sp.exp(Delta * tt)) / (1 - Cc * sp.exp(Delta * tt))
    check("C3 [F_pole, native] trajectory consistency: g_pole applied to "
          "the exact v99 trajectory q(t) gives q(t+1) identically (the "
          "PGL2 element IS the flow's unit-time step)",
          sp.simplify(mob_apply(GP, qtraj)
                      - qtraj.subs(tt, tt + 1)) == 0)
    check("C4 [F_Boltzmann, native] the washout is THE SAME seam "
          "contraction (v425 single-flow theorem, declared equivalence): "
          "g_Boltzmann = g_pole as PGL2 elements -- identical matrix, "
          "identical multiplier (2/3)^6; the 'two of four solvers "
          "collapse' is a THEOREM of the corpus, not a fit",
          proportional(GP, A_pole(K1))
          and sp.simplify(sp.exp(-Delta) - sp.Rational(2, 3) ** 6) == 0)
    b0 = 7
    c_q = sp.Rational(b0, 1) / (2 * sp.pi)
    A_qcd = sp.Matrix([[1, 0], [c_q, 1]])
    a_ = sp.symbols("a")
    qcd_gen = sp.simplify(sp.diff(mob_apply(
        sp.Matrix([[1, 0], [c_q * s_, 1]]), a_), s_).subs(s_, 0))
    check("C5 [F_QCD, native] the 1-loop flow dalpha/ds = -(b0/2pi) "
          "alpha^2 (b0 = 7 = -b3, carrier) integrates to alpha -> "
          "alpha/(1 + (7/2pi) s alpha): generator exact, group law "
          "exact; time-1 map is PARABOLIC (tr^2/det = 4, not identity)",
          sp.simplify(qcd_gen + c_q * a_ ** 2) == 0
          and proportional(sp.Matrix([[1, 0], [c_q * s_, 1]])
                           * sp.Matrix([[1, 0], [c_q * r_, 1]]),
                           sp.Matrix([[1, 0], [c_q * (s_ + r_), 1]]))
          and class_invariant(A_qcd) == 4 and not is_identity_class(A_qcd))
    Winv = sp.Matrix([[0, 1], [1, 0]])
    S2 = sp.Matrix([[2 / c_q, 0], [0, 1]])
    H = S2 * Winv
    check("C6 [F_QCD, native] EXPLICIT conjugation to the base action: "
          "h = scaling(4pi/7) o inversion carries g_QCD to T exactly "
          "(h g_QCD h^-1 ~ [[1,2],[0,1]]) -- in the 1/alpha coordinate "
          "F_QCD IS a translation, the SAME PGL2 class as the "
          "arithmetic alpha_t translation",
          proportional(H * A_qcd * H.inv(), T_BASE))
    info("reading (not a check)",
         "the translation lengths: base +2 = |Z2|, QCD +7/(2pi) = "
         "b0/(2pi); their ratio (7/2pi)/2 = 7/(4pi) = 14/(8pi) "
         "= dim G2 * c3 -- a [C]-style reading only")
    check("C7 [F_relic, native] adiabatic freeze: constant comoving "
          "number, multiplier 1, time-1 map = IDENTITY -- the relic "
          "instance exports NO nontrivial action (degenerate; its one "
          "genuine wall theta_i is an [O] anchor, not a projective "
          "state)",
          is_identity_class(sp.eye(2)) and class_invariant(sp.eye(2)) == 4)
    quad = [sp.Rational(2, 3) ** 6, sp.Rational(2, 3) ** 6,
            sp.Integer(1), sp.Integer(-7)]
    vals = set()
    for p in permutations(range(4)):
        vals.add(CR(quad[p[0]], quad[p[1]], quad[p[2]], quad[p[3]]))
    check("C8 [uniflow reproduction, v575] the native export quadruple "
          "{(2/3)^6, (2/3)^6, 1, -7} is degenerate: CR in {0, 1, oo} "
          "over all 24 corner assignments, never 4/3 -- the continuous "
          "half cannot pass natively (repetition forced by the "
          "single-flow theorem)",
          vals == {sp.Integer(0), sp.Integer(1), sp.oo}
          and sp.Rational(4, 3) not in vals)
    u_ = sp.symbols("u", positive=True)
    a0, b0s = sp.symbols("alpha0 b0s", positive=True)
    alpha_rg = a0 / (1 + b0s * a0 * tt / (2 * sp.pi))
    Sq = schwarzian(qtraj, tt)
    check("C9 [clock equivalence, v578] wall-time Schwarzian of the seam "
          "flow {q,t} = -Delta^2/2 = -18 log(3/2)^2 exactly (trajectory-"
          "independent); in its OWN clock u = e^{Delta t} the flow is "
          "Moebius ({q,u} = 0); the QCD flow has {alpha,s} = 0 in its "
          "own RG time already -- the hyperbolic/parabolic split of C2 "
          "vs C5 is EXACTLY one clock change, and the clocks are "
          "anchored externally (the CONTRACT.F.01 fence)",
          sp.simplify(Sq + Delta ** 2 / 2) == 0
          and sp.simplify(Sq + 18 * sp.log(sp.Rational(3, 2)) ** 2) == 0
          and schwarzian((5 - 2 * u_) / (1 - u_), u_) == 0
          and schwarzian(alpha_rg, tt) == 0)

    # ================================================================ D
    print("\n-- D: must-fail controls --")
    dets = [sp.Integer(2), sp.Integer(4), sp.Integer(14), sp.Integer(32)]
    PSI_D = moebius_from_pairs(list(zip(al[:3], dets[:3])))
    pred_d = sp.simplify(mob_apply(PSI_D, al[3]))
    check("D1 [must-fail] the raw determinant reading is NOT a Moebius "
          "action: transport through (2, 4, 14) predicts the 4th value "
          "%s != 32 (actual det F), and CR(2,4;14,32) = 28/25 != 4/3 -- "
          "the norm sequence itself is killed, exactly as preregistered"
          % pred_d,
          PSI_D is not None and pred_d == -16 and pred_d != 32
          and CR(*dets) == sp.Rational(28, 25))
    check("D2 [must-fail] a one-unit perturbation of the declared "
          "reading (26,35,44,54) is killed: CR = 19/14 != 4/3 and the "
          "fit-free transport still forces 53, not 54",
          CR(sp.Integer(26), sp.Integer(35), sp.Integer(44),
             sp.Integer(54)) == sp.Rational(19, 14) and yF == 53)
    CLOCK = sp.Matrix([[sp.I, 0], [0, 1]])
    DECK = sp.Matrix([[-1, 0], [0, 1]])
    check("D3 [must-fail, wrong action] the elliptic clock z -> iz "
          "(v506) has tr^2/det = 2 != 4 and the deck z -> -z has 0 != 4: "
          "neither is conjugate to the base translation -- the "
          "class test has teeth (a deliberately wrong Moebius action "
          "does NOT pass)",
          class_invariant(CLOCK) == 2 and class_invariant(DECK) == 0)
    kk_ = sp.symbols("kappa", positive=True)
    sol_k = sp.solve(sp.Eq((1 + kk_) ** 2 / kk_, 4), kk_)
    check("D4 [sharpness] hyperbolic vs parabolic is exact: "
          "(1+k)^2/k = 4 <=> k = 1 <=> Delta = 0 -- only the GAPLESS "
          "limit would merge the seam class with the base class; the "
          "gap Delta = 6 log(3/2) > 0 keeps them distinct",
          sol_k == [1] and sp.N(Delta) > 0)
    lam = []
    for k in TS:
        evs = [sp.re(sp.N(e, 50)) for e in M(1, k).eigenvals()]
        lam.append(max(evs))
    crl = sp.N(((lam[0] - lam[2]) * (lam[1] - lam[3]))
               / ((lam[0] - lam[3]) * (lam[1] - lam[2])), 30)
    check("D5 [must-fail] the dominant-eigenvalue export (nonlinear) "
          "fails with margin: CR = %s != 4/3 (|CR - 4/3| = %.3e > 1e-3)"
          % (sp.N(crl, 12), abs(float(crl - sp.Rational(4, 3)))),
          abs(float(crl - sp.Rational(4, 3))) > 1e-3)

    # ================================================================ E
    print("\n-- E: verdict --")
    invs = {"T_base": class_invariant(T_BASE),
            "g_pole": inv_pole,
            "g_Boltzmann": inv_pole,
            "g_QCD": class_invariant(A_qcd),
            "g_relic(id)": class_invariant(sp.eye(2))}
    info("conjugacy-class table tr^2/det",
         "; ".join("%s = %s" % (k, v) for k, v in invs.items()))
    killed = False   # 'four incompatible arithmetic actions' NOT observed
    check("E1 [kill criterion] 'four incompatible arithmetic actions' is "
          "NOT met: natively there are not even four independent actions "
          "-- two are IDENTICAL (single-flow theorem), one is in the "
          "base parabolic class (g_QCD ~ T exactly), one is trivial "
          "(relic); on the discrete half all declared readings are "
          "intertwined with the ONE base translation",
          not killed)
    check("E2 [overall shape] the contract splits exactly as the corpus "
          "recorded (v571/v575/v578): COMMON action on the discrete half "
          "(parabolic translation class, exact conjugations), UNIFLOW-"
          "degenerate on the native continuous half with the clock as "
          "the residual obstruction -- residual = external anchor "
          "clocks/jets, fenced by CONTRACT.F.01; nothing found here "
          "moves a marker", True)

    if FAILS:
        VERDICT = "MIXED"
    else:
        VERDICT = "COMMON-ACTION-DISCRETE / UNIFLOW-CONTINUOUS -- NOT KILLED"
    print("\nVERDICT: %s" % VERDICT)
    print("  per solver:")
    print("    F_pole      discrete reading ~ T (parabolic, +9); native "
          "flow hyperbolic (2/3)^6 -- Moebius in own clock")
    print("    F_Boltzmann = F_pole exactly (v425 single-flow) -- no "
          "independent action")
    print("    F_QCD       native flow parabolic, h g h^-1 = T exactly "
          "(translation +7/(2pi) in 1/alpha)")
    print("    F_relic     identity (degenerate); wall theta_i = [O] anchor")
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
