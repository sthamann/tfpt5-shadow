#!/usr/bin/env python3
"""tfpt4d_hamiltonian_route_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (TFPT4D.LATTICE.ACTION.01 [O] + QFT4D.OS.RECON.01 route
ordering): tfpt4d_first_candidate_probe KILLED the naive Euclidean
candidate at the T2 gate (the interacting overlap determinant breaks
reflection positivity at N_t = 2).  The corpus route says: build the
HAMILTONIAN first, then T = e^{-aH} is positive BY CONSTRUCTION and the
Euclidean chain is RP by construction.  This probe executes that route
on the same physics content:

    Z4 = mu4 lattice gauge theory with STAGGERED fermions on a RING of
    4 sites whose closing (seam) link is a mu4 BACKGROUND i^k (3 quantum
    links; Hilbert dim 4^3 * 2^4 = 1024),
    H = -lam_E sum_l (X_l + X_l^dag)                (electric)
        + w sum_x (psi^dag_x Z_l psi_{x+1} + h.c.)  (gauge-cov. hopping)
        + w (psi^dag_3 i^k psi_0 + h.c.)            (seam link, background)
        + m sum_x (-1)^x psi^dag_x psi_x            (staggered mass),
    with X the flux shift and Z the link phase (X Z X^dag = i^{-1} Z).
    On the RING the seam background is NOT gaugeable away (it feeds the
    Wilson loop), so the mu4 clock sectors are physical.

  T1  GAUSS LAW EXACT: the interior Z4 gauge unitaries
      V_x = X_{l(x-1,x)}^{-1} X_{l(x,x+1)} * i^{n_x} commute with H to
      machine precision -- exact local gauge invariance, fermions
      included.
  T2  POSITIVITY BY CONSTRUCTION: H = H^dag exactly, so T = e^{-aH} is
      symmetric positive definite -- the gate that KILLED the Euclidean
      candidate holds structurally on this route (the point of the
      corpus ordering).
  T3  SEAM PINNING, TWO CORRECT HALVES (a probe finding in itself):
      (a) with DYNAMICAL links the seam background i^k is a pure sector
      RELABELING -- the spectrum is exactly k-independent and an
      explicit intertwiner V with V H(k) V^dag = H(k+1) exists (found
      empirically) -- the correct gauge-theory statement that a single
      background link phase is absorbable when links fluctuate;
      (b) in the BACKGROUND-FIELD (frozen gauge) limit the mu4 clock is
      PHYSICAL: the fermion ring in flux i^k has split ground energies
      with the conjugate pair k = 1, 3 exactly degenerate -- the seam
      boundary condition is a genuine mu4 observable exactly where the
      contract puts it (the seam as a boundary MODULE, not a bulk
      degree of freedom).
  T7  NOT GENERALIZED-FREE (Gaussianity test done right): for a
      fermionic GAUSSIAN state the charge correlator obeys the
      determinantal law <n_{x1}..n_{xk}> = det[G_{xi xj}] with
      G = <psi^dag psi> (this INCLUDES the ring diagrams that a naive
      pair-Wick formula misses -- the naive formula was a typed trap in
      the first version of this probe).  The free control satisfies the
      determinantal law to machine precision; the interacting ground
      state VIOLATES it -- genuinely non-Gaussian, not generalized-free.

  T4/T5/T6 typed: anomaly bookkeeping, index and mirror separation live
  in the Euclidean probes (tfpt4d_t4t7_gates_probe); the content here is
  vectorlike-staggered at reduced size.

HONEST BOUNDARY (dimension-uplift firewall): 1+1D, 4 sites, one
staggered flavor, structure group Z4 (not the TFPT representation
content); no continuum statement; no gate of the contract CLOSES -- the
deliverable is that the corpus-preferred route clears exactly the gate
at which the Euclidean shortcut died.

VERDICT ENUM: HAMILTONIAN_ROUTE_CLEARS_T2 (contract stays [O]).
"""
import numpy as np

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


NS = 4                    # sites
NLQ = NS - 1              # quantum links (open chain)
DL = 4 ** NLQ             # link Hilbert dim
DF = 2 ** NS              # fermion Hilbert dim
D = DL * DF

# link operators in the flux basis |k>, k in Z4
Z1 = np.diag([1j ** k for k in range(4)]).astype(complex)   # link phase
X1 = np.roll(np.eye(4), 1, axis=0).astype(complex)          # flux shift


def link_op(l, M):
    out = np.array([[1.0]], dtype=complex)
    for j in range(NLQ):
        out = np.kron(out, M if j == l else np.eye(4))
    return np.kron(out, np.eye(DF))


# fermion operators via Jordan-Wigner on the site chain
def ferm_op(x):
    out = np.array([[1.0]], dtype=complex)
    sz = np.diag([1.0, -1.0])
    a = np.array([[0, 1], [0, 0]], dtype=complex)   # annihilator
    for j in range(NS):
        if j < x:
            out = np.kron(out, sz)
        elif j == x:
            out = np.kron(out, a)
        else:
            out = np.kron(out, np.eye(2))
    return np.kron(np.eye(DL), out)


PSI = [ferm_op(x) for x in range(NS)]
NUM = [PSI[x].conj().T @ PSI[x] for x in range(NS)]

LAM_E, W_HOP, MASS = 1.0, 0.7, 0.5


def build_H(k_seam=0, lam_e=LAM_E, w=W_HOP, m=MASS):
    """ring of NS sites; links 0..NS-2 quantum, the closing (seam) link
    site NS-1 -> 0 is the mu4 background i^{k_seam}."""
    H = np.zeros((D, D), dtype=complex)
    for l in range(NLQ):
        Xl = link_op(l, X1)
        H += -lam_e * (Xl + Xl.conj().T)
    for x in range(NS - 1):
        U = link_op(x, Z1)
        hop = PSI[x].conj().T @ U @ PSI[x + 1]
        H += w * (hop + hop.conj().T)
    hop_seam = (1j ** k_seam) * (PSI[NS - 1].conj().T @ PSI[0])
    H += w * (hop_seam + hop_seam.conj().T)
    for x in range(NS):
        H += m * ((-1) ** x) * NUM[x]
    return H


H = build_H()

# ---------------------------------------------------------------- T1
def gauss_unitary(x):
    """V_x = X_{l(x-1,x)}^{-1} X_{l(x,x+1)} i^{n_x} (open-chain edges:
    drop the absent link factor)."""
    V = np.eye(D, dtype=complex)
    if x - 1 >= 0:
        V = V @ np.linalg.matrix_power(link_op(x - 1, X1), 3)  # X^{-1}
    if x < NLQ:
        V = V @ link_op(x, X1)
    # i^{n_x} phase on the fermion at x
    phase = np.eye(D, dtype=complex) + (1j - 1) * NUM[x]
    return V @ phase


devs = []
for x in (1, 2):                    # interior sites (do not touch the seam)
    V = gauss_unitary(x)
    devs.append(float(np.max(np.abs(H @ V - V @ H))))
print("   interior Gauss commutators:", ["%.1e" % d for d in devs])
rep("T1 [exact]: the interior Z4 Gauss unitaries commute with H "
    "(max dev %.1e) -- local gauge invariance with fermions included"
    % max(devs), max(devs) < 1e-12)
# edge Gauss ops are sector INTERTWINERS: find the orientation empirically
H0_, H1_ = build_H(k_seam=0), build_H(k_seam=1)
PH0 = np.eye(D, dtype=complex) + (1j - 1) * NUM[0]      # i^{n_0}
best = None
for s in (1, 3):
    for use_phase in (True, False):
        V = np.linalg.matrix_power(link_op(0, X1), s)
        if use_phase:
            V = V @ PH0
        for tgt, lbl in ((H1_, "k+1"), (build_H(k_seam=3), "k-1")):
            dev = float(np.max(np.abs(V @ H0_ @ V.conj().T - tgt)))
            if best is None or dev < best[0]:
                best = (dev, s, use_phase, lbl)
rep("T1 seam covariance [exact]: an explicit intertwiner V = X_0^%d%s "
    "maps H(0) -> H(%s) (dev %.1e) -- the mu4 background transforms "
    "covariantly under the edge gauge structure"
    % (best[1], " i^{n_0}" if best[2] else "", best[3], best[0]),
    best[0] < 1e-12)

# ---------------------------------------------------------------- T2
herm = float(np.max(np.abs(H - H.conj().T)))
wH = np.linalg.eigvalsh(H)
rep("T2 [BY CONSTRUCTION]: H = H^dag exactly (dev %.1e), so "
    "T = e^{-aH} is symmetric positive definite -- the gate that killed "
    "the Euclidean candidate holds structurally on the Hamiltonian "
    "route (spec H in [%.2f, %.2f])" % (herm, wH[0], wH[-1]),
    herm < 1e-12)

# ---------------------------------------------------------------- T3
E0dyn = {}
dev_pin = []
for k in range(4):
    Hp = build_H(k_seam=k)
    dev_pin.append(float(np.max(np.abs(Hp - Hp.conj().T))))
    for x in (1, 2):
        V = gauss_unitary(x)
        dev_pin.append(float(np.max(np.abs(Hp @ V - V @ Hp))))
    E0dyn[k] = float(np.linalg.eigvalsh(Hp)[0])
print("   dynamical-link E0(k):", {k: "%.6f" % E0dyn[k] for k in E0dyn})
spread_dyn = max(E0dyn.values()) - min(E0dyn.values())
rep("T3a [relabeling, the gauge-theory statement]: with DYNAMICAL links "
    "the seam background is exactly absorbable -- E0(k) identical to "
    "%.1e (all sectors hermitian, interior Gauss exact %.1e); one "
    "background link phase is a sector relabeling when links fluctuate"
    % (spread_dyn, max(dev_pin)),
    spread_dyn < 1e-9 and max(dev_pin) < 1e-12)

# background-field limit: fermions in the frozen mu4 flux (dim 16)
def E0_background(k):
    Df = 2 ** NS
    sz = np.diag([1.0, -1.0])
    a = np.array([[0, 1], [0, 0]], dtype=complex)
    def fop(x):
        out = np.array([[1.0]], dtype=complex)
        for j in range(NS):
            out = np.kron(out, sz if j < x else (a if j == x
                                                 else np.eye(2)))
        return out
    ps = [fop(x) for x in range(NS)]
    Hb = np.zeros((Df, Df), dtype=complex)
    for x in range(NS - 1):
        hop = ps[x].conj().T @ ps[x + 1]
        Hb += W_HOP * (hop + hop.conj().T)
    hop = (1j ** k) * (ps[NS - 1].conj().T @ ps[0])
    Hb += W_HOP * (hop + hop.conj().T)
    for x in range(NS):
        Hb += MASS * ((-1) ** x) * (ps[x].conj().T @ ps[x])
    return float(np.linalg.eigvalsh(Hb)[0])


E0bg = {k: E0_background(k) for k in range(4)}
print("   background-field E0(k):", {k: "%.6f" % E0bg[k] for k in E0bg})
spread_bg = max(E0bg.values()) - min(E0bg.values())
rep("T3b [seam pinning physical in the background-field limit]: the "
    "frozen mu4 flux SPLITS the fermion ground energies (spread %.4f > "
    "0) with the conjugate clock pair k = 1, 3 exactly degenerate "
    "(|dE| = %.1e) -- the seam boundary condition is a genuine mu4 "
    "observable exactly as a boundary MODULE"
    % (spread_bg, abs(E0bg[1] - E0bg[3])),
    spread_bg > 1e-6 and abs(E0bg[1] - E0bg[3]) < 1e-10
    and abs(E0bg[0] - E0bg[1]) > 1e-6)

# ---------------------------------------------------------------- T7
def gaussianity_deviation(Hm):
    """deviation of <n_0 n_1 n_2 n_3> from the determinantal law
    det[G_{xy}] that any fermionic GAUSSIAN state satisfies (includes
    all ring diagrams; the naive pair-Wick formula was a typed trap)."""
    wv, vv = np.linalg.eigh(Hm)
    g = vv[:, 0]
    gap = wv[1] - wv[0]
    G = np.zeros((NS, NS), dtype=complex)
    for x in range(NS):
        for y in range(NS):
            G[x, y] = complex(g.conj() @ ((PSI[x].conj().T @ PSI[y]) @ g))
    prod = np.eye(D)
    for x in range(NS):
        prod = prod @ NUM[x]
    lhs = complex(g.conj() @ (prod @ g))
    rhs = np.linalg.det(G)
    return abs(lhs - rhs), gap


dev_int, gap_int = gaussianity_deviation(H)


def free_control():
    """OPEN staggered chain on the FERMION factor alone (dim 16;
    building it on the full space would carry a trivial 4^3-fold link
    degeneracy)."""
    Df = 2 ** NS
    sz = np.diag([1.0, -1.0])
    a = np.array([[0, 1], [0, 0]], dtype=complex)
    def fop(x):
        out = np.array([[1.0]], dtype=complex)
        for j in range(NS):
            out = np.kron(out, sz if j < x else (a if j == x
                                                 else np.eye(2)))
        return out
    ps = [fop(x) for x in range(NS)]
    Hb = np.zeros((Df, Df), dtype=complex)
    for x in range(NS - 1):
        hop = ps[x].conj().T @ ps[x + 1]
        Hb += W_HOP * (hop + hop.conj().T)
    for x in range(NS):
        Hb += MASS * ((-1) ** x) * (ps[x].conj().T @ ps[x])
    wv, vv = np.linalg.eigh(Hb)
    g = vv[:, 0]
    G = np.array([[complex(g.conj() @ ((ps[x].conj().T @ ps[y]) @ g))
                   for y in range(NS)] for x in range(NS)])
    prod = np.eye(Df)
    for x in range(NS):
        prod = prod @ (ps[x].conj().T @ ps[x])
    return abs(complex(g.conj() @ (prod @ g)) - np.linalg.det(G)), \
        float(wv[1] - wv[0])


dev_free, gap_free = free_control()
rep("T7 [not generalized-free]: the interacting ground state VIOLATES "
    "the fermionic determinantal law by %.3e != 0 (gap %.3f), while "
    "the free control satisfies det[G] to %.1e (gap %.3f) -- genuinely "
    "non-Gaussian; the naive pair-Wick formula is a typed trap (ring "
    "diagrams)" % (dev_int, gap_int, dev_free, gap_free),
    dev_int > 1e-6 and dev_free < 1e-10 and gap_free > 1e-6)

rep("T4/T5/T6 typed: bookkeeping/index/mirror gates live in the "
    "Euclidean probes (tfpt4d_t4t7_gates_probe); content here is "
    "vectorlike-staggered at reduced size; no gate closes", True)

print()
print("VERDICT: HAMILTONIAN_ROUTE_CLEARS_T2 -- the corpus-preferred "
      "construction (Gauss-law Hilbert space + hermitian H + "
      "T = e^{-aH}) clears exactly the gate at which the Euclidean "
      "overlap shortcut died, with the mu4 seam pinning physical; "
      "TFPT4D.LATTICE.ACTION.01 and QFT4D.OS.RECON.01 stay [O]")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
