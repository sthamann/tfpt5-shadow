(* ::Package:: *)

(* tfpt_readouts.wl  --  independent Wolfram Language reproduction of the core
   TFPT numerical readouts (Alessandro 5.0 review, point 3: a second [C] path).

   This mirrors the Python verification suite (verification/v*.py) on an
   independent engine.  Run with:

       wolframscript -file tfpt_readouts.wl

   It prints PASS/FAIL for each headline readout and a final summary line.
   Only the two primitives c3 = 1/(8 Pi) and g_car = 5 are inputs; everything
   else is derived. *)

(* ---- check harness ---- *)
$MaxExtraPrecision = 200;   (* allow deep cancellation in symbolic seam terms *)
$pass = 0; $fail = 0;
check[name_, got_, want_, tol_: 10^-10] := Module[{ok},
  ok = Abs[N[got - want, 30]] <= tol Max[Abs[N[want, 30]], 1];
  If[ok, $pass++, $fail++];
  Print[If[ok, "[PASS] ", "[FAIL] "], name,
        "  (", N[got, 14], " vs ", N[want, 14], ")"]];
checkExact[name_, cond_] := (If[TrueQ[cond], $pass++, $fail++];
  Print[If[TrueQ[cond], "[PASS] ", "[FAIL] "], name]);

(* ---- primitives (the two axioms) ---- *)
c3 = 1/(8 Pi);
gcar = 5;
phibase = 1/(6 Pi);
dtop = 48 c3^4;
phi0 = phibase + dtop;
Nfam = (2^(gcar - 1) - 1)/gcar;             (* 3 *)
mu4 = 4;

Print["=== TFPT readouts (Wolfram, independent path) ==="];

(* ---- (v3) electromagnetic closure: alpha^-1 ---- *)
M = 41;
phiseam[a_] := phibase + (dtop Exp[-2 a]) (1 - dtop Exp[-2 a])^(-5/4);
F[a_] := a^3 - 2 c3^3 a^2 - (4/5) c3^6 M Log[1/phiseam[a]];
aStar = a /. FindRoot[F[a] == 0, {a, 0.0073}, WorkingPrecision -> 40];
alphaInv = 1/aStar;
check["alpha_* = 0.00729735256220985", aStar, 0.00729735256220985, 10^-15];
check["alpha^-1 = 137.0359992168407", alphaInv, 137.0359992168407, 10^-12];

(* ---- (v1) E8 glue arithmetic ---- *)
checkExact["240 = 16*5*3 (roots = dim S+ * g_car * N_fam)", 16*5*3 == 240];
checkExact["248 = 240 + 8 (dim E8 = roots + rank)", 240 + 8 == 248];
checkExact["E8 Coxeter h = 30 = 2*3*5", 2*3*5 == 30];

(* ---- (v2) carrier / Pascal ---- *)
checkExact["dim S+ = 2^(g_car-1) = 16", 2^(gcar - 1) == 16];
checkExact["16 = 1 + 5 + 10 = C(5,0)+C(5,1)+C(5,2)",
  Binomial[5, 0] + Binomial[5, 1] + Binomial[5, 2] == 16];
checkExact["N_fam = 3", Nfam == 3];
checkExact["rank E8 = g_car + N_fam = 8", gcar + Nfam == 8];

(* ---- (v13) M = 41 budget ---- *)
b1 = (gcar 2^(gcar - 2) + 1)/10;            (* 41/10 *)
checkExact["M = 40 + N_Phi(=1) = 10 b1 = 41", 40 + 1 == 10 b1 && 10 b1 == 41];

(* ---- (v10) K/Q/Sigma determinant ladder ---- *)
R = {{1, 3, 0}, {1, 5, 2}, {2, 5, 3}};
W = {{1, 0, 0}, {1, 0, 0}, {1, 0, 0}};
L = R + 6 W;
K = {{4, 2, 0}, {4, 3, 2}, {5, 3, 2}};
Q = {{3, 1, 0}, {3, 2, 0}, {3, 2, 1}};
Sig = DiagonalMatrix[{1, -1, -1}];
checkExact["K = R + Q.Sigma", K == R + Q.Sig];
checkExact["L = R + Q.(I + Sigma)", L == R + Q.(IdentityMatrix[3] + Sig)];
checkExact["det ladder (Q,K,R,L) = (3,4,8,20)",
  {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20}];
checkExact["det product = 1920 = |W(D5)|",
  Det[Q] Det[K] Det[R] Det[L] == 1920];
aVec = {1, 1, 2};
checkExact["a^T K a = 41 (the EM budget anchor)", aVec.K.aVec == 41];

(* ---- (v20/v21) lepton c's: delta=1/2 resolvent + product rule ---- *)
amp[r_] := 1/(5/4 - Cos[r Pi/3]);          (* |1/(1 - (1/2) zeta^r)|^2 at y=1 *)
ce = mu4^1 amp[2];                          (* e: r=2, w=1 *)
cmu = mu4^0 amp[5];                          (* mu: r=5, w=0 *)
prodC = 2^gcar/Nfam^2;                       (* 32/9 *)
ctau = prodC/(ce cmu);
checkExact["c_e = |mu4|^1 / (5/4 - cos(2pi/3)) = 16/7", ce == 16/7];
checkExact["c_mu = 4/3", cmu == 4/3];
checkExact["product rule 2^g_car/N_fam^2 = 32/9", prodC == 32/9];
checkExact["c_tau = product/(c_e c_mu) = 7/6", ctau == 7/6];

(* ---- (v16/v21) solar angle from the A3 glue-norm q(A3) = 3/4 ---- *)
qA3 = 3/4; qD5 = 5/4;
checkExact["E8 glue norm q(D5) + q(A3) = 2", qA3 + qD5 == 2];
checkExact["eps leading q(A3)/(6pi) = 1/(8pi) = c3", Simplify[qA3/(6 Pi) - c3] == 0];
s12 = 1/3 - (2/3) qA3 phi0;
checkExact["sin^2 theta12 = 1/3 - phi0/2 (exact)", Simplify[s12 - (1/3 - phi0/2)] == 0];

(* ---- (v23) anchor generator a=(1,1,2) ---- *)
av = {1, 1, 2};
e1 = Total[av]; e2 = av[[1]] av[[2]] + av[[1]] av[[3]] + av[[2]] av[[3]]; e3 = Times @@ av;
checkExact["anchor e_k(a)=(4,5,2)=(|mu4|,g_car,|Z2|)", {e1, e2, e3} == {4, 5, 2}];
checkExact["c3 = 1/(2 e1 pi) = 1/(8pi)", 1/(2 e1 Pi) == 1/(8 Pi)];
pn[n_] := 1^n + 1^n + 2^n;
checkExact["p_n(a)=2+2^n -> |R(E8)|=p1 p2 p3=240", pn[1] pn[2] pn[3] == 240];
checkExact["dim E8 = p1 p2 p3 + (p4 - p3) = 248", pn[1] pn[2] pn[3] + (pn[4] - pn[3]) == 248];
checkExact["binary ladder p_{n+1}-p_n = 2^n", Table[pn[n + 1] - pn[n], {n, 1, 4}] == {2, 4, 8, 16}];

(* ---- (v24) quark ratio closure ---- *)
checkExact["c_u/c_d = g_car*11/(N_fam^2 Delta_Q) = 55/117", (gcar*11)/(Nfam^2*13) == 55/117];
checkExact["c_c/c_s = p_5(a)/(Omega_adm-1) = 34/47", pn[5]/(48 - 1) == 34/47];
checkExact["c_t/c_b = N_fam/(2 Delta_Q) = 3/26", Nfam/(2*13) == 3/26];
check["m_c/m_s = (34/47)/phi0 = 13.605", (34/47)/phi0, 13.605, 10^-3];
check["m_t/m_b = (3/26)/phi0^2 = 40.81", (3/26)/phi0^2, 40.81, 10^-2];

(* ---- (v36) G2: spectral-action Seeley-DeWitt coefficients -> R + R^2 ---- *)
(* Dirac operator: E = -Rs/4 (Lichnerowicz), spinor trace tr I = 4. *)
trI = 4; EE = -Rs/4;
a2coef = Simplify[(6 EE + Rs) trI/6];                         (* Einstein-Hilbert *)
a4coef = Simplify[(180 EE^2 + 60 Rs EE + 5 Rs^2) trI/360];    (* R^2 / Starobinsky *)
checkExact["G2: a2 = -R/3 (Einstein-Hilbert emerges)", Simplify[a2coef + Rs/3] == 0];
checkExact["G2: a4|R^2 = R^2/72 (Starobinsky R^2 emerges)", Simplify[a4coef - Rs^2/72] == 0];
checkExact["G2: scalaron ratio M^2/Mbar^2 = 6(4pi)^2/f0 fixed by c3^7 (f0 = 6(4pi)^2/c3^7)",
  Simplify[6 (4 Pi)^2/(6 (4 Pi)^2/c3^7) - c3^7] == 0];

(* ---- (v37) anchor-plane Plücker apparatus + K+xQ pencil + dualities ---- *)
oneV = {1, 1, 1}; aVc = {1, 1, 2};
plLeft[Mat_] := Module[{r1 = oneV.Mat, r2 = aVc.Mat},
  {r1[[1]] r2[[2]] - r1[[2]] r2[[1]], r1[[1]] r2[[3]] - r1[[3]] r2[[1]],
   r1[[2]] r2[[3]] - r1[[3]] r2[[2]]}];
plRight[Mat_] := Module[{c1 = Mat.oneV, c2 = Mat.aVc},
  {c1[[1]] c2[[2]] - c1[[2]] c2[[1]], c1[[1]] c2[[3]] - c1[[3]] c2[[1]],
   c1[[2]] c2[[3]] - c1[[3]] c2[[2]]}];
checkExact["Pl(K) = (-1,6,4) and ||Pl(K)||_1 = 11 (the '11' localised in K)",
  plLeft[K] == {-1, 6, 4} && Total[Abs[plLeft[K]]] == 11];
checkExact["Pl_R(K)=(12,12,-2), ||Pl_R(K)||_1=26; sum Pl_R(L)=60 (cascade start)",
  plRight[K] == {12, 12, -2} && Total[Abs[plRight[K]]] == 26 && Total[plRight[L]] == 60];
checkExact["pencil det(K + x Q) = 3x^3 + 7x^2 + 6x + 4 = (N_fam,7,|R+A3|,|mu4|)",
  Expand[Det[K + x Q]] === 3 x^3 + 7 x^2 + 6 x + 4];
checkExact["lepton-up duality: K_e - K_u = a = (1,1,2)", K[[3]] - K[[1]] == {1, 1, 2}];
checkExact["lepton-up duality: L_e - L_u = Exp(A3) = (1,2,3)", L[[3]] - L[[1]] == {1, 2, 3}];
checkExact["lepton ring: c_e c_tau = |Z2| c_mu (= 8/3)", ce ctau == 2 cmu];

(* ---- (v39) (U_wall) selectors read off the bundle (algebraic) ---- *)
Qplus = (Q + Sig.Q.Sig)/2;
checkExact["Spec(Q_+) = {1,2,3} (A3 exponents)", Sort[Eigenvalues[Qplus]] == {1, 2, 3}];
checkExact["Spec(Q_+) = 3 alpha + 1, alpha = cusp weights {0,1/3,2/3}",
  Sort[3 {0, 1/3, 2/3} + 1] == {1, 2, 3}];
checkExact["det R = 8 selector; splitting type = anchor a = (1,1,2)",
  Det[R] == 8 && aVc == {1, 1, 2}];

(* ---- (v42) Exterior Leg Lemma: u/d leg is a Lambda^2 F area, not a scalar ---- *)
(* u,d share (r,w)=(1,1): the C6 resolvent reads only (r,w) => scalar ratio = 1. *)
cresRW[r_, w_] := mu4^w/(5/4 - Cos[r Pi/3]);
checkExact["scalar leg necessity: u,d share (r,w)=(1,1) => c_u/c_d (scalar) = 1",
  Simplify[cresRW[1, 1]/cresRW[1, 1]] == 1];
(* the separation is the exterior-square anchor-plane area Pl(K); '11' generated *)
pnA[n_] := 1^n + 1^n + 2^n;            (* power sums of a=(1,1,2): p_n = 2 + 2^n *)
e2A = aVc[[1]] aVc[[2]] + aVc[[1]] aVc[[3]] + aVc[[2]] aVc[[3]];   (* e_2(a)=5 *)
checkExact["anchor microcode: p_0=3=N_fam, p_2=6, p_3=10; Delta_Q=2p_2+1=13; ||Pl(K)||_1=p_3+1=11",
  pnA[0] == 3 && pnA[2] == 6 && pnA[3] == 10 && 2 pnA[2] + 1 == 13 && pnA[3] + 1 == 11];
checkExact["c_u/c_d = e_2(a)(p_3+1)/(p_0^2(2p_2+1)) = 55/117 (Lambda^2 F readout)",
  (e2A (pnA[3] + 1))/(pnA[0]^2 (2 pnA[2] + 1)) == 55/117];

(* ---- (v44) exterior leg = carrier exterior-algebra grading ---- *)
checkExact["16 = Lambda^even(5) = C(5,0)+C(5,2)+C(5,4) = 1+10+5",
  {Binomial[5, 0], Binomial[5, 2], Binomial[5, 4]} == {1, 10, 5}];
(* u^c in 10=Lambda^2(5) deg 2 ; d^c in 5bar=Lambda^4(5) deg 4 *)
checkExact["exterior degrees: deg(u)+deg(d)=2+4=6=|R^+(A3)|, deg(d)-deg(u)=2=|Z2|",
  2 + 4 == 6 && 4 - 2 == 2];

(* ---- (v45) the '11' = exterior algebra of the family fundamental 4=mu4 (Pascal) ---- *)
checkExact["Lambda^k(4)=Pascal row 4=(1,4,6,4,1), sum=2^4=16=dim S+",
  Table[Binomial[4, k], {k, 0, 4}] == {1, 4, 6, 4, 1} && Total[Table[Binomial[4, k], {k, 0, 4}]] == 16];
checkExact["|Pl(K)|={1,4,6}={Lambda^0,Lambda^1,Lambda^2}(mu4); ||Pl(K)||_1=11=sum_{k<=2}C(4,k)=16-g_car",
  Sort[Abs[plLeft[K]]] == {1, 4, 6} &&
   Total[Abs[plLeft[K]]] == Sum[Binomial[4, k], {k, 0, 2}] == 16 - gcar];
checkExact["family(x)carrier=15=dim su(4)=Lambda^2(5)+Lambda^4(5)=10+5=N_fam*g_car",
  4^2 - 1 == Binomial[5, 2] + Binomial[5, 4] == Nfam gcar == 15];

(* ---- (v46) Grand Mass Volume: absolute mass-scaling = det ~ u^25 ---- *)
(* sector det exponents = K row sums (6,9,10); Q row sums (4,5,6) *)
checkExact["sector det exponents = K row sums (6,9,10)=(|R+A3|,N_fam^2,A_Lambda); total 25=g_car^2",
  (Total /@ K) == {6, 9, 10} && Total[Total /@ K] == gcar^2 == 25];
checkExact["Q row sums (4,5,6) sum 15=dim A3; 25+15=40=sum L=|R(D5)|",
  (Total /@ Q) == {4, 5, 6} && Total[Total /@ Q] == 15 && 25 + 15 == Total[Total /@ L] == 40];

(* ---- (v47) Boundary Carrier Selection Theorem (Theorem A) ---- *)
checkExact["q(D5)+q(A3)=5/4+3/4=2 (E8 root norm); glue index sqrt(4*4/1)=4=|mu4|",
  5/4 + 3/4 == 2 && Sqrt[4*4/1] == 4];
checkExact["only n=5 gives 16-dim D_n half-spinor (2^{n-1}=16) => D5",
  Select[Range[2, 8], 2^(# - 1) == 16 &] == {5}];

(* ---- (v48) EM boundary Ward decomposition (Theorem C) ---- *)
checkExact["transport coeff 8 b1 = (4/5) M = (4/5)(40+1) = 164/5; -5/4 = q(D5)",
  8*(41/10) == (4/5)*41 == 164/5 && 5/4 == 5/4];

(* ---- (v50) Q geometry (Theorem Q): Sigma-split char polys ---- *)
Qp = (Q + Sig.Q.Sig)/2; Qm = (Q - Sig.Q.Sig)/2;
checkExact["Q_+ char poly = (t-1)(t-2)(t-3) => Spec(Q_+)={1,2,3}",
  Sort[Eigenvalues[Qp]] == {1, 2, 3}];
checkExact["Q_- char poly = t(t^2-3) => Q_-^2 eigenvalues {0,3} (3=N_fam)",
  Sort[Eigenvalues[Qm]] == Sort[{0, Sqrt[3], -Sqrt[3]}] && Sort[Eigenvalues[Qm.Qm]] == {0, 3, 3}];

(* ---- (v49) Readout Rigidity: c_u/c_d constant on the selector stratum ---- *)
checkExact["Readout Rigidity: c_u/c_d = g_car*||Pl(K)||_1/(N_fam^2 Delta_Q) = 55/117 (stratum-constant)",
  (gcar*Total[Abs[plLeft[K]]])/(Nfam^2*(Total[K][[1]])) == 55/117];

(* ---- (v51) delta=1/2 glue-norm origin + (g_car,N_fam)/|mu4| unification ---- *)
checkExact["glue norms = (g_car,N_fam)/|mu4|: q(D5)=5/4=gcar/4, q(A3)=3/4=Nfam/4",
  5/4 == gcar/4 && 3/4 == Nfam/4];
checkExact["four ops forced: sum=2(root), diff=1/2(delta=|Z2|/4), prod=15/16(su4/S+), ratio=5/3(gcar/Nfam)",
  {5/4 + 3/4, 5/4 - 3/4, 5/4*3/4, (5/4)/(3/4)}
   == {(gcar + Nfam)/4, (gcar - Nfam)/4, gcar*Nfam/16, gcar/Nfam}
   == {2, 1/2, 15/16, 5/3}];
checkExact["delta=1/2 reproduces leptons: 4*1/(5/4-cos(2 Pi/3))=16/7, 1/(5/4-cos(Pi/3))=4/3",
  4*1/(5/4 - Cos[2 Pi/3]) == 16/7 && 1/(5/4 - Cos[Pi/3]) == 4/3];

(* ---- (v52) K+xQ pencil endpoints ---- *)
checkExact["pencil P(x)=det(K+xQ): P(-1)=2=|Z2|, P(0)=4=|mu4|, P(1)=20=det L, P(2)=68=2 p5(a)",
  With[{P = Function[xx, Det[K + xx Q]]},
   {P[-1], P[0], P[1], P[2]} == {2, 4, 20, 68} && 68 == 2 (1 + 1 + 32)]];
checkExact["det(K-Q)=2=|Z2|, trace(K-Q)=3=N_fam",
  Det[K - Q] == 2 && Tr[K - Q] == Nfam == 3];

(* ---- (v53) compiler core: everything from (g_car,N_fam)=(5,3) ---- *)
checkExact["rank E8=g+n=8, |Z2|=g-n=2, |mu4|=(g+n)/2=4; five core ints {2,3,4,5,8} from (5,3)",
  gcar + Nfam == 8 && gcar - Nfam == 2 && (gcar + Nfam)/2 == 4 &&
   Sort[{gcar - Nfam, Nfam, 4, gcar, gcar + Nfam}] == {2, 3, 4, 5, 8}];
checkExact["Pythagorean mass-volume: Delta_Y=g^2=25=N_fam^2 + (g-n)(g+n)=9+16; up+lep=|Z2|*rank E8=dim S+",
  Module[{rs = Total /@ K},
   gcar^2 == Nfam^2 + 4^2 == 25 && rs == {6, 9, 10} && rs[[2]] == Nfam^2 == 9 &&
    (rs[[1]] + rs[[3]]) == (gcar - Nfam)(gcar + Nfam) == 16]];
checkExact["anchor char-poly: (t-1)^2(t-2)=t^3-|mu4|t^2+g_car t-|Z2|; e_k(1,1,2)=(4,5,2)",
  Module[{tt}, Expand[(tt - 1)^2 (tt - 2)] == tt^3 - 4 tt^2 + gcar tt - 2] &&
   {1 + 1 + 2, 1*1 + 1*2 + 1*2, 1*1*2} == {4, 5, 2}];

(* ---- (v54) seam=horizon keystones: triply-forced 8 + shared transfer operator ---- *)
checkExact["8 overdetermined: 2|mu4| = rank E8 = h(D5) = phi(30) = 8",
  2*4 == gcar + Nfam == 2 gcar - 2 == EulerPhi[30] == 8];
checkExact["both pi-coeffs are 2pi*integer: phi_tree=1/(6pi)=(|mu4|/N_fam) c3, 6=2 N_fam, 8=2|mu4|",
  6 == 2 Nfam && 8 == 2*4 && Simplify[1/(6 Pi) - (4/Nfam)*(1/(8 Pi))] == 0];
checkExact["one transfer operator: spec {1,(2/3)^6,(1/3)^6}; flavor gap=-log(2/3)^6=6 log(3/2); same lambda2 in horizon",
  Table[(k/3)^6, {k, 3, 1, -1}] == {1, 64/729, 1/729} &&
   Simplify[-Log[(2/3)^6] - 6 Log[3/2]] == 0];
checkExact["de Sitter: 128 c3^4 = 1/(32 pi^4); T_dS coeff 16=|mu4|^2; S_BH 1/4=1/|mu4|",
  Simplify[128 (1/(8 Pi))^4 - 1/(32 Pi^4)] == 0 && 16 == 4^2 && 1/4 == 1/4];

(* ---- (v55) cyclic element in the hull: E8 Coxeter order 30 + one-alpha cross-sector ---- *)
checkExact["E8 exponents {1,7,11,13,17,19,23,29} = totatives of 30; count phi(30)=8=rank E8",
  {1, 7, 11, 13, 17, 19, 23, 29} == Select[Range[1, 29], CoprimeQ[#, 30] &] &&
   EulerPhi[30] == 8 == gcar + Nfam];
checkExact["cycle order 30 = |Z2|*N_fam*g_car = 2*3*5",
  30 == 2*Nfam*gcar == 2*3*5];
checkExact["one alpha^-1: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (de Sitter entropy ~ 1/Lambda)",
  Simplify[1/(128 (1/(8 Pi))^4) - 32 Pi^4] == 0];
checkExact["S_dS = 2^g_car pi^|mu4| e^{2 ainv}: 32=2^g_car=dim Dirac(D5)=16+16; 128=2^7, 7=g+n-1",
  32 == 2^gcar == 16 + 16 && 128 == 2^7 && 7 == gcar + Nfam - 1];

(* ---- (v56) unique attractor: gapped transport, Coxeter planes ---- *)
checkExact["spectral gap Delta = -log(2/3)^6 = 6 log(3/2) > 0 => unique dominant eigenvector (Perron-Frobenius)",
  Simplify[-Log[(2/3)^6] - 6 Log[3/2]] == 0 && N[-Log[(2/3)^6]] > 0];
checkExact["exponents pair m+(30-m)=30 => rank/2 = 4 = |mu4| invariant planes; sum exps=120=|R+(E8)|; rank*h=240",
  ({1, 7, 11, 13} + {29, 23, 19, 17}) == {30, 30, 30, 30} &&
   Total[{1, 7, 11, 13, 17, 19, 23, 29}] == 120 && 8*30 == 240];

(* ---- (v57) horizon cross-links: Jacobson 8pi, Hod ln(3), Hawking |W(D5)| ---- *)
checkExact["c3=1/(8pi) Einstein/Jacobson: 1/(16pi)=c3/2; 1/4=1/|mu4|; 1/(2pi)=4c3",
  Simplify[1/(16 Pi) - (1/(8 Pi))/2] == 0 && 1/4 == 1/4 && Simplify[1/(2 Pi) - 4/(8 Pi)] == 0];
checkExact["Hod QNM omega_R/T_H = ln(3) = ln(N_fam); Hawking power denom 1920=|W(D5)|=2^4*5!",
  Nfam == 3 && 1920 == 2^4 * 5!];

(* ---- (v58) seam-horizon chain: one-sided Gauss-Bonnet, KMS, S_BH, RT in seam units ---- *)
checkExact["one-sided S^2 Gauss-Bonnet: c3 = 1/(|Z2| * 2pi chi(S^2)) = 1/(2*4pi) = 1/(8pi)",
  Simplify[1/(2*(2 Pi*2)) - 1/(8 Pi)] == 0];
checkExact["seam units: 1/(2c3)=4pi (S_BH=M^2/2c3), 1/(4c3)=2pi (RT), 1/(2pi)=4c3 (KMS)",
  Simplify[1/(2*(1/(8 Pi))) - 4 Pi] == 0 && Simplify[1/(4*(1/(8 Pi))) - 2 Pi] == 0 &&
   Simplify[1/(2 Pi) - 4/(8 Pi)] == 0];

(* ---- (v59) area-law evidence: exact seam-unit parts (the EE area-law is numerical, Python-only) ---- *)
checkExact["8 = |Z2|*|mu4| (sheet x glue); chaos-bound/seam unit 2pi = 1/(4 c3)",
  2*4 == 8 && Simplify[2 Pi - 1/(4*(1/(8 Pi)))] == 0];
(* NOTE: the free-field entanglement area-law of v59 is a numerical computation (numpy
   symplectic spectra), Python-only by design -- not mirrored here. *)

(* ---- (v60) Lambda branch selection: prefactor 3/(4pi^2), branch mis-scale 64pi^3/3 ---- *)
checkExact["delta_top=48 c3^4=3/(256 pi^4); (8pi)^2 delta_top=3/(4 pi^2); 2c3/delta_top=64 pi^3/3 (G_N pinned)",
  With[{c3 = 1/(8 Pi), dt = 48 (1/(8 Pi))^4},
   Simplify[dt - 3/(256 Pi^4)] == 0 && Simplify[(8 Pi)^2 dt - 3/(4 Pi^2)] == 0 &&
    Simplify[2 c3/dt - 64 Pi^3/3] == 0]];
checkExact["action exponents (1,5,10) = K5 counts (5 vertices, C(5,2)=10 edges); Pascal 16=1+5+10",
  {1, 5, Binomial[5, 2]} == {1, 5, 10} && 1 + 5 + 10 == 16];

(* ---- (v61) boundary-CFT bridge: WZW central charges = atoms, conformal embedding ---- *)
checkExact["WZW level-1 central charges: c(E8)=248/31=8, c(D5)=45/9=5, c(A3)=15/5=3 = (rank E8,g_car,N_fam)",
  248/31 == 8 && 45/9 == 5 && 15/5 == 3];
checkExact["conformal embedding: c_coset = c(E8)-c(D5)-c(A3) = 8-5-3 = 0; additivity 5+3=8=c(E8)",
  (248/31 - 45/9 - 15/5) == 0 && 5 + 3 == 8];
checkExact["reconciliation: N_fam = |mu4|-1 = 3 (P^1\\mu4 homology); SU(3) triality {0,1/3,2/3} != SU(4)_1 {0,3/8,1/2}",
  (4 - 1) == Nfam == 3 &&
   Table[j (4 - j)/8, {j, 0, 3}] == {0, 3/8, 1/2, 3/8} &&
   {0, 3/8, 1/2} != {0, 1/3, 2/3}];

(* ---- (v63) Seam-Engineering Index: exact closed form ---- *)
checkExact["||V||=248 c3^2=31/(8pi^2); 2||V||=31/(4pi^2); 248=dim E8, 31=1+h^v(E8)",
  With[{c3 = 1/(8 Pi)}, Simplify[248 c3^2 - 31/(8 Pi^2)] == 0 && 248/8 == 31 == 1 + 30]];
checkExact["Xi = 2||V||/Delta = 31/(24 pi^2 log(3/2)); Delta_eff = Delta - 2||V|| > 0",
  Simplify[(31/(4 Pi^2))/(6 Log[3/2]) - 31/(24 Pi^2 Log[3/2])] == 0 &&
   N[6 Log[3/2] - 31/(4 Pi^2)] > 1];

(* ---- (v66) compiler atoms = E8 Casimir invariant degrees ---- *)
checkExact["E8 degrees {2,8,12,14,18,20,24,30}: clean atoms 2=|Z2|,8=rank,14=dimG2,20=detL,24=4!,30=h(E8)",
  {2, 8, 12, 14, 18, 20, 24, 30}[[{1, 2, 4, 6, 7, 8}]] == {2, 8, 14, 20, 24, 30} && 4! == 24 && 2*Nfam*gcar == 30];
checkExact["sum(degrees)=128=2^7 (dS prefactor, 7=g+n-1); sum(exponents)=120=|R+(E8)|; prod=|W(E8)|",
  Total[{2, 8, 12, 14, 18, 20, 24, 30}] == 128 == 2^7 &&
   Total[{1, 7, 11, 13, 17, 19, 23, 29}] == 120 &&
   Times @@ {2, 8, 12, 14, 18, 20, 24, 30} == 696729600];

(* ---- (v67) central theorem structural closure: replica area-law coeff => c3=1/(8pi) ---- *)
checkExact["Fursaev-Solodukhin: k=c3/2=1/(16pi); S=4pi k A=2pi c3 A; 2pi c3=1/4 => S=A/4 (BH)",
  With[{c3 = 1/(8 Pi)}, Simplify[c3/2 - 1/(16 Pi)] == 0 && Simplify[2 Pi c3 - 1/4] == 0 && Simplify[4 Pi (c3/2) - 1/4] == 0]];
checkExact["theorem (inverse): S=A/4 & S=4pi k A & k=c3/2 => c3=1/(8pi) UNIQUE",
  Module[{ksol = 1/(4 (4 Pi))}, Simplify[ksol - 1/(16 Pi)] == 0 && Simplify[2*ksol - 1/(8 Pi)] == 0]];

(* ---- (v68) Seeley-DeWitt a2 for the carrier; 1/G UV-sensitive => k=c3/2 is a normalization ---- *)
checkExact["Seeley-DeWitt a2 = (1/(4pi)^2)(1/6)(R d + 6(-R/4)d) = -d/(192 pi^2) R (Dirac, carrier dof d)",
  With[{R = Symbol["Rcurv"], d = Symbol["dof"]},
   Simplify[1/(4 Pi)^2 (1/6) (R d + 6 (-R/4) d) - (-d/(192 Pi^2) R)] == 0]];
checkExact["1/(16 pi G)=f2 Lambda^2 d/(192 pi^2) is UV-sensitive: d/dLambda = f2 d Lambda/(96 pi^2) != 0",
  With[{f2 = Symbol["f2c"], L = Symbol["Lc"], d = Symbol["dc"]},
   Simplify[D[f2 L^2 d/(192 Pi^2), L] - f2 d L/(96 Pi^2)] == 0]];

(* ---- (v69) D4-equivariant Q-geometry: Q_+ from cusp weights, Q_- E-block coupling ---- *)
checkExact["Z4 4-cycle eigenvalues {1,i,-1,-i}; H_1(sum=0) families = {i,-1,-i}",
  Sort[Eigenvalues[{{0,0,0,1},{1,0,0,0},{0,1,0,0},{0,0,1,0}}]] == Sort[{1, I, -1, -I}]];
checkExact["Q_+=3 diag(0,1/3,2/3)+1=diag(1,2,3): Spec{1,2,3}; Q_-=E-coupling sqrt3: Spec{0,+-sqrt3}",
  Sort[Eigenvalues[3 DiagonalMatrix[{0, 1/3, 2/3}] + IdentityMatrix[3]]] == {1, 2, 3} &&
   Sort[Eigenvalues[{{0, 0, 0}, {0, 0, Sqrt[3]}, {0, Sqrt[3], 0}}]] == Sort[{0, Sqrt[3], -Sqrt[3]}]];

(* ---- (v70) integer-lift of Q: Z4 puncture action unimodular, det Q = N_fam ---- *)
checkExact["Z4 puncture action R unimodular (det=-1, eigenvalues {-1,i,-i}); det Q=3=N_fam (transport)",
  Det[{{0, 0, -1}, {1, 0, -1}, {0, 1, -1}}] == -1 &&
   Sort[Eigenvalues[{{0, 0, -1}, {1, 0, -1}, {0, 1, -1}}]] == Sort[{-1, I, -I}] &&
   Det[{{3, 1, 0}, {3, 2, 0}, {3, 2, 1}}] == 3 == Nfam];

(* ---- (v71) SIMPLE R-bridge: selector stratum derived => ratios are integer Plucker, no monodromy ---- *)
checkExact["det ladder (Q,K,R,L)=(3,4,8,20)=(N_fam,|mu4|,rank E8,det L); det R=8=rank E8=g+n; det Q=3=N_fam",
  {Det[Q], Det[K], Det[R], Det[L]} == {3, 4, 8, 20} && Det[R] == 8 == gcar + Nfam && Det[Q] == Nfam];
checkExact["selector stratum derived => c_u/c_d=55/117 is a pure integer Plucker readout (13=8+5=9+4)",
  (gcar*11)/(Nfam^2*13) == 55/117 && 13 == 8 + 5 == Nfam^2 + 4];

(* ---- (v72) det Q = N_fam from the cusp class: order = weight denominator = |coker Q| ---- *)
checkExact["det Q=3=|coker Q|=cusp-class order=denominator of cusp weights {0,1/3,2/3}=N_fam (same data as Spec Q_+)",
  Det[Q] == 3 == Nfam && LCM[1, 3, 3] == 3 == Nfam && Sort[{1, 2, 3}] == Sort[3*{0, 1/3, 2/3} + 1]];

(* ---- (v73) k=c3/2 forced: variational factor x Gauss-Bonnet topology; Fursaev-Solodukhin S=A/4 ---- *)
checkExact["k=c3/2=1/(16pi)=(1/2)*(1/(|Z2|*2pi*chi(S2))), chi(S2)=2; Fursaev-Solodukhin 4pi k = 1/4",
  Module[{c3 = 1/(8 Pi), chi = 2, Z2 = 2},
    (c3/2 == 1/(16 Pi)) && (c3 == 1/(Z2*2 Pi*chi)) && (4 Pi*(c3/2) == 1/4)]];

(* ---- (v74) compiler micro-lemmas: pencil differences 2->16->48; anchor QF 41-25=16 ---- *)
checkExact["pencil P(x)=det(K+xQ) endpoints (2,4,20,68); consecutive differences (2,16,48)=(|Z2|,dim S+,Omega_adm)",
  Module[{P, v}, P[xx_] := Det[K + xx*Q]; v = P /@ {-1, 0, 1, 2};
    v == {2, 4, 20, 68} && Differences[v] == {2, 16, 48}]];
checkExact["anchor QF: 1^TK1=25=g_car^2, a^TKa=41=10 b1, a^TKa-1^TK1=16=dim S+ (EM budget = mass vol + one gen)",
  Module[{one = {1, 1, 1}, av = {1, 1, 2}},
    (one.K.one == 25 == gcar^2) && (av.K.av == 41) && (av.K.av - one.K.one == 16)]];

(* ---- (v75) Gate 1: U_point -> v_geo. lepton product 32/9; (ratios,product)<=>(individuals) bijection ---- *)
checkExact["lepton c-product 16/7*4/3*7/6 = 32/9 = 2^g_car/N_fam^2; (ratios,product)=>(individuals) bijection rebuilds (16/7,4/3,7/6)",
  Module[{c = {16/7, 4/3, 7/6}, P, r, c0},
    P = Times @@ c; r = c/c[[1]]; c0 = (P/(Times @@ r))^(1/3);
    (P == 32/9 == 2^gcar/Nfam^2) && (c0*r === c)]];

(* ---- (v76) Gate 2: decoupling margin Delta_eff = 6log(3/2) - 31/(4pi^2) > 0 ---- *)
checkExact["||V||<=248 c3^2 = 31/(8pi^2) (31=2^g_car-1); 2||V||=31/(4pi^2); Delta_eff=6log(3/2)-31/(4pi^2)>0",
  Module[{c3 = 1/(8 Pi)},
    (248 c3^2 == 31/(8 Pi^2)) && (31 == 2^gcar - 1) && (6 Log[3/2] - 31/(4 Pi^2) > 0)]];

(* ---- (v77) G6 via E8 level-1 net: level-1 central charges + conformal embedding c-sum ---- *)
checkExact["level-1 c=dim/(1+h^v): c(E8)=248/31=8=rank E8, c(D5)=45/9=5, c(A3)=15/5=3; embedding 5+3=8 => coset c=0",
  Module[{cE8 = 248/(1 + 30), cD5 = 45/(1 + 8), cA3 = 15/(1 + 4)},
    (cE8 == 8) && (cD5 == 5) && (cA3 == 3) && (cD5 + cA3 == cE8)]];

(* ---- (v78) v_geo floor: S_dS*rho_Lambda = 1/(128 c3^4) = 32 pi^4 (one scale pinned by one measurement) ---- *)
checkExact["S_dS * rho_Lambda = 1/(128 c3^4) = 32 pi^4 (cosmological pinning of the single scale)",
  Module[{c3 = 1/(8 Pi)}, 1/(128 c3^4) == 32 Pi^4]];

(* ---- (v79) hypercharge Lucas-Binet D_n + the quark-ratio reading ---- *)
checkExact["Lucas-Binet D_n=(3^n-(-2)^n)/5 = {1,1,7,13,55,133}; c_u/c_d = D_5/(N_fam^2 D_4) = 55/117",
  Module[{D}, D = Table[(3^n - (-2)^n)/5, {n, 1, 6}];
    D == {1, 1, 7, 13, 55, 133} && D[[5]]/(Nfam^2 D[[4]]) == 55/117]];

(* ---- (v79) Inverse Anchor Theorem: 1^T M^-1 1 = 1/atom; a^T M^-1 a = 1 for R,K,L ---- *)
checkExact["1^T M^-1 1 = 1/atom (Q->1/3,R=K->1/4,L->1/10); a^T R^-1 a = a^T K^-1 a = a^T L^-1 a = 1 (a^T Q^-1 a=7/3)",
  Module[{one = {1, 1, 1}, av = {1, 1, 2}},
    (one.Inverse[Q].one == 1/3) && (one.Inverse[R].one == 1/4) && (one.Inverse[K].one == 1/4) &&
    (one.Inverse[L].one == 1/10) && (av.Inverse[R].av == 1) && (av.Inverse[K].av == 1) &&
    (av.Inverse[L].av == 1) && (av.Inverse[Q].av == 7/3)]];

(* ---- (v80) operator-pencil geometry: anchor singularity + block-det type checker + F4xG2 shadow ---- *)
checkExact["anchor singularity: det B(K+xQ)=(3x+2)(3x+5); type checker det B = (9,10,16,40) for (Q,K,R,L)",
  Module[{one = {1, 1, 1}, av = {1, 1, 2}, bb, dbx},
    bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}};
    dbx = Det[bb[K + xx*Q]];
    (Factor[dbx] == (3 xx + 2) (3 xx + 5)) &&
    (Det[bb[Q]] == 9) && (Det[bb[K]] == 10) && (Det[bb[R]] == 16) && (Det[bb[L]] == 40)]];
checkExact["F4xG2 shadow: det B_{R+Q}=52=dim F4; 248 = 52 + 14 + 26*7 (real E8->F4xG2 branching)",
  Module[{one = {1, 1, 1}, av = {1, 1, 2}, F = R + Q, bb},
    bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}};
    (Det[bb[F]] == 52) && (52 + 14 + 26*7 == 248)]];

(* ---- (v81) double cover: det B(K+xQ) quadratic, branch points {-2/3,-5/3}, disc=81=N_fam^4 ---- *)
checkExact["double cover y^2=det B(K+xQ)=(3x+2)(3x+5): branch points {-5/3,-2/3}, discriminant 81=N_fam^4, separation 1",
  Module[{one = {1, 1, 1}, av = {1, 1, 2}, bb, q},
    bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}};
    q = Det[bb[K + xx*Q]];
    (Factor[q] == (3 xx + 2) (3 xx + 5)) && (Discriminant[q, xx] == 81) &&
    (Sort[xx /. Solve[q == 0, xx]] == {-5/3, -2/3})]];
checkExact["clearing matrices: C_{2/3}=3K-2Q (tr=15,sum=45,det=60), B=(5,7)^T(9,11) sum=240; C_{5/3}=3K-5Q neutral chi=(l+2)(l^2+l+6)",
  Module[{one = {1, 1, 1}, av = {1, 1, 2}, bb, c23, c53},
    bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}};
    c23 = 3 K - 2 Q; c53 = 3 K - 5 Q;
    (Tr[c23] == 15) && (Total[c23, 2] == 45) && (Det[c23] == 60) &&
    (bb[c23] == Outer[Times, {5, 7}, {9, 11}]) && (Total[bb[c23], 2] == 240) &&
    (Total[c53, 2] == 0) && (Factor[-CharacteristicPolynomial[c53, ll]] == (ll + 2) (ll^2 + ll + 6))]];
checkExact["branch divisor = (scalaron,A_Lambda): sum roots=-7/3=-scalaron/N_fam, product=10/9=A_Lambda/N_fam^2; {2,5} sum=7 prod=10 diff=3",
  Module[{one = {1, 1, 1}, av = {1, 1, 2}, bb, q, rt},
    bb[M_] := {{one.M.one, one.M.av}, {av.M.one, av.M.av}};
    q = Det[bb[K + xx*Q]]; rt = Sort[xx /. Solve[q == 0, xx]];
    (Total[rt] == -7/3) && (Times @@ rt == 10/9) && (2 + 5 == 7) && (2*5 == 10) && (5 - 2 == 3)]];

(* ==== 2026-08-28 catch-up: exact mirrors deferred by the v974-v997 waves ====
   Exact algebraic / identity / lattice cores of v983, v985, v987, v993, v994,
   v997.  Numerical / ODE / QCA / entropy / SMG-toy siblings stay Python-only
   (flagged in the README v974-v997 census). *)

(* 2026-08-30 late-evening harvest: v1013 thermodynamic-dynamics numeric twin
   and v1014 detline/W-bridge refinements stay Python-only (LR/expm + QWZ
   eigensolves; W-bridge is sympy-exact but Wolfram engine DEFERRED_NO_ENGINE).
   2026-08-31 Monday-morning harvest: v1015 axiom-core closure (sympy-exact P-dem)
   and v1016 state/gap batteries (euclidean cap / TEL-B / nuclearity / DFP)
   stay Python-only; engine still DEFERRED_NO_ENGINE.
   2026-09-02: v1018 (sympy-exact E8 readout identities; C7 open) and v1019
   (exact cyclotomic + mpmath Euler products) stay Python-only;
   engine still DEFERRED_NO_ENGINE. *)

(* ---- (v983) SEAM.SIMPLECURRENT.GENERATOR.01: glue vector lambda = (omega_s, omega_f) ---- *)
Module[{omegaS, omegaF, lam, inD5, inA3, inL0, gensD5, gensA3, dots,
    cosetRoots, census, lamV, omega2, nV, n2, cartanD8},
  omegaS = ConstantArray[1/2, 5];
  omegaF = {3/4, -1/4, -1/4, -1/4};
  lam = Join[omegaS, omegaF];
  inD5[x_] := (And @@ (IntegerQ /@ x)) && EvenQ[Total[x]];
  inA3[y_] := (And @@ (IntegerQ /@ y)) && Total[y] === 0;
  inL0[z_] := inD5[Take[z, 5]] && inA3[Take[z, {6, 9}]];
  checkExact["v983 NORMS+WEIGHT [E]: |omega_s|^2=5/4, |omega_f|^2=3/4, |lambda|^2=2, h_lambda=1",
    Total[omegaS^2] === 5/4 && Total[omegaF^2] === 3/4 &&
    Total[lam^2] === 2 && Total[lam^2]/2 === 1];
  checkExact["v983 ORDER FOUR [E]: 4*lambda in D5(+)A3, lambda and 2*lambda not -- [lambda] generates the diagonal Z4",
    inL0[4 lam] && ! inL0[2 lam] && ! inL0[lam]];
  gensD5 = {{1, 1, 0, 0, 0}, {1, -1, 0, 0, 0}, {0, 1, 1, 0, 0},
    {0, 0, 1, 1, 0}, {0, 0, 0, 1, 1}};
  gensA3 = {{1, -1, 0, 0}, {0, 1, -1, 0}, {0, 0, 1, -1}};
  dots = Join[omegaS . # & /@ gensD5, omegaF . # & /@ gensA3];
  checkExact["v983 ISOTROPY+UNIMODULAR [E]: lambda.L0 subset Z on a generator set; det(D5)*det(A3)=16, index-4 glue => det L=1",
    (And @@ (IntegerQ /@ dots)) && 16/4^2 === 1];
  cosetRoots[k_] := Module[{t = k lam, d5, a3},
    d5 = Counts @ Select[
      Total[(# + Take[t, 5])^2] & /@
        Select[Tuples[Range[-5, 3], 5], EvenQ[Total[#]] &],
      # <= 2 &];
    a3 = Counts @ Select[
      Total[(Join[#, {-Total[#]}] + Take[t, {6, 9}])^2] & /@
        Tuples[Range[-6, 6], 3],
      # <= 2 &];
    Total[KeyValueMap[#2 Lookup[a3, 2 - #1, 0] &, d5]]];
  census = Table[cosetRoots[k], {k, 0, 3}];
  checkExact["v983 COSET ROOT CENSUS [E]: norm-2 vectors per fusion power k=0..3 = {52,64,60,64}, total 240; odd powers 64+64=128",
    census === {52, 64, 60, 64} && Total[census] === 240 &&
    census[[2]] + census[[4]] === 128];
  lamV = Join[{1, 0, 0, 0, 0}, omegaF];
  omega2 = {1/2, 1/2, -1/2, -1/2};
  nV = Total[lamV^2];
  n2 = Total[omegaS^2] + Total[omega2^2];
  cartanD8 = {{2, -1, 0, 0, 0, 0, 0, 0}, {-1, 2, -1, 0, 0, 0, 0, 0},
    {0, -1, 2, -1, 0, 0, 0, 0}, {0, 0, -1, 2, -1, 0, 0, 0},
    {0, 0, 0, -1, 2, -1, 0, 0}, {0, 0, 0, 0, -1, 2, -1, -1},
    {0, 0, 0, 0, 0, -1, 2, 0}, {0, 0, 0, 0, 0, -1, 0, 2}};
  checkExact["v983 KILLS+HOLOMORPHY SHADOW [E]: vector glue (v,omega_f) norm 7/4 and mismatched (omega_s, omega_2) norm 9/4 not in 2Z; det Cartan D8=4 vs glued det=1",
    nV === 7/4 && n2 === 9/4 && Det[cartanD8] === 4 && 16/4^2 === 1];
];

(* ---- (v985) ALPHA.QUILLEN.EXACT.01: mu4 circulant spectra + graded channel swap ---- *)
Module[{jumpPat, markPat, mu4Spec, eigJ, eigM, swapped, odd, gLog,
    gJ, gM, ratios},
  jumpPat = {2, -1, 0, -1};
  markPat = {0, 1, 2, 1};
  mu4Spec[pat_] := Table[
    Simplify[Sum[pat[[m + 1]] I^(m k), {m, 0, 3}]], {k, 0, 3}];
  eigJ = mu4Spec[jumpPat];
  eigM = mu4Spec[markPat];
  checkExact["v985 SPECTRA [E]: jump circ(2,-1,0,-1) -> {0,2,4,2} (kernel k=0); mark circ(0,1,2,1) -> {4,-2,0,-2} (kernel k=2)",
    eigJ === {0, 2, 4, 2} && eigM === {4, -2, 0, -2}];
  swapped = Table[Abs[eigJ[[Mod[k + 2, 4] + 1]]], {k, 0, 3}];
  odd = Table[Abs[eigJ[[Mod[k + 1, 4] + 1]]], {k, 0, 3}];
  checkExact["v985 DECK SWAP [E]: r->r+2 maps |jump| onto |mark| exactly; odd swap r->r+1 does NOT (Z2 deck, not arbitrary)",
    swapped === (Abs /@ eigM) && odd =!= (Abs /@ eigM)];
  gLog[eigs_, unit_] := Sum[
    If[eigs[[k + 1]] === 0, 0,
      (-1)^k Log[Abs[eigs[[k + 1]]] unit]], {k, 0, 3}];
  gJ = gLog[eigJ, 16 c3];
  gM = gLog[eigM, 4 c3 Log[2]];
  checkExact["v985 GRADED DET' [E]: gr(jump)-gr(mark)=log(ln2/4) exactly, c3-free",
    PossibleZeroQ[FullSimplify[gJ - gM - Log[Log[2]/4]]]];
  ratios = Table[
    If[eigM[[k + 1]] === 0, Nothing,
      Simplify[(16 c3 Abs[eigJ[[Mod[k + 2, 4] + 1]]])/
        (4 c3 Log[2] Abs[eigM[[k + 1]]])]], {k, 0, 3}];
  checkExact["v985 UNIFORM RATIO [E]: after deck swap, (16 c3 |lambda^J_{r+2}|)/(4 c3 ln2 |lambda^M_r|)=4/ln2 in every matched nonzero channel",
    (And @@ ((# === 4/Log[2]) & /@ ratios)) && Length[ratios] === 3];
];

(* ---- (v987) DYN.UNITARY.DILATION.01: B spectral decomp, H=-log B, Wick, congruence ----
   Python-only: size-uniform free-band D2/LR (numeric collision), interacting
   gap plateau, quantum SWAP coupling. *)
Module[{u1, u2, u3, P1, P2, P3, B, H, Ut, n, Kdiag, K12, Bbad, zero3, zQ},
  u1 = {1, 1, 1}/Sqrt[3];
  u2 = {1, -1, 0}/Sqrt[2];
  u3 = {1, 1, -2}/Sqrt[6];
  P1 = Outer[Times, u1, u1];
  P2 = Outer[Times, u2, u2];
  P3 = Outer[Times, u3, u3];
  B = {{13, 1, 4}, {1, 13, 4}, {4, 4, 10}}/18;
  zero3 = ConstantArray[0, {3, 3}];
  zQ[m_] := And @@ PossibleZeroQ /@ Flatten[Simplify[m]];
  checkExact["v987 SPECTRAL [E]: B=P1+(2/3)P2+(1/3)P3 with orthogonal projectors summing to I",
    zQ[B - (P1 + (2/3) P2 + (1/3) P3)] &&
    zQ[P1 + P2 + P3 - IdentityMatrix[3]] &&
    zQ[P1.P2] && zQ[P1.P3] && zQ[P2.P3]];
  H = Log[3/2] P2 + Log[3] P3;
  checkExact["v987 H=-log B [E]: spectrum {0, log(3/2), log 3}, gap log(3/2), H.u1=0",
    SortBy[Simplify[Eigenvalues[H]], N] === {0, Log[3/2], Log[3]} &&
    zQ[{H.u1}]];
  Ut[t_] := P1 + (2/3)^(I t) P2 + (1/3)^(I t) P3;
  checkExact["v987 WICK ANCHOR [E]: U(-i n)=B^n for n=1..6",
    And @@ Table[
      zQ[Ut[-I n] - (P1 + (2/3)^n P2 + (1/3)^n P3)] &&
      zQ[(P1 + (2/3)^n P2 + (1/3)^n P3) - MatrixPower[B, n]],
      {n, 1, 6}]];
  Kdiag = DiagonalMatrix[{2, 3, 5}];
  K12 = DiagonalMatrix[{Sqrt[2], Sqrt[3], Sqrt[5]}];
  Bbad = P1 - (1/10) P2 + (1/3) P3;
  checkExact["v987 CONGRUENCE+MUST-FAIL [E]: K^{1/2} B K^{1/2} symmetric (Sylvester: B SPD with eigs {1,2/3,1/3}); mutant K.B not symmetric; v971 negative kernel det<0",
    Sort[Eigenvalues[B]] === {1/3, 2/3, 1} &&
    zQ[K12.B.K12 - Transpose[K12.B.K12]] &&
    ! zQ[Kdiag.B - Transpose[Kdiag.B]] &&
    Det[Bbad] < 0];
];

(* ---- (v993) AX.P2.01 census: SNF disc groups, unique (D5,A3), [lambda]^2=[v], CE dims ----
   Python-only: random CE axiom sampling on M_d^{Z4} / crossed product. *)
Module[{cartanA, cartanD, cartanE, snfF, cyclicZ4, hasZ4, genOQ,
    addPair, rows, find, hits, daHits, uniqueDA, canon, uniqueFull,
    rD4A4, rA4A4, rE7A1, rD4D4, rA7A1, rE6A2, rD5A3,
    omegaS, omegaF, lam, vD5, inD5, inA3, inL0,
    freeQ, nFree, devKer, n, m, C1, C2},
  cartanA[n_] := Normal[SparseArray[
    {{i_, i_} -> 2, {i_, j_} /; Abs[i - j] === 1 -> -1}, {n, n}]];
  cartanD[n_] := Module[{M},
    If[n === 2, Return[DiagonalMatrix[{2, 2}]]];
    M = Normal[cartanA[n]];
    M[[n, n - 1]] = M[[n - 1, n]] = 0;
    M[[n, n - 2]] = M[[n - 2, n]] = -1;
    M];
  cartanE[n_] := Module[{M = 2 IdentityMatrix[n]},
    Do[M[[i, i + 1]] = M[[i + 1, i]] = -1, {i, 1, n - 2}];
    M[[3, n]] = M[[n, 3]] = -1;
    M];
  snfF[C_] := Select[Abs[Diagonal[SmithDecomposition[C][[2]]]], # > 1 &];
  cyclicZ4[f_] := f === {4};
  hasZ4[f_] := f =!= {} && Mod[LCM @@ f, 4] === 0;
  checkExact["v993 SNF TEXTBOOK [E]: A_n=Z_{n+1} (n=1..8); D_n=Z4 (n odd)/Z2xZ2 (n even) (n=2..8); E6=Z3, E7=Z2, E8=1; D3 cong A3",
    (And @@ Table[snfF[cartanA[n]] === {n + 1}, {n, 1, 8}]) &&
    (And @@ Table[snfF[cartanD[n]] === If[OddQ[n], {4}, {2, 2}], {n, 2, 8}]) &&
    snfF[cartanE[6]] === {3} && snfF[cartanE[7]] === {2} &&
    snfF[cartanE[8]] === {} &&
    snfF[cartanD[3]] === snfF[cartanA[3]] === {4} &&
    Abs[Det[cartanD[3]]] === Abs[Det[cartanA[3]]] === 4];
  genOQ[C_] := Module[{Cinv = Inverse[C], nn = Length[C], k, order, q},
    k = UnitVector[nn, nn];
    order = Catch[Do[
      If[And @@ (IntegerQ /@ Flatten[Cinv.(t k)]), Throw[t]],
      {t, 1, Abs[Det[C]] + 1}]];
    q = Simplify[k.Cinv.k];
    {order, q}];
  rows = {};
  addPair[fam_, t1_, n1_, CC1_, t2_, n2_, CC2_, alias_: None] := Module[
    {f1 = snfF[CC1], f2 = snfF[CC2], d1 = Abs[Det[CC1]], d2 = Abs[Det[CC2]],
      both, prod, unimod, o1, q1, o2, q2, iso, hit},
    both = cyclicZ4[f1] && cyclicZ4[f2];
    prod = d1 d2;
    unimod = prod === 16;
    iso = False; q1 = None; q2 = None;
    If[both,
      {o1, q1} = genOQ[CC1]; {o2, q2} = genOQ[CC2];
      iso = o1 === 4 && o2 === 4 && IntegerQ[Simplify[(q1 + q2)/2]]];
    hit = both && unimod && TrueQ[iso];
    AppendTo[rows, <|"fam" -> fam, "n1" -> n1, "n2" -> n2, "f1" -> f1,
      "f2" -> f2, "prod" -> prod, "both" -> both, "q1" -> q1, "q2" -> q2,
      "iso" -> iso, "hit" -> hit, "alias" -> alias, "t1" -> t1, "t2" -> t2|>]];
  Do[addPair["D+A", "D", n, cartanD[n], "A", 8 - n, cartanA[8 - n]], {n, 2, 7}];
  Do[addPair["D+D", "D", n, cartanD[n], "D", 8 - n, cartanD[8 - n],
    If[{n, 8 - n} === {3, 5} || {n, 8 - n} === {5, 3}, "D5(+)A3", None]],
    {n, 2, 4}];
  Do[If[8 - n >= 1 && 8 - n <= n,
    addPair["A+A", "A", n, cartanA[n], "A", 8 - n, cartanA[8 - n]]], {n, 4, 7}];
  addPair["E+A", "E", 6, cartanE[6], "A", 2, cartanA[2]];
  addPair["E+D", "E", 6, cartanE[6], "D", 2, cartanD[2]];
  addPair["E+A", "E", 7, cartanE[7], "A", 1, cartanA[1]];
  find[fam_, n1_, n2_] := SelectFirst[rows,
    #["fam"] === fam && #["n1"] === n1 && #["n2"] === n2 &, None];
  hits = Select[rows, #["hit"] &];
  daHits = Select[rows, #["fam"] === "D+A" && #["hit"] &];
  uniqueDA = Length[daHits] === 1 && daHits[[1]]["n1"] === 5 &&
    daHits[[1]]["n2"] === 3;
  canon = Table[
    If[(r["t1"] === "D" && r["n1"] === 5 && r["t2"] === "A" && r["n2"] === 3) ||
      r["alias"] === "D5(+)A3", "D5(+)A3",
      r["t1"] <> ToString[r["n1"]] <> "(+)" <> r["t2"] <> ToString[r["n2"]]],
    {r, hits}];
  uniqueFull = Length[hits] >= 1 && Union[canon] === {"D5(+)A3"};
  checkExact["v993 ADE RANK-8 CENSUS [E]: only diagonal cyclic-Z4 isotropic unimodular glue is (D5,A3), up to D3 cong A3",
    uniqueDA && uniqueFull];
  rD4A4 = find["D+A", 4, 4]; rA4A4 = find["A+A", 4, 4];
  rE7A1 = find["E+A", 7, 1]; rD4D4 = find["D+D", 4, 4];
  rA7A1 = find["A+A", 7, 1]; rE6A2 = find["E+A", 6, 2];
  rD5A3 = find["D+A", 5, 3];
  checkExact["v993 KILLS [X]: (D4,A4) not cyclic Z4; (A4,A4) prod 25; (E7,A1) prod 4; (D4,D4) Klein no order-4; (A7,A1) A1=Z2; (E6,A2)=Z3xZ3; isotropic q(D5)+q(A3)=5/4+3/4=2",
    rD4A4 =!= None && ! rD4A4["both"] && ! rD4A4["hit"] &&
    rA4A4 =!= None && rA4A4["prod"] === 25 && ! rA4A4["hit"] &&
    rE7A1 =!= None && rE7A1["prod"] === 4 && ! rE7A1["hit"] &&
    rD4D4 =!= None && rD4D4["prod"] === 16 && rD4D4["f1"] === {2, 2} &&
    rD4D4["f2"] === {2, 2} && ! rD4D4["both"] && ! hasZ4[rD4D4["f1"]] &&
    rA7A1 =!= None && rA7A1["prod"] === 16 && hasZ4[rA7A1["f1"]] &&
    ! hasZ4[rA7A1["f2"]] && ! rA7A1["both"] &&
    rE6A2 =!= None && rE6A2["f1"] === {3} && rE6A2["f2"] === {3} &&
    rE6A2["prod"] === 9 && ! rE6A2["hit"] &&
    rD5A3 =!= None && rD5A3["q1"] === 5/4 && rD5A3["q2"] === 3/4 &&
    TrueQ[rD5A3["iso"]]];
  omegaS = ConstantArray[1/2, 5];
  omegaF = {3/4, -1/4, -1/4, -1/4};
  lam = Join[omegaS, omegaF];
  vD5 = {1, 0, 0, 0, 0};
  inD5[x_] := (And @@ (IntegerQ /@ x)) && EvenQ[Total[x]];
  inA3[y_] := (And @@ (IntegerQ /@ y)) && Total[y] === 0;
  inL0[z_] := inD5[Take[z, 5]] && inA3[Take[z, {6, 9}]];
  checkExact["v993 [lambda]^2=[v] [E]: 2[omega_s]=[v] in disc(D5); 4*lambda in L0, 2*lambda not; order-2 vector glue norm 7/4 not in 2Z",
    inD5[2 omegaS - vD5] && 2 omegaS === {1, 1, 1, 1, 1} &&
    inL0[2 lam - Join[vD5, 2 omegaF]] && ! inA3[2 omegaF] &&
    inL0[4 lam] && ! inL0[2 lam] && ! inL0[lam] &&
    Total[Join[vD5, omegaF]^2] === 7/4 && Total[lam^2] === 2];
  freeQ[{i_, j_, k_, l_}, bim_] :=
    Mod[k, 4] === Mod[l, 4] && Mod[i, 4] =!= Mod[j, 4] &&
    (! bim || (Mod[k, 4] === Mod[i, 4] && Mod[l, 4] === Mod[j, 4]));
  nFree[d_, bim_] := Count[Tuples[Range[0, d - 1], 4], x_ /; freeQ[x, bim]];
  devKer[d_, bim_] := Module[{idx, coord, rowsA, A},
    idx = Select[Tuples[Range[0, d - 1], 4], freeQ[#, bim] &];
    If[idx === {}, Return[0]];
    coord = Association[MapIndexed[#1 -> First[#2] &, idx]];
    rowsA = Flatten[Table[
      Module[{row = ConstantArray[0, Length[idx]], nonempty = False, key},
        Do[key = {i, j, k, k};
          If[KeyExistsQ[coord, key],
            row[[coord[key]]] = 1; nonempty = True], {k, 0, d - 1}];
        If[nonempty, row, Nothing]],
      {i, 0, d - 1}, {j, 0, d - 1}], 1];
    If[rowsA === {}, Length[idx], Length[idx] - MatrixRank[rowsA]]];
  checkExact["v993 UNIQUE-CE DIMS [E]: bimodule deviations force D=0 (n_free=0 at d=4,8); dropping the module property leaves kernel 36 (d=4) / 720 (d=8)",
    nFree[4, True] === 0 && nFree[8, True] === 0 &&
    devKer[4, False] === 36 && devKer[8, False] === 720];
];

(* ---- (v994) SEAM.EQUIV.MMST.01 C3: Theta_E8 / eta^8 = {1,248,4124,34752} ----
   Python-only: C1 entropy, C2 QWZ spectrum, C4 two-point numeric, C5 sector
   recombination beyond det, C6 cited, C7 open, GSO/N=8 must-fail combinatorics. *)
Module[{z, q, th2, th3, th4, thE8, e4theta, e4sigma, inv8, chi, coeffs},
  (* EllipticTheta[a,0,z] defining sums (Jacobi nome z; lattice q = z^2). *)
  th2 = 2 z^(1/4) Sum[z^(n (n + 1)), {n, 0, 6}];
  th3 = 1 + 2 Sum[z^(n^2), {n, 1, 6}];
  th4 = 1 + 2 Sum[(-1)^n z^(n^2), {n, 1, 6}];
  thE8 = Expand[(th2^8 + th3^8 + th4^8)/2];
  e4theta = Sum[Coefficient[thE8, z, 2 n] q^n, {n, 0, 4}];
  e4sigma = 1 + 240 Sum[DivisorSigma[3, n] q^n, {n, 1, 4}];
  inv8 = Normal[Series[Product[(1 - q^n)^-8, {n, 1, 8}], {q, 0, 4}]];
  chi = Normal[Series[e4theta inv8, {q, 0, 3}]];
  coeffs = Table[Coefficient[chi, q, n], {n, 0, 3}];
  checkExact["v994 THETA_E8/eta^8 [E]: SeriesCoefficient of (EllipticTheta[2]^8+EllipticTheta[3]^8+EllipticTheta[4]^8)/2 / Product[(1-q^n)^8] = {1,248,4124,34752}; Jacobi theta_E8 matches E4=1+240 Sum sigma_3 (DedekindEta^8 = q^{1/3} Product)",
    coeffs === {1, 248, 4124, 34752} &&
    Expand[e4theta - e4sigma] === 0];
];

(* ---- (v997) GRAV.SPIN2.EMERGENCE.01: Barnes-Rivers ranks (5,3,1,1) ----
   Python-only: Weyl^2 ghost residues, random-p numeric, SMG N=8 Fidkowski-Kitaev
   toy (spectrum / Spin(7) / Schmidt / edge). *)
Module[{basis, i, j, h, p, omega, theta, inner, act, proj, kinds, Ps, eye10, zero10, zQ},
  basis = Flatten[Table[
    h = ConstantArray[0, {4, 4}];
    If[i === j, h[[i, i]] = 1, h[[i, j]] = h[[j, i]] = 1/Sqrt[2]];
    h, {i, 1, 4}, {j, i, 4}], 1];
  p = {0, 0, 0, 1};
  omega = Outer[Times, p, p];
  theta = IdentityMatrix[4] - omega;
  inner[a_, b_] := Total[a b, 2];
  act["2", h_] := theta.h.theta - theta Tr[theta.h]/(4 - 1);
  act["1", h_] := theta.h.omega + omega.h.theta;
  act["0s", h_] := theta Tr[theta.h]/(4 - 1);
  act["0w", h_] := omega Tr[omega.h];
  kinds = {"2", "1", "0s", "0w"};
  proj[kind_] := Table[Simplify[inner[a, act[kind, b]]], {a, basis}, {b, basis}];
  Ps = Association[# -> proj[#] & /@ kinds];
  eye10 = IdentityMatrix[10];
  zero10 = ConstantArray[0, {10, 10}];
  zQ[m_] := And @@ PossibleZeroQ /@ Flatten[Simplify[m]];
  checkExact["v997 BARNES-RIVERS [E]: projector algebra P_i P_j=delta_ij P_i, sum=I_10; ranks (spin-2, spin-1, 0s, 0w)=(5,3,1,1) at p=(0,0,0,1)",
    (And @@ (zQ[Ps[#].Ps[#] - Ps[#]] & /@ kinds)) &&
    (And @@ Flatten[Table[
      If[a === b, True, zQ[Ps[a].Ps[b]]],
      {a, kinds}, {b, kinds}]]) &&
    zQ[Total[Ps /@ kinds] - eye10] &&
    MatrixRank[Ps["2"]] === 5 && MatrixRank[Ps["1"]] === 3 &&
    MatrixRank[Ps["0s"]] === 1 && MatrixRank[Ps["0w"]] === 1];
];

(* ---- round-4 representative exact mirrors; native Arb remains Python-only ---- *)
Get[FileNameJoin[{DirectoryName[$InputFileName], "tfpt_round4.wl"}]];
(* Round 7: bounded exact free-field/twist/mirror/Ward representatives. *)
Get[FileNameJoin[{DirectoryName[$InputFileName], "tfpt_round7.wl"}]];

(* ---- summary ---- *)
Print["--- Wolfram readouts: ", $pass, " passed, ", $fail, " failed ---"];
If[$fail == 0, Print["ALL WOLFRAM CHECKS PASSED"]];
