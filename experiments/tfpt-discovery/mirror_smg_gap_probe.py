#!/usr/bin/env python3
r"""mirror_smg_gap_probe -- EXPLORATION ONLY.

The smallest executable shadow of the mirror-gap half of
CHIRAL4D.NOMIRROR.01: the Fidkowski--Kitaev Z8 fixed point, with eight
Majoranas per site, compared with four Majoranas.

Important symmetry correction: no nonzero quartic made from the SO(8)
vector Majoranas is invariant under all of SO(8).  The canonical FK
interaction is invariant under Spin(7), the stabilizer of one chiral
spinor.  This script verifies both statements rather than calling the
interaction "SO(8)-invariant".

The on-site FK Hamiltonian is generated without hard-coded coefficients.
Start from four commuting stabilizers of
    |Omega> = (|0000> + |1111>)/sqrt(2).
The stabilizer group has identity, fermion parity (degree eight), and
exactly fourteen degree-four elements.  Minus the sum of those fourteen
quartics is the Spin(7)-invariant Cayley/FK Hamiltonian.  Its spectrum is
{-14 x 1, 0 x 8, 2 x 7}; hence a chain of L decoupled sites has a unique
product ground state and volume-independent gap 14.  The N=4 analogue
-gamma_1 gamma_2 gamma_3 gamma_4 is fully SO(4)-invariant but retains
2^L ground states: the required must-fail contrast.

An independent free chiral branch is then attached by a Kronecker sum.
Below the mirror gap its complete many-body spectrum, including
multiplicities, is exactly unchanged; its finite-size gap scales as
pi/L_edge.  This is a mechanism seed, not the requested 4D theorem:
there is no Spin(10), gauge field, uniform interacting-continuum proof,
or 4D chiral lattice measure here.

VERDICT ENUM:
  SMG_TOY_GAP_CONFIRMED_Z8_CONTRAST
  SMG_TOY_CONTRAST_FAILS
  SMG_TOY_ALGEBRA_FAIL

Expected: SMG_TOY_GAP_CONFIRMED_Z8_CONTRAST.  The contract stays [O].
"""

import itertools
import math
import sys

import numpy as np


TOL = 2.0e-10
CHECKS = []


def check(name, condition, detail):
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-35s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def kron_all(ops):
    out = np.array([[1.0]], dtype=complex)
    for op in ops:
        out = np.kron(out, op)
    return out


def majoranas(n_majorana):
    n_qubits = n_majorana // 2
    out = []
    for site in range(n_qubits):
        out.append(kron_all([Z] * site + [X] + [I2] *
                            (n_qubits - site - 1)))
        out.append(kron_all([Z] * site + [Y] + [I2] *
                            (n_qubits - site - 1)))
    return out


def monomial(gammas, indices):
    out = np.eye(gammas[0].shape[0], dtype=complex)
    for index in indices:
        out = out @ gammas[index]
    return out


def levels(eigenvalues, digits=9):
    grouped = {}
    for value in eigenvalues:
        key = round(float(np.real(value)), digits)
        grouped[key] = grouped.get(key, 0) + 1
    return dict(sorted(grouped.items()))


def clifford_label(matrix, gammas, degree):
    dim = matrix.shape[0]
    hits = []
    for indices in itertools.combinations(range(len(gammas)), degree):
        candidate = monomial(gammas, indices)
        coefficient = np.trace(candidate.conj().T @ matrix) / dim
        if abs(coefficient) > TOL:
            hits.append((indices, complex(coefficient)))
    return hits


def fk_hamiltonian():
    gammas = majoranas(8)
    stabilizer_generators = [
        kron_all([Z, Z, I2, I2]),
        kron_all([I2, Z, Z, I2]),
        kron_all([I2, I2, Z, Z]),
        kron_all([X, X, X, X]),
    ]
    parity = kron_all([Z, Z, Z, Z])
    quartics = []
    labels = []
    for bits in itertools.product((0, 1), repeat=4):
        element = np.eye(16, dtype=complex)
        for bit, generator in zip(bits, stabilizer_generators):
            if bit:
                element = element @ generator
        if not any(bits) or np.max(np.abs(element - parity)) < TOL:
            continue
        hits = clifford_label(element, gammas, 4)
        if len(hits) != 1:
            raise RuntimeError("stabilizer element is not one quartic: %r" % (hits,))
        quartics.append(element)
        labels.append(hits[0])
    return -sum(quartics), gammas, quartics, labels, parity


def spin7_generators(ground, hamiltonian, gammas):
    """Find the stabilizer Lie algebra inside the 28 Majorana bilinears."""
    pairs = list(itertools.combinations(range(8), 2))
    bilinears = [1j * gammas[a] @ gammas[b] for a, b in pairs]
    action = np.column_stack([generator @ ground for generator in bilinears])
    action_real = np.vstack([action.real, action.imag])
    _u, singular_values, vh = np.linalg.svd(action_real, full_matrices=True)
    rank = int(np.sum(singular_values > TOL))
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


def full_so8_quartic_nullity(gammas):
    """Dimension of quartics commuting with all 28 so(8) bilinears."""
    quartics = [monomial(gammas, indices)
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
    rank = int(np.sum(singular_values > TOL))
    return len(quartics) - rank, rank, singular_values[-1]


def convolve_spectrum(local_levels, length):
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


def ground_data(spectrum):
    items = list(spectrum.items())
    e0, degeneracy = items[0]
    gap = items[1][0] - e0
    return e0, degeneracy, gap, items[1][1]


def chiral_edge_spectrum(length, velocity=1.0):
    """Free right-moving branch with anti-periodic momenta and filled sea."""
    mode_numbers = np.arange(-length // 2, length // 2)
    one_particle = velocity * 2 * np.pi * (mode_numbers + 0.5) / length
    vacuum_occupancy = one_particle < 0
    vacuum_energy = float(np.sum(one_particle[vacuum_occupancy]))
    many_body = []
    for occupancy in itertools.product((0, 1), repeat=length):
        energy = float(np.dot(one_particle, occupancy) - vacuum_energy)
        many_body.append(round(energy, 10))
    return np.array(sorted(many_body)), one_particle


def low_level_multiset(values, cutoff):
    return levels([value for value in values if value < cutoff - 1.0e-8],
                  digits=8)


def main():
    print("=" * 78)
    print("mirror_smg_gap_probe -- 8-Majorana FK fixed point versus N=4")
    print("EXPLORATION ONLY; CHIRAL4D.NOMIRROR.01 stays [O]")
    print("=" * 78)

    h8, gam8, quartics, quartic_labels, parity8 = fk_hamiltonian()
    clifford_dev = max(np.max(np.abs(gam8[a] @ gam8[b]
                                      + gam8[b] @ gam8[a]
                                      - (2 * np.eye(16) if a == b
                                         else np.zeros((16, 16)))))
                       for a in range(8) for b in range(8))
    quartic_ok = (len(quartics) == 14
                  and len({label[0] for label in quartic_labels}) == 14
                  and all(abs(abs(label[1]) - 1) < TOL
                          for label in quartic_labels))
    check("Clifford + Cayley quartic", clifford_dev < TOL and quartic_ok,
          "{gamma_a,gamma_b}=2delta (dev %.1e); 14 distinct degree-4 "
          "stabilizers, coefficients +/-1" % clifford_dev)

    eigen8, vectors8 = np.linalg.eigh(h8)
    spectrum8 = levels(eigen8)
    ground8 = vectors8[:, 0]
    target = np.zeros(16, dtype=complex)
    target[0] = target[-1] = 1 / math.sqrt(2)
    overlap = abs(np.vdot(target, ground8))
    gap8 = eigen8[1] - eigen8[0]
    check("N=8 unique gapped ground", spectrum8 == {
        -14.0: 1, 0.0: 8, 2.0: 7}
          and abs(gap8 - 14.0) < TOL and abs(overlap - 1.0) < TOL,
          "spectrum %s; gap %.1f; |<GHZ+|Omega>|=%.12f"
          % (spectrum8, gap8, overlap))

    spin7, action_rank, annihilation, symmetry_comm = spin7_generators(
        ground8, h8, gam8)
    check("Spin(7) singlet quantum numbers",
          len(spin7) == 21 and action_rank == 7
          and annihilation < TOL and symmetry_comm < TOL,
          "28 bilinears -> rank 7 + stabilizer dim 21; "
          "max |Q_A Omega| %.1e, max [Q_A,H] %.1e"
          % (annihilation, symmetry_comm))

    so8_nullity, so8_rank, smallest_singular = full_so8_quartic_nullity(gam8)
    check("full SO(8) overclaim rejected",
          so8_nullity == 0 and so8_rank == 70,
          "commutant scan on all C(8,4)=70 quartics: nullity %d, rank %d, "
          "smallest singular %.2e; FK symmetry is Spin(7), not SO(8)"
          % (so8_nullity, so8_rank, smallest_singular))

    gam4 = majoranas(4)
    parity4 = monomial(gam4, range(4))
    h4 = -parity4
    eigen4 = np.linalg.eigvalsh(h4)
    spectrum4 = levels(eigen4)
    so4_comm = max(np.max(np.abs(
        (1j * gam4[a] @ gam4[b]) @ h4
        - h4 @ (1j * gam4[a] @ gam4[b])))
        for a, b in itertools.combinations(range(4), 2))
    check("N=4 must-fail anchor",
          spectrum4 == {-1.0: 2, 1.0: 2} and so4_comm < TOL,
          "SO(4)-invariant quartic spectrum %s: gapped but ground degeneracy 2"
          % spectrum4)

    local8 = spectrum8
    local4 = spectrum4
    table = []
    volume_ok = True
    contrast_ok = True
    for length in (1, 2, 3):
        chain8 = convolve_spectrum(local8, length)
        chain4 = convolve_spectrum(local4, length)
        e08, d08, d8, first8 = ground_data(chain8)
        e04, d04, d4, first4 = ground_data(chain4)
        table.append((length, 16 ** length, e08, d08, d8, first8,
                      4 ** length, e04, d04, d4, first4))
        volume_ok &= (d08 == 1 and abs(d8 - 14.0) < TOL
                      and first8 == 8 * length)
        contrast_ok &= (d04 == 2 ** length and abs(d4 - 2.0) < TOL)
    check("N=8 volume-uniform gap", volume_ok,
          "L=1,2,3: unique ground, Delta=14 exactly; first multiplets 8L")
    check("Z8 versus Z4 contrast", contrast_ok,
          "N=4: ground degeneracy 2^L for L=1,2,3 despite Delta=2")

    # The fixed-point chain is literally a tensor product.  Its two-site ground
    # has one Schmidt value, so it is short-range entangled and has no 1D
    # intrinsic topological order in this toy.
    ground_two = np.kron(ground8, ground8).reshape(16, 16)
    schmidt = np.linalg.svd(ground_two, compute_uv=False)
    schmidt_rank = int(np.sum(schmidt > TOL))
    entropy = -sum(value ** 2 * math.log(value ** 2)
                   for value in schmidt if value > TOL)
    check("product-state / no-topological-order shadow",
          schmidt_rank == 1 and abs(entropy) < TOL,
          "two-site ground Schmidt rank %d, entropy %.2e; exact depth-0 product"
          % (schmidt_rank, entropy))

    edge_rows = []
    edge_ok = True
    edge_gaps = []
    for mirror_length, edge_length in zip((1, 2, 3), (4, 6, 8)):
        edge_values, momenta = chiral_edge_spectrum(edge_length)
        positive = sorted(set(value for value in edge_values if value > TOL))
        edge_gap = positive[0]
        edge_gaps.append(edge_gap)

        mirror_relative = {}
        chain8 = convolve_spectrum(local8, mirror_length)
        mirror_e0 = min(chain8)
        for energy, multiplicity in chain8.items():
            mirror_relative[round(energy - mirror_e0, 9)] = multiplicity

        combined = []
        for mirror_energy, mirror_multiplicity in mirror_relative.items():
            for edge_energy in edge_values:
                combined.extend([mirror_energy + edge_energy]
                                * mirror_multiplicity)
        edge_low = low_level_multiset(edge_values, 14.0)
        combined_low = low_level_multiset(combined, 14.0)
        exact_match = edge_low == combined_low
        edge_ok &= exact_match
        edge_rows.append((mirror_length, edge_length, edge_gap,
                          len(edge_low), exact_match,
                          float(np.min(np.abs(momenta)))))
    scaling = [math.pi / length for length in (4, 6, 8)]
    edge_scaling_ok = max(abs(a - b) for a, b in zip(edge_gaps, scaling)) < TOL
    check("physical edge spectrum untouched",
          edge_ok and edge_scaling_ok,
          "below mirror Delta=14, complete multisets match exactly; "
          "edge gaps %s = pi/L_edge" %
          ["%.6f" % value for value in edge_gaps])

    if not all(CHECKS):
        verdict = "SMG_TOY_ALGEBRA_FAIL"
    elif contrast_ok and edge_ok:
        verdict = "SMG_TOY_GAP_CONFIRMED_Z8_CONTRAST"
    else:
        verdict = "SMG_TOY_CONTRAST_FAILS"

    print("\nGAP TABLE")
    print("  L | N=8 dim  E0   deg  gap first-deg | N=4 dim E0 deg gap first-deg")
    for row in table:
        print("  %d | %7d %4.0f %4d %4.0f %9d | %7d %3.0f %3d %3.0f %9d"
              % row)
    print("\nEDGE TABLE")
    print("  mirror-L edge-L edge-gap levels<14 exact-match min|k|")
    for row in edge_rows:
        print("  %8d %6d %8.6f %9d %-11s %8.6f" % row)
    print("\nVERDICT: %s" % verdict)
    print("BOUNDARY: 1D FK fixed-point toy with Spin(7) (not full SO(8), "
          "not Spin(10)); decoupled on-site chain; finite L<=3; no dynamical "
          "gauge field or gauge-coupling stability theorem; no 4D continuum "
          "limit.  The edge comparison is an exact tensor-factor statement.  "
          "CHIRAL4D.NOMIRROR.01 stays [O].")
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("=" * 78)
    return 0 if all(CHECKS) and verdict == \
        "SMG_TOY_GAP_CONFIRMED_Z8_CONTRAST" else 1


if __name__ == "__main__":
    sys.exit(main())
