# EGA pre-Stacks machine-readable indexing scaffold

Date: 2026-08-02

Status: controlling design rule for EGA source/translation production.

## Purpose

EGA indexing must be richer than clickable-reference plumbing. The French and
English editions should expose a stable, machine-readable mathematical
scaffold from which later Stacks-style exposition, multilingual editions,
search, dependency exploration, and selected formalization can proceed without
re-parsing the books from scratch.

This is preparatory structure, not a claim that EGA has already been rewritten
in Stacks form or formalized in Lean.

## Canonical hub

The diplomatic French source is the immutable textual authority layer. The
English edition, later natural-language editions, Interslavic/Romance or other
terminology projects, and future formalization records attach to the same
stable semantic IDs. No later language should independently invent a second
mathematical object graph for the same source unit.

## Required node classes

At cumulative indexing checkpoints, record at least:

1. volumes, chapters, sections, numbered paragraphs, and unnumbered source
   units;
2. definitions, conventions, remarks, examples, propositions, lemmas,
   corollaries, theorems, and proof bodies;
3. displayed and semantically referenced formulas, exact sequences,
   commutative diagrams, tables, and source notes;
4. named objects and constructions where they are introduced;
5. hypotheses, conclusions, and scope/parent relationships when these can be
   stated without interpretive invention;
6. internal dependencies and citations, distinguishing proof-use,
   definition-use, comparison, forward pointer, range, and external-work
   citation;
7. source-error, English-normalization, reversal, and erratum decision IDs;
8. terminology/notation correspondences needed for later multilingual reuse.

## Minimum machine fields

The CSV/JSONL representation should support, as applicable:

- `stable_id`, `volume`, `source_number`, `kind`, `parent_id`;
- printed page, source-PDF page, TeX path, and explicitly named coordinate
  basis;
- French exact-source locator/slice hash and English target locator;
- visible title or locator, declaration/reference role, and statement status;
- hypothesis IDs, conclusion/statement ID, and dependency edge type;
- formula/diagram ID and notation/glossary bindings;
- correction/normalization/reversal IDs and current/superseded state;
- cross-volume/external scope and unresolved/ambiguous disposition;
- provenance, review method, and confidence without promoting OCR guesses.

Line/byte coordinates are generation-specific. Stable semantic IDs must not be
derived solely from mutable line numbers.

## Production timing

- During source-first French/English work, capture stable identities, semantic
  kinds, parents, obvious introductions, formulas/diagrams, and explicit
  dependency pointers when doing so is cheap and source-certain.
- Do not interrupt continuous transcription for exhaustive proof
  decomposition or speculative ontology work.
- At cumulative reader checkpoints, regenerate the complete target/edge/
  residual graph against the final TeX/PDF coordinates and run the exhaustive
  reference audit.
- After the canonical French/English layer freezes, deepen the graph into a
  Stacks-style reconstruction and attach additional languages to the existing
  IDs.

## Fidelity and restraint

The scaffold never licenses silent correction of diplomatic French, silent
promotion of OCR/extraction guesses, or invented hypotheses/dependencies.
Ambiguity remains explicit. English departures and all later reversals stay
individually justified in the project logbooks.

## Release custody

The final machine-readable scaffold, schema notes, decision/reversal ledgers,
and production logbooks are provenance artifacts. Bind privacy-clean versions
into both the methodology concept DOI `10.5281/zenodo.21124403` and the
replication concept DOI `10.5281/zenodo.20461174`, in addition to any reader
package in which they are directly useful.

## Incremental EGA I p.107 scaffold

The following source-certain nodes are available from the diplomatic p.107
pass. These are semantic anchors, not final PDF coordinates or an exhaustive
edge inventory.

- `I.3.2.6.3-fr`: lemma; parent theorem `I.3.2.6-fr`; concept = gluing local
  products along canonical overlap isomorphisms. Explicit dependencies:
  `I.3.2.6.1-fr` for restriction to overlaps, `I.2.3.1-fr` for gluing, and
  `I.3.2.6.2-fr` for the final product criterion. Formula roles include the
  overlap isomorphism `f_{ij}=h_{ij}\circ h_{ji}^{-1}` and cocycle identity
  `f_{ik}=f_{ij}\circ f_{jk}`.
- `I.3.2.6.4-fr`: lemma; parent theorem `I.3.2.6-fr`; concept = locality of
  product existence over an open cover of the base. Explicit dependencies:
  `I.3.2.6.3-fr` and `I.3.2.6.1-fr`.
- `I.3.2.6.5-fr`: proof-step node, incomplete at the p.107 seam; parent
  theorem `I.3.2.6-fr`; concept = existence of products over an affine base
  followed by descent across an affine open cover. Current explicit
  dependencies: `I.3.2.2-fr` and `I.3.2.6.3-fr`; the same node continues on
  p.108 and must not be treated as statement-complete yet.

English correction `EG-EGA-I-P107-EN-3263-CITATION-PLACEMENT-001` binds the
3.2.6.1 citation to the product-structure assertion rather than the preceding
inverse-image equality. This is a logical-attribution repair with no new
mathematical edge. Final candidate/edge/residual coordinates remain deferred
to a stable cumulative source/PDF generation.

## Incremental EGA I p.108 scaffold

These are source-certain semantic nodes and dependencies from the diplomatic
p.108 pass. They are not final PDF coordinates or an exhaustive graph.

- `I.3.2.6.5-fr`: prior incomplete proof-step node is now statement-complete.
  Added explicit dependencies `I.3.2.5-fr` and `I.3.2.6.4-fr` for the final
  descent from affine bases to an arbitrary base prescheme.
- `I.3.2.7-fr`: corollary; concept = restriction of a fiber product to open
  subpreschemes over an open part of the base. Explicit dependencies:
  `I.3.2.5-fr` and `I.3.2.6.1-fr`.
- `I.3.2.8-fr`: product/coproduct compatibility node; concept = distribution
  of fiber product over indexed coproducts. Explicit dependency:
  `I.3.2.6.3-fr`.
- `subsection:I.3.3-fr`: formal properties of products and change of base.
- `I.3.3.1-fr`: scope/portability node; the formal results apply in any
  category where the required products exist, except the specifically excluded
  later statements 3.3.13 and 3.3.15.
- `I.3.3.2-fr`: functoriality node; product is a covariant bifunctor in both
  variables. The native diagram records composable maps `f`, `f'` and their
  product maps with identities.
- `I.3.3.3-fr`: unit-product proposition; `X x_S S`, `S x_S X`, and `X` are
  canonically isomorphic.
- `I.3.3.4-fr`: projection-identification corollary; explicit dependency
  `I.3.3.3-fr`.
- `I.3.3.5-fr`: incomplete at the p.108 seam; concept = finite products,
  commutativity, and associativity. Do not mark statement-complete before the
  p.109 continuation is transcribed.

English repair `EG-EGA-I-P108-EN-331-EMPHASIS-001` is typographic source
fidelity and introduces no mathematical edge. Translator augmentation 3.2.9
remains an English-only editorial node pending independent replay of its cited
EGA II p.221 authority; it is not a diplomatic EGA I node.

## Incremental EGA I p.109 scaffold

- `I.3.3.5-fr`: prior incomplete node is now statement-complete. Concept =
  existence, commutativity, and associativity of finite products; explicit
  dependency `I.3.2.6-fr`.
- `I.3.3.6-fr`: definition/construction node for base extension or inverse
  image of a prescheme. Semantic diagram target
  `I.3.3.6.base-change-diagram-fr` records the cartesian construction and its
  structural morphisms `p`, `pi`, `pi'`, `theta`, and `varphi`.
- `I.3.3.7-fr`: functoriality node for inverse image/base change; explicit
  dependency `I.3.3.6-fr`.
- `I.3.3.8-fr`: universal-mapping characterization of base change; explicit
  dependency `I.3.3.6-fr`. Source-typo witness
  `EG-EGA-I-P109-FR-338-F-VS-G-SRCTYPO-001` records that French prints `f`
  where the defining pair is `(g,psi)`. Keep the source witness and the English
  correction as separate diplomatic/editorial layers.
- `I.3.3.9-fr`: transitivity proposition for successive base changes; proof
  continues on p.110. Semantic diagram target
  `I.3.3.9.transitivity-diagram-fr` records the three-level base-change tower.
  The p.109 diagram is intentionally unpunctuated because the sentence remains
  open across the page seam.

English punctuation repair `EG-EGA-I-P109-EN-339-DIAGRAM-PERIOD-001`
introduces no mathematical edge. Final coordinate, candidate, and action
closure remains deferred to the stable cumulative reader.

## Incremental EGA I p.110 scaffold

- `I.3.3.9.1-fr`: formula target for transitivity of base change on objects;
  explicit parent `I.3.3.9-fr`.
- `I.3.3.9.2-fr`: formula target for transitivity of base change on morphisms;
  explicit parent `I.3.3.9-fr`.
- `I.3.3.10-fr`: product/base-change compatibility corollary; dependencies
  `I.3.3.9.1-fr` and finite-product associativity from `I.3.3.5-fr`.
- `I.3.3.10.1-fr`: functoriality formula target for the preceding canonical
  product isomorphism.
- `I.3.3.11-fr`: relative-product characterization of base change;
  dependencies `I.3.3.9-fr` and `I.3.3.4-fr`.
- `I.3.3.11.diagram-fr`: semantic diagram target with six objects and arrows
  `psi_(S')`, `f_(S')`, `psi`, and `f`. English restoration
  `EG-EGA-I-P110-EN-3311-DIAGRAM-MISSING-PSI-LABEL-001` changes no edge
  semantics; it restores the visible label for the already-present arrow.
- `I.3.3.12-fr`: statement node, presently page-complete through `u=v` but
  semantically continued on p.111; concept = products of monomorphisms are
  monomorphisms; external locator `(T, I, 1.1)` remains unclassified until the
  stable cumulative graph pass.

Diagram-side repair
`EG-EGA-I-P109-P110-FR-DIAGRAM-LABEL-SIDE-REPAIR-001` changes rendered geometry
only and creates no new mathematical edge. It supersedes the p.109 layout-PASS
surface while preserving all stable target identities. Final coordinate,
candidate, edge, subject-index, formula-index, dependency, and implication
closure remains deferred until the cumulative source and PDF stabilize.

## Incremental EGA I p.111 scaffold

- `I.3.3.12.base-change-monomorphism-fr`: formula/conclusion target under
  `I.3.3.12-fr`; product of base-changed monomorphisms is a monomorphism.
  Provenance binding
  `EG-EGA-I-P111-FR-3312-BASECHANGE-TARGET-Y-VS-XPRIME-SRCTYPO-001`
  records the diplomatic printed codomain `Y_(S')` and the source-backed
  English correction `X'_(S')` without changing this semantic target.
- `I.3.3.13-fr`: proposition target; base change preserves open immersions,
  closed immersions, and local immersions. Parent/dependency:
  `I.3.3.12-fr` plus the definitions of the three immersion kinds.
- `I.3.3.14-fr`: affine base-change construction target. Its canonical
  correspondence target is `I.3.3.14.correspondence-fr`, relating ring
  homomorphisms `A->B` to scheme morphisms `Spec(B)->Spec(A)`.
- `I.3.3.15-fr`: local characterization of morphisms into `Z[T]` by compatible
  ring maps `A(T_i)->B_i`. Provenance binding
  `EG-EGA-I-P111-FR-3315-MORPHISM-DIRECTION-SRCTYPO-001` records diplomatic
  `Z[T]->X` versus source-backed English `X->Z[T]`; the semantic direction is
  fixed by the local-ring correspondence in `I.3.3.14.correspondence-fr`.
- `subsection:I.3.4-fr`: subsection target, ``Morphisms determined by
  restrictions to open sets.''
- `I.3.4.1-fr`: proposition target; equality of two morphisms is local on an
  open covering of the source.
- `I.3.4.2-fr`: proposition target begun on p.111 and continued on p.112;
  current diplomatic text ends after `la partie de`. Mark this node
  `continued=true`, `next_printed_page=112`, and do not close its statement or
  proof until the p.112 authority is transcribed.

The two `...SRCTYPO-001` identifiers above are provenance/adjudication records,
not mathematical targets. They should remain queryable as annotations on the
corresponding formula/statement nodes. Final page coordinates, reference
actions, subject/formula indices, and implication closure remain deferred
until the cumulative source and PDF stabilize.

## Incremental EGA I p.112 scaffold

- `I.3.4.2-fr`: the p.111-open proposition is now statement-complete.
  `I.3.4.2.1-fr` is its fibre-product formula target, with the two structure
  maps to `S(T)` explicit.
- `I.3.4.3-fr`: relative-points notation and product characterization node.
  Formula targets are `I.3.4.3.1-fr` and `I.3.4.3.2-fr`; diagram target
  `I.3.4.3.product-diagram-fr` records the maps `r'`, `s'`, `varphi'`, and
  `psi'`. English repair
  `EG-EGA-I-P112-EN-343-PRODUCT-DIAGRAM-PSI-LABEL-SIDE-001` restores visible
  label geometry and creates no new edge.
- `I.3.4.4-fr`: notation node for points with values in an affine ring or
  algebra and covariance in the value ring.
- `I.3.4.5-fr`: geometric-point definition node begun on p.112 and completed
  on p.113. Its explicit source citation is `I.2.4.4-fr`, the local-scheme
  morphism/local-homomorphism correspondence. The inherited English link to
  I.2.2.4 was discovered and repaired during p.113 compiled QA under
  `EG-EGA-I-P112-EN-345-CITATION-224-VS-244-001`; R42 preserves the exact
  pre-repair English generation.

## Incremental EGA I p.113 scaffold

- `I.3.4.5-fr`: now statement-complete. Concept = a geometric point consists
  of its location and a residue-field extension, with relative and rational
  point specializations. Explicit dependency `I.2.4.4-fr`.
- `I.3.4.6-fr`: lemma target; a finite family of points over one base point
  admits a common residue-field extension and a geometric point of the
  product with the prescribed projected locations. External proof citation:
  Bourbaki, *Alg.*, chapter V, section 4, proposition 2.
- `I.3.4.7-fr`: finite-product point criterion; necessary and sufficient that
  all projected points lie over one point of the base. Explicit dependency
  `I.3.4.6-fr`. Target `I.3.4.7.underlying-map-fr` records the canonical
  surjection `(X x_S Y) -> (X) x_(S) (Y)` and its general failure of
  injectivity; forward explanatory dependency `I.3.4.9-fr` remains pending
  until p.114.
- `I.3.4.8-fr`: base-change image corollary, statement-complete with proof
  pending on p.114. Formula target `I.3.4.8.base-change-image-fr` records
  `q^(-1)(f(M))=f_(S')(p^(-1)(M))`. Do not close proof dependencies before
  the next authority page is admitted.

English repairs `EG-EGA-I-P113-EN-345-UNDERLYING-SPACE-001` and
`EG-EGA-I-P113-EN-345-AINSI-CONNECTOR-001` restore carrier terminology and
source discourse logic only. The p.112 citation repair changes one explicit
dependency target from the incorrect I.2.2.4 to source-backed I.2.4.4. Final
coordinates, exhaustive references, subject/formula indices, and implication
closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.114 scaffold

- `I.3.4.8-fr`: proof is now complete. Diagram target
  `I.3.4.8.proof-diagram-fr` records the cartesian identification
  `X_(S') = X x_Y Y_(S')` and the arrows `p`, `q`, `f`, and `f_(S')`.
  Explicit proof dependencies are `I.3.3.11-fr` and `I.3.4.7-fr`.
- `I.3.4.9-fr`: proposition target; points of `X x_S Y` over prescribed
  `x` and `y` correspond canonically to types of composite extensions of
  `k(x)` and `k(y)` over `k(s)`. Formula target
  `I.3.4.9.tensor-product-fibre-fr` identifies the auxiliary fibre product
  with `Spec(k(x) tensor_(k(s)) k(y))`. Explicit internal dependencies are
  `I.2.4.7-fr`, `I.3.2.4-fr`, `I.2.4.5-fr`, and `I.3.2.1-fr`; the external
  locators are Bourbaki, *Alg.*, chapter VIII, section 8, propositions 1 and
  2.
- `subsection:I.3.5-fr`: subsection target, ``Surjections and injections.''
- `I.3.5.1-fr`: general property-stability discussion begun on p.114. Clauses
  (i) and (ii) are admitted, but the surrounding argument continues on p.115;
  mark the node `continued=true`, `next_printed_page=115`, and do not treat it
  as statement-complete.

Provenance annotation
`EG-EGA-I-P114-FR-349-TENSOR-MONOMORPHISM-SRCTYPO-001` records the printed French
`monomorphisme` for the induced map
`k(x) tensor_(k(s)) k(y) -> k(z)`. The diplomatic French layer preserves the
author text. The paired English layer retains its already-explicit correction
to `homomorphism` and visible translator note because the tensor-product map
need not be injective. English repair
`EG-EGA-I-P114-EN-348-DIAGRAM-Q-LABEL-SIDE-001` changes only rendered label
geometry for `q` and creates no mathematical edge. Final coordinates,
exhaustive references, subject/formula indices, and implication closure remain
deferred to the stable cumulative reader.

## Incremental EGA I p.115 scaffold

- `I.3.5.1-fr`: the p.114-open discussion is now statement-complete. Formula
  target `I.3.5.1.product-composition-fr` factors `f x_S g` as
  `(f x 1_Y)` followed by `(1_X' x g)`. The node records the two sufficient
  transfer principles: identities with property P plus product stability give
  base-extension stability, while stability of P under composition plus
  base-extension stability gives product stability.
- `I.3.5.2-fr`: proposition target; surjectivity is stable under products and
  arbitrary base extension. Explicit dependencies are `I.3.5.1-fr` and
  `I.3.4.8-fr`, with the latter applied to `M=X`.
- `I.3.5.3-fr`: field-valued lifting criterion for surjectivity. Diagram target
  `I.3.5.3.surjectivity-diagram-fr` records the extension `K'/K` and a lift
  `Spec(K')->X` over `Spec(K)->Y`. Explicit internal dependencies are
  `I.2.4.6-fr`, `I.2.2.1-fr`, and `I.3.4.5-fr`; the external construction
  cites Bourbaki, *Alg.*, chapter V, section 4, proposition 2.
- `I.3.5.4-fr`: definition target; a morphism is universally injective, or
  radicial, exactly when `X(K)->Y(K)` is injective for every field `K`.
  External locator `(T, 1.1)` supplies the immediate monomorphism example.
- `I.3.5.5-fr`: reduction of radiciality testing to algebraically closed
  fields, presently incomplete at the p.115 seam. Diagram target
  `I.3.5.5.algebraic-closure-diagram-fr` records `alpha`, `alpha-prime`,
  `phi`, and `phi-prime`; mark the node `continued=true`,
  `next_printed_page=116`, and do not close the argument before the next
  authority page.

English repair `EG-EGA-I-P115-EN-351-COMPOSITION-ANTECEDENT-001` restores the
source hypothesis that both component morphisms possess P before their
composite is assumed to preserve P; it repairs the English logical statement
without introducing a new French-source edge. Repairs
`EG-EGA-I-P115-EN-353-ENCORE-CONNECTOR-001` and
`EG-EGA-I-P115-EN-354-AUSSITOT-ADVERB-001` affect discourse only.
`EG-EGA-I-P115-EN-355-ALPHA-PRIME-LABEL-SIDE-001` changes diagram geometry
only. Final coordinates, exhaustive references, subject/formula indices, and
implication closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.116 scaffold

- `I.3.5.5-fr`: the p.115-open algebraic-closure argument is now complete.
  The injectivity conclusion follows from injectivity of `phi` and, by
  hypothesis, `alpha-prime` in
  `I.3.5.5.algebraic-closure-diagram-fr`.
- `I.3.5.6-fr`: proposition target; radicial morphisms are stable under
  composition, and radiciality of `g composed with f` descends to `f`.
  Explicit dependency `I.3.5.4-fr`; the proof reduces to the corresponding
  field-valued maps.
- `I.3.5.7-fr`: product and arbitrary base-extension stability for radicial
  morphisms. Formula target `I.3.5.7.field-valued-product-fr` records the two
  simultaneous identities for `(X x_S Y)(K)` and
  `(X-prime x_S Y-prime)(K)` and the induced map
  `(u,v) -> (f composed with u, g composed with v)`. Explicit dependencies
  are `I.3.5.1-fr` and `I.3.4.2.1-fr`.
- `I.3.5.8-fr`: point-map and residue-field characterization of radicial
  morphisms. The node records injectivity of `psi` and radicality of each
  extension `k(x)/k(psi(x))`; internal dependency `I.2.4.6-fr`, with external
  locator Bourbaki, *Alg.*, chapter V, section 4, proposition 2.
- `I.3.5.9-fr`: localization corollary; the canonical morphism
  `Spec(S inverse A) -> Spec(A)` is radicial because it is a monomorphism.
  Explicit dependency `I.1.6.2-fr`.
- `I.3.5.10-fr`: base-change corollary; the underlying-space image and the
  field-valued inverse-image description are statement-complete, with
  explicit dependencies `I.3.5.7-fr`, `I.3.5.8-fr`, and `I.3.4.8-fr`. Its
  proof remains incomplete after the exact words ``de la commutativité du
  diagramme''; mark the node `continued=true`, `next_printed_page=117`, and
  do not close the diagrammatic argument before the next authority page.

English repairs `EG-EGA-I-P116-EN-357-AUSSITOT-ADVERB-001` and
`EG-EGA-I-P116-EN-3510-AUSSITOT-ADVERB-001` restore source discourse force
only and introduce no mathematical edge. The paired field-valued product
identities remain in consecutive English displays as a documented measure
normalization; formula order, equality, and joint logical role are unchanged.
Final coordinates, exhaustive references, subject/formula indices, and
implication closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.117 scaffold

- `I.3.5.10-fr`: the p.116-open proof is now complete. Diagram target
  `I.3.5.10.base-change-points-diagram-fr` records the field-valued
  base-change square with objects `X-prime(K)`, `Y-prime(K)`, `X(K)`, and
  `Y(K)` and two horizontal plus two vertical maps.
- `I.3.5.11-fr`: remark target; universal injectivity is characterized by
  injectivity after every base change. The converse uses a non-radicial
  residue-field monomorphism to produce two distinct `Y-prime`-sections.
  Explicit dependencies are `I.3.5.7-fr`, `I.3.5.8-fr`, and
  `I.3.3.14-fr`.
- `subsection:I.3.6-fr`: subsection target, ``Fibres.''
- `I.3.6.1-fr`: proposition target; the underlying space of
  `X x_Y Spec(O_y/a_y)` is homeomorphic to the fibre `f^(-1)(y)` with its
  induced topology. Formula target `I.3.6.1.localization-fraction-fr` records
  the affine-localization representation of every element of
  `B tensor_A A-prime`. Explicit dependencies are `I.3.5.4-fr`,
  `I.2.4.7-fr`, `I.1.1.12-fr`, `I.3.5.10-fr`, `I.3.3.4-fr`,
  `I.3.2.7-fr`, and `I.1.2.4-fr`.
- `I.3.6.2-fr`: convention target; a fibre's `k(y)`-prescheme structure is
  transported from `X x_Y Spec(k(y))`. It also records the historical
  `X tensor_Y B` and `X tensor_(O_Y) B` notations and the field-valued-points
  consequence of `I.3.5.10-fr`.
- `I.3.6.3-fr`: fibre-of-a-composite node begun on p.117. Formula target
  `I.3.6.3.fibre-composition-fr` identifies
  `X x_Z Spec(k(z))`, `(X x_Y Y) x_Z Spec(k(z))`, and
  `X x_Y g^(-1)(z)`. The numbered paragraph continues on p.118; mark it
  `continued=true`, `next_printed_page=118`, and do not close the open-set
  consequence before the next authority page.

English repair `EG-EGA-I-P117-EN-3511-DABORD-SEQUENCE-001` restores the
source's first-step discourse cue and introduces no mathematical edge. The
English fibre-product sign in 3.6.2, explicit proof boundary for 3.6.1, and
terminal period after the p.117 3.6.3 display are documented reader-facing
normalizations with unchanged objects, formulas, and implications. Final
coordinates, exhaustive references, subject/formula indices, and implication
closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.118 scaffold

- `I.3.6.3-fr`: the p.117-open numbered paragraph is now complete. Its
  open-subset consequence identifies the prescheme induced by `f^(-1)(y)` on
  `U intersect f^(-1)(y)` with the fibre of the restriction `f_U`.
- `I.3.6.4-fr`: titled transitivity-of-fibres proposition. For
  `X-prime=X x_Y Y-prime` and `y=g(y-prime)`, it identifies
  `f-prime^(-1)(y-prime)` with
  `f^(-1)(y) tensor_(k(y)) k(y-prime)`. Explicit dependency
  `I.3.3.9.1-fr`. Its open-neighbourhood consequence canonically identifies
  the fibre with the fibre of the restriction over any neighbourhood `V` of
  `y`.
- `I.3.6.5-fr`: local-prescheme projection proposition. It records the
  homeomorphism from `X x_Y Spec(O_y)` to the subspace `f^(-1)(Z)` and the
  local-ring isomorphism at each point. The affine proof identifies
  `A tensor_B B_y` with `S^(-1)A`; dependencies are `I.2.4.2-fr`,
  `I.3.6.1-fr`, Chapter 0 locator `0.1.5.2`, and `I.1.6.2-fr`.
- `subsection:I.3.7-fr` / `I.3.7-fr`: subsection target, ``Application:
  reduction of a prescheme mod. J.'' The attached provenance footnote marks
  the subsection as dependent on later Chapter I and Chapter II material and
  intended only for readers familiar with classical algebraic geometry.
- `I.3.7.1-fr`: reduction node; defines
  `X_0=X tensor_A (A/J)` as an `(A/J)`-prescheme induced from `X` by reduction
  mod. `J`.
- `I.3.7.2-fr`: historical reduction-terminology node begun on p.118. It
  records the local-ring residue-field case, the fraction-field prescheme
  `X-prime`, and the projective-embedding context, then begins the two-point
  affine-base description. The diplomatic text ends after the exact words
  ``l'unique point''; mark the node `continued=true`,
  `next_printed_page=119`, and do not close the closed/generic-point argument
  before the next authority page.

English repair
`EG-EGA-I-P118-EN-37-FOOTNOTE-LATER-CHAPTER-I-SCOPE-001` restores the
footnote's forward-reference scope and changes no mathematical edge. The
English title position, inline footnote treatment, reordered p.119 marker
within ``the unique closed point,'' and explicit proof boundaries are
documented structural normalizations. The French bounded wrapper's standard
Arabic footnote marker differs from the printed parenthesized marker while
preserving attachment, counter identity, and complete text; final facsimile
styling remains deferred to the cumulative reader. Final coordinates,
exhaustive references, subject/formula indices, and implication closure remain
deferred to the stable cumulative reader.

## Incremental EGA I p.119 scaffold

- `I.3.7.2-fr`: the p.118-open historical reduction discussion is now
  complete. For the two-point base `Y=Spec(A)`, it identifies the generic
  open `U=Spec(K)`, the induced prescheme `X tensor_A K`, and, for a
  Noetherian ambient prescheme `P`, the smallest closed subprescheme
  `X=closure(X-prime)` containing `X-prime`. It then identifies reduction
  mod. `J` with the closed fibre `psi^(-1)(y)` and records that intrinsic
  assertions belong to the `A`-prescheme `X`, independently of a prior
  projective immersion. The two closure assertions cite future Chapter I
  locator `I.9.5.10`.
- `I.3.7.3-fr`: discrete-valuation properness node. For `X` proper over `A`,
  `A`-valued points of `X` and `K`-valued points of `X-prime` correspond
  bijectively; external locators are `II.5.5.4` and `II.7.3.8`. The closing
  sentence separates the result from the unnecessary dimension-one
  hypothesis on the local base ring.
- `section:I.4-fr`: section target, ``Subpreschemes and immersion
  morphisms.''
- `subsection:I.4.1-fr`: subsection target, ``Subpreschemes.''
- `I.4.1.1-fr`: quasi-coherence locality and closure node. A quasi-coherent
  `O_X`-module is characterized on affine opens by an associated
  `Gamma(V,O_X)`-module; kernels, cokernels, images, inductive limits, and
  direct sums remain quasi-coherent. Explicit dependencies are
  `0.5.1.3-fr`, `I.1.4.1-fr`, `I.1.3.7-fr`, and `I.1.3.9-fr`.
- `I.4.1.2-fr`: proposition-statement target. For a quasi-coherent ideal
  sheaf `I` in `O_X`, the support `Y` of `O_X/I` is closed and the restriction
  `O_Y` makes `(Y,O_Y)` a prescheme. The statement is complete on p.119, but
  its proof begins on p.120; mark `proof_pending=true`,
  `next_printed_page=120`, and do not admit proof content before the next
  authority page.

The paired p.119 English recheck requires no source mutation. Its expansion
of the two terminal references in 4.1.1 to ``Theorem'' and ``Corollary'' is a
reader-facing reference-type normalization with unchanged targets. The
bounded English QA prefix is line-identical to the live `ega1-4.tex` source
through Proposition 4.1.2, and its section-counter seed affects only the
bounded render. Final coordinates, exhaustive references, subject/formula
indices, and implication closure remain deferred to the stable cumulative
reader.

## Incremental EGA I p.120 scaffold

- `I.4.1.2-fr`: the p.119-complete proposition now has its full proof. On an
  affine `X=Spec(A)`, the quasi-coherent ideal sheaf is
  `I=tilde(mathfrak I)`, its support is `V(mathfrak I)=Spec(A/mathfrak I)`,
  and the direct image of the quotient structure sheaf is canonically
  `O_X/I`. Explicit dependencies are `I.2.1.3-fr`, `I.1.4.1-fr`,
  `I.1.1.11-fr`, `I.1.6.3-fr`, and `I.1.3.9-fr`.
- `term:sous-preschema-fr`: terminology node for the subprescheme of `X`
  defined by a quasi-coherent ideal sheaf `I`.
- `I.4.1.3-fr`: definition node. A subprescheme has a locally closed
  underlying subspace `Y` and, in the largest open `U` where `Y` is closed,
  is defined by a quasi-coherent ideal sheaf on `O_X|U`; it is a closed
  subprescheme exactly in the specialization `U=X`.
- `I.4.1.closed-subprescheme-ideal-bijection-fr`: canonical-bijection node
  between closed subpreschemes of `X` and quasi-coherent ideal sheaves of
  `O_X`. Uniqueness is recovered from common closed support and identical
  restrictions of the quotient sheaves. Explicit dependency
  `I.4.1.2-fr`.
- `I.4.1.4-fr`: open-restriction node. For `V` open in the maximal `U`, the
  induced prescheme on `Y intersect V` is the closed subprescheme of `V`
  defined by `J|V`; the paragraph ends by opening the converse.
- `I.4.1.5-fr`: local subprescheme criterion and proof. A cover of `Y` by
  opens `V_alpha` on which the induced ringed spaces are closed
  subpreschemes glues to a unique quasi-coherent ideal sheaf on the maximal
  open `U`, hence makes `Y` a subprescheme of `X`. Explicit dependencies are
  `I.4.1.3-fr` and `I.4.1.4-fr`.
- `I.4.1.open-induced-subprescheme-fr`: consequence node; the prescheme
  induced by `X` on any open subset of `X` is a subprescheme of `X`.
- `I.4.1.6-fr`: proposition node begun on p.120. The diplomatic source ends
  at the exact printed-page hyphenation ``d'un sous-''; mark it
  `continued=true`, `next_printed_page=121`, and do not complete the nested
  subprescheme assertion before the next authority page.

The paired p.120 English recheck requires no source mutation. Its explicit
proof environments and the type words ``Proposition'' and ``Corollary'' in
the proof of 4.1.2 are reader-facing structural/reference normalizations with
unchanged claims and targets. Its p.121 marker follows the complete English
word ``subprescheme'', whereas the diplomatic French source preserves the
printed mid-word seam ``sous-'' / ``préschéma''. The bounded English
continuation projection is line-identical to live `ega1-4.tex` lines 18--67,
apart from its final balancing environment close. Final coordinates,
exhaustive references, subject/formula indices, and implication closure
remain deferred to the stable cumulative reader.

## Incremental EGA I p.121 scaffold

- `I.4.1.6-fr`: the p.120-open proposition is now complete. A subprescheme,
  respectively closed subprescheme, of a subprescheme of `X` is canonically
  identified with a subprescheme, respectively closed subprescheme, of `X`.
  Its affine proof uses the canonical quotient identification
  `A/J-prime = (A/J)/(J-prime/J)` for `J` contained in `J-prime`; explicit
  dependency `I.4.1.5-fr`. The following sentence makes this identification
  a standing convention.
- `I.4.1.7-fr`: canonical-injection node. The underlying-space injection
  `psi:Y to X` and the surjective sheaf homomorphism
  `omega:O_X|Y to O_Y` define the monomorphism of ringed spaces
  `j=(psi,omega^b)`, hence the canonical injection morphism of preschemes.
  The composite `Y to X to Z` is the restriction of a morphism `f:X to Z`
  to `Y`. Explicit dependencies are `0.3.7.1-fr`, `0.4.1.1-fr`, and
  `I.2.2.1-fr`.
- `I.4.1.8-fr`: factorization node. A morphism `f:Z to X` is ``majoré'' by
  the injection `j:Y to X` when it factors as `Z to Y to X`; the intervening
  morphism is unique because `j` is a monomorphism. External dependency
  `T.I.1.1`.
- `I.4.1.9-fr`: injection-factorization criterion. Factorization through
  `j:Y to X` is equivalent to `f(Z)` being contained in `Y` together with
  factorization of every corresponding stalk map through `(O_Y)_y`; the
  equivalent formulation is containment of the two stalk-map kernels. Its
  proof reduces to a closed subprescheme, forms the kernel ideal sheaf `J`,
  uses `psi^*(I)` contained in `J`, and factors `theta^sharp` through
  `psi^*(O_X/I)` to construct a local morphism `g-prime:Z to Y`. Explicit
  dependencies are `I.4.1.3-fr` and `0.3.7.2-fr`. The proof prose continues
  on p.122; mark `continued=true`, `next_printed_page=122`, and do not state
  the final factorization conclusion before the next authority page.

The paired p.121 English recheck requires no source mutation. Its whole-word
p.121 marker and explicit proof environment for 4.1.6 are reader-facing
structural normalizations. The retained translator footnote explains the
deliberate use of the French term ``majoré'' and introduces no source node.
At the terminal seam English names the constructed morphism `g` rather than
French `g-prime`; this dummy-variable normalization changes no map or
implication. The bounded continuation is line-identical to live
`ega1-4.tex` lines 18--113 apart from its final balancing proof close. Final
coordinates, exhaustive references, subject/formula indices, and implication
closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.122 scaffold

- `I.4.1.9-fr`: the p.121-open proof is now complete. The constructed local
  morphism from `Z` to `Y` is a morphism of preschemes and gives the required
  factorization through the canonical injection. Explicit dependency
  `I.2.2.1-fr`. The diplomatic text preserves the printed change from
  `g-prime` at the p.121 seam to `g` in the concluding equation.
- `I.4.1.10-fr`: injection-factorization corollary. An injection morphism
  `Z to X` factors through `Y to X` exactly when `Z` is a subprescheme of
  `Y`.
- `I.4.1.subprescheme-order-fr`: order node. The notation `Z <= Y` records
  the resulting order relation on the set of subpreschemes of `X`.
- `subsection:I.4.2-fr`: subsection target, ``Morphismes d'immersion.''
- `I.4.2.1-fr`: immersion-definition node. An immersion, closed immersion,
  or open immersion factors as an isomorphism onto the corresponding kind
  of subprescheme followed by its canonical injection. The associated
  subprescheme and isomorphism are unique; the factorization is canonical.
  Every immersion is a monomorphism and therefore radicial. Explicit
  dependencies are `I.4.1.10-fr`, `I.4.1.7-fr`, and `I.3.5.4-fr`.
- `I.4.2.2-fr`: immersion-criterion node. Part (a) characterizes open
  immersions by a homeomorphism onto an open subset and bijective stalk
  maps. Part (b) characterizes immersions and closed immersions by a
  homeomorphism onto a locally closed or closed subset and surjective stalk
  maps. The proof establishes (a), then begins the affine closed-image case
  of (b), transports the ringed-space structure to `Z=psi(Y)`, and starts
  the local proof that the direct image is a quasi-coherent `O_X`-module.
  It ends at the exact words ``restriction a U de l'image''; mark
  `continued=true`, `next_printed_page=123`.
- `erratum:I.4.2.2.theta-sharp-direction-fr`: printed-source mathematical
  error node. In proof (a), printed French reverses the source and target of
  `theta-sharp`, saying it is an isomorphism from `O_Y` onto
  `psi^*(O_X)`. The typed map has source `psi^*(O_X)` and target `O_Y`.
  Canonical diplomatic French preserves the print and applies no silent
  correction; the paired English gives the typed direction and carries an
  explicit translator footnote.

The paired p.122 English recheck requires no new source mutation. Its
consistent `g` notation across the p.121/p.122 seam is a dummy-variable
normalization. Its p.123 marker precedes the complete direct-image object,
whereas printed French p.122 ends inside the corresponding phrase after
``de l'image''; this page-boundary normalization changes no object or
implication. The bounded continuation is line-identical to live
`ega1-4.tex` lines 18--161 apart from its final balancing `end-enumerate`
and `end-proof`. Final coordinates, exhaustive references, subject/formula
indices, and implication closure remain deferred to the stable cumulative
reader.

## Incremental EGA I p.123 scaffold

- `I.4.2.2-fr`: the p.122-open proof is now complete. In the affine
  closed-image case, the restricted direct image is locally identified with
  the module associated to the affine-ring homomorphism, hence is
  quasi-coherent. The stalk diagram compares `theta_(psi(y))` with
  `theta_y^sharp`; its vertical arrows are isomorphisms, so stalkwise
  surjectivity makes the sheaf homomorphism surjective. The quotient
  presentation `A-tilde/J-tilde` then produces the associated closed
  subprescheme and factorization. Explicit dependencies are `I.1.7.3-fr`,
  `I.1.6.3-fr`, `0.3.4.5-fr`, `0.3.7.2-fr`, and `I.1.3.8-fr`.
- `I.4.2.2.theta-diagram-fr`: commutative-diagram node linking the stalk of
  `O_X`, the stalk of `psi_*(O_Y)`, `psi^*(O_X)` at `y`, and `O_y`, with
  horizontal maps `theta_(psi(y))` and `theta_y^sharp`.
- `I.4.2.2.general-case-fr`: local-to-global factorization node. On affine
  opens `U` for which `U intersect psi(Y)` is closed, the restriction is a
  closed immersion with canonical factorization through `Z_U`. Uniqueness
  identifies the restrictions on nested affine opens, and the `Z_U` glue to
  a subprescheme `Z` of `X` together with an isomorphism `g:Y to Z` and
  `f=j composed with g`. Explicit dependencies are `I.4.2.1-fr` and
  `I.4.1.5-fr`.
- `I.4.2.3-fr`: affine closed-immersion criterion. For affine `X`, a
  morphism `f=(psi,theta):Y to X` is a closed immersion exactly when `Y` is
  affine and `Gamma(psi):Gamma(O_X) to Gamma(O_Y)` is surjective.
- `I.4.2.4-fr`: locality corollary begun on p.123. Part (a) states that
  immersion or open-immersion status is checked after restriction over an
  open cover `(V_lambda)` of `f(Y)`. The diplomatic text ends at the exact
  words ``il faut et il suffit''; mark `continued=true`,
  `next_printed_page=124`.

The paired p.123 English recheck requires no source mutation and introduces
no new author correction. The explicit correction of the p.122
`theta-sharp` direction remains carried and visible but is not counted anew.
At the p.122/p.123 seam English keeps ``direct image'' before the marker and
the complete parenthesized object after it, while printed French begins
p.123 with ``directe''; this boundary normalization changes no object. The
bounded continuation is line-identical to live `ega1-4.tex` lines 18--204
apart from its final balancing `end-enumerate` and `end-corollary`. Final
coordinates, exhaustive references, subject/formula indices, and implication
closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.124 scaffold

- `I.4.2.4-fr`: locality corollary completed. Part (a) checks immersion or
  open-immersion status on the induced preschemes over an open cover of
  `f(Y)`; part (b) checks closed-immersion status on the induced preschemes
  over an open cover of `X`. The proof combines the stalk criterion of
  `I.4.2.2-fr` with the corresponding locally closed, open, or closed
  topological image condition.
- `I.4.2.5-fr`: composition node. The composite of two immersions, two open
  immersions, or two closed immersions is respectively an immersion, an
  open immersion, or a closed immersion. Explicit dependency is
  `I.4.1.6-fr`.
- `subsection:I.4.3-fr`: subsection target, ``Produit d'immersions.''
- `I.4.3.1-fr`: product-of-immersions node. For `S`-morphisms
  `alpha:X' to X` and `beta:Y' to Y`, their fiber-product morphism preserves
  immersion, open-immersion, and closed-immersion status. When the factors
  identify `X'` and `Y'` with subpreschemes `X''` and `Y''`, the underlying
  product space is identified with
  `p^(-1)(X'') intersect q^(-1)(Y'')`. The proof reduces first to closed
  subpreschemes and then begins the reduction to affine `S` via the
  `S_lambda` restrictions and mixed-index product identifications. Explicit
  dependencies are `I.4.2.1-fr`, `I.3.2.7-fr`, `I.4.1.3-fr`,
  `I.3.2.5-fr`, and `I.3.2.6.4-fr`. It ends at the exact words ``la
  restriction de alpha times-sub-S beta''; mark `continued=true`,
  `next_printed_page=125`.

The paired p.124 English recheck requires no source mutation and introduces
no new author correction. The explicit p.122 `theta-sharp` correction remains
carried but is not counted anew. English places the p.124 marker immediately
before ``for its restriction'', matching the French semantic continuation
``que sa restriction''. The bounded continuation is line-identical to live
`ega1-4.tex` lines 18--250 apart from its final balancing `end-proof`. Final
coordinates, exhaustive references, subject/formula indices, and implication
closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.125 scaffold

- `I.4.3.1-fr`: the p.124-open proof is now complete. After reducing over an
  affine cover of `S`, affine covers of `X` and `Y` reduce the product map to
  mixed-index restrictions over `U_i times-sub-S V_j`. In the affine case,
  quotient maps `rho:B to B-prime` and `sigma:C to C-prime` induce the
  surjection `tau=rho tensor sigma`; its kernel
  `u(mathfrak-b)+v(mathfrak-c)` defines the closed set
  `p^(-1)(X-prime) intersect q^(-1)(Y-prime)`. Explicit dependencies are
  `I.4.2.4-fr`, `I.3.2.7-fr`, `I.1.7.3-fr`, `I.3.2.2-fr`,
  `I.3.2.3-fr`, `I.1.2.2.1-fr`, and `I.1.1.2-fr`.
- `I.4.3.2-fr`: base-change node. An immersion, open immersion, or closed
  immersion remains of the same kind after every extension of the base
  prescheme. Explicit dependency is `I.4.3.1-fr`.
- `subsection:I.4.4-fr`: subsection target, ``Image réciproque d'un
  sous-préschéma.''
- `I.4.4.1-fr`: inverse-image node. For a subprescheme `Y-prime` of `Y`,
  the projection `X times-sub-Y Y-prime to X` is the corresponding kind of
  immersion, its associated subprescheme has underlying space
  `f^(-1)(Y-prime)`, and a morphism into `X` factors through it exactly when
  its composite with `f` factors through `Y-prime`. Explicit dependencies
  are `I.3.3.4-fr`, `I.4.3.1-fr`, and `I.3.5.10-fr`.
- `I.4.4.inverse-image-terminology-fr`: terminology node begun on p.125.
  The associated subprescheme is called the inverse image of `Y-prime`
  under `f`. The diplomatic text ends at the exact words ``qui s'accorde
  avec celle introduite''; mark `continued=true`,
  `next_printed_page=126`.

The paired p.125 English recheck requires no source mutation and introduces
no new author correction. The explicit p.122 `theta-sharp` correction remains
carried but is not counted anew. English places the p.125 marker at the same
semantic continuation and the p.126 marker after the same incomplete
terminology sentence. The bounded continuation is line-identical to live
`ega1-4.tex` lines 18--298 and requires no balancing additions. Final
coordinates, exhaustive references, subject/formula indices, and implication
closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.126 scaffold

- `I.4.4.inverse-image-terminology-fr`: the p.125-open terminology sentence
  is complete. The subprescheme denoted `f^(-1)(Y-prime)` is the inverse
  image defined by the general fibre-product construction, and every later
  use of that notation as a subprescheme has this meaning. Explicit
  dependency is `I.3.3.6-fr`.
- `I.4.4.inverse-image-factorisation-fr`: identity-case factorization node.
  If `f^(-1)(Y-prime)=X`, the injection is the identity and `f` factors as
  `X to Y-prime to Y`.
- `I.4.4.closed-point-fibre-fr`: closed-point node. For closed `y`, the
  inverse image of the least closed subprescheme `Spec(k(y))` is canonically
  identified with the fibre `f^(-1)(y)`. Explicit dependencies are
  `I.4.1.9-fr` and `I.3.6.2-fr`.
- `I.4.4.2-fr`: composition node. For `h=g composed-with f`, inverse image
  satisfies `f^(-1)(g^(-1)(Z-prime))=h^(-1)(Z-prime)`. Explicit dependency
  is the canonical product isomorphism `I.3.3.9.1-fr`.
- `I.4.4.3-fr`: infimum node. Pulling each of two subpreschemes back along
  the other's injection produces their greatest lower bound, canonically
  represented by `X-prime times-sub-X X-double-prime`. Explicit dependencies
  are `I.4.4.1-fr` and `I.4.1.10-fr`. Diplomatic French preserves the
  printed singular phrase ``canoniquement isomorphée''.
- `I.4.4.4-fr`: inverse-image/infimum node. Inverse image commutes with the
  binary greatest lower bound. Explicit dependency is `I.3.3.9.1-fr`.
- `I.4.4.5-fr`: ideal-pullback node. If closed `Y-prime` is defined by the
  quasi-coherent ideal `K`, its inverse image is defined by
  `f-star(K) O_X`; the local proof uses the tensor-quotient identity. Explicit
  dependencies are `I.4.1.3-fr` and `I.1.6.9-fr`.
- `erratum:I.4.4.5.algebra-direction-fr`: officially evidenced printed
  mathematical error node. French prints ``B est une A-algèbre'' before
  forming `A tensor-sub-B (B/K)=A/KA`; the typed statement requires `A` to
  be a `B`-algebra. Canonical French preserves print. English retains the
  explicit `erratum[II]` correction. The existing official-evidence crop has
  SHA-256 `19055BEC1A1046C9BCB4BDD2BAF0CA519E4C7B3D994BC29E9BCC6EB9EB14E823`.
- `I.4.4.6-fr`: factorization/ideal-inclusion node. The restriction to a
  closed subprescheme `X-prime` factors through `Y-prime` exactly when
  `f-star(K) O_X` is contained in `J`. Explicit dependencies are
  `I.4.4.1-fr` and `I.4.4.5-fr`.
- `repair:I.4.4.6.ideal-O_X-en`: paired-English source-fidelity repair node.
  Inherited English omitted the `O_X` factor from the final ideal inclusion,
  despite retaining it in `I.4.4.5` and later parallel uses. The repair
  restores `f-star(K) O_X subset J`; one context-bound inverse operation
  reproduces the R56 English source exactly.
- `subsection:I.4.5-fr`: subsection target, ``Immersions locales et
  isomorphismes locaux.''
- `I.4.5.1-fr`: local-immersion definition. At every point, suitable open
  neighbourhoods in source and target make the restricted map a closed
  immersion between the induced preschemes.
- `I.4.5.2-fr`: local-isomorphism definition begun on p.126. The diplomatic
  text ends at the exact words ``un isomorphisme local en''; mark
  `continued=true`, `next_printed_page=127`, and
  `temporary_final_close=end-definition`.

The paired p.126 English recheck confirms one new official author correction
at `I.4.4.5` and applies one inherited formula-fidelity repair at
`I.4.4.6`. R57 changes only `ega1/ega1-4.tex`, restoring the omitted `O_X`;
R56 is the exact inverse point. The p.126 marker follows the French semantic
continuation, and the p.127 marker follows the same incomplete local-
isomorphism phrase. The bounded continuation's first 353 lines are
line-identical to repaired live `ega1-4.tex` lines 18--370, followed by one
temporary `end-definition`. Final coordinates, exhaustive references,
subject/formula indices, and implication closure remain deferred to the
stable cumulative reader.

## Incremental EGA I p.127 scaffold

- `I.4.5.2-fr`: the p.126-open definition is complete. A morphism is a local
  isomorphism at `x` when its restriction to a suitable open neighbourhood of
  `x` is an open immersion into the target; it is a local isomorphism when
  this holds at every source point.
- `I.4.5.3-fr`: characterization node. An immersion (respectively closed
  immersion) is a local immersion whose underlying map is a homeomorphism
  onto a subset (respectively closed subset); an open immersion is an
  injective local isomorphism. Parent is `subsection:I.4.5-fr`; terminology
  dependencies are `I.4.5.1-fr` and `I.4.5.2-fr`.
- `I.4.5.4-fr`: irreducible-source criterion. A dominant injective local
  immersion from irreducible `X` is an immersion with open image. The proof
  uses density of every nonempty open neighbourhood, dominance, and
  injectivity to identify the local source neighbourhood with the full
  inverse image of its target neighbourhood. Definition-use edge is
  `I.4.5.1-fr`.
- `I.4.5.5-fr`: stability node. Local immersions and local isomorphisms are
  stable under composition, fibre products over `S`, and base extension.
  Explicit proof-use edges are `I.3.5.1-fr`, typed transitivity target
  `I.4.2.5-fr`, `I.3.2.7-fr`, and `I.4.3.1-fr`. The printed citation edge to
  `I.4.2.4-fr` is retained separately as a source-error edge and is not
  promoted to a mathematical dependency.
- `source-error:I.4.5.5.transitivity-citation-fr`: French print cites
  `(4.2.4)` for transitivity of immersions; the typed dependency is
  `I.4.2.5-fr`. Canonical French preserves `(4.2.4)`. English retains
  `I.4.2.5` and exposes the intervention in a translator footnote. No official
  erratum evidence was found in the bounded recheck.
- `source-error:I.4.5.5.unintroduced-z-fr`: the product proof uses `z` and
  `z-prime` in the definitions of `x,x-prime,y,y-prime` without first
  introducing either point. Canonical French preserves the omission. English
  introduces `z in X times-sub-S Y` and its image `z-prime`, with a visible
  translator footnote. Typed object edges attach both points to the source and
  target of `f times-sub-S g`.
- `section:I.5-fr`: section target, ``Preschemes reduits; condition de
  separation.''
- `subsection:I.5.1-fr`: subsection target, ``Preschemes reduits.''
- `I.5.1.1-fr`: nilradical-sheaf proposition. For a quasi-coherent
  `O_X`-algebra `B`, there is a unique quasi-coherent `O_X`-module `N` whose
  stalk at each `x` is the nilradical of `B_x`; in the affine case it is the
  sheaf associated to the nilradical of the corresponding algebra. The
  statement is complete on p.127; proof dependencies are not inferred before
  their direct-authority admission on p.128.

Exact p.127 source coordinates are French `ega1-4-fr.tex` lines 619--682,
3,098 UTF-8 bytes / SHA-256
`24B57E6824B25F8BCA4C047840C56C1A041104ADA96ECC94A8434EBE07A33696`,
plus all 17 lines of new `ega1-5-fr.tex`, 681 bytes / SHA-256
`E4893706A6EFAEB40D74BECC0FFA3C7E32A1FB3FCA64374CC4B6F9EDCD17163C`.
Paired English coordinates are `ega1-4.tex` lines 371--413, 3,340 bytes /
SHA-256
`FF5067E17E8D9BC81A5E43E5774F3A4D0D29A0E20420F6F69E6FB5661857CC92`,
plus `ega1-5.tex` lines 1--12, 615 bytes / SHA-256
`9DAABBF45EDF88BCB9F91E1183143CE0937E725699616E4F5DC22472CA2A52E8`.
The two visible English notes are the only R58-to-R59 source delta; removing
each unique note replays the exact R58 `ega1-4.tex` at 33,373 bytes / SHA-256
`CE8036FF9EF584DD794C7D4925EA62FE7937229E57212873B1C25DE68F8715A5`.
The section-4 projection is line-identical to live lines 18--413 and the
section-5 projection is line-identical to live lines 1--12. Final cumulative
coordinates, exhaustive references, subject/formula/terminology indices, and
implication closure remain deferred to the stable cumulative reader.
