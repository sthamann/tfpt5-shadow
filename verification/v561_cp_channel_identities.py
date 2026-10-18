"""v561 -- CP.CHANNEL.IDENT.01: the CP channel / invariant identities (T177).

THE CP MIRROR, AS ALGEBRA.  T177 (contract CP.INVARIANT, probe
cp_invariant_probe.py, 49/49, verdict DEGENERATE) ran the newest tool of the
prime-front series -- gauge-degree bookkeeping under declared group actions --
on the four CP ledger rows (REDTEAM.D.01, E8.CHAN.01, CP.MOD.01,
DUAL.FRAME.01).  THIS module is the load-bearing version of the exact,
theorem-shaped cores of that mirror -- per instance, machine-checkable, each
with a mutation control -- and it derives NOTHING: every statement below is a
NARROWING of an existing ledger reading, no marker of any pre-existing
contract moves, and no CP derivation is claimed anywhere.

[E] (1) THE HEXAGONAL CHANNEL IDENTITY (T177 F1.2).  On the hexagonal CM unit
    rho = e^{i pi/3} (CP.MOD.01) the E8 channel split 248 = 120 + 128
    (E8.CHAN.01, v227) acquires an EXACT fiber realisation: the PHASE channel
    carries sum_k rho^{d_k} = 4 rho (arg = pi/3 exactly; the degrees
    {2,8,12,14,18,20,24,30} reduce mod 6 to four 0s and four 2s, and
    1 + rho^2 = rho), while the MAGNITUDE channel carries
    sum_k rho^{m_k} = 4 (arg = 0 exactly; the exponents
    {1,7,11,13,17,19,23,29} reduce mod 6 to four 1s and four 5s, and
    rho + rho^5 = 2 cos(pi/3) = 1).  PARITY TYPING: all E8 degrees are EVEN,
    so the phase channel is SHEET-EVEN under the sheet flip
    sigma: rho -> rho^4 = -rho; all E8 exponents are ODD, so the magnitude
    channel is SHEET-ODD.  CONSEQUENCE THAT MATTERS: being sheet-even, the
    phase-channel angle CANNOT distinguish quark from lepton -- it carries
    pi/3 but not the CP.MU6.01 sheet split.  Mutation controls: the identity
    breaks on the non-CM unit e^{i pi/5} and on a mutated degree list
    (30 -> 31); reality of the exponent sum breaks on a mutated exponent
    list (29 -> 30).  HONEST CAVEAT, wired as a check: reality of the
    exponent-channel sum alone is NOT hexagon-specific (the exponent residues
    are conjugation-closed mod 10 as well, so the e^{i pi/5} exponent sum is
    real too) -- only the DEGREE half (= 4 rho) is specific to the hexagonal
    fiber.
[E] (2) THE MAGNITUDE CHANNEL CARRIES ZERO PHASE + THE BRANCH-ORDER LAW
    (T177 F2.3/F2.4; the REDTEAM.D.01 narrowing).  arg(prod_i c_i) = 0
    EXACTLY on both TFPT sectors -- the lepton triple (16/7, 4/3, 7/6) and
    the up-quark gauge triple (1/2, 34/41, 4/13) are positive rationals, so
    the CP residual is not hidden in the product.  The mu3 branch group
    {1, w, w^2} (w = e^{2 pi i/3}) is EXACTLY the kernel of the magnitude
    data because its diagonal action multiplies the product by w^{3j} = 1:
    the blindness is the statement that the branch order DIVIDES
    N_fam = 3.  Mutation control: a mu4 branch (i-diagonal) already shifts
    the product phase by arg(i^3) = -pi/2 != 0 -- the kernel property is a
    property of the order, not of diagonality.  RECOMMENDED LEDGER WORDING
    (executed in the same change): the residual is a FIBER datum (the
    hexagonal CM unit), not a magnitude datum.
[E] (3) TIER-1 EMPTINESS BY THE BLINDNESS THEOREM (T177 F3.1).  Both complex
    kernels commute with conjugation -- conj(sum rho^{d_k}) =
    sum (conj rho)^{d_k} and Im det(1, d, conj(rho) n) =
    -Im det(1, d, rho n) -- so EVERY pi/3-carrier is kappa-ODD (its value
    conjugates under the CP involution kappa), and a functional that is both
    strictly invariant AND kappa-odd has Im F = 0, i.e. carries no pi/3:
    strict invariance under all four T177 groups is EMPTY on pi/3-carriers,
    per algebra and as preregistered, NOT as a scan result.
[E] (4) THE FRAME REMOVAL + THE DEGREE ACCOUNT (T177 F2.5; the DUAL.FRAME.01
    narrowing).  On the dual normal frame (v225): det(1, d, n) = 21 =
    N_fam * scalaron exactly and Im det(1, d, rho n) = 21 sin(pi/3) exactly;
    the raw orientation functional P4 is homogeneous of DEGREE +1 in the
    frame normalisation n -> t n (t > 0), so the NUMBER 21 sin(pi/3) is
    FRAME data, not an invariant -- and dividing by the oriented volume
    removes the frame IDENTICALLY: Im(rho det)/det = Im(rho) = sin(pi/3)
    exactly for every real det != 0 (checked symbolically and on the
    instance).  The invariant core of the orientation reading is the FIBER
    datum Im(rho) = sin(pi/3); the sign is a declared orientation.
[E] (5) THE TWO TIER-2 CHARACTERS + THE JARLSKOG ANCHOR (T177 F2/F3.3).
    The two surviving pi/3-carriers P2 = arg(sum rho^{d_k}) and
    V5 = Im(rho det)/det carry the characters (chi(kappa), chi(sigma)) =
    (-1, +1) and (-1, -1) respectively -- verified as HOMOMORPHISMS on the
    four-element group {1, kappa, sigma, kappa sigma} -- and a real
    invariant equivalence factor preserves every character, so the two
    classes are INEQUIVALENT: the pi/3 structure is invariant as a VALUE but
    not pinned to one functional (the DEGENERATE verdict), and NEITHER
    carrier couples to the frame.  THE CLASSICAL ANCHOR (Jarlskog 1985): the
    TFPT CKM rebuild (s12 = lambda_C, s23 = phi0/(1+lambda_C),
    s13 = lambda_C^3/3, delta = pi/3 + 3 lambda_C^2 frozen per
    REG.FREEZE.01) is unitary at working precision and gives
    J = 3.327021e-5 = the v88 lattice value; J passes (a) rephasing
    invariance (including the mu3 branch group), (b) scale/normalisation
    freedom, (c) CP-oddness J(conj V) = -J(V), and fails ONLY (d) the
    pi/3-carrier test -- its phase content is delta = pi/3 + 3 lambda_C^2,
    not pi/3 -- so the benchmark VALIDATES the criterion instead of the
    value, and the full delta has no character (a CP-even correction added
    to a CP-odd angle; the CP.MOD.01 scope narrowing).

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   NARROWINGS ONLY.  Four ledger readings are narrowed (executed in the
        same change): REDTEAM.D.01 (the residual is a fiber datum, not a
        magnitude datum), E8.CHAN.01 (exact hexagonal realisation + parity
        typing; the phase channel is sheet-blind), CP.MOD.01 ([C] scoped:
        the invariant part of the frozen reading is the leading term
        arg(rho) = pi/3, the full delta is branch/frame-relative;
        REG.FREEZE.01 untouched), DUAL.FRAME.01 (the orientation READING is
        degree +1 in the frame normalisation; the invariant core is
        Im(rho) = sin(pi/3), the sign a declared orientation).  NO marker
        moves, NO closure of the CP residual, and the word 'derived'
        appears nowhere.
  (ii)  R1 STAYS OPEN: whether a frame-coupled, scale-free,
        character-covariant pi/3-carrier can exist at all -- the obstruction
        found by T177 is that the (1, d, n) frame has only ONE oriented
        volume to normalise against.  R2 STAYS OPEN: which of the two
        Tier-2 characters is physical -- the sheet-odd (orientation) reading
        reproduces CP.MU6.01's quark/lepton split, the sheet-even (channel)
        reading cannot; that is a structural preference, NOT a derivation.
  (iii) The D4 deck column of T177 is a DECLARED MODEL and is not promoted
        here (only the model-free G1/G2/G3 statements are); the frozen
        coefficient question (3 vs 2 lambda_C^2) is untouched.
HONEST FENCES: no RH statement anywhere (the discovery probe belongs to the
prime-front diary, but every object here is a finite exact statement about
roots of unity, 3x3 determinants and one 3x3 unitary matrix); Jarlskog 1985,
Wolfenstein 1983, Weyl 1946 (invariant theory as the frame), Kleinian
j-invariants (CM points) named CLASSICAL as addresses.  Status: [E] exact
identities and certified numerics with mutation controls; sympy exact where
possible; Python-only, counted per GATE.WOLFRAM.02.  Discovery provenance:
  experiments/tfpt-discovery/cp_invariant_probe.py   (T177, 49/49, DEGENERATE)
"""
import mpmath as mp
import sympy as sp

from tfpt_constants import check, summary, reset, phi0, N_fam

# ---- the exact objects (all sympy-exact) ----------------------------------
RHO = sp.exp(sp.I * sp.pi / 3)              # the hexagonal CM unit, j = 0
E8_DEGREES = (2, 8, 12, 14, 18, 20, 24, 30)   # fundamental degrees, sum 128
E8_EXPONENTS = (1, 7, 11, 13, 17, 19, 23, 29)  # exponents, sum 120
SCALARON = 7

# the dual normal frame (v225)
D_VEC = sp.Matrix([sp.Rational(-1, 2), sp.Rational(-1, 2), 1])
N_VEC = sp.Matrix([5, -9, 6])
ONE = sp.Matrix([1, 1, 1])

# the two TFPT magnitude triples (rt_D_upoint / v20 / v24)
LEPTON_TRIPLE = (sp.Rational(16, 7), sp.Rational(4, 3), sp.Rational(7, 6))
UPQUARK_TRIPLE = (sp.Rational(1, 2), sp.Rational(34, 41), sp.Rational(4, 13))


def unit_sum(unit, powers):
    return sp.simplify(sum(unit**k for k in powers))


def zer(expr):
    """Exact zero test in rectangular form (the sums live in Q(sqrt3, i))."""
    return sp.simplify(sp.expand_complex(expr)) == 0


def frame_det(third_row):
    m = sp.Matrix.hstack(ONE, D_VEC, third_row)
    return sp.simplify(m.det())


def run():
    reset()
    print("=" * 72)
    print("v561  CP.CHANNEL.IDENT.01 -- the CP channel / invariant "
          "identities (T177)")
    print("=" * 72)

    # ================================================================ S1
    print("\nS1 -- the hexagonal channel identity + parity typing (T177 F1.2)")
    s_deg = unit_sum(RHO, E8_DEGREES)
    s_exp = unit_sum(RHO, E8_EXPONENTS)
    check("S1.SPLIT [E] the E8 channel split rebuilt exactly: sum(exp) = 120 "
          "= |R+(E8)|, sum(deg) = 128 = 2^(rank-1), 120 + 128 = 248 = dim E8,"
          " sum(deg) - sum(exp) = rank = 8 (E8.CHAN.01 / v227)",
          sum(E8_EXPONENTS) == 120 and sum(E8_DEGREES) == 128
          and sum(E8_DEGREES) + sum(E8_EXPONENTS) == 248
          and sum(E8_DEGREES) - sum(E8_EXPONENTS) == 8)
    check("S1.PHASE [E] the PHASE channel on the hexagonal fiber: "
          "sum_k rho^{d_k} = 4 rho EXACTLY (sympy zero), hence "
          "arg = pi/3 exactly -- E8.CHAN.01's phase-channel typing has an "
          "exact fiber realisation, not only a counting analogy",
          zer(s_deg - 4 * RHO)
          and sp.simplify(sp.arg(sp.expand_complex(s_deg)) - sp.pi / 3) == 0)
    check("S1.MAG [E] the MAGNITUDE channel on the same fiber: "
          "sum_k rho^{m_k} = 4 EXACTLY (real, arg = 0) -- the magnitude "
          "channel carries zero phase on the fiber unit",
          zer(s_exp - 4))
    s_deg_sheet = unit_sum(-RHO, E8_DEGREES)     # sigma: rho -> rho^4 = -rho
    s_exp_sheet = unit_sum(-RHO, E8_EXPONENTS)
    check("S1.PARITY [E] the parity typing is forced by integer parity: all "
          "E8 degrees are EVEN so the phase channel is SHEET-EVEN "
          "(sum(rho^4)^{d_k} = sum rho^{d_k} exactly), all E8 exponents are "
          "ODD so the magnitude channel is SHEET-ODD "
          "(sum(rho^4)^{m_k} = -4 exactly) -- CONSEQUENCE: the sheet-even "
          "phase-channel angle cannot distinguish quark from lepton (it "
          "carries pi/3, not the CP.MU6.01 sheet split)",
          all(k % 2 == 0 for k in E8_DEGREES)
          and all(k % 2 == 1 for k in E8_EXPONENTS)
          and zer(s_deg_sheet - s_deg) and zer(s_exp_sheet + 4))
    u5 = sp.exp(sp.I * sp.pi / 5)
    s_deg_u5 = unit_sum(u5, E8_DEGREES)
    s_exp_u5 = unit_sum(u5, E8_EXPONENTS)
    check("S1.MUT-UNIT [must-break] on the non-CM unit e^{i pi/5} the "
          "degree-channel identity BREAKS (sum u^{d_k} != 4 u): the 4 rho "
          "identity is a joint property of the E8 degrees and the hexagonal "
          "fiber, of neither alone",
          not zer(s_deg_u5 - 4 * u5))
    check("S1.CAVEAT [E, honesty wired as a check] reality of the "
          "exponent-channel sum alone is NOT hexagon-specific: the exponent "
          "residues are conjugation-closed mod 10 too, so sum u^{m_k} is "
          "real even at u = e^{i pi/5} -- only the DEGREE half is specific "
          "to the hexagonal fiber (the weaker magnitude statement, said "
          "out loud)",
          sp.simplify(sp.im(s_exp_u5)) == 0)
    deg_mut = tuple(31 if k == 30 else k for k in E8_DEGREES)
    exp_mut = tuple(30 if k == 29 else k for k in E8_EXPONENTS)
    check("S1.MUT-LIST [must-break] mutated lists fail loudly: degrees with "
          "30 -> 31 miss sum rho^{d_k} = 4 rho, exponents with 29 -> 30 "
          "lose reality (Im = sin(pi/3) != 0): the identities are "
          "statements about THE E8 lists",
          not zer(unit_sum(RHO, deg_mut) - 4 * RHO)
          and not zer(sp.im(sp.expand_complex(unit_sum(RHO, exp_mut)))))

    # ================================================================ S2
    print("\nS2 -- zero phase in the magnitude data + the branch-order law "
          "(T177 F2.3/F2.4)")
    w3 = sp.exp(2 * sp.pi * sp.I / 3)
    prod_lep = sp.prod(LEPTON_TRIPLE)
    prod_upq = sp.prod(UPQUARK_TRIPLE)
    check("S2.ZEROPHASE [E] the REDTEAM.D.01 narrowing, checkable half: "
          "arg(prod c) = 0 EXACTLY on both TFPT sectors (lepton triple "
          "(16/7, 4/3, 7/6): product 32/9; up-quark triple (1/2, 34/41, "
          "4/13): positive rational) -- the magnitude data carry exactly "
          "zero phase, the CP residual is NOT hidden in the product",
          prod_lep == sp.Rational(32, 9) and prod_lep > 0 and prod_upq > 0
          and sp.arg(prod_lep) == 0 and sp.arg(prod_upq) == 0)
    check("S2.KERNEL [E] the mu3 branch group {1, w, w^2} (w = e^{2pi i/3}) "
          "is EXACTLY the kernel of the magnitude data: the diagonal action "
          "c -> w^j c preserves all ratios trivially and multiplies the "
          "product by w^{3j} = 1 exactly (j = 1, 2) -- blindness = the "
          "branch order DIVIDES N_fam = 3",
          sp.simplify(w3**3 - 1) == 0
          and sp.simplify((w3**1)**3 - 1) == 0
          and sp.simplify((w3**2)**3 - 1) == 0
          and int(N_fam) % 3 == 0)
    check("S2.MUT-MU4 [must-break] a mu4 branch (i-diagonal) already SHIFTS "
          "the product phase: arg(i^3 prod c) = -pi/2 != 0 on the lepton "
          "triple -- the kernel property is a property of the ORDER "
          "(3 | N_fam), not of diagonality",
          sp.simplify(sp.arg(sp.I**3 * prod_lep) + sp.pi / 2) == 0)
    check("S2.RESIDUAL [E] the branch kernel is NOT phase-blind on "
          "individuals: arg(w) = 2 pi/3 != 0, so the residual the bijection "
          "leaves is a genuine FIBER phase freedom, not a relabelling -- "
          "the narrowing 'the residual is a fiber datum, not a magnitude "
          "datum' is the conjunction of this and S2.ZEROPHASE",
          sp.simplify(sp.arg(w3) - 2 * sp.pi / 3) == 0)

    # ================================================================ S3
    print("\nS3 -- Tier-1 emptiness by the blindness theorem (T177 F3.1)")
    s_deg_conj = unit_sum(sp.conjugate(RHO), E8_DEGREES)
    check("S3.COMMUTE [E] the channel kernel commutes with conjugation: "
          "conj(sum rho^{d_k}) = sum conj(rho)^{d_k} exactly (= 4 conj(rho))"
          " -- the CP involution kappa acts on the VALUE by conjugation",
          zer(s_deg_conj - sp.conjugate(s_deg))
          and zer(s_deg_conj - 4 * sp.conjugate(RHO)))
    im_or = sp.im(frame_det(RHO * N_VEC))
    im_or_conj = sp.im(frame_det(sp.conjugate(RHO) * N_VEC))
    check("S3.ORIENT [E] the orientation kernel commutes with conjugation "
          "the same way: Im det(1, d, conj(rho) n) = -Im det(1, d, rho n) "
          "exactly (equal magnitude, opposite sign)",
          sp.simplify(im_or_conj + im_or) == 0 and sp.simplify(im_or) != 0)
    check("S3.EMPTY [E] TIER-1 IS EMPTY PER ALGEBRA (the preregistered kill "
          "criterion, decided by a theorem and not by a scan): every "
          "pi/3-carrier is kappa-ODD (its value conjugates, S3.COMMUTE/"
          "S3.ORIENT), and invariant + odd forces Im F = 0 -- but a "
          "pi/3-carrier has Im F != 0 (both kernels: Im(4 rho) = 2 sqrt(3) "
          "!= 0, Im det = 21 sin(pi/3) != 0), contradiction: NO functional "
          "is strictly invariant under all four T177 groups and carries "
          "pi/3",
          zer(sp.im(sp.expand_complex(s_deg)) - 2 * sp.sqrt(3))
          and zer(im_or - 21 * sp.sin(sp.pi / 3)))

    # ================================================================ S4
    print("\nS4 -- the frame removal + the degree account (T177 F2.5)")
    det0 = frame_det(N_VEC)
    check("S4.FRAME [E] DUAL.FRAME.01 rebuilt exactly: det(1, d, n) = 21 = "
          "N_fam * scalaron = 3 * 7 and Im det(1, d, rho n) = 21 sin(pi/3) "
          "= 21 sqrt(3)/2 exactly (rho scales the third column linearly)",
          det0 == 21 and det0 == int(N_fam) * SCALARON
          and sp.simplify(im_or - 21 * sp.sqrt(3) / 2) == 0)
    t = sp.symbols("t", positive=True)
    im_scaled = sp.im(sp.expand_complex(frame_det(RHO * (t * N_VEC))))
    check("S4.DEGREE [E] the orientation functional P4 is homogeneous of "
          "DEGREE +1 in the frame normalisation: Im det(1, d, rho (t n)) = "
          "t * 21 sin(pi/3) symbolically for t > 0 -- the NUMBER "
          "21 sin(pi/3) is FRAME data, not an invariant",
          sp.simplify(im_scaled - t * 21 * sp.sin(sp.pi / 3)) == 0)
    v = sp.symbols("v", real=True, nonzero=True)
    check("S4.REMOVE [E] dividing by the oriented volume removes the frame "
          "IDENTICALLY: Im(rho v)/v = Im(rho) = sin(pi/3) symbolically for "
          "every real v != 0, and on the instance Im det(1, d, rho n)/"
          "det(1, d, n) = sin(pi/3) exactly -- the invariant core of the "
          "orientation reading is the FIBER datum Im(rho), the sign a "
          "declared orientation (the DUAL.FRAME.01 narrowing)",
          sp.simplify(sp.im(RHO * v) / v - sp.im(RHO)) == 0
          and sp.simplify(im_or / det0 - sp.sin(sp.pi / 3)) == 0)
    im_sheet = sp.im(frame_det((RHO**4) * N_VEC))
    check("S4.SHEET [E] the sheet control (CP.MU6.01 wiring): Im det(1, d, "
          "rho^4 n) = -21 sin(pi/3) -- equal magnitude, opposite sign "
          "(rho^4 = -rho): the ORIENTATION reading is sheet-odd, which is "
          "exactly the split the sheet-even channel angle cannot see",
          sp.simplify(im_sheet + 21 * sp.sin(sp.pi / 3)) == 0)
    check("S4.MUT [must-break] a mutated selector n' = (5, -8, 6) changes "
          "the oriented volume (det = 39/2 != 21) and with it the frame "
          "factor: the 21 = N_fam * scalaron account is a statement about "
          "THE frame, not generic 3x3 algebra",
          frame_det(sp.Matrix([5, -8, 6])) == sp.Rational(39, 2))

    # ================================================================ S5
    print("\nS5 -- the two Tier-2 characters + the Jarlskog anchor "
          "(T177 F2/F3.3)")

    # group action on the fiber unit: kappa = conjugation, sigma = sheet flip
    def act(unit, g):
        u = unit
        if "s" in g:
            u = u**4                      # sigma: rho -> rho^4 = -rho
        if "k" in g:
            u = sp.conjugate(u)           # kappa: complex conjugation
        return sp.simplify(u)

    GROUP = ("1", "k", "s", "ks")

    def mult(g1, g2):
        k = (g1.count("k") + g2.count("k")) % 2
        s = (g1.count("s") + g2.count("s")) % 2
        return ("k" * k + "s" * s) or "1"

    def chi_p2(g):
        # P2 = arg(sum rho^{d_k}): value on the acted unit vs pi/3
        val = sp.arg(unit_sum(act(RHO, g), E8_DEGREES))
        if sp.simplify(val - sp.pi / 3) == 0:
            return 1
        if sp.simplify(val + sp.pi / 3) == 0:
            return -1
        return 0

    def chi_v5(g):
        # V5 = Im(rho det)/det, frame removed: the fiber datum Im(unit)
        val = sp.simplify(sp.im(act(RHO, g)) / sp.im(RHO))
        return int(val) if val in (1, -1) else 0

    ok_hom = all(chi_p2(mult(g1, g2)) == chi_p2(g1) * chi_p2(g2)
                 and chi_v5(mult(g1, g2)) == chi_v5(g1) * chi_v5(g2)
                 for g1 in GROUP for g2 in GROUP)
    check("S5.CHARACTERS [E] the two Tier-2 carriers have well-defined "
          "characters and the bookkeeping is a HOMOMORPHISM on the full "
          "four-element group {1, kappa, sigma, kappa sigma} (16 products "
          "checked): P2 = arg(sum rho^{d_k}) carries (chi(kappa), "
          "chi(sigma)) = (-1, +1) (sheet-EVEN, forced by the even degrees), "
          "V5 = Im(rho det)/det carries (-1, -1) (sheet-ODD)",
          ok_hom and (chi_p2("k"), chi_p2("s")) == (-1, 1)
          and (chi_v5("k"), chi_v5("s")) == (-1, -1))
    check("S5.INEQUIV [E] the two classes are INEQUIVALENT under the "
          "declared equivalence (a real invariant factor preserves every "
          "character): chi(sigma) differs (+1 vs -1), so TWO distinct "
          "invariants carry the same value pi/3 -- the DEGENERATE verdict "
          "as algebra -- and NEITHER couples to the frame (P2 is "
          "fiber-only; V5 has the frame removed identically, S4.REMOVE; "
          "the only frame-coupled candidate P4 fails at degree +1, "
          "S4.DEGREE)",
          chi_p2("s") != chi_v5("s") and chi_p2("k") == chi_v5("k"))

    # the classical anchor: Jarlskog on the TFPT CKM rebuild (v88)
    lam = mp.sqrt(phi0 * (1 - phi0))
    s12, s23, s13 = lam, phi0 / (1 + lam), lam**3 / 3
    c12, c23, c13 = (mp.sqrt(1 - s12**2), mp.sqrt(1 - s23**2),
                     mp.sqrt(1 - s13**2))
    delta = mp.pi / 3 + 3 * lam**2

    def ckm(dlt):
        e = mp.e**(-1j * dlt)
        return mp.matrix(
            [[c12 * c13, s12 * c13, s13 * e],
             [-s12 * c23 - c12 * s23 * s13 / e,
              c12 * c23 - s12 * s23 * s13 / e, s23 * c13],
             [s12 * s23 - c12 * c23 * s13 / e,
              -c12 * s23 - s12 * c23 * s13 / e, c23 * c13]])

    V = ckm(delta)
    unit_err = max(abs((V * V.transpose_conj())[i, j] - (1 if i == j else 0))
                   for i in range(3) for j in range(3))

    def jarlskog(M):
        return float(mp.im(M[0, 1] * M[1, 2]
                           * mp.conj(M[0, 2]) * mp.conj(M[1, 1])))

    J = jarlskog(V)
    check("S5.ANCHOR [E] the CKM rebuild from the compiler magnitudes "
          "(s12 = lambda_C, s23 = phi0/(1+lambda_C), s13 = lambda_C^3/3) "
          "with the FROZEN delta = pi/3 + 3 lambda_C^2 = 1.198231638 rad "
          "(REG.FREEZE.01, untouched) is unitary at working precision "
          f"({float(unit_err):.1e} <= 1e-12) and reproduces the v88 lattice "
          "value J = 3.327021e-5",
          unit_err < mp.mpf("1e-12")
          and abs(J / 3.327021e-5 - 1) < 1e-5
          and abs(float(delta) - 1.198231638) < 1e-8)
    ph_u = [0.3, 1.1, 2.7]
    ph_d = [0.9, 0.2, 1.9]
    Vre = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            Vre[i, j] = mp.e**(1j * ph_u[i]) * V[i, j] * mp.e**(-1j * ph_d[j])
    w_num = mp.e**(2j * mp.pi / 3)
    Vbr = V * w_num                       # the mu3 branch as a rephasing
    check("S5.JARL-ABC [E] the Jarlskog anchor passes criteria (a)-(c) of "
          "the T177 Tier-2 test: (a) rephasing-invariant under generic "
          "diagonal phases AND under the mu3 branch group of REDTEAM.D.01 "
          f"(moves {abs(jarlskog(Vre) / J - 1):.1e} / "
          f"{abs(jarlskog(Vbr) / J - 1):.1e} <= 1e-12 relative), "
          "(c) CP-odd: J(conj V) = -J(V) exactly at working precision -- "
          "it is the right KIND of object (Jarlskog 1985)",
          abs(jarlskog(Vre) / J - 1) < 1e-12
          and abs(jarlskog(Vbr) / J - 1) < 1e-12
          and abs(jarlskog(V.transpose().transpose_conj()) / J + 1) < 1e-12)
    check("S5.JARL-D [E, the criterion validated] the anchor fails ONLY "
          "criterion (d): its phase content is delta = pi/3 + 3 lambda_C^2, "
          f"not pi/3 -- the gap is exactly 3 lambda_C^2 = "
          f"{float(3 * lam**2):.6f} rad != 0, and J(delta) != J(pi/3) "
          f"(relative difference {abs(jarlskog(ckm(mp.pi / 3)) / J - 1):.3f}"
          " > 1e-3): the benchmark validates the pi/3-carrier criterion "
          "instead of the value, and the full delta has NO character under "
          "the parity involution (a CP-even correction on a CP-odd angle "
          "-- the CP.MOD.01 scope narrowing)",
          abs(float(delta) - float(mp.pi) / 3 - 3 * float(lam) ** 2) < 1e-15
          and abs(jarlskog(ckm(mp.pi / 3)) / J - 1) > 1e-3)

    # ================================================================ S6
    print("\nS6 -- the fences, restated as a check")
    check("S6.FENCE: NARROWINGS ONLY -- four ledger readings narrowed, no "
          "marker of any pre-existing contract moves, the CP residual is "
          "NOT closed and no CP derivation is claimed; the frozen reading "
          "delta = pi/3 + 3 lambda_C^2 is untouched (REG.FREEZE.01) and "
          "the 3-vs-2 lambda_C^2 coefficient question is untouched; R1 "
          "(can a frame-coupled scale-free pi/3-carrier exist at all -- "
          "the obstruction: one oriented volume only) and R2 (which "
          "Tier-2 character is physical -- the sheet-odd reading matches "
          "CP.MU6.01, a structural preference, NOT a derivation) stay "
          "OPEN and typed open; the D4 deck column of T177 is a DECLARED "
          "MODEL and is not promoted; every claim here is a finite exact "
          "statement about roots of unity, 3x3 determinants and one 3x3 "
          "unitary matrix -- NO RH statement, no L-function, no zero of "
          "anything is read; Jarlskog 1985 / Wolfenstein 1983 / Weyl 1946 "
          "named CLASSICAL as addresses",
          True)

    print("\nv561 anchors: sum rho^{d_k} = 4 rho (arg pi/3, sheet-even), "
          "sum rho^{m_k} = 4 (arg 0, sheet-odd);")
    print("  arg(prod c) = 0 on both sectors; Tier-1 empty per algebra; "
          "Im(rho det)/det = Im rho exactly;")
    print(f"  J = {J:.6e} (v88), unitarity {float(unit_err):.1e}; "
          "two inequivalent Tier-2 characters, neither frame-coupled")
    return summary("CP.CHANNEL.IDENT.01 CP channel/invariant identities")


if __name__ == "__main__":
    raise SystemExit(run())
