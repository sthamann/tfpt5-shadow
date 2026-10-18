#!/usr/bin/env python3
"""dilation_coherent_toy_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (DYN.UNITARY.DILATION.01 [O], demand D1 at kernel level):
after v976 proved the DEPLOYED Kraus dilation K_ij = sqrt(T_ij)|i><j| is
measure-and-prepare (entanglement breaking, quantum capacity 0), does the
seam single step B admit ANY exact unitary dilation with a FINITE fresh
environment that PRESERVES the classically hidden quantum data?  This
probe constructs one explicitly: the Birkhoff-fibre channel Psi_t (the
v976 random-unitary family over S3 permutations) realized as a
repeated-interaction / collision model with ONE 6-dimensional fresh
ancilla per step.

  [EXACT] 1. the Birkhoff base: B = (1/2)I + (1/18)P12 + (2/9)P13 +
        (2/9)P23 bit-exact, B^6 = T_v221 (spectrum {1, 64/729, 1/729});
        the fibre family w_t(pi) = w_0(pi) + t*sgn(pi), t in [0, 1/18],
        reproduces B as a matrix for EVERY t (sum sgn(pi) Pi_pi = 0).
  [EXACT] 2. STINESPRING/COLLISION DILATION: V|psi> = sum_pi
        sqrt(w_t(pi)) (Pi_pi|psi>) tensor |pi>_E is an exact isometry
        (V^dag V = I_3 symbolically in t) and Tr_E V rho V^dag = Psi_t(rho)
        on the complete operator basis (9 matrix units, symbolic in t).
        One step = one unitary interaction with a FRESH 6-dim ancilla;
        n steps = n fresh ancillas (repeated-interaction model).
  [EXACT] 3. POPULATIONS ARE B, t-FREE: diag(Psi_t(|j><j|)) = B e_j for
        every j identically in t -- the Markov matrix is the DEPHASED
        SHADOW of the dilation (the master-route dynamics order:
        unitary -> decoherence -> Markov, exhibited at kernel level).
  [EXACT] 4. THE HIDDEN DATUM SURVIVES: the triangle ring current A
        (Hermitian, diag 0) is an exact eigen-observable,
        Psi_t(A) = 6t A -- the dilation transports the v976
        discriminator; the deployed Kraus dilation kills it (checked).
  [EXACT] 5. NOT ENTANGLEMENT BREAKING: Choi(Psi_t)^{T2} has an exact
        NEGATIVE eigenvalue at rational fibre points (t = 0 and
        t = 1/36 evaluated exactly), reproducing the v976 full-level
        law lambda_min = -(1/3)(2/3) = -2/9 at n = 1, t-independent --
        the collision dilation realizes a genuinely quantum channel,
        in exact contrast to the EB Kraus dilation (Choi diagonal).

HONEST SCOPE: this closes NOTHING in DYN.UNITARY.DILATION.01 -- it
exhibits demand D1 at the FINITE KERNEL level only (a local dilation with
finite fresh environment exists and preserves the coherent data).  D2
(size consistency in the thermodynamic limit), D3 (Lieb-Robinson bound)
and D4 (OS continuation) are field-level statements untouched here; the
physical selection of the fibre point t stays [O] (v976).

VERDICT ENUM: DILATION_COLLISION_EXACT (kernel level; D2-D4 open).
"""
import hashlib
import sys

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def spec_sha():
    with open(__file__, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def perm_matrix(p):
    """3x3 permutation matrix sending basis vector j -> p[j]."""
    M = sp.zeros(3, 3)
    for j in range(3):
        M[p[j], j] = 1
    return M


def main():
    print("dilation_coherent_toy_probe -- exact collision-model dilation "
          "of the seam single step (DYN.UNITARY.DILATION.01 D1, kernel "
          "level)")

    t = sp.Symbol("t", nonnegative=True)

    # S3: identity, two 3-cycles (even), three transpositions (odd)
    perms = {
        "I":    ([0, 1, 2], +1),
        "C123": ([1, 2, 0], +1),
        "C132": ([2, 0, 1], +1),
        "P12":  ([1, 0, 2], -1),
        "P13":  ([2, 1, 0], -1),
        "P23":  ([0, 2, 1], -1),
    }
    Pi = {k: perm_matrix(p) for k, (p, s) in perms.items()}
    sgn = {k: s for k, (p, s) in perms.items()}

    w0 = {"I": sp.Rational(1, 2), "C123": 0, "C132": 0,
          "P12": sp.Rational(1, 18), "P13": sp.Rational(2, 9),
          "P23": sp.Rational(2, 9)}
    wt = {k: w0[k] + t * sgn[k] for k in perms}

    # 1. base identities
    B = sum((w0[k] * Pi[k] for k in perms), sp.zeros(3, 3))
    one = sp.ones(3, 1)
    u2 = sp.Matrix([1, -1, 0])
    u3 = sp.Matrix([1, 1, -2])
    J = one * one.T / 3
    P2 = u2 * u2.T / (u2.T * u2)[0]
    P3 = u3 * u3.T / (u3.T * u3)[0]
    T221 = J + sp.Rational(64, 729) * P2 + sp.Rational(1, 729) * P3
    check("B = (1/2)I + (1/18)P12 + (2/9)P13 + (2/9)P23 bit-exact and "
          "B^6 = T_v221 (spectrum {1, 64/729, 1/729})",
          sp.simplify(B ** 6 - T221) == sp.zeros(3, 3))
    B_t = sum((wt[k] * Pi[k] for k in perms), sp.zeros(3, 3))
    check("fibre: sum_pi w_t(pi) Pi_pi = B for EVERY t (sgn direction in "
          "the Birkhoff kernel); weights >= 0 exactly on t in [0, 1/18]",
          sp.simplify(B_t - B) == sp.zeros(3, 3)
          and all(sp.simplify(wt[k].subs(t, sp.Rational(1, 18))) >= 0
                  for k in perms))

    # 2. Stinespring isometry V: C^3 -> C^3 (x) C^6
    # (row block e carries sqrt(w_e) Pi_e; environment basis |pi>_E)
    keys = list(perms.keys())
    V = sp.zeros(18, 3)
    for e, k in enumerate(keys):
        blk = sp.sqrt(wt[k]) * Pi[k]
        V[e * 3:(e + 1) * 3, 0:3] = blk
    check("V^dag V = I_3 symbolically in t (exact isometry; environment "
          "= 6-dim FRESH ancilla per step -- collision model)",
          sp.simplify(V.T * V - sp.eye(3)) == sp.zeros(3, 3))

    def psi_channel(rho):
        return sp.simplify(sum((wt[k] * Pi[k] * rho * Pi[k].T
                                for k in perms), sp.zeros(3, 3)))

    def dilated(rho):
        big = V * rho * V.T
        out = sp.zeros(3, 3)
        for e in range(6):
            out += big[e * 3:(e + 1) * 3, e * 3:(e + 1) * 3]
        return sp.simplify(out)

    ok = True
    for a in range(3):
        for b in range(3):
            Eab = sp.zeros(3, 3)
            Eab[a, b] = 1
            ok = ok and sp.simplify(dilated(Eab) - psi_channel(Eab)) \
                == sp.zeros(3, 3)
    check("Tr_E V rho V^dag = Psi_t(rho) on the COMPLETE operator basis "
          "(9 matrix units), symbolic in t", ok)

    # 3. populations = B, t-free
    ok = True
    for j in range(3):
        Ejj = sp.zeros(3, 3)
        Ejj[j, j] = 1
        out = psi_channel(Ejj)
        col = sp.Matrix([out[i, i] for i in range(3)])
        ok = ok and sp.simplify(col - B[:, j]) == sp.zeros(3, 1)
    check("populations: diag(Psi_t(|j><j|)) = B e_j identically in t -- "
          "the Markov matrix is the dephased shadow (unitary -> "
          "decoherence -> Markov exhibited)", ok)

    # 4. ring current eigen-observable
    A = sp.Matrix([[0, sp.I, -sp.I], [-sp.I, 0, sp.I], [sp.I, -sp.I, 0]])

    def psi_c(rho):
        return sum((wt[k] * Pi[k] * rho * Pi[k].T for k in perms),
                   sp.zeros(3, 3))

    check("hidden datum: Psi_t(A) = 6t A exactly (Hermitian ring current,"
          " diag 0 -- the v976 discriminator transported by the dilation)",
          sp.simplify(psi_c(A) - 6 * t * A) == sp.zeros(3, 3))
    # deployed Kraus dilation kills it: Phi_K(rho) = sum_ij T_ij <j|rho|j>
    # |i><i| is diagonal-valued => Phi_K(A) = 0 since diag(A) = 0
    PhiK_A = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            PhiK_A[i, i] += T221[i, j] * A[j, j]
    check("contrast: the deployed measure-and-prepare Kraus dilation "
          "sends A to 0 (kills the coherent datum)",
          sp.simplify(PhiK_A) == sp.zeros(3, 3))

    # 5. NPT at rational fibre points (n = 1): Choi and partial transpose
    def choi_pt_min(tval):
        wts = {k: sp.nsimplify(wt[k].subs(t, tval)) for k in perms}
        C = sp.zeros(9, 9)
        for a in range(3):
            for b in range(3):
                Eab = sp.zeros(3, 3)
                Eab[a, b] = 1
                out = sum((wts[k] * Pi[k] * Eab * Pi[k].T
                           for k in perms), sp.zeros(3, 3))
                for r in range(3):
                    for c in range(3):
                        C[a * 3 + r, b * 3 + c] = out[r, c]
        C = C / 3                     # normalized Choi state J = C/d
        # partial transpose on the SECOND (output) factor
        PT = sp.zeros(9, 9)
        for a in range(3):
            for b in range(3):
                blk = C[a * 3:(a + 1) * 3, b * 3:(b + 1) * 3].T
                PT[a * 3:(a + 1) * 3, b * 3:(b + 1) * 3] = blk
        eigs = PT.eigenvals()
        return min(eigs.keys(), key=lambda e: sp.N(e, 30))

    m0 = choi_pt_min(sp.Integer(0))
    m1 = choi_pt_min(sp.Rational(1, 36))
    check("NOT EB: lambda_min(Choi(Psi_t)^{T2}) = -2/9 exactly at t = 0 "
          "AND t = 1/36 (the v976 full-level law -(1/3)(2/3)^n at n = 1, "
          "t-independent) -- the collision dilation is genuinely quantum",
          sp.simplify(m0 + sp.Rational(2, 9)) == 0
          and sp.simplify(m1 + sp.Rational(2, 9)) == 0,
          "min eigs: %s, %s" % (m0, m1))

    check("HONEST SCOPE (typed): D1 exhibited at kernel level only; D2 "
          "(size uniformity), D3 (Lieb-Robinson), D4 (OS continuation) "
          "are field-level and untouched; the fibre point t stays "
          "unselected [O]", True)

    npass = sum(CHECKS)
    print("-" * 70)
    print("CHECKS %d/%d PASS" % (npass, len(CHECKS)))
    print("VERDICT: DILATION_COLLISION_EXACT (kernel-level D1; D2-D4 and "
          "fibre-point selection open)")
    print("SPEC_SHA %s" % spec_sha()[:16])
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
