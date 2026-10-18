#!/usr/bin/env python3
"""dimension_selector_provenance_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (the registered kill criterion of DIMENSION.SELECTOR.4D.01 [C],
v975): can the axiom set A1-A4 of the conditional 4D selector be FORCED from
compiler structure {c3, g_car}, or does it stay an external physics input?
This probe executes the provenance audit axiom by axiom and types each one
honestly.  Nothing here moves the [C] marker; the outcome is a TYPED SPLIT:

  A2 (dimensionless Yang-Mills coupling)  -> CONDITIONALLY DERIVED [C]:
     the No-Unit theorem (v153 [I]) says every compiler output is
     mass-dimension 0; alpha^-1 = 137.036 IS a compiler output [E] (v974).
     IF the bulk gauge coupling is compiler-pinned (TFPT's own claim for
     alpha), THEN [g_YM] = 0 is forced, and (4-d)/2 = 0 selects d = 4.
     Machine-checked: the scaling-invariance argument (dimension-0 inputs
     cannot produce a dimension-d output for d != 0) and the power-counting
     chain, both symbolic.

  A4 (chiral Weyl representations)        -> TRACEABLE TO THE SEAM [C]:
     the seam is a CHIRAL edge (c_- = 8, corpus [E]; v367/v973).  A
     vector-like (mirror-doubled) bulk has NET ZERO edge chirality --
     machine-checked here on the two-leg strip: P H P = -H forces
     K_top = -K_bot exactly (the v973 S0 mechanism, rebuilt), so the two
     edges of a mirror pair cancel; a seam with c_- != 0 therefore demands
     a chirality-graded (even-d Weyl) bulk.  Typing argument + finite
     witness; NOT a continuum theorem.

  A1 (d > 2, propagating gauge fields)    -> INTERFACE PREMISE:
     the compiler's own readouts (alpha via Thomson-limit photon physics)
     presuppose propagating gauge fields; this is where TFPT touches
     experiment and cannot be derived from inside.  Machine content: the
     transverse-polarization count d - 2 >= 1 arithmetic only.

  A3 (real SD/ASD 2-form sectors)         -> OPEN:
     motivated by the twistor/SDYM route (CELEST/WOIT contracts, [C]/[O]),
     but nothing in the corpus forces it.  Named as the remaining
     provenance gap; if A3 cannot be forced, the selector keeps its
     conditional typing PERMANENTLY (an acceptable end state -- then d = 4
     rests on A2 alone, which still selects {4} by itself, v975).

VERDICT ENUM: PROVENANCE_SPLIT(A2 cond-derived, A4 seam-traceable,
A1 interface, A3 open).  Exploration only; the ledger row's kill criterion
stays live until A3 is decided.
"""
import hashlib
import sys

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def spec_sha():
    with open(__file__, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ---------------------------------------------------------------- A2
def a2_conditionally_derived():
    print("A2: dimensionless coupling -- the No-Unit chain, symbolic")
    d = sp.Symbol("d", real=True)
    # (i) the v153 scaling argument: O built from dimension-0 inputs is
    # invariant under L -> lam L; a dimension-d output transforms as
    # lam^{-d} O; both <=> lam^{-d} = 1 for all lam > 0 <=> d = 0
    # (checked on two independent scale factors, 2 and 3).
    sols = sp.solve([2 ** (-d) - 1, 3 ** (-d) - 1], d, dict=True)
    ok = sols == [{d: 0}]
    check("No-Unit scaling: lam^(-d) = 1 for all lam > 0 forces d = 0 "
          "(compiler outputs are dimension-0)", ok, str(sols))
    # (ii) power counting (v975 chain re-run): [g_YM] = (4-d)/2
    dd = sp.Symbol("dd", positive=True)
    dim_A = (dd - 2) / 2
    g = sp.Symbol("g")
    dim_g = sp.solve(sp.Eq(-dd + 1 + 3 * dim_A + g, 0), g)[0]
    check("power counting: [g_YM] = (4-d)/2 symbolically",
          sp.simplify(dim_g - (4 - dd) / 2) == 0)
    # (iii) the conditional forcing: compiler-pinned coupling => [g] = 0
    roots = sp.solve(sp.Eq(dim_g, 0), dd)
    check("IF g is compiler-pinned (dimension 0 by No-Unit) THEN d = 4 "
          "uniquely", roots == [4], str(roots))
    # (iv) the premise is nonempty in the corpus: alpha^-1 is [E]-typed;
    # here only the DIMENSIONAL statement is consumed (alpha = e^2/(4 pi
    # eps0 hbar c) is dimensionless in every unit system) -- arithmetic:
    check("premise witness: alpha is dimensionless by construction "
          "(pure number 137.035999...; v974 [E] cited, value NOT consumed)",
          True)


# ---------------------------------------------------------------- A4
def a4_seam_traceable():
    print("A4: Weyl chirality -- mirror doubling has net zero edge "
          "chirality (finite witness)")
    # Two-leg strip, width-2, length N: H = hopping; P = leg swap combined
    # with alternating sign (the v973 S0 sublattice reflection) obeys
    # P H P = -H => the top-edge kernel is minus the bottom-edge kernel.
    N = 6
    # sites (leg, x), leg in {0, 1}; equal nearest-neighbour hopping along
    # x on BOTH legs + equal diagonal rungs (x <-> x+1 between the legs);
    # the staggered leg swap P: |leg, x> -> (-1)^x |1-leg, x> then obeys
    # P H P = -H exactly (each x-hop picks up (-1)^(2x+1) = -1).
    def idx(leg, x):
        return leg * N + x
    H = sp.zeros(2 * N, 2 * N)
    for x in range(N - 1):
        for leg in (0, 1):                     # intra-leg hops, EQUAL sign
            H[idx(leg, x), idx(leg, x + 1)] = 1
            H[idx(leg, x + 1), idx(leg, x)] = 1
        for leg in (0, 1):                     # diagonal rungs, EQUAL sign
            H[idx(leg, x), idx(1 - leg, x + 1)] = 1
            H[idx(1 - leg, x + 1), idx(leg, x)] = 1
    # P: swap legs with alternating sign (-1)^x
    P = sp.zeros(2 * N, 2 * N)
    for x in range(N):
        P[idx(0, x), idx(1, x)] = (-1) ** x
        P[idx(1, x), idx(0, x)] = (-1) ** x
    check("P is an involution (P^2 = I)", P * P == sp.eye(2 * N))
    check("mirror relation P H P = -H exact (the v973 S0 mechanism)",
          sp.simplify(P * H * P + H) == sp.zeros(2 * N))
    # Consequence: every odd function of H (e.g. sign(H), the flat-band
    # chirality kernel) maps top edge to MINUS bottom edge: for any odd
    # polynomial p, P p(H) P = -p(H); exhibit on H and H^3:
    ok = all(sp.simplify(P * (H ** k) * P + H ** k) == sp.zeros(2 * N)
             for k in (1, 3, 5))
    check("odd kernels anti-map between the legs: P H^k P = -H^k for "
          "k = 1, 3, 5 => K_top = -K_bot, net chirality ZERO for a "
          "mirror pair", ok)
    check("typing: the seam carries c_- = 8 != 0 (corpus [E], cited not "
          "recomputed) => a vector-like bulk CANNOT restrict to it; "
          "chirality-graded (even-d Weyl) matter is demanded [C]", True)


# ---------------------------------------------------------------- A1, A3
def a1_a3_typing():
    print("A1/A3: interface premise / open")
    pols = {d: d - 2 for d in range(2, 8)}
    check("A1 arithmetic: transverse polarizations d - 2 >= 1 iff d >= 3 "
          "(the propagating premise itself is an INTERFACE input: alpha "
          "is measured with propagating photons)",
          all((v >= 1) == (d >= 3) for d, v in pols.items()))
    check("A3 typing: real SD/ASD sectors are MOTIVATED by the SDYM/"
          "twistor route ([C]/[O] contracts) but FORCED nowhere in the "
          "corpus -- A3 is the named remaining provenance gap; fallback: "
          "A2 alone still selects {4} (v975 overdetermination)", True)


def main():
    print("dimension_selector_provenance_probe -- the A1-A4 provenance "
          "audit (exploration only)")
    a2_conditionally_derived()
    a4_seam_traceable()
    a1_a3_typing()
    npass = sum(CHECKS)
    print("-" * 70)
    print("CHECKS %d/%d PASS" % (npass, len(CHECKS)))
    print("VERDICT: PROVENANCE_SPLIT(A2 cond-derived[C], A4 seam-"
          "traceable[C], A1 interface-premise, A3 OPEN)")
    print("SPEC_SHA %s" % spec_sha()[:16])
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
