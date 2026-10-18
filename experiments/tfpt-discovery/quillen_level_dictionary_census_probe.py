#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""quillen_level_dictionary_census_probe -- ALPHA.QUILLEN.LEVEL.CENSUS.01
(EXPLORATION ONLY).

HARDNESS TEST on the PREVIOUS round (ALPHA.QUILLEN.RAMIFIED.LEVEL.01,
verdict QUILLEN-RAMIFIED-LEVEL).  That round derived the Maxwell level
k0 = 1 as

    L(m)  =  n_marks * h(order_m)  =  4 * (1/4)   at depth m >= 3,

with h(k) = 0 for k <= 1 and 1/k otherwise.  The rule "h = 1/order"
was a SET dictionary, not a measured one.  The RP-NSR round already
taught us that a coarse predicate can be FAMILY-BLIND (every side
satisfied it, so it selected nothing).  This probe asks the same
question of the level dictionary, BEFORE anything is promoted:

    how many predeclared dictionaries reproduce k0 = 1, and how many
    reproduce the full corpus tuple (0, 2, 1, 1)?

FROZEN GRID (declared before the count; NOT tuned to the answer).
  Counts A (corpus-native integers only): 1, 2 (|Z2|), 3 (channels),
  4 (2 chi = |mu4|), 5 (g_car), 6 (|R+(A3)|), 8 (rank E8), 15
  (nonzero classes), 16 (|V|), 41 (M), 48 (Omega_adm), 240 (roots).
  Fraction rules f(k) on the clock order k:
    f_recip      0 if k<=1 else 1/k          [the rule used last round]
    f_recip_all  1/k                          (no depth-1 collapse)
    f_compl      0 if k<=1 else (k-1)/k
    f_half       0 if k<=1 else 1/2
    f_two_over   0 if k<=1 else 2/k
    f_k_over_8   k/8
    f_recip_sq   0 if k<=1 else 1/k^2
    f_log        0 if k<=1 else log2(k)/4
    f_pow2       0 if k<=1 else 1/2^(k/2)
    f_kminus1_4  (k-1)/4
  Level map: L(m) = A * f(order_m), order tuple (1,2,4,4).

DEMANDS (this probe is allowed to REFUTE its predecessor's rhetoric):
  U1  DOMAIN LIMITATION.  The order tuple takes only THREE distinct
      values {1,2,4}.  Any two rules agreeing at k in {1,2,4} are
      indistinguishable here.  Demand: exhibit at least one pair of
      DIFFERENT rule expressions that agree on the domain.  If so,
      "the reciprocal-order rule is uniquely selected" is DEAD.
  U2  COARSE CENSUS (dictionary-blindness).  Count the grid pairs with
      L(depth>=3) = 1.  Demand: MORE THAN ONE (the coarse demand does
      not select a dictionary).
  U3  SHARP CENSUS.  Count the grid pairs with the full tuple
      (0, 2, 1, 1).  Report the count, and demand that EVERY sharp
      survivor realises the SAME level map k -> 4/k on the domain:
      the MAP is determined, the factorisation into count x fraction
      is NOT.
  U4  THE FACTORISATION-FREE INVARIANT.  Independent of A and f:
          chi / k0  =  2 / 1  =  2  =  ord(m>=3) / ord(m=2)  =  4 / 2.
      The metric level (gravity, chi) and the gauge level (Maxwell)
      stand in the ratio of the two clock orders.  No count, no
      fraction rule, no dictionary enters.  THIS is what survives.
  U5  THE KILL STILL HOLDS (exact, no root-finding): k0 = 2 gives
      F_2(a*) = a*^3 != 0 at the [E] Quillen split.
  U6  HONEST DOWNGRADE, recorded: what the predecessor established is
      (U4) + (U5), NOT a unique holonomy dictionary.  The phrase
      "k0 = 1 derived" must be read as "k0 = 1 is forced RELATIVE TO
      chi = 2 by the order ratio", not as a dictionary-free theorem.

CONTROLS:
  C1  a scrambled fraction rule (seed 20260819) does NOT reproduce the
      sharp tuple for any A in the grid.
  C2  a hypothetical chi = 3 seam gives ratio 3 != 2 -- the invariant
      is contentful, not an identity.
  C3  the order tuple is (1,2,4,4), rebuilt from the Hjelmslev ring.

KILLS: K1 the sharp census is EMPTY (the predecessor's tuple is not
reachable at all); K2 the sharp survivors realise DIFFERENT maps
(then even the map is undetermined); K3 the ratio invariant fails;
K4 a control fires.

VERDICT ENUM:
  LEVEL-RATIO-SURVIVES-DICT-BLIND  U1-U6: coarse demand blind, sharp
                                   demand fixes the MAP only, and the
                                   surviving content is the order-ratio
                                   invariant plus the kill.
  LEVEL-DICTIONARY-UNIQUE          U1 fails (rules ARE distinguishable)
                                   and exactly one sharp survivor.
  LEVEL-CENSUS-DEAD                K1 or K2 or K3.
  CONTROL-VOID                     a control fails.

FIREWALL: experiments/tfpt-discovery only; no verification/ import; no
ledger/paper/website; no .md; no RH; no marker move.  Exact Fraction /
sympy.  AST-ban verification, zeta, numpy, mpmath.  Do not import
sibling probes.  ALPHA.QUILLEN.EXACT.01 stays [O].

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/quillen_level_dictionary_census_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import time
from fractions import Fraction

import sympy as sp

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
ALPHA.QUILLEN.LEVEL.CENSUS.01 FROZEN SPEC (2026-08-19).
Grid A in {1,2,3,4,5,6,8,15,16,41,48,240}; 10 predeclared fraction
rules on the clock order; L(m)=A*f(order_m), orders (1,2,4,4).
U1 domain has 3 distinct orders -> rules agreeing there are
indistinguishable; 'reciprocal rule uniquely selected' DEAD.
U2 coarse census L(>=3)=1 has MORE THAN ONE survivor (blind).
U3 sharp census (0,2,1,1): report count; all survivors realise the
SAME map k->4/k (map determined, factorisation not).
U4 factorisation-free invariant chi/k0 = 2 = ord(m>=3)/ord(m=2).
U5 kill: k0=2 => F_2(a*)=a*^3 != 0 at the [E] split.
U6 honest downgrade: surviving content = U4 + U5, not a unique dict.
C1 scrambled rule fails. C2 chi=3 gives ratio 3. C3 orders (1,2,4,4).
ALPHA.QUILLEN.EXACT.01 stays [O]. No marker move.
Verdict: RATIO-SURVIVES-DICT-BLIND / DICTIONARY-UNIQUE / DEAD / VOID.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

COUNTS = (1, 2, 3, 4, 5, 6, 8, 15, 16, 41, 48, 240)
CHI = 2
K0_CORPUS = 1
SHARP_TUPLE = (Fraction(0), Fraction(2), Fraction(1), Fraction(1))


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0))


def ast_firewall(src: str) -> list[str]:
    banned = {"verification", "zeta", "zetazero", "numpy", "mpmath"}
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


def build_ring(m: int):
    size = 1 << m
    dec = []
    for code in range(size):
        a = b = 0
        pa, pb = 1, 0
        for j in range(m):
            if (code >> j) & 1:
                a += pa
                b += pb
            pa, pb = pa - pb, pa + pb
        dec.append((a, b))

    def enc(a, b):
        code = 0
        aa, bb = int(a), int(b)
        for _j in range(m):
            d = (aa + bb) & 1
            if d:
                code |= 1 << _j
                aa -= 1
            aa, bb = (aa + bb) // 2, (bb - aa) // 2
        return code

    mul = [[enc(dec[x][0] * dec[y][0] - dec[x][1] * dec[y][1],
                dec[x][0] * dec[y][1] + dec[x][1] * dec[y][0])
            for y in range(size)] for x in range(size)]
    return dict(size=size, enc=enc, mul=mul)


def order_of_i(m: int) -> int:
    R = build_ring(m)
    code = R["enc"](0, 1)
    one = R["enc"](1, 0)
    acc = one
    for k in range(1, R["size"] + 2):
        acc = R["mul"][acc][code]
        if acc == one:
            return k
    return 0


def f_recip(k):
    return Fraction(0) if k <= 1 else Fraction(1, k)


def f_recip_all(k):
    return Fraction(1, k)


def f_compl(k):
    return Fraction(0) if k <= 1 else Fraction(k - 1, k)


def f_half(k):
    return Fraction(0) if k <= 1 else Fraction(1, 2)


def f_two_over(k):
    return Fraction(0) if k <= 1 else Fraction(2, k)


def f_k_over_8(k):
    return Fraction(k, 8)


def f_recip_sq(k):
    return Fraction(0) if k <= 1 else Fraction(1, k * k)


def f_log(k):
    return Fraction(0) if k <= 1 else Fraction(k.bit_length() - 1, 4)


def f_pow2(k):
    return Fraction(0) if k <= 1 else Fraction(1, 1 << (k // 2))


def f_kminus1_4(k):
    return Fraction(k - 1, 4)


RULES = (
    ("f_recip", f_recip),
    ("f_recip_all", f_recip_all),
    ("f_compl", f_compl),
    ("f_half", f_half),
    ("f_two_over", f_two_over),
    ("f_k_over_8", f_k_over_8),
    ("f_recip_sq", f_recip_sq),
    ("f_log", f_log),
    ("f_pow2", f_pow2),
    ("f_kminus1_4", f_kminus1_4),
)


def lcg_fracs(seed: int, ks) -> dict:
    x = seed
    out = {}
    for k in ks:
        x = (1103515245 * x + 12345) & 0x7FFFFFFF
        out[k] = Fraction(1 + (x % 7), 8)
    return out


def main() -> int:
    print("ALPHA.QUILLEN.LEVEL.CENSUS.01 -- is the level dictionary "
          "unique, or family-blind?")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("C3 clock orders rebuilt")
    orders = tuple(order_of_i(m) for m in (1, 2, 3, 4))
    check("C3 order(i in R_m) = (1,2,4,4) rebuilt from the Hjelmslev ring",
          orders == (1, 2, 4, 4), "orders=%s" % (orders,))
    domain = sorted(set(orders))

    section("U1 domain limitation (only 3 distinct orders)")
    agree_pairs = []
    for i in range(len(RULES)):
        for j in range(i + 1, len(RULES)):
            n1, r1 = RULES[i]
            n2, r2 = RULES[j]
            if all(r1(k) == r2(k) for k in domain):
                agree_pairs.append((n1, n2))
    check("U1 the order tuple takes only 3 distinct values %s, and at "
          "least one pair of DIFFERENT rule expressions agrees on that "
          "domain -- 'reciprocal-order is uniquely selected' is DEAD"
          % (domain,),
          len(domain) == 3 and len(agree_pairs) >= 1,
          "agreeing pairs=%s" % (agree_pairs,))

    section("U2 coarse census: how many dictionaries give k0 = 1?")
    coarse = []
    for a in COUNTS:
        for name, rule in RULES:
            if a * rule(orders[2]) == Fraction(K0_CORPUS):
                coarse.append((a, name))
    check("U2 the coarse demand L(depth>=3) = 1 is DICTIONARY-BLIND: "
          "%d of %d grid pairs satisfy it"
          % (len(coarse), len(COUNTS) * len(RULES)),
          len(coarse) > 1,
          "survivors=%s" % (coarse,))

    section("U3 sharp census: the full corpus tuple (0,2,1,1)")
    sharp = []
    for a in COUNTS:
        for name, rule in RULES:
            tup = tuple(a * rule(k) for k in orders)
            if tup == SHARP_TUPLE:
                sharp.append((a, name))
    maps = set()
    for a, name in sharp:
        rule = dict(RULES)[name]
        maps.add(tuple(a * rule(k) for k in domain))
    check("U3a the sharp tuple (0,2,1,1) is reachable and NARROWS the "
          "grid: %d survivors (vs %d coarse)" % (len(sharp), len(coarse)),
          len(sharp) >= 1 and len(sharp) < len(coarse),
          "survivors=%s" % (sharp,))
    expected_map = tuple(Fraction(4, k) if k > 1 else Fraction(0)
                         for k in domain)
    check("U3b EVERY sharp survivor realises the SAME level map "
          "k -> 4/k on the domain -- the MAP is determined, the "
          "factorisation count x fraction is NOT",
          len(maps) == 1 and maps == {expected_map},
          "maps=%s" % (sorted(maps),))

    section("U4 the factorisation-free invariant")
    ratio_corpus = Fraction(CHI, K0_CORPUS)
    ratio_clock = Fraction(orders[2], orders[1])
    check("U4 chi / k0 = %s = ord(m>=3) / ord(m=2) = %s -- no count, "
          "no fraction rule, no dictionary enters"
          % (ratio_corpus, ratio_clock),
          ratio_corpus == ratio_clock == 2)

    section("U5 the kill (exact, no root-finding)")
    a = sp.symbols("a", positive=True)
    s = sp.symbols("S", positive=True)
    f2_on_root = sp.simplify((2 * a ** 3 - s).subs(s, a ** 3))
    check("U5 k0 = 2 gives F_2(a*) = a*^3 != 0 at the [E] Quillen "
          "split -- stationarity dies; the kill is dictionary-free",
          f2_on_root == a ** 3
          and sp.simplify((a ** 3 - s).subs(s, a ** 3)) == 0)

    section("U6 honest downgrade recorded")
    check("U6 surviving content = the order-ratio invariant (U4) + the "
          "kill (U5); NOT a unique holonomy dictionary (U1/U2/U3b). "
          "'k0 = 1 derived' reads as 'k0 = 1 forced RELATIVE TO "
          "chi = 2 by the clock-order ratio'",
          len(agree_pairs) >= 1 and len(coarse) > 1 and len(maps) == 1)

    section("controls")
    scr = lcg_fracs(20260819, domain)
    scr_hits = [a for a in COUNTS
                if tuple(a * (Fraction(0) if k <= 1 else scr[k])
                         for k in orders) == SHARP_TUPLE]
    check("C1 scrambled fraction rule (seed 20260819) reproduces the "
          "sharp tuple for NO count in the grid",
          not scr_hits,
          "scr=%s hits=%s" % ({k: str(v) for k, v in scr.items()},
                              scr_hits))
    check("C2 a hypothetical chi = 3 seam would give ratio 3 != 2 -- "
          "the invariant is contentful, not an identity",
          Fraction(3, K0_CORPUS) != ratio_clock)

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref):
        hits = [(n, ok) for n, ok in CHECKS if n.startswith(pref)]
        return bool(hits) and all(ok for _, ok in hits)

    c_ok = pfx("C1") and pfx("C2") and pfx("C3") and pfx("G0")
    u_ok = all(pfx("U%d" % k) for k in range(1, 7))
    if not c_ok:
        verdict = "CONTROL-VOID"
    elif not (pfx("U3") and pfx("U4")):
        verdict = "LEVEL-CENSUS-DEAD"
    elif u_ok:
        verdict = "LEVEL-RATIO-SURVIVES-DICT-BLIND"
    else:
        verdict = "LEVEL-CENSUS-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("CENSUS: coarse survivors %d, sharp survivors %d, distinct "
          "sharp maps %d." % (len(coarse), len(sharp), len(maps)))
    print("DOWNGRADE OF THE PREVIOUS ROUND (recorded honestly): the "
          "holonomy dictionary is NOT unique (only 3 clock orders; "
          "several rule expressions coincide).  What survives is "
          "chi/k0 = ord(m>=3)/ord(m=2) = 2 plus the exact kill of "
          "k0 = 2.  ALPHA.QUILLEN.EXACT.01 UNTOUCHED [O].  "
          "NO MARKER MOVE.  NO RH CLAIM.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot
                 and verdict == "LEVEL-RATIO-SURVIVES-DICT-BLIND") else 1


if __name__ == "__main__":
    raise SystemExit(main())
