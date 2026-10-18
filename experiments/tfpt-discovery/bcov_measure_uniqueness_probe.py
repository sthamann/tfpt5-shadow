#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bcov_measure_uniqueness_probe -- SEAM.TWISTOR.MEASURE_RIGIDITY.01:
strategy S5 -- upgrade "DECLARED twisted BCOV/KS measure" to "unique
solution of the EXECUTED constraints" on the computable twistor
sector: parametrise an honest deformation family of the measure data
and cut it with the already-executed constraint gates; count the
surviving deformation dimensions.  Exact rational linear algebra
throughout (sympy / Fraction, no floats, no RNG, deterministic).

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  v516/v518 leave the BCOV measure question as
the named [O]: the DECLARED completion reading delivers the psi = 64
slice and cancels 32 T3, the DERIVED chiral measure fails all three
testers (v518, the negative anchor of this round).  Before any new
derivation, S5 asks the cheaper RIGIDITY question: how much freedom
do the constraints ALREADY EXECUTED in the suite leave for the
measure data on the finite computable sector?  Joint kernel 0 would
upgrade "declared" to "unique-on-sector"; a nonzero kernel names the
surviving directions exactly.

THE COMPUTABLE SECTOR (what "measure" concretely means here -- the
finite shadow the cited modules actually compute):
  (a) v508: the 5-dim W(D5) x W(A3)-invariant quartic space
      (P1, P2, P3, T5, T3); the per-class quartic power sums Q_m
      (m = 0..3, with Q_1 = Q_3 exactly); the contact vector
      A = kappa sum_m v_m Q_m with declared weights
      v* = (5/4, -1/4, -3/4, -1/4) (= the AB weights
      w = (0, 1/2, 1/4, 1/2) Fourier-transformed to class space);
      A(declared) = A_fix = (9, -30, -15, 0, 32), certificate
      (Phi_T5, Phi_T3, Phi_P) = (0, 32, 72).
  (b) v515: the seam-fibre period vector Pi_j(0) = 2 pi i t0 (i-1)
      (1, i, i^2) of the centre orbit z_p = i^p t0; the clock
      covariance Pi_{j+1}(-i la) = i Pi_j(la) for ALL la; the
      linking charges N_p = (1, 1, 1, 1) in Omega_N = Omega_0 +
      sum_p N_p K_p with every period in (2 pi i)^2 Z; the
      residue-form cover charge 4 = |mu4| (omega2 = c dX^dZ/X,
      pullback 4c dz1^dz2).
  (c) v518 (the negative anchor): the delta-1 route is DEAD under
      the derived measure; "compatibility with the kill" = the
      deformed contact vector must stay on the executed certificate
      level set (driving Phi_T3 -> 0 / Phi_P -> 0 would make A_fix
      exchange-reachable = resurrect the killed normalisation).

THE DEFORMATION FAMILY (18 real rational parameters at the declared
point; honest = it deforms exactly the data entering the
period/pairing computations, same support, same grading):
  dk          overall normalisation kappa of the contact functional
  dv_m        the four sector weights v_m (m = 0..3)
  dc          the residue-form normalisation c (omega2 = c dX^dZ/X)
  dn_p        the four linking charges N_p
  da_p, db_p  the four centre positions z_p = i^p (1 + da_p + i db_p)
GAUGE (reparametrisations verified to act trivially on EVERY
constraint output by FINITE substitution, not just linearised):
  g1 the (kappa, v) rescaling kappa -> t kappa, v -> v/t;
  g2 the common centre phase (coordinate rotation Z -> s Z, |s| = 1);
  g3 the common centre scale (the t0 / coordinate rescaling --
     trivial on the dimensionless / quantised executed outputs);
  g4 the conjugate-sector transfer v_1 <-> v_3 (Q_1 = Q_3 EXACTLY on
     this sector, so the transfer is invisible here; on a finer
     sector -- the full tensor ledger -- it would be physical; typed
     honestly as gauge-ON-SECTOR).
dim(param) = 18, dim(gauge) = 4, dim(moduli) = 14.

CONSTRAINT TRANSCRIPTION (typed; each leg = an executed gate):
  C1 CLOCK INVARIANCE, order 4 (v492 S5 / v515 S2.3, TRANSCRIBED):
     the clock permutes the centre lines L_p -> L_{p+1} and centres
     i z_p = z_{p+1}; invariance rows dz_{p+1} = dz_p (exact linear
     residual, not a linearisation) and n_{p+1} = n_p.
  C2 LOCKSTEP / PERIOD STRUCTURE (v515 S3.2/S3.3/S4, TRANSCRIBED;
     the integrality leg is the tangent condition of a DISCRETE
     executed constraint: the only continuous deformation of a
     (2 pi i)^2 Z-valued period is zero): rows dn_p = 0; the clock
     covariance of Pi_j(la) at all powers of la; lockstep modulus
     equality |Pi_j| = |Pi_0| (expected to add rank 0 beyond the
     covariance rows on this family -- printed either way).
  C3 FORCED SOURCE CHARGE 4 = |mu4| (v515 S1.2/S4.3, TRANSCRIBED):
     cover-pullback charge 4c = 4 (row dc = 0) and lens total
     charge sum_p N_p = 4 (row sum dn = 0).
  C4 NULL-IDEAL / NO-RESURRECTION (v508 S3.2 + v518, TRANSCRIBED):
     the deformed contact vector stays on the executed certificate
     level set Phi_T5(A) = 0, Phi_T3(A) = 32, Phi_P(A) = 72; the
     psi functional is DEPENDENT (psi = Phi_P - Phi_T3/4, shown
     exactly), so psi(A) = 64 is implied.
     NOT-TRANSCRIBABLE on this sector: the W_2 : W_13 = 4 : 3
     Harvey-Moore tester (it needs the modular-integral kernel
     weights J(Delta, s), which have no finite exact shadow in this
     probe) -- typed, not faked.

PRE-REGISTERED ADJUDICATION (frozen before the record run):
  P1 anchors, one headline number per module, re-derived exactly:
     v508: A_fix = (9, -30, -15, 0, 32) + certificate (0, 32, 72)
     from the 240 glue roots; v515: the closed twistor family +
     lockstep vector 2 pi i t0 (i-1)(1, i, i^2) + lens forcing
     N = 0 mod 4; v518: psi(A_fix) = 64 + the Q_1 = Q_3 ledger.
  P2 the deformation space is built: dims 18 / 4 / 14 printed;
     every gauge direction verified trivial by FINITE substitution
     and contained in every constraint kernel.
  P3-P6 constraint Jacobians exact, per-constraint ranks printed
     (expected C1 = 9, C2 = 8, C3 = 2, C4 = 2 with the exact
     dependency Phi_P = 3 Phi_T5 + (9/4) Phi_T3 on the deformation
     image; note the executed triple satisfies the same relation:
     72 = 3*0 + (9/4)*32); joint rank 13, joint kernel 5, gauge
     inside the kernel, moduli kernel = 1.
  P7 verdict gate: joint moduli kernel 1 => RESIDUAL_FREEDOM(1);
     the surviving direction identified EXACTLY as the uniform
     weight shift dv = (1, 1, 1, 1): dA = sum_m Q_m =
     36 (1, 2, 1, 0, 0) = the UNTWISTED Okubo square Q^{(0)} -- the
     direction every executed certificate functional annihilates BY
     CONSTRUCTION (v508 S3.4: Phi_P(Q^{(0)}) = 0, T5 = T3 = 0);
     second-order check: the direction is EXACTLY flat (all
     constraint outputs constant to all orders along it, finite
     rational-epsilon substitution).
  P8 negative controls: a clock-violating deformation (dz_0 only)
     must show a nonzero C1 residual (CAUGHT); the centre
     TRANSLATION mode dz_p = (-i)^p must be caught by C1 while
     invisible to EVERY C2 period row (the v515 "forced twice over"
     structure made visible); every gauge direction must lie in
     every per-constraint kernel (sanity).
  P9 ablation ledger (leave-one-out moduli kernels): expected
     (full, -C1, -C2, -C3, -C4, -C1&C2) = (1, 3, 1, 2, 3, 10):
     C1 / C3 / C4 load-bearing; C2 redundant ON THE TANGENT given
     C1 + C3 (the executed double-forcing of the flux vector,
     v515 S4.4 "forced uniform twice over").
  Plus 2 must-fail mutants: MUT1 corrupted AB weight (sector-2
     denominator 4 -> 2) must break the anchor + certificate; MUT2
     clock-phase mutant covariance (phase 1 instead of i) must be
     rejected by the DECLARED point already at zeroth order.

VERDICT ENUM: UNIQUE_ON_SECTOR / RESIDUAL_FREEDOM(dim) /
SECTOR_TOO_THIN (fewer than 3 independent constraints transcribe).
EXPECTED VERDICT (pre-registered): RESIDUAL_FREEDOM(1), the one flat
direction = the untwisted (bulk) admixture; equivalently: the
TWISTED-relative measure data (all sector-weight directions
transverse to the bulk slot, the charge vector, the centre orbit,
the residue normalisation) are UNIQUE on the sector, and the single
unfixed coordinate is exactly the sector-0 slot that the v505/v508
certificates annihilate by construction.

FENCES.  Exploration only; the "computable sector" is the finite
shadow named above -- this is NOT a BCOV derivation and does not
touch the v516-vs-v518 measure decision; C4 pins level sets of
EXECUTED functionals, not the full contact vector; the W-ratio
tester is typed NOT-TRANSCRIBABLE; g3 / g4 are gauge ON THIS SECTOR
only.  SEAM.EQUIV.TWISTOR.01 and the BCOV measure question stay [O]
exactly as before; NO marker moves anywhere.
"""
import hashlib
import time
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

T_START = time.perf_counter()
HALF = F(1, 2)
I = sp.I
R = sp.Rational

GATES = []


def gate(desc, ok):
    GATES.append(bool(ok))
    print("  [G%02d %s] %s" % (len(GATES), "PASS" if ok else "FAIL", desc))
    return bool(ok)


def fmt(xs):
    return "(" + ", ".join(str(x) for x in xs) + ")"


# ---------------------------------------------------------------------------
# E8 roots in D5 (+) A3 glue coordinates (v128/v492/v508/v518 construction)
# ---------------------------------------------------------------------------
def build_glue_roots():
    d5_roots, d5_v = [], []
    for i, j in combinations(range(5), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [F(0)] * 5
                v[i], v[j] = F(si), F(sj)
                d5_roots.append(tuple(v))
    for i in range(5):
        for s in (1, -1):
            v = [F(0)] * 5
            v[i] = F(s)
            d5_v.append(tuple(v))
    d5_s, d5_c = [], []
    for signs in product((1, -1), repeat=5):
        v = tuple(HALF * s for s in signs)
        (d5_s if signs.count(-1) % 2 == 0 else d5_c).append(v)
    a3_roots = []
    for i in range(4):
        for j in range(4):
            if i != j:
                v = [F(0)] * 4
                v[i], v[j] = F(1), F(-1)
                a3_roots.append(tuple(v))

    def wclass(k):
        out = []
        for sub in combinations(range(4), k):
            v = [F(-k, 4)] * 4
            for i in sub:
                v[i] += 1
            out.append(tuple(v))
        return out

    z5, z4 = tuple([F(0)] * 5), tuple([F(0)] * 4)
    roots = {}
    for r in d5_roots:
        roots[r + z4] = 0
    for r in a3_roots:
        roots[z5 + r] = 0
    for d in d5_s:
        for w in wclass(1):
            roots[d + w] = 1
    for d in d5_v:
        for w in wclass(2):
            roots[d + w] = 2
    for d in d5_c:
        for w in wclass(3):
            roots[d + w] = 3
    return roots


# ---------------------------------------------------------------------------
# exact quartic ledger Q_m via the 6-sample-point solve (v518 machinery)
# ---------------------------------------------------------------------------
SAMPLES = [
    (1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 1, 1, 1),
    (1, 2, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 1, 0, 0),
    (1, 1, 1, 0, 0, 1, 1, 1),
]


def basis_at(pt):
    xs, ys = pt[:5], list(pt[5:])
    ys4 = ys + [-sum(ys)]
    S5 = sum(x * x for x in xs)
    S3 = sum(y * y for y in ys4)
    T5 = sum(x ** 4 for x in xs)
    T3 = sum(y ** 4 for y in ys4)
    return (S5 * S5, S5 * S3, S3 * S3, T5, T3)


BMAT = [basis_at(p) for p in SAMPLES]


def pair_at(alpha, s):
    d = sum(a * F(x) for a, x in zip(alpha[:5], s[:5]))
    y4 = (F(s[5]), F(s[6]), F(s[7]), F(-(s[5] + s[6] + s[7])))
    d += sum(a * y for a, y in zip(alpha[5:], y4))
    return d


def solve5(bvals):
    """exact coefficients in (P1, P2, P3, T5, T3) from 6 sample values."""
    A = sp.Matrix([[BMAT[k][i] for i in range(5)] for k in range(6)])
    b = sp.Matrix([R(x.numerator, x.denominator) for x in bvals])
    sol, params = A.gauss_jordan_solve(b)
    assert len(params) == 0 and A * sol == b, "sample solve inconsistent"
    return [R(x) for x in sol]


def dot(f, v):
    return sum(R(a) * R(b) for a, b in zip(f, v))


PHI_T5 = [0, 0, 0, 1, 0]
PHI_T3 = [0, 0, 0, 0, 1]
PHI_P = [3, -1, -1, 0, 0]
PSI = [3, -1, -1, 0, R(-1, 4)]

# declared class-space weights v* (= AB weights (0, 1/2, 1/4, 1/2) after
# the mu4 Fourier transform to class space, v518 S0.3)
VSTAR = [R(5, 4), R(-1, 4), R(-3, 4), R(-1, 4)]

CERT_TARGET = [0, 32, 72, 64]        # (Phi_T5, Phi_T3, Phi_P, psi)


# ---------------------------------------------------------------------------
# S0 -- P1 anchors (v508 / v515 / v518 headline numbers, re-derived)
# ---------------------------------------------------------------------------
def section0():
    print("  -- S0: P1 anchors -- headline numbers of v508/v515/v518, "
          "re-derived exactly")
    roots = build_glue_roots()
    counts = [sum(1 for c in roots.values() if c == m) for m in range(4)]
    norm_ok = all(sum(x * x for x in r) == 2 for r in roots)
    gate("ANCHOR v508a: 240 glue roots, all norm 2, class split %s = "
         "(52, 64, 60, 64)" % fmt(counts),
         len(roots) == 240 and norm_ok and counts == [52, 64, 60, 64])

    # quartic ledger Q_m (exact, sample solve)
    Q5 = {}
    for m in range(4):
        bvals = []
        for s in SAMPLES:
            acc = F(0)
            for alpha, c in roots.items():
                if c == m:
                    acc += pair_at(alpha, s) ** 4
            bvals.append(acc)
        Q5[m] = solve5(bvals)
    QTAB = {0: [12, 0, 6, 4, 8], 1: [12, 24, 0, -8, 16],
            2: [0, 24, 30, 12, -40], 3: [12, 24, 0, -8, 16]}
    for m in range(4):
        print("     Q_%d = %s" % (m, fmt(Q5[m])))

    # quadratic ledger parallelism K^{(0)} = -15 K^{(2)} via exact Grams
    G = {m: [[F(0)] * 9 for _ in range(9)] for m in range(4)}
    for alpha, c in roots.items():
        for i in range(9):
            if alpha[i] == 0:
                continue
            for j in range(9):
                G[c][i][j] += alpha[i] * alpha[j]
    combo_zero = all(
        16 * G[0][i][j] - 14 * G[1][i][j]
        + 16 * G[2][i][j] - 14 * G[3][i][j] == 0
        for i in range(9) for j in range(9))
    gate("ANCHOR v508b: quartic ledger Q_m matches the v518 table "
         "exactly AND K^{(0)} + 15 K^{(2)} = 0 as exact Gram matrices "
         "(16 K_0 - 14 K_1 + 16 K_2 - 14 K_3 = 0, the v508 S0.2 "
         "parallelism)",
         all(Q5[m] == QTAB[m] for m in range(4)) and combo_zero)

    Afix = [dot([VSTAR[m] for m in range(4)],
                [Q5[m][i] for m in range(4)]) for i in range(5)]
    cert = [dot(PHI_T5, Afix), dot(PHI_T3, Afix), dot(PHI_P, Afix)]
    print("     A_fix = %s, certificate (Phi_T5, Phi_T3, Phi_P) = %s"
          % (fmt(Afix), fmt(cert)))
    gate("ANCHOR v508c: A_fix = sum_m v*_m Q_m = (9, -30, -15, 0, 32) "
         "with certificate (0, 32, 72) (v508 S0.3/S3.2 replicated)",
         Afix == [9, -30, -15, 0, 32] and cert == [0, 32, 72])

    # v515 anchors: closed family, lockstep periods, lens forcing
    lam, Zs = sp.symbols('lam Zserf')
    t0 = sp.Symbol('t0', positive=True)
    Qs = [sp.expand(I ** p * t0 - I ** (-p) * t0 * lam ** 2)
          for p in range(4)]
    P4 = sp.expand(sp.prod([Zs - q for q in Qs]))
    ok_fam = (P4.coeff(Zs, 3) == 0 and P4.coeff(Zs, 1) == 0
              and sp.expand(P4.coeff(Zs, 2) - 4 * t0 ** 2 * lam ** 2) == 0
              and sp.expand(P4.coeff(Zs, 0)
                            + t0 ** 4 * (1 - lam ** 4) ** 2) == 0
              and sp.expand(P4.subs(lam, 0) - (Zs ** 4 - t0 ** 4)) == 0)
    gate("ANCHOR v515a: the twistor family closes exactly -- "
         "prod(Z - q_p) = Z^4 + 4 t0^2 la^2 Z^2 - t0^4 (1 - la^4)^2, "
         "seam fibre Z^4 - t0^4 (v515 S2.2 replicated)", ok_fam)

    def Pi(j, la):
        return sp.expand(2 * sp.pi * I
                         * (Qs[(j + 1) % 4] - Qs[j]).subs(lam, la))

    Pi0 = [Pi(j, 0) for j in range(3)]
    tgt = [sp.expand(2 * sp.pi * I * t0 * (I - 1) * I ** j)
           for j in range(3)]
    mods_ok = all(sp.simplify(sp.Abs(p) - 2 * sp.sqrt(2) * sp.pi * t0) == 0
                  for p in Pi0)
    ratios = [sp.simplify(Pi0[j] / Pi0[0]) for j in range(3)]
    cov = [sp.expand(Pi((j + 1) % 4, -I * lam) - I * Pi(j, lam))
           for j in range(4)]
    quant = [n for n in (1, 2, 3, 4, 8) if R(n, 4).is_integer]
    gate("ANCHOR v515b: seam period vector 2 pi i t0 (i-1)(1, i, i^2), "
         "moduli all 2 sqrt(2) pi t0 (lockstep), clock covariance "
         "Pi_{j+1}(-i la) = i Pi_j(la) for ALL la, lens quantisation "
         "passes only N = 0 mod 4 (source charge 4 = |mu4| forced): "
         "quant survivors %s" % fmt(quant),
         all(sp.expand(Pi0[j] - tgt[j]) == 0 for j in range(3))
         and mods_ok and ratios == [1, I, sp.expand(I ** 2)]
         and all(c == 0 for c in cov) and quant == [4, 8])

    psiA = dot(PSI, Afix)
    dep = [R(PSI[i]) - (R(PHI_P[i]) - R(PHI_T3[i], 4) * 1)
           for i in range(5)]
    gate("ANCHOR v518: psi(A_fix) = %s = 64, psi = Phi_P - Phi_T3/4 "
         "identically (dependency %s), and Q_1 = Q_3 exactly (the "
         "conjugate sectors are IDENTICAL on this sector -- the g4 "
         "gauge slot)" % (psiA, fmt(dep)),
         psiA == 64 and all(d == 0 for d in dep) and Q5[1] == Q5[3])
    return Q5, Afix


# ---------------------------------------------------------------------------
# the deformation family: 18 real parameters
# ---------------------------------------------------------------------------
dk = sp.Symbol('dk', real=True)
dv = sp.symbols('dv0:4', real=True)
dc = sp.Symbol('dc', real=True)
dn = sp.symbols('dn0:4', real=True)
da = sp.symbols('da0:4', real=True)
db = sp.symbols('db0:4', real=True)
SYMS = [dk, dv[0], dv[1], dv[2], dv[3], dc,
        dn[0], dn[1], dn[2], dn[3],
        da[0], db[0], da[1], db[1], da[2], db[2], da[3], db[3]]
NP = len(SYMS)
ZERO = {s: 0 for s in SYMS}

Zc = [sp.expand(I ** p * (1 + da[p] + I * db[p])) for p in range(4)]
Zb = [sp.expand((-I) ** p * (1 + da[p] - I * db[p])) for p in range(4)]
LAM = sp.Symbol('lamdef')


def q_def(p, la):
    return Zc[p] - Zb[p] * la ** 2


def Pi_def(j, la):
    return sp.expand(q_def((j + 1) % 4, la) - q_def(j, la))


def lin_rows(residuals, tag):
    """exact linear rows over SYMS; asserts zero constant term; splits
    complex residuals into re/im rows; drops zero rows."""
    rows = []
    for r_expr in residuals:
        r_expr = sp.expand(r_expr)
        c0 = sp.simplify(r_expr.subs(ZERO))
        assert c0 == 0, "%s: nonzero constant term %s" % (tag, c0)
        coefs = [sp.expand(sp.diff(r_expr, s).subs(ZERO)) for s in SYMS]
        for part in (sp.re, sp.im):
            row = [sp.nsimplify(part(c)) for c in coefs]
            if any(x != 0 for x in row):
                rows.append(row)
    return rows


def build_constraints(Q5, Afix):
    """the four executed constraints as exact row systems."""
    # C1 -- clock invariance (order 4): i z_p = z_{p+1}, n_p = n_{p+1}
    c1_res = [I * Zc[p] - Zc[(p + 1) % 4] for p in range(4)]
    c1_res += [(1 + dn[p]) - (1 + dn[(p + 1) % 4]) for p in range(4)]
    rows_c1 = lin_rows(c1_res, "C1")

    # C2 -- lockstep / period structure
    c2_res = [dn[p] for p in range(4)]              # integrality tangent
    for j in range(4):                              # clock covariance
        Rj = sp.expand(Pi_def((j + 1) % 4, -I * LAM) - I * Pi_def(j, LAM))
        for k in (0, 1, 2):
            c2_res.append(Rj.coeff(LAM, k))
    for j in (1, 2, 3):                             # lockstep moduli
        mj = sp.expand((Zc[(j + 1) % 4] - Zc[j]) * (Zb[(j + 1) % 4] - Zb[j]))
        m0 = sp.expand((Zc[1] - Zc[0]) * (Zb[1] - Zb[0]))
        c2_res.append(mj - m0)
    rows_c2 = lin_rows(c2_res, "C2")

    # C3 -- forced source charge 4 = |mu4|
    c3_res = [4 * (1 + dc) - 4,
              sum(1 + dn[p] for p in range(4)) - 4]
    rows_c3 = lin_rows(c3_res, "C3")

    # C4 -- certificate level set of the contact vector
    kt = 1 + dk
    vt = [VSTAR[m] + dv[m] for m in range(4)]
    Adef = [sp.expand(kt * sum(vt[m] * Q5[m][i] for m in range(4)))
            for i in range(5)]
    c4_res = [sum(R(f[i]) * Adef[i] for i in range(5)) - t
              for f, t in zip((PHI_T5, PHI_T3, PHI_P, PSI), CERT_TARGET)]
    rows_c4 = lin_rows(c4_res, "C4")
    return rows_c1, rows_c2, rows_c3, rows_c4


def mat(rows):
    return sp.Matrix(rows) if rows else sp.zeros(0, NP)


def vec(entries):
    v = [R(0)] * NP
    for k, val in entries.items():
        v[SYMS.index(k)] = R(val)
    return sp.Matrix(NP, 1, v)


def in_kernel(M, v):
    return M.rows == 0 or all(x == 0 for x in M * v)


# ---------------------------------------------------------------------------
def main():
    print("bcov_measure_uniqueness_probe  SEAM.TWISTOR.MEASURE_RIGIDITY.01"
          " -- is the declared twisted BCOV/KS measure the unique solution"
          " of the executed constraints on the computable sector?")
    print("EXPLORATION ONLY (2026-08-27): no promotion, no ledger row, "
          "no marker moved, no gate closed or narrowed.")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()[:16]
    print("SPEC_SHA = %s" % spec_sha)

    Q5, Afix = section0()

    # -----------------------------------------------------------------
    print("  -- S1: the deformation family and its gauge group")
    rows_c1, rows_c2, rows_c3, rows_c4 = build_constraints(Q5, Afix)
    M1, M2, M3, M4 = mat(rows_c1), mat(rows_c2), mat(rows_c3), mat(rows_c4)
    ALL_M = {'C1': M1, 'C2': M2, 'C3': M3, 'C4': M4}
    gate("P2a DEFORMATION SPACE BUILT: dim(param) = %d (dk 1 + dv 4 + "
         "dc 1 + dn 4 + dz 8); every constraint residual vanishes at "
         "the declared point (zeroth order checked inside row "
         "construction); row counts (C1, C2, C3, C4) = (%d, %d, %d, %d)"
         % (NP, M1.rows, M2.rows, M3.rows, M4.rows),
         NP == 18 and min(M.rows for M in ALL_M.values()) >= 1)

    # gauge directions
    g1 = vec({dk: 1, dv[0]: -VSTAR[0], dv[1]: -VSTAR[1],
              dv[2]: -VSTAR[2], dv[3]: -VSTAR[3]})
    g2 = vec({db[0]: 1, db[1]: 1, db[2]: 1, db[3]: 1})
    g3 = vec({da[0]: 1, da[1]: 1, da[2]: 1, da[3]: 1})
    g4 = vec({dv[1]: 1, dv[3]: -1})
    GAUGE = [g1, g2, g3, g4]
    gauge_rank = sp.Matrix.hstack(*GAUGE).rank()

    # finite (not linearised) triviality checks
    t = R(1, 3)
    A_g1 = [(1 + t) * sum((VSTAR[m] / (1 + t)) * R(Q5[m][i])
                          for m in range(4)) for i in range(5)]
    ok_g1 = [sp.nsimplify(x) for x in A_g1] == [R(a) for a in Afix]
    ok_g4 = all(R(Q5[1][i]) - R(Q5[3][i]) == 0 for i in range(5))

    def finite_orbit_ok(s):
        sb = sp.conjugate(s)
        zn = [sp.expand(s * I ** p) for p in range(4)]
        zbn = [sp.expand(sb * (-I) ** p) for p in range(4)]
        ok = all(sp.expand(I * zn[p] - zn[(p + 1) % 4]) == 0
                 for p in range(4))
        qf = lambda p, la: zn[p] - zbn[p] * la ** 2
        Pf = lambda j, la: qf((j + 1) % 4, la) - qf(j, la)
        ok = ok and all(sp.expand(Pf((j + 1) % 4, -I * LAM)
                                  - I * Pf(j, LAM)) == 0 for j in range(4))
        m0 = sp.expand((zn[1] - zn[0]) * (zbn[1] - zbn[0]))
        ok = ok and all(sp.expand((zn[(j + 1) % 4] - zn[j])
                                  * (zbn[(j + 1) % 4] - zbn[j]) - m0) == 0
                        for j in (1, 2, 3))
        return ok

    ok_g2 = finite_orbit_ok(R(3, 5) + R(4, 5) * I)   # |s| = 1 exactly
    ok_g3 = finite_orbit_ok(R(3, 2))                 # common scale
    ok_ker = all(in_kernel(M, g) for M in ALL_M.values() for g in GAUGE)
    gate("P2b GAUGE: 4 directions -- g1 (kappa, v)-rescale (finite check "
         "A unchanged at t = 1/3: %s), g2 common phase s = 3/5 + 4i/5 "
         "(%s), g3 common scale s = 3/2 (%s), g4 conjugate-sector "
         "transfer (Q_1 = Q_3: %s); gauge rank %d = 4; dim(moduli) = "
         "18 - 4 = 14; every gauge direction lies in every constraint "
         "kernel (%s)"
         % (ok_g1, ok_g2, ok_g3, ok_g4, gauge_rank, ok_ker),
         ok_g1 and ok_g2 and ok_g3 and ok_g4 and gauge_rank == 4
         and ok_ker)

    # -----------------------------------------------------------------
    print("  -- S2: per-constraint Jacobians (exact ranks)")
    r1, r2, r3, r4 = M1.rank(), M2.rank(), M3.rank(), M4.rank()
    gate("P3 C1 CLOCK Jacobian: TRANSCRIBED (exact residuals "
         "i z_p - z_{p+1} and n_p - n_{p+1}); rank %d = 9 "
         "(3 charge differences + 6 real centre differences)" % r1,
         r1 == 9)

    # is the lockstep-moduli block redundant beyond the covariance rows?
    rows_c2_cov = lin_rows(
        [sp.expand(Pi_def((j + 1) % 4, -I * LAM)
                   - I * Pi_def(j, LAM)).coeff(LAM, k)
         for j in range(4) for k in (0, 1, 2)], "C2cov")
    r2_cov = mat(rows_c2_cov).rank()
    lockstep_extra = r2 - 4 - r2_cov     # 4 = integrality rows dn_p
    gate("P4 C2 LOCKSTEP/PERIODS Jacobian: TRANSCRIBED (integrality "
         "typed as the tangent condition of the discrete (2 pi i)^2 Z "
         "constraint); rank %d = 8 = 4 (integrality) + %d (covariance, "
         "all la powers) + %d (lockstep-moduli EXTRA rank beyond "
         "covariance = 0 on this family: the family moves the orbit "
         "rigidly, centre-splitting is already killed)"
         % (r2, r2_cov, lockstep_extra),
         r2 == 8 and r2_cov == 4 and lockstep_extra == 0)

    gate("P5 C3 SOURCE-CHARGE Jacobian: TRANSCRIBED (cover charge "
         "4c = 4, lens total sum N_p = 4); rank %d = 2; the sum-row "
         "overlaps C2's integrality block (redundancy quantified in "
         "the P9 ablation)" % r3, r3 == 2)

    # C4 dependency: Phi_P = 3 Phi_T5 + (9/4) Phi_T3 on the image
    rowT5, rowT3, rowP = (sp.Matrix([rows_c4[k]]) for k in (0, 1, 2))
    dep_ok = all(x == 0 for x in (rowP - 3 * rowT5 - R(9, 4) * rowT3))
    dep_cert = (72 == 3 * 0 + R(9, 4) * 32)
    gate("P6a C4 NULL-IDEAL Jacobian: TRANSCRIBED (certificate level "
         "set Phi_T5 = 0, Phi_T3 = 32, Phi_P = 72; psi = 64 dependent); "
         "rank %d = 2 with the EXACT dependency Phi_P = 3 Phi_T5 + "
         "(9/4) Phi_T3 on the deformation image (%s) -- and the "
         "executed triple satisfies the same relation 72 = (9/4)*32 "
         "(%s); the W_2 : W_13 = 4 : 3 Harvey-Moore tester is "
         "NOT-TRANSCRIBABLE on this sector (needs the modular-integral "
         "kernel weights J(Delta, s); no finite exact shadow) -- typed, "
         "not faked" % (r4, dep_ok, dep_cert),
         r4 == 2 and dep_ok and dep_cert)

    # -----------------------------------------------------------------
    print("  -- S3: joint kernel and the surviving direction")
    Mall = sp.Matrix.vstack(M1, M2, M3, M4)
    rall = Mall.rank()
    null = Mall.nullspace()
    kdim = len(null)
    ok_gauge_in = all(in_kernel(Mall, g) for g in GAUGE)
    kmod = kdim - 4
    gate("P6b JOINT KERNEL: stacked Jacobian %d x 18, joint rank %d = "
         "13, kernel dim %d = 5, gauge (4) inside the kernel (%s) => "
         "moduli kernel dim = %d" % (Mall.rows, rall, kdim,
                                     ok_gauge_in, kmod),
         rall == 13 and kdim == 5 and ok_gauge_in and kmod == 1)

    # identify the surviving direction: uniform weight shift dv = 1
    u = vec({dv[0]: 1, dv[1]: 1, dv[2]: 1, dv[3]: 1})
    ok_u_ker = in_kernel(Mall, u)
    span_gu = sp.Matrix.hstack(*(GAUGE + [u]))
    ok_u_indep = span_gu.rank() == 5
    ok_span = all(sp.Matrix.hstack(span_gu, nv).rank() == 5 for nv in null)
    dA_u = [sum(R(Q5[m][i]) for m in range(4)) for i in range(5)]
    okubo = dA_u == [36, 72, 36, 0, 0]
    phis_u = [dot(f, dA_u) for f in (PHI_T5, PHI_T3, PHI_P, PSI)]
    # exact flatness to all orders: finite rational epsilon
    eps = R(1, 7)
    v_eps = [VSTAR[m] + eps for m in range(4)]
    A_eps = [sum(v_eps[m] * R(Q5[m][i]) for m in range(4))
             for i in range(5)]
    cert_eps = [dot(f, A_eps) for f in (PHI_T5, PHI_T3, PHI_P, PSI)]
    moved = [A_eps[i] - R(Afix[i]) for i in range(5)]
    flat_ok = (cert_eps == CERT_TARGET
               and moved == [36 * eps, 72 * eps, 36 * eps, 0, 0])
    gate("P7a SURVIVING DIRECTION IDENTIFIED: the joint kernel = "
         "span(gauge + uniform weight shift dv = (1,1,1,1)) (in kernel "
         "%s, independent of gauge %s, spans the nullspace %s); its "
         "image dA = sum_m Q_m = %s = 36 (1, 2, 1, 0, 0) = the "
         "UNTWISTED Okubo square Q^{(0)}; every executed functional "
         "annihilates it: (Phi_T5, Phi_T3, Phi_P, psi)(dA) = %s "
         "(v508 S3.4 replicated as the mechanism); EXACT FLATNESS: at "
         "finite eps = 1/7 the certificate stays (0, 32, 72, 64) while "
         "A moves by %s != 0 -- flat to ALL orders, second order kills "
         "nothing"
         % (ok_u_ker, ok_u_indep, ok_span, fmt(dA_u), fmt(phis_u),
            fmt(moved)),
         ok_u_ker and ok_u_indep and ok_span and okubo
         and phis_u == [0, 0, 0, 0] and flat_ok)

    n_indep = sum(1 for M in ALL_M.values() if M.rank() >= 1)
    if n_indep < 3:
        verdict = "SECTOR_TOO_THIN"
    elif kmod == 0:
        verdict = "UNIQUE_ON_SECTOR"
    else:
        verdict = "RESIDUAL_FREEDOM(%d)" % kmod
    gate("P7b VERDICT GATE: %d >= 3 independent constraints transcribe "
         "(not SECTOR_TOO_THIN); joint moduli kernel = %d => verdict "
         "%s -- the TWISTED-relative measure data (weight directions "
         "transverse to the bulk slot, charge vector, centre orbit, "
         "residue normalisation) are UNIQUE on the sector; the single "
         "flat direction is the sector-0 (bulk Okubo) admixture, "
         "exactly the slot the executed certificates annihilate by "
         "construction" % (n_indep, kmod, verdict),
         n_indep == 4 and verdict == "RESIDUAL_FREEDOM(1)")

    # -----------------------------------------------------------------
    print("  -- S4: negative controls")
    bad_clock = vec({da[0]: 1})
    res_c1 = M1 * bad_clock
    caught_clock = any(x != 0 for x in res_c1)
    bad_charge = vec({dn[0]: 1})
    caught_n = (any(x != 0 for x in M1 * bad_charge)
                and any(x != 0 for x in M2 * bad_charge))
    # translation mode dz_p = (-i)^p: caught by C1, invisible to C2
    trans = vec({da[0]: 1, db[1]: -1, da[2]: -1, db[3]: 1})
    caught_trans = any(x != 0 for x in M1 * trans)
    blind_trans = in_kernel(M2, trans)
    gate("P8a NEGATIVE CONTROLS CAUGHT: clock-violating dz_0-only "
         "deformation has nonzero C1 residual (%s); dn_0-only is caught "
         "by BOTH C1 and C2 (%s); the centre TRANSLATION mode dz_p = "
         "(-i)^p is caught by C1 (%s) while INVISIBLE to every C2 "
         "period row (%s) -- the v515 'forced twice over' structure "
         "made visible: periods alone would NOT pin the orbit centre, "
         "the clock does"
         % (caught_clock, caught_n, caught_trans, blind_trans),
         caught_clock and caught_n and caught_trans and blind_trans)

    ok_sanity = all(in_kernel(M, g) for M in ALL_M.values()
                    for g in GAUGE)
    gate("P8b GAUGE SANITY: all 4 gauge directions lie in all 4 "
         "per-constraint kernels (16/16 exact checks)", ok_sanity)

    # -----------------------------------------------------------------
    print("  -- S5: P9 ablation ledger (leave-one-out moduli kernels)")

    def moduli_kernel(mats):
        Ms = sp.Matrix.vstack(*mats)
        assert all(in_kernel(Ms, g) for g in GAUGE)
        return (NP - Ms.rank()) - 4

    abl = {
        'full': moduli_kernel([M1, M2, M3, M4]),
        '-C1': moduli_kernel([M2, M3, M4]),
        '-C2': moduli_kernel([M1, M3, M4]),
        '-C3': moduli_kernel([M1, M2, M4]),
        '-C4': moduli_kernel([M1, M2, M3]),
        '-C1-C2': moduli_kernel([M3, M4]),
    }
    print("     ablation table (moduli kernel dims): %s"
          % ", ".join("%s: %d" % (k, v) for k, v in abl.items()))
    gate("P9 ABLATION LEDGER: (full, -C1, -C2, -C3, -C4, -C1&C2) = "
         "(%d, %d, %d, %d, %d, %d) = (1, 3, 1, 2, 3, 10): C1 load-"
         "bearing (+2 = the translation modes periods cannot see), C3 "
         "load-bearing (+1 = the residue normalisation), C4 load-"
         "bearing (+2 = the constrained weight directions), C2 "
         "redundant ON THE TANGENT given C1 + C3 (the executed "
         "double-forcing of the flux vector, v515 S4.4 'forced uniform "
         "twice over'); dropping C1 AND C2 opens the centre/charge "
         "blocks wide (10)"
         % (abl['full'], abl['-C1'], abl['-C2'], abl['-C3'],
            abl['-C4'], abl['-C1-C2']),
         (abl['full'], abl['-C1'], abl['-C2'], abl['-C3'], abl['-C4'],
          abl['-C1-C2']) == (1, 3, 1, 2, 3, 10))

    # -----------------------------------------------------------------
    print("  -- S6: must-fail mutants")
    # MUT1: corrupted AB weight -- sector-2 denominator 4 -> 2, i.e.
    # w = (0, 1/2, 1/2, 1/2) => class weights (3/2, -1/2, -1/2, -1/2)
    v_mut = [R(3, 2), R(-1, 2), R(-1, 2), R(-1, 2)]
    A_mut = [sum(v_mut[m] * R(Q5[m][i]) for m in range(4))
             for i in range(5)]
    cert_mut = [dot(f, A_mut) for f in (PHI_T5, PHI_T3, PHI_P, PSI)]
    print("     MUT1: A_mut = %s, certificate %s (executed target "
          "(0, 32, 72, 64))" % (fmt(A_mut), fmt(cert_mut)))
    gate("MUT1 (must fail, CAUGHT): corrupting the sector-2 AB "
         "denominator 4 -> 2 gives A_mut = (6, -36, -6, 8, 16) != "
         "A_fix and certificate (8, 16, 60, 56) != (0, 32, 72, 64): "
         "the anchor + level-set machinery rejects the corrupted "
         "measure at zeroth order",
         A_mut == [6, -36, -6, 8, 16]
         and cert_mut == [8, 16, 60, 56]
         and cert_mut != CERT_TARGET)

    # MUT2: clock-phase mutant covariance -- phase 1 instead of i
    mut2_defect = []
    for j in range(4):
        Rj = sp.expand(Pi_def((j + 1) % 4, -I * LAM) - Pi_def(j, LAM))
        mut2_defect.append(sp.expand(Rj.coeff(LAM, 0).subs(ZERO)))
    expect = [sp.expand(-2 * I * I ** j) for j in range(4)]
    print("     MUT2: mutant-covariance zeroth-order defects %s "
          "(expected -2i i^j)" % fmt(mut2_defect))
    gate("MUT2 (must fail, CAUGHT): the clock-phase mutant covariance "
         "Pi_{j+1}(-i la) = Pi_j(la) (phase 1 instead of the executed "
         "i = det(clock)) is violated by the DECLARED measure already "
         "at zeroth order: defects -2i i^j != 0 on every segment -- "
         "the probe distinguishes the executed clock phase from the "
         "phaseless fake",
         all(sp.expand(mut2_defect[j] - expect[j]) == 0
             for j in range(4))
         and all(d != 0 for d in mut2_defect))

    # -----------------------------------------------------------------
    npass = sum(GATES)
    runtime = time.perf_counter() - T_START
    print("")
    print("  == FINAL REPORT ==")
    print("  gates: %d/%d passed%s" % (npass, len(GATES),
          "" if npass == len(GATES) else "  <-- FAILURES PRESENT"))
    if npass == len(GATES):
        print("  ALL GATES PASSED %d/%d" % (npass, len(GATES)))
    print("  VERDICT: %s" % verdict)
    print("  dims: param 18, gauge 4, moduli 14; ranks C1/C2/C3/C4 = "
          "%d/%d/%d/%d; joint rank %d; joint kernel %d; moduli kernel "
          "%d" % (r1, r2, r3, r4, rall, kdim, kmod))
    print("  surviving direction: uniform sector-weight shift "
          "dv = (1, 1, 1, 1) mod gauge; dA = 36 (1, 2, 1, 0, 0) = the "
          "untwisted Okubo square Q^{(0)}; exactly flat to all orders; "
          "annihilated by every executed certificate functional "
          "(Phi_T5, Phi_T3, Phi_P, psi).")
    print("  honest limitations: the computable sector = the 5-dim "
          "invariant quartic shadow + seam-fibre period vector + "
          "linking-charge lattice + cover charge; C4 pins level sets "
          "of EXECUTED functionals only; the W_2 : W_13 tester is "
          "NOT-TRANSCRIBABLE here; g3/g4 are gauge on THIS sector "
          "only.")
    print("  SPEC_SHA = %s" % spec_sha)
    print("  runtime: %.1f s" % runtime)
    return npass == len(GATES)


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
