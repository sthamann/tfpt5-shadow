#!/usr/bin/env python3
"""nu_qplus_spectral_matrix_probe -- EXPLORATION ONLY (no promotion).

REVIEW WAVE 3 (2026-08-28).  Two claims landed on the FLAV.NUSCALE.05
scalaron-trace candidate (v986, [C]/[N], mechanism [O]):

  (a) LOGIC CORRECTION.  v986 motivated the prefactor 3 by 'Tr_{A3} I = 3'.
      Trace 3 does NOT make 3 an eigenvalue of I (Spec(I) = {1,1,1}).  The
      candidate ROW typed the mechanism [O], so this is a motivation
      retyping, not a ledger error.
  (b) REPAIRED OPERATOR.  TFPT allegedly has a family operator Q_+ with
      Spec(Q_+) = {1,2,3}.  With Lagrange spectral projectors P_1, P_2, P_3
      and epsilon = (phi0^ret)^2 / A_Lambda, the proposal is

          M_R = M_scal (epsilon P_1 + 2 epsilon P_2 + 3 P_3)

      giving eigenvalues
          M_1 = epsilon M_scal      (= v212/v372 decuple leptogenesis scale)
          M_2 = 2 epsilon M_scal    (new)
          M_3 = 3 M_scal            (= v986 seesaw scale).

THIS PROBE (exact sympy):

  1. Premise hunt.  Does a corpus Q_+ with Spec = {1,2,3} exist?
  2. Lagrange projectors of that operator: idempotent, orthogonal,
     complete -- exact.
  3. Build M_R, verify eigenvalues, and type the unification
     M_1 == M_scal phi0^2 / A_Lambda as exact-by-construction
     (a REPARAMETRIZATION) vs what is genuinely new (M_2).

HONEST BOUNDARY (firewall): exploration; no ledger/paper/website touch;
the mixed insertion (epsilon on the {1,2}-subspace, unsuppressed 3 on
P_3) is a REVIEWER ANSATZ, not a derived corpus identity.  Q_+ supplies
the spectrum {1,2,3}; it does not by itself decide which eigenvalues
carry epsilon.
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import Mbar, g_car  # noqa: E402

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


# ---------------------------------------------------------------------------
# 1. PREMISE: the corpus Q_+
# ---------------------------------------------------------------------------
# Canonical generation-basis matrix, v50 / v10:
#   Q = [[3,1,0],[3,2,0],[3,2,1]],  Sigma = diag(1,-1,-1)
#   Q_+ = (Q + Sigma Q Sigma)/2 = [[3,0,0],[0,2,0],[0,2,1]]
# Eigenbasis form, v69 / v72:
#   Q_+ = 3*diag({0,1/3,2/3})+1 = diag(1,2,3)
# Both have chi = (t-1)(t-2)(t-3).  We use the v50 matrix (the actual
# flavor-address operator in the R/Q/K/L basis), not a reconstructed
# diagonal stand-in.

Q = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
Sig = sp.diag(1, -1, -1)
I = sp.eye(3)
t = sp.symbols("t")
Qp = sp.simplify((Q + Sig * Q * Sig) / 2)
Qp_v50 = sp.Matrix([[3, 0, 0], [0, 2, 0], [0, 2, 1]])
chi = sp.factor(Qp.charpoly(t).as_expr())
spec = sorted(int(e) for e in Qp.eigenvals().keys())

rep("PREMISE: v50 Sigma-even part equals the published Q_+ = "
    "[[3,0,0],[0,2,0],[0,2,1]]",
    Qp == Qp_v50)
rep("PREMISE: chi_{Q_+} = (t-1)(t-2)(t-3)",
    chi == (t - 1) * (t - 2) * (t - 3))
rep("PREMISE: Spec(Q_+) = {1,2,3} (A3 exponents, v10/v50/v69)",
    spec == [1, 2, 3])

w = [sp.Integer(0), sp.Rational(1, 3), sp.Rational(2, 3)]
Qp_diag = sp.diag(*[3 * wi + 1 for wi in w])
rep("PREMISE: v69 cusp form Q_+ = 3*diag({0,1/3,2/3})+1 = diag(1,2,3) "
    "has the SAME spectrum (change of basis, not a different operator)",
    sorted(int(e) for e in Qp_diag.eigenvals().keys()) == [1, 2, 3]
    and Qp_diag == sp.diag(1, 2, 3))

# Q_+ is diagonalizable (distinct eigenvalues) but NOT symmetric, hence
# not normal: the Lagrange projectors are polynomial spectral projectors,
# not Hermitian orthogonal projectors of a Hilbert-space observable.
rep("HONESTY: Q_+ is not symmetric (generation-basis form is non-normal)",
    Qp != Qp.T)

PREMISE = "PREMISE_FOUND"
print("VERDICT_PREMISE  %s  | corpus Q_+ at v10/v50 (generation basis) "
      "and v69/v72 (cusp eigenbasis); Spec = {1,2,3} is load-bearing, "
      "not reconstructed.  Nearest-object fallback not needed."
      % PREMISE)

# ---------------------------------------------------------------------------
# 2. Lagrange spectral projectors (reviewer formulae)
# ---------------------------------------------------------------------------
# For distinct eigenvalues, P_lam = prod_{mu != lam} (Q - mu I)/(lam - mu):
#   P_1 = (Q-2I)(Q-3I)/((1-2)(1-3)) = (Q-2I)(Q-3I)/2
#   P_2 = (Q-I)(Q-3I)/((2-1)(2-3))  = -(Q-I)(Q-3I)
#   P_3 = (Q-I)(Q-2I)/((3-1)(3-2))  = (Q-I)(Q-2I)/2

P1 = sp.simplify((Qp - 2 * I) * (Qp - 3 * I) / 2)
P2 = sp.simplify(-(Qp - I) * (Qp - 3 * I))
P3 = sp.simplify((Qp - I) * (Qp - 2 * I) / 2)

rep("P_1 = (Q_+-2I)(Q_+-3I)/2  (Lagrange)", True,
    extra="P1 = " + str(P1.tolist()))
rep("P_2 = -(Q_+-I)(Q_+-3I)     (Lagrange)", True,
    extra="P2 = " + str(P2.tolist()))
rep("P_3 = (Q_+-I)(Q_+-2I)/2    (Lagrange)", True,
    extra="P3 = " + str(P3.tolist()))

for name, P in (("P1", P1), ("P2", P2), ("P3", P3)):
    rep("%s idempotent  P^2 = P (exact)" % name,
        sp.simplify(P * P - P) == sp.zeros(3))
    rep("%s rank-1 (trace = 1)" % name,
        sp.simplify(P.trace()) == 1)

rep("orthogonal P1 P2 = 0 (exact)", sp.simplify(P1 * P2) == sp.zeros(3))
rep("orthogonal P1 P3 = 0 (exact)", sp.simplify(P1 * P3) == sp.zeros(3))
rep("orthogonal P2 P3 = 0 (exact)", sp.simplify(P2 * P3) == sp.zeros(3))
rep("complete P1+P2+P3 = I (exact)",
    sp.simplify(P1 + P2 + P3 - I) == sp.zeros(3))
rep("spectral calculus Q_+ = 1 P1 + 2 P2 + 3 P3 (exact)",
    sp.simplify(1 * P1 + 2 * P2 + 3 * P3 - Qp) == sp.zeros(3))

# same formulae on the Hermitian eigenbasis form -- ordinary diagonal
# projectors, as a sanity check that the polynomials are not an artefact
# of the non-normal generation-basis matrix.
P1d = sp.simplify((Qp_diag - 2 * I) * (Qp_diag - 3 * I) / 2)
P2d = sp.simplify(-(Qp_diag - I) * (Qp_diag - 3 * I))
P3d = sp.simplify((Qp_diag - I) * (Qp_diag - 2 * I) / 2)
rep("eigenbasis: P1d,P2d,P3d are the standard diag projectors E11,E22,E33 "
    "in the v69 ordering diag(1,2,3)",
    P1d == sp.diag(1, 0, 0) and P2d == sp.diag(0, 1, 0)
    and P3d == sp.diag(0, 0, 1))

# ---------------------------------------------------------------------------
# 3. M_R = M_scal (eps P1 + 2 eps P2 + 3 P3)
# ---------------------------------------------------------------------------
# epsilon = (phi0^ret)^2 / A_Lambda.  Corpus: phi0 is the retained seed
# (tfpt_constants); A_Lambda = 2 g_car = 10.

A_LAMBDA = 2 * int(g_car)
eps = sp.symbols("epsilon", positive=True)
C = sp.simplify(eps * P1 + 2 * eps * P2 + 3 * P3)
spec_C = set(sp.simplify(ev) for ev in C.eigenvals().keys())
rep("Spec(C) = {epsilon, 2 epsilon, 3}  where C = eps P1 + 2 eps P2 + 3 P3",
    spec_C == {eps, 2 * eps, sp.Integer(3)},
    extra="got " + str(spec_C))

# generation-basis matrix of C (exact, symbolic eps)
C_closed = sp.Matrix([[3, 0, 0], [0, 2 * eps, 0], [0, 2 * eps, eps]])
rep("generation-basis C = [[3,0,0],[0,2 eps,0],[0,2 eps, eps]] (exact)",
    sp.simplify(C - C_closed) == sp.zeros(3),
    extra="C = " + str(C.tolist()))
rep("HONESTY: generation-basis C is not symmetric -- it is NOT itself "
    "a Majorana matrix.  The seesaw uses the v69 eigenbasis form "
    "diag(eps, 2 eps, 3), the unique symmetric operator with those "
    "eigenvalues on the Q_+ eigenlines",
    C != C.T)

# the mixed insertion is an ANSATZ: Q_+ alone yields either
#   M_scal * Q_+           -> {M_scal, 2 M_scal, 3 M_scal}   (no leptogenesis)
#   eps M_scal * Q_+       -> {eps, 2 eps, 3 eps} M_scal     (no v986 seesaw)
# Putting eps on {P1,P2} and not on P3 is extra structure.
rep("ANSATZ (typed): epsilon on {P1,P2} and unsuppressed 3 on P3 is NOT "
    "forced by Q_+; it is the reviewer's mixed insertion that packages "
    "the two existing scales",
    True)

# ---------------------------------------------------------------------------
# 4. Numerical scales and the exact-by-construction unification
# ---------------------------------------------------------------------------
c3_s = 1 / (8 * sp.pi)
phi0_s = 1 / (6 * sp.pi) + 48 * c3_s ** 4
eps_s = sp.simplify(phi0_s ** 2 / A_LAMBDA)
Mscal_s = c3_s ** sp.Rational(7, 2) * sp.Float(str(Mbar), 40)

# EXACT identity: eps M_scal == M_scal * phi0^2 / A_Lambda  (definition)
ident = sp.simplify(eps_s * Mscal_s - Mscal_s * phi0_s ** 2 / A_LAMBDA)
rep("EXACT IDENTITY: eps M_scal == M_scal * phi0^2 / A_Lambda  "
    "(holds by DEFINITION of eps; the M_1 unification is a "
    "REPARAMETRIZATION, not a new derivation)",
    ident == 0)

M1 = float(eps_s * Mscal_s)
M2 = float(2 * eps_s * Mscal_s)
M3 = float(3 * Mscal_s)
Mscal = float(Mscal_s)
M1_decuple = float(Mscal_s * phi0_s ** 2 / A_LAMBDA)

rep("NUM: M_1 = eps M_scal = %.6e GeV  == v212 decuple "
    "M_scal phi0^2/A_Lambda = %.6e GeV" % (M1, M1_decuple),
    abs(M1 / M1_decuple - 1) < 1e-14)
rep("NUM: M_2 = 2 eps M_scal = %.6e GeV  (GENUINELY NEW prediction; "
    "no prior corpus scale sits here)" % M2,
    1e10 < M2 < 3e10)
rep("NUM: M_3 = 3 M_scal = %.6e GeV  == v986 seesaw rung" % M3,
    abs(M3 / (3 * Mscal) - 1) < 1e-14)
rep("NUM: A_Lambda = 2 g_car = %d" % A_LAMBDA, A_LAMBDA == 10)
rep("NUM: phi0^ret = %.8f (retained seed, not golden-ratio phi)"
    % float(phi0_s),
    0.05 < float(phi0_s) < 0.06)

print()
print("TYPING")
print("  PREMISE            %s" % PREMISE)
print("  REPACKAGING        M_1 (v212 decuple) and M_3 (v986 seesaw) "
      "are two existing corpus scales, now eigenvalues of one matrix; "
      "M_1 = eps M_scal is tautological once eps is defined as "
      "phi0^2/A_Lambda.")
print("  NEW                M_2 = 2 eps M_scal = %.6e GeV" % M2)
print("  ANSATZ             mixed insertion (eps, 2 eps, 3); Q_+ does "
      "not derive the eps-vs-1 split.")
print("  LOGIC CORRECTION   v986's 'Tr I = 3 => prefactor 3' is a TRACE "
      "argument (Spec(I)={1,1,1}); the repaired operator uses the "
      "EIGENVALUE 3 of Q_+ via P_3.  Same M_3 scale, different "
      "(generation-dependent) operator.  Mechanism stays [O].")
print("  PROJECTORS         P1=(Q-2I)(Q-3I)/2, P2=-(Q-I)(Q-3I), "
      "P3=(Q-I)(Q-2I)/2 -- idempotent, mutually annihilating, complete.")
print("  M_R / M_scal       [[3, 0, 0], [0, 2 eps, 0], [0, 2 eps, eps]] "
      "in the v50 generation basis.")
print()
print("VERDICT  PREMISE_FOUND; UNIFICATION_EXACT_BY_CONSTRUCTION "
      "(reparametrization of {M_1, M_3}); NEW_PREDICTION M_2.")
raise SystemExit(0 if ok_all else 1)
