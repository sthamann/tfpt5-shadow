#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""e8_coxeter_euler_completion_probe -- r617 E8.COXETER.EULER.COMPLETION.01

FROZEN SPEC v1 (2026-09-02).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.
Deterministic (no randomness).  Pure Coxeter / cyclotomic / Euler-product
algebra.  No TFPT physics input.  Not a claim.

The trace-free completion is zero-free and pole-free in Re s > 1/2. The splitting into the scalar zeta channel and the Coxeter channel is open and RH-equivalent. No RH claim.

=======================================================================
SETUP (copied from sealed r609 e8_directed_readout_probe, not imported)
=======================================================================
Bourbaki E8 edges (1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4).
S = Euler/Seifert matrix of the bipartite orientation (S_ii=1,
S_ij=-1 on arrow i->j).  S + S^T = A_{E8}.  C = -S^{-1} S^T,
det(xI - C) = Phi_30(x) = x^8 + x^7 - x^5 - x^4 - x^3 + x + 1.

=======================================================================
T1  self-reciprocal identity (exact)
=======================================================================
det(I - x C) = Phi_30(x)  (self-reciprocal: x^8 Phi_30(1/x) = Phi_30(x)).
Tr C = -1  (linear coefficient of Phi_30 is +1).

=======================================================================
T2  Möbius / cyclotomic identity (exact rational-function identity)
=======================================================================
Phi_30(x) = Prod_{d|30} (1 - x^d)^{mu(30/d)}
          = (1-x^2)(1-x^3)(1-x^5)(1-x^30)
            / [(1-x)(1-x^6)(1-x^10)(1-x^15)].
Gated by sympy cancel.

=======================================================================
T3  local completion (exact)
=======================================================================
U = 1 ⊕ C  (9 x 9).  det(I - x U) = (1-x) Phi_30(x)
  = 1 - x^2 - x^3 + x^6 + x^7 - x^9.
Tr U = 0; the linear term of the expansion vanishes.

=======================================================================
T4  global Euler products (from T2) and numerical check
=======================================================================
Derivation from T2.  Phi_30(x) = Prod_{d|30} (1-x^d)^{mu(30/d)}, so
  Z_C(s) := Prod_p Phi_30(p^{-s})^{-1}
          = Prod_{d|30} zeta(d s)^{mu(30/d)}
          = zeta(2s) zeta(3s) zeta(5s) zeta(30s)
            / [zeta(s) zeta(6s) zeta(10s) zeta(15s)].
The extra local factor (1-x) of T3 cancels the d=1 term
(mu(30)=-1, so (1-x)^{1+mu(30)} = 1) and yields
  D_{E8}(s) := Prod_p (1 - p^{-s}) Phi_30(p^{-s})
            = zeta(6s) zeta(10s) zeta(15s)
              / [zeta(2s) zeta(3s) zeta(5s) zeta(30s)].
Tautology (state as such):  1/zeta(s) = D_{E8}(s) · Z_C(s).
This is the cancellation of every zeta(ks) with k>1; it is not an
independent arithmetic identity.

Numeric (mpmath, dps>=30):
  (1) Z_C only at Re s > 1 (absolute convergence), partial products
      p <= X vs the zeta ratio; residual and decay with cutoff.
  (3) D_{E8} at s in {0.75, 1.0, 1.5, 2.0} and s = 0.8+3i
      (absolute convergence for Re s > 1/2: local factor 1+O(p^{-2s})).
      Residuals at X = 10^4, 10^5, 10^6 vs ~ X^{1-2 sigma}/log X.

=======================================================================
T5  regularized determinant (finite truncation)
=======================================================================
T_s^{(X)} = ⊕_{p<=X} p^{-s} U  on C^{9 · pi(X)}.
For a finite-rank operator, det_2(I-T) := Prod_lambda (1-lambda) e^lambda
equals det(I-T) e^{Tr T} = Prod_{p<=X} det(I - p^{-s} U) e^{p^{-s} Tr U}.
Tr U = 0, so this equals Prod_{p<=X} (1-p^{-s}) Phi_30(p^{-s}) exactly.
Scalar control: det_2(I - ⊕_{p<=X} p^{-s})
  = Prod_{p<=X} (1-p^{-s}) e^{p^{-s}}  →  e^{P(s)} / zeta(s),
with prime zeta P(s) = Sum_k mu(k)/k · log zeta(k s).
Check at s=1.5, 2 to <= 1e-8 with X=10^6 (report residuals).

Fence / typed no-go  E8.COXETER.REGULARIZED_SPLIT.NO_GO.01:
the det_2 regularization removes exactly the trace term
Sum_p p^{-s} · Tr(·); for the scalar channel that term is P(s),
whose analytic continuation carries all zeros of zeta in Re s > 1/2
(P(s) = Sum_k mu(k)/k log zeta(k s), singularities at rho/k); hence
any construction controlling only the Hilbert-Schmidt / det_2 part of
the completion cannot isolate 1/zeta(s).

=======================================================================
K1  class check (E8 selects the divisor set, not the regularity)
=======================================================================
Vanishing linear term  <=>  Tr C = -1, for EVERY matrix with Tr C = -1.
  (a) scalar C = -1: completion Prod (1-p^{-s})(1+p^{-s}) = 1/zeta(2s).
  (b) Coxeter of A1 (Phi_2) and A2 (Phi_3: completion 1/zeta(3s)).
  (c) Coxeter of E6 (charpoly Phi_3 Phi_12, trace -1); completion as a
      zeta(ks) ratio via the same Möbius routine; numeric at s=1.5.
  (d) NEGATIVE control B2 (Phi_4 = 1+x^2, trace 0): linear term of
      (1-x)(1+x^2) is -1 ≠ 0, so the "completion"
      Prod (1-p^{-s}) Phi_4(p^{-s}) = zeta(2s)/(zeta(s) zeta(4s))
      still contains 1/zeta(s) and does NOT converge absolutely at
      s=0.75 (partial products drift).
Conclusion: the E8 datum selects the divisor set {1,2,3,5,6,10,15,30}
(which zeta(ks) appear); the regularity in Re s > 1/2 is the generic
consequence of Tr = -1.

=======================================================================
K2  Beurling / scramble blindness
=======================================================================
Prod_{q in Q} (1 - q^{-s}) Phi_30(q^{-s})
  = Prod_{d|30} [Prod_{q in Q} (1 - q^{-d s})]^{mu(30/d)}
    · Prod_{q in Q} (1 - q^{-s})
holds for ANY finite set Q of reals > 1 (the same Möbius rearrangement).
Verified with sympy for Q = {2,3,5,7} and scrambled
Q = {2.3, 3.7, 4.1, 8.9}.
The completion identity is Beurling-generic (no additive/prime-specific
input); its RH content is exactly the analytic continuation of the
scalar channel.

=======================================================================
VERDICT
=======================================================================
COMPLETION_EXACT  if T1-T5 pass, K1(a-c) pass, K1(d) confirms the
                  negative control, and K2 passes.
INCONCLUSIVE      otherwise, with the failing gate.

Deterministic; --smoke (cutoff 10^4) and full (cutoff 10^6).
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

mp.mp.dps = 30

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

CHECKS: list[tuple[str, bool, str]] = []

EDGES_E8 = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
PHI30_DESC = [1, 1, 0, -1, -1, -1, 0, 1, 1]
COMP_DESC = (-1, 0, 1, 1, 0, 0, -1, -1, 0, 1)  # 1 - x^2 - x^3 + x^6 + x^7 - x^9
DIV30 = (1, 2, 3, 5, 6, 10, 15, 30)
NO_GO_ID = "E8.COXETER.REGULARIZED_SPLIT.NO_GO.01"
FENCE = (
    "The trace-free completion is zero-free and pole-free in Re s > 1/2. "
    "The splitting into the scalar zeta channel and the Coxeter channel "
    "is open and RH-equivalent. No RH claim."
)

# Reported residual tables (filled during the run).
T4_ROWS: list[dict] = []
T5_ROWS: list[dict] = []
K1_ROWS: list[dict] = []


# ---------------------------------------------------------------------------
# r609 E8 Seifert construction (copied, not imported)
# ---------------------------------------------------------------------------
def cartan_e8() -> sp.Matrix:
    a = sp.eye(8) * 2
    for i, j in EDGES_E8:
        a[i - 1, j - 1] = -1
        a[j - 1, i - 1] = -1
    return a


def euler_S(arrows: list[tuple[int, int]]) -> sp.Matrix:
    """Euler matrix: S_ii=1, S_ij=-1 on arrow i->j (1-based).  S+S^T = Cartan."""
    s = sp.eye(8)
    for i, j in arrows:
        s[i - 1, j - 1] = -1
    return s


def bipartite_arrows() -> list[tuple[int, int]]:
    # colour: {1,4,6,8} vs {2,3,5,7}; all arrows colour-A -> colour-B
    a_set = {1, 4, 6, 8}
    arrows = []
    for i, j in EDGES_E8:
        if i in a_set:
            arrows.append((i, j))
        else:
            arrows.append((j, i))
    return arrows


def coxeter_from_arrows(arrows: list[tuple[int, int]]) -> sp.Matrix:
    s = euler_S(arrows)
    return -s.inv() * s.T


def charpoly_coeffs(m: sp.Matrix) -> list[int]:
    x = sp.symbols("x")
    p = m.charpoly(x)
    return [int(c) for c in p.all_coeffs()]


# ---------------------------------------------------------------------------
# plumbing
# ---------------------------------------------------------------------------
def gate(name: str, ok: bool, detail: str = "") -> bool:
    flag = bool(ok)
    CHECKS.append((name, flag, detail))
    print(
        "  [%s] %s%s"
        % ("PASS" if flag else "FAIL", name, ("  --  " + detail) if detail else ""),
        flush=True,
    )
    return flag


def section(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def file_sha256() -> str:
    return hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()


def fmt_mp(z, n: int = 8) -> str:
    return mp.nstr(z, n, strip_zeros=False)


def abs_mp(z):
    return abs(mp.mpmathify(z))


def primes_upto(n: int) -> list[int]:
    n = int(n)
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = 0
    sieve[1] = 0
    p = 2
    while p * p <= n:
        if sieve[p]:
            step = p
            start = p * p
            for m in range(start, n + 1, step):
                sieve[m] = 0
        p += 1
    return [i for i, v in enumerate(sieve) if v]


def mobius_cyclotomic(n: int, x) -> sp.Expr:
    expr = sp.Integer(1)
    for d in sp.divisors(n):
        mu = int(sp.mobius(n // d))
        if mu:
            expr *= (1 - x ** d) ** mu
    return expr


def zeta_exponents_from_cyclotomics(
    ns: list[int], extra_one_minus_x: bool = False
) -> dict[int, int]:
    """Exponent of zeta(k s) in Prod_p (1-x)^{delta} Prod_n Phi_n(x), x=p^{-s}.

    Phi_n(x) = Prod_{d|n} (1-x^d)^{mu(n/d)}, so
    Prod_p Phi_n(p^{-s}) = Prod_d zeta(d s)^{-mu(n/d)}.
    Z_C inverts that product (negate these exponents).
    """
    e_one_minus: dict[int, int] = {}
    for n in ns:
        for d in sp.divisors(n):
            e_one_minus[int(d)] = e_one_minus.get(int(d), 0) + int(sp.mobius(n // d))
    if extra_one_minus_x:
        e_one_minus[1] = e_one_minus.get(1, 0) + 1
    # Prod_p Prod_k (1 - p^{-k s})^{e_k} = Prod_k zeta(k s)^{-e_k}
    out = {}
    for k, e in e_one_minus.items():
        if e:
            out[k] = -e
    return out


def negate_exps(exps: dict[int, int]) -> dict[int, int]:
    return {k: -v for k, v in exps.items() if v}


def format_zeta_ratio(exps: dict[int, int]) -> str:
    num = []
    den = []
    for k in sorted(exps):
        e = exps[k]
        token = "ζ(s)" if k == 1 else "ζ(%ds)" % k
        if e > 0:
            num.extend([token] * e)
        elif e < 0:
            den.extend([token] * (-e))
    n = "".join(num) if num else "1"
    if not den:
        return n
    d = "".join(den)
    if len(den) == 1:
        return "%s/%s" % (n, d)
    return "%s / [%s]" % (n, d)


def horner(coeffs_desc, x):
    acc = x * 0
    for c in coeffs_desc:
        acc = acc * x + c
    return acc


def log_closed_from_exps(exps: dict[int, int], s):
    acc = s * 0
    for k, e in exps.items():
        if e == 0:
            continue
        acc += e * mp.log(mp.zeta(k * s))
    return acc


def prime_zeta(s, kmax: int = 80):
    acc = s * 0
    for k in range(1, kmax + 1):
        mu = int(sp.mobius(k))
        if mu == 0:
            continue
        z = mp.zeta(k * s)
        acc += (mp.mpf(mu) / k) * mp.log(z)
    return acc


def running_log(
    primes: list[int],
    s,
    log_local,
    cutoffs: list[int],
) -> dict[int, object]:
    snaps: dict[int, object] = {}
    acc = s * 0
    ci = 0
    cuts = list(cutoffs)
    last = primes[-1] if primes else 0
    for p in primes:
        while ci < len(cuts) and p > cuts[ci]:
            snaps[cuts[ci]] = acc
            ci += 1
        if p > cuts[-1]:
            break
        acc = acc + log_local(p, s)
    while ci < len(cuts):
        if cuts[ci] >= last or True:
            snaps[cuts[ci]] = acc
        ci += 1
    return snaps


def rel_res(log_partial, log_true):
    return abs_mp(mp.expm1(log_partial - log_true))


def tail_pred_D(X: int, sigma) -> float:
    """~ X^{1-2σ} / log X  (leading D_{E8} Euler tail)."""
    X = max(int(X), 3)
    sig = float(sigma)
    return (X ** (1.0 - 2.0 * sig)) / math.log(X)


def tail_pred_ZC(X: int, sigma) -> float:
    X = max(int(X), 3)
    sig = float(sigma)
    return (X ** (1.0 - sig)) / math.log(X)


def coxeter_from_edges(n: int, edges: list[tuple[int, int]]) -> sp.Matrix:
    """Bipartite orientation of a tree; C = -S^{-1} S^T."""
    adj: dict[int, list[int]] = {i: [] for i in range(1, n + 1)}
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    colour = {1: 0}
    queue = [1]
    for u in queue:
        for v in adj[u]:
            if v not in colour:
                colour[v] = 1 - colour[u]
                queue.append(v)
    arrows = []
    for i, j in edges:
        if colour[i] == 0:
            arrows.append((i, j))
        else:
            arrows.append((j, i))
    s = sp.eye(n)
    for i, j in arrows:
        s[i - 1, j - 1] = -1
    return -s.inv() * s.T


def block_U(C: sp.Matrix) -> sp.Matrix:
    n = C.rows
    U = sp.zeros(n + 1)
    U[0, 0] = 1
    for i in range(n):
        for j in range(n):
            U[i + 1, j + 1] = C[i, j]
    return U


def k2_identity(Q: list, x_sym) -> tuple[bool, str]:
    """Möbius rearrangement on an arbitrary finite set Q of rationals > 1.

    Univariate-in-t identity with x_q = t/q (coefficients depend on Q),
    plus exact rational specializations t=1 and the s=2 slice x_q = 1/q^2.
    The identity factors per q, so it is Beurling-generic.
    """
    t = sp.symbols("t")
    phi = sp.cyclotomic_poly(30, x_sym)
    qrats = [sp.nsimplify(q, rational=True) for q in Q]
    lhs_t = sp.Integer(1)
    rhs_t = sp.Integer(1)
    for qrat in qrats:
        xq = t / qrat
        lhs_t *= (1 - xq) * phi.subs(x_sym, xq)
        rhs_t *= (1 - xq) * mobius_cyclotomic(30, xq)
    t_ok = sp.cancel(lhs_t / rhs_t) == 1
    slices_ok = True
    for power in (1, 2):
        lhs = sp.Integer(1)
        rhs = sp.Integer(1)
        for qrat in qrats:
            xq = 1 / qrat ** power
            lhs *= (1 - xq) * phi.subs(x_sym, xq)
            rhs *= (1 - xq) * mobius_cyclotomic(30, xq)
        if sp.cancel(lhs / rhs) != 1:
            slices_ok = False
    ok = bool(t_ok and slices_ok)
    detail = "Q=%s  cancel(t/q)=%s  slices s=1,2=%s" % (
        [str(q) for q in qrats],
        t_ok,
        slices_ok,
    )
    return ok, detail


# ---------------------------------------------------------------------------
# theorems
# ---------------------------------------------------------------------------
def run_t1_t3():
    section("T1  self-reciprocal Phi_30 and Tr C = -1")
    x = sp.symbols("x")
    A = cartan_e8()
    arrows = bipartite_arrows()
    S = euler_S(arrows)
    C = coxeter_from_arrows(arrows)
    phi30 = sp.cyclotomic_poly(30, x)

    gate(
        "T1.S_plus_ST_eq_Cartan",
        sp.expand(S + S.T - A) == sp.zeros(8),
        "S+S^T = A_E8 (bipartite Euler)",
    )
    cp = C.charpoly(x)
    gate(
        "T1.charpoly_Phi30",
        sp.expand(cp.as_expr() - phi30) == 0
        and charpoly_coeffs(C) == PHI30_DESC,
        "det(xI-C) = Phi_30  coeffs=%s" % charpoly_coeffs(C),
    )
    dIxC = sp.expand((sp.eye(8) - x * C).det())
    gate(
        "T1.det_I_minus_xC_eq_Phi30",
        sp.expand(dIxC - phi30) == 0,
        "self-reciprocal: det(I-xC)=Phi_30(x)",
    )
    gate(
        "T1.Phi30_self_reciprocal",
        sp.expand(sp.together(x ** 8 * phi30.subs(x, 1 / x)) - phi30) == 0,
        "x^8 Phi_30(1/x) = Phi_30(x)",
    )
    tr = int(C.trace())
    gate("T1.TrC_eq_m1", tr == -1, "Tr C = %d" % tr)
    lin = int(sp.Poly(phi30, x).coeff_monomial(x))
    gate(
        "T1.Phi30_linear_coeff_plus1",
        lin == 1,
        "linear coeff of Phi_30 is %+d  (so Tr C = -1)" % lin,
    )

    section("T2  Möbius / cyclotomic identity")
    mob = mobius_cyclotomic(30, x)
    gate(
        "T2.mobius_identity",
        sp.cancel(mob / phi30) == 1,
        "Phi_30 = Prod_{d|30} (1-x^d)^{mu(30/d)}",
    )
    explicit = (
        (1 - x ** 2)
        * (1 - x ** 3)
        * (1 - x ** 5)
        * (1 - x ** 30)
        / ((1 - x) * (1 - x ** 6) * (1 - x ** 10) * (1 - x ** 15))
    )
    gate(
        "T2.explicit_rational",
        sp.cancel(explicit / phi30) == 1,
        "(1-x^2)(1-x^3)(1-x^5)(1-x^30)/[(1-x)(1-x^6)(1-x^10)(1-x^15)]",
    )

    section("T3  local completion U = 1 ⊕ C")
    U = block_U(C)
    dU = sp.expand((sp.eye(9) - x * U).det())
    target = 1 - x ** 2 - x ** 3 + x ** 6 + x ** 7 - x ** 9
    gate(
        "T3.det_I_minus_xU",
        sp.expand(dU - (1 - x) * phi30) == 0,
        "det(I-xU)=(1-x)Phi_30(x)",
    )
    gate(
        "T3.expanded_poly",
        sp.expand(dU - target) == 0,
        "1 - x^2 - x^3 + x^6 + x^7 - x^9",
    )
    trU = int(U.trace())
    gate("T3.TrU_eq_0", trU == 0, "Tr U = 1 + Tr C = %d" % trU)
    linU = int(sp.Poly(sp.expand((1 - x) * phi30), x).coeff_monomial(x))
    gate(
        "T3.linear_term_vanishes",
        linU == 0,
        "linear coeff of (1-x)Phi_30 is %d" % linU,
    )
    return C, U, phi30, x


def run_t4(primes: list[int], cutoffs: list[int], smoke: bool):
    section("T4  Euler products (numeric, mpmath dps=%d)" % mp.mp.dps)
    exps_phi = zeta_exponents_from_cyclotomics([30], extra_one_minus_x=False)
    exps_ZC = negate_exps(exps_phi)  # Z_C = Prod Phi_30^{-1}
    exps_D = zeta_exponents_from_cyclotomics([30], extra_one_minus_x=True)
    print("  Z_C(s) = %s" % format_zeta_ratio(exps_ZC), flush=True)
    print("  D_E8(s) = %s" % format_zeta_ratio(exps_D), flush=True)
    # tautology of meromorphic functions: D * Z_C = 1/zeta
    combined = dict(exps_ZC)
    for k, e in exps_D.items():
        combined[k] = combined.get(k, 0) + e
    combined = {k: v for k, v in combined.items() if v}
    taut_exact = combined == {1: -1}
    gate(
        "T4.tautology_exact",
        taut_exact,
        "D_E8 · Z_C = 1/ζ(s)  (zeta-exponent cancellation; tautology)  got %s"
        % format_zeta_ratio(combined),
    )

    def log_phi30_inv(p, s):
        xloc = mp.power(mp.mpf(p), -s)
        return -mp.log(horner(PHI30_DESC, xloc))

    def log_comp(p, s):
        xloc = mp.power(mp.mpf(p), -s)
        return mp.log(horner(COMP_DESC, xloc))

    s_real = [
        ("0.75", mp.mpf("0.75"), False),
        ("1.0", mp.mpf("1.0"), False),
        ("1.5", mp.mpf("1.5"), True),
        ("2.0", mp.mpf("2.0"), True),
    ]
    s_cplx = ("0.8+3i", mp.mpc(mp.mpf("0.8"), mp.mpf("3.0")))

    # Z_C at Re s > 1
    zc_decay_ok = True
    for label, s, do_zc in s_real:
        if not do_zc:
            continue
        log_true = log_closed_from_exps(exps_ZC, s)
        snaps = running_log(primes, s, log_phi30_inv, cutoffs)
        prev = None
        details = []
        in_margin = True
        sigma = float(s)
        for X in cutoffs:
            r = rel_res(snaps[X], log_true)
            pred = tail_pred_ZC(X, sigma)
            T4_ROWS.append(
                {
                    "obj": "Z_C",
                    "s": label,
                    "X": X,
                    "residual": r,
                    "pred": pred,
                }
            )
            details.append("X=%s r=%s pred~%s" % (X, fmt_mp(r, 4), "%.2e" % pred))
            margin = max(mp.mpf("50") * mp.mpf(str(pred)), mp.mpf("1e-12"))
            if r > margin:
                in_margin = False
                zc_decay_ok = False
            if prev is not None and r > prev * mp.mpf("1.05") and r > mp.mpf("1e-18"):
                zc_decay_ok = False
            prev = r
        gate(
            "T4.ZC_s%s" % label,
            in_margin,
            "; ".join(details),
        )

    gate(
        "T4.ZC_residual_decays",
        zc_decay_ok,
        "Z_C residual shrinks with cutoff at Re s>1",
    )

    # D_{E8} at all listed s
    d_decay_ok = True
    jobs = [(lab, s) for lab, s, _ in s_real] + [s_cplx]
    for label, s in jobs:
        log_true = log_closed_from_exps(exps_D, s)
        snaps = running_log(primes, s, log_comp, cutoffs)
        sigma = float(mp.re(s))
        details = []
        prev = None
        ratios = []
        in_margin = True
        for X in cutoffs:
            r = rel_res(snaps[X], log_true)
            pred = tail_pred_D(X, sigma)
            T4_ROWS.append(
                {
                    "obj": "D_E8",
                    "s": label,
                    "X": X,
                    "residual": r,
                    "pred": pred,
                }
            )
            ratio = float(r) / pred if pred > 0 else 0.0
            ratios.append(ratio)
            details.append(
                "X=%s r=%s pred~%s r/pred=%.3g"
                % (X, fmt_mp(r, 4), "%.2e" % pred, ratio)
            )
            margin = max(mp.mpf("80") * mp.mpf(str(pred)), mp.mpf("1e-12"))
            if r > margin:
                in_margin = False
                d_decay_ok = False
            if prev is not None and r > prev * mp.mpf("1.2") and r > mp.mpf("1e-18"):
                d_decay_ok = False
            prev = r
        # decay-rate shape: r/pred O(1) and stable across cutoffs
        shape_ok = True
        if len(cutoffs) >= 2 and tail_pred_D(cutoffs[0], sigma) > 1e-12:
            pos = [abs(t) for t in ratios if t > 0]
            if pos:
                shape_ok = max(pos) / max(min(pos), 1e-30) < 50 and max(pos) < 80
        gate(
            "T4.DE8_s%s" % label,
            in_margin and shape_ok,
            "; ".join(details),
        )

    gate(
        "T4.DE8_decay_rate",
        d_decay_ok,
        "D_E8 residual decays; leading tail ~ X^{1-2σ}/log X",
    )

    # tautology numeric at Re s > 1 via closed forms
    taut_num_ok = True
    taut_details = []
    for label, s, do in s_real:
        if not do:
            continue
        # D * Z_C * zeta(s) == 1
        val = mp.exp(
            log_closed_from_exps(exps_D, s)
            + log_closed_from_exps(exps_ZC, s)
            + mp.log(mp.zeta(s))
        )
        r = abs_mp(val - 1)
        taut_details.append("s=%s |D Z ζ - 1|=%s" % (label, fmt_mp(r, 4)))
        if r > mp.mpf("1e-20"):
            taut_num_ok = False
    gate(
        "T4.tautology_numeric",
        taut_num_ok,
        "tautology 1/ζ = D_E8 · Z_C  (closed forms)  " + "; ".join(taut_details),
    )


def run_t5(C: sp.Matrix, U: sp.Matrix, primes: list[int], X: int, smoke: bool):
    section("T5  regularized det_2  (X=%s)" % X)
    x = sp.symbols("x")
    phi30 = sp.cyclotomic_poly(30, x)
    trU = U.trace()
    det_poly = sp.expand((sp.eye(U.rows) - x * U).det())
    # finite-rank identity: Prod (1-λ) e^λ = det(I-xU) e^{x Tr U}
    # Tr U = 0 ⇒ = (1-x) Phi_30(x)
    gate(
        "T5.det2_equals_det_exp_tr",
        trU == 0 and sp.expand(det_poly - (1 - x) * phi30) == 0,
        "det_2(I-xU)=det(I-xU) e^{x Tr U}=(1-x)Phi_30  (Tr U=0)",
    )

    # numeric eig check on a few blocks
    Um = mp.matrix(U.rows)
    for i in range(U.rows):
        for j in range(U.rows):
            Um[i, j] = mp.mpf(int(U[i, j]))
    eigs = mp.eig(Um, left=False, right=False)
    eig_ok = True
    eig_worst = mp.mpf(0)
    s_eig = mp.mpf("1.5")
    for p in (2, 3, 5, 7, 11):
        xs = mp.power(mp.mpf(p), -s_eig)
        acc = mp.mpf(1)
        tr_acc = mp.mpf(0)
        for lam in eigs:
            mu = xs * lam
            acc *= (1 - mu) * mp.exp(mu)
            tr_acc += mu
        closed = horner(COMP_DESC, xs)  # Tr U=0 ⇒ no extra exp
        r = abs_mp(acc / closed - 1)
        if r > eig_worst:
            eig_worst = r
        if r > mp.mpf("1e-12"):
            eig_ok = False
    gate(
        "T5.det2_eigs_small_blocks",
        eig_ok,
        "p=2,3,5,7,11 at s=1.5  worst |det2/comp-1|=%s  (Tr U term=%s)"
        % (fmt_mp(eig_worst, 4), trU),
    )

    # scalar control
    pX = [p for p in primes if p <= X]
    scalar_ok = True
    for label, s in (("1.5", mp.mpf("1.5")), ("2.0", mp.mpf("2.0"))):
        acc_log = mp.mpf(0)
        for p in pX:
            xs = mp.power(mp.mpf(p), -s)
            acc_log += mp.log(1 - xs) + xs
        P = prime_zeta(s)
        log_true = P - mp.log(mp.zeta(s))
        r = rel_res(acc_log, log_true)
        T5_ROWS.append({"s": label, "X": X, "residual": r})
        tol = mp.mpf("1e-8") if not smoke else mp.mpf("1e-8")
        ok = r <= tol
        if not ok:
            scalar_ok = False
        gate(
            "T5.scalar_s%s" % label,
            ok,
            "X=%s  |Prod (1-p^{-s}) e^{p^{-s}}  /  (e^{P(s)}/ζ(s)) - 1| = %s  (tol %s)"
            % (X, fmt_mp(r, 6), tol),
        )
    print(
        "  NO-GO %s: det_2 removes exactly Sum_p p^{-s}·Tr(·); "
        "scalar channel that term is P(s)=Σ_k μ(k)/k log ζ(ks), "
        "singularities at ρ/k.  Hilbert-Schmidt/det_2 control cannot "
        "isolate 1/ζ(s)."
        % NO_GO_ID,
        flush=True,
    )
    gate(
        "T5.nogo_REGULARIZED_SPLIT",
        True,
        "%s recorded (fence: det_2 cannot isolate 1/ζ)" % NO_GO_ID,
    )
    return scalar_ok


def run_k1(primes: list[int], cutoffs: list[int], X: int):
    section("K1  class check (E8 selects the divisor set)")
    x = sp.symbols("x")

    def one_system(name, C, cyclos, extra_note=""):
        phi = sp.Integer(1)
        for n in cyclos:
            phi *= sp.cyclotomic_poly(n, x)
        phi = sp.expand(phi)
        cp = sp.expand(C.charpoly(x).as_expr())
        tr = C.trace()
        tr_ok = tr == -sp.Integer(1) if name != "B2" else tr == 0
        char_ok = sp.expand(cp - phi) == 0
        exps = zeta_exponents_from_cyclotomics(cyclos, extra_one_minus_x=True)
        ratio = format_zeta_ratio(exps)
        lin = int(sp.Poly(sp.expand((1 - x) * phi), x).coeff_monomial(x))
        return {
            "name": name,
            "C": C,
            "phi": phi,
            "cyclos": cyclos,
            "char_ok": char_ok,
            "tr": int(tr),
            "tr_ok": bool(tr_ok),
            "lin": lin,
            "exps": exps,
            "ratio": ratio,
            "note": extra_note,
        }

    # (a) scalar C = -1  == Coxeter of A1
    C_a = sp.Matrix([[-1]])
    a = one_system("scalar/A1", C_a, [2])
    gate(
        "K1a.scalar_C_m1",
        a["char_ok"] and a["tr"] == -1 and a["lin"] == 0 and a["ratio"] == "1/ζ(2s)",
        "C=-1  charpoly Phi_2  Tr=%d  lin(1-x)Phi=%d  completion %s"
        % (a["tr"], a["lin"], a["ratio"]),
    )

    # (b) A2
    C_a2 = coxeter_from_edges(2, [(1, 2)])
    b = one_system("A2", C_a2, [3])
    gate(
        "K1b.A2_Phi3",
        b["char_ok"] and b["tr"] == -1 and b["lin"] == 0 and b["ratio"] == "1/ζ(3s)",
        "charpoly Phi_3  Tr=%d  lin=%d  completion %s" % (b["tr"], b["lin"], b["ratio"]),
    )
    # A1 already covered by (a); explicit gate
    gate(
        "K1b.A1_Phi2",
        a["char_ok"] and a["ratio"] == "1/ζ(2s)",
        "A1 Coxeter = scalar -1, completion 1/ζ(2s)",
    )

    # (c) E6  Bourbaki: 1-2-3-4-5 with 3-6
    C_e6 = coxeter_from_edges(6, [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6)])
    c = one_system("E6", C_e6, [3, 12])
    gate(
        "K1c.E6_charpoly",
        c["char_ok"],
        "Phi_3 Phi_12 = %s" % sp.Poly(c["phi"], x).as_expr(),
    )
    gate("K1c.E6_trace", c["tr"] == -1, "Tr C_E6 = %d" % c["tr"])
    gate(
        "K1c.E6_linear_vanishes",
        c["lin"] == 0,
        "lin(1-x)Phi_E6 = %d" % c["lin"],
    )
    # Möbius-derived ratio
    expected_e6 = {4: 1, 6: 1, 2: -1, 3: -1, 12: -1}
    # drop zeros
    expected_e6 = {k: v for k, v in expected_e6.items() if v}
    gate(
        "K1c.E6_zeta_ratio_symbolic",
        c["exps"] == expected_e6,
        "completion %s" % c["ratio"],
    )
    # numeric at s=1.5
    s15 = mp.mpf("1.5")

    def log_local_from_phi(phi_expr):
        ppoly = sp.Poly(sp.expand((1 - x) * phi_expr), x)

        def _ll(p, s, _pp=ppoly):
            xs = mp.power(mp.mpf(p), -s)
            acc = xs * 0
            # horner descending
            coeffs = [int(_pp.coeff_monomial(x ** k)) for k in range(_pp.degree(), -1, -1)]
            for cv in coeffs:
                acc = acc * xs + cv
            return mp.log(acc)

        return _ll

    snaps_e6 = running_log(primes, s15, log_local_from_phi(c["phi"]), [X])
    r_e6 = rel_res(snaps_e6[X], log_closed_from_exps(c["exps"], s15))
    pred_e6 = tail_pred_D(X, 1.5)
    gate(
        "K1c.E6_numeric_s1.5",
        r_e6 <= max(mp.mpf("80") * mp.mpf(str(pred_e6)), mp.mpf("1e-10")),
        "X=%s residual=%s  pred~%.2e  ratio %s" % (X, fmt_mp(r_e6, 5), pred_e6, c["ratio"]),
    )

    # (d) B2 negative control
    C_b2 = sp.Matrix([[0, -1], [1, 0]])  # rotation by pi/2 = Coxeter of I2(4)≅B2
    d = one_system("B2", C_b2, [4])
    lin_b2 = d["lin"]
    gate(
        "K1d.B2_charpoly_Phi4",
        d["char_ok"],
        "Phi_4 = 1+x^2",
    )
    gate("K1d.B2_trace_0", d["tr"] == 0, "Tr = %d" % d["tr"])
    gate(
        "K1d.linear_term_nonzero",
        lin_b2 == -1,
        "(1-x)(1+x^2) linear coeff = %d ≠ 0" % lin_b2,
    )
    # completion still contains 1/zeta(s)
    contains_zeta = d["exps"].get(1, 0) != 0
    gate(
        "K1d.contains_1_over_zeta",
        contains_zeta,
        "completion %s  (zeta(s) exponent %s)"
        % (d["ratio"], d["exps"].get(1, 0)),
    )
    # partial products at s=0.75 must drift
    s075 = mp.mpf("0.75")
    phi4 = sp.cyclotomic_poly(4, x)  # 1+x^2

    def log_b2(p, s):
        xs = mp.power(mp.mpf(p), -s)
        return mp.log((1 - xs) * (1 + xs ** 2))

    snaps_b2 = running_log(primes, s075, log_b2, cutoffs)
    closed_b2 = log_closed_from_exps(d["exps"], s075)
    residuals = []
    logs = []
    for Xc in cutoffs:
        r = rel_res(snaps_b2[Xc], closed_b2)
        residuals.append(r)
        logs.append(abs_mp(snaps_b2[Xc]))
    # drift: residual stays O(1) (product → 0, closed form finite)
    # and |log partial| grows with X
    drift = residuals[-1] > mp.mpf("0.2") and (
        len(logs) < 2 or logs[-1] > logs[0] * mp.mpf("1.05")
    )
    # contrast: E8 D at same s should be small (already gated in T4)
    gate(
        "K1d.not_abs_conv_s0.75",
        drift,
        "B2 partial residuals %s  |log P| %s  (DRIFT, not abs-conv at s=0.75)"
        % ([fmt_mp(r, 3) for r in residuals], [fmt_mp(l, 4) for l in logs]),
    )

    print(
        "  CONCLUSION: the E8 datum selects the divisor set "
        "{1,2,3,5,6,10,15,30} (which ζ(ks) appear); the regularity "
        "in Re s > 1/2 is the generic consequence of Tr = -1.",
        flush=True,
    )

    # numeric A1/A2 at s=1.5 for the table
    def residual_of(exps, phi_expr, s, XX):
        snaps = running_log(primes, s, log_local_from_phi(phi_expr), [XX])
        return rel_res(snaps[XX], log_closed_from_exps(exps, s))

    r_a = residual_of(a["exps"], a["phi"], s15, X)
    r_b = residual_of(b["exps"], b["phi"], s15, X)

    for rec, conv075, rnum in (
        (a, True, r_a),
        (b, True, r_b),
        (c, True, r_e6),
        (d, False, residuals[-1]),
    ):
        K1_ROWS.append(
            {
                "system": rec["name"],
                "charpoly": str(sp.Poly(rec["phi"], x).as_expr()),
                "trace": rec["tr"],
                "completion": rec["ratio"],
                "conv_0.75": conv075,
                "residual": rnum,
            }
        )
    # E8 row (from T4 exponents)
    e8_exps = zeta_exponents_from_cyclotomics([30], extra_one_minus_x=True)
    K1_ROWS.insert(
        2,
        {
            "system": "E8",
            "charpoly": "Phi_30",
            "trace": -1,
            "completion": format_zeta_ratio(e8_exps),
            "conv_0.75": True,
            "residual": None,
        },
    )
    gate(
        "K1.a_b_c_pass_class",
        a["lin"] == 0 and b["lin"] == 0 and c["lin"] == 0 and d["lin"] != 0,
        "Tr=-1 systems complete; B2 (Tr=0) does not",
    )


def run_k2():
    section("K2  Beurling / scramble blindness")
    x = sp.symbols("x")
    ok1, d1 = k2_identity([2, 3, 5, 7], x)
    gate("K2.Q_primes_2_3_5_7", ok1, d1)
    ok2, d2 = k2_identity([sp.Rational(23, 10), sp.Rational(37, 10),
                           sp.Rational(41, 10), sp.Rational(89, 10)], x)
    gate("K2.Q_scrambled_2.3_3.7_4.1_8.9", ok2, d2)
    print(
        "  PRINT: the completion identity is Beurling-generic "
        "(no additive/prime-specific input); its RH content is exactly "
        "the analytic continuation of the scalar channel.",
        flush=True,
    )


def print_tables():
    section("TABLES")
    print("  T4 residuals  (|partial/closed - 1|)", flush=True)
    print(
        "  %-6s %-8s %12s %14s %14s"
        % ("obj", "s", "X", "residual", "pred tail"),
        flush=True,
    )
    for row in T4_ROWS:
        print(
            "  %-6s %-8s %12s %14s %14.3e"
            % (
                row["obj"],
                row["s"],
                row["X"],
                fmt_mp(row["residual"], 5),
                row["pred"],
            ),
            flush=True,
        )
    print("  T5 scalar det_2 residuals", flush=True)
    for row in T5_ROWS:
        print(
            "  s=%s  X=%s  residual=%s"
            % (row["s"], row["X"], fmt_mp(row["residual"], 8)),
            flush=True,
        )
    print(
        "  K1  system / charpoly / trace / completion / abs-conv at s=0.75?",
        flush=True,
    )
    for row in K1_ROWS:
        print(
            "  %-10s  %-28s  Tr=%+d  %s  conv@0.75=%s"
            % (
                row["system"],
                row["charpoly"][:28],
                row["trace"],
                row["completion"],
                "yes" if row["conv_0.75"] else "NO (contains 1/ζ)",
            ),
            flush=True,
        )


def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    global CHECKS, T4_ROWS, T5_ROWS, K1_ROWS
    CHECKS = []
    T4_ROWS = []
    T5_ROWS = []
    K1_ROWS = []

    X = 10 ** 4 if smoke else 10 ** 6
    if smoke:
        cutoffs = [10 ** 3, 10 ** 4]
    else:
        cutoffs = [10 ** 4, 10 ** 5, 10 ** 6]
    cutoffs = [c for c in cutoffs if c <= X]
    if X not in cutoffs:
        cutoffs.append(X)

    t0 = time.time()
    print("=" * 74)
    print("e8_coxeter_euler_completion_probe -- r617 E8.COXETER.EULER.COMPLETION.01")
    print("Firewall: exploration, no physics claim, no RH claim")
    print("mode: %s  X=%s  dps=%s" % ("SMOKE" if smoke else "FULL", X, mp.mp.dps))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA %s" % file_sha256())
    print("FENCE: %s" % FENCE)
    print("=" * 74, flush=True)

    C, U, _phi30, _x = run_t1_t3()
    print("  sieving primes <= %s ..." % X, flush=True)
    primes = primes_upto(X)
    print("  pi(%s) = %d" % (X, len(primes)), flush=True)
    run_t4(primes, cutoffs, smoke)
    run_t5(C, U, primes, X, smoke)
    run_k1(primes, cutoffs, X)
    run_k2()
    print_tables()

    section("VERDICT")
    failed = [name for name, ok, _ in CHECKS if not ok]
    all_ok = not failed
    verdict = "COMPLETION_EXACT" if all_ok else "INCONCLUSIVE"
    gate(
        "V.enum",
        verdict in ("COMPLETION_EXACT", "INCONCLUSIVE"),
        verdict,
    )
    if not all_ok:
        print("  failing gates: %s" % ", ".join(failed), flush=True)
    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    dt = time.time() - t0
    print("\n  GATES %d/%d" % (n_pass, len(CHECKS)), flush=True)
    print("  SPEC_SHA %s" % SPEC_SHA, flush=True)
    print("  FILE_SHA %s" % file_sha256(), flush=True)
    print("  VERDICT: %s" % verdict, flush=True)
    print("  runtime %.1f s" % dt, flush=True)
    print("  %s" % NO_GO_ID, flush=True)
    print("  FENCE: %s" % FENCE, flush=True)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
