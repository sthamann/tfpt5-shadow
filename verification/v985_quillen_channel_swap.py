"""v985 -- ALPHA.QUILLEN.EXACT.01 [O update: the CHANNEL-SWAP face resolved
at the finite level by mu4-character grading]; companions v974 (read-only
anchors: BFK jump matrix, mark matrix, swapped kernels, doublet ratio).

THE POINT (external master-object review, wave 2, 2026-08-28).  v974 found
that the BFK jump matrix and the TFPT mark matrix agree channel-wise in the
mu4 Fourier basis but hold their kernels in SWAPPED characters (the jump
matrix kills the gauge/zero-mode k = 0 channel, the mark matrix kills the
sign-rep k = 2 channel), so the UNGRADED determinants cannot be compared
globally.  The review proposes the character-GRADED determinant

    log det'_gr Delta = sum_r (-1)^r log det'(Delta |_{P_r H})

with the deck/Hodge swap P_0 <-> P_2, P_1 <-> P_3.  This module makes that
exact at the finite level:

  [E] 1. SPECTRA: jump pattern circ(2,-1,0,-1) has mu4 eigenvalues
        [0, 2, 4, 2] (kernel at k = 0); mark pattern circ(0,1,2,1) has
        [4, -2, 0, -2] (kernel at k = 2) -- the v974 swapped-kernel fact
        re-derived symbolically.
  [E] 2. THE DECK SWAP WORKS: r -> r + 2 maps the |spectrum| pattern of
        the jump matrix onto the mark pattern EXACTLY ([0,2,4,2] ->
        [4,2,0,2] = |[4,-2,0,-2]|) -- after the swap the two kernels sit
        in the SAME channel and the graded comparison is well defined.
  [E] 3. MUST-FAIL FIRES: the odd swap r -> r + 1 does NOT match -- the
        grading is selected by the Z2 deck (P_0 <-> P_2, P_1 <-> P_3),
        not arbitrary.
  [E] 4. GRADED DETERMINANT IS UNIT-CLEAN: with physical units restored
        (jump = 16 c3 x pattern, mark = 4 c3 ln2 x pattern), the graded
        det' difference is c3-FREE: gr(jump) - gr(mark) = log(ln2/4)
        exactly -- the seam constant CANCELS in the graded object (the
        v974 doublet ratio 4/ln2 is its ungraded shadow), so the graded
        determinant compares the two kernels without any c3-dependent
        normalization ambiguity.

HONEST SCOPE (firewall): finite 4x4 mu4 circulant matrices only (the v974
finite witnesses).  NOT verified here and stays [O]: the continuum
Bismut-Freed identification, the KMS/state-rigidity leg, the claimed
compensation of the local BFK constant 2^-4 by the Quillen metric, and the
from-first-principles exactness of F_U(1) (the named target).  alpha^-1 is
neither touched nor re-derived; no status-marker move.
"""
import sympy as sp

from tfpt_constants import check, summary, reset

JUMP_PATTERN = [2, -1, 0, -1]      # v974: R_0 = 16 c3 circ(2,-1,0,-1)
MARK_PATTERN = [0, 1, 2, 1]        # v484/v974: G_marks = -4 c3 ln2 circ(0,1,2,1)


def mu4_spectrum(pattern):
    """exact mu4-character eigenvalues of circ(pattern)."""
    i_ = sp.I
    return [sp.simplify(sum(pattern[m] * i_ ** (m * k) for m in range(4)))
            for k in range(4)]


def graded_logdet(eigs, unit):
    """sum_r (-1)^r log|lambda_r * unit| over the nonzero channels."""
    return sum((-1) ** k * sp.log(sp.Abs(e) * unit)
               for k, e in enumerate(eigs) if e != 0)


def run():
    reset()
    print("v985  ALPHA.QUILLEN.EXACT.01 channel-swap face: the mu4-graded "
          "determinant (finite level)")

    eig_jump = mu4_spectrum(JUMP_PATTERN)
    eig_mark = mu4_spectrum(MARK_PATTERN)
    check("SPECTRA [E]: jump circ(2,-1,0,-1) -> [0, 2, 4, 2] (kernel k=0); "
          "mark circ(0,1,2,1) -> [4, -2, 0, -2] (kernel k=2) -- the v974 "
          "swapped-kernel fact symbolically",
          eig_jump == [0, 2, 4, 2] and eig_mark == [4, -2, 0, -2])

    swapped = [sp.Abs(eig_jump[(k + 2) % 4]) for k in range(4)]
    check("DECK SWAP [E]: r -> r+2 (P0 <-> P2, P1 <-> P3) maps the jump "
          "|spectrum| onto the mark pattern EXACTLY ([0,2,4,2] -> "
          "[4,2,0,2]) -- after the swap both kernels sit in the same "
          "channel, the graded comparison is well defined",
          swapped == [sp.Abs(e) for e in eig_mark])

    odd = [sp.Abs(eig_jump[(k + 1) % 4]) for k in range(4)]
    check("MUST-FAIL FIRES [E]: the odd swap r -> r+1 does NOT match -- "
          "the grading is selected by the Z2 deck, not arbitrary",
          odd != [sp.Abs(e) for e in eig_mark])

    c3s = sp.Symbol("c3", positive=True)
    g_jump = graded_logdet(eig_jump, 16 * c3s)
    g_mark = graded_logdet(eig_mark, 4 * c3s * sp.log(2))
    diff = sp.simplify(g_jump - g_mark)
    check("GRADED DET' UNIT-CLEAN [E]: gr(jump) - gr(mark) = log(ln2/4) "
          "exactly, c3-FREE -- the seam constant cancels in the graded "
          "object (v974's doublet ratio 4/ln2 is its ungraded shadow)",
          sp.simplify(diff - sp.log(sp.log(2) / 4)) == 0)

    ratios = [sp.simplify((16 * c3s * sp.Abs(eig_jump[(k + 2) % 4]))
                          / (4 * c3s * sp.log(2) * sp.Abs(eig_mark[k])))
              for k in range(4) if eig_mark[k] != 0]
    check("UNIFORM CHANNEL RATIO [E]: after the deck swap the ratio "
          "(16 c3 |lambda^J_{r+2}|)/(4 c3 ln2 |lambda^M_r|) = 4/ln2 in "
          "EVERY matched nonzero channel (c3 cancels) -- v974's doublet "
          "ratio extends to full channelwise uniformity; the graded "
          "difference log(ln2/4) is its signed sum (+1-1-1)",
          all(sp.simplify(x - 4 / sp.log(2)) == 0 for x in ratios)
          and len(ratios) == 3)

    check("FIREWALL (scope): finite 4x4 mu4 circulants only; continuum "
          "Bismut-Freed, KMS rigidity, the 2^-4/Quillen-metric "
          "compensation and the exactness of F_U(1) stay [O]; alpha^-1 "
          "untouched; no marker move", True)

    return summary("v985 graded channel swap: deck grading resolves the "
                   "v974 kernel swap at the finite level")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
