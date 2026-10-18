# TFPT, Simplicity First: the Big Picture on 2026-08-28

This is the stringent version of the story: TFPT is not presently a completed theory of nature, but a two-input discrete compiler whose finite algebraic core is unusually rigid and whose remaining physical claims have been separated into named, falsifiable contracts (`AX.P1.01`, `AX.P2.01`, `QFT4D.LATTICE.FUNDAMENTAL.01`). The central methodological claim is therefore not “everything has been proved”; it is that the verified pieces repeatedly collapse apparently independent choices onto one small order-four structure, while every unclosed bridge remains visibly marked `[C]` or `[O]` (`SEAM.SIMPLECURRENT.GENERATOR.01`, `TFPT4D.LATTICE.ACTION.01`, `PRED.JOINTLIKELIHOOD.01`).

## 1. The two-line theory

The compiler starts from exactly two declared inputs,
\[
c_3=\frac{1}{8\pi},\qquad g_{\rm car}=5,
\]
with \(c_3\) the seam normalization P1 and \(g_{\rm car}\) the five-slot carrier P2 (`AX.P1.01`, `AX.P2.01`). They are axioms in the ledger, even though each has substantial internal motivation and overdetermination; neither is newly derived by the 2026-08-28 work (`AX.P1.01`, `AX.P2.01`).

What changed today is the status of the architecture *downstream* of those inputs at the lattice level. The full census in `v993` takes rank eight, ADE type, and a cyclic order-four discriminant class on both factors as its premises, computes every relevant Smith normal form, and finds exactly one pair: \((D_5,A_3)\), with the raw \((D_5,D_3)\) duplicate removed by \(D_3\cong A_3\) (`v993_minimal_defect_selector.py`). Thus the earlier \(D_{d+1}\oplus A_{d-1}\) ansatz is no longer an input to the lattice census: within the stated premises, \(D_5\oplus A_3\) is `[E]`-selected (`v993_minimal_defect_selector.py`; `SEAM.SIMPLECURRENT.GENERATOR.01`).

The qualification is load-bearing. Rank eight comes from the cited minimal chiral premise \(c_-=8\), ADE-ness is assumed, and the passage from the order-four lift \(U^2=(-1)^F\) to cyclic \(\mathbb Z_4\) glue is a premise of the census; operator-algebraic minimality and uniqueness of the holomorphic \((E_8)_1\) theory are cited, not proved by `v993` (`v993_minimal_defect_selector.py`). P1 and P2 remain axioms, and the identification of the finite \(\mu_4\) average with the physical modular determinant-line response remains `[C]` (`AX.P1.01`, `AX.P2.01`).

Inside that firewall, the result is sharp: \(D_4\oplus D_4\) and \(A_7\oplus A_1\) have determinant product \(16\) but fail the cyclic order-four requirement, while \(E_6\oplus A_2\) is the explicit \(\mathbb Z_3\) control (`v993_minimal_defect_selector.py`). The isotropic index-four extension is even and unimodular of rank eight, hence is identified with \(E_8\) by the cited classification, while the coordinates, determinant, norms, and root census are `[E]` computations (`v983_simple_current_generator.py`). “Census-forced” therefore means exactly this: the rank-eight ADE lattice architecture is unique under the named order-four premises; it does not mean that the axioms, continuum net, four-dimensional world, or physical interpretation have been proved (`v993_minimal_defect_selector.py`; `QFT4D.OS.RECON.01`).

## 2. One object, four shadows

The simplest synthesis is that today’s four strongest finite results are four controlled shadows of one order-four organizing datum, not four unrelated mechanisms (`SEAM.SIMPLECURRENT.GENERATOR.01`, `ALPHA.QUILLEN.EXACT.01`).

1. **Boundary generator.** The seam candidate is the single class
   \(\lambda=(\omega_s,\omega_f)\), with \(\|\lambda\|^2=2\), conformal weight \(h_\lambda=1\), and order four in the diagonal \(\mathbb Z_4\subset\operatorname{disc}(D_5)\times\operatorname{disc}(A_3)\) (`v983_simple_current_generator.py`). Its strong operator limit is not claimed: the finite lattice generator is `[E]`, the quasi-free reduction is `[C]`, and the MMST/net identification remains `[O]` (`v988_psi_lambda_reduction.py`; `SEAM.SIMPLECURRENT.GENERATOR.01`).

2. **Deck grading.** The finite Quillen/BFK mismatch was a channel swap, not a normalization failure: the order-two deck shift \(r\mapsto r+2\) maps the jump spectrum \([0,2,4,2]\) to the absolute mark spectrum \([4,2,0,2]\), whereas an odd shift fails (`v985_quillen_channel_swap.py`). The graded determinant difference is exactly \(c_3\)-free, \(\log(\log 2/4)\), but KMS rigidity and continuum Bismut–Freed identification remain `[O]` (`v985_quillen_channel_swap.py`; `ALPHA.QUILLEN.EXACT.01`).

3. **Parity glue.** The order-four class satisfies \([\lambda]^2=[v]\) exactly in \(\operatorname{disc}(D_5)\), so its square is the vector/fermion-parity class, the finite lattice shadow of \(U^2=(-1)^F\) (`v993_minimal_defect_selector.py`). The order-two vector class cannot itself perform the glue because its norm \(7/4\) is not even (`v983_simple_current_generator.py`; `v993_minimal_defect_selector.py`).

4. **The 128 from one fusion orbit.** The four cosets contain \([52,64,60,64]\) norm-two vectors, and the two odd fusion powers carry \(64+64=128\), the entire spinor extension sector (`v983_simple_current_generator.py`). This is the precise finite sense in which one normalized order-four field replaces 128 independent choices; locality, energy bounds, braiding, and net-level Q-system closure are still the open analytic content (`SEAM.SIMPLECURRENT.GENERATOR.01`).

The \(\mu_4\) clock also has a dynamical shadow: a local collision unitary with an environment reproduces the Markov step exactly, while a closed unitary cannot reproduce its second iterate (`v984_markov_qca_dilation.py`). That result does not identify all five objects as one theorem, but it supports the disciplined reading: order-four grading organizes lattice glue, parity, determinant channels, boundary sectors, and reduced dynamics without adding a continuous fitting parameter (`v984_markov_qca_dilation.py`; `DYN.UNITARY.DILATION.01`).

## 3. The world-building ladder

Today’s decisive route clarification begins with a failure. The naive Euclidean overlap shortcut is reflection-positive at \(N_t=2\) but its determinant-only Gram becomes indefinite at \(N_t=4\), with \(\lambda_{\min}\simeq-0.249\); the pure-gauge and ultralocal Wilson controls stay positive, pinning the failure on overlap time nonlocality (`v989_lattice_gate_battery.py`). The result is exact at the tested finite sizes and kills that shortcut, not all chiral lattice constructions (`v989_lattice_gate_battery.py`; `CHIRAL4D.NOMIRROR.01`).

The Hamiltonian route clears the same positivity gate by construction: impose the Gauss-law Hilbert space, build a local Hermitian \(H\), and then \(T=e^{-aH}\) is positive; the finite model also carries the seam-sector intertwiner and the expected \(k=1,3\) \(\mu_4\) degeneracy (`v989_lattice_gate_battery.py`). This finite witness motivates the registered **Decision** `QFT4D.LATTICE.FUNDAMENTAL.01`: physical completeness is assigned to a finite, local, unitary lattice quantum theory, while an exact continuum Osterwalder–Schrader limit is mathematical reinforcement and remains `[O]` (`QFT4D.LATTICE.FUNDAMENTAL.01`, `QFT4D.OS.RECON.01`).

The dual rest formula prevents that decision from being mistaken for closure:
\[
\mathrm{Rest}_{\rm Compiler}=v_{\rm geo}\oplus G_{\rm net}\oplus F_{\rm transfer},
\]
where \(v_{\rm geo}\) is the irreducible dimensionful metrology unit `[O]`, the MMST route to \(G_{\rm net}\) is `[C]` closed modulo cited theorems while the unconditional parent stays `[O]`, and the four physical transfer interfaces remain `[O]` until derived from one theory (`v153`; `SEAM.EQUIV.MMST.01`; `SEAM.EQUIV.01`; `FTRANSFER.GENERATING.01`).

The stricter accounting is
\[
\begin{aligned}
\mathrm{Rest}_{\rm TOE}={}&\mathrm{SeamContinuum}\oplus\mathrm{4DAction}
\oplus\mathrm{ChiralMeasure}\oplus\mathrm{MirrorGap}\\
&\oplus\mathrm{UnitaryDynamics}\oplus\mathrm{IR/continuum}
\oplus\mathrm{BulkSeam}\oplus\mathrm{QuantumGravity}\\
&\oplus\mathrm{GeneratingFunctional}\oplus\mathrm{InitialState}.
\end{aligned}
\]
Its ten items currently read as follows (`QFT4D.LATTICE.FUNDAMENTAL.01`).

- **SeamContinuum:** lattice glue and the order-four generator are `[E]`, the quasi-free theorem reduction is `[C]`, and the MMST/net identification remains `[O]` (`v983_simple_current_generator.py`; `v988_psi_lambda_reduction.py`; `SEAM.EQUIV.MMST.01`).
- **4DAction:** anomaly, overlap, non-Gaussianity, and positivity mechanisms are `[E]` at finite toy level, but one explicit finite 4D TFPT action passing T1–T7 remains `[O]` (`v989_lattice_gate_battery.py`; `TFPT4D.LATTICE.ACTION.01`).
- **ChiralMeasure:** exact anomaly bookkeeping and a finite Gauss census are `[E]`; a local gauge-invariant chiral measure for the actual TFPT content remains `[O]` (`v989_lattice_gate_battery.py`; `CHIRAL4D.NOMIRROR.01`).
- **MirrorGap:** the 2D overlap index and Ginsparg–Wilson circle are `[E]` mechanisms, but mirror decoupling in the physical spectrum and its stable limit remain `[O]` (`v989_lattice_gate_battery.py`; `CHIRAL4D.NOMIRROR.01`).
- **UnitaryDynamics:** the collision dilation, kernel OS continuation, size-uniform free band, interacting congruence family, and quantum-coupled band are finite `[E]` witnesses; continuous interacting field reconstruction and branch selection remain `[O]` (`v984_markov_qca_dilation.py`; `v987_os_dilation_package.py`; `DYN.UNITARY.DILATION.01`).
- **IR/continuum:** the lattice-fundamental reading is a **Decision**, while clustering, uniform bounds, continuum limit, and Wightman/Haag–Kastler reconstruction remain `[O]` mathematical reinforcement (`QFT4D.LATTICE.FUNDAMENTAL.01`; `QFT4D.OS.RECON.01`).
- **BulkSeam:** bulk Chern number \(+1\) equals seam holonomy winding \(+1\) in the finite QWZ model `[E]`; the determinant-line isomorphism with connection and continuum Bismut–Freed theorem remain `[O]` (`v991_detline_bulk_edge.py`; `SEAM.DETLINE.UNIFICATION.01`).
- **QuantumGravity:** no module yet produces a massless transverse spin-two mode; that demand is `[O]`, and the existing Einstein-equation readout remains downstream and conditional (`GRAV.SPIN2.EMERGENCE.01`; `GRAV.NONCIRCULAR.01`).
- **GeneratingFunctional:** finite identities \(\partial_JW=\langle O\rangle\), Hessian \(=\) Kubo, and a nonzero mixed transduction channel are `[E]` witnesses, while one 4D \(W[J]\) generating all four transfer bridges remains `[O]` (`v990_wj_transduction_mechanism.py`; `FTRANSFER.GENERATING.01`).
- **InitialState:** the Schwinger–Keldysh pair \((S,\rho_0)\), its Euclidean cap, and KMS selection are `[O]`; \(\theta_i=3\pi/5\) with the \(k=0\) orientation is only the typed candidate (`FTRANSFER.SK.RHO0.01`).

## 4. The evidence, honestly counted

The first joint likelihood gives \(\chi^2=11.80\) for nine nominal degrees of freedom, \(\chi^2/{\rm dof}=1.31\), and \(p=0.225\), with leave-one-out values stable and TFPT at the zeroth percentile of 200 scrambled decoders (`v992_joint_likelihood_v1.py`). Its most important number is \(\nu_{\rm eff}=1\): the nine matches mostly probe one compiler-atom direction rather than nine independent successes, so the result explicitly rejects hit-counting (`v992_joint_likelihood_v1.py`; `PRED.JOINTLIKELIHOOD.01`). In the simplicity thesis this is a feature—one atom generates many overdetermined relations—but statistically it is also a warning that the evidence has only one effective direction; full covariance, a prespecified formula grammar, and genuine holdouts remain `[O]` (`PRED.JOINTLIKELIHOOD.01`).

The neutrino–scalaron candidate is comparably exposed. Its frozen v1 chain predicts \(\Sigma m_\nu=0.0600/0.0599\) eV against the dated DESI DR2 \(\Lambda\)CDM limit \(0.0642\) eV, leaving only about \(+0.004\) eV and a model-dependent posterior tension (`FLAV.NUSCALE.05`; `v986_nu_scalaron_rung.py`). The candidate dies if a robust bound falls below \(0.0599\) eV, if the required \(M_R\) moves by more than about five percent under the same premise chain, if inverted ordering is established, or if \(m_{\beta\beta}\) lies above the frozen normal-ordering interval; the v2 untextured \(Y_\nu\propto I\) option is already killed by its four-order-of-magnitude mass overshoot (`FLAV.NUSCALE.05`; `v986_nu_scalaron_rung.py`). JUNO mass splitting, DESI \(\Sigma m_\nu\), DUNE \(\delta_{\rm CP}\), and LiteBIRD \(r\) are declared holdouts rather than consumed confirmations (`v992_joint_likelihood_v1.py`; `PRED.JOINTLIKELIHOOD.01`).

## 5. What would kill it, and what would close it

- **MMST identification:** close it by proving that the controlled finite-collar implementers converge with the required energy/locality bounds to the \((E_8)_1\) extension; failure of convergence or relative locality kills the simple-current route (`v988_psi_lambda_reduction.py`; `SEAM.SIMPLECURRENT.GENERATOR.01`).
- **KMS rigidity:** close it with a continuum uniqueness theorem identifying the seam KMS state with the quasi-free determinant-line state; a surviving inequivalent normalized state kills the claimed rigidity (`ALPHA.QUILLEN.EXACT.01`; `SEAM.STATE.RPMIXING.01`).
- **Bismut–Freed:** close it by proving \(\operatorname{Res}_{\rm seam}\det D_{4D}\cong\det D_{\rm seam}\) as line bundles with connection and matching holonomy; an irremovable local mismatch kills the unification (`v991_detline_bulk_edge.py`; `SEAM.DETLINE.UNIFICATION.01`).
- **\(\alpha_s\) fixpoint:** close it with one nonabelian zeta-determinant functional having unique positive-Hessian stationary points for all three couplings and correct RG landing without measured \(\alpha_s(M_Z)\); failure of uniqueness, positivity, or RG landing kills it (`GAUGE.DETLINE.FIXPOINT.01`).
- **Neutrino texture:** close it with a frozen \(3\times3\) Dirac texture that preserves \(y_3=y_t\), reproduces masses and PMNS mixing, and survives the frozen kills; requiring fitted \(y_1,y_2\) leaves the mechanism `[O]` (`v986_nu_scalaron_rung.py`; `FLAV.NUSCALE.05`).
- **Spin two:** close it by deriving from the same determinant a massless two-helicity transverse pole with universal \(T_{\mu\nu}\) coupling, diffeomorphism Ward identities, and positive transfer; an extra longitudinal/massive mode or non-universal coupling kills it (`GRAV.SPIN2.EMERGENCE.01`).
- **Chiral measure:** close it with a local gauge-invariant Ginsparg–Wilson measure for the actual TFPT representations, global-anomaly freedom, correct index, and mirror decoupling; any unavoidable nonlocality, Witten anomaly, or surviving mirror kills the route (`v989_lattice_gate_battery.py`; `CHIRAL4D.NOMIRROR.01`).
- **SK/\(\rho_0\):** close it by deriving a KMS-consistent Euclidean cap that selects the \(3\pi/5\), \(k=0\) initial state from the same \(W[J]\); inconsistency with that \(W[J]\), another forced \(k\), or failed KMS kills the candidate (`FTRANSFER.SK.RHO0.01`).

## 6. The simplicity thesis, stated strictly

The falsifiable simplicity claim is: after the two declared dimensionless inputs P1 and P2 and the one unavoidable dimensionful unit \(v_{\rm geo}\), no normalized downstream observable may require an additional freely adjustable dimensionless parameter (`AX.P1.01`, `AX.P2.01`; `v153`; `TFPT4D.LATTICE.ACTION.01`). This is stronger than saying that formulas are short, and it is refuted if the 4D action, chiral sector, transfer functional, or initial state closes only after a new dial is introduced (`TFPT4D.LATTICE.ACTION.01`; `FTRANSFER.GENERATING.01`; `FTRANSFER.SK.RHO0.01`).

The discipline today was genuinely freeze-first where data or selection entered: the neutrino projects were pinned by SHA-16 `4941b396729636de` and `c912e95e91a247ac`, the likelihood was compared with 200 scrambled decoders, and the lattice architecture was selected by a full convention-controlled ADE census rather than by searching only the desired \(D{+}A\) family (`v986_nu_scalaron_rung.py`; `v992_joint_likelihood_v1.py`; `v993_minimal_defect_selector.py`). Those procedures do not prove the theory, but they sharply limit post-hoc freedom and expose negative results—the Euclidean overlap shortcut and the untextured neutrino operator were allowed to die (`v989_lattice_gate_battery.py`; `FLAV.NUSCALE.05`).

Two possible hiding places for a dial remain and must be named. First, \(y_\nu=y_t\) is a premise, not a derivation, and the first two entries of the Dirac texture are not frozen by the corpus; the scalaron rung is therefore `[C]` with mechanism `[O]`, not a closed neutrino theory (`v986_nu_scalaron_rung.py`; `FLAV.NUSCALE.05`). Second, \(\phi_{\rm seam}\) is fixed in the executed formulas, but the from-first-principles provenance of its modulus response as the exact continuum Quillen/KMS determinant-line functional remains `[O]`; until that identification is proved, hidden normalization or modulus freedom has not been excluded (`v341_alpha_quillen.py`; `v985_quillen_channel_swap.py`; `ALPHA.QUILLEN.EXACT.01`).

That is the evening verdict: the finite compiler has become simpler because an exhaustive census and four order-four shadows replaced several architectural choices, while the physical theory has become harder to overstate because every surviving gap now has a name, a status, and a decisive landing test (`v983_simple_current_generator.py`–`v993_minimal_defect_selector.py`; `QFT4D.LATTICE.FUNDAMENTAL.01`).
