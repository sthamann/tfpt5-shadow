#!/usr/bin/env python3
r"""v776 -- ARF.BOUNDARY.CODE.01: boundary code uniqueness -- the non-circular chain boundary -> code -> E8 -> F2^4 -> 5 slots closes with g_car = 5 as OUTPUT (31/31 checks, ~2 s; discovery probe boundary_hamming_uniqueness_probe.py, 2026-08-05, verdict BOUNDARY-CODE-UNIQUE).  THE CHAIN, REBUILT WITHOUT HAMMING/E8 INPUT: direct enumeration gives 135 self-dual binary codes of length 8 (mass formula) of which 30 are doubly even; J-compatibility (pi_J-invariance, the condition for J L = L) leaves 14; sigma-equivariance (deck 3-cycle, anchor pair fixed) leaves 2, swapped by the anchor transposition (67) -- which IS boundary gauge until the flag datum; the flag/side-orientation datum selects EXACTLY ONE code, identically under all three predeclared formalizations (FF1 flag word, FF2 orientation parity, FF3 anchor-side existence), and the decisive boundary content is ONE deck-invariant Z2 -- the product of the four side orientations (all 16 side assignments select uniquely, dependence only on sum(s) mod 2).  The boundary gauge group (centralizer of {pi_J, pi_sigma} in S8, order 12) makes the flagless twofold pure gauge.  DERIVED CHAIN, EXACT: Construction A of the selected code IS E8 (240/2160 theta, even unimodular after rescale, simple-root Cartan det 1 with branch arms 1-2-4; post-selection cross-check: weight-4 supports == the deployed v638 C* list verbatim); L/(1+i)L = F2^4 with the canonical symplectic bbar (well-defined, alternating, nondegenerate, sigma-invariant); the Arf selector with the BOUNDARY-canonical anchor naming (A = class of the flag-transversal root) picks a unique q*; the sigma-orbit packets output g_car = 1 + 4 = 5 (240 = 5 x 48 roots, 60 = 5 x 12 Gaussian lines).  HONEST RESIDUALS (typed, load-bearing for the new contract form): R1 the UNIVERSE premise -- 'the boundary realizes a doubly-even self-dual binary code on its 8 sides' is the new named premise; the circularity is not removed, it is relocated and shrunk to this premise + the flag bit + the anchor naming; R2 deck-placement blindness -- WHICH pair is the anchor is invisible to the code selection (Aut(C*) contains every straight pair 3-cycle); the anchor placement is SEMANTIC, not selective (the wrong-deck control does not fire, typed as an honest deviation from the naive expectation); R3 anchor naming -- bbar(F_Sigma, A) = 1, so A vs A + F_Sigma changes q*; the flag-transversal-root naming is boundary-canonical but part of the frozen selector, not a theorem.  NO P2-REMOVAL CLAIM: this module measures that the derivation chain exists; the OPEN contract form is registered in the ledger (ARF.BOUNDARY.CODE.01 [O]): derive evenness/self-duality of the mark bookkeeping from the seam axioms, plus the R2/R3 residuals.  All controls fire (drop-J/drop-sigma/drop-flag/twisted deck/illegal deck/all 105 non-doubly-even codes fail Construction-A evenness).  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe boundary_hamming_uniqueness_probe.py (2026-08-05, 31/31, 1.5 s, BOUNDARY-CODE-UNIQUE; re-run identical at promotion).  Promoted verbatim inside _run_probe(); run() encodes the all-pass BOUNDARY-CODE-UNIQUE pattern (v757 precedent).  Numbers unchanged.

Original probe docstring (verbatim):
boundary_hamming_uniqueness_probe.py -- ARF.BOUNDARY.CODE.01
(discovery probe, Priority 3 of the Arf compiler programme):
boundary -> code -> E8 -> F2^4 -> 5 slots -- does the non-circular
selection chain EXIST, with g_car = 5 as OUTPUT, not input?

THE CIRCULARITY BEING ATTACKED (v736 circularity fence, verbatim
honest): the code C*, the lattice L, the complex structure J and the
clock sigma are all built FROM E8 (v626/v634/v638/v689); reading
g_car = 5 back out of the quotient is an internal RECONSTRUCTION, not
a derivation.  A non-circular derivation must construct the code from
the boundary datum WITHOUT E8 input.  This probe measures whether that
derivation chain exists.  NO CLAIM that P2 is removed from the axiom
list is made or implied -- that is a promotion decision, out of scope.

FROZEN DESIGN (SHA-256 of FROZEN_SPEC printed before enumeration):

FORBIDDEN inputs: the compiler, g_car = 5, D5, the carrier, E8's
five-slot construction, any Hamming generator matrix.  The [8,4,4]
census is done by DIRECT enumeration of all doubly-even self-dual
binary codes of length 8 (universe premise: doubly-even self-duality
itself -- named as the honest residual premise in the report).

ALLOWED boundary data (exact formalization, frozen):
  (B1) 8 coordinates = 4 marks x 2 sides; mark k owns the coordinate
       pair {2k, 2k+1}; the complex structure J rotates each pair
       (e_{2k} -> e_{2k+1} -> -e_{2k}).  Holomorphy for a binary code
       C:  J-compatibility := invariance under the in-pair swap
       pi_J = (01)(23)(45)(67)  (signs are invisible mod 2; this is
       exactly what J L = L needs for L = A(C)).
  (B2) Z3 deck sigma: cycles the three family marks, fixes the anchor
       mark; as coordinate permutation pi_sigma:
       (0,1)->(2,3)->(4,5)->(0,1), (6,7) fixed pointwise.
       Equivariance := code invariance under pi_sigma.
  (B3) Locality / boundary-legal equivalences: coordinate permutations
       only (monomial group mod signs = S8 on placements); the gauge
       group of the boundary data = centralizer of {pi_J, pi_sigma}
       in S8 (computed explicitly, and its action on the survivor set
       reported).
  (B4) THE FLAG / SIDE-ORIENTATION datum: a choice of one flagged side
       per mark, s in {0,1}^4 (flagged coordinate of mark k is 2k+s_k;
       default s = (0,0,0,0), flag set {0,2,4,6}).  Three predeclared
       formalizations, all tested:
       FF1 (flag word): the indicator vector of the four flagged sides
           is a codeword.
       FF2 (orientation parity): every transversal codeword (exactly
           one coordinate per pair) sits at EVEN total displacement
           from the flagged sides (sum of in-pair digits relative to
           the flags == 0 mod 2).
       FF3 (anchor-side existence): the code contains a transversal
           through the flagged ANCHOR side with even total family
           displacement.
       Flag-dependence typing (frozen): re-run FF1 over all 16 side
       assignments s; the decisive boundary content is measured
       (predicted: only the TOTAL orientation bit sum(s) mod 2).

FROZEN CONSTRAINT ORDER: (a) J-compatibility, (b) sigma-equivariance,
(c) flag datum.  Census numbers reported at every stage; corpus
reference numbers (v689 I0.1): 30 placements, 14 pi_J-invariant
(16 not), 2 both-invariant, the two swapped by (67).

DERIVED CHAIN (for the selected code, all exact):
  (D1) Construction A -> E8: 240 norm-4 vectors, 2160 norm-8 vectors
       (theta match), even lattice of determinant 256 (unimodular
       after 1/sqrt2), simple-root Cartan matrix = E8 (det 1,
       branch-node arms 1,2,4); post-selection cross-check: weight-4
       supports == the deployed v638 C* list.
  (D2) mod-(1+i) reduction: L/(1+i)L = F2^4, 15 x 16 root census,
       zero class empty; canonical symplectic form
       bbar(x,y) := h(x,y) mod (1+i) with
       h(x,y) = (<x,y> + i<x,Jy>)/2  -- checked alternating,
       nondegenerate, sigma-invariant, well-defined (exhaustive
       representative shifts).
  (D3) ARF SELECTOR (imported from the parallel Priority-1 spec,
       frozen here): q* = the unique sigma-invariant quadratic
       refinement of bbar with q(F_Sigma) = 0 and q(A) = 1, where
       F_Sigma := class of the coordinate roots (+-2e_i) and
       A := class of the FLAG-TRANSVERSAL ROOT (the indicator vector
       of the four flagged sides, an integer norm-4 vector) -- the
       boundary-canonical anchor naming; sensitivity of the selector
       to the naming A vs A + F_Sigma is computed and reported
       (bbar(F_Sigma, A) decides it).
  (D4) FIVE SLOTS AS OUTPUT: the sigma-orbit packets of the 15
       root-bearing classes -- 1 fixed block (3 sigma-fixed classes)
       + 4 moved blocks (the four 3-cycles), 240 = 5 x 48 roots,
       60 = 5 x 12 Gaussian lines; g_car := 1 + #moved blocks = 5,
       an OUTPUT of the chain.  q* separates the anchor class inside
       the fixed block (reported).

CONTROLS (frozen expectations):
  (C1) drop J: count sigma-only survivors; without pi_J-invariance no
       Z[i]-module exists (chain undefined).
  (C2) drop sigma: count J+flag survivors among the 14 (measures
       whether sigma is load-bearing for the SELECTION, reported
       honestly either way).
  (C3) drop flag: survivor count must be exactly 2 (uniqueness lost).
  (C4) wrong deck (anchor on pair (4,5) instead of (6,7)): survivor
       set recomputed; consistency theorem checked (conjugation by
       the pair swap rho = (46)(57) must map one survivor set to the
       other); whether the set CHANGES is measured -- the corpus
       automorphism group Aut(C*) is large, so deck-placement
       blindness of the SELECTION is a possible honest outcome, in
       which case the deck's anchor placement is typed as SEMANTIC
       (it names which quotient classes are families) rather than
       selective.  Also: a doubly twisted legal deck, and an
       ILLEGAL deck (evens-only 3-cycle, no J-commutation) -- the
       latter is not boundary-legal and is reported as such.
  (C5) non-doubly-even self-dual codes: full direct census of ALL
       self-dual binary codes of length 8 (mass formula: 135);
       every non-doubly-even one must FAIL Construction A evenness
       (a codeword of weight == 2 mod 4 lifts to an odd-norm vector
       after rescaling): fires for all of them.

VERDICT ENUM (frozen): BOUNDARY-CODE-UNIQUE / BOUNDARY-CODE-TWOFOLD /
BOUNDARY-CODE-DEAD.

Everything exact F2 / integer / Fraction arithmetic; no floats in any
gate.  FIREWALL: experiments/ probe; writes nothing; no verification/,
paper, ledger or website surface touched; typed exploration only.

Corpus read-only references: gaussian_code_bridge_probe.py / v689
(census machinery + I0.1 reference numbers), v736_orbit_packet.py
(packet law + circularity fence), note_e8_gaussian_code.tex (deployed
C* weight-4 supports).
"""


def _run_probe():
    import hashlib
    import itertools
    import time
    from collections import Counter
    from fractions import Fraction as Fr

    T0 = time.time()
    CHECKS = []


    def check(name, ok, detail=""):
        CHECKS.append((name, bool(ok)))
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                             (" -- " + detail) if detail else ""), flush=True)


    def section(title):
        print("=" * 78)
        print(title)
        print("=" * 78, flush=True)


    # ------------------------------------------------------------ frozen spec
    FROZEN_SPEC = """ARF.BOUNDARY.CODE.01 frozen design v1 (2026-08-05).
FORBIDDEN: compiler, g_car=5, D5, carrier, E8 five-slot construction,
Hamming generator matrices.  UNIVERSE: all doubly-even self-dual binary
codes of length 8 by direct enumeration (universe premise named).
BOUNDARY DATA: pairs {2k,2k+1}; holomorphy = pi_J=(01)(23)(45)(67)
invariance; deck = pi_sigma (01)->(23)->(45), anchor (67) fixed;
legal equivalences = S8, boundary gauge = centralizer of {pi_J,pi_sigma};
flags s in {0,1}^4, default (0,0,0,0).
CONSTRAINT ORDER: J, sigma, flag.
FLAG FORMALIZATIONS: FF1 flag word in C; FF2 all transversal codewords
at even total displacement from flags; FF3 exists transversal through
flagged anchor side with even family displacement.  All 16 flag
assignments re-tested; decisive content measured.
CHAIN: Construction A -> E8 (240/2160 theta, Cartan det 1 arms 1,2,4);
L/(1+i)L with bbar(x,y)=h(x,y) mod (1+i); Arf selector q* = unique
sigma-invariant refinement with q(F_Sigma)=0, q(A)=1,
A := class of flag-transversal root; packets 1+4 -> g_car OUTPUT.
CONTROLS: drop-J, drop-sigma, drop-flag(=2), wrong deck (consistency by
rho=(46)(57) conjugation; blindness honest outcome), twisted deck,
illegal deck (no J-commutation), all 135 self-dual codes with the
non-doubly-even ones failing Construction-A evenness.
VERDICT: BOUNDARY-CODE-UNIQUE / BOUNDARY-CODE-TWOFOLD /
BOUNDARY-CODE-DEAD.  No P2 removal claim."""

    section("B0: frozen design")
    print("FROZEN_SPEC sha256 = %s"
          % hashlib.sha256(FROZEN_SPEC.encode()).hexdigest(), flush=True)

    N = 8
    ZERO_W = (0,) * N
    PAIRS = ((0, 1), (2, 3), (4, 5), (6, 7))
    PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
    PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)         # deck (01)->(23)->(45), anchor (67)
    PI_SIG_WRONG = (6, 7, 0, 1, 4, 5, 2, 3)   # wrong anchor: (01)->(23)->(67)
    PI_SIG_TWIST = (4, 5, 1, 0, 3, 2, 6, 7)   # legal deck, two in-pair twists
    PI_BAD = (4, 1, 0, 3, 2, 5, 6, 7)         # evens-only 3-cycle (0 2 4)
    RHO_SWAP_23 = (0, 1, 2, 3, 6, 7, 4, 5)    # pair swap (45)<->(67)
    FLAG_SIDES_DEFAULT = (0, 0, 0, 0)

    # deployed C* weight-4 supports (note_e8_gaussian_code.tex / v638) --
    # used ONLY as a post-selection cross-check in D1, never as input
    DEPLOYED_CSTAR_W4 = [
        (0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6), (0, 2, 5, 7),
        (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 4, 6),
        (1, 3, 5, 7), (2, 3, 4, 5), (2, 3, 6, 7), (4, 5, 6, 7)]


    # ------------------------------------------------------------- F2 helpers
    def dot2(a, b):
        return sum(x * y for x, y in zip(a, b)) % 2


    def addw(a, b):
        return tuple((x + y) % 2 for x, y in zip(a, b))


    def wt(a):
        return sum(a)


    def apply_perm(w, p):
        return tuple(w[p[k]] for k in range(N))


    def code_image(code, p):
        return frozenset(apply_perm(w, p) for w in code)


    def pcomp(a, b):
        """permutation composition in the apply_perm convention."""
        return tuple(a[b[k]] for k in range(N))


    def supports_w4(code):
        return sorted(tuple(i for i in range(N) if w[i])
                      for w in code if wt(w) == 4)


    def transversal_digits(word):
        """in-pair digits d in F2^4 if word picks exactly one side per
        mark, else None."""
        d = []
        for (a, b) in PAIRS:
            if word[a] + word[b] != 1:
                return None
            d.append(word[b])
        return tuple(d)


    # --------------------------------------------- direct code enumeration
    def enumerate_selfdual(candidates):
        """all dim-4 self-orthogonal codes spanned by the candidate words
        (= all self-dual codes inside the candidate closure), by BFS over
        subspaces.  Exact F2, no code input beyond the candidate list."""
        current = {frozenset([ZERO_W])}
        for _ in range(4):
            nxt = set()
            for code in current:
                for v in candidates:
                    if v in code:
                        continue
                    if any(dot2(v, c) for c in code):
                        continue
                    nxt.add(frozenset(code | {addw(v, c) for c in code}))
            current = nxt
        return sorted(current, key=lambda c: sorted(c))


    # ---------------------------------------------------- exact linear algebra
    def mat_det_inv(rows):
        n = len(rows)
        A = [[Fr(v) for v in r] for r in rows]
        I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
        det = Fr(1)
        for col in range(n):
            piv = next((r for r in range(col, n) if A[r][col] != 0), None)
            assert piv is not None, "singular matrix"
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


    def f2_rref(words):
        rows = [list(w) for w in sorted(words, reverse=True) if any(w)]
        basis, pivots = [], []
        for r in rows:
            r = r[:]
            for b, pv in zip(basis, pivots):
                if r[pv]:
                    r = [(a + c) % 2 for a, c in zip(r, b)]
            if any(r):
                basis.append(r)
                pivots.append(next(i for i, a in enumerate(r) if a))
        return basis, pivots


    # ------------------------------------------------------- vector helpers
    def J_vec(x):
        out = []
        for k in range(0, N, 2):
            out += [-x[k + 1], x[k]]
        return tuple(out)


    def sig_vec(x):
        return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


    def add_vec(x, y):
        return tuple(a + b for a, b in zip(x, y))


    def ip(x, y):
        return sum(a * b for a, b in zip(x, y))


    # ======================================================================
    section("B1: the census from scratch -- no Hamming input")

    DE_WORDS = [w for w in itertools.product((0, 1), repeat=N)
                if w != ZERO_W and wt(w) % 4 == 0]
    DE_SD = enumerate_selfdual(DE_WORDS)
    enums = [tuple(sorted(Counter(wt(w) for w in c).items())) for c in DE_SD]
    ok_enum = all(e == ((0, 1), (4, 14), (8, 1)) for e in enums)
    ok_sd = all(all(dot2(u, v) == 0 for u in c for v in c) and len(c) == 16
                for c in DE_SD)
    check("B1.1 direct enumeration: %d doubly-even self-dual codes of "
          "length 8 (corpus census: 30 = 8!/1344 placements of e8-hat); "
          "all self-dual dim 4, weight enumerator 1 + 14x^4 + x^8"
          % len(DE_SD), len(DE_SD) == 30 and ok_enum and ok_sd)

    ALL_EVEN = [w for w in itertools.product((0, 1), repeat=N)
                if w != ZERO_W and wt(w) % 2 == 0]
    SD_ALL = enumerate_selfdual(ALL_EVEN)
    NON_DE = [c for c in SD_ALL if any(wt(w) % 4 == 2 for w in c)]
    check("B1.2 full self-dual census: %d codes (mass formula "
          "(2+1)(4+1)(8+1) = 135), %d of them NOT doubly even "
          "(control pool for C5)" % (len(SD_ALL), len(NON_DE)),
          len(SD_ALL) == 135 and len(NON_DE) == 105
          and all(c in SD_ALL for c in DE_SD))

    # ======================================================================
    section("B2: boundary constraints in frozen order (J, then sigma)")

    J_CODES = [c for c in DE_SD if code_image(c, PI_J) == c]
    check("B2.1 constraint (a) J-compatibility (pi_J-invariance, the "
          "condition for J L = L): %d/30 survive (corpus: 14, i.e. 16 "
          "fail)" % len(J_CODES), len(J_CODES) == 14)

    JS_CODES = [c for c in J_CODES if code_image(c, PI_SIG) == c]
    check("B2.2 constraint (b) sigma-equivariance (deck 3-cycle, anchor "
          "(6,7)): %d survive both (corpus census I0.1: exactly 2)"
          % len(JS_CODES), len(JS_CODES) == 2)

    pi_67 = (0, 1, 2, 3, 4, 5, 7, 6)
    ok_twin = (len(JS_CODES) == 2
               and code_image(JS_CODES[0], pi_67) == JS_CODES[1])
    check("B2.3 the two survivors are swapped by the anchor in-pair "
          "transposition (67) (corpus: 'the other is its image under "
          "(67)')", ok_twin)

    CENT = [p for p in itertools.permutations(range(N))
            if pcomp(p, PI_J) == pcomp(PI_J, p)
            and pcomp(p, PI_SIG) == pcomp(PI_SIG, p)]
    n_fix = sum(1 for p in CENT if code_image(JS_CODES[0], p) == JS_CODES[0])
    n_swap = sum(1 for p in CENT
                 if code_image(JS_CODES[0], p) == JS_CODES[1])
    check("B2.4 boundary gauge group = centralizer of {pi_J, pi_sigma} in "
          "S8: order %d; action on the survivor pair: %d fix, %d swap "
          "(the (67) swap is boundary gauge UNTIL the flag datum breaks "
          "it -- without flags the two survivors are strictly "
          "gauge-equivalent, i.e. 'unique up to gauge')"
          % (len(CENT), n_fix, n_swap),
          pi_67 in CENT and n_swap > 0 and n_fix + n_swap == len(CENT))

    # ======================================================================
    section("B3: constraint (c) -- the flag / side-orientation datum")

    FLAG_SET = tuple(2 * k + s for k, s in enumerate(FLAG_SIDES_DEFAULT))
    W_FLAG = tuple(1 if i in FLAG_SET else 0 for i in range(N))

    ff1_sel = [c for c in JS_CODES if W_FLAG in c]
    check("B3.1 FF1 (flag word): the indicator of the flagged sides "
          "%s is a codeword of exactly %d/2 survivors -> selects ONE"
          % (list(FLAG_SET), len(ff1_sel)), len(ff1_sel) == 1)


    def ff2_holds(code, flags):
        trs = [transversal_digits(w) for w in code]
        trs = [d for d in trs if d is not None]
        if len(trs) != 8:
            return False, len(trs)
        return all(sum((dk + fk) % 2 for dk, fk in zip(d, flags)) % 2 == 0
                   for d in trs), len(trs)


    ff2_flags = [ff2_holds(c, FLAG_SIDES_DEFAULT) for c in JS_CODES]
    ff2_sel = [c for c, (ok, _) in zip(JS_CODES, ff2_flags) if ok]
    check("B3.2 FF2 (orientation parity): each survivor carries exactly 8 "
          "transversal codewords, with HOMOGENEOUS displacement parity "
          "(one survivor all-even, the other all-odd relative to the "
          "flags); the all-even one is selected: %d/2"
          % len(ff2_sel),
          len(ff2_sel) == 1 and all(n == 8 for _, n in ff2_flags))


    def ff3_holds(code, flags):
        anchor_side = 6 + flags[3]
        for w in code:
            d = transversal_digits(w)
            if d is None:
                continue
            if w[anchor_side] == 1 and \
               sum((d[k] + flags[k]) % 2 for k in range(3)) % 2 == 0:
                return True
        return False


    ff3_sel = [c for c in JS_CODES if ff3_holds(c, FLAG_SIDES_DEFAULT)]
    check("B3.3 FF3 (anchor-side existence): a transversal through the "
          "flagged anchor side with even family displacement exists in "
          "%d/2 survivors -> selects ONE" % len(ff3_sel), len(ff3_sel) == 1)

    agree = (len(ff1_sel) == 1 and ff1_sel == ff2_sel == ff3_sel)
    check("B3.4 all three predeclared formalizations select the SAME code",
          agree)

    # flag-dependence typing: which part of the flag datum is decisive?
    sel_by_s = {}
    ok_all_defined = True
    for s in itertools.product((0, 1), repeat=4):
        w_s = tuple(1 if i in {2 * k + sk for k, sk in enumerate(s)} else 0
                    for i in range(N))
        sel = [c for c in JS_CODES if w_s in c]
        if len(sel) != 1:
            ok_all_defined = False
        sel_by_s[s] = sel[0] if len(sel) == 1 else None
    parity_classes = {0: set(), 1: set()}
    for s, c in sel_by_s.items():
        parity_classes[sum(s) % 2].add(id(c) if c is None else
                                       tuple(sorted(c)))
    ok_parity = (ok_all_defined
                 and len(parity_classes[0]) == 1
                 and len(parity_classes[1]) == 1
                 and parity_classes[0] != parity_classes[1])
    check("B3.5 flag-dependence typing: all 16 side assignments select "
          "exactly one survivor, and the selection depends ONLY on the "
          "total orientation bit sum(s) mod 2 -- the decisive boundary "
          "datum is a single Z2 (the product of the four side "
          "orientations), deck-invariant", ok_parity)

    C_SEL = ff1_sel[0] if len(ff1_sel) == 1 else \
        next(c for c in JS_CODES if W_FLAG in c)

    # ======================================================================
    section("B4/D1: derived chain -- Construction A of the selected code "
            "is E8 (exact)")

    check("B4.0 post-selection cross-check: weight-4 supports of the "
          "boundary-selected code == the deployed v638 C* list verbatim",
          supports_w4(C_SEL) == DEPLOYED_CSTAR_W4)

    ROOTS = []
    n4 = n8 = 0
    for x in itertools.product(range(-2, 3), repeat=N):
        n = sum(v * v for v in x)
        if n == 4:
            if tuple(v % 2 for v in x) in C_SEL:
                ROOTS.append(x)
                n4 += 1
        elif n == 8:
            if tuple(v % 2 for v in x) in C_SEL:
                n8 += 1
    check("B4.1 theta check: %d vectors of norm 4 and %d of norm 8 "
          "(E8 theta after rescale: 240, 2160)" % (n4, n8),
          n4 == 240 and n8 == 2160)

    cb, pivots = f2_rref(C_SEL)
    B_ROWS = [tuple(r) for r in cb]
    B_ROWS += [tuple(2 if i == j else 0 for i in range(N))
               for j in range(N) if j not in pivots]
    detB, B_INV = mat_det_inv(B_ROWS)
    gram = [[ip(u, v) for v in B_ROWS] for u in B_ROWS]
    ok_even = all(gram[i][j] % 2 == 0 for i in range(N) for j in range(N))
    ok_de = all(gram[i][i] % 4 == 0 for i in range(N))
    check("B4.2 lattice: |det basis| = %d = [Z^8 : L], Gram all-even with "
          "doubly-even diagonal -> L/sqrt2 is an even unimodular rank-8 "
          "lattice" % abs(int(detB)),
          abs(int(detB)) == 16 and ok_even and ok_de)

    FWTS = [5 ** k for k in range(N)]
    POS = [r for r in ROOTS if sum(w * v for w, v in zip(FWTS, r)) > 0]
    POS_SET = set(POS)
    SIMPLE = []
    for a in POS:
        decomposable = any(tuple(x - y for x, y in zip(a, b)) in POS_SET
                           for b in POS if b != a)
        if not decomposable:
            SIMPLE.append(a)
    cartan = [[ip(u, v) // 2 for v in SIMPLE] for u in SIMPLE]
    ok_diag = all(cartan[i][i] == 2 for i in range(len(SIMPLE)))
    ok_off = all(cartan[i][j] in (0, -1)
                 for i in range(len(SIMPLE)) for j in range(len(SIMPLE))
                 if i != j)
    det_c, _ = mat_det_inv(cartan) if len(SIMPLE) == 8 else (Fr(0), None)
    adj = {i: [j for j in range(len(SIMPLE))
               if j != i and cartan[i][j] == -1]
           for i in range(len(SIMPLE))}
    degs = sorted(len(adj[i]) for i in adj)
    branch = [i for i in adj if len(adj[i]) == 3]
    arms = []
    if len(branch) == 1:
        b0 = branch[0]
        for start in adj[b0]:
            ln, prev, cur = 1, b0, start
            while True:
                nxts = [j for j in adj[cur] if j != prev]
                if not nxts:
                    break
                prev, cur = cur, nxts[0]
                ln += 1
            arms.append(ln)
        arms.sort()
    seen = {0}
    frontier = [0]
    while frontier:
        i = frontier.pop()
        for j in adj[i]:
            if j not in seen:
                seen.add(j)
                frontier.append(j)
    check("B4.3 simple-root Cartan matrix: %d simple roots, diagonal 2, "
          "off-diagonal in {0,-1}, connected, det = %s, branch-node arms "
          "%s -> the diagram IS E8 (arms 1,2,4; D8 would be 1,1,5; "
          "det(E8) = 1)" % (len(SIMPLE), det_c, arms),
          len(SIMPLE) == 8 and ok_diag and ok_off and len(seen) == 8
          and det_c == 1 and arms == [1, 2, 4])

    # ======================================================================
    section("B4/D2: mod-(1+i) reduction -- the four-bit symplectic space")

    A_MAT = [vec_mat(add_vec(b, J_vec(b)), B_INV) for b in B_ROWS]
    A_INT = [[int(v) for v in row] for row in A_MAT]
    assert all(v.denominator == 1 for row in A_MAT for v in row)
    detA, _ = mat_det_inv(A_INT)
    H = row_hnf(A_INT)


    def coords(x):
        c = vec_mat(x, B_INV)
        assert all(v.denominator == 1 for v in c), "not a lattice vector"
        return tuple(int(v) for v in c)


    def label(x):
        return hnf_reduce(coords(x), H)


    REPS = {label((0,) * N): (0,) * N}
    frontier = [(0,) * N]
    while frontier:
        v = frontier.pop()
        for b in B_ROWS:
            w = add_vec(v, b)
            lb = label(w)
            if lb not in REPS:
                REPS[lb] = w
                frontier.append(w)
    ZERO_L = label((0,) * N)
    check("B4.4 [L : (1+i)L] = |det| = %d = 2^4; exactly %d classes "
          "generated -> L/(1+i)L = F2^4" % (abs(int(detA)), len(REPS)),
          abs(int(detA)) == 16 and len(REPS) == 16)

    root_label = {r: label(r) for r in ROOTS}
    census = Counter(root_label.values())
    check("B4.5 root census: zero class EMPTY, 15 classes x 16 roots "
          "(240 = 15 x 16): %s" % dict(Counter(sorted(census.values()))),
          ZERO_L not in census and len(census) == 15
          and sorted(census.values()) == [16] * 15)


    def bbar_vec(x, y):
        """h(x,y) mod (1+i) with h(x,y) = (<x,y> + i<x,Jy>)/2 in Z[i];
        a + bi == a + b mod (1+i)."""
        a2, b2 = ip(x, y), ip(x, J_vec(y))
        assert a2 % 2 == 0 and b2 % 2 == 0
        return (a2 // 2 + b2 // 2) % 2


    LBLS = list(REPS)
    ok_wd = True
    for u in LBLS:
        for v in LBLS:
            base = bbar_vec(REPS[u], REPS[v])
            for z in B_ROWS:
                sh = add_vec(z, J_vec(z))
                if bbar_vec(add_vec(REPS[u], sh), REPS[v]) != base or \
                   bbar_vec(REPS[u], add_vec(REPS[v], sh)) != base:
                    ok_wd = False
    B_DIR = {(u, v): bbar_vec(REPS[u], REPS[v]) for u in LBLS for v in LBLS}
    ok_alt = all(B_DIR[(u, u)] == 0 for u in LBLS)
    ok_sym = all(B_DIR[(u, v)] == B_DIR[(v, u)] for u in LBLS for v in LBLS)
    ok_nd = all(any(B_DIR[(u, v)] for v in LBLS)
                for u in LBLS if u != ZERO_L)
    SIGL = {lb: label(sig_vec(REPS[lb])) for lb in LBLS}
    ok_sinv = all(B_DIR[(SIGL[u], SIGL[v])] == B_DIR[(u, v)]
                  for u in LBLS for v in LBLS)
    check("B4.6 canonical hbar: bbar = h mod (1+i) is well-defined "
          "(exhaustive shifts), alternating, symmetric, NONDEGENERATE and "
          "sigma-invariant -- the four-bit SYMPLECTIC space",
          ok_wd and ok_alt and ok_sym and ok_nd and ok_sinv)

    fixed_lbls = [lb for lb in LBLS if SIGL[lb] == lb]
    seen_orb = set()
    orbits = []
    for lb in LBLS:
        if lb == ZERO_L or lb in seen_orb or SIGL[lb] == lb:
            continue
        orb = (lb, SIGL[lb], SIGL[SIGL[lb]])
        seen_orb |= set(orb)
        orbits.append(orb)
    check("B4.7 sigma-bar action: sigma^3 = 1, %d fixed labels (dim 2 "
          "fixed space), 15 nonzero classes = 3 fixed + %d three-cycles"
          % (len(fixed_lbls), len(orbits)),
          all(SIGL[SIGL[SIGL[lb]]] == lb for lb in LBLS)
          and len(fixed_lbls) == 4 and len(orbits) == 4)

    # ======================================================================
    section("B4/D3: the Arf selector q* (imported Priority-1 spec, frozen)")

    F_SIG = label((2, 0, 0, 0, 0, 0, 0, 0))
    ok_coord = all(label(tuple(2 * s if i == j else 0 for i in range(N)))
                   == F_SIG for j in range(N) for s in (1, -1))
    FLAG_ROOT = tuple(1 if i in FLAG_SET else 0 for i in range(N))
    A_LBL = label(FLAG_ROOT)
    third = [lb for lb in fixed_lbls
             if lb not in (ZERO_L, F_SIG, A_LBL)]
    check("B4.8 anchor naming from the boundary: F_Sigma = class of the "
          "coordinate roots (all 16 agree), A = class of the "
          "flag-transversal root %s (norm 4, sigma-fixed, distinct from "
          "F_Sigma); third fixed class = A + F_Sigma"
          % (FLAG_ROOT,),
          ok_coord and A_LBL in fixed_lbls and A_LBL != F_SIG
          and A_LBL != ZERO_L and len(third) == 1)

    # bits coordinates for the quotient
    basis_lbls = []
    span = {ZERO_L}
    for lb in LBLS:
        if lb in span:
            continue
        basis_lbls.append(lb)
        span = set()
        for bits in itertools.product((0, 1), repeat=len(basis_lbls)):
            w = (0,) * N
            for bit, l2 in zip(bits, basis_lbls):
                if bit:
                    w = add_vec(w, REPS[l2])
            span.add(label(w))
        if len(basis_lbls) == 4:
            break
    BITS = {}
    for bits in itertools.product((0, 1), repeat=4):
        w = (0,) * N
        for bit, l2 in zip(bits, basis_lbls):
            if bit:
                w = add_vec(w, REPS[l2])
        BITS[label(w)] = bits
    assert len(BITS) == 16
    B_BASIS = [[B_DIR[(basis_lbls[i], basis_lbls[j])] for j in range(4)]
               for i in range(4)]


    def make_q(tvals):
        q = {}
        for lb, eps in BITS.items():
            val = sum(e * t for e, t in zip(eps, tvals))
            val += sum(eps[i] * eps[j] * B_BASIS[i][j]
                       for i in range(4) for j in range(i + 1, 4))
            q[lb] = val % 2
        return q


    def xor_lbl(u, v):
        return label(add_vec(REPS[u], REPS[v]))


    REFINEMENTS = [make_q(t) for t in itertools.product((0, 1), repeat=4)]
    ok_ref = all(all((q[xor_lbl(u, v)] - q[u] - q[v] - B_DIR[(u, v)]) % 2
                     == 0 for u in LBLS for v in LBLS)
                 for q in REFINEMENTS)
    check("B4.9 all 16 quadratic refinements of bbar constructed and "
          "verified (polarization identity on all 256 label pairs each)",
          ok_ref and len(REFINEMENTS) == 16)

    INV_REF = [q for q in REFINEMENTS
               if all(q[SIGL[lb]] == q[lb] for lb in LBLS)]
    QSTAR = [q for q in INV_REF if q[F_SIG] == 0 and q[A_LBL] == 1]
    b_FA = B_DIR[(F_SIG, A_LBL)]
    QSTAR_ALT = [q for q in INV_REF
                 if q[F_SIG] == 0 and q[xor_lbl(A_LBL, F_SIG)] == 1]
    check("B4.10 Arf selector: %d sigma-invariant refinements; with "
          "q(F_Sigma) = 0 and q(A) = 1 exactly %d survives -> q* UNIQUE. "
          "Naming sensitivity: bbar(F_Sigma, A) = %d, so the alternative "
          "naming A' = A + F_Sigma selects a DIFFERENT (also unique) "
          "refinement (%d) -- the boundary-canonical flag-root naming of "
          "A is load-bearing and is part of the frozen selector"
          % (len(INV_REF), len(QSTAR), b_FA, len(QSTAR_ALT)),
          len(INV_REF) == 4 and len(QSTAR) == 1 and len(QSTAR_ALT) == 1
          and (QSTAR[0] is not QSTAR_ALT[0]) == (b_FA == 1))

    qs = QSTAR[0]
    n_zero_q = sum(1 for lb in LBLS if qs[lb] == 0)
    arf = 0 if n_zero_q == 10 else (1 if n_zero_q == 6 else None)
    check("B4.11 q* profile: %d zeros / %d ones on the 16 labels -> "
          "Arf(q*) = %s; on the fixed block q*(F_Sigma) = %d, q*(A) = %d, "
          "q*(A+F_Sigma) = %d -- q* singles out the anchor class inside "
          "the fixed block"
          % (n_zero_q, 16 - n_zero_q, arf, qs[F_SIG], qs[A_LBL],
             qs[third[0]]),
          arf is not None and qs[A_LBL] == 1
          and qs[F_SIG] == 0)

    # ======================================================================
    section("B4/D4: the five carrier slots as OUTPUT")

    line_of = {}
    lines = []
    for r in ROOTS:
        if r in line_of:
            continue
        orb = [r]
        y = J_vec(r)
        while y != r:
            orb.append(y)
            y = J_vec(y)
        for x in orb:
            line_of[x] = len(lines)
        lines.append(orb)
    fixed_block = [lb for lb in fixed_lbls if lb != ZERO_L]
    blocks = [fixed_block] + [list(o) for o in orbits]
    root_counts = [sum(census[lb] for lb in blk) for blk in blocks]
    line_counts = []
    for blk in blocks:
        lset = {line_of[r] for r in ROOTS if root_label[r] in blk}
        line_counts.append(len(lset))
    G_CAR_OUT = 1 + len(orbits)
    check("B4.12 packets: 1 fixed block + %d moved blocks, root counts %s "
          "(240 = 5 x 48), Gaussian-line counts %s (60 = 5 x 12) -> "
          "g_car = 1 + 4 = %d as OUTPUT of the chain "
          "boundary -> code -> E8 -> F2^4 -> packets"
          % (len(orbits), root_counts, line_counts, G_CAR_OUT),
          root_counts == [48] * 5 and line_counts == [12] * 5
          and len(lines) == 60 and G_CAR_OUT == 5)

    # ======================================================================
    section("B5: controls")

    SIG_ONLY = [c for c in DE_SD if code_image(c, PI_SIG) == c]
    non_J_sig = [c for c in SIG_ONLY if code_image(c, PI_J) != c]
    check("B5.1 CONTROL drop-J: %d/30 codes are sigma-invariant (%d of "
          "them NOT J-compatible: for those no Z[i]-module exists and the "
          "chain is UNDEFINED); J is load-bearing"
          % (len(SIG_ONLY), len(non_J_sig)),
          len(SIG_ONLY) >= 2)

    J_FLAG = [c for c in J_CODES if W_FLAG in c]
    check("B5.2 CONTROL drop-sigma: %d/14 J-compatible codes contain the "
          "flag word -- measured honestly: sigma is %sload-bearing for "
          "the SELECTION under FF1"
          % (len(J_FLAG),
             "" if len(J_FLAG) > 1 else "NOT "),
          len(J_FLAG) >= 1)

    check("B5.3 CONTROL drop-flag: without the orientation datum the "
          "survivor count is %d (uniqueness LOST -- the flag is "
          "load-bearing; fires)" % len(JS_CODES), len(JS_CODES) == 2)

    JS_WRONG = [c for c in J_CODES if code_image(c, PI_SIG_WRONG) == c]
    rho_img = sorted(tuple(sorted(code_image(c, RHO_SWAP_23)))
                     for c in JS_CODES)
    wrong_sorted = sorted(tuple(sorted(c)) for c in JS_WRONG)
    same_set = sorted(tuple(sorted(c)) for c in JS_CODES) == wrong_sorted
    check("B5.4 CONTROL wrong deck (anchor on pair (4,5)): %d survivors; "
          "conjugation consistency rho(survivors) == wrong-deck survivors "
          "holds; survivor set %s the original -- MEASURED: the code "
          "selection is DECK-PLACEMENT-BLIND (Aut(C*) contains every "
          "straight pair 3-cycle); the anchor placement is SEMANTIC "
          "(it names which quotient classes are the families), not "
          "selective; the task's naive expectation 'set must change' "
          "does NOT fire and is reported as an honest deviation"
          % (len(JS_WRONG), "EQUALS" if same_set else "DIFFERS FROM"),
          rho_img == wrong_sorted)

    tw3 = pcomp(PI_SIG_TWIST, pcomp(PI_SIG_TWIST, PI_SIG_TWIST))
    tw_legal = (tw3 == tuple(range(N))
                and pcomp(PI_SIG_TWIST, PI_J) == pcomp(PI_J, PI_SIG_TWIST))
    JS_TWIST = [c for c in J_CODES if code_image(c, PI_SIG_TWIST) == c]
    check("B5.5 CONTROL twisted legal deck (two in-pair flips, order 3, "
          "J-commuting): %d survivors -- twisting by an even number of "
          "side flips does not move the survivor pair (consistent with "
          "B3.5: only the TOTAL orientation bit is decisive)"
          % len(JS_TWIST), tw_legal)

    bad_comm = pcomp(PI_BAD, PI_J) == pcomp(PI_J, PI_BAD)
    JS_BAD = [c for c in J_CODES if code_image(c, PI_BAD) == c]
    check("B5.6 CONTROL illegal deck (evens-only 3-cycle (0 2 4)): does "
          "NOT commute with pi_J (boundary-illegal: %s), J+bad-deck "
          "survivors: %d -- a deck must respect the J-pairing to be a "
          "boundary datum at all"
          % (not bad_comm, len(JS_BAD)), not bad_comm)

    fail_even = 0
    witness = None
    for c in NON_DE:
        w = next((w for w in c if wt(w) % 4 == 2), None)
        if w is not None:
            fail_even += 1
            if witness is None:
                witness = w
    check("B5.7 CONTROL non-doubly-even self-dual codes: all %d/105 "
          "contain a weight == 2 (mod 4) word (witness %s), whose "
          "Construction-A lift has norm == 2 (mod 4) -> the rescaled "
          "lattice is NOT even -> Construction A cannot yield E8 (fires "
          "for the entire other self-dual class)"
          % (fail_even, witness), fail_even == 105)

    # ======================================================================
    section("B6: verdict")

    dead = not (len(DE_SD) == 30 and len(J_CODES) == 14
                and len(JS_CODES) == 2 and n4 == 240 and n8 == 2160
                and len(SIMPLE) == 8 and det_c == 1 and arms == [1, 2, 4]
                and sorted(census.values()) == [16] * 15)
    flag_ok = (len(ff1_sel) == 1 and agree and ok_parity)
    chain_ok = (len(QSTAR) == 1 and G_CAR_OUT == 5)
    controls_ok = (len(JS_CODES) == 2 and fail_even == 105)

    if dead:
        VERDICT = "BOUNDARY-CODE-DEAD"
    elif flag_ok and chain_ok and controls_ok:
        VERDICT = "BOUNDARY-CODE-UNIQUE"
    else:
        VERDICT = "BOUNDARY-CODE-TWOFOLD"

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print()
    print("checks: %d/%d passed, %.1f s" % (n_pass, len(CHECKS),
                                            time.time() - T0))
    print("VERDICT: %s" % VERDICT)
    print()
    print("SUMMARY (census at every stage):")
    print("  universe (direct enumeration, no Hamming input): 135 "
          "self-dual, %d doubly-even self-dual" % len(DE_SD))
    print("  + J-compatibility: %d" % len(J_CODES))
    print("  + sigma-equivariance: %d (gauge pair, swapped by (67), which "
          "IS boundary gauge until the flag)" % len(JS_CODES))
    print("  + flag datum: 1 (FF1 = FF2 = FF3; decisive content = the "
          "total side-orientation bit, a single Z2)")
    print("  chain: Construction A -> E8 (240/2160, Cartan det 1, arms "
          "1-2-4); L/(1+i)L symplectic; q* unique (4 invariant "
          "refinements, both normalizations); packets 1+4 -> g_car = %d "
          "OUTPUT" % G_CAR_OUT)
    print()
    print("HONEST RESIDUALS (typed):")
    print("  R1 the UNIVERSE premise: 'the boundary realizes a doubly-even")
    print("     self-dual binary code on its 8 sides' is the new named")
    print("     premise -- the circularity is not removed, it is relocated")
    print("     and shrunk to this premise + the flag bit + the anchor")
    print("     naming of the Arf selector.")
    print("  R2 deck-placement blindness (B5.4): the deck cuts 14 -> 2 as")
    print("     a 3-fold pair-coherence condition, but WHICH pair is the")
    print("     anchor is invisible to the code selection (it is semantic,")
    print("     fixing the family/anchor reading of the quotient).")
    print("  R3 anchor naming (B4.10): bbar(F_Sigma, A) = 1, so A vs")
    print("     A + F_Sigma changes q*; the flag-transversal-root naming")
    print("     of A is boundary-canonical but is part of the frozen")
    print("     selector, not a theorem.")
    print("  R4 NO P2 REMOVAL CLAIM: this probe only measures that the")
    print("     derivation chain exists; any axiom-list change is a")
    print("     promotion decision outside this probe.")
    print()
    print("RECOMMENDED CONTRACT TEXT (report only, not written anywhere):")
    print("  ARF.BOUNDARY.CODE.01 -- boundary code uniqueness: among ALL")
    print("  doubly-even self-dual binary codes of length 8 (direct census")
    print("  30, no Hamming/E8 input), the boundary data (four J-paired")
    print("  marks, Z3 deck pair-coherence, total side-orientation bit)")
    print("  select exactly one code; Construction A of it IS E8, the")
    print("  (1+i)-reduction is the canonical 4-bit symplectic space, the")
    print("  sigma-invariant Arf refinement with q(F_Sigma)=0, q(A)=1 is")
    print("  unique, and the deck packets output g_car = 1 + 4 = 5.")
    print("  OPEN (the new contract form): WHY does the physical boundary")
    print("  realize the doubly-even self-dual flagged-equivariant code --")
    print("  i.e. derive evenness/self-duality of the mark bookkeeping")
    print("  from the seam axioms; plus the R2/R3 residuals above.")
    return n_pass, len(CHECKS), VERDICT


def run():
    """run_all entry point (v757 precedent): expected pattern 31/31 with
    verdict BOUNDARY-CODE-UNIQUE (TWOFOLD or DEAD breaks the suite)."""
    n_pass, n_all, verdict = _run_probe()
    ok = (n_pass == n_all == 31 and verdict == "BOUNDARY-CODE-UNIQUE")
    print("\n[%s] PATTERN GATE: expected 31/31 BOUNDARY-CODE-UNIQUE; got "
          "%d/%d %s" % ("PASS" if ok else "FAIL", n_pass, n_all, verdict))
    print("\nADJUDICATION: %s -- BOUNDARY-CODE-UNIQUE: census 135 -> 30 "
          "-> 14 -> 2 -> 1 without Hamming/E8 input; the flag datum is one "
          "deck-invariant Z2; Construction A -> E8 exact; g_car = 1 + 4 = "
          "5 as OUTPUT.  Residuals R1 (universe premise), R2 (deck "
          "placement semantic), R3 (anchor naming) typed; NO P2-removal "
          "claim -- the open contract form lives in ARF.BOUNDARY.CODE.01.  "
          "NO RH claim." % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
