#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bsd_stage_a_cm_quotient_probe -- MATH.BSD.STAGEA.01
(Millennium-adjacency round, lane BSD): the COMPLETE certified
Birch--Swinnerton-Dyer package for the compiler's canonical CM
elliptic quotient E: y^3 = u^2 - 1 (v610/L1), i.e. the Weierstrass
curve

    E: Y^2 = X^3 + 1        (conductor 36, CM by Q(omega), j = 0).

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved.  This is "Stufe A" of the proposed
BSD contract: verify that the TFPT compiler's arithmetic object
carries the full BSD data, on a curve where BSD is a CLASSICAL
THEOREM (CM + analytic rank 0: Coates--Wiles; finiteness of Sha:
Rubin).  NO new BSD progress is claimed in either direction --
the value is the machine-checked bridge compiler -> weight-2
modular form -> L-value -> descent -> full leading-coefficient
formula, with every computable step done EXACTLY or to certified
precision here.

THE SIX LEGS:

  (A) COMPILER BRIDGE [E]: the v610 quotient E: y^3 = u^2 - 1 is
      literally Y^2 = X^3 + 1 (rename u->Y, y->X); the v610-style
      point counts over F_p agree with the Weierstrass counts for
      the full v610 prime list, and a_p = 0 exactly for p = 2 mod 3
      (supersingular, CM by Q(omega)) with 4p = a_p^2 + 3b^2 at the
      split primes.

  (B) WEIGHT-2 MODULAR FORM [E]: the unique newform of level 36
      and weight 2 is the eta product f = eta(6 tau)^4; its exact
      integer q-expansion reproduces a_p from the point counts for
      EVERY good prime p < 300, satisfies Hecke multiplicativity
      a_{mn} = a_m a_n and a_{p^2} = a_p^2 - p on the tested range,
      and is supported on n = 1 mod 6.  This is the "reconstruct
      the weight-2 form from the compiler's point counts" step --
      the weight-4 Hecke machine of the E8 glue (v535-v537) is NOT
      used or needed here.

  (C) TORSION EXACT [E]: Lutz--Nagell enumeration (integral points
      with y = 0 or y^2 | 432) + exact group law over Q gives
      E(Q)_tors = Z/6Z = <(2,3)>, with the full subgroup listed.

  (D) RANK 0 BY EXACT 2-ISOGENY DESCENT [E]: on the shifted model
      E1: y^2 = x(x^2 - 3x + 3) (the 2-torsion point (-1,0) moved
      to the origin; exact change of variables gated) and its
      2-isogenous dual E1': y^2 = x(x^2 + 6x - 3), the Selmer
      images are computed with CERTIFICATES: real-positivity
      insolubility for the negative classes on E1, an exhaustive
      3-adic residue certificate (no primitive solutions mod 3^k)
      for the nontrivial classes on E1', and explicit rational
      points on the soluble torsors.  |Im alpha| = |Im alpha'| = 2,
      hence 2^rank = 2*2/4 = 1: rank E(Q) = 0.  (Rank formula:
      standard 2-isogeny descent, Silverman X.4.9, typed [C].)

  (E) L-VALUE AND ANALYTIC RANK [E]: L(E,1) computed from the
      exact eta coefficients via the rapidly convergent series
      L(E,1) = 2 sum a_n/n exp(-2 pi n / sqrt(36)) at 60 digits
      with an explicit tail bound; L(E,1) = 0.7010923... > 0, so
      ord_{s=1} L = 0 = rank E(Q): the BSD RANK EQUATION holds for
      this curve (as the classical theorems demand).

  (F) FULL BSD LEADING-COEFFICIENT FORMULA [E + C]: the real
      period Omega = int_{E(R)} dx/2y = B(1/3,1/6)/2 -- EXACTLY
      the period the compiler already named in v611 (Omega_E =
      B(1/3,1/6)/2, the Beta-value resource of the mu3-cover).
      Numerically certified: L(E,1)/Omega = 1/6 to 40 digits.
      With rank 0 (Reg = 1), |T| = 6 the BSD formula demands
      |Sha| * prod c_p = L * |T|^2 / Omega = 6; Cassels
      (|Sha| is a perfect square if finite, and it IS finite here
      by Rubin [C]) forces the unique split prod c_p = 6, |Sha|=1,
      consistent with Tate's algorithm (c_2, c_3) = (3, 2) [C]
      (LMFDB 36.a4).  Closed form: L(E,1) = B(1/3,1/6)/12.

All checks deterministic (integer point counts; exact eta
expansion; exact fractions in the group law and descent; mpmath
at fixed dps for the analytic leg).  Verdict enums (frozen):
BSD_STAGE_A_VERIFIED (all), BSD_STAGE_A_FAILS, MIXED.

FIREWALL: no gate moves; the theorem content (Coates--Wiles,
Rubin, Cassels, the descent rank formula, Tamagawa numbers at the
additive primes) is typed [C] -- cited, not re-proved; the [E]
content is that every computable ingredient of the BSD formula
for the compiler's canonical CM quotient checks out exactly.
This does NOT constitute progress on BSD for general curves; the
missing general mechanism (a functor E -> H_E with
dim ker H_E = rank E(Q)) remains fully open and is NOT claimed.

PROVENANCE: v610 (QGEO.LANDSCAPE.01, curve + point counts),
v611 (periods: Omega_E = B(1/3,1/6)/2).  Python-only.
"""

from fractions import Fraction

import mpmath as mp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ================================================================ A
print("=" * 72)
print("A: compiler bridge -- v610 quotient = Y^2 = X^3 + 1, CM point counts")
print("=" * 72)


def count_E_v610(p):
    """v610 convention: affine points of y^3 = u^2 - 1 over F_p, +1."""
    cnt = 0
    for uv in range(p):
        rhs = (uv * uv - 1) % p
        for yv in range(p):
            if (yv * yv * yv - rhs) % p == 0:
                cnt += 1
    return cnt + 1


def count_weierstrass(p):
    """affine points of Y^2 = X^3 + 1 over F_p, +1 (point at infinity)."""
    cnt = 0
    for xv in range(p):
        rhs = (xv * xv * xv + 1) % p
        for yv in range(p):
            if (yv * yv - rhs) % p == 0:
                cnt += 1
    return cnt + 1


V610_PRIMES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 61, 73]

check("A1 the v610 curve y^3 = u^2 - 1 IS the Weierstrass curve Y^2 = X^3 + 1 "
      "(same F_p counts for all 14 v610 primes)",
      all(count_E_v610(p) == count_weierstrass(p) for p in V610_PRIMES))


def sieve_primes(n):
    s = list(range(n + 1))
    s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = 0
    return [x for x in s if x > 1]


def a_p_count(p):
    """a_p = p + 1 - #E(F_p) via the quadratic character (good p only)."""
    if p in (2, 3):
        raise ValueError("bad prime")
    ssum = 0
    for x in range(p):
        r = (x * x * x + 1) % p
        if r == 0:
            continue
        ssum += 1 if pow(r, (p - 1) // 2, p) == 1 else -1
    return -ssum


GOOD_PRIMES = [p for p in sieve_primes(300) if p not in (2, 3)]
AP = {p: a_p_count(p) for p in GOOD_PRIMES}

check("A2 CM by Q(omega): a_p = 0 EXACTLY iff p = 2 mod 3, for all %d good "
      "primes p < 300" % len(GOOD_PRIMES),
      all((AP[p] == 0) == (p % 3 == 2) for p in GOOD_PRIMES))


def is_norm_form(p, ap):
    """4p = ap^2 + 3 b^2 with integer b (CM norm form of Q(sqrt(-3)))."""
    rest = 4 * p - ap * ap
    if rest < 0 or rest % 3 != 0:
        return False
    m = rest // 3
    r = int(m ** 0.5)
    return any((r + d) ** 2 == m for d in (-1, 0, 1, 2))


check("A3 split primes carry the CM norm form 4p = a_p^2 + 3 b^2 (all "
      "p = 1 mod 3, p < 300)",
      all(is_norm_form(p, AP[p]) for p in GOOD_PRIMES if p % 3 == 1))

# ================================================================ B
print("=" * 72)
print("B: the weight-2 newform eta(6 tau)^4 from the compiler's point counts")
print("=" * 72)

NMAX = 4000
# f = q * prod_{n>=1} (1 - q^{6n})^4  (exact integer arithmetic)
coeff = [0] * (NMAX + 1)
coeff[0] = 1
for n6 in range(6, NMAX + 1, 6):
    for _ in range(4):
        # multiply by (1 - x^{n6})
        for k in range(NMAX, n6 - 1, -1):
            coeff[k] -= coeff[k - n6]
A = [0] * (NMAX + 1)
for k in range(NMAX):
    A[k + 1] = coeff[k]          # shift by q

check("B1 eta(6 tau)^4 reproduces a_p from the point counts for EVERY good "
      "prime p < 300 (%d primes)" % len(GOOD_PRIMES),
      all(A[p] == AP[p] for p in GOOD_PRIMES))

check("B2 level-36 support: a_n = 0 unless n = 1 mod 6 (n <= %d)" % NMAX,
      all(A[n] == 0 for n in range(1, NMAX + 1) if n % 6 != 1))

mult_ok = True
for m in range(2, 64):
    for n in range(2, 64):
        if m * n <= NMAX:
            from math import gcd
            if gcd(m, n) == 1 and A[m * n] != A[m] * A[n]:
                mult_ok = False
check("B3 Hecke multiplicativity a_{mn} = a_m a_n (coprime m,n < 64)", mult_ok)

check("B4 weight-2 Hecke recursion a_{p^2} = a_p^2 - p at p = 7, 13, 19, 31, "
      "37, 43, 61",
      all(A[p * p] == A[p] ** 2 - p for p in (7, 13, 19, 31, 37, 43, 61)))

check("B5 [C] f = eta(6 tau)^4 is the unique newform of level 36, weight 2 "
      "(classical; dim S_2^new(Gamma_0(36)) = 1) -- the compiler's counts "
      "reconstruct it, no weight transport from the weight-4 E8 machine "
      "(v535-v537) is needed on this lane", True)

# ================================================================ C
print("=" * 72)
print("C: torsion exactly (Lutz--Nagell + exact group law)")
print("=" * 72)

# group law on Y^2 = X^3 + 1 over Q, points as (Fraction, Fraction) or None=O
def ec_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == -y2:
        return None
    if P == Q:
        lam = (3 * x1 * x1) / (2 * y1)
    else:
        lam = (y2 - y1) / (x2 - x1)
    x3 = lam * lam - x1 - x2
    y3 = lam * (x1 - x3) - y1
    return (x3, y3)


def ec_order(P, cap=16):
    R, n = P, 1
    while R is not None and n <= cap:
        R = ec_add(R, P)
        n += 1
    return n if R is None else None


# Lutz--Nagell: integral (x,y), y = 0 or y^2 | Delta = -432
DELTA_ABS = 432
cands = set()
for y in range(0, DELTA_ABS + 1):
    if y == 0 or (y * y != 0 and DELTA_ABS % (y * y) == 0):
        c = y * y - 1
        x = round(abs(c) ** (1.0 / 3)) * (1 if c >= 0 else -1)
        for xt in (x - 1, x, x + 1):
            if xt ** 3 == c:
                cands.add((xt, y))
                if y:
                    cands.add((xt, -y))
check("C1 Lutz--Nagell candidate set is exactly {(-1,0), (0,+-1), (2,+-3)}",
      cands == {(-1, 0), (0, 1), (0, -1), (2, 3), (2, -3)}, str(sorted(cands)))

P6 = (Fraction(2), Fraction(3))
orders = {pt: ec_order((Fraction(pt[0]), Fraction(pt[1]))) for pt in cands}
check("C2 all candidates are torsion; (2,3) has exact order 6, (0,+-1) "
      "order 3, (-1,0) order 2",
      orders[(2, 3)] == 6 and orders[(2, -3)] == 6 and orders[(0, 1)] == 3
      and orders[(0, -1)] == 3 and orders[(-1, 0)] == 2, str(orders))

sub = []
R = None
for _ in range(6):
    R = ec_add(R, P6)
    sub.append(R)
check("C3 <(2,3)> = {O, (2,3), (0,1), (-1,0), (0,-1), (2,-3)}: E(Q)_tors = Z/6",
      set(pt for pt in sub if pt is not None)
      == {(Fraction(2), Fraction(3)), (Fraction(0), Fraction(1)),
          (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1)),
          (Fraction(2), Fraction(-3))} and sub[-1] is None)

# ================================================================ D
print("=" * 72)
print("D: rank 0 by exact 2-isogeny descent (with insolubility certificates)")
print("=" * 72)

import sympy as sp

xs = sp.symbols("x")
lhs = sp.expand((xs - 1) ** 3 + 1)
check("D1 exact model shift: Y^2 = X^3 + 1 with X = x - 1 becomes "
      "y^2 = x(x^2 - 3x + 3)  (a = -3, b = 3)",
      sp.expand(lhs - xs * (xs ** 2 - 3 * xs + 3)) == 0)

a1, b1 = -3, 3                    # E1 : y^2 = x(x^2 - 3x + 3)
a2, b2 = -2 * a1, a1 * a1 - 4 * b1  # dual E1': y^2 = x(x^2 + 6x - 3)
check("D2 2-isogenous dual is y^2 = x(x^2 + 6x - 3)  (a' = 6, b' = -3)",
      (a2, b2) == (6, -3))


def torsor_rhs(d, a, b, u, v):
    """N_d : d w^2 = d^2 u^4 + a d u^2 v^2 + b v^4  ->  w^2 = rhs/d."""
    return d * u ** 4 + a * u ** 2 * v ** 2 + (b // d) * v ** 4


def pos_def_certificate(d, a, b):
    """certify d*w^2 = quartic has no REAL nontrivial solution:
    quartic/d = q(u^2, v^2) with q(s,t) = d s^2 + a s t + (b/d) t^2 must be
    positive definite while d < 0 forces w^2 <= 0 -- i.e. d<0, leading d^2>0,
    q'(s,t) = s^2 + (a/d) s t + (b/d^2)... simplest exact test: the RHS
    quadratic form in (s,t) = (u^2, v^2), rhs = d^2 s^2 + a d s t + b t^2,
    is positive definite (disc < 0, lead > 0) while d w^2 <= 0 for d < 0."""
    disc = (a * d) ** 2 - 4 * d * d * b
    return d < 0 and disc < 0 and d * d > 0


def insoluble_mod_3k(d, a, b, k):
    """certify: d w^2 = d^2 u^4 + a d u^2 v^2 + b v^4 has NO solution with
    (u,v) primitive at 3, modulo 3^k (=> no Q_3-point).  w^2 = rhs where
    rhs = (d^2 u^4 + a d u^2 v^2 + b v^4)/d must be a square residue;
    residues where rhs is 0 mod 3^k count as 'possible' (conservative)."""
    m = 3 ** k
    squares = set((w * w) % m for w in range(m))
    for u in range(m):
        for v in range(m):
            if u % 3 == 0 and v % 3 == 0:
                continue
            num = (d * d * u ** 4 + a * d * u ** 2 * v ** 2 + b * v ** 4)
            if num % d != 0:
                continue
            rhs = (num // d) % m
            if rhs % m == 0 or rhs in squares:
                return False        # possible solution at this depth
    return True


# --- Im(alpha) on E1: candidates squarefree d | b = 3: {1, -1, 3, -3}
sol_3 = torsor_rhs(3, a1, b1, 0, 1) == 1  # w^2 = 3u^4 - 3u^2v^2 + v^4: (0,1,1)
check("D3 E1 torsor d=3 HAS the rational point (u,v,w) = (0,1,1) "
      "[= class of (0,0), alpha((0,0)) = b = 3]", sol_3)
check("D4 E1 torsors d=-1 and d=-3 are insoluble over R (positive-definite "
      "certificate: disc(a d)^2 - 4 d^2 b < 0, d < 0)",
      pos_def_certificate(-1, a1, b1) and pos_def_certificate(-3, a1, b1))
im_alpha = 2

# --- Im(alpha') on E1': candidates squarefree d | b' = -3: {1, -1, 3, -3}
sol_m3 = torsor_rhs(-3, a2, b2, 0, 1) == 1  # w^2 = -3u^4+6u^2v^2+v^4: (0,1,1)
check("D5 E1' torsor d=-3 HAS the rational point (u,v,w) = (0,1,1) "
      "[= class of (0,0), alpha'((0,0)) = b' = -3]", sol_m3)
check("D6 E1' torsor d=3 (w^2 = 3u^4 + 6u^2v^2 - v^4) is 3-adically "
      "insoluble: exhaustive primitive-residue certificate mod 3^4",
      insoluble_mod_3k(3, a2, b2, 4))
check("D7 E1' torsor d=-1 (w^2 = -u^4 + 6u^2v^2 + 3v^4) is 3-adically "
      "insoluble: exhaustive primitive-residue certificate mod 3^4",
      insoluble_mod_3k(-1, a2, b2, 4))
im_alpha_p = 2

rank_pow = (im_alpha * im_alpha_p) // 4
check("D8 [C] descent rank formula (Silverman X.4.9): 2^rank = "
      "|Im alpha| * |Im alpha'| / 4 = %d  =>  rank E(Q) = 0" % rank_pow,
      rank_pow == 1)
check("D9 hence E(Q) = E(Q)_tors = Z/6 -- Mordell--Weil group EXACT", True)

# ================================================================ E
print("=" * 72)
print("E: L(E,1) and the analytic rank")
print("=" * 72)

mp.mp.dps = 60
Lval = 2 * mp.fsum(mp.mpf(A[n]) / n * mp.exp(-mp.pi * n / 3)
                   for n in range(1, NMAX + 1) if A[n])
# crude tail bound |a_n| <= n:  2 * sum_{n>NMAX} e^{-pi n/3}
tail = 2 * mp.exp(-mp.pi * (NMAX + 1) / 3) / (1 - mp.exp(-mp.pi / 3))
print("    L(E,1) = %s   (tail bound %.3e)" % (mp.nstr(Lval, 30), float(tail)))
check("E1 L(E,1) = 0.70109... with truncation tail < 1e-1000 (functional "
      "equation sign w = +1; series 2*sum a_n/n e^{-2 pi n/sqrt(36)})",
      abs(Lval - mp.mpf("0.701091")) < 1e-5 and tail < mp.mpf("1e-1000"))
check("E2 L(E,1) != 0  =>  ord_{s=1} L(E,s) = 0 = rank E(Q):  the BSD RANK "
      "EQUATION holds for the compiler's CM quotient "
      "[C: as Coates--Wiles demands for CM curves with L(1) != 0]",
      Lval > mp.mpf("0.5"))

# ================================================================ F
print("=" * 72)
print("F: real period, v611 bridge, and the full BSD formula")
print("=" * 72)

# x = -1 + s^2 removes the endpoint singularity exactly:
# x^3 + 1 = s^2 (s^4 - 3 s^2 + 3),  dx = 2 s ds
Omega = mp.quad(lambda s: 2 / mp.sqrt(s ** 4 - 3 * s ** 2 + 3),
                [0, 2, mp.inf])
Beta = mp.gamma(mp.mpf(1) / 3) * mp.gamma(mp.mpf(1) / 6) / mp.gamma(mp.mpf(1) / 2)
print("    Omega  = %s" % mp.nstr(Omega, 30))
print("    B(1/3,1/6)/2 = %s" % mp.nstr(Beta / 2, 30))
check("F1 real period Omega = int_{E(R)} dx/2y = B(1/3,1/6)/2 to 40 digits "
      "-- EXACTLY the v611 compiler period Omega_E (the Beta-value resource "
      "of the mu3-cover IS the BSD period of its CM quotient)",
      abs(Omega - Beta / 2) < mp.mpf("1e-40"))

ratio = Lval / Omega
check("F2 L(E,1)/Omega = 1/6 to 30 digits (BSD ratio is EXACTLY rational)",
      abs(ratio - mp.mpf(1) / 6) < mp.mpf("1e-30"),
      "L/Omega = " + mp.nstr(ratio, 25))

# BSD: L(E,1) = Omega * Reg * prod(c_p) * |Sha| / |T|^2 ; rank 0 => Reg = 1
bsd_rhs_over_omega = Fraction(1, 6)     # certified numerically in F2
T_ORDER = 6
sha_times_c = bsd_rhs_over_omega * T_ORDER ** 2
check("F3 BSD demands |Sha| * prod c_p = (L/Omega) * |T|^2 = 6 exactly",
      sha_times_c == 6)

# Cassels: |Sha| (finite here by Rubin [C]) is a perfect square; the only
# split of 6 = prod(c) * square is prod(c) = 6, |Sha| = 1.
def is_square(n):
    r = int(n ** 0.5)
    return r * r == n

splits = [c for c in (1, 2, 3, 6) if 6 % c == 0 and is_square(6 // c)]
check("F4 Cassels-square filter forces the UNIQUE split: prod c_p = 6, "
      "|Sha| = 1 (candidates prod(c) with 6/prod a square: %s)" % splits,
      splits == [6])
check("F5 [C] Tate's algorithm at the additive primes gives (c_2, c_3) = "
      "(3, 2), product 6 (LMFDB 36.a4) -- consistent with F4; and Sha "
      "finiteness is Rubin's theorem for CM curves", True)
check("F6 closed form: L(E,1) = B(1/3,1/6)/12 to 40 digits -- the BSD "
      "leading coefficient of the compiler's CM quotient is a pure "
      "compiler period",
      abs(Lval - Beta / 12) < mp.mpf("1e-40"))

# ================================================================ G
print("=" * 72)
print("G: honesty scope")
print("=" * 72)
check("G1 [C] scope: BSD for THIS curve is a classical theorem instance "
      "(CM, analytic rank 0: Coates--Wiles + Rubin + Cassels); this probe "
      "verifies the compiler carries the full package (Stufe A) and claims "
      "NO progress on general BSD -- the general rank functor "
      "E -> H_E with dim ker H_E = rank E(Q) remains fully open", True)

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: BSD_STAGE_A_VERIFIED -- the compiler's canonical CM")
    print("quotient carries the complete certified BSD package: weight-2")
    print("form from point counts, Z/6 torsion, rank 0 by exact descent,")
    print("L(E,1) = B(1/3,1/6)/12 = Omega_E/6, |Sha| = 1, rank equation")
    print("verified.  Stufe A of the BSD contract is CLOSED; Stufe B (the")
    print("general rank operator) remains open and unclaimed.")
else:
    print("SOME CHECKS FAILED")
    print("VERDICT: MIXED" if n_pass else "VERDICT: BSD_STAGE_A_FAILS")


def run():
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
