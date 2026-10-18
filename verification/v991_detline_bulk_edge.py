"""v991 -- SEAM.DETLINE.UNIFICATION.01 [O update: finite bulk-edge
determinant-line shadow [E]; continuum Bismut-Freed stays Open].

THE POINT (promote round 2026-08-28).  Re-derives the executable
content of detline_bulk_edge_probe (not imported) on the v367 QWZ
collar:

  [E] BULK: occupied-frame FHS Chern of the determinant line over the
        twist torus is +1 at M = 1 (L = 4 and L = 6); curvature
        integral = 2 pi * (+1).  M = 3 control is 0 both sizes.

  [E] EDGE: bottom-weighted seam holonomy winding = +1 (phase 2 pi);
        occupied-only winding = +1; signed spectral flow of the
        in-gap bottom branch = +1, top = -1.

  [E] CORRESPONDENCE: 2 pi * C_bulk == holonomy winding (diff machine
        zero; probe 6e-16).  M = 3 control 0 = 0 both sides.

  [E] CONJUGATION MUTANT (SY -> -SY): both signs flip coherently
        (C -> -1 and W -> -1).

HONEST SCOPE (firewall): 2+1D bulk / 1D edge finite lattice shadow.
Continuum Bismut-Freed and the 4D chiral-measure unification stay [O].
No marker move.  Python-only / Wolfram mirror deferred.

Provenance: experiments/tfpt-discovery/detline_bulk_edge_probe.py
(ALL PASS; not imported).
"""
import numpy as np

from tfpt_constants import check, summary, reset

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
TX = (SX / (2j) - SZ / 2)

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
            assert n_occ == n_ref

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


def run():
    reset()
    print("v991  SEAM.DETLINE.UNIFICATION.01: finite bulk-edge "
          "determinant-line correspondence")

    bulk = {}
    for (M, sy, tag) in ((1.0, 1.0, "TOP"), (3.0, 1.0, "TRIV"),
                         (1.0, -1.0, "CONJ")):
        bulk[tag] = {}
        for L in (L_SMALL, L_LARGE):
            C, gap, F = detline_chern(L, M, sy=sy)
            bulk[tag][L] = dict(C=C, gap=gap, F=F)
            print("   %s L=%d: C=%+.10f  int F=%+.10f  gap=%.4f"
                  % (tag, L, C, F, gap))

    C_top4 = bulk["TOP"][L_SMALL]["C"]
    C_top6 = bulk["TOP"][L_LARGE]["C"]
    F_top6 = bulk["TOP"][L_LARGE]["F"]
    check("BULK TOP [E]: det-line Chern = +1 at L = 4 and L = 6 "
          "(C4=%+.8f C6=%+.8f)" % (C_top4, C_top6),
          near_int(C_top4, 1, TOL_CHERN)
          and near_int(C_top6, 1, TOL_CHERN))
    check("BULK CURVATURE [E]: integral F = 2 pi * (+1) at L = 6 "
          "(diff %.1e)" % abs(F_top6 - 2.0 * np.pi),
          abs(F_top6 - 2.0 * np.pi) < 1e-7)
    check("BULK CONTROL [E]: M = 3 Chern = 0 on both sizes",
          all(near_int(bulk["TRIV"][L]["C"], 0, TOL_CHERN)
              for L in (L_SMALL, L_LARGE)))

    edge = {}
    for (M, sy, tag) in ((1.0, 1.0, "TOP"), (3.0, 1.0, "TRIV"),
                         (1.0, -1.0, "CONJ")):
        r = seam_detline(M, sy=sy)
        edge[tag] = r
        print("   EDGE %s: W_seam=%+.8f  W_occ=%+.8f  W_top=%+.8f  "
              "sf_bot=%+d  sf_top=%+d"
              % (tag, r["W_seam"], r["W_occ"], r["W_top"],
                 r["sf_bot"], r["sf_top"]))

    et = edge["TOP"]
    check("EDGE SEAM [E]: bottom-weighted holonomy winding = +1",
          near_int(et["W_seam"], 1, TOL_WIND))
    check("EDGE SLATER [E]: occupied-only winding = +1 and "
          "sf_bot = +1, sf_top = -1",
          near_int(et["W_occ"], 1, TOL_WIND)
          and et["sf_bot"] == 1 and et["sf_top"] == -1)
    ev = edge["TRIV"]
    check("EDGE CONTROL [E]: M = 3 W_seam = W_occ = 0 and "
          "sf_bot = sf_top = 0",
          near_int(ev["W_seam"], 0, TOL_WIND)
          and near_int(ev["W_occ"], 0, TOL_WIND)
          and ev["sf_bot"] == 0 and ev["sf_top"] == 0)

    cyl = {}
    for (M, sy, tag) in ((1.0, 1.0, "TOP"), (3.0, 1.0, "TRIV"),
                         (1.0, -1.0, "CONJ")):
        cyl[tag] = cylinder_edge_flow(M, sy=sy)
    check("CYLINDER [E]: M = 1 bottom flow +1, top -1; M = 3 none",
          cyl["TOP"]["bottom"] == 1 and cyl["TOP"]["top"] == -1
          and cyl["TRIV"]["bottom"] == 0 and cyl["TRIV"]["top"] == 0)

    C = C_top6
    W = et["W_seam"]
    diff = C - W
    print("   C - W = %+.3e" % diff)
    check("CORRESPONDENCE [E]: C_bulk = W_seam = +1 "
          "(diff %.1e; probe ~6e-16)" % abs(diff),
          near_int(C, 1, TOL_CHERN) and near_int(W, 1, TOL_WIND)
          and et["sf_bot"] == 1 and abs(diff) < 1e-6)
    check("CORRESPONDENCE CONTROL [E]: M = 3 gives 0 = 0 both sides",
          near_int(bulk["TRIV"][L_LARGE]["C"], 0, TOL_CHERN)
          and near_int(ev["W_seam"], 0, TOL_WIND)
          and ev["sf_bot"] == 0)

    Cc = bulk["CONJ"][L_LARGE]["C"]
    Wc = edge["CONJ"]["W_seam"]
    check("MUTANT [E]: conjugation flips C and W together "
          "(C=%+.8f W=%+.8f)" % (Cc, Wc),
          near_int(Cc, -1, TOL_CHERN) and near_int(Wc, -1, TOL_WIND)
          and edge["CONJ"]["sf_bot"] == -1
          and cyl["CONJ"]["bottom"] == -1
          and cyl["CONJ"]["top"] == 1
          and near_int(Cc + C, 0, 1e-7)
          and near_int(Wc + W, 0, 1e-6))

    check("FIREWALL (scope): 2+1D/1D finite lattice shadow; "
          "continuum Bismut-Freed and 4D unification stay [O]; "
          "SEAM.DETLINE.UNIFICATION.01 not closed", True)
    return summary("v991 detline bulk-edge: finite shadow [E], "
                   "continuum stays [O]")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
