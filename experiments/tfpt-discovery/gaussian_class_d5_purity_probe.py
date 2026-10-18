#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gaussian_class_d5_purity_probe -- ARF.P2: gaussian_class_d5_weight_purity
-- THE PHYSICAL KILL TEST for the code->matter reading of V = L/(1+i)L.

QUESTION (Priority 2 of the Arf compiler programme, preregistered): does
each of the 15 nonzero Gaussian classes of the E8 quotient V = L/(1+i)L
(v752: 240 roots = 15 x 16, zero class empty) carry EXACTLY the matter
semantics of ONE SU(5) weight state of the D5 half-spinor 16, per the
frozen Arf-compiler prediction table (FROZEN_SPEC below, SHA-256 printed
BEFORE any root data is computed)?

  SUCCESS (ROOTCLASS-PURE)  = the code layer is a genuine matter
                              classifier; the reading MAY later be
                              promoted (separate decision, not here).
  KILL    (ROOTCLASS-MIXED) = at least one class mixes incompatible
                              5bar/10/hypercharge orbits under every
                              defensible convention -> the Arf structure
                              stays mathematics, the physical reading
                              dies; the code->matter table must NOT
                              enter any main claim.
  ROOTCLASS-CONVENTION-AMBIGUOUS = defensible D5(+)A3 / SU(5)
                              conventions disagree (some pure, some
                              mixed) -> the ambiguity is typed exactly.
  TEST-VOID               = a must-fail control does not fire.

MODEL AND CONVENTIONS (documented, frozen):
  *  All computations run in the v752 STANDARD DOUBLED E8 model
     (B_STD basis; integer roots 2(+-e_i +- e_j), 112; spinor roots
     (+-1)^8 with sum = 0 mod 4, 128; J = pair rotation on
     (0,1),(2,3),(4,5),(6,7); sigma = pair 3-cycle).  v752 P5.1 and
     note_e8_gaussian_code Rem. 2 certify that this model carries the
     SAME Gaussian bridge (15 x 16 census, empty zero class, family/
     anchor basis, chi_NSR) as the Construction-A model -- the census
     is presentation independent.  The v752 label machinery is copied
     VERBATIM (make_lattice / label_group / family_anchor_basis /
     herm_std / hbar_std).
  *  D5(+)A3 decomposition: the corpus deploys D5(+)A3 at the Cartan/
     representation level only (v1 glue theorem, v47 selection theorem,
     S+ = Lambda^even(C^5) = 1+10+5bar); NO root-level embedding is
     deployed anywhere in verification/ or the Lean tree.  Therefore
     the probe scans ALL C(8,5) = 56 coordinate splits (D5 = integer
     roots supported in a 5-coordinate block D, A3 = D3 on the
     complement -- the standard D5+D3 c D8 c E8 chain, glue index
     sqrt(4*4/1) = 4 = |mu4| as in v1), and treats the split as a
     convention.  CANONICAL REPORTING SPLIT: D = (0,2,4,6,7) -- one of
     exactly two sigma-stable splits ({0,2,4}+{6,7} and {1,3,5}+{6,7}):
     sigma cycles the three "colour" coordinates 0->2->4 and fixes the
     anchor pair (6,7) = the two "weak" slots.  Non-coordinate (Weyl-
     conjugate) embeddings are NOT scanned; instead the probe proves
     the embedding-INDEPENDENT counting bound: every D5(+)A3 c E8 has
     exactly 128 spinor-side roots ((16,4)+(16bar,4bar)), so at most
     floor(128/16) = 8 of the 15 classes can be spinor-pure for ANY
     embedding whatsoever.
  *  SU(5) branching derived explicitly from root data (documented):
     for a split D, an integer root with both nonzero coordinates in D
     is D5-adjoint (45 of SO(10); sub-orbits: mixed signs -> 24,
     (+,+) -> 10, (-,-) -> 10bar of SU(5)); both outside D -> (1,15)
     A3-adjoint; one in each -> (10_v, 6) with 10_v = 5 (+) 5bar.
     A spinor root restricted to D is a D5 half-spinor weight
     (+-1/2)^5; chirality = parity of the number of minus signs over
     the 5 slots; 16 = Lambda^even(C^5) reading: the NORMALIZED weight
     of a 16bar root is the negative (particle <-> antiparticle), and
     a weight is encoded as its plus-set S (slots with +1/2); with the
     frozen chirality convention cc = 1 ("16" = odd number of minus
     signs over D) all normalized plus-sets are EVEN subsets, matching
     S+ = Lambda^even(C^5) = 1 (+) 10 (+) 5bar exactly.  Hypercharge:
     X(root) = <halved D5 weight, Xvec>, Xvec = (-2,-2,-2,3,3) on the
     role slots (c1,c2,c3,w1,w2); Y = X/6 (CarrierData.lean /
     Hypercharge.lean base charges -1/3 = -2/6 and 1/2 = 3/6).  For a
     traceless Xvec and a chirality-16 root, X = sum_{i in S} X_i.
  *  Everything exact (int / Fraction); zero floats anywhere; no RNG
     except the frozen-seed LCG of control C2; fully deterministic.

FIREWALL: experiments/tfpt-discovery probe; writes nothing; touches no
verification/, paper, ledger, changelog or website surface; NO physics
promotion claim in either direction -- this probe only decides whether
the code->matter reading MAY be considered for promotion later.

Sources (read-only): verification/v752_projective_hamming_incidence.py
(machinery, census, chi_NSR, y0 = FSUM), v1_e8_glue.py / v47_selection_
theorem.py (D5(+)A3 rep-level), v753_ramified_polarity.py (28-form
census for control C3), TfptCarrier/CarrierData.lean + Hypercharge.lean
(base charges), note_e8_gaussian_code.tex (bridge theorems).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gaussian_class_d5_purity_probe.py
"""

import hashlib
import itertools
import time
from collections import Counter
from fractions import Fraction as Fr

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ======================================================================
# S0: THE FROZEN PREDICTION -- hashed BEFORE any root data is computed
# ======================================================================
FROZEN_SPEC = """\
ARF-COMPILER PRIORITY-2 FROZEN PREDICTION (gaussian_class_d5_weight_purity)
frozen 2026-08-05, BEFORE computing any root data in this run.

Charge vector (primitive, traceless, five role slots (c1,c2,c3,w1,w2)):
    X = (-2, -2, -2, 3, 3),    hypercharge Y = X/6.

Class dictionary: v752 family/anchor basis (F1,F2,F3,A) of V = L/(1+i)L;
predicted state = even plus-set S of the normalized D5 half-spinor
weight; the table is the unique F2-LINEAR map determined by
F_i |-> {c_i, w1} and A |-> {w1, w2} (symmetric difference = addition):

    class 0          -> nu^c       S = {}                 X =  0
    A                -> e^c        S = {w1,w2}            X =  6
    F_i        (x3)  -> Q_L upper  S = {c_i,w1}           X =  1
    F_i+A      (x3)  -> Q_L lower  S = {c_i,w2}           X =  1
    F_i+F_j    (x3)  -> u^c        S = {c_i,c_j}          X = -4
    F_i+F_j+A  (x3)  -> d^c        S = {c_i,c_j,w1,w2}    X =  2
    F1+F2+F3         -> nu_L       S = {c1,c2,c3,w1}      X = -3
    F1+F2+F3+A       -> e_L        S = {c1,c2,c3,w2}      X = -3

SUCCESS CRITERION (strict, frozen; per nonzero class c):
  (i)   all 16 roots of c are SPINOR-SIDE ((16,4) or (16bar,4bar)) --
        no D5-adjoint, A3-adjoint or (10_v,6) root in the class;
  (ii)  conjugate pairing: the 16 roots form the 8 pairs {r, -r};
        exactly 8 roots have D5-chirality 16 (particle copies) and 8
        have 16bar (antiparticle copies) -- this is how the 16 roots
        map onto particle (+) antiparticle: 8 + 8, r <-> -r;
  (iii) the 8 chirality-16 roots ALL carry the single predicted weight
        S(c) (hence X(c)); the 8 chirality-16bar roots carry -S(c)
        (hence -X(c)).
  Class 0 must stay empty on roots (nu^c sterile).
  SUCCESS of a convention = (i)-(iii) for ALL 15 nonzero classes.

CONVENTION SPACE (all defensible discrete choices; scanned exhaustively):
  split: 56 coordinate D5-blocks D (5-subsets of {0..7}); canonical
         reporting split D = (0,2,4,6,7) (sigma-stable);
  slot assignment: ordered weak pair (w1,w2) among the 5 slots (x20),
         colour order on the remaining 3 (x6);
  chirality: which D5 parity is "16" (x2; canonical cc = 1).

VERDICT RULE (frozen):
  ROOTCLASS-PURE      : every one of the 56 splits admits an assignment
                        making all 15 classes pure per the table;
  ROOTCLASS-CONVENTION-AMBIGUOUS : at least one but not all splits do;
  ROOTCLASS-MIXED     : no scanned convention does;
  TEST-VOID           : a must-fail control does not fire.

MUST-FAIL CONTROLS (frozen):
  C1 wrong charge vector: X' = (-2,-2,-2,3,4) (non-traceless) and
     X'' = 2X (non-primitive) must break the frozen X column and the
     root-level identity X(root) = X(S_norm);
  C2 scrambled class assignment: a deterministic LCG shuffle (seed
     20260805) of the 240 root labels must destroy the measured class
     structure (NS/R sector purity per class and +-pair symmetry);
  C3 wrong symplectic form: of the 28 nondegenerate alternating forms
     on V (v753 census), every form except the canonical hbar must
     break the canonical pairing package (sigma-invariance AND
     B(., y0) = chi_NSR with y0 = the coordinate class FSUM).
"""

section("S0: SHA-freeze of the prediction table and all conventions")
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
print("(table, criterion, convention space, verdict rule, controls all")
print(" frozen in the hashed block; root data computed only below)")

# frozen X on role slots (c1,c2,c3,w1,w2)
XVEC = (-2, -2, -2, 3, 3)

# frozen table as (nF, bA) -> (state name, X); subsets via linear masks
STATE_NAME = {(0, 0): "nu^c", (0, 1): "e^c",
              (1, 0): "Q_L upper", (1, 1): "Q_L lower",
              (2, 0): "u^c", (2, 1): "d^c",
              (3, 0): "nu_L", (3, 1): "e_L"}
STATE_X = {(0, 0): 0, (0, 1): 6, (1, 0): 1, (1, 1): 1,
           (2, 0): -4, (2, 1): 2, (3, 0): -3, (3, 1): -3}


def phi_subset(bits, role_pos):
    """frozen linear dictionary: bits (b1,b2,b3,bA) -> plus-set mask over
    the 5 D-positions; role_pos = positions of (c1,c2,c3,w1,w2) in D."""
    c1, c2, c3, w1, w2 = role_pos
    m = 0
    if bits[0]:
        m ^= (1 << c1) | (1 << w1)
    if bits[1]:
        m ^= (1 << c2) | (1 << w1)
    if bits[2]:
        m ^= (1 << c3) | (1 << w1)
    if bits[3]:
        m ^= (1 << w1) | (1 << w2)
    return m


def x_of_mask(mask, role_pos, xvec):
    """X(S) = sum_{i in S} X_i in role coordinates (traceless xvec)."""
    inv = [None] * 5
    for role, pos in enumerate(role_pos):
        inv[pos] = xvec[role]
    return sum(inv[p] for p in range(5) if (mask >> p) & 1)


# internal consistency of the frozen table (no root data touched)
ID_ROLE = (0, 1, 2, 3, 4)
all_bits = list(itertools.product((0, 1), repeat=4))
masks = {b: phi_subset(b, ID_ROLE) for b in all_bits}
ok_even = all(bin(m).count("1") % 2 == 0 for m in masks.values())
ok_dist = len(set(masks.values())) == 16
ok_x = all(x_of_mask(masks[b], ID_ROLE, XVEC)
           == STATE_X[(b[0] + b[1] + b[2], b[3])] for b in all_bits)
check("S0.1 frozen dictionary internally consistent: 16 distinct EVEN "
      "plus-sets, F2-linear, X column reproduced by X(S) = sum_{i in S} "
      "X_i for all 16 classes", ok_even and ok_dist and ok_x)
check("S0.2 frozen charge vector primitive and traceless: sum X = 0, "
      "gcd = 1, Y = X/6 = (-1/3 x3, 1/2 x2) (CarrierData/Hypercharge "
      "base charges)",
      sum(XVEC) == 0
      and all(Fr(x, 6) in (Fr(-1, 3), Fr(1, 2)) for x in XVEC))

# ======================================================================
# v752 machinery (VERBATIM: mat_det_inv, row_hnf, hnf_reduce, J_vec,
# sig_vec, add_vec, ip, make_lattice, label_group, family_anchor_basis,
# standard doubled model, parity, herm_std, hbar_std)
# ======================================================================


def mat_det_inv(rows):
    n = len(rows)
    A = [[Fr(v) for v in r] for r in rows]
    I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        if piv is None:
            return Fr(0), None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            I[col], I[piv] = I[piv], I[col]
            det = -det
        det *= A[col][col]
        inv = 1 / A[col][col]
        A[col] = [a * inv for a in A[col]]
        I[col] = [a * inv for a in I[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                I[r] = [a - f * b for a, b in zip(I[r], I[col])]
    return det, I


def vec_mat(x, M):
    n = len(M)
    return tuple(sum(x[i] * M[i][j] for i in range(n)) for j in range(n))


def row_hnf(rows):
    M = [list(map(int, r)) for r in rows]
    m = len(M)
    for col in range(m):
        piv = next(r for r in range(col, m) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, m):
            while M[r][col] != 0:
                q = M[col][col] // M[r][col]
                M[col] = [a - q * b for a, b in zip(M[col], M[r])]
                M[col], M[r] = M[r], M[col]
        if M[col][col] < 0:
            M[col] = [-a for a in M[col]]
    return M


def hnf_reduce(c, H):
    c = list(c)
    for i in range(len(H)):
        q = c[i] // H[i][i]
        if q:
            c = [a - q * b for a, b in zip(c, H[i])]
    return tuple(c)


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def add_vec(x, y):
    return tuple(a + b for a, b in zip(x, y))


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


def make_lattice(in_lat, basis_rows):
    det, Binv = mat_det_inv(basis_rows)
    lat = {"in": in_lat, "B": basis_rows, "det": det, "Binv": Binv}

    def coords(x):
        c = vec_mat(x, Binv)
        assert all(v.denominator == 1 for v in c), "kein Gittervektor"
        return tuple(int(v) for v in c)

    A = [coords(add_vec(b, J_vec(b))) for b in basis_rows]
    H = row_hnf(A)
    lat["coords"] = coords
    lat["A"] = A
    lat["H"] = H
    lat["label"] = lambda x: hnf_reduce(coords(x), H)
    return lat


def label_group(lat):
    reps = {hnf_reduce((0,) * 8, lat["H"]): (0,) * 8}
    frontier = [(0,) * 8]
    while frontier:
        v = frontier.pop()
        for b in lat["B"]:
            w = add_vec(v, b)
            l = lat["label"](w)
            if l not in reps:
                reps[l] = w
                frontier.append(w)
    return reps


def family_anchor_basis(lat, reps, zero_label, sig_label_fn):
    fixed_labels = [lb for lb in reps if sig_label_fn(lb) == lb]
    fam_basis = None
    for lb in reps:
        if lb == zero_label or sig_label_fn(lb) == lb:
            continue
        o1 = lb
        o2 = sig_label_fn(lb)
        o3 = sig_label_fn(o2)
        s = lat["label"](add_vec(add_vec(reps[o1], reps[o2]), reps[o3]))
        if s == zero_label:
            continue
        span3 = set()
        for bits in itertools.product((0, 1), repeat=3):
            w = (0,) * 8
            for bit, l2 in zip(bits, (o1, o2, o3)):
                if bit:
                    w = add_vec(w, reps[l2])
            span3.add(lat["label"](w))
        if len(span3) != 8:
            continue
        anchor = next(l2 for l2 in fixed_labels
                      if l2 != zero_label and l2 not in span3)
        fam_basis = (o1, o2, o3, anchor, s)
        break
    assert fam_basis is not None
    o1, o2, o3, anc, fsum = fam_basis
    bits_of = {}
    for bits in itertools.product((0, 1), repeat=4):
        v = (0,) * 8
        for bit, l2 in zip(bits, (o1, o2, o3, anc)):
            if bit:
                v = add_vec(v, reps[l2])
        bits_of[lat["label"](v)] = bits
    return fam_basis, bits_of


def in_E8_std(x):
    par = {v % 2 for v in x}
    return len(par) == 1 and sum(x) % 4 == 0


B_STD = [(4, 0, 0, 0, 0, 0, 0, 0),
         (-2, 2, 0, 0, 0, 0, 0, 0),
         (0, -2, 2, 0, 0, 0, 0, 0),
         (0, 0, -2, 2, 0, 0, 0, 0),
         (0, 0, 0, -2, 2, 0, 0, 0),
         (0, 0, 0, 0, -2, 2, 0, 0),
         (0, 0, 0, 0, 0, -2, 2, 0),
         (1, 1, 1, 1, 1, 1, 1, 1)]


def parity(w):
    return w[0] % 2                      # 0 = integer/NS, 1 = spinor/R


def herm_std(w, v):
    re4, im4 = ip(w, v), ip(w, J_vec(v))
    assert re4 % 4 == 0 and im4 % 4 == 0
    return (re4 // 4, im4 // 4)


def hbar_std(w, v):
    h = herm_std(w, v)
    return (h[0] + h[1]) % 2


# ======================================================================
# S1: the v752 state in the standard doubled model
# ======================================================================
section("S1: v752 state re-established (standard doubled model, verbatim)")

LATS = make_lattice(in_E8_std, list(B_STD))
ZEROS = LATS["label"]((0,) * 8)
roots_std = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        roots_std.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        roots_std.append(v)
REPS_S = label_group(LATS)
rl_std = {r: LATS["label"](r) for r in roots_std}
census_s = Counter(rl_std.values())
check("S1.1 census 15 x 16, zero class EMPTY on roots (nu^c sterile per "
      "the frozen table): %d classes, sizes %s, zero-class roots %d"
      % (len(census_s), sorted(set(census_s.values())),
         census_s.get(ZEROS, 0)),
      len(census_s) == 15 and sorted(census_s.values()) == [16] * 15
      and ZEROS not in census_s)


def sig_label_s(lb):
    return LATS["label"](sig_vec(REPS_S[lb]))


FAM_S, BITS_S = family_anchor_basis(LATS, REPS_S, ZEROS, sig_label_s)
F1S, F2S, F3S, ANCS, FSUMS = FAM_S
BASE = [F1S, F2S, F3S, ANCS]
LBL_OF_BITS = {v: k for k, v in BITS_S.items()}

# NS/R parity per class (v752 P5.1/P5.2)
class_par = {}
pure_nsr = True
for r, lb in rl_std.items():
    p = parity(r)
    if lb in class_par and class_par[lb] != p:
        pure_nsr = False
    class_par[lb] = p
n_ns = sum(1 for lb in class_par if class_par[lb] == 0)
n_r = sum(1 for lb in class_par if class_par[lb] == 1)
check("S1.2 NS/R purity per class (v752 P5.1): every class is all-integer "
      "or all-spinor; 7 NS classes (112 integer roots) + 8 R classes "
      "(128 spinor roots)",
      pure_nsr and n_ns == 7 and n_r == 8)

# +- pair symmetry: -r = r mod (1+i)L (2 = -i (1+i)^2)
ok_neg = all(rl_std[tuple(-a for a in r)] == rl_std[r] for r in roots_std)
check("S1.3 conjugate pairing carrier: -r is in the SAME class as r for "
      "all 240 roots (2 = -i(1+i)^2) => each class = 8 pairs {r,-r}",
      ok_neg)

chi = {lb: class_par[lb] for lb in class_par}
chi[ZEROS] = 0
chi_vec = tuple(chi[b] for b in BASE)
ok_chi_lin = all(chi[LBL_OF_BITS[b]]
                 == (sum(x * y for x, y in zip(b, chi_vec)) % 2)
                 for b in all_bits)
G4 = [[hbar_std(REPS_S[bi], REPS_S[bj]) for bj in BASE] for bi in BASE]
ok_g_repr = all(hbar_std(REPS_S[LBL_OF_BITS[a]], REPS_S[LBL_OF_BITS[b]])
                == (sum(a[i] * G4[i][j] * b[j] for i in range(4)
                        for j in range(4)) % 2)
                for a in all_bits for b in all_bits)
y0bits = BITS_S[FSUMS]
ok_y0 = all((sum(G4[i][j] * y0bits[j] for j in range(4)) % 2) == chi_vec[i]
            for i in range(4))
check("S1.4 chi_NSR linear with coefficients %s in (F1,F2,F3,A); hbar "
      "Gram G4 reproduces hbar on all 256 label pairs; chi = hbar(., y0) "
      "with y0 = FSUM (bits %s) -- v752 P5.3 re-derived"
      % (chi_vec, y0bits), ok_chi_lin and ok_g_repr and ok_y0)

# sigma structure
sig_bits = [BITS_S[sig_label_s(b)] for b in BASE]
check("S1.5 sigma-bar: F1 -> F2 -> F3 -> F1, A fixed (family 3-cycle "
      "with anchor)",
      sig_label_s(F1S) == F2S and sig_label_s(F2S) == F3S
      and sig_label_s(F3S) == F1S and sig_label_s(ANCS) == ANCS)

root_list = sorted(roots_std)
cls_roots = {}
for r in root_list:
    cls_roots.setdefault(rl_std[r], []).append(r)

# ======================================================================
# split machinery
# ======================================================================


def analyze_split(D):
    """per root: (sector, D5 halved weight (5 entries; spinor doubled
    +-1 = 2 x (+-1/2)), plus-mask for spinor roots)."""
    Dset = set(D)
    out = {}
    for r in root_list:
        if r[0] % 2 == 0:
            supp = [c for c in range(8) if r[c] != 0]
            nd = sum(1 for c in supp if c in Dset)
            dvec = tuple(r[c] // 2 for c in D)
            if nd == 2:
                sector = "D5adj"
            elif nd == 0:
                sector = "A3"
            else:
                sector = "V10x6"
            out[r] = (sector, dvec, None)
        else:
            dvec = tuple(r[c] for c in D)
            plus = 0
            for k in range(5):
                if dvec[k] == 1:
                    plus |= (1 << k)
            out[r] = ("S", dvec, plus)
    return out


def x_of_root(entry, role_pos, xvec):
    """exact hypercharge-x of one root: <halved D5 weight, Xvec>."""
    sector, dvec, plus = entry
    inv = [None] * 5
    for role, pos in enumerate(role_pos):
        inv[pos] = xvec[role]
    if sector == "S":
        return Fr(sum(dvec[k] * inv[k] for k in range(5)), 2)
    return Fr(sum(dvec[k] * inv[k] for k in range(5)), 1)


def norm_pair(plus):
    """unordered weight pair {S, complement(S)} as canonical key."""
    comp = plus ^ 31
    return min(plus, comp), max(plus, comp)


def class_structure(info):
    """per class: sector census, spinor pair census, all-spinor flag,
    single-pair flag."""
    struct = {}
    for lb, roots in cls_roots.items():
        sec = Counter(e[0] for e in (info[r] for r in roots))
        pairs = Counter(norm_pair(info[r][2]) for r in roots
                        if info[r][0] == "S")
        struct[lb] = (sec, pairs)
    return struct


def mask_str(mask, role_pos):
    names = [None] * 5
    for role, pos in enumerate(role_pos):
        names[pos] = ("c1", "c2", "c3", "w1", "w2")[role]
    got = [names[p] for p in range(5) if (mask >> p) & 1]
    return "{" + ",".join(got) + "}" if got else "{}"


def state_of_mask(mask, role_pos):
    """SM state name of an even plus-set under an assignment."""
    inv = [None] * 5
    for role, pos in enumerate(role_pos):
        inv[pos] = role
    roles = [inv[p] for p in range(5) if (mask >> p) & 1]
    nc = sum(1 for x in roles if x < 3)
    nw = sum(1 for x in roles if x >= 3)
    if (nc + nw) % 2 == 1:
        return "(odd subset: 5/5bar-type)"
    if (nc, nw) == (0, 0):
        return "nu^c"
    if (nc, nw) == (0, 2):
        return "e^c"
    if (nc, nw) == (1, 1):
        return "Q_L upper" if 3 in roles else "Q_L lower"
    if (nc, nw) == (2, 0):
        return "u^c"
    if (nc, nw) == (2, 2):
        return "d^c"
    if (nc, nw) == (3, 1):
        return "nu_L" if 3 in roles else "e_L"
    return "?"


def gate_class(lb, info, role_pos, cc):
    """strict frozen criterion (i)-(iii) for one class; returns
    (pure?, reason)."""
    bits = BITS_S[lb]
    roots = cls_roots[lb]
    secs = Counter(info[r][0] for r in roots)
    if set(secs) != {"S"}:
        return False, "adjoint-side roots present: %s" % dict(secs)
    pred = phi_subset(bits, role_pos)
    n16 = n16b = 0
    for r in roots:
        plus = info[r][2]
        nminus = 5 - bin(plus).count("1")
        if nminus % 2 == cc % 2:
            n16 += 1
            if plus != pred:
                return False, ("chirality-16 weight %s != predicted %s"
                               % (mask_str(plus, role_pos),
                                  mask_str(pred, role_pos)))
        else:
            n16b += 1
            if (plus ^ 31) != pred:
                return False, ("chirality-16bar weight conj %s != "
                               "predicted %s"
                               % (mask_str(plus ^ 31, role_pos),
                                  mask_str(pred, role_pos)))
    if (n16, n16b) != (8, 8):
        return False, "chirality split %d/%d != 8/8" % (n16, n16b)
    return True, "pure"


# ======================================================================
# S2: canonical convention -- the full 15-class table
# ======================================================================
section("S2: canonical convention (sigma-stable split D = (0,2,4,6,7), "
        "roles (c1,c2,c3,w1,w2) in order, cc = 1) -- the full table")

CANON_D = (0, 2, 4, 6, 7)
CANON_ROLE = (0, 1, 2, 3, 4)
CANON_CC = 1
info_c = analyze_split(CANON_D)

sec_tot = Counter(info_c[r][0] for r in root_list)
check("S2.1 D5(+)A3 branching from root data: sector census %s = "
      "40 (45 of D5) + 12 ((1,15) of A3) + 60 ((10_v,6)) + 128 "
      "((16,4)+(16bar,4bar)) -- matches the v1/v47 rep bookkeeping "
      "(45+15+60+64+64 = 248 with the 8 Cartan)"
      % dict(sec_tot),
      sec_tot == Counter({"S": 128, "V10x6": 60, "D5adj": 40, "A3": 12}))

# sigma-equivariance of the canonical split (canonicity argument)
sig_pos = {0: 1, 1: 2, 2: 0, 3: 3, 4: 4}   # coords 0->2->4 cycle, 6,7 fix


def rot_mask(m):
    out = 0
    for p in range(5):
        if (m >> p) & 1:
            out |= (1 << sig_pos[p])
    return out


ok_sig_split = True
for r in root_list:
    rs = sig_vec(r)
    if info_c[r][0] != info_c[rs][0]:
        ok_sig_split = False
        break
    if info_c[r][0] == "S" and rot_mask(info_c[r][2]) != info_c[rs][2]:
        ok_sig_split = False
        break
check("S2.2 canonical split is sigma-EQUIVARIANT: sigma preserves every "
      "sector and rotates the colour slots c1 -> c2 -> c3 (w1, w2 fixed) "
      "on the spinor weights -- the family 3-cycle acts exactly like the "
      "frozen dictionary demands", ok_sig_split)

# the deliverable table
struct_c = class_structure(info_c)
order = sorted((lb for lb in census_s),
               key=lambda lb: (sum(BITS_S[lb][:3]), BITS_S[lb][3],
                               BITS_S[lb]))
print()
print("THE 15-CLASS TABLE (canonical convention; predicted vs measured)")
print("-" * 78)
n_pure_canon = 0
mix_report = []
for lb in order:
    bits = BITS_S[lb]
    nF = sum(bits[:3])
    name_parts = [n for n, b in zip(("F1", "F2", "F3", "A"), bits) if b]
    cname = "+".join(name_parts) if name_parts else "0"
    pred_mask = phi_subset(bits, CANON_ROLE)
    pred_name = STATE_NAME[(nF, bits[3])]
    pred_x = STATE_X[(nF, bits[3])]
    sec, pairs = struct_c[lb]
    xs = Counter(x_of_root(info_c[r], CANON_ROLE, XVEC)
                 for r in cls_roots[lb])
    pure, reason = gate_class(lb, info_c, CANON_ROLE, CANON_CC)
    if pure:
        n_pure_canon += 1
    else:
        mix_report.append((cname, reason))
    nsr = "R " if chi[lb] else "NS"
    print("class %-11s bits %s  [%s]  %d roots" %
          (cname, "".join(map(str, bits)), nsr, len(cls_roots[lb])))
    print("  predicted : %-10s S = %-15s X = %+d  (Y = %s)"
          % (pred_name, mask_str(pred_mask, CANON_ROLE), pred_x,
             Fr(pred_x, 6)))
    print("  sectors   : %s" % dict(sec))
    if pairs:
        pl = ", ".join("%s|%s x%d (%s)" %
                       (mask_str(a, CANON_ROLE), mask_str(b, CANON_ROLE),
                        n, state_of_mask(max(a, b) if
                                         bin(a).count("1") % 2 else a,
                                         CANON_ROLE))
                       for (a, b), n in sorted(pairs.items()))
        print("  16-weights: %s" % pl)
    if sec.get("D5adj") or sec.get("V10x6") or sec.get("A3"):
        orb = Counter()
        for r in cls_roots[lb]:
            s, dvec, _ = info_c[r]
            if s == "D5adj":
                nz = [v for v in dvec if v]
                typ = "24" if nz[0] * nz[1] < 0 else \
                      ("10" if nz[0] > 0 else "10bar")
            elif s == "V10x6":
                nz = [v for v in dvec if v]
                typ = ("(5v,6)" if nz and nz[0] > 0 else
                       "(5vbar,6)" if nz else "(6 only)")
            else:
                typ = "(1,15)"
            orb[(typ, x_of_root(info_c[r], CANON_ROLE, XVEC))] += 1
        print("  adj orbits: %s"
              % ", ".join("%s X=%s x%d" % (t, x, n)
                          for (t, x), n in sorted(orb.items(),
                                                  key=lambda kv:
                                                  str(kv[0]))))
    print("  X census  : {%s}"
          % ", ".join("%s: %d" % (x, n) for x, n in sorted(xs.items())))
    print("  verdict   : %s%s" % ("PURE" if pure else "MIXED",
                                  "" if pure else "  -- " + reason))
    print("-" * 78)

check("S2.3 strict frozen gate under the CANONICAL convention: %d / 15 "
      "classes pure" % n_pure_canon, True,
      "purity count is a measurement, not a pass/fail check")

# ======================================================================
# S3: exhaustive convention scan (56 splits x assignments x chirality)
# ======================================================================
section("S3: convention scan -- all 56 coordinate splits, all slot "
        "assignments, both chiralities")

n_spin128 = sum(1 for r in root_list if r[0] % 2)
check("S3.1 embedding-INDEPENDENT counting bound: EVERY D5(+)A3 c E8 "
      "has exactly 128 spinor-side roots; 15 x 16 = 240 > 128, so at "
      "most 8 of the 15 classes can be all-spinor for ANY embedding "
      "(coordinate or not) -- the strict gate can never reach 15/15",
      n_spin128 == 128 and 128 // 16 == 8)

split_stats = []
passing_splits = []
for D in itertools.combinations(range(8), 5):
    info = analyze_split(D)
    struct = class_structure(info)
    n_allspin = 0
    n_single = 0
    for lb in census_s:
        sec, pairs = struct[lb]
        if set(sec) == {"S"}:
            n_allspin += 1
            if len(pairs) == 1:
                n_single += 1
    split_stats.append((D, n_allspin, n_single))
    if n_single == 15:
        # only then can any assignment match the frozen table
        for wpair in itertools.permutations(range(5), 2):
            rest = [p for p in range(5) if p not in wpair]
            for cperm in itertools.permutations(rest):
                role_pos = (cperm[0], cperm[1], cperm[2],
                            wpair[0], wpair[1])
                for cc in (0, 1):
                    if all(gate_class(lb, info, role_pos, cc)[0]
                           for lb in census_s):
                        passing_splits.append((D, role_pos, cc))

allspin_census = Counter(s[1] for s in split_stats)
single_census = Counter(s[2] for s in split_stats)
print("    per-split census of ALL-SPINOR classes  : %s"
      % dict(sorted(allspin_census.items())))
print("    per-split census of single-weight classes: %s"
      % dict(sorted(single_census.items())))
check("S3.2 scan result: %d of 56 splits admit ANY assignment with all "
      "15 classes pure per the frozen table; max all-spinor classes "
      "over all splits = %d (bound 8), max single-weight-pure = %d"
      % (len({d for d, _, _ in passing_splits}),
         max(s[1] for s in split_stats),
         max(s[2] for s in split_stats)), True,
      "measurement; verdict rule applied in S6")

# ======================================================================
# S4: the structure actually measured (honest typing of the mixture)
# ======================================================================
section("S4: what the classes REALLY carry (canonical convention)")

# R classes: weight-pair incidence
pair_to_classes = {}
for lb in census_s:
    if chi[lb] == 0:
        continue
    for pr, n in struct_c[lb][1].items():
        pair_to_classes.setdefault(pr, []).append((BITS_S[lb], n))
pair_mult = sorted(len(v) for v in pair_to_classes.values())
per_class_pairs = sorted(len(struct_c[lb][1])
                         for lb in census_s if chi[lb] == 1)
check("S4.1 R-side fine structure: %d distinct 16-weight pairs over the "
      "8 spinor classes; pairs per class %s; classes per pair %s"
      % (len(pair_to_classes), dict(Counter(per_class_pairs)),
         dict(Counter(pair_mult))), True, "measurement")

# does the frozen linear dictionary phi match the spinor roots at all?
best_match = -1
best_conv = None
for wpair in itertools.permutations(range(5), 2):
    rest = [p for p in range(5) if p not in wpair]
    for cperm in itertools.permutations(rest):
        role_pos = (cperm[0], cperm[1], cperm[2], wpair[0], wpair[1])
        for cc in (0, 1):
            n_match = 0
            for r in root_list:
                if info_c[r][0] != "S":
                    continue
                plus = info_c[r][2]
                nminus = 5 - bin(plus).count("1")
                s_norm = plus if nminus % 2 == cc % 2 else plus ^ 31
                if s_norm == phi_subset(BITS_S[rl_std[r]], role_pos):
                    n_match += 1
            if n_match > best_match:
                best_match = n_match
                best_conv = (role_pos, cc)
check("S4.2 best-case match of the frozen linear dictionary phi on the "
      "128 spinor roots, over ALL 240 assignments of the canonical "
      "split: %d / 128 (role_pos %s, cc %d)"
      % (best_match, best_conv[0], best_conv[1]), True, "measurement")

# X-only weakened purity (typed secondary -- NOT the gate)
n_xpure = 0
for lb in census_s:
    bits = BITS_S[lb]
    px = STATE_X[(sum(bits[:3]), bits[3])]
    xs = set(x_of_root(info_c[r], CANON_ROLE, XVEC) for r in cls_roots[lb])
    if xs <= {Fr(px), Fr(-px)}:
        n_xpure += 1
check("S4.3 SECONDARY (not the gate): classes whose full X census lies "
      "in {+X_pred, -X_pred} under the canonical convention: %d / 15"
      % n_xpure, True, "measurement")

# ======================================================================
# S5: must-fail controls
# ======================================================================
section("S5: must-fail controls (all three must fire)")

# C1 -- wrong charge vectors
XP = (-2, -2, -2, 3, 4)          # non-traceless
XPP = tuple(2 * x for x in XVEC)  # non-primitive
col_ok = all(x_of_mask(masks[b], ID_ROLE, XVEC)
             == STATE_X[(b[0] + b[1] + b[2], b[3])] for b in all_bits)
col_p = [b for b in all_bits
         if x_of_mask(masks[b], ID_ROLE, XP)
         != STATE_X[(b[0] + b[1] + b[2], b[3])]]
col_pp = [b for b in all_bits
          if x_of_mask(masks[b], ID_ROLE, XPP)
          != STATE_X[(b[0] + b[1] + b[2], b[3])]]
# root-level: traceless identity X(root) = X(S_norm) breaks for XP
root_break = 0
for r in root_list:
    if info_c[r][0] != "S":
        continue
    plus = info_c[r][2]
    nminus = 5 - bin(plus).count("1")
    s_norm = plus if nminus % 2 == 1 else plus ^ 31
    xr = x_of_root(info_c[r], CANON_ROLE, XP)
    xs_pred = x_of_mask(s_norm, CANON_ROLE, XP)
    sign = 1 if nminus % 2 == 1 else -1
    if xr != sign * Fr(xs_pred) or xr.denominator != 1:
        root_break += 1
check("S5.1 C1 FIRES: non-traceless X' breaks %d/16 frozen X rows and "
      "the root identity X(root) = +-X(S) on %d/128 spinor roots "
      "(half-integer charges appear); non-primitive 2X breaks %d/16 "
      "rows; the true X reproduces all 16 (%s)"
      % (len(col_p), root_break, len(col_pp), col_ok),
      col_ok and len(col_p) > 0 and root_break > 0 and len(col_pp) > 0)

# C2 -- scrambled class assignment (frozen-seed LCG shuffle)


def lcg_shuffle(n, seed):
    s = seed
    idx = list(range(n))
    for i in range(n - 1, 0, -1):
        s = (s * 6364136223846793005 + 1442695040888963407) % 2 ** 64
        j = s % (i + 1)
        idx[i], idx[j] = idx[j], idx[i]
    return idx


perm240 = lcg_shuffle(240, 20260805)
labels_true = [rl_std[r] for r in root_list]
scram = {root_list[i]: labels_true[perm240[i]] for i in range(240)}
scram_par_pure = True
seen_par = {}
for r in root_list:
    lb = scram[r]
    p = parity(r)
    if lb in seen_par and seen_par[lb] != p:
        scram_par_pure = False
        break
    seen_par[lb] = p
scram_neg = all(scram[tuple(-a for a in r)] == scram[r]
                for r in root_list)
check("S5.2 C2 FIRES: LCG-scrambled root->class map (seed 20260805) "
      "destroys NS/R sector purity per class (pure: %s) and the "
      "+-pair symmetry (intact: %s) -- the measured structure is a "
      "property of the TRUE Gaussian reduction, not of any 15 x 16 "
      "partition" % (scram_par_pure, scram_neg),
      (not scram_par_pure) and (not scram_neg))

# C3 -- wrong symplectic form (v753 census: 28 nondegenerate alternating)


def f2_rank4(M):
    A = [row[:] for row in M]
    rank = 0
    for col in range(4):
        piv = next((r for r in range(rank, 4) if A[r][col]), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(4):
            if r != rank and A[r][col]:
                A[r] = [(a + b) % 2 for a, b in zip(A[r], A[rank])]
        rank += 1
    return rank


S2M = [list(BITS_S[sig_label_s(b)]) for b in BASE]   # rows = sigma(base)
forms = []
for bitsel in range(64):
    M = [[0] * 4 for _ in range(4)]
    idx = 0
    for i in range(4):
        for j in range(i + 1, 4):
            M[i][j] = M[j][i] = (bitsel >> idx) & 1
            idx += 1
    if f2_rank4(M) == 4:
        forms.append(M)
G4L = [list(row) for row in G4]
n_forms = len(forms)
assert G4L in forms


def form_val(M, a, b):
    return sum(a[i] * M[i][j] * b[j] for i in range(4)
               for j in range(4)) % 2


def sig_bits_vec(x):
    return tuple(sum(x[i] * S2M[i][j] for i in range(4)) % 2
                 for j in range(4))


def package(M):
    """canonical pairing package: sigma-invariance AND B(., y0) = chi."""
    sig_inv = all(form_val(M, sig_bits_vec(a), sig_bits_vec(b))
                  == form_val(M, a, b)
                  for a in all_bits for b in all_bits)
    slice_ok = all(form_val(M, a, y0bits)
                   == (sum(x * y for x, y in zip(a, chi_vec)) % 2)
                   for a in all_bits)
    return sig_inv, slice_ok


ok_canon = package(G4L)
n_sig_inv = 0
n_slice = 0
n_both = 0
for M in forms:
    if M == G4L:
        continue
    si, sl = package(M)
    n_sig_inv += si
    n_slice += sl
    n_both += (si and sl)
check("S5.3 C3 FIRES: of the %d nondegenerate alternating forms on V "
      "(v753 census: 28), the canonical hbar satisfies the pairing "
      "package (sigma-invariant AND B(., y0=FSUM) = chi_NSR: %s); of "
      "the %d WRONG forms, %d are sigma-invariant, %d match the chi "
      "slice, and %d satisfy BOTH -- every wrong form breaks the "
      "package" % (n_forms, ok_canon, n_forms - 1, n_sig_inv,
                   n_slice, n_both),
      n_forms == 28 and ok_canon == (True, True) and n_both == 0)

# ======================================================================
# S6: verdict (frozen rule)
# ======================================================================
section("S6: VERDICT (frozen enum: ROOTCLASS-PURE / ROOTCLASS-MIXED / "
        "ROOTCLASS-CONVENTION-AMBIGUOUS; TEST-VOID on control failure)")

controls_fire = all(ok for name, ok in CHECKS if name.startswith("S5."))
splits_passing = {d for d, _, _ in passing_splits}
if not controls_fire:
    verdict = "TEST-VOID"
elif len(splits_passing) == 56:
    verdict = "ROOTCLASS-PURE"
elif len(splits_passing) > 0:
    verdict = "ROOTCLASS-CONVENTION-AMBIGUOUS"
else:
    verdict = "ROOTCLASS-MIXED"

n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
print("VERDICT: %s" % verdict)
if verdict == "ROOTCLASS-MIXED":
    print()
    print("CONSEQUENCE (stated plainly):")
    print("  * The matter-classifier reading of the Gaussian classes is")
    print("    DEAD at root level: no scanned D5(+)A3 / SU(5) convention")
    print("    makes even one full set of 15 classes pure per the frozen")
    print("    table, and the 128-spinor-root counting bound kills the")
    print("    strict gate for EVERY D5(+)A3 embedding, coordinate or")
    print("    not (>= 7 classes always contain adjoint-side roots).")
    print("  * The Arf compiler keeps its mathematics (v752/v753")
    print("    structures untouched: census, symplectic form, polarity,")
    print("    NS/R point) -- but the code->matter table of this")
    print("    prediction must NOT enter any main claim, and the")
    print("    'genuine matter classifier' phrasing is falsified in")
    print("    this root-level form.")
    print("  * Mixed classes (canonical convention): %d of 15; first"
          % (15 - n_pure_canon))
    for cname, reason in mix_report[:3]:
        print("      %s: %s" % (cname, reason))
elif verdict == "ROOTCLASS-PURE":
    print()
    print("CONSEQUENCE: the code layer IS a matter classifier at root")
    print("level under every scanned convention; promotion remains a")
    print("SEPARATE decision (this probe makes no physics claim).")
elif verdict == "ROOTCLASS-CONVENTION-AMBIGUOUS":
    print()
    print("CONSEQUENCE: defensible conventions disagree; passing splits:")
    print("  %s" % sorted(splits_passing))
    print("The ambiguity itself is the finding; no promotion either way.")
print()
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS)
      else "CHECKS FAILED (%d)" % (len(CHECKS) - n_pass))


def run():
    return len(CHECKS) - n_pass


if __name__ == "__main__":
    raise SystemExit(0 if n_pass == len(CHECKS) else 1)
