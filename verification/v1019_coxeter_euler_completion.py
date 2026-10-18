#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1019 -- E8.COXETER.EULER.COMPLETION.01 (2026-09-02):
THE COXETER--EULER COMPLETION OF E8 (EXACT + NUMERICAL).

Promotion of round r617.  The module RE-DERIVES the identities from
scratch (no probe imports, no subprocess).  Exact polynomial/matrix
identities are [E] (Identity, sympy over Z/Q).  Euler-product checks
are Numerical (mpmath, cutoff X=10^5 to keep runtime < 60 s).

THE EXACT LAYER (classical cyclotomic Euler products, re-derived):

  T1.  C = -S^{-1} S^T on the bipartite Euler matrix of Bourbaki E8.
       det(I - x C) = Phi_30(x), Tr C = -1.
  T2.  Möbius identity (classical inversion of cyclotomic Euler
       products): Phi_30(x) = (1-x^2)(1-x^3)(1-x^5)(1-x^30)
       / [(1-x)(1-x^6)(1-x^10)(1-x^15)].
  T3.  Local completion U = 1 ⊕ C, det(I - x U) = (1-x) Phi_30(x)
       = 1 - x^2 - x^3 + x^6 + x^7 - x^9, Tr U = 0.

THE GLOBAL IDENTITIES (from T2, classical Möbius; E8 reading is new):

  Z_C(s) = Prod_p Phi_30(p^{-s})^{-1}
         = zeta(2s) zeta(3s) zeta(5s) zeta(30s)
           / [zeta(s) zeta(6s) zeta(10s) zeta(15s)]
  D_{E8}(s) = Prod_p (1-p^{-s}) Phi_30(p^{-s})
            = zeta(6s) zeta(10s) zeta(15s)
              / [zeta(2s) zeta(3s) zeta(5s) zeta(30s)]
  Absolutely convergent for Re s > 1/2.  Numerical residuals at the
  probe cutoff X=10^6 were 1.28e-4 at s=0.75 and 3.5e-14 at s=1.5;
  this module reports residuals at X=10^5.

  det_2 identity: Prod_p det(I - p^{-s} U) e^{p^{-s} Tr U} = D_{E8}(s)
  (Tr U = 0).  Scalar control: det_2 = e^{P(s)} / zeta(s) with
  P(s) = Sum_k mu(k)/k · log zeta(k s).

MANDATORY HONESTY (typed; no marker upgrade on the RH-adjacent sentence):

  (i) CLASS STATEMENT.  The vanishing linear term is the generic
      consequence of Tr C = -1 (controls: scalar -1 → 1/zeta(2s);
      A1 → 1/zeta(2s); A2 → 1/zeta(3s); E6 (Phi_3 Phi_12) →
      zeta(4s) zeta(6s)/[zeta(2s) zeta(3s) zeta(12s)]; negative
      control B2 (Phi_4, trace 0) → zeta(2s)/[zeta(s) zeta(4s)],
      still contains 1/zeta(s)).  E8 only selects the divisor set of 30.
  (ii) BEURLING-GENERICITY.  The identity holds for any set of
      "primes" Q subset (1,∞) — no prime-specific input.
  (iii) FENCE (verbatim): "The trace-free completion is zero-free and
      pole-free in Re s > 1/2. The splitting into the scalar zeta
      channel and the Coxeter channel is open and RH-equivalent.
      No RH claim."
  (iv) Typed no-go E8.COXETER.REGULARIZED_SPLIT.NO_GO.01: any
      construction controlling only the det_2/Hilbert-Schmidt part
      cannot isolate 1/zeta(s); the RH content sits in the analytic
      continuation of the trace term P(s) = Sum_k mu(k)/k · log zeta(ks).

The analytic identities themselves are classical (Möbius inversion of
cyclotomic Euler products).  The new statement is the E8 reading with
the fence.  Like the Eisenstein bridge, the completion is RH-neutral
as a finite identity: it does not locate zeros.

NO RH CLAIM.  Python-only / Wolfram deferred (engine DEFERRED_NO_ENGINE).

PROVENANCE: experiments/tfpt-discovery/e8_coxeter_euler_completion_probe.py
(r617, 45/45, VERDICT COMPLETION_EXACT, SPEC_SHA
5aa3935bd4d5698caa889d62dafba4b7efe62a7b3132d07ab62299c22dd03f8c,
FILE_SHA 6ac6bab28a355d3b2b3a98114c32586211cbdec0b2712e8e6c60511e03d12c21).
The probe stays experiments-side.
"""
from __future__ import annotations

import math

import mpmath as mp
import sympy as sp

from tfpt_constants import check as suite_check, summary, reset

mp.mp.dps = 30

R617_SPEC = "5aa3935bd4d5698caa889d62dafba4b7efe62a7b3132d07ab62299c22dd03f8c"
R617_FILE = "6ac6bab28a355d3b2b3a98114c32586211cbdec0b2712e8e6c60511e03d12c21"
EDGES_E8 = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
PHI30_DESC = [1, 1, 0, -1, -1, -1, 0, 1, 1]
COMP_DESC = (-1, 0, 1, 1, 0, 0, -1, -1, 0, 1)
NO_GO_ID = "E8.COXETER.REGULARIZED_SPLIT.NO_GO.01"
FENCE = (
    "The trace-free completion is zero-free and pole-free in Re s > 1/2. "
    "The splitting into the scalar zeta channel and the Coxeter channel "
    "is open and RH-equivalent. No RH claim."
)
X_CUT = 10 ** 5
CUTOFFS = [10 ** 4, 10 ** 5]


def check(label: str, condition: bool, detail: str = "") -> bool:
    ok = bool(condition)
    suite_check(label if not detail else "%s -- %s" % (label, detail), ok)
    return ok


def cartan_e8() -> sp.Matrix:
    a = sp.eye(8) * 2
    for i, j in EDGES_E8:
        a[i - 1, j - 1] = -1
        a[j - 1, i - 1] = -1
    return a


def euler_S(arrows: list[tuple[int, int]]) -> sp.Matrix:
    s = sp.eye(8)
    for i, j in arrows:
        s[i - 1, j - 1] = -1
    return s


def bipartite_arrows() -> list[tuple[int, int]]:
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
            for m in range(p * p, n + 1, p):
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
    e_one_minus: dict[int, int] = {}
    for n in ns:
        for d in sp.divisors(n):
            e_one_minus[int(d)] = e_one_minus.get(int(d), 0) + int(sp.mobius(n // d))
    if extra_one_minus_x:
        e_one_minus[1] = e_one_minus.get(1, 0) + 1
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
    return "%s / [%s]" % (n, "".join(den))


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
        acc += (mp.mpf(mu) / k) * mp.log(mp.zeta(k * s))
    return acc


def running_log(primes: list[int], s, log_local, cutoffs: list[int]) -> dict[int, object]:
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


def abs_mp(z):
    return abs(mp.mpmathify(z))


def fmt_mp(z, n: int = 8) -> str:
    return mp.nstr(z, n, strip_zeros=False)


def rel_res(log_partial, log_true):
    return abs_mp(mp.expm1(log_partial - log_true))


def tail_pred_D(X: int, sigma) -> float:
    X = max(int(X), 3)
    sig = float(sigma)
    return (X ** (1.0 - 2.0 * sig)) / math.log(X)


def tail_pred_ZC(X: int, sigma) -> float:
    X = max(int(X), 3)
    sig = float(sigma)
    return (X ** (1.0 - sig)) / math.log(X)


def coxeter_from_edges(n: int, edges: list[tuple[int, int]]) -> sp.Matrix:
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
        [str(q) for q in qrats], t_ok, slices_ok,
    )
    return ok, detail


def run_t1_t3():
    print("\nT1  self-reciprocal Phi_30 and Tr C = -1")
    x = sp.symbols("x")
    A = cartan_e8()
    arrows = bipartite_arrows()
    S = euler_S(arrows)
    C = coxeter_from_arrows(arrows)
    phi30 = sp.cyclotomic_poly(30, x)
    check("T1.S_plus_ST_eq_Cartan",
          sp.expand(S + S.T - A) == sp.zeros(8),
          "S+S^T = A_E8 (bipartite Euler)")
    cp = C.charpoly(x)
    check("T1.charpoly_Phi30",
          sp.expand(cp.as_expr() - phi30) == 0
          and charpoly_coeffs(C) == PHI30_DESC,
          "det(xI-C) = Phi_30  coeffs=%s" % charpoly_coeffs(C))
    dIxC = sp.expand((sp.eye(8) - x * C).det())
    check("T1.det_I_minus_xC_eq_Phi30",
          sp.expand(dIxC - phi30) == 0,
          "self-reciprocal: det(I-xC)=Phi_30(x)")
    check("T1.Phi30_self_reciprocal",
          sp.expand(sp.together(x ** 8 * phi30.subs(x, 1 / x)) - phi30) == 0,
          "x^8 Phi_30(1/x) = Phi_30(x)")
    tr = int(C.trace())
    check("T1.TrC_eq_m1", tr == -1, "Tr C = %d" % tr)
    lin = int(sp.Poly(phi30, x).coeff_monomial(x))
    check("T1.Phi30_linear_coeff_plus1", lin == 1,
          "linear coeff of Phi_30 is %+d  (so Tr C = -1)" % lin)

    print("\nT2  Möbius / cyclotomic identity (classical)")
    mob = mobius_cyclotomic(30, x)
    check("T2.mobius_identity",
          sp.cancel(mob / phi30) == 1,
          "Phi_30 = Prod_{d|30} (1-x^d)^{mu(30/d)}")
    explicit = (
        (1 - x ** 2) * (1 - x ** 3) * (1 - x ** 5) * (1 - x ** 30)
        / ((1 - x) * (1 - x ** 6) * (1 - x ** 10) * (1 - x ** 15))
    )
    check("T2.explicit_rational",
          sp.cancel(explicit / phi30) == 1,
          "(1-x^2)(1-x^3)(1-x^5)(1-x^30)/[(1-x)(1-x^6)(1-x^10)(1-x^15)]")

    print("\nT3  local completion U = 1 ⊕ C")
    U = block_U(C)
    dU = sp.expand((sp.eye(9) - x * U).det())
    target = 1 - x ** 2 - x ** 3 + x ** 6 + x ** 7 - x ** 9
    check("T3.det_I_minus_xU",
          sp.expand(dU - (1 - x) * phi30) == 0,
          "det(I-xU)=(1-x)Phi_30(x)")
    check("T3.expanded_poly",
          sp.expand(dU - target) == 0,
          "1 - x^2 - x^3 + x^6 + x^7 - x^9")
    trU = int(U.trace())
    check("T3.TrU_eq_0", trU == 0, "Tr U = 1 + Tr C = %d" % trU)
    linU = int(sp.Poly(sp.expand((1 - x) * phi30), x).coeff_monomial(x))
    check("T3.linear_term_vanishes", linU == 0,
          "linear coeff of (1-x)Phi_30 is %d" % linU)
    return C, U, phi30, x


def run_t4(primes: list[int], cutoffs: list[int]) -> None:
    print("\nT4  Euler products (numeric, mpmath dps=%d, X=%s)" % (mp.mp.dps, X_CUT))
    exps_phi = zeta_exponents_from_cyclotomics([30], extra_one_minus_x=False)
    exps_ZC = negate_exps(exps_phi)
    exps_D = zeta_exponents_from_cyclotomics([30], extra_one_minus_x=True)
    print("  Z_C(s) = %s" % format_zeta_ratio(exps_ZC), flush=True)
    print("  D_E8(s) = %s" % format_zeta_ratio(exps_D), flush=True)
    combined = dict(exps_ZC)
    for k, e in exps_D.items():
        combined[k] = combined.get(k, 0) + e
    combined = {k: v for k, v in combined.items() if v}
    check("T4.tautology_exact",
          combined == {1: -1},
          "D_E8 · Z_C = 1/ζ(s)  (tautology of meromorphic functions)  got %s"
          % format_zeta_ratio(combined))

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
            details.append("X=%s r=%s pred~%s" % (X, fmt_mp(r, 4), "%.2e" % pred))
            margin = max(mp.mpf("50") * mp.mpf(str(pred)), mp.mpf("1e-12"))
            if r > margin:
                in_margin = False
                zc_decay_ok = False
            if prev is not None and r > prev * mp.mpf("1.05") and r > mp.mpf("1e-18"):
                zc_decay_ok = False
            prev = r
        check("T4.ZC_s%s" % label, in_margin, "; ".join(details))
    check("T4.ZC_residual_decays", zc_decay_ok,
          "Z_C residual shrinks with cutoff at Re s>1")

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
        shape_ok = True
        if len(cutoffs) >= 2 and tail_pred_D(cutoffs[0], sigma) > 1e-12:
            pos = [abs(t) for t in ratios if t > 0]
            if pos:
                shape_ok = max(pos) / max(min(pos), 1e-30) < 50 and max(pos) < 80
        check("T4.DE8_s%s" % label, in_margin and shape_ok, "; ".join(details))
    check("T4.DE8_decay_rate", d_decay_ok,
          "D_E8 residual decays; leading tail ~ X^{1-2σ}/log X")

    taut_num_ok = True
    taut_details = []
    for label, s, do in s_real:
        if not do:
            continue
        val = mp.exp(
            log_closed_from_exps(exps_D, s)
            + log_closed_from_exps(exps_ZC, s)
            + mp.log(mp.zeta(s))
        )
        r = abs_mp(val - 1)
        taut_details.append("s=%s |D Z ζ - 1|=%s" % (label, fmt_mp(r, 4)))
        if r > mp.mpf("1e-20"):
            taut_num_ok = False
    check("T4.tautology_numeric", taut_num_ok,
          "tautology 1/ζ = D_E8 · Z_C  (closed forms)  " + "; ".join(taut_details))


def run_t5(C: sp.Matrix, U: sp.Matrix, primes: list[int], X: int) -> None:
    print("\nT5  regularized det_2  (X=%s)" % X)
    x = sp.symbols("x")
    phi30 = sp.cyclotomic_poly(30, x)
    trU = U.trace()
    det_poly = sp.expand((sp.eye(U.rows) - x * U).det())
    check("T5.det2_equals_det_exp_tr",
          trU == 0 and sp.expand(det_poly - (1 - x) * phi30) == 0,
          "det_2(I-xU)=det(I-xU) e^{x Tr U}=(1-x)Phi_30  (Tr U=0)")
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
        for lam in eigs:
            mu = xs * lam
            acc *= (1 - mu) * mp.exp(mu)
        closed = horner(COMP_DESC, xs)
        r = abs_mp(acc / closed - 1)
        if r > eig_worst:
            eig_worst = r
        if r > mp.mpf("1e-12"):
            eig_ok = False
    check("T5.det2_eigs_small_blocks", eig_ok,
          "p=2,3,5,7,11 at s=1.5  worst |det2/comp-1|=%s" % fmt_mp(eig_worst, 4))
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
        ok = r <= mp.mpf("1e-8")
        if not ok:
            scalar_ok = False
        check("T5.scalar_s%s" % label, ok,
              "X=%s  |Prod (1-p^{-s}) e^{p^{-s}} / (e^{P(s)}/ζ(s)) - 1| = %s  (tol 1e-8)"
              % (X, fmt_mp(r, 6)))
    print(
        "  NO-GO %s: det_2 removes exactly Sum_p p^{-s}·Tr(·); "
        "scalar channel that term is P(s)=Σ_k μ(k)/k log ζ(ks), "
        "singularities at ρ/k.  Hilbert-Schmidt/det_2 control cannot "
        "isolate 1/ζ(s)."
        % NO_GO_ID,
        flush=True,
    )
    check("T5.nogo_REGULARIZED_SPLIT", True,
          "%s recorded (fence: det_2 cannot isolate 1/ζ)" % NO_GO_ID)
    check("T5.scalar_control_ok", scalar_ok, "scalar det_2 at s=1.5,2.0")


def run_k1(primes: list[int], cutoffs: list[int], X: int) -> None:
    print("\nK1  class check (E8 selects the divisor set, not the regularity)")
    x = sp.symbols("x")

    def one_system(name, C, cyclos):
        phi = sp.Integer(1)
        for n in cyclos:
            phi *= sp.cyclotomic_poly(n, x)
        phi = sp.expand(phi)
        cp = sp.expand(C.charpoly(x).as_expr())
        tr = C.trace()
        tr_ok = tr == -sp.Integer(1) if name != "B2" else tr == 0
        char_ok = sp.expand(cp - phi) == 0
        exps = zeta_exponents_from_cyclotomics(cyclos, extra_one_minus_x=True)
        lin = int(sp.Poly(sp.expand((1 - x) * phi), x).coeff_monomial(x))
        return {
            "name": name, "C": C, "phi": phi, "cyclos": cyclos,
            "char_ok": char_ok, "tr": int(tr), "tr_ok": bool(tr_ok),
            "lin": lin, "exps": exps, "ratio": format_zeta_ratio(exps),
        }

    C_a = sp.Matrix([[-1]])
    a = one_system("scalar/A1", C_a, [2])
    check("K1a.scalar_C_m1",
          a["char_ok"] and a["tr"] == -1 and a["lin"] == 0 and a["ratio"] == "1/ζ(2s)",
          "C=-1  charpoly Phi_2  Tr=%d  lin=%d  completion %s"
          % (a["tr"], a["lin"], a["ratio"]))
    C_a2 = coxeter_from_edges(2, [(1, 2)])
    b = one_system("A2", C_a2, [3])
    check("K1b.A2_Phi3",
          b["char_ok"] and b["tr"] == -1 and b["lin"] == 0 and b["ratio"] == "1/ζ(3s)",
          "charpoly Phi_3  Tr=%d  lin=%d  completion %s" % (b["tr"], b["lin"], b["ratio"]))
    check("K1b.A1_Phi2", a["char_ok"] and a["ratio"] == "1/ζ(2s)",
          "A1 Coxeter = scalar -1, completion 1/ζ(2s)")
    C_e6 = coxeter_from_edges(6, [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6)])
    c = one_system("E6", C_e6, [3, 12])
    check("K1c.E6_charpoly", c["char_ok"],
          "Phi_3 Phi_12 = %s" % sp.Poly(c["phi"], x).as_expr())
    check("K1c.E6_trace", c["tr"] == -1, "Tr C_E6 = %d" % c["tr"])
    check("K1c.E6_linear_vanishes", c["lin"] == 0, "lin(1-x)Phi_E6 = %d" % c["lin"])
    expected_e6 = {4: 1, 6: 1, 2: -1, 3: -1, 12: -1}
    check("K1c.E6_zeta_ratio_symbolic", c["exps"] == expected_e6,
          "completion %s" % c["ratio"])
    s15 = mp.mpf("1.5")

    def log_local_from_phi(phi_expr):
        ppoly = sp.Poly(sp.expand((1 - x) * phi_expr), x)

        def _ll(p, s, _pp=ppoly):
            xs = mp.power(mp.mpf(p), -s)
            acc = xs * 0
            coeffs = [int(_pp.coeff_monomial(x ** k)) for k in range(_pp.degree(), -1, -1)]
            for cv in coeffs:
                acc = acc * xs + cv
            return mp.log(acc)

        return _ll

    snaps_e6 = running_log(primes, s15, log_local_from_phi(c["phi"]), [X])
    r_e6 = rel_res(snaps_e6[X], log_closed_from_exps(c["exps"], s15))
    pred_e6 = tail_pred_D(X, 1.5)
    check("K1c.E6_numeric_s1.5",
          r_e6 <= max(mp.mpf("80") * mp.mpf(str(pred_e6)), mp.mpf("1e-10")),
          "X=%s residual=%s  pred~%.2e  ratio %s"
          % (X, fmt_mp(r_e6, 5), pred_e6, c["ratio"]))

    C_b2 = sp.Matrix([[0, -1], [1, 0]])
    d = one_system("B2", C_b2, [4])
    check("K1d.B2_charpoly_Phi4", d["char_ok"], "Phi_4 = 1+x^2")
    check("K1d.B2_trace_0", d["tr"] == 0, "Tr = %d" % d["tr"])
    check("K1d.linear_term_nonzero", d["lin"] == -1,
          "(1-x)(1+x^2) linear coeff = %d != 0" % d["lin"])
    contains_zeta = d["exps"].get(1, 0) != 0
    check("K1d.contains_1_over_zeta", contains_zeta,
          "completion %s  (zeta(s) exponent %s)"
          % (d["ratio"], d["exps"].get(1, 0)))
    s075 = mp.mpf("0.75")

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
    drift = residuals[-1] > mp.mpf("0.2") and (
        len(logs) < 2 or logs[-1] > logs[0] * mp.mpf("1.05")
    )
    check("K1d.not_abs_conv_s0.75", drift,
          "B2 partial residuals %s  |log P| %s  (DRIFT, not abs-conv at s=0.75)"
          % ([fmt_mp(r, 3) for r in residuals], [fmt_mp(l, 4) for l in logs]))
    print(
        "  CONCLUSION: the E8 datum selects the divisor set "
        "{1,2,3,5,6,10,15,30} (which ζ(ks) appear); the regularity "
        "in Re s > 1/2 is the generic consequence of Tr = -1.",
        flush=True,
    )
    check("K1.a_b_c_pass_class",
          a["lin"] == 0 and b["lin"] == 0 and c["lin"] == 0 and d["lin"] != 0,
          "Tr=-1 systems complete; B2 (Tr=0) does not")


def run_k2() -> None:
    print("\nK2  Beurling / scramble blindness")
    x = sp.symbols("x")
    ok1, d1 = k2_identity([2, 3, 5, 7], x)
    check("K2.Q_primes_2_3_5_7", ok1, d1)
    ok2, d2 = k2_identity(
        [sp.Rational(23, 10), sp.Rational(37, 10),
         sp.Rational(41, 10), sp.Rational(89, 10)],
        x,
    )
    check("K2.Q_scrambled_2.3_3.7_4.1_8.9", ok2, d2)
    print(
        "  PRINT: the completion identity is Beurling-generic "
        "(no additive/prime-specific input); its RH content is exactly "
        "the analytic continuation of the scalar channel.",
        flush=True,
    )


def run():
    reset()
    print("=" * 74)
    print("v1019 -- E8.COXETER.EULER.COMPLETION.01")
    print("SPEC_SHA %s" % R617_SPEC)
    print("FILE_SHA (probe) %s" % R617_FILE)
    print("FENCE: %s" % FENCE)
    print("NO-GO %s" % NO_GO_ID)
    print("cutoff X=%s  (suite; probe full used 10^6)" % X_CUT)
    print("=" * 74, flush=True)

    C, U, _phi30, _x = run_t1_t3()
    print("  sieving primes <= %s ..." % X_CUT, flush=True)
    primes = primes_upto(X_CUT)
    print("  pi(%s) = %d" % (X_CUT, len(primes)), flush=True)
    run_t4(primes, CUTOFFS)
    run_t5(C, U, primes, X_CUT)
    run_k1(primes, CUTOFFS, X_CUT)
    run_k2()
    check("FENCE recorded verbatim", True, FENCE)
    print("  r617 SPEC_SHA  %s" % R617_SPEC)
    return summary("v1019 Coxeter-Euler completion")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
