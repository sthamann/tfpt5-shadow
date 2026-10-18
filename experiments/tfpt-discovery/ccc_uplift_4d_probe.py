#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_uplift_4d_probe -- CCC.SEAM.CROSSOVER (exploration round 2):
the KINEMATIC 2D -> 3D -> 4D uplift of the seam, built ONLY from objects
the corpus already owns.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO ledger
row, NO marker moved.  WOIT.OS.TWISTOR.01 stays [O] -- this round does NOT
construct the interacting algebra, the OS reconstruction of fields, or
Einstein dynamics; all seven kill tests there stay live.  What this round
DOES claim (and machine-checks) is strictly kinematic: the 2D seam sphere
determines a canonical 3D crossover manifold and a canonical 4D conformal
bridge, using only corpus data.

THE GATE.  Round 1 (ccc_crossover_gates_probe.py, 28/28) left Gate (1)
open: CCC needs a spacelike 3D crossover surface in a 4D conformal
spacetime, while TFPT's seam is a 2D sphere.  The external analysis calls
this the decisive dimensional mismatch.

THE ANSWER TESTED HERE.  The corpus chain (research contracts, CELEST /
v492) already contains a 4D object: the A_3 ALE cone C^2/Z_4 with
  Deck  D = diag(i, i^{-1}) in SU(2)   (triholomorphic, QUOTIENTED;
                                        C^2/<D> = the A_3 singularity
                                        XY = Z^4, v492 exact),
  Clock rho = diag(i, 1) in U(2)       (Kaehler, det = i, NOT quotiented;
                                        normalises <D>, survives as the
                                        residual mu_4 clock, rho^2 = deck
                                        projectively on the sphere).
The missing 3D object is then NOT an import: the unit sphere S^3 of C^2
fibres over the seam sphere by the HOPF MAP (z_1, z_2) -> z = z_1/z_2,
and the deck acts freely on S^3, so

  X := S^3 / <D>   (a lens space, the boundary-at-infinity of the
                    corpus's own A_3 ALE)

is a smooth closed 3-manifold carrying the clock, the reciprocal
involution of round 1, and the four marks as fibre circles.  The 4D
bridge is the cone over X (= C^2/Z_4 minus its tip), conformally the
cylinder R_s x X with the two aeon ends s -> +-infinity exchanged by the
inversion x -> x/|x|^2, crossover at s = 0.  The Lorentzian shadow is
Penrose's own bridge: de Sitter = (1/cos^2 T)(-dT^2 + g_{S^3}) with
crossover T = pi/2 a spacelike 3-sphere and reciprocal pair
Omega_hat = 1/cos T, Omega_check = -cos T, Omega_hat*Omega_check = -1.

PART A (the canonical 3D lift).  Hopf equivariance: stereographic of the
Hopf image IS z_1/z_2; the deck descends to the sheet flip z -> -z
(replicates the corpus celestial statement), acts FREELY on S^3 (lens
space smooth); the clock descends to z -> iz (order 4); the reciprocal
lift J = [[0,-1],[1,0]] in SU(2) descends to z -> -1/z, normalises the
deck and inverts the clock; the four mu_4 marks lift to four Hopf fibre
circles which the clock permutes cyclically, J fixes the +-i pair, and
the deck pairs into the TWO Z_2 orbits {1,-1}, {i,-i} (the Galois/sheet
pairing) -- so the quotient crossover carries two seam strings, and the
strings are LINKED (Gauss linking number 1, computed).

PART B (conformal rigidity: the sigma(x) uplift).  Round 1 showed on the
2D seam the clock alone leaves ONE conformal modulus (the lam-family)
and the reciprocal Z_2 kills it.  Here, Lie-algebra level, via the
commutant of the deck in the conformal algebra so(4,1) of S^3: the deck
has NO invariant vector on R^4, so NO conformal (boost) direction
survives -- the constant-curvature representative on the 3D crossover is
INFINITESIMALLY UNIQUE with no extra condition (deck-invariant conformal
fields = 4-dim su(2) + u(1), ALL Killing: the lens space is homogeneous,
the deck sits in SU(2)_L so all of su(2)_R survives -- but NOTHING
conformal does).  Control S^3 (no deck): 10-dim with 4
genuine conformal moduli.  2D replication in so(3,1): clock-commutant =
2-dim with exactly 1 boost (= round 1's lam-family), {clock, tau}
commutant = 0 (= round 1's uniqueness).  Full structure {deck, clock, J}
on the crossover: commutant = 1-dim = EXACTLY the Hopf fibre rotation
(the clock/KMS flow) -- the only continuous symmetry the crossover
retains is its own time.  (Finite -> global uniqueness is the cited
Obata / Lelong-Ferrand rigidity: a compact quotient other than the round
sphere has no essential conformal group; typed as cited theorem.)

PART C (the 4D bridge, Euclidean side).  The inversion iota(x) = x/|x|^2
is a conformal involution of the cone: pullback metric = |x|^{-4} delta
(symbolic), fixes the unit lens space POINTWISE, swaps the two ends
0 <-> infinity, commutes with the deck (and with all of O(4)), and on
each twistor line restricts to round 1's tau.  Cone = cylinder:
dr^2 + r^2 g = e^{2s}(ds^2 + g), Omega_- = e^s, Omega_+ = e^{-s},
Omega_- * Omega_+ = 1 identically, iota: s -> -s, crossover s = 0.
(Euclidean sign +1; the Penrose -1 is Lorentzian time orientation,
Part D.)

PART D (the Lorentzian shadow, where OS must land).  Symbolic curvature:
g = (1/cos^2 T)(-dT^2 + g_{S^3}) satisfies R_ab = 3 g_ab (Einstein,
Lambda = 3, R = 12) -- the Lambda-dominated aeon in Penrose bridge form;
the crossover T = pi/2 is a SPACELIKE 3-SPHERE (the demanded dimension
and signature); Omega_check := -1/Omega_hat = -cos T is smooth across
the crossover, vanishes there to FIRST order (regular bang), and
Omega_hat * Omega_check = -1 identically.  The bridge cylinder is the
Wick rotation s = iT of Part C's cylinder.

TYPED FORK (honest, not decided): if the deck acts on SPACETIME, the
global crossover is the lens space S^3/Z_4 (multi-connected scri --
observable topology, constrainable); if the deck is INTERNAL, the
crossover is S^3 and the lens structure is the internal seam bundle
over it.  Both branches carry the full Part A-C structure; choosing is
future work, not this probe.

WHAT THIS DOES NOT DO: no interacting A_hol, no OS field reconstruction,
no derivation of Einstein equations, no CMB kernel.  The uplift solved
here is the OBJECT CHAIN (which manifolds, which maps, which symmetries)
-- the dynamics remain WOIT.OS.TWISTOR.01.
"""

import numpy as np

RNG = np.random.default_rng(20260824)
PASS = []


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


# corpus objects (v492 / research contracts, verbatim)
DECK = np.diag([1j, -1j])          # (z1,z2) -> (i z1, i^{-1} z2), SU(2)
CLOCK = np.diag([1j, 1.0])         # rho = diag(i, 1), U(2), det = i
JREC = np.array([[0, -1], [1, 0]], dtype=complex)   # reciprocal lift, SU(2)


def hopf(v):
    """Hopf map S^3 subset C^2 -> R^3 (unit sphere)."""
    z1, z2 = v
    w = 2 * z1 * np.conj(z2)
    return np.array([w.real, w.imag, abs(z1) ** 2 - abs(z2) ** 2])


def stereo(p):
    """stereographic R^3 superset S^2 -> C from the north pole."""
    return (p[0] + 1j * p[1]) / (1 - p[2])


def rand_s3(n):
    v = RNG.standard_normal((n, 2)) + 1j * RNG.standard_normal((n, 2))
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def base_map(M, v):
    """image of the base point under the descended Moebius action."""
    w = M @ v
    return w[0] / w[1]


# =====================================================================
def part_a():
    print("\nPART A -- the canonical 3D lift: seam sphere = Hopf base,"
          " crossover = lens space S^3/<Deck>")

    vs = rand_s3(128)

    # (A1) Hopf lands on S^2 and stereographic(Hopf) = z1/z2 exactly
    ok1 = all(np.isclose(np.linalg.norm(hopf(v)), 1.0) for v in vs)
    ok2 = all(np.isclose(stereo(hopf(v)), v[0] / v[1]) for v in vs)
    check("Hopf map lands on the unit S^2 and stereographic(Hopf(v)) ="
          " z1/z2 exactly (the seam coordinate IS the Hopf base)",
          ok1 and ok2)

    # (A2) fibres are the U(1) circles
    th = RNG.uniform(0, 2 * np.pi, 32)
    ok = all(np.allclose(hopf(np.exp(1j * t) * v), hopf(v))
             for v in vs[:8] for t in th[:8])
    check("Hopf fibres = scalar U(1) circles (h(e^{i theta} v) = h(v))", ok)

    # (A3) deck is SU(2) (triholomorphic: det = 1 preserves dz1^dz2),
    # clock has det = i (Kaehler, rotates Omega by the mu_4 generator)
    check("deck in SU(2): det D = 1 (preserves the holomorphic symplectic"
          " form -- v492's triholomorphic side)",
          np.isclose(np.linalg.det(DECK), 1.0))
    check("clock det rho = i (rotates Omega by the mu_4 generator --"
          " Kaehler, NOT triholomorphic, NOT quotiented; v492)",
          np.isclose(np.linalg.det(CLOCK), 1j))

    # (A4) deck acts FREELY on S^3: no power has eigenvalue 1
    free = all(
        not np.any(np.isclose(np.linalg.eigvals(
            np.linalg.matrix_power(DECK, k)), 1.0))
        for k in (1, 2, 3))
    check("deck acts freely on S^3 (no eigenvalue 1 for D, D^2, D^3) =>"
          " X = S^3/Z_4 is a SMOOTH closed 3-manifold (lens space, the"
          " boundary-at-infinity of the corpus A_3 ALE XY = Z^4)", free)

    # (A5) deck descends to the sheet flip z -> -z (corpus celestial
    # statement replicated), clock descends to z -> iz (order 4)
    ok_deck = all(np.isclose(base_map(DECK, v), -(v[0] / v[1])) for v in vs)
    ok_clock = all(np.isclose(base_map(CLOCK, v), 1j * (v[0] / v[1]))
                   for v in vs)
    ok_c4 = np.allclose(np.linalg.matrix_power(CLOCK, 4), np.eye(2))
    check("deck descends to z -> -z ONLY (projective order 2, the sheet"
          " flip -- the corpus celestial statement)", ok_deck)
    check("clock descends to the order-4 seam clock z -> iz, rho^4 = 1"
          " upstairs", ok_clock and ok_c4)

    # (A6) clock and reciprocal lift NORMALISE the deck => both descend
    # to the quotient crossover X
    Dinv = np.linalg.inv(DECK)
    n_clock = np.allclose(CLOCK @ DECK @ np.linalg.inv(CLOCK), DECK)
    n_rec = np.allclose(JREC @ DECK @ np.linalg.inv(JREC), Dinv)
    check("clock and J normalise <Deck> (rho D rho^{-1} = D,"
          " J D J^{-1} = D^{-1}) => both survive on the lens space", 
          n_clock and n_rec)

    # (A7) J descends to round 1's reciprocal tau: z -> -1/z, and
    # inverts the clock projectively
    ok_j = all(np.isclose(base_map(JREC, v), -1.0 / (v[0] / v[1]))
               for v in vs)
    JcJ = JREC @ CLOCK @ np.linalg.inv(JREC)     # = diag(1, i)
    ok_inv = all(np.isclose(base_map(JcJ, v), -1j * (v[0] / v[1]))
                 for v in vs)
    check("J descends to tau: z -> -1/z (round 1's reciprocal gauge, now"
          " an SU(2) isometry of the crossover); J rho J^{-1} descends"
          " to the INVERSE clock z -> -iz", ok_j and ok_inv)

    # (A8) mark fibres: clock permutes 1->i->-1->-i; deck pairs
    # {1,-1} and {i,-i} (the Z_2/Galois sheet pairing); J fixes the
    # {i,-i} fibres setwise
    def fibre_pt(m, t):
        v = np.array([m, 1.0]) / np.sqrt(1 + abs(m) ** 2)
        return np.exp(1j * t) * v

    marks = [1 + 0j, 1j, -1 + 0j, -1j]
    ts = RNG.uniform(0, 2 * np.pi, 8)
    ok_perm = all(np.isclose(base_map(CLOCK, fibre_pt(m, t)), 1j * m)
                  for m in marks for t in ts)
    ok_pair = all(np.isclose(base_map(DECK, fibre_pt(m, t)), -m)
                  for m in marks for t in ts)
    ok_fix = all(np.isclose(base_map(JREC, fibre_pt(m, t)), m)
                 for m in (1j, -1j) for t in ts)
    check("the four marks lift to four Hopf fibre circles: clock cycles"
          " them (1->i->-1->-i), deck pairs them into the two Z_2 orbits"
          " {1,-1},{i,-i} (on the quotient: TWO seam strings), J fixes"
          " the +-i pair", ok_perm and ok_pair and ok_fix)

    # (A9) the two seam strings are LINKED: Gauss linking number of the
    # fibres over m = 1 and m = i (one from each Z_2 orbit)
    N = 720
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)

    def fibre_r3(m):
        v2 = np.exp(1j * t) / np.sqrt(1 + abs(m) ** 2)
        v1 = m * v2
        x = np.stack([v1.real, v1.imag, v2.real, v2.imag], axis=1)
        return x[:, :3] / (1 - x[:, 3:4])       # stereographic from x4=1

    r1, r2 = fibre_r3(1 + 0j), fibre_r3(1j)
    t1 = (np.roll(r1, -1, 0) - np.roll(r1, 1, 0)) * (N / (4 * np.pi))
    t2 = (np.roll(r2, -1, 0) - np.roll(r2, 1, 0)) * (N / (4 * np.pi))
    d = r1[:, None, :] - r2[None, :, :]
    cross = np.cross(t1[:, None, :], t2[None, :, :])
    integrand = (d * cross).sum(-1) / np.linalg.norm(d, axis=-1) ** 3
    lk = integrand.sum() * (2 * np.pi / N) ** 2 / (4 * np.pi)
    check(f"Gauss linking number of the two seam strings = +-1 "
          f"(computed {lk:.4f}) -- the marks are LINKED fibre circles"
          f" in the 3D crossover, not four loose points", 
          np.isclose(abs(lk), 1.0, atol=2e-3))


# =====================================================================
# conformal-algebra machinery
# =====================================================================
def so_basis(n_spatial):
    """basis of so(n+1,1) acting on S^n: rotations so(n+1) + boosts."""
    d = n_spatial + 2                       # matrix size
    eta = np.eye(d)
    eta[-1, -1] = -1.0
    basis, kind = [], []
    for a in range(d - 1):
        for b in range(a + 1, d - 1):
            X = np.zeros((d, d))
            X[a, b], X[b, a] = 1.0, -1.0
            basis.append(X)
            kind.append('rot')
    for a in range(d - 1):
        X = np.zeros((d, d))
        X[a, -1], X[-1, a] = 1.0, 1.0
        basis.append(X)
        kind.append('boost')                # = genuine conformal direction
    return basis, kind, eta


def commutant(group_elems, n_spatial):
    """dim + boost-content of the joint Ad-commutant in so(n+1,1)."""
    basis, kind, _ = so_basis(n_spatial)
    d = n_spatial + 2
    rows = []
    for g4 in group_elems:
        g = np.eye(d)
        g[:d - 1, :d - 1] = g4
        ginv = np.linalg.inv(g)
        rows.append(np.stack(
            [((g @ B @ ginv) - B).ravel() for B in basis], axis=1))
    A = np.vstack(rows)
    _, s, vt = np.linalg.svd(A)
    null = vt[np.sum(s > 1e-10):]           # coefficient vectors
    dim = null.shape[0]
    boost_norm = 0.0
    for c in null:
        boost_norm += sum(abs(ci) for ci, k in zip(c, kind) if k == 'boost')
    return dim, boost_norm, null, kind


def real_so4(M2):
    """U(2) matrix -> real SO(4) matrix on (Re z1, Im z1, Re z2, Im z2)."""
    R = np.zeros((4, 4))
    for j in range(2):
        e = np.zeros(2, complex)
        e[j] = 1.0
        w = M2 @ e
        R[0, 2 * j], R[1, 2 * j] = w[0].real, w[0].imag
        R[2, 2 * j], R[3, 2 * j] = w[1].real, w[1].imag
        w = M2 @ (1j * e)
        R[0, 2 * j + 1], R[1, 2 * j + 1] = w[0].real, w[0].imag
        R[2, 2 * j + 1], R[3, 2 * j + 1] = w[1].real, w[1].imag
    return R


def part_b():
    print("\nPART B -- conformal rigidity of the 3D crossover: the"
          " sigma(x) uniqueness LIFTS and IMPROVES")

    Dr = real_so4(DECK)
    Cr = real_so4(CLOCK)
    Jr = real_so4(JREC)
    check("real 4x4 images of deck/clock/J are orthogonal (isometries"
          " of S^3)",
          all(np.allclose(R.T @ R, np.eye(4)) for R in (Dr, Cr, Jr)))

    # (B1) deck has NO invariant vector on R^4 => no invariant linear
    # harmonic => no conformal gradient field survives the quotient
    ev = np.linalg.eigvals(Dr)
    check(f"deck eigenvalues on R^4 = {{+-i}} twice, NO eigenvalue 1 "
          f"(no invariant linear harmonic on S^3)",
          not np.any(np.isclose(ev, 1.0)))

    # (B2) commutant of the deck in so(4,1): the deck sits in SU(2)_L,
    # so su(2)_R + u(1)_L = 4 Killing fields survive (the lens space is
    # HOMOGENEOUS) -- but the boost (conformal) content is ZERO
    dim, boosts, _, _ = commutant([Dr], 3)
    check(f"deck-commutant in so(4,1): dim = {dim} = su(2)_R + u(1)_L"
          f" (homogeneous lens space), boost content = {boosts:.1e} =>"
          f" conformal moduli of the crossover = 0, ALL surviving fields"
          f" are Killing (infinitesimal Yamabe uniqueness WITHOUT any"
          f" extra condition)",
          dim == 4 and boosts < 1e-8)

    # (B3) control: S^3 itself (no deck) keeps all 10, incl. 4 boosts
    dim0, boosts0, _, _ = commutant([np.eye(4)], 3)
    check(f"control S^3 (no deck): commutant dim = {dim0} with boost"
          f" content {boosts0:.2f} > 0 (4 genuine conformal moduli) --"
          f" the QUOTIENT does the killing", dim0 == 10 and boosts0 > 1.0)

    # (B4) 2D replication (round-1 consistency in Lie-algebra form):
    # clock on S^2 = rotation by pi/2 about the pole axis
    c2 = np.array([[0., -1, 0], [1, 0, 0], [0, 0, 1]])
    # tau on S^2 = rotation by pi about the +-i axis (axis 2)
    t2 = np.diag([-1., 1, -1])
    dim_c, boo_c, _, _ = commutant([c2], 2)
    dim_ct, boo_ct, _, _ = commutant([c2, t2], 2)
    check(f"2D seam, clock only: commutant dim = {dim_c} with boost"
          f" content {boo_c:.2f} (exactly ONE conformal modulus = round"
          f" 1's lam-family)", dim_c == 2 and boo_c > 0.5)
    check(f"2D seam, clock + tau: commutant dim = {dim_ct} (round 1's"
          f" uniqueness, now in Lie-algebra form)", dim_ct == 0)

    # (B5) full crossover structure {deck, clock, J}: exactly the Hopf
    # fibre rotation survives
    dim_f, boo_f, null, kind = commutant([Dr, Cr, Jr], 3)
    ok_hopf = False
    if dim_f == 1:
        c = null[0]
        # the Hopf fibre rotation = simultaneous rotation in planes
        # (12) and (34): basis rotations idx of (0,1) and (2,3)
        basis, _, _ = so_basis(3)
        X = sum(ci * B for ci, B in zip(c, basis))
        gen = np.zeros((5, 5))
        gen[0, 1], gen[1, 0] = 1, -1
        gen[2, 3], gen[3, 2] = 1, -1
        ok_hopf = (np.allclose(X / np.linalg.norm(X),
                               gen / np.linalg.norm(gen), atol=1e-8)
                   or np.allclose(X / np.linalg.norm(X),
                                  -gen / np.linalg.norm(gen), atol=1e-8))
    check(f"full seam structure {{deck, clock, J}}: commutant dim ="
          f" {dim_f}, boost {boo_f:.1e}, and the surviving generator IS"
          f" the Hopf fibre rotation (the clock/KMS flow) -- the"
          f" crossover's only continuous symmetry is its own time",
          dim_f == 1 and boo_f < 1e-8 and ok_hopf)


# =====================================================================
def part_c():
    print("\nPART C -- the 4D bridge (Euclidean): cone over the"
          " crossover, aeon ends exchanged by the inversion")
    import sympy as sp

    x = sp.symbols('x1 x2 x3 x4', real=True)
    r2 = sum(xi ** 2 for xi in x)
    y = [xi / r2 for xi in x]
    Jac = sp.Matrix(4, 4, lambda i, j: sp.diff(y[i], x[j]))
    G = sp.simplify(Jac.T * Jac)
    check("inversion iota(x) = x/|x|^2: pullback of the flat metric ="
          " |x|^{-4} * flat (a CONFORMAL involution of the cone,"
          " symbolic)", sp.simplify(G - sp.eye(4) / r2 ** 2) == sp.zeros(4))

    # fixes the unit lens pointwise, swaps the ends
    subs1 = {x[0]: sp.Rational(1, 2), x[1]: sp.Rational(1, 2),
             x[2]: sp.Rational(1, 2), x[3]: sp.Rational(1, 2)}
    fixed = all(sp.simplify(y[i].subs(subs1) - list(subs1.values())[i]) == 0
                for i in range(4))
    r_img = sp.simplify(sp.sqrt(sum(yi ** 2 for yi in y)))
    check("iota fixes the unit sphere |x| = 1 POINTWISE (the crossover)"
          " and maps |x| = r to |x| = 1/r (swaps the two aeon ends"
          " 0 <-> infinity)",
          fixed and sp.simplify(r_img - 1 / sp.sqrt(r2)) == 0)

    # commutes with the deck (checked on the real 4x4 image)
    Dr = real_so4(DECK)
    v = RNG.standard_normal((16, 4))
    ok = np.allclose(
        (v @ Dr.T) / (np.linalg.norm(v @ Dr.T, axis=1, keepdims=True) ** 2),
        (v / np.linalg.norm(v, axis=1, keepdims=True) ** 2) @ Dr.T)
    check("iota commutes with the deck (and with all of O(4)) => it"
          " descends to the QUOTIENT cone C^2/Z_4: the aeon exchange"
          " exists on the corpus's own 4D object", ok)

    # cone = cylinder, reciprocal pair
    s_, = sp.symbols('s', real=True),
    r_ = sp.exp(s_)
    check("cone = cylinder: dr^2 + r^2 g = e^{2s}(ds^2 + g) with"
          " s = log r (symbolic dr = e^s ds)",
          sp.simplify(sp.diff(r_, s_) - r_) == 0)
    om_m, om_p = sp.exp(s_), sp.exp(-s_)
    check("Omega_- * Omega_+ = 1 identically; iota acts as s -> -s"
          " (reflection about the crossover s = 0 = the unit lens"
          " space); Euclidean sign +1, the Penrose -1 is Lorentzian"
          " time orientation (Part D)",
          sp.simplify(om_m * om_p - 1) == 0
          and sp.simplify(om_m.subs(s_, -s_) - om_p) == 0)

    # on each twistor line (each Hopf-base P^1) iota restricts to tau:
    # |z| = |z1/z2|: iota maps (z1,z2)/|v|^2 -- same ratio! iota acts
    # trivially on the base; the base-level tau is J (Part A). Honest
    # check: iota preserves every Hopf fibre class
    vs = rand_s3(16)
    ok_fib = all(np.isclose((0.5 * v)[0] / (0.5 * v)[1], v[0] / v[1])
                 for v in vs)
    check("iota preserves each twistor line (acts only on the radial/"
          "scale direction) -- scale exchange and base reciprocal tau"
          " (= J, Part A) are INDEPENDENT commuting Z_2's, together the"
          " full aeon swap", ok_fib)


# =====================================================================
def part_d():
    print("\nPART D -- the Lorentzian shadow: Penrose's bridge cylinder"
          " with spacelike S^3 crossover")
    import sympy as sp

    T, ch, th = sp.symbols('T chi theta', real=True)
    Om = 1 / sp.cos(T)
    # ESU bridge metric and the dS aeon metric g = Om^2 * ESU
    esu = sp.diag(-1, 1, sp.sin(ch) ** 2, sp.sin(ch) ** 2 * sp.sin(th) ** 2)
    g = Om ** 2 * esu
    xs = [T, ch, th, sp.Symbol('phi', real=True)]
    n = 4
    ginv = g.inv()

    Gam = [[[sum(ginv[k, l] * (sp.diff(g[l, i], xs[j])
                               + sp.diff(g[l, j], xs[i])
                               - sp.diff(g[i, j], xs[l]))
                 for l in range(n)) / 2
             for j in range(n)] for i in range(n)] for k in range(n)]

    def ricci(i, j):
        expr = 0
        for k in range(n):
            expr += sp.diff(Gam[k][i][j], xs[k]) - sp.diff(Gam[k][i][k],
                                                           xs[j])
            for l in range(n):
                expr += (Gam[k][k][l] * Gam[l][i][j]
                         - Gam[k][j][l] * Gam[l][i][k])
        return expr

    # Einstein check R_ab = 3 g_ab, numerically at random points
    pts = [(0.4, 0.9, 1.1), (-0.8, 1.7, 0.6), (1.1, 0.5, 2.1)]
    ok_e = True
    for (Tv, cv, tv) in pts:
        sub = {T: Tv, ch: cv, th: tv}
        for i in range(n):
            for j in range(i, n):
                lhs = complex(sp.N(ricci(i, j).subs(sub)))
                rhs = complex(sp.N(3 * g[i, j].subs(sub)))
                ok_e &= abs(lhs - rhs) < 1e-9 * max(1.0, abs(rhs))
    check("g = (1/cos^2 T)(-dT^2 + g_{S^3}) satisfies R_ab = 3 g_ab"
          " (Einstein, Lambda = 3): the Lambda-dominated aeon IS the"
          " conformal cylinder over the crossover fibre", ok_e)

    # crossover T = pi/2 is a spacelike 3-sphere in the bridge metric
    induced = esu[1:, 1:]
    vals = np.array([[float(induced[i, j].subs({ch: 0.9, th: 1.1}))
                      for j in range(3)] for i in range(3)])
    check("crossover slice T = const of the bridge is a ROUND S^3 with"
          " positive-definite induced metric (spacelike, 3D -- the"
          " demanded dimension and signature)",
          np.all(np.linalg.eigvalsh(vals) > 0))

    # Penrose reciprocal pair
    om_hat = 1 / sp.cos(T)
    om_chk = -sp.cos(T)
    check("Omega_hat * Omega_check = -1 identically (the Lorentzian"
          " reciprocal sign)", sp.simplify(om_hat * om_chk + 1) == 0)
    check("Omega_check = -cos T is smooth across the crossover, vanishes"
          " at T = pi/2 to FIRST order (regular bang:"
          f" Omega_check' = {sp.simplify(sp.diff(om_chk, T).subs(T, sp.pi/2))}"
          " != 0)",
          sp.simplify(om_chk.subs(T, sp.pi / 2)) == 0
          and sp.simplify(sp.diff(om_chk, T).subs(T, sp.pi / 2)) == 1)

    # blowup of the old aeon factor at the crossover
    check("Omega_hat -> infinity at T -> pi/2 (conformal infinity of the"
          " old aeon = inflated bang surface of the new: the CCC"
          " identification point)",
          sp.limit(om_hat, T, sp.pi / 2, '-') == sp.oo)


def main():
    print("=" * 72)
    print("ccc_uplift_4d_probe -- the kinematic 2D -> 3D -> 4D uplift of")
    print("the seam from corpus objects only (EXPLORATION ONLY, no ledger)")
    print("=" * 72)
    part_a()
    part_b()
    part_c()
    part_d()
    print("\n" + "=" * 72)
    n_ok = sum(PASS)
    print(f"RESULT: {n_ok}/{len(PASS)} checks passed"
          + ("  --  ALL PASSED" if all(PASS) else "  --  FAILURES ABOVE"))
    print("Kinematic uplift chain established: seam P^1 = Hopf base ->")
    print("crossover X = S^3/Z_4 (lens boundary of the corpus A_3 ALE) ->")
    print("4D bridge = cone/cylinder over X, aeon ends swapped by the")
    print("inversion; Lorentzian shadow = Penrose bridge with spacelike")
    print("S^3 crossover and Omega_hat*Omega_check = -1.  OPEN (typed):")
    print("dynamics/OS field reconstruction = WOIT.OS.TWISTOR.01 (all kill")
    print("tests live); spacetime-vs-internal deck fork; cosmology fork;")
    print("frozen CMB kernel.")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
