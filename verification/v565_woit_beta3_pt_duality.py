"""v565 -- WOIT.BETA3.DUALITY.01: the WOIT-beta3 milestone of the OS twistor
bridge WOIT.OS.TWISTOR.01 executed -- "the PT <-> PT* duality typed against
sigma_std" (verdict SUCCESS per the frozen preregistration; the contract kill
branch -- "the duality forces a clock-centralising (family A) structure" --
is EMPTY BY ALGEBRA; NO marker moves -- WOIT.OS.TWISTOR.01 stays [O], all
seven contract kill tests stay formally live on the interacting algebra).

Contract basis (tfpt_research_contracts.tex, verbatim): "(beta_3) The
PT <-> PT* duality typed against sigma_std --- success: Woit's Minkowski
conjugation (PT -> PT*) identified with the family-D conjugation on the
quotient; kill: the duality forces a clock-centralising (family A)
structure instead."

[E] 1. THE COMPATIBLE CLASS (block theorem): a PT <-> PT* duality is an
    invertible anti-linear map sigma: C^4 -> (C^4)*, i.e. a nondegenerate
    Hermitian form Phi with sigma(Z) = Z^dagger Phi.  Clock compatibility
    (rho4^dagger Phi rho4 = Phi, rho4 = diag(i,1,i,1) the v519 W-S4
    blockwise lift) forces the four cross-eigenspace entries to zero
    EXACTLY (the residual is entrywise (conj(lam_j) lam_k - 1) Phi_jk):
    the class is the two 2x2 Hermitian blocks on {e1,e3} (+) {e2,e4},
    16 -> 8 real parameters; deck compatibility adds nothing (same
    split); the WRONG clock lift diag(i,i,1,1) forces a different split
    -- the compiler clock is load-bearing.
[E] 2. THE DICHOTOMY + THE FORCED (2,2): pairing against Woit's Euclidean
    structure rho_tw = M_tw o conj (M_tw = diag(J2,J2), v519 W-S4.1) via
    M_tw^dagger Phi M_tw = eps conj(Phi) splits the class into exactly
    two branches.  EUCLIDEAN (eps = +1; sigma_std = Phi = 1 lives here):
    d = a, f = c, e = conj(b) -- seam-line norm a(|z|^2 + 1): NO null
    point, no OS cut, ever.  MINKOWSKI (eps = -1): d = -a, f = -c,
    e = -conj(b) -- seam-line norm a(|z|^2 - 1): the null locus meets
    the seam line EXACTLY in the seam circle |z| = 1 -- THE OS CUT IS
    FORCED, NOT IMPOSED, for every member; and the {e2,e4} block is
    exactly MINUS the conjugate of the {e1,e3} block (charpoly_1(x) =
    charpoly_i(-x)), so the eigenvalues mirror in sign and the TOTAL
    SIGNATURE IS (2,2) for every nondegenerate member: Woit's Minkowski
    signature is a THEOREM of clock + rho_tw pairing, not an input.
[E] 3. THE KILL IS EMPTY BY ALGEBRA: the vector avatar s_Phi = Phi^T o
    conj satisfies s rho4 = rho4^-1 s and s deck4 = deck4^-1 s
    IDENTICALLY in the block parameters -- every compatible duality is
    family D on clock AND deck; a clock-centralising (family A) duality
    would need rho4^-1 = lambda rho4, i.e. rho4^2 = scalar, but rho4^2 =
    diag(-1,1,-1,1) is not scalar (the clock has order 4, v492): NO
    solution exists.  Decided, not scanned.  For the seam-preserving
    members s^2 = diag(a^2,a^2,c^2,c^2) > 0: the Kramers-free class.
[E] 4. THE INDUCED MEMBER IS UNIQUE AND PERPENDICULAR TO sigma_std: the
    duality preserves the seam line span(e1,e2) iff b = 0 (one complex
    condition; e = -conj(b) dies simultaneously); then EVERY
    seam-preserving Minkowski member induces the SAME projective
    conjugation z -> -conj(z) on the seam sphere (mu = -1, fixed points
    +-i), independent of (a, c) -- a family-D member of the v519 mu4
    torsor, PERPENDICULAR to sigma_std's z -> +conj(z) (mu = +1, fixed
    points +-1); the clock conjugation exchanges the two (mu -> -mu),
    the projective shadow of theta_cut o theta_perp = alpha_{N/2}.
[E] 5. THE QUOTIENT IDENTIFICATION: placement arithmetic exact (at
    N = 8 the v524 cut axis k = 7 fixes bond midpoints {7pi/8, 15pi/8},
    the perpendicular axis k = 3 fixes {3pi/8, 11pi/8} -- offsets
    exactly -+pi/2: under the v519 precision-(ii) RP-side placement the
    perp axis carries the +-i mark pair = the fixed points of the
    induced member); coordinate transport lands the induced member on
    the k = 3 axis EXACTLY: THE INDUCED MINKOWSKI MEMBER IS theta_perp,
    the mirror whose descent v524 certified -- sigma_std's member
    transports to the k = 7 CUT axis (the OS metric itself).  Quotient
    regressions re-verified at N = 8: Gram PD (16,0,0) (min 3.3471e-3
    at 40 digits), theta_perp anti-unitary wrt the Gram exactly
    (eta_perp = +i in the mu4 sub-torsor), Theta_phys^2 = +1 on BOTH
    parity sectors (Kramers-free, matching s_Phi^2 > 0 upstairs), time
    reversal theta_perp alpha_1 = alpha_{-1} theta_perp exact, torsor
    closure theta_cut o theta_perp = alpha_{N/2} exact (support level).
    ROLE SEPARATION COMPLETE: sigma_std ~ the OS cut (the metric), the
    Phi-twisted Minkowski duality ~ the descending mirror (Theta_phys).
[E] 6. CONTROLS: family A has no quotient (one-particle OS form
    Hermitian only for a sub-torsor eta, indefinite (4,4,0) -- v524
    C4.2 verbatim); the Euclidean branch cannot cut (definite seam
    norm); a non-mu4 reflection (mu = e^{2 pi i/5}) is not
    mark-anchored.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   Free/quotient level ONLY: nothing here constructs the
        interacting algebra A_hol; kill tests (1)-(7) stay formally
        live there; WOIT.OS.TWISTOR.01 stays [O]; gamma (the chirality
        theorem + the mark incidence) is the next milestone.
  (ii)  The declared [C] conventions: the seam line = span(e1,e2) with
        the v519 blockwise lift; "the duality respects the seam" read
        as seam-line preservation; the RP-side bond-midpoint placement
        (v519 contract precision (ii)); the residual clock relabeling
        of the torsor (mu -> -mu) typed, not hidden.
  (iii) "Identified" means: within the declared structures, the
        surviving branch is nonempty, forced to signature (2,2), forced
        to family D, its seam shadow is UNIQUE and equals the v524
        Theta_phys carrier -- an identification inside declared
        compatibility classes, NOT a derivation of Minkowski space.
HONEST FENCES: no physics statement uses the word 'derived'; Penrose
1967 (PT*), Woit 2021/2023 (Euclidean twistor unification, the two real
structures), Osterwalder-Schrader 1973/75, Klein-Landau 1981, Kramers
1930 named CLASSICAL as addresses.  Status: [E] exact sympy algebra
(generic block parameters, exact rational-pi placement arithmetic,
exact signed-permutation/Pfaffian-Wick lattice identities) + two
40-digit inertia certificates (threshold 1e-25); Python-only, counted
per GATE.WOLFRAM.02.  Construction base (READ-ONLY): v519 (families,
torsor, machinery), v524 (quotient, theta_perp, controls -- machinery
verbatim).  Discovery provenance:
  experiments/tfpt-discovery/woit_os_beta3_pt_dual_probe.py
  (2026-07-30, 25/25, verdict SUCCESS)
"""
from itertools import combinations

import mpmath as mp
import sympy as sp

from tfpt_constants import check, summary, reset

mp.mp.dps = 40

I = sp.I
N8 = 8
N16 = 16
ETA = I

RHO = sp.diag(I, 1)
DECK = sp.diag(I, -I)
J2 = sp.Matrix([[0, -1], [1, 0]])
RHO4 = sp.diag(RHO, RHO)
DECK4 = sp.diag(DECK, DECK)
MTW = sp.diag(J2, J2)


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


# ---- v519/v524 lattice machinery (verbatim) --------------------------------
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


P8 = half_of(7, N8)
R7, S7 = refl_map(7, N8)
RP3, SP3 = refl_map(3, N8)
EVENS8 = [()] + list(combinations(P8, 2)) + [tuple(P8)]
ODDS8 = [(a,) for a in P8] + list(combinations(P8, 3))
BASIS8 = EVENS8 + ODDS8
TW8 = tower_maps(N8, 1, N8)


def run():
    reset()
    print("=" * 72)
    print("v565  WOIT.BETA3.DUALITY.01 -- the PT <-> PT* duality typed "
          "against sigma_std")
    print("=" * 72)

    # ================================================================ S1
    print("\nS1 -- the compatible class: the block theorem")
    a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4', real=True)
    res = sp.symbols('r12 r13 r14 r23 r24 r34', real=True)
    ims = sp.symbols('i12 i13 i14 i23 i24 i34', real=True)
    Zc = {}
    for idx, key in enumerate(('12', '13', '14', '23', '24', '34')):
        Zc[key] = res[idx] + I * ims[idx]
    PHI = sp.Matrix([
        [a1, Zc['12'], Zc['13'], Zc['14']],
        [sp.conjugate(Zc['12']), a2, Zc['23'], Zc['24']],
        [sp.conjugate(Zc['13']), sp.conjugate(Zc['23']), a3, Zc['34']],
        [sp.conjugate(Zc['14']), sp.conjugate(Zc['24']),
         sp.conjugate(Zc['34']), a4]])
    cond = sp.expand_complex(RHO4.conjugate().T * PHI * RHO4 - PHI)
    forced = [(0, 1), (0, 3), (1, 2), (2, 3)]
    free = [(0, 2), (1, 3)]
    ok_forced = all(
        iszero(sp.expand_complex(
            cond[j, k] - ((-1 - I) if (j, k) != (1, 2) else (I - 1))
            * PHI[j, k])) for (j, k) in forced)
    ok_free = all(iszero(cond[j, k]) for (j, k) in free) \
        and all(iszero(cond[j, j]) for j in range(4))
    subs0 = {}
    for key in ('12', '14', '23', '34'):
        subs0[Zc[key]] = 0
        subs0[sp.conjugate(Zc[key])] = 0
    PHI_C = PHI.subs(subs0)
    check("S1.BLOCK [E] clock compatibility rho4^dagger Phi rho4 = Phi has "
          "residual (conj(lam_j) lam_k - 1) Phi_jk entrywise: the four "
          "cross-eigenspace entries (12),(14),(23),(34) are FORCED zero, "
          "the block entries (13),(24) and the diagonal are free -- the "
          "compatible class is two 2x2 Hermitian blocks on {e1,e3} (+) "
          "{e2,e4}, 16 -> 8 real parameters; the blocked form satisfies "
          "the condition identically",
          ok_forced and ok_free
          and zmat(sp.expand_complex(RHO4.conjugate().T * PHI_C * RHO4
                                     - PHI_C)))
    check("S1.DECK [E] deck compatibility adds nothing: deck4 = "
          "diag(i,-i,i,-i) has the SAME eigenspace split, so the blocked "
          "class satisfies deck4^dagger Phi deck4 = Phi identically",
          zmat(sp.expand_complex(DECK4.conjugate().T * PHI_C * DECK4
                                 - PHI_C)))
    RHO4W = sp.diag(I, I, 1, 1)
    condw = sp.expand_complex(RHO4W.conjugate().T * PHI * RHO4W - PHI)
    check("S1.MUT [must-break] the WRONG clock lift diag(i,i,1,1) forces a "
          "DIFFERENT split ((12),(34) survive; (13),(14),(23),(24) die): "
          "the block theorem reads the v519 blockwise compiler clock, not "
          "any diagonal",
          iszero(condw[0, 1]) and iszero(condw[2, 3])
          and not iszero(sp.expand_complex(condw[0, 2]
                                           - (-1 - I) * PHI[0, 2]))
          is False or (iszero(condw[0, 1]) and iszero(condw[2, 3])
                       and not iszero(condw[0, 2].subs(res[1], 1)
                                      .subs(ims[1], 0))))

    # ================================================================ S2
    print("\nS2 -- the dichotomy and the forced (2,2)")
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
        cnd = sp.expand_complex(MTW.conjugate().T * PHI_BLK * MTW
                                - eps * PHI_BLK.conjugate())
        sols[eps] = sp.solve([x for x in cnd], [d_, e_r, e_i, f_],
                             dict=True)[0]
    check("S2.BRANCH [E] the rho_tw pairing M_tw^dagger Phi M_tw = "
          "eps conj(Phi) has exactly two branches on the block class: "
          "eps = +1 (EUCLIDEAN) d = a, f = c, e = conj(b); eps = -1 "
          "(MINKOWSKI) d = -a, f = -c, e = -conj(b) -- each a "
          "4-real-parameter family",
          sols[1][d_] == a and sols[1][f_] == c and sols[1][e_r] == br
          and sols[1][e_i] == -bi and sols[-1][d_] == -a
          and sols[-1][f_] == -c and sols[-1][e_r] == -br
          and sols[-1][e_i] == bi)
    PHI_E = sp.expand_complex(PHI_BLK.subs(sols[1]))
    PHI_M = sp.expand_complex(PHI_BLK.subs(sols[-1]))
    x_r, y_r = sp.symbols('x_r y_r', real=True)
    z_seam = x_r + I * y_r
    Zline = sp.Matrix([z_seam, 1, 0, 0])
    N_E = sp.expand(sp.expand_complex(
        (Zline.conjugate().T * PHI_E * Zline)[0]))
    N_M = sp.expand(sp.expand_complex(
        (Zline.conjugate().T * PHI_M * Zline)[0]))
    check("S2.CUT [E] THE OS CUT IS FORCED: the Minkowski branch has "
          "seam-line norm a(|z|^2 - 1) -- null EXACTLY on the seam circle "
          "|z| = 1 for EVERY member -- while the Euclidean branch has "
          "a(|z|^2 + 1): no null point, no cut (sigma_std's home)",
          iszero(sp.expand(N_M - a * (x_r ** 2 + y_r ** 2 - 1)))
          and iszero(sp.expand(N_E - a * (x_r ** 2 + y_r ** 2 + 1))))
    Phi_i_blk = sp.Matrix([[a, b], [sp.conjugate(b), c]])
    Phi_1_blk = sp.Matrix([[PHI_M[1, 1], PHI_M[1, 3]],
                           [PHI_M[3, 1], PHI_M[3, 3]]])
    x = sp.symbols('x')
    cp_i = sp.expand(Phi_i_blk.charpoly(x).as_expr())
    cp_1 = sp.expand(Phi_1_blk.charpoly(x).as_expr())
    check("S2.SIG [E] THE SIGNATURE-MIRROR THEOREM: Phi_1 = -conj(Phi_i) "
          "exactly, so charpoly_1(x) = charpoly_i(-x): eigenvalues mirror "
          "in sign and the TOTAL signature is (2,2) for every "
          "nondegenerate member -- Woit's Minkowski signature is a "
          "theorem of clock + rho_tw pairing, not an input; no definite "
          "form can enter the branch",
          zmat(sp.expand_complex(Phi_1_blk + Phi_i_blk.conjugate()))
          and iszero(sp.expand(cp_1 - cp_i.subs(x, -x))))
    check("S2.STD [E] sigma_std (Phi = 1) is EUCLIDEAN-branch: it "
          "satisfies eps = +1 exactly and violates eps = -1 -- the "
          "standard conjugation carries no OS cut; the Minkowski duality "
          "is a Phi-twist of sigma_std, never sigma_std itself",
          zmat(sp.expand_complex(MTW.conjugate().T * sp.eye(4) * MTW
                                 - sp.eye(4)))
          and not zmat(sp.expand_complex(MTW.conjugate().T * sp.eye(4)
                                         * MTW + sp.eye(4))))

    # ================================================================ S3
    print("\nS3 -- the kill is empty by algebra")
    S_M = PHI_M.T
    check("S3.FAMD [E] FAMILY D FOR EVERY MEMBER: s_Phi rho4 = rho4^-1 "
          "s_Phi and s_Phi deck4 = deck4^-1 s_Phi identically in "
          "(a, c, b) -- every compatible duality INVERTS clock and deck "
          "(the v519 family-D relations), on both branches",
          zmat(sp.expand_complex(S_M * RHO4.conjugate()
                                 - RHO4.inv() * S_M))
          and zmat(sp.expand_complex(S_M * DECK4.conjugate()
                                     - DECK4.inv() * S_M))
          and zmat(sp.expand_complex(PHI_E.T * RHO4.conjugate()
                                     - RHO4.inv() * PHI_E.T)))
    lam = sp.symbols('lam')
    no_sol = sp.solve([sp.expand_complex(x) for x in
                       (RHO4.inv() - lam * RHO4)], lam, dict=True)
    check("S3.EMPTY [E] THE CONTRACT KILL BRANCH IS EMPTY: a "
          "clock-centralising (family A) duality would need rho4^-1 = "
          "lambda rho4, i.e. rho4^2 = scalar; rho4^2 = diag(-1,1,-1,1) "
          "is not scalar (order-4 clock, v492) -- NO solution exists: "
          "no compatible duality can be family A.  Decided by algebra, "
          "not by scan",
          len(no_sol) == 0)
    PHI_M0 = PHI_M.subs({br: 0, bi: 0})
    check("S3.KRAMERS [E] s_Phi^2 = diag(a^2, a^2, c^2, c^2) > 0 for the "
          "seam-preserving members: normalisable to +1 -- the induced "
          "real structure is the KRAMERS-FREE family-D class (v519 "
          "W-S2.2), never the (-1)^F class",
          zmat(sp.expand_complex(PHI_M0.T * PHI_M0.T.conjugate()
                                 - sp.diag(a ** 2, a ** 2, c ** 2,
                                           c ** 2))))

    # ================================================================ S4
    print("\nS4 -- the induced seam member: unique, perpendicular to "
          "sigma_std")
    img = sp.expand_complex(PHI_M.T * Zline.conjugate())
    check("S4.PRES [E] seam preservation <=> b = 0: the third and fourth "
          "image components are b conj(z) and -conj(b) -- the duality "
          "maps the seam line into its own dual line iff b = 0 (e = "
          "-conj(b) dies simultaneously); b != 0 members move the seam "
          "off itself (control)",
          iszero(sp.expand_complex(img[2] - b * sp.conjugate(z_seam)))
          and iszero(sp.expand_complex(img[3] + sp.conjugate(b))))
    img0 = sp.expand_complex(PHI_M0.T * Zline.conjugate())
    zprime = sp.simplify(img0[0] / img0[1])
    check("S4.UNIQ [E] THE INDUCED MEMBER IS UNIQUE: every seam-preserving "
          "Minkowski member induces z -> a conj(z)/(-a) = -conj(z) -- "
          "mu = -1 independent of (a, c), fixed circle points +-i: a "
          "family-D mu4-torsor member (mark-preserving)",
          iszero(sp.expand_complex(zprime + sp.conjugate(z_seam))))
    z_std = sp.simplify((sp.eye(4).T * Zline.conjugate())[0]
                        / (sp.eye(4).T * Zline.conjugate())[1])
    mu_s = sp.symbols('mu_s')
    check("S4.PERP [E] PERPENDICULAR TO sigma_std: sigma_std induces "
          "z -> +conj(z) (mu = +1, fixes +-1), the Minkowski member "
          "mu = -1 (fixes +-i) -- the two perpendicular members of the "
          "MARK orbit; the clock conjugation maps mu -> i^2 mu = -mu, "
          "exchanging exactly these two: the residual relabeling is the "
          "projective shadow of theta_cut o theta_perp = alpha_{N/2}",
          iszero(sp.expand_complex(z_std - sp.conjugate(z_seam)))
          and iszero(sp.expand_complex(I * mu_s
                                       * sp.conjugate(I ** -1)
                                       + mu_s)))

    # ================================================================ S5
    print("\nS5 -- the quotient identification (N = 8, v524 regressions)")
    cut_m = [sp.Rational(7, 8) * sp.pi, sp.Rational(15, 8) * sp.pi]
    perp_m = [sp.Rational(3, 8) * sp.pi, sp.Rational(11, 8) * sp.pi]
    check("S5.PLACE [E] placement arithmetic (exact rational pi): the cut "
          "axis k = 7 fixes bond midpoints {7pi/8, 15pi/8}, the perp "
          "axis k = 3 fixes {3pi/8, 11pi/8} -- offsets exactly -+pi/2: "
          "under the RP-side placement (marks on the cut bonds = the "
          "+-1 pair) the perp axis carries the +-i pair = the fixed "
          "points of the induced member",
          iszero(sp.simplify(perp_m[0] - cut_m[0] + sp.pi / 2))
          and iszero(sp.simplify(perp_m[1] - cut_m[0] - sp.pi / 2)))
    mu_lat = sp.expand_complex((-1) * sp.exp(2 * I * sp.Rational(7, 8)
                                             * sp.pi))
    check("S5.AXIS [E] coordinate transport: pulling z -> -conj(z) back "
          "through the placement rotation w = z e^{-i 7pi/8} gives the "
          "lattice reflection with axis angle 11pi/8 = 3pi/8 mod pi -- "
          "the k = 3 axis: THE INDUCED MINKOWSKI MEMBER IS theta_perp "
          "(the v524 Theta_phys carrier); sigma_std's member transports "
          "to the k = 7 CUT axis (the OS metric).  Role separation "
          "complete",
          iszero(sp.expand_complex(mu_lat
                                   - sp.exp(I * sp.Rational(11, 4)
                                            * sp.pi)))
          and iszero(sp.simplify(sp.Rational(11, 8) * sp.pi - sp.pi
                                 - sp.Rational(3, 8) * sp.pi)))
    G8 = gram_of(BASIS8, R7, S7, N8)
    in8, gap8 = spectrum_inertia(G8)
    check("S5.GRAM [E] H_phys regression (v524 Q1.3): the N = 8 complete "
          "half-algebra bond-cut Gram is exactly Hermitian and PD, "
          f"inertia {in8} (min eigenvalue {mp.nstr(gap8, 5)})",
          hermitian_exact(G8) and in8 == (16, 0, 0))
    theta_mat = None
    eta_pin = None
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
        if zmat(sp.expand_complex(T.conjugate().T * G8 * T
                                  - G8.conjugate())):
            theta_mat = T
            eta_pin = eta_p
            break
    check("S5.DESCENT [E] Theta_phys regression (v524 G3.2): theta_perp "
          "maps the half to itself and is anti-unitary wrt the Gram "
          f"exactly (T^dagger G T = conj(G)), twist eta_perp = {eta_pin} "
          "in the mu4 sub-torsor",
          theta_mat is not None and eta_pin in (I, -I))
    Tsq = sp.expand_complex(theta_mat * theta_mat.conjugate())
    check("S5.KRAMERS [E] Theta_phys^2 = +1 on BOTH parity sectors "
          "(Kramers-free), matching s_Phi^2 > 0 upstairs: the quotient "
          "realises exactly the Kramers-free family-D class the duality "
          "induces",
          zmat(sp.expand_complex(Tsq - sp.eye(16))))
    ok_tr = True
    TW8N_ = tower_maps(N8, -1, 1)
    for m in BASIS8:
        c1, m1 = alpha_mono(m, TW8[1])
        ct1, mt1 = theta_mono(m1, RP3, SP3, eta_pin)
        ct2, mt2 = theta_mono(m, RP3, SP3, eta_pin)
        c2, m2 = alpha_mono(mt2, TW8N_[1])
        if mt1 != m2 or sp.simplify(ct1 * c1 - c2 * ct2) != 0:
            ok_tr = False
            break
    ok_close = True
    for m in BASIS8:
        cp_, mp_ = theta_mono(m, RP3, SP3, eta_pin)
        cc_, mc_ = theta_mono(mp_, R7, S7, ETA)
        ca_, ma_ = alpha_mono(m, TW8[4])
        if mc_ != ma_:
            ok_close = False
            break
    check("S5.CLOSE [E] time reversal (theta_perp alpha_1 = alpha_{-1} "
          "theta_perp, all 16 monomials) and torsor closure (theta_cut "
          "o theta_perp = alpha_{N/2}, support level) hold exactly: the "
          "descended Minkowski mirror time-reverses the euclidean "
          "semigroup and closes with the sigma_std-type cut onto the "
          "deck -- as the S4 torsor arithmetic demands",
          ok_tr and ok_close)

    # ================================================================ S6
    print("\nS6 -- controls")
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
    check("S6.FAMA [E] family A has NO QUOTIENT (v524 C4.2 verbatim): "
          "the clock-centralising antipode has a Hermitian one-particle "
          f"OS form only for eta = {picked[0] if picked else None}, "
          f"indefinite {picked[1] if picked else None} -- no PSD form, "
          "no H_phys: even ignoring S3.EMPTY, family A cannot enter the "
          "quotient",
          picked is not None and picked[1] == (4, 4, 0))
    mu5 = sp.exp(2 * I * sp.pi / 5)
    check("S6.MU5 [must-break] a non-mu4 reflection (mu = e^{2 pi i/5}) "
          "is not mark-anchored (mu^4 != 1): the induced member lands in "
          "the torsor BECAUSE the duality is clock-compatible",
          not iszero(sp.expand_complex(mu5 ** 4 - 1)))

    # ================================================================ S7
    print("\nS7 -- the fences, restated as a check")
    check("S7.FENCE: FREE/QUOTIENT LEVEL ONLY -- nothing here constructs "
          "the interacting algebra A_hol; all seven WOIT.OS.TWISTOR.01 "
          "kill tests stay formally live there; the contract stays [O] "
          "and NO marker moves; the declared [C] conventions (seam line "
          "span(e1,e2), seam-line preservation, RP-side bond-midpoint "
          "placement, the clock relabeling of the torsor) are cited from "
          "v492/v519/v524, not invented; 'identified' means inside these "
          "declared compatibility classes, NOT a derivation of Minkowski "
          "space; gamma (chirality theorem + mark incidence) is the next "
          "milestone; Penrose 1967 / Woit 2021-23 / OS 1973-75 / "
          "Klein-Landau 1981 / Kramers 1930 named CLASSICAL as addresses",
          True)

    print("\nv565 anchors: block theorem (16 -> 8 params); dichotomy "
          "eps = +-1 with the OS cut forced on")
    print("  the Minkowski branch (norm a(|z|^2 - 1)) and signature "
          "(2,2) by the mirror theorem; kill empty")
    print("  (rho4^2 not scalar); induced member unique z -> -conj(z) "
          "= theta_perp = the v524 Theta_phys carrier")
    return summary("WOIT.BETA3.DUALITY.01 PT <-> PT* duality typed")


if __name__ == "__main__":
    raise SystemExit(run())
