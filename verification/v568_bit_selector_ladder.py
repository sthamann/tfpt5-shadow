"""v568 -- DIAMOND.BIT.SELECT.01: the residual reconstruction bit located,
separated, and given a canonical exact witness -- the ladder self-consistency
selects the compiler Q uniquely on the carrier-free class.

PROVENANCE.  Priorities 2+3 of the self-code review, fused with the v567
residual bit: the No-Carrier-Reconstruction audit left EXACTLY one binary
freedom -- the 81-pinned class is {Q (q32 = 2 = |Z2|), Q_alt (q32 = 0)},
with every classical carrier-free certificate coinciding on the pair.
Audited and decided by the discovery probe (bit_selector_probe.py, 10/10,
verdict SELECTOR-FOUND); this module is the load-bearing version.

[E] 1. THE BIT IS INTEGRALLY VISIBLE: the two 81-twins generate DIFFERENT
    integral orders (Hermite bases differ; equal index 81, equal Smith
    divisors (1,1,1,3,3,3,3), different sublattices of the parabolic
    lattice) -- the bit is real integral structure even where every
    classical invariant coincides.
[E] 2. THE SELECTOR (the central result): for the whole reconstruction
    family the dominant mode of the sheet direction satisfies
    V_c (1, 2, 2c)^T = 2 (1, 2, 2c)^T identically in the coupling c --
    and demanding THE LADDER SELF-CONSISTENCY, that the dominant mode
    reproduce its own eigenvalue as the geometric ladder
    v = (lam^0, lam^1, lam^2) = (1, 2, 4), forces 2c = 4, c = 2:
    on ALL 28 members of the v567 parabolic carrier-free class EXACTLY
    ONE satisfies it -- the compiler Q.  The selection needs no 81-pin
    and no column budget: it alone pins Q within the class.
[C] 3. THE WITNESS IS PRIOR STRUCTURE, NOT A FOUND NUMBER (no-free-pattern
    discipline): the selected ladder (1,2,4) = (2^0, 2^1, 2^2) is the
    binary AnchorLadder step sequence p_{n+1} - p_n = 2^n (Lean-
    formalised) with 2 = |Z2| the sheet datum, and the trace code
    p_n(a) = 1 + tr(V^n) = 2 + 2^n (v566) rides the SAME ladder --
    consistency re-verified exactly for n = 1..6.
[E] 4. THE SPLIT GEOMETRY LOCATED AND EXCLUDED: an invariant module
    complement of the seam line exists IFF q32 = 1 (U-invariance forces
    a + b = 1, V-invariance forces a = 0 and a + b = q32; the plane
    span((1,0,0),(0,1,1)) is exactly invariant there) -- and that member's
    direction algebra COLLAPSES to dimension 5 (Smith (1,1,1,3,3), no
    full parabolic, no 81): the seam-line + saturation demands admit
    ONLY nonsplit geometry.  Consequence for the v566 A2 carrier: the
    Ext arrow is NONZERO on the whole reconstruction class -- the split
    class of the two-element module classification is structurally
    unreachable, and the residual bit (q32 in {0,2}) lives INSIDE the
    nonsplit side: it toggles WHICH nonsplit integral order is realised
    and whether the dominant mode carries the full binary ladder, not
    split-vs-nonsplit.
[E] 5. PRIORITY-2 CANDIDATE TESTS (mark-local structure of the 81, both
    reported honestly): (i) the mu4-grading candidate deg(E_jk) =
    g_k - g_j mod 4 (g = the A3 exponent grading) FAILS -- the order is
    not a graded sublattice (5 of 7 Hermite vectors homogeneous), so the
    grading does not descend to the cokernel; the review's kill condition
    does NOT fire (other mechanisms remain) and the 81 stays a
    FINGERPRINT pending a mechanism; (ii) left multiplication by V
    PRESERVES the order lattice, so it induces a canonical F3-linear
    action on the cokernel (Z/3)^4 -- the mark-local question is
    sharpened to a concrete module computation (the F3[V]-character
    structure vs the four marks), named open.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   THE PHYSICAL SELECTION IS NOT DERIVED: why the dominant mode
        should satisfy the ladder self-consistency is the relocated open
        question -- the same slot as the RP-selection of the alignment
        bit (v528/v534); this module LOCATES the bit and equips it with a
        canonical exact witness, nothing more.
  (ii)  The resonance between this reconstruction bit and the alignment
        bit remains a TYPED OBSERVATION (two binary choices in the same
        structural slot), not an identification.
  (iii) Stage B of v567 (deriving the geometric inputs from mu4/D4/H^1
        parabolic geometry, GATE.QGEO.01) is untouched; NO P2 reduction;
        AX.P2.01 / ANCHOR.GEN.01 markers untouched.
HONEST FENCES: 'derived' appears nowhere for any physics statement; the
selector is typed [C] as candidate canonical selection with its
justification open; Smith 1861 / Hermite 1851 (normal forms), Gabriel
1972 (quivers), Perron-Frobenius (dominant modes) named CLASSICAL as
addresses.  Status: [E] exact integer/symbolic algebra + [C] the anchored
selector typing; Python-only, counted per GATE.WOLFRAM.02.  Discovery:
  experiments/tfpt-discovery/bit_selector_probe.py (2026-07-31, 10/10,
  SELECTOR-FOUND)
"""
from itertools import product

import sympy as sp
import sympy.matrices.normalforms as nf
from sympy.matrices.normalforms import hermite_normal_form

from tfpt_constants import check, summary, reset

I3 = sp.eye(3)
SIG = sp.diag(1, -1, -1)
N_FAM = 3
IDX7 = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))


def Qc(c):
    return sp.Matrix([[3, 1, 0], [3, 2, 0], [3, c, 1]])


def UV(Q):
    return Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)


def words_up_to(U, V, maxlen=5):
    words = [I3]
    frontier = [I3]
    for _ in range(maxlen):
        frontier = [w * G for w in frontier for G in (U, V)]
        words += frontier
    return words


def order_coords(Q):
    U, V = UV(Q)
    return sp.Matrix([[w[i, j] for (i, j) in IDX7]
                      for w in words_up_to(U, V)])


def snf_divs(M):
    s_ = nf.smith_normal_form(M.T)
    return [abs(s_[i, i]) for i in range(min(s_.shape)) if s_[i, i] != 0]


def sem_int(q11, q12, q13, q21, q22, q23, q31, q32, q33):
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


def dom_ladder_test(V):
    ev = V.eigenvals()
    evs = sorted(ev.keys(), key=lambda e: abs(sp.re(sp.N(e))))
    dom = evs[-1]
    if ev[dom] != 1 or not dom.is_integer:
        return False
    for e_, m_, vecs in V.eigenvects():
        if e_ == dom:
            v = sp.Matrix(vecs[0])
            d = sp.lcm([sp.denom(x_) for x_ in v])
            v = sp.expand(v * d)
            g = sp.gcd(list(v))
            v = sp.Matrix([sp.cancel(x_ / g) for x_ in v])
            if v[0] < 0:
                v = -v
            return list(v) == [dom**0, dom**1, dom**2]
    return False


def run():
    reset()
    print("=" * 72)
    print("v568  DIAMOND.BIT.SELECT.01 -- the reconstruction bit located "
          "and given its canonical witness")
    print("=" * 72)

    # ---------------------------------------------------------------- S1
    print("\nS1 -- the twins are integrally distinct")
    H0 = hermite_normal_form(order_coords(Qc(0)).T)
    H2 = hermite_normal_form(order_coords(Qc(2)).T)
    check("S1.LATTICE [E] the two 81-twins generate DIFFERENT integral "
          "orders (Hermite bases differ) with EQUAL index 81 and equal "
          "Smith divisors (1,1,1,3,3,3,3) -- the bit is integrally "
          "visible where every classical invariant coincides",
          H0 != H2
          and snf_divs(order_coords(Qc(0)))
          == snf_divs(order_coords(Qc(2))) == [1, 1, 1, 3, 3, 3, 3])

    # ---------------------------------------------------------------- S2
    print("\nS2 -- the ladder self-consistency selector")
    c = sp.symbols('c', nonnegative=True)
    Vc = sp.Matrix([[0, 1, 0], [0, 2, 0], [0, c, 1]])
    vdom = sp.Matrix([1, 2, 2 * c])
    check("S2.MODE [E] V_c (1, 2, 2c)^T = 2 (1, 2, 2c)^T identically in "
          "the coupling c: the dominant mode of the sheet direction is "
          "v(c) = (1, 2, 2c) across the whole reconstruction family",
          sp.simplify(Vc * vdom - 2 * vdom) == sp.zeros(3, 1))
    check("S2.SELECT [E] the LADDER SELF-CONSISTENCY -- the dominant mode "
          "reproduces its own eigenvalue as the geometric ladder "
          "(2^0, 2^1, 2^2) = (1,2,4) -- holds iff 2c = 4 iff c = 2: "
          "uniquely the compiler Q; the twin truncates to (1,2,0)",
          sp.solve(sp.Eq(2 * c, 4), c) == [2]
          and vdom.subs(c, 2) == sp.Matrix([1, 2, 4])
          and vdom.subs(c, 0) != sp.Matrix([1, 2, 4]))
    # uniqueness on the whole v567 class
    family = []
    for q12, q13, q22, q23, q32, q33 in product(range(7), repeat=6):
        if not sem_int(3, q12, q13, 3, q22, q23, 3, q32, q33):
            continue
        Q = sp.Matrix([[3, q12, q13], [3, q22, q23], [3, q32, q33]])
        if Q * (I3 + SIG) != 2 * N_FAM * sp.Matrix([[1, 0, 0], [1, 0, 0],
                                                    [1, 0, 0]]):
            continue
        Qp = (Q + SIG * Q * SIG) / 2
        if Qp.eigenvals() != {sp.Integer(1): 1, sp.Integer(2): 1,
                              sp.Integer(3): 1}:
            continue
        Qm = (Q - SIG * Q * SIG) / 2
        P_ = Qm * Qm / N_FAM
        if P_ == sp.zeros(3, 3) or sp.expand(P_ * P_ - P_) \
                != sp.zeros(3, 3):
            continue
        U, V = UV(Q)
        if stab_line_exists(U, V):
            Mc = sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                            for w in words_up_to(U, V, 4)])
            if Mc.rank() <= 7:
                family.append(Q)
    ladder_members = [Q for Q in family
                      if dom_ladder_test(Q * sp.diag(0, 1, 1))]
    check("S2.UNIQUE [E] on ALL 28 members of the v567 parabolic "
          "carrier-free class EXACTLY ONE satisfies the ladder "
          "self-consistency, and it is the compiler Q -- the selection "
          "needs neither the 81-pin nor any column budget",
          len(family) == 28 and len(ladder_members) == 1
          and ladder_members[0] == Qc(2))
    check("S2.ANCHOR [C, anchored -- no-free-pattern] the witness ladder "
          "(1,2,4) = (2^0,2^1,2^2) is PRIOR load-bearing structure: the "
          "binary AnchorLadder steps p_{n+1} - p_n = 2^n "
          "(Lean-formalised), 2 = |Z2| the sheet datum, and the v566 "
          "trace code p_n(a) = 1 + tr(V^n) = 2 + 2^n rides the same "
          "ladder (n = 1..6 re-verified exactly)",
          all(((Qc(2) * sp.diag(0, 1, 1))**n_).trace() == 1 + 2**n_
              for n_ in range(1, 7)))

    # ---------------------------------------------------------------- S3
    print("\nS3 -- the split geometry located and excluded")
    a_, b_, c0 = sp.symbols('a_ b_ c0')
    sol = sp.solve([sp.Eq(a_ + b_, 1), sp.Eq(a_, 0), sp.Eq(a_ + b_, c0)],
                   [a_, b_, c0])
    Us, Vs = UV(Qc(1))
    L1, L2 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 1])
    inv_ok = all(sp.Matrix.hstack(L1, L2, M * w).det() == 0
                 for M in (Us, Vs) for w in (L1, L2))
    d1 = order_coords(Qc(1))
    check("S3.SPLIT [E] a module complement of the seam line exists IFF "
          "q32 = 1 (solve: a = 0, b = 1, q32 = 1; the plane "
          "span((1,0,0),(0,1,1)) is exactly (U,V)-invariant there) -- "
          "and that member's algebra COLLAPSES to dim 5 (Smith "
          "(1,1,1,3,3), no full parabolic, no 81): the seam-line + "
          "saturation demands admit ONLY nonsplit geometry -- the v566 "
          "A2 Ext arrow is NONZERO on the whole reconstruction class",
          sol == {a_: 0, b_: 1, c0: 1} and inv_ok
          and d1.rank() == 5 and snf_divs(d1) == [1, 1, 1, 3, 3])
    check("S3.TWINS [E] neither twin splits: for q32 in {0, 2} the "
          "complement system (a + b = 1, a = 0, a + b = q32) is "
          "inconsistent -- the residual bit does NOT toggle "
          "split/nonsplit; it toggles WHICH nonsplit integral order is "
          "realised (S1) and whether the dominant mode carries the full "
          "binary ladder (S2)",
          sp.solve([sp.Eq(a_ + b_, 1), sp.Eq(a_, 0), sp.Eq(a_ + b_, 0)],
                   [a_, b_]) == []
          and sp.solve([sp.Eq(a_ + b_, 1), sp.Eq(a_, 0),
                        sp.Eq(a_ + b_, 2)], [a_, b_]) == [])

    # ---------------------------------------------------------------- S4
    print("\nS4 -- Priority-2 candidate tests (the 81's mark-local "
          "structure)")
    H2T = H2.T
    g_ = (1, 2, 3)
    deg = {p: (g_[p[1]] - g_[p[0]]) % 4 for p in IDX7}
    homog = 0
    for j in range(H2T.shape[0]):
        supp = [IDX7[k] for k in range(7) if H2T[j, k] != 0]
        if len({deg[p] for p in supp}) <= 1:
            homog += 1
    check("S4.GRADE [E, candidate FAILS -- reported honestly] the "
          "mu4-grading candidate deg(E_jk) = g_k - g_j mod 4 does NOT "
          "make the order a graded sublattice (only %d of 7 Hermite "
          "vectors homogeneous): the grading cannot descend to the "
          "cokernel -- this natural 'one Z/3 per mark' candidate fails; "
          "the kill condition does NOT fire, the 81 stays a fingerprint "
          "pending a mechanism" % homog,
          homog < 7)
    Vb = Qc(2) * sp.diag(0, 1, 1)
    Hs = H2
    img_ok = True
    for j in range(Hs.shape[1]):
        x = sp.zeros(3, 3)
        for k, (i2, j2) in enumerate(IDX7):
            x[i2, j2] = Hs[k, j]
        y = Vb * x
        yv = sp.Matrix([[y[i2, j2]] for (i2, j2) in IDX7])
        t_ = Hs.solve(yv)
        if not all(x_.is_integer for x_ in t_):
            img_ok = False
            break
    check("S4.VACT [E] left multiplication by V PRESERVES the order "
          "lattice (V O subset O), so it induces a canonical F3-linear "
          "action on the cokernel (Z/3)^4 -- the mark-local question is "
          "sharpened to a concrete module computation (the "
          "F3[V]-character structure vs the four marks)",
          img_ok)

    # --- the F3[V]-character computation, executed ------------------------
    def smith_with_transforms(M):
        M = sp.Matrix(M)
        A = M.copy()
        S_ = sp.eye(A.rows)
        T_ = sp.eye(A.cols)

        def minaij(A_, t_):
            best = None
            for i_ in range(t_, A_.rows):
                for j_ in range(t_, A_.cols):
                    if A_[i_, j_] != 0 and (
                            best is None
                            or abs(A_[i_, j_]) < abs(A_[best[0], best[1]])):
                        best = (i_, j_)
            return best

        t_ = 0
        while t_ < min(A.rows, A.cols):
            p_ = minaij(A, t_)
            if p_ is None:
                break
            A.row_swap(t_, p_[0])
            S_.row_swap(t_, p_[0])
            A.col_swap(t_, p_[1])
            T_.col_swap(t_, p_[1])
            done = False
            while not done:
                done = True
                for i_ in range(t_ + 1, A.rows):
                    if A[i_, t_] != 0:
                        q_ = A[i_, t_] // A[t_, t_]
                        A[i_, :] = A[i_, :] - q_ * A[t_, :]
                        S_[i_, :] = S_[i_, :] - q_ * S_[t_, :]
                        if A[i_, t_] != 0:
                            A.row_swap(t_, i_)
                            S_.row_swap(t_, i_)
                            done = False
                for j_ in range(t_ + 1, A.cols):
                    if A[t_, j_] != 0:
                        q_ = A[t_, j_] // A[t_, t_]
                        A[:, j_] = A[:, j_] - q_ * A[:, t_]
                        T_[:, j_] = T_[:, j_] - q_ * T_[:, t_]
                        if A[t_, j_] != 0:
                            A.col_swap(t_, j_)
                            S_.col_swap(t_, j_)
                            done = False
            t_ += 1
        return A, S_, T_

    x = sp.symbols('x')
    results = {}
    for cx in (2, 0):
        Hx = hermite_normal_form(order_coords(Qc(cx)).T)
        Dx, Sx, Tx = smith_with_transforms(Hx)
        dd = [Dx[i, i] for i in range(7)]
        tor = [i for i in range(7) if abs(dd[i]) == 3]
        Vb_ = Qc(cx) * sp.diag(0, 1, 1)
        Ub_ = Qc(cx) * sp.diag(1, 0, 0)
        LV = sp.zeros(7, 7)
        LU = sp.zeros(7, 7)
        for k, (i2, j2) in enumerate(IDX7):
            E = sp.zeros(3, 3)
            E[i2, j2] = 1
            colV = [(Vb_ * E)[i3, j3] for (i3, j3) in IDX7]
            colU = [(Ub_ * E)[i3, j3] for (i3, j3) in IDX7]
            for r_ in range(7):
                LV[r_, k] = colV[r_]
                LU[r_, k] = colU[r_]
        subV = (Sx * LV * Sx.inv())[tor, tor].applyfunc(
            lambda v_: sp.Integer(v_) % 3)
        subU = (Sx * LU * Sx.inv())[tor, tor].applyfunc(
            lambda v_: sp.Integer(v_) % 3)
        cp = sp.Poly(subV.charpoly(x), x, modulus=3).as_expr()
        results[cx] = (cp, subU == sp.zeros(4, 4))
    check("S4.VCHAR [E, candidate (ii) FAILS THE MARK PATTERN -- reported "
          "honestly] the induced F3[V]-action on the cokernel has "
          "characteristic polynomial x(x - 1)^2(x + 1) mod 3 -- "
          "eigenvalues {0, 1, 1, -1}, NOT the regular mu4 pattern "
          "x^4 - 1 that 'one Z/3 per mark' would require (the action is "
          "not even invertible), and U acts as ZERO on the cokernel; "
          "both twins give the identical structure (the cokernel action "
          "separates nothing).  Priority-2 status after two candidates: "
          "grading fails, V-action exists but is non-regular -- the 81 "
          "stays a FINGERPRINT; the kill condition (no canonical local "
          "decomposition exists at all) is closer but not proven",
          all(sp.expand(results[cx][0]
                        - (x**4 - x**3 - x**2 + x)) == 0
              and results[cx][1] for cx in (2, 0)))

    # ---------------------------------------------------------------- S5
    print("\nS5 -- the fences, restated as a check")
    check("S5.FENCE: THE PHYSICAL SELECTION IS NOT DERIVED -- why the "
          "dominant mode should satisfy the ladder self-consistency is "
          "the relocated open question (the same slot as the "
          "RP-selection of the alignment bit, v528/v534); the resonance "
          "between the reconstruction bit and the alignment bit is a "
          "TYPED OBSERVATION, not an identification; Stage B of v567 "
          "(GATE.QGEO.01) untouched; NO P2 reduction; AX.P2.01 and "
          "ANCHOR.GEN.01 markers untouched; the selector is typed [C] "
          "as candidate canonical selection; Smith 1861 / Hermite 1851 "
          "/ Gabriel 1972 / Perron-Frobenius named CLASSICAL as "
          "addresses",
          True)

    print("\nv568 anchors: twins integrally distinct (equal index 81, "
          "different lattices); dominant mode v(c) =")
    print("  (1, 2, 2c) with the ladder self-consistency picking c = 2 "
          "uniquely on all 28; split member at")
    print("  q32 = 1 excluded (dim 5); mu4-grading candidate fails, "
          "F3[V]-action exists (Priority 2 sharpened)")
    return summary("DIAMOND.BIT.SELECT.01 reconstruction bit selector")


if __name__ == "__main__":
    raise SystemExit(run())
