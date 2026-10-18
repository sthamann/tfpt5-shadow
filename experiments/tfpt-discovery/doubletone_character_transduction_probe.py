#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""doubletone_character_transduction_probe -- OBS.DOUBLETONE.CHARACTER.01
(signature-bundle round 2026-08-27): the INTERNAL half of the missing
double-tone transduction theorem (B_even P_- == 0, B_odd P_+ == 0) is
EXACT ALGEBRA of the deployed transport, and it PINS the channel
assignment OPPOSITE to the naive proposal.

DEPLOYED ANCHORS (read-only):
  * k5_sixstep_transport_probe A0 / transfer_coherent_wilson_probe:
    single step B = (1/18)[[13,1,4],[1,13,4],[4,4,10]], T = B^6 =
    T_v221 with spec {1, (2/3)^6 = 64/729, (1/3)^6 = 1/729}.
  * ccc freeze v1 (2026-08-24, SHA 1df51166d0a2ef5b): rates
    Delta_+ = ln(729/64), Delta_- = ln 729, ratio 2.709511; defect
    classes: Z2-pair (c2, c3) = (+-1/sqrt2, 1/sqrt6) with sign(c2) =
    sheet-parity bit; anchor (0, -2/sqrt6).
  * DLX fo01 minimal model: uniform functional exactly blind to the
    64/729 tone; character channel reconstructs it (re-derived here).
  * cmb-primordial-logcomb: frozen TT search at omega_+ = 2.5827,
    Planck prior log10(omega) in [0, 2.1].

TASK A -- THE SHEET-SWAP Z2 IS A SYMMETRY OF THE DEPLOYED TRANSPORT
(all sympy-exact):
 A1  S = swap(1,2): S^2 = I, [S, B] = 0, hence [S, T] = 0 and the
     whole semigroup/generator commutes (f(B) commutes for every f).
 A2  exact eigentriple: pi ~ (1,1,1) (lambda = 1), u_odd ~ (1,-1,0)
     (lambda_B = 2/3 -> lambda_T = 64/729), u_ev ~ (1,1,-2)
     (lambda_B = 1/3 -> lambda_T = 1/729); S u_odd = -u_odd,
     S pi = pi, S u_ev = u_ev -- the corpus defect table (c2 = the
     +-1/sqrt2 sheet bit on u_odd, anchor = (0, -2/sqrt6) on u_ev)
     is exactly the character decomposition.
 A3  character projectors P_- = (I-S)/2 = u_odd u_odd^T (RANK ONE),
     P_+ = (I+S)/2 (rank 2, contains BOTH pi and u_ev).
 A4  THE ASSIGNMENT (theorem core): T P_- = (64/729) P_- exactly --
     the omega_+ = 2pi/Delta_+ = 2.5827 tone IS the odd character;
     the even sector carries {1, 1/729} -- the stationary mode AND
     the omega_- = 0.9532 tone TOGETHER.

TASK B -- THE FORBIDDEN-CHANNEL DICTIONARY:
 B1  linear readouts, PROVEN: every even functional b (bS = b)
     satisfies b T^n P_- = 0 for all n (generic symbolic b, n = 1..4)
     == "B_even P_- == 0"; every odd functional kills P_+ likewise
     == "B_odd P_+ == 0".  The requested theorem statement holds
     EXACTLY at the internal level.
 B2  fo01 re-derivation: the uniform functional (1,1,1) is even =>
     exactly blind to the 64/729 tone at every n; the character
     functional u_odd reconstructs (64/729)^n exactly.
 B3  THE MONOPOLE PIN (typed argument, machine part exact): pi lies
     in P_+.  The smooth background is OBSERVED in parity-even CMB
     spectra (TT/EE) [observational premise, typed [C]].  Hence any
     character-faithful transduction must map internal-even ->
     cosmological-even; the parity-FLIPPING bridge would place the
     stationary background in TB/EB -- excluded.  COROLLARY: the
     proposed table "omega_+ in even channels, omega_- in odd" is
     INCONSISTENT with every character-faithful bridge; the pinned
     table is the OPPOSITE: omega_- -> TT/TE/EE, omega_+ -> TB/EB.
 B4  quadratic readouts (power spectra are quadratic in fields):
     characters multiply; allowed decay-rate sets are
       EVEN channels: {0, Delta_-, 2 Delta_-, 2 Delta_+}
       ODD  channels: {Delta_+, Delta_+ + Delta_-}
     computed exactly.  EXCLUSION THEOREM (both readout classes):
     the bare rate Delta_+ NEVER appears in even channels, the bare
     Delta_- NEVER in odd channels.  Frequency dictionary:
       EVEN: omega_- = 0.9532, omega_-/2 = 0.4766, omega_+/2 = 1.2914
       ODD : omega_+ = 2.5827, 2pi/(Delta_+ + Delta_-) = 0.6963.
 B5  CONSEQUENCE FOR THE FROZEN TT SEARCH (typed, no retraction): the
     existing cmb-primordial-logcomb freeze targets omega_+ = 2.5827
     in TT -- under a character-faithful bridge that is the FORBIDDEN
     combination; the allowed TT tones are {0.9532, 0.4766, 1.2914},
     and log10(0.9532) = -0.021 sits just BELOW the published Planck
     search prior [0, 2.1].  Dated decision structure: a TT detection
     at 2.5827 refutes character-faithful transduction (supports the
     character-blind S15 bridge); a TT detection at 0.9532/1.2914
     supports the faithful bridge; TB/EB structure at 2.5827 is the
     faithful bridge's own positive channel.

KILLS (frozen, any one fires => DEAD):
  K-A  [S,B] != 0 or eigen/character table fails.   (SYMMETRY-DEAD)
  K-B  a generic even functional does NOT kill P_-. (THEOREM-DEAD)
  K-C  quadratic rate sets violate the exclusion.   (DICTIONARY-DEAD)
VERDICTS (frozen):
  INTERNAL-THEOREM-EXACT iff A1-A4, B1-B2 pass.
  CHANNEL-TABLE-PINNED iff B3-B4 pass (typed corollary).

TYPING (carried): [E neu] every exact identity (A1-A4, B1-B2, B4 rate
sets); [C] the monopole-pin premise (smooth background is parity-even)
and both bridge-class readings; [O] UNCHANGED: the physical middle
arrow internal-Z2 -> cosmological E/B parity (OBS.TRANSDUCTION.01) --
this probe proves the INTERNAL half and the conditional channel
dictionary, NOT the transduction itself.  No search is run here.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt; keine Marker-Bewegung; OBS.DOUBLETONE.CHARACTER.01 ist ein
VORSCHLAG fuer next.txt, keine Ledger-Zeile.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/doubletone_character_transduction_probe.py
"""

import math
import time

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
I3 = sp.eye(3)
T = B ** 6
LAM_ODD = sp.Rational(64, 729)          # (2/3)^6
LAM_EV = sp.Rational(1, 729)            # (1/3)^6
D_PLUS = sp.log(sp.Rational(729, 64))   # Delta_+ = 6 ln(3/2)
D_MINUS = sp.log(729)                   # Delta_- = 6 ln 3


# ==================================================================== A
def task_a():
    section("A: der Sheet-Swap Z2 ist Symmetrie des deployed Transports")
    ok1 = check("A1 S^2 = I und [S, B] = 0 exakt (=> [S, T] = 0, ganze "
                "Halbgruppe)",
                S * S == I3 and sp.simplify(S * B - B * S) == sp.zeros(3)
                and sp.simplify(S * T - T * S) == sp.zeros(3),
                kill="SYMMETRY-DEAD")

    pi_v = sp.Matrix([1, 1, 1])
    u_odd = sp.Matrix([1, -1, 0])
    u_ev = sp.Matrix([1, 1, -2])
    ok2 = check("A2 exakte Eigentripel: B pi = pi, B u_odd = (2/3) u_odd, "
                "B u_ev = (1/3) u_ev; S-Charaktere (+, -, +)",
                sp.simplify(B * pi_v - pi_v) == sp.zeros(3, 1)
                and sp.simplify(B * u_odd - sp.Rational(2, 3) * u_odd)
                == sp.zeros(3, 1)
                and sp.simplify(B * u_ev - sp.Rational(1, 3) * u_ev)
                == sp.zeros(3, 1)
                and S * pi_v == pi_v and S * u_odd == -u_odd
                and S * u_ev == u_ev,
                detail="u_odd = (1,-1,0)/sqrt2 = das Sheet-Paritaets-Bit "
                       "c2; u_ev = (1,1,-2)/sqrt6 = der Anker (0,-2/sqrt6)",
                kill="SYMMETRY-DEAD")

    p_minus = (I3 - S) / 2
    p_plus = (I3 + S) / 2
    ok3 = check("A3 P_- = (I-S)/2 = u_odd u_odd^T / 2 ist RANG 1; "
                "P_+ Rang 2 enthaelt pi UND u_ev",
                sp.simplify(p_minus - u_odd * u_odd.T / 2) == sp.zeros(3)
                and p_minus.rank() == 1 and p_plus.rank() == 2
                and sp.simplify(p_plus * pi_v - pi_v) == sp.zeros(3, 1)
                and sp.simplify(p_plus * u_ev - u_ev) == sp.zeros(3, 1),
                kill="SYMMETRY-DEAD")

    ok4 = check("A4 ZUORDNUNG: T P_- = (64/729) P_- exakt -- der "
                "omega_+ = 2.5827-Ton IST der ungerade Charakter; even "
                "traegt {1, 1/729} = Monopol + omega_-",
                sp.simplify(T * p_minus - LAM_ODD * p_minus) == sp.zeros(3),
                kill="SYMMETRY-DEAD")

    w_plus = 2 * math.pi / float(D_PLUS)
    w_minus = 2 * math.pi / float(D_MINUS)
    ok5 = check("A5 Frequenzen: omega_+ = 2.58270695, omega_- = "
                "0.95320029, ratio Delta_-/Delta_+ = 2.709511",
                abs(w_plus - 2.58270695) < 1e-8
                and abs(w_minus - 0.95320029) < 1e-8
                and abs(float(D_MINUS / D_PLUS) - 2.709511) < 1e-6)
    return ok1 and ok2 and ok3 and ok4 and ok5, p_minus, p_plus


# ==================================================================== B
def task_b(p_minus, p_plus):
    section("B: das Verbotskanal-Woerterbuch")
    p, q, r = sp.symbols("p q r", real=True)
    b_even = sp.Matrix([[p, p, q]])            # generisches gerades Funktional
    b_odd = sp.Matrix([[r, -r, 0]])            # generisches ungerades
    ok_e = all(sp.simplify(b_even * B ** n * p_minus) == sp.zeros(1, 3)
               for n in range(1, 5))
    ok_o = all(sp.simplify(b_odd * B ** n * p_plus) == sp.zeros(1, 3)
               for n in range(1, 5))
    ok1 = check("B1 SATZ (intern): b_even T^n P_- = 0 und b_odd T^n P_+ "
                "= 0 fuer generische Funktionale, n = 1..4 -- "
                "B_even P_- == 0 und B_odd P_+ == 0 exakt",
                ok_e and ok_o, kill="THEOREM-DEAD")

    u_odd = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    uni = sp.Matrix([[1, 1, 1]])
    x0 = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 6),
                    sp.Rational(1, 3)])        # Zustand mit c2 != 0
    blind = all(sp.simplify(
        (uni * T ** n * x0)[0] - (uni * T ** n * (x0 - (u_odd.T * x0)[0]
                                                  * u_odd))[0]) == 0
        for n in range(1, 4))
    recon = all(sp.simplify((u_odd.T * T ** n * u_odd)[0] - LAM_ODD ** n)
                == 0 for n in range(1, 4))
    ok2 = check("B2 fo01 re-hergeleitet: Uniform-Funktional exakt blind "
                "auf den 64/729-Ton; Charakter-Kanal rekonstruiert "
                "(64/729)^n exakt", blind and recon, kill="THEOREM-DEAD")

    ok3 = check("B3 MONOPOL-PIN: pi in P_+ (maschinell) + Praemisse "
                "[C] 'glatter Hintergrund ist parity-even' => "
                "charaktertreue Bruecke gepinnt even->even; die "
                "vorgeschlagene Tabelle (omega_+ even) braeuchte den "
                "Flip, der den Hintergrund nach TB/EB schickt -- "
                "ausgeschlossen; gepinnt: omega_- -> TT/TE/EE, "
                "omega_+ -> TB/EB",
                sp.simplify(p_plus * sp.Matrix([1, 1, 1])
                            - sp.Matrix([1, 1, 1])) == sp.zeros(3, 1))

    # quadratische Charaktere: even x even = even, odd x odd = even,
    # even x odd = odd; Raten = Summen der beteiligten Gaps
    rates = {"pi": (sp.Integer(0), +1), "ev": (D_MINUS, +1),
             "odd": (D_PLUS, -1)}
    even_rates, odd_rates = set(), set()
    for a in rates.values():
        for b2 in rates.values():
            rate = sp.simplify(a[0] + b2[0])
            (even_rates if a[1] * b2[1] == +1 else odd_rates).add(rate)
    even_expect = {sp.Integer(0), D_MINUS, sp.simplify(2 * D_MINUS),
                   sp.simplify(2 * D_PLUS)}
    odd_expect = {D_PLUS, sp.simplify(D_PLUS + D_MINUS)}
    ok4 = check("B4 quadratisches Woerterbuch: EVEN-Raten {0, D-, 2D-, "
                "2D+}, ODD-Raten {D+, D+ + D-}; AUSSCHLUSS: nacktes "
                "D+ nie in even, nacktes D- nie in odd (beide "
                "Readout-Klassen)",
                even_rates == even_expect and odd_rates == odd_expect
                and D_PLUS not in even_rates and D_MINUS not in odd_rates,
                kill="DICTIONARY-DEAD")

    freq = lambda d: 2 * math.pi / float(d)
    even_f = sorted(freq(d) for d in even_rates if d != 0)
    odd_f = sorted(freq(d) for d in odd_rates)
    def close(xs, target):
        return any(abs(x - target) < 1e-6 for x in xs)

    ok5 = check("B5 Frequenz-Tabelle + Planck-Band: EVEN {%.4f, %.4f, "
                "%.4f}, ODD {%.4f, %.4f}; log10(omega_-) = %.3f sitzt "
                "knapp UNTER dem Planck-Prior [0, 2.1]" %
                (even_f[0], even_f[1], even_f[2], odd_f[0], odd_f[1],
                 math.log10(freq(D_MINUS))),
                close(even_f, 0.95320029)                # D-  -> omega_-
                and close(even_f, 0.95320029 / 2)        # 2D- -> omega_-/2
                and close(even_f, 2.58270695 / 2)        # 2D+ -> omega_+/2
                and close(odd_f, 2.58270695)             # D+  -> omega_+
                and close(odd_f, 2 * math.pi
                          / float(D_PLUS + D_MINUS))     # D+ + D-
                and not close(even_f, 2.58270695)        # Ausschluss
                and not close(odd_f, 0.95320029)
                and math.log10(freq(D_MINUS)) < 0)
    return ok1 and ok2 and ok3 and ok4 and ok5


def main():
    section("OBS.DOUBLETONE.CHARACTER.01 -- interne Satz-Haelfte + "
            "Kanal-Woerterbuch")
    ok_a, p_minus, p_plus = task_a()
    ok_b = task_b(p_minus, p_plus)

    section("VERDIKT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("gates: %d/%d PASS; kills: %s" % (n_pass, len(CHECKS),
                                            KILLS or "keine"))
    if ok_a and ok_b:
        print("VERDIKT: INTERNAL-THEOREM-EXACT + CHANNEL-TABLE-PINNED")
        print("  bewiesen [E neu]: B_even P_- == 0, B_odd P_+ == 0 "
              "(intern, exakt);")
        print("  Zuordnung: omega_+ = ungerader Charakter, omega_- + "
              "Monopol = gerader;")
        print("  getypt [C]: Monopol-Pin => charaktertreue Bruecke "
              "liefert omega_- in TT/TE/EE, omega_+ in TB/EB -- die "
              "naive Tabelle ist GEDREHT;")
        print("  offen [O]: die physische Transduktion Z2 -> E/B "
              "(OBS.TRANSDUCTION.01) -- unberuehrt.")
    else:
        print("VERDIKT: DEAD (%s)" % KILLS)
    print("total %.1f s" % (time.time() - T0))
    return 0 if (ok_a and ok_b) else 1


if __name__ == "__main__":
    raise SystemExit(main())
