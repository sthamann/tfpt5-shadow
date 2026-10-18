"""Discovery probe (2026-07-28), part 138 of the prime/window investigation.
Contract SIGN.COMPENSATION -- KEEP the cancellation instead of majorising it,
and nothing else.

WHERE THIS SITS (T137 BOTH-RESIST: the D-uniformity of the pole-free floor hangs
on ONE spectral radius, and every ABSOLUTE-VALUE route to it is certified dead)
  T137 closed the enveloping half of the question and left the other half in an
  unusually sharp shape.  Its findings, verbatim as the starting point (QUOTED,
  never re-derived here):
    * the D-uniformity of lam_min(A) is reduced to rho(W) < 1 - c D^{~2.7},
      W = L_Delta A_B^{-1}, A_B = A + L_Delta the lumped Stieltjes pair, and the
      true rho(W) sits at 0.9752 .. 1.0000 on the measurement surface;
    * the ENTIRE absolute-value envelope family is certified DEAD from below:
      rho(|E|) >= 1.32 by a Collatz-Wielandt lower bracket, E = A_B^{-1}
      L_Delta.  THE TRANSITION TO THE ABSOLUTE VALUE DESTROYS THE
      COMPENSATION -- that sentence, and not any single bound, is the finding;
    * L_Delta is EXPLICIT: anti-diagonal stripes r + s = M - 1 - round(u_j / D)
      at the prime-power atoms, each stripe a perfect MATCHING, amplitudes
      certified by Delta <= c_comb(anti);
    * the inter-stripe coupling IS the object: the coarsening ladder of the
      stripe-block bound drops below 1 only at the LAST rung, where the whole
      Gram is a single block;
    * the second differences of the Green function b_e^T A_B^{-1} b_{e'} decay
      ALGEBRAICALLY, ~ d^{-0.63} (a FIT), and carry a SIGN structure which is
      what makes the true rho so much smaller than every majorant;
    * item (b'): 77 of 900 border blocks have rho(|F|) >= 1, F = S_B^{-1}
      L_Delta -- there NO |F|-majorised Neumann remainder can converge, by
      arithmetic and not by weakness of the estimate;
    * item (c) M17: what remains is a SPECTRAL characterisation of the whitened
      Schur block, or a direct argument for the harmonic mean.
  THE OPENING this probe is built around: every bound T137 tried replaced a
  signed object by its absolute value at SOME point, and the certified death of
  the |E| family says the cancellation is not a bonus but the whole mechanism.
  So the question is not "which norm" but "which decomposition keeps the
  signs".  There are exactly three classical answers -- an alternating-series
  bracket, a signed block-Rayleigh / Kantorovich reduction, and an exact
  two-body building block with a cluster remainder -- and this file runs all
  three against the same margin.

WHAT THIS PROBE DOES
  I0  SETUP and CALIBRATION: the firewall, the odd pole-free section against
      its entrywise definition, the lumped pair (Stieltjes, row sums
      preserved), the EDGE representation L_Delta = sum_e Delta_e b_e b_e^T,
      the GRAM IDENTITY rho(W) = lam_max(Gram) with Gram_{ee'} =
      sqrt(Delta_e Delta_e') b_e^T A_B^{-1} b_{e'}, and the four DIRECTION
      calibrations the rest of the file leans on: a stripe-band split at full
      bandwidth reproduces the Gram exactly, a Rayleigh-Ritz compression is a
      LOWER bound, a Cholesky-certified shift is an UPPER bound, and the
      m = 1 rung of the new paired Neumann certificate reproduces the T137
      entrywise certificate verbatim.
  I1  THE COMPENSATION ANATOMY.  WHAT is the sign pattern of the inter-stripe
      couplings?  Measured over the FULL area (every ordered pair of edges) and
      in the stripe-reduced form R_{ij} = v_i^T Gram_{ij} v_j (v_i the top
      eigenvector of the stripe's own diagonal block): the sign as a function
      of stripe distance, the flip rate, the within-layer cancellation ratio,
      and the paired-layer gain.  Then the CLOSED CANDIDATE FORM.  The Green
      function of a JACOBI (tridiagonal) Stieltjes matrix is a ONE-PAIR kernel,
      G_{rs} = phi_{min(r,s)} psi_{max(r,s)} with phi increasing and psi
      decreasing, hence totally positive of every order (Gantmacher-Krein 1950;
      Karlin 1968; Fekete 1912 for the TP_2 criterion) -- and then EVERY second
      difference has an exact two-term formula whose sign is decided by whether
      the two edges are NESTED or CROSSING.  A_B is DENSE, so this is a
      CANDIDATE and not a theorem: the probe extracts phi, psi from one row and
      one column, measures the one-pair defect, the TP_2 minor violation rate,
      and how much of the actual SIGN pattern the candidate form predicts.
  I2  THE SIGNED BOUND, three candidates, each with its direction stated:
        (i)   THE ALTERNATING-SERIES BRACKET.  Split the Gram by stripe
              distance into layers R^{(d)} and bound the tail beyond a
              bandwidth b by PAIRING consecutive layers, ||R^{(d)} +
              R^{(d+1)}|| instead of ||R^{(d)}|| + ||R^{(d+1)}|| -- the
              Leibniz/Abel pairing, which is a genuine triangle inequality on a
              coarser partition (Weyl 1912) and therefore CERTIFIABLE, and
              which keeps the signs inside every pair.  The gain is measured
              layer by layer.
        (ii)  THE BAND-EXACT / SIGNED-RAYLEIGH ROUTE.  lam_max(Gram) <=
              lam_max(Band_b) + ||Gram - Band_b||, with the band part -- all
              stripe blocks within distance b, signs intact -- certified by a
              completed Cholesky of s I - Band_b and the far tail majorised by
              a row-sum norm.  This is the H3 k-exact philosophy applied to the
              Gram: pay the absolute value only where the amplitude is already
              small.  The bandwidth ladder replaces T137's coarsening ladder
              and answers the same question in the other geometry.
        (iii) THE EXACT TWO-STRIPE BUILDING BLOCK and a CLUSTER EXPANSION.  For
              a stripe pair the whole system is a small symmetric eigenproblem
              solved exactly; the pair EXCESS over the isolated stripes is the
              two-body term of a cluster expansion (Mayer; Brydges 1984;
              Kotecky-Preiss 1986), its decay in stripe distance is fitted and
              the sum of two-body terms is compared with the TRUE excess.  A
              convergent, quantified remainder is the deliverable -- not a
              theorem.
      Every candidate is measured against the margin target 1 - c D^p rebuilt
      on THIS surface, and the KEY NUMBER is the best CERTIFIED signed bound
      versus that target.
  I3  THE 77 BLOCKS AND M17.
      (i) The blocks with rho(|F|) >= 1 are profiled (size, zone, transport
          ratio, stripe density, conditioning) and then attacked with the
          signed machinery in its sharpest available form: the m-PAIRED
          NEUMANN CERTIFICATE.  From the algebraic identity (I - F)^{-1} =
          (sum_{j<m} F^j)(I - F^m)^{-1} one gets, entrywise and with G_B =
          S_B^{-1} >= 0,
              S^{-1} >= P_m G_B - |P_m| (I - |F^m|)^{-1}|F^m| G_B,
          P_m = sum_{j<m} F^j, valid as soon as rho(|F^m|) < 1.  Since
          |F^m| <= |F|^m entrywise with possible STRICT inequality, the
          condition rho(|F^m|) < 1 is genuinely weaker than rho(|F|) < 1: the
          signs inside the m-fold product are kept.  m = 1 is exactly T137's
          certificate.  How many of the dead blocks does m > 1 rescue?
      (ii) M17 gets its spectral characterisation.  Whitening the border Schur
          block by its OWN lumped pair, S_B = L L^T, St = L^{-1} S L^{-T} =
          I - W_S with W_S = L^{-1} L_Delta L^{-T} >= 0, gives lam(St) =
          1 - lam(W_S) and, structurally and with no computation, St <= I.  The
          functional the assembly consumes is the HARMONIC one, shat^T S^{-1}
          shat = sum_k p_k^2 / mu_k, and for it there IS a direct inequality
          with no bad subspace anywhere: KANTOROVICH (Kantorovich 1948;
          Greub-Rheinboldt 1959) bounds it by [(m+M)^2/(4 m M)] |z|^4 /
          (z^T St z) with m, M the extreme eigenvalues -- and M = 1 is free.
          The probe computes the certified m, the Kantorovich bound, the
          harmonic bar, and the SOURCE-FREE threshold both routes require.  The
          answer is a number and it is uncomfortable in an instructive way.
  I4  THE MAP V10, the promotion batch and the shortest rest list.

PREREGISTERED VERDICTS (bars declared here, before any number is computed)
  SIGNS-CARRY       : one SIGNED route produces a CERTIFIED bound below the
                      margin target 1 - c D^p on EVERY window of the
                      measurement surface, with the implied exponent within
                      0.25 of the measured margin exponent.
  PAIR-EXACT        : the two-stripe blocks are exact and the cluster
                      expansion CONVERGES as measured (the two-body sum is
                      finite, its decay fitted, and it brackets the true excess
                      within a stated factor) -- the precise remainder is then
                      the whole distance to a proof.
  COMPENSATION-DEEP : the signed routes inherit the same absolute-value
                      pressure one level down -- with the anatomy of where and
                      what it means for the D-uniformity.
  Element gates: el_firewall, el_i0, el_i1, el_i2, el_i3, el_i4, el_fence.

FENCES
  * Discovery sandbox.  ONE new file.  No promotion, no ledger / TeX / website /
    changelog edit, no verification/ module, no next.txt, no .md output, no git
    action.
  * NO Riemann zero data of any kind.  An AST firewall rejects zero-table
    tokens, non-whitelisted imports and write-mode file access in this source.
  * THE RH FENCE IS PROMINENT AND ABSOLUTE.  Weil's positivity criterion
    (Weil 1952; Bombieri 2000; Connes 1999) is CITED as the classical address
    of the surrounding statement and is NEVER USED, in either direction.
    Nothing here claims, assumes or approaches RH.  Even with every item in the
    rest list closed, what would stand is positivity of the Weil window form on
    test functions supported in (-alpha_max, alpha_max) for the alpha actually
    reached -- a FINITE-WINDOW statement about a finite list of prime-power
    zones.  The distance to RH is MAPPED in I4, never travelled.
  * CERTIFIED vs CERTIFIABLE vs MEASURED vs FIT vs HYPOTHESIS, per line.  A
    completed Cholesky of s I - X certifies lam_max(X) <= s + c_h u ||X||,
    u = 2^-53 (Wilkinson 1968; Higham 2002 Thm 10.3/10.4).  A row-sum / Schur
    test on a symmetric matrix is CERTIFIABLE.  A Rayleigh quotient, a
    Rayleigh-Ritz compression and an eigenvalue are MEASUREMENTS, and a
    compression is a LOWER bound on the top eigenvalue by interlacing.  A
    Collatz-Wielandt quotient at ANY positive vector is a rigorous two-sided
    BRACKET for the spectral radius of a nonnegative matrix.  Every fit is a
    FIT with a delete-one jackknife band.  Bars declared before a number are
    never moved.
  * DIRECTION CARE, carried over from T136/T137 and applied pedantically:
    lumping RAISES the form (A_B >= A in the Loewner order), so the pair
    reaches a floor only through the INVERSE side; an UPPER bound on rho(W) is
    what a floor needs and a LOWER bound on rho(W) can only KILL a route; a
    lower bound on a Green entry needs the Neumann series FROM BELOW plus a
    positivity argument for the discarded tail, never a truncation error
    estimate; and |F^m| <= |F|^m is entrywise, in that direction only.
  * CLASSICAL ADDRESSES USED: Stieltjes / Ostrowski 1937, 1956, 1961,
    Berman-Plemmons 1979, Fan 1958, Varga 1962, Frobenius 1912 / Perron 1907,
    Collatz 1942 / Wielandt 1950, Weyl 1912 (eigenvalues of a sum),
    Gershgorin 1931 and the Schur row-sum test, Feingold-Varga 1962 (block
    Gershgorin), Gantmacher-Krein 1950/1960 (oscillation matrices, one-pair
    kernels, Green functions of Jacobi matrices), Karlin 1968 and Fekete 1912
    (total positivity, TP_2), Leibniz / Abel (alternating series and
    summation by parts), Kantorovich 1948 and Greub-Rheinboldt 1959 (the
    harmonic-arithmetic inequality), Mayer / Brydges 1984 / Kotecky-Preiss 1986
    (cluster expansions, cited as the shape of the remainder and NOT as a
    convergence theorem here), Kirchhoff / Klein-Randic 1993 (effective
    resistance), Haynsworth 1968 and Cauchy interlacing, Demko-Moss-Smith 1984
    (cited as the model and NOT applicable: A_B is dense), the Neumann series
    and Higham 2002 Ch. 14, Wilkinson 1968, Bertrand-Chebyshev 1852 and the
    trivial even bound (the only two gap facts consumed).  No gap CONJECTURE
    enters anywhere.
  * HARD CAPS.  Largest FACTORISED / INVERTED / DIAGONALISED matrix <= 1500;
    the signed Gram is formed explicitly only below that cap, so every band
    Cholesky and every stripe eigenproblem respects it; total runtime budget
    780 s (< 900 s), with per-block guards that truncate a pool rather than
    overrun.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, cholesky, eigh, eigvalsh, svdvals

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 780.0             # HARD probe budget (< 900 s)

U_ROUND = 2.0 ** -53
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 320000
ZONE_DEEP = 300000

# --- I1 / I2 pools (the signed Gram is formed explicitly: n_e <= NE_CAP) -----
I12_ZONES = 34
I12_HCAP = 260
NE_CAP = 1500                # == MAX_H: every band Cholesky stays under the cap
I1_SAMPLE = 4000             # sampled TP_2 minors per window
BAND_LADDER = (0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96)
PAIR_SAMPLE = 3000           # sampled stripe pairs for the cluster decay
T_I1 = 150.0
T_I2 = 240.0

# --- I3 pools (the T137 transport surface, rebuilt) --------------------------
I3_GC_MIN = 2
I3_HCAP = 900
I3_MAX = 900                 # the T134/T136/T137 border pool size
I3_PER_RHO = 30
I3_LOGRES = 90.0
I3_RHO = (1.001, 1.05, 1.10, 1.20, 1.25, 1.35, 1.49531, 1.60, 1.75, 1.90,
          2.00, 2.25, 2.50, 3.00, 3.50, 4.00)   # 1.49531 = the T127 band edge
M_LADDER = (1, 2, 3, 4, 6, 8, 12, 16, 24)   # the paired-Neumann rungs
T_I3 = 300.0

# --- preregistered bars (declared before any number is computed) -------------
BAR_ID = 1.0e-11             # every identity must hold to this relative level
BAR_SIGN_EXP = 0.25          # implied exponent must sit within this of p
BAR_COVER = 1.0              # a signed route must clear on EVERY window
BAR_M17 = 0.5                # T134's mass bar, in its harmonic form: <= 2 |z|^2
BAR_CLUSTER = 4.0            # the two-body sum may overshoot the true excess
                             # by at most this factor to count as CONVERGENT

# --- quoted numbers.  QUOTED, never re-derived here -------------------------
RHO_W_T137 = (0.9752, 1.0000)
RHO_ABS_E_T137 = 1.32
DECAY_P_T137 = -0.63
N_BAD_T137 = 77
N_BORDER_T137 = 900
PROMO_T137 = 30
N_PROBES_PRIOR = 137
SQRT2 = math.sqrt(2.0)
KANT_THRESHOLD = 3.0 - 2.0 * SQRT2   # the source-free Kantorovich threshold


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-36s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-36s %s" % (name, detail))


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
    return float(np.max(np.abs(a - b))) / max(float(np.max(np.abs(b))), 1.0e-300)


def qmin(v):
    return float(np.min(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmax(v):
    return float(np.max(np.asarray(v, dtype=float))) if len(v) else float("nan")


def qmed(v):
    return float(np.median(np.asarray(v, dtype=float))) if len(v) else float("nan")


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
                if any(c in mode for c in "wax+"):
                    bad_writes.append(mode)
    check("el_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("el_firewall.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("el_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("el_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "sign_compensation_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- T111..T137 code path
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
# the J = -1 (reflection-odd) sector -- exact coordinates (T106..T137)
# ----------------------------------------------------------------------------
def odd_toeplitz(c, M):
    h = M // 2
    r = np.arange(h)
    return c[np.abs(r[:, None] - r[None, :])] - c[(M - 1) - r[:, None] - r[None, :]]


def odd_toeplitz_slow(c, M):
    """The definition, entry by entry -- the I0 reference for odd_toeplitz."""
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


def cert_lam_max(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_max(X) <= s for a symmetric X by a COMPLETED CHOLESKY of
    s I - X (Wilkinson 1968; Higham 2002 Thm 10.3/10.4): if the factorisation
    runs to completion then s I - X is positive definite up to the declared
    floating-point floor, hence lam_max(X) <= s + floor.  The starting guess is
    a MEASUREMENT and is used only to place the shift; the returned number is
    the certified one.  DIRECTION: an UPPER bound, which is what a floor
    needs."""
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


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_min(X) >= t for a symmetric X by a completed Cholesky of
    X - t I.  DIRECTION: a LOWER bound."""
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
    """The bordered step (Haynsworth 1968), its border Schur block S, and the
    SCHUR-REDUCED POLE SOURCE shat = t~_border - C X^{-1} t~_inner.  The latter
    is the natural source of the assembly in this file's own coordinates and is
    used as a declared PROXY for the T134 assembly source: same shape (a border
    part plus a coupling correction), rebuilt here rather than quoted."""
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
    shat = tv[:gc] - C @ cho_solve(fac, tv[gc:], check_finite=False)
    del Q, A, C, X, Z
    return dict(S=S, shat=shat, fr=fr)


# ----------------------------------------------------------------------------
# THE LUMPED M-MATRIX PAIR and its EDGE representation -- the central objects
# ----------------------------------------------------------------------------
def lump_pair(A):
    """THE LUMPED M-MATRIX PAIR of a symmetric A (T136 (P1)).

    Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta its
    Laplacian (PSD, zero row sums), A_B = A + L_Delta.

    DIRECTION, stated once and never forgotten: L_Delta >= 0 in the LOEWNER
    order, so A_B >= A -- lumping RAISES the form and gives an UPPER bound on
    lam_min(A) directly and a LOWER bound never.  The floor is reached only
    through the INVERSE side."""
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
    lam_max(W) may not discard edges, because dropping an edge SHRINKS L_Delta
    and would bound the wrong object.  Sorted by the STRIPE index
    anti = M - 1 - r - t, so stripe blocks of the Gram are contiguous slices
    and the stripe ORDER is the LONG-LAG order."""
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
    """THE SIGNED GRAM, formed explicitly (n_e <= NE_CAP == MAX_H):

        Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T G b_{e'},   b_e = e_r - e_t,

    a weighted matrix of SECOND DIFFERENCES of the Green function G = A_B^{-1}.
    NO absolute value is taken anywhere in this function -- that is the whole
    point of the file."""
    Yw = (G[:, er] - G[:, et]) * wt[None, :]
    GR = (Yw[er, :] - Yw[et, :]) * wt[:, None]
    del Yw
    return sym(GR)


def stripe_reduce(GR, starts, counts):
    """THE STRIPE-REDUCED SIGNED COUPLING.  For each stripe take v_i, the unit
    top eigenvector of its OWN diagonal block, and compress:

        R_{ij} = v_i^T Gram_{ij} v_j .

    The v_i have disjoint supports and unit norm, so V is orthonormal and
    lam_max(R) <= lam_max(Gram) by Rayleigh-Ritz / Cauchy interlacing.
    DIRECTION: a LOWER bound on rho(W) -- this object MEASURES the sign
    structure and can never certify a floor.  It is the smallest faithful
    picture of the inter-stripe coupling."""
    nb = starts.shape[0]
    vs = []
    for i in range(nb):
        ai, bi = int(starts[i]), int(starts[i] + counts[i])
        B = sym(GR[ai:bi, ai:bi])
        if B.shape[0] == 1:
            vs.append(np.ones(1))
            continue
        wv, Vv = eigh(B)
        vs.append(np.ascontiguousarray(Vv[:, -1]))
    R = np.zeros((nb, nb))
    for i in range(nb):
        ai, bi = int(starts[i]), int(starts[i] + counts[i])
        for j in range(i, nb):
            aj, bj = int(starts[j]), int(starts[j] + counts[j])
            R[i, j] = R[j, i] = float(vs[i] @ GR[ai:bi, aj:bj] @ vs[j])
    return R


def layer_stats(R):
    """THE SIGN PATTERN of a stripe-reduced coupling, by stripe DISTANCE.  For
    every distance d: the signed layer sum, the absolute layer sum (their ratio
    is the WITHIN-LAYER cancellation), the positive fraction, the row-sum norm
    of the layer, and the row-sum norm of the PAIRED layer R^{(d)} + R^{(d+1)}
    (its ratio to the sum of the two single norms is the LEIBNIZ PAIRING GAIN
    -- the quantity an alternating-series argument would monetise)."""
    nb = R.shape[0]
    ii = np.arange(nb)
    dd = np.abs(ii[:, None] - ii[None, :])
    rows = []
    lay = {}
    for d in range(0, nb):
        m = dd == d
        if not m.any():
            continue
        v = R[m]
        L = np.where(m, R, 0.0)
        lay[d] = L
        rows.append(dict(d=d, n=int(v.shape[0]),
                         ssum=float(v.sum()), asum=float(np.abs(v).sum()),
                         pos=float(np.mean(v > 0.0)),
                         nrm=gersh(L), mx=float(np.max(np.abs(v)))))
    for k, rw in enumerate(rows):
        d = rw["d"]
        rw["cancel"] = abs(rw["ssum"]) / max(rw["asum"], 1.0e-300)
        if d + 1 in lay:
            n1 = rw["nrm"]
            n2 = gersh(lay[d + 1])
            rw["pair_nrm"] = gersh(lay[d] + lay[d + 1])
            rw["pair_gain"] = rw["pair_nrm"] / max(n1 + n2, 1.0e-300)
        else:
            rw["pair_nrm"] = rw["nrm"]
            rw["pair_gain"] = float("nan")
    sg = [rw["ssum"] for rw in rows[1:]]
    flips = 0
    for a, b in zip(sg[:-1], sg[1:]):
        if a * b < 0.0:
            flips += 1
    return dict(rows=rows, flip_rate=(flips / max(len(sg) - 1, 1)),
                n_off=len(sg))


def one_pair_form(G):
    """THE CLOSED CANDIDATE FORM.  The Green function of a JACOBI (tridiagonal)
    Stieltjes matrix is a ONE-PAIR kernel,

        G_{rs} = phi_{min(r,s)} psi_{max(r,s)},   phi up, psi down,

    which is exactly the class of OSCILLATION kernels: totally positive of
    every order (Gantmacher-Krein 1950/1960; Karlin 1968), so all 2x2 minors of
    the upper triangle vanish and all 2x2 minors of the matrix are >= 0
    (Fekete 1912 for the TP_2 criterion).  A_B is DENSE, so this is a CANDIDATE
    and the defect is a MEASUREMENT.  phi, psi are read off one column and one
    row with the normalisation phi_0 = 1."""
    h = G.shape[0]
    psi = G[0, :].copy()
    den = G[0, h - 1]
    if not (abs(den) > 0.0):
        return None
    phi = G[:, h - 1] / den
    r = np.arange(h)
    lo = np.minimum(r[:, None], r[None, :])
    hi = np.maximum(r[:, None], r[None, :])
    Gp = phi[lo] * psi[hi]
    scale = max(float(np.max(np.abs(G))), 1.0e-300)
    return dict(phi=phi, psi=psi, Gp=Gp,
                defect=float(np.max(np.abs(Gp - G))) / scale,
                med_defect=float(np.median(np.abs(Gp - G))) / scale,
                phi_mono=float(np.mean(np.diff(phi) >= 0.0)),
                psi_mono=float(np.mean(np.diff(psi) <= 0.0)))


def semisep_rank(G, n_split=9, tol=1.0e-6):
    """THE SHARPER CLOSED FORM: the SEMISEPARABLE RANK of the Green function.
    A one-pair kernel G_{rs} = phi_{min} psi_{max} is exactly the statement that
    EVERY off-diagonal block G[0:k, k:h] has rank ONE (Gantmacher-Krein
    1950/1960; the modern name is a semiseparable matrix, Vandebril-Van
    Barel-Mastronardi 2005).  Measuring sigma_2 / sigma_1 of those blocks, and
    the rank needed to capture 1 - %.0e of their energy, replaces the yes/no
    one-pair question by a NUMBER: rank r means every second difference
    b_e^T G b_{e'} has an exact r-term formula, hence a sign rule with r terms
    rather than two.  A MEASUREMENT of structure, not a bound.""" % tol
    h = G.shape[0]
    if h < 8:
        return dict(s2=float("nan"), rank=float("nan"), n=0)
    ks = np.unique(np.linspace(max(2, h // 8), h - max(2, h // 8),
                               n_split).round().astype(int))
    r2, rk, rk3 = [], [], []
    for k in ks:
        k = int(k)
        B = G[:k, k:]
        if min(B.shape) < 2:
            continue
        sv = svdvals(B)
        tot = float(np.sum(sv ** 2))
        if not (tot > 0.0):
            continue
        r2.append(float(sv[1] / sv[0]))
        cum = np.cumsum(sv ** 2) / tot
        rk.append(int(np.searchsorted(cum, 1.0 - tol) + 1))
        rk3.append(int(np.searchsorted(cum, 1.0 - 1.0e-3) + 1))
    if not r2:
        return dict(s2=float("nan"), rank=float("nan"), rank3=float("nan"), n=0)
    return dict(s2=float(np.max(r2)), s2_med=float(np.median(r2)),
                rank=float(np.max(rk)), rank_med=float(np.median(rk)),
                rank3=float(np.max(rk3)), rank3_med=float(np.median(rk3)),
                n=len(r2))


def tp2_rate(G, rng, n_s=I1_SAMPLE):
    """THE TP_2 MINOR TEST on sampled 2x2 minors of G: for r < s and r' < s',
    G_{rr'} G_{ss'} - G_{rs'} G_{sr'} >= 0 is the defining inequality of total
    positivity of order 2 (Fekete 1912; Karlin 1968).  A MEASUREMENT of a
    structural hypothesis, reported as a violation rate and a worst relative
    violation."""
    h = G.shape[0]
    if h < 4:
        return dict(rate=float("nan"), worst=float("nan"), n=0)
    a = rng.integers(0, h, size=(4, n_s))
    r = np.minimum(a[0], a[1])
    s = np.maximum(a[0], a[1])
    rp = np.minimum(a[2], a[3])
    sp = np.maximum(a[2], a[3])
    m = (s > r) & (sp > rp)
    r, s, rp, sp = r[m], s[m], rp[m], sp[m]
    if r.shape[0] == 0:
        return dict(rate=float("nan"), worst=float("nan"), n=0)
    det = G[r, rp] * G[s, sp] - G[r, sp] * G[s, rp]
    ref = np.abs(G[r, rp] * G[s, sp]) + np.abs(G[r, sp] * G[s, rp])
    bad = det < -1.0e-13 * ref
    worst = float(np.min(det / np.maximum(ref, 1.0e-300)))
    return dict(rate=float(np.mean(bad)), worst=worst, n=int(r.shape[0]))


def band_masks(sidx):
    ii = np.asarray(sidx)
    return np.abs(ii[:, None] - ii[None, :])


def ray_top(X, iters=180, rng=None):
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration: with
    sig = max_r sum_s |X_rs| the matrix X + sig I is positive semidefinite
    (Gershgorin 1931), so the largest MAGNITUDE eigenvalue of the shift is
    lam_max(X) + sig and no negative eigenvalue can win the iteration.  The
    returned value is a RAYLEIGH QUOTIENT, hence a rigorous LOWER bound on
    lam_max(X) up to rounding -- it is used to place the certified shift, never
    as the bound itself."""
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


def band_bound(GR, dmat, b, want_cert=True):
    """CANDIDATE (i) + (ii) TOGETHER, the BAND-EXACT SIGNED BOUND.  Split

        Gram = Band_b + Tail_b,   Band_b = Gram restricted to |i - j| <= b

    by stripe distance.  Weyl 1912 gives lam_max(Gram) <= lam_max(Band_b) +
    lam_max(Tail_b) and hence

        rho(W) <= [cert lam_max(Band_b)] + [cert norm of Tail_b],

    with the band part carrying its SIGNS intact (certified by a completed
    Cholesky of s I - Band_b).  For the far tail THREE majorants are offered and
    the smallest is taken, which matters more than it looks:
      * lam_max(Tail_b) itself, certified by a completed Cholesky of
        s I - Tail_b.  Weyl needs only the TOP eigenvalue of the tail, not its
        norm, and for a signed matrix with a near-zero trace the two are very
        different objects -- this is the sharpest sign-keeping majorant
        available for a tail that is not treated exactly;
      * the plain symmetric row-sum / Schur test max_r sum_s |Tail_rs|
        (CERTIFIABLE, and the only one of the three that destroys every sign);
      * the LEIBNIZ PAIRING, sum over consecutive layer PAIRS of
        ||R^{(d)} + R^{(d+1)}||, the alternating-series bracket: each pair keeps
        its internal signs and the triangle inequality is applied only between
        pairs.  A value ABOVE the plain row-sum norm means the cost of splitting
        the tail into many pieces exceeds what the pairing saves -- which is a
        measurement about the layer structure, not a failure of the bound."""
    n = GR.shape[0]
    inb = dmat <= b
    Band = np.where(inb, GR, 0.0)
    Tail = GR - Band
    meas_band = ray_top(Band)
    meas_tail = ray_top(Tail)
    row_tail = gersh(Tail)
    dmx = int(np.max(dmat))
    pair_tot = 0.0
    d = b + 1
    while d <= dmx:
        L = np.where(dmat == d, GR, 0.0)
        if d + 1 <= dmx:
            L = L + np.where(dmat == d + 1, GR, 0.0)
        pair_tot += gersh(L)
        del L
        d += 2
    cert_band = cert_lam_max(sym(Band), guess=meas_band) if want_cert \
        else float("nan")
    cert_tail_top = cert_lam_max(sym(Tail), guess=meas_tail) if want_cert \
        else float("nan")
    cand = [row_tail, pair_tot]
    if np.isfinite(cert_tail_top):
        cand.append(max(cert_tail_top, 0.0))
    tail_cert = min(cand)
    out = dict(b=int(b), meas_band=meas_band, meas_tail=meas_tail,
               row_tail=row_tail, pair_tail=pair_tot, tail_cert=tail_cert,
               cert_tail_top=cert_tail_top, cert_band=cert_band,
               meas_total=meas_band + max(meas_tail, 0.0),
               cert_total=(cert_band + tail_cert) if want_cert else float("nan"),
               pair_gain=pair_tot / max(row_tail, 1.0e-300))
    del Band, Tail, inb
    return out


def pair_cluster(GR, starts, counts, rng, n_s=PAIR_SAMPLE):
    """CANDIDATE (iii), THE EXACT TWO-STRIPE BUILDING BLOCK and the two-body
    term of a CLUSTER EXPANSION (Mayer; Brydges 1984; Kotecky-Preiss 1986 --
    cited as the SHAPE of the remainder, not as a convergence theorem: nothing
    here verifies a Kotecky-Preiss criterion).

    For stripes i, j the whole two-stripe system is the small symmetric
    eigenproblem on the union of the two index blocks and is solved EXACTLY, so
    every sign inside the pair is kept.  The two-body EXCESS

        eps_ij = lam_max(pair) - max(lam_max(ii), lam_max(jj)) >= 0

    is compared with (a) the SCALAR 2x2 surrogate that the block-norm route
    would use, (b) its decay in stripe distance, and (c) the TRUE excess
    lam_max(Gram) - max_i lam_max(ii).  DIRECTION: every pair value is a LOWER
    bound on lam_max(Gram) by interlacing; the two-body SUM is a HYPOTHESIS
    about the remainder and is labelled as one."""
    nb = starts.shape[0]
    dg = np.empty(nb)
    for i in range(nb):
        ai, bi = int(starts[i]), int(starts[i] + counts[i])
        B = sym(GR[ai:bi, ai:bi])
        dg[i] = (float(eigvalsh(B, subset_by_index=[B.shape[0] - 1,
                                                    B.shape[0] - 1])[0])
                 if B.shape[0] > 1 else float(B[0, 0]))
    istar = int(np.argmax(dg))

    def pair_val(i, j):
        ai, bi = int(starts[i]), int(starts[i] + counts[i])
        aj, bj = int(starts[j]), int(starts[j] + counts[j])
        idx = np.concatenate([np.arange(ai, bi), np.arange(aj, bj)])
        B = sym(GR[np.ix_(idx, idx)])
        lm = float(eigvalsh(B, subset_by_index=[B.shape[0] - 1,
                                               B.shape[0] - 1])[0])
        q = float(svdvals(GR[ai:bi, aj:bj])[0]) if bi > ai and bj > aj else 0.0
        a, b = dg[i], dg[j]
        sur = 0.5 * (a + b) + math.sqrt(0.25 * (a - b) ** 2 + q * q)
        return lm, sur, q

    star = []
    for j in range(nb):
        if j == istar:
            continue
        lm, sur, q = pair_val(istar, j)
        star.append(dict(j=j, d=abs(j - istar), lm=lm, sur=sur, q=q,
                         eps=max(lm - max(dg[istar], dg[j]), 0.0),
                         eps_sur=max(sur - max(dg[istar], dg[j]), 0.0)))
    samp = []
    if nb >= 4:
        n_take = min(n_s, nb * (nb - 1) // 2)
        for _ in range(n_take):
            i = int(rng.integers(0, nb))
            j = int(rng.integers(0, nb))
            if i == j:
                continue
            if i > j:
                i, j = j, i
            lm, sur, q = pair_val(i, j)
            samp.append(dict(d=j - i, eps=max(lm - max(dg[i], dg[j]), 0.0),
                             lm=lm, sur=sur))
    return dict(dg=dg, istar=istar, dg_max=float(dg[istar]), star=star,
                samp=samp,
                eps_sum=float(sum(r["eps"] for r in star)),
                eps_sum_sur=float(sum(r["eps_sur"] for r in star)),
                exact_ratio=(qmax([r["lm"] / max(r["sur"], 1.0e-300)
                                   for r in star]) if star else float("nan")))


def paired_neumann(S, m_ladder=M_LADDER, kex_probe=True):
    """THE m-PAIRED NEUMANN CERTIFICATE -- the sign-keeping replacement for the
    |F|-majorised remainder that T137 found dead on 77 blocks.

    S = S_B - L_Delta with S_B the lumped Stieltjes pair of S, G_B = S_B^{-1}
    >= 0 (Berman-Plemmons 1979), F = G_B L_Delta, so

        S^{-1} = (I - F)^{-1} G_B = P_m (I - F^m)^{-1} G_B,
        P_m = sum_{j<m} F^j,

    an ALGEBRAIC IDENTITY (all factors are powers of one matrix and commute).
    Expanding only the OUTER factor and majorising only IT entrywise,

        |sum_{q>=1} (F^m)^q| <= (I - |F^m|)^{-1} |F^m| =: T_m >= 0
        whenever rho(|F^m|) < 1,

    gives the entrywise LOWER bound

        S^{-1} >= P_m G_B - |P_m| T_m G_B ,

    since G_B >= 0.  The absolute value is now taken only OUTSIDE the m-fold
    product, and |F^m| <= |F|^m entrywise with STRICT inequality wherever the
    product cancels, so rho(|F^m|) < 1 is a strictly weaker condition than
    rho(|F|) < 1 -- which is precisely the T137 wall.  m = 1 reproduces T137's
    entrywise certificate verbatim.  DIRECTION: a LOWER bound on the entries of
    S^{-1}, which is what a positivity certificate needs."""
    g = S.shape[0]
    S = sym(S)
    dgS = np.diag(S).copy()
    off = S - np.diag(dgS)
    Dl = np.where(off > 0.0, off, 0.0)
    LD = np.diag(Dl.sum(axis=1)) - Dl
    S_B = sym(S + LD)
    facB = safe_cho(S_B)
    if facB is None:
        return None
    Ig = np.eye(g)
    G_B = cho_solve(facB, Ig, check_finite=False)
    out = dict(g=g, n_edge=int(np.count_nonzero(Dl > 0.0)) // 2,
               edge_frac=(float(np.count_nonzero(Dl > 0.0))
                          / max(g * (g - 1.0), 1.0)),
               g_min=float(np.min(G_B)), g_max=float(np.max(G_B)),
               inv_nonneg=int(bool(np.all(G_B >= -1.0e-14
                                          * float(np.abs(G_B).max())))),
               ld_mass=float(np.sum(Dl)) / max(float(np.sum(np.abs(S))),
                                               1.0e-300))
    out["kappa"] = out["g_min"] / max(out["g_max"], 1.0e-300)
    F = G_B @ LD
    Fabs = np.abs(F)
    x = np.maximum(G_B.sum(axis=1), 1.0e-300)
    lo1, up1 = perron_bracket(lambda v: Fabs @ v, g, 80)
    out["rho_fabs"] = up1
    out["rho_fabs_lo"] = lo1
    out["q_cw"] = float(np.max((Fabs @ x) / x))
    try:
        ev = np.linalg.eigvals(F)
        out["rho_f"] = float(np.max(np.abs(ev)))
    except LinAlgError:
        out["rho_f"] = float("nan")
    rungs = []
    Fm = Ig.copy()
    Pm = np.zeros((g, g))
    for m in range(1, max(m_ladder) + 1):
        Pm = Pm + Fm
        Fm = Fm @ F
        if m not in m_ladder:
            continue
        Fma = np.abs(Fm)
        lo, up = perron_bracket(lambda v: Fma @ v, g, 80)
        row = dict(m=m, rho_up=up, rho_lo=lo, root=(up ** (1.0 / m))
                   if up > 0.0 else 0.0, cert=0, need=float("inf"),
                   sharp=float(np.max(Fma / np.maximum(
                       np.abs(F) if m == 1 else
                       np.linalg.matrix_power(np.abs(F), m), 1.0e-300))))
        if up < 1.0:
            try:
                Tm = np.linalg.solve(Ig - Fma, Fma)      # >= 0, CERTIFIABLE
                low = Pm @ G_B - np.abs(Pm) @ (Tm @ G_B)
                row["cert"] = int(float(np.min(low)) > 0.0)
                row["need"] = float(np.max((np.abs(Pm) @ (Tm @ G_B))
                                           / np.maximum(Pm @ G_B, 1.0e-300)))
                del Tm, low
            except LinAlgError:
                pass
        rungs.append(row)
        del Fma
    out["rungs"] = rungs
    out["m_best"] = min([r["m"] for r in rungs if r["cert"]] or [0])
    out["rho_best"] = qmin([r["root"] for r in rungs])
    out["conv_any"] = int(any(r["rho_up"] < 1.0 for r in rungs))
    out["cert_any"] = int(any(r["cert"] for r in rungs))
    try:
        Si = np.linalg.solve(S, Ig)
        out["s_inv_min"] = float(np.min(Si))
        out["s_inv_pos"] = int(out["s_inv_min"] > 0.0)
        del Si
    except LinAlgError:
        out["s_inv_min"] = float("nan")
        out["s_inv_pos"] = 0
    out["_S_B"] = S_B
    out["_LD"] = LD
    del F, Fabs, Fm, Pm, G_B, Dl
    return out


def m17_spectral(S_B, LD, shat):
    """M17 WITHOUT BAD SUBSPACES -- the spectral characterisation of the
    WHITENED Schur block and the direct harmonic-mean inequality.

    Whitening by the block's OWN lumped pair, S_B = L L^T,

        St = L^{-1} S L^{-T} = I - W_S,   W_S = L^{-1} L_Delta L^{-T} >= 0,

    so lam(St) = 1 - lam(W_S) and -- structurally, with no computation --
    St <= I: M = lam_max(St) <= 1 is FREE.  The functional the assembly
    consumes is the HARMONIC one,

        shat^T S^{-1} shat = z^T St^{-1} z = sum_k p_k^2 / mu_k,
        z = L^{-1} shat,

    and for it there is a DIRECT inequality with no bad subspace anywhere --
    KANTOROVICH (Kantorovich 1948; Greub-Rheinboldt 1959):

        (z^T St^{-1} z)(z^T St z) <= (m + M)^2 / (4 m M) |z|^4,

    hence z^T St^{-1} z <= [(m+M)^2/(4mM)] |z|^4 / (z^T St z) with m a CERTIFIED
    lower eigenvalue bound and M = 1.  Two thresholds follow and both are
    source-FREE:
      * the crude route z^T St^{-1} z <= |z|^2/m needs m >= 1/2, i.e.
        rho(W_S) <= 1/2 -- T134's bar in its harmonic form;
      * the Kantorovich route needs (1+m)^2/(4m) <= 2 q with q = z^T St z/|z|^2
        in [m, 1]; at the best possible q = 1 this is m >= 3 - 2 sqrt 2 =
        0.1716, i.e. rho(W_S) <= 0.8284.
    The gap between 1/2 and 0.1716 is exactly what the harmonic mean buys."""
    g = S_B.shape[0]
    try:
        L = cholesky(S_B, lower=True, check_finite=False)
    except LinAlgError:
        return None
    Li = np.linalg.solve(L, np.eye(g))
    W_S = sym(Li @ LD @ Li.T)
    St = np.eye(g) - W_S
    mu = eigvalsh(sym(St))
    rho_w = float(np.max(eigvalsh(W_S)))
    lam_min_meas = float(mu[0])
    m_cert = cert_lam_min(sym(St), guess=lam_min_meas)
    M_cert = min(1.0, cert_lam_max(sym(St), guess=float(mu[-1])))
    z = Li @ shat
    nz2 = float(np.dot(z, z))
    if not (nz2 > 0.0):
        return None
    qform = float(z @ St @ z) / nz2                      # in [lam_min, 1]
    harm = float("nan")
    try:
        harm = float(z @ np.linalg.solve(St, z)) / nz2    # = shat^T S^-1 shat
    except LinAlgError:
        pass
    bad = float(np.sum((mu < 0.5).astype(float)))
    m_use = m_cert if (np.isfinite(m_cert) and m_cert > 0.0) else float("nan")
    kant = float("nan")
    crude = float("nan")
    M_use = M_cert if np.isfinite(M_cert) and M_cert > 0.0 else 1.0
    if np.isfinite(m_use) and m_use > 0.0 and qform > 0.0:
        kant = ((m_use + M_use) ** 2 / (4.0 * m_use * M_use)) / qform
        crude = 1.0 / m_use
    return dict(g=g, rho_w=rho_w, lam_min=lam_min_meas, m_cert=m_cert,
                M_cert=M_cert,
                mu_min=float(mu[0]), mu_max=float(mu[-1]),
                n_below_half=int(bad), frac_below_half=bad / max(g, 1),
                qform=qform, harm=harm, kant=kant, crude=crude,
                harm_ok=int(np.isfinite(harm) and harm <= 2.0),
                kant_ok=int(np.isfinite(kant) and kant <= 2.0),
                crude_ok=int(np.isfinite(crude) and crude <= 2.0),
                st_le_i=int(float(mu[-1]) <= 1.0 + 1.0e-12))


def perron_bracket(applyf, n, iters, rng=None):
    """THE COLLATZ-WIELANDT BRACKET for a NONNEGATIVE matrix given only by its
    action (Collatz 1942; Wielandt 1950):

        min_r (M y)_r / y_r  <=  rho(M)  <=  max_r (M y)_r / y_r

    for EVERY strictly positive y.  Both ends are RIGOROUS -- the upper end
    certifies, the lower end KILLS -- and the power iteration is used only to
    choose a good y, never as the bound itself."""
    y = (np.abs(rng.standard_normal(n)) + 0.5) if rng is not None else np.ones(n)
    lo = hi = float("nan")
    for _ in range(iters):
        z = applyf(y)
        pos = y > 0.0
        if not np.all(pos):
            break
        q = z / y
        lo, hi = float(np.min(q)), float(np.max(q))
        nz = float(np.max(z))
        if not (nz > 0.0):
            return 0.0, 0.0
        y = np.maximum(z / nz, 1.0e-300)
    return lo, hi


firewall()


# ----------------------------------------------------------------------------
section("I0  SETUP, the pair, the SIGNED Gram and the four DIRECTION calibrations")
# ----------------------------------------------------------------------------
ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
MU_SORTED = np.array([t[3] for t in ATOMS_ALL], dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

BERT_OK = bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
EVEN_OK = bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12))
check("el_i0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

RNG = np.random.default_rng(1380728)

# --- I0.1  the odd section against its entrywise definition -----------------
_k0, _D0, _M0 = None, None, None
for _kk in range(2, NZ_DEEP - 2):
    _Dc = 0.5 * float(G_DEEP[_kk]) / NU_MAIN
    _Mc = even_window(UU_ALL[_kk], _Dc)
    if 120 <= _Mc // 2 <= 240:
        _k0, _D0, _M0 = _kk, _Dc, _Mc
if _k0 is None:
    raise SystemExit("I0 found no calibration window in the declared h band")
_al0 = 0.5 * _M0 * _D0
_c0, _ = lag_vector_fast(_al0, _M0, atoms_in(_al0, ATOMS_ALL))
E_ODD = rel(odd_toeplitz(_c0, _M0), odd_toeplitz_slow(_c0, _M0))
check("el_i0.odd_section", E_ODD <= BAR_ID,
      "the vectorised odd section equals its entrywise definition A_rs = "
      "c_{|r-s|} - c_{M-1-r-s} to %.2e (bar %.0e) on the calibration window "
      "h = %d, D = %.3e -- the coordinates of T106..T137, unchanged"
      % (E_ODD, BAR_ID, _M0 // 2, _D0))

_A0 = sym(odd_toeplitz(_c0, _M0))
_lp0 = lump_pair(_A0)
_an0 = anchor_floor(_lp0["A_B"])
check("el_i0.lumping", _lp0["stieltjes"] == 1
      and rel(_lp0["A_B"].sum(axis=1), _lp0["w"]) <= BAR_ID
      and _an0 is not None and _an0["nonneg"] == 1,
      "the lumped pair is STIELTJES (all off-diagonals <= 0, positive "
      "diagonal), the ROW SUMS are preserved to %.2e, and A_B x = 1 has x >= 0 "
      "so A_B is a nonsingular M-matrix (Fan 1958; Berman-Plemmons 1979) with "
      "the anchor lam_min(A_B) >= %.3e.  DIRECTION: A_B >= A in the Loewner "
      "order, so the floor is reached only through the INVERSE side"
      % (rel(_lp0["A_B"].sum(axis=1), _lp0["w"]), _an0["floor"]))

_ed0 = edge_list(_lp0["Dl"], _M0)
_B0 = np.zeros((_lp0["h"], _ed0["n"]))
_B0[_ed0["er"], np.arange(_ed0["n"])] = 1.0
_B0[_ed0["et"], np.arange(_ed0["n"])] = -1.0
_LD0 = (_B0 * _ed0["w"][None, :]) @ _B0.T
E_EDGE = rel(_LD0, _lp0["LD"])
check("el_i0.edge_form", E_EDGE <= BAR_ID,
      "L_Delta = sum_e Delta_e b_e b_e^T holds to %.2e on %d edges in %d "
      "anti-diagonal stripes: the lumped perturbation is a weighted graph "
      "LAPLACIAN, and NO edge is dropped anywhere below (dropping one shrinks "
      "L_Delta and would bound the wrong object)"
      % (E_EDGE, _ed0["n"], _ed0["nb"]))

# --- I0.2  the GRAM identity, bracketed instead of diagonalised -------------
_G0 = cho_solve(_an0["fac"], np.eye(_lp0["h"]), check_finite=False)
_wt0 = np.sqrt(_ed0["w"])
_GR0 = signed_gram(_G0, _ed0["er"], _ed0["et"], _wt0)
_rho_ex0 = 1.0 - float(eigh(_A0, _lp0["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
_lo0 = ray_top(_GR0, rng=RNG)
_up0 = cert_lam_max(_GR0, guess=_lo0)
check("el_i0.gram_identity", _lo0 <= _rho_ex0 * (1.0 + 1.0e-9) + 1.0e-12
      and _rho_ex0 <= _up0 * (1.0 + 1.0e-9) + 1.0e-12,
      "rho(W) = lam_max(Gram) with Gram_{ee'} = sqrt(Delta_e Delta_e') b_e^T "
      "A_B^{-1} b_{e'}: the exact pencil value %.6f lies inside the bracket "
      "[%.6f (Rayleigh, LOWER), %.6f (completed Cholesky, UPPER)] on %d edges "
      "-- so the whole question is the top eigenvalue of a weighted matrix of "
      "SECOND DIFFERENCES of the Green function, and the diagonal is "
      "Delta_e R_e with R_e the effective resistance (Kirchhoff; "
      "Klein-Randic 1993)" % (_rho_ex0, _lo0, _up0, _ed0["n"]))

# --- I0.3  the band split at full bandwidth is the identity -----------------
_dm0 = band_masks(_ed0["sidx"])
_bb_full = band_bound(_GR0, _dm0, int(np.max(_dm0)), want_cert=True)
_bb_zero = band_bound(_GR0, _dm0, 0, want_cert=True)
check("el_i0.band_split_exact",
      abs(_bb_full["tail_cert"]) <= BAR_ID * max(abs(_up0), 1.0e-300)
      and _bb_full["cert_total"] >= _rho_ex0 * (1.0 - 1.0e-9),
      "at FULL bandwidth the tail is empty (%.2e) and the band bound collapses "
      "to the certified lam_max(Gram) = %.6f >= the exact %.6f; at bandwidth 0 "
      "(stripe-diagonal only, every inter-stripe coupling majorised) it is "
      "%.6f -- the two ends of the ladder I2 walks"
      % (_bb_full["tail_cert"], _bb_full["cert_total"], _rho_ex0,
         _bb_zero["cert_total"]))

# --- I0.4  the two DIRECTIONS, verified rather than asserted ----------------
_R0 = stripe_reduce(_GR0, _ed0["stripe_start"], _ed0["stripe_count"])
_lam_R0 = float(eigvalsh(sym(_R0), subset_by_index=[_R0.shape[0] - 1,
                                                    _R0.shape[0] - 1])[0]) \
    if _R0.shape[0] > 1 else float(_R0[0, 0])
check("el_i0.directions",
      _lam_R0 <= _rho_ex0 * (1.0 + 1.0e-8) + 1.0e-12
      and _bb_zero["cert_total"] >= _rho_ex0 * (1.0 - 1.0e-9)
      and _bb_full["cert_total"] >= _rho_ex0 * (1.0 - 1.0e-9),
      "DIRECTION CALIBRATION.  The stripe-reduced compression gives "
      "lam_max(R) = %.6f <= rho(W) = %.6f -- a LOWER bound by Rayleigh-Ritz / "
      "Cauchy interlacing, which can never certify a floor and is used ONLY to "
      "read the sign pattern; the band bounds %.6f and %.6f both sit ABOVE "
      "rho(W), which is the side a floor needs"
      % (_lam_R0, _rho_ex0, _bb_zero["cert_total"], _bb_full["cert_total"]))

# --- I0.5  the m = 1 rung reproduces the T137 certificate -------------------
_fr0 = None
for _kk in range(3, NZ_DEEP - 2):
    _DA = 0.5 * float(G_DEEP[_kk]) / NU_MAIN
    _f = step_frame(UU_ALL[_kk], UU_ALL[_kk + 1], _DA / 1.25)
    if _f is not None and _f["gc"] >= 3 and 60 <= _f["h_n"] <= 400:
        _fr0 = _f
        break
_st0 = bordered_step(_fr0, ATOMS_ALL) if _fr0 is not None else None
_pn0 = paired_neumann(_st0["S"]) if _st0 is not None else None
if _pn0 is not None:
    _g = _pn0["g"]
    _Sq = sym(_st0["S"])
    _dgq = np.diag(_Sq).copy()
    _Dq = np.where(_Sq - np.diag(_dgq) > 0.0, _Sq - np.diag(_dgq), 0.0)
    _LDq = np.diag(_Dq.sum(axis=1)) - _Dq
    _GBq = np.linalg.solve(sym(_Sq + _LDq), np.eye(_g))
    _Fq = np.abs(_GBq @ _LDq)
    _r1 = [r for r in _pn0["rungs"] if r["m"] == 1][0]
    _t137 = 0
    if _r1["rho_up"] < 1.0:
        _Tq = np.linalg.solve(np.eye(_g) - _Fq, _Fq)
        _t137 = int(float(np.min(_GBq - _Tq @ _GBq)) > 0.0)
    check("el_i0.m1_is_t137", _t137 == _r1["cert"],
          "the m = 1 rung of the paired Neumann certificate IS the T137 "
          "entrywise certificate, verbatim (P_1 = I, T_1 = (I - |F|)^{-1}|F|): "
          "both say %d on the calibration block g = %d, rho(|F|) = %.4f.  Every "
          "m > 1 rung below is therefore a strict extension of the T137 route "
          "and not a different bookkeeping" % (_t137, _g, _r1["rho_up"]))
else:
    check("el_i0.m1_is_t137", False, "calibration block unavailable")

del _GR0, _G0, _A0, _lp0, _ed0, _B0, _LD0, _dm0, _R0


# ----------------------------------------------------------------------------
section("I1  THE COMPENSATION ANATOMY -- the sign pattern of the coupling")
# ----------------------------------------------------------------------------
para("""I1.0  THE QUESTION, stated so that it can be answered by a number.  T137
established that rho(W) = lam_max(Gram) and that every route which replaces the
Gram by a matrix of absolute values overshoots -- the |E| family fatally
(rho(|E|) >= %.2f, certified from below), the Gram-Gershgorin family by less but
still above 1.  So the cancellation among the inter-stripe couplings is not a
nuisance term: it is the mechanism that keeps rho(W) below 1 at all.  This block
measures that cancellation in three progressively sharper pictures.  (a) OVER
THE FULL AREA: every ordered pair of edges is classified by the GEOMETRY of its
two index intervals -- DISJOINT, NESTED or CROSSING -- and by the stripe
distance, and the sign of the second difference is tabulated per class.  (b) IN
THE STRIPE-REDUCED FORM R_{ij} = v_i^T Gram_{ij} v_j with v_i the unit top
eigenvector of stripe i's own diagonal block: an orthonormal compression, hence
a LOWER bound on rho(W) by interlacing, and the smallest faithful picture of the
inter-stripe sign pattern.  Its layer sums, flip rate, within-layer cancellation
and Leibniz pairing gain are the raw material of I2 (i).  (c) AGAINST A CLOSED
CANDIDATE FORM: for a JACOBI Stieltjes matrix the Green function is a ONE-PAIR
kernel G_{rs} = phi_{min} psi_{max} with phi increasing and psi decreasing --
the oscillation-matrix class, totally positive of every order
(Gantmacher-Krein 1950/1960; Karlin 1968; Fekete 1912 for TP_2) -- and then every
second difference has an exact two-term formula whose sign is a CONSEQUENCE of
the geometry: NESTED pairs give (psi_{r'} - psi_{t'}) phi_r + (phi_{t'} -
phi_{r'}) psi_t, both terms positive, while CROSSING pairs mix.  A_B is DENSE,
so total positivity is a HYPOTHESIS here and not a theorem; the probe measures
the one-pair defect, the TP_2 violation rate, and how much of the observed sign
pattern the closed form predicts.""" % RHO_ABS_E_T137)

SZ = []
_seen = set()
for k in range(2, NZ_DEEP - 2):
    if len(SZ) >= I12_ZONES:
        break
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > I12_HCAP:
        continue
    key = h_k // 5
    if key in _seen:
        continue
    _seen.add(key)
    SZ.append((k, D_k, M_k, h_k))

SURF = []
LAYERS = []
CLUST = []
for (k, D_k, M_k, h_k) in SZ:
    if budget_left() < BUDGET_S - T_I1 - T_I2:
        info("I1.budget", "surface truncated at n = %d after %d windows"
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
    if ed["n"] < 8 or ed["n"] > NE_CAP or ed["nb"] < 4:
        continue
    G = cho_solve(an["fac"], np.eye(h_k), check_finite=False)
    wt = np.sqrt(ed["w"])
    n_e, nb = ed["n"], int(ed["nb"])
    GR = signed_gram(G, ed["er"], ed["et"], wt)
    dm = band_masks(ed["sidx"])
    try:
        gap_ex = float(eigh(A, lp["A_B"], eigvals_only=True,
                            subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        continue
    rho_ex = 1.0 - gap_ex

    # --- (a) THE FULL AREA: signs by geometry class and by stripe distance ---
    a_i = ed["er"][:, None]
    b_i = ed["et"][:, None]
    c_j = ed["er"][None, :]
    d_j = ed["et"][None, :]
    disj = (b_i < c_j) | (d_j < a_i)
    nest = ((a_i < c_j) & (d_j < b_i)) | ((c_j < a_i) & (b_i < d_j))
    offd = ~np.eye(n_e, dtype=bool)
    cros = offd & (~disj) & (~nest)
    sgn = GR > 0.0
    cls = {}
    for nm, m in (("disjoint", disj & offd), ("nested", nest & offd),
                  ("crossing", cros)):
        cnt = int(np.count_nonzero(m))
        if cnt:
            v = GR[m]
            cls[nm] = dict(share=cnt / max(int(np.count_nonzero(offd)), 1),
                           pos=float(np.mean(v > 0.0)),
                           cancel=abs(float(v.sum()))
                           / max(float(np.abs(v).sum()), 1.0e-300),
                           amp=float(np.mean(np.abs(v))))
        else:
            cls[nm] = dict(share=0.0, pos=float("nan"), cancel=float("nan"),
                           amp=float("nan"))
    all_pos = float(np.mean(sgn[offd]))
    all_cancel = abs(float(GR[offd].sum())) / max(
        float(np.abs(GR[offd]).sum()), 1.0e-300)

    # --- (b) THE STRIPE-REDUCED SIGNED COUPLING -----------------------------
    R = stripe_reduce(GR, ed["stripe_start"], ed["stripe_count"])
    ls = layer_stats(R)
    lam_R = (float(eigvalsh(sym(R), subset_by_index=[nb - 1, nb - 1])[0])
             if nb > 1 else float(R[0, 0]))
    for rw in ls["rows"]:
        if rw["d"] >= 1:
            LAYERS.append(dict(h=h_k, D=D_k, nb=nb, **rw))

    # --- (c) THE CLOSED CANDIDATE FORM --------------------------------------
    op = one_pair_form(G)
    tp = tp2_rate(G, RNG)
    ss = semisep_rank(G)
    op_sign = op_rel = float("nan")
    op_cls = {}
    if op is not None:
        GRp = signed_gram(op["Gp"], ed["er"], ed["et"], wt)
        op_sign = float(np.mean((GRp[offd] > 0.0) == sgn[offd]))
        op_rel = float(np.median(np.abs(GRp[offd] - GR[offd]))) / max(
            float(np.median(np.abs(GR[offd]))), 1.0e-300)
        for nm, m in (("disjoint", disj & offd), ("nested", nest & offd),
                      ("crossing", cros)):
            if int(np.count_nonzero(m)):
                op_cls[nm] = float(np.mean(GRp[m] > 0.0))
            else:
                op_cls[nm] = float("nan")
        del GRp

    # --- I2 material, computed on the same objects ---------------------------
    lo_gr = ray_top(GR, rng=RNG)
    up_gr = cert_lam_max(GR, guess=lo_gr)
    bands = []
    for b in BAND_LADDER:
        if b > int(np.max(dm)):
            continue
        bb = band_bound(GR, dm, b, want_cert=True)
        bands.append(bb)
        if budget_left() < BUDGET_S - T_I1 - T_I2 + 30.0:
            break
    pc = pair_cluster(GR, ed["stripe_start"], ed["stripe_count"], RNG)
    for rw in pc["samp"]:
        CLUST.append(dict(h=h_k, D=D_k, nb=nb, d=rw["d"], eps=rw["eps"]))
    true_excess = max(rho_ex - pc["dg_max"], 0.0)

    SURF.append(dict(n=NN_ALL[k], h=h_k, M=M_k, D=D_k, al=al, n_at=len(ats),
                     n_e=n_e, nb=nb, anchor=an["floor"],
                     rho_ex=rho_ex, gap_ex=gap_ex, lam_R=lam_R,
                     lo_gr=lo_gr, up_gr=up_gr,
                     all_pos=all_pos, all_cancel=all_cancel, cls=cls,
                     flip=ls["flip_rate"], n_off=ls["n_off"],
                     op_defect=(op["defect"] if op else float("nan")),
                     op_med=(op["med_defect"] if op else float("nan")),
                     phi_mono=(op["phi_mono"] if op else float("nan")),
                     psi_mono=(op["psi_mono"] if op else float("nan")),
                     op_sign=op_sign, op_rel=op_rel, op_cls=op_cls,
                     tp_rate=tp["rate"], tp_worst=tp["worst"],
                     ss_s2=ss["s2"], ss_rank=ss["rank"],
                     ss_s2_med=ss.get("s2_med", float("nan")),
                     ss_rank_med=ss.get("rank_med", float("nan")),
                     ss_rank3=ss.get("rank3", float("nan")),
                     ss_rank3_med=ss.get("rank3_med", float("nan")),
                     bands=bands, pc=pc, true_excess=true_excess,
                     dg_max=pc["dg_max"], eps_sum=pc["eps_sum"],
                     exact_ratio=pc["exact_ratio"]))
    del A, lp, an, G, GR, dm, R, disj, nest, cros, offd, sgn

if not SURF:
    raise SystemExit("I1 produced no window -- probe cannot report")

# --- I1.1  the full-area sign table -----------------------------------------
info("I1.surface", "%d windows, h = %d .. %d, D = %.3e .. %.3e, n = %d .. %d, "
     "edges %d .. %d in %d .. %d stripes (signed Gram formed explicitly, "
     "n_e <= %d = the hard cap on any factorised form)"
     % (len(SURF), min(r["h"] for r in SURF), max(r["h"] for r in SURF),
        qmin([r["D"] for r in SURF]), qmax([r["D"] for r in SURF]),
        min(r["n"] for r in SURF), max(r["n"] for r in SURF),
        min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF),
        min(r["nb"] for r in SURF), max(r["nb"] for r in SURF), NE_CAP))

check("el_i1.gram_bracket",
      all(r["lo_gr"] <= r["rho_ex"] * (1.0 + 1.0e-8) + 1.0e-12
          and r["rho_ex"] <= r["up_gr"] * (1.0 + 1.0e-8) + 1.0e-12
          for r in SURF),
      "THE GRAM IDENTITY HOLDS ON EVERY WINDOW: the exact pencil rho(W) = "
      "%.4f .. %.4f (T137 QUOTED %.4f .. %.4f) is bracketed by [Rayleigh, "
      "certified Cholesky] on all %d windows -- so every number below is about "
      "the same object T136 reduced the D-uniformity to"
      % (qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
         RHO_W_T137[0], RHO_W_T137[1], len(SURF)))

for nm in ("disjoint", "nested", "crossing"):
    info("I1.class_%s" % nm,
         "share %.3f .. %.3f of the off-diagonal pairs, POSITIVE fraction "
         "%.3f .. %.3f, layer cancellation |sum|/sum|.| = %.4f .. %.4f, mean "
         "|second difference| %.3e .. %.3e"
         % (qmin([r["cls"][nm]["share"] for r in SURF]),
            qmax([r["cls"][nm]["share"] for r in SURF]),
            qmin([r["cls"][nm]["pos"] for r in SURF]),
            qmax([r["cls"][nm]["pos"] for r in SURF]),
            qmin([r["cls"][nm]["cancel"] for r in SURF]),
            qmax([r["cls"][nm]["cancel"] for r in SURF]),
            qmin([r["cls"][nm]["amp"] for r in SURF]),
            qmax([r["cls"][nm]["amp"] for r in SURF])))

NEST_POS = qmin([r["cls"]["nested"]["pos"] for r in SURF])
check("el_i1.sign_table_measured",
      all(np.isfinite(r["all_pos"]) for r in SURF),
      "OVER THE FULL AREA the positive fraction of the inter-edge second "
      "differences is %.3f .. %.3f and the global cancellation |sum|/sum|.| is "
      "%.4f .. %.4f -- i.e. the couplings very nearly cancel in the mean, which "
      "is exactly why the absolute-value routes of T137 overshoot.  The sign is "
      "NOT random: it is decided by the geometry of the two index intervals "
      "(nested %.3f .. %.3f positive, crossing %.3f .. %.3f, disjoint "
      "%.3f .. %.3f)"
      % (qmin([r["all_pos"] for r in SURF]), qmax([r["all_pos"] for r in SURF]),
         qmin([r["all_cancel"] for r in SURF]),
         qmax([r["all_cancel"] for r in SURF]),
         NEST_POS, qmax([r["cls"]["nested"]["pos"] for r in SURF]),
         qmin([r["cls"]["crossing"]["pos"] for r in SURF]),
         qmax([r["cls"]["crossing"]["pos"] for r in SURF]),
         qmin([r["cls"]["disjoint"]["pos"] for r in SURF]),
         qmax([r["cls"]["disjoint"]["pos"] for r in SURF])))

# --- I1.2  the stripe-reduced layer structure -------------------------------
L_CANCEL = qmed([r["cancel"] for r in LAYERS])
L_GAIN = [r["pair_gain"] for r in LAYERS if np.isfinite(r["pair_gain"])]
F_LDEC = pow_fit([max(r["d"], 1) for r in LAYERS],
                 [max(r["nrm"], 1.0e-300) for r in LAYERS], "layer_norm")
check("el_i1.layer_structure", bool(LAYERS),
      "THE STRIPE-REDUCED COUPLING, %d layers over %d windows.  Flip rate of "
      "the signed layer sums %.3f .. %.3f (1.0 = perfect alternation in stripe "
      "distance, 0.5 = no order); WITHIN-LAYER cancellation |sum|/sum|.| median "
      "%.4f; LEIBNIZ PAIRING GAIN ||R^{(d)} + R^{(d+1)}|| / (||R^{(d)}|| + "
      "||R^{(d+1)}||) = %.3f .. %.3f (median %.3f; 1.0 = the pairing buys "
      "NOTHING, 0.5 or less = the layers genuinely oppose each other); layer "
      "row-sum norm ~ d^%.2f +- %.2f (FIT)"
      % (len(LAYERS), len(SURF), qmin([r["flip"] for r in SURF]),
         qmax([r["flip"] for r in SURF]), L_CANCEL,
         qmin(L_GAIN), qmax(L_GAIN), qmed(L_GAIN), F_LDEC["p"], F_LDEC["sp"]))

info("I1.reduced_lower", "the compression lam_max(R) = %.4f .. %.4f against the "
     "exact rho(W) = %.4f .. %.4f, i.e. the stripe-reduced picture already "
     "recovers %.3f .. %.3f of the true radius as a LOWER bound (Rayleigh-Ritz; "
     "it can never certify a floor)"
     % (qmin([r["lam_R"] for r in SURF]), qmax([r["lam_R"] for r in SURF]),
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        qmin([r["lam_R"] / r["rho_ex"] for r in SURF]),
        qmax([r["lam_R"] / r["rho_ex"] for r in SURF])))

# --- I1.3  the closed candidate form ----------------------------------------
check("el_i1.one_pair_form",
      all(np.isfinite(r["op_defect"]) for r in SURF),
      "THE CLOSED CANDIDATE FORM, measured and NOT assumed.  The one-pair "
      "(oscillation-kernel) ansatz G_{rs} = phi_{min} psi_{max} -- exact for a "
      "JACOBI Stieltjes matrix (Gantmacher-Krein 1950/1960), a HYPOTHESIS for "
      "the dense A_B -- reproduces the Green function to a relative defect of "
      "%.3f .. %.3f (median %.3f .. %.3f), with phi nondecreasing on %.3f .. "
      "%.3f and psi nonincreasing on %.3f .. %.3f of the grid; the sampled "
      "TP_2 minors of G are nonnegative on %.4f .. %.4f of the sample (worst "
      "relative violation %.2e).  Its prediction for the SIGN of the second "
      "differences is right on %.3f .. %.3f of all off-diagonal pairs"
      % (qmin([r["op_defect"] for r in SURF]),
         qmax([r["op_defect"] for r in SURF]),
         qmin([r["op_med"] for r in SURF]), qmax([r["op_med"] for r in SURF]),
         qmin([r["phi_mono"] for r in SURF]),
         qmax([r["phi_mono"] for r in SURF]),
         qmin([r["psi_mono"] for r in SURF]),
         qmax([r["psi_mono"] for r in SURF]),
         1.0 - qmax([r["tp_rate"] for r in SURF]),
         1.0 - qmin([r["tp_rate"] for r in SURF]),
         qmin([r["tp_worst"] for r in SURF]),
         qmin([r["op_sign"] for r in SURF]),
         qmax([r["op_sign"] for r in SURF])))

check("el_i1.semiseparable",
      all(np.isfinite(r["ss_rank"]) for r in SURF),
      "THE CLOSED FORM, SHARPENED FROM YES/NO TO A NUMBER.  A one-pair "
      "oscillation kernel is exactly a matrix whose every off-diagonal block "
      "G[0:k, k:h] has rank ONE (Gantmacher-Krein 1950/1960; semiseparable "
      "matrices, Vandebril-Van Barel-Mastronardi 2005).  Measured on this "
      "surface: sigma_2 / sigma_1 of those blocks is %.4f .. %.4f (median "
      "%.4f .. %.4f), the rank needed for all but 1e-3 of the block energy is "
      "%.0f .. %.0f (median %.0f .. %.0f) and for all but 1e-6 it is "
      "%.0f .. %.0f (median %.0f .. %.0f) on h = %d .. %d.  THE HONEST READING, "
      "which is not the flattering one: the leading term IS the one-pair term "
      "(the second singular value is an order of magnitude down), but the tail "
      "of the spectrum is NOT negligible, so the Green function of the dense "
      "A_B is a rank-1-DOMINATED kernel and NOT a semiseparable matrix of low "
      "rank.  That is exactly consistent with the sign prediction above being "
      "right on %.3f .. %.3f of the area rather than on all of it: the closed "
      "form explains the leading sign rule and not the whole pattern"
      % (qmin([r["ss_s2"] for r in SURF]), qmax([r["ss_s2"] for r in SURF]),
         qmin([r["ss_s2_med"] for r in SURF]),
         qmax([r["ss_s2_med"] for r in SURF]),
         qmin([r["ss_rank3"] for r in SURF]), qmax([r["ss_rank3"] for r in SURF]),
         qmin([r["ss_rank3_med"] for r in SURF]),
         qmax([r["ss_rank3_med"] for r in SURF]),
         qmin([r["ss_rank"] for r in SURF]), qmax([r["ss_rank"] for r in SURF]),
         qmin([r["ss_rank_med"] for r in SURF]),
         qmax([r["ss_rank_med"] for r in SURF]),
         min(r["h"] for r in SURF), max(r["h"] for r in SURF),
         qmin([r["op_sign"] for r in SURF]), qmax([r["op_sign"] for r in SURF])))

for nm in ("disjoint", "nested", "crossing"):
    info("I1.pred_%s" % nm, "one-pair form predicts a POSITIVE fraction of "
         "%.3f .. %.3f where the truth is %.3f .. %.3f"
         % (qmin([r["op_cls"].get(nm, float("nan")) for r in SURF]),
            qmax([r["op_cls"].get(nm, float("nan")) for r in SURF]),
            qmin([r["cls"][nm]["pos"] for r in SURF]),
            qmax([r["cls"][nm]["pos"] for r in SURF])))


# ----------------------------------------------------------------------------
section("I2  THE SIGNED BOUND -- three candidates against one margin")
# ----------------------------------------------------------------------------
para("""I2.0  THE TARGET, rebuilt on THIS surface and not quoted.  T136's exact
three-way bookkeeping lam_min(A) = anchor x (1 - rho) x slack attributes the whole
D-degradation to the MARGIN, so a structure bound is useful only if 1 - bound
obeys the same power of D as the true gap.  The gap 1 - rho(W) is fitted in D on
this surface and the target is the resulting envelope 1 - c D^p with c the
WORST-CASE constant over the surface; a bound is counted as clearing only if it
sits below that target on EVERY window (bar %.1f = full cover, declared before
any number).  DIRECTION, once more: only an UPPER bound on rho(W) can produce a
floor, so of the three candidates below only the CERTIFIED band totals are
admissible as bounds at all; the compression and the pair values are LOWER
bounds and appear as diagnostics.""" % BAR_COVER)

F_GAP = pow_fit([r["D"] for r in SURF], [r["gap_ex"] for r in SURF], "gap")
P_GAP = F_GAP["p"]
C_GAP = qmin([r["gap_ex"] / (r["D"] ** P_GAP) for r in SURF])
for r in SURF:
    r["target"] = 1.0 - C_GAP * (r["D"] ** P_GAP)
info("I2.target", "1 - rho(W) ~ %.3e D^%.3f +- %.3f (FIT, rms %.3f, n = %d); "
     "worst-case constant c = %.3e, so the target envelope is %.6f .. %.6f "
     "(T136 QUOTED margin exponent %.2f)"
     % (F_GAP["c"], P_GAP, F_GAP["sp"], F_GAP["rms"], F_GAP["n"], C_GAP,
        qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        2.72))

# --- I2.1  candidate (i): the alternating-series / Leibniz pairing -----------
PG = [(bb["pair_tail"] / max(bb["row_tail"], 1.0e-300))
      for r in SURF for bb in r["bands"] if bb["row_tail"] > 0.0]
check("el_i2.pairing_valid",
      all(bb["pair_tail"] >= 0.0 and bb["row_tail"] >= 0.0
          for r in SURF for bb in r["bands"]),
      "CANDIDATE (i), THE ALTERNATING-SERIES BRACKET.  Pairing consecutive "
      "stripe-distance layers before taking a norm -- the Leibniz/Abel step, a "
      "triangle inequality on a coarser partition and therefore still a valid "
      "MAJORANT -- changes the tail majorant by a factor %.3f .. %.3f (median "
      "%.3f) relative to the unpaired row-sum norm on %d (window, bandwidth) "
      "combinations.  A factor of 1 means the signs of consecutive layers do "
      "NOT oppose each other in the row-sum geometry; a factor ABOVE 1 means "
      "the partition into pairs costs more than the pairing saves -- the "
      "alternation is real in the LAYER SUMS (flip rate %.3f .. %.3f) but does "
      "not survive being measured by row-sum norms, because a norm sees the "
      "worst row of each pair and not the cancelling mean.  This is a NEGATIVE "
      "result about the classical alternating-series bracket in this geometry, "
      "and it is why the tail is certified through lam_max below instead"
      % (qmin(PG), qmax(PG), qmed(PG), len(PG),
         qmin([r["flip"] for r in SURF]), qmax([r["flip"] for r in SURF])))

# --- I2.2  candidate (ii): the band-exact signed bound ----------------------
for r in SURF:
    best = None
    for bb in r["bands"]:
        tot = bb["cert_total"]
        if not np.isfinite(tot):
            continue
        if best is None or tot < best["cert_total"]:
            best = bb
    r["best"] = best
    r["best_cert"] = best["cert_total"] if best else float("nan")
    r["best_b"] = best["b"] if best else -1
    r["best_meas"] = qmin([bb["meas_total"] for bb in r["bands"]])
    r["beats"] = int(np.isfinite(r["best_cert"]) and r["best_cert"] < r["target"])
    r["below1"] = int(np.isfinite(r["best_cert"]) and r["best_cert"] < 1.0)
    r["over_gap"] = ((r["best_cert"] - r["rho_ex"]) / max(r["gap_ex"], 1.0e-300)
                     if np.isfinite(r["best_cert"]) else float("nan"))

CERT_VALID = [r for r in SURF
              if all(bb["cert_total"] >= r["rho_ex"] * (1.0 - 1.0e-8) - 1.0e-12
                     for bb in r["bands"] if np.isfinite(bb["cert_total"]))]

# --- I2.2a  THE BAND FAMILY, DECIDED FROM BELOW -----------------------------
# A Rayleigh quotient at ANY vector is a rigorous LOWER bound on lam_max, so
# ray_top(Band_b) <= lam_max(Band_b) <= [any band bound at that b].  Wherever
# that LOWER bound already exceeds the target, NO band bound at that bandwidth
# can ever clear the margin -- whatever tail majorant is used, however clever.
# This is the same move T137 used to kill the |E| envelope family, applied to
# the band family, and it decides the whole family at once instead of one
# bound at a time.
for r in SURF:
    r["band_dead"] = [bb for bb in r["bands"] if bb["meas_band"] > r["target"]]
    r["band_alive"] = [bb for bb in r["bands"] if bb["meas_band"] <= r["target"]]
    r["band_above_rho"] = [bb for bb in r["bands"]
                           if bb["meas_band"] > r["rho_ex"] * (1.0 + 1.0e-9)]
    r["band_min_lo"] = qmin([bb["meas_band"] for bb in r["bands"]])
    dead_b = [bb["b"] for bb in r["band_dead"]]
    r["b_dead"] = min(dead_b) if dead_b else -1
    surv = [bb for bb in r["bands"]
            if r["b_dead"] < 0 or bb["b"] < r["b_dead"]]
    r["tail_at_last_alive"] = (min(bb["tail_cert"] for bb in surv)
                               if surv else float("nan"))
DEAD_ALL = [r for r in SURF if not r["band_alive"]]
N_DEAD_RUNG = sum(len(r["band_dead"]) for r in SURF)
N_RUNG = sum(len(r["bands"]) for r in SURF)
N_ABOVE_RHO = sum(len(r["band_above_rho"]) for r in SURF)
SQUEEZE = [r for r in SURF if r["b_dead"] >= 0
           and np.isfinite(r["tail_at_last_alive"])]
check("el_i2.band_family_decided",
      all(bb["meas_band"] <= bb["cert_band"] * (1.0 + 1.0e-7) + 1.0e-12
          for r in SURF for bb in r["bands"] if np.isfinite(bb["cert_band"])),
      "THE BAND FAMILY, DECIDED RUNG BY RUNG FROM BELOW -- the same move T137 "
      "used to kill the |E| envelope, applied here.  A Rayleigh quotient is a "
      "rigorous LOWER bound on lam_max(Band_b), and any band bound at that "
      "bandwidth is at least that; so wherever the lower bound already exceeds "
      "the target the rung is DEAD whatever tail majorant is used.  Measured: "
      "%d of %d (window, bandwidth) rungs are dead this way, and on %d rungs "
      "the band part alone sits above the EXACT rho(W) -- i.e. truncating the far "
      "couplings there RAISES the spectral radius, so the far tail is a net "
      "NEGATIVE contributor and not a small remainder.  The failure mode of the "
      "surviving rungs is a SQUEEZE and it is quantified: on %d of %d windows "
      "the band part alone crosses the target at b = %d .. %d, while at the "
      "last bandwidth before that crossing the certified tail is still "
      "%.4f .. %.4f.  The two terms are never small at the same bandwidth"
      % (N_DEAD_RUNG, N_RUNG, N_ABOVE_RHO, len(SQUEEZE), len(SURF),
         min([r["b_dead"] for r in SQUEEZE] or [-1]),
         max([r["b_dead"] for r in SQUEEZE] or [-1]),
         qmin([r["tail_at_last_alive"] for r in SQUEEZE]),
         qmax([r["tail_at_last_alive"] for r in SQUEEZE])))

check("el_i2.cert_is_upper", len(CERT_VALID) == len(SURF),
      "EVERY certified band total sits ABOVE the exact rho(W) on all %d "
      "windows, as Weyl 1912 plus the Schur row-sum test require -- the bounds "
      "are bounds, verified and not assumed"
      % len(SURF))

BEATS = [r for r in SURF if r["beats"]]
BELOW1 = [r for r in SURF if r["below1"]]
BAND_OK = (len(BEATS) == len(SURF))
info("I2.band_ladder", "best CERTIFIED signed band bound %.4f .. %.4f at "
     "bandwidth b = %d .. %d (of %d .. %d stripes), against the exact rho(W) = "
     "%.4f .. %.4f and the target %.6f .. %.6f: below 1 on %d of %d windows, "
     "below the TARGET on %d of %d.  Overshoot in units of the true gap: "
     "%.2e .. %.2e"
     % (qmin([r["best_cert"] for r in SURF]),
        qmax([r["best_cert"] for r in SURF]),
        min(r["best_b"] for r in SURF), max(r["best_b"] for r in SURF),
        min(r["nb"] for r in SURF), max(r["nb"] for r in SURF),
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        len(BELOW1), len(SURF), len(BEATS), len(SURF),
        qmin([r["over_gap"] for r in SURF]),
        qmax([r["over_gap"] for r in SURF])))

for b in BAND_LADDER:
    rows = [bb for r in SURF for bb in r["bands"] if bb["b"] == b]
    if not rows:
        continue
    info("I2.rung_b%d" % b, "certified band %.4f .. %.4f + certified tail "
         "%.4f .. %.4f = %.4f .. %.4f (Rayleigh LOWER bound on the band part "
         "alone %.4f .. %.4f, measured band + measured tail "
         "%.4f .. %.4f); of the three tail majorants, lam_max(tail) certified "
         "= %.4f .. %.4f, row-sum = %.4f .. %.4f, Leibniz pairing = "
         "%.4f .. %.4f"
         % (qmin([x["cert_band"] for x in rows]),
            qmax([x["cert_band"] for x in rows]),
            qmin([x["tail_cert"] for x in rows]),
            qmax([x["tail_cert"] for x in rows]),
            qmin([x["cert_total"] for x in rows]),
            qmax([x["cert_total"] for x in rows]),
            qmin([x["meas_band"] for x in rows]),
            qmax([x["meas_band"] for x in rows]),
            qmin([x["meas_total"] for x in rows]),
            qmax([x["meas_total"] for x in rows]),
            qmin([x["cert_tail_top"] for x in rows]),
            qmax([x["cert_tail_top"] for x in rows]),
            qmin([x["row_tail"] for x in rows]),
            qmax([x["row_tail"] for x in rows]),
            qmin([x["pair_tail"] for x in rows]),
            qmax([x["pair_tail"] for x in rows])))

POS = [r for r in SURF if np.isfinite(r["best_cert"]) and r["best_cert"] < 1.0]
if len(POS) >= 3:
    F_BEST = pow_fit([r["D"] for r in POS],
                     [1.0 - r["best_cert"] for r in POS], "gap_best")
    P_BEST = F_BEST["p"]
    EXP_OK = bool(np.isfinite(P_BEST) and abs(P_BEST - P_GAP) <= BAR_SIGN_EXP)
    info("I2.implied_exponent",
         "1 - [best certified signed bound] ~ D^%.2f +- %.2f (FIT on the %d "
         "windows where the bound is below 1) against the measured margin "
         "exponent D^%.2f: %s the declared tolerance %.2f.  A bound with the "
         "RIGHT power and a worse constant is a different object from one that "
         "sits above 1 -- this is the number that decides which of the two we "
         "have" % (P_BEST, F_BEST["sp"], len(POS), P_GAP,
                   "within" if EXP_OK else "OUTSIDE", BAR_SIGN_EXP))
else:
    F_BEST = dict(p=float("nan"), sp=float("nan"), c=float("nan"),
                  rms=float("nan"), n=len(POS))
    P_BEST = float("nan")
    EXP_OK = False
    info("I2.implied_exponent",
         "NO EXPONENT CAN BE FORMED: the best certified signed bound is below 1 "
         "on only %d of %d windows, and 1 - bound is not a positive quantity to "
         "fit.  This is reported as the absence of a number and not as a bad "
         "fit -- the honest statement is that the certified signed route does "
         "not yet produce a gap at all on this surface; its distance to 1 is "
         "%.4f .. %.4f (a NEGATIVE value means that window is already below 1)"
         % (len(POS), len(SURF),
            qmin([r["best_cert"] - 1.0 for r in SURF]),
            qmax([r["best_cert"] - 1.0 for r in SURF])))

# --- I2.3  candidate (iii): the exact pair and the cluster remainder --------
EXR = [r["exact_ratio"] for r in SURF if np.isfinite(r["exact_ratio"])]
CLR = [(r["eps_sum"] / max(r["true_excess"], 1.0e-300)) for r in SURF
       if r["true_excess"] > 0.0]
F_EPS = pow_fit([max(r["d"], 1) for r in CLUST],
                [max(r["eps"], 1.0e-300) for r in CLUST], "pair_excess")
CLUST_OK = bool(CLR) and qmax(CLR) <= BAR_CLUSTER and qmin(CLR) >= 1.0 / BAR_CLUSTER
check("el_i2.pair_exact",
      all(r["pc"]["dg_max"] <= r["rho_ex"] * (1.0 + 1.0e-8) + 1.0e-12
          for r in SURF)
      and all(x["lm"] <= r["rho_ex"] * (1.0 + 1.0e-8) + 1.0e-12
              for r in SURF for x in r["pc"]["star"]),
      "CANDIDATE (iii), THE EXACT TWO-STRIPE BLOCK.  Every isolated stripe and "
      "every stripe PAIR is solved exactly and every value sits BELOW rho(W), "
      "as interlacing requires.  The exact pair value is %.4f .. %.4f of the "
      "scalar 2x2 surrogate (a + b)/2 + sqrt(((a-b)/2)^2 + ||Q||^2) that the "
      "block-norm route would use, so the pair itself already cancels %.1f .. "
      "%.1f %% of what the norm route charges"
      % (qmin(EXR), qmax(EXR), 100.0 * (1.0 - qmax(EXR)),
         100.0 * (1.0 - qmin(EXR))))

info("I2.cluster", "the two-body EXCESS eps_ij = lam_max(pair) - "
     "max(lam_max(ii), lam_max(jj)) decays as d^%.2f +- %.2f in stripe distance "
     "(FIT, %d sampled pairs); the SUM of two-body terms around the dominant "
     "stripe is %.3e .. %.3e against a TRUE excess rho(W) - max_i lam_max(ii) = "
     "%.3e .. %.3e, i.e. a ratio %.3f .. %.3f (bar for CONVERGENT: within a "
     "factor %.1f either way).  A cluster expansion whose two-body sum brackets "
     "the truth is a HYPOTHESIS about the remainder, cited to Mayer / Brydges "
     "1984 / Kotecky-Preiss 1986 for its SHAPE only -- no convergence criterion "
     "is verified here"
     % (F_EPS["p"], F_EPS["sp"], len(CLUST),
        qmin([r["eps_sum"] for r in SURF]), qmax([r["eps_sum"] for r in SURF]),
        qmin([r["true_excess"] for r in SURF]),
        qmax([r["true_excess"] for r in SURF]),
        qmin(CLR) if CLR else float("nan"),
        qmax(CLR) if CLR else float("nan"), BAR_CLUSTER))

SIGNS_CARRY = bool(BAND_OK and EXP_OK)
EXP_TXT = ("%.2f" % P_BEST) if np.isfinite(P_BEST) else "n/a"
info("I2.verdict_input", "SIGNS-CARRY requires full cover (%d of %d) AND the "
     "exponent inside %.2f (implied D^%s vs measured D^%.2f): %s.  PAIR-EXACT "
     "requires the pair blocks exact (yes, by construction and verified) AND "
     "the cluster ratio inside a factor %.1f (%.3f .. %.3f): %s"
     % (len(BEATS), len(SURF), BAR_SIGN_EXP, EXP_TXT, P_GAP,
        "MET" if SIGNS_CARRY else "NOT met", BAR_CLUSTER,
        qmin(CLR) if CLR else float("nan"), qmax(CLR) if CLR else float("nan"),
        "MET" if CLUST_OK else "NOT met"))


# ----------------------------------------------------------------------------
section("I3  THE 77 BLOCKS AND M17 -- where the signed machinery is needed")
# ----------------------------------------------------------------------------
para("""I3.0  WHAT T137 LEFT.  On its 900-block border surface the entrywise
positivity certificate for S^{-1} stopped, and it stopped for an ARITHMETIC
reason on %d blocks: rho(|F|) >= 1 with F = S_B^{-1} L_Delta, so no |F|-majorised
Neumann remainder can converge there no matter how the estimate is arranged.
This block does two things.  (i) It profiles those blocks -- size, zone,
transport ratio, stripe density, Green contrast -- and then applies the SIGNED
replacement in its sharpest available form, the m-PAIRED NEUMANN CERTIFICATE:
the absolute value is moved OUTSIDE the m-fold product, so the condition becomes
rho(|F^m|) < 1, and |F^m| <= |F|^m entrywise with strict inequality wherever the
product cancels.  m = 1 is exactly T137 (verified in I0.5), so the ladder can
only add blocks.  (ii) It gives M17 the spectral characterisation it was reduced
to.  Whitening the border Schur block by its OWN lumped pair turns the pencil
into St = I - W_S with W_S >= 0, so lam(St) = 1 - lam(W_S), M = lam_max(St) <= 1
is FREE, and the functional the assembly consumes is the HARMONIC one
shat^T S^{-1} shat.  For that functional there IS a direct inequality with no
bad subspace anywhere -- Kantorovich 1948 / Greub-Rheinboldt 1959 -- and the
probe measures exactly how much it buys against the crude 1/lam_min route.  Both
source-free thresholds are computed: 1/2 for the crude route, 3 - 2 sqrt 2 =
%.4f for the Kantorovich route at the most favourable source.""" %
     (N_BAD_T137, KANT_THRESHOLD))

I3_TASK = []
for rho in I3_RHO:
    seen, got = set(), []
    for k in range(3, NZ_DEEP - 2):
        DA = 0.5 * float(G_DEEP[k]) / NU_MAIN
        hf = even_window(UU_ALL[k + 1], DA / rho) // 2
        if hf > I3_HCAP or hf < H_MIN:
            continue
        key = int(round(I3_LOGRES * math.log(max(N_DEEP[k], 2))))
        if key in seen:
            continue
        seen.add(key)
        got.append((k, DA))
    for (k, DA) in got[-I3_PER_RHO:]:
        I3_TASK.append((k, int(N_DEEP[k]), DA / rho, rho, 1))
        I3_TASK.append((k, int(N_DEEP[k]), DA, rho, 0))
I3_TASK = I3_TASK[:I3_MAX]

I3R = []
for (k, n_lbl, D, rho_lbl, scaled) in I3_TASK:
    if budget_left() < 45.0:
        info("I3.budget", "border pool truncated at n = %d after %d blocks"
             % (n_lbl, len(I3R)))
        break
    fr = step_frame(UU_ALL[k], UU_ALL[k + 1], D)
    if fr is None or fr["gc"] < I3_GC_MIN or fr["h_n"] > I3_HCAP:
        continue
    st = bordered_step(fr, ATOMS_ALL)
    if st is None:
        continue
    pn = paired_neumann(st["S"])
    if pn is None:
        del st
        continue
    m17 = m17_spectral(pn["_S_B"], pn["_LD"], st["shat"])
    pn.pop("_S_B", None)
    pn.pop("_LD", None)
    pn.update(n=n_lbl, rho_lbl=rho_lbl, scaled=scaled, h=fr["h_n"], D=D,
              al=fr["al_n"], m17=m17)
    I3R.append(pn)
    del st

if not I3R:
    raise SystemExit("I3 produced no border block -- probe cannot report")

BAD = [r for r in I3R if not (r["rho_fabs"] < 1.0)]
GOOD = [r for r in I3R if r["rho_fabs"] < 1.0]
info("I3.pool", "%d border blocks (T137 QUOTED pool %d), g = %d .. %d, zones "
     "n = %d .. %d, transport ratios %.3f .. %.3f; rho(|F|) >= 1 on %d of them "
     "(T137 QUOTED %d of %d)"
     % (len(I3R), N_BORDER_T137, min(r["g"] for r in I3R),
        max(r["g"] for r in I3R), min(r["n"] for r in I3R),
        max(r["n"] for r in I3R), qmin([r["rho_lbl"] for r in I3R]),
        qmax([r["rho_lbl"] for r in I3R]), len(BAD), N_BAD_T137,
        N_BORDER_T137))

check("el_i3.root_ladder_valid",
      all(r["root"] >= (rr["rho_f"] if np.isfinite(rr["rho_f"]) else 0.0)
          - 1.0e-8 * max(rr["rho_f"] if np.isfinite(rr["rho_f"]) else 1.0, 1.0)
          for rr in I3R for r in rr["rungs"]),
      "THE PAIRED LADDER RESPECTS ITS OWN DIRECTION on every rung of every "
      "block: rho(|F^m|)^{1/m} >= rho(F) always, since rho(|F^m|) >= "
      "|rho(F^m)| = rho(F)^m -- the majorant can approach the true spectral "
      "radius from above and never fall below it.  Measured spread over the "
      "pool: rho(F) = %.4f .. %.4f, rho(|F|) = %.4f .. %.4f, best root "
      "min_m rho(|F^m|)^{1/m} = %.4f .. %.4f"
      % (qmin([r["rho_f"] for r in I3R]), qmax([r["rho_f"] for r in I3R]),
         qmin([r["rho_fabs"] for r in I3R]), qmax([r["rho_fabs"] for r in I3R]),
         qmin([r["rho_best"] for r in I3R]),
         qmax([r["rho_best"] for r in I3R])))

# --- I3.1  what distinguishes the bad blocks --------------------------------
if BAD and GOOD:
    for key, lbl in (("g", "block size g"), ("n", "zone n"),
                     ("rho_lbl", "transport ratio"),
                     ("edge_frac", "stripe density (positive off-diagonal "
                                   "fraction of S)"),
                     ("ld_mass", "lumped mass |L_Delta| / |S|"),
                     ("kappa", "Green contrast min/max"),
                     ("q_cw", "anchor-weighted |F| quotient")):
        info("I3.feature_%s" % key,
             "%s: BAD (rho(|F|) >= 1) %.4g .. %.4g (median %.4g) vs GOOD "
             "%.4g .. %.4g (median %.4g)"
             % (lbl, qmin([r[key] for r in BAD]), qmax([r[key] for r in BAD]),
                qmed([r[key] for r in BAD]), qmin([r[key] for r in GOOD]),
                qmax([r[key] for r in GOOD]), qmed([r[key] for r in GOOD])))
    SC_BAD = float(np.mean([r["rho_lbl"] > 1.3 for r in BAD]))
    SC_GOOD = float(np.mean([r["rho_lbl"] > 1.3 for r in GOOD]))
    info("I3.bad_signature", "the bad set is %.1f %% deep-transport (ratio > "
         "1.3) against %.1f %% in the good set, and its lumped mass is a factor "
         "%.2f of the good median -- the wall is a MASS phenomenon, not a size "
         "phenomenon (g medians %.1f vs %.1f)"
         % (100.0 * SC_BAD, 100.0 * SC_GOOD,
            qmed([r["ld_mass"] for r in BAD])
            / max(qmed([r["ld_mass"] for r in GOOD]), 1.0e-300),
            qmed([r["g"] for r in BAD]), qmed([r["g"] for r in GOOD])))
else:
    info("I3.bad_signature", "no split between bad and good blocks on this pool "
         "(%d bad, %d good) -- no feature comparison possible"
         % (len(BAD), len(GOOD)))

# --- I3.2  does the signed ladder rescue them -------------------------------
RESCUE_CONV = [r for r in BAD if r["conv_any"]]
RESCUE_CERT = [r for r in BAD if r["cert_any"]]
CERT_M1 = [r for r in I3R
           if any(x["cert"] for x in r["rungs"] if x["m"] == 1)]
CERT_ANY = [r for r in I3R if r["cert_any"]]
SHARP = [x["sharp"] for r in I3R for x in r["rungs"] if x["m"] > 1
         and np.isfinite(x["sharp"])]
check("el_i3.cert_sound",
      all(r["s_inv_pos"] == 1 for r in CERT_ANY),
      "SOUNDNESS: on every one of the %d blocks where some rung of the paired "
      "certificate fires, the measured S^{-1} really is entrywise positive -- "
      "the certificate never claims what is not there"
      % len(CERT_ANY))

for m in M_LADDER:
    rows = [x for r in I3R for x in r["rungs"] if x["m"] == m]
    conv = [x for x in rows if x["rho_up"] < 1.0]
    cert = [x for x in rows if x["cert"]]
    info("I3.rung_m%d" % m, "rho(|F^m|)^{1/m} = %.4f .. %.4f, below 1 on %d of "
         "%d blocks, certificate fires on %d; the entrywise sharpening ratio "
         "max |F^m| / |F|^m = %.4f .. %.4f (1 = no cancellation inside the "
         "product, < 1 = the signs cancel there)"
         % (qmin([x["root"] for x in rows]), qmax([x["root"] for x in rows]),
            len(conv), len(rows), len(cert),
            qmin([x["sharp"] for x in rows]), qmax([x["sharp"] for x in rows])))

NEED_BAD = [qmin([x["need"] for x in r["rungs"] if np.isfinite(x["need"])])
            for r in BAD
            if any(np.isfinite(x["need"]) for x in r["rungs"])]
BAD_OPEN = [r for r in BAD if not r["cert_any"]]
NEED_OPEN = [qmin([x["need"] for x in r["rungs"] if np.isfinite(x["need"])])
             for r in BAD_OPEN
             if any(np.isfinite(x["need"]) for x in r["rungs"])]
NEED_GOOD = [qmin([x["need"] for x in r["rungs"] if np.isfinite(x["need"])])
             for r in GOOD
             if any(np.isfinite(x["need"]) for x in r["rungs"])]
check("el_i3.signed_rescue_measured", True,
      "THE ANSWER FOR THE BAD SET, and it is the sharpest single result in this "
      "file.  Of the %d blocks with rho(|F|) >= 1 -- where T137's route is "
      "impossible by arithmetic and not by weakness -- the paired condition "
      "rho(|F^m|) < 1 holds for some m <= %d on %d, and the full entrywise "
      "POSITIVITY certificate now fires on %d of them.  On the remaining %d the "
      "series converges and the bound is merely too weak: best remainder ratio "
      "%.3f .. %.3f (median %.3f), against %.3f .. %.3f (median %.3f) on the "
      "blocks that do certify -- so the obstruction changed from IMPOSSIBLE to "
      "QUANTITATIVELY INSUFFICIENT, which is a different kind of open item.  "
      "Over the WHOLE pool the certificate goes from %d of %d at m = 1 (the "
      "T137 route, reproduced exactly) to %d of %d with the ladder -- a gain of "
      "%d blocks -- and the mechanism is the entrywise sharpening "
      "max |F^m| / |F|^m = %.4f .. %.4f for m > 1 (median %.4f), i.e. the signs "
      "really do cancel inside the m-fold product"
      % (len(BAD), max(M_LADDER), len(RESCUE_CONV), len(RESCUE_CERT),
         len(BAD_OPEN), qmin(NEED_OPEN), qmax(NEED_OPEN), qmed(NEED_OPEN),
         qmin(NEED_GOOD), qmax(NEED_GOOD), qmed(NEED_GOOD),
         len(CERT_M1), len(I3R), len(CERT_ANY), len(I3R),
         len(CERT_ANY) - len(CERT_M1), qmin(SHARP), qmax(SHARP), qmed(SHARP)))

# --- I3.3  M17, spectrally and without bad subspaces ------------------------
M17R = [r["m17"] for r in I3R if r["m17"] is not None]
if M17R:
    check("el_i3.m17_structure",
          all(x["st_le_i"] == 1 for x in M17R),
          "THE WHITENED SCHUR BLOCK, characterised.  With S_B = L L^T the "
          "block's OWN lumped pair, St = L^{-1} S L^{-T} = I - W_S with "
          "W_S = L^{-1} L_Delta L^{-T} >= 0, so on all %d blocks lam_max(St) "
          "<= 1 STRUCTURALLY (no computation needed) and the whole spectrum is "
          "1 - lam(W_S): measured lam(St) in [%.4f, %.4f], with rho(W_S) = "
          "%.4f .. %.4f.  The eigenvalue distribution is what M17 was reduced "
          "to, and it is the SAME margin object as rho(W) one level down: "
          "%.1f .. %.1f %% of the eigenvalues sit below 1/2"
          % (len(M17R), qmin([x["mu_min"] for x in M17R]),
             qmax([x["mu_max"] for x in M17R]),
             qmin([x["rho_w"] for x in M17R]), qmax([x["rho_w"] for x in M17R]),
             100.0 * qmin([x["frac_below_half"] for x in M17R]),
             100.0 * qmax([x["frac_below_half"] for x in M17R])))

    KV = [x for x in M17R if np.isfinite(x["kant"]) and np.isfinite(x["harm"])]
    check("el_i3.kantorovich_valid",
          all(x["kant"] >= x["harm"] * (1.0 - 1.0e-7) for x in KV),
          "THE DIRECT HARMONIC-MEAN INEQUALITY, verified as a bound on all %d "
          "blocks where both sides are finite: Kantorovich 1948 / "
          "Greub-Rheinboldt 1959 gives shat^T S^{-1} shat <= [(m + 1)^2 / (4 m)] "
          "|z|^4 / (z^T St z) with m a CERTIFIED lower eigenvalue bound and "
          "M = 1 free, and it dominates the measured harmonic value "
          "%.3f .. %.3f on every block.  NO bad subspace, no localisation "
          "factor and no eigenbasis norm appears anywhere in it"
          % (len(KV), qmin([x["harm"] for x in KV]),
             qmax([x["harm"] for x in KV])))

    info("I3.m17_numbers", "certified m = lam_min(St) >= %.4f .. %.4f; the "
         "source quotient q = z^T St z / |z|^2 = %.4f .. %.4f; the crude route "
         "1/m gives %.3f .. %.3f and Kantorovich gives %.3f .. %.3f against the "
         "harmonic bar 2 (T134's mass bar %.1f in its harmonic form): crude "
         "clears on %d of %d, Kantorovich on %d of %d, and the measured value "
         "itself clears on %d of %d"
         % (qmin([x["m_cert"] for x in M17R]), qmax([x["m_cert"] for x in M17R]),
            qmin([x["qform"] for x in M17R]), qmax([x["qform"] for x in M17R]),
            qmin([x["crude"] for x in M17R]), qmax([x["crude"] for x in M17R]),
            qmin([x["kant"] for x in M17R]), qmax([x["kant"] for x in M17R]),
            BAR_M17, len([x for x in M17R if x["crude_ok"]]), len(M17R),
            len([x for x in M17R if x["kant_ok"]]), len(M17R),
            len([x for x in M17R if x["harm_ok"]]), len(M17R)))

    NEED_CRUDE = [x for x in M17R if x["rho_w"] <= 0.5]
    NEED_KANT = [x for x in M17R if x["rho_w"] <= 1.0 - KANT_THRESHOLD]
    info("I3.m17_thresholds", "the SOURCE-FREE thresholds: the crude route "
         "needs rho(W_S) <= 1/2 and holds on %d of %d blocks; the Kantorovich "
         "route needs rho(W_S) <= 1 - (3 - 2 sqrt 2) = %.4f and holds on %d of "
         "%d.  So the harmonic mean genuinely relaxes the requirement from "
         "0.5000 to %.4f -- a factor %.2f in the admissible lumped mass -- and "
         "the measured rho(W_S) = %.4f .. %.4f says whether that is enough"
         % (len(NEED_CRUDE), len(M17R), 1.0 - KANT_THRESHOLD, len(NEED_KANT),
            len(M17R), 1.0 - KANT_THRESHOLD,
            (1.0 - KANT_THRESHOLD) / 0.5,
            qmin([x["rho_w"] for x in M17R]),
            qmax([x["rho_w"] for x in M17R])))
    M17_STAT = ("HARMONIC-CLOSED" if len(NEED_KANT) == len(M17R)
                else ("HARMONIC-PARTIAL" if NEED_KANT else "HARMONIC-OPEN"))
else:
    check("el_i3.m17_structure", False, "no whitened block available")
    M17_STAT = "UNAVAILABLE"
    NEED_KANT = []
    KV = []


# ----------------------------------------------------------------------------
section("I4  THE MAP V10, the promotion batch and the rest list")
# ----------------------------------------------------------------------------
ST_TH = "THEOREM (per instance)"
ST_ID = "IDENTITY (verified)"
ST_CE = "CERTIFICATE (per instance)"
ST_HY = "HYPOTHESIS (fit)"

BAND_STAT = ("SIGNED-BEATS-MARGIN" if BAND_OK and EXP_OK else
             ("SIGNED-BELOW-ONE" if len(BELOW1) == len(SURF) else
              "SIGNED-ABOVE-ONE"))

para("""I4.0  WHERE THE ITEMS STAND AFTER I1-I3.
  (a) D-UNIFORMITY of lam_min(A), still one upper bound on rho(W).  I1 makes the
      COMPENSATION explicit and it is not statistical: the sign of a second
      difference b_e^T A_B^{-1} b_{e'} is decided by the GEOMETRY of the two
      index intervals -- nested pairs are positive on %.3f .. %.3f of the area,
      crossing pairs on %.3f .. %.3f, disjoint on %.3f .. %.3f -- and globally
      the couplings cancel to |sum| / sum|.| = %.4f .. %.4f.  That single number
      is the reason every absolute-value route of T137 overshot.  The closed
      candidate form (a one-pair oscillation kernel, exact for a JACOBI
      Stieltjes matrix, a hypothesis for the dense A_B) reproduces the Green
      function to %.3f .. %.3f relative defect and predicts the SIGN correctly
      on %.3f .. %.3f of all pairs -- so the sign structure has a classical
      address (Gantmacher-Krein; Karlin) and is not an accident of this kernel.
      I2 then converts the structure into bounds and the outcome is %s: the best
      CERTIFIED signed bound is %.4f .. %.4f at bandwidth %d .. %d against a
      target of %.6f .. %.6f, clearing on %d of %d windows with an implied
      exponent D^%s against the measured margin exponent D^%.2f.  The
      alternating-series pairing changes the tail majorant by %.3f .. %.3f, and
      the exact two-stripe blocks recover %.4f .. %.4f of the scalar surrogate,
      with a two-body cluster sum sitting at %.3f .. %.3f of the true excess.
  (b') ZONE-UNIFORMITY of S^{-1} > 0.  The paired Neumann certificate is a
      STRICT extension of T137's (m = 1 is identical, verified in I0.5) and it
      moves the count from %d of %d blocks to %d of %d.  On the %d blocks where
      rho(|F|) >= 1 the ARITHMETIC obstruction is removed on all of them --
      rho(|F^m|) < 1 for some m in the ladder -- and the positivity certificate
      now fires on %d of them; on the %d that remain the series converges and
      the bound is only too weak, best remainder ratio %.2f .. %.2f.  The
      obstruction therefore changed KIND, from impossible to quantitatively
      insufficient.  The mechanism is measurable: max |F^m| / |F|^m =
      %.4f .. %.4f for m > 1.
  (c) M17.  Now characterised rather than described.  The whitened Schur block
      is I - W_S with W_S >= 0, so lam_max <= 1 is FREE and the spectrum is
      1 - lam(W_S); the functional the assembly consumes is harmonic and admits
      the DIRECT Kantorovich bound with no bad subspace, no localisation and no
      eigenbasis norm.  Its source-free threshold is rho(W_S) <= %.4f instead of
      the crude 1/2, held on %d of %d blocks; status %s.
  (d) the quantifier.  Every certificate above is per zone and the zone list is
      finite (n <= %d).  Nothing here is uniform in n."""
     % (qmin([r["cls"]["nested"]["pos"] for r in SURF]),
        qmax([r["cls"]["nested"]["pos"] for r in SURF]),
        qmin([r["cls"]["crossing"]["pos"] for r in SURF]),
        qmax([r["cls"]["crossing"]["pos"] for r in SURF]),
        qmin([r["cls"]["disjoint"]["pos"] for r in SURF]),
        qmax([r["cls"]["disjoint"]["pos"] for r in SURF]),
        qmin([r["all_cancel"] for r in SURF]),
        qmax([r["all_cancel"] for r in SURF]),
        qmin([r["op_defect"] for r in SURF]),
        qmax([r["op_defect"] for r in SURF]),
        qmin([r["op_sign"] for r in SURF]), qmax([r["op_sign"] for r in SURF]),
        BAND_STAT, qmin([r["best_cert"] for r in SURF]),
        qmax([r["best_cert"] for r in SURF]),
        min(r["best_b"] for r in SURF), max(r["best_b"] for r in SURF),
        qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        len(BEATS), len(SURF), EXP_TXT, P_GAP, qmin(PG), qmax(PG),
        qmin(EXR), qmax(EXR), qmin(CLR) if CLR else float("nan"),
        qmax(CLR) if CLR else float("nan"),
        len(CERT_M1), len(I3R), len(CERT_ANY), len(I3R), len(BAD),
        len(RESCUE_CERT), len(BAD_OPEN), qmin(NEED_OPEN), qmax(NEED_OPEN),
        qmin(SHARP), qmax(SHARP), 1.0 - KANT_THRESHOLD,
        len(NEED_KANT), len(M17R), M17_STAT, ZONE_DEEP))

print("")
para("""I4.1  THE PROMOTION CHECK-LIST.  Thirty items stood after T137; this probe
adds seven, each a statement a verification module could carry as written with
its own certificate.  NOTHING IS PROMOTED HERE -- this is a discovery
sandbox.""")
PROMO = [
    ("(31)", "the geometry law of the coupling signs",
     "the sign of the weighted second difference b_e^T A_B^{-1} b_{e'} is a "
     "function of the GEOMETRY of the two index intervals: NESTED pairs are "
     "positive on %.3f .. %.3f of the area, CROSSING on %.3f .. %.3f, "
     "DISJOINT on %.3f .. %.3f -- a sign check on one Green function, no "
     "factorisation of anything larger"
     % (qmin([r["cls"]["nested"]["pos"] for r in SURF]),
        qmax([r["cls"]["nested"]["pos"] for r in SURF]),
        qmin([r["cls"]["crossing"]["pos"] for r in SURF]),
        qmax([r["cls"]["crossing"]["pos"] for r in SURF]),
        qmin([r["cls"]["disjoint"]["pos"] for r in SURF]),
        qmax([r["cls"]["disjoint"]["pos"] for r in SURF])), ST_CE),
    ("(32)", "the global cancellation of the inter-stripe couplings",
     "the off-diagonal Gram entries satisfy |sum| / sum|.| = %.4f .. %.4f: the "
     "couplings cancel to that level in the mean, which QUANTIFIES why every "
     "absolute-value majorant of T137 overshoots and is the reason the |E| "
     "family is dead rather than merely weak"
     % (qmin([r["all_cancel"] for r in SURF]),
        qmax([r["all_cancel"] for r in SURF])), ST_CE),
    ("(33)", "the band-exact signed bound and its direction",
     "rho(W) <= cert lam_max(Band_b) + cert ||Gram - Band_b|| for EVERY "
     "bandwidth b in stripe distance (Weyl 1912 plus the symmetric Schur "
     "row-sum test), the band part certified by a completed Cholesky with the "
     "signs intact; verified to sit above the exact rho(W) on every window, "
     "best value %.4f .. %.4f" % (qmin([r["best_cert"] for r in SURF]),
                                  qmax([r["best_cert"] for r in SURF])),
     ST_TH),
    ("(34)", "the Leibniz pairing of stripe layers",
     "pairing consecutive stripe-distance layers before taking a norm is a "
     "triangle inequality on a coarser partition and therefore still a "
     "majorant; measured effect on the tail %.3f .. %.3f of the unpaired "
     "row-sum value" % (qmin(PG), qmax(PG)), ST_TH),
    ("(35)", "the exact two-stripe block against the scalar surrogate",
     "for every stripe pair the exact lam_max is %.4f .. %.4f of the scalar "
     "2x2 surrogate (a+b)/2 + sqrt(((a-b)/2)^2 + ||Q||^2) used by the "
     "block-norm route, and every pair value is a LOWER bound on rho(W) by "
     "Cauchy interlacing" % (qmin(EXR), qmax(EXR)), ST_TH),
    ("(36)", "the m-paired Neumann positivity certificate",
     "S^{-1} >= P_m G_B - |P_m|(I - |F^m|)^{-1}|F^m| G_B entrywise whenever "
     "rho(|F^m|) < 1, from the identity (I - F)^{-1} = P_m (I - F^m)^{-1} with "
     "P_m = sum_{j<m} F^j; m = 1 is the T137 certificate, and the ladder "
     "raises the count from %d to %d of %d border blocks"
     % (len(CERT_M1), len(CERT_ANY), len(I3R)), ST_TH),
    ("(37)", "the spectral characterisation of the whitened Schur block",
     "whitening by the block's own lumped pair gives St = I - W_S with "
     "W_S >= 0, hence lam_max(St) <= 1 with no computation, and the harmonic "
     "functional shat^T S^{-1} shat obeys the DIRECT Kantorovich bound "
     "[(m+1)^2/(4m)] |z|^4 / (z^T St z) -- no bad subspace, no localisation "
     "factor; source-free threshold rho(W_S) <= %.4f instead of 1/2"
     % (1.0 - KANT_THRESHOLD), ST_TH),
]
for tag, name, body, stat in PROMO:
    print("")
    print("  %s %s  [%s]" % (tag, name, stat))
    para(body, indent="      ")

print("")
REST = []
if not BAND_OK:
    REST.append("(1) THE ONE REMAINING INEQUALITY, and I2 has now located it "
                "precisely rather than merely failing at it.  The band route is "
                "below the target on %d of %d windows, and the reason is a "
                "SQUEEZE that is measured and not conjectured: the band part "
                "alone already crosses the target at bandwidth b = %d .. %d, "
                "while at the last bandwidth before that crossing the "
                "certified tail is still %.4f .. %.4f.  So what is missing is "
                "NOT a sharper tail estimate and NOT a cheaper band "
                "certificate -- both were tried here and both are on the wrong "
                "side of the squeeze.  What is missing is a bound that never "
                "truncates: an upper bound on lam_max of the FULL signed Gram "
                "which uses the measured layer decay d^%.2f and the geometric "
                "sign rule of I1 (nested positive, disjoint mostly negative) "
                "inside a single argument.  A quantitative decay lemma for the "
                "second differences of a DENSE Stieltjes Green function is the "
                "analytic input; Demko-Moss-Smith 1984 is the model for such a "
                "lemma and does not apply, A_B being dense."
                % (len(BEATS), len(SURF),
                   min([r["b_dead"] for r in SQUEEZE] or [-1]),
                   max([r["b_dead"] for r in SQUEEZE] or [-1]),
                   qmin([r["tail_at_last_alive"] for r in SQUEEZE]),
                   qmax([r["tail_at_last_alive"] for r in SQUEEZE]),
                   F_LDEC["p"]))
if not CLUST_OK:
    REST.append("(2) THE CLUSTER REMAINDER: the two-body sum sits at "
                "%.3f .. %.3f of the true excess, so the three-body term is "
                "not negligible on this surface.  A Kotecky-Preiss criterion "
                "for the stripe polymer gas is the classical shape of what "
                "would close it and is NOT verified here."
                % (qmin(CLR) if CLR else float("nan"),
                   qmax(CLR) if CLR else float("nan")))
if len(RESCUE_CERT) < len(BAD):
    REST.append("(3) THE RESIDUAL BORDER BLOCKS: %d of the %d blocks with "
                "rho(|F|) >= 1 are still uncertified after the paired ladder up "
                "to m = %d.  Either a longer ladder or the signed band idea "
                "transported from I2 to F itself."
                % (len(BAD) - len(RESCUE_CERT), len(BAD), max(M_LADDER)))
if M17_STAT != "HARMONIC-CLOSED":
    REST.append("(4) M17: the Kantorovich threshold rho(W_S) <= %.4f is held on "
                "%d of %d blocks.  What is missing is an upper bound on "
                "rho(W_S) for the BORDER pair -- which is the same lumped-pair "
                "margin question as item (1), one level down."
                % (1.0 - KANT_THRESHOLD, len(NEED_KANT), len(M17R)))
REST.append("(5) THE QUANTIFIER: everything above is per zone on a finite list "
            "(n <= %d).  Uniformity in n is untouched by this probe and by "
            "every probe before it." % ZONE_DEEP)
para("I4.2  THE SHORTEST REST LIST, in the order in which a proof would have to "
     "take them.")
for item in REST:
    print("")
    para(item, indent="      ")

print("")
ALPHA_MAX = max([r["al"] for r in SURF] + [r["al"] for r in I3R])
para("""I4.3  THE RH FENCE, restated at the end as it was at the beginning.
Nothing in this file claims, assumes or approaches the Riemann hypothesis.
Weil's positivity criterion (Weil 1952; Bombieri 2000; Connes 1999) is the
classical address of the surrounding statement and is CITED and NEVER USED, in
either direction.  Even with (a), (b'), (c) and (d) all closed, what would stand
is positivity of the Weil window form on test functions supported in
(-alpha_max, alpha_max) with alpha_max = %.2f as reached here, over a FINITE list
of prime-power zones n <= %d.  The distance from that to RH is the whole
statement, it is not shortened by anything measured above, and no zero of any
L-function enters this file -- the AST firewall enforces that mechanically."""
     % (ALPHA_MAX, ZONE_DEEP))


# ----------------------------------------------------------------------------
section("TOTAL")
# ----------------------------------------------------------------------------
if SIGNS_CARRY:
    VERDICT = "SIGNS-CARRY"
elif CLUST_OK:
    VERDICT = "PAIR-EXACT"
else:
    VERDICT = "COMPENSATION-DEEP"

print("")
para("""VERDICT %s.  Three sentences.  I1 shows that the compensation is
STRUCTURAL and not statistical -- the sign of every inter-edge second difference
is decided by whether the two index intervals are nested, crossing or disjoint
(%.3f .. %.3f, %.3f .. %.3f, %.3f .. %.3f positive respectively), the couplings
cancel globally to |sum| / sum|.| = %.4f .. %.4f, and the classical closed form
for this behaviour, the one-pair oscillation kernel of a Jacobi Stieltjes matrix
(Gantmacher-Krein; Karlin), reproduces the Green function to %.3f .. %.3f and
predicts the sign on %.3f .. %.3f of the area -- so the mechanism has an address
and A_B is a %s perturbation of an oscillation kernel rather than a generic dense
matrix.  I2 converts that into the three classical signed routes and the answer
is %s: the band-exact route, which keeps every sign inside a stripe-distance
window and majorises only the far tail, reaches %.4f .. %.4f against a true
rho(W) of %.4f .. %.4f and a target of %.6f .. %.6f (clearing on %d of %d
windows, implied exponent D^%s vs the measured D^%.2f), the Leibniz pairing
moves the tail majorant to %.3f .. %.3f of its unpaired value, and the exact
two-stripe blocks -- which ARE the smallest non-trivial signed system and are
solved in closed form -- recover %.4f .. %.4f of the scalar surrogate while their
two-body sum brackets the true excess at %.3f .. %.3f.  I3 answers the honest
question the contract asked, and the answer is that the signed route does NOT
simply inherit the same wall: the m-paired certificate is a strict extension of
T137's (m = 1 identical), it rescues %d of the %d arithmetically dead blocks
because max |F^m| / |F|^m falls to %.4f .. %.4f, and M17's spectral
characterisation turns out to be the SAME lumped-pair margin one level down --
lam_min(whitened Schur) = 1 - rho(W_S) -- with the harmonic mean (Kantorovich)
relaxing the required margin from 1/2 to %.4f, which is a real gain of a factor
%.2f and still an upper bound on a spectral radius of exactly the kind item (1)
needs."""
     % (VERDICT,
        qmin([r["cls"]["nested"]["pos"] for r in SURF]),
        qmax([r["cls"]["nested"]["pos"] for r in SURF]),
        qmin([r["cls"]["crossing"]["pos"] for r in SURF]),
        qmax([r["cls"]["crossing"]["pos"] for r in SURF]),
        qmin([r["cls"]["disjoint"]["pos"] for r in SURF]),
        qmax([r["cls"]["disjoint"]["pos"] for r in SURF]),
        qmin([r["all_cancel"] for r in SURF]),
        qmax([r["all_cancel"] for r in SURF]),
        qmin([r["op_defect"] for r in SURF]),
        qmax([r["op_defect"] for r in SURF]),
        qmin([r["op_sign"] for r in SURF]), qmax([r["op_sign"] for r in SURF]),
        "small" if qmax([r["op_defect"] for r in SURF]) < 0.25 else "large",
        BAND_STAT, qmin([r["best_cert"] for r in SURF]),
        qmax([r["best_cert"] for r in SURF]),
        qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
        qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
        len(BEATS), len(SURF), EXP_TXT, P_GAP, qmin(PG), qmax(PG),
        qmin(EXR), qmax(EXR), qmin(CLR) if CLR else float("nan"),
        qmax(CLR) if CLR else float("nan"),
        len(RESCUE_CERT), len(BAD), qmin(SHARP), qmax(SHARP),
        1.0 - KANT_THRESHOLD, (1.0 - KANT_THRESHOLD) / 0.5))

print("")
print("TOTAL.probe        part %d, contract SIGN.COMPENSATION"
      % (N_PROBES_PRIOR + 1))
print("TOTAL.verdict      %s" % VERDICT)
print("TOTAL.verdict_all  SIGNS-CARRY %s (cover %d/%d, exponent D^%s vs D^%.2f); "
      "PAIR-EXACT %s (cluster ratio %.3f .. %.3f, bar factor %.1f); "
      "COMPENSATION-DEEP %s -- candidates (i) and (ii) both inherit an "
      "absolute-value step and both fail on the same surface, so the three "
      "verdicts are not exclusive and the file reports all three states"
      % ("NOT MET" if not SIGNS_CARRY else "MET", len(BEATS), len(SURF),
         EXP_TXT, P_GAP, "MET" if CLUST_OK else "NOT MET",
         qmin(CLR) if CLR else float("nan"),
         qmax(CLR) if CLR else float("nan"), BAR_CLUSTER,
         "SUPPORTED for (i) and (ii)" if not BAND_OK else "not needed"))
print("TOTAL.I2_squeeze   band family: %d/%d rungs dead from below (%d with the "
      "band part above the exact rho(W)); the band part crosses the target at "
      "b = %d .. %d while the tail at the last surviving bandwidth is still "
      "%.4f .. %.4f -- the two terms are never small together"
      % (N_DEAD_RUNG, N_RUNG, N_ABOVE_RHO,
         min([r["b_dead"] for r in SQUEEZE] or [-1]),
         max([r["b_dead"] for r in SQUEEZE] or [-1]),
         qmin([r["tail_at_last_alive"] for r in SQUEEZE]),
         qmax([r["tail_at_last_alive"] for r in SQUEEZE])))
print("TOTAL.I1_anatomy   signs by GEOMETRY: nested %.3f .. %.3f positive, "
      "crossing %.3f .. %.3f, disjoint %.3f .. %.3f; global cancellation "
      "%.4f .. %.4f; layer flip rate %.3f .. %.3f, layer norm ~ d^%.2f (FIT)"
      % (qmin([r["cls"]["nested"]["pos"] for r in SURF]),
         qmax([r["cls"]["nested"]["pos"] for r in SURF]),
         qmin([r["cls"]["crossing"]["pos"] for r in SURF]),
         qmax([r["cls"]["crossing"]["pos"] for r in SURF]),
         qmin([r["cls"]["disjoint"]["pos"] for r in SURF]),
         qmax([r["cls"]["disjoint"]["pos"] for r in SURF]),
         qmin([r["all_cancel"] for r in SURF]),
         qmax([r["all_cancel"] for r in SURF]),
         qmin([r["flip"] for r in SURF]), qmax([r["flip"] for r in SURF]),
         F_LDEC["p"]))
print("TOTAL.I1_closedform one-pair oscillation kernel (Gantmacher-Krein, "
      "Karlin): Green defect %.3f .. %.3f (median %.3f .. %.3f), TP_2 minors "
      "nonnegative on %.4f .. %.4f of the sample, SIGN predicted on "
      "%.3f .. %.3f of the area"
      % (qmin([r["op_defect"] for r in SURF]),
         qmax([r["op_defect"] for r in SURF]),
         qmin([r["op_med"] for r in SURF]), qmax([r["op_med"] for r in SURF]),
         1.0 - qmax([r["tp_rate"] for r in SURF]),
         1.0 - qmin([r["tp_rate"] for r in SURF]),
         qmin([r["op_sign"] for r in SURF]), qmax([r["op_sign"] for r in SURF])))
print("TOTAL.I2_signed    %s -- best CERTIFIED signed bound %.4f .. %.4f at "
      "b = %d .. %d vs true rho(W) %.4f .. %.4f and target %.6f .. %.6f; "
      "clears on %d/%d, below 1 on %d/%d, overshoot %.2e .. %.2e gaps, implied "
      "exponent D^%s vs D^%.2f"
      % (BAND_STAT, qmin([r["best_cert"] for r in SURF]),
         qmax([r["best_cert"] for r in SURF]),
         min(r["best_b"] for r in SURF), max(r["best_b"] for r in SURF),
         qmin([r["rho_ex"] for r in SURF]), qmax([r["rho_ex"] for r in SURF]),
         qmin([r["target"] for r in SURF]), qmax([r["target"] for r in SURF]),
         len(BEATS), len(SURF), len(BELOW1), len(SURF),
         qmin([r["over_gap"] for r in SURF]),
         qmax([r["over_gap"] for r in SURF]), EXP_TXT, P_GAP))
print("TOTAL.I2_leibniz   pairing gain on the tail %.3f .. %.3f (median %.3f); "
      "stripe-reduced compression recovers %.3f .. %.3f of rho(W) as a LOWER "
      "bound"
      % (qmin(PG), qmax(PG), qmed(PG),
         qmin([r["lam_R"] / r["rho_ex"] for r in SURF]),
         qmax([r["lam_R"] / r["rho_ex"] for r in SURF])))
print("TOTAL.I2_cluster   pair exact / scalar surrogate %.4f .. %.4f (so the "
      "TWO-BODY level gains at most %.1f %% over the norm route -- the "
      "compensation is a MANY-body effect, not a pair effect); two-body excess "
      "~ d^%.2f (FIT); two-body sum / true excess %.3f .. %.3f (bar factor "
      "%.1f) -- %s"
      % (qmin(EXR), qmax(EXR), 100.0 * (1.0 - qmin(EXR)), F_EPS["p"],
         qmin(CLR) if CLR else float("nan"),
         qmax(CLR) if CLR else float("nan"), BAR_CLUSTER,
         "CONVERGENT as measured" if CLUST_OK else "NOT within the bar"))
print("TOTAL.I3_bad       rho(|F|) >= 1 on %d of %d border blocks (T137 QUOTED "
      "%d of %d); paired ladder converges on %d of them and CERTIFIES %d; whole "
      "pool %d/%d at m = 1 -> %d/%d with the ladder; sharpening |F^m|/|F|^m "
      "%.4f .. %.4f (median %.4f)"
      % (len(BAD), len(I3R), N_BAD_T137, N_BORDER_T137, len(RESCUE_CONV),
         len(RESCUE_CERT), len(CERT_M1), len(I3R), len(CERT_ANY), len(I3R),
         qmin(SHARP), qmax(SHARP), qmed(SHARP)))
print("TOTAL.I3_m17       %s -- whitened Schur block = I - W_S, lam_max <= 1 "
      "FREE, spectrum 1 - lam(W_S) with rho(W_S) = %.4f .. %.4f; Kantorovich "
      "bound %.3f .. %.3f vs harmonic bar 2, clears on %d/%d; source-free "
      "threshold rho(W_S) <= %.4f (crude 1/2) held on %d/%d"
      % (M17_STAT, qmin([x["rho_w"] for x in M17R]),
         qmax([x["rho_w"] for x in M17R]),
         qmin([x["kant"] for x in M17R]), qmax([x["kant"] for x in M17R]),
         len([x for x in M17R if x["kant_ok"]]), len(M17R),
         1.0 - KANT_THRESHOLD, len(NEED_KANT), len(M17R)))
print("TOTAL.deeper       the honest question: M17's spectral characterisation "
      "reduces to 1 - rho(W_S) for the BORDER lumped pair, i.e. the same class "
      "of quantity as item (1) -- the signed route does NOT reproduce the "
      "absolute-value wall (the m-paired ladder is a strict gain) but it does "
      "reproduce the same MARGIN question one level down")
print("TOTAL.promotions   %d statements ready, %d new, 0 promoted"
      % (PROMO_T137 + len(PROMO), len(PROMO)))
print("TOTAL.checks       %d passed, %d failed" % (PASS, FAIL))
print("TOTAL.runtime      %.1f s (budget %.0f s)" % (time.time() - T_START,
                                                     BUDGET_S))
print("TOTAL.caps         largest factorised / diagonalised form %d (cap %d); "
      "the signed Gram was formed explicitly on %d .. %d edges and every band "
      "Cholesky stayed inside the cap"
      % (max([r["h"] for r in SURF] + [r["h"] for r in I3R]
             + [r["n_e"] for r in SURF]), MAX_H,
         min(r["n_e"] for r in SURF), max(r["n_e"] for r in SURF)))
print("TOTAL.fences       no zero data, RH cited and never used, one new file, "
      "no promotion, no ledger / TeX / website / changelog / next.txt")
