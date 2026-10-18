#!/usr/bin/env python3
"""dilation_os_continuation_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (DYN.UNITARY.DILATION.01 [O], the (b)->(c) step after v984
executed the discrete collision leg): does the seam single-step kernel B
admit the OS continuation chain

    B = e^{-H}  (H self-adjoint, >= 0)   ->   U(t) = e^{-itH} unitary,

exactly and with must-fail teeth?  This is the KERNEL-LEVEL D4 leg: the
transfer operator is positive, its logarithm is the OS Hamiltonian, and
the analytic continuation to real time is a genuine one-parameter
unitary group whose Wick rotation returns B^n exactly.

EXACT RESULTS (sympy, no numerics in the claims):

  1. SPECTRAL POSITIVITY: B = P1 + (2/3) P2 + (1/3) P3 with exact
     orthogonal projectors (uniform / sign / trace-free), so B > 0 and
     H := -log B = log(3/2) P2 + log(3) P3  is PSD self-adjoint with
     ground state = the uniform vector and OS gap log(3/2).
  2. SEMIGROUP INTERPOLATION: T(t) = e^{-tH} = P1 + (2/3)^t P2 +
     (1/3)^t P3 is symmetric, positive, STOCHASTIC for all t >= 0
     (row sums 1; entrywise positivity checked on a dense t-grid and at
     the half step exactly) -- the discrete chain embeds in a continuous
     OS semigroup.
  3. UNITARY CONTINUATION: U(t) = e^{-itH} = P1 + (2/3)^{it} P2 +
     (1/3)^{it} P3 satisfies U(t)U(s) = U(t+s), U(t)* = U(-t) (symbolic
     in t, s) and the WICK ANCHOR U(-i n) = B^n exactly (n = 1..6; in
     particular the six-step macro-gate T = B^6 = e^{-6H}).
  4. KMS/DETAILED BALANCE: B is symmetric w.r.t. the uniform stationary
     measure (reversibility) -- the OS inner product is well defined; the
     two-point functions S(n) = <f, B^{|n|} g> are reflection-positive
     because B >= 0.
  5. MUST-FAIL (teeth): the v971 negative-control kernel with second
     eigenvalue -1/10 (doubly stochastic, det < 0) admits NO self-
     adjoint OS Hamiltonian: -log B is non-real (the half-step B^{1/2}
     leaves the real stochastic cone) -- positivity of the transfer
     operator is exactly what the OS step consumes.
  6. DISTINCTION TYPED: this H generates the REDUCED dynamics on the
     classical L^2(pi) space -- it is NOT a microstep unitary generator
     on C^3 (v977: no fixed microstep exists) and NOT yet the
     quasi-local dilated Hamiltonian demanded by D1/D2 at field level.

HONEST BOUNDARY (firewall): kernel-level (3 states) only; the field-
level OS continuation (uniform in system size, quasi-local generator,
Lieb-Robinson) stays [O]; no contract closes; no marker moves.

VERDICT ENUM: OS_CONTINUATION_KERNEL_EXACT (field level open).
"""
import sympy as sp

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


B = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18

# 1. exact spectral decomposition
u1 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
u2 = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
u3 = sp.Matrix([1, 1, -2]) / sp.sqrt(6)
P1, P2, P3 = (u1 * u1.T, u2 * u2.T, u3 * u3.T)
rep("spectral decomposition exact: B = P1 + (2/3)P2 + (1/3)P3, "
    "orthogonal projectors summing to I",
    sp.simplify(B - (P1 + sp.Rational(2, 3) * P2 + sp.Rational(1, 3) * P3))
    == sp.zeros(3)
    and sp.simplify(P1 + P2 + P3 - sp.eye(3)) == sp.zeros(3)
    and all(sp.simplify(P * Q) == sp.zeros(3)
            for P, Q in ((P1, P2), (P1, P3), (P2, P3))))

H = sp.log(sp.Rational(3, 2)) * P2 + sp.log(3) * P3
eigH = sorted(sp.simplify(x) for x in H.eigenvals())
rep("OS HAMILTONIAN exact: H = -log B = log(3/2) P2 + log 3 P3, "
    "self-adjoint, spectrum {0, log(3/2), log 3} >= 0, ground state "
    "uniform, OS gap = log(3/2)",
    sp.simplify(H - H.T) == sp.zeros(3)
    and sp.simplify(H * u1) == sp.zeros(3, 1)
    and eigH == [0, sp.log(sp.Rational(3, 2)), sp.log(3)])

# verify e^{-H} = B via the spectral form (avoid matrix exp pitfalls)
expmH = P1 + sp.Rational(2, 3) * P2 + sp.Rational(1, 3) * P3
rep("Wick anchor at t=1: e^{-H} (spectral form) = B exactly",
    sp.simplify(expmH - B) == sp.zeros(3))

# 2. semigroup interpolation
t, s = sp.symbols("t s", real=True)
Tt = P1 + sp.exp(-t * sp.log(sp.Rational(3, 2))) * P2 \
     + sp.exp(-t * sp.log(3)) * P3
row_sums = sp.simplify(Tt * sp.Matrix([1, 1, 1]))
prod_diff = (Tt * Tt.subs(t, s) - Tt.subs(t, t + s)).applyfunc(
    lambda x: sp.simplify(sp.powsimp(sp.expand(x), force=True)))
rep("T(t) stochastic-symmetric family: T(t) rows sum to 1 symbolically; "
    "T(t)T(s) = T(t+s) symbolically",
    sp.simplify(row_sums - sp.Matrix([1, 1, 1])) == sp.zeros(3, 1)
    and prod_diff == sp.zeros(3))
Thalf = Tt.subs(t, sp.Rational(1, 2))
rep("half step exact and entrywise positive: B^{1/2} = T(1/2) real with "
    "min entry > 0 (the chain interpolates INSIDE the stochastic cone)",
    all(sp.simplify(sp.im(x)) == 0 for x in Thalf)
    and all(sp.N(x) > 0 for x in Thalf))
grid_ok = all(all(sp.N(Tt.subs(t, tv)[i, j]) > 0 for i in range(3)
                  for j in range(3))
              for tv in [sp.Rational(k, 10) for k in range(1, 41)])
rep("entrywise positivity on the t-grid 0.1..4.0 (dense witness)",
    grid_ok)

# 3. unitary continuation
Ut = P1 + sp.Rational(2, 3) ** (sp.I * t) * P2 \
     + sp.Rational(1, 3) ** (sp.I * t) * P3
rep("U(t) = e^{-itH}: group law U(t)U(s) = U(t+s) and U(t)^dag = U(-t) "
    "symbolically in t, s",
    sp.simplify(Ut * Ut.subs(t, s) - Ut.subs(t, t + s)) == sp.zeros(3)
    and sp.simplify(Ut.H - Ut.subs(t, -t)) == sp.zeros(3))
wick = all(sp.simplify(Ut.subs(t, -sp.I * n) - B ** n) == sp.zeros(3)
           for n in range(1, 7))
rep("WICK ROTATION exact: U(-i n) = B^n for n = 1..6 (the six-step "
    "macro-gate T = B^6 = e^{-6H} included)", wick)

# 4. reversibility / OS positivity ingredients
rep("KMS/detailed balance: B symmetric w.r.t. the uniform measure "
    "(reversible chain) and B >= 0 => the OS two-point functions are "
    "reflection-positive",
    sp.simplify(B - B.T) == sp.zeros(3))

# 5. must-fail: the v971 negative control (eigenvalue -1/10)
Bbad = P1 - sp.Rational(1, 10) * P2 + sp.Rational(1, 3) * P3
rep("must-fail input check: B_bad doubly stochastic, symmetric, "
    "det = -1/30 < 0",
    sp.simplify(Bbad * sp.Matrix([1, 1, 1]) - sp.Matrix([1, 1, 1]))
    == sp.zeros(3, 1) and sp.simplify(Bbad.det() + sp.Rational(1, 30)) == 0)
half_bad = P1 + sp.sqrt(sp.Rational(-1, 10)) * P2 \
    + sp.sqrt(sp.Rational(1, 3)) * P3
rep("MUST-FAIL FIRES: B_bad^{1/2} is non-real (leaves the real "
    "stochastic cone) -- no self-adjoint OS Hamiltonian exists; "
    "positivity of the transfer operator is exactly what OS consumes",
    any(sp.simplify(sp.im(x)) != 0 for x in half_bad))

# 6. distinction typed (documented, trivially true statements)
rep("DISTINCTION TYPED: H acts on the classical L^2(pi) space (reduced "
    "chain), not on C^3 as a microstep generator (v977: no fixed "
    "microstep; v984: the microdynamics is the collision band); the "
    "field-level D1/D2 legs stay open", True)

print()
print("VERDICT: OS_CONTINUATION_KERNEL_EXACT (field-level OS/quasi-local "
      "legs stay [O]; no promotion decision here)")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
