#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""doily_selfduality_demand_probe -- SEAM.DOILY.SELFDUAL.DEMAND.01
(EXPLORATION ONLY, experiments/; 2026-08-12 -- the direct successor to
SEAM.QUADRATIC.EXHAUSTION.01 (CCXXXI, verdict P2-PARTIAL): can the
doily self-duality be formulated as a g-FREE compiler demand -- one
that mentions NO number 5 and NO carrier dimension -- which FORCES
g = 5 rather than presupposing it?  If yes, P2's residual axiom
collapses into a self-duality/incidence demand and P2 becomes a
theorem modulo ONE structural postulate with independent meaning.)

THE g-PARAMETRIZED STRUCTURE (CCXXXI T4, reused verbatim): for the
carrier parameter g, the extended letter set is X = {0, 1, .., g}
(|X| = g+1: g carrier letters + 1 vacuum letter; ONLY the count g+1
enters -- pure incidence combinatorics, no kernel, no wiring):
  points  P(g) = duads = 2-subsets of X   (the data alphabet;
                                           |P| = C(g+1, 2));
  lines   L(g) = perfect matchings of K_{g+1}   (the elementary
                 Wick contraction schemes; |L| = g!! for odd g,
                 0 for even g -- CCXXXI T4b);
  incidence  e I M  iff  e is one of the duads of M.
An ANTI-FLAG is a pair (e, M) with e not in M.  Write m = (g+1)/2
for odd g (the number of contractions per scheme).

THE CANDIDATE DEMANDS (each precise, checkable, g-free):
 D1 SELF-DUAL: |P| = |L| >= 1 and the incidence structure is
    isomorphic to its dual -- there is a bijection pair
    delta: P -> L, eps: L -> P with (e I M <=> eps(M) I delta(e)).
    Verified by exact backtracking count of part-swapping
    automorphisms of the Levi (incidence) graph.
 D2 GQ-DEMAND: NONDEG (at least one anti-flag exists) and BIREG
    (point- and line-regular) and AX1 (two distinct lines share
    <= 1 point) and AX2 (EVERY anti-flag (e, M) has EXACTLY ONE
    f in M with e cap f = empty -- the generalized-quadrangle
    anti-flag axiom; ward: whenever L is nonempty, two duads are
    collinear iff disjoint, so this IS the GQ axiom verbatim).
    SHARP CORE  D2core := NONDEG and AX2  ("every elementary
    contraction scheme routes each datum it does not consume
    through exactly one disjoint contraction" -- unambiguous
    routing, the compiler reading).
 D3 NATURAL-SELF-DUAL (the strict categorical form of 'the object
    of elementary data equals the object of elementary operations,
    naturally in the composition'): D1 with delta equivariant
    under the full letter-symmetry S_{g+1}
    (delta . pi_sigma = pi_sigma . delta for all sigma).
 WEAKENED VARIANTS (sharpness controls, must be reported as FAILED
 FORCING where they pass g != 5):
    W-COUNT   |P| = |L| >= 1        (this IS P-count of CCXXXI);
    W-BIREG   L nonempty and biregular;
    W-AX1     L nonempty and AX1;
    W-DUALAX1 L nonempty and two distinct points on <= 1 common
              line.

FROZEN FORCING RULE: a demand D FORCES g = 5 iff its pass-set on
g = 1..10 intersected with {2..10} equals {5}, and if g = 1 passes
it is killed by ALPHABET-EMPTY (the carrier bilinear alphabet
Lambda^2 E has dim C(1,2) = 0 -- the CCXXXI T4a kill, cited).
A demand that also passes at g = 3 or g = 7 (or any other g in
2..10) is FAILED-FORCING.

FROZEN CLAIMS (hand-derived before the run; verify, do not trust):
 F1 ANTI-FLAG LAW: at odd g the disjointness count is CONSTANT
    over ALL anti-flags and equals m - 2 (an anti-flag duad's two
    endpoints lie in two DISTINCT contractions of the scheme,
    killing exactly 2 of the m) ==> AX2 <=> m = 3 <=> g = 5, for
    ALL g by arithmetic; measured exhaustively on g = 1..10.
 F2 PASS-SETS on g = 1..10:  D1 {1, 5};  D2core {5} (g = 1 killed
    INTERNALLY by NONDEG: zero anti-flags);  D2full {5};
    D3 EMPTY -- the strict natural form fails EVEN AT g = 5
    (every doily duality is necessarily OUTER-twisted);
    W-COUNT {1, 5};  W-BIREG {1, 3, 5, 7, 9};  W-AX1 {1, 3, 5};
    W-DUALAX1 {1, 3, 5}.
 F3 DOILY STRUCTURE at g = 5: GQ(2,2) parameters exact (15/15,
    3-regular both ways, s = t = 2); collineations = 720 = the
    S6 letter action, faithful AND full (backtracking count ==
    the 720 induced maps, as sets); dualities = 720; correlation
    group order 1440 = |Aut(S6)|; ZERO of the 720 dualities is
    S6-equivariant; the automorphism of S6 induced by any duality
    maps a transposition to a triple transposition (cycle type
    2+2+2) = the OUTER class; stabilizer witness for the
    no-natural-correspondence: duad stabilizer order 48 with
    vertex orbits {2, 4}, matching stabilizer order 48 TRANSITIVE
    {6} -- non-conjugate subgroups, so no equivariant bijection
    between the two 15-element S6-sets can exist.
 F4 LETTER-VALUED COMPOSITION (the incidence avatar of CCXXXI's
    ONE-STEP + LETTER-DUAL): the complement of a disjoint duad
    pair is itself a duad iff 2m - 4 = 2 iff g = 5; at g = 5
    EVERY disjoint pair {e, f} closes with its complement c into
    a LINE {e, f, c} (all 45 = 15*6/2: each duad is disjoint from
    exactly C(4,2) = 6 others) -- depth-1 self-hosting IS the line
    closure of the alphabet; at g = 3 the complement is EMPTY
    (the composition dies, = Lambda^4 = 0), at odd g >= 7 the
    complement has >= 4 letters (the output leaves the alphabet,
    = the two-step regime).
 F5 EQUIPOTENCE: footprint(D2core) = footprint(EXHAUST-IDENT,
    the CCXXXI T3a census rebuilt uniformly on g = 2..10)
    = footprint(letter-valued composition) = {5}: the g-free
    incidence demand and the exterior-algebra identity carve the
    SAME class -- the collapse is a REFORMULATION, not a strictly
    more primitive premise.
 F6 DUAL ANTI-FLAG LAW (secondary): two disjoint duads lie on
    exactly (2m-5)!! common lines (uniform), so W-DUALAX1 <=>
    m <= 3.

FROZEN VERDICT RULE:
 COLLAPSE-G5-REFORMULATION iff D1, D2core, D2full all FORCE g = 5
   under the frozen rule, F1/F3/F4 hold as stated, all three
   weakened controls W-BIREG/W-AX1/W-DUALAX1 are FAILED-FORCING
   (census sharp), the equal-counts impostor control fires (counts
   15 = 15 yet AX2 broken and duality count 0 -- counts do NOT
   imply structure), and the equipotence F5 is measured -- the
   composed P2 theorem is then stated with the demand typed
   EQUIPOTENT-REFORMULATION: no measured independent compiler fact
   (mu4 step, orientation rules, E8 hull) implies the demand; that
   implication test is OPEN and outside finite incidence reach.
 COLLAPSE-G5-PRIMITIVE iff additionally an existing independent
   compiler fact measured HERE implies the demand (no such
   measurement is attempted in this probe; the enum exists so the
   distinction is typed, it cannot trigger).
 NO-COLLAPSE iff no structural demand forces g = 5, or a weakened
   control silently forces, or the impostor stays silent.

ANTI-CIRCULARITY (declared): every census consumes ONLY the letter
count g+1 and pure incidence combinatorics; NO rank(P), NO deployed
kernel, NO wiring, NO carrier data; g_car and N_fam are imported
READ-ONLY and appear exclusively in the S0 cross-ward and the final
N_fam bridge CITATION (CCXXXI T4b/c), never as census inputs.
Exact integer combinatorics throughout; NO float in any decision;
RNG nowhere.

EXTERNAL-CITED (classical facts, verified where finite): GQ(2,2) =
W(2) is the unique GQ of order (2,2) and is self-dual (Payne-Thas,
Finite Generalized Quadrangles, 2nd ed., EMS 2009, 5.2.3/6.1);
duads/synthemes and their duality: Sylvester 1861; the outer
automorphism of S6, transpositions -> triple transpositions, and
the non-existence of a natural duad/syntheme correspondence:
Hoelder 1895; Janusz-Rotman, Amer. Math. Monthly 89 (1982) 407-410.
Corpus anchor: v796 (the Sylvester bridge is OUTER, cited).

SMOKE-RUN DISCLOSURE (2026-08-12, one smoke round before freezing;
fail-first preserved; no claim inverted):
 (i)   SMOKE 1 FAILED 3/17, all three failures real and disclosed:
       (1)+(2) T1.2/T1.3 fell to a pure LOOKUP bug on the dual
       side: the common-line counter is keyed by mask-value-sorted
       duad pairs, but the disjoint-pair list was built in duad
       LIST order, which is not ascending as integers (e.g. the
       pair ({0,3}, {1,2}) = (9, 6) missed the key (6, 9)), so
       some disjoint pairs read 0 common lines; keys normalized --
       the anti-flag law T2.1, the forcing census T3 and every
       g = 5 structure check were UNAFFECTED and already passed in
       smoke with the hand-derived values (pass-sets exactly F2,
       720/720/1440, zero equivariant dualities, cycle type 2+2+2,
       stabilizers 48/{2,4} vs 48/{6}, impostor fired).
       (3) T5.2: the HAND COUNT of disjoint duad pairs in K6 was
       wrong (60); the machine says 45 = 15*6/2 -- each duad is
       disjoint from exactly C(4,2) = 6 others, not 8; the
       CLOSURE ITSELF held on 45/45 pairs already in smoke (the
       debug census showed 0 non-closing pairs), only the frozen
       cardinality was corrected in F4.  No decision logic, no
       demand definition, no forcing rule and no verdict rule
       changed; smoke 2 passed 17/17.
 (ii)  measured runtime 1.3 s in smoke; budget < 20 min trivially.
 (iii) the [DIAG] polarity count (dualities with delta^2 = id)
       measured 36 in smoke; REPORTED unfrozen (no claim).

VERDICT SEMANTICS: exploration only; NO status-ledger move, NO
paper edit, NO marker change.  Whatever T6 returns, P2 remains an
axiom in the compiler until a promotion decision is taken by the
maintainer.

Run:
    . experiments/tfpt-discovery/.venv/bin/activate
    python experiments/tfpt-discovery/doily_selfduality_demand_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402  (READ-ONLY)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime", "random",
              "randint", "seed", "shuffle")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

G_RANGE = list(range(1, 11))


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


# ======================================================== combinatorics
def dfact(k):
    """double factorial, (-1)!! = 0!! = 1."""
    r = 1
    while k > 1:
        r *= k
        k -= 2
    return r


def duad_masks(n):
    """All 2-subsets of {0..n-1} as bitmasks, sorted."""
    return [(1 << a) | (1 << b)
            for a in range(n) for b in range(a + 1, n)]


def perfect_matchings(verts):
    verts = sorted(verts)
    if not verts:
        return [[]]
    out = []
    v0 = verts[0]
    for w in verts[1:]:
        rest = [x for x in verts[1:] if x != w]
        for m in perfect_matchings(rest):
            out.append([(v0, w)] + m)
    return out


def lines_of(n):
    """Perfect matchings of K_n as sorted tuples of duad masks."""
    out = []
    for M in perfect_matchings(list(range(n))):
        out.append(tuple(sorted((1 << a) | (1 << b) for a, b in M)))
    return out


def structure(g):
    """Build the incidence structure S(g); everything exact."""
    n = g + 1
    pts = duad_masks(n)
    lns = lines_of(n)
    linesets = [frozenset(L) for L in lns]
    pt_deg = {e: 0 for e in pts}
    for L in lns:
        for e in L:
            pt_deg[e] += 1
    # anti-flag disjointness counts
    af_counts = set()
    n_af = 0
    for i, L in enumerate(lns):
        s = linesets[i]
        for e in pts:
            if e in s:
                continue
            n_af += 1
            af_counts.add(sum(1 for f in L if not (e & f)))
    # AX1: max shared duads between two distinct lines
    ax1_max = 0
    for i in range(len(lns)):
        si = linesets[i]
        for j in range(i + 1, len(lns)):
            v = len(si & linesets[j])
            if v > ax1_max:
                ax1_max = v
    # common-line counts for point pairs (dual side)
    pair_lines = {}
    for L in lns:
        for a, b in itertools.combinations(L, 2):
            key = (a, b) if a < b else (b, a)
            pair_lines[key] = pair_lines.get(key, 0) + 1
    # NOTE (smoke amendment): keys must be normalized by mask VALUE
    # (the duad list is not ascending as integers), see disclosure.
    disj_pairs = [tuple(sorted((a, b)))
                  for a, b in itertools.combinations(pts, 2)
                  if not (a & b)]
    disj_counts = set(pair_lines.get(p, 0) for p in disj_pairs)
    meet_extra = any(pair_lines.get(tuple(sorted(p)), 0) > 0
                     for p in itertools.combinations(pts, 2)
                     if (p[0] & p[1]))
    return dict(g=g, n=n, pts=pts, lns=lns, linesets=linesets,
                pt_deg=pt_deg, af_counts=af_counts, n_af=n_af,
                ax1_max=ax1_max, disj_pairs=disj_pairs,
                disj_counts=disj_counts, meet_extra=meet_extra,
                pair_lines=pair_lines)


# ================================================= Levi-graph machinery
def levi_graph(pts, lns, linesets):
    """Vertices 0..P-1 = points, P..P+L-1 = lines; adjacency sets."""
    P, L = len(pts), len(lns)
    n = P + L
    adj = [set() for _ in range(n)]
    idx = {e: i for i, e in enumerate(pts)}
    for j, s in enumerate(linesets):
        for e in s:
            adj[idx[e]].add(P + j)
            adj[P + j].add(idx[e])
    parts = [0] * P + [1] * L
    return adj, parts


def graph_maps(adj, parts, mode, collect=False, cap=None):
    """Count (and optionally collect) automorphisms of the graph.
    mode: 'pre' part-preserving, 'swap' part-swapping.
    Exact backtracking with full adjacency biconditional."""
    n = len(adj)
    deg = [len(adj[v]) for v in range(n)]
    order = []
    seen = set()
    for root in range(n):
        if root in seen:
            continue
        queue = [root]
        seen.add(root)
        while queue:
            v = queue.pop(0)
            order.append(v)
            for u in sorted(adj[v]):
                if u not in seen:
                    seen.add(u)
                    queue.append(u)
    mapping = [None] * n
    used = [False] * n
    found = []
    count = [0]

    def ok_part(v, w):
        return (parts[w] == parts[v]) if mode == "pre" \
            else (parts[w] == 1 - parts[v])

    def extend(k):
        if cap is not None and count[0] > cap:
            return
        if k == n:
            count[0] += 1
            if collect:
                found.append(tuple(mapping))
            return
        v = order[k]
        mapped_nbrs = [u for u in adj[v] if mapping[u] is not None]
        if mapped_nbrs:
            cand = set(adj[mapping[mapped_nbrs[0]]])
            for u in mapped_nbrs[1:]:
                cand &= adj[mapping[u]]
        else:
            cand = set(range(n))
        for w in sorted(cand):
            if used[w] or deg[w] != deg[v] or not ok_part(v, w):
                continue
            good = True
            for idx2 in range(k):
                u = order[idx2]
                if (u in adj[v]) != (mapping[u] in adj[w]):
                    good = False
                    break
            if good:
                mapping[v] = w
                used[w] = True
                extend(k + 1)
                mapping[v] = None
                used[w] = False

    extend(0)
    return count[0], found


def induced_vertex_maps(pts, lns, sigma):
    """The permutation pi_sigma of the Levi vertices induced by a
    permutation sigma of the letters (list of images)."""
    P = len(pts)

    def pm(mask):
        out = 0
        b = 0
        m = mask
        while m:
            if m & 1:
                out |= (1 << sigma[b])
            m >>= 1
            b += 1
        return out

    pt_idx = {e: i for i, e in enumerate(pts)}
    ln_idx = {L: j for j, L in enumerate(lns)}
    pi = [0] * (P + len(lns))
    for i, e in enumerate(pts):
        pi[i] = pt_idx[pm(e)]
    for j, L in enumerate(lns):
        pi[P + j] = P + ln_idx[tuple(sorted(pm(f) for f in L))]
    return tuple(pi)


# ============================================ exterior census (CCXXXI)
def exhaust_ident(g):
    """CCXXXI T3a EXHAUST-IDENT rebuilt: Lambda^2 E wedge Lambda^2 E
    = Lambda^{g-1} E as a monomial-span census (exact)."""
    dd = duad_masks(g)          # carrier duads: 2-subsets of g letters
    span2 = set()
    for m in dd:
        for d in dd:
            if not (m & d):
                span2.add(m | d)
    return (g - 1 == 4) and (len(span2) == math.comb(g, 4)) \
        and (math.comb(g, 4) == math.comb(g, g - 1))


def main():
    print("SEAM.DOILY.SELFDUAL.DEMAND.01 -- the g-free self-duality "
          "demand census (successor to CCXXXI)")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + read-only constants ward")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers, RNG nowhere",
          not bad, "found %s" % bad if bad else "", kill="K0")
    check("S0.1 read-only cross-ward: g_car == 5, N_fam == 3 "
          "(imported, NEVER a census input)",
          g_car == 5 and N_fam == 3, kill="K0")

    # ==================================================================
    section("T1 -- construction census g = 1..10 (exact)")
    # ==================================================================
    S = {g: structure(g) for g in G_RANGE}
    want_mt = {1: 1, 2: 0, 3: 3, 4: 0, 5: 15, 6: 0, 7: 105, 8: 0,
               9: 945, 10: 0}
    ok_counts = True
    for g in G_RANGE:
        st = S[g]
        ok_counts &= (len(st["pts"]) == math.comb(g + 1, 2))
        ok_counts &= (len(st["lns"]) == want_mt[g])
        if g % 2 == 1:
            degs = set(st["pt_deg"].values())
            ok_counts &= (degs == {dfact(g - 2)})
        print("    g=%d: |P| = %d = C(%d,2), |L| = %d, per-duad "
              "multiplicity %s"
              % (g, len(st["pts"]), g + 1, len(st["lns"]),
                 sorted(set(st["pt_deg"].values()))))
    check("T1.1 counts: |P| = C(g+1,2), matching census %s, per-duad "
          "multiplicity (g-2)!! at odd g (CCXXXI T4b rebuilt)"
          % ([want_mt[g] for g in G_RANGE],), ok_counts, kill="K1")

    ok_coll = True
    for g in G_RANGE:
        if g % 2 == 1 and S[g]["lns"]:
            # every disjoint pair lies on >= 1 common line
            ok_coll &= all(S[g]["pair_lines"].get(p, 0) >= 1
                           for p in S[g]["disj_pairs"])
            # meeting duads never share a line
            ok_coll &= not S[g]["meet_extra"]
    check("T1.2 collinear <=> disjoint whenever L nonempty (every "
          "disjoint pair extends to a matching; meeting pairs never "
          "share a line) -- AX2 is the GQ anti-flag axiom verbatim",
          ok_coll, kill="K1")

    ok_dual_law = True
    dl_tab = {}
    for g in G_RANGE:
        if g % 2 == 1 and g >= 3:
            m = (g + 1) // 2
            dl_tab[g] = sorted(S[g]["disj_counts"])
            ok_dual_law &= (S[g]["disj_counts"] == {dfact(2 * m - 5)})
    check("T1.3 dual anti-flag law (F6): two disjoint duads lie on "
          "exactly (2m-5)!! common lines, uniform: %s" % dl_tab,
          ok_dual_law, kill="K1")

    # ==================================================================
    section("T2 -- the demands (defined in the frozen spec; census "
            "columns computed here)")
    # ==================================================================
    # anti-flag law F1
    ok_af = True
    af_tab = {}
    for g in G_RANGE:
        st = S[g]
        if g % 2 == 1 and st["n_af"] > 0:
            m = (g + 1) // 2
            af_tab[g] = (sorted(st["af_counts"]), st["n_af"], m - 2)
            ok_af &= (st["af_counts"] == {m - 2})
        else:
            af_tab[g] = ("no anti-flags", st["n_af"], None)
    arith = all(((mm - 2 == 1) == (mm == 3)) for mm in range(2, 51))
    check("T2.1 ANTI-FLAG LAW (F1): disjointness count UNIFORM = m-2 "
          "over ALL anti-flags at every odd g with anti-flags %s; "
          "m-2 = 1 <=> m = 3 <=> g = 5 (arithmetic, all m <= 50)"
          % ({g: af_tab[g][0] for g in af_tab if g % 2 == 1},),
          ok_af and arith, kill="K2")

    # per-g demand columns
    cols = {}
    for g in G_RANGE:
        st = S[g]
        P, L = len(st["pts"]), len(st["lns"])
        nondeg = st["n_af"] > 0
        bireg = (L > 0
                 and len(set(st["pt_deg"].values())) == 1
                 and min(st["pt_deg"].values()) > 0)
        ax1 = (L > 0) and (st["ax1_max"] <= 1) if L > 1 else (L > 0)
        ax2 = nondeg and (st["af_counts"] == {1})
        count_eq = (P == L) and (L >= 1)
        dual_ax1 = (L > 0) and all(v <= 1
                                   for v in st["disj_counts"]) \
            if st["disj_pairs"] else (L > 0)
        cols[g] = dict(nondeg=nondeg, bireg=bireg, ax1=ax1, ax2=ax2,
                       count_eq=count_eq, dual_ax1=dual_ax1)

    # D1 self-duality: count-guard, then exact Levi backtracking
    selfdual = {}
    dual_counts = {}
    for g in G_RANGE:
        if not cols[g]["count_eq"]:
            selfdual[g] = False
            continue
        st = S[g]
        adj, parts = levi_graph(st["pts"], st["lns"], st["linesets"])
        cnt, _ = graph_maps(adj, parts, "swap", collect=False)
        dual_counts[g] = cnt
        selfdual[g] = cnt > 0
    print("    duality counts where |P| = |L| >= 1: %s" % dual_counts)

    # ==================================================================
    section("T3 -- THE FORCING CENSUS (demand x g, exact)")
    # ==================================================================
    def passes(g, name):
        c = cols[g]
        if name == "D1":
            return selfdual[g]
        if name == "D2core":
            return c["nondeg"] and c["ax2"]
        if name == "D2full":
            return (c["nondeg"] and c["bireg"] and c["ax1"]
                    and c["ax2"])
        if name == "W-COUNT":
            return c["count_eq"]
        if name == "W-BIREG":
            return c["bireg"]
        if name == "W-AX1":
            return (len(S[g]["lns"]) > 0) and c["ax1"]
        if name == "W-DUALAX1":
            return (len(S[g]["lns"]) > 0) and c["dual_ax1"]
        raise KeyError(name)

    names = ["D1", "D2core", "D2full", "W-COUNT", "W-BIREG",
             "W-AX1", "W-DUALAX1"]
    pass_sets = {nm: sorted(g for g in G_RANGE if passes(g, nm))
                 for nm in names}
    hdr = "    %-10s " % "demand" + " ".join("g=%-2d" % g
                                             for g in G_RANGE)
    print(hdr)
    for nm in names:
        print("    %-10s " % nm
              + " ".join(("PASS" if g in pass_sets[nm] else
                          ".   ") for g in G_RANGE))

    def forces(nm):
        ps = set(pass_sets[nm])
        if (ps & set(range(2, 11))) != {5}:
            return False
        if 1 in ps and math.comb(1, 2) != 0:
            return False        # g=1 must be ALPHABET-EMPTY killable
        return True

    want_sets = {"D1": [1, 5], "D2core": [5], "D2full": [5],
                 "W-COUNT": [1, 5], "W-BIREG": [1, 3, 5, 7, 9],
                 "W-AX1": [1, 3, 5], "W-DUALAX1": [1, 3, 5]}
    check("T3.1 pass-sets == frozen F2: %s"
          % {nm: pass_sets[nm] for nm in names},
          all(pass_sets[nm] == want_sets[nm] for nm in names),
          kill="K3")
    check("T3.2 FORCING: D1 (self-duality), D2core (GQ anti-flag "
          "core) and D2full (full GQ demand) each force g = 5 under "
          "the frozen rule; D2core kills g = 1 INTERNALLY (zero "
          "anti-flags), D1/W-COUNT need the CCXXXI ALPHABET-EMPTY "
          "kill (C(1,2) = 0)",
          forces("D1") and forces("D2core") and forces("D2full")
          and not cols[1]["nondeg"], kill="K3")
    check("T3.3 CONTROLS FIRE (census is sharp): W-BIREG passes at "
          "g in {3,7,9}, W-AX1 and W-DUALAX1 pass at g = 3 -- all "
          "three FAILED-FORCING as demanded; W-COUNT forces (it IS "
          "P-count, reported as such, NOT a failed control)",
          (not forces("W-BIREG")) and (not forces("W-AX1"))
          and (not forces("W-DUALAX1")) and forces("W-COUNT"),
          kill="K3")

    # ==================================================================
    section("T4 -- the doily at g = 5: self-duality is real, "
            "necessarily OUTER (EXTERNAL-CITED)")
    # ==================================================================
    st5 = S[5]
    c5 = cols[5]
    check("T4.1 GQ(2,2) parameters exact: 15 points / 15 lines, "
          "3 duads per matching, each duad in 3 matchings, AX1 "
          "(<= 1 shared), AX2 (= 1), s = t = 2 -- GQ(2,2) is the "
          "unique GQ of this order and is self-dual "
          "[EXTERNAL-CITED Payne-Thas 2009]",
          len(st5["pts"]) == 15 and len(st5["lns"]) == 15
          and set(st5["pt_deg"].values()) == {3}
          and all(len(L) == 3 for L in st5["lns"])
          and c5["ax1"] and c5["ax2"], kill="K4")

    adj5, parts5 = levi_graph(st5["pts"], st5["lns"], st5["linesets"])
    n_pre, pre_maps = graph_maps(adj5, parts5, "pre", collect=True)
    n_swap, swap_maps = graph_maps(adj5, parts5, "swap",
                                   collect=True)
    sigmas = list(itertools.permutations(range(6)))
    pi_of = {}
    for sg in sigmas:
        pi_of[induced_vertex_maps(st5["pts"], st5["lns"],
                                  list(sg))] = sg
    ok_full = (set(pre_maps) == set(pi_of.keys()))
    check("T4.2 correlation census (exact backtracking on the Levi "
          "graph): collineations %d == 720 == the induced S6 maps "
          "AS SETS (faithful and full: %s); dualities %d == 720; "
          "correlation group order %d == 1440 == |Aut(S6)|"
          % (n_pre, ok_full, n_swap, n_pre + n_swap),
          n_pre == 720 and n_swap == 720 and ok_full, kill="K4")

    gens = [induced_vertex_maps(st5["pts"], st5["lns"],
                                [1, 0, 2, 3, 4, 5]),
            induced_vertex_maps(st5["pts"], st5["lns"],
                                [1, 2, 3, 4, 5, 0])]
    n_equiv = 0
    for d in swap_maps:
        if all(tuple(d[p[i]] for i in range(30))
               == tuple(p[d[i]] for i in range(30)) for p in gens):
            n_equiv += 1
    delta = swap_maps[0]
    dinv = [0] * 30
    for i, v in enumerate(delta):
        dinv[v] = i
    pi_t = induced_vertex_maps(st5["pts"], st5["lns"],
                               [1, 0, 2, 3, 4, 5])
    rho = tuple(delta[pi_t[dinv[i]]] for i in range(30))
    tau = pi_of.get(rho)
    cyc = []
    if tau is not None:
        seen = set()
        for a in range(6):
            if a in seen:
                continue
            ln = 0
            b = a
            while b not in seen:
                seen.add(b)
                b = tau[b]
                ln += 1
            cyc.append(ln)
        cyc = sorted(cyc, reverse=True)
    n_pol = sum(1 for d in swap_maps
                if all(d[d[i]] == i for i in range(30)))
    check("T4.3 THE TWIST IS FORCED: %d of 720 dualities commute "
          "with the S6 action (STRICT NATURALITY FAILS AT g = 5, "
          "so D3 pass-set is EMPTY); a duality conjugates the "
          "transposition (0 1) to cycle type %s == [2,2,2] (triple "
          "transposition = the OUTER class [EXTERNAL-CITED "
          "Janusz-Rotman 1982]); [DIAG, unfrozen] polarities: %d"
          % (n_equiv, cyc, n_pol),
          n_equiv == 0 and cyc == [2, 2, 2] and tau is not None,
          kill="K4")

    duad_w = (1 << 4) | (1 << 5)
    line_w = frozenset(((1 << 0) | (1 << 1), (1 << 2) | (1 << 3),
                        (1 << 4) | (1 << 5)))

    def pm6(mask, sg):
        out = 0
        for b in range(6):
            if (mask >> b) & 1:
                out |= (1 << sg[b])
        return out

    stab_d = [sg for sg in sigmas if pm6(duad_w, sg) == duad_w]
    stab_l = [sg for sg in sigmas
              if frozenset(pm6(f, sg) for f in line_w) == line_w]

    def orbit_sizes(stab):
        rem = set(range(6))
        out = []
        while rem:
            a = next(iter(rem))
            orb = {a}
            frontier = {a}
            while frontier:
                nxt = set()
                for x in frontier:
                    for sg in stab:
                        y = sg[x]
                        if y not in orb:
                            orb.add(y)
                            nxt.add(y)
                frontier = nxt
            out.append(len(orb))
            rem -= orb
        return sorted(out)

    os_d, os_l = orbit_sizes(stab_d), orbit_sizes(stab_l)
    check("T4.4 no-natural-correspondence witness: duad stabilizer "
          "|%d| with letter orbits %s, matching stabilizer |%d| "
          "letter orbits %s (transitive) -- equal order, "
          "NON-CONJUGATE (different orbit signatures), so NO "
          "S6-equivariant bijection between the two 15-element "
          "S6-sets exists" % (len(stab_d), os_d, len(stab_l), os_l),
          len(stab_d) == 48 and len(stab_l) == 48
          and os_d == [2, 4] and os_l == [6], kill="K4")

    # ---- equal-counts impostor (must fire)
    imp_lns = [L for L in st5["lns"] if frozenset(L) != line_w]
    fake = tuple(sorted(((1 << 0) | (1 << 1), (1 << 0) | (1 << 2),
                         (1 << 0) | (1 << 3))))
    imp_lns.append(fake)
    imp_sets = [frozenset(L) for L in imp_lns]
    af_bad = sum(1 for f in fake if not (duad_w & f))
    adj_i, parts_i = levi_graph(st5["pts"], imp_lns, imp_sets)
    n_swap_i, _ = graph_maps(adj_i, parts_i, "swap", collect=False,
                             cap=0)
    check("T4.5 CONTROL FIRES: equal-counts impostor (one matching "
          "replaced by the non-matching triple {01,02,03}): counts "
          "%d = %d EQUAL, yet the anti-flag ({4,5}, fake) has "
          "disjointness count %d != 1 (AX2 broken) and the duality "
          "count is %d == 0 -- COUNT EQUALITY DOES NOT IMPLY "
          "STRUCTURE, the structural demands have teeth"
          % (len(st5["pts"]), len(imp_lns), af_bad, n_swap_i),
          len(imp_lns) == 15 and af_bad == 3 and n_swap_i == 0,
          kill="K4")

    # ==================================================================
    section("T5 -- equipotence: the incidence demand vs the CCXXXI "
            "exterior identity")
    # ==================================================================
    fp_exh = sorted(g for g in range(2, 11) if exhaust_ident(g))
    fp_core = sorted(g for g in range(2, 11) if passes(g, "D2core"))
    check("T5.1 EXHAUST-IDENT census rebuilt on g = 2..10: footprint "
          "%s == %s == footprint(D2core) -- the g-free incidence "
          "demand and the exterior one-step identity carve the SAME "
          "class" % (fp_exh, fp_core),
          fp_exh == [5] and fp_core == [5], kill="K5")

    lv = {}
    ok_close = True
    for g in G_RANGE:
        if g % 2 == 0 or not S[g]["disj_pairs"]:
            continue
        st = S[g]
        full = (1 << (g + 1)) - 1
        letter_valued = all(
            bin(full ^ (a | b)).count("1") == 2
            for a, b in st["disj_pairs"])
        lv[g] = letter_valued
        if g == 5:
            lines_set = set(st["linesets"])
            ok_close = all(
                frozenset((a, b, full ^ (a | b))) in lines_set
                for a, b in st["disj_pairs"]) \
                and len(st["disj_pairs"]) == 45
    check("T5.2 LETTER-VALUED COMPOSITION (F4): the complement of a "
          "disjoint duad pair is again a duad on footprint %s == "
          "[5]; at g = 5 all 45 disjoint pairs close with their "
          "complement into a LINE (%s) -- depth-1 self-hosting IS "
          "the line closure of the alphabet; at g = 3 the "
          "complement is empty (composition dies), at g >= 7 it "
          "leaves the alphabet"
          % (sorted(g for g in lv if lv[g]), ok_close),
          sorted(g for g in lv if lv[g]) == [5] and ok_close,
          kill="K5")

    equip = (fp_exh == fp_core == [5]
             and sorted(g for g in lv if lv[g]) == [5])
    check("T5.3 EQUIPOTENCE TYPED (F5): footprint(D2core) == "
          "footprint(EXHAUST-IDENT) == footprint(letter "
          "composition) == {5} -- the self-duality/GQ demand is "
          "EQUIPOTENT with P-depth and (mod the g = 1 kill) with "
          "P-count; the independent-implication test against mu4 / "
          "orientation rules / E8 hull is NOT finitely measurable "
          "here and stays OPEN", equip, kill="K5")

    # ==================================================================
    section("T6 -- THE VERDICT (frozen typed rule)")
    # ==================================================================
    forcing_ok = (forces("D1") and forces("D2core")
                  and forces("D2full"))
    struct_ok = all(ok for name, ok in CHECKS
                    if name.startswith(("T1", "T2", "T4.1", "T4.2",
                                        "T4.3", "T4.4")))
    controls_ok = ((not forces("W-BIREG")) and (not forces("W-AX1"))
                   and (not forces("W-DUALAX1"))
                   and af_bad == 3 and n_swap_i == 0)
    if forcing_ok and struct_ok and controls_ok and equip:
        verdict = "COLLAPSE-G5-REFORMULATION"
    else:
        verdict = "NO-COLLAPSE"
    print("\n  VERDICT: %s" % verdict)
    print("  (COLLAPSE-G5-PRIMITIVE cannot trigger: no independent "
          "compiler implication is measured in this probe.)")
    if verdict == "COLLAPSE-G5-REFORMULATION":
        print("\n  THE COMPOSED P2 THEOREM (every premise typed):")
        print("   (a) quasi-free on the deployed seam"
              "                    [FINITE THEOREM, CCXXXI T1]")
        print("   (b) bilinear generation"
              "                              [FINITE THEOREM, "
              "CCXXXI T2]")
        print("   (P-selfdual) THE ONE POSTULATE, g-free (no 5, no "
              "carrier dim):")
        print("       'the incidence of the data alphabet (duads of "
              "the extended")
        print("        letter space) in the elementary contraction "
              "schemes (perfect")
        print("        matchings) is a NONDEGENERATE GENERALIZED "
              "QUADRANGLE' --")
        print("        sharp core: at least one anti-flag exists and "
              "every anti-flag")
        print("        (e, M) has EXACTLY ONE contraction f in M "
              "disjoint from e")
        print("        (unambiguous routing of unconsumed data)"
              "      [POSTULATE]")
        print("   ==> g_car = 5      [THIS PROBE T3: pass-set {5} on "
              "1..10; T2.1: the")
        print("        anti-flag law count = m-2 makes it an all-g "
              "arithmetic fact]")
        print("   ==> N_fam = (g-2)!! = 3"
              "                   [FINITE THEOREM, CCXXXI T4b/c]")
        print("   and self-duality of the incidence then HOLDS at "
              "the forced g = 5")
        print("   (720 dualities measured; GQ(2,2) self-dual, "
              "EXTERNAL-CITED), but")
        print("   NECESSARILY OUTER: no S6-equivariant duality "
              "exists (T4.3/T4.4) --")
        print("   the compiler's data/operation exchange is a "
              "720-torsor, not a")
        print("   canonical map; the strict-natural categorical "
              "demand D3 is FALSE.")
        print("\n  HONEST TYPING: the demand is EQUIPOTENT with "
              "P-depth/P-count (T5)")
        print("   -- a g-free STRUCTURAL REFORMULATION with "
              "independent meaning")
        print("   (unique routing / self-duality), NOT a strictly "
              "more primitive")
        print("   premise; whether any compiler fact (mu4, "
              "orientation, E8 hull)")
        print("   IMPLIES the demand remains OPEN.")

    # ------------------------------------------------------------ tally
    section("SUMMARY")
    npass = sum(1 for _, ok in CHECKS if ok)
    print("  checks: %d/%d passed; kills: %s"
          % (npass, len(CHECKS), KILLS if KILLS else "none"))
    print("  verdict: %s" % verdict)
    print("  runtime: %.1f s" % (time.time() - T0))
    print("  SPEC_SHA: %s" % SPEC_SHA[:8])
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
