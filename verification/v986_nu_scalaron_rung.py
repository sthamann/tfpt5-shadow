"""v986 -- FLAV.NUSCALE.05: the SCALARON-TRACE RUNG M_R = N_fam M_scal =
3 c3^{7/2} Mbar, a structured point INSIDE the v481 window, 1.8% from the
1-loop requirement.  Candidate [C]/[N] -- NO seesaw closure, mechanism [O].

THE POINT (external master-object review, wave 2, 2026-08-28).  v481 left
the honest endpoint 'M_R free inside the PS window; required M_R = 9.3e13
GeV under the carrier normalisation y_nu = y_t [P]'; v482 declined the
integer rung c3^3 Mbar (m_3 comes out 40% low) and v488 killed the 3/5
group-theory Clebsch rescue.  The review proposes a DIFFERENT mechanism
class for a structured point: the Majorana operator rides the scalaron
(the common trace mode, M_scal = c3^{7/2} Mbar, v253/v272 anchors) times
a generation-space insertion whose third-generation slot is the family
count N_fam = 3:

    M_R = N_fam * M_scal = 3 c3^{7/2} Mbar.

  HONEST MOTIVATION (wave-3 retype, 2026-08-28): the original trace
  argument Tr_A3 I = 3 is LOOSE -- Spec(I) = {1,1,1}, and a trace of 3
  does not make 3 an eigenvalue.  The operator reading is the Q_+
  eigenvalue route Spec{1,2,3} (v10/v50/v69); the mixed insertion
  texture M_R = M_scal diag(eps, 2eps, 3) is typed
  DATA_CONSTRAINS_TEXTURE in the nu-scalaron v2 project (untextured
  Y prop I is killed x10^4; aligned diagonal Y incompatible with v270
  PMNS).  The NUMBER below is unchanged: M3 = 3 M_scal remains the
  candidate rung.  The mechanism stays [O].

  [N] 1. THE NUMBER: 3 M_scal = 9.180e13 GeV vs the v481-required
        M_R = 9.346e13 GeV (same 1-loop SM inversion, y_nu = y_t) --
        deviation -1.8%; m_3 at the candidate rung = 0.0512 eV vs the
        observed 0.0503 eV (+1.9%, well inside the >50% RG scheme
        envelope named in v482).  NOTE: the review text claimed 'about
        one percent'; the honest number at the frozen v481 inputs is 1.8.
  [E] 2. EXACT LADDER POSITION: 3 c3^{7/2} = (3 sqrt(c3)) c3^3, i.e. the
        candidate sits a factor 3 sqrt(c3) = 3/sqrt(8 pi) = 0.598413
        below the declined integer rung -- numerically 0.26% from the
        3/5 = 0.6 of the v482/v488 story.  ADJACENCY TYPED HONESTLY: the
        v488 negative killed 3/5 as an SO(10)/PS CLEBSCH; the
        scalaron-trace reading is a different mechanism class (an
        absolute scale from the gravity/scalaron sector times a
        generation-space insertion whose third slot is N_fam -- the
        Q_+ Spec{1,2,3} eigenvalue route, not Tr I = 3; texture
        DATA_CONSTRAINS_TEXTURE), and it is NOT derived here: the
        mechanism stays [O].
  [N] 3. SHARPER THAN THE DECLINED RUNG: |m_3(cand)/obs - 1| = 0.019 vs
        0.40 for c3^3 Mbar -- a 20x closer structured point.
  [E] 4. CONSISTENCY ACROSS THE SCALARON SECTOR: the same M_scal already
        carries f_a = M_scal/128 (v185) and the inflation scale (v253);
        the candidate adds no new scale atom -- it reuses the frozen
        c3^{7/2} rung times the frozen N_fam.
  [X] 5. KILL TEST (inherited and sharpened): Sigma m_nu (NO, m1 ~ 0) at
        the candidate rung = 0.059 eV; a robust cosmological bound below
        0.059 eV, or a measured m_3 pulling the required M_R more than
        ~5% away from 9.18e13 GeV under the same premise chain, kills
        the candidate.

HONEST SCOPE (firewall): [P] y_nu = y_t stays a NAMED premise (v481); the
1-loop SM running is the frozen v481 tool (scheme envelope >50% per
v482); the scalaron-trace mechanism is a typed hypothesis, not a
derivation -- this row does NOT close FLAV.NUSCALE, does not move the
window candidate, and makes no PMNS claim.  It registers a structured,
falsifiable point inside the window.
"""
import math

from tfpt_constants import check, summary, reset, c3, Mbar, N_fam

MZ = 91.1876
V_EW = 246.22
YT_MZ = math.sqrt(2) * 162.5 / V_EW
LAM_MZ = 0.130
A_INV_MZ = (59.01, 29.59, 8.44)
M3_OBS = 0.0503                       # eV (NuFIT NO, v481 frozen input)
DM2_21 = 7.42e-5                      # eV^2
C3 = float(c3)
MBARF = float(Mbar)


def run_sm_up(mu_hi, n=20000):
    """the frozen v481 1-loop SM runner (verbatim tool, read-only)."""
    g1, g2, g3 = [math.sqrt(4 * math.pi / a) for a in A_INV_MZ]
    yt, lam = YT_MZ, LAM_MZ
    h = math.log(mu_hi / MZ) / n
    k = 1 / (16 * math.pi ** 2)
    b = (41 / 10, -19 / 6, -7)
    I_alpha = 0.0
    for _ in range(n):
        I_alpha += (-3 * g2 * g2 + 6 * yt * yt + lam) * h
        dg1 = k * b[0] * g1 ** 3
        dg2 = k * b[1] * g2 ** 3
        dg3 = k * b[2] * g3 ** 3
        dyt = k * yt * (4.5 * yt ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2
                        - (17 / 20) * g1 ** 2)
        dlam = k * (24 * lam ** 2 - 6 * yt ** 4 + 12 * lam * yt ** 2
                    - 3 * lam * (3 * g2 ** 2 + 0.6 * g1 ** 2)
                    + 0.375 * (2 * g2 ** 4 + (g2 ** 2 + 0.6 * g1 ** 2) ** 2))
        g1 += h * dg1
        g2 += h * dg2
        g3 += h * dg3
        yt += h * dyt
        lam += h * dlam
    return yt, math.exp(-I_alpha / (16 * math.pi ** 2))


def m3_pred_eV(MR):
    yt, R = run_sm_up(MR)
    return (yt * V_EW / math.sqrt(2)) ** 2 / MR * R * 1e9


def run():
    reset()
    print("v986  FLAV.NUSCALE.05: the scalaron-trace rung "
          "M_R = N_fam M_scal = 3 c3^{7/2} Mbar (candidate)")

    M_scal = C3 ** 3.5 * MBARF
    MR_cand = N_fam * M_scal

    lo, hi = 1e13, 1e16
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if m3_pred_eV(mid) > M3_OBS:
            lo = mid
        else:
            hi = mid
    MR_req = math.sqrt(lo * hi)
    dev = MR_cand / MR_req - 1
    check("THE NUMBER [N]: M_R = 3 M_scal = %.3e GeV vs the v481-required "
          "%.3e GeV (same frozen 1-loop inversion, y_nu = y_t [P]) -- "
          "deviation %.1f%% (the review said 'about 1%%'; honest value "
          "1.8), inside the PS window and the >50%% v482 RG envelope"
          % (MR_cand, MR_req, 100 * dev),
          abs(dev) < 0.03 and 4.2e13 < MR_cand < 2.4e15)

    m3_cand = m3_pred_eV(MR_cand)
    check("m_3 AT THE CANDIDATE [N]: %.4f eV vs observed %.4f eV "
          "(ratio %.4f, +1.9%%)" % (m3_cand, M3_OBS, m3_cand / M3_OBS),
          abs(m3_cand / M3_OBS - 1) < 0.03)

    ladder = 3 * math.sqrt(C3)
    check("EXACT LADDER POSITION [E]: 3 c3^{7/2} = (3 sqrt c3) c3^3 with "
          "3 sqrt(c3) = 3/sqrt(8 pi) = %.6f -- 0.26%% from the 3/5 of "
          "the v482/v488 story; v488 killed 3/5 as an SO(10) CLEBSCH, "
          "this is a DIFFERENT mechanism class (generation-blind "
          "scalaron trace), itself [O]" % ladder,
          abs(ladder - 3 / math.sqrt(8 * math.pi)) < 1e-15
          and abs(ladder / 0.6 - 1) < 0.003)

    m3_old = m3_pred_eV(C3 ** 3 * MBARF)
    check("SHARPER THAN THE DECLINED RUNG [N]: |m3/obs - 1| = %.3f at the "
          "candidate vs %.3f at c3^3 Mbar (v482 declined) -- a ~20x "
          "closer structured point" % (abs(m3_cand / M3_OBS - 1),
                                       abs(m3_old / M3_OBS - 1)),
          abs(m3_cand / M3_OBS - 1) < 0.1 * abs(m3_old / M3_OBS - 1))

    f_a = M_scal / 128
    check("SCALARON-SECTOR CONSISTENCY [E]: the same M_scal = c3^{7/2} "
          "Mbar = %.3e GeV already carries f_a = M_scal/128 = %.3e GeV "
          "(v185) -- the candidate reuses the frozen rung times the "
          "frozen N_fam = %d, no new scale atom"
          % (M_scal, f_a, N_fam),
          2.0e11 < f_a < 2.8e11 and N_fam == 3)

    summ = M3_OBS + math.sqrt(DM2_21)
    check("KILL TEST [X]: Sigma m_nu (NO, m1 ~ 0) = %.4f eV at the "
          "candidate; a robust bound below 0.059 eV or a required-M_R "
          "shift beyond ~5%% kills it" % summ,
          0.055 < summ < 0.062)

    check("FIREWALL (scope): y_nu = y_t stays a NAMED premise [P]; the "
          "scalaron-trace mechanism is a typed hypothesis [O], not a "
          "derivation (the Tr I = 3 motivation is loose -- Spec(I) = "
          "{1,1,1}; the operator reading is Q_+ Spec{1,2,3}, texture "
          "DATA_CONSTRAINS_TEXTURE); FLAV.NUSCALE does NOT close; the "
          "v481 window candidate and the v488 negative are untouched; "
          "no PMNS claim",
          True)

    return summary("v986 scalaron-trace rung M_R = 3 c3^{7/2} Mbar: "
                   "structured candidate 1.8% inside the window")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
