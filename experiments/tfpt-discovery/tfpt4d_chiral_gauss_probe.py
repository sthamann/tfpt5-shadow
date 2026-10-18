#!/usr/bin/env python3
"""tfpt4d_chiral_gauss_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (CHIRAL4D.NOMIRROR.01 [O] + TFPT4D.LATTICE.ACTION.01 [O],
the chiral matter test of today's Hamiltonian route):
tfpt4d_hamiltonian_route_probe cleared T2 with VECTORLIKE staggered
content and an exact interior Z4 Gauss law.  This probe asks whether
that Gauss law is an ANOMALY FILTER -- the 1+1D mechanism that a
local Gauss unitary exists iff the fermion content is anomaly-free --
on a two-species Z4 (= mu4) Hamiltonian of the same class:

    4-site ring, two 1-component species with charges (q_L, q_R) in Z4,
    covariant hopping uses Z^{q} (charge q means psi -> i^{q g} psi and
    the hop is psi^dag Z^{q} psi_{x+1} + h.c.),
    links 0,1 dynamical (flux basis |k>, X = flux shift, Z = diag(i^k),
    X Z X^dag = i^{-1} Z), links 2,3 background (Hilbert dim
    4^2 * 2^8 = 4096, checks run factorized on 16 x 256 so the 4096
    Kronecker is never materialised),
    interior Gauss at site 1:
        V = X_right^{s} (X_left)^{-s} * i^{g_L n_L + g_R n_R},
    s in {1,3} the two Z4 orientations, (g_L, g_R) in Z4 x Z4.

  T1  VECTORLIKE CONTROL: q_L = q_R = 1.  H is hermitian by
      construction; the covariant Gauss (g,s) = ((1,1), 1) commutes
      with every term of H to machine precision -- today's T1
      re-anchored with two species.
  T2  THE ANOMALY GATE (single-exponent scan): a naive Z4 Gauss
      generator uses ONE group element, Phi = i^{g (n_L + n_R)} with
      g in Z4.  Exhaustive scan of (g, s).  VECTORLIKE content admits
      a hit; every CHIRAL pair q_L != q_R fails every candidate.
      The 4 x 4 census of (q_L, q_R) equals the closed form
      q_L ≡ q_R (mod 4) -- machine-derived discrete condition.
  T3  COVARIANT CENSUS (independent exponents): the representation-
      theoretically correct Gauss, Phi = i^{g_L n_L + g_R n_R},
      scanned over Z4 x Z4 x {1,3}.  EVERY (q_L, q_R) admits a hit,
      namely (g, s) = ((q_L, q_R), 1) and ((-q_L, -q_R), 3).  Closed
      form g_s ≡ s q_s (mod 4).  This is Nielsen-Ninomiya as a Gauss
      statement: each 1-component two-way hop is lattice-Dirac, so
      the continuum Weyl anomaly is cancelled by the doubler and does
      NOT obstruct a local Gauss law.
  T4  GROUP LAW of every successful V: V^4 = I and the two
      orientations generate inverse Z4 elements (s = 3 is s = 1
      inverted).  Option (b) of the contract does not fire -- when a
      Gauss unitary exists it is an honest Z4 representation.
  T5  ANOMALY-FREE CHIRAL SEED: (q_L, q_R) = (1, 3) is genuinely
      chiral (1 != 3) and continuum-anomaly-free for Z4
      (1^2 - 3^2 = -8 ≡ 0 mod 8).  Independent-exponent Gauss PASSES
      (T3); single-exponent Gauss FAILS (T2).  It is the executable
      NOMIRROR seed of the covariant construction, and it is
      INVISIBLE to the naive one-exponent filter.  The same covariant
      UV also admits the continuum-anomalous pair (1, 0) -- the
      Hamiltonian route at this size is not yet an anomaly polynomial
      filter (that is the T3 finding).

HONEST BOUNDARY (dimension-uplift firewall): 1+1D toy, 4-site ring,
structure group Z4, two 1-component species -- NOT the TFPT
representation content, not 3+1D, no Ginsparg-Wilson / overlap chiral
measure.  Nothing closes CHIRAL4D.NOMIRROR.01 or
TFPT4D.LATTICE.ACTION.01.  The deliverable is the two-scan census:
the Gauss obstruction of a SINGLE Z4 exponent is q_L ≡ q_R; the
covariant two-exponent Gauss exists for every charge pair because
each lattice species is Dirac.

VERDICT ENUM: CHIRAL_GAUSS_CENSUS_COMPLETE (contracts stay [O]).
"""
import numpy as np

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


NS = 4
NLQ = 2                          # links 0,1 quantum; 2,3 background
NFERM = 2 * NS                   # L,R at each site
DF = 2 ** NFERM                  # 256
DL = 4 ** NLQ                    # 16
W_HOP, MASS, LAM_E = 0.7, 0.5, 1.0

Z1 = np.diag([1j ** k for k in range(4)]).astype(complex)
X1 = np.roll(np.eye(4), 1, axis=0).astype(complex)
assert np.max(np.abs(X1 @ Z1 @ X1.conj().T - (1j ** (-1)) * Z1)) < 1e-14

sz = np.diag([1.0, -1.0])
ann = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)


def ferm_op(alpha):
    """Jordan-Wigner annihilator on mode alpha in 0..7.
    Mode layout: (L0, R0, L1, R1, L2, R2, L3, R3)."""
    out = np.array([[1.0]], dtype=complex)
    for j in range(NFERM):
        if j < alpha:
            out = np.kron(out, sz)
        elif j == alpha:
            out = np.kron(out, ann)
        else:
            out = np.kron(out, np.eye(2))
    return out


PSI = [[ferm_op(2 * x + s) for s in range(2)] for x in range(NS)]
NUM = [[PSI[x][s].conj().T @ PSI[x][s] for s in range(2)] for x in range(NS)]
HOP = [[PSI[x][s].conj().T @ PSI[(x + 1) % NS][s]
        for s in range(2)] for x in range(NS)]


def link_mat(l, M):
    out = np.array([[1.0]], dtype=complex)
    for j in range(NLQ):
        out = np.kron(out, M if j == l else np.eye(4))
    return out


def maxabs(A):
    return float(np.max(np.abs(A)))


def kron_conj_dev(A, B, C, D):
    """||kron(C,D) kron(A,B) kron(C,D)^dag - kron(A,B)|| via the
    identity kron(A2, B2) = kron(A, B) iff A2 = ω A and B2 = ω^{-1} B
    (A, B are the Weyl / occupation factors here, so this is exact)."""
    A2 = C @ A @ C.conj().T
    B2 = D @ B @ D.conj().T
    nA = complex(np.vdot(A.ravel(), A.ravel()))
    nB = complex(np.vdot(B.ravel(), B.ravel()))
    if abs(nA) < 1e-20 and abs(nB) < 1e-20:
        return maxabs(A2) + maxabs(B2)
    if abs(nA) >= 1e-20:
        omega = complex(np.vdot(A.ravel(), A2.ravel()) / nA)
        dA = maxabs(A2 - omega * A)
        if abs(omega) < 1e-14:
            return 1.0 if maxabs(A) > 1e-14 else maxabs(A2)
        dB = maxabs(B2 - (1.0 / omega) * B)
        return max(dA, dB)
    omega = complex(np.vdot(B.ravel(), B2.ravel()) / nB)
    dB = maxabs(B2 - omega * B)
    if abs(omega) < 1e-14:
        return 1.0 if maxabs(B) > 1e-14 else maxabs(B2)
    dA = maxabs(A2 - (1.0 / omega) * A)
    return max(dA, dB)


def i_n_phase(n_op, g):
    """i^{g n} for n a 0-1 projector: I + (i^g - 1) n."""
    return np.eye(n_op.shape[0], dtype=complex) + ((1j ** g) - 1.0) * n_op


def gauss_factors(gL, gR, s, site=1):
    """V = kron(Vlink, Phi) at the interior site (left=link 0, right=link 1)."""
    s = int(s) % 4
    Vlink = (np.linalg.matrix_power(link_mat(1, X1), s)
             @ np.linalg.matrix_power(link_mat(0, X1), (4 - s) % 4))
    Phi = (i_n_phase(NUM[site][0], gL) @ i_n_phase(NUM[site][1], gR))
    return Vlink, Phi


def term_comm(qL, qR, gL, gR, s):
    """max commutator bound of V with every term of H(qL, qR)."""
    qs = (int(qL) % 4, int(qR) % 4)
    Vlink, Phi = gauss_factors(gL, gR, s)
    I_L, I_F = np.eye(DL), np.eye(DF)
    mx = 0.0
    for l in range(NLQ):
        Xl = link_mat(l, X1)
        mx = max(mx, kron_conj_dev(Xl, I_F, Vlink, Phi))
        mx = max(mx, kron_conj_dev(Xl.conj().T, I_F, Vlink, Phi))
    for x in range(NLQ):
        Zx = link_mat(x, Z1)
        for sp in range(2):
            Zq = np.linalg.matrix_power(Zx, qs[sp])
            hop = HOP[x][sp]
            mx = max(mx, kron_conj_dev(Zq, hop, Vlink, Phi))
            mx = max(mx, kron_conj_dev(Zq.conj().T, hop.conj().T, Vlink, Phi))
    for x in range(NLQ, NS):
        for sp in range(2):
            hop = HOP[x][sp]
            mx = max(mx, kron_conj_dev(I_L, hop, Vlink, Phi))
            mx = max(mx, kron_conj_dev(I_L, hop.conj().T, Vlink, Phi))
    for x in range(NS):
        for sp in range(2):
            mx = max(mx, kron_conj_dev(I_L, NUM[x][sp], Vlink, Phi))
    return mx


def hits_independent(qL, qR, tol=1e-10):
    out = []
    for gL in range(4):
        for gR in range(4):
            for s in (1, 3):
                c = term_comm(qL, qR, gL, gR, s)
                if c < tol:
                    out.append((gL, gR, s, c))
    return out


def hits_single_g(qL, qR, tol=1e-10):
    """naive one-exponent Gauss: g_L = g_R = g."""
    out = []
    for g in range(4):
        for s in (1, 3):
            c = term_comm(qL, qR, g, g, s)
            if c < tol:
                out.append((g, s, c))
    return out


# background-field H on the fermion factor (dim 256) -- exact matrices
def H_background(qL, qR, nlinks, w=W_HOP, m=MASS):
    H = np.zeros((DF, DF), dtype=complex)
    qs = (int(qL) % 4, int(qR) % 4)
    for x in range(NS):
        U = 1j ** int(nlinks[x])
        for sp in range(2):
            hop = (U ** qs[sp]) * HOP[x][sp]
            H += w * (hop + hop.conj().T)
        for sp in range(2):
            H += m * ((-1) ** x) * NUM[x][sp]
    return H


def gauge_tf_links(nlinks, x, g=1):
    """Many-body conjugation by i^{q n_x} multiplies psi^dag_x by i^q, so
    the right link must pick up i^{q} (n_right += g) to keep the hop
    covariant; the left link is the inverse (matches X_right X_left^{-1}
    on the dynamical side, where X Z X^dag = i^{-1} Z cancels Phi)."""
    n = list(nlinks)
    n[x] = (n[x] + g) % 4
    n[(x - 1) % NS] = (n[(x - 1) % NS] - g) % 4
    return tuple(n)


def Phi_site(x, gL, gR):
    return i_n_phase(NUM[x][0], gL) @ i_n_phase(NUM[x][1], gR)


# ================================================================= T1
print("=== T1: vectorlike control q_L = q_R = 1 ===")
Hbg = H_background(1, 1, (0, 0, 0, 0))
herm = maxabs(Hbg - Hbg.conj().T)
print("   background H hermitian dev", "%.1e" % herm)
rep("T1 hermiticity [exact]: H = H^dag on the fermion factor "
    "(dev %.1e); electric X+X^dag and Z^q hops + h.c. are hermitian "
    "termwise on the dynamical factors" % herm, herm < 1e-14)

# covariance of H_bg under the covariant Gauss at every site
cov_devs = []
for x in range(NS):
    n0 = (0, 1, 2, 3)
    Phi = Phi_site(x, 1, 1)
    Hg = H_background(1, 1, gauge_tf_links(n0, x, 1))
    Ht = Phi @ H_background(1, 1, n0) @ Phi.conj().T
    cov_devs.append(maxabs(Ht - Hg))
print("   background covariance per site:", ["%.1e" % d for d in cov_devs])
rep("T1 background covariance [exact]: V_ferm H(U) V_ferm^dag = H(U^g) "
    "at every site (max dev %.1e)" % max(cov_devs), max(cov_devs) < 1e-12)

c11 = term_comm(1, 1, 1, 1, 1)
print("   dynamical interior Gauss bound ((gL,gR),s)=((1,1),1):",
      "%.1e" % c11)
rep("T1 dynamical Gauss [exact]: interior V = X_right (X_left)^{-1} "
    "i^{n_L + n_R} commutes with every term of H (bound %.1e) -- "
    "today's T1 re-anchored with two charge-1 species" % c11,
    c11 < 1e-12)

# mutant: wrong exponent fails
c_mut = term_comm(1, 1, 1, 0, 1)
rep("T1 MUTANT FIRES: (g_L, g_R) = (1, 0) on vectorlike content does "
    "NOT commute (bound %.1e) -- the gate has teeth" % c_mut,
    c_mut > 0.1)

# ================================================================= T2
print("=== T2: single-exponent Gauss census (naive Z4 generator) ===")
print("   (q_L, q_R) | n_hits | hits (g, s) | q_L==q_R | "
      "q_L^2-q_R^2 mod 8")
t2_admit = {}
for qL in range(4):
    for qR in range(4):
        h = hits_single_g(qL, qR)
        t2_admit[(qL, qR)] = len(h) > 0
        print("   (%d,%d)       %d      %s           %s        %d"
              % (qL, qR, len(h),
                 [(g, s) for g, s, _ in h],
                 str(qL == qR),
                 (qL * qL - qR * qR) % 8))

t2_closed = {(qL, qR): (qL == qR) for qL in range(4) for qR in range(4)}
n_t2 = sum(1 for v in t2_admit.values() if v)
rep("T2 census [exact]: single-exponent Gauss admits a commuting V "
    "on exactly the %d vectorlike pairs q_L = q_R, and on 0/12 chiral "
    "pairs -- every candidate (g, s) fails when q_L != q_R"
    % n_t2,
    t2_admit == t2_closed and n_t2 == 4)

rep("T2 vectorlike control in the census: (1,1) admits "
    "(g,s) = %s" % [(g, s) for g, s, _ in hits_single_g(1, 1)],
    t2_admit[(1, 1)] and (1, 1) in [(g, s) for g, s, _ in
                                    hits_single_g(1, 1)])

rep("T2 anomaly gate: (1, 3) and (1, 0) (chiral) admit ZERO "
    "single-exponent Gauss unitaries",
    (not t2_admit[(1, 3)]) and (not t2_admit[(1, 0)]))

rep("T2 closed form [derived]: admit iff q_L ≡ q_R (mod 4) -- the "
    "discrete condition machine-read from the Gauss obstruction of a "
    "single Z4 exponent; this is STRICTER than the continuum 1+1D "
    "Z4 polynomial (q_L^2 - q_R^2) ≡ 0 (mod 8), which would also "
    "pass (1,3) and (3,1)",
    t2_admit == t2_closed)

# ================================================================= T3
print("=== T3: independent-exponent Gauss census (covariant Z4 x Z4) ===")
print("   (q_L, q_R) | n_hits | representative hits | "
      "q_L^2-q_R^2 mod 8")
t3_admit = {}
t3_hits = {}
for qL in range(4):
    for qR in range(4):
        h = hits_independent(qL, qR)
        t3_admit[(qL, qR)] = len(h) > 0
        t3_hits[(qL, qR)] = h
        print("   (%d,%d)       %d      %s     %d"
              % (qL, qR, len(h),
                 [(gL, gR, s) for gL, gR, s, _ in h],
                 (qL * qL - qR * qR) % 8))

t3_closed = True
for qL in range(4):
    for qR in range(4):
        expected = {((qL, qR, 1)),
                    (((-qL) % 4, (-qR) % 4, 3))}
        got = {(gL, gR, s) for gL, gR, s, _ in t3_hits[(qL, qR)]}
        if got != expected:
            t3_closed = False
            print("   MISMATCH at (%d,%d): got %s expected %s"
                  % (qL, qR, got, expected))

rep("T3 census [exact]: EVERY (q_L, q_R) in Z4 x Z4 admits a "
    "covariant Gauss law (%d/16) -- Nielsen-Ninomiya: each "
    "1-component two-way hop is lattice-Dirac, the Weyl anomaly is "
    "doubler-cancelled and does not obstruct Gauss"
    % sum(1 for v in t3_admit.values() if v),
    all(t3_admit.values()) and t3_closed)

rep("T3 closed form [derived]: hits are exactly (g, s) = "
    "((q_L, q_R), 1) and ((-q_L, -q_R), 3), i.e. g_s ≡ s q_s "
    "(mod 4) -- X vs X^{-1} with inverted charges",
    t3_closed)

# ================================================================= T4
print("=== T4: group law of successful Gauss unitaries ===")
glaw_ok = True
glaw_devs = []
for qL, qR in ((1, 1), (1, 3), (0, 0), (2, 2), (1, 0)):
    for gL, gR, s, _ in t3_hits[(qL, qR)]:
        Vlink, Phi = gauss_factors(gL, gR, s)
        dL = maxabs(np.linalg.matrix_power(Vlink, 4) - np.eye(DL))
        dF = maxabs(np.linalg.matrix_power(Phi, 4) - np.eye(DF))
        # s=1 and s=3 are inverses on the link factor when g flips sign
        glaw_devs.append(max(dL, dF))
        if max(dL, dF) >= 1e-12:
            glaw_ok = False
print("   max(Vlink^4 - I, Phi^4 - I) over successful V:",
      "%.1e" % max(glaw_devs))
rep("T4 group law [exact]: every successful V satisfies V^4 = I on "
    "both factors (max dev %.1e) -- when a Gauss unitary exists it "
    "is an honest Z4 representation; option (b) does not fire"
    % max(glaw_devs),
    glaw_ok and max(glaw_devs) < 1e-12)

# inverse-orientation identity: V(q, s=1) and V(-q, s=3) 
V1, _ = gauss_factors(1, 1, 1)
V3, _ = gauss_factors(3, 3, 3)
inv_dev = maxabs(V1 @ V3 - np.eye(DL))
rep("T4 orientation [exact]: s = 3 with inverted charges is the "
    "group inverse of s = 1 (V_{(1,1),1} V_{(3,3),3} = I, "
    "dev %.1e)" % inv_dev, inv_dev < 1e-12)

# ================================================================= T5
print("=== T5: (1,3) as a chiral Gauss-compatible seed ===")
a13 = (1 * 1 - 3 * 3) % 8
a10 = (1 * 1 - 0 * 0) % 8
rep("T5 continuum polynomial: (1,3) has q_L^2 - q_R^2 = -8 ≡ 0 "
    "(mod 8), the Z4-even anomaly-free condition; (1,0) has "
    "1 ≢ 0 (mod 8) and is continuum-anomalous",
    a13 == 0 and a10 == 1)

rep("T5 NOMIRROR seed of the covariant UV: (1, 3) is chiral "
    "(1 != 3) and independent-exponent Gauss PASSES with hits %s; "
    "the naive single-exponent filter REJECTS it -- the seed is "
    "invisible to T2 and exists only once the two species are "
    "allowed independent Z4 representation labels"
    % [(gL, gR, s) for gL, gR, s, _ in t3_hits[(1, 3)]],
    t3_admit[(1, 3)] and (not t2_admit[(1, 3)])
    and (1, 3, 1) in [(gL, gR, s) for gL, gR, s, _ in
                      t3_hits[(1, 3)]])

rep("T5 honesty: the same covariant UV admits the continuum-"
    "anomalous pair (1, 0) (hits %s) -- at this size the "
    "Hamiltonian route is NOT an anomaly-polynomial filter; the "
    "T2 single-exponent obstruction is vectorlike (q_L ≡ q_R), "
    "stricter than (q_L^2 - q_R^2) ≡ 0 (mod 8); no 3-4-5-class "
    "multi-species seed is needed at Z4 because (1, 3) already "
    "saturates 1^2 ≡ 3^2, but T2 kills it"
    % [(gL, gR, s) for gL, gR, s, _ in t3_hits[(1, 0)]],
    t3_admit[(1, 0)] and (not t2_admit[(1, 0)]))

print()
print("CENSUS TABLE (admit commuting Gauss?):")
print("   qL\\qR   0      1      2      3     "
      "   [single-g / independent-g / A=qL^2-qR^2 mod 8]")
for qL in range(4):
    row = []
    for qR in range(4):
        sg = "Y" if t2_admit[(qL, qR)] else "n"
        ig = "Y" if t3_admit[(qL, qR)] else "n"
        A = (qL * qL - qR * qR) % 8
        row.append("%s/%s/%d" % (sg, ig, A))
    print("     %d   " % qL + "  ".join("%7s" % c for c in row))
print("   single-g Y iff q_L = q_R; independent-g Y iff True; "
      "A=0 is the continuum Z4 even polynomial")

print()
print("VERDICT: CHIRAL_GAUSS_CENSUS_COMPLETE -- the 1+1D "
      "anomaly-as-Gauss-obstruction mechanism is executable on the "
      "Hamiltonian route: a single Z4 exponent filters to q_L ≡ q_R "
      "(kills all chiral assignments, including the continuum-free "
      "(1,3)); the covariant two-exponent Gauss exists for every "
      "charge pair (Nielsen-Ninomiya / lattice-Dirac doubling) and "
      "supplies (1,3) as a chiral seed that the naive filter cannot "
      "see.  CHIRAL4D.NOMIRROR.01 and TFPT4D.LATTICE.ACTION.01 stay [O]")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
