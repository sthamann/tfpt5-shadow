#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v834 -- PG32.FLAGS.01: the PG(3,2) flag normal form for the 105 + 35 vacuum completion, with the incidence kill test typed as a split, ONE module from one probe (26/26 checks, verdict PG32-FLAGS-EXACT + INCIDENCE-SPLIT; discovery probe pg32_flag_completion_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, < 1 s).  THE COUNTING NORMAL FORM (exact): the Gaussian binomial [4 choose 2]_2 = 35 = the census of 2-dim subspaces of F2^4; each subspace has 4 cosets, so 140 affine 2-flats of AG(4,2) = 35 through the origin + 105 not; PG(3,2) has 15 points, 35 lines, 105 = 35 x 3 point-line flags, canonically bijective to the C(15,2) = 105 point pairs via {x,y} <-> (x+y, {x,y,x+y}).  THE RM LAYER (v819 S4 / v821 S1-S2 / v822 rebuilt, all set equalities): shortened RM(2,4) = [15,10,4] has weight enumerator 1 + 105z^4 + 280z^6 + 435z^8 + 168z^10 + 35z^12 EXACT, and its 105 weight-4 words ARE the indicators of the 105 flats avoiding 0; the 140 weight-4 words of RM(2,4) ARE all 140 flats; Grams entrywise H105^T H105 = 22I + 6J, H35^T H35 = 6I + J, A140^T A140 = 28 I_16 + 7 J_16 (the v822 unshortening identity).  THE VACUUM READING: the 35 origin planes puncture to weight 3, NONE lies in the shortened code (min distance 4), ONE origin plane unshortens dim 10 -> 11, and in RM(2,4) the vacuum coordinate restores weight 4 -- the vacuum coordinate is ORIGIN RESTORATION.  THE INCIDENCE SPLIT (the kill test, typed): with the corpus symplectic form hb(v,w) = (sum v)(sum w) - v.w mod 2 (v774), the 105 = 45 + 60 split is the Sp(4,2)-ORBIT decomposition on BOTH sides (|Sp(4,2)| = 720 by brute force; flats and flags each split 45 + 60); on the 60 NON-ISOTROPIC rungs the polarity map PHI: (U,t) -> ((t+U) n U^omega, U^omega) is well-defined (unique intersection on all 60), bijective, Sp(4,2)-EQUIVARIANT (all 60 x 720) and INCIDENCE-PRESERVING; on the 45 DOILY rungs the obstruction is typed: U^omega = U (doily self-polarity) and (t+U) n U = EMPTY for 45/45 flats -- NO flag can put its point inside its own check support -- and the unique abstract equivariant bijection matches flags whose support n line = 0; the flag incidence Gram is 18I + 3J != 22I + 6J, so no flag reading reproduces the corpus check Gram.  THE TYPED CONCLUSION: '105 checks = 105 flags' is exact as a deck-equivariant BIJECTION, NOT as an incidence isomorphism -- the obstruction sits exactly on the doily (the typed reason v822's continuum dilation died).  VACUUM CARRIER CONTENT: the zero class of L/(1+i)L carries NO E8 root (0/240 rebuilt, v689 [E]) -- the vacuum point repairs the label Gram (+6I+J) but adds no carrier content; v822's frozen continuum kill (UNSHORTEN-DEAD / DILATION-DEAD) cited as the companion negative.  Controls fire (a scrambled plane row breaks the 22I+6J Gram; a degenerate form breaks the doily census; the 45-sector obstruction fires as its own control vs 0/60 empty on the non-isotropic side).  Exact integer arithmetic; no floats, no RNG, no fit.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe pg32_flag_completion_probe.py (26/26,
verdict PG32-FLAGS-EXACT + INCIDENCE-SPLIT, 2026-08-07, re-run
identically at promotion); this module runs the frozen protocol
VERBATIM (< 1 s).  The original probe docstring and frozen protocol
live in the probe file verbatim (experiments/tfpt-discovery/).  Corpus
sources rebuilt inline: v819 S4 ([15,10,4] enumerator), v821 (140 =
105 + 35, Grams), v822 (unshortening identity, code dims; its
continuum kill cited, not recomputed), v774 (corpus symplectic form),
note_e8_gaussian_code / v689 (zero-class census).
"""
import itertools
import time
from collections import Counter

EXPECTED_VERDICT_HEAD = "PG32-FLAGS-EXACT + INCIDENCE-SPLIT"


def run():
    t_start = time.time()
    checks = []

    def check(name, ok, detail=""):
        checks.append(bool(ok))
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                               ("  -- " + detail) if detail else ""))
        return bool(ok)

    def section(title):
        print("\n== %s ==  (t=%.1fs)" % (title, time.time() - t_start))

    print("v834 PG32.FLAGS.01 -- the PG(3,2) flag normal form for "
          "105 + 35")

    PTS = list(range(16))               # F2^4 as ints (bit k = coord k)
    NZ = [v for v in PTS if v]

    def pc(v):
        return bin(v).count("1")

    # ==================================================================
    section("S1: Gaussian binomial and the 140 = 105 + 35 flats")
    # ==================================================================
    gb = ((2 ** 4 - 1) * (2 ** 4 - 2)) // ((2 ** 2 - 1) * (2 ** 2 - 2))
    subspaces = set()
    for u1, u2 in itertools.combinations(NZ, 2):
        subspaces.add(frozenset([0, u1, u2, u1 ^ u2]))
    subspaces = sorted(subspaces, key=sorted)
    check("S1.1 [4 choose 2]_2 = (15*14)/(3*2) = %d == 35 == census of "
          "2-dim subspaces of F2^4 (%d)" % (gb, len(subspaces)),
          gb == 35 == len(subspaces))

    flats = []                          # (U, frozenset coset)
    for U in subspaces:
        cosets = set()
        for t in PTS:
            cosets.add(frozenset(t ^ u for u in U))
        assert len(cosets) == 4
        for cs in cosets:
            flats.append((U, cs))
    through0 = [(U, cs) for U, cs in flats if 0 in cs]
    not0 = [(U, cs) for U, cs in flats if 0 not in cs]
    check("S1.2 each U has 4 cosets -> %d affine 2-flats; %d through "
          "the origin + %d not; 105 + 35 = 140"
          % (len(flats), len(through0), len(not0)),
          len(flats) == 140 and len(through0) == 35
          and len(not0) == 105)

    # ==================================================================
    section("S2: PG(3,2) points, lines, flags")
    # ==================================================================
    lines = [frozenset(U - {0}) for U in subspaces]
    flags = [(p, ln) for ln in lines for p in ln]
    npairs = len(list(itertools.combinations(NZ, 2)))
    check("S2.1 PG(3,2): %d points, %d lines, 3 points per line, "
          "%d point-line flags = 35 x 3; flags ~= point pairs "
          "(C(15,2) = %d) via {x,y} <-> (x+y, {x,y,x+y})"
          % (len(NZ), len(lines), len(flags), npairs),
          len(NZ) == 15 and len(lines) == 35
          and all(len(ln) == 3 for ln in lines)
          and len(flags) == 105 and npairs == 105)
    pair_bij = {frozenset((a, b)): (a ^ b, frozenset((a, b, a ^ b)))
                for a, b in itertools.combinations(NZ, 2)}
    check("S2.2 the pair<->flag map is a bijection onto the 105 flags",
          sorted(pair_bij.values(), key=str) == sorted(flags, key=str)
          or set(pair_bij.values()) == set(flags))

    # ==================================================================
    section("S3: the RM layer (v819 S4 / v821 S1-S2 / v822 rebuilt)")
    # ==================================================================
    def eval_word(func):
        """evaluate a boolean function on all 16 points -> 16-bit
        word."""
        return tuple(func(v) for v in PTS)

    monos1 = [eval_word(lambda v, k=k: (v >> k) & 1) for k in range(4)]
    monos2 = [eval_word(lambda v, k=k, l=l:
                        ((v >> k) & 1) * ((v >> l) & 1))
              for k, l in itertools.combinations(range(4), 2)]
    ONEW = tuple(1 for _ in PTS)

    def span(gens):
        out = set()
        for bits in itertools.product((0, 1), repeat=len(gens)):
            w = tuple(sum(b * g[k] for b, g in zip(bits, gens)) % 2
                      for k in range(len(gens[0])))
            out.add(w)
        return out

    rm24 = span([ONEW] + monos1 + monos2)          # RM(2,4), dim 11
    short_gens = [tuple(w[v] for v in NZ) for w in monos1 + monos2]
    c1perp = span(short_gens)                      # shortened RM(2,4)
    check("S3.1 dims: |RM(2,4)| = %d == 2^11, |shortened| = %d == 2^10 "
          "(v822 code dims 11 / 10)" % (len(rm24), len(c1perp)),
          len(rm24) == 2048 and len(c1perp) == 1024)

    we = Counter(sum(w) for w in c1perp)
    check("S3.2 weight enumerator of [15,10,4] = 1 + 105z^4 + 280z^6 + "
          "435z^8 + 168z^10 + 35z^12 EXACT (census: %s)"
          % dict(sorted(we.items())),
          dict(we) == {0: 1, 4: 105, 6: 280, 8: 435, 10: 168, 12: 35})

    w4_words = {w for w in c1perp if sum(w) == 4}
    flat_ind = {tuple(1 if v in cs else 0 for v in NZ)
                for U, cs in not0}
    check("S3.3 the 105 weight-4 words of [15,10,4] ARE the indicators "
          "of the 105 flats avoiding 0 (set equality, %d = %d)"
          % (len(w4_words), len(flat_ind)), w4_words == flat_ind)

    w4_full = {w for w in rm24 if sum(w) == 4}
    all_flat_ind = {tuple(1 if v in cs else 0 for v in PTS)
                    for U, cs in flats}
    check("S3.4 the 140 weight-4 words of RM(2,4) ARE all 140 affine "
          "2-flats (v821 S1; %d = %d)"
          % (len(w4_full), len(all_flat_ind)),
          w4_full == all_flat_ind)

    H105 = sorted(w4_words)
    H35 = [tuple(1 if v in U else 0 for v in NZ) for U in subspaces]

    def gram(cols):
        n = len(cols[0])
        return [[sum(c[i] * c[j] for c in cols) for j in range(n)]
                for i in range(n)]

    def is_aIbJ(G, a, b):
        return all(G[i][j] == (a + b if i == j else b)
                   for i in range(len(G)) for j in range(len(G)))

    G105 = gram(H105)
    G35 = gram(H35)
    check("S3.5 GRAMS entrywise: H105^T H105 == 22I + 6J, H35^T H35 == "
          "6I + J (v821 S2 / v822: 28 planes through a point, 6 "
          "through a pair; 7 lines through a point, 1 through a pair)",
          is_aIbJ(G105, 22, 6) and is_aIbJ(G35, 6, 1))
    A140 = sorted(w4_full)
    G140 = gram(A140)
    check("S3.6 UNSHORTENING IDENTITY: A140^T A140 == 28 I_16 + 7 J_16 "
          "entrywise on all 16 coordinates (diag 35 = planes through a "
          "point, offdiag 7 = through a pair; v822 [E])",
          is_aIbJ(G140, 28, 7))

    w3_punct = {tuple(w[v] for v in NZ) for w in w4_full
                if w[0] == 1}           # origin planes punctured at 0
    check("S3.7 VACUUM READING: the 35 origin planes puncture to "
          "weight 3 (%d words, all weight 3), NONE lies in the "
          "[15,10,4] shortened code (min distance 4), and in RM(2,4) "
          "the vacuum coordinate restores weight 4"
          % len(w3_punct),
          len(w3_punct) == 35 and all(sum(w) == 3 for w in w3_punct)
          and not (w3_punct & c1perp)
          and all(sum(w) == 4 for w in w4_full if w[0] == 1))
    one_unshort = span(short_gens + [sorted(w3_punct)[0]])
    check("S3.8 ONE origin plane unshortens dim 10 -> 11: "
          "|span| = %d == 2^11 = |punctured RM(2,4)| (v822 'ONE origin "
          "plane unshortens')" % len(one_unshort),
          len(one_unshort) == 2048
          and one_unshort == {tuple(w[v] for v in NZ) for w in rm24})

    # ==================================================================
    section("S4: the incidence check (the kill) -- Sp(4,2) and the "
            "doily")
    # ==================================================================
    def hb(v, w):
        # corpus form (v774 GJI = J - I): v^T(J-I)w
        return ((pc(v) & 1) & (pc(w) & 1)) ^ (pc(v & w) & 1)

    rad = [v for v in NZ if all(hb(v, w) == 0 for w in NZ)]
    check("S4.1 hb is alternating (hb(v,v) = 0 all v) and "
          "nondegenerate (radical %s empty)" % rad,
          all(hb(v, v) == 0 for v in PTS) and not rad)

    iso_lines = [U for U in subspaces
                 if all(hb(u, w) == 0 for u in U for w in U)]
    noniso = [U for U in subspaces if U not in iso_lines]
    check("S4.2 DOILY: %d isotropic lines + %d non-isotropic = 35 "
          "(GQ(2,2) has 15 lines)" % (len(iso_lines), len(noniso)),
          len(iso_lines) == 15 and len(noniso) == 20)

    flats45 = [(U, cs) for U, cs in not0 if U in iso_lines]
    flats60 = [(U, cs) for U, cs in not0 if U not in iso_lines]
    iso_line_set = {frozenset(U - {0}) for U in iso_lines}
    flags45 = [(p, ln) for p, ln in flags if ln in iso_line_set]
    flags60 = [(p, ln) for p, ln in flags if ln not in iso_line_set]
    check("S4.3 THE 105 = 45 + 60 SPLIT on BOTH sides: flats %d + %d, "
          "flags %d + %d (45 = 15 x 3 doily-line flags)"
          % (len(flats45), len(flats60), len(flags45), len(flags60)),
          len(flats45) == 45 and len(flats60) == 60
          and len(flags45) == 45 and len(flags60) == 60)

    E = [1, 2, 4, 8]
    SP = []
    for a in NZ:
        for b in NZ:
            if b == a:
                continue
            if hb(a, b) != hb(1, 2):
                continue
            for c in NZ:
                if c in (a, b):
                    continue
                if hb(a, c) != hb(1, 4) or hb(b, c) != hb(2, 4):
                    continue
                span3 = {0, a, b, a ^ b, c, a ^ c, b ^ c, a ^ b ^ c}
                if len(span3) != 8:
                    continue
                for d in NZ:
                    if d in span3:
                        continue
                    if hb(a, d) != hb(1, 8) or hb(b, d) != hb(2, 8) \
                       or hb(c, d) != hb(4, 8):
                        continue
                    m = [0] * 16
                    for v in PTS:
                        x = 0
                        if v & 1:
                            x ^= a
                        if v & 2:
                            x ^= b
                        if v & 4:
                            x ^= c
                        if v & 8:
                            x ^= d
                        m[v] = x
                    SP.append(tuple(m))
    check("S4.4 |Sp(4,2)| = %d == 720 (brute force; the deck action "
          "on V)" % len(SP), len(SP) == 720)

    def act_flat(m, fl):
        U, cs = fl
        return (frozenset(m[u] for u in U),
                frozenset(m[x] for x in cs))

    def act_flag(m, fg):
        p, ln = fg
        return (m[p], frozenset(m[x] for x in ln))

    def orbits(objs, act):
        rem = set(objs)
        out = []
        while rem:
            x = next(iter(rem))
            orb = {act(m, x) for m in SP}
            out.append(len(orb))
            rem -= orb
        return sorted(out)

    ofl = orbits([(U, cs) for U, cs in not0], act_flat)
    ofg = orbits(flags, act_flag)
    check("S4.5 Sp(4,2) ORBITS: flats %s == [45, 60], flags %s == "
          "[45, 60] -- the 45/60 split IS the orbit decomposition on "
          "both sides" % (ofl, ofg), ofl == [45, 60] and ofg == [45, 60])

    def omega(U):
        return frozenset(v for v in PTS
                         if all(hb(v, u) == 0 for u in U))

    phi = {}
    ok_unique = True
    for U, cs in flats60:
        Uw = omega(U)
        inter = [x for x in cs if x in Uw]
        if len(inter) != 1:
            ok_unique = False
            break
        phi[(U, cs)] = (inter[0], frozenset(Uw - {0}))
    check("S4.6 60-SECTOR polarity map PHI: (U,t) -> ((t+U) n U^omega, "
          "U^omega): intersection unique for all 60 (%s), image = the "
          "60 non-isotropic flags, bijective" % ok_unique,
          ok_unique and len(set(phi.values())) == 60
          and set(phi.values()) == set(flags60))
    equi = all(phi[act_flat(m, fl)] == act_flag(m, phi[fl])
               for fl in flats60 for m in SP)
    check("S4.7 PHI is Sp(4,2)-EQUIVARIANT (all 60 x 720 checks) and "
          "INCIDENCE-PRESERVING: the flag point lies IN the check "
          "support and the flag line meets the support in EXACTLY "
          "that point",
          equi and all(phi[fl][0] in fl[1]
                       and len([x for x in fl[1]
                                if x in phi[fl][1]]) == 1
                       for fl in flats60))

    empty_iso = sum(1 for U, cs in flats45
                    if not any(x in omega(U) for x in cs))
    check("S4.8 45-SECTOR OBSTRUCTION: U^omega = U for isotropic U "
          "(doily self-polarity) and (t+U) n U = EMPTY for %d/45 flats "
          "-- on the doily sector NO flag can put its point inside its "
          "own check support via the polarity" % empty_iso,
          all(omega(U) == U for U in iso_lines) and empty_iso == 45)

    fl0 = flats45[0]
    stab_fl0 = [m for m in SP if act_flat(m, fl0) == fl0]
    n_equib = 0
    match_types = []
    for fg in flags45:
        if all(act_flag(m, fg) == fg for m in stab_fl0):
            n_equib += 1
            match_types.append(fg)
    support_hits = [sum(1 for x in fl0[1] if x == fg[0]
                        or x in fg[1]) for fg in match_types]
    check("S4.9 ABSTRACT G-SET CENSUS (45-sector): |Stab(flat0)| = %d "
          "(= 720/45); equivariant images of flat0 among the 45 flags "
          "= %d -> %d equivariant bijection(s) flats45 -> flags45 "
          "exist(s); matched flag(s) %s share their LINE with flat0's "
          "direction U but support n line = %s (the incidence fails "
          "pointwise)"
          % (len(stab_fl0), n_equib, n_equib,
             [(f[0], sorted(f[1])) for f in match_types],
             support_hits),
          len(stab_fl0) == 16
          and all(fg[1] == frozenset(fl0[0] - {0})
                  for fg in match_types)
          and all(h == 0 for h in support_hits))

    Gflag = gram([tuple(1 if (v == p or v in ln) else 0 for v in NZ)
                  for p, ln in flags])
    check("S4.10 GRAM OBSTRUCTION: flag->line incidence Gram = "
          "18I + 3J (diag %d, offdiag %d) != 22I + 6J of the corpus "
          "checks -- the flag reading does NOT reproduce H105^T H105"
          % (Gflag[0][0], Gflag[0][1]),
          is_aIbJ(Gflag, 18, 3) and not is_aIbJ(Gflag, 22, 6))

    # ==================================================================
    section("S5: vacuum carrier content (zero class has no E8 root)")
    # ==================================================================
    G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
               (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
    C_NAIVE = frozenset(
        tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
              for j in range(8))
        for m in itertools.product((0, 1), repeat=4))
    PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
    PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)

    def code_image(code, p):
        return frozenset(tuple(c[p[k]] for k in range(8)) for c in code)

    placements = set()
    for perm in itertools.permutations(range(8)):
        placements.add(code_image(C_NAIVE, perm))
    both = [c for c in placements
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    CSTAR = next(c for c in both if (1, 0, 1, 0, 1, 0, 1, 0) in c)
    ROOTS = []
    for k in range(8):
        for s in (2, -2):
            v = [0] * 8
            v[k] = s
            ROOTS.append(tuple(v))
    for c in (c for c in CSTAR if sum(c) == 4):
        sup = [k for k in range(8) if c[k]]
        for signs in itertools.product((1, -1), repeat=4):
            v = [0] * 8
            for k, s in zip(sup, signs):
                v[k] = s
            ROOTS.append(tuple(v))

    def in_pi2L(v):
        w = [0] * 8
        for k in range(4):
            w[2 * k] = v[2 * k] + v[2 * k + 1]
            w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
        if any(x % 2 for x in w):
            return False
        return tuple((x // 2) % 2 for x in w) in CSTAR

    n_zero = sum(1 for r in ROOTS if in_pi2L(r))
    check("S5.1 the ZERO CLASS carries NO E8 root: %d/240 roots in "
          "(1+i)L (v689 [E] rebuilt) -- the vacuum point repairs the "
          "label Gram (+6I+J, S3.5/S3.6) but adds no carrier content; "
          "v822's frozen continuum kill (UNSHORTEN-DEAD / "
          "DILATION-DEAD) cited as the companion negative" % n_zero,
          len(ROOTS) == 240 and n_zero == 0)

    # ==================================================================
    section("C: controls (must fire)")
    # ==================================================================
    bad_word = tuple(1 if v in (1, 2, 4, 8) else 0 for v in NZ)
    H105_bad = [bad_word] + H105[1:]
    check("C1 scrambled plane row (weight-4 non-plane word "
          "{e1,e2,e3,e4}): H105'^T H105' != 22I + 6J (%s) -- the Gram "
          "identity needs the plane structure"
          % (not is_aIbJ(gram(H105_bad), 22, 6)),
          bad_word not in w4_words
          and not is_aIbJ(gram(H105_bad), 22, 6))

    def hb_deg(v, w):
        """rank-2 alternating form using only coords 0,1 (radical
        dim 2)."""
        return ((v & 1) * ((w >> 1) & 1)
                + (w & 1) * ((v >> 1) & 1)) % 2

    iso_deg = [U for U in subspaces
               if all(hb_deg(u, w) == 0 for u in U for w in U)]
    check("C2 degenerate alternating form (rank 2, radical dim 2): "
          "isotropic-line census %d != 15 -- the doily needs the "
          "nondegenerate corpus form" % len(iso_deg),
          len(iso_deg) != 15)

    check("C3 the 45-sector obstruction FIRES as a control: empty "
          "polarity intersection on 45/45 isotropic flats (S4.8), vs "
          "0/60 empty on the non-isotropic side",
          empty_iso == 45
          and all(any(x in omega(U) for x in cs) for U, cs in flats60))

    # ==================================================================
    n_all = len(checks)
    n_fail = n_all - sum(checks)
    if n_fail == 0:
        verdict = ("PG32-FLAGS-EXACT + INCIDENCE-SPLIT (60-sector "
                   "exact via the symplectic polarity; 45-sector = the "
                   "doily lines obstructed: (t+U) n U^omega = EMPTY, "
                   "and the flag Gram 18I+3J != 22I+6J)")
    else:
        verdict = "PG32-FLAGS-BROKEN (see FAILs)"
    print("\nv834: %d/%d checks passed, %d failed  (%.1f s)"
          % (n_all - n_fail, n_all, n_fail, time.time() - t_start))
    print("VERDICT: %s" % verdict)
    pattern_ok = verdict.startswith(EXPECTED_VERDICT_HEAD)
    print("[%s] PATTERN GATE: expected verdict head %s"
          % ("PASS" if pattern_ok else "FAIL", EXPECTED_VERDICT_HEAD))
    return n_fail + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
