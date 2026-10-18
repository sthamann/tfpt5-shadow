#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_uplift_bit_kms_probe -- CCC.SEAM.CROSSOVER (exploration round 8):
can the 2D -> 4D uplift solve OTHER open TFPT items?  Two targets:
(A) the ONE discrete symmetry-lift bit (v512: flag transitivity <=>
tau = i <=> delta = pi/2; "the bit remains formal input") and
(B) the ONE open bridge of P1.INDEX.KMS.01 (the even modular-response
distribution over the deck sectors; kill: any asymmetric sector offset).

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO
ledger row, NO marker moved.  QGEO.SYM.01 stays TFPT's one fundamental
postulate; CELEST's ALE identification stays its own hypothesis chain.
TYPING FENCE (prominent, per the corpus's own warning "a relocation of
the same order-4 carrier input, not a new derivation"): what this probe
establishes are CONDITIONAL REDUCTIONS -- given the ALE/lens uplift
(the corpus's own C^2/Z_4 realisation, WP1-verified at the glue level)
the bit and half the KMS bridge become CONSEQUENCES; the remaining
input collapses onto QGEO.SYM.01 + the CELEST realisation.  No input is
derived from nothing.

PART A (the bit is supplied by the uplift geometry).
  v512: mark-transitivity is automatic for every deck-invariant
  configuration M(delta) = {+-1, +-e^{i delta}} (the pair-exchanging
  V_4); what selects delta = pi/2 <=> tau = i is FLAG transitivity
  (V_4 -> D_4 symmetry lift) -- one discrete bit, formal input.
  THE UPLIFT SUPPLIES IT: on S^3 all four D_4 reflections of the seam
  base are realised by SU(2) isometries M_alpha = [[0, alpha],
  [-conj(alpha), 0]] (base action z -> -(alpha/conj(alpha))/z: all four
  reflection coefficients mu in mu_4 realizable), and EVERY such M
  normalises the deck (M D M^{-1} = D^{-1}) -- so all four descend to
  the lens crossover X = S^3/Z_4 as honest isometries, and the
  descended group acts transitively on the EIGHT FLAGS of the mark
  square: flag transitivity is not a choice on the crossover, it is
  geometry.  ANTI-CIRCULARITY (the decisive check): the lens
  construction consumes only the DECK (order 4 in SU(2) = the A_3 ALE
  datum) and the CLOCK ORDER (4 = h(A_3)) -- NOT the mark positions;
  the free orbit of ANY order-4 rotation through a non-fixed point is
  automatically a square (cross-ratio 2 = the corpus mu_4 signature,
  checked for random base points), while M(delta != pi/2) is NOT the
  free orbit of any order-4 isometry (cyclic cross-ratio != 2, all
  cyclic orders checked): delta = pi/2 is FORCED by orbit structure.
  CONCLUSION (typed): bit <= (QGEO.SYM.01 + CELEST realisation) -- the
  two inputs {order-4 clock, symmetry-lift bit} reduce to one.

PART B (half of the P1.INDEX.KMS.01 bridge from the reciprocal
involution).  The ledger row records the measured "finite evenness
precursor": tracial weights per mu_4 deck sector satisfy w_1 = w_3 =
1/4 EXACTLY at every level, while the w_0/w_2 pair carries the
symmetric offset +-2^{-(l+1)} halving per level.  THE UPLIFT EXPLAINS
THE EXACT HALF: the reciprocal lift J satisfies J D J^{-1} = D^{-1},
so J maps deck sector chi_k to chi_{-k} -- swapping sectors 1 <-> 3
and fixing 0, 2 (checked on the regular representation and on the
fibre Fourier modes).  ANY J-invariant state therefore has w_1 = w_3
EXACTLY -- which is precisely the part the corpus measured as exact;
and the DLII uniqueness result (the unique deck-invariant KMS
representative) IS J-invariant (J is an isometry of the round
representative).  The kill criterion of the contract ("any asymmetric
sector offset") CANNOT fire on the 1/3 pair given the uplift.  What J
cannot force is w_0 = w_2 (sectors fixed by J): that residual is the
GSO-sector balance -- sector 2 is exactly the seam-string holonomy
class of round DLII -- and it is the measured vanishing offset
+-2^{-(l+1)}.  CONCLUSION (typed): the open bridge of P1.INDEX.KMS.01
reduces from "even distribution over four sectors" to the single
Z_2-graded statement w_0 = w_2 (NS/R-type balance), with the other
half now geometric.

WHAT THIS DOES NOT DO: derive QGEO.SYM.01; close P1.INDEX.KMS.01 (the
w_0 = w_2 half stays open); move any marker.
"""

import numpy as np

RNG = np.random.default_rng(20260824)
PASS = []


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


DECK = np.diag([1j, -1j])
CLOCK = np.diag([1j, 1.0])


def mob(M, z):
    return (M[0, 0] * z + M[0, 1]) / (M[1, 0] * z + M[1, 1])


def su2_reflection(mu):
    """SU(2) element with base action z -> mu/z (|mu| = 1):
    M = [[0, alpha], [-conj(alpha), 0]] gives z -> -(alpha/conj(alpha))/z,
    so alpha = i*sqrt(mu) works: -(i sqrt(mu))/(-i conj(sqrt(mu))) =
    sqrt(mu)/conj(sqrt(mu)) = mu."""
    a = 1j * np.sqrt(mu)
    return np.array([[0, a], [-np.conj(a), 0]], dtype=complex)


def part_a():
    print("\nPART A -- the symmetry-lift bit is supplied by the lens"
          " uplift (conditional reduction, typed)")
    mu4 = np.exp(1j * np.pi / 2 * np.arange(4))

    # (A1) all four D_4 reflections realizable in SU(2)
    ok_lift = True
    for mu in mu4:
        M = su2_reflection(mu)
        ok_lift &= np.allclose(M.conj().T @ M, np.eye(2))
        ok_lift &= np.isclose(np.linalg.det(M), 1.0)
        zs = RNG.standard_normal(8) + 1j * RNG.standard_normal(8)
        ok_lift &= all(np.isclose(mob(M, z), mu / z) for z in zs)
    check("all four D_4 reflections z -> mu/z (mu in mu_4) are realised"
          " by SU(2) isometries of S^3 (unitary, det 1, base action"
          " verified)", ok_lift)

    # (A2) every reflection lift normalises the deck => descends to X
    ok_norm = all(np.allclose(
        su2_reflection(mu) @ DECK @ np.linalg.inv(su2_reflection(mu)),
        np.linalg.inv(DECK)) for mu in mu4)
    check("every reflection lift normalises the deck (M D M^{-1} ="
          " D^{-1}) => all four descend to the lens crossover as honest"
          " isometries", ok_norm)

    # (A3) flag transitivity on the crossover: the descended group acts
    # transitively on the 8 flags (mark, direction) of the mark square
    flags = [(k, s) for k in range(4) for s in (+1, -1)]

    def act_on_flag(gname, flag):
        k, s = flag
        if gname == "rho":                 # z -> iz: mark k -> k+1
            return ((k + 1) % 4, s)
        # reflection with coefficient mu = i^m: z -> i^m/z maps mark
        # i^k -> i^{m-k}; orientation reverses
        m = int(gname)
        return ((m - k) % 4, -s)

    reached = {flags[0]}
    frontier = [flags[0]]
    gens = ["rho", "0", "1", "2", "3"]
    while frontier:
        new = []
        for f in frontier:
            for g in gens:
                f2 = act_on_flag(g, f)
                if f2 not in reached:
                    reached.add(f2)
                    new.append(f2)
        frontier = new
    check(f"the descended group acts TRANSITIVELY on all 8 flags of the"
          f" mark square (reached {len(reached)}/8): flag transitivity"
          f" -- the v512 bit -- is GEOMETRY on the crossover, not an"
          f" input", len(reached) == 8)

    # (A4) anti-circularity 1: the free orbit of the order-4 clock
    # through ANY non-fixed point is a square (cross-ratio 2)
    def cross_ratio(a, b, c, d):
        return ((a - c) * (b - d)) / ((a - d) * (b - c))

    ok_orbit = True
    for _ in range(16):
        z0 = RNG.standard_normal() + 1j * RNG.standard_normal()
        orb = [z0 * 1j ** k for k in range(4)]
        ok_orbit &= np.isclose(cross_ratio(*orb), 2.0)
    check("the free orbit of ANY order-4 rotation is automatically a"
          " square: cross-ratio(z0, iz0, -z0, -iz0) = 2 (the corpus"
          " mu_4 signature) for random base points -- the lens"
          " construction never consumed the mark positions", ok_orbit)

    # (A5) anti-circularity 2: M(delta != pi/2) is NOT a free order-4
    # orbit (no cyclic order gives cross-ratio 2)
    ok_force = True
    for delta in (0.4, 0.9, 1.3, 2.1):
        pts = [1, np.exp(1j * delta), -1, -np.exp(1j * delta)]
        import itertools
        crs = []
        for perm in itertools.permutations(pts):
            crs.append(cross_ratio(*perm))
        ok_force &= not any(np.isclose(c, 2.0, atol=1e-9) for c in crs)
    ok_pi2 = np.isclose(
        cross_ratio(1, 1j, -1, -1j), 2.0)
    check("M(delta) for delta != pi/2 admits NO ordering with"
          " cross-ratio 2 (checked all 24 orderings, four deltas) while"
          " delta = pi/2 does: the square is FORCED by order-4 orbit"
          " structure -- delta = pi/2 is a consequence, not a choice",
          ok_force and ok_pi2)

    print("    TYPED CONCLUSION: bit <= QGEO.SYM.01 + CELEST/ALE"
          " realisation (conditional reduction; a relocation onto the"
          " existing premises, honestly NOT a derivation from nothing)")


def part_b():
    print("\nPART B -- half of the P1.INDEX.KMS.01 bridge from the"
          " reciprocal involution")

    # (B1) J conjugation inverts the deck => sector swap 1 <-> 3
    J = np.array([[0, -1], [1, 0]], dtype=complex)
    check("J D J^{-1} = D^{-1} (the reciprocal lift inverts the deck)",
          np.allclose(J @ DECK @ np.linalg.inv(J), np.linalg.inv(DECK)))

    # (B2) on the regular representation of Z_4: the sector projectors
    # P_k = (1/4) sum_j chi_k(j)* S^j; conjugation by the inversion
    # permutation maps P_k -> P_{-k}
    S = np.roll(np.eye(4), 1, axis=0)              # regular shift
    inv_perm = np.eye(4)[[0, 3, 2, 1]]             # j -> -j
    ok_swap = True
    for k in range(4):
        Pk = sum(np.exp(-2j * np.pi * k * j / 4) * np.linalg.matrix_power(
            S, j) for j in range(4)) / 4
        Pmk = sum(np.exp(-2j * np.pi * ((-k) % 4) * j / 4)
                  * np.linalg.matrix_power(S, j) for j in range(4)) / 4
        ok_swap &= np.allclose(inv_perm @ Pk @ inv_perm.T, Pmk)
    check("deck-sector projectors under the inversion: P_k -> P_{-k}"
          " exactly -- sectors 1 and 3 SWAP, sectors 0 and 2 are fixed",
          ok_swap)

    # (B3) fibre Fourier modes: J reverses the clock/fibre orientation,
    # mode k -> -k, sector k mod 4 -> -k mod 4
    ks = np.arange(-8, 9)
    sect = ks % 4
    sect_J = (-ks) % 4
    ok_modes = all((a, b) in {(0, 0), (1, 3), (2, 2), (3, 1)}
                   for a, b in zip(sect, sect_J))
    check("fibre Fourier modes: J maps sector k -> -k mod 4 on every"
          " mode (1 <-> 3, 0 and 2 fixed)", ok_modes)

    # (B4) any J-invariant state has w_1 = w_3 EXACTLY
    w = RNG.uniform(0.1, 1.0, 4)
    wJ = w[[0, 3, 2, 1]]
    w_sym = (w + wJ) / 2
    w_sym /= w_sym.sum()
    check(f"J-symmetrisation forces w_1 = w_3 exactly"
          f" (symmetrised weights {np.round(w_sym, 4).tolist()}) while"
          f" leaving w_0, w_2 free -- the contract kill 'asymmetric"
          f" sector offset' CANNOT fire on the 1/3 pair given the"
          f" uplift", np.isclose(w_sym[1], w_sym[3]))

    # (B5) correspondence with the measured corpus precursor (cited):
    # w_1 = w_3 = 1/4 EXACT at every level; the offset sits ONLY in
    # (w_0, w_2) as +-2^{-(l+1)} -- exactly the J-forced/J-free split
    levels = np.arange(1, 7)
    off = 2.0 ** (-(levels + 1))
    w0 = 0.25 + off
    w2 = 0.25 - off
    ok_shape = (np.allclose(w0 + w2, 0.5)
                and np.all(np.abs(w0 - w2) > 0)
                and np.allclose(np.diff(np.log2(off)), -1.0))
    check("the corpus's measured precursor has EXACTLY the J-split"
          " shape: the J-forced pair (1,3) exact at 1/4, the J-free"
          " pair (0,2) carrying the halving offset +-2^{-(l+1)} (zero-"
          "sum, vanishing) -- typed [C] correspondence, not a"
          " re-measurement", ok_shape)

    print("    TYPED CONCLUSION: the open bridge reduces to the single"
          " Z_2-graded statement w_0 = w_2 (the GSO/seam-string sector"
          " balance, = the DLII holonomy class) -- half the bridge is"
          " now geometric, the other half stays [O]")


def main():
    print("=" * 72)
    print("ccc_uplift_bit_kms_probe -- the uplift attacks two other open")
    print("TFPT items: the v512 symmetry-lift bit and the P1.INDEX.KMS.01")
    print("bridge (EXPLORATION ONLY, no ledger)")
    print("=" * 72)
    part_a()
    part_b()
    print("\n" + "=" * 72)
    n_ok = sum(PASS)
    print(f"RESULT: {n_ok}/{len(PASS)} checks passed"
          + ("  --  ALL PASSED" if all(PASS) else "  --  FAILURES ABOVE"))
    print("(A) the delta = pi/2 / tau = i bit: supplied by the lens-uplift")
    print("    D_4 isometries; forced by order-4 orbit structure --")
    print("    conditional reduction onto QGEO.SYM.01 + CELEST (typed).")
    print("(B) P1.INDEX.KMS.01: w_1 = w_3 now geometric (J-invariance);")
    print("    the bridge reduces to the GSO balance w_0 = w_2 [O].")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
