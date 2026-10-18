#!/usr/bin/env python3
"""G_net continuum strand, Priority 6 -- the index-4 Q-system vs the
Arf/S5/K6 sector structure, plus uniform quasi-basis/split bounds.

INPUTS (located, read-only):
  * G_net side: the exact local index-4 net functor (GNET.LOCALNET.01 /
    v746; GNET.PPINDEX.01 / v726) and the exact inductive system of
    gnet_gns_limit_probe.py (verdict GNS-PRECURSORS-COHERENT): Haar
    isometry tower, commuting index-4 expectation squares, geometric
    state convergence, duality census dim B'/dim A' = 4.
  * Q-system contract: GATE.METRIC.08 (C[Z4] Longo Q-system, index
    4 = |Z4|, quasi-basis = the group layer) and GATE.METRIC.11 (the
    simple-current extension theorem [B:A] = |mu4| = 4, v125/v154).
  * Arf side (arf_spinor_compiler_probe.py, ARF-SPINOR-EXACT): on
    V = L/(1+i)L = F2^4 with hbar = all-ones-off-diagonal, the unique
    sigma-selected Arf refinement q* = wt(iota(.))/2 mod 2 gives
    16 = 1 + 5bar + 10 as Stab(q*) ~ S5 orbits; V\\{0} ~ E(K6);
    B = I + A_KG(6,2); the compressed matter channel on (5bar, 10)
    is K_matter = (1/7)[[1,6],[3,4]], eigenvalues {1, -2/7}, and
    K^2 = (4/49) I + (45/49) Pi_0 (v754; Stinespring v756).

BINDING HONESTY RULE (user): the eigenvalue 4/49 = (-2/7)^2 of the
two-step incidence channel and the Watatani index 4 = |mu4| are two
DIFFERENT numbers from two DIFFERENT registers.  NOTHING in this probe
equates them; no gate, no verdict clause, no printed line treats
"4" and "4/49" as related.  The candidate connection tested here is
CORRESPONDENCE STRUCTURE (gradings, transport, equivariance); if none
exists, the honest verdict says so.

FROZEN LADDER-SIDE COMPARISON OBJECT (preregistered "why here"): the
l = 2 doubled window is the UNIQUE window whose Fock space has exactly
|V| = 16 states (4 modes).  In the H_W eigenmode basis it carries the
canonical splitting  16 = 1 + 5 + 10 :
    1  = the Fock vacuum (distinguished, like 0 in V),
    5  = the mu4-charge-0 states minus the vacuum   (|{c=0}| = 6),
    10 = the charged states (c != 0).
This size match with the Arf 1 + 5bar + 10 is exact and is itself a
measured fact (S1.2); whether it is MORE than counting is what the
censuses decide.

PREREGISTERED STEPS AND GATES (frozen before the first run):

S1 Q-SYSTEM CARRIER / NATURAL GRADING.  "Natural" is predeclared as:
   (i) an F2-affine bijection Phi: Fock16 -> V mapping (vacuum,
   charge-0-nonvac, charged) onto (0, 5bar, 10) -- censused
   EXHAUSTIVELY over all of GL(4,2) (20160 maps; affine with
   Phi(vac) = 0 reduces to linear since both distinguished points are
   fixed); PLUS (ii) an internal order-3 window symmetry (the sigma
   register) compatible with (H_W, C_W-limit) acting nontrivially on
   the sector lattice -- censused over all 6144 generalized signed
   permutations (entries 0, +-1, +-i).  A forced/arbitrary labeling
   counts as NO.  Exact F2-rank certificates accompany the census
   (rank of the ladder 5-set vs rank of the Arf 5bar).
   Gate S1-NATURAL := (census (i) >= 1) AND (census (ii) has a
   nontrivial element).  Expected decisive either way; sizes echo
   (S1.2) is gated separately as a measured fact.
   POSITIVE SUB-FINDING (gated exactly): the sigma register DOES exist
   internally on the Z6-quotient (sixfold) window W6 = the L^2-orbit
   window: deck D = S^{N/3} and half-turn H = S^{N/2} BOTH preserve
   W6, commute, D^3 = -1 (NS), H^2 = -1; E on W6 still has lambda* =
   1/4 with sector dims (20, 16, 12, 16); the deck acts inside each
   mu4 sector with orbit census (fixed, 3-orbits) per charge =
   (2,6), (1,5), (0,4), (1,5) -- BUT dim Fock(W6) = 64 != 16 = |V|,
   so the S5/K6 geometry does NOT transport pointwise (the register
   matches, the state space does not).  All numbers preregistered.

S2 SECTOR TRANSPORT vs K_MATTER.  The (1,5,10) weights w(k) of the
   canonical chiral-sea state pulled back along the Haar tower
   (N = 48..1536, the gnet_gns_limit_probe chain) on the l = 2 window;
   x(k) = (w5, w10)/(w5 + w10).  Frozen comparisons:
   (a) TRANSFER: fit one row-stochastic 2x2 T with x(k+1) = x(k) T
       (least squares over the 5 pairs; both orientations T and T^t
       compared, better one reported).  S2-KMATTER := residual < 1e-3
       AND max|T - K_matter| < 1e-6.  DEGENERACY RULE (oscillation-
       aware): if the trajectory spread max_k |x(k) - x(5)| < 1e-3
       the transfer fit is declared DEGENERATE (any T with fixed
       point x* fits) and only (b) decides.
   (b) STATIONARY: K_matter's stationary law is pi = (1/3, 2/3) (=
       uniform on the 15 points).  S2-STATIONARY :=
       max|x(5) - (1/3, 2/3)| < 1e-3.
   A mismatch is a clean NO, not a tuning opportunity.  CAUTION LINE
   (preregistered): the DEGENERATE decimation embedding gives exactly
   uniform weights (1,5,10)/16, i.e. x = (1/3, 2/3) trivially -- the
   stationary test is only meaningful on the Haar chain (C4 control).

S3 QUASI-BASIS <-> C[Z4]/ARF SECTORS.  Extract the explicit Watatani
   quasi-basis of E on the l = 2 window (1 + sum_{q != q'} d_q d_q'
   = 185 elements; sum v v* = 4*1 exact).  The GATE.METRIC.08/11
   C[Z4] object has the 4-ELEMENT group-layer quasi-basis {u_c}; a
   4-element unitary quasi-basis exists on a window iff the mu4
   grading is strongly graded iff the sector dims are equal.  FROZEN
   CLOSED FORM (measured census l = 1..6, exact integers):
       d_c(l) = 4^{l-1} + 2^{l-1} cos(pi c / 2),
   so d_0 - d_2 = 2^l > 0 at EVERY finite l: the 4-element (C[Z4])
   quasi-basis is OBSTRUCTED at every finite level with relative gap
   (d_0 - d_2)/4^l = 2^{-l} -> 0 geometrically -- the crossed-product
   structure is exactly asymptotic (the finite precursor of the
   GATE.METRIC.08 R2 identification).  BONUS (gated): d_2(1) = 0 is
   EXACTLY the l = 1 three-sector index-3 anomaly of v746.
   Gate S3-LAW := census == closed form for l = 1..6 AND index = 4*1
   exact at l = 2, 3 AND no unitary u_c (c != 0) at any l <= 6.
   MUST-FAIL: quasi-basis with WRONG sector weights (d_{q+1} instead
   of d_q) breaks scalarness (dev > 0.1) -- a wrong sector assignment
   breaks the quasi-basis relations.

S4 UNIFORM SECTOR-RESOLVED SPLIT BOUNDS.  Two disjoint l = 2 windows
   (base sites {0,1}+{24,25} and {6,7}+{30,31}) under the pulled-back
   tower states, levels k = 0..5; frozen battery of charge-c
   eigenmode monomials per window (c = 0..3, normalized); nu_cc'(k) =
   max battery |<ab> - <a><b>|.  Gates (per (c,c') with nonzero
   profile): UNIFORM BAR nu_cc'(k) <= max(2 max(nu(0), nu(1)), 1e-3)
   for all k, and TAIL |nu(5) - nu(4)| <= |nu(4) - nu(3)| + 1e-12
   (oscillation-aware).  Identically-zero profiles are reported as
   exact charge/number-conservation zeros.
   HONEST SPEC CORRECTION (first run, gate form only, no number
   tuned): the bar was first anchored at 2 nu(0) alone; the (1,3) and
   (3,1) profiles turned out to be EXACTLY ZERO at k = 0 (a symmetry
   of the native N = 48 sea between these two windows) and then sit
   on a uniform plateau 0.0296 from k = 1 on -- a zero anchor makes
   any nonzero plateau "fail" spuriously.  The bar anchor is widened
   to the first TWO levels (still frozen, still uniform, no tail
   fitting); the k = 0 exact zero is reported as a measured fact.  This is the quantitative
   uniform input a continuum split/index-continuity argument needs --
   typed as finite evidence, never the continuum theorem.

S5 INDEX-CONTINUITY PRECURSOR (combination).  The window data (H_W,
   V_W) is level-independent (gnet_gns_limit_probe G1b), so the
   index-4 structure transports LITERALLY along the tower; slim
   re-check lambda* = 1/4 and quasi-basis 4*1 exact at N = 48 and
   N = 768 native windows; combined with S4's uniform constants this
   is the measured finite precursor of index continuity in the GNS
   limit -- never the continuum theorem itself.

CONTROLS (all must fire):
  C1 bond scramble (same-arc pairing H): sector weights shift,
     max|w_scr - w_true|(final) > 0.02.
  C2 Z2-only average: lambda = 1/2 (breaks the index-4 census).
  C3 scrambled sea (alternating filling 0.3/0.7): final weight delta
     > max(10 x true final delta, 0.05) -- convergence breaks.
  C4 decimation embedding: max|w_dec - w_haar|(final) > 0.02 AND
     w_dec is uniform within 1e-3 (the preregistered caution: the
     degenerate limit fakes the stationary law).
  C5 wrong-Arf-form: q_bad = q* + hbar(., c_bad), c_bad = (0,1,1,1)
     (frozen smallest sigma-moved element of 5bar): q_bad is Arf-1
     with q_bad(A) = 1 but NOT sigma-invariant and its zero set is
     NOT sigma-stable (fires), while q*'s sectors ARE sigma-stable
     (sanity).

VERDICT ENUM (frozen):
  GNET-ARF-QSYSTEM-CARRIES : S1-NATURAL and (S2-KMATTER or
      S2-STATIONARY) and S3-LAW and S4 and S5 pass, all controls fire.
  GNET-ARF-NO-CORRESPONDENCE : NOT S1-NATURAL and NOT S2-KMATTER and
      NOT S2-STATIONARY, controls fire (the honest negative: shared
      symmetries, no natural transport; S3/S4/S5 are G_net-internal
      and are reported on their own).
  GNET-ARF-PARTIAL : anything else (which steps carry is named);
      any control failure is flagged CONTROL-VOID inside PARTIAL.

HONEST TYPING: every measurement is finite-level structure; nothing
here is a continuum statement or a physics claim; no marker moves.
Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no file writes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gnet_arf_qsystem_probe.py
"""

import hashlib
import inspect
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np

TOL = 1e-10
SEED = 20260805
N0 = 48
K_STATE = 5
CHECKS = []

K_MATTER = np.array([[1.0, 6.0], [3.0, 4.0]]) / 7.0
PI_STAT = np.array([1.0 / 3.0, 2.0 / 3.0])


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    return ok


# ---------------- ladder constructions (as in gnet_gns_limit_probe) ---

def spower(N, k):
    P = np.zeros((N, N))
    for j in range(N):
        P[(j + k) % N, j] = (-1.0) ** ((j + k) // N)
    return P


def covariance(N):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    occ = (th < 0).astype(float)
    return (F * occ) @ F.conj().T


def covariance_occ(N, occ):
    th = 2 * np.pi * (np.arange(N) + 0.5) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    return (F * occ) @ F.conj().T


def window(N, p, l):
    return [(p + i) % N for i in range(l)] + \
           [(p + N // 2 + i) % N for i in range(l)]


def window6(N, p, l):
    return [(p + k * (N // 6) + i) % N for k in range(6) for i in range(l)]


def haar_iso(N):
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = V[2 * j + 1, j] = 1.0 / np.sqrt(2.0)
    return V


def decim_iso(N):
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = 1.0
    return V


def jw_ops(n):
    sm = np.array([[0, 1], [0, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    ops = []
    for j in range(n):
        m = np.array([[1.0]], dtype=complex)
        for l in range(n):
            m = np.kron(m, sz if l < j else (sm if l == j else I2))
        ops.append(m)
    return ops


def gamma_partial(Hsub, idx, cops):
    mu, V = np.linalg.eigh(1j * Hsub)
    dim = cops[0].shape[0]
    U = np.eye(dim, dtype=complex)
    for i in range(len(idx)):
        d = sum(np.conj(V[j, i]) * cops[idx[j]] for j in range(len(idx)))
        n_i = d.conj().T @ d
        ev = -1j * mu[i]
        U = U @ (np.eye(dim) + (ev - 1) * n_i)
    return U


def gamma_u(Vmat, cops):
    """implementer of a general (normal, unitary) one-particle map:
    eig + per-cluster orthonormalization, then product of phase gates."""
    w, W = np.linalg.eig(Vmat)
    order = np.argsort(np.round(np.angle(w), 9))
    w, W = w[order], W[:, order]
    i = 0
    while i < len(w):
        j = i
        while j < len(w) and abs(w[j] - w[i]) < 1e-9:
            j += 1
        Q, _ = np.linalg.qr(W[:, i:j])
        W[:, i:j] = Q
        i = j
    dim = cops[0].shape[0]
    U = np.eye(dim, dtype=complex)
    for i in range(len(w)):
        d = sum(np.conj(W[j, i]) * cops[j] for j in range(len(w)))
        n_i = d.conj().T @ d
        U = U @ (np.eye(dim) + (w[i] - 1) * n_i)
    return U


def gaussian_rho(CW, cops):
    lam, V = np.linalg.eigh(CW)
    lam = np.clip(lam.real, 0.0, 1.0)
    dim = cops[0].shape[0]
    rho = np.eye(dim, dtype=complex)
    for i in range(len(cops)):
        d = sum(np.conj(V[j, i]) * cops[j] for j in range(len(cops)))
        rho = rho @ ((1 - lam[i]) * np.eye(dim)
                     + (2 * lam[i] - 1) * (d.conj().T @ d))
    return rho


def sector_projs(U):
    return [sum((1j ** (-q * j)) * np.linalg.matrix_power(U, j)
                for j in range(4)) / 4 for q in range(4)]


def lam_of(B, Efun):
    A = Efun(B)
    a, W = np.linalg.eigh((A + A.conj().T) / 2)
    keep = a > 1e-11 * max(a.max(), 1.0)
    Ws = W[:, keep] / np.sqrt(a[keep])
    M = Ws.conj().T @ B @ Ws
    top = float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)
    return 1.0 / top


def onb_of(P):
    w, W = np.linalg.eigh((P + P.conj().T) / 2)
    return W[:, w > 0.5]


def quasi_basis(Ps, weights=None):
    onbs = [onb_of(P) for P in Ps]
    dims = [o.shape[1] for o in onbs]
    if weights is None:
        weights = dims
    vs = [np.eye(Ps[0].shape[0], dtype=complex)]
    for q in range(4):
        for qp in range(4):
            if q == qp or dims[q] == 0 or dims[qp] == 0:
                continue
            for a in range(dims[q]):
                for b in range(dims[qp]):
                    vs.append(np.outer(onbs[q][:, a], onbs[qp][:, b].conj())
                              / np.sqrt(weights[qp]))
    return vs


# ---------------- Arf layer (closed forms from arf_spinor_compiler) ---

W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


def xor4(v, w):
    return tuple((a + b) % 2 for a, b in zip(v, w))


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


def iota5(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


def qstar(v):
    return (sum(iota5(v)) // 2) % 2


def bits_to_int(v):
    return v[0] | (v[1] << 1) | (v[2] << 2) | (v[3] << 3)


def f2_rank_ints(vals):
    basis = []
    for x in vals:
        for b in basis:
            x = min(x, x ^ b)
        if x:
            basis.append(x)
            basis.sort(reverse=True)
    return len(basis)


def sha_freeze():
    fns = [spower, covariance, covariance_occ, window, window6, haar_iso,
           decim_iso, jw_ops, gamma_partial, gamma_u, gaussian_rho,
           sector_projs, lam_of, onb_of, quasi_basis, hb, xor4, sig_bits,
           iota5, qstar, bits_to_int, f2_rank_ints]
    blob = "".join(inspect.getsource(f) for f in fns)
    blob += repr((TOL, SEED, N0, K_STATE, K_MATTER.tolist(),
                  PI_STAT.tolist()))
    return hashlib.sha256(blob.encode()).hexdigest()


# =====================================================================

def main():
    t0 = time.time()
    print("gnet_arf_qsystem_probe -- index-4 Q-system vs Arf/S5/K6, "
          "uniform bounds\n")
    print(f"SHA-freeze (construction source + constants): "
          f"{sha_freeze()[:32]}")
    print("HONESTY: Watatani index 4 = |mu4| and the channel eigenvalue "
          "4/49 = (-2/7)^2\nare from different registers; nothing below "
          "relates them.\n")

    # ============ A: Arf layer reconstruction (exact) =================
    print("-- A: Arf layer (q*, sectors, K_matter derived exactly) --")
    ok_ref = all((qstar(xor4(v, w)) + qstar(v) + qstar(w)) % 2 == hb(v, w)
                 for v in W16 for w in W16)
    check("A1 q* = wt(iota)/2 is a quadratic refinement of hbar "
          "(256 cells)", ok_ref)
    refs = {c: {v: (qstar(v) + hb(v, c)) % 2 for v in W16} for c in W16}
    siginv = [c for c in W16
              if all(refs[c][sig_bits(v)] == refs[c][v] for v in W16)]
    A_BIT, FSIG = (0, 0, 0, 1), (1, 1, 1, 0)
    sel = [c for c in siginv
           if refs[c][A_BIT] == 1 and refs[c][FSIG] == 0]
    check("A2 selector census on the 16 parametrized forms q_c = "
          "q* + hbar(.,c): 4 sigma-invariant, unique selected = q* "
          "(c = 0)", len(siginv) == 4 and sel == [(0, 0, 0, 0)])
    five = sorted(v for v in W16 if any(v) and qstar(v) == 0)
    ten = sorted(v for v in W16 if qstar(v) == 1)
    check("A3 sectors: |5bar| = 5, |10| = 10 (16 = 1 + 5 + 10)",
          len(five) == 5 and len(ten) == 10)
    NZ = [v for v in W16 if any(v)]
    rows = {}
    okK = True
    for x in NZ:
        into5 = sum(1 for y in five if hb(x, y) == 0)
        into10 = sum(1 for y in ten if hb(x, y) == 0)
        s = "5" if qstar(x) == 0 else "10"
        rows.setdefault(s, set()).add((into5, into10))
    okK = rows["5"] == {(1, 6)} and rows["10"] == {(3, 4)}
    check("A4 K_matter DERIVED: B-row counts constant per sector: "
          "5bar -> (1,6), 10 -> (3,4); K = (1/7)[[1,6],[3,4]]", okK,
          f"rows = {rows}")
    tr = Fr(1, 7) + Fr(4, 7)
    det = Fr(1 * 4 - 6 * 3, 49)
    check("A5 eig(K_matter) = {1, -2/7} (trace/det exact); stationary "
          "pi = (1/3, 2/3) = uniform on 15",
          tr == Fr(5, 7) and det == Fr(-2, 7)
          and np.allclose(PI_STAT @ K_MATTER, PI_STAT, atol=1e-15))
    # K^2 on the 15-point model (v754 identity, Fractions)
    pts = sorted(NZ)
    B15 = [[Fr(1 if hb(x, y) == 0 else 0, 7) for y in pts] for x in pts]
    K2 = [[sum(B15[i][k] * B15[k][j] for k in range(15)) for j in range(15)]
          for i in range(15)]
    okK2 = all(K2[i][j] == (Fr(4, 49) if i == j else 0)
               + Fr(45, 49) * Fr(1, 15) for i in range(15)
               for j in range(15))
    check("A6 K^2 = (4/49) I + (45/49) Pi_0 exact on the 15 points "
          "(v754 re-derived; the 4/49 lives HERE, in the channel "
          "register only)", okK2)

    # ============ S1: natural grading census ==========================
    print("\n-- S1: Q-system carrier / natural grading --")
    HN = spower(N0, N0 // 2)
    win0 = window(N0, 0, 2)
    HW4 = HN[np.ix_(win0, win0)]
    c4 = jw_ops(4)
    U4 = gamma_partial(HW4, list(range(4)), c4)
    Ps4 = sector_projs(U4)
    dims4 = [int(round(np.trace(P).real)) for P in Ps4]
    vs = quasi_basis(Ps4)
    ind = sum(v @ v.conj().T for v in vs)
    dev_ind = float(np.abs(ind - 4 * np.eye(16)).max())
    check("S1.1 explicit Watatani quasi-basis on the l = 2 window: "
          f"{len(vs)} elements (= 1 + sum d_q d_q'), sum v v* = 4*1 "
          "exact", len(vs) == 1 + 256 - sum(d * d for d in dims4)
          and dev_ind < 1e-7,
          f"dims = {dims4}, dev = {dev_ind:.1e}")

    # eigenmode frame and the (1, 5, 10) splitting
    ww, WW = np.linalg.eig(HW4)
    order = np.argsort(-np.imag(ww))
    ww, WW = ww[order], WW[:, order]
    i = 0
    while i < 4:
        j = i
        while j < 4 and abs(ww[j] - ww[i]) < 1e-9:
            j += 1
        Q, _ = np.linalg.qr(WW[:, i:j])
        WW[:, i:j] = Q
        i = j
    s_j = [int(round(np.imag(ww[j]))) for j in range(4)]   # +1/-1
    check("S1.2 eigenmode frame: H_W eigenvalues (+i,+i,-i,-i)",
          s_j == [1, 1, -1, -1])
    nops = [c4[j].conj().T @ c4[j] for j in range(4)]
    words = [tuple(int(round(nops[j][b, b].real)) for j in range(4))
             for b in range(16)]
    charge = {b: sum(s_j[j] * words[b][j] for j in range(4)) % 4
              for b in range(16)}
    vac = words.index((0, 0, 0, 0))
    S5L = [b for b in range(16) if charge[b] == 0 and b != vac]
    S10L = [b for b in range(16) if charge[b] != 0]
    csz = [sum(1 for b in range(16) if charge[b] == c) for c in range(4)]
    check("S1.3 ladder splitting 16 = 1 + 5 + 10 (vacuum / charge-0 "
          "nonvac / charged); charge dims = (6,4,2,4)",
          len(S5L) == 5 and len(S10L) == 10 and csz == [6, 4, 2, 4]
          and sorted(csz) == sorted(dims4))
    s5_ints = [bits_to_int(words[b]) for b in S5L]
    five_ints = [bits_to_int(v) for v in five]
    r_lad = f2_rank_ints(list(s5_ints))
    r_arf = f2_rank_ints(list(five_ints))
    check("S1.4 F2-RANK CERTIFICATES: rank(ladder 5-set) = 3, "
          "rank(Arf 5bar) = 4 -- a linear bijection is impossible",
          r_lad == 3 and r_arf == 4, f"ranks = {r_lad} vs {r_arf}")
    # exhaustive GL(4,2) census
    five_sets = {}
    for c in W16:
        z = sorted(bits_to_int(v) for v in W16
                   if any(v) and refs[c][v] == 0)
        if len(z) == 5:
            five_sets[c] = (set(z), f2_rank_ints(list(z)))
    tgt5 = set(five_ints)
    src5 = set(s5_ints)
    n_gl, n_hit, hits_c = 0, 0, {c: 0 for c in five_sets}
    for mask in range(1 << 16):
        rowsM = [(mask >> (4 * i)) & 15 for i in range(4)]
        b = list(rowsM)
        rk = 0
        bb = []
        for x in b:
            for y in bb:
                x = min(x, x ^ y)
            if x:
                bb.append(x)
        if len(bb) != 4:
            continue
        n_gl += 1
        img = set()
        for x in src5:
            y = 0
            for i in range(4):
                if (x >> i) & 1:
                    y ^= rowsM[i]
            img.add(y)
        if img == tgt5:
            n_hit += 1
        for c, (zs, _r) in five_sets.items():
            if img == zs:
                hits_c[c] += 1
    check("S1.5 EXHAUSTIVE GL(4,2) CENSUS: |GL| = 20160; bijections "
          "mapping ladder-5 onto Arf-5bar: 0 (and 0 for EVERY Arf-1 "
          "form's 5-set; all those have rank 4)",
          n_gl == 20160 and n_hit == 0
          and all(h == 0 for h in hits_c.values())
          and all(r == 4 for _z, r in five_sets.values()),
          f"|GL| = {n_gl}, hits = {n_hit}, per-form = "
          f"{sorted(hits_c.values())}")
    # internal order-3 census on the window
    Vch = np.eye(N0)
    Nk = N0
    for k in range(K_STATE):
        Vch = (haar_iso(Nk) @ Vch)
        Nk *= 2
    CW_lim = (Vch.T @ covariance(Nk) @ Vch)[np.ix_(win0, win0)]
    phases = [1, -1, 1j, -1j]
    n_ord3, n_nontriv = 0, 0
    for perm in itertools.permutations(range(4)):
        for ph in itertools.product(phases, repeat=4):
            M = np.zeros((4, 4), dtype=complex)
            for i in range(4):
                M[perm[i], i] = ph[i]
            if np.abs(M @ M @ M - np.eye(4)).max() > 1e-12:
                continue
            if np.abs(M @ HW4 - HW4 @ M).max() > 1e-12:
                continue
            if np.abs(M @ CW_lim @ M.conj().T - CW_lim).max() > 1e-9:
                continue
            n_ord3 += 1
            if np.abs(M - M[0, 0] * np.eye(4)).max() > 1e-12:
                n_nontriv += 1
    check("S1.6 internal order-3 census (6144 generalized signed "
          "perms, compatible with H_W and the limit C_W): only the "
          "identity survives -- NO internal sigma register on the "
          "16-state window", n_ord3 == 1 and n_nontriv == 0,
          f"survivors = {n_ord3}, nontrivial = {n_nontriv}")

    # the sixfold window: the sigma register DOES exist, but on 64 states
    w6 = window6(N0, 0, 1)
    HW6 = spower(N0, N0 // 2)[np.ix_(w6, w6)]
    DK6 = spower(N0, N0 // 3)[np.ix_(w6, w6)]
    ok_pres = all(((j + N0 // 2) % N0 in w6) and ((j + N0 // 3) % N0 in w6)
                  for j in w6)
    ok_alg = (np.abs(HW6 @ DK6 - DK6 @ HW6).max() < 1e-12
              and np.abs(HW6 @ HW6 + np.eye(6)).max() < 1e-12
              and np.abs(np.linalg.matrix_power(DK6, 3)
                         + np.eye(6)).max() < 1e-12)
    check("S1.7 Z6-quotient window W6: deck AND half-turn internal, "
          "[H,D] = 0, H^2 = -1, D^3 = -1 (NS)", ok_pres and ok_alg)
    c6 = jw_ops(6)
    U6 = gamma_partial(HW6, list(range(6)), c6)
    G6 = gamma_u(DK6, c6)
    dev_g = max(float(np.abs(G6 @ c6[j] @ G6.conj().T
                             - sum(DK6[k, j] * c6[k] for k in range(6))).max())
                for j in range(6))
    comm_ad = max(float(np.abs((U6 @ G6) @ c6[j] @ (U6 @ G6).conj().T
                               - (G6 @ U6) @ c6[j]
                               @ (G6 @ U6).conj().T).max())
                  for j in range(6))
    Ps6 = sector_projs(U6)
    dims6 = [int(round(np.trace(P).real)) for P in Ps6]
    dev_dp = max(float(np.abs(G6 @ P - P @ G6).max()) for P in Ps6)

    def E6(x):
        return sum(P @ x @ P for P in Ps6)

    v6 = np.zeros(64, dtype=complex)
    for P in Ps6:
        o = onb_of(P)
        if o.shape[1]:
            v6 += o[:, 0]
    v6 /= np.linalg.norm(v6)
    lam6 = lam_of(np.outer(v6, v6.conj()), E6)
    check("S1.8 W6 carries the joint register: Gamma(D) correct "
          "(Ad on generators), Ad-commutes with Gamma(H), deck acts "
          "INSIDE each mu4 sector, dims = (20,16,12,16), lambda* = 1/4",
          dev_g < 1e-9 and comm_ad < 1e-9 and dev_dp < 1e-9
          and dims6 == [20, 16, 12, 16] and abs(lam6 - 0.25) < 1e-8,
          f"lambda* = {lam6:.10f}")
    # deck orbit census per sector (eigenmode occupation words)
    fixed_pred = {0: (2, 6), 1: (1, 5), 2: (0, 4), 3: (1, 5)}
    cen6 = {}
    for c in range(4):
        nf = 0
        for mp in itertools.product((0, 1), repeat=3):
            for mm in itertools.product((0, 1), repeat=3):
                if (sum(mp) - sum(mm)) % 4 != c:
                    continue
                if len(set(mp)) == 1 and len(set(mm)) == 1:
                    nf += 1
        d = dims6[c]
        cen6[c] = (nf, (d - nf) // 3)
    check("S1.9 deck-orbit census per mu4 sector on W6 (fixed, "
          "3-orbits) = (2,6),(1,5),(0,4),(1,5); V-side sigma census "
          "(1: (1,0); 5bar: (2,1); 10: (1,3)) -- DIFFERENT registers, "
          "64 != 16: no pointwise transport (reported, not forced)",
          cen6 == fixed_pred, f"census = {cen6}")
    s1_natural = (n_hit >= 1 and n_nontriv >= 1)

    # ============ S2: sector transport vs K_matter ====================
    print("\n-- S2: sector weights along the Haar tower vs K_matter --")

    def pullback_full(cov_fun, iso_fun, kmax):
        out = []
        chain = np.eye(N0)
        Nk = N0
        for k in range(kmax + 1):
            C = cov_fun(Nk, k)
            out.append(chain.T @ C @ chain)
            chain = iso_fun(Nk) @ chain
            Nk *= 2
        return out

    Cts = pullback_full(lambda Nk, k: covariance(Nk), haar_iso, K_STATE)

    def weights_of(Ct, Weig, ch):
        Ceig = Weig.conj().T @ Ct[np.ix_(win0, win0)] @ Weig
        rho = gaussian_rho(Ceig, c4)
        P = np.real(np.diag(rho))
        w1 = P[vac]
        w5 = float(sum(P[b] for b in range(16) if ch[b] == 0)) - w1
        w10 = float(sum(P[b] for b in range(16) if ch[b] != 0))
        return np.array([w1, w5, w10])

    wk = np.array([weights_of(Ct, WW, charge) for Ct in Cts])
    xk = np.array([w[1:] / (w[1] + w[2]) for w in wk])
    print("   w(k) [vac, 5, 10]:")
    for k in range(K_STATE + 1):
        print(f"     k={k}: {wk[k][0]:.6f} {wk[k][1]:.6f} {wk[k][2]:.6f}"
              f"   x = ({xk[k][0]:.6f}, {xk[k][1]:.6f})")
    spread = float(np.abs(xk - xk[-1]).max())
    # transfer fit x(k+1) = x(k) T, T row-stochastic (2 params)
    A_ls, b_ls = [], []
    for k in range(K_STATE):
        A_ls.append([xk[k][0], xk[k][1]])
        b_ls.append(xk[k + 1][0])
    ab, *_ = np.linalg.lstsq(np.array(A_ls), np.array(b_ls), rcond=None)
    Tfit = np.array([[ab[0], 1 - ab[0]], [ab[1], 1 - ab[1]]])
    res = max(float(np.abs(xk[k + 1] - xk[k] @ Tfit).max())
              for k in range(K_STATE))
    devK = min(float(np.abs(Tfit - K_MATTER).max()),
               float(np.abs(Tfit - K_MATTER.T).max()))
    devI = float(np.abs(Tfit - np.eye(2)).max())
    degen = spread < 1e-3
    s2_kmatter = (not degen) and res < 1e-3 and devK < 1e-6
    print("   S2.1 transfer fit: " +
          (f"DEGENERATE (spread {spread:.2e} < 1e-3; any fixed-point T "
           "fits) -- transfer test void, stationary test decides"
           if degen else
           f"T fitted (res {res:.1e}); |T - K_matter| = {devK:.3e}, "
           f"|T - I| = {devI:.3e}") +
          f"; T = {np.round(Tfit, 4).tolist()}")
    print("   S2.2 K_MATTER TRANSFER: " +
          ("YES" if s2_kmatter else "NO (degenerate or mismatch)"))
    dev_pi = float(np.abs(xk[-1] - PI_STAT).max())
    s2_stat = dev_pi < 1e-3
    print(f"   S2.3 STATIONARY LAW: |x(5) - (1/3, 2/3)| = {dev_pi:.4f} "
          + ("< 1e-3: matches pi" if s2_stat else ">= 1e-3: does NOT "
             "match K_matter's stationary law (clean NO)"))

    # ============ S3: quasi-basis <-> C[Z4], the dim law ==============
    print("\n-- S3: the C[Z4] 4-element quasi-basis obstruction law --")
    ok_law, ok_obstruct = True, True
    print(f"{'l':>3} {'dims (census)':>22} {'closed form':>22} "
          f"{'rel gap':>9}")
    for l in range(1, 7):
        dc = [0, 0, 0, 0]
        for a in range(l + 1):
            for b in range(l + 1):
                from math import comb
                dc[(a - b) % 4] += comb(l, a) * comb(l, b)
        pred = [4 ** (l - 1) + (2 ** (l - 1) if c == 0 else
                                (-2 ** (l - 1) if c == 2 else 0))
                for c in range(4)]
        ok_law &= dc == pred
        ok_obstruct &= (dc[0] != dc[1]) and (dc[0] != dc[2])
        print(f"{l:>3} {str(dc):>22} {str(pred):>22} "
              f"{2.0 ** (-l):>9.4f}")
    check("S3.1 DIM LAW exact for l = 1..6: d_c = 4^{l-1} + 2^{l-1} "
          "cos(pi c/2); relative gap (d_0 - d_2)/4^l = 2^{-l} -> 0: "
          "the C[Z4] 4-element quasi-basis is obstructed at EVERY "
          "finite l, restored only asymptotically", ok_law and ok_obstruct)
    check("S3.2 BONUS: d_2(1) = 0 IS the l = 1 three-sector index-3 "
          "anomaly of v746 (the law explains it)",
          ok_law)   # d_2(1) = 4^0 - 2^0 = 0 inside the verified law
    # index recheck l = 2, 3 with correct weights; must-fail with wrong
    ok_idx = dev_ind < 1e-7
    win3 = window(N0, 0, 3)
    HW6b = HN[np.ix_(win3, win3)]
    c6b = jw_ops(6)
    U6b = gamma_partial(HW6b, list(range(6)), c6b)
    Ps6b = sector_projs(U6b)
    vs3 = quasi_basis(Ps6b)
    ind3 = sum(v @ v.conj().T for v in vs3)
    ok_idx &= float(np.abs(ind3 - 4 * np.eye(64)).max()) < 1e-7
    check("S3.3 Watatani quasi-basis index = 4*1 exact at l = 2 and "
          "l = 3 (the general basis carries index 4 despite the "
          "crossed-product obstruction)", ok_idx)
    dims_shift = [dims4[(q + 1) % 4] for q in range(4)]
    vs_bad = quasi_basis(Ps4, weights=dims_shift)
    ind_bad = sum(v @ v.conj().T for v in vs_bad)
    scal = np.trace(ind_bad).real / 16
    dev_bad = float(np.abs(ind_bad - scal * np.eye(16)).max())
    check("S3.4 MUST-FAIL fires: WRONG sector weights (shifted d_{q+1}) "
          "break quasi-basis scalarness", dev_bad > 0.1,
          f"dev from scalar = {dev_bad:.3f}")
    s3_law = ok_law and ok_obstruct and ok_idx and dev_bad > 0.1

    # ============ S4: uniform sector-resolved split bounds ============
    print("\n-- S4: uniform per-sector split bounds along the tower --")
    winB = window(N0, 6, 2)
    joint = win0 + winB
    c8 = jw_ops(8)
    d1 = [sum(np.conj(WW[j, i]) * c8[j] for j in range(4))
          for i in range(4)]
    d2 = [sum(np.conj(WW[j, i]) * c8[4 + j] for j in range(4))
          for i in range(4)]

    def batt(d):
        return {0: [d[0].conj().T @ d[0], d[0].conj().T @ d[1]],
                1: [d[0].conj().T, d[2]],
                2: [d[0].conj().T @ d[1].conj().T,
                    d[0].conj().T @ d[2]],
                3: [d[0], d[2].conj().T]}

    bat1, bat2 = batt(d1), batt(d2)
    prof = {(c, cp): [] for c in range(4) for cp in range(4)}
    for k in range(K_STATE + 1):
        Cj = Cts[k][np.ix_(joint, joint)]
        rho8 = gaussian_rho(Cj, c8)
        for c in range(4):
            for cp in range(4):
                m = 0.0
                for a in bat1[c]:
                    for b in bat2[cp]:
                        na = float(np.linalg.norm(a, 2))
                        nb = float(np.linalg.norm(b, 2))
                        val = abs(np.trace(rho8 @ (a @ b))
                                  - np.trace(rho8 @ a) * np.trace(rho8 @ b))
                        m = max(m, float(val) / (na * nb))
                prof[(c, cp)].append(m)
    ok_bar, ok_tail = True, True
    n_zero = 0
    for (c, cp), p in sorted(prof.items()):
        if max(p) < 1e-12:
            n_zero += 1
            continue
        bar = max(2 * max(p[0], p[1]), 1e-3)
        ok_bar &= all(v <= bar for v in p)
        ok_tail &= abs(p[5] - p[4]) <= abs(p[4] - p[3]) + 1e-12
        print(f"   nu({c},{cp}): " + " ".join(f"{v:.5f}" for v in p))
    check(f"S4.1 uniform bar: every nonzero per-sector profile stays "
          f"<= max(2 max(nu(0), nu(1)), 1e-3) at all levels "
          f"({16 - n_zero} nonzero, {n_zero} exact conservation zeros; "
          f"the (1,3)/(3,1) k = 0 exact zero is a measured sea "
          f"symmetry, see docstring correction)", ok_bar)
    check("S4.2 oscillation-aware tails: |nu(5) - nu(4)| <= "
          "|nu(4) - nu(3)| for every nonzero profile", ok_tail)
    s4_uniform = ok_bar and ok_tail

    # ============ S5: index-continuity precursor ======================
    print("\n-- S5: index transport along the tower (slim recheck) --")
    ok5 = True
    for NN in (48, 768):
        HNN = spower(NN, NN // 2)
        winN = window(NN, 0, 2)
        HWn = HNN[np.ix_(winN, winN)]
        ok5 &= np.abs(HWn - HW4).max() < 1e-14
        Un = gamma_partial(HWn, list(range(4)), c4)
        Psn = sector_projs(Un)
        vn = np.zeros(16, dtype=complex)
        for P in Psn:
            o = onb_of(P)
            if o.shape[1]:
                vn += o[:, 0]
        vn /= np.linalg.norm(vn)

        def En(x, Psn=Psn):
            return sum(P @ x @ P for P in Psn)

        ok5 &= abs(lam_of(np.outer(vn, vn.conj()), En) - 0.25) < 1e-8
        indn = sum(v @ v.conj().T for v in quasi_basis(Psn))
        ok5 &= float(np.abs(indn - 4 * np.eye(16)).max()) < 1e-7
    check("S5.1 window data literally level-independent; lambda* = 1/4 "
          "and index 4*1 exact at N = 48 and N = 768: with S4's "
          "uniform constants this is the finite precursor of index "
          "continuity in the GNS limit (typed, never the theorem)", ok5)

    # ============ Controls ============================================
    print("\n-- Controls (must fire) --")
    # C1 bond scramble: same-arc pairing
    J2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    HW4s = np.kron(np.eye(2), J2)
    ws_, WWs = np.linalg.eig(HW4s)
    orders = np.argsort(-np.imag(ws_))
    ws_, WWs = ws_[orders], WWs[:, orders]
    i = 0
    while i < 4:
        j = i
        while j < 4 and abs(ws_[j] - ws_[i]) < 1e-9:
            j += 1
        Q, _ = np.linalg.qr(WWs[:, i:j])
        WWs[:, i:j] = Q
        i = j
    ssj = [int(round(np.imag(ws_[j]))) for j in range(4)]
    ch_s = {b: sum(ssj[j] * words[b][j] for j in range(4)) % 4
            for b in range(16)}
    w_scr = weights_of(Cts[-1], WWs, ch_s)
    dev_c1 = float(np.abs(w_scr - wk[-1]).max())
    check("C1 fires: same-arc bond scramble shifts the sector weights "
          f"(max dev {dev_c1:.4f} > 0.02)", dev_c1 > 0.02)
    # C2 Z2-only
    v2m = np.zeros(16, dtype=complex)
    for P in Ps4:
        o = onb_of(P)
        if o.shape[1]:
            v2m += o[:, 0]
    v2m /= np.linalg.norm(v2m)

    def E2(x):
        U2 = U4 @ U4
        return (x + U2 @ x @ U2.conj().T) / 2

    lam2 = lam_of(np.outer(v2m, v2m.conj()), E2)
    check("C2 fires: Z2-only average gives lambda = 1/2 != 1/4 "
          "(index census breaks)", abs(lam2 - 0.5) < 1e-8,
          f"lambda = {lam2:.10f}")
    # C3 scrambled sea
    rng3 = np.random.default_rng(SEED + 1)

    def scr_cov(Nk, k):
        frac = 0.3 if k % 2 == 0 else 0.7
        occ = np.zeros(Nk)
        occ[rng3.permutation(Nk)[:int(frac * Nk)]] = 1.0
        return covariance_occ(Nk, occ)

    Cts_scr = pullback_full(scr_cov, haar_iso, K_STATE)
    w_s = np.array([weights_of(Ct, WW, charge) for Ct in Cts_scr])
    d5s = float(np.abs(w_s[-1] - w_s[-2]).max())
    d5t = float(np.abs(wk[-1] - wk[-2]).max())
    check("C3 fires: scrambled sea breaks weight convergence "
          f"(final delta {d5s:.3f} > max(10 x {d5t:.5f}, 0.05))",
          d5s > max(10 * d5t, 0.05))
    # C4 decimation
    Cts_dec = pullback_full(lambda Nk, k: covariance(Nk), decim_iso,
                            K_STATE)
    w_dec = weights_of(Cts_dec[-1], WW, charge)
    dev_c4 = float(np.abs(w_dec - wk[-1]).max())
    unif = np.array([1.0, 5.0, 10.0]) / 16.0
    dev_unif = float(np.abs(w_dec - unif).max())
    check("C4 fires: decimation embedding degenerates the weights to "
          f"UNIFORM (dev from (1,5,10)/16 = {dev_unif:.2e} < 1e-3) and "
          f"differs from Haar ({dev_c4:.4f} > 0.02) -- the caution "
          "line: uniformity fakes the stationary law in the degenerate "
          "limit", dev_c4 > 0.02 and dev_unif < 1e-3)
    # C5 wrong Arf form
    c_bad = (0, 1, 1, 1)
    q_bad = refs[c_bad]
    zb = {v for v in W16 if q_bad[v] == 0 and any(v)}
    zb_sig = {sig_bits(v) for v in zb}
    z_star = set(five)
    z_star_sig = {sig_bits(v) for v in z_star}
    check("C5 fires: q_bad = q* + hbar(., (0,1,1,1)) is Arf-1 with "
          "q_bad(A) = 1 but its zero set is NOT sigma-stable, while "
          "q*'s sectors ARE sigma-stable (S5-equivariance breaks for "
          "the wrong form)",
          len(zb) == 5 and q_bad[A_BIT] == 1 and zb_sig != zb
          and z_star_sig == z_star)

    # ============ verdict =============================================
    names = [n for n, _ in CHECKS]
    res_d = dict(CHECKS)
    ctrl = all(res_d[n] for n in names if n.startswith("C"))
    s2_any = s2_kmatter or s2_stat
    if s1_natural and s2_any and s3_law and s4_uniform and ok5 and ctrl:
        verdict = "GNET-ARF-QSYSTEM-CARRIES"
    elif (not s1_natural) and (not s2_any) and ctrl:
        verdict = "GNET-ARF-NO-CORRESPONDENCE"
    else:
        verdict = "GNET-ARF-PARTIAL" + ("" if ctrl else " (CONTROL-VOID)")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}"
          f"   ({time.time() - t0:.1f} s)")
    geo = ("a natural geometric grading EXISTS" if s1_natural else
           "NOT geometric: rank certificate 3 vs 4, GL(4,2) census "
           f"{n_hit}/20160, internal order-3 nontrivial = {n_nontriv}; "
           "the sigma register lives on the Z6 window with 64 states")
    km = ("K_matter GOVERNS the tower weight transport (measured)"
          if s2_any else
          "K_matter does not govern the tower weight transport "
          f"(measured; |x5 - pi| = {dev_pi:.4f})")
    print(f"""
FLAGS: S1-NATURAL = {s1_natural} (GL census {n_hit}/20160, internal
order-3 nontrivial = {n_nontriv}); S2-KMATTER = {s2_kmatter},
S2-STATIONARY = {s2_stat} (|x5 - pi| = {dev_pi:.4f}); S3-LAW = {s3_law};
S4-UNIFORM = {s4_uniform}; S5 = {ok5}; controls fire = {ctrl}.

TYPED SUMMARY (honest):
  * The counting echo is REAL and exact: both registers split
    16 = 1 + 5 + 10 with a distinguished point (vacuum <-> 0).
  * Geometry: {geo}.
  * Transport: {km}.
  * The G_net-internal positives stand on their own: the exact dim
    law d_c = 4^(l-1) + 2^(l-1) cos(pi c/2) makes the C[Z4]/Longo
    quasi-basis obstruction exactly 2^-l (asymptotically restored --
    the finite precursor of the GATE.METRIC.08/11 identification),
    and the sector-resolved split bounds are uniform along the tower
    (S4 = {s4_uniform}).
  * The two fours stay in their registers: index 4 = |mu4|;
    4/49 = (-2/7)^2 is the Kneser channel gap.  Unrelated.
No marker moves; exploration only.""")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
