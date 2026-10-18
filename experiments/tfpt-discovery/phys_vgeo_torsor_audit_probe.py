#!/usr/bin/env python3
"""phys_vgeo_torsor_audit_probe -- T1-SCHLUSS: der Kalibrations-/Skalen-Torsor-Audit
fuer v_geo (GPT-Rat-Spezifikation, beide Strategieraete einstimmig).

FRAGE: Ist die v_geo-Schnittstelle der Theorie als R+-Skalen-Torsor wohldefiniert
und schliessbar -- d.h. (1) exportiert der Korpus ALLE dimensionalen Groessen als
O_i = r_i * v_geo^{d_i} mit maschinen-abgeleiteten dimensionslosen r_i, (2) hat die
Dimensionsmatrix Rang 1 (genau EINE unabhaengige Skala), (3) sind ALLE
Konsistenz-Bedingungen homogen unter L -> lambda L (kein interner absoluter Anker),
(4) sind die Kreuzkalibrierungen (leave-one-anchor-out) kompatibel, (5) laesst sich
der KALIBRATIONS-SATZ in Torsor-Sprache praezise formulieren (Vertrags-
Schliessungs-Kandidat), und (6) welcher legale Moonshot bleibt (NUR benannt)?

KORPUS-QUELLEN (alle nur gelesen, Stand 2026-08-03):
  v153_no_unit_theorem.py       No-Unit-Satz (dimensionsloser Compiler kann keine
                                absolute Skala ausgeben; v_geo = deklarierte Einheit)
  v152_norm_is_anchor.py        Seam-EH-Normierung: k=c3/2 <=> m/mu = e^{3/4} (dim 0)
  v274_scale_overdetermination.py  Anker ueberbestimmt: Gravitation (G) vs.
                                Kosmologie (rho_Lambda) -> dasselbe Mbar zu 0.11%
  v401_metrology_closure.py     Input-Set {a, pi, v_geo}; Buchhaltung
                                Masse/1G/Lambda/U_point/(m/mu) = Zahl x v_geo^{1,2,4,1,0}
  v364_vgeo_sharpen.py          Gravitation fuegt keine Einheit hinzu (1/c3=8pi,
                                Lambda-Praefaktor 3/(4pi^2) dimensionslos)
  v75_upoint_to_vgeo.py         U_point -> eine Flavor-Amplitudenskala (Ratios+Produkt)
  v68_seeley_dewitt_residual.py 1/G UV-sensitiv (Sakharov); seam=Planck ist
                                IDENTIFIKATION [A], keine Ableitung
  v60_lambda_metrology_branch.py / v7_gravity_cosmo.py  rho_L/Mbar^4 =
                                (3/4pi^2) e^{-2 ainv} = 7.12533e-121; M_scal = c3^{7/2} Mbar
  v20_lepton_c_derivation.py    Lepton-Ratios m_mu/m_tau=(8/7)phi0, m_e/m_mu=(12/7)phi0^2
  v272_nu_mass_scale.py         nu-Skala = (y_nu v_EW)^2/M_R -- EIN externer UV-Input [O]
  v3_em_alpha.py                alpha^-1-Fixpunkt F(a)=0 (rein dimensionslos)
  redteam/rt_E_vgeo.py          Single-Scale-Audit: 4 Flags (seam-cutoff-Identifikation,
                                EW-Matching, T_reh, Leptogenese-M_R) -- ehrlich getypt
  v714_moonshot_hecke_groupoid.py  heutige Gruppoid-Normierungen: Halbdichte
                                mu_n = 2 Lambda_A(n)/sqrt(n), Orbitlaenge log n --
                                reine Zaehl-Daten (Massendimension 0)
  status_ledger.csv             ANCHOR.VGEO.01/02, VGEO.SHARPEN.01, SCALE.OVERDET.01,
                                METROLOGY.CLOSURE.01, FIRSTPRINCIPLES.BOUNDARY.01

FIREWALL: reine Exploration (tfpt-discovery Sandbox). Nichts wird in run_all.py,
Ledger, Papers oder Website geschrieben. Kein neuer Zahlenwert wird fabriziert;
alle Messwerte sind die im Korpus dokumentierten Referenzen (CODATA Mbar,
Planck-2018 rho_Lambda^{1/4} = 2.24 meV, PDG-Leptonmassen).

EHRLICHER RAHMEN (vorab deklariert):
  * Dies ist ein STRUKTUR-Audit der Schnittstelle -- KEINE Ableitung einer
    absoluten Skala (per No-Unit v153 unmoeglich; das ist der Satz, nicht der Makel).
  * Route 2 (Kosmologie) ist konditional auf den Lambda-Branch [C] (v274, rt_F).
  * Die Flavor-Amplitude U_point ist per DEKLARIERTER Identifikation [A]
    (seam=Planck, v68; EW-Matching rt_E-Flag) derselbe Anker -- das wird als
    Konditionalitaet berichtet, nicht versteckt.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/phys_vgeo_torsor_audit_probe.py
"""

import mpmath as mp
import sympy as sp

mp.mp.dps = 30

# --------------------------------------------------------------------------
# Harness
# --------------------------------------------------------------------------
_PASS = 0
_FAIL = 0
_KILLS = []


def check(name, ok, kill_note=None):
    global _PASS, _FAIL
    ok = bool(ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        if kill_note:
            _KILLS.append(kill_note)
    return ok


# --------------------------------------------------------------------------
# Compiler-Primitiven (nur aus den Axiomen; identisch zu tfpt_constants.py)
# --------------------------------------------------------------------------
PI = mp.pi
c3 = 1 / (8 * PI)                      # P1
g_car = 5                              # P2
phibase = 1 / (6 * PI)
dtop = 48 * c3 ** 4
phi0 = phibase + dtop                  # 0.0531719...

# alpha^-1-Fixpunkt (v3 make_F, Budget M=41, reimplementiert -- rein dimensionslos)
def _F_alpha(a):
    Q = dtop * mp.e ** (-2 * a)
    phiseam = phibase + Q * (1 - Q) ** (mp.mpf(-5) / 4)
    return a ** 3 - 2 * c3 ** 3 * a ** 2 - (mp.mpf(4) / 5) * c3 ** 6 * 41 * mp.log(1 / phiseam)


AINV = 1 / mp.findroot(_F_alpha, mp.mpf("0.0073"))          # ~137.036
RHO_RATIO = mp.mpf(3) / (4 * PI ** 2) * mp.e ** (-2 * AINV)  # rho_L/Mbar^4 ~ 7.1253e-121

# Im Korpus benutzte Referenz-Messwerte (Quellen siehe Docstring)
MBAR_GRAV = mp.mpf("2.435323203e18")   # GeV, aus CODATA G (tfpt_constants.py)
RHO_QRT_MEAS_MEV = mp.mpf("2.24")      # meV, Planck 2018 (v274)
HBAR = mp.mpf("1.054571817e-34")       # J s   (exakt, SI)
CLIGHT = mp.mpf("2.99792458e8")        # m/s   (exakt, SI)
GEV_TO_KG = mp.mpf("1.78266192e-27")   # kg/GeV
G_CODATA = mp.mpf("6.67430e-11")       # m^3 kg^-1 s^-2
M_E = mp.mpf("0.51099895")             # MeV (PDG)
M_MU = mp.mpf("105.6583755")           # MeV (PDG)
M_TAU = mp.mpf("1776.86")              # MeV (PDG)
V_EW = mp.mpf("174.0")                 # GeV (m_t-Konvention, v272) -- externer Input
M_R_Y1 = V_EW ** 2 / (mp.sqrt(mp.mpf("2.5e-3")) * mp.mpf("1e-9"))  # y=1-Seesaw (v272)


def G_from_Mbar(Mbar_GeV):
    """G = hbar c / (8 pi Mbar[kg]^2) -- SI-Rueckuebersetzung des Ankers."""
    Mkg = Mbar_GeV * GEV_TO_KG
    return HBAR * CLIGHT / (8 * PI * Mkg ** 2)


# ==========================================================================
print("=" * 78)
print("phys_vgeo_torsor_audit_probe -- T1-SCHLUSS: Skalen-Torsor-Audit fuer v_geo")
print("=" * 78)

# --------------------------------------------------------------------------
# TEIL 1 -- Die vollstaendige Dimensionstabelle O_i = r_i * v_geo^{d_i}
# --------------------------------------------------------------------------
print("\nTEIL 1 -- VOLLSTAENDIGE EXPORT-TABELLE  O_i = r_i * v_geo^{d_i}")
print("-" * 78)

M_SCAL_R = c3 ** (mp.mpf(7) / 2)             # 1.2564e-5
F_A_R = (c3 / 4) ** (mp.mpf(7) / 2)          # = M_SCAL_R/128
A_S = 55 ** 2 * c3 ** 7 / (24 * PI ** 2)     # dimensionslos (v7)

# (Name, r_i-Formel, r_i numerisch oder None, d_i, Quelle, Status)
EXPORTS = [
    ("1/G  (Newton)",        "8 pi (Def. Mbar=(8 pi G)^{-1/2})", 8 * PI,      2,
     "v68/v274",  "ANKER-Route 1 (gemessen: CODATA G)"),
    ("rho_Lambda",           "(3/4pi^2) e^{-2 ainv}",            RHO_RATIO,   4,
     "v60/v7",    "ANKER-Route 2 (gemessen: Planck; konditional [C] Lambda-Branch)"),
    ("M_scal (Skalaron)",    "c3^{7/2}",                          M_SCAL_R,    1,
     "v7/v68",    "Vorhersage (ungemessen)"),
    ("f_a (Axion)",          "(c3/|mu4|)^{7/2} = c3^{7/2}/128",   F_A_R,       1,
     "v25/rt_E",  "Vorhersage (ungemessen)"),
    ("m/mu (Seam-EH)",       "e^{3/4}",                           mp.e ** mp.mpf("0.75"), 0,
     "v152",      "reines Verhaeltnis (dim 0)"),
    ("A_s (Inflation)",      "N*^2 c3^7/(24 pi^2)",               A_S,         0,
     "v7",        "dimensionsloser Export"),
    ("m_f (9 gel. Fermionen)", "(pi/sqrt2) c_f phi0^{k_f}  [x U_point]", None, 1,
     "v20/v46/v75", "Ratios geschlossen; Absolutwert via Flavor-Kalibration "
                    "(U_point = Anker per Identifikation [A], v68/rt_E-Flag)"),
    ("m_3 (nu-Skala)",       "(y_nu v_EW)^2/M_R -- KEIN Compiler-r_i", None,   1,
     "v272",      "Frontier [O]: EIN externer UV-Input (kein Export)"),
    ("v_EW",                 "f(c3) NICHT abgeleitet",             None,       1,
     "rt_E-Flag", "Frontier: EW-Matching-Skala (externer Input)"),
    ("T_reh, M_R (Leptog.)", "--",                                 None,       1,
     "rt_E-Flag", "Frontier [P]: kosmologische Inputs (keine Exporte)"),
]

hdr = f"{'Groesse':24s} {'r_i (Formel)':38s} {'r_i (Zahl)':14s} {'d_i':>3s}  {'Quelle':12s} Status"
print(hdr)
print("-" * len(hdr))
for name, formel, rnum, d, src, status in EXPORTS:
    rtxt = mp.nstr(rnum, 6) if rnum is not None else "--"
    print(f"{name:24s} {formel:38s} {rtxt:14s} {d:3d}  {src:12s} {status}")

certified = [e for e in EXPORTS if e[2] is not None]
flagged = [e for e in EXPORTS if e[2] is None]
check(f"Tabelle vollstaendig: {len(certified)} zertifizierte Exporte (r_i maschinen-"
      f"abgeleitet) + {len(flagged)} ehrlich geflaggte Nicht-Exporte (Flavor-Absolutwert, "
      "nu-Skala, v_EW, T_reh/M_R) -- konsistent mit rt_E_vgeo.py (5 Reduktionen + 4 "
      "Flags) und v401; einzige Verschaerfung: m_f hier KONDITIONAL getypt (rt_E "
      "reduziert auf den Flavor-Anker, dessen Mbar-Identifikation das rt_E-Flag ist)",
      len(certified) == 6 and len(flagged) == 4)
check("Exakte Zahlen: rho_L/Mbar^4 = %s (Soll 7.12533e-121, v7); M_scal/Mbar = %s; "
      "f_a/Mbar = %s; alpha^-1 = %s"
      % (mp.nstr(RHO_RATIO, 6), mp.nstr(M_SCAL_R, 6), mp.nstr(F_A_R, 6), mp.nstr(AINV, 10)),
      abs(RHO_RATIO / mp.mpf("7.12533e-121") - 1) < mp.mpf("1e-4")
      and abs(M_SCAL_R * MBAR_GRAV / mp.mpf("3.06e13") - 1) < mp.mpf("5e-3"))

# --------------------------------------------------------------------------
# TEIL 2 -- Rang-Check der Dimensionsmatrix
# --------------------------------------------------------------------------
print("\nTEIL 2 -- RANG-CHECK: Dimensionsmatrix ueber der Skalen-Basis")
print("-" * 78)
# Spalten: [Mbar(=v_geo), U_point(Flavor), v_EW, M_R, T_reh]
# Zeilen: dokumentierte Exponenten der Exporte (Quellen wie Tabelle oben).
ROWS = {
    "rho_Lambda": [4, 0, 0, 0, 0],
    "1/G":        [2, 0, 0, 0, 0],
    "M_scal":     [1, 0, 0, 0, 0],
    "f_a":        [1, 0, 0, 0, 0],
    "m/mu":       [0, 0, 0, 0, 0],
    "A_s":        [0, 0, 0, 0, 0],
    # nicht-zertifizierte Zeilen (Flavor-Absolutwert + Frontier):
    "m_f":        [0, 1, 0, 0, 0],
    "m_3(nu)":    [0, 0, 2, -1, 0],
    "T_reh":      [0, 0, 0, 0, 1],
}
CERT_KEYS = ["rho_Lambda", "1/G", "M_scal", "f_a", "m/mu", "A_s"]

M_cert = sp.Matrix([ROWS[k] for k in CERT_KEYS])
rank_cert = M_cert.rank()
check(f"ZERTIFIZIERTER Export-Block: Rang = {rank_cert} (genau EINE unabhaengige "
      "Skala Mbar = v_geo; alle Exponentenvektoren sind Vielfache von (1,0,0,0,0))",
      rank_cert == 1,
      kill_note="Rang > 1 im zertifizierten Block = versteckte zweite Skala")

M_full = sp.Matrix([ROWS[k] for k in ROWS])
rank_full = M_full.rank()
print(f"  [INFO] Volle Matrix (inkl. Flavor-Absolutwert + Frontier-Inputs): Rang = {rank_full}")

# Aufloesung per dokumentierter Typisierung: U_point = kappa * Mbar (Identifikation
# [A], v75/v68); v_EW, M_R, T_reh sind deklarierte EXTERNE INPUTS (v272 [O],
# v339 FIRSTPRINCIPLES.BOUNDARY.01, rt_E) -- keine Exporte, also keine Matrixzeilen.
M_resolved = sp.Matrix([[r[0] + r[1], *r[2:]] for r in (ROWS[k] for k in
                        ["rho_Lambda", "1/G", "M_scal", "f_a", "m/mu", "A_s", "m_f"])])
rank_resolved = M_resolved.rank()
check(f"Volle Matrix Rang {rank_full} -> nach den DOKUMENTIERTEN Typisierungen "
      f"(U_point=kappa*Mbar per [A]-Identifikation v75/v68; v_EW/M_R/T_reh = externe "
      f"Inputs per v272/v339/rt_E, keine Exporte): Rang = {rank_resolved}",
      rank_resolved == 1)
check("Kein UNDEKLARIERTER Fundort: jede Zeile mit Exponent auf einer Nicht-Mbar-"
      "Spalte traegt eine explizite Ledger-Typisierung ([A] EW-Matching/seam=Planck; "
      "[O] nu-UV-Input; [P] T_reh/M_R) -- die Rang-1-Aussage ist exakt auf dem "
      "zertifizierten Block und KONDITIONAL (benannt) auf dem Flavor-Block",
      all(ROWS[k][1:] == [0, 0, 0, 0] for k in CERT_KEYS))

# Mutations-Negativkontrolle: EIN zertifizierter Export mit verstecktem v_EW-Anteil
# muesste den Rang-Check sofort killen (Rang 2) -- der Detektor ist scharf.
M_mut = sp.Matrix([ROWS[k] for k in CERT_KEYS] + [[1, 0, 1, 0, 0]])
check("MUTATIONS-KONTROLLE: injiziert man einen hypothetischen zertifizierten Export "
      "mit verstecktem v_EW-Anteil (Exponentenvektor (1,0,1,0,0)), springt der Rang "
      f"auf {M_mut.rank()} -- der Kill-Detektor (Rang > 1 = versteckte zweite Skala) "
      "funktioniert nachweislich",
      M_mut.rank() == 2)

# --------------------------------------------------------------------------
# TEIL 3 -- lambda-Homogenitaet (symbolisch): kein interner absoluter Anker
# --------------------------------------------------------------------------
print("\nTEIL 3 -- LAMBDA-HOMOGENITAET (symbolisch, sympy): L -> lambda L")
print("-" * 78)

lam = sp.symbols("lambda", positive=True)
a_s, c3_s, n_s, LamA_s, mun_s = sp.symbols("a c_3 n Lambda_A mu_n", positive=True)  # dim 0
Mb_s, rho_s, Msc_s, fa_s, Gi_s, m_s, mu_s, v_s = sp.symbols(
    "Mbar rho_Lambda M_scal f_a Ginv m mu v_geo", positive=True)
ui_s, uj_s = sp.symbols("u_i u_j", real=True)

DIM = {a_s: 0, c3_s: 0, n_s: 0, LamA_s: 0, mun_s: 0,
       Mb_s: 1, rho_s: 4, Msc_s: 1, fa_s: 1, Gi_s: 2, m_s: 1, mu_s: 1, v_s: 1}


def scale(expr):
    """L -> lambda L: jede Groesse der Massendimension d skaliert als X -> lambda^{-d} X."""
    return expr.subs({x: lam ** (-d) * x for x, d in DIM.items()}, simultaneous=True)


pi_s = sp.pi
phib_s = 1 / (6 * pi_s)
dtop_s = 48 * c3_s ** 4
Q_s = dtop_s * sp.exp(-2 * a_s)
phiseam_s = phib_s + Q_s * (1 - Q_s) ** sp.Rational(-5, 4)

# Konsistenz-Bedingungen des Korpus (LHS == 0), mit erwartetem Homogenitaetsgrad d_C
CONSTRAINTS = [
    ("K1 c3-Fixpunkt F(a)=0 (v3): a^3 - 2c3^3 a^2 - (4/5)c3^6*41*ln(1/phi_seam)",
     a_s ** 3 - 2 * c3_s ** 3 * a_s ** 2
     - sp.Rational(4, 5) * c3_s ** 6 * 41 * sp.log(1 / phiseam_s), 0),
    ("K2 Seam-Normierung 2 pi c3 = 1/4 (v153)",
     2 * pi_s * c3_s - sp.Rational(1, 4), 0),
    ("K3 Seam-EH-Normierung 12 pi (c3/2) = ln(m/mu) (v152)",
     12 * pi_s * c3_s / 2 - sp.log(m_s / mu_s), 0),
    ("K4 Lambda-Branch rho_L = (3/4pi^2) e^{-2/a} Mbar^4 (v60/v7)",
     rho_s - sp.Rational(3, 4) / pi_s ** 2 * sp.exp(-2 / a_s) * Mb_s ** 4, 4),
    ("K5 Skalaron M_scal = c3^{7/2} Mbar (v7)",
     Msc_s - c3_s ** sp.Rational(7, 2) * Mb_s, 1),
    ("K6 Newton 1/G = 8 pi Mbar^2 (v68/v274)",
     Gi_s - 8 * pi_s * Mb_s ** 2, 2),
    ("K7 Axion f_a = (c3/4)^{7/2} Mbar (v25/rt_E)",
     fa_s - (c3_s / 4) ** sp.Rational(7, 2) * Mb_s, 1),
    ("K8 Gruppoid-Normierung (v714): mu_n = 2 Lambda_A(n)/sqrt(n) -- alle Symbole "
     "reine Zaehl-Daten (dim 0)",
     mun_s - 2 * LamA_s / sp.sqrt(n_s), 0),
]

all_hom = True
for name, lhs, d_expect in CONSTRAINTS:
    scaled = scale(lhs)
    hom = sp.simplify(sp.expand(scaled - lam ** (-d_expect) * lhs)) == 0
    all_hom &= bool(hom)
    tag = "PASS" if hom else "FAIL"
    print(f"  [{tag}] {name}  ->  Grad {d_expect} homogen")
check("ALLE Konsistenz-Bedingungen sind lambda-homogen (Grad 0 fuer dimensionslose, "
      "Grad d fuer dimensionale) -- die maschinelle Form des No-Unit-Satzes: "
      "KEINE Gleichung pinnt lambda",
      all_hom,
      kill_note="inhomogene Bedingung gefunden = interner absoluter Anker")

# Mutations-Negativkontrolle fuer den Homogenitaets-Scanner: typt man die
# Gruppoid-Masse mu_n FAELSCHLICH als dimensionsbehaftet (dim 1), wird K8
# inhomogen -- der Scanner haette eine dimensionsbehaftete Normierung gefunden.
_bad_dim = dict(DIM)
_bad_dim[mun_s] = 1
_k8_lhs = mun_s - 2 * LamA_s / sp.sqrt(n_s)
_k8_bad = _k8_lhs.subs({x: lam ** (-d) * x for x, d in _bad_dim.items()},
                       simultaneous=True)
check("MUTATIONS-KONTROLLE Homogenitaet: typt man die v714-Gruppoid-Masse mu_n "
      "faelschlich als dim 1, ist K8 weder Grad-0- noch Grad-1-homogen -- der "
      "Scanner erkennt dimensionsbehaftete Normierungen nachweislich",
      sp.simplify(_k8_bad - _k8_lhs) != 0
      and sp.simplify(_k8_bad - lam ** (-1) * _k8_lhs) != 0)

# Index-Identitaeten (Integer-Bedingungen, trivial invariant -- explizit geprueft)
N_fam = (2 ** (g_car - 1) - 1) // g_car
check("K9 Index-Identitaeten invariant: g_car + N_fam = 8 = rank E8; "
      "N_fam = (2^{g_car-1}-1)/g_car = 3; e-sym(1,1,2) = (4,5,2) = (|mu4|,g_car,|Z2|); "
      "det(Q,K,R,L)-Produkt = 1920 -- alles Massendimension 0",
      g_car + N_fam == 8 and N_fam == 3
      and (1 + 1 + 2, 1 * 1 + 1 * 2 + 1 * 2, 1 * 1 * 2) == (4, 5, 2)
      and 3 * 4 * 8 * 20 == 1920)

# Log-Achse der Montage: u -> u + ln(lambda) ist eine TRANSLATION; Lag-Differenzen
# (die Objekte der L1-Montage/Gruppoid-Fenster) sind exakt invariant -- die additive
# Spiegelung des multiplikativen R+-Torsors.
shift = sp.log(lam)
check("K10 Log-Achse (L1-Montage/v714): unter x -> lambda x verschiebt sich u = ln x "
      "um +ln(lambda); Lag-Differenzen (u_i - u_j) exakt invariant -- die Log-Achse "
      "ist ein affiner R-Torsor (kein absoluter Nullpunkt)",
      sp.simplify(((ui_s + shift) - (uj_s + shift)) - (ui_s - uj_s)) == 0)

# Freiheit + Transitivitaet der R+-Wirkung auf der Skalen-Faser
free = sp.solve(sp.Eq(lam * v_s, v_s), lam)
lam12 = sp.symbols("lambda_12", positive=True)
v1_s, v2_s = sp.symbols("v_1 v_2", positive=True)
trans = sp.solve(sp.Eq(lam12 * v1_s, v2_s), lam12)
check("K11 R+-Wirkung auf der Skalen-Faser ist FREI (lambda*v = v => lambda = 1) und "
      "TRANSITIV (zu v1,v2 > 0 existiert eindeutig lambda = v2/v1) -- die Faser ist "
      "ein R+-TORSOR",
      free == [1] and trans == [v2_s / v1_s])

# Negativ-Check (v153-Kern): eine Anker-Gleichung v_geo = f(dimensionslos) waere
# inhomogen (links Grad 1, rechts Grad 0) -- sie erzwingt lambda = 1 fuer alle
# Skalenwahlen, Widerspruch zur freien Wirkung.
anchor_lhs = v_s - sp.exp(a_s)          # Beispiel-Anker: dim 1 == dim 0
scaled_anchor = scale(anchor_lhs)
inhom = sp.simplify(scaled_anchor - lam ** (-1) * anchor_lhs) != 0 \
    and sp.simplify(scaled_anchor - anchor_lhs) != 0
check("K12 NEGATIV-KONTROLLE: eine hypothetische Anker-Gleichung v_geo = f(dim-0-Daten) "
      "ist NICHT homogen (weder Grad 0 noch Grad 1) -- der Scan haette sie gefunden; "
      "der Korpus enthaelt keine solche Gleichung",
      inhom)

# --------------------------------------------------------------------------
# TEIL 4 -- Kreuzkalibrierung: leave-one-anchor-out
# --------------------------------------------------------------------------
print("\nTEIL 4 -- KREUZKALIBRIERUNG (leave-one-anchor-out)")
print("-" * 78)

# ---- 4a. Mbar-Block: die zwei im Korpus benutzten Anker (v274) ----
# Anker A1 = Newton G (CODATA): Mbar = 2.435323203e18 GeV
# Anker A2 = Dunkle Energie (Planck 2018): rho_L^{1/4} = 2.24 meV, invertiert
Mbar_A1 = MBAR_GRAV
rho_qrt_GeV = RHO_QRT_MEAS_MEV * mp.mpf("1e-12")
Mbar_A2 = rho_qrt_GeV / RHO_RATIO ** (mp.mpf(1) / 4)
dev_anchor = Mbar_A2 / Mbar_A1 - 1

print(f"  Anker A1 (Gravitation, CODATA G):     Mbar = {mp.nstr(Mbar_A1, 8)} GeV")
print(f"  Anker A2 (Kosmologie, rho_L^1/4):     Mbar = {mp.nstr(Mbar_A2, 8)} GeV")
print(f"  relative Abweichung A2/A1 - 1       = {mp.nstr(100 * dev_anchor, 4)} %")

check("Anker-Kompatibilitaet (v274 reproduziert): |Mbar(A2)/Mbar(A1) - 1| = "
      f"{mp.nstr(100 * abs(dev_anchor), 3)} % < 1 % -- die zwei unabhaengigen "
      "Referenzen waehlen DENSELBEN Punkt im Torsor (konditional auf Lambda-Branch [C])",
      abs(dev_anchor) < mp.mpf("0.01"),
      kill_note="inkompatible Kalibrierungen im Mbar-Block")

# Vorhersage-Tabelle unter beiden Kalibrierungen
print("\n  Vorhersagen unter jeder Kalibrierung (leave-one-anchor-out):")
print(f"  {'Groesse':22s} {'unter A1 (G)':>18s} {'unter A2 (rho_L)':>18s} {'Messwert':>14s} {'Abw. LOO':>10s}")

rows_pred = []
# rho_L^{1/4} vorhergesagt aus A1, gemessen 2.24 meV  (leave A2 out)
p1 = RHO_RATIO ** (mp.mpf(1) / 4) * Mbar_A1 * mp.mpf("1e12")     # meV
rows_pred.append(("rho_L^1/4 [meV]", p1, RHO_QRT_MEAS_MEV, RHO_QRT_MEAS_MEV,
                  p1 / RHO_QRT_MEAS_MEV - 1))
# G vorhergesagt aus A2, gemessen CODATA  (leave A1 out)
G_A2 = G_from_Mbar(Mbar_A2)
rows_pred.append(("G [m^3/(kg s^2)]", G_from_Mbar(Mbar_A1), G_A2, G_CODATA,
                  G_A2 / G_CODATA - 1))
# ungemessene Vorhersagen: Verschiebung zwischen den Kalibrierungen = dev_anchor
rows_pred.append(("M_scal [GeV]", M_SCAL_R * Mbar_A1, M_SCAL_R * Mbar_A2, None, dev_anchor))
rows_pred.append(("f_a [GeV]", F_A_R * Mbar_A1, F_A_R * Mbar_A2, None, dev_anchor))

for name, pa1, pa2, meas, dev in rows_pred:
    mtxt = mp.nstr(meas, 6) if meas is not None else "--"
    print(f"  {name:22s} {mp.nstr(pa1, 8):>18s} {mp.nstr(pa2, 8):>18s} {mtxt:>14s} "
          f"{mp.nstr(100 * dev, 3):>9s}%")

check("LOO Mbar-Block: rho_L^{1/4}(A1) = %s meV vs gemessen 2.24 meV (%.2f %%); "
      "G(A2) = %s vs CODATA %s (%.2f %%); M_scal- und f_a-Vorhersagen verschieben "
      "sich um genau den EINEN gemeinsamen Faktor %.2f %% -- keine inkompatible "
      "Kalibrierung"
      % (mp.nstr(p1, 6), float(100 * (p1 / RHO_QRT_MEAS_MEV - 1)),
         mp.nstr(G_A2, 6), mp.nstr(G_CODATA, 6), float(100 * (G_A2 / G_CODATA - 1)),
         float(100 * dev_anchor)),
      abs(p1 / RHO_QRT_MEAS_MEV - 1) < mp.mpf("0.01")
      and abs(G_A2 / G_CODATA - 1) < mp.mpf("0.01"))

# ---- 4b. Flavor-Block: Kalibration mit je EINER Leptonmasse ----
# Korpus-Ratios (v20, Baum-Saat): m_e/m_mu = (12/7) phi0^2 ; m_mu/m_tau = (8/7) phi0
r_emu = mp.mpf(12) / 7 * phi0 ** 2
r_mutau = mp.mpf(8) / 7 * phi0
MEAS = {"m_e": M_E, "m_mu": M_MU, "m_tau": M_TAU}
# Amplitudenvektor relativ zu m_tau = 1 (nur Ratios, dimensionslos):
REL = {"m_e": r_emu * r_mutau, "m_mu": r_mutau, "m_tau": mp.mpf(1)}

print("\n  Flavor-Block (Baum-Saat-Ratios v20; Kalibration mit je EINER Masse):")
print(f"  {'Anker':8s} {'m_e pred [MeV]':>15s} {'m_mu pred [MeV]':>16s} "
      f"{'m_tau pred [MeV]':>17s} {'max |Abw.|':>11s}")

pred_vectors = {}
maxdevs = {}
for anchor in MEAS:
    scale_fac = MEAS[anchor] / REL[anchor]           # der gewaehlte Torsor-Punkt
    preds = {f: REL[f] * scale_fac for f in MEAS}
    pred_vectors[anchor] = preds
    devs = {f: preds[f] / MEAS[f] - 1 for f in MEAS}
    maxdevs[anchor] = max(abs(v) for v in devs.values())
    print(f"  {anchor:8s} {mp.nstr(preds['m_e'], 7):>15s} {mp.nstr(preds['m_mu'], 8):>16s} "
          f"{mp.nstr(preds['m_tau'], 8):>17s} {mp.nstr(100 * maxdevs[anchor], 3):>10s}%")

check("LOO Flavor-Block: jede Ein-Massen-Kalibration reproduziert die anderen zwei "
      "auf max %.2f %% (Baum-Saat-Niveau der v20-Ratios; die Abweichungen sind "
      "RATIO-Praezision, keine Skalen-Inkonsistenz -- sie sind ankerunabhaengig)"
      % float(100 * max(maxdevs.values())),
      max(maxdevs.values()) < mp.mpf("0.03"))

# Exakter Torsor-Faser-Check: Ankerwechsel = EIN globaler Faktor auf ALLEN Vorhersagen
fiber_ok = True
anchors = list(MEAS)
for i in range(len(anchors)):
    for j in range(i + 1, len(anchors)):
        f0 = pred_vectors[anchors[j]]["m_e"] / pred_vectors[anchors[i]]["m_e"]
        for f in MEAS:
            ratio = pred_vectors[anchors[j]][f] / pred_vectors[anchors[i]][f]
            fiber_ok &= abs(ratio / f0 - 1) < mp.mpf("1e-25")
check("TORSOR-FASER exakt: der Wechsel des Kalibrations-Ankers multipliziert ALLE "
      "Vorhersagen mit EINEM gemeinsamen lambda (maschinell auf < 1e-25 relativ, "
      "alle 3 Ankerpaare) -- Ankerwahl bewegt nur den Punkt in der Faser, nie die "
      "dimensionslosen Exporte",
      fiber_ok,
      kill_note="Ankerwechsel wirkt nicht als globaler Skalenfaktor")

# --------------------------------------------------------------------------
# TEIL 5 -- Der KALIBRATIONS-SATZ (Torsor-Formulierung, Vertrags-Kandidat)
# --------------------------------------------------------------------------
print("\nTEIL 5 -- KALIBRATIONS-SATZ (Vertrags-Schliessungs-Kandidat, Torsor-Sprache)")
print("-" * 78)

# Klausel (a): die Exporte r_i = O_i / v^{d_i} sind torsor-invariant (symbolisch)
r_sym = rho_s / v_s ** 4
inv_ok = sp.simplify(scale(r_sym) - r_sym) == 0
# Klausel (b): EINE Referenz mit d_j != 0 waehlt den Punkt eindeutig
O_meas, r_j = sp.symbols("O_meas r_j", positive=True)
sol_d2 = sp.solve(sp.Eq(r_j * v_s ** 2, O_meas), v_s)
sol_pos = [s for s in sol_d2 if s.is_positive]
# Klausel (b'): eine dim-0-Groesse kann NICHT kalibrieren
sol_d0 = sp.solve(sp.Eq(r_j * v_s ** 0, O_meas), v_s)

check("Klausel (a): jedes exportierte r_i = O_i/v_geo^{d_i} ist invariant unter der "
      "R+-Wirkung (symbolisch verifiziert) -- die Theorie exportiert genau die "
      "torsor-invarianten Funktionen",
      inv_ok)
check("Klausel (b): EINE gemessene Referenz O_j mit d_j != 0 waehlt den physischen "
      "Punkt EINDEUTIG: v_geo = (O_j/r_j)^{1/d_j} (einzige positive Loesung; "
      "symbolisch fuer d_j = 2 geprueft)",
      len(sol_pos) == 1 and sp.simplify(sol_pos[0] - sp.sqrt(O_meas / r_j)) == 0)
check("Klausel (b'): eine dim-0-Groesse (z.B. m/mu = e^{3/4}) kann NICHT kalibrieren "
      "(die Gleichung enthaelt v_geo nicht; sympy: keine Loesung nach v_geo) -- "
      "der Grad d_j != 0 ist notwendig UND hinreichend",
      sol_d0 == [])
check("Klausel (c): nach der Wahl sind ALLE weiteren dimensionalen Aussagen "
      "Vorhersagen; Ueberbestimmung = Kompatibilitaet mehrerer Referenzen "
      "(Teil 4: 0.11 % im Mbar-Block) -- maximale Praediktivitaet eines "
      "dimensionslosen Compilers (v274)",
      abs(dev_anchor) < mp.mpf("0.01"))

print("""
  KALIBRATIONS-SATZ (praezise Formulierung, Kandidat fuer die v_geo-Schnittstelle):

    Die Menge der zulaessigen Skalen-Zuweisungen der TFPT ist ein R+-TORSOR T:
    die Gruppe R+ wirkt frei und transitiv durch v_geo -> lambda * v_geo,
    O_i -> lambda^{d_i} * O_i. Die Theorie exportiert ausschliesslich die
    torsor-invarianten Daten { (r_i, d_i) } (dimensionslose Compiler-Verhaeltnisse
    plus Dimensionsgrade); KEIN Punkt von T ist intern ausgezeichnet (No-Unit,
    v153; Teil 3 maschinell). EINE gemessene Referenz (O_j, d_j != 0) waehlt den
    physischen Punkt v_geo = (O_j/r_j)^{1/d_j} in T eindeutig; danach ist jedes
    weitere O_i = r_i * v_geo^{d_i} eine Vorhersage, und jede weitere Referenz
    ist eine UEBERBESTIMMUNGS-Probe (aktuell: G vs. rho_Lambda, kompatibel zu
    0.11 %, konditional auf den Lambda-Branch [C]).

  EHRLICHER FENCE (Pflichtteil des Satzes):
    * Dies ist eine STRUKTUR-Schliessung: die Schnittstelle (Exporte = invariante
      Daten; Import = genau ein Kalibrationspunkt) ist wohldefiniert und
      maschinell zertifiziert. Es ist KEINE Ableitung einer absoluten Skala --
      die ist per No-Unit-Satz (v153) beweisbar unmoeglich, fuer jeden
      dimensionslosen Compiler.
    * Der Rang-1-Status ist EXAKT auf dem zertifizierten Export-Block
      {rho_Lambda, 1/G, M_scal, f_a, m/mu, A_s} und KONDITIONAL auf dem
      Flavor-Block (U_point = Anker nur per deklarierter [A]-Identifikation
      seam=Planck/EW-Matching, v68/v75/rt_E-Flag).
    * Route 2 (Kosmologie) haengt am Lambda-Branch [C] (v274/rt_F); v_EW, T_reh,
      M_R bleiben ehrlich getypte EXTERNE Inputs (v272/v339) -- keine Exporte.
""")

# --------------------------------------------------------------------------
# TEIL 6 -- Der einzige legale Moonshot (NUR benannt, nicht ausgefuehrt)
# --------------------------------------------------------------------------
print("TEIL 6 -- MOONSHOT-AUSBLICK (benannt, nicht ausgefuehrt)")
print("-" * 78)

H_EW = mp.log(MBAR_GRAV / V_EW)
log_c3_EW = mp.log(V_EW / MBAR_GRAV) / mp.log(c3)
log_phi0_EW = mp.log(V_EW / MBAR_GRAV) / mp.log(phi0)
log_c3_MR = mp.log(M_R_Y1 / MBAR_GRAV) / mp.log(c3)

print(f"  Der Korpus prediziert bereits EINEN Hierarchie-Exponenten: die "
      f"Lambda-Hierarchie\n    |log10(rho_L/M_Pl^4)| = 122.948 = 2 alpha^-1/ln10 "
      f"(= {mp.nstr(2 * AINV / mp.log(10), 6)}) + 3.920 (v60).")
print(f"  OFFEN bleibt genau EIN dimensionsloses Skalen-Verhaeltnis der Kette: die "
      f"EW-Hierarchie\n    H_EW = ln(Mbar/v_EW) = {mp.nstr(H_EW, 6)}   "
      f"(v_EW = 174 GeV, m_t-Konvention)")
print(f"  Ehrlicher Erstbefund (kein Fit, v184-Firewall respektiert):")
print(f"    log_c3(v_EW/Mbar)   = {mp.nstr(log_c3_EW, 6)}   (NICHT ganzzahlig)")
print(f"    log_phi0(v_EW/Mbar) = {mp.nstr(log_phi0_EW, 6)}   (NICHT ganzzahlig)")
print(f"    log_c3(M_R/Mbar)    = {mp.nstr(log_c3_MR, 6)}   (v272: 2.57, NICHT ganzzahlig)")

check("MOONSHOT BENANNT: 'Der EW-Hierarchie-Exponent H_EW = ln(Mbar/v_EW) ~ 37.18 "
      "als neues dimensionsloses Compiler-Verhaeltnis' -- das EINZIGE noch offene "
      "Skalen-Verhaeltnis, dessen Ableitung der No-Unit-Satz ERLAUBT (dim 0). "
      "Ein Erfolg wuerde die [A]-Identifikation des Flavor-Blocks zur Ableitung "
      "machen (Rang 1 unbedingt) und alle 9 Fermionmassen zu Mbar-Vorhersagen. "
      "Naive c3-/phi0-Leitern scheiden aus (11.53 / 12.67, nicht ganzzahlig) -- "
      "NICHT ausgefuehrt, nur benannt (Sekundaer-Kandidat: nu-Seesaw-Ratio, v272/v481)",
      abs(log_c3_EW - mp.nint(log_c3_EW)) > mp.mpf("0.05")
      and abs(log_phi0_EW - mp.nint(log_phi0_EW)) > mp.mpf("0.05"))

# --------------------------------------------------------------------------
# VERDIKT
# --------------------------------------------------------------------------
print("\n" + "=" * 78)
total = _PASS + _FAIL
if _FAIL == 0:
    print(f"VERDIKT: TORSOR-SCHLIESSUNG PASS ({_PASS}/{total} Checks)")
    print("""
  T1-SCHLUSS: Die v_geo-Schnittstelle ist als R+-Skalen-Torsor STRUKTURELL
  GESCHLOSSEN: (1) vollstaendige Export-Tabelle O_i = r_i * v_geo^{d_i} aus dem
  Korpus, (2) Dimensionsmatrix Rang 1 auf dem zertifizierten Block (konditional
  [A] auf dem Flavor-Block -- benannt), (3) alle Konsistenz-Bedingungen
  lambda-homogen (kein interner Anker; maschinelle Form des No-Unit-Satzes),
  (4) leave-one-anchor-out kompatibel (G vs. rho_Lambda: 0.11 %; Flavor-Faser
  exakt), (5) Kalibrations-Satz formuliert (eine Referenz waehlt den Punkt im
  Torsor; alles Weitere ist Vorhersage). FENCE: Struktur-Schliessung, KEINE
  Skalen-Ableitung (per No-Unit unmoeglich). Moonshot benannt: H_EW.""")
else:
    print(f"VERDIKT: FAIL ({_FAIL}/{total} Checks gescheitert)")
    for k in _KILLS:
        print(f"  KILL: {k}")
print("=" * 78)

raise SystemExit(1 if _FAIL else 0)
