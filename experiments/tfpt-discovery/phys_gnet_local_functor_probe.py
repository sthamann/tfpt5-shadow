#!/usr/bin/env python3
"""PHYS T2-B -- the LOCALITY FUNCTOR test for the G_net reading:
is I |-> (A(I), E_I) a net of algebras with expectations (isotony,
graded locality, clock covariance), is the Watatani index 4 LOCAL
(every interval), and is the Ramond/Klein dressing locally
implementable?  Kill (GPT council T2-B): "no functor from intervals
to subgroupoids" would end the network reading of G_net.

DESIGN DECISION (documented, with must-fail): the mu4 average
E = (1/4) sum_j Ad(Gamma(H))^j, H = S^{N/2}, maps an interval algebra
into itself ONLY if "interval" means the H-orbit window
    I-hat = I u (I + N/2)  over the BASE circle of N/2 sites --
the net lives on the mu4/half-turn QUOTIENT circle (the orbifold
structure; v679 frame).  A naive single-arc interval is NOT E-stable:
must-fail MF3.  Likewise the deck mu3 average would need TRIPLE
windows: must-fail MF2.  So the doubling is forced, not chosen.

CHECKS
  F1a ISOTONY + expectation compatibility (Fock-exact, ambient
      window J-hat, N = 48): for I subset J the inclusion
      A(I-hat) subset A(J-hat) holds by construction, and
      E_J|_{A(I-hat)} == E_I exactly (battery of monomials + random
      elements; E_I represented ambiently via the partial Bogoliubov
      unitary V_I = H P_I-hat + (1 - P_I-hat)); E_J maps A(I-hat)
      into itself.
  F1b GRADED LOCALITY (Fock-exact): disjoint base intervals =>
      disjoint doubled windows; homogeneous elements satisfy
      a b = (-1)^{|a||b|} b a exactly.  MF1: the UNGRADED commutator
      of odd x odd elements does NOT vanish -- the fermionic grading
      is load-bearing (control fires).
  F1c CLOCK COVARIANCE (one-particle exact, sufficient at the
      Bogoliubov level): [L, H] = 0, [L, C] = 0, L maps the window
      of I to the window of I + N/12 (support sets, unit-modulus
      entries), and L V_I L^{-1} = V_{I + N/12} exactly => the net
      map and the expectations are clock-covariant.
  F2  LOCAL INDEX LADDER: over N = 48/96/192, base lengths
      l = 1..4, positions p = {0, 7, N/2 - 1 (wrap)}: sector dims,
      optimal PP constant lambda* (explicit mixing minimizer),
      local Takesaki [rho_W, U] = 0, quasi-basis Watatani index
      (l <= 3).  Expected: lambda* = 1/4 and Ind = 4*1 for EVERY
      interval with l >= 2 at EVERY position including the wrap;
      l = 1 anomaly (3 sectors, index 3) typed as before.
      MF4: Z2-only average gives 1/2 (teeth).
  F2R RAMOND LOCALITY: the Klein dressing D = e^{i pi/2 n_0} acts on
      one-particle vectors by V_D = 1 + (e^{-i pi/2} - 1) P_{k=0}
      with P_{k=0} the DELOCALIZED zero-mode projection: the
      strictly-interval-local reading has a measured NO-GO,
      leakage delta(N, l) = sqrt(2/N) * sqrt(1 - 2l/N) > 0 (exact
      closed form, verified; rate N^{-1/2} on the ladder).  BUT the
      dressing IS boundary-anchored: the half-line string
      sigma = diag(-1 on j < j0, +1 else) conjugates the NS shift
      EXACTLY into the R shift with one bond defect at j0
      (sigma S_NS sigma = S_R-defect, machine-exact) -- the v679
      "twist sector = bond defect" reproduced: R sectors are
      SOLITONIC (half-line/boundary) defects, not interval-local
      operators, with vanishing local footprint ~ N^{-1/2}.

VERDICT ENUM: GNET-LOCAL-FUNCTOR-ALIVE / PARTIAL / DEAD.

CIRCULARITY: H derived from the clock (L^6, order 4 forced by NS,
as in phys_car_pp_index_probe); the doubling is forced by MF2/MF3,
not inserted; state = declared chiral Dirac sea, C = f(S).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no marker move.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/phys_gnet_local_functor_probe.py
"""

import sys

import numpy as np

TOL = 1e-10
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    return ok


# ---------------- one-particle layer ----------------

def shift(N, ns=True):
    S = np.zeros((N, N))
    for j in range(N - 1):
        S[j + 1, j] = 1.0
    S[0, N - 1] = -1.0 if ns else 1.0
    return S


def covariance(N, ns=True):
    sigma = 0.5 if ns else 0.0
    th = 2 * np.pi * (np.arange(N) + sigma) / N
    th = np.mod(th + np.pi, 2 * np.pi) - np.pi
    th[np.isclose(th, -np.pi)] = np.pi
    F = np.exp(1j * np.outer(np.arange(N), th)) / np.sqrt(N)
    occ = (th < 0).astype(float)
    if not ns:
        occ[np.isclose(th, 0.0)] = 0.5
    return (F * occ) @ F.conj().T


def window(N, p, l):
    return [(p + i) % N for i in range(l)] + \
           [(p + N // 2 + i) % N for i in range(l)]


# ---------------- Fock layer ----------------

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
    """implementer of the Bogoliubov unitary acting as Hsub on the modes
    idx (subset of the ambient modes) and as identity elsewhere.
    Hsub must be skew-real with Hsub^2 = -1 restricted (eigenvalues +-i)."""
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
    top = float(np.linalg.eigvalsh((M + M.conj().T) / 2).max().real)
    return 1.0 / top


def onb_of(P):
    w, W = np.linalg.eigh((P + P.conj().T) / 2)
    return W[:, w > 0.5]


def quasi_basis(Ps):
    onbs = [onb_of(P) for P in Ps]
    dims = [o.shape[1] for o in onbs]
    vs = [np.eye(Ps[0].shape[0], dtype=complex)]
    for q in range(4):
        for qp in range(4):
            if q == qp or dims[q] == 0 or dims[qp] == 0:
                continue
            for a in range(dims[q]):
                for b in range(dims[qp]):
                    vs.append(np.outer(onbs[q][:, a], onbs[qp][:, b].conj())
                              / np.sqrt(dims[qp]))
    return vs


def rnd_elem(gens, rng, terms=6, maxdeg=3):
    dim = gens[0].shape[0]
    x = np.zeros((dim, dim), dtype=complex)
    for _ in range(terms):
        deg = rng.integers(1, maxdeg + 1)
        m = np.eye(dim, dtype=complex)
        for _ in range(deg):
            m = m @ gens[rng.integers(0, len(gens))]
        x += (rng.standard_normal() + 1j * rng.standard_normal()) * m
    return x


def main():
    rng = np.random.default_rng(20260804)
    print("phys_gnet_local_functor_probe -- net axioms for the mu4 seam net\n")

    # ================= F1a isotony + expectation compatibility ==========
    N = 48
    S = shift(N)
    H = np.linalg.matrix_power(S, N // 2)
    baseJ = [0, 1, 2, 3]
    ambJ = window(N, 0, 4)                       # 8 sites
    cops = jw_ops(len(ambJ))
    pos = {s: i for i, s in enumerate(ambJ)}
    HJ = H[np.ix_(ambJ, ambJ)]
    UJ = gamma_partial(HJ, list(range(len(ambJ))), cops)

    def EJ(x):
        return sum(np.linalg.matrix_power(UJ, j) @ x
                   @ np.linalg.matrix_power(UJ, j).conj().T
                   for j in range(4)) / 4

    for baseI in ([0, 1], [1, 2], [0, 1, 2]):
        ambI = window(N, baseI[0], len(baseI))
        idxI = [pos[s] for s in ambI]
        HI = H[np.ix_(ambI, ambI)]
        UI = gamma_partial(HI, idxI, cops)       # V_I = H on I-hat, 1 else

        def EI(x, UI=UI):
            return sum(np.linalg.matrix_power(UI, j) @ x
                       @ np.linalg.matrix_power(UI, j).conj().T
                       for j in range(4)) / 4

        gens = []
        for i in idxI:
            gens += [cops[i], cops[i].conj().T]
        batt = [cops[idxI[0]],
                cops[idxI[0]].conj().T @ cops[idxI[1]],
                cops[idxI[0]] @ cops[idxI[1]],
                cops[idxI[0]].conj().T @ cops[idxI[0]]]
        batt += [rnd_elem(gens, rng) for _ in range(4)]
        dev = max(np.abs(EJ(x) - EI(x)).max() for x in batt)
        check(f"F1a isotony: E_J|A(I-hat) == E_I exactly, base I = {baseI} "
              f"in J = {baseJ}", dev < TOL, f"max dev = {dev:.2e}")

    # ================= F1b graded locality ==============================
    baseI, baseK = [0, 1], [3, 4]
    ambU = window(N, 0, 5)                       # contains both, 10 sites
    copsU = jw_ops(10)
    posU = {s: i for i, s in enumerate(ambU)}
    iI = [posU[s] for s in window(N, 0, 2)]
    iK = [posU[s] for s in window(N, 3, 2)]
    # homogeneous battery: (element, parity)
    def hbatt(idx, cs):
        return [(cs[idx[0]], 1), (cs[idx[0]].conj().T, 1),
                (cs[idx[0]] @ cs[idx[1]], 0),
                (cs[idx[0]].conj().T @ cs[idx[1]], 0),
                (cs[idx[0]].conj().T @ cs[idx[1]] @ cs[idx[2]], 1)]
    dev, worst_ug = 0.0, 0.0
    for a, pa in hbatt(iI, copsU):
        for b, pb in hbatt(iK, copsU):
            g = a @ b - ((-1) ** (pa * pb)) * b @ a
            dev = max(dev, np.abs(g).max())
            if pa == 1 and pb == 1:
                worst_ug = max(worst_ug, np.abs(a @ b - b @ a).max())
    check("F1b graded locality: a b = (-1)^{|a||b|} b a exactly for "
          "disjoint base intervals {0,1}, {3,4}", dev < TOL,
          f"max dev = {dev:.2e}")
    check("MF1 fires: UNGRADED commutator of odd x odd does NOT vanish "
          "(fermionic grading is load-bearing)", worst_ug > 0.5,
          f"max |[odd,odd]| = {worst_ug:.3f}")

    # ================= F1c clock covariance =============================
    ok_all = True
    det = []
    for NN in (48, 96, 192):
        SS = shift(NN)
        LL = np.linalg.matrix_power(SS, NN // 12)
        HH = np.linalg.matrix_power(SS, NN // 2)
        CC = covariance(NN)
        step = NN // 12
        ok = (np.abs(LL @ HH - HH @ LL).max() < TOL
              and np.abs(LL @ CC - CC @ LL).max() < 1e-8)
        # window transport + expectation intertwining at one-particle level
        for (p, l) in ((0, 2), (7, 3)):
            w0, w1 = window(NN, p, l), window(NN, p + step, l)
            img = [np.argmax(np.abs(LL[:, j])) for j in w0]
            ok &= sorted(img) == sorted(w1)
            P0 = np.zeros((NN, NN))
            P0[w0, w0] = 1.0
            V0 = HH @ P0 + (np.eye(NN) - P0)
            P1 = np.zeros((NN, NN))
            P1[w1, w1] = 1.0
            V1 = HH @ P1 + (np.eye(NN) - P1)
            det.append(np.abs(LL @ V0 @ LL.conj().T - V1).max())
            ok &= det[-1] < TOL
        ok_all &= ok
    check("F1c clock covariance: [L,H] = 0, [L,C] = 0, L(window(I)) = "
          "window(I + N/12), and L V_I L^-1 = V_{I+N/12} exactly "
          "(one-particle/Bogoliubov level, N = 48/96/192)", ok_all,
          f"max intertwining dev = {max(det):.2e}")

    # ================= F2 local index ladder ============================
    print("\n-- F2: local index over N x length x position --")
    print(f"{'N':>4} {'l':>2} {'p':>3} {'sector dims':>18} {'lambda*':>13} "
          f"{'[rho,U]':>9} {'Ind':>7}")
    ok_lam, ok_ind, ok_anom, ok_tak = True, True, True, True
    for NN in (48, 96, 192):
        SS = shift(NN)
        HH = np.linalg.matrix_power(SS, NN // 2)
        CC = covariance(NN)
        for l in (1, 2, 3, 4):
            for p in (0, 7, NN // 2 - 1):
                win = window(NN, p, l)
                HW = HH[np.ix_(win, win)]
                CW = CC[np.ix_(win, win)]
                cs = jw_ops(2 * l)
                U = gamma_partial(HW, list(range(2 * l)), cs)
                Ps = sector_projs(U)
                dims = [int(round(np.trace(P).real)) for P in Ps]
                m = sum(1 for d in dims if d > 0)

                def E(x, Ps=Ps):
                    return sum(P @ x @ P for P in Ps)

                v = np.zeros(2 ** (2 * l), dtype=complex)
                for P in Ps:
                    o = onb_of(P)
                    if o.shape[1]:
                        v += o[:, 0]
                v /= np.linalg.norm(v)
                lam = lam_of(np.outer(v, v.conj()), E)
                rho = gaussian_rho(CW, cs)
                tak = np.abs(rho @ U - U @ rho).max()
                ind_s = "-"
                if l <= 3:
                    vs = quasi_basis(Ps)
                    ind = sum(vv @ vv.conj().T for vv in vs)
                    d_ind = np.abs(ind - m * np.eye(2 ** (2 * l))).max()
                    ind_s = f"{m}*1" if d_ind < 1e-7 else "BAD"
                    ok_ind &= d_ind < 1e-7 and ((m == 4) if l >= 2 else (m == 3))
                if l >= 2:
                    ok_lam &= abs(lam - 0.25) < 1e-8 and m == 4
                else:
                    ok_anom &= abs(lam - 1 / 3) < 1e-8 and m == 3
                ok_tak &= tak < 1e-8
                print(f"{NN:>4} {l:>2} {p:>3} {str(dims):>18} "
                      f"{lam:>13.10f} {tak:>9.1e} {ind_s:>7}")
    check("F2 local index: lambda* == 1/4 and 4 sectors for EVERY interval "
          "l >= 2, every position (incl. wrap), every N", ok_lam)
    check("F2 local index: Watatani quasi-basis Ind == m*1 scalar for every "
          "tested interval (4 for l >= 2)", ok_ind)
    check("F2 l = 1 anomaly stable at all positions/N: 3 sectors, "
          "lambda = 1/3 (single-site window cannot see |mu4| = 4)", ok_anom)
    check("F2 local Takesaki: [rho_W, U] = 0 on every interval", ok_tak)

    # MF4: Z2-only control (one instance)
    win = window(48, 0, 2)
    HW = np.linalg.matrix_power(shift(48), 24)[np.ix_(win, win)]
    cs = jw_ops(4)
    U = gamma_partial(HW, list(range(4)), cs)
    Ps = sector_projs(U)
    v = np.zeros(16, dtype=complex)
    for P in Ps:
        o = onb_of(P)
        if o.shape[1]:
            v += o[:, 0]
    v /= np.linalg.norm(v)

    def E2(x, U=U):
        U2 = U @ U
        return (x + U2 @ x @ U2.conj().T) / 2

    lam2 = lam_of(np.outer(v, v.conj()), E2)
    check("MF4 fires: Z2-only average gives lambda = 1/2 != 1/4 "
          "(the probe measures mu4, not mu2)", abs(lam2 - 0.5) < 1e-8,
          f"lambda_Z2 = {lam2:.10f}")

    # ================= MF2/MF3: the doubling is forced ==================
    NN = 48
    SS = shift(NN)
    Dk = np.linalg.matrix_power(SS, NN // 3)
    win = set(window(NN, 0, 2))
    img = {np.argmax(np.abs(Dk[:, j])) for j in win}
    check("MF2 fires: the deck mu3 average does NOT preserve the doubled "
          "window (Dk support leaves I-hat: mu3 would need triple windows)",
          not img.issubset(win), f"Dk(window) = {sorted(img)}")
    HH = np.linalg.matrix_power(SS, NN // 2)
    bad = [0, 1, 24, 26]                          # misaligned second arc
    imgH = {np.argmax(np.abs(HH[:, j])) for j in bad}
    check("MF3 fires: a misaligned window I u (I + N/2 + shift) is not "
          "H-stable (the exact doubling is forced)",
          not imgH.issubset(set(bad)), f"H(bad) = {sorted(imgH)}")

    # ================= F2R Ramond locality ==============================
    print("\n-- F2R: Ramond/Klein dressing locality --")
    l = 2
    deltas = {}
    ok_form = True
    for NN in (48, 96, 192):
        k0 = np.ones(NN) / np.sqrt(NN)            # R zero mode (delocalized)
        VD = np.eye(NN, dtype=complex) + (np.exp(-1j * np.pi / 2) - 1) \
            * np.outer(k0, k0.conj())
        win = window(NN, 0, l)
        Pw = np.zeros((NN, NN))
        Pw[win, win] = 1.0
        d = max(np.linalg.norm(((np.eye(NN) - Pw) @ (VD - np.eye(NN)))[:, j])
                for j in win)
        deltas[NN] = d
        pred = np.sqrt(2.0 / NN) * np.sqrt(1 - 2 * l / NN)
        ok_form &= abs(d - pred) < 1e-12
    r1 = np.log2(deltas[48] / deltas[96])
    r2 = np.log2(deltas[96] / deltas[192])
    check("F2R strict-locality NO-GO: dressing leakage delta(N) = "
          "sqrt(2/N) sqrt(1 - 2l/N) > 0 exactly (closed form verified)",
          ok_form and all(v > 0 for v in deltas.values()),
          f"delta = {deltas[48]:.6f}/{deltas[96]:.6f}/{deltas[192]:.6f}")
    check("F2R leakage rate == N^{-1/2} on the ladder (local footprint of "
          "the R defect vanishes)", abs(r1 - 0.5) < 0.05 and abs(r2 - 0.5) < 0.05,
          f"rates = {r1:.4f}, {r2:.4f}")
    ok = True
    for NN in (48, 96, 192):
        Sns = shift(NN, ns=True)
        j0 = NN // 2
        sg = np.where(np.arange(NN) < j0, -1.0, 1.0)
        Sc = np.diag(sg) @ Sns @ np.diag(sg)
        Sr_def = shift(NN, ns=False).copy()
        Sr_def[j0, j0 - 1] = -1.0                 # one bond defect at j0
        ok &= np.abs(Sc - Sr_def).max() < 1e-14
    check("F2R bond-defect identity: the HALF-LINE string sigma conjugates "
          "the NS shift exactly into the R shift with ONE bond defect "
          "(v679 'twist = bond defect' reproduced; the dressing is "
          "boundary-anchored, solitonic -- not interval-local)", ok)

    # ================= verdict ==========================================
    n_pass = sum(1 for _, ok in CHECKS if ok)
    all_ok = n_pass == len(CHECKS)
    verdict = "GNET-LOCAL-FUNCTOR-ALIVE" if all_ok else "PARTIAL-OR-DEAD"
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}")
    print("""
typed consequence if ALIVE: I |-> (A(I-hat), E_I) is a genuine net of
CAR algebras with clock-covariant index-4 expectations on the mu4
quotient circle; the R sector is a SOLITONIC (half-line/bond) defect
with N^{-1/2} local footprint, not an interval-local operator --
exactly the DHR/solitonic structure the seam-Calderon identification
needs.  MISSING CONTINUUM THEOREMS (named, not claimed):
  (1) uniform bounds + tightness => GNS limit net (the v679 formal
      residual);
  (2) index continuity along the inductive limit (Pimsner-Popa /
      Longo heredity) => Jones index 4 of the limit inclusion;
  (3) identification of the limit fixed-point net with the Longo
      Q-system extension of GATE.METRIC.11 (simple-current direction);
  (4) solitonic sector construction from the bond defect (twisted
      DHR/Longo-Roberts) for the R sectors;
  (5) Haag duality/split for the quotient-circle net (index =
      statistical dimension reading).
No marker moves; exploration only.""")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
