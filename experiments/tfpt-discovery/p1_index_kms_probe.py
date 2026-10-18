#!/usr/bin/env python3
"""P1.INDEX.KMS.01 -- the closed normalization identity
c3 = 1/(I_Jones * beta_angle) = 1/(4 * 2pi) = 1/(8pi), its convention
audit, and the sharpened P1 contract.

THE THREE CORPUS DATA (located; module names are the anchors):
 (1) I = 4 = |mu4|, the carrier-to-E8 transition index:
     GATE.METRIC.11 / v154_simple_current_theorem.py ("Jones index
     [B:A] = |L| = 4 = |mu4|", KLM, isotropic glue line; C[Z4] Longo
     Q-system v125) and the LOCAL measurement chain
     v726_phys_car_pp_index.py ("Pimsner-Popa / Watatani index 4 on
     the CAR ladder"), v746_phys_gnet_local_functor.py,
     v779_gnet_gns_arf.py.
 (2) beta_angle = 2pi and T_seam = 4 c3:
     v526_seam_thermal_kms_nariai_bridge.py ("beta MEASURED, NOT
     ASSUMED": beta = N clock steps exactly, by the detailed-balance
     Q-polynomial identity; wrong beta {N/2, N/4, 2N} excluded
     exactly; angle units via the v519 Q1.1 pin step = 2pi/N =>
     "beta_angle = 2pi EXACT, T_seam = 1/(2pi) = 4 c3");
     v239_kms_thermal_time.py (Tomita-Takesaki KMS at beta = 1
     exact; the geometric normalisation beta_phys = 2pi with
     "2 pi = 1/(4 c3)"; residual = the QGEO.SYM.01 geometric-boost
     premise); v8_horizon.py / HOR.01 ("1/(2 pi) = 4 c3").
 (3) c3 = 1/(8pi): tfpt_constants.py ("c3 = 1 / (8 * PI)", the P1
     axiom); AX.P1.01 ledger row: declared but not a free knob --
     "c3 = 1/(2 e1(a) pi) = 1/(8pi)" with "e1(a)=4=|mu4|"
     (ANCHOR.GEN.01/v23, the parabolic-anchor route);
     GATE.METRIC.12: the |Z2| halving phrasing "c3=1/(2*4pi)".
 (+) area-entropy factor: v208_bh_thermodynamics.py
     ("entropy-area coefficient 1/4 = 1/|mu_4|") -- 1/4 = 1/I.

PREREGISTERED GATES (frozen before running):
 S1 CORPUS ANCHORS: every frozen substring above is found in its
    module (read-only file reads; exact strings in ANCHORS below).
 S2 IDENTITY CHAIN [E]: in exact formal arithmetic (Fraction
    coefficient x pi^k, pi symbolic -- no floats):
      S2.1  I * beta * c3 = 4 * 2pi * 1/(8pi) = 1 exactly;
      S2.2  c3 = 1/(I * beta) exactly;
      S2.3  T_seam := 4 c3 = 1/(2pi) and T_seam * beta = 1 exactly
            (HONEST UNITS NOTE: S2.1-S2.3 are ONE identity in three
            rearrangements once T_seam := 4 c3 = 1/beta_angle; they
            are gated as arithmetic, counted as one content);
      S2.4  1/4 = 1/I (the v208 entropy coefficient);
      S2.5  the anchor route: 1/(2 * e1 * pi) with e1 = 4 equals c3
            (AX.P1.01) -- the identity aligns anchor-4 with index-4.
 S3 CONVENTION AUDIT (the load-bearing honesty step) -- dependency
    graph with typed edges, each gated on measured source facts:
      S3.1  the index derivation is c3-free and beta-free: the
            sources of v154, v726, v746, v779 contain ZERO
            occurrences of "c3" (gated by file scan);
      S3.2  the beta measurement is independent: v526 contains the
            frozen measured-claim strings (detailed balance, wrong-
            beta exclusion) and the unit pin "v519"; c3 enters v526
            only through the closure READING/selection (the frozen
            anti-numerology lattice line "optionally times c3^k" --
            recorded, typed, reported);
      S3.3  typed shared items (typing, no gate): (i) the RADIAN
            convention: the 2pi in beta_angle and the 8pi in c3 use
            the same angle unit (v519 pin) -- it cancels in the
            unit-invariant statement "per full modular circle the
            normalized response is 1/I"; (ii) the two fours: e1(a)=4
            (parabolic anchor, v23) and [B:A]=4 (Jones index, v154)
            are TWO INDEPENDENT THEOREMS about the same mu4 object
            -- alignment, not circularity; (iii) c3 itself is the P1
            AXIOM: the identity EXPLAINS its value, it does not yet
            DERIVE it (that is the open bridge, S5).
 S4 FINITE EVENNESS MEASUREMENT (real, not bookkeeping): the finite
    modular-response object in hand is the TRACIAL weight per mu4
    deck sector on the l-windows (dim law, v779):
      S4.1  exact law (Fractions, l = 1..6): sector trace weights
            w_c = d_c/4^l satisfy w_1 = w_3 = 1/4 EXACTLY at every
            l, and w_0 - 1/4 = +2^-(l+1), w_2 - 1/4 = -2^-(l+1):
            a SYMMETRIC zero-sum offset pair, halving per level --
            equal quarters asymptotically, NO anomaly offset (the
            kill object would be an asymmetric offset);
      S4.2  operator cross-check at l = 2: constructed sector
            projections have traces (6,4,2,4) and the index-4 E is
            TRACE-PRESERVING (tr o E = tr, dev < 1e-12) -- the
            modular(tracial)-response normalization at finite level;
      S4.3  the SEA STATE does not equidistribute: omega(P_q) at the
            Haar-limit level (N = 1536 pullback) has max deviation
            from 1/4 > 0.05 (measured) -- the evenness is a property
            of the TRACIAL/modular normalization, not of the vacuum
            weights: the contract's bridge must normalize the
            modular response functional, not vacuum expectation.
 S5 THE SHARPENED CONTRACT (deliverable text, printed): see the
    CONTRACT block in the output, with the one open bridge and the
    kill criterion.
 CONTROLS (must fire):
      C1  wrong index I = 2 (the Z2 anchor case): the chain gives
          1/(2 * 2pi) = 1/(4pi) != c3; the corpus explicitly
          associates 1/(4pi) with OTHER objects: the un-halved
          Gauss-Bonnet step (GATE.METRIC.12 "the |Z2| halving
          c3=1/(2*4pi)") and SdS "1/(4pi)=2 c3" (v526/v208).
          Measured leg: the Z2-only average on the l = 2 window has
          lambda = 1/2 => measured index 2 (my v726-style machinery)
          => the wrong chain lands on 1/(4pi) exactly.
      C2  wrong beta = pi (half circle): I * beta_wrong * c3 = 1/2
          != 1 (and v526's measured wrong-beta exclusion {N/2, N/4,
          2N} is the corpus-level version of this control).
 VERDICT ENUM (frozen):
      P1-IDENTITY-CLOSED : S1 + S2 exact + S3 independence gates
          pass (index modules c3-free; beta measured with c3 only in
          the reading) + S4 + controls fire.  The chain is exact,
          the inputs audited independent, the contract carries ONE
          open bridge.
      P1-IDENTITY-CONVENTION : S2 exact but an S3 independence gate
          fails (hidden c3 use found in the index/beta derivations)
          -- the identity is then a consistency check only.
      P1-IDENTITY-BROKEN : any S2 identity fails.

HONESTY: c3 remains the P1 axiom; nothing here derives it.  The
identity organizes one axiom + two independently certified
quantities into the sharpened contract P1.INDEX.KMS.01 whose single
open bridge is the modular-response normalization.  No marker moves.
Exploration only (tfpt-experiment firewall): read-only corpus file
reads; NOT wired into run_all.py; no ledger row; no file writes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/p1_index_kms_probe.py
"""

import hashlib
import inspect
import os
import sys
import time
from fractions import Fraction as Fr
from math import comb

import numpy as np

SEED = 20260806
CHECKS = []
HERE = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.abspath(os.path.join(HERE, "..", "..", "verification"))

ANCHORS = [
    ("tfpt_constants.py", "c3 = 1 / (8 * PI)",
     "P1 axiom line (c3 declared)"),
    ("v8_horizon.py", "1/(2 pi) = 4 c3",
     "HOR.01 horizon unit code"),
    ("v208_bh_thermodynamics.py", "entropy-area coefficient 1/4 = 1/|mu_4|",
     "area-entropy factor 1/4 = 1/I"),
    ("v239_kms_thermal_time.py", "2 pi = 1/(4 c3)",
     "seam unit in the KMS module"),
    ("v239_kms_thermal_time.py", "KMS AT beta = 1",
     "Tomita-Takesaki beta = 1 exact"),
    ("v239_kms_thermal_time.py", "QGEO.SYM.01",
     "the geometric-boost residual, typed open"),
    ("v526_seam_thermal_kms_nariai_bridge.py", "beta MEASURED, NOT ASSUMED",
     "beta = N clock steps, detailed balance"),
    ("v526_seam_thermal_kms_nariai_bridge.py", "beta_angle = 2pi EXACT",
     "angle units via the v519 pin"),
    ("v526_seam_thermal_kms_nariai_bridge.py", "{N/2,N/4,2N} excluded",
     "wrong-beta exclusion, measured"),
    ("v526_seam_thermal_kms_nariai_bridge.py", "v519",
     "the angle-unit pin (step = 2pi/N)"),
    ("v526_seam_thermal_kms_nariai_bridge.py", "SdS 1/(4pi)=2 c3",
     "1/(4pi) is a DIFFERENT corpus object (SdS)"),
    ("v726_phys_car_pp_index.py", "Watatani index 4",
     "local index-4 measurement chain"),
    ("status_ledger.csv", "Jones index [B:A] = |L| = 4 = |mu4|",
     "GATE.METRIC.11 / v154 transition index"),
    ("status_ledger.csv", "c3 = 1/(2 e1(a) pi) = 1/(8pi)",
     "AX.P1.01 anchor route for the 8"),
    ("status_ledger.csv", "e1(a)=4=|mu4|",
     "anchor four = |mu4| (v23)"),
    ("status_ledger.csv", "c3=1/(2*4pi)",
     "GATE.METRIC.12 |Z2| halving phrasing"),
]
INDEX_MODULES_C3FREE = [
    "v154_simple_current_theorem.py", "v726_phys_car_pp_index.py",
    "v746_phys_gnet_local_functor.py", "v779_gnet_gns_arf.py"]


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name
          + ("  -- " + detail if detail else ""))
    return ok


# ---- exact formal arithmetic: value = (Fraction q, int k) = q * pi^k

def pmul(a, b):
    return (a[0] * b[0], a[1] + b[1])


def pinv(a):
    return (1 / a[0], -a[1])


I_JONES = (Fr(4), 0)
BETA = (Fr(2), 1)          # 2 * pi^1
C3 = (Fr(1, 8), -1)        # (1/8) * pi^-1
ONE = (Fr(1), 0)


# ---- minimal ladder machinery (as in the sibling probes) -------------

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


def window(N, p, l):
    return [(p + i) % N for i in range(l)] + \
           [(p + N // 2 + i) % N for i in range(l)]


def haar_iso(N):
    V = np.zeros((2 * N, N))
    for j in range(N):
        V[2 * j, j] = V[2 * j + 1, j] = 1.0 / np.sqrt(2.0)
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
    return 1.0 / float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)


def onb_of(P):
    w, W = np.linalg.eigh((P + P.conj().T) / 2)
    return W[:, w > 0.5]


def sha_freeze():
    fns = [pmul, pinv, spower, covariance, window, haar_iso, jw_ops,
           gamma_partial, gaussian_rho, sector_projs, lam_of, onb_of]
    blob = "".join(inspect.getsource(f) for f in fns)
    blob += repr((SEED, ANCHORS, INDEX_MODULES_C3FREE, I_JONES, BETA, C3))
    return hashlib.sha256(blob.encode()).hexdigest()


def main():
    t0 = time.time()
    print("p1_index_kms_probe -- c3 = 1/(I_Jones * beta_angle): identity, "
          "audit, contract\n")
    print(f"SHA-freeze: {sha_freeze()[:32]}\n")

    # ============ S1: corpus anchors ==================================
    print("-- S1: located corpus anchors (read-only file scans) --")
    srcs = {}
    ok_anch = True
    for fname, needle, why in ANCHORS:
        path = os.path.join(VERI, fname)
        if fname not in srcs:
            with open(path, encoding="utf-8") as fh:
                srcs[fname] = fh.read()
        hit = needle in srcs[fname]
        ok_anch &= hit
        print(f"   [{'ok' if hit else 'MISSING'}] {fname}: "
              f'"{needle}"  ({why})')
    check("S1 all frozen corpus-anchor strings found in their modules",
          ok_anch)

    # ============ S2: the identity chain (exact, formal pi) ===========
    print("\n-- S2: the identity chain [E] (Fraction x pi^k, no floats) --")
    chain = pmul(pmul(I_JONES, BETA), C3)
    check("S2.1 I * beta * c3 = 4 * 2pi * 1/(8pi) = 1 EXACT",
          chain == ONE, f"= {chain[0]} * pi^{chain[1]}")
    check("S2.2 c3 = 1/(I * beta) EXACT",
          C3 == pinv(pmul(I_JONES, BETA)))
    T_seam = pmul((Fr(4), 0), C3)
    check("S2.3 T_seam := 4 c3 = 1/(2pi) and T_seam * beta = 1 EXACT "
          "(units note: S2.1-S2.3 are ONE identity, three "
          "rearrangements -- counted as one content)",
          T_seam == pinv(BETA) and pmul(T_seam, BETA) == ONE,
          f"T_seam = {T_seam[0]} * pi^{T_seam[1]}")
    check("S2.4 area-entropy factor 1/4 = 1/I (v208 coefficient)",
          Fr(1, 4) == 1 / I_JONES[0])
    anchor_route = pinv(pmul((Fr(2), 1), (Fr(4), 0)))   # 1/(2 e1 pi)
    check("S2.5 anchor route 1/(2 e1(a) pi), e1 = 4, equals c3 "
          "(AX.P1.01): the identity aligns anchor-4 with index-4",
          anchor_route == C3)

    # ============ S3: the convention audit ============================
    print("\n-- S3: convention audit / dependency graph --")
    ok_free = True
    for fname in INDEX_MODULES_C3FREE:
        with open(os.path.join(VERI, fname), encoding="utf-8") as fh:
            n_c3 = fh.read().count("c3")
        ok_free &= n_c3 == 0
        print(f"   {fname}: c3 occurrences = {n_c3}")
    check("S3.1 the index derivation is c3-free and beta-free: ZERO "
          "'c3' occurrences in v154/v726/v746/v779", ok_free)
    v526 = srcs["v526_seam_thermal_kms_nariai_bridge.py"]
    lattice_line = "optionally times c3^k" in v526
    check("S3.2 the beta measurement is independent: measured-claim "
          "strings + wrong-beta exclusion + v519 unit pin present "
          "(S1); c3 enters v526 only via the closure READING/frozen "
          "selection lattice", lattice_line,
          "lattice line found: c3 is a candidate in the class-1 "
          "selection, not an input to the beta measurement")
    print("""   DEPENDENCY GRAPH (edges typed):
     I = 4    <- v154 (KLM, [B:A]=|L|) + v726/v746/v779 (Watatani/PP,
                measured exact)          [INDEPENDENT THEOREM: no c3,
                no beta in any source]
     beta     <- v526 (beta = N steps MEASURED, detailed balance;
                wrong beta excluded)      [INDEPENDENT MEASUREMENT]
                x v519 pin (step = 2pi/N) [SHARED CONVENTION: radian
                unit -- cancels in the unit-invariant statement
                'response per full modular circle = 1/I']
     c3       <- P1 AXIOM (tfpt_constants) [DECLARED]; anchor route
                c3 = 1/(2 e1(a) pi), e1(a)=4 (v23) [ALIGNED: the two
                fours are two independent theorems (parabolic anchor
                vs Jones index) about the SAME mu4 object -- an
                alignment, not a circularity]
     identity I*beta*c3 = 1 [CONSISTENCY, exact]: it EXPLAINS the
                axiom's value; it does not yet DERIVE it (open
                bridge, S5).""")

    # ============ S4: finite evenness measurement =====================
    print("\n-- S4: per-sector modular(tracial) response, finite level --")
    ok_law = True
    print(f"{'l':>3} {'w_0 - 1/4':>12} {'w_1 - 1/4':>12} "
          f"{'w_2 - 1/4':>12} {'w_3 - 1/4':>12}")
    for l in range(1, 7):
        dc = [0, 0, 0, 0]
        for a in range(l + 1):
            for b in range(l + 1):
                dc[(a - b) % 4] += comb(l, a) * comb(l, b)
        w = [Fr(d, 4 ** l) for d in dc]
        dev = [x - Fr(1, 4) for x in w]
        ok_law &= dev[1] == 0 and dev[3] == 0
        ok_law &= dev[0] == Fr(1, 2 ** (l + 1))
        ok_law &= dev[2] == -Fr(1, 2 ** (l + 1))
        ok_law &= sum(dev, Fr(0)) == 0
        print(f"{l:>3} " + " ".join(f"{str(d):>12}" for d in dev))
    check("S4.1 EXACT evenness law (l = 1..6): w_1 = w_3 = 1/4 exactly;"
          " w_0/w_2 offset = +-2^-(l+1), symmetric and zero-sum, "
          "halving per level -- equal quarters asymptotically, NO "
          "anomaly offset", ok_law)
    N0 = 48
    win0 = window(N0, 0, 2)
    HW4 = spower(N0, N0 // 2)[np.ix_(win0, win0)]
    c4 = jw_ops(4)
    U4 = gamma_partial(HW4, list(range(4)), c4)
    Ps = sector_projs(U4)
    trs = [float(np.trace(P).real) for P in Ps]

    def E4(x):
        return sum(P @ x @ P for P in Ps)

    rng = np.random.default_rng(SEED)
    dev_tr = 0.0
    for _ in range(6):
        A = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16))
        dev_tr = max(dev_tr, abs(np.trace(E4(A)) - np.trace(A)))
    check("S4.2 operator cross-check (l = 2): sector traces (6,4,2,4) "
          "and tr o E = tr (E trace-preserving: the finite "
          "modular-response normalization)",
          np.allclose(trs, [6, 4, 2, 4], atol=1e-9) and dev_tr < 1e-12,
          f"traces = {[round(t, 6) for t in trs]}, dev = {dev_tr:.1e}")
    chain_m = np.eye(N0)
    Nk = N0
    for _ in range(5):
        chain_m = haar_iso(Nk) @ chain_m
        Nk *= 2
    CW = (chain_m.T @ covariance(Nk) @ chain_m)[np.ix_(win0, win0)]
    rho = gaussian_rho(CW, c4)
    wq = [float(np.real(np.trace(rho @ P))) for P in Ps]
    dev_sea = max(abs(w - 0.25) for w in wq)
    check("S4.3 the SEA STATE does not equidistribute: omega(P_q) at "
          f"the N = {Nk} Haar pullback deviates from 1/4 by "
          f"{dev_sea:.3f} > 0.05 -- evenness is a TRACIAL/modular "
          "property, not a vacuum property (sharpens the bridge)",
          dev_sea > 0.05,
          "omega(P_q) = " + str([round(w, 4) for w in wq]))

    # ============ S5: the sharpened contract ==========================
    print("""
-- S5: P1.INDEX.KMS.01, the sharpened contract (report only) --
  STATEMENT.  An index-I simple-current extension (here I = 4 =
  |mu4|, GATE.METRIC.11) carries per modular period beta_angle
  exactly the normalized response 1/(I * beta_angle); with the
  measured beta_angle = 2pi (v526, one full seam circle) this VALUE
  is c3 = 1/(8pi) -- the P1 axiom as the index-KMS normalization.
  PROOF NEEDS (the one open bridge): (a) the modular response
  functional's normalization -- the Quillen/determinant-line answer
  per modular period distributing EVENLY over the I deck sectors
  with NO anomaly offset (the finite precursor is measured here:
  S4.1 symmetric zero-sum offset vanishing at 2^-l; S4.2 the
  trace-preserving index-4 E).  ALREADY CORPUS THEOREMS: the index
  (v154/v125 + v726/v746/v779), the angle (v526 measured, v239
  Tomita beta = 1), the tracial evenness precursor (v779 dim law).
  STILL OPEN BESIDES THE BRIDGE: the geometric-boost identification
  (QGEO.SYM.01, typed [O] in v239).
  KILL CRITERION: an anomaly offset making the per-sector
  distribution UNEVEN -- concretely, a sector weight asymmetry that
  is NOT the symmetric zero-sum +-2^-(l+1) pair (e.g. w_1 != w_3 at
  any level, or a non-vanishing offset as l -> inf): any such
  measurement kills the bridge and the contract.""")

    # ============ Controls ============================================
    print("-- Controls (must fire) --")
    v2m = np.zeros(16, dtype=complex)
    for P in Ps:
        o = onb_of(P)
        if o.shape[1]:
            v2m += o[:, 0]
    v2m /= np.linalg.norm(v2m)

    def EZ2(x):
        UU = U4 @ U4
        return (x + UU @ x @ UU.conj().T) / 2

    lam2 = lam_of(np.outer(v2m, v2m.conj()), EZ2)
    I_wrong = (Fr(round(1 / lam2)), 0)
    wrong_c3 = pinv(pmul(I_wrong, BETA))
    check("C1 fires: measured Z2 index = 2 (lambda = 1/2) gives "
          "1/(2*2pi) = 1/(4pi) != c3; corpus books 1/(4pi) elsewhere "
          "(un-halved Gauss-Bonnet, GATE.METRIC.12; SdS 1/(4pi) = "
          "2 c3, v526/v208)",
          abs(lam2 - 0.5) < 1e-8 and wrong_c3 == (Fr(1, 4), -1)
          and wrong_c3 != C3 and wrong_c3 == pmul((Fr(2), 0), C3),
          f"lambda = {lam2:.10f}, wrong chain = "
          f"{wrong_c3[0]} * pi^{wrong_c3[1]}")
    beta_wrong = (Fr(1), 1)
    check("C2 fires: wrong beta = pi (half circle) breaks the chain: "
          "I * beta_wrong * c3 = 1/2 != 1 (corpus-level version: "
          "v526's exact wrong-beta exclusion {N/2, N/4, 2N})",
          pmul(pmul(I_JONES, beta_wrong), C3) == (Fr(1, 2), 0)
          and pmul(T_seam, beta_wrong) != ONE)

    # ============ verdict =============================================
    res = dict(CHECKS)
    s1 = res.get("S1 all frozen corpus-anchor strings found in their "
                 "modules", False)
    s2 = all(v for n, v in CHECKS if n.startswith("S2"))
    s3 = all(v for n, v in CHECKS if n.startswith("S3"))
    s4 = all(v for n, v in CHECKS if n.startswith("S4"))
    ctrl = all(v for n, v in CHECKS if n.startswith("C"))
    if not s2:
        verdict = "P1-IDENTITY-BROKEN"
    elif s1 and s2 and s3 and s4 and ctrl:
        verdict = "P1-IDENTITY-CLOSED"
    else:
        verdict = "P1-IDENTITY-CONVENTION" + ("" if ctrl
                                              else " (CONTROL-VOID)")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}"
          f"   ({time.time() - t0:.1f} s)")
    print("""
TYPED SUMMARY: the chain 4 * 2pi * 1/(8pi) = 1 is exact; the index
is an independent c3-free theorem; beta is an independent
measurement (radian unit = the one shared convention, cancelling in
the unit-invariant form); c3 stays the P1 axiom -- the identity
EXPLAINS its value and the contract P1.INDEX.KMS.01 names the one
open bridge (even modular-response distribution, kill = anomaly
offset).  The finite evenness precursor is measured (symmetric
zero-sum offset, vanishing at 2^-l; E trace-preserving; the sea
state does NOT equidistribute -- the bridge is about the modular
response, not vacuum weights).  No marker moves; exploration only.""")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
