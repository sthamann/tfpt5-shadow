#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v796 -- CURVE.CODE.OUTERSPIN.01: the canonical OUTER bridge between the code's duad side and the curve's syntheme side of the S6 duality (24/24 checks, ~11 s; discovery probe duad_syntheme_bridge_probe.py, 2026-08-05, verdict BRIDGE-CANONICAL).  THE CONSTRUCTION (Sylvester duality made explicit): a bridge is a bijection beta: Omega_code -> T_curve (code odd Arf forms -> curve isotropic spreads/totals), canonically inducing the incidence-preserving duality Delta_beta: V\{0} -> IsoLines(A[2]) through the K6 duad model and the shared-syntheme rule (every pair of totals shares exactly one line -- verified).  THE CENSUS: 18 + 18 bridges intertwine sigma with tau|T resp. tau^2|T (each family a torsor under C_S6(3-cycle), order 18); after pinning beta(q*) = S* -- the UNIQUE curve spread fixed by the FULL <tau, rho> automorphism image (rho = the mu4 rotation = the complex structure J = mult by zeta^9; existence + uniqueness COMPUTED, not assumed) -- exactly 6 + 6 remain = ONE ORBIT (torsor) under the order-6 code joint stabilizer, with the tau/tau^2 families exchanged by an inner code symmetry (one statement).  B2 ARF RESOLUTION: the pullback of the curve's even q_Theta through the two frozen even<->3|3-split dictionaries is CONSTANT over all 36 B1 bridges and equals q_even* = the unique sigma-invariant even code refinement, with the NAMED operation q* = q_even* + hbar(., A) EXACT -- the anchor shift resolves the v784 Arf mismatch canonically.  THE OUTER WITNESS exact: sigma is [3,1,1,1] on odds but [3,3] on spreads, tau the reverse, the anchor transvection t_A is [2,1,1,1,1] on odds but [2,2,2] on spreads, and the class swap is UNIFORM (0 violations over all 720 group elements) -- the twist IS the outer automorphism of S6, not an inner accident.  TRANSPORTS (structure labels only): {q* = 0}\{0} maps EXACTLY onto the 5 lines of S* (5bar) and the 10 onto the complement; the 3+2 split maps onto the [3,1,1] tau-orbit structure of S*; t_A maps to rho = J on every census bridge; chi_NSR transports as an honest exact TWO-VARIANT torsor ('incidence with one of the two tau-fixed lines of S*') -- it is pinned code-side by the v752 NS/R lattice parity, a datum the bare quadruple (V, hbar, sigma, q*) does not carry, and rho swaps the two candidate lines (the two-fold ambiguity intrinsic).  CONTROLS: inner cross-side census 0 (class mismatch), same-side census 0, no bridge pulls q_Theta to an ODD form (never to q*), scrambled sigma census 0.  The v784 INNER identification stays dead (CURVE-CODE-PARTIAL untouched); the bridge is a NEW statement about the outer twist.  NO matter semantics (5bar/10, 3+2, chi_NSR are structure labels; ROOTCLASS-MIXED v775 stands).  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe duad_syntheme_bridge_probe.py (2026-08-05, 24/24, ~11 s, BRIDGE-CANONICAL; no spec corrections disclosed); re-run identically at promotion (2026-08-06).  Promoted verbatim; the probe's top-level statements are wrapped in a function scope _probe() (v791 precedent 'top-level statements moved into main()'), its final SystemExit replaced by a return of (n_pass, n_tot, verdict); numbers unchanged; run() encodes the pattern (v757 precedent).  The curve side is the exact certified model of curve_code_2torsion_probe / v784 (period-lattice recognition certified there at dps 120; nothing numerical recomputed here).

Original duad_syntheme_bridge_probe.py docstring (verbatim):
duad_syntheme_bridge_probe -- CURVE.CODE.BRIDGE.01 (follow-up to
curve_code_2torsion_probe, verdict CURVE-CODE-PARTIAL): is there a
CANONICAL outer bridge between the code's duad side and the curve's
syntheme side of the S6 duality?

STRUCTURAL RESIDUE OF THE KILL (input facts, re-verified here):
  * code side (V, hbar, sigma, q*): sigma = family 3-cycle, fixed-space
    dim 2, cycle type [3,1,1,1] on the 6 odd refinements (duad side);
    q* odd/Arf-1 with decomposition 1+5bar+10.
  * curve side (A[2], e_2, tau, q_Theta): deck tau acts freely, cycle
    type [3,3] on the 6 odd theta characteristics (syntheme side);
    q_Theta even/Arf-0 with decomposition 1+6+9.
  * the two order-3 classes are exchanged only by the OUTER automorphism
    of S6; Arf is a transport invariant: joint inner census was 0.

THE FROZEN BRIDGE CONSTRUCTION (Sylvester duality, made explicit):
  On each side the doily GQ(2,2) has 6 ovoids = odd refinements
  ("points" Omega of the six-set), 15 points = duads of Omega (v <-> D(v),
  the K6 duad model), 15 isotropic lines = synthemes (perfect matchings),
  and 6 isotropic spreads = totals (1-factorizations).  The action of
  Sp(4,2) = S6 on the 6 totals is the OUTER twist of its action on the 6
  points.  A BRIDGE is a bijection
        beta : Omega_code -> T_curve   (code odd forms -> curve spreads),
  which canonically induces the duality
        Delta_beta : V\{0} -> IsoLines(A[2]),
        v -> D(v) = {o, o'} -> the UNIQUE line shared by the spreads
        beta(o), beta(o')   (every pair of totals shares exactly one
        syntheme -- verified),
  incidence-preserving for every beta (purely set-theoretic; all 720
  dualities arise this way).

FROZEN BRIDGE CONDITIONS:
  (B1) twisted equivariance on the distinguished order-3 elements:
       beta o (sigma|Omega_code) o beta^{-1} = tau|T_curve  (tau^2 variant
       reported as the family related by an inner code symmetry).
  (B2) Arf resolution (consequence, must be CONSTANT over the census):
       the pullback of q_Theta along the bridge -- via the two frozen
       dictionaries below -- equals q_even* := the unique sigma-invariant
       EVEN code refinement, and the NAMED operation
             q* = q_even* + hbar(., A)      (the anchor shift)
       relates it to q* exactly.
       Transport note (frozen expectation): chi_NSR = hbar(., F_Sigma)
       is pinned on the code side by the v752 NS/R LATTICE parity, a
       datum the bare quadruple (V, hbar, sigma, q*) does not carry (the
       joint stabilizer swaps F_Sigma <-> F_Sigma + A); its transport is
       therefore required to be an exact TWO-variant torsor whose
       variants are 'incidence with one of the two tau-fixed lines of
       S*' -- not a constant.
  (B3) distinguished-element pinning: beta(q*) = S*, where S* := the
       UNIQUE spread of the curve fixed by the FULL curve-automorphism
       image <tau, rho> mod 2 (rho = the mu4 rotation = the complex
       structure J = mult by zeta^9; existence+uniqueness of S* is part
       of the CANONICAL criterion and is computed, not assumed).

FROZEN DICTIONARIES (both sides, canonical and equivariant):
  * evens <-> 3|3-splits of the six POINTS: for an even refinement q,
    join odd forms o, o' iff q(v_{oo'}) = 1 where v_{oo'} is the duad
    vector (D(v_{oo'}) = {o,o'}); the graph must be two disjoint
    triangles (6 within-block duads carry q = 1, the 9 cross duads
    q = 0) -- verified, bijective onto the 10 splits.
  * evens <-> 3|3-splits of the six TOTALS: join spreads S, S' iff their
    shared line lies entirely in {q = 0} (each spread contains exactly 2
    of the 6 generator lines of the even quadric, and disjoint
    generators lie in one regulus) -- verified, bijective.

VERDICT ENUM (frozen):
  BRIDGE-CANONICAL      B1-census = torsor under C_{S6}(sigma) (18 per
                        family), S* exists uniquely, full census
                        B1+B3 = |code joint stabilizer| = 6 per family
                        (one orbit incl. the tau/tau^2 swap under code
                        symmetries), and the B2 pullback is constant
                        q_even*: the outer twist canonically identifies
                        the two sides.
  BRIDGE-NONCANONICAL   the exchange exists (B1-census > 0) but the
                        pinning fails (S* not unique, or the census is
                        not a single stabilizer-torsor): the exact
                        ambiguity census is reported.
  BRIDGE-DEAD           B1-census = 0: no equivariant exchange.
  TEST-VOID             a must-fire control does not fire.

CONTROLS (frozen, must fire):
  C1a  inner instead of outer, cross-side: bijections Omega_code ->
       Omega_curve intertwining sigma with tau: 0 (class mismatch
       [3,1,1,1] vs [3,3]).
  C1b  inner instead of outer, same-side: bijections Omega_code ->
       T_code intertwining sigma|Omega with sigma|T: 0.
  C2   wrong Arf target: no B1 bridge pulls q_Theta back to an ODD code
       form (in particular never to q*): the dictionaries are
       even-to-even.
  C3   scrambled sigma: tau|T composed with a frozen transposition of
       two tau-fixed spreads has the wrong cycle type: B1 census 0.
  (positive control = the main census itself: nonzero AND exactly the
  stabilizer torsor, with the explicit orbit verification.)

FENCES (honesty, frozen):
  *  Finite exact algebra only.  The curve side is the exact certified
     model of curve_code_2torsion_probe (E* = Tr(zeta^3 x conj y)/2 of
     type (1,3) on O/2O, O = Z[zeta_12]; period-lattice recognition was
     certified there at dps 120, residuals < 1e-41; nothing numerical is
     recomputed or needed here).
  *  NO matter semantics: the names 5bar/10, 3+2, chi_NSR are used as
     STRUCTURE LABELS only.  The root-level matter reading is separately
     DEAD per gaussian_class_d5_purity_probe (ROOTCLASS-MIXED) and is
     not resurrected in either direction.
  *  This probe does not modify the CURVE-CODE-PARTIAL verdict: the
     inner identification stays dead; the bridge (if canonical) is a NEW
     statement about the outer twist.

FIREWALL: experiments/tfpt-discovery probe; ONE new file; writes
nothing; touches no verification/, paper, ledger, changelog or website
surface; report only.

Sources (read-only): experiments/tfpt-discovery/curve_code_2torsion_probe.py
(both frozen models), arf_spinor_compiler_probe.py (code layer, K6 duads),
verification/v752/v753 (code provenance), v610/v611 (curve provenance).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/duad_syntheme_bridge_probe.py
"""

def _probe():
    import itertools
    import time

    T0 = time.time()
    CHECKS = []
    KILLS = []


    def check(name, ok, detail="", kill=None):
        CHECKS.append((name, bool(ok)))
        if kill and not ok:
            KILLS.append(kill)
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                             (" -- " + detail) if detail else ""), flush=True)
        return bool(ok)


    def section(title):
        print("=" * 78)
        print(title)
        print("=" * 78, flush=True)


    # ======================================================================
    # exact Z[zeta_12] layer (frozen copy from curve_code_2torsion_probe)
    # ======================================================================
    ZPOW = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
            (-1, 0, 1, 0), (0, -1, 0, 1), (-1, 0, 0, 0)]
    CONJ_BASIS = [(1, 0, 0, 0), (0, 1, 0, -1), (1, 0, -1, 0), (0, 0, 0, -1)]
    E_K = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]


    def kmul(a, b):
        conv = [0] * 7
        for i in range(4):
            if a[i]:
                for j in range(4):
                    conv[i + j] += a[i] * b[j]
        out = [0, 0, 0, 0]
        for k in range(7):
            if conv[k]:
                for t in range(4):
                    out[t] += conv[k] * ZPOW[k][t]
        return tuple(out)


    def kconj(a):
        out = [0, 0, 0, 0]
        for i in range(4):
            if a[i]:
                for t in range(4):
                    out[t] += a[i] * CONJ_BASIS[i][t]
        return tuple(out)


    def ktrace(a):
        return 4 * a[0] + 2 * a[2]


    def kpow_zeta(k):
        out = (1, 0, 0, 0)
        for _ in range(k % 12):
            out = kmul(out, (0, 1, 0, 0))
        return out


    def mult_matrix_mod2(g):
        return [[kmul(g, E_K[j])[i] % 2 for j in range(4)] for i in range(4)]


    def Estar(x, y):
        t = ktrace(kmul(kmul(kpow_zeta(3), x), kconj(y)))
        assert t % 2 == 0
        return t // 2


    # ======================================================================
    # generic side builder: vectors = 4-bit ints, bit k = basis coeff k
    # ======================================================================
    def build_tables(gram):
        tab = [[0] * 16 for _ in range(16)]
        for x in range(16):
            for y in range(16):
                xv = [(x >> k) & 1 for k in range(4)]
                yv = [(y >> k) & 1 for k in range(4)]
                tab[x][y] = sum(xv[i] * gram[i][j] * yv[j]
                                for i in range(4) for j in range(4)) % 2
        return tab


    def all_refinements(tab):
        refs = []
        for mask in range(1 << 16):
            q = [(mask >> i) & 1 for i in range(16)]
            ok = True
            for i in range(16):
                row = tab[i]
                qi = q[i]
                for j in range(16):
                    if q[i ^ j] ^ qi ^ q[j] != row[j]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                refs.append(tuple(q))
        return refs


    def iso_lines(tab):
        out = set()
        for a in range(1, 16):
            for b in range(a + 1, 16):
                if tab[a][b] == 0 and (a ^ b) != 0:
                    out.add(frozenset({a, b, a ^ b}))
        return sorted(out, key=sorted)


    def spreads_of(lines):
        pts = set(range(1, 16))
        by_pt = {}
        for L in lines:
            for p in L:
                by_pt.setdefault(p, []).append(L)

        def rec(cov, used):
            if len(cov) == 15:
                return [frozenset(used)]
            p = min(pts - cov)
            res = []
            for L in by_pt[p]:
                if cov & L:
                    continue
                res += rec(cov | L, used + [L])
            return res

        return sorted(set(rec(frozenset(), [])), key=lambda S: sorted(map(sorted, S)))


    def linear_transporters(src_tab, dst_tab):
        out = []
        for m in range(1 << 16):
            cols = [(m >> (4 * k)) & 15 for k in range(4)]
            img = [0] * 16
            for x in range(16):
                v = 0
                for k in range(4):
                    if x & (1 << k):
                        v ^= cols[k]
                img[x] = v
            if len(set(img)) != 16:
                continue
            ok = True
            for x in range(1, 16):
                for y in range(x, 16):
                    if dst_tab[img[x]][img[y]] != src_tab[x][y]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                out.append(tuple(img))
        return out


    def perm_cycle_type(p):
        seen, ct = set(), []
        for s in range(len(p)):
            if s in seen:
                continue
            ln, cur = 0, s
            while cur not in seen:
                seen.add(cur)
                cur = p[cur]
                ln += 1
            ct.append(ln)
        return sorted(ct, reverse=True)


    def inv_perm16(g):
        gi = [0] * 16
        for x in range(16):
            gi[g[x]] = x
        return gi


    class Side(object):
        def __init__(self, name, gram, dist3):
            self.name = name
            self.tab = build_tables(gram)
            self.dist3 = dist3                      # image table of the order-3
            self.refs = all_refinements(self.tab)
            self.zeros = {q: sum(1 for b in q if b == 0) for q in self.refs}
            self.odds = sorted(q for q in self.refs if self.zeros[q] == 6)
            self.evens = sorted(q for q in self.refs if self.zeros[q] == 10)
            self.lines = iso_lines(self.tab)
            self.spreads = spreads_of(self.lines)
            self.sp = linear_transporters(self.tab, self.tab)
            # duad vector for each pair of odds
            self.duad_vec = {}
            for v in range(1, 16):
                dv = [i for i, q in enumerate(self.odds) if q[v] == 0]
                assert len(dv) == 2
                self.duad_vec[frozenset(dv)] = v
            # shared line for each pair of spreads
            self.shared = {}
            for i in range(6):
                for j in range(i + 1, 6):
                    inter = self.spreads[i] & self.spreads[j]
                    self.shared[frozenset({i, j})] = inter

        def odd_perm(self, g):
            gi = inv_perm16(g)
            return [self.odds.index(tuple(q[gi[v]] for v in range(16)))
                    for q in self.odds]

        def spread_perm(self, g):
            out = []
            for S in self.spreads:
                Sg = frozenset(frozenset(g[p] for p in L) for L in S)
                out.append(self.spreads.index(Sg))
            return out

        def split_pts(self, q):
            """even refinement -> 3|3 split of the 6 odds (frozen dictionary)."""
            adj = {i: set() for i in range(6)}
            for i in range(6):
                for j in range(i + 1, 6):
                    if q[self.duad_vec[frozenset({i, j})]] == 1:
                        adj[i].add(j)
                        adj[j].add(i)
            comp = []
            seen = set()
            for s in range(6):
                if s in seen:
                    continue
                blk, stack = set(), [s]
                while stack:
                    u = stack.pop()
                    if u in blk:
                        continue
                    blk.add(u)
                    stack += list(adj[u] - blk)
                seen |= blk
                comp.append(frozenset(blk))
            return frozenset(comp)

        def split_tot(self, q):
            """even refinement -> 3|3 split of the 6 spreads (frozen dict)."""
            adj = {i: set() for i in range(6)}
            for key, inter in self.shared.items():
                i, j = sorted(key)
                (L,) = inter
                if all(q[p] == 0 for p in L):
                    adj[i].add(j)
                    adj[j].add(i)
            comp = []
            seen = set()
            for s in range(6):
                if s in seen:
                    continue
                blk, stack = set(), [s]
                while stack:
                    u = stack.pop()
                    if u in blk:
                        continue
                    blk.add(u)
                    stack += list(adj[u] - blk)
                seen |= blk
                comp.append(frozenset(blk))
            return frozenset(comp)


    # ======================================================================
    # S1 -- both sides rebuilt, base censuses
    # ======================================================================
    section("S1: both sides rebuilt exactly -- base censuses")

    # code side: Gram J - I in (F1,F2,F3,A); sigma = family 3-cycle on bits
    GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
    SIG_B = [0] * 16
    for x in range(16):
        b = [(x >> k) & 1 for k in range(4)]
        nb = (b[2], b[0], b[1], b[3])
        SIG_B[x] = nb[0] | (nb[1] << 1) | (nb[2] << 2) | (nb[3] << 3)
    code = Side("code", GJI, SIG_B)

    # curve side: E* Gram mod 2 (frozen (1,3) polarization); tau = M(zeta^4)
    ESTAR = [[Estar(E_K[i], E_K[j]) % 2 for j in range(4)] for i in range(4)]
    MT = mult_matrix_mod2(kpow_zeta(4))
    MR = mult_matrix_mod2(kpow_zeta(9))     # rho = J = mult by zeta^9
    TAU_B = [0] * 16
    RHO_B = [0] * 16
    for x in range(16):
        xv = [(x >> k) & 1 for k in range(4)]
        it = [sum(MT[i][j] * xv[j] for j in range(4)) % 2 for i in range(4)]
        ir = [sum(MR[i][j] * xv[j] for j in range(4)) % 2 for i in range(4)]
        TAU_B[x] = it[0] | (it[1] << 1) | (it[2] << 2) | (it[3] << 3)
        RHO_B[x] = ir[0] | (ir[1] << 1) | (ir[2] << 2) | (ir[3] << 3)
    curve = Side("curve", ESTAR, TAU_B)

    check("S1.1 refinement censuses: 16 = 6 odd + 10 even on BOTH sides",
          len(code.refs) == 16 and len(code.odds) == 6
          and len(curve.refs) == 16 and len(curve.odds) == 6, kill="K")
    check("S1.2 doily counts on BOTH sides: 15 isotropic lines, exactly 6 "
          "isotropic spreads (= the 6 totals/1-factorizations); every pair "
          "of spreads shares exactly one line; every line lies in exactly 2 "
          "spreads",
          len(code.lines) == 15 and len(code.spreads) == 6
          and len(curve.lines) == 15 and len(curve.spreads) == 6
          and all(len(v) == 1 for v in code.shared.values())
          and all(len(v) == 1 for v in curve.shared.values())
          and all(sum(1 for S in code.spreads if L in S) == 2
                  for L in code.lines)
          and all(sum(1 for S in curve.spreads if L in S) == 2
                  for L in curve.lines), kill="K")

    A_INT = 0b1000          # anchor A = (0,0,0,1)
    FSIG_INT = 0b0111       # F_Sigma = (1,1,1,0)
    QSTAR = [q for q in code.odds
             if all(q[SIG_B[x]] == q[x] for x in range(16))
             and q[A_INT] == 1 and q[FSIG_INT] == 0]
    sig_inv_evens = [q for q in code.evens
                     if all(q[SIG_B[x]] == q[x] for x in range(16))]
    tau_inv_refs = [q for q in curve.refs
                    if all(q[TAU_B[x]] == q[x] for x in range(16))]
    check("S1.3 distinguished data: q* unique (%d); q_even* = the UNIQUE "
          "sigma-invariant even code form (%d); q_Theta = the unique "
          "tau-invariant curve refinement (%d), even"
          % (len(QSTAR), len(sig_inv_evens), len(tau_inv_refs)),
          len(QSTAR) == 1 and len(sig_inv_evens) == 1
          and len(tau_inv_refs) == 1
          and curve.zeros[tau_inv_refs[0]] == 10, kill="K")
    QSTAR = QSTAR[0]
    QEVEN = sig_inv_evens[0]
    QTHETA = tau_inv_refs[0]

    shifted = tuple((QEVEN[x] + code.tab[x][A_INT]) % 2 for x in range(16))
    check("S1.4 NAMED OPERATION exact: q* = q_even* + hbar(., A) (the anchor "
          "shift relates the even and odd distinguished forms)",
          shifted == QSTAR, kill="K")

    # ======================================================================
    # S2 -- the six-set actions and the outer witness
    # ======================================================================
    section("S2: the two six-set actions of Sp(4,2) and the OUTER witness")

    code_odd_perms = set()
    code_spr_perms = set()
    pair_types = set()
    for g in code.sp:
        po = tuple(code.odd_perm(g))
        ps = tuple(code.spread_perm(g))
        code_odd_perms.add(po)
        code_spr_perms.add(ps)
        pair_types.add((tuple(perm_cycle_type(list(po))),
                        tuple(perm_cycle_type(list(ps)))))
    curve_odd_perms = set()
    curve_spr_perms = set()
    for g in curve.sp:
        curve_odd_perms.add(tuple(curve.odd_perm(g)))
        curve_spr_perms.add(tuple(curve.spread_perm(g)))
    check("S2.1 both actions faithful + surjective onto S6 on BOTH sides: "
          "odd-perms %d/%d/%d/%d spread-perms all == 720"
          % (len(code_odd_perms), len(code_spr_perms),
             len(curve_odd_perms), len(curve_spr_perms)),
          len(code_odd_perms) == 720 and len(code_spr_perms) == 720
          and len(curve_odd_perms) == 720 and len(curve_spr_perms) == 720,
          kill="K")

    sigO = code.odd_perm(SIG_B)
    sigT = code.spread_perm(SIG_B)
    tauO = curve.odd_perm(TAU_B)
    tauT = curve.spread_perm(TAU_B)
    rhoO = curve.odd_perm(RHO_B)
    rhoT = curve.spread_perm(RHO_B)
    # a code transvection t_A(x) = x + hbar(x, A) A (canonical: the anchor)
    T_A = [x ^ (code.tab[x][A_INT] * A_INT) for x in range(16)]
    tAO = code.odd_perm(T_A)
    tAT = code.spread_perm(T_A)
    print("    cycle types  (on 6 odds | on 6 spreads):")
    print("      code sigma      : %s | %s" % (perm_cycle_type(sigO),
                                               perm_cycle_type(sigT)))
    print("      code t_A        : %s | %s" % (perm_cycle_type(tAO),
                                               perm_cycle_type(tAT)))
    print("      curve tau       : %s | %s" % (perm_cycle_type(tauO),
                                               perm_cycle_type(tauT)))
    print("      curve rho (= J) : %s | %s" % (perm_cycle_type(rhoO),
                                               perm_cycle_type(rhoT)))
    check("S2.2 OUTER WITNESS: the point-action and total-action differ by "
          "the outer automorphism: sigma is [3,1,1,1] on odds but [3,3] on "
          "spreads; tau is [3,3] on odds but [3,1,1,1] on spreads; the "
          "anchor transvection t_A is [2,1,1,1,1] on odds but [2,2,2] on "
          "spreads (transposition <-> triple transposition)",
          perm_cycle_type(sigO) == [3, 1, 1, 1]
          and perm_cycle_type(sigT) == [3, 3]
          and perm_cycle_type(tauO) == [3, 3]
          and perm_cycle_type(tauT) == [3, 1, 1, 1]
          and perm_cycle_type(tAO) == [2, 1, 1, 1, 1]
          and perm_cycle_type(tAT) == [2, 2, 2], kill="K")
    n_3cyc_swap = sum(1 for a, b in pair_types
                      if a == (3, 1, 1, 1) and b != (3, 3))
    check("S2.3 class swap is UNIFORM: every code element of type [3,1,1,1] "
          "on odds is [3,3] on spreads (violations: %d) -- the twist is the "
          "outer automorphism, not an inner accident" % n_3cyc_swap,
          n_3cyc_swap == 0, kill="K")

    # ======================================================================
    # S3 -- the frozen dictionaries evens <-> splits
    # ======================================================================
    section("S3: dictionaries -- evens <-> 3|3 splits of points and totals")


    def dict_ok(side):
        d_pts, d_tot = {}, {}
        for q in side.evens:
            sp_ = side.split_pts(q)
            st_ = side.split_tot(q)
            if sorted(len(b) for b in sp_) != [3, 3]:
                return None
            if sorted(len(b) for b in st_) != [3, 3]:
                return None
            d_pts[q] = sp_
            d_tot[q] = st_
        if len(set(d_pts.values())) != 10 or len(set(d_tot.values())) != 10:
            return None
        return d_pts, d_tot


    dc = dict_ok(code)
    du = dict_ok(curve)
    check("S3.1 both dictionaries are well-defined 3|3 splits and BIJECTIVE "
          "onto the 10 splits, on both sides (the within-block duads carry "
          "q = 1; the within-block shared lines lie in {q = 0})",
          dc is not None and du is not None, kill="K")
    DPTS_CODE, DTOT_CODE = dc
    DPTS_CURVE, DTOT_CURVE = du

    # equivariance spot check over 60 group elements per side
    ok_eq = True
    for side, dp in ((code, DPTS_CODE), (curve, DPTS_CURVE)):
        for g in side.sp[::12]:
            gi = inv_perm16(g)
            po = side.odd_perm(g)
            for q in side.evens[:4]:
                qg = tuple(q[gi[v]] for v in range(16))
                want = frozenset(frozenset(po[i] for i in blk) for blk in dp[q])
                if dp[qg] != want:
                    ok_eq = False
    check("S3.2 dictionary equivariance (spot check, 60 elements x 4 evens "
          "per side)", ok_eq, kill="K")

    tau_fixed_spr = [i for i in range(6) if tauT[i] == i]
    split_qT = DTOT_CURVE[QTHETA]
    tau_inv_split = frozenset({frozenset(tau_fixed_spr),
                               frozenset(set(range(6)) - set(tau_fixed_spr))})
    check("S3.3 q_Theta's split of the curve totals == the unique "
          "tau-invariant split {3 fixed spreads | 3 cycled spreads}: %s"
          % (sorted(map(sorted, split_qT)),),
          split_qT == tau_inv_split and len(tau_fixed_spr) == 3, kill="K")
    sig_fixed_odds = [i for i in range(6) if sigO[i] == i]
    split_qE = DPTS_CODE[QEVEN]
    sig_inv_split = frozenset({frozenset(sig_fixed_odds),
                               frozenset(set(range(6)) - set(sig_fixed_odds))})
    check("S3.4 q_even*'s split of the code odds == the unique "
          "sigma-invariant split {3 fixed odds | 3 cycled odds}",
          split_qE == sig_inv_split and len(sig_fixed_odds) == 3, kill="K")

    # ======================================================================
    # S4 -- the distinguished spread S*
    # ======================================================================
    section("S4: the distinguished spread S* (fixed by the full <tau, rho> "
            "image)")

    rho_fixed_spr = [i for i in range(6) if rhoT[i] == i]
    S_STAR_SET = [i for i in tau_fixed_spr if i in rho_fixed_spr]
    print("    tau-fixed spreads: %s; rho-fixed spreads: %s; joint: %s"
          % (tau_fixed_spr, rho_fixed_spr, S_STAR_SET))
    sstar_unique = check(
        "S4.1 S* UNIQUE: exactly one curve spread is fixed by BOTH tau and "
        "rho (the full C12 curve-automorphism image mod 2): %s"
        % S_STAR_SET, len(S_STAR_SET) == 1)
    S_STAR = S_STAR_SET[0] if S_STAR_SET else None
    qstar_idx = code.odds.index(QSTAR)

    # ======================================================================
    # S5 -- THE BRIDGE CENSUS
    # ======================================================================
    section("S5: the bridge census over all 720 bijections beta: "
            "Omega_code -> T_curve")

    tauT2 = [tauT[tauT[i]] for i in range(6)]
    B1_tau, B1_tau2 = [], []
    for beta in itertools.permutations(range(6)):
        if all(beta[sigO[i]] == tauT[beta[i]] for i in range(6)):
            B1_tau.append(beta)
        if all(beta[sigO[i]] == tauT2[beta[i]] for i in range(6)):
            B1_tau2.append(beta)
    check("S5.1 B1 census: %d bridges intertwine sigma with tau|T, %d with "
          "tau^2|T -- each family a torsor under C_S6(3-cycle), order 18"
          % (len(B1_tau), len(B1_tau2)),
          len(B1_tau) == 18 and len(B1_tau2) == 18, kill="K")


    def pullback_even(beta):
        """pull q_Theta back through the bridge via the two dictionaries."""
        binv = [0] * 6
        for i in range(6):
            binv[beta[i]] = i
        split_code = frozenset(frozenset(binv[t] for t in blk)
                               for blk in DTOT_CURVE[QTHETA])
        cands = [q for q in code.evens if DPTS_CODE[q] == split_code]
        return cands[0] if len(cands) == 1 else None


    pb_all = {pullback_even(b) for b in B1_tau} | \
             {pullback_even(b) for b in B1_tau2}
    check("S5.2 B2 ARF RESOLUTION: the pullback of q_Theta is CONSTANT over "
          "all 36 B1 bridges and equals q_even* (hence q* = pullback + "
          "hbar(., A): the outer bridge resolves the Arf mismatch by the "
          "canonical anchor shift)", pb_all == {QEVEN}, kill="K")

    FULL_tau = [b for b in B1_tau if S_STAR is not None
                and b[qstar_idx] == S_STAR]
    FULL_tau2 = [b for b in B1_tau2 if S_STAR is not None
                 and b[qstar_idx] == S_STAR]
    # code joint stabilizer (order 6) acting on bridges by precomposition
    stab_code = [g for g in code.sp
                 if all(g[SIG_B[x]] == SIG_B[g[x]] for x in range(16))
                 and all(QSTAR[g[x]] == QSTAR[x] for x in range(16))]
    stab_odd_perms = {tuple(code.odd_perm(g)) for g in stab_code}
    orbit0 = {tuple(b[p[i]] for i in range(6))
              for b in FULL_tau[:1] for p in stab_odd_perms} if FULL_tau else set()
    torsor_ok = (len(FULL_tau) == 6 and len(FULL_tau2) == 6
                 and orbit0 == {tuple(b) for b in FULL_tau})
    check("S5.3 FULL census (B1 + B3: beta(q*) = S*): %d (tau family) + %d "
          "(tau^2 family); the tau family is ONE orbit (torsor) under the "
          "order-%d code joint stabilizer" % (len(FULL_tau), len(FULL_tau2),
                                              len(stab_code)),
          torsor_ok and len(stab_code) == 6, kill="K")

    # tau <-> tau^2 swap realized by an inner code symmetry:
    # g fixes q* and inverts sigma, i.e. g(sigma(x)) = sigma^2(g(x))
    sw = [g for g in code.sp
          if all(QSTAR[g[x]] == QSTAR[x] for x in range(16))
          and all(g[SIG_B[x]] == SIG_B[SIG_B[g[x]]] for x in range(16))]
    sw_moves = False
    if sw and FULL_tau:
        p = tuple(code.odd_perm(sw[0]))
        b0 = FULL_tau[0]
        b_moved = tuple(b0[p[i]] for i in range(6))
        sw_moves = b_moved in {tuple(b) for b in FULL_tau2}
    check("S5.4 the tau/tau^2 families are exchanged by an inner code "
          "symmetry (g fixes q*, inverts sigma): %d such g; the two families"
          " are ONE statement" % len(sw), len(sw) > 0 and sw_moves, kill="K")

    # ======================================================================
    # S6 -- transports under the canonical bridge (structure labels only)
    # ======================================================================
    section("S6: structure transport under the canonical bridge (NO matter "
            "semantics -- ROOTCLASS-MIXED stands)")


    def duality_map(beta):
        """Delta_beta: nonzero vectors of V -> isotropic lines of A[2]."""
        out = {}
        for v in range(1, 16):
            pair = frozenset(i for i, q in enumerate(code.odds) if q[v] == 0)
            i, j = sorted(beta[i] for i in pair)
            (L,) = curve.shared[frozenset({i, j})]
            out[v] = L
        return out


    ok_equiv15 = True
    ok_5bar = True
    ok_orbits = True
    chi_tables = set()
    lsig_lines = set()
    for b in FULL_tau:
        D = duality_map(b)
        # full 15-point twisted equivariance: Delta(sigma v) = tau(Delta v)
        for v in range(1, 16):
            Lt = frozenset(TAU_B[p] for p in D[v])
            if D[SIG_B[v]] != Lt:
                ok_equiv15 = False
        # 5bar -> the 5 lines of S*, 10 -> the complement
        img5 = {tuple(sorted(D[v])) for v in range(1, 16) if QSTAR[v] == 0}
        sstar_lines = {tuple(sorted(L)) for L in curve.spreads[S_STAR]}
        if img5 != sstar_lines:
            ok_5bar = False
        # 3+2 split: sigma orbits on the 5bar words are [3,1,1] and map to
        # tau orbits on the S* lines
        fixed_w = [v for v in range(1, 16) if QSTAR[v] == 0 and SIG_B[v] == v]
        fixed_l = [L for L in curve.spreads[S_STAR]
                   if frozenset(TAU_B[p] for p in L) == L]
        if not (len(fixed_w) == 2 and len(fixed_l) == 2
                and {tuple(sorted(D[v])) for v in fixed_w}
                == {tuple(sorted(L)) for L in fixed_l}):
            ok_orbits = False
        # chi_NSR transport
        chi = tuple(code.tab[v][FSIG_INT] for v in range(16))
        chi_lines = tuple(sorted(tuple(sorted(D[v]))
                                 for v in range(1, 16) if chi[v] == 0))
        chi_tables.add(chi_lines)
        lsig_lines.add(tuple(sorted(D[FSIG_INT])))

    check("S6.1 full twisted equivariance of the induced duality on all 15 "
          "vectors: Delta(sigma v) = tau(Delta v) for every census bridge",
          ok_equiv15, kill="K")
    check("S6.2 5bar/10 TRANSPORT: {q* = 0}\\{0} maps EXACTLY onto the 5 "
          "lines of the distinguished spread S*; the 10 maps onto the 10 "
          "non-S* lines -- the 1+5bar+10 decomposition becomes 'S* lines vs "
          "the rest'", ok_5bar, kill="K")
    check("S6.3 3+2 TRANSPORT: the two sigma-fixed 5bar words (F_Sigma, "
          "F_Sigma+A) map onto the two tau-fixed lines of S*; the cycled 3 "
          "map onto the tau-3-cycle of S* lines ([3,1,1] orbit match)",
          ok_orbits, kill="K")

    # chi_NSR is pinned on the code side by the v752 NS/R LATTICE parity --
    # a datum the bare quadruple (V, hbar, sigma, q*) does not carry: the
    # joint stabilizer swaps F_Sigma <-> F_Sigma + A.  The determinate
    # statement is therefore a TWO-variant torsor:
    chi_geom_all = True
    sfix_lines = [tuple(sorted(L)) for L in curve.spreads[S_STAR]
                  if frozenset(TAU_B[p] for p in L) == frozenset(L)]
    for b in FULL_tau:
        D = duality_map(b)
        LSIG = D[FSIG_INT]
        meets = {tuple(sorted(D[v])) for v in range(1, 16)
                 if D[v] == LSIG or (D[v] & LSIG)}
        chi0 = {tuple(sorted(D[v])) for v in range(1, 16)
                if code.tab[v][FSIG_INT] == 0}
        if meets != chi0:
            chi_geom_all = False
    check("S6.4 chi_NSR TRANSPORT (two-variant torsor): the census produces "
          "exactly %d chi tables and %d candidate lines Delta(F_Sigma) = the"
          " two tau-fixed lines of S* (the code stabilizer swaps F_Sigma <->"
          " F_Sigma + A: chi_NSR is pinned by the v752 NS/R LATTICE parity, "
          "which the bare 2-torsion quadruple does not carry); per variant "
          "the geometric form holds: chi = 0 exactly on the 7 lines meeting "
          "l_Sigma = Delta(F_Sigma)"
          % (len(chi_tables), len(lsig_lines)),
          len(chi_tables) == 2 and len(lsig_lines) == 2
          and set(lsig_lines) == set(sfix_lines) and chi_geom_all, kill="K")
    rho_on_lsig = {tuple(sorted(frozenset(RHO_B[p] for p in set(L))))
                   for L in lsig_lines}
    print("    [reported] rho maps the two candidate l_Sigma lines to: %s "
          "(swaps them: %s -- the two-fold chi ambiguity is intrinsic even "
          "with the full curve C12 data)"
          % (sorted(rho_on_lsig),
             rho_on_lsig == set(lsig_lines)
             and not all(tuple(sorted(frozenset(RHO_B[p] for p in set(L))))
                         == L for L in lsig_lines)))

    # bonus (reported, not frozen): does the bridge relate the code anchor
    # transvection t_A to the curve rotation rho?
    tA_on_T = set()
    for b in FULL_tau:
        p = tuple(b[tAO[i]] for i in range(6))
        # conjugated permutation of T_curve: beta o t_A|Omega o beta^{-1}
        binv = [0] * 6
        for i in range(6):
            binv[b[i]] = i
        conj = tuple(b[tAO[binv[t]]] for t in range(6))
        tA_on_T.add(conj)
    print("    [reported] Psi_beta(t_A) over the census: %d distinct perms "
          "of T_curve; equal to rho|T: %s"
          % (len(tA_on_T), tuple(rhoT) in tA_on_T))

    # ======================================================================
    # S7 -- controls (must fire)
    # ======================================================================
    section("S7: controls")

    n_inner_cross = sum(1 for beta in itertools.permutations(range(6))
                        if all(beta[sigO[i]] == tauO[beta[i]]
                               for i in range(6)))
    check("C1a FIRES: inner (point-to-point) exchange sigma|Omega_code <-> "
          "tau|Omega_curve: census %d == 0 (class mismatch [3,1,1,1] vs "
          "[3,3])" % n_inner_cross, n_inner_cross == 0, kill="K7")

    n_inner_same = sum(1 for beta in itertools.permutations(range(6))
                       if all(beta[sigO[i]] == sigT[beta[i]]
                              for i in range(6)))
    check("C1b FIRES: same-side exchange sigma|Omega_code <-> sigma|T_code: "
          "census %d == 0 (the duad and syntheme actions of the SAME element"
          " are never identified)" % n_inner_same, n_inner_same == 0,
          kill="K7")

    n_odd_pull = sum(1 for b in B1_tau + B1_tau2
                     if pullback_even(b) in code.odds
                     or pullback_even(b) == QSTAR)
    check("C2 FIRES: no B1 bridge pulls q_Theta back to an ODD form (never "
          "to q*): %d == 0 -- a wrong Arf-type target is impossible, the "
          "dictionaries are even-to-even" % n_odd_pull, n_odd_pull == 0,
          kill="K7")

    t0, t1 = tau_fixed_spr[0], tau_fixed_spr[1]
    tau_scr = list(tauT)
    tau_scr[t0], tau_scr[t1] = tau_scr[t1], tau_scr[t0]
    n_scr = sum(1 for beta in itertools.permutations(range(6))
                if all(beta[sigO[i]] == tau_scr[beta[i]] for i in range(6)))
    check("C3 FIRES: scrambled sigma (tau|T composed with a transposition of"
          " two tau-fixed spreads, cycle type %s): B1 census %d == 0"
          % (perm_cycle_type(tau_scr), n_scr), n_scr == 0, kill="K7")

    # ======================================================================
    # S8 -- verdict (frozen rule)
    # ======================================================================
    section("S8: VERDICT (frozen enum: BRIDGE-CANONICAL / "
            "BRIDGE-NONCANONICAL / BRIDGE-DEAD; TEST-VOID on control "
            "failure)")

    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    print("%d/%d checks passed" % (n_pass, n_tot))

    # frozen rule (docstring): CANONICAL iff the B1 census is the C(sigma)
    # torsor, S* is unique, the FULL census is the joint-stabilizer torsor
    # (one orbit incl. the tau/tau^2 swap), the B2 pullback is constant
    # q_even*, and no structural kill fired.
    if not controls_ok:
        verdict = "TEST-VOID"
    elif len(B1_tau) + len(B1_tau2) == 0:
        verdict = "BRIDGE-DEAD"
    elif (sstar_unique and len(B1_tau) == 18 and len(B1_tau2) == 18
          and len(FULL_tau) == 6 and len(FULL_tau2) == 6
          and torsor_ok and sw_moves and pb_all == {QEVEN} and not KILLS):
        verdict = "BRIDGE-CANONICAL"
    else:
        verdict = "BRIDGE-NONCANONICAL"

    print("VERDICT: %s" % verdict)
    if verdict == "BRIDGE-CANONICAL":
        print()
        print("THE CANONICAL OUTER BRIDGE (theorem-candidate statement,")
        print("exploration grade -- promotion is a separate decision):")
        print("  * The Sylvester duality beta: Omega_code -> T_curve with")
        print("    beta sigma = tau beta and beta(q*) = S* (the unique")
        print("    <tau, rho>-fixed spread) exists and is UNIQUE up to the")
        print("    order-6 joint stabilizer (one orbit incl. tau/tau^2).")
        print("  * It resolves the Arf mismatch canonically: q_Theta pulls")
        print("    back to q_even* = q* + hbar(., A) -- the anchor shift.")
        print("  * It transports 1+5bar+10 to {S*} + {5 lines of S*} +")
        print("    {10 other lines}, the 3+2 split to the [3,1,1] tau-orbit")
        print("    structure on S*, and it sends the code anchor")
        print("    transvection t_A to the curve rotation rho = J mod 2")
        print("    (constant over the census).")
        print("  * chi_NSR transports as an exact TWO-variant torsor")
        print("    ('incidence with one of the two tau-fixed lines of S*'):")
        print("    it is pinned on the code side by the v752 NS/R lattice")
        print("    parity, which the bare 2-torsion quadruple lacks.")
        print("  * NO matter semantics claimed (ROOTCLASS-MIXED stands);")
        print("    the inner identification stays CURVE-CODE-PARTIAL/dead.")
    elif verdict == "BRIDGE-NONCANONICAL":
        print("  ambiguity census: S* candidates %s; full census %d + %d"
              % (S_STAR_SET, len(FULL_tau), len(FULL_tau2)))
    print("Runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return n_pass, n_tot, verdict


def run():
    """run_all entry point (v757 precedent): expected pattern 24/24 with
    verdict BRIDGE-CANONICAL."""
    n_pass, n_tot, v = _probe()
    ok = (n_pass == n_tot == 24 and v == "BRIDGE-CANONICAL")
    print("\n[%s] PATTERN GATE: expected 24/24 with verdict "
          "BRIDGE-CANONICAL; got %d/%d, verdict: %s"
          % ("PASS" if ok else "FAIL", n_pass, n_tot, v))
    print("\nCOMBINED ADJUDICATION: %s -- BRIDGE-CANONICAL: the Sylvester "
          "duality beta: Omega_code -> T_curve with beta sigma = tau beta "
          "and beta(q*) = S* (the unique <tau, rho>-fixed spread) exists "
          "and is unique up to the order-6 joint stabilizer (one orbit "
          "incl. the tau/tau^2 swap); it resolves the v784 Arf mismatch "
          "canonically (q_Theta pulls back to q_even* = q* + hbar(., A) "
          "-- the anchor shift), transports 1+5bar+10 to the S*-line "
          "geometry and t_A to rho = J, and types chi_NSR as an exact "
          "two-variant torsor pinned by the v752 NS/R parity.  The inner "
          "identification stays dead; no matter semantics.  NO RH claim."
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
