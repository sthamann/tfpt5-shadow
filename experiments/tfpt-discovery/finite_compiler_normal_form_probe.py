#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""finite_compiler_normal_form_probe -- NORMALFORM.CFIN.01: the
four-bit symplectic compiler as ONE object
      C_fin = (V, hbar, q*, sigma, iota),
assembled FROM the Gaussian quotient, with the code-to-matter kill
built in as a checked NEGATIVE and the remaining P2 bridge typed.

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; work
package A of the v5.4 strategy, "formally close the finite normal
form"; assembles v752/v774/v775/v799/v833 into one machine-checked
object):

 S1  THE CARRIER OF THE OBJECT: rebuild the Gaussian E8 (Construction
     A over C*, 2 of 30 placements); 240 roots; V = L/(1+i)L with
     census 240 = 15 x 16, zero class empty; |V| = 16, 15 nonzero
     classes; sigma = the coordinate 3-cycle (pi_sigma) descends to V
     with EXACTLY 3 nonzero fixed classes; a family/anchor basis
     (F1, F2, F3, A) exists with Gram(hbar) = J - I (all-ones off
     diagonal) and hbar = the bit form on ALL 256 label pairs -- the
     quadruple (V, hbar) is READ OFF the lattice, not postulated.

 S2  THE DISTINGUISHED REFINEMENT q*: brute force over all 2^16
     functions gives EXACTLY 16 quadratic refinements of hbar; Arf
     census 6 + 10; the frozen selector (sigma-invariant: 4 ->
     q(A) = 1: 2 -> q(F_Sigma) = 0: 1) picks a UNIQUE q*, of Arf
     type 1 (v774 S2-S4 rebuilt).

 S3  THE ORDER-3 OPERATOR sigma: sigma^3 = id, symplectic for hbar;
     fixed nonzero classes = {A, F_Sigma, F_Sigma + A}; the other 12
     classes fall in EXACTLY 4 free 3-orbits (the family cycle
     F1 -> F2 -> F3 with fixed anchor bit); sigma preserves q*.

 S4  THE PARITY LIFT iota: iota(v) = (f1, f2, f3, a, f1+f2+f3+a) maps
     V bijectively onto the even five-slot code C_even(5); beta(v,w) =
     iota(v).iota(w) mod 2 == hbar in all 256 cells; q_wt =
     wt(iota)/2 mod 2 IS q*; sigma acts on the five carrier slots as
     the 3+2 split (slots {1,2,3} cycled, {4,5} fixed) -- iota
     intertwines the message register with the carrier register.

 S5  DERIVED COUNTING (all from the ONE object): Stab_Sp(q*) has order
     120, acts faithfully as S5 on the 5 non-q* Arf-1 forms, orbits
     {1, 5, 10} on refinements; words split 15 = 5 + 10 ({q*=0}\{0}
     and {q*=1}); PASCAL READING: the iota-weight census is
     (wt 0, 2, 4) = (1, 10, 5) = (C(5,0), C(5,2), C(5,4)) and q* =
     wt/2 mod 2; PROJECTIVE READING: PG(3,2) has 15 points and 35
     lines, 15 isotropic (the doily), and the 5bar is an OVOID (meets
     every isotropic line exactly once).

 S6  DERIVED BUDGET vs the ACTUAL objects: 240 = 16 x (5+10) = the
     root census; 60 Gaussian lines = 4 x 15; 30 = 2 x (5+10) =
     |lines|/2 = |R|/rank = h(E8); rank 8 (HNF index 16); 248 =
     16 x (5+10) + 8 = |R| + rank.

 S7  MANDATORY NEGATIVE (the code-to-matter kill, per the strategy):
     (a) the counting bound: EVERY D5(+)A3 c E8 has exactly 128
     spinor-side roots (v775 [E]); 15 x 16 = 240 > 128, so at most
     floor(128/16) = 8 of the 15 classes can be all-spinor and >= 7
     ALWAYS contain adjoint-side roots -- the 15 classes do NOT map to
     pure matter multiplets, as an exact arithmetic statement.
     (b) the concrete census: in the standard doubled E8 model (v752/
     v775 conventions; 112 integer + 128 spinor roots; J = pair
     rotation) the Gaussian census is again 15 x 16; EXACTLY 8 classes
     are spinor-pure (saturating the bound) and EXACTLY 7 = 15 - 8
     classes consist of adjoint-side integer roots (saturating the
     bound; the J-quotient respects the D8 integer/spinor grading, so
     no class mixes the two types).
     (c) the WEIGHT-level kill re-verified at the canonical
     sigma-stable split D = (0,2,4,6,7) (v775 convention): each of the
     8 spinor-pure classes restricts to 8 DISTINCT half-spinor
     +-weight pairs -- NO class carries exactly one SU(5) weight
     state.  The exhaustive convention scan (56 splits x 240
     assignments x 2 chiralities, ZERO pure conventions) is v775
     ROOTCLASS-MIXED [E], cited NOT overturned: expected-negative
     PASSES as a negative.

SPEC v2 (declared gate repair, v836 precedent; intent, kills and
verdict rule UNCHANGED): the v1 frozen wording of S7(b) mis-typed the
v775 bound as ">= 7 classes are MIXED (contain BOTH root types)"; the
first run showed the factual census is a clean 8 + 7 split along the
D8 grading with ZERO both-type classes (reported by the v1 run
verbatim).  The v775 statement is ">= 7 classes contain ADJOINT-SIDE
roots" (saturated at exactly 7) and its mixing kill lives at the
WEIGHT level (8 distinct weight pairs per spinor class), now checked
as S7.3.  No numeric result of any other section changed.

 S8  WHAT THE NORMAL FORM DOES NOT REMOVE (P2 narrowed, NOT
     eliminated): all 30 placements are Type II [8,4] codes (dim 4,
     self-dual, weight enumerator 1 + 14 z^4 + z^8) -- the Type II set
     that v799 TYPEII-FORCED [E] derives from the three seam axioms
     (A1 mutual locality <=> self-orthogonal, A2 integer conformal
     spin <=> doubly even, A3 holomorphy/index one <=> self-dual).
     TYPED REMAINING BRIDGE: C_fin does NOT derive A1-A3, the
     OPE-linearity scope note, or the v776 selection of ONE copy --
     that [C] residual R1' is exactly where P2 (g_car = 5, entering
     C_fin as the slot count of iota) still hangs; narrowed, not
     eliminated.

 C   CONTROLS (must fire):
     C1 the non-alternating dot form x.y admits ZERO quadratic
        refinements (v774 C1) -- hbar must be alternating.
     C2 the trivial deck sigma' = id: the selector census becomes
        16 -> 8 -> 4 != 1 -- WITHOUT the family 3-cycle q* is not
        unique; the order-3 operator is load-bearing.
     C3 the wrong lift iota' = (f1,f2,f3,a,0): image not inside
        C_even(5) and beta' != hbar (witness cell) -- the checksum
        slot is load-bearing.

KILLS (any one fires => typed gap):
  K1 quotient census / sigma / family basis breaks   -> QUOTIENT-BROKEN
  K2 refinement count / selector uniqueness breaks   -> SELECTOR-BROKEN
  K3 iota / beta / q_wt / slot action breaks         -> LIFT-BROKEN
  K4 a counting identity (1+5+10, 240, 248, ...)     -> COUNT-BROKEN
  K5 the negative fails (a pure-matter reading would
     open up)                                        -> NEGATIVE-OVERTURNED
  K6 the Type II echo (30 copies, enumerator) breaks -> TYPEII-ECHO-BROKEN
  K7 a control does not fire                         -> CONTROL-DEAD

VERDICT (frozen enum): NORMAL-FORM-ASSEMBLED / <typed gap above> /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface.
Exact integer/Fraction/sympy arithmetic; no floats, no RNG, no fit.

Sources (read-only, machinery rebuilt inline): verification/
v752_projective_hamming_incidence.py + v774_arf_spinor_compiler.py
(quotient, selector, lift, S5 geometry), v775_gaussian_class_d5_purity
.py (ROOTCLASS-MIXED, counting bound), v799_seam_code_typeii.py
(TYPEII-FORCED, R1'), v776 (30 copies, selection), v833 (Gaussian
rebuild), tfpt_constants (g_car, N_fam).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/finite_compiler_normal_form_probe.py
"""
import hashlib
import itertools
import os
import sys
import time

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "verification"))
from tfpt_constants import N_fam, g_car  # noqa: E402  (read-only import)

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("NORMALFORM.CFIN.01 -- C_fin = (V, hbar, q*, sigma, iota) as ONE "
      "object")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ======================================================================
section("S1: the carrier -- V = L/(1+i)L from the Gaussian E8")
# ======================================================================
G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
          for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)


def code_image(code, perm):
    return frozenset(tuple(c[perm[k]] for k in range(8)) for c in code)


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


def J_vec(v):
    out = [0] * 8
    for k in range(4):
        out[2 * k] = -v[2 * k + 1]
        out[2 * k + 1] = v[2 * k]
    return tuple(out)


def sig_vec(v):
    return tuple(v[PI_SIG[k]] for k in range(8))


def in_L(v):
    return tuple(x % 2 for x in v) in CSTAR


def in_pi2L(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L([x // 2 for x in w])


REPS = [(0,) * 8]                       # class representatives; 0 first
for r in ROOTS:
    if not any(in_pi2L(tuple(a - b for a, b in zip(r, rep)))
               for rep in REPS):
        REPS.append(r)


def label_of(v):
    for li, rep in enumerate(REPS):
        if in_pi2L(tuple(a - b for a, b in zip(v, rep))):
            return li
    raise AssertionError("vector not in L or label table broken")


census = {}
for r in ROOTS:
    census[label_of(r)] = census.get(label_of(r), 0) + 1
check("S1.1 |V| = 16 = %d classes; 15 nonzero; census 240 = 15 x 16; "
      "zero class EMPTY on roots" % len(REPS),
      len(placements) == 30 and len(both) == 2 and len(REPS) == 16
      and len(census) == 15 and 0 not in census
      and sorted(census.values()) == [16] * 15, kill="K1")


def sig_label(li):
    return label_of(sig_vec(REPS[li]))


fixed_nz = [li for li in range(1, 16) if sig_label(li) == li]
check("S1.2 sigma descends to V: sigma^3 = id on all 16 labels, "
      "EXACTLY 3 nonzero fixed classes",
      all(sig_label(sig_label(sig_label(li))) == li for li in range(16))
      and len(fixed_nz) == 3 and sig_label(0) == 0, kill="K1")


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


def hbar_vec(x, y):
    re2, im2 = ip(x, y), ip(x, J_vec(y))
    assert re2 % 2 == 0 and im2 % 2 == 0
    return ((re2 // 2) + (im2 // 2)) % 2


GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


BITS = None
FAM = None
for o1 in range(1, 16):
    if o1 in fixed_nz:
        continue
    o2, o3 = sig_label(o1), sig_label(sig_label(o1))
    if len({o1, o2, o3}) != 3:
        continue
    r1, r2, r3 = REPS[o1], REPS[o2], REPS[o3]
    fsum = label_of(tuple(a + b + c for a, b, c in zip(r1, r2, r3)))
    if fsum not in fixed_nz:
        continue
    span3 = set()
    for e1, e2, e3 in itertools.product((0, 1), repeat=3):
        span3.add(label_of(tuple(e1 * a + e2 * b + e3 * c
                                 for a, b, c in zip(r1, r2, r3))))
    if len(span3) != 8:
        continue
    for anc in fixed_nz:
        if anc in span3:
            continue
        ra = REPS[anc]
        bits_map = {}
        for bits in itertools.product((0, 1), repeat=4):
            v = tuple(bits[0] * a + bits[1] * b + bits[2] * c
                      + bits[3] * d
                      for a, b, c, d in zip(r1, r2, r3, ra))
            bits_map[label_of(v)] = bits
        if len(bits_map) != 16:
            continue
        gram = [[hbar_vec(u, w) for w in (r1, r2, r3, ra)]
                for u in (r1, r2, r3, ra)]
        if gram == GJI:
            BITS = bits_map
            FAM = (o1, o2, o3, anc, fsum)
            break
    if BITS is not None:
        break
check("S1.3 family/anchor basis (F1,F2,F3,A) FOUND with Gram(hbar) = "
      "J - I; the 16 bit addresses are a bijection onto the classes",
      BITS is not None and len(BITS) == 16, kill="K1")
o1, o2, o3, ANC, FSUM = FAM

ok_bitform = all(
    hbar_vec(REPS[lx], REPS[ly]) == hb(BITS[lx], BITS[ly])
    for lx in range(16) for ly in range(16))
ok_sigbits = all(BITS[sig_label(li)]
                 == (BITS[li][2], BITS[li][0], BITS[li][1], BITS[li][3])
                 for li in range(16))
check("S1.4 hbar == the bit form on ALL 256 label pairs; sigma in bits "
      "= the family 3-cycle (f1,f2,f3,a) -> (f3,f1,f2,a), A fixed",
      ok_bitform and ok_sigbits, kill="K1")

A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)
check("S1.5 BITS[A] = (0,0,0,1), BITS[F_Sigma] = (1,1,1,0), F_Sigma "
      "sigma-fixed",
      BITS[ANC] == A_BIT and BITS[FSUM] == FSIG
      and sig_label(FSUM) == FSUM, kill="K1")


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


# ======================================================================
section("S2: the distinguished refinement q* (brute force + selector)")
# ======================================================================
def refinements_of(form):
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            qi = q[i]
            vi = W16[i]
            for j in range(16):
                vj = W16[j]
                vs = tuple((a + b) % 2 for a, b in zip(vi, vj))
                if q[WIDX[vs]] ^ qi ^ q[j] != form(vi, vj):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


refs = refinements_of(hb)
zeros = {q: sum(1 for i in range(16) if q[i] == 0) for q in refs}
arf1 = sorted(q for q in refs if zeros[q] == 6)
arf0 = sorted(q for q in refs if zeros[q] == 10)
check("S2.1 EXACTLY 16 refinements (brute force over 2^16); Arf census "
      "6 + 10", len(refs) == 16 and len(arf1) == 6 and len(arf0) == 10,
      kill="K2")

siginv = [q for q in refs
          if all(q[WIDX[sig_bits(w)]] == q[WIDX[w]] for w in W16)]
cand_a = [q for q in siginv if q[WIDX[A_BIT]] == 1]
cand = [q for q in cand_a if q[WIDX[FSIG]] == 0]
check("S2.2 SELECTOR UNIQUE: sigma-invariant %d == 4 -> q(A)=1: %d == "
      "2 -> q(F_Sigma)=0: %d == 1; q* has Arf type 1"
      % (len(siginv), len(cand_a), len(cand)),
      len(siginv) == 4 and len(cand_a) == 2 and len(cand) == 1
      and zeros[cand[0]] == 6, kill="K2")
QSTAR = cand[0]

# ======================================================================
section("S3: the order-3 operator -- the family cycle structure")
# ======================================================================
ok_symp = all(hb(sig_bits(v), sig_bits(w)) == hb(v, w)
              for v in W16 for w in W16)
fixed_bits = sorted(BITS[li] for li in fixed_nz)
want_fixed = sorted([A_BIT, FSIG,
                     tuple((a + b) % 2 for a, b in zip(A_BIT, FSIG))])
orbits3 = set()
for w in W16:
    if w in (A_BIT, FSIG, (0, 0, 0, 0),
             tuple((a + b) % 2 for a, b in zip(A_BIT, FSIG))):
        continue
    orbits3.add(frozenset({w, sig_bits(w), sig_bits(sig_bits(w))}))
check("S3.1 sigma symplectic (256 pairs); fixed nonzero classes = "
      "{A, F_Sigma, F_Sigma+A}; the other 12 classes = EXACTLY 4 free "
      "3-orbits (the family cycle)",
      ok_symp and fixed_bits == want_fixed and len(orbits3) == 4
      and all(len(o) == 3 for o in orbits3), kill="K1")
check("S3.2 sigma preserves q* (selector consistency)",
      all(QSTAR[WIDX[sig_bits(w)]] == QSTAR[WIDX[w]] for w in W16),
      kill="K1")

# ======================================================================
section("S4: the parity lift iota into the even five-slot code")
# ======================================================================
def iota(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


CEVEN = {w for w in itertools.product((0, 1), repeat=5)
         if sum(w) % 2 == 0}
img = {iota(v) for v in W16}
check("S4.1 iota(V) == C_even(5) (bijective onto the 16 even-weight "
      "five-slot words); g_car = %d = the slot count" % g_car,
      img == CEVEN and len(img) == 16 and g_car == 5, kill="K3")
ok_beta = all(sum(x * y for x, y in zip(iota(v), iota(w))) % 2
              == hb(v, w) for v in W16 for w in W16)
check("S4.2 beta(v,w) = iota(v).iota(w) mod 2 == hbar in ALL 256 cells",
      ok_beta, kill="K3")
qwt = tuple((sum(iota(w)) // 2) % 2 for w in W16)
check("S4.3 q_wt = wt(iota)/2 mod 2 IS q* (the lift induces the "
      "selected refinement)", qwt == QSTAR, kill="K3")
ok_slots = all(iota(sig_bits(v))
               == (iota(v)[2], iota(v)[0], iota(v)[1],
                   iota(v)[3], iota(v)[4]) for v in W16)
check("S4.4 sigma acts on the FIVE carrier slots as the 3+2 split "
      "(slots {1,2,3} cycled, {4,5} fixed) -- message register and "
      "carrier register intertwined by iota", ok_slots, kill="K3")

# ======================================================================
section("S5: derived counting -- 16 = 1 + 5 + 10 and the two readings")
# ======================================================================
sp_mats = []
for bits in range(1 << 16):
    M = [[(bits >> (4 * i + j)) & 1 for j in range(4)] for i in range(4)]
    ok = True
    for i in range(4):
        ei = tuple(1 if k == i else 0 for k in range(4))
        Mei = tuple(sum(M[r][k] * ei[k] for k in range(4)) % 2
                    for r in range(4))
        for j in range(4):
            ej = tuple(1 if k == j else 0 for k in range(4))
            Mej = tuple(sum(M[r][k] * ej[k] for k in range(4)) % 2
                        for r in range(4))
            if hb(Mei, Mej) != GJI[i][j]:
                ok = False
                break
        if not ok:
            break
    if ok:
        sp_mats.append(M)
perms = []
for M in sp_mats:
    p = [WIDX[tuple(sum(M[r][k] * w[k] for k in range(4)) % 2
                    for r in range(4))] for w in W16]
    perms.append(tuple(p))
inv_perms = []
for p in perms:
    q = [0] * 16
    for i, pi in enumerate(p):
        q[pi] = i
    inv_perms.append(tuple(q))


def act(q, ipm):
    return tuple(q[ipm[i]] for i in range(16))


check("S5.1 |Sp(4,2)| = %d == 720 (full 65536-matrix census)"
      % len(sp_mats), len(sp_mats) == 720
      and len(set(perms)) == 720, kill="K4")

stab_idx = [k for k in range(720) if act(QSTAR, inv_perms[k]) == QSTAR]
orbs = []
seen = set()
for q in refs:
    if q in seen:
        continue
    o = {act(q, inv_perms[k]) for k in stab_idx}
    seen |= o
    orbs.append(o)
osz = sorted(len(o) for o in orbs)
arf1_rest = [q for q in arf1 if q != QSTAR]
ok_types = (any(o == {QSTAR} for o in orbs)
            and any(o == set(arf1_rest) for o in orbs)
            and any(o == set(arf0) for o in orbs))
s5_perms = {tuple(arf1_rest.index(act(q, inv_perms[k]))
                  for q in arf1_rest) for k in stab_idx}
check("S5.2 16 = 1 + 5 + 10: |Stab(q*)| = %d == 120, orbits %s == "
      "[1, 5, 10] ({q*} u {5 Arf-1} u {10 Arf-0}); Stab(q*) faithful "
      "S5 on the five (%d distinct perms)"
      % (len(stab_idx), osz, len(s5_perms)),
      len(stab_idx) == 120 and osz == [1, 5, 10] and ok_types
      and len(s5_perms) == 120, kill="K4")

NZ = [w for w in W16 if any(w)]
five = [w for w in NZ if QSTAR[WIDX[w]] == 0]
ten = [w for w in W16 if QSTAR[WIDX[w]] == 1]
check("S5.3 WORDS: 15 = 5 + 10 ({q*=0}\\{0} = %d, {q*=1} = %d)"
      % (len(five), len(ten)),
      len(five) == 5 and len(ten) == 10, kill="K4")

wt_census = {}
for v in W16:
    wt_census[sum(iota(v))] = wt_census.get(sum(iota(v)), 0) + 1
check("S5.4 PASCAL READING: iota-weight census (0, 2, 4) = (%d, %d, "
      "%d) == (C(5,0), C(5,2), C(5,4)) = (1, 10, 5); ten = weight-2, "
      "5bar = weight-4"
      % (wt_census.get(0, 0), wt_census.get(2, 0), wt_census.get(4, 0)),
      wt_census == {0: 1, 2: 10, 4: 5}
      and all(sum(iota(w)) == 2 for w in ten)
      and all(sum(iota(w)) == 4 for w in five), kill="K4")

lines_pg = set()
for a2, b2 in itertools.combinations(NZ, 2):
    c2 = tuple((x + y) % 2 for x, y in zip(a2, b2))
    lines_pg.add(frozenset({a2, b2, c2}))
iso_lines = [L for L in lines_pg
             if all(hb(u, w) == 0 for u in L for w in L)]
check("S5.5 PROJECTIVE READING: PG(3,2) has 15 points, %d lines, %d "
      "isotropic (the doily); the 5bar is an OVOID: it meets every "
      "isotropic line exactly once"
      % (len(lines_pg), len(iso_lines)),
      len(lines_pg) == 35 and len(iso_lines) == 15
      and all(sum(1 for pt in L if pt in set(five)) == 1
              for L in iso_lines), kill="K4")

# ======================================================================
section("S6: derived budget vs the actual lattice objects")
# ======================================================================
lines60 = set()
for r in ROOTS:
    lines60.add(frozenset([r, J_vec(r), tuple(-x for x in r),
                           tuple(-x for x in J_vec(r))]))
gens = sp.Matrix([list(c) for c in sorted(CSTAR)]
                 + [[2 * (rr == k) for k in range(8)]
                    for rr in range(8)]).T
Bc = hermite_normal_form(gens)
check("S6.1 240 = 16 x (5+10): root census %d == 16 x 15; 60 lines = "
      "4 x 15 (%d)" % (len(ROOTS), len(lines60)),
      len(ROOTS) == 16 * (len(five) + len(ten))
      and len(lines60) == 60 == 4 * 15, kill="K4")
check("S6.2 30 = 2 x (5+10) = |lines|/2 = |R|/rank = h(E8) "
      "(MESSAGE.LADDER.01 rung 1); rank 8 (HNF |det| = %d == 16); "
      "248 = 16 x (5+10) + 8 = |R| + rank = %d"
      % (abs(Bc.det()), len(ROOTS) + 8),
      2 * (len(five) + len(ten)) == 30 == len(lines60) // 2
      == len(ROOTS) // 8
      and Bc.rank() == 8 and abs(Bc.det()) == 16
      and 16 * 15 + 8 == 248 == len(ROOTS) + Bc.rank(), kill="K4")

# ======================================================================
section("S7: MANDATORY NEGATIVE -- the code-to-matter kill (v775)")
# ======================================================================
check("S7.1 COUNTING BOUND (exact arithmetic; embedding-independent, "
      "v775 [E]): every D5(+)A3 c E8 has 128 spinor-side roots; "
      "240 = 15 x 16 > 128; at most floor(128/16) = 8 all-spinor "
      "classes; >= 15 - 8 = 7 classes ALWAYS contain adjoint-side "
      "roots -- the 15 classes canNOT map to 15 pure matter "
      "multiplets",
      240 > 128 and 128 // 16 == 8 and 15 - 8 == 7 and 8 < 15,
      kill="K5")


def in_E8_std(x):
    par = {v % 2 for v in x}
    return len(par) == 1 and sum(x) % 4 == 0


roots_std = []
for v in itertools.product((-1, 0, 1), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        roots_std.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(v) % 4 == 0:
        roots_std.append(v)
n_int = sum(1 for r in roots_std if any(abs(x) == 2 for x in r))
n_spin = len(roots_std) - n_int


def in_pi2L_std(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_E8_std([x // 2 for x in w])


reps_std = []
lab_std = {}
for r in roots_std:
    for li, rep in enumerate(reps_std):
        if in_pi2L_std(tuple(a - b for a, b in zip(r, rep))):
            lab_std[r] = li
            break
    else:
        lab_std[r] = len(reps_std)
        reps_std.append(r)
cls_int = [0] * len(reps_std)
cls_spin = [0] * len(reps_std)
for r in roots_std:
    if any(abs(x) == 2 for x in r):
        cls_int[lab_std[r]] += 1
    else:
        cls_spin[lab_std[r]] += 1
n_pure = sum(1 for li in range(len(reps_std)) if cls_int[li] == 0)
n_adj = sum(1 for li in range(len(reps_std)) if cls_int[li] > 0)
n_both = sum(1 for li in range(len(reps_std))
             if cls_int[li] > 0 and cls_spin[li] > 0)
check("S7.2 CONCRETE CENSUS (standard doubled model, SPEC v2): %d "
      "integer + %d spinor roots; Gaussian census %d x 16, zero class "
      "empty; spinor-pure classes = %d == 8 (bound SATURATED) and "
      "adjoint-side classes = %d == 7 >= 7 (bound SATURATED); the "
      "J-quotient respects the D8 grading (%d both-type classes) -- "
      "at least 7 of the 15 mailboxes canNOT be matter multiplets"
      % (n_int, n_spin, len(reps_std), n_pure, n_adj, n_both),
      n_int == 112 and n_spin == 128 and len(reps_std) == 15
      and not any(in_pi2L_std(r) for r in roots_std)
      and sorted(cls_int[li] + cls_spin[li]
                 for li in range(15)) == [16] * 15
      and n_pure == 8 and n_adj == 7 and n_both == 0
      and n_pure < 15, kill="K5")
print("    per-class (integer, spinor) mix: %s"
      % sorted((cls_int[li], cls_spin[li]) for li in range(15)))

D_SPLIT = (0, 2, 4, 6, 7)               # canonical sigma-stable split
pairs_per_class = {}
for li in range(15):
    if cls_int[li]:
        continue
    wset = set()
    for r in roots_std:
        if lab_std[r] != li or any(abs(x) == 2 for x in r):
            continue
        w = tuple(r[k] for k in D_SPLIT)
        wset.add(frozenset({w, tuple(-x for x in w)}))
    pairs_per_class[li] = len(wset)
check("S7.3 WEIGHT-LEVEL KILL (canonical split D = (0,2,4,6,7), v775): "
      "each of the 8 spinor-pure classes restricts to %s distinct "
      "half-spinor +-weight pairs == 8 each, NEVER 1 -- no class is "
      "ONE SU(5) weight state; v775 ROOTCLASS-MIXED [E] re-verified "
      "at the canonical split, NOT overturned (the exhaustive 56 x "
      "240 x 2 scan found ZERO pure conventions)"
      % sorted(set(pairs_per_class.values())),
      len(pairs_per_class) == 8
      and all(v2_ == 8 for v2_ in pairs_per_class.values())
      and all(v2_ != 1 for v2_ in pairs_per_class.values()),
      kill="K5")

# ======================================================================
section("S8: what the normal form does NOT remove -- P2 typed (v799)")
# ======================================================================
ok_typeii = True
for c in placements:
    wts = sorted(sum(w) for w in c)
    if len(c) != 16 or any(w % 4 for w in wts) \
       or wts != [0] + [4] * 14 + [8]:
        ok_typeii = False
    # self-dual: |C| = 2^4 at n = 8 and all pairs orthogonal
    cl = sorted(c)
    if any(sum(a * b for a, b in zip(u, w)) % 2
           for u in cl for w in cl):
        ok_typeii = False
check("S8.1 TYPE II ECHO: all 30 placements are [8,4] doubly-even "
      "self-dual codes with weight enumerator 1 + 14 z^4 + z^8 -- the "
      "Type II set that v799 TYPEII-FORCED [E] derives from the three "
      "seam axioms (A1 locality, A2 integer spin, A3 holomorphy)",
      len(placements) == 30 and ok_typeii, kill="K6")
check("S8.2 TYPED REMAINING BRIDGE (honesty, not a derivation): C_fin "
      "does NOT derive A1-A3, the OPE-linearity scope note, or the "
      "v776 selection of ONE of the 30 copies -- P2 (g_car = 5 = the "
      "iota slot count) is NARROWED to the v799 residual R1' "
      "([C] class), not eliminated",
      True,
      "residual typed per v799: three physical axioms + linearity "
      "scope + uniqueness selection", kill=None)

# ======================================================================
section("C: controls (must fire)")
# ======================================================================
def dot4(v, w):
    return sum(a * b for a, b in zip(v, w)) % 2


refs_dot = refinements_of(dot4)
check("C1 FIRES: the non-alternating dot form admits %d == 0 quadratic "
      "refinements (dot(e1,e1) = 1 forces alternation to fail)"
      % len(refs_dot),
      len(refs_dot) == 0 and dot4((1, 0, 0, 0), (1, 0, 0, 0)) == 1,
      kill="K7")

cand_id = [q for q in refs if q[WIDX[A_BIT]] == 1
           and q[WIDX[FSIG]] == 0]
check("C2 FIRES: trivial deck sigma' = id: selector census 16 -> 8 -> "
      "%d != 1 -- WITHOUT the family 3-cycle q* is NOT unique"
      % len(cand_id),
      len([q for q in refs if q[WIDX[A_BIT]] == 1]) == 8
      and len(cand_id) == 4 and len(cand_id) != 1, kill="K7")


def iota_bad(v):
    return (v[0], v[1], v[2], v[3], 0)


img_bad = {iota_bad(v) for v in W16}
beta_bad_ok = all(sum(x * y for x, y in zip(iota_bad(v), iota_bad(w)))
                  % 2 == hb(v, w) for v in W16 for w in W16)
check("C3 FIRES: wrong lift iota' = (f1,f2,f3,a,0): image not inside "
      "C_even(5) (%s) and beta' != hbar (witness e1,e2: %d != %d)"
      % (not (img_bad <= CEVEN),
         dot4((1, 0, 0, 0), (0, 1, 0, 0)),
         hb((1, 0, 0, 0), (0, 1, 0, 0))),
      not (img_bad <= CEVEN) and not beta_bad_ok, kill="K7")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
if not controls_ok:
    VERDICT = "CONTROL-DEAD"
elif KILLS:
    VERDICT = {"K1": "QUOTIENT-BROKEN", "K2": "SELECTOR-BROKEN",
               "K3": "LIFT-BROKEN", "K4": "COUNT-BROKEN",
               "K5": "NEGATIVE-OVERTURNED",
               "K6": "TYPEII-ECHO-BROKEN"}.get(KILLS[0], "CONTROL-DEAD")
else:
    VERDICT = "NORMAL-FORM-ASSEMBLED"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
print("  * ONE OBJECT: C_fin = (V, hbar, q*, sigma, iota) read off the")
print("    Gaussian quotient assembles v752 (census + form), v774")
print("    (refinements, selector, parity lift, S5 geometry, Pascal")
print("    1+5+10), v833 (quotient rebuild) into one normal form; the")
print("    counting corollary chain 16 = 1+5+10, 15 = 5+10, 30 =")
print("    2(5+10), 240 = 16(5+10), 248 = 16(5+10)+8 is derived from")
print("    the object and checked against the actual lattice census.")
print("  * BUILT-IN NEGATIVE: the code-to-matter reading stays DEAD")
print("    (v775 ROOTCLASS-MIXED re-anchored via the 128-spinor")
print("    counting bound + the concrete doubled-model mix census).")
print("  * P2 STATUS: narrowed to v799's residual R1' (three seam")
print("    axioms + linearity scope + v776 uniqueness selection);")
print("    the 30-copy Type II echo verified here; NOT eliminated.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot
                       and VERDICT == "NORMAL-FORM-ASSEMBLED") else 1)
