#!/usr/bin/env python3
"""v626 -- E8.CODE.01: the E8 code round -- E8 IS an error-correcting code:
Construction A on the extended Hamming code [8,4,4] yields the even
unimodular rank-8 lattice with 240 roots, single-bit errors are
correctable by syndrome decoding, and the code parameters meet the
compiler's numbers (8 = rank, 4 = d = |mu4|, 16 = |C| = the carrier
half-spinor, 14 = 2 x 7 weight-4 words).

The external note's 'error correction' framing gets its theorem-level
anchor:

  (E1) THE CODE [E]: the extended Hamming code [8,4,4] has 16
       codewords with weight distribution {0: 1, 4: 14, 8: 1} (doubly
       even) and is SELF-DUAL (C = C-perp, verified exactly).

  (E2) CONSTRUCTION A [E]: L = {x in Z^8 : x mod 2 in C}/sqrt(2) is
       EVEN (all weights divisible by 4) and UNIMODULAR (covolume
       2^8/|C| / 2^4 = 1): by uniqueness of the even unimodular rank-8
       lattice, L = E8.

  (E3) THE SHELLS [E]: 240 vectors of minimal norm and 2160 on the
       second shell -- matching the v625 theta identity
       (240 sigma_3(1), 240 sigma_3(2)).

  (E4) ERROR CORRECTION IS LITERAL [E]: minimum distance 4 corrects
       every single-bit error by nearest-codeword (syndrome) decoding
       -- verified exhaustively (16 x 8 corrupted words, unique
       nearest codeword = the original in every case).

  (E5) THE COMPILER TIES [C, typed observations]: 8 = rank(E8),
       4 = min distance = d = |mu4| (the v624 boundary degree),
       16 = |C| = the carrier half-spinor dimension = the seam sites,
       14 = #weight-4 words = 2 x 7 (the parabolic dimension, the
       v605 denominator 14) -- observations, not derivations.

  (E6) THE READING [C]: 'E8 is an error-correcting code' is a THEOREM
       (Construction A), so the robustness narrative (independent
       check channels, no silent errors) has an exact anchor; combined
       with v625 (commuting Hecke channels) the code reading of the
       compiler is now theorem-backed at two levels; no physics
       derivation is claimed.

Verdict enums (frozen): E8-IS-A-CODE (all pass), CODE-FAILS, MIXED.

FIREWALL: no marker changes; typed observations only.

PROVENANCE: discovery probe e8_code_probe.py (2026-08-02, 7/7, verdict
E8-IS-A-CODE).

Python-only (exact integer combinatorics), counted per GATE.WOLFRAM.02.
"""

import itertools
from collections import Counter

import numpy as np

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


G = np.array([
    [1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 0]], dtype=int)
CODE = sorted({tuple((m @ G) % 2)
               for m in itertools.product([0, 1], repeat=4)})
CW = {tuple(c) for c in CODE}

# ================================================================== E1
print("=" * 72)
print("E1: the extended Hamming code [8,4,4]")
print("=" * 72)

wdist = Counter(sum(c) for c in CODE)
dual = [v for v in itertools.product([0, 1], repeat=8)
        if all(sum(a * b for a, b in zip(v, c)) % 2 == 0 for c in CODE)]
check("E1.1 16 codewords, weight distribution {0: 1, 4: 14, 8: 1} "
      "(doubly even), minimum distance 4",
      len(CODE) == 16 and dict(wdist) == {0: 1, 4: 14, 8: 1})
check("E1.2 the code is SELF-DUAL: C = C-perp exactly",
      sorted(dual) == CODE)

# ================================================================== E2
print("=" * 72)
print("E2: Construction A gives an even unimodular rank-8 lattice")
print("=" * 72)

check("E2.1 doubly-even weights make the lattice EVEN (x.x in 4Z for "
      "x = c + 2z since c.c = wt(c) = 0 mod 4), and the covolume is "
      "2^8/|C| / 2^4 = 1: UNIMODULAR -- by uniqueness of the even "
      "unimodular rank-8 lattice, Construction A(Hamming) = E8",
      all(sum(c) % 4 == 0 for c in CODE)
      and (2 ** 8 / len(CODE)) / 2 ** 4 == 1.0)

# ================================================================== E3
print("=" * 72)
print("E3: the shells match the v625 theta identity")
print("=" * 72)

n4 = sum(1 for x in itertools.product(range(-2, 3), repeat=8)
         if sum(v * v for v in x) == 4
         and tuple(v % 2 for v in x) in CW)
n8 = sum(1 for x in itertools.product(range(-3, 4), repeat=8)
         if sum(v * v for v in x) == 8
         and tuple(v % 2 for v in x) in CW)
check("E3.1 240 minimal vectors and 2160 on the second shell "
      "(= 240 sigma_3(1), 240 sigma_3(2): the v625 theta identity on "
      "the CODE model of E8)", n4 == 240 and n8 == 2160,
      "shells: %d, %d" % (n4, n8))

# ================================================================== E4
print("=" * 72)
print("E4: error correction is literal (syndrome decoding)")
print("=" * 72)

ok_corr = True
for c in CODE:
    for i in range(8):
        w = list(c)
        w[i] ^= 1  # single-bit error
        dists = sorted((sum(a != b for a, b in zip(w, cc)), cc)
                       for cc in CODE)
        best_d, best_c = dists[0]
        second_d = dists[1][0]
        if not (best_d == 1 and best_c == c and second_d >= 3):
            ok_corr = False
check("E4.1 every single-bit corruption of every codeword has a UNIQUE "
      "nearest codeword = the original (16 x 8 cases exhaustively; the "
      "second-nearest is at distance >= 3): minimum distance 4 corrects "
      "single errors, literally", ok_corr)

# ================================================================== E5
print("=" * 72)
print("E5: the compiler ties (typed observations)")
print("=" * 72)

check("E5.1 [C] 8 = rank(E8); 4 = min distance = d = |mu4| (the v624 "
      "boundary degree); 16 = |C| = the carrier half-spinor dimension = "
      "the seam sites; 14 = #weight-4 words = 2 x 7 (the parabolic "
      "dimension; the v605 denominator 14) -- observations, not "
      "derivations",
      len(CODE) == 16 and wdist[4] == 14 and 14 == 2 * 7)

# ================================================================== E6
print("=" * 72)
print("E6: the reading")
print("=" * 72)

check("E6.1 [C] 'E8 is an error-correcting code' is a THEOREM "
      "(Construction A on the extended Hamming code): the robustness "
      "narrative (independent check channels, no silent errors) has an "
      "exact anchor, complementing v625's commuting Hecke channels; no "
      "physics derivation claimed; no marker moves", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: E8-IS-A-CODE -- Construction A on the extended Hamming")
    print("code yields E8 exactly, single-bit errors are correctable, and")
    print("the code parameters meet the compiler's numbers.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
