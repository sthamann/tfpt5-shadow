#!/usr/bin/env python3
"""fano_disc7_bridge_probe -- REVIEW MODULE 6: the preregistered
FANO -> DISCRIMINANT(-7) bridge.

REVIEW HYPOTHESIS UNDER TEST (verbatim scope): "the finite ramified fiber
is a Fano geometry; the continuous transfer is its arithmetic lift with
discriminant -7."  Substrates: every hyperplane of the four-bit space
V = L/(1+i)L = F2^4 (v689/v722/v738) is projectively a Fano plane PG(2,2)
with 7 points; the F_transfer sheet-diamond path runs over the order
O = Z[(1+sqrt(-7))/2] as the norm line alpha_t = (4t+7+sqrt(-7))/2
= (2t+3) + omega (v533), with the v632 cross-ratio 4/3 on the Koide chain.

===========================================================================
PREREGISTRATION (frozen BEFORE any computation; review verbatim: an
EQUIVARIANT lift PG(2,2) -> O_{-7} -> PGL2 with FOUR binding conditions --
NO hit counts unless ALL FOUR hold; this is the anti-numerology clause).
===========================================================================

The four conditions AS KILL CRITERIA, with frozen operationalizations:

COND1 (sigma three-cycle preservation).  The Fano plane must carry a
  canonical order-3 automorphism that the lift maps onto the sigma-action
  of the transfer states.
  FROZEN: (i) code side: the canonical Fano plane is P = the 7 nonzero
  points of ker chi_par (the NS hyperplane -- canonical by the review's
  own NS/R naming, v722; must be sigma-invariant); sigma-bar restricted
  to P must be a NONTRIVIAL order-3 collineation.  (ii) arithmetic side:
  the canonical 7-structure and its canonical order-3 action must be
  CONSTRUCTED, not chosen: candidates are machine-censused (units /
  small-norm elements / ideals of norm <= 7 / the ramified residue field
  O/(sqrt(-7)) = F7); a candidate counts as canonical only if its Fano
  structure is invariant under the transfer translation x -> x + red(2)
  (the alpha-line step, v533) and its order-3 action commutes with the
  canonical arithmetic (norm, conjugation) resp. is the difference-set
  multiplier.  (iii) an incidence-preserving bijection Phi with
  Phi o sigma-bar = (canonical 3-cycle) o Phi must EXIST for every
  canonical model (the models come in a unit-conjugate pair; requiring
  a single model would be one free bit -- forbidden).  Exact counts
  recorded.  Any failure => KILLED at COND1.

COND2 (parity-bit preservation).  The NS/R character chi_par must have a
  lift invariant.  FROZEN candidate list (exhaustive-canonical; anything
  further would be a free construction, excluded by the anti-numerology
  clause; state-level invariants would need the COND3 correspondence and
  are excluded by the preregistered ORDER):
    (2a) norm parity nu = N mod 2 (the 2-adic bit; canonical because the
         J-endpoint norm 2 = |Z2| names the split place) factoring
         through the ramified fiber: exhaustive counterexample search in
         the box |a|,|b| <= 3.
    (2b) the canonical order-2 structure of the fiber itself -- the
         quadratic-residue character chi_7 (both bit conventions
         QR = 0 and QR = 1) -- pulled back along EVERY Phi from COND1
         must reproduce chi_par|P (which is identically 0 on P).
    (2c) an ideal-quotient realization of the parity-carrying spaces:
         chi_par lives on V = F2^4 (2-rank 4) with R-coset an affine
         F2^3 (2-rank 3); some O/I must realize 2-rank >= 3.  Machine
         census: ALL ideals of norm 8 and 16 (complete lists via
         p-adic factorization, h = 1), Smith invariants of each
         quotient, maximal 2-rank recorded.
  COND2 passes iff at least one candidate works.  Else KILLED at COND2.

COND3 (the four distinguished transfer states as canonical Fano objects).
  The chain J -> K -> C -> F on the norm line alpha_t = (2t+3) + omega,
  t = -2..1 (norms 2, 4, 14, 32) reduces into the fiber; the image
  4-set must BE a canonical Fano 4-substructure, IDENTICALLY in every
  canonical model (no free model choice).  FROZEN canonical 4-object
  types: (i) a frame / quadrilateral (= complement of a line; the only
  PGL-canonical 4-point class: no 3 collinear), or (ii) a full line
  plus THE canonical point (the unique fixed point of the canonical
  order-3 action), point external to the line.  Anything else, or a
  type that holds in one canonical model but not the other => KILLED.

COND4 (cross-ratio reconstruction).  The v632 cross-ratio 4/3 of the
  Koide chain must be reconstructible from Fano INCIDENCE.  FROZEN:
  (4a) functoriality witness: CR(red J, red K; red C, red F) computed in
  P^1(F7) must equal red(4/3) = 4 * inv(3) = 6 mod 7 (this is forced by
  functoriality of CR under reduction and is NOT yet reconstruction);
  (4b) reconstruction: over the FULL collineation stabilizer of the
  COND3 canonical structure inside the model's automorphism group
  (168 collineations, machine-enumerated), the cross-ratio of the
  permuted quadruple must be CONSTANT -- incidence data must determine
  the value.  If it varies, 4/3 is not incidence-reconstructible
  => KILLED.

ABORT DISCIPLINE (preregistered): the conditions are tested in the order
COND1 -> COND2 -> COND3 -> COND4, each exactly; the run ABORTS at the
first violation; later conditions are reported SKIPPED and do NOT score.
No hit without all four (review verbatim).

VERDICT ENUMS (frozen): FANO-DISC7-BRIDGE (all four hold; then the
theorem candidate "code geometry <-> transfer geometry" is to be
formulated) / FANO-DISC7-DECORATIVE (any kill; the seven-correlation is
decorative and is documented so, with the exact break point) /
SUBSTRATE-FAIL (a rebuilt corpus identity failed; no verdict).

MUST-FIRE CONTROLS (teeth): (C-a) replacing the order-3 multiplier by a
non-multiplier (x -> 3x) must yield ZERO equivariant lifts; (C-b) a
one-line-broken incidence structure must yield ZERO lifts; (C-c) the
ideal 7-census must REFUSE an order-3 symmetry (the compatible-3-cycle
count over all 5040 permutations must be 0).  A control that does not
fire invalidates the probe.

FIREWALL: experiments/tfpt-discovery probe; ONE new file; writes nothing;
no verification/, paper, ledger, changelog or website surface touched; a
kill is a valid, well-powered outcome; nothing here moves CONTRACT.F.01
markers.  Design typed [X].

SUBSTRATES REBUILT EXACTLY (not imported): the doubled-coordinate E8
(v722 frame: J = in-pair rotation, sigma = coordinate-pair 3-cycle
sig8), V = L/(1+i)L via F2 linear algebra on a machine-derived Z-basis,
chi_par = coordinate parity (v722), the 15 x 16 root census (v689), the
v533 norm line identities, the v632/v571 cross-ratio 4/3.

Predecessors (read-only): v533_ftransfer_disc7_norm.py,
v632_ftransfer_pgl2.py, v689_gaussian_code_bridge.py,
v722_phys_ramified_ns_r.py, v738_hecke_mod_ramified.py.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/fano_disc7_bridge_probe.py
"""

import time
from collections import Counter
from itertools import combinations, permutations, product

import sympy as sp

T0 = time.time()
CHECKS = []
CONTROLS_FIRED = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def info(name, detail=""):
    print("[INFO] %s%s" % (name, ("  -- " + detail) if detail else ""),
          flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ===========================================================================
# S0  code-side substrate: E8 doubled, V = L/(1+i)L, sigma-bar, chi_par
# ===========================================================================

def J8(w):
    return (-w[1], w[0], -w[3], w[2], -w[5], w[4], -w[7], w[6])


def sig8(w):
    return (w[4], w[5], w[0], w[1], w[2], w[3], w[6], w[7])


def in_L(w):
    par = {wi & 1 for wi in w}
    return len(par) == 1 and sum(w) % 4 == 0


def roots_E8():
    roots = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((2, -2), repeat=2):
            w = [0] * 8
            w[i], w[j] = si, sj
            roots.append(tuple(w))
    for signs in product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(signs)
    return roots


def z_row_basis(vectors):
    """Z-basis of the row span (integer echelon reduction, exact)."""
    rows = [list(v) for v in vectors]
    basis = []
    for col in range(8):
        while True:
            nz = [r for r in rows if r[col] != 0]
            if not nz:
                break
            piv = min(nz, key=lambda r: abs(r[col]))
            rows.remove(piv)
            new_rows = []
            for r in rows:
                if r[col] != 0:
                    q = r[col] // piv[col]
                    r = [ri - q * pi for ri, pi in zip(r, piv)]
                if any(r):
                    new_rows.append(r)
            rows = new_rows
            if any(r[col] != 0 for r in rows):
                rows.append(piv)
            else:
                basis.append(piv)
                break
    return basis


def f2_rowspace_basis(rows):
    rows = [list(r) for r in rows]
    basis, piv_cols = [], []
    for r in rows:
        r = r[:]
        for b, c in zip(basis, piv_cols):
            if r[c]:
                r = [(x ^ y) for x, y in zip(r, b)]
        nz = next((i for i, x in enumerate(r) if x), None)
        if nz is not None:
            basis.append(r)
            piv_cols.append(nz)
    return basis


def f2_nullspace(rows, n):
    """basis of {h in F2^n : r . h = 0 for all rows r}"""
    basis = f2_rowspace_basis(rows)
    piv = [next(i for i, x in enumerate(b) if x) for b in basis]
    free = [j for j in range(n) if j not in piv]
    # reduced echelon
    for k, b in enumerate(basis):
        for l, b2 in enumerate(basis):
            if l != k and b2[piv[k]]:
                basis[l] = [(x ^ y) for x, y in zip(b2, b)]
    out = []
    for j in free:
        h = [0] * n
        h[j] = 1
        for b, p in zip(basis, piv):
            if b[j]:
                h[p] = 1
        out.append(h)
    return out


section("S0  code-side substrate: V = L/(1+i)L, sigma-bar, chi_par (rebuilt)")

ROOTS = roots_E8()
check("S0.1 root census: 112 integer-type + 128 spinor-type = 240, all in L,"
      " |w|^2 = 8 (doubled)",
      len(ROOTS) == 240 and all(in_L(w) for w in ROOTS)
      and all(sum(x * x for x in w) == 8 for w in ROOTS),
      "240 roots")
check("S0.2 J and sigma are lattice automorphisms of the root set, "
      "[J, sigma] = 0, sigma^3 = id",
      set(map(J8, ROOTS)) == set(ROOTS) and set(map(sig8, ROOTS)) == set(ROOTS)
      and all(J8(sig8(w)) == sig8(J8(w)) for w in ROOTS[:40])
      and all(sig8(sig8(sig8(w))) == w for w in ROOTS[:40]))

B = z_row_basis(ROOTS)
MB = sp.Matrix(B)
DET_B = MB.det()
check("S0.3 machine-derived Z-basis of L: 8 rows, |det| = 256 "
      "(= covolume of doubled E8; certifies a genuine basis)",
      len(B) == 8 and abs(DET_B) == 256, "det = %d" % DET_B)

MBinv = MB.inv()


def coords(w):
    c = (sp.Matrix([list(w)]) * MBinv)
    cl = [sp.nsimplify(x) for x in c]
    assert all(x.is_Integer for x in cl), "non-integral coords"
    return [int(x) for x in cl]


K_ROWS = [[c % 2 for c in coords(tuple(b[i] + J8(b)[i] for i in range(8)))]
          for b in B]
K_BASIS = f2_rowspace_basis(K_ROWS)
check("S0.4 image of (1+i)L in L/2L has F2-dimension 4 "
      "(=> |V| = |L/(1+i)L| = 16, v689 index)",
      len(K_BASIS) == 4, "dim = %d" % len(K_BASIS))

H_ROWS = f2_nullspace(K_BASIS, 8)
check("S0.5 check matrix H: 4 independent functionals vanishing on (1+i)L",
      len(H_ROWS) == 4)


def label(w):
    c = coords(w)
    return tuple(sum(h[i] * c[i] for i in range(8)) & 1 for h in H_ROWS)


root_label = {w: label(w) for w in ROOTS}
CEN = Counter(root_label.values())
ALL_V = [v for v in product((0, 1), repeat=4)]
ZERO = (0, 0, 0, 0)
check("S0.6 v689 census: the 240 roots fall 15 x 16 over the nonzero "
      "classes, zero class EMPTY",
      len(CEN) == 15 and ZERO not in CEN
      and all(n == 16 for n in CEN.values()),
      "classes: %d, sizes: %s" % (len(CEN), sorted(set(CEN.values()))))

REP = {}
for w, v in root_label.items():
    REP.setdefault(v, w)
REP[ZERO] = (0,) * 8

SIGMA_MAP = {v: label(sig8(REP[v])) for v in ALL_V}
ok_sig = all(label(sig8(w)) == SIGMA_MAP[root_label[w]] for w in ROOTS)
FIX = [v for v in ALL_V if SIGMA_MAP[v] == v]
ok_lin = all(SIGMA_MAP[tuple(a ^ b for a, b in zip(u, v))]
             == tuple(a ^ b for a, b in
                      zip(SIGMA_MAP[u], SIGMA_MAP[v]))
             for u in ALL_V for v in ALL_V)
ok_ord3 = all(SIGMA_MAP[SIGMA_MAP[SIGMA_MAP[v]]] == v for v in ALL_V)
check("S0.7 sigma-bar on V: well-defined on all 240 roots, F2-linear, "
      "sigma^3 = id, exactly 4 fixed classes (v738 S1.4)",
      ok_sig and ok_lin and ok_ord3 and len(FIX) == 4,
      "fixed classes: %d" % len(FIX))

# chi_par: coordinate parity (v722); as F2 functional in B-coords
CHI_VEC = [b[0] & 1 for b in B]


def chi_of_coords(c):
    return sum(CHI_VEC[i] * c[i] for i in range(8)) & 1


# solve f (1x4) with f.H = CHI_VEC over F2
F_SOL = None
for f in product((0, 1), repeat=4):
    vec = [sum(f[k] * H_ROWS[k][i] for k in range(4)) & 1 for i in range(8)]
    if vec == CHI_VEC:
        F_SOL = f
        break
check("S0.8 chi_par is well-defined on V (v722 S3: (1+i)L is NS-pure): "
      "the parity functional factors through the check matrix",
      F_SOL is not None, "f = %s" % (F_SOL,))


def chi_par(v):
    return sum(F_SOL[k] * v[k] for k in range(4)) & 1


ok_chi = all(chi_par(root_label[w]) == (w[0] & 1) for w in ROOTS)
NS = [v for v in ALL_V if v != ZERO and chi_par(v) == 0]
RR = [v for v in ALL_V if chi_par(v) == 1]
check("S0.9 v722 NS/R census on V: 7 NS nonzero classes + 8 R classes, "
      "consistent over all 240 roots",
      ok_chi and len(NS) == 7 and len(RR) == 8,
      "NS = %d, R = %d" % (len(NS), len(RR)))

# the canonical Fano plane P = ker chi_par \ {0}; its 7 lines
P_PTS = sorted(NS)
P_IDX = {v: i for i, v in enumerate(P_PTS)}
P_LINES = set()
for u, v in combinations(P_PTS, 2):
    w = tuple(a ^ b for a, b in zip(u, v))
    if w in P_IDX:
        P_LINES.add(frozenset((P_IDX[u], P_IDX[v], P_IDX[w])))
P_LINES = sorted(P_LINES)
pair_cover = all(sum(1 for L in P_LINES if i in L and j in L) == 1
                 for i, j in combinations(range(7), 2))
check("S0.10 the NS hyperplane is projectively a Fano plane: 7 points, "
      "7 lines, every point pair on exactly one line",
      len(P_LINES) == 7 and pair_cover)

SIG_P = [P_IDX[SIGMA_MAP[P_PTS[i]]] for i in range(7)]
sig_p_ok = (sorted(SIG_P) == list(range(7))
            and [SIG_P[SIG_P[SIG_P[i]]] for i in range(7)] == list(range(7))
            and SIG_P != list(range(7)))
FIX_P = [i for i in range(7) if SIG_P[i] == i]
check("S0.11 sigma-bar restricted to the NS plane: a NONTRIVIAL order-3 "
      "collineation with exactly 1 fixed point (cycle type 1+3+3)",
      sig_p_ok and len(FIX_P) == 1,
      "fixed points on P: %d; sigma-invariant plane: %s"
      % (len(FIX_P), all(SIGMA_MAP[v] in NS for v in NS)))
n_fix_ns = sum(1 for v in FIX if v != ZERO and chi_par(v) == 0)
info("S0.12 of the 3 nonzero sigma-fixed classes, %d is NS (on the plane), "
     "%d are R" % (n_fix_ns, 3 - n_fix_ns))

# ===========================================================================
# S1  arithmetic substrate: O = Z[omega], the norm line, CR = 4/3
# ===========================================================================
section("S1  arithmetic substrate: O_{-7}, norm line alpha_t, CR = 4/3")


def omul(x, y):
    a, b = x
    c, d = y
    return (a * c - 2 * b * d, a * d + b * c + b * d)


def oconj(x):
    return (x[0] + x[1], -x[1])


def onorm(x):
    a, b = x
    return a * a + a * b + 2 * b * b


def red7(x):
    return (x[0] + 4 * x[1]) % 7


t, X = sp.symbols("t x")
s7 = sp.sqrt(-7)
alpha_sym = (4 * t + 7 + s7) / 2
check("S1.1 v533 rebuilt: alpha_t = (4t+7+sqrt(-7))/2 = (2t+3) + omega, "
      "N(alpha_t) = 4t^2+14t+14, translation alpha_{t+1} = alpha_t + 2, "
      "char-poly discriminant -7 for every t",
      sp.expand(alpha_sym - ((2 * t + 3) + (1 + s7) / 2)) == 0
      and sp.expand(sp.expand(alpha_sym * ((4 * t + 7 - s7) / 2))
                    - (4 * t**2 + 14 * t + 14)) == 0
      and sp.expand(alpha_sym.subs(t, t + 1) - alpha_sym - 2) == 0
      and sp.discriminant(X**2 - (4 * t + 7) * X + 4 * t**2 + 14 * t + 14,
                          X) == -7)

ALPHA = {n: (2 * n + 3, 1) for n in (-2, -1, 0, 1)}
NORMS = [onorm(ALPHA[n]) for n in (-2, -1, 0, 1)]
REDS = [red7(ALPHA[n]) for n in (-2, -1, 0, 1)]
check("S1.2 the four transfer states J,K,C,F: norms (2,4,14,32), "
      "ramified-fiber images red(alpha_t) = 2t mod 7 = (3,5,0,2)",
      NORMS == [2, 4, 14, 32] and REDS == [3, 5, 0, 2],
      "reds: %s" % (REDS,))

a1, b1, c1, d1 = [alpha_sym.subs(t, n) for n in (-2, -1, 0, 1)]
CR = sp.simplify(((a1 - c1) * (b1 - d1)) / ((a1 - d1) * (b1 - c1)))
check("S1.3 v632/v571 cross-ratio rebuilt: CR(alpha_-2, alpha_-1; "
      "alpha_0, alpha_1) = 4/3 exactly",
      CR == sp.Rational(4, 3), "CR = %s" % CR)

check("S1.4 ramification/splitting witnesses: x^2 - x + 2 has the DOUBLE "
      "root 4 mod 7 (7 ramified, O/(sqrt(-7)) = F7, omega -> 4) and splits "
      "as x(x+1) mod 2 (2 split, -7 = 1 mod 8)",
      (-8 - (-1)) % 7 == 0 and (16 - 2) % 7 == 0        # (x-4)^2 = x^2-x+2
      and (0 * 0 - 0 + 2) % 2 == 0 and (1 - 1 + 2) % 2 == 0
      and (-7) % 8 == 1)

UNITS = [(a, b) for a in range(-3, 4) for b in range(-3, 4)
         if onorm((a, b)) == 1]
AUT_IMGS = [(a, b) for a in range(-4, 5) for b in range(-4, 5)
            if (a, b) != (0, 1)
            and sp.expand((a + b * (1 + s7) / 2)**2 - (a + b * (1 + s7) / 2)
                          + 2) == 0]
check("S1.5 unit and automorphism census: units = {+-1} only; the ring "
      "automorphism group is {id, conj} (order 2) -- O_{-7} carries NO "
      "order-3 symmetry globally",
      UNITS in ([(-1, 0), (1, 0)], [(1, 0), (-1, 0)])
      and AUT_IMGS == [(1, -1)],
      "units: %s, other root of minpoly: %s (= omega-bar)"
      % (UNITS, AUT_IMGS))

# ===========================================================================
# S2  part (a): the canonical 7-structure census in O_{-7}
# ===========================================================================
section("S2  part (a): what is the canonical 7-structure in O_{-7}?")

BOX = [(a, b) for a in range(-6, 7) for b in range(-6, 7)]
n_norm = Counter(onorm(x) for x in BOX if onorm(x) <= 8)
info("S2.1 element census (norms <= 8, exact): "
     + ", ".join("N=%d: %d" % (k, n_norm[k]) for k in sorted(n_norm)))

# ideals of norm <= 7 (h = 1; generators up to units; complete by
# p-adic factorization: norms are products of split 2 and ramified 7)
IDEALS_7 = {
    "(1)": (1, 0),
    "p": (0, 1),               # omega, N = 2
    "pbar": (1, -1),           # omega-bar, N = 2
    "p^2": (-2, 1),            # omega^2 = omega - 2, N = 4
    "p pbar": (2, 0),          # 2, N = 4
    "pbar^2": (-1, -1),        # omega-bar^2, N = 4
    "(sqrt-7)": (-1, 2),       # sqrt(-7) = -1 + 2 omega, N = 7
}
check("S2.2 ideal census: exactly SEVEN ideals of norm <= 7 "
      "(1 + 2 + 3 + 1 by norm 1/2/4/7) -- a canonical 7-set exists",
      [onorm(g) for g in IDEALS_7.values()] == [1, 2, 2, 4, 4, 4, 7]
      and len(IDEALS_7) == 7)

# does the ideal 7-set carry an order-3 symmetry compatible with the
# canonical arithmetic (norm preserved, commutes with conjugation)?
NAMES = list(IDEALS_7)
NRM = {k: onorm(v) for k, v in IDEALS_7.items()}
CONJ_IDEAL = {"(1)": "(1)", "p": "pbar", "pbar": "p", "p^2": "pbar^2",
              "pbar^2": "p^2", "p pbar": "p pbar", "(sqrt-7)": "(sqrt-7)"}
n_compat3 = 0
for pm in permutations(range(7)):
    g = {NAMES[i]: NAMES[pm[i]] for i in range(7)}
    if any(NRM[g[k]] != NRM[k] for k in NAMES):
        continue
    if any(g[CONJ_IDEAL[k]] != CONJ_IDEAL[g[k]] for k in NAMES):
        continue
    gg = {k: g[g[k]] for k in NAMES}
    ggg = {k: g[gg[k]] for k in NAMES}
    if all(ggg[k] == k for k in NAMES) and any(g[k] != k for k in NAMES):
        n_compat3 += 1
check("S2.3 CONTROL C-c (must fire): the ideal 7-set admits NO order-3 "
      "symmetry commuting with norm + conjugation (count over all 5040 "
      "permutations = 0) -- the ideal census is NOT the Fano carrier",
      n_compat3 == 0, "compatible 3-cycles: %d" % n_compat3)
CONTROLS_FIRED.append(n_compat3 == 0)

# canonical Fano structures on the ramified fiber F7 = O/(sqrt(-7)):
# census of ALL Fano structures on 7 labeled points, then the frozen
# canonicity filter: invariance under the transfer translation x -> x+2.
PTS3 = [p for p in product((0, 1), repeat=3) if p != (0, 0, 0)]
IDX3 = {p: i for i, p in enumerate(PTS3)}
STD_LINES = set()
for u, v in combinations(PTS3, 2):
    w = tuple(a ^ b for a, b in zip(u, v))
    STD_LINES.add(frozenset((IDX3[u], IDX3[v], IDX3[w])))
STD_LINES = sorted(STD_LINES)

ALL_FANO = set()
for pm in permutations(range(7)):
    ALL_FANO.add(frozenset(frozenset(pm[i] for i in L) for L in STD_LINES))
check("S2.4 Fano census: exactly 30 Fano structures on 7 labeled points "
      "(7!/168)", len(ALL_FANO) == 30, "count: %d" % len(ALL_FANO))

STEP = red7((2, 0))     # the transfer translation step red(2) = 2
TRANS_INV = [F for F in ALL_FANO
             if frozenset(frozenset((i + 1) % 7 for i in L) for L in F) == F]
check("S2.5 frozen canonicity filter: exactly 2 translation-invariant "
      "structures (the QR / QNR difference-set models), swapped by the "
      "unit -1, each invariant under the transfer step x -> x + %d" % STEP,
      len(TRANS_INV) == 2
      and all(frozenset(frozenset((i + STEP) % 7 for i in L) for L in F)
              == F for F in TRANS_INV)
      and all(frozenset(frozenset((-i) % 7 for i in L) for L in F)
              != F for F in TRANS_INV)
      and frozenset(frozenset((-i) % 7 for i in L) for L in TRANS_INV[0])
      == TRANS_INV[1],
      "count: %d" % len(TRANS_INV))

MODELS = {}
for F in TRANS_INV:
    tag = "QR" if frozenset({1, 2, 4}) in F else "QNR"
    MODELS[tag] = F
MUL2_OK = all(frozenset(frozenset((2 * i) % 7 for i in L) for L in F) == F
              for F in MODELS.values())
check("S2.6 the canonical order-3 action: x -> 2x (the difference-set "
      "multiplier; 2^3 = 1 mod 7, fixed point 0 only) is an automorphism "
      "of BOTH canonical models; 2 = the transfer step = |Z2|",
      MUL2_OK and pow(2, 3, 7) == 1
      and [x for x in range(7) if (2 * x) % 7 == x] == [0])
info("S2.7 canonical 7-structure ANSWER: the ramified residue field "
     "F7 = O/(sqrt(-7)) with the two translation-invariant difference-set "
     "Fano models (QR lines contain {1,2,4}; QNR contain {3,5,6}); the "
     "ideal 7-set exists but refuses the 3-cycle (S2.3)")

# ===========================================================================
# THE FOUR PREREGISTERED CONDITIONS -- sequential, ABORT at first violation
# ===========================================================================
BREAK_AT = None
COND_STATE = {}


def sub_ok():
    return all(ok for _, ok in CHECKS)


SUBSTRATE_OK = sub_ok()

# --------------------------------------------------------------- COND 1
section("COND1  sigma three-cycle preservation (kill criterion 1)")


def equivariant_lifts(model_lines, sig_perm, mult):
    """all incidence bijections Phi: P -> F7 with Phi.sigma = mult.Phi"""
    sols = []
    for pm in permutations(range(7)):
        if any(pm[sig_perm[i]] != (mult * pm[i]) % 7 for i in range(7)):
            continue
        if frozenset(frozenset(pm[i] for i in L)
                     for L in P_LINES) == model_lines:
            sols.append(pm)
    return sols


LIFTS = {tag: equivariant_lifts(MODELS[tag], SIG_P, 2) for tag in MODELS}
c1a = check("C1.a equivariant lifts EXIST for both canonical models: "
            "count(QR) = %d, count(QNR) = %d (expected: the centralizer "
            "order of an order-3 element, = 3 each)"
            % (len(LIFTS["QR"]), len(LIFTS["QNR"])),
            len(LIFTS["QR"]) >= 1 and len(LIFTS["QNR"]) >= 1)
fx_img = {tag: {pm[FIX_P[0]] for pm in LIFTS[tag]} for tag in MODELS}
c1b = check("C1.b every lift sends the unique sigma-bar fixed point of the "
            "NS plane to 0 = red(alpha_0) = the C corner (norm 14 = dim G2) "
            "-- forced, machine-confirmed",
            all(fx_img[tag] == {0} for tag in MODELS if LIFTS[tag]))
n_ctrl_a = sum(len(equivariant_lifts(MODELS[tag], SIG_P, 3))
               for tag in MODELS)
c1c = check("C1.c CONTROL C-a (must fire): with the non-multiplier x -> 3x "
            "there are ZERO equivariant lifts",
            n_ctrl_a == 0, "count: %d" % n_ctrl_a)
CONTROLS_FIRED.append(n_ctrl_a == 0)
broken = set(MODELS["QR"])
L0 = sorted(broken)[0]
broken.remove(L0)
ll = sorted(L0)
broken.add(frozenset([ll[0], ll[1], (ll[2] + 1) % 7
                      if (ll[2] + 1) % 7 not in (ll[0], ll[1])
                      else (ll[2] + 2) % 7]))
n_ctrl_b = len(equivariant_lifts(frozenset(broken), SIG_P, 2))
c1d = check("C1.d CONTROL C-b (must fire): a one-line-broken incidence "
            "structure admits ZERO lifts",
            n_ctrl_b == 0, "count: %d" % n_ctrl_b)
CONTROLS_FIRED.append(n_ctrl_b == 0)

COND_STATE["COND1"] = c1a and c1b and c1c and c1d
if not COND_STATE["COND1"]:
    BREAK_AT = "COND1"

# --------------------------------------------------------------- COND 2
if BREAK_AT is None:
    section("COND2  parity-bit preservation: chi_par needs a lift invariant "
            "(kill criterion 2)")

    # (2a) norm parity through the ramified fiber?
    cex = None
    for x in BOX:
        for y in BOX:
            if red7(x) == red7(y) and (onorm(x) - onorm(y)) % 2 != 0:
                cex = (x, y)
                break
        if cex:
            break
    alive_2a = cex is None
    info("C2.a candidate (2a) %s: norm parity nu = N mod 2 %s through the "
         "ramified fiber"
         % ("ALIVE" if alive_2a else "DEAD",
            "factors" if alive_2a else "does NOT factor"),
         "" if alive_2a else
         "counterexample x = %s (N = %d, red = %d) vs y = %s (N = %d, "
         "red = %d)" % (cex[0], onorm(cex[0]), red7(cex[0]),
                        cex[1], onorm(cex[1]), red7(cex[1])))

    # (2b) the fiber's own order-2 structure (QR character) pulled back
    # along the COND1 lifts (most lenient reading: SOME lift suffices)?
    QRS = {1, 2, 4}
    alive_2b = False
    n_pullbacks = 0
    for tag in MODELS:
        for pm in LIFTS[tag]:
            for conv in (0, 1):
                bits = [(1 - conv) if pm[i] in QRS else
                        (conv if pm[i] != 0 else 0) for i in range(7)]
                n_pullbacks += 1
                if all(b == 0 for b in bits):
                    alive_2b = True
    info("C2.b candidate (2b) %s: chi_par|P = 0 identically, the quadratic "
         "character chi_7 pulled back along the lifts is %s "
         "(%d pullbacks, both bit conventions)"
         % ("ALIVE" if alive_2b else "DEAD",
            "constant 0 for some lift" if alive_2b else "NONCONSTANT in "
            "every case", n_pullbacks))

    # (2c) 2-rank census of ALL ideal quotients of norm 8 and 16
    IDEALS_2ADIC = {
        "p^3": (-2, -1), "pbar^3": (-3, 1), "p^2 pbar": (0, 2),
        "p pbar^2": (2, -2),
        "p^4": (2, -3), "pbar^4": (-1, 3), "p^3 pbar": (-4, 2),
        "p pbar^3": (-2, -2), "p^2 pbar^2": (4, 0),
    }

    def quot_invariants(g):
        a, b = g
        m11, m12 = a, b
        m21, m22 = -2 * b, a + b
        det = abs(m11 * m22 - m12 * m21)
        d1 = sp.igcd(sp.igcd(abs(m11), abs(m12)),
                     sp.igcd(abs(m21), abs(m22)))
        return (int(d1), int(det // d1))

    ranks = {}
    for k, g in IDEALS_2ADIC.items():
        d1_, d2_ = quot_invariants(g)
        ranks[k] = (onorm(g), (d1_, d2_),
                    sum(1 for d in (d1_, d2_) if d % 2 == 0))
    ok_norms = ([ranks[k][0] for k in
                 ("p^3", "pbar^3", "p^2 pbar", "p pbar^2")] == [8] * 4
                and [ranks[k][0] for k in
                     ("p^4", "pbar^4", "p^3 pbar", "p pbar^3",
                      "p^2 pbar^2")] == [16] * 5)
    max_rank = max(r[2] for r in ranks.values())
    alive_2c = ok_norms and max_rank >= 3
    info("C2.c candidate (2c) %s: complete 2-adic quotient census (all "
         "ideals of norm 8 and 16, h = 1, norms verified: %s): maximal "
         "2-rank = %d (need >= 3) -- 2 SPLITS (-7 = 1 mod 8, O tensor Z2 "
         "= Z2 x Z2), so no quotient is F2^3 or F2^4"
         % ("ALIVE" if alive_2c else "DEAD", ok_norms, max_rank),
         "; ".join("%s: N=%d, inv=%s, 2-rank %d" % (k, *ranks[k])
                   for k in IDEALS_2ADIC))

    COND_STATE["COND2"] = check(
        "C2.d COND2 verdict: at least one frozen candidate provides a lift "
        "invariant for the NS/R parity bit (2a: %s, 2b: %s, 2c: %s)"
        % tuple("ALIVE" if a else "DEAD"
                for a in (alive_2a, alive_2b, alive_2c)),
        alive_2a or alive_2b or alive_2c)
    if not COND_STATE["COND2"]:
        BREAK_AT = "COND2"

# --------------------------------------------------------------- COND 3
if BREAK_AT is None:
    section("COND3  the four transfer states as canonical Fano objects "
            "(kill criterion 3)")
    S_IMG = set(REDS)
    types = {}
    for tag, F in MODELS.items():
        inner = [L for L in F if L <= S_IMG]
        if not inner:
            types[tag] = "frame"
        elif len(inner) == 1:
            rest = S_IMG - set(inner[0])
            types[tag] = ("line+fixedpoint" if rest == {0}
                          and 0 not in inner[0] else
                          "line+point(noncanonical: %s)" % sorted(rest))
        else:
            types[tag] = "degenerate"
    c3 = check("C3.a red({J,K,C,F}) = %s is the SAME canonical 4-object in "
               "both models: QR -> %s, QNR -> %s"
               % (sorted(S_IMG), types["QR"], types["QNR"]),
               types["QR"] == types["QNR"]
               and types["QR"] in ("frame", "line+fixedpoint"))
    COND_STATE["COND3"] = c3
    if not c3:
        BREAK_AT = "COND3"

# --------------------------------------------------------------- COND 4
if BREAK_AT is None:
    section("COND4  cross-ratio 4/3 reconstructible from incidence "
            "(kill criterion 4)")

    def cr7(a, b, c, d):
        num = ((a - c) * (b - d)) % 7
        den = ((a - d) * (b - c)) % 7
        return (num * pow(den, 5, 7)) % 7  # den^-1 = den^5 mod 7

    c4a = check("C4.a functoriality witness: CR(3,5;0,2) mod 7 = %d equals "
                "red(4/3) = 4 * inv(3) = %d"
                % (cr7(3, 5, 0, 2), (4 * pow(3, 5, 7)) % 7),
                cr7(3, 5, 0, 2) == (4 * pow(3, 5, 7)) % 7)
    cr_vals = {}
    for tag, F in MODELS.items():
        vals = set()
        for pm in permutations(range(7)):
            if frozenset(frozenset(pm[i] for i in L) for L in F) != F:
                continue
            if {pm[i] for i in S_IMG} != S_IMG:
                continue
            vals.add(cr7(pm[3], pm[5], pm[0], pm[2]))
        cr_vals[tag] = vals
    c4b = check("C4.b reconstruction: CR constant over the full collineation "
                "stabilizer of the 4-object: QR values %s, QNR values %s"
                % (sorted(cr_vals["QR"]), sorted(cr_vals["QNR"])),
                all(len(v) == 1 for v in cr_vals.values()))
    COND_STATE["COND4"] = c4a and c4b
    if not COND_STATE["COND4"]:
        BREAK_AT = "COND4"

# ===========================================================================
# VERDICT
# ===========================================================================
section("VERDICT")

for cond in ("COND1", "COND2", "COND3", "COND4"):
    if cond in COND_STATE:
        print("  %s : %s" % (cond, "PASS" if COND_STATE[cond] else
                             "FAIL (KILL)"))
    else:
        print("  %s : SKIPPED (preregistered abort at %s)"
              % (cond, BREAK_AT))

n_fail = sum(1 for _, ok in CHECKS if not ok)
if not SUBSTRATE_OK:
    VERDICT = "SUBSTRATE-FAIL"
elif BREAK_AT is None and all(COND_STATE.get(c, False)
                              for c in ("COND1", "COND2", "COND3", "COND4")):
    VERDICT = "FANO-DISC7-BRIDGE"
else:
    VERDICT = "FANO-DISC7-DECORATIVE"

print()
print("VERDICT: %s%s" % (VERDICT,
                         ("  (break at %s)" % BREAK_AT) if BREAK_AT else ""))
if VERDICT == "FANO-DISC7-DECORATIVE":
    print()
    print("DOCUMENTATION OF THE BREAK (preregistered duty):")
    if BREAK_AT == "COND2":
        print("  The seven-correlation is DECORATIVE.  The Fano side needs")
        print("  F2-rank 3 (the plane) resp. 4 (the four-bit space V); the")
        print("  2-adic structure of O_{-7} maxes out at 2-rank 2 because 2")
        print("  SPLITS (-7 = 1 mod 8, O tensor Z2 = Z2 x Z2).  The NS/R")
        print("  parity bit has no arithmetic carrier: it neither factors")
        print("  through the ramified fiber (C2.a counterexample) nor")
        print("  matches the fiber's own order-2 structure (C2.b), nor is")
        print("  any ideal quotient elementary-abelian of rank >= 3 (C2.c).")
        print("  The equivariant 3-cycle half (COND1) is real and exact;")
        print("  the parity half kills the bridge.")
print()
print("controls fired: %d/%d (all must fire)"
      % (sum(CONTROLS_FIRED), len(CONTROLS_FIRED)))
print("checks: %d, failures (incl. preregistered DEAD candidates): %d"
      % (len(CHECKS), n_fail))
print("elapsed: %.1f s" % (time.time() - T0))
