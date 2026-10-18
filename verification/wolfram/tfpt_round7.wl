(* Exact representative Round-7 mirrors for v1031--v1035.

   This file is an independent Wolfram-language cross-check of bounded exact
   algebra only.  It does not mirror the finite QWZ/Fock calculations, promote
   a factorized parent to a local interacting parent, complete the TOE, or make
   an RH claim.

   When Get[] is used from a shared runner, the existing global $pass/$fail
   counters are updated.  When run directly, a standalone harness owns and
   summarizes those counters.  Every other symbol is localized by Module. *)

Module[{standalone = !(ValueQ[$pass] && ValueQ[$fail])},
  If[standalone, $pass = 0; $fail = 0];

  Module[
    {check, zeroQ, symBasis, tensorData, explicitPTT, coords, riemann,
     curvatureMap, covariantNumerator, hPairs, hBasis, sPairs, sBasis,
     wedgePairs, curvaturePairs, eta, p, r2, b, trace, scalar,
     kp, kq, c, ptt, cFactor, k, a, pi, gaugeColumns, embed, kernel,
     nullFactor, z4, x4, qDeck, omegaS, omegaF, lambdaNorm2,
     dispersionAmplitude, symmetricBond, xx, yy, zz, threshold, thresholdPrime,
     xStar, gapStar, derivativeRoots, endpointValues, coupling, rho,
     current, tau, q, canonicalP, dotQ, dotP, dotRho, dotCurrent, psi0,
     psi, dotPsi0, dotPsi, alpha, beta, gamma, coefficientSolution,
     lambda, phiValues, interactionResidual},

    check[name_, condition_] := If[TrueQ[condition],
      $pass++; Print["  [PASS] ", name],
      $fail++; Print["  [FAIL] ", name]
    ];
    zeroQ[value_] := And @@
      (TrueQ[PossibleZeroQ[#]] & /@ Flatten[{Simplify[value]}]);

    symBasis[n_, pairs_] := Table[
      With[{ii = pair[[1]], jj = pair[[2]]},
        If[ii === jj,
          SparseArray[{{ii, ii} -> 1}, {n, n}],
          SparseArray[{{ii, jj} -> 1/Sqrt[2],
                       {jj, ii} -> 1/Sqrt[2]}, {n, n}]
        ]
      ],
      {pair, pairs}
    ];

    sPairs = {{1, 1}, {2, 2}, {3, 3}, {2, 3}, {1, 3}, {1, 2}};
    sBasis = symBasis[3, sPairs];
    tensorData[momentum_] := Module[{localR2, localB, localTrace,
                                     localV, localScalar, localKp,
                                     localKq, localC},
      localR2 = momentum.momentum;
      localB = Transpose[(#.momentum) & /@ sBasis];
      localTrace = {1, 1, 1, 0, 0, 0};
      localV = Transpose[localB].momentum;
      localScalar = localV - localR2 localTrace;
      localKp = IdentityMatrix[6] -
                Outer[Times, localTrace, localTrace]/2;
      localKq = localR2 (IdentityMatrix[6] -
                 Outer[Times, localTrace, localTrace]) -
                2 Transpose[localB].localB +
                Outer[Times, localTrace, localV] +
                Outer[Times, localV, localTrace];
      localC = Expand[localKq.localKp.localKq];
      {localR2, localB, localTrace, localScalar, localKp, localKq,
       localC}
    ];
    explicitPTT[momentum_, localR2_] := Module[
      {projector, images},
      projector = IdentityMatrix[3] -
                  Outer[Times, momentum, momentum]/localR2;
      images = Table[
        With[{image = projector.h.projector -
                      projector Tr[projector.h]/2},
          Tr[Transpose[test].image] & /@ sBasis
        ],
        {h, sBasis}
      ];
      Transpose[images]
    ];

    (* v1031: exact rational-fibre curvature projector and positivity. *)
    p = {1, 2, 2};
    {r2, b, trace, scalar, kp, kq, c} = tensorData[p];
    ptt = Simplify[explicitPTT[p, r2]];
    check["v1031 C=r^4 PTT with a symmetric rank-two projector",
      zeroQ[c - r2^2 ptt] && zeroQ[ptt - Transpose[ptt]] &&
      zeroQ[ptt.ptt - ptt] && MatrixRank[ptt] === 2];
    cFactor = r2 ptt;
    check["v1031 exact PSD factorization has spectrum {0^4,r^4,r^4}",
      zeroQ[c - cFactor.Transpose[cFactor]] && MatrixRank[c] === 2 &&
      Sort[Simplify[Eigenvalues[c]]] === {0, 0, 0, 0, r2^2, r2^2}];

    (* v1032: a separate Lorentz-covariant curvature calculation at one
       exact nonzero null momentum.  Pi is the de Donder trace-reversed
       numerator; positivity is inferred only after the curvature sandwich. *)
    hPairs = Flatten[Table[{ii, jj}, {ii, 1, 4}, {jj, ii, 4}], 1];
    hBasis = symBasis[4, hPairs];
    wedgePairs = {{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}};
    curvaturePairs = Flatten[
      Table[{aa, bb}, {aa, 1, 6}, {bb, aa, 6}], 1];
    eta = DiagonalMatrix[{-1, 1, 1, 1}];
    coords[h_] := Tr[Transpose[#].h] & /@ hBasis;
    riemann[momentum_, h_, mu_, nu_, rr_, ss_] :=
      (momentum[[ss]] momentum[[nu]] h[[mu, rr]] +
       momentum[[rr]] momentum[[mu]] h[[nu, ss]] -
       momentum[[rr]] momentum[[nu]] h[[mu, ss]] -
       momentum[[ss]] momentum[[mu]] h[[nu, rr]])/2;
    curvatureMap[momentum_] := Table[
      With[{mn = wedgePairs[[curvaturePairs[[row, 1]]]],
            rs = wedgePairs[[curvaturePairs[[row, 2]]]]},
        riemann[momentum, hBasis[[column]], mn[[1]], mn[[2]],
                rs[[1]], rs[[2]]]
      ],
      {row, Length[curvaturePairs]}, {column, Length[hBasis]}
    ];
    covariantNumerator[] := Transpose[
      (coords[eta.#.eta - eta Tr[eta.#]/2] &) /@ hBasis];

    k = {-1, 0, 0, 1};
    a = curvatureMap[k];
    pi = covariantNumerator[];
    check["v1032 de Donder numerator is symmetric with inertia (6+,4-)",
      zeroQ[pi - Transpose[pi]] && Det[pi] =!= 0 &&
      Sort[Eigenvalues[pi]] === {-1, -1, -1, -1, 1, 1, 1, 1, 1, 1}];
    gaugeColumns = Table[
      With[{xi = UnitVector[4, jj]},
        a.coords[Outer[Times, k, xi] + Outer[Times, xi, k]]
      ],
      {jj, 1, 4}
    ];
    check["v1032 curvature annihilates all four exact pure-gauge columns",
      And @@ (zeroQ /@ gaugeColumns)];
    p = {0, 0, 1};
    {r2, b, trace, scalar, kp, kq, c} = tensorData[p];
    ptt = Simplify[c/r2^2];
    embed = Transpose[(coords[ArrayPad[#, {{1, 0}, {1, 0}}]] &) /@ sBasis];
    kernel = Simplify[a.pi.Transpose[a]];
    nullFactor = Simplify[a.embed.ptt];
    check["v1032 null de Donder sandwich is PSD of physical rank two",
      zeroQ[kernel - nullFactor.Transpose[nullFactor]] &&
      MatrixRank[kernel] === 2 && MatrixRank[nullFactor] === 2];

    (* v1033: exact Z4 deck algebra and the load-bearing weight mismatch. *)
    z4 = DiagonalMatrix[{1, I, -1, -I}];
    x4 = Sum[SparseArray[{{Mod[col, 4] + 1, col} -> 1}, {4, 4}],
             {col, 1, 4}];
    check["v1033 local flux register is an exact Z4 Weyl pair",
      zeroQ[MatrixPower[z4, 4] - IdentityMatrix[4]] &&
      zeroQ[MatrixPower[x4, 4] - IdentityMatrix[4]] &&
      zeroQ[z4.x4.ConjugateTranspose[z4] - I x4]];
    qDeck = ConstantArray[1/4, 8];
    check["v1033 common quarter deck charge has norm 1/2 and h=1/4",
      qDeck.qDeck === 1/2 && qDeck.qDeck/2 === 1/4];
    omegaS = ConstantArray[1/2, 5];
    omegaF = Join[{3/4}, ConstantArray[-1/4, 3]];
    lambdaNorm2 = omegaS.omegaS + omegaF.omegaF;
    check["v1033 D5+A3 lambda has h=1, distinct from deck h=1/4",
      omegaS.omegaS === 5/4 && omegaF.omegaF === 3/4 &&
      lambdaNorm2 === 2 && lambdaNorm2/2 === 1 &&
      lambdaNorm2/2 =!= qDeck.qDeck/2];

    (* v1034: exact source parent envelope.  The source's 3/5 is a
       dispersion amplitude; a standard symmetric NN bond has half of it. *)
    dispersionAmplitude = 3/5;
    symmetricBond = dispersionAmplitude/2;
    check["v1034 source dispersion 3/5 corresponds to symmetric bond 3/10",
      symmetricBond === 3/10 && 2 symmetricBond === dispersionAmplitude &&
      symmetricBond =!= dispersionAmplitude];
    threshold[xx_] := 1 - xx + Sqrt[1 + 4 xx^2];
    thresholdPrime = D[threshold[xx], xx];
    xStar = 1/(2 Sqrt[3]);
    gapStar = 1 + Sqrt[3]/2;
    derivativeRoots = Solve[
      {thresholdPrime == 0, 0 <= xx <= dispersionAmplitude}, xx, Reals];
    check["v1034 unique derivative root lies inside the source domain",
      derivativeRoots === {{xx -> xStar}} && 0 < xStar < dispersionAmplitude &&
      PossibleZeroQ[thresholdPrime /. xx -> xStar]];
    endpointValues = threshold /@ {0, dispersionAmplitude};
    check["v1034 endpoint comparison fixes minimum 1+sqrt(3)/2",
      PossibleZeroQ[threshold[xStar] - gapStar] &&
      And @@ (TrueQ[FullSimplify[# > gapStar]] & /@ endpointValues)];

    (* v1035: physical-position Fourier convention D -> i k.  Retain I:
       c0=-s.q and c_i=i (B p)_i.  The source Ward equations then propagate
       both affine constraints exactly. *)
    {xx, yy, zz} = Unique /@ {"x", "y", "z"};
    k = {xx, yy, zz};
    {r2, b, trace, scalar, kp, kq, c} = tensorData[k];
    coupling = Unique["g"];
    rho = Unique["rho"];
    current = Array[Unique["j"] &, 3];
    tau = Array[Unique["tau"] &, 6];
    q = Array[Unique["q"] &, 6];
    canonicalP = Array[Unique["p"] &, 6];
    dotQ = kp.canonicalP;
    dotP = -kq.q - coupling tau;
    dotRho = -I k.current;
    dotCurrent = -I b.tau;
    psi0 = -scalar.q + coupling rho;
    psi = I b.canonicalP - coupling current;
    dotPsi0 = -scalar.dotQ + coupling dotRho;
    dotPsi = I b.dotP - coupling dotCurrent;
    check["v1035 full-complex c0=-s.q, ci=iBp obey Ward propagation",
      zeroQ[dotPsi0 - I k.psi] && zeroQ[dotPsi]];
    {alpha, beta, gamma} = Unique /@ {"alpha", "beta", "gamma"};
    coefficientSolution = Solve[
      {gamma + beta == 0, alpha + beta == 0}, {alpha, beta}];
    check["v1035 Ward cancellation uniquely fixes alpha=gamma, beta=-gamma",
      coefficientSolution === {{alpha -> gamma, beta -> -gamma}}];
    lambda = Unique["lambda"];
    phiValues = {0, 1, 2, 4};
    interactionResidual = lambda Sum[
      (phiValues[[site]] + phiValues[[Mod[site, 4] + 1]])
      (phiValues[[Mod[site, 4] + 1]] - phiValues[[site]])^3/24,
      {site, 1, 4}
    ];
    check["v1035 phi4 sample has homogeneous residual -17 lambda/2",
      PossibleZeroQ[interactionResidual + 17 lambda/2]];
  ];

  If[standalone,
    Print["--- TFPT round-7 Wolfram mirrors: ", $pass, " passed, ", $fail,
          " failed ---"];
    If[$fail == 0, Print["ALL ROUND7 WOLFRAM CHECKS PASSED"], Exit[1]]
  ];
];
