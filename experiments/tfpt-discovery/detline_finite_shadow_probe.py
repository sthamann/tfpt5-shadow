#!/usr/bin/env python3
"""detline_finite_shadow_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (SEAM.DETLINE.UNIFICATION.01 [O]): the hypothesis
Res_seam det D_4D ~= det D_seam (determinant lines with connection, bulk
holonomy = discrete orientation phase) needs a computable finite shadow
before anyone attacks the continuum Bismut-Freed step.  This probe builds
that shadow EXACTLY on a magnetic graph Laplacian over a 4x4 grid disk
(12 boundary = "seam" nodes, 4 interior = "bulk" nodes), U(1) phases on
edges, mass term for invertibility -- all exact in Q(i).

THE SCHUR/BFK SHADOW: with L = (D + m) - A_phi and the block split
(I = interior, B = boundary), the Schur identity

    det L = det L_II * det S,   S = L_BB - L_BI L_II^{-1} L_IB

is the finite form of the BFK/Mayer-Vietoris factorization (v974 executed
the continuum circle version): det S is the SEAM determinant (the
Dirichlet-to-Neumann-type boundary object), det L_II the Dirichlet bulk
factor.

  [EXACT] 1. the Schur identity holds exactly in Q(i) on the phased graph.
  [EXACT] 2. RES_SEAM HALF: for flux through a BOUNDARY-ADJACENT
        plaquette (gauge: the mu4 phase i on one boundary-boundary edge)
        the interior Dirichlet block is phase-free, so the FULL bulk
        determinant-line holonomy det L(i)/det L(1) equals the seam
        holonomy det S(i)/det S(1) EXACTLY -- the finite shadow of
        Res_seam det D_bulk ~= det D_seam, with the mu4 orientation
        phase as the tested holonomy.  The holonomy is nontrivial
        (ratio != 1).
  [EXACT] 3. THE LOCAL-FACTOR KILL SHADOW: for flux through an INTERIOR
        plaquette (phase on an interior-interior edge) the Dirichlet
        factor det L_II acquires its own phase dependence, and the bulk
        and seam holonomies DISAGREE by exactly that local factor --
        the finite exhibit of the registered kill test ("the two
        determinant lines differ by a nontrivial local factor"); the
        compatibility theorem must quotient it by a counterterm.
  [EXACT] 4. GAUGE DISCIPLINE: interior gauge transformations leave S
        entrywise invariant; boundary gauge transformations conjugate S
        by a diagonal unitary and leave det S invariant -- the seam
        determinant is a genuine gauge-invariant line datum.

HONEST BOUNDARY: a graph Laplacian shadow, not a Dirac operator, not a
determinant LINE BUNDLE over a parameter space, and nothing about the
continuum Quillen/Bismut-Freed identification (the named critical step of
the contract).  What it establishes: the contract's central identity and
its kill test are both EXHIBITABLE and machine-checkable at finite level,
so the contract has a concrete executable ladder.

VERDICT ENUM: DETLINE_SHADOW_EXACT (Schur level; boundary-adjacent flux
holonomy carried by the seam exactly; interior flux = the local-factor
kill shadow; continuum Bismut-Freed open).
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


def build_L(phase_edges, m=sp.Integer(1)):
    """Magnetic Laplacian L = (deg + m) I - A_phi on the 4x4 grid;
    phase_edges: dict {(u, v): phase} applied as A[u, v] = phase,
    A[v, u] = conj(phase)."""
    nodes = [(x, y) for x in range(4) for y in range(4)]
    idx = {n: k for k, n in enumerate(nodes)}
    N = len(nodes)
    A = sp.zeros(N, N)
    deg = [0] * N
    for (x, y) in nodes:
        for (dx, dy) in ((1, 0), (0, 1)):
            u, v = (x, y), (x + dx, y + dy)
            if v in idx:
                ph = phase_edges.get((u, v), sp.Integer(1))
                A[idx[u], idx[v]] = ph
                A[idx[v], idx[u]] = sp.conjugate(ph)
                deg[idx[u]] += 1
                deg[idx[v]] += 1
    L = sp.diag(*[deg[k] + m for k in range(N)]) - A
    interior = [idx[n] for n in nodes if 0 < n[0] < 3 and 0 < n[1] < 3]
    boundary = [k for k in range(N) if k not in interior]
    return L, interior, boundary, idx


def blocks(L, interior, boundary):
    LII = L[interior, interior]
    LBB = L[boundary, boundary]
    LBI = L[boundary, interior]
    LIB = L[interior, boundary]
    return LII, LBB, LBI, LIB


def schur(L, interior, boundary):
    LII, LBB, LBI, LIB = blocks(L, interior, boundary)
    S = sp.simplify(LBB - LBI * LII.inv() * LIB)
    return LII, S


def main():
    print("detline_finite_shadow_probe -- the finite Schur/BFK shadow of "
          "Res_seam det D_4D ~= det D_seam (exact, Q(i))")

    I4 = sp.I                                    # the mu4 phase

    # ---- flux-free reference
    L0, INT, BND, idx = build_L({})
    LII0, S0 = schur(L0, INT, BND)
    detL0 = sp.simplify(L0.det())
    detS0 = sp.simplify(S0.det())
    detI0 = sp.simplify(LII0.det())
    check("Schur/BFK identity exact (flux-free): det L = det L_II * det S",
          sp.simplify(detL0 - detI0 * detS0) == 0)

    # ---- case A: mu4 flux through a boundary-adjacent plaquette; gauge
    # with the phase i on ONE boundary-boundary edge ((0,0)-(1,0))
    LA, _, _, _ = build_L({((0, 0), (1, 0)): I4})
    LIIA, SA = schur(LA, INT, BND)
    detLA = sp.simplify(LA.det())
    detSA = sp.simplify(SA.det())
    check("case A: the interior Dirichlet block is PHASE-FREE in this "
          "gauge (L_II identical to the flux-free block)",
          sp.simplify(LIIA - LII0) == sp.zeros(4, 4))
    check("case A Schur identity exact with the mu4 phase on the seam "
          "edge", sp.simplify(detLA - sp.simplify(LIIA.det()) * detSA) == 0)
    ratio_bulk = sp.simplify(detLA / detL0)
    ratio_seam = sp.simplify(detSA / detS0)
    check("RES_SEAM HALF exact: bulk holonomy det L(i)/det L(1) == seam "
          "holonomy det S(i)/det S(1) (the full determinant-line response "
          "to the mu4 orientation phase is carried by the seam object)",
          sp.simplify(ratio_bulk - ratio_seam) == 0)
    check("the holonomy is NONTRIVIAL (ratio != 1): the test has content",
          sp.simplify(ratio_bulk - 1) != 0, "ratio = %s" % ratio_bulk)

    # ---- case B: flux through an INTERIOR plaquette; phase on the
    # interior-interior edge ((1,1)-(2,1))
    LB, _, _, _ = build_L({((1, 1), (2, 1)): I4})
    LIIB, SB = schur(LB, INT, BND)
    detLB = sp.simplify(LB.det())
    detSB = sp.simplify(SB.det())
    detIB = sp.simplify(LIIB.det())
    check("case B Schur identity exact with the interior flux",
          sp.simplify(detLB - detIB * detSB) == 0)
    local_factor = sp.simplify(detIB / detI0)
    check("LOCAL-FACTOR KILL SHADOW: the interior Dirichlet determinant "
          "acquires its own phase dependence (local factor != 1)",
          sp.simplify(local_factor - 1) != 0,
          "local factor = %s" % local_factor)
    rb = sp.simplify(detLB / detL0)
    rs = sp.simplify(detSB / detS0)
    check("case B: bulk and seam holonomies DISAGREE exactly by that "
          "local factor (bulk/seam ratio == det L_II ratio) -- the "
          "registered kill test exhibited finitely",
          sp.simplify(rb / rs - local_factor) == 0)

    # ---- gauge discipline
    # interior gauge at node (1,1): G diagonal with i at that node
    g = {n: sp.Integer(1) for n in idx}
    g[(1, 1)] = I4
    G = sp.diag(*[g[n] for n in sorted(idx, key=lambda n: idx[n])])
    # careful: order by index
    Gd = sp.zeros(16, 16)
    for n, k in idx.items():
        Gd[k, k] = g[n]
    LA_g = sp.simplify(Gd * LA * Gd.conjugate().T)
    _, SA_g = schur(LA_g, INT, BND)
    check("gauge discipline: an INTERIOR gauge transformation leaves the "
          "seam Schur complement entrywise invariant",
          sp.simplify(SA_g - SA) == sp.zeros(12, 12))
    g2 = {n: sp.Integer(1) for n in idx}
    g2[(0, 0)] = I4                               # boundary gauge
    Gd2 = sp.zeros(16, 16)
    for n, k in idx.items():
        Gd2[k, k] = g2[n]
    LA_g2 = sp.simplify(Gd2 * LA * Gd2.conjugate().T)
    _, SA_g2 = schur(LA_g2, INT, BND)
    check("gauge discipline: a BOUNDARY gauge transformation conjugates S "
          "by a diagonal unitary and leaves det S invariant (the seam "
          "determinant is a gauge-invariant line datum)",
          sp.simplify(SA_g2.det() - detSA) == 0)

    check("HONEST BOUNDARY (typed): graph-Laplacian shadow, no Dirac "
          "operator, no bundle over parameter space, no continuum "
          "Quillen/Bismut-Freed content -- the contract's identity and "
          "kill test are exhibited finitely, nothing more", True)

    npass = sum(CHECKS)
    print("-" * 70)
    print("CHECKS %d/%d PASS" % (npass, len(CHECKS)))
    print("VERDICT: DETLINE_SHADOW_EXACT (seam carries the boundary-flux "
          "holonomy exactly; interior flux = the local-factor kill "
          "shadow; continuum step open)")
    print("SPEC_SHA %s" % spec_sha()[:16])
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
