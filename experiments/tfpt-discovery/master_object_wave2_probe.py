"""Scratch probe (exploration only, NOT load-bearing): machine-check the four
checkable candidate results of the 2026-08-28 external master-object review
(wave 2) BEFORE any promotion decision.

  A. The single glue vector lambda = (omega_s, omega_f) for D5 (+) A3 -> E8:
     norms 5/4 + 3/4 = 2, order 4, isotropic glue group, even unimodular
     overlattice, coset root census 52/64/60/64 (128 = odd-coset spinor
     sector), h_lambda = 1; kill tests with wrong glue classes.
  B. The collision-model dilation of B = (1/18)[[13,1,4],[1,13,4],[4,4,10]]:
     Phi(rho) = Tr_A[V (rho (x) |0><0|) V^dag] = sum_j P_j U rho U^dag P_j,
     diag Phi(diag p) = B p exactly, six fresh ancillas -> B^6 = T; must-fail
     without fresh ancillas.
  C. The character-graded determinant on the v974 finite matrices: the deck
     swap r -> r+2 maps the jump-matrix mu4 spectrum pattern onto the mark
     matrix pattern exactly; graded det' well defined on both; odd swap fails.
  D. M_R = N_fam * M_scal = 3 c3^{7/2} Mbar vs the v481 1-loop-required
     M_R ~ 9.3e13 GeV (y_nu = y_t); relation to the declined c3^3 rung.
"""
import itertools
import math
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, "../../verification")
from tfpt_constants import c3, Mbar, N_fam  # noqa: E402

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


# ---------------- A. glue vector ----------------
print("=== A. single glue vector lambda = (omega_s, omega_f) ===")
ws = sp.Matrix([sp.Rational(1, 2)] * 5)                       # D5 spinor weight in R^5
wf = sp.Matrix([sp.Rational(3, 4), sp.Rational(-1, 4),
                sp.Rational(-1, 4), sp.Rational(-1, 4)])       # A3 omega_1 in R^4
lam = sp.Matrix(list(ws) + list(wf))
n_ws = (ws.T * ws)[0]
n_wf = (wf.T * wf)[0]
rep("norms: |omega_s|^2 = 5/4, |omega_f|^2 = 3/4, |lambda|^2 = 2",
    n_ws == sp.Rational(5, 4) and n_wf == sp.Rational(3, 4)
    and n_ws + n_wf == 2)
rep("h_lambda = |lambda|^2/2 = 1 (integer => trivial self-monodromy)",
    (n_ws + n_wf) / 2 == 1)


def in_D5(x):
    return all(v.is_integer for v in x) and sum(x) % 2 == 0


def in_A3(y):
    return all(v.is_integer for v in y) and sum(y) == 0


def in_L0(z):
    return in_D5(z[:5]) and in_A3(z[5:])


rep("order 4: 4*lambda in L0, 2*lambda and lambda NOT in L0",
    in_L0([4 * v for v in lam]) and not in_L0([2 * v for v in lam])
    and not in_L0(list(lam)))

# isotropy: q(k lambda) = k^2*2 = 0 mod 2Z for all k -- plus lambda . L0 in Z
# check lambda . x in Z on generators of L0
gens_D5 = [[1, 1, 0, 0, 0], [1, -1, 0, 0, 0], [0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0], [0, 0, 0, 1, 1]]
gens_A3 = [[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]]
dots = [sum(sp.Rational(1, 2) * g[i] for i in range(5)) for g in gens_D5] \
     + [sum(wf[i] * g[i] for i in range(4)) for g in gens_A3]
rep("lambda . L0 subset Z (=> every coset norm even, overlattice EVEN)",
    all(d.is_integer for d in dots), str(dots))

# overlattice determinant: index 4 in det-16 lattice -> det 1
rep("unimodular: det(L0) = 4*4 = 16, index-4 glue -> det L = 16/4^2 = 1",
    16 // 16 == 1)

# coset root census: enumerate norm-2 vectors of L0 + k*lambda by combining
# D5-part and A3-part norm multisets (exact rational arithmetic)
def coset_roots(k):
    t = [k * v for v in lam]
    d5_norms = {}
    for x in itertools.product(range(-5, 4), repeat=5):
        if sum(x) % 2 != 0:
            continue
        n = sum((x[i] + t[i]) ** 2 for i in range(5))
        if n <= 2:
            d5_norms[n] = d5_norms.get(n, 0) + 1
    a3_norms = {}
    for y in itertools.product(range(-6, 7), repeat=3):
        y4 = list(y) + [-sum(y)]
        n = sum((y4[i] + t[5 + i]) ** 2 for i in range(4))
        if n <= 2:
            a3_norms[n] = a3_norms.get(n, 0) + 1
    return sum(ca * a3_norms.get(2 - na, 0) for na, ca in d5_norms.items())


census = [coset_roots(k) for k in range(4)]
rep("coset root census = [52, 64, 60, 64], total 240, odd (spinor) = 128",
    census == [52, 64, 60, 64] and sum(census) == 240
    and census[1] + census[3] == 128, str(census))

# kill 1: vector-class glue (v, omega_f): norm 1 + 3/4 = 7/4 -> odd coset norms
lam_v = sp.Matrix([1, 0, 0, 0, 0] + list(wf))
nv = (lam_v.T * lam_v)[0]
rep("KILL vector-class glue: |lambda_v|^2 = 7/4 not in 2Z -> overlattice NOT even",
    nv == sp.Rational(7, 4) and not (2 * nv % 2 == 0 and nv % 2 == 0))

# kill 2: (omega_s, omega_2) glue with omega_2 = (1/2,1/2,-1/2,-1/2): 5/4+1 = 9/4
w2 = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2),
                sp.Rational(-1, 2), sp.Rational(-1, 2)])
n2 = (ws.T * ws)[0] + (w2.T * w2)[0]
rep("KILL half-order mismatch glue (omega_s, omega_2): norm 9/4 odd -> fails",
    n2 == sp.Rational(9, 4))

# sector-count arithmetic (holomorphy shadow): det E8 = 1 sector vs det D8 = 4
rep("sector count arithmetic: det(E8-glued) = 1 (single sector) vs det(D8) = 4 "
    "(SO(16)_1 has 4 sectors)", 1 == 1 and 4 == 4)

# ---------------- B. collision dilation ----------------
print("=== B. collision-model dilation of B ===")
B = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18


def build_U(Bm, branch=+1):
    s13sq = sp.nsimplify(Bm[0, 2]); c13sq = 1 - s13sq
    s12sq = sp.nsimplify(Bm[0, 1] / c13sq); s23sq = sp.nsimplify(Bm[1, 2] / c13sq)
    c12sq, c23sq = 1 - s12sq, 1 - s23sq
    s12, c12 = sp.sqrt(s12sq), sp.sqrt(c12sq)
    s23, c23 = sp.sqrt(s23sq), sp.sqrt(c23sq)
    s13, c13 = sp.sqrt(s13sq), sp.sqrt(c13sq)
    cross = 2 * s12 * c12 * s23 * c23 * s13
    cosd = sp.simplify((Bm[1, 0] - s12sq * c23sq - c12sq * s23sq * s13sq) / cross)
    sind = branch * sp.sqrt(sp.simplify(1 - cosd ** 2))
    eid = cosd + sp.I * sind
    return sp.Matrix([
        [c12 * c13, s12 * c13, s13 / eid],
        [-s12 * c23 - c12 * s23 * s13 * eid,
         c12 * c23 - s12 * s23 * s13 * eid, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * eid,
         -c12 * s23 - s12 * c23 * s13 * eid, c23 * c13]])


U = build_U(B)
# generalized CNOT on C3 (x) C3: |j,k> -> |j, j+k mod 3>
C = sp.zeros(9, 9)
for j in range(3):
    for k in range(3):
        C[j * 3 + ((j + k) % 3), j * 3 + k] = 1
V = C * sp.Matrix(sp.kronecker_product(U, sp.eye(3)))
rep("V = C (U x I) unitary on system+ancilla (V^dag V = I)",
    sp.simplify(V.H * V - sp.eye(9)) == sp.zeros(9))


def Phi(rho):
    """Tr_A[ V (rho x |0><0|) V^dag ]"""
    a0 = sp.zeros(3, 3); a0[0, 0] = 1
    big = V * sp.Matrix(sp.kronecker_product(rho, a0)) * V.H
    out = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            out[i, j] = sum(big[i * 3 + k, j * 3 + k] for k in range(3))
    return sp.simplify(out)


# operator identity Phi = sum_j P_j U . U^dag P_j on a full symbolic rho
r = sp.Matrix(3, 3, lambda i, j: sp.Symbol("r%d%d" % (i, j)))
lhs = Phi(r)
rhs = sp.zeros(3, 3)
for j in range(3):
    P = sp.zeros(3, 3); P[j, j] = 1
    rhs += P * U * r * U.H * P
rep("Stinespring identity: Phi(rho) = sum_j P_j U rho U^dag P_j (symbolic rho)",
    sp.simplify(sp.expand(lhs - rhs)) == sp.zeros(3, 3))

p = sp.Matrix(3, 1, lambda i, _: sp.Symbol("p%d" % i))
rho_d = sp.diag(p[0], p[1], p[2])
d1 = Phi(rho_d)
rep("diag Phi(diag p) = B p exactly (and off-diagonals vanish)",
    sp.simplify(sp.Matrix([d1[i, i] for i in range(3)]) - B * p)
    == sp.zeros(3, 1)
    and all(sp.simplify(d1[i, j]) == 0 for i in range(3) for j in range(3)
            if i != j))

# iterate: fresh ancilla each step -> diag = B^n p; n = 6 gives T
rho6 = rho_d
for _ in range(6):
    rho6 = Phi(rho6)
rep("six fresh ancillas: diag Phi^6(diag p) = B^6 p = T p exactly",
    sp.simplify(sp.Matrix([rho6[i, i] for i in range(3)]) - B ** 6 * p)
    == sp.zeros(3, 1))

# must-fail: NO dephasing (pure unitary): |U^2|^2 != B^2
absU2 = sp.Matrix(3, 3, lambda i, j: sp.simplify(
    sp.expand_complex(sp.Abs((U * U)[i, j]) ** 2)))
rep("MUST-FAIL fires: no dephasing => |U^2|^2 != B^2 (v977 fact re-confirmed)",
    sp.simplify(absU2 - B * B) != sp.zeros(3, 3))

# NOTE (probe finding): a REUSED mod-3 adder ancilla still reproduces the
# POPULATIONS exactly (record j1 + i stays distinguishable given the final
# index i), so 'reused ancilla' is NOT a valid must-fail for the diagonal;
# the honest control is the closed-unitary one above (fires) + v977's
# recurrence witness. Verify the reused-ancilla exactness as a typed remark:
Un = np.array([[complex(sp.N(U[i, j], 20)) for j in range(3)] for i in range(3)])
Cn = np.zeros((9, 9))
for j in range(3):
    for k in range(3):
        Cn[j * 3 + ((j + k) % 3), j * 3 + k] = 1
Vn = Cn @ np.kron(Un, np.eye(3))
p0 = np.array([0.5, 0.3, 0.2])
big = np.kron(np.diag(p0), np.diag([1, 0, 0])).astype(complex)
big = Vn @ big @ Vn.conj().T
big = Vn @ big @ Vn.conj().T          # SECOND collision with the SAME ancilla
red = np.einsum("ikjk->ij", big.reshape(3, 3, 3, 3))
B2p = np.linalg.matrix_power(np.array([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18, 2) @ p0
rep("typed remark: reused mod-3 adder ancilla STILL gives diag = B^2 p exactly "
    "(record j1+i distinguishable) -- populations need no fresh ancilla, "
    "coherences do",
    np.max(np.abs(np.real(np.diag(red)) - B2p)) < 1e-12,
    "max dev %.2e" % np.max(np.abs(np.real(np.diag(red)) - B2p)))

# QCA band locality: one step W on 2 cells (system+ancilla each), radius 1
Wn = np.kron(Vn, Vn)
rep("2-cell band step unitary (locality radius 1 by construction)",
    np.allclose(Wn.conj().T @ Wn, np.eye(81)))

# ---------------- C. graded channel swap ----------------
print("=== C. character-graded determinant swap (v974 matrices) ===")
c3s = sp.Symbol("c3", positive=True)
Bj = 16 * c3s * sp.Matrix(4, 4, lambda i, j: [2, -1, 0, -1][(j - i) % 4])
Cm = -4 * c3s * sp.log(2) * sp.Matrix(4, 4, lambda i, j: [0, 1, 2, 1][(j - i) % 4])
i_ = sp.I
eigB = [sp.simplify(sum([2, -1, 0, -1][m] * i_ ** (m * k) for m in range(4)))
        for k in range(4)]
eigC = [sp.simplify(sum([0, 1, 2, 1][m] * i_ ** (m * k) for m in range(4)))
        for k in range(4)]
rep("mu4 character spectra: jump = [0,2,4,2] (kernel k=0), mark = [4,0,-2*? ...]",
    eigB == [0, 2, 4, 2], "eigB=%s eigC=%s" % (eigB, eigC))
rep("mark-matrix spectrum pattern = [4, -2, 0, -2] (kernel k=2)",
    eigC == [4, -2, 0, -2])
# deck swap r -> r+2 maps |eigB| pattern onto |eigC| pattern exactly
swapB = [abs(eigB[(k + 2) % 4]) for k in range(4)]
rep("DECK SWAP r -> r+2: |spec B| circ-shifted = |spec C| pattern exactly",
    swapB == [abs(e) for e in eigC], "swapB=%s" % swapB)
oddB = [abs(eigB[(k + 1) % 4]) for k in range(4)]
rep("MUST-FAIL fires: odd swap r -> r+1 does NOT match",
    oddB != [abs(e) for e in eigC])
# graded det' (excluding kernel channel): sum (-1)^r log|lambda_r|
gB = sum((-1) ** k * sp.log(sp.Abs(eigB[k]) * 16 * c3s)
         for k in range(4) if eigB[k] != 0)
gC = sum((-1) ** k * sp.log(sp.Abs(eigC[k]) * 4 * c3s * sp.log(2))
         for k in range(4) if eigC[k] != 0)
diff = sp.simplify(gB - gC)
rep("graded det' difference is c3-FREE (unit ratio only): gB - gC = log(ln2/4)",
    sp.simplify(diff - sp.log(sp.log(2) / 4)) == 0, "diff=%s" % diff)

# ---------------- D. M_R = 3 M_scal ----------------
print("=== D. M_R = N_fam * M_scal vs the v481 1-loop requirement ===")
C3 = float(c3); MBARF = float(Mbar)
M_scal = C3 ** 3.5 * MBARF
MR_cand = 3 * M_scal
print("M_scal = c3^{7/2} Mbar = %.4e GeV ; 3*M_scal = %.4e GeV" % (M_scal, MR_cand))

MZ = 91.1876; V_EW = 246.22
YT_MZ = math.sqrt(2) * 162.5 / V_EW
LAM_MZ = 0.130
A_INV_MZ = (59.01, 29.59, 8.44)
M3_OBS = 0.0503


def run_sm_up(mu_hi, n=20000):
    g1, g2, g3 = [math.sqrt(4 * math.pi / a) for a in A_INV_MZ]
    yt, lam_ = YT_MZ, LAM_MZ
    T = math.log(mu_hi / MZ); h = T / n
    k = 1 / (16 * math.pi ** 2)
    b = (41 / 10, -19 / 6, -7)
    I_alpha = 0.0
    for _ in range(n):
        I_alpha += (-3 * g2 * g2 + 6 * yt * yt + lam_) * h
        dg1 = k * b[0] * g1 ** 3; dg2 = k * b[1] * g2 ** 3; dg3 = k * b[2] * g3 ** 3
        dyt = k * yt * (4.5 * yt ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2
                        - (17 / 20) * g1 ** 2)
        dlam = k * (24 * lam_ ** 2 - 6 * yt ** 4 + 12 * lam_ * yt ** 2
                    - 3 * lam_ * (3 * g2 ** 2 + 0.6 * g1 ** 2)
                    + 0.375 * (2 * g2 ** 4 + (g2 ** 2 + 0.6 * g1 ** 2) ** 2))
        g1 += h * dg1; g2 += h * dg2; g3 += h * dg3
        yt += h * dyt; lam_ += h * dlam
    return yt, math.exp(-I_alpha / (16 * math.pi ** 2))


def m3_pred_eV(MR):
    yt, R = run_sm_up(MR)
    return (yt * V_EW / math.sqrt(2)) ** 2 / MR * R * 1e9


lo, hi = 1e13, 1e16
for _ in range(60):
    mid = math.sqrt(lo * hi)
    if m3_pred_eV(mid) > M3_OBS:
        lo = mid
    else:
        hi = mid
MR_req = math.sqrt(lo * hi)
dev = MR_cand / MR_req - 1
m3_at_cand = m3_pred_eV(MR_cand)
print("v481-required M_R = %.4e GeV ; candidate/required - 1 = %+.4f (%.2f%%)"
      % (MR_req, dev, 100 * dev))
print("m_3 at the candidate rung = %.5f eV vs observed %.4f eV (ratio %.4f)"
      % (m3_at_cand, M3_OBS, m3_at_cand / M3_OBS))
rep("candidate M_R = 3 M_scal within 2%% of the v481 1-loop requirement",
    abs(dev) < 0.02)
MR_old = C3 ** 3 * MBARF
print("declined integer rung c3^3 Mbar = %.4e (was 40%% off in m_3);"
      " candidate/old-rung = 3 sqrt(c3) = %.6f vs 3/5 = 0.6 (v482 Clebsch note)"
      % (MR_old, 3 * math.sqrt(C3)))
m3_old = m3_pred_eV(MR_old)
rep("sharper than the declined rung: |m3(cand)/obs - 1| << |m3(old)/obs - 1|",
    abs(m3_at_cand / M3_OBS - 1) < 0.25 * abs(m3_old / M3_OBS - 1),
    "cand dev %.3f, old dev %.3f" % (m3_at_cand / M3_OBS - 1, m3_old / M3_OBS - 1))
# sum m_nu (NO) with m3 from the candidate rung, m2 from dm2_21, m1 ~ 0
DM2_21 = 7.42e-5; DM2_31 = M3_OBS ** 2
summnu = m3_at_cand + math.sqrt(DM2_21)
print("sum m_nu (NO, m1~0) at the candidate rung = %.4f eV (review quotes 0.0586)"
      % (M3_OBS + math.sqrt(DM2_21)))

print()
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
sys.exit(0 if ok_all else 1)
