#!/usr/bin/env python3
"""Exact certificate for the finite-range cubic free-scalar Ward complex.

This is a standalone theory-contract checker.  It uses independent SymPy
symbols on Z^3 for the local universal identities, and a separate finite
periodic lattice for homogeneous-mode checks.  There are no floating-point
or random tests.

Scope: free scalar matter on the declared staggered regulator only.  This does
not check gravity constraints, matter-gravity feedback, interactions, Kubo
response, full TOE, or RH.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product

import sympy as sp


Coord = tuple[int, int, int]
ZERO: Coord = (0, 0, 0)
E: tuple[Coord, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(x: Coord, y: Coord) -> Coord:
    return tuple(a + b for a, b in zip(x, y))  # type: ignore[return-value]


def sub(x: Coord, y: Coord) -> Coord:
    return tuple(a - b for a, b in zip(x, y))  # type: ignore[return-value]


@dataclass
class Fields:
    """Lazily named canonical variables, optionally with periodic wrapping."""

    period: int | None = None
    phi_vars: dict[Coord, sp.Symbol] = field(default_factory=dict)
    pi_vars: dict[Coord, sp.Symbol] = field(default_factory=dict)
    reverse: dict[sp.Symbol, tuple[str, Coord]] = field(default_factory=dict)

    def wrap(self, x: Coord) -> Coord:
        if self.period is None:
            return x
        return tuple(a % self.period for a in x)  # type: ignore[return-value]

    @staticmethod
    def label(x: Coord) -> str:
        return "_".join(str(a).replace("-", "m") for a in x)

    def phi(self, x: Coord) -> sp.Symbol:
        x = self.wrap(x)
        if x not in self.phi_vars:
            symbol = sp.Symbol(f"q_{self.label(x)}", real=True)
            self.phi_vars[x] = symbol
            self.reverse[symbol] = ("phi", x)
        return self.phi_vars[x]

    def pi(self, x: Coord) -> sp.Symbol:
        x = self.wrap(x)
        if x not in self.pi_vars:
            symbol = sp.Symbol(f"p_{self.label(x)}", real=True)
            self.pi_vars[x] = symbol
            self.reverse[symbol] = ("pi", x)
        return self.pi_vars[x]


class WardComplex:
    def __init__(self, fields: Fields) -> None:
        self.f = fields
        self.a = sp.Symbol("a", positive=True, nonzero=True)
        self.mass2 = sp.Symbol("mass2", real=True)

    def g(self, axis: int, x: Coord) -> sp.Expr:
        return (self.f.phi(add(x, E[axis])) - self.f.phi(x)) / self.a

    def force(self, x: Coord) -> sp.Expr:
        lap = sum(
            (self.g(axis, x) - self.g(axis, sub(x, E[axis]))) / self.a
            for axis in range(3)
        )
        return lap - self.mass2 * self.f.phi(x)

    def dt(self, expression: sp.Expr) -> sp.Expr:
        result = sp.Integer(0)
        # Snapshot: force() may lazily create additional neighbouring symbols.
        for symbol in tuple(expression.free_symbols):
            datum = self.f.reverse.get(symbol)
            if datum is None:
                continue
            kind, x = datum
            velocity = self.f.pi(x) if kind == "phi" else self.force(x)
            result += sp.diff(expression, symbol) * velocity
        return sp.expand(result)

    def rho(self, x: Coord) -> sp.Expr:
        gradient = sum(
            self.g(axis, x) ** 2 + self.g(axis, sub(x, E[axis])) ** 2
            for axis in range(3)
        ) / 4
        return (
            self.f.pi(x) ** 2 / 2
            + self.mass2 * self.f.phi(x) ** 2 / 2
            + gradient
        )

    def current(self, axis: int, x: Coord) -> sp.Expr:
        return -(
            self.f.pi(x) + self.f.pi(add(x, E[axis]))
        ) * self.g(axis, x) / 2

    def tau(self, left: int, right: int, x: Coord) -> sp.Expr:
        """Symmetric stress on sites (diagonal) and plaquettes (off diagonal)."""
        if left == right:
            axis = left
            longitudinal = self.g(axis, x) * self.g(axis, sub(x, E[axis])) / 2
            transverse = sum(
                self.g(other, x) ** 2
                + self.g(other, sub(x, E[other])) ** 2
                for other in range(3)
                if other != axis
            ) / 4
            return (
                self.f.pi(x) ** 2 / 2
                - self.mass2 * self.f.phi(x) ** 2 / 2
                + longitudinal
                - transverse
            )

        avg_left = (
            self.g(left, x) + self.g(left, add(x, E[right]))
        ) / 2
        avg_right = (
            self.g(right, x) + self.g(right, add(x, E[left]))
        ) / 2
        return sp.expand(avg_left * avg_right)

    def naive_tau(self, left: int, right: int, x: Coord) -> sp.Expr:
        """Continuum-looking mutant: misses the longitudinal product repair."""
        if left != right:
            return self.tau(left, right, x)
        axis = left
        longitudinal = (
            self.g(axis, x) ** 2
            + self.g(axis, sub(x, E[axis])) ** 2
        ) / 4
        transverse = sum(
            self.g(other, x) ** 2
            + self.g(other, sub(x, E[other])) ** 2
            for other in range(3)
            if other != axis
        ) / 4
        return (
            self.f.pi(x) ** 2 / 2
            - self.mass2 * self.f.phi(x) ** 2 / 2
            + longitudinal
            - transverse
        )

    def asymmetric_tau(self, left: int, right: int, x: Coord) -> sp.Expr:
        """Mutant with only one of the two plaquette edge averages."""
        if left == right:
            return self.tau(left, right, x)
        avg_left = (
            self.g(left, x) + self.g(left, add(x, E[right]))
        ) / 2
        return sp.expand(avg_left * self.g(right, x))

    def energy_residual(self, x: Coord) -> sp.Expr:
        divergence = sum(
            self.current(axis, x) - self.current(axis, sub(x, E[axis]))
            for axis in range(3)
        ) / self.a
        return sp.expand(self.dt(self.rho(x)) + divergence)

    def momentum_residual(
        self,
        axis: int,
        x: Coord,
        stress: str = "repaired",
    ) -> sp.Expr:
        tau = {
            "repaired": self.tau,
            "naive": self.naive_tau,
            "asymmetric": self.asymmetric_tau,
        }[stress]
        divergence = (
            tau(axis, axis, add(x, E[axis])) - tau(axis, axis, x)
        ) / self.a
        divergence += sum(
            tau(axis, other, x) - tau(axis, other, sub(x, E[other]))
            for other in range(3)
            if other != axis
        ) / self.a
        return sp.expand(self.dt(self.current(axis, x)) + divergence)


PASS = 0
TOTAL = 0


def is_zero(expression: sp.Expr) -> bool:
    return sp.cancel(sp.expand(expression)) == 0


def check(name: str, condition: bool) -> None:
    global PASS, TOTAL
    TOTAL += 1
    PASS += int(bool(condition))
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")


def coordinates_in(expression: sp.Expr, fields: Fields, kind: str) -> set[Coord]:
    return {
        x
        for symbol in expression.free_symbols
        if (datum := fields.reverse.get(symbol)) is not None
        for variable_kind, x in (datum,)
        if variable_kind == kind
    }


def local_universal_checks() -> None:
    print("\nLOCAL Z^3 POLYNOMIAL IDENTITIES")
    fields = Fields()
    ward = WardComplex(fields)

    check("fixed energy density/current obey exact energy Ward identity",
          is_zero(ward.energy_residual(ZERO)))

    for axis in range(3):
        check(
            f"axis {axis}: repaired symmetric stress obeys exact momentum Ward identity",
            is_zero(ward.momentum_residual(axis, ZERO)),
        )
        check(
            f"axis {axis}: naive averaged longitudinal square is a genuine polynomial mutant",
            not is_zero(ward.momentum_residual(axis, ZERO, "naive")),
        )
        check(
            f"axis {axis}: one-sided off-diagonal average is a Ward mutant",
            not is_zero(ward.momentum_residual(axis, ZERO, "asymmetric")),
        )

    for left in range(3):
        for right in range(left + 1, 3):
            check(
                f"tau_{left}{right} equals tau_{right}{left} on the same plaquette",
                is_zero(ward.tau(left, right, ZERO) - ward.tau(right, left, ZERO)),
            )
            check(
                f"asymmetric mutant really violates tau_{left}{right}=tau_{right}{left}",
                not is_zero(
                    ward.asymmetric_tau(left, right, ZERO)
                    - ward.asymmetric_tau(right, left, ZERO)
                ),
            )

    # Off-diagonal formula equals the compact diagonal-difference expression
    # suggested by the plaquette geometry.
    for left, right in ((0, 1), (0, 2), (1, 2)):
        xij = add(add(ZERO, E[left]), E[right])
        compact = (
            (fields.phi(xij) - fields.phi(ZERO)) ** 2
            - (fields.phi(add(ZERO, E[left])) - fields.phi(add(ZERO, E[right]))) ** 2
        ) / (4 * ward.a**2)
        check(
            f"tau_{left}{right} has the compact plaquette-diagonal formula",
            is_zero(ward.tau(left, right, ZERO) - compact),
        )


def locality_checks() -> None:
    print("\nREAL-SPACE SUPPORT / MASK AUDIT")
    fields = Fields()
    ward = WardComplex(fields)

    rho = ward.rho(ZERO)
    rho_phi = coordinates_in(rho, fields, "phi")
    rho_pi = coordinates_in(rho, fields, "pi")
    check("rho uses only the site and six nearest-neighbour phi sites",
          rho_phi == {ZERO, *E, *(sub(ZERO, e) for e in E)})
    check("rho uses only onsite pi", rho_pi == {ZERO})

    for axis in range(3):
        current = ward.current(axis, ZERO)
        expected_link_vertices = {ZERO, E[axis]}
        check(f"j_{axis} uses only its link endpoints (phi)",
              coordinates_in(current, fields, "phi") == expected_link_vertices)
        check(f"j_{axis} uses only its link endpoints (pi)",
              coordinates_in(current, fields, "pi") == expected_link_vertices)

        diagonal = ward.tau(axis, axis, ZERO)
        check(
            f"tau_{axis}{axis} has radius-one site support",
            all(sum(abs(component) for component in x) <= 1
                for x in coordinates_in(diagonal, fields, "phi"))
            and coordinates_in(diagonal, fields, "pi") == {ZERO},
        )

    for left, right in ((0, 1), (0, 2), (1, 2)):
        off_diagonal = ward.tau(left, right, ZERO)
        expected_corners = {
            ZERO,
            E[left],
            E[right],
            add(E[left], E[right]),
        }
        check(
            f"tau_{left}{right} uses exactly the four corners of its plaquette",
            coordinates_in(off_diagonal, fields, "phi") == expected_corners
            and not coordinates_in(off_diagonal, fields, "pi"),
        )


def periodic_zero_mode_checks() -> None:
    print("\nPERIODIC GLOBAL / HOMOGENEOUS MODES")
    size = 3
    fields = Fields(period=size)
    ward = WardComplex(fields)
    sites = list(product(range(size), repeat=3))

    total_energy_rate = sp.expand(sum(ward.dt(ward.rho(x)) for x in sites))
    check("periodic total energy is exactly conserved", is_zero(total_energy_rate))

    for axis in range(3):
        total_momentum_rate = sp.expand(
            sum(ward.dt(ward.current(axis, x)) for x in sites)
        )
        check(f"periodic total lattice momentum P_{axis}=sum j_{axis} is conserved",
              is_zero(total_momentum_rate))

        total_stress_divergence = sp.expand(sum(
            (
                ward.tau(axis, axis, add(x, E[axis]))
                - ward.tau(axis, axis, x)
                + sum(
                    ward.tau(axis, other, x)
                    - ward.tau(axis, other, sub(x, E[other]))
                    for other in range(3) if other != axis
                )
            ) / ward.a
            for x in sites
        ))
        check(f"axis {axis}: every periodic stress divergence has zero homogeneous mode",
              is_zero(total_stress_divergence))

        centered_form = -sum(
            fields.pi(x)
            * (fields.phi(add(x, E[axis])) - fields.phi(sub(x, E[axis])))
            / (2 * ward.a)
            for x in sites
        )
        link_form = sum(ward.current(axis, x) for x in sites)
        check(f"P_{axis} equals the centered-difference translation charge",
              is_zero(link_form - centered_form))

    homogeneous_substitution = {
        **{fields.phi(x): sp.Symbol("q0", real=True) for x in sites},
        **{fields.pi(x): sp.Symbol("p0", real=True) for x in sites},
    }
    check("homogeneous scalar mode has zero current",
          all(is_zero(sum(ward.current(axis, x) for x in sites).subs(homogeneous_substitution))
              for axis in range(3)))


def fourier_gluing_checks() -> None:
    """Build bilinear vertices from the real-space polynomials, not a mask stub."""
    print("\nBILINEAR FOURIER / RECIPROCAL-AXIS GLUING")
    fields = Fields()
    ward = WardComplex(fields)
    u = sp.symbols("u0:3", nonzero=True)
    v = sp.symbols("v0:3", nonzero=True)
    mixing, p_amplitude, q_amplitude = sp.symbols("mixing p_amplitude q_amplitude", real=True)
    components = [("rho", ward.rho(ZERO), ZERO)]
    components += [(f"j{axis}", ward.current(axis, ZERO), E[axis]) for axis in range(3)]
    components += [(f"tau{left}{right}", ward.tau(left, right, ZERO),
                    ZERO if left == right else add(E[left], E[right]))
                   for left in range(3) for right in range(left, 3)]
    for label, expression, mask in components:
        replacements = {}
        for symbol in expression.free_symbols:
            if symbol not in fields.reverse:
                continue
            kind, x = fields.reverse[symbol]
            wave_p = sp.prod(u[axis] ** (2 * x[axis]) for axis in range(3))
            wave_q = sp.prod(v[axis] ** (2 * x[axis]) for axis in range(3))
            replacements[symbol] = (wave_p + mixing * wave_q if kind == "phi"
                                    else p_amplitude * wave_p + mixing * q_amplitude * wave_q)
        vertex = sp.expand(expression.subs(replacements)).coeff(mixing)
        vertex *= sp.prod((u[axis] * v[axis]) ** (-mask[axis]) for axis in range(3))
        # u=exp(i ap/2), v=exp(i aq/2); q_i -> q_i+2pi/a sends v_i -> -v_i.
        check(f"{label}: actual bilinear vertex obeys all three staggered Bloch transitions",
              all(is_zero(vertex.subs(v[axis], -v[axis]) - (-1) ** mask[axis] * vertex)
                  for axis in range(3)))


def poisson(left: sp.Expr, right: sp.Expr,
            qvars: list[sp.Symbol], pvars: list[sp.Symbol]) -> sp.Expr:
    return sp.expand(sum(
        sp.diff(left, q) * sp.diff(right, p)
        - sp.diff(left, p) * sp.diff(right, q)
        for q, p in zip(qvars, pvars)
    ))


def second_bidifferential(left: sp.Expr, right: sp.Expr,
                          qvars: list[sp.Symbol], pvars: list[sp.Symbol]) -> sp.Expr:
    """The order-hbar^2 bidifferential in the Weyl/Moyal star product."""
    result = sp.Integer(0)
    for qa, pa in zip(qvars, pvars):
        for qb, pb in zip(qvars, pvars):
            result += sp.diff(left, qa, qb) * sp.diff(right, pa, pb)
            result -= sp.diff(left, qa, pb) * sp.diff(right, pa, qb)
            result -= sp.diff(left, pa, qb) * sp.diff(right, qa, pb)
            result += sp.diff(left, pa, pb) * sp.diff(right, qa, qb)
    return sp.expand(result)


def star_quadratic(left: sp.Expr, right: sp.Expr, hbar: sp.Symbol,
                   qvars: list[sp.Symbol], pvars: list[sp.Symbol]) -> sp.Expr:
    """Exact star product when both inputs have total canonical degree <= 2."""
    return sp.expand(
        left * right
        + sp.I * hbar * poisson(left, right, qvars, pvars) / 2
        - hbar**2 * second_bidifferential(left, right, qvars, pvars) / 8
    )


def quantum_weyl_checks() -> None:
    print("\nFINITE PERIODIC QUANTUM WEYL LIFT")
    # Two sites per direction keep the explicit star-product audit small.  The
    # local Z^3 identities above carry the universal real-space statement.
    size = 2
    fields = Fields(period=size)
    ward = WardComplex(fields)
    sites = list(product(range(size), repeat=3))
    qvars = [fields.phi(x) for x in sites]
    pvars = [fields.pi(x) for x in sites]
    hbar = sp.Symbol("hbar", real=True, nonzero=True)

    hamiltonian = sp.expand(sum(
        fields.pi(x) ** 2 / 2
        + ward.mass2 * fields.phi(x) ** 2 / 2
        + sum(ward.g(axis, x) ** 2 for axis in range(3)) / 2
        for x in sites
    ))
    observables = [ward.rho(ZERO)]
    observables += [ward.current(axis, ZERO) for axis in range(3)]
    observables += [ward.tau(axis, axis, ZERO) for axis in range(3)]
    observables += [ward.tau(left, right, ZERO)
                    for left, right in ((0, 1), (0, 2), (1, 2))]

    canonical = qvars + pvars
    check("Hamiltonian and every rho/j/tau symbol are quadratic",
          sp.Poly(hamiltonian, *canonical).total_degree() <= 2
          and all(sp.Poly(item, *canonical).total_degree() <= 2
                  for item in observables))

    # For quadratics, third and higher derivatives vanish, so star_quadratic
    # is the complete (not truncated) Weyl product.  This explicit calculation
    # also checks cancellation of its hbar^2 term in the commutator.
    for label, observable in zip(
        ["rho", "j0", "j1", "j2", "tau00", "tau11", "tau22",
         "tau01", "tau02", "tau12"],
        observables,
    ):
        heisenberg_symbol = sp.expand(
            sp.I
            * (
                star_quadratic(hamiltonian, observable, hbar, qvars, pvars)
                - star_quadratic(observable, hamiltonian, hbar, qvars, pvars)
            )
            / hbar
        )
        classical_symbol = poisson(observable, hamiltonian, qvars, pvars)
        check(f"Weyl Heisenberg bracket equals the classical Poisson bracket for {label}",
              is_zero(heisenberg_symbol - classical_symbol)
              and is_zero(classical_symbol - ward.dt(observable)))

    # The link current's two linear factors commute even before invoking the
    # general quadratic Weyl theorem.
    for axis in range(3):
        psum = fields.pi(ZERO) + fields.pi(E[axis])
        gradient = ward.g(axis, ZERO)
        check(f"axis {axis}: current factors have zero canonical bracket",
              is_zero(poisson(psum, gradient, qvars, pvars)))


def main() -> int:
    global PASS, TOTAL
    PASS = TOTAL = 0
    local_universal_checks()
    locality_checks()
    periodic_zero_mode_checks()
    fourier_gluing_checks()
    quantum_weyl_checks()
    print(f"\nCOUNTS: {PASS}/{TOTAL} exact checks passed")
    if PASS != TOTAL:
        print("VERDICT: CHECKER_FAILURE")
        return 1
    print(
        "VERDICT: FIXED_RHO_J_ADMIT_FINITE_RANGE_SYMMETRIC_FULL_3D_FREE_SCALAR_STRESS; "
        "EXACT_CLASSICAL_AND_WEYL_QUANTUM_WARD_IDENTITIES; FREE_PERIODIC_SCALAR_ONLY"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
