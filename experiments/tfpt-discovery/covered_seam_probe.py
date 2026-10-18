#!/usr/bin/env python3
"""Discovery probe: the covered seam round -- the lattice skeleton of the
covering-level identification: the lifted seam is ONE 48-site NS circle,
the lifted clock has order 12 with L^4 = deck (the lattice avatar of
r^4 = omega), and the deck-character mode grid is the 12-grid with the
untwisted sector equal to the base seam verbatim.  (The named residue of
v622, first executed slice.)

v622 identified the physical seam with the conformal seam at the kernel
and dictionary level; the remaining bedrock residue is the
COVERING-level identification.  This probe builds its lattice skeleton
exactly:

  (V1) CONNECTIVITY CENSUS [E]: lifting the 16-site seam circle to the
       mu3-cover (sheet shift j per mark-bond crossing, marks at
       {0, 4, 8, 12}), the covered seam is ONE 48-site circle for the
       uniform weights j = 1, 2 (total monodromy 4j != 0 mod 3) and
       DISCONNECTS into 3 circles for the trivial weight AND for the
       alternating weights (1,2,1,2) -- a NEW, independent kill of the
       alternating pair (v617/v620 killed it by mark equivalence; seam
       connectivity kills it structurally).

  (V2) THE 48-WALK [E]: the explicit walk closes after exactly 48
       steps (one orbit; the walk covers the base circle three times
       and crosses marks 12 times).

  (V3) THE LIFTED CLOCK [E]: the lift L of the base quarter turn
       (4 base steps with sheet bookkeeping) satisfies L^4 = deck and
       L^12 = id on ALL 48 points, with L^k != id for k in
       {1, 2, 3, 4, 6}: the lifted clock has EXACT ORDER 12 -- the
       zeta_12 spectrum of the Burau rotation (v612/v613) and the
       relation r^4 = omega (v597, transport-derived in v614) are
       LATTICE COMBINATORICS on the covered seam.

  (V4) THE KERNEL IDENTITY AT N = 48 [E]: the v622 NS mode-sum
       identity generalizes verbatim -- the 48-site chiral kernel
       (2/48)/sin(pi d/48) for odd d and 0 for even d equals the NS
       mode sum for ALL d = 1..47 (closed form with M = 24).

  (V5) THE DECK-CHARACTER MODE GRID [E]: the NS modes (m + 1/2)/48
       split under the deck (shift by 16) into THREE classes of 16
       modes with offsets {1/6, 1/2, 5/6} -- the even 12-grid
       {2, 6, 10}/12; the offset-1/2 class equals the BASE NS
       frequencies EXACTLY (the untwisted sector IS the base seam,
       verbatim); the offsets 1/6 and 5/6 form the conjugate twisted
       pair (the t = omega / omega-bar sheets of v613).  The fermionic
       deck lift satisfies deck^3 = -1 on every mode class (the NS
       full rotation -- the spin double; the geometric deck has order
       3 on bilinears, where the products give omega exactly):
       resonates with the v510/v519 (-1)^F dichotomy, typed as
       observation.

  (V6) THE LIFTED MARKS [E]: the walk crosses mark-bonds at exactly 12
       positions and the lifted clock permutes these 12 crossings in a
       SINGLE 12-cycle: the zeta_12 organizes the lifted mark set
       transitively.

  (V7) THE READING [C]: the covering-level identification has its
       lattice skeleton -- connected covered seam, order-12 lifted
       clock with L^4 = deck, the 12-grid mode split with the
       untwisted sector = the base and the twisted pair = the
       conjugate sheets; the remaining residue is the
       interacting/CFT-level orbifold statement (twist-field OPE, the
       full Z3 orbifold of the seam CFT), named, not claimed.
       GATE.QGEO does not move.

Verdict enums (frozen): COVERED-SEAM-SKELETON (all pass),
SKELETON-FAILS, MIXED.

Python-only (sympy + exact combinatorics), counted per GATE.WOLFRAM.02.
"""

from collections import defaultdict

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


N = 16
NC = 48
MARK_BONDS = (0, 4, 8, 12)


def successor(a, s, weights):
    """One base step a -> a+1; crossing bond (a+1) shifts the sheet by
    the mark's weight."""
    a2 = (a + 1) % N
    if a2 in MARK_BONDS:
        s = (s + weights[MARK_BONDS.index(a2)]) % 3
    return a2, s


def components(weights):
    seen = set()
    comps = 0
    for a0 in range(N):
        for s0 in range(3):
            if (a0, s0) in seen:
                continue
            comps += 1
            a, s = a0, s0
            while (a, s) not in seen:
                seen.add((a, s))
                a, s = successor(a, s, weights)
    return comps


# ================================================================== V1
print("=" * 72)
print("V1: the connectivity census")
print("=" * 72)

comp = {"j=1": components((1, 1, 1, 1)), "j=2": components((2, 2, 2, 2)),
        "j=0": components((0, 0, 0, 0)), "alt": components((1, 2, 1, 2))}
check("V1.1 uniform weights give ONE 48-site covered seam (j = 1: %d "
      "component, j = 2: %d); [must-fail] the trivial weight gives 3 "
      "components and the ALTERNATING pair (1,2,1,2) DISCONNECTS the "
      "seam (3 components) -- a new, independent kill of the "
      "alternating weights (total monodromy 6 = 0 mod 3)"
      % (comp["j=1"], comp["j=2"]),
      comp["j=1"] == 1 and comp["j=2"] == 1
      and comp["j=0"] == 3 and comp["alt"] == 3)

# ================================================================== V2
print("=" * 72)
print("V2: the explicit 48-walk")
print("=" * 72)

W = (1, 1, 1, 1)
walk = []
a, s = 0, 0
crossings = []
for i in range(NC):
    walk.append((a, s))
    a2, s2 = successor(a, s, W)
    if s2 != s:
        crossings.append(i)
    a, s = a2, s2
check("V2.1 the walk closes after exactly 48 steps (one orbit), covers "
      "the base three times, and crosses marks exactly 12 times",
      (a, s) == (0, 0) and len(set(walk)) == NC and len(crossings) == 12)

# ================================================================== V3
print("=" * 72)
print("V3: the lifted clock has exact order 12 with L^4 = deck")
print("=" * 72)


def lift_clock(p):
    aa, ss = p
    for _ in range(4):
        aa, ss = successor(aa, ss, W)
    return (aa, ss)


def Lk(p, k):
    for _ in range(k):
        p = lift_clock(p)
    return p


pts = [(aa, ss) for aa in range(N) for ss in range(3)]
L4_deck = all(Lk(p, 4) == (p[0], (p[1] + 1) % 3) for p in pts)
L12_id = all(Lk(p, 12) == p for p in pts)
proper = all(any(Lk(p, k) != p for p in pts) for k in (1, 2, 3, 4, 6))
check("V3.1 L^4 = deck (one base turn = one deck step -- the lattice "
      "avatar of v597's r^4 = omega and v614's boundary-monodromy "
      "transport) and L^12 = id on ALL 48 points, with proper order 12 "
      "(L^k != id for every proper divisor k)", L4_deck and L12_id and proper)

# ================================================================== V4
print("=" * 72)
print("V4: the kernel identity at N = 48")
print("=" * 72)


def c_of(d, n):
    if d % 2 == 0:
        return sp.Integer(0)
    return sp.Rational(2, n) / sp.sin(sp.pi * sp.Rational(d, n))


x = sp.symbols("x")
lhs = sum(sp.sin((2 * j + 1) * x) for j in range(24))
rhs = sp.sin(24 * x) ** 2 / sp.sin(x)
closed_ok = sp.simplify(sp.expand_trig(lhs - rhs).rewrite(sp.exp)) == 0
ns48_ok = True
for d in range(1, NC):
    ms = sp.Rational(2, NC) * sum(sp.sin((2 * j + 1) * sp.pi * d / NC)
                                  for j in range(NC // 2))
    if sp.simplify(ms - c_of(d, NC)) != 0:
        ns48_ok = False
check("V4.1 the v622 NS mode-sum identity generalizes verbatim to the "
      "covered seam: the 48-site chiral kernel equals the NS mode sum "
      "for ALL d = 1..47 (closed form sum_{j<24} sin((2j+1)x) = "
      "sin^2(24x)/sin(x))", closed_ok and ns48_ok)

# ================================================================== V5
print("=" * 72)
print("V5: the deck-character mode grid (the 12-grid)")
print("=" * 72)

classes = defaultdict(list)
for m in range(NC):
    off = sp.Rational(2 * m + 1, 6) % 1  # (m + 1/2)/3 mod 1
    classes[off].append(m)
offs = sorted(classes.keys())
check("V5.1 the NS modes split under the deck into THREE classes of 16 "
      "modes with offsets {1/6, 1/2, 5/6} = the even 12-grid "
      "{2, 6, 10}/12",
      offs == [sp.Rational(1, 6), sp.Rational(1, 2), sp.Rational(5, 6)]
      and all(len(classes[o]) == 16 for o in offs))

base_freqs = {sp.Rational(2 * n + 1, 2 * N) for n in range(N)}
half_class = {sp.Rational(2 * m + 1, 2 * NC)
              for m in classes[sp.Rational(1, 2)]}
check("V5.2 the offset-1/2 class equals the BASE NS frequencies EXACTLY: "
      "the untwisted sector IS the 16-site base seam, verbatim",
      half_class == base_freqs)

# fermionic deck lift: eigenvalue e^{2 pi i (m+1/2)/3}; cube = -1
cube_ok = all(
    sp.simplify(sp.exp(2 * sp.pi * sp.I * sp.Rational(2 * m + 1, 6)) ** 3
                + 1) == 0 for m in [classes[o][0] for o in offs])
# bilinear deck eigenvalues: products of two twisted-mode eigenvalues
w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
e16 = sp.exp(2 * sp.pi * sp.I * sp.Rational(1, 6))
bilinear_omega = sp.simplify(sp.expand_complex(e16 * e16 - w)) == 0
check("V5.3 the fermionic deck lift satisfies deck^3 = -1 on every mode "
      "class (the NS full rotation -- the spin double), and the "
      "BILINEAR deck eigenvalue of the twisted pair is exactly omega "
      "(e^{i pi/3} squared = omega): the geometric deck has order 3 on "
      "the H^1 level, where the t = omega / omega-bar sheets live",
      cube_ok and bilinear_omega)

# ================================================================== V6
print("=" * 72)
print("V6: the lifted marks")
print("=" * 72)

# crossing positions on the 48-walk; the lifted clock advances the walk
# index by 4: it permutes the 12 crossing indices in a single 12-cycle
cross_set = set(crossings)
shifted = {(i + 4) % NC for i in cross_set}
single_cycle = True
i0 = crossings[0]
seen_c = set()
i = i0
for _ in range(12):
    seen_c.add(i)
    i = (i + 4) % NC
check("V6.1 the 12 mark crossings are equally spaced (step 4) on the "
      "48-walk, the lifted clock maps the crossing set to itself, and "
      "it permutes the crossings in a SINGLE 12-cycle: zeta_12 "
      "organizes the lifted mark set transitively",
      shifted == cross_set and seen_c == cross_set and len(seen_c) == 12)

# ================================================================== V7
print("=" * 72)
print("V7: the reading")
print("=" * 72)

check("V7.1 [C] the covering-level identification has its lattice "
      "skeleton: connected 48-site covered seam (uniform weights only), "
      "order-12 lifted clock with L^4 = deck, the 12-grid mode split "
      "with the untwisted sector = the base verbatim and the twisted "
      "pair = the conjugate sheets (t = omega / omega-bar); the "
      "remaining residue is the interacting/CFT-level orbifold "
      "statement (twist-field OPE, the full Z3 orbifold of the seam "
      "CFT), named, not claimed; GATE.QGEO does not move", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: COVERED-SEAM-SKELETON -- the covered seam is one 48-site")
    print("NS circle, the lifted clock has order 12 with L^4 = deck, and the")
    print("deck-character mode grid is the 12-grid with the untwisted sector")
    print("equal to the base seam verbatim.")
else:
    print("SOME CHECKS FAILED")
