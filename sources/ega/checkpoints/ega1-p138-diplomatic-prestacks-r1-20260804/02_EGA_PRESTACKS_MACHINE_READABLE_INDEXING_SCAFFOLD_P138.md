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

## Incremental EGA I p.128 scaffold

- `I.5.1.1-fr`: proof-completion node. The nilradical of the localization
  `B_x` is the localization `N_x`: if `(z/s)^k=0`, some
  `t not-in j_x` satisfies `t z^k=0`, hence `(tz)^k=0` and
  `z/s=(tz)/(ts)` lies in `N_x`. Explicit dependency is
  `I.1.4.1-fr`; the localization/nilpotence calculation is retained as a
  typed proof edge rather than inferred from the English witness.
- `terminology:I.5.1.nilradical-fr`: terminology node. The constructed
  quasi-coherent module is the nilradical of the quasi-coherent
  `O_X`-algebra `B`; `N_X` denotes the nilradical of `O_X`.
- `I.5.1.2-fr`: reduced-subprescheme extremal node. The closed subprescheme
  defined by `N_X` is the unique reduced subprescheme with underlying space
  `X` and the least subprescheme with that underlying space. Explicit edges
  are `0.4.1.4-fr`, `I.4.1.3-fr`, `I.4.1.9-fr`, and
  `I.5.1.1-fr`.
- `source-error:I.5.1.2.word-order-fr`: printed word-order node. French
  prints ``du sous-preschema ferme defini Y par N_X'' where the typed order
  is ``du sous-preschema ferme Y defini par N_X''. Canonical French
  preserves print. English retains its inherited grammatical resolution by
  first introducing `Y`; no mathematical object or implication is changed.
- `I.5.1.3-fr`: definition node. `X_red` is the unique reduced
  subprescheme of `X` with underlying space `X`.
- `equivalence:I.5.1.3.reduced-fr`: defining-equivalence node. A prescheme
  `X` is reduced exactly when `X=X_red`.
- `I.5.1.4-fr`: affine spectrum criterion. `Spec(A)` is reduced
  (respectively integral) exactly when `A` is reduced (respectively
  integral). Explicit dependencies are `I.5.1.1-fr`, `I.2.1.7-fr`, and
  `I.1.1.13-fr`.
- `consequence:I.5.1.4.locally-integral-fr`: local-ring consequence and
  converse node. A locally integral prescheme has integral local rings. If
  the underlying space is locally Noetherian, integral local rings imply
  locally integral components; the proof separates the finitely many
  irreducible components of an affine Noetherian open. Explicit edges are
  `I.5.1.4-fr` and `I.1.1.14-fr`.
- `I.5.1.5-fr`: reduced-morphism construction begun on p.128. The
  diplomatic text ends at the exact printed fragment ``l'homomor-''; mark
  `continued=true`, `next_printed_page=129`, and
  `temporary_final_close=end-env`.
- `repair:I.5.1.2.ideal-subscript-en`: paired-English mathematical-notation
  repair. Direct French and the proof require the ideal itself in
  `mathfrak I subset mathfrak j_x`; inherited English incorrectly placed a
  stalk/localization subscript on the left. Removing that single `_x`
  restores the typed relation and its immediate universal-prime conclusion.
- `repair:I.5.1.3.signifie-means-en`: paired-English logical repair. French
  `signifie` states the defining equivalence; ``thus means'' replaces the
  inherited one-way ``thus implies'' wording.

Exact p.128 coordinates are French `ega1-5-fr.tex` lines 19--103,
4,409 UTF-8 bytes / SHA-256
`EF33E8767B2A9209D26CBF9C98CF24D563F0A3C333C53299FC92273C94C1989D`.
The inverse truncation to the first 681 bytes reproduces sealed p.127 at
SHA-256
`E4893706A6EFAEB40D74BECC0FFA3C7E32A1FB3FCA64374CC4B6F9EDCD17163C`.
Paired English coordinates are `ega1-5.tex` lines 15--68, 4,055 UTF-8 bytes /
SHA-256
`9AC0433B9DE07E35B77E1AF45C450C99285EBD7AB5E9312204594B51D6CF5955`.
Two unique inverse substitutions reproduce the exact R60 English source,
46,833 bytes / SHA-256
`1585EC164F57E55BA86264F86F428523D7659442AAE5046D43D9E5FA49B5F777`.
The p.128 bounded English projection is line-identical to live
`ega1-5.tex` lines 1--68; its wrapper supplies one temporary `end-env` after
the exact projection because `I.5.1.5` remains open at the page seam. Final cumulative
coordinates, exhaustive references, subject/formula/terminology indices,
and implication closure remain deferred to the stable cumulative reader.

## Incremental EGA I p.129 scaffold

- `I.5.1.5-fr`: reduced-morphism and functoriality node, completed from the
  p.128 seam. A morphism `f=(psi,theta):X to Y` carries nilpotents to
  nilpotents and induces `f_red:X_red to Y_red`. Composition satisfies
  `(g composed-with f)_red=g_red composed-with f_red`, so reduction is a
  covariant functor. The displayed square with the two injection morphisms is
  commutative. If `X` is reduced, every `f:X to Y` factors through
  `Y_red to Y`.
- `diagram:I.5.1.5.reduction-naturality-fr`: commutative-square node with
  top edge `f_red`, bottom edge `f`, and vertical injections
  `X_red to X`, `Y_red to Y`. It records naturality of the functorial
  reduction morphism rather than merely a visual coordinate.
- `I.5.1.6-fr`: preservation node. Surjectivity, radiciality, immersion,
  closed/open/local immersion, and local isomorphism pass from `f` to
  `f_red`; surjectivity and radiciality also pass back. Explicit proof-use
  edges are `I.3.5.8-fr`, `I.5.1.2-fr`, `I.4.2.2-fr`, and
  `I.5.5.12-fr`.
- `I.5.1.7-fr`: product/reduction node. The products
  `X_red times-sub-S_red Y_red` and `X_red times-sub-S Y_red` are identical
  and canonically form a subprescheme of `X times-sub-S Y` with the same
  underlying space. Explicit edges are `I.4.3.1-fr`, `I.5.1.5-fr`, and
  `I.3.2.4-fr`; the monomorphism `S_red to S` controls the base identity.
- `I.5.1.8-fr`: reduced-product comparison node. The reductions of
  `X times-sub-S Y` and `X_red times-sub-S_red Y_red` identify canonically.
  Explicit edges are `I.5.1.2-fr` and `I.5.1.7-fr`.
- `warning:I.5.1.8.reduced-product-nilpotents-fr`: warning node. A fibre
  product of reduced preschemes need not be reduced because a tensor product
  of reduced algebras can contain nilpotent elements.
- `english:I.5.1.p129-confirmation`: paired-English confirmation node. The
  direct-authority recheck requires no source mutation. Established English
  `omega-flat` and residue-field notation are retained, and the physical
  French `l'homomor-/phisme` split is normalized to one English word while
  keeping the p.129 marker at the same semantic continuation.

Exact p.129 coordinates are French `ega1-5-fr.tex` lines 103--190, 3,979
UTF-8 bytes / SHA-256
`B0D630DDBDC8D4A6597F12105E6314F0AD0415D40E65B8F192F207C71B696966`.
Replacing the unique p.129 marker-to-EOF region with one `end-env` line
reproduces sealed p.128 at 5,091 bytes / SHA-256
`EB37539C7AAD273C7A780E087FDB8863CD86A0C284D0BA532B72D395FC5860A0`.
Paired English coordinates are `ega1-5.tex` lines 69--125, 3,457 UTF-8
bytes / SHA-256
`1613516E5198693420370041667CE6EC2B8B2C67209B6501722684839729D779`.
The p.128 prefix plus p.129 continuation reproduce live lines 1--125 at
8,142 bytes / SHA-256
`9BEF395F1E37CFFC7819B25487C4A9F54B8505FE547E2131752EAB830A565B78`
with no balancing additions. Final cumulative coordinates, exhaustive
references, subject/formula/terminology indices, and implication closure
remain deferred to the stable cumulative reader.

## Incremental EGA I p.130 scaffold

- `I.5.1.9-fr`: nilpotent-thickening affineness proposition, begun on p.130.
  If a quasi-coherent ideal sheaf `J` is nilpotent and `X_0=(X,O_X/J)`, then
  `X` is affine exactly when `X_0` is affine.
- `reduction:I.5.1.9.square-zero-fr`: induction-reduction node. The proof
  replaces `X` successively by `X_k=(X,O_X/J^(k+1))` and reduces the theorem
  to the square-zero case `J^2=0`.
- `formula:I.5.1.9.1-fr`: exact-sequence target
  `0 to Gamma(X,J) to Gamma(X,O_X) to Gamma(X,O_X/J) to 0`. Surjectivity of
  `phi:A to A_0` is the remaining cohomological gate.
- `construction:I.5.1.9.global-ideal-fr`: square-zero ideal node.
  `K=Gamma(X,J)` is a square-zero ideal of `A` and an `A_0=A/K`-module;
  quasi-coherence on affine `X_0` gives `J isomorphic-to K-tilde` and
  `K_x=J_x`. Explicit dependency is `I.1.4.1-fr`.
- `construction:I.5.1.9.canonical-map-fr`: canonical comparison morphism.
  With `X-prime=Spec(A)`, the identity on `A=Gamma(X,O_X)` determines
  `f=(psi,theta):X to X-prime`. Explicit dependency is `I.2.2.4-fr`.
- `diagram:I.5.1.9.sections-fr`: commutative sections diagram with top row
  `A to Gamma(V,O_X|V)` and bottom row
  `A_0=A/K to Gamma(V,O_X0|V)` for affine open `V`.
- `diagram:I.5.1.9.closed-comparison-fr`: commutative closed-subprescheme
  square with horizontal maps `f` and `f_0` and vertical injection morphisms
  `j-prime` and `j`. The lower-left closed subprescheme is defined by
  `K-tilde`.
- `argument:I.5.1.9.five-lemma-fr`: isomorphism argument. Affineness of
  `X_0` makes `f_0` an isomorphism; equality of underlying maps makes `psi` a
  homeomorphism; the ideal and quotient restrictions of `theta-sharp` are
  isomorphisms, so the five lemma makes `theta-sharp`, hence `f`, an
  isomorphism.
- `continuation:I.5.1.9.cohomology-gate-fr`: the proof remains open at the
  exact printed words ``ce qui resultera de''; mark `continued=true` and
  `next_printed_page=131`. No temporary environment close is present.
- `english:I.5.1.p130-confirmation`: paired-English confirmation node. No
  source mutation is required. The inherited English marker keeps
  `H^1(X,I)=0` with its governing sentence on the p.130 side, while direct
  French places that formula on p.131; this page-boundary normalization is
  explicit and reversible.

Exact p.130 appended coordinates are French `ega1-5-fr.tex` bytes
9,061--12,517, a 3,457-byte suffix / SHA-256
`C27E7F6F0D0C4ACE819B4C536D7010DABFD498ABC0900BF1FE350D9DA3924E45`.
The unique marker-to-EOF region is 3,410 bytes / SHA-256
`5A44990E0600011BF267809CB2589F5FC277AD4744BBD2F54AEC1DA3B8BB6420`;
truncation to the first 9,060 bytes reproduces sealed p.129 at SHA-256
`D3DEC590DD38DE0A1CB5F756F7970AC4434CF1E5521379855BCC0592B4E7941C`.
Paired English p.130 marker coordinates are `ega1-5.tex` lines 129--177,
3,128 bytes / SHA-256
`2B906A89E896C7D417052B1F1DC0DC899E26714B0D8B75605169AEF5C672A563`.
The exact build continuation is live lines 126--177, 3,172 bytes / SHA-256
`AB1B318C93CEB0F2CA17E6DF96C5C438F27AD5E4390D296E67BB0F6A4B2EEC56`;
together with prior projections it reproduces lines 1--177 at 11,314 bytes /
SHA-256
`C48CBD81D34FB48E0B8756F6B9C23960B3E207A466FD68C54FF69787F2E51D08`
with no balancing additions. Final cumulative coordinates, exhaustive
references, subject/formula/terminology indices, and implication closure
remain deferred to the stable cumulative reader.

## Incremental EGA I p.131 scaffold

- `I.5.1.9.2-fr`: affine cohomology-vanishing lemma. For an affine scheme
  `Y` and a quasi-coherent `O_Y`-module `F`, `H^1(Y,F)=0`. The proof records a
  future dependency on EGA III, section 1, and gives the independent
  extension-class route through `T.4.2.3`, `0.5.4.9-fr`, and
  `I.1.3.11-fr`.
- `error:I.5.1.9.2.restriction-fr`: printed-source error node. In the local
  splitting of `G|V`, French prints `F|Y direct-sum O_Y|V`; the restriction
  required on the neighbourhood is `F|V`. Diplomatic French preserves the
  printed term. English retains the type-correct `F|V` and now exposes the
  intervention in one reversible translator footnote.
- `I.5.1.9-fr`: completion node. The p.130 cohomology gate closes by applying
  `I.5.1.9.2-fr` to the quasi-coherent `O_X0`-module `J`; the exact sequence
  and affineness proof are therefore complete.
- `I.5.1.10-fr`: nilpotent-nilradical corollary. If `N_X` is nilpotent, `X`
  is affine exactly when `X_red` is affine. Explicit dependency is
  `I.5.1.9-fr`.
- `subsection:I.5.2-fr`: existence and uniqueness of reduced subpreschemes
  with prescribed locally closed underlying space.
- `I.5.2.1-fr`: unique-reduced-subprescheme proposition. For locally closed
  `Y` in the underlying space of `X`, there is exactly one reduced
  subprescheme with underlying space `Y`. The affine construction uses the
  radical ideal `j(Y)` and glues by uniqueness. Explicit dependencies are
  `I.5.1.2-fr` and `I.1.1.4-fr`.
- `I.5.2.2-fr`: closed-factorization proposition. A morphism from reduced
  `X` whose image lies in a closed subprescheme `Z` factors through `Z`.
  Explicit dependencies are `I.4.4.1-fr` and `I.5.1.2-fr`.
- `I.5.2.3-fr`: reduced-closure corollary statement. If `X` is a reduced
  subprescheme of `Y` and `Z` is the reduced closed subprescheme underlying
  `closure(X)`, then `X` is induced on an open subset of `Z`. Mark
  `continued=true`; its proof begins on printed p.132.
- `english:I.5.1-5.2.p131-confirmation`: paired-English correction node. The
  only p.131 source mutation is the visible footnote on `F|V`; its unique
  removal reproduces R66. The inherited English page seam keeps
  `H^1(X,I)=0` immediately before the p.131 marker, and that physical
  placement remains explicit and reversible.

Exact p.131 appended coordinates are French `ega1-5-fr.tex` bytes
12,518--16,480, a 3,963-byte suffix / SHA-256
`35023EDB16116F0E9B7818692F2E393671D0DEC682274B353C44210747E0D9C3`.
The unique marker-to-EOF region is 3,962 bytes / SHA-256
`024197841460D9454B35C6118D0D49528F982FCA4C212646E0285FD8894BD422`;
truncation to the first 12,517 bytes reproduces sealed p.130 at SHA-256
`4F6DDD36624D115FF3571344674D5B3D49E101F4851D2E634ED094359F3DC7A2`.
Paired English p.131 coordinates are `ega1-5.tex` lines 178--238, 3,856
bytes / SHA-256
`B8C9CC0121AC191F2AA7585204797D1E398BEA228B74EF5D9F5F6B27E6AFB4B8`.
Together with the preceding projections they reproduce live lines 1--238 at
15,170 bytes / SHA-256
`011C647717CF82BC45CA3AA9C41A60AAFBE410FE779DD0D1DB9C1BDE67F124AD`
with no balancing additions. Final cumulative coordinates, exhaustive
references, subject/formula/terminology indices, and implication closure
remain deferred to the stable cumulative reader.

## Incremental EGA I p.132 scaffold

- `I.5.2.3-fr`: completion node. Choose an open `U` of `Y` with
  `X=U intersect closure(X)`; `I.5.2.2-fr` makes reduced `X` a subprescheme
  of the reduced closed `Z`, and uniqueness `I.5.2.1-fr` identifies it with
  the subprescheme induced by `Z` on the open subspace `X`.
- `I.5.2.4-fr`: ideal-pullback corollary. For closed subpreschemes `X-prime`
  and `Y-prime` defined by quasi-coherent ideals `J` and `K`, if `X-prime`
  is reduced and maps into `Y-prime`, then `f^*(K)O_X subset J`. Explicit
  dependencies are `I.5.2.2-fr` and `I.4.4.6-fr`.
- `subsection:I.5.3-fr`: diagonal and graph of a morphism.
- `I.5.3.1-fr`: diagonal-morphism definition. `Delta_(X|S)` is the unique
  `S`-morphism from `X` to `X times_S X` whose composites with both
  projections are `1_X`.
- `formula:I.5.3.1.1-fr`: projection identities
  `p_1 o Delta_X = p_2 o Delta_X = 1_X`. Explicit dependency is
  `I.3.2.1-fr`.
- `formula:I.5.3.1.2-fr`: pairing-through-diagonal identity
  `(f,g)_S = (f times_S g) o Delta_(T|S)`.
- `portability:I.5.3.1-fr`: categorical portability node. Items 5.3.1--5.3.8
  require only the existence of the products they use.
- `I.5.3.2-fr`: product-diagonal proposition. Under the canonical product
  identification, `Delta_(X times Y)` is `Delta_X times Delta_Y`; the proof
  checks both projections.
- `numbering-gap:I.5.3.3-fr`: printed-numbering discontinuity node. Direct
  French authority jumps from 5.3.2 to 5.3.4. No French 5.3.3 text is
  invented. The inherited English empty `I.5.3.3` environment rendered a
  stray period and is replaced by a non-rendering `phantomsection` anchor
  that retains only the compatibility label.
- `I.5.3.4-fr`: base-extension compatibility of the diagonal:
  `Delta_(X_(S-prime))` identifies canonically with
  `(Delta_X)_(S-prime)`. Explicit dependency is `I.3.3.10-fr`.
- `I.5.3.5-fr`: change-of-base diagonal proposition, begun on p.132. The
  structural maps and projections form diagram `I.5.3.5.1-fr` from
  `X times_S Y` to `X times_T Y` over `S to S times_T S`.
- `error:I.5.3.5.missing-g-fr`: printed-source omission node. French prints
  `f:X to S, Y to S` without naming the second structure morphism; the
  immediately following identity `pi=f o p=g o q` and the diagram require
  `g:Y to S`. Diplomatic French preserves the omission. English retains the
  type-complete reading and exposes it in one reversible translator footnote.
- `continuation:I.5.3.5-fr`: p.132 ends after diagram 5.3.5.1, before
  ``est commutatif''. Mark `continued=true`, `next_printed_page=133`, and
  `temporary_final_env_close=true`; remove only that final
  `end-proposition` before continuing.
- `english:I.5.2-5.3.p132-confirmation`: paired-English correction node. The
  p.132 source mutations are the visible missing-`g` footnote and removal of
  the stray period by replacing the empty 5.3.3 environment with a
  non-rendering anchor. Removing the footnote and restoring the former empty
  environment reproduces R68. The source-grounded p.132 slice is live lines
  239--320, with one build-only `end-proposition` balancing the open seam.

Exact p.132 appended coordinates are French `ega1-5-fr.tex` bytes
16,481--19,923, a 3,443-byte suffix / SHA-256
`E1DD07F18D2B412BDB99DCF905FC14A6199C182E4F48B955F4F61F3A35510DB9`.
The unique marker-to-EOF region is 3,442 bytes / SHA-256
`F81B9107A2C068052156AA5C867DDB9131E5FA68E4CF91A6002F9432DA280F0F`;
truncation to the first 16,480 bytes reproduces sealed p.131 at SHA-256
`C6F64E7AD05183672B3F709BE452A0EA0EA3D5013030AE0A03792D3D0B85B6EA`.
Paired English p.132 marker coordinates are `ega1-5.tex` lines 240--320,
3,565 bytes / SHA-256
`C6EC16CAA72F0C963CE6D8207763528045861CB11B38C204EE12DC2F2E90A491`.
The exact build continuation is live lines 239--320 plus one temporary final
`end-proposition`, 3,597 bytes / SHA-256
`A371A89C1EEF3922B618F0BC32E0F005A1E667F752B57844267BB48ECD26F773`;
together with prior projections it reproduces live lines 1--320 plus that one
balancing close at 18,767 bytes / SHA-256
`AE7E802D9469D2B54CB700487F46FFB1B9CC80EE7F298522EF62FFB7E76A67A8`.
Final cumulative coordinates, exhaustive references,
subject/formula/terminology indices, and implication closure remain deferred
to the stable cumulative reader.


## Incremental EGA I p.133 scaffold

- `I.5.3.5-fr`: completion node. Diagram 5.3.5.1 is cartesian: it identifies
  `X times_S Y` with the product of the `(S times_T S)`-preschemes `S` and
  `X times_T Y`, with projections `pi` and `(p,q)_T`. The proof reduces via
  `I.3.4.3-fr` to the corresponding set-theoretic statement.
- `I.5.3.6-fr`: base-diagonal pullback identification. With
  `P=S times_T S`, `(p,q)_T` identifies with
  `1_(X times_T Y) times_P Delta_S`. Explicit dependencies are
  `I.5.3.5-fr` and `I.3.3.4-fr`.
- `I.5.3.7-fr`: graph-diagonal cartesian square. For an `S`-morphism
  `f:X to Y`, the square formed by `(1_X,f)_S`, `f`, `f times_S 1_Y`, and
  `Delta_Y` identifies `X` with the relevant product. Explicit dependencies
  are `I.5.3.5-fr` and `I.3.3.3-fr`.
- `I.5.3.8-fr`: monomorphism criterion. `f:X to Y` is a monomorphism exactly
  when `Delta_(X|Y):X to X times_Y X` is an isomorphism. The functor-of-points
  proof uses `I.3.4.3.1-fr`.
- `error:I.5.3.8.one-element-fr`: printed-source imprecision. French says
  that `X(Z)_Y` is likewise reduced to one element after mapping injectively
  into the singleton `Y(Z)_Y`; the valid conclusion is at most one element,
  since `X(Z)_Y` may be empty. Diplomatic French preserves the wording.
  English retains the type-correct statement and exposes it in one reversible
  translator footnote.
- `I.5.3.9-fr`: diagonal-immersion proposition. `Delta_X` is an immersion
  into `X times_S X`; the proof combines the homeomorphism onto its image with
  surjectivity on stalks. Explicit dependency is `I.4.2.2-fr`.
- `term:I.5.3.diagonal-fr`: the subprescheme associated to the immersion
  `Delta_X` is called the diagonal of `X times_S X`. Explicit dependency is
  `I.4.2.1-fr`.
- `I.5.3.10-fr`: canonical-immersion corollary. Under 5.3.5, `(p,q)_T` is an
  immersion and is called the canonical immersion of `X times_S Y` into
  `X times_T Y`. Explicit dependencies are `I.5.3.6-fr` and `I.4.3.1-fr`.
- `I.5.3.11-fr`: graph-immersion corollary. For an `S`-morphism `f:X to Y`,
  `Gamma_f=(1_X,f)_S` is an immersion of `X` into `X times_S Y`. Explicit
  dependencies are `I.3.3.14-fr`, `I.5.3.10-fr`, and `I.5.3.7-fr`.
- `english:I.5.3.p133-confirmation`: paired-English correction node. The sole
  p.133 source mutation is the visible at-most-one-element footnote; its
  unique removal reproduces R71. The p.132 temporary projection close is
  retired by using the exact combined live slice through p.133.

Exact p.133 French replacement coordinates are `ega1-5-fr.tex` bytes
19,906--23,519, the unique marker-to-EOF region of 3,614 bytes / SHA-256
`9D8475E0BB535C2061A1A1A6F860A339C911E31E7C530987C66ED99AD1AB78FD`.
Replacing that region with the 18-byte terminal `end-proposition` reproduces
sealed p.132 at 19,923 bytes / SHA-256
`EE969AFC8501A89A9D5A079E7A9503FD2D355E89C557F97D50825C806D2A0FAC`.
Paired English p.133 marker coordinates are `ega1-5.tex` lines 321--401,
3,713 bytes / SHA-256
`0F8884F778BD6E84AE70F4812688FB99511FB1D4ADE1E9F6BE7868CAD3A946CF`.
The exact build continuation is live lines 239--401, 7,292 bytes / SHA-256
`509C0BCCBE4B7FA86F642D2032B36BD63C662DBF70881E85E1C47A04F91B543F`;
together with prior projections it reproduces live lines 1--401 at 22,462
bytes / SHA-256
`20C09CBE4E058340D3E23C26C6377233C358FFA49CB706EDF5F2E62341DA9187`
with no balancing additions. Final cumulative coordinates, exhaustive
references, subject/formula/terminology indices, and implication closure
remain deferred to the stable cumulative reader.
## Incremental EGA I p.134 scaffold

- `provenance:EGA-I-p134-fr`: direct-authority page node. Source is NUMDAM EGA
  I PDF one-based p.133 / printed p.134, verified against the one bounded
  context image at SHA-256
  `6D57CB50CF18A51FF996D8F71D10516D12E499365B62F2EA8F3B6DAF25F40F8A`
  and the existing PDF text layer at SHA-256
  `0C92D2FD88D9CD2D20856DC272C78A46A53853504F48EC418878269666980992`.
  Method is direct visual reading plus non-OCR text-layer confirmation;
  `confidence=high` and `unresolved_reading_count=0`.
- `term:I.5.3.graph-fr`: graph-subprescheme definition. The subprescheme of
  `X times_S Y` associated to the graph immersion `Gamma_f` is the graph of
  `f`. Definition-use edges are `I.5.3.11-fr -> term:I.5.3.graph-fr` and
  `I.4.2.1-fr -> term:I.5.3.graph-fr`.
- `criterion:I.5.3.graph-fr`: graph characterization. A subprescheme `G` of
  `X times_S Y` is a graph exactly when the restricted first projection is an
  isomorphism `g:G to X`; the represented morphism is
  `p_2 composed_with g^-1`. Parent scope is `term:I.5.3.graph-fr`.
- `term:I.5.3.S-section-image-fr`: when `X=S`, `S`-morphisms `S to Y` are
  their graph morphisms. Their graph subpreschemes are called the images of
  the sections and, by the printed abuse of language, the `S`-sections of
  `Y`. Explicit dependency is `I.2.5.5-fr`.
- `I.5.3.12-fr`: graph/base-change compatibility. For `g:S-prime to S` and
  the pullback `f-prime` of `f`, `Gamma_(f-prime)` is the pullback of
  `Gamma_f` by `g`. Typed edges are `base_change_of` to `I.5.3.11-fr` and
  `proof_uses` to `I.3.3.7-fr` and `I.3.3.10.1-fr`.
- `I.5.3.13-fr`: immersion cancellation through composition. If
  `g composed_with f` is an immersion (respectively local immersion), then
  `f` is likewise. Dependencies are `I.3.3.4-fr`, `I.4.3.1-fr`,
  `I.4.5.5-fr`, `I.5.3.11-fr`, and `I.4.2.4-fr`.
- `formula:I.5.3.13.factorization-fr`: the proof factors
  `f:X to Y` as
  `X --Gamma_f--> X times_Z Y --p_2--> Y` and identifies `p_2` with
  `(g composed_with f) times_Z 1_Y`. Parent is `I.5.3.13-fr`.
- `I.5.3.14-fr`: pair-morphism immersion corollary. For `S`-morphisms
  `j:X to Y` and `g:X to Z`, immersion (respectively local immersion) of
  `j` implies the same for `(j,g)_S`. Its proof factors
  `j=p composed_with (j,g)_S` and uses `I.5.3.13-fr`.
- `I.5.3.15-fr`: functoriality of the diagonal under an `S`-morphism
  `f:X to Y`. The square `I.5.3.15.1-fr` commutes; the text identifies this
  with `Delta_X` being functorial in the category of preschemes.
- `diagram:I.5.3.15.1-fr`: commutative square with horizontal maps
  `Delta_X` and `Delta_Y` and vertical maps `f` and `f times_S f`. Typed
  edges are `expresses` to `I.5.3.15-fr` and `used_by`
  `I.5.3.16-fr`.
- `I.5.3.16-fr`: diagonal-subprescheme intersection corollary. For a
  subprescheme `X` of `Y`, `Delta_X(X)` is a subprescheme of `Delta_Y(Y)`
  with underlying space
  `Delta_Y(Y) intersect p_1^-1(X) = Delta_Y(Y) intersect p_2^-1(X)`.
  The proof uses `I.5.3.15-fr` and `I.4.3.1-fr`.
- `formula:I.5.3.16.intersection-fr`: the two equal diagonal intersections
  in `Y times_S Y`. Parent is `I.5.3.16-fr`; comparison edges join the two
  projection preimages.
- `continuation:I.5.3.16-fr`: printed p.134 ends in the proof after
  `z in Delta_Y(Y) intersect p_1^-1(X)` and
  `z=Delta_Y(y)`. Mark `continued=true`,
  `next_printed_page=135`, and `temporary_final_env_close=false` in French.
  The English bounded projection requires exactly one build-only `end-proof`.
- `english:I.5.3.p134-confirmation`: direct paired-English recheck node.
  Existing live lines 402--472 are source-grounded with no mutation; R74
  exactly preserves the R73-gated 127-file tree. The sole projection-only
  operation is the reversible closing of the proof opened at live line 470.

Exact p.134 French append coordinates are `ega1-5-fr.tex` bytes
23,520--27,093, a 3,574-byte suffix / SHA-256
`EEB829591264986666DBBD5263B58BADCA8122A168BF721A6186DDACDCB9582D`.
The p.134 marker begins at byte 23,521; marker-to-EOF is 3,573 bytes /
SHA-256
`BD738E67ABDD444C2EC478FE9854A62F64CCC687D3E18E980CA39A32DE3DEBE9`.
Truncation to the first 23,519 bytes reproduces sealed p.133 at SHA-256
`DC5D2863A197CE33C9AAC314696ABDD36E840183D8DA735ACE6E99613A60FB91`.
Paired English p.134 marker coordinates are `ega1-5.tex` lines 402--472,
3,396 bytes / SHA-256
`204DBB914F7B0045FE07843421E7F0BFFE2C989253DB9511DAD43889ADD6E9DD`.
The exact build continuation is live lines 239--472 plus one build-only
`end-proof`, 10,700 bytes / SHA-256
`9399F92A8CC4F49BCD546E3C693F9BF0851B260CA3F0FD3F717EF2D66CD3ED33`;
together with prior projections the live source reproduces lines 1--472 at
25,858 bytes / SHA-256
`CADC842FB7FBAC8C4104D1A3DCE490EC14DD5DDF59ED07D87F7031C1EB4575CA`
before that one balancing close. Final cumulative coordinates, exhaustive
references, subject/formula/terminology indices, and implication closure
remain deferred to the stable cumulative reader.
## Incremental EGA I p.135 scaffold

- `provenance:EGA-I-p135-fr`: direct-authority page node. Source is NUMDAM EGA
  I PDF one-based p.134 / printed p.135, verified against the one bounded
  context image at SHA-256
  `AA876A55EC9FD2FE0B3140B0F00AB9031D7C0D1909146B1B2396CD508126BB0A`
  and the existing PDF text layer at SHA-256
  `F2957B8386662FC62E68EA0A528DC4A22B002E41E1FCCD61E5B6F8EB858E606C`.
  Method is direct visual reading plus non-OCR text-layer confirmation;
  `confidence=high` and `unresolved_reading_count=0`.
- `completion:I.5.3.16-fr`: p.135 closes the diagonal-intersection proof.
  From `z=Delta_Y(y)` it obtains `y=p_1(z) in X`, uses the printed
  identification `y=f(y)`, and invokes commutativity of
  `diagram:I.5.3.15.1-fr` to place `z=Delta_Y(f(y))` in `Delta_X(X)`.
  Typed edges are `completes -> I.5.3.16-fr` and
  `proof_uses -> diagram:I.5.3.15.1-fr`.
- `I.5.3.17-fr`: residue-field diagonal criterion. If two `S`-morphisms
  `f_1,f_2:Y to X` agree at `y` and induce the same map
  `k(x) to k(y)`, then `(f_1,f_2)_S(y)` lies on `Delta_(X|S)(X)`.
  Hypotheses, conclusion, and point `x=f_1(y)=f_2(y)` are explicit.
- `diagram:I.5.3.17.residue-square-fr`: generic commutative square for
  `g_i:Spec(k(y)) to Spec(k(x))` over `f_i:Y to X`. Parent is
  `I.5.3.17-fr`; the two instances correspond to `i=1,2`.
- `diagram:I.5.3.17.pair-square-fr`: commutative square comparing
  `(g_1,g_2)_S` with `(f_1,f_2)_S`. Equality `g_1=g_2` places the unique
  point of `Spec(k(y))` on the top diagonal; `I.5.3.15-fr` transfers the
  conclusion to `X times_S X`.
- `term:I.5.4.separated-morphism-fr`: a morphism `f:X to Y` is separated
  exactly when `Delta_(X|Y):X to X times_Y X` is a closed immersion.
  Definition owner is `I.5.4.1-fr`.
- `term:I.5.4.Y-scheme-fr`: historical EGA terminology. A prescheme
  separated over `Y` is also called a `Y`-scheme; a prescheme separated over
  `Spec(Z)` is called a scheme. The French wording is preserved
  diplomatically, with forward dependency `I.5.5.7-fr`.
- `criterion:I.5.4.1.closed-diagonal-space-fr`: by `I.5.3.9-fr`,
  separatedness over `Y` is equivalent to `Delta_X(X)` being a closed
  subspace of the underlying space of `X times_Y X`.
- `english:I.5.4.1.historical-terminology-note`: visible inherited
  translator-paratext node. The English footnote explains the early
  prescheme/scheme nomenclature; it is not French source and is retained
  explicitly rather than silently attributed to the author.
- `I.5.4.2-fr`: closed canonical-immersion proposition. If `S to T` is
  separated and `X,Y` are `S`-preschemes, then
  `X times_S Y to X times_T Y` is a closed immersion. Proof dependencies are
  `I.5.3.5.1-fr`, `I.5.3.10-fr`, and `I.4.3.2-fr`.
- `formula:I.5.4.2.base-change-fr`: the proof realizes `(p,q)_T` as the
  base change of `Delta_(S|T)` along
  `f times_T g:X times_T Y to S times_T S`. Parent is `I.5.4.2-fr`.
- `I.5.4.3-fr`: closed graph corollary. For an `S`-scheme `Y` and an
  `S`-morphism `f:X to Y`, `Gamma_f:X to X times_S Y` is a closed
  immersion. Typed edges are `special_case_of -> I.5.4.2-fr` and
  `uses_definition -> term:I.5.3.graph-fr`.
- `I.5.4.4-fr`: separated cancellation corollary. For
  `f:X to Y` and separated `g:Y to Z`, closed immersion of
  `g composed_with f` implies closed immersion of `f`. The printed proof
  comparison links `I.5.4.3-fr` to `I.5.3.13-fr` via `I.5.3.11-fr`.
- `english:I.5.p135-confirmation`: direct paired-English recheck node.
  Existing live lines 473--551 are source-grounded with no mutation; R76
  exactly preserves the R75-gated 127-file tree.

Exact p.135 French append coordinates are `ega1-5-fr.tex` bytes
27,094--30,547, a 3,454-byte suffix / SHA-256
`1E124A848F2701CEF32A1409EF733137892FE2AE4043DCF8A66904AF125C9A33`.
The p.135 marker begins at one-based byte 27,095; marker-to-EOF is 3,453
bytes / SHA-256
`2777E902C9828353AC86BD2BC537B6178799FDD2DD0D68CF5EC891AD46FE896C`.
Truncation to the first 27,093 bytes reproduces sealed p.134 at SHA-256
`2BF15FE97B29DE032BB338E83897243673A7CC9C5956049AB1A29E195281DC2F`.
Paired English p.135 marker coordinates are `ega1-5.tex` lines 473--551,
3,556 bytes / SHA-256
`447A72CE618908E7009F8CA09640955AA57E35BC3FFED3E57F1E6E7F6906ACD0`.
The exact build continuation is live lines 239--551, 14,244 bytes / SHA-256
`DEA714B7DC7D922B851FF8CB629CD13E46F9A0CB0666DCE0CF92B8119457E779`
with no balancing additions; together with prior projections the live source
reproduces lines 1--551 at 29,414 bytes / SHA-256
`95B44FEFCE90A788F99BBFE5226ED73B3F2F669CC3BD63CA3D1BCEDC3E11E344`.
Final cumulative coordinates, exhaustive references,
subject/formula/terminology indices, and implication closure remain deferred
to the stable cumulative reader.
## Incremental EGA I p.136 scaffold

- `provenance:EGA-I-p136-fr`: direct-authority page node. Source is NUMDAM EGA
  I PDF one-based p.135 / printed p.136, verified against the one bounded
  context image at SHA-256
  `E0116F6D3509552A6308EBD99DABAFAD63D60ECCCB12EF1907415E734085921E`
  and the existing PDF text layer at SHA-256
  `BA752752DA446DD2EB32AD4805E51487FBA656F82664EE7D81F9AA6692529106`.
  Method is direct visual reading plus non-OCR text-layer confirmation;
  `confidence=high` and `unresolved_reading_count=0`.
- `I.5.4.5-fr`: closed pair-morphism corollary. If `Z` is an `S`-scheme and
  `j:X to Y` is a closed immersion, then
  `(j,g)_S:X to Y times_S Z` is a closed immersion. The printed proof
  comparison uses `I.5.4.4-fr`, `I.5.3.14-fr`, and `I.5.3.13-fr`.
- `I.5.4.6-fr`: closed-section corollary. Every `S`-section of an `S`-scheme
  is a closed immersion. Typed dependencies are `I.2.5.5-fr` and
  `I.5.4.5-fr`, applied to `phi composed_with psi=1_S`.
- `I.5.4.7-fr`: generic-point uniqueness of sections. Over an integral
  prescheme `S` with generic point `s`, two sections of an `S`-scheme that
  agree at `s` agree globally. The proof uses equality of
  `k(x) to k(s)` maps, `I.5.3.17-fr`, closure
  `S=closure({s})`, and factorization through the closed diagonal by
  `I.5.2.2-fr`.
- `formula:I.5.4.7.diagonal-factorization-fr`: with
  `h=(f,g)_S` and `Z=Delta_X(X)`, the proof factors
  `S to Z to X times_S X` and concludes `f=g` by definition of the
  diagonal. Parent is `I.5.4.7-fr`.
- `I.5.4.8-fr`: three converse separatedness observations. The nodes test
  `I.5.4.3-fr` at `f=1_Y`, `I.5.4.5-fr` on
  `Y --Delta_Y--> Y times_Z Y --p_1--> Y`, and `I.5.4.6-fr` on the
  `Y`-section `Delta_Y` of `Y times_S Y to Y`.
- `I.5.5.1-fr`: six-part separation-criteria proposition. Statement subnodes
  are `I.5.5.1.i-fr` monomorphisms, `I.5.5.1.ii-fr` composition,
  `I.5.5.1.iii-fr` products, `I.5.5.1.iv-fr` base change,
  `I.5.5.1.v-fr` cancellation from a separated composite, and
  `I.5.5.1.vi-fr` invariance under reduction.
- `I.5.5.1.i-fr` has proof edge `proof_uses -> I.5.3.8-fr`.
- `diagram:I.5.5.1.1-fr`: triangular diagonal diagram
  `X -> X times_Z X` through `X times_Y X`, with maps
  `Delta_(X|Z)`, `Delta_(X|Y)`, and canonical immersion `j`. It expresses
  the composition proof for `I.5.5.1.ii-fr` and uses
  `I.5.3.10-fr`, `I.5.4.2-fr`, and `I.4.2.4-fr`.
- `continuation:I.5.5.1-fr`: printed p.136 ends inside the proof of item
  `(ii)` at the words `ce qui`. Mark `continued=true`,
  `next_printed_page=137`, and `temporary_final_env_close=false` in French.
  The English bounded projection requires exactly one build-only
  `end-proof`.
- `english:I.5.p136-confirmation`: direct paired-English recheck node.
  Existing live lines 552--621 are source-grounded with no mutation; R78
  exactly preserves the R77-gated 127-file tree.

Exact p.136 French append coordinates are `ega1-5-fr.tex` bytes
30,548--34,221, a 3,674-byte suffix / SHA-256
`8DA69EAF0AAB88FFFC45A9A0F8A6D95215ABC96578B798C51528827ADD4A677B`.
The p.136 marker begins at one-based byte 30,549; marker-to-EOF is 3,673
bytes / SHA-256
`8CE157BFD7AD62E057D10CF143B51EF6EA27A69744EFC54A1D24D66FB8983615`.
Truncation to the first 30,547 bytes reproduces sealed p.135 at SHA-256
`E1DBCD8A7DEF99161EE00A439D8BC4C1144D57B79DAB4853B0BDC80716B350F5`.
Paired English p.136 marker coordinates are `ega1-5.tex` lines 552--621,
3,461 bytes / SHA-256
`FF6AE4299248F4ED0B7B10A1229B6687A93A87A5A5D538ACEDEACF0501DE2E10`.
The exact live build prefix is lines 239--621, 17,705 bytes / SHA-256
`C9D2F72175A81BC1B564BA588ECB72D1EE564D2EC44AF09C87ED8AF773096189`;
adding one build-only `end-proof` produces the 17,717-byte projection at
SHA-256
`9892021E9733F25826BA7B8F6B7C259CDA98759113F13BDCD2D79225657D38A4`.
Together with prior projections the live source reproduces lines 1--621 at
32,875 bytes / SHA-256
`FD22AA54585F562274BD911873E332C6411E9104214D63E7E3B373100651D2F6`
before that one balancing close. Final cumulative coordinates, exhaustive
references, subject/formula/terminology indices, and implication closure
remain deferred to the stable cumulative reader.
## Incremental EGA I p.137 scaffold

- `provenance:EGA-I-p137-fr`: direct-authority page node. Source is NUMDAM EGA
  I PDF one-based p.136 / printed p.137, verified against the one bounded
  context image at SHA-256
  `85D4DC363A051C5EA7D369D41B0756B13FB29BBC286EF1F77505E32A2B3A109E`
  and the existing PDF text layer at SHA-256
  `58F824549A3718171C76DFF77DAFE5CC6DDFE3033A48ED601BC200C5EE713350`.
  Method is direct visual reading plus non-OCR text-layer confirmation;
  `confidence=high`, `unresolved_reading_count=0`, and
  `catalogued_author_error_count=0`.
- `proof:I.5.5.1.ii-fr`: completion of composition separatedness. The
  triangular diagonal factorization from p.136 closes the proof through
  `proof_uses -> I.5.4.2-fr` and `proof_uses -> I.4.2.4-fr`.
- `formula:I.5.5.1.iv-base-change-fr`: canonical identification
  `X_(S') times_(Y_(S')) X_(S') = (X times_Y X) times_Y Y_(S')`, under which
  the diagonal is `Delta_X times_Y 1_(Y_(S'))`. Typed dependencies are
  `I.3.5.1-fr`, `I.3.3.11-fr`, `I.3.3.9.1-fr`, and `I.4.3.1-fr`; parent is
  `I.5.5.1.iv-fr`.
- `proof:I.5.5.1.v-fr`: cancellation proof through the graph factorization
  `X --Gamma_f--> X times_Z Y --p_2--> Y`, with
  `p_2=(g composed_with f) times_Z 1_Y`. It uses
  `I.5.3.13-fr`, `I.5.5.1.iii-fr`, `I.5.5.1.i-fr`, and
  `I.5.5.1.ii-fr`.
- `diagram:I.5.5.1.reduction-fr`: unnumbered commutative square from
  `X_red` to `X_red times_Y X_red` above `X` to `X times_Y X`; vertical maps
  are `j` and `j times_Y j`, the top label is `Delta_(X_red)`, and the bottom
  `Delta_X` label is on the lower side of its arrow. Parent is
  `I.5.5.1.vi-fr`.
- `proof:I.5.5.1.vi-fr`: invariance under reduction uses the canonical
  identification of `X_red times_(Y_red) X_red` with
  `X_red times_Y X_red`, the preceding square, and the fact that both
  vertical arrows are homeomorphisms on underlying spaces. Dependencies are
  `I.5.1.7-fr`, `I.5.3.15-fr`, and `I.4.3.1-fr`.
- `I.5.5.2-fr`: restriction corollary. A separated morphism remains separated
  on every subprescheme of its source; proof edges target
  `I.5.5.1.i-fr` and `I.5.5.1.ii-fr`.
- `I.5.5.3-fr`: product-over-source corollary. If `Y` is separated over `S`,
  then `X times_S Y` is separated over `X`; proof edge targets
  `I.5.5.1.iv-fr`.
- `I.5.5.4-fr`: finite closed-cover criterion. Hypotheses are a prescheme
  `X`, a finite closed cover `(X_k)_(1<=k<=n)`, reduced induced preschemes
  `X_k`, closed subsets `Y_k` containing `f(X_k)`, reduced induced
  preschemes `Y_k`, and factorizations
  `X_k --f_k--> Y_k --> Y`. Conclusion is
  `f separated iff every f_k separated`. Construction dependencies are
  `I.5.2.1-fr` and `I.5.2.2-fr`.
- `formula:I.5.5.4.diagonal-cover-fr`: for projections `p_1,p_2` of
  `X times_Y X`, the proof uses
  `Delta_(X_k)(X_k) = Delta_X(X) intersect p_1^(-1)(X_k)` in the underlying
  space. Parent is `I.5.5.4-fr`; comparison edge targets `I.5.3.16-fr`.
- `proof:I.5.5.4-fr`: necessity uses clauses (i), (ii), and (v) of
  `I.5.5.1-fr`. Sufficiency makes every diagonal piece closed and uses the
  finite union `union_k Delta_(X_k)(X_k)=Delta_X(X)`.
- `comparison:I.5.5.4.integral-reduction-fr`: choosing the `X_k` as the
  irreducible components and compatible `Y_k` as irreducible components
  reduces separatedness to integral preschemes. Edges target
  `0.2.1.5-fr`, `I.5.5.4-fr`, and `I.2.1.7-fr`; this is a mathematical
  reduction, not merely a conceptual suggestion.
- `english-repair:I.5.p137.ref-3.3.9.1`: visible citation `(3.3.9.1)` now
  targets exact label `I.3.3.9.1` rather than parent `I.3.3.9`.
- `english-repair:I.5.p137.diagram-delta-side`: the lower horizontal
  `Delta_X` label in the reduction square now uses the source-faithful lower
  side. No object, arrow, or formula changed.
- `english-repair:I.5.p137.reduction-strength`: inherited “leads to the idea
  of separation” is replaced by “therefore reduces ... the notion of
  separation,” restoring the implication strength of French `ramène`.
- `english:I.5.p137-confirmation`: after those three reversible repairs, live
  lines 622--680 are source-grounded. R80 changes exactly
  `ega1/ega1-5.tex` from the R79-gated 127-file tree.

Exact p.137 French append coordinates are `ega1-5-fr.tex` bytes
34,222--38,044, a 3,823-byte suffix / SHA-256
`804E027A1BCA48480DE29FC8B4B45436BA00B2A588C0042A93B21E64EC50EF91`.
The p.137 marker begins at one-based byte 34,223; marker-to-EOF is 3,822
bytes / SHA-256
`2923B7C0294AA85C665F4F10E45081D2859EE51B2065882ABDEFD9D79D2EFBBC`.
Truncation to the first 34,221 bytes reproduces sealed p.136 at SHA-256
`E025EFA76D8F9C9BBDA04042337FA59D653F93E403AAB5FD3BC287F2712FDE67`.
Paired English p.137 marker coordinates are `ega1-5.tex` lines 622--680,
3,499 bytes / SHA-256
`A67BE199B4179065BF5BE53CAEC3C9639BD95B5D3B00635CA2BD90DB1736CEBD`.
The exact live build prefix is lines 239--680, 21,204 bytes / SHA-256
`0F477657D318698B5FB3FEBBD90E6768AD3AB7AFB93432A17F88699892FDCCB2`
with no balancing addition; together with prior projections the live source
reproduces lines 1--680 at 36,374 bytes / SHA-256
`95BE9F42A97B3222137BA29376401C9DE00531A697C30C7D79A419111459C4E1`.
Final cumulative coordinates, exhaustive references, subject/formula/
terminology indices, and implication closure remain deferred to the stable
cumulative reader.

## Incremental EGA I p.138 scaffold

- `provenance:EGA-I-p138-fr`: direct-authority page node. Source is NUMDAM EGA
  I PDF one-based p.137 / printed p.138, verified against the one bounded
  600-dpi page image at SHA-256
  `C5104A4DB04052A58074BF34EDD92726FE3C25FC1E5F68D59C46E286F50A240F`
  and the existing PDF text layer at SHA-256
  `F92EEB6316D10137CD3A34E1634478D7C48013E0E8A717162F0E868E7A30F889`.
  Method is direct visual reading plus non-OCR text-layer confirmation;
  `confidence=high`, `unresolved_reading_count=0`, and
  `catalogued_author_error_count=0`.
- `I.5.5.5-fr`: target-open-cover locality criterion. Hypotheses are a
  prescheme morphism `f:X->Y` and an open cover `(Y_lambda)` of `Y`; conclusion
  is `f separated iff every restriction f^(-1)(Y_lambda)->Y_lambda separated`.
  Parent is section 5.5.
- `object:I.5.5.5.cover-pullbacks-fr`: definitions
  `X_lambda=f^(-1)(Y_lambda)`, `Y_(lambda mu)=Y_lambda intersect Y_mu`, and
  `X_(lambda mu)=X_lambda intersect X_mu=f^(-1)(Y_(lambda mu))`. Product
  comparison edges target `I.3.2.5-fr` and `I.3.2.6.4-fr`.
- `proof:I.5.5.5-fr`: same-index products
  `X_lambda times_Y X_lambda` cover `X times_Y X`; cross products
  `X_lambda times_Y X_mu` identify with
  `X_(lambda mu) times_(Y_(lambda mu)) X_(lambda mu)`, then with
  `X_(lambda mu) times_Y X_(lambda mu)`, hence with an open of a same-index
  product. Typed dependencies are `I.4.2.4.b-fr`, `I.3.2.5-fr`,
  `I.3.2.6.4-fr`, and `I.3.2.7-fr`.
- `comparison:I.5.5.4.affine-target-reduction-fr`: an affine open cover of
  `Y` reduces the study of separated morphisms to separated morphisms taking
  values in affine schemes. Dependency is `I.5.5.4-fr`; the edge type is
  `mathematical_reduction`, not `attention_only`.
- `I.5.5.6-fr`: affine-base separatedness criterion. Hypotheses are affine
  `Y`, a prescheme `X`, and an affine-open cover `(U_alpha)`. Conclusion is
  that `f:X->Y` is separated iff every `U_alpha intersect U_beta` is affine
  and `Gamma(U_alpha intersect U_beta,O_X)` is generated by the canonical
  images of `Gamma(U_alpha,O_X)` and `Gamma(U_beta,O_X)`.
- `formula:I.5.5.6.diagonal-preimage-intersection-fr`: two-line identity
  `Delta_X^(-1)(U_alpha times_Y U_beta)` equals
  `Delta_X^(-1)(p^(-1)(U_alpha) intersect q^(-1)(U_beta))`, hence equals
  `U_alpha intersect U_beta`. Parent is `proof:I.5.5.6-fr`; cover dependency
  is `I.3.2.7-fr`.
- `formula:I.5.5.6.tensor-ring-fr`: canonical ring identification
  `Gamma(U_alpha,O_X) tensor_(Gamma(Y,O_Y)) Gamma(U_beta,O_X)` for the affine
  scheme `U_alpha times_Y U_beta`. Dependency is `I.3.2.2-fr`.
- `map:I.5.5.6.multiplication-fr`: source map
  `h_alpha tensor h_beta -> h_alpha h_beta` from
  `A(U_alpha times_Y U_beta)` to
  `Gamma(U_alpha intersect U_beta,O_X)`; conclusion is surjectivity. Typed
  dependency is `I.4.2.3-fr`.
- `I.5.5.7-fr`: affine schemes are separated and therefore schemes. It
  depends on `I.5.5.6-fr` and terminologically compares to `I.5.4.1-fr`.
- `I.5.5.8-fr`: for affine `Y`, a morphism `f:X->Y` is separated iff `X` is
  separated, equivalently iff `X` is a scheme. Proof edge targets
  `I.5.5.6-fr` and records that the criterion is independent of `f`.
- `I.5.5.9-fr`: local target criterion with asymmetric logical polarity.
  Necessity: every open `U` on which `Y` induces a separated prescheme has
  separated `f^(-1)(U)`. Sufficiency: it is enough to check every affine open
  `U subset Y`. Necessity uses `I.5.5.4-fr` plus `I.5.5.1.ii-fr`; sufficiency
  uses `I.5.5.4-fr` plus `I.5.5.8-fr` and affine-open covers.
- `corollary:I.5.5.9.affine-morphism-fr`: if `X` and `Y` are affine schemes,
  every morphism `X->Y` is separated. Parent is `I.5.5.9-fr`.
- `I.5.5.10-fr`: affine intersection statement. Hypotheses are a scheme `Y`,
  a morphism `f:X->Y`, affine open `U subset X`, and affine open
  `V subset Y`; conclusion is `U intersect f^(-1)(V)` affine.
- `object:I.5.5.10.graph-intersection-fr`: proof object
  `Gamma_f(X) intersect p_1^(-1)(U) intersect p_2^(-1)(V)` inside
  `X times_Z Y`, whose image under `p_1` is `U intersect f^(-1)(V)`. The
  proof continues on printed p.139; `range_status=open`.
- `english-repair:I.5.p138.ref-3.2.5`: restores the source's first 3.2.5
  dependency in the proof of 5.5.5; the later 3.2.5 dependency remains
  distinct.
- `english-repair:I.5.p138.affine-target-reduction`: replaces a mere
  restriction-of-study formulation by the source's actual reduction to the
  affine-target case.
- `english-repair:I.5.p138.criterion-number`: restores singular `criterion`
  in the observation after 5.5.8.
- `english-repair:I.5.p138.necessity-sufficiency`: removes the inherited
  false `necessary and sufficient` claim for the broad condition in 5.5.9
  and restores the distinct necessary and sufficient scopes.
- `english-normalization:I.5.p138.mapsto-retained`: English `mapsto` is an
  explicitly ledgered semantic normalization of printed/source `to`; it is
  not attributed to the author and changes no domain, codomain, or product.
- `english-normalization:I.5.p138.proof-structure-retained`: inherited proof
  environments remain for navigation and proof-scope semantics although the
  French prints no explicit Demonstration headings. The diplomatic French
  remains print-structure faithful.
- `english:I.5.p138-confirmation`: after four reversible repairs and the
  explicitly retained normalizations, live lines 681--749 are source-grounded.
  R82 changes exactly `ega1/ega1-5.tex` from the R81-gated 127-file tree.

Exact p.138 French append coordinates are `ega1-5-fr.tex` bytes
38,045--42,953, a 4,909-byte suffix / SHA-256
`0B25E5A1D790A3A1C09C38E94BE63132A169C8808DFABD2112C1E3664B3F857A`.
The p.138 marker begins at one-based byte 38,046; marker-to-EOF is 4,908
bytes / SHA-256
`26C37233B0E0885230BFABF37989C6A86FF2BCE6D5C016D89F9C4D2469A9E4FB`.
Truncation to the first 38,044 bytes reproduces sealed p.137 at SHA-256
`9F316E9901A7DC8F069853E0DC3A9061FA49779CB59CE2016CFF95B2D11FD4BE`.
Paired English p.138 marker coordinates are `ega1-5.tex` lines 681--749,
4,718 bytes / SHA-256
`93D246F22000ABBAD8944FDB5AC9A8875E8D4609375C8915F813811C6351C3D6`.
The exact live build prefix is lines 239--749, 25,922 bytes / SHA-256
`1B1CCE5050ADD9E0889175B7E07EC242EEF8B6079AAC438D7C07C0B02180EAD5`
with no addition inside the exact projection. The bounded wrapper adds one
12-byte build-only `\end{proof}` because Proposition 5.5.10 continues on
printed p.139. Together with prior projections the live source reproduces
lines 1--749 at 41,092 bytes / SHA-256
`4E881F44824A65188E1B999B876FF510476E944E3B96A29980904B928BAD4372`.
Final cumulative coordinates, exhaustive references, subject/formula/
terminology indices, and implication closure remain deferred to the stable
cumulative reader.
