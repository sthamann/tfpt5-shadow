#!/usr/bin/env python3
"""detline_bulk_edge_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (SEAM.DETLINE.UNIFICATION.01 [O]): the hypothesis
Res_seam det D_4D ~= det D_seam WITH CONNECTION (bulk determinant line
restricted to the seam = seam determinant line; holonomy = discrete
orientation phase) would unify seam extension, chiral measure, generation
index and CP orientation.  The finite Schur/BFK shadow already exists
(detline_finite_shadow_probe.py: graph Laplacian, identity vs local-factor
kill, no bundle over moduli).  v472 computed the bulk Quillen object
(occupied-frame det-line Chern = 1 on the v367 twist torus) but not the
bulk-edge correspondence of that line.  This probe is the missing finite
BULK-EDGE determinant-line correspondence on the real collar, re-derived
independently (no import of v472 numbers or code).

TYPED CLAIMS (2+1D QWZ/p+ip collar, M = 1 topological / M = 3 trivial;
hopping convention of psi_lambda_seam_edge_s1s2_probe.py):

  [BULK]  Occupied-frame determinant line over the U(1)-twist torus
        (theta_x, theta_y) of an L x L lattice.  Fukui-Hatsugai-Suzuki
        curvature integral = 2 pi * C with C(M=1) = 1, size-independent
        (L = 4 and L = 6).  Fermi gap open over the whole torus (section
        globally defined).  Independent re-computation, not a lookup.

  [EDGE/SEAM]  Exact edge theory of the same model: the open-y strip at
        Bloch momentum k (the dimensional reduction of the QWZ cylinder).
        (a) SEAM DET-LINE HOLONOMY: winding of the bottom-weighted
        regularized determinant  sum_n w_bot(psi_n) log(E_n + i eps)
        over k : 0 -> 2 pi  equals +1 (phase 2 pi).  w_bot = exp(-<y>/xi)
        is a frozen collar weight; the occupied-only sibling (E_n < 0)
        winds by the same integer -- the spectral-flow-induced phase
        winding of the edge Slater determinant.
        (b) SLATER OCCUPATION WINDING: signed zero-crossings of the
        in-gap bottom-localized branch = +1 (the skeleton probe's
        spectral-flow swing, now edge-resolved and signed).
        Cylinder cross-check: bottom flow = +1, top = -1 (opposite
        chirality, inflow antisymmetry).

  [CORRESPONDENCE]  C_bulk = W_seam = W_Slater as integers; the finite
        Bismut-Freed / inflow shadow
            curv(L_bulk) integral / 2 pi  -  holonomy_winding(L_seam)  =  0
        ('exact' at the lattice integer level).

  [CONTROLS]  Trivial phase M = 3: C = 0 and W = 0 on BOTH sides.
        Conjugation mutant (SY -> -SY, the complex-conjugate collar)
        flips BOTH signs coherently: C -> -1 and W -> -1.  The holonomy
        sign is the orientation branch -- the same Z2 typing as
        sgn J = +-1/27 in v977 (prose only; this probe does not touch
        the Wilson/Jarlskog matrix).

HONEST BOUNDARY (firewall): a 2+1D bulk / 1D edge finite lattice shadow
of the determinant-line correspondence.  Complements, does not replace,
the graph-Laplacian Schur shadow.  The continuum Bismut-Freed
identification and the 4D chiral-measure unification stay [O]; nothing
here closes SEAM.DETLINE.UNIFICATION.01.  One complex-fermion copy (the
physical collar is 16 Majoranas).  No marker moves, no promotion.

VERDICT ENUM: DETLINE_BULK_EDGE_SHADOW_MATCHES
(bulk curvature integer = edge holonomy winding, controls and mutant
coherent; continuum / 4D side of the contract open).
"""
import numpy as np

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name
          + (("  | " + extra) if extra else ""))
    return bool(ok)


SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)

# QWZ real-space hoppings, verbatim psi_lambda_seam_edge_s1s2_probe.py:
#   h(k) = sin kx SX + sin ky SY + (M - cos kx - cos ky) SZ
TX = (SX / (2j) - SZ / 2)

# frozen lattice / regulator choices (stability: W_seam = 1 for xi in
# [0.8, 1.5], Nk in {48, 64, 128}, Ny in {12, 16, 20}, eps in {0.02, 0.05})
L_SMALL, L_LARGE = 4, 6
N_GRID = 8
NY_STRIP, NK_STRIP = 16, 64
EPS_DET, XI_BOT = 0.02, 1.2
GAP_WINDOW = 0.8
NX_CYL, NY_CYL, NT_CYL = 8, 10, 40
TOL_CHERN = 1e-8
TOL_WIND = 1e-6


def _TY(sy):
    return (sy * SY / (2j) - SZ / 2)


def torus_H(L, M, thx, thy, sy=1.0):
    """QWZ on an L x L torus with U(1) twists (thx, thy)."""
    n = L * L
    H = np.zeros((2 * n, 2 * n), complex)
    TYm = _TY(sy)

    def blk(x, y):
        return 2 * ((x % L) + L * (y % L))

    for x in range(L):
        for y in range(L):
            i = blk(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            for dx, dy, T, th in ((1, 0, TX, thx), (0, 1, TYm, thy)):
                j = blk(x + dx, y + dy)
                phase = (np.exp(1j * th)
                         if (x + dx == L or y + dy == L) else 1.0)
                H[j:j + 2, i:i + 2] += phase * T
                H[i:i + 2, j:j + 2] += np.conj(phase) * T.conj().T
    return H


def detline_chern(L, M, n_grid=N_GRID, sy=1.0):
    """FHS Chern of the occupied-frame determinant line over the twist
    torus.  Returns (C, min_gap, curvature_integral = 2 pi C)."""
    ths = np.linspace(0.0, 2.0 * np.pi, n_grid, endpoint=False)
    frames = {}
    min_gap, n_ref = np.inf, None
    for i, tx in enumerate(ths):
        for j, ty in enumerate(ths):
            w, v = np.linalg.eigh(torus_H(L, M, tx, ty, sy))
            n_occ = int(np.sum(w < 0.0))
            frames[(i, j)] = v[:, :n_occ]
            min_gap = min(min_gap, float(w[n_occ] - w[n_occ - 1]))
            if n_ref is None:
                n_ref = n_occ
            assert n_occ == n_ref, "occupation jumped -- gap closed on torus"

    def link(a, b):
        u = np.linalg.det(frames[a].conj().T @ frames[b])
        return u / abs(u)

    F = 0.0
    for i in range(n_grid):
        for j in range(n_grid):
            ip, jp = (i + 1) % n_grid, (j + 1) % n_grid
            F += np.angle(link((i, j), (ip, j))
                          * link((ip, j), (ip, jp))
                          * np.conj(link((i, jp), (ip, jp)))
                          * np.conj(link((i, j), (i, jp))))
    C = F / (2.0 * np.pi)
    return float(C), float(min_gap), float(F)


def strip_H(k, M, Ny, sy=1.0):
    """Open-y strip at Bloch momentum k (exact edge theory of the cylinder)."""
    ons = np.sin(k) * SX + (M - np.cos(k)) * SZ
    hop = -0.5 * SZ + sy * (1.0 / (2j)) * SY
    H = np.zeros((2 * Ny, 2 * Ny), complex)
    for y in range(Ny):
        H[2 * y:2 * y + 2, 2 * y:2 * y + 2] = ons
    for y in range(Ny - 1):
        H[2 * y:2 * y + 2, 2 * y + 2:2 * y + 4] = hop
        H[2 * y + 2:2 * y + 4, 2 * y:2 * y + 2] = hop.conj().T
    return H


def _wind(logdets):
    im = np.unwrap([z.imag for z in logdets] + [logdets[0].imag])
    return float((im[-1] - im[0]) / (2.0 * np.pi))


def seam_detline(M, Ny=NY_STRIP, Nk=NK_STRIP, sy=1.0,
                 eps=EPS_DET, xi=XI_BOT, gap_win=GAP_WINDOW):
    """Bottom-weighted regularized det winding + in-gap spectral flow
    of the strip.  Returns dict with W_seam, W_occ, W_top, sf_bot, sf_top."""
    ks = np.linspace(0.0, 2.0 * np.pi, Nk, endpoint=False)
    y_site = np.repeat(np.arange(Ny), 2).astype(float)
    ld_bot, ld_occ, ld_top = [], [], []
    E_bot, E_top = [], []
    for k in ks:
        w, v = np.linalg.eigh(strip_H(k, M, Ny, sy))
        acc_b = acc_o = acc_t = 0.0j
        bot_in, top_in = [], []
        for n, E in enumerate(w):
            yexp = float(np.abs(v[:, n]) ** 2 @ y_site)
            wb = np.exp(-yexp / xi)
            wt = np.exp(-(Ny - 1.0 - yexp) / xi)
            z = np.log(E + 1j * eps)
            acc_b += wb * z
            acc_t += wt * z
            if E < 0.0:
                acc_o += wb * z
            if abs(E) < gap_win:
                if yexp < Ny / 2.0:
                    bot_in.append(E)
                else:
                    top_in.append(E)
        ld_bot.append(acc_b)
        ld_occ.append(acc_o)
        ld_top.append(acc_t)
        E_bot.append(bot_in[int(np.argmin(np.abs(bot_in)))] if bot_in
                     else np.nan)
        E_top.append(top_in[int(np.argmin(np.abs(top_in)))] if top_in
                     else np.nan)

    def signed_flow(energies):
        sf = 0
        seq = list(energies) + [energies[0]]
        for a, b in zip(seq, seq[1:]):
            if np.isnan(a) or np.isnan(b):
                continue
            if a < 0.0 <= b:
                sf += 1
            if a > 0.0 >= b:
                sf -= 1
        return sf

    W_seam = _wind(ld_bot)
    return dict(W_seam=W_seam, W_occ=_wind(ld_occ), W_top=_wind(ld_top),
                phase=2.0 * np.pi * W_seam,
                sf_bot=signed_flow(E_bot), sf_top=signed_flow(E_top))


def qwz_cylinder(Nx, Ny, M, theta, sy=1.0):
    """Cylinder: periodic x with twist theta on the seam bond, open y."""
    TYm = _TY(sy)
    dim = 2 * Nx * Ny
    H = np.zeros((dim, dim), complex)

    def sl(x, y):
        return 2 * ((x % Nx) * Ny + y)

    ph = np.exp(1j * theta)
    for x in range(Nx):
        for y in range(Ny):
            i = sl(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            j = sl(x + 1, y)
            amp = ph if x == Nx - 1 else 1.0
            H[j:j + 2, i:i + 2] += amp * TX
            H[i:i + 2, j:j + 2] += np.conj(amp) * TX.conj().T
            if y + 1 < Ny:
                jy = sl(x, y + 1)
                H[jy:jy + 2, i:i + 2] += TYm
                H[i:i + 2, jy:jy + 2] += TYm.conj().T
    return H


def cylinder_edge_flow(M, Nx=NX_CYL, Ny=NY_CYL, Nt=NT_CYL, sy=1.0,
                       gap_win=GAP_WINDOW):
    """Signed in-gap zero-crossings of bottom vs top edge vs twist.
    Half-step theta grid so a symmetric E=0 hit is not pinned on a sample."""
    ths = 2.0 * np.pi * (np.arange(Nt) + 0.5) / Nt
    y_site = np.array([y for _x in range(Nx) for y in range(Ny)
                       for _or in (0, 1)], float)
    flow = {"bottom": 0, "top": 0}
    prev = {}
    for th in ths:
        w, v = np.linalg.eigh(qwz_cylinder(Nx, Ny, M, th, sy))
        ingap = {}
        for i in np.where(np.abs(w) < gap_win)[0]:
            yexp = float(np.abs(v[:, i]) ** 2 @ y_site)
            edge = "bottom" if yexp < Ny / 2.0 else "top"
            if edge not in ingap or abs(w[i]) < abs(ingap[edge]):
                ingap[edge] = float(w[i])
        for edge, E_new in ingap.items():
            E_old = prev.get(edge)
            if E_old is not None and E_old * E_new < 0.0:
                flow[edge] += 1 if E_new > E_old else -1
        prev = ingap
    return flow


def near_int(x, n, tol):
    return abs(x - n) < tol


def main():
    print("detline_bulk_edge_probe -- finite bulk-edge determinant-line "
          "correspondence on the v367 QWZ collar")
    print("(EXPLORATION ONLY; SEAM.DETLINE.UNIFICATION.01 stays [O])")
    print()

    # ------------------------------------------------------------------ bulk
    print("=== BULK: occupied-frame det line over the twist torus ===")
    bulk = {}
    for (M, sy, tag) in ((1.0, 1.0, "TOP"), (3.0, 1.0, "TRIV"),
                         (1.0, -1.0, "CONJ")):
        bulk[tag] = {}
        for L in (L_SMALL, L_LARGE):
            C, gap, F = detline_chern(L, M, sy=sy)
            bulk[tag][L] = dict(C=C, gap=gap, F=F)
            print("   %s M=%+.0f sy=%+.0f L=%d:  C=%+.10f  "
                  "int F = %+.10f  (= 2 pi C)  min_gap=%.4f"
                  % (tag, M, sy, L, C, F, gap))

    C_top4 = bulk["TOP"][L_SMALL]["C"]
    C_top6 = bulk["TOP"][L_LARGE]["C"]
    F_top6 = bulk["TOP"][L_LARGE]["F"]
    rep("BULK TOP (M=1): det-line Chern over the twist torus = 1 "
        "(L=4 and L=6, independently re-derived)",
        near_int(C_top4, 1, TOL_CHERN) and near_int(C_top6, 1, TOL_CHERN),
        "C(L=4)=%+.10f  C(L=6)=%+.10f" % (C_top4, C_top6))
    rep("BULK curvature integral = 2 pi * 1 (L=6)",
        abs(F_top6 - 2.0 * np.pi) < 1e-7,
        "int F = %+.12f" % F_top6)
    rep("BULK section globally defined: Fermi gap open on the whole "
        "twist torus at M=1 (min gap = 2)",
        bulk["TOP"][L_SMALL]["gap"] > 1.9
        and bulk["TOP"][L_LARGE]["gap"] > 1.9,
        "gap L=4 %.4f  L=6 %.4f"
        % (bulk["TOP"][L_SMALL]["gap"], bulk["TOP"][L_LARGE]["gap"]))
    C_triv6 = bulk["TRIV"][L_LARGE]["C"]
    rep("BULK CONTROL (M=3): det-line Chern = 0 on both sizes",
        all(near_int(bulk["TRIV"][L]["C"], 0, TOL_CHERN)
            for L in (L_SMALL, L_LARGE)),
        "C(L=6)=%+.10f" % C_triv6)

    # ------------------------------------------------------------------ edge
    print()
    print("=== EDGE/SEAM: strip det-line holonomy + Slater spectral flow ===")
    edge = {}
    for (M, sy, tag) in ((1.0, 1.0, "TOP"), (3.0, 1.0, "TRIV"),
                         (1.0, -1.0, "CONJ")):
        r = seam_detline(M, sy=sy)
        edge[tag] = r
        print("   %s:  W_seam=%+.8f  (phase=%+.8f)  W_occ=%+.8f  "
              "W_top=%+.8f  sf_bot=%+d  sf_top=%+d"
              % (tag, r["W_seam"], r["phase"], r["W_occ"], r["W_top"],
                 r["sf_bot"], r["sf_top"]))

    et = edge["TOP"]
    rep("EDGE SEAM DET-LINE (M=1): bottom-weighted holonomy winding = +1 "
        "(phase 2 pi; finite Quillen/BF det of the chiral edge)",
        near_int(et["W_seam"], 1, TOL_WIND),
        "W_seam=%+.10f  phase=%+.10f" % (et["W_seam"], et["phase"]))
    rep("EDGE SLATER PHASE (M=1): occupied-only bottom-weighted winding "
        "= +1 -- spectral-flow-induced phase winding of the edge Slater det",
        near_int(et["W_occ"], 1, TOL_WIND),
        "W_occ=%+.10f" % et["W_occ"])
    rep("EDGE SLATER OCCUPATION (M=1): signed spectral flow of the "
        "in-gap bottom branch = +1 (skeleton swing, now signed)",
        et["sf_bot"] == 1,
        "sf_bot=%+d  sf_top=%+d" % (et["sf_bot"], et["sf_top"]))
    rep("EDGE chirality: top-edge winding = -1 (opposite to bottom, "
        "inflow antisymmetry of a C=1 collar)",
        near_int(et["W_top"], -1, TOL_WIND) and et["sf_top"] == -1,
        "W_top=%+.10f  sf_top=%+d" % (et["W_top"], et["sf_top"]))

    ev = edge["TRIV"]
    rep("EDGE CONTROL (M=3): W_seam = W_occ = 0 and sf_bot = sf_top = 0",
        near_int(ev["W_seam"], 0, TOL_WIND)
        and near_int(ev["W_occ"], 0, TOL_WIND)
        and ev["sf_bot"] == 0 and ev["sf_top"] == 0,
        "W_seam=%+.10f  sf_bot=%+d" % (ev["W_seam"], ev["sf_bot"]))

    # ------------------------------------------------------------------ cyl
    print()
    print("=== CYLINDER cross-check (same twist cycle, both edges) ===")
    cyl = {}
    for (M, sy, tag) in ((1.0, 1.0, "TOP"), (3.0, 1.0, "TRIV"),
                         (1.0, -1.0, "CONJ")):
        cyl[tag] = cylinder_edge_flow(M, sy=sy)
        print("   %s:  flow bottom=%+d  top=%+d" % (tag, cyl[tag]["bottom"],
                                                    cyl[tag]["top"]))
    rep("CYLINDER (M=1): bottom spectral flow = +1, top = -1 "
        "(one chiral branch per edge)",
        cyl["TOP"]["bottom"] == 1 and cyl["TOP"]["top"] == -1)
    rep("CYLINDER CONTROL (M=3): no in-gap flow on either edge",
        cyl["TRIV"]["bottom"] == 0 and cyl["TRIV"]["top"] == 0)

    # ------------------------------------------------------------------ corr
    print()
    print("=== CORRESPONDENCE: curv(L_bulk) / 2 pi  =  holonomy(L_seam) ===")
    C = C_top6
    W = et["W_seam"]
    Wsf = float(et["sf_bot"])
    diff = C - W
    print("   C_bulk(L=6)=%+.10f   W_seam=%+.10f   W_Slater_sf=%+.10f   "
          "C - W = %+.3e" % (C, W, Wsf, diff))
    rep("CORRESPONDENCE (M=1): C_bulk = W_seam = W_Slater = +1 "
        "(finite Bismut-Freed / inflow shadow; difference exact at "
        "lattice integers)",
        near_int(C, 1, TOL_CHERN) and near_int(W, 1, TOL_WIND)
        and Wsf == 1.0 and abs(diff) < 1e-6,
        "C - W = %+.3e" % diff)
    rep("CORRESPONDENCE CONTROL (M=3): 0 = 0 on both sides",
        near_int(C_triv6, 0, TOL_CHERN)
        and near_int(ev["W_seam"], 0, TOL_WIND)
        and ev["sf_bot"] == 0)

    # ------------------------------------------------------------------ mutant
    print()
    print("=== CONJUGATION MUTANT (SY -> -SY): both signs flip ===")
    Cc = bulk["CONJ"][L_LARGE]["C"]
    Wc = edge["CONJ"]["W_seam"]
    sfc = edge["CONJ"]["sf_bot"]
    print("   C_conj=%+.10f   W_seam_conj=%+.10f   sf_bot_conj=%+d   "
          "cyl bot/top = %+d/%+d"
          % (Cc, Wc, sfc, cyl["CONJ"]["bottom"], cyl["CONJ"]["top"]))
    rep("MUTANT bulk: C(M=1, SY -> -SY) = -1",
        near_int(Cc, -1, TOL_CHERN), "C=%+.10f" % Cc)
    rep("MUTANT edge: W_seam = W_occ = sf_bot = -1 "
        "(and top edge flips to +1)",
        near_int(Wc, -1, TOL_WIND)
        and near_int(edge["CONJ"]["W_occ"], -1, TOL_WIND)
        and sfc == -1
        and near_int(edge["CONJ"]["W_top"], 1, TOL_WIND)
        and edge["CONJ"]["sf_top"] == 1,
        "W_seam=%+.10f  sf_bot=%+d" % (Wc, sfc))
    rep("MUTANT cylinder: bottom flow = -1, top = +1",
        cyl["CONJ"]["bottom"] == -1 and cyl["CONJ"]["top"] == 1)
    rep("MUTANT coherent: conjugation flips bulk C and edge W together "
        "(C_conj = -C_topo, W_conj = -W_topo) -- holonomy sign = the "
        "orientation branch, the same Z2 typing as sgn J = +-1/27 in v977 "
        "(prose only)",
        near_int(Cc + C, 0, 1e-7) and near_int(Wc + W, 0, 1e-6),
        "C_topo+C_conj=%+.3e  W_topo+W_conj=%+.3e" % (C + Cc, W + Wc))

    # ------------------------------------------------------------------ honest
    print()
    rep("HONEST BOUNDARY (typed): 2+1D bulk / 1D edge finite lattice "
        "shadow; graph-Laplacian Schur probe is complemented not duplicated; "
        "continuum Bismut-Freed and 4D chiral-measure unification stay [O]; "
        "SEAM.DETLINE.UNIFICATION.01 is not closed", True)

    print()
    if ok_all:
        verdict = "DETLINE_BULK_EDGE_SHADOW_MATCHES"
    else:
        verdict = "DETLINE_BULK_EDGE_MISMATCH"
    print("VERDICT: %s -- bulk det-line curvature integer equals the "
          "seam det-line holonomy winding on the v367 collar; trivial "
          "and conjugation controls coherent; the continuum / 4D face of "
          "SEAM.DETLINE.UNIFICATION.01 stays [O]; no promotion"
          % verdict)
    print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
