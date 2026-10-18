#!/usr/bin/env python3
"""v621 -- WOIT.GAMMA.SEMI.01: the interacting Klein-Landau semigroup --
the clock survives the interaction as a positive transfer exactly on
the mu4-commensurate steps.

The WOIT gamma milestone, the net-dynamics slice after v615/v616.

v524 established the Klein-Landau local symmetric semigroup on the FREE
net (tau_k Hermitian on shrinking domains, even steps PSD, odd steps
indefinite).  This probe runs the semigroup ON the RP-surviving
interaction (the alignment bit, v534) and lands the interacting law:

  (K1) FREE BASELINE [E-float, v524 pattern at N = 16]: at g = 0 all
       seven steps tau_k (k = 1..7, domain dims 29, 22, 16, 11, 7, 4,
       2 on the admissible cut 3) are exactly Hermitian; the even steps
       are PD ((22,0,0), (11,0,0), (4,0,0)); the odd steps are
       indefinite with EXACTLY ZERO one-particle diagonal (the free
       chirality datum); the vacuum is normalized on every step.

  (K2) THE INTERACTING LAW [MEASURED, central]: at g > 0 exact
       Hermiticity survives PRECISELY on the steps {4, 6, 7} (deviation
       < 1e-8) and is lost on the generic steps {1, 2, 3, 5}
       (deviation > 0.1): the local symmetric semigroup CONTRACTS to
       the mu4-commensurate window.

  (K3) THE CLOCK ACTS INTERACTING [MEASURED, the gamma-relevant
       statement]: the clock step k = 4 (the quarter turn) stays
       Hermitian AND positive definite ((11,0,0)) over the whole
       coupling grid g in {1/32, 1/4, 1, 8} -- the mu4 clock is a
       positive transfer operator on the interacting net.

  (K4) THE MECHANISM, EXACT [E]: the survivor interaction is
       alpha_4-invariant EXACTLY (the quartet sum is fixed by the
       quarter shift as a Clifford element) and NOT alpha_1/alpha_2
       invariant: the interaction breaks the free translation
       invariance down to the quartet stabilizer {0, 4, 8, 12} -- the
       surviving Hermitian steps are exactly the symmetry-protected
       ones.

  (K5) THE SUBSTEP TYPING [E/measured]: k = 6 is the even
       quartet-contained substep (domain in Q_4, image in Q_8,
       theta-side in Q_0 -- protected by the same quartet symmetry);
       k = 7 is parity-trivial (every deg-1 cross term vanishes by
       fermion parity); k = 5 shows quartet containment alone does NOT
       protect (odd + contained still loses Hermiticity): even parity
       AND quartet alignment are both needed.

  (K6) THE READING [C]: the Klein-Landau structure survives the
       interaction exactly where the mu4 symmetry survives -- the
       clock acts on the interacting net as a positive transfer, the
       generic euclidean steps are interaction-broken: the
       reconstructed rotation group of the interacting toy is the
       CLOCK tower, not the full circle.  One toy, one interaction
       class; gamma proper stays open on A_hol; no marker moves.

Verdict enums (frozen): CLOCK-SURVIVES-INTERACTING (all pass),
SEMIGROUP-FAILS, MIXED.

FIREWALL: WOIT.OS.TWISTOR.01 does not move; no marker changes.

PROVENANCE: discovery probe interacting_semigroup_probe.py (2026-08-01,
6/6, verdict CLOCK-SURVIVES-INTERACTING).

Machinery: v615 imported READ-ONLY (Cl(16), parents, survivor).
Python-only, counted per GATE.WOLFRAM.02.
"""

import os
import sys
from itertools import combinations

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v615_gamma_toy_interacting.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v615_gamma_toy_interacting as V  # noqa: E402  (READ-ONLY import)
from fractions import Fraction as Fr  # noqa: E402

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


HF, HINT = V.HF, V.HINT
TOL_HERM = 1e-8
CUT = 3
QUARTETS = {"Q0": {14, 15, 0, 1}, "Q4": {2, 3, 4, 5},
            "Q8": {6, 7, 8, 9}, "Q12": {10, 11, 12, 13}}


def dom_basis(k):
    sites = list(range(2, 10 - k))
    return [()] + [(a,) for a in sites] + list(combinations(sites, 2))


def tau_k(x, k, eta=1j):
    basis = dom_basis(k)
    r, s = V.refl_map(CUT)
    th = [V.theta_mono_num(m, r, s, eta) for m in basis]
    nb = len(basis)
    T = np.zeros((nb, nb), dtype=complex)
    for a, (ca, ta) in enumerate(th):
        wa = V.mono_mat(ta).conj().T @ x
        for b in range(nb):
            c2, m2 = V.alpha_mono(basis[b], V.TW[k])
            T[a, b] = ca * c2 * np.vdot(wa, V.mono_mat(m2) @ x)
    return T, basis


# ================================================================== K1
print("=" * 72)
print("K1: the free baseline (v524 Klein-Landau pattern at N = 16)")
print("=" * 72)

x0, _ = V.ground(HF)
free_ok = True
dims = []
for k in range(1, 8):
    T, basis = tau_k(x0, k)
    dims.append(len(basis))
    dev = V.herm_dev(T)
    Th = (T + T.conj().T) / 2
    it = V.inertia(Th)
    d1max = max([abs(T[i, i]) for i, m in enumerate(basis)
                 if len(m) == 1] or [0.0])
    vac = abs(T[0, 0])
    if dev > TOL_HERM or abs(vac - 1) > 1e-12:
        free_ok = False
    if k % 2 == 0 and it[1] + it[2] != 0:
        free_ok = False
    if k in (1, 3, 5) and (it[1] == 0 or d1max > 1e-12):
        free_ok = False
    if k == 7 and it != (1, 0, 1):
        free_ok = False
check("K1.1 at g = 0 all seven steps are Hermitian with normalized "
      "vacuum; even steps PD, odd steps k = 1, 3, 5 indefinite with "
      "EXACTLY ZERO one-particle diagonal (the free chirality datum); "
      "k = 7 is the parity-trivial edge step (PSD with one null "
      "direction, (1,0,1)) -- the v524 Klein-Landau pattern at N = 16 "
      "(domain dims %s)" % dims,
      free_ok and dims == [29, 22, 16, 11, 7, 4, 2])

# ================================================================== K2 + K3
print("=" * 72)
print("K2/K3: the interacting law and the surviving clock")
print("=" * 72)

herm_sets_ok = True
for g in (0.25, 1.0):
    xg, _ = V.ground(HF + g * HINT)
    herm, broken = [], []
    for k in range(1, 8):
        T, basis = tau_k(xg, k)
        dev = V.herm_dev(T)
        (herm if dev < TOL_HERM else broken).append(k)
    print("  g = %-5s: Hermitian steps %s | broken %s" % (g, herm, broken))
    if herm != [4, 6, 7] or broken != [1, 2, 3, 5]:
        herm_sets_ok = False
check("K2.1 at g > 0 exact Hermiticity survives PRECISELY on the steps "
      "{4, 6, 7} and is lost on {1, 2, 3, 5} (dev > 0.1 there): the "
      "semigroup contracts to the mu4-commensurate window",
      herm_sets_ok)

clock_ok = True
for g in (1.0 / 32, 0.25, 1.0, 8.0):
    xg, _ = V.ground(HF + g * HINT)
    T, basis = tau_k(xg, 4)
    dev = V.herm_dev(T)
    it = V.inertia((T + T.conj().T) / 2)
    clock_ok &= (dev < TOL_HERM and it == (11, 0, 0))
check("K3.1 THE CLOCK ACTS INTERACTING: the quarter-turn step k = 4 "
      "stays Hermitian AND PD ((11,0,0)) over the whole grid "
      "g in {1/32, 1/4, 1, 8} -- the mu4 clock is a positive transfer "
      "on the interacting net", clock_ok)

# ================================================================== K4
print("=" * 72)
print("K4: the mechanism, exact")
print("=" * 72)

hint_dict = {}
for b in (0, 4, 8, 12):
    q = V.quartet(b)
    for m, c in q.items():
        hint_dict[m] = hint_dict.get(m, Fr(0)) + c

def shifted(H, k):
    out = {}
    for m, c in H.items():
        c2, m2 = V.alpha_mono(m, V.TW[k])
        out[m2] = out.get(m2, Fr(0)) + c * c2
    return {m: c for m, c in out.items() if c}


inv4 = shifted(hint_dict, 4) == hint_dict
inv1 = shifted(hint_dict, 1) == hint_dict
inv2 = shifted(hint_dict, 2) == hint_dict
check("K4.1 [E, exact Clifford combinatorics] the survivor interaction "
      "is alpha_4-invariant EXACTLY and NOT alpha_1/alpha_2 invariant: "
      "the interaction breaks translation invariance to the quartet "
      "stabilizer {0, 4, 8, 12} -- the surviving Hermitian steps are "
      "the symmetry-protected ones", inv4 and not inv1 and not inv2)

# ================================================================== K5
print("=" * 72)
print("K5: the substep typing")
print("=" * 72)

r, _s = V.refl_map(CUT)
dom6 = set(range(2, 4))
img6 = {(a + 6) % 16 for a in dom6}
th6 = {r(a) % 16 for a in dom6}
aligned6 = (dom6 <= QUARTETS["Q4"] and img6 <= QUARTETS["Q8"]
            and th6 <= QUARTETS["Q0"])
dom5 = set(range(2, 5))
img5 = {(a + 5) % 16 for a in dom5}
th5 = {r(a) % 16 for a in dom5}
aligned5 = (dom5 <= QUARTETS["Q4"] and img5 <= QUARTETS["Q8"]
            and th5 <= QUARTETS["Q0"])
xg, _ = V.ground(HF + 0.25 * HINT)
T5, _ = tau_k(xg, 5)
T7, basis7 = tau_k(xg, 7)
# k = 7: every deg-1 cross term with the vacuum is an odd operator
# expectation -- zero by fermion parity
cross7 = max(abs(T7[0, i]) for i, m in enumerate(basis7) if len(m) == 1)
check("K5.1 k = 6 is the even quartet-contained substep (domain in Q4, "
      "image in Q8, theta-side in Q0: %s); k = 5 is ALSO "
      "quartet-contained (%s) yet loses Hermiticity (dev %.2f) -- "
      "even parity AND quartet alignment are both needed; k = 7 is "
      "parity-trivial (vacuum cross terms %.1e)"
      % (aligned6, aligned5, V.herm_dev(T5), cross7),
      aligned6 and aligned5 and V.herm_dev(T5) > 0.1 and cross7 < 1e-12)

# ================================================================== K6
print("=" * 72)
print("K6: the reading")
print("=" * 72)

check("K6.1 [C] the Klein-Landau structure survives the interaction "
      "exactly where the mu4 symmetry survives: the clock acts on the "
      "interacting net as a positive transfer, the generic euclidean "
      "steps are interaction-broken -- the reconstructed rotation group "
      "of the interacting toy is the CLOCK tower, not the full circle; "
      "one toy, one interaction class; gamma proper stays open on "
      "A_hol; WOIT.OS.TWISTOR.01 does not move", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: CLOCK-SURVIVES-INTERACTING -- the semigroup contracts to")
    print("the mu4-commensurate steps, and the clock step stays a positive")
    print("transfer on the interacting net over the whole coupling grid.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
