---
title: "AI-Run Modern LaTeX Manuscript Workflow"
subtitle: "Replication Packet"
date: "Version 2026-07-18: frozen gates, translation fleets, and public readback"
---

This document describes the workflow actually used by the Modern LaTeX Manuscripts project. The process is AI-run under human direction. Local machines perform source intake, OCR and image preparation, compilation, hashing, packaging, and publication. High-context model sessions perform bounded transcription, translation, and source comparison. Deterministic gates decide what may be promoted.

This is a workflow record, not a certification of any manuscript. A successful build, a large page count, a green validator, or a filename containing `complete` does not prove source fidelity.

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

## 4. Divide local and high-context work deliberately

Local machines are efficient at:

- downloading, inventorying, splitting, and rasterizing scans;
- GPU OCR, VLM extraction, formula-crop generation, and page classification;
- TeX compilation, text extraction, PDF rendering, and font checks;
- hashing, manifests, ZIP construction, and CRC validation;
- Git and Zenodo publication and readback.

High-context sessions are efficient at:

- mathematical and historical prose;
- source-to-TeX comparison;
- translation and terminology decisions;
- reconstruction of formulas, tables, and diagrams from labelled witnesses;
- adversarial review of claimed completion.

A useful handoff supplies full-page context, high-resolution crops for hard objects, current TeX anchors, source coordinates, OCR witnesses, known defects, and an exact return contract. It does not ask a session to infer the whole archive from an unlabeled multi-gigabyte dump.

## 5. OCR and GPU extraction are omission witnesses

OCR is most valuable as a prose-completeness and localization layer. It can reveal that a paragraph, citation, display, table row, or diagram exists where the TeX has nothing. Formula OCR can provide a candidate for a tightly cropped expression. Neither should be pasted into a release without source comparison.

Record how a witness was generated:

- source checksum and page range;
- rasterization DPI, color mode, and preprocessing;
- crop coordinates;
- tool, model, and version;
- environment and CPU/GPU mode;
- raw output and normalized output;
- reviewer disposition: accepted, rejected, uncertain, or locator-only.

The project has used an RTX 4080-class GPU to make witness generation cheaper than repeatedly spending model vision context. The cost saving is real, but it does not raise the witness to source authority.

## 6. Use a page-unit source-rescribe gate

For each page or stable source unit:

1. confirm the scan coordinate and printed-page identity;
2. render ordinary text pages into roughly three overlapping bands;
3. use five or more bands, object crops, or higher native resolution for dense mathematics, diagrams, tables, and ambiguous glyphs;
4. compare every paragraph, formula, citation, note, heading, and object against the source;
5. apply exact, reviewable TeX changes;
6. compile and render the affected region;
7. record the decision, remaining deferred issues, and next cursor.

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

Do not substitute a screenshot for a commutative diagram, table, or displayed formula in an editable edition. Arrow direction, object placement, subscripts, primes, equation tags, and notation families must be checked individually. A run of fabricated equation tags does not prove that the next tag is fabricated.

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

## 9. Use language managers and bounded production tranches

The interlanguage program separates management from production. A language manager maintains source anchors, terminology, script policy, route coverage, quality state, and release gates. Bounded worker tranches translate independently identified units.

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

- perform OCR, rendering, hashing, and compilation locally;
- send compact TeX/evidence packets for routine work and source-complete packets when source comparison is required;
- batch edits before full cumulative rebuilds;
- keep source and target units small enough to review independently;
- use exact replacement patches that fail on missing or non-unique anchors;
- reserve expensive image reads for source disputes and hard objects;
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
