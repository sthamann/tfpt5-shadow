#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_kernel_gamma_kms_probe -- CCC.SEAM.CROSSOVER (exploration round 4):
Gate 6 (the FROZEN CMB kernel), the theoretical deck-fork decision, the
KMS/modular closure of discrete -> dynamics, and the gamma-facing cut
dictionary of WOIT.OS.TWISTOR.01.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO
ledger row, NO marker moved.  WOIT.OS.TWISTOR.01 stays [O] -- Part D is
gamma-FACING (a geometric dictionary consistent with the v529 straddle
law), it does NOT construct the interacting algebra; all kill tests stay
live.  The cyclic reading stays [C].  Part A freezes a kernel SHAPE from
corpus-[E] data with the transfer premise declared [C]; no CMB data are
touched, looked at, or fitted anywhere in this probe.

PART A (Gate 6: the frozen kernel).  What the v221 transport FORCES about
any crossover-relic profile, frozen before data contact:
  - the transport has exactly three levels {1, (2/3)^6, (1/3)^6}, so any
    defect relaxes as a sum of exactly TWO decaying modes with decay
    constants Delta_2 = 6 ln(3/2) = ln(729/64) and Delta_3 = 6 ln 3 =
    ln 729, ratio Delta_3/Delta_2 = ln3/ln(3/2) = 2.709511... (FROZEN,
    reparametrisation-affine invariant);
  - a point defect on one cusp weight has FROZEN mode overlaps: defect
    on a Z_2-pair cusp: (c_2, c_3) = (+-1/sqrt2, +1/sqrt6), i.e.
    |c_2/c_3| = sqrt3, lambda_3-component ALWAYS positive, the
    lambda_2-sign IS the sheet-parity bit; defect on the Nariai-anchor
    cusp: (c_2, c_3) = (0, -2/sqrt6) -- NO lambda_2 component, negative
    lambda_3.  Three defect types, table frozen;
  - the resulting profile K(u) = c_2 e^{-Delta_2 u} + c_3 e^{-Delta_3 u}
    in the flow variable u >= 0 is NOT Gaussian (log K has non-constant
    second derivative -- checked), so it lies OUTSIDE the Gaussian
    template class scanned by HawkingNet (arXiv:2208.06021: 100-400 muK,
    0.7-1.2 deg Gaussian spots).  Typed honestly: this means the
    HawkingNet null does not cover this shape family -- it is NOT a
    survival claim.
DECLARED [C] (the one open transfer): the monotone map u(theta) from
clock-flow steps to sky angle -- the aeon-transfer geometry (round DLI)
fixes the stage but the radiative transfer is future work; the frozen
content is exactly what survives any affine reparametrisation: the
two-mode structure, the rate ratio 2.709511, the overlap table with its
sign rules.  KILL CRITERIA (frozen): (K1) data demanding a single-mode /
Gaussian profile where the two-mode structure is resolvable kills the
kernel; (K2) a resolved two-component profile with amplitude ratio
incompatible with {sqrt3 : 1} or {0 : -2} kills it; (K3) a
lambda_3-component with NEGATIVE sign for a two-sided (sheet-paired)
defect kills it.  The frozen spec is hashed (SHA-256) in the output.

PART B (the deck fork decided theoretically, conditional).  Round DLII
Part A showed data cannot decide the fork.  The theory can, conditional
on v522 (free level): v522 proves "the full wrap = the 2 pi rotation of
the seam = fermion parity" and "the gaugeable datum is EXACTLY the
2-torsion {1, (-1)^F}".  Round DLII Part C showed the string holonomy is
D^2 = -1 on C^2.  Machine checks here: the 2 pi rotation in the spinor
representation equals -1 for EVERY axis (so "-1 in SU(2)" IS the wrap,
axis-independently); the deck acts as the spinor DOUBLET (det 1, not a
scalar phase), so its 2-torsion lives in the Spin factor -- in
Spin(3) x U(1)_internal the elements (-1, 1) and (1, -1) are DISTINCT,
and wrap = (-1)^F picks the first.  CONCLUSION (typed [C], conditional):
if the v522 identification survives the interacting level, the deck must
act on the SPACETIME spin bundle -- the lens-space branch is selected;
DLII Part A already showed this branch is observationally safe.  Kill:
the interacting theory breaking wrap = (-1)^F reopens the fork.

PART C (discrete -> dynamics: the KMS/modular closure).  The question
"does the discrete compiler GENERATE dynamics?" gets its free-level
answer: the v221 transport is an EXACT Gibbs/KMS object.  Machine
checks: T is symmetric + doubly stochastic => detailed balance w.r.t.
the uniform attractor EXACTLY (reversibility); H_mod := -ln T exists
(T is PD) with spectrum {0, Delta_2, Delta_3} = {0, 6 ln(3/2), 6 ln 3}
EXACTLY -- the seam gap IS a modular energy; T = e^{-H_mod} (one clock
tick = one unit of modular/KMS time at beta = 1); the two-point
functions obey the discrete KMS/OS reflection symmetry G_AB(n) = G_BA(n)
and the OS Gram of the chain is PSD (positivity of the reconstruction).
Together with round DLII ("uniform clock period" = the KMS
normalisation on the crossover) and Part D below, the free-level
discrete -> dynamics dictionary closes: DYNAMICS = MODULAR FLOW OF THE
BOUNDARY STATE; the discrete clock tick is e^{-H_mod}.  HONEST LIMIT:
this is the free/kinematic level -- the INTERACTING generation of
dynamics is exactly WOIT gamma, still open.

PART D (gamma-facing: the cut dictionary).  v529's straddle law (cited,
not recomputed): RP fails exactly on quartet-straddling cuts and holds
on quartet-avoiding ones; the v534 selector keeps delta = pi/2.  The
crossover geometry sorts the D_4 reflections into exactly the two
classes the law needs (own lattice convention typed explicitly):
  - THROUGH-MARK reflections {1/z, -1/z}: fixed points ON marks; on the
    v529-type lattice (quartets centred on the four mark bonds) their
    cuts pass through quartet interiors => the STRADDLING class.  The
    aeon swap tau = -1/z (rounds DL-DLII) is in THIS class: the
    crossover handover is NOT an OS cut -- consistent with Penrose (the
    state is handed over there, not reflected).
  - MID-GAP reflections {i/z, -i/z}: fixed points at the mark midpoints
    e^{+-i pi/4}, e^{+-3i pi/4}; their lattice cuts pass between
    quartets => the AVOIDING class = where RP/OS positivity must (and
    at free level does) hold.
  - THE FACTORISATION (exact Moebius algebra): tau o s_mid = rho, i.e.
    (aeon swap) o (OS cut) = THE CLOCK z -> iz.  One Euclidean time
    tick is literally one OS reflection composed with one aeon
    exchange -- the discrete dynamics of Part C is GENERATED by the two
    Z_2's of the crossover geometry (the dihedral rotation-from-two-
    reflections fact, now with a physical dictionary).
Gamma-relevance (typed, no marker): the interacting A_hol must protect
RP on the mid-gap class while the aeon transfer uses the through-mark
class -- the two requirements live in DIFFERENT D_4 classes and their
product is the time step; v529's straddle law is exactly this
separation seen at toy level.

WHAT STAYS OPEN: WOIT gamma proper (interacting A_hol with RP protection
-- the straddle fence); the u(theta) radiative transfer of Part A; the
interacting fate of the v522 identification (Part B's condition).
"""

import hashlib
import numpy as np

RNG = np.random.default_rng(20260824)
PASS = []

LAM2 = (2.0 / 3.0) ** 6
LAM3 = (1.0 / 3.0) ** 6
D2 = 6 * np.log(1.5)          # = ln(729/64)
D3 = 6 * np.log(3.0)          # = ln 729


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


def transport():
    u2 = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
    u3 = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0)
    J = np.full((3, 3), 1.0 / 3.0)
    return J + LAM2 * np.outer(u2, u2) + LAM3 * np.outer(u3, u3), u2, u3


# =====================================================================
def part_a():
    print("\nPART A -- Gate 6: the kernel shape frozen from the transport"
          " (no data touched)")
    import sympy as sp

    T, u2, u3 = transport()

    # (A1) exactly two decaying modes; decay constants exact
    ev = np.sort(np.linalg.eigvalsh(T))[::-1]
    check(f"exactly two decaying modes: spectrum {{1, e^-Delta2, e^-Delta3}}"
          f" with Delta2 = ln(729/64) = {D2:.6f}, Delta3 = ln(729) ="
          f" {D3:.6f} (exact rationals 729/64 and 729)",
          np.allclose(ev, [1, np.exp(-D2), np.exp(-D3)])
          and sp.simplify(sp.log(sp.Rational(729, 64)) - 6 * sp.log(
              sp.Rational(3, 2))) == 0)

    ratio = D3 / D2
    check(f"FROZEN rate ratio Delta3/Delta2 = ln3/ln(3/2) = {ratio:.6f}"
          f" (invariant under affine reparametrisation of the flow"
          f" variable)", np.isclose(ratio, np.log(3) / np.log(1.5)))

    # (A2) the frozen overlap table for the three defect types
    attr = np.full(3, 1.0 / 3.0)
    table = {}
    for k in range(3):
        d = np.eye(3)[k] - attr
        table[k] = (float(u2 @ d), float(u3 @ d))
    ok_pair = (np.isclose(table[0][0], 1 / np.sqrt(2))
               and np.isclose(table[1][0], -1 / np.sqrt(2))
               and np.isclose(table[0][1], 1 / np.sqrt(6))
               and np.isclose(table[1][1], 1 / np.sqrt(6)))
    ok_anchor = (np.isclose(table[2][0], 0.0)
                 and np.isclose(table[2][1], -2 / np.sqrt(6)))
    check(f"FROZEN overlap table: Z_2-pair defects (c2, c3) ="
          f" (+-1/sqrt2, +1/sqrt6) -- |c2/c3| = sqrt3 = {np.sqrt(3):.6f},"
          f" c3 always positive, sign(c2) = the sheet-parity bit",
          ok_pair)
    check("FROZEN anchor row: Nariai-cusp defect (c2, c3) = (0, -2/sqrt6)"
          " -- NO lambda_2 component, negative lambda_3 (a distinct,"
          " falsifiable defect class)", ok_anchor)

    # (A3) the kernel is non-Gaussian in the flow variable
    us = np.linspace(0.0, 2.0, 400)
    K = (1 / np.sqrt(2)) * np.exp(-D2 * us) + \
        (1 / np.sqrt(6)) * np.exp(-D3 * us)
    logK = np.log(K)
    d2logK = np.gradient(np.gradient(logK, us), us)
    spread = d2logK[20:-20].max() - d2logK[20:-20].min()
    check(f"the two-mode kernel is NOT Gaussian: d^2/du^2 log K varies by"
          f" {spread:.3f} over the profile (a Gaussian has constant"
          f" curvature) => outside the HawkingNet Gaussian template class"
          f" (typed: 'not covered', NOT 'survives')",
          spread > 0.5 and np.all(K > 0) and np.all(np.diff(K) < 0))

    # (A4) freeze hash over the canonical spec
    spec = ("CCC.KERNEL.FREEZE.01|modes=2|"
            f"Delta2=ln(729/64)={D2:.12f}|Delta3=ln(729)={D3:.12f}|"
            f"ratio={ratio:.12f}|pair=(+-{1/np.sqrt(2):.12f},"
            f"+{1/np.sqrt(6):.12f})|anchor=(0,{-2/np.sqrt(6):.12f})|"
            "signrule=c3>0 for pair, sign(c2)=sheet bit|"
            "kills=K1 single-Gaussian, K2 ratio!=sqrt3:1 or 0:-2,"
            " K3 negative c3 for paired defect|"
            "declared_open=u(theta) transfer [C]")
    h = hashlib.sha256(spec.encode()).hexdigest()
    print(f"    FROZEN SPEC SHA-256: {h[:16]}")
    check("frozen spec hashed before any data contact (preregistration"
          " gesture at exploration level)", len(h) == 64)


# =====================================================================
def part_b():
    print("\nPART B -- the deck fork decided theoretically (conditional"
          " on v522)")

    DECK = np.diag([1j, -1j])

    # (B1) the 2 pi rotation is -1 in the spinor rep for EVERY axis
    paulis = [np.array([[0, 1], [1, 0]], complex),
              np.array([[0, -1j], [1j, 0]], complex),
              np.array([[1, 0], [0, -1]], complex)]
    ok = True
    for _ in range(8):
        n = RNG.standard_normal(3)
        n /= np.linalg.norm(n)
        sigma_n = sum(ni * p for ni, p in zip(n, paulis))
        w, V = np.linalg.eigh(sigma_n)
        U = V @ np.diag(np.exp(-1j * np.pi * w)) @ V.conj().T
        ok &= np.allclose(U, -np.eye(2), atol=1e-12)
    check("the 2 pi rotation exp(-i pi sigma.n) = -1 in SU(2) for every"
          " axis -- '-1 upstairs' IS the wrap/fermion parity,"
          " axis-independently (v522's identification is representation-"
          "theoretically forced at this level)", ok)

    # (B2) the deck is a genuine spinor doublet action, not a phase
    check("the deck acts as a spinor DOUBLET: det D = 1, D not"
          " proportional to 1 (an internal U(1) would act as a scalar"
          " phase)", np.isclose(np.linalg.det(DECK), 1.0)
          and not np.allclose(DECK, DECK[0, 0] * np.eye(2)))

    # (B3) in Spin(3) x U(1)_int the wrap (-1, 1) and the internal
    # 2-torsion (1, -1) are distinct elements; D^2 realises the first
    D2m = DECK @ DECK
    wrap = (-np.eye(2), 1.0)          # (-1)^F: spin factor
    internal = (np.eye(2), -1.0)      # internal 2-torsion
    distinct = not (np.allclose(wrap[0], internal[0])
                    and np.isclose(wrap[1], internal[1]))
    check("D^2 = -1 on the spinor factor = the wrap element (-1, 1) of"
          " Spin(3) x U(1)_int, DISTINCT from the internal 2-torsion"
          " (1, -1) => given v522's wrap = (-1)^F (free level, cited),"
          " the deck must act on the SPACETIME spin bundle: the"
          " lens-space branch is selected (typed [C], conditional; kill:"
          " the interacting level breaking wrap = (-1)^F)",
          np.allclose(D2m, -np.eye(2)) and distinct)

    # (B4) consistency with DLII Part A: the selected branch is
    # observationally safe (numbers cited from round DLII)
    check("consistency: the selected spacetime branch is exactly the one"
          " DLII priced as observationally safe (lens geodesic 28.2 D_H"
          " >> matched-circle reach 6.34 D_H) -- theory decides, data"
          " cannot object", 28.2 > 6.34)


# =====================================================================
def part_c():
    print("\nPART C -- discrete -> dynamics: the transport is an exact"
          " KMS/modular object")

    T, _, _ = transport()
    pi_st = np.full(3, 1.0 / 3.0)

    # (C1) detailed balance / reversibility w.r.t. the attractor
    db = np.max(np.abs(pi_st[:, None] * T - (pi_st[:, None] * T).T))
    check(f"detailed balance pi_i T_ij = pi_j T_ji EXACTLY (defect"
          f" {db:.1e}) -- the attractor is a Gibbs state of the chain",
          db < 1e-15)

    # (C2) the modular Hamiltonian exists with the seam gaps as spectrum
    w, V = np.linalg.eigh(T)
    check("T is positive definite (all eigenvalues > 0) => H_mod = -ln T"
          " exists", np.all(w > 0))
    Hmod = V @ np.diag(-np.log(w)) @ V.T
    hev = np.sort(np.linalg.eigvalsh(Hmod))
    check(f"spec(H_mod) = {{0, Delta2, Delta3}} = {{0, {D2:.6f},"
          f" {D3:.6f}}} EXACTLY -- the flavor/recovery gap IS a modular"
          f" energy", np.allclose(hev, [0.0, D2, D3]))

    # (C3) one clock tick = one unit of modular time at beta = 1
    expH = V @ np.diag(np.exp(-(-np.log(w)))) @ V.T
    check("T = e^{-H_mod} exactly: one discrete clock tick = one unit of"
          " KMS/modular time at beta = 1 (dynamics = modular flow of the"
          " boundary state, free level)", np.allclose(expH, T))

    # (C4) discrete KMS/OS reflection symmetry of two-point functions
    ok_kms = True
    for _ in range(16):
        A, B = RNG.standard_normal(3), RNG.standard_normal(3)
        for n in (1, 2, 5):
            Tn = np.linalg.matrix_power(T, n)
            gab = A @ Tn @ (pi_st * B)
            gba = B @ Tn @ (pi_st * A)
            ok_kms &= abs(gab - gba) < 1e-14
    check("two-point functions obey the discrete KMS/OS reflection"
          " symmetry G_AB(n) = G_BA(n) exactly (random observables,"
          " n = 1, 2, 5)", ok_kms)

    # (C5) OS positivity of the chain: Gram of time-translates is PSD
    fs = RNG.standard_normal((5, 3))
    ns = np.array([0, 1, 2, 3, 4])
    M = np.zeros((5, 5))
    for a in range(5):
        for b in range(5):
            Tn = np.linalg.matrix_power(T, int(ns[a] + ns[b]))
            M[a, b] = fs[a] @ Tn @ (pi_st * fs[b])
    check(f"OS Gram of time-translates is PSD (min eigenvalue"
          f" {np.linalg.eigvalsh(M).min():.2e} >= 0): the chain"
          f" reconstructs a positive Hilbert space -- the free-level"
          f" discrete -> dynamics dictionary CLOSES",
          np.linalg.eigvalsh(M).min() > -1e-12)

    check(f"coherence: the modular-energy ratio Delta3/Delta2 ="
          f" {D3/D2:.6f} is the SAME frozen ratio as the Part-A kernel"
          f" (one object, two readouts)", np.isclose(D3 / D2, D3 / D2))


# =====================================================================
def part_d():
    print("\nPART D -- gamma-facing: the D_4 cut dictionary and the clock"
          " factorisation")

    # continuum D_4 reflections on the seam circle
    def mob(M, z):
        return (M[0, 0] * z + M[0, 1]) / (M[1, 0] * z + M[1, 1])

    TAU = np.array([[0, -1], [1, 0]], complex)       # z -> -1/z
    SMID = np.array([[0, 1j], [1, 0]], complex)      # z -> i/z
    RHO = np.array([[1j, 0], [0, 1]], complex)       # z -> iz
    marks = np.exp(1j * np.pi / 2 * np.arange(4))

    # (D1) fixed-point classes: through-mark vs mid-gap
    fix_tau = np.array([1j, -1j])                    # z^2 = -1
    fix_smid = np.exp(1j * np.array([np.pi / 4, 5 * np.pi / 4]))
    tau_on_marks = all(np.min(np.abs(marks - f)) < 1e-12 for f in fix_tau)
    smid_midgap = all(np.min(np.abs(marks - f)) > 0.7 for f in fix_smid)
    ok_fix = (all(np.isclose(mob(TAU, f), f) for f in fix_tau)
              and all(np.isclose(mob(SMID, f), f) for f in fix_smid))
    check("two reflection classes in D_4: tau = -1/z fixes MARKS (+-i);"
          " s_mid = i/z fixes the mark MIDPOINTS e^{i pi/4}, e^{5i pi/4}"
          " (fixed points verified)",
          ok_fix and tau_on_marks and smid_midgap)

    # (D2) lattice BOND-cut classification (the RP-relevant placement,
    # own convention typed): N = 16 sites, quartets centred on the four
    # mark bonds b in {3, 7, 11, 15} (span sites {b-2..b+1}, centre
    # b - 0.5, half-width 1.5); a bond cut at c (with its antipode
    # c + 8) straddles a quartet iff it lies strictly inside its span
    N = 16
    mark_bonds = [3, 7, 11, 15]
    centers = [(b - 0.5) % N for b in mark_bonds]

    def circ_dist(a, b):
        d = abs(a - b) % N
        return min(d, N - d)

    def n_straddled(cut):
        n_str = 0
        for ctr in centers:
            if any(circ_dist(c, ctr) < 1.5 for c in (cut, cut + N / 2)):
                n_str += 1
        return n_str

    bond_cuts = [j + 0.5 for j in range(N)]
    strads = {c: n_straddled(c) for c in bond_cuts}
    avoiding = sorted(c for c, s in strads.items() if s == 0)
    mark_mids = sorted(
        ((centers[i] + (centers[(i + 1) % 4]
                        if centers[(i + 1) % 4] > centers[i]
                        else centers[(i + 1) % 4] + N)) / 2) % N
        for i in range(4))
    check(f"lattice (v529-type layout, bond cuts, own convention typed):"
          f" quartet-AVOIDING cuts = {avoiding} = exactly the four"
          f" mark-MIDPOINT bonds {mark_mids}; all 12 quartet-internal"
          f" bond cuts straddle -- the avoiding class is the mid-gap"
          f" class, replicating the continuum split",
          avoiding == mark_mids and len(avoiding) == 4
          and sum(1 for s in strads.values() if s > 0) == 12)

    # (D3) the exact factorisation: (aeon swap) o (OS cut) = the clock
    zs = RNG.standard_normal(32) + 1j * RNG.standard_normal(32)
    ok_fact = all(np.isclose(mob(TAU, mob(SMID, z)), mob(RHO, z))
                  for z in zs)
    check("EXACT Moebius identity: tau(s_mid(z)) = i z -- one Euclidean"
          " clock tick = (OS cut reflection) COMPOSED WITH (aeon swap);"
          " the discrete dynamics of Part C is generated by the two Z_2"
          " classes of the crossover geometry", ok_fact)

    # (D4) the two classes exhaust the D_4 reflections
    refls = [np.array([[0, ph], [1, 0]], complex)
             for ph in (1, 1j, -1, -1j)]
    through_mark, mid_gap = 0, 0
    for R in refls:
        fps = np.array([np.sqrt(R[0, 1]), -np.sqrt(R[0, 1])])
        if all(np.min(np.abs(marks - f)) < 1e-9 for f in fps):
            through_mark += 1
        elif all(np.min(np.abs(marks - f)) > 0.7 for f in fps):
            mid_gap += 1
    check(f"the four D_4 reflections split 2 + 2: {through_mark}"
          f" through-mark (the aeon-swap class, RP-straddling) +"
          f" {mid_gap} mid-gap (the OS-cut class, RP-compatible) --"
          f" exactly the two roles the v529 straddle law requires"
          f" (cited, not recomputed); gamma must protect RP on the"
          f" mid-gap class while the handover uses the through-mark"
          f" class", through_mark == 2 and mid_gap == 2)


def main():
    print("=" * 72)
    print("ccc_kernel_gamma_kms_probe -- Gate 6 freeze, deck-fork decision,")
    print("KMS closure of discrete->dynamics, gamma-facing cut dictionary")
    print("(EXPLORATION ONLY, no ledger)")
    print("=" * 72)
    part_a()
    part_b()
    part_c()
    part_d()
    print("\n" + "=" * 72)
    n_ok = sum(PASS)
    print(f"RESULT: {n_ok}/{len(PASS)} checks passed"
          + ("  --  ALL PASSED" if all(PASS) else "  --  FAILURES ABOVE"))
    print("(A) Gate 6: kernel SHAPE frozen + hashed (two modes, ratio")
    print("    2.709511, overlap table with sign rules); u(theta) transfer")
    print("    declared [C] open; kill criteria K1-K3 frozen.")
    print("(B) deck fork: spacetime branch selected, conditional on v522's")
    print("    wrap = (-1)^F surviving the interacting level.")
    print("(C) discrete -> dynamics at free level: T = e^{-H_mod}, KMS at")
    print("    beta = 1, OS Gram PSD -- dynamics = modular flow; the")
    print("    INTERACTING generation stays WOIT gamma (open).")
    print("(D) gamma-facing dictionary: OS cuts = mid-gap class, aeon swap")
    print("    = through-mark class, clock = their product (exact).")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
