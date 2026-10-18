(* Exact representative round-4 mirrors for v1027--v1030.

   This file deliberately mirrors algebraic identities only.  The deterministic
   floating spectra, 2x2x2 tensor contraction, and finite-size regressions remain
   Python checks; they are not mislabeled as native interval certificates here.

   When Get[] is used from tfpt_readouts.wl, the existing global $pass/$fail
   counters are updated.  When run directly, a small standalone harness owns and
   summarizes those counters.  Every other symbol is localized by Module. *)

Module[{standalone = !(ValueQ[$pass] && ValueQ[$fail])},
  If[standalone, $pass = 0; $fail = 0];

  Module[
    {check, zeroQ, a, delta, lambda, g, mass, beta, eta, c, h,
     weights, colors, higgs, roots, add, buildExterior, buildDenominator,
     p2, denominator, residues, oneSiteResidue, frobeniusQ,
     cs, cf, js, jf, rot, refl, psi, proj, cap, invariantDimension,
     x, y, z, k, basis, bmat, trace, k2, v, scalar, kp, kq,
     r, zeroEnergy, e, projectors, shift, words, diagonalVars,
     diagonal, connectedRank, broken, brokenRank},

    check[name_, condition_] := If[TrueQ[condition],
      $pass++; Print["  [PASS] ", name],
      $fail++; Print["  [FAIL] ", name]
    ];
    zeroQ[m_] := And @@ (PossibleZeroQ /@ Flatten[Simplify[m]]);

    (* v1027: exact signed-wall determinant and unsquared low branch. *)
    {a, delta, lambda, g} = Unique /@ {"a", "delta", "lambda", "g"};
    mass = delta + lambda;
    beta = lambda g^2;
    eta = lambda g;
    c = beta - eta^2/mass;
    h = {{a + beta a^2, eta a}, {eta a, mass}};
    check["v1027 signed determinant M a (1+c a)",
      Together[Det[h] - mass a (1 + c a)] === 0];
    check["v1027 physical kernel remains one-dimensional at a=0",
      NullSpace[h /. a -> 0] === {{1, 0}}];

    (* v1028: exact characteristic-five reduction of the full 192-mode
       one-site character.  P^12 == P^2 P(z^5)^2 mod 5 is evaluated by
       coefficient dictionaries, never by floating group quadrature. *)
    colors = {{1, 0}, {0, 1}, {-1, -1}};
    weights = Join[
      Flatten[Table[{col[[1]], col[[2]], weak, 1}, {col, colors},
                    {weak, {-1, 1}}], 1],
      ({-#[[1]], -#[[2]], 0, -4} & /@ colors),
      ({-#[[1]], -#[[2]], 0, 2} & /@ colors),
      {{0, 0, -1, -3}, {0, 0, 1, -3}, {0, 0, 0, 6}, {0, 0, 0, 0}}
    ];
    higgs = {{0, 0, 0, 0}, {0, 0, -1, 3}, {0, 0, 1, 3}};
    roots = {{1, -1, 0, 0}, {2, 1, 0, 0},
             {1, 2, 0, 0}, {0, 0, 2, 0}};
    add[u_, w_] := u + w;
    buildExterior[list_] := Module[{poly = <|{0, 0, 0, 0} -> 1|>, next, key},
      Do[
        next = Association[Normal[poly]];
        KeyValueMap[
          Function[{exponent, coefficient},
            key = add[exponent, weight];
            AssociateTo[next, key -> Mod[
              If[KeyExistsQ[next, key], next[key], 0] + coefficient, 5]]
          ], poly];
        poly = Select[next, # =!= 0 &],
        {weight, list}
      ];
      poly
    ];
    buildDenominator[] := Module[{poly = <|{0, 0, 0, 0} -> 1|>, next, key},
      Do[
        next = Association[Normal[poly]];
        KeyValueMap[
          Function[{exponent, coefficient},
            key = add[exponent, root];
            AssociateTo[next, key ->
              (If[KeyExistsQ[next, key], next[key], 0] - coefficient)]
          ], poly];
        poly = Select[next, # =!= 0 &],
        {root, roots}
      ];
      poly
    ];
    frobeniusQ = And @@ Table[
      Mod[Binomial[12, degree], 5] ===
        Mod[Sum[If[left + 5 right === degree,
                   Binomial[2, left] Binomial[2, right], 0],
                {left, 0, 2}, {right, 0, 2}], 5],
      {degree, 0, 12}
    ];
    check["v1028 exact factorwise Frobenius identity mod 5", frobeniusQ];
    p2 = buildExterior[Join[weights, weights]];
    denominator = buildDenominator[];
    residues = GroupBy[Keys[p2], Mod[#, 5] &];
    oneSiteResidue = Mod[4 Total[KeyValueMap[
      Function[{root, sign},
        sign Sum[
          With[{offset = root + hh},
            Sum[
              With[{second = Quotient[#, 5] & /@ (-exponent - offset)},
                p2[exponent] If[KeyExistsQ[p2, second], p2[second], 0]
              ],
              {exponent, If[KeyExistsQ[residues, Mod[-offset, 5]],
                            residues[Mod[-offset, 5]], {}]}
            ]
          ],
          {hh, higgs}
        ]
      ], denominator]], 5];
    check["v1028 full 192-mode one-site Gauss dimension is 3 mod 5",
      Length[weights] === 16 && Length[denominator] === 12 && oneSiteResidue === 3];

    (* v1028: exact ordinary D4 cap on the selected 12D even pair space. *)
    cs = DiagonalMatrix[{1, -I, -1, I}];
    cf = DiagonalMatrix[{-I, -1, I}];
    js = SparseArray[Table[{Mod[-kk, 4] + 1, kk + 1} -> 1, {kk, 0, 3}], {4, 4}];
    jf = {{0, 0, 1}, {0, 1, 0}, {1, 0, 0}};
    rot = KroneckerProduct[cs, cf];
    refl = KroneckerProduct[js, jf];
    check["v1028 ordinary D4 relations on selected even pair space",
      zeroQ[MatrixPower[rot, 4] - IdentityMatrix[12]] &&
      zeroQ[refl.refl - IdentityMatrix[12]] &&
      zeroQ[refl.rot.refl - ConjugateTranspose[rot]]];
    (* One-based flattened slots for (k,g)=(1,3),(2,2),(3,1). *)
    psi = SparseArray[{{6} -> 1, {8} -> 1, {10} -> 1}, {12}];
    proj = Outer[Times, psi, psi]/3;
    cap = IdentityMatrix[12] - proj;
    check["v1028 D4-invariant selected-space cap has rank 11 and gap one",
      zeroQ[proj.proj - proj] && zeroQ[rot.proj - proj] &&
      zeroQ[refl.proj - proj] && MatrixRank[cap] === 11];
    invariantDimension = 12 - MatrixRank[Join[rot - IdentityMatrix[12],
                                               refl - IdentityMatrix[12]]];
    check["v1028 invariant-ray space is two-dimensional, not oriented",
      invariantDimension === 2];

    (* v1029: exact generic local tensor identities and the k=0 instability. *)
    {x, y, z} = Unique /@ {"x", "y", "z"};
    k = {x, y, z};
    basis = Join[
      Table[Outer[Times, UnitVector[3, ii], UnitVector[3, ii]], {ii, 1, 3}],
      Table[With[{ii = pair[[1]], jj = pair[[2]]},
        (Outer[Times, UnitVector[3, ii], UnitVector[3, jj]] +
         Outer[Times, UnitVector[3, jj], UnitVector[3, ii]])/Sqrt[2]],
        {pair, {{2, 3}, {1, 3}, {1, 2}}}]
    ];
    bmat = Transpose[(#.k) & /@ basis];
    trace = {1, 1, 1, 0, 0, 0};
    k2 = k.k;
    v = Transpose[bmat].k;
    scalar = v - k2 trace;
    kp = IdentityMatrix[6] - Outer[Times, trace, trace]/2;
    kq = k2 (IdentityMatrix[6] - Outer[Times, trace, trace]) -
          2 Transpose[bmat].bmat + Outer[Times, trace, v] + Outer[Times, v, trace];
    check["v1029 generic local tensor constraint identities",
      zeroQ[bmat.Transpose[bmat] - (k2 IdentityMatrix[3] + Outer[Times, k, k])/2] &&
      zeroQ[kq.Transpose[bmat]] && zeroQ[kp.scalar - Transpose[bmat].k] &&
      PossibleZeroQ[scalar.scalar - 2 k2^2]];
    r = Unique[];
    zeroEnergy = Expand[(r trace).kp.(r trace)/2];
    check["v1029 periodic k=0 trace mode has exact energy -3 r^2/4",
      zeroEnergy === -3 r^2/4];

    (* v1030: actual connected-sector words span M4; a disconnected mutant
       leaves one extra commutant degree. *)
    e[ii_, jj_] := SparseArray[{{ii, jj} -> 1}, {4, 4}];
    projectors = Table[e[ii, ii], {ii, 1, 4}];
    shift = Sum[e[Mod[ii, 4] + 1, ii], {ii, 1, 4}];
    words = Flatten[Table[
      projectors[[ii]].MatrixPower[shift, Mod[ii - jj, 4]].projectors[[jj]],
      {ii, 1, 4}, {jj, 1, 4}], 1];
    check["v1030 connected-sector actual-word frame spans all 16 matrix units",
      MatrixRank[Transpose[Flatten /@ words]] === 16];
    diagonalVars = Table[Unique["c"], {4}];
    diagonal = DiagonalMatrix[diagonalVars];
    connectedRank = MatrixRank[CoefficientArrays[
      Flatten[diagonal.shift - shift.diagonal], diagonalVars][[2]]];
    broken = e[2, 1] + e[4, 3];
    brokenRank = MatrixRank[CoefficientArrays[
      Flatten[diagonal.broken - broken.diagonal], diagonalVars][[2]]];
    check["v1030 connected/disconnected commutant ranks are 3 and 2",
      connectedRank === 3 && brokenRank === 2];
  ];

  If[standalone,
    Print["--- TFPT round-4 Wolfram mirrors: ", $pass, " passed, ", $fail,
          " failed ---"];
    If[$fail == 0, Print["ALL ROUND4 WOLFRAM CHECKS PASSED"], Exit[1]]
  ];
];
