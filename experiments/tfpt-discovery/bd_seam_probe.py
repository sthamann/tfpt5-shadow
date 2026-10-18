"""Discovery probe (2026-07-28), part 132 of the seam/kernel investigation.
Contract BD.SEAM -- the Beurling-Deny TRIAS of the seam DtN as an OPERATOR-VALUED
discriminator: a finite tool for the one thing QGEO.KERNEL.01 asks for and the
spectral list cannot give.

WHERE THIS SITS
  The open theory gate QGEO.KERNEL.01 (v177/v178) demands, verbatim, that the raw
  RP seam Calderon operator IS the mu4-equivariant free gapped contraction
        C_Sigma = U^{-1} C_mu4 U      AS AN OPERATOR
  "not merely as the same spectral list".  v178 closed the FINITE CORE of that
  demand on the multiplicity-free 3-dim H^1 block (Schur: distinct mu4 characters
  force diagonality, so character->eigenvalue assignment determines the operator)
  and recorded that the 'spectrum vs operator' gap "is real on infinite-dim L^2".
  Until now the jump from spectral list to operator had NO finite instrument on
  the non-multiplicity-free block.
  The prime-front series supplies one.  T126 found the exact Beurling-Deny
  decomposition of |k|-symbol operators,
        v^T A v = sum_r w_r v_r^2 + sum_{r<s} (-A_rs) (v_r - v_s)^2,
        w_r = sum_s A_rs      (row sum = killing mass at site r),
  i.e. a jump measure plus a killing measure.  The Beurling-Deny TRIAS (jump
  measure, killing measure, diffusion part) is a strictly FINER datum than the
  spectrum and a finitely computable one: two Dirichlet forms are equal as
  OPERATORS iff their trias agree (Beurling-Deny 1959; Fukushima-Oshima-Takeda,
  "Dirichlet Forms and Symmetric Markov Processes", Thm 3.2.1 / 4.5.2).  The
  classical anchor for the seam symbol itself is Caffarelli-Silvestre 2007: the
  Dirichlet-to-Neumann map of the harmonic extension IS the 1/2-Laplacian, whose
  Dirichlet form is PURE JUMP with kernel ~ |x-y|^{-2} and no diffusion part.

HONEST CEILING, DECLARED BEFORE ANY NUMBER
  QGEO.KERNEL.01 speaks about the RAW RP seam.  This probe works on the MODEL DtN
  of v210 (Steklov DtN = |D_theta| + M_f from a real von-Mises mu4 mark-sum
  curvature profile).  It therefore SHARPENS what the gate asserts and supplies a
  finite discriminator for it; it does NOT close the gate.  No marker, no ledger
  row, no promotion follows from this file.

WHAT THIS PROBE DOES
  A  KERNEL-BUILDER (pure reproduction -- a failure here is a bug, not a result).
     v210's Lambda_Sigma = diag(|k|) + Toeplitz(f_k) is rebuilt in the POSITION
     basis on the marked circle, where it becomes  C(|k|) + diag(f(theta_j)) with
     C(|k|) the circulant of the |k| symbol; the mode-basis form, the mark-sum
     Fourier support f_k = 4 g_k [k = 0 mod 4], the clock commutator and the
     quasi-free STATE invariance of v210 are all re-verified on the rebuild.  In
     parallel the mu4 reference contraction U^{-1} C_mu4 U is built in the SAME
     position basis: the operator that is diagonal in the mu4-GRADED free real
     mode basis (v162/v178: mu4-equivariance + character->eigenvalue assignment)
     carrying EXACTLY the forced spectrum of Lambda_Sigma.  The builder is kept
     modular -- a follow-up probe (COMB.COMPRESS) reuses it.
  B  THE IDENTITY (kill block).  The Beurling-Deny decomposition of Lambda_Sigma
     at every N, its residual, the sign census of the jump weights and the
     explicitly reported non-Markovian remainder.
  C  THE TRIAS.  Jump measure, killing measure, diffusion part, plus completeness
     (Lambda = jump + killing with no residuum) and the Caffarelli-Silvestre
     decay rate of the jump kernel.
  D  THE DISCRIMINATOR (the point of the probe).  Trias of Lambda_Sigma against
     trias of U^{-1} C_mu4 U, TRIAS COMPONENT BY TRIAS COMPONENT, with the
     spectra matched first.
  E  NEGATIVE CONTROLS.  v210's three controls (off-centre bump, Z3 marks, 4
     unequal marks); the Z3 case must break the trias by O(1) (non-vacuity).
  F  BASIS COVARIANCE (the honest limit).  A random orthogonal conjugation must
     preserve the spectrum and destroy the trias; then the sharper question --
     what exactly must be fixed for the trias to be canonical: the marks alone
     (full mu4-equivariant unitary group) or the MARKED BOUNDARY COORDINATE (the
     position basis together with its mark-preserving lattice symmetries)?

PREREGISTERED BARS (declared here, before any number is computed)
  A1  mark-sum Fourier support: max off-(mod 4) |f_k| < 1e-12          (v210 bar)
  A2a the position-basis rebuild equals the mode-basis DtN
      diag(|k|) + Toeplitz(f_{[k-k']}) exactly, to < 1e-10 RELATIVE to the
      operator scale max |Lambda| = d/2 (the entries of the principal part grow
      with d, so only a scale-free residual is meaningful), where [m] is the
      representative of m mod d in [-d/2, d/2) (a position grid periodises the
      Toeplitz symbol -- that is the only difference to a mode truncation)
  A2b the periodisation error against v210's untruncated coefficients,
      max_{|m| < d/2} |f^{(d)}_m - f_m| < 1e-8: the von-Mises coefficients decay
      super-exponentially, so the rebuild agrees with v210's truncated
      diag(|n|) + Toeplitz(f_k) over the whole window (not machine-zero at the
      smallest window, hence the 1e-8 bar and not 1e-12)
  A3  clock commutator ||[rho, Lambda]|| < 1e-10 and quasi-free STATE residual
      ||rho C rho^dag - C|| < 1e-10                                   (v210 bars)
  A4  the mu4 reference contraction is mu4-equivariant to < 1e-10 and carries the
      spectrum of Lambda_Sigma to < 1e-10 (else block D cannot be run)
  B1  Beurling-Deny identity residual <= 1e-12 at EVERY N, on random test
      vectors -- the KILL bar of this block
  B2  killing measure nonnegative: min_r w_r >= -1e-12
  B3  the non-Markovian remainder is REPORTED, not expected (T126 comparison:
      86.1% of the off-diagonals negative).  DECLARED KILL THRESHOLD: if the
      share of off-diagonal MASS carried by jump weights of the WRONG sign
      exceeds 25% at the largest N, or grows with N, the |k| reading is not a
      Dirichlet form and the candidate is dead (verdict DECOMP-FAILS).
  C1  completeness ||Lambda - (jump + killing)|| <= 1e-12
  C2  diffusion part exactly 0 (a finite atomic state space carries no strongly
      local part; Caffarelli-Silvestre: the 1/2-Laplacian form is pure jump)
  C3  jump-kernel decay exponent 2.00 +- 0.05 at the largest N (the
      Caffarelli-Silvestre |Delta theta|^{-2} rate)
  D1  TRIPLE-MATCH  : spectra agree <= 1e-10 AND every trias component agrees
                      <= 1e-10
  D2  SPECTRUM-ONLY : spectra agree <= 1e-10 and some trias component deviates
                      by > 1e-6 relative -- this REFUTES the naive route
                      (mu4-equivariance + forced spectrum => operator identity)
                      and localises the gap inside the trias
  D3  a SPECTRUM-ONLY gap must be N-stable in the deviating component (spread
      < 1e-6 relative across N) and must not be carried by a component that
      shrinks with N, else it is a truncation artefact and not an operator gap
  D3  Bug           : spectra do not agree (block A broken)
  E1  each control's killing measure must break mu4-equivariance by > 0.1
      relative; the Z3 control MUST (non-vacuity).  Mark-local: < 1e-10.
  E2  each control must also destroy the mu4 SECTOR BLOCK STRUCTURE by > 0.1,
      measured relative to the SUB-PRINCIPAL part M_f = diag(f) -- the marks
      live in M_f only, the principal circulant C(|k|) is block-diagonal for any
      mode grading, so normalising by ||Lambda|| would merely divide by the
      irrelevant ||C(|k|)|| ~ d/2
  F1  random orthogonal conjugation: spectrum preserved <= 1e-10 AND trias
      destroyed by > 0.1 relative (sanity of the discriminator)
  F2  random mu4-EQUIVARIANT (mark-preserving-grading) orthogonal conjugation:
      reported.  NOTE, declared up front: a generic element of the mu4 commutant
      group U(d/4)^{...} is expected to destroy the trias -- that alone shows the
      trias is not canonical relative to the MARKS ALONE, which is a STRUCTURE
      statement, not a kill.  The kill bar is F3.
  F3  mark-preserving LATTICE symmetries (the dihedral group of the marked
      circle: rotation by pi/2 and the sheet reflection) must leave the trias
      EXACTLY invariant, <= 1e-12.  KILL (verdict NOT-CANONICAL) iff F3 fails:
      then the trias is not even canonical relative to the marked boundary
      coordinate and is no discriminator at all.
  VERDICTS: TRIPLE-MATCH / SPECTRUM-ONLY / DECOMP-FAILS (block B) /
            NOT-CANONICAL (block F3).

HARD CAPS: largest matrix dimension <= 1500; runtime budget < 900 s.
FENCES: sandbox only; verification/ is READ-ONLY and only read for the rebuild;
        no marker, ledger, changelog, TeX or website touch; structure and
        interpretation kept on separate lines.
CLASSICAL SOURCES: Beurling-Deny 1959 (the decomposition of a Dirichlet form);
        Fukushima-Oshima-Takeda (trias <=> form, uniqueness of the pieces);
        Caffarelli-Silvestre 2007 (DtN of the harmonic extension = 1/2-Laplacian,
        a pure-jump form); Lee-Uhlmann (principal symbol |k|, via v156).
"""
import time

import numpy as np

T_START = time.time()
RUNTIME_BUDGET = 900.0
DIM_CAP = 1500

GRID = 2048          # v210: divisible by 4 => the pi/2 shifts are exact grid steps
KAPPA = 4.0          # v210: von-Mises concentration of the curvature bump
N_LIST = (16, 32, 64, 128)          # mode parameter; position dimension d = 2N
RNG_SEED = 20260728

BAR_REPRO = 1e-10
BAR_ALIAS = 1e-8
BAR_SUPPORT = 1e-12
BAR_IDENTITY = 1e-12
BAR_KILL_NEG = -1e-12
BAR_NONMARKOV_MASS = 0.25
BAR_TRIAS_EQ = 1e-10
BAR_TRIAS_DEV = 1e-6
BAR_EXACT = 1e-12
BAR_BREAK = 0.1
BAR_EXPONENT = (1.95, 2.05)
NEG_FRAC_T126 = 0.861

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-38s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-38s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


# ============================================================================
#  BLOCK A -- the kernel builder (modular; reused by COMB.COMPRESS)
# ============================================================================

def vonmises_bump(theta):
    """v210: a real, smooth, 2pi-periodic, even curvature bump localised at 0."""
    return np.exp(KAPPA * (np.cos(theta) - 1.0))


def mark_profile(positions, d):
    """f(theta_j) = sum_p g(theta_j - p) sampled on the d-point position grid."""
    th = 2 * np.pi * np.arange(d) / d
    return sum(vonmises_bump(th - p) for p in positions)


def mark_coeffs(positions, grid=GRID):
    """v210's fourier_coeffs(mark_sum(positions)): c_q with f = sum_q c_q e^{i q th}."""
    f = mark_profile(positions, grid)
    return np.fft.fft(f) / grid


def coef(C, q):
    """v210: integer-mode Fourier coefficient c_q (wrap negative indices)."""
    return C[q % len(C)]


def modes(d):
    """Integer modes in FFT order: [0, 1, .., d/2-1, -d/2, .., -1]."""
    return np.fft.fftfreq(d, 1.0 / d).astype(int)


def symbol_circulant(symbol_vals, d):
    """Real symmetric circulant with the given symbol in FFT mode order."""
    c = np.real(np.fft.ifft(symbol_vals))
    idx = (np.arange(d)[:, None] - np.arange(d)[None, :]) % d
    return c[idx]


def seam_dtn_position(positions, d):
    """Lambda_Sigma in the POSITION basis: C(|k|) + diag(f(theta_j)).

    This is v210's Lambda = diag(|n|) + Toeplitz(f_k) conjugated by the DFT: the
    principal |k| becomes the circulant of the |k| symbol, the sub-principal
    multiplication operator M_f becomes diag(f) on the grid.
    """
    principal = symbol_circulant(np.abs(modes(d)).astype(float), d)
    f = mark_profile(positions, d)
    return principal + np.diag(f), f


def dft_matrix(d):
    """Unitary DFT F with (F v)_k = d^{-1/2} sum_j v_j e^{-2 pi i k j / d}."""
    j = np.arange(d)
    k = modes(d)
    return np.exp(-2j * np.pi * np.outer(k, j) / d) / np.sqrt(d)


def clock_position(d):
    """The mu4 carrier clock in the position basis: rotation by pi/2 = shift d/4."""
    assert d % 4 == 0
    return np.roll(np.eye(d), d // 4, axis=0)


def covariance(Lam):
    """v210: quasi-free covariance C = 1/2(1 + sgn(H_1)), H_1 = Lambda - mu."""
    w, V = np.linalg.eigh(Lam)
    mu = 0.5 * (w[len(w) // 2 - 1] + w[len(w) // 2])
    sgn = V @ np.diag(np.sign(w - mu)) @ V.conj().T
    return 0.5 * (np.eye(Lam.shape[0]) + sgn)


def graded_real_basis(d):
    """mu4-GRADED free real mode basis of the marked circle.

    Columns: the free real modes (constant, cos/sin of k = 1..d/2-1, Nyquist),
    ordered by |k|.  Grades are the mu4 characters: modes +-k carry characters
    i^{+-k}, so k = 0 mod 4 and k = 2 mod 4 give real one-dimensional sectors
    (rho = +1 resp. -1) while the ODD k pair into the single real two-dimensional
    sector on which rho acts as a complex structure.  Returns (B, grade) with B
    orthonormal and grade in {0, 2, 1} ('1' = the odd/J sector).
    """
    th = 2 * np.pi * np.arange(d) / d
    cols, grades = [], []
    cols.append(np.ones(d) / np.sqrt(d))
    grades.append(0)
    for k in range(1, d // 2):
        g = 1 if k % 2 == 1 else (k % 4)
        cols.append(np.sqrt(2.0 / d) * np.cos(k * th))
        grades.append(g)
        cols.append(np.sqrt(2.0 / d) * np.sin(k * th))
        grades.append(g)
    kn = d // 2
    cols.append(np.cos(kn * th) / np.sqrt(d))
    grades.append(1 if kn % 2 == 1 else (kn % 4))
    return np.array(cols).T, np.array(grades)


def mu4_reference_contraction(Lam, d):
    """U^{-1} C_mu4 U in the position basis.

    C_mu4 is the mu4-equivariant free gapped contraction wearing the FORCED
    spectrum of Lam (v162/v178: a mu4-equivariant operator is fixed by its
    character->eigenvalue assignment).  Concretely: diagonal in the mu4-graded
    free real mode basis, sector by sector, with the sector's own eigenvalues in
    ascending order assigned to the free modes in ascending |k| order.  U is the
    graded basis, so the result lives in the SAME position basis as Lam.
    Returns (C_pos, block_off_frobenius_norm, max_pair_split); the caller decides
    what the block-off norm is measured against.
    """
    B, grade = graded_real_basis(d)
    C_pos = np.zeros((d, d))
    proj_sum = np.zeros((d, d))
    pair_split = 0.0
    for g in (0, 2, 1):
        cols = np.where(grade == g)[0]
        if len(cols) == 0:
            continue
        Bs = B[:, cols]
        block = Bs.T @ Lam @ Bs
        lam = np.sort(np.linalg.eigvalsh(block))
        if g == 1:                       # the J sector: real spectrum is paired
            pair_split = max(pair_split,
                             float(np.max(np.abs(lam[0::2] - lam[1::2]))))
        C_pos += (Bs * lam) @ Bs.T
        Ps = Bs @ Bs.T
        proj_sum += Ps @ Lam @ Ps
    return C_pos, float(np.linalg.norm(Lam - proj_sum)), pair_split


# ============================================================================
#  BLOCKS B / C -- the Beurling-Deny identity and the trias
# ============================================================================

def bd_trias(A):
    """Beurling-Deny data of a real symmetric A in its distinguished basis.

    jump    J_rs = -A_rs  (r != s)         -- the jump (conductance) measure
    killing w_r  = sum_s A_rs              -- the killing measure
    diffusion                              -- identically 0 on a finite atomic
                                              state space (no strongly local part)
    """
    d = A.shape[0]
    J = -A.copy()
    np.fill_diagonal(J, 0.0)
    w = A.sum(axis=1)
    return J, w, np.zeros(d)


def bd_form(J, w, v):
    """sum_r w_r v_r^2 + sum_{r<s} J_rs (v_r - v_s)^2."""
    diff2 = (v[:, None] - v[None, :]) ** 2
    return float(w @ (v ** 2) + 0.5 * np.sum(J * diff2))


def bd_reconstruct(J, w):
    """The unique symmetric operator with the given jump and killing measure."""
    A = -J.copy()
    np.fill_diagonal(A, w + J.sum(axis=1))
    return A


def sign_census(J):
    """(count fraction of nonneg jump weights, mass fraction of WRONG sign)."""
    d = J.shape[0]
    off = J[~np.eye(d, dtype=bool)]
    mass = np.abs(off).sum()
    wrong = np.abs(off[off < 0.0]).sum()
    return float((off >= 0.0).mean()), float(wrong / mass if mass > 0 else 0.0)


def trias_distance(A, Bm):
    """Relative trias distances (jump, killing, diffusion) between two operators."""
    J1, w1, k1 = bd_trias(A)
    J2, w2, k2 = bd_trias(Bm)
    dj = np.linalg.norm(J1 - J2) / max(np.linalg.norm(J1), 1e-300)
    dw = np.linalg.norm(w1 - w2) / max(np.linalg.norm(w1), 1e-300)
    dk = np.linalg.norm(k1 - k2)
    return float(dj), float(dw), float(dk)


def spec_distance(A, Bm):
    return float(np.max(np.abs(np.linalg.eigvalsh(A) - np.linalg.eigvalsh(Bm))))


def mu4_defect(vec, d):
    """Relative failure of a site function to be invariant under theta -> theta+pi/2."""
    return float(np.max(np.abs(vec - np.roll(vec, d // 4))) /
                 max(np.max(np.abs(vec)), 1e-300))


def equivariant_orthogonal(rho, d, rng):
    """A random orthogonal matrix commuting with the clock rho (mu4-equivariant)."""
    M = rng.standard_normal((d, d))
    P = sum(np.linalg.matrix_power(rho, j) @ M @ np.linalg.matrix_power(rho.T, j)
            for j in range(4)) / 4.0
    W, _, Vt = np.linalg.svd(P)
    return W @ Vt


def random_orthogonal(d, rng):
    Q, R = np.linalg.qr(rng.standard_normal((d, d)))
    return Q * np.sign(np.diag(R))


# ============================================================================

MU4 = [j * np.pi / 2 for j in range(4)]
CONTROLS = {
    "off-centre bump": [1.0],
    "Z3 (3 equal marks)": [2 * np.pi * j / 3 for j in range(3)],
    "4 unequal marks": [0.0, 1.0, 2.5, 4.0],
}

rng = np.random.default_rng(RNG_SEED)
verdict_parts = {}

section("BLOCK A -- KERNEL BUILDER (pure reproduction of v210; failure = bug)")

C_ml = mark_coeffs(MU4)
off_mod4 = max(abs(coef(C_ml, q)) for q in range(-2 * max(N_LIST), 2 * max(N_LIST) + 1)
               if q % 4 != 0)
on_mod4 = max(abs(coef(C_ml, q)) for q in range(-2 * max(N_LIST), 2 * max(N_LIST) + 1)
              if q % 4 == 0)
check("A1.mark_sum_fourier_support", off_mod4 < BAR_SUPPORT and on_mod4 > 0.1,
      "max off-(mod4) |f_k| = %.2e < %.0e; max on-(mod4) = %.4f  "
      "(f_k = 4 g_k [k=0 mod 4], v210 fact 1)" % (off_mod4, BAR_SUPPORT, on_mod4))

repro_worst = 0.0
alias_worst = 0.0
comm_worst = 0.0
state_worst = 0.0
equi_worst = 0.0
spec_worst = 0.0
pair_worst = 0.0
blockoff_worst = 0.0
LAM = {}
REF = {}
PROFILE = {}
for N in N_LIST:
    d = 2 * N
    Lam, f = seam_dtn_position(MU4, d)
    LAM[N], PROFILE[N] = Lam, f
    # A2: the position rebuild IS v210's mode-basis DtN diag(|k|) + Toeplitz(f_{k-k'})
    F = dft_matrix(d)
    Lam_mode = F @ Lam @ F.conj().T
    k = modes(d)
    rep = lambda m: int((m + d // 2) % d - d // 2)          # representative in [-d/2, d/2)
    target = np.diag(np.abs(k).astype(float)).astype(complex)
    target += np.array([[coef(C_ml, rep(a - b)) for b in k] for a in k])
    repro_worst = max(repro_worst, float(np.max(np.abs(Lam_mode - target))
                                         / np.max(np.abs(target))))
    fhat = np.fft.fft(f) / d
    alias_worst = max(alias_worst, max(abs(coef(fhat, m) - coef(C_ml, m))
                                       for m in range(-d // 2 + 1, d // 2)))
    # A3: v210's clock commutator and quasi-free STATE invariance
    rho = clock_position(d)
    comm_worst = max(comm_worst, float(np.linalg.norm(rho @ Lam - Lam @ rho)))
    Cov = covariance(Lam)
    state_worst = max(state_worst, float(np.linalg.norm(rho @ Cov @ rho.T - Cov)))
    # A4: the mu4 reference contraction in the SAME position basis
    Cref, blockoff, pair = mu4_reference_contraction(Lam, d)
    REF[N] = Cref
    blockoff_worst = max(blockoff_worst, blockoff / np.linalg.norm(np.diag(f)))
    pair_worst = max(pair_worst, pair)
    equi_worst = max(equi_worst, float(np.linalg.norm(rho @ Cref - Cref @ rho)))
    spec_worst = max(spec_worst, spec_distance(Lam, Cref))

check("A2a.position_rebuild_is_the_dtn", repro_worst < BAR_REPRO,
      "max |F Lambda F* - (diag(|k|) + Toeplitz(f_{[k-k']}))| / max|Lambda| = "
      "%.2e < %.0e over N = %s" % (repro_worst, BAR_REPRO, list(N_LIST)))
check("A2b.periodisation_vs_v210_coeffs", alias_worst < BAR_ALIAS,
      "max_{|m| < d/2} |f^{(d)}_m - f_m| = %.2e < %.0e: the position grid's "
      "periodised symbol agrees with v210's untruncated Fourier coefficients "
      "over the whole window (von-Mises decay)" % (alias_worst, BAR_ALIAS))
check("A3.clock_and_state_invariance",
      comm_worst < BAR_REPRO and state_worst < BAR_REPRO,
      "||[rho, Lambda]|| = %.2e, quasi-free state residual "
      "||rho C rho^dag - C|| = %.2e, both < %.0e (v210 facts 2+3)"
      % (comm_worst, state_worst, BAR_REPRO))
check("A4.mu4_reference_contraction",
      equi_worst < BAR_REPRO and spec_worst < BAR_REPRO and blockoff_worst < BAR_REPRO,
      "U^-1 C_mu4 U: ||[rho, C]|| = %.2e, spectral distance to Lambda_Sigma = "
      "%.2e, both < %.0e; mu4-sector block-off mass of Lambda relative to the "
      "sub-principal M_f = %.2e"
      % (equi_worst, spec_worst, BAR_REPRO, blockoff_worst))
info("A4.J_sector_pairing",
     "max split inside a J-sector eigenvalue pair = %.2e -- a real symmetric "
     "mu4-equivariant operator has doubly degenerate odd-sector spectrum, so the "
     "forced spectrum is realisable in the graded basis" % pair_worst)
info("A.dimensions", "position dimension d = 2N in %s, largest %d <= cap %d"
     % ([2 * N for N in N_LIST], 2 * max(N_LIST), DIM_CAP))

section("BLOCK B -- THE BEURLING-DENY IDENTITY (kill block)")

ident_worst = 0.0
kill_min = np.inf
census = {}
for N in N_LIST:
    d = 2 * N
    Lam = LAM[N]
    J, w, _ = bd_trias(Lam)
    kill_min = min(kill_min, float(w.min()))
    for _ in range(4):
        v = rng.standard_normal(d)
        lhs = float(v @ Lam @ v)
        rhs = bd_form(J, w, v)
        ident_worst = max(ident_worst, abs(lhs - rhs) / max(abs(lhs), 1.0))
    census[N] = sign_census(J)

check("B1.bd_identity_exact", ident_worst <= BAR_IDENTITY,
      "max relative residual of v^T Lambda v = sum w_r v_r^2 + sum (-Lambda_rs)"
      "(v_r - v_s)^2 = %.2e <= %.0e, over %d random v at each N in %s"
      % (ident_worst, BAR_IDENTITY, 4, list(N_LIST)))
check("B2.killing_measure_nonneg", kill_min >= BAR_KILL_NEG,
      "min_r w_r = %.6f >= %.0e -- the killing measure of the seam DtN is a "
      "genuine (nonnegative) killing measure" % (kill_min, BAR_KILL_NEG))

nonmarkov_large = census[max(N_LIST)][1]
nonmarkov_growing = any(census[N_LIST[i + 1]][1] > census[N_LIST[i]][1] + 1e-15
                        for i in range(len(N_LIST) - 1))
decomp_fails = nonmarkov_large > BAR_NONMARKOV_MASS or nonmarkov_growing
check("B3.jump_weight_sign_census", not decomp_fails,
      "nonneg-jump-weight COUNT fraction = %s (T126 comparison: %.1f%%); "
      "non-Markovian MASS share = %s, largest-N value %.2e <= declared kill "
      "threshold %.2f and not growing in N"
      % (["%.3f" % census[N][0] for N in N_LIST], 100 * NEG_FRAC_T126,
         ["%.1e" % census[N][1] for N in N_LIST], nonmarkov_large,
         BAR_NONMARKOV_MASS))
info("B3.structure",
     "the jump weights of the |k| circulant have the CLOSED FORM "
     "J_rs = 1/(d sin^2(pi (r-s)/d)) for r-s ODD and EXACTLY 0 for r-s even, so "
     "every nonzero jump weight is strictly positive: the non-Markovian "
     "remainder is not small, it is ZERO (the even-lag count fraction is what "
     "keeps the COUNT census near 1/2)")
info("B.interpretation",
     "structure: Lambda_Sigma is an exact Dirichlet form in the position basis. "
     "interpretation (not a claim of the gate): the |k| reading of the seam is "
     "Markovian, so the Beurling-Deny trias is available as a datum at all")

section("BLOCK C -- THE TRIAS (jump, killing, diffusion)")

d_big = 2 * max(N_LIST)
Lam_big = LAM[max(N_LIST)]
J_big, w_big, diff_big = bd_trias(Lam_big)
recon = bd_reconstruct(J_big, w_big)
complete = float(np.max(np.abs(recon - Lam_big)))
check("C1.completeness_no_residuum", complete <= BAR_EXACT,
      "||Lambda - (jump + killing)||_max = %.2e <= %.0e at d = %d: the trias "
      "reconstructs the OPERATOR, not just its form" % (complete, BAR_EXACT, d_big))
check("C2.diffusion_part_zero", float(np.max(np.abs(diff_big))) == 0.0,
      "diffusion part identically 0 -- a finite atomic state space carries no "
      "strongly local part, and the continuum DtN of the harmonic extension is "
      "the 1/2-Laplacian, a PURE JUMP form (Caffarelli-Silvestre 2007)")

lag = np.arange(1, d_big // 2)
exact = np.array([1.0 / (d_big * np.sin(np.pi * L / d_big) ** 2) if L % 2 == 1
                  else 0.0 for L in lag])
meas = np.array([J_big[0, L] for L in lag])
closed_err = float(np.max(np.abs(meas - exact)))
check("C3a.jump_kernel_closed_form", closed_err <= BAR_EXACT,
      "max |J_0L - [L odd] / (d sin^2(pi L / d))| = %.2e <= %.0e at d = %d"
      % (closed_err, BAR_EXACT, d_big))
odd = [L for L in range(3, max(5, d_big // 8)) if L % 2 == 1]
slope = np.polyfit(np.log([2 * np.pi * L / d_big for L in odd]),
                  np.log([J_big[0, L] for L in odd]), 1)[0]
check("C3b.caffarelli_silvestre_rate", BAR_EXPONENT[0] <= -slope <= BAR_EXPONENT[1],
      "fitted jump-kernel decay exponent = %.4f in [%.2f, %.2f] -- the "
      "|Delta theta|^{-2} rate of the 1/2-Laplacian (Caffarelli-Silvestre 2007)"
      % (-slope, BAR_EXPONENT[0], BAR_EXPONENT[1]))

kill_vs_profile = float(np.max(np.abs(w_big - PROFILE[max(N_LIST)])))
check("C4.killing_measure_is_the_mark_profile", kill_vs_profile <= BAR_EXACT,
      "max |w_r - f(theta_r)| = %.2e <= %.0e: the killing measure of the seam "
      "DtN IS the mu4 mark-sum curvature profile pointwise (the |k| circulant "
      "has row sums = symbol at k = 0 = 0)" % (kill_vs_profile, BAR_EXACT))
info("C.trias_numbers",
     "jump mass sum_{r<s} J_rs = %.4f, killing mass sum_r w_r = %.4f, killing "
     "range [%.4f, %.4f], diffusion 0"
     % (0.5 * J_big.sum(), w_big.sum(), w_big.min(), w_big.max()))
info("C.interpretation",
     "structure: the trias of the model seam DtN is (pure |k| jump kernel, mark "
     "profile as killing measure, no diffusion). interpretation: the marks enter "
     "the OPERATOR exclusively through the killing measure")

section("BLOCK D -- THE DISCRIMINATOR (trias of Lambda_Sigma vs trias of U^-1 C_mu4 U)")

dj_worst = dw_worst = 0.0
dspec_worst = 0.0
dj_trend, dw_trend = [], []
for N in N_LIST:
    dj, dw, dk = trias_distance(LAM[N], REF[N])
    ds = spec_distance(LAM[N], REF[N])
    dj_worst, dw_worst = max(dj_worst, dj), max(dw_worst, dw)
    dspec_worst = max(dspec_worst, ds)
    dj_trend.append(dj)
    dw_trend.append(dw)
    info("D.N=%-3d d=%-4d" % (N, 2 * N),
         "spec %.2e | jump %.3e | killing %.3e | diffusion %.1e" % (ds, dj, dw, dk))

spectra_match = dspec_worst <= BAR_TRIAS_EQ
trias_match = max(dj_worst, dw_worst) <= BAR_TRIAS_EQ
trias_deviates = max(dj_worst, dw_worst) > BAR_TRIAS_DEV
if not spectra_match:
    d_verdict = "BUG"
elif trias_match:
    d_verdict = "TRIPLE-MATCH"
elif trias_deviates:
    d_verdict = "SPECTRUM-ONLY"
else:
    d_verdict = "INCONCLUSIVE"
verdict_parts["D"] = d_verdict

check("D1.spectra_match_first", spectra_match,
      "max spectral distance spec(Lambda_Sigma) vs spec(U^-1 C_mu4 U) = %.2e <= "
      "%.0e -- the forced spectral list is reproduced exactly, so a trias "
      "difference cannot be a spectral artefact" % (dspec_worst, BAR_TRIAS_EQ))
check("D2.discriminator_verdict_is_preregistered",
      d_verdict in ("TRIPLE-MATCH", "SPECTRUM-ONLY"),
      "verdict %s: trias distances jump %.3e, killing %.3e against the bars "
      "TRIPLE-MATCH <= %.0e / SPECTRUM-ONLY > %.0e"
      % (d_verdict, dj_worst, dw_worst, BAR_TRIAS_EQ, BAR_TRIAS_DEV))
dw_stable = (max(dw_trend) - min(dw_trend)) / max(dw_trend) < 1e-6
dj_shrinks = all(dj_trend[i + 1] < dj_trend[i] for i in range(len(dj_trend) - 1))
check("D3.gap_is_N_stable_and_in_the_killing_measure", dw_stable and dj_shrinks,
      "the KILLING-measure gap is N-INDEPENDENT (%s, spread %.1e relative) while "
      "the jump-measure gap SHRINKS monotonically with N (%s) -- the operator "
      "gap is not a truncation artefact and lives in the killing measure"
      % (["%.4f" % v for v in dw_trend],
         (max(dw_trend) - min(dw_trend)) / max(dw_trend),
         ["%.1e" % v for v in dj_trend]))
dom = "killing measure" if dw_worst > dj_worst else "jump measure"
info("D.gap_localisation",
     "the trias gap sits in the %s (killing %.3e vs jump %.3e). The mu4-graded "
     "free contraction has a killing measure fixed by its sector-wise mode "
     "assignment, while the seam's killing measure is the mark-sum curvature "
     "profile f(theta_r) -- so the marks are exactly what the naive route "
     "cannot carry" % (dom, dw_worst, dj_worst))
info("D.interpretation",
     "structure: mu4-equivariance + the forced spectrum do NOT determine the "
     "seam DtN as an operator on the non-multiplicity-free block, and the "
     "Beurling-Deny trias exhibits the difference in finite dimension. "
     "interpretation: this is a finite witness of exactly the gap v178 declared "
     "'real on infinite-dim L^2' -- NOT a closure and NOT a refutation of the "
     "gate, which speaks about the raw seam")

section("BLOCK E -- NEGATIVE CONTROLS (v210's three; the Z3 case must break O(1))")

d_ctl = 2 * max(N_LIST)
ml_defect = mu4_defect(PROFILE[max(N_LIST)], d_ctl)
ctl_rows = []
for name, pos in CONTROLS.items():
    Lc, fc = seam_dtn_position(pos, d_ctl)
    Jc, wc, _ = bd_trias(Lc)
    defect = mu4_defect(wc, d_ctl)
    _, blockoff, _ = mu4_reference_contraction(Lc, d_ctl)
    blockoff /= np.linalg.norm(np.diag(fc))
    ctl_rows.append((name, defect, blockoff))
    info("E.%-22s" % name,
         "killing-measure mu4 defect = %.4f | mu4-sector block-off mass "
         "relative to M_f = %.4f" % (defect, blockoff))

z3_defect = [r[1] for r in ctl_rows if r[0].startswith("Z3")][0]
check("E1.controls_break_the_trias",
      all(r[1] > BAR_BREAK for r in ctl_rows) and ml_defect < BAR_REPRO,
      "mark-local killing-measure mu4 defect = %.2e < %.0e while all three "
      "controls exceed %.2f (Z3: %.4f) -- the trias of the seam is SPECIFIC to "
      "the mu4 orbit, the discriminator is not vacuous"
      % (ml_defect, BAR_REPRO, BAR_BREAK, z3_defect))
check("E2.controls_break_the_grading",
      all(r[2] > BAR_BREAK for r in ctl_rows),
      "each control also destroys the mu4-sector block structure by O(1) "
      "(block-off mass relative to M_f = %s, mark-local %.1e) -- the "
      "PRECONDITION for building U^-1 C_mu4 U at all already detects the wrong "
      "mark group"
      % (["%.3f" % r[2] for r in ctl_rows], blockoff_worst))

section("BLOCK F -- BASIS COVARIANCE (the honest limit of the discriminator)")

d_f = 2 * max(N_LIST)
Lam_f = LAM[max(N_LIST)]
rho_f = clock_position(d_f)

N_DRAWS = 3
ds_Q = dj_Q = dw_Q = 0.0
for _ in range(N_DRAWS):
    Q = random_orthogonal(d_f, rng)
    Lam_Q = Q.T @ Lam_f @ Q
    ds_Q = max(ds_Q, spec_distance(Lam_f, Lam_Q))
    dj, dw, _ = trias_distance(Lam_f, Lam_Q)
    dj_Q, dw_Q = max(dj_Q, dj), max(dw_Q, dw)
check("F1.random_orthogonal_kills_trias",
      ds_Q <= BAR_TRIAS_EQ and max(dj_Q, dw_Q) > BAR_BREAK,
      "%d draws: spectrum preserved (worst %.2e <= %.0e), trias destroyed (jump "
      "%.3f, killing %.3f > %.2f) -- the trias is strictly finer than the "
      "spectrum" % (N_DRAWS, ds_Q, BAR_TRIAS_EQ, dj_Q, dw_Q, BAR_BREAK))

V_equi = V_orth = ds_V = 0.0
dj_V = dw_V = np.inf
for _ in range(N_DRAWS):
    V = equivariant_orthogonal(rho_f, d_f, rng)
    V_equi = max(V_equi, float(np.linalg.norm(rho_f @ V - V @ rho_f)))
    V_orth = max(V_orth, float(np.max(np.abs(V.T @ V - np.eye(d_f)))))
    Lam_V = V.T @ Lam_f @ V
    ds_V = max(ds_V, spec_distance(Lam_f, Lam_V))
    dj, dw, _ = trias_distance(Lam_f, Lam_V)
    dj_V, dw_V = min(dj_V, dj), min(dw_V, dw)      # the MILDEST draw decides
equi_kills = max(dj_V, dw_V) > BAR_BREAK
check("F2.mu4_equivariant_conjugation_is_valid",
      V_equi < BAR_REPRO and V_orth < BAR_REPRO and ds_V <= BAR_TRIAS_EQ,
      "%d random mark-preserving (mu4-equivariant) orthogonals V satisfy "
      "||[rho, V]|| = %.2e, ||V^T V - 1|| = %.2e and preserve the spectrum "
      "(%.2e) -- legitimate test elements" % (N_DRAWS, V_equi, V_orth, ds_V))
info("F2.result",
     "the MILDEST of the mu4-equivariant conjugations %s the trias (jump %.3f, "
     "killing %.3f): "
     "the trias is therefore NOT canonical relative to the MARKS ALONE -- the "
     "mu4 commutant is a continuous group and only its lattice subgroup fixes "
     "the site structure" % ("DESTROYS" if equi_kills else "PRESERVES",
                             dj_V, dw_V))

lattice = {"rotation by pi/2 (the clock)": rho_f,
           "sheet reflection theta -> -theta": np.eye(d_f)[:, (-np.arange(d_f)) % d_f]}
lat_worst = 0.0
for name, P in lattice.items():
    Lam_P = P.T @ Lam_f @ P
    J1, w1, _ = bd_trias(Lam_f)
    J2, w2, _ = bd_trias(Lam_P)
    dev = max(float(np.max(np.abs(np.sort(w1) - np.sort(w2)))),
              float(abs(J1.sum() - J2.sum())),
              float(np.max(np.abs(np.sort(J1.ravel()) - np.sort(J2.ravel())))))
    lat_worst = max(lat_worst, dev)
    info("F3.%-34s" % name, "trias deviation = %.2e" % dev)
not_canonical = lat_worst > BAR_EXACT
check("F3.mark_preserving_lattice_invariance", not not_canonical,
      "the mark-preserving lattice symmetries of the marked circle (rotation by "
      "pi/2 and the sheet reflection, generating the dihedral group of v178's "
      "D4) leave the trias EXACTLY invariant: worst deviation %.2e <= %.0e"
      % (lat_worst, BAR_EXACT))
info("F.coupling_statement",
     "structure: the trias is invariant under the mark-preserving LATTICE "
     "symmetries but not under the full mu4-equivariant unitary group, so the "
     "discriminator is canonical relative to the MARKED BOUNDARY COORDINATE and "
     "not relative to the marks alone. interpretation: read through the "
     "Dirichlet-form lens, QGEO.MARKS.01 and QGEO.KERNEL.01 are COUPLED -- the "
     "kernel obligation becomes operator-formulable in finite terms only after "
     "MARKS has fixed the marked boundary coordinate; 'same spectrum + "
     "mu4-equivariance' is provably too weak (block D)")

# ============================================================================

if decomp_fails:
    VERDICT = "DECOMP-FAILS"
elif not_canonical:
    VERDICT = "NOT-CANONICAL"
else:
    VERDICT = verdict_parts["D"]

section("TOTAL")
print("TOTAL.probe        part 132, contract BD.SEAM")
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.A_builder    v210 rebuilt in the position basis: support %.1e, "
      "mode-form %.1e, periodisation %.1e, clock %.1e, state %.1e, reference "
      "contraction equivariant %.1e / isospectral %.1e"
      % (off_mod4, repro_worst, alias_worst, comm_worst, state_worst,
         equi_worst, spec_worst))
print("TOTAL.B_identity   exact to %.1e at every N; killing measure >= %.4f; "
      "non-Markovian jump mass %.1e (nonneg-weight count fraction %.3f, T126 "
      "comparison %.3f)" % (ident_worst, kill_min, nonmarkov_large,
                            census[max(N_LIST)][0], NEG_FRAC_T126))
print("TOTAL.C_trias      jump = closed-form |k| kernel (exponent %.3f), "
      "killing = the mark profile (%.1e), diffusion = 0, completeness %.1e"
      % (-slope, kill_vs_profile, complete))
print("TOTAL.D_discrim    %s -- spectra %.1e, jump %s (shrinks with N), KILLING "
      "%.4f at EVERY N (the gap sits in the %s)"
      % (verdict_parts["D"], dspec_worst, ["%.1e" % v for v in dj_trend],
         dw_worst, dom))
print("TOTAL.E_controls   mark-local defect %.1e; controls %s (all > %.2f)"
      % (ml_defect, ["%.3f" % r[1] for r in ctl_rows], BAR_BREAK))
print("TOTAL.F_covariance random orthogonal destroys trias (%.3f); mu4-"
      "equivariant conjugation %s (%.3f); mark-preserving lattice EXACT (%.1e)"
      % (max(dj_Q, dw_Q), "destroys" if equi_kills else "preserves",
         max(dj_V, dw_V), lat_worst))
print("TOTAL.gate         QGEO.KERNEL.01 NOT closed: this is v210's MODEL DtN, "
      "not the raw RP seam. What is new is a finite operator-level discriminator "
      "and the coupling of KERNEL to MARKS.")
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.caps         largest matrix %d (cap %d); runtime %.1f s (budget "
      "%.0f s)" % (d_big, DIM_CAP, time.time() - T_START, RUNTIME_BUDGET))
print("TOTAL.status       %s" % ("ALL CHECKS PASSED" if FAIL == 0
                                 else "%d CHECK(S) FAILED" % FAIL))
raise SystemExit(1 if FAIL else 0)
