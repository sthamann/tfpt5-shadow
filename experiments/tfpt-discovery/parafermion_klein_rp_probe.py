#!/usr/bin/env python3
"""Discovery probe: parafermionic Klein-twist reflection positivity of
the Z3 twist sector -- the precise RP question left open by
orbifold_twist_ope_probe.py S4 (the naive antiunitary mirror pairing is
indefinite, N-stable min/max ~ -4.5e-3; the Z2 control is exactly PSD).

THE CONSTRUCTION (three sentences):

  1. On the seam-double chain (complex free fermion, NS sector, half
     filling -- the lattice of orbifold_twist_ope_probe.py), the twist
     field sigma_k(x) is the zero-mode-dressed axis string
     sigma_k(x) = exp(i lam_k (N_[b, b+x) - x/2)), lam_k = 2 pi k/3,
     supported in the right half of the bond-centered diameter
     reflection r(j) = 2b - 1 - j (v622 cut geometry, axis bond b; all
     coordinates even).
  2. The bond reflection reverses the string orientation and therefore
     flips the endpoint winding, and the antilinear conjugation flips
     it AGAIN -- so the naive antiunitary pairing pairs sigma_k with
     sigma_k (SAME Z3 charge) and pins a spurious e^{2 i lam} defect on
     the axis bond; for Z2 this is invisible (e^{-i pi N} = e^{+i pi N}
     identically), which is exactly why the predecessor's Z2 control
     was PSD while the Z3 sector failed.
  3. The parafermionic Klein-twist pairing composes the mirror with
     charge conjugation (particle-hole): Theta_K(sigma_k(x)) =
     eta_k sigma_{3-k}(r(x)) = reflected support with the SAME string
     angle lam_k plus the zero-mode phase omega^{-k (x/2 mod 3)} (the
     "omega^{k q}" phases, q = half-position mod 3) -- the glued
     configuration is then the single smooth flux line
     <sigma_{3-k}(theta x) sigma_k(y)> through the axis, and the exact
     particle-hole identity <e^{i u N_S}> = e^{i u |S|} <e^{-i u N_S}>
     (I - C = D C D, D = diag((-1)^j), at half filling) makes every
     dressed Gram entry EXACTLY real.

Checks:

  (K0) MACHINERY / STRUCTURE [exact]: (i) the dressed-string reality
       identity at machine precision for random multi-arc, mixed-angle
       configurations; (ii) for lam = pi the naive and Klein pairings
       COINCIDE identically (the Z2 control of the predecessor could
       not distinguish them); (iii) axis-defect bookkeeping: the naive
       glued configuration carries the spurious axis jump 2 lam != 0
       mod 2 pi, the Klein glue is defect-free.

  (K1) KLEIN PSD OF THE CHARGED BLOCKS [numeric]: the sector-diagonal
       Gram G^(k)_ij = <sigma_{3-k}(theta x_i) sigma_k(x_j)> (charge
       conservation: only the -k+l = 0 mod 3 blocks are nontrivial)
       is exactly real symmetric and PSD (eigenvalue floor -1e-10
       relative) for k = 1, 2, on BOTH diameter axes (through-mark
       b = 0 and between-mark b = N/8), at N = 48/96/192/384; the two
       charge blocks coincide exactly (charge conjugation) and the two
       axes coincide exactly (translation invariance of the seam
       double -- the mark distinction lives in the covering
       bookkeeping, not in the free chain).

  (K2) THE PHASE SCAN [numeric, uniqueness]: over the finite family
       (eta_1, eta_2) in {+-1, +-omega, +-omega^2}^2, EXACTLY ONE pair
       satisfies {Klein consistency eta_k eta_{3-k}* = 1, Hermiticity,
       PSD}: eta = (1, 1) on top of the omega^{k q} zero-mode dressing.
       Sharpening: (a) NO phase in the family rescues the NAIVE
       pairing (both Hermitian choices stay indefinite -- the fix is
       structural charge conjugation, not a phase); (b) on the 6Z
       sub-grid the bare sigma-dagger pairing is already PSD (the
       dressing is trivial there), while off the 6Z grid the bare
       pairing is NOT Hermitian and the omega^{-k (x/2 mod 3)}
       dressing is exactly what restores reality.

  (K3) N-STABILITY [numeric]: the K1 minimal eigenvalues at
       N = 48/96/192/384 stay above the -1e-10 relative floor and do
       not drift towards 0^-.

  (K4) MUST-FAIL CONTROLS [numeric]: (a) the naive pairing reproduces
       the predecessor violation (charged axis strings min/max
       ~ -4.5e-3 at N = 96/192/384, N-stable; neutral pairs
       ~ -2.5e-2); (b) the deliberately wrong phases fail: eta = -1
       flips the spectrum (PSD lost), eta = omega breaks Hermiticity.

  (K5) THE MIXED SECTOR / LATTICE OS STATEMENT [numeric]: the FULL
       Gram over {1, sigma_1(x_i), sigma_2(x_i)} (+ neutral
       sigma-dagger-sigma dipoles at N = 48/96), with NO sector
       projection (all cross blocks kept as lattice numbers), is real
       symmetric and PSD under the Klein pairing; Z2 mixed control
       likewise.

  (K6) TYPING [C]: what stands and what is still open for the full
       CFT-level statement (continuum OS reconstruction, R /
       fermion-parity sectors, modularity, non-abelian content).

Verdict enums (frozen): KLEIN-RP-POSITIVE (K1-K5 pass incl. the mixed
OS matrix), KLEIN-RP-SECTOR-ONLY (K1-K4 pass, mixed K5 fails),
KLEIN-RP-FAILS (the Klein pairing itself is not PSD), MIXED (controls
break).

FIREWALL: experiments/ only; GATE.QGEO does not move; no marker
changes; verification/ untouched.

Machinery (cov, string_det) copied verbatim from
experiments/tfpt-discovery/orbifold_twist_ope_probe.py (read-only
predecessor of another worker; conventions h_sigma = 1/36,
Delta = 1/9, lam = 2 pi/3 unchanged).
"""

import numpy as np

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------------ constants
LAM = 2.0 * np.pi / 3.0                       # Z3 twist string angle
LAMK = {1: LAM, 2: 2.0 * LAM, "z2": np.pi}    # sector -> string angle
OMEGA = np.exp(2j * np.pi / 3.0)
ROOTS6 = [np.exp(1j * np.pi * j / 3.0) for j in range(6)]
ROOT_LBL = ["+1", "-w2", "+w", "-1", "+w2", "-w"]
TOL_MACH = 1e-10                              # machine-precision identities
TOL_RP = 1e-10                                # RP eigenvalue floor (relative)
TOL_EQ = 1e-9                                 # exact-symmetry equalities
N_LIST = (48, 96, 192, 384)
RNG = np.random.default_rng(61)


# ------------------------------------------------------------------ machinery
def cov(N):
    """NS (antiperiodic) half-filled covariance <c^dag_j c_l> on N sites
    (verbatim orbifold_twist_ope_probe.py)."""
    assert N % 4 == 0
    m = np.arange(-(N // 4), N // 4)
    k = 2.0 * np.pi * (m + 0.5) / N
    j = np.arange(N)
    V = np.exp(1j * np.outer(k, j)) / np.sqrt(N)
    return V.conj().T @ V


def string_det(C, sites, u):
    """<prod_{j in sites} e^{i u_j n_j}> = det(I + D C_S), D = diag(e^{iu}-1)."""
    S = np.asarray(sites, dtype=int)
    Cs = C[np.ix_(S, S)]
    M = np.eye(len(S), dtype=complex) \
        + (np.exp(1j * np.asarray(u, dtype=float)) - 1.0)[:, None] * Cs
    return np.linalg.det(M)


COVS = {Nv: cov(Nv) for Nv in N_LIST}


def xgrid(N):
    """11 even right-half insertion points, the predecessor grid scaled."""
    return [4 * i * N // 96 for i in range(1, 12)]


def dip_pairs(N):
    """Neutral sigma^dag-sigma dipole windows, predecessor PAIRS scaled."""
    return [(s * N // 96, (s + l) * N // 96)
            for s in (0, 4, 8, 16, 24) for l in (4, 8, 16) if s + l <= 48]


def ket_ops(el, b, N):
    """Right-half string realization of a basis element at axis bond b."""
    if el[0] == "id":
        return []
    if el[0] == "sig":
        _, k, x = el
        return [(np.arange(b, b + x) % N, LAMK[k])]
    _, k, a1, a2 = el
    return [(np.arange(b + a1, b + a2) % N, LAMK[k])]


def bra_ops(el, b, N, klein):
    """Reflected (left-half) string: Klein keeps the angle (+lam_k, the
    charge-conjugated anti-twist), naive flips it to -lam_k."""
    if el[0] == "id":
        return []
    if el[0] == "sig":
        _, k, x = el
        ang = LAMK[k] if klein else -LAMK[k]
        return [(np.arange(b - x, b) % N, ang)]
    _, k, a1, a2 = el
    ang = LAMK[k] if klein else -LAMK[k]
    return [(np.arange(b - a2, b - a1) % N, ang)]


def gram(N, b, els, klein=True, dress=True):
    """Mirror Gram M_AB = <Theta(O_A) O_B>; dress = zero-mode phase
    e^{-i sum(u)/2} (the parafermionic omega^{k q} Klein phases)."""
    C = COVS[N]
    n = len(els)
    M = np.zeros((n, n), dtype=complex)
    for i, A in enumerate(els):
        ba = bra_ops(A, b, N, klein)
        for j, B in enumerate(els):
            ops = ba + ket_ops(B, b, N)
            if not ops:
                M[i, j] = 1.0
                continue
            sites = np.concatenate([s for s, _ in ops])
            u = np.concatenate([a * np.ones(len(s)) for s, a in ops])
            val = string_det(C, sites, u)
            M[i, j] = np.exp(-0.5j * u.sum()) * val if dress else val
    return M


def herm_dev(M):
    return np.abs(M - M.conj().T).max() / np.abs(M).max()


def imag_dev(M):
    return np.abs(M.imag).max() / np.abs(M).max()


def eig_ratio(M):
    """(eigenvalues, lambda_min / max|lambda|).  The floor ratio uses
    max|lambda| (NOT lambda_max) so that negative-definite matrices
    report -1, not a spurious positive min/max quotient."""
    ev = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
    return ev, ev.min() / np.abs(ev).max()


# ================================================================== K0
print("=" * 72)
print("K0: machinery and the structural bookkeeping")
print("=" * 72)

# K0.1 the dressed-string reality identity (exact PH identity
# <e^{iuN_S}> = e^{iu|S|} <e^{-iuN_S}> at half filling)
C96 = COVS[96]
dev_re = 0.0
for _ in range(40):
    cuts = np.sort(RNG.choice(np.arange(0, 96, 2), size=6, replace=False))
    ops = []
    for (a1, a2) in ((cuts[0], cuts[1]), (cuts[2], cuts[3]),
                     (cuts[4], cuts[5])):
        if a2 > a1:
            ops.append((np.arange(a1, a2),
                        RNG.choice([LAM, 2 * LAM, np.pi])))
    sites = np.concatenate([s for s, _ in ops])
    u = np.concatenate([a * np.ones(len(s)) for s, a in ops])
    w = np.exp(-0.5j * u.sum()) * string_det(C96, sites, u)
    dev_re = max(dev_re, abs(w.imag) / max(1.0, abs(w)))
check("K0.1 the zero-mode-dressed string e^{-i sum(u)/2} <prod e^{i u n}> "
      "is EXACTLY real for random multi-arc mixed-angle configurations "
      "(the particle-hole identity I - C = DCD at half filling): reality "
      "IS the lattice fingerprint of the charge-conjugating Klein pairing",
      dev_re < TOL_MACH, "max |Im|/|w| = %.3e (40 configs)" % dev_re)

# K0.2 Z2 degeneracy of the pairings: e^{-i pi N} = e^{+i pi N}
els_z2 = [("sig", "z2", x) for x in xgrid(96)]
Mz2_naive = gram(96, 0, els_z2, klein=False, dress=False)
Mz2_klein = gram(96, 0, els_z2, klein=True, dress=False)
dev_z2 = np.abs(Mz2_naive - Mz2_klein).max()
ev_z2, r_z2 = eig_ratio(gram(96, 0, els_z2, klein=True, dress=True))
check("K0.2 for lam = pi the naive and Klein pairings COINCIDE "
      "identically (e^{-i pi N} = e^{+i pi N}): the predecessor's Z2 "
      "control validated the machinery but could not distinguish the "
      "pairings; the dressed Z2 Gram is PSD",
      dev_z2 < 1e-14 and r_z2 >= -TOL_RP,
      "max |naive - klein| = %.3e, Z2 min/max = %.3e" % (dev_z2, r_z2))

# K0.3 axis-defect bookkeeping (angle arithmetic of the glued profiles)
naive_jump = (LAM - (-LAM)) % (2 * np.pi)     # bra -lam -> ket +lam
klein_jump = (LAM - LAM) % (2 * np.pi)        # bra +lam -> ket +lam
z2_jump = (np.pi - (-np.pi)) % (2 * np.pi)    # Z2: 2 pi = 0
check("K0.3 axis-defect bookkeeping: the naive glue jumps by 2 lam = "
      "4 pi/3 != 0 mod 2 pi at the axis bond (spurious charge-2k twist "
      "pinned ON the mirror -- it pairs sigma_k with sigma_k), the "
      "Klein glue is defect-free (sigma_k with sigma_{3-k}), and for Z2 "
      "the naive jump 2 pi is invisible",
      abs(naive_jump - 4 * np.pi / 3) < 1e-12 and klein_jump < 1e-12
      and z2_jump < 1e-12,
      "naive jump = %.6f, klein jump = %.6f" % (naive_jump, klein_jump))


# ================================================================== K1
print("=" * 72)
print("K1: Klein PSD of the charged blocks (both axes, N = 48..384)")
print("=" * 72)

GK = {}          # (N, axis_label, k) -> dressed Klein block
K1_ROWS = []
k1_real, k1_psd = True, True
for Nv in N_LIST:
    axes = (("through-mark", 0), ("between-mark", Nv // 8))
    for lbl, b in axes:
        for k in (1, 2):
            els = [("sig", k, x) for x in xgrid(Nv)]
            M = gram(Nv, b, els, klein=True, dress=True)
            GK[(Nv, lbl, k)] = M
            ev, r = eig_ratio(M)
            k1_real &= (imag_dev(M) < TOL_MACH and herm_dev(M) < TOL_MACH)
            k1_psd &= (r >= -TOL_RP)
            K1_ROWS.append((Nv, lbl, k, ev, r))
            print("  N=%4d %-13s k=%d  min=%.6e  max=%.6e  min/max=%.3e"
                  % (Nv, lbl, k, ev.min(), ev.max(), r))

print("  eigenvalues (N=96, through-mark, k=1):")
print("  %s" % np.array2string(
    [row for row in K1_ROWS if row[:3] == (96, "through-mark", 1)][0][3],
    precision=4, max_line_width=70))

check("K1.1 every Klein block G^(k)_ij = <sigma_{3-k}(theta x_i) "
      "sigma_k(x_j)> is EXACTLY real symmetric (machine precision) -- "
      "the omega^{k q} zero-mode dressing removes every phase",
      k1_real, "max Im/herm dev over %d blocks" % len(K1_ROWS))
check("K1.2 every Klein block is PSD at the -1e-10 relative floor "
      "(k = 1, 2; both axes; N = 48/96/192/384): the charge-conjugated "
      "sigma-dagger pairing carries the positivity the naive pairing "
      "lost", k1_psd,
      "worst min/max = %.3e" % min(r for *_, r in K1_ROWS))

dev_sector = max(np.abs(GK[(Nv, lbl, 1)] - GK[(Nv, lbl, 2)]).max()
                 / np.abs(GK[(Nv, lbl, 1)]).max()
                 for Nv in N_LIST for lbl in ("through-mark", "between-mark"))
check("K1.3 the two charge blocks coincide exactly, G^(1) = G^(2) "
      "(charge conjugation of the seam double)", dev_sector < TOL_EQ,
      "max rel dev = %.3e" % dev_sector)

dev_axis = max(np.abs(GK[(Nv, "through-mark", k)]
                      - GK[(Nv, "between-mark", k)]).max()
               / np.abs(GK[(Nv, "through-mark", k)]).max()
               for Nv in N_LIST for k in (1, 2))
check("K1.4 through-mark and between-mark diameter axes give the SAME "
      "Gram (translation invariance of the free seam double: the mark "
      "distinction lives in the covering bookkeeping, not in the "
      "chain) -- both axes tested, both PSD", dev_axis < TOL_EQ,
      "max rel dev = %.3e" % dev_axis)


# ================================================================== K2
print("=" * 72)
print("K2: the phase scan (uniqueness of the Klein phase)")
print("=" * 72)

G1, G2 = GK[(96, "through-mark", 1)], GK[(96, "through-mark", 2)]
winners, cons_rows = [], []
for i1, e1 in enumerate(ROOTS6):
    for i2, e2 in enumerate(ROOTS6):
        cons = abs(e1 * np.conj(e2) - 1.0) < 1e-9
        h = max(herm_dev(e1 * G1), herm_dev(e2 * G2))
        herm = h < TOL_MACH
        psd = False
        if herm:
            r = min(eig_ratio(e1 * G1)[1], eig_ratio(e2 * G2)[1])
            psd = r >= -TOL_RP
        if cons:
            cons_rows.append((ROOT_LBL[i1], ROOT_LBL[i2], herm, psd))
        if cons and herm and psd:
            winners.append((ROOT_LBL[i1], ROOT_LBL[i2]))
print("  consistent pairs (eta_1 eta_2* = 1):")
for lbl1, lbl2, herm, psd in cons_rows:
    print("    (%s, %s): hermitian=%s psd=%s" % (lbl1, lbl2, herm, psd))
check("K2.1 UNIQUENESS: over the 36 pairs (eta_1, eta_2) in "
      "{+-1, +-w, +-w^2}^2, exactly ONE satisfies {consistency "
      "eta_k eta_{3-k}* = 1, Hermiticity, PSD}: eta = (+1, +1) on top "
      "of the omega^{k q} zero-mode dressing -- the Klein phase is "
      "unique in the scanned family", winners == [("+1", "+1")],
      "winners = %s" % winners)

els_n96 = [("sig", 1, x) for x in xgrid(96)]
Mn96 = gram(96, 0, els_n96, klein=False, dress=False)
rescue = []
for i1, e1 in enumerate(ROOTS6):
    if herm_dev(e1 * Mn96) < TOL_MACH:
        if eig_ratio(e1 * Mn96)[1] >= -TOL_RP:
            rescue.append(ROOT_LBL[i1])
check("K2.2 [must-fail] NO phase in the family rescues the NAIVE "
      "pairing (the Hermitian choices +-1 both leave it indefinite): "
      "the fix is the structural charge conjugation, not a phase",
      rescue == [], "rescuing phases = %s, naive min/max = %.3e"
      % (rescue, eig_ratio(Mn96)[1]))

x6 = [6 * i for i in range(1, 8)]
M6_bare = gram(96, 0, [("sig", 1, x) for x in x6], klein=True, dress=False)
ev6, r6 = eig_ratio(M6_bare)
Mg_bare = gram(96, 0, els_n96, klein=True, dress=False)
hd_bare = herm_dev(Mg_bare)
dev_dress = 0.0
for k in (1, 2):
    for xa in xgrid(96):
        for xb in xgrid(96):
            d1 = np.exp(-0.5j * LAMK[k] * (xa + xb))
            d2 = OMEGA ** (-k * ((xa // 2 + xb // 2) % 3))
            dev_dress = max(dev_dress, abs(d1 - d2))
check("K2.3 the omega^{k q} structure: on the 6Z sub-grid the BARE "
      "sigma-dagger pairing is already PSD (the dressing is trivial "
      "there, herm dev %.1e); on the general even grid the bare "
      "pairing is NOT Hermitian (dev %.3f) and the zero-mode dressing "
      "e^{-i lam_k (x_a+x_b)/2} = omega^{-k (x_a/2 + x_b/2 mod 3)} "
      "(parafermionic sector-charge phases) is exactly what restores "
      "reality (identity dev %.1e)"
      % (herm_dev(M6_bare), hd_bare, dev_dress),
      herm_dev(M6_bare) < TOL_MACH and r6 >= -TOL_RP and hd_bare > 0.1
      and dev_dress < 1e-12,
      "6Z min/max = %.3e" % r6)


# ================================================================== K3
print("=" * 72)
print("K3: N-stability of the Klein positivity")
print("=" * 72)

ratios_k1 = {Nv: [r for (n, lbl, k, ev, r) in K1_ROWS if n == Nv]
             for Nv in N_LIST}
mins_k1 = {Nv: min(v) for Nv, v in ratios_k1.items()}
print("  worst min/max per N: %s"
      % {Nv: "%.3e" % v for Nv, v in mins_k1.items()})
check("K3.1 the Klein minimal eigenvalues stay above the -1e-10 "
      "relative floor at every N = 48/96/192/384 (no drift towards "
      "0^-): the positivity is N-stable, in contrast to the N-stable "
      "VIOLATION of the naive pairing", min(mins_k1.values()) >= -TOL_RP,
      "floor across N = %.3e" % min(mins_k1.values()))


# ================================================================== K4
print("=" * 72)
print("K4: must-fail controls")
print("=" * 72)

# (a) the naive pairing reproduces the predecessor violation
naive_c = {}
for Nv in (96, 192, 384):
    els = [("sig", 1, x) for x in xgrid(Nv)]
    naive_c[Nv] = eig_ratio(gram(Nv, 0, els, klein=False, dress=False))[1]
naive_n = {}
for Nv in (96, 192):
    els = [("dip", 1, a1, a2) for a1, a2 in dip_pairs(Nv)]
    naive_n[Nv] = eig_ratio(gram(Nv, 0, els, klein=False, dress=False))[1]
rc = np.array(sorted(naive_c.values()))
stable_naive = (rc.max() < -1e-3 and rc.min() > -1e-2
                and (rc.max() - rc.min()) / abs(rc.mean()) < 0.5
                and abs(naive_c[96] - (-4.5e-3)) < 2e-3
                and min(naive_n.values()) < -1.5e-2)
check("K4.1 [must-fail control] the NAIVE pairing still violates, "
      "reproducing the predecessor: charged axis strings in the "
      "-4.5e-3 range at N = 96/192/384 (N-stable), neutral pairs "
      "~ -2.5e-2", stable_naive,
      "charged min/max: %s; neutral min/max: %s"
      % ({k: "%.3e" % v for k, v in naive_c.items()},
         {k: "%.3e" % v for k, v in naive_n.items()}))

# (b) deliberately wrong phases
r_neg = eig_ratio(-1.0 * G1)[1]
hd_om = herm_dev(OMEGA * G1)
check("K4.2 [must-fail control] the deliberately wrong phases fail: "
      "eta = -1 makes the block negative definite (floor ratio = "
      "%.3e, PSD lost), eta = omega breaks Hermiticity (dev = %.3f)"
      % (r_neg, hd_om), r_neg < -0.5 and hd_om > 0.1)


# ================================================================== K5
print("=" * 72)
print("K5: the mixed sector -- the lattice OS statement")
print("=" * 72)

k5_rows = []
k5_real, k5_psd = True, True
for Nv in (48, 96):
    els = ([("id",)]
           + [("sig", 1, x) for x in xgrid(Nv)]
           + [("sig", 2, x) for x in xgrid(Nv)]
           + [("dip", 1, a1, a2) for a1, a2 in dip_pairs(Nv)]
           + [("dip", 2, a1, a2) for a1, a2 in dip_pairs(Nv)])
    M = gram(Nv, 0, els, klein=True, dress=True)
    ev, r = eig_ratio(M)
    k5_real &= (imag_dev(M) < TOL_MACH and herm_dev(M) < TOL_MACH)
    k5_psd &= (r >= -TOL_RP)
    k5_rows.append((Nv, len(els), ev, r))
    print("  N=%3d full basis (dim %d: 1 + 2x11 sigma + 2x15 dipoles):"
          % (Nv, len(els)))
    print("    min=%.6e max=%.6e min/max=%.3e" % (ev.min(), ev.max(), r))
    print("    lowest eigenvalues: %s"
          % np.array2string(ev[:6], precision=4))

els_192 = ([("id",)] + [("sig", 1, x) for x in xgrid(192)]
           + [("sig", 2, x) for x in xgrid(192)])
M192 = gram(192, 0, els_192, klein=True, dress=True)
ev192, r192 = eig_ratio(M192)
k5_real &= (imag_dev(M192) < TOL_MACH and herm_dev(M192) < TOL_MACH)
print("  N=192 {1, sigma_1, sigma_2} (dim %d): min=%.6e max=%.6e "
      "min/max=%.3e" % (len(els_192), ev192.min(), ev192.max(), r192))

els_z2m = ([("id",)] + [("sig", "z2", x) for x in xgrid(96)]
           + [("dip", "z2", a1, a2) for a1, a2 in dip_pairs(96)])
Mz2m = gram(96, 0, els_z2m, klein=True, dress=True)
evz2m, rz2m = eig_ratio(Mz2m)

check("K5.1 Z2 mixed control: the full {1, disorder, dipole} Gram "
      "(dim %d) is PSD" % len(els_z2m), rz2m >= -TOL_RP,
      "min/max = %.3e" % rz2m)
check("K5.2 the FULL mixed Z3 Gram over {1, sigma_1(x), sigma_2(x), "
      "dipoles} with NO sector projection (all cross blocks kept as "
      "lattice numbers) is exactly real symmetric AND PSD at N = 48 "
      "and 96 -- the lattice Osterwalder-Schrader statement of the "
      "orbifold twist sector under the Klein pairing",
      k5_real and k5_psd,
      "min/max: %s" % {n: "%.3e" % r for n, d, e, r in k5_rows})
check("K5.3 the mixed {1, sigma_1, sigma_2} Gram stays PSD at N = 192 "
      "(stability of the mixed statement)", r192 >= -TOL_RP,
      "min/max = %.3e" % r192)


# ================================================================== K6
print("=" * 72)
print("K6: the typing")
print("=" * 72)

check("K6.1 [C, honest typing] WHAT STANDS: reflection positivity of "
      "the Z3 twist sector on the seam-double lattice with the "
      "parafermionic Klein-twist pairing -- mirror composed with "
      "charge conjugation, sigma_k paired with sigma_{3-k} at the "
      "reflected point, omega^{k q} zero-mode phases, eta = (1, 1) "
      "unique in the scanned family -- N-stable 48..384, both diameter "
      "axes, including the mixed identity+twist+dipole Gram (lattice "
      "OS level).  STILL OPEN for the full CFT statement: the "
      "continuum OS reconstruction (operator convergence, not just "
      "Gram entries), the R / fermion-parity sectors (deck^3 = -1 spin "
      "structure), modular invariance of the full orbifold partition "
      "function, chiral factorization, and any non-abelian content -- "
      "named, not claimed.  GATE.QGEO does not move", True)


# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
k1_ok = all(ok for n, ok in CHECKS if n.startswith("K1"))
k5_ok = all(ok for n, ok in CHECKS if n.startswith("K5"))
ctrl_ok = all(ok for n, ok in CHECKS if n.startswith(("K0", "K4")))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: KLEIN-RP-POSITIVE -- the Z3 twist sector is reflection")
    print("positive on the seam-double lattice under the parafermionic")
    print("Klein-twist pairing (mirror x charge conjugation, omega^{k q}")
    print("zero-mode phases, eta = (1,1) unique), N-stable 48..384, both")
    print("axes, including the mixed identity+twist+dipole OS Gram; the")
    print("naive pairing keeps its N-stable violation (must-fail).")
elif k1_ok and ctrl_ok and not k5_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: KLEIN-RP-SECTOR-ONLY -- charged Klein blocks PSD but")
    print("the mixed OS Gram fails: the sector projection is load-bearing.")
elif not k1_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: KLEIN-RP-FAILS -- the Klein pairing does not carry")
    print("positivity on the lattice: honest negative.")
else:
    print("SOME CHECKS FAILED")
    print("VERDICT: MIXED")
