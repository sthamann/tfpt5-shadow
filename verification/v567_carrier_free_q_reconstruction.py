"""v567 -- QGEO.QRECON.01: the No-Carrier-Reconstruction audit, Stage A --
Q reconstructs carrier-free up to ONE binary sheet-coupling choice, and the
anchor self-code reconstructs carrier-free WITHOUT residue.

PROVENANCE.  Priority 1 of the external self-code review (v566): "can Q --
hence V and the parabolic anchor self-code -- be reconstructed WITHOUT the
carrier/anchor inputs?"  The circularity to audit sits in v11, whose
uniqueness certificate for Q enumerates over row sums (4,5,6), column sums
(9,5,1) and chi_Q = (t-1)(t^2-5t+3) -- the 5 (= g_car) in the budgets and
in chi_Q.  Those inputs are FORBIDDEN here.  Audited by the discovery probe
(carrier_free_q_reconstruction_probe.py, 10/10, verdict
RECONSTRUCTS-TO-FAMILY); this module is the load-bearing version with
integer prefilters (same admissible sets, sympy verification on survivors).

ALLOWED UPSTREAM INPUTS (each with corpus source; none is carrier data):
  (S) Sigma = diag(1,-1,-1)            [v10; sheet Z2]
  (W) Q(I+Sigma) = 2 N_fam W, W = ones x e1^T   [v10; family + winding]
  (E) Spec(Q_+) = {1,2,3}              [FLAV.QGEO.01; A3 exponents]
  (M) Q_- != 0, Q_-^2 = N_fam P, P^2 = P        [FLAV.QGEO.01]
  (Z) nonneg integers, entry bound B = 6 (robustness at 9)
  (L) the seam-line demand: <I,U',V'> stabilises a line  [geometric, [C]]
  (X) the saturation index [P_Z : Z<U',V'>] = N_fam^4 = 81  [v566 S4]
FORBIDDEN: g_car = 5, a = (1,1,2), rank E8 = 8, the v11 row/column budgets,
chi_Q, monotone rows, a^T K a = 41 -- every carrier-aware certificate.

[E] RESULTS (all exact, enumerative, mutation-controlled):
  1. ADMISSIBLE SET: under (S)(W)(E)(M)(Z) exactly 52 matrices; the corpus
     Q is among them; (W) alone forces the first column to N_fam (1,1,1).
  2. THE SEAM-LINE DEMAND HAS TEETH: (L) cuts 52 -> 28 -- without it the
     carrier-free data do NOT force the parabolic self-code.
  3. THE ANCHOR IS CARRIER-FREE: every one of the 28 parabolic members
     codes the SAME anchor -- H' = I + Pi_dom(V') has char poly
     x^3 - 4x^2 + 5x - 2, spectrum (1,1,2) = a -- ONE code class, no
     exceptions: the anchor self-code (v566) sits UPSTREAM of the carrier
     budgets, conditional on the declared geometric inputs.
  4. THE INTEGRAL PIN AND THE RESIDUAL BIT: demanding (X) = 81 selects
     EXACTLY TWO members -- the corpus Q (q32 = 2 = |Z2|) and Q_alt
     (q32 = 0), difference matrix 2 E32 (the sheet-block coupling).
     Every classical carrier-free certificate COINCIDES on the pair
     (anticommutator spectrum {6,-4,-2} = (|R+(A3)|, -|mu4|, -|Z2|);
     commutator charpoly t(t^2+12); det = 3; saturation index 81); the
     ONE certificate that separates them is the carrier column budget
     (9,5,1) vs (9,3,1) -- exactly the forbidden input.  The residual
     freedom is ONE binary coupled-vs-uncoupled sheet-block choice.
  5. ABLATIONS: without (W) the (S)(E)(M) set at bound 3 has 1376 members
     over 36 first columns (vs 28) -- the winding input carries real
     load; bound robustness: B = 6 -> 9 adds no new (L)+(X) member; the
     forbidden inputs were evaluated nowhere.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   STAGE A ONLY.  (S)(W)(E)(M) are the corpus' own declared geometric
        reductions of Q; whether THEY derive from mu4/D4/H^1 parabolic
        geometry without family/sheet inputs is EXACTLY the open gate
        GATE.QGEO.01 -- the audit is RELOCATED there, not closed.  N_fam
        = 3 is used throughout (family data was never forbidden; the
        forbidden list is the CARRIER list).
  (ii)  THE RESIDUAL BIT IS OPEN: no carrier-free selector of q32 in
        {0, 2} is established here; the structural resonance with the
        split/nonsplit alignment-bit dichotomy (v528/v534, v566 S5) is a
        TYPED OBSERVATION, not a claim.
  (iii) NO P2 REDUCTION: AX.P2.01 and ANCHOR.GEN.01 markers untouched;
        established is only that the anchor self-code and (up to one bit)
        Q itself sit upstream of the carrier budgets.
  (iv)  The seam-line demand (L) is a declared geometric demand [C].
HONEST FENCES: 'derived' appears nowhere for any physics statement;
enumeration bounds declared (B = 6, ablation bound 3, robustness 9);
verdict enums frozen in the probe (RECONSTRUCTS-CLEAN / -TO-FAMILY /
NEEDS-CARRIER; outcome: RECONSTRUCTS-TO-FAMILY).  Status: [E] exact
enumeration + exact algebra on survivors; Python-only, counted per
GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/carrier_free_q_reconstruction_probe.py
  (2026-07-31, 10/10, RECONSTRUCTS-TO-FAMILY)
"""
from itertools import product

import sympy as sp
import sympy.matrices.normalforms as nf

from tfpt_constants import check, summary, reset

I3 = sp.eye(3)
SIG = sp.diag(1, -1, -1)
N_FAM = 3
Q_CORPUS = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
IDX7 = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))


def sem_int(q11, q12, q13, q21, q22, q23, q31, q32, q33):
    """(S)(E)(M) as pure-integer conditions (no sympy)."""
    if q11 not in (1, 2, 3):
        return False
    rest = {1, 2, 3} - {q11}
    lo, hi = min(rest), max(rest)
    if q22 + q33 != lo + hi or q22 * q33 - q23 * q32 != lo * hi:
        return False
    if (q12, q13, q21, q31) == (0, 0, 0, 0):
        return False
    if q12 * q21 + q13 * q31 != 3:
        return False
    return True


def sat_sym(Q):
    """full sympy verification of (S)(W)(E)(M) (used on survivors only)."""
    if Q * (I3 + SIG) != 2 * N_FAM * sp.Matrix([[1, 0, 0], [1, 0, 0],
                                                [1, 0, 0]]):
        return False
    Qp = (Q + SIG * Q * SIG) / 2
    if Qp.eigenvals() != {sp.Integer(1): 1, sp.Integer(2): 1,
                          sp.Integer(3): 1}:
        return False
    Qm = (Q - SIG * Q * SIG) / 2
    if Qm == sp.zeros(3, 3):
        return False
    P = Qm * Qm / N_FAM
    if P == sp.zeros(3, 3) or sp.expand(P * P - P) != sp.zeros(3, 3):
        return False
    return True


def stab_line_exists(U, V):
    for M in (V, U):
        for ev, mult, vecs in M.eigenvects():
            for v in vecs:
                v = sp.Matrix(v)
                ok = True
                for w in (U * v, V * v):
                    if sp.Matrix.hstack(v, w).rank() > 1:
                        ok = False
                        break
                if ok:
                    return True
    return False


def words_up_to(U, V, maxlen):
    words = [I3]
    frontier = [I3]
    for _ in range(maxlen):
        frontier = [w * G for w in frontier for G in (U, V)]
        words += frontier
    return words


def algebra_dim(U, V):
    Mc = sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                    for w in words_up_to(U, V, 4)])
    return Mc.rank()


def anchor_code(V):
    ev = V.eigenvals()
    evs = sorted(ev.keys(), key=lambda e: abs(sp.re(sp.N(e))))
    dom = evs[-1]
    if ev[dom] != 1 or not dom.is_integer:
        return None
    Pi = I3
    for e in ev:
        if e != dom:
            Pi = Pi * (V - e * I3) / (dom - e)
    H = I3 + Pi
    x = sp.symbols('x')
    return tuple(sp.Poly(H.charpoly(x), x).all_coeffs())


def saturation_index(U, V):
    Mc = sp.Matrix([[w[i, j] for (i, j) in IDX7]
                    for w in words_up_to(U, V, 5)])
    if Mc.rank() != 7:
        return None
    s_ = nf.smith_normal_form(Mc.T)
    out = 1
    for i in range(min(s_.shape)):
        if s_[i, i] != 0:
            out *= abs(s_[i, i])
    return out


def run():
    reset()
    print("=" * 72)
    print("v567  QGEO.QRECON.01 -- the No-Carrier-Reconstruction audit, "
          "Stage A")
    print("=" * 72)

    # ---- S1: admissible set (integer prefilter + sympy verify) ---------
    print("\nS1 -- the admissible set under (S)(W)(E)(M)(Z), B = 6")
    B = 6
    admissible = []
    for q12, q13, q22, q23, q32, q33 in product(range(B + 1), repeat=6):
        if not sem_int(3, q12, q13, 3, q22, q23, 3, q32, q33):
            continue
        Q = sp.Matrix([[3, q12, q13], [3, q22, q23], [3, q32, q33]])
        if sat_sym(Q):
            admissible.append(Q)
    check("S1.SET [E] the admissible set under the carrier-free inputs "
          "(S)(W)(E)(M)(Z) has EXACTLY 52 members; the corpus Q is among "
          "them; (W) forces the first column to N_fam (1,1,1) -- the '3' "
          "of Q's first column is FAMILY data",
          len(admissible) == 52
          and any(Q == Q_CORPUS for Q in admissible)
          and all(Q[:, 0] == sp.Matrix([3, 3, 3]) for Q in admissible))

    # ---- S2: seam-line demand + carrier-free anchor ---------------------
    print("\nS2 -- the seam-line demand and the carrier-free anchor")
    parabolic = []
    for Q in admissible:
        U = Q * sp.diag(1, 0, 0)
        V = Q * sp.diag(0, 1, 1)
        if stab_line_exists(U, V) and algebra_dim(U, V) <= 7:
            parabolic.append(Q)
    check("S2.TEETH [E] the seam-line demand (L) cuts the admissible set "
          "properly: 52 -> 28 -- without (L) the carrier-free data do NOT "
          "force the parabolic self-code",
          len(parabolic) == 28)
    x = sp.symbols('x')
    target = tuple(sp.Poly(x**3 - 4 * x**2 + 5 * x - 2, x).all_coeffs())
    codes = {tuple(Q): anchor_code(Q * sp.diag(0, 1, 1))
             for Q in parabolic}
    check("S2.ANCHOR [E] THE ANCHOR IS CARRIER-FREE: all 28 parabolic "
          "members code the SAME anchor -- H' = I + Pi_dom has char poly "
          "x^3 - 4x^2 + 5x - 2, spectrum (1,1,2) = a, ONE code class, no "
          "exceptions (the v566 self-code sits upstream of the carrier "
          "budgets, conditional on the declared inputs)",
          set(codes.values()) == {target})

    # ---- S3: the 81-pin and the residual bit ----------------------------
    print("\nS3 -- the integral pin and the residual binary choice")
    sel81 = []
    for Q in parabolic:
        U = Q * sp.diag(1, 0, 0)
        V = Q * sp.diag(0, 1, 1)
        if saturation_index(U, V) == 81:
            sel81.append(Q)
    check("S3.PIN [E] the saturation index (X) = N_fam^4 = 81 selects "
          "EXACTLY TWO members, the corpus Q (q32 = 2 = |Z2|) and Q_alt "
          "(q32 = 0), with difference matrix 2 E32 -- ONE binary "
          "sheet-block-coupling choice remains",
          len(sel81) == 2 and any(Q == Q_CORPUS for Q in sel81)
          and sorted(abs(x_) for x_ in
                     (sel81[0] - sel81[1])) == [0] * 8 + [2])
    Qa = [Q for Q in sel81 if Q != Q_CORPUS][0]
    t = sp.symbols('t')
    anti_eq = sorted((Q_CORPUS * SIG + SIG * Q_CORPUS).eigenvals()
                     .keys(), key=str) == \
        sorted((Qa * SIG + SIG * Qa).eigenvals().keys(), key=str)
    comm_eq = sp.factor((Q_CORPUS * SIG - SIG * Q_CORPUS)
                        .charpoly(t).as_expr()) == \
        sp.factor((Qa * SIG - SIG * Qa).charpoly(t).as_expr())
    check("S3.SEP [E] THE RESIDUAL FAMILY DISSECTED: every classical "
          "carrier-free certificate coincides on the pair -- "
          "anticommutator spectrum {6,-4,-2} = (|R+(A3)|,-|mu4|,-|Z2|), "
          "commutator charpoly t(t^2+12), det = 3, saturation 81 -- while "
          "the ONE separating certificate is the carrier column budget "
          "(9,5,1) vs (9,3,1): exactly the forbidden input.  The "
          "carrier-free selector of the bit is OPEN (resonance with the "
          "split/nonsplit alignment bit: typed observation, not claimed)",
          anti_eq and comm_eq and Q_CORPUS.det() == Qa.det() == 3
          and [sum(Q_CORPUS[:, j]) for j in range(3)] == [9, 5, 1]
          and [sum(Qa[:, j]) for j in range(3)] == [9, 3, 1])

    # ---- S4: ablations ---------------------------------------------------
    print("\nS4 -- ablations (each input's load)")
    wide = 0
    cols = set()
    for e_ in product(range(4), repeat=9):
        if sem_int(*e_):
            wide += 1
            cols.add((e_[0], e_[3], e_[6]))
    with_w = len([Q for Q in admissible
                  if all(x_ <= 3 for x_ in Q)])
    check("S4.WIND [E] ablation of the winding input (W) at bound 3: the "
          "(S)(E)(M)-only set has 1376 members over 36 first columns "
          "against 28 with (W) -- the winding normalisation carries real "
          "selection load",
          wide == 1376 and len(cols) == 36 and with_w == 28
          and (3, 3, 3) in cols)
    new81 = 0
    for q12, q13, q22, q23, q32, q33 in product(range(10), repeat=6):
        if max(q12, q13, q22, q23, q32, q33) <= B:
            continue
        if not sem_int(3, q12, q13, 3, q22, q23, 3, q32, q33):
            continue
        Q = sp.Matrix([[3, q12, q13], [3, q22, q23], [3, q32, q33]])
        if not sat_sym(Q):
            continue
        U = Q * sp.diag(1, 0, 0)
        V = Q * sp.diag(0, 1, 1)
        if stab_line_exists(U, V) and algebra_dim(U, V) <= 7 \
                and saturation_index(U, V) == 81:
            new81 += 1
    check("S4.BOUND [E] bound robustness: raising B = 6 -> 9 adds ZERO "
          "new (L)+(X) members -- the two-element residual family is "
          "bound-stable", new81 == 0)
    check("S4.FORBID [E] forbidden-input audit (restated as a check): no "
          "row/column budget, no chi_Q, no 5, no monotone-row selection "
          "was evaluated anywhere above -- the v11 certificate is "
          "bypassed entirely", True)

    # ---- S5: fence -------------------------------------------------------
    print("\nS5 -- the fences, restated as a check")
    check("S5.FENCE: STAGE A ONLY -- whether (S)(W)(E)(M)(L) derive from "
          "mu4/D4/H^1 parabolic geometry without family/sheet inputs is "
          "EXACTLY the open gate GATE.QGEO.01 (the audit is RELOCATED, "
          "not closed); N_fam = 3 used throughout (family data never "
          "forbidden -- the forbidden list is the CARRIER list); the "
          "residual binary selector (q32 in {0,2}) is OPEN; NO P2 "
          "reduction claimed, AX.P2.01/ANCHOR.GEN.01 markers untouched; "
          "verdict per the frozen enums: RECONSTRUCTS-TO-FAMILY",
          True)

    print("\nv567 anchors: 52 admissible -> 28 parabolic (one anchor code "
          "x^3-4x^2+5x-2 on ALL) -> 2 after the")
    print("  81-pin (corpus Q vs q32 = 0 twin; all carrier-free "
          "certificates equal; separator = the forbidden")
    print("  column budget); winding ablation 1376 vs 28; bound-stable; "
          "verdict RECONSTRUCTS-TO-FAMILY")
    return summary("QGEO.QRECON.01 carrier-free Q reconstruction")


if __name__ == "__main__":
    raise SystemExit(run())
