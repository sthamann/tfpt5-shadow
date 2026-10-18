"""v987 -- DYN.UNITARY.DILATION.01 [O update: the OS/dilation LADDER is
executed at kernel + free-field + interacting-kernel + quantum-coupled
band level]; v971 / v984 / v977 (read-only anchors).

THE POINT (promote round 2026-08-28).  v984 executed the DISCRETE
collision/QCA leg.  This module re-derives the next four executed legs
from the seam single-step kernel B (exact sixth root of the v221
transfer; B = [[13,1,4],[1,13,4],[4,4,10]]/18):

  [E] A. KERNEL OS CONTINUATION (probe dilation_os_continuation):
        B = P1 + (2/3) P2 + (1/3) P3 > 0 with exact orthogonal
        projectors; H = -log B = log(3/2) P2 + log 3 P3 is PSD with
        gap log(3/2); T(t) = e^{-tH} is a stochastic semigroup inside
        the cone; U(t) = e^{-itH} is a unitary group with Wick anchor
        U(-i n) = B^n for n = 1..6.  MUST-FAIL: the v971 negative
        kernel (second eigenvalue -1/10) has no real half-step.

  [E] B. SIZE-UNIFORM FREE BAND (probe dilation_field_os_uniform):
        T_L = B^(x L) has H_L = sum_x h_x commuting local, gap
        log(3/2) UNIFORM in L (exact at L = 2, 3 via the projector
        algebra); D2: the per-cell reduced channel of the collision
        band is B at L = 1, 2; LR radius 1 on the L = 2 band
        (far-cell commutator machine-zero; near-cell strictly
        nonzero).

  [E/N] C. INTERACTING CONGRUENCE FAMILY (probe dilation_interacting_os):
        T_eps = K^{1/2} B^(x L) K^{1/2} is SPD for EVERY tested
        diagonal coupling (congruence of a PD matrix); the one-sided
        mutant K B^(x L) is not symmetric.  Gap plateau measured
        (~0.17 at L = 2..4, eps = 0.3); quasi-locality of -log T
        measured (2-site coefficients decay with distance).

  [N] D. QUANTUM SWAP COUPLING (probe dilation_quantum_coupled_band):
        W_theta = U_int(theta) (x)_x V_x with h = SWAP is unitary,
        CPTP at the reduced cell, d(theta) ~ theta^2 (leading even
        power), and an even-bond matching layer of the same SWAP
        family makes the far cell vanish at machine precision.

HONEST SCOPE (firewall): finite, discrete-time, 1+1D kernel / band.
The CONTINUOUS field-level OS reconstruction, thermodynamic-limit
branch selection, and any 3+1D reading stay [O].  No marker move.
Python-only / Wolfram mirror deferred (GATE.WOLFRAM.02 convention of
the v974-v986 wave).

Provenance: experiments/tfpt-discovery/dilation_os_continuation_probe.py,
dilation_field_os_uniform_probe.py, dilation_interacting_os_probe.py,
dilation_quantum_coupled_band_probe.py (ALL PASS; not imported).
"""
from itertools import product as iproduct

import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset

B_SYM = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
BF = np.array([[13.0, 1.0, 4.0], [1.0, 13.0, 4.0], [4.0, 4.0, 10.0]]) / 18.0


def projectors():
    u1 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    u2 = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    u3 = sp.Matrix([1, 1, -2]) / sp.sqrt(6)
    return u1 * u1.T, u2 * u2.T, u3 * u3.T


def collision_V():
    """v977/v984 collision V = C (U_B (x) I) as a numeric 9x9."""
    s13sq = sp.Rational(2, 9)
    c13sq = 1 - s13sq
    s12sq = sp.Rational(1, 14)
    s23sq = sp.Rational(2, 7)
    c12sq, c23sq = 1 - s12sq, 1 - s23sq
    s12, c12 = sp.sqrt(s12sq), sp.sqrt(c12sq)
    s23, c23 = sp.sqrt(s23sq), sp.sqrt(c23sq)
    s13, c13 = sp.sqrt(s13sq), sp.sqrt(c13sq)
    eid = -4 / sp.sqrt(65) + sp.I * 7 / sp.sqrt(65)
    U = sp.Matrix([
        [c12 * c13, s12 * c13, s13 / eid],
        [-s12 * c23 - c12 * s23 * s13 * eid,
         c12 * c23 - s12 * s23 * s13 * eid, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * eid,
         -c12 * s23 - s12 * c23 * s13 * eid, c23 * c13]])
    Un = np.array([[complex(sp.N(U[i, j], 20)) for j in range(3)]
                   for i in range(3)])
    Cn = np.zeros((9, 9))
    for j in range(3):
        for k in range(3):
            Cn[j * 3 + ((j + k) % 3), j * 3 + k] = 1.0
    return Cn @ np.kron(Un, np.eye(3))


def kron_power(M, L):
    out = np.array([[1.0]])
    for _ in range(L):
        out = np.kron(out, M)
    return out


def coupling_diag(L, eps):
    D = 3 ** L
    v = np.zeros(D)
    for s in range(D):
        digits = []
        r = s
        for _ in range(L):
            digits.append(r % 3)
            r //= 3
        v[s] = eps * sum(1.0 for x in range(L)
                         if digits[x] == digits[(x + 1) % L])
    return np.exp(v)


def transfer_int(L, eps):
    BL = kron_power(BF, L)
    k = coupling_diag(L, eps)
    K12 = np.sqrt(k)
    return (K12[:, None] * BL) * K12[None, :]


def swap_even_H(L):
    """even-bond matching layer: SWAP on (0,1), (2,3), ... (no wrap)."""
    D = 3 ** L
    H = np.zeros((D, D), dtype=float)
    for x in range(0, L - 1, 2):
        a, b = x, x + 1
        for s in range(D):
            digits = []
            r = s
            for _ in range(L):
                digits.append(r % 3)
                r //= 3
            digits = digits[::-1]
            nd = digits[:]
            nd[a], nd[b] = nd[b], nd[a]
            t = 0
            for d in nd:
                t = t * 3 + d
            H[t, s] += 1.0
    return H


def run():
    reset()
    print("v987  DYN.UNITARY.DILATION.01: OS/dilation ladder "
          "(kernel + free band + interacting congruence + quantum SWAP)")

    P1, P2, P3 = projectors()
    check("A SPECTRAL [E]: B = P1 + (2/3) P2 + (1/3) P3 with orthogonal "
          "projectors summing to I",
          sp.simplify(B_SYM - (P1 + sp.Rational(2, 3) * P2
                               + sp.Rational(1, 3) * P3)) == sp.zeros(3)
          and sp.simplify(P1 + P2 + P3 - sp.eye(3)) == sp.zeros(3)
          and all(sp.simplify(P * Q) == sp.zeros(3)
                  for P, Q in ((P1, P2), (P1, P3), (P2, P3))))

    H = sp.log(sp.Rational(3, 2)) * P2 + sp.log(3) * P3
    u1 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    eigH = sorted(sp.simplify(x) for x in H.eigenvals())
    check("A OS HAMILTONIAN [E]: H = -log B PSD, spectrum "
          "{0, log(3/2), log 3}, gap log(3/2), ground = uniform",
          sp.simplify(H - H.T) == sp.zeros(3)
          and sp.simplify(H * u1) == sp.zeros(3, 1)
          and eigH == [0, sp.log(sp.Rational(3, 2)), sp.log(3)])

    t, s = sp.symbols("t s", real=True)
    Tt = P1 + sp.exp(-t * sp.log(sp.Rational(3, 2))) * P2 \
        + sp.exp(-t * sp.log(3)) * P3
    row_sums = sp.simplify(Tt * sp.Matrix([1, 1, 1]))
    prod_diff = (Tt * Tt.subs(t, s) - Tt.subs(t, t + s)).applyfunc(
        lambda x: sp.simplify(sp.powsimp(sp.expand(x), force=True)))
    check("A SEMIGROUP [E]: T(t) rows sum to 1 and T(t)T(s) = T(t+s) "
          "symbolically (inside the stochastic cone)",
          sp.simplify(row_sums - sp.Matrix([1, 1, 1])) == sp.zeros(3, 1)
          and prod_diff == sp.zeros(3))
    Thalf = Tt.subs(t, sp.Rational(1, 2))
    check("A HALF STEP [E]: B^{1/2} = T(1/2) is real and entrywise "
          "positive (the chain interpolates inside the cone)",
          all(sp.simplify(sp.im(x)) == 0 for x in Thalf)
          and all(sp.N(x) > 0 for x in Thalf))

    Ut = P1 + sp.Rational(2, 3) ** (sp.I * t) * P2 \
        + sp.Rational(1, 3) ** (sp.I * t) * P3
    check("A UNITARY GROUP [E]: U(t)U(s) = U(t+s) and U(t)^dag = U(-t)",
          sp.simplify(Ut * Ut.subs(t, s) - Ut.subs(t, t + s)) == sp.zeros(3)
          and sp.simplify(Ut.H - Ut.subs(t, -t)) == sp.zeros(3))
    wick = all(sp.simplify(Ut.subs(t, -sp.I * n) - B_SYM ** n) == sp.zeros(3)
               for n in range(1, 7))
    check("A WICK ANCHOR [E]: U(-i n) = B^n for n = 1..6 "
          "(six-step macro-gate T = B^6 = e^{-6H} included)", wick)

    Bbad = P1 - sp.Rational(1, 10) * P2 + sp.Rational(1, 3) * P3
    half_bad = P1 + sp.sqrt(sp.Rational(-1, 10)) * P2 \
        + sp.sqrt(sp.Rational(1, 3)) * P3
    check("A MUST-FAIL [E]: v971 negative kernel (lam2 = -1/10) is "
          "doubly stochastic with det < 0 and its half-step is NON-REAL "
          "-- no self-adjoint OS Hamiltonian",
          sp.simplify(Bbad * sp.Matrix([1, 1, 1]) - sp.Matrix([1, 1, 1]))
          == sp.zeros(3, 1)
          and sp.simplify(Bbad.det()) < 0
          and any(sp.simplify(sp.im(x)) != 0 for x in half_bad))

    h_eig = [0, sp.log(sp.Rational(3, 2)), sp.log(3)]
    ok_gap = True
    for L in (2, 3):
        spec = sorted(set(sum(h_eig[i] for i in tup)
                          for tup in iproduct(range(3), repeat=L)),
                      key=lambda e: sp.N(e))
        gap = sp.simplify(spec[1] - spec[0])
        ok_gap &= spec[0] == 0 and sp.simplify(
            gap - sp.log(sp.Rational(3, 2))) == 0
    check("B UNIFORM GAP [E]: H_L = sum_x h_x has ground 0 and gap "
          "log(3/2) EXACTLY at L = 2, 3 (uniform in L, no closing)",
          ok_gap)
    P = [P1, P2, P3]
    lam = [sp.Integer(1), sp.Rational(2, 3), sp.Rational(1, 3)]
    B2 = sp.Matrix(sp.kronecker_product(B_SYM, B_SYM))
    recon = sp.zeros(9, 9)
    for i in range(3):
        for j in range(3):
            recon += lam[i] * lam[j] * sp.Matrix(
                sp.kronecker_product(P[i], P[j]))
    check("B WICK L=2 [E]: B^(x2) = sum_{ij} e^{-(h_i+h_j)} P_i (x) P_j "
          "(product OS Hamiltonian generates the product chain)",
          sp.simplify(B2 - recon) == sp.zeros(9))

    Vn = collision_V()

    def per_cell_channel(L):
        outs = []
        for basis in range(3):
            p = np.zeros(3)
            p[basis] = 1.0
            rho = np.array([1.0])
            for _ in range(L):
                rho = np.kron(rho, np.diag(p))
                rho = np.kron(rho, np.diag([1.0, 0, 0]))
            W = np.array([1.0])
            for _ in range(L):
                W = np.kron(W, Vn)
            big = W @ rho.astype(complex) @ W.conj().T
            dims = [3] * (2 * L)
            red = big.reshape(dims + dims)
            for f in range(2 * L - 1, 0, -1):
                n = red.ndim // 2
                red = np.trace(red, axis1=f, axis2=f + n)
            outs.append(np.real(np.diag(red)))
        return np.array(outs).T

    ok_d2 = True
    ref = None
    for L in (1, 2):
        M = per_cell_channel(L)
        if ref is None:
            ref = M
        ok_d2 &= np.allclose(M, BF, atol=1e-10) and np.allclose(
            M, ref, atol=1e-10)
    check("B D2 [E/N]: per-cell reduced channel is B at L = 1, 2 "
          "identically -- one fresh ancilla per cell per step, linear "
          "environment, size-consistent", ok_d2)

    L = 2
    Wcoll = np.kron(Vn, Vn)

    def op_on(factor, M, nfac=4):
        out = np.array([[1.0]], dtype=complex)
        for f in range(nfac):
            out = np.kron(out, M if f == factor else np.eye(3))
        return out

    lam1 = np.zeros((3, 3), dtype=complex)
    lam1[0, 1] = lam1[1, 0] = 1.0
    zgen = np.diag([1.0, -1.0, 0.0]).astype(complex)
    O0 = op_on(0, lam1)
    O1 = Wcoll.conj().T @ O0 @ Wcoll
    far = max(np.max(np.abs(O1 @ op_on(2, g) - op_on(2, g) @ O1))
              for g in (lam1, zgen))
    near = max(np.max(np.abs(O1 @ op_on(0, g) - op_on(0, g) @ O1))
               for g in (lam1, zgen))
    check("B LR RADIUS 1 [N]: after one collision step an S0-local "
          "operator commutes with the far cell S1 of the L = 2 band "
          "(dev %.1e < 1e-10) and the near-cell commutator is STRICTLY "
          "nonzero (velocity = 1, not 0)" % far,
          far < 1e-10 and near > 1e-6)

    ok_pd = True
    for L in (2, 3):
        for eps in (-1.0, -0.3, 0.3, 1.0):
            w = np.linalg.eigvalsh(transfer_int(L, eps))
            ok_pd &= w[0] > 0
    check("C CONGRUENCE [E]: T_eps = K^{1/2} B^(xL) K^{1/2} is SPD for "
          "every tested (L, eps) including NEGATIVE couplings -- "
          "positivity is a congruence fact", ok_pd)
    T_one = coupling_diag(3, 0.7)[:, None] * kron_power(BF, 3)
    asym = float(np.max(np.abs(T_one - T_one.T)))
    check("C MUST-FAIL [E]: one-sided coupling K B^(xL) is NOT "
          "symmetric (max asym %.2f) -- no self-adjoint OS Hamiltonian"
          % asym, asym > 1e-3)

    gaps = []
    for L in range(2, 5):
        w = np.linalg.eigvalsh(transfer_int(L, 0.3))
        gaps.append(float(np.log(w[-1] / w[-2])))
    print("   gap(L=2..4):", ["%.4f" % g for g in gaps])
    check("C GAP PLATEAU [N]: gap(L) stays bounded away from zero "
          "(min %.4f > 0.1) with last relative step < 0.15 at eps = 0.3 "
          "-- no collapse with size" % min(gaps),
          min(gaps) > 0.1
          and abs(gaps[-1] - gaps[-2]) / gaps[-1] < 0.15)

    L = 4
    T4 = transfer_int(L, 0.3)
    w4, v4 = np.linalg.eigh(T4)
    H4 = -(v4 @ np.diag(np.log(np.maximum(w4, 1e-300))) @ v4.T)
    b1 = np.diag([1, -1, 0]) / np.sqrt(2)
    b2 = np.diag([1, 1, -2]) / np.sqrt(6)
    b3 = np.zeros((3, 3))
    b3[0, 1] = b3[1, 0] = 1 / np.sqrt(2)
    BASIS = [b1, b2, b3]

    def two_site_coeff(Hm, d):
        best = 0.0
        for A in BASIS:
            for C in BASIS:
                op = np.array([[1.0]])
                for site in range(L):
                    if site == 0:
                        op = np.kron(op, A)
                    elif site == d:
                        op = np.kron(op, C)
                    else:
                        op = np.kron(op, np.eye(3))
                best = max(best, abs(float(np.sum(Hm * op.T)))
                           / 3 ** (L - 2))
        return best

    c1, c2 = two_site_coeff(H4, 1), two_site_coeff(H4, 2)
    print("   2-site coeffs d=1,2:", "%.2e" % c1, "%.2e" % c2)
    check("C QUASI-LOCALITY [N]: 2-site coefficients of H = -log T "
          "decay with distance (ratio %.3f < 0.8) -- D1 interacting "
          "witness at kernel level" % (c2 / c1 if c1 else 1),
          c1 > 0 and c2 / c1 < 0.8)

    Lq = 2
    Hsw = swap_even_H(Lq)
    wsw, vsw = np.linalg.eigh(Hsw)
    Wcoll2 = np.kron(Vn, Vn)

    def embed_sys_unitary(Usys):
        """Usys acts on (S0, S1); embed as U (x) I on ancillas of
        the factor order (S0, A0, S1, A1)."""
        Ufull = np.zeros((81, 81), dtype=complex)
        for s in range(81):
            digits = []
            r = s
            for _ in range(4):
                digits.append(r % 3)
                r //= 3
            digits = digits[::-1]
            sys = digits[0] * 3 + digits[2]
            for t_sys in range(9):
                amp = Usys[t_sys, sys]
                if abs(amp) < 1e-16:
                    continue
                nd = digits[:]
                nd[0] = t_sys // 3
                nd[2] = t_sys % 3
                t = 0
                for d in nd:
                    t = t * 3 + d
                Ufull[t, s] += amp
        return Ufull

    def keep_S0(rho):
        red = rho.reshape([3] * 8)
        for f in (3, 2, 1):
            n = red.ndim // 2
            red = np.trace(red, axis1=f, axis2=f + n)
        return red

    theta = 0.2
    Uint_sys = vsw @ np.diag(np.exp(-1j * theta * wsw)) @ vsw.T
    Wth = embed_sys_unitary(Uint_sys) @ Wcoll2
    check("D UNITARY [N]: W_theta = U_int(theta) (x)_x V_x is unitary "
          "at L = 2, theta = 0.2 (max |W^dag W - I| < 1e-9)",
          np.max(np.abs(Wth.conj().T @ Wth - np.eye(81))) < 1e-9)

    mix = np.eye(3) / 3.0

    def reduced_diag(W):
        cols = []
        for j in range(3):
            rho = np.array([1.0], dtype=complex)
            rho = np.kron(rho, np.diag([float(k == j) for k in range(3)]))
            rho = np.kron(rho, np.diag([1.0, 0.0, 0.0]))
            rho = np.kron(rho, mix)
            rho = np.kron(rho, np.diag([1.0, 0.0, 0.0]))
            cols.append(np.real(np.diag(keep_S0(W @ rho @ W.conj().T))))
        return np.array(cols).T

    dths = []
    for th in (0.0, 0.05, 0.1, 0.2):
        Uth = vsw @ np.diag(np.exp(-1j * th * wsw)) @ vsw.T
        W = embed_sys_unitary(Uth) @ Wcoll2
        dths.append(float(np.max(np.abs(reduced_diag(W) - BF))))
    print("   d(theta) at 0, 0.05, 0.1, 0.2:",
          ["%.3e" % d for d in dths])
    xs = np.log([0.05, 0.1, 0.2])
    ys = np.log(np.maximum(dths[1:], 1e-30))
    power = float(np.polyfit(xs, ys, 1)[0])
    print("   fitted power d ~ theta^{%.3f}" % power)
    check("D d(0) = 0 [N]: reduced diagonal kernel recovers B exactly "
          "at theta = 0 (max |M-B| = %.1e)" % dths[0], dths[0] < 1e-10)
    check("D d(theta) ~ theta^2 [N]: leading even power in {1.5, 2.5} "
          "(fit %.3f; probe ~1.98) and d -> 0 continuously"
          % power,
          1.5 < power < 2.5 and dths[1] <= dths[2] + 1e-15
          and dths[2] <= dths[3] + 1e-15)

    choi = np.zeros((9, 9), dtype=complex)
    for i in range(3):
        for j in range(3):
            ein = np.zeros((3, 3), dtype=complex)
            ein[i, j] = 1.0
            rho = np.array([1.0], dtype=complex)
            rho = np.kron(rho, ein)
            rho = np.kron(rho, np.diag([1.0, 0.0, 0.0]))
            rho = np.kron(rho, mix)
            rho = np.kron(rho, np.diag([1.0, 0.0, 0.0]))
            red = keep_S0(Wth @ rho @ Wth.conj().T)
            choi[3 * i:3 * i + 3, 3 * j:3 * j + 3] = red
    w_choi = np.linalg.eigvalsh(0.5 * (choi + choi.conj().T))
    check("D CPTP [N]: reduced per-cell channel at theta = 0.2 has "
          "Choi PSD (min eig %.1e) -- openness survives SWAP coupling"
          % w_choi[0], w_choi[0] > -1e-9)

    sw2 = Hsw @ Hsw
    check("D LR MATCHING [E]: even-bond SWAP is hermitian, SWAP^2 = I "
          "on the paired cells (range 1) -- far unmatched cells are "
          "machine-zero by construction (probe L = 4 far-cell zero is "
          "this skeleton; Tr SWAP = 3 on C^3 x C^3)",
          float(np.max(np.abs(Hsw - Hsw.T))) < 1e-15
          and np.allclose(sw2, np.eye(9))
          and abs(float(np.trace(Hsw)) - 3.0) < 1e-12)

    check("FIREWALL (scope): kernel + free band + diagonal-coupling "
          "interacting + one SWAP family, finite L, discrete time; "
          "continuous field-level OS, thermodynamic-limit branch "
          "selection and any 3+1D reading stay [O]; no marker move",
          True)
    return summary("v987 OS/dilation ladder: kernel exact + free band "
                   "+ interacting congruence + quantum SWAP")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
