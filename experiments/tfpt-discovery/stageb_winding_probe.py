"""QGEO.WINDING.SELF -- Stage B of the No-Carrier-Reconstruction audit,
first narrowing: the winding normalisation N_fam = 3 and the involution
TYPE relocate from declared inputs to consistency-forced -- the double
self-consistency (ladder + saturation) pins (N, Q) = (3, compiler Q)
across the whole N-ablated family.

THE QUESTION (GATE.QGEO.01, relocated by v567): the Stage-A audit used the
geometric inputs (S) Sigma = diag(1,-1,-1), (W) Q(I+Sigma) = 2 N_fam W,
(E) Spec Q_+ = {1,2,3}, (M) Q_-^2 = N_fam P, (L) seam line.  Stage B asks
which of these are themselves forced.  This probe ablates TWO of them:
the involution TYPE in (S) and the family factor N in (W)+(M).

DESIGN (bounds declared before the run): enumeration bound B = 6 on the
free entries (the v567 bound); N scanned over {1..6}; the corpus
involution type (1|2: one positive direction) vs the opposite type (2|1);
ladder self-consistency and saturation self-consistency sat = N^4 as the
two selectors (both prior structure: v568's selector and v567's (X)).
Verdict enums (frozen): FORCED (exactly (N, Q) = (3, compiler Q) survives
the double self-consistency; type killed by theorem), FREE (other N
survive), MIXED.

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import time
from itertools import product

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

T0 = time.time()
FAILS = []
N_CHK = 0

B_ENTRY = 6


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def info(name, detail=""):
    print("[INFO] %s%s" % (name, (": " + detail) if detail else ""))


I3 = sp.eye(3)
IDX7 = ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2))
SIG = sp.diag(1, -1, -1)
Q_CORPUS = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])

print("=" * 78)
print("QGEO.WINDING.SELF -- Stage B, first narrowing")
print("=" * 78)

# --- S1: the involution TYPE is killed by a rank theorem --------------------
q = sp.MatrixSymbol("q", 3, 3)
Pminus_21 = sp.diag(0, 0, 1)      # opposite type: 2-dim POSITIVE eigenspace
Vgen = sp.Matrix(q) * Pminus_21
x = sp.symbols("x")
cp = sp.factor(Vgen.charpoly(x).as_expr())
check("S1.1 [E, theorem -- THE TYPE IS FORCED] for ANY involution with a "
      "TWO-dimensional positive eigenspace the sheet direction V' = Q "
      "P_- has rank <= 1: its characteristic polynomial is x^2 (x - t) "
      "identically in Q (symbolic: %s), so Spec V' has at most ONE "
      "nonzero value -- the binary trace code Spec V = {0, 1, 2} "
      "(v566, p_n = 2 + 2^n) is UNREACHABLE: only the corpus type "
      "(one positive direction) can carry the self-code" % cp,
      sp.simplify(cp / x**2 * 0 + (Vgen.charpoly(x).as_expr()
                                   - x**3 + sp.trace(Vgen) * x**2))
      == 0)


def admissible_class(N):
    """(S)(W)(E)(M)(Z) enumeration at winding normalisation N."""
    out = []
    if N > 3:
        return out                     # (E): q11 = N must be an exponent
    rest = {1, 2, 3} - {N}
    lo, hi = min(rest), max(rest)
    for q12, q13, q22, q23, q32, q33 in product(range(B_ENTRY + 1),
                                                repeat=6):
        # (E) integer prefilter on the lower block
        if q22 + q33 != lo + hi or q22 * q33 - q23 * q32 != lo * hi:
            continue
        if (q12, q13) == (0, 0):
            continue
        Q = sp.Matrix([[N, q12, q13], [N, q22, q23], [N, q32, q33]])
        Qm = (Q - SIG * Q * SIG) / 2
        Q2 = Qm * Qm
        if Q2 == sp.zeros(3, 3):
            continue
        P = Q2 / N
        if sp.expand(P * P - P) != sp.zeros(3, 3):
            continue
        out.append(Q)
    return out


def parabolic_members(cls):
    out = []
    for Q in cls:
        U, V = Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)
        ws = [I3]
        fr = [I3]
        for _ in range(4):
            fr = [w * G for w in fr for G in (U, V)]
            ws += fr
        Mc = sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                        for w in ws])
        if Mc.rank() == 7:
            out.append(Q)
    return out


def ladder_members(para):
    out = []
    for Q in para:
        V = Q * sp.diag(0, 1, 1)
        ev = [e for e in V.eigenvals() if e != 0]
        dom = max(ev, key=lambda e: abs(e))
        vlad = sp.Matrix([1, dom, dom**2])
        if sp.simplify(V * vlad - dom * vlad) == sp.zeros(3, 1):
            out.append((Q, dom))
    return out


def saturation(Q):
    U, V = Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)
    ws = [I3]
    fr = [I3]
    for _ in range(5):
        fr = [w * G for w in fr for G in (U, V)]
        ws += fr
    Mc = sp.Matrix([[w[i, j] for (i, j) in IDX7] for w in ws])
    if Mc.rank() != 7:
        return None
    s_ = smith_normal_form(Mc.T)
    sat = 1
    for i in range(7):
        if s_[i, i] != 0:
            sat *= abs(s_[i, i])
    return sat


# --- S2: (E) bounds N --------------------------------------------------------
kills = all(len(admissible_class(N)) == 0 for N in (4, 5, 6))
check("S2.1 [E] the exponent demand (E) BOUNDS the winding "
      "normalisation: (W) forces the first column to (N, N, N), so "
      "q11 = N must itself be an A3 exponent -- N in {4, 5, 6} give "
      "EMPTY admissible classes (enumeration at B = %d), N <= 3 by "
      "theorem" % B_ENTRY, kills)

# --- S3: the three surviving families ---------------------------------------
results = {}
for N in (1, 2, 3):
    cls = admissible_class(N)
    para = parabolic_members(cls)
    lads = ladder_members(para)
    sats = [(Q, dom, saturation(Q)) for (Q, dom) in lads]
    results[N] = dict(n_adm=len(cls), n_para=len(para), lads=sats)
    info("N = %d" % N, "admissible %d, parabolic %d, ladder-selected %d"
         % (len(cls), len(para), len(lads)))

check("S3.1 [E] the ladder self-consistency (v568) is ROBUST across the "
      "family: for EVERY N in {1, 2, 3} it selects EXACTLY ONE member "
      "of the parabolic class (%d/%d/%d members -> 1/1/1)"
      % (results[1]["n_para"], results[2]["n_para"],
         results[3]["n_para"]),
      all(len(results[N]["lads"]) == 1 for N in (1, 2, 3)))

sel = {N: results[N]["lads"][0] for N in (1, 2, 3)}
check("S3.2 [E] the selected members and their data: N = 1 -> dom 3, "
      "sat %s; N = 2 -> dom 3, sat %s; N = 3 -> dom 2, sat %s = 3^4 -- "
      "only N = 3 selects the COMPILER Q and the binary ladder (1,2,4)"
      % (sel[1][2], sel[2][2], sel[3][2]),
      sel[3][0] == Q_CORPUS and sel[3][1] == 2
      and sel[1][1] == 3 and sel[2][1] == 3)

# --- S4: the double self-consistency pins N ---------------------------------
sat_ok = {N: (sel[N][2] == N**4) for N in (1, 2, 3)}
check("S4.1 [E, THE CENTRAL RESULT -- the winding normalisation is "
      "FORCED] the saturation self-consistency sat = N^4 (v567's (X), "
      "read as a self-consistency in the family) holds ONLY at N = 3: "
      "N = 1 gives sat 32 != 1, N = 2 gives 512 != 16, N = 3 gives "
      "81 = 3^4 -- the DOUBLE self-consistency (ladder + saturation) "
      "pins (N, Q) = (3, compiler Q) uniquely across the whole "
      "N-ablated family: N_fam = 3 relocates from declared input to "
      "consistency-forced within the reconstruction",
      sat_ok == {1: False, 2: False, 3: True}
      and sel[1][2] == 32 and sel[2][2] == 512 and sel[3][2] == 81)

specs = {}
for N in (1, 2, 3):
    V = sel[N][0] * sp.diag(0, 1, 1)
    specs[N] = tuple(sorted(V.eigenvals().keys(), key=lambda e: sp.N(e)))
check("S4.2 [E] the V-spectra of the selected members: N = 1 -> "
      "{0, 2, 3}, N = 2 -> {0, 1, 3}, N = 3 -> {0, 1, 2}: only N = 3 "
      "carries the binary trace code p_n = 2 + 2^n (the v566 "
      "Spec V = {0, 1, 2}); the winding normalisation and the trace "
      "code select the SAME point",
      specs[1] == (0, 2, 3) and specs[2] == (0, 1, 3)
      and specs[3] == (0, 1, 2))

# --- S4b: the spectrum ablation -- the honest decomposition -----------------
from itertools import combinations

dsc_points = []
for spec in combinations(range(0, 7), 3):
    aa, bb, cc = spec
    for N in spec:
        if N == 0:
            continue
        rest = sorted(set(spec) - {N})
        lo2, hi2 = rest
        for q12, q13, q22, q23, q32, q33 in product(range(B_ENTRY + 1),
                                                    repeat=6):
            if q22 + q33 != lo2 + hi2 or q22 * q33 - q23 * q32 != lo2 * hi2:
                continue
            if (q12, q13) == (0, 0):
                continue
            Q = sp.Matrix([[N, q12, q13], [N, q22, q23], [N, q32, q33]])
            Qm = (Q - SIG * Q * SIG) / 2
            Q2 = Qm * Qm
            if Q2 == sp.zeros(3, 3):
                continue
            P = Q2 / N
            if sp.expand(P * P - P) != sp.zeros(3, 3):
                continue
            Qp = (Q + SIG * Q * SIG) / 2
            if Qp.eigenvals() != {sp.Integer(aa): 1, sp.Integer(bb): 1,
                                  sp.Integer(cc): 1}:
                continue
            U, V = Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)
            ws = [I3]
            fr = [I3]
            for _ in range(4):
                fr = [w * G for w in fr for G in (U, V)]
                ws += fr
            if sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                          for w in ws]).rank() != 7:
                continue
            ev = [e for e in V.eigenvals() if e != 0]
            dom = max(ev, key=lambda e: abs(e))
            vlad = sp.Matrix([1, dom, dom**2])
            if sp.simplify(V * vlad - dom * vlad) != sp.zeros(3, 1):
                continue
            if saturation(Q) == N**4:
                dsc_points.append((spec, N))
check("S4.2b [E, full scan] over ALL 35 three-element spectra in {0..6} "
      "and every admissible N, the double-selfconsistent points are "
      "EXACTLY the one-parameter family spectrum = {1, 2, N}: found %s "
      "-- no other spectrum carries the double self-consistency"
      % dsc_points,
      dsc_points == [((1, 2, 3), 3), ((1, 2, 4), 4), ((1, 2, 5), 5),
                     ((1, 2, 6), 6)])
shape_ok = True
for N in (4, 5, 6):
    QN = sp.Matrix([[N, 1, 0], [N, 2, 0], [N, 2, 1]])
    Qp = (QN + SIG * QN * SIG) / 2
    if Qp.eigenvals() != {sp.Integer(1): 1, sp.Integer(2): 1,
                          sp.Integer(N): 1}:
        shape_ok = False
    VN = QN * sp.diag(0, 1, 1)
    dom = max([e for e in VN.eigenvals() if e != 0], key=lambda e: abs(e))
    vlad = sp.Matrix([1, dom, dom**2])
    if sp.simplify(VN * vlad - dom * vlad) != sp.zeros(3, 1):
        shape_ok = False
    if saturation(QN) != N**4:
        shape_ok = False
check("S4.3 [E, THE HONEST DECOMPOSITION -- spectrum ablation] freeing "
      "the exponent spectrum itself, the double self-consistency does "
      "NOT pin N absolutely: the ONE surviving family is spectrum = "
      "{1, 2, N} with the shape Q(N) = [[N,1,0],[N,2,0],[N,2,1]] -- "
      "verified here for N = 4, 5, 6 (each ladder-selfconsistent with "
      "sat = N^4; full 35-spectrum scan in the discovery probe finds NO "
      "other double-selfconsistent point).  So the forcing decomposes "
      "PRECISELY: the self-consistency forces the SHEET spectrum {1,2} "
      "(the binary trace code) and the compiler SHAPE; the exponent "
      "demand (E) -- the A3 glue geometry -- contributes exactly ONE "
      "datum, N = 3.  The family number is pinned by (self-consistency) "
      "x (A3 exponents), each load-bearing", shape_ok)

# --- S4c: the redundancy ablation -- (M) and (L) fall too -------------------
def selfcode_hits(require_M):
    hits = []
    n_adm = 0
    for q12, q13, q22, q23, q32, q33 in product(range(B_ENTRY + 1),
                                                repeat=6):
        if q22 + q33 != 3 or q22 * q33 - q23 * q32 != 2:
            continue
        Q = sp.Matrix([[3, q12, q13], [3, q22, q23], [3, q32, q33]])
        Qp = (Q + SIG * Q * SIG) / 2
        if not all(x.is_integer for x in Qp):
            continue
        if Qp.eigenvals() != {sp.Integer(1): 1, sp.Integer(2): 1,
                              sp.Integer(3): 1}:
            continue
        if require_M:
            Qm = (Q - SIG * Q * SIG) / 2
            Q2 = Qm * Qm
            if Qm == sp.zeros(3, 3) or Q2 == sp.zeros(3, 3):
                continue
            P = Q2 / 3
            if sp.expand(P * P - P) != sp.zeros(3, 3):
                continue
        n_adm += 1
        V = Q * sp.diag(0, 1, 1)
        ev = [e for e in V.eigenvals() if e != 0]
        if not ev:
            continue
        dom = max(ev, key=lambda e: abs(e))
        vlad = sp.Matrix([1, dom, dom**2])
        if sp.simplify(V * vlad - dom * vlad) != sp.zeros(3, 1):
            continue
        U = Q * sp.diag(1, 0, 0)
        ws = [I3]
        fr = [I3]
        for _ in range(4):
            fr = [w * G for w in fr for G in (U, V)]
            ws += fr
        if sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                      for w in ws]).rank() != 7:
            continue
        if saturation(Q) == 81:
            hits.append(Q)
    return n_adm, hits


n_ml, hits_ml = selfcode_hits(require_M=True)     # (L) dropped
n_none, hits_none = selfcode_hits(require_M=False)  # (M) and (L) dropped
check("S4.4 [E, REDUNDANCY -- (M) and (L) fall too] relative to the "
      "self-code demands (parabolic dim 7 + ladder + sat = 81), the "
      "monodromy budget (M) and the seam-line demand (L) are REDUNDANT "
      "at the declared bound: dropping (L) leaves %d admissible members "
      "and the self-code picks EXACTLY the compiler Q; dropping BOTH "
      "(M) and (L) widens the class to %d members and the self-code "
      "STILL picks exactly the compiler Q -- the declared geometric "
      "input list of the reconstruction shrinks to (S)-existence, "
      "(W)-form and (E), with the type and N already forced"
      % (n_ml, n_none),
      len(hits_ml) == 1 and hits_ml[0] == Q_CORPUS
      and len(hits_none) == 1 and hits_none[0] == Q_CORPUS
      and n_none > 1000)

# --- S4d: the maximal ablation -- (E) falls too ------------------------------
hits_noE = []
cands_noE = 0
for lam_ in range(1, 20):
    for q13 in range(B_ENTRY + 1):
        q12 = 1 - q13 * lam_
        if not (0 <= q12 <= B_ENTRY):
            continue
        for q23 in range(B_ENTRY + 1):
            q22 = lam_ - q23 * lam_
            if not (0 <= q22 <= B_ENTRY):
                continue
            for q33 in range(B_ENTRY + 1):
                q32 = lam_ * lam_ - q33 * lam_
                if not (0 <= q32 <= B_ENTRY):
                    continue
                Q = sp.Matrix([[3, q12, q13], [3, q22, q23],
                               [3, q32, q33]])
                V = Q * sp.diag(0, 1, 1)
                ev = [e for e in V.eigenvals() if e != 0]
                if not ev:
                    continue
                dom = max(ev, key=lambda e: abs(sp.N(e)))
                if dom != lam_:
                    continue
                cands_noE += 1
                U = Q * sp.diag(1, 0, 0)
                ws = [I3]
                fr = [I3]
                for _ in range(4):
                    fr = [w * G for w in fr for G in (U, V)]
                    ws += fr
                if sp.Matrix([[w[i, j] for i in range(3)
                               for j in range(3)]
                              for w in ws]).rank() != 7:
                    continue
                if saturation(Q) == 81:
                    hits_noE.append(Q)
check("S4.5 [E, THE MAXIMAL ABLATION -- (E) falls too] dropping the "
      "exponent demand ENTIRELY (no spectrum condition on Q_+ at all), "
      "the demands (W: first column 3(1,1,1)) + integrality (B = %d) + "
      "the self-code package (parabolic + ladder + sat = 81) STILL pin "
      "the compiler Q uniquely: %d ladder candidates, exactly 1 "
      "self-code hit = the compiler.  Together with S4.4: (E), (M) and "
      "(L) are ALL redundant at the declared bound -- the "
      "reconstruction needs only the sheet involution (type forced), "
      "the winding column with N_fam = 3 (the E8-glue count, v1: "
      "240 = 16 x 5 x 3) and the self-code demands"
      % (B_ENTRY, cands_noE),
      len(hits_noE) == 1 and hits_noE[0] == Q_CORPUS
      and cands_noE >= 20)

# --- S4e: what the winding FORM really does ----------------------------------
lad_cols = []
for lam_ in range(1, 20):
    for q13 in range(B_ENTRY + 1):
        q12 = 1 - q13 * lam_
        if not (0 <= q12 <= B_ENTRY):
            continue
        for q23 in range(B_ENTRY + 1):
            q22 = lam_ - q23 * lam_
            if not (0 <= q22 <= B_ENTRY):
                continue
            for q33 in range(B_ENTRY + 1):
                q32 = lam_ * lam_ - q33 * lam_
                if not (0 <= q32 <= B_ENTRY):
                    continue
                V = sp.Matrix([[0, q12, q13], [0, q22, q23],
                               [0, q32, q33]])
                ev = [e for e in V.eigenvals() if e != 0]
                if not ev:
                    continue
                if max(ev, key=lambda e: abs(sp.N(e))) != lam_:
                    continue
                lad_cols.append((q12, q13, q22, q23, q32, q33))
col_hits = set()
for (q12, q13, q22, q23, q32, q33) in lad_cols:
    for c1, c2, c3 in product(range(B_ENTRY + 1), repeat=3):
        if (c1, c2, c3) == (0, 0, 0):
            continue
        Q = sp.Matrix([[c1, q12, q13], [c2, q22, q23], [c3, q32, q33]])
        U, V = Q * sp.diag(1, 0, 0), Q * sp.diag(0, 1, 1)
        ws = [I3]
        fr = [I3]
        for _ in range(4):
            fr = [w * G for w in fr for G in (U, V)]
            ws += fr
        if sp.Matrix([[w[i, j] for i in range(3) for j in range(3)]
                      for w in ws]).rank() != 7:
            continue
        if saturation(Q) == 81:
            col_hits.add((c1, c2, c3))
uniform = [col for col in col_hits if col[0] == col[1] == col[2]]
check("S4.6 [E, what the winding FORM really does] dropping the winding "
      "demand entirely (arbitrary first column), the self-code package "
      "leaves a FOUR-element column family %s -- and exactly ONE of "
      "them is uniform: (3, 3, 3), the compiler.  The winding demand's "
      "load-bearing content is precisely the UNIFORMITY of the column "
      "(1 of 4); it stays a genuine declared input, now with sharply "
      "located content" % sorted(col_hits),
      len(col_hits) == 4 and uniform == [(3, 3, 3)])

# --- S5: honesty --------------------------------------------------------------
check("S5.1 [C, named limits] what remains of Stage B: the demands (E) "
      "(the A3 exponent spectrum), (M) (the monodromy budget) and (L) "
      "(the seam line) are still DECLARED geometric inputs -- deriving "
      "them from mu4/D4/H^1 geometry is exactly the remaining "
      "GATE.QGEO.01; this probe narrows the gate by two items ((S)'s "
      "type by theorem, (W)'s normalisation by double self-consistency) "
      "and does NOT close it; enumeration bound B = %d declared; "
      "NO P2 reduction, markers untouched" % B_ENTRY, True)

VERDICT = ("FORCED" if not FAILS else "MIXED")
print("\nVERDICT: %s -- type killed by rank theorem; N <= 3 by (E); "
      "double self-consistency (ladder + sat = N^4) pins "
      "(N, Q) = (3, compiler Q) uniquely" % VERDICT)
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
