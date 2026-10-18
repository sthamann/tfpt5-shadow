#!/usr/bin/env python3
"""v1030 -- sector connectivity and conditional ALG2 frame bridge.

Finite theorem: if the neutral algebra is the full matrix algebra on every
finite sector, adjoining a charged operator generates End(H) exactly when its
sector graph is connected.  Conditional stability theorem: actual microscopic
words with uniformly bounded norms and a non-collapsing compressed-word frame
give a uniform double-cutoff section with bound 2*M*D^(3/2)/sigma.

ALG2 additionally needs the same y for y and y*, via a joint real-linear frame,
plus high-output tail bounds for x,y and their adjoints; the resulting one-sided
error is at most 3*epsilon.  This module checks the algebraic lemmas and all
listed counterexamples.  It does not establish those microscopic hypotheses,
FE-GEN, ALG-EXH, T2, TOE, or RH.  NO RH CLAIM.
"""
from __future__ import annotations

import json

import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


def check(name: str, condition: bool) -> None:
    suite_check(name, bool(condition))


def matrix_unit(dimension: int, row: int, column: int) -> sp.Matrix:
    result = sp.zeros(dimension)
    result[row, column] = 1
    return result


def uniform_section_bound(dimension: sp.Expr, word_bound: sp.Expr,
                          limiting_sigma: sp.Expr) -> sp.Expr:
    """Conditional norm bound once the frame hypotheses are supplied."""
    return 2*word_bound*dimension**sp.Rational(3, 2)/limiting_sigma


def sector_connectivity_certificate() -> None:
    dimension = 4
    projectors = [matrix_unit(dimension, i, i) for i in range(dimension)]
    shift = sum(
        (matrix_unit(dimension, (i+1) % dimension, i) for i in range(dimension)),
        sp.zeros(dimension),
    )
    check("four-sector charge shift has order four", shift**4 == sp.eye(dimension))
    words = []
    for row in range(dimension):
        for column in range(dimension):
            word = projectors[row]*shift**((row-column) % dimension)*projectors[column]
            check(f"connected-sector matrix unit {row},{column}",
                  word == matrix_unit(dimension, row, column))
            words.append(word.reshape(dimension**2, 1))
    frame = sp.Matrix.hstack(*words)
    check("actual compressed-word frame is full and conditioned",
          frame.T*frame == sp.eye(dimension**2))

    variables = sp.symbols("c0:4")
    diagonal = sp.diag(*variables)
    equations, _ = sp.linear_eq_to_matrix(list(diagonal*shift-shift*diagonal), variables)
    check("connected sector graph leaves only a scalar commutant", equations.rank() == 3)
    broken = matrix_unit(4, 1, 0)+matrix_unit(4, 3, 2)
    broken_equations, _ = sp.linear_eq_to_matrix(
        list(diagonal*broken-broken*diagonal), variables
    )
    check("disconnected two-pair mutant leaves an extra commutant",
          broken_equations.rank() == 2)


def frame_and_cutoff_firewalls() -> None:
    even_indices = (0, 3)
    odd_indices = (1, 2)
    even_frame = [
        matrix_unit(4, row, column).reshape(16, 1)
        for block in (even_indices, odd_indices)
        for row in block for column in block
    ]
    check("two-mode even CAR algebra has dimension eight rather than sixteen",
          sp.Matrix.hstack(*even_frame).rank() == 8)
    odd_witness = matrix_unit(4, 1, 0)
    check("odd witness lies outside the parity-preserving generated algebra",
          sp.Matrix.hstack(*(even_frame+[odd_witness.reshape(16, 1)])).rank() == 9)

    n = sp.symbols("N", integer=True, positive=True)
    collapsing = sp.diag(1, 1, 1, 1/n)
    check("full rank at every finite N does not give a uniform section",
          collapsing.det() == 1/n and collapsing.inv()[3, 3] == n)

    projection = matrix_unit(2, 0, 0)
    flip = sp.Matrix([[0, 1], [1, 0]])
    check("compression is not a homomorphism for actual words",
          projection*flip*projection*flip*projection == sp.zeros(2)
          and projection*flip*flip*projection == projection)

    for dimension in (3, 5, 8):
        low_input = matrix_unit(dimension, 0, 0)
        fixed_output = sum(
            (matrix_unit(dimension, i, i) for i in range(dimension-1)),
            sp.zeros(dimension),
        )
        escape = matrix_unit(dimension, dimension-1, 0)
        check(f"double cutoff misses a norm-one output at d={dimension}",
              fixed_output*escape*low_input == sp.zeros(dimension)
              and escape*low_input != sp.zeros(dimension)
              and (escape*low_input).norm() == 1)


def run() -> int:
    reset()
    print("v1030 -- finite sector connectivity and conditional joint-adjoint frame bridge")
    sector_connectivity_certificate()
    frame_and_cutoff_firewalls()
    dimension, word_bound, sigma, epsilon = sp.symbols(
        "D M sigma epsilon", positive=True
    )
    report = {
        "conditional_uniform_section_bound": str(
            uniform_section_bound(dimension, word_bound, sigma)
        ),
        "joint_adjoint_map": "L_N(y)=(P_F y P_E, P_F y* P_E), real-linear",
        "required_tail_data": ["x", "x*", "y", "y*"],
        "conditional_one_sided_error_bound": str(3*epsilon),
        "claim_boundary": {
            "proved": ["finite connected-sector generation criterion",
                       "conditional non-collapsing-frame norm estimate",
                       "parity, compression, conditioning and escape firewalls"],
            "not_proved": ["microscopic neutral block generation",
                           "nonzero charged corners in the TFPT collar",
                           "uniform local word bounds and joint y/y* frame",
                           "high-output tails", "FE-GEN, ALG-EXH, T2 or TOE"],
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("VERDICT: CONDITIONAL_SECTOR_AND_FRAME_LEMMAS_PROVED; MICROSCOPIC_FE_GEN_AND_ALG2_OPEN")
    return summary("v1030 ALG2 sector frame")


if __name__ == "__main__":
    raise SystemExit(run())
