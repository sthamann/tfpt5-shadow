#!/usr/bin/env python3
"""dilation_interacting_os_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (DYN.UNITARY.DILATION.01 / QFT4D.OS.RECON.01 [O], the
INTERACTING field level after dilation_field_os_uniform_probe executed
the free/product level): does the OS continuation survive COUPLING the
seam cells?  Construction: the interacting transfer matrix

    T_eps = K^{1/2} (B^{(x)L}) K^{1/2},
    K = diag exp(eps * sum_x delta(s_x, s_{x+1}))   (ring, ferromagnetic
                                                     alignment coupling)

-- a genuine 1+1D classical statistical system (space L cells, discrete
time), whose OS Hamiltonian is H_eps = -log T_eps.

  (1) OS POSITIVITY BY CONGRUENCE, EXACT: K^{1/2} B^{(x)L} K^{1/2} is
      symmetric positive definite for EVERY real eps (congruence of a
      PD matrix) -- the whole diagonal-coupling family passes the T2/OS
      gate STRUCTURALLY; must-fail: the one-sided (non-symmetric)
      coupling K B^{(x)L} admits no self-adjoint OS Hamiltonian.
  (2) UNIFORM GAP MEASURED: gap(L) = -log(lambda_2/lambda_1) of T_eps
      at eps = 0.3 for L = 2..6 -- bounded away from zero, approaching
      a plateau (no gap collapse with size).
  (3) QUASI-LOCALITY OF H MEASURED: the two-site coefficients of
      H_eps = -log T_eps in the traceless product-operator basis decay
      with distance d (max |coeff(A_0, C_d)| vs d, L = 6) -- the OS
      Hamiltonian of the interacting chain is quasi-local, the D1
      demand at interacting-kernel level.

HONEST BOUNDARY (firewall): classical-kernel (diagonal-coupling) level;
the QUANTUM interacting field level (coupled collision bands with
non-diagonal interactions) and the operator-algebraic OS reconstruction
stay [O].  No marker moves.

VERDICT ENUM: INTERACTING_OS_KERNEL_LEVEL_EXECUTED (quantum level open).
"""
import numpy as np

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


Bf = np.array([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
EPS = 0.3


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


def transfer(L, eps):
    BL = kron_power(Bf, L)
    k = coupling_diag(L, eps)
    K12 = np.sqrt(k)
    return (K12[:, None] * BL) * K12[None, :]


# ---------------------------------------------------------------- (1)
print("=== (1) OS positivity by congruence (exact structure) ===")
ok_pd = True
for L in (2, 3, 4):
    for eps in (-1.0, -0.3, 0.3, 1.0, 3.0):
        w = np.linalg.eigvalsh(transfer(L, eps))
        ok_pd &= w[0] > 0
rep("T_eps = K^{1/2} B^(xL) K^{1/2} is symmetric PD for every tested "
    "(L, eps) incl. strong and NEGATIVE couplings -- positivity is a "
    "CONGRUENCE fact (B^(xL) PD, K diagonal positive): the whole "
    "diagonal-coupling family passes the OS gate structurally", ok_pd)

T_one = coupling_diag(3, 0.7)[:, None] * kron_power(Bf, 3)
asym = float(np.max(np.abs(T_one - T_one.T)))
rep("MUST-FAIL FIRES: the one-sided coupling K B^(xL) is NOT symmetric "
    "(max asym %.2f) -- no self-adjoint OS Hamiltonian; the symmetric "
    "K^{1/2} . K^{1/2} splitting is what OS consumes" % asym,
    asym > 1e-3)

# ---------------------------------------------------------------- (2)
print("=== (2) uniform gap, eps = 0.3, L = 2..6 ===")
gaps = {}
for L in range(2, 7):
    w = np.linalg.eigvalsh(transfer(L, EPS))
    gaps[L] = float(np.log(w[-1] / w[-2]))
print("   gap(L):", {L: "%.4f" % gaps[L] for L in gaps})
gvals = [gaps[L] for L in range(2, 7)]
plateau = abs(gvals[-1] - gvals[-2]) / gvals[-1]
rep("gap(L) stays bounded away from zero and approaches a plateau "
    "(min %.4f > 0.1; last relative step %.1e) -- no gap collapse with "
    "system size at eps = 0.3" % (min(gvals), plateau),
    min(gvals) > 0.1 and plateau < 0.05)

# ---------------------------------------------------------------- (3)
print("=== (3) quasi-locality of H = -log T (L = 6, dim 729) ===")
L = 6
T6 = transfer(L, EPS)
w6, v6 = np.linalg.eigh(T6)
H6 = -(v6 @ np.diag(np.log(w6)) @ v6.T)

# orthonormal traceless single-site basis (Gell-Mann-like, real sym +
# diagonal ones suffice since H is real symmetric)
b1 = np.diag([1, -1, 0]) / np.sqrt(2)
b2 = np.diag([1, 1, -2]) / np.sqrt(6)
b3 = np.zeros((3, 3))
b3[0, 1] = b3[1, 0] = 1 / np.sqrt(2)
b4 = np.zeros((3, 3))
b4[0, 2] = b4[2, 0] = 1 / np.sqrt(2)
b5 = np.zeros((3, 3))
b5[1, 2] = b5[2, 1] = 1 / np.sqrt(2)
BASIS = [b1, b2, b3, b4, b5]


def two_site_coeff(Hm, d):
    """max over basis pairs of |Tr(H (A_0 (x) C_d (x) I))| / 3^{L-2}."""
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
            best = max(best, abs(float(np.sum(Hm * op.T))) / 3 ** (L - 2))
    return best


coeffs = {d: two_site_coeff(H6, d) for d in range(1, 4)}
print("   max 2-site coefficient vs distance:",
      {d: "%.2e" % coeffs[d] for d in coeffs})
decay1 = coeffs[2] / coeffs[1]
decay2 = coeffs[3] / coeffs[2]
rep("QUASI-LOCALITY MEASURED: the 2-site coefficients of H = -log T "
    "decay with distance (ratios %.3f, %.3f < 1) -- the interacting OS "
    "Hamiltonian is quasi-local at kernel level (D1 interacting "
    "witness)" % (decay1, decay2),
    decay1 < 0.8 and decay2 < 0.8)

print()
print("VERDICT: INTERACTING_OS_KERNEL_LEVEL_EXECUTED -- symmetric "
      "diagonal couplings keep the OS gate structurally, the gap is "
      "size-stable, and -log T is measurably quasi-local; the QUANTUM "
      "interacting level stays [O]; no promotion")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
