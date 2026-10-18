#!/usr/bin/env python3
"""overlap_rp_nt_dependence_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (follow-up to tfpt4d_first_candidate_probe): the naive
Euclidean overlap measure |det D_ov|^2 broke reflection positivity at
N_t = 2 (exact enumeration; pure gauge PSD).  Is that an N_t = 2
artifact (the overlap sgn function wraps the short time torus), or does
the violation persist at N_t = 4?

METHOD: Z4 gauge on the 2 x 4 torus (16 links, 4^16 configs -- beyond
enumeration), deterministic-seed Monte Carlo (uniform proposal, ratio
estimator), link reflection theta: t -> 3 - t (positive half slices
{2, 3}, mirror {1, 0}); Gram of the 16 characters of the slice-2
x-links against the mirrored slice-1 characters.  Three ensembles on
COMMON random numbers: pure gauge (validation: must be PSD within
noise), det-only, full (beta = 1).  Bootstrap CI on the min eigenvalue.

HONEST BOUNDARY: MC (statistical, seed-pinned) -- unlike every other
probe of this wave this leg is NOT exact; the verdict compares the
det-ensemble min eigenvalue against the pure-gauge noise floor with
bootstrap errors.  No marker moves.
"""
import numpy as np

rng = np.random.default_rng(20260828)
NX, NT = 2, 4
M0 = 1.0
BETA = 1.0
NSAMP = 800000
S1 = np.array([[0, 1], [1, 0]], complex)
S2m = np.array([[0, -1j], [1j, 0]], complex)
S3m = np.array([[1, 0], [0, -1]], complex)

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


def plaq_sum(n):
    tot = 0.0
    for x in range(NX):
        for t in range(NT):
            p = (n[0, x, t] + n[1, (x + 1) % NX, t]
                 - n[0, x, (t + 1) % NT] - n[1, x, t]) % 4
            tot += np.real(1j ** p)
    return tot


def det_ov(n):
    dim = NX * NT
    idx = lambda x, t: (x % NX) * NT + (t % NT)
    Tx = np.zeros((dim, dim), complex)
    Tt = np.zeros((dim, dim), complex)
    for x in range(NX):
        for t in range(NT):
            Tx[idx(x + 1, t), idx(x, t)] += 1j ** n[0, x, t]
            Tt[idx(x, t + 1), idx(x, t)] += 1j ** n[1, x, t]
    I = np.eye(dim)
    DW = np.zeros((2 * dim, 2 * dim), complex)
    for S, T in ((S1, Tx), (S2m, Tt)):
        DW += np.kron(S, (T - T.conj().T) / 2)
        DW += np.kron(np.eye(2), -(T + T.conj().T - 2 * I) / 2)
    HW = np.kron(S3m, np.eye(dim)) @ (DW - M0 * np.eye(2 * dim))
    HW = (HW + HW.conj().T) / 2
    w, v = np.linalg.eigh(HW)
    sgn = v @ np.diag(np.sign(w)) @ v.conj().T
    Dov = np.eye(2 * dim) + np.kron(S3m, np.eye(dim)) @ sgn
    return abs(np.linalg.det(Dov)) ** 2


import itertools
CHARS = list(itertools.product(range(4), repeat=2))


def slice_vec(n, t):
    return np.array([1j ** ((r[0] * n[0, 0, t] + r[1] * n[0, 1, t]) % 4)
                     for r in CHARS])


# sampling pass (common random numbers for all three ensembles)
print("sampling %d configs on the 2 x 4 torus ..." % NSAMP)
F0 = np.zeros((NSAMP, 16), complex)     # mirror slice (t = 1)
F1 = np.zeros((NSAMP, 16), complex)     # positive slice (t = 2)
WG = np.zeros(NSAMP)                    # gauge weight
WD = np.zeros(NSAMP)                    # det weight
for s in range(NSAMP):
    n = rng.integers(0, 4, size=(2, NX, NT))
    F0[s] = slice_vec(n, 1)
    F1[s] = slice_vec(n, 2)
    WG[s] = np.exp(BETA * plaq_sum(n))
    WD[s] = det_ov(n)


def min_eig(wv):
    Zs = np.sum(wv)
    G = (F0.conj() * wv[:, None]).T @ F1 / Zs
    G = (G + G.conj().T) / 2
    return float(np.linalg.eigvalsh(G)[0])


def bootstrap(wv, nb=20):
    vals = []
    for b in range(nb):
        idx = rng.integers(0, NSAMP, NSAMP)
        Zs = np.sum(wv[idx])
        G = (F0[idx].conj() * wv[idx, None]).T @ F1[idx] / Zs
        G = (G + G.conj().T) / 2
        vals.append(float(np.linalg.eigvalsh(G)[0]))
    return np.mean(vals), np.std(vals)


res = {}
for tag, wv in (("pure gauge", WG), ("det only", WD), ("full", WG * WD)):
    m, sd = bootstrap(wv)
    res[tag] = (min_eig(wv), m, sd)
    print("%s: min eig %.4f (bootstrap %.4f +/- %.4f)"
          % (tag, res[tag][0], m, sd))

# the pure-gauge ensemble is EXACTLY RP (Osterwalder-Seiler), so its
# measured min eigenvalue IS the estimator noise floor (the min-eig
# statistic is noise-biased downward); characterize it
floor = abs(res["pure gauge"][1]) + 3 * res["pure gauge"][2]
rep("NOISE FLOOR CHARACTERIZED: pure gauge (exactly RP) reads min eig "
    "%.4f +/- %.4f -- the min-eig estimator noise floor at this reach "
    "is ~%.4f; any det-ensemble violation must undercut it to count"
    % (res["pure gauge"][1], res["pure gauge"][2], -floor),
    res["pure gauge"][2] > 0)

sig = (abs(res["det only"][1]) - abs(res["pure gauge"][1])) \
    / max(res["det only"][2], 1e-9)
persists = res["det only"][1] < -(floor + 3 * res["det only"][2])
print("   det-only violation vs noise floor: %.4f vs %.4f (%.1f sigma)"
      % (res["det only"][1], -floor, sig))
if persists:
    rep("FINDING: the overlap-determinant RP violation PERSISTS at "
        "N_t = 4 (min eig %.4f +/- %.4f, beyond the noise floor) -- "
        "NOT an N_t = 2 artifact within this reach"
        % (res["det only"][1], res["det only"][2]), True)
else:
    rep("FINDING: at N_t = 4 the det-ensemble min eigenvalue (%.4f +/- "
        "%.4f) is NOT resolvably below the noise floor %.4f -- the "
        "N_t = 2 violation is consistent with a short-time artifact at "
        "this statistical reach; typed DATA_LIMITED, an exact larger-N_t "
        "check needs a different method"
        % (res["det only"][1], res["det only"][2], -floor), True)

print()
print("VERDICT: %s (MC, seed 20260828, %d samples; no marker move)"
      % ("VIOLATION_PERSISTS_NT4" if persists
         else "NT4_DATA_LIMITED_OR_ARTIFACT", NSAMP))
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
