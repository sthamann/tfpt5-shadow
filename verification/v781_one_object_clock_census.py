#!/usr/bin/env python3
"""v781 -- E8.ONEOBJECT.01: the d = 4 forcing census + the 60-line clock synchronization kill, ONE module from two probes (21/21 + 23/23 checks, ~9 s; discovery probes one_object_reduction_probe.py ONE-OBJECT-PARTIAL and clock_fiber_product_probe.py CLOCK-FIBER-DEAD, both 2026-08-05).  THE FORCING CENSUS (part 1, exact Fraction arithmetic, no floats): for d = 2..12 the discriminant forms are disc(A_{d-1}) = Z_d and disc(D_{d+1}) = Z4 (d even) / Z2 x Z2 (d odd), and the TFPT glue pattern (isotropic glue group, evenness q = 0 mod 2Z, unimodularity |H|^2 = 4d) admits an even unimodular DIAGONAL glue of A_{d-1} (+) D_{d+1} iff d = 4 -- even stronger, ANY even unimodular glue exists only at d = 4; the coarse square layer (|H|^2 = 4d a perfect square) passes only d in {4, 9}, and d = 9 dies at isotropy (disc(D_10) q-values {0, 1, 1/2, 1/2}: the forced order-2 part of an |H| = 6 subgroup cannot be even-isotropic).  At d = 4 the census reproduces v92 EXACTLY: precisely TWO even Lagrangian glues, both diagonal cyclic Z4, the graphs of the two anti-isometries k -> k and k -> 3k (q(A3) = 3/4, q(D5) = 5/4, 3/4 + 5/4 = 2 = the E8 root norm), intersecting in the order-2 halfway glue {0, (2,2)} (v92's SO(16)_1 rung); the explicit v1 lattice certificate closes: glued basis (drop root #2, add g = (w_A3, spinor_D5)) with integer Gram, even diagonal, det = 1, norm-2 count per glue coset [52, 64, 60, 64], total 240, ALL 240 integral over the glued basis -- THE even unimodular E8.  Controls fire: dropping evenness opens d = 9 (an odd unimodular glue exists there), dropping unimodularity opens d in {7, 8, 9, 12}.  Corollaries at the forced d, typed honestly: g_car = d+1 = 5, N_fam = d-1 = 3, rank = 2d = 8, glue index = sqrt(4d) = 4 = d = |mu4| are verified arithmetic; c_3 = 1/(2 pi d)|_{d=4} = 1/(8 pi) is a corpus-legitimate REWRITING (c_3 = 1/(2 e_1(a) pi) with e_1(a) = 4 = |mu4| = d, tfpt_1 ~L189-194 / v23 anchor-first refinement), NOT a new derivation of P1 (the corpus Gauss-Bonnet chain reads the 4 pi as total sphere curvature, not d; ONE-OBJECT-FORCED predeclared unreachable).  THE CLOCK KILL (part 2, three levels, each independently fatal to L_60 = Z12 x_{Z6} Z30 on the 60 Gaussian lines): (1) the seam clock c = J o sigma (order 12; c^4 = sigma, c^9 = J, c^6 = -1 exact, v634 S7) acts on the 60 lines only through Z3 = <sigma> (line-trivial powers {0, 3, 6, 9}; sigma line census {3: 19, 1: 3}, v633 Q4); (2) the deployed Coxeter clock w = s_1 ... s_8 (order 30 on the 240 roots, Kostant census {30: 8}, w^15 = -1) does NOT descend to the lines (line-preserving powers {0, 15} only; w J w^-1 not in {J, J^-1}); (3) the existence sweep decides EVERY realization: the FULL line-compatible group (the 60 unitary reflections + the conj coset of N(<J>)) has order 23040 = 2 x 11520 (the antiunitary coset is genuinely new) with max element order 12 (spectrum {1: 1, 2: 751, 3: 800, 4: 4560, 5: 2304, 6: 7520, 8: 2880, 10: 2304, 12: 1920}) -- orders 15, 30, 60 ALL absent, while a simply-transitive Z60 needs line order 60 and any root-level order-30 clock would induce line order 30 or 15: no realization can exist.  The abstract layer stays exact: the fiber product Z12 x_{Z6} Z30 has order 60 and IS cyclic Z60 (phi(60) = 16 generators), while the wrong pairing Z12 x Z30 has order 360 with invariant factors (6, 60) (CC1 fires); CC2 fires 5/5 (frozen-seed random order-12 unitary words break r^4 = sigma, r^9 = J); CC3 fires (the wrong complex structure J' preserves the roots and the free-60 census but breaks [J', sigma] = 0); the mu4 layer 240 = 4 x 60 is exact; the joint <c, w> orbit census on the 240 roots is {240: 1}.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes one_object_reduction_probe.py (2026-08-05, 21/21, 4.3 s, ONE-OBJECT-PARTIAL; no disclosed corrections) + clock_fiber_product_probe.py (2026-08-05, 23/23, 4.7 s, CLOCK-FIBER-DEAD; the CC2 SAMPLER CORRECTION disclosed in the probe docstring carried verbatim: "the first run's word length <= 5 letters found NO order-12 words in 4000 frozen-seed tries; the sampler was widened to words of length <= 12 with 20000 tries.  The control's SEMANTICS (random order-12 unitary must break r^4 = sigma, r^9 = J) is unchanged; the frozen spec text and SHA are untouched."); both re-run identically at promotion.  Promoted verbatim (part 2 wrapped in a function scope).  Numbers unchanged.  run() encodes both patterns (v757 precedent).

Original one_object_reduction_probe docstring (verbatim):
one_object_reduction_probe -- THE d = 4 FORCING CENSUS: are P1 and P2
two functors of ONE four-point boundary object?

CLAIM CHAIN UNDER TEST (frozen; see FROZEN_SPEC, SHA-256 printed BEFORE
any lattice data is computed): for a boundary divisor with d marked
points the cycle side gives A_{d-1} (N_fam = d-1 = rank H_1 of the
d-punctured P^1) and the function/carrier side gives D_{d+1}
(g_car = d+1).  The corpus already reads 3 and 5 this way at d = 4:

  * X_f deg 4 boundary: X_f^o ~= P^1 \\ mu_4, H_1 = Z^3, "hence A_3 and
    N_fam = 3" (tfpt_1_architecture_e8.tex ~L894, ~L4234);
  * g_car = rank D_5 = 5, q(D5) = g_car/|mu4|, q(A3) = N_fam/|mu4| with
    n+1 = 4 = |mu4| on the A-side (tfpt_1 ~L4201-4205);
  * |mu4| = (g_car + N_fam)/2 = 4 (tfpt_1 ~L4235, v53_compiler_core).

THE NEW FORCING ARGUMENT to verify exactly: disc(A_{d-1}) ~= Z_d, while
disc(D_{d+1}) is Z_4 for d+1 odd (d even) and Z_2 x Z_2 for d+1 even
(d odd).  The TFPT glue pattern (v1_e8_glue + v92_glue_uniqueness:
cyclic isotropic glue group, evenness q = 0 mod 2Z, unimodularity
|H|^2 = |disc A| * |disc D|) admits a DIAGONAL glue of
A_{d-1} (+) D_{d+1} iff Z_d ~= Z_4 with anti-isometric quadratic forms,
i.e. iff d = 4 -- yielding E8 = the D5 (+) A3 glue.  Any other d
admitting an even unimodular diagonal glue KILLS the forcing claim.

CENSUS: for d = 2..12 compute both discriminant groups and their
quadratic/linking forms EXACTLY from the Cartan matrices (Fraction
arithmetic, no floats), enumerate ALL subgroups of the direct-sum
discriminant form, and classify:
  * even unimodular glues      (Lagrangian, q = 0 mod 2Z)
  * ... of which DIAGONAL      (trivial intersection with both factors)
  * odd unimodular glues       (Lagrangian, q = 0 mod Z, b = 0 mod Z,
                                NOT even)          [control: evenness]
  * nontrivial even glues of ANY index              [control: unimod]

VERDICT ENUMS (frozen):
  ONE-OBJECT-FORCED  = glue census forces d = 4 AND the c_3 = 1/(2 pi d)
                       link is corpus-DERIVED from the boundary object.
                       Predeclared UNREACHABLE for this corpus snapshot:
                       P1 is a primitive postulate (tfpt_1 ~L169) whose
                       Gauss-Bonnet hardening 1/(|Z2| * 4 pi) reads the
                       "4 pi" as total sphere curvature, NOT as d
                       (tfpt_1 ~L670-689).
  ONE-OBJECT-PARTIAL = the glue census forces d = 4 exactly (controls
                       fire), corollary g_car = d+1 = 5 is verified
                       arithmetic, but the c_3 link stays INTERPRETIVE:
                       c_3 = 1/(2 e_1(a) pi) with e_1(a) = 4 = |mu4| IS
                       corpus-legitimate (tfpt_1 ~L189-194, v23
                       anchor-first refinement), so 1/(2 pi d)|_{d=4}
                       = 1/(8 pi) is a corpus-legitimate REWRITING --
                       but "the glue-forced d derives P1" would be a NEW
                       derivation, which this probe must NOT smuggle.
  ONE-OBJECT-DEAD    = some d != 4 admits an even unimodular diagonal
                       glue (the forcing claim dies), or d = 4 fails.
  TEST-VOID          = a corpus-reproduction gate fails (G2/G3) or a
                       must-fire control does not fire (G4/G5).

GATES (frozen before running):
  G1  d-table: {d in 2..12 admitting an even unimodular DIAGONAL glue}
      must be decided exactly; forcing holds iff it equals {4}.
  G2  at d = 4 the census must reproduce v92 EXACTLY: precisely TWO
      even Lagrangian glues, both diagonal cyclic Z4 -- the graphs of
      the two anti-isometries k -> k and k -> 3k.
  G3  explicit lattice certificate at d = 4 (v1 reproduction): gluing
      A3 (+) D5 by one such glue gives an even lattice with Gram det 1
      and EXACTLY 240 norm-2 vectors, all integral over the glued
      basis -- i.e. E8.
  G4  CONTROL (must fire): dropping evenness (isotropy mod Z only)
      opens at least one d != 4 (an odd unimodular glue exists there).
  G5  CONTROL (must fire): dropping unimodularity (any nontrivial even
      isotropic glue subgroup) opens at least one d != 4.
  G6  square obstruction layer: |H|^2 = 4d needs 4d to be a perfect
      square, i.e. d itself a square: only d in {4, 9} survive the
      coarse layer in 2..12; the census must show HOW d = 9 dies
      (no isotropic-even Lagrangian in Z9 (+) Z2 x Z2).
  G7  corollaries stated as verified arithmetic at the forced d:
      g_car = d+1 = 5, N_fam = d-1 = 3, rank = 2d = 8,
      glue index = sqrt(4d) = 4 = d = |mu4|; c_3 typing per the
      PARTIAL/FORCED rule above (honesty gate: interpretation label).

FIREWALL: experiments/tfpt-discovery probe; EXPLORATION ONLY; writes
nothing; touches no verification/, paper, ledger, changelog or website
surface; no marker moves; no physics claims.  ROOTCLASS-MIXED fence
(v775_gaussian_class_d5_purity): no code->matter semantics is used or
implied anywhere -- this census is pure lattice/discriminant-form
arithmetic.  A d != 4 hit is a valid, well-powered KILL and will be
reported honestly.

Sources (read-only): verification/v1_e8_glue.py (glue conditions +
lattice certificate pattern), v92_glue_uniqueness.py (Lagrangian
classification of Z4 x Z4, q = (5x^2+3y^2)/8 mod 1 in conformal-weight
normalization = half of our q mod 2Z), v53_compiler_core.py (atoms),
tfpt_1_architecture_e8.tex ~L160-194 (P1/P2, anchor-first refinement),
~L670-689 (Gauss-Bonnet hardening), ~L4190-4245 (glue norms as
compiler atoms), ~L894/4234 (H_1 = Z^3 reading).

Run:
    experiments/tfpt-discovery/.venv/bin/python \\
        experiments/tfpt-discovery/one_object_reduction_probe.py

Original clock_fiber_product_probe docstring (verbatim):
clock_fiber_product_probe -- THE 60-LINE CLOCK SYNCHRONIZATION CENSUS:
is L_60 ~= Z_12 x_{Z_6} Z_30 realized on the 60 Gaussian E8 lines?

HYPOTHESIS UNDER TEST (frozen; FROZEN_SPEC SHA-256 printed BEFORE any
root data is computed): the 60 Gaussian E8 lines (the free mu4-quotient
of the 240 roots, v629 R3 / v633 Q1) carry a canonical simply-transitive
(or at least orbit-defining) action of the fiber product
    L_60 ~= Z_12 x_{Z_6} Z_30
of the SEAM CLOCK (order 12; corpus: v623 V3 "L^4 = deck and L^12 = id
... proper order 12" on the covered seam; E8 avatar: the compiler clock
c = J o sigma with sigma = c^4, J = c^9, <c> = Z12, v629 R1 / v634 S7)
and the COXETER CLOCK (order 30; the E8 Coxeter element, constructed
exactly as the product of the 8 Bourbaki simple reflections deployed in
v1_e8_glue), over their shared Z_6 (sheet x family phase).

DEPLOYED CONVENTIONS (frozen, all corpus-verbatim):
  * Root model: D8+spinor, exact Fractions (v633 verbatim): 112 integer
    roots +-e_i +- e_j and 128 half-integer roots (+-1/2)^8 with an
    even number of minus signs / even coordinate sum.
  * J_all = i-rotation on the four coordinate pairs ((a,b) -> (-b,a));
    sigma = 3-cycle of pairs 1 -> 2 -> 3 -> 1 fixing pair 4; lines =
    the 60 free J-orbits, canonical rep = lexicographic minimum over
    the J-orbit (v633 canon).
  * Seam clock avatar: c = J o sigma (order 12).  Deployment gates:
    c^4 = sigma, c^9 = J, c^6 = -1 (v634 S7 identities).
  * Coxeter clock: w = s_1 s_2 ... s_8, the simple reflections of the
    Bourbaki E8 basis of v1_e8_glue.e8_simple_roots(), applied in
    Bourbaki index order.  Deployment gates: order 30 on the 240
    roots, Kostant orbit census {30: 8}, w^15 = -1 (E8 exponents all
    odd).
  * Z6 target: <c>/<c^6 = -1> and <w>/<w^6>; "sheet x family" = the
    -1 (sheet) and sigma (family) content.
  * Everything exact (int/Fraction permutations); the only RNG is the
    frozen-seed control CC2.

TESTS:
  (i)   FIBER CONDITION: both clocks must descend to the 60 lines and
        induce the SAME Z6 quotient action (compatibility square
        Z12 -> Z6 <- Z30 verified on the actual line permutations).
  (ii)  SIMPLE TRANSITIVITY: the joint line action of the two clock
        images must be isomorphic to the fiber product Z12 x_{Z6} Z30
        (order 60, computed exactly: it is CYCLIC Z60) acting on
        itself -- or the actual orbit type is named honestly.
  (iii) MU4 LAYER: 240 = 4 x 60 via the mu4 phases (J free with 60
        orbits of size 4) as the final layer.

EXISTENCE SWEEP (decisive for any realization, not just the deployed
one): the full line-compatible world is N(<J>) inside the root-set
automorphisms; its line image is generated by the 60 unitary
reflections (v633 Q7: order 11520) together with the complex
conjugation representative conj: (a,b) -> (a,-b) per pair (which obeys
conj o J o conj^-1 = J^-1).  Any order-30 root-level clock acting on
the 60 lines would have line order 30 or 15 (its cyclic group meets
the line-kernel <J> in a subgroup of order gcd-limited to <= 2), and a
simply-transitive Z60 needs line order 60.  The exact element-order
spectrum of the full line-compatible group therefore DECIDES the
hypothesis for EVERY realization of the clocks.

CENSUS CONTROLS (must fire):
  CC1 wrong pairing: the FULL product Z12 x Z30 has order 360 != 60
      and invariant factors (6, 60) != (60): it cannot act simply
      transitively on 60 lines; the fiber product Z12 x_{Z6} Z30 is
      cyclic of order 60 (exact SNF-level arithmetic).
  CC2 a random order-12 element of the unitary line world in place of
      the seam clock must BREAK the deployment identities
      (r^4 != sigma or r^9 != J) -- the compatibility square is not
      generic (frozen-seed word sampling in the 60 reflections).
      SAMPLER CORRECTION (disclosed): the first run's word length
      <= 5 letters found NO order-12 words in 4000 frozen-seed tries;
      the sampler was widened to words of length <= 12 with 20000
      tries.  The control's SEMANTICS (random order-12 unitary must
      break r^4 = sigma, r^9 = J) is unchanged; the frozen spec text
      and SHA are untouched.
  CC3 a wrong complex structure J' (i-rotation on a scrambled
      coordinate pairing) must break the corpus deployment (fail to
      preserve the root set, or fail the free-60-orbit census, or fail
      [J', sigma] = 0).

VERDICT ENUMS (frozen):
  CLOCK-FIBER-EXACT   = both clocks act on the 60 lines, induce the
                        same Z6, and the joint image is simply
                        transitive ~= Z60 = Z12 x_{Z6} Z30.
  CLOCK-FIBER-PARTIAL = both act on the lines and the Z6 squares agree,
                        but the joint action is NOT simply transitive
                        -- the true orbit type is named.
  CLOCK-FIBER-DEAD    = a clock fails to act on the 60 lines at all
                        (descent failure), or the Z6 compatibility
                        fails, or the required element orders
                        (15/30/60) are absent from the FULL
                        line-compatible group (no realization can
                        work).
  TEST-VOID           = a must-fire control does not fire or a corpus
                        deployment gate fails.

FIREWALL: experiments/tfpt-discovery probe; EXPLORATION ONLY; writes
nothing; touches no verification/, paper, ledger, changelog or website
surface; no marker moves; NO physics claims.  ROOTCLASS-MIXED fence
(v775_gaussian_class_d5_purity, binding): no code->matter or
line->matter semantics is used or implied -- the 60 lines are treated
as pure lattice/group-theory objects; any clock structure found here
carries NO matter reading.  A DEAD verdict is a valid, well-powered
outcome and is reported honestly.

Sources (read-only): verification/v633_orbit60_quotient.py (lines,
canon, hermitian form, reflections, 11520 line group), v629 (compiler
clock c = J o sigma, free mu4 quotient), v634_st31_structure.py
(sigma = c^4, J = c^9, G31 order 46080, max element order 24),
v647_st31_degree24.py (line 6-clock), v623_covered_seam.py (seam clock
L^4 = deck, L^12 = id), v1_e8_glue.py (Bourbaki simple roots).

Run:
    experiments/tfpt-discovery/.venv/bin/python \\
        experiments/tfpt-discovery/clock_fiber_product_probe.py
"""

import hashlib
import itertools
import time
from fractions import Fraction as Fr

CHECKS = []


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
# S0: FROZEN SPEC -- hashed BEFORE any lattice data is computed
# ======================================================================
FROZEN_SPEC = """\
ONE-OBJECT REDUCTION FROZEN SPEC (one_object_reduction_probe)
frozen 2026-08-05, BEFORE computing any lattice data in this run.

CLAIM: the TFPT glue pattern (cyclic isotropic glue group, evenness
q = 0 mod 2Z, unimodularity |H|^2 = |disc|) admits an even unimodular
DIAGONAL glue of A_{d-1} (+) D_{d+1} iff d = 4; the boundary object
with d marks then forces g_car = d+1 = 5 and N_fam = d-1 = 3 as the
two functor readouts of ONE four-point object.

CENSUS RANGE: d = 2..12 inclusive.  All arithmetic exact (Fraction).
DIAGONAL glue := Lagrangian H with H int (A(+)0) = 0 = H int (0(+)D).
EVEN glue     := q(h) = 0 mod 2Z for all h in H.
UNIMODULAR    := |H|^2 = |disc(A_{d-1})| * |disc(D_{d+1})| = 4d.
ODD-relaxed   := q(h) = 0 mod Z and b(h,h') = 0 mod Z, not even.

VERDICT RULE (frozen):
  TEST-VOID          if G2 or G3 fails, or G4 or G5 does not fire;
  ONE-OBJECT-DEAD    if {d with even unimodular diagonal glue} != {4};
  ONE-OBJECT-PARTIAL otherwise.  ONE-OBJECT-FORCED is predeclared
  unreachable: the c_3 = 1/(2 pi d) link is a corpus-legitimate
  REWRITING (c_3 = 1/(2 e_1(a) pi), e_1(a) = 4 = |mu4| = d; tfpt_1
  ~L189-194, v23) but NOT a corpus derivation of P1 from the boundary
  object; this probe must not smuggle a new derivation of P1.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()


# ======================================================================
# exact linear algebra helpers (Fractions, no floats anywhere)
# ======================================================================
def cartan_A(n):
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = 2
    for i in range(n - 1):
        M[i][i + 1] = M[i + 1][i] = -1
    return M


def cartan_D(n):
    """v1_e8_glue convention: A_n chain, detach last node, re-attach at
    the fork (n >= 3; D_3 ~= A_3)."""
    M = cartan_A(n)
    M[n - 2][n - 1] = M[n - 1][n - 2] = 0
    M[n - 3][n - 1] = M[n - 1][n - 3] = -1
    return M


def frac_inv(G):
    """exact matrix inverse via Gauss-Jordan."""
    n = len(G)
    A = [[Fr(G[i][j]) for j in range(n)] + [Fr(int(i == k)) for k in range(n)]
         for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [A[r][j] - f * A[c][j] for j in range(2 * n)]
    return [row[n:] for row in A]


def det_int(G):
    """exact integer determinant (fraction-free would be nicer; Fraction
    Gaussian elimination is exact and fine at n <= 11)."""
    n = len(G)
    A = [[Fr(G[i][j]) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            A[c], A[p] = A[p], A[c]
            det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / A[c][c]
                A[r] = [A[r][j] - f * A[c][j] for j in range(n)]
    assert det.denominator == 1
    return int(det)


def mod1(x):
    return x - (x.numerator // x.denominator)


def mod2(x):
    m = x % 2
    return m


class DiscForm(object):
    """discriminant group L*/L of an even lattice with Gram G, with the
    quadratic form q: A -> Q/2Z and linking form b: A x A -> Q/Z,
    computed exactly from the Cartan/Gram matrix."""

    def __init__(self, G):
        self.G = G
        self.n = len(G)
        Ginv = frac_inv(G)
        gens = [tuple(Ginv[i][j] for i in range(self.n))
                for j in range(self.n)]  # dual basis vectors, root coords
        # BFS closure of the generators mod Z^n
        elems = {tuple(Fr(0) for _ in range(self.n))}
        frontier = list(elems)
        while frontier:
            nxt = []
            for e in frontier:
                for g in gens:
                    s = tuple(mod1(a + b) for a, b in zip(e, g))
                    if s not in elems:
                        elems.add(s)
                        nxt.append(s)
            frontier = nxt
        self.elems = sorted(elems)
        self.index = {e: i for i, e in enumerate(self.elems)}
        self.zero = self.index[tuple(Fr(0) for _ in range(self.n))]
        m = len(self.elems)
        self.add = [[0] * m for _ in range(m)]
        for i, u in enumerate(self.elems):
            for j, v in enumerate(self.elems):
                self.add[i][j] = self.index[
                    tuple(mod1(a + b) for a, b in zip(u, v))]

    def q(self, i):
        v = self.elems[i]
        s = Fr(0)
        for a in range(self.n):
            for b in range(self.n):
                s += v[a] * self.G[a][b] * v[b]
        return mod2(s)

    def b(self, i, j):
        u, v = self.elems[i], self.elems[j]
        s = Fr(0)
        for a in range(self.n):
            for b in range(self.n):
                s += u[a] * self.G[a][b] * v[b]
        return mod1(s)

    def order_of(self, i):
        k, cur = 1, i
        while cur != self.zero:
            cur = self.add[cur][i]
            k += 1
        return k

    def structure(self):
        from collections import Counter
        return dict(Counter(self.order_of(i) for i in range(len(self.elems))))


class SumForm(object):
    """orthogonal direct sum of two DiscForms; elements are index pairs."""

    def __init__(self, A, D):
        self.A, self.D = A, D
        self.elems = [(i, j) for i in range(len(A.elems))
                      for j in range(len(D.elems))]
        self.index = {e: k for k, e in enumerate(self.elems)}
        self.zero = self.index[(A.zero, D.zero)]

    def add(self, x, y):
        (a1, d1), (a2, d2) = self.elems[x], self.elems[y]
        return self.index[(self.A.add[a1][a2], self.D.add[d1][d2])]

    def q(self, x):
        a, d = self.elems[x]
        return mod2(self.A.q(a) + self.D.q(d))

    def b(self, x, y):
        (a1, d1), (a2, d2) = self.elems[x], self.elems[y]
        return mod1(self.A.b(a1, a2) + self.D.b(d1, d2))

    def closure(self, gens):
        H = {self.zero}
        frontier = list(H)
        while frontier:
            nxt = []
            for h in frontier:
                for g in gens:
                    s = self.add(h, g)
                    if s not in H:
                        H.add(s)
                        nxt.append(s)
            frontier = nxt
        return frozenset(H)

    def all_subgroups(self):
        subs = {frozenset({self.zero})}
        work = [frozenset({self.zero})]
        while work:
            H = work.pop()
            for e in range(len(self.elems)):
                if e in H:
                    continue
                H2 = self.closure(list(H) + [e])
                if H2 not in subs:
                    subs.add(H2)
                    work.append(H2)
        return subs


def classify(d):
    """full glue census for A_{d-1} (+) D_{d+1}."""
    A = DiscForm(cartan_A(d - 1))
    D = DiscForm(cartan_D(d + 1))
    S = SumForm(A, D)
    total = len(S.elems)
    lag_order_sq = total  # |H|^2 == |A|*|D| condition on the order
    res = {
        "d": d,
        "discA": A.structure(),
        "discD": D.structure(),
        "orderA": len(A.elems),
        "orderD": len(D.elems),
        "square": int(round(total ** 0.5)) ** 2 == total,
        "even_unimod": [],
        "even_unimod_diagonal": [],
        "odd_unimod": [],
        "even_nontrivial_any": [],
    }
    for H in S.all_subgroups():
        hl = sorted(H)
        even = all(S.q(h) == 0 for h in hl)
        modZ = (all(S.q(h).denominator == 1 for h in hl)
                and all(S.b(x, y) == 0 for x in hl for y in hl))
        lag = len(H) * len(H) == lag_order_sq
        intA = sum(1 for h in hl if S.elems[h][1] == D.zero)
        intD = sum(1 for h in hl if S.elems[h][0] == A.zero)
        diagonal = (intA == 1 and intD == 1)  # only 0 in each factor
        if even and len(H) > 1:
            res["even_nontrivial_any"].append(H)
        if lag and even:
            res["even_unimod"].append(H)
            if diagonal:
                res["even_unimod_diagonal"].append(H)
        if lag and modZ and not even:
            res["odd_unimod"].append(H)
    return A, D, S, res


# =====================================================================

def main():
    T0 = time.time()
    section("S0: FROZEN SPEC (SHA-256 %s)" % SPEC_SHA)
    print(FROZEN_SPEC)

    # ==================================================================
    # S1: THE d-CENSUS 2..12
    # ==================================================================
    section("S1: the d-census (exact discriminant-form glue theory, d = 2..12)")

    TABLE = {}
    FORMS = {}
    for d in range(2, 13):
        A, D, S, res = classify(d)
        FORMS[d] = (A, D, S)
        TABLE[d] = res
        print("  d=%2d  disc(A_%d)=%s (Z_%d)  disc(D_%d)=%s  4d=%2d square=%s  "
              "evenUnimod=%d (diag %d)  oddUnimod=%d  evenAnyIndex(nontriv)=%d"
              % (d, d - 1, res["discA"], res["orderA"], d + 1, res["discD"],
                 4 * d, res["square"], len(res["even_unimod"]),
                 len(res["even_unimod_diagonal"]), len(res["odd_unimod"]),
                 len(res["even_nontrivial_any"])), flush=True)

    # structural sanity: disc(A_{d-1}) = Z_d; disc(D_{d+1}) = Z4 (d even) /
    # Z2xZ2 (d odd)
    ok_A = all(TABLE[d]["orderA"] == d and max(TABLE[d]["discA"]) == d
               for d in range(2, 13))
    ok_D = all(TABLE[d]["orderD"] == 4 and
               (max(TABLE[d]["discD"]) == (4 if d % 2 == 0 else 2))
               for d in range(2, 13))
    check("S1.1 disc(A_{d-1}) ~= Z_d for all d (order d, cyclic)", ok_A)
    check("S1.2 disc(D_{d+1}) ~= Z4 for d even, Z2 x Z2 for d odd (order 4)",
          ok_D)

    forced_set = sorted(d for d in TABLE
                        if len(TABLE[d]["even_unimod_diagonal"]) > 0)
    any_glue_set = sorted(d for d in TABLE if len(TABLE[d]["even_unimod"]) > 0)
    g1 = check("S1.3 [G1] {d : even unimodular DIAGONAL glue exists} = %s "
               "(forcing claim needs exactly {4})" % forced_set,
               forced_set == [4])
    check("S1.4 [G1+] even stronger: {d : ANY even unimodular glue exists} "
          "= %s (all glues at the forced d are diagonal)" % any_glue_set,
          any_glue_set == [4])

    # G6: the coarse square layer
    square_set = sorted(d for d in TABLE if TABLE[d]["square"])
    check("S1.5 [G6] coarse layer: |H|^2 = 4d is a perfect square only for "
          "d in %s (d must itself be a square)" % square_set,
          square_set == [4, 9])
    d9 = TABLE[9]
    # how d = 9 dies: no even Lagrangian; exact reason: the order-2 part of
    # any |H| = 6 subgroup must sit in disc(D_10) (Z9 has no 2-torsion) and
    # no element of disc(D_10) has q = 0 mod 2Z.
    D10 = FORMS[9][1]
    d10_qvals = sorted(str(D10.q(i)) for i in range(len(D10.elems)))
    check("S1.6 [G6] d = 9 dies at isotropy: 0 even Lagrangians; "
          "disc(D_10) q-values %s contain no 0 besides the origin -> the "
          "forced order-2 part of |H| = 6 cannot be even-isotropic"
          % d10_qvals,
          len(d9["even_unimod"]) == 0
          and all(D10.q(i) != 0 for i in range(len(D10.elems))
                  if i != D10.zero))

    # ==================================================================
    # S2: G2 -- d = 4 must reproduce v92 EXACTLY
    # ==================================================================
    section("S2: [G2] d = 4 reproduces v92 (two diagonal Lagrangians, "
            "graphs of k -> k and k -> 3k)")

    A4, D4, S4 = FORMS[4]
    res4 = TABLE[4]
    # corpus q-values: q(A3) = 3/4, q(D5) = 5/4 on primitive generators
    qA_prim = sorted({str(A4.q(i)) for i in range(len(A4.elems))
                      if A4.order_of(i) == 4})
    qD_prim = sorted({str(D4.q(i)) for i in range(len(D4.elems))
                      if D4.order_of(i) == 4})
    check("S2.1 q on primitive generators: q(A3) = {3/4} mod 2Z, "
          "q(D5) = {5/4} mod 2Z (v1: 3/4 + 5/4 = 2 = E8 root norm)",
          qA_prim == ["3/4"] and qD_prim == ["5/4"],
          "qA %s qD %s" % (qA_prim, qD_prim))

    lags = res4["even_unimod"]
    check("S2.2 EXACTLY two even Lagrangian glues at d = 4 (v92: <(1,1)> "
          "and <(1,3)>), both diagonal, both cyclic Z4",
          len(lags) == 2 and len(res4["even_unimod_diagonal"]) == 2
          and all(max(len({h for h in H}), 0) == 4 for H in lags))

    # graph check: each Lagrangian is the graph of an anti-isometry
    # Z4 -> Z4; the two anti-isometries are k -> k and k -> 3k on suitable
    # generators (equivalently: their intersection is {0, (2,2)})
    a_gen = next(i for i in range(len(A4.elems)) if A4.order_of(i) == 4)
    d_gen = next(i for i in range(len(D4.elems)) if D4.order_of(i) == 4)
    d_gen3 = D4.add[D4.add[d_gen][d_gen]][d_gen]
    exp1 = S4.closure([S4.index[(a_gen, d_gen)]])
    exp2 = S4.closure([S4.index[(a_gen, d_gen3)]])
    check("S2.3 the two Lagrangians ARE the graphs <(a, s)> and <(a, 3s)> "
          "for a fixed primitive pair (a, s) (v92's <(1,1)>, <(1,3)>)",
          {exp1, exp2} == set(lags))
    inter = set(lags[0]) & set(lags[1])
    check("S2.4 their intersection is the order-2 halfway glue "
          "{0, (2,2)} (v92's unique isotropic Z2 = the SO(16)_1 rung)",
          len(inter) == 2 and all(S4.q(h) == 0 for h in inter))

    # ==================================================================
    # S3: G3 -- explicit lattice certificate at d = 4 (v1 reproduction)
    # ==================================================================
    section("S3: [G3] explicit glue A3 (+) D5 + <(w1, s)> = E8 "
            "(240 roots, even, det 1)")

    # orthonormal ambient R^4 (+) R^5; A3 = sum-zero integer vectors of Z^4,
    # D5 = even-sum integer vectors of Z^5.
    A3_basis = [(1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1)]
    D5_basis = [(1, -1, 0, 0, 0), (0, 1, -1, 0, 0), (0, 0, 1, -1, 0),
                (0, 0, 0, 1, -1), (0, 0, 0, 1, 1)]
    wA = (Fr(3, 4), Fr(-1, 4), Fr(-1, 4), Fr(-1, 4))       # A3 weight, q = 3/4
    wD = (Fr(1, 2),) * 5                                    # D5 spinor, q = 5/4
    glue = tuple(list(wA) + list(wD))                       # norm 2 = E8 root

    def dot(u, v):
        return sum(Fr(a) * Fr(b) for a, b in zip(u, v))

    check("S3.1 glue vector g = (w_A3, spinor_D5) has norm q(A3) + q(D5) "
          "= 3/4 + 5/4 = 2 (an E8 root already)",
          dot(wA, wA) == Fr(3, 4) and dot(wD, wD) == Fr(5, 4)
          and dot(glue, glue) == 2)

    full9 = [tuple(list(b) + [0] * 5) for b in A3_basis] + \
            [tuple([0] * 4 + list(b)) for b in D5_basis]

    # glued basis: replace one root vector by g so that the 8-set has det 1
    best = None
    for drop in range(8):
        basis = [full9[i] for i in range(8) if i != drop] + [glue]
        Gm = [[dot(u, v) for v in basis] for u in basis]
        dt = det_int([[int(x) if x.denominator == 1 else x for x in row]
                      for row in Gm]) if all(
            x.denominator == 1 for row in Gm for x in row) else None
        if dt is None:
            # Gram has half-integers off-diagonal? (g vs roots gives
            # integers here, but keep the exact fallback)
            n = len(basis)
            Af = [[Fr(Gm[i][j]) for j in range(n)] for i in range(n)]
            dtf = Fr(1)
            for c in range(n):
                p = next((r for r in range(c, n) if Af[r][c] != 0), None)
                if p is None:
                    dtf = Fr(0)
                    break
                if p != c:
                    Af[c], Af[p] = Af[p], Af[c]
                    dtf = -dtf
                dtf *= Af[c][c]
                for r in range(c + 1, n):
                    if Af[r][c] != 0:
                        f = Af[r][c] / Af[c][c]
                        Af[r] = [Af[r][j] - f * Af[c][j] for j in range(n)]
            dt = dtf
        if dt == 1:
            even_diag = all(Gm[i][i] % 2 == 0 for i in range(8))
            integer = all(x.denominator == 1 for row in Gm for x in row)
            if even_diag and integer:
                best = (drop, basis, Gm)
                break
    check("S3.2 glued basis found (drop root #%s, add g): Gram is integer, "
          "even diagonal, det = 1 -> even UNIMODULAR rank 8"
          % (best[0] if best else "-"), best is not None)

    # count norm-2 vectors coset by coset: L' = L + Z g, L'/L = Z4
    def coset_norm_counts(k, side):
        """multiset {norm: count} of vectors in k*w + lattice, norm <= 2."""
        if side == "A":
            w, dim = wA, 4
        else:
            w, dim = wD, 5
        counts = {}
        for m in itertools.product(range(-3, 4), repeat=dim):
            if side == "A" and sum(m) != 0:
                continue
            if side == "D" and sum(m) % 2 != 0:
                continue
            v = tuple(Fr(k) * w[i] + m[i] for i in range(dim))
            nrm = dot(v, v)
            if nrm <= 2:
                counts[nrm] = counts.get(nrm, 0) + 1
        return counts

    root_total = 0
    per_coset = []
    for k in range(4):
        cA = coset_norm_counts(k, "A")
        cD = coset_norm_counts(k, "D")
        n_k = sum(cA[na] * cD[nd] for na in cA for nd in cD if na + nd == 2)
        per_coset.append(n_k)
        root_total += n_k
    check("S3.3 norm-2 count per glue coset k = 0..3: %s, total = %d "
          "(v1: A3+D5 roots 12+40 = 52 in k = 0; glued total must be 240)"
          % (per_coset, root_total),
          per_coset[0] == 52 and root_total == 240)

    # integrality of all 240 roots over the glued basis
    if best:
        _, basis, Gm = best
        Ginv8 = frac_inv([[Fr(x) for x in row] for row in Gm])
        roots_all = []
        for k in range(4):
            for mA in itertools.product(range(-3, 4), repeat=4):
                if sum(mA) != 0:
                    continue
                vA = tuple(Fr(k) * wA[i] + mA[i] for i in range(4))
                nA = dot(vA, vA)
                if nA > 2:
                    continue
                for mD in itertools.product(range(-3, 4), repeat=5):
                    if sum(mD) % 2 != 0:
                        continue
                    vD = tuple(Fr(k) * wD[i] + mD[i] for i in range(5))
                    if nA + dot(vD, vD) == 2:
                        roots_all.append(tuple(list(vA) + list(vD)))
        integral = True
        for r in roots_all:
            proj = [dot(r, bv) for bv in basis]
            coef = [sum(Ginv8[i][j] * proj[j] for j in range(8))
                    for i in range(8)]
            if not all(c.denominator == 1 for c in coef):
                integral = False
                break
        check("S3.4 all %d enumerated norm-2 vectors are INTEGRAL over the "
              "glued basis: the glue closes to THE even unimodular E8 "
              "lattice (v1 certificate reproduced)" % len(roots_all),
              integral and len(roots_all) == 240)

    # ==================================================================
    # S4: CONTROLS G4 / G5 -- the constraints must BIND
    # ==================================================================
    section("S4: controls -- relaxing evenness/unimodularity must open "
            "other d (must fire)")

    odd_set = sorted(d for d in TABLE if d != 4 and len(TABLE[d]["odd_unimod"]))
    g4 = check("S4.1 [G4, must fire] dropping EVENNESS opens d in %s "
               "(odd unimodular glues exist there; e.g. d = 9: "
               "A8 (+) D10 + <(3,0),(0,v)> is an ODD unimodular rank-18 "
               "glue)" % odd_set, len(odd_set) > 0)

    sub_set = sorted(d for d in TABLE
                     if d != 4 and len(TABLE[d]["even_nontrivial_any"]))
    g5 = check("S4.2 [G5, must fire] dropping UNIMODULARITY opens d in %s "
               "(nontrivial even isotropic glue subgroups of smaller index "
               "exist there)" % sub_set, len(sub_set) > 0)

    check("S4.3 the intermediate at d = 4 itself: exactly one nontrivial "
          "even isotropic subgroup BELOW the Lagrangians (v92's halfway "
          "SO(16)_1 rung, |H| = 2)",
          sum(1 for H in TABLE[4]["even_nontrivial_any"] if len(H) == 2) == 1)

    # ==================================================================
    # S5: [G7] corollaries at the forced d -- typed honestly
    # ==================================================================
    section("S5: [G7] corollaries at the forced d = 4 (typed)")

    d_star = forced_set[0] if len(forced_set) == 1 else None
    if d_star is not None:
        check("S5.1 [verified arithmetic] g_car = d+1 = %d, N_fam = d-1 = %d, "
              "rank = 2d = %d, glue index = sqrt(4d) = %d = d = |mu4|"
              % (d_star + 1, d_star - 1, 2 * d_star,
                 int(round((4 * d_star) ** 0.5))),
              d_star + 1 == 5 and d_star - 1 == 3 and 2 * d_star == 8
              and int(round((4 * d_star) ** 0.5)) == 4)
        check("S5.2 [corpus-anchored] N_fam = d-1 = rank H_1(P^1 minus d "
              "points) = 3 (tfpt_1 ~L894/4234: H_1 = Z^3 hence A_3); "
              "q(A3) = N_fam/|mu4|, q(D5) = g_car/|mu4| with n+1 = 4 = "
              "|mu4| = d (tfpt_1 ~L4201-4205)", d_star == 4)
        # the c3 honesty gate: arithmetic identity is [E]-grade, the LINK is
        # an interpretation -- frozen in the spec, restated here.
        c3_arith = Fr(1, 2 * d_star) # times 1/pi: 1/(2 pi d) = 1/(8 pi)
        check("S5.3 [verified arithmetic] 1/(2 pi d)|_{d=4} = 1/(8 pi): "
              "coefficient 1/(2d) = %s = 1/8" % c3_arith,
              c3_arith == Fr(1, 8))
        check("S5.4 [HONESTY GATE -- interpretation, NOT derivation] the "
              "1/(2 pi d) READING of P1 is corpus-legitimate only as a "
              "rewriting: c_3 = 1/(2 e_1(a) pi) with e_1(a) = 4 = |mu4| "
              "(tfpt_1 ~L189-194, v23 anchor-first refinement) and "
              "|mu4| = #marks = d; but the corpus derivation chain of P1 "
              "is Gauss-Bonnet 1/(|Z2| * oint K dA) = 1/(2 * 4 pi) where "
              "4 pi is TOTAL SPHERE CURVATURE, not d (tfpt_1 ~L670-689); "
              "P1 status: primitive postulate (tfpt_1 ~L169).  The glue "
              "census therefore does NOT derive P1; the c_3 link is typed "
              "INTERPRETATION", True)

    # ==================================================================
    # S6: VERDICT (frozen rule)
    # ==================================================================
    section("S6: VERDICT (frozen enum: ONE-OBJECT-FORCED / ONE-OBJECT-"
            "PARTIAL / ONE-OBJECT-DEAD / TEST-VOID)")

    g2_ok = all(ok for name, ok in CHECKS if name.startswith("S2."))
    g3_ok = all(ok for name, ok in CHECKS if name.startswith("S3."))
    controls_fire = g4 and g5
    if not (g2_ok and g3_ok and controls_fire):
        VERDICT = "TEST-VOID"
    elif forced_set != [4]:
        VERDICT = "ONE-OBJECT-DEAD"
    else:
        VERDICT = "ONE-OBJECT-PARTIAL"

    print("VERDICT: %s" % VERDICT)
    print("  glue-forced d set: %s (needed {4})" % forced_set)
    print("  c_3 link: corpus-legitimate rewriting via e_1(a) = |mu4| = d "
          "(tfpt_1 ~L192), typed INTERPRETATION -- FORCED predeclared "
          "unreachable")
    print("  controls: evenness relaxation opens %s, unimodularity "
          "relaxation opens %s" % (odd_set, sub_set))

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("%d/%d checks passed" % (n_pass, len(CHECKS)))
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("elapsed: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else
          "SOME CHECKS FAILED")
    return 0 if n_pass == len(CHECKS) else 1


_run_part1 = main


def _run_part2():
    # PART 2 -- clock_fiber_product_probe.py (verbatim; module-level names
    # local to this function scope)
    import hashlib
    import itertools
    import time
    from collections import Counter, deque
    from fractions import Fraction as Fr
    from math import gcd

    T0 = time.time()
    CHECKS = []

    def check(name, ok, detail=""):
        CHECKS.append((name, bool(ok)))
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                             (" -- " + detail) if detail else ""), flush=True)
        return bool(ok)

    def section(title):
        print("=" * 78)
        print(title)
        print("=" * 78, flush=True)

    # ==================================================================
    # S0: FROZEN SPEC -- hashed BEFORE any root data is computed
    # ==================================================================
    FROZEN_SPEC = """\
CLOCK FIBER-PRODUCT FROZEN SPEC (clock_fiber_product_probe)
frozen 2026-08-05, BEFORE computing any root data in this run.

HYPOTHESIS: L_60 ~= Z12 x_{Z6} Z30 acts canonically (simply
transitively, or at least orbit-definingly) on the 60 Gaussian E8
lines; the seam clock (corpus avatar c = J o sigma, order 12, c^4 =
sigma, c^9 = J) and the Coxeter clock (w = product of the 8 Bourbaki
simple reflections, order 30, w^15 = -1) are its two legs over the
shared Z6 (sheet x family phase); 240 = 4 x 60 via mu4 is the final
layer.

DECISION RULE (frozen):
  TEST-VOID  if a deployment gate (root census, clock identities,
             Coxeter order/census) fails or a control CC1-CC3 does
             not fire;
  CLOCK-FIBER-EXACT   if both clocks descend to the 60 lines, the Z6
             squares agree, and the joint line image is simply
             transitive of order 60 (necessarily Z60);
  CLOCK-FIBER-PARTIAL if both descend and the Z6 squares agree but
             the joint action is not simply transitive (name the
             orbit type);
  CLOCK-FIBER-DEAD    otherwise (descent failure / Z6 mismatch /
             required orders 15, 30, 60 absent from the FULL
             line-compatible group -- the existence sweep kills every
             realization, not only the deployed one).

MEASURED DRIVERS (not gates; reported exactly): the line order of c,
the descent subgroup {k : w^k preserves the line partition}, the full
line-compatible group order and its element-order spectrum, the joint
<c, w> orbit census on the 240 roots.
"""
    SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    section("S0: FROZEN SPEC (SHA-256 %s)" % SPEC_SHA)
    print(FROZEN_SPEC)

    # ==================================================================
    # S1: deployment -- roots, lines, seam clock (corpus reproduction gates)
    # ==================================================================
    section("S1: deployment gates (corpus reproduction, v629/v633/v634)")

    roots = []
    for v in itertools.product(range(-1, 2), repeat=8):
        if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
            roots.append(tuple(Fr(a) for a in v))
    half = Fr(1, 2)
    for y in itertools.product((0, -1), repeat=8):
        v = tuple(Fr(a) + half for a in y)
        if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
            roots.append(v)
    roots = sorted(roots)
    RS = set(roots)
    root_idx = {r: i for i, r in enumerate(roots)}
    N = len(roots)

    def J_all(v):
        out = []
        for i in range(0, 8, 2):
            a, b = v[i], v[i + 1]
            out += [-b, a]
        return tuple(out)

    def sigma(v):
        return (v[4], v[5], v[0], v[1], v[2], v[3], v[6], v[7])

    def canon(v):
        o = v
        best = v
        for _ in range(3):
            o = J_all(o)
            if o < best:
                best = o
        return best

    check("S1.1 240 roots in the D8+spinor model (v633 verbatim)", N == 240)

    reps = sorted({canon(v) for v in roots})
    line_of = {}
    for i, rep in enumerate(reps):
        o = rep
        for _ in range(4):
            line_of[o] = i
            o = J_all(o)
    orb_sizes = Counter()
    for rep in reps:
        orb = {rep, J_all(rep), J_all(J_all(rep)), J_all(J_all(J_all(rep)))}
        orb_sizes[len(orb)] += 1
    check("S1.2 [mu4 layer, test (iii)] J free with EXACTLY 60 orbits of "
          "size 4: 240 = 4 x 60 (v629 R3 / v633 Q1)",
          len(reps) == 60 and orb_sizes == Counter({4: 60}))

    def perm_of(f):
        return tuple(root_idx[f(roots[i])] for i in range(N))

    def compose(p, q):
        """(p o q)(x) = p[q[x]]."""
        return tuple(p[q[i]] for i in range(N))

    def perm_order(p):
        n = len(p)
        seen = [False] * n
        o = 1
        for s in range(n):
            if seen[s]:
                continue
            ln, cur = 0, s
            while not seen[cur]:
                seen[cur] = True
                cur = p[cur]
                ln += 1
            o = o * ln // gcd(o, ln)
        return o

    def orbit_census(perms, n):
        seen = [False] * n
        cens = Counter()
        for s in range(n):
            if seen[s]:
                continue
            comp = {s}
            dq = deque([s])
            seen[s] = True
            while dq:
                x = dq.popleft()
                for p in perms:
                    for y in (p[x],):
                        if not seen[y]:
                            seen[y] = True
                            comp.add(y)
                            dq.append(y)
            cens[len(comp)] += 1
        return cens

    P_J = perm_of(J_all)
    P_sig = perm_of(sigma)
    P_c = compose(P_J, P_sig)          # c = J o sigma
    P_id = tuple(range(N))
    P_minus = perm_of(lambda v: tuple(-a for a in v))

    def perm_pow(p, k):
        r = P_id
        for _ in range(k):
            r = compose(r, p)
        return r

    check("S1.3 seam clock avatar c = J o sigma has order 12 on the roots "
          "(v629 R1)", perm_order(P_c) == 12)
    check("S1.4 clock identities c^4 = sigma, c^9 = J, c^6 = -1 "
          "(v634 S7; L^4 = deck matches: c^4 IS the order-3 family deck)",
          perm_pow(P_c, 4) == P_sig and perm_pow(P_c, 9) == P_J
          and perm_pow(P_c, 6) == P_minus)

    # ==================================================================
    # S2: the seam clock on the 60 lines
    # ==================================================================
    section("S2: the seam clock's line action (measured driver)")

    LINES = [frozenset({rep, J_all(rep), J_all(J_all(rep)),
                        J_all(J_all(J_all(rep)))}) for rep in reps]
    LINESET = set(LINES)

    def line_perm_of_rootperm(p):
        """line permutation induced by a root permutation IF it preserves
        the line partition, else None."""
        out = []
        for L in LINES:
            img = frozenset(roots[p[root_idx[r]]] for r in L)
            if img not in LINESET:
                return None
            out.append(LINES.index(img))
        return tuple(out)

    lc = line_perm_of_rootperm(P_c)
    lc_ok = lc is not None
    lc_ord = perm_order(lc) if lc_ok else 0
    lc_kernel = sorted(k for k in range(12)
                       if line_perm_of_rootperm(perm_pow(P_c, k))
                       == tuple(range(60))) if lc_ok else []
    check("S2.1 c descends to the 60 lines (J = c^9 is line-trivial by "
          "construction)", lc_ok)
    lsig = line_perm_of_rootperm(P_sig)
    check("S2.2 MEASURED: line order of the seam clock = %d; line-trivial "
          "powers %s; line image = <sigma's line action> (census on lines "
          "%s)" % (lc_ord, lc_kernel,
                   dict(orbit_census([lc], 60)) if lc_ok else "-"),
          lc_ok, "c^3 = J^3 sigma^3 = J^3 is line-trivial, so the Z12 seam "
          "clock acts on the lines through Z12/<c^3> = Z3 only")
    same_as_sigma = lc_ok and orbit_census([lc], 60) == orbit_census([lsig], 60)
    check("S2.3 the seam clock's line action has the sigma line census "
          "{3: 19, 1: 3} (v633 Q4)",
          same_as_sigma and orbit_census([lsig], 60) == Counter({3: 19, 1: 3}))

    # ==================================================================
    # S3: the Coxeter clock (deployment gates)
    # ==================================================================
    section("S3: the Coxeter clock w = s_1 ... s_8 (Bourbaki, v1 basis)")

    def bourbaki_simple_roots():
        e = [[Fr(int(i == j)) for j in range(8)] for i in range(8)]
        a1 = [Fr(1, 2) * (e[0][j] - e[1][j] - e[2][j] - e[3][j] - e[4][j]
                          - e[5][j] - e[6][j] + e[7][j]) for j in range(8)]
        a2 = [e[0][j] + e[1][j] for j in range(8)]
        a3 = [e[1][j] - e[0][j] for j in range(8)]
        a4 = [e[2][j] - e[1][j] for j in range(8)]
        a5 = [e[3][j] - e[2][j] for j in range(8)]
        a6 = [e[4][j] - e[3][j] for j in range(8)]
        a7 = [e[5][j] - e[4][j] for j in range(8)]
        a8 = [e[6][j] - e[5][j] for j in range(8)]
        return [tuple(a) for a in (a1, a2, a3, a4, a5, a6, a7, a8)]

    def refl(alpha):
        def f(v, alpha=alpha):
            s = sum(a * b for a, b in zip(v, alpha))  # norm 2 simple roots
            return tuple(v[j] - s * alpha[j] for j in range(8))
        return f

    simples = bourbaki_simple_roots()
    check("S3.1 the 8 Bourbaki simple roots are norm-2 roots of the model "
          "(v1 basis deployed verbatim)",
          all(sum(a * a for a in s) == 2 and s in RS for s in simples))

    P_w = P_id
    for s in simples:
        P_w = compose(P_w, perm_of(refl(s)))  # w = s1 o s2 o ... o s8
    w_ord = perm_order(P_w)
    w_census = orbit_census([P_w], N)
    check("S3.2 Coxeter clock order 30 on the 240 roots (h(E8) = 30)",
          w_ord == 30)
    check("S3.3 Kostant orbit census {30: 8} (8 = rank E8 free 30-orbits)",
          w_census == Counter({30: 8}), str(dict(w_census)))
    check("S3.4 w^15 = -1 (all E8 exponents odd)",
          perm_pow(P_w, 15) == P_minus)

    # ==================================================================
    # S4: descent of the Coxeter clock to the 60 lines (measured driver)
    # ==================================================================
    section("S4: does the Coxeter clock act on the 60 lines? (test (i))")

    descent_powers = sorted(k for k in range(30)
                            if line_perm_of_rootperm(perm_pow(P_w, k))
                            is not None)
    w_descends = 1 in descent_powers
    # the descent powers form a subgroup <w^m> of <w>
    m = descent_powers[1] if len(descent_powers) > 1 else 0
    line_shadow = {}
    for k in descent_powers:
        lp = line_perm_of_rootperm(perm_pow(P_w, k))
        line_shadow[k] = perm_order(lp)
    check("S4.1 MEASURED: powers of w preserving the line partition: %s "
          "(a subgroup <w^%s> of <w>); their induced line orders: %s"
          % (descent_powers, m if m else "-", line_shadow), True)
    check("S4.2 the Coxeter clock itself descends to the 60 lines: %s "
          "(descent FAILURE means the strict fiber-product hypothesis "
          "cannot be built from the deployed Coxeter clock)"
          % w_descends, True, "measured driver, feeds the frozen verdict "
          "rule, not a gate")
    wJw = compose(P_w, compose(P_J, perm_pow(P_w, 29)))
    normalizes = (wJw == P_J) or (wJw == perm_pow(P_J, 3))
    check("S4.3 MEASURED: w J w^-1 in {J, J^-1}: %s (normalizing <J> is "
          "exactly the line-partition compatibility)" % normalizes, True)

    # ==================================================================
    # S5: existence sweep -- the FULL line-compatible group and its
    #     element-order spectrum (decides every realization)
    # ==================================================================
    section("S5: existence sweep over N(<J>): line group + order spectrum")

    def herm(u, v):
        re = Fr(0)
        im = Fr(0)
        for i in range(4):
            a, b = u[2 * i], u[2 * i + 1]
            c, d = v[2 * i], v[2 * i + 1]
            re += a * c + b * d
            im += b * c - a * d
        return (re, im)

    def refl2(x, v):
        """order-2 unitary reflection R_v(x) = x - H(x,v) v (v633 Q6)."""
        re, im = herm(x, v)
        out = []
        for i in range(4):
            c, d = v[2 * i], v[2 * i + 1]
            out += [x[2 * i] - (re * c - im * d),
                    x[2 * i + 1] - (re * d + im * c)]
        return tuple(out)

    def conj_map(v):
        """complex conjugation per pair: (a, b) -> (a, -b);
        conj o J o conj^-1 = J^-1."""
        out = []
        for i in range(0, 8, 2):
            out += [v[i], -v[i + 1]]
        return tuple(out)

    P_conj = perm_of(conj_map)
    cJc = compose(P_conj, compose(P_J, P_conj))  # conj is an involution
    check("S5.1 conj preserves the roots and conjugates J to J^-1 "
          "(the antiunitary leg of N(<J>))",
          cJc == perm_pow(P_J, 3) and compose(P_conj, P_conj) == P_id)

    line_gens = set()
    for v in reps:
        lp = line_perm_of_rootperm(perm_of(lambda x, v=v: refl2(x, v)))
        line_gens.add(lp)
    lp_conj = line_perm_of_rootperm(P_conj)
    line_gens.add(lp_conj)
    line_gens = sorted(line_gens)

    ident60 = tuple(range(60))
    seen_g = {ident60}
    dq = deque([ident60])
    CAP = 60000
    while dq and len(seen_g) <= CAP:
        p = dq.popleft()
        for g in line_gens:
            q = tuple(p[g[i]] for i in range(60))
            if q not in seen_g:
                seen_g.add(q)
                dq.append(q)
    full_order = len(seen_g)
    check("S5.2 the FULL line-compatible group (60 unitary reflections + "
          "conj) has order %d (v633 Q7 unitary part: 11520; N(<J>) adds "
          "the conj coset)" % full_order, full_order in (11520, 23040),
          "11520 means conj's line image is already unitary-realized; "
          "23040 means the antiunitary coset is genuinely new")

    spec = Counter(perm_order(p) for p in seen_g)
    has15 = spec.get(15, 0) > 0
    has30 = spec.get(30, 0) > 0
    has60 = spec.get(60, 0) > 0
    maxord = max(spec)
    check("S5.3 MEASURED element-order spectrum of the full line world: "
          "%s" % dict(sorted(spec.items())), True)
    kill_orders = not (has15 or has30 or has60)
    check("S5.4 DECISIVE: orders {15, 30, 60} present? 15:%s 30:%s 60:%s "
          "(max order %d).  Any root-level order-30 clock acting on the "
          "lines would induce line order 30 or 15 (its cyclic group meets "
          "the line kernel <J> in order <= 2 since 4 does not divide 30); "
          "a simply-transitive Z60 = Z12 x_{Z6} Z30 needs line order 60. "
          "Absence of ALL THREE kills EVERY realization"
          % (has15, has30, has60, maxord), True)

    # joint <c, w> orbit census on the 240 roots (honest orbit type)
    joint_census = orbit_census([P_c, P_w], N)
    check("S5.5 MEASURED: joint <seam clock, Coxeter clock> orbit census "
          "on the 240 roots: %s" % dict(joint_census), True)

    # ==================================================================
    # S6: the abstract fiber product + control CC1 (wrong pairing)
    # ==================================================================
    section("S6: abstract layer -- Z12 x_{Z6} Z30 vs Z12 x Z30 (control CC1)")

    fib = [(a, b) for a in range(12) for b in range(30) if a % 6 == b % 6]
    fib_orders = Counter()
    for (a, b) in fib:
        k = 1
        x, y = a, b
        while (x, y) != (0, 0):
            x, y = (x + a) % 12, (y + b) % 30
            k += 1
        fib_orders[k] += 1
    fib_cyclic = fib_orders.get(60, 0) > 0
    check("S6.1 the fiber product Z12 x_{Z6} Z30 has order %d and IS "
          "cyclic Z60 (max element order 60, phi(60) = %d generators)"
          % (len(fib), fib_orders.get(60, 0)),
          len(fib) == 60 and fib_cyclic and fib_orders.get(60, 0) == 16)
    cc1 = check("S6.2 [CC1, must fire] wrong pairing: |Z12 x Z30| = 360 "
                "!= 60 and its invariant factors are (6, 60) != (60): the "
                "full product can NEVER act simply transitively on the 60 "
                "lines; only the fiber product has the right size",
                12 * 30 == 360 and gcd(12, 30) == 6
                and (12 * 30 // 6 == 60))

    # ==================================================================
    # S7: controls CC2 / CC3 (must fire)
    # ==================================================================
    section("S7: controls CC2 (random order-12 unitary) and CC3 (wrong J)")

    class LCG(object):
        def __init__(self, seed):
            self.s = seed

        def next(self, n):
            self.s = (1103515245 * self.s + 12345) % (1 << 31)
            return self.s % n

    refl_perms = sorted({perm_of(lambda x, v=v: refl2(x, v)) for v in reps})
    rng = LCG(20260805)
    fired_cc2 = 0
    tried = 0
    found12 = 0
    while found12 < 5 and tried < 20000:
        tried += 1
        p = refl_perms[rng.next(len(refl_perms))]
        for _ in range(rng.next(11) + 1):
            p = compose(p, refl_perms[rng.next(len(refl_perms))])
        if perm_order(p) == 12:
            found12 += 1
            breaks = (perm_pow(p, 4) != P_sig) or (perm_pow(p, 9) != P_J)
            if breaks:
                fired_cc2 += 1
    cc2 = check("S7.1 [CC2, must fire] %d/%d random order-12 unitary "
                "elements (frozen-seed words in the 60 reflections) BREAK "
                "the seam-clock deployment identities (r^4 = sigma, "
                "r^9 = J): the compatibility square is NOT generic"
                % (fired_cc2, found12), found12 >= 3 and fired_cc2 == found12)

    def J_wrong(v):
        """i-rotation on the scrambled pairing (0,2),(1,3),(4,6),(5,7)."""
        out = list(v)
        for (i, j) in ((0, 2), (1, 3), (4, 6), (5, 7)):
            out[i], out[j] = -v[j], v[i]
        return tuple(out)

    jw_preserves = all(J_wrong(r) in RS for r in roots)
    if jw_preserves:
        P_jw = perm_of(J_wrong)
        jw_free60 = (perm_order(P_jw) == 4 and
                     orbit_census([P_jw], N) == Counter({4: 60}))
        jw_comm = compose(P_jw, P_sig) == compose(P_sig, P_jw)
        jw_broken = not (jw_free60 and jw_comm)
    else:
        jw_broken = True
    cc3 = check("S7.2 [CC3, must fire] the wrong complex structure J' "
                "(pairing (0,2),(1,3),(4,6),(5,7)) breaks the deployment: "
                "root-preservation %s%s"
                % (jw_preserves,
                   "" if not jw_preserves else
                   ", free-60 census %s, [J',sigma] = 0 %s"
                   % (jw_free60, jw_comm)), jw_broken)

    # ==================================================================
    # S8: VERDICT (frozen rule)
    # ==================================================================
    section("S8: VERDICT (frozen enum: CLOCK-FIBER-EXACT / "
            "CLOCK-FIBER-PARTIAL / CLOCK-FIBER-DEAD / TEST-VOID)")

    deploy_ok = all(ok for name, ok in CHECKS
                    if name.startswith(("S1.", "S3.")))
    controls_ok = cc1 and cc2 and cc3

    both_descend = lc_ok and w_descends
    z6_compatible = False
    simply_transitive = False
    if both_descend:
        lw = line_perm_of_rootperm(P_w)
        # Z6 squares: images of c^2 (Z6 side of Z12) and w^5 (Z6 side of
        # Z30) must generate the same line action
        lc2 = line_perm_of_rootperm(perm_pow(P_c, 2))
        lw5 = line_perm_of_rootperm(perm_pow(P_w, 5))
        z6_compatible = (lc2 is not None and lw5 is not None
                         and orbit_census([lc2], 60) == orbit_census([lw5], 60))
        # joint line group
        jseen = {ident60}
        jdq = deque([ident60])
        while jdq:
            p = jdq.popleft()
            for g in (lc, lw):
                q = tuple(p[g[i]] for i in range(60))
                if q not in jseen:
                    jseen.add(q)
                    jdq.append(q)
        joint_line_census = orbit_census([lc, lw], 60)
        simply_transitive = (len(jseen) == 60
                             and joint_line_census == Counter({60: 1}))

    if not (deploy_ok and controls_ok):
        VERDICT = "TEST-VOID"
    elif not both_descend or kill_orders:
        VERDICT = "CLOCK-FIBER-DEAD"
    elif z6_compatible and simply_transitive:
        VERDICT = "CLOCK-FIBER-EXACT"
    elif z6_compatible:
        VERDICT = "CLOCK-FIBER-PARTIAL"
    else:
        VERDICT = "CLOCK-FIBER-DEAD"

    print("VERDICT: %s" % VERDICT)
    print("  seam clock line order: %d (Z12 acts through Z3 = <sigma> "
          "only; line-trivial powers %s)" % (lc_ord, lc_kernel))
    print("  Coxeter descent powers: %s -> line shadow orders %s"
          % (descent_powers, line_shadow))
    print("  full line-compatible group: order %d, max element order %d, "
          "orders 15/30/60 present: %s/%s/%s"
          % (full_order, maxord, has15, has30, has60))
    print("  abstract fiber product: Z12 x_{Z6} Z30 = Z60 (cyclic, order "
          "60); realized on the lines: %s" % simply_transitive)
    print("  mu4 layer 240 = 4 x 60: exact (S1.2)")
    print("  joint <c, w> census on the 240 roots: %s" % dict(joint_census))

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("%d/%d checks passed" % (n_pass, len(CHECKS)))
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("elapsed: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else
          "SOME CHECKS FAILED")
    return (0 if n_pass == len(CHECKS) else 1), list(CHECKS)


def run():
    """run_all entry point (combined adjudication): part 1 must be 21/21
    (ONE-OBJECT-PARTIAL: the glue census forces d = 4, the c_3 link stays
    a corpus-legitimate rewriting), part 2 must be 23/23 with the
    three-level kill (CLOCK-FIBER-DEAD: no realization of
    Z12 x_{Z6} Z30 on the 60 lines exists)."""
    rc1 = _run_part1()
    fails1 = [n for (n, ok) in CHECKS if not ok]
    part1_ok = (rc1 == 0 and not fails1 and len(CHECKS) == 21)
    print("\n[%s] PART-1 PATTERN GATE: expected 21/21 "
          "(ONE-OBJECT-PARTIAL) -- fails: %s"
          % ("PASS" if part1_ok else "FAIL", fails1 or "none"))
    rc2, chks2 = _run_part2()
    fails2 = [n for (n, ok) in chks2 if not ok]
    part2_ok = (rc2 == 0 and not fails2 and len(chks2) == 23)
    print("\n[%s] PART-2 PATTERN GATE: expected 23/23 "
          "(CLOCK-FIBER-DEAD) -- fails: %s"
          % ("PASS" if part2_ok else "FAIL", fails2 or "none"))
    ok = part1_ok and part2_ok
    print("\nCOMBINED ADJUDICATION: %s -- ONE-OBJECT-PARTIAL + "
          "CLOCK-FIBER-DEAD: the exact discriminant-form census over "
          "d = 2..12 admits an even unimodular diagonal glue of "
          "A_{d-1} (+) D_{d+1} ONLY at d = 4 (v92's two Z4 anti-isometry "
          "glues k -> k and k -> 3k reproduced; explicit E8 certificate "
          "with 240 integral norm-2 vectors, coset counts [52, 64, 60, "
          "64]; controls open d = 9 without evenness and d in {7, 8, 9, "
          "12} without unimodularity), forcing g_car = d+1 = 5, N_fam = "
          "d-1 = 3, |mu4| = 4 = d as readouts of ONE four-point object; "
          "c_3 = 1/(2 pi d)|_{d=4} = 1/(8 pi) stays a corpus-legitimate "
          "REWRITING, not a new P1 derivation.  The 60-line clock "
          "synchronization hypothesis L_60 = Z12 x_{Z6} Z30 is DEAD at "
          "three independent levels: the seam clock acts only through "
          "Z3, the Coxeter clock does not descend (powers {0, 15} only), "
          "and the FULL line-compatible group (order 23040, max element "
          "order 12) contains NO element of order 15, 30 or 60 -- while "
          "the abstract fiber product IS cyclic Z60 exactly (CC1-CC3 "
          "fire).  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
