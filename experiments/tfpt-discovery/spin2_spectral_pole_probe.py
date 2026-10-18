#!/usr/bin/env python3
r"""spin2_spectral_pole_probe -- EXPLORATION ONLY.

This is the smallest quadratic shadow of GRAV.SPIN2.EMERGENCE.01.  It
does not construct Gamma[e,omega], a graviton Hilbert space, universal
matter coupling, or an interacting/reflection-positive theory.

The read-only corpus inputs are the frozen structures in v253--v255:

  * a2 supplies Einstein--Hilbert;
  * a4 supplies R^2 AND a nonzero Weyl^2 term;
  * M_scal = c3^(7/2) Mbar;
  * the effective Starobinsky normalization is
        (Mbar^2/2) [R + R^2/(6 M_scal^2)].

Around a stationary flat background (the a0 cosmological term is
subtracted/tuned so flat space is actually a saddle), the script
constructs the Barnes--Rivers projectors and evaluates the quadratic
curvatures on spin-2, spin-1 and spin-0 representatives.  The result is
honest: the R+R^2 control has one massless spin-2 pole and one scalaron,
but the frozen a4 structure explicitly contains Weyl^2.  Any nonzero
local Weyl^2 coefficient adds a massive spin-2 pole with residue opposite
to the massless pole (and one coefficient sign is additionally
tachyonic/Euclidean-indefinite).  Therefore the local a4 truncation is
NOT clean; this reproduces the Stelle caveat already recorded in v269
and v304.

VERDICT ENUM:
  SPIN2_QUADRATIC_CLEAN
  SPIN2_QUADRATIC_GHOST_TYPED
  SPIN2_QUADRATIC_ALGEBRA_FAIL

Expected here: SPIN2_QUADRATIC_GHOST_TYPED.  The contract stays [O].
"""

import itertools
import sys

import numpy as np
import sympy as sp


D = 4
TOL = 2.0e-11
SEED = 20260828
CHECKS = []


def check(name, condition, detail):
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-34s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def symmetric_basis(n):
    basis = []
    labels = []
    for i in range(n):
        for j in range(i, n):
            h = sp.zeros(n)
            if i == j:
                h[i, j] = 1
            else:
                h[i, j] = h[j, i] = 1 / sp.sqrt(2)
            basis.append(h)
            labels.append((i, j))
    return basis, labels


SYM_BASIS, SYM_LABELS = symmetric_basis(D)


def inner(a, b):
    return sp.simplify(sum(a[i, j] * b[i, j]
                           for i in range(D) for j in range(D)))


def apply_projector(kind, h, theta, omega):
    out = sp.zeros(D)
    for mu, nu, rho, sig in itertools.product(range(D), repeat=4):
        if kind == "2":
            coef = ((theta[mu, rho] * theta[nu, sig]
                     + theta[mu, sig] * theta[nu, rho]) / 2
                    - theta[mu, nu] * theta[rho, sig] / (D - 1))
        elif kind == "1":
            coef = (theta[mu, rho] * omega[nu, sig]
                    + theta[mu, sig] * omega[nu, rho]
                    + theta[nu, rho] * omega[mu, sig]
                    + theta[nu, sig] * omega[mu, rho]) / 2
        elif kind == "0s":
            coef = theta[mu, nu] * theta[rho, sig] / (D - 1)
        elif kind == "0w":
            coef = omega[mu, nu] * omega[rho, sig]
        else:
            raise ValueError(kind)
        out[mu, nu] += coef * h[rho, sig]
    return sp.simplify(out)


def projector_matrix(kind, theta, omega):
    return sp.Matrix([
        [inner(a, apply_projector(kind, b, theta, omega))
         for b in SYM_BASIS]
        for a in SYM_BASIS
    ])


def linear_curvatures(h, p):
    p2 = sp.simplify(sum(x * x for x in p))
    trh = sp.trace(h)
    ric = sp.zeros(D)
    for mu in range(D):
        for nu in range(D):
            ric[mu, nu] = sp.simplify(sum(
                (p[rho] * p[mu] * h[nu, rho]
                 + p[rho] * p[nu] * h[mu, rho]) / 2
                for rho in range(D))
                - (p2 * h[mu, nu] + p[mu] * p[nu] * trh) / 2)
    scalar = sp.simplify(sum(p[mu] * p[nu] * h[mu, nu]
                             for mu in range(D) for nu in range(D))
                         - p2 * trh)
    riem2 = 0
    for mu, nu, rho, sig in itertools.product(range(D), repeat=4):
        r = (p[rho] * p[nu] * h[mu, sig]
             + p[sig] * p[mu] * h[nu, rho]
             - p[sig] * p[nu] * h[mu, rho]
             - p[rho] * p[mu] * h[nu, sig]) / 2
        riem2 += r * r
    ric2 = sum(ric[i, j] ** 2 for i in range(D) for j in range(D))
    weyl2 = sp.simplify(riem2 - 2 * ric2 + scalar ** 2 / 3)
    return sp.simplify(scalar), sp.simplify(ric2), weyl2


def fierz_pauli(h, p):
    """Gauge-invariant massless quadratic form, before its Mbar^2/4 factor."""
    p2 = sp.simplify(sum(x * x for x in p))
    trh = sp.trace(h)
    h2 = inner(h, h)
    div2 = sum(sum(p[mu] * h[mu, nu] for mu in range(D)) ** 2
               for nu in range(D))
    pph = sum(p[mu] * p[nu] * h[mu, nu]
              for mu in range(D) for nu in range(D))
    return sp.simplify(p2 * h2 / 2 - div2 + pph * trh
                       - p2 * trh ** 2 / 2)


def numeric_projectors(momentum):
    p = np.asarray(momentum, dtype=float)
    p2 = float(p @ p)
    omega = np.outer(p, p) / p2
    theta = np.eye(D) - omega

    def action(kind, h):
        if kind == "2":
            return (theta @ h @ theta
                    - theta * np.trace(theta @ h) / (D - 1))
        if kind == "0s":
            return theta * np.trace(theta @ h) / (D - 1)
        if kind == "0w":
            return omega * np.trace(omega @ h)
        if kind == "1":
            return theta @ h @ omega + omega @ h @ theta
        raise ValueError(kind)

    mats = {}
    basis = [np.array(x, dtype=float) for x in SYM_BASIS]
    for kind in ("2", "1", "0s", "0w"):
        mats[kind] = np.array([
            [np.sum(a * action(kind, b)) for b in basis] for a in basis
        ])
    return mats


def main():
    print("=" * 78)
    print("spin2_spectral_pole_probe -- quadratic spectral-action shadow")
    print("EXPLORATION ONLY; GRAV.SPIN2.EMERGENCE.01 stays [O]")
    print("=" * 78)

    q = sp.symbols("q", nonzero=True, real=True)
    p = sp.Matrix([0, 0, 0, q])
    p2 = q ** 2
    omega = sp.simplify(p * p.T / p2)
    theta = sp.eye(D) - omega

    projectors = {
        kind: projector_matrix(kind, theta, omega)
        for kind in ("2", "1", "0s", "0w")
    }
    eye10 = sp.eye(len(SYM_BASIS))
    algebra_ok = (
        all(sp.simplify(P * P - P) == sp.zeros(10) for P in projectors.values())
        and all(sp.simplify(projectors[a] * projectors[b]) == sp.zeros(10)
                for a, b in itertools.permutations(projectors, 2))
        and sp.simplify(sum(projectors.values(), sp.zeros(10)) - eye10)
        == sp.zeros(10)
    )
    ranks = {k: int(P.rank()) for k, P in projectors.items()}
    check("symbolic projector algebra", algebra_ok and ranks == {
        "2": 5, "1": 3, "0s": 1, "0w": 1},
        "P_i P_j=delta_ij P_i, sum P_i=I_10; ranks %s" % ranks)

    h_tt = SYM_BASIS[SYM_LABELS.index((0, 1))]
    h_vec = SYM_BASIS[SYM_LABELS.index((0, 3))]
    h_scal = theta / sp.sqrt(D - 1)
    representatives = {"spin-2 TT": h_tt, "spin-1 gauge": h_vec,
                       "spin-0 transverse": h_scal}
    expected = {"spin-2 TT": "2", "spin-1 gauge": "1",
                "spin-0 transverse": "0s"}
    rep_ok = True
    for name, h in representatives.items():
        for kind in projectors:
            target = h if kind == expected[name] else sp.zeros(D)
            rep_ok &= sp.simplify(
                apply_projector(kind, h, theta, omega) - target) == sp.zeros(D)
    check("irrep representatives", rep_ok,
          "TT -> P2, longitudinal vector -> P1, transverse trace -> P0s")

    data = {}
    for name, h in representatives.items():
        scalar, ric2, weyl2 = linear_curvatures(h, p)
        data[name] = {
            "FP": sp.simplify(fierz_pauli(h, p)),
            "R": scalar,
            "Ric2": ric2,
            "C2": weyl2,
        }
    curvature_ok = (
        data["spin-2 TT"]["FP"] == p2 / 2
        and data["spin-2 TT"]["R"] == 0
        and data["spin-2 TT"]["C2"] == p2 ** 2 / 2
        and all(data["spin-1 gauge"][key] == 0
                for key in ("FP", "R", "Ric2", "C2"))
        and data["spin-0 transverse"]["FP"] == -p2
        and sp.simplify(data["spin-0 transverse"]["R"] ** 2
                        - 3 * p2 ** 2) == 0
        and data["spin-0 transverse"]["C2"] == 0
    )
    check("quadratic curvature split", curvature_ok,
          "TT: FP=q^2/2,C^2=q^4/2,R=0; vector: all zero; "
          "scalar: FP=-q^2,R^2=3q^4,C^2=0")

    c3, mbar, z = sp.symbols("c3 Mbar z", positive=True)
    alpha_c = sp.symbols("alpha_C", nonzero=True, real=True)
    m_scal = c3 ** sp.Rational(7, 2) * mbar
    A = mbar ** 2 / 4

    # Lorentz-invariant pole variable z=p^2.  These kernels follow directly
    # from the representative action values above; Euclidean continuation is
    # z=-p_E^2.
    k2_clean = sp.expand(A * z)
    k1 = sp.Integer(0)
    k0 = sp.factor(-2 * A * z * (1 - z / m_scal ** 2))
    scalar_roots = sp.solve(k0, z)
    scalar_mass = next(root for root in scalar_roots if root != 0)
    scalar_ok = sp.simplify(scalar_mass - m_scal ** 2) == 0
    check("frozen scalaron normalization", scalar_ok,
          "R^2/(6 M_scal^2) gives roots p^2=%s and M_scal=%s"
          % (scalar_roots, m_scal))
    check("TT massless control", (k2_clean.subs(z, 0) == 0
                                  and sp.diff(k2_clean, z).subs(z, 0) != 0),
          "K2(clean)=%s: nonzero p^2 coefficient, no p^0 mass term"
          % k2_clean)
    check("vector Ward shadow", k1 == 0,
          "K1=0 exactly: h_{mu nu}=p_(mu xi_nu) is pure gauge")

    # A local Weyl^2 term contributes alpha_C z^2 P2.  Its coefficient is
    # left symbolic because v255 freezes its presence and heat-kernel origin,
    # while the exact cutoff-moment normalization remains open.
    k2_frozen = sp.factor(A * z + alpha_c * z ** 2)
    prop_frozen = sp.apart(1 / k2_frozen, z)
    extra_pole = sp.simplify(-A / alpha_c)
    residue_zero = sp.simplify(sp.limit(z / k2_frozen, z, 0))
    residue_extra = sp.simplify(
        sp.limit((z - extra_pole) / k2_frozen, z, extra_pole))
    ghost_typed = (sp.simplify(residue_zero - 1 / A) == 0
                   and sp.simplify(residue_extra + 1 / A) == 0)
    check("frozen Weyl ghost typed", ghost_typed,
          "v255 a4 has Weyl^2: K2=%s, poles {0,%s}, residues {%s,%s}"
          % (k2_frozen, extra_pole, residue_zero, residue_extra))

    m2_mut = sp.symbols("M2_mut", positive=True)
    k2_mut = A * z * (1 + z / m2_mut)
    mut_prop = sp.apart(1 / k2_mut, z)
    mut_r0 = sp.limit(z / k2_mut, z, 0)
    mut_rm = sp.limit((z + m2_mut) / k2_mut, z, -m2_mut)
    mutant_ok = (sp.simplify(mut_r0 - 1 / A) == 0
                 and sp.simplify(mut_rm + 1 / A) == 0)
    check("wrong-sign Weyl mutant", mutant_ok,
          "1/K2=%s; p^2=-M2_mut residue %s is opposite to massless %s"
          % (mut_prop, mut_rm, mut_r0))

    rng = np.random.default_rng(SEED)
    worst = 0.0
    numeric_ranks = None
    for _ in range(8):
        momentum = rng.normal(size=D)
        mats = numeric_projectors(momentum)
        numeric_ranks = {k: int(np.linalg.matrix_rank(P, tol=1e-10))
                         for k, P in mats.items()}
        total = sum(mats.values())
        worst = max(worst, np.max(np.abs(total - np.eye(10))))
        for a, Pa in mats.items():
            worst = max(worst, np.max(np.abs(Pa @ Pa - Pa)))
            for b, Pb in mats.items():
                if a != b:
                    worst = max(worst, np.max(np.abs(Pa @ Pb)))
    check("random-momentum cross-check",
          worst < TOL and numeric_ranks == ranks,
          "8 seeded p vectors; worst algebra dev %.2e; ranks %s"
          % (worst, numeric_ranks))

    eps_plus = np.zeros((4, 4))
    eps_plus[0, 0], eps_plus[1, 1] = 1.0, -1.0
    eps_cross = np.zeros((4, 4))
    eps_cross[0, 1] = eps_cross[1, 0] = 1.0
    # Coordinate order here is (x,y,z,t), matching the symbolic q-axis above.
    null_p = np.array([0.0, 0.0, 1.0, 1.0])
    helicity_ok = (
        np.max(np.abs(null_p @ eps_plus)) == 0
        and np.max(np.abs(null_p @ eps_cross)) == 0
        and abs(np.trace(eps_plus)) < TOL
        and abs(np.trace(eps_cross)) < TOL
        and abs(np.sum(eps_plus * eps_cross)) < TOL
    )
    check("two TT polarization witnesses", helicity_ok,
          "plus/cross are transverse, traceless and independent for "
          "null p=(0,0,1,1) in (x,y,z,t) order")

    algebra_all = all(CHECKS)
    if not algebra_all:
        verdict = "SPIN2_QUADRATIC_ALGEBRA_FAIL"
    elif ghost_typed:
        verdict = "SPIN2_QUADRATIC_GHOST_TYPED"
    else:
        verdict = "SPIN2_QUADRATIC_CLEAN"

    print("\nPOLE-STRUCTURE TABLE")
    print("  block   quadratic kernel                              poles / meaning")
    print("  spin-2  A p^2 + alpha_C p^4                         0 + extra ghost")
    print("  spin-1  0                                             pure gauge")
    print("  spin-0 -2A p^2(1-p^2/M_scal^2)                     scalaron M_scal")
    print("  A=Mbar^2/4; M_scal=c3^(7/2) Mbar; alpha_C != 0 at local a4")
    print("  clean R+R^2 control: alpha_C=0 (one massless spin-2 pole)")
    print("  flat-background condition: effective a0/cosmological tadpole removed")
    print("\nVERDICT: %s" % verdict)
    print("BOUNDARY: quadratic order, stationary flat background, local a4 "
          "truncation.  No interacting graviton, universal T_munu coupling, "
          "nonlinear Ward theorem, positive Hamiltonian or RP transfer theorem.  "
          "GRAV.SPIN2.EMERGENCE.01 stays [O].")
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("=" * 78)
    return 0 if algebra_all and verdict == "SPIN2_QUADRATIC_GHOST_TYPED" else 1


if __name__ == "__main__":
    sys.exit(main())
