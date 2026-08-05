# Binding safeguards for the Verdier Astérisque 239 corpus

Status: controlling, fail-closed, append-only as to numbered safeguards  
Corpus: the complete Astérisque 239 publication only  
Authority: NUMDAM/SMF PDF SHA-256
`6214C252BACEBA5584E3C4AEB564C129851941C1A9250BABAB45B79A3939B0AE`  
Work root: this no-overwrite Verdier root only

## 1. How this control is to be read

Each safeguard below has four parts:

1. an invariant that must remain true;
2. an executable or independently replayable test;
3. a stop condition defining what must not proceed when the test fails; and
4. a recovery rule defining the only acceptable way to resume.

“PASS” is always typed and scoped. A build PASS is not a source-fidelity PASS;
a source-fidelity PASS is not a semantic-closure PASS; a semantic-closure PASS
is not a privacy or rights PASS; and a local package PASS is not a publication
or raw-readback PASS. No narrower result may be promoted by prose into a
broader claim.

These safeguards are successors to, not replacements for, the adverse
predecessor record. If a later rule is improved, the old text remains and a
new numbered rule or explicit supersession record is appended. A failed
control is evidence; it is not silently rewritten into a PASS.

## 2. Scope, custody, and no-overwrite controls

### VDR-SG-0001 — exact corpus boundary

**Invariant.** The admitted corpus begins with the first issue-content page of
Astérisque 239 and ends at physical PDF page 270. Physical page 1 is the NUMDAM
provider wrapper, not issue content. No other Verdier work, SGA 4, or SGA
4 1/2 material may enter this source tree.

**Test.** `PAGE_AND_UNIT_MAP.csv` and `semantics/SOURCE_PAGE_MAP.csv` must have
one and only one disposition for each physical page 1--270. Their physical-page
sets must be equal. Page 1 must be typed `provider_wrapper`; pages 2--270 must
be typed according to the issue topology. No authority locator may name a
page outside 1--270 or a different source publication.

**Stop.** Stop source admission, build, and package promotion on a missing,
duplicate, or out-of-range page; on a foreign-work citation treated as local
source; or on any attempt to continue after page 270.

**Recovery.** Append a page-map correction with old and new values, repair all
dependent unit and semantic locators, replay exact set equality, and resume
only at the first unresolved in-scope page.

### VDR-SG-0002 — exclusive producer ownership

**Invariant.** This task is the sole producer for the Verdier Astérisque 239
root. FGA, Tôhoku, Illusie I--II, SGA, FAC, GAGA, EGA, and Deligne owners do
not share its mutation surface.

**Test.** Before any resumed production session, inspect the live task roster
and append an ownership receipt naming task IDs, scopes, and the exact Verdier
root. Compare the result with `INTAKE_AND_OWNERSHIP.md`.

**Stop.** Stop before editing if another live task claims the same publication,
page range, or target root, or if ownership cannot be reproduced.

**Recovery.** Obtain an explicit handback or disjoint allocation, append the
new custody record, and rehash the entire Verdier root before mutation.

### VDR-SG-0003 — authority and predecessor immutability

**Invariant.** Authority PDFs, comparison witnesses, common handoff files, and
all predecessor roots are read-only. Every Verdier mutation occurs under the
prescribed no-overwrite root.

**Test.** The retrospective and production manifests bind the external files'
read-time identities. A final changed-file inventory must contain no path
outside the Verdier root. Source-generation scripts may read external paths but
must have no write target outside this root or an explicitly created temporary
directory.

**Stop.** Stop immediately on any detected external write, timestamp change
caused by this task, or command whose resolved output path is outside the
Verdier root.

**Recovery.** Preserve the incident, determine whether external bytes changed,
restore only through an authorized non-destructive successor procedure, and
do not resume until exact custody is re-established.

### VDR-SG-0004 — path resolution before mutation

**Invariant.** Every write, delete, move, build output, and cleanup target is an
explicit resolved absolute path inside this root or a verified task-specific
temporary directory. No unresolved variable, wildcard, home-directory alias,
or inherited current directory decides a destructive target.

**Test.** Scripts must resolve and prefix-check every output target. A build
preflight prints the resolved source, job name, output directory, and expected
artifact set. Literal names such as `$out` or `$buildDir` are forbidden in the
resolved tree.

**Stop.** Stop on an unresolved variable, unexpected current working directory,
literal variable-name directory, or extra output path.

**Recovery.** Preserve a workflow-error receipt, remove only verified generated
scratch, issue a corrected no-overwrite command, and prove source bytes did not
change.

## 3. Durable intent and restart controls

### VDR-SG-0005 — complete durable objective

**Invariant.** The durable objective and disk handoff explicitly name every
terminal deliverable: diplomatic French, corrected French, source-aligned
English, bilingual and single-language readers, one shared semantic graph,
exhaustive targets/candidates/edges/residuals and indexes, evidence-qualified
pre-Stacks mappings, builds, privacy-clean package, rights state, and exact
handoff. They also state that Verdier's thesis body is unfinished and must not
be silently completed.

**Test.** A restart validator checks for these named deliverables in both
`INTAKE_AND_OWNERSHIP.md` and `CONTINUATION_HANDOFF.md`. Missing required terms
are an error, not a warning.

**Stop.** Stop production if a goal, summary, compacted context, or successor
prompt narrows any required layer or forgets the hard stop.

**Recovery.** Reread the controlling brief and on-disk controls through EOF,
append a scope-correction receipt, reinstall the complete objective, and only
then resume.

### VDR-SG-0006 — mandatory restart read-in

**Invariant.** A successor does not infer purpose or cursor from chat memory.
It reads the controlling common handoff, Verdier README, this file, status,
logbook, assumption/reversal ledger, source manifest and validation, current
page/unit map, all live decision ledgers, semantic validation, and the exact
continuation section through EOF.

**Test.** The successor appends a machine-readable receipt containing every
required path, observed bytes, SHA-256, EOF/read status, acceptance timestamp,
and discrepancies. Required-file set equality and stable-ID uniqueness must
pass.

**Stop.** Stop before mutation if a required file is missing, unread, truncated,
or identity-incoherent, or if the exact cursor and ownership cannot be stated.

**Recovery.** Resolve the discrepancy from disk and immutable handoff history;
never guess from a compact summary. If a mutable file advanced legitimately,
record both the historical binding and the current generation.

### VDR-SG-0007 — historical versus live identities

**Invariant.** A handoff hash certifies the generation it names. Later
append-only advancement is neither corruption nor proof that the historical
validation covers the live tree.

**Test.** Every identity record is typed `immutable`, `historical_snapshot`, or
`live_gate`. Validators compare only the generation named by the claim and
report current drift separately. Historical uncertainty, correction, and
lineage rows must also join to exactly one machine-readable current disposition;
append-only preservation without a current-state overlay is not closure.

**Stop.** Stop any claim that uses a historical PASS to certify later bytes, or
that treats expected mutable advancement as corruption without evidence.

**Recovery.** Generate a new ordinal whole-tree manifest and validation for the
current generation, preserve the historical record, and state the relationship
between them.

## 4. Source authority and content-layer separation

### VDR-SG-0008 — direct authority decides

**Invariant.** The controlling NUMDAM/SMF page image decides diplomatic source
content. Extracted text, OCR, reconstructed TeX, comparison DJVU/PDF, prior
translations, and later literature are locator or comparison witnesses only.

**Test.** Every admitted source unit has the controlling authority SHA-256,
physical page, printed page or front-matter coordinate, review method, and
confidence. Any use of a comparison witness has its own decision ID and states
why the primary page was insufficient.

**Stop.** Stop on any content decision supported only by extraction, OCR,
inherited TeX, translation, memory, or an unbound crop.

**Recovery.** Reopen the bounded direct-authority page or tight crop, decide the
reading, and record whether the witness guess was confirmed or reversed.

### VDR-SG-0009 — no new OCR

**Invariant.** No OCR generation is authorized for this corpus.

**Test.** The changed-file and process logs must contain no OCR output and no
OCR invocation. Existing text layers may be used only for navigation and must
never be cited as the deciding witness.

**Stop.** Stop on an OCR command, an OCR-produced artifact, or a decision whose
provenance is merely `extracted_text`.

**Recovery.** Exclude the output from evidence, preserve the workflow incident,
re-adjudicate affected readings directly from the authority image, and prove no
OCR artifact entered source or package manifests.

### VDR-SG-0010 — three independent textual layers

**Invariant.** Diplomatic French, corrected French, and source-aligned English
are distinct artifacts with distinct editorial roles. They share unit IDs and
semantic nodes but do not share mutable prose or correction state.

**Test.** Every unit maps one diplomatic slice, one corrected-French slice, and
one English slice to the same semantic ID. A layer-difference report classifies
every non-identical French pair and every functional English departure by
stable decision ID. Include graphs and TeX macros must not cause one layer's
edit to alter another implicitly.

**Stop.** Stop on copied corrections in diplomatic French, unlogged corrections
in corrected French, English editorial structure treated as diplomatic
evidence, or a shared content file that erases layer provenance.

**Recovery.** Restore the last exact layer identities, append the mistaken
cross-layer operation and its inverse, reapply the decision to the correct
layer only, and regenerate all three projections.

### VDR-SG-0011 — diplomatic French

**Invariant.** Diplomatic French preserves printed wording, spelling,
punctuation, notation, ordering, labels, source errors, incomplete sentences,
and unfinished passages, subject only to reversible TeX representation.

**Test.** Each unit's transcription ledger records `source_corrections_applied`
as zero. Apparent errors are either preserved with a source-oddity record or
held unresolved. A direct page comparison and page-envelope check close the
unit.

**Stop.** Stop on silent accenting, modernization, repaired grammar, balanced
punctuation not present in print, corrected formula, supplied proof closure, or
completion of an unfinished argument.

**Recovery.** Restore the printed form, append the reversal and blame class,
propagate the repair to every diplomatic projection, and retain any desired
correction only in corrected French with a visible record.

### VDR-SG-0012 — corrected French

**Invariant.** Corrected French begins as an exact projection of diplomatic
French. It differs only through explicit, source-bound corrections or declared
reader-facing normalizations. Every difference is reversible and visible in
the correction apparatus.

**Test.** A token- or AST-aware French-layer diff must resolve every delta to
one active `SOURCE_CORRECTIONS.jsonl` or `NORMALIZATION_DECISIONS.jsonl` ID.
Each record includes source form, corrected form, rationale, scope, confidence,
visible-note disposition, inverse, and supersession state.

**Stop.** Stop on an unexplained delta, a correction based on stylistic
preference alone, a correction whose scope is unknown, or a hidden emendation
of unfinished text.

**Recovery.** Revert the unbound delta or append a fully evidenced decision;
then replay the complete French-layer diff and correction-note coverage.

### VDR-SG-0013 — source-aligned English

**Invariant.** English preserves the mathematical and logical content, scope,
dependencies, incompleteness, and author/editor boundary of the controlling
French while allowing declared idiomatic translation and reader typography.

**Test.** Every aligned unit receives a proposition/formula/diagram/reference
comparison, and every functional departure receives a stable translation or
normalization decision with source text, final text, rationale, inverse, and
affected-copy scope.

**Stop.** Stop on omission of a hypothesis, logical connector, object, index,
reference, qualification, incomplete ending, or editorial attribution; on an
unjustified strengthening; or on silently importing later mathematical
knowledge.

**Recovery.** Repair every active English projection and cumulative source,
append the discovered error and exact inverse, rebuild only the affected
checkpoint, and run a fixed-string plus semantic-scope recurrence search.

### VDR-SG-0014 — comparison lineage is not a fourth authority layer

**Invariant.** Comparison witnesses and later editions remain provenance
records. Their readings are never merged invisibly into diplomatic, corrected,
or English text.

**Test.** `SOURCE_AUTHORITY.csv` types each witness and every comparison use.
Any adopted comparison reading names its primary-source defect or damage,
decision class, and final layer. No delivered reader imports comparison prose
without a visible scholarly reason.

**Stop.** Stop when a comparison text silently decides a primary-source
reading or when comparison provenance cannot be reconstructed.

**Recovery.** Separate the lineage, restore the authority-backed reading, and
append any legitimate comparison note to the apparatus or graph.

## 5. Authorship, editorial apparatus, and unfinished state

### VDR-SG-0015 — author/editor role integrity

**Invariant.** Jean-Louis Verdier's thesis text, Luc Illusie's preface, Georges
Maltsiniotis's editorial notes, bibliographic apparatus, indexes, and publisher
front matter retain their actual roles. Editor text is not attributed to
Verdier and vice versa.

**Test.** Every unit has `responsible_agent`, `unit_role`, and `source_pages` in
the page/unit map and semantic graph. Reader headings and metadata reproduce
those roles. A role-transition audit checks every boundary.

**Stop.** Stop on a missing or ambiguous responsibility field, a merged unit
crossing roles, or reader metadata that makes the editor a coauthor of thesis
body text.

**Recovery.** Split the units at the source boundary, correct all reader and
graph projections, and append the attribution repair.

### VDR-SG-0016 — unfinished thesis preservation

**Invariant.** The thesis body is historically unfinished. No proof, sentence,
section, cross-reference, or planned continuation is supplied to simulate
completion. Editorial indications of incompleteness remain visible.

**Test.** The topology and semantic graph mark every unfinished, truncated,
promised-but-absent, or editor-supplied locus. Translation comparison confirms
that English and corrected French preserve the same epistemic state. Reader
front matter states the unfinished status without workflow prose.

**Stop.** Stop on inferred completion, imported continuation from another
Verdier work, silently closed proof environments, or a completion claim that
does not preserve the unfinished state.

**Recovery.** Restore the exact source boundary, move explanatory material to a
clearly attributed note, append the reversal, and search globally for every
copy of the supplied text.

## 6. Decision, normalization, and reversal controls

### VDR-SG-0017 — one decision, one stable record

**Invariant.** Every source-affecting transcription choice, correction,
normalization, translation departure, rejected candidate, diagram
interpretation, and later reversal has a stable ID and an append-only record.

**Test.** All JSONL and CSV ledgers parse; required fields are nonempty; stable
IDs are unique across the complete corpus namespace; decision bindings resolve
to existing units and exact authority locators. Prose-only rationale is not
sufficient evidence of ledger completion.

**Stop.** Stop promotion on a missing decision, duplicate ID, dangling binding,
or source delta that cannot be inverted from the record.

**Recovery.** Preserve the adverse state, allocate a new stable ID, record the
original/final forms and inverse, repair all bindings, and replay uniqueness and
closure.

### VDR-SG-0018 — append-only reversal and blame precision

**Invariant.** Reversals never erase the original judgment. Records distinguish
authorial source error, inherited witness error, translation error, lead
editorial error, rejected pre-admission candidate, tooling error, control-plane
error, and workflow/resource error.

**Test.** Every reversal has `supersedes_id`, `superseded_by_id`, reason,
detection channel, affected artifacts, repair state, and recurrence test. The
original record remains present and immutable.

**Stop.** Stop on an in-place history rewrite, vague blame such as “typo” where
the responsible layer is knowable, or a corrected artifact without reciprocal
supersession.

**Recovery.** Restore the adverse predecessor record if lost, append the
correction, and validate the two-way supersession chain.

### VDR-SG-0019 — global propagation after discovery

**Invariant.** A discovered error or policy correction is searched across every
active occurrence and derived projection; local repair alone does not close it.

**Test.** The reversal record lists the search universe, exact occurrence count,
all affected units/copies, repaired identities, zero-residual query, and rebuilt
or revalidated derivatives. Search is bounded to named active roots and fields.

**Stop.** Stop when the occurrence universe is unknown, a known copy remains
stale, or a global correction is claimed from one local edit.

**Recovery.** Expand only to the explicitly authorized active surfaces, repair
copy-on-write, preserve frozen historical copies, and close with exact residual
zero or a documented held residual set.

### VDR-SG-0020 — inherited assumptions are ledgered

**Invariant.** Every inherited assumption about scope, authority, cursor,
layer policy, author/editor role, visual evidence, rights, semantic mapping,
build state, and publication state appears in
`ASSUMPTION_NORMALIZATION_AND_REVERSAL_LEDGER.csv`, even when confirmed.

**Test.** At each cumulative checkpoint, compare current status fields and
manifest claims against the assumption ledger. Any changed premise must have a
new append-only row and, when applicable, a supersession pointer.

**Stop.** Stop when a controlling assumption changed only in prose or chat, or
when downstream artifacts still embody a reversed premise.

**Recovery.** Append the missing assumption/reversal, enumerate affected
artifacts, repair them, and execute the recorded recurrence test.

## 7. Page, formula, and diagram evidence

### VDR-SG-0021 — exact page and unit set equality

**Invariant.** The page map is an inventory, not a sampling aid. Every physical
page, printed page or unnumbered coordinate, source unit, language slice, and
semantic node belongs to one consistent topology.

**Test.** Compare five sets: authority pages, page-map rows, source-unit page
envelopes, reader page markers, and semantic source-page rows. Require no
missing pages, duplicates, impossible ranges, or units whose terminal page was
reviewed only partially. Blank and wrapper pages remain explicit rows. Store
physical PDF ordinal, printed Roman/Arabic label, logical unit, and offset rule
in separate fields; no untyped `page` field may substitute one for another.

**Stop.** Stop a range-complete claim on any set inequality, underinclusive
page range, unreviewed seam, or unit whose continuation falls on the next page.

**Recovery.** Correct the range append-only, reopen every newly affected page,
repair all nine-or-more dependent locators when necessary, and supersede the
underinclusive validation.

### VDR-SG-0022 — resolution is chosen by represented detail

**Invariant.** Broad ordinary reading uses approximately 1,100--1,800
dpi-equivalent when no sufficient reusable witness exists. Genuinely small or
ambiguous glyphs, primes, subscripts, arrowheads, label sides, attachments, or
punctuation use one tight direct crop at approximately 5,000--9,000
dpi-equivalent. A thumbnail or contact sheet never adjudicates source content.

**Test.** Each visual decision records whether the evidence was a broad page or
tight crop, its effective resolution, dimensions, SHA-256, target feature, and
why that resolution was sufficient. Ambiguity records below 5,000 require an
explicit reason or remain open.

**Stop.** Stop on approval from a low-resolution overview, an upscaled crop
rather than a direct render, or an unresolved small mark.

**Recovery.** Generate at most one narrowly bounded direct crop, inspect it,
append the old and new evidence disposition, and reopen related prior units if
the new view reveals a recurring failure pattern.

### VDR-SG-0023 — delivered mathematical diagrams are native TeX

**Invariant.** Every delivered mathematical diagram is encoded in native TeX.
Source scans and crops remain private evidence; they are not reader assets.

**Test.** Derive the diagram universe from every active source component and
all diagram macros, not merely direct `includegraphics` calls. Require set
equality with `semantics/DIAGRAM_INDEX.csv` and
`DIAGRAM_AND_FORMULA_REVIEW.csv`. Scan active sources for raster dependencies,
scan the built PDF for image objects, and require an explicit disposition for
non-mathematical source images such as the portrait.

**Stop.** Stop on an unindexed diagram macro, a PNG/JPEG/PDF crop used as a
mathematical diagram, a PDF image object without an allowed asset record, or a
zero-raster claim based on only a narrower source subset.

**Recovery.** Fail-close the prior claim, add the omitted diagrams to the exact
universe, reconstruct them natively, and repeat source-, macro-, index-, and
PDF-level set equality.

### VDR-SG-0024 — diagram graph review

**Invariant.** A diagram passes only after direct-authority review of every
node, arrow, direction, label, label side, prime, subscript, superscript,
attachment, punctuation mark, and relevant layout relationship.

**Test.** One review row per diagram records node count, edge count, exact label
inventory, direction inventory, source crop identities, native TeX locus,
reviewer, confidence, and residuals. Counts and stable IDs must be unique and
must match the semantic graph.

**Stop.** Stop on “looks right,” page-level review without element inventory,
an unreviewed label side, or delegated final mathematical/visual judgment.

**Recovery.** Reopen the diagram with direct tight crops, repair native TeX if
necessary, append the superseding review, and search prior diagrams for the
same newly discovered failure class.

### VDR-SG-0025 — formulas have stable identities and exact scope

**Invariant.** Every displayed formula, numbered equation, exact sequence, and
mathematically consequential inline formula receives a stable identity,
authority locator, layer slices, and review state. Formula punctuation and
indices are content decisions, not build trivia.

**Test.** Extract the active formula universe from source units and require set
equality with `semantics/FORMULA_INDEX.csv` and the formula review rows. Each
formula's diplomatic/corrected/English forms and any deltas resolve to decision
IDs. Reader anchors must resolve uniquely.

**Stop.** Stop on an unindexed formula, an authority-absent added sign or comma,
an omitted factor or index, a duplicated formula ID, or a clean build offered
as formula proof.

**Recovery.** Recompare the exact authority locus, append the correction and
global scope, repair every active projection, and rerun formula set equality.

### VDR-SG-0026 — new failure patterns reopen relevant history

**Invariant.** Discovery of a new systematic failure class triggers a bounded
retroactive check of every earlier unit plausibly affected.

**Test.** The discovering record names a reproducible search predicate and the
closed earlier range searched. Results are recorded as repaired, confirmed
clean, or explicit residuals; silence is not a negative result.

**Stop.** Stop cumulative promotion while the bounded recurrence search is
pending.

**Recovery.** Complete the search sequentially, repair globally, and append a
closure receipt with exact counts and identities.

## 8. Shared semantic graph and pre-Stacks scaffold

### VDR-SG-0027 — one semantic graph shared by all languages

**Invariant.** French and English do not receive separate mathematical object
graphs. Stable semantic nodes model the source work; language slices and
editorial decisions attach to those nodes.

**Test.** Every source unit and mathematical object has one stable semantic ID
with zero or more diplomatic, corrected-French, and English slice bindings.
Graph validation rejects language-coded duplicate object IDs representing the
same source object.

**Stop.** Stop on parallel language-specific object graphs, mismatched unit
boundaries, or a translation node lacking its source node.

**Recovery.** Merge only through an explicit identity adjudication, preserve
old aliases as superseded records, and replay every incoming and outgoing edge.

### VDR-SG-0028 — exhaustive inventory is proven by source-universe equality

**Invariant.** “Complete,” “reference-complete,” “index-complete,” and
“semantic-complete” mean the declared inventory equals the controlling source
universe. A zero-residual result inside a hand-selected inventory is not enough.

**Test.** Derive independent source-side inventories for units, labels,
references, formulas, diagrams, bibliography entries, names, notation, terms,
and declared constructions. Require exact set equality with the corresponding
semantic tables and report missing, extra, duplicate, and unclassified items.

**Stop.** Stop any completeness claim when the universe generator excludes an
active component, hides occurrences behind a macro, samples pages, or cannot
state its scope.

**Recovery.** Fail-close the narrow claim, correct the universe generator,
preserve the prior PASS as adverse evidence, and regenerate all dependent
counts and residuals.

### VDR-SG-0029 — targets, candidates, edges, and residuals are distinct

**Invariant.** A textual reference first becomes a candidate, then an
adjudicated edge to a stable target, or a typed residual. Clickability is an
output property, not the semantic record.

**Test.** Every extracted reference occurrence has exactly one current
disposition across `REFERENCE_CANDIDATES.csv`, `REFERENCE_EDGES.csv`, and
`REFERENCE_RESIDUALS.csv`. Edges name relation type, evidence, source and target
IDs, scope, confidence, and external/internal state. PDF links are replayed
against the final edge generation only after source freeze.

**Stop.** Stop on a plain-text reference silently omitted from the inventory,
a link to a merely convenient target, a dangling edge, or an unresolved
candidate suppressed to obtain zero residuals.

**Recovery.** Restore the candidate, adjudicate or retain it as a visible
residual, create the exact target if source-supported, and regenerate reader
coordinates.

### VDR-SG-0030 — the scaffold is reusable mathematical data

**Invariant.** The pre-Stacks scaffold records units, hypotheses, conclusions,
objects, constructions, formulas, diagrams, terminology, notation,
bibliography, typed dependencies, ambiguities, and correction provenance. A
collection of hyperlinks or prose notes alone is insufficient.

**Test.** Schema validation checks required node and edge fields, referential
integrity, stable-ID uniqueness, role and page bindings, confidence vocabulary,
and coverage counts for every declared class. It also checks visible labels for
loss, truncation, TeX corruption, or accidental ID suffixes and verifies that
every equation and diagram class has an independently derived universe.
Machine-readable CSV/JSONL data, not only Markdown exposition, carries the
graph.

**Stop.** Stop semantic-complete or pre-Stacks-complete claims on absent object
classes, prose-only relationships, non-reusable line-number IDs, or deferred
residual accounting.

**Recovery.** Add the missing records without inventing content, preserve
ambiguity explicitly, and rerun schema and universe closure.

### VDR-SG-0031 — Stacks mappings remain candidates unless directly proven

**Invariant.** No official Stacks Project tag, lemma equivalence, or dependency
is invented. The corpus may record candidate alignments, but it may not mint
official tags or represent an analogy as identity.

**Test.** Every row in `STACKS_ALIGNMENT_CANDIDATES.csv` contains a real target
identifier or URL only when directly verified, exact supporting source units,
relation type (`equivalent`, `special_case`, `analogue`, `prerequisite`, or
`terminology_only`), evidence, confidence, reviewer, and unresolved caveat.
Unknown targets remain blank candidates. A validator rejects the word
`official` unless an exact external verification record is bound.

**Stop.** Stop on guessed tag syntax, unsupported equivalence, confidence
inflation, or a candidate silently promoted into the main dependency graph.

**Recovery.** Demote the mapping to unresolved, append the reason and prior
claim, and require direct authoritative verification before any later
promotion.

### VDR-SG-0032 — stable IDs survive mutable layout

**Invariant.** Semantic and decision IDs derive from publication/unit identity,
not mutable TeX line numbers, output pages, byte offsets, or generation order.

**Test.** Reflow a controlled fixture or compare successive generations: IDs
must remain unchanged while line/page coordinates update as attributes. All
aliases and supersessions resolve without cycles.

**Stop.** Stop if ordinary reflow changes IDs, if two objects collide, or if an
ID is reused for changed mathematical scope.

**Recovery.** Allocate a corrected stable ID, preserve the old ID as an alias or
superseded record as appropriate, and repair all graph, reader, and decision
bindings.

## 9. Manifests, validation, logs, and generation coherence

### VDR-SG-0033 — exact ordinal manifests

**Invariant.** Manifests use a stated Unicode-code-point ordinal relative-path
order, exact bytes and SHA-256, explicit root, explicit exclusions, and
self-excluding logic where required.

**Test.** Independent implementations replay membership, order, row hashes,
byte totals, and any aggregate/tree digest. The validator recomputes totals
from rows rather than trusting stored prose or cached variables.

**Stop.** Stop on culture-dependent sorting, null totals, list-order hashing
mislabeled ordinal, self-reference, missing/extra files, or an aggregate that
does not replay even when individual rows do.

**Recovery.** Preserve the wrong manifest, issue a no-overwrite successor,
state the implemented algorithm, and rebind every validation that depended on
the superseded generation.

### VDR-SG-0034 — every PASS binds one coherent generation

**Invariant.** A validation record binds the exact current source, ledgers,
renders, PDFs, semantic tables, manifest, and scope it claims. Current prose
cannot coexist with stale artifact paths or old byte totals under PASS.

**Test.** The validator recomputes all identity fields at runtime and checks a
single generation ID across every dependency. Stored counts are compared with
recomputed counts. Any stale path, stale checkpoint name, aggregate delta,
blank live hash, or `next_gate` already marked complete is an error.

**Stop.** Stop on a PASS whose fields refer to different checkpoints, a
manifest replay that coexists with a wrong validation aggregate, or a build
narrower than the claimed corpus.

**Recovery.** Mark the earlier validation superseded or failed, regenerate from
the intended exact set, and independently replay the new record.

### VDR-SG-0035 — shared append logs require locking

**Invariant.** A file with more than one possible writer is appended only by a
lock-aware helper that rereads current bytes while holding an exclusive append
lock, rejects duplicate IDs, flushes durably, validates, and truncates to the
original length on failure.

**Test.** Shared-log mutation records helper version, pre/post bytes and hash,
record count, unique-ID result, and lock acquisition. Direct editor,
`apply_patch`, `Set-Content`, or cached whole-file replacement of a shared log
is forbidden.

**Stop.** Stop on an observed regression, missing prior decision, lock failure,
or unknown concurrent writer.

**Recovery.** Recover the longest independently validated generation, append
the lost record exactly once under lock, verify uniqueness, and retain the
transient-regression receipt. Verdier-local single-writer logs may use ordinary
append-only editing until ownership changes; the moment a second writer is
possible, this locked rule becomes mandatory.

### VDR-SG-0036 — duplicate IDs fail closed

**Invariant.** Stable IDs are globally unique within their declared namespace.
Historical supersession does not permit reusing an ID.

**Test.** Parse every CSV/JSONL/semantic table and compute duplicates across the
union, not file by file only. References to IDs must resolve to exactly one
record of the expected type.

**Stop.** Stop source admission, merge, package, and handoff on any duplicate or
ambiguous resolution.

**Recovery.** Preserve both conflicting records, allocate a new ID to the later
one, append a mapping/supersession record, and repair every dependent link.

### VDR-SG-0037 — validation code is evidence-bearing and fallible

**Invariant.** A validator can be wrong. Its PASS is accepted only after
independent replay of its assertions and its scope.

**Test.** At meaningful checkpoints, execute at least one independent
implementation or direct recomputation for set membership, counts, hashes,
ordering, and critical semantic assertions. Recheck representative semantic
labels and current-state joins that a uniqueness-only validator cannot assess.
Preserve false-positive and false-negative validators as adverse history.

**Stop.** Stop when a validator's assertion is generic where multiple valid
occurrences exist, when its scope cannot be reconstructed, or when independent
replay disagrees.

**Recovery.** Correct by no-overwrite successor, bind a more specific assertion,
and state whether any content byte depended on the faulty control.

## 10. Builds, reader surfaces, and claim discipline

### VDR-SG-0038 — serial builds after substantive edits only

**Invariant.** Builds are serialized and occur after a real source or build-
system change, at meaningful bounded or cumulative checkpoints. No parallel
heavy build or zero-edit rebuild swarm is permitted. The project uses one
checked-in corpus runner; ad hoc shell reconstruction is not a promotion path.

**Test.** Each build receipt names the triggering edit IDs, exact inputs,
engine, working directory, output directory, passes, diagnostics, page count,
and output hash. The runner prints resolved paths before execution and rejects
unexpanded variables, wrong engine, wildcard literal paths, source-tree output,
and out-of-root destinations. At most one heavy build process is active.

**Stop.** Stop on concurrent builds, missing trigger, wrong engine/CWD, hung
process, or output written into source.

**Recovery.** terminate only the verified task process, preserve logs, correct
the invocation, and rebuild once from exact inputs.

### VDR-SG-0039 — typed closure lattice

**Invariant.** Status uses distinct states: `drafted`, `authority_read`,
`layer_admitted`, `bounded_build_pass`, `visual_pass`, `semantic_pass`,
`cumulative_source_sealed`, `privacy_pass`, `rights_disposition_recorded`,
`package_pass`, `handoff_accepted`, `published`, and `public_readback_pass`.
Later states require all stated predecessors; none is inferred from the word
“complete” in prose.

**Test.** Machine validation checks the prerequisite graph and exact generation
IDs. Every claim includes its bounded range and open holds.

**Stop.** Stop on “complete,” “canonical,” “sealed,” “reference-complete,”
“released,” or “published” without the corresponding full-scope gate.

**Recovery.** Downgrade the claim explicitly, preserve the overclaim as an
incident, close missing gates, and only then issue a new status generation.

### VDR-SG-0040 — reader PDFs contain scholarship, not workflow

**Invariant.** Reader PDFs contain the mathematical/editorial edition and
appropriate scholarly apparatus only. They contain no AI/model names, task
IDs, private paths, build status, workflow notes, QA receipts, source-tree
instructions, internal badges, or operational commentary.

**Test.** Scan TeX sources, extracted PDF text, annotations, bookmarks,
metadata, attachments, and visible page renders for prohibited classes. The
scan vocabulary includes known terms and independent shape detectors for UUIDs,
drive paths, task/state syntax, model/vendor names, and status headings.

**Stop.** Stop reader promotion on any internal workflow residue, even if the
PDF otherwise builds and reads correctly.

**Recovery.** Remove the material from reader surfaces while retaining it in
private controls, rebuild, rescan all surfaces, and append a cleanup receipt.

### VDR-SG-0041 — visual QA scope matches the claim

**Invariant.** Visual review covers every changed output page plus structural
seams and any page implicated by source mapping. Sampling may support a bounded
claim but never a whole-corpus visual closure unless the declared sampling rule
is itself the approved claim.

**Test.** Map each source change and asset to reader pages; require a review row
for every affected page in every impacted reader. Independently check page
count, blank pages, clipping, overlap, missing content, role boundaries, and
terminal pages.

**Stop.** Stop on a page omitted from the affected set, a seam reviewed on only
one side, or a narrow build used to claim the global reader.

**Recovery.** Render and inspect only the missing bounded pages, append their
hashes and dispositions, and regenerate the exact review-set validation.

## 11. Privacy, rights, archive routing, and public readback

### VDR-SG-0042 — privacy scans use independent detectors

**Invariant.** Privacy closure is not a single regex or word-boundary count.
It covers absolute and relative project roots, Documents/home/worktree paths,
tool/cache/state paths, alternate local filenames, command lines, task/thread/
UUID shapes, internal staging names, usernames, and operational prose across
source, package, archive members, metadata, and extracted/rendered PDFs.

**Test.** Run at least two independent detector families: literal/normalized
root variants and shape-based scans. Record event count, affected-record count,
affected-file count, field distribution, allowlist, and residuals separately.

**Stop.** Stop on a zero claim produced only by an allowlist-sensitive detector,
on conflicting counts, or on any unexplained residual.

**Recovery.** Preserve the earlier count and zero claim, append the corrected
counts, create a privacy-clean projection without rewriting the private source
log, and rescan from raw bytes and rendered/extracted PDF surfaces.

### VDR-SG-0043 — privacy counts are reproducible and typed

**Invariant.** A count states whether it measures matches/events, records,
fields, files, or unique values. These categories are never substituted for one
another.

**Test.** Validation recomputes all categories from the same frozen input and
checks their arithmetic relationships. A summary must name the exact scanner
generation and input manifest.

**Stop.** Stop on an unexplained count change, mixed denominator, or stale
privacy total under a newer PASS.

**Recovery.** Append a count-correction record with both old and recomputed
figures, explain the detector gap, and supersede downstream claims.

### VDR-SG-0044 — public French redistribution is rights-gated

**Invariant.** Archival French TeX and local readers are required, but public
redistribution of source-derived French and source images is a separate
rights-aware decision. Source scans and portrait crops are excluded unless a
specific right permits them.

**Test.** Package validation requires an asset-by-asset rights disposition,
source/crop exclusion check, and explicit separation of local scholarly output
from public candidate contents.

**Stop.** Stop public packaging on an unknown license, private authority image,
or blanket rights assertion not supported by the exact artifact.

**Recovery.** Exclude the held artifact, use a lawful native/textual treatment,
record the caveat, and regenerate the public manifest.

### VDR-SG-0045 — existing archive concepts decide routing

**Invariant.** Publication uses the verified existing methodology and
replication concepts when authorized. No duplicate concept is minted for a
transport retry, compact handoff, or corrected package. Concept IDs and DOIs
are verified from live authoritative readback at action time.

**Test.** Compare the intended concept map, live concept metadata, package
purpose, and prior transport ledger. Detect transposed or unrelated DOIs.
Require an explicit no-duplicate result before mutation.

**Stop.** Stop on an unverified DOI, mismatched concept subject, duplicate
purpose, or absent authorization.

**Recovery.** Append a concept-map correction without rewriting prior records,
route only to the correct existing concept, and preserve erroneous historical
references as superseded evidence.

### VDR-SG-0046 — one logical package, one transport lineage

**Invariant.** Retries, mirror repairs, line-ending corrections, and compact
handoffs remain generations of one named package/transport lineage. They do
not become new logical releases or duplicate archive concepts.

**Test.** Package IDs, predecessor/successor fields, manifest identities, and
transport receipts form a single acyclic chain. Before transport, compare
against every existing active package ID and concept payload.

**Stop.** Stop on an already-delivered package, ambiguous lineage, duplicate
payload under a new name, or a request to mint around a failed readback.

**Recovery.** Correct the existing lineage append-only and retransport only the
authorized successor generation.

### VDR-SG-0047 — raw public readback is mandatory for publication claims

**Invariant.** Upload success, API metadata, a container hash, or a Git commit
does not prove public bytes. Publication closure requires raw readback of every
outer artifact and, for containers, every member with safe paths and exact
bytes/hashes.

**Test.** Fetch from the public endpoint independently, enumerate the exact
manifest set, compare bytes/SHA-256, inspect container member paths, and scan
public bytes for privacy residue and line-ending drift.

**Stop.** Stop a `published` or `mirror_complete` claim on missing members,
normalized blobs, stale CSVs, absent receipts, unsafe archive paths, or no raw
readback.

**Recovery.** Correct the existing transport, reread all raw bytes, and append
the successor receipt. Never hide the adverse first transport.

## 12. Resource safety and bounded concurrency

### VDR-SG-0048 — exact-path-only discovery

**Invariant.** Search is confined to exact named roots and files required by
the current unit or control. No recursive scan of all Documents, the user
profile, a drive, or the relocated Chatnotes tree is permitted.

**Test.** Each search command records its exact root and purpose. A preflight
rejects broad roots, empty variables, drive roots, profiles, and recursive
globs above the authorized project subtree.

**Stop.** Stop before executing an unbounded command or when output volume
shows the intended bounded query expanded unexpectedly.

**Recovery.** Cancel the process, record the workflow error and actual scope,
identify exact target paths from manifests/handoffs, and resume with a bounded
query. A broad command that happened to finish is still an incident.

### VDR-SG-0049 — sequential RAM-light visual work

**Invariant.** Reuse exact existing evidence first. Generate and inspect at most
one tightly relevant high-resolution crop at a time. Never batch-render or
bulk-load full pages at original detail.

**Test.** Before rendering, record the unresolved feature, existing evidence
searched, intended crop rectangle, resolution, estimated pixel count, and
memory bound. Confirm no other heavy render/build process is active.

**Stop.** Stop on speculative batches, whole-page 5,000/9,000-dpi renders,
parallel heavy processes, or memory pressure.

**Recovery.** terminate the verified task process, retain failed artifacts as
non-adjudicative evidence, confirm no background process remains, and retry
only with a narrower crop or lower ordinary-reading resolution.

### VDR-SG-0050 — bounded agent delegation

**Invariant.** Agents may perform genuinely disjoint, low-intensity,
read-only or mechanical tasks. The lead owns source readings, translation,
mathematics, diagram interpretation, visual approval, scope, and final claims.

**Test.** Every delegation names a disjoint corpus/path set, prohibits OCR and
heavy concurrent work, and requires exact evidence. The lead independently
checks any fact used for a material editorial or completion decision.

**Stop.** Stop on overlapping writers, duplicate ranges, delegated final
judgment, render/build swarms, or an agent result without inspectable evidence.

**Recovery.** Interrupt overlapping work, rehash affected files, reassign sole
ownership, and have the lead adjudicate from direct authority.

## 13. Handoff, retrospective, and terminal closure

### VDR-SG-0051 — continuation must be sufficient without chat history

**Invariant.** `CONTINUATION_HANDOFF.md` gives a successor the complete purpose,
authority, ownership, exact live generation, closed and open ranges, next
cursor, layer states, semantic state, decisions/reversals, build state, rights
holds, resource rules, first safe action, and terminal hard stop. Chat and task
history are supplemental adverse evidence, never a required custody layer.

**Test.** A restart simulation using disk files only must reconstruct the next
safe action and all prohibited actions. Every referenced artifact exists and
matches the identity in the current handoff validation.

**Stop.** Stop handoff on “see chat,” an approximate cursor, missing holds,
stale paths, or an identity that cannot be replayed.

**Recovery.** Expand the handoff from exact on-disk controls, independently
replay it, and obtain an acceptance receipt before custody transfers.

### VDR-SG-0052 — retrospective checkpoint precedes resumed production

**Invariant.** No further Verdier source admission or TeX build occurs until
the forensic audit, failure register, this safeguard file, assumption ledger,
source manifest, validation JSON, and detailed continuation section exist and
pass their declared checks. One hundred thousand investigation tokens is a
minimum, never a stop condition.

**Test.** `RETROSPECTIVE_VALIDATION.json` must report `PASS`, `errors: []`, all
mandated topic dispositions present, all manifest rows read through EOF, exact
hash replay at checkpoint time, unique stable IDs, and no change to the frozen
four opening draft identities.

**Stop.** Stop on a missing mandated topic, generic lesson without evidence,
incident misreported as fact or hazard, unresolved source identity, changed
draft byte, or threshold-based premature closure.

**Recovery.** Continue investigation, append missing sources or corrections,
rerun validation, and preserve any earlier failed retrospective generation.

### VDR-SG-0053 — later violations remain append-only

**Invariant.** Every later breach or near miss of these safeguards receives a
stable incident ID, exact evidence, scope, blame class, containment, repair,
and recurrence result. A clean final package does not erase its adverse path.

**Test.** At each checkpoint, reconcile workflow-error and reversal ledgers
against build logs, status changes, validation failures, and changed files.
Every failed attempt is either bound or explicitly non-source-affecting.

**Stop.** Stop promotion when adverse evidence exists only in ephemeral console
output or when a known violation is absent from the ledger.

**Recovery.** Preserve or reconstruct the receipt from exact artifacts, append
it, and re-run the affected gate.

### VDR-SG-0054 — final corpus closure is conjunctive

**Invariant.** Final completion requires all of the following on one exact
generation: physical pages 1--270 disposed; issue pages 2--270 represented as
appropriate; all three textual layers closed; author/editor/unfinished-state
roles correct; every formula/diagram/reference/index universe reconciled; one
shared semantic graph complete to its declared pre-Stacks scope; no invented
Stacks mapping; readers built and visually checked; privacy and rights gates
closed; exact package and handoff accepted; and no work past page 270.

**Test.** The final validator evaluates every prerequisite independently and
then computes the conjunction. It reports each component state and exact
generation, not merely a top-level Boolean.

**Stop.** Stop a completion claim if even one prerequisite is open, stale,
bounded to less than the full issue, or tied to another generation.

**Recovery.** Report the honest last closed state and next cursor, close only
the missing gates, and issue a new exact final generation.

### VDR-SG-0055 — compact paths and filenames

**Invariant.** New project-owned artifacts use short stable names. Put meaning
in semantic IDs and manifests, not in sentence-length filenames. Except for an
imported authority name or a frozen compatibility path, a new basename is at
most 32 characters and a new path is at most four components below this work
root. One coherent page or unit is grouped in one source file per textual
layer; crops and receipts are not multiplied merely to narrate workflow.

Frozen checkpoint paths remain valid historical identities. Any shortening of
live, unfrozen paths is one atomic migration: rename once, update every source,
semantic, build, and ledger reference, then validate that the old live path has
no remaining consumer. Do not create aliases or duplicate copies as a shortcut.

**Test.** Before each checkpoint, enumerate only this bounded root and report
maximum relative depth, maximum project-owned basename length, exceptions, and
duplicate-content paths. New exceptions require a recorded reason. The reader,
package, and handoff expose a compact logical tree rather than every private QA
scratch witness.

**Stop.** Stop new artifact creation when a descriptive filename exceeds the
limit, a directory fan-out substitutes for an index, aliases duplicate one
artifact, or a rename would leave stale references or invalidate a frozen
generation.

**Recovery.** Choose a short stable ID, retain description inside existing
metadata, migrate only unfrozen paths atomically, re-run reference and hash
validation, and preserve frozen historical paths without cloning them.

## 14. Mandatory stop-state vocabulary

The following conditions are always fail-close:

- authority identity or page mapping cannot be reproduced;
- ownership overlaps or the intended root is not exclusive;
- a source decision rests only on OCR, extraction, inherited TeX, or memory;
- diplomatic and corrected French cannot be distinguished mechanically;
- an unfinished passage has been editorially completed;
- a content delta lacks a stable rationale and inverse;
- a new global correction has not been propagated across all active copies;
- diagram, formula, reference, or semantic source-universe equality fails;
- a mathematical diagram remains raster-backed in a delivered reader;
- a Stacks tag or equivalence is guessed rather than verified;
- a manifest or validation mixes generations, has a stale aggregate, or does
  not independently replay;
- stable IDs collide or a shared append log regresses;
- a reader contains private, AI, status, build, or workflow material;
- privacy counts disagree or residual detectors disagree;
- rights or archive-concept routing is unverified;
- public raw-byte/member readback is incomplete;
- a broad scan, speculative render batch, or heavy concurrency threatens the
  workstation;
- project-owned path or filename sprawl violates VDR-SG-0055 or makes the
  deliverable tree materially harder to audit;
- the successor cannot resume from disk without reconstructing intent from
  chat; or
- any claim is broader than the exact build, review, inventory, or generation
  that supports it.

When any condition occurs, the correct action is to preserve the adverse
evidence, state the honest bounded result, append a correction or supersession,
and rerun the exact failed gate. The correct action is never to make the claim
smaller in fine print while leaving a broader headline PASS in place.
