---
title: "AI-Run Modern LaTeX Manuscript Workflow"
subtitle: "Replication Packet"
date: "Version 2026-07-28: source-image adjudication, disjoint sessions, and resource discipline"
---

This document describes the workflow actually used by the Modern LaTeX Manuscripts project. The process is AI-run under human direction. Local machines perform source intake, image preparation, compilation, hashing, packaging, and publication. High-context model sessions perform bounded transcription, translation, source comparison, diagram reconstruction, and release work. Deterministic gates decide what may be promoted.

This is a workflow record, not a certification of any manuscript. A successful build, a large page count, a green validator, or a filename containing `complete` does not prove source fidelity.

The July 28 correction makes production discipline explicit. A top-level Codex
session is not a subagent. Top-level sessions own disjoint whole-exposé ranges.
They do not commission agent cascades for mathematical translation,
transcription adjudication, diagram reconstruction, reference semantics, or
visual audit. Those judgments remain with the top-level session. Subagents may
perform bounded mechanical support or preliminary drafting only.

For scan-controlled work, the source image decides. The complete
user-supplied OCR corpus already exists and may be consulted read-only as a
locator or drafting witness. It must not be generated, rerun, re-extracted, or
delegated again. For SGA 1 and SGA 2, the completed mathematicians' LaTeX
transcription is the controlling text and is not subjected to another blanket
image-by-image transcription audit. Source images are opened for genuine
ambiguities, diagrams, or a declared source-control question, not to repeat
completed work.

## 1. Define the public object before doing the work

Every lane begins with an output contract:

- exact author, work, edition, language, and source range;
- expected reader PDF and editable TeX;
- source scan or source-image witnesses;
- page or unit map;
- terminology, formula, table, diagram, and correction ledgers where relevant;
- build and render evidence;
- manifest, checksums, status statement, and continuation cursor.

The contract forbids summaries in place of text, screenshots in place of editable diagrams or tables, silent omission of difficult material, and unlabelled interpolation. A model may return a partial tranche, but it must say exactly where it stops.

## 2. Keep authority layers separate

The project uses a layered authority model:

1. **Source authority:** the verified scan or born-digital source, with edition identity, checksum, page count, scan coordinates, and native image resolution.
2. **Witness layer:** OCR, VLM readings, formula OCR, extracted PDF text, crops, and layout detections. These locate possible omissions and difficult objects; they are not authority.
3. **Scaffold layer:** inherited TeX, earlier transcription, or translation memory. It may be useful for navigation while still being paraphrased, compressed, or wrong.
4. **Source-reconciled working layer:** text and mathematics checked against identified source pages or units, with decisions and unresolved issues recorded.
5. **Translation layer:** a target-language rendering tied to a frozen source-control layer and stable unit IDs.
6. **Release layer:** a frozen reader and evidence closure whose manifest, build, render, source map, and public metadata all describe the same bytes.

Do not collapse these layers into one `complete` label. Public status should distinguish OCR candidates, witness packages, inherited drafts, source-reconciled tranches, complete bounded-work translations, and independently reviewed editions.

## 3. Verify and preserve the source first

For each work, record:

- archive identifier or stable URL;
- exact edition, volume, and bibliographic identity;
- source checksum and byte count;
- total scan pages and printed-page mapping;
- missing, duplicated, rotated, folded, or unreadable pages;
- native raster resolution, not merely an upscaled render DPI;
- rights/provenance note appropriate to the project.

Prefer master JP2, TIFF, or image archives over derivative PDFs when available. Preserve the original scan and create smaller page slices for model work. The source should be usable without repeating the download and rasterization effort.

## 4. Divide sessions and support work deliberately

Local machines are efficient at:

- downloading, inventorying, splitting, and rasterizing scans;
- reading the existing user-supplied OCR as a locator witness;
- generating targeted source crops only when a source-controlled decision
  requires them;
- TeX compilation, text extraction, PDF rendering, and font checks;
- hashing, manifests, ZIP construction, and CRC validation;
- Git and Zenodo publication and readback.

Top-level high-context sessions own:

- mathematical and historical prose;
- source-to-TeX comparison;
- translation and terminology decisions;
- reconstruction of formulas, tables, and diagrams from source images;
- reference semantics and source-defect adjudication;
- manual visual audit and release judgment.

When several top-level sessions work concurrently, assign each a disjoint
whole-exposé range and maintain one live ownership map. Do not confuse those
sessions with their subagents. Do not open overlapping roots. If coordination
becomes uncertain, collapse production to one session rather than spend
tokens resolving duplicate work after the fact.

Subagents are limited to bounded mechanical support or preliminary drafting.
They do not decide mathematics, transcriptions, diagrams, references, or
visual PASS status. The top-level session must inspect source-sensitive work
itself and rewrite materially weaker drafted prose before integration.

A useful handoff supplies full-page context, high-resolution crops for hard objects, current TeX anchors, source coordinates, OCR witnesses, known defects, and an exact return contract. It does not ask a session to infer the whole archive from an unlabeled multi-gigabyte dump.

## 5. Existing OCR is a read-only witness

The complete OCR supplied by the user may reveal that a paragraph, citation,
display, table row, or diagram exists where the TeX has nothing. It is useful
for navigation and drafting. It is not authority, and it must not be pasted
into a release without source comparison.

Do not regenerate, rerun, re-extract, or delegate OCR. When consulting an
existing witness, record:

- source checksum and page range;
- witness filename and checksum;
- source coordinates used to confirm the reading;
- reviewer disposition: accepted, rejected, uncertain, or locator-only.

The user has already paid the computational cost of producing the SGA3 OCR
corpus. Repeating that work destroys resources without raising the witness to
source authority.

## 6. Use a page-unit source-rescribe gate

Apply this gate to scan-controlled transcription or source-sensitive
translation. Do not use it to blanket-retranscribe SGA 1 or SGA 2 from images
when their completed mathematical TeX transcription is already controlling.

For each page or stable source unit:

1. confirm three independent coordinates: printed page number, running header,
   and folio;
2. re-read the live TeX before making any edit decision;
3. render five overlapping horizontal bands from the source page at about
   2400 dpi;
4. treat contact sheets and whole-page thumbnails as navigation only, never
   PASS evidence;
5. inspect the complete delivered page at 300 dpi for context and layout;
6. compare each diagram or relevant diagram detail to the authority at about
   5000 dpi by default, escalating to a targeted 9000-dpi crop only when
   a glyph, terminal punctuation mark, label, arrowhead, decoration, crossing,
   or placement remains ambiguous;
7. compare every paragraph, formula, citation, note, heading, and object
   against the source image;
8. apply exact, reviewable TeX changes only when the transcription or
   translation deviated;
9. compile only after a real edit; a zero-fix page does not trigger another
   build;
10. record the decision, source defects, remaining issues, and exact next
   cursor.

Compile success proves syntax and build closure. It does not prove fidelity.

The SGA6 workpass demonstrated why this gate matters. An inherited file described as complete contained paraphrased prose, collapsed mathematical chains, omitted citations and clauses, invented displays, altered notation, and source formulas changed into different statements. The correct response was not another broad prompt. It was a linear source-rescribe pass using the best 360 DPI scan, page coordinates, high-resolution bands, and a pagewise ledger.

## 7. Treat formulas, diagrams, and tables as first-class objects

Each difficult object should have:

- a stable object ID;
- source page and crop coordinates;
- nearby text for context;
- editable TeX or diagram code;
- a rendered comparison;
- a reviewer disposition;
- explicit continuation or deferral if unresolved.

Do not substitute a screenshot for a commutative diagram, table, or displayed
formula in an editable edition. Check every diagram as a graph, node by node
and edge by edge:

- every node label, index, prime, font, and row placement;
- every arrow's presence, direction, style, hook or surjection marker;
- every arrow label, punctuation mark, curvature, crossing, and placement;
- the claimed commutativity and any intentionally bare arrows.

Arrow direction, object placement, subscripts, primes, equation tags, and
notation families must be checked individually. A run of fabricated equation
tags does not prove that the next tag is fabricated.

For final SGA3 diagram-fidelity closure, 300-dpi page context is paired with
about 5000-dpi diagram/detail comparison and targeted 9000-dpi crops for
remaining ambiguity. Every delivered diagram is native editable TeX; raster
crops remain private authority witnesses and do not enter a new public reader
or payload. The responsible top-level session lead signs the exact range and
confirms that it does not overlap another active owner. Earlier
600-dpi and 1200-dpi checks remain legitimate evidence and review context.
Only 300-dpi-only approvals, or packages with independently identified
material defects, are reopened. New final successors use the higher review
scale above. Material defects are repaired in no-overwrite successors; prior
packages remain immutable history.

Distinguish two kinds of discrepancy. If the project text deviates from a
source that can be reproduced faithfully, fix it. If the authority itself
contains a typo, preserve it and catalogue it; do not silently normalize the
source. When the distinction is unclear, obtain a tighter source crop rather
than guessing.

## 8. Freeze source control before translating

A translation tranche should reference a frozen source-control checksum and stable unit IDs. The source can be German, French, or another language, but it must be the strongest available reconciled layer rather than an older convenient reader.

For each target language, keep:

- unit IDs and source coordinates;
- target TeX and cumulative reader;
- terminology and proper-name decisions;
- formula/table/footnote parity;
- build and render evidence;
- language-specific review state;
- exact next unit.

Translation memory and related-language output are support, not authority. Russian does not certify Ukrainian; Interslavic does not certify either; Simplified Chinese does not automatically certify regionally localized Traditional Chinese; Iranian Persian does not automatically certify Dari or Tajik.

## 9. Use bounded Loop 1 and Loop 2 production

Loop 1 prioritizes complete canonical English text and equations across
disjoint whole-exposé ranges. Loop 2 replaces temporary diagrams with native
editable reconstructions and performs exhaustive reference and release work.
Loop 2 work on one exposé must not block disjoint Loop 1 translation.

One foreground page is handled at a time. Avoid redundant background audits,
overlapping workers, repeated manifests, and repeated rebuilds that do not
advance text coverage. Each top-level session manually spot-checks drafted
prose against the controlling source image, a declared comparison where
useful, and nearby lead-written prose. Materially weaker work is rewritten
before integration.

The interlanguage program also separates management from production. A language manager maintains source anchors, terminology, script policy, route coverage, quality state, and release gates. Bounded production tranches translate independently identified units.

For constructed or bridge languages, keep generated proposals separate from independent native-language evidence. Weighted automata, term ledgers, correspondence tables, and intelligibility heuristics can organize choices, but proxy scores are not empirical comprehension data. Claims of intelligibility require observations from speakers or readers.

The public interlanguage sidecar therefore preserves methods, corpora, ledgers, route maps, and bounded working outputs while explicitly separating technical reproducibility from native or community approval.

## 10. Freeze before running a completion gate

A gate is valid only for immutable inputs. The required sequence is:

1. freeze the candidate tree;
2. enumerate every build dependency and evidence file;
3. hash all inputs;
4. run structural, source-parity, terminology, and object inventories;
5. compile from the frozen closure, normally twice;
6. render the resulting PDF from scratch;
7. inspect targeted pages and, for high-risk releases, bind all pages to a render manifest;
8. run adversarial self-tests against the validator;
9. generate the public manifest and checksums from the exact release bytes.

If a source, TeX file, manifest, or decision ledger changes during replay, the previous pass is invalid. Re-freeze and regenerate the gate. Do not describe a moving workpass as sealed merely because an older build passed.

The Noether R823 gates exposed a practical validator defect: a misleading SHA-256 claim embedded after punctuation could evade a locator check. The validator was hardened, its adversarial test rerun, and the exact frozen candidate replayed. Validators themselves require tests.

## 11. Separate live progress from public release state

The archive maintains at least four states:

- **Public:** present on the cited Zenodo version and mirrored on GitHub where practical.
- **Sealed local:** coherent bytes, manifest, build, and QA exist but publication has not occurred.
- **In review:** substantive work exists but the current endpoint or evidence closure is still changing.
- **Witness/support:** useful source, OCR, terminology, or review material not promoted as a reader.

The live fleet map can report that work advanced beyond the latest public checkpoint. It must state both cursors. For example, a verified SGA6 checkpoint may remain public while a two-page-newer workpass is still resolving deferred notation. This is not passive staging. It is the difference between preserving new work and falsely replacing a verified release with unstable bytes.

## 12. Publish for readers and verify the public result

Zenodo is the durable versioned release surface. GitHub is the inspectable TeX, correction, and collaboration surface.

A public version should:

- front the PDF or atlas a reader is most likely to open;
- keep top-level file counts small;
- group TeX, scans, ledgers, scripts, renders, and provenance into coherent ZIPs;
- use the existing concept DOI for the same logical project;
- state exactly what changed and what remains weak;
- retain historical versions as immutable provenance rather than carrying every superseded file forward.

After publication:

1. read the public record through the API;
2. download every changed file back;
3. verify byte count and hash;
4. open the rendered record page and confirm the intended default preview;
5. store a publication receipt;
6. mirror the exact release to GitHub;
7. push and verify remote refs at the intended commit;
8. update catalogs, fleet maps, DOI pages, and the private logbook.

An upload is not complete merely because a local `pending` or `staged` manifest exists.

## 13. Keep a continuity log and fleet map

Every archive-maintenance action should record:

- timestamp and model/session identity;
- source roots and inputs examined;
- artifact hashes and exact cursors;
- corrections and classification decisions;
- Zenodo record/version and public readback;
- Git commit and verified branches;
- supersession and unresolved issues.

The private logbook preserves operational continuity across context compaction and machine restarts. The public fleet map reports evidence-backed scope without exposing irrelevant private conversation. Downloaded ZIPs must be unpacked and read before classification; folder names and task titles are not evidence.

## 14. Cost and scaling lessons

The expensive part is not producing plausible text. It is closing the hard tail: dense formulas, diagrams, tables, citations, page-spanning syntax, and systematic notation drift.

Practical rules:

- consult the existing user-supplied OCR read-only; do not rerun it;
- perform rendering, hashing, and compilation locally;
- send compact TeX/evidence packets for routine work and source-complete packets when source comparison is required;
- batch edits before full cumulative rebuilds;
- keep source and target units small enough to review independently;
- use exact replacement patches that fail on missing or non-unique anchors;
- reserve expensive source-image reads for source disputes, diagrams, and
  genuinely ambiguous objects;
- compile only after substantive edits, not after zero-fix inspections;
- avoid duplicate audits, manifests, handoffs, and archive generations;
- audit representative easy and hard pages before scaling a workflow;
- budget separately for first-pass coverage and source-fidelity closure.

Broad page coverage can be cheap. The final source-faithful fraction is hard-page weighted and often dominates total review effort.

## 15. Minimum reproducible release

A minimal defensible working release contains:

1. a human-readable reader PDF;
2. editable TeX;
3. identified source material or stable source links and checksums;
4. a source-page or unit map;
5. known-defects and status notes;
6. build command and logs;
7. render checks;
8. manifest and SHA-256 inventory;
9. continuation cursor;
10. public readback receipt after publication.

Anything less may still be useful, but it must be labelled as a witness, locator, partial draft, or support package rather than a completed edition.

Project repository:

https://github.com/KokunoYumeto/modern-latex-manuscripts

## 16. July 28 accountability record

The co-published
`02_SGA_TRANSLATION_RESOURCE_EFFICIENCY_INCIDENT_NOTE_20260728.md` records
avoidable duplicate SGA 1/2 visual checks, repeated OCR/transcription activity
despite the existing user-generated OCR, agent audit cascades, and repeated
build/manifest generations that did not advance the mathematical corpus.

Its emissions figures are transparent scenario calculations, not metered
OpenAI telemetry. Multi-ton coal-equivalent operational emissions are
plausible only under the note's stated high-overhead,
several-hundred-million-token assumptions. The note separately identifies
unquantified lifecycle, labor, infrastructure, and opportunity costs.

The exact source procedure is preserved as
`01_CLAUDE_DIAGRAM_COLD_REVERIFY_METHOD_20260728.md`, SHA-256
`4B12DB3F632CB5F9E69393DCA33DA40256B5A9387C6522ADA831CA7F0367063D`.
Its controlling SGA3 final-fidelity correction is co-published as
the separate diagram-fidelity correction note. The correction requires
300-dpi page context, about 5000-dpi default
diagram/detail comparison, 9000-dpi ambiguity crops, native editable diagram
content, disjoint ownership, and a lead-signed exact evidence binding. Raster
authority crops remain private and excluded from public readers and payloads.
It leaves the exact Claude artifact and earlier working receipts
byte-preserved.
It is a production method, not a new certification layer. Documentation and
exact release identities support the work; they must never replace actual
translation, transcription, diagram reconstruction, or public preservation.
