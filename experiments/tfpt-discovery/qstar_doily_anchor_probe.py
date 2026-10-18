#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""qstar_doily_anchor_probe -- CFIN.QSTAR.NORMALFORM.01 +
DOILY.ANCHOR.LOCAL.01 + DOILY.HODGE.FACTOR.01 +
P2.QUADRATIC.EXHAUSTION.01 (+ FLAVOR.ANCHOR.VIETA report)
(EXPLORATION ONLY, experiments/; round 38, the four finite theorems of
the 2026-08-09 external review, 2026-08-09).

WHY NEW (duplicate check done against the corpus): v845 has the q*
SELECTOR (brute-force census 16 -> 4 -> 2 -> 1) and the ovoid-line
incidence (S5.5); v844 has the doily rank theorem and the message
ladder with anchor a = (1,1,2); v857/flavor_feedback has the winding
identity chi_L - chi_R = -6(t^2 - 5t + 2).  NOT in the corpus: the
CLOSED BOOLEAN NORMAL FORM of q*, the per-line ANCHOR-MULTISET law
with the secant/external census, the Lambda^2 x Lambda^2 -> Lambda^4
multiplication-table reading of the doily, and the one-step quadratic
exhaustion theorem forcing g_car = 5.  This probe freezes exactly
those four statements plus the anchor-notation Vieta rewrite.

FROZEN CLAIMS (2026-08-09, frozen + SHA-hashed before first run):

 S1  CFIN.QSTAR.NORMALFORM.01 -- the closed formula.  On V = F_2^4 in
     the family/anchor basis (F1, F2, F3, A) with the bit form of
     Gram J - I (v845 S1):
       (a) the distinguished refinement q* (frozen v845 selector:
           sigma-invariant -> q(A) = 1 -> q(F_Sigma) = 0, unique)
           EQUALS the closed boolean normal form
             q*(x) = sum_{i<j} x_i x_j + sum_i x_i  (mod 2);
       (b) equivalently q*(x) = C(w+1, 2) mod 2 with w = |x| the
           Hamming weight -- q* is WEIGHT-ONLY with the value table
           (w=0..4) -> (0, 1, 1, 0, 0);
       (c) zeros = {0000} u {0111, 1011, 1101, 1110, 1111} (the five
           ovoid messages, weights 3 and 4); the other TEN messages
           (weights 1 and 2) have q* = 1;
       (d) DERIVATION WITHOUT CENSUS: the 16 refinements of the bit
           form are EXACTLY q_c(x) = sum_{i<j} x_i x_j + c.x over the
           16 linear parts c in F_2^4 (polar-form theorem); the
           selector chain acts on c as: sigma-invariance <=> c1 = c2
           = c3 (4 survive) -> q(A) = 1 <=> c4 = 1 (2 survive) ->
           q(F_Sigma) = 0 <=> c1 = 1 (1 survives) => c = (1,1,1,1) is
           FORCED -- the closed formula replaces the 2^16 search;
       (e) sigma split: the five ovoid messages fall as 5 = 1 + 1 + 3
           (fixed F_Sigma = 1110 and F_Sigma + A = 1111, one free
           3-orbit) and the ten pair messages as 10 = 1 + 3 + 3 + 3
           (fixed A = 0001, three free 3-orbits) -- the 9 = N_fam^2
           non-fixed pair messages are literally three family cycles.

 S2  DOILY.ANCHOR.LOCAL.01 -- every doily line carries the anchor.
     With the local weight w(v) := 2 - q*(v) and the frozen anchor
     a = (1, 1, 2) (v832 [E]):
       (a) EVERY of the 15 isotropic lines of PG(3,2) has q*-pattern
           {0, 1, 1} (one ovoid + two pair points; v845 S5.5 rebuilt)
           and hence weight-MULTISET {2, 1, 1} = the anchor multiset;
       (b) the per-line characteristic polynomial is
           prod_{v in ell}(t - w(v)) = (t-2)(t-1)^2
           = t^3 - 4 t^2 + 5 t - 2, i.e. the elementary symmetric
           values (e1, e2, e3) = (4, 5, 2) = (e1, e2, e3)(a), with
           e2 = g_car and e3 = |Z2|;
       (c) EXCLUSIVITY CENSUS: the 20 non-isotropic lines split as
           EXACTLY 10 secants (pattern {0, 0, 1}, weight multiset
           {2, 2, 1} = the WRONG anchor (1, 2, 2)) + 10 external
           lines (pattern {1, 1, 1}) -- the anchor law holds on ALL
           doily lines and on NO other line of PG(3,2);
       (d) incidence budget: sum over doily lines of ovoid incidences
           = 15 = M_0 and of pair incidences = 30 = M_1 = h(E8) --
           the first doubling rung of MESSAGE.LADDER.01 (v844) is
           already contained in the doily incidence (counting
           statement ONLY; no canonical bijection claimed).

 S3  DOILY.HODGE.FACTOR.01 -- the doily is the multiplication table
     Lambda^2 E x Lambda^2 E -> Lambda^4 E of the five-slot carrier.
     Via the v845 parity lift iota: V -> C_even(5) map the ten pair
     messages (iota-weight 2, support {j,k}) to b_jk = e_j ^ e_k and
     the five ovoid messages (iota-weight 4, support = comp{i}) to
     f_i = e_1 ^ ... ^ e-hat_i ^ ... ^ e_5:
       (a) on EVERY isotropic line the three iota-supports partition
           {1..5} as {i} u {j,k} u {l,m};
       (b) exact integer exterior algebra: b_jk ^ b_lm = +-f_i on
           every line;
       (c) the map line -> (i; {j,k}, {l,m}) is a BIJECTION onto all
           5 x 3 = 15 such configurations (three perfect matchings of
           the four remaining indices per carrier slot i);
       (d) converse/multiplication reading: on the 10 external lines
           (three pair points, pairwise overlapping supports) ALL
           pairwise wedges vanish; secants carry <= 1 pair point (no
           Lambda^2 x Lambda^2 product) -- the wedge product is
           NONZERO exactly on the doily lines.

 S4  P2.QUADRATIC.EXHAUSTION.01 -- the algebraic half of the g_car
     forcing.  For E of odd dimension g and S+ = Lambda^even E:
       (a) at g = 5: Lambda^2 E ^ Lambda^2 E SPANS Lambda^4 E (exact
           integer rank 5 = C(5,4)) and dim S+ = 1 + 10 + 5 = 16;
       (b) the ONE-STEP demand deg(Lambda^2 ^ Lambda^2) = 4 = g - 1
           forces g = 5 among odd g in {3, 5, 7, 9, 11}: for g = 3
           the product lands in Lambda^4 = 0, for g >= 7 it misses
           the top sector Lambda^{g-1} by degree -- g_car = 5 is the
           unique odd rank with quadratic one-step exhaustion;
       (c) HONEST TYPING (no upgrade): the algebraic theorem is
           exact; the PHYSICAL premise (the Calderon boundary kernel
           exhausts the nontrivial half-spinor in one quadratic
           step) is [O] -- P2 stays narrowed to v799's R1' (v845 S8),
           NOT eliminated.

 S5  FLAVOR.ANCHOR.VIETA (report-level rewrite, corpus identities in
     anchor notation; no new claim):
       (a) power sum p_2(a) = 6, elementary symmetric (4, 5, 2);
       (b) chi_L - chi_R = -p_2(a) (t^2 - e2(a) t + e3(a)) with the
           v4 residue matrix R = [[1,3,0],[1,5,2],[2,5,3]] and
           L = R + 6 1 e1^T (v857 q_wind = t^2 - g_car t + |Z2|
           rewritten: e2(a) = g_car, e3(a) = |Z2|);
       (c) ladder rewrite M_n = 15 (1, e3, e1, e1 e3, e1^2)
           = (15, 30, 60, 120, 240);
       (d) doily Vieta: the point-line incidence N of the 15
           isotropic lines has charpoly(N N^T) = (x-9)(x-4)^9 x^5,
           rank N = C(e2, 2) = 10, dim ker N = e2 = 5 (v844 rank
           theorem rebuilt in the bit model).

 C   CONTROLS (must fire):
     C1 the wrong anchor (1, 2, 2): its multiset does NOT match any
        isotropic line -- it matches the 10 SECANT lines instead
        (Vieta (5, 8, 4)); the ladder 15 (1, e3, e1, ...) misses
        (30, 60, 120, 240).
     C2 an Arf-0 refinement q' (10 zeros, hyperbolic): the line
        pattern census over the 15 isotropic lines is NOT constant
        {0, 1, 1} (hyperbolic quadrics meet lines in 1 or 3 points).
     C3 the wrong lift iota' = (f1, f2, f3, a, 0): the supports do
        not partition {1..5} on some doily line (checksum slot is
        load-bearing for the Hodge reading).
     C4 even control g = 4: Lambda^2 ^ Lambda^2 = Lambda^4 is the TOP
        sector Lambda^g, not Lambda^{g-1} -- the odd/half-spinor
        demand is load-bearing.

KILLS (any one fires => typed gap):
  K1 closed formula / weight form / derivation breaks -> QSTAR-FORM-BROKEN
  K2 an isotropic line misses the anchor multiset     -> ANCHOR-LOCAL-BROKEN
  K3 exclusivity census (10 + 10) breaks              -> LINE-CENSUS-BROKEN
  K4 wedge factorization / bijection breaks           -> HODGE-FACTOR-BROKEN
  K5 exhaustion rank / uniqueness breaks              -> EXHAUSTION-BROKEN
  K6 a Vieta/ladder identity breaks                   -> VIETA-BROKEN
  K7 a control does not fire                          -> CONTROL-DEAD

VERDICT (frozen enum): FINITE-ANCHOR-CLOSED / <typed gap above> /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface.
Exact integer/sympy arithmetic; no floats, no RNG, no fit.  NO marker
moves; S4(c) states its own [O] typing.

Sources (read-only, machinery rebuilt inline): verification/
v845_cfin_normal_form.py (bit form, selector, iota, ovoid), v844
(rank theorem, message ladder, anchor), v832 (anchor a = (1,1,2)),
v4_flavor_matrix + v857 (R, winding quadratic), tfpt_constants
(N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qstar_doily_anchor_probe.py
"""

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
    print(title)
    print("=" * 74, flush=True)


# ---------------------------------------------------------------- setup
GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)
ANCHOR = (1, 1, 2)                      # v832 [E]
Z2 = 2


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


def refinements_of(form):
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            vi = W16[i]
            for j in range(16):
                vj = W16[j]
                vs = tuple((a + b) % 2 for a, b in zip(vi, vj))
                if q[WIDX[vs]] ^ q[i] ^ q[j] != form(vi, vj):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


def qform_closed(x):
    return (sum(x[i] * x[j] for i in range(4) for j in range(i + 1, 4))
            + sum(x)) % 2


def elem_sym(vals):
    a, b, c = vals
    return (a + b + c, a * b + a * c + b * c, a * b * c)


def main():
    print("CFIN.QSTAR.NORMALFORM.01 + DOILY.ANCHOR.LOCAL.01 + "
          "DOILY.HODGE.FACTOR.01 + P2.QUADRATIC.EXHAUSTION.01")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO RH claim; no marker moves; exploration only.")

    # ==================================================================
    section("S1 -- CFIN.QSTAR.NORMALFORM.01: the closed boolean form")
    # ==================================================================
    refs = refinements_of(hb)
    siginv = [q for q in refs
              if all(q[WIDX[sig_bits(w)]] == q[WIDX[w]] for w in W16)]
    cand_a = [q for q in siginv if q[WIDX[A_BIT]] == 1]
    cand = [q for q in cand_a if q[WIDX[FSIG]] == 0]
    sel_ok = (len(refs) == 16 and len(siginv) == 4
              and len(cand_a) == 2 and len(cand) == 1)
    QSTAR = cand[0]
    check("S1.0 selector rebuilt (v845): 16 refinements -> 4 -> 2 -> 1",
          sel_ok, kill="K1")

    closed = tuple(qform_closed(w) for w in W16)
    check("S1.1(a) q*(x) == sum_{i<j} x_i x_j + sum_i x_i on ALL 16 "
          "words", closed == QSTAR, kill="K1")

    wt_form = tuple(((sum(w) + 1) * sum(w) // 2) % 2 for w in W16)
    wt_table = {}
    for w in W16:
        wt_table.setdefault(sum(w), set()).add(QSTAR[WIDX[w]])
    weight_only = all(len(s) == 1 for s in wt_table.values())
    vals = tuple(sorted(wt_table[k])[0] for k in range(5))
    check("S1.1(b) q*(x) == C(w+1,2) mod 2; WEIGHT-ONLY with table "
          "(w=0..4) -> %s == (0,1,1,0,0)" % (vals,),
          wt_form == QSTAR and weight_only
          and vals == (0, 1, 1, 0, 0), kill="K1")

    five = sorted(w for w in W16 if any(w) and QSTAR[WIDX[w]] == 0)
    ten = sorted(w for w in W16 if QSTAR[WIDX[w]] == 1)
    want_five = sorted([(0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1),
                        (1, 1, 1, 0), (1, 1, 1, 1)])
    check("S1.1(c) zeros = {0} u the FIVE ovoid messages (weights 3, "
          "4): %s; the TEN pair messages have weights 1, 2"
          % ("/".join("".join(map(str, w)) for w in five)),
          five == want_five and len(ten) == 10
          and all(sum(w) in (3, 4) for w in five)
          and all(sum(w) in (1, 2) for w in ten), kill="K1")

    # (d) derivation without census
    cand16 = []
    for c in W16:
        q = tuple((sum(w[i] * w[j] for i in range(4)
                       for j in range(i + 1, 4))
                   + sum(a * b for a, b in zip(c, w))) % 2 for w in W16)
        cand16.append((c, q))
    all_are_refs = sorted(q for _c, q in cand16) == sorted(refs)
    surv_sig = [c for c, q in cand16 if c[0] == c[1] == c[2]]
    surv_a = [c for c in surv_sig if c[3] == 1]
    surv_f = [c for c in surv_a if c[0] == 1]
    forced = (len(surv_sig) == 4 and len(surv_a) == 2
              and len(surv_f) == 1 and surv_f[0] == (1, 1, 1, 1))
    check("S1.1(d) DERIVATION: the 16 refinements ARE the 16 linear "
          "shifts q_c of the polar quadratic; selector on c: "
          "c1=c2=c3 (4) -> c4=1 (2) -> c1=1 (1) => c = (1,1,1,1) "
          "FORCED -- no 2^16 search needed",
          all_are_refs and forced, kill="K1")

    orb5 = set()
    for w in five:
        orb5.add(frozenset({w, sig_bits(w), sig_bits(sig_bits(w))}))
    orb10 = set()
    for w in ten:
        orb10.add(frozenset({w, sig_bits(w), sig_bits(sig_bits(w))}))
    sz5 = sorted(len(o) for o in orb5)
    sz10 = sorted(len(o) for o in orb10)
    check("S1.1(e) sigma split: five = 1 + 1 + 3 (orbits %s), ten = "
          "1 + 3 + 3 + 3 (orbits %s); 9 = N_fam^2 = %d non-fixed "
          "pair messages" % (sz5, sz10, N_fam ** 2),
          sz5 == [1, 1, 3] and sz10 == [1, 3, 3, 3]
          and 3 * 3 == N_fam ** 2, kill="K1")

    # ==================================================================
    section("S2 -- DOILY.ANCHOR.LOCAL.01: every line carries (1,1,2)")
    # ==================================================================
    NZ = [w for w in W16 if any(w)]
    lines_pg = set()
    for a2, b2 in itertools.combinations(NZ, 2):
        c2 = tuple((x + y) % 2 for x, y in zip(a2, b2))
        lines_pg.add(frozenset({a2, b2, c2}))
    iso = [L for L in lines_pg
           if all(hb(u, w) == 0 for u in L for w in L)]
    noniso = [L for L in lines_pg if L not in set(iso)]
    check("S2.0 PG(3,2): 35 lines, 15 isotropic (the doily), 20 other",
          len(lines_pg) == 35 and len(iso) == 15 and len(noniso) == 20,
          kill="K2")

    anchor_ms = sorted(ANCHOR)
    ok_pat = ok_ms = ok_poly = True
    for L in iso:
        qs = sorted(QSTAR[WIDX[v]] for v in L)
        ws = sorted(2 - QSTAR[WIDX[v]] for v in L)
        ok_pat &= (qs == [0, 1, 1])
        ok_ms &= (ws == anchor_ms)
        ok_poly &= (elem_sym(ws) == (4, 5, 2))
    check("S2.1(a) EVERY doily line: q*-pattern {0,1,1}, weight "
          "multiset {2,1,1} == the anchor multiset {1,1,2}",
          ok_pat and ok_ms, kill="K2")
    t = sp.symbols("t")
    chi = sp.expand((t - 2) * (t - 1) ** 2)
    check("S2.1(b) per-line charpoly (t-2)(t-1)^2 = %s; (e1,e2,e3) = "
          "(4,5,2) == elem. sym. of a = (1,1,2); e2 = g_car = %d, "
          "e3 = |Z2| = %d" % (chi, g_car, Z2),
          ok_poly and chi == t ** 3 - 4 * t ** 2 + 5 * t - 2
          and elem_sym(ANCHOR) == (4, 5, 2)
          and elem_sym(ANCHOR)[1] == g_car
          and elem_sym(ANCHOR)[2] == Z2, kill="K2")

    sec_lines = [L for L in noniso
                 if sorted(QSTAR[WIDX[v]] for v in L) == [0, 0, 1]]
    ext_lines = [L for L in noniso
                 if sorted(QSTAR[WIDX[v]] for v in L) == [1, 1, 1]]
    check("S2.1(c) EXCLUSIVITY: the 20 non-isotropic lines = 10 "
          "secants (pattern {0,0,1}) + 10 external (pattern {1,1,1}) "
          "-- got %d + %d; the anchor law holds on NO non-doily line"
          % (len(sec_lines), len(ext_lines)),
          len(sec_lines) == 10 and len(ext_lines) == 10
          and len(sec_lines) + len(ext_lines) == 20, kill="K3")

    n_car = sum(1 for L in iso for v in L if QSTAR[WIDX[v]] == 0)
    n_tra = sum(1 for L in iso for v in L if QSTAR[WIDX[v]] == 1)
    check("S2.1(d) incidence budget: 15 x 1 = %d = M_0 carrier "
          "incidences, 15 x 2 = %d = M_1 = h(E8) transport "
          "incidences -- the first ladder doubling is IN the doily "
          "(counting only, no bijection claimed)" % (n_car, n_tra),
          n_car == 15 and n_tra == 30, kill="K6")

    # ==================================================================
    section("S3 -- DOILY.HODGE.FACTOR.01: Lambda^2 ^ Lambda^2 = doily")
    # ==================================================================
    def iota(v):
        return (v[0], v[1], v[2], v[3],
                (v[0] + v[1] + v[2] + v[3]) % 2)

    def support(v):
        return frozenset(k + 1 for k, b in enumerate(iota(v)) if b)

    def wedge_sign(pair1, pair2):
        seq = sorted(pair1) + sorted(pair2)
        if len(set(seq)) != 4:
            return None                       # overlapping -> zero
        inv = sum(1 for i in range(4) for j in range(i + 1, 4)
                  if seq[i] > seq[j])
        return -1 if inv % 2 else 1

    ok_part = ok_wedge = True
    fact_per_i = {i: [] for i in range(1, 6)}
    for L in iso:
        ov = [v for v in L if QSTAR[WIDX[v]] == 0]
        pr = [v for v in L if QSTAR[WIDX[v]] == 1]
        if len(ov) != 1 or len(pr) != 2:
            ok_part = False
            continue
        S, T = support(pr[0]), support(pr[1])
        comp = support(ov[0])
        i_slot = (frozenset(range(1, 6)) - comp)
        ok_part &= (len(S) == 2 and len(T) == 2 and not (S & T)
                    and (S | T) == comp and len(i_slot) == 1)
        sgn = wedge_sign(S, T)
        ok_wedge &= (sgn in (1, -1))
        if len(i_slot) == 1:
            fact_per_i[next(iter(i_slot))].append(
                (frozenset({S, T}), sgn))
    check("S3.1(a) support partition {i} u {j,k} u {l,m} = {1..5} on "
          "EVERY doily line", ok_part, kill="K4")
    check("S3.2(b) b_jk ^ b_lm = +-f_i EXACT (integer exterior "
          "algebra) on every line; sign census %s"
          % sorted(sum(1 for _m, s in v if s == 1)
                   for v in fact_per_i.values()),
          ok_wedge, kill="K4")
    n_fact = [len({m for m, _s in fact_per_i[i]}) for i in range(1, 6)]
    all_cfg = set()
    for i in range(1, 6):
        rest = sorted(set(range(1, 6)) - {i})
        a_, b_, c_, d_ = rest
        for m in ([{a_, b_}, {c_, d_}], [{a_, c_}, {b_, d_}],
                  [{a_, d_}, {b_, c_}]):
            all_cfg.add((i, frozenset(frozenset(x) for x in m)))
    got_cfg = {(next(iter(frozenset(range(1, 6))
                          - frozenset().union(*m))), m)
               for i in range(1, 6) for m, _s in fact_per_i[i]}
    check("S3.3(c) BIJECTION: factorizations per carrier slot = %s "
          "== [3]*5 (the three perfect matchings); 5 x 3 = 15 = all "
          "configurations realized" % n_fact,
          n_fact == [3] * 5 and len(all_cfg) == 15
          and got_cfg == all_cfg, kill="K4")

    ok_ext_zero = True
    for L in ext_lines:
        prs = [support(v) for v in L]
        for S, T in itertools.combinations(prs, 2):
            ok_ext_zero &= (wedge_sign(S, T) is None)
    n_sec_pairs = sum(1 for L in sec_lines
                      if sum(1 for v in L if QSTAR[WIDX[v]] == 1) <= 1)
    check("S3.4(d) CONVERSE: all pairwise wedges VANISH on the 10 "
          "external lines (overlapping supports); all 10 secants "
          "carry <= 1 pair point -- the product is nonzero EXACTLY "
          "on the doily lines", ok_ext_zero and n_sec_pairs == 10,
          kill="K4")

    # ==================================================================
    section("S4 -- P2.QUADRATIC.EXHAUSTION.01: one step forces g = 5")
    # ==================================================================
    def lam_wedge_rank(g):
        """integer rank of Lambda^2 ^ Lambda^2 inside Lambda^4(F^g).

        Every product b_S ^ b_T with S, T disjoint pairs equals
        +- ONE standard basis 4-form e_{S u T}; the rank is therefore
        exactly the number of DISTINCT supports S u T reached (each
        row of the product matrix is +- a standard basis vector)."""
        four = list(itertools.combinations(range(1, g + 1), 4))
        supports = set()
        for S in itertools.combinations(range(1, g + 1), 2):
            for T in itertools.combinations(range(1, g + 1), 2):
                if set(S) & set(T):
                    continue
                supports.add(tuple(sorted(S + T)))
        return len(supports), len(four)

    rk5, dim45 = lam_wedge_rank(5)
    dims = (1, 10, 5)
    check("S4.1(a) g = 5: rank(Lambda^2 ^ Lambda^2) = %d == dim "
          "Lambda^4 = %d (SPANS); S+ dims (1, 10, 5), total 16"
          % (rk5, dim45),
          rk5 == dim45 == 5 and dims == (1, 10, 5)
          and sum(dims) == 16, kill="K5")

    uniq = []
    for g in (3, 5, 7, 9, 11):
        rk, d4 = lam_wedge_rank(g)
        top = g - 1
        one_step = (4 == top) and (rk == d4)
        uniq.append((g, one_step))
    check("S4.2(b) UNIQUENESS over odd g in {3,5,7,9,11}: one-step "
          "demand holds %s -- only g = 5"
          % ["g=%d:%s" % (g, o) for g, o in uniq],
          [g for g, o in uniq if o] == [5], kill="K5")
    check("S4.3(c) HONEST TYPING: the algebraic theorem is exact; "
          "the quadratic one-step Calderon exhaustion premise stays "
          "[O]; P2 narrowed to v799 R1', NOT eliminated (v845 S8)",
          True, "typed, no upgrade")

    # ==================================================================
    section("S5 -- FLAVOR.ANCHOR.VIETA: the corpus in anchor notation")
    # ==================================================================
    p2 = sum(x * x for x in ANCHOR)
    e1, e2, e3 = elem_sym(ANCHOR)
    check("S5.1(a) p2(a) = %d == 6; (e1,e2,e3) = (%d,%d,%d)"
          % (p2, e1, e2, e3),
          p2 == 6 and (e1, e2, e3) == (4, 5, 2), kill="K6")

    R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
    L_mat = R + 6 * sp.Matrix([1, 1, 1]) * sp.Matrix([[1, 0, 0]])
    chiR = R.charpoly(t).as_expr()
    chiL = L_mat.charpoly(t).as_expr()
    rhs = sp.expand(-p2 * (t ** 2 - e2 * t + e3))
    check("S5.2(b) chi_L - chi_R = %s == -p2(a)(t^2 - e2 t + e3) "
          "(v857 winding quadratic in anchor notation)"
          % sp.expand(chiL - chiR),
          sp.expand(chiL - chiR - rhs) == 0, kill="K6")

    ladder = tuple(15 * m for m in (1, e3, e1, e1 * e3, e1 ** 2))
    check("S5.3(c) M_n = 15 (1, e3, e1, e1 e3, e1^2) = %s == "
          "(15, 30, 60, 120, 240)" % (ladder,),
          ladder == (15, 30, 60, 120, 240), kill="K6")

    Nmat = sp.Matrix(15, 15, lambda i, j: 1 if NZ[i] in iso[j] else 0)
    x = sp.symbols("x")
    cp = sp.factor((Nmat * Nmat.T).charpoly(x).as_expr())
    want_cp = sp.expand((x - 9) * (x - 4) ** 9 * x ** 5)
    check("S5.4(d) doily Vieta: charpoly(N N^T) = %s == "
          "(x-9)(x-4)^9 x^5; rank N = %d == C(e2,2) = 10; "
          "dim ker = %d == e2 = 5"
          % (cp, Nmat.rank(), 15 - Nmat.rank()),
          sp.expand(cp - want_cp) == 0 and Nmat.rank() == 10
          and 15 - Nmat.rank() == e2, kill="K6")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    wrong = (1, 2, 2)
    wms = sorted(wrong)
    n_match_iso = sum(1 for L in iso
                      if sorted(2 - QSTAR[WIDX[v]] for v in L) == wms)
    n_match_sec = sum(1 for L in sec_lines
                      if sorted(2 - QSTAR[WIDX[v]] for v in L) == wms)
    wrong_ladder = tuple(15 * m for m in (
        1, elem_sym(wrong)[2], elem_sym(wrong)[0],
        elem_sym(wrong)[0] * elem_sym(wrong)[2],
        elem_sym(wrong)[0] ** 2))
    check("C1 FIRES: wrong anchor (1,2,2): matches %d == 0 doily "
          "lines but ALL %d == 10 secants (Vieta (5,8,4)); its "
          "ladder %s misses every rung past 15"
          % (n_match_iso, n_match_sec, (wrong_ladder,)),
          n_match_iso == 0 and n_match_sec == 10
          and elem_sym(wrong) == (5, 8, 4)
          and all(wrong_ladder[k] != (15, 30, 60, 120, 240)[k]
                  for k in range(1, 5)), kill="K7")

    arf0 = [q for q in refs
            if sum(1 for i in range(16) if q[i] == 0) == 10]
    q0 = arf0[0]
    pats = {tuple(sorted(q0[WIDX[v]] for v in L)) for L in iso}
    check("C2 FIRES: Arf-0 refinement: doily line patterns %s are "
          "NOT constant {0,1,1} -- the ovoid (Arf-1, sigma-selected) "
          "is load-bearing" % sorted(pats),
          pats != {(0, 1, 1)} and len(pats) >= 2, kill="K7")

    def support_bad(v):
        return frozenset(k + 1 for k, b in enumerate(
            (v[0], v[1], v[2], v[3], 0)) if b)

    ok_bad_breaks = False
    for L in iso:
        sups = sorted((len(support_bad(v)) for v in L))
        parts = [support_bad(v) for v in L]
        union = frozenset().union(*parts)
        if union != frozenset(range(1, 6)) or sups.count(2) != 2:
            ok_bad_breaks = True
            break
    check("C3 FIRES: wrong lift iota' (checksum slot dropped): the "
          "support partition of {1..5} breaks on a doily line",
          ok_bad_breaks, kill="K7")

    rk4, d44 = lam_wedge_rank(4)
    check("C4 FIRES: even control g = 4: Lambda^2 ^ Lambda^2 fills "
          "Lambda^4 = the TOP sector Lambda^g (rank %d == dim %d "
          "== 1), not Lambda^{g-1} -- the odd half-spinor demand is "
          "load-bearing" % (rk4, d44),
          rk4 == d44 == 1 and 4 != 4 - 1, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = {"K1": "QSTAR-FORM-BROKEN",
                   "K2": "ANCHOR-LOCAL-BROKEN",
                   "K3": "LINE-CENSUS-BROKEN",
                   "K4": "HODGE-FACTOR-BROKEN",
                   "K5": "EXHAUSTION-BROKEN",
                   "K6": "VIETA-BROKEN"}.get(KILLS[0], "CONTROL-DEAD")
    else:
        VERDICT = "FINITE-ANCHOR-CLOSED"
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
PROMOTION-READY STATEMENTS (report only -- no promotion, no edits):
  * q*(x) = sum_{i<j} x_i x_j + sum_i x_i = C(|x|+1,2) mod 2 -- the
    census-free closed form of the v845 selector (weight-only).
  * EVERY doily line carries the anchor as its local weight multiset
    {2,1,1} = {a}; secants carry the wrong anchor (1,2,2); external
    lines (1,1,1) -- the anchor law is EXCLUSIVE to the doily.
  * The doily IS the multiplication table Lambda^2 E x Lambda^2 E ->
    Lambda^4 E of the five-slot carrier (15 = 5 x 3 factorizations;
    wedge nonzero EXACTLY on doily lines).
  * One-step quadratic exhaustion forces g_car = 5 (algebraic half
    exact; the Calderon premise stays [O] -- P2 not eliminated).
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot) else 1


if __name__ == "__main__":
    raise SystemExit(main())
