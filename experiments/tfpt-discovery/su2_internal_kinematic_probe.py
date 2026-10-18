#!/usr/bin/env python3
"""Discovery probe: the internal SU(2), kinematic separation at twistor
level -- kill test (6)'s kinematic branch does not fire.  (WOIT gamma
milestone, the last untouched kill test, first executed slice.)

Kill test (6) of WOIT.OS.TWISTOR.01: "the internal SU(2) remains a
spacetime factor (no genuine internal weak factor separates from the
Euclidean rotation group)".  On C^4 = H^2 (twistor space as a 2-dim
quaternionic module, v519/v565 conventions) the question has an exact
kinematic half, decided here by finite linear algebra over the reals:

  (W1) THE QUATERNION SPLIT [E]: right multiplications by i, j, k close
       the quaternion algebra exactly (as real-linear operators), and
       Woit's Euclidean structure IS the internal j-direction:
       rho_tw = right-j VERBATIM in the v519/v565 conventions
       (M_tw = diag(J2, J2) composed with conj).

  (W2) THE INTERNAL ALGEBRA [E]: right-sp(1) = span{right-i, right-j,
       right-k} is a 3-dimensional real Lie algebra with the exact su(2)
       brackets, and it preserves EVERY fiber of the twistor fibration
       PT -> S^4 = HP^1 (each quaternionic line C-span{v, rho_tw v} is
       mapped to itself -- the group acts TRIVIALLY on spacetime);
       control: the spacetime generators (left multiplications) move a
       generic fiber.

  (W3) THE SEPARATION [E, the kill-test datum]: left and right
       multiplications commute EXACTLY (the internal su(2) commutes with
       the full spacetime quaternion action), and the two algebras
       intersect in {0}: the internal factor SEPARATES from the
       Euclidean rotation group at the kinematic level -- kill test
       (6)'s kinematic branch does NOT fire.

  (W4) THE CLOCK FACTORIZATION [E]: the mu4 clock lift factorizes
       EXACTLY as RHO4 = left-u o right-u with u = e^{i pi/4} -- the
       clock entangles a SPACETIME half-quarter turn with an INTERNAL
       half-quarter phase; must-fail controls: neither factor alone is
       the clock; the ALE deck is PURELY spacetime-side (DECK4 = left-i
       exactly), and RHO4^2 = DECK4 o right-i: the deck and the internal
       quarter phase are the two halves of the clock square.

  (W5) THE BREAKING [E]: the complex-linear part of the internal
       algebra is exactly span{right-i} -- the choice of the complex
       structure (the Euclidean section, v519 family A's role) breaks
       the internal SU(2) to U(1) KINEMATICALLY; the v519 mark torsor
       mu in mu4 is exactly the mu4 subgroup of this internal U(1)
       composed with the OS conjugation (family D: z -> mu conj(z) =
       right-mu o sigma_std).

  (W6) OS COMPATIBILITY [E]: sigma_std (family D) normalizes the
       internal algebra and inverts the internal charge
       (sigma right-i sigma = -right-i = right-i^{-1}-direction), and
       the Theta-clock inversion decomposes: sigma inverts BOTH factors
       of W4 simultaneously.

  (W7) THE READING [C]: kinematic twistor level only -- the DYNAMICAL
       half of kill test (6) (the internal SU(2) acting as a genuine
       gauge symmetry on the reconstructed net / A_hol) stays OPEN and
       the kill test stays formally live there; this round types its
       kinematic branch: the internal factor exists, separates, commutes
       with spacetime, and the Euclidean/complex choice breaks it to
       U(1) with the mark torsor as its mu4 -- consistent with (not
       derived) the electroweak reading.

Verdict enums (frozen): SU2-KINEMATIC-SEPARATED (all pass),
SU2-KINEMATIC-FAILS, MIXED.

Conventions: v519/v565 verbatim (RHO4 = diag(i,1,i,1), M_tw =
diag(J2,J2), DECK4 = diag(i,-i,i,-i), sigma_std = coordinatewise conj).
Real-linear operators are represented exactly as pairs (A, B):
v -> A v + B conj(v).  Python-only (sympy), counted per GATE.WOLFRAM.02.
"""

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


I = sp.I
I4 = sp.eye(4)
Z4 = sp.zeros(4, 4)
J2 = sp.Matrix([[0, -1], [1, 0]])
MTW = sp.diag(J2, J2)
RHO4 = sp.diag(I, 1, I, 1)
DECK4 = sp.diag(I, -I, I, -I)


# real-linear operator: v -> A v + B conj(v)
def op(A, B):
    return (sp.ImmutableMatrix(sp.expand_complex(A)),
            sp.ImmutableMatrix(sp.expand_complex(B)))


def comp(f, g):
    """f o g on v -> ... (apply g first): f(g(v)) with g(v) = A2 v + B2
    conj(v) gives A-part A1 A2 + B1 conj(B2), B-part A1 B2 + B1 conj(A2)."""
    A1, B1 = f
    A2, B2 = g
    return op(A1 * A2 + B1 * B2.conjugate(),
              A1 * B2 + B1 * A2.conjugate())


def opeq(f, g):
    return (sp.simplify(sp.expand_complex(f[0] - g[0])) == sp.zeros(4, 4)
            and sp.simplify(sp.expand_complex(f[1] - g[1])) == sp.zeros(4, 4))


def bracket(f, g):
    fg = comp(f, g)
    gf = comp(g, f)
    return op(fg[0] - gf[0], fg[1] - gf[1])


def scal(c, f):
    """REAL scalar multiple (real Lie algebra)."""
    return op(c * f[0], c * f[1])


def add(f, g):
    return op(f[0] + g[0], f[1] + g[1])


ID = op(I4, Z4)
NEG = op(-I4, Z4)

# right multiplications (internal side); as OPERATORS X_q(v) = v q the
# right multiplications are an ANTI-homomorphism: X_p o X_q = X_{qp}
Ri = op(I * I4, Z4)          # right-i = the complex structure
Rj = op(Z4, MTW)             # right-j
Rk = comp(Rj, Ri)            # X_k = X_j o X_i (v -> (v i) j = v (ij) = v k)

# left multiplications (spacetime side); left-u for complex u:
# diag(u, conj u, u, conj u); left-j = diag(J2, J2) C-linear
def left_u(u):
    return op(sp.diag(u, sp.conjugate(u), u, sp.conjugate(u)), Z4)


Lj = op(MTW, Z4)             # left-j (C-linear)
Li = left_u(I)               # left-i
Lk = comp(Li, Lj)            # left-k

# ================================================================== W1
print("=" * 72)
print("W1: the quaternion split; rho_tw = right-j verbatim")
print("=" * 72)

quat_ok = (opeq(comp(Ri, Ri), NEG) and opeq(comp(Rj, Rj), NEG)
           and opeq(comp(Rk, Rk), NEG)
           and opeq(comp(Ri, Rj), scal(-1, Rk))
           and opeq(comp(Rj, Rk), scal(-1, Ri))
           and opeq(comp(Rk, Ri), scal(-1, Rj))
           and opeq(comp(Rj, Ri), Rk))
check("W1.1 right-{i,j,k} close the OPPOSITE quaternion algebra exactly "
      "(i^2 = j^2 = k^2 = -1; as operators X_p X_q = X_{qp}: "
      "Ri Rj = -Rk cyclic, Rj Ri = +Rk)", quat_ok)

rho_tw = op(Z4, MTW)
check("W1.2 rho_tw = right-j VERBATIM (M_tw o conj = right multiplication "
      "by the quaternion j; the Euclidean structure is an INTERNAL "
      "direction)", opeq(rho_tw, Rj))

quat_left = (opeq(comp(Li, Li), NEG) and opeq(comp(Lj, Lj), NEG)
             and opeq(comp(Li, Lj), Lk) and opeq(comp(Lj, Li), scal(-1, Lk)))
check("W1.3 left-{i,j,k} close the quaternion algebra exactly (the "
      "spacetime side)", quat_left)

# ================================================================== W2
print("=" * 72)
print("W2: the internal algebra preserves every twistor fiber")
print("=" * 72)

# su(2) brackets (opposite orientation): [Ri, Rj] = -2 Rk cyclic
br_ok = (opeq(bracket(Ri, Rj), scal(-2, Rk))
         and opeq(bracket(Rj, Rk), scal(-2, Ri))
         and opeq(bracket(Rk, Ri), scal(-2, Rj)))
check("W2.1 right-sp(1) = span{right-i, right-j, right-k} has the exact "
      "su(2) brackets ([Ri,Rj] = -2Rk cyclic, the opposite orientation): "
      "a 3-dim real Lie algebra", br_ok)


def apply_op(f, v):
    A, B = f
    return A * v + B * v.conjugate()


# generic fiber: L(v) = C-span{v, rho_tw(v)}; internal ops preserve it
v = sp.Matrix(sp.symbols("a1 a2 a3 a4", complex=True))
fib = sp.Matrix.hstack(v, apply_op(Rj, v))


def in_fiber(w, fibm):
    M = sp.Matrix.hstack(fibm, w)
    # rank stays 2 for generic v: all 3x3 minors vanish identically
    for rows in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
        if sp.simplify(sp.expand_complex(
                M.extract(list(rows), [0, 1, 2]).det())) != 0:
            return False
    return True


fiber_ok = all(in_fiber(apply_op(g, v), fib) for g in (Ri, Rj, Rk))
check("W2.2 the internal algebra preserves EVERY quaternionic line "
      "L(v) = C-span{v, rho_tw v} (all 3x3 minors vanish identically in "
      "the generic v): the internal group acts TRIVIALLY on spacetime "
      "S^4 = HP^1", fiber_ok)

moves = not in_fiber(apply_op(Lj, v), fib)
check("W2.3 [control] the spacetime generator left-j MOVES the generic "
      "fiber (a 3x3 minor is generically nonzero): the left action is the "
      "spacetime action", moves)

# ================================================================== W3
print("=" * 72)
print("W3: the separation (kill test 6, kinematic branch)")
print("=" * 72)

comm_ok = all(opeq(bracket(Rg, Lg), op(Z4, Z4))
              for Rg in (Ri, Rj, Rk) for Lg in (Li, Lj, Lk))
check("W3.1 the internal su(2) COMMUTES with the full spacetime "
      "quaternion action exactly (all nine brackets vanish)", comm_ok)

# trivial intersection: x1 Ri + x2 Rj + x3 Rk = y1 Li + y2 Lj + y3 Lk
xs = sp.symbols("x1 x2 x3 y1 y2 y3", real=True)
lhs_A = xs[0] * Ri[0] + xs[1] * Rj[0] + xs[2] * Rk[0]
lhs_B = xs[0] * Ri[1] + xs[1] * Rj[1] + xs[2] * Rk[1]
rhs_A = xs[3] * Li[0] + xs[4] * Lj[0] + xs[5] * Lk[0]
rhs_B = xs[3] * Li[1] + xs[4] * Lj[1] + xs[5] * Lk[1]
eqs = []
for M in (sp.expand_complex(lhs_A - rhs_A), sp.expand_complex(lhs_B - rhs_B)):
    for e in M:
        eqs += [sp.re(e), sp.im(e)]
sol = sp.solve(eqs, xs, dict=True)
inter_ok = (len(sol) == 1
            and all(sp.simplify(sol[0].get(x_, 0)) == 0 for x_ in xs))
check("W3.2 the two algebras intersect in {0} (the only common element of "
      "right-sp(1) and left-sp(1)-span is zero): the internal factor "
      "SEPARATES from the Euclidean rotation group -- kill test (6)'s "
      "KINEMATIC branch does not fire", inter_ok)

# ================================================================== W4
print("=" * 72)
print("W4: the clock factorization")
print("=" * 72)

u8 = sp.exp(I * sp.pi / 4)
clock = op(RHO4, Z4)
fact = comp(left_u(u8), op(u8 * I4, Z4))
check("W4.1 THE CLOCK FACTORIZES: RHO4 = left-u o right-u with "
      "u = e^{i pi/4} EXACTLY -- the mu4 clock entangles a SPACETIME "
      "half-quarter turn with an INTERNAL half-quarter phase",
      opeq(clock, fact))
check("W4.2 [must-fail controls] neither factor alone is the clock",
      not opeq(clock, left_u(u8)) and not opeq(clock, op(u8 * I4, Z4)))
check("W4.3 the ALE deck is PURELY spacetime-side: DECK4 = left-i exactly",
      opeq(op(DECK4, Z4), Li))
check("W4.4 RHO4^2 = DECK4 o right-i exactly: the clock square splits "
      "into the deck (spacetime) times the internal quarter phase",
      opeq(comp(clock, clock), comp(Li, Ri)))

# ================================================================== W5
print("=" * 72)
print("W5: the breaking (internal SU(2) -> U(1) by the complex structure)")
print("=" * 72)

# C-linear part of the internal algebra: B-part must vanish
c1, c2, c3 = sp.symbols("c1 c2 c3", real=True)
Bpart = sp.expand_complex(c1 * Ri[1] + c2 * Rj[1] + c3 * Rk[1])
eqs = []
for e in Bpart:
    eqs += [sp.re(e), sp.im(e)]
solB = sp.solve(eqs, (c2, c3), dict=True)
break_ok = (len(solB) == 1 and sp.simplify(solB[0][c2]) == 0
            and sp.simplify(solB[0][c3]) == 0)
check("W5.1 the COMPLEX-LINEAR part of the internal algebra is exactly "
      "span{right-i}: the choice of complex structure (the Euclidean "
      "section) breaks the internal SU(2) to U(1) kinematically", break_ok)

# the v519 mark torsor: family D maps z -> mu conj(z) = right-mu o sigma
sigma = op(Z4, I4)
torsor_ok = all(
    opeq(comp(op(mu * I4, Z4), sigma), op(Z4, mu * I4))
    for mu in (1, I, -1, -I))
check("W5.2 the v519 mark torsor (family D, z -> mu conj z, mu in mu4) is "
      "exactly {right-mu o sigma_std : mu in mu4}: the mark set IS the mu4 "
      "subgroup of the internal U(1), composed with the OS conjugation",
      torsor_ok)

# ================================================================== W6
print("=" * 72)
print("W6: OS compatibility")
print("=" * 72)

check("W6.1 sigma_std inverts the internal charge and normalizes the "
      "internal algebra as the j-real form: sigma Ri sigma = -Ri, "
      "sigma Rj sigma = +Rj (the OS conjugation FIXES the Euclidean "
      "structure), sigma Rk sigma = -Rk",
      opeq(comp(sigma, comp(Ri, sigma)), scal(-1, Ri))
      and opeq(comp(sigma, comp(Rj, sigma)), Rj)
      and opeq(comp(sigma, comp(Rk, sigma)), scal(-1, Rk)))

lu_inv = left_u(sp.conjugate(u8))
ru_inv = op(sp.conjugate(u8) * I4, Z4)
check("W6.2 the Theta-clock inversion decomposes: sigma inverts BOTH "
      "factors simultaneously (sigma (left-u) sigma = left-u^-1 and "
      "sigma (right-u) sigma = right-u^-1) -- Theta rho Theta = rho^-1 "
      "factor by factor",
      opeq(comp(sigma, comp(left_u(u8), sigma)), lu_inv)
      and opeq(comp(sigma, comp(op(u8 * I4, Z4), sigma)), ru_inv))

# ================================================================== W7
print("=" * 72)
print("W7: the reading")
print("=" * 72)

check("W7.1 [C] kinematic twistor level only: the internal SU(2) exists, "
      "separates from the Euclidean rotation group, commutes with "
      "spacetime, and the Euclidean/complex choice breaks it to U(1) with "
      "the mark torsor as its mu4 -- the DYNAMICAL half of kill test (6) "
      "(gauge action on the reconstructed net / A_hol) stays OPEN and the "
      "kill test stays formally live there; consistent with (not derived) "
      "the electroweak reading", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: SU2-KINEMATIC-SEPARATED -- the internal SU(2) exists and")
    print("separates from the Euclidean rotation group at the kinematic level;")
    print("the clock entangles the two sides exactly (left-u o right-u), the")
    print("deck is spacetime-side, and the complex choice breaks the internal")
    print("factor to U(1) with the mark torsor as its mu4.")
else:
    print("SOME CHECKS FAILED")
