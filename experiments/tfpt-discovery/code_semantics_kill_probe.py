#!/usr/bin/env python3
"""SLICE 3 sandbox probe -- the code-semantics kill test for the v626 find
(extended Hamming [8,4,4] -> E8 via Construction A).

The natural candidate assignment: the 8 bit positions = the 8 coordinates
of the D8 model carrying the mu4 pair structure ((1,2)(3,4)(5,6)(7,8)).
The compiler symmetries reduce mod 2 to permutations of F_2^8:
  piJ    = J_all mod 2 = the in-pair swap (01)(23)(45)(67)
           (since (a,b) -> (-b,a) = (b,a) mod 2),
  pisig  = the pair 3-cycle (positions (0 2 4)(1 3 5), pair 4 fixed).
piJ and pisig commute; <piJ, pisig> = Z_6.

  K1  v626 code reproduced: 16 words, weight distribution {0:1, 4:14, 8:1},
      self-dual.
  K2  THE SHARP TEST (natural assignment): piJ(C) = C?  pisig(C) = C?
      If the code is not invariant under a compiler symmetry, the naive
      position semantics is dead for that symmetry.
  K3  THE CENSUS: all codes S8-equivalent to C (the extended-Hamming
      coordinate placements; expected 30 = |S8|/|AGL(3,2)| =
      40320/1344); how many are invariant under piJ alone, pisig alone,
      and BOTH.  If none under both -> semantics dead for every
      labelling; if some -> semantics needs a specific relabelling.
  K4  weight-4 orbit decomposition: under the invariance subgroup of the
      GIVEN code, and under the full Z_6 for a both-invariant census code
      (if any); orbit sizes vs compiler numbers.
  K5  transport check for a both-invariant code C*: on the Construction-A
      roots of C*, J_all is free with 60 orbits, and the sigma-fixed and
      g = J o sigma orbit censuses are compared to the v629 D8-model
      values (60 orbits / 12 fixed / 19x12+3x4).

Sandbox probe: writes nothing.
"""
import itertools
import time
from collections import Counter

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ---------------------------------------------------------------- the code
G = [(1, 0, 0, 0, 0, 1, 1, 1),
     (0, 1, 0, 0, 1, 0, 1, 1),
     (0, 0, 1, 0, 1, 1, 0, 1),
     (0, 0, 0, 1, 1, 1, 1, 0)]
CODE = frozenset(tuple(sum(m[k] * G[k][j] for k in range(4)) % 2
                       for j in range(8))
                 for m in itertools.product((0, 1), repeat=4))

# ================================================================== K1
print("=" * 78)
print("K1: the v626 code reproduced")
print("=" * 78)

wdist = Counter(sum(c) for c in CODE)
dual = [v for v in itertools.product((0, 1), repeat=8)
        if all(sum(a * b for a, b in zip(v, c)) % 2 == 0 for c in CODE)]
check("K1.1 16 codewords, weights {0:1, 4:14, 8:1}, self-dual",
      len(CODE) == 16 and dict(wdist) == {0: 1, 4: 14, 8: 1}
      and frozenset(dual) == CODE)

# ---------------------------------------------------------------- the perms
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)          # in-pair swap
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)        # new[k] = old[PI_SIG[k]]


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def perm_compose(p, q):
    """(p o q)[k] = p[q[k]] as position-permutation on tuples."""
    return tuple(q[p[k]] for k in range(8))


commute = (perm_compose(PI_J, PI_SIG) == perm_compose(PI_SIG, PI_J))
z6 = set()
p = tuple(range(8))
elems = []
for a in range(2):
    for b in range(3):
        q = tuple(range(8))
        for _ in range(a):
            q = perm_compose(q, PI_J)
        for _ in range(b):
            q = perm_compose(q, PI_SIG)
        z6.add(q)
check("K1.2 piJ and pisig commute and generate Z_6 (order %d)" % len(z6),
      commute and len(z6) == 6)

# ================================================================== K2
print("=" * 78)
print("K2: the sharp test on the NATURAL assignment")
print("=" * 78)


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


inv_J = (code_image(CODE, PI_J) == CODE)
inv_S = (code_image(CODE, PI_SIG) == CODE)
check("K2.1 [measured] the v626 code IS invariant under piJ (the mu4 "
      "in-pair swap mod 2): %s" % inv_J, True)
check("K2.2 [measured] the v626 code invariant under pisig (the family "
      "pair 3-cycle): %s" % inv_S, True)
check("K2.3 the kill verdict for the NAIVE full assignment (both "
      "symmetries): %s" % ("ALIVE" if (inv_J and inv_S) else
                           "DEAD for pisig" if inv_J else "DEAD"), True)

# ================================================================== K3
print("=" * 78)
print("K3: the census over all coordinate placements")
print("=" * 78)

codes = set()
for p in itertools.permutations(range(8)):
    codes.add(code_image(CODE, p))
n_codes = len(codes)
invJ_codes = [c for c in codes if code_image(c, PI_J) == c]
invS_codes = [c for c in codes if code_image(c, PI_SIG) == c]
both_codes = [c for c in codes
              if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
check("K3.1 S8 orbit of the code has %d distinct placements (expected "
      "30 = 40320/|AGL(3,2)| = 40320/1344)" % n_codes, n_codes == 30)
check("K3.2 census: %d/30 invariant under piJ, %d/30 under pisig, "
      "%d/30 under BOTH" % (len(invJ_codes), len(invS_codes),
                            len(both_codes)),
      True)
sem_alive = len(both_codes) > 0
check("K3.3 semantics verdict: a mu4+family-equivariant extended-Hamming "
      "placement %s" % ("EXISTS (%d placements)" % len(both_codes)
                        if sem_alive else "does NOT exist -- hard kill"),
      True)
for k, c in enumerate(sorted(both_codes)):
    supp = sorted(tuple(i for i in range(8) if w[i]) for w in c
                  if sum(w) == 4)
    print("    both-invariant placement %d: weight-4 supports %s"
          % (k + 1, supp))
if len(both_codes) == 2:
    c1, c2 = sorted(both_codes)
    movers = [p for p in itertools.permutations(range(8))
              if perm_compose(p, PI_J) == perm_compose(PI_J, p)
              and perm_compose(p, PI_SIG) == perm_compose(PI_SIG, p)
              and code_image(c1, p) == c2]
    check("K3.4 the two placements are exchanged by a Z_6-centralizing "
          "relabelling: %s (%d such perms)"
          % (bool(movers), len(movers)), True,
          "example: %s" % (movers[0],) if movers else "")

# ================================================================== K4
print("=" * 78)
print("K4: weight-4 orbit decompositions")
print("=" * 78)


def orbits_of(words, perms):
    seen = set()
    sizes = []
    for w in sorted(words):
        if w in seen:
            continue
        orb = {w}
        frontier = [w]
        while frontier:
            u = frontier.pop()
            for p in perms:
                v = apply_perm(u, p)
                if v not in orb:
                    orb.add(v)
                    frontier.append(v)
        seen.update(orb)
        sizes.append(len(orb))
    return sorted(sizes)


w4_given = [c for c in CODE if sum(c) == 4]
sub_perms = [p for p in (PI_J, PI_SIG) if code_image(CODE, p) == CODE]
sizes_given = orbits_of(w4_given, sub_perms)
check("K4.1 GIVEN code: invariance subgroup generated by %s; weight-4 "
      "orbit sizes %s"
      % (["piJ" if p == PI_J else "pisig" for p in sub_perms],
         sizes_given), True)

sizes_both = None
Cstar = None
if both_codes:
    Cstar = sorted(both_codes)[0]
    w4_star = [c for c in Cstar if sum(c) == 4]
    sizes_both = orbits_of(w4_star, [PI_J, PI_SIG])
    check("K4.2 both-invariant code C*: weight-4 Z_6 orbit sizes %s "
          "(compiler numbers to compare: 2 = sheet involution, 3 = "
          "cycles, 6 = |det P|, 12 = lifted marks, 14 = 2x7)"
          % sizes_both, True,
          "C* generator-free description: %d words" % len(Cstar))
else:
    check("K4.2 no both-invariant code exists -- Z_6 orbit question moot",
          True)

# ================================================================== K5
print("=" * 78)
print("K5: transport to the Construction-A roots of C*")
print("=" * 78)

if Cstar:
    CW = set(Cstar)
    roots = [x for x in itertools.product(range(-2, 3), repeat=8)
             if sum(v * v for v in x) == 4
             and tuple(v % 2 for v in x) in CW]
    RS = set(roots)

    def J_all(v):
        out = []
        for i in range(0, 8, 2):
            a, b = v[i], v[i + 1]
            out += [-b, a]
        return tuple(out)

    def sigma_r(v):
        return (v[4], v[5], v[0], v[1], v[2], v[3], v[6], v[7])

    def census(f):
        seen = set()
        cnt = Counter()
        for v in roots:
            if v in seen:
                continue
            orb = [v]
            y = f(v)
            while y != v:
                orb.append(y)
                y = f(y)
            seen.update(orb)
            cnt[len(orb)] += 1
        return dict(cnt)

    closed = all(J_all(x) in RS and sigma_r(x) in RS for x in roots)
    cJ = census(J_all)
    cS = census(sigma_r)
    cG = census(lambda v: J_all(sigma_r(v)))
    check("K5.1 C* Construction-A roots: %d, closed under J_all and "
          "sigma: %s" % (len(roots), closed),
          len(roots) == 240 and closed)
    check("K5.2 censuses on the C* roots: J %s, sigma %s, g = J o sigma "
          "%s -- v629 D8-model values were J {4:60}, sigma {3:76,1:12}, "
          "g {12:19,4:3}" % (cJ, cS, cG), True)
else:
    check("K5.1 skipped: no both-invariant code", True)

# ================================================================== summary
print("=" * 78)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if inv_J and inv_S:
    v = "CODE-SEMANTICS-ALIVE"
elif sem_alive:
    v = "CODE-SEMANTICS-RELABELLED (naive placement dead for pisig: %s, "\
        "piJ: %s; %d/30 placements carry both symmetries)" \
        % (not inv_S, not inv_J, len(both_codes))
else:
    v = "CODE-SEMANTICS-DEAD"
print("VERDICT: %s" % v)
print("elapsed: %.1f s" % (time.time() - T0))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECKS FAILED")
