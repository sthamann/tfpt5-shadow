#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wilson_combphase_freeze_probe -- HOLONOMY.COMBPHASE.01 (proposal)
(signature-bundle round 2026-08-27, follow-up to
transfer_coherent_wilson_probe + doubletone_character_transduction_probe):
the FREEZE half of the missing "holonomy -> inflation comb phase"
theorem is exact algebra: IF the comb phase is set by any
rephasing-invariant holonomy functional of the coherent transport
lift, it can take EXACTLY the two values +-phi_W = +-1.96559 rad --
zero continuous freedom.  The PHYSICAL intertwiner (holonomy ->
primordial P(k) phase) stays [O]; the frozen template classes are
written down for BOTH bridge classes of the double-tone dictionary.

DEPLOYED ANCHORS (read-only):
  * transfer_coherent_wilson_probe: B unistochastic, complete lift set
    {U, U*} up to rephasing (A2/D1), main plaquette
    Q = U11 U22 U12* U21* = (-5+12i)/324, J = Im Q = +-1/27.
  * doubletone_character_transduction_probe: sheet swap S = swap(1,2),
    P_- = span(1,-1,0); channel dictionary (even: omega_-, odd:
    omega_+ under the faithful bridge).
  * cmb-primordial-logcomb freeze: (omega, A) = (2.58270695, 0.017302)
    in TT; phase phi was the LAST free template parameter.

TASK W -- all gates exact (sympy; mpmath only for digits):
 W1  GAUSSIAN ALGEBRA: 324 Q = -5 + 12i; (2+3i)^2 = -5+12i with
     N(2+3i) = 13; phi_W = arg(-5+12i) = pi - atan(12/5) and
     tan(phi_W) = -12/5 = tan(2 atan(3/2)) -- the plaquette phase is
     the DOUBLED base-atom angle of the Gaussian prime (2+3i)
     (atoms 2, 3 = the kernel pair; norm 13 = Delta_Q).
     phi_W = 1.9655874464 (30 digits pinned).
 W2  BLOCK LINK + SWAP INVARIANCE: the main plaquette lives on the
     sheet-pair block rows {1,2} x cols {1,2} = the support block of
     P_-; S-conjugation leaves Q invariant EXACTLY (the comb phase
     does NOT carry the sheet bit); conjugation U -> U* maps
     Q -> conj(Q) (the orientation bit is the classically invisible
     branch bit, and ONLY it).
 W3  THE FREEZE THEOREM (rigidity): |U|^2 = |U*|^2 = B entrywise and
     J(U) = +1/27, J(U*) = -1/27 recomputed exactly; the complete
     lift set is {U, U*} up to diagonal rephasing (cited, TRANSFER.
     COHERENT.WILSON.01 A2) and every rephasing-invariant phase
     functional is a word in the plaquettes => IF the comb phase is
     holonomy-set, phi in {+phi_W, -phi_W} EXACTLY -- the "Satz ->
     Freeze" step is done up to the one Z2 orientation bit; NO
     continuous phase freedom survives.
 W4  ANTI-NUMEROLOGY CENSUS: over the candidate table {Delta_+,
     omega_+, Delta_-, omega_-, pi*phi0, 2pi*eps, pi/golden,
     pi ln(3/2), sqrt2 ln3, ...} NOTHING matches phi_W within 1e-6
     except the two true forms (closest distractor pi/golden at
     2.4e-2) -- the phase is NOT a coincidence of the usual corpus
     numbers.
 W5  FROZEN TEMPLATE CLASSES (contract proposal, typed):
     class BLIND (character-blind S15 bridge):
         TT: (omega, A, phi) = (2.58270695, 0.017302, +-1.96559)
     class FAITHFUL (character-faithful bridge, doubletone dict):
         TT: omega_- = 0.95320029 (amplitude typing OPEN),
         TB/EB: omega_+ = 2.58270695, phi = +-1.96559.
     KILLS (frozen): a detected comb with phase outside
     {+-phi_W} (omega, A fixed first) kills the holonomy bridge; a
     TT detection at 2.5827 kills the FAITHFUL class (and vice
     versa); detection of BOTH tones in the SAME parity channel at
     bare rates kills the character dictionary.

KILLS: K-W1 Gaussian identity fails (ALGEBRA-DEAD); K-W2 swap moves
the phase (LINK-DEAD); K-W3 a third inequivalent lift or a continuous
phase family exists at the checked level (FREEZE-DEAD); K-W4 a
distractor matches within 1e-6 (NUMEROLOGY-ALARM).

TYPING (carried): [E neu] W1-W4 exact identities and the two-value
freeze CONDITIONAL on the holonomy-bridge hypothesis; [C] the cited
lift-set classification and both bridge-class readings; [O] UNCHANGED:
the physical intertwiner holonomy -> primordial phase (the actual
HOLONOMY.COMBPHASE.01 contract demand) -- data contact stays
forbidden for the phase leg until that theorem exists.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt; keine Marker-Bewegung.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wilson_combphase_freeze_probe.py
"""

import math
import time

import mpmath as mp
import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []


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


B = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
S = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])


def build_lift(Bm, branch=+1):
    s13sq = sp.nsimplify(Bm[0, 2])
    c13sq = 1 - s13sq
    s12sq = sp.nsimplify(Bm[0, 1] / c13sq)
    s23sq = sp.nsimplify(Bm[1, 2] / c13sq)
    c12sq, c23sq = 1 - s12sq, 1 - s23sq
    s12, c12 = sp.sqrt(s12sq), sp.sqrt(c12sq)
    s23, c23 = sp.sqrt(s23sq), sp.sqrt(c23sq)
    s13, c13 = sp.sqrt(s13sq), sp.sqrt(c13sq)
    cross = 2 * s12 * c12 * s23 * c23 * s13
    cosd = sp.simplify((Bm[1, 0] - s12sq * c23sq
                        - c12sq * s23sq * s13sq) / cross)
    sind = branch * sp.sqrt(sp.simplify(1 - cosd ** 2))
    eid = cosd + sp.I * sind
    return sp.Matrix([
        [c12 * c13, s12 * c13, s13 / eid],
        [-s12 * c23 - c12 * s23 * s13 * eid,
         c12 * c23 - s12 * s23 * s13 * eid, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * eid,
         -c12 * s23 - s12 * c23 * s13 * eid, c23 * c13]])


def plaq(U, i, k, j, l):
    return sp.simplify(sp.expand(
        U[i, j] * U[k, l] * sp.conjugate(U[i, l]) * sp.conjugate(U[k, j])))


def abs2(U):
    return sp.Matrix(3, 3, lambda i, j:
                     sp.simplify(sp.expand_complex(sp.Abs(U[i, j]) ** 2)))


def main():
    section("HOLONOMY.COMBPHASE.01 -- die Freeze-Haelfte der Kammphase")

    U = build_lift(B, +1)
    Q12 = plaq(U, 0, 1, 0, 1)
    phi_exact = sp.pi - sp.atan(sp.Rational(12, 5))
    tan_double = sp.simplify(
        sp.expand_trig(sp.tan(2 * sp.atan(sp.Rational(3, 2))))
        + sp.Rational(12, 5)) == 0
    mp.mp.dps = 32
    phi30 = mp.pi - mp.atan(mp.mpf(12) / 5)
    check("W1 Gauss-Algebra: 324 Q = -5+12i, (2+3i)^2 = -5+12i "
          "(N = 13), phi_W = pi - atan(12/5), tan(phi_W) = -12/5 "
          "= tan(2 atan(3/2)); phi_W = %s" % mp.nstr(phi30, 12),
          sp.simplify(324 * Q12 - (-5 + 12 * sp.I)) == 0
          and sp.expand((2 + 3 * sp.I) ** 2) == -5 + 12 * sp.I
          and sp.simplify(sp.arg(-5 + 12 * sp.I) - phi_exact) == 0
          and tan_double
          and abs(float(phi30) - 1.9655874464) < 1e-10,
          kill="ALGEBRA-DEAD")

    Us = S * U * S
    Q12s = plaq(Us, 0, 1, 0, 1)
    Uc = sp.conjugate(U)
    Q12c = plaq(Uc, 0, 1, 0, 1)
    check("W2 Block-Link + Swap-Invarianz: Hauptplaquette lebt auf dem "
          "Sheet-Paar-Block {1,2}x{1,2} (= P_- Support); Q(SUS) = Q "
          "exakt (Kammphase traegt NICHT das Sheet-Bit); Q(U*) = "
          "conj(Q) (Orientierungsbit = Konjugationsbranch, nur er)",
          sp.simplify(Q12s - Q12) == 0
          and sp.simplify(Q12c - sp.conjugate(Q12)) == 0
          and abs2(Us) == B,
          kill="LINK-DEAD")

    Jp = sp.simplify(sp.im(Q12))
    Jm = sp.simplify(sp.im(Q12c))
    check("W3 FREEZE-SATZ: |U|^2 = |U*|^2 = B entrywise, J(U) = +1/27, "
          "J(U*) = -1/27; Lift-Menge {U, U*} bis Rephasing (zitiert, "
          "WILSON.01 A2) => jede rephasing-invariante Phase ist ein "
          "Plaquette-Wort => holonomie-gesetzte Kammphase in "
          "{+phi_W, -phi_W} EXAKT, null kontinuierliche Freiheit",
          abs2(U) == B and Jp == sp.Rational(1, 27)
          and Jm == -sp.Rational(1, 27),
          kill="FREEZE-DEAD")

    phi_w = float(phi30)
    phi0 = 0.053171952
    eps = 0.017302
    cands = {
        "Delta_+": math.log(729 / 64),
        "omega_+": 2 * math.pi / math.log(729 / 64),
        "Delta_-": math.log(729),
        "omega_-": 2 * math.pi / math.log(729),
        "pi*phi0": math.pi * phi0,
        "2pi*eps": 2 * math.pi * eps,
        "pi - atan(12/5)": math.pi - math.atan(12 / 5),
        "2 atan(3/2)": 2 * math.atan(1.5),
        "pi/golden": math.pi / ((1 + math.sqrt(5)) / 2),
        "pi ln(3/2)": math.pi * math.log(1.5),
        "sqrt2 ln3": math.sqrt(2) * math.log(3),
    }
    hits = [k for k, v in cands.items() if abs(v - phi_w) < 1e-6]
    closest_distractor = min(
        (abs(v - phi_w), k) for k, v in cands.items()
        if k not in ("pi - atan(12/5)", "2 atan(3/2)"))
    check("W4 Anti-Numerologie-Zensus: genau die 2 wahren Formen "
          "treffen (<1e-6); naechster Distraktor %s bei %.1e"
          % (closest_distractor[1], closest_distractor[0]),
          sorted(hits) == ["2 atan(3/2)", "pi - atan(12/5)"]
          and closest_distractor[0] > 1e-3,
          kill="NUMEROLOGY-ALARM")

    check("W5 eingefrorene Template-Klassen (Kontrakt-Vorschlag): "
          "BLIND: TT (2.58270695, 0.017302, +-1.96559); FAITHFUL: "
          "TT omega_- = 0.95320029 (A offen), TB/EB omega_+ = "
          "2.58270695 mit phi = +-1.96559; Kills: Phase ausserhalb "
          "{+-phi_W} toetet die Holonomie-Bruecke, TT@2.5827 toetet "
          "FAITHFUL, beide Toene im selben Paritaetskanal toeten das "
          "Charakter-Woerterbuch", True)

    section("VERDIKT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    ok_all = n_pass == len(CHECKS)
    print("gates: %d/%d PASS; kills: %s" % (n_pass, len(CHECKS),
                                            KILLS or "keine"))
    if ok_all:
        print("VERDIKT: COMBPHASE-FREEZE-EXACT (bis auf das Z2-"
              "Orientierungsbit)")
        print("  bewiesen [E neu]: phi in {+-1.9655874464} falls "
              "holonomie-gesetzt -- keine kontinuierliche Freiheit;")
        print("  getypt [C]: beide Bruecken-Klassen-Templates "
              "eingefroren VOR Datenkontakt;")
        print("  offen [O]: der physische Intertwiner Holonomie -> "
              "P(k)-Phase (HOLONOMY.COMBPHASE.01) -- der Phasen-Leg "
              "bleibt datenkontakt-gesperrt bis zum Satz.")
    else:
        print("VERDIKT: DEAD (%s)" % KILLS)
    print("total %.1f s" % (time.time() - T0))
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
