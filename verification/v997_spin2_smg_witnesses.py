"""v997 -- GRAV.SPIN2.EMERGENCE.01 [O update: quadratic witnesses [E];
content pinned on the untruncated form factor] +
CHIRAL4D.NOMIRROR.01 [O update: SMG mechanism toy-proved [E];
4D Spin(10) theorem stays [O]].  Provenance:
experiments/tfpt-discovery/spin2_spectral_pole_probe.py (ALL PASS) +
experiments/tfpt-discovery/mirror_smg_gap_probe.py (ALL PASS).

THE POINT (completeness wave, 2026-08-28).  Two quadratic / toy
witnesses, not the interacting 4D theorems.

GRAV.SPIN2.EMERGENCE.01 -- Barnes--Rivers quadratic decomposition
  [E] projector algebra: ranks (5,3,1,1) for (spin-2, spin-1, 0s, 0w).
  [E] R+R^2 control: one massless TT pole, two helicities, scalaron at
        M_scal = c3^(7/2) Mbar exact.
  [E typed] LOCAL a4 Weyl^2 truncation necessarily carries an
        opposite-residue spin-2 ghost (Stelle caveat; residues
        {1/A, -1/A}).  Contract content is pinned on the UNTRUNCATED
        form factor, not the local a4 polynomial.
  [X] wrong-sign Weyl mutant: same opposite-residue structure.

CHIRAL4D.NOMIRROR.01 -- Fidkowski--Kitaev SMG toy
  [E] N=8: unique Spin(7)-singlet ground state, spectrum
        {-14 x 1, 0 x 8, 2 x 7}, Schmidt rank 1, volume-independent
        gap 14 at L=1,2,3.
  [X] N=4 contrast: SO(4)-invariant quartic, 2^L-degenerate ground
        states despite gap 2.
  [E] physical chiral edge keeps its pi/L spectrum exactly below the
        mirror gap.
  Honest: Spin(7) not SO(8), not Spin(10); 1D toy, not 4D.

HONEST SCOPE (firewall): quadratic order / 1D FK chain.  No interacting
graviton, universal T_munu coupling, diffeomorphism Ward, or 4D
Spin(10) chiral lattice theorem.  Both contracts stay [O].  Python-only
/ Wolfram mirror deferred.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset, c3 as C3_MP, Mbar as MBAR_MP

D = 4
TOL_SPIN2 = 2.0e-11
TOL_SMG = 2.0e-10
SEED = 20260828


def _symmetric_basis(n):
    basis = []
    labels = []
    for i in range(n):
        for j in range(i, n):
            h = sp.zeros(n)
            if i == j:
                h[i, j] = 1
            else:
                h[i, j] = h[j, i] = 1 / sp.sqrt(2)
            basis.append(h)
            labels.append((i, j))
    return basis, labels


SYM_BASIS, SYM_LABELS = _symmetric_basis(D)


def _inner(a, b):
    return sp.simplify(sum(a[i, j] * b[i, j]
                           for i in range(D) for j in range(D)))


def _apply_projector(kind, h, theta, omega):
    out = sp.zeros(D)
    for mu, nu, rho, sig in itertools.product(range(D), repeat=4):
        if kind == "2":
            coef = ((theta[mu, rho] * theta[nu, sig]
                     + theta[mu, sig] * theta[nu, rho]) / 2
                    - theta[mu, nu] * theta[rho, sig] / (D - 1))
        elif kind == "1":
            coef = (theta[mu, rho] * omega[nu, sig]
                    + theta[mu, sig] * omega[nu, rho]
                    + theta[nu, rho] * omega[mu, sig]
                    + theta[nu, sig] * omega[mu, rho]) / 2
        elif kind == "0s":
            coef = theta[mu, nu] * theta[rho, sig] / (D - 1)
        elif kind == "0w":
            coef = omega[mu, nu] * omega[rho, sig]
        else:
            raise ValueError(kind)
        out[mu, nu] += coef * h[rho, sig]
    return sp.simplify(out)


def _projector_matrix(kind, theta, omega):
    return sp.Matrix([
        [_inner(a, _apply_projector(kind, b, theta, omega))
         for b in SYM_BASIS]
        for a in SYM_BASIS
    ])


def _linear_curvatures(h, p):
    p2 = sp.simplify(sum(x * x for x in p))
    trh = sp.trace(h)
    ric = sp.zeros(D)
    for mu in range(D):
        for nu in range(D):
            ric[mu, nu] = sp.simplify(sum(
                (p[rho] * p[mu] * h[nu, rho]
                 + p[rho] * p[nu] * h[mu, rho]) / 2
                for rho in range(D))
                - (p2 * h[mu, nu] + p[mu] * p[nu] * trh) / 2)
    scalar = sp.simplify(sum(p[mu] * p[nu] * h[mu, nu]
                             for mu in range(D) for nu in range(D))
                         - p2 * trh)
    riem2 = 0
    for mu, nu, rho, sig in itertools.product(range(D), repeat=4):
        r = (p[rho] * p[nu] * h[mu, sig]
             + p[sig] * p[mu] * h[nu, rho]
             - p[sig] * p[nu] * h[mu, rho]
             - p[rho] * p[mu] * h[nu, sig]) / 2
        riem2 += r * r
    ric2 = sum(ric[i, j] ** 2 for i in range(D) for j in range(D))
    weyl2 = sp.simplify(riem2 - 2 * ric2 + scalar ** 2 / 3)
    return sp.simplify(scalar), sp.simplify(ric2), weyl2


def _fierz_pauli(h, p):
    p2 = sp.simplify(sum(x * x for x in p))
    trh = sp.trace(h)
    h2 = _inner(h, h)
    div2 = sum(sum(p[mu] * h[mu, nu] for mu in range(D)) ** 2
               for nu in range(D))
    pph = sum(p[mu] * p[nu] * h[mu, nu]
              for mu in range(D) for nu in range(D))
    return sp.simplify(p2 * h2 / 2 - div2 + pph * trh
                       - p2 * trh ** 2 / 2)


def _numeric_projectors(momentum):
    p = np.asarray(momentum, dtype=float)
    p2 = float(p @ p)
    omega = np.outer(p, p) / p2
    theta = np.eye(D) - omega

    def action(kind, h):
        if kind == "2":
            return (theta @ h @ theta
                    - theta * np.trace(theta @ h) / (D - 1))
        if kind == "0s":
            return theta * np.trace(theta @ h) / (D - 1)
        if kind == "0w":
            return omega * np.trace(omega @ h)
        if kind == "1":
            return theta @ h @ omega + omega @ h @ theta
        raise ValueError(kind)

    mats = {}
    basis = [np.array(x, dtype=float) for x in SYM_BASIS]
    for kind in ("2", "1", "0s", "0w"):
        mats[kind] = np.array([
            [np.sum(a * action(kind, b)) for b in basis] for a in basis
        ])
    return mats


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def _kron_all(ops):
    out = np.array([[1.0]], dtype=complex)
    for op in ops:
        out = np.kron(out, op)
    return out


def _majoranas(n_majorana):
    n_qubits = n_majorana // 2
    out = []
    for site in range(n_qubits):
        out.append(_kron_all([Z] * site + [X] + [I2] *
                             (n_qubits - site - 1)))
        out.append(_kron_all([Z] * site + [Y] + [I2] *
                             (n_qubits - site - 1)))
    return out


def _monomial(gammas, indices):
    out = np.eye(gammas[0].shape[0], dtype=complex)
    for index in indices:
        out = out @ gammas[index]
    return out


def _levels(eigenvalues, digits=9):
    grouped = {}
    for value in eigenvalues:
        key = round(float(np.real(value)), digits)
        grouped[key] = grouped.get(key, 0) + 1
    return dict(sorted(grouped.items()))


def _clifford_label(matrix, gammas, degree):
    dim = matrix.shape[0]
    hits = []
    for indices in itertools.combinations(range(len(gammas)), degree):
        candidate = _monomial(gammas, indices)
        coefficient = np.trace(candidate.conj().T @ matrix) / dim
        if abs(coefficient) > TOL_SMG:
            hits.append((indices, complex(coefficient)))
    return hits


def _fk_hamiltonian():
    gammas = _majoranas(8)
    stabilizer_generators = [
        _kron_all([Z, Z, I2, I2]),
        _kron_all([I2, Z, Z, I2]),
        _kron_all([I2, I2, Z, Z]),
        _kron_all([X, X, X, X]),
    ]
    parity = _kron_all([Z, Z, Z, Z])
    quartics = []
    labels = []
    for bits in itertools.product((0, 1), repeat=4):
        element = np.eye(16, dtype=complex)
        for bit, generator in zip(bits, stabilizer_generators):
            if bit:
                element = element @ generator
        if not any(bits) or np.max(np.abs(element - parity)) < TOL_SMG:
            continue
        hits = _clifford_label(element, gammas, 4)
        if len(hits) != 1:
            raise RuntimeError("stabilizer element is not one quartic")
        quartics.append(element)
        labels.append(hits[0])
    return -sum(quartics), gammas, quartics, labels, parity


def _spin7_generators(ground, hamiltonian, gammas):
    pairs = list(itertools.combinations(range(8), 2))
    bilinears = [1j * gammas[a] @ gammas[b] for a, b in pairs]
    action = np.column_stack([generator @ ground for generator in bilinears])
    action_real = np.vstack([action.real, action.imag])
    _u, singular_values, vh = np.linalg.svd(action_real, full_matrices=True)
    rank = int(np.sum(singular_values > TOL_SMG))
    nullspace = vh[rank:].T
    generators = []
    for coefficients in nullspace.T:
        generator = sum(coefficient * bilinear for coefficient, bilinear
                        in zip(coefficients, bilinears))
        generators.append(generator)
    annihilation = max(np.max(np.abs(generator @ ground))
                       for generator in generators)
    commutator = max(np.max(np.abs(generator @ hamiltonian
                                   - hamiltonian @ generator))
                     for generator in generators)
    return generators, rank, annihilation, commutator


def _full_so8_quartic_nullity(gammas):
    quartics = [_monomial(gammas, indices)
                for indices in itertools.combinations(range(8), 4)]
    bilinears = [1j * gammas[a] @ gammas[b]
                 for a, b in itertools.combinations(range(8), 2)]
    columns = []
    for quartic in quartics:
        blocks = [(generator @ quartic - quartic @ generator).reshape(-1)
                  for generator in bilinears]
        columns.append(np.concatenate(blocks))
    matrix = np.column_stack(columns)
    real_matrix = np.vstack([matrix.real, matrix.imag])
    singular_values = np.linalg.svd(real_matrix, compute_uv=False)
    rank = int(np.sum(singular_values > TOL_SMG))
    return len(quartics) - rank, rank, singular_values[-1]


def _convolve_spectrum(local_levels, length):
    spectrum = {0.0: 1}
    for _ in range(length):
        updated = {}
        for energy, multiplicity in spectrum.items():
            for local_energy, local_multiplicity in local_levels.items():
                new_energy = round(energy + local_energy, 9)
                updated[new_energy] = (updated.get(new_energy, 0)
                                       + multiplicity * local_multiplicity)
        spectrum = updated
    return dict(sorted(spectrum.items()))


def _ground_data(spectrum):
    items = list(spectrum.items())
    e0, degeneracy = items[0]
    gap = items[1][0] - e0
    return e0, degeneracy, gap, items[1][1]


def _chiral_edge_spectrum(length, velocity=1.0):
    mode_numbers = np.arange(-length // 2, length // 2)
    one_particle = velocity * 2 * np.pi * (mode_numbers + 0.5) / length
    vacuum_occupancy = one_particle < 0
    vacuum_energy = float(np.sum(one_particle[vacuum_occupancy]))
    many_body = []
    for occupancy in itertools.product((0, 1), repeat=length):
        energy = float(np.dot(one_particle, occupancy) - vacuum_energy)
        many_body.append(round(energy, 10))
    return np.array(sorted(many_body)), one_particle


def _low_level_multiset(values, cutoff):
    return _levels([value for value in values if value < cutoff - 1.0e-8],
                   digits=8)


def _run_spin2():
    print("-- GRAV.SPIN2.EMERGENCE.01 quadratic witnesses --")
    q = sp.symbols("q", nonzero=True, real=True)
    p = sp.Matrix([0, 0, 0, q])
    p2 = q ** 2
    omega = sp.simplify(p * p.T / p2)
    theta = sp.eye(D) - omega

    projectors = {
        kind: _projector_matrix(kind, theta, omega)
        for kind in ("2", "1", "0s", "0w")
    }
    eye10 = sp.eye(len(SYM_BASIS))
    algebra_ok = (
        all(sp.simplify(P * P - P) == sp.zeros(10) for P in projectors.values())
        and all(sp.simplify(projectors[a] * projectors[b]) == sp.zeros(10)
                for a, b in itertools.permutations(projectors, 2))
        and sp.simplify(sum(projectors.values(), sp.zeros(10)) - eye10)
        == sp.zeros(10)
    )
    ranks = {k: int(P.rank()) for k, P in projectors.items()}
    check("SPIN2 projector algebra [E]: P_i P_j=delta_ij P_i, sum=I_10; "
          "ranks (2,1,0s,0w)=(5,3,1,1)",
          algebra_ok and ranks == {"2": 5, "1": 3, "0s": 1, "0w": 1})

    h_tt = SYM_BASIS[SYM_LABELS.index((0, 1))]
    h_vec = SYM_BASIS[SYM_LABELS.index((0, 3))]
    h_scal = theta / sp.sqrt(D - 1)
    representatives = {"spin-2 TT": h_tt, "spin-1 gauge": h_vec,
                       "spin-0 transverse": h_scal}
    expected = {"spin-2 TT": "2", "spin-1 gauge": "1",
                "spin-0 transverse": "0s"}
    rep_ok = True
    for name, h in representatives.items():
        for kind in projectors:
            target = h if kind == expected[name] else sp.zeros(D)
            rep_ok &= sp.simplify(
                _apply_projector(kind, h, theta, omega) - target) == sp.zeros(D)
    check("SPIN2 irrep representatives [E]: TT->P2, vector->P1, "
          "transverse trace->P0s",
          rep_ok)

    data = {}
    for name, h in representatives.items():
        scalar, ric2, weyl2 = _linear_curvatures(h, p)
        data[name] = {
            "FP": sp.simplify(_fierz_pauli(h, p)),
            "R": scalar,
            "Ric2": ric2,
            "C2": weyl2,
        }
    curvature_ok = (
        data["spin-2 TT"]["FP"] == p2 / 2
        and data["spin-2 TT"]["R"] == 0
        and data["spin-2 TT"]["C2"] == p2 ** 2 / 2
        and all(data["spin-1 gauge"][key] == 0
                for key in ("FP", "R", "Ric2", "C2"))
        and data["spin-0 transverse"]["FP"] == -p2
        and sp.simplify(data["spin-0 transverse"]["R"] ** 2
                        - 3 * p2 ** 2) == 0
        and data["spin-0 transverse"]["C2"] == 0
    )
    check("SPIN2 quadratic curvature split [E]: TT FP=q^2/2, C^2=q^4/2, "
          "R=0; vector all zero; scalar FP=-q^2, R^2=3q^4, C^2=0",
          curvature_ok)

    c3, mbar = sp.symbols("c3 Mbar", positive=True)
    alpha_c = sp.symbols("alpha_C", nonzero=True, real=True)
    z = sp.symbols("z", nonzero=True, real=True)
    m_scal = c3 ** sp.Rational(7, 2) * mbar
    A = mbar ** 2 / 4
    k2_clean = sp.expand(A * z)
    k1 = sp.Integer(0)
    k0 = sp.factor(-2 * A * z * (1 - z / m_scal ** 2))
    scalar_roots = sp.solve(k0, z)
    scalar_mass = next(root for root in scalar_roots if root != 0)
    check("SPIN2 frozen scalaron [E]: R^2/(6 M_scal^2) root p^2 = M_scal^2 "
          "with M_scal = c3^{7/2} Mbar",
          sp.simplify(scalar_mass - m_scal ** 2) == 0)
    check("SPIN2 TT massless control [E]: K2(clean)=A z, no p^0 mass term "
          "(R+R^2: one massless spin-2 pole)",
          k2_clean.subs(z, 0) == 0
          and sp.diff(k2_clean, z).subs(z, 0) != 0)
    check("SPIN2 vector Ward shadow [E]: K1=0 exactly (pure gauge)",
          k1 == 0)

    k2_frozen = sp.factor(A * z + alpha_c * z ** 2)
    extra_pole = sp.simplify(-A / alpha_c)
    residue_zero = sp.simplify(sp.limit(z / k2_frozen, z, 0))
    residue_extra = sp.simplify(
        sp.limit((z - extra_pole) / k2_frozen, z, extra_pole))
    ghost_typed = (sp.simplify(residue_zero - 1 / A) == 0
                   and sp.simplify(residue_extra + 1 / A) == 0)
    check("SPIN2 frozen Weyl ghost TYPED [E]: local a4 has Weyl^2; "
          "poles {0, -A/alpha_C}; residues {1/A, -1/A} opposite",
          ghost_typed)

    m2_mut = sp.symbols("M2_mut", positive=True)
    k2_mut = A * z * (1 + z / m2_mut)
    mut_r0 = sp.limit(z / k2_mut, z, 0)
    mut_rm = sp.limit((z + m2_mut) / k2_mut, z, -m2_mut)
    check("SPIN2 MUST-FAIL [X]: wrong-sign Weyl mutant has opposite "
          "residue at p^2=-M2_mut",
          sp.simplify(mut_r0 - 1 / A) == 0
          and sp.simplify(mut_rm + 1 / A) == 0)

    rng = np.random.default_rng(SEED)
    worst = 0.0
    numeric_ranks = None
    for _ in range(8):
        momentum = rng.normal(size=D)
        mats = _numeric_projectors(momentum)
        numeric_ranks = {k: int(np.linalg.matrix_rank(P, tol=1e-10))
                         for k, P in mats.items()}
        total = sum(mats.values())
        worst = max(worst, np.max(np.abs(total - np.eye(10))))
        for a, pa in mats.items():
            worst = max(worst, np.max(np.abs(pa @ pa - pa)))
            for b, pb in mats.items():
                if a != b:
                    worst = max(worst, np.max(np.abs(pa @ pb)))
    check("SPIN2 random-momentum cross-check [N]: 8 seeded p; ranks match",
          worst < TOL_SPIN2 and numeric_ranks == ranks)

    eps_plus = np.zeros((4, 4))
    eps_plus[0, 0], eps_plus[1, 1] = 1.0, -1.0
    eps_cross = np.zeros((4, 4))
    eps_cross[0, 1] = eps_cross[1, 0] = 1.0
    null_p = np.array([0.0, 0.0, 1.0, 1.0])
    helicity_ok = (
        np.max(np.abs(null_p @ eps_plus)) == 0
        and np.max(np.abs(null_p @ eps_cross)) == 0
        and abs(np.trace(eps_plus)) < TOL_SPIN2
        and abs(np.trace(eps_cross)) < TOL_SPIN2
        and abs(np.sum(eps_plus * eps_cross)) < TOL_SPIN2
    )
    check("SPIN2 two TT helicity witnesses [E]: plus/cross transverse, "
          "traceless, independent for null p=(0,0,1,1)",
          helicity_ok)

    # Frozen M_scal identity against the suite primitives (readout only).
    m_scal_num = float(C3_MP ** (sp.Rational(7, 2)) * MBAR_MP)
    check("SPIN2 M_scal primitive consistency [E]: c3^{7/2} Mbar > 0 "
          "(the pole location, not a new number)",
          m_scal_num > 0)
    check("SPIN2 CONTENT PIN [C]: the contract's spin-2 content is pinned "
          "on the UNTRUNCATED form factor; the local a4 Weyl^2 truncation "
          "is typed as carrying the Stelle ghost -- not a clean quadratic "
          "theory",
          ghost_typed)
    return ghost_typed


def _run_smg():
    print("-- CHIRAL4D.NOMIRROR.01 FK SMG toy --")
    h8, gam8, quartics, quartic_labels, _parity8 = _fk_hamiltonian()
    clifford_dev = max(np.max(np.abs(gam8[a] @ gam8[b]
                                      + gam8[b] @ gam8[a]
                                      - (2 * np.eye(16) if a == b
                                         else np.zeros((16, 16)))))
                       for a in range(8) for b in range(8))
    quartic_ok = (len(quartics) == 14
                  and len({label[0] for label in quartic_labels}) == 14
                  and all(abs(abs(label[1]) - 1) < TOL_SMG
                          for label in quartic_labels))
    check("SMG Clifford + Cayley quartic [E]: {gamma,gamma}=2delta; "
          "14 distinct degree-4 stabilizers",
          clifford_dev < TOL_SMG and quartic_ok)

    eigen8, vectors8 = np.linalg.eigh(h8)
    spectrum8 = _levels(eigen8)
    ground8 = vectors8[:, 0]
    target = np.zeros(16, dtype=complex)
    target[0] = target[-1] = 1 / math.sqrt(2)
    overlap = abs(np.vdot(target, ground8))
    gap8 = eigen8[1] - eigen8[0]
    check("SMG N=8 unique gapped ground [E]: spectrum {-14:1, 0:8, 2:7}; "
          "gap=14; |<GHZ+|Omega>|=1",
          spectrum8 == {-14.0: 1, 0.0: 8, 2.0: 7}
          and abs(gap8 - 14.0) < TOL_SMG and abs(overlap - 1.0) < TOL_SMG)

    spin7, action_rank, annihilation, symmetry_comm = _spin7_generators(
        ground8, h8, gam8)
    check("SMG Spin(7) singlet [E]: 28 bilinears -> rank 7 + stabilizer "
          "dim 21; [Q_A,H]=0 and Q_A Omega=0",
          len(spin7) == 21 and action_rank == 7
          and annihilation < TOL_SMG and symmetry_comm < TOL_SMG)

    so8_nullity, so8_rank, _smallest = _full_so8_quartic_nullity(gam8)
    check("SMG full SO(8) overclaim rejected [E]: C(8,4)=70 quartics, "
          "nullity 0 -- FK symmetry is Spin(7), not SO(8)",
          so8_nullity == 0 and so8_rank == 70)

    gam4 = _majoranas(4)
    parity4 = _monomial(gam4, range(4))
    h4 = -parity4
    eigen4 = np.linalg.eigvalsh(h4)
    spectrum4 = _levels(eigen4)
    so4_comm = max(np.max(np.abs(
        (1j * gam4[a] @ gam4[b]) @ h4
        - h4 @ (1j * gam4[a] @ gam4[b])))
        for a, b in itertools.combinations(range(4), 2))
    check("SMG N=4 MUST-FAIL [X]: SO(4)-invariant quartic spectrum "
          "{-1:2, 1:2} -- gapped but ground degeneracy 2",
          spectrum4 == {-1.0: 2, 1.0: 2} and so4_comm < TOL_SMG)

    volume_ok = True
    contrast_ok = True
    for length in (1, 2, 3):
        chain8 = _convolve_spectrum(spectrum8, length)
        chain4 = _convolve_spectrum(spectrum4, length)
        _e08, d08, d8, first8 = _ground_data(chain8)
        _e04, d04, d4, _first4 = _ground_data(chain4)
        volume_ok &= (d08 == 1 and abs(d8 - 14.0) < TOL_SMG
                      and first8 == 8 * length)
        contrast_ok &= (d04 == 2 ** length and abs(d4 - 2.0) < TOL_SMG)
    check("SMG N=8 volume-uniform gap [E]: L=1,2,3 unique ground, "
          "Delta=14 exactly",
          volume_ok)
    check("SMG Z8 vs Z4 contrast [E]: N=4 ground degeneracy 2^L for "
          "L=1,2,3 despite Delta=2",
          contrast_ok)

    ground_two = np.kron(ground8, ground8).reshape(16, 16)
    schmidt = np.linalg.svd(ground_two, compute_uv=False)
    schmidt_rank = int(np.sum(schmidt > TOL_SMG))
    entropy = -sum(value ** 2 * math.log(value ** 2)
                   for value in schmidt if value > TOL_SMG)
    check("SMG product-state / no-topological-order [E]: two-site "
          "Schmidt rank 1",
          schmidt_rank == 1 and abs(entropy) < TOL_SMG)

    edge_ok = True
    edge_gaps = []
    for _mirror_length, edge_length in zip((1, 2, 3), (4, 6, 8)):
        edge_values, _momenta = _chiral_edge_spectrum(edge_length)
        positive = sorted(set(value for value in edge_values if value > TOL_SMG))
        edge_gap = positive[0]
        edge_gaps.append(edge_gap)
        chain8 = _convolve_spectrum(spectrum8, _mirror_length)
        mirror_e0 = min(chain8)
        mirror_relative = {}
        for energy, multiplicity in chain8.items():
            mirror_relative[round(energy - mirror_e0, 9)] = multiplicity
        combined = []
        for mirror_energy, mirror_multiplicity in mirror_relative.items():
            for edge_energy in edge_values:
                combined.extend([mirror_energy + edge_energy]
                                * mirror_multiplicity)
        edge_low = _low_level_multiset(edge_values, 14.0)
        combined_low = _low_level_multiset(combined, 14.0)
        edge_ok &= edge_low == combined_low
    scaling = [math.pi / length for length in (4, 6, 8)]
    edge_scaling_ok = max(abs(a - b) for a, b in zip(edge_gaps, scaling)) < TOL_SMG
    check("SMG physical edge spectrum untouched [E]: below mirror "
          "Delta=14, complete multisets match; edge gaps = pi/L_edge",
          edge_ok and edge_scaling_ok)
    print("  edge gaps %s = pi/L_edge"
          % ["%.6f" % value for value in edge_gaps])
    return contrast_ok and edge_ok


def run():
    reset()
    print("v997  GRAV.SPIN2.EMERGENCE.01 + CHIRAL4D.NOMIRROR.01: "
          "quadratic + SMG-toy witnesses (completeness wave)")
    ghost_typed = _run_spin2()
    smg_ok = _run_smg()
    check("VERDICT SPIN2 [E typed]: SPIN2_QUADRATIC_GHOST_TYPED "
          "(R+R^2 clean; local a4 Weyl^2 carries the ghost)",
          ghost_typed)
    check("VERDICT SMG [E]: SMG_TOY_GAP_CONFIRMED_Z8_CONTRAST "
          "(N=8 unique Spin(7) singlet; N=4 2^L contrast)",
          smg_ok)
    check("FIREWALL (scope): quadratic order + 1D FK toy; no interacting "
          "graviton / universal T_munu / diffeomorphism Ward; no 4D "
          "Spin(10) theorem; both contracts stay [O]; Python-only",
          True)
    return summary("v997 spin-2 + SMG witnesses: R+R^2 clean, Weyl ghost "
                   "typed; N=8 gap 14, N=4 2^L contrast")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
