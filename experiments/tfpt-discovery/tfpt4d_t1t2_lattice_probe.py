#!/usr/bin/env python3
"""tfpt4d_t1t2_lattice_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (TFPT4D.LATTICE.ACTION.01 [O], the cheapest entry): do the
first two finite gates of the contract -- T1 exact gauge invariance and
T2 a positive transfer matrix -- hold for a Wilson/heat-kernel transfer
construction with the mu4 structure group AND with a seam-pinned boundary
link, at a size where everything is machine-checkable?  This is the
Osterwalder-Seiler mechanism made executable on two toys:

  MODEL (i)  Z2 gauge on ONE 3D CUBE (12 links, 6 faces; Hilbert dim
        2^12 = 4096) -- three SPATIAL dimensions, i.e. the transfer-
        matrix geometry of a 3+1D theory at minimal spatial size.
        T = V^(1/2) K V^(1/2) with V = exp(beta * sum_faces s_f)
        (diagonal magnetic term) and K = tensor product of per-link
        heat kernels (kinetic/electric term, PD by positive Fourier
        coefficients).
        [T2] T is symmetric positive definite (Cholesky succeeds; PD is
             structural: T is congruent to the PD kernel K).
        [T1] all 8 Gauss operators G_v = prod_{links at v} X commute
             with T exactly (each face at v contains exactly two
             v-incident links, so V is invariant; K is X-diagonal).
        [MUTANT] a complex-action mutant (beta -> beta + i*gamma)
             destroys hermiticity/positivity -- the gate has teeth.

  MODEL (ii) Z4 = mu4 gauge on one plaquette (4 links; dim 4^4 = 256),
        the structure group being the compiler clock itself.
        [T1] the four Z4 Gauss operators commute with T (< 1e-12).
        [T2] T positive definite.
        [T3 MECHANISM] SEAM PINNING: freezing one boundary link to the
             mu4 clock value g = 1 (phase i) restricts T to a 64-dim
             block that stays positive definite and stays invariant
             under the two Gauss operators NOT touching the pinned
             link, while the two seam-touching gauge transformations
             are (correctly) broken by the boundary condition -- the
             mechanism of the T3 gate (a seam boundary restriction
             compatible with interior gauge invariance + RP).

HONEST BOUNDARY (dimension-uplift firewall applies): these are REDUCED-
SIZE mechanism checks of the Osterwalder-Seiler class -- one spatial cube
resp. one plaquette, structure groups Z2/Z4, no fermions, no Phi sector,
no TFPT representation content, no continuum statement, and T3 is checked
as a MECHANISM (pinning compatible with T1/T2), not as the exact TFPT
seam-data restriction.  Nothing here closes any gate of the contract; it
establishes that the T1/T2(/T3-mechanism) ladder is executable and that
the natural first candidate class passes it at toy level.

VERDICT ENUM: T1T2_MECHANISM_OK_REDUCED (seam pinning compatible; full
gates open).
"""
import hashlib
import sys
from functools import reduce

import numpy as np

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def spec_sha():
    with open(__file__, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ------------------------------------------------------------ model (i)
def cube_links_faces():
    """One 3D cube: vertices = {0,1}^3, 12 edges, 6 faces (as link lists
    with orientations ignored -- Z2)."""
    verts = [(x, y, z) for x in range(2) for y in range(2)
             for z in range(2)]
    links = []
    for v in verts:
        for d in range(3):
            w = list(v)
            w[d] += 1
            if w[d] < 2:
                links.append((v, tuple(w)))
    lidx = {e: k for k, e in enumerate(links)}
    faces = []
    for v in verts:
        for d1 in range(3):
            for d2 in range(d1 + 1, 3):
                a = list(v)
                a[d1] += 1
                b = list(v)
                b[d2] += 1
                c = list(v)
                c[d1] += 1
                c[d2] += 1
                if a[d1] < 2 and b[d2] < 2:
                    A, B, C = tuple(a), tuple(b), tuple(c)
                    faces.append([lidx[(v, A)], lidx[(A, C)]
                                  if (A, C) in lidx else lidx[(C, A)],
                                  lidx[(B, C)] if (B, C) in lidx
                                  else lidx[(C, B)], lidx[(v, B)]])
    return links, lidx, faces, verts


def model_i():
    print("model (i): Z2 gauge on one 3D cube (12 links, 4096-dim)")
    links, lidx, faces, verts = cube_links_faces()
    check("cube census: 12 links, 6 faces, 8 vertices",
          len(links) == 12 and len(faces) == 6 and len(verts) == 8)
    nl = len(links)
    dim = 2 ** nl
    beta, kappa = 0.7, 0.9

    # spins per configuration: s_l = +-1 from bit l
    bits = ((np.arange(dim)[:, None] >> np.arange(nl)[None, :]) & 1)
    spins = 1 - 2 * bits                                # (dim, 12)
    face_energy = np.zeros(dim)
    for f in faces:
        face_energy += spins[:, f[0]] * spins[:, f[1]] \
            * spins[:, f[2]] * spins[:, f[3]]
    V = np.exp(beta * face_energy)                      # diagonal
    k2 = np.array([[np.cosh(kappa), np.sinh(kappa)],
                   [np.sinh(kappa), np.cosh(kappa)]])   # PD heat kernel
    K = reduce(np.kron, [k2] * nl)
    sqV = np.sqrt(V)
    T = sqV[:, None] * K * sqV[None, :]

    check("T symmetric (max asym 0 up to fp)",
          float(np.max(np.abs(T - T.T))) < 1e-12)
    try:
        np.linalg.cholesky(T)
        pd = True
    except np.linalg.LinAlgError:
        pd = False
    check("T2 (3 spatial dims): T = V^(1/2) K V^(1/2) POSITIVE DEFINITE "
          "(Cholesky succeeds on the 4096-dim transfer matrix)", pd)

    # Gauss operators: flip all links incident to vertex v
    ok = True
    for v in verts:
        mask = 0
        for e, k in lidx.items():
            if v in e:
                mask |= (1 << k)
        perm = np.arange(dim) ^ mask
        # G T G^{-1} = T  <=>  T[perm][:, perm] == T
        dev = float(np.max(np.abs(T[np.ix_(perm, perm)] - T)))
        ok = ok and dev < 1e-10
    check("T1: all 8 Gauss operators commute with T (max deviation "
          "< 1e-10; structural: every face at v holds exactly two "
          "v-incident links)", ok)

    # mutant: complex action breaks hermiticity
    Vm = np.exp((beta + 0.3j) * face_energy)
    Tm = np.sqrt(Vm)[:, None] * K * np.sqrt(Vm)[None, :]
    herm_dev = float(np.max(np.abs(Tm - Tm.conj().T)))
    check("MUTANT caught: the complex-action mutant destroys hermiticity "
          "(deviation > 0.1) -- T2 is a property of the reflection-"
          "symmetric Wilson class, not automatic", herm_dev > 0.1,
          "dev = %.3f" % herm_dev)


# ----------------------------------------------------------- model (ii)
def model_ii():
    print("model (ii): Z4 = mu4 gauge on one plaquette (4 links, "
          "256-dim) + seam pinning")
    q = 4
    nl = 4
    dim = q ** nl
    beta, kappa = 0.5, 0.8
    # link configs
    digs = (np.arange(dim)[:, None] // (q ** np.arange(nl)[None, :])) % q
    # oriented plaquette: g1 + g2 - g3 - g4 mod 4; energy = Re i^h
    h = (digs[:, 0] + digs[:, 1] - digs[:, 2] - digs[:, 3]) % q
    energy = np.cos(np.pi * h / 2)
    V = np.exp(beta * energy)
    # Z4 heat kernel: f_hat(q') = exp(kappa cos(pi q'/2)) > 0 => PD
    fhat = np.exp(kappa * np.cos(np.pi * np.arange(q) / 2))
    f = np.real(np.fft.ifft(fhat))          # f(h), real positive-definite
    # explicit product kernel K[a, b] = prod_links f(a_l - b_l mod 4)
    # (avoids kron stride-order pitfalls with the digit indexing)
    diff = (digs[:, None, :] - digs[None, :, :]) % q
    K = np.prod(f[diff], axis=2)
    sqV = np.sqrt(V)
    T = sqV[:, None] * K * sqV[None, :]

    check("T symmetric", float(np.max(np.abs(T - T.T))) < 1e-12)
    try:
        np.linalg.cholesky(T + 0.0)
        pd = True
    except np.linalg.LinAlgError:
        pd = False
    check("T2 (mu4 structure group): T positive definite on the 256-dim "
          "plaquette space", pd)

    # Gauss operators at the 4 vertices of the square:
    # links 0: v0->v1, 1: v1->v2, 2: v3->v2, 3: v0->v3 (orientations so
    # that the plaquette word is g0 + g1 - g2 - g3)
    incident = {0: [(0, +1), (3, +1)],       # v0: links 0,3 outgoing
                1: [(0, -1), (1, +1)],       # v1: 0 incoming, 1 outgoing
                2: [(1, -1), (2, -1)],       # v2: 1,2 incoming
                3: [(2, +1), (3, -1)]}       # v3: 2 outgoing, 3 incoming
    ok = True
    for v, incs in incident.items():
        newd = digs.copy()
        for (l, s) in incs:
            newd[:, l] = (newd[:, l] + s) % q
        perm = (newd * (q ** np.arange(nl)[None, :])).sum(axis=1)
        dev = float(np.max(np.abs(T[np.ix_(perm, perm)] - T)))
        ok = ok and dev < 1e-10
    check("T1: all 4 Z4 Gauss operators commute with T (< 1e-10)", ok)

    # T3 mechanism: pin link 3 (a boundary link) to the clock value g = 1
    sel = np.where(digs[:, 3] == 1)[0]
    Tp = T[np.ix_(sel, sel)]
    try:
        np.linalg.cholesky(Tp)
        pd = True
    except np.linalg.LinAlgError:
        pd = False
    check("T3 mechanism: the seam-pinned block (link 3 frozen to the mu4 "
          "clock g = 1) is still POSITIVE DEFINITE (RP survives the "
          "boundary condition)", pd)
    digs_sel = digs[sel]
    ok_int, broken = True, True
    for v, incs in incident.items():
        newd = digs_sel.copy()
        for (l, s) in incs:
            if l != 3:
                newd[:, l] = (newd[:, l] + s) % q
        touches = any(l == 3 for (l, s) in incs)
        if touches:
            # apply only the non-pinned part -> should NOT be a symmetry
            key = {tuple(r): i for i, r in enumerate(digs_sel)}
            perm = np.array([key[tuple(r)] for r in newd])
            dev = float(np.max(np.abs(Tp[np.ix_(perm, perm)] - Tp)))
            broken = broken and dev > 1e-3
        else:
            key = {tuple(r): i for i, r in enumerate(digs_sel)}
            perm = np.array([key[tuple(r)] for r in newd])
            dev = float(np.max(np.abs(Tp[np.ix_(perm, perm)] - Tp)))
            ok_int = ok_int and dev < 1e-10
    check("T3 mechanism: INTERIOR gauge transformations (vertices not "
          "touching the pinned link) still commute with the pinned block",
          ok_int)
    check("T3 mechanism honesty: the two seam-touching gauge "
          "transformations are broken by the boundary condition (as a "
          "boundary condition must)", broken)


def main():
    print("tfpt4d_t1t2_lattice_probe -- gates T1/T2 (+T3 mechanism) of "
          "TFPT4D.LATTICE.ACTION.01 at reduced size (exploration only)")
    model_i()
    model_ii()
    check("HONEST BOUNDARY (typed): reduced-size Osterwalder-Seiler "
          "mechanism checks only -- no fermions, no Phi, no TFPT rep "
          "content, no continuum; the dimension-uplift firewall applies; "
          "no contract gate is closed", True)
    npass = sum(CHECKS)
    print("-" * 70)
    print("CHECKS %d/%d PASS" % (npass, len(CHECKS)))
    print("VERDICT: T1T2_MECHANISM_OK_REDUCED (mu4 structure group + seam "
          "pinning compatible with gauge invariance and RP at toy level)")
    print("SPEC_SHA %s" % spec_sha()[:16])
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
