#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v833 -- GAUSSIAN.RAMLADDER.01: the (1+i) ramification ladder -- the four documented roles of the ramified Gaussian prime pi2 = 1+i are ONE machine-checked object with four rungs, each re-certified from scratch, ONE module from one probe (33/33 checks, verdict RAMIFICATION-LADDER-EXACT; discovery probe gaussian_ramification_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~5 s).  RUNG 1, NORM DOUBLING: N(pi2) = 2 and (pi2^2) = (2) as ideals (2 RAMIFIES); on the Gaussian E8 lattice L = A(C*) (the unique mu4/sigma-equivariant Construction-A placement, 2 of 30, rebuilt) the lattice realisation is (1+J)^T (1+J) = 2 I_8 EXACTLY; min L = 4 by exhaustive census of {-1,0,1}^8, so the zero class of L/(1+i)L carries NO root (0/240 directly), the 240 roots distribute 240 = 15 x 16 over the nonzero classes with each class a union of exactly 4 of the 60 Gaussian lines, and the elementary divisors of (1+i)L in L are (1,1,1,1,2,2,2,2) with index 16 = N(pi2)^4.  RUNG 2, THE FOUR-BIT ADDRESS: L/(1+i)L ~= F2^4 with the deck J acting TRIVIALLY (Jx = x mod (1+i)L for all 240 roots) -- the 15 nonzero classes are the address space.  RUNG 3, THE NON-SPLIT JET: Z[i]/(2) ~= F2[eps]/(eps^2) is a ring iso UNIQUE among all 24 bijections (eps = the image of 1+i, the unique nonzero nilpotent); W = L/2L is FREE of rank 4 over the dual numbers (all 4^4 = 256 combinations distinct); the self-extension 0 -> V -> W -> V -> 0 with V = eps W = ker eps = im eps is exact, the deck is the JET UNIT Jbar = 1 + eps, and of ALL 16^4 = 65536 linear sections EXACTLY 0 are deck-equivariant -- the no-canonical-origin obstruction IS non-splitness (v803); the plus-type form q = <x,x>/4 mod 2 has census 136/120, Arf 0, trivial radical, and the 120 root pairs are EXACTLY the q = 1 shell: 240 = 15 x 8 x 2 (address, jet, orientation).  RUNG 4, THE METAPLECTIC LIFT: zeta8 = (1+i)/sqrt2 with zeta8^2 = i, zeta8^8 = 1; the lattice half-deck (1+J)^2 = 2J i.e. ((1+J)/sqrt2)^2 = J; the metaplectic anomaly (S H)^3 = zeta8 I per binary factor and (T3 K3)^3 = i I = THE DECK for the total Fourier (v798); the exact Z[zeta8] BFS census of C2 = <H(x)I, I(x)H, S(x)I, I(x)S, CNOT> mod mu8 gives projective order 11520 = 16 x 720 with ZERO Galois-mixed classes, scalars = mu8, hence |C2| = 92160 = 2 x 46080 and C2 = K u zeta8 K (K = the Q(i)-rational part; K = U G31 U^-1 is v783's chart theorem, cited [E]); witness parities chi(H(x)I) = 1 (the missing coset = the RM-CSS zeta8 phase bit, v819 S4 -> v798 [E]), chi(H(x)H) = chi(CZ) = 0.  Controls fire (the split ring F2 x F2 admits 0 ring isos -- 2 must ramify; the split self-extension admits 65536/65536 equivariant sections -- non-splitness is contentful; a scrambled nilpotent breaks ker = im).  THE COMPRESSION: the four corpus roles of pi2 -- norm doubling / empty zero class (note_e8_gaussian_code Thm 1, v689), the 4-bit address (v689), the non-split jet with deck = 1 + eps (v803), the metaplectic zeta8 with the Clifford index-2 coset and the RM-CSS phase bit (v783/v798/v819) -- are ONE ladder: the same ramified prime read at (pi2), (pi2^2) and pi2/sqrt2.  Exact integer/Fraction/sympy arithmetic; no floats, no RNG.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe gaussian_ramification_probe.py (33/33,
verdict RAMIFICATION-LADDER-EXACT, 2026-08-07, re-run identically at
promotion); this module runs the frozen protocol VERBATIM (~5 s).  The
original probe docstring and frozen protocol live in the probe file
verbatim (experiments/tfpt-discovery/).  Corpus sources re-certified
inline: note_e8_gaussian_code / v689 (census 15 x 16, zero class,
norm doubling, 60 lines), v803 (non-split jet), v783 (two-qubit
Clifford C2 = G31 u zeta8 G31), v798 (metaplectic anomaly), v819 S4
(the RM-CSS zeta8 bit, carried as the v798-certified coset membership).
"""
import itertools
import time

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, \
    smith_normal_form
from sympy.polys.domains import ZZ

EXPECTED_VERDICT = "RAMIFICATION-LADDER-EXACT"


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

    print("v833 GAUSSIAN.RAMLADDER.01 -- the (1+i) ramification ladder "
          "(norm doubling / 4-bit address / non-split jet / "
          "metaplectic lift)")

    # ==================================================================
    section("R1a: the ramified prime in Z[i] (sympy exact)")
    # ==================================================================
    i = sp.I
    pi2 = 1 + i
    check("R1.1 N(pi2) = pi2 * conj(pi2) = %s == 2"
          % sp.expand(pi2 * sp.conjugate(pi2)),
          sp.expand(pi2 * sp.conjugate(pi2)) == 2)
    check("R1.2 pi2^2 = %s == 2i and (pi2^2) = (2) as ideals: "
          "2 = -i * pi2^2 exactly (i a unit)" % sp.expand(pi2 ** 2),
          sp.expand(pi2 ** 2) == 2 * i
          and sp.expand(-i * pi2 ** 2) == 2)

    # ==================================================================
    section("R1b: rebuild the Gaussian E8 (Construction A over C*, "
            "note_e8_gaussian_code / v689 machinery)")
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
    W0246 = (1, 0, 1, 0, 1, 0, 1, 0)
    check("R1.3 placement census: %d distinct placements (= 8!/1344), "
          "exactly %d invariant under both pi_J and pi_sigma"
          % (len(placements), len(both)),
          len(placements) == 30 and len(both) == 2)
    CSTAR = next(c for c in both if W0246 in c)

    w4 = [c for c in CSTAR if sum(c) == 4]
    ROOTS = []
    for k in range(8):
        for s in (2, -2):
            v = [0] * 8
            v[k] = s
            ROOTS.append(tuple(v))
    for c in w4:
        sup = [k for k in range(8) if c[k]]
        for signs in itertools.product((1, -1), repeat=4):
            v = [0] * 8
            for k, s in zip(sup, signs):
                v[k] = s
            ROOTS.append(tuple(v))
    check("R1.4 root census: 16 coordinate + 14*16 codeword lifts = %d "
          "== 240, all norm 4, all in L (mod 2 in C*)" % len(ROOTS),
          len(ROOTS) == 240 and len(set(ROOTS)) == 240
          and all(sum(x * x for x in r) == 4 for r in ROOTS)
          and all(tuple(abs(x) % 2 for x in r) in CSTAR for r in ROOTS))

    Jm = sp.zeros(8, 8)
    for k in range(4):
        Jm[2 * k, 2 * k + 1] = -1
        Jm[2 * k + 1, 2 * k] = 1
    I8 = sp.eye(8)
    check("R1.5 NORM DOUBLING: (1+J)^T (1+J) == 2*I_8 exactly "
          "(multiplication by pi2 doubles norms; Lean one_add_J_gram)",
          (I8 + Jm).T * (I8 + Jm) == 2 * I8)

    short = [v for v in itertools.product((-1, 0, 1), repeat=8)
             if any(v) and tuple(abs(x) % 2 for x in v) in CSTAR
             and sum(x * x for x in v) < 4]
    check("R1.6 min L = 4: census over {-1,0,1}^8 finds %d nonzero "
          "vectors of norm < 4; hence min (1+i)L = 2*4 = 8 > 4 and the "
          "ZERO CLASS IS EMPTY on roots" % len(short), len(short) == 0)

    def in_L(v):
        return tuple(x % 2 for x in v) in CSTAR

    def in_pi2L(v):
        # x in (1+i)L  <=>  (1-J)x/2 in L    (since (1+J)(1-J) = 2)
        w = [0] * 8
        for k in range(4):
            w[2 * k] = v[2 * k] + v[2 * k + 1]
            w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
        if any(x % 2 for x in w):
            return False
        return in_L([x // 2 for x in w])

    def J_vec(v):
        out = [0] * 8
        for k in range(4):
            out[2 * k] = -v[2 * k + 1]
            out[2 * k + 1] = v[2 * k]
        return tuple(out)

    check("R1.7 zero class empty, directly: %d of 240 roots lie in "
          "(1+i)L" % sum(1 for r in ROOTS if in_pi2L(r)),
          not any(in_pi2L(r) for r in ROOTS))

    labels = {}
    reps = []
    for r in ROOTS:
        for li, rep in enumerate(reps):
            if in_pi2L(tuple(a - b for a, b in zip(r, rep))):
                labels[r] = li
                break
        else:
            labels[r] = len(reps)
            reps.append(r)
    counts = sorted(
        [sum(1 for r in ROOTS if labels[r] == li)
         for li in range(len(reps))])
    check("R1.8 CENSUS 240 = 15 x 16: %d classes, sizes %s"
          % (len(reps), sorted(set(counts))),
          len(reps) == 15 and counts == [16] * 15)

    lines = set()
    for r in ROOTS:
        orbit = frozenset([r, J_vec(r), tuple(-x for x in r),
                           tuple(-x for x in J_vec(r))])
        lines.add(orbit)
    check("R1.9 60 Gaussian lines (J free on roots, orbits size 4), "
          "each class a union of exactly 4 lines: %d lines, per-class "
          "line count %s" % (len(lines), sorted(set(
              sum(1 for ln in lines if labels[next(iter(ln))] == li)
              for li in range(15)))),
          len(lines) == 60 and all(len(ln) == 4 for ln in lines)
          and all(sum(1 for ln in lines
                      if labels[next(iter(ln))] == li) == 4
                  for li in range(15)))

    gens = sp.Matrix([list(c) for c in sorted(CSTAR)]
                     + [[2 * (r == k) for k in range(8)]
                        for r in range(8)]).T
    Bc = hermite_normal_form(gens)      # 8x8, columns = Z-basis of L
    detB = abs(Bc.det())
    M1J = Bc.inv() * (I8 + Jm) * Bc     # (1+i) in basis coordinates
    check("R1.10 HNF basis of L: |det| = %d == 16 (= [Z^8 : L]); "
          "(1+i)-transport matrix integral: %s"
          % (detB, all(x.is_Integer for x in M1J)),
          detB == 16 and all(x.is_Integer for x in M1J))
    snf = list(smith_normal_form(M1J, domain=ZZ).diagonal())
    snf_abs = sorted(abs(x) for x in snf)
    check("R1.11 elementary divisors of (1+i)L in L = %s == "
          "(1,1,1,1,2,2,2,2); index = det(1+J) = %d == 16 = N(pi2)^4"
          % (snf_abs, abs((I8 + Jm).det())),
          snf_abs == [1, 1, 1, 1, 2, 2, 2, 2]
          and abs((I8 + Jm).det()) == 16)

    # ==================================================================
    section("R2: the four-bit address V = L/(1+i)L")
    # ==================================================================
    check("R2.1 |L/(1+i)L| = 2^4, F2-dimension 4: V ~= F2^4 (15 "
          "nonzero addresses, R1.8)", len(reps) == 15 and 2 ** 4 == 16)
    check("R2.2 mu4-STABILITY: Jx == x mod (1+i)L for all 240 roots "
          "(J acts trivially on the address)",
          all(in_pi2L(tuple(a - b for a, b in zip(J_vec(r), r)))
              for r in ROOTS))

    # ==================================================================
    section("R3: the non-split jet W = L/2L = L/pi2^2 L")
    # ==================================================================
    ZI2 = [(0, 0), (1, 0), (0, 1), (1, 1)]      # a + b i mod 2

    def zi_mul(x, y):
        a, b = x
        c, d = y
        return ((a * c - b * d) % 2, (a * d + b * c) % 2)

    def zi_add(x, y):
        return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)

    DUAL = [(0, 0), (1, 0), (0, 1), (1, 1)]     # a + b eps, eps^2 = 0

    def du_mul(x, y):
        a, b = x
        c, d = y
        return ((a * c) % 2, (a * d + b * c) % 2)

    def du_add(x, y):
        return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)

    def count_ring_isos(mul2, add2, zero_idx, one_idx):
        """unital ring isos Z[i]/(2) -> target among all 24 bijections."""
        n = 0
        for img in itertools.permutations(range(4)):
            f = {ZI2[k]: k for k in range(4)}
            ok = (img[f[(0, 0)]] == zero_idx
                  and img[f[(1, 0)]] == one_idx)
            if ok:
                for x in ZI2:
                    for y in ZI2:
                        if img[f[zi_mul(x, y)]] != mul2(img[f[x]],
                                                        img[f[y]]) \
                           or img[f[zi_add(x, y)]] != add2(img[f[x]],
                                                           img[f[y]]):
                            ok = False
                            break
                    if not ok:
                        break
            n += ok
        return n

    du_mul_i = lambda p, q: DUAL.index(du_mul(DUAL[p], DUAL[q]))
    du_add_i = lambda p, q: DUAL.index(du_add(DUAL[p], DUAL[q]))
    n_iso = count_ring_isos(du_mul_i, du_add_i, 0, 1)
    check("R3.1 RING ISO Z[i]/(2) ~= F2[eps]/(eps^2): exactly %d of 24 "
          "bijections is a ring iso (1+i <-> eps, the unique nonzero "
          "nilpotent)" % n_iso, n_iso == 1)

    E8_cols = [[int(M1J[r, c]) % 2 for r in range(8)] for c in range(8)]

    def E_apply(cbits):
        out = 0
        for c in range(8):
            if (cbits >> c) & 1:
                for r in range(8):
                    if E8_cols[c][r]:
                        out ^= (1 << r)
        return out

    EIM = sorted({E_apply(w) for w in range(256)})
    EKER = [w for w in range(256) if E_apply(w) == 0]
    E2_zero = all(E_apply(E_apply(w)) == 0 for w in range(256))
    check("R3.2 eps^2 = 0 on W (pi2^2 = 2), rank eps = 4, and "
          "ker(eps) = im(eps) (%d = %d elements): the self-dual "
          "differential code" % (len(EIM), len(EKER)),
          E2_zero and len(EIM) == 16 and set(EIM) == set(EKER))

    Vlab = {}
    for w in range(256):
        cls = min(w ^ m for m in EIM)
        Vlab[w] = cls
    vbasis = []
    spanned = {0}
    for w in range(1, 256):
        if Vlab[w] in spanned:
            continue
        vbasis.append(w)
        spanned = set()
        for bits in itertools.product((0, 1), repeat=len(vbasis)):
            acc = 0
            for bt, vb in zip(bits, vbasis):
                if bt:
                    acc ^= vb
            spanned.add(Vlab[acc])
        if len(spanned) == 16:
            break
    assert len(vbasis) == 4 and len(spanned) == 16
    free_span = set()
    for coefs in itertools.product(range(4), repeat=4):
        acc = 0
        for cf, g in zip(coefs, vbasis):
            a, b = DUAL[cf]
            if a:
                acc ^= g
            if b:
                acc ^= E_apply(g)
        free_span.add(acc)
    check("R3.3 FREENESS: W is free of rank 4 over F2[eps]/(eps^2) -- "
          "the 4^4 = 256 dual-number combinations of the 4 generators "
          "are distinct (%d/256)" % len(free_span),
          len(free_span) == 256)
    check("R3.4 EXACTNESS 0 -> V -> W -> V -> 0: V = eps W (16 = 2^4 "
          "elements), W/eps W ~= F2^4 (16 classes), ker = im (R3.2)",
          len(EIM) == 16 and len(set(Vlab.values())) == 16)

    Jbar_cols = [[int((Bc.inv() * Jm * Bc)[r, c]) % 2 for r in range(8)]
                 for c in range(8)]

    def Jbar_apply(cbits):
        out = 0
        for c in range(8):
            if (cbits >> c) & 1:
                for r in range(8):
                    if Jbar_cols[c][r]:
                        out ^= (1 << r)
        return out

    check("R3.5 DECK = JET UNIT: Jbar == 1 + eps on W (all 256), and "
          "Jbar acts trivially on V (mu4-equivariance = J-fixedness "
          "of sections)",
          all(Jbar_apply(w) == (w ^ E_apply(w)) for w in range(256))
          and all(Vlab[Jbar_apply(w)] == Vlab[w] for w in range(256)))

    fibers = [[w for w in range(256) if Vlab[w] == Vlab[vb]]
              for vb in vbasis]
    n_sections = 0
    n_equivariant = 0
    for choice in itertools.product(*fibers):
        n_sections += 1
        if all(Jbar_apply(s) == s for s in choice):
            n_equivariant += 1
    check("R3.6 NON-SPLITNESS: %d linear sections total (== 16^4 = "
          "65536), deck-equivariant splittings = %d == 0 -- the "
          "no-canonical-origin obstruction IS non-splitness (v803)"
          % (n_sections, n_equivariant),
          n_sections == 65536 and n_equivariant == 0)

    Bc_int = [[int(Bc[r, c]) for c in range(8)] for r in range(8)]

    def lift(cbits):
        return tuple(sum(Bc_int[r][c] * ((cbits >> c) & 1)
                         for c in range(8)) for r in range(8))

    qv = {}
    for w in range(256):
        xv = lift(w)
        n2 = sum(t * t for t in xv)
        assert n2 % 4 == 0
        qv[w] = (n2 // 4) % 2
    q1 = [w for w in range(256) if qv[w] == 1]
    Binv = Bc.inv()
    root_pts = set()
    for r in ROOTS:
        cb = Binv * sp.Matrix(r)
        assert all(x.is_Integer for x in cb)
        root_pts.add(sum((int(cb[k]) % 2) << k for k in range(8)))
    rad = [w for w in range(256) if w and all(
        (qv[w ^ u] + qv[w] + qv[u]) % 2 == 0 for u in range(256))]
    check("R3.7 PLUS-TYPE FORM: census q=0/q=1 = %d/%d == 136/120, "
          "Arf = 0, radical of b = <x,y>/2 trivial (%d nonzero radical "
          "elements)" % (256 - len(q1), len(q1), len(rad)),
          len(q1) == 120 and len(rad) == 0)
    check("R3.8 THE 120 ROOT PAIRS ARE THE q=1 SHELL: 240 roots -> %d "
          "distinct points of W, all q=1, equal to the shell as a SET: "
          "240 = 15 x 8 x 2 (address, jet, orientation)"
          % len(root_pts),
          len(root_pts) == 120 and root_pts == set(q1))

    # ==================================================================
    section("R4: the metaplectic lift zeta8 = (1+i)/sqrt2")
    # ==================================================================
    s2 = sp.sqrt(2)
    z8 = (1 + i) / s2
    check("R4.1 zeta8 = (1+i)/sqrt2: zeta8^2 = %s == i, zeta8^4 = %s "
          "== -1, zeta8^8 = %s == 1"
          % (sp.simplify(z8 ** 2), sp.simplify(z8 ** 4),
             sp.simplify(z8 ** 8)),
          sp.simplify(z8 ** 2 - i) == 0
          and sp.simplify(z8 ** 4 + 1) == 0
          and sp.simplify(z8 ** 8 - 1) == 0)
    check("R4.2 HALF-DECK REALISATION on the lattice: (1+J)^2 == 2J "
          "exactly, i.e. ((1+J)/sqrt2)^2 = J (v798: zeta8 is the real "
          "orthogonal half-deck)", (I8 + Jm) * (I8 + Jm) == 2 * Jm)

    H2 = sp.Matrix([[1, 1], [1, -1]]) / s2
    S2m = sp.diag(1, i)
    I2 = sp.eye(2)
    anom1 = sp.simplify((S2m * H2) ** 3 - z8 * I2)
    check("R4.3 METAPLECTIC ANOMALY per binary factor: (S H)^3 == "
          "zeta8 * I_2 exactly (Weil constant gamma = zeta8, v798)",
          anom1 == sp.zeros(2, 2))
    K1 = sp.kronecker_product(H2, I2)
    T1 = sp.kronecker_product(S2m, I2)
    K3 = sp.kronecker_product(H2, H2)
    T3 = sp.kronecker_product(S2m, S2m)
    check("R4.4 (T1 K1)^3 == zeta8 * I_4 and TOTAL FOURIER "
          "(T3 K3)^3 == i * I_4 = THE DECK (v798: the deck is the "
          "metaplectic anomaly of the total modular lift)",
          sp.simplify((T1 * K1) ** 3 - z8 * sp.eye(4)) == sp.zeros(4, 4)
          and sp.simplify((T3 * K3) ** 3 - i * sp.eye(4))
          == sp.zeros(4, 4))

    w_coset = sp.simplify(z8 ** -1 * K1)
    qi_rat = all(sp.simplify(sp.re(x)).is_rational
                 and sp.simplify(sp.im(x)).is_rational for x in w_coset)
    check("R4.5 COSET WITNESS (v783 P3.8): zeta8^-1 (H(x)I) has Q(i) "
          "entries (%s); H(x)I itself has irrational sqrt2 entries -> "
          "Galois parity chi(H(x)I) = 1" % qi_rat,
          qi_rat and not all(sp.simplify(sp.re(x)).is_rational
                             and sp.simplify(sp.im(x)).is_rational
                             for x in K1))

    # ---- exact BFS of C2 mod mu8 phases (Z[zeta8]/sqrt2^e arithmetic)
    print("    building C2 = <H(x)I, I(x)H, S(x)I, I(x)S, CNOT> mod "
          "mu8 (exact Z[zeta8] BFS) ...")

    def emul(a, b):
        c = [0, 0, 0, 0]
        for p in range(4):
            ap = a[p]
            if ap:
                for q in range(4):
                    bq = b[q]
                    if bq:
                        m = p + q
                        if m < 4:
                            c[m] += ap * bq
                        else:
                            c[m - 4] -= ap * bq
        return tuple(c)

    SQ2 = (0, 1, 0, -1)                 # sqrt2 = z - z^3

    def mat_mul(A, B):
        ea, Ma = A
        eb, Mb = B
        out = []
        for r in range(4):
            for cidx in range(4):
                acc = [0, 0, 0, 0]
                for k in range(4):
                    xv = emul(Ma[4 * r + k], Mb[4 * k + cidx])
                    acc[0] += xv[0]
                    acc[1] += xv[1]
                    acc[2] += xv[2]
                    acc[3] += xv[3]
                out.append(tuple(acc))
        e = ea + eb
        while e > 0:
            red = []
            ok = True
            for ent in out:
                y = emul(ent, SQ2)
                if any(t % 2 for t in y):
                    ok = False
                    break
                red.append(tuple(t // 2 for t in y))
            if not ok:
                break
            out = red
            e -= 1
        return (e, tuple(out))

    def zmul_entry(ent):
        c0, c1, c2, c3 = ent
        return (-c3, c0, c1, c2)

    def canon(A):
        e, M = A
        best = None
        cur = M
        for _ in range(8):
            key = (e,) + tuple(t for ent in cur for t in ent)
            if best is None or key < best:
                best = key
            cur = tuple(zmul_entry(ent) for ent in cur)
        return best

    def gtype(A):
        """Galois homogeneity: 0 = all entries even-graded
        (Z[i]-numerator), 1 = all odd-graded (zeta8 Z[i]),
        None = mixed."""
        e, M = A
        ty = None
        for ent in M:
            ev = ent[0] or ent[2]
            od = ent[1] or ent[3]
            if ev and od:
                return None
            if ev:
                t = 0
            elif od:
                t = 1
            else:
                continue
            if ty is None:
                ty = t
            elif ty != t:
                return None
        return (ty + e) % 2 if ty is not None else e % 2

    def mk(entries, e=0):
        return (e, tuple(entries))

    ZE = (0, 0, 0, 0)
    ONE = (1, 0, 0, 0)
    MONE = (-1, 0, 0, 0)
    II = (0, 0, 1, 0)                   # i = z^2
    HxI = mk([ONE, ZE, ONE, ZE,  ZE, ONE, ZE, ONE,
              ONE, ZE, MONE, ZE, ZE, ONE, ZE, MONE], 1)
    IxH = mk([ONE, ONE, ZE, ZE,  ONE, MONE, ZE, ZE,
              ZE, ZE, ONE, ONE,  ZE, ZE, ONE, MONE], 1)
    SxI = mk([ONE, ZE, ZE, ZE,  ZE, ONE, ZE, ZE,
              ZE, ZE, II, ZE,   ZE, ZE, ZE, II], 0)
    IxS = mk([ONE, ZE, ZE, ZE,  ZE, II, ZE, ZE,
              ZE, ZE, ONE, ZE,  ZE, ZE, ZE, II], 0)
    CNOT = mk([ONE, ZE, ZE, ZE,  ZE, ONE, ZE, ZE,
               ZE, ZE, ZE, ONE,  ZE, ZE, ONE, ZE], 0)
    GENS = [HxI, IxH, SxI, IxS, CNOT]
    IDm = mk([ONE, ZE, ZE, ZE, ZE, ONE, ZE, ZE,
              ZE, ZE, ONE, ZE, ZE, ZE, ZE, ONE], 0)

    group = {canon(IDm): IDm}
    frontier = [IDm]
    homog = {canon(IDm): gtype(IDm)}
    while frontier:
        nxt = []
        for A in frontier:
            for g in GENS:
                B = mat_mul(A, g)
                key = canon(B)
                if key not in group:
                    group[key] = B
                    homog[key] = gtype(B)
                    nxt.append(B)
        frontier = nxt
    n_proj = len(group)
    n_mixed = sum(1 for v in homog.values() if v is None)
    check("R4.6 PROJECTIVE BFS CENSUS: |C2 / mu8| = %d == 11520 = "
          "16 x 720 (Pauli x Sp(4,2)); Galois-MIXED classes = %d == 0 "
          "(every class homogeneous)" % (n_proj, n_mixed),
          n_proj == 11520 and n_mixed == 0)
    check("R4.7 SCALARS = mu8: zeta8 I = (T1 K1)^3 in C2 (R4.4) and "
          "roots of unity in Q(zeta8) are exactly mu8 => |C2| = "
          "8 x %d = %d == 92160 = 2 x 46080 = 2 x |G31|: C2 = "
          "K u zeta8 K, |K| = %d == 46080 (K = Q(i)-rational part; "
          "K = U G31 U^-1 is v783's chart theorem, cited [E])"
          % (n_proj, 8 * n_proj, 4 * n_proj),
          8 * n_proj == 92160 and 4 * n_proj == 46080)

    CZ = mk([ONE, ZE, ZE, ZE, ZE, ONE, ZE, ZE,
             ZE, ZE, ONE, ZE, ZE, ZE, ZE, MONE], 0)
    chiH = gtype(HxI)
    chiHH = gtype(mat_mul(HxI, IxH))
    chiCZ = gtype(CZ)
    check("R4.8 WITNESS PARITIES: chi(H(x)I) = %s == 1 (the missing "
          "coset = the RM-CSS zeta8 bit, v819 S4 -> v798 [E]); "
          "chi(H(x)H) = %s == 0 and chi(CZ) = %s == 0 (inside "
          "K = G31)" % (chiH, chiHH, chiCZ),
          chiH == 1 and chiHH == 0 and chiCZ == 0)
    in_group = all(canon(g) in group
                   for g in (HxI, IxH, SxI, IxS, CNOT, CZ))
    check("R4.9 sanity: all generators and CZ found in the BFS census",
          in_group)

    # ==================================================================
    section("C: controls (must fire)")
    # ==================================================================
    F22 = [(0, 0), (1, 0), (0, 1), (1, 1)]
    f2_mul = lambda p, q: F22.index(((F22[p][0] * F22[q][0]) % 2,
                                     (F22[p][1] * F22[q][1]) % 2))
    f2_add = lambda p, q: F22.index(((F22[p][0] + F22[q][0]) % 2,
                                     (F22[p][1] + F22[q][1]) % 2))
    n_iso_split = count_ring_isos(f2_mul, f2_add, 0, 3)
    check("C1 the SPLIT ring F2 x F2 admits %d == 0 ring isos with "
          "Z[i]/(2) (all 24 bijections fail): 2 must ramify"
          % n_iso_split, n_iso_split == 0)

    n_eq_split = sum(1 for choice in itertools.product(*fibers)
                     if all(s == s for s in choice))
    check("C2 SPLIT self-extension (eps' = 0, deck = identity) admits "
          "%d/65536 equivariant sections (vs 0 for the ramified jet): "
          "non-splitness is contentful" % n_eq_split,
          n_eq_split == 65536)

    Ebad = [[0] * 8 for _ in range(8)]
    Ebad[0][1] = 1
    Ebad[0][2] = 1
    Ebad[1][3] = 1

    def Ebad_apply(cbits):
        out = 0
        for c in range(8):
            if (cbits >> c) & 1:
                for r in range(8):
                    if Ebad[r][c]:
                        out ^= (1 << r)
        return out

    im_bad = {Ebad_apply(w) for w in range(256)}
    ker_bad = [w for w in range(256) if Ebad_apply(w) == 0]
    check("C3 scrambled E' (|im| = %d, |ker| = %d): ker != im and "
          "E'^2 != 0 -- the self-dual differential-code structure dies"
          % (len(im_bad), len(ker_bad)),
          set(ker_bad) != im_bad
          and any(Ebad_apply(Ebad_apply(w)) for w in range(256)))

    # ==================================================================
    n_all = len(checks)
    n_fail = n_all - sum(checks)
    verdict = (EXPECTED_VERDICT if n_fail == 0
               else "RAMIFICATION-BROKEN")
    print("\nv833: %d/%d checks passed, %d failed  (%.1f s)"
          % (n_all - n_fail, n_all, n_fail, time.time() - t_start))
    print("VERDICT: %s" % verdict)
    pattern_ok = verdict == EXPECTED_VERDICT
    print("[%s] PATTERN GATE: expected verdict %s"
          % ("PASS" if pattern_ok else "FAIL", EXPECTED_VERDICT))
    return n_fail + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
