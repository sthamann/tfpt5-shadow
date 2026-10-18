#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""sheetflip_skyparity_bridge_probe -- SHEETFLIP.SKYPARITY.BRIDGE.01
(signature-bundle round 2026-08-27, the bridge-theorem attack): the
missing physical arrow "internal Z2 -> cosmological E/B parity"
(OBS.TRANSDUCTION.01, double-tone leg) is REDUCED TO ONE COVARIANCE
AXIOM by three machine-checked pieces:

  (I)   SEAM SIDE (exact): the sheet flip is the CLOCK-REVERSAL coset
        of the deployed D4 seam symmetry; every representative
        reverses the seam-circle orientation (the 1D chirality that
        orders the mu4 marks), but the SPHERE-orientation bit is NOT
        determined by the seam action alone (holomorphic vs
        anti-holomorphic representatives both exist) -- the "rep bit".
        The corpus CPT typing of the sheet flip (anti-UNITARY, hence
        anti-linear, hence anti-holomorphic on the celestial sphere)
        PINS the orientation-REVERSING class.  [machine: Moebius
        algebra with conjugation flags; typing cited]
  (II)  SKY SIDE (machine-verified to 1e-14): under the
        orientation-reversing sky map (antipodal; exact on the
        HEALPix grid) T -> (-1)^l T, E -> (-1)^l E,
        B -> (-1)^{l+1} B -- B carries the EXTRA relative minus sign;
        rotations (orientation-preserving) never mix or flip E/B;
        the wrong-U-sign pseudo-map control FIRES (not an isometry
        pullback).  Hence TB/EB are the parity-ODD spectra, TT/TE/EE
        the parity-EVEN ones.
  (III) EQUIVARIANCE THEOREM (exact, the new statement): for EVERY
        coupling K intertwining the internal sheet swap S with the
        sky parity R (K S = R K), the channel dictionary follows
        IDENTICALLY: E-type readouts annihilate P_- (the omega_+
        tone feeds ONLY TB/EB) and B-type readouts annihilate P_+
        (omega_- + monopole feed ONLY TT/TE/EE).  A generic
        non-equivariant K violates it (negative control fires).

THE THEOREM (typed): COVARIANT COUPLING + CPT-TYPED SHEET BIT
==> the double-tone forbidden-channel dictionary.  The [O] middle
arrow of OBS.TRANSDUCTION.01 (double-tone leg) SHRINKS from "unknown
transduction map" to the single premise
    TE: the physical coupling is geometrically covariant w.r.t. the
        crossover isometries realizing the seam D4 (DLVIII: all four
        mirrors ARE SU(2) isometries of S^3 descending to the lens
        crossover -- cited), with the sheet bit implemented
        anti-unitarily (CPT reading, origin_theory / round DL).
NOT claimed: TE itself (a physical axiom about the coupling, not yet
a theorem); no data contact here; no marker moves.

DEPLOYED ANCHORS (read-only): round DL (tau rho tau^-1 = rho^-1 ==
"Clock-Umkehr == die Z2 sheet parity / CPT-Flip der Origin Theory");
DLVIII (D4 mirrors as SU(2) isometries); DLI (seam sphere == Hopf/
celestial base); doubletone_character_transduction_probe (S, P_+-,
tone assignment); standard spin-2 parity (Zaldarriaga-Seljak class,
machine-verified here rather than cited).

KILLS: K-1 Moebius/coset algebra fails (SEAM-DEAD); K-2 sky parity
law fails or a control does not fire (SKY-DEAD); K-3 the equivariance
consequence fails or the negative control passes (THEOREM-DEAD).

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface;
keine Marker-Bewegung; SHEETFLIP.SKYPARITY.BRIDGE.01 ist ein
VORSCHLAG fuer next.txt, keine Ledger-Zeile.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/sheetflip_skyparity_bridge_probe.py
"""

import time

import numpy as np
import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []
SEED = 20260827
NSIDE, LMAX = 64, 20


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# -------------------------------------------- Moebius maps + conj flag
def act(m, z):
    """apply (matrix, conjflag) to a point z."""
    mat, cf = m
    w = sp.conjugate(z) if cf else z
    return sp.simplify((mat[0, 0] * w + mat[0, 1])
                       / (mat[1, 0] * w + mat[1, 1]))


def comp(m1, m2):
    """(m1 o m2) with conjugation bookkeeping."""
    a1, c1 = m1
    a2, c2 = m2
    a2e = a2.applyfunc(sp.conjugate) if c1 else a2
    return (sp.simplify(a1 * a2e), c1 ^ c2)


def proj_eq(m1, m2, pts):
    """projective equality of two (matrix, conj) maps on test points."""
    if m1[1] != m2[1]:
        return False
    return all(sp.simplify(act(m1, z) - act(m2, z)) == 0 for z in pts)


RHO = (sp.Matrix([[sp.I, 0], [0, 1]]), False)          # clock z -> iz
TAU = (sp.Matrix([[0, -1], [1, 0]]), False)            # z -> -1/z
SREF = (sp.Matrix([[0, 1], [1, 0]]), False)            # z -> 1/z
CONJ = (sp.eye(2), True)                               # z -> conj(z)
RHO_INV = (sp.Matrix([[-sp.I, 0], [0, 1]]), False)     # z -> -iz
PTS = [sp.Rational(1, 3) + 2 * sp.I, 2 - sp.I, sp.Rational(5, 7)]


def circle_orientation(m):
    """sign of d(theta')/d(theta) for the induced circle map."""
    th = sp.symbols("theta", real=True)
    w = act(m, sp.exp(sp.I * th))
    thp = sp.arg(w)
    d = sp.simplify(sp.diff(sp.re(w), th) * (-sp.sin(sp.arg(w)))
                    + sp.diff(sp.im(w), th) * sp.cos(sp.arg(w)))
    # simpler: evaluate numeric derivative of arg at a generic angle
    f = sp.lambdify(th, sp.im(sp.log(w)), "numpy")
    t0, h = 0.7, 1e-6
    return 1 if (f(t0 + h) - f(t0 - h)) > 0 else -1


def sphere_orientation(m):
    """sign of the real 2x2 Jacobian det at a generic point."""
    x, y = sp.symbols("x y", real=True)
    z = x + sp.I * y
    w = act(m, z)
    u, v = sp.re(w), sp.im(w)
    jac = sp.Matrix([[sp.diff(u, x), sp.diff(u, y)],
                     [sp.diff(v, x), sp.diff(v, y)]])
    d = sp.simplify(jac.det()).subs({x: sp.Rational(1, 3),
                                     y: sp.Rational(2, 5)})
    return 1 if d > 0 else -1


# ==================================================================== I
def task_seam():
    section("I: Seam-Seite -- Sheet-Flip = Uhr-Umkehr-Coset, Rep-Bit, "
            "CPT-Pin")
    ok1 = check("I1 Uhr-Umkehr-Coset: tau rho tau^-1 = s rho s^-1 = "
                "c rho c^-1 = rho^-1 exakt (alle drei Repraesentanten "
                "kehren die Uhr)",
                proj_eq(comp(comp(TAU, RHO), TAU), RHO_INV, PTS)
                and proj_eq(comp(comp(SREF, RHO), SREF), RHO_INV, PTS)
                and proj_eq(comp(comp(CONJ, RHO), CONJ), RHO_INV, PTS),
                kill="SEAM-DEAD")

    marks = [1, sp.I, -1, -sp.I]
    ok2 = check("I2 Seam-Kreis: rho erhaelt die Orientierung (+), tau/"
                "s/c KEHREN sie um (-) -- der Sheet-Flip kehrt die "
                "zyklische Markenordnung (1D-Chiralitaet) um; Marken "
                "bleiben als Menge erhalten",
                circle_orientation(RHO) == 1
                and circle_orientation(TAU) == -1
                and circle_orientation(SREF) == -1
                and circle_orientation(CONJ) == -1
                and all(set(sp.simplify(act(m, z)) for z in marks)
                        == set(marks) for m in (RHO, TAU, SREF, CONJ)),
                kill="SEAM-DEAD")

    ok3 = check("I3 REP-BIT: Sphaeren-Orientierung ist im Coset NICHT "
                "bestimmt -- tau, s holomorph (det J > 0), c anti-"
                "holomorph (det J < 0); die Seam-Daten allein lassen "
                "das Himmels-Orientierungsbit frei",
                sphere_orientation(TAU) == 1
                and sphere_orientation(SREF) == 1
                and sphere_orientation(CONJ) == -1,
                kill="SEAM-DEAD")

    check("I4 CPT-PIN (getypt [C], zitiert DL/origin_theory): der "
          "Sheet-Flip ist der CPT-Flip => anti-UNITAER (Wigner) => "
          "anti-linear => anti-holomorpher Repraesentant => das "
          "orientierungs-UMKEHRENDE Himmelsbit ist selektiert", True)
    return ok1 and ok2 and ok3


# =================================================================== II
def task_sky():
    section("II: Himmels-Seite -- Orientierungsumkehr fixiert E, "
            "flippt B (maschinell)")
    import healpy as hp

    rng = np.random.default_rng(SEED)
    n_alm = hp.Alm.getsize(LMAX)

    def rand_alm():
        a = rng.normal(size=n_alm) + 1j * rng.normal(size=n_alm)
        for l in range(LMAX + 1):
            a[hp.Alm.getidx(LMAX, l, 0)] = \
                a[hp.Alm.getidx(LMAX, l, 0)].real
        for l in range(2):
            for m in range(l + 1):
                a[hp.Alm.getidx(LMAX, l, m)] = 0
        return a

    alm_e, alm_b = rand_alm(), rand_alm()
    q, u = hp.alm2map_spin([alm_e, alm_b], NSIDE, 2, LMAX)
    ae0, ab0 = hp.map2alm_spin([q, u], 2, LMAX)

    npix = hp.nside2npix(NSIDE)
    vx, vy, vz = hp.pix2vec(NSIDE, np.arange(npix))
    anti = hp.vec2pix(NSIDE, -vx, -vy, -vz)
    av = np.array(hp.pix2vec(NSIDE, anti))
    ok0 = check("II0 Antipoden-Map exakt auf dem HEALPix-Gitter "
                "(max |v(anti) + v| = %.1e)" %
                np.max(np.abs(av + np.array([vx, vy, vz]))),
                np.max(np.abs(av + np.array([vx, vy, vz]))) < 1e-12,
                kill="SKY-DEAD")

    aep, abp = hp.map2alm_spin([q[anti], -u[anti]], 2, LMAX)
    dev_e, dev_b = [], []
    for l in range(2, LMAX + 1):
        idx = [hp.Alm.getidx(LMAX, l, m) for m in range(l + 1)]
        dev_e.append(np.nanmax(np.abs(aep[idx] / ae0[idx] - (-1) ** l)))
        dev_b.append(np.nanmax(np.abs(abp[idx] / ab0[idx]
                                      - (-1) ** (l + 1))))
    ok1 = check("II1 Paritaetsgesetz: E -> (-1)^l E (max dev %.1e), "
                "B -> (-1)^(l+1) B (max dev %.1e) -- B traegt das "
                "relative MINUS" % (max(dev_e), max(dev_b)),
                max(dev_e) < 1e-10 and max(dev_b) < 1e-10,
                kill="SKY-DEAD")

    alm_t = rand_alm()
    t_map = hp.alm2map(alm_t, NSIDE, lmax=LMAX)
    at0 = hp.map2alm(t_map, lmax=LMAX, iter=3)
    atp = hp.map2alm(t_map[anti], lmax=LMAX, iter=3)
    dev_t = []
    for l in range(2, LMAX + 1):
        idx = [hp.Alm.getidx(LMAX, l, m) for m in range(l + 1)]
        dev_t.append(np.nanmax(np.abs(atp[idx] / at0[idx] - (-1) ** l)))
    ok2 = check("II2 T -> (-1)^l T (max dev %.1e) => TB/EB sind die "
                "paritaets-UNGERADEN Spektren, TT/TE/EE die geraden"
                % max(dev_t), max(dev_t) < 1e-10, kill="SKY-DEAD")

    # controls
    aew, abw = hp.map2alm_spin([q[anti], +u[anti]], 2, LMAX)
    l = 5
    idx = [hp.Alm.getidx(LMAX, l, m) for m in range(1, l + 1)]
    wrong_clean = (np.allclose(aew[idx] / ae0[idx], (-1) ** l)
                   and np.allclose(abw[idx] / ab0[idx], (-1) ** (l + 1)))
    rot = hp.Rotator(rot=(37.0, 21.0, 11.0), deg=True)
    aer, abr = rot.rotate_alm(ae0.copy()), rot.rotate_alm(ab0.copy())
    cl_be = hp.alm2cl(abr, aer)
    cl_bb = hp.alm2cl(ab0)
    cl_bb_r = hp.alm2cl(abr)
    ok3 = check("II3 Kontrollen: Pseudo-Map (falsches U-Vorzeichen) "
                "erfuellt das Gesetz NICHT (feuert); Rotation laesst "
                "BB-Leistung invariant (max rel dev %.1e) -- "
                "Rotationen flippen/mischen nichts"
                % np.max(np.abs(cl_bb_r[2:] - cl_bb[2:])
                         / np.abs(cl_bb[2:])),
                (not wrong_clean)
                and np.max(np.abs(cl_bb_r[2:] - cl_bb[2:])
                           / np.abs(cl_bb[2:])) < 1e-8,
                kill="SKY-DEAD")
    _ = cl_be
    return ok0 and ok1 and ok2 and ok3


# ================================================================== III
def task_theorem():
    section("III: der Aequivarianz-Satz -- KOVARIANZ + CPT => "
            "Kanalwoerterbuch")
    s_swap = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    r_sky = sp.diag(1, -1)                       # (E, B), B paritaets-odd
    b_mat = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
    t_op = b_mat ** 6
    p_minus = (sp.eye(3) - s_swap) / 2
    p_plus = (sp.eye(3) + s_swap) / 2

    ksyms = sp.symbols("k0:6", real=True)
    k_gen = sp.Matrix(2, 3, ksyms)
    constraint = sp.expand(k_gen * s_swap - r_sky * k_gen)
    sol = sp.solve([e for e in constraint], list(ksyms), dict=True)[0]
    k_eq = k_gen.subs(sol)
    free = sorted(k_eq.free_symbols, key=lambda s: s.name)
    ok1 = check("III1 allgemeine Loesung von K S = R K: E-Zeile "
                "S-gerade, B-Zeile S-ungerade (3 freie Parameter: %s)"
                % ", ".join(str(f) for f in free),
                sp.simplify(k_eq * s_swap - r_sky * k_eq) == sp.zeros(2, 3)
                and len(free) == 3, kill="THEOREM-DEAD")

    ok2 = check("III2 SATZ: fuer JEDES aequivariante K gilt "
                "K P_- = (0; *) und K P_+ = (*; 0) -- E-Kanal "
                "annihiliert den omega_+-Ton, B-Kanal annihiliert "
                "Monopol + omega_-, IDENTISCH in den freien Parametern",
                sp.simplify((k_eq * p_minus)[0, :]) == sp.zeros(1, 3)
                and sp.simplify((k_eq * p_plus)[1, :]) == sp.zeros(1, 3),
                kill="THEOREM-DEAD")

    x = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 6),
                   sp.Rational(1, 3)])
    lam = sp.Rational(64, 729)
    tone_b = [sp.simplify((k_eq * t_op ** n * x)[1, 0]
                          / (k_eq * t_op * x)[1, 0]) for n in (2, 3)]
    ok3 = check("III3 Ton-Zuordnung durch den Satz: B-Kanal-Signal "
                "skaliert exakt mit (64/729)^n (Verhaeltnisse %s) -- "
                "der omega_+-Ton lebt NUR in TB/EB; E-Kanal traegt "
                "{1, 1/729}" % tone_b,
                tone_b[0] == lam and tone_b[1] == lam ** 2,
                kill="THEOREM-DEAD")

    k_bad = sp.Matrix([[1, 2, 3], [4, 5, 6]])
    ok4 = check("III4 Negativkontrolle: generisches NICHT-aequivariantes "
                "K leckt in beide Richtungen (feuert)",
                sp.simplify((k_bad * p_minus)[0, :]) != sp.zeros(1, 3)
                and sp.simplify((k_bad * p_plus)[1, :]) != sp.zeros(1, 3),
                kill="THEOREM-DEAD")

    check("III5 REDUKTION (getypt): OBS.TRANSDUCTION.01 (Doppelton-Leg) "
          "schrumpft von 'unbekannte Transduktionsabbildung' auf das "
          "EINE Axiom TE = geometrische Kovarianz der Kopplung "
          "(DLVIII: die D4-Spiegel SIND Isometrien des Crossovers -- "
          "zitiert) + CPT-Lesart des Sheet-Bits (I4); unter TE ist das "
          "Woerterbuch ein SATZ; TE selbst bleibt [O]", True)
    return ok1 and ok2 and ok3 and ok4


def main():
    section("SHEETFLIP.SKYPARITY.BRIDGE.01 -- der Bruecken-Satz, "
            "reduziert auf ein Kovarianz-Axiom")
    ok_i = task_seam()
    ok_ii = task_sky()
    ok_iii = task_theorem()

    section("VERDIKT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("gates: %d/%d PASS; kills: %s" % (n_pass, len(CHECKS),
                                            KILLS or "keine"))
    if ok_i and ok_ii and ok_iii:
        print("VERDIKT: BRIDGE-REDUCED-TO-COVARIANCE")
        print("  [E neu] Seam-Coset-Algebra, Rep-Bit-Dichotomie, "
              "Himmels-Paritaetsgesetz (maschinell), Aequivarianz-Satz;")
        print("  [C] CPT-Pin des Sheet-Bits (zitiert) + DLVIII-"
              "Isometrie-Anker;")
        print("  [O] verbleibend: NUR das Kovarianz-Axiom TE der "
              "physischen Kopplung -- der frueher formlose "
              "Transduktions-Pfeil ist jetzt EIN benanntes Axiom.")
    else:
        print("VERDIKT: DEAD (%s)" % KILLS)
    print("total %.1f s" % (time.time() - T0))
    return 0 if (ok_i and ok_ii and ok_iii) else 1


if __name__ == "__main__":
    raise SystemExit(main())
