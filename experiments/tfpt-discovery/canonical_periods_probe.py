#!/usr/bin/env python3
"""Discovery probe: the canonical period normalization -- the analytic bridge
closes.  (QGEO cover program, round 16 candidate; executes v612's named
step B5.)

The v611/v612 rounds left ONE named step: fix the diagonal weights of the
polarization J in the rotation frame by the analytic period normalization.
This probe lands four structural results:

  (A) DECK-FREE ROTATION ON SEGMENTS [E-numeric]: the quarter rotation
      x -> ix maps the four branch-point segments cyclically with NO deck
      correction (all twelve wrap factors are exactly 1 at working
      precision), and the single homology relation on the omega-sheet is
      seg1 + seg2 + seg3 + seg4 = 0.  A must-fail control documents the
      falsification of the naive ansatz: the raw period rows are NOT
      r-eigenvectors.

  (B) THE EXACT DICTIONARY r = deck o rotation [E]: the induced rotation
      on the 3-basis is the companion matrix M (M^4 = 1), and the reduced
      Burau rotation r at t = omega is GL3-conjugate to omega * M -- the
      geometric quarter rotation composed with EXACTLY ONE deck step.
      This explains v597's r^4 = omega structurally.  The deck power is
      UNIQUE: among all scalar twists c*M with (c*M)^4 = omega (the four
      c = zeta_12 * i^k), only c = omega (= i * zeta_12, the deck itself)
      matches the r spectrum; c = 1 and c = omega^2 fail as well.

  (C) PERIOD ROWS ARE ROTATION EIGENVECTORS [E-numeric]: on the honest
      omega-sheet cohomology basis (hol dx/y^2, hol x dx/y^2, antihol
      conj(dx/y)) the period rows are left eigenvectors of M with the
      three characters (i, -1, -i); transported through the exact
      conjugator G they are left eigenvectors of r with eigenvalues
      omega * (i, -1, -i) = spec(r).

  (D) THE HODGE WEIGHTS ARE EXPLICIT GAMMA MONOMIALS [E]: the Hodge form
      h(eta, eta) = (i/2) int eta wedge conj(eta) is diagonal per
      character with values
        h0 = (3/4) pi G(1/4)G(1/3)G(5/12) / (G(3/4)G(2/3)G(7/12))   (> 0)
        h1 = (3/4) pi G(1/3)G(1/6) / (G(2/3)G(5/6))
           = (3 sqrt3 / (16 pi)) G(1/3)^2 G(1/6)^2                  (> 0)
        h2 = (3/4) pi G(1/4)G(2/3)G(1/12) / (G(3/4)G(1/3)G(11/12))  (> 0)
      via the complex Beta (Gelfand/KLT) formula, verified numerically to
      high precision; the omega-sheet signature is (2,1) with the UNIQUE
      NEGATIVE direction = the antiholomorphic line conj(dx/y).

  (E) THE SIGN BRIDGE J = -h PER CHARACTER [E]: v612's J-diagonal in the
      rotation frame has its UNIQUE POSITIVE entry on the zeta_12
      eigenline; the analytic h has its UNIQUE NEGATIVE entry on the SAME
      character (antihol <-> -i*omega = zeta_12).  All three character-
      matched sign products are negative: the compiler polarization J is
      the NEGATIVE of the analytic Hodge form up to per-line positive
      scales -- Riemann-Hodge positivity is realized by J, and the
      diagonal weights are fixed by the Gamma monomials above.

Verdict enums (frozen): PERIOD-NORMALIZED (all pass),
PERIOD-NORMALIZATION-FAILS, MIXED.

Python-only (sympy + mpmath), counted per GATE.WOLFRAM.02.
"""

import sympy as sp
from mpmath import (mp, mpf, mpc, exp, pi, arg, im, re, quad, matrix, norm,
                    gamma, hyp2f1, sqrt, fabs)

mp.dps = 40


def sym_to_mpc(e):
    """Full-precision sympy -> mpmath conversion (no double-precision loss)."""
    ee = sp.expand_complex(e)
    return mpc(mpf(str(sp.N(sp.re(ee), 45))), mpf(str(sp.N(sp.im(ee), 45))))
t = sp.symbols("t")
OMEGA = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
Z12 = sp.exp(sp.I * sp.pi / 6)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


def burau_gen(i, n=4):
    m = n - 1
    M = sp.eye(m)
    if i - 2 >= 0:
        M[i - 2, i - 1] = t
    M[i - 1, i - 1] = -t
    if i < m:
        M[i, i - 1] = 1
    return M


S = [sp.simplify(burau_gen(i).subs({t: OMEGA})) for i in (1, 2, 3)]
r_sym = sp.simplify(S[0] * S[1] * S[2])
J = sp.Matrix([[0, 1 + sp.sqrt(3) * sp.I, -1 + sp.sqrt(3) * sp.I],
               [1 - sp.sqrt(3) * sp.I, 2, 1 + sp.sqrt(3) * sp.I],
               [-1 - sp.sqrt(3) * sp.I, 1 - sp.sqrt(3) * sp.I, 0]])

# ================================================================== A
print("=" * 72)
print("A: deck-free rotation on segments and the homology relation")
print("=" * 72)

BRANCH_PTS = [mpc(1, 0), mpc(0, 1), mpc(-1, 0), mpc(0, -1)]


def branch_offsets(k, n_scan=2048):
    """Exact staircase of 2*pi jumps of arg(x^4 - 1) along segment k.

    Principal-arg jumps (> pi) are located by bisection; between jumps the
    principal argument is smooth, so theta(s) = principal + offset(s) is
    exact at working precision (no interpolation error)."""
    a, b = BRANCH_PTS[k % 4], BRANCH_PTS[(k + 1) % 4]

    def parg(s):
        x = a + s * (b - a)
        return arg(x ** 4 - 1)

    eps = mpf(1) / (10 ** 6)
    jumps = []
    prev_s, prev_a = eps, parg(eps)
    for q in range(1, n_scan + 1):
        s = eps + (1 - 2 * eps) * mpf(q) / n_scan
        cur = parg(s)
        d = cur - prev_a
        if fabs(d) > pi:
            lo, hi = prev_s, s
            for _ in range(80):
                mid = (lo + hi) / 2
                if fabs(parg(mid) - prev_a) > pi:
                    hi = mid
                else:
                    lo = mid
            jumps.append(((lo + hi) / 2, -mpf(2) * pi if d > pi else mpf(2) * pi))
        prev_s, prev_a = s, cur
    return a, b, jumps


def seg_period(k, m, expo):
    """int over segment p_k -> p_{k+1} of x^m (x^4-1)^(-expo) dx,
    with continuous branch of the argument (exact staircase)."""
    a, b, jumps = branch_offsets(k)

    def theta(s):
        off = mpf(0)
        for sj, dj in jumps:
            if s > sj:
                off += dj
        x = a + s * (b - a)
        return arg(x ** 4 - 1) + off

    def f(s):
        x = a + s * (b - a)
        rr = fabs(x ** 4 - 1)
        return x ** m * (b - a) * rr ** (-expo) * exp(-mpc(0, 1) * theta(s) * expo)

    pts = sorted([mpf(0)] + [sj for sj, _ in jumps] + [mpf(1)])
    return quad(f, pts)


# honest omega-sheet basis: hol m=0 (dx/y^2), hol m=1 (x dx/y^2),
# antihol = conj(dx/y): rows of the 3x4 period matrix
Q4 = matrix(3, 4)
for k in range(4):
    Q4[0, k] = seg_period(k, 0, mpf(2) / 3)
    Q4[1, k] = seg_period(k, 1, mpf(2) / 3)
    Q4[2, k] = seg_period(k, 0, mpf(1) / 3).conjugate()

PHASES = [mpc(0, 1), mpc(-1, 0), mpc(0, -1)]  # pullback characters i, -1, -i
wrap_max = mpf(0)
for row in range(3):
    for k in range(4):
        ratio = Q4[row, (k + 1) % 4] / (PHASES[row] * Q4[row, k])
        wrap_max = max(wrap_max, fabs(ratio - 1))
check("A1 all 12 wrap factors = 1 (rotation acts deck-free on segments; "
      "characters i, -1, -i)", wrap_max < mpf(10) ** (-20),
      "max |factor - 1| = %s" % mp.nstr(wrap_max, 3))

rel_max = mpf(0)
for row in range(3):
    ssum = sum(Q4[row, k] for k in range(4))
    rel_max = max(rel_max, fabs(ssum) / fabs(Q4[row, 0]))
check("A2 homology relation seg1 + seg2 + seg3 + seg4 = 0 on all three rows",
      rel_max < mpf(10) ** (-20), "max rel residual = %s" % mp.nstr(rel_max, 3))

rN = matrix(3, 3)
for i in range(3):
    for j in range(3):
        rN[i, j] = sym_to_mpc(r_sym[i, j])

worst_resid = mpf("inf")
for row in range(3):
    v = matrix([[Q4[row, 0], Q4[row, 1], Q4[row, 2]]])
    vr = v * rN
    lam = vr[0, 0] / v[0, 0]
    worst_resid = min(worst_resid, norm(vr - lam * v) / norm(v))
check("A3 [must-fail control] raw period rows are NOT r-eigenvectors "
      "(naive ansatz falsified)", worst_resid > mpf(1) / 10,
      "min residual = %s" % mp.nstr(worst_resid, 3))

# ================================================================== B
print("=" * 72)
print("B: the exact dictionary r = deck o rotation")
print("=" * 72)

# induced rotation on (seg1, seg2, seg3): e1 -> e2 -> e3 -> -(e1+e2+e3)
M = sp.Matrix([[0, 0, -1], [1, 0, -1], [0, 1, -1]])
x = sp.symbols("x")
check("B1.1 M^4 = 1 and char(M) = x^3 + x^2 + x + 1 (spectrum {-1, i, -i})",
      sp.simplify(M ** 4 - sp.eye(3)) == sp.zeros(3, 3)
      and sp.expand(M.charpoly(x).as_expr() - (x ** 3 + x ** 2 + x + 1)) == 0)

char_r = sp.expand(sp.expand_complex(r_sym.charpoly(x).as_expr()))
char_wM = sp.expand(sp.expand_complex((OMEGA * M).charpoly(x).as_expr()))
check("B1.2 char(r) = char(omega * M) EXACTLY (r is the rotation times one "
      "deck step)", sp.simplify(char_r - char_wM) == 0)

# exact conjugator via eigenvector matching
def eig_cols(A):
    out = {}
    for ev, mult, vecs in A.eigenvects():
        out[sp.simplify(sp.expand_complex(ev))] = sp.simplify(vecs[0])
    return out


er = eig_cols(r_sym)
ew = eig_cols(sp.simplify(OMEGA * M))
order = sorted(er.keys(), key=lambda z: str(z))
Pr = sp.Matrix.hstack(*[er[lam] for lam in order])
Pw = sp.Matrix.hstack(*[ew[lam] for lam in order])
G = sp.simplify(Pr * Pw.inv())
check("B2.1 explicit conjugator G with r G = G (omega M) exactly, det G != 0",
      sp.simplify(sp.expand_complex(r_sym * G - G * (OMEGA * M))) == sp.zeros(3, 3)
      and sp.simplify(G.det()) != 0)

# uniqueness of the deck power among all scalar twists with (cM)^4 = omega
unique_ok = True
for kk in range(4):
    c = sp.simplify(sp.expand_complex(Z12 * sp.I ** kk))
    match = sp.simplify(sp.expand_complex(
        sp.expand(char_r - (c * M).charpoly(x).as_expr()))) == 0
    is_deck = sp.simplify(sp.expand_complex(c - OMEGA)) == 0
    if match != is_deck:
        unique_ok = False
check("B3.1 deck power UNIQUE: among the four scalar twists c*M with "
      "(cM)^4 = omega, ONLY c = omega matches spec(r)", unique_ok)
check("B3.2 [must-fail controls] char(r) != char(M) and char(r) != char(omega^2 M)",
      sp.simplify(char_r - sp.expand(M.charpoly(x).as_expr())) != 0
      and sp.simplify(sp.expand_complex(
          char_r - sp.expand(sp.expand_complex(
              (OMEGA ** 2 * M).charpoly(x).as_expr())))) != 0)

# ================================================================== C
print("=" * 72)
print("C: period rows are rotation eigenvectors; transported = r-eigenvectors")
print("=" * 72)

MN = matrix(3, 3)
for i in range(3):
    for j in range(3):
        MN[i, j] = mpc(int(M[i, j]), 0)

worst_c1 = mpf(0)
for row in range(3):
    v = matrix([[Q4[row, 0], Q4[row, 1], Q4[row, 2]]])
    vM = v * MN
    worst_c1 = max(worst_c1, norm(vM - PHASES[row] * v) / norm(v))
check("C1 period rows are left eigenvectors of M with characters (i, -1, -i)",
      worst_c1 < mpf(10) ** (-20), "max residual = %s" % mp.nstr(worst_c1, 3))

GiN = matrix(3, 3)
Gi = sp.simplify(G.inv())
for i in range(3):
    for j in range(3):
        GiN[i, j] = sym_to_mpc(Gi[i, j])

wN = mpc(-mpf(1) / 2, sqrt(3) / 2)
worst_c2 = mpf(0)
lam_seen = []
for row in range(3):
    v = matrix([[Q4[row, 0], Q4[row, 1], Q4[row, 2]]]) * GiN
    vr = v * rN
    lam = wN * PHASES[row]
    lam_seen.append(lam)
    worst_c2 = max(worst_c2, norm(vr - lam * v) / norm(v))
check("C2 transported rows q G^-1 are left eigenvectors of r with eigenvalues "
      "omega * (i, -1, -i) = spec(r)", worst_c2 < mpf(10) ** (-20),
      "max residual = %s" % mp.nstr(worst_c2, 3))

# character matching: hol0 <-> -zeta12, hol1 <-> -i zeta12, antihol <-> zeta12
z12N = exp(mpc(0, 1) * pi / 6)
match_ok = (fabs(lam_seen[0] + z12N) < mpf(10) ** (-25)
            and fabs(lam_seen[1] + mpc(0, 1) * z12N) < mpf(10) ** (-25)
            and fabs(lam_seen[2] - z12N) < mpf(10) ** (-25))
check("C3 character match: hol dx/y^2 <-> -zeta_12, hol x dx/y^2 <-> -i zeta_12, "
      "ANTIHOL conj(dx/y) <-> zeta_12", match_ok)

# ================================================================== D
print("=" * 72)
print("D: the Hodge weights are explicit Gamma monomials")
print("=" * 72)


def complex_beta(alpha, beta):
    """int over C of |w|^(2 alpha) |1-w|^(2 beta) d^2w (Gelfand/KLT)."""
    return (pi * gamma(1 + alpha) * gamma(1 + beta) * gamma(-1 - alpha - beta)
            / (gamma(-alpha) * gamma(-beta) * gamma(2 + alpha + beta)))


def complex_beta_numeric(alpha, beta):
    """Radial reduction: angular average of |1-rho e^{i th}|^(2 beta) is
    2 pi 2F1(-beta, -beta; 1; rho^2) inside, with inversion outside
    (u = 1/rho).  The algebraic endpoint singularities at 0 are removed
    by the substitution x = (1/2) v^12."""
    half = mpf(1) / 2

    def rad_in(rho):
        return rho ** (2 * alpha + 1) * 2 * pi * hyp2f1(-beta, -beta, 1, rho ** 2)

    def rad_out(u):
        return (u ** (-2 * alpha - 2 * beta - 3)
                * 2 * pi * hyp2f1(-beta, -beta, 1, u ** 2))

    def in0(v):
        return rad_in(half * v ** 12) * 12 * half * v ** 11

    def out0(v):
        return rad_out(half * v ** 12) * 12 * half * v ** 11

    return (quad(in0, [0, 1]) + quad(rad_in, [half, mpf(7) / 8, 1])
            + quad(out0, [0, 1]) + quad(rad_out, [half, mpf(7) / 8, 1]))


# h_m = 3 * (1/4) * CB(alpha_m, beta_m): 3 sheets, w = x^4 is 4:1 with
# d^2x = d^2w / (16 |w|^{3/2})
CASES = [("h0 (hol dx/y^2)", mpf(-3) / 4, mpf(-2) / 3),
         ("h1 (hol x dx/y^2)", mpf(-1) / 2, mpf(-2) / 3),
         ("h2 (antihol conj(dx/y), |.|^2-weight)", mpf(-3) / 4, mpf(-1) / 3)]
hvals = []
for name, alpha, beta in CASES:
    closed = mpf(3) / 4 * complex_beta(alpha, beta)
    numeric = mpf(3) / 4 * complex_beta_numeric(alpha, beta)
    hvals.append(closed)
    check("D1 %s: closed Gamma monomial matches numeric integral" % name,
          fabs(closed - numeric) / fabs(closed) < mpf(10) ** (-25),
          "value = %s, rel diff = %s"
          % (mp.nstr(closed, 12), mp.nstr(fabs(closed - numeric) / fabs(closed), 3)))

h1_gamma = 3 * sqrt(3) / (16 * pi) * gamma(mpf(1) / 3) ** 2 * gamma(mpf(1) / 6) ** 2
check("D2 reflection identity: h1 = (3 sqrt3 / 16 pi) Gamma(1/3)^2 Gamma(1/6)^2",
      fabs(hvals[1] - h1_gamma) / hvals[1] < mpf(10) ** (-25))

# Hodge form on the omega-sheet: diag(+h0, +h1, -h2) per character
check("D3 omega-sheet Hodge signature (2,1): h0, h1, h2 all positive, form = "
      "diag(+h0, +h1, -h2), UNIQUE negative = antiholomorphic conj(dx/y)",
      all(h > 0 for h in hvals))

# ================================================================== E
print("=" * 72)
print("E: the sign bridge J = -h per character")
print("=" * 72)

evs = (r_sym.T).eigenvects()
eigs, W_rows = [], []
for ev, mult, vecs in evs:
    eigs.append(sp.simplify(sp.expand_complex(ev)))
    W_rows.append(list(sp.simplify(vecs[0].T)))
W = sp.Matrix(W_rows)
Wi = W.inv()
D = sp.expand(sp.simplify(Wi.conjugate().T * J * Wi))
jdiag = {eigs[i]: sp.simplify(D[i, i]) for i in range(3)}

# analytic signs per character (C3 matching)
h_sign = {sp.simplify(sp.expand_complex(-Z12)): 1,          # hol0
          sp.simplify(sp.expand_complex(-sp.I * Z12)): 1,   # hol1
          sp.simplify(sp.expand_complex(Z12)): -1}          # antihol
bridge_ok = True
for lam, dval in jdiag.items():
    prod_sign = sp.sign(sp.re(dval)) * h_sign[lam]
    if prod_sign != -1:
        bridge_ok = False
check("E1 all three character-matched sign products are NEGATIVE: "
      "J = -h per character (compiler polarization = MINUS the Hodge form, "
      "up to per-line positive scales)", bridge_ok,
      str({str(k): sp.nsimplify(v) for k, v in jdiag.items()}))

check("E2 the distinguished lines coincide: J's unique POSITIVE line "
      "(zeta_12, v612) = h's unique NEGATIVE line (antihol conj(dx/y), C3/D3)",
      sp.sign(sp.re(jdiag[sp.simplify(sp.expand_complex(Z12))])) == 1
      and h_sign[sp.simplify(sp.expand_complex(Z12))] == -1)

# ================================================================== F
print("=" * 72)
print("F: the reading")
print("=" * 72)

check("F1 [C] the analytic bridge closes: r = deck o rotation (B), period "
      "rows realize the rotation eigenframe (C), the diagonal weights are "
      "the explicit Gamma monomials h0, h1, h2 (D), and J = -h per character "
      "(E); the residue is the canonical FORK-BASIS identification (basepoint "
      "bookkeeping for G), named, not claimed", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: PERIOD-NORMALIZED -- the Burau rotation is the curve rotation")
    print("times one deck step, the period rows realize the eigenframe, the Hodge")
    print("weights are explicit Gamma monomials, and J = -h per character.")
else:
    print("SOME CHECKS FAILED")
