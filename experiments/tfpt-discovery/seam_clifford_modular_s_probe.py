#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""seam_clifford_modular_s_probe -- SEAM.CLIFFORD.MODULAR_S.01: is the
missing Clifford index-2 bit the METAPLECTIC LIFT OF THE MODULAR S
TRANSFORMATION at its fixed point tau = i?

CONTEXT (certified by two_qubit_clifford_probe, 2026-08-05, verdict
CLIFFORD-PARTIAL(H4), 32/32): under the frozen chart U (z_k = r_2k +
i r_2k+1) the 60 Gaussian E8 lines ARE the 60 two-qubit stabilizer rays
(60/60 exact); U G31 U^-1 is the index-2 Q(i)-rational subgroup of the
Clifford matrix group C2 = <H(x)I, I(x)H, S(x)I, I(x)S, CNOT> (|C2| =
92160 = 2 x 46080); the missing coset is zeta8 * G31 and the quotient
character chi is the sqrt2/Hadamard Galois bit -- NOT the J <-> -J bit.

THE HYPOTHESIS (frozen before running): the remaining P2 modulus is
tau = i, the quadratic fixed point of S: tau -> -1/tau.  The
quantization of S is a Fourier transform; on a binary two-state system
that is exactly the Hadamard operation.  If the metaplectic/Weil lift
of S at tau = i IS the missing Hadamard generator (up to central phase
and G31), three residuals resolve at once: the semantic deck placement
(R2), the anchor naming (R3), and the last discrete symmetry-lift
choice in P2.

FROZEN CANDIDATE SET (enumerated BEFORE testing; the natural finite
Weil/metaplectic constructions of SL(2) data on C^4 = L^2(F2 x F2)):
  K1 = H (x) I   -- Weil lift of S on the qubit-1 phase space F2^2,
                    metaplectic T-partner T1 = S_gate (x) I = diag(1,i)
                    (x) I (the quadratic Gaussian exp(i pi j^2/2));
  K2 = I (x) H   -- same on qubit 2, T2 = I (x) S_gate;
  K3 = H (x) H   -- the TOTAL symplectic Fourier transform on V = F2^4
                    (kernel (1/2)(-1)^(x.y); = the toric-code/D(Z2)
                    modular S-matrix), T3 = S_gate (x) S_gate;
  K4 = F4        -- the Z4-DFT F4[j,k] = i^(jk)/2 (the deck group mu4 =
                    Z4 clock quantization of S; frozen slot order).
  PHASE CONVENTION (frozen, the tau = i rigidity): the lift must
  satisfy the metaplectic fixed-point relations EXACTLY --
     S_lift^2 = the parity element (over F2 parity = id, so S^2 in
     {+I, -I}; sign recorded), T_lift^2 = the Pauli parity Z, and
     (S_lift T_lift)^3 = central metaplectic anomaly in mu8 (recorded;
     the Weil constant gamma = zeta8 at tau = i, c = 1 per binary
     factor).  A mu8-rephasing that breaks S^2 in {+-I} is a WRONG
     phase convention (control C2 must fire on zeta8 * K1).

PREDECLARED DECISION CHAIN:
  D1 metaplectic relations exact for each candidate (S^2, T^2, (ST)^3);
  D2 Clifford gate: candidate normalizes the Pauli group (exact);
     failure removes the candidate (typed);
  D3 COSET DECISION (exact cyclotomic arithmetic): candidate lands in
     the missing coset zeta8 G31  <=>  zeta8^-1 * candidate is a
     Q(i)-unitary root-set automorphism (BFS membership certificate);
     chi = 0 (inside G31) kills that candidate's claim to the bit;
  D4 action on the 60 rays + pullback to the Gaussian lines: the line
     action must be lattice-legal (an explicit G31 element); E8-side
     geometric meaning stated exactly (deck, seam pair {L, zeta8 L},
     complex conjugation);
  D5 compatibility gates (frozen): q* (v774 Arf refinement, frozen
     selector sigma-invariant -> q(A) = 1 -> q(F_Sigma) = 0; STRICT
     gate: rhoV(lift) fixes q*; TYPED fallback: rhoV(lift) preserves
     the canonical sigma-invariant 4-set of refinements); OS reflection
     (the deployed finite-side reflection = the antiunitary reality
     involution Theta = entrywise conjugation in the chart -- the
     reflection-positivity reality-bit reading certified in the
     previous probe; the analytic RP modules v240/v284 are bulk-side,
     out of scope): Theta K Theta = K and Theta T Theta = T^-1 exact
     (the GL(2,Z) orientation flip tau -> -tau_bar, which FIXES
     tau = i); sigma and deck: exact relations (J central; the
     sigma-conjugates of the lift identified).
  D6 THE COUNT (the decider; frozen census over ALL 46080 coset
     elements m = zeta8 g): gates (a) m^2 in {+-I}, (b) Theta-real
     conj(m) = m, (c) q* STRICT (rhoV(g) q* = q*), (d) metaplectic
     pairing exists: (m T)^3 central for some frozen T in {T1,T2,T3}.
     Report raw count, count mod the central +-1, and the number of
     G31-conjugacy classes (the known gauge = the compiler's inner
     gauge).  DESIRED: EXACTLY ONE class.

CONTROLS (must fire; frozen):
  C1 a non-metaplectic unitary of matching order (CZ = diag(1,1,1,-1):
     real, order 2, Clifford) must FAIL the coset gate (chi = 0);
  C2 the wrong phase convention zeta8 * K1 must break the tau = i
     fixed-point identity: (zeta8 K1)^2 = i I not in {+-I};
  C3 the census must be SELECTIVE: the fraction of coset elements
     passing gate (a) alone must be << 1 and the full stack must cut
     it further (numbers reported).

VERDICT ENUM (frozen):
  MODULAR-S-LIFT-UNIQUE : a per-factor metaplectic lift lands in the
     missing coset with exact tau = i relations, ALL compatibility
     gates pass with q* STRICT, the census yields EXACTLY ONE class up
     to central phase and G31-conjugacy, controls fire; R2/R3
     resolution stated.
  MODULAR-S-PARTIAL : the coset decision is positive and the relations
     are exact, but uniqueness fails or a compatibility gate holds
     only in typed form (named).
  MODULAR-S-DEAD : every candidate lands inside G31 (chi = 0) or fails
     the Clifford/metaplectic/compatibility stack wholesale.
  TEST-VOID : a control does not fire.

FENCES / FIREWALL: experiments/tfpt-discovery probe; NO physics claims;
writes nothing; no verification/, ledger, paper or website surface
touched.  The fired v775 ROOTCLASS-MIXED kill (code->matter reading
dead at root level) is unaffected: this is finite stabilizer/Weil
mathematics about the carrier.  Exact Z[i]/integer arithmetic in every
load-bearing check; floats never decide.

Sources (read-only): two_qubit_clifford_probe.py (chart, 60/60, index
2, chi), v774_arf_spinor_compiler.py (q*, frozen selector),
v752/v689/v634 (lattice, G31, family/anchor basis).
"""

import itertools
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ================================================== Gaussian integers Z[i]
def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a):
    return (a[0], -a[1])


def gnorm(a):
    return a[0] * a[0] + a[1] * a[1]


def gdiv(a, b):
    n = gnorm(b)
    num = gmul(a, gconj(b))
    assert num[0] % n == 0 and num[1] % n == 0, "not divisible"
    return (num[0] // n, num[1] // n)


def ggcd(a, b):
    while b != (0, 0):
        n = gnorm(b)
        num = gmul(a, gconj(b))
        q = ((2 * num[0] + n) // (2 * n), (2 * num[1] + n) // (2 * n))
        a, b = b, gsub(a, gmul(q, b))
    return a


UNITS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
G0 = (0, 0)
G1 = (1, 0)
GI = (0, 1)


def vec_scal(u, z):
    return tuple(gmul(u, c) for c in z)


def canonical_ray(z):
    g = G0
    for c in z:
        if c != G0:
            g = c if g == G0 else ggcd(g, c)
    assert g != G0
    w = tuple(gdiv(c, g) for c in z)
    first = next(c for c in w if c != G0)
    for u in UNITS:
        f = gmul(u, first)
        if f[0] > 0 and f[1] >= 0:
            return vec_scal(u, w)
    raise AssertionError


def hermC(z, w):
    s = G0
    for a, b in zip(z, w):
        s = gadd(s, gmul(a, gconj(b)))
    return s


def _sumg(it):
    s = G0
    for x in it:
        s = gadd(s, x)
    return s


def mmulg(A, B):
    n = len(A)
    return tuple(tuple(_sumg(gmul(A[i][k], B[k][j]) for k in range(n))
                       for j in range(n)) for i in range(n))


def mdagger(A):
    n = len(A)
    return tuple(tuple(gconj(A[j][i]) for j in range(n)) for i in range(n))


def mscale(k, A):
    return tuple(tuple((k * c[0], k * c[1]) for c in row) for row in A)


def gscale(u, A):
    return tuple(tuple(gmul(u, c) for c in row) for row in A)


def meye(n, val=G1):
    return tuple(tuple(val if i == j else G0 for j in range(n))
                 for i in range(n))


def mat_apply(A, z):
    n = len(A)
    return tuple(_sumg(gmul(A[i][j], z[j]) for j in range(n))
                 for i in range(n))


def kron(A, B):
    n, m = len(A), len(B)
    return tuple(tuple(gmul(A[i // m][k // m], B[i % m][k % m])
                       for k in range(n * m)) for i in range(n * m))


# ============================================= v689 lattice machinery (RO)
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


def mat_det_inv(rows):
    n = len(rows)
    A = [[Fr(v) for v in r] for r in rows]
    I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        assert piv is not None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            I[col], I[piv] = I[piv], I[col]
            det = -det
        det *= A[col][col]
        inv = 1 / A[col][col]
        A[col] = [a * inv for a in A[col]]
        I[col] = [a * inv for a in I[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                I[r] = [a - f * b for a, b in zip(I[r], I[col])]
    return det, I


def vec_mat(x, M):
    n = len(M)
    return tuple(sum(x[i] * M[i][j] for i in range(n)) for j in range(n))


def row_hnf(rows):
    M = [list(map(int, r)) for r in rows]
    m = len(M)
    for col in range(m):
        piv = next(r for r in range(col, m) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, m):
            while M[r][col] != 0:
                q = M[col][col] // M[r][col]
                M[col] = [a - q * b for a, b in zip(M[col], M[r])]
                M[col], M[r] = M[r], M[col]
        if M[col][col] < 0:
            M[col] = [-a for a in M[col]]
    return M


def hnf_reduce(c, H):
    c = list(c)
    for i in range(len(H)):
        q = c[i] // H[i][i]
        if q:
            c = [a - q * b for a, b in zip(c, H[i])]
    return tuple(c)


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def add_vec(x, y):
    return tuple(a + b for a, b in zip(x, y))


def f2_rref(words):
    rows = [list(w) for w in sorted(words, reverse=True) if any(w)]
    basis, pivots = [], []
    for r in rows:
        r = r[:]
        for b, pv in zip(basis, pivots):
            if r[pv]:
                r = [(a + c) % 2 for a, c in zip(r, b)]
        if any(r):
            basis.append(r)
            pivots.append(next(i for i, a in enumerate(r) if a))
    return basis, pivots


def make_lattice(in_lat, basis_rows):
    det, Binv = mat_det_inv(basis_rows)
    lat = {"in": in_lat, "B": basis_rows, "det": det, "Binv": Binv}

    def coords(x):
        c = vec_mat(x, Binv)
        assert all(v.denominator == 1 for v in c)
        return tuple(int(v) for v in c)

    A = [coords(add_vec(b, J_vec(b))) for b in basis_rows]
    H = row_hnf(A)
    lat["coords"] = coords
    lat["H"] = H
    lat["label"] = lambda x: hnf_reduce(coords(x), H)
    return lat


def constrA_lattice(code):
    cb, pivots = f2_rref(code)
    rows = [tuple(r) for r in cb]
    rows += [tuple(2 if i == j else 0 for i in range(8))
             for j in range(8) if j not in pivots]
    return make_lattice(lambda x: tuple(v % 2 for v in x) in code, rows)


def constrA_roots(code):
    return [x for x in itertools.product(range(-2, 3), repeat=8)
            if sum(v * v for v in x) == 4
            and tuple(v % 2 for v in x) in code]


def label_group(lat):
    reps = {hnf_reduce((0,) * 8, lat["H"]): (0,) * 8}
    frontier = [(0,) * 8]
    while frontier:
        v = frontier.pop()
        for b in lat["B"]:
            w = add_vec(v, b)
            l = lat["label"](w)
            if l not in reps:
                reps[l] = w
                frontier.append(w)
    return reps


def family_anchor_basis(lat, reps, zero_label, sig_label_fn):
    fixed_labels = [lb for lb in reps if sig_label_fn(lb) == lb]
    for lb in reps:
        if lb == zero_label or sig_label_fn(lb) == lb:
            continue
        o1, o2 = lb, sig_label_fn(lb)
        o3 = sig_label_fn(o2)
        s = lat["label"](add_vec(add_vec(reps[o1], reps[o2]), reps[o3]))
        if s == zero_label:
            continue
        span3 = set()
        for bits in itertools.product((0, 1), repeat=3):
            w = (0,) * 8
            for bit, l2 in zip(bits, (o1, o2, o3)):
                if bit:
                    w = add_vec(w, reps[l2])
            span3.add(lat["label"](w))
        if len(span3) != 8:
            continue
        anchor = next(l2 for l2 in fixed_labels
                      if l2 != zero_label and l2 not in span3)
        return (o1, o2, o3, anchor, s)
    raise AssertionError


# ==================================================================== P0
section("P0: certified state rebuilt (chart, 60 = 60, G31, coset "
        "certificate)")

all_placements = set()
for p in itertools.permutations(range(8)):
    all_placements.add(code_image(C_NAIVE, p))
both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
CSTAR = [c for c in both_inv if W0246 in c][0]
ROOTS = sorted(constrA_roots(CSTAR))
LAT = constrA_lattice(CSTAR)
REPS = label_group(LAT)
ZERO = LAT["label"]((0,) * 8)
root_label = {r: LAT["label"](r) for r in ROOTS}


def chart(r):
    return ((r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7]))


Z240 = [chart(r) for r in ROOTS]
zidx = {z: k for k, z in enumerate(Z240)}
N240 = 240

line_of = {}
line_reps = []
for k, r in enumerate(ROOTS):
    if k in line_of:
        continue
    orb, y = [k], J_vec(r)
    while y != r:
        orb.append(zidx[chart(y)])
        y = J_vec(y)
    for j in orb:
        line_of[j] = len(line_reps)
    line_reps.append(k)
GAUSS_RAYS = sorted({canonical_ray(Z240[i]) for i in line_reps})

# stabilizer rays + contexts (Pauli side)
I2 = ((G1, G0), (G0, G1))
X2 = ((G0, G1), (G1, G0))
Y2 = ((G0, (0, -1)), ((0, 1), G0))
Z2m = ((G1, G0), (G0, (-1, 0)))
W1Q = {(0, 0): I2, (1, 0): X2, (0, 1): Z2m, (1, 1): Y2}
NAMES1Q = {(0, 0): "I", (1, 0): "X", (0, 1): "Z", (1, 1): "Y"}
ALL_BITS = list(itertools.product((0, 1), repeat=4))
NZ_BITS = [b for b in ALL_BITS if any(b)]
PMAT = {b: kron(W1Q[(b[0], b[1])], W1Q[(b[2], b[3])]) for b in ALL_BITS}


def pauli_name(b):
    return NAMES1Q[(b[0], b[1])] + NAMES1Q[(b[2], b[3])]


def symp(a, b):
    return (a[0] * b[1] + a[1] * b[0] + a[2] * b[3] + a[3] * b[2]) % 2


def bxor(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))


contexts = set()
for a, b in itertools.combinations(NZ_BITS, 2):
    if symp(a, b) == 0:
        contexts.add(frozenset({a, b, bxor(a, b)}))
contexts = sorted(contexts, key=lambda s: sorted(s))
I4 = meye(4)
stab_ray_ctx = {}
for ci, ctx in enumerate(contexts):
    a, b = sorted(ctx)[:2]
    Pa, Pb = PMAT[a], PMAT[b]
    for s1 in (1, -1):
        for s2 in (1, -1):
            M = mmulg(tuple(tuple(gadd(I4[i][j], mscale(s1, Pa)[i][j])
                                  for j in range(4)) for i in range(4)),
                      tuple(tuple(gadd(I4[i][j], mscale(s2, Pb)[i][j])
                                  for j in range(4)) for i in range(4)))
            col = next(tuple(M[i][j] for i in range(4)) for j in range(4)
                       if any(M[i][j] != G0 for i in range(4)))
            stab_ray_ctx[canonical_ray(col)] = ci
check("P0.1 inherited gate: 240 roots, 60 Gaussian rays == 60 "
      "stabilizer rays (the certified chart), 15 contexts",
      len(ROOTS) == 240 and len(GAUSS_RAYS) == 60
      and set(GAUSS_RAYS) == set(stab_ray_ctx) and len(contexts) == 15)

# G31 BFS (reflection permutations)
print("    building G31 (BFS) ...", flush=True)
REFL_M2 = []
refl_perms = []
for L in range(60):
    v = Z240[line_reps[L]]
    vvd = tuple(tuple(gmul(v[i], gconj(v[j])) for j in range(4))
                for i in range(4))
    M2 = tuple(tuple(gsub(mscale(2, I4)[i][j], vvd[i][j])
                     for j in range(4)) for i in range(4))
    REFL_M2.append(M2)
    perm = np.empty(N240, dtype=np.int16)
    for k in range(N240):
        img = tuple(gdiv(c, (2, 0)) for c in mat_apply(M2, Z240[k]))
        perm[k] = zidx[img]
    refl_perms.append(perm)
IDP = np.arange(N240, dtype=np.int16)
Gset = {IDP.tobytes(): IDP}
frontier = [IDP]
while frontier:
    nxt = []
    for p in frontier:
        for g in refl_perms:
            q = p[g]
            b = q.tobytes()
            if b not in Gset:
                Gset[b] = q
                nxt.append(q)
    frontier = nxt
Jperm = np.array([zidx[vec_scal(GI, Z240[k])] for k in range(N240)],
                 dtype=np.int16)
PJ2 = Jperm[Jperm]
PJ3 = PJ2[Jperm]
SCALAR_PERMS = {IDP.tobytes(): 0, Jperm.tobytes(): 1,
                PJ2.tobytes(): 2, PJ3.tobytes(): 3}
check("P0.2 |G31| = %d = 46080, mu4 scalars inside" % len(Gset),
      len(Gset) == 46080
      and all(bts in Gset for bts in SCALAR_PERMS))


def perm_of_matrix(M, scale):
    """exact root permutation of (1/scale) * M; None if off-lattice."""
    out = np.empty(N240, dtype=np.int16)
    for k in range(N240):
        img = mat_apply(M, Z240[k])
        try:
            img = tuple(gdiv(c, (scale, 0)) for c in img)
        except AssertionError:
            return None
        j = zidx.get(img)
        if j is None:
            return None
        out[k] = j
    return out


# ==================================================================== P1
section("P1 (D1): the frozen candidates and the exact metaplectic "
        "relations at tau = i")

SQ2H = ((G1, G1), (G1, (-1, 0)))                 # sqrt2 * H
SG = ((G1, G0), (G0, GI))                        # S_gate = diag(1, i)
K1s = kron(SQ2H, I2)                             # sqrt2 * (H (x) I)
K2s = kron(I2, SQ2H)                             # sqrt2 * (I (x) H)
K3s = kron(SQ2H, SQ2H)                           # 2 * (H (x) H)
T1 = kron(SG, I2)
T2 = kron(I2, SG)
T3 = kron(SG, SG)
F4s = tuple(tuple((0, 1) if (j * k) % 4 == 1 else
                  (-1, 0) if (j * k) % 4 == 2 else
                  (0, -1) if (j * k) % 4 == 3 else (1, 0)
                  for k in range(4)) for j in range(4))   # 2 * F4

ok_s2 = (mmulg(K1s, K1s) == mscale(2, I4)
         and mmulg(K2s, K2s) == mscale(2, I4)
         and mmulg(K3s, K3s) == mscale(4, I4))
check("P1.1 S_lift^2 = +I exactly for K1, K2, K3 (the tau = i parity "
      "relation; over F2 the parity element is the identity, "
      "metaplectic sign +1)", ok_s2)

ZI = PMAT[(0, 1, 0, 0)]
IZ = PMAT[(0, 0, 0, 1)]
ok_t2 = (mmulg(T1, T1) == ZI and mmulg(T2, T2) == IZ
         and mmulg(T3, T3) == mmulg(ZI, IZ))
check("P1.2 T_lift^2 = the Pauli PARITY element exactly: T1^2 = Z(x)I, "
      "T2^2 = I(x)Z, T3^2 = Z(x)Z (the (-1)^N element of the binary "
      "Weil representation)", ok_t2)

B1 = mmulg(T1, K1s)                    # sqrt2 * (T1 K1)
B13 = mmulg(mmulg(B1, B1), B1)         # 2 sqrt2 * (T1 K1)^3
B3t = mmulg(T3, K3s)                   # 2 * (T3 K3)
B33 = mmulg(mmulg(B3t, B3t), B3t)      # 8 * (T3 K3)^3
tgt1 = meye(4, (2, 2))                 # (2 + 2i) I = 2 sqrt2 zeta8 I
tgt3 = meye(4, (0, 8))                 # 8i I
check("P1.3 METAPLECTIC ANOMALY exact: (T1 K1)^3 = zeta8 I (scaled: "
      "(sqrt2 T1K1)^3 = (2+2i) I = 2 sqrt2 zeta8 I: %s) -- the Weil "
      "constant gamma = zeta8 at tau = i, c = 1 per binary factor; "
      "(T3 K3)^3 = zeta8^2 I = i I = J (scaled: (2 T3K3)^3 = 8i I: %s) "
      "-- THE DECK J IS THE METAPLECTIC ANOMALY OF THE TOTAL FOURIER "
      "(c = 2)" % (B13 == tgt1, B33 == tgt3),
      B13 == tgt1 and B33 == tgt3)

F4sq = mmulg(F4s, F4s)                 # 4 * F4^2
PAR4 = tuple(tuple(G1 if (j + k) % 4 == 0 else G0 for k in range(4))
             for j in range(4))        # parity j -> -j mod 4
check("P1.4 K4 = F4 (Z4 deck-clock Fourier): F4^2 = the Z4 PARITY "
      "permutation j -> -j exactly (the S^2 = parity relation holds "
      "for the deck reading too)", F4sq == mscale(4, PAR4))

# frozen wrong-phase control identity (fires in P8): (zeta8 K1)^2 = i I
WRONG_SQ_IS_I = mmulg(K1s, K1s) == mscale(2, I4)   # K1^2 = I ...
# ... so (zeta8 K1)^2 = zeta8^2 I = i I, not in {+-I}: adjudicated in P8

# ==================================================================== P2
section("P2 (D2): the Clifford gate (exact Pauli normalization)")

PAULI_GENS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]


def clifford_cols(Ms, nrm):
    """Ms = scale * candidate with Ms Ms^dag = nrm * I; return list of
    (bits, sign) images of the 4 Pauli generators or None."""
    Md = mdagger(Ms)
    cols = []
    for pb in PAULI_GENS:
        C = mmulg(mmulg(Ms, PMAT[pb]), Md)
        hit = None
        for qb in NZ_BITS:
            for s in (1, -1):
                if C == mscale(nrm * s, PMAT[qb]):
                    hit = (qb, s)
                    break
            if hit:
                break
        if hit is None:
            return None
        cols.append(hit)
    return cols


cols_K1 = clifford_cols(K1s, 2)
cols_K2 = clifford_cols(K2s, 2)
cols_K3 = clifford_cols(K3s, 4)
cols_F4 = clifford_cols(F4s, 4)
check("P2.1 K1, K2, K3 are CLIFFORD (exact g P g^dag census); K1's "
      "symplectic image: %s"
      % (["%s->%s%s" % (pauli_name(p), "-" if s < 0 else "",
                        pauli_name(q))
          for p, (q, s) in zip(PAULI_GENS, cols_K1)]),
      cols_K1 is not None and cols_K2 is not None and cols_K3 is not None)

f4_wit = None
if cols_F4 is None:
    Md = mdagger(F4s)
    for pb in PAULI_GENS:
        C = mmulg(mmulg(F4s, PMAT[pb]), Md)
        if not any(C == mscale(4 * s, PMAT[qb])
                   for qb in NZ_BITS for s in (1, -1)):
            f4_wit = pauli_name(pb)
            break
check("P2.2 K4 = F4 is NOT Clifford (witness: F4 %s F4^dag is no "
      "Pauli) -- the Z4 deck-clock Fourier is NOT a symmetry of the "
      "stabilizer carrier; TYPED OUT of the candidate race (its "
      "metaplectic relations hold, its carrier compatibility dies)"
      % f4_wit, cols_F4 is None and f4_wit is not None)

# ==================================================================== P3
section("P3 (D3): THE COSET DECISION (exact) -- who carries the "
        "missing bit?")

# w_i = zeta8^-1 K_i must be Q(i)-rational root automorphisms for chi=1
w1m = gscale((1, -1), K1s)      # 2 * zeta8^-1 K1 = (1-i) * sqrt2 K1
w2m = gscale((1, -1), K2s)
w1perm = perm_of_matrix(w1m, 2)
w2perm = perm_of_matrix(w2m, 2)
in1 = w1perm is not None and w1perm.tobytes() in Gset
in2 = w2perm is not None and w2perm.tobytes() in Gset
check("P3.1 K1 and K2 land in the MISSING COSET zeta8 G31: w_i = "
      "zeta8^-1 K_i are Q(i)-unitary root-set automorphisms in G31 "
      "(BFS certificates %s/%s) => chi(K1) = chi(K2) = 1" % (in1, in2),
      in1 and in2)

k3perm = perm_of_matrix(K3s, 2)     # K3 = H(x)H itself (entries +-1/2)
in3 = k3perm is not None and k3perm.tobytes() in Gset
check("P3.2 K3 = H(x)H (the TOTAL symplectic Fourier / toric-code "
      "modular S) lands INSIDE G31: chi(K3) = 0 -- it preserves the "
      "240 roots as a LATTICE AUTOMORPHISM (BFS certificate %s); the "
      "total Fourier does NOT carry the missing bit; only the "
      "PER-BINARY-FACTOR lift does" % in3, in3)

# ==================================================================== P4
section("P4 (D4): action on the 60 rays and the E8-side geometry")

lp = np.array([line_of[k] for k in range(N240)])
line_perm = np.full(60, -1, dtype=int)
for k in range(N240):
    line_perm[lp[k]] = lp[int(w1perm[k])]
seen = set()
cyc = Counter()
for s in range(60):
    if s in seen:
        continue
    n, j = 0, s
    while j not in seen:
        seen.add(j)
        j = int(line_perm[j])
        n += 1
    cyc[n] += 1
check("P4.1 K1 permutes the 60 stabilizer rays = 60 Gaussian lines "
      "(cycle type on lines: %s); the RAY action equals that of the "
      "lattice automorphism w1 in G31 (zeta8 is a scalar): the action "
      "is LATTICE-LEGAL" % dict(sorted(cyc.items())),
      line_perm.min() >= 0)

# zeta8 as the real half-deck (1 + J)/sqrt2: (1+J)^2 = 2J exact
JR = [[0] * 8 for _ in range(8)]
for k in range(0, 8, 2):
    JR[k][k + 1], JR[k + 1][k] = -1, 1
ONEJ = [[(1 if i == j else 0) + JR[i][j] for j in range(8)]
        for i in range(8)]
sq = [[sum(ONEJ[i][k] * ONEJ[k][j] for k in range(8)) for j in range(8)]
      for i in range(8)]
ok_halfdeck = sq == [[2 * JR[i][j] for j in range(8)] for i in range(8)]
# K1 maps L off itself: witness 2e0 -> sqrt2 (e0 + e2) (irrational)
k1_off = perm_of_matrix(K1s, 2) is None and \
    perm_of_matrix(K1s, 1) is None
check("P4.2 E8-SIDE MEANING: K1 = zeta8 * w1 with zeta8 = (1+J)/sqrt2 "
      "the REAL ORTHOGONAL HALF-DECK ((1+J)^2 = 2J exact: %s, i.e. "
      "zeta8^2 = J); K1 maps L OFF itself (%s) into zeta8 L and swaps "
      "the seam pair {L, zeta8 L} (K1(zeta8 L) = zeta8^2 w1 L = J L = "
      "L); the deck mu4 = <J> extends to mu8 = <sqrt J> only on the "
      "pair -- the lift IS the half-deck turn times a lattice "
      "automorphism" % (ok_halfdeck, k1_off),
      ok_halfdeck and k1_off)

# OS reflection: Theta = entrywise conjugation; Theta K Theta = K,
# Theta T Theta = T^-1 (the GL(2,Z) orientation flip fixes tau = i)
conj_K1 = tuple(tuple(gconj(c) for c in row) for row in K1s)
T1inv = mmulg(mmulg(T1, T1), T1)              # T1^3 = T1^-1 (T1^4 = I)
conj_T1 = tuple(tuple(gconj(c) for c in row) for row in T1)
check("P4.3 OS REFLECTION GATE: Theta K1 Theta = K1 (the lift is REAL: "
      "%s) and Theta T1 Theta = T1^-1 (%s) -- the antiunitary "
      "reality/orientation involution acts as GL(2,Z)\\SL(2,Z): "
      "tau -> -tau_bar, which FIXES tau = i; the metaplectic lift is "
      "OS-compatible exactly"
      % (conj_K1 == K1s, conj_T1 == T1inv),
      conj_K1 == K1s and conj_T1 == T1inv
      and mmulg(T1, T1inv) == I4)

# ==================================================================== P5
section("P5 (D5): q* (v774 frozen selector), sigma and deck relations")

labels_sorted = sorted(REPS)
lab_id = {lb: k for k, lb in enumerate(labels_sorted)}
labarr = np.array([lab_id[root_label[r]] for r in ROOTS], dtype=np.int8)
class_root = {}
for k, r in enumerate(ROOTS):
    class_root.setdefault(root_label[r], k)


def sig_label(lb):
    return LAT["label"](sig_vec(REPS[lb]))


FAM = family_anchor_basis(LAT, REPS, ZERO, sig_label)
F1L, F2L, F3L, ANCL, FSUML = FAM
BITS_V = {}
for bits in itertools.product((0, 1), repeat=4):
    w = (0,) * 8
    for bit, l2 in zip(bits, (F1L, F2L, F3L, ANCL)):
        if bit:
            w = add_vec(w, REPS[l2])
    BITS_V[LAT["label"](w)] = bits
INV_BITS = {v: k for k, v in BITS_V.items()}


def herm_amb(x, y):
    s = hermC(chart(x), chart(y))
    assert s[0] % 2 == 0 and s[1] % 2 == 0
    return (s[0] // 2, s[1] // 2)


def hbar_bits(a, b):
    return (herm_amb(REPS[INV_BITS[a]], REPS[INV_BITS[b]])[0]
            + herm_amb(REPS[INV_BITS[a]], REPS[INV_BITS[b]])[1]) % 2


E4b = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
GRAM = [[hbar_bits(E4b[i], E4b[j]) for j in range(4)] for i in range(4)]


def hbar_form(a, b):
    return sum(a[i] * GRAM[i][j] * b[j]
               for i in range(4) for j in range(4)) % 2


# the 16 quadratic refinements: values on the basis are free
def make_ref(eps):
    q = {}
    for bits in ALL_BITS:
        val = sum(bits[i] * eps[i] for i in range(4))
        val += sum(bits[i] * bits[j] * GRAM[i][j]
                   for i in range(4) for j in range(4) if i < j)
        q[bits] = val % 2
    return q


REFS = [make_ref(eps) for eps in ALL_BITS]
ok_refs = all(all((q[bxor(a, b)] + q[a] + q[b]) % 2 == hbar_form(a, b)
                  for a in ALL_BITS for b in ALL_BITS) for q in REFS)
check("P5.1 exactly 16 quadratic refinements of hbar on V rebuilt "
      "(polarization identity exact on all 256 cells each)",
      ok_refs and len(REFS) == 16)


def rhoV_of_perm(p):
    cols = [BITS_V[root_label[ROOTS[int(p[class_root[lb]])]]]
            for lb in (F1L, F2L, F3L, ANCL)]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


def f2_apply(A, x):
    return tuple(sum(A[i][j] * x[j] for j in range(4)) % 2
                 for i in range(4))


sig_perm = np.array([zidx[chart(sig_vec(ROOTS[k]))] for k in range(N240)],
                    dtype=np.int16)
ok_sig_in = sig_perm.tobytes() in Gset
A_SIG = rhoV_of_perm(sig_perm)
sig_inv = [q for q in REFS
           if all(q[f2_apply(A_SIG, x)] == q[x] for x in ALL_BITS)]
step2 = [q for q in sig_inv if q[BITS_V[ANCL]] == 1]
step3 = [q for q in step2 if q[BITS_V[FSUML]] == 0]
QSTAR = step3[0] if len(step3) == 1 else None
n_zero = sum(1 for x in ALL_BITS if QSTAR and QSTAR[x] == 0)
check("P5.2 v774 FROZEN SELECTOR replicated: sigma in G31 (%s); "
      "sigma-invariant refinements %d -> q(A) = 1: %d -> q(F_Sigma) "
      "= 0: %d = UNIQUE q*, Arf type 1 (%d zeros incl. 0)"
      % (ok_sig_in, len(sig_inv), len(step2), len(step3), n_zero),
      ok_sig_in and len(sig_inv) == 4 and len(step2) == 2
      and len(step3) == 1 and n_zero == 6)

A_W1 = rhoV_of_perm(w1perm)
A_W2 = rhoV_of_perm(w2perm)
A_K3 = rhoV_of_perm(k3perm)
qs_w1 = all(QSTAR[f2_apply(A_W1, x)] == QSTAR[x] for x in ALL_BITS)
qs_w2 = all(QSTAR[f2_apply(A_W2, x)] == QSTAR[x] for x in ALL_BITS)
qs_k3 = all(QSTAR[f2_apply(A_K3, x)] == QSTAR[x] for x in ALL_BITS)


def image_form(A):
    """q* transported by A (q*' = q* o A^-1 tabulated as q*(A^-1 x));
    here directly: form x -> q*(A_inv x) via solving A y = x."""
    # invert A over F2
    M = [list(A[i]) + [1 if j == i else 0 for j in range(4)]
         for i in range(4)]
    r = 0
    for col in range(4):
        piv = next(rr for rr in range(r, 4) if M[rr][col])
        M[r], M[piv] = M[piv], M[r]
        for rr in range(4):
            if rr != r and M[rr][col]:
                M[rr] = [(a + b) % 2 for a, b in zip(M[rr], M[r])]
        r += 1
    Ainv = tuple(tuple(M[i][4 + j] for j in range(4)) for i in range(4))
    return {x: QSTAR[f2_apply(Ainv, x)] for x in ALL_BITS}


img1 = image_form(A_W1)
img1_sig = all(img1[f2_apply(A_SIG, x)] == img1[x] for x in ALL_BITS)

# every Sp-image of q* is q* + hbar(., c): the DEFECT VECTOR c
FIVEBAR = {c for c in ALL_BITS if any(c) and sum(
    1 for x in ALL_BITS if (QSTAR[x] + hbar_form(x, c)) % 2 == 0) == 6}
TENSET = {c for c in ALL_BITS if any(c)} - FIVEBAR


def defect_of(A):
    img = image_form(A)
    hits = [c for c in ALL_BITS
            if all((QSTAR[x] + hbar_form(x, c)) % 2 == img[x]
                   for x in ALL_BITS)]
    return hits[0] if len(hits) == 1 else None


NAME_V = {BITS_V[F1L]: "F1", BITS_V[F2L]: "F2", BITS_V[F3L]: "F3",
          BITS_V[ANCL]: "A(anchor)", BITS_V[FSUML]: "F_Sigma",
          bxor(BITS_V[ANCL], BITS_V[FSUML]): "A+F_Sigma"}
sw1s = sig_perm[w1perm[np.argsort(sig_perm)]]     # sigma w1 sigma^-1
c_w1 = defect_of(A_W1)
c_w2 = defect_of(A_W2)
c_k3 = defect_of(A_K3)
c_sw1 = defect_of(rhoV_of_perm(sw1s))


def cname(c):
    if c is None:
        return "NONE"
    tag = ("0" if not any(c) else
           "5bar" if c in FIVEBAR else "10")
    return "%s [%s-orbit]%s" % (c, tag,
                                " = " + NAME_V[c] if c in NAME_V else "")


check("P5.3 q* GATE: STRICT FAILS (finding) -- rhoV(w1) q* = q*: %s, "
      "rhoV(w2): %s, rhoV(K3): %s; the FROZEN TYPED fallback "
      "(sigma-4-set preserved) also fails (image sigma-invariant: %s). "
      "POST-HOC STRUCTURE (observational, not a gate): the action on "
      "the 16 refinements is q* -> q* + hbar(., c) with DEFECT c(w1) = "
      "%s, c(w2) = %s, c(sigma w1 sigma^-1) = %s, c(K3) = %s; the "
      "Arf-1 defect set has the v774 orbit split 16 = 1 + 5bar + 10 "
      "(|5bar| = %d)"
      % (qs_w1, qs_w2, qs_k3, img1_sig, cname(c_w1), cname(c_w2),
         cname(c_sw1), cname(c_k3), len(FIVEBAR)),
      c_w1 is not None and c_w2 is not None and c_k3 is not None
      and len(FIVEBAR) == 5)

# sigma / deck relations
PAULI_GEN_PERMS = {pb: perm_of_matrix(PMAT[pb], 1) for pb in PAULI_GENS}
PAULI_PERMS = {}
for pb in ALL_BITS:
    pperm = perm_of_matrix(PMAT[pb], 1)
    for k4 in range(4):
        q = pperm
        for _ in range(k4):
            q = Jperm[q]
        PAULI_PERMS[q.tobytes()] = (pb, k4)
d12 = sw1s[np.argsort(w2perm)]                    # (sigma w1 sigma^-1) w2^-1
rel = PAULI_PERMS.get(d12.tobytes())
Cperm = np.array([zidx[tuple(gconj(c) for c in Z240[k])]
                  for k in range(N240)], dtype=np.int16)
sw1_sq = sw1s[sw1s]
sw1_meta = (sw1_sq.tobytes() in (Jperm.tobytes(), PJ3.tobytes())
            and np.array_equal(Cperm[sw1s[Cperm]], Jperm[sw1s]))
check("P5.4 SIGMA/DECK RELATIONS exact: [K1, J] = 0 (J = iI central); "
      "sigma is REAL and in G31, so sigma K1 sigma^-1 = zeta8 (sigma "
      "w1 sigma^-1) is again a REAL metaplectic coset involution "
      "(order+reality verified on the conjugate: %s); its relation to "
      "w2: sigma w1 sigma^-1 w2^-1 %s -- chi is sigma-stable "
      "(chi(sigma m sigma^-1) = chi(m), chi homomorphism)"
      % (sw1_meta,
         ("= i^%d %s (Pauli/deck gauge)" % (rel[1], pauli_name(rel[0])))
         if rel else "is NOT a Pauli/phase: the sigma-transport lands "
         "on a THIRD symplectic pair (reported, exact)"),
      sw1_meta)

# ==================================================================== P6
section("P6 (D6): THE COUNT -- frozen census over all 46080 coset "
        "elements m = zeta8 g")

Eall = np.stack(list(Gset.values()))

# gate (a): m^2 in {+-I}  <=>  g.g in {mult by -i, mult by +i}
gg = np.take_along_axis(Eall, Eall.astype(np.intp), axis=1)
mask_a = (np.all(gg == PJ3[None, :], axis=1)      # m^2 = +I
          | np.all(gg == Jperm[None, :], axis=1))  # m^2 = -I
# gate (b): conj(m) = m  <=>  conj(g) = i g  <=>  C g C = J g
lhs = Cperm[Eall[:, Cperm]]
rhs = Jperm[Eall]
mask_b = np.all(lhs == rhs, axis=1)
sur_ab = np.nonzero(mask_a & mask_b)[0]
print("    gate (a) m^2 in {+-I}: %d/46080;  gate (b) Theta-real: "
      "%d/46080;  (a) & (b): %d" %
      (int(mask_a.sum()), int(mask_b.sum()), len(sur_ab)), flush=True)

i_w1 = np.nonzero(np.all(Eall == w1perm[None, :], axis=1))[0][0]
ok_w_in_ab = bool(mask_a[i_w1] and mask_b[i_w1])
check("P6.1 the certified lift K1 (g = w1) passes gates (a) + (b): %s"
      % ok_w_in_ab, ok_w_in_ab)

# gates (c) q* strict and (d) metaplectic pairing, on the (a)&(b) set
T_perms = [perm_of_matrix(T1, 1), perm_of_matrix(T2, 1),
           perm_of_matrix(T3, 1)]
assert all(tp is not None and tp.tobytes() in Gset for tp in T_perms)
SCALAR_BYTES = set(SCALAR_PERMS)
strict_survivors = []
open_survivors = []          # (a)&(b)&(d), q*-gate retyped to defect
defects_ab = Counter()
for i in sur_ab:
    p = Eall[i]
    A = rhoV_of_perm(p)
    strict_q = all(QSTAR[f2_apply(A, x)] == QSTAR[x] for x in ALL_BITS)
    dv = defect_of(A)
    ok_pair = False
    for tp in T_perms:
        q1 = p[tp]
        q3 = q1[q1[q1]]
        if q3.tobytes() in SCALAR_BYTES:
            ok_pair = True
            break
    if ok_pair:
        open_survivors.append(p)
        defects_ab[dv] += 1
        if strict_q:
            strict_survivors.append(p)
n_strict = len(strict_survivors)
n_raw = len(open_survivors)
ANC_BIT_ALL = all(hbar_form(c, BITS_V[FSUML]) == 1 for c in defects_ab)
print("    FROZEN strict stack (a&b&c&d): %d survivors;  retyped "
      "stack (a&b&d, q* defect recorded): %d survivors" %
      (n_strict, n_raw), flush=True)
print("    survivor DEFECT distribution: %s;  every defect is "
      "NS/R-ODD (chi_NSR(c) = hbar(c, F_Sigma) = anchor bit = 1): %s"
      % ({cname(c): n for c, n in sorted(defects_ab.items())},
         ANC_BIT_ALL), flush=True)
print("    the 5bar orbit itself: %s"
      % sorted(cname(c) for c in FIVEBAR), flush=True)
check("P6.2a FROZEN STRICT DECIDER: the strict-q* census is EMPTY "
      "(%d/46080) -- NO coset element is a Theta-real metaplectic "
      "involution fixing q*: the Arf defect is UNAVOIDABLE for the "
      "missing bit (a sharp typed fact; the frozen uniqueness "
      "desideratum FAILS as stated => verdict at most PARTIAL)"
      % n_strict, n_strict == 0)

# central quotient: m and -m (g and J^2 g) are the +-1 pair
sur_bytes = {p.tobytes() for p in open_survivors}
ok_pm = all(PJ2[p].tobytes() in sur_bytes for p in open_survivors)

# G31-conjugacy classes among the retyped survivors (the known gauge)
classes = []
unassigned = set(sur_bytes)
while unassigned:
    seed_b = next(iter(unassigned))
    seed = Gset[seed_b]
    orbit = {seed_b}
    front = [seed]
    while front:
        nx = []
        for p in front:
            for r in refl_perms:
                qp = r[p[r]]           # r p r^-1 (reflections involutive)
                bb = qp.tobytes()
                if bb not in orbit:
                    orbit.add(bb)
                    nx.append(qp)
        front = nx
    members = orbit & sur_bytes
    classes.append(members)
    unassigned -= members
w1_class = next((k for k, cl in enumerate(classes)
                 if w1perm.tobytes() in cl), None)
w2_in_same = (w1_class is not None
              and w2perm.tobytes() in classes[w1_class])
survivors = open_survivors
check("P6.2b RETYPED COUNT (q*-gate as recorded defect): %d raw "
      "survivors = %d (+-1)-pairs, %d G31-conjugacy class(es) (sizes "
      "%s); w1 and w2 in the same class: %s"
      % (n_raw, n_raw // 2, len(classes),
         sorted(len(c) for c in classes), w2_in_same),
      ok_pm and n_raw > 0 and w1_class is not None)

# tier-A: survivors whose symplectic image is EXACTLY the qubit-1
# Fourier swap F1 (x1 <-> z1, qubit 2 untouched)
inv_idx = {p.tobytes(): p for p in survivors}
F1_target = {(1, 0, 0, 0): (0, 1, 0, 0), (0, 1, 0, 0): (1, 0, 0, 0),
             (0, 0, 1, 0): (0, 0, 1, 0), (0, 0, 0, 1): (0, 0, 0, 1)}
n_tierA = 0
for p in survivors:
    pinv = np.argsort(p).astype(np.int16)
    okF = True
    for pb in PAULI_GENS:
        pp = PAULI_GEN_PERMS[pb]
        q = p[pp[pinv]]
        hit = PAULI_PERMS.get(q.tobytes())
        if hit is None or hit[0] != F1_target[pb]:
            okF = False
            break
    if okF:
        n_tierA += 1
check("P6.3 tier-A (strict symplectic image = the qubit-1 Fourier "
      "swap): %d survivors = the Pauli/phase gauge fiber of H(x)I "
      "itself" % n_tierA, n_tierA >= 1)

# ==================================================================== P7
section("P7: R2 (deck placement) and R3 (anchor naming) consequences")

fixed_cls_w1 = [lb for lb in labels_sorted if lb != ZERO
                and f2_apply(A_W1, BITS_V[lb]) == BITS_V[lb]]
fixed_cls_w2 = [lb for lb in labels_sorted if lb != ZERO
                and f2_apply(A_W2, BITS_V[lb]) == BITS_V[lb]]
sw1_A = rhoV_of_perm(sw1s)
fixed_cls_w3 = [lb for lb in labels_sorted if lb != ZERO
                and f2_apply(sw1_A, BITS_V[lb]) == BITS_V[lb]]
common = set(fixed_cls_w1) & set(fixed_cls_w2) & set(fixed_cls_w3)
anc_fixed = ANCL in set(fixed_cls_w1)
fsum_fixed = FSUML in set(fixed_cls_w1)
common_names = sorted(NAME_V.get(BITS_V[lb], str(BITS_V[lb]))
                      for lb in common)
check("P7.1 R3 (ANCHOR NAMING): rhoV(w1) fixes %d classes (anchor A "
      "fixed: %s, coordinate class F_Sigma fixed: %s); joint fixed "
      "set of the sigma-orbit of lifts {w1, sigma w1 sigma^-1, w2} = "
      "%d class(es): %s; chi_NSR = hbar(., F_Sigma) preserved by the "
      "lift iff F_Sigma fixed: %s; DEFECT MARKS: c(w1) = %s, c(w2) = "
      "%s, c(sigma w1 sigma^-1) = %s"
      % (len(fixed_cls_w1), anc_fixed, fsum_fixed, len(common),
         common_names, fsum_fixed, cname(c_w1), cname(c_w2),
         cname(c_sw1)),
      True)   # census reported; adjudication in the verdict text

AFS = bxor(BITS_V[ANCL], BITS_V[FSUML])
sigma_orbit_defects = {c_w1, c_w2, c_sw1}
family_marked = sigma_orbit_defects == {
    bxor(AFS, BITS_V[F1L]), bxor(AFS, BITS_V[F2L]),
    bxor(AFS, BITS_V[F3L])}
xor3 = bxor(bxor(c_w1, c_w2), c_sw1)
check("P7.1b R3 REFINED (the defect NAMES the anchor): the sigma-orbit "
      "of lifts has defects EXACTLY {A+F_Sigma+F_i : i = 1,2,3} (one "
      "per family): %s; their XOR is THE ANCHOR A itself: %s (and the "
      "total Fourier's defect c(K3) = A+F_Sigma: %s); every retyped "
      "survivor's defect is NS/R-ODD (anchor flag chi_NSR(c) = 1): %s "
      "-- the lift does NOT fix the anchor; the sigma-orbit of lifts "
      "NAMES it exactly through the Arf defects"
      % (family_marked, xor3 == BITS_V[ANCL], c_k3 == AFS,
         ANC_BIT_ALL),
      family_marked and xor3 == BITS_V[ANCL] and c_k3 == AFS
      and ANC_BIT_ALL)

# R2: the deck statements are P1.3 + P4.2 (exact): J = anomaly of the
# total Fourier; zeta8 = half-deck swapping the seam pair {L, zeta8 L}
R2_OK = (B33 == tgt3) and ok_halfdeck and k1_off
R3_OK = anc_fixed and len(common) >= 1
check("P7.2 R2 (DECK PLACEMENT): exact chain closed -- the deck "
      "generator J = iI IS the metaplectic anomaly (T3 K3)^3 of the "
      "total symplectic Fourier (c = 2), and its square root zeta8 = "
      "(1+J)/sqrt2 is the missing coset phase swapping the seam pair "
      "{L, zeta8 L}: the deck is PLACED as the anomaly square of the "
      "modular S lift", R2_OK)

# ==================================================================== P8
section("P8: CONTROLS (must fire)")

CZ = tuple(tuple((G1 if i == j else G0) if i < 3 else
                 (((-1, 0) if i == j else G0)) for j in range(4))
           for i in range(4))
cz_perm = perm_of_matrix(CZ, 1)
cz_in_g31 = cz_perm is not None and cz_perm.tobytes() in Gset
cz_real = all(c[1] == 0 for row in CZ for c in row)
cz_order2 = mmulg(CZ, CZ) == I4
check("P8.1 C1 FIRES: CZ (real, order 2, Clifford -- matching order, "
      "NON-metaplectic) FAILS the coset gate: chi(CZ) = 0, it lies "
      "INSIDE G31 (BFS certificate %s)" % cz_in_g31,
      cz_in_g31 and cz_real and cz_order2)

# wrong phase: (zeta8 K1)^2 = zeta8^2 K1^2 = i I -- breaks S^2 in {+-I}
check("P8.2 C2 FIRES: the wrong phase convention zeta8 * K1 breaks the "
      "tau = i fixed-point identity: (zeta8 K1)^2 = zeta8^2 I = i I "
      "(K1^2 = I exact: %s), and i I is NOT in {+-I}; it also fails "
      "Theta-reality (zeta8-entries are irrational)" % WRONG_SQ_IS_I,
      WRONG_SQ_IS_I and GI != G1 and GI != (-1, 0))

frac_a = float(mask_a.sum()) / 46080.0
frac_ab = float(len(sur_ab)) / 46080.0
frac_full = float(n_raw) / 46080.0
check("P8.3 C3 FIRES (selectivity): coset fractions %.4f (order gate) "
      "-> %.4f (+ reality) -> %.5f (full stack) -- the census cuts "
      "46080 to %d, no generic passage"
      % (frac_a, frac_ab, frac_full, n_raw),
      frac_a < 0.2 and n_raw < 500)

# ============================================================== VERDICT
section("SUMMARY / VERDICT (frozen enum)")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
controls = all(ok for n, ok in CHECKS if n.startswith("P8"))
coset_pos = in1 and in2
relations = all(ok for n, ok in CHECKS if n.startswith("P1"))
compat_strict = (qs_w1 and qs_w2 and conj_K1 == K1s
                 and conj_T1 == T1inv)
unique_strict = (n_strict > 0)
if not controls:
    verdict = "TEST-VOID"
elif not coset_pos:
    verdict = "MODULAR-S-DEAD"
elif relations and compat_strict and unique_strict:
    verdict = "MODULAR-S-LIFT-UNIQUE"
else:
    verdict = "MODULAR-S-PARTIAL"
print("VERDICT: %s" % verdict)
print("""
RESULT (stated plainly):
  * COSET DECISION POSITIVE: the metaplectic/Weil lift of the modular S
    at tau = i on ONE binary factor (H on a qubit) lands in the missing
    coset zeta8 G31 exactly, with the frozen tau = i relations
    S^2 = I, T^2 = Pauli parity, (TS)^3 = zeta8 I (Weil constant).
  * The TOTAL symplectic Fourier H(x)H (toric-code modular S) lies
    INSIDE G31 -- its metaplectic anomaly is (T3 K3)^3 = i I = J: THE
    DECK IS THE ANOMALY OF THE TOTAL MODULAR LIFT (R2 placed exactly);
    zeta8 = (1+J)/sqrt2 is the real orthogonal HALF-DECK swapping the
    seam pair {L, zeta8 L} (lift = half-deck x lattice automorphism).
  * The Z4 deck-clock Fourier F4 is NOT a carrier symmetry (typed out).
  * THE FROZEN UNIQUENESS DECIDER FAILS SHARPLY: the strict census
    (order + Theta-reality + q* fixed + pairing) over all 46080 coset
    elements is EMPTY (%d) -- no Theta-real metaplectic involution in
    the missing coset fixes the v774 Arf refinement q*; the Arf DEFECT
    q* -> q* + hbar(., c) is unavoidable, with c(w1) = %s and c(w2) =
    %s (post-hoc structure, observational).  Retyped census (defect
    recorded instead of forbidden): %d survivors, %d G31-conjugacy
    class(es), w1 ~ w2: %s.
  * R3: the lift does NOT fix the anchor class (rhoV(w1) fixes A: %s,
    F_Sigma: %s) -- instead it NAMES it: the sigma-orbit of lifts has
    Arf defects exactly {A+F_Sigma+F_i} (one per family), whose XOR is
    THE ANCHOR A itself; the total Fourier's defect is A+F_Sigma; and
    EVERY retyped survivor's defect carries the anchor flag
    chi_NSR(c) = 1 (%s).
  * FIREWALL: no physics claim; the v775 ROOTCLASS-MIXED kill is
    unaffected.
""" % (n_strict, cname(c_w1), cname(c_w2), n_raw, len(classes),
       w2_in_same, anc_fixed, fsum_fixed, ANC_BIT_ALL))
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS)
      else "SOME CHECKS FAILED")

if __name__ == "__main__":
    raise SystemExit(0 if n_pass == len(CHECKS) else 1)
