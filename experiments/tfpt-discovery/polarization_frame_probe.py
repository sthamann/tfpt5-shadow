#!/usr/bin/env python3
"""The polarization frame round: J diagonalizes exactly in the rotation
eigenbasis, and the positive (Hodge) direction is the zeta_12 eigenspace.

Round 15 of the QGEO cover program (after v611).  The period dictionary
(v611) says period rows are rotation eigenvectors; this module lands the
form-level bridge:

  (B1) THE ROTATION SPECTRUM [E]: the braid rotation r has three SIMPLE
       eigenvalues, e^{i pi/6}, e^{-i pi/3}, e^{-i 5pi/6} -- i.e.
       zeta_12 x {1, -i, -1}: the twelfth roots organize the spectrum;
       det r = -1 exactly.

  (B2) J DIAGONALIZES IN THE ROTATION FRAME [E]: in the left-eigenvector
       basis W of r, the polarization becomes EXACTLY diagonal:
       (W^dagger)^-1 J W^-1 = diag(-1, (1-sqrt3)/2, (1+sqrt3)/2) (for
       the canonical sympy normalization of W).  Honest typing: the
       diagonality itself is the standard consequence of r being
       J-unitary with simple unimodular eigenvalues (eigenspaces to
       lambda != mu are J-orthogonal); the CONTENT is the exact values
       and the signature distribution.

  (B3) THE HODGE DIRECTION IS THE ZETA_12 EIGENSPACE [E]: the unique
       POSITIVE direction of J (signature (1,2), v597/v599) is exactly
       the eigenspace of the PRIMITIVE twelfth root e^{i pi/6} = zeta_12
       -- the h^{1,0} = 1 Hodge line of the omega-sheet sits on the
       zeta_12 eigenvector of the rotation: the analytic Hodge structure
       and the finite rotation agree on where "positivity" lives.

  (B4) CONSISTENCY [E]: r is J-unitary (r^dagger J r = J, the v597
       invariance, re-verified) and the three diagonal values multiply
       to det((W^dag)^-1 J W^-1) = det J / |det W|^2 consistently.

  (B5) THE READING [C]: with v611 (periods = Beta values on the zeta_12
       grid) and this round (the Hodge direction = the zeta_12
       eigenspace), the remaining step of the analytic bridge is the
       canonical PERIOD NORMALIZATION of the eigenvectors (fixing the
       diagonal weights as explicit Beta monomials) -- named, not
       claimed.

All checks exact (sympy).  Verdict enums (frozen): POLARIZATION-FRAMED
(all), POLARIZATION-FRAME-FAILS, MIXED.

FIREWALL: GATE.QGEO does not move; no marker changes.

PROVENANCE: discovery probe polarization_frame_probe.py (2026-08-01).
Python-only, counted per GATE.WOLFRAM.02.
"""

import sympy as sp

t = sp.symbols("t")
OMEGA = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""))


def burau_gen(i, n=4):
    m = n - 1
    M = sp.eye(m)
    if i - 2 >= 0:
        M[i - 2, i - 1] = t
    M[i - 1, i - 1] = -t
    if i < m:
        M[i, i - 1] = 1
    return M


I3 = sp.eye(3)
S = [sp.simplify(burau_gen(i).subs({t: OMEGA})) for i in (1, 2, 3)]
r = sp.simplify(S[0] * S[1] * S[2])
J = sp.Matrix([[0, 1 + sp.sqrt(3) * sp.I, -1 + sp.sqrt(3) * sp.I],
               [1 - sp.sqrt(3) * sp.I, 2, 1 + sp.sqrt(3) * sp.I],
               [-1 - sp.sqrt(3) * sp.I, 1 - sp.sqrt(3) * sp.I, 0]])

# ---------------------------------------------------------------- B1
print("=" * 72)
print("B1: the rotation spectrum on the zeta_12 circle")
print("=" * 72)

evs = (r.T).eigenvects()
eigs = []
W_rows = []
for ev, mult, vecs in evs:
    eigs.append(sp.simplify(ev))
    for v_ in vecs:
        W_rows.append(list(sp.simplify(v_.T)))
W = sp.Matrix(W_rows)
z12 = sp.exp(sp.I * sp.pi / 6)
targets = {sp.simplify(z12), sp.simplify(-z12), sp.simplify(-sp.I * z12)}
check("B1.1 three SIMPLE eigenvalues = zeta_12 x {1, -1, -i} "
      "(e^{i pi/6}, e^{-i 5pi/6}, e^{-i pi/3})",
      len(eigs) == 3 and {sp.simplify(sp.expand_complex(e)) for e in eigs}
      == {sp.simplify(sp.expand_complex(x_)) for x_ in targets})
check("B1.2 det r = -1 exactly", sp.simplify(r.det() + 1) == 0)
check("B1.3 the left-eigenvector matrix W is invertible", sp.simplify(W.det()) != 0)

# ---------------------------------------------------------------- B2
print("=" * 72)
print("B2: J diagonalizes exactly in the rotation frame")
print("=" * 72)

Wi = W.inv()
D = sp.expand(sp.simplify(Wi.conjugate().T * J * Wi))
offdiag = all(sp.simplify(D[i, j]) == 0 for i in range(3) for j in range(3) if i != j)
check("B2.1 (W^dag)^-1 J W^-1 is EXACTLY diagonal", offdiag)
dvals = {sp.simplify(sp.expand_complex(eigs[i])): sp.simplify(D[i, i]) for i in range(3)}
expected = {sp.simplify(sp.expand_complex(z12)): sp.Rational(1, 2) + sp.sqrt(3) / 2,
            sp.simplify(sp.expand_complex(-z12)): sp.Rational(1, 2) - sp.sqrt(3) / 2,
            sp.simplify(sp.expand_complex(-sp.I * z12)): sp.Integer(-1)}
ok_vals = all(sp.simplify(dvals[k] - vv) == 0 for k, vv in expected.items())
check("B2.2 diagonal values: d(zeta_12) = (1+sqrt3)/2, d(-zeta_12) = (1-sqrt3)/2, "
      "d(-i zeta_12) = -1 (canonical W normalization)", ok_vals,
      str({str(k): sp.nsimplify(v) for k, v in dvals.items()}))

# ---------------------------------------------------------------- B3
print("=" * 72)
print("B3: the Hodge direction is the zeta_12 eigenspace")
print("=" * 72)

signs = {k: sp.sign(sp.re(v)) for k, v in dvals.items()}
pos_eigs = [k for k, s_ in signs.items() if s_ == 1]
check("B3.1 the signature in the rotation frame is (1,2), and the UNIQUE positive "
      "direction is the PRIMITIVE zeta_12 eigenspace (e^{i pi/6})",
      len(pos_eigs) == 1 and sp.simplify(pos_eigs[0]
      - sp.simplify(sp.expand_complex(z12))) == 0)

# ---------------------------------------------------------------- B4
print("=" * 72)
print("B4: consistency")
print("=" * 72)

check("B4.1 r is J-unitary: r^dagger J r = J exactly (the v597 invariance)",
      sp.simplify(sp.expand(r.conjugate().T * J * r - J)) == sp.zeros(3, 3))
lhs = sp.simplify(D[0, 0] * D[1, 1] * D[2, 2])
rhs = sp.simplify(J.det() / (W.det() * sp.conjugate(W.det())))
check("B4.2 product of diagonal values = det J / |det W|^2 exactly",
      sp.simplify(sp.expand_complex(lhs - rhs)) == 0,
      "product = %s" % sp.nsimplify(lhs))

# ---------------------------------------------------------------- B5
print("=" * 72)
print("B5: the reading")
print("=" * 72)

check("B5.1 [C] the analytic bridge is one step from closing: periods are Beta "
      "values on the zeta_12 grid (v611), the Hodge direction is the zeta_12 "
      "eigenspace (B3); the canonical period normalization of the eigenvectors "
      "(diagonal weights as explicit Beta monomials) is the named next step", True)

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: POLARIZATION-FRAMED -- J diagonalizes exactly in the rotation")
    print("eigenbasis with signature (1,2), and the unique positive (Hodge)")
    print("direction is the primitive zeta_12 eigenspace.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
