#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""curve_code_2torsion_probe -- CURVE.CODE.2TORSION.01 (strategic round,
top priority): does the 2-torsion of the seam-curve abelian surface REALIZE
the certified Gaussian-code geometry?

THEOREM CANDIDATE (frozen before any computation):
    (A[2], e_2, sigma, q_Theta)  ~iso~  (V = L/(1+i)L, hbar, sigma-bar, q*)
where A is the abelian-surface component of Jac(C), C: y^3 = x^4 - 1
(genus 3; Jacobian splits per v610 into the zeta_12 CM surface times the
omega CM elliptic curve), e_2 the Weil pairing on A[2], sigma the curve
automorphism that descends to an order-3 cycle on A[2] (DERIVED below, not
assumed), q_Theta the theta-characteristic quadratic refinement of the
distinguished ODD polarization; and on the right the frozen code objects of
v752/v753 and today's arf_spinor_compiler_probe: hbar with Gram J - I in the
family/anchor basis (F1,F2,F3,A), sigma-bar = the family 3-cycle, q* = the
unique sigma-invariant Arf-1 refinement with q*(A)=1, q*(F_Sigma)=0
(= the parity lift, census 6 odd + 10 even, K6 duad model).

ROUTE (ONE route, frozen -- the CM-model route):
  R1  Exact differential characters of C under tau: y->omega*y and
      rho: x->i*x (sympy, reproducing v610 L1); g := rho*tau acts on the two
      abelian-surface differentials (dx/y, dx/y^2) with eigenvalues
      zeta^11, zeta^7 (zeta = e^{2 pi i/12}) => CM type Phi = {sigma_11,
      sigma_7} on K = Q(zeta_12), O = Z[zeta_12].
  R2  DECLARED REALIZATION: A := C^2 / Phi(O) * diag(Omega_1, Omega_2) --
      the zeta_12-isotypic period image (v610's named CM resource; class
      number h(K) = 1 so every O-lattice realization is O-isomorphic).
      CERTIFICATION (the only numerical step, mpmath dps = 120): all
      generator-cycle period vectors of (dx/y, dx/y^2) -- sheet-difference
      cycles over the branch-point edges [1,i], i[1,i], -[1,i], -i[1,i] and
      an edge to infinity -- are recognized as Phi(alpha) * v0 with alpha
      INTEGRAL in O (recognition tolerance 1e-30, residual tolerance 1e-35,
      margins printed); the recognized alphas generate O (HNF index 1).
      Numerical period steps END in these certified integer recognitions.
  R3  A[2] := (1/2)Lambda/Lambda = O/2O = F2^4 with basis (1, zeta, zeta^2,
      zeta^3) mod 2.  The complex structure is O-rational: J = mult by
      zeta^9 (both CM embeddings send zeta^9 -> i).  EXACT from here on.
  R4  sigma := the induced action of the deck tau = g^4 = mult by zeta^4
      (order 3).  DERIVATION of "which automorphism descends": monodromy
      exponents force every reduced automorphism of P^1 to fix infinity and
      preserve {1,i,-1,-i} affinely => reduced group = mu_4, Aut(C) =
      <tau, rho> = C12 ([C]: automorphisms of the non-hyperelliptic plane
      quartic Y^3 Z = X^4 - Z^4 are linear); the ONLY order-3 elements are
      tau, tau^2, and both act on A[2] as mult by zeta^{+-4}.
  R5  e_2 := E* mod 2 with E*(x,y) = Tr_{K/Q}(zeta^3 x conj(y))/2 -- the
      FROZEN minimal ODD tau-invariant polarization (type (1,3), Pfaffian
      3).  Justification computed exactly: the tau-invariant slice of NS
      contains NO principal form (unit-sign obstruction: the fundamental
      unit 2+sqrt3 of the real subfield is totally positive), its minimal
      type is the even (1,2) (mod-2 DEGENERATE -- the curve-induced Prym
      type [C], reported), and (1,3) is the minimal ODD type => the unique
      convention under which the candidate is even well-posed.
  R6  q_Theta := the quadratic refinement of the UNIQUE tau-invariant
      symmetric theta structure = the unique tau-fixed refinement of
      (A[2], e_2) (exists and is unique because tau - 1 is invertible:
      N(omega - 1) = 9 is odd).
  R7  THE DECIDER: full census over GL(4,2) of F2-linear isos
      phi: A[2] -> V carrying e_2 -> hbar, tau -> sigma-bar (both tau and
      tau^2 tested), q_Theta -> q* (and the Arf-orbit variant).  Then the
      induced transports (1+5bar+10, 3+2 slot split, K6 duads) if and only
      if a joint phi exists.

KILLS (frozen; any one fires => the corresponding layer is dead):
  K1  code layer: selector not unique, census not 6+10, |Sp(4,2)| != 720.
  K2  curve exact layer: characters not (zeta^11, zeta^7, zeta^10), genus
      != 3, order-3 automorphisms != {tau, tau^2}.
  K3  certification: any generator period not integrally recognized at the
      stated tolerance, or HNF index != 1.
  K4  polarization layer: E* not integral/alternating/invariant/positive,
      Pf(E*) != 3, or a tau-invariant form with |Pf| = 1 exists in the
      census box (would contradict the frozen minimality).
  K5  refinement layer: #refinements != 16, census != 6+10, tau-fixed
      refinement not unique.
  K6  census layer: N_pair != |Sp(4,2)| = 720 (forms are both symplectic
      F2^4, so the transporter must be a Sp-torsor).
  K7  controls: any must-fire control fails, or the positive control
      (code clone) census != the code-side stabilizer order.

VERDICT ENUM (frozen):
  CURVE-CODE-ISOMORPHIC  N_all > 0: canonical phi exists (census = the
                         stabilizer order), all structure transports --
                         curve, code, spinor decomposition, theta geometry
                         are one statement.
  CURVE-CODE-PARTIAL     N_all = 0 but N_pair > 0: phi exists for a
                         sub-structure; the breaking layer(s) are named
                         exactly (sigma conjugacy / distinguished
                         refinement).
  CURVE-CODE-DEAD        N_pair = 0: no phi at all.
  TEST-VOID              a must-fire control does not fire.

FENCES (honesty, frozen):
  *  This is finite exact algebra on 2-torsion.  NO physical labeling is
     claimed anywhere in this file.  The root-level matter reading of the
     Gaussian classes is separately DEAD as of today per
     gaussian_class_d5_purity_probe.py (verdict ROOTCLASS-MIXED): no
     scanned D5+A3 / SU(5) convention makes the 15 classes pure.  The
     theta surface tested here is a DIFFERENT object and this probe does
     NOT resurrect the killed reading in either direction.
  *  Numerical steps: mpmath dps = 120; every period computation ends in a
     certified integer recognition (tolerances and margins printed; the
     margin to the nearest half-integer is > 10^25 times the residual).
  *  Realization fence: the declared A is the projected CM lattice
     Phi(O)*Omega; the sub-abelian-variety Lambda_sub = H_1 cap V_A is
     O-isomorphic to it (h(K) = 1), and the two structural kill facts --
     tau - 1 invertible mod 2 (N(omega-1) = 9 odd) and the tau-invariant
     polarization type census -- are REALIZATION-INDEPENDENT (they only
     use the O-module structure).  The completeness of the generator
     cycles for H_1 is typed [C] (standard superelliptic generation); the
     recognition certifies containment and index-1 generation of O.
  *  The polarization induced on A by restricting the principal theta of
     Jac(C) is the even Prym type (1,2) ([C], complementary-pair theory
     for the degree-2 quotient C -> E); its mod-2 Weil form is DEGENERATE
     (verified exactly below) -- the naive induced-e_2 reading is ill
     posed, which is WHY the frozen route uses the minimal odd
     tau-invariant type (1,3): the maximally theorem-friendly convention.
     Under NO convention in the tau-invariant cone does a principal form
     exist (exact box census + unit-sign argument).

FIREWALL: experiments/tfpt-discovery probe; ONE new file; writes nothing;
touches no verification/, paper, ledger, changelog or website surface; no
status marker moves; report only.

Sources (read-only): verification/v610_curve_landscape.py (splitting,
characters), verification/v611_periods.py (Beta periods, rotation action),
verification/v752_projective_hamming_incidence.py + v753 (code layer),
experiments/tfpt-discovery/arf_spinor_compiler_probe.py (hbar Gram J - I,
sigma-bar, q*, 6+10, K6 duads -- the abstract layer is re-verified here),
experiments/tfpt-discovery/gaussian_class_d5_purity_probe.py
(ROOTCLASS-MIXED fence).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/curve_code_2torsion_probe.py
"""

import itertools
import time
from fractions import Fraction as Fr

import sympy as sp
from mpmath import mp, mpf, mpc, quad, exp as mexp, log as mlog, arg as marg
from mpmath import pi as mpi_, matrix as mmatrix, lu_solve, fabs, nstr, beta as mbeta

mp.dps = 120                   # tanh-sinh with algebraic endpoint
                               # singularities achieves ~0.36*dps digits;
                               # dps 120 => residuals ~1e-42
TOL_RESID = mpf(10) ** -35     # certified residual tolerance
TOL_REC = mpf(10) ** -30       # integer-recognition tolerance

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
# exact arithmetic in K = Q(zeta_12), O = Z[zeta], zeta^4 = zeta^2 - 1
# elements = 4-tuples (a0, a1, a2, a3) = a0 + a1 z + a2 z^2 + a3 z^3
# ======================================================================
ZPOW = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
        (-1, 0, 1, 0), (0, -1, 0, 1), (-1, 0, 0, 0)]   # z^0 .. z^6


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


def kadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def kneg(a):
    return tuple(-x for x in a)


# conj: z -> z^11 = z - z^3;  z^2 -> 1 - z^2;  z^3 -> -z^3
CONJ_BASIS = [(1, 0, 0, 0), (0, 1, 0, -1), (1, 0, -1, 0), (0, 0, 0, -1)]


def kconj(a):
    out = [0, 0, 0, 0]
    for i in range(4):
        if a[i]:
            for t in range(4):
                out[t] += a[i] * CONJ_BASIS[i][t]
    return tuple(out)


def ktrace(a):
    # Tr(1, z, z^2, z^3) = (4, 0, 2, 0), verified below via mult matrices
    return 4 * a[0] + 2 * a[2]


def kpow_zeta(k):
    """zeta^k as an exact element."""
    out = (1, 0, 0, 0)
    z = (0, 1, 0, 0)
    for _ in range(k % 12):
        out = kmul(out, z)
    return out


E_K = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
ZETA3 = kpow_zeta(3)
ZETA4 = kpow_zeta(4)     # = omega under both CM embeddings' cube part
ZETA9 = kpow_zeta(9)     # = the complex structure J (both embeddings -> i)


def mult_matrix(g):
    """integer matrix of x -> g*x in basis (1, z, z^2, z^3), columns = images."""
    return [[kmul(g, E_K[j])[i] for j in range(4)] for i in range(4)]


def mat_mul_i(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]


def Estar(x, y):
    """E*(x,y) = Tr(zeta^3 * x * conj(y)) / 2 -- the frozen (1,3) form."""
    t = ktrace(kmul(kmul(ZETA3, x), kconj(y)))
    assert t % 2 == 0, "E* not integral"
    return t // 2


def pfaffian4(E):
    return E[0][1] * E[2][3] - E[0][2] * E[1][3] + E[0][3] * E[1][2]


# ======================================================================
# S1 -- the frozen CODE side (abstract layer of v752/arf probe, re-verified)
# ======================================================================
section("S1: the frozen code side (V, hbar, sigma-bar, q*) -- re-verified")

W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


def xor4(v, w):
    return tuple((a + b) % 2 for a, b in zip(v, w))


HB = [[hb(v, w) for w in W16] for v in W16]
ADD = [[WIDX[xor4(v, w)] for w in W16] for v in W16]
A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


SIG_PERM = [WIDX[sig_bits(w)] for w in W16]


def all_refinements(pair_tab, add_tab):
    refs = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            hrow = pair_tab[i]
            arow = add_tab[i]
            qi = q[i]
            for j in range(16):
                if q[arow[j]] ^ qi ^ q[j] != hrow[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            refs.append(tuple(q))
    return refs


REFS_V = all_refinements(HB, ADD)
zeros_of = {q: sum(1 for b in q if b == 0) for q in REFS_V}
arf1_V = sorted(q for q in REFS_V if zeros_of[q] == 6)
arf0_V = sorted(q for q in REFS_V if zeros_of[q] == 10)
check("S1.1 code refinement census: 16 refinements, 6 Arf-1 (6 zeros) + "
      "10 Arf-0 (10 zeros)",
      len(REFS_V) == 16 and len(arf1_V) == 6 and len(arf0_V) == 10,
      kill="K1")

siginv_V = [q for q in REFS_V if all(q[SIG_PERM[i]] == q[i]
                                     for i in range(16))]
cand = [q for q in siginv_V if q[WIDX[A_BIT]] == 1 and q[WIDX[FSIG]] == 0]
check("S1.2 frozen selector unique: %d sigma-invariant refinements, exactly"
      " 1 with q(A)=1, q(F_Sigma)=0 => q*" % len(siginv_V),
      len(siginv_V) == 4 and len(cand) == 1, kill="K1")
QSTAR = cand[0]


def iota5(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


qwt = tuple((sum(iota5(w)) // 2) % 2 for w in W16)
check("S1.3 q* == the parity lift q_wt (arf probe S6), Arf 1",
      qwt == QSTAR and zeros_of[QSTAR] == 6, kill="K1")


def linear_maps_transporting(src_tab, dst_tab):
    """all invertible 4x4 F2 maps phi with dst(phi x, phi y) = src(x, y);
    vectors indexed 0..15 by bit patterns; returns list of image tables."""
    out = []
    for m in range(1 << 16):
        cols = [(m >> (4 * k)) & 15 for k in range(4)]
        img = [0] * 16
        ok = True
        for x in range(16):
            v = 0
            if x & 1:
                v ^= cols[0]
            if x & 2:
                v ^= cols[1]
            if x & 4:
                v ^= cols[2]
            if x & 8:
                v ^= cols[3]
            img[x] = v
        if len(set(img)) != 16:
            continue
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


# vectors of V as 4-bit ints (bit k = coordinate k in (F1,F2,F3,A))
HB_I = [[HB[i][j] for j in range(16)] for i in range(16)]
# reindex: W16 tuple order == bit order? W16 from itertools.product is
# lexicographic in tuple; map tuple <-> int via bits explicitly:
TUP2INT = {w: (w[0] | (w[1] << 1) | (w[2] << 2) | (w[3] << 3)) for w in W16}
INT2TUP = {v: k for k, v in TUP2INT.items()}
HB_B = [[0] * 16 for _ in range(16)]
for wa in W16:
    for wb in W16:
        HB_B[TUP2INT[wa]][TUP2INT[wb]] = hb(wa, wb)
SIG_B = [0] * 16
for w in W16:
    SIG_B[TUP2INT[w]] = TUP2INT[sig_bits(w)]
QSTAR_B = [0] * 16
for w in W16:
    QSTAR_B[TUP2INT[w]] = QSTAR[WIDX[w]]

SP_V = linear_maps_transporting(HB_B, HB_B)
check("S1.4 |Sp(4,2)| = %d == 720 (full census)" % len(SP_V),
      len(SP_V) == 720, kill="K1")

stab_joint = [g for g in SP_V
              if all(g[SIG_B[x]] == SIG_B[g[x]] for x in range(16))
              and all(QSTAR_B[g[x]] == QSTAR_B[x] for x in range(16))]
check("S1.5 code-side joint stabilizer of (hbar, sigma-bar, q*): order %d "
      "(the expected torsor size for a canonical phi)" % len(stab_joint),
      len(stab_joint) in (6,), "centralizer of a 3-cycle in Stab(q*) ~ S5",
      kill="K1")
N_STAB = len(stab_joint)

# sigma-bar diagnostics: fixed space, cycle type on the 6 odd forms
SIGMAT = [[0] * 4 for _ in range(4)]
for k in range(4):
    img = INT2TUP[SIG_B[1 << k]]
    for i in range(4):
        SIGMAT[i][k] = img[i]


def f2_rank(M):
    A = [row[:] for row in M]
    n, m = len(A), len(A[0])
    r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if A[i][c] % 2), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(n):
            if i != r and A[i][c] % 2:
                A[i] = [(a + b) % 2 for a, b in zip(A[i], A[r])]
        r += 1
    return r


fix_sig = 4 - f2_rank([[(SIGMAT[i][j] + (1 if i == j else 0)) % 2
                        for j in range(4)] for i in range(4)])


def perm_cycle_type(perm_on_list):
    seen = set()
    ct = []
    n = len(perm_on_list)
    for s in range(n):
        if s in seen:
            continue
        ln, cur = 0, s
        while cur not in seen:
            seen.add(cur)
            cur = perm_on_list[cur]
            ln += 1
        ct.append(ln)
    return sorted(ct, reverse=True)


def act_on_ref(q, img_inv):
    return tuple(q[img_inv[i]] for i in range(16))


arf1_Vb = sorted(tuple(q[WIDX[INT2TUP[i]]] for i in range(16))
                 for q in arf1_V)
sig_inv_perm = [0] * 16
for x in range(16):
    sig_inv_perm[SIG_B[x]] = x
sig_on_odd = [arf1_Vb.index(act_on_ref(q, sig_inv_perm)) for q in arf1_Vb]
ct_sig = perm_cycle_type(sig_on_odd)
print("    sigma-bar: fixed-space dim = %d; cycle type on the 6 odd "
      "refinements = %s (a 3-cycle: duad side of S6)" % (fix_sig, ct_sig))

# ======================================================================
# S2 -- curve exact layer: characters, genus, Aut, CM type
# ======================================================================
section("S2: curve exact layer -- characters, genus, Aut(C), CM type")

w3s = sp.exp(2 * sp.pi * sp.I / 3)
chars = {}
for nm, (k, j) in {"dx/y": (0, 1), "dx/y^2": (0, 2), "x dx/y^2": (1, 2)}.items():
    cs = sp.simplify(w3s ** (-j))       # deck tau: y -> w y
    cr = sp.simplify(sp.I ** (k + 1))   # rotation rho: x -> i x
    z = sp.simplify(cs * cr)
    # identify as zeta_12 power exactly
    got = None
    for n in range(12):
        if sp.simplify(z - sp.exp(2 * sp.pi * sp.I * n / 12)) == 0:
            got = n
            break
    chars[nm] = got
check("S2.1 g = rho*tau eigencharacters: dx/y -> zeta^%s, dx/y^2 -> "
      "zeta^%s (order 12: the CM type Phi = {sigma_11, sigma_7}), "
      "x dx/y^2 -> zeta^%s (order 6: the omega elliptic factor)"
      % (chars["dx/y"], chars["dx/y^2"], chars["x dx/y^2"]),
      chars == {"dx/y": 11, "dx/y^2": 7, "x dx/y^2": 10}, kill="K2")

# genus: Riemann-Hurwitz for the mu3 cover, 5 totally ramified points
lhs_rh = 2 * 3 - 2
rhs_rh = 3 * (2 * 0 - 2) + 5 * (3 - 1)
# smoothness of the plane quartic Y^3 Z = X^4 - Z^4 (exact partials)
X, Y, Z = sp.symbols("X Y Z")
F = Y ** 3 * Z - X ** 4 + Z ** 4
sols = sp.solve([sp.diff(F, v) for v in (X, Y, Z)], [X, Y, Z], dict=True)
only_origin = all(all(s.get(v, 0) == 0 for v in (X, Y, Z)) for s in sols)
check("S2.2 genus 3: RH %d == %d (5 totally ramified points) and the "
      "plane quartic Y^3Z = X^4 - Z^4 is smooth (singular locus = origin "
      "only)" % (lhs_rh, rhs_rh),
      lhs_rh == rhs_rh and only_origin, kill="K2")

# Aut derivation: reduced automorphisms fix infinity (monodromy exponent 2
# there vs 1 at finite branch points), hence are affine x -> ax + b with
# a*{1,i,-1,-i} + b = {1,i,-1,-i}; centroid => b = 0; a*mu4 = mu4 => a in mu4.
mu4 = [sp.Integer(1), sp.I, sp.Integer(-1), -sp.I]
good_a = [a for a in mu4
          if {sp.simplify(a * b) for b in mu4} == set(mu4)]
bad_a_example = sp.exp(sp.I * sp.pi / 3)
bad = {sp.simplify(bad_a_example * b) for b in mu4} == set(mu4)
check("S2.3 reduced Aut = mu4 (b = 0 forced by the centroid; a*mu4 = mu4 "
      "iff a^4 = 1; non-mu4 example fails); Aut(C) = <tau, rho> = C12 [C: "
      "plane-quartic automorphisms are linear]; ONLY order-3 elements: "
      "tau, tau^2", len(good_a) == 4 and not bad, kill="K2")
check("S2.4 the descending order-3 action DERIVED: tau = g^4 acts on the "
      "A-lattice as mult by zeta^4 (sigma_11: zeta^4 -> omega^2, sigma_7: "
      "zeta^4 -> omega -- nontrivial cube roots on both A-differentials); "
      "rho = g^9 acts as mult by zeta^9 = the complex structure J itself",
      kmul(ZETA4, ZETA4) == kpow_zeta(8)
      and kmul(kmul(ZETA4, ZETA4), ZETA4) == (1, 0, 0, 0)
      and kmul(ZETA9, ZETA9) == kneg((1, 0, 0, 0)), kill="K2")

# ======================================================================
# S3 -- period certification (the ONLY numerical step)
# ======================================================================
section("S3: certified period recognition -- Lambda_A = Phi(O) * v0 "
        "(dps = 120)")

OM = mexp(2j * mpi_ / 3)
Z11 = mexp(2j * mpi_ * 11 / 12)
Z7 = mexp(2j * mpi_ * 7 / 12)


def cbrt_cut(w):
    """cube root with branch cut along the POSITIVE reals (paths below
    stay off R+ for x^4 - 1)."""
    a = marg(w)
    if a < 0:
        a += 2 * mpi_
    return mexp((mlog(abs(w)) + 1j * a) / 3)


def edge_integrals(x_of_t, dx_of_t, pts):
    def f1(t):
        x = x_of_t(t)
        return dx_of_t(t) / cbrt_cut(x ** 4 - 1)

    def f2(t):
        x = x_of_t(t)
        return dx_of_t(t) / cbrt_cut(x ** 4 - 1) ** 2
    return quad(f1, pts), quad(f2, pts)


I_ = mpc(0, 1)
EDGES = {}
# finite edges: [1 -> i], and its mu4 rotations
for m in range(4):
    rot = I_ ** m
    b0, b1 = rot * 1, rot * I_
    EDGES["E%d" % m] = edge_integrals(
        lambda t, b0=b0, b1=b1: b0 + t * (b1 - b0),
        lambda t, b0=b0, b1=b1: (b1 - b0),
        [0, mpf(1) / 2, 1])
# infinity edge: 1 -> 1+i -> (1+i)*(1+s), s -> inf
leg1 = edge_integrals(lambda t: 1 + t * I_, lambda t: I_,
                      [0, mpf(1) / 2, 1])
leg2 = edge_integrals(lambda s: (1 + I_) * (1 + s),
                      lambda s: (1 + I_), [0, 1, mp.inf])
EDGES["EINF"] = (leg1[0] + leg2[0], leg1[1] + leg2[1])

# v611 cross-check: real Beta integrals
Ib01 = quad(lambda x: (1 - x ** 4) ** (mpf(-1) / 3), [0, mpf(9) / 10, 1])
Ib02 = quad(lambda x: (1 - x ** 4) ** (mpf(-2) / 3), [0, mpf(9) / 10, 1])
r_beta = max(fabs(Ib01 - mbeta(mpf(1) / 4, mpf(2) / 3) / 4),
             fabs(Ib02 - mbeta(mpf(1) / 4, mpf(1) / 3) / 4))
check("S3.1 v611 Beta identities reproduced numerically: worst residual "
      "%s < 1e-35" % nstr(r_beta, 3), r_beta < TOL_RESID)

# sheet-difference cycle vectors
def cycle_vec(edge, s):
    A1, A2 = EDGES[edge]
    c1 = (OM ** (-s) - OM ** (-(s + 1))) * A1
    c2 = (OM ** (-2 * s) - OM ** (-2 * (s + 1))) * A2
    return (c1, c2)


V0 = cycle_vec("E0", 0)
check("S3.2 base period vector v0 nonzero in both coordinates: |v0| = "
      "(%s, %s)" % (nstr(abs(V0[0]), 8), nstr(abs(V0[1]), 8)),
      abs(V0[0]) > mpf(10) ** -5 and abs(V0[1]) > mpf(10) ** -5, kill="K3")

# recognition matrix: alpha = sum c_k zeta^k, embeddings sigma_11, sigma_7
M4 = mmatrix(4, 4)
for k in range(4):
    M4[0, k] = (Z11 ** k).real
    M4[1, k] = (Z11 ** k).imag
    M4[2, k] = (Z7 ** k).real
    M4[3, k] = (Z7 ** k).imag


def recognize(vec):
    r1 = vec[0] / V0[0]
    r2 = vec[1] / V0[1]
    rhs = mmatrix([r1.real, r1.imag, r2.real, r2.imag])
    c = lu_solve(M4, rhs)
    ints = [int(mp.nint(c[i])) for i in range(4)]
    err = max(fabs(c[i] - ints[i]) for i in range(4))
    # certified residual against exact integer alpha
    a11 = sum(ints[k] * Z11 ** k for k in range(4))
    a7 = sum(ints[k] * Z7 ** k for k in range(4))
    res = max(fabs(vec[0] - a11 * V0[0]), fabs(vec[1] - a7 * V0[1]))
    return tuple(ints), err, res


ALPHAS = []
worst_err, worst_res = mpf(0), mpf(0)
all_int = True
for edge in ("E0", "E1", "E2", "E3", "EINF"):
    for s in (0, 1, 2):
        alpha, err, res = recognize(cycle_vec(edge, s))
        ALPHAS.append((edge, s, alpha))
        worst_err = max(worst_err, err)
        worst_res = max(worst_res, res)
        if err > TOL_REC or res > TOL_RESID * max(abs(V0[0]), abs(V0[1])):
            all_int = False
check("S3.3 ALL 15 generator cycles recognized INTEGRALLY in Phi(O)*v0: "
      "worst rounding error %s (< 1e-30), worst certified residual %s "
      "(< 1e-35 * scale); margin to the nearest half-integer > 10^25 x "
      "residual" % (nstr(worst_err, 3), nstr(worst_res, 3)),
      all_int, kill="K3")


def row_hnf_index(rows):
    """|det| of the HNF of the integer row lattice (0 if rank < 4)."""
    M = [list(r) for r in rows if any(r)]
    r0 = 0
    for col in range(4):
        while True:
            nz = [i for i in range(r0, len(M)) if M[i][col] != 0]
            if not nz:
                piv_i = None
                break
            if len(nz) == 1:
                piv_i = nz[0]
                break
            nz.sort(key=lambda i: abs(M[i][col]))
            p = nz[0]
            for i in nz[1:]:
                qd = M[i][col] // M[p][col]
                M[i] = [a - qd * b for a, b in zip(M[i], M[p])]
        if piv_i is None:
            continue
        M[r0], M[piv_i] = M[piv_i], M[r0]
        if M[r0][col] < 0:
            M[r0] = [-a for a in M[r0]]
        r0 += 1
    if r0 < 4:
        return 0
    det = 1
    for i in range(4):
        det *= M[i][i]
    return abs(det)


idx = row_hnf_index([list(a) for _, _, a in ALPHAS])
alpha_set = sorted(set(a for _, _, a in ALPHAS))
check("S3.4 the recognized alphas generate O with HNF index %d == 1: the "
      "CM lattice IS Phi(O)*v0 (certified); distinct alphas: %s"
      % (idx, alpha_set), idx == 1, kill="K3")

# ======================================================================
# S4 -- the polarization layer (fully exact)
# ======================================================================
section("S4: polarization layer -- NS, tau-invariant cone, the frozen "
        "odd (1,3) form")

MJ = mult_matrix(ZETA9)
MT = mult_matrix(ZETA4)
MJ2 = mat_mul_i(MJ, MJ)
MT3 = mat_mul_i(mat_mul_i(MT, MT), MT)
check("S4.1 exact matrices: J = M(zeta^9), J^2 = -I; tau = M(zeta^4), "
      "tau^3 = I; trace vector Tr(1,z,z^2,z^3) = (4,0,2,0) verified",
      MJ2 == [[-1 if i == j else 0 for j in range(4)] for i in range(4)]
      and MT3 == [[1 if i == j else 0 for j in range(4)] for i in range(4)]
      and [sum(mult_matrix(E_K[k])[i][i] for i in range(4))
           for k in range(4)] == [4, 0, 2, 0], kill="K4")


def sym_apply(E, M):
    """E'(x,y) = E(Mx, My) as matrix M^T E M."""
    MT_ = [[M[j][i] for j in range(4)] for i in range(4)]
    return mat_mul_i(mat_mul_i(MT_, E), M)


# solve for J-invariant (and tau-invariant) alternating integer forms
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def basis_form(p):
    E = [[0] * 4 for _ in range(4)]
    E[p[0]][p[1]] = 1
    E[p[1]][p[0]] = -1
    return E


def invariance_nullspace(mats):
    rows = []
    for p_out in pairs:
        row = []
        for p_in in pairs:
            Eb = basis_form(p_in)
            acc = 0
            # sum of (M^T Eb M - Eb) entries at p_out over all constraints
            row_entry = []
            for M in mats:
                Ep = sym_apply(Eb, M)
                row_entry.append(Ep[p_out[0]][p_out[1]]
                                 - Eb[p_out[0]][p_out[1]])
            row.append(row_entry)
        rows.append(row)
    # build one stacked system: constraints x mats
    sysm = []
    for mi in range(len(mats)):
        for r in rows:
            sysm.append([r[c][mi] for c in range(6)])
    Msys = sp.Matrix(sysm)
    null = Msys.nullspace()
    out = []
    for v in null:
        den = sp.lcm([sp.fraction(sp.nsimplify(x))[1] for x in v])
        vi = [int(x * den) for x in v]
        g = 0
        for x in vi:
            g = sp.gcd(g, x)
        vi = [x // int(g) for x in vi] if g else vi
        out.append(vi)
    return out


ns_J = invariance_nullspace([MJ])
ns_Jt = invariance_nullspace([MJ, MT])
check("S4.2 NS(A) has rank %d == 4 (A is non-simple: consistent with the "
      "v610 point counts, which match a SQUARE of a Q(i)-CM curve at "
      "p = 1 mod 12 [C]); the tau-invariant slice has rank %d == 2 (the "
      "K-Hermitian forms Tr(xi x conj y))" % (len(ns_J), len(ns_Jt)),
      len(ns_J) == 4 and len(ns_Jt) == 2, kill="K4")


def coeffs_to_form(c):
    E = [[0] * 4 for _ in range(4)]
    for cc, p in zip(c, pairs):
        E[p[0]][p[1]] = cc
        E[p[1]][p[0]] = -cc
    return E


def pos_def_S(E):
    """S(x,y) = E(Jx, y) symmetric positive definite? exact minors."""
    S = mat_mul_i([[MJ[j][i] for j in range(4)] for i in range(4)], E)
    # S_ij = E(J e_i, e_j) = (J^T E)_ij
    if any(S[i][j] != S[j][i] for i in range(4) for j in range(4)):
        return False, S
    minors = []
    for k in range(1, 5):
        sub = sp.Matrix([[S[i][j] for j in range(k)] for i in range(k)])
        minors.append(sub.det())
    return all(m > 0 for m in minors), S


B1, B2 = (coeffs_to_form(ns_Jt[0]), coeffs_to_form(ns_Jt[1]))
census_pf = {}
found_pf = {}
for m in range(-30, 31):
    for n in range(-30, 31):
        if m == 0 and n == 0:
            continue
        E = [[m * B1[i][j] + n * B2[i][j] for j in range(4)]
             for i in range(4)]
        ok, _ = pos_def_S(E)
        if ok:
            pf = abs(pfaffian4(E))
            census_pf[pf] = census_pf.get(pf, 0) + 1
            if pf not in found_pf:
                found_pf[pf] = (m, n)
min_pf = min(census_pf) if census_pf else None
min_odd = min((p for p in census_pf if p % 2 == 1), default=None)
check("S4.3 tau-invariant polarization cone (box |m|,|n| <= 30): minimal "
      "Pfaffian %s == 2 (the even Prym/induced type (1,2) [C]), NO "
      "principal form (|Pf| = 1 absent: unit-sign obstruction, 2+sqrt3 "
      "totally positive), minimal ODD Pfaffian %s == 3 (type (1,3))"
      % (min_pf, min_odd),
      min_pf == 2 and min_odd == 3 and 1 not in census_pf, kill="K4")

ESTAR = [[Estar(E_K[i], E_K[j]) for j in range(4)] for i in range(4)]
okE, S_of_E = pos_def_S(ESTAR)
gcd_E = 0
for i in range(4):
    for j in range(4):
        gcd_E = sp.gcd(gcd_E, ESTAR[i][j])
check("S4.4 FROZEN E*(x,y) = Tr(zeta^3 x conj y)/2: integral, alternating,"
      " J- and tau-invariant, S = E*(J.,.) positive definite, Pf = %d, "
      "gcd = %d => type (1,3) (odd)" % (pfaffian4(ESTAR), int(gcd_E)),
      all(ESTAR[i][i] == 0 for i in range(4))
      and all(ESTAR[i][j] == -ESTAR[j][i] for i in range(4)
              for j in range(4))
      and sym_apply(ESTAR, MJ) == ESTAR and sym_apply(ESTAR, MT) == ESTAR
      and okE and pfaffian4(ESTAR) == 3 and int(gcd_E) == 1, kill="K4")
print("    E* Gram (1,z,z^2,z^3) = %s" % ESTAR)
print("    S Gram = %s" % S_of_E)

E2A = [[ESTAR[i][j] % 2 for j in range(4)] for i in range(4)]
mn12 = found_pf.get(2, (0, 0))
E12 = coeffs_to_form([mn12[0] * a + mn12[1] * b
                      for a, b in zip(ns_Jt[0], ns_Jt[1])])
rank_e2 = f2_rank([[E2A[i][j] for j in range(4)] for i in range(4)])
rank_12 = f2_rank([[E12[i][j] % 2 for j in range(4)] for i in range(4)])
check("S4.5 mod-2 Weil forms: the frozen odd (1,3) form is NONDEGENERATE "
      "(rank %d == 4); the even induced (1,2) form is DEGENERATE (rank %d "
      "== 2) -- the naive induced-e_2 reading is ill posed and is hereby "
      "reported dead" % (rank_e2, rank_12),
      rank_e2 == 4 and rank_12 == 2, kill="K4")

# principal polarizations in the FULL NS (informative, not load-bearing)
pp_found = []
for c in itertools.product(range(-4, 5), repeat=4):
    if not any(c):
        continue
    E = [[sum(c[k] * coeffs_to_form(ns_J[k])[i][j] for k in range(4))
          for j in range(4)] for i in range(4)]
    if abs(pfaffian4(E)) != 1:
        continue
    ok, _ = pos_def_S(E)
    if ok:
        pp_found.append(E)
tau_mod2_pp = [E for E in pp_found
               if all((sym_apply(E, MT)[i][j] - E[i][j]) % 2 == 0
                      for i in range(4) for j in range(4))]
print("    full NS box |c| <= 4: %d principal polarizations found (A IS "
      "principally polarizable, but none is tau-invariant integrally; "
      "%d are tau-invariant even mod 2)" % (len(pp_found), len(tau_mod2_pp)))

# ======================================================================
# S5 -- A[2] = O/2O: refinements, q_Theta, internal geometry
# ======================================================================
section("S5: A[2] = O/2O -- e_2, tau, q_Theta and the internal geometry")

# vectors as 4-bit ints, bit k = coefficient of zeta^k
E2A_TAB = [[0] * 16 for _ in range(16)]
for x in range(16):
    for y in range(16):
        xv = [(x >> k) & 1 for k in range(4)]
        yv = [(y >> k) & 1 for k in range(4)]
        E2A_TAB[x][y] = sum(xv[i] * E2A[i][j] * yv[j]
                            for i in range(4) for j in range(4)) % 2
ADD_I = [[x ^ y for y in range(16)] for x in range(16)]

TAU_B = [0] * 16
for x in range(16):
    xv = [(x >> k) & 1 for k in range(4)]
    img = [sum(MT[i][j] * xv[j] for j in range(4)) % 2 for i in range(4)]
    TAU_B[x] = img[0] | (img[1] << 1) | (img[2] << 2) | (img[3] << 3)
TAU2_B = [TAU_B[TAU_B[x]] for x in range(16)]

fix_tau = 4 - f2_rank([[(MT[i][j] + (1 if i == j else 0)) % 2
                        for j in range(4)] for i in range(4)])
ok_symp_tau = all(E2A_TAB[TAU_B[x]][TAU_B[y]] == E2A_TAB[x][y]
                  for x in range(16) for y in range(16))
check("S5.1 tau on A[2]: order 3 (tau != id, tau^3 = id), SYMPLECTIC for "
      "e_2, fixed-space dim = %d == 0 (REALIZATION-INDEPENDENT: "
      "N(omega - 1) = 9 is odd, so tau - 1 is a unit at 2 on every "
      "O-lattice) -- vs sigma-bar fixed-space dim = %d == 2"
      % (fix_tau, fix_sig),
      TAU_B != list(range(16)) and TAU2_B != list(range(16))
      and [TAU_B[TAU2_B[x]] for x in range(16)] == list(range(16))
      and ok_symp_tau and fix_tau == 0 and fix_sig == 2, kill="K5")

REFS_A = all_refinements(E2A_TAB, ADD_I)
zerosA = {q: sum(1 for b in q if b == 0) for q in REFS_A}
arf1_A = sorted(q for q in REFS_A if zerosA[q] == 6)
arf0_A = sorted(q for q in REFS_A if zerosA[q] == 10)
check("S5.2 curve refinement census: 16 refinements of e_2, 6 odd (Arf 1)"
      " + 10 even (Arf 0) -- the 6+10 theta-characteristic census",
      len(REFS_A) == 16 and len(arf1_A) == 6 and len(arf0_A) == 10,
      kill="K5")

tau_inv_A = [q for q in REFS_A
             if all(q[TAU_B[x]] == q[x] for x in range(16))]
check("S5.3 q_Theta: the tau-invariant refinement is UNIQUE (%d found; "
      "torsor + free tau argument) -- the refinement of the unique "
      "tau-fixed symmetric theta structure of the odd polarization"
      % len(tau_inv_A), len(tau_inv_A) == 1, kill="K5")
QTHETA = tau_inv_A[0]
arf_qtheta = 1 if zerosA[QTHETA] == 6 else 0
print("    q_Theta zeros = %d => Arf type %d (%s); code q* zeros = 6 => "
      "Arf 1 (odd)" % (zerosA[QTHETA], arf_qtheta,
                       "odd" if arf_qtheta else "EVEN"))

# internal K6 duad model on the curve side
duadA = {}
ok_duad = True
for v in range(1, 16):
    dv = [q for q in arf1_A if q[v] == 0]
    if len(dv) != 2:
        ok_duad = False
    duadA[v] = frozenset(dv)
check("S5.4 internal K6 duad model on the curve side: D(v) = {odd q : "
      "q(v) = 0} is a 2-set for all 15 v, bijective onto E(K6)",
      ok_duad and len(set(duadA.values())) == 15, kill="K5")

tau_inv_perm = [0] * 16
for x in range(16):
    tau_inv_perm[TAU_B[x]] = x
tau_on_odd = [arf1_A.index(act_on_ref(q, tau_inv_perm)) for q in arf1_A]
ct_tau = perm_cycle_type(tau_on_odd)
check("S5.5 tau permutes the 6 odd theta characteristics with cycle type "
      "%s == [3, 3] (syntheme side of S6) -- sigma-bar has %s (duad side):"
      " OUTER-related, never conjugate" % (ct_tau, ct_sig),
      ct_tau == [3, 3] and ct_sig == [3, 1, 1, 1])

SP_A = linear_maps_transporting(E2A_TAB, E2A_TAB)
stab_qT = [g for g in SP_A
           if all(QTHETA[g[x]] == QTHETA[x] for x in range(16))]
ginvs = []
for g in stab_qT:
    gi = [0] * 16
    for x in range(16):
        gi[g[x]] = x
    ginvs.append(gi)
orbs = []
seen = set()
for q in REFS_A:
    if q in seen:
        continue
    orb = {act_on_ref(q, gi) for gi in ginvs}
    seen |= orb
    orbs.append(orb)
osz = sorted(len(o) for o in orbs)
check("S5.6 Stab(q_Theta) has order %d == 72 (O^-(4,2): the EVEN "
      "stabilizer) and its refinement orbits are %s == [1, 6, 9] -- the "
      "curve-canonical decomposition is 1+6+9, NOT the code's 1+5+10"
      % (len(stab_qT), osz),
      len(stab_qT) == 72 and osz == [1, 6, 9])

# ======================================================================
# S6 -- THE DECIDER: the phi census over GL(4,2)
# ======================================================================
section("S6: the phi census -- all F2-linear isos A[2] -> V")

PAIR_PHIS = linear_maps_transporting(E2A_TAB, HB_B)
N_pair = len(PAIR_PHIS)
check("S6.1 N_pair = %d == 720: phis carrying e_2 -> hbar form an "
      "Sp(4,2)-torsor (both forms symplectic; this layer is content-free "
      "as a discriminator)" % N_pair, N_pair == 720, kill="K6")

N_sig_t = sum(1 for img in PAIR_PHIS
              if all(img[TAU_B[x]] == SIG_B[img[x]] for x in range(16)))
N_sig_t2 = sum(1 for img in PAIR_PHIS
               if all(img[TAU2_B[x]] == SIG_B[img[x]] for x in range(16)))
check("S6.2 sigma layer: phis with phi o tau = sigma-bar o phi: %d; with "
      "tau^2: %d -- BOTH ZERO (fixed-space 0 vs 2, cycle types [3,3] vs "
      "[3,1,1,1]: different Sp(4,2) classes)" % (N_sig_t, N_sig_t2),
      N_sig_t == 0 and N_sig_t2 == 0)

N_q = sum(1 for img in PAIR_PHIS
          if all(QSTAR_B[img[x]] == QTHETA[x] for x in range(16)))
# Arf-orbit variant: the transported refinement q_Theta o phi^{-1} has the
# same zero count as q_Theta (phi is a bijection), so it lands in the
# Arf-1 orbit iff zeros(q_Theta) == 6:
N_q_orbit = N_pair if zerosA[QTHETA] == 6 else 0
check("S6.3 refinement layer: phis with q* o phi = q_Theta: %d == 0; "
      "Arf-orbit variant (q_Theta into the Arf-1 orbit): %d == 0 -- "
      "q_Theta is EVEN (Arf 0, 10 zeros), q* is ODD (Arf 1, 6 zeros); "
      "Arf is a transport invariant" % (N_q, N_q_orbit),
      N_q == 0 and N_q_orbit == 0)

N_all = sum(1 for img in PAIR_PHIS
            if all(img[TAU_B[x]] == SIG_B[img[x]] for x in range(16))
            and all(QSTAR_B[img[x]] == QTHETA[x] for x in range(16)))
N_all2 = sum(1 for img in PAIR_PHIS
             if all(img[TAU2_B[x]] == SIG_B[img[x]] for x in range(16))
             and all(QSTAR_B[img[x]] == QTHETA[x] for x in range(16)))
check("S6.4 JOINT census (the decider): N_all = %d (tau) and %d (tau^2) "
      "-- expected torsor size for a canonical phi would be %d"
      % (N_all, N_all2, N_STAB), True)

blocked = (N_all == 0 and N_all2 == 0)
if blocked:
    print("    => transports of 1+5bar+10, the 3+2 slot split and the K6")
    print("       duad matching are BLOCKED (no joint phi); the curve's")
    print("       internal decomposition is 1+6+9 (S5.6), its 6 odd theta")
    print("       characteristics carry the K6 duads internally (S5.4)")
    print("       but with the deck acting as [3,3], not as the family")
    print("       3-cycle.")

# ======================================================================
# S7 -- controls (must fire) + positive control
# ======================================================================
section("S7: controls")

# C1: wrong pairing -- the non-alternating dot form admits no refinement
DOT_TAB = [[bin(x & y).count("1") % 2 for y in range(16)]
           for x in range(16)]
refs_dot = all_refinements(DOT_TAB, ADD_I)
check("C1 FIRES: the non-symplectic dot form admits %d == 0 quadratic "
      "refinements (alternation is forced)" % len(refs_dot),
      len(refs_dot) == 0, kill="K7")

# C2: wrong distinguished refinement -- an even/Arf-0 choice kills 1+5+10
q_even = arf0_V[0]
q_even_b = [0] * 16
for w in W16:
    q_even_b[TUP2INT[w]] = q_even[WIDX[w]]
n5 = sum(1 for x in range(1, 16) if q_even_b[x] == 0)
n10 = sum(1 for x in range(16) if q_even_b[x] == 1)
check("C2 FIRES: an even/Arf-0 distinguished refinement on the code side "
      "gives word split 1+%d+%d != 1+5+10 (the spinor decomposition "
      "dies); [informative: the even-even transporter has size 72, the "
      "even stabilizer]" % (n5, n10), (n5, n10) != (5, 10)
      and (n5, n10) == (9, 6), kill="K7")

# positive control CP: transport the code triple onto A[2] via phi0 --
# the machinery MUST reproduce the stabilizer census
img0 = PAIR_PHIS[0]
inv0 = [0] * 16
for x in range(16):
    inv0[img0[x]] = x
s0 = [inv0[SIG_B[img0[x]]] for x in range(16)]      # code sigma pulled back
q0 = [QSTAR_B[img0[x]] for x in range(16)]           # code q* pulled back
N_cp = sum(1 for img in PAIR_PHIS
           if all(img[s0[x]] == SIG_B[img[x]] for x in range(16))
           and all(QSTAR_B[img[x]] == q0[x] for x in range(16)))
check("CP POSITIVE CONTROL: the code clone on A[2] (sigma-bar and q* "
      "pulled back through a fixed pairing-phi) has joint census %d == "
      "%d == |joint stabilizer|: the census machinery CAN certify an "
      "isomorphism when one exists -- the zero in S6.4 is structural, "
      "not an artifact" % (N_cp, N_STAB), N_cp == N_STAB, kill="K7")

# C3: scrambled sigma -- conjugate the PASSING clone sigma by a frozen
# non-symplectic linear map (deterministic: the FIRST enumerated
# invertible R that is non-symplectic and pushes sigma out of Sp):
# the census must die
def int_to_map(m):
    cols = [(m >> (4 * k)) & 15 for k in range(4)]
    img = [0] * 16
    for x in range(16):
        v = 0
        for k in range(4):
            if x & (1 << k):
                v ^= cols[k]
        img[x] = v
    return img


R_B, s0_scr = None, None
for m in range(1, 1 << 16):
    img = int_to_map(m)
    if len(set(img)) != 16:
        continue
    if all(E2A_TAB[img[x]][img[y]] == E2A_TAB[x][y]
           for x in range(16) for y in range(16)):
        continue                        # symplectic: skip
    rinv = [0] * 16
    for x in range(16):
        rinv[img[x]] = x
    cand_s = [rinv[s0[img[x]]] for x in range(16)]
    if all(E2A_TAB[cand_s[x]][cand_s[y]] == E2A_TAB[x][y]
           for x in range(16) for y in range(16)):
        continue                        # scrambled sigma still in Sp: skip
    R_B, s0_scr = img, cand_s
    break
N_scr = sum(1 for img in PAIR_PHIS
            if all(img[s0_scr[x]] == SIG_B[img[x]] for x in range(16))
            and all(QSTAR_B[img[x]] == q0[x] for x in range(16)))
check("C3 FIRES: scrambling the clone sigma by the first enumerated "
      "NON-symplectic conjugation (scrambled sigma leaves Sp(e_2)) kills "
      "the passing census: %d -> %d" % (N_cp, N_scr),
      R_B is not None and N_scr == 0, kill="K7")

# C4: the elliptic factor cannot carry the structure (dimension)
dim_E2, dim_V = 2, 4
check("C4 FIRES: the omega-CM elliptic factor has E[2] = F2^2, dim %d != "
      "%d: no linear iso to V = F2^4 exists (dimension obstruction)"
      % (dim_E2, dim_V), dim_E2 != dim_V, kill="K7")

# ======================================================================
# S8 -- verdict (frozen rule)
# ======================================================================
section("S8: VERDICT (frozen enum: CURVE-CODE-ISOMORPHIC / "
        "CURVE-CODE-PARTIAL / CURVE-CODE-DEAD; TEST-VOID on control "
        "failure)")

controls_ok = all(ok for nm, ok in CHECKS
                  if nm.startswith(("C1", "C2", "C3", "C4", "CP")))
n_pass = sum(1 for _, ok in CHECKS if ok)
n_all_checks = len(CHECKS)
print("%d/%d checks passed" % (n_pass, n_all_checks))

if KILLS or not controls_ok:
    if not controls_ok:
        verdict = "TEST-VOID"
    else:
        verdict = "CURVE-CODE-DEAD"
        # a K-kill means a frozen layer broke before the census
elif N_all > 0 or N_all2 > 0:
    verdict = "CURVE-CODE-ISOMORPHIC"
elif N_pair > 0:
    verdict = "CURVE-CODE-PARTIAL"
else:
    verdict = "CURVE-CODE-DEAD"

print("VERDICT: %s" % verdict)
if verdict == "CURVE-CODE-PARTIAL":
    print()
    print("BREAKING LAYERS (named exactly):")
    print("  1. SIGMA LAYER: the deck 3-cycle tau acts FREELY on A[2]")
    print("     (fixed space 0; N(omega-1) = 9 odd -- realization-")
    print("     independent), cycle type [3,3] on the 6 odd theta")
    print("     characteristics (syntheme side); the code family cycle")
    print("     sigma-bar fixes a 2-plane, cycle type [3,1,1,1] (duad")
    print("     side).  The two order-3 classes are exchanged only by the")
    print("     OUTER automorphism of S6 -- never by conjugation.")
    print("     Equivariant phi census: 0 (tau and tau^2).")
    print("  2. REFINEMENT LAYER: the curve's canonical (deck-invariant)")
    print("     theta refinement q_Theta is EVEN (Arf 0, 10 zeros,")
    print("     stabilizer 72, decomposition 1+6+9); the code's q* is ODD")
    print("     (Arf 1, 6 zeros, stabilizer 120, decomposition 1+5+10).")
    print("     Arf is a transport invariant: census 0.")
    print("  SURVIVING SUB-STRUCTURE: (A[2], e_2) ~ (V, hbar) as bare")
    print("  symplectic F2^4 (720 phis -- content-free: all symplectic")
    print("  F2^4 are isomorphic) and the bare 6+10 census.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_all_checks
      else "CHECKS FAILED: %d" % (n_all_checks - n_pass))
raise SystemExit(0 if n_pass == n_all_checks else 1)
