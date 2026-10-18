#!/usr/bin/env python3
"""v1029 -- local linear spin-2 constraint quotient with a global-mode fence.

This self-contained exact checker proves a quadratic target theory at nonzero
momentum: four first-class local polynomial constraints reduce a symmetric
tensor canonical pair to two positive z=1 modes.  On the staggered regulator
the only derivative zero is the global mode.

The unmodified periodic k=0 block is not positive: for p_0=r(1,1,1,0,0,0),
H_0=-3r^2/4.  Positivity therefore requires removing the complete global
canonical block as a separate zero-mean prescription.  This is not a stable
unqualified local-parent theorem, a QLGW32 embedding, nonlinear gravity, TOE,
or RH progress.  NO RH CLAIM.
"""
from __future__ import annotations

import itertools
import math

import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


def check(name: str, condition: bool) -> None:
    suite_check(name, bool(condition))


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def tensor_data(k: sp.Matrix) -> tuple[sp.Matrix, ...]:
    basis = []
    for index in range(3):
        element = sp.zeros(3)
        element[index, index] = 1
        basis.append(element)
    for left, right in ((1, 2), (0, 2), (0, 1)):
        element = sp.zeros(3)
        element[left, right] = element[right, left] = 1/sp.sqrt(2)
        basis.append(element)
    b = sp.Matrix.hstack(*(element*k for element in basis))
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    k2 = (k.T*k)[0]
    v = b.T*k
    scalar = v-k2*trace
    kp = sp.eye(6)-trace*trace.T/2
    kq = k2*(sp.eye(6)-trace*trace.T)-2*b.T*b+trace*v.T+v*trace.T
    return b, trace, scalar, kp, kq, k2


def generic_and_axis_certificate() -> tuple[sp.Matrix, ...]:
    x, y, z = sp.symbols("x y z", real=True)
    k = sp.Matrix([x, y, z])
    b, trace, scalar, kp, kq, k2 = tensor_data(k)
    symplectic = sp.BlockMatrix(
        [[sp.zeros(6), sp.eye(6)], [-sp.eye(6), sp.zeros(6)]]
    ).as_explicit()
    constraints = sp.BlockMatrix(
        [[scalar.T, sp.zeros(1, 6)], [sp.zeros(3, 6), b]]
    ).as_explicit()
    energy = sp.diag(kq, kp)
    evolution = sp.zeros(4)
    evolution[0, 1:] = k.T
    check("all four constraints are first class at generic momentum",
          zero(constraints*symplectic*constraints.T))
    check("Hamiltonian evolution preserves the constraint ideal",
          zero(constraints*symplectic*energy-evolution*constraints))
    check("spatial gauge directions lie in the potential kernel", zero(kq*b.T))
    check("scalar gauge kinetic variation is a momentum constraint",
          zero(kp*scalar-b.T*k))
    check("scalar-constraint gauge direction has zero kinetic norm",
          zero(scalar.T*kp*scalar))
    check("momentum Gram identity",
          zero(b*b.T-(k2*sp.eye(3)+k*k.T)/2))
    check("scalar constraint has squared norm 2|k|^4",
          sp.simplify((scalar.T*scalar)[0]-2*k2**2) == 0)

    ba, ta, sa, kpa, kqa, _ = tensor_data(sp.Matrix([0, 0, z]))
    tt = sp.Matrix.hstack(
        sp.Matrix([1, -1, 0, 0, 0, 0])/sp.sqrt(2),
        sp.Matrix([0, 0, 0, 0, 0, 1]),
    )
    check("two TT polarizations are orthonormal", zero(tt.T*tt-sp.eye(2)))
    check("TT polarizations are transverse and traceless", zero(ba*tt) and zero(ta.T*tt))
    check("reduced kinetic energy is the positive unit matrix", zero(tt.T*kpa*tt-sp.eye(2)))
    check("reduced potential is |k|^2 times the unit matrix", zero(tt.T*kqa*tt-z**2*sp.eye(2)))
    check("full equations preserve the TT representative",
          zero(kpa*tt-tt) and zero(kqa*tt-z**2*tt))
    check("unconstrained conformal kinetic mode is negative",
          (trace.T*kp*trace)[0] == -sp.Rational(3, 2))

    for momentum in ((1, 0, 0), (1, 2, 3), (-2, 1, 5)):
        bm, tm, sm, kpm, kqm, km2 = tensor_data(sp.Matrix(momentum))
        cm = sp.BlockMatrix(
            [[sm.T, sp.zeros(1, 6)], [sp.zeros(3, 6), bm]]
        ).as_explicit()
        physical = sp.Matrix.hstack(*bm.col_join(tm.T).nullspace())
        check(f"rank four gives physical phase-space dimension four at {momentum}",
              cm.rank() == 4 and 12-2*cm.rank() == 4)
        check(f"TT quotient has two z=1 modes at {momentum}",
              physical.cols == 2 and zero(kpm*physical-physical)
              and zero(kqm*physical-km2*physical))
    return x, y, z, k, b, trace, scalar, kp, kq, symplectic, constraints


def staggered_and_global_certificate(data: tuple[sp.Matrix, ...]) -> None:
    x, y, z, k, b, trace, scalar, kp, kq, symplectic, constraints = data
    masks = ((0, 0, 0), (0, 0, 0), (0, 0, 0),
             (0, 1, 1), (1, 0, 1), (1, 1, 0))
    for axis in range(3):
        vector_gluing = sp.eye(3)
        vector_gluing[axis, axis] = -1
        tensor_gluing = sp.diag(*(1 if mask[axis] == 0 else -1 for mask in masks))
        bp, _, sp_scalar, kpp, kqp, _ = tensor_data(vector_gluing*k)
        check(f"staggered vector-derivative gluing axis {axis}",
              zero(bp-vector_gluing*b*tensor_gluing))
        check(f"staggered scalar-constraint gluing axis {axis}",
              zero(sp_scalar-tensor_gluing*scalar))
        check(f"local Hamiltonian Bloch gluing axis {axis}",
              zero(kqp-tensor_gluing*kq*tensor_gluing)
              and zero(kpp-tensor_gluing*kp*tensor_gluing))

    for size in (4, 6, 8):
        indices = range(-size//2, size//2)
        centered_zeros = sum(
            all(2*entry % size == 0 for entry in triple)
            for triple in itertools.product(indices, repeat=3)
        )
        staggered_zeros = sum(
            all(entry % size == 0 for entry in triple)
            for triple in itertools.product(indices, repeat=3)
        )
        check(f"centered-derivative mutant has eight zeros at L={size}", centered_zeros == 8)
        check(f"staggered derivative has only the global zero at L={size}", staggered_zeros == 1)

    for size in (8, 16, 32, 64):
        ratio = 2*math.sin(math.pi/size)/(2*math.pi/size)
        check(f"analytic sine bound gives linear IR at L={size}",
              1-(math.pi/size)**2/6 <= ratio <= 1)

    substitutions = {x: 0, y: 0, z: 0}
    check("k=0 constraints vanish and require separate global treatment",
          zero(constraints.subs(substitutions)))
    amplitude = sp.symbols("amplitude", real=True)
    zero_energy = ((amplitude*trace).T*kp*(amplitude*trace))[0]/2
    check("unmodified periodic global trace mode has H0=-3r^2/4",
          sp.simplify(zero_energy+3*amplitude**2/4) == 0)
    check("global block before removal is a nondegenerate 12D canonical block",
          symplectic.shape == (12, 12) and symplectic.rank() == 12)

    for dimension in (2, 3, 5):
        annihilator = sp.zeros(dimension)
        for level in range(1, dimension):
            annihilator[level-1, level] = sp.sqrt(level)
        q = (annihilator+annihilator.T)/sp.sqrt(2)
        p = (annihilator-annihilator.T)/(sp.I*sp.sqrt(2))
        top = sp.zeros(dimension)
        top[dimension-1, dimension-1] = 1
        defect = q*p-p*q-sp.I*sp.eye(dimension)
        check(f"finite CCR embedding fails exactly at d={dimension}",
              zero(defect+sp.I*dimension*top) and sp.trace(defect) == -sp.I*dimension)


def run() -> int:
    reset()
    print("v1029 -- local tensor constraints with mandatory global zero-mode removal")
    data = generic_and_axis_certificate()
    staggered_and_global_certificate(data)
    print("VERDICT: NONZERO_MOMENTUM_LOCAL_Z1_CONSTRAINT_QUOTIENT_PROVED; "
          "GLOBAL_ZERO_MODE_REMOVAL_REQUIRED; TFPT_PARENT_AND_T7_OPEN")
    return summary("v1029 local tensor constraints")


if __name__ == "__main__":
    raise SystemExit(run())
