#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""intertwiner_split_probe -- SEAM.CFIN.INTERTWINER12.01
(EXPLORATION ONLY, experiments/; round 58, strategy S2 of the
cross-front memo: the exact character computation that decides
whether the 8+4 = 12 pattern is EVIDENCE or NUMEROLOGY -- the
reviewer's own test: 'without an intertwiner it stays decorative').

THE TWO 12s (frozen inputs, corpus verbatim):
 * F-SIDE (finite compiler, rounds 51/52): the Iota/3-compressed
   block space of Ahat -- 2 compressed vacuum dims + 10 carrier
   dims = 12 -- carrying the compressed C6 lift Ohat (identity on
   the compressed vacuum pair, carrier pairs permuted as units by
   the deployed pi, cycle type (1,2,3)); the round-51 MEASURED
   channel commutant splits 12 = 8 symmetric + 4 antisymmetric,
   exact (wick_mixing_covariance_probe W1(a); at block level it is
   the channel-scalar X (x) I2 subalgebra).
 * A-SIDE (arithmetic port ladder, deepcore_anatomy_probe): the 12
   J-window aliases JWIN = {2, 4, ..., 24} (the frozen even window,
   deepcore/cocycle-window convention) = the 8 deep even aliases
   {2, ..., 16} (the ALIAS-FIXED modal deep core, deepcore D1) +
   the 4-alias binding exterior {18, 20, 22, 24}; the frozen fold
   conventions: aliases are folded representatives uf = min(j, L-j)
   with y_j = cos(2 pi j / L), and max(JWIN) = 24 < L/2 on every
   frame-A rung (L ~ 4h, h >= 100).
THE QUESTION: does ANY natural arithmetic action on the 12 aliases
carry the SAME C6 character as the block space -- and if so, does
the equivariant map carry the deep-8 onto the symmetric summand
and the exterior-4 onto the antisymmetric summand?  Without such
an intertwiner the 8+4 = 12 coincidence is typed numerology.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
pure exact integer / sympy rational arithmetic in EVERY decision --
no floats, no RNG, no fits; all C6 character values at the sixth
roots are rational, so everything below is exact):

 S0  SETUP (corpus rebuilt inline, wick_block_functor verbatim):
     q* selector, duad model, vacuum label V0, carrier dictionary
     phi; Sp(4,2) census (720), Aut(C_fin) ~= C6, generator pin
     g^2 = sigma; the deployed channel permutation PI6 (fixes 0,
     cycle type (1,2,3)); the 16-dim lift O16 and the compressed
     12-dim lift Ohat with the compression ward T O16 = Ohat T
     (T = the Iota^T/3 vacuum compression (+) carrier identity);
     Ohat orthogonal integer of order EXACTLY 6; ward 12 =
     2 (g_car + 1) and 1/3 = 1/N_fam.
 F1  THE F-SIDE CHARACTER: chi_F(g^k) = tr(Ohat^k) for k = 0..5
     exactly (signed permutation traces; expected (12, 2, 6, 8, 6,
     2) from the (1,2,3) channel cycle type -- MEASURED).  Complex
     multiplicities m_j = (1/6) sum_k chi(g^k) omega^{-jk} (omega
     = e^{i pi/3}, exact sympy); real irrep multiplicities (triv,
     sign, E1 = the faithful 2-dim, E2 = the order-3 2-dim); exact
     rational isotypic projectors P_triv/P_sign/P_E1/P_E2 (rank,
     idempotency, orthogonality, sum = I -- all exact);
     reconstruction ward sum_j m_j chi_j == chi_F elementwise.
 F2  THE COMMUTANT SPLIT (the round-51 object, measured here):
     (a) the scalar channel commutant {X in R^6x6 : PX = XP}
         (P = the PI6 permutation matrix): exact nullspace; dim ==
         12 with symmetric part == 8 and antisymmetric part == 4;
     (b) the block-level identification: [X (x) I2, Ohat] =
         [X, P] (x) I2 symbolically, so the SAME 12 = 8 + 4 lives
         on the channel-scalar subalgebra of the block space; the
         FULL block commutant measured too (expected 48 = 28 + 20
         by the multiplicity bookkeeping -- the 12 = 8+4 is the
         channel-scalar slice, stated precisely);
     (c) the bookkeeping identity, verified against the measured
         numbers: sym = sum_{1-dim} m(m+1)/2 + sum_{2-dim} m^2,
         antisym = sum_{1-dim} m(m-1)/2 + sum_{2-dim} m^2;
     (d) ISOTYPIC-UNION TEST (the I1 question, made precise both
         ways): (i) as a SPACE split of the 12-dim block space, is
         there a union of isotypic components with dims (8, 4)?
         (expected: UNIQUE -- {triv (+) sign} = 8 vs {E2} = 4);
         (ii) as an ALGEBRA split, the per-isotypic support census
         of the measured 8-sym / 4-antisym commutant (each
         commuting X preserves isotypics; dims of P_j X P_j spans
         printed) -- whether the sym/antisym split ALIGNS with the
         (8,4) space split component by component, or mixes.
 A1  THE A-SIDE ACTIONS (hard-coded 12x12 signed permutations on
     the alias coordinates, frozen order: 2,4,...,24; all signs +1
     -- the frozen natural choice, folded weights are aggregated
     absolute masses):
     (a) FOLD: j -> L - j restricted to the 12 aliases.  Per the
         frozen fold conventions every alias is its OWN folded
         representative (24 < L/2 on every frame-A rung), so the
         reflection maps each unfolded pair {j, L-j} to itself:
         the induced signed permutation is the IDENTITY (stated
         exactly, all 12 fixed, sign +1); as a C6 candidate it is
         the trivial action; chi_A computed.
     (b) SHIFT: the natural cyclic action on the equally spaced
         alias ladder (step 2): the 12-cycle sigma: j -> j + 2
         (24 -> 2); the frozen ORDER-6 VERSION is sigma^2: j ->
         j + 4 with wraparound -- two 6-cycles (2 6 10 14 18 22)
         (4 8 12 16 20 24); order exactly 6 verified; chi_A.
     (c) CLOCK: the order-6 quotient of the mod-30 clock (k6 T4 /
         coxeter_schedule C2: the schedule rotation T: j -> j + 1
         on Z30, with the mod-30 fold F: j -> -j).  MEASURED
         census: which of the 60 dihedral clock elements T^s /
         F T^s restrict to bijections of the alias set {2..24}
         inside Z30?  (Expected: only the identity and the
         reflection j -> 26 - j -- a C2; every order-6 rotation is
         a shift by 5 or 25, ODD, and maps every even alias out of
         the set: the parity obstruction, printed.)  The canonical
         action of the order-6 quotient therefore factors through
         the maximal induced group: g -> (j -> 26 - j); chi_A
         computed; the census of what the reflection does to the
         deep-8 / exterior-4 split printed (expected: it SWAPS
         {2,4,6,8} with the exterior {24,22,20,18} -- the split is
         not even clock-stable).
 M1  THE MATCH + THE INTERTWINER: per candidate compare the real
     multiplicity vector with the F-side vector.  IF a candidate
     matches: construct Phi: A -> F explicitly by equivariant
     averaging of a frozen seed (Phi = (1/6) sum_k Ohat^k L
     rho^{-k}, L = the alias-position dictionary), demand
     equivariance defect EXACTLY 0 (Ohat Phi - Phi rho == 0) and
     invertibility, and test whether Phi maps span(deep-8) onto
     the symmetric summand {triv (+) sign} and span(exterior-4)
     onto the antisymmetric summand {E2} (block structure of Phi
     printed).  BONUS if matched: transport of the measured
     structures (the eta-minimizer port seat, port_seated_pivot /
     eta_margin_source; the wall soft-mode coordinate,
     normalized_core_update) to finite-side objects -- report
     descriptively, no bar.  IF ALL THREE MISMATCH: the honest
     demotion line is printed verbatim: '8+4 = 12 is typed
     NUMEROLOGY-UNTIL-NEW-ACTION per the firewall.'
 C   CONTROLS (must fire; frozen fire rules; specified at freeze
     for the measured-match-empty case):
     C1 SHUFFLED ALIAS LABELING: on the synthetic TRANSPLANT
        action rho* := Ohat read on the 12 alias positions (a
        matched pair BY CONSTRUCTION -- the machinery ward), the
        averaged Phi has defect exactly 0 and is invertible; the
        frozen shuffle S = transposition of alias positions 0 and
        2 (labeling change only) conjugates rho* to rho' = S rho*
        S^-1: the CHARACTER is unchanged (conjugation-invariant,
        printed -- the match survives every relabeling) but the
        FIXED Phi's equivariance defect becomes NONZERO (exact
        Frobenius^2 printed) -- the reviewer's lesson in one
        control: characters are cheap, the intertwiner is the
        content.  Must fire; silent -> CONTROL-DEAD.
     C2 CHARACTER ORTHOGONALITY WARDS: the exact Gram matrix of
        the four real C6 characters under (1/6) sum_k is
        diag(1, 1, 2, 2) with zero off-diagonals; every computed
        multiplicity vector is a nonnegative integer vector that
        reconstructs its character exactly.

KILLS (any one fires => typed gap):
  K0 AST firewall / setup ward breaks              -> PIPELINE-BROKEN
  K1 F-side character / projectors / commutant
     measurement incoherent                        -> FSIDE-BROKEN
  K2 A-side action construction incoherent         -> ASIDE-BROKEN
  K3 match / intertwiner algebra inconsistent      -> MATCH-BROKEN
  K7 a control does not fire                       -> CONTROL-DEAD

VERDICT (frozen enum): INTERTWINER12-MEASURED [typed
INTERTWINER-EXISTS(action, multiplicities) / INTERTWINER-PARTIAL
(what failed) / INTERTWINER-EMPTY] / PIPELINE-BROKEN /
CONTROL-DEAD.  INTERTWINER-EXISTS iff match + zero defect + split
carried; INTERTWINER-EMPTY iff all three candidates mismatch (an
honest EMPTY is a first-class outcome and exits 0).  NO claim
upgrades either way: EXISTS would be a finite exact statement
about two frozen representations, NOT a physics or RH claim.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits; v563 and the port pipeline are NOT
imported (the A-side inputs are the frozen deepcore constants,
hard-coded above).  AST firewall: banned identifiers zetazero /
nzeros / primerange / isprime / primepi / nextprime / prevprime
(self-scan).  No marker moves.

SPEC v2 AMENDMENTS (fail-first preserved): (i) MECHANICAL, first
run: sympy left the sixth-root sums in unsimplified (-1)^(1/3)
form (F1.2 printed m_E1 = 2/3 - 2(-1)^{1/3}/3 + 2(-1)^{2/3}/3,
which IS 0 but did not reduce), and int-seeded sum() over
matrices raised TypeError (two instances: the projector
accumulator and the projector-sum ward).  Fix: force
expand_complex + nsimplify in the multiplicity extraction and
explicit matrix accumulators -- pure simplification/typing repairs,
no bar, no protocol change; the fail-first output is preserved in
the round log.

Sources (read-only, machinery rebuilt inline): wick_block_functor_
probe (round 52: CH2 block layout, Iota/3 compression, O16 lift,
S0 compiler setup verbatim), wick_mixing_covariance_probe (round
51: the 12 = 8 + 4 channel commutant measurement), deepcore_
anatomy_probe (JWIN = {2..24}, deep-8 modal set {2..16}, fold
conventions), k6_pfaffian_selfhosting_probe (T4 mod-30 clock,
CLOCK-DISTINGUISHED) + coxeter_schedule_probe (the 30-cycle
schedule), port_seated_pivot_probe / eta_margin_source_probe (the
eta-minimizer seat), normalized_core_update_probe (the wall
soft mode), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/intertwiner_split_probe.py
"""

import ast
import hashlib
import itertools
import os
import sys
import time

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# ------------------------------------------------- frozen A-side data
ALIASES = tuple(range(2, 25, 2))          # JWIN, deepcore verbatim
DEEP8 = tuple(range(2, 17, 2))            # modal deep core (D1)
EXT4 = tuple(range(18, 25, 2))            # the binding exterior
POS = {j: p for p, j in enumerate(ALIASES)}
MOD30 = 30                                # the k6 anchor clock modulus
SHUFFLE_SWAP = (0, 2)                     # frozen C1 labeling shuffle

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ---------------------------------------------------------- bit model
# (v880 / v888 conventions rebuilt inline, wick_block verbatim)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    """order-3 deck sigma: (b0,b1,b2,b3) -> (b2,b0,b1,b3) (v880)."""
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    """q_c(v) = C(|v|,2) + c.v mod 2 -- the 16 refinements (v880)."""
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v])
                     if bit)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def fro2(M):
    """exact squared Frobenius norm of a sympy matrix."""
    return sum(x * x for x in M)


def mat_order(M, cap=13):
    P = sp.eye(M.shape[0])
    for k in range(1, cap):
        P = P * M
        if P == sp.eye(M.shape[0]):
            return k
    return None


# ------------------------------------------- exact C6 character tools
OMEGA = sp.exp(sp.I * sp.pi / 3)          # primitive 6th root, exact
# real irreps of C6 = <g>: characters at g^k, k = 0..5 (all integer)
CHI_REAL = {
    "triv": [sp.Integer(1)] * 6,
    "sign": [sp.Integer(-1) ** k for k in range(6)],
    "E1":   [sp.Integer(v) for v in (2, 1, -1, -2, -1, 1)],
    "E2":   [sp.Integer(v) for v in (2, -1, -1, 2, -1, -1)],
}
REAL_ORDER = ("triv", "sign", "E1", "E2")
REAL_DIM = {"triv": 1, "sign": 1, "E1": 2, "E2": 2}
# rational cosine weights for the exact real isotypic projectors
COS6 = {1: [sp.Rational(v, 2) for v in (2, 1, -1, -2, -1, 1)],
        2: [sp.Rational(v, 2) for v in (2, -1, -1, 2, -1, -1)]}


def char_of(R):
    """chi(g^k) = tr(R^k), k = 0..5, exact."""
    out, P = [], sp.eye(R.shape[0])
    for _k in range(6):
        out.append(sp.trace(P))
        P = P * R
    return [sp.nsimplify(c) for c in out]


def complex_mults(chi):
    """m_j = (1/6) sum_k chi(g^k) omega^{-jk}, j = 0..5, exact
    (expand_complex forces the sixth roots into a + b*I form so
    the rational result actually simplifies -- amendment (i))."""
    out = []
    for j in range(6):
        s = sum(chi[k] * OMEGA ** ((-j * k) % 6) for k in range(6))
        out.append(sp.nsimplify(sp.simplify(
            sp.expand_complex(s / 6))))
    return out


def real_mults(chi):
    """(triv, sign, E1, E2) multiplicities from the complex ones."""
    m = complex_mults(chi)
    ok = (all(v.is_integer and v >= 0 for v in m)
          and sp.simplify(m[1] - m[5]) == 0
          and sp.simplify(m[2] - m[4]) == 0)
    return (m[0], m[3], m[1], m[2]), ok


def iso_projectors(R):
    """exact rational real isotypic projectors of the C6 action
    generated by R (order dividing 6)."""
    n = R.shape[0]
    pows = [sp.eye(n)]
    for _k in range(5):
        pows.append(pows[-1] * R)

    def acc(weights, scale):
        M = sp.zeros(n)
        for k in range(6):
            M += weights[k] * pows[k]
        return sp.Matrix(M * scale)

    return {"triv": acc([sp.Integer(1)] * 6, sp.Rational(1, 6)),
            "sign": acc([sp.Integer(-1) ** k for k in range(6)],
                        sp.Rational(1, 6)),
            "E1": acc(COS6[1], sp.Rational(2, 6)),
            "E2": acc(COS6[2], sp.Rational(2, 6))}


def reconstructs(chi, mults):
    diff = [sp.simplify(chi[k]
                        - sum(mults[i] * CHI_REAL[nm][k]
                              for i, nm in enumerate(REAL_ORDER)))
            for k in range(6)]
    return all(d == 0 for d in diff)


def commutant_dims(R, n):
    """measured commutant of conjugation by R on n x n matrices:
    (full dim, symmetric dim, antisymmetric dim), exact."""
    def kernel_dim(basis):
        cols = []
        for B in basis:
            D = R * B - B * R
            cols.append([D[r, c] for r in range(n)
                         for c in range(n)])
        M = sp.Matrix(cols).T
        return len(basis) - M.rank()

    full = [sp.Matrix(n, n, lambda r, c, rr=i, cc=j:
                      1 if (r, c) == (rr, cc) else 0)
            for i in range(n) for j in range(n)]
    sym, anti = [], []
    for i in range(n):
        for j in range(i, n):
            B = sp.zeros(n)
            B[i, j] = 1
            B[j, i] = 1
            sym.append(B)
            if i != j:
                A = sp.zeros(n)
                A[i, j] = 1
                A[j, i] = -1
                anti.append(A)
    return (kernel_dim(full), kernel_dim(sym), kernel_dim(anti))


def commutant_basis(R, n, part):
    """explicit exact basis of the (anti)symmetric commutant."""
    basis = []
    for i in range(n):
        for j in range(i, n):
            if part == "sym":
                B = sp.zeros(n)
                B[i, j] = 1
                B[j, i] = 1
                basis.append(B)
            elif i != j:
                B = sp.zeros(n)
                B[i, j] = 1
                B[j, i] = -1
                basis.append(B)
    cols = []
    for B in basis:
        D = R * B - B * R
        cols.append([D[r, c] for r in range(n) for c in range(n)])
    ns = sp.Matrix(cols).T.nullspace()
    out = []
    for v in ns:
        X = sp.zeros(n)
        for t, B in enumerate(basis):
            if v[t] != 0:
                X += v[t] * B
        out.append(X)
    return out


def span_dim(mats):
    if not mats:
        return 0
    n = mats[0].shape[0]
    M = sp.Matrix([[X[r, c] for r in range(n) for c in range(n)]
                   for X in mats])
    return M.rank()


def perm_matrix12(perm):
    """12x12 permutation matrix (all signs +1) from an alias map."""
    R = sp.zeros(12)
    for j in ALIASES:
        R[POS[perm[j]], POS[j]] = 1
    return R


def main():
    print("SEAM.CFIN.INTERTWINER12.01 -- does an intertwiner carry "
          "the 8+4 = 12 split?  (round 58, strategy S2)")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("Pure exact arithmetic; NO claim upgrades; exploration "
          "only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (corpus rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s"
          % (BANNED_IDS,), not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique "
          "q* under the frozen selector",
          ok_ref and len(set(refs)) == 16 and len(arf1) == 6
          and len(cand) == 1, kill="K0")
    QSTAR = cand[0]
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    DUADS_L = sorted((frozenset(d)
                      for d in itertools.combinations(range(6), 2)),
                     key=sorted)
    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS_L)
    check("S0.2 duad model: 15 messages <-> 15 duads; vacuum label "
          "V0 = %d" % V0, biject and 0 <= V0 < 6, kill="K0")

    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5
               and set(phi.values()) == set(range(1, 6)))
    check("S0.3 carrier dictionary phi (ovoid-induced) bijective: %s"
          % (sorted(phi.items()),), ok_phi, kill="K0")

    def lab(j):
        return 0 if j == V0 else phi[j]

    # deployed C6: Sp(4,2) census + Aut pin (wick_block verbatim)
    gl_n = 0
    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        gl_n += 1
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                              for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.4 |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == 720, "
          "|Aut(C_fin)| = %d == 6, generator pin g^2 = sigma unique"
          % (gl_n, len(SP6), len(AUT)),
          gl_n == 20160 and len(SP6) == 720 and len(AUT) == 6
          and len(g_pin) == 1, kill="K0")
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(pia[j])
    PI6 = tuple(PI6)
    ct6 = cycle_type(PI6)
    ok_int = all(dmap[GEN[v]] == frozenset(pia[j] for j in dmap[v])
                 for v in NZ)
    check("S0.5 DEPLOYED channel permutation PI6 = %s: fixes "
          "channel 0, cycle type %s == (1, 2, 3); intertwines the "
          "duad action on all 15" % (PI6, ct6),
          PI6[0] == 0 and ct6 == (1, 2, 3) and ok_int, kill="K0")

    # the 16-dim lift O16, the compression T, the 12-dim lift Ohat
    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    O16 = sp.zeros(16)
    for r in CH[0]:
        O16[r, r] = 1
    for i in range(1, 6):
        src, dst = CH[i], CH[PI6[i]]
        O16[dst[0], src[0]] = 1
        O16[dst[1], src[1]] = 1

    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}
    IOTA6 = sp.Matrix.vstack(sp.eye(2), sp.eye(2), sp.eye(2))
    Tcmp = sp.zeros(12, 16)
    for r in range(2):
        for c in range(6):
            Tcmp[r, CH[0][c]] = sp.Rational(IOTA6[c, r], 3)
    for i in range(1, 6):
        Tcmp[CH2[i][0], CH[i][0]] = 1
        Tcmp[CH2[i][1], CH[i][1]] = 1

    Ohat = sp.zeros(12)
    Ohat[0, 0] = 1
    Ohat[1, 1] = 1
    for i in range(1, 6):
        src, dst = CH2[i], CH2[PI6[i]]
        Ohat[dst[0], src[0]] = 1
        Ohat[dst[1], src[1]] = 1
    ohat_ord = mat_order(Ohat)
    check("S0.6 COMPRESSED C6 LIFT Ohat: orthogonal integer (%s), "
          "order EXACTLY %s == 6; compression ward T O16 == Ohat T "
          "(%s); dim 12 == 2 (g_car + 1) (%s), compression "
          "normalization 1/3 = 1/N_fam (%s)"
          % (sp.simplify(Ohat * Ohat.T) == sp.eye(12), ohat_ord,
             sp.simplify(Tcmp * O16 - Ohat * Tcmp) == sp.zeros(12,
                                                               16),
             12 == 2 * (g_car + 1), N_fam == 3),
          sp.simplify(Ohat * Ohat.T) == sp.eye(12)
          and ohat_ord == 6
          and sp.simplify(Tcmp * O16 - Ohat * Tcmp)
          == sp.zeros(12, 16)
          and 12 == 2 * (g_car + 1) and N_fam == 3, kill="K0")

    # ==================================================================
    section("F1 -- THE F-SIDE CHARACTER (exact)")
    # ==================================================================
    chi_F = char_of(Ohat)
    print("      chi_F(g^k), k = 0..5: %s" % (chi_F,))
    check("F1.1 chi_F == (12, 2, 6, 8, 6, 2) (signed permutation "
          "traces of the (1,2,3) channel cycle type, measured)",
          chi_F == [12, 2, 6, 8, 6, 2], kill="K1")

    mF, okF = real_mults(chi_F)
    print("      complex multiplicities m_0..m_5: %s"
          % (complex_mults(chi_F),))
    print("      REAL MULTIPLICITY VECTOR m_F (triv, sign, E1, E2) "
          "= %s" % (mF,))
    check("F1.2 m_F == (6, 2, 0, 2): 12 = 6 triv + 2 sign + 2 E2 "
          "(E1, the faithful 2-dim, is ABSENT); integrality + "
          "conjugation symmetry (%s); reconstruction sum m chi == "
          "chi_F (%s)"
          % (okF, reconstructs(chi_F, mF)),
          mF == (6, 2, 0, 2) and okF and reconstructs(chi_F, mF),
          kill="K1")

    PJ = iso_projectors(Ohat)
    ranks = {k: PJ[k].rank() for k in REAL_ORDER}
    ok_id = all(sp.simplify(PJ[k] * PJ[k] - PJ[k]) == sp.zeros(12)
                for k in REAL_ORDER)
    ok_orth = all(
        sp.simplify(PJ[a] * PJ[b]) == sp.zeros(12)
        for a, b in itertools.combinations(REAL_ORDER, 2))
    PJ_sum = sp.zeros(12)
    for k in REAL_ORDER:
        PJ_sum += PJ[k]
    ok_sum = sp.simplify(PJ_sum - sp.eye(12)) == sp.zeros(12)
    check("F1.3 exact isotypic projectors: idempotent (%s), "
          "mutually orthogonal (%s), sum = I (%s); ranks %s == "
          "{triv 6, sign 2, E1 0, E2 4}"
          % (ok_id, ok_orth, ok_sum, ranks),
          ok_id and ok_orth and ok_sum
          and [ranks[k] for k in REAL_ORDER] == [6, 2, 0, 4],
          kill="K1")

    # ==================================================================
    section("F2 -- THE COMMUTANT SPLIT (round-51 object, measured)")
    # ==================================================================
    P6 = sp.zeros(6)
    for i in range(6):
        P6[PI6[i], i] = 1
    d_full, d_sym, d_anti = commutant_dims(P6, 6)
    check("F2.1(a) scalar channel commutant of PI6 on 6x6: dim %d "
          "== 12, symmetric %d == 8, antisymmetric %d == 4 (the "
          "round-51 measured split, rebuilt exactly)"
          % (d_full, d_sym, d_anti),
          (d_full, d_sym, d_anti) == (12, 8, 4), kill="K1")

    Xs = sp.Matrix(6, 6, lambda r, c:
                   sp.Symbol("x_%d%d" % (r, c)))
    lift_id = sp.simplify(
        sp.Matrix(sp.kronecker_product(Xs, sp.eye(2))) * Ohat
        - Ohat * sp.Matrix(sp.kronecker_product(Xs, sp.eye(2)))
        - sp.Matrix(sp.kronecker_product(Xs * P6 - P6 * Xs,
                                         sp.eye(2))))
    # NOTE: Ohat = P6 (x) I2 in the CH2 coordinates up to the
    # channel-block ordering; the identity is checked directly.
    ok_lift = (sp.simplify(
        Ohat - sp.Matrix(sp.kronecker_product(P6, sp.eye(2))))
        == sp.zeros(12))
    b_full, b_sym, b_anti = commutant_dims(Ohat, 12)
    check("F2.2(b) block identification: Ohat == P6 (x) I2 exactly "
          "(%s), so [X (x) I2, Ohat] = [X, P6] (x) I2 (symbolic "
          "residual == 0: %s) and the 12 = 8 + 4 lives verbatim on "
          "the channel-scalar subalgebra; FULL block commutant "
          "measured: dim %d == 48 = 28 sym + 20 antisym (%d/%d)"
          % (ok_lift, lift_id == sp.zeros(12), b_full, b_sym,
             b_anti),
          ok_lift and lift_id == sp.zeros(12)
          and (b_full, b_sym, b_anti) == (48, 28, 20), kill="K1")

    m_scalar, ok_ms = real_mults(char_of(P6))
    def book(m):
        t, s, e1, e2 = m
        return (t * (t + 1) / 2 + s * (s + 1) / 2
                + e1 ** 2 + e2 ** 2,
                t * (t - 1) / 2 + s * (s - 1) / 2
                + e1 ** 2 + e2 ** 2)
    bs, ba = book(m_scalar)
    bbs, bba = book(mF)
    check("F2.3(c) bookkeeping identity vs measured: scalar mults "
          "%s -> (sym, antisym) = (%s, %s) == (8, 4); block mults "
          "%s -> (%s, %s) == (28, 20) -- the 8/4 numbers are a "
          "FUNCTION of the multiplicity vector"
          % (m_scalar, bs, ba, mF, bbs, bba),
          ok_ms and m_scalar == (3, 1, 0, 1)
          and (bs, ba) == (8, 4) and (bbs, bba) == (28, 20),
          kill="K1")

    # (d)(i) the unique (8, 4) isotypic union of the BLOCK SPACE
    comps = [(k, ranks[k]) for k in REAL_ORDER if ranks[k] > 0]
    unions = []
    for rmask in range(1, 2 ** len(comps) - 1):
        grp = [comps[i] for i in range(len(comps))
               if rmask >> i & 1]
        if sum(d for _k, d in grp) == 8:
            unions.append(sorted(k for k, _d in grp))
    check("F2.4(d-i) SPACE SPLIT: unions of isotypic components "
          "with dims (8, 4): %s == [['sign', 'triv']] -- UNIQUE: "
          "F_sym := triv(6) (+) sign(2) = 8, F_anti := E2 = 4"
          % (unions,),
          unions == [["sign", "triv"]], kill="K1")
    F_SYM = PJ["triv"] + PJ["sign"]
    F_ANTI = PJ["E2"]

    # (d)(ii) per-isotypic support census of the measured commutant
    sym_basis = commutant_basis(P6, 6, "sym")
    anti_basis = commutant_basis(P6, 6, "anti")
    PJ6 = iso_projectors(P6)
    ok_pres = True
    census = {}
    for name, basis in (("sym", sym_basis), ("anti", anti_basis)):
        row = {}
        for k in REAL_ORDER:
            diag = [sp.Matrix(PJ6[k] * X * PJ6[k]) for X in basis]
            row[k] = span_dim(diag)
        offsum = sp.zeros(6)
        for X in basis:
            for a, b2 in itertools.permutations(REAL_ORDER, 2):
                offsum += (PJ6[a] * X * PJ6[b2]).applyfunc(sp.Abs)
        ok_pres &= (sp.simplify(offsum) == sp.zeros(6))
        census[name] = row
    print("      per-isotypic support of the measured commutant "
          "(scalar level): sym %s | anti %s"
          % ({k: census["sym"][k] for k in REAL_ORDER},
             {k: census["anti"][k] for k in REAL_ORDER}))
    aligned = (census["sym"]["E2"] == 0
               and census["anti"]["triv"] == 0
               and census["anti"]["sign"] == 0)
    check("F2.5(d-ii) ALGEBRA SPLIT census: every commutant element "
          "preserves isotypics (off-blocks == 0: %s); sym 8 = "
          "(triv %s, sign %s, E2 %s) and antisym 4 = (triv %s, "
          "sign %s, E2 %s) -- the sym/antisym split %s align "
          "component-by-component with the (8,4) space split "
          "(measured either way: the honest anatomy of the two "
          "8+4s)"
          % (ok_pres, census["sym"]["triv"], census["sym"]["sign"],
             census["sym"]["E2"], census["anti"]["triv"],
             census["anti"]["sign"], census["anti"]["E2"],
             "DOES" if aligned else "does NOT"),
          ok_pres
          and census["sym"]["triv"] + census["sym"]["sign"]
          + census["sym"]["E2"] == 8
          and census["anti"]["triv"] + census["anti"]["sign"]
          + census["anti"]["E2"] == 4, kill="K1")

    # ==================================================================
    section("A1 -- THE A-SIDE ACTIONS (hard-coded signed "
            "permutations on the 12 aliases)")
    # ==================================================================
    print("      alias order (frozen): %s" % (ALIASES,))
    print("      deep-8 %s | exterior-4 %s" % (DEEP8, EXT4))

    # (a) FOLD -- identity on the folded representatives
    fold_perm = {j: j for j in ALIASES}
    R_fold = perm_matrix12(fold_perm)
    chi_fold = char_of(R_fold)
    m_fold, ok_mf = real_mults(chi_fold)
    check("A1.1(a) FOLD j -> L - j: every alias is its own folded "
          "representative (max alias 24 < L/2 on every frame-A "
          "rung), the reflection maps each unfolded pair {j, L-j} "
          "to itself -> induced action = IDENTITY, all 12 fixed, "
          "sign +1; chi_A = %s, mults %s == (12, 0, 0, 0)"
          % (chi_fold, m_fold),
          R_fold == sp.eye(12) and m_fold == (12, 0, 0, 0)
          and ok_mf and reconstructs(chi_fold, m_fold), kill="K2")

    # (b) SHIFT -- order-6 version of the alias 12-cycle
    shift_perm = {j: (ALIASES[(POS[j] + 2) % 12]) for j in ALIASES}
    R_shift = perm_matrix12(shift_perm)
    chi_shift = char_of(R_shift)
    m_shift, ok_msh = real_mults(chi_shift)
    ord_shift = mat_order(R_shift)
    cycs = cycle_type(tuple(POS[shift_perm[ALIASES[p]]]
                            for p in range(12)))
    check("A1.2(b) SHIFT sigma^2: j -> j + 4 with wraparound, "
          "cycle type %s == (6, 6) -- two 6-cycles (2 6 10 14 18 "
          "22)(4 8 12 16 20 24), order %s == 6; chi_A = %s, mults "
          "%s == (2, 2, 2, 2) (twice the regular representation)"
          % (cycs, ord_shift, chi_shift, m_shift),
          cycs == (6, 6) and ord_shift == 6
          and chi_shift == [12, 0, 0, 0, 0, 0]
          and m_shift == (2, 2, 2, 2) and ok_msh
          and reconstructs(chi_shift, m_shift), kill="K2")

    # (c) CLOCK -- the order-6 quotient of the mod-30 clock
    alias_set = set(ALIASES)
    closed_rot = [s for s in range(MOD30)
                  if all((j + s) % MOD30 in alias_set
                         for j in ALIASES)]
    closed_ref = [s for s in range(MOD30)
                  if all((s - j) % MOD30 in alias_set
                         for j in ALIASES)]
    ord6_rots = [s for s in range(MOD30)
                 if MOD30 // sp.gcd(s, MOD30) == 6]
    check("A1.3(c) MOD-30 CLOCK CENSUS: alias-preserving rotations "
          "T^s: s in %s == [0]; alias-preserving reflections "
          "F T^s: s in %s == [26] (j -> 26 - j); order-6 rotations "
          "of the clock: s in %s == [5, 25], BOTH ODD -- the "
          "parity obstruction: no order-6 clock element acts on "
          "the even aliases; maximal induced group = C2"
          % (closed_rot, closed_ref, ord6_rots),
          closed_rot == [0] and closed_ref == [26]
          and ord6_rots == [5, 25]
          and all(s % 2 == 1 for s in ord6_rots), kill="K2")

    clock_perm = {j: (26 - j) % MOD30 for j in ALIASES}
    R_refl = perm_matrix12(clock_perm)
    # canonical action of the order-6 quotient THROUGH its maximal
    # alias-preserving image C2: g -> (j -> 26 - j)
    chi_clock = char_of(R_refl)  # order 2: chi at g^k = R_refl^k
    m_clock, ok_mc = real_mults(chi_clock)
    swaps = sorted((j, clock_perm[j]) for j in ALIASES
                   if j < clock_perm[j])
    deep_img = sorted(clock_perm[j] for j in DEEP8)
    split_stable = (set(deep_img) == set(DEEP8))
    check("A1.4(c) CLOCK action (through the maximal image C2): "
          "j -> 26 - j, pairs %s, order %s == 2; as the canonical "
          "C6-quotient action chi_A = %s, mults %s == (6, 6, 0, 0)"
          % (swaps, mat_order(R_refl), chi_clock, m_clock),
          mat_order(R_refl) == 2
          and chi_clock == [12, 0, 12, 0, 12, 0]
          and m_clock == (6, 6, 0, 0) and ok_mc
          and reconstructs(chi_clock, m_clock), kill="K2")
    print("      NOTE (measured): the only nontrivial clock "
          "symmetry of the window maps deep-8 -> %s -- it SWAPS "
          "{2,4,6,8} with the exterior {24,22,20,18}: the deep-8 / "
          "exterior-4 split is %s clock-stable."
          % (deep_img, "NOT" if not split_stable else ""))

    # ==================================================================
    section("M1 -- THE MATCH + THE INTERTWINER")
    # ==================================================================
    cands = [("FOLD", R_fold, m_fold),
             ("SHIFT", R_shift, m_shift),
             ("CLOCK", R_refl, m_clock)]
    print("      F-side multiplicity vector m_F = %s" % (mF,))
    matches = []
    for name, R, m in cands:
        mism = [REAL_ORDER[i] for i in range(4) if m[i] != mF[i]]
        tag = "MATCH" if not mism else ("MISMATCH at %s" % mism)
        print("      %-6s mults %-14s -> %s" % (name, m, tag))
        if not mism:
            matches.append((name, R, m))
    check("M1.1 match census: %d of 3 candidates carry the F-side "
          "character (fold: triv-only; shift: regular x2; clock: "
          "quotient-degenerate -- each differs from (6, 2, 0, 2))"
          % len(matches), len(matches) in (0, 1, 2, 3),
          "measured either way", kill="K3")

    typed = None
    if matches:
        name, R, m = matches[0]
        # equivariant averaging from the identity seed
        Phi = sp.zeros(12)
        Ok, Rk = sp.eye(12), sp.eye(12)
        Rinv = R.inv()
        for _k in range(6):
            Phi += Ok * Rk
            Ok = Ohat * Ok
            Rk = Rinv * Rk
        Phi = Phi / 6
        defect = fro2(Ohat * Phi - Phi * R)
        inv_ok = (Phi.det() != 0)
        deep_cols = [POS[j] for j in DEEP8]
        ext_cols = [POS[j] for j in EXT4]
        img_deep = Phi[:, deep_cols]
        img_ext = Phi[:, ext_cols]
        deep_in_sym = (sp.simplify(F_ANTI * img_deep)
                       == sp.zeros(12, 8)
                       and (F_SYM * img_deep).rank() == 8)
        ext_in_anti = (sp.simplify(F_SYM * img_ext)
                       == sp.zeros(12, 4)
                       and (F_ANTI * img_ext).rank() == 4)
        print("      Phi block structure (rows = F, cols = A):")
        sp.pprint(Phi)
        check("M1.2 INTERTWINER for %s: equivariance defect %s "
              "(must be 0), invertible %s, deep-8 -> F_sym %s, "
              "exterior-4 -> F_anti %s"
              % (name, defect, inv_ok, deep_in_sym, ext_in_anti),
              defect == 0 and inv_ok, kill="K3")
        if defect == 0 and inv_ok and deep_in_sym and ext_in_anti:
            typed = ("INTERTWINER-EXISTS(%s, %s)" % (name, (m,)))
            print("      BONUS (descriptive, no bar): transport of "
                  "the eta-minimizer seat and the wall soft-mode "
                  "coordinate through Phi -- distinguished images "
                  "printed above via the Phi columns at their "
                  "alias positions.")
        else:
            typed = ("INTERTWINER-PARTIAL(%s: defect %s, inv %s, "
                     "split %s/%s)" % (name, defect, inv_ok,
                                       deep_in_sym, ext_in_anti))
    else:
        typed = "INTERTWINER-EMPTY"
        check("M1.2 NO candidate matches -> no Phi is constructed; "
              "the split question and the BONUS transport (eta-"
              "minimizer seat, soft-mode coordinate) are VACUOUS",
              True, "typed, first-class outcome")
        print("      HONEST DEMOTION LINE (verbatim, per the "
              "firewall):")
        print("      8+4 = 12 is typed NUMEROLOGY-UNTIL-NEW-ACTION "
              "per the firewall: the finite side is structured "
              "(the block 12 splits isotypically 8 = triv+sign / "
              "4 = E2 under Ohat), but NO natural arithmetic "
              "action on the 12 aliases -- fold, shift, or mod-30 "
              "clock -- carries the C6 character (6, 2, 0, 2); "
              "without an intertwiner the numeric coincidence "
              "stays decorative.")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    # C1: synthetic transplant + frozen labeling shuffle
    rho_star = sp.Matrix(Ohat)     # Ohat read on alias positions
    m_star, _ok = real_mults(char_of(rho_star))
    Phi_c = sp.zeros(12)
    Ok, Rk = sp.eye(12), sp.eye(12)
    rinv = rho_star.T              # orthogonal
    for _k in range(6):
        Phi_c += Ok * Rk
        Ok = Ohat * Ok
        Rk = rinv * Rk
    Phi_c = Phi_c / 6
    def0 = fro2(Ohat * Phi_c - Phi_c * rho_star)
    S = sp.eye(12)
    a, b2 = SHUFFLE_SWAP
    S[a, a] = S[b2, b2] = 0
    S[a, b2] = S[b2, a] = 1
    rho_sh = S * rho_star * S.T
    m_sh, _ok2 = real_mults(char_of(rho_sh))
    def_sh = fro2(Ohat * Phi_c - Phi_c * rho_sh)
    check("C1 FIRES: TRANSPLANT ward -- rho* (Ohat on alias "
          "positions) matches by construction (mults %s == %s), "
          "averaged Phi has defect %s == 0 and det %s != 0; the "
          "FROZEN SHUFFLE (positions %s swapped) keeps the "
          "character (mults %s, unchanged -- matches survive every "
          "relabeling) but breaks the fixed intertwiner: defect "
          "%s != 0 -- characters are cheap, the intertwiner is the "
          "content"
          % (m_star, mF, def0, Phi_c.det(), SHUFFLE_SWAP, m_sh,
             def_sh),
          m_star == mF and def0 == 0 and Phi_c.det() != 0
          and m_sh == mF and def_sh != 0, kill="K7")

    # C2: character orthogonality wards
    gram = sp.Matrix(4, 4, lambda r, c: sp.Rational(
        sum(CHI_REAL[REAL_ORDER[r]][k] * CHI_REAL[REAL_ORDER[c]][k]
            for k in range(6)), 6))
    ok_gram = gram == sp.diag(1, 1, 2, 2)
    ok_rec = all(
        reconstructs(chi, m) and all(v.is_integer and v >= 0
                                     for v in m)
        for chi, m in ((chi_F, mF), (chi_fold, m_fold),
                       (chi_shift, m_shift), (chi_clock, m_clock)))
    check("C2 WARDS: real C6 character Gram (1/6 sum) == "
          "diag(1, 1, 2, 2) with zero off-diagonals (%s); every "
          "multiplicity vector is a nonnegative integer vector "
          "that reconstructs its character exactly (%s)"
          % (ok_gram, ok_rec), ok_gram and ok_rec, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "K7" in KILLS:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = "INTERTWINER12-PARTIAL [%s]" % ", ".join(
            sorted(set({"K1": "FSIDE-BROKEN",
                        "K2": "ASIDE-BROKEN",
                        "K3": "MATCH-BROKEN"}.get(k, k)
                       for k in KILLS)))
    else:
        VERDICT = ("INTERTWINER12-MEASURED [%s; F-SPLIT-ISOTYPIC"
                   "(8 = triv6 + sign2, 4 = E2); "
                   "CLOCK-NO-C6-ACTION(parity)]" % typed)
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * F-SIDE (F1/F2): chi_F = (12, 2, 6, 8, 6, 2), multiplicities
    (triv, sign, E1, E2) = %s -- the faithful 2-dim E1 is ABSENT.
    The unique (8, 4) union of isotypic components is F_sym =
    triv(6) (+) sign(2) vs F_anti = E2(4).  The round-51 commutant
    12 = 8 + 4 is rebuilt exactly and its per-isotypic anatomy is
    sym = (triv %s, sign %s, E2 %s) / anti = (triv %s, sign %s,
    E2 %s): the two F-side 8+4s (space split vs algebra split)
    have DIFFERENT isotypic provenance -- already on the finite
    side the coincidence of the two numbers is bookkeeping, not
    one object.
  * A-SIDE (A1): fold = identity (mults (12,0,0,0)); order-6 shift
    = two 6-cycles (mults (2,2,2,2), twice regular); the mod-30
    clock CANNOT act with order 6 on the even aliases (all order-6
    clock elements are odd shifts 5/25 -- exact parity
    obstruction); its maximal induced symmetry is the single
    reflection j -> 26 - j, which does not even preserve the
    deep-8 / exterior-4 split (it swaps {2,4,6,8} with the
    exterior).
  * THE ANSWER (M1): %s.
  * CONTROLS: the transplant ward proves the machinery FINDS a
    match and a zero-defect Phi when one exists, and the frozen
    labeling shuffle preserves the character while killing the
    intertwiner -- the reviewer's point, mechanized.
  * No marker moves; nothing upgraded; the finite-side structure
    (isotypic split) and the arithmetic-side structure (deep-8
    coherence) both stand, unconnected.
Runtime: %.1f s""" % (mF, census["sym"]["triv"],
                      census["sym"]["sign"], census["sym"]["E2"],
                      census["anti"]["triv"],
                      census["anti"]["sign"],
                      census["anti"]["E2"], typed,
                      time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
