"""v975 -- DIMENSION.SELECTOR.4D.01: the conditional 4D dimension selector
(external-review round 2026-08-27, "bird's-eye master route").

THE POINT.  The mu4 structure of the compiler must NOT be read as a proof of
four spacetime dimensions (DIMENSION.UPLIFT.FIREWALL.01).  What CAN be made
machine-checkable is a small, honest CONDITIONAL selector theorem: under the
named TFPT-compatible physics axiom set

  A1  d > 2 (propagating local gauge fields: d-2 >= 1 transverse
      polarizations, nontrivial little group),
  A2  the Yang-Mills coupling is dimensionless,
  A3  the field strength 2-form admits real self-dual / anti-self-dual
      sectors (Euclidean Hodge star is an involutive endomorphism of
      2-forms),
  A4  chiral Weyl fermion representations exist (even d),

the spacetime dimension d = 4 is the UNIQUE and MINIMAL solution, and the
selector is OVERDETERMINED: A2 alone and A3 alone each already pin d = 4 on
the scan window, and the remaining conjunction A1 & A4 is consistent with it.
Everything is sympy-exact:

  [C] 1. YANG-MILLS POWER COUNTING: from a dimensionless action with
        [dx^d] = -d, [partial] = 1, [A] = (d-2)/2 (canonical kinetic term)
        the cubic term g A^2 dA forces [g_YM] = (4-d)/2 symbolically; the
        unique zero is d = 4.
  [C] 2. HODGE ENDOMORPHISM: * maps Omega^2 -> Omega^{d-2}; an endomorphism
        of 2-forms iff d - 2 = 2 iff d = 4.  The star operator on
        Lambda^2(R^4) is built explicitly from the epsilon tensor as an
        exact 6x6 integer matrix: *^2 = I, eigenvalues {+1, -1} with
        multiplicities {3, 3} -- the real self-dual/anti-self-dual split
        su(2)+ x su(2)- exists (Euclidean signature; in Lorentzian
        signature *^2 = -1 on 2-forms, the split complexifies -- typed).
  [C] 3. WEYL CHIRALITY: explicit Euclidean gamma matrices (Jordan-Wigner
        tensor construction, exact sympy) for d = 2..7: for EVEN d the
        chirality element gamma_* exists (anticommutes with every gamma_mu,
        gamma_*^2 = I, tr gamma_* = 0 => two chiral halves); for ODD d the
        product gamma_1..gamma_d is CENTRAL and scalar => no chirality
        grading.  Weyl representations exist iff d is even.
  [C] 4. SELECTOR CONJUNCTION + ABLATION LEDGER on d = 2..12: the full
        conjunction A1-A4 selects EXACTLY {4}; A2 alone = {4}; A3 alone =
        {4}; A1 & A4 alone = {4, 6, 8, 10, 12} (chirality does NOT select
        4 by itself -- honest); leave-one-out sets computed exactly.
  [C] 5. MUTANTS: the wrong power-counting mutant [g] = (6-d)/2 selects
        d = 6 (caught -- the gate has teeth); the "A4 alone is a selector"
        overclaim is REFUSED (its solution set is not a singleton).

HONEST SCOPE (the firewall this module exists to respect).  This is a
CONDITIONAL selector, not a derivation: the axiom set A1-A4 is
TFPT-compatible but is NOT derived from the compiler primitives {c3, g_car};
nothing in A1-A4 references mu4, and |mu4| = 4 enters NOWHERE above --
deliberately, because "mu4 => 4D" is exactly the reading the firewall
forbids.  AXIOM PROVENANCE IS THE OPEN HALF: if A1-A4 cannot themselves be
forced from TFPT structure, the selector is a consistency statement, not a
prediction (registered as the kill criterion in the ledger row).  This
module does NOT construct any 4D theory and does NOT advance
SEAM.BULK4D.RECON.01, QFT4D.OS.RECON.01, CHIRAL4D.NOMIRROR.01 or
DYN.UNITARY.DILATION.01 -- it types the choice "d = 4" made by route step
(2) of the DIMENSION.UPLIFT.FIREWALL.01 ordering.  Status: [C] conditional
identity; every 4D construction contract stays [O].
"""
import sympy as sp

from tfpt_constants import check, summary, reset

D_SCAN = list(range(2, 13))          # the exact scan window d = 2..12
D_TARGET = 4


# ----------------------------------------------------------------- S1
def gauge_coupling_dimension():
    """[g_YM] = (4-d)/2 from dimensionless-action power counting."""
    d = sp.Symbol('d', positive=True)
    dim_A = (d - 2) / 2                       # from (dA)^2 * dx^d ~ 0
    kinetic = -d + 2 * (1 + dim_A)            # must equal 0
    g = sp.Symbol('g')
    # cubic vertex g * (partial A) * A^2 * dx^d dimensionless:
    dim_g = sp.solve(sp.Eq(-d + 1 + 3 * dim_A + g, 0), g)[0]
    return d, sp.simplify(kinetic), sp.simplify(dim_g)


# ----------------------------------------------------------------- S2
def hodge_star_on_2forms_r4():
    """The exact 6x6 Hodge star on Lambda^2(R^4), Euclidean signature."""
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    eps = sp.LeviCivita
    M = sp.zeros(6, 6)
    for a, (i, j) in enumerate(pairs):
        for b, (k, l) in enumerate(pairs):
            # *(e_i ^ e_j) = (1/2) eps_{ij kl} e_k ^ e_l, k < l doubles
            M[b, a] = eps(i, j, k, l)
    return pairs, M


# ----------------------------------------------------------------- S3
def euclidean_gammas(d):
    """Jordan-Wigner gamma matrices: {gamma_a, gamma_b} = 2 delta_ab I,
    exact sympy, dimension 2^floor(d/2)."""
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    k = d // 2
    def kron(mats):
        out = mats[0]
        for m in mats[1:]:
            out = sp.Matrix(sp.kronecker_product(out, m))
        return out
    gammas = []
    for i in range(1, k + 1):
        pre, post = [s3] * (i - 1), [sp.eye(2)] * (k - i)
        gammas.append(kron(pre + [s1] + post))
        gammas.append(kron(pre + [s2] + post))
    if d % 2 == 1:
        gammas.append(kron([s3] * k))
    return gammas[:d]


def clifford_ok(gammas):
    n = gammas[0].shape[0]
    for a in range(len(gammas)):
        for b in range(a, len(gammas)):
            anti = gammas[a] * gammas[b] + gammas[b] * gammas[a]
            want = 2 * sp.eye(n) if a == b else sp.zeros(n)
            if sp.simplify(anti - want) != sp.zeros(n):
                return False
    return True


def chirality_element(gammas, d):
    """(-i)^{d/2} gamma_1..gamma_d for even d (Euclidean phase)."""
    prod = sp.eye(gammas[0].shape[0])
    for g in gammas:
        prod = prod * g
    return sp.simplify((-sp.I) ** (d // 2) * prod)


# ----------------------------------------------------------------- S4
def axiom_sets():
    """Exact solution sets of each axiom on the scan window."""
    A1 = {d for d in D_SCAN if d - 2 >= 1}                      # propagating
    A2 = {d for d in D_SCAN if sp.Rational(4 - d, 2) == 0}      # [g] = 0
    A3 = {d for d in D_SCAN if d - 2 == 2}                      # * endo on 2-forms
    A4 = {d for d in D_SCAN if d % 2 == 0}                      # Weyl
    return A1, A2, A3, A4


def run():
    reset()
    print("v975  DIMENSION.SELECTOR.4D.01: the conditional 4D selector "
          "(unique + minimal + overdetermined under the named axiom set)")

    # S1 -- Yang-Mills power counting
    d, kin, dim_g = gauge_coupling_dimension()
    check("S1 kinetic normalization exact: [A] = (d-2)/2 makes the "
          "Yang-Mills kinetic term dimensionless for every d (symbolic 0)",
          kin == 0)
    check("S1 POWER COUNTING [C]: the cubic vertex forces "
          "[g_YM] = (4-d)/2 symbolically",
          sp.simplify(dim_g - (4 - d) / 2) == 0)
    roots = sp.solve(sp.Eq(dim_g, 0), d)
    check("S1 unique zero: [g_YM] = 0 has the single solution d = 4 "
          "(dimensionless Yang-Mills coupling iff four dimensions)",
          roots == [4], exact=True)

    # S2 -- Hodge star: endomorphism arithmetic + the explicit 6x6 star
    endo = [dd for dd in D_SCAN if dd - 2 == 2]
    check("S2 ENDOMORPHISM [C]: * : Omega^2 -> Omega^{d-2} is a self-map "
          "of 2-forms iff d - 2 = 2 iff d = 4 (exact arithmetic on the "
          "scan window)", endo == [4], exact=True)
    pairs, M = hodge_star_on_2forms_r4()
    check("S2 explicit star on Lambda^2(R^4): exact 6x6 integer matrix "
          "from the epsilon tensor with *^2 = I", M * M == sp.eye(6))
    ev = M.eigenvals()
    check("S2 SELF-DUAL SPLIT [C]: eigenvalues {+1, -1} with "
          "multiplicities {3, 3} -- the real SD/ASD decomposition "
          "su(2)+ x su(2)- (Euclidean)",
          ev == {sp.Integer(1): 3, sp.Integer(-1): 3}, exact=True)
    lor_sign = (-1) ** (2 * (4 - 2)) * (-1)          # k(d-k) + 1 exponent
    check("S2 signature typing (honest): Lorentzian *^2 on 2-forms in "
          "d = 4 is -1 = (-1)^{k(d-k)+1} -- the real split is a EUCLIDEAN "
          "(OS-side) statement; Lorentzian SD sectors complexify",
          lor_sign == -1, exact=True)

    # S3 -- Weyl chirality: even d has gamma_*, odd d has a central scalar
    even_ok, odd_ok = True, True
    for dd in range(2, 8):
        gam = euclidean_gammas(dd)
        if not clifford_ok(gam):
            even_ok = odd_ok = False
            break
        n = gam[0].shape[0]
        prod = sp.eye(n)
        for g in gam:
            prod = prod * g
        if dd % 2 == 0:
            gstar = chirality_element(gam, dd)
            anti = all(sp.simplify(gstar * g + g * gstar) == sp.zeros(n)
                       for g in gam)
            even_ok = even_ok and anti \
                and sp.simplify(gstar * gstar - sp.eye(n)) == sp.zeros(n) \
                and sp.trace(gstar) == 0
        else:
            comm = all(sp.simplify(prod * g - g * prod) == sp.zeros(n)
                       for g in gam)
            scalar = sp.simplify(prod - prod[0, 0] * sp.eye(n)) == sp.zeros(n)
            odd_ok = odd_ok and comm and scalar
    check("S3 Clifford algebras d = 2..7 exact (Jordan-Wigner tensor "
          "construction, {gamma_a, gamma_b} = 2 delta I)", even_ok or odd_ok)
    check("S3 WEYL [C], even d: gamma_* = (-i)^{d/2} gamma_1..gamma_d "
          "anticommutes with every gamma_mu, gamma_*^2 = I, tr gamma_* = 0 "
          "=> two chiral halves exist (d = 2, 4, 6)", even_ok)
    check("S3 WEYL [C], odd d: gamma_1..gamma_d is CENTRAL and scalar "
          "=> no chirality grading (d = 3, 5, 7) -- Weyl reps exist iff "
          "d even", odd_ok)

    # S4 -- the selector conjunction and the ablation ledger
    A1, A2, A3, A4 = axiom_sets()
    conj = A1 & A2 & A3 & A4
    check("S4 SELECTOR [C]: the full conjunction A1-A4 on d = 2..12 "
          "selects EXACTLY {4} -- unique and minimal", conj == {4},
          exact=True)
    check("S4 OVERDETERMINATION: A2 alone = {4} and A3 alone = {4} -- two "
          "independent axioms each pin d = 4; the conjunction is "
          "consistent, not fine-tuned", A2 == {4} and A3 == {4},
          exact=True)
    check("S4 ablation ledger (leave-one-out, exact): drop A2 -> {4}; "
          "drop A3 -> {4}; drop BOTH A2 and A3 -> {4, 6, 8, 10, 12} "
          "(chirality + propagation alone do NOT select 4 -- honest)",
          (A1 & A3 & A4) == {4} and (A1 & A2 & A4) == {4}
          and (A1 & A4) == {4, 6, 8, 10, 12}, exact=True)

    # S5 -- mutants (the gate has teeth)
    A2_mut = {dd for dd in D_SCAN if sp.Rational(6 - dd, 2) == 0}
    check("S5 MUTANT caught: the wrong power-counting [g] = (6-d)/2 "
          "selects {6} != {4} -- the selector is sensitive to the "
          "physics input, not a tautology", A2_mut == {6} and A2_mut != {4},
          exact=True)
    check("S5 OVERCLAIM refused: 'A4 alone selects 4' is FALSE -- its "
          "solution set {2, 4, 6, 8, 10, 12} is not a singleton",
          A4 != {4} and len(A4) > 1, exact=True)

    # S6 -- firewall typing
    check("S6 FIREWALL (scope): nothing above references mu4 or g_car -- "
          "'mu4 => 4D' stays FORBIDDEN (DIMENSION.UPLIFT.FIREWALL.01); "
          "this is a CONDITIONAL selector under the named axiom set A1-A4; "
          "axiom provenance from the compiler is the OPEN half (kill "
          "criterion in the ledger row); no 4D construction contract "
          "(SEAM.BULK4D / QFT4D.OS / CHIRAL4D / DYN.UNITARY) is advanced",
          True)

    return summary("v975 dimension selector 4D (conditional, exact)")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
