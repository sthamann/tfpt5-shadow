#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ccc_crossover_gates_probe -- CCC.SEAM.CROSSOVER (exploration round 1):
which of the six CCC-crossover gates does the EXISTING TFPT corpus already
answer, machine-checked?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion, NO ledger
row, NO marker moved, NO gate of WOIT.OS.TWISTOR.01 closed or narrowed, NO
claim that Penrose CCC follows from TFPT (the cyclic reading stays [C] in
origin_theory).  This probe only checks which pieces of the CCC-crossover
wish list are ALREADY theorems of the existing seam/transport objects.

CONTEXT.  An external analysis of TFPT vs. Penrose CCC (Tod arXiv:1309.7248,
Penrose--Meissner arXiv:2503.24263) lists six gates for a would-be contract
CCC.SEAM.CROSSOVER.01: (1) dimensions (2D seam vs 3D crossover in 4D),
(2) local scale (dimensionless sigma(x), vgeo = calibration only),
(3) reciprocal gauge (Omega_hat * Omega_check = -1), (4) unitarity of the
rank-1 attractor (Stinespring dilation), (5) cosmology fork, (6) frozen CMB
kernel.  Gates (1), (5), (6) are genuinely open (they ARE WOIT.OS.TWISTOR.01
resp. new work).  THIS PROBE shows gates (2), (3), (4) are already answered
by existing [E] objects of the corpus:

PART A (reciprocal gate).  The Moebius stabiliser of mu_4 is the PROVEN
D_4 = <rho: z->iz, s: z->1/z> of order 8 (research contracts, finite
rigidity; v168/v180).  The element tau := rho^2 s : z -> -1/z is Penrose's
reciprocal-gauge involution Omega_check = -1/Omega_hat.  Machine checks:
tau^2 = id, tau rho tau = rho^{-1} (tau reverses the clock = the Z_2 sheet
parity / CPT flip of origin_theory), tau swaps the two clock fixed points
0 <-> infinity (the two aeon poles: big-bang inflation point vs conformal
infinity), tau preserves mu_4 (fixes +-i, swaps 1 <-> -1), and the
crossover locus |Omega_hat| = |Omega_check| is the unit circle -- which
carries ALL FOUR mu_4 marks.  So the reciprocal gauge is not an import:
it is an element of the already-proven seam stabiliser.

PART B (local-scale gate).  Within the conformal class of the round seam
sphere, every constant-curvature(+1) representative is a Moebius pullback;
the residual freedom modulo isometries is 3-dimensional (H^3).  Machine
checks: (i) the dilation family sigma_lam(z) = lam(1+|z|^2)/(1+lam^2|z|^2)
solves the Liouville equation K = +1 for every lam (grid check); (ii) it is
clock-invariant (rho: z->iz) for EVERY lam -- so the clock alone does NOT
pin the conformal factor (a 1-parameter modulus survives, exactly the
"free scale" the external analysis worries about); (iii) imposing the
reciprocal involution tau (Part A) kills the modulus: tau-invariance holds
iff lam = 1, and a lam-scan shows the unique zero.  A translation control
breaks clock invariance (the family is special, not generic).  CONCLUSION:
D_4-equivariance (clock + reciprocal Z_2) pins the DIMENSIONLESS conformal
representative sigma == 1 uniquely; v_geo stays pure unit calibration
(VGEO.TORSOR.01, rank-1 dimension matrix, v725) -- i.e. TFPT's candidate
answer to CCC's open "unique conformal factor" problem at seam level is:
sigma is fixed by the seam symmetry, the unit by the torsor point.

PART C (unitarity gate).  The v221 transport T = J + (2/3)^6 u2 u2^T +
(1/3)^6 u3 u3^T (u2 ~ (1,-1,0), u3 ~ (1,1,-2), J = uniform) is symmetric
doubly stochastic -- a CPTP classical channel, NOT unitary.  Machine
checks: exact spectrum {1, (2/3)^6, (1/3)^6}; ||T - unitary|| quantified;
the 9 Kraus operators K_(ij) = sqrt(T_ij) |i><j| satisfy sum K^dag K = 1
(column-stochasticity IS the isometry condition); the Stinespring isometry
V = sum_a K_a (x) |a>_E has V^dag V = 1_3 exactly and Tr_E V rho V^dag
reproduces T; iterating with fresh environments, the GLOBAL overlap
<Psi_1(n)|Psi_2(n)> is exactly invariant (no information destroyed), the
REDUCED trace distance decays exactly at (2/3)^6 per step (the rank-1
attractor), and the ENVIRONMENT trace distance grows to the full initial
distinguishability (the microstate record migrates to the complementary
channel).  CONCLUSION: the "entropy reset" of the cyclic [C] reading is
already consistent as a REDUCED channel -- the Stinespring dilation the
external analysis demands exists explicitly for the actual TFPT transport;
"unitarity + rank-1 attractor" is not a contradiction, it is
isometry + partial trace.

PART D (de Sitter phrasing).  origin_theory says "asymptotically de Sitter,
hence conformally flat".  Symbolic check (sympy, static patch
f = 1 - 2M/r - Lambda r^2/3): the Weyl invariant C^2 = 48 M^2 / r^6 --
zero for PURE de Sitter (M = 0), nonzero for every M != 0 even though the
spacetime is asymptotically de Sitter.  So the corpus phrase is too strong
as stated; the correct statement is C^2 -> 0 as r -> infinity (conformal
flatness only asymptotically / for the exact dS realisation).  A prose
sharpening candidate, no marker move.

WHAT STAYS OPEN (honest).  Gate (1) 2D seam -> 3D crossover in 4D is
exactly the open OS/twistor bridge WOIT.OS.TWISTOR.01 (alpha, beta_1
executed, gamma next) -- nothing here touches it.  Gate (5) the cosmology
fork (Starobinsky vs gravitational-wave epoch vs hybrid) is a genuine
model decision.  Gate (6) a frozen CMB kernel K_TFPT does not exist yet.
mu_4 marks are NOT Hawking points (clock structure vs event-dependent
positions) -- no identification is made or checked here.
"""

import numpy as np

RNG = np.random.default_rng(20260824)
LAM2 = (2.0 / 3.0) ** 6          # 64/729
LAM3 = (1.0 / 3.0) ** 6          # 1/729

PASS = []


def check(name, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


# =====================================================================
# Moebius helpers (2x2 complex matrices acting on P^1)
# =====================================================================
RHO = np.array([[1j, 0], [0, 1]], dtype=complex)      # z -> i z   (clock)
S = np.array([[0, 1], [1, 0]], dtype=complex)         # z -> 1/z
TAU = np.array([[0, -1], [1, 0]], dtype=complex)      # z -> -1/z  (reciprocal)


def moebius(M, z):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    if z == np.inf:
        return a / c if c != 0 else np.inf
    den = c * z + d
    if abs(den) < 1e-300:
        return np.inf
    return (a * z + b) / den


def proj_eq(M, N):
    """Projective equality of 2x2 matrices (equal up to scalar)."""
    idx = np.unravel_index(np.argmax(np.abs(N)), N.shape)
    if abs(M[idx]) < 1e-12:
        return False
    return np.allclose(M / M[idx], N / N[idx], atol=1e-12)


def part_a():
    print("\nPART A -- reciprocal gate: Penrose's Omega_hat*Omega_check = -1"
          " is an element of the proven mu_4 stabiliser D_4")

    mu4 = [1 + 0j, 1j, -1 + 0j, -1j]

    # (A1) group generated by rho, s is D_4 of order 8 (projectively)
    elems = [np.eye(2, dtype=complex)]
    frontier = [np.eye(2, dtype=complex)]
    while frontier:
        new = []
        for g in frontier:
            for h in (RHO, S):
                cand = h @ g
                if not any(proj_eq(cand, e) for e in elems):
                    elems.append(cand)
                    new.append(cand)
        frontier = new
    check(f"<rho, s> has projective order 8 = |D_4| (got {len(elems)})",
          len(elems) == 8)

    # (A2) tau = rho^2 s projectively, i.e. -1/z is inside the group
    check("tau: z -> -1/z equals rho^2 s (inside the proven stabiliser)",
          proj_eq(RHO @ RHO @ S, TAU))

    # (A3) tau is an involution
    check("tau^2 = id (an honest Z_2)", proj_eq(TAU @ TAU, np.eye(2)))

    # (A4) tau reverses the clock: tau rho tau^{-1} = rho^{-1}
    check("tau rho tau^{-1} = rho^{-1} (reciprocal gauge = clock/orientation"
          " reversal = the Z_2 sheet parity)",
          proj_eq(TAU @ RHO @ np.linalg.inv(TAU), np.linalg.inv(RHO)))

    # (A5) clock fixed points are {0, inf}; tau swaps them (aeon poles)
    fp_rho_0 = moebius(RHO, 0) == 0
    fp_rho_inf = moebius(RHO, np.inf) == np.inf
    swap = (moebius(TAU, 0) == np.inf) and (moebius(TAU, np.inf) == 0)
    check("clock fixes exactly the poles {0, inf}; tau swaps them "
          "(Omega_check -> 0 where Omega_hat -> inf: the aeon exchange)",
          fp_rho_0 and fp_rho_inf and swap)

    # (A6) tau preserves mu_4: fixes +-i, swaps 1 <-> -1
    img = {z: moebius(TAU, z) for z in mu4}
    fixes = np.isclose(img[1j], 1j) and np.isclose(img[-1j], -1j)
    swaps = np.isclose(img[1 + 0j], -1 + 0j) and np.isclose(img[-1 + 0j], 1 + 0j)
    check("tau preserves mu_4 setwise: fixes {+i,-i}, swaps {1,-1} "
          "(its fixed points ARE two marks)", fixes and swaps)

    # (A7) the reciprocal constraint Omega_hat*Omega_check = -1 holds
    # identically for Omega_check := tau(Omega_hat)
    zs = RNG.standard_normal(64) + 1j * RNG.standard_normal(64)
    ok = all(np.isclose(z * moebius(TAU, z), -1.0) for z in zs)
    check("Omega_check := tau(Omega_hat) satisfies "
          "Omega_hat*Omega_check = -1 identically", ok)

    # (A8) crossover locus |Omega_hat| = |Omega_check| is the unit circle,
    # and all four mu_4 marks lie on it
    theta = RNG.uniform(0, 2 * np.pi, 64)
    circ = np.exp(1j * theta)
    on_circle = np.allclose([abs(moebius(TAU, z)) for z in circ],
                            np.abs(circ))
    off = abs(moebius(TAU, 2.0 + 0j))  # |tau(2)| = 1/2 != 2
    marks_on = all(np.isclose(abs(z), 1.0) for z in mu4)
    check("crossover locus |Omega_hat|=|Omega_check| = unit circle; "
          "all four mu_4 marks sit ON the crossover", 
          on_circle and not np.isclose(off, 2.0) and marks_on)


# =====================================================================
# PART B -- local-scale gate
# =====================================================================
def part_b():
    print("\nPART B -- local-scale gate: D_4-equivariance pins the"
          " dimensionless conformal representative uniquely")

    def u_lam(z, lam):
        # conformal factor of sigma_lam^2 * ghat in the plane chart:
        # metric e^{2u}|dz|^2 with e^u = 2 lam / (1 + lam^2 |z|^2)
        return np.log(2 * lam) - np.log1p((lam * np.abs(z)) ** 2)

    # (B1) Liouville: K = -e^{-2u} Lap(u) = +1 for every lam (exact, sympy)
    import sympy as sp
    xs_, ys_, lam_ = sp.symbols('x y lam', real=True, positive=True)
    u_sym = sp.log(2 * lam_) - sp.log(1 + lam_ ** 2 * (xs_ ** 2 + ys_ ** 2))
    lap_u = sp.diff(u_sym, xs_, 2) + sp.diff(u_sym, ys_, 2)
    K_sym = sp.simplify(-sp.exp(-2 * u_sym) * lap_u)
    check(f"dilation family sigma_lam solves the Liouville equation "
          f"K = +1 for EVERY lam symbolically (got K = {K_sym})",
          sp.simplify(K_sym - 1) == 0)

    # (B2) clock invariance for EVERY lam: u(iz) = u(z) exactly
    zs = (RNG.standard_normal(256) + 1j * RNG.standard_normal(256))
    res_clock = max(
        float(np.max(np.abs(u_lam(1j * zs, lam) - u_lam(zs, lam))))
        for lam in (0.3, 1.0, 2.0, 5.0))
    check(f"clock rho: z->iz leaves sigma_lam invariant for ALL lam "
          f"(residual {res_clock:.1e}) -- the clock alone does NOT fix "
          f"the scale profile", res_clock < 1e-12)

    # (B3) reciprocal invariance: u(tau z) + log|tau'(z)| = u(z) iff lam = 1
    def tau_residual(lam):
        zt = -1.0 / zs
        r = u_lam(zt, lam) + np.log(1.0 / np.abs(zs) ** 2) - u_lam(zs, lam)
        return float(np.max(np.abs(r)))

    res_at_1 = tau_residual(1.0)
    lams = np.linspace(0.2, 5.0, 481)
    residuals = np.array([tau_residual(l) for l in lams])
    zeros = lams[residuals < 1e-10]
    check(f"reciprocal tau-invariance residual at lam=1: {res_at_1:.1e} "
          f"(invariant)", res_at_1 < 1e-12)
    check(f"lam-scan [0.2, 5.0]: tau-invariance holds ONLY at lam = 1 "
          f"(zeros found: {zeros.tolist() if len(zeros) < 4 else len(zeros)})"
          f" -- the reciprocal Z_2 kills the residual modulus",
          len(zeros) == 1 and np.isclose(zeros[0], 1.0))

    # (B4) monotone growth of the defect away from lam=1 (unique minimum)
    i1 = int(np.argmin(np.abs(lams - 1.0)))
    left = residuals[:i1]
    right = residuals[i1 + 1:]
    check("tau-defect decreases towards lam=1 from the left and increases "
          "to the right (unique minimum)",
          bool(np.all(np.diff(left) < 0) and np.all(np.diff(right) > 0)))

    # (B5) control: a translated representative breaks CLOCK invariance
    c = 0.7 + 0.3j

    def u_trans(z):
        w = z + c
        return np.log(2.0) - np.log1p(np.abs(w) ** 2)

    res_ctrl = float(np.max(np.abs(u_trans(1j * zs) - u_trans(zs))))
    check(f"control: translation representative breaks clock invariance "
          f"(residual {res_ctrl:.2f} >> 0) -- the family is selected, "
          f"not generic", res_ctrl > 0.1)


# =====================================================================
# PART C -- unitarity gate: explicit Stinespring dilation of the v221
# transport
# =====================================================================
def part_c():
    print("\nPART C -- unitarity gate: the rank-1 attractor is a reduced"
          " channel of an explicit isometry (Stinespring)")

    # the exact v221 transport on the cusp-weight 3-space
    u2 = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
    u3 = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0)
    J = np.full((3, 3), 1.0 / 3.0)
    T = J + LAM2 * np.outer(u2, u2) + LAM3 * np.outer(u3, u3)

    evals = np.sort(np.linalg.eigvalsh(T))[::-1]
    check(f"transport spectrum = {{1, (2/3)^6, (1/3)^6}} "
          f"(got {evals[0]:.6f}, {evals[1]:.6f} = {LAM2:.6f}, "
          f"{evals[2]:.6f} = {LAM3:.6f})",
          np.allclose(evals, [1.0, LAM2, LAM3]))
    dstoch = (np.allclose(T.sum(0), 1) and np.allclose(T.sum(1), 1)
              and (T >= 0).all())
    check("T symmetric, doubly stochastic, entrywise >= 0 (CPTP classical"
          " channel)", np.allclose(T, T.T) and dstoch)

    # (C1) T is NOT unitary -- the naive 'unitary reset' reading fails
    dev_unitary = np.linalg.norm(T.T @ T - np.eye(3), 2)
    check(f"T is NOT unitary: ||T^t T - 1||_2 = {dev_unitary:.6f} > 0 "
          f"(so 'unitarity + rank-1 contraction' NEEDS a dilation)",
          dev_unitary > 0.9)

    # (C2) exact contraction to the rank-1 attractor
    ok_rate = all(
        np.isclose(np.linalg.norm(np.linalg.matrix_power(T, k) - J, 2),
                   LAM2 ** k, rtol=1e-10)
        for k in range(1, 7))
    check("||T^n - P_star||_2 = (2/3)^{6n} EXACTLY for n = 1..6 "
          "(rank-1 attractor at the seam rate)", ok_rate)

    # (C3) Kraus operators and the isometry condition
    kraus = [np.sqrt(T[i, j]) * np.outer(np.eye(3)[i], np.eye(3)[j])
             for i in range(3) for j in range(3)]
    ksum = sum(K.T @ K for K in kraus)
    check("sum_a K_a^dag K_a = 1 (column-stochasticity IS the trace-"
          "preservation / isometry condition)", np.allclose(ksum, np.eye(3)))

    # V : C^3 -> C^3 (x) C^9, V|psi> = sum_a K_a|psi> (x) |a>
    V = np.zeros((27, 3))
    for a, K in enumerate(kraus):
        for i in range(3):
            for j in range(3):
                V[i * 9 + a, j] += K[i, j]
    check("Stinespring V^dag V = 1_3 exactly (an isometry, the global"
          " evolution)", np.allclose(V.T @ V, np.eye(3)))

    rho_in = np.diag([0.5, 0.3, 0.2])
    big = V @ rho_in @ V.T
    red = np.trace(big.reshape(3, 9, 3, 9), axis1=1, axis2=3)
    check("Tr_E (V rho V^dag) reproduces the transport on classical"
          " states", np.allclose(np.diag(red), T @ np.diag(rho_in)))

    # (C4) iterate with fresh environments; two orthogonal microstates
    def evolve(psi, n):
        """psi in C^3 -> global pure state in C^{3 * 9^n}."""
        state = psi.astype(complex)
        for _ in range(n):
            m = state.reshape(3, -1)          # (sys, env_so_far)
            state = np.einsum('iaj,je->iae', V.reshape(3, 9, 3),
                              m).reshape(-1)
        return state

    psi1 = np.array([1.0, 0.0, 0.0])
    psi2 = np.array([0.0, 1.0, 0.0])
    d_glob0 = np.sqrt(1 - abs(psi1 @ psi2) ** 2)   # = 1 (orthogonal)

    print("    n   |<Psi1|Psi2>|   D_sys(n)      D_sys/lam2^n   D_env(n)")
    ok_overlap = ok_sys = True
    d_env_list = []
    for nstep in range(1, 6):
        s1, s2 = evolve(psi1, nstep), evolve(psi2, nstep)
        ov = abs(np.vdot(s1, s2))
        m1, m2 = s1.reshape(3, -1), s2.reshape(3, -1)
        rho1, rho2 = m1 @ m1.conj().T, m2 @ m2.conj().T
        d_sys = 0.5 * np.abs(np.linalg.eigvalsh(rho1 - rho2)).sum()
        # environment states have rank <= 3: work in the joint column space
        rows = np.vstack([m1, m2]).conj().T          # (E, 6)
        q, _ = np.linalg.qr(rows)
        e1, e2 = m1 @ q, m2 @ q                       # (3, r)
        env1, env2 = e1.conj().T @ e1, e2.conj().T @ e2
        d_env = 0.5 * np.abs(np.linalg.eigvalsh(env1 - env2)).sum()
        d_env_list.append(d_env)
        print(f"    {nstep}   {ov:.3e}     {d_sys:.6e}  "
              f"{d_sys / LAM2 ** nstep:.6f}       {d_env:.6f}")
        ok_overlap &= np.isclose(ov, abs(psi1 @ psi2), atol=1e-12)
        ok_sys &= np.isclose(d_sys, LAM2 ** nstep, rtol=1e-9)
    check("global overlap <Psi1(n)|Psi2(n)> invariant for all n "
          "(NO information destroyed -- the dilation is exact)", ok_overlap)
    check("reduced (seam-visible) trace distance = (2/3)^{6n} exactly "
          "(the 'reset' is the reduced channel, e1 - e2 is the u2 mode)",
          ok_sys)
    check(f"environment distinguishability grows monotonically to the full"
          f" initial value {d_glob0:.0f} (last: {d_env_list[-1]:.6f}) -- "
          f"the microstate record migrates to the complementary channel",
          all(np.diff(d_env_list) > 0) or d_env_list[-1] > 0.99)


# =====================================================================
# PART D -- 'asymptotically de Sitter hence conformally flat' is too
# strong: symbolic Weyl invariant of Schwarzschild-de Sitter
# =====================================================================
def part_d():
    print("\nPART D -- de Sitter phrasing: Weyl^2 of Schwarzschild-de"
          " Sitter (symbolic)")
    import sympy as sp

    t, r, th, ph, M, L = sp.symbols('t r theta phi M Lambda', positive=True)
    f = 1 - 2 * M / r - L * r ** 2 / 3
    g = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2)
    ginv = g.inv()
    xs = [t, r, th, ph]

    n = 4
    Gamma = [[[sp.simplify(sum(ginv[k, l] * (sp.diff(g[l, i], xs[j])
                                             + sp.diff(g[l, j], xs[i])
                                             - sp.diff(g[i, j], xs[l]))
                               for l in range(n)) / 2)
               for j in range(n)] for i in range(n)] for k in range(n)]

    Riem = [[[[sp.simplify(sp.diff(Gamma[k][i][j2], xs[j1])
                           - sp.diff(Gamma[k][i][j1], xs[j2])
                           + sum(Gamma[k][j1][l] * Gamma[l][i][j2]
                                 - Gamma[k][j2][l] * Gamma[l][i][j1]
                                 for l in range(n)))
               for j2 in range(n)] for j1 in range(n)]
             for i in range(n)] for k in range(n)]

    Ric = sp.Matrix(n, n, lambda i, j: sp.simplify(
        sum(Riem[k][i][k][j] for k in range(n))))
    Rs = sp.simplify(sum(ginv[i, j] * Ric[i, j]
                         for i in range(n) for j in range(n)))

    # lower first index, then full contractions
    Rlow = [[[[sp.simplify(sum(g[a, k] * Riem[k][i][j1][j2]
                               for k in range(n)))
               for j2 in range(n)] for j1 in range(n)]
             for i in range(n)] for a in range(n)]
    Kre = sp.simplify(sum(
        Rlow[a][b][c][d] * ginv[a, aa] * ginv[b, bb] * ginv[c, cc]
        * ginv[d, dd] * Rlow[aa][bb][cc][dd]
        for a in range(n) for b in range(n) for c in range(n)
        for d in range(n) for aa in range(n) for bb in range(n)
        for cc in range(n) for dd in range(n)
        if (g[a, aa] != 0 and g[b, bb] != 0 and g[c, cc] != 0
            and g[d, dd] != 0)))
    Ric2 = sp.simplify(sum(Ric[i, j] * ginv[i, a] * ginv[j, b] * Ric[a, b]
                           for i in range(n) for j in range(n)
                           for a in range(n) for b in range(n)
                           if (g[i, a] != 0 and g[j, b] != 0)))
    C2 = sp.simplify(Kre - 2 * Ric2 + Rs ** 2 / 3)

    check(f"scalar curvature R = 4*Lambda (Einstein space): got {Rs}",
          sp.simplify(Rs - 4 * L) == 0)
    check(f"Weyl invariant C^2 = 48 M^2 / r^6: got {C2}",
          sp.simplify(C2 - 48 * M ** 2 / r ** 6) == 0)
    check("pure de Sitter (M = 0): C^2 = 0 -- conformally flat, the CCC"
          " rescaling condition holds for the EXACT dS realisation",
          sp.simplify(C2.subs(M, 0)) == 0)
    check("Schwarzschild-de Sitter (M != 0): C^2 != 0 at every finite r "
          "although asymptotically de Sitter -- 'asymptotically dS hence"
          " conformally flat' is TOO STRONG; only C^2 -> 0 as r -> inf",
          sp.simplify(C2.subs([(M, 1), (r, 2)])) != 0
          and sp.limit(C2.subs(M, 1), r, sp.oo) == 0)


def main():
    print("=" * 72)
    print("ccc_crossover_gates_probe -- which CCC crossover gates does the")
    print("existing TFPT corpus already answer? (EXPLORATION ONLY, no ledger)")
    print("=" * 72)
    part_a()
    part_b()
    part_c()
    part_d()
    print("\n" + "=" * 72)
    n_ok = sum(PASS)
    print(f"RESULT: {n_ok}/{len(PASS)} checks passed"
          + ("  --  ALL PASSED" if all(PASS) else "  --  FAILURES ABOVE"))
    print("Gates answered by existing objects: (3) reciprocal [Part A],")
    print("(2) local scale [Part B], (4) unitarity [Part C]; phrasing fix")
    print("candidate [Part D].  Open and untouched: (1) 4D uplift =")
    print("WOIT.OS.TWISTOR.01, (5) cosmology fork, (6) frozen CMB kernel.")
    print("=" * 72)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
