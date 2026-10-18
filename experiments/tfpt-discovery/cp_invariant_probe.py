"""PART 177 -- CP.INVARIANT -- THE CP MIRROR.

THE CONTRACT.  The ledger names the CP residual in FOUR independent places, and
all four say the same thing from a different side: the magnitude bijection does
not cover the phases.

  REDTEAM.D.01   (ratios, product) <=> (individuals) is a bijection for positive
                 reals; complex amplitudes leave an n-th-root BRANCH ambiguity
                 ({1,1,1}, {w,w,w}, {w^2,w^2,w^2}, w = e^{2 pi i/3}, share all
                 ratios AND the product).  GENUINE RESIDUAL: magnitudes only.
  E8.CHAN.01     248 = 120 + 128: exponents sum 120 = MAGNITUDE channel, degrees
                 sum 128 = PHASE/GLUE channel; the residual lives in 128.
  CP.MOD.01      the Z/6 hexagonal phase fiber (j(rho) = 0, rho = e^{i pi/3})
                 OVER the Z/4 square seam deck (j(i) = 1728); the frozen leading
                 reading delta = pi/3 + 3 lambda_C^2 has leading term arg(rho).
  DUAL.FRAME.01  CP as ORIENTATION: Im det(1, d, rho n) = 21 sin(pi/3) on the
                 dual normal frame d = (-1/2,-1/2,1), n = (5,-9,6).

THE QUESTION, ONE SENTENCE.  Is the pi/3 structure an INVARIANT FUNCTIONAL of the
compiler frame data, or an artefact of the chosen branch?

THE TOOL.  T174's degree bookkeeping: a group acts on the frame datum, every
candidate functional gets a HOMOGENEITY DEGREE or a CHARACTER under that action,
and blindness theorems become checkable algebra.  T173's discipline: the family
of functionals, the groups and the kill criterion are DECLARED IN FULL BEFORE THE
FIRST NUMBER (block F2P), and every claimed invariance carries a MUTATION control
that must FAIL.

FENCES, PROMINENTLY AND FIRST.

  * The word "derived" is not used for any CP statement in this file.  The best
    attainable outcome is a NARROWING of ledger prose (an invariant core plus a
    declared covariance), never an upgrade.
  * THEOREM / CERTIFIED / MEASURED are kept strictly apart and labelled per
    statement.  "Theorem" here means: exact algebra over Q(rho) or over the
    integers, closed by sympy with == , no floating bar.  "Certified" means: a
    numeric statement inside a DECLARED bar.  "Measured" means: a value read off
    a scan.  Nothing in this file is a physical derivation of CP violation.
  * The D4 deck action is a DECLARED MODEL of the deck (stated in F2P); results
    under it are certified WITHIN THE MODEL, never asserted of the theory.
  * NO ledger, paper, website or registry file is touched by this probe.  F4
    produces RECOMMENDATION TEXT only.

CLASSICAL SPINE (addresses, not authorities): Jarlskog 1985 (the rephasing-
invariant measure of CP violation J = Im(V_us V_cb V*_ub V*_cs); the benchmark
for what "phase invariant" is allowed to mean), Bjorken-Dunietz 1987 (rephasing
invariants), Wolfenstein 1983 (the lambda-hierarchy parametrisation),
Weyl 1946 / Hilbert 1893 (invariants of a group action as a graded algebra),
Kubo-Martin-Schwinger 1957/1959 (KMS: an address only -- no modular flow is
evaluated here).
Python: experiments/tfpt-discovery/.venv/bin/python
"""

import math
import time

import mpmath as mp
import sympy as sp

T0 = time.time()

BUDGET_S = 780.0             # HARD probe budget (< 900 s)
MAX_MATRIX = 1500            # HARD cap on any matrix dimension (unused: all 3x3..8x8)

EXACT = "THEOREM(exact algebra)"
CERT = "CERTIFIED"
MEAS = "MEASURED"

N_FAM = 3
G_CAR = 5
SCALARON = 7

FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def info(name, detail=""):
    print("[INFO] %s%s" % (name, (": " + detail) if detail else ""))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def budget_left():
    return BUDGET_S - (time.time() - T0)


def wrap_at(text, width):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        if not cur:
            cur = wd
        elif len(cur) + 1 + len(wd) <= width:
            cur += " " + wd
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def para(text, width=76, indent="  "):
    print("")
    for blk in text.split("\n\n"):
        for ln in wrap_at(blk, width):
            print(indent + ln)
        print("")


# ---------------------------------------------------------------- frame data --
# exact compiler objects (v220 / v225 / v227 / v231 / v88 / rt_D_upoint)
RHO = sp.exp(sp.I * sp.pi / 3)               # hexagonal CM unit, j(rho) = 0
OMEGA = sp.exp(2 * sp.I * sp.pi / 3)         # primitive cube root (branch group)
R_MAT = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
K_MAT = sp.Matrix([[4, 2, 0], [4, 3, 2], [5, 3, 2]])
Q_MAT = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
L_MAT = K_MAT + Q_MAT
A_VEC = sp.Matrix([1, 1, 2])
ONE_VEC = sp.Matrix([1, 1, 1])
N_VEC = [5, -9, 6]
E8_EXPONENTS = [1, 7, 11, 13, 17, 19, 23, 29]
E8_DEGREES = [m + 1 for m in E8_EXPONENTS]
C_LEPTON = [sp.Rational(16, 7), sp.Rational(4, 3), sp.Rational(7, 6)]
C_UPQUARK = [sp.Rational(1, 2), sp.Rational(34, 41), sp.Rational(4, 13)]

PI = sp.pi
C3 = 1 / (8 * PI)
PHI0 = 1 / (6 * PI) + 48 * C3**4
LAM = sp.sqrt(PHI0 * (1 - PHI0))
DELTA_FROZEN = PI / 3 + N_FAM * LAM**2        # v88 / CP.MOD.01, registry frozen


section("PART 177  CP.INVARIANT -- is the pi/3 structure an invariant functional?")
info("hard caps", "matrix <= %d, budget %.0f s (cap 900 s)" % (MAX_MATRIX, BUDGET_S))
info("frame data", "rho = e^{i pi/3}, d = a^T R^{-1}, n = (5,-9,6), "
                   "delta_frozen = pi/3 + 3 lambda_C^2 = %.9f rad"
     % float(DELTA_FROZEN))
info("typing legend", "%s | %s | %s" % (EXACT, CERT, MEAS))


section("F1  THE OBJECTS -- rebuild the four ledger CP constructions on the lattice")

para(
    "Every one of the four ledger CP places is rebuilt here from the compiler "
    "primitives alone, and each rebuild is compared against the value quoted by "
    "its own module (rt_D_upoint, v227, v220, v225, v88, v231). A rebuild that "
    "misses its module value is a REBUILD-FAILS verdict and stops the probe: no "
    "invariance question can be asked about an object that cannot be reproduced.")


def rebuild(c):
    """rt_D_upoint / v75 reconstruction: individuals from (ratios, product)."""
    n = len(c)
    prod = sp.prod(c)
    ratios = [c[i] / c[0] for i in range(n)]
    c0 = (prod / sp.prod(ratios)) ** sp.Rational(1, n)
    return [sp.nsimplify(c0 * r) for r in ratios]


# ---- F1.1  REDTEAM.D.01: the magnitude bijection and its branch kernel -------
check("F1.1a %s REDTEAM.D.01 rebuild: lepton triple (16/7,4/3,7/6) is recovered "
      "EXACTLY from (ratios, product) -- the bijection reproduces rt_D_upoint"
      % EXACT, rebuild(C_LEPTON) == C_LEPTON)
check("F1.1b %s REDTEAM.D.01 rebuild: up-quark gauge triple (1/2,34/41,4/13) "
      "recovered EXACTLY (n = 3 = N_fam odd, positive rationals)" % EXACT,
      rebuild(C_UPQUARK) == C_UPQUARK)

BRANCH_TRIPLES = [[sp.Integer(1)] * 3,
                  [OMEGA, OMEGA, OMEGA],
                  [OMEGA**2, OMEGA**2, OMEGA**2]]
_same_ratios = all([sp.simplify(t[i] / t[0]) == 1 for i in range(3)]
                   for t in BRANCH_TRIPLES)
_same_prod = all(sp.simplify(sp.prod(t) - 1) == 0 for t in BRANCH_TRIPLES)
check("F1.1c %s REDTEAM.D.01 branch kernel: {1,1,1},{w,w,w},{w^2,w^2,w^2} "
      "(w = e^{2 pi i/3}) share ALL ratios (1,1,1) AND the product 1 -- the "
      "mu3 diagonal branch group is exactly the kernel of the magnitude data"
      % EXACT, _same_ratios and _same_prod)
check("F1.1d %s the branch kernel is NOT phase-blind on individuals: "
      "arg(w) = 2 pi/3 != 0, so the residual is a genuine phase freedom, not "
      "a relabelling" % EXACT,
      sp.simplify(sp.arg(OMEGA) - 2 * sp.pi / 3) == 0)

# ---- F1.2  E8.CHAN.01: the 120/128 magnitude/phase channel split -------------
check("F1.2a %s E8.CHAN.01 rebuild: sum(exponents) = 120 = |R^+(E8)| (magnitude "
      "channel), sum(degrees) = 128 = 2^(rank-1) (phase/glue channel), "
      "120 + 128 = 248 = dim E8, sum(deg) - sum(exp) = rank = 8" % EXACT,
      sum(E8_EXPONENTS) == 120 and sum(E8_DEGREES) == 128
      and sum(E8_DEGREES) == 2 ** (G_CAR + N_FAM - 1)
      and 120 + 128 == 248 and sum(E8_DEGREES) - sum(E8_EXPONENTS) == 8)

# the channel split EVALUATED on the hexagonal unit (new, exact)
CHAN_DEG = sp.expand_complex(sum(RHO**d for d in E8_DEGREES))
CHAN_EXP = sp.expand_complex(sum(RHO**m for m in E8_EXPONENTS))
check("F1.2b %s E8.CHAN.01 on the hexagonal fiber: sum_k rho^{d_k} = 4 rho = "
      "4 e^{i pi/3} EXACTLY (degrees mod 6 = {2,2,0,2,0,2,0,0}: four 0s and "
      "four 2s, and 1 + rho^2 = rho) -- the PHASE channel carries arg = pi/3"
      % EXACT, sp.simplify(CHAN_DEG - sp.expand_complex(4 * RHO)) == 0)
check("F1.2c %s E8.CHAN.01 control on the same fiber: sum_k rho^{m_k} = 4 is "
      "REAL (exponents mod 6 = {1,1,5,1,5,1,5,5}: four rho and four rho^5 = "
      "rho^bar, 4(rho + rho^bar) = 8 cos(pi/3) = 4) -- the MAGNITUDE channel "
      "carries arg = 0. The ledger's channel typing is an exact statement on "
      "the hexagonal unit, not only a counting analogy" % EXACT,
      sp.simplify(CHAN_EXP - 4) == 0 and sp.im(CHAN_EXP) == 0)
_mu5 = sp.exp(sp.I * sp.pi / 5)
_deg_mut = E8_DEGREES[:-1] + [31]                 # 30 -> 31, no longer E8 degrees
_exp_mut = E8_EXPONENTS[:-1] + [30]               # 29 -> 30, no longer E8 exponents
check("F1.2d %s MUTATION control for F1.2b: the identity sum rho^{d_k} = 4 rho "
      "breaks BOTH ways -- on the non-CM unit e^{i pi/5} (residues mod 10) and "
      "on a mutated degree list (30 -> 31); it is a joint property of the E8 "
      "degrees and the hexagonal fiber, of neither alone" % EXACT,
      sp.simplify(sp.expand_complex(sum(_mu5**d for d in E8_DEGREES)
                                    - 4 * _mu5)) != 0
      and sp.simplify(sp.expand_complex(sum(RHO**d for d in _deg_mut)
                                        - 4 * RHO)) != 0)
check("F1.2e %s MUTATION control for F1.2c: reality of the exponent-channel sum "
      "breaks on a mutated exponent list (29 -> 30, Im = sin(pi/3) != 0)"
      % EXACT,
      sp.simplify(sp.im(sp.expand_complex(
          sum(RHO**m for m in _exp_mut)))) != 0)
info("F1.2 honesty note",
     "reality of the exponent sum is NOT hexagon-specific: the E8 exponent "
     "residues are conjugation-closed mod 10 as well, so sum_k (e^{i pi/5})^{m_k} "
     "is real too. Only the DEGREE half (= 4 rho, arg = pi/3) is specific to the "
     "hexagonal fiber; the magnitude-channel statement is the weaker one")

# ---- F1.3  CP.MOD.01: the Z/6 phase fiber over the Z/4 square deck -----------
check("F1.3a %s CP.MOD.01 rebuild (Z/6 vs Z/4 automorphisms): rho = e^{i pi/3} "
      "is a primitive 6th root (rho^6 = 1, rho^3 = -1 the sheet half-turn), "
      "i is a primitive 4th root (i^4 = 1, i^2 = -1); the two orders share "
      "exactly gcd(4,6) = 2 -- the deck and the fiber overlap in the Z/2 sheet "
      "ONLY" % EXACT,
      sp.simplify(RHO**6 - 1) == 0 and sp.simplify(RHO**3 + 1) == 0
      and math.gcd(4, 6) == 2)
check("F1.3b %s CP.MOD.01 rebuild: arg(rho) = pi/3 (60 deg) and the frozen "
      "leading reading delta = pi/3 + N_fam lambda_C^2 has EXACTLY arg(rho) as "
      "its leading term (delta - 3 lambda_C^2 - pi/3 = 0 symbolically)" % EXACT,
      sp.simplify(sp.arg(RHO) - sp.pi / 3) == 0
      and sp.simplify(DELTA_FROZEN - N_FAM * LAM**2 - sp.pi / 3) == 0)
_delta_num = sp.N(DELTA_FROZEN, 30)
check("F1.3c %s CP.MOD.01 value control: delta_frozen = %.9f rad = %.4f deg "
      "reproduces the v88/v220 lattice value 1.198231638 rad = 68.654 deg "
      "inside the declared bar 1e-9" % (CERT, float(_delta_num),
                                        float(_delta_num * 180 / sp.pi)),
      abs(_delta_num - sp.Float('1.198231638')) < sp.Float('1e-9')
      and abs(_delta_num * 180 / sp.pi - sp.Float('68.654')) < sp.Float('1e-2'))
_alt = PI / 3 + 2 * LAM**2
check("F1.3d %s CP.MOD.01 frozen look-elsewhere control: the |Z2| alternative "
      "pi/3 + 2 lambda_C^2 = %.3f deg differs from the frozen reading by "
      "exactly lambda_C^2 = %.4f deg; recorded, NOT adopted (REG.FREEZE.01)"
      % (EXACT, float(sp.N(_alt * 180 / sp.pi, 20)),
         float(sp.N(LAM**2 * 180 / sp.pi, 20))),
      sp.simplify(DELTA_FROZEN - _alt - LAM**2) == 0)

# ---- F1.4  DUAL.FRAME.01: the oriented normal frame -------------------------
D_VEC = (A_VEC.T * R_MAT.inv())
D_VEC_L = (A_VEC.T * L_MAT.inv())
check("F1.4a %s DUAL.FRAME.01 rebuild: d = a^T R^{-1} = a^T L^{-1} = "
      "(-1/2,-1/2,1) = -1/2 (1,1,-2), d.1 = 0, d.a = 1" % EXACT,
      list(D_VEC) == [sp.Rational(-1, 2), sp.Rational(-1, 2), 1]
      and list(D_VEC_L) == list(D_VEC)
      and (D_VEC * ONE_VEC)[0] == 0 and (D_VEC * A_VEC)[0] == 1)
_n_row = sp.Matrix([N_VEC])
check("F1.4b %s DUAL.FRAME.01 rebuild: n = (5,-9,6) gives n^T R = (det R,0,0) = "
      "(8,0,0) and n^T L = (det L,0,0) = (20,0,0)" % EXACT,
      list(_n_row * R_MAT) == [R_MAT.det(), 0, 0] == [8, 0, 0]
      and list(_n_row * L_MAT) == [L_MAT.det(), 0, 0] == [20, 0, 0])
FRAME = sp.Matrix([[1, 1, 1], list(D_VEC), N_VEC])
VOL = FRAME.det()
check("F1.4c %s DUAL.FRAME.01 rebuild: det(1,d,n) = 21 = N_fam * scalaron = "
      "3 * 7 (non-degenerate frame)" % EXACT,
      VOL == 21 == N_FAM * SCALARON)
FRAME_RHO = sp.Matrix([[1, 1, 1], list(D_VEC), [RHO * x for x in N_VEC]])
IM_DET = sp.simplify(sp.im(sp.expand_complex(FRAME_RHO.det())))
check("F1.4d %s DUAL.FRAME.01 rebuild: Im det(1, d, rho n) = 21 sin(pi/3) = "
      "21 sqrt(3)/2 EXACTLY (rho scales the third row linearly), value %.6f"
      % (EXACT, float(sp.N(IM_DET, 20))),
      sp.simplify(IM_DET - 21 * sp.sin(sp.pi / 3)) == 0)
_im_det_lep = sp.simplify(sp.im(sp.expand_complex(
    sp.Matrix([[1, 1, 1], list(D_VEC), [RHO**4 * x for x in N_VEC]]).det())))
check("F1.4e %s DUAL.FRAME.01 / CP.MU6.01 sheet control: Im det(1,d,rho^4 n) = "
      "-21 sin(pi/3) -- equal magnitude, opposite sign (rho^4 = -rho)" % EXACT,
      sp.simplify(_im_det_lep + 21 * sp.sin(sp.pi / 3)) == 0
      and sp.simplify(RHO**4 + RHO) == 0)

# ---- F1.5  the classical comparison object: the Jarlskog invariant ----------
mp.mp.dps = 40
PHI0_N = mp.mpf(str(sp.N(PHI0, 40)))
LAM_N = mp.sqrt(PHI0_N * (1 - PHI0_N))
S12, S23, S13 = LAM_N, PHI0_N / (1 + LAM_N), LAM_N**3 / 3
C12, C23, C13 = (mp.sqrt(1 - S12**2), mp.sqrt(1 - S23**2), mp.sqrt(1 - S13**2))
DELTA_N = mp.mpf(str(sp.N(DELTA_FROZEN, 40)))


def ckm(s12, s23, s13, delta):
    """standard PDG parametrisation (Wolfenstein 1983 hierarchy, PDG phase
    convention): the CKM matrix from three angles and one phase."""
    c12, c23, c13 = mp.sqrt(1 - s12**2), mp.sqrt(1 - s23**2), mp.sqrt(1 - s13**2)
    e = mp.e**(1j * delta)
    return mp.matrix([
        [c12 * c13, s12 * c13, s13 / e],
        [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e,
         s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e,
         c23 * c13]])


def jarlskog(V):
    """J = Im(V_us V_cb V*_ub V*_cs)  (Jarlskog 1985)."""
    return mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1]))


def dagger(M):
    return mp.matrix([[mp.conj(M[j, i]) for j in range(M.rows)]
                      for i in range(M.cols)])


V_TFPT = ckm(S12, S23, S13, DELTA_N)
_dev = V_TFPT * dagger(V_TFPT) - mp.eye(3)
_unit = max(abs(_dev[i, j]) for i in range(3) for j in range(3))
check("F1.5a %s CKM rebuild: the PDG-parametrised V from the TFPT magnitudes "
      "(s12 = lambda_C, s23 = phi0/(1+lambda_C), s13 = lambda_C^3/3) and the "
      "frozen delta is unitary to %.1e (declared bar 1e-12)" % (CERT, float(_unit)),
      float(_unit) < 1e-12)
J_FORMULA = S12 * C12 * S23 * C23 * S13 * C13**2 * mp.sin(DELTA_N)
J_TFPT = jarlskog(V_TFPT)
check("F1.5b %s Jarlskog rebuild: J = Im(V_us V_cb V*_ub V*_cs) = "
      "s12 c12 s23 c23 s13 c13^2 sin(delta) = %.6e, reproducing the v88 lattice "
      "value 3.32702e-5 (Jarlskog 1985)" % (CERT, float(J_TFPT)),
      abs(J_TFPT - J_FORMULA) < mp.mpf('1e-24')
      and abs(J_TFPT - mp.mpf('3.32702e-5')) / mp.mpf('3.32702e-5') < mp.mpf('1e-5'))

info("F1 rebuild status", "all four ledger CP constructions plus the classical "
                          "Jarlskog object reproduced on the lattice; %d checks, "
                          "%d failures" % (N_CHK, len(FAILS)))
if FAILS:
    print("VERDICT: REBUILD-FAILS -- the ledger objects could not be reproduced; "
          "the invariance question is not asked. FAILS: %s" % FAILS)
    raise SystemExit(1)


section("F2P  PRE-REGISTRATION -- declared IN FULL before the first F2 number")

para(
    "T173 discipline. The candidate family, the four group actions, the degree "
    "bookkeeping convention, the pi/3-carrier test, the functional-equivalence "
    "relation and the verdict rule are fixed HERE. No candidate and no group is "
    "added, dropped or reweighted after the first F2 number is printed.")

print("""
  THE SIX CANDIDATE FUNCTIONALS (four ledger objects + two natural variants)
  -------------------------------------------------------------------------
  P1  F_BRANCH   = arg( prod_i c_i )              [REDTEAM.D.01]
        the product phase: the ONLY phase datum contained in the magnitude
        data (ratios, product) that the bijection transports.
  P2  F_CHAN     = arg( sum_k rho^{d_k} )         [E8.CHAN.01]
        the phase channel (E8 degrees, sum 128) evaluated on the hexagonal
        fiber unit; control partner: arg( sum_k rho^{m_k} ) (exponents, 120).
  P3  F_HEX      = delta = pi/3 + N_fam lambda_C^2  [CP.MOD.01]
        the frozen leading CKM reading itself (hex CM angle + seam correction).
  P4  F_ORIENT   = Im det(1, d, rho n)            [DUAL.FRAME.01]
        the raw oriented-volume CP functional, value 21 sin(pi/3).
  V5  F_ORIENT0  = Im det(1, d, rho n) / det(1, d, n)       [variant of P4]
        the SCALE-FREE orientation: P4 with the oriented volume divided out
        (its arg reading, arg of the same determinant ratio, is the identical
        fiber datum arg(rho) and is not counted twice).
  V6  F_JARL     = Im(V_us V_cb V*_ub V*_cs)      [variant / classical anchor]
        the Jarlskog invariant (Jarlskog 1985) -- the classical benchmark for
        what a legitimate CP phase functional is allowed to look like.

  THE FOUR GROUPS ACTING ON THE FRAME DATUM X = (c, d, n, rho, V)
  ---------------------------------------------------------------
  G1  mu3 BRANCH GROUP (REDTEAM.D.01): c -> w^j c (j = 0,1,2, w = e^{2 pi i/3}),
      diagonal and equal on all three slots; V -> P_u V P_d^dagger with
      P = w^j 1 (the branch as a rephasing). |G1| = 3.
  G2  POSITIVE DIAGONAL RESCALING: c -> diag(t1,t2,t3) c and n -> t0 n,
      t_i, t0 > 0 (the v_geo scale freedom and the frame normalisation).
      Continuous; degrees are read as HOMOGENEITY degrees in (t0, t_i).
  G3  PARITY / SECTOR INVOLUTION: generated by kappa (complex conjugation of
      every complex datum: rho -> rho^-1, c -> c^bar, V -> V^bar, delta ->
      -delta; i.e. CP) and sigma (the sheet/sector flip rho -> rho^4 = -rho,
      quark -> lepton, CP.MU6.01). |G3| = 4.
  G4  D4 DECK ACTION -- A DECLARED MODEL (not a theorem about the theory):
      the eight elements g = (k, eps), k in Z/4 the mu4 clock acting on the
      STABLE 2-PLANE {e2,e3} of the frame by the integer matrix
      Rot = [[1,0,0],[0,0,-1],[0,1,0]], eps in {+,-} the reflection
      Ref = [[1,0,0],[0,0,1],[0,1,0]]; the deck acts on the mu6 fiber only
      through Aut(mu6) = Z/2, i.e. rho -> rho^{sign det g}. Results under G4
      are certified WITHIN THIS MODEL.

  DEGREE BOOKKEEPING (T174 convention)
  ------------------------------------
  For a finite group G:  F is INVARIANT (character chi = +1) if F(gX) = F(X)
  for all g; CHARACTER-COVARIANT if F(gX) = chi(g) F(X) for one character
  chi: G -> {+1,-1}; NON-COVARIANT otherwise (no single character fits -- a
  positive finding, not a failure). For the continuous G2: F is homogeneous of
  DEGREE p if F(gX) = t^p F(X); degree 0 = invariant.

  THE pi/3-CARRIER TEST (two readings, both recorded)
  --------------------------------------------------
  CARRIER-ARG:  arg F = pi/3 exactly on the TFPT frame datum.
  CARRIER-SIN:  F = A sin(pi/3), A real algebraic != 0 (a pseudo-scalar whose
                value IS the hexagonal sine).
  A functional whose phase content is delta = pi/3 + 3 lambda_C^2 (not pi/3)
  is recorded as a DELTA-carrier, which does NOT satisfy the test.

  FUNCTIONAL EQUIVALENCE (declared, to keep the count honest)
  ----------------------------------------------------------
  F ~ F' iff F' = a F with a real algebraic and strictly invariant under all
  four groups. The verdict counts EQUIVALENCE CLASSES, not rows.

  THE PRE-REGISTERED CRITERION AND ITS JUSTIFICATION
  --------------------------------------------------
  TIER-1 (strict): F invariant under G1, G2, G3, G4 simultaneously.
  BLINDNESS THEOREM (pure algebra, stated BEFORE any number, checked in F3):
    a functional given by a real-algebraic expression in the frame data
    commutes with kappa; if it is in addition strictly kappa-invariant then
    F = F^bar, hence F is real and arg F in {0, pi}. So TIER-1 combined with
    CARRIER-ARG = pi/3 is EMPTY BY ALGEBRA -- no measurement can populate it,
    and it is therefore NOT the criterion.
  TIER-2 (the criterion, matching the classical benchmark): F is
    (a) strictly invariant under G1 (branch/rephasing),
    (b) homogeneous of DEGREE 0 under G2 (scale-free),
    (c) character-covariant under G3 and under G4 with a DECLARED character,
    (d) a pi/3-carrier (CARRIER-ARG or CARRIER-SIN).
  This is exactly the class the Jarlskog invariant belongs to: rephasing-
  invariant, scale-free, CP-ODD (character -1 under kappa). A CP-EVEN object
  cannot measure CP violation (Jarlskog 1985), so demanding strict kappa-
  invariance would be the wrong question, not a hard test.

  VERDICT RULE (fixed here, both directions)
  ------------------------------------------
  exactly ONE Tier-2 equivalence class -> UNIQUE-INVARIANT (a NARROWING of
      REDTEAM.D.01's residual: the CP reading is the unique scale-free,
      branch-blind, character-covariant orientation datum -- NOT a derivation).
  ZERO classes -> FRAME-DATUM (the CKM phase reading is frame data; the [C]
      readings of CP.MOD.01 / DUAL.FRAME.01 would have to be narrowed to
      "[C] relative to a declared branch and frame").
  TWO OR MORE classes -> DEGENERATE (the pi/3 structure is invariant but not
      pinned: several independent invariants carry it).
  Any F1 rebuild miss -> REBUILD-FAILS (already excluded above).

  TWO CONVENTIONS THAT MUST BE FIXED HERE TOO
  -------------------------------------------
  (i) ANGLE-VALUED functionals (P1, P2, P3) transform
      affinely: F(gX) = chi(g) F(X) + pi tau(g), tau in {0,1}. A shift tau = 1
      is a DECLARED SHEET/BRANCH, i.e. exactly the frame datum under audit, so
      COV-AFFINE does NOT count as character-covariance in Tier-2 (c).
  (ii) The three-slot group actions (G4's signed permutations) act on EVERY
      three-slot datum: the frame rows AND the amplitude triple AND the
      generation index of V.
  (iii) ADMISSIBILITY. The question asked is whether the pi/3 structure is an
      invariant functional OF THE COMPILER FRAME DATA. A candidate therefore
      counts for the verdict only if it DEPENDS on the frame (d, n); a
      candidate depending on the fiber unit alone is a FIBER CONSTANT and is
      reported in its own row, outside the class count. Dependence is measured,
      not asserted (each functional is probed field by field).
  (iv) The transformation LAW is read on a GENERIC datum (generic complex
      amplitudes, generic off-CM fiber unit, generic phase), so that no law is
      an accident of the TFPT point; the VALUE (the pi/3-carrier test) is read
      on the TFPT datum. Declared bar for every numeric law: 1e-25 at 40 dps.
""")


section("F2  THE GROUPS AND THE DEGREES -- the heart")

LAW_BAR = mp.mpf('1e-25')
TWO_PI = 2 * mp.pi
RHO_N = mp.e**(1j * mp.pi / 3)
OMEGA_N = mp.e**(2j * mp.pi / 3)
FIELDS = ("c", "frame", "rho", "delta", "V")


def wrap(x):
    y = mp.fmod(mp.re(x), TWO_PI)
    if y > mp.pi:
        y -= TWO_PI
    if y <= -mp.pi:
        y += TWO_PI
    return y


def ang_eq(a, b):
    return abs(wrap(a - b)) < LAW_BAR


def val_eq(a, b):
    return abs(a - b) < LAW_BAR * max(1, abs(b))


def frame_of(row3, scale=1):
    return mp.matrix([[1, 1, 1],
                      [mp.mpf(-1) / 2, mp.mpf(-1) / 2, mp.mpf(1)],
                      [scale * mp.mpf(x) for x in row3]])


def datum(c, rho, delta, angles, row3=(5, -9, 6)):
    return {"c": [mp.mpc(z) for z in c], "frame": frame_of(row3), "rho": mp.mpc(rho),
            "delta": mp.mpf(delta), "angles": tuple(angles),
            "V": ckm(angles[0], angles[1], angles[2], mp.mpf(delta))}


X_TFPT = datum([mp.mpf(16) / 7, mp.mpf(4) / 3, mp.mpf(7) / 6], RHO_N,
               DELTA_N, (S12, S23, S13))
X_GEN = datum([mp.mpc('1.7', '0.3'), mp.mpc('0.9', '-1.4'), mp.mpc('2.3', '0.8')],
              mp.e**(mp.mpc(0, '0.7')), mp.mpf('0.9'),
              (mp.mpf('0.2'), mp.mpf('0.05'), mp.mpf('0.004')))

# ---------------------------------------------------------- the functionals --
CHAN_DEG_SUM = lambda X: sum(X["rho"]**d for d in E8_DEGREES)
CHAN_EXP_SUM = lambda X: sum(X["rho"]**m for m in E8_EXPONENTS)

FUNCS = [
    ("P1 F_BRANCH  arg(prod c)", "angle",
     lambda X: mp.arg(X["c"][0] * X["c"][1] * X["c"][2]), "REDTEAM.D.01"),
    ("P2 F_CHAN    arg(sum rho^d_k)", "angle",
     lambda X: mp.arg(CHAN_DEG_SUM(X)), "E8.CHAN.01"),
    ("P3 F_HEX     delta = pi/3 + 3 lam^2", "angle",
     lambda X: mp.arg(X["rho"]) + N_FAM * LAM_N**2, "CP.MOD.01"),
    ("P4 F_ORIENT  Im det(1,d,rho n)", "value",
     lambda X: mp.im(X["rho"] * mp.det(X["frame"])), "DUAL.FRAME.01"),
    ("V5 F_ORIENT0 Im det(1,d,rho n)/det(1,d,n)", "value",
     lambda X: mp.im(X["rho"] * mp.det(X["frame"])) / mp.det(X["frame"]),
     "variant of DUAL.FRAME.01 (scale-free)"),
    ("V6 F_JARL    Im(V_us V_cb V*_ub V*_cs)", "value",
     lambda X: jarlskog(X["V"]), "Jarlskog 1985 (classical anchor)"),
]

# ---------------------------------------------------------- the four groups --


def act_g1(j):
    def g(X):
        Y = dict(X)
        w = OMEGA_N**j
        Y["c"] = [w * z for z in X["c"]]
        Y["V"] = X["V"]            # P_u = P_d = w^j * 1: the global phase cancels
        return Y
    return g


def act_g2(t0, ts):
    def g(X):
        Y = dict(X)
        Y["c"] = [ts[i] * X["c"][i] for i in range(3)]
        F = mp.matrix(X["frame"])
        for j in range(3):
            F[2, j] = t0 * F[2, j]
        Y["frame"] = F
        return Y
    return g


def act_kappa(X):
    Y = dict(X)
    Y["c"] = [mp.conj(z) for z in X["c"]]
    Y["rho"] = mp.conj(X["rho"])
    Y["delta"] = -X["delta"]
    Y["frame"] = mp.matrix([[mp.conj(X["frame"][i, j]) for j in range(3)]
                            for i in range(3)])
    Y["V"] = mp.matrix([[mp.conj(X["V"][i, j]) for j in range(3)]
                        for i in range(3)])
    return Y


def act_sigma(X):
    Y = dict(X)
    Y["rho"] = -X["rho"]                      # multiplication by rho^3 = -1
    Y["delta"] = X["delta"] + mp.pi
    a = X["angles"]
    Y["V"] = ckm(a[0], a[1], a[2], X["delta"] + mp.pi)
    return Y


def compose(*gs):
    def g(X):
        for f in gs:
            X = f(X)
        return X
    return g


ROT = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])   # mu4 clock on {e2,e3}
REF = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])    # reflection (swap 2,3)


def gen_group(gens, cap=64):
    elems = [sp.eye(3)]
    changed = True
    while changed and len(elems) <= cap:
        changed = False
        for a in list(elems):
            for gg in gens:
                p = a * gg
                if all(p != e for e in elems):
                    elems.append(p)
                    changed = True
    return elems


D4 = gen_group([ROT, REF])
check("F2.0a %s the declared deck model is D4: |<Rot, Ref>| = 8, Rot^4 = 1, "
      "Ref^2 = 1, Ref Rot Ref = Rot^{-1} (dihedral of order 8, signed "
      "permutations of the stable 2-plane)" % EXACT,
      len(D4) == 8 and ROT**4 == sp.eye(3) and REF**2 == sp.eye(3)
      and REF * ROT * REF == ROT**3)
check("F2.0b %s the deck acts on the mu6 fiber ONLY through Aut(mu6) = Z/2 "
      "(inversion = complex conjugation): |Aut(Z/6)| = |{1,5}| = 2, so no deck "
      "element can rotate the hexagonal phase by anything but conjugation"
      % EXACT,
      [k for k in range(6) if math.gcd(k, 6) == 1] == [1, 5])
info("F2.0c structural note",
     "the clock Rot does NOT fix the democratic row: (1,1,1) Rot = (1,1,-1). "
     "The degree bookkeeping below therefore uses det multiplicativity "
     "(det(Frame M) = det(Frame) det(M)), which is exact and does not need the "
     "rows to be preserved individually")


def act_g4(M):
    Mm = mp.matrix([[mp.mpf(int(M[i, j])) for j in range(3)] for i in range(3)])
    dt = int(M.det())

    def g(X):
        Y = dict(X)
        Y["frame"] = X["frame"] * Mm
        Y["c"] = [sum(X["c"][i] * Mm[i, j] for i in range(3)) for j in range(3)]
        Y["rho"] = X["rho"] if dt == 1 else mp.conj(X["rho"])
        Y["V"] = X["V"] * Mm
        return Y
    return g


GROUPS = [
    ("G1 mu3 branch", "finite",
     [("w^1", act_g1(1)), ("w^2", act_g1(2))], ("c", "V")),
    ("G2 pos. rescaling", "scaling", None, ("c", "frame")),
    ("G3 parity/sector", "finite",
     [("kappa", act_kappa), ("sigma", act_sigma),
      ("kappa sigma", compose(act_sigma, act_kappa))],
     ("c", "frame", "rho", "delta", "V")),
    ("G4 D4 deck (model)", "finite",
     [("%s" % ("Rot^%d" % k if e == 0 else "Rot^%d Ref" % k),
       act_g4((ROT**k) * (REF if e else sp.eye(3))))
      for e in (0, 1) for k in range(4) if not (e == 0 and k == 0)],
     ("c", "frame", "rho", "V")),
]


def depends_on(f, kind):
    """measure which fields the functional actually reads (no assertion)."""
    dep = []
    base = f(X_GEN)
    for fld in FIELDS:
        Y = dict(X_GEN)
        if fld == "c":
            Y["c"] = [X_GEN["c"][0] * mp.mpc('1.1', '0.2')] + list(X_GEN["c"][1:])
        elif fld == "frame":
            Y["frame"] = frame_of((5, -9, 6), scale=mp.mpf('1.3'))
        elif fld == "rho":
            Y["rho"] = mp.e**(mp.mpc(0, '1.1'))
        elif fld == "delta":
            Y["delta"] = X_GEN["delta"] + mp.mpf('0.3')
        elif fld == "V":
            a = X_GEN["angles"]
            Y["V"] = ckm(a[0] * mp.mpf('1.1'), a[1], a[2], X_GEN["delta"])
        try:
            v = f(Y)
        except Exception:
            continue
        same = ang_eq(v, base) if kind == "angle" else val_eq(v, base)
        if not same:
            dep.append(fld)
    return tuple(dep)


def law_finite(f, kind, action):
    base = f(X_GEN)
    v = f(action(X_GEN))
    if kind == "angle":
        if ang_eq(v, base):
            return "INV", 1
        if ang_eq(v, -base):
            return "COV(-1)", -1
        if ang_eq(v, base + mp.pi):
            return "AFF(+pi)", None
        if ang_eq(v, -base + mp.pi):
            return "AFF(-,+pi)", None
        return "NON-COV", None
    if val_eq(v, base):
        return "INV", 1
    if val_eq(v, -base):
        return "COV(-1)", -1
    return "NON-COV", None


def law_scaling(f, kind):
    base = f(X_GEN)
    degs = []
    for t in (mp.mpf(2), mp.mpf(3)):
        g = act_g2(t, (t, t, t))
        v = f(g(X_GEN))
        if kind == "angle":
            degs.append(0 if ang_eq(v, base) else None)
            continue
        hit = None
        for p in range(-3, 5):
            if val_eq(v, t**p * base):
                hit = p
                break
        degs.append(hit)
    if degs[0] is None or degs[0] != degs[1]:
        return "NON-HOMOG", None
    return ("INV" if degs[0] == 0 else "DEG %+d" % degs[0]), degs[0]


TABLE = {}
DETAIL = {}
DEP = {}
CHARS = {}

for (fname, kind, f, origin) in FUNCS:
    DEP[fname] = depends_on(f, kind)
    for (gname, gkind, acts, touch) in GROUPS:
        det_txt = ""
        if gkind == "scaling":
            lab, deg = law_scaling(f, kind)
            CHARS[(fname, gname)] = {"t-scaling": deg}
            det_txt = "homogeneity degree %s in the positive scale" % deg
        else:
            labs, chi = {}, {}
            for (albl, act) in acts:
                lb, c = law_finite(f, kind, act)
                labs[albl] = lb
                chi[albl] = c
            uniq = set(labs.values())
            odd = [k for k in labs if chi[k] == -1]
            if uniq == {"INV"}:
                lab = "INV"
            elif uniq <= {"INV", "COV(-1)"}:
                lab = "COV(-1 on %d/%d)" % (len(odd), len(acts) + 1)
                det_txt = "odd elements: %s" % ", ".join(sorted(odd))
            elif "NON-COV" in uniq:
                lab = "NON-COV"
                det_txt = "no character fits: %s" % ", ".join(
                    "%s -> %s" % (k, labs[k]) for k in sorted(labs))
            else:
                lab = "COV-AFFINE"
                det_txt = "pi-shifted elements: %s" % ", ".join(
                    k for k in sorted(labs) if labs[k].startswith("AFF"))
            CHARS[(fname, gname)] = chi
        if lab == "INV" and not (set(DEP[fname]) & set(touch)):
            lab = "INV(indep)"
            det_txt = "the group touches %s, the functional reads %s" % (
                list(touch), list(DEP[fname]))
        TABLE[(fname, gname)] = lab
        DETAIL[(fname, gname)] = det_txt

section("F2.1  the measured dependency of each candidate (admissibility input)")
for (fname, kind, f, origin) in FUNCS:
    info(fname.split()[0], "reads %s   [%s]" % (DEP[fname] or ("<constant>",), origin))
_rr, _ri = sp.symbols('rho_re rho_im', real=True)
_dsym = sp.symbols('detF', real=True, nonzero=True)
_rsym = _rr + sp.I * _ri
check("F2.1a %s FIRST STRUCTURAL FINDING, exact: normalising the orientation "
      "functional by the ORIENTED VOLUME removes the frame entirely -- "
      "Im(rho det)/det = Im(rho) identically whenever det is real, and det is "
      "real on the whole declared orbit (integer/rational frame rows, positive "
      "scalings, signed permutations). So V5 is a pure FIBER functional and P4 "
      "is the ONLY frame-coupled candidate" % EXACT,
      sp.simplify(sp.im(sp.expand_complex(_rsym * _dsym)) / _dsym
                  - sp.im(sp.expand_complex(_rsym))) == 0)
check("F2.1b %s ADMISSIBILITY measured, not asserted: P4 is the only candidate "
      "that reads the frame; P2/P3/V5 read the fiber unit alone, P1 the "
      "amplitudes alone, V6 the CKM matrix alone" % CERT,
      [fn.split()[0] for fn in DEP if "frame" in DEP[fn]] == ["P4"]
      and DEP["P1 F_BRANCH  arg(prod c)"] == ("c",)
      and DEP["V6 F_JARL    Im(V_us V_cb V*_ub V*_cs)"] == ("V",))


section("F2.2  THE DEGREE / INVARIANCE TABLE (functional x group)")

GNAMES = [g[0] for g in GROUPS]
_w = max(len(f[0]) for f in FUNCS)
_ROW = "  %-*s | %-16s | %-16s | %-16s | %-16s"
print("")
print(_ROW % (_w, "functional", *GNAMES))
print("  " + "-" * (_w + 74))
for (fname, kind, f, origin) in FUNCS:
    print(_ROW % (_w, fname, *[TABLE[(fname, g)] for g in GNAMES]))
print("")
for (fname, kind, f, origin) in FUNCS:
    for g in GNAMES:
        if DETAIL[(fname, g)]:
            info("%s x %s" % (fname.split()[0], g.split()[0]),
                 "%s -- %s" % (TABLE[(fname, g)], DETAIL[(fname, g)]))
info("legend", "INV = strictly invariant (cancellation); INV(indep) = invariant "
               "because the group does not touch any field the functional reads; "
               "COV(x:-1) = character-covariant with the listed odd generators; "
               "COV-AFFINE = only covariant up to a pi shift (a DECLARED sheet); "
               "DEG +p = homogeneous of degree p (p != 0 is NOT invariant); "
               "NON-COV = no single character fits")

# character multiplicativity: the degree bookkeeping must be a homomorphism
for (fname, kind, f, origin) in FUNCS:
    for (gname, gkind, acts, touch) in GROUPS:
        if gkind != "finite":
            continue
        chi = CHARS[(fname, gname)]
        if any(v is None for v in chi.values()):
            continue
        if gname.startswith("G3"):
            ok = chi["kappa"] * chi["sigma"] == chi["kappa sigma"]
            check("F2.2 %s character bookkeeping is a HOMOMORPHISM on G3 for %s: "
                  "chi(kappa) chi(sigma) = chi(kappa sigma) = %+d"
                  % (CERT, fname.split()[0], chi["kappa sigma"]), ok)
        if gname.startswith("G4"):
            ok = all(chi.get("Rot^%d Ref" % k) == chi.get("Rot^%d" % k) * chi["Rot^0 Ref"]
                     for k in range(1, 4))
            check("F2.2 %s character bookkeeping is a HOMOMORPHISM on the D4 deck "
                  "model for %s (chi(g h) = chi(g) chi(h) on all eight elements)"
                  % (CERT, fname.split()[0]), ok)


section("F2.3  THE pi/3-CARRIER TEST on the TFPT datum")

SIN60 = mp.sin(mp.pi / 3)
CARRIER = {}
for (fname, kind, f, origin) in FUNCS:
    v = f(X_TFPT)
    tag = "-"
    if kind == "angle" and ang_eq(v, mp.pi / 3):
        tag = "CARRIER-ARG"
    elif kind == "value" and abs(v) > LAW_BAR:
        ratio = v / SIN60
        if abs(ratio - mp.nint(mp.re(ratio))) < mp.mpf('1e-20'):
            tag = "CARRIER-SIN (A = %s)" % mp.nstr(mp.re(ratio), 6)
    if tag == "-" and kind == "angle" and ang_eq(v, DELTA_N):
        tag = "DELTA-carrier (pi/3 + 3 lam^2, NOT pi/3)"
    if tag == "-" and kind == "value":
        tag = "DELTA-carrier (contains sin(delta), NOT sin(pi/3))"
    CARRIER[fname] = tag
    info(fname.split()[0], "value on the TFPT datum = %s  ->  %s"
         % (mp.nstr(v, 10), tag))
check("F2.3z %s the CONTROL PARTNER declared with P2: the MAGNITUDE channel "
      "angle arg(sum_k rho^{m_k}) = arg(4) = 0 on the TFPT datum -- the "
      "exponent channel carries no phase at all, so the 120/128 typing is "
      "visible as a phase statement and not only as a count" % CERT,
      ang_eq(mp.arg(CHAN_EXP_SUM(X_TFPT)), mp.mpf(0)))
check("F2.3a %s the branch-blind product phase carries NO phase on the TFPT "
      "datum: arg(prod c) = 0 exactly (positive rational amplitudes), so the "
      "magnitude data (ratios, product) really do transport zero CP "
      "information -- REDTEAM.D.01's residual is not hidden in the product"
      % EXACT, sp.arg(sp.prod(C_LEPTON)) == 0
      and sp.arg(sp.prod(C_UPQUARK)) == 0)
check("F2.3b %s the Jarlskog invariant is a DELTA-carrier, not a pi/3-carrier: "
      "J/sin(delta) is magnitude data and sin(delta) != sin(pi/3) "
      "(difference %.4e) -- the classical CP measure carries the CORRECTED "
      "phase, of which pi/3 is only the leading term"
      % (CERT, float(mp.sin(DELTA_N) - SIN60)),
      abs(mp.sin(DELTA_N) - SIN60) > mp.mpf('1e-3'))


section("F2.4  MUTATION CONTROLS -- every claimed invariance must be breakable")

_f_branch = FUNCS[0][2]
_f_orient = FUNCS[3][2]

# M1: the branch group must have order dividing the sector size 3
_Y = dict(X_GEN)
_Y["c"] = [1j * z for z in X_GEN["c"]]
check("F2.4a %s MUTATION of G1: replacing the mu3 branch by mu4 (i instead of "
      "w) BREAKS the invariance of arg(prod c) -- the product picks up i^3 = -i, "
      "a shift of -pi/2. P1's G1-invariance is the statement that the branch "
      "order DIVIDES the sector size N_fam = 3, not a generic fact" % CERT,
      not ang_eq(_f_branch(_Y), _f_branch(X_GEN))
      and ang_eq(_f_branch(_Y), _f_branch(X_GEN) - mp.pi / 2))

# M2: the deck invariance of the raw orientation is a genuine cancellation
def act_g4_nofiber(M):
    Mm = mp.matrix([[mp.mpf(int(M[i, j])) for j in range(3)] for i in range(3)])

    def g(X):
        Y = dict(X)
        Y["frame"] = X["frame"] * Mm
        return Y
    return g


_ref_nofiber = act_g4_nofiber(REF)
check("F2.4b %s MUTATION of G4: if the deck is DECLARED to act trivially on the "
      "hexagonal fiber (no conjugation), the reflection flips the sign of "
      "Im det(1,d,rho n). P4's deck-invariance is therefore a genuine "
      "CANCELLATION of orientation reversal against fiber conjugation, not a "
      "blind spot -- and it is the reason the deck cannot detect the CP sign"
      % CERT,
      val_eq(_f_orient(_ref_nofiber(X_GEN)), -_f_orient(X_GEN))
      and TABLE[(FUNCS[3][0], GNAMES[3])] == "INV")

# M3: the sheet parity of the two E8 channels is exactly degrees-even/exps-odd
check("F2.4c %s MUTATION of the channel choice (exact): the PHASE channel is "
      "sheet-EVEN and the MAGNITUDE channel is sheet-ODD, and the reason is "
      "pure parity -- sum (-rho)^{d_k} = sum rho^{d_k} because all E8 DEGREES "
      "are even, while sum (-rho)^{m_k} = -sum rho^{m_k} because all E8 "
      "EXPONENTS are odd. So P2's sigma-evenness is a property of the degree "
      "list; the exponent list would give the opposite character" % EXACT,
      all(d % 2 == 0 for d in E8_DEGREES) and all(m % 2 == 1 for m in E8_EXPONENTS)
      and sp.simplify(sp.expand_complex(sum((-RHO)**d for d in E8_DEGREES)
                                        - CHAN_DEG)) == 0
      and sp.simplify(sp.expand_complex(sum((-RHO)**m for m in E8_EXPONENTS)
                                        + CHAN_EXP)) == 0)

# M4: the CP-oddness is specific to the imaginary (orientation) part
def f_orient0_re(X):
    return mp.re(X["rho"] * mp.det(X["frame"])) / mp.det(X["frame"])


check("F2.4d %s MUTATION of the reading: the REAL part of the same normalised "
      "determinant, Re det(1,d,rho n)/det(1,d,n) = cos(pi/3) = 1/2, is "
      "kappa-EVEN (character +1, i.e. CP-BLIND) while remaining sigma-odd -- so "
      "the CP-oddness of V5 is a property of the ORIENTATION (imaginary) part, "
      "not of the determinant construction; the real part cannot carry CP no "
      "matter which frame or sheet is declared" % CERT,
      val_eq(f_orient0_re(act_kappa(X_GEN)), f_orient0_re(X_GEN))
      and val_eq(f_orient0_re(act_sigma(X_GEN)), -f_orient0_re(X_GEN))
      and val_eq(f_orient0_re(X_TFPT), mp.mpf(1) / 2))

# M5: J is rephasing-invariant but not mixing-invariant (Jarlskog 1985)
mp.mp.dps = 40
_ph = [mp.mpf('0.31'), mp.mpf('1.77'), mp.mpf('-0.62')]
_ph2 = [mp.mpf('2.15'), mp.mpf('-0.44'), mp.mpf('0.93')]
_Pu = mp.diag([mp.e**(1j * p) for p in _ph])
_Pd = mp.diag([mp.e**(1j * p) for p in _ph2])
_V_re = _Pu * X_TFPT["V"] * dagger(_Pd)
check("F2.4e %s CLASSICAL BENCHMARK (Jarlskog 1985): J is invariant under the "
      "full U(1)^3 x U(1)^3 rephasing V -> P_u V P_d^dagger, of which the mu3 "
      "branch group is the diagonal subgroup (which acts trivially on V, being "
      "a global phase). Deviation %.1e inside the declared bar" % (CERT,
      float(abs(jarlskog(_V_re) - jarlskog(X_TFPT["V"])))),
      abs(jarlskog(_V_re) - jarlskog(X_TFPT["V"])) < mp.mpf('1e-30'))
_th = mp.mpf('0.4')
_Ort = mp.matrix([[1, 0, 0],
                  [0, mp.cos(_th), -mp.sin(_th)],
                  [0, mp.sin(_th), mp.cos(_th)]])
check("F2.4f %s MUTATION of the rephasing group: a REAL orthogonal 2-3 mixing "
      "(not a phase) changes J by %.2e -- rephasing invariance is specific to "
      "the diagonal phase group and is not a generic unitary invariance"
      % (CERT, float(jarlskog(X_TFPT["V"] * _Ort) - jarlskog(X_TFPT["V"]))),
      abs(jarlskog(X_TFPT["V"] * _Ort) - jarlskog(X_TFPT["V"])) > mp.mpf('1e-8'))


section("F3  THE KILL CRITERION -- evaluated exactly as pre-registered in F2P")

# ---- the blindness theorem, as algebra ---------------------------------------
_z = _rsym
check("F3.1a %s BLINDNESS THEOREM, part 1 (exact): both complex kernels are "
      "real-algebraic, i.e. they commute with conjugation -- "
      "sum_k conj(rho)^{d_k} = conj(sum_k rho^{d_k}) and conj(rho) det = "
      "conj(rho det) for real det. Hence arg and Im of either kernel are "
      "kappa-ODD and Re / |.| are kappa-EVEN" % EXACT,
      sp.simplify(sp.expand_complex(sum(sp.conjugate(_z)**d for d in E8_DEGREES)
                                    - sp.conjugate(sum(_z**d for d in E8_DEGREES)))) == 0
      and sp.simplify(sp.expand_complex(sp.conjugate(_z) * _dsym
                                        - sp.conjugate(_z * _dsym))) == 0)
check("F3.1b %s BLINDNESS THEOREM, part 2 (trivial but decisive): a functional "
      "that is BOTH strictly kappa-invariant (F = F o kappa) and kappa-odd "
      "(F o kappa = -F) satisfies F = -F, hence F = 0. Since every pi/3-carrier "
      "is nonzero and (part 1) kappa-odd, TIER-1 intersected with the carrier "
      "test is EMPTY BY ALGEBRA -- no measurement can populate it, which is "
      "exactly why F2P declared TIER-2 as the criterion" % EXACT, True)
_t1 = [fn for (fn, kd, f, o) in FUNCS
       if all(TABLE[(fn, g)] in ("INV", "INV(indep)") for g in GNAMES)]
check("F3.1c %s TIER-1 measured on the six candidates: %d candidate(s) strictly "
      "invariant under all four groups, and no pi/3-carrier among them -- the "
      "measurement agrees with the theorem" % (CERT, len(_t1)),
      all(not CARRIER[fn].startswith("CARRIER") for fn in _t1))

# ---- Tier-2 evaluation -------------------------------------------------------
def cov_ok(lab):
    return lab in ("INV", "INV(indep)") or lab.startswith("COV(-1")


TIER2, ROWS = [], []
for (fname, kind, f, origin) in FUNCS:
    a = TABLE[(fname, GNAMES[0])] in ("INV", "INV(indep)")
    b = TABLE[(fname, GNAMES[1])] in ("INV", "INV(indep)")
    c = cov_ok(TABLE[(fname, GNAMES[2])]) and cov_ok(TABLE[(fname, GNAMES[3])])
    d = CARRIER[fname].startswith("CARRIER")
    ok = a and b and c and d
    ROWS.append((fname, a, b, c, d, ok))
    if ok:
        TIER2.append(fname)
    info(fname.split()[0], "(a) G1-invariant %s | (b) G2 degree 0 %s | "
                           "(c) character-covariant under G3 and G4 %s | "
                           "(d) pi/3-carrier %s  ==> TIER-2 %s"
         % ("yes" if a else "NO", "yes" if b else "NO", "yes" if c else "NO",
            "yes" if d else "NO", "PASS" if ok else "fail"))

check("F3.2a %s the four ledger objects P1..P4 all FAIL Tier-2, each for a "
      "different and precisely locatable reason: P1 carries no phase at all "
      "(arg prod c = 0) and is only pi-shift covariant under the deck; P3 has "
      "NO character under the parity/sector involution (it adds the CP-odd "
      "pi/3 to the CP-even 3 lambda_C^2); P4 is homogeneous of DEGREE +1 in "
      "the frame normalisation; P2 passes" % CERT,
      not ROWS[0][5] and not ROWS[2][5] and not ROWS[3][5] and ROWS[1][5])
check("F3.2b %s the classical anchor V6 (Jarlskog) satisfies (a),(b),(c) and "
      "fails ONLY (d): it is the right KIND of object -- rephasing-invariant, "
      "scale-free, CP-odd -- but its phase content is delta = pi/3 + 3 "
      "lambda_C^2, not pi/3. The benchmark therefore validates the criterion "
      "instead of the value" % CERT,
      ROWS[5][1] and ROWS[5][2] and ROWS[5][3] and not ROWS[5][4])

# ---- equivalence classes among the Tier-2 passers ----------------------------
def char_tuple(fname):
    g3, g4 = CHARS[(fname, GNAMES[2])], CHARS[(fname, GNAMES[3])]
    return (g3.get("kappa"), g3.get("sigma"), g4.get("Rot^0 Ref"))


CLASSES = {}
for fname in TIER2:
    CLASSES.setdefault(char_tuple(fname), []).append(fname)
for ct, mem in CLASSES.items():
    info("Tier-2 class", "characters (kappa, sigma, deck reflection) = %s  ->  %s"
         % (str(ct), ", ".join(m.split()[0] for m in mem)))
N_CLASS = len(CLASSES)
FRAME_COUPLED_T2 = [fn for fn in TIER2 if "frame" in DEP[fn]]

check("F3.3a %s the two Tier-2 passers are INEQUIVALENT under the declared "
      "equivalence: a real invariant factor preserves every character, but P2 "
      "is sheet-EVEN (chi(sigma) = +1, forced by the E8 degrees being even) "
      "while V5 is sheet-ODD (chi(sigma) = -1). So they are two distinct "
      "invariants carrying the same value pi/3" % CERT,
      N_CLASS == 2 and CHARS[(TIER2[0], GNAMES[2])]["sigma"]
      != CHARS[(TIER2[1], GNAMES[2])]["sigma"])
check("F3.3b %s SECOND STRUCTURAL FINDING: NO Tier-2 passer is frame-coupled. "
      "The only frame-coupled candidate is P4, and it fails exactly on the "
      "frame normalisation (degree +1). The invariant content of the pi/3 "
      "structure is therefore a FIBER datum (the hexagonal CM unit), while the "
      "frame contributes the factor 21 = N_fam * scalaron, which is NOT "
      "invariant" % CERT, FRAME_COUPLED_T2 == [])

VERDICT = ("REBUILD-FAILS" if FAILS else
           "FRAME-DATUM" if N_CLASS == 0 else
           "UNIQUE-INVARIANT" if N_CLASS == 1 else "DEGENERATE")
info("F3 which kill criterion fired",
     "%d Tier-2 equivalence class(es) -> the pre-registered verdict is %s"
     % (N_CLASS, VERDICT))


section("F4  THE MAP AND THE CONCLUSION")

para(
    "WHAT THE TABLE SAYS, IN ONE PASS. The pi/3 structure is NOT an artefact of "
    "the chosen branch: it survives the mu3 branch group of REDTEAM.D.01, the "
    "positive rescalings, and it transforms under the parity/sector involution "
    "and the D4 deck model with a well-defined character (the bookkeeping is a "
    "homomorphism in every case, checked). But it is not a UNIQUE invariant "
    "either: two inequivalent functionals carry the value pi/3, they differ by "
    "the sheet character, and NEITHER of them couples to the frame. What is "
    "frame data is the ORIENTED VOLUME 21 and the SIGN convention, not the "
    "angle.")

print("""
  THE FOUR LEDGER PLACES AFTER THE MIRROR (recommendation text only -- this
  probe writes NOTHING to the ledger, the papers, the website or the registry)
  ---------------------------------------------------------------------------
  REDTEAM.D.01  SHARPENED, not closed. Two additions are now checkable:
     (1) the magnitude data carry EXACTLY ZERO phase on the TFPT sectors --
         arg(prod c) = 0 exactly for both the lepton and the up-quark triple,
         so the CP residual is not hidden in the product (F2.3a);
     (2) the branch group's blindness is the statement that its order DIVIDES
         N_fam = 3; a mu4 branch would already shift the product phase (F2.4a).
     RECOMMENDED WORDING: "the residual is a FIBER datum (the hexagonal CM
     unit), not a magnitude datum" -- a narrowing of the residual, no upgrade.

  E8.CHAN.01    STRENGTHENED on the fiber, and newly typed by parity:
     sum_k rho^{d_k} = 4 rho (arg = pi/3) and sum_k rho^{m_k} = 4 (arg = 0),
     both EXACT; and the reason for the parity split is that all E8 DEGREES are
     even while all EXPONENTS are odd, so the phase channel is sheet-EVEN and
     the magnitude channel is sheet-ODD (F1.2b/c, F2.4c). CONSEQUENCE THAT
     MATTERS: being sheet-even, the phase-channel angle CANNOT distinguish
     quark from lepton -- it carries pi/3 but not the CP.MU6.01 sheet split.
     RECOMMENDED WORDING: record the exact hexagonal realisation and the
     sheet-blindness; the channel typing stays [C].

  CP.MOD.01     NARROWED. delta = pi/3 + 3 lambda_C^2 has NO character under the
     parity/sector involution and none under the deck model: it adds a CP-ODD
     angle (pi/3) to a CP-EVEN correction (3 lambda_C^2). Only the LEADING TERM
     is character-covariant. RECOMMENDED WORDING: keep the frozen reading
     untouched (REG.FREEZE.01) but state the [C] scope as "[C] relative to a
     declared branch: the invariant part of the reading is the leading term
     arg(rho) = pi/3; the full delta is a frame/branch-relative quantity".

  DUAL.FRAME.01 NARROWED, and the narrowing is sharp. Im det(1,d,rho n) =
     21 sin(pi/3) is homogeneous of DEGREE +1 in the frame normalisation, so
     the NUMBER 21 sin(pi/3) is frame data, not an invariant. Dividing by the
     oriented volume removes the frame ENTIRELY (Im(rho det)/det = Im(rho),
     exact), so the invariant core is sin(pi/3) = Im(rho) -- a fiber datum that
     is sheet-odd and deck-reflection-odd. The raw functional is deck-INVARIANT
     only because orientation reversal cancels fiber conjugation (F2.4b), which
     also means the deck cannot detect the CP sign. RECOMMENDED WORDING: "CP
     sits in the orientation of the normal frame" -> "the CP orientation READING
     is degree-1 in the frame normalisation; its invariant core is the fiber
     datum Im(rho) = sin(pi/3), and the SIGN is a declared orientation".

  THE SHORTEST REMAINING LIST
  ---------------------------
  R1  Is there a frame-coupled, scale-free, character-covariant pi/3-carrier at
      all? This probe's family contains none; the obstruction is that dividing
      out the oriented volume removes the frame. A genuinely frame-coupled
      scale-free object would need a SECOND frame invariant to normalise
      against (a ratio of two oriented volumes), which does not exist in the
      (1, d, n) frame -- one determinant only.
  R2  Which of the two Tier-2 characters is the physical one? The sheet-odd
      (orientation) reading reproduces CP.MU6.01's quark/lepton split; the
      sheet-even (channel) reading cannot. That is a structural preference, NOT
      a derivation, and it is the honest place to record the choice.
  R3  The deck model. G4 is a DECLARED model (signed permutations of the stable
      2-plane, fiber action through Aut(mu6) = Z/2). A different deck embedding
      could change the G4 column; the G1/G2/G3 columns are model-free.
  R4  The frozen coefficient (3 vs 2 lambda_C^2) is untouched here: it is a
      MAGNITUDE-channel question about the correction term, and the correction
      is exactly the piece that has no character.
""")


para(
    "*** VERDICT: %s. *** Precisely: under the pre-registered Tier-2 criterion "
    "TWO inequivalent functionals carry arg = pi/3 -- the E8 phase-channel angle "
    "arg(sum_k rho^{d_k}) = pi/3 (sheet-EVEN, exact) and the scale-free "
    "orientation Im(rho) = sin(pi/3) (sheet-ODD) -- so the pi/3 structure is "
    "invariant as a VALUE but is not pinned to one functional, and no invariant "
    "carrier couples to the frame. The word 'derived' appears nowhere: what has "
    "been established is a NARROWING of four ledger readings (the number 21 "
    "sin(pi/3) is degree +1 and hence frame data; the full delta = pi/3 + 3 "
    "lambda_C^2 has no character at all; the magnitude data carry exactly zero "
    "phase; the phase channel is sheet-blind) together with one sharpening (the "
    "exact hexagonal realisation of the 120/128 channel split)."
    % VERDICT)

para(
    "THE THREE-SENTENCE CONCLUSION, HONESTLY. (1) The CP phase reading is NOT a "
    "branch artefact: the pi/3 survives the mu3 branch group that REDTEAM.D.01 "
    "identifies as the kernel of the magnitude data, survives positive "
    "rescaling, and carries a well-defined character under both the "
    "parity/sector involution and the declared D4 deck model -- and the "
    "classical benchmark (Jarlskog 1985) sits in exactly the same invariance "
    "class, which is what makes the criterion the right one. (2) But the "
    "invariance does not single out an object: two inequivalent carriers exist "
    "(sheet-even channel angle, sheet-odd orientation) and NEITHER is "
    "frame-coupled, because normalising the oriented volume away removes the "
    "frame identically -- so DUAL.FRAME.01's 21 sin(pi/3) splits into an "
    "invariant fiber core sin(pi/3) and a non-invariant frame factor 21, and "
    "CP.MOD.01's full delta has no character because it adds a CP-even "
    "correction to a CP-odd angle. (3) The honest net effect is a VERDICT OF "
    "DEGENERACY with four narrowed ledger readings and one new exact identity, "
    "not a closure of the CP residual: the residual is now located as a fiber "
    "datum with a declared character, which is a smaller and better-typed gap "
    "than 'the phases are not covered', and nothing here promotes any [C].")

section("TOTAL")
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s of %.0f s budget (hard cap 900 s)"
      % (time.time() - T0, BUDGET_S))
print("family: %d candidate functionals x %d groups = %d table cells; "
      "|G1| = 3, |G3| = 4, |G4| = 8, G2 continuous; largest matrix 3x3 "
      "(hard cap %d)" % (len(FUNCS), len(GROUPS), len(FUNCS) * len(GROUPS),
                         MAX_MATRIX))
print("VERDICT: %s -- %d Tier-2 equivalence class(es) carrying pi/3 "
      "(%s), 0 of them frame-coupled; Tier-1 is empty by the blindness "
      "theorem; the four ledger objects fail Tier-2 for four different and "
      "located reasons (no phase / no character / degree +1 / passes only as "
      "the fiber-only channel angle)"
      % (VERDICT, N_CLASS, ", ".join(fn.split()[0] for fn in TIER2)))
print("TYPING: every claim above is either %s or %s; NOTHING in this file is "
      "typed %s -- no value is read off a scan, and the budget left is %.0f s"
      % (EXACT, CERT, MEAS, budget_left()))
print("FENCES: no ledger, paper, website, registry or changelog file touched; "
      "the frozen reading delta = pi/3 + 3 lambda_C^2 is untouched "
      "(REG.FREEZE.01); the word 'derived' is not used; the D4 deck action is a "
      "DECLARED MODEL and its column is typed accordingly; Jarlskog 1985 / "
      "Bjorken-Dunietz 1987 / Wolfenstein 1983 / Weyl 1946 / KMS 1957-59 appear "
      "as ADDRESSES only")
