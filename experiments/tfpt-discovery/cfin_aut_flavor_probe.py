#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cfin_aut_flavor_probe -- CFIN.AUT.FLAVOR.C6.01 (round 44, from
section 8 of the 2026-08-09 external review of Revision 555): does the
C6 automorphism group of the unique finite compiler GENERATE the flavor
hexagon transport?

WHY NEW (redundancy check against the corpus FIRST): v849
(CFIN.UNIQUE.01) proves |Aut(C_fin)| = 6 with element orders
[1,2,3,3,6,6], abelian, cyclic ~= C6, faithful into Sp(4,2) -- but it
never FACTORS the generator (g^2 =? the family 3-cycle, g^3 =? a sheet
parity), never computes the induced action on the 10 pair-messages,
and never touches flavor.  v808 (CARRIER.PETERSEN.RADIAL.01) proves
the flavor hexagon IS the distance-2 shell of the Petersen graph on
E(K5) with the explicit deployed cycle (f1w1, f2w2, f3w1, f1w2, f2w1,
f3w2) -- but its symmetry bookkeeping is Aut(Petersen) = S5, never
Aut(C_fin).  v54/v56/v82/v124 freeze the recovery value (2/3)^6 =
lambda_2 of the transfer spectrum {1, (2/3)^6, (1/3)^6} with the
exponent 6 identified as p2 = |R+(A3)| = the hexagon size -- never as
|Aut(C_fin)|.  NOT in the corpus: the factorization of the C6
generator, its Lambda^2 E cycle structure, the intertwiner against the
deployed hexagon transport, and the orbit reading of the recovery
exponent.  This probe freezes exactly those four questions.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
exact integer / Fraction arithmetic only):

 A1  CONSTRUCT Aut(C_fin).  From the deployed compiler data on
     V = F_2^4 (bit form hbar of Gram J - I; q* = the v845/v880
     selector-pinned Arf-1 refinement, closed form
     q*(x) = sum_{i<j} x_i x_j + sum_i x_i; sigma = the family
     3-cycle (x1,x2,x3,x4) -> (x3,x1,x2,x4); iota = the parity lift
     V -> C_even(5)): enumerate Sp(4,2) exhaustively (ward: order
     720), and compute Aut(C_fin) = { g in Sp(4,2) : q* o g = q*,
     g sigma = sigma g, and SOME pi in S_5 intertwines iota o g =
     pi o iota } exactly.  WARD against the corpus claim (v849):
     |Aut| = 6, element orders [1,2,3,3,6,6], abelian, cyclic, the
     slot permutation pi determined by g.  FROZEN GENERATOR PIN: g =
     the unique order-6 element with g^2 = sigma (the deployed
     3-cycle, not its inverse); if no order-6 element squares to
     sigma, take the lex-min order-6 element and TYPE the deviation.
     Print g as a 4x4 F_2 matrix (columns = images of e_1..e_4) and
     its slot permutation pi_g.

 A2  FACTORIZATION.  Verify exactly: ord(g^2) = 3, ord(g^3) = 2,
     g^2 g^3 = g^3 g^2, and <g^2> x <g^3> = Aut (the C3 x C2
     splitting).  TYPED: (a) does g^2 EQUAL the deployed family
     3-cycle sigma (permutation equality on all 16 classes)?
     (b) SHEET HONESTY: the corpus deploys NO sheet-involution
     operator ON V (v118's sheet twist -1 acts on the 3-dim family
     monodromy; v857 I1: the lattice maps J and -1 both induce the
     IDENTITY on V) -- so the honest factor test is: which corpus
     operator does g^3 match?  Frozen candidate: the W-edge swap --
     pi_{g^3} = the transposition (w1 w2) fixing the three F slots
     pointwise, i.e. the S2 factor of Stab_{S5}(W) = S3 x S2 (v808
     P1.5), with |W| = 2 = |Z2| the sheet count.  Measured either
     way (fixed-space dimension of g^3 on V printed).

 A3  THE LAMBDA^2 ACTION.  The 10 pair-messages = the {q* = 1} words
     of V; via the v880 parity lift their iota-supports are EXACTLY
     E(K5) (ward: bijection; charge census {-4: 3, +1: 6, +6: 1}
     under X5 = (-2,-2,-2,3,3), v808 P1).  Rebuild the deployed
     hexagon (v808 P2, read-only machinery rebuilt inline): Petersen
     adjacency = disjointness, distance shells around W = {w1,w2}
     of sizes (1, 3, 6), charge-pure, and the deployed transport
     cycle HEX = ({f1,w1},{f2,w2},{f3,w1},{f1,w2},{f2,w1},{f3,w2})
     edge-verified.  Then MEASURE: (a) the cycle type of g on the 10
     pair-messages (predicted 1 + 3 + 6) and whether the g-orbits
     EQUAL the three charge shells; (b) THE INTERTWINER: the g-orbit
     sequence s_n = g^n({f1,w1}), n = 0..5, vs the deployed cycle --
     INTERTWINED iff every g-step is an edge of the deployed hexagon
     AND the cyclic sequence equals HEX up to rotation + reflection
     (the D6 convention of the flavor transport theorem, tfpt_2
     Lemma dd: residue triples are fixed 'up to D6'); the matching
     dihedral element is printed (orientation typed honestly: the
     TWO C6 generators traverse the hexagon in opposite directions).
     PARTIAL iff only the cycle type (1, 3, 6) matches; DEAD if
     neither.  The corpus quotient is the RESTRICTION to the 6-orbit
     (= the distance-2 shell): the flavor sector's C6 acts on the 6
     residue sites Z_6 (word length L = 6n + r, residue sets = the
     D6-orbit of {0,1,3}), deployed as exactly this hexagon (v808
     [E neu], tfpt_2 round-22 note).

 A4  THE ORBIT READING (report, no fit, no marker move).  If A2/A3
     hold: 6 = |Aut(C_fin)| = the length of the full automorphism
     orbit on the hexagon; the chain
         lambda_rec = (|Z2| / N_fam)^{|Aut(C_fin)|} = (2/3)^6
                    = 64/729
     against the DEPLOYED frozen recovery value = the subleading
     transfer eigenvalue lambda_1 = (1 - 1/3)^6 (v124 lambda_n =
     (1 - n/3)^6; v54/v56 frozen spectrum; v82 Koide multiplier) --
     exact Fraction equality.  HONEST TYPING: the corpus derives the
     exponent 6 as p2 = |R+(A3)| = the hexagon size; '6 =
     |Aut(C_fin)|' is a NEW reading made consistent by A3 (the
     hexagon is one full Aut orbit); the first-generation winding +6
     (L = R + 6 1 e1^T, v4/v857) = one full revolution = one full
     Aut orbit is a report line, not a claim upgrade.

 C   CONTROLS (must fire; frozen fire rules):
     C1 NON-AUTOMORPHISM: among ALL 600 symplectic maps p that
        preserve hbar but NOT q* (ward: |Sp| - |Stab(q*)| =
        720 - 120), COUNT those factoring consistently as g^2/g^3
        (p^2 in {sigma, sigma^2} AND p^3 = the Aut involution):
        must be 0 (any such p = p^3 (p^2)^{-1} would lie in Aut,
        contradiction -- verified by census, not narrated); the
        lex-min example p with its square/cube diagnostics printed.
     C2 SCRAMBLED TRANSPORT TABLE: swapping two entries of the
        deployed cycle (positions 1 and 2) must BREAK A3: the
        scrambled table is NOT D6-equivalent to the g-sequence AND
        contains a non-edge step (fire iff both).

KILLS (any one fires => typed):
  K1 machinery ward breaks (Sp order, refinement census, selector,
     iota, E(K5) bijection, Petersen shells, deployed cycle)
                                                -> PIPELINE-BROKEN
  K2 corpus Aut claim breaks (|Aut| != 6, not cyclic, orders wrong,
     pi not determined, sigma not in Aut)       -> PIPELINE-BROKEN
  K3 a control does not fire                    -> CONTROL-DEAD

VERDICT (frozen enum, decision order):
  0. a control does not fire      -> CONTROL-DEAD, exit 1
  1. any kill                     -> PIPELINE-BROKEN, exit 1
  2. otherwise                    -> C6FLAVOR-MEASURED + <INTERTWINED
     iff A2(a) g^2 = family 3-cycle (sigma or sigma^{-1}, typed)
     AND A2(b) pi_{g^3} = the W-edge swap AND A3 orbits = shells AND
     the intertwiner matches up to D6 with every step an edge;
     PARTIAL iff only the cycle type (1,3,6) matches; DEAD if
     neither> -- an honest DEAD is a fine outcome (the review calls
     this a hypothesis, not a claim).

RUN NOTE (fail-first preserved, no spec amendment): run 1 aborted at
A1.3 with a pure %%-formatting TypeError in a report string (a bare
tuple passed to %%s); the fix wraps the argument -- NO frozen claim,
check, kill, control or fire rule was altered (SPEC stays v1).

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  Exact integer / Fraction arithmetic in
every decision; no floats, no RNG, no fits.  AST firewall: banned
identifiers zetazero / nzeros / primerange / isprime / primepi /
nextprime / prevprime (self-scan).  NO physics claim beyond the typed
reading, NO RH claim, no marker moves.  Runtime cap 600 s.

Sources (read-only, machinery rebuilt inline): verification/
v849_cfin_unique_cofinal_lean.py (Aut(C_fin) ~= C6, admissibility
conventions), v880_finite_anchor_theorems.py (q* closed form, parity
lift, pair/ovoid split), v808_petersen_sixthroot.py (K5 edge machine,
X5, deployed hexagon cycle, Stab_{S5}(W) = S3 x S2), v845 (selector),
v54/v56/v82/v124 (frozen transfer spectrum {1, (2/3)^6, (1/3)^6},
lambda_n = (1 - n/3)^6, p2 = 6), v4/v857 (winding L = R + 6 1 e1^T),
tfpt_2_standard_model.tex (flavor transport theorem, distance set
{0,1,3} up to D6), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cfin_aut_flavor_probe.py
"""
import ast
import hashlib
import itertools
import os
import sys
import time
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


# ------------------------------------------------------- bit machinery
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
GJI = ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0))
BASIS = [WIDX[tuple(1 if k == i else 0 for k in range(4))]
         for i in range(4)]
ADD = [[WIDX[tuple((a + b) % 2 for a, b in zip(W16[i], W16[j]))]
        for j in range(16)] for i in range(16)]
IDENT = tuple(range(16))
A_BIT, FSIG = (0, 0, 0, 1), (1, 1, 1, 0)
LA, LF = WIDX[A_BIT], WIDX[FSIG]
SIGP = tuple(WIDX[(w[2], w[0], w[1], w[3])] for w in W16)

HB = [[sum(W16[i][r] * GJI[r][c] * W16[j][c] for r in range(4)
           for c in range(4)) % 2 for j in range(16)]
      for i in range(16)]

IOTA = [tuple(list(w) + [sum(w) % 2]) for w in W16]
S5 = list(itertools.permutations(range(5)))


def perm_of_images(g1, g2, g3, g4):
    gs = (g1, g2, g3, g4)
    p = []
    for i in range(16):
        acc = 0
        for k in range(4):
            if W16[i][k]:
                acc = ADD[acc][gs[k]]
        p.append(acc)
    return tuple(p)


def compose(p, q):
    """(p o q)[i] = p[q[i]]."""
    return tuple(p[q[i]] for i in range(16))


def perm_order(p):
    o, pp = 1, p
    while pp != tuple(range(len(p))):
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def gmat(p):
    """4x4 F_2 matrix of the linear map p (columns = images of e_j)."""
    return [[W16[p[BASIS[j]]][i] for j in range(4)] for i in range(4)]


def fmt_mat(m):
    return " / ".join("".join(str(x) for x in row) for row in m)


def cyc_variants(seq):
    """all 12 D6 images (rotations + rotations of the reversal)."""
    out = set()
    n = len(seq)
    for base in (list(seq), list(reversed(seq))):
        for r in range(n):
            out.add(tuple(base[r:] + base[:r]))
    return out


def main():
    print("CFIN.AUT.FLAVOR.C6.01 -- Aut(C_fin) ~= C6 vs the flavor "
          "hexagon transport")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO RH claim; no marker moves; exploration only.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles: %s)"
          % (BANNED_IDS,), not ast_scan(BANNED_IDS))
    Z2 = g_car - N_fam
    check("S0.2 constants: N_fam = %d, g_car = %d, |Z2| = g_car - "
          "N_fam = %d" % (N_fam, g_car, Z2),
          N_fam == 3 and g_car == 5 and Z2 == 2, kill="K1")

    # ==================================================================
    section("A1 -- Aut(C_fin) from the deployed compiler data")
    # ==================================================================
    GL_n = 0
    SP = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = perm_of_images(*imgs)
        if len(set(p)) != 16:
            continue
        GL_n += 1
        if all(HB[p[BASIS[i]]][p[BASIS[j]]] == GJI[i][j]
               for i in range(4) for j in range(i + 1, 4)):
            SP.append(p)
    check("A1.1 ward: |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == 720 "
          "(exhaustive image enumeration, v849 U0)" % (GL_n, len(SP)),
          GL_n == 20160 and len(SP) == 720, kill="K1")

    # 16 refinements = the 16 linear shifts of the polar quadric (v880)
    refs = []
    for c in W16:
        q = tuple((sum(w[i] * w[j] for i in range(4)
                       for j in range(i + 1, 4))
                   + sum(a * b for a, b in zip(c, w))) % 2 for w in W16)
        refs.append((c, q))
    all_ref = all(all(q[ADD[i][j]] ^ q[i] ^ q[j] == HB[i][j]
                      for i in range(16) for j in range(16))
                  for _c, q in refs)
    siginv = [(c, q) for c, q in refs
              if all(q[SIGP[i]] == q[i] for i in range(16))]
    cand_a = [(c, q) for c, q in siginv if q[LA] == 1]
    cand = [(c, q) for c, q in cand_a if q[LF] == 0]
    QSTAR = cand[0][1] if len(cand) == 1 else None
    closed = tuple((sum(w[i] * w[j] for i in range(4)
                        for j in range(i + 1, 4)) + sum(w)) % 2
                   for w in W16)
    check("A1.2 ward: the 16 polar shifts are ALL refinements of hbar; "
          "selector 16 -> %d -> %d -> %d == 1 pins q* = the closed "
          "form C(|x|+1,2) mod 2 (v845/v880)"
          % (len(siginv), len(cand_a), len(cand)),
          all_ref and len(siginv) == 4 and len(cand_a) == 2
          and len(cand) == 1 and QSTAR == closed, kill="K1")

    sig_ok = (perm_order(SIGP) == 3 and SIGP in SP
              and all(QSTAR[SIGP[i]] == QSTAR[i] for i in range(16))
              and sum(1 for i in range(1, 16) if SIGP[i] == i) == 3)
    pi_sig = [pi for pi in S5
              if all(IOTA[SIGP[i]] == tuple(IOTA[i][pi[s]]
                                            for s in range(5))
                     for i in range(16))]
    check("A1.3 ward: sigma admissible (order 3, symplectic, "
          "q*-preserving, 3 nonzero fixed classes) and iota-"
          "equivariant with slot permutation pi_sigma = %s (v849 U2/U3)"
          % ((pi_sig[0] if len(pi_sig) == 1 else pi_sig),),
          sig_ok and len(pi_sig) == 1, kill="K1")

    # ---- the Aut census
    AUT = []
    for p in SP:
        if any(QSTAR[p[i]] != QSTAR[i] for i in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5
               if all(IOTA[p[i]] == tuple(IOTA[i][pi[s]]
                                          for s in range(5))
                      for i in range(16))]
        if pis:
            AUT.append((p, pis))
    orders = sorted(perm_order(p) for p, _ in AUT)
    one_pi = all(len(pis) == 1 for _p, pis in AUT)
    abelian = all(compose(p1, p2) == compose(p2, p1)
                  for (p1, _), (p2, _) in
                  itertools.combinations(AUT, 2))
    cyclic = bool(AUT) and max(orders) == len(AUT)
    check("A1.4 CORPUS WARD (v849 U5): |Aut(C_fin)| = %d == 6; element "
          "orders %s == [1,2,3,3,6,6]; abelian = %s; cyclic = %s => "
          "C6; slot permutation pi DETERMINED by g (one pi per g: %s)"
          % (len(AUT), orders, abelian, cyclic, one_pi),
          len(AUT) == 6 and orders == [1, 2, 3, 3, 6, 6]
          and abelian and cyclic and one_pi, kill="K2")

    SIGP2 = compose(SIGP, SIGP)
    o3 = sorted(p for p, _ in AUT if perm_order(p) == 3)
    check("A1.5 the C3 part of Aut IS the deployed family cycle: "
          "order-3 elements = {sigma, sigma^2} exactly (sigma in Aut)",
          o3 == sorted([SIGP, SIGP2]), kill="K2")

    g_cands = sorted(p for p, _ in AUT if perm_order(p) == 6)
    g_pin = [p for p in g_cands if compose(p, p) == SIGP]
    pinned = (len(g_pin) == 1)
    G = g_pin[0] if pinned else (g_cands[0] if g_cands else None)
    PI_G = next(pis[0] for p, pis in AUT if p == G)
    check("A1.6 FROZEN GENERATOR PIN: %d order-6 elements; exactly ONE "
          "with g^2 = sigma (the deployed 3-cycle, not its inverse): "
          "%s -- g frozen" % (len(g_cands), pinned),
          len(g_cands) == 2 and pinned, kill="K2")
    print("      g as 4x4 F_2 matrix (rows; columns = g(e_1..e_4)): %s"
          % fmt_mat(gmat(G)))
    print("      g as class permutation: %s" % (G,))
    print("      slot permutation pi_g = %s  (convention: "
          "iota(g v)_s = iota(v)_{pi[s]})" % (PI_G,))

    # ==================================================================
    section("A2 -- factorization: g^2, g^3, the C2 x C3 splitting")
    # ==================================================================
    G2 = compose(G, G)
    G3 = compose(G2, G)
    split = sorted(compose(a, b) for a in (IDENT, G2, compose(G2, G2))
                   for b in (IDENT, G3))
    check("A2.1 ord(g^2) = %d == 3; ord(g^3) = %d == 2; g^2 g^3 = "
          "g^3 g^2; <g^2> x <g^3> = Aut (the C2 x C3 splitting, all 6 "
          "elements reproduced)"
          % (perm_order(G2), perm_order(G3)),
          perm_order(G2) == 3 and perm_order(G3) == 2
          and compose(G2, G3) == compose(G3, G2)
          and split == sorted(p for p, _ in AUT), kill="K2")

    is_sig = (G2 == SIGP)
    is_sig_inv = (G2 == SIGP2)
    check("A2.2 TYPED (a): g^2 == the deployed family 3-cycle sigma: "
          "%s (== sigma^{-1}: %s) -- the review's g^2 = sigma_family "
          "%s, exactly as deployed"
          % (is_sig, is_sig_inv,
             "HOLDS" if is_sig else
             ("holds up to orientation" if is_sig_inv else "FAILS")),
          True, "measured, typed either way")

    PI_G3 = tuple(PI_G[PI_G[PI_G[s]]] for s in range(5))
    w_swap = (0, 1, 2, 4, 3)
    fix_g3 = sum(1 for i in range(16) if G3[i] == i)
    is_wswap = (PI_G3 == w_swap)
    check("A2.3 TYPED (b) SHEET HONESTY: the corpus deploys NO sheet "
          "involution ON V (v118 twist lives on the 3-dim monodromy; "
          "v857 I1: J and -1 induce the identity on V); the measured "
          "factor: pi_{g^3} = %s %s the W-edge swap (w1 w2) fixing F "
          "pointwise = the S2 factor of Stab_{S5}(W) = S3 x S2 (v808 "
          "P1.5), |W| = 2 = |Z2|; fix(g^3 on V) = %d classes (dim %d)"
          % (PI_G3, "==" if is_wswap else "!=", fix_g3,
             fix_g3.bit_length() - 1),
          True, "measured, typed either way")
    print("      g^3 as 4x4 F_2 matrix: %s" % fmt_mat(gmat(G3)))
    print("      g^2 as class permutation: %s" % (G2,))
    print("      g^3 as class permutation: %s" % (G3,))

    # ==================================================================
    section("A3 -- the Lambda^2 action and the hexagon intertwiner")
    # ==================================================================
    TEN = [i for i in range(1, 16) if QSTAR[i] == 1]
    supp = {i: frozenset(s for s in range(5) if IOTA[i][s])
            for i in TEN}
    PAIRS = [frozenset(p) for p in itertools.combinations(range(5), 2)]
    bij = (len(TEN) == 10 and all(len(supp[i]) == 2 for i in TEN)
           and sorted(supp.values(), key=sorted) ==
           sorted(PAIRS, key=sorted))
    X5 = (-2, -2, -2, 3, 3)
    from collections import Counter
    cen = Counter(sum(X5[s] for s in P) for P in PAIRS)
    check("A3.1 ward: the 10 pair-messages {q* = 1} biject via iota-"
          "support onto E(K5); charge census %s == {-4: 3, +1: 6, "
          "+6: 1} = the SU(5) decuple (v808 P1)"
          % dict(sorted(cen.items())),
          bij and dict(cen) == {-4: 3, 1: 6, 6: 1}, kill="K1")

    # Petersen + shells around W (v808 P2 rebuilt read-only)
    W_V = frozenset({3, 4})

    def adj(a, b):
        return a != b and not (a & b)

    dist = {W_V: 0}
    frontier = [W_V]
    while frontier:
        nxt = []
        for u in frontier:
            for v2 in PAIRS:
                if adj(u, v2) and v2 not in dist:
                    dist[v2] = dist[u] + 1
                    nxt.append(v2)
        frontier = nxt
    shells = {d: sorted((P for P in PAIRS if dist[P] == d), key=sorted)
              for d in set(dist.values())}
    sizes = tuple(len(shells[d]) for d in sorted(shells))
    pure = {d: {sum(X5[s] for s in P) for P in shells[d]}
            for d in shells}
    HEX = [frozenset(s) for s in
           ({0, 3}, {1, 4}, {2, 3}, {0, 4}, {1, 3}, {2, 4})]
    hex_edges = all(adj(HEX[k], HEX[(k + 1) % 6]) for k in range(6))
    check("A3.2 ward: distance shells around W sizes %s == (1, 3, 6), "
          "charge-pure (%s); the DEPLOYED transport cycle (f1w1, f2w2, "
          "f3w1, f1w2, f2w1, f3w2) is edge-verified (v808 P2.5/P2.6)"
          % (sizes, {d: sorted(pure[d]) for d in sorted(pure)}),
          sizes == (1, 3, 6) and pure[0] == {6} and pure[1] == {-4}
          and pure[2] == {1} and hex_edges
          and sorted(HEX, key=sorted) == sorted(shells[2], key=sorted),
          kill="K1")

    # the g action on the pair-messages (direct word action, no pi)
    p2w = {supp[i]: i for i in TEN}

    def gpair(P, perm=G):
        return supp[perm[p2w[P]]]

    orbits = []
    seen = set()
    for P in PAIRS:
        if P in seen:
            continue
        orb = [P]
        cur = gpair(P)
        while cur != P:
            orb.append(cur)
            cur = gpair(cur)
        seen |= set(orb)
        orbits.append(orb)
    ctype = sorted(len(o) for o in orbits)
    orb_by_len = {len(o): o for o in orbits}
    orbits_are_shells = (
        ctype == [1, 3, 6]
        and orb_by_len[1][0] == W_V
        and sorted(orb_by_len[3], key=sorted) == shells[1]
        and sorted(orb_by_len[6], key=sorted) == shells[2])
    check("A3.3 TYPED: cycle type of g on the 10 pair-messages = %s "
          "(predicted 1 + 3 + 6); g-orbits == the charge shells "
          "(fixed = W = the message A; 3-orbit = distance-1 = u^c; "
          "6-orbit = distance-2 = the hexagon = Q): %s"
          % (ctype, orbits_are_shells),
          True, "measured, typed either way")
    for o in orbits:
        print("      orbit (len %d): %s"
              % (len(o), [tuple(sorted(P)) for P in o]))

    base = frozenset({0, 3})
    seq = [base]
    for _ in range(5):
        seq.append(gpair(seq[-1]))
    period6 = (gpair(seq[-1]) == base and len(set(seq)) == 6)
    steps_edges = all(adj(seq[k], seq[(k + 1) % 6]) for k in range(6))
    hexedges = {frozenset({tuple(sorted(HEX[k])),
                           tuple(sorted(HEX[(k + 1) % 6]))})
                for k in range(6)}
    steps_deployed = all(
        frozenset({tuple(sorted(seq[k])),
                   tuple(sorted(seq[(k + 1) % 6]))}) in hexedges
        for k in range(6))
    hex_t = [tuple(sorted(P)) for P in HEX]
    variants = cyc_variants(hex_t)
    rotations = {tuple(hex_t[r:] + hex_t[:r]) for r in range(6)}
    gtuple = tuple(tuple(sorted(P)) for P in seq)
    d6_match = gtuple in variants
    if gtuple in rotations:
        orientation = "+1 (deployed order)"
    elif d6_match:
        orientation = ("-1 (reversal; the other C6 generator g^5 "
                       "traverses the deployed order)")
    else:
        orientation = "none (no D6 match)"
    check("A3.4 TYPED INTERTWINER: the g-sequence g^n(f1w1), n = 0..5 "
          "= %s; period 6: %s; every g-step an edge of the deployed "
          "hexagon: %s; equals the deployed cycle up to D6 (rotation + "
          "reflection, the tfpt_2 Lemma-dd convention): %s; "
          "orientation %s"
          % (list(gtuple), period6, steps_deployed, d6_match,
             orientation),
          True, "measured, typed either way")

    print("      corpus quotient reading: the flavor C6 acts on the 6 "
          "residue sites Z_6")
    print("      (word length L = 6n + r; residue sets = the D6-orbit "
          "of {0,1,3}, tfpt_2);")
    print("      deployed graph realization = exactly this hexagon "
          "(v808 [E neu]) -- the")
    print("      restriction of the Lambda^2 action to the 6-orbit IS "
          "the transport hexagon.")

    intertwined = ((is_sig or is_sig_inv) and is_wswap
                   and orbits_are_shells and period6
                   and steps_edges and steps_deployed and d6_match)
    partial = (not intertwined) and ctype == [1, 3, 6]

    # ==================================================================
    section("A4 -- the orbit reading of the recovery exponent (report)")
    # ==================================================================
    lam_rec = Fr(Z2, N_fam) ** len(AUT)
    lam_dep = (Fr(1) - Fr(1, N_fam)) ** 6      # v124 lambda_1
    check("A4.1 the chain: lambda_rec = (|Z2|/N_fam)^{|Aut(C_fin)|} = "
          "(2/3)^6 = %s == the deployed frozen recovery value "
          "(1 - 1/3)^6 = %s (v54/v56/v82/v124; exact Fractions, no "
          "fit)" % (lam_rec, lam_dep),
          lam_rec == Fr(64, 729) == lam_dep and len(AUT) == 6,
          kill="K1")
    check("A4.2 HONEST TYPING: the corpus derives the exponent 6 as "
          "p2 = |R+(A3)| = the hexagon size (v124); '6 = |Aut(C_fin)|'"
          " is a NEW reading, consistent iff the hexagon is one full "
          "Aut orbit (A3.3: %s); the first-generation winding +6 "
          "(L = R + 6 1 e1^T, v4/v857) = one full revolution = one "
          "full Aut orbit -- report line, NO claim upgrade, no marker "
          "move" % orbits_are_shells,
          True, "measured, typed either way")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    stab_q = [p for p in SP
              if all(QSTAR[p[i]] == QSTAR[i] for i in range(16))]
    nonpres = [p for p in SP if p not in set(stab_q)]
    n_factor = 0
    example = None
    for p in sorted(nonpres):
        pp2 = compose(p, p)
        pp3 = compose(pp2, p)
        if pp2 in (SIGP, SIGP2) and pp3 == G3:
            n_factor += 1
        if example is None:
            example = (p, perm_order(pp2), perm_order(pp3),
                       pp2 in (SIGP, SIGP2), pp3 == G3)
    check("C1 FIRES: |Stab_Sp(q*)| = %d == 120, non-preserving maps "
          "%d == 600; NONE factors consistently as g^2/g^3 (square in "
          "{sigma, sigma^2} AND cube = the Aut involution): count = "
          "%d == 0" % (len(stab_q), len(nonpres), n_factor),
          len(stab_q) == 120 and len(nonpres) == 600 and n_factor == 0,
          kill="K3")
    print("      lex-min non-q*-preserving example: ord(p^2) = %d, "
          "ord(p^3) = %d, p^2 in {sigma, sigma^2}: %s, p^3 = g^3: %s"
          % (example[1], example[2], example[3], example[4]))

    scram = [HEX[0], HEX[2], HEX[1], HEX[3], HEX[4], HEX[5]]
    scram_t = [tuple(sorted(P)) for P in scram]
    scram_nonedge = any(not adj(scram[k], scram[(k + 1) % 6])
                        for k in range(6))
    scram_nomatch = gtuple not in cyc_variants(scram_t)
    check("C2 FIRES: scrambled transport table (entries 1 and 2 "
          "swapped): contains a non-edge step (%s) and is NOT D6-"
          "equivalent to the g-sequence (%s) -- the intertwiner test "
          "breaks on a scrambled table"
          % (scram_nonedge, scram_nomatch),
          scram_nonedge and scram_nomatch, kill="K3")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = "PIPELINE-BROKEN"
    else:
        sub = ("INTERTWINED" if intertwined
               else ("PARTIAL" if partial else "DEAD"))
        VERDICT = "C6FLAVOR-MEASURED + " + sub
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * Aut(C_fin) recomputed from the deployed data: C6, generator g
    pinned by g^2 = sigma; matrix and slot permutation printed above.
  * factorization: g^2 = the family 3-cycle (as deployed); g^3 = the
    unique involution, slot action = the W-edge swap (the S2 sheet
    factor of the F|W = 3+2 split) -- the corpus has NO deployed sheet
    involution ON V, typed honestly.
  * Lambda^2 action: cycle type and orbit/shell comparison measured;
    the intertwiner against the deployed v808 hexagon cycle decided up
    to D6 (the flavor convention), orientation typed.
  * orbit reading: (|Z2|/N_fam)^{|Aut|} = (2/3)^6 = 64/729 == the
    frozen recovery value; the exponent reading 6 = |Aut(C_fin)| is
    NEW and stays a report line (corpus: 6 = p2 = |R+(A3)|).
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot
                 and VERDICT.startswith("C6FLAVOR-MEASURED")) else 1


if __name__ == "__main__":
    raise SystemExit(main())
