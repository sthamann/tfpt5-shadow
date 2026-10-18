#!/usr/bin/env python3
"""v722 -- GNET.RAMIFIED.01: PHYS moonshot slice (T2 / G_net) -- is the
Ramond projection (1+i)-adic?

QUESTION (moonshot strategy round 2026-08-03): the open half of G_net is the
identification of the constructed index-4 Q-system (GATE.METRIC.08, C[Z4])
with the actual seam-Calderon inclusion INCLUDING the Ramond sectors
(GATE.METRIC.10: the odd glue classes live ONLY in the R module; "the glue
choice IS the R-projection").  Today's commensurability-groupoid gluing
(moonshot_hecke_groupoid_probe + moonshot_arch_glue_probe) puts a Z[i]-E8
Hecke tower on the table whose ONE ramified edge is the Gaussian prime
(1+i).  v689 proved E8(Z[i])/(1+i) = F2^4 (the mark bits).  FIRST SLICE
TESTED HERE: does the ramified quotient F2^4 SEE the NS/R grading -- i.e.
is the untwisted/twisted (NS/R) sector label of GATE.METRIC.10 a CHARACTER
of L/(1+i)L?  If yes, the Ramond identification (the openest part of R2)
acquires an arithmetic home at the ramified place of the groupoid, and the
"groupoid = network" strategy has its first exact witness.

CONSTRUCTION (standalone, exact integer arithmetic, no imports from
verification/):
  * E8 in the even-coordinate model, doubled coordinates w = 2x:
    w in Z^8, all entries even (integer/NS type, = D8 part) or all odd
    (spinor/R type), sum(w) == 0 mod 4.  Roots |w|^2 = 8:
    112 integer-type (+-2e_i +- 2e_j) + 128 spinor-type ({+-1}^8, even
    number of minus signs).  NS/R label := coordinate parity type
    (this is the SO(16) = 16-Majorana NS/R split; E8 = 120 NS-adjoint
    + 128 R, GATE.METRIC.10 census).
  * mu4 clock J = block rotation on pairs (12)(34)(56)(78) -- an explicit
    integral complex structure (J^2 = -I, orthogonal, lattice-stable),
    making E8 a rank-4 Z[i]-lattice (a concrete witness of the v634/v689
    Gaussian E8; the probe checks stability, it does not import it).
  * (1+i)-equivalence closed form: x ~ y  <=>  (I-J)(x-y)/2 in L
    (because (1+i)^{-1} = (1-i)/2 and J represents i).

CHECKS:
  G0  J integral, J^2=-I, J^T J=I, J L = L (basis images + root-set
      permutation).
  S1  no root lies in (1+i)L (0-class empty; norm proof |(1+i)v|^2=2|v|^2).
  S2  the 240 roots fall into exactly 15 classes x 16 (v689 census,
      re-derived in this frame).
  S3  THE THEOREM CHECK: (1+i)L is contained in the even (NS) sublattice
      -- verified on a Z-basis.  ((1+i) doubles: (I+J)w has entries
      w_{2k-1}-+w_{2k}, even for both parity types.)  Hence the parity
      functional factors through the quotient.
  S4  PURITY: every root class is purely NS or purely R; census 7 NS
      classes (112 = 7x16) + 8 R classes (128 = 8x16).
  S5  mu4-stability: J r ~ r for all 240 roots ((i-1) = i(1+i)).
  S6  quotient group structure: class(x)+class(y) is a class (closure,
      16x16 addition table), 2L in (1+i)L (elementary abelian), and
      parity is a HOMOMORPHISM L/(1+i)L -> F2 (the R-character).
  C1  control (trivialization): Z[i]^4 = Z^8 with the same J -- the
      minimal-vector census must NOT show the 15x16 pattern (v689 I4c).
  C2  control (teeth): pseudo-randomly scrambled NS/R labels must BREAK
      purity (fixed seed).

KILL CRITERIA (preregistered): if S3 or S4 fails, the (1+i) reading of the
Ramond projection is dead at slice 1 and the groupoid route to G_net loses
its cheapest entry point (Pimsner-Popa via the v679/v715 CAR ladder stays
the recommended route unchanged).  If C1 or C2 does not fire, the test has
no teeth and proves nothing.

CIRCULARITY: the NS/R label (coordinate parity) and the class map
((1+i)-equivalence) are computed from independent definitions on one
explicit lattice; no fit, no external tables, no prime table, no zeta.

PROVENANCE: discovery probe phys_ramified_ns_r_probe.py (2026-08-03,
9/9 PASS, verdict RAMIFIED-SEES-NSR: the GATE.METRIC.10 NS/R grading
IS the parity character of E8(Z[i])/(1+i) = F2^4 -- (1+i)L lies in
the even/NS sublattice (Z-basis proof), the 240 roots fall into
15 x 16 classes with PURE parity (7 NS + 8 R), and parity is a
homomorphism F2^4 -> F2; controls fire: the Z[i]^4 census is NOT
15 x 16, scrambled labels break purity).  Promoted verbatim; numbers
unchanged.
"""

import itertools
import sys

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    return ok


# ---------------------------------------------------------------- lattice
# doubled coordinates: true vector x = w/2, w integer 8-tuple.

def in_E8_doubled(w):
    par = {wi % 2 for wi in w}
    if len(par) != 1:
        return False
    return sum(w) % 4 == 0


def roots_E8():
    roots = []
    # integer type: +-2e_i +- 2e_j (doubled: +-4? no: doubled of +-e_i+-e_j)
    # true root +-e_i +- e_j  ->  doubled w = +-2e_i +- 2e_j, |w|^2 = 8. OK
    for i, j in itertools.combinations(range(8), 2):
        for si in (2, -2):
            for sj in (2, -2):
                w = [0] * 8
                w[i], w[j] = si, sj
                roots.append(tuple(w))
    # spinor type: {+-1}^8 with even number of -1
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(signs)
    return roots


def J_apply(w):
    out = []
    for k in range(4):
        a, b = w[2 * k], w[2 * k + 1]
        out.extend([-b, a])
    return tuple(out)


def basis_E8_doubled():
    # doubled Z-basis: D8 simple roots doubled + spinor vector
    B = []
    for i in range(6):
        w = [0] * 8
        w[i], w[i + 1] = 2, -2
        B.append(tuple(w))
    w = [0] * 8
    w[6], w[7] = 2, 2
    B.append(tuple(w))
    B.append(tuple([1] * 8))
    return B


def sub(w, v):
    return tuple(a - b for a, b in zip(w, v))


def add(w, v):
    return tuple(a + b for a, b in zip(w, v))


def one_plus_i_equiv(w, v, member=in_E8_doubled):
    """x ~ y mod (1+i)L  <=>  (I-J)(x-y)/2 in L   (doubled coords)."""
    d = sub(w, v)
    u = sub(d, J_apply(d))  # (I-J) d
    if any(c % 2 for c in u):
        return False
    return member(tuple(c // 2 for c in u))


def classify(vectors, member=in_E8_doubled):
    reps, classes = [], []
    for v in vectors:
        for k, r in enumerate(reps):
            if one_plus_i_equiv(v, r, member):
                classes[k].append(v)
                break
        else:
            reps.append(v)
            classes.append([v])
    return reps, classes


def parity_type(w):
    return w[0] % 2  # 0 = integer/NS, 1 = spinor/R (uniform by membership)


def main():
    roots = roots_E8()
    print("phys_ramified_ns_r_probe -- is the Ramond projection (1+i)-adic?")
    print(f"root census: {len(roots)} total, "
          f"{sum(1 for r in roots if parity_type(r) == 0)} NS(integer) + "
          f"{sum(1 for r in roots if parity_type(r) == 1)} R(spinor)")

    # ---- G0
    B = basis_E8_doubled()
    ok = all(in_E8_doubled(J_apply(b)) for b in B)
    JJ = [J_apply(J_apply(b)) for b in B]
    ok &= all(tuple(-c for c in b) == jb for b, jb in zip(B, JJ))
    rootset = set(roots)
    ok &= all(J_apply(r) in rootset for r in roots)
    check("G0 J integral complex structure, J^2=-I, J-stable lattice+roots", ok)

    # ---- S1: 0-class empty
    zero = tuple([0] * 8)
    ok = not any(one_plus_i_equiv(r, zero) for r in roots)
    check("S1 no root in (1+i)L (norm: |(1+i)v|^2 = 2|v|^2 = 4 > 2)", ok)

    # ---- S2: 15 x 16
    reps, classes = classify(roots)
    sizes = sorted(len(c) for c in classes)
    ok = len(classes) == 15 and sizes == [16] * 15
    check("S2 exactly 15 classes x 16 roots", ok,
          f"n_classes={len(classes)}, sizes={sorted(set(sizes))}")

    # ---- S3: (1+i)L inside the even (NS) sublattice  [theorem check]
    ok = True
    for b in B:
        img = add(b, J_apply(b))  # (1+i) b  (doubled)
        ok &= in_E8_doubled(img) and all(c % 2 == 0 for c in img)
    check("S3 (1+i)L is contained in the even/NS sublattice (Z-basis)", ok)

    # ---- S4: purity + census 7 + 8
    pure = all(len({parity_type(v) for v in c}) == 1 for c in classes)
    n_ns = sum(1 for c in classes if parity_type(c[0]) == 0)
    n_r = sum(1 for c in classes if parity_type(c[0]) == 1)
    ok = pure and n_ns == 7 and n_r == 8
    check("S4 NS/R purity per class; census 7 NS + 8 R", ok,
          f"pure={pure}, NS classes={n_ns}, R classes={n_r}")

    # ---- S5: mu4 stability
    ok = all(one_plus_i_equiv(J_apply(r), r) for r in roots)
    check("S5 every class mu4-stable (J r ~ r; (i-1) = i(1+i))", ok)

    # ---- S6: quotient group + parity homomorphism
    all_reps = [zero] + reps

    def class_index(w):
        for k, r in enumerate(all_reps):
            if one_plus_i_equiv(w, r):
                return k
        return None

    ok_closure, ok_two, ok_hom = True, True, True
    par = [parity_type(r) % 2 for r in all_reps]
    for a in range(16):
        wa = all_reps[a]
        if not one_plus_i_equiv(add(wa, wa), zero):
            ok_two = False
        for b in range(16):
            s = add(wa, all_reps[b])
            k = class_index(s)
            if k is None:
                ok_closure = False
            elif (par[a] + par[b]) % 2 != par[k]:
                ok_hom = False
    check("S6 quotient is elementary abelian (closure, 2L in (1+i)L) and "
          "parity is a homomorphism F2^4 -> F2", ok_closure and ok_two and ok_hom,
          f"closure={ok_closure}, 2-torsion={ok_two}, hom={ok_hom}")

    # ---- C1 control: Z[i]^4 = Z^8 trivializes
    def in_Z8_doubled(w):
        return all(c % 2 == 0 for c in w)

    minvecs = []
    for i in range(8):
        for s in (2, -2):
            w = [0] * 8
            w[i] = s
            minvecs.append(tuple(w))  # doubled +-e_i, true norm 1
    reps_c, classes_c = classify(minvecs, member=in_Z8_doubled)
    sizes_c = sorted(len(c) for c in classes_c)
    fired = not (len(classes_c) == 15 and sizes_c == [16] * 15)
    check("C1 control fires: Z[i]^4 minimal-vector census is NOT 15x16", fired,
          f"classes={len(classes_c)}, sizes={sorted(set(sizes_c))}")

    # ---- C2 control: scrambled labels break purity
    state = 123456789
    def rnd():
        nonlocal state
        state = (1103515245 * state + 12345) % (2 ** 31)
        return state

    scram = {r: rnd() % 2 for r in roots}
    pure_scram = all(len({scram[v] for v in c}) == 1 for c in classes)
    check("C2 control fires: scrambled NS/R labels break purity", not pure_scram)

    n_pass = sum(1 for _, ok in CHECKS if ok)
    verdict = ("RAMIFIED-SEES-NSR" if n_pass == len(CHECKS)
               else "RAMIFIED-BLIND-OR-CONSTRUCTION-FAIL")
    print(f"\n{n_pass}/{len(CHECKS)} checks pass -- VERDICT: {verdict}")
    print("typed consequence if GO: the GATE.METRIC.10 NS/R grading is the "
          "parity character of E8(Z[i])/(1+i) = F2^4 -- the Ramond projection "
          "is (1+i)-adic; first exact witness for the groupoid reading of "
          "G_net.  No marker moves; exploration only.")
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())


def run():
    """run_all entry point."""
    return main()
