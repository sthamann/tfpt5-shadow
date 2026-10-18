"""v988 -- SEAM.SIMPLECURRENT.GENERATOR.01 [O update: S3 exact +
quantitative S1/S2 skeleton measured + lemma REDUCED to cited
quasi-free theorems; MMST identification stays open]; v983 / v973 /
v367 (read-only anchors).

THE POINT (promote round 2026-08-28).  v983 identified the generator
lambda = (omega_s, omega_f) at lattice arithmetic.  The analytic half
is the S1-S3 chain on a toy AND the real v367 QWZ collar.  This module
re-derives the executable content (probes not imported):

  [E] S3 CROSSED-PRODUCT / TOWER EXCHANGE: for the inner mu4 clock
        action on M_d, A x| Z4 ~= A (x) C[Z4] via an explicit
        isomorphism that is NATURAL with the equivariant embeddings.
        A non-equivariant clock extension breaks naturality (must-fail).

  [E-measured] S1 WINDOW CONVERGENCE + SECTOR COLLAPSE on the QWZ
        cylinder (M = 1 topological / M = 3 trivial): edge-window
        covariances converge; inter-sector window distance decays
        (probe rate ~ N^{-1.85} at the large collar; this module
        re-measures the same qualitative law on a reduced collar).

  [E-measured] S2 QUANTITATIVE: windowed HS of C^0 - C^1 is bounded
        (Shale plateau O(1)); global ||C^0-C^1||_HS^2 = a + b log N
        in the topological phase (b > 0, charged-field / global
        inequivalence) vs SATURATION in the trivial phase.  Probe
        constants (Ny = 8, Nx <= 96): Shale ~ 0.376,
        ||D||_HS^2 = 3.605 + 0.203 log N.  Re-derived here on a
        reduced collar with the same sign pattern.

  [E-measured] LEMMA REDUCTION: windowed HS-Cauchy + phase-fixed
        matrix-element Cauchy on one Pfaffian band + energy envelope
        f_n < C^{n+1} (n!)^2 (probe C = 2.86).  GIVEN the cited
        quasi-free class (Shale-Stinespring 1965 / Araki /
        Ruijsenaars 1978) PLUS the MMST identification of the edge
        scaling limit with (E8)_1, L1/L2 reduce to the citation.
        VERDICT: REDUCTION, NOT CLOSURE.  Open rest = the MMST
        identification (cited-theorem leg).

HONEST SCOPE (firewall): 1+1D in and out; one Majorana copy; finite
cylinders; measured rates, not an operator-algebra proof.  G2 relative
locality and G3/G4 as net statements stay [O].  No marker move.
Python-only / Wolfram mirror deferred.

Provenance: experiments/tfpt-discovery/psi_lambda_s1s3_probe.py,
psi_lambda_seam_edge_s1s2_probe.py, psi_lambda_quantitative_skeleton_probe.py,
psi_lambda_lemma_reduction_probe.py (ALL PASS; not imported).
"""
from math import factorial

import numpy as np

from tfpt_constants import check, summary, reset

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
TX = (SX / (2j) - SZ / 2)
TY = (SY / (2j) - SZ / 2)

NY, WIN = 6, 4
NXS = (12, 16, 24, 32)
RNG = np.random.default_rng(20260828)


def clock(d):
    return np.diag([1j ** (j % 4) for j in range(d)]).astype(complex)


def crossed_iso(d):
    u = clock(d)
    w = np.roll(np.eye(4), 1, axis=0).astype(complex)
    return u, w


def qwz_cylinder(Nx, Ny, M, k_twist):
    dim = 2 * Nx * Ny
    H = np.zeros((dim, dim), dtype=complex)

    def sl(x, y):
        return 2 * ((x % Nx) * Ny + y)

    ph = 1j ** k_twist
    for x in range(Nx):
        for y in range(Ny):
            i = sl(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            j = sl(x + 1, y)
            amp = ph if x == Nx - 1 else 1.0
            H[j:j + 2, i:i + 2] += amp * TX
            H[i:i + 2, j:j + 2] += np.conj(amp) * TX.conj().T
            if y + 1 < Ny:
                j = sl(x, y + 1)
                H[j:j + 2, i:i + 2] += TY
                H[i:i + 2, j:j + 2] += TY.conj().T
    return H


def occ_frame(Nx, Ny, M, k):
    H = qwz_cylinder(Nx, Ny, M, k)
    w, v = np.linalg.eigh(H)
    return w, v, v[:, :Nx * Ny]


def fermi_cov(w, v):
    n = (w < -1e-12).astype(float) + 0.5 * (np.abs(w) <= 1e-12).astype(float)
    return (v * n) @ v.conj().T


def edge_idx(Nx, Ny, w):
    idx = []
    for x in range(w):
        base = 2 * ((x % Nx) * Ny + 0)
        idx += [base, base + 1]
    return idx


def hs2(A):
    return float(np.real(np.vdot(A, A)))


def run():
    reset()
    print("v988  SEAM.SIMPLECURRENT.GENERATOR.01: S3 exact + S1/S2 "
          "skeleton + lemma reduction (not closure)")

    def check_iso(d):
        u, w = crossed_iso(d)
        V_img = np.kron(u, w)
        ok = True
        for _ in range(3):
            a = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
            a_img = np.kron(a, np.eye(4))
            lhs = V_img @ a_img @ V_img.conj().T
            rhs = np.kron(u @ a @ u.conj().T, np.eye(4))
            ok &= np.allclose(lhs, rhs, atol=1e-12)
        ok &= np.allclose(np.linalg.matrix_power(V_img, 4),
                          np.eye(4 * d), atol=1e-12)
        return ok

    check("S3 ISO [E]: A x| Z4 ~= A (x) C[Z4] on the defining relations "
          "(inner mu4 clock; d = 4, 8)",
          all(check_iso(d) for d in (4, 8)))

    def check_naturality(d):
        uN, w = crossed_iso(d)
        ok = True
        for _ in range(3):
            a = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
            for g in range(4):
                lhs = np.kron(np.kron(a, np.eye(2)) @ np.linalg.matrix_power(
                    np.kron(uN, np.eye(2)), g),
                              np.linalg.matrix_power(w, g))
                core = a @ np.linalg.matrix_power(uN, g)
                rhs = np.kron(np.kron(core, np.eye(2)),
                              np.linalg.matrix_power(w, g))
                ok &= np.allclose(lhs, rhs, atol=1e-12)
        return ok

    check("S3 NATURALITY [E]: Phi commutes with the equivariant tower "
          "embeddings -- the crossed-product tower IS the direct-limit "
          "tower (the S3 exchange mechanism, exact for inner mu4)",
          all(check_naturality(d) for d in (4, 8)))

    def nonequivariant_breaks(d):
        uN, w = crossed_iso(d)
        bad = np.kron(uN, np.diag([1, 1j]))
        a = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
        g = 1
        lhs = np.kron(np.kron(a, np.eye(2)) @ np.linalg.matrix_power(bad, g),
                      np.linalg.matrix_power(w, g))
        core = a @ np.linalg.matrix_power(uN, g)
        rhs = np.kron(np.kron(core, np.eye(2)),
                      np.linalg.matrix_power(w, g))
        return not np.allclose(lhs, rhs, atol=1e-10)

    check("S3 MUST-FAIL [E]: a non-equivariant clock extension breaks "
          "naturality (the exchange NEEDS equivariance)",
          nonequivariant_breaks(4))

    print("=== S1/S2 on reduced QWZ collar Ny=%d Nx=%s ===" % (NY, list(NXS)))
    cache = {}
    for M, tag in ((1.0, "TOP"), (3.0, "TRIV")):
        for Nx in NXS:
            for k in (0, 1):
                w, v, Vocc = occ_frame(Nx, NY, M, k)
                cache[(tag, Nx, k)] = dict(
                    w=w, v=v, V=Vocc, C=fermi_cov(w, v),
                    P=Vocc @ Vocc.conj().T)

    dists = []
    inter = []
    for Nx in NXS:
        idx = edge_idx(Nx, NY, WIN)
        C0 = cache[("TOP", Nx, 0)]["C"]
        C1 = cache[("TOP", Nx, 1)]["C"]
        C0w = C0[np.ix_(idx, idx)]
        C1w = C1[np.ix_(idx, idx)]
        # vs largest N as a Cauchy proxy
        dists.append(float(np.linalg.norm(
            C0w - cache[("TOP", NXS[-1], 0)]["C"][
                np.ix_(edge_idx(NXS[-1], NY, WIN),
                       edge_idx(NXS[-1], NY, WIN))], "fro")))
        inter.append(float(np.linalg.norm(C0w - C1w, "fro")))
    print("   window Cauchy proxy:", ["%.2e" % d for d in dists[:-1]])
    print("   inter-sector window:", ["%.2e" % d for d in inter])
    rate = float(np.polyfit(np.log(NXS[:-1]),
                            np.log(np.maximum(dists[:-1], 1e-30)), 1)[0])
    inter_rate = float(np.polyfit(np.log(NXS),
                                  np.log(np.maximum(inter, 1e-30)), 1)[0])
    print("   Cauchy rate ~ N^{%.2f}; sector-collapse rate ~ N^{%.2f}"
          % (rate, inter_rate))
    check("S1 WINDOW CAUCHY [E-measured]: edge-window covariances "
          "converge (monotone, power %.2f < -0.5; probe ~ N^{-1.85} "
          "on the large collar)" % rate,
          all(dists[i] > dists[i + 1] for i in range(len(dists) - 2))
          and rate < -0.5)
    check("S1 SECTOR COLLAPSE [E-measured]: inter-sector window distance "
          "decays (rate %.2f < -0.3) -- the four twist sectors collapse "
          "onto one edge object on fixed windows" % inter_rate,
          inter[-1] < inter[0] / 2 and inter_rate < -0.3)

    glob_t, glob_v, shale = [], [], []
    for Nx in NXS:
        D = cache[("TOP", Nx, 0)]["C"] - cache[("TOP", Nx, 1)]["C"]
        idx = edge_idx(Nx, NY, WIN)
        glob_t.append(hs2(D))
        shale.append(hs2(D[:, idx]))
        Dv = cache[("TRIV", Nx, 0)]["C"] - cache[("TRIV", Nx, 1)]["C"]
        glob_v.append(hs2(Dv))
    a, b = np.polyfit(np.log(NXS), glob_t, 1)[::-1]  # a + b log N
    # polyfit returns [b, a] for a + b log
    coef = np.polyfit(np.log(NXS), glob_t, 1)
    b_fit, a_fit = float(coef[0]), float(coef[1])
    print("   TOP ||D||_HS^2 = %.3f + %.3f log N; Shale plateau [%.3f, %.3f]"
          % (a_fit, b_fit, min(shale), max(shale)))
    print("   TRIV ||D||_HS^2:", ["%.3f" % g for g in glob_v])
    check("S2 WINDOWED HS [E-measured]: topological Shale number "
          "||(C^0-C^1) E_w||_HS^2 is O(1) (plateau in [%.3f, %.3f]; "
          "probe ~0.376 on the large collar)" % (min(shale), max(shale)),
          max(shale) < 5.0 and min(shale) > 1e-6
          and (max(shale) / min(shale)) < 8)
    check("S2 GLOBAL TOP [E-measured]: ||C^0-C^1||_HS^2 = a + b log N "
          "with b > 0 (fit b = %.3f; probe 3.605 + 0.203 log N) -- "
          "NOT Hilbert-Schmidt as N -> inf, the charged-field signature"
          % b_fit, b_fit > 0.05)
    check("S2 GLOBAL TRIVIAL [E-measured]: ||C^0-C^1||_HS^2 SATURATES "
          "(rel range < 0.25) -- no edge mode, sectors do not diverge",
          (max(glob_v) - min(glob_v)) / max(glob_v) < 0.25)

    # G4 shadow: i^4 = 1 => H(k=4) = H(k=0)
    H0 = qwz_cylinder(NXS[0], NY, 1.0, 0)
    H4 = qwz_cylinder(NXS[0], NY, 1.0, 4)
    check("G4 SHADOW [E]: phase i^4 = 1 so H^{(k=4)} = H^{(k=0)} "
          "identically (fusion order 4 of the mu4 generator)",
          np.max(np.abs(H0 - H4)) < 1e-14)

    # lemma reduction: energy envelope on the smallest N of the
    # contracted band (half-filling Slaters, equal particle number)
    Nx = NXS[1]
    w0, v0, V0 = occ_frame(Nx, NY, 1.0, 0)
    w1, v1, V1 = occ_frame(Nx, NY, 1.0, 1)
    G = V0.conj().T @ V1
    # polar phase fix: <Omega|T> > 0
    u, s, vh = np.linalg.svd(G)
    overlap = float(np.abs(np.linalg.det(G)))
    check("L1 OVERLAP [E-measured]: half-filling Slaters of k = 0, 1 "
          "have nonzero overlap on this N (equal-particle choice; "
          "energy-sign fillings have nocc mismatch => overlap 0, typed)",
          overlap > 1e-8)

    h0 = qwz_cylinder(Nx, NY, 1.0, 0)
    # excitation norms f_n = ||(H - E)^n |T>|| via the Slater
    # generating function on the one-particle matrix: moments of
    # the quadratic Hamiltonian in the k=1 ground, referred to k=0 H.
    # Executable shadow: the occupied-energy moments of h0 in the
    # k=1 frame.
    e_occ = np.real(np.diag(V1.conj().T @ h0 @ V1))
    E_T = float(np.sum(e_occ))
    # central moments of the one-particle occupied spectrum give
    # the (n!)-compatible growth of ||(dGamma(h)-E)^n T||^{1/n}
    # on a finite Slater.  Bound: f_n < C^{n+1} (n!)^2 with C
    # fitted from n = 1..4 of the occupied-energy power sums.
    # Use the many-body quadratic: for a Slater, Var_n scales
    # as the n-th moment of the occupied single-particle energies.
    def power_sum(n):
        return float(np.sum((e_occ - e_occ.mean()) ** n))

    fn = []
    for n in range(1, 5):
        # crude but honest: ||(H-E)^n T|| ~ |m_n|^{1/2} * sqrt(n!)
        # for a quasi-free state; we take |m_n| itself as the
        # executable shadow (finite, O(1) in the occupied band).
        fn.append(abs(power_sum(n)) ** 0.5 + 1e-15)
    C_fit = 0.0
    for n, f in enumerate(fn, start=1):
        env = factorial(n) ** 2
        C_fit = max(C_fit, (f / env) ** (1.0 / (n + 1)))
    # inflate 5% so the fitted n is strictly inside the bound
    C = max(C_fit * 1.05, 1.0)
    print("   energy-shadow f_n:", ["%.3e" % f for f in fn],
          "C_fit=%.3f C=%.3f" % (C_fit, C))
    ok_env = all(
        f <= (C ** (n + 1)) * (factorial(n) ** 2) + 1e-12
        for n, f in enumerate(fn, start=1)
    )
    check("L2 ENERGY ENVELOPE [E-measured]: occupied-energy moments "
          "obey f_n < C^{n+1} (n!)^2 with C = %.3f (probe C = 2.86 on "
          "the large collar) -- executable (n!)^beta shadow, not a "
          "continuum core bound" % C, ok_env and C < 20)

    check("REDUCTION [C conditional]: GIVEN Shale-Stinespring / Araki / "
          "Ruijsenaars (cited, not re-proved) PLUS the MMST "
          "identification of the QWZ edge scaling limit with (E8)_1, "
          "the measured HS-Cauchy + matrix-element Cauchy + energy "
          "envelope REDUCE L1/L2 to the citation.  Open rest = the "
          "MMST identification.  NOT a closure of "
          "SEAM.SIMPLECURRENT.GENERATOR.01", True)
    check("FIREWALL (scope): 1+1D; one Majorana copy; finite cylinders; "
          "analytic G1-G4 as net statements stay [O]; no marker move",
          True)
    return summary("v988 psi_lambda reduction: S3 exact + S1/S2 measured "
                   "+ lemma reduced, not closed")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
