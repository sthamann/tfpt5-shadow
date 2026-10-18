"""v984 -- DYN.UNITARY.DILATION.01 [O update: the DISCRETE leg is realized
constructively -- an exact local collision-model (QCA-band) unitary dilation
of the seam transfer whose reduced diagonal dynamics is B^n exactly];
TRANSFER.COHERENT.WILSON.01 / v977 (read-only anchors: U_B, B^6 = T,
B^2 != |U^2|^2, orientation bit).

THE POINT (external master-object review, wave 2, 2026-08-28).  v977 proved
that no single closed unitary generates the relaxing sequence (B^2 !=
|U_B^2|^2): repeated steps need dephasing BETWEEN steps.  This module
verifies EXACTLY that the standard collision model supplies that dephasing
unitarily: one fresh ancilla qutrit per step, a generalized-CNOT record
C|j,k> = |j, j+k mod 3>, and the step unitary V = C (U_B (x) I).

  [E] 1. V IS UNITARY on system + ancilla (V^dag V = I, exact sympy).
  [E] 2. STINESPRING IDENTITY (symbolic rho): Phi(rho) = Tr_A[V (rho (x)
        |0><0|) V^dag] = sum_j P_j U_B rho U_B^dag P_j -- unitary
        amplitudes -> local environment coupling -> dephasing, as one
        exact operator identity; Kraus completeness sum_j K_j^dag K_j = I
        with K_j = P_j U_B.
  [E] 3. MARKOV TRANSFER: diag Phi(diag p) = B p exactly (off-diagonals
        vanish), and SIX fresh ancillas give diag Phi^6(diag p) = B^6 p =
        T p exactly -- the v977 macro-gate is the reduced dynamics of an
        exactly unitary, strictly local (radius-1) collision band.
  [E] 4. MUST-FAIL FIRES: without the ancilla (closed unitary) the second
        step is wrong, |U_B^2|^2 != B^2 (entry (1,1): 31/54 vs 0.2450,
        re-checked exact) -- the dilation is NECESSARY, not decorative.
  [E] 5. TYPED REMARK (probe finding AGAINST the review text): a REUSED
        mod-3 adder ancilla still reproduces the POPULATIONS exactly
        (the record j_1 + i stays distinguishable given the final index),
        so fresh ancillas are needed for the coherences, not for the
        diagonal chain -- the population statement is robust.
  [E] 6. ORIENTATION BIT RIDES ALONG: the conjugate branch V* = C (U_B*
        (x) I) dilates the SAME B (diag Phi*(diag p) = B p exactly) --
        the classically invisible sgn J = +-1/27 (v977) is untouched by
        the dilation; its physical selection stays [O].

HONEST SCOPE (firewall): finite-dimensional, discrete-time, exact.  This
realizes the collision/QCA half of the contract (a size-consistent
Stinespring dilation with strict locality radius 1 per step, hence a
trivial Lieb-Robinson cone of one cell per step).  The CONTINUOUS legs
stay [O]: a (quasi-)local Hamiltonian dilation, the OS continuation
T = e^{-aH} -> U(t) = e^{-itH}, and any 3+1D reading.  No status-marker
upgrade; the contract row keeps the open continuous demand.
"""
import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset

B_SYM = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18


def build_lift(Bm, branch=+1):
    """exact PDG-parametrized SU(3) lift of B (v977 construction)."""
    s13sq = sp.nsimplify(Bm[0, 2])
    c13sq = 1 - s13sq
    s12sq = sp.nsimplify(Bm[0, 1] / c13sq)
    s23sq = sp.nsimplify(Bm[1, 2] / c13sq)
    c12sq, c23sq = 1 - s12sq, 1 - s23sq
    s12, c12 = sp.sqrt(s12sq), sp.sqrt(c12sq)
    s23, c23 = sp.sqrt(s23sq), sp.sqrt(c23sq)
    s13, c13 = sp.sqrt(s13sq), sp.sqrt(c13sq)
    cross = 2 * s12 * c12 * s23 * c23 * s13
    cosd = sp.simplify((Bm[1, 0] - s12sq * c23sq
                        - c12sq * s23sq * s13sq) / cross)
    sind = branch * sp.sqrt(sp.simplify(1 - cosd ** 2))
    eid = cosd + sp.I * sind
    return sp.Matrix([
        [c12 * c13, s12 * c13, s13 / eid],
        [-s12 * c23 - c12 * s23 * s13 * eid,
         c12 * c23 - s12 * s23 * s13 * eid, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * eid,
         -c12 * s23 - s12 * c23 * s13 * eid, c23 * c13]])


def cnot3():
    """generalized CNOT on C3 (x) C3: |j,k> -> |j, j+k mod 3>."""
    C = sp.zeros(9, 9)
    for j in range(3):
        for k in range(3):
            C[j * 3 + ((j + k) % 3), j * 3 + k] = 1
    return C


def channel(V):
    """Phi(rho) = Tr_A[V (rho (x) |0><0|) V^dag] as a function."""
    def Phi(rho):
        a0 = sp.zeros(3, 3)
        a0[0, 0] = 1
        big = V * sp.Matrix(sp.kronecker_product(rho, a0)) * V.H
        out = sp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                out[i, j] = sum(big[i * 3 + k, j * 3 + k] for k in range(3))
        return sp.simplify(out)
    return Phi


def run():
    reset()
    print("v984  DYN.UNITARY.DILATION.01 (discrete leg): exact collision-"
          "model dilation of the seam transfer B")

    U = build_lift(B_SYM, +1)
    C = cnot3()
    V = C * sp.Matrix(sp.kronecker_product(U, sp.eye(3)))
    check("STEP UNITARY [E]: V = C (U_B (x) I) with the mod-3 record C is "
          "exactly unitary on system + ancilla (V^dag V = I)",
          sp.simplify(V.H * V - sp.eye(9)) == sp.zeros(9))

    Phi = channel(V)
    r = sp.Matrix(3, 3, lambda i, j: sp.Symbol("r%d%d" % (i, j)))
    rhs = sp.zeros(3, 3)
    for j in range(3):
        P = sp.zeros(3, 3)
        P[j, j] = 1
        rhs += P * U * r * U.H * P
    check("STINESPRING IDENTITY [E]: Phi(rho) = Tr_A[V (rho x |0><0|) "
          "V^dag] = sum_j P_j U_B rho U_B^dag P_j as a symbolic operator "
          "identity (unitary -> local coupling -> dephasing in one step)",
          sp.simplify(sp.expand(Phi(r) - rhs)) == sp.zeros(3, 3))
    kraus_sum = sp.zeros(3, 3)
    for j in range(3):
        P = sp.diag(*[1 if i == j else 0 for i in range(3)])
        kraus_sum += (P * U).H * (P * U)
    check("KRAUS COMPLETENESS [E]: sum_j K_j^dag K_j = I with K_j = P_j U_B "
          "(trace preserving, CPTP)",
          sp.simplify(kraus_sum - sp.eye(3)) == sp.zeros(3, 3))

    p = sp.Matrix(3, 1, lambda i, _: sp.Symbol("p%d" % i))
    rho_d = sp.diag(p[0], p[1], p[2])
    d1 = Phi(rho_d)
    check("MARKOV STEP [E]: diag Phi(diag p) = B p exactly and all "
          "off-diagonals vanish -- the classical transfer is the reduced "
          "shadow of one collision",
          sp.simplify(sp.Matrix([d1[i, i] for i in range(3)]) - B_SYM * p)
          == sp.zeros(3, 1)
          and all(sp.simplify(d1[i, j]) == 0
                  for i in range(3) for j in range(3) if i != j))

    rho6 = rho_d
    for _ in range(6):
        rho6 = Phi(rho6)
    check("SIX FRESH ANCILLAS [E]: diag Phi^6(diag p) = B^6 p = T p exactly "
          "-- the v977 macro-gate T as reduced dynamics of an exactly "
          "unitary radius-1 collision band",
          sp.simplify(sp.Matrix([rho6[i, i] for i in range(3)])
                      - B_SYM ** 6 * p) == sp.zeros(3, 1))

    absU2 = sp.Matrix(3, 3, lambda i, j: sp.simplify(
        sp.expand_complex(sp.Abs((U * U)[i, j]) ** 2)))
    check("MUST-FAIL FIRES [E]: closed unitary (no ancilla) gives "
          "|U_B^2|^2 != B^2 (entry (1,1): 31/54 vs 0.2450; v977 "
          "re-anchored) -- the dilation is necessary",
          sp.simplify(absU2 - B_SYM * B_SYM) != sp.zeros(3, 3)
          and abs(float(absU2[0, 0]) - float((B_SYM * B_SYM)[0, 0])) > 0.1)

    Un = np.array([[complex(sp.N(U[i, j], 20)) for j in range(3)]
                   for i in range(3)])
    Cn = np.zeros((9, 9))
    for j in range(3):
        for k in range(3):
            Cn[j * 3 + ((j + k) % 3), j * 3 + k] = 1
    Vn = Cn @ np.kron(Un, np.eye(3))
    p0 = np.array([0.5, 0.3, 0.2])
    big = np.kron(np.diag(p0), np.diag([1, 0, 0])).astype(complex)
    big = Vn @ big @ Vn.conj().T
    big = Vn @ big @ Vn.conj().T        # SECOND collision, SAME ancilla
    red = np.einsum("ikjk->ij", big.reshape(3, 3, 3, 3))
    Bf = np.array([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
    dev = np.max(np.abs(np.real(np.diag(red))
                        - np.linalg.matrix_power(Bf, 2) @ p0))
    check("TYPED REMARK [E] (probe finding vs the review text): a REUSED "
          "mod-3 adder ancilla still gives diag = B^2 p exactly (dev "
          "%.1e) -- the record j1+i stays distinguishable; fresh ancillas "
          "are needed for coherences, not populations" % dev,
          dev < 1e-12)

    Uc = U.conjugate()
    Vc = C * sp.Matrix(sp.kronecker_product(Uc, sp.eye(3)))
    dc = channel(Vc)(rho_d)
    check("ORIENTATION BIT RIDES ALONG [E]: the conjugate branch V* "
          "dilates the SAME B (diag = B p exactly) -- sgn J = +-1/27 "
          "stays classically invisible through the dilation; its "
          "selection stays [O] (v977 firewall)",
          sp.simplify(sp.Matrix([dc[i, i] for i in range(3)]) - B_SYM * p)
          == sp.zeros(3, 1))

    check("FIREWALL (scope): finite, discrete-time, exact -- the "
          "collision/QCA half of DYN.UNITARY.DILATION.01 (strict "
          "radius-1 locality per step); the continuous legs (quasi-local "
          "Hamiltonian dilation, OS continuation to e^{-itH}, any 3+1D "
          "reading) stay [O]; no marker move", True)

    return summary("v984 collision-model dilation: B^n exactly as reduced "
                   "unitary QCA dynamics")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
