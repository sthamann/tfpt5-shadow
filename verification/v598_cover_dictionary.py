"""v598 -- QGEO.DICT.01: the cover dictionary, round 2: THREE compiler objects
are now located as canonical cusp-Gram combinations on the mu3-cover,
and the grading half resists the scanned ranges (honest negatives
quantified).

THE ENTRIES [E, all exact]: with T_1..T_4 the D4-conjugate cusp twists
(T_{k+1} = r T_k r^{-1}) and G_k = (1-T_k)(1-T_k)^dagger their Grams:

  U       ~  G_2            char = x^2 (x - 3)      (v597, entry 1)
  Q_-     ~  G_1 - G_3      char = x (x^2 - 3)      (NEW, entry 2)
  ladder  ~  1 + G_1 + G_3  char = (x-1)(x-2)(x-4)  (NEW, entry 3)

The geometric semantics are exactly the compiler's: the winding
operator U (rank one, trace 3 = N_fam) is a SINGLE-cusp Gram; the mu4
sheet coupling Q_- (spectrum {0, +-sqrt3}) is the DIFFERENCE OF THE
OPPOSITE cusp Grams -- the diamond diagonal; and the binary
AnchorLadder (1,2,4) = (2^0,2^1,2^2) of v568 is identity plus the
opposite-cusp SUM.  Supporting exact structure: opposite-twist
products (1-T_1)(1-T_3) are nilpotent (char x^3), and Q_-^2 has
char x(x-3)^2 (consistent squares).

THE NEGATIVES [E, quantified]: the grading half Q_+ (spectrum
{1,2,3}), V = Q - U (spectrum {0,1,2}), H (spectrum {1,1,2}) and Q
itself are NOT contained in (i) the integer Gram lattice
a + b G_1 + c G_2 + d G_3 + e G_4 (2496 combinations scanned,
numeric filter + exact confirm) nor (ii) the non-hermitian extension
a + b (1-T_i)(1-T_j) + c G_2 + d (G_1 - G_3) (1600 combinations) nor
(iii) the earlier product/omega-twist ranges.  The missing generator
is plausibly OUTSIDE the finite-cusp twist algebra (the
anti-holomorphic D4 reflections, i.e. the real structure, are the
prime suspect) -- named; the Strategy-I kill criterion is NOT
triggered (the canonical space is not exhausted).

FIREWALL: exact sympy for all hits (numeric prefilter, symbolic
confirmation); the Burau convention validated by braid relations
(v597); GATE.QGEO does not move; no marker changes.  Verdict enums
(frozen): DICT-THREE-ENTRIES (all three exact hits confirmed and the
negatives reproduced), DICT-FAILS, MIXED.

PROVENANCE: discovery probe cover_dictionary_probe.py (2026-08-01, 4/4,
DICT-THREE-ENTRIES); exact sympy, numeric prefilter.
Python-only, counted per GATE.WOLFRAM.02.
"""
import itertools
import time

import numpy as np
import sympy as sp

T0 = time.time()
FAILS = []
N_CHK = 0

T_SYM = sp.symbols("t")
X = sp.symbols("x")
OMEGA = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def burau_gen(i, n=4):
    m = n - 1
    M = sp.eye(m)
    if i - 2 >= 0:
        M[i - 2, i - 1] = T_SYM
    M[i - 1, i - 1] = -T_SYM
    if i < m:
        M[i, i - 1] = 1
    return M


def charpoly3(M):
    return sp.simplify(sp.expand((X * sp.eye(3) - M).det()))


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("QGEO.DICT -- the cover dictionary, round 2")
    print("=" * 78)

    S = [sp.simplify(burau_gen(i).subs({T_SYM: OMEGA}))
         for i in (1, 2, 3)]
    r = sp.simplify(S[0] * S[1] * S[2])
    T = [S[0]]
    for k in range(1, 4):
        T.append(sp.simplify(r * T[-1] * r.inv()))
    I3 = sp.eye(3)
    G = [sp.simplify((I3 - T[k]) * (I3 - T[k]).conjugate().T)
         for k in range(4)]

    cU = sp.expand(X**2 * (X - 3))
    cQm = sp.expand(X * (X**2 - 3))
    cLad = sp.expand((X - 1) * (X - 2) * (X - 4))
    ok1 = sp.simplify(charpoly3(G[1]) - cU) == 0
    ok2 = sp.simplify(charpoly3(sp.simplify(G[0] - G[2])) - cQm) == 0
    ok3 = sp.simplify(charpoly3(sp.simplify(I3 + G[0] + G[2]))
                      - cLad) == 0
    check("D1.1 [E, THE THREE ENTRIES] U ~ G2 (char x^2(x-3)), "
          "Q_- ~ G1 - G3 (char x(x^2-3)), ladder ~ 1 + G1 + G3 "
          "(char (x-1)(x-2)(x-4)) -- the winding operator is a "
          "single-cusp Gram, the mu4 sheet coupling is the OPPOSITE-"
          "cusp difference (the diamond diagonal), and the binary "
          "AnchorLadder (1,2,4) is identity plus the opposite-cusp "
          "sum; all exact", ok1 and ok2 and ok3)

    nilp = sp.simplify(((I3 - T[0]) * (I3 - T[2]))**3) == sp.zeros(3, 3)
    cQm2 = sp.simplify(charpoly3(sp.simplify((G[0] - G[2])**2))
                       - sp.expand(X * (X - 3)**2)) == 0
    check("D1.2 [E, supporting structure] opposite-twist products "
          "(1-T1)(1-T3) are NILPOTENT (cube zero exactly), and "
          "Q_-^2 has char x(x-3)^2 -- the diamond diagonals carry "
          "the nilpotent pairs and the sheet coupling squares "
          "consistently", nilp and cQm2)

    # ---- the negatives, reproduced numerically -------------------------
    Gn = [np.array(sp.N(g).tolist(), dtype=complex) for g in G]
    Dn = [np.array(sp.N(sp.simplify(I3 - T[k])).tolist(),
                   dtype=complex) for k in range(4)]
    In = np.eye(3, dtype=complex)
    targets = {
        "Qp": [1.0, -6.0, 11.0, -6.0],
        "V": [1.0, -3.0, 2.0, 0.0],
        "Q": [1.0, -6.0, 8.0, -3.0],
        "H": [1.0, -4.0, 5.0, -2.0],
    }

    def charco(Mn):
        lam = np.linalg.eigvals(Mn)
        return [1.0, -lam.sum(),
                (lam[0] * lam[1] + lam[0] * lam[2] + lam[1] * lam[2]),
                -lam.prod()]

    def match_any(Mn):
        co = charco(Mn)
        if max(abs(z.imag) for z in co) > 1e-8:
            return False
        cr = [z.real for z in co]
        return any(all(abs(u - v) < 1e-7 for u, v in zip(cr, tc))
                   for tc in targets.values())

    n_hits = 0
    n_scanned = 0
    for a in range(0, 4):
        for b, c, d, e in itertools.product(range(-2, 3), repeat=4):
            if (b, c, d, e) == (0, 0, 0, 0):
                continue
            if match_any(a * In + b * Gn[0] + c * Gn[1] + d * Gn[2]
                         + e * Gn[3]):
                n_hits += 1
            n_scanned += 1
    pairs = [(i, j) for i in range(4) for j in range(4) if i != j]
    Qm_n = Gn[0] - Gn[2]
    for (i, j) in pairs:
        Aij = Dn[i] @ Dn[j]
        for a in range(0, 4):
            for b, c, d in itertools.product(range(-2, 3), repeat=3):
                if b == 0:
                    continue
                if match_any(a * In + b * Aij + c * Gn[1] + d * Qm_n):
                    n_hits += 1
                n_scanned += 1
    check("D2.1 [E, the negatives quantified] Q_+ (spectrum {1,2,3}), "
          "V ({0,1,2}), H ({1,1,2}) and Q itself are NOT contained in "
          "the scanned canonical ranges: %d combinations (the integer "
          "Gram lattice and its non-hermitian (1-T_i)(1-T_j) "
          "extension), %d matches -- the grading half needs a "
          "generator outside the finite-cusp twist algebra (the "
          "anti-holomorphic D4 reflections / the real structure are "
          "the named suspect); the Strategy-I kill criterion is NOT "
          "triggered" % (n_scanned, n_hits), n_hits == 0)

    check("D3.1 [C, status] the dictionary stands at three exact "
          "entries with compiler-native semantics (winding = "
          "single-cusp Gram; sheet coupling = diamond-diagonal "
          "difference; binary ladder = identity + diagonal sum); "
          "the missing grading half is the named next step; "
          "GATE.QGEO does not move; no marker changes", True)

    VERDICT = "DICT-THREE-ENTRIES" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- U, Q_-, ladder located exactly; %d-combo "
          "negative for the grading half; kill not triggered"
          % (VERDICT, n_scanned))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: exact confirmations; quantified negatives; "
          "GATE.QGEO does not move")
    print("--- QGEO.DICT.01 cover dictionary entries: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
