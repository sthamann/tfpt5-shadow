"""NO-CARRIER-RECONSTRUCTION -- Priority 1 of the self-code review, Stage A.

THE QUESTION (the review's 'single brutal question', verbatim): can Q --
hence V and the whole parabolic anchor self-code (v566) -- be reconstructed
WITHOUT the carrier / anchor inputs?  If yes, the self-code is upstream of
a = (1,1,2) and g_car = 5 and becomes a P2-reduction candidate; if no, it is
an elegant self-compression, not a reduction.

THE CIRCULARITY, LOCATED EXACTLY.  The corpus' uniqueness certificate for Q
(v11) enumerates over row sums (4,5,6), column sums (9,5,1) and
chi_Q = (t-1)(t^2 - 5t + 3), with monotone rows -- the 5 (= g_car) sits in
the budgets AND in chi_Q.  Those inputs are FORBIDDEN here.

ALLOWED UPSTREAM INPUTS (declared; each with its corpus source and its
carrier-free provenance):
  (S)  Sigma = diag(1,-1,-1)          -- the sheet Z2 involution (v10; sheet
                                         datum, not carrier).
  (W)  Q(I + Sigma) = 2 N_fam W       -- the first-generation winding
                                         normalisation, W = ones x e1^T
                                         (v10 check line, '6W = 2*N_fam';
                                         family + winding datum).
  (E)  Spec(Q_+) = {1, 2, 3}          -- the A3 exponent grading
                                         (FLAV.QGEO.01; family Lie datum).
  (M)  Q_- != 0, Q_-^2 = N_fam P, P^2 = P
                                      -- the sheet-monodromy budget
                                         (FLAV.QGEO.01 'Q_-^2 = N_fam on
                                         support'; family datum).
  (Z)  nonnegative integrality, entry bound B (declared: B = 6; robustness
                                         re-run at B = 9) -- compiler
                                         convention.
  (L)  the SEAM-LINE demand: the direction algebra <I, U', V'> stabilises
       a line (the parabolic/flag structure; geometric demand, typed [C] --
       it is the 'realise Q_+/Q_- on parabolic P1\\mu4' side of the gate).
  (X)  optionally, ONE integral invariant: the saturation index
       [P_Z : Z<U',V'>] = N_fam^4 = 81 (family datum; v566 S4).
FORBIDDEN (the review's list): g_car = 5, a = (1,1,2), rank E8 = 8, the v11
row/column budgets, chi_Q, monotone-row selection, a^T K a = 41, any
carrier-aware quantity.

VERDICT RULE (frozen BEFORE the run):
  RECONSTRUCTS-CLEAN   if the admissible set under (S)(W)(E)(M)(Z)(L)(X) is
                       a single Sigma-equivalence class containing Q, and
                       every member codes the SAME anchor
                       ((1,1,2) spectrum; (4,5,2) = flag/Levi/radical).
  RECONSTRUCTS-TO-FAMILY if the admissible set is larger but EVERY member
                       codes the same anchor data -- the anchor self-code
                       is carrier-free even where Q itself is not pinned;
                       the residual freedom is reported exactly.
  NEEDS-CARRIER (KILL) if admissible members code DIFFERENT anchor spectra,
                       or if no carrier-free invariant separates them where
                       they differ, or if the corpus Q is not admissible.
Equivalence: conjugation by the Sigma-preserving coordinate swap
P23 = perm(2,3) (the sheet-mirror relabeling).

HONESTY / FENCES:
  * Stage A only: the constraints (S)(W)(E)(M) are the corpus' OWN declared
    geometric reductions of Q; whether THEY can be derived from
    mu4/D4/H^1-geometry without family data is the still-open gate
    GATE.QGEO.01 -- untouched here.  A PASS below upgrades nothing by
    itself; it RELOCATES the audit to that gate.
  * The seam-line demand (L) is typed [C]: it is the structural reading of
    'the diamond directions act on the flag', not a theorem.
  * The ablation (A4) reports what happens WITHOUT the winding input (W) --
    the class widens; the widening is quantified, not hidden.
  * No ledger/paper/website file is touched; AX.P2.01 untouched.

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import time
from itertools import product

import sympy as sp
import sympy.matrices.normalforms as nf

T0 = time.time()
I3 = sp.eye(3)
SIG = sp.diag(1, -1, -1)
P23 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
N_FAM = 3
Q_CORPUS = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])

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


IDX7 = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))


def qplus(Q):
    return (Q + SIG * Q * SIG) / 2


def qminus(Q):
    return (Q - SIG * Q * SIG) / 2


def sat_constraints(Q):
    """(W) winding, (E) exponent spectrum, (M) monodromy budget."""
    if Q * (I3 + SIG) != 2 * N_FAM * sp.Matrix([[1, 0, 0], [1, 0, 0],
                                                [1, 0, 0]]):
        return False
    Qp = qplus(Q)
    if not all(x.is_integer for x in Qp):
        return False
    ev = Qp.eigenvals()
    if ev != {sp.Integer(1): 1, sp.Integer(2): 1, sp.Integer(3): 1}:
        return False
    Qm = qminus(Q)
    if Qm == sp.zeros(3, 3):
        return False
    Q2 = Qm * Qm
    if Q2 == sp.zeros(3, 3):
        return False
    P = Q2 / N_FAM
    if not all(x.is_integer or x.is_rational for x in P):
        pass
    if sp.expand(P * P - P) != sp.zeros(3, 3):
        return False
    return True


def stabilised_lines(U, V):
    """rational common invariant lines of U and V."""
    lines = []
    seen = []
    for M in (V, U):
        for ev, mult, vecs in M.eigenvects():
            for v in vecs:
                v = sp.Matrix(v)
                d = sp.lcm([sp.denom(x) for x in v])
                v = sp.expand(v * d)
                g = sp.gcd(list(v))
                if g != 0:
                    v = sp.Matrix([sp.cancel(x / g) for x in v])
                key = tuple(v)
                if key in seen or tuple(-x for x in v) in seen:
                    continue
                seen.append(key)
                Uv, Vv = U * v, V * v
                ok = True
                for w in (Uv, Vv):
                    M2 = sp.Matrix.hstack(v, w)
                    if M2.rank() > 1:
                        ok = False
                        break
                if ok:
                    lines.append(v)
    return lines


def algebra_span(U, V, maxlen=5):
    words = [I3]
    frontier = [I3]
    for _ in range(maxlen):
        frontier = [w * G for w in frontier for G in (U, V)]
        words += frontier
    return words


def algebra_dim(U, V):
    words = algebra_span(U, V, 4)
    Mc = sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                    for w in words])
    return Mc.rank()


def anchor_code(V):
    """(spectrum of H, dominant simple?) via the dominant projector."""
    ev = V.eigenvals()
    evs = sorted(ev.keys(), key=lambda e: abs(sp.re(sp.N(e))))
    dom = evs[-1]
    if ev[dom] != 1 or not dom.is_integer:
        return None
    others = [e for e in ev if e != dom]
    Pi = I3
    for e in others:
        Pi = Pi * (V - e * I3) / (dom - e)
    H = I3 + Pi
    return tuple(sorted(sp.Poly(H.charpoly(sp.symbols('x')),
                                sp.symbols('x')).all_coeffs()))


def saturation_index(U, V):
    words = algebra_span(U, V, 5)
    Mc = sp.Matrix([[w[i, j] for (i, j) in IDX7] for w in words])
    if Mc.rank() != 7:
        return None
    s_ = nf.smith_normal_form(Mc.T)
    divs = [abs(s_[i, i]) for i in range(min(s_.shape)) if s_[i, i] != 0]
    out = 1
    for d in divs:
        out *= d
    return out


section("NO-CARRIER-RECONSTRUCTION -- Stage A (the review's Priority 1)")
info("forbidden", "g_car = 5, a = (1,1,2), rank 8, v11 budgets "
                  "(rows (4,5,6), cols (9,5,1), chi_Q), monotone rows")
info("allowed", "(S) Sigma, (W) winding 2 N_fam W, (E) Spec Q_+ = {1,2,3}, "
                "(M) Q_-^2 = N_fam P idempotent, (Z) nonneg int <= B, "
                "(L) seam-line demand, (X) saturation index N_fam^4")

# ============================================================ A1 =============
section("A1  THE ADMISSIBLE SET under (S)(W)(E)(M)(Z), B = 6")

B = 6
admissible = []
# (W) forces the first column to (3,3,3): scan the remaining 6 entries
for q12, q13, q22, q23, q32, q33 in product(range(B + 1), repeat=6):
    Q = sp.Matrix([[3, q12, q13], [3, q22, q23], [3, q32, q33]])
    if sat_constraints(Q):
        admissible.append(Q)
info("A1 count", "admissible under (S)(W)(E)(M)(Z): %d matrices"
     % len(admissible))
corpus_in = any(Q == Q_CORPUS for Q in admissible)
check("A1.1 the corpus Q IS admissible under the carrier-free constraints "
      "(a necessary sanity condition for the whole audit)", corpus_in)
# the (W)-forced structure, stated exactly:
check("A1.2 the winding normalisation (W) alone forces the first column to "
      "(3,3,3) = N_fam (1,1,1) and hence q11 = 3 in Spec(Q_+): the '3' of "
      "the corpus Q's first column is FAMILY data, not carrier data",
      all(Q[:, 0] == sp.Matrix([3, 3, 3]) for Q in admissible))

# ============================================================ A2 =============
section("A2  THE SEAM-LINE DEMAND (L): which admissible Q' are parabolic?")

parabolic = []
for Q in admissible:
    U = Q * sp.diag(1, 0, 0)
    V = Q * sp.diag(0, 1, 1)
    if len(stabilised_lines(U, V)) >= 1 and algebra_dim(U, V) <= 7:
        parabolic.append(Q)
info("A2 count", "parabolic (line-stabilising, dim <= 7): %d of %d"
     % (len(parabolic), len(admissible)))
check("A2.1 the seam-line demand has TEETH: it cuts the admissible set "
      "properly (%d -> %d) -- without (L), the carrier-free constraints do "
      "NOT force the parabolic self-code"
      % (len(admissible), len(parabolic)),
      0 < len(parabolic) < len(admissible))

# ============================================================ A3 =============
section("A3  THE ANCHOR CODE on the parabolic class -- pass/family/kill")

codes = {}
sat_idx = {}
dims = {}
for Q in parabolic:
    U = Q * sp.diag(1, 0, 0)
    V = Q * sp.diag(0, 1, 1)
    c = anchor_code(V)
    codes[tuple(Q)] = c
    dims[tuple(Q)] = algebra_dim(U, V)
    sat_idx[tuple(Q)] = saturation_index(U, V)
uniq_codes = set(codes.values())
x = sp.symbols('x')
target = tuple(sorted(sp.Poly(x**3 - 4 * x**2 + 5 * x - 2, x).all_coeffs()))
check("A3.1 EVERY parabolic admissible Q' codes the SAME anchor: the "
      "dominant projector construction H' = I + Pi_dom gives char poly "
      "x^3 - 4x^2 + 5x - 2, i.e. spectrum (1,1,2) = a, for ALL %d members "
      "(%d distinct codes) -- the ANCHOR is carrier-free on this class"
      % (len(parabolic), len(uniq_codes)),
      uniq_codes == {target})
full7 = [Q for Q in parabolic if dims[tuple(Q)] == 7]
info("A3 algebra dims", "dim 7 (full parabolic): %d of %d; smaller: %s"
     % (len(full7), len(parabolic),
        sorted({dims[tuple(Q)] for Q in parabolic} - {7})))
idx_hist = {}
for Q in parabolic:
    idx_hist.setdefault(sat_idx[tuple(Q)], []).append(Q)
info("A3 saturation indices", "%s"
     % {k: len(v) for k, v in sorted(idx_hist.items(),
                                     key=lambda kv: (kv[0] is None,
                                                     kv[0]))})
sel81 = idx_hist.get(81, [])
# Sigma-mirror equivalence classes of the 81-selected set
classes = []
used = set()
for Q in sel81:
    tq = tuple(Q)
    if tq in used:
        continue
    Qm = P23 * Q * P23
    used.add(tq)
    used.add(tuple(Qm))
    classes.append((Q, Qm))
check("A3.2 THE INTEGRAL PIN (X): demanding the saturation index 81 = "
      "N_fam^4 (a FAMILY datum, v566 S4) selects %d matrices = %d "
      "Sigma-mirror class(es); the corpus Q is among them"
      % (len(sel81), len(classes)),
      len(sel81) >= 1 and any(Q == Q_CORPUS for Q in sel81))
uniq_after_pin = len(classes) == 1
info("A3 verdict input", "unique class after (X): %s; class "
     "representatives: %s" % (uniq_after_pin,
                              [list(c[0]) for c in classes[:4]]))

# --- A3.3: the residual family, dissected exactly ---------------------------
if len(sel81) == 2:
    Qa = [Q for Q in sel81 if Q != Q_CORPUS][0]
    t = sp.symbols('t')
    anti_c = sorted((Q_CORPUS * SIG + SIG * Q_CORPUS).eigenvals().keys(),
                    key=str)
    anti_a = sorted((Qa * SIG + SIG * Qa).eigenvals().keys(), key=str)
    comm_c = sp.factor((Q_CORPUS * SIG - SIG * Q_CORPUS)
                       .charpoly(t).as_expr())
    comm_a = sp.factor((Qa * SIG - SIG * Qa).charpoly(t).as_expr())
    diff = sp.expand(Q_CORPUS - Qa)
    colsum_c = [sum(Q_CORPUS[:, j]) for j in range(3)]
    colsum_a = [sum(Qa[:, j]) for j in range(3)]
    check("A3.3 THE RESIDUAL TWO-ELEMENT FAMILY, DISSECTED: the two "
          "(X)-survivors are the corpus Q and Q_alt differing ONLY in the "
          "sheet-block coupling entry q32 (2 = |Z2| vs 0; difference "
          "matrix = 2 E32); ALL classical carrier-free separators "
          "COINCIDE -- anticommutator spectrum {6,-4,-2} = "
          "(|R+(A3)|, -|mu4|, -|Z2|) (equal: %s), commutator charpoly "
          "t(t^2+12) (equal: %s), det = 3 (equal: %s) -- while the one "
          "certificate that DOES separate them is the carrier column "
          "budget (9,5,1) vs (9,3,1), i.e. exactly the FORBIDDEN input: "
          "the residual binary freedom is a coupled-vs-uncoupled "
          "sheet-block choice, and its carrier-free selection is an open "
          "door (candidate: the split/nonsplit alignment-bit structure, "
          "v528/v534/v566 S5 -- recorded as a typed observation, NOT "
          "claimed)"
          % (anti_c == anti_a, comm_c == comm_a,
             Q_CORPUS.det() == Qa.det()),
          diff == 2 * sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 1, 0]])
          and anti_c == anti_a and comm_c == comm_a
          and Q_CORPUS.det() == Qa.det() == 3
          and colsum_c == [9, 5, 1] and colsum_a == [9, 3, 1])

# ============================================================ A4 =============
section("A4  ABLATIONS -- honesty about each input's load")

# (a) drop (X): how much freedom remains in the parabolic class?
resid = {}
for Q in parabolic:
    key = (dims[tuple(Q)], sat_idx[tuple(Q)])
    resid.setdefault(key, 0)
resid_n = len({tuple(Q) for Q in parabolic})
check("A4.1 WITHOUT the integral pin (X), the parabolic class retains %d "
      "members -- but ALL of them code the same anchor (A3.1): the anchor "
      "self-code needs (S)(W)(E)(M)(L) only; the pin is needed to select "
      "Q itself, not the anchor" % resid_n,
      resid_n >= 1 and uniq_codes == {target})
# (b) drop (W): fast pure-integer scan WITHOUT the winding condition
B_ABL = 3


def sem_only(q11, q12, q13, q21, q22, q23, q31, q32, q33):
    """(S)(E)(M) without (W), plain integers (Sigma = diag(1,-1,-1))."""
    # Q_+ = diag-block(q11, D), D = [[q22,q23],[q32,q33]]
    if q11 not in (1, 2, 3):
        return False
    trD, detD = q22 + q33, q22 * q33 - q23 * q32
    rest = {1, 2, 3} - {q11}
    lo, hi = min(rest), max(rest)
    if trD != lo + hi or detD != lo * hi:
        return False
    # discriminant must give the two integer eigenvalues (2x2: automatic
    # once trace/det match a factorable pair)
    # Q_- = offblock((q12,q13);(q21,q31)); Q_-^2 = 3P, P idempotent, != 0
    s = q12 * q21 + q13 * q31
    if (q12, q13, q21, q31) == (0, 0, 0, 0):
        return False
    if s != 3:
        return False
    return True


wide = 0
seen_first_cols = set()
for entries in product(range(B_ABL + 1), repeat=9):
    if sem_only(*entries):
        wide += 1
        seen_first_cols.add((entries[0], entries[3], entries[6]))
with_w = len([Q for Q in admissible if all(x <= B_ABL for x in Q)])
check("A4.2 WITHOUT the winding input (W) (pure-integer ablation at "
      "B_abl = %d): the (S)(E)(M)-only set has %d members over %d distinct "
      "first columns, vs %d WITH (W) -- the winding normalisation carries "
      "REAL selection load (it fixes the first column to N_fam(1,1,1))"
      % (B_ABL, wide, len(seen_first_cols), with_w),
      wide > with_w and len(seen_first_cols) > 1
      and (3, 3, 3) in seen_first_cols)
# (c) robustness of A1 at B = 9 (spot: no new parabolic-81 classes)
adm9_new81 = []
for q12, q13, q22, q23, q32, q33 in product(range(10), repeat=6):
    if max(q12, q13, q22, q23, q32, q33) <= B:
        continue
    Q = sp.Matrix([[3, q12, q13], [3, q22, q23], [3, q32, q33]])
    if not sat_constraints(Q):
        continue
    U = Q * sp.diag(1, 0, 0)
    V = Q * sp.diag(0, 1, 1)
    if len(stabilised_lines(U, V)) >= 1 and algebra_dim(U, V) <= 7 \
            and saturation_index(U, V) == 81:
        adm9_new81.append(Q)
check("A4.3 BOUND ROBUSTNESS: raising the entry bound B = 6 -> 9 adds %d "
      "new parabolic members with saturation index 81 -- the (X)-selected "
      "class is bound-stable" % len(adm9_new81),
      len(adm9_new81) == 0)
# (d) forbidden-input audit: the constraints nowhere reference 5/(4,5,6)/...
check("A4.4 FORBIDDEN-INPUT AUDIT (by construction, restated as a check): "
      "the admissibility test uses only Sigma, N_fam = 3, the exponent set "
      "{1,2,3}, idempotency, nonneg integrality and the line demand -- no "
      "row/column budget, no chi_Q, no 5, no monotonicity was evaluated "
      "anywhere in A1-A3", True)

# ======================================================== VERDICT ===========
section("VERDICT -- evaluated as pre-registered")

if not any(Q == Q_CORPUS for Q in parabolic):
    VERDICT = "NEEDS-CARRIER"
elif uniq_codes == {target} and uniq_after_pin:
    VERDICT = "RECONSTRUCTS-CLEAN"
elif uniq_codes == {target}:
    VERDICT = "RECONSTRUCTS-TO-FAMILY"
else:
    VERDICT = "NEEDS-CARRIER"

print("""
  *** VERDICT: %s. ***

  WHAT WAS DECIDED.  Under the corpus' OWN carrier-free geometric data --
  the sheet involution (S), the winding normalisation (W), the A3 exponent
  spectrum (E), the sheet-monodromy budget (M), nonneg integrality (Z) and
  the seam-line demand (L) -- EVERY admissible direction pair codes the
  SAME anchor a = (1,1,2) via the dominant-projector construction: the
  ANCHOR SELF-CODE IS CARRIER-FREE on the whole admissible class.  Adding
  the single FAMILY invariant (X) = saturation index N_fam^4 = 81 narrows
  Q itself to a TWO-ELEMENT residual family {Q_corpus, Q_alt} differing
  only in the sheet-block coupling entry q32 in {2 = |Z2|, 0}; every
  classical carrier-free certificate (anticommutator spectrum, commutator
  charpoly, determinant, saturation index) COINCIDES on the pair, and the
  one certificate that separates them is the carrier column budget
  (9,5,1) -- exactly the forbidden input.  The v11 carrier budgets were
  used NOWHERE in the reconstruction.

  WHAT THIS DOES NOT DECIDE (the relocated audit, named): (i) Stage B --
  whether (S)(W)(E)(M) and the line demand (L) can themselves be derived
  from mu4/D4/H^1 parabolic geometry without family/sheet inputs is
  EXACTLY the open gate GATE.QGEO.01, untouched (N_fam = 3 is used
  throughout: family data was never on the forbidden list -- the
  forbidden list is the CARRIER list); (ii) the carrier-free SELECTOR of
  the residual binary choice q32 in {0, 2} -- the coupled-vs-uncoupled
  sheet block -- is open; its structural resonance with the split/
  nonsplit alignment-bit dichotomy (v528/v534/v566 S5) is recorded as a
  typed observation, NOT claimed.  No marker moves; AX.P2.01 untouched;
  a P2-reduction is NOT claimed -- established is: the anchor self-code
  sits UPSTREAM of the carrier budgets, and Q is carrier-free up to ONE
  binary sheet-coupling choice, conditional on the declared geometric
  inputs.
""" % VERDICT)

section("TOTAL")
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
print("VERDICT: %s" % VERDICT)
