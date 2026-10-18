#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""g31_winding_decoder_probe -- G31.WINDING.DECODER.01 (phase 1 of the
2026-08-08 evening plan): the winding quadratic q(t) = t^2 - g_car t +
|Z2| READS the G31 clock alphabet {2,3,5,6} into compiler atoms
{-|mu4|, -|mu4|, |Z2|, h(D5)}, packages them into ONE decoder polynomial
D(y) = (y+4)^2 (y-2)(y-8) = y^4 - 2y^3 - 48y^2 - 32y + 256, and bridges
EXACTLY to the Walsh eigenvalue -1/15 of the Gaussian census
(|mu4| q(|Z2|) / |R(E8)| = 4 x (-4) / 240 = -1/15, v857's law).

FROZEN CLAIMS (2026-08-08 evening, frozen + SHA-hashed before first run):

 S1  THE ALPHABET AND THE QUADRATIC (exact):
     S1.1 the clock alphabet {2,3,5,6} = {|Z2|, N_fam, g_car, |R+(A3)|}
     = Deg(G31)/4 (v858 normal form); the arithmetic pin recomputed
     HERE: the integer-quadruple census with product 46080 and sum 64
     returns EXACTLY [(8,12,20,24)]; the 607-group kill-scan
     selectivity (G31 the SOLE full-battery passer) is CITED from
     v858, not recomputed.
     S1.2 q(t) = t^2 - 5t + 2 (v857 part B winding quadratic) on the
     alphabet: q(2) = -4, q(3) = -4, q(5) = 2, q(6) = 8 EXACTLY; in
     compiler atoms {-|mu4|, -|mu4|, |Z2|, h(D5)} with h(D5) = 8.
     S1.3 THE PALINDROME (the complement check-code): q(5 - t) = q(t)
     identically (axis g_car/2), hence q(|Z2|) = q(N_fam) = -|mu4|
     BECAUSE 2 + 3 = 5 = g_car; typed honestly (measured): the
     reflection images of 5 and 6 are 0 and -1, OUTSIDE the alphabet
     (only the {2,3} pair is complement-closed).
 S2  THE DECODER POLYNOMIAL (exact expansion):
     S2.1 D(y) = prod_{a in {2,3,5,6}} (y - q(a)) = (y+4)^2 (y-2)(y-8)
     = y^4 - 2y^3 - 48y^2 - 32y + 256.
     S2.2 coefficient identification (signed coefficients
     (-2, -48, -32, +256)): 2 = |Z2|; 48 = Omega_adm = N_fam dim S+
     (ARCH.QUAD.01); 32 = 2^{g_car} = dim(S+ (+) S-); 256 =
     2^{rank E8}; the double root -4 = -|mu4| is FORCED by the
     palindrome pair {2,3} (report).
 S3  THE FOURIER BRIDGE (exact; v857 census law reproduced, not cited):
     S3.1 census rebuild on the 240 standard-model roots (v844/v857
     S6.3 machinery, read-only): V = L/(1+i)L has 15 nonzero classes
     x 16 roots, zero class EMPTY.
     S3.2 Walsh transform of the census: rhat(0) = 240, rhat(u) = -16
     for ALL 15 nonzero u; lambda_msg = -16/240 = -1/15 EXACT.
     S3.3 THE BRIDGE IDENTITY: |mu4| q(|Z2|) / |R(E8)| = 4 x (-4)/240
     = -1/15 = lambda_msg, and the SAME via q(N_fam) (the palindrome
     route): the winding quadratic evaluated at the sheet atom IS the
     nonzero-character Walsh eigenvalue, -16 = |mu4| q(|Z2|) = rhat(u).
 C   CONTROLS (each must fire; exact):
     C1 sibling deformation directions (probe-1 / v857 controls)
        change q and COLLAPSE the bridge: q2 = t^2 - t + 2 gives
        |mu4| q2(|Z2|)/240 = 16/240 = +1/15 != -1/15; q3 = t^2 + t - 2
        gives +1/15; q_row = t^2 - 5t + 1 gives -20/240 = -1/12.
     C2 sibling palindromes break the check-code: the axis of q2 is
        1/2 and of q3 is -1/2 (!= 5/2 = g_car/2); q2(3) = 8 != 4 =
        q2(2): the 2 <-> 3 complement symmetry dies off-direction.
     C3 alternative alphabets give DIFFERENT decoder polynomials:
        {2,3,5,7}: (y+4)^2 (y-2)(y-16) = y^4 - 10y^3 - 96y^2 - 32y
        + 512 (constant 2^9, NOT 2^{rank E8}; q(7) = 16);
        {1,2,3,5}: (y+2)(y+4)^2 (y-2) = y^4 + 8y^3 + 12y^2 - 32y - 64;
        HONEST LINE (typed, no kill): the -32 y coefficient SURVIVES
        in both alternatives -- per-coefficient selectivity is weak,
        the selective object is the full vector (-2,-48,-32,+256);
        the 6-vs-7 tension typed: replacing 6 = |R+(A3)| by 7 loses
        the y^3, y^2 and constant identifications; a third alphabet
        {3,5,6,7} is computed and reported (measured, not frozen).
 T   THE TYPING (mandatory, verbatim in the output): exact AUDIT
     theorem, NOT a physical functor -- an explicit intertwiner would
     be needed to make it causal; report only.

KILLS (any one fires => typed failure):
  K1 alphabet / arithmetic pin breaks           -> ALPHABET-MISMATCH
  K2 q-values / palindrome break                -> QVALUE-MISMATCH
  K3 decoder expansion / coefficients break     -> DECODER-MISMATCH
  K4 census / Walsh / bridge breaks             -> BRIDGE-MISMATCH
  K5 a control does not fire                    -> CONTROL-DEAD

VERDICT (frozen enum): WINDING-DECODER-EXACT / ALPHABET-MISMATCH /
QVALUE-MISMATCH / DECODER-MISMATCH / BRIDGE-MISMATCH / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact sympy/integer/Fraction arithmetic in every
decision; no floats, no RNG, no fits.  NO physics claim, NO RH claim.
Runtime cap: minutes.

Sources (read-only, machinery rebuilt inline): verification/
v858_g31_clock_alphabet.py (alphabet normal form + kill scan),
v857_simplex_fourier_winding.py (q_wind, census Walsh law -1/15,
S6.3 std-model census), v844_message_doily_rank.py + v833_gaussian_
ramification_ladder.py (class machinery), v832_anchor_flavor_
checksum.py (anchor/flavor context), ARCH.QUAD.01 (Omega_adm = 48).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/g31_winding_decoder_probe.py
"""
import hashlib
import itertools
import time
from fractions import Fraction as Fr

import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []

G_CAR = 5
Z2 = 2
N_FAM = 3
MU4 = 4
RP_A3 = 6
H_D5 = 8
OMEGA_ADM = 48
R_E8 = 240
RANK_E8 = 8
DEG31 = (8, 12, 20, 24)
ALPHABET = (2, 3, 5, 6)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("=" * 74)
print("G31.WINDING.DECODER.01 -- q(t) = t^2 - 5t + 2 reads {2,3,5,6} into")
print("{-4,-4,2,8}; D(y) = (y+4)^2(y-2)(y-8); |mu4| q(|Z2|)/240 = -1/15")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

t, y = sp.symbols("t y")
q = t ** 2 - G_CAR * t + Z2

# ======================================================================
section("S1: the alphabet and the quadratic")
# ======================================================================
quads = []
divs = [d for d in range(2, 46081) if 46080 % d == 0]
for d1 in divs:
    if d1 > 16:
        continue
    for d2 in divs:
        if d2 < d1 or 46080 % (d1 * d2) != 0:
            continue
        rest = 46080 // (d1 * d2)
        for d3 in divs:
            if d3 < d2 or rest % d3 != 0:
                continue
            d4 = rest // d3
            if d4 >= d3 and d1 + d2 + d3 + d4 == 64:
                quads.append((d1, d2, d3, d4))
check("S1.1 alphabet {2,3,5,6} = {|Z2|, N_fam, g_car, |R+(A3)|} = "
      "Deg(G31)/4 = %s; arithmetic pin recomputed: quadruples with "
      "product 46080, sum 64: %s == [(8,12,20,24)] UNIQUE"
      % (tuple(d // 4 for d in DEG31), quads),
      tuple(d // 4 for d in DEG31) == ALPHABET
      and set(ALPHABET) == {Z2, N_FAM, G_CAR, RP_A3}
      and quads == [DEG31], kill="K1")
print("      CITED (v858, not recomputed): the 607-group rank-4 kill "
      "scan --")
print("      G31 is the SOLE full-battery passer; weak-triple and "
      "raw-sum-64")
print("      impostors typed there.")

qvals = tuple(int(q.subs(t, a)) for a in ALPHABET)
check("S1.2 q on the alphabet: (q(2), q(3), q(5), q(6)) = %s == "
      "(-4,-4,2,8) = (-|mu4|, -|mu4|, |Z2|, h(D5))" % (qvals,),
      qvals == (-MU4, -MU4, Z2, H_D5), kill="K2")

pal = sp.expand(q.subs(t, G_CAR - t) - q)
check("S1.3 palindrome q(5-t) = q(t) identically (axis g_car/2); "
      "q(|Z2|) = q(N_fam) = -|mu4| BECAUSE 2 + 3 = 5 = g_car; "
      "reflection images of 5, 6 are %d, %d -- OUTSIDE the alphabet "
      "(typed: only {2,3} is complement-closed)"
      % (G_CAR - 5, G_CAR - 6),
      pal == 0 and Z2 + N_FAM == G_CAR
      and int(q.subs(t, Z2)) == int(q.subs(t, N_FAM)) == -MU4
      and (G_CAR - 5) not in ALPHABET and (G_CAR - 6) not in ALPHABET,
      kill="K2")

# ======================================================================
section("S2: the decoder polynomial D(y)")
# ======================================================================
D = sp.expand(sp.prod([y - v for v in qvals]))
D_target = y ** 4 - 2 * y ** 3 - 48 * y ** 2 - 32 * y + 256
D_factored = sp.expand((y + 4) ** 2 * (y - 2) * (y - 8))
check("S2.1 D(y) = prod (y - q(a)) = %s == (y+4)^2 (y-2)(y-8) == "
      "y^4 - 2y^3 - 48y^2 - 32y + 256" % D,
      sp.expand(D - D_target) == 0
      and sp.expand(D - D_factored) == 0, kill="K3")

coeffs = tuple(int(D.coeff(y, k)) for k in (3, 2, 1, 0))
check("S2.2 coefficients %s: 2 = |Z2|; 48 = Omega_adm = N_fam dim S+ "
      "= 3 x 16; 32 = 2^g_car = dim(S+ (+) S-); 256 = 2^rank(E8); "
      "double root -4 = -|mu4| forced by the palindrome pair {2,3}"
      % (coeffs,),
      coeffs == (-Z2, -OMEGA_ADM, -2 ** G_CAR, 2 ** RANK_E8)
      and OMEGA_ADM == N_FAM * 16 and 2 ** G_CAR == 32
      and qvals[0] == qvals[1] == -MU4, kill="K3")

# ======================================================================
section("S3: the Fourier bridge -- census Walsh law reproduced")
# ======================================================================
STD = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        STD.append(tuple(2 * a for a in v))
for yb in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in yb)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        STD.append(v)
STD = sorted(STD)


def in_L_std(v):
    if all(x % 2 == 0 for x in v):
        return sum(x // 2 for x in v) % 2 == 0
    if all(x % 2 == 1 for x in v):
        return sum(v) % 4 == 0
    return False


def in_pi2L_std(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L_std([x // 2 for x in w])


reps = []
label = {}
for r in STD:
    for li, rep in enumerate(reps):
        if in_pi2L_std(tuple(a - b for a, b in zip(r, rep))):
            label[r] = li
            break
    else:
        label[r] = len(reps)
        reps.append(r)
ZERO = (0,) * 8
REPS16 = [ZERO] + list(reps)


def cls16(v):
    return [k for k in range(16)
            if in_pi2L_std(tuple(a - b for a, b in zip(v, REPS16[k])))]


census = [0] * 16
for r in STD:
    census[label[r] + 1] += 1
check("S3.1 std-model census: %d classes + zero; census (zero; "
      "nonzero) = (%d; %s) == (0; 16 x15)"
      % (len(reps), census[0], sorted(set(census[1:]))),
      len(reps) == 15 and census[0] == 0
      and sorted(census[1:]) == [16] * 15, kill="K4")

ADD = [[None] * 16 for _ in range(16)]
add_ok = True
for a in range(16):
    for b in range(16):
        sv = tuple(x + z for x, z in zip(REPS16[a], REPS16[b]))
        hits = cls16(sv)
        if len(hits) != 1:
            add_ok = False
        else:
            ADD[a][b] = hits[0]
basis = []
for k in range(1, 16):
    closure = {0}
    frontier = [0]
    while frontier:
        x = frontier.pop()
        for g in basis:
            z = ADD[x][g]
            if z not in closure:
                closure.add(z)
                frontier.append(z)
    if k not in closure:
        basis.append(k)
COORD = {}
for bits in itertools.product((0, 1), repeat=4):
    c = 0
    for i, b in enumerate(bits):
        if b:
            c = ADD[c][basis[i]]
    COORD[c] = bits
RHAT = {}
for u in itertools.product((0, 1), repeat=4):
    RHAT[u] = sum((-1) ** (sum(a * b for a, b in zip(u, COORD[k])) % 2)
                  * census[k] for k in range(16))
U0 = (0, 0, 0, 0)
nz = sorted(set(RHAT[u] for u in RHAT if u != U0))
check("S3.2 Walsh: rhat(0) = %d == 240; rhat(u != 0) values %s == "
      "{-16}; lambda_msg = -16/240 = %s == -1/15"
      % (RHAT[U0], nz, Fr(-16, 240)),
      add_ok and len(COORD) == 16 and len(basis) == 4
      and RHAT[U0] == 240 and nz == [-16]
      and Fr(-16, 240) == Fr(-1, 15), kill="K4")

bridge = Fr(MU4 * int(q.subs(t, Z2)), R_E8)
bridge_fam = Fr(MU4 * int(q.subs(t, N_FAM)), R_E8)
check("S3.3 THE BRIDGE: |mu4| q(|Z2|)/|R(E8)| = 4 x (-4)/240 = %s == "
      "-1/15 == lambda_msg; same via q(N_fam) (palindrome route): %s; "
      "-16 = |mu4| q(|Z2|) = rhat(u)"
      % (bridge, bridge_fam),
      bridge == Fr(-1, 15) == bridge_fam
      and MU4 * int(q.subs(t, Z2)) == -16 == nz[0], kill="K4")

# ======================================================================
section("C: controls (each must fire)")
# ======================================================================
q2 = t ** 2 - t + 2
q3 = t ** 2 + t - 2
q_row = t ** 2 - 5 * t + 1
b2 = Fr(MU4 * int(q2.subs(t, Z2)), R_E8)
b3 = Fr(MU4 * int(q3.subs(t, Z2)), R_E8)
brow = Fr(MU4 * int(q_row.subs(t, Z2)), R_E8)
check("C1 FIRES: sibling directions collapse the bridge: q2 -> %s, "
      "q3 -> %s, q_row -> %s; none equals -1/15"
      % (b2, b3, brow),
      b2 == Fr(1, 15) and b3 == Fr(1, 15) and brow == Fr(-1, 12)
      and all(v != Fr(-1, 15) for v in (b2, b3, brow)), kill="K5")

ax2 = sp.Rational(1, 2)
ax3 = sp.Rational(-1, 2)
check("C2 FIRES: sibling palindromes: axis of q2 = %s, axis of q3 = %s "
      "(!= 5/2); q2(3) = %d != %d = q2(2): the 2 <-> 3 complement "
      "check-code dies off-direction"
      % (ax2, ax3, q2.subs(t, 3), q2.subs(t, 2)),
      sp.expand(q2.subs(t, 2 * ax2 - t) - q2) == 0
      and sp.expand(q3.subs(t, 2 * ax3 - t) - q3) == 0
      and ax2 != sp.Rational(5, 2) and ax3 != sp.Rational(5, 2)
      and int(q2.subs(t, 3)) == 8 != 4 == int(q2.subs(t, 2)), kill="K5")


def decoder(alphabet):
    return sp.expand(sp.prod([y - q.subs(t, a) for a in alphabet]))


D7 = decoder((2, 3, 5, 7))
D7_target = y ** 4 - 10 * y ** 3 - 96 * y ** 2 - 32 * y + 512
D1235 = decoder((1, 2, 3, 5))
D1235_target = y ** 4 + 8 * y ** 3 + 12 * y ** 2 - 32 * y - 64
D3567 = decoder((3, 5, 6, 7))
check("C3 FIRES: alternative alphabets: {2,3,5,7} -> %s (constant 512 "
      "= 2^9 NOT 2^rank(E8); q(7) = %d); {1,2,3,5} -> %s; both != D"
      % (D7, q.subs(t, 7), D1235),
      sp.expand(D7 - D7_target) == 0 and int(q.subs(t, 7)) == 16
      and sp.expand(D1235 - D1235_target) == 0
      and sp.expand(D7 - D) != 0 and sp.expand(D1235 - D) != 0
      and int(D7.coeff(y, 0)) == 512 != 256, kill="K5")
print("      HONEST LINE (typed, no kill): the -32 y coefficient "
      "survives in")
print("      BOTH alternatives (%s, %s) -- per-coefficient selectivity "
      "is weak;"
      % (int(D7.coeff(y, 1)), int(D1235.coeff(y, 1))))
print("      the selective object is the full vector (-2,-48,-32,+256).")
print("      6-vs-7 TENSION typed: replacing 6 = |R+(A3)| by 7 loses "
      "the y^3,")
print("      y^2 and constant identifications (10, 96, 512 are not "
      "compiler")
print("      atoms of this normal form).")
print("      MEASURED (report, not frozen): {3,5,6,7} -> %s" % D3567)

# ======================================================================
section("T: the typing (mandatory)")
# ======================================================================
print("  TYPING (verbatim): exact AUDIT theorem, NOT a physical functor")
print("  -- an explicit intertwiner would be needed to make it causal;")
print("  report only.")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if KILLS:
    VERDICT = {"K1": "ALPHABET-MISMATCH", "K2": "QVALUE-MISMATCH",
               "K3": "DECODER-MISMATCH", "K4": "BRIDGE-MISMATCH",
               "K5": "CONTROL-DEAD"}[KILLS[0]]
else:
    VERDICT = "WINDING-DECODER-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nPROMOTION-READY STATEMENT (report only -- no promotion, no edits):")
print("  THEOREM (winding decoder of the clock alphabet): the v857")
print("  winding quadratic q(t) = t^2 - g_car t + |Z2| maps the G31")
print("  clock alphabet {|Z2|, N_fam, g_car, |R+(A3)|} to the atom")
print("  quadruple (-|mu4|, -|mu4|, |Z2|, h(D5)) -- with q(|Z2|) =")
print("  q(N_fam) forced by the palindrome axis g_car/2 and 2 + 3 = 5;")
print("  the decoder D(y) = (y+4)^2 (y-2)(y-8) expands with signed")
print("  coefficients (|Z2|, Omega_adm, 2^g_car, 2^rank(E8)); and")
print("  |mu4| q(|Z2|)/|R(E8)| = -1/15 is EXACTLY the nonzero-character")
print("  Walsh eigenvalue of the Gaussian census (reproduced here on")
print("  the std-model roots).  Every sibling deformation direction")
print("  collapses the bridge; alternative alphabets change the")
print("  decoder (honest line: the -32 coefficient alone is not")
print("  selective).  TYPE: exact AUDIT theorem, NOT a physical")
print("  functor -- an explicit intertwiner would be needed to make it")
print("  causal; report only.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
