"""BIT.SELECTOR -- Priorities 2+3 of the self-code review, fused with the
v567 residual bit.

THE SITUATION.  v567 (No-Carrier-Reconstruction, Stage A) left EXACTLY one
binary freedom: the 81-pinned reconstruction class is {Q_2 (corpus, q32 = 2
= |Z2|), Q_0 (q32 = 0)}, and every classical carrier-free certificate
coincides on the pair -- the only classical separator is the FORBIDDEN
carrier column budget.  The review's Priority 3 asks for split/nonsplit
variants BEFORE physical selection; v566 S5 gave the A2 Ext carrier.  THIS
probe decides what actually separates the twins, whether the split geometry
is even reachable, and it runs the Priority-2 candidate tests for the
mark-local structure of the 81.

VERDICT RULE (frozen): SELECTOR-FOUND iff (i) the twins are separated by an
exact intrinsic (carrier-free) datum, (ii) a canonical, corpus-anchored
selection condition picks the corpus member UNIQUELY on the whole
28-member class, and (iii) the split geometry is located and excluded by
the already-imposed demands; UNDERDETERMINED if the twins admit no
intrinsic separator; the Priority-2 candidate tests are reported
support/fail per candidate (no verdict weight -- the mechanism may need a
candidate not tried here).

FENCES:
  * The selection condition is typed [C] (candidate canonical selector):
    its UPSTREAM justification -- why the dominant mode should reproduce
    its own eigenvalue ladder -- is the relocated open question, exactly
    parallel to the alignment-bit selection (v528/v534: RP selects).
    Nothing here derives the bit; it LOCATES it and gives it a canonical
    exact witness.
  * No-free-pattern: the (1,2,4) ladder is admitted as a selector ONLY
    because it is prior load-bearing corpus structure (AnchorLadder
    p_{n+1} - p_n = 2^n, Lean-formalised; p_n(a) = 2 + 2^n; 2 = |Z2|) --
    not a number found by staring.
  * Priority-2 honesty: a failed candidate does NOT fire the review's
    kill condition (which requires that NO canonical local decomposition
    exists); the 81 stays a fingerprint pending a mechanism.
  * No ledger/paper edits from this probe; markers untouched.

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import time
from itertools import product

import sympy as sp
import sympy.matrices.normalforms as nf
from sympy.matrices.normalforms import hermite_normal_form

T0 = time.time()
I3 = sp.eye(3)
SIG = sp.diag(1, -1, -1)
IDX7 = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))

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


def section(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


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


section("BIT.SELECTOR -- the residual bit located, separated and given a "
        "canonical witness")

# ============================================================ B1 =============
section("B1  THE TWINS ARE INTEGRALLY DISTINCT (the bit is visible)")

H0 = hermite_normal_form(order_coords(Qc(0)).T)
H2 = hermite_normal_form(order_coords(Qc(2)).T)
check("B1.1 [E] the two 81-twins generate DIFFERENT integral orders: the "
      "Hermite bases of Z<U,V> for q32 = 0 and q32 = 2 differ (equal "
      "index 81, different sublattices of the parabolic lattice) -- the "
      "bit is integrally visible even though every classical certificate "
      "(anticommutator spectrum, commutator charpoly, det, Smith "
      "divisors) coincides",
      H0 != H2
      and snf_divs(order_coords(Qc(0))) == snf_divs(order_coords(Qc(2)))
      == [1, 1, 1, 3, 3, 3, 3])

# ============================================================ B2 =============
section("B2  THE SELECTOR: the dominant mode reproduces its own eigenvalue "
        "ladder iff q32 = 2")

c = sp.symbols('c', nonnegative=True)
Vc = sp.Matrix([[0, 1, 0], [0, 2, 0], [0, c, 1]])
vdom = sp.Matrix([1, 2, 2 * c])
check("B2.1 [E] symbolic in the coupling c: V_c (1, 2, 2c)^T = "
      "2 (1, 2, 2c)^T identically -- the dominant (eigenvalue-2) "
      "eigenvector of the sheet direction is v(c) = (1, 2, 2c) for EVERY "
      "member of the reconstruction family",
      sp.simplify(Vc * vdom - 2 * vdom) == sp.zeros(3, 1))
lam = sp.Integer(2)
ladder = sp.Matrix([lam**0, lam**1, lam**2])
sol = sp.solve(sp.Eq(2 * c, 4), c)
check("B2.2 [E] THE SELF-CONSISTENCY SELECTION: v(c) equals the geometric "
      "ladder of its own eigenvalue, (lam^0, lam^1, lam^2) = (1, 2, 4), "
      "iff 2c = 4 iff c = 2 -- UNIQUELY.  The corpus member is the one "
      "whose dominant mode reproduces its own eigenvalue as the ladder; "
      "the twin (c = 0) truncates it to (1, 2, 0)",
      sol == [2] and vdom.subs(c, 2) == ladder
      and vdom.subs(c, 0) != ladder)
# uniqueness on the WHOLE v567 28-member class (rebuild it quickly)
N_FAM = 3


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
    """dominant eigenvalue simple+integer AND eigenvector = its ladder."""
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
    if P_ == sp.zeros(3, 3) or sp.expand(P_ * P_ - P_) != sp.zeros(3, 3):
        continue
    U, V = UV(Q)
    if stab_line_exists(U, V):
        Mc = sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                        for w in words_up_to(U, V, 4)])
        if Mc.rank() <= 7:
            family.append(Q)
ladder_members = [Q for Q in family
                  if dom_ladder_test(Q * sp.diag(0, 1, 1))]
check("B2.3 [E] UNIQUENESS ON THE WHOLE CLASS: among ALL %d members of the "
      "v567 parabolic reconstruction class, EXACTLY ONE satisfies the "
      "ladder self-consistency -- and it is the corpus Q.  The selection "
      "condition needs no 81-pin and no column budget: it alone pins Q "
      "within the carrier-free class" % len(family),
      len(ladder_members) == 1 and ladder_members[0] == Qc(2))
check("B2.4 [C, anchored] THE WITNESS IS PRIOR STRUCTURE, NOT A FOUND "
      "NUMBER: the selected ladder (1, 2, 4) = (2^0, 2^1, 2^2) is the "
      "binary AnchorLadder step sequence p_{n+1} - p_n = 2^n "
      "(Lean-formalised) and 2 = |Z2| is the sheet datum; the trace code "
      "p_n(a) = 1 + tr(V^n) = 2 + 2^n (v566) rides the SAME ladder -- "
      "consistency: tr(V^n) = 0^n + 1^n + 2^n for n = 1..6 exact",
      all(((Qc(2) * sp.diag(0, 1, 1))**n_).trace() == 1 + 2**n_
          for n_ in range(1, 7)))

# ============================================================ B3 =============
section("B3  THE SPLIT GEOMETRY: located at q32 = 1 and EXCLUDED by the "
        "demands already imposed")

a_, b_ = sp.symbols('a_ b_')
# invariant complement L = span((1,0,a),(0,1,b)) of the line Z e3:
# U-invariance forces a + b = 1; V-invariance forces a = 0 and a + b = c
Qs = Qc(1)
Us, Vs = UV(Qs)
L1, L2 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 1])


def in_plane(v, p1, p2):
    return sp.Matrix.hstack(p1, p2, v).det() == 0


split_ok = all(in_plane(M * w, L1, L2)
               for M in (Us, Vs) for w in (L1, L2))
check("B3.1 [E] the SPLIT member exists and sits at q32 = 1: the plane "
      "span((1,0,0),(0,1,1)) is invariant under BOTH U and V exactly -- "
      "the standard module splits as (plane) (+) (line); general solve: "
      "U-invariance forces a + b = 1, V-invariance forces a = 0 and "
      "a + b = q32, so a complement exists IFF q32 = 1",
      split_ok
      and sp.solve([sp.Eq(a_ + b_, 1), sp.Eq(a_, 0),
                    sp.Eq(a_ + b_, sp.Symbol('c0'))],
                   [a_, b_, sp.Symbol('c0')])
      == {a_: 0, b_: 1, sp.Symbol('c0'): 1})
d1 = order_coords(Qc(1))
check("B3.2 [E] AND IT IS EXCLUDED BY THE DEMANDS ALREADY IMPOSED: the "
      "split member's direction algebra collapses to dimension %d < 7 "
      "(Smith divisors %s -- no full parabolic, no 81): the seam-line + "
      "saturation demands of v567 admit ONLY nonsplit geometry.  "
      "CONSEQUENCE for the A2 carrier (v566 S5): on the whole "
      "reconstruction class the Ext arrow is NONZERO -- the split class "
      "of the two-element module classification is structurally "
      "unreachable, the bit's remaining freedom (q32 in {0,2}) lives "
      "INSIDE the nonsplit side"
      % (d1.rank(), snf_divs(d1)),
      d1.rank() == 5 and snf_divs(d1) == [1, 1, 1, 3, 3])
for cx in (0, 2):
    Qx = Qc(cx)
    Ux, Vx = UV(Qx)
    sol_x = sp.solve([sp.Eq(a_ + b_, 1), sp.Eq(a_, 0),
                      sp.Eq(b_, cx)], [a_, b_])
check("B3.3 [E] neither twin splits: for q32 in {0, 2} the constraint "
      "system (a + b = 1, a = 0, a + b = q32) is inconsistent -- both "
      "twins are honestly NONSPLIT; the bit does NOT toggle "
      "split/nonsplit, it toggles WHICH nonsplit integral order is "
      "realised (B1) and whether the dominant mode carries the full "
      "binary ladder (B2)",
      sp.solve([sp.Eq(a_ + b_, 1), sp.Eq(a_, 0), sp.Eq(a_ + b_, 0)],
               [a_, b_]) == [] and
      sp.solve([sp.Eq(a_ + b_, 1), sp.Eq(a_, 0), sp.Eq(a_ + b_, 2)],
               [a_, b_]) == [])

# ============================================================ B4 =============
section("B4  PRIORITY-2 CANDIDATE TESTS: mark-local structure of the 81")

# cokernel presentation from the Hermite basis of O_2
# coordinates: (E11, E12, E21, E22, E31, E32, E33)
rows = [list(H2[:, j]) for j in range(H2.shape[1])]
info("B4 coker presentation",
     "O_2 Hermite basis (columns as lattice vectors): %s" % rows)
# quotient relations derived exactly: reduce the standard basis mod O_2
Mlat = H2.T  # rows = lattice basis
# candidate (i): the Q_+ grading deg(E_jk) = g_k - g_j mod 4, g = (1,2,3)
g_ = (1, 2, 3)
deg = {p: (g_[p[1]] - g_[p[0]]) % 4 for p in IDX7}
# is the order O_2 a GRADED sublattice? (every Hermite basis vector
# homogeneous)  -- if not, the grading cannot descend to the cokernel
homog = []
for j in range(Mlat.shape[0]):
    supp = [IDX7[k] for k in range(7) if Mlat[j, k] != 0]
    degs = {deg[p] for p in supp}
    homog.append(len(degs) <= 1)
check("B4.1 [E, candidate FAILS -- reported honestly] the mu4-grading "
      "candidate deg(E_jk) = g_k - g_j mod 4 (g = the A3 exponent "
      "grading) does NOT make the order a graded sublattice (%d of 7 "
      "Hermite basis vectors are homogeneous): the grading does not "
      "descend to the cokernel -- this natural candidate for 'one Z/3 "
      "per mark' fails; the review's kill condition does NOT fire (other "
      "mechanisms remain), the 81 stays a FINGERPRINT pending a "
      "mechanism" % sum(homog),
      sum(homog) < 7)
# candidate (ii): left multiplication by V on the cokernel (F3-module)
# build the induced action: for each standard unit E, reduce V*E mod O_2
import itertools


def mat_of_coords(vec):
    M = sp.zeros(3, 3)
    for k, (i, j) in enumerate(IDX7):
        M[i, j] = vec[k]
    return M


Vb = Qc(2) * sp.diag(0, 1, 1)
# solve reduction: represent x in P_Z by coords; class of x mod O_2 via
# solving H2 * y = x over Z (residues mod the diagonal structure)
Hs = sp.Matrix(Mlat).T  # columns = basis
act = sp.zeros(7, 7)
for k, (i, j) in enumerate(IDX7):
    E = sp.zeros(3, 3)
    E[i, j] = 1
    W_ = Vb * E
    act[:, k] = sp.Matrix([[W_[i2, j2]] for (i2, j2) in IDX7])
# the cokernel is (Z/3)^4 on generators; compute the action mod the
# lattice: charpoly of the action on P_Z/O_2 over F3 via Smith transform
s_, Uu, Vv = None, None, None
D_, L_, R_ = None, None, None
# use smith_normal_form with transformation: sympy lacks it directly; do
# a pragmatic check instead: does left-V-multiplication PRESERVE O_2?
img_ok = True
for j in range(Hs.shape[1]):
    x = mat_of_coords(list(Hs[:, j]))
    y = Vb * x
    yv = sp.Matrix([[y[i2, j2]] for (i2, j2) in IDX7])
    # y in O_2 iff solving Hs * t = yv has integer solution
    t_ = Hs.solve(yv)
    if not all(x_.is_integer for x_ in t_):
        img_ok = False
        break
check("B4.2 [E] candidate (ii): left multiplication by V preserves the "
      "order lattice (V * O_2 subset O_2: %s), so it DOES induce an "
      "F3-linear action on the cokernel (Z/3)^4 -- a canonical module "
      "structure EXISTS; whether its character decomposition matches "
      "'one Z/3 per mark' is the sharpened Priority-2 question, left "
      "open with a concrete object to compute on" % img_ok,
      img_ok)

# ======================================================== VERDICT ===========
section("VERDICT -- evaluated as pre-registered")

VERDICT = "SELECTOR-FOUND" if not FAILS else "UNDERDETERMINED"
print("""
  *** VERDICT: %s. ***

  (1) THE BIT IS INTEGRALLY VISIBLE: the two 81-twins generate different
      integral orders (equal index, different lattices) -- B1.
  (2) A CANONICAL SELECTOR EXISTS: the dominant mode of the sheet
      direction satisfies V v = 2v with v = (1, 2, 2 q32); demanding that
      the dominant mode reproduce ITS OWN eigenvalue ladder
      (v = (2^0, 2^1, 2^2)) picks q32 = 2 -- the corpus Q -- UNIQUELY on
      the whole 28-member carrier-free class, with no 81-pin and no
      column budget.  The witness ladder is prior load-bearing structure
      (AnchorLadder / trace code), not a found number -- B2.
  (3) THE SPLIT GEOMETRY IS LOCATED AND EXCLUDED: a module complement
      exists iff q32 = 1, and that member's algebra collapses (dim 5, no
      81): the reconstruction class is nonsplit THROUGHOUT -- the v566
      A2 Ext arrow is nonzero on the whole class, and the residual bit
      lives inside the nonsplit side -- B3.
  (4) PRIORITY 2: the mu4-grading candidate for 'one Z/3 per mark' FAILS
      (the order is not graded); but left-V-multiplication induces a
      canonical F3-action on the cokernel -- the mechanism question is
      sharpened to a concrete module computation, kill not fired -- B4.

  RELOCATED OPEN QUESTIONS: why the dominant mode should satisfy the
  ladder self-consistency (the physical selection -- same slot as the
  RP-selection of the alignment bit, v528/v534); the F3[V]-character
  structure of the cokernel vs the four marks; Stage B of v567.
""" % VERDICT)

section("TOTAL")
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
print("VERDICT: %s" % VERDICT)
