#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wiring_gauge_rp_audit_probe -- SEAM.STATE.WIRING.GAUGE.RP.01
(EXPLORATION ONLY, experiments/; 2026-08-12 -- the mandatory
gauge-covariance audit of the reflection-positivity exclusion,
ordered by the program lead on top of CCXIII (wiring census) and
CCXV (theta-frame decision).  Two exact questions, one corrected
canonical sentence.)

THE LEAD'S TWO QUESTIONS (verbatim scope).
 (a) CONJUGATION: is Theta_S^(J) = g Theta_S^(I) g^{-1} -- i.e.
     are the collar reflections attached to the pure-J and pure-I
     representatives exact rule-gauge conjugates under the integer
     element g_int = (+)_5 J2 (+) I6, and how does the relation
     extend to a generic rule-gauge element?
 (b) COVARIANCE OF THE RP GRAM FORMS: do the strict-collar RP
     Grams transform covariantly under the rule-gauge orbit, so
     that RP(theta, wiring) depends only on the RELATIVE angle
     delta(frame, wiring) -- and hence: is the RP exclusion of a
     wiring (1) gauge-invariant (an orbit statement) or (2) valid
     only at fixed Theta_S (a frame statement, NOT a wiring
     no-go)?

CONVENTIONS (identical to theta_frame_selector_probe / CCXV;
machinery rebuilt inline; READ-ONLY import of tfpt_constants):
16-dim Majorana space, carrier C = 0..9 (channels 1..5, pairs),
boundary B = 10..15 (channel 0, three seats); A_CC = (+)_5 J2,
J3 = A16_dep[B, B]; deployed wiring V_dep = A_int[C, B] (PURE-I,
census point (-1,0,0,0|-1,0,0,0)); parent family A(kappa, m, t, V)
at the frozen probe-7 point (1/2, 1/2, 1/20).  theta_S = pair swap
(X per Majorana pair, v440 lift); half-side = even indices; twist
eta = +i (v519).  Frames: theta' = g_int theta_S g_int^T (integer),
theta_r = g_r theta_S g_r^T with g_r = R(3/5, 4/5) per carrier
pair (+) I6 (rational generic angle).  Wirings on C_rot: pure-I
(u = -I), pure-J (u = J2), the theta_r-selected ray
u = (4/5) I + (3/5) J.  Wiring transport under a gauge g:
V' = g_C^T V g_B (theta-selector convention, CCXV P2.b).  RP
Grams for a frame theta with half-side vectors f_p:
Theta(f_{p1}..f_{pk}) = eta^k phi(theta f_{pk})..phi(theta f_{p1})
(v519 reversal + degree twist), M[a, b] = omega(Theta(m_a) m_b) by
vector-Wick (Pfaffian recursion on kernel dot products
u^T (I + iA) v).  NUMERICAL PROTOCOL (declared): conjugation
relations, torus identities, kernel-covariance law, Gram
covariance at the witnesses, PD decisions (LDL) and the
orientation invariance are EXACT (integer/rational/symbolic
sympy); float64 ONLY in disclosed wards (machinery regression,
defect-law wards, spectra); RNG nowhere (all controls
deterministic).

SMOKE-RUN DISCLOSURE (2026-08-12, one declared smoke round before
freezing; fail-first preserved): smoke-1 ran 20/21 and corrected
EXACTLY ONE hand-prediction by measurement, not inverting any
verdict logic: the reflection-circle SIGN -- with the deployed
convention J = [[0,1],[-1,0]], R(t) = cos t I - sin t J, the
conjugated per-carrier-pair block is cos(2 gamma) X -
sin(2 gamma) Z (NOT +; the CCXV "+" statement is the same circle
traversed with the opposite orientation -- a pure convention),
and the angle-addition target was rebuilt with the corrected
sign.  Two further hand-DERIVATIONS were pre-registered in this
spec before the smoke and CONFIRMED unchanged by it: (i) the
g_int wiring transport sends pure-J to pure-(+I)
(u' = J2^T J2 I = +I) and pure-I to pure-(+J)
(u' = J2^T (-I) = +J2) -- the CCXIII map "pure-I -> pure-(-J)"
used the inverse transport direction; both are the same orbit
statement (signs are flips inside the selected +-ray); (ii) the
strict-collar deg-2 defect law max|M2 - M2^dagger| = 2t|a'| with
a' = a cos(delta) + c sin(delta) at all three equal-orbit witness
configurations.

FROZEN CLAIMS (2026-08-12, frozen + SHA-hashed before the frozen
run):

 P1  THE CONJUGATION ANSWER (question a; exact).
     (a) theta_S wards reproduced (integer involution, orthogonal,
         [theta_S, O16] = 0, theta_S A16_dep theta_S = -A16_dep,
         det +1, side-exchanging, split-preserving); census gauge
         objects reproduced: dim g0 = 16, rule stabilizer = 9;
     (b) THE RELATION HOLDS, BOTH DIRECTIONS, EXACTLY:
         theta^(I) := theta' = g_int theta_S g_int^{-1} AND
         theta_S = g_int theta' g_int^{-1} (g_int^2 = (+)_5(-I2)
         (+) I6 lies in the isotropy of theta_S, so conjugation
         by g_int is an involution on the frame pair); theta' =
         per carrier pair -X, boundary X (integer identity);
     (c) the attached-wiring correspondence transports with the
         frame (exact): the selection map sends theta_S ->
         pure-(+-J) and theta' -> pure-(+-I); g_int transports
         the pure-J wiring to pure-(+I) and pure-I to pure-(+J)
         (u' = g_C^T u g_B per pair; smoke-disclosed signs);
     (d) GENERIC EXTENSION (symbolic): the rule-gauge torus
         g(gamma, y) conjugates theta_S to the frame with
         per-carrier-pair block cos(2 gamma) X - sin(2 gamma) Z
         (boundary: 2y; smoke-corrected sign, see disclosure),
         frame legality (involution, C6 commutant, A16-reversal)
         holds IDENTICALLY on the torus, and conjugation
         composes by angle addition:
         g(g0) . frame(gamma) = frame(gamma + g0) exactly -- the
         generic rule element acts as a rotation of the
         delta-circle.
 P2  THE COVARIANCE ANSWER (question b; exact).
     (a) machinery regression (float): the general-theta
         vector-Wick Grams reproduce the round-60 index machinery
         entrywise (<= 1e-12); strict theta_S regression at the
         deployed parent: raw deg-2 defect 0.1 = 2t, 30 entries;
     (b) THE KERNEL-COVARIANCE LAW (symbolic, the proof): on the
         full symbolic torus with the symbolic wiring W,
         g(gamma, y)^T g(gamma, y) = I16 and
         g^T A(V) g = A(g_C^T V g_B) IDENTICALLY (256 entries
         each, reduced by cos^2 + sin^2 = 1); since every Gram
         entry is a polynomial in kernel dot products
         u^T (I + iA) v of vectors {theta f_p, f_p}, and the
         frame/half-side transport multiplies every vector by g,
         Gram(g theta g^T, gF, A(V)) = Gram(theta, F, A(V'))
         ENTRYWISE -- strict-collar RP is a function of the
         RELATIVE datum (frame, wiring) mod gauge only;
     (c) EXACT GRAM COVARIANCE AT THE WITNESSES: for
         (g, V) in {(g_int, pure-I), (g_int, pure-J),
         (g_r, pure-I)}: LHS Gram(g theta_S g^T, gF, A(V)) ==
         RHS Gram(theta_S, F, A(g_C^T V g_B)) with EXACT
         entrywise equality (sympy expand == 0), 1p and deg-2;
     (d) THE DELTA REDUCTION (symbolic + float wards): the
         transported two-seat law a'_o = a_o cos(delta) +
         c_o sin(delta), delta = y - gamma, with the 1p seat
         identically zero on C_rot; defect-law wards: raw deg-2
         defect = 2t |a'| at (theta_S, pure-I) = 0.1,
         (theta_r, pure-I) = 0.06, (theta', pure-J) = 0.1
         (mirror witness), all <= 1e-12;
     (e) THE WITNESS TABLE AND THE OPTION VERDICT: strict collar
         RP passes EXACTLY (Hermitian + PD by exact LDL) at
         (theta_S, pure-J), (theta', pure-I) and
         (theta_r, (4/5, 3/5)); the 1p/deg-2 spectra of
         (theta_S, pure-J) and (theta', pure-I) agree <= 1e-10
         (covariance corollary; the round-60 V_J numbers
         lam_min 0.3064 / 0.1532); the SAME pure-I wiring fails
         at theta_S (defect 0.1) and the SAME pure-J wiring
         fails at theta' (defect 0.1).  HENCE OPTION (2): the RP
         exclusion of pure-I is a statement AT THE FIXED FRAME
         theta_S -- a frame statement, NOT a gauge-invariant
         wiring no-go; the orbit-invariant content is the
         covariance law itself: EVERY frame's strict collar
         selects exactly its delta = 0 ray, and the pair
         (frame, wiring) enters only through the delta-circle
         coordinate.
 P3  THE ORBIT-INVARIANT PART: THE Z/X EXCLUSION (exact).
     (a) orientation is frame-transport-invariant, symbolically:
         det(R(-gamma) u R(y)) = det u identically, and
         det u = a^2 + c^2 - b^2 - d^2 in Pauli coordinates;
     (b) the Z- and X-wirings have det u = -1 identically, and
         the whole reflection component C_refl has det u =
         -(b^2 + d^2) <= 0 -- so the orientation-propagation
         exclusion E4 fires in EVERY orbit frame: the Z/X
         exclusion IS genuinely rule-gauge-orbit-invariant
         (CONFIRMED, as the lead expected).
 P4  THE CORRECTED CANONICAL SENTENCE (frozen verbatim in this
     log, SHA-hashed).  PERMITTED: "The exact Groebner census
     determines a single admissible three-dimensional wiring
     orbit (the rotation cell C_rot); Z- and X-wirings are
     excluded by orientation propagation, and this exclusion is
     rule-gauge-invariant.  Pure-I and pure-J are connected by an
     integer rule-gauge element and lie on one orbit: pure-I is a
     deployment representative, not a compiler theorem.  Strict
     collar reflection positivity is covariant under the rule
     gauge and depends only on the relative angle delta between
     collar frame and wiring: strict Hermiticity in the theta_S
     frame would select pure-J; the same demand in the
     integer-conjugated frame selects pure-I.  A canonical wiring
     selection requires an additionally derived physical frame."
     FORBIDDEN (equally frozen): "pure-I is compiler-forced";
     "the compiler derives the pure-I wiring"; "strict collar RP
     excludes the J-wiring" (without the frame qualifier).
 C   CONTROLS (must fire; frozen fire rules; NO RNG).
     C1 NON-ORTHOGONAL ELEMENT BREAKS THE KERNEL LAW: the shear
        N = I16 + (1/2) e_0 e_1^T (det 1, not orthogonal) gives
        max|N^T (I + iA) N - (I + i N^T A N)| >= 1/4 exactly
        (the real part N^T N - I != 0) -- orthogonality is
        load-bearing for the covariance;
     C2 NON-RULE GAUGE ELEMENT BREAKS RULE-COVARIANCE: the
        relative-rotation element (g0 but NOT rule stabilizer,
        2-cycle carrier channels only, rational 3/5-4/5)
        transports pure-J OFF the admissible variety: pencil
        quadric a2 c3 - c2 a3 = -4/5 != 0 exact -- the covariance
        orbit statement lives on the RULE gauge only;
     C3 ORIENTATION-FLIP CONTROL: s = (+)_5 Z (+) I6 is
        orthogonal and WOULD legalize the Z-wiring
        (det(Z u) = -det u symbolically) -- but it is NOT
        rule-gauge: s A_CC s^T = -A_CC != A_CC exactly (the bare
        vacuum flips) -- the only way to undo the Z/X exclusion
        leaves the rule gauge: the P3 orbit-invariance is
        non-vacuous;
     C4 eta = +1 at the bare point breaks collar Gram
        Hermiticity (raw defect >= 0.4; v519 twist regression);
     C5 CENSUS REGRESSION GATE: pure-I passes E1 + pencil + E4 +
        canonical census 10/10 with J-coordinate exactly +1/200;
        V_Z passes E1/pencil but fails EXACTLY orientation E4
        (dets == -1).

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 a conjugation / frame ward breaks           -> CONJUGATION-BROKEN
  K2 a covariance / machinery ward breaks        -> COVARIANCE-BROKEN
  K3 an orbit-invariance computation breaks      -> ORIENTATION-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): RP-FRAME-COVARIANT
[CONJUGATION-EXACT(theta' = g_int theta_S g_int^{-1}, both
directions; generic element = delta-circle rotation),
KERNEL-COVARIANCE-EXACT(symbolic torus + exact Gram witnesses),
DELTA-ONLY(defect = 2t|a cos delta + c sin delta|),
EXCLUSION-IS-FRAME-STATEMENT(option 2: fixed-Theta_S statement,
not a wiring no-go), Z-X-EXCLUSION-ORBIT-INVARIANT(det u
gauge-invariant), CANONICAL-SENTENCE-FROZEN] / RP-GAUGE-INVARIANT
/ COVARIANCE-PARTIAL / PIPELINE-BROKEN / CONJUGATION-BROKEN /
COVARIANCE-BROKEN / ORIENTATION-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the covariance statement is over the
rule-gauge orbit as constructed in CCXIII/CCXV (torus symbolic +
integer/rational witnesses); whether the actual seam physics
derives a specific collar frame remains outside the formalized
rules; the v898/v903 [O] premise is unmoved; no marker moves.
NO RH claim.

SPEC v1 (2026-08-12): frozen after the declared smoke round; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline):
theta_frame_selector_probe (CCXV: frame orbit, transport,
selection map), seam_wiring_groebner_probe (CCXIII: census,
g_int, C_refl), seam_ness_parent_probe (round 60: Gram
machinery), v519 (eta = +i), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wiring_gauge_rp_audit_probe.py
"""

import ast
import hashlib
import itertools
import os
import sys
import time

import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402  (READ-ONLY)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

PERMITTED_SENTENCE = (
    "The exact Groebner census determines a single admissible "
    "three-dimensional wiring orbit (the rotation cell C_rot); "
    "Z- and X-wirings are excluded by orientation propagation, "
    "and this exclusion is rule-gauge-invariant.  Pure-I and "
    "pure-J are connected by an integer rule-gauge element and "
    "lie on one orbit: pure-I is a deployment representative, "
    "not a compiler theorem.  Strict collar reflection "
    "positivity is covariant under the rule gauge and depends "
    "only on the relative angle delta between collar frame and "
    "wiring: strict Hermiticity in the theta_S frame would "
    "select pure-J; the same demand in the integer-conjugated "
    "frame selects pure-I.  A canonical wiring selection "
    "requires an additionally derived physical frame.")
FORBIDDEN_SENTENCES = (
    "pure-I is compiler-forced",
    "the compiler derives the pure-I wiring",
    "strict collar RP excludes the J-wiring "
    "(without the frame qualifier)")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ---------------------------------------------------------- bit model
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v]) if bit)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def edge_orbits(perm):
    n_ord = perm_order(perm)
    seen = set()
    out = []
    for i, j in itertools.combinations(range(6), 2):
        e = frozenset({i, j})
        if e in seen:
            continue
        x, y = i, j
        edges = set()
        rev = False
        for _k in range(n_ord):
            edges.add(frozenset({x, y}))
            x, y = perm[x], perm[y]
            if (x, y) == (j, i):
                rev = True
        seen |= edges
        out.append((frozenset(edges), rev, (i, j)))
    return out


DUADS_CH = sorted(itertools.combinations(range(6), 2))
CAR_DUADS = sorted(itertools.combinations(range(1, 6), 2))

I2s = sp.eye(2)
Xs = sp.Matrix([[0, 1], [1, 0]])
Js = sp.Matrix([[0, 1], [-1, 0]])
Zs = sp.Matrix([[1, 0], [0, -1]])


def pauli_coords(M):
    return (sp.expand((M[0, 0] + M[1, 1]) / 2),
            sp.expand((M[0, 1] + M[1, 0]) / 2),
            sp.expand((M[0, 1] - M[1, 0]) / 2),
            sp.expand((M[0, 0] - M[1, 1]) / 2))


def main():
    print("SEAM.STATE.WIRING.GAUGE.RP.01 -- gauge-covariance audit "
          "of the RP wiring exclusion")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (census rebuild)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s" % (BANNED_IDS,),
          not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    QSTAR = cand[0] if cand else None
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5 and set(phi.values()) == set(range(1, 6)))

    def lab(j):
        return 0 if j == V0 else phi[j]

    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                              for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.1 compiler rebuilt: unique q*, |Aut| = %d == 6, "
          "generator pin unique" % len(AUT),
          ok_ref and len(cand) == 1 and ok_phi and len(AUT) == 6
          and len(g_pin) == 1, kill="K0")
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(pia[j])
    PI6 = tuple(PI6)
    cycles = []
    seen = set()
    for i in range(6):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = PI6[j]
        cycles.append(cyc)
    TWO = sorted(next(c for c in cycles if len(c) == 2))
    THREE = sorted(next(c for c in cycles if len(c) == 3))
    a_ch, b_ch = TWO
    check("S0.2 deployed pi = %s, cycle type %s == (1, 2, 3); "
          "2-cycle {%d,%d}, 3-cycle %s"
          % (PI6, cycle_type(PI6), a_ch, b_ch, THREE),
          PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3), kill="K0")

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    CAR_IDX = list(range(10))
    BND_IDX = list(range(10, 16))
    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]

    J2i = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    I2i = np.eye(2, dtype=np.int64)
    IOTA6i = np.vstack([I2i, I2i, I2i])
    orbs = edge_orbits(PI6)

    def put_ordered(A, x, y, B):
        rx, cy = CH[x], CH[y]
        for r in range(len(rx)):
            for c in range(len(cy)):
                A[rx[r], cy[c]] = B[r, c]
                A[cy[c], rx[r]] = -B[r, c]

    A_int = np.zeros((16, 16), dtype=np.int64)
    for edges, rev, rep in orbs:
        i, j = rep
        B = J2i if rev else (IOTA6i if i == 0 else I2i)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    A16_dep = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    okA = (np.array_equal(A_int[np.ix_(img, img)], A_int)
           and np.array_equal(A_int, -A_int.T))
    okD = np.array_equal(A16_dep[np.ix_(img, img)], A16_dep)

    A_CC = A16_dep[np.ix_(CAR_IDX, CAR_IDX)]
    J3 = A16_dep[np.ix_(BND_IDX, BND_IDX)]
    Vdep = A_int[np.ix_(CAR_IDX, BND_IDX)]
    check("S0.3 blocks extracted: A_CC = (+)_5 J2, J3, deployed "
          "wiring V_dep = A_int[C, B]", okA and okD, kill="K0")

    O16 = np.zeros((16, 16), dtype=np.int64)
    for src in range(16):
        O16[img[src], src] = 1
    O_C = O16[np.ix_(CAR_IDX, CAR_IDX)]
    O_B = O16[np.ix_(BND_IDX, BND_IDX)]

    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}
    IOTA_f = IOTA6i.astype(np.float64)

    def compress12(A):
        Ahat = np.zeros((12, 12))
        for (i, j) in DUADS_CH:
            if i == 0:
                Bm = IOTA_f.T @ A[np.ix_(CH[0], CH[j])] / 3.0
            else:
                Bm = A[np.ix_(CH[i], CH[j])]
            for rr in range(2):
                for cc in range(2):
                    Ahat[CH2[i][rr], CH2[j][cc]] = Bm[rr, cc]
                    Ahat[CH2[j][cc], CH2[i][rr]] = -Bm[rr, cc]
        return Ahat

    pf4_c = {}
    Ahat_c = compress12(A_int.astype(np.float64) / 200.0)
    for (i, j) in DUADS_CH:
        Bm = Ahat_c[np.ix_(CH2[i], CH2[j])]
        pf4_c[frozenset({i, j})] = -(Bm[0, 0] * Bm[1, 1]
                                     - Bm[0, 1] * Bm[1, 0])
    sign_c = {d: (1 if v > 0 else -1) for d, v in pf4_c.items()}
    check("S0.4 canonical G_c Pf4 signs rebuilt: 15 nonzero, all "
          "negative",
          all(abs(v) > 1e-16 for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ==================================================================
    section("P1 -- question (a): the conjugation relation")
    # ==================================================================
    T0i = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        T0i[2 * i, 2 * i + 1] = 1
        T0i[2 * i + 1, 2 * i] = 1
    okT_inv = np.array_equal(T0i @ T0i, np.eye(16, dtype=np.int64))
    okT_orth = np.array_equal(T0i @ T0i.T, np.eye(16, dtype=np.int64))
    okT_c6 = np.array_equal(T0i @ O16, O16 @ T0i)
    okT_rev = np.array_equal(T0i @ A16_dep @ T0i, -A16_dep)
    okT_det = int(round(np.linalg.det(T0i.astype(np.float64)))) == 1
    P_S = [2 * i for i in range(8)]
    okT_side = all(T0i[2 * i + 1, 2 * i] == 1 for i in range(8))
    okT_split = all(T0i[r, c] == 0
                    for r in CAR_IDX for c in BND_IDX)

    # census gauge algebra: g0 and rule stabilizer (dims reproduced)
    a2, b2, c2, d2, a3, b3, c3, d3 = sp.symbols(
        "a2 b2 c2 d2 a3 b3 c3 d3", real=True)
    GENS8 = (a2, b2, c2, d2, a3, b3, c3, d3)
    u2 = a2 * I2s + b2 * Xs + c2 * Js + d2 * Zs
    u3 = a3 * I2s + b3 * Xs + c3 * Js + d3 * Zs

    def mkW(u2m, u3m):
        V = sp.zeros(10, 6)
        for i in range(1, 6):
            uo = u2m if i in TWO else u3m
            for s in range(3):
                V[2 * (i - 1):2 * i, 2 * s:2 * s + 2] = uo
        return V

    V_sym = mkW(u2, u3)

    pairsC = list(itertools.combinations(range(10), 2))
    pairsB = list(itertools.combinations(range(6), 2))
    nv = len(pairsC) + len(pairsB)
    A_CCs = sp.Matrix(A_CC.tolist())
    J3s = sp.Matrix(J3.tolist())
    O_Cs = sp.Matrix(O_C.tolist())

    def XC_of(vec):
        X = sp.zeros(10, 10)
        for k, (i, j) in enumerate(pairsC):
            X[i, j] = vec[k]
            X[j, i] = -vec[k]
        return X

    def XB_of(vec):
        X = sp.zeros(6, 6)
        for k, (i, j) in enumerate(pairsB):
            X[i, j] = vec[len(pairsC) + k]
            X[j, i] = -vec[len(pairsC) + k]
        return X

    vsyms = sp.symbols("x0:%d" % nv, real=True)
    XCs = XC_of(vsyms)
    XBs = XB_of(vsyms)
    eqs = []
    eqs += list(sp.expand(XCs * O_Cs - O_Cs * XCs))
    eqs += list(sp.expand(XCs * A_CCs - A_CCs * XCs))
    eqs += list(sp.expand(XBs * J3s - J3s * XBs))
    Meq = sp.Matrix([[sp.diff(e, v) for v in vsyms] for e in eqs])
    g0_basis = Meq.nullspace()
    dim_g0 = len(g0_basis)

    UT2 = sp.expand(u2.T * u2)
    UT3 = sp.expand(u3.T * u3)
    g1_2 = sp.expand(UT2[0, 1])
    g2_2 = sp.expand(UT2[0, 0] - UT2[1, 1])
    g1_3 = sp.expand(UT3[0, 1])
    g2_3 = sp.expand(UT3[0, 0] - UT3[1, 1])
    Mcross = sp.expand(3 * u2 * Js * u3.T)
    pI, pX, pJ, pZ = pauli_coords(Mcross)
    IDEAL_GENS = [g1_2, g2_2, g1_3, g2_3,
                  sp.expand(2 * pI), sp.expand(2 * pX),
                  sp.expand(2 * pZ)]
    gb = sp.groebner(IDEAL_GENS, *GENS8, order="grevlex")

    def rem(expr):
        return gb.reduce(sp.expand(expr))[1]

    rep2, rep3 = TWO[0], THREE[0]
    per_elem = []
    for base in g0_basis:
        XCk = XC_of(list(base))
        XBk = XB_of(list(base))
        dV = sp.expand(XCk * V_sym - V_sym * XBk)
        du2 = dV[2 * (rep2 - 1):2 * rep2, 0:2]
        du3 = dV[2 * (rep3 - 1):2 * rep3, 0:2]
        condsW = []
        for i in range(1, 6):
            ref = du2 if i in TWO else du3
            for s in range(3):
                blk = dV[2 * (i - 1):2 * i, 2 * s:2 * s + 2]
                for e in sp.expand(blk - ref):
                    condsW.append(e)
        d_coords = {}
        for symx, val in zip((a2, b2, c2, d2), pauli_coords(du2)):
            d_coords[symx] = val
        for symx, val in zip((a3, b3, c3, d3), pauli_coords(du3)):
            d_coords[symx] = val
        condsI = []
        for f in IDEAL_GENS:
            df = sp.expand(sum(sp.diff(f, x) * d_coords[x]
                               for x in GENS8))
            condsI.append(sp.expand(rem(df)))
        per_elem.append((condsW, condsI, d_coords))
    n_condW = len(per_elem[0][0])
    n_condI = len(per_elem[0][1])
    lin_rows = []
    for ci in range(n_condW + n_condI):
        monos = set()
        polys = []
        for condsW, condsI, _dc in per_elem:
            e = (condsW[ci] if ci < n_condW
                 else condsI[ci - n_condW])
            pe = sp.Poly(e, *GENS8)
            polys.append(pe)
            monos |= set(pe.monoms())
        for mono in monos:
            lin_rows.append([pe.nth(*mono) for pe in polys])
    Mstab = sp.Matrix(lin_rows)
    stab_basis = Mstab.nullspace()
    dim_stab = len(stab_basis)
    check("P1.1 theta_S wards + census gauge reproduced: theta_S "
          "involution/orthogonal/C6/A16-reversal/det+1/side/split "
          "all exact; dim g0 = %d == 16, rule stabilizer = %d == 9"
          % (dim_g0, dim_stab),
          okT_inv and okT_orth and okT_c6 and okT_rev and okT_det
          and okT_side and okT_split and dim_g0 == 16
          and dim_stab == 9, kill="K1")

    # ---- the integer conjugation relation, both directions (exact)
    T0s = sp.Matrix(T0i.tolist())
    g_int = sp.zeros(16, 16)
    for i in range(5):
        g_int[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Js
    g_int[10:16, 10:16] = sp.eye(6)
    g_int_inv = g_int.T          # orthogonal
    ok_orth_gi = sp.expand(g_int * g_int.T) == sp.eye(16)
    th_int = sp.expand(g_int * T0s * g_int_inv)
    # forward: theta^(I) = g_int theta_S g_int^{-1}
    ok_fw = all(
        th_int[2 * i:2 * i + 2, 2 * i:2 * i + 2] == -Xs
        for i in range(5)) and all(
        th_int[10 + 2 * i:12 + 2 * i, 10 + 2 * i:12 + 2 * i] == Xs
        for i in range(3))
    # backward: theta_S = g_int theta' g_int^{-1} (conjugation by
    # g_int is an involution on the frame pair, since g_int^2 is
    # in the isotropy of theta_S)
    ok_bw = sp.expand(g_int * th_int * g_int_inv - T0s) \
        == sp.zeros(16, 16)
    gsq = sp.expand(g_int * g_int)
    ok_iso = sp.expand(gsq * T0s * gsq.T - T0s) == sp.zeros(16, 16)
    O16s = sp.Matrix(O16.tolist())
    A16s = sp.Matrix(A16_dep.tolist())

    def frame_legal(th):
        inv = sp.expand(th * th) == sp.eye(16)
        c6 = sp.expand(th * O16s - O16s * th) == sp.zeros(16, 16)
        rev = sp.expand(th * A16s * th + A16s) == sp.zeros(16, 16)
        return inv and c6 and rev

    check("P1.2 THE CONJUGATION RELATION (exact, both directions): "
          "theta^(I) = g_int theta_S g_int^{-1} (per carrier pair "
          "-X, boundary X: %s) AND theta_S = g_int theta^(I) "
          "g_int^{-1} (%s; g_int^2 in the isotropy of theta_S: "
          "%s); g_int orthogonal (%s); both frames rule-legal "
          "(%s, %s)"
          % (ok_fw, ok_bw, ok_iso, ok_orth_gi,
             frame_legal(T0s), frame_legal(th_int)),
          ok_fw and ok_bw and ok_iso and ok_orth_gi
          and frame_legal(T0s) and frame_legal(th_int), kill="K1")

    # ---- attached-wiring correspondence under g_int (exact)
    def wiring(u2v, u3v):
        return {a2: u2v[0], b2: u2v[1], c2: u2v[2], d2: u2v[3],
                a3: u3v[0], b3: u3v[1], c3: u3v[2], d3: u3v[3]}

    wI = wiring((-1, 0, 0, 0), (-1, 0, 0, 0))
    wJ = wiring((0, 0, 1, 0), (0, 0, 1, 0))
    V_I = V_sym.subs(wI)
    V_J = V_sym.subs(wJ)
    ok_VI = sp.expand(V_I - sp.Matrix(Vdep.tolist())) \
        == sp.zeros(10, 6)
    gC = g_int[0:10, 0:10]
    gB = g_int[10:16, 10:16]
    V_J_tr = sp.expand(gC.T * V_J * gB)
    V_I_tr = sp.expand(gC.T * V_I * gB)
    # smoke-disclosed signs: pure-J -> pure-(+I), pure-I -> pure-(+J)
    ok_JtoI = sp.expand(V_J_tr - V_sym.subs(
        wiring((1, 0, 0, 0), (1, 0, 0, 0)))) == sp.zeros(10, 6)
    ok_ItoJ = sp.expand(V_I_tr - V_J) == sp.zeros(10, 6)
    # selected-ray transport: g_C (lam J2) g_B^T per pair = -lam I
    lam = sp.symbols("lam", real=True)
    sel_tr = sp.expand(Js * (lam * Js) * sp.eye(2))
    ok_sel = sel_tr == sp.expand(-lam * sp.eye(2))
    check("P1.3 attached-wiring correspondence under g_int "
          "(exact): pure-J transports to pure-(+I) (%s), pure-I "
          "to pure-(+J) (%s) [smoke-disclosed signs; same +-ray "
          "orbit as CCXIII's pure-(-J)]; selected-ray transport "
          "g_C (lam J2) g_B^T = -lam I per pair (%s): the frame "
          "and its selected wiring move together"
          % (ok_JtoI, ok_ItoJ, ok_sel),
          ok_JtoI and ok_ItoJ and ok_sel, kill="K1")

    # ---- generic extension: the symbolic torus (exact)
    cg, sg, cy, sy = sp.symbols("cg sg cy sy", real=True)
    cg0, sg0 = sp.symbols("cg0 sg0", real=True)
    Rg = sp.Matrix([[cg, -sg], [sg, cg]])
    Ry = sp.Matrix([[cy, -sy], [sy, cy]])
    Rg0 = sp.Matrix([[cg0, -sg0], [sg0, cg0]])
    relg = [cg ** 2 + sg ** 2 - 1, cy ** 2 + sy ** 2 - 1,
            cg0 ** 2 + sg0 ** 2 - 1]

    def redrel(e):
        return sp.expand(sp.reduced(sp.expand(e), relg,
                                    cg, sg, cy, sy, cg0, sg0)[1])

    def redrel_mat(M):
        return sp.Matrix(M.rows, M.cols,
                         lambda i, j: redrel(M[i, j]))

    g_tor = sp.zeros(16, 16)
    for i in range(5):
        g_tor[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Rg
    for i in range(3):
        g_tor[10 + 2 * i:12 + 2 * i, 10 + 2 * i:12 + 2 * i] = Ry
    th_tor = sp.expand(g_tor * T0s * g_tor.T)
    # smoke-corrected sign: R X R^T = cos(2g) X - sin(2g) Z in
    # the deployed J/R convention
    pair_form = sp.expand((cg ** 2 - sg ** 2) * Xs
                          - 2 * cg * sg * Zs)
    ok_pair = all(
        redrel_mat(th_tor[2 * i:2 * i + 2, 2 * i:2 * i + 2]
                   - pair_form) == sp.zeros(2, 2)
        for i in range(5))
    ok_inv_t = redrel_mat(sp.expand(th_tor * th_tor) - sp.eye(16)) \
        == sp.zeros(16, 16)
    ok_c6_t = redrel_mat(sp.expand(th_tor * O16s - O16s * th_tor)) \
        == sp.zeros(16, 16)
    ok_rev_t = redrel_mat(sp.expand(th_tor * A16s * th_tor + A16s)) \
        == sp.zeros(16, 16)
    # angle addition: R(g0) [pair_form(gamma)] R(g0)^T =
    # pair_form(gamma + g0)
    Cc = cg * cg0 - sg * sg0
    Ss = sg * cg0 + cg * sg0
    added = sp.expand((Cc ** 2 - Ss ** 2) * Xs - 2 * Cc * Ss * Zs)
    conj = sp.expand(Rg0 * pair_form * Rg0.T)
    ok_add = redrel_mat(conj - added) == sp.zeros(2, 2)
    check("P1.4 GENERIC EXTENSION (symbolic torus): "
          "g(gamma, y) theta_S g^T has per-carrier-pair block "
          "cos(2g) X - sin(2g) Z (%s); frame legality IDENTICAL "
          "on the torus (involution %s, C6 %s, A16-reversal %s); "
          "conjugation composes by angle addition (%s): a generic "
          "rule element acts as a delta-circle rotation"
          % (ok_pair, ok_inv_t, ok_c6_t, ok_rev_t, ok_add),
          ok_pair and ok_inv_t and ok_c6_t and ok_rev_t and ok_add,
          kill="K1")

    # ==================================================================
    section("P2 -- question (b): covariance of the RP Gram forms")
    # ==================================================================
    def wick_factory(A):
        W = np.eye(A.shape[0], dtype=complex) + 1j * A
        memo = {}

        def wick(idx):
            idx = tuple(idx)
            if len(idx) == 0:
                return 1.0 + 0j
            if len(idx) % 2 == 1:
                return 0.0 + 0j
            if idx in memo:
                return memo[idx]
            head, rest = idx[0], idx[1:]
            tot = 0.0 + 0j
            for j, bb in enumerate(rest):
                sub = rest[:j] + rest[j + 1:]
                tot += (-1) ** j * W[head, bb] * wick(sub)
            memo[idx] = tot
            return tot
        return wick

    def gram_idx(basis, r, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis):
            imgs_ = [r[a] for a in reversed(ma)]
            coeff = eta ** len(ma)
            lst = list(imgs_)
            sgn = 1
            for i in range(len(lst)):
                for j in range(len(lst) - 1 - i):
                    if lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                        sgn = -sgn
            ca = coeff * sgn
            ia = tuple(lst)
            for bi, mb in enumerate(basis):
                M[ai, bi] = ca * wick(tuple(list(ia) + list(mb)))
        return M

    r_S = {}
    for i in range(8):
        r_S[2 * i] = 2 * i + 1
        r_S[2 * i + 1] = 2 * i
    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]
    POS1 = [(p,) for p in range(8)]
    POS2 = [()] + [tuple(c) for c in
                   itertools.combinations(range(8), 2)]

    def gram_gen(theta_f, F_f, eta, A, basis_pos):
        W = np.eye(16, dtype=complex) + 1j * A
        imgs_ = [theta_f @ F_f[p] for p in range(len(F_f))]

        def wickv(vecs):
            k = len(vecs)
            if k % 2 == 1:
                return 0.0 + 0j
            if k == 0:
                return 1.0 + 0j
            K = [[vecs[p] @ W @ vecs[q] for q in range(k)]
                 for p in range(k)]

            def rec(idxs):
                if not idxs:
                    return 1.0 + 0j
                head, rest = idxs[0], idxs[1:]
                tot = 0.0 + 0j
                for j, bpos in enumerate(rest):
                    sub = rest[:j] + rest[j + 1:]
                    tot += (-1) ** j * K[head][bpos] * rec(sub)
                return tot
            return rec(list(range(k)))

        n = len(basis_pos)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis_pos):
            va = [imgs_[p] for p in reversed(ma)]
            coeff = eta ** len(ma)
            for bi, mb in enumerate(basis_pos):
                vb = [F_f[p] for p in mb]
                M[ai, bi] = coeff * wickv(va + vb)
        return M

    A_CCf = A_CC.astype(np.float64)
    J3f = J3.astype(np.float64)

    def parentV_f(kap, m, tt, V):
        A = np.zeros((16, 16))
        A[np.ix_(CAR_IDX, CAR_IDX)] = kap * A_CCf
        A[np.ix_(BND_IDX, BND_IDX)] = m * J3f
        A[np.ix_(CAR_IDX, BND_IDX)] = tt * V
        A[np.ix_(BND_IDX, CAR_IDX)] = -tt * V.T
        return A

    T0f = T0i.astype(np.float64)
    F_S = [np.eye(16)[:, a] for a in P_S]
    A_dep = parentV_f(0.5, 0.5, 0.05, Vdep.astype(np.float64))
    wk_dep = wick_factory(A_dep)
    M1_idx = gram_idx(B1_S, r_S, 1j, wk_dep)
    M2_idx = gram_idx(B2_S, r_S, 1j, wk_dep)
    M1_gen = gram_gen(T0f, F_S, 1j, A_dep, POS1)
    M2_gen = gram_gen(T0f, F_S, 1j, A_dep, POS2)
    dev_m = max(float(np.max(np.abs(M1_idx - M1_gen))),
                float(np.max(np.abs(M2_idx - M2_gen))))
    D2S = M2_gen - M2_gen.conj().T
    defS = float(np.max(np.abs(D2S)))
    nentS = int(np.sum(np.abs(D2S) > 1e-12))
    check("P2.1 machinery regression: general-theta == round-60 "
          "index machinery entrywise (max dev %.1e <= 1e-12); "
          "strict theta_S at the deployed parent: raw deg-2 "
          "defect %.4f == 2t = 0.1, %d == 30 entries"
          % (dev_m, defS, nentS),
          dev_m <= 1e-12 and abs(defS - 0.1) <= 1e-12
          and nentS == 30, kill="K2")

    # ---- THE KERNEL-COVARIANCE LAW (symbolic torus; the proof)
    kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                    sp.Rational(1, 20))

    def exact_parent(Vm):
        A_ex = sp.zeros(16, 16)
        A_ex[0:10, 0:10] = kapQ * A_CCs
        A_ex[10:16, 10:16] = mQ * J3s
        A_ex[0:10, 10:16] = tQ * Vm
        A_ex[10:16, 0:10] = -tQ * Vm.T
        return A_ex

    gC_tor = g_tor[0:10, 0:10]
    gB_tor = g_tor[10:16, 10:16]
    ok_orth_tor = redrel_mat(
        sp.expand(g_tor.T * g_tor) - sp.eye(16)) == sp.zeros(16, 16)
    A_of_V = exact_parent(V_sym)
    V_tr_sym = sp.expand(gC_tor.T * V_sym * gB_tor)
    A_of_Vtr = exact_parent(V_tr_sym)
    E_cov = redrel_mat(sp.expand(g_tor.T * A_of_V * g_tor)
                       - A_of_Vtr)
    ok_cov_law = E_cov == sp.zeros(16, 16)
    check("P2.2 THE KERNEL-COVARIANCE LAW (symbolic, generic "
          "wiring, full torus): g^T g = I16 (%s) and "
          "g^T A(V) g = A(g_C^T V g_B) IDENTICALLY (%s) => every "
          "kernel dot product u^T (I + iA) v, hence EVERY Gram "
          "entry, is invariant under (theta, F, V) -> "
          "(g theta g^T, gF, V) with V -> g_C^T V g_B: strict-"
          "collar RP is a function of the RELATIVE (frame, "
          "wiring) datum only"
          % (ok_orth_tor, ok_cov_law),
          ok_orth_tor and ok_cov_law, kill="K2")

    # ---- exact Gram machinery
    def wickv_exact_factory(Aex):
        Wm = sp.eye(16) + sp.I * Aex

        def wickv(vecs):
            k = len(vecs)
            if k % 2 == 1:
                return sp.Integer(0)
            if k == 0:
                return sp.Integer(1)
            K = [[sp.expand((vecs[p].T * Wm * vecs[q])[0, 0])
                  for q in range(k)] for p in range(k)]

            def rec(idxs):
                if not idxs:
                    return sp.Integer(1)
                head, rest = idxs[0], idxs[1:]
                tot = sp.Integer(0)
                for j, bpos in enumerate(rest):
                    w = K[head][bpos]
                    if w != 0:
                        sub = rest[:j] + rest[j + 1:]
                        tot += sp.Integer(-1) ** j * w * rec(sub)
                return tot
            return rec(list(range(k)))
        return wickv

    def gram_gen_exact(theta_s, F_cols, eta, wickv, basis_pos):
        imgs_ = [sp.expand(theta_s * f) for f in F_cols]
        n = len(basis_pos)
        M = sp.zeros(n, n)
        for ai, ma in enumerate(basis_pos):
            va = [imgs_[p] for p in reversed(ma)]
            coeff = eta ** len(ma)
            for bi, mb in enumerate(basis_pos):
                vb = [F_cols[p] for p in mb]
                M[ai, bi] = sp.expand(coeff * wickv(va + vb))
        return M

    def herm_exact(M):
        return sp.expand(M - M.conjugate().T) == sp.zeros(*M.shape)

    def psd_exact(M):
        n = M.shape[0]
        M = sp.Matrix(M)
        pivots = []
        for k in range(n):
            d = sp.nsimplify(sp.re(M[k, k]))
            pivots.append(d)
            if d == 0:
                if any(sp.expand(M[k, j]) != 0 for j in range(k, n)):
                    return False, pivots
                continue
            if d < 0:
                return False, pivots
            for i in range(k + 1, n):
                if M[i, k] != 0:
                    f = M[i, k] / d
                    for j in range(k, n):
                        M[i, j] = sp.expand(M[i, j] - f * M[k, j])
        return True, pivots

    eye16 = sp.eye(16)
    F_S_sym = [eye16[:, a] for a in P_S]
    Rr = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                    [sp.Rational(4, 5), sp.Rational(3, 5)]])
    g_r = sp.zeros(16, 16)
    for i in range(5):
        g_r[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Rr
    g_r[10:16, 10:16] = sp.eye(6)
    th_r = sp.expand(g_r * T0s * g_r.T)

    def exact_grams(th, F_cols, Vm):
        wv = wickv_exact_factory(exact_parent(Vm))
        M1 = gram_gen_exact(th, F_cols, sp.I, wv, POS1)
        M2 = gram_gen_exact(th, F_cols, sp.I, wv, POS2)
        return M1, M2

    def transported(g, Vm):
        return sp.expand(g[0:10, 0:10].T * Vm * g[10:16, 10:16])

    # covariance witness pairs (LHS in the conjugated frame,
    # RHS at theta_S with the transported wiring)
    cov_pairs = [("g_int, pure-I", g_int, th_int, V_I),
                 ("g_int, pure-J", g_int, th_int, V_J),
                 ("g_r,   pure-I", g_r, th_r, V_I)]
    lhs_store = {}
    ok_cov_all = True
    for nm, g, th, Vm in cov_pairs:
        F_g = [sp.expand(g * f) for f in F_S_sym]
        L1, L2 = exact_grams(th, F_g, Vm)
        R1, R2 = exact_grams(T0s, F_S_sym, transported(g, Vm))
        eq1 = sp.expand(L1 - R1) == sp.zeros(*L1.shape)
        eq2 = sp.expand(L2 - R2) == sp.zeros(*L2.shape)
        lhs_store[nm] = (L1, L2)
        ok_cov_all &= (eq1 and eq2)
        print("      cov witness (%s): 1p exact-equal %s, deg-2 "
              "exact-equal %s" % (nm, eq1, eq2), flush=True)
    check("P2.3 EXACT GRAM COVARIANCE at the witnesses: "
          "Gram(g theta_S g^T, gF, A(V)) == Gram(theta_S, F, "
          "A(g_C^T V g_B)) with exact entrywise equality on all "
          "3 (gauge, wiring) pairs, 1p and deg-2", ok_cov_all,
          kill="K2")

    # ---- the delta reduction (symbolic two-seat law + defect wards)
    def redrel4(e):
        return sp.expand(sp.reduced(
            sp.expand(e), relg[:2], cg, sg, cy, sy)[1])

    up2 = sp.expand(Rg.T * u2 * Ry)
    up3 = sp.expand(Rg.T * u3 * Ry)
    a2p, b2p, c2p, d2p = [redrel4(x) for x in pauli_coords(up2)]
    a3p, b3p, c3p, d3p = [redrel4(x) for x in pauli_coords(up3)]
    Cd = cg * cy + sg * sy
    Sd = sy * cg - cy * sg
    rot_sub = {b2: 0, d2: 0, b3: 0, d3: 0}
    ok_cf2 = redrel4(a2p.subs(rot_sub) - (a2 * Cd + c2 * Sd)) == 0
    ok_cf3 = redrel4(a3p.subs(rot_sub) - (a3 * Cd + c3 * Sd)) == 0
    ok_1p = (redrel4(b2p.subs(rot_sub)) == 0
             and redrel4(b3p.subs(rot_sub)) == 0)
    # defect-law float wards: raw deg-2 defect = 2t|a'| at three
    # equal-orbit configurations
    gf_r = np.array(g_r.tolist(), dtype=np.float64)
    th_rf = gf_r @ T0f @ gf_r.T
    F_rf = [gf_r @ f for f in F_S]
    M2r_f = gram_gen(th_rf, F_rf, 1j, A_dep, POS2)
    defR = float(np.max(np.abs(M2r_f - M2r_f.conj().T)))
    gf_i = np.array(g_int.tolist(), dtype=np.float64)
    th_if = gf_i @ T0f @ gf_i.T
    F_if = [gf_i @ f for f in F_S]
    V_Jf = np.array(V_J.tolist(), dtype=np.float64)
    A_J = parentV_f(0.5, 0.5, 0.05, V_Jf)
    M2iJ = gram_gen(th_if, F_if, 1j, A_J, POS2)
    defIJ = float(np.max(np.abs(M2iJ - M2iJ.conj().T)))
    check("P2.4 THE DELTA REDUCTION: transported two-seat law "
          "a' = a cos(delta) + c sin(delta) (%s, %s), 1p seat "
          "identically 0 on C_rot (%s); defect-law wards "
          "2t|a'|: (theta_S, pure-I) %.4f == 0.1, "
          "(theta_r, pure-I) %.4f == 0.06, (theta', pure-J) "
          "%.4f == 0.1 (mirror witness), all <= 1e-12"
          % (ok_cf2, ok_cf3, ok_1p, defS, defR, defIJ),
          ok_cf2 and ok_cf3 and ok_1p
          and abs(defS - 0.1) <= 1e-12
          and abs(defR - 0.06) <= 1e-12
          and abs(defIJ - 0.1) <= 1e-12, kill="K2")

    # ---- the witness table and the option verdict
    M1_SJ, M2_SJ = exact_grams(T0s, F_S_sym, V_J)
    h_SJ = herm_exact(M1_SJ) and herm_exact(M2_SJ)
    p1, piv1 = psd_exact(M1_SJ)
    p2, piv2 = psd_exact(M2_SJ)
    pd_SJ = (p1 and all(p > 0 for p in piv1)
             and p2 and all(p > 0 for p in piv2))
    L1_iI, L2_iI = lhs_store["g_int, pure-I"]
    h_iI = herm_exact(L1_iI) and herm_exact(L2_iI)
    q1, qiv1 = psd_exact(L1_iI)
    q2, qiv2 = psd_exact(L2_iI)
    pd_iI = (q1 and all(p > 0 for p in qiv1)
             and q2 and all(p > 0 for p in qiv2))
    # spectra corollary
    s1a = np.sort(np.linalg.eigvalsh(np.array(
        M1_SJ.evalf(16), dtype=complex)))
    s1b = np.sort(np.linalg.eigvalsh(np.array(
        L1_iI.evalf(16), dtype=complex)))
    s2a = np.sort(np.linalg.eigvalsh(np.array(
        M2_SJ.evalf(16), dtype=complex)))
    s2b = np.sort(np.linalg.eigvalsh(np.array(
        L2_iI.evalf(16), dtype=complex)))
    dev_sp = max(float(np.max(np.abs(s1a - s1b))),
                 float(np.max(np.abs(s2a - s2b))))
    lm1, lm2 = float(s1a[0]), float(s2a[0])
    # theta' + pure-J fails (exact anti-Hermitian defect)
    _L1_iJ, L2_iJ = lhs_store["g_int, pure-J"]
    D_iJ = sp.expand(L2_iJ - L2_iJ.conjugate().T)
    def_iJ = float(max(abs(complex(x)) for x in
                       np.array(D_iJ.evalf(16),
                                dtype=complex).flatten()))
    # theta_r + its selected ray passes exactly
    w_sel = wiring((sp.Rational(4, 5), 0, sp.Rational(3, 5), 0),
                   (sp.Rational(4, 5), 0, sp.Rational(3, 5), 0))
    V_sel = V_sym.subs(w_sel)
    F_r_sym = [sp.expand(g_r * f) for f in F_S_sym]
    M1_rs, M2_rs = exact_grams(th_r, F_r_sym, V_sel)
    h_rs = herm_exact(M1_rs) and herm_exact(M2_rs)
    r1, riv1 = psd_exact(M1_rs)
    r2, riv2 = psd_exact(M2_rs)
    pd_rs = (r1 and all(p > 0 for p in riv1)
             and r2 and all(p > 0 for p in riv2))
    check("P2.5 THE WITNESS TABLE => OPTION (2): strict RP passes "
          "EXACTLY at (theta_S, pure-J) (%s/%s), (theta', pure-I) "
          "(%s/%s) and (theta_r, (4/5,3/5)) (%s/%s); spectra of "
          "the first two agree (dev %.1e <= 1e-10; lam_min %.4f "
          "== 0.3064 +- 0.005, %.4f == 0.1532 +- 0.005); the SAME "
          "pure-I fails at theta_S (0.1) and the SAME pure-J "
          "fails at theta' (%.4f == 0.1): the RP exclusion is a "
          "FIXED-FRAME statement, NOT a gauge-invariant wiring "
          "no-go"
          % (h_SJ, pd_SJ, h_iI, pd_iI, h_rs, pd_rs, dev_sp,
             lm1, lm2, def_iJ),
          h_SJ and pd_SJ and h_iI and pd_iI and h_rs and pd_rs
          and dev_sp <= 1e-10 and abs(lm1 - 0.3064) <= 5e-3
          and abs(lm2 - 0.1532) <= 5e-3
          and abs(def_iJ - 0.1) <= 1e-12, kill="K2")

    # ==================================================================
    section("P3 -- the orbit-invariant part: the Z/X exclusion")
    # ==================================================================
    det_u = sp.expand(u2.det())
    ok_detform = sp.expand(
        det_u - (a2 ** 2 + c2 ** 2 - b2 ** 2 - d2 ** 2)) == 0
    det_tr = redrel4(sp.expand(up2.det()) - det_u)
    ok_detinv = det_tr == 0
    detZ = det_u.subs({a2: 0, b2: 0, c2: 0, d2: 1})
    detX = det_u.subs({a2: 0, b2: 1, c2: 0, d2: 0})
    # C_refl: a = c = 0 => det = -(b^2 + d^2)
    det_refl = sp.expand(det_u.subs({a2: 0, c2: 0}))
    ok_refl = sp.expand(det_refl + b2 ** 2 + d2 ** 2) == 0
    check("P3.1 THE Z/X EXCLUSION IS ORBIT-INVARIANT (exact): "
          "det u = a^2 + c^2 - b^2 - d^2 (%s) is frame-transport-"
          "invariant det(R(-g) u R(y)) = det u identically (%s); "
          "det = -1 for Z (%s) and X (%s) in EVERY orbit frame, "
          "and the whole reflection component has det = "
          "-(b^2 + d^2) <= 0 (%s): orientation propagation E4 "
          "fires on the entire rule-gauge orbit -- CONFIRMED "
          "genuinely gauge-invariant"
          % (ok_detform, ok_detinv, detZ, detX, ok_refl),
          ok_detform and ok_detinv and detZ == -1 and detX == -1
          and ok_refl, kill="K3")

    # ==================================================================
    section("P4 -- the corrected canonical sentence (frozen)")
    # ==================================================================
    sent_sha = hashlib.sha256(
        PERMITTED_SENTENCE.encode("utf-8")).hexdigest()
    print("      PERMITTED (verbatim, sha256 %s):" % sent_sha[:16])
    print("      | " + PERMITTED_SENTENCE.replace(".  ", ".\n      | "))
    print("      FORBIDDEN (verbatim):")
    for s in FORBIDDEN_SENTENCES:
        print("      | " + s)
    check("P4.1 canonical sentence frozen (permitted sha256 %s...; "
          "%d forbidden formulations recorded)"
          % (sent_sha[:16], len(FORBIDDEN_SENTENCES)),
          len(PERMITTED_SENTENCE) > 0
          and len(FORBIDDEN_SENTENCES) == 3)

    # ==================================================================
    section("P5 -- controls (must fire; deterministic)")
    # ==================================================================
    # C1 non-orthogonal element breaks the kernel law
    N_sh = sp.eye(16)
    N_sh[0, 1] = sp.Rational(1, 2)
    A_I_ex = exact_parent(V_I)
    E_C1 = sp.expand(N_sh.T * (sp.eye(16) + sp.I * A_I_ex) * N_sh
                     - (sp.eye(16)
                        + sp.I * sp.expand(N_sh.T * A_I_ex * N_sh)))
    max_C1 = float(max(abs(complex(x)) for x in
                       np.array(E_C1.evalf(16),
                                dtype=complex).flatten()))
    check("C1 non-orthogonal shear N = I + (1/2) e0 e1^T breaks "
          "the kernel law: max|N^T (I+iA) N - (I + i N^T A N)| = "
          "%.4f >= 0.25 (the real part N^T N - I != 0) -- "
          "orthogonality is load-bearing" % max_C1,
          max_C1 >= 0.25, kill="K7")

    # C2 non-rule gauge element: transported pure-J leaves the variety
    g_relm = sp.eye(16)
    for i in TWO:
        r0 = 2 * (i - 1)
        g_relm[r0:r0 + 2, r0:r0 + 2] = Rr
    Vp_rel = sp.expand(g_relm[0:10, 0:10].T * V_J)
    u2rel = Vp_rel[2 * (rep2 - 1):2 * rep2, 0:2]
    u3rel = Vp_rel[2 * (rep3 - 1):2 * rep3, 0:2]
    a2r_, _b, c2r_, _d = pauli_coords(u2rel)
    a3r_, _b3x, c3r_, _d3x = pauli_coords(u3rel)
    minor_val = sp.expand(a2r_ * c3r_ - c2r_ * a3r_)
    check("C2 relative-rotation element (g0, NOT rule stabilizer): "
          "transported pure-J violates the pencil quadric "
          "a2 c3 - c2 a3 = %s == -4/5 != 0 -- the covariance "
          "orbit statement lives on the RULE gauge only"
          % minor_val, minor_val == -sp.Rational(4, 5), kill="K7")

    # C3 orientation-flip control
    s_fl = sp.zeros(16, 16)
    for i in range(5):
        s_fl[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Zs
    s_fl[10:16, 10:16] = sp.eye(6)
    ok_orth_s = sp.expand(s_fl * s_fl.T) == sp.eye(16)
    flip_vac = sp.expand(s_fl[0:10, 0:10] * A_CCs
                         * s_fl[0:10, 0:10].T + A_CCs) \
        == sp.zeros(10, 10)
    det_flip = sp.expand(sp.expand(Zs * u2).det() + det_u) == 0
    check("C3 orientation-flip control s = (+)_5 Z (+) I6: "
          "orthogonal (%s) and WOULD legalize Z "
          "(det(Z u) = -det u: %s) -- but s A_CC s^T = -A_CC "
          "(vacuum flips: %s): the only way to undo the Z/X "
          "exclusion leaves the rule gauge"
          % (ok_orth_s, det_flip, flip_vac),
          ok_orth_s and det_flip and flip_vac, kill="K7")

    # C4 eta = +1 breaks bare Hermiticity
    A0f = np.tanh(0.5) * A16_dep.astype(np.float64)
    M1e = gram_gen(T0f, F_S, 1.0, A0f, POS1)
    defE = float(np.max(np.abs(M1e - M1e.conj().T)))
    check("C4 eta = +1 at the bare point: 1p Gram Hermiticity "
          "defect %.4f >= 0.4 (v519 twist regression)" % defE,
          defE >= 0.4, kill="K7")

    # C5 census regression gate
    def eval_E1(sub):
        return [sp.expand(g.subs(sub)) for g in
                (g1_2, g2_2, g1_3, g2_3)]

    def eval_pencil(sub):
        return [sp.expand(g.subs(sub)) for g in (pI, pX, pZ)]

    def eval_dets(sub):
        return (sp.expand(u2.det().subs(sub)),
                sp.expand(u3.det().subs(sub)))

    def census_exact(sub):
        lamQ = mQ / (1 - mQ ** 2)
        Vm = V_sym.subs(sub)
        S = Vm * J3s * Vm.T
        A_eff = kapQ * A_CCs + lamQ * tQ ** 2 * S
        n_nz, n_sig = 0, 0
        Jco45 = None
        for (i, j) in CAR_DUADS:
            Bx = A_eff[2 * (i - 1):2 * i, 2 * (j - 1):2 * j]
            nz = any(e != 0 for e in Bx)
            n_nz += nz
            pf = sp.expand(-(Bx[0, 0] * Bx[1, 1]
                             - Bx[0, 1] * Bx[1, 0]))
            if pf != 0:
                n_sig += (int(sp.sign(pf))
                          == sign_c[frozenset({i, j})])
            if (i, j) == (a_ch, b_ch):
                Jco45 = sp.expand((Bx[0, 1] - Bx[1, 0]) / 2)
        return n_nz, n_sig, Jco45

    E1I = eval_E1(wI)
    penI = eval_pencil(wI)
    detI = eval_dets(wI)
    nzI, sigI, JcoI = census_exact(wI)
    wZ = wiring((0, 0, 0, 1), (0, 0, 0, 1))
    detZc = eval_dets(wZ)
    E1Z = eval_E1(wZ)
    penZ = eval_pencil(wZ)
    check("C5 census regression gate: pure-I passes E1 %s == 0, "
          "pencil %s == 0, dets %s > 0, census %d/10 canonical "
          "%d/10, J-coordinate %s == 1/200; V_Z passes E1/pencil "
          "(%s, %s) but fails EXACTLY orientation (dets %s == "
          "(-1, -1))"
          % (E1I, penI, detI, nzI, sigI, JcoI,
             all(e == 0 for e in E1Z), all(e == 0 for e in penZ),
             detZc),
          all(e == 0 for e in E1I) and all(e == 0 for e in penI)
          and all(d > 0 for d in detI) and nzI == 10 and sigI == 10
          and JcoI == sp.Rational(1, 200)
          and all(e == 0 for e in E1Z)
          and all(e == 0 for e in penZ)
          and all(d == -1 for d in detZc), kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    all_ok = (n_pass == n_tot) and not KILLS
    if all_ok:
        verdict = ("RP-FRAME-COVARIANT [CONJUGATION-EXACT"
                   "(theta' = g_int theta_S g_int^{-1}, both "
                   "directions; generic element = delta-circle "
                   "rotation), KERNEL-COVARIANCE-EXACT(symbolic "
                   "torus + exact Gram witnesses), DELTA-ONLY"
                   "(defect = 2t|a cos delta + c sin delta|), "
                   "EXCLUSION-IS-FRAME-STATEMENT(option 2: "
                   "fixed-Theta_S statement, not a wiring no-go), "
                   "Z-X-EXCLUSION-ORBIT-INVARIANT(det u "
                   "gauge-invariant), CANONICAL-SENTENCE-FROZEN]")
    else:
        verdict = " / ".join(sorted(set(KILLS))) or "CHECK-FAILED"
    print("  checks: %d/%d passed; kills: %s"
          % (n_pass, n_tot, KILLS if KILLS else "none"))
    print("  VERDICT: %s" % verdict)
    print("  runtime: %.1f s" % (time.time() - T0))
    print("  (constants sanity: N_fam = %s, g_car = %s)"
          % (N_fam, g_car))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
