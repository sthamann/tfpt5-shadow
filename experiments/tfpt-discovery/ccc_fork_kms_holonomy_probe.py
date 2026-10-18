#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_fork_kms_holonomy_probe -- CCC.SEAM.CROSSOVER (exploration round 3):
the three targets named by round DLI, executed -- (A) the deck fork priced
against CMB topology constraints, (B) GLOBAL Yamabe uniqueness on the
crossover + the KMS/clock normalisation, (C) the holonomy dictionary of
the seam strings (Z_4 monodromy vs the v522 GSO Z_2).

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO
ledger row, NO marker moved.  WOIT.OS.TWISTOR.01 stays [O] (all kill
tests live); the cyclic reading stays [C]; nothing here claims CCC
follows from TFPT.  External data in Part A are quoted with sources and
typed as external.

PART A (the deck fork, priced).  Round DLI left a typed fork: deck acts
on SPACETIME (global crossover = lens space S^3/Z_4, multi-connected
scri) vs deck INTERNAL (crossover S^3, lens structure = internal seam
bundle).  Pricing against data [external inputs, typed]:
  - Planck 2018 (TT,TE,EE+lowE+lensing+BAO): Omega_K = 0.0007 +/- 0.0019
    => closed-side 95% bound |Omega_K| <= 0.0031
    => curvature radius R_c >= D_H/sqrt(0.0031) = 17.96 D_H.
  - Comoving distance to last scattering chi_rec ~= 3.17 D_H
    (z ~ 1090, standard LCDM).
  - Matched-circle searches (Cornish-Spergel-Starkman; Planck XVIII/
    XXVI): detectable only if the shortest closed geodesic
    l_min < 2 chi_rec.
For L(4): l_min = (2 pi R_c)/4 = (pi/2) R_c >= 28.2 D_H, while
2 chi_rec = 6.34 D_H -- ratio >= 4.45: the lens branch predicts NO
matched circles under current curvature bounds (consistent with the
null searches), and would become topology-detectable only at
|Omega_K| >= (pi/(4 chi_rec/D_H))^2 = 0.061, which is ~32 sigma against
the measurement.  VERDICT (typed): the fork is EMPIRICALLY UNDECIDABLE
by topology searches -- both branches stay alive; the decision must be
theoretical (or the fork is harmless: the two branches differ by no
current observable).  Same conclusion a fortiori for the Z_8 spin tower.

PART B (global Yamabe uniqueness + KMS normalisation).  Round DLI proved
the INFINITESIMAL statement (deck-commutant boost content = 0).  Here
the GLOBAL solution manifold: by Obata's theorem (cited) the constant-
scalar-curvature representatives in the conformal class of round S^3
are EXACTLY the conformal-group orbit of the round metric -- the boost
family Omega_{n,beta}(x) = 1/(gamma(1 + beta n.x)).  Machine checks:
the boost maps S^3 -> S^3 conformally (numeric Jacobian isotropy); a
boosted representative is deck-invariant iff its axis n is a deck-
invariant vector, and the deck has NONE -- numerically the deck-
invariance defect is bounded away from zero over a full axis scan for
every beta > 0, and vanishes only at beta = 0.  Hence, WITHIN the
complete Obata solution manifold, exactly ONE point is deck-invariant:
the round representative.  The 2D->3D contrast of round DL/DLI is
replicated globally.  KMS/CLOCK NORMALISATION: in the round
representative every Hopf/clock orbit has the SAME period (2 pi
upstairs; numeric spread ~ 1e-15), while every boosted representative
gives POSITION-DEPENDENT clock periods (spread > 0) -- i.e. the unique
deck-invariant Yamabe representative is exactly the one in which the
seam KMS flow has a globally well-defined period.  "The clock ticks
uniformly" IS the normalisation that picks sigma == 1; v_geo then only
converts the period into seconds (VGEO.TORSOR.01, unchanged).

PART C (the holonomy dictionary).  pi_1(X) = Z_4 = <Deck>, and the
corpus glue is the flat Z_4 monodromy at infinity (v492, character
chi(D) = i).  Machine checks via explicit path lifts on S^3:
  - POLE STRINGS: the two clock fixed circles {z_2 = 0}, {z_1 = 0}
    (the aeon poles 0, infinity of rounds DL/DLI) descend to the two
    CORE GEODESICS of the lens space, length (2 pi)/4; the lift path
    (e^{i theta}, 0), theta in [0, pi/2] ends at D.(1,0) => class
    D in pi_1 => holonomy chi(D) = i: the pole strings carry the FULL
    order-4 mu_4 monodromy.
  - MARK STRINGS: a Hopf fibre over a mark closes in X after theta =
    pi (the lift ends at -v = D^2 v) => class D^2 => holonomy
    chi(D^2) = -1: EVERY seam string over the base carries exactly the
    2-torsion Z_2.  And D^2 = -1 on C^2 acts TRIVIALLY on the base
    while flipping the spinor coordinates -- the v522 statement "the
    gaugeable part of the tower is EXACTLY its 2-torsion {1, (-1)^F};
    the full wrap = the 2 pi rotation of the seam = fermion parity"
    becomes geometric: THE GSO/FERMION-PARITY Z_2 IS THE HOLONOMY
    AROUND THE SEAM STRINGS.  (Typed [C]-level structural
    correspondence -- v522's algebraic object and this geometric one
    share the same group element; no dynamical identification claimed.)
  - LINKING: every mark string links each pole string once (Gauss
    integral) -- the Z_2 flux is threaded by the order-4 axes.
  - The generic-fibre control: fibres over non-mark points carry the
    same class D^2 (the marks are distinguished by SYMMETRY -- clock
    orbit + J-pairing, round DLI -- not by holonomy), stated honestly.

PART D (the cosmology fork, priced -- the opposite of Part A).  Gate 5
of the external analysis: Starobinsky inflation vs CCC gravitational-
wave epoch vs hybrid -- exactly one active story.  Pricing [external
data typed]: the corpus Starobinsky branch predicts n_s = 1 - 2/N_star,
r = 12/N_star^2; over the corpus band N_star in [50, 60] this gives
n_s in [0.960, 0.967] (consistent with Planck n_s = 0.9649 +/- 0.0042)
and r in [0.0033, 0.0048] -- BELOW the current bound r < 0.036
(BICEP/Keck+Planck) but ABOVE the ~0.001 sensitivity of LiteBIRD /
CMB-S4.  VERDICT (typed): unlike the deck fork, the cosmology fork IS
empirically decidable within ~a decade: r detected at 0.003-0.005 =>
the Starobinsky branch wins and the CCC branch must reproduce the
tensor signal from crossover dynamics or die; r < 0.001 => the
Starobinsky branch dies and the CCC/hybrid branch is forced.  TFPT
does not get to keep both stories past that measurement.

WHAT STAYS OPEN: the dynamics (WOIT gamma); the frozen CMB kernel; the
theoretical decision of the deck fork (Part A shows data will not
decide it); the cosmology-fork decision itself (Part D shows data WILL).
"""

import numpy as np

RNG = np.random.default_rng(20260824)
PASS = []


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


DECK = np.diag([1j, -1j])


def real_so4(M2):
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


DR = real_so4(DECK)


# =====================================================================
def part_a():
    print("\nPART A -- the deck fork priced against CMB topology"
          " constraints (external data typed)")

    # EXTERNAL DATA (typed, not TFPT outputs):
    # Planck 2018 VI (TT,TE,EE+lowE+lensing+BAO): Omega_K = 0.0007+-0.0019
    OMK_CENTRAL, OMK_SIGMA = 0.0007, 0.0019
    omk95 = abs(OMK_CENTRAL - 2 * OMK_SIGMA)      # closed-side 95% bound
    # comoving distance to last scattering in Hubble units (z ~ 1090):
    CHI_REC = 3.17                                 # ~14.0 Gpc / 4.42 Gpc

    r_c = 1.0 / np.sqrt(omk95)                     # min curvature radius
    check(f"closed-side 95% curvature bound |Omega_K| <= {omk95:.4f} =>"
          f" R_c >= {r_c:.2f} D_H (Planck 2018, typed external)",
          np.isclose(omk95, 0.0031) and r_c > 17.9)

    # L(4): shortest closed geodesic = (2 pi R_c)/4
    l_min = (np.pi / 2) * r_c
    detect = 2 * CHI_REC
    ratio = l_min / detect
    check(f"L(4) shortest closed geodesic >= {l_min:.1f} D_H vs matched-"
          f"circle reach 2 chi_rec = {detect:.2f} D_H (ratio {ratio:.2f})"
          f" => the lens branch predicts NO matched circles (consistent"
          f" with the null searches)", ratio > 4.0)

    # detectability threshold and its tension with the measurement
    omk_needed = (np.pi / (4 * CHI_REC)) ** 2
    tension = (omk_needed - abs(OMK_CENTRAL)) / OMK_SIGMA
    check(f"topology-detectability would need |Omega_K| >="
          f" {omk_needed:.4f} -- {tension:.0f} sigma against the"
          f" measurement => the fork is EMPIRICALLY UNDECIDABLE by"
          f" topology searches; both branches stay alive (typed verdict:"
          f" data_limited)", omk_needed > 0.05 and tension > 25)

    # a fortiori for the Z_8 spin tower (shorter geodesic by 2, still
    # far beyond reach)
    l8 = (np.pi / 4) * r_c
    check(f"Z_8 spin tower: l_min >= {l8:.1f} D_H, still"
          f" {l8 / detect:.2f} x beyond matched-circle reach (a fortiori"
          f" undecidable)", l8 / detect > 2.0)


# =====================================================================
# boost conformal maps of S^3 (the Obata solution manifold)
# =====================================================================
def boost(x, n, beta):
    """conformal diffeo of S^3 from the SO(4,1) boost along n; returns
    (image point y, conformal factor Omega = 1/t')."""
    gamma = 1.0 / np.sqrt(1 - beta ** 2)
    xn = x @ n
    tprime = gamma * (1 + beta * xn)
    y = (x - np.outer(xn, n) + np.outer(gamma * (xn + beta), n)) / \
        tprime[:, None]
    return y, 1.0 / tprime


def rand_s3_real(k):
    v = RNG.standard_normal((k, 4))
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def part_b():
    print("\nPART B -- GLOBAL Yamabe uniqueness on the crossover + the"
          " KMS/clock normalisation")

    xs = rand_s3_real(64)
    n = RNG.standard_normal(4)
    n /= np.linalg.norm(n)
    beta = 0.4

    # (B1) boost maps S^3 -> S^3
    y, om = boost(xs, n, beta)
    check("the SO(4,1) boost maps S^3 to S^3 (|y| = 1 on samples)",
          np.allclose(np.linalg.norm(y, axis=1), 1.0))

    # (B2) conformality: the numeric differential is isotropic with
    # factor Omega (two independent tangent directions agree)
    ok_conf = True
    eps = 1e-6
    for x in xs[:12]:
        # two orthonormal tangents at x
        u = RNG.standard_normal(4)
        u -= (u @ x) * x
        u /= np.linalg.norm(u)
        w = RNG.standard_normal(4)
        w -= (w @ x) * x + (w @ u) * u
        w /= np.linalg.norm(w)
        x0 = x[None, :]
        for tvec in (u, w):
            p_, _ = boost((x0 + eps * tvec) /
                          np.linalg.norm(x0 + eps * tvec), n, beta)
            m_, _ = boost((x0 - eps * tvec) /
                          np.linalg.norm(x0 - eps * tvec), n, beta)
            speed = np.linalg.norm(p_ - m_) / (2 * eps)
            _, om0 = boost(x0, n, beta)
            ok_conf &= abs(speed - om0[0]) < 5e-5
    check("the boost is CONFORMAL: numeric differential isotropic with"
          " factor Omega(x) = 1/(gamma(1 + beta n.x)) -- the Obata"
          " solution family realised explicitly", ok_conf)

    # (B3) deck invariance of the boosted representative fails for
    # EVERY axis n (deck has no invariant vector): full axis scan
    def deck_defect(nvec, b):
        _, om1 = boost(xs, nvec, b)
        _, om2 = boost(xs @ DR.T, nvec, b)
        return float(np.max(np.abs(om1 - om2)))

    defects = []
    for _ in range(200):
        nv = RNG.standard_normal(4)
        nv /= np.linalg.norm(nv)
        defects.append(deck_defect(nv, beta))
    defects = np.array(defects)
    d_round = deck_defect(n, 0.0)
    check(f"deck-invariance defect over a 200-axis scan at beta = 0.4:"
          f" min = {defects.min():.4f} > 0 (NO escape axis -- the deck"
          f" has no invariant vector); at beta = 0 the defect is"
          f" {d_round:.1e}", defects.min() > 1e-3 and d_round < 1e-12)

    # (B4) defect scales to zero ONLY as beta -> 0 (the unique point of
    # the solution manifold)
    betas = np.linspace(0.0, 0.8, 17)
    dvals = np.array([deck_defect(n, b) for b in betas])
    check("deck-defect along the boost ray: zero at beta = 0, strictly"
          " increasing in beta -- within Obata's COMPLETE solution"
          " manifold exactly one deck-invariant point exists: the round"
          " representative (global uniqueness, Obata cited)",
          dvals[0] < 1e-12 and np.all(np.diff(dvals) > 0))

    # (B5) KMS/clock normalisation: Hopf-orbit periods.  Length of the
    # clock orbit through v in the representative Omega^2 g:
    # L(v) = int_0^{2pi} Omega(e^{i theta} v) d theta
    def orbit_lengths(nvec, b, k=8, m=512):
        th = np.linspace(0, 2 * np.pi, m, endpoint=False)
        out = []
        for _ in range(k):
            v = RNG.standard_normal(2) + 1j * RNG.standard_normal(2)
            v /= np.linalg.norm(v)
            orbit = np.stack([
                np.stack([(np.exp(1j * t) * v)[0].real,
                          (np.exp(1j * t) * v)[0].imag,
                          (np.exp(1j * t) * v)[1].real,
                          (np.exp(1j * t) * v)[1].imag]) for t in th])
            _, om_ = boost(orbit, nvec, b)
            out.append(om_.mean() * 2 * np.pi)
        return np.array(out)

    L_round = orbit_lengths(n, 0.0)
    L_boost = orbit_lengths(n, beta)
    spread_r = float(L_round.max() - L_round.min())
    spread_b = float(L_boost.max() - L_boost.min())
    check(f"round representative: ALL clock orbits have the same period"
          f" 2 pi (spread {spread_r:.1e}); boosted representative:"
          f" position-dependent periods (spread {spread_b:.3f}) => the"
          f" unique deck-invariant representative is EXACTLY the one"
          f" with a globally well-defined KMS period -- 'the clock ticks"
          f" uniformly' IS the sigma == 1 normalisation; v_geo only"
          f" converts the period into units",
          spread_r < 1e-10 and spread_b > 0.05
          and np.allclose(L_round, 2 * np.pi))


# =====================================================================
def part_c():
    print("\nPART C -- the holonomy dictionary: pole strings carry the"
          " mu_4, seam strings carry the GSO Z_2")

    # flat Z_4 monodromy character of the corpus glue (v492): chi(D) = i
    chi = {0: 1, 1: 1j, 2: -1, 3: -1j}

    # (C1) pole string: lift path (e^{i theta}, 0), theta in [0, pi/2]
    v0 = np.array([1.0, 0.0], dtype=complex)
    end = np.array([np.exp(1j * np.pi / 2), 0.0])
    check("pole-string lift ends at D.(1,0) exactly => class D in"
          " pi_1(X) = Z_4 => holonomy chi(D) = i: the two aeon-pole"
          " core geodesics carry the FULL order-4 mu_4 monodromy",
          np.allclose(end, DECK @ v0) and chi[1] == 1j)

    # (C2) pole strings have quotient length 2 pi / 4 (quarter fibre)
    check("pole strings close after theta = pi/2 (quotient length"
          " (2 pi)/4 -- the deck acts with full order 4 on the pole"
          " circles)", np.allclose(np.linalg.matrix_power(DECK, 4),
                                   np.eye(2))
          and not np.allclose(DECK @ v0, v0))

    # (C3) mark string: lift along the fibre over m = 1 ends at -v =
    # D^2 v after theta = pi => class D^2 => holonomy -1
    m = 1 + 0j
    v = np.array([m, 1.0]) / np.sqrt(2)
    end = np.exp(1j * np.pi) * v
    check("mark-string lift ends at -v = D^2 v after theta = pi =>"
          " class D^2 => holonomy chi(D^2) = -1: every seam string"
          " carries EXACTLY the 2-torsion Z_2",
          np.allclose(end, np.linalg.matrix_power(DECK, 2) @ v)
          and chi[2] == -1)

    # (C4) D^2 = -1 on C^2: trivial on the base, spinor flip upstairs
    D2 = np.linalg.matrix_power(DECK, 2)
    vs = RNG.standard_normal((16, 2)) + 1j * RNG.standard_normal((16, 2))
    base_triv = all(np.isclose((D2 @ v)[0] / (D2 @ v)[1], v[0] / v[1])
                    for v in vs)
    check("D^2 = -1 acts TRIVIALLY on the seam base and as the 2 pi"
          " spinor flip upstairs -- v522's 'gaugeable datum = the"
          " 2-torsion {1, (-1)^F}; full wrap = fermion parity' becomes"
          " geometric: THE GSO Z_2 IS THE STRING HOLONOMY (typed [C]"
          " structural correspondence)",
          np.allclose(D2, -np.eye(2)) and base_triv)

    # (C5) generic-fibre control: fibres over NON-mark points carry the
    # same class D^2 (marks distinguished by symmetry, not holonomy)
    w = np.array([0.7 + 0.2j, 1.0])
    w /= np.linalg.norm(w)
    check("generic-fibre control: the same D^2 class for non-mark"
          " fibres -- the marks are distinguished by clock/J symmetry"
          " (round DLI), NOT by holonomy (stated honestly)",
          np.allclose(np.exp(1j * np.pi) * w,
                      np.linalg.matrix_power(DECK, 2) @ w))

    # (C6) every mark string links each pole string once (Gauss)
    N = 720
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)

    def circ_r3(kind):
        if kind == 'mark':
            v2 = np.exp(1j * t) / np.sqrt(2)
            v1 = v2
        else:                                   # pole {z2 = 0}
            v1 = np.exp(1j * t)
            v2 = np.zeros_like(v1)
        x = np.stack([v1.real, v1.imag, v2.real, v2.imag], axis=1)
        return x[:, :3] / (1 - x[:, 3:4])

    r1, r2 = circ_r3('mark'), circ_r3('pole')
    t1 = (np.roll(r1, -1, 0) - np.roll(r1, 1, 0)) * (N / (4 * np.pi))
    t2 = (np.roll(r2, -1, 0) - np.roll(r2, 1, 0)) * (N / (4 * np.pi))
    d = r1[:, None, :] - r2[None, :, :]
    cross = np.cross(t1[:, None, :], t2[None, :, :])
    integrand = (d * cross).sum(-1) / np.linalg.norm(d, axis=-1) ** 3
    lk = integrand.sum() * (2 * np.pi / N) ** 2 / (4 * np.pi)
    check(f"Gauss linking of a mark string with a pole string = +-1"
          f" (computed {lk:.4f}): the Z_2 flux strings are threaded by"
          f" the order-4 aeon axes", np.isclose(abs(lk), 1.0, atol=2e-3))


def part_d():
    print("\nPART D -- the cosmology fork priced: decidable, unlike the"
          " deck fork (external data typed)")

    # EXTERNAL DATA (typed): Planck 2018 n_s = 0.9649 +/- 0.0042;
    # BICEP/Keck+Planck r_0.05 < 0.036 (95%); LiteBIRD/CMB-S4 target
    # sigma(r) ~ 0.001.
    NS_C, NS_S = 0.9649, 0.0042
    R_BOUND, R_FUTURE = 0.036, 0.001

    Ns = np.array([50.0, 55.0, 60.0])
    ns = 1 - 2 / Ns
    r = 12 / Ns ** 2
    ok_ns = np.all(np.abs(ns - NS_C) < 2 * NS_S)
    check(f"Starobinsky branch over N_star in [50, 60]: n_s in"
          f" [{ns.min():.4f}, {ns.max():.4f}] -- within 2 sigma of"
          f" Planck ({NS_C} +/- {NS_S})", ok_ns)
    check(f"tensor ratio r in [{r.min():.4f}, {r.max():.4f}]: below the"
          f" current bound {R_BOUND} (branch alive today)...",
          np.all(r < R_BOUND))
    check(f"...but ABOVE the future sensitivity {R_FUTURE} by a factor"
          f" {r.min() / R_FUTURE:.1f}-{r.max() / R_FUTURE:.1f} => the"
          f" cosmology fork IS decidable: r detected at 0.003-0.005"
          f" kills the pure-CCC branch (unless crossover dynamics"
          f" reproduce it); r < 0.001 kills the Starobinsky branch --"
          f" TFPT cannot keep both stories past that measurement",
          np.all(r > 3 * R_FUTURE))


def main():
    print("=" * 72)
    print("ccc_fork_kms_holonomy_probe -- round-DLI targets executed:")
    print("fork pricing, global Yamabe/KMS uniqueness, string holonomy")
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
    print("(A) deck fork: EMPIRICALLY UNDECIDABLE by topology searches --")
    print("    both branches alive, decision is theoretical (typed).")
    print("(B) Yamabe representative on the crossover GLOBALLY unique")
    print("    (Obata manifold scanned); uniqueness == uniform KMS period.")
    print("(C) holonomy dictionary: pole strings = mu_4 (order 4), seam")
    print("    strings = GSO/fermion-parity Z_2 (v522 correspondence),")
    print("    linked once by the aeon axes.")
    print("(D) cosmology fork: DECIDABLE -- Starobinsky r = 0.003-0.005")
    print("    sits between the current bound and future sensitivity;")
    print("    one branch dies within ~a decade.")
    print("OPEN: WOIT gamma dynamics; frozen CMB kernel; theoretical")
    print("    deck-fork decision.")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
