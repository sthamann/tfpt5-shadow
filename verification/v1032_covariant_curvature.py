#!/usr/bin/env python3
"""Exact algebra for the free Lorentz-covariant curvature extension.

No TFPT-parent, interacting-gravity, T7-completion, TOE, or RH claim.
The distributional construction and its scope are proved in PROOF.tex.
Only SymPy is required. All checks below are exact, not floating scans.

Port provenance: native verification port of
`toe_round7_covariant_curvature/covariant_curvature_checker.py`
(source SHA-256 10eff5bab2ac8df6a532f5112503678e58233006d2fe93daa7e00271c6d9f210).
The port changes only harness integration and execution lifecycle.
"""
from __future__ import annotations

import json
import time

import sympy as s

from tfpt_constants import check as suite_check, reset, summary

ETA = s.diag(-1, 1, 1, 1)
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
CURV = tuple((a, b) for a in range(6) for b in range(a, 6))
SPATIAL = ((0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1))
CHECKS: list[str] = []
FAILED = 0


def check(label, condition):
    global FAILED
    passed = suite_check(label, bool(condition))
    CHECKS.append(label)
    FAILED += int(not passed)


def zero(value):
    values = list(value) if isinstance(value, s.MatrixBase) else [value]
    return all(s.expand(v) == 0 for v in values)


def symbasis(n, pairs):
    result = []
    for i, j in pairs:
        b = s.zeros(n)
        b[i, j] = b[j, i] = 1 if i == j else 1/s.sqrt(2)
        result.append(b)
    return result


HPAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))
HBASIS = symbasis(4, HPAIRS)
SBASIS = symbasis(3, SPATIAL)


def coordinates(h):
    return s.Matrix([s.trace(b.T*h) for b in HBASIS])


def riemann(k, h, mu, nu, rho, sigma):
    return (k[sigma]*k[nu]*h[mu, rho]
            + k[rho]*k[mu]*h[nu, sigma]
            - k[rho]*k[nu]*h[mu, sigma]
            - k[sigma]*k[mu]*h[nu, rho])/2


def curvature_map(k):
    return s.Matrix([[riemann(k, h, *PAIRS[a], *PAIRS[b])
                      for h in HBASIS] for a, b in CURV])


def covariant_numerator():
    # Pi_{mn,ab}=1/2(eta_ma eta_nb+eta_mb eta_na-eta_mn eta_ab).
    return s.Matrix.hstack(*(
        coordinates(ETA*h*ETA-ETA*s.trace(ETA*h)/2) for h in HBASIS))


def spatial_data(p):
    r2 = (p.T*p)[0]
    b = s.Matrix.hstack(*(h*p for h in SBASIS))
    tr = s.Matrix([1, 1, 1, 0, 0, 0])
    v = b.T*p
    kp = s.eye(6)-tr*tr.T/2
    kq = r2*(s.eye(6)-tr*tr.T)-2*b.T*b+tr*v.T+v*tr.T
    c = s.expand(kq*kp*kq)
    embedded = []
    for h in SBASIS:
        hh = s.zeros(4)
        hh[1:4, 1:4] = h
        embedded.append(coordinates(hh))
    return r2, c, s.Matrix.hstack(*embedded)


def on_cone_zero(matrix, omega, r2):
    modulus = s.Poly(omega**2-r2, omega)
    return all(s.Poly(s.expand(v), omega).rem(modulus).is_zero for v in matrix)


def curvature_tensor_action(lorentz):
    wedge = s.Matrix([
        [lorentz[mu, a]*lorentz[nu, b]-lorentz[mu, b]*lorentz[nu, a]
         for a, b in PAIRS] for mu, nu in PAIRS])
    columns = []
    for a, b in CURV:
        tensor = s.zeros(6)
        tensor[a, b] = tensor[b, a] = 1
        transformed = wedge*tensor*wedge.T
        columns.append(s.Matrix([transformed[i, j] for i, j in CURV]))
    return s.Matrix.hstack(*columns)


def universal_checks():
    omega, x, y, z = s.symbols('omega x y z', real=True)
    p = s.Matrix([x, y, z])
    k = s.Matrix([-omega, x, y, z])
    a = curvature_map(k)
    pi = covariant_numerator()
    r2, c, embed = spatial_data(p)
    kernel = s.expand(a*pi*a.T)
    check('covariant metric numerator is symmetric but indefinite',
          pi == pi.T and pi.det() != 0
          and pi.eigenvals() == {-1: 4, 1: 6})
    for j in range(4):
        xi = s.eye(4)[:, j]
        check(f'curvature annihilates arbitrary pure gauge column {j}',
              zero(a*coordinates(k*xi.T+xi*k.T)))
    check('kernel has homogeneous degree four and no momentum denominators',
          all(v == 0 or s.Poly(v, omega, x, y, z).is_homogeneous
              and s.Poly(v, omega, x, y, z).total_degree() == 4
              for v in kernel))
    defect = s.expand(a*(r2**2*pi-embed*c*embed.T)*a.T)
    check('all 441 null-cone entries: A Pi A^T equals A P_TT A^T',
          on_cone_zero(defect, omega, r2))
    check('must-fail: same identity is false away from the null cone',
          not zero(defect.subs({omega: 2, x: 0, y: 0, z: 1})))
    trace = coordinates(ETA)
    wrong = s.expand(a*(pi+trace*trace.T/2)*a.T-kernel)
    check('must-fail: omitting trace reversal changes the null curvature kernel',
          not zero(wrong.subs({omega: 1, x: 0, y: 0, z: 1})))

    # Algebraic and differential identities checked on each of 10 metric bases.
    check('Riemann antisymmetries and pair interchange for all metric columns',
          all(zero(riemann(k,h,m,n,r,t)+riemann(k,h,n,m,r,t))
              and zero(riemann(k,h,m,n,r,t)+riemann(k,h,m,n,t,r))
              and zero(riemann(k,h,m,n,r,t)-riemann(k,h,r,t,m,n))
              for h in HBASIS for m,n in PAIRS for r,t in PAIRS))
    check('algebraic Bianchi identity for all metric columns and tensor indices',
          all(zero(riemann(k,h,m,n,r,t)+riemann(k,h,m,r,t,n)
                   +riemann(k,h,m,t,n,r))
              for h in HBASIS for m in range(4) for n in range(4)
              for r in range(4) for t in range(4)))
    check('differential Bianchi identity for all curvature columns',
          all(zero(k[u]*riemann(k,h,m,n,r,t)
                   +k[r]*riemann(k,h,m,n,t,u)
                   +k[t]*riemann(k,h,m,n,u,r))
              for h in HBASIS for m,n in PAIRS for u in range(4)
              for r,t in PAIRS))
    ricci = s.Matrix([
        [sum(ETA[mu,mu]*riemann(k,h,mu,nu,mu,sigma)
             for mu in range(4)) for h in HBASIS]
        for nu in range(4) for sigma in range(4)])
    check('on-cone Ricci tensor annihilates the whole TT range',
          on_cone_zero(s.expand(ricci*embed*c), omega, r2))

    electric = s.Matrix([[riemann(k,h,0,i+1,0,j+1)
                          for h in HBASIS] for i,j in SPATIAL])
    normalization = s.diag(1,1,1,s.sqrt(2),s.sqrt(2),s.sqrt(2))
    electric = normalization*electric
    check('electric curvature R_0i0j is omega^2 q_ij/2 in radiation gauge',
          zero(electric*embed-omega**2*s.eye(6)/2))
    check('null electric covariance is exactly one quarter of Round 6 C',
          on_cone_zero(s.expand(electric*pi*electric.T-c/4), omega, r2))
    # W(x,y) has phase exp(-i omega (t_x-t_y)); differentiate y for <R dot R>.
    delay = s.symbols('delay', real=True)
    scalar_w = s.exp(-s.I*omega*delay)/(2*omega)
    check('second-argument Wightman derivative fixes positive mixed sign',
          s.simplify((-s.diff(scalar_w, delay)).subs(delay, 0)) == s.I/2)
    check('two Wightman time derivatives fix positive derivative covariance',
          s.simplify((-s.diff(scalar_w, delay, 2)).subs(delay, 0)) == omega/2)
    check('mixed electric-time covariance equals i C/8 on the cone',
          on_cone_zero(s.expand(s.I*electric*pi*electric.T/2-s.I*c/8), omega, r2))
    return pi


def fibre_and_covariance_checks(pi):
    for values in ((1,0,0,1),(3,1,2,2),(7,-2,3,6),(s.Rational(5,3),1,0,s.Rational(4,3))):
        w,x,y,z = values
        k = s.Matrix([-w,x,y,z])
        a = curvature_map(k)
        kernel = s.simplify(a*pi*a.T)
        r2,c,embed = spatial_data(s.Matrix([x,y,z]))
        ptt = c/r2**2
        factor = s.simplify(a*embed*ptt)
        check(f'exact positive factorization at null fibre {values}',
              zero(kernel-factor*factor.T))
        check(f'exact two physical curvature polarizations at fibre {values}',
              kernel.rank() == 2 and factor.rank() == 2)

    boost = s.eye(4)
    boost[0,0] = boost[1,1] = s.Rational(5,3)
    boost[0,1] = boost[1,0] = -s.Rational(4,3)
    k = s.Matrix([-3,1,2,2])
    action = curvature_tensor_action(boost)
    a = curvature_map(k)
    transformed_a = curvature_map(boost*k)
    check('rational boost preserves eta and future null energy',
          boost*ETA*boost.T == ETA and -(boost*k)[0] > 0
          and ((boost*k).T*ETA*(boost*k))[0] == 0)
    check('all 441 curvature kernel entries obey nontrivial boost covariance',
          zero(transformed_a*pi*transformed_a.T-action*a*pi*a.T*action.T))


def little_group_checks():
    k = s.Matrix([-1,0,0,1])
    a = curvature_map(k)
    plus = s.diag(0,1,-1,0)/s.sqrt(2)
    cross = s.zeros(4)
    cross[1,2] = cross[2,1] = 1/s.sqrt(2)
    u,v = s.symbols('u v', real=True)
    q = (u*u+v*v)/2
    null_rotation = s.Matrix([[1+q,-u,-v,q],[-u,1,0,-u],
                              [-v,0,1,-v],[-q,u,v,1-q]])
    check('all-parameter null rotations preserve eta and the reference momentum',
          zero(null_rotation*ETA*null_rotation.T-ETA)
          and zero(null_rotation*k-k))
    for name,h in (('plus',plus),('cross',cross)):
        check(f'null little-group translations act trivially on {name} curvature',
              zero(a*coordinates(null_rotation*h*null_rotation.T-h)))
    t = s.symbols('t', real=True)
    cosine, sine = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    rotation = s.eye(4)
    rotation[1:3,1:3] = s.Matrix([[cosine,-sine],[sine,cosine]])
    pol = s.Matrix.hstack(coordinates(plus),coordinates(cross))
    h_action = s.Matrix.hstack(coordinates(rotation*plus*rotation.T),
                               coordinates(rotation*cross*rotation.T))
    double = s.Matrix([[cosine*cosine-sine*sine,-2*cosine*sine],
                       [2*cosine*sine,cosine*cosine-sine*sine]])
    check('all-angle TT rotation has exactly spin-two double-angle action',
          all(s.cancel(v) == 0 for v in h_action-pol*double))
    for sign in (-1,1):
        vector = s.Matrix([1,sign*s.I])
        phase = (cosine-sign*s.I*sine)**2
        check(f'circular curvature polarization has helicity {2*sign:+d}',
              all(s.cancel(v) == 0 for v in double*vector-phase*vector))


def run() -> int:
    global FAILED
    reset()
    CHECKS.clear()
    FAILED = 0
    started = time.perf_counter()
    pi = universal_checks()
    fibre_and_covariance_checks(pi)
    little_group_checks()
    print(json.dumps({'status':'PASS' if FAILED == 0 else 'FAIL',
                      'exact_checks':len(CHECKS),
                      'elapsed_seconds':time.perf_counter()-started,
                      'claim':'free covariant curvature extension only',
                      'checks':CHECKS}, indent=2))
    return summary("v1032 covariant curvature")


if __name__ == '__main__':
    raise SystemExit(run())
