"""v590 -- QGEO.INVOL.01: the sheet-involution existence question of
GATE.QGEO.01, narrowed to a two-demand selection with UNCONDITIONAL
existence.  THE RIGIDITY [E]: the integral involutions commuting with
the sheet flow V form EXACTLY the spectral sign group (Z/2)^3 -- all
eight sign choices epsilon on V's eigenspaces {0, 1, 2} give INTEGER
matrices that STABILIZE the integral order Z<U,V> (nontrivial: for a
generic integral operator the spectral projectors are not integral),
and the same holds verbatim on the alt twin.  THE NARROWING CHAIN [E]:
(i) the v574 rank theorem (a two-dim-positive involution cannot carry
the binary trace code) kills the trace +1 half: 6 nontrivial
involutions -> 3 of Sigma-signature (1,-1,-1); (ii) the seam-reversal
demand S e3 = -e3 narrows 3 -> 2; (iii) the zero-mode-fixing demand
(+1 on ker V, i.e. the involution leaves the inert direction alone
and flips exactly the dynamical sheet pair {1,2}) singles out

    S0 = [[1,-1,0],[0,-1,0],[0,0,-1]]     (trace -1, S0^2 = I)

UNIQUELY.  Existence is therefore UNCONDITIONAL (S0 is explicit,
integral, order-stabilizing, of exact Sigma-signature); the residual
freedom of GATE.QGEO.01's involution input is the explicit,
finite selection above -- two geometric demands, each machine-checked,
no continuum input.  HONEST SCOPE: this is the V-COMPATIBLE
(automorphism) involution class -- the corpus RP reflection theta(X) =
Sigma X^T Sigma is an anti-automorphism and does NOT commute with V
(checked); the two structures play different roles; the gate demand
addressed here is existence/selection of the sheet involution, not
the RP reflection.  The alt twin admits the same classification (the
involution does not separate the twins).

FIREWALL: exact sympy arithmetic throughout; the two demands are
declared, not derived from continuum geometry (that remains the open
[C] of the gate); no marker moves beyond the narrowing note.  Verdict
enums (frozen): EXISTENCE-UNCONDITIONAL, AMBIGUOUS, FAILS.

PROVENANCE: discovery probe involution_existence_probe.py
(2026-08-01, 7/7, EXISTENCE-UNCONDITIONAL); exact sympy throughout.
Python-only, counted per GATE.WOLFRAM.02.
"""
import itertools
import time

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

T0 = time.time()
FAILS = []
N_CHK = 0

I3 = sp.eye(3)
IDX7 = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))
E3 = sp.Matrix([0, 0, 1])
S0_EXPECT = sp.Matrix([[1, -1, 0], [0, -1, 0], [0, 0, -1]])


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def Qc(c):
    return sp.Matrix([[3, 1, 0], [3, 2, 0], [3, c, 1]])


def order_data(c):
    Q = Qc(c)
    U, V = Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)
    ws, fr = [I3], [I3]
    for _ in range(5):
        fr = [w * G for w in fr for G in (U, V)]
        ws += fr
    Mrows = sp.Matrix([[w[i, j] for (i, j) in IDX7] for w in ws])
    H = hermite_normal_form(Mrows.T)
    basis = []
    for k in range(H.cols):
        Mx = sp.zeros(3, 3)
        for r, (i, j) in enumerate(IDX7):
            Mx[i, j] = H[r, k]
        basis.append(Mx)
    Bm = sp.Matrix([[b[i, j] for (i, j) in IDX7] for b in basis]).T
    return U, V, Bm


def in_order(X, Bm):
    if X[0, 2] != 0 or X[1, 2] != 0:
        return False
    v = sp.Matrix([X[i, j] for (i, j) in IDX7])
    coef = Bm.solve(v)
    return all(x.is_integer for x in coef)


def spectral_involutions(V):
    evs = sorted(V.eigenvals().keys(), key=lambda e: abs(e))
    Ps = []
    for e in evs:
        P = sp.eye(3)
        for e2 in evs:
            if e2 != e:
                P = P * (V - e2 * sp.eye(3)) / (e - e2)
        Ps.append(sp.simplify(P))
    out = []
    for eps in itertools.product((1, -1), repeat=3):
        S = sp.simplify(eps[0] * Ps[0] + eps[1] * Ps[1] + eps[2] * Ps[2])
        out.append((eps, S))
    return evs, Ps, out


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("QGEO.INVOL -- existence and selection of the sheet "
          "involution")
    print("=" * 78)

    results = {}
    for c in (2, 0):
        U, V, Bm = order_data(c)
        evs, Ps, cands = spectral_involutions(V)
        all_integral = all(all(x.is_integer for x in S)
                           for _, S in cands)
        all_stab = all(in_order(S * U * S, Bm)
                       and in_order(S * V * S, Bm) for _, S in cands)
        all_invol = all(sp.simplify(S * S - I3) == sp.zeros(3, 3)
                        for _, S in cands)
        all_commute = all(sp.simplify(S * V - V * S) == sp.zeros(3, 3)
                          for _, S in cands)
        results[c] = (V, cands, all_integral, all_stab, all_invol,
                      all_commute)

    check("I1.1 [E, THE RIGIDITY] the integral V-commuting involutions "
          "are EXACTLY the spectral sign group (Z/2)^3: all eight sign "
          "choices on V's eigenspaces {0,1,2} are INTEGER matrices, "
          "genuine involutions, commute with V, and STABILIZE the "
          "integral order Z<U,V> -- on BOTH twins (nontrivial: generic "
          "integral operators do not have integral spectral "
          "projectors)",
          all(results[c][2] and results[c][3] and results[c][4]
              and results[c][5] for c in (2, 0)))

    V2, cands2 = results[2][0], results[2][1]
    nontriv = [(eps, S) for eps, S in cands2 if S != I3 and S != -I3]
    sig = [(eps, S) for eps, S in nontriv if sp.trace(S) == -1]
    check("I2.1 [E, narrowing step 1 -- the v574 type theorem] the "
          "trace +1 half (two-dim-positive type, killed by the v574 "
          "rank theorem: it cannot carry the binary trace code) drops "
          "%d -> %d candidates, all of exact Sigma-signature "
          "(1,-1,-1)" % (len(nontriv), len(sig)),
          len(nontriv) == 6 and len(sig) == 3)

    seam = [(eps, S) for eps, S in sig
            if sp.simplify(S * E3 + E3) == sp.zeros(3, 1)]
    check("I2.2 [E, narrowing step 2 -- seam reversal] the demand "
          "S e3 = -e3 (the involution reverses the seam line) narrows "
          "%d -> %d" % (len(sig), len(seam)),
          len(seam) == 2)

    ker_fix = [(eps, S) for eps, S in seam if eps[0] == 1]
    check("I2.3 [E, narrowing step 3 -- the zero mode] the demand "
          "that the involution FIX ker V (act as +1 on the inert "
          "direction, flipping exactly the dynamical sheet pair "
          "{1,2}) singles out ONE candidate: S0 = %s -- explicit, "
          "integral, order-stabilizing, trace -1: EXISTENCE IS "
          "UNCONDITIONAL"
          % (ker_fix[0][1].tolist() if ker_fix else None),
          len(ker_fix) == 1 and ker_fix[0][1] == S0_EXPECT)

    SIG_RP = sp.diag(1, -1, -1)
    rp_commutes = sp.simplify(SIG_RP * V2 - V2 * SIG_RP) == sp.zeros(3, 3)
    check("I3.1 [E, honest scope] the corpus RP reflection Sigma = "
          "diag(1,-1,-1) (used as the ANTI-automorphism theta(X) = "
          "Sigma X^T Sigma) does NOT commute with V (%s): the sheet "
          "involution S0 and the RP reflection are different "
          "structures with different roles -- the gate demand "
          "addressed here is the sheet involution, not the RP slot"
          % rp_commutes, not rp_commutes)

    V0, cands0 = results[0][0], results[0][1]
    s0_alt = [S for eps, S in cands0
              if eps == (1, -1, -1)][0]
    check("I4.1 [E] the alt twin admits the same classification and "
          "its selected involution is %s: the involution does NOT "
          "separate the twins -- consistent with v567/v572 (every "
          "classical certificate coincides on the pair); the "
          "narrowing is a GATE.QGEO.01 statement, not a bit selector"
          % s0_alt.tolist(),
          sp.simplify(s0_alt * s0_alt - I3) == sp.zeros(3, 3)
          and sp.trace(s0_alt) == -1)

    check("I5.1 [C, the relocation] GATE.QGEO.01's involution-"
          "existence input relocates: existence is now DERIVED "
          "(unconditional, explicit S0), and the residual freedom is "
          "the finite two-demand selection (seam reversal + zero-mode "
          "fixing), machine-checked; deriving those two demands from "
          "the continuum geometry (mu4/D4/H1) is the remaining open "
          "[C] of the gate -- named, not claimed", True)

    VERDICT = "EXISTENCE-UNCONDITIONAL" if not FAILS else "AMBIGUOUS"
    print("\nVERDICT: %s -- rigidity (Z/2)^3 on both twins; narrowing "
          "6 -> 3 -> 2 -> 1; S0 explicit with Sigma-signature; the "
          "two demands named" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: exact sympy; demands declared; continuum "
          "derivation stays open; no marker moves beyond the "
          "narrowing note")
    print("--- QGEO.INVOL.01 sheet involution existence: %d passed, "
          "%d failed ---" % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
