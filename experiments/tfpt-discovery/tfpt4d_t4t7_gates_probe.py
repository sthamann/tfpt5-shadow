#!/usr/bin/env python3
"""tfpt4d_t4t7_gates_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (TFPT4D.LATTICE.ACTION.01 [O], continuing the T1/T2/T3
mechanism probe): are the remaining four finite gates T4-T7 of the
contract EXECUTABLE -- i.e. does each admit a machine-checkable test at
reduced size, with teeth?  Together with tfpt4d_t1t2_lattice_probe this
makes the full T1-T7 harness executable.

  T4  ANOMALY BOOKKEEPING, EXACT (the actual TFPT content, not a toy):
      one SM generation (hypercharge normalisation Y(Q) = 1/6):
      [U(1)]^3, [SU(2)]^2 U(1), [SU(3)]^2 U(1), grav^2 U(1) all vanish
      as exact rationals, and the WITTEN SU(2) count is 4 doublets
      (3 color + 1 lepton) = even.  MUTANT: a leptoquark-less mutant
      (drop the lepton doublet) breaks three sums and makes the Witten
      count odd.
  T5  INDEX/GENERATION MECHANISM (2D overlap, executable): on an N x N
      torus with U(1) background flux q, the overlap operator
      D_ov = 1 + gamma_5 sgn(H_W) reproduces the index theorem
      index(D_ov) = q (orientation convention) for q = -2..2 (Wilson
      mass 0 < m0 < 2) -- the lattice mechanism by which the contract's
      T5 gate counts chiral zero modes; at q = 0 the free periodic
      doublet is chirality-paired (index 0).  (The 4D TFPT index count
      itself stays open.)
  T6  MIRROR SEPARATION (same operator): all D_ov eigenvalues lie on the
      Ginsparg-Wilson circle |lambda - 1| = 1 (machine precision), zero
      modes have definite chirality, and the doubler branch sits at the
      cutoff end (Re lambda near 2) with a clean spectral gap above the
      physical zero modes -- mirrors separated, not deleted.
  T7  NONVANISHING CONNECTED FOUR-POINT (Z2 cube, exact enumeration):
      for the four lateral faces of the single 3D cube at beta = 0.4 the
      connected 4-point kappa_4 != 0, while the free/product control
      beta = 0 gives kappa_4 = 0 exactly -- the theory-vs-generalized-
      free discriminator of the contract, executable.

HONEST BOUNDARY (dimension-uplift firewall): T4 is exact bookkeeping of
the actual one-generation content; T5/T6 are the 2D overlap MECHANISM
(not the 4D TFPT operator); T7 is a Z2 toy at one cube.  No gate of the
contract CLOSES here; the deliverable is that all seven gates now have
executable finite tests with mutants.

VERDICT ENUM: T4_EXACT + T5T6_MECHANISM_OK_2D + T7_TOY_OK
(contract stays [O]).
"""
from fractions import Fraction as F
from itertools import product as iproduct

import numpy as np

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


# ======================================================================
# T4: exact anomaly bookkeeping, one SM generation
# ======================================================================
print("=== T4: anomaly bookkeeping (exact, actual TFPT content) ===")
# fields: (name, color dim, SU2 dim, hypercharge Y) -- left-handed Weyl
GEN = [
    ("Q",   3, 2, F(1, 6)),
    ("u^c", 3, 1, F(-2, 3)),
    ("d^c", 3, 1, F(1, 3)),
    ("L",   1, 2, F(-1, 2)),
    ("e^c", 1, 1, F(1, 1)),
]


def anomaly_sums(fields):
    y3 = sum(c * w * y ** 3 for _, c, w, y in fields)
    su2y = sum(c * y for _, c, w, y in fields if w == 2)      # T(2)=1/2 common
    su3y = sum(w * y for _, c, w, y in fields if c == 3)      # T(3)=1/2 common
    grav = sum(c * w * y for _, c, w, y in fields)
    witten = sum(c for _, c, w, y in fields if w == 2)        # of SU(2) doublets
    return y3, su2y, su3y, grav, witten


y3, su2y, su3y, grav, witten = anomaly_sums(GEN)
rep("T4 [exact]: [U(1)]^3 = %s, [SU(2)]^2U(1) = %s, [SU(3)]^2U(1) = %s, "
    "grav^2 U(1) = %s -- all vanish" % (y3, su2y, su3y, grav),
    y3 == su2y == su3y == grav == 0)
rep("T4 WITTEN [exact]: %d SU(2) doublets per generation (3 color + 1 "
    "lepton) -- even, no global anomaly" % witten, witten % 2 == 0)
y3m, su2ym, su3ym, gravm, wittenm = anomaly_sums(
    [f for f in GEN if f[0] != "L"])
rep("T4 MUTANT FIRES: dropping the lepton doublet breaks [U(1)]^3, "
    "[SU(2)]^2U(1), grav and makes the Witten count odd",
    y3m != 0 and su2ym != 0 and gravm != 0 and wittenm % 2 == 1)

# ======================================================================
# T5/T6: 2D overlap index + mirror separation
# ======================================================================
print("=== T5/T6: 2D overlap index theorem + GW circle (mechanism) ===")
N = 8
M0 = 1.0     # Wilson mass, 0 < m0 < 2 selects the physical branch
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)


def links_flux(q):
    """uniform U(1) flux q on the N x N torus: constant plaquette phase
    2 pi q / N^2."""
    Ux = np.ones((N, N), dtype=complex)
    Uy = np.ones((N, N), dtype=complex)
    for x in range(N):
        for y_ in range(N):
            Uy[x, y_] = np.exp(2j * np.pi * q * x / N ** 2)
            if x == N - 1:
                Ux[x, y_] = np.exp(-2j * np.pi * q * y_ / N)
    return Ux, Uy


def overlap(q):
    dim = N * N
    idx = lambda x, y_: (x % N) * N + (y_ % N)
    Tx = np.zeros((dim, dim), dtype=complex)
    Ty = np.zeros((dim, dim), dtype=complex)
    Ux, Uy = links_flux(q)
    for x in range(N):
        for y_ in range(N):
            Tx[idx(x + 1, y_), idx(x, y_)] = Ux[x, y_]
            Ty[idx(x, y_ + 1), idx(x, y_)] = Uy[x, y_]
    I = np.eye(dim)
    DW = np.zeros((2 * dim, 2 * dim), dtype=complex)
    for S, T in ((S1, Tx), (S2, Ty)):
        DW += np.kron(S, (T - T.conj().T) / 2)
        DW += np.kron(np.eye(2), -(T + T.conj().T - 2 * I) / 2)
    HW = np.kron(S3, np.eye(dim)) @ (DW - M0 * np.eye(2 * dim))
    HW = (HW + HW.conj().T) / 2
    w, v = np.linalg.eigh(HW)
    sgn = v @ np.diag(np.sign(w)) @ v.conj().T
    Dov = np.eye(2 * dim) + np.kron(S3, np.eye(dim)) @ sgn
    return Dov


g5 = None
idx_results = {}
for q in (-2, -1, 0, 1, 2):
    Dov = overlap(q)
    dim2 = Dov.shape[0]
    g5 = np.kron(S3, np.eye(dim2 // 2))
    # index = -(1/2) Tr[g5 (2 - Dov)] ... use zero-mode counting:
    w, v = np.linalg.eig(Dov)
    zero = np.abs(w) < 1e-8
    nz = int(np.sum(zero))
    chir = 0
    for i in np.where(zero)[0]:
        vec = v[:, i]
        chir += float(np.real(vec.conj() @ (g5 @ vec)))
    idx_results[q] = (nz, round(chir))
print("   flux -> (zero modes, summed chirality):", idx_results)
rep("T5 [mechanism]: index(D_ov) = q for q = -2..2 in this orientation "
    "convention (chirality-summed zero modes = the background flux; at "
    "q = 0 the free periodic doublet gives a chirality-PAIRED pair, "
    "index 0 -- consistent)",
    all(idx_results[q][1] == q for q in idx_results))

Dov1 = overlap(1)
w1 = np.linalg.eigvals(Dov1)
on_circle = np.max(np.abs(np.abs(w1 - 1) - 1))
nonzero = np.sort(np.abs(w1))[int(np.sum(np.abs(w1) < 1e-8)):]
doublers = int(np.sum(np.real(w1) > 1.5))
rep("T6 [mechanism]: all eigenvalues on the GW circle |lambda - 1| = 1 "
    "(max dev %.1e); gap above the physical zero modes (min nonzero "
    "|lambda| = %.3f); doubler branch at the cutoff end (%d modes with "
    "Re > 1.5) -- mirrors separated, not deleted"
    % (on_circle, nonzero[0], doublers),
    on_circle < 1e-8 and nonzero[0] > 0.05 and doublers > 0)

# ======================================================================
# T7: connected 4-point on the Z2 cube (exact enumeration)
# ======================================================================
print("=== T7: connected 4-point, Z2 gauge on one cube ===")
# cube vertices (x,y,z) in {0,1}^3; 12 links; 6 faces
verts = list(iproduct((0, 1), repeat=3))
links = []
for v_ in verts:
    for d in range(3):
        if v_[d] == 0:
            w_ = list(v_)
            w_[d] = 1
            links.append((v_, tuple(w_)))
lidx = {frozenset(l): i for i, l in enumerate(links)}


def face_links(fixed_dim, fixed_val):
    dims = [d for d in range(3) if d != fixed_dim]
    c = [0, 0, 0]
    c[fixed_dim] = fixed_val
    out = []
    for da, db in ((0, 0), (0, 1), (1, 0), (1, 1)):
        pass
    # four boundary links of the square
    def pt(a, b):
        p = list(c)
        p[dims[0]], p[dims[1]] = a, b
        return tuple(p)
    for a, b, a2, b2 in ((0, 0, 1, 0), (1, 0, 1, 1), (0, 1, 1, 1),
                         (0, 0, 0, 1)):
        out.append(lidx[frozenset((pt(a, b), pt(a2, b2)))])
    return out


faces = [face_links(d, v_) for d in range(3) for v_ in (0, 1)]
lateral = [faces[i] for i in (0, 1, 2, 3)]     # 4 faces around axis z=dim 2


def four_point(beta):
    Z = 0.0
    m1 = np.zeros(4)
    m2 = np.zeros((4, 4))
    m4 = 0.0
    for cfg in range(4096):
        s = [1 if (cfg >> i) & 1 else -1 for i in range(12)]
        fvals = [np.prod([s[i] for i in f]) for f in faces]
        w_ = np.exp(beta * sum(fvals))
        Z += w_
        lat = np.array([np.prod([s[i] for i in f]) for f in lateral],
                       dtype=float)
        m1 += w_ * lat
        m2 += w_ * np.outer(lat, lat)
        m4 += w_ * np.prod(lat)
    m1 /= Z
    m2 /= Z
    m4 /= Z
    # connected 4-point (cumulant) for centred variables
    c2 = m2 - np.outer(m1, m1)
    # centred fourth moment: enumerate again for exact centred product
    m4c = 0.0
    Z2 = 0.0
    for cfg in range(4096):
        s = [1 if (cfg >> i) & 1 else -1 for i in range(12)]
        fvals = [np.prod([s[i] for i in f]) for f in faces]
        w_ = np.exp(beta * sum(fvals))
        lat = np.array([np.prod([s[i] for i in f]) for f in lateral],
                       dtype=float) - m1
        m4c += w_ * np.prod(lat)
        Z2 += w_
    m4c /= Z2
    kappa4 = m4c - (c2[0, 1] * c2[2, 3] + c2[0, 2] * c2[1, 3]
                    + c2[0, 3] * c2[1, 2])
    return kappa4


k4_int = four_point(0.4)
k4_free = four_point(0.0)
rep("T7 [toy]: connected 4-point of the four lateral faces kappa_4 = "
    "%.3e != 0 at beta = 0.4, while the free/product control beta = 0 "
    "gives %.1e = 0 -- the generalized-free discriminator executable"
    % (k4_int, k4_free),
    abs(k4_int) > 1e-6 and abs(k4_free) < 1e-12)

print()
print("VERDICT: T4_EXACT + T5T6_MECHANISM_OK_2D + T7_TOY_OK -- together "
      "with tfpt4d_t1t2_lattice_probe the full T1-T7 harness is "
      "executable at finite size; TFPT4D.LATTICE.ACTION.01 stays [O]")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
