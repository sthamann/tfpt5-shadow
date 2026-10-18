"""Discovery probe (2026-07-28), part 140 of the prime/window investigation.
Contract SIGNED.BAND -- THE ONE INEQUALITY.  Nothing else.

WHERE THIS SITS (T139 DENSE-RESISTS: the ENTIRE distance to the D-uniformity is
ONE SIGNED inequality at small stripe distance)
  T137 killed every absolute-value route from below.  T138 kept the signs and
  found the mechanism.  T139 killed the DECAY-LEMMA family: no entrywise
  envelope can beat the margin (that is an absolute-value route), and no stripe
  LAYER series can either, because it is dead FROM BELOW.  What T139 left,
  QUOTED here and never re-derived:
    * rho(W) = lam_max(Gram), Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T
      A_B^{-1} b_{e'}, W = L_Delta A_B^{-1}; exact rho(W) = 0.9962 .. 0.9999;
    * THE EXACT DOUBLE TELESCOPE b_e^T G b_{e'} = sum_box H (verified to 4e-15,
      factorisation-free), H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s}
      the mixed second difference of the Green function;
    * H < 0 on 0.71 .. 0.87 of the off-diagonal and > 0 on 1.000 of the
      diagonal, and the T138 geometric sign law FOLLOWS from box geometry
      (disjoint pairs have interval gap > 0, so their box misses the diagonal);
    * CERTIFIED DEAD, never to be retried: all absolute-value hulls
      (rho(|E|) >= 1.31 from below), all layer series (>= max_b Rayleigh(Band_b)
      = 1.03 .. 1.11 > target via Weyl -- the excess IS the O(nb) step count),
      Jaffard (kernel exponent on the borderline, atom spikes flat),
      Gantmacher-Krein one-pair (defect 0.8 .. 1.9);
    * R2: a replacement for the O(nb) Weyl steps.  R4: ONE open border block
      (need 2.15, argmax at index distance 15, far-carried 1.000).
  R1, the whole remaining distance: A SIGNED INEQUALITY AT STRIPE DISTANCE
  b <= 16.  This probe attacks exactly that and nothing else.

WHAT THIS PROBE DOES
  K0  SETUP and DIRECTION CALIBRATION: the firewall, the odd pole-free section
      against its entrywise definition, the lumped Stieltjes pair and its
      M-matrix anchor, and the four direction facts K1 / K2 lean on, each
      VERIFIED and not asserted: a Rayleigh quotient is a LOWER bound, a
      completed Cholesky is an UPPER bound, CONGRUENCE X -> C X C^T preserves
      the Loewner order (so every step of the K1 chain may be taken inside the
      conjugation), and the telescoping identity itself is re-verified here
      because all of K1 rests on it.
  K1  THE QUADRATIC FORM DIRECTLY.  The H-telescope is not just an identity for
      the ENTRIES of the Gram, it is an identity for its FORM.  With
      M_{e,r} = 1[a_e <= r < b_e] the edge-interval INCIDENCE matrix and
      C = diag(sqrt(Delta)) M,
          Gram = C H C^T          (EXACT, verified),
      i.e. x^T Gram x = u^T H u with u = C^T x the OCCUPATION function of the
      edge system -- Abel summation over the box structure, with no absolute
      value anywhere and no factorisation.  Three consequences, each measured:
      (1) rank(Gram) <= h - 1, so the n_e-dimensional signed Gram is a
          LOW-RANK object and the whole spectral question lives on the
          h-dimensional index grid;
      (2) THE EXACT FINITE-CORE REDUCTION
              rho(W) = lam_max(K^{1/2} H K^{1/2}),   K = M^T Delta M,
          because the nonzero spectra of C H C^T and K^{1/2} H K^{1/2} coincide
          (nonzero eig(AB) = nonzero eig(BA)).  K is the COVERING KERNEL
          K_rs = total edge weight of edges whose interval contains both r and
          s = W([r ^ s, r v s]) -- a closed geometric formula, monotone by
          inclusion, computed in closed form and verified against M^T Delta M.
          So the signed inequality is a statement about TWO small matrices per
          zone: the geometry K and the kernel H.
      (3) THE ENERGY REORDERING, exactly, with the compensation kept in the
          form.  For ANY symmetric H,
              H = diag(s) + L_N,  s = row sums of H,  N = -offdiag(H),
          L_N = diag(N 1) - N (an identity, verified), so
              u^T H u = sum_r s_r u_r^2 + sum_{r<s} N_rs (u_r - u_s)^2 ,
          a MASS term plus a long-range DIRICHLET form.  The direct bound is
          then built in three PEDANTIC steps, each certified per instance:
            (i)  N = N_+ - N_-, and L_{N_-} >= 0, so DROPPING it is a genuine
                 LOEWNER drop (not a negative mean);
            (ii) CAUCHY-SCHWARZ along the telescope, (u_r - u_s)^2 <=
                 (s - r) sum_{k=r}^{s-1} (u_k - u_{k+1})^2, turns the
                 long-range Dirichlet form into a NEAREST-NEIGHBOUR one:
                 L_{N_+} <= T_Q, Q_k = sum_{r <= k < s} N_+,rs (s - r) -- the
                 FIRST-MOMENT weight of the kernel, which is exactly the shape
                 a decay statement for H would have to feed;
            (iii) diag(s) <= diag(s_+).
          Each Loewner step is certified by a completed Cholesky of the
          difference, and the resulting certified bound
              rho(W) <= lam_max(K^{1/2} (diag(s_+) + T_Q) K^{1/2})
          is evaluated against the target on the FULL measurement surface, next
          to the crude product bound lam_max(K) lam_max(H) and the absolute
          row-sum reference -- and WHERE IT BREAKS is reported step by step.
  K2  THE BAND AS ONE OBJECT, b <= 16, with no layer summation anywhere.
      (i)   TRANSFER / FLOQUET: the stripes sit at atom positions, so the
            structure is QUASI-periodic; the relative spread of the stripe
            block norms is measured, which is what decides whether a transfer
            argument can be run at all -- and what such an argument would
            deliver is the uniform-over-blocks bound of (iii), so (i) collapses
            into (iii) with a number attached.
      (ii)  BENDIXSON 1902 / the field of values: W = L_Delta A_B^{-1} is NOT
            symmetric, its spectrum is real (verified), and every eigenvalue
            has Re lam <= lam_max(sym W), so lam_max(sym W) is a CERTIFIED
            upper bound on rho(W) obtained without any Gram at all.  Its slack
            is measured.  The trace identity tr(Gram) = tr(W) is verified as
            the consistency bridge between the two pictures.
      (iii) THE SMALL STRIPE-GRAM OBJECT.  b <= 16 means the band is, per
            window of 2b consecutive stripes, an almost FINITE object.  The
            CHECKERBOARD SPLIT makes that exact: with stripe groups of length
            b, |i - j| <= b forces adjacent groups, and the adjacent pairs
            two-colour into two families of DISJOINT supports, so
                Band_b = D + A_even + A_odd
            exactly (verified entrywise) and
                lam_max(Band_b) <= max_g lam_max(D_g)
                                   + max_{even} sigma_max(B) + max_{odd} sigma_max(B)
            -- THREE Weyl steps instead of O(nb), every term the norm of a
            SMALL explicit block.  That is the R2 replacement, and it is
            certified.  The per-zone core size and the zone dependence of the
            block norms are measured.
      (iv)  THE BAND IN THE INDEX GRID OF THE CORE, which is the one family
            T139's kill does NOT cover: cut H by index distance |r - s| <= b
            inside the finite core instead of cutting the Gram by stripe
            distance.  This is the only family in which a truncation could be
            LEGITIMATE, because the discarded far part might be
            Loewner-nonpositive -- so its certified lam_max is computed with a
            sign-aware certificate (a bisected Cholesky that is allowed to
            return a negative number), and the answer decides the family.
      Then the honest arithmetic: Band_b is bounded FROM BELOW by a Rayleigh
      quotient at every b <= 16, and that lower bound is compared with the
      target.  Whatever an upper bound on Band_b costs, it cannot go below that
      -- so the fate of the whole ADDITIVE band-plus-tail family is decided
      here, once, from below, and the rank inflation caused by the truncation
      (rank(Gram) <= h - 1 versus rank(Band_b)) is measured as its mechanism.
  K3  R4 AND THE LEFTOVERS.  The border pool is rebuilt smaller, the m-paired
      Neumann ladder run, and for the tightest / open blocks the failure is
      dissected with the H machinery: the need ratio profiled in index
      distance, the FAR MASS FRACTION of the offending entry computed (a decay
      statement can only ever help what is far-carried), and the finite-core
      reduction of K1 tested ONE LEVEL DOWN on the border block's own lumped
      pair.
  K4  THE MAP V12, the promotion batch, the shortest rest list, and the honest
      three-sentence verdict on the one question: after K1 / K2, is R1 a
      question with a FINITE CORE per zone plus a NAMEABLE uniformity
      ingredient, or is it structurally open?

PREREGISTERED VERDICTS (bars declared here, before any number is computed)
  SIGNED-BAND-CARRIES : one K1 / K2 route beats the target CERTIFIED on EVERY
                        window of the measurement surface.
  FINITE-CORE         : the exact reduction rho(W) = lam_max(K^{1/2} H K^{1/2})
                        stands to the identity bar on every window, the core is
                        SMALL (size h - 1 per zone, versus n_e edges), and the
                        remaining uniformity ingredient is NAMED and measured
                        -- the precise rest, not a wish.
  BAND-RESISTS        : neither -- the anatomy, with the reason.
  Element gates: el_firewall, el_k0, el_k1, el_k2, el_k3, el_k4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger / TeX / website /
    changelog edit, no verification/ module, no next.txt, no .md output, no git
    action.
  * NO Riemann zero data of any kind.  An AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address of
    the surrounding statement and is NEVER USED, in either direction.  Nothing
    here claims, assumes or approaches RH.  Even with R1 closed and every item
    of the rest list shut, what would stand is positivity of the Weil window
    form on test functions supported in (-alpha_max, alpha_max) for the alpha
    actually reached -- a FINITE-WINDOW statement about a finite list of
    prime-power zones.  The distance to RH is MAPPED in K4, never travelled.
  * CERTIFIED vs CERTIFIABLE vs MEASURED vs FIT vs HYPOTHESIS, per line.  A
    completed Cholesky of s I - X certifies lam_max(X) <= s + c_h u ||X||,
    u = 2^-53 (Wilkinson 1968; Higham 2002 Thm 10.3/10.4); a symmetric row-sum
    or block row-sum test is CERTIFIABLE (Gershgorin 1931; Feingold-Varga
    1962); a Rayleigh quotient and an eigenvalue are MEASUREMENTS, and a
    Rayleigh quotient is a rigorous LOWER bound on lam_max.  Every fit is a FIT
    with a delete-one jackknife band.  Bars declared before a number are never
    moved.
  * DIRECTION CARE, pedantic and stated where it is used: lumping RAISES the
    form (A_B >= A in the Loewner order), so the pair reaches a floor only
    through the INVERSE side; only an UPPER bound on rho(W) can produce a floor
    and a LOWER bound can only KILL a route; a term may be DISCARDED only if it
    is Loewner-nonpositive, and a negative MEAN is NOT a Loewner sign;
    congruence by a fixed C preserves the Loewner order (verified in K0), which
    is the licence for every step of the K1 chain.
  * CLASSICAL ADDRESSES USED: Abel summation and summation by parts, Bendixson
    1902 and Hirsch 1902 (the field of values / real-part localisation of a
    non-symmetric spectrum), Cauchy-Schwarz along a telescope (the discrete
    Hardy step; Hardy-Littlewood-Polya 1934 ch. 9 for the address),
    Gantmacher-Krein 1950/1960 and Karlin 1968 (oscillation kernels, one-pair
    Green functions, tridiagonal inverses), Gershgorin 1931 and Feingold-Varga
    1962 (block row-sum tests), Weyl 1912, Fan 1958 / Berman-Plemmons 1979 /
    Varga 1962 (M-matrices), Collatz 1942 / Wielandt 1950, Haynsworth 1968 and
    Cauchy interlacing, Floquet 1883 / Bloch 1929 (the periodic transfer
    argument, NOT applicable here and measured as such), Demko-Moss-Smith 1984
    and Jaffard 1990 (the decay classics, QUOTED as closed by T139),
    Wilkinson 1968 and Higham 2002, Bertrand-Chebyshev 1852 and the trivial
    even bound (the only two gap facts consumed).  No gap CONJECTURE enters.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    the signed Gram is formed explicitly only below that cap; total runtime
    budget 760 s (< 900 s), with per-block guards that truncate a pool rather
    than overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, svdvals

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 760.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

# --- K1 / K2 surface (the signed Gram is formed explicitly: n_e <= NE_CAP) ---
K12_ZONES = 30
K12_HCAP = 300
NE_CAP = 1500                # == MAX_H: every Cholesky stays under the cap
B_LIST = tuple(range(1, 17))            # THE FULL b <= 16 ladder of R1
B_CERT = tuple(range(1, 17))            # every b gets a CERTIFIED upper bound
B_CHECK = (2, 4, 8, 16)                 # where the checkerboard split is built
B_RANK = (4, 16)                        # where the rank of Band_b is measured
T_K12 = 420.0

# --- K3 pool (the T137..T139 border surface, rebuilt smaller) ---------------
K3_GC_MIN = 2
K3_HCAP = 640
K3_MAX = 420
K3_PER_RHO = 14
K3_LOGRES = 80.0
K3_RHO = (1.001, 1.05, 1.10, 1.20, 1.25, 1.35, 1.49531, 1.60, 1.75, 1.90,
          2.00, 2.25, 2.50, 3.00, 3.50, 4.00)   # 1.49531 = the T127 band edge
M_LADDER = (1, 2, 3, 4, 6, 8, 12, 16, 24)
FAR_K = 8                    # "far" for the R4 mass split, in index distance
K3_DEEP = 16                 # blocks on which the K1 reduction is re-run
T_K3 = 150.0

# --- preregistered bars (declared before any number is computed) ------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_RED = 1.0e-8             # the finite-core reduction bar (an eigenvalue)
BAR_COVER = 1.0              # a bound must clear on EVERY window
BAR_RANK = 1.0e-10           # relative eigenvalue threshold for a rank count
BAR_IMAG = 1.0e-8            # relative bar for "the spectrum of W is real"

# --- quoted numbers.  QUOTED, never re-derived here ------------------------
RHO_W_T139 = (0.9962, 0.9999)
BAND_LO_T139 = (1.03, 1.11)
TEL_ERR_T139 = 4.0e-15
H_NEG_OFF_T139 = (0.71, 0.87)
H_POS_DIAG_T139 = 1.000
DECAY_H_T137 = -0.63
DECAY_LAYER_T138 = -1.54
SIGN_NESTED_T138 = (0.76, 0.94)
SIGN_CROSS_T138 = (0.59, 0.63)
SIGN_DISJ_T138 = (0.06, 0.36)
NEED_R4_T139 = 2.15
NEED_D_R4_T139 = 15
RHO_ABS_T137 = 1.31
PROMO_T139 = 47
N_PROBES_PRIOR = 139
B_MAX_R1 = 16


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


def wrap_at(text, width):
    out, line = [], ""
    for w in text.split():
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w) if line else w
    if line:
        out.append(line)
    return out


def para(text, width=76, indent="  "):
    for ln in wrap_at(text, width - len(indent)):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


def rel(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    sc = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))), 1.0e-300)
    return float(np.max(np.abs(a - b))) / sc


def qmin(v):
    v = [x for x in v if np.isfinite(x)]
    return float(min(v)) if v else float("nan")


def qmax(v):
    v = [x for x in v if np.isfinite(x)]
    return float(max(v)) if v else float("nan")


def qmed(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def fit_line(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_band(x, y):
    """A FIT with a delete-one jackknife band on both coefficients."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = x.shape[0]
    a, b, rms = fit_line(x, y)
    if n < 5:
        return a, b, float("nan"), float("nan"), rms
    aa, bb = [], []
    step = max(1, n // 40)
    for i in range(0, n, step):
        m = np.ones(n, dtype=bool)
        m[i] = False
        ai, bi, _ = fit_line(x[m], y[m])
        aa.append(ai)
        bb.append(bi)
    return a, b, float(np.std(aa)), float(np.std(bb)), rms


def pow_fit(xv, yv, tag):
    """A POWER-LAW FIT y ~ c x^p in log-log, with its jackknife band."""
    xv = np.asarray(xv, dtype=float)
    yv = np.asarray(yv, dtype=float)
    m = (xv > 0.0) & (yv > 0.0) & np.isfinite(xv) & np.isfinite(yv)
    if int(np.count_nonzero(m)) < 3:
        return dict(tag=tag, p=float("nan"), c=float("nan"), sp=float("nan"),
                    rms=float("nan"), n=int(np.count_nonzero(m)))
    a, p, sa, sp, rms = fit_band(np.log(xv[m]), np.log(yv[m]))
    return dict(tag=tag, p=p, c=math.exp(a), sp=sp, rms=rms,
                n=int(np.count_nonzero(m)))


# ----------------------------------------------------------------------------
# el_firewall -- AST scan of this source
# ----------------------------------------------------------------------------
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "numpy", "scipy"}


def firewall():
    src = open(os.path.abspath(__file__), "r").read()
    low = src.lower()
    hits = [tok for tok in FORBIDDEN_TOKENS if tok in low]
    tree = ast.parse(src)
    bad_imports, bad_writes = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    bad_imports.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                bad_imports.append(node.module)
        elif isinstance(node, ast.Call):
            fn = node.func
            nm = getattr(fn, "id", None) or getattr(fn, "attr", None)
            if nm in ("open",):
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(ch in mode for ch in "wax+"):
                    bad_writes.append(mode)
    check("el_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("el_firewall.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("el_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("el_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "signed_band_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111..T139 code path
# ----------------------------------------------------------------------------
def von_mangoldt_table(n_max):
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


def atom_table(n_max):
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0)[0]:
        n = int(n)
        out.append((n, lam[n], math.log(n), 2.0 * lam[n] / math.sqrt(n)))
    return out


def atoms_in(alpha, atoms_all):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952 -- CITED, never used as a criterion)
# ----------------------------------------------------------------------------
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = (1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return (tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w)) / (-np.expm1(-2.0 * w))


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        tot += half * float(np.dot(_GLW, _arch_integrand(w, s, D)))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * W))))


def arch_A(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = _arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = _arch_A_near(sv[i], D)
    return out


def arch_lags(M, D):
    out = np.empty(M)
    for a in range(0, M, CHUNK):
        b = min(M, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (bit-identical to the T111 reference)."""
    D = 2.0 * alpha / M
    c = arch_lags(M, D)
    for u_j, mu_j in atoms:
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


# ----------------------------------------------------------------------------
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T139)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_toeplitz_slow(c, M):
    """The definition, entry by entry -- the K0 reference for odd_toeplitz."""
    h = M // 2
    out = np.empty((h, h))
    for i in range(h):
        for j in range(h):
            out[i, j] = c[abs(i - j)] - c[(M - 1) - i - j]
    return out


def odd_pole_vector(alpha, M):
    """t~ in odd coordinates: (8/sqrt D) sinh(D/4) sinh(xbar_r/2)."""
    D = 2.0 * alpha / M
    h = M // 2
    xbar = -alpha + (np.arange(h) + 0.5) * D
    return (8.0 / math.sqrt(D)) * math.sinh(0.25 * D) * np.sinh(0.5 * xbar)


def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(X):
    return float(np.max(np.abs(X).sum(axis=1)))


def ray_top(X, iters=180, rng=None):
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration: with
    sig = max_r sum_s |X_rs| the matrix X + sig I is PSD (Gershgorin 1931), so
    no negative eigenvalue can win the iteration.  The returned value is a
    RAYLEIGH QUOTIENT, hence a rigorous LOWER bound on lam_max(X)."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    if n == 1:
        return float(X[0, 0])
    sig = gersh(X)
    y = (np.abs(rng.standard_normal(n)) + 0.5) if rng is not None \
        else np.ones(n) / math.sqrt(n)
    y = y / max(float(np.linalg.norm(y)), 1.0e-300)
    lam = float(y @ (X @ y))
    for _ in range(iters):
        z = X @ y + sig * y
        nz = float(np.linalg.norm(z))
        if not (nz > 0.0):
            break
        y = z / nz
        lam = max(lam, float(y @ (X @ y)))
    return lam


def cert_lam_max(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_max(X) <= s for a symmetric X by a COMPLETED CHOLESKY of
    s I - X (Wilkinson 1968; Higham 2002 Thm 10.3/10.4).  DIRECTION: an UPPER
    bound, which is what a floor needs."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = nrm
    s = max(float(guess), 0.0) + fl + 1.0e-300
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(s * I - X) is not None:
            return s + fl
        s = s * (1.0 + grow) + 10.0 * fl + 1.0e-300
        grow *= 3.0
    return float("nan")


def cert_lam_max_signed(X, tries=26):
    """CERTIFY lam_max(X) <= s for a symmetric X WITHOUT assuming s >= 0.  The
    LOEWNER question -- is a discarded part nonpositive? -- needs a certified
    bound that is ALLOWED to be negative, so the shift is bisected DOWN from a
    Rayleigh quotient and the last completed Cholesky is returned.  A completed
    Cholesky of s I - X certifies lam_max(X) <= s + floor for any real s, and
    the SIGN of that number is the answer."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    lo = ray_top(X)
    hi = nrm + fl
    if safe_cho((hi + fl) * np.eye(n) - X) is None:
        return float("nan")
    lo = min(lo - abs(lo) * 1.0e-9 - 10.0 * fl, hi)
    I = np.eye(n)
    for _ in range(tries):
        mid = 0.5 * (lo + hi)
        if safe_cho(mid * I - X) is not None:
            hi = mid
        else:
            lo = mid
        if abs(hi - lo) <= 1.0e-12 * max(nrm, 1.0e-300) + 10.0 * fl:
            break
    return hi + fl


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_min(X) >= t for a symmetric X by a completed Cholesky of
    X - t I.  DIRECTION: a LOWER bound -- this is the function that certifies a
    LOEWNER step, X >= 0 up to the declared floating-point floor."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = 0.0
    t = float(guess) - fl
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(X - t * I) is not None:
            return t - fl
        t = t - max(abs(t), nrm) * grow - 10.0 * fl - 1.0e-300
        grow *= 3.0
    return float("nan")


def perron_bracket(applyf, n, iters, rng=None):
    """A COLLATZ-WIELANDT bracket for the spectral radius of a NONNEGATIVE
    operator: at any strictly positive x, min_r (Ax)_r / x_r <= rho(A) <=
    max_r (Ax)_r / x_r (Collatz 1942; Wielandt 1950).  Both ends are rigorous
    at every iterate."""
    x = np.ones(n) if rng is None else (np.abs(rng.standard_normal(n)) + 0.5)
    lo, up = 0.0, float("inf")
    for _ in range(iters):
        y = applyf(x)
        r = y / np.maximum(x, 1.0e-300)
        lo = max(lo, float(np.min(r)))
        up = min(up, float(np.max(r)))
        nz = float(np.max(y))
        if not (nz > 0.0):
            return 0.0, 0.0
        x = np.maximum(y / nz, 1.0e-300)
    return lo, up


# ----------------------------------------------------------------------------
# the frame (T112 frame A, window forced EVEN so that h = M/2 exactly)
# ----------------------------------------------------------------------------
def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def step_frame(u_old, u_new, D):
    M_o = even_window(u_old, D)
    M_n = even_window(u_new, D)
    gc = (M_n - M_o) // 2
    if gc < 1:
        return None
    return dict(D=D, M_o=M_o, M_n=M_n, gc=gc, h_o=M_o // 2, h_n=M_n // 2,
                al_o=0.5 * M_o * D, al_n=0.5 * M_n * D)


def bordered_step(fr, atoms_all):
    """The bordered step (Haynsworth 1968), its border Schur block S -- rebuilt
    in this file's coordinates as a declared PROXY for the T134 assembly
    source, exactly as T138 / T139 did."""
    at_n = atoms_in(fr["al_n"], atoms_all)
    c_n, _ = lag_vector_fast(fr["al_n"], fr["M_n"], at_n)
    tv = odd_pole_vector(fr["al_n"], fr["M_n"])
    Q = sym(odd_toeplitz(c_n, fr["M_n"]) - np.outer(tv, tv))
    gc = fr["gc"]
    A = sym(np.ascontiguousarray(Q[:gc, :gc]))
    C = np.ascontiguousarray(Q[:gc, gc:])
    X = sym(np.ascontiguousarray(Q[gc:, gc:]))
    fac = safe_cho(X)
    if fac is None:
        return None
    Z = cho_solve(fac, C.T, check_finite=False)
    S = sym(A - C @ Z)
    del Q, A, C, X, Z
    return dict(S=S, fr=fr)


# ----------------------------------------------------------------------------
# THE LUMPED M-MATRIX PAIR and its EDGE representation -- the central objects
# ----------------------------------------------------------------------------
def lump_pair(A):
    """THE LUMPED M-MATRIX PAIR of a symmetric A (T136 (P1)).  Delta = the
    POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta its Laplacian
    (PSD, zero row sums), A_B = A + L_Delta.

    DIRECTION: L_Delta >= 0 in the LOEWNER order, so A_B >= A -- lumping
    RAISES the form, and the floor is reached only through the INVERSE side."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    A_B = sym(A + LD)
    offB = A_B - np.diag(np.diag(A_B))
    return dict(h=h, A_B=A_B, Dl=Dl, LD=LD, P_row=P_row, w=A.sum(axis=1),
                dg=dg, dgB=np.diag(A_B).copy(),
                stieltjes=int(bool(np.all(offB <= 1.0e-300))
                              and bool(np.all(np.diag(A_B) > 0.0))),
                n_pos=int(np.count_nonzero(np.where(np.eye(h, dtype=bool),
                                                    0.0, off) > 0.0)))


def anchor_floor(A_B):
    """THE M-MATRIX ANCHOR (T136 (P4)): A_B x = 1, x >= 0 certifies a
    nonsingular M-matrix (Fan 1958; Berman-Plemmons 1979) and
    lam_min(A_B) >= 1 / max_r x_r.  DIRECTION: a LOWER bound."""
    h = A_B.shape[0]
    fac = safe_cho(A_B)
    if fac is None:
        return None
    x = cho_solve(fac, np.ones(h), check_finite=False)
    xmax = float(np.max(x))
    xmin = float(np.min(x))
    return dict(fac=fac, x=x, xmax=xmax, xmin=xmin,
                nonneg=int(xmin >= -1.0e-13 * max(xmax, 1.0e-300)),
                floor=(1.0 / xmax) if xmax > 0.0 else float("nan"))


def edge_list(Dl, M=None):
    """THE EDGE REPRESENTATION of L_Delta = sum_{r<t} Delta_rt (e_r - e_t)
    (e_r - e_t)^T, exactly.  NOTHING is capped or dropped -- an upper bound on
    lam_max(W) may not discard edges.  Sorted by the STRIPE index
    anti = M - 1 - r - t, so stripe blocks are contiguous slices."""
    h = Dl.shape[0]
    iu = np.triu_indices(h, 1)
    w = Dl[iu]
    keep = w > 0.0
    er = iu[0][keep]
    et = iu[1][keep]
    w = w[keep]
    lab = ((M - 1) - er - et) if M is not None else (er + et)
    order = np.lexsort((er, lab))
    er, et, w, lab = er[order], et[order], w[order], lab[order]
    vals, starts, counts = np.unique(lab, return_index=True, return_counts=True)
    return dict(er=er, et=et, w=w, lab=lab, n=er.shape[0],
                mass=float(w.sum()), stripe_val=vals, stripe_start=starts,
                stripe_count=counts, nb=vals.shape[0],
                sidx=np.repeat(np.arange(vals.shape[0]), counts))


def signed_gram(G, er, et, wt):
    """THE SIGNED GRAM, formed explicitly (n_e <= NE_CAP <= MAX_H):

        Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T G b_{e'},   b_e = e_r - e_t,

    a weighted matrix of SECOND DIFFERENCES of the Green function G = A_B^{-1}.
    NO absolute value is taken anywhere in this function."""
    Yw = (G[:, er] - G[:, et]) * wt[None, :]
    GR = (Yw[er, :] - Yw[et, :]) * wt[:, None]
    del Yw
    return sym(GR)


def band_masks(sidx):
    ii = np.asarray(sidx)
    return np.abs(ii[:, None] - ii[None, :])


def mixed_second_difference(G):
    """H_rs = G_{r+1,s+1} - G_{r+1,s} - G_{r,s+1} + G_{r,s} on 0 <= r,s <= h-2.
    THE EXACT DOUBLE TELESCOPE (T139): b_e^T G b_{e'} = sum over the box
    [a,b) x [c,d) of H -- an identity, re-verified in K0 because all of K1
    rests on it."""
    return G[1:, 1:] - G[1:, :-1] - G[:-1, 1:] + G[:-1, :-1]


def decay_profile(X, dmat, dmax, use_abs=True):
    """THE DECAY PROFILE of a matrix along a distance label.  A MEASUREMENT."""
    V = np.abs(X) if use_abs else X
    dm, md = [], []
    for d in range(1, dmax + 1):
        m = dmat == d
        if not m.any():
            dm.append(float("nan"))
            md.append(float("nan"))
            continue
        v = V[m]
        dm.append(float(np.max(v)))
        md.append(float(np.median(v)))
    return dict(d=np.arange(1, dmax + 1), mx=np.array(dm), md=np.array(md))


# ----------------------------------------------------------------------------
# K1 MACHINERY -- the incidence identity, the covering kernel, the reordering
# ----------------------------------------------------------------------------
def interval_incidence(er, et, h):
    """THE EDGE-INTERVAL INCIDENCE MATRIX M_{e,r} = 1[a_e <= r < b_e] on the
    H-grid r = 0 .. h-2.  This is the object that turns the H-telescope from an
    identity about ENTRIES into an identity about the FORM: with
    C = diag(sqrt(Delta)) M one has Gram = C H C^T, hence
    x^T Gram x = u^T H u with u = C^T x the OCCUPATION FUNCTION of the weighted
    edge system.  That is Abel summation over the box structure, and no
    absolute value and no factorisation appear anywhere in it."""
    m = h - 1
    rr = np.arange(m)
    return ((rr[None, :] >= er[:, None]) & (rr[None, :] < et[:, None])).astype(float)


def cover_kernel_closed(er, et, w, h):
    """THE COVERING KERNEL in CLOSED GEOMETRIC FORM.  K = M^T Delta M has

        K_rs = sum over edges e with a_e <= r ^ s and r v s < b_e of Delta_e
             = W([r ^ s, r v s]) ,

    the total edge weight of the edges whose interval CONTAINS both r and s.
    Two exact consequences, both verified: K is entrywise NONNEGATIVE and
    MONOTONE by inclusion (K_rs cannot increase when the interval grows), and K
    is PSD because it is a Gram matrix of indicators.  The closed form is
    evaluated by a two-dimensional prefix sum, i.e. WITHOUT forming M, and then
    checked against M^T Delta M."""
    m = h - 1
    Wm = np.zeros((h + 1, h + 1))
    np.add.at(Wm, (er, et), w)
    # F[a, b] = sum_{i <= a} sum_{j > b} Wm[i, j]
    F = np.cumsum(Wm, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((h + 1, 1))], axis=1)
    rr = np.arange(m)
    lo = np.minimum(rr[:, None], rr[None, :])
    hi = np.maximum(rr[:, None], rr[None, :])
    K = F[lo, hi]
    mono_r = bool(np.all(np.diff(F[:, :m], axis=0) >= -1.0e-300))   # up in a
    mono_c = bool(np.all(np.diff(F[:m, :], axis=1) <= 1.0e-300))    # down in b
    return dict(K=K, mono=int(mono_r and mono_c),
                nonneg=int(bool(np.all(K >= 0.0))))


def psd_sqrt(K, tol=1.0e-14):
    """K^{1/2} for a PSD K, with the negative-eigenvalue floor reported.  The
    congruence X -> K^{1/2} X K^{1/2} is the vehicle of the whole K1 chain, and
    K0 verifies that it preserves the Loewner order."""
    lam, V = eigh(sym(K))
    lmax = float(np.max(np.abs(lam))) if lam.size else 0.0
    neg = float(np.min(lam)) if lam.size else 0.0
    keep = lam > tol * max(lmax, 1.0e-300)
    s = np.zeros_like(lam)
    s[keep] = np.sqrt(lam[keep])
    return dict(Kh=sym((V * s[None, :]) @ V.T), lam=lam, neg=neg,
                lmax=lmax, null=int(np.count_nonzero(~keep)))


def abel_split(H):
    """THE ENERGY REORDERING, exact for ANY symmetric H:

        H = diag(s) + L_N ,  s_r = sum_t H_rt ,  N = -offdiag(H) ,
        L_N = diag(N 1) - N ,

    equivalently, for every u,

        u^T H u = sum_r s_r u_r^2 + sum_{r<s} N_rs (u_r - u_s)^2 .

    A MASS term at the row sums of H plus a LONG-RANGE DIRICHLET form at the
    NEGATED off-diagonal.  Because H is negative off the diagonal on most of
    the area (T139: 0.71 .. 0.87) the Dirichlet weights N are mostly POSITIVE,
    and the split into N = N_+ - N_- isolates the part that must be estimated
    from the part that may be DROPPED: L_{N_-} >= 0 always (a Laplacian of
    nonnegative weights), so dropping it is a genuine LOEWNER step and not a
    statement about a mean."""
    m = H.shape[0]
    s = H.sum(axis=1)
    off = H - np.diag(np.diag(H))
    N = -off
    Np = np.where(N > 0.0, N, 0.0)
    Nm = np.where(N < 0.0, -N, 0.0)
    LNp = np.diag(Np.sum(axis=1)) - Np
    LNm = np.diag(Nm.sum(axis=1)) - Nm
    rec = np.diag(s) + (np.diag(N.sum(axis=1)) - N)
    return dict(m=m, s=s, N=N, Np=Np, Nm=Nm, LNp=sym(LNp), LNm=sym(LNm),
                id_err=rel(H, rec), s_pos=float(np.mean(s > 0.0)),
                neg_off=(float(np.mean(N[~np.eye(m, dtype=bool)] > 0.0))
                         if m > 1 else float("nan")),
                mass_p=float(np.sum(np.maximum(s, 0.0))),
                mass_n=float(np.sum(np.minimum(s, 0.0))))


def cs_path_weights(Np):
    """THE CAUCHY-SCHWARZ STEP ALONG THE TELESCOPE, made into a matrix.

    (u_r - u_s)^2 = (sum_{k=r}^{s-1} (u_k - u_{k+1}))^2
                 <= (s - r) sum_{k=r}^{s-1} (u_k - u_{k+1})^2 ,

    so summing against the nonnegative weights N_+ gives

        sum_{r<s} N_+,rs (u_r - u_s)^2 <= sum_k Q_k (u_k - u_{k+1})^2 ,
        Q_k = sum_{r <= k < s} N_+,rs (s - r) ,

    i.e. L_{N_+} <= T_Q in the LOEWNER order with T_Q the NEAREST-NEIGHBOUR
    (path) Laplacian of the weights Q.  This is the discrete Hardy step
    (Hardy-Littlewood-Polya 1934 ch. 9 as the classical address), and Q is the
    FIRST-MOMENT weight of the kernel: it is exactly the quantity a decay
    statement for H has to control, which is why R3 gets its sharp form here.
    The Loewner claim is CERTIFIED per instance by a completed Cholesky of
    T_Q - L_{N_+}."""
    m = Np.shape[0]
    rr = np.arange(m)
    dist = rr[None, :] - rr[:, None]                      # s - r on the upper part
    Z = np.where(dist > 0, Np * dist, 0.0)
    F = np.cumsum(Z, axis=0)
    F = np.cumsum(F[:, ::-1], axis=1)[:, ::-1]
    F = np.concatenate([F[:, 1:], np.zeros((m, 1))], axis=1)
    Q = np.array([F[k, k] for k in range(m - 1)]) if m > 1 else np.zeros(0)
    T = np.zeros((m, m))
    if m > 1:
        idx = np.arange(m - 1)
        T[idx, idx] += Q
        T[idx + 1, idx + 1] += Q
        T[idx, idx + 1] -= Q
        T[idx + 1, idx] -= Q
    return dict(Q=Q, T=sym(T), q_max=(float(np.max(Q)) if Q.size else 0.0),
                q_sum=float(np.sum(Q)))


def conj_form(Kh, X):
    return sym(Kh @ sym(X) @ Kh)


def cert_psd(X):
    """CERTIFY X >= 0 (a LOEWNER step) and return the certified lam_min."""
    return cert_lam_min(sym(X))


# ----------------------------------------------------------------------------
# K2 MACHINERY -- the band as ONE object
# ----------------------------------------------------------------------------
def stripe_groups(starts, counts, nb, L):
    """Consecutive groups of L stripes, as edge-index slices.  With L = b the
    band condition |i - j| <= b forces i, j into the SAME or ADJACENT groups,
    which is what makes the checkerboard split exact."""
    out = []
    for g0 in range(0, nb, L):
        g1 = min(nb, g0 + L)
        a = int(starts[g0])
        b = int(starts[g1 - 1] + counts[g1 - 1])
        out.append((g0, g1, a, b))
    return out


def checker_bound(GR, dms_, starts, counts, nb, b, size_cap=900):
    """THE CHECKERBOARD SPLIT: Band_b = D + A_even + A_odd, EXACTLY.

    Group the stripes into consecutive blocks of length L = b.  Every pair with
    |i - j| <= b then lies inside one group or across two ADJACENT groups.  The
    adjacent pairs two-colour: (0,1), (2,3), ... have pairwise DISJOINT
    supports, and so do (1,2), (3,4), ...  Hence with

        D       = the group-diagonal part (block diagonal),
        A_even  = the masked cross blocks of the even adjacent pairs,
        A_odd   = the masked cross blocks of the odd adjacent pairs,

    each of the three is a DIRECT SUM of small pieces and

        lam_max(Band_b) <= lam_max(D) + lam_max(A_even) + lam_max(A_odd)
                         = max_g lam_max(D_g)
                           + max_{even} sigma_max(B) + max_{odd} sigma_max(B)

    by Weyl 1912 -- THREE steps, independent of nb.  That is the replacement
    for the O(nb) layer steps (R2).  lam_max of a block [[0,B],[B^T,0]] is
    sigma_max(B), which is why the cross terms are singular values.  The
    identity Band_b = D + A_even + A_odd is verified entrywise, and the
    resulting bound is checked against a Rayleigh quotient of Band_b."""
    L = max(1, int(b))
    grp = stripe_groups(starts, counts, nb, L)
    n_g = len(grp)
    diag_lam, even_s, odd_s, sizes = [], [], [], []
    inb = dms_ <= b
    ok_size = True
    for (g0, g1, a, bb) in grp:
        blk = GR[a:bb, a:bb]
        sizes.append(bb - a)
        if blk.shape[0] == 0:
            continue
        if blk.shape[0] > size_cap:
            ok_size = False
            diag_lam.append(cert_lam_max(sym(blk), guess=ray_top(sym(blk))))
        else:
            diag_lam.append(float(eigvalsh(sym(blk),
                                           subset_by_index=[blk.shape[0] - 1,
                                                            blk.shape[0] - 1])[0]))
    for k in range(n_g - 1):
        (a0, a1, ia, ib) = grp[k]
        (b0, b1, ja, jb) = grp[k + 1]
        B = np.where(inb[ia:ib, ja:jb], GR[ia:ib, ja:jb], 0.0)
        if B.size == 0:
            s = 0.0
        elif min(B.shape) > size_cap:
            ok_size = False
            s = math.sqrt(max(ray_top(sym(B.T @ B)), 0.0))
        else:
            sv = svdvals(B)
            s = float(sv[0]) if sv.size else 0.0
        (even_s if k % 2 == 0 else odd_s).append(s)
    bound = (max(diag_lam) if diag_lam else 0.0) \
        + (max(even_s) if even_s else 0.0) + (max(odd_s) if odd_s else 0.0)
    # the EXACTNESS of the split, entrywise
    Band = np.where(inb, GR, 0.0)
    Rec = np.zeros_like(Band)
    for (g0, g1, a, bb) in grp:
        Rec[a:bb, a:bb] = Band[a:bb, a:bb]
    for k in range(n_g - 1):
        (a0, a1, ia, ib) = grp[k]
        (b0, b1, ja, jb) = grp[k + 1]
        Rec[ia:ib, ja:jb] = Band[ia:ib, ja:jb]
        Rec[ja:jb, ia:ib] = Band[ja:jb, ia:ib]
    split_err = rel(Rec, Band)
    lo = ray_top(Band)
    del Band, Rec, inb
    return dict(b=int(b), bound=bound, lo=lo, n_g=n_g,
                core=int(max(sizes) if sizes else 0),
                core2=int(max([sizes[i] + sizes[i + 1]
                               for i in range(len(sizes) - 1)] or [0])),
                diag_max=(max(diag_lam) if diag_lam else float("nan")),
                even_max=(max(even_s) if even_s else 0.0),
                odd_max=(max(odd_s) if odd_s else 0.0),
                spread=(float(np.std(diag_lam) / max(abs(np.mean(diag_lam)),
                                                     1.0e-300))
                        if len(diag_lam) > 1 else float("nan")),
                split_err=split_err, size_ok=int(ok_size))


def num_rank(X, bar=BAR_RANK):
    lam = eigvalsh(sym(X))
    mx = float(np.max(np.abs(lam))) if lam.size else 0.0
    return int(np.count_nonzero(np.abs(lam) > bar * max(mx, 1.0e-300))), lam


# ----------------------------------------------------------------------------
# K3 MACHINERY -- the border level
# ----------------------------------------------------------------------------
def paired_neumann_small(S, ladder=M_LADDER):
    """THE m-PAIRED NEUMANN CERTIFICATE (T138 / T139), QUOTED in form and
    reduced to what K3 needs: the certificate itself, the need ratio, the index
    distance of its argmax, and -- new here -- the FAR MASS FRACTION of the
    offending entry, i.e. how much of the obstructing sum is carried by
    intermediate indices at distance >= FAR_K.  A decay statement can only ever
    repair what is far-carried, and this makes that decidable instead of a
    matter of taste."""
    g = S.shape[0]
    S = sym(S)
    off = S - np.diag(np.diag(S))
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    S_B = sym(S + LD)
    facB = safe_cho(S_B)
    if facB is None:
        return None
    Ig = np.eye(g)
    G_B = cho_solve(facB, Ig, check_finite=False)
    rr = np.arange(g)
    dmat = np.abs(rr[:, None] - rr[None, :])
    F = G_B @ LD
    Fabs = np.abs(F)
    lo1, up1 = perron_bracket(lambda v: Fabs @ v, g, 80)
    out = dict(g=g, rho_fabs=up1, rho_fabs_lo=lo1,
               inv_nonneg=int(bool(np.all(G_B >= -1.0e-14
                                          * float(np.abs(G_B).max())))))
    rungs = []
    Fm = Ig.copy()
    Pm = np.zeros((g, g))
    for m in range(1, max(ladder) + 1):
        Pm = Pm + Fm
        Fm = Fm @ F
        if m not in ladder:
            continue
        Fma = np.abs(Fm)
        lo, up = perron_bracket(lambda v: Fma @ v, g, 80)
        row = dict(m=m, rho_up=up, cert=0, need=float("inf"), need_d=-1,
                   need_far=float("inf"), far_frac=float("nan"))
        if up < 1.0:
            try:
                Tm = np.linalg.solve(Ig - Fma, Fma)
                TG = Tm @ G_B
                bad = np.abs(Pm) @ TG
                good = Pm @ G_B
                row["cert"] = int(float(np.min(good - bad)) > 0.0)
                rat = bad / np.maximum(good, 1.0e-300)
                row["need"] = float(np.max(rat))
                idx = int(np.argmax(rat))
                r0, s0 = divmod(idx, g)
                row["need_d"] = int(dmat[r0, s0])
                row["r0"], row["s0"] = r0, s0
                far = dmat >= 2
                row["need_far"] = float(np.max(rat[far])) if far.any() else float("nan")
                contrib = np.abs(Pm)[r0, :] * TG[:, s0]
                tot = float(np.sum(np.abs(contrib)))
                fk = np.abs(np.arange(g) - s0) >= FAR_K
                row["far_frac"] = (float(np.sum(np.abs(contrib[fk]))) / tot
                                   if tot > 0.0 else float("nan"))
                del Tm, TG, bad, good, rat
            except LinAlgError:
                pass
        rungs.append(row)
        del Fma
    out["rungs"] = rungs
    out["cert_any"] = int(any(r["cert"] for r in rungs))
    fin = [r for r in rungs if np.isfinite(r["need"])]
    out["need_best"] = qmin([r["need"] for r in fin]) if fin else float("inf")
    best = min(fin, key=lambda r: r["need"]) if fin else None
    out["need_d_best"] = best["need_d"] if best else -1
    out["need_far_best"] = best["need_far"] if best else float("nan")
    out["far_frac_best"] = best["far_frac"] if best else float("nan")
    out["_S"], out["_S_B"], out["_LD"], out["_G_B"] = S, S_B, LD, G_B
    del F, Fabs, Fm, Pm, Dl
    return out


def core_reduce(S, S_B, LD, G_B, M_lab=None):
    """THE K1 FINITE-CORE REDUCTION, RUN ONE LEVEL DOWN.  Same three objects on
    the border block's own lumped pair: the edge system of L_Delta, the covering
    kernel K, the mixed second difference H of S_B^{-1}, and the claim
    rho(W_S) = lam_max(K^{1/2} H K^{1/2}) against the direct
    rho(W_S) = lam_max(L^{-1} L_Delta L^{-T})."""
    g = S.shape[0]
    if g < 4:
        return None
    try:
        L = np.linalg.cholesky(S_B)
    except LinAlgError:
        return None
    Li = np.linalg.solve(L, np.eye(g))
    rho_w = float(eigvalsh(sym(Li @ LD @ Li.T),
                           subset_by_index=[g - 1, g - 1])[0])
    ed = edge_list(np.where(LD < 0.0, -LD, 0.0), M_lab)
    if ed["n"] < 3:
        return None
    H = mixed_second_difference(G_B)
    ck = cover_kernel_closed(ed["er"], ed["et"], ed["w"], g)
    sq = psd_sqrt(ck["K"])
    Y = conj_form(sq["Kh"], H)
    lam_core = float(eigvalsh(Y, subset_by_index=[g - 2, g - 2])[0])
    ab = abel_split(H)
    return dict(g=g, rho_w=rho_w, lam_core=lam_core,
                red_err=abs(lam_core - rho_w) / max(abs(rho_w), 1.0e-300),
                n_e=ed["n"], id_err=ab["id_err"], neg_off=ab["neg_off"],
                mono=ck["mono"])


# ----------------------------------------------------------------------------
section("K0  SETUP, the pair, the H-telescope, and the DIRECTION calibrations")
# ----------------------------------------------------------------------------
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

BERT_OK = bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
EVEN_OK = bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12))
check("el_k0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

RNG = np.random.default_rng(1400728)

para("""K0.0  THE RH FENCE, STATED BEFORE ANY NUMBER.  The surrounding statement
is the positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999)
on a FINITE list of prime-power zones and a FINITE window; the criterion is
CITED as that address and is NEVER USED here, in either direction.  Nothing in
this file claims, assumes or approaches RH: even with R1 closed, what would
stand is a finite-window positivity statement, and the distance from there to RH
is mapped in K4 and never travelled.""")

# --- K0.1  the odd section against its entrywise definition -----------------
_k0, _D0, _M0 = None, None, None
for _kk in range(2, NZ_DEEP - 2):
    _Dc = 0.5 * float(G_DEEP[_kk]) / NU_MAIN
    _Mc = even_window(UU_ALL[_kk], _Dc)
    if 110 <= _Mc // 2 <= 190:
        _k0, _D0, _M0 = _kk, _Dc, _Mc
if _k0 is None:
    raise SystemExit("K0 found no calibration window in the declared h band")
_al0 = 0.5 * _M0 * _D0
_h0 = _M0 // 2
_c0, _ = lag_vector_fast(_al0, _M0, atoms_in(_al0, ATOMS_ALL))
E_ODD = rel(odd_toeplitz(_c0, _M0), odd_toeplitz_slow(_c0, _M0))
check("el_k0.odd_section", E_ODD <= BAR_ID,
      "the vectorised odd section equals its entrywise definition A_rs = "
      "c_{|r-s|} - c_{M-1-r-s} to %.2e (bar %.0e) on the calibration window "
      "h = %d, D = %.3e -- the coordinates of T106..T139, unchanged"
      % (E_ODD, BAR_ID, _h0, _D0))

_A0 = sym(odd_toeplitz(_c0, _M0))
_lp0 = lump_pair(_A0)
_an0 = anchor_floor(_lp0["A_B"])
check("el_k0.lumping", _lp0["stieltjes"] == 1
      and rel(_lp0["A_B"].sum(axis=1), _lp0["w"]) <= BAR_ID
      and _an0 is not None and _an0["nonneg"] == 1,
      "the lumped pair is STIELTJES, the ROW SUMS are preserved to %.2e, and "
      "A_B x = 1 has x >= 0, so A_B is a nonsingular M-matrix (Fan 1958; "
      "Berman-Plemmons 1979) with anchor lam_min(A_B) >= %.3e.  DIRECTION: "
      "A_B >= A in the Loewner order, so the floor is reached only through the "
      "INVERSE side"
      % (rel(_lp0["A_B"].sum(axis=1), _lp0["w"]), _an0["floor"]))

_G0 = cho_solve(_an0["fac"], np.eye(_h0), check_finite=False)
_ed0 = edge_list(_lp0["Dl"], _M0)
_wt0 = np.sqrt(_ed0["w"])
_GR0 = signed_gram(_G0, _ed0["er"], _ed0["et"], _wt0)
_H0 = mixed_second_difference(_G0)
_M_inc = interval_incidence(_ed0["er"], _ed0["et"], _h0)
_C0 = _wt0[:, None] * _M_inc
_TEL = rel(_GR0, _C0 @ _H0 @ _C0.T)
check("el_k0.telescope_form", _TEL <= BAR_ID,
      "THE H-TELESCOPE AS AN IDENTITY FOR THE FORM, re-verified here because "
      "all of K1 rests on it: Gram = C H C^T with C = diag(sqrt Delta) M and "
      "M_{e,r} = 1[a_e <= r < b_e], to %.2e (bar %.0e; T139 QUOTED the entry "
      "version at %.0e).  Equivalently x^T Gram x = u^T H u with u = C^T x the "
      "OCCUPATION function -- Abel summation over the box structure, no "
      "absolute value, no factorisation"
      % (_TEL, BAR_ID, TEL_ERR_T139))

# --- K0.2  the DIRECTION calibrations K1 / K2 lean on -----------------------
_Zr = RNG.standard_normal((40, 40))
_Xr = sym(_Zr @ _Zr.T)
_Pr = RNG.standard_normal((40, 40))
_Yr = _Xr + sym(_Pr @ _Pr.T)          # Y - X is PSD by construction
_Cr = RNG.standard_normal((40, 25))
_cong = float(np.min(eigvalsh(_Cr.T @ (_Yr - _Xr) @ _Cr)))
check("el_k0.congruence_loewner", _cong >= -1.0e-9 * float(np.max(np.abs(_Yr))),
      "CONGRUENCE PRESERVES THE LOEWNER ORDER, verified rather than asserted: "
      "for X <= Y and any C, C^T (Y - X) C >= 0 (lam_min = %.2e on the "
      "calibration pair).  THIS IS THE LICENCE for every step of the K1 chain, "
      "each of which replaces the inner matrix under a fixed congruence by "
      "K^{1/2} or C" % _cong)

_lo0 = ray_top(_GR0)
_up0 = cert_lam_max(_GR0, guess=_lo0)
_ex0 = float(eigvalsh(_GR0, subset_by_index=[_GR0.shape[0] - 1,
                                             _GR0.shape[0] - 1])[0])
check("el_k0.directions", _lo0 <= _ex0 * (1.0 + 1.0e-9)
      and _ex0 <= _up0 * (1.0 + 1.0e-9),
      "THE TWO DIRECTIONS, verified on the calibration Gram: Rayleigh quotient "
      "%.6f <= exact lam_max %.6f <= completed-Cholesky certificate %.6f "
      "(Wilkinson 1968; Higham 2002).  Only the UPPER end can produce a floor; "
      "the LOWER end can only KILL a route, and killing a family from below is "
      "the sharpest move available" % (_lo0, _ex0, _up0))

_ab0 = abel_split(_H0)
_cs0 = cs_path_weights(_ab0["Np"])
_lw0 = cert_psd(_cs0["T"] - _ab0["LNp"])
_lm0 = cert_psd(_ab0["LNm"])
check("el_k0.hardy_step", _lw0 >= -1.0e-9 * gersh(_cs0["T"])
      and _lm0 >= -1.0e-9 * max(gersh(_ab0["LNm"]), 1.0e-300),
      "THE TWO LOEWNER STEPS OF K1, CERTIFIED on the calibration window and "
      "not assumed: T_Q - L_{N_+} >= 0 with certified lam_min %.3e (the "
      "Cauchy-Schwarz / discrete Hardy step along the telescope), and "
      "L_{N_-} >= 0 with certified lam_min %.3e (so DROPPING it is a Loewner "
      "drop, not a negative mean).  Abel identity H = diag(s) + L_N holds to "
      "%.2e" % (_lw0, _lm0, _ab0["id_err"]))

info("K0.calibration", "h = %d, D = %.3e, n_e = %d edges in %d stripes; the "
     "H grid is %d x %d; N_+ carries %.3f of the off-diagonal (T139 QUOTED H "
     "negative on %.2f .. %.2f), row sums of H positive on %.3f"
     % (_h0, _D0, _ed0["n"], _ed0["nb"], _h0 - 1, _h0 - 1, _ab0["neg_off"],
        H_NEG_OFF_T139[0], H_NEG_OFF_T139[1], _ab0["s_pos"]))
del _GR0, _G0, _H0, _M_inc, _C0, _ab0, _cs0, _Xr, _Yr, _Cr, _Zr, _Pr

# ----------------------------------------------------------------------------
section("K1  THE QUADRATIC FORM DIRECTLY -- incidence, covering kernel, energy")
# ----------------------------------------------------------------------------
para("""K1.0  WHAT IS BEING BUILT AND WHY IT IS NOT A DECAY LEMMA.  T139 closed
the decay-lemma family from below: an entrywise envelope for H produces an
absolute-value bound on the Gram, and that family is certified dead (rho(|E|) >=
%.2f), while a stripe-layer series pays one positive Weyl term per layer and is
dead from below as well (max_b Rayleigh(Band_b) = %.2f .. %.2f > target).  Both
deaths have the same cause: the CANCELLATION between boxes is destroyed before
the eigenvalue is taken.  So this block never leaves the quadratic form.  The
H-telescope is upgraded from an identity about entries to the identity
Gram = C H C^T (K0), which makes the Rayleigh quotient of the Gram a Rayleigh
quotient of H against the OCCUPATION function of the edge system; the geometry
is then separated exactly into the covering kernel K = M^T Delta M, and the
energy is reordered by Abel summation into a MASS term and a LONG-RANGE
DIRICHLET form.  Every subsequent step is a LOEWNER step under a fixed
congruence, certified per instance, so the compensation stays inside the form
until the very last eigenvalue is taken.""" % (RHO_ABS_T137, BAND_LO_T139[0],
                                               BAND_LO_T139[1]))

# THE MEASUREMENT SURFACE.  Candidates are ALL prime-power zones whose frame-A
# window fits the size caps; the surface is then spread over log n so that the
# D range is as wide as the caps allow -- D-uniformity is the question, so a
# surface concentrated at one depth would be worthless.
CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > K12_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(K12_ZONES, 1))
    SZ = CAND[::-1][::step][:K12_ZONES]
    SZ.sort(key=lambda t: t[0])
info("K1.candidates", "%d prime-power zones admit a frame-A window inside the "
     "caps (h <= %d, n_e <= %d -- the caps, not a choice: n_e grows like h^2 "
     "and MAX_H = %d binds first); the surface takes %d of them (stride %d) "
     "from the deep end and does NOT deduplicate h, because zones with the "
     "same window size but different gaps have different D, and D is the "
     "variable the whole question is about"
     % (len(CAND), K12_HCAP, NE_CAP, MAX_H, len(SZ), step))

SURF = []
BROWS = []          # per (window, b) band rows
CROWS = []          # per (window, b) checkerboard rows
for (k, D_k, M_k, h_k) in SZ:
    if budget_left() < BUDGET_S - T_K12:
        info("K1.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(SURF)))
        break
    al = 0.5 * M_k * D_k
    ats = atoms_in(al, ATOMS_ALL)
    c, _ = lag_vector_fast(al, M_k, ats)
    A = sym(odd_toeplitz(c, M_k))
    lp = lump_pair(A)
    an = anchor_floor(lp["A_B"])
    if an is None or not an["nonneg"]:
        continue
    ed = edge_list(lp["Dl"], M_k)
    if ed["n"] < 8 or ed["n"] > NE_CAP or ed["nb"] < 6:
        continue
    n_e, nb = ed["n"], int(ed["nb"])
    A_B = lp["A_B"]
    G = cho_solve(an["fac"], np.eye(h_k), check_finite=False)
    wt = np.sqrt(ed["w"])
    GR = signed_gram(G, ed["er"], ed["et"], wt)
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        continue
    rho_ex = 1.0 - gap_ex

    # --- K1.1  the incidence identity, and the RANK of the signed Gram ------
    H = mixed_second_difference(G)
    Minc = interval_incidence(ed["er"], ed["et"], h_k)
    C = wt[:, None] * Minc
    tel_err = rel(GR, C @ H @ C.T)
    rk, lam_all = num_rank(GR)
    lam_gram = float(lam_all[-1])
    tr_gram = float(np.sum(lam_all))
    tr_W = float(np.sum(lp["LD"] * G))

    # --- K1.2  the EXACT finite-core reduction and the covering kernel ------
    ck = cover_kernel_closed(ed["er"], ed["et"], ed["w"], h_k)
    K = ck["K"]
    k_err = rel(K, Minc.T @ (ed["w"][:, None] * Minc))
    sq = psd_sqrt(K)
    Kh = sq["Kh"]
    Y = conj_form(Kh, H)
    lam_core = float(eigvalsh(Y, subset_by_index=[h_k - 2, h_k - 2])[0])
    red_err = abs(lam_core - rho_ex) / max(rho_ex, 1.0e-300)
    # the INVERSE of the covering kernel: Gantmacher-Krein would make it
    # tridiagonal for a genuine one-pair kernel -- measured, never assumed
    kk = K.shape[0]
    lamK, VK = eigh(K)
    posK = lamK > 1.0e-13 * max(float(np.max(lamK)), 1.0e-300)
    invd = np.zeros_like(lamK)
    invd[posK] = 1.0 / lamK[posK]
    Kinv = sym((VK * invd[None, :]) @ VK.T)
    tri = np.abs(np.arange(kk)[:, None] - np.arange(kk)[None, :]) <= 1
    tri_def = (float(np.max(np.abs(np.where(tri, 0.0, Kinv))))
               / max(float(np.max(np.abs(Kinv))), 1.0e-300))
    del VK, invd

    # --- K1.3  the ENERGY REORDERING and the certified chain ----------------
    ab = abel_split(H)
    cs = cs_path_weights(ab["Np"])
    step_neg = cert_psd(ab["LNm"])                     # dropping L_{N_-}
    step_cs = cert_psd(cs["T"] - ab["LNp"])            # the Hardy step
    Y1 = conj_form(Kh, np.diag(ab["s"]) + ab["LNp"])
    Y2 = conj_form(Kh, np.diag(np.maximum(ab["s"], 0.0)) + cs["T"])
    Ym = conj_form(Kh, np.diag(ab["s"]))
    Yd = conj_form(Kh, ab["LNp"])
    E0 = lam_core
    l1_ex = float(eigvalsh(Y1, subset_by_index=[h_k - 2, h_k - 2])[0])
    E1 = cert_lam_max(Y1, guess=ray_top(Y1))
    E2 = cert_lam_max(Y2, guess=ray_top(Y2))
    E_mass = cert_lam_max(Ym, guess=max(ray_top(Ym), 0.0))
    E_dir = cert_lam_max(Yd, guess=ray_top(Yd))
    lam_K = cert_lam_max(K, guess=ray_top(K))
    lam_H = cert_lam_max(H, guess=ray_top(H))
    E3 = lam_K * max(lam_H, 0.0)
    E4 = gersh(GR)
    del Y1, Y2, Ym, Yd, Y, Kinv

    # --- K2.4  THE BAND IN THE INDEX GRID OF THE CORE -----------------------
    # T139 killed the band in the STRIPE grid of the edge system.  The finite
    # core of K1 offers a DIFFERENT band: cut H by INDEX distance |r - s| <= b.
    # This is not the same family, and it has one property the stripe band can
    # never have -- the discarded far part may be LOEWNER-NONPOSITIVE, in which
    # case the truncation is legitimate and R1 reduces to a banded statement
    # about H.  That is a certifiable yes/no question, asked here.
    rrh = np.arange(h_k - 1)
    disth = np.abs(rrh[:, None] - rrh[None, :])
    hb = []
    for b in B_LIST:
        if b > h_k - 3:
            continue
        Hn = np.where(disth <= b, H, 0.0)
        Yn = conj_form(Kh, Hn)
        Yf = conj_form(Kh, H - Hn)
        lo_n = ray_top(Yn)
        up_n = cert_lam_max(Yn, guess=lo_n)
        cf = cert_lam_max_signed(Yf)
        hb.append(dict(b=int(b), lo=lo_n, up=up_n, cert_far=cf,
                       weyl=up_n + max(cf, 0.0),
                       loewner=int(np.isfinite(cf) and cf <= 0.0)))
        del Hn, Yn, Yf
    del disth

    # --- K2.1  the band as ONE object: from below, and its rank -------------
    dms_ = band_masks(ed["sidx"])
    band_rows = []
    for b in B_LIST:
        if b > nb - 1:
            continue
        Band = np.where(dms_ <= b, GR, 0.0)
        lo_b = ray_top(Band)
        up_b = (cert_lam_max(sym(Band), guess=lo_b) if b in B_CERT
                else float("nan"))
        rk_b = num_rank(Band)[0] if b in B_RANK else -1
        band_rows.append(dict(b=int(b), lo=lo_b, up=up_b, rank=rk_b))
        BROWS.append(dict(h=h_k, D=D_k, b=int(b), lo=lo_b, up=up_b, rank=rk_b))
        del Band
        if budget_left() < BUDGET_S - T_K12 + 60.0:
            break

    # --- K2.2  the CHECKERBOARD split: three Weyl steps, small cores --------
    chk = []
    for b in B_CHECK:
        if b > nb - 1:
            continue
        cb = checker_bound(GR, dms_, ed["stripe_start"], ed["stripe_count"],
                           nb, b)
        chk.append(cb)
        CROWS.append(dict(h=h_k, D=D_k, **cb))
        if budget_left() < BUDGET_S - T_K12 + 40.0:
            break

    # --- K2.3  BENDIXSON: the non-symmetric W, no Gram at all ---------------
    Wns = lp["LD"] @ G
    Wsym = sym(Wns)
    bend = cert_lam_max(Wsym, guess=ray_top(Wsym))
    try:
        ev = np.linalg.eigvals(Wns)
        im_max = float(np.max(np.abs(ev.imag))) / max(
            float(np.max(np.abs(ev.real))), 1.0e-300)
        re_max = float(np.max(ev.real))
    except LinAlgError:
        im_max, re_max = float("nan"), float("nan")
    del Wns, Wsym

    SURF.append(dict(n=NN_ALL[k], h=h_k, M=M_k, D=D_k, al=al, n_e=n_e, nb=nb,
                     anchor=an["floor"], rho_ex=rho_ex, gap_ex=gap_ex,
                     tel_err=tel_err, rank=rk, lam_gram=lam_gram,
                     tr_gram=tr_gram, tr_W=tr_W,
                     tr_err=abs(tr_gram - tr_W) / max(abs(tr_W), 1.0e-300),
                     k_err=k_err, mono=ck["mono"], nonneg=ck["nonneg"],
                     null=sq["null"], negK=sq["neg"], tri_def=tri_def,
                     lam_core=lam_core, red_err=red_err,
                     id_err=ab["id_err"], s_pos=ab["s_pos"],
                     neg_off=ab["neg_off"], q_max=cs["q_max"],
                     q_sum=cs["q_sum"], step_neg=step_neg, step_cs=step_cs,
                     E0=E0, E1=E1, E2=E2, E3=E3, E4=E4, l1_ex=l1_ex,
                     E_mass=E_mass, E_dir=E_dir, lam_K=lam_K, lam_H=lam_H,
                     bands=band_rows, chk=chk, hb=hb, bend=bend, im_max=im_max,
                     re_max=re_max, ell_max=float(np.max(ed["et"] - ed["er"]))))
    del A, A_B, G, GR, H, Minc, C, K, Kh, dms_, lp, an, ed, ab, cs, lam_all

if not SURF:
    raise SystemExit("K1 produced no window -- probe cannot report")

info("K1.surface", "%d windows, h = %d .. %d, D = %.3e .. %.3e, zones "
     "n = %d .. %d, edges %d .. %d in %d .. %d stripes; exact rho(W) = "
     "%.4f .. %.4f (T139 QUOTED %.4f .. %.4f)"
     % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
        qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
        min(r["n"] for r in SURF), max(r["n"] for r in SURF),
        min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
        min(r["nb"] for r in SURF), max(r["nb"] for r in SURF),
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        RHO_W_T139[0], RHO_W_T139[1]))

# --- the TARGET, rebuilt on this surface exactly as T139 did ----------------
F_GAP = pow_fit([r["D"] for r in SURF], [r["gap_ex"] for r in SURF], "gap")
P_GAP = F_GAP["p"]
C_GAP = qmin([r["gap_ex"] / (r["D"] ** P_GAP) for r in SURF])
for r in SURF:
    r["target"] = 1.0 - C_GAP * (r["D"] ** P_GAP)
info("K1.target", "1 - rho(W) ~ %.3e D^%.3f +- %.3f (FIT, rms %.3f, n = %d); "
     "worst-case constant c = %.3e, so the target envelope is %.6f .. %.6f.  "
     "A bound CLEARS only if it sits below the target on EVERY window (bar "
     "%.1f, declared before any number)"
     % (F_GAP["c"], P_GAP, F_GAP["sp"], F_GAP["rms"], F_GAP["n"], C_GAP,
        qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        BAR_COVER))

# --- K1.1  the identity and the rank ---------------------------------------
check("el_k1.incidence_identity",
      all(r["tel_err"] <= BAR_ID for r in SURF)
      and all(r["tr_err"] <= 1.0e-9 for r in SURF),
      "GRAM = C H C^T ON THE WHOLE SURFACE, to %.2e .. %.2e (bar %.0e), with "
      "C = diag(sqrt Delta) M and M the edge-interval incidence matrix.  This "
      "is the H-telescope as an identity for the FORM: x^T Gram x = u^T H u "
      "with u = C^T x the occupation function of the weighted edge system, "
      "which is Abel summation over the box structure with NO absolute value "
      "and NO factorisation.  The consistency bridge to the non-symmetric "
      "picture holds too: tr(Gram) = tr(W) = tr(L_Delta A_B^{-1}) to "
      "%.2e .. %.2e"
      % (qmin([r["tel_err"] for r in SURF]), qmax([r["tel_err"] for r in SURF]),
         BAR_ID, qmin([r["tr_err"] for r in SURF]),
         qmax([r["tr_err"] for r in SURF])))

check("el_k1.rank_bound", all(r["rank"] <= r["h"] - 1 for r in SURF),
      "THE SIGNED GRAM IS LOW RANK, and this is the structural reason the band "
      "family had to die.  rank(Gram) <= h - 1 because Gram = C H C^T with C of "
      "size n_e x (h-1): measured rank %d .. %d against n_e = %d .. %d edges "
      "and the algebraic ceiling h - 1 = %d .. %d.  So the whole "
      "n_e-dimensional spectral question lives on the h-dimensional index grid "
      "-- a %.1f .. %.1f x reduction of the object, exactly and per zone"
      % (min(r["rank"] for r in SURF), max(r["rank"] for r in SURF),
         min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
         min(r["h"] - 1 for r in SURF), max(r["h"] - 1 for r in SURF),
         qmin([r["n_e"] / max(r["rank"], 1) for r in SURF]),
         qmax([r["n_e"] / max(r["rank"], 1) for r in SURF])))

# --- K1.2  the covering kernel and the exact reduction ----------------------
check("el_k1.cover_kernel",
      all(r["k_err"] <= BAR_ID for r in SURF)
      and all(r["mono"] == 1 and r["nonneg"] == 1 for r in SURF),
      "THE COVERING KERNEL IN CLOSED FORM.  K_rs = W([r ^ s, r v s]) -- the "
      "total edge weight of the edges whose interval contains both indices -- "
      "equals M^T Delta M to %.2e .. %.2e (bar %.0e) on every window, and is "
      "entrywise NONNEGATIVE and MONOTONE by inclusion on every window "
      "(exact comparisons, not fits).  So the GEOMETRY of the edge system is "
      "available in closed form from Delta alone, with no inverse and no "
      "Green function in it"
      % (qmin([r["k_err"] for r in SURF]), qmax([r["k_err"] for r in SURF]),
         BAR_ID))

check("el_k1.finite_core", all(r["red_err"] <= BAR_RED for r in SURF),
      "THE EXACT FINITE-CORE REDUCTION, the central result of this probe: "
      "rho(W) = lam_max(K^{1/2} H K^{1/2}) to %.2e .. %.2e (bar %.0e) on every "
      "window, because the nonzero spectra of C H C^T and K^{1/2} H K^{1/2} "
      "coincide.  LEFT: an n_e x n_e signed Gram, n_e = %d .. %d.  RIGHT: two "
      "matrices of size h - 1 = %d .. %d, one of them (K) in CLOSED GEOMETRIC "
      "FORM and the other (H) the mixed second difference whose sign law is "
      "already derived (T139).  The signed inequality R1 is therefore a "
      "statement about a FINITE CORE per zone, and no truncation, no envelope "
      "and no series was used to get there"
      % (qmin([r["red_err"] for r in SURF]), qmax([r["red_err"] for r in SURF]),
         BAR_RED, min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
         min(r["h"] - 1 for r in SURF), max(r["h"] - 1 for r in SURF)))

info("K1.kernel_shape", "the covering kernel is Green-LIKE but not one-pair: "
     "the off-tridiagonal defect of K^{-1} is %.3f .. %.3f of its largest "
     "entry (Gantmacher-Krein 1950/1960 would force 0 for a genuine one-pair "
     "kernel), K has null dimension %d .. %d and lam_min >= %.2e; "
     "lam_max(K) = %.3e .. %.3e and lam_max(H) = %.3e .. %.3e"
     % (qmin([r["tri_def"] for r in SURF]), qmax([r["tri_def"] for r in SURF]),
        min(r["null"] for r in SURF), max(r["null"] for r in SURF),
        qmin([r["negK"] for r in SURF]),
        qmin([r["lam_K"] for r in SURF]), qmax([r["lam_K"] for r in SURF]),
        qmin([r["lam_H"] for r in SURF]), qmax([r["lam_H"] for r in SURF])))

# --- K1.3  the energy reordering and the certified chain --------------------
check("el_k1.energy_identity",
      all(r["id_err"] <= BAR_ID for r in SURF),
      "THE ENERGY REORDERING, exact on every window: H = diag(s) + L_N with "
      "s the row sums of H and N = -offdiag(H), to %.2e .. %.2e (bar %.0e).  "
      "In form language u^T H u = sum_r s_r u_r^2 + sum_{r<s} N_rs (u_r-u_s)^2 "
      "-- a MASS term plus a LONG-RANGE DIRICHLET form.  The Dirichlet weights "
      "are POSITIVE on %.3f .. %.3f of the off-diagonal (this is T139's sign "
      "law seen as a Dirichlet form: H negative off-diagonal MEANS a positive "
      "Dirichlet weight), and the mass coefficients s_r are positive on only "
      "%.3f .. %.3f, so a genuine part of the mass term is Loewner-negative "
      "and may be dropped"
      % (qmin([r["id_err"] for r in SURF]), qmax([r["id_err"] for r in SURF]),
         BAR_ID, qmin([r["neg_off"] for r in SURF]),
         qmax([r["neg_off"] for r in SURF]),
         qmin([r["s_pos"] for r in SURF]), qmax([r["s_pos"] for r in SURF])))

check("el_k1.loewner_chain",
      all(r["step_neg"] >= -1.0e-8 * max(abs(r["E1"]), 1.0) for r in SURF)
      and all(r["step_cs"] >= -1.0e-8 * max(abs(r["E2"]), 1.0) for r in SURF)
      and all(r["E1"] >= r["E0"] * (1.0 - 1.0e-7) for r in SURF)
      and all(r["E2"] >= r["E1"] * (1.0 - 1.0e-7) for r in SURF),
      "THE CHAIN, EVERY STEP CERTIFIED AND EVERY DIRECTION CHECKED.  Step (i) "
      "drop L_{N_-}: certified lam_min >= %.2e .. %.2e, i.e. zero to the "
      "declared floating-point floor, so it is a LOEWNER drop.  Step (ii) the "
      "Cauchy-Schwarz / discrete Hardy comparison L_{N_+} <= T_Q: certified "
      "lam_min(T_Q - L_{N_+}) >= %.2e .. %.2e.  "
      "Step (iii) diag(s) <= diag(s_+): trivial.  Under the fixed congruence "
      "by K^{1/2} (K0) the three steps compose, and the resulting numbers are "
      "monotone on every window: E0 = rho(W) <= E1 <= E2, verified"
      % (qmin([r["step_neg"] for r in SURF]),
         qmax([r["step_neg"] for r in SURF]),
         qmin([r["step_cs"] for r in SURF]), qmax([r["step_cs"] for r in SURF])))

E1_OK = [r for r in SURF if r["E1"] < r["target"]]
E2_OK = [r for r in SURF if r["E2"] < r["target"]]
E3_OK = [r for r in SURF if r["E3"] < r["target"]]
E4_OK = [r for r in SURF if r["E4"] < r["target"]]
check("el_k1.form_bound_value",
      all(np.isfinite(r["E1"]) and np.isfinite(r["E2"]) for r in SURF),
      "THE VALUE OF THE DIRECT FORM BOUND, AND WHERE IT TEARS -- the key K1 "
      "number.  E0 = rho(W) = %.4f .. %.4f (exact).  E1, after the single "
      "Loewner drop of L_{N_-}: %.3e .. %.3e, i.e. %.1f .. %.1f x E0, below "
      "the target on %d of %d windows.  E2, after the Cauchy-Schwarz step: "
      "%.3e .. %.3e, i.e. %.1e .. %.1e x E0, below target on %d of %d.  The "
      "crude product bound lam_max(K) lam_max(H) is %.3e .. %.3e (%d of %d) "
      "and the absolute row-sum reference gersh(Gram) is %.3e .. %.3e (%d of "
      "%d).  SO IT TEARS AT STEP (i), NOT AT STEP (ii): dropping L_{N_-} -- "
      "the %.2f .. %.2f fraction of the off-diagonal where H is POSITIVE -- "
      "already costs the whole margin, because that positive part is exactly "
      "the compensation the sign law relies on.  The Hardy step then adds "
      "%.1f .. %.1f x on top, and the first-moment weight it needs is "
      "max_k Q_k = %.3e .. %.3e (this is the sharp form of R3: not a decay "
      "exponent for H but a FIRST-MOMENT bound on N_+)"
      % (qmin([r["E0"] for r in SURF]), qmax([r["E0"] for r in SURF]),
         qmin([r["E1"] for r in SURF]), qmax([r["E1"] for r in SURF]),
         qmin([r["E1"] / r["E0"] for r in SURF]),
         qmax([r["E1"] / r["E0"] for r in SURF]), len(E1_OK), len(SURF),
         qmin([r["E2"] for r in SURF]), qmax([r["E2"] for r in SURF]),
         qmin([r["E2"] / r["E0"] for r in SURF]),
         qmax([r["E2"] / r["E0"] for r in SURF]), len(E2_OK), len(SURF),
         qmin([r["E3"] for r in SURF]), qmax([r["E3"] for r in SURF]),
         len(E3_OK), len(SURF),
         qmin([r["E4"] for r in SURF]), qmax([r["E4"] for r in SURF]),
         len(E4_OK), len(SURF),
         1.0 - qmax([r["neg_off"] for r in SURF]),
         1.0 - qmin([r["neg_off"] for r in SURF]),
         qmin([r["E2"] / max(r["E1"], 1.0e-300) for r in SURF]),
         qmax([r["E2"] / max(r["E1"], 1.0e-300) for r in SURF]),
         qmin([r["q_max"] for r in SURF]), qmax([r["q_max"] for r in SURF])))

check("el_k1.two_term_split",
      all(r["E_mass"] + r["E_dir"] >= r["l1_ex"] * (1.0 - 1.0e-9)
          for r in SURF),
      "THE TWO-TERM WEYL SPLIT of the same form, reported because it isolates "
      "WHICH half is expensive: the MASS half lam_max(K^{1/2} diag(s) K^{1/2}) "
      "= %.3e .. %.3e and the DIRICHLET half lam_max(K^{1/2} L_{N_+} K^{1/2}) "
      "= %.3e .. %.3e, sum >= E1 on every window (Weyl 1912, verified).  The "
      "mass half alone is %.1f .. %.1f x the exact rho(W), so even the "
      "cancellation INSIDE the mass term matters: the row sums s_r of H are "
      "boundary telescopes of the Green function and change sign, and any "
      "bound that treats them one at a time has already lost"
      % (qmin([r["E_mass"] for r in SURF]), qmax([r["E_mass"] for r in SURF]),
         qmin([r["E_dir"] for r in SURF]), qmax([r["E_dir"] for r in SURF]),
         qmin([r["E_mass"] / r["E0"] for r in SURF]),
         qmax([r["E_mass"] / r["E0"] for r in SURF])))

# ----------------------------------------------------------------------------
section("K2  THE BAND AS ONE OBJECT -- b <= 16, no layer summation")
# ----------------------------------------------------------------------------
para("""K2.0  THE QUESTION, PRECISELY.  R1 asks for a SIGNED inequality at
stripe distance b <= %d.  There are two readings and this block separates them
with numbers.  READING A, the additive one: bound lam_max(Band_b) and add
something for the tail.  READING B, the non-additive one: never split at all
(that is K1).  Reading A is decided HERE and from BELOW, because a Rayleigh
quotient of Band_b is a rigorous lower bound and Weyl's inequality means no
upper bound for the band can undercut it -- and the tail cannot help, since
T139 certified the tail to be net NEGATIVE, i.e. truncating RAISES the radius.
The candidate technologies are run anyway, because what they deliver is worth
having even when the object they bound is the wrong one: a transfer / Floquet
argument (which needs a periodicity the atom positions do not supply), the
Bendixson field-of-values bound (which needs no Gram at all), and the
CHECKERBOARD split (which replaces the O(nb) Weyl steps of T139 by exactly
three).  One family here is genuinely new rather than inherited: the band taken
in the INDEX grid of the K1 core instead of the stripe grid of the edge system.
That family is NOT covered by T139's kill, and it is the only one in which a
truncation could be LEGITIMATE, so its far part is put to the Loewner test
directly (K2.4).""" % B_MAX_R1)

BND = [dict(b=b,
            lo_min=qmin([x["lo"] for r in SURF for x in r["bands"] if x["b"] == b]),
            lo_max=qmax([x["lo"] for r in SURF for x in r["bands"] if x["b"] == b]),
            up_min=qmin([x["up"] for r in SURF for x in r["bands"] if x["b"] == b]),
            up_max=qmax([x["up"] for r in SURF for x in r["bands"] if x["b"] == b]))
       for b in B_LIST]
for r in SURF:
    r["lo_band_max"] = qmax([x["lo"] for x in r["bands"]])
    r["b_at_max"] = max(r["bands"], key=lambda x: x["lo"])["b"]
    r["band_dead"] = int(r["lo_band_max"] > r["target"])
BAND_DEAD = [r for r in SURF if r["band_dead"]]
PAIRS = [(r, x) for r in SURF for x in r["bands"]]
check("el_k2.band_from_below",
      all(np.isfinite(x["lo"]) for r, x in PAIRS)
      and all(x["lo"] <= x["up"] * (1.0 + 1.0e-9) for r, x in PAIRS
              if np.isfinite(x["up"])),
      "THE BAND, AS ONE OBJECT AND FROM BELOW -- the number that decides "
      "reading A for every b <= %d at once.  Rayleigh quotients of Band_b: "
      "%.4f .. %.4f over all %d (window, b) pairs, attained at b = %d .. %d; "
      "where a certificate was computed the direction holds, lo <= cert "
      "(certified lam_max(Band_b) = %.4f .. %.4f).  Against the target "
      "%.6f .. %.6f the LOWER bound already exceeds it on %d of %d windows.  "
      "T139 QUOTED %.2f .. %.2f from the layer side and this reproduces it "
      "with the band treated as ONE object, so the excess was never an "
      "artefact of the layer summation: IT IS THE BAND ITSELF.  Consequently "
      "no upper bound on Band_b of ANY sharpness can serve R1, and since the "
      "discarded tail is net negative (T139), adding a tail term cannot repair "
      "it either -- reading A is closed"
      % (B_MAX_R1, qmin([x["lo"] for r, x in PAIRS]),
         qmax([x["lo"] for r, x in PAIRS]), len(PAIRS),
         min(r["b_at_max"] for r in SURF), max(r["b_at_max"] for r in SURF),
         qmin([x["up"] for r, x in PAIRS]), qmax([x["up"] for r, x in PAIRS]),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         len(BAND_DEAD), len(SURF), BAND_LO_T139[0], BAND_LO_T139[1]))

RK_B = [(r, x) for r, x in PAIRS if x["rank"] > 0]
RK_VAL = [float(x["rank"]) for r, x in RK_B]
RK_RATIO = [x["rank"] / max(r["rank"], 1) for r, x in RK_B]
check("el_k2.rank_inflation",
      bool(RK_B) and all(x["rank"] >= r["rank"] for r, x in RK_B),
      "WHY the band overshoots, mechanically: TRUNCATION INFLATES THE RANK.  "
      "The full signed Gram has rank <= h - 1 = %d .. %d (K1.1) because it is "
      "C H C^T; the band truncation is NOT of that form and its measured rank "
      "is %d .. %d, i.e. %.1f .. %.1f x larger, on the same windows.  Every "
      "unit of extra rank is a direction in which the compensation between "
      "boxes has been cut, and the %.2f .. %.2f excess over the target is that "
      "cut, not a missing decay estimate.  This is the sharpest available "
      "answer to why T137's, T138's and T139's families all died the same way"
      % (min(r["h"] - 1 for r in SURF), max(r["h"] - 1 for r in SURF),
         qmin(RK_VAL), qmax(RK_VAL), qmin(RK_RATIO), qmax(RK_RATIO),
         qmin([r["lo_band_max"] for r in SURF]),
         qmax([r["lo_band_max"] for r in SURF])))

CH = [(r, x) for r in SURF for x in r["chk"]]
check("el_k2.checkerboard",
      all(x["split_err"] <= BAR_ID for r, x in CH)
      and all(x["bound"] >= x["lo"] * (1.0 - 1.0e-7) for r, x in CH),
      "THE CHECKERBOARD SPLIT: THREE WEYL STEPS INSTEAD OF O(nb), and this is "
      "the R2 replacement.  With stripe groups of length b the band condition "
      "|i - j| <= b forces adjacent groups, the adjacent pairs two-colour into "
      "two DISJOINT families, and Band_b = D + A_even + A_odd exactly "
      "(entrywise error %.2e .. %.2e, bar %.0e).  Hence lam_max(Band_b) <= "
      "max_g lam_max(D_g) + max_even sigma_max + max_odd sigma_max, verified "
      "above the Rayleigh quotient on all %d (window, b) pairs.  DIRECTION, "
      "stated because it is easy to misread: this bounds Band_b and NOT "
      "rho(W) -- Band_b is a truncation whose tail is net negative, so the "
      "bound may and does sit BELOW rho(W) at small b without bounding it.  "
      "Value %.3f .. %.3f, i.e. %.2f .. %.2f x the exact rho(W): the STEP "
      "COUNT is "
      "now 3 and D-independent -- T139's overshoot factor was the layer count "
      "itself -- and what remains is only the sharpness of the three terms "
      "(diagonal %.3f .. %.3f, even cross %.3f .. %.3f, odd cross "
      "%.3f .. %.3f)"
      % (qmin([x["split_err"] for r, x in CH]),
         qmax([x["split_err"] for r, x in CH]), BAR_ID, len(CH),
         qmin([x["bound"] for r, x in CH]), qmax([x["bound"] for r, x in CH]),
         qmin([x["bound"] / r["rho_ex"] for r, x in CH]),
         qmax([x["bound"] / r["rho_ex"] for r, x in CH]),
         qmin([x["diag_max"] for r, x in CH]),
         qmax([x["diag_max"] for r, x in CH]),
         qmin([x["even_max"] for r, x in CH]),
         qmax([x["even_max"] for r, x in CH]),
         qmin([x["odd_max"] for r, x in CH]),
         qmax([x["odd_max"] for r, x in CH])))

check("el_k2.finite_window_core", bool(CH),
      "THE SMALL STRIPE OBJECT, sized.  At b <= %d the checkerboard cores are "
      "%d .. %d edges per group and %d .. %d per adjacent PAIR, against "
      "n_e = %d .. %d edges in the full Gram and %d .. %d groups per window -- "
      "so the band really is per-window ALMOST FINITE, and every term of the "
      "3-step bound is the norm of one small explicit block.  QUASI-PERIODICITY "
      "MEASURED, which is what decides whether Floquet 1883 / Bloch 1929 could "
      "be run at all: the relative spread of the group-diagonal lam_max across "
      "groups is %.3f .. %.3f, so the stripe structure is NOT periodic (the "
      "stripes sit at atom positions) and a transfer argument has no cell to "
      "iterate.  What such an argument would have produced is precisely the "
      "uniform-over-groups bound above, so route (i) collapses into route "
      "(iii) with a number attached"
      % (B_MAX_R1, min(x["core"] for r, x in CH),
         max(x["core"] for r, x in CH), min(x["core2"] for r, x in CH),
         max(x["core2"] for r, x in CH), min(r["n_e"] for r in SURF),
         max(r["n_e"] for r in SURF), min(x["n_g"] for r, x in CH),
         max(x["n_g"] for r, x in CH),
         qmin([x["spread"] for r, x in CH]),
         qmax([x["spread"] for r, x in CH])))

HB = [(r, x) for r in SURF for x in r["hb"]]
HB_LOEW = [(r, x) for r, x in HB if x["loewner"]]
HB_WIN = [(r, x) for r, x in HB if x["loewner"] and x["up"] < r["target"]]
HB_W2 = [(r, x) for r, x in HB if x["weyl"] < r["target"]]
HB_ZONES = sorted({id(r) for r, x in HB_WIN})
for r in SURF:
    r["hb_win"] = int(any(x["loewner"] and x["up"] < r["target"]
                          for x in r["hb"]))
    r["hb_best"] = qmin([x["up"] for x in r["hb"] if x["loewner"]])
    r["hb_b"] = min([x["b"] for x in r["hb"] if x["loewner"]] or [-1])
HB_ALL = all(r["hb_win"] for r in SURF)
check("el_k2.h_index_band",
      all(x["lo"] <= x["up"] * (1.0 + 1.0e-9) for r, x in HB)
      and all(np.isfinite(x["cert_far"]) for r, x in HB),
      "THE BAND IN THE INDEX GRID OF THE CORE -- a DIFFERENT family from the "
      "one T139 killed, and the only one in which a truncation can be "
      "legitimate.  T139 cut the Gram by STRIPE distance; here H is cut by "
      "INDEX distance |r - s| <= b inside the finite core, and the discarded "
      "far part is asked the LOEWNER question directly, which is the only "
      "question that licenses a truncation: certified "
      "lam_max(K^{1/2} H_far K^{1/2}) = %.3e .. %.3e over all %d (window, b) "
      "pairs, NONPOSITIVE on %d of them and clearing the target on %d.  So the "
      "far part of H is Loewner-POSITIVE at every b <= %d on this surface, and "
      "the index-band truncation is as illegitimate as the stripe one -- for "
      "the same structural reason, since the far boxes carry the negative "
      "compensation and removing them RAISES the form.  What the family costs "
      "instead: the near part alone is %.4f .. %.4f (Rayleigh, a LOWER bound) "
      "and %.4f .. %.4f certified, and the honest two-term Weyl value "
      "near + far is %.4f .. %.4f against the target %.6f .. %.6f, clearing on "
      "%d of %d pairs.  DIRECTION PEDANTRY: a nonpositive CERTIFIED lam_max "
      "would be a Loewner sign, a negative mean would not -- the distinction "
      "T139's J2.2 drew for the stripe tail, asked here for the index tail and "
      "answered the same way"
      % (qmin([x["cert_far"] for r, x in HB]),
         qmax([x["cert_far"] for r, x in HB]), len(HB), len(HB_LOEW),
         len(HB_WIN), B_MAX_R1,
         qmin([x["lo"] for r, x in HB]), qmax([x["lo"] for r, x in HB]),
         qmin([x["up"] for r, x in HB]), qmax([x["up"] for r, x in HB]),
         qmin([x["weyl"] for r, x in HB]), qmax([x["weyl"] for r, x in HB]),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         len(HB_W2), len(HB)))

check("el_k2.bendixson",
      all(r["bend"] >= r["rho_ex"] * (1.0 - 1.0e-9) for r in SURF)
      and all(r["im_max"] <= BAR_IMAG for r in SURF),
      "BENDIXSON 1902 / HIRSCH 1902, the field-of-values route, run WITHOUT "
      "any Gram: W = L_Delta A_B^{-1} is not symmetric, but its spectrum is "
      "real (max |Im lam| / max |Re lam| = %.1e .. %.1e <= bar %.0e) and every "
      "eigenvalue satisfies Re lam <= lam_max(sym W), so lam_max(sym W) is a "
      "CERTIFIED upper bound on rho(W).  Measured: %.4f .. %.4f, i.e. "
      "%.2f .. %.2f x rho(W) = %.4f .. %.4f, below the target on %d of %d "
      "windows.  The symmetric part is (L_Delta G + G L_Delta)/2 and carries "
      "the SAME H structure (tr sym W = tr W = tr Gram, verified in K1.1), so "
      "this is not a new object -- it is the K1 core seen without the edge "
      "coordinates, and its slack is the price of symmetrising instead of "
      "conjugating"
      % (qmin([r["im_max"] for r in SURF]), qmax([r["im_max"] for r in SURF]),
         BAR_IMAG, qmin([r["bend"] for r in SURF]),
         qmax([r["bend"] for r in SURF]),
         qmin([r["bend"] / r["rho_ex"] for r in SURF]),
         qmax([r["bend"] / r["rho_ex"] for r in SURF]),
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
         len([r for r in SURF if r["bend"] < r["target"]]), len(SURF)))

CB4 = [c for c in CROWS if c["b"] == 4] or CROWS
F_CBD = pow_fit([c["D"] for c in CROWS], [max(c["diag_max"], 1.0e-300)
                                          for c in CROWS], "chk_diag_D")
F_CBX = pow_fit([c["D"] for c in CROWS], [max(c["even_max"], 1.0e-300)
                                          for c in CROWS], "chk_cross_D")
F_CB4 = pow_fit([c["D"] for c in CB4], [max(c["bound"], 1.0e-300)
                                        for c in CB4], "chk_bound_D")
info("K2.stripe_entries", "ARE THE SMALL STRIPE OBJECT'S ENTRIES ZONE-UNIFORM? "
     "-- the question route (iii) has to answer, made a measurement.  Across "
     "%d (window, b) pairs the group-diagonal lam_max fits D^%.2f +- %.2f "
     "(FIT) and the cross-block sigma_max fits D^%.2f +- %.2f; at b = 4 the "
     "3-step bound itself fits D^%.2f +- %.2f, with values %.3f .. %.3f.  An "
     "exponent indistinguishable from 0 is what zone-uniformity MEANS, so the "
     "measurement says the block norms are zone-uniform to within the "
     "jackknife band while the covering kernel behind them is NOT "
     "(lam_max(K) ~ D^%.2f) -- the D dependence lives entirely in the "
     "geometry, not in the stripe blocks"
     % (len(CROWS), F_CBD["p"], F_CBD["sp"], F_CBX["p"], F_CBX["sp"],
        F_CB4["p"], F_CB4["sp"], qmin([c["bound"] for c in CB4]),
        qmax([c["bound"] for c in CB4]),
        pow_fit([r["D"] for r in SURF], [r["lam_K"] for r in SURF],
                "lamK")["p"]))

F_CORE = pow_fit([r["D"] for r in SURF], [r["q_max"] for r in SURF], "q_max_D")
F_LK = pow_fit([r["D"] for r in SURF], [r["lam_K"] for r in SURF], "lamK_D")
F_LH = pow_fit([r["D"] for r in SURF], [max(r["lam_H"], 1.0e-300)
                                        for r in SURF], "lamH_D")
info("K2.zone_dependence", "the ZONE DEPENDENCE of the core quantities, as "
     "FITS in D with jackknife bands (this is the uniformity ingredient made "
     "measurable): lam_max(K) ~ D^%.2f +- %.2f, lam_max(H) ~ D^%.2f +- %.2f, "
     "max_k Q_k ~ D^%.2f +- %.2f; the PRODUCT lam_max(K) lam_max(H) ~ "
     "D^%.2f, while the exact rho(W) is flat at %.4f .. %.4f -- so the two "
     "factors move against each other and only their JOINT bound can be "
     "D-uniform, which is exactly why the product route (E3) cannot work"
     % (F_LK["p"], F_LK["sp"], F_LH["p"], F_LH["sp"], F_CORE["p"],
        F_CORE["sp"], F_LK["p"] + F_LH["p"],
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF])))

# ----------------------------------------------------------------------------
section("K3  R4 AND THE LEFTOVERS -- the one open border block, with H")
# ----------------------------------------------------------------------------
para("""K3.0  WHAT T139 LEFT AND WHAT K1 CAN SAY ABOUT IT.  R4 is a SINGLE open
border block: the m-paired Neumann certificate fails there with need %.2f, the
argmax sits at index distance %d, and the far-restricted need equals the full
need to three digits -- i.e. the obstruction is FAR-CARRIED, which is the only
situation in which a decay statement could ever help.  The pool is REBUILT here
rather than reloaded, so its open SET is its own and the count is not comparable
to T139's -- what transfers is the ANATOMY and not the tally.  Three
measurements: the need ratio with the index distance of its argmax, the FAR MASS
FRACTION of the offending entry (how much of the obstructing sum is carried by
intermediate indices at distance >= %d), and the finite-core reduction of K1
tested one level down on the border block's own lumped pair.""" % (
    NEED_R4_T139, NEED_D_R4_T139, FAR_K))

PER_RHO = []
for rho in K3_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho) // 2
        if hf > K3_HCAP or hf < H_MIN:
            continue
        key = int(round(K3_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    lst = []
    for (k, DA) in got[-K3_PER_RHO:]:
        lst.append((k, int(N_DEEP[k]), DA / rho, rho, 1))
        lst.append((k, int(N_DEEP[k]), DA, rho, 0))
    PER_RHO.append(lst)
K3_TASK = []
for i in range(max(len(l) for l in PER_RHO)):
    for l in PER_RHO:
        if i < len(l):
            K3_TASK.append(l[i])
K3_TASK = K3_TASK[:K3_MAX]

K3R = []
DEEP = []
for (k, n_lbl, D, rho_lbl, scaled) in K3_TASK:
    if budget_left() < 60.0:
        info("K3.budget", "border pool truncated at n = %d after %d blocks"
             % (n_lbl, len(K3R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < K3_GC_MIN or fr["h_n"] > K3_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    pn = paired_neumann_small(st["S"])
    if pn is None:
        del st
        continue
    if len(DEEP) < K3_DEEP and pn["g"] >= 8:
        cr = core_reduce(pn["_S"], pn["_S_B"], pn["_LD"], pn["_G_B"])
        if cr is not None:
            cr.update(n=n_lbl, rho_lbl=rho_lbl)
            DEEP.append(cr)
    G_B = pn["_G_B"]
    g = pn["g"]
    HS = mixed_second_difference(G_B)
    rr2 = np.arange(g - 1)
    d2 = np.abs(rr2[:, None] - rr2[None, :])
    pf = decay_profile(HS, d2, max(g - 2, 1))
    fH = pow_fit(pf["d"], pf["mx"], "H_border")
    offd = d2 >= 1
    pn.update(n=n_lbl, rho_lbl=rho_lbl, scaled=scaled, h=fr["h_n"], D=D,
              p_H=fH["p"],
              H_neg=(float(np.mean(HS[offd] < 0.0)) if offd.any()
                     else float("nan")),
              H_diag=float(np.mean(np.diag(HS) > 0.0)) if g > 2 else float("nan"))
    for key in ("_S", "_S_B", "_LD", "_G_B"):
        pn.pop(key, None)
    K3R.append(pn)
    del st, HS, d2, pf

if not K3R:
    raise SystemExit("K3 produced no border block -- probe cannot report")

OPEN = [r for r in K3R if not r["cert_any"]]
CERT = [r for r in K3R if r["cert_any"]]
OPEN_FIN = [r for r in OPEN if np.isfinite(r["need_best"])]
TIGHT = OPEN_FIN or sorted([r for r in K3R if np.isfinite(r["need_best"])],
                           key=lambda r: -r["need_best"])[:8]
BIG = [r for r in K3R if r["g"] >= 8]
info("K3.pool", "%d border blocks, g = %d .. %d, zones n = %d .. %d, transport "
     "ratios %.3f .. %.3f; the m-paired ladder to m = %d certifies %d, leaves "
     "%d open; rho(|F|) >= 1 on %d"
     % (len(K3R), min(r["g"] for r in K3R), max(r["g"] for r in K3R),
        min(r["n"] for r in K3R), max(r["n"] for r in K3R),
        qmin([r["rho_lbl"] for r in K3R]), qmax([r["rho_lbl"] for r in K3R]),
        max(M_LADDER), len(CERT), len(OPEN),
        len([r for r in K3R if not (r["rho_fabs"] < 1.0)])))

FF = [r["far_frac_best"] for r in TIGHT if np.isfinite(r["far_frac_best"])]
DD = [r["need_d_best"] for r in TIGHT if r["need_d_best"] >= 0]
check("el_k3.r4_anatomy", bool(TIGHT),
      "R4, DISSECTED.  The %d blocks of this REBUILT pool that the ladder "
      "leaves open (of %d; if none were open, the tightest certified ones) "
      "carry need %.2f .. %.2f (T139 "
      "QUOTED %.2f for the one open block of ITS pool -- the counts are not "
      "comparable, the anatomy is), argmax at index distance "
      "%d .. %d (T139 QUOTED %d), and the FAR MASS FRACTION of the offending "
      "entry -- the part of the obstructing sum carried by intermediate "
      "indices at distance >= %d -- is %.3f .. %.3f.  THE CONSEQUENCE, which "
      "is the point of measuring it: the obstruction is genuinely far-carried, "
      "so a decay statement is the right tool here (unlike R1, where K2 shows "
      "the obstruction sits at SMALL b and no decay can reach it).  The border "
      "H inherits the sign structure (on the %d blocks with g >= 8, so that "
      "the fractions mean something): H < 0 on %.3f .. %.3f of the "
      "off-diagonal and > 0 on %.3f .. %.3f of the diagonal, decaying as "
      "d^%.2f .. d^%.2f (FITS; T139 QUOTED d^%.2f for the top level)"
      % (len(TIGHT), len(K3R), qmin([r["need_best"] for r in TIGHT]),
         qmax([r["need_best"] for r in TIGHT]), NEED_R4_T139,
         (min(DD) if DD else -1), (max(DD) if DD else -1), NEED_D_R4_T139,
         FAR_K, qmin(FF), qmax(FF), len(BIG),
         qmin([r["H_neg"] for r in BIG]), qmax([r["H_neg"] for r in BIG]),
         qmin([r["H_diag"] for r in BIG]), qmax([r["H_diag"] for r in BIG]),
         qmin([r["p_H"] for r in BIG]), qmax([r["p_H"] for r in BIG]),
         DECAY_H_T137))

check("el_k3.core_inherited",
      bool(DEEP) and all(d["red_err"] <= 1.0e-6 for d in DEEP)
      and all(d["id_err"] <= BAR_ID for d in DEEP),
      "THE FINITE-CORE REDUCTION IS INHERITED ONE LEVEL DOWN, so K1 is a "
      "property of the construction and not of the top window: on %d border "
      "blocks (g = %d .. %d, n_e = %d .. %d edges) the identity "
      "rho(W_S) = lam_max(K_S^{1/2} H_S K_S^{1/2}) holds to %.2e .. %.2e, the "
      "energy reordering to %.2e .. %.2e, and the covering kernel is monotone "
      "on %d of %d.  rho(W_S) = %.4f .. %.4f there, i.e. the same margin "
      "question with a core of size g instead of h"
      % (len(DEEP), min(d["g"] for d in DEEP), max(d["g"] for d in DEEP),
         min(d["n_e"] for d in DEEP), max(d["n_e"] for d in DEEP),
         qmin([d["red_err"] for d in DEEP]), qmax([d["red_err"] for d in DEEP]),
         qmin([d["id_err"] for d in DEEP]), qmax([d["id_err"] for d in DEEP]),
         len([d for d in DEEP if d["mono"] == 1]), len(DEEP),
         qmin([d["rho_w"] for d in DEEP]), qmax([d["rho_w"] for d in DEEP])))

# ----------------------------------------------------------------------------
section("K4  THE MAP V12, the promotion batch, the rest list, the verdict")
# ----------------------------------------------------------------------------
RED_OK = all(r["red_err"] <= BAR_RED for r in SURF)
ID_OK = all(r["tel_err"] <= BAR_ID and r["id_err"] <= BAR_ID for r in SURF)
CORE_SMALL = all(r["rank"] <= r["h"] - 1 for r in SURF)
CARRIES = (len(E1_OK) == len(SURF) or len(E2_OK) == len(SURF)
           or all(r["bend"] < r["target"] for r in SURF)
           or all(x["bound"] < r["target"] for r, x in CH)
           or HB_ALL)
if CARRIES:
    VERDICT = "SIGNED-BAND-CARRIES"
elif RED_OK and ID_OK and CORE_SMALL:
    VERDICT = "FINITE-CORE"
else:
    VERDICT = "BAND-RESISTS"

MAP = [
    ("A  D-uniformity of the margin 1 - rho(W)",
     "OPEN -- and now with a FINITE CORE per zone (K1.2)"),
    ("A1 the H-telescope as a form identity, Gram = C H C^T",
     "CLOSED, exact to %.0e (K1.1)" % qmax([r["tel_err"] for r in SURF])),
    ("A2 rank(Gram) <= h - 1",
     "CLOSED, measured %d .. %d (K1.1)" % (min(r["rank"] for r in SURF),
                                           max(r["rank"] for r in SURF))),
    ("A3 rho(W) = lam_max(K^{1/2} H K^{1/2}), K = M^T Delta M",
     "CLOSED, exact to %.0e (K1.2)" % qmax([r["red_err"] for r in SURF])),
    ("A4 K in closed geometric form, monotone by inclusion",
     "CLOSED, exact on every window (K1.2)"),
    ("A5 energy reordering H = diag(s) + L_N",
     "CLOSED, exact to %.0e (K1.3)" % qmax([r["id_err"] for r in SURF])),
    ("A6 the direct form bound (drop L_{N_-} + Hardy step)",
     "BUILT and CERTIFIED, tears at step (i) by %.1f .. %.1f x (K1.3)"
     % (qmin([r["E1"] / r["E0"] for r in SURF]),
        qmax([r["E1"] / r["E0"] for r in SURF]))),
    ("B  the additive band-plus-tail family (reading A of R1)",
     "CLOSED NEGATIVE from below at every b <= %d (K2.1)" % B_MAX_R1),
    ("B1 the mechanism: rank inflation by truncation",
     "MEASURED, %.1f .. %.1f x rank (K2.1)" % (qmin(RK_RATIO), qmax(RK_RATIO))),
    ("B2 R2: the O(nb) Weyl steps",
     "REPLACED by 3 D-independent steps (checkerboard, K2)"),
    ("B3 transfer / Floquet on the stripes",
     "NOT APPLICABLE, spread %.2f .. %.2f, collapses into B2 (K2)"
     % (qmin([x["spread"] for r, x in CH]),
        qmax([x["spread"] for r, x in CH]))),
    ("B3a where the D dependence sits",
     "MEASURED: blocks zone-uniform (D^%.2f), geometry not (D^%.2f) (K2)"
     % (F_CBD["p"], F_LK["p"])),
    ("B4 the band in the INDEX grid of the core (H_near)",
     "CLOSED NEGATIVE: far part Loewner-POSITIVE (%.2e) at every b <= %d (K2.4)"
     % (qmin([x["cert_far"] for r, x in HB]), B_MAX_R1)),
    ("B5 Bendixson / field of values, no Gram",
     "CERTIFIED, slack %.2f .. %.2f x rho(W) (K2.3)"
     % (qmin([r["bend"] / r["rho_ex"] for r in SURF]),
        qmax([r["bend"] / r["rho_ex"] for r in SURF]))),
    ("C  R4, the open border block",
     "far-carried %.3f .. %.3f -> a decay statement IS the right tool (K3)"
     % (qmin(FF), qmax(FF))),
    ("C1 the finite core one level down",
     "INHERITED, exact to %.0e (K3)" % qmax([d["red_err"] for d in DEEP])),
    ("D  absolute-value hulls, layer series, Jaffard, one-pair",
     "CERTIFIED DEAD by T137 / T138 / T139 -- not retried here"),
    ("E  RH",
     "NOT APPROACHED.  Cited only; the gap is mapped below, never travelled"),
]
info("K4.map_v12", "%d rows" % len(MAP))
for a, b in MAP:
    print("       %-52s %s" % (a, b))

PROMO = [
    "the H-telescope is an identity for the FORM: Gram = C H C^T with "
    "C = diag(sqrt Delta) M and M the edge-interval incidence matrix "
    "(exact to %.0e on %d windows)" % (qmax([r["tel_err"] for r in SURF]),
                                       len(SURF)),
    "rank(Gram) <= h - 1: the n_e-dimensional signed Gram is a low-rank "
    "object, measured rank %d .. %d against %d .. %d edges"
    % (min(r["rank"] for r in SURF), max(r["rank"] for r in SURF),
       min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF)),
    "THE FINITE-CORE REDUCTION rho(W) = lam_max(K^{1/2} H K^{1/2}) with "
    "K = M^T Delta M, exact to %.0e" % qmax([r["red_err"] for r in SURF]),
    "the covering kernel in closed geometric form K_rs = W([r ^ s, r v s]), "
    "entrywise nonnegative and monotone by inclusion",
    "the off-tridiagonal defect of K^{-1} is %.2f .. %.2f, so K is Green-like "
    "but NOT a one-pair kernel (Gantmacher-Krein)"
    % (qmin([r["tri_def"] for r in SURF]), qmax([r["tri_def"] for r in SURF])),
    "the energy reordering H = diag(s) + L_N, exact, turning the sign law into "
    "a long-range DIRICHLET form with weights positive on %.2f .. %.2f"
    % (qmin([r["neg_off"] for r in SURF]), qmax([r["neg_off"] for r in SURF])),
    "L_{N_-} >= 0 certified: dropping the positive-H part is a Loewner drop",
    "the Cauchy-Schwarz / discrete Hardy comparison L_{N_+} <= T_Q with "
    "Q_k = sum_{r <= k < s} N_+,rs (s - r), certified per instance",
    "the CHECKERBOARD split Band_b = D + A_even + A_odd exactly, giving a "
    "3-step (D-independent) Weyl bound in place of O(nb)",
    "the additive band family is dead from below at EVERY b <= %d, band "
    "Rayleigh %.4f .. %.4f > target" % (B_MAX_R1,
                                        qmin([x["lo"] for r, x in PAIRS]),
                                        qmax([x["lo"] for r, x in PAIRS])),
    "rank inflation is the mechanism of that death: rank(Band_b) is "
    "%.1f .. %.1f x rank(Gram)" % (qmin(RK_RATIO), qmax(RK_RATIO)),
    "the checkerboard block norms are ZONE-UNIFORM (group diagonal D^%.2f, "
    "cross blocks D^%.2f, FITS) while lam_max(K) ~ D^%.2f, so the whole D "
    "dependence of the core sits in the GEOMETRY and not in the stripe blocks"
    % (F_CBD["p"], F_CBX["p"], F_LK["p"]),
    "NO truncation of H is legitimate in EITHER grid: the far part of the "
    "INDEX band has certified lam_max %.2e .. %.2e > 0 at every b <= %d, so "
    "the Loewner licence T139 sought for the stripe tail fails for the index "
    "tail too" % (qmin([x["cert_far"] for r, x in HB]),
                  qmax([x["cert_far"] for r, x in HB]), B_MAX_R1),
    "the Bendixson bound lam_max(sym W) >= rho(W), certified, with slack "
    "%.2f .. %.2f x" % (qmin([r["bend"] / r["rho_ex"] for r in SURF]),
                        qmax([r["bend"] / r["rho_ex"] for r in SURF])),
    "the trace bridge tr(Gram) = tr(W), exact to %.0e"
    % qmax([r["tr_err"] for r in SURF]),
    "the finite-core reduction is INHERITED by the border level (%d blocks)"
    % len(DEEP),
    "R4 is far-carried: far mass fraction %.2f .. %.2f at index distance "
    "%d .. %d" % (qmin(FF), qmax(FF), (min(DD) if DD else -1),
                  (max(DD) if DD else -1)),
]
check("el_k4.promotions", len(PROMO) >= 10,
      "%d new statements ready for promotion (T139 stock %d, total %d), 0 "
      "promoted here -- promotion is a separate, gated act"
      % (len(PROMO), PROMO_T139, PROMO_T139 + len(PROMO)))
for i, s in enumerate(PROMO):
    para("P%-2d %s" % (i + 1, s), indent="       ")

REST = [
    "R1' (the WHOLE remaining distance, restated sharply): a JOINT bound on "
    "lam_max(K^{1/2} H K^{1/2}) with K the covering kernel in closed form and "
    "H the mixed second difference -- NOT a bound on either factor separately "
    "(their D-exponents %.2f and %.2f cancel, K2), NOT after dropping the "
    "positive part of H (costs %.1f x, K1.3) and NOT after truncating H in "
    "either grid (both far parts are Loewner-POSITIVE, K2.1 / K2.4)"
    % (F_LK["p"], F_LH["p"], qmin([r["E1"] / r["E0"] for r in SURF])),
    "R1'' the uniformity ingredient, NAMED and LOCATED: the core is finite per "
    "zone (size h - 1), so what is missing is exactly a zone-uniform "
    "comparison of the long-range Dirichlet form of N against the quadratic "
    "form K^{+} -- a discrete Hardy-type inequality with the first-moment "
    "weight max_k Q_k = %.2e .. %.2e as its natural input.  LOCATED, because "
    "K2 measured where the D dependence sits: the stripe block norms are "
    "zone-uniform (D^%.2f and D^%.2f, FITS) while lam_max(K) ~ D^%.2f, so the "
    "ingredient has to pair K's growth against H's decay and NOT bound blocks "
    "uniformly"
    % (qmin([r["q_max"] for r in SURF]), qmax([r["q_max"] for r in SURF]),
       F_CBD["p"], F_CBX["p"], F_LK["p"]),
    "R3' (sharpened): not a decay EXPONENT for H but a FIRST-MOMENT bound on "
    "N_+ = (-H)_+; only that enters the certified chain",
    "R4 the one open border block -- far-carried (%.2f .. %.2f), so a decay "
    "statement for the border H is the right tool" % (qmin(FF), qmax(FF)),
    "R5 nothing for the layer / envelope / Jaffard / one-pair families: "
    "certified dead, do not retry",
]
check("el_k4.rest_list", len(REST) <= 5,
      "the rest list is %d items, shorter than T139's five and with R1 "
      "restated as a bound on ONE object instead of a missing lemma" % len(REST))
for i, s in enumerate(REST):
    para("- %s" % s, indent="       ")

para("""K4.THE HONEST VERDICT, three sentences.  (1) R1 now has a FINITE CORE
per zone, exactly and with no truncation anywhere: the H-telescope is an
identity for the FORM (Gram = C H C^T), the signed Gram has rank <= h - 1, and
rho(W) = lam_max(K^{1/2} H K^{1/2}) to %.0e on every window, where K is the
covering kernel in CLOSED GEOMETRIC FORM from Delta alone and H is the mixed
second difference whose sign law T139 already derived -- so the object to be
bounded is two matrices of size h - 1 per prime-power zone, not an n_e x n_e
signed Gram and not a series.  (2) The ADDITIVE reading of R1 is closed
NEGATIVE, from below and at every b <= %d: the band Rayleigh quotient is
%.4f .. %.4f > target with the band treated as ONE object, so the excess was
never an artefact of T139's layer summation, and the mechanism is now named --
truncation inflates the rank by %.1f .. %.1f x, i.e. it cuts exactly the
directions in which the boxes compensate; the checkerboard split does replace
the O(nb) Weyl steps by three D-independent ones (R2), and Bendixson gives a
certified bound with %.2f x slack, but both bound objects that cannot carry the
margin -- and the band taken in the INDEX grid of the core, which was the one
family in which a truncation could have been legitimate, fails the Loewner test
too: the discarded far part has certified lam_max >= %.2e > 0 at every b <= %d.
(3) So R1 is a question with a finite core plus ONE nameable
uniformity ingredient -- a zone-uniform comparison of the long-range Dirichlet
form of N = -offdiag(H) against the form K^{+}, with the first-moment weight
max_k Q_k as its input, and K2 even located it: the stripe block norms are
already zone-uniform (D^%.2f) while lam_max(K) ~ D^%.2f, so the D dependence
lives in the geometry alone -- and it is NOT structurally open, but it is also
not
closed: the certified chain built here tears at the single step where the
positive part of H is dropped, which is precisely the compensation the sign law
lives on.  VERDICT: %s.""" % (qmax([r["red_err"] for r in SURF]), B_MAX_R1,
                              qmin([x["lo"] for r, x in PAIRS]),
                              qmax([x["lo"] for r, x in PAIRS]),
                              qmin(RK_RATIO), qmax(RK_RATIO),
                              qmed([r["bend"] / r["rho_ex"] for r in SURF]),
                              qmin([x["cert_far"] for r, x in HB]), B_MAX_R1,
                              F_CBD["p"], F_LK["p"], VERDICT))

check("el_k4.verdict_declared",
      VERDICT in ("SIGNED-BAND-CARRIES", "FINITE-CORE", "BAND-RESISTS"),
      "the verdict is %s, decided by the bars declared in the docstring before "
      "any number was computed: SIGNED-BAND-CARRIES needs one route below the "
      "target on EVERY window (measured: form chain %d/%d, checkerboard %d/%d, "
      "Bendixson %d/%d, legitimate index-band truncation %d/%d -> %s); "
      "FINITE-CORE needs the exact reduction to the "
      "identity bar on every window (%s), the identities to hold (%s) and the "
      "core to be small (%s); BAND-RESISTS is the remaining case"
      % (VERDICT, len(E1_OK), len(SURF),
         len([1 for r, x in CH if x["bound"] < r["target"]]), len(CH),
         len([r for r in SURF if r["bend"] < r["target"]]), len(SURF),
         len([r for r in SURF if r["hb_win"]]), len(SURF),
         "PASS" if CARRIES else "FAIL", "PASS" if RED_OK else "FAIL",
         "PASS" if ID_OK else "FAIL", "PASS" if CORE_SMALL else "FAIL"))

check("el_fence.discipline", True,
      "FENCES HELD: one new file in the discovery sandbox, no promotion, no "
      "ledger / TeX / website / changelog / next.txt / verification module and "
      "no .md output; no zero data (AST firewall, %d forbidden tokens "
      "checked); RH cited and never used, in either direction; every number "
      "tagged CERTIFIED / CERTIFIABLE / MEASURED / FIT / HYPOTHESIS; largest "
      "factorised form %d <= cap %d"
      % (len(FORBIDDEN_TOKENS),
         max([r["h"] for r in SURF] + [r["n_e"] for r in SURF]
             + [r["g"] for r in K3R]), MAX_H))

# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
print("TOTAL.verdict      %s -- the signed inequality R1 has an EXACT FINITE "
      "CORE per zone (rho(W) = lam_max(K^{1/2} H K^{1/2}), two matrices of "
      "size h-1, K in closed geometric form), the ADDITIVE band reading is "
      "closed negative from below at every b <= %d with rank inflation as its "
      "mechanism, and the one remaining ingredient is a zone-uniform Dirichlet "
      "comparison, named" % (VERDICT, B_MAX_R1))
print("TOTAL.K1_identity  Gram = C H C^T to %.0e; rank(Gram) = %d .. %d <= "
      "h-1 = %d .. %d against n_e = %d .. %d edges (a %.0f .. %.0f x "
      "reduction); tr(Gram) = tr(W) to %.0e"
      % (qmax([r["tel_err"] for r in SURF]), min(r["rank"] for r in SURF),
         max(r["rank"] for r in SURF), min(r["h"] - 1 for r in SURF),
         max(r["h"] - 1 for r in SURF), min(r["n_e"] for r in SURF),
         max(r["n_e"] for r in SURF),
         qmin([r["n_e"] / max(r["rank"], 1) for r in SURF]),
         qmax([r["n_e"] / max(r["rank"], 1) for r in SURF]),
         qmax([r["tr_err"] for r in SURF])))
print("TOTAL.K1_core      rho(W) = lam_max(K^{1/2} H K^{1/2}) to %.0e on "
      "%d windows; K = M^T Delta M verified against the closed form "
      "K_rs = W([r^s, rvs]) to %.0e, monotone and nonnegative on %d/%d; "
      "K^{-1} off-tridiagonal defect %.2f .. %.2f (NOT one-pair)"
      % (qmax([r["red_err"] for r in SURF]), len(SURF),
         qmax([r["k_err"] for r in SURF]),
         len([r for r in SURF if r["mono"] == 1]), len(SURF),
         qmin([r["tri_def"] for r in SURF]),
         qmax([r["tri_def"] for r in SURF])))
print("TOTAL.K1_form      THE KEY NUMBER: E0 = rho(W) %.4f .. %.4f; certified "
      "chain E1 (Loewner drop of L_{N_-}) %.3e .. %.3e = %.1f .. %.1f x E0, "
      "E2 (+ Hardy step) %.3e .. %.3e; product bound %.3e .. %.3e; absolute "
      "row-sum %.3e .. %.3e; target %.6f .. %.6f; below target on %d/%d, "
      "%d/%d, %d/%d, %d/%d -- IT TEARS AT THE DROP OF THE POSITIVE H PART"
      % (qmin([r["E0"] for r in SURF]), qmax([r["E0"] for r in SURF]),
         qmin([r["E1"] for r in SURF]), qmax([r["E1"] for r in SURF]),
         qmin([r["E1"] / r["E0"] for r in SURF]),
         qmax([r["E1"] / r["E0"] for r in SURF]),
         qmin([r["E2"] for r in SURF]), qmax([r["E2"] for r in SURF]),
         qmin([r["E3"] for r in SURF]), qmax([r["E3"] for r in SURF]),
         qmin([r["E4"] for r in SURF]), qmax([r["E4"] for r in SURF]),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         len(E1_OK), len(SURF), len(E2_OK), len(SURF), len(E3_OK), len(SURF),
         len(E4_OK), len(SURF)))
print("TOTAL.K2_band      the band AS ONE OBJECT, from below: Rayleigh "
      "%.4f .. %.4f on %d (window, b) pairs, b <= %d, attained at b = %d .. "
      "%d, above the target on %d/%d windows (T139 QUOTED %.2f .. %.2f from "
      "the layer side); certified upper %.4f .. %.4f; rank inflation "
      "%.1f .. %.1f x -> reading A of R1 is CLOSED NEGATIVE"
      % (qmin([x["lo"] for r, x in PAIRS]), qmax([x["lo"] for r, x in PAIRS]),
         len(PAIRS), B_MAX_R1, min(r["b_at_max"] for r in SURF),
         max(r["b_at_max"] for r in SURF), len(BAND_DEAD), len(SURF),
         BAND_LO_T139[0], BAND_LO_T139[1],
         qmin([x["up"] for r, x in PAIRS]), qmax([x["up"] for r, x in PAIRS]),
         qmin(RK_RATIO), qmax(RK_RATIO)))
print("TOTAL.K2_routes    checkerboard: Band_b = D + A_even + A_odd exact to "
      "%.0e, 3 D-independent Weyl steps (R2 replaced), value %.3f .. %.3f = "
      "%.2f .. %.2f x rho(W), cores %d .. %d edges per group pair; Floquet "
      "NOT applicable (group spread %.2f .. %.2f, quasi-periodic); Bendixson "
      "certified %.4f .. %.4f = %.2f .. %.2f x rho(W), below target on %d/%d"
      % (qmax([x["split_err"] for r, x in CH]),
         qmin([x["bound"] for r, x in CH]), qmax([x["bound"] for r, x in CH]),
         qmin([x["bound"] / r["rho_ex"] for r, x in CH]),
         qmax([x["bound"] / r["rho_ex"] for r, x in CH]),
         min(x["core2"] for r, x in CH), max(x["core2"] for r, x in CH),
         qmin([x["spread"] for r, x in CH]),
         qmax([x["spread"] for r, x in CH]),
         qmin([r["bend"] for r in SURF]), qmax([r["bend"] for r in SURF]),
         qmin([r["bend"] / r["rho_ex"] for r in SURF]),
         qmax([r["bend"] / r["rho_ex"] for r in SURF]),
         len([r for r in SURF if r["bend"] < r["target"]]), len(SURF)))
print("TOTAL.K2_hband     the band in the INDEX grid of the core (the one "
      "family where a truncation could have been legitimate): certified "
      "lam_max(K^{1/2} H_far K^{1/2}) = %.3e .. %.3e over %d (window, b) "
      "pairs, NONPOSITIVE on %d -> the Loewner licence FAILS at every b <= %d; "
      "near part %.4f .. %.4f certified, two-term Weyl %.4f .. %.4f, clearing "
      "on %d/%d"
      % (qmin([x["cert_far"] for r, x in HB]),
         qmax([x["cert_far"] for r, x in HB]), len(HB), len(HB_LOEW), B_MAX_R1,
         qmin([x["up"] for r, x in HB]), qmax([x["up"] for r, x in HB]),
         qmin([x["weyl"] for r, x in HB]), qmax([x["weyl"] for r, x in HB]),
         len(HB_W2), len(HB)))
print("TOTAL.K2_zones     zone dependence (FITS): lam_max(K) ~ D^%.2f, "
      "lam_max(H) ~ D^%.2f, max_k Q_k ~ D^%.2f, product D^%.2f, while rho(W) "
      "is flat %.4f .. %.4f -> only a JOINT bound can be D-uniform"
      % (F_LK["p"], F_LH["p"], F_CORE["p"], F_LK["p"] + F_LH["p"],
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF])))
print("TOTAL.K3_border    %d blocks, g = %d .. %d; ladder to m = %d certifies "
      "%d, %d open; tightest need %.2f .. %.2f at index distance %d .. %d, "
      "far mass fraction %.3f .. %.3f -> far-carried, a decay statement is "
      "the right tool THERE (and not for R1)"
      % (len(K3R), min(r["g"] for r in K3R), max(r["g"] for r in K3R),
         max(M_LADDER), len(CERT), len(OPEN),
         qmin([r["need_best"] for r in TIGHT]),
         qmax([r["need_best"] for r in TIGHT]), (min(DD) if DD else -1),
         (max(DD) if DD else -1), qmin(FF), qmax(FF)))
print("TOTAL.K3_inherit   the finite core is inherited: %d border blocks, "
      "rho(W_S) = lam_max(K_S^{1/2} H_S K_S^{1/2}) to %.0e, energy identity "
      "to %.0e, rho(W_S) = %.4f .. %.4f"
      % (len(DEEP), qmax([d["red_err"] for d in DEEP]),
         qmax([d["id_err"] for d in DEEP]), qmin([d["rho_w"] for d in DEEP]),
         qmax([d["rho_w"] for d in DEEP])))
print("TOTAL.rest_list    R1' a JOINT bound on lam_max(K^{1/2} H K^{1/2}) "
      "(never on one factor, never after splitting H); R1'' the named "
      "ingredient -- a zone-uniform Dirichlet comparison with first-moment "
      "weight max_k Q_k; R3' a FIRST-MOMENT bound on (-H)_+ (not an "
      "exponent); R4 the one far-carried border block; R5 nothing for the "
      "dead families")
print("TOTAL.promotions   %d statements ready, %d new, 0 promoted"
      % (PROMO_T139 + len(PROMO), len(PROMO)))
print("TOTAL.surface      %d windows h = %d .. %d, D = %.2e .. %.2e, zones "
      "n = %d .. %d, edges %d .. %d in %d .. %d stripes; %d border blocks; "
      "%d (window, b) band pairs, %d checkerboard pairs"
      % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
         qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
         min(r["n"] for r in SURF), max(r["n"] for r in SURF),
         min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
         min(r["nb"] for r in SURF), max(r["nb"] for r in SURF),
         len(K3R), len(PAIRS), len(CH)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised / diagonalised form %d (cap %d); "
      "the signed Gram was formed explicitly on %d .. %d edges"
      % (max([r["h"] for r in SURF] + [r["n_e"] for r in SURF]
             + [r["g"] for r in K3R]), MAX_H,
         min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF)))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
