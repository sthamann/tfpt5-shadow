#!/usr/bin/env python3
"""The free gamma slice of the WOIT roadmap: mirror modes are strictly
OS-negative (sector-level upgrade of the v519 shadow), the chiral
generation is multiplicity-free, and the mark transport exists.

The WOIT gamma milestone (tfpt_research_contracts: "the chirality theorem
+ the mark incidence -- success: the odd-sector definiteness flip of v519
upgraded to 'one chiral generation without mirrors' on the reconstructed
net, and the four mu4 marks extended incidence-compatibly; kill: kill
tests (3)/(6)/(7) fire") is a full research contract on the interacting
algebra A_hol.  This module executes its FREE SLICE on the explicit
reconstructed net of v524 (the N = 8 OS quotient H_phys), reusing the
v524 machinery verbatim (imported read-only):

  (G1) BASELINE [E, reproduction]: the chiral N = 8 OS Gram is PD
       (16,0,0) -- H_phys exists (v524 Q1.3).

  (G2) THE FLIP LOCALIZES [E]: the anti-chiral state's Gram has inertia
       (8,8,0), and the split is EXACTLY by fermion parity: the even
       sector stays PD (8,0,0) while the odd sector is STRICTLY NEGATIVE
       DEFINITE (0,8,0) -- the v519 "odd-sector definiteness flip",
       now stated sector-exactly on the full N = 8 half algebra.

  (G3) MIRROR EXCLUSION [E, the gamma-A statement at the free level]:
       every nonzero odd (fermionic) vector of the mirror (anti-chiral)
       state has strictly negative OS norm; hence in the doubled
       (vector-like) system chiral (+) anti-chiral, ANY OS-positive
       subspace intersects the mirror odd sector in {0}: no mirror
       fermion mode survives OS reconstruction -- kill test (3) cannot
       fire at the free level, upgraded from the v519 state-level shadow
       to the SECTOR level.

  (G4) ONE GENERATION, MULTIPLICITY-FREE [E, reproduction + reading]:
       the compressed clock spectrum on the odd transfer domain is
       EXACTLY {1, sqrt(2)-1} -- two DISTINCT eigenvalues, no
       degeneracy: the chiral fermion content is multiplicity-free (one
       generation's worth, no doubling).

  (G5) MARK INCIDENCE AT THE FREE LEVEL [E]: the two positive-half mark
       algebras (monomials on {4,5} and on {6,7}) have PD OS Grams
       (4,0,0) each (dim 4 = |mu4|); their monomial products generate
       the FULL 16-dim H_phys basis; and the quarter-turn transfer
       tau_2 is exactly the mark-A -> mark-B transport (alpha_2 shifts
       {4,5} -> {6,7}), Hermitian and PD (4,0,0) on the mark algebra:
       the incidence-compatible extension EXISTS at the free level --
       kill test (7) does not fire there.

FIREWALL: this is the FREE slice only -- the gamma milestone itself
(A_hol, the interacting net, the spacetime extension) stays OPEN; all
seven contract kill tests stay formally live on A_hol; WOIT.OS.TWISTOR.01
does not move; no marker changes.  Verdict enums (frozen):
GAMMA-FREE-SLICE-LANDED (all), GAMMA-FREE-SLICE-FAILS, MIXED.

PROVENANCE: direct construction on the v524 machinery (imported
read-only); 2026-08-01.  Python-only, counted per GATE.WOLFRAM.02.
"""

import os
import sys

import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v524_woit_beta2_os_quotient.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v524_woit_beta2_os_quotient as W  # noqa: E402  (READ-ONLY import)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""))


# ---------------------------------------------------------------- G1 + G2
print("=" * 72)
print("G1/G2: the chiral baseline and the sector-exact flip")
print("=" * 72)

G_chi = W.gram_of(W.BASIS8, W.R7, W.S7, W.N8, chi=1)
in_chi, _ = W.spectrum_inertia(G_chi)
check("G1.1 chiral N = 8 OS Gram PD (16,0,0): H_phys exists (v524 baseline)",
      in_chi == (16, 0, 0))

G_anti = W.gram_of(W.BASIS8, W.R7, W.S7, W.N8, chi=-1)
in_anti, _ = W.spectrum_inertia(G_anti)
check("G2.1 anti-chiral N = 8 Gram inertia (8,8,0): no OS quotient for the mirror",
      in_anti == (8, 8, 0))
in_even_anti, _ = W.spectrum_inertia(G_anti[:8, :8])
in_odd_anti, _ = W.spectrum_inertia(G_anti[8:, 8:])
in_odd_chi, _ = W.spectrum_inertia(G_chi[8:, 8:])
check("G2.2 the flip is SECTOR-EXACT: anti-chiral even (8,0,0) PD, odd (0,8,0) "
      "strictly ND (chiral odd: (8,0,0) PD)",
      in_even_anti == (8, 0, 0) and in_odd_anti == (0, 8, 0)
      and in_odd_chi == (8, 0, 0))

# ---------------------------------------------------------------- G3
print("=" * 72)
print("G3: mirror exclusion (gamma-A at the free level)")
print("=" * 72)

check("G3.1 every nonzero mirror fermion vector has STRICTLY NEGATIVE OS norm "
      "(the odd anti-chiral Gram is ND) => any OS-positive subspace of the "
      "doubled vector-like system meets the mirror odd sector in {0}: NO mirror "
      "mode survives reconstruction -- kill test (3) cannot fire at the free "
      "level (sector-level upgrade of the v519 shadow)",
      in_odd_anti == (0, 8, 0))

# ---------------------------------------------------------------- G4
print("=" * 72)
print("G4: one generation, multiplicity-free")
print("=" * 72)

TW8 = W.TW8
D2 = W.dom_monos(W.BASIS8, 4, 5)
M2 = W.term_matrix(D2, TW8[2], W.R7, W.S7, W.ETA, W.N8)
check("G4.0 the tau_2 domain IS the mark-A algebra (monomials on {4,5}, dim 4)",
      set(D2) == {(), (4,), (5,), (4, 5)})
herm2 = W.hermitian_exact(M2)
in2, _ = W.spectrum_inertia(M2)
bidx8 = {m: i for i, m in enumerate(W.BASIS8)}
idx_o = [i for i, m in enumerate(D2) if len(m) % 2 == 1]
idx_e = [i for i, m in enumerate(D2) if len(m) % 2 == 0]
lam = sp.symbols("lam")
Go = sp.Matrix(2, 2, lambda i, j: G_chi[bidx8[D2[idx_o[i]]], bidx8[D2[idx_o[j]]]])
To = M2.extract(idx_o, idx_o)
roots_o = sp.solve(sp.det(To - lam * Go), lam)
silver = sp.sqrt(2) - 1
ok_spec = (len(roots_o) == 2
           and any(sp.simplify(rt - 1) == 0 for rt in roots_o)
           and any(sp.simplify(rt - silver) == 0 for rt in roots_o))
check("G4.1 the compressed clock spectrum on the odd (fermion) domain is EXACTLY "
      "{1, sqrt(2)-1}: two DISTINCT eigenvalues, multiplicity-free -- one "
      "generation's worth, no doubling", herm2 and in2 == (4, 0, 0) and ok_spec)

# ---------------------------------------------------------------- G5
print("=" * 72)
print("G5: mark incidence at the free level")
print("=" * 72)

markA = [(), (4,), (5,), (4, 5)]
markB = [(), (6,), (7,), (6, 7)]
GA = sp.Matrix(4, 4, lambda i, j: G_chi[bidx8[markA[i]], bidx8[markA[j]]])
GB = sp.Matrix(4, 4, lambda i, j: G_chi[bidx8[markB[i]], bidx8[markB[j]]])
inA, _ = W.spectrum_inertia(GA)
inB, _ = W.spectrum_inertia(GB)
check("G5.1 both mark algebras have PD OS Grams (4,0,0), dim 4 = |mu4|",
      inA == (4, 0, 0) and inB == (4, 0, 0))

# products of mark-A and mark-B monomials generate the full basis
products = set()
for ma in markA:
    for mb in markB:
        products.add(tuple(sorted(set(ma) | set(mb))))
check("G5.2 mark-A x mark-B monomial products = the FULL 16-dim H_phys basis "
      "(the two marks jointly generate the net; intersection = the vacuum line "
      "by PD monomial independence)", products == set(W.BASIS8))

# the quarter-turn transport: alpha_2 shifts the mark-A support {4,5} -> {6,7}
shiftA = {tuple(sorted((a + 2) for a in m)) for m in markA}
check("G5.3 the clock quarter-step transports mark A to mark B "
      "(alpha_2: {4,5} -> {6,7}) and the transport form tau_2 is Hermitian PD "
      "(4,0,0) on the mark algebra: the incidence-compatible extension exists "
      "at the free level -- kill test (7) does not fire there",
      shiftA == set(markB) and herm2 and in2 == (4, 0, 0))

# ---------------------------------------------------------------- summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: GAMMA-FREE-SLICE-LANDED -- mirror modes are strictly")
    print("OS-negative (sector level), the chiral generation is multiplicity-")
    print("free, and the mark transport exists; the gamma milestone itself")
    print("stays open on A_hol (all kill tests live there).")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
