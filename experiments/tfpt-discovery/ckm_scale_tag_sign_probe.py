#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ckm_scale_tag_sign_probe -- FLAV.RGSTAB.01 CKM scale-tag sign
FROZEN SPEC v1 (2026-09-02). EXPLORATION ONLY, experiments/ only. Writes no files; no marker moves.
HYPOTHESIS. SM one-loop makes small CKM elements SMALLER at high scale
(16 pi^2 d ln|V_cb|/dt = -(3/2)(y_t^2+y_b^2), same |V_ub|,|V_td|,|V_ts|;
lambda_C, delta, PMNS RG-stable). v88 offset has the wrong sign. Source
reading of s23=0.043428 predicts |V_cb|(M_Z)~0.0488 (~+8.5s) and
|V_ub|(M_Z)~0.00424 (~+5s). Frozen |V_ub|=lambda_C^3/3=0.0037654 fits
M_Z (+0.7s) so the M_Z reading is forced. M_Z reading: record V_cb +2.0s;
pattern V_cb=lambda_C^2/(1+lambda_C)=0.041119 is -0.85s.
AXIOMS. c3=1/(8 pi); phi0=(4/3)c3+48 c3^4=0.053171952176846;
lambda_C=sqrt(phi0(1-phi0))=0.224376; M_scal/Mbar=c3^{7/2}=1.2565e-5;
Mbar=2.435323203e18 GeV -> M_scal=3.06e13 GeV. Record (v84):
s23=phi0/(1+lambda_C)=0.043428; s13=lambda_C^3/3=0.0037654;
delta=pi/3+3 lambda_C^2. v467: V_cb=lambda_C^2/(1+lambda_C)=0.041119;
V_ub unchanged. FLAV.RGSTAB.01: PMNS stable (y_tau^2~1e-4); up sector
runs through y_t^2, kappa_t~0.15.
RGE (t=ln mu, GUT g1, M_Z=91.1876): g1'=(41/10)g1^3/(16pi^2);
g2'=(-19/6)g2^3/(16pi^2); g3'=-7 g3^3/(16pi^2);
y_t'=y_t/(16pi^2)(9/2 y_t^2+3/2 y_b^2-(17/20 g1^2+9/4 g2^2+8 g3^2));
y_b'=y_b/(16pi^2)(9/2 y_b^2+3/2 y_t^2-(1/4 g1^2+9/4 g2^2+8 g3^2)).
M_Z inputs: g1=0.4626, g2=0.6520, g3=1.2210, y_t=0.99, y_b=0.0167.
scipy solve_ivp rtol 1e-8.
FROZEN DATA (verbatim): |V_cb| = 0.0418 +/- 0.0008 (PDG 2024, M_Z-scale); |V_ub| = 0.00369 +/- 0.00011 (PDG 2024); lambda_C = 0.22501 +/- 0.00068; J = 3.08e-5 +/- 0.14e-5 (repo value, v88); literature sanity band: SM one-loop |V_cb|(1e16 GeV)/|V_cb|(M_Z) in [0.85, 0.93] (Babu 1987; Balzereit-Hansmann-Mannel-Pluemper 1999; Xing-Zhang-Zhou 2008).
READINGS. M_Z: pred=frozen. Source: pred=frozen/R(M_scal). lambda_C, delta unchanged.
S1 R at 1e3,1e6,1e10,M_scal,1e16 + yt,g3. S2 R(M_scal) yt in {0.95,0.99,1.03} and y_b=0.
S3 four rows (record,pattern)x(M_Z,source). S4 J=s12 c12 s23 c23 s13 c13^2 sin(delta); v88 J=3.327e-5 to 3 digits.
S5 SIGN_INVERTED iff R(M_scal)<1 (corpus needs R>1). S6 MZ_READING_FORCED iff source |V_ub|>3s and M_Z |V_ub|<=2s else READING_UNDECIDED; plus sign; plus pulls at forced reading.
NOTE: one-loop SM RG only; TFPT's own F_transfer for quarks is not modelled here; no marker move.
GATES. G01 R(1e16) in [0.85,0.93]; G02 monotone; G03 v88 J; G04 two evals identical; G05 enum frozen.
"""
import hashlib, math, sys
from scipy.integrate import solve_ivp
FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
CHECKS = []
C3 = 1.0/(8.0*math.pi)
PHI0 = (4.0/3.0)*C3 + 48.0*C3**4
LAM = math.sqrt(PHI0*(1.0-PHI0))
MSCAL = C3**3.5 * 2.435323203e18
T0, LOOP = math.log(91.1876), 1.0/(16.0*math.pi**2)
MUS = (1e3, 1e6, 1e10, MSCAL, 1e16)
S23R, S13 = PHI0/(1.0+LAM), LAM**3/3.0
S23P, DELTA = LAM**2/(1.0+LAM), math.pi/3.0 + 3.0*LAM**2
VCB, DCB, VUB, DUB = 0.0418, 0.0008, 0.00369, 0.00011
LAM_D, LAM_S, J_D, J_S = 0.22501, 0.00068, 3.08e-5, 0.14e-5
NOTE = ("one-loop SM RG only; TFPT's own F_transfer for quarks is not "
        "modelled here; no marker move")
def gate(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name, ("  "+detail) if detail else ""))
def rhs(_t, y):
    g1, g2, g3, yt, yb, _ln = y
    return [(41/10)*g1**3*LOOP, (-19/6)*g2**3*LOOP, -7*g3**3*LOOP,
            yt*LOOP*(4.5*yt**2+1.5*yb**2-(0.85*g1**2+2.25*g2**2+8*g3**2)),
            yb*LOOP*(4.5*yb**2+1.5*yt**2-(0.25*g1**2+2.25*g2**2+8*g3**2)),
            -1.5*(yt**2+yb**2)*LOOP]
def evolve(yt, yb, mus):
    ts = [math.log(m) for m in mus]
    sol = solve_ivp(rhs, [T0, ts[-1]], [0.4626, 0.6520, 1.2210, yt, yb, 0.0],
                    rtol=1e-8, t_eval=ts)
    return tuple((float(math.exp(sol.y[5, i])), float(sol.y[3, i]),
                  float(sol.y[2, i])) for i in range(len(mus)))
def jarlskog(s23):
    return (LAM*math.sqrt(1.0-LAM**2)*s23*math.sqrt(1.0-s23**2)
            *S13*(1.0-S13**2)*math.sin(DELTA))
def payload():
    s1 = evolve(0.99, 0.0167, MUS)
    grid = ((0.95, 0.0167), (0.99, 0.0167), (1.03, 0.0167),
            (0.95, 0.0), (0.99, 0.0), (1.03, 0.0))
    return s1, tuple(evolve(yt, yb, (MSCAL,))[0][0] for yt, yb in grid), jarlskog(S23R), jarlskog(S23P)
def pulls(vcb, vub):
    return (vcb-VCB)/DCB, (vub-VUB)/DUB
def main():
    a, b = payload(), payload()
    s1, sens, jr, jp = a
    rs, rsc = [r[0] for r in s1], s1[3][0]
    pcb_mz, pub_mz = pulls(S23R, S13)
    pcb_src, pub_src = pulls(S23R/rsc, S13/rsc)
    pcb_pmz, pub_pmz = pulls(S23P, S13)
    pcb_psrc, pub_psrc = pulls(S23P/rsc, S13/rsc)
    sign = "SIGN_INVERTED" if rsc < 1.0 else "SIGN_CONSISTENT"
    reading = ("MZ_READING_FORCED" if abs(pub_src) > 3.0 and abs(pub_mz) <= 2.0
               else "READING_UNDECIDED")
    forced = ((pcb_mz, pub_mz, pcb_pmz, pub_pmz) if reading == "MZ_READING_FORCED"
              else (pcb_src, pub_src, pcb_psrc, pub_psrc))
    gate("G01 R(1e16) in [0.85, 0.93]", 0.85 <= rs[-1] <= 0.93, "R=%.4f" % rs[-1])
    gate("G02 monotone decrease", all(rs[i] > rs[i+1] for i in range(4)))
    gate("G03 v88 J reproduced", "%.3e" % jr == "3.327e-05", "J=%.3e" % jr)
    gate("G04 two evaluations byte-identical", a == b)
    gate("G05 verdict enum frozen", reading in ("MZ_READING_FORCED", "READING_UNDECIDED")
         and sign in ("SIGN_INVERTED", "SIGN_CONSISTENT"))
    print("S1 Running factors R(mu)=|V_cb|(mu)/|V_cb|(M_Z)")
    for lab, mu, (rval, yt, g3) in zip(("1e3", "1e6", "1e10", "M_scal", "1e16"), MUS, s1):
        print("  mu=%s=%.4e  R=%.4f  yt=%.4f  g3=%.4f" % (lab, mu, rval, yt, g3))
    print("S2 Sensitivity R(M_scal)")
    print("  yt=0.95/0.99/1.03 yb_nom: %.6f %.6f %.6f" % sens[:3])
    print("  yt=0.95/0.99/1.03 yb=0:    %.6f %.6f %.6f" % sens[3:])
    print("  spread_yt=%.5f  yb0_shift=%.2e" % (max(sens[:3])-min(sens[:3]), sens[4]-sens[1]))
    print("S3 Two readings x (record, pattern); source M_Z-facing=frozen/R(M_scal); lambda_C, delta RG-stable")
    plam = (LAM-LAM_D)/LAM_S
    rows = (("record", "M_Z", S23R, S13, pcb_mz, pub_mz),
            ("record", "source", S23R/rsc, S13/rsc, pcb_src, pub_src),
            ("pattern", "M_Z", S23P, S13, pcb_pmz, pub_pmz),
            ("pattern", "source", S23P/rsc, S13/rsc, pcb_psrc, pub_psrc))
    for name, rd, vcb, vub, pcb, pub in rows:
        print("  %-8s %-6s  Vcb=%.6f (%+.2f s)  Vub=%.6f (%+.2f s)  "
              "lam=%.6f (%+.2f s)  delta=%.5f rad (unchanged)"
              % (name, rd, vcb, pcb, vub, pub, LAM, plam, DELTA))
    print("S4 Jarlskog (M_Z reading)")
    print("  record  J=%.3e  pull=%+.2f  (v88 3.327e-5 gate)" % (jr, (jr-J_D)/J_S))
    print("  pattern J=%.3e  pull=%+.2f" % (jp, (jp-J_D)/J_S))
    print("S5 v88 sign check: corpus 'source 0.0434 vs M_Z 0.0408' requires R>1 "
          "(values SHRINK toward M_Z); computed R(M_scal)=%.4f  %s" % (rsc, sign))
    print("S6 VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("GATES %d/%d" % (n_pass, len(CHECKS)))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("VERDICT: %s %s  record(Vcb=%+.2f,Vub=%+.2f) pattern(Vcb=%+.2f,Vub=%+.2f)  NOTE: %s"
          % (reading, sign, forced[0], forced[1], forced[2], forced[3], NOTE))
    sys.exit(0 if n_pass == len(CHECKS) else 1)
if __name__ == "__main__":
    main()
