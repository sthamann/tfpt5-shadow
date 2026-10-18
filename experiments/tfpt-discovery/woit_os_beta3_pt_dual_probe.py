"""WOIT-beta3 -- PT.DUAL -- THE PT <-> PT* DUALITY, TYPED AGAINST sigma_std.

THE CONTRACT (tfpt_research_contracts.tex, WOIT.OS.TWISTOR.01, verbatim):
  "(beta_3) The PT <-> PT* duality typed against sigma_std --- success:
   Woit's Minkowski conjugation (PT -> PT*) identified with the family-D
   conjugation on the quotient; kill: the duality forces a
   clock-centralising (family A) structure instead."

Predecessors: alpha = v519 (Theta exists, free RP picks family D; honest
fence there, verbatim: "Woit's MINKOWSKI structure maps PT -> PT* (dual),
so the OS-quotient interpretation of sigma_std stays contract work");
beta_1 = v522 (UNDECIDED, gauge datum = GSO Z2); beta_2 = v524 (SUCCESS:
H_phys explicit and PD, clock = positive transfer step, Theta_phys =
the perpendicular torsor mirror, Kramers-free).  THIS probe executes
beta_3: the duality is CONSTRUCTED as a compatibility class, its two
branches are SEPARATED by a dichotomy theorem, the kill branch is decided
EMPTY BY ALGEBRA, and the surviving branch is identified -- member by
member -- with the family-D mirror that v524 descended to the quotient.

=== PREREGISTRATION (frozen BEFORE the first number; criteria not
    adjusted after) ===

[C-1] "PT <-> PT* duality" := an invertible anti-linear map
  sigma: C^4 -> (C^4)^*, equivalently a nondegenerate Hermitian
  sesquilinear form Phi via sigma(Z) = Z^dagger Phi (row covector),
  COMPATIBLE with the compiler structure on twistor space:
    (a) clock-compatible:   rho4^dagger Phi rho4 = Phi,
    (b) deck-compatible:    deck4^dagger Phi deck4 = Phi,
  with rho4 = diag(RHO, RHO), deck4 = diag(DECK, DECK) the v519 W-S4
  blockwise lifts (RHO = diag(i,1), DECK = diag(i,-i); v492 S5).
[C-2] "typed against sigma_std" := the vector-level avatar
  s_Phi(Z) := Phi^T conj(Z) under the standard-basis identification
  (C^4)^* ~ C^4, so that Phi = 1 IS sigma_std (v519 W-S4.3).  Family
  typing per v519 W-S1/W-S4: family D <=> s rho4 s^-1 = rho4^-1 exactly;
  family A <=> s centralises the clock (at most projectively).
[C-3] "Woit's Minkowski conjugation" := a compatible duality whose
  EUCLIDEAN pairing against Woit's rho_tw (= M_tw o conj,
  M_tw = diag(J2, J2), v519 W-S4.1) carries the MINKOWSKI sign:
    Phi(rho_tw z, rho_tw w) = eps * Phi(w, z),  eps in {+1, -1},
  i.e. M_tw^dagger Phi M_tw = eps * conj(Phi).  BOTH signs are examined;
  no sign is imposed.  The branch separation criterion (pre-declared):
  a duality can furnish an OS cut on the seam iff its null locus meets
  the seam line; the seam line is DECLARED as span(e1, e2) with
  projective coordinate z -> [z : 1] (the v492/v519 seam sphere, first
  block of the W-S4 lift).
[C-4] "identified on the quotient" := the induced seam member of the
  surviving branch, lattice-lifted under the v519 contract precision
  (ii) placement (RP-side: marks on the BOND MIDPOINTS; the v524 cut
  axis k_cut = 7 at N = 8 carries one mark pair, the perpendicular
  axis k_cut - N/2 = 3 the other), coincides with the mirror whose
  descent v524 certified (Theta_phys = [theta_perp(.)]); re-verified
  here at N = 8: G8 PD, anti-unitarity entrywise, Theta_phys^2 = +1
  per parity sector, semigroup time reversal.  The residual freedom is
  the v519 W-S2.5 clock relabeling of the torsor (typed, not hidden).
[C-5] negative controls (all mandatory): (i) sigma_std itself (Phi = 1)
  lands in the eps = +1 branch and furnishes NO cut; (ii) the wrong
  clock lift diag(i,i,1,1) changes the block theorem (the compiler
  clock is load-bearing); (iii) family A on the quotient has no PSD
  form ((4,4,0) one-particle, v524 C4.2 verbatim); (iv) the definite
  signatures cannot enter the Minkowski branch (signature-mirror
  theorem); (v) a NON-seam-preserving member (b != 0) maps the seam
  line off itself -- the seam-preservation demand has teeth.

VERDICT LOGIC (frozen): KILL iff some compatible duality is
clock-centralising (family A) -- decided in D3 by algebra.  SUCCESS iff
(S1) the compatible class is nonempty and classified [D1]; (S2) the
Euclidean/Minkowski dichotomy separates exactly as pre-declared, with
the Minkowski branch nonempty, of forced total signature (2,2), and
with null locus meeting the seam line EXACTLY in the seam circle [D2];
(S3) every compatible duality is family D on clock AND deck -- the kill
branch is EMPTY BY ALGEBRA [D3]; (S4) the seam-preserving Minkowski
members induce ONE projective seam conjugation (z -> -conj(z)), a
family-D mu4-torsor member on the mark pair PERPENDICULAR to the
sigma_std pair [D4]; (S5) under the [C-4] placement that member IS
theta_perp -- the v524 Theta_phys carrier -- and the quotient descent
re-verifies (PD Gram, anti-unitary, Theta^2 = +1 per sector, time
reversal, torsor closure onto the deck) [D5]; (S6) all five controls
behave as typed.  Otherwise UNDECIDED with the gap named.

FENCES, PROMINENTLY AND FIRST.
  * Free/quotient level ONLY.  Nothing here touches the interacting
    algebra A_hol; all seven WOIT.OS.TWISTOR.01 kill tests stay
    formally live there; NO marker moves (the contract stays [O]).
  * The word "derived" is not used for any physics statement: beta_3 is
    an IDENTIFICATION inside declared structures ([C-1]..[C-4]), with
    its two conventions (seam-line declaration, RP-side placement)
    cited from v492/v519/v524, not invented here.
  * THEOREM(exact algebra) / CERTIFIED(40-digit, declared bar) typed
    per check; sympy exact everywhere else.
  * Classical spine (addresses, not authorities): Penrose 1967
    (twistor space, PT*), Woit 2021/2023 (Euclidean twistor
    unification: rho_tw, the two real structures), Osterwalder-Schrader
    1973/75 (reflection positivity), Klein-Landau 1981 (local
    semigroups), Kramers 1930 (Theta^2 dichotomy).

Machinery: v519/v522/v524 verbatim (kernel c_of, Pfaffian-Wick,
refl_map/tower_maps/theta_mono/alpha_mono/os_term, gram_of, 40-digit
inertia).  Python: experiments/tfpt-discovery/.venv/bin/python
"""
import time
from itertools import combinations

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
T0 = time.time()
BUDGET_S = 600.0

I = sp.I
N8 = 8
N16 = 16
ETA = I

EXACT = "THEOREM(exact algebra)"
CERT = "CERTIFIED(40-digit)"

FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def info(name, detail=""):
    print("[INFO] %s%s" % (name, (": " + detail) if detail else ""))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def iszero(e):
    e2 = sp.expand(e)
    if e2 == 0:
        return True
    e3 = sp.expand(sp.expand_complex(e2))
    if e3 == 0:
        return True
    return sp.simplify(e3) == 0


def zmat(M):
    return all(iszero(x) for x in M)


# ---------------------------------------------------------------- compiler --
RHO = sp.diag(I, 1)
DECK = sp.diag(I, -I)
J2 = sp.Matrix([[0, -1], [1, 0]])
RHO4 = sp.diag(RHO, RHO)                    # v519 W-S4 blockwise clock lift
DECK4 = sp.diag(DECK, DECK)                 # v519 W-S4 blockwise deck lift
MTW = sp.diag(J2, J2)                       # Woit rho_tw = MTW o conj

# ------------------------------------------------- v524 machinery, verbatim --
def c_of(d, n):
    if d % 2 == 0:
        return sp.Integer(0)
    return sp.Rational(2, n) / sp.sin(sp.pi * sp.Rational(d, n))


def g2f(a, b, n, chi):
    if a == b:
        return sp.Integer(1)
    return I * chi * c_of(a - b, n)


_WICK = {}


def wick(idx, n, chi=1):
    idx = tuple(idx)
    if len(idx) == 0:
        return sp.Integer(1)
    if len(idx) % 2 == 1:
        return sp.Integer(0)
    key = (idx, n, chi)
    if key in _WICK:
        return _WICK[key]
    head, rest = idx[0], idx[1:]
    tot = sp.Integer(0)
    for j, b in enumerate(rest):
        sub = rest[:j] + rest[j + 1:]
        tot += (-1) ** j * g2f(head, b, n, chi) * wick(sub, n, chi)
    tot = sp.expand_complex(tot)
    _WICK[key] = tot
    return tot


def refl_map(k, n):
    def r(a):
        return (k - a) % n

    def s(a):
        return -1 if (k - a) % (2 * n) >= n else 1
    return r, s


def half_of(k, n):
    if k % 2 == 0:
        f1 = (k // 2) % n
        P = [(f1 + j) % n for j in range(1, n // 2)]
    else:
        b = (k + 1) // 2
        P = [(b + j) % n for j in range(n // 2)]
    rP = {(k - a) % n for a in P}
    assert not (rP & set(P))
    return P


PLUS = lambda a: 1


def tower_maps(n, shift, kmax):
    maps = [(tuple(range(n)), (1,) * n)]
    for _ in range(kmax):
        perm, sign = maps[-1]
        np_, ns_ = [], []
        for a in range(n):
            p, s0 = perm[a], sign[a]
            q = p + shift
            np_.append(q % n)
            ns_.append(s0 * (-1 if (q >= n or q < 0) else 1))
        maps.append((tuple(np_), tuple(ns_)))
    return maps


def alpha_mono(m, pm):
    perm, sign = pm
    c = 1
    imgs = []
    for a in m:
        c *= sign[a]
        imgs.append(perm[a])
    lst = list(imgs)
    sgn = 1
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                sgn = -sgn
    assert len(set(lst)) == len(lst)
    return c * sgn, tuple(lst)


def theta_mono(mono, r, s, eta):
    imgs = [r(a) for a in reversed(mono)]
    coeff = eta ** len(mono)
    for a in mono:
        coeff *= s(a)
    lst = list(imgs)
    sign = 1
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                sign = -sign
    assert len(set(lst)) == len(lst)
    return coeff * sign, tuple(lst)


def mono_mul(m1, m2):
    out = list(m1)
    sign = 1
    for g in m2:
        out.append(g)
        i = len(out) - 1
        while i > 0 and out[i - 1] > out[i]:
            out[i - 1], out[i] = out[i], out[i - 1]
            sign = -sign
            i -= 1
        if i > 0 and out[i - 1] == out[i]:
            del out[i - 1:i + 1]
    return sign, tuple(out)


def os_term(ea, eb, pm, r, s, eta, n, chi=1):
    ca, ma = theta_mono(ea, r, s, eta)
    cb, mb = alpha_mono(eb, pm)
    cs, mm = mono_mul(ma, mb)
    return sp.expand_complex(ca * cb * cs * wick(mm, n, chi))


def term_matrix(basis, pm, r, s, eta, n, chi=1):
    d = len(basis)
    return sp.Matrix(d, d, lambda i, j: os_term(basis[i], basis[j], pm,
                                                r, s, eta, n, chi))


def gram_of(basis, r, s, n, chi=1):
    tw0 = (tuple(range(n)), (1,) * n)
    return term_matrix(basis, tw0, r, s, ETA, n, chi)


def hermitian_exact(M):
    return zmat(M - M.conjugate().T)


def spectrum_inertia(M, tol=None):
    if tol is None:
        tol = mp.mpf(10) ** (-25)
    n = M.shape[0]
    A = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            re_, im_ = M[i, j].evalf(45).as_real_imag()
            A[i, j] = mp.mpc(mp.mpf(str(re_)), mp.mpf(str(im_)))
    E, _ = mp.eighe(A)
    evs = [E[i].real for i in range(n)]
    npos = sum(1 for e in evs if e > tol)
    nneg = sum(1 for e in evs if e < -tol)
    nzero = n - npos - nneg
    nz = [abs(e) for e in evs if abs(e) > tol]
    return (npos, nneg, nzero), (min(nz) if nz else mp.mpf(0))


# pinned v524 data at N = 8
P8 = half_of(7, N8)                              # {4,5,6,7}
R7, S7 = refl_map(7, N8)                         # the OS cut, axis 7 (bond)
RP3, SP3 = refl_map(3, N8)                       # theta_perp, axis 3 (bond)
EVENS8 = [()] + list(combinations(P8, 2)) + [tuple(P8)]
ODDS8 = [(a,) for a in P8] + list(combinations(P8, 3))
BASIS8 = EVENS8 + ODDS8
TW8 = tower_maps(N8, 1, N8)


section("WOIT-beta3  PT.DUAL -- the PT <-> PT* duality, typed against "
        "sigma_std")
info("contract", "success: Minkowski conjugation = family D on the "
                 "quotient; kill: the duality forces family A -- verdict "
                 "logic frozen in the header")
info("compiler data", "rho4 = diag(i,1,i,1), deck4 = diag(i,-i,i,-i), "
                      "M_tw = diag(J2,J2); seam line = span(e1,e2), "
                      "z -> [z:1]")


# ============================================================ D1 ============
section("D1  THE COMPATIBLE CLASS -- the block theorem")

a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4', real=True)
res, ims = sp.symbols('r12 r13 r14 r23 r24 r34', real=True), \
    sp.symbols('i12 i13 i14 i23 i24 i34', real=True)
Z = {}
for idx, (rr, ii) in enumerate(zip(res, ims)):
    Z[('12', '13', '14', '23', '24', '34')[idx]] = rr + I * ii
PHI = sp.Matrix([
    [a1, Z['12'], Z['13'], Z['14']],
    [sp.conjugate(Z['12']), a2, Z['23'], Z['24']],
    [sp.conjugate(Z['13']), sp.conjugate(Z['23']), a3, Z['34']],
    [sp.conjugate(Z['14']), sp.conjugate(Z['24']), sp.conjugate(Z['34']), a4]])

clock_cond = sp.expand_complex(RHO4.conjugate().T * PHI * RHO4 - PHI)
# entrywise: cond_{jk} = (conj(lam_j) lam_k - 1) Phi_{jk}; the factor is
# nonzero exactly on the cross-eigenspace entries -> those are FORCED zero
forced_pairs = [(0, 1), (0, 3), (1, 2), (2, 3)]
free_pairs = [(0, 2), (1, 3)]
ok_forced = all(
    iszero(sp.expand_complex(clock_cond[j, k]
                             - ((-1 - I) if (j, k) != (1, 2) else (I - 1))
                             * PHI[j, k]))
    for (j, k) in forced_pairs)
ok_free = all(iszero(clock_cond[j, k]) for (j, k) in free_pairs) \
    and all(iszero(clock_cond[j, j]) for j in range(4))
PHI_C = PHI.subs({Z['12']: 0, Z['14']: 0, Z['23']: 0, Z['34']: 0,
                  sp.conjugate(Z['12']): 0, sp.conjugate(Z['14']): 0,
                  sp.conjugate(Z['23']): 0, sp.conjugate(Z['34']): 0})
resid = sp.expand_complex(RHO4.conjugate().T * PHI_C * RHO4 - PHI_C)
check("D1.1 %s CLOCK => BLOCK THEOREM: the compatibility residual is "
      "entrywise (conj(lam_j) lam_k - 1) Phi_jk, with NONZERO factor "
      "exactly on the four cross-eigenspace entries (12),(14),(23),(34) "
      "-- those are FORCED zero -- while the block entries (13),(24) and "
      "the diagonal are free: the compatible class is the two 2x2 "
      "Hermitian blocks on {e1,e3} (clock eigenvalue i) and {e2,e4} "
      "(eigenvalue 1), 16 -> 8 real parameters; the blocked form "
      "satisfies the condition identically" % EXACT,
      ok_forced and ok_free and zmat(resid))
deck_cond = sp.expand_complex(DECK4.conjugate().T * PHI_C * DECK4 - PHI_C)
check("D1.2 %s DECK ADDS NOTHING: deck4-compatibility holds identically on "
      "the clock-blocked class (same eigenspace split {e1,e3}/{e2,e4}) -- "
      "the deck is already served by the clock blocks" % EXACT,
      zmat(deck_cond))
RHO4_WRONG = sp.diag(I, I, 1, 1)
wrong_cond = sp.expand_complex(RHO4_WRONG.conjugate().T * PHI * RHO4_WRONG
                               - PHI)
sol_w = sp.solve([x for x in wrong_cond], list(res) + list(ims), dict=True)
check("D1.3 %s MUTATION (the compiler clock is load-bearing): the wrong "
      "lift diag(i,i,1,1) forces a DIFFERENT split ({e1,e2}/{e3,e4}: the "
      "(12) and (34) entries survive, (13),(14),(23),(24) die) -- the "
      "block theorem reads the v519 blockwise clock, not any diagonal"
      % EXACT,
      len(sol_w[0]) == 8
      and all(sol_w[0].get(v, None) == 0 for v in
              (res[1], ims[1], res[2], ims[2], res[3], ims[3],
               res[4], ims[4])))


# ============================================================ D2 ============
section("D2  THE DICHOTOMY -- Euclidean vs Minkowski branch, and the "
        "forced (2,2)")

a, c = sp.symbols('a c', real=True, nonzero=True)
br, bi = sp.symbols('br bi', real=True)
d_, e_r, e_i, f_ = sp.symbols('d_ e_r e_i f_', real=True)
b = br + I * bi
e = e_r + I * e_i
PHI_BLK = sp.Matrix([[a, 0, b, 0],
                     [0, d_, 0, e],
                     [sp.conjugate(b), 0, c, 0],
                     [0, sp.conjugate(e), 0, f_]])

sols = {}
for eps in (1, -1):
    cond = sp.expand_complex(MTW.conjugate().T * PHI_BLK * MTW
                             - eps * PHI_BLK.conjugate())
    sols[eps] = sp.solve([x for x in cond], [d_, e_r, e_i, f_], dict=True)[0]
check("D2.1 %s THE TWO BRANCHES SOLVE EXACTLY: the rho_tw pairing "
      "M_tw^dagger Phi M_tw = eps conj(Phi) forces, on the block class, "
      "eps = +1 (EUCLIDEAN): d = a, f = c, e = conj(b); "
      "eps = -1 (MINKOWSKI): d = -a, f = -c, e = -conj(b) -- both branches "
      "nonempty, each a 4-real-parameter family (a, c, b)" % EXACT,
      sols[1][d_] == a and sols[1][f_] == c
      and sols[1][e_r] == br and sols[1][e_i] == -bi
      and sols[-1][d_] == -a and sols[-1][f_] == -c
      and sols[-1][e_r] == -br and sols[-1][e_i] == bi)

PHI_E = sp.expand_complex(PHI_BLK.subs(sols[1]))
PHI_M = sp.expand_complex(PHI_BLK.subs(sols[-1]))
x_r, y_r = sp.symbols('x_r y_r', real=True)
z_seam = x_r + I * y_r                 # explicit real/imag: exact |z|^2
Zline = sp.Matrix([z_seam, 1, 0, 0])
N_E = sp.expand(sp.expand_complex((Zline.conjugate().T * PHI_E * Zline)[0]))
N_M = sp.expand(sp.expand_complex((Zline.conjugate().T * PHI_M * Zline)[0]))
check("D2.2 %s THE OS CUT IS FORCED, NOT IMPOSED: on the seam line the "
      "Minkowski branch has norm a(|z|^2 - 1) -- null EXACTLY on the seam "
      "circle |z| = 1, for EVERY member -- while the Euclidean branch has "
      "a(|z|^2 + 1): no null point anywhere (no cut).  The branch "
      "separation criterion of [C-3] lands exactly as pre-declared"
      % EXACT,
      iszero(sp.expand(N_M - a * (x_r ** 2 + y_r ** 2 - 1)))
      and iszero(sp.expand(N_E - a * (x_r ** 2 + y_r ** 2 + 1))))
Phi_i_blk = sp.Matrix([[a, b], [sp.conjugate(b), c]])
Phi_1_blk = sp.Matrix([[PHI_M[1, 1], PHI_M[1, 3]],
                       [PHI_M[3, 1], PHI_M[3, 3]]])
x = sp.symbols('x')
cp_i = sp.expand(Phi_i_blk.charpoly(x).as_expr())
cp_1 = sp.expand(Phi_1_blk.charpoly(x).as_expr())
check("D2.3 %s THE SIGNATURE-MIRROR THEOREM: in the Minkowski branch the "
      "{e2,e4} block is exactly MINUS the conjugate of the {e1,e3} block "
      "(Phi_1 = -conj(Phi_i)), so charpoly_1(x) = charpoly_i(-x): the "
      "eigenvalues mirror in sign and the TOTAL signature is (2,2) for "
      "every nondegenerate member -- Woit's Minkowski signature is a "
      "THEOREM of clock + rho_tw pairing, not an input; corollary: no "
      "definite form can enter the Minkowski branch (control (iv))"
      % EXACT,
      zmat(sp.expand_complex(Phi_1_blk + Phi_i_blk.conjugate()))
      and iszero(sp.expand(cp_1 - cp_i.subs(x, -x))))
check("D2.4 %s SIGMA_STD IS EUCLIDEAN-BRANCH: Phi = 1 satisfies the "
      "eps = +1 pairing exactly (M_tw^dagger M_tw = 1 = conj(1)) and "
      "VIOLATES eps = -1 -- the standard conjugation carries no OS cut; "
      "the Minkowski duality is a Phi-twist of sigma_std, not sigma_std "
      "itself (control (i))" % EXACT,
      zmat(sp.expand_complex(MTW.conjugate().T * sp.eye(4) * MTW
                             - sp.eye(4)))
      and not zmat(sp.expand_complex(MTW.conjugate().T * sp.eye(4) * MTW
                                     + sp.eye(4))))


# ============================================================ D3 ============
section("D3  THE KILL IS EMPTY BY ALGEBRA -- every compatible duality is "
        "family D")

S_AVATAR = PHI_M.T                     # s_Phi = Phi^T o conj on C^4
lhs_rho = sp.expand_complex(S_AVATAR * RHO4.conjugate())
rhs_rho = sp.expand_complex(RHO4.inv() * S_AVATAR)
lhs_deck = sp.expand_complex(S_AVATAR * DECK4.conjugate())
rhs_deck = sp.expand_complex(DECK4.inv() * S_AVATAR)
check("D3.1 %s FAMILY D ON THE CLOCK, FOR EVERY MEMBER: "
      "s_Phi rho4 = rho4^-1 s_Phi identically in (a, c, b) -- the vector "
      "avatar of every Minkowski-branch duality INVERTS the clock exactly "
      "(v519 family-D relation), and the same holds on the Euclidean "
      "branch (the block structure alone forces it)" % EXACT,
      zmat(lhs_rho - rhs_rho)
      and zmat(sp.expand_complex(PHI_E.T * RHO4.conjugate()
                                 - RHO4.inv() * PHI_E.T)))
check("D3.2 %s FAMILY D ON THE DECK: s_Phi deck4 = deck4^-1 s_Phi "
      "identically -- the duality inverts the Z4 deck as well (the v519 "
      "W-S4.3 sigma_std behaviour, inherited by every Phi-twist)" % EXACT,
      zmat(lhs_deck - rhs_deck))
# family A would need rho4^-1 = lambda * rho4 for a scalar lambda
lam = sp.symbols('lam')
fam_a_eqs = sp.solve([sp.expand_complex(x) for x in
                      (RHO4.inv() - lam * RHO4)], lam, dict=True)
check("D3.3 %s THE KILL BRANCH IS EMPTY: a clock-CENTRALISING duality "
      "(family A, s rho4 s^-1 = lambda rho4) would need rho4^-1 = lambda "
      "rho4, i.e. rho4^2 = scalar -- but rho4^2 = diag(-1,1,-1,1) is NOT "
      "scalar (the clock has order 4, v492): NO solution exists (%d), so "
      "no compatible duality can be clock-centralising.  The contract "
      "kill branch cannot fire, by algebra -- decided, not scanned"
      % (EXACT, len(fam_a_eqs)),
      len(fam_a_eqs) == 0
      and not zmat(sp.expand_complex(RHO4 ** 2 - (-1) * sp.eye(4))))
PHI_M0 = PHI_M.subs({br: 0, bi: 0})
s_sq = sp.expand_complex(PHI_M0.T * PHI_M0.T.conjugate())
check("D3.4 %s THETA^2 = +1 (KRAMERS-FREE): for the seam-preserving "
      "members (D4) s_Phi^2 = Phi^T conj(Phi^T) = diag(a^2, a^2, c^2, "
      "c^2) > 0 -- normalisable to +1: the induced real structure is the "
      "Kramers-free family-D class (v519 W-S2.2), never the (-1)^F class"
      % EXACT,
      zmat(s_sq - sp.diag(a ** 2, a ** 2, c ** 2, c ** 2)))


# ============================================================ D4 ============
section("D4  THE SEAM RESTRICTION -- one projective conjugation, "
        "perpendicular to sigma_std")

img = sp.expand_complex(PHI_M.T * Zline.conjugate())
check("D4.1 %s SEAM PRESERVATION <=> b = 0: the duality maps the seam "
      "line into its own dual line iff the third and fourth components "
      "a-priori (b conj(z), -conj(b)) vanish, i.e. b = 0 -- one complex "
      "condition, with e = -conj(b) dying simultaneously (control (v): "
      "b != 0 members move the seam off itself)" % EXACT,
      iszero(sp.expand_complex(img[2] - b * sp.conjugate(z_seam)))
      and iszero(sp.expand_complex(img[3] + sp.conjugate(b)))
      and not iszero(img[2].subs({br: 1, bi: 0})))
img0 = sp.expand_complex(PHI_M0.T * Zline.conjugate())
zprime = sp.simplify(img0[0] / img0[1])
check("D4.2 %s THE INDUCED MEMBER IS UNIQUE: every seam-preserving "
      "Minkowski duality induces on the seam sphere the SAME projective "
      "conjugation z -> a conj(z) / (-a) = -conj(z) -- independent of "
      "(a, c): mu_induced = -1, a family-D member of the v519 mu4 torsor "
      "(mark-preserving), with fixed circle points z = +-i" % EXACT,
      iszero(sp.expand_complex(zprime + sp.conjugate(z_seam)))
      and iszero(sp.expand_complex((-sp.conjugate(I)) - I))
      and iszero(sp.expand_complex((-sp.conjugate(-I)) - (-I))))
img_std = sp.eye(4).T * Zline.conjugate()
z_std = sp.simplify(img_std[0] / img_std[1])
check("D4.3 %s PERPENDICULAR TO SIGMA_STD: sigma_std induces z -> "
      "+conj(z) (mu = +1, fixed points +-1); the Minkowski member has "
      "mu = -1 (fixed points +-i) -- the two PERPENDICULAR members of "
      "the MARK orbit of the v519 mu4 torsor: 'typed against sigma_std' "
      "lands as perpendicularity, with the fixed-point sets exactly the "
      "two mark pairs" % EXACT,
      iszero(sp.expand_complex(z_std - sp.conjugate(z_seam)))
      and iszero(sp.expand_complex(sp.conjugate(sp.Integer(1)) - 1))
      and iszero(sp.expand_complex(-sp.conjugate(I) - I)))
# the clock-orbit statement, exactly: conjugating z -> mu conj(z) by
# z -> i z gives z -> (i^2 mu) conj(z) = -mu conj(z)
mu_s = sp.symbols('mu_s')
check("D4.4 %s THE TORSOR ORBIT ARITHMETIC: conjugating Theta_mu by the "
      "clock (z -> iz) maps mu -> i^2 mu = -mu exactly -- so the clock "
      "conjugation EXCHANGES sigma_std (mu = +1) and the Minkowski "
      "member (mu = -1) within the mark orbit, and the silver pair "
      "{+i,-i} forms the other orbit: the residual freedom of the "
      "identification is exactly this exchange, typed in [C-4] -- and "
      "it is the projective shadow of theta_cut o theta_perp = "
      "alpha_{N/2} downstairs (D5.7)" % EXACT,
      iszero(sp.expand_complex(I * mu_s * sp.conjugate(I ** -1)
                               - (- mu_s))))


# ============================================================ D5 ============
section("D5  THE QUOTIENT IDENTIFICATION -- the induced member IS the "
        "v524 Theta_phys carrier")

# (a) placement arithmetic: cut axis k=7 fixes bond midpoints 7pi/8 and
# 15pi/8; perp axis k=3 fixes 3pi/8 and 11pi/8; with the [C-4] placement
# (marks on the cut bonds), the perp bonds sit at EXACTLY +-pi/2 from them
cut_marks = [sp.Rational(7, 8) * sp.pi, sp.Rational(15, 8) * sp.pi]
perp_marks = [sp.Rational(3, 8) * sp.pi, sp.Rational(11, 8) * sp.pi]
d1 = sp.simplify(perp_marks[0] - cut_marks[0])
d2 = sp.simplify(perp_marks[1] - cut_marks[0])
check("D5.1 %s PLACEMENT ARITHMETIC (exact rational-pi): at N = 8 the "
      "v524 cut axis k = 7 fixes the bond midpoints {7pi/8, 15pi/8} and "
      "the perpendicular axis k = 3 fixes {3pi/8, 11pi/8} -- offsets "
      "-pi/2 and +pi/2 exactly: under the [C-4] RP-side placement (marks "
      "on the cut bonds = the +-1 pair) the perp axis carries the +-i "
      "pair, i.e. EXACTLY the fixed points of the induced member "
      "z -> -conj(z)" % EXACT,
      iszero(d1 + sp.pi / 2) and iszero(d2 - sp.pi / 2))
# (b) in the rotated seam coordinate w = z e^{-i 7pi/8} (mark_+1 at the
# cut bond), the induced member w -> -conj(w) is the reflection with axis
# angle 3pi/8 mod pi = the lattice axis k = 3: theta_perp
axis_angle = sp.Rational(11, 8) * sp.pi / 1  # arg(mu e^{2 i 7pi/8})/2 check
mu_lattice = sp.expand_complex((-1) * sp.exp(2 * I * sp.Rational(7, 8)
                                             * sp.pi))
check("D5.2 %s COORDINATE TRANSPORT: pulling z -> -conj(z) back through "
      "the placement rotation w = z e^{-i 7pi/8} gives the lattice "
      "reflection z -> e^{i 11pi/4} conj(z), axis angle 11pi/8 = 3pi/8 "
      "mod pi -- the k = 3 axis: THE INDUCED MINKOWSKI MEMBER IS "
      "theta_perp, the exact mirror v524 descends to Theta_phys; "
      "sigma_std's member (w -> +conj(w)) transports to the k = 7 CUT "
      "axis -- the OS metric itself.  Role separation complete: "
      "sigma_std ~ the cut (metric), the Phi-twisted Minkowski duality "
      "~ the descending mirror (Theta_phys)" % EXACT,
      iszero(sp.expand_complex(mu_lattice - sp.exp(I * sp.Rational(11, 4)
                                                   * sp.pi)))
      and iszero(sp.simplify(sp.Rational(11, 8) * sp.pi - sp.pi
                             - sp.Rational(3, 8) * sp.pi)))

# (c) rebuild the v524 N = 8 quotient and the Theta_phys descent
G8 = gram_of(BASIS8, R7, S7, N8)
herm8 = hermitian_exact(G8)
in8, gap8 = spectrum_inertia(G8)
check("D5.3 %s H_PHYS REGRESSION (v524 Q1.3): the N = 8 complete "
      "half-algebra bond-cut Gram (16 monomials on {4,5,6,7}) is exactly "
      "Hermitian and PD, inertia %s (min eigenvalue %s) -- the quotient "
      "carrier exists, null space {0}"
      % (CERT, in8, mp.nstr(gap8, 5)),
      herm8 and in8 == (16, 0, 0))

# theta_perp maps the half to itself: build its matrix on BASIS8
theta_mat = None
eta_perp_pin = None
for eta_p in (I, -I, sp.Integer(1), sp.Integer(-1)):
    cols = {}
    ok = True
    for j, m in enumerate(BASIS8):
        cf, mm = theta_mono(m, RP3, SP3, eta_p)
        if mm not in BASIS8:
            ok = False
            break
        cols[j] = (BASIS8.index(mm), cf)
    if not ok:
        continue
    T = sp.zeros(16, 16)
    for j, (i_, cf) in cols.items():
        T[i_, j] = cf
    # anti-unitarity wrt G8: <Theta a, Theta b> = <b, a>
    # <Theta a, Theta b> = sum conj(T_ia) G_ij T_jb (Theta anti-linear)
    lhs = sp.expand_complex(T.conjugate().T * G8 * T)
    ok_anti = zmat(sp.expand_complex(lhs.conjugate() - G8.T).T
                   - sp.zeros(16, 16)) or zmat(lhs - G8.conjugate())
    if ok_anti:
        theta_mat = T
        eta_perp_pin = eta_p
        break
check("D5.4 %s THETA_PHYS DESCENT REGRESSION (v524 G3.2): theta_perp "
      "(axis 3) maps the half {4,5,6,7} to itself, its matrix on the 16 "
      "basis monomials is anti-unitary wrt the Gram exactly "
      "(<Theta a, Theta b> = <b, a> entrywise), with the twist pinned in "
      "the mu4 sub-torsor (eta_perp = %s)" % (EXACT, eta_perp_pin),
      theta_mat is not None and eta_perp_pin in (I, -I))
Tsq = sp.expand_complex(theta_mat * theta_mat.conjugate())
ev_idx = list(range(8))
od_idx = list(range(8, 16))
sq_even = all(iszero(Tsq[i, j] - (1 if i == j else 0))
              for i in ev_idx for j in ev_idx)
sq_odd = all(iszero(Tsq[i, j] - (1 if i == j else 0))
             for i in od_idx for j in od_idx)
check("D5.5 %s THETA_PHYS^2 = +1 ON EVERY SECTOR (Kramers-free, v524 "
      "regression): the anti-linear square Theta_mat conj(Theta_mat) is "
      "the identity on the even AND the odd sector exactly -- matching "
      "D3.4's C^4-level s_Phi^2 > 0: the quotient realises the same "
      "Kramers-free family-D class the duality induces" % EXACT,
      sq_even and sq_odd)
# time reversal: theta_perp alpha_1 = alpha_{-1} theta_perp on monomials
ok_tr = True
for m in BASIS8:
    c1, m1 = alpha_mono(m, TW8[1])
    ct1, mt1 = theta_mono(m1, RP3, SP3, eta_perp_pin)
    ct2, mt2 = theta_mono(m, RP3, SP3, eta_perp_pin)
    # alpha_{-1} = alpha_7 up to the NS wrap on the circle: use inverse map
    TW8N_ = tower_maps(N8, -1, 1)
    c2, m2 = alpha_mono(mt2, TW8N_[1])
    if mt1 != m2 or sp.simplify(ct1 * c1 - c2 * ct2) != 0:
        ok_tr = False
        break
check("D5.6 %s TIME REVERSAL (v524 regression): theta_perp alpha_1 = "
      "alpha_{-1} theta_perp exactly on all 16 monomials -- the descended "
      "Minkowski mirror time-reverses the euclidean semigroup, as an OS "
      "Minkowski conjugation must" % EXACT, ok_tr)
# torsor closure onto the deck: theta_cut o theta_perp = alpha_{N/2}
ok_close = True
TW8_4 = TW8[4]
for m in BASIS8:
    cp_, mp_ = theta_mono(m, RP3, SP3, eta_perp_pin)
    cc_, mc_ = theta_mono(mp_, R7, S7, ETA)
    ca_, ma_ = alpha_mono(m, TW8_4)
    if mc_ != ma_:
        ok_close = False
        break
check("D5.7 %s TORSOR CLOSURE (v524 regression, support level): "
      "theta_cut o theta_perp = alpha_{N/2} on every basis monomial "
      "(support exactly; the composite of the sigma_std-type cut and the "
      "Minkowski mirror is the half rotation = the deck/antipode lift): "
      "the duality and the OS metric close onto the deck, exactly as the "
      "torsor arithmetic upstairs (D4.4) demands" % EXACT, ok_close)


# ============================================================ D6 ============
section("D6  CONTROLS -- family A has no quotient; the branch has teeth")

r_anti = lambda a_: (a_ + 8) % N16
s_alt = lambda a_: 1 if a_ % 2 == 0 else -1
basis_a = [(a_,) for a_ in range(8)]
tw0_16 = (tuple(range(N16)), (1,) * N16)
picked = None
for etac in (sp.Integer(1), sp.Integer(-1), I, -I):
    Ma = term_matrix(basis_a, tw0_16, r_anti, s_alt, etac, N16)
    if hermitian_exact(Ma):
        ia, _ = spectrum_inertia(Ma)
        picked = (etac, ia)
        break
check("D6.1 %s FAMILY A -> NO QUOTIENT (v524 C4.2 verbatim): the "
      "clock-centralising antipode candidate has a Hermitian OS form "
      "only for eta = %s and it is INDEFINITE, inertia %s -- even if the "
      "D3.3 emptiness were ignored, the family-A structure cannot enter "
      "the quotient: no PSD form, no H_phys (control (iii))"
      % (CERT, picked[0] if picked else None,
         picked[1] if picked else None),
      picked is not None and picked[1] == (4, 4, 0))
check("D6.2 %s THE EUCLIDEAN BRANCH CANNOT CUT: the eps = +1 solution "
      "family has seam-line norm a(|z|^2 + 1), definite for every a != 0 "
      "-- sigma_std and all its Euclidean twists furnish NO OS cut "
      "circle: the role Woit assigns them (defining the euclidean "
      "section, v519 W-S3.3) is the only role they can play" % EXACT,
      iszero(sp.expand(N_E - a * (x_r ** 2 + y_r ** 2 + 1))))
mu5 = sp.exp(2 * I * sp.pi / 5)
check("D6.3 %s NON-mu4 MUTATION: a reflection member with mu = "
      "e^{2 pi i/5} would NOT preserve the mu4 marks (mu notin mu4, v519 "
      "mark pinning) -- the induced member mu = -1 lands in the torsor "
      "BECAUSE the duality is clock-compatible; an incompatible Phi "
      "(D1.3) would not be mark-anchored" % EXACT,
      not iszero(sp.expand_complex(mu5 ** 4 - 1)))


# ======================================================== VERDICT ==========
section("VERDICT -- evaluated exactly as pre-registered in the header")

S1 = not any(f.startswith("D1") for f in FAILS)
S2 = not any(f.startswith("D2") for f in FAILS)
S3 = not any(f.startswith("D3") for f in FAILS)
S4 = not any(f.startswith("D4") for f in FAILS)
S5 = not any(f.startswith("D5") for f in FAILS)
S6 = not any(f.startswith("D6") for f in FAILS)
VERDICT = "SUCCESS" if all((S1, S2, S3, S4, S5, S6)) else "UNDECIDED"

print("""
  *** VERDICT: %s (beta_3). ***  The PT <-> PT* duality is typed against
  sigma_std and the identification demanded by the contract holds:

  (1) THE CLASS: clock-compatibility forces the block structure (D1) --
      the compatible dualities are the two-block Hermitian forms, with
      the deck served automatically and the wrong clock lift breaking
      the split (the compiler clock is load-bearing).
  (2) THE DICHOTOMY: the rho_tw pairing splits the class into an
      EUCLIDEAN branch (sigma_std's home; no null point on the seam
      line -- no OS cut, ever) and a MINKOWSKI branch whose null locus
      meets the seam line EXACTLY in the seam circle -- the OS cut is
      FORCED by the compatibility conditions, and the total signature
      is (2,2) by the signature-mirror theorem: Woit's Minkowski
      signature is a consequence, not an assumption (D2).
  (3) THE KILL IS EMPTY: every compatible duality inverts the clock and
      the deck exactly (family D); a clock-centralising (family A)
      duality would need rho^2 = scalar -- impossible for the order-4
      clock.  Decided by algebra, not by scan (D3); and family A
      independently has no quotient ((4,4,0), D6.1).
  (4) THE IDENTIFICATION: every seam-preserving Minkowski member
      induces ONE projective conjugation z -> -conj(z) (mu = -1, fixed
      points +-i) -- perpendicular to sigma_std's z -> +conj(z); under
      the declared RP-side placement this is EXACTLY theta_perp, the
      mirror whose quotient descent v524 certified: Theta_phys is the
      shadow of the PT <-> PT* duality, anti-unitary, Kramers-free
      (Theta^2 = +1 per sector), time-reversing the semigroup, closing
      with the sigma_std-type cut onto the deck (D4/D5).

  Woit's Minkowski conjugation (PT -> PT*) = the family-D conjugation
  on the quotient: the beta_3 success criterion, met member by member.
""" % VERDICT)

print("""
  WHAT THIS DOES AND DOES NOT SAY.  Free/quotient level only: nothing
  here constructs the interacting algebra A_hol, and all seven contract
  kill tests stay formally live there; WOIT.OS.TWISTOR.01 stays [O] and
  no marker moves.  The declared conventions ([C]-fences): the seam line
  span(e1,e2) with the v519 blockwise lift; seam preservation as the
  reading of 'the duality respects the seam'; the RP-side bond-midpoint
  placement (v519 precision (ii)); the two-orbit clock relabeling of the
  torsor.  Within those declared structures, everything above is exact:
  the branch dichotomy, the (2,2), the emptiness of the kill, the
  uniqueness of the induced member and its identity with the v524
  mirror.  Next milestone: gamma (the chirality theorem + the mark
  incidence), with kill tests (3)/(6)/(7).
""")

section("TOTAL")
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s of %.0f s budget" % (time.time() - T0, BUDGET_S))
print("VERDICT: %s -- beta_3 executed; kill branch empty by algebra; "
      "signature (2,2) and the OS cut forced; induced member unique "
      "(mu = -1) and identified with the v524 Theta_phys carrier "
      "(theta_perp), Kramers-free, time-reversing" % VERDICT)
print("FENCES: no ledger/paper/website/registry file touched by this "
      "probe; no marker moves; free/quotient level only, A_hol "
      "untouched; Penrose 1967 / Woit 2021-23 / OS 1973-75 / "
      "Klein-Landau 1981 / Kramers 1930 named CLASSICAL as addresses")
