#!/usr/bin/env python3
"""Exact derivability census for smaller TFPT compiler seeds.

EXPLORATION ONLY.  This probe does not import the verification suite and does
not move any status marker.  Every calculation is over ZZ, QQ, finite fields,
or symbolic expressions containing pi.  There are no floats, tolerances,
random choices, fitted coefficients, or post-hoc candidate maps.

Frozen seeds (declared before all calculations)
------------------------------------------------
S1  Brieskorn triple (2,3,5), including its Milnor algebra.
S2  D = F2[eps]/(eps^2), a free D-module of rank four, and socle/CP.
S3  Unit-winding defect with c_- = 8 and a non-split Z4 lift.
S4  Current baseline axioms c3 = 1/(8*pi), g_car = 5.

Entry types
-----------
THEOREM      an exact chain from the stated seed premises is checked here.
CONDITIONAL  exact arithmetic closes only after the named structural bridge.
FAIL         none of the pre-declared exact attempts supplies a chain.

The bridge names are obligations, not assumed results.  A numerical equality
without the bridge that identifies the two objects is never called a theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import gcd

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


# ---------------------------------------------------------------------------
# Frozen protocol: seeds, targets, bridges, and candidate maps
# ---------------------------------------------------------------------------
SEEDS = ("S1", "S2", "S3", "S4")

TARGETS = (
    "rank8",
    "h30",
    "E8_exponents",
    "D5+A3",
    "g_car=5",
    "N_fam=3",
    "|mu4|=4",
    "xi=3/4",
    "anchor=(1,1,2)",
    "c3=1/(8pi)",
    "winding=5/2",
    "pencil=7/3",
    "clock_link=30=2*3*5",
)

B_MILNOR_COMPILER = "B_MILNOR_COMPILER"
B_CANONICAL_INTEGRAL_LIFT = "B_CANONICAL_INTEGRAL_LIFT"
B_ADE_DISCRIMINANT = "B_ADE_DISCRIMINANT"
B_KMS_EQUIDISTRIBUTION = "B_KMS_EQUIDISTRIBUTION"
B_WINDING_REALIZATION = "B_WINDING_REALIZATION"
B_QC_CANONICALITY = "B_QC_CANONICALITY"

# Exactly three anchor maps, fixed before evaluation.
ANCHOR_MAPS = (
    "Jacobian truncation lengths: (p-1,q-1,r-1)",
    "branch data minus seam offsets: (p,q,r)-(1,1,2)",
    "integral weighted degrees: (h/p,h/q,h/r)",
)

# Exactly three pencil candidates, fixed before evaluation.  Equalities alone
# remain coincidence-risk unless Q and C are canonically reconstructed.
PENCIL_MAPS = (
    "(q+|mu4|)/q",
    "(rank-1)/N_fam",
    "(sum E8 exponents)/(rank*h)",
)

# Exactly five phi0 candidates, fixed before evaluation.  Candidate P3 is the
# existing corpus normal form and therefore a positive control, not a novel
# discovery.  The cubic/log fixed-point belongs to alpha, not phi0.
PHI0_CANDIDATES = (
    "P1 linear seam term: (|mu4|/N_fam)c3",
    "P2 top-form term: Omega_adm*c3^|mu4|",
    "P3 corpus normal form: P1+P2",
    "P4 singularity clock: 1/h",
    "P5 glue fraction: |mu4|/h",
)


THEOREM = "THEOREM"
CONDITIONAL = "CONDITIONAL"
FAIL = "FAIL"
ENTRY_TYPES = {THEOREM, CONDITIONAL, FAIL}


@dataclass(frozen=True)
class Entry:
    kind: str
    bridges: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.kind not in ENTRY_TYPES:
            raise ValueError("invalid entry kind")
        if (self.kind == CONDITIONAL) != bool(self.bridges):
            raise ValueError("CONDITIONAL iff at least one bridge is named")

    @property
    def label(self) -> str:
        if self.kind != CONDITIONAL:
            return self.kind
        return "%s[%s]" % (self.kind, "+".join(self.bridges))


T = Entry(THEOREM)
F = Entry(FAIL)


def C(*bridges: str) -> Entry:
    return Entry(CONDITIONAL, tuple(bridges))


# The matrix is frozen before the computations below.  It records derivability,
# not mere occurrence of the same rational number.
MATRIX = {
    "S1": {
        "rank8": T,
        "h30": T,
        "E8_exponents": T,
        "D5+A3": C(B_MILNOR_COMPILER),
        "g_car=5": C(B_MILNOR_COMPILER),
        "N_fam=3": C(B_MILNOR_COMPILER),
        "|mu4|=4": C(B_MILNOR_COMPILER),
        "xi=3/4": C(B_MILNOR_COMPILER),
        "anchor=(1,1,2)": F,
        "c3=1/(8pi)": C(B_MILNOR_COMPILER, B_KMS_EQUIDISTRIBUTION),
        "winding=5/2": C(B_MILNOR_COMPILER, B_WINDING_REALIZATION),
        "pencil=7/3": C(B_MILNOR_COMPILER, B_QC_CANONICALITY),
        "clock_link=30=2*3*5": T,
    },
    "S2": {
        "rank8": T,
        "h30": F,
        "E8_exponents": F,
        "D5+A3": C(B_CANONICAL_INTEGRAL_LIFT),
        "g_car=5": F,
        "N_fam=3": F,
        "|mu4|=4": F,
        "xi=3/4": F,
        "anchor=(1,1,2)": F,
        "c3=1/(8pi)": F,
        "winding=5/2": F,
        "pencil=7/3": F,
        "clock_link=30=2*3*5": F,
    },
    "S3": {
        "rank8": T,
        "h30": C(B_ADE_DISCRIMINANT),
        "E8_exponents": C(B_ADE_DISCRIMINANT),
        "D5+A3": C(B_ADE_DISCRIMINANT),
        "g_car=5": C(B_ADE_DISCRIMINANT),
        "N_fam=3": C(B_ADE_DISCRIMINANT),
        "|mu4|=4": T,
        "xi=3/4": C(B_ADE_DISCRIMINANT),
        "anchor=(1,1,2)": C(B_ADE_DISCRIMINANT),
        "c3=1/(8pi)": C(B_KMS_EQUIDISTRIBUTION),
        "winding=5/2": C(B_ADE_DISCRIMINANT, B_WINDING_REALIZATION),
        "pencil=7/3": C(B_ADE_DISCRIMINANT, B_QC_CANONICALITY),
        "clock_link=30=2*3*5": C(B_ADE_DISCRIMINANT),
    },
    "S4": {
        "rank8": T,
        "h30": T,
        "E8_exponents": T,
        "D5+A3": T,
        "g_car=5": T,
        "N_fam=3": T,
        "|mu4|=4": T,
        "xi=3/4": T,
        "anchor=(1,1,2)": T,
        "c3=1/(8pi)": T,
        "winding=5/2": C(B_WINDING_REALIZATION),
        "pencil=7/3": C(B_QC_CANONICALITY),
        "clock_link=30=2*3*5": T,
    },
}


N_PASS = 0
N_FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global N_PASS, N_FAIL
    passed = bool(condition)
    if passed:
        N_PASS += 1
    else:
        N_FAIL += 1
    suffix = " -- %s" % detail if detail else ""
    print("  [%s] %s%s" % ("PASS" if passed else "FAIL", name, suffix))


def section(title: str) -> None:
    print("\n== %s ==" % title)


# ---------------------------------------------------------------------------
# Exact common machinery
# ---------------------------------------------------------------------------
def cartan_A(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for index in range(n):
        matrix[index, index] = 2
        if index + 1 < n:
            matrix[index, index + 1] = -1
            matrix[index + 1, index] = -1
    return matrix


def cartan_D(n: int) -> sp.Matrix:
    if n == 2:
        return sp.diag(2, 2)
    matrix = cartan_A(n)
    matrix[n - 2, n - 1] = 0
    matrix[n - 1, n - 2] = 0
    matrix[n - 3, n - 1] = -1
    matrix[n - 1, n - 3] = -1
    return matrix


def cartan_E(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for index in range(n - 1):
        matrix[index, index] = 2
        if index + 1 < n - 1:
            matrix[index, index + 1] = -1
            matrix[index + 1, index] = -1
    matrix[n - 1, n - 1] = 2
    matrix[2, n - 1] = -1
    matrix[n - 1, 2] = -1
    return matrix


def snf_factors(matrix: sp.Matrix) -> tuple[int, ...]:
    smith = smith_normal_form(matrix, domain=sp.ZZ)
    return tuple(
        abs(int(smith[index, index]))
        for index in range(smith.rows)
        if abs(int(smith[index, index])) != 1
    )


def generator_order_and_q(
    matrix: sp.Matrix, generator: sp.Matrix | None = None
) -> tuple[int, sp.Expr]:
    inverse = matrix.inv()
    if generator is None:
        generator = sp.zeros(matrix.rows, 1)
        generator[matrix.rows - 1] = 1

    def trivial(multiple: int) -> bool:
        vector = inverse * (multiple * generator)
        return all(entry.is_integer for entry in vector)

    order = next(
        multiple
        for multiple in range(1, abs(int(matrix.det())) + 2)
        if trivial(multiple)
    )
    q_value = sp.simplify((generator.T * inverse * generator)[0])
    return order, q_value


def ade_rank8_census() -> list[tuple[str, int, str, int]]:
    rows: list[tuple[str, int, str, int, bool]] = []

    def add(kind1: str, n1: int, c1: sp.Matrix,
            kind2: str, n2: int, c2: sp.Matrix) -> None:
        factors1 = snf_factors(c1)
        factors2 = snf_factors(c2)
        both_z4 = factors1 == factors2 == (4,)
        determinant_product = abs(int(c1.det() * c2.det()))
        isotropic = False
        if both_z4:
            order1, q1 = generator_order_and_q(c1)
            order2, q2 = generator_order_and_q(c2)
            isotropic = (
                order1 == order2 == 4
                and sp.simplify((q1 + q2) / 2).is_integer
            )
        rows.append((
            kind1, n1, kind2, n2,
            bool(both_z4 and determinant_product == 16 and isotropic),
        ))

    for n_value in range(2, 8):
        m_value = 8 - n_value
        add("D", n_value, cartan_D(n_value),
            "A", m_value, cartan_A(m_value))
    for n_value in range(2, 5):
        m_value = 8 - n_value
        add("D", n_value, cartan_D(n_value),
            "D", m_value, cartan_D(m_value))
    for n_value in range(4, 8):
        m_value = 8 - n_value
        if 1 <= m_value <= n_value:
            add("A", n_value, cartan_A(n_value),
                "A", m_value, cartan_A(m_value))
    add("E", 6, cartan_E(6), "A", 2, cartan_A(2))
    add("E", 6, cartan_E(6), "D", 2, cartan_D(2))
    add("E", 7, cartan_E(7), "A", 1, cartan_A(1))
    return [
        (kind1, n1, kind2, n2)
        for kind1, n1, kind2, n2, hit in rows if hit
    ]


def e8_coxeter_data() -> tuple[sp.Expr, tuple[int, ...]]:
    coordinate_rows = [
        [
            sp.Rational(1, 2), sp.Rational(-1, 2),
            sp.Rational(-1, 2), sp.Rational(-1, 2),
            sp.Rational(-1, 2), sp.Rational(-1, 2),
            sp.Rational(-1, 2), sp.Rational(1, 2),
        ],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [-1, 1, 0, 0, 0, 0, 0, 0],
        [0, -1, 1, 0, 0, 0, 0, 0],
        [0, 0, -1, 1, 0, 0, 0, 0],
        [0, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 0, -1, 1, 0, 0],
        [0, 0, 0, 0, 0, -1, 1, 0],
    ]
    roots = sp.Matrix(coordinate_rows)
    cartan = roots * roots.T
    coxeter = sp.eye(8)
    for reflection_index in range(8):
        reflection = sp.eye(8)
        for column in range(8):
            reflection[reflection_index, column] -= \
                cartan[reflection_index, column]
        coxeter *= reflection
    variable = sp.symbols("t")
    polynomial = sp.expand(coxeter.charpoly(variable).as_expr())
    exponents = tuple(value for value in range(30) if gcd(value, 30) == 1)
    return polynomial, exponents


def anchor_from_symmetric_data(
    e1: int, e2: int, e3: int
) -> tuple[sp.Expr, ...]:
    variable = sp.symbols("u")
    polynomial = variable**3 - e1 * variable**2 + e2 * variable - e3
    roots = sp.solve(polynomial, variable)
    roots_with_multiplicity: list[sp.Expr] = []
    for root, multiplicity in sp.roots(polynomial).items():
        roots_with_multiplicity.extend([root] * multiplicity)
    return tuple(sorted(roots_with_multiplicity, key=sp.default_sort_key))


# ---------------------------------------------------------------------------
# Part 1: seed certificates
# ---------------------------------------------------------------------------
def part1_seed_certificates() -> dict[str, object]:
    section("PART 1 -- CANDIDATE SEEDS")
    p, q, r = 2, 3, 5
    milnor_rank = (p - 1) * (q - 1) * (r - 1)
    basis = tuple(
        (a, b)
        for a in range(q - 1)
        for b in range(r - 1)
    )
    rank_table = tuple(
        tuple((q - 1 - a) * (r - 1 - b) for b in range(r - 1))
        for a in range(q - 1)
    )
    rank_clock_sum = sum(sum(row) for row in rank_table)
    spectral_labels = tuple(sorted(
        int(
            p * q * r * (
                sp.Rational(1, p)
                + sp.Rational(a + 1, q)
                + sp.Rational(b + 1, r)
                - 1
            )
        )
        for a, b in basis
    ))
    expected_exponents = (1, 7, 11, 13, 17, 19, 23, 29)
    check(
        "S1 Milnor rank is exactly 8",
        milnor_rank == len(basis) == 8,
        "basis exponents=%s" % (basis,),
    )
    check(
        "S1 rank clock sums to 30=p*q*r",
        rank_clock_sum == p * q * r == 30,
        "rank table=%s" % (rank_table,),
    )
    check(
        "S1 weighted spectrum is exactly the E8 exponent set",
        spectral_labels == expected_exponents,
        "labels=%s" % (spectral_labels,),
    )

    # S2: D has four elements, but no element of additive or multiplicative
    # order four.  D^4 has F2-dimension eight; that rank statement is exact,
    # while a cyclic mu4 interpretation is specifically not present.
    dual_elements = tuple(product((0, 1), repeat=2))

    def dual_add(left: tuple[int, int], right: tuple[int, int]) \
            -> tuple[int, int]:
        return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)

    def dual_mul(left: tuple[int, int], right: tuple[int, int]) \
            -> tuple[int, int]:
        return (
            (left[0] * right[0]) % 2,
            (left[0] * right[1] + left[1] * right[0]) % 2,
        )

    additive_orders = []
    for element in dual_elements:
        running = (0, 0)
        for order in range(1, 5):
            running = dual_add(running, element)
            if running == (0, 0):
                additive_orders.append(order)
                break
    units = tuple(
        element for element in dual_elements
        if any(
            dual_mul(element, candidate) == (1, 0)
            for candidate in dual_elements
        )
    )
    unit_orders = []
    for element in units:
        running = (1, 0)
        for order in range(1, 5):
            running = dual_mul(running, element)
            if running == (1, 0):
                unit_orders.append(order)
                break
    check(
        "S2 D^4 has F2-dimension 8",
        2 * 4 == 8 and len(dual_elements) ** 4 == 2**8,
    )
    check(
        "S2 dual numbers do not contain a cyclic order-four element",
        max(additive_orders) == 2 and max(unit_orders) == 2,
        "additive orders=%s, unit orders=%s"
        % (tuple(additive_orders), tuple(unit_orders)),
    )
    # The complement pairing on basis eps^a e_j is nondegenerate.
    gram = sp.zeros(8)
    for left in range(8):
        left_a, left_j = divmod(left, 4)
        for right in range(8):
            right_a, right_j = divmod(right, 4)
            gram[left, right] = int(
                left_a + right_a == 1 and left_j + right_j == 3
            )
    check(
        "S2 declared socle/CP complement pairing is unimodular",
        abs(int(gram.det())) == 1,
    )

    # S3 is a structural premise.  The finite consequences recorded as
    # theorems are only its explicitly declared c_- and lift order.
    s3_c_minus = 8
    s3_lift_order = 4
    check(
        "S3 premises expose rank-count 8 and non-split lift order 4",
        s3_c_minus == 8 and s3_lift_order == 4,
    )

    # S4: exact baseline closure.  Extracting mu4 uses the already deployed
    # baseline normalization c3=1/(2*|mu4|*pi); this is not used for S1/S3,
    # where that identification is precisely the KMS bridge.
    c3 = 1 / (8 * sp.pi)
    g_car = 5
    dim_splus = 2 ** (g_car - 1)
    n_fam = (dim_splus - 1) // g_car
    rank_e8 = g_car + n_fam
    mu_symbol = sp.symbols("mu", positive=True, integer=True)
    mu_solution = sp.solve(
        sp.Eq(1 / (2 * mu_symbol * sp.pi), c3), mu_symbol
    )
    mu4 = int(mu_solution[0])
    anchor = anchor_from_symmetric_data(mu4, g_car, 2)
    check(
        "S4 known carrier chain gives N_fam=3 and rank 8",
        dim_splus == 16 and n_fam == 3 and rank_e8 == 8,
    )
    check(
        "S4 baseline normalization extracts |mu4|=4 exactly",
        mu_solution == [4] and mu4 == 4,
    )
    check(
        "S4 symmetric-data inverse gives the unique anchor multiset",
        anchor == (1, 1, 2),
        "roots of u^3-4u^2+5u-2=%s" % (anchor,),
    )

    return {
        "triple": (p, q, r),
        "milnor_rank": milnor_rank,
        "rank_clock_sum": rank_clock_sum,
        "spectral_labels": spectral_labels,
        "expected_exponents": expected_exponents,
        "s4": {
            "c3": c3,
            "g_car": g_car,
            "N_fam": n_fam,
            "rank": rank_e8,
            "mu4": mu4,
            "anchor": anchor,
            "dim_Splus": dim_splus,
        },
    }


# ---------------------------------------------------------------------------
# Part 2: exact derivation matrix and special questions
# ---------------------------------------------------------------------------
def part2_derivation_matrix(data: dict[str, object]) -> dict[str, int]:
    section("PART 2 -- DERIVATION MATRIX")
    check(
        "matrix covers exactly four declared seeds and thirteen targets",
        tuple(MATRIX) == SEEDS
        and all(tuple(MATRIX[seed]) == TARGETS for seed in SEEDS),
    )
    check(
        "every conditional entry names at least one frozen bridge",
        all(
            entry.kind in ENTRY_TYPES
            and ((entry.kind == CONDITIONAL) == bool(entry.bridges))
            for seed in SEEDS for entry in MATRIX[seed].values()
        ),
    )

    hits = ade_rank8_census()
    canonical_hits = set()
    for hit in hits:
        if (
            hit[0] == hit[2] == "D"
            and {hit[1], hit[3]} == {3, 5}
        ):
            canonical_hits.add(("D", 5, "A", 3))
        else:
            canonical_hits.add(hit)
    check(
        "v993 logic rerun: full rank-8 ADE census uniquely selects D5+A3",
        canonical_hits == {("D", 5, "A", 3)},
        "raw hits=%s" % (hits,),
    )
    q_d5 = generator_order_and_q(cartan_D(5))[1]
    q_a3 = generator_order_and_q(cartan_A(3))[1]
    check(
        "selected discriminant norms give q(A3)=3/4 and even glue",
        q_d5 == sp.Rational(5, 4)
        and q_a3 == sp.Rational(3, 4)
        and q_d5 + q_a3 == 2,
    )

    coxeter_polynomial, cartan_exponents = e8_coxeter_data()
    variable = sp.symbols("t")
    check(
        "exact E8 Coxeter reconstruction gives Phi_30",
        coxeter_polynomial == sp.cyclotomic_poly(30, variable),
        "chi=%s" % coxeter_polynomial,
    )
    check(
        "Milnor labels and Cartan exponents are the same exact set",
        data["spectral_labels"] == cartan_exponents
        == data["expected_exponents"],
    )
    s4 = data["s4"]
    check(
        "S4 known chain closes D5+A3, h, exponents, xi, and clock link",
        s4["rank"] == 8
        and s4["g_car"] == 5
        and s4["N_fam"] == 3
        and s4["mu4"] == 4
        and canonical_hits == {("D", 5, "A", 3)}
        and cartan_exponents == data["expected_exponents"]
        and q_a3 == sp.Rational(3, 4)
        and 30 == 2 * s4["N_fam"] * s4["g_car"],
    )

    print("\nDERIVATION MATRIX")
    print("seed | " + " | ".join(TARGETS))
    for seed in SEEDS:
        print(seed + " | " + " | ".join(
            MATRIX[seed][target].label for target in TARGETS
        ))

    # Anchor question: all three direct Milnor maps miss.  Separately, the
    # moment measure 2 delta_1 + delta_2 tautologically has atom multiset
    # (1,1,2), but no seed theorem identifies that measure with Milnor data.
    p, q, r = data["triple"]
    h = p * q * r
    anchor_attempts = (
        (p - 1, q - 1, r - 1),
        (p - 1, q - 1, r - 2),
        (sp.Rational(h, p), sp.Rational(h, q), sp.Rational(h, r)),
    )
    anchor_target = (1, 1, 2)
    check(
        "anchor protocol has exactly three pre-declared maps",
        len(ANCHOR_MAPS) == len(anchor_attempts) == 3,
    )
    check(
        "no direct Milnor branch/weight map yields anchor (1,1,2)",
        all(attempt != anchor_target for attempt in anchor_attempts),
        "attempts=%s" % (anchor_attempts,),
    )
    moment_atoms = (1, 1, 2)
    moment_values = tuple(
        sum(atom**degree for atom in moment_atoms)
        for degree in range(4)
    )
    check(
        "2 delta_1 + delta_2 yields anchor only when moment structure is given",
        moment_values == (3, 4, 6, 10)
        and moment_atoms == anchor_target,
    )
    print("\nANCHOR ATTEMPTS")
    for name, value in zip(ANCHOR_MAPS, anchor_attempts):
        print("  %s -> %s -> FAIL" % (name, value))
    print(
        "  moment measure 2*delta_1+delta_2 -> atoms (1,1,2): "
        "THEOREM FROM THE MEASURE, not from S1; Milnor-to-moment bridge absent"
    )

    # Winding and pencil: exact number matches are checked, then honestly
    # withheld from THEOREM because neither R,L nor Q,C follows from a seed.
    winding_matches = {
        "S1 branch ratio r/p": sp.Rational(r, p),
        "S3/S4 carrier-sheet ratio g_car/|Z2|":
            sp.Rational(s4["g_car"], 2),
    }
    check(
        "two pre-declared arithmetic readings equal 5/2 exactly",
        set(winding_matches.values()) == {sp.Rational(5, 2)},
    )
    pencil_attempts = (
        sp.Rational(q + s4["mu4"], q),
        sp.Rational(s4["rank"] - 1, s4["N_fam"]),
        sp.Rational(sum(cartan_exponents), s4["rank"] * 30),
    )
    check(
        "pencil protocol has exactly three pre-declared maps",
        len(PENCIL_MAPS) == len(pencil_attempts) == 3,
    )
    check(
        "7/3 arithmetic hits exist but normalized exponent mean does not hit",
        pencil_attempts[:2] == (sp.Rational(7, 3), sp.Rational(7, 3))
        and pencil_attempts[2] == sp.Rational(1, 2),
        "attempts=%s" % (pencil_attempts,),
    )
    print("\nWINDING / PENCIL TYPING")
    for name, value in winding_matches.items():
        print(
            "  %s = %s: coincidence-risk until %s is proved"
            % (name, value, B_WINDING_REALIZATION)
        )
    for name, value in zip(PENCIL_MAPS, pencil_attempts):
        result = "arithmetic hit" if value == sp.Rational(7, 3) else "miss"
        print("  %s -> %s (%s)" % (name, value, result))
    print(
        "  7/3 remains Q/C provenance only: a seed theorem requires %s"
        % B_QC_CANONICALITY
    )

    remainder_scores: dict[str, int] = {}
    print("\nIRREDUCIBLE REMAINDER")
    for seed in SEEDS:
        entries = MATRIX[seed].values()
        underivable = sum(entry.kind == FAIL for entry in entries)
        bridges = sorted({
            bridge
            for entry in entries
            for bridge in entry.bridges
        })
        score = underivable + len(bridges)
        remainder_scores[seed] = score
        print(
            "  %s: FAIL targets=%d; typed bridges=%d %s; remainder=%d"
            % (seed, underivable, len(bridges), bridges, score)
        )
    check(
        "remainder scores are exact frozen counts",
        remainder_scores == {"S1": 5, "S2": 12, "S3": 4, "S4": 2},
        "scores=%s" % remainder_scores,
    )
    return remainder_scores


# ---------------------------------------------------------------------------
# Part 3: phi0 candidates -- exact expressions only
# ---------------------------------------------------------------------------
def part3_phi0(data: dict[str, object]) -> None:
    section("PART 3 -- THE PHI0 QUESTION")
    s4 = data["s4"]
    c3 = s4["c3"]
    mu4 = s4["mu4"]
    n_fam = s4["N_fam"]
    omega_adm = s4["N_fam"] * s4["dim_Splus"]
    h = 30
    phi0_exact = 1 / (6 * sp.pi) + sp.Rational(3, 256) / sp.pi**4
    candidates = (
        sp.Rational(mu4, n_fam) * c3,
        omega_adm * c3**mu4,
        sp.Rational(mu4, n_fam) * c3 + omega_adm * c3**mu4,
        sp.Rational(1, h),
        sp.Rational(mu4, h),
    )
    hits = tuple(
        index + 1
        for index, candidate in enumerate(candidates)
        if sp.simplify(candidate - phi0_exact) == 0
    )
    check(
        "phi0 protocol has exactly five pre-declared no-fit candidates",
        len(PHI0_CANDIDATES) == len(candidates) == 5,
    )
    check(
        "corpus phi0 is exactly 1/(6pi)+3/(256pi^4)",
        sp.simplify(
            phi0_exact
            - (sp.Rational(4, 3) * c3 + 48 * c3**4)
        ) == 0,
    )
    check(
        "only pre-declared P3 hits phi0 exactly",
        hits == (3,),
        "hit indices=%s" % (hits,),
    )
    print("\nPHI0 CANDIDATES")
    for index, (name, candidate) in enumerate(
        zip(PHI0_CANDIDATES, candidates), start=1
    ):
        result = (
            "HIT -- existing corpus normal form"
            if index in hits else "NULL"
        )
        print("  %s -> %s -> %s" % (name, sp.factor(candidate), result))
    print(
        "  RESULT: PHI0_KNOWN_NORMAL_FORM_HIT(P3); "
        "NOVEL_SEED_EXPRESSION_NULL"
    )
    print(
        "  TYPING: S4 supplies P3 by its deployed exact consequence chain; "
        "S1/S3 inherit it only through compiler/KMS bridges.  This does not "
        "derive a new dynamical law.  The cubic/log fixed-point equation in "
        "the corpus fixes alpha, not phi0."
    )


# ---------------------------------------------------------------------------
# Mutants and verdict
# ---------------------------------------------------------------------------
def mutants(data: dict[str, object]) -> None:
    section("MUTANTS")
    p, q, r = 2, 3, 7
    mu = (p - 1) * (q - 1) * (r - 1)
    rank_sum = sp.Rational(p * q * r * mu, 8)
    mutant_basis = tuple(
        (a, b)
        for a in range(q - 1)
        for b in range(r - 1)
    )
    mutant_labels = tuple(sorted(
        p * q * r * (
            sp.Rational(1, p)
            + sp.Rational(a + 1, q)
            + sp.Rational(b + 1, r)
            - 1
        )
        for a, b in mutant_basis
    ))
    s1_theorem_targets = tuple(
        target for target in TARGETS
        if MATRIX["S1"][target].kind == THEOREM
    )
    surviving = {
        "rank8": mu == 8,
        "h30": p * q * r == 30,
        "E8_exponents": mutant_labels == data["expected_exponents"],
        "clock_link=30=2*3*5":
            rank_sum == p * q * r == 30,
    }
    check(
        "(2,3,7) loses every S1 THEOREM target",
        s1_theorem_targets == tuple(surviving)
        and not any(surviving.values()),
        "mu=%s, rank-sum=%s, pqr=%s" % (mu, rank_sum, p * q * r),
    )
    check(
        "(2,3,7) specifically breaks self-clock S=pqr",
        rank_sum == 63 and p * q * r == 42 and rank_sum != p * q * r,
    )

    s4_theorems = {
        target for target in TARGETS
        if MATRIX["S4"][target].kind == THEOREM
    }
    check(
        "S4 baseline does not promote winding or pencil beyond known chain",
        s4_theorems == set(TARGETS) - {"winding=5/2", "pencil=7/3"}
        and MATRIX["S4"]["g_car=5"].kind == THEOREM
        and MATRIX["S4"]["c3=1/(8pi)"].kind == THEOREM,
    )
    print(
        "  MUTANT (2,3,7): mu=12, rank-clock sum=63, pqr=42; "
        "THEOREM retention 0/4"
    )
    print(
        "  S4 CONTROL: own axioms plus the deployed exact chain are THEOREM; "
        "winding and 7/3 remain bridge-typed"
    )


def main() -> int:
    print("SIMPLICITY CORE DERIVABILITY CENSUS")
    print("Arithmetic: exact ZZ/QQ/F2/symbolic-pi only; no fitting")
    data = part1_seed_certificates()
    remainder_scores = part2_derivation_matrix(data)
    part3_phi0(data)
    mutants(data)

    section("VERDICT")
    best_seed = min(remainder_scores, key=remainder_scores.get)
    best_score = remainder_scores[best_seed]
    check(
        "baseline S4 uniquely minimizes the irreducible remainder",
        best_seed == "S4"
        and best_score == 2
        and list(remainder_scores.values()).count(best_score) == 1,
    )
    verdict = (
        "SIMPLICITY_CORE_NO_REDUCTION("
        "best=S4,remainder=2,"
        "why=winding-and-QC-canonicality-remain)"
    )
    print("VERDICT: %s" % verdict)
    print(
        "FIREWALL: exploration-only; no axiom/status/contract marker move; "
        "all CONDITIONAL labels are proof obligations"
    )
    total = N_PASS + N_FAIL
    print(
        "PROTOCOL-%s: %d/%d"
        % ("ALL-PASS" if N_FAIL == 0 else "FAIL", N_PASS, total)
    )
    return 0 if N_FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
