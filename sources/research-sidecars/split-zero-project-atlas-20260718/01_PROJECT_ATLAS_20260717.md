---
title: "Split-Zero Geometry and Common Deformation Registers"
subtitle: "Project atlas, exact results, formal checks, and visual work"
author:
  - "The Clankers"
date: "18 July 2026"
lang: en-GB
geometry: margin=20mm
fontsize: 10pt
colorlinks: true
linkcolor: teal
urlcolor: teal
toc: true
toc-depth: 2
numbersections: true
header-includes:
  - |
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhf{}
    \lhead{Split-Zero Geometry and Common Deformation Registers}
    \rhead{Project Atlas}
    \cfoot{\thepage}
    \setlength{\headheight}{14pt}
---

# Read this first

This record is the public home for a continuing mathematics project at the
intersection of explicit arithmetic registers, the Erdos--Strauss research
programme, split-zero and tagged-sedenion models, finite moonshine and
$\widehat Z$ calculations, and exact geometric experiments. It is organised as
a working mathematical library, not as a sequence of announcements.

The concept DOI is **[10.5281/zenodo.20822444](https://doi.org/10.5281/zenodo.20822444)**.
It resolves to the latest version. New releases belong to this concept and do
not create a second project page.

The public surface has three layers:

1. This atlas states what is established, what is generated, what has been
   obstructed, and what is genuinely open.
2. The results compendium contains the complete current packets, including
   formulae, finite tables, proof statements, and source boundaries.
3. The ZIP archives preserve Lean, Python, ledgers, data, editable visual
   sources, and machine-readable text. They are evidence and replay material,
   not the front door.

No JT-authored corpus dump is included. Jacolm Tobley (JT) remains credited as
a researcher and project relationship. Direct source material remains under
its own provenance and ownership. The public payload consists of work supplied
by the repository maintainer, generated project mathematics, exact checks, and
rights-screened derivatives. The release licence is CC BY 4.0; third-party
literature keeps its original copyright and is cited rather than republished.

## File map

| File | Use it for |
|---|---|
| `00_PROJECT_ATLAS_20260717.pdf` | Human front door, mathematical map, status boundaries, and reading routes. |
| `01_PROJECT_ATLAS_20260717.md` | Searchable and reusable source of the atlas. |
| `02_CURRENT_RESULTS_COMPENDIUM_20260717.pdf` | Complete current result packets with bookmarks and a contents index. |
| `03_FORMALIZATION_AND_EXACT_CHECKS_20260717.zip` | Lean sources, Python checkers, ledgers, build/audit logs, and replay guide. |
| `04_VISUAL_ATLAS_20260717.pdf` | Selected exact and explanatory visual results. |
| `05_VISUALIZATIONS_AND_DATA_20260717.zip` | Editable visual sources, scene data, GeoGebra/HTML assets, renders, and QA. |
| `06_CURRENT_WORKING_TEXTS_20260717.zip` | TeX, Markdown, plain text, and per-packet machine extracts. |
| `README.md` | Short navigation and citation instructions. |
| `CHANGELOG.md` | Version history and material changes. |
| `PROVENANCE_AND_RIGHTS.md` | Inclusion, exclusion, credit, and reuse rules. |
| `MANIFEST.json` / `SHA256SUMS.txt` | Machine-readable inventory and integrity checks. |

## Status vocabulary

The record uses the following labels literally.

| Label | Meaning |
|---|---|
| **Exact theorem** | A finite or symbolic statement proved in Lean, or an exact calculation replayed independently with a complete finite certificate. |
| **Checked calculation** | A reproducible calculation whose stated finite or bounded scope has been replayed. |
| **Generated construction** | A mathematically exact object built by the project, but not recovered as the unique or source-defined object. |
| **Obstruction / no-go** | A tested candidate map or identification fails for an explicit reason or counterexample. |
| **Diagnostic** | A deliberately artificial or degenerate model used to expose an underconstrained interface. |
| **Evidence-backed open problem** | A positive pattern survives nontrivial checks, but a named proof, source, or naturality step remains missing. |
| **Investigation prompt** | A similarity worth testing. It is not a conjecture and carries no assertion of truth. |
| **Historical exploration** | Preserved provenance that is superseded, false, under-specified, or no longer part of the current result surface. |

A statement is not promoted to a conjecture merely because it appeared in a
conversation or because a user gestured toward it. Conditional statements
invented to avoid saying that a proposed map is false are excluded from the
current result surface. Failed maps are recorded as failed maps.

# Arithmetic register and the Gamma-107 chain

The clearest new theorem-level chain begins with a finite arithmetic register
and ends with an exact generated order-six target model. The complete Lean
statements are exposed through
`FiniteRegisterGamma107PublicFacade.lean`; the implementation tables and
replay evidence are in the formalization archive.

## The 48-state register

Let $U_{24}$ denote the unit classes modulo $24$. The checked character map

$$
\Phi:U_{24}\longrightarrow \mathbf F_2^3
$$

is bijective and multiplicative. The six accepted conductor faces are
represented by

$$
S_{840}=\{1,121,169,289,361,529\}.
$$

The accepted square-support register
$G_{840}^{\square 35}$ has exactly $48$ elements and decomposes as an explicit
product of an eight-element ground-character register with a six-sector
coordinate. Its square-class map has the checked kernel described in Packet
129.

**Public theorem:** `acceptedFiniteRegisterIsComplete`.

**Status:** exact finite theorem. The public alias uses standard Lean
`propext`; it uses no native evaluator axiom.

## Tagged sedenion preflight

The target preflight uses a 32-basis tagged algebra with multiplication modelled
as $A_4\otimes \mathbf R[C_2]$. The packet checks the basis product, the
cross-polarised zero-divisor pairs, the quartet squares and associators, and the
block data of the displayed operator $\Gamma_{107}$.

The exact block dimensions are

$$
\dim V_0=8,\qquad \dim V_2=16,\qquad \dim V_4=8,
$$

with characteristic and minimal polynomials

$$
\chi_{\Gamma_{107}}(x)=x^8(x^2+4)^8(x^2+16)^4,
\qquad
m_{\Gamma_{107}}(x)=x(x^2+4)(x^2+16).
$$

**Public theorem:** `gamma107BlockDecomposition`.

**Status:** exact finite theorem. This is a checked algebraic model, not an
authorship claim about the source corpus.

## Sector 289 and the unnormalised no-go theorem

Multiplication by $289$ on the 48-state register produces eight disjoint
six-cycles. On the target, the sixth power of the unnormalised operator has
diagonal scale factors

$$
0 \text{ on } V_0,\qquad -64 \text{ on } V_2,
\qquad -4096 \text{ on } V_4.
$$

No nonzero vector is fixed. Therefore an exact intertwiner from the tested
period-six source action to the unnormalised $\Gamma_{107}$ action must vanish.

**Public theorems:** `sector289ActsByEightSixCycles` and
`unnormalisedGamma107Sector289NoGo`.

**Status:** exact obstruction. It rules out this unnormalised target action; it
does not rule out a normalised, projective, rescaled, or exponential action.

## The kernel-collapse diagnostic

An artificial action can be made equivariant by forcing its image into the
kernel of $\Gamma_{107}$. The resulting code can still be injective at the
finite interface level. This proves that the old bridge specification was too
weak: interface inhabitance did not exclude a mathematically degenerate model.

**Public theorem:** `degenerateKernelBridgeDiagnostic`.

**Status:** diagnostic counterexample. It is not a candidate bridge, not a
source result, and not evidence for the desired naturality.

## Generated exponential order-six repair

Write $G=\Gamma_{107}$ and define the spectral projectors

$$
P_0=\frac{(G^2+4I)(G^2+16I)}{64},\qquad
P_2=-\frac{G^2(G^2+16I)}{48},\qquad
P_4=\frac{G^2(G^2+4I)}{192}.
$$

The generated target step is

$$
E=P_0+\left(\frac12P_2+\frac{\sqrt3}{4}GP_2\right)
-\frac12P_4+\frac{\sqrt3}{8}GP_4.
$$

Exact arithmetic gives

$$
E^6=I,\qquad E^k\ne I\ (1\le k<6),\qquad
\chi_E(t)=(t-1)^8(t^2-t+1)^8(t^2+t+1)^4.
$$

The project constructs 48 distinct nonzero target codes with exact
equivariance, a checked alternating parity reader, and a fixed provenance
reader. On a frequency-two plane the six phases are the exact
$\mathbf Q(\sqrt3)$ hexagon

$$
(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1),
$$

under the pair update

$$
(a,b)\longmapsto \left(\frac{a-3b}{2},\frac{a+b}{2}\right).
$$

**Public theorem:** `generatedExponentialC6Repair`.

**Status:** exact generated construction. The finite phase model is proved;
the analytic exponential motivation is checked separately. No source-defined
normalisation or source-natural bridge has been recovered.

**Genuine open problem:** `SourceNaturalNondegenerateBridgeExists` asks for a
nonzero bridge for an externally supplied source action. The proposition is
defined but not inhabited.

# Moonshine, E8 cubed, and Sigma(2,3,5)

The second main body of work compares exact $q$-series and finite module data
between an $E_8^3$ umbral-moonshine surface and sectors associated with
$-\Sigma(2,3,5)$. The compendium preserves the source crosswalk in Packet 76
and the complete sequence of Packets 77--108 and 115--120 because the negative
results are as important as the surviving equalities.

## Exact common output series

The project identifies exact shared coefficient series $\chi_0$ and $\chi_1$
at the displayed output level. Named endpoint pullbacks and finite labels make
the comparison explicit and reproducible.

**Status:** checked common output data. Equality of displayed series does not
imply an isomorphism of modules, manifolds, defects, or vertex-algebra objects.

## Internal-morphism boundary

The source-backed cone-VOA construction supplies a rigorous method dependency,
but the displayed ranks, symmetry actions, topology, and internal carriers are
not the same. A Lean countermodel shows that agreement of selected traces does
not force an internal object morphism.

**Status:** exact logical obstruction to the inference; no internal morphism
has been extracted.

## Sigma(2,3,5) W1 finite structure

The checked finite surface includes:

- exact no-defect and component-7 alpha tables and admissibility tests;
- 30 end-node classes with explicit component fibres;
- exact trace aggregation and signs;
- an obstruction to a canonical residue action from representative-dependent
  $S_3$ transports;
- vanishing off-diagonal Hom spaces from disjoint momentum support;
- the intrinsic endomorphism algebra $\mathbf C\times\mathbf C$ on the two
  signed summands;
- exactly four intrinsic sign-pair $S_3$ actions, all nonfaithful;
- a separate four-dimensional multiplicity factor that creates nine $S_3$
  types, four faithful, while remaining an added tensor factor rather than a
  source-intrinsic symmetry.

The generated family carrier and vertex-mode actions are finite algebraic
shadows. They are not a construction of the full VOA.

## Analytic and topological checks

Within their stated bounded or source-backed scopes, the following are
checked:

- positivity and finite energy shells;
- rank-two oscillator grades and combined lattice--oscillator $L_0$ grades;
- finite diagonal traces and a nonzero $g_b$ phase;
- twisted-module closure and the analytic trace envelope;
- prefactor/component consistency;
- an executable W1/Habiro recomputation showing that the manuscript token
  `H5` is a source-label defect and that the executable component is `H7`;
- the weakly negative plumbing prefactor
  $C_\Gamma=-q^{-5/4}$;
- unnormalised regularised totals
  $F_{000}=-\eta H_1$ and $F_{001}=-\eta H_7$;
- a calibrated orientation-reverse representative with a mandatory finite
  correction.

The physical Wilson half-index identification remains open. In the visual
atlas it is deliberately marked by a dashed `?=` rather than converted into a
claim.

# Mixed support and the K=4 raise

The newest exact bridge begins with the regularised indefinite-theta factor in
*3d Modularity Revisited*. Away from its two cone boundaries, write

$$
\epsilon_j(n)=\operatorname{sgn}B(c_j,n)\in\{-1,+1\}.
$$

The pair $(\epsilon_1,\epsilon_2)$ is a Klein four sign register under
coordinatewise multiplication. The cone-support factor is exactly

$$
\frac12|\epsilon_1-\epsilon_2|
=\frac{1-\epsilon_1\epsilon_2}{2}.
$$

It is the XOR indicator: one on the two mixed-sign faces and zero on the two
synchronised faces. This is an exact finite theorem, not a resemblance between
two fourfold pictures.

## Source-enriched selection of the second boundary

For the $6-1=5$ member of the source family, the displayed data are

$$
A=\begin{pmatrix}-60&0\\0&3\end{pmatrix},\qquad
c_1=(1,0),\qquad c_2=(3,10).
$$

Exact integer arithmetic gives

$$
B(c_1,c_1)=-60,\quad B(c_2,c_2)=-240,\quad B(c_1,c_2)=-180.
$$

The two primitive vectors therefore lie in the same negative-cone component.
Their primitive perpendicular directions $(0,1)$ and $(1,6)$ have positive
norms $3$ and $48$. Packet 198 proves this support skeleton but, using only
$A$ and $c_1$, correctly finds five source-form candidate rays.

Packet 200 retains the full ordered source datum

$$
A=\operatorname{diag}(-2p\bar p,x),\qquad d_2=(1,\bar p),
\qquad \bar p x>2p.
$$

If $g=\gcd(x,2p)$, the unique positive primitive integer generator of the
$A$-orthogonal line $d_2^\perp$ is

$$
c_2^{\mathrm{prim}}=\left(\frac{x}{g},\frac{2p}{g}\right).
$$

The source vector $(x,2p)$ is its positive $g$-fold multiple. Thus the full
ordered cone datum canonically selects the projective $c_2$ ray. For the
ordered Brieskorn data $(p_1,p_2,p_3)=(2,3,5)$, one has
$p=5$, $\bar p=6$, $x=3$, and hence $c_2=(3,10)$. The exact odd projector is

$$
P_{c_2}=\begin{pmatrix}9/4&-3/8\\15/2&-5/4\end{pmatrix},
$$

with kernel $\mathbb R(1,6)$ and image $\mathbb R(3,10)$. It is idempotent,
$A$-self-adjoint, and natural under exact bilinear coordinate changes.

There is also a source-scope correction and an exact follow-up. The paper
states a broader $-\Sigma(2,3,6\pm1)$ cancellation, but the cited lemma
directly assumes an $L=4$ case. At $x=3$ those hypotheses cover a
$\Sigma(2,3,7)$-type ordering, not the displayed $L=8$ $\Sigma(2,3,5)$
datum. Packet 202 independently reconstructs the displayed no-defect $j=2$
aggregate and isolates the unique coefficient

$$
[q^{1/120}\bar q^{1/24}]\,\mathcal S^{(2)}_{235}
=2\exp(2\pi i/12)\ne0.
$$

The displayed no-defect aggregate therefore does not cancel. The pointwise
$c_2$ support and source-enriched selector remain exact; all-sector and full
$j=1+j=2$ shadow questions remain open.

**Status:** exact XOR support theorem, exact source-enriched projective
selector, exact arithmetic projector, and exact no-defect $j=2$
noncancellation. No all-sector/full-shadow theorem, Jordan-algebra morphism,
or physical half-index theorem is asserted.

## Blind planes, ternary recovery, and the sphere

The project already contains exact finite models for the higher operation
that motivated this comparison. In the two-weight model
$W=\mathbb C_G\oplus\mathbb C_C$, the admissible equivariant cross-Hom spaces
vanish: each complex plane is invisible to the other under the specified
lower observer. In the shared-unit algebra $J_\kappa$, the mixed binary product
vanishes while the ternary associator recovers the hidden factor. The
obstruction is not discarded; it becomes operation data at the next rung.

On the centred zeta sphere, the critical great circle is $X=0$ and

$$
X_s=\frac{c_{-+}}{1+|2s-1|^2},\qquad
c_{-+}=2(2\operatorname{Re}s-1).
$$

Thus $X$ is the compactified amplitude of the existing $(-,+)$ violation
sector. A zero amplitude does not delete the support channel from the K=4
datum. The sphere is a geometric compactification of the complementary
coordinate that a lower on-circle register cannot express internally.

Two different Klein four-groups act on this sphere: the holomorphic coordinate
half-turn group and the classical zeta-zero reflection group. The current
audit separates them. The zero quartet belongs to the latter; no conflation is
used in the bridge above.

Inside this project, the "impossible extension" is the recursive predatum move
to a higher obstruction language: a lower null relation or invisible support
becomes a coordinate of the next stratum. The exact sign-register theorem
supplies an external mixed-modular target, and the ordered source datum now
selects its projective boundary ray. What remains open is a typed,
algebra-valued natural map from the predatum/associator object to this
arithmetic projector, together with all-sector/full-shadow and physical
half-index checks.

The public formal archive also contains a rights-safe K-ladder charter
integration. It preserves the intended shifted-rung vocabulary, zero-operator
reading, and predatum test shape as project architecture, not as proved
theorems. It explicitly separates the componentwise-XOR four-state register
from the $C_2$ multiplicative unit subgroup and queues the missing typed
intertwiner, the Hopf/no-global-section candidate, and a rung-by-rung
dimension audit.

## Cowlicks, sedenion annihilators, and coordinate half-turns

Packet 201 separates a useful topological ladder into its actual theorem
levels. The classical Poincare-Hopf theorem forces a zero for every continuous
tangent field on an even sphere. Bott-Milnor and Kervaire classify the
positive-dimensional parallelizable spheres as $S^1,S^3,S^7$, and Adams gives
the optimal number of independent tangent fields on every sphere. Those are
cited external theorems.

The new project calculation is finite and fully replayable. In the audited
Cayley-Dickson convention, every imaginary basis left-action matrix is skew
and orthogonal in dimensions $2,4,8,16$. The complete multiplication-frame
identity holds in dimensions $2,4,8$ and fails in dimension 16. For the
selected sedenion zero divisor

$$
u=e_3+e_{10},
$$

the exact matrix $L_u$ has rank 12 and kernel

$$
\langle-e_5+e_{12},\ e_4+e_{13},\ e_7+e_{14},\ -e_6+e_{15}\rangle.
$$

Thus the selected tangent field $x\mapsto ux$ on $S^{15}$ vanishes on an
$S^3$. This is not a claim that every field on the odd sphere must vanish or
that this one example exhausts non-parallelizability.

On the centred compactified $s$-plane, the identity and three coordinate
half-turns form $K_4$. The selected $x$-axis rotation field has zeros
$\Sigma(0)$ and $\Sigma(1)$, each of local index $+1$; among the three
coordinate-axis fields, only that pair lies off the critical great circle
$X=0$. Hairy-ball does not force exactly two zeros, the Radon-Hurwitz value is
$\rho(16)=9$ rather than 8, and no typed map identifies Adams's maximum of
eight fields with a separate eight-dimensional ghost kernel.

**Status:** exact universal matrix identities, exact selected annihilator,
exact coordinate $K_4$ and local-index calculation; classical topology cited;
cross-program ghost/predatum/modular identifications open.

# Residual Niemeier lattice certificate

The public Part 8-C2B audit starts with the displayed marked glue subgroup of
order 72 in the discriminant module of the root lattice $A_5^4D_4$. A
source-free exact checker reconstructs an explicit index-72 extension basis
and verifies that its $24\times24$ Gram matrix is integral, even, positive
definite, and of determinant one. It then enumerates every glue class. The
complete minimum distribution is one class at norm 0, 46 classes at norm 4,
and 25 classes at norm 6. In particular, no nonzero class contributes a
norm-2 vector.

It follows that the extension is an even unimodular rank-24 lattice whose root
system is exactly $A_5^4D_4$. The final statement is

$$
N_{\mathrm{ES}}\cong N(A_5^4D_4),
$$

where $\cong$ means lattice isometry. The passage from the checked root system
to the named Niemeier lattice uses the standard classification and uniqueness
of rootful Niemeier lattices; it is not a literal equality of independently
defined constructions. The public reference is Cheng, Duncan, and Harvey,
[*Umbral Moonshine and the Niemeier Lattices*](https://arxiv.org/abs/1307.5793v2),
arXiv:1307.5793v2.

With the convention
$\Theta_L(\tau)=\sum_{x\in L}q^{(x,x)/2}$, the independently checked initial
coefficients and the standard weight-12 theta-modularity theorem give

$$
\Theta_{N_{\mathrm{ES}}}=E_4^3-576\Delta,
\qquad
\frac{\Theta_{N_{\mathrm{ES}}}}{\Delta}=J+168.
$$

The finite coefficient arithmetic is replayed in the checker; identifying it
as the full lattice theta series retains the standard even-unimodular
theta-modularity theorem. The source's alternate $q^{(x,x)}$ convention is
recorded as a rescaling, not a discrepancy.

Finally, Scaduto's definition and theorem specialize arithmetically to
$\delta(N_{\mathrm{ES}})=3$ and $g_4(N_{\mathrm{ES}})\ge5$. This is a
literature-dependent statement about Scaduto's geometric 4-genus, not an
independently formalized gauge-theory theorem or an unrestricted topological
non-realizability result. The primary citation is C. Scaduto,
[*Niemeier lattices, smooth 4-manifolds and instantons*](https://doi.org/10.1007/s00208-020-02060-y),
Math. Ann. 379 (2021), 549--568.

The level-six eta-quotient/$R=107$ compatibility sentence is not rechecked in
this audit, and “instanton-sensitive datum” remains interpretive context rather
than a theorem. The facade, TeX, 19-check source-free checker, replay ledger,
status row, and boundary ledger travel together in
`audits/branch32a_part8c2b/repository/`, with their original relative paths
preserved for unchanged replay. No raw Branch32-A source, copied literature,
private run material, direct JT witness, or JT theorem entry is included.

**Status:** exact finite lattice and no-new-roots certificate; Niemeier
classification, theta modularity, and geometric 4-genus theorem explicitly
literature-dependent; level-six and interpretive cross-program claims bounded.

# Descartes and split-zero geometry

Circle and Descartes geometry is secondary to the arithmetic and moonshine
work in this release, but it supplies a useful exact geometric laboratory.

Packet 122 establishes a field-closure audit for the selected Descartes
construction. Packet 123 supplies a reproducible $D_3$ orbit dataset with
exact circle data and independent render coordinates. The visual archive
contains the editable dataset, checker, GeoGebra companion, and depth-reveal
assets. The depth-reveal family was rerendered in readability revision R2:
larger high-contrast panel text, no clipped labels at 1920 x 1080, and an
explicit 960 x 540 scaled-view gate. Its rebuilt storyboard, MP4, Blender
scene, manifest, and handoff ZIP pass 22/22 checks.

**Status:** exact finite dataset and generated visualisation. No statement
about an unbounded orbit or all source images follows from the selected depth.

The split-zero project title should be read as a research programme rather
than a claim that every construction belongs to one completed axiomatic
framework. Its most useful current role is to organise common deformation
registers, complementary nullity conditions, and explicit failed or surviving
maps.

# Formal trust surface

The public Lean facade is intentionally small. It names the mathematical
dependency chain without forcing readers to parse large enumeration tables.
The complete formal archive contains the implementation modules, independent
Python checkers, JSONL ledgers, and build logs.

The 17 July 2026 combined audit checks 31 theorem surfaces: 25 underlying
statements and six readable facade aliases. Twenty-two report no axioms. Nine
use only the standard Lean axioms `propext` and/or `Quot.sound`. No audited
theorem depends on `native_decide` or a native code-generation axiom. The full
Lake build completes successfully.

This is not advertised as globally axiom-free. The precise axiom footprint is
included so that a reader can decide which proof paths meet their own trust
requirements.

The central public aliases have the following footprint:

| Alias | Lean reports |
|---|---|
| `acceptedFiniteRegisterIsComplete` | `propext` |
| `gamma107BlockDecomposition` | none |
| `sector289ActsByEightSixCycles` | none |
| `unnormalisedGamma107Sector289NoGo` | `propext`, `Quot.sound` |
| `degenerateKernelBridgeDiagnostic` | `propext`, `Quot.sound` |
| `generatedExponentialC6Repair` | none |

# What is not asserted

The present record does not assert any of the following:

- that matching $q$-series determine an internal moonshine/manifold morphism;
- that the unnormalised $\Gamma_{107}$ is a six-step permutation action;
- that the generated exponential action is source-selected or unique;
- that the kernel-collapse diagnostic is a satisfactory bridge;
- that a finite carrier or mode table is a full VOA;
- that the two Klein-four actions on the centred zeta sphere are the same;
- that the K4/XOR support theorem alone selects $c_2=(3,10)$;
- that the displayed no-defect $L=8$, $j=2$ $\Sigma(2,3,5)$ aggregate
  cancels (Packet 202 proves that it is nonzero);
- that Packet 202's no-defect coefficient classifies every Wilson sector or
  the full $j=1+j=2$ shadow;
- that any shadow simplification makes the second cone boundary dispensable;
- that the predatum support bridge proves a Wilson/half-index equality;
- that hairy-ball forces exactly two zeros or that $S^{15}$ has no
  nonvanishing tangent field;
- that Adams's maximum of eight fields is identified with the ghost-kernel
  dimension without a typed map;
- that the residual-lattice construction is literally equal to a separately
  defined Niemeier lattice rather than isometric to it by classification;
- that the Part 8-C2B audit proves level-six/$R=107$ compatibility or promotes
  “instanton-sensitive datum” beyond interpretive context;
- that the arithmetic specialization $g_4\ge5$ replaces Scaduto's cited
  geometric theorem and definition;
- that a bounded Descartes dataset proves an all-depth theorem;
- that conversational similarities are conjectures;
- that JT-authored source material is owned by, or relicensed through, this
  record.

# Open research programme

The following questions survive the current checks and are stated because
there is positive mathematical content behind them.

## Source-natural exponential bridge

Can an external source action and a natural normalisation select a
nondegenerate bridge compatible with the exact 48-state register? The generated
$E$ model proves finite feasibility, while the unnormalised no-go theorem and
kernel diagnostic sharply constrain an acceptable answer.

## Internal object relation behind common series

What additional structure, beyond equality of selected output traces, could
support a genuine relation between the $E_8^3$ moonshine object and the
$\Sigma(2,3,5)$ sector? The current result is an output-level equality plus an
obstruction to inferring an internal map for free.

## Predatum and complementary nullity

The project now has exact local models for the recursive operation: vanishing
cross-Hom spaces between two weighted complex planes, a Hopf quotient with no
global section, binary-null but ternary-recoverable mixed directions, a K=4
support register, and the XOR cone selector above. Together they establish a
coherent finite mechanism in which a lower impossibility becomes a coordinate
or operation datum of the next stratum.

The source-enriched arithmetic datum now selects $[c_2]$ and supplies a
coordinate-natural odd projector. The global architecture remains open:
Packet 199 finds standard Jordan, normal/conormal, affine, scheme-theoretic,
operator-algebraic, and $\mathbf F_1$-adjacent constructions, but no natural
algebra-valued morphism from the predatum/associator object to the arithmetic
projector. The right status is therefore theorem-level local mechanism,
source-enriched projective selector, and open cross-theory intertwiner.

# Related Zenodo records

Earlier records remain useful as citable, versioned studies. They are not
duplicated wholesale in this release.

| Topic | Cite-all-versions DOI | Current role |
|---|---|---|
| Split-zero/common deformation project | [10.5281/zenodo.20822444](https://doi.org/10.5281/zenodo.20822444) | Canonical public home; this record. |
| Full divisor locks | [10.5281/zenodo.20207306](https://doi.org/10.5281/zenodo.20207306) | Prior Erdos--Strauss divisor-lock work. |
| Odd $n$-line work | [10.5281/zenodo.20208683](https://doi.org/10.5281/zenodo.20208683) | Prior ES line decomposition. |
| Residual cubic support | [10.5281/zenodo.20401937](https://doi.org/10.5281/zenodo.20401937) | Prior residual-support calculation. |
| Mixed mock Virasoro | [10.5281/zenodo.20451738](https://doi.org/10.5281/zenodo.20451738) | Prior moonshine/modular study. |
| Rank-fifteen/Ogg study | [10.5281/zenodo.20217934](https://doi.org/10.5281/zenodo.20217934) | Related finite/moonshine study. |
| Sedenion ghost study | [10.5281/zenodo.20033645](https://doi.org/10.5281/zenodo.20033645) | Historical precursor to the checked target preflight. |
| Constructive terminal algebra | [10.5281/zenodo.20376531](https://doi.org/10.5281/zenodo.20376531) | Historical exploration; not the current project home and not relied on as a present theorem surface. |

# Credit and citation

The project combines conceptual direction, source discovery, generated
formalisation, exact computation, and visual explanation. The public record
credits Jacolm Tobley as a researcher/project relationship without transferring
ownership of JT-authored material. Generated model prose is never stored as JT
verbatim.

For the evolving project, cite the concept DOI:

> The Clankers, *Split-Zero Geometry and Common Deformation Registers:
> Project Atlas, Exact Results, Formalization, and Visualizations*,
> Zenodo, 2026. <https://doi.org/10.5281/zenodo.20822444>.

For a fixed computational state, cite the version DOI shown on the Zenodo
landing page together with the relevant stable theorem, packet, or certificate
ID.
