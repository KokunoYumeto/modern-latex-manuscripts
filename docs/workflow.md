# Workflow Notes

The project workflow is deliberately redundant: raw source packets are preserved, while clean public records present the best current reader PDFs and organized artifacts.

## Typical Path

1. Identify public-domain or otherwise suitable source material.
2. Download scans or source PDFs.
3. Produce initial TeX with automated transcription.
4. Compile and repair into readable PDFs.
5. Review against source scans.
6. Translate where useful.
7. Publish a coherent reader/source checkpoint.
8. Track corrections, superseded generations, and future work in GitHub.

## Provenance Model

The archive is machine-assisted and source-checkable by design.

| Stage | Role |
|---|---|
| Work selection | Coverage maps and project notes identify older works worth transcribing, translating, or rescuing from scan-only access. |
| Source acquisition | Contributors gather public scans, source PDFs, and existing open TeX where available, then record exact source identities and hashes. |
| Draft transcription | Automated transcription systems produce first-pass TeX, often in parallel across many sections or works. |
| Review and repair | Reviewers and automated tools compile, inspect, repair, organize, and compare outputs against source witnesses. |
| Translation | Translation drafts are produced when useful, then kept as front-facing reader PDFs if they are readable enough to inspect. |
| Publication | A coherent checkpoint presents readable editions first and preserves editable source, manifests, checks, and provenance alongside them. |

This means a public PDF should be treated as a working scholarly draft unless its record explicitly says it has been proofread. The archive aims to make correction easy: every useful public reader should have TeX or source/provenance material nearby.

## Public File Roles

Reader PDFs are the public browsing surface. They should be named by author, work, language when helpful, and draft status when the text is not final.

Artifact ZIPs are not meant to be pretty. They preserve TeX, source witnesses, OCR text, render checks, source packets, and provenance so the reader-facing PDF can be checked and rebuilt.

Name files by role, not optimism. Use `OCR_candidate`, `formula_witness`, `crop_witness`, or `locator_aid` for machine-extracted or unpromoted material. Use `working_draft`, `source_checked`, `reader`, or `cumulative` only for TeX/PDF that has been compiled and checked to the declared level against source witnesses. A file named `reader` should be readable as an edition draft; a file named `OCR_candidate` should be understood as evidence for repair, not as a mathematical edition.

This distinction should also be reflected in Zenodo descriptions. Do not describe an OCR-derived TeX scrape as a working edition. Conversely, when a multilingual or source-checked reader is genuinely usable as a mathematical draft, say so plainly while preserving the caveat that important equations, tables, and diagrams should still be checked against the source.

Manifest/status files explain what is included, what passed technical checks, and what still needs review. They should be short enough to read and precise enough to act on.

The 2026-06-29 Noether web-memo digest sharpened this into a practical rule: the German/source branch should not be outrun by translations. Translation branches can be valuable before full certification, but public metadata should say whether the underlying source branch is only a current-base survival check, a targeted source-certain patch, a source-limited best-available closure, or a fuller page/table/formula audit. Reader TeX/PDF should stay separate from apparatus/provenance ledgers so that useful translations are easy to find without hiding uncertainty.

## Artifact Classification And Promotion

A newly found ZIP or directory name is evidence of an artifact, not evidence of
its scholarly state. It may contain a current reader, a superseded handoff, a
source-witness bundle, a scan master, an OCR locator aid, or a suspect draft.
Read its manifest and represented scope before describing it publicly.

A 2026-06-28 intake audit made this explicit: the largest newly indexed
families mixed repair packets, OCR witnesses, source-audit material,
multilingual support, continuation packets, and reader candidates. They belong
in author-level coverage maps and provenance ledgers, not in an undifferentiated
file dump.

Before promoting a package, check its README, manifest, build logs, and
source/audit ledgers. Classify it as a front-facing reader/current TeX, compact
source-support rollup, provenance/source witness, workflow-method evidence,
superseded/backstop material, or unpublished repair queue. When the reader is
the main scholarly object, present it before the supporting audit bundles.

For the vocabulary used to describe draft quality, see the [quality rubric](quality-rubric.md).

## Recovered Workflow Artifacts

Some earlier workflow material remains as historical evidence rather than as a
current edition claim. It includes OCR scripts under
[`scripts/ocr`](../scripts/ocr/README.md), Cayley cost/coverage notes under
[`workflow/audits`](../workflow/audits/cayley-raw-efficiency-note-20260603.md),
non-European public-surface audits under
[`workflow/audits/non-european-public-surface-current`](../workflow/audits/non-european-public-surface-current/README_FOR_WEB_SESSION.md),
and June 2026 status manifests under
[`manifests`](../manifests/current_archive_status.md).

These files are useful for reproducing the process and understanding failure modes. They should not be read as later certification of the mathematical accuracy of any reader unless a current record page or audit ledger explicitly says so.

## Quality Checks

A technical audit means that a file opens, has plausible page counts, has no configured public naming problems, and does not trip the current surface checks. It does not mean the mathematics has been proofread.

The strongest review is source comparison: open the reader PDF, open the source scan or reference PDF from the artifact ZIP or record, and check page order, theorem numbering, displayed formulas, diagrams, tables, and cross-references.

## Witness-Aid Handoff Packages

The most useful handoff is not a raw OCR dump or a screenshot set. It is a source-faithful witness package that lets the next worker compare current TeX against the source quickly.

Minimum useful contents:

- source PDF or source page images for the covered range;
- source-PDF-page to printed-page map;
- labelled full-page context PNGs;
- labelled 400-600 dpi crops for diagrams, tables, dense displays, special symbols, arrows, accents, subscripts, and superscripts;
- manifest CSV with stable witness ID, source file, source page, printed page, crop box, render DPI, object type, nearby source anchor, current TeX anchor, status, and notes;
- OCR-generation log when OCR is used, including source PDF checksum, page range, rasterization settings, DPI, color mode, crop/preprocessing steps, OCR tool and version, execution environment, raw-output identity, normalized-output identity, and reviewer decision;
- explicit triage status such as `must_promote`, `check_current`, `already_confirmed`, `context_only`, `candidate_unfiltered`, `false_positive`, or `equation_symbol_detail`;
- current-render comparison where available;
- SHA256/provenance notes and method limits.

This structure emerged from SGA, Deligne, Gordan, Kneser, Weber, Sylvester, Cayley, and Maxwell repair work. It is especially important for diagram-heavy or formula-heavy pages: a full-page screenshot is context, but a labelled object crop plus a ledger row is actionable.

Witness packages should distinguish certified repairs from candidate evidence. Detector output and geometry candidates must be labelled as candidates until manually filtered; false positives should be recorded rather than silently removed.

For the object-level diagram/table promotion rule, see [Object-Level Diagram And Table Audit](workflow-addendum-20260612-object-level-audit.md). The short version is: full-page screenshots and contact sheets are orientation aids, not authority. Diagram/table promotion needs a source object witness, an output render witness, an object ID, and an explicit verdict in a ledger.

## Page-Unit Audit Harnesses

A reusable 2026-06-24 pattern is now visible across SGA6, Weber, and Steinitz: build a page-unit audit harness around the best cumulative TeX, not around raw OCR drops. The harness should declare the canonical TeX file, the source scan, the printed-page to PDF-page offset, any offset drift, and the exact scope of ready audit units. The queued SGA6 harness makes this concrete: the mature cumulative French `sga6_fr.tex` is the audit basis, the original SGA6 scan is ground truth, and Kimi OCR drops are locator-only.

Raw OCR drops can be valuable, but only as locator aids. In the SGA6 harness, Kimi OCR drops are explicitly not the transcription basis; the audit basis is the mature cumulative French `sga6_fr.tex`, while the original scan remains ground truth. A July 2026 SGA6 source-rescribe pass sharpens that rule further: a compile-clean, mature-looking TeX branch can still be a paraphrased scaffold if earlier repair rounds compressed source prose. When source sampling finds scaffold behavior, stop treating the branch as the audit authority; use it only as a navigation layer, switch to the best available scan, and rewrite page bands source-first with explicit cursor and compile logs. In Weber, the useful scaffold is a 1720-page manifest across the three volumes with volume-specific source scans and offsets. In Steinitz, only the 1910 `Algebraische Theorie der Körper` pages with explicit `\sourcepage{}` markers are truly page-unit audit-ready; other works with good TeX but no page anchors are spot-audit ready until page markers are added.

The July 10 SGA6 continuation gives a concrete failure catalogue for that rule. Direct scan comparison found a page compressed to two paraphrased lines, dropped proof paragraphs, an invented lemma statement, a wrong identity value (`0` where the source has `1`), altered lambda/gamma notation, and equation tags added where the scan has none. It also confirmed that a nearby `(5.3.1)` tag is genuine. Therefore equation numbers, theorem statements, arrow directions, and notation families must be verified object by object against the source; a run of fabricated tags does not justify deleting the next tag by pattern. Compile success and visual plausibility remain necessary gates, not fidelity evidence.

The recommended harness contents are:

- one manifest row per audit unit, with work, source file, printed page, PDF page or scan image, TeX file, and TeX line/page anchor;
- a chunk-on-demand renderer that produces high-detail page crops only for requested pages;
- explicit source-quality notes, including DPI, scan class, and any drift in page offsets;
- a statement of which TeX branch is canonical and which older or OCR branches are superseded or locator-only;
- a caveat separating page-unit readiness from whole-work certification.

Do not mass-render thousands of pages unless the next stage actually needs them. Render only the pages or objects being audited, and keep the resulting crops keyed to the manifest row that requested them.

A June 25 SGA5 workpass snapshot adds a stricter find-verify-fix pattern for
source repair. Broad passes can discover likely defects, but the safer scalable
unit is page-local discovery, independent source verification, deterministic
old-string/new-string patching that refuses missing or non-unique matches, and
a compile gate. The preserved method snapshot is
`workflow/AI_Run_Workflow_SGA5_FindVerifyFix_Workpass_Method_20260625.zip`; it
is not a claim that SGA5 is complete.

Audit folders and workpass logs can contain completion language for a page range
or one bounded procedure. Public status must translate that claim rather than
copy it uncritically. A `full audit`, `workpass complete`, `source checked`, or
`certified` label means evidence exists for the stated scope; it does not by
itself establish a critical edition, whole-work source closure, or safe
mathematical reliance. State the actual evidence level: page-local workpass,
source-witnessed tranche, anti-regression bridge, source-routing packet, or
human-certified closure.

A June 25 Weber adaptation shows how the method changes when the starting TeX
is not faithful. German transcription comes first: audit omitted lines,
compressed prose, missing formulae, wrong symbols, and editorial additions
before treating English translation as a production axis. The available source
images were below the declared 650-ppi dense-math threshold, so difficult
formula checks require targeted crops and explicit uncertainty. The preserved
method packets record the exact ranges. By 2026-07-02, source-checked German
retranscriptions or faithful checks covered sections 141, 148, 149, 151,
153–156, 158, 162, 163, 165, and 167–183, while sections 69, 138, p.466, and
184 onward remained open. Broad scans are useful for locating defects; once a
section is shown to be fabricated or heavily compressed, controlled
page-by-page retranscription is safer. Keep the page-count compile gate: the
working reader grew to 410 pages as omitted content returned, so a sudden drop
or implausibly fast “all clean” result is a warning.

## Failed-Web Salvage Packets

Failed or crashed web-review runs can still contain useful evidence, but they must be packaged as salvage and locator material, not as reader patches. The safe pattern is to preserve the transcript excerpts, source pointers, candidate TeX context, and next-action notes in a deliberately labelled packet with a README, `do_not_promote` or no-fix-trap ledger, salvaged-items ledger, source-quality note, and checksums where available.

The public rule is simple: a failed run may identify where to look; it does not itself certify what to print. OCR snippets, visual impressions, partial reconstructions, and crashed-response prose are locator evidence until a later pass checks the source scan, edits the TeX intentionally, records confirmed fixes, compiles the result, and states what remains open. This pattern is now used for Noether Paper 42 salvage material: the RA10/P42 package preserves useful scan and apparatus leads, while explicitly saying that Paper 42 remains open and that no cumulative patch is proposed.

When a salvage packet is useful, queue it as provenance or workflow evidence. Do not front it as a reader-facing edition, paper closure, or corpus certification. If the record is file-count constrained, fold the salvage into one compact source-support rollup instead of uploading many failed-run artifacts one by one.

## Evidence-Packet Review Workflow

The scalable pattern separates evidence preparation from mathematical review.
An evidence packet supplies source identities, page maps, targeted crops, OCR
witnesses, current TeX anchors, and checksums. A reviewer uses that bounded
packet to translate, repair, and compare the draft against the source. Keeping
those roles explicit makes omissions, flattened diagrams, and symbol-level
mismatches easier to locate and independently recheck.

Send compact, labelled evidence rather than indiscriminate image batches. A
good packet contains source PDF slices, full-page context where needed,
high-resolution crops for diagrams or formula regions, OCR prose witnesses,
current TeX anchors, and a manifest explaining every object. Use OCR as a gap
detector and prose witness, not as authority. A suspected skipped paragraph
still has to be checked against the source image before promotion.

High-DPI witness images are expensive in model context but often necessary. Commutative diagrams, cumulative diagram sequences, long arrows, small subscripts, accents, table rules, and dense symbolic displays can be misread at ordinary preview resolution. For these pages, a 150-200 dpi full-page image supplies orientation, while 400-600 dpi object crops supply the actual evidence. The packet should make clear which crops are mandatory repair targets, which are context only, and which are candidate detections.

Scan quality is a first-order method variable. Bad scans or overcompressed page images can create false confidence: a draft may look plausible while silently compressing text, flattening diagrams, or normalizing symbols that differ in the source. The Gordan repair lane showed the same lesson from the opposite side: OCR and source crops can be excellent gap detectors only when the underlying scan is good enough to support the claim. A later Cayley source audit added a concrete rule: Internet Archive derivative PDFs may be far lower resolution than the available `_jp2.zip` master image archives, so source-audit repair should verify the scan class and prefer master JP2 images plus scan-page maps where possible. When a repair lane stalls or produces inconsistent output, first check whether the source image is good enough. If not, obtain a better scan or use a higher-resolution source crop before asking for another translation pass.

This method is more reproducible than blind rereading. Use OCR/prose witnesses
and object ledgers to identify likely gaps, inspect only the relevant page or
crop evidence, and return accepted, rejected, or uncertain findings with exact
source-page references.

## Constructed And Semi-Constructed Language Lanes

The Noether Slavic/Interslavic lane adds a separate workflow lesson. Translation into Ukrainian and Russian can be checked against established mathematical registers, but Interslavic is both a mathematical translation branch and a linguistics/register-construction artifact. It should therefore be archived as the whole working apparatus, not only the rendered reader: TeX/PDF outputs, source-control notes, logbooks, glossaries, rejected or uncertain terms, script-conversion rules, and generalizability notes all belong in the package. Interslavic is better understood as constrained register construction: the AI is not an authority inventing a language, but a proposal, consistency, and audit engine for candidate technical terminology.

For semi-constructed-language work, keep the terminology trail as a first-class artifact. The package should include rendered PDFs, TeX, glossaries, term ledgers, script-conversion rules, review flags, and notes explaining why recurring technical terms were selected. Weak, coined, or institution-forming terms should be labelled for human/community review rather than silently frozen into the public record.

When a lane has multiple scripts, use one lexical authority branch and generate reader variants from it only when the transformation is explicit and auditable. In the Noether package, Latin Interslavic is treated as the working lexical authority, while Cyrillic Interslavic is a deterministic reader variant requiring separate visual and text-layer checks. Citation islands, proper names, Roman numerals, TeX commands, and mathematical identifiers must be protected from blind transliteration. Public metadata should say when such a package is a translation/register-construction checkpoint and should point readers to the included logbooks and term ledgers as part of the scholarly object.

Mathematics is a good pilot domain for this because formulas, theorem structures, and repeated proof patterns provide anchors. Those anchors do not eliminate responsibility: they make inconsistent terminology easier to find and review. Public descriptions should therefore describe such packages as translation/register-construction handoffs or checkpoints unless a later human review certifies the language branch.

The Noether Slavic lane is a representative example. The 2026-06-14 Papers 01-21 handoff showed why the whole apparatus matters: the rendered Ukrainian, Russian, Interslavic Latin, and Interslavic Cyrillic readers were useful translation artifacts, while the constructed-language reflection/logbooks exposed terminology and mojibake issues that reader PDFs alone would hide. The current public-safe checkpoint is file 117 on the Noether record, covering Papers 01-33 and Paper 34 section 02. It deliberately preserves TeX, cumulative readers, logbooks, terminology/provenance/audit material, and deterministic Latin/Cyrillic conversion tooling while excluding modern third-party reference PDFs. It still belongs in the archive as a translation/register-construction checkpoint with caveats, not as source-closed terminology data or a critical edition.

## Publication Rule

Availability and provenance matter, but the public surface should not look like a raw tool dump. When a source packet has internal run names, partial folders, or repair logs, keep those inside artifact packages and give the public landing a human title organized by author, work, corpus, or mathematical tradition.

Public-facing titles should name the author, work, language/status where needed, and role. Internal run names should stay inside raw provenance archives, not in landing titles or top-level filenames.

For large, iterative translation projects, separate working evidence from the reader surface. A working-evidence package may contain audits, screenshots, source slices, failed attempts, render checks, and intermediate TeX. Preserve that provenance, while fronting the mathematical deliverables: individual paper PDFs/TeX, cumulative language branches, source/witness packages, concise correction ledgers, and a short status note that says what is source-checked, what is OCR-derived, and what remains provisional.

This is especially important for multilingual records. Do not make readers sort through dozens of audit bundles to find the translation. Put the clean language branch first, package each language or source branch coherently, and keep audit bundles as supporting QA evidence or deliberately labelled provenance. The Noether and SGA repair streams showed why this matters: raw audit bundles are essential for repair, but top-level records should foreground the usable German/source, English, Spanish, Japanese, French, Chinese, or other reader artifacts and their reliability labels.

For a standalone statement of this rule, see [Curated Public Surfaces](workflow-addendum-20260612-curated-public-surfaces.md).

## Current Review Loop

1. Run the public archive readability audit.
2. Run the public PDF surface audit.
3. Check the newest source packets against the current public summaries.
4. Front the clearest coherent current reader without deleting, overwriting, or silently collapsing any distinct generation.
5. Preserve every predecessor, draft, error, reversal, correction, and supersession; deduplicate containers and transport, never distinct content.
6. Update the archive guide, file catalog, known gaps, and current-status manifest.

Exact filename coverage is not enough for mutable pointer or index packages. A
same-named ZIP may acquire rows, logs, or status corrections. Compare size,
SHA-256, and parsed row counts rather than asking only whether the name is
listed. A no-patch audit package, a source-route pointer, and a cumulative TeX
patchset are distinct objects even when they concern the same author or work.

For the full publication pass, use the [release checklist](release-checklist.md).

## OCR And Math-Extraction Notes

The project workflow can use several open-source OCR/math extraction tools, but their outputs should be treated as witnesses unless a page-specific audit promotes them.

Current tool lessons:

- OCR can be useful as a prose-block comparator. In the Gordan Formensystem audit, OCR text was trimmed to article body, normalized against cumulative TeX, and used to search for likely prose omissions. Formula-heavy low-score blocks were then manually checked. This found no prose omission, and no OCR text was accepted as authority.
- OCR/math OCR is unreliable as insertion-grade TeX unless source checked. It may locate formulas, tables, and diagram regions, and it may provide candidate TeX, but the source scan remains authority.
- Pix2Text can produce useful LaTeX witnesses for modern mathematical display regions. Treat its formula output as a witness, not a final patch. Use visual source comparison before promotion.
- For multilingual text, route by content type. Math/formulas can go to Pix2Text/pix2tex-style tools; modern multilingual print can go to Surya/PaddleOCR-style tools; historical trainable scripts and unusual numeral systems may need Kraken/eScriptorium-style supervised data rather than generic OCR.
- In recorded SGA-style French mathematical-typescript tests, Surya-style OCR was more useful than a conventional OCR baseline for page-level gap detection: prose was usable and formulas often preserved labels, arrows, and subscripts well enough for locator evidence. RapidOCR-style output remained useful for anchors and formula numbers but was weaker for math-bearing prose. Treat this as an engine-selection observation, not an authority claim.
- OCR generated from the wrong scan copy can be actively misleading. A whole-volume OCR layer may still answer "does this string occur somewhere in the source?", but if it came from a different PDF pagination, chunk/page names must not be used for source-page claims. Page maps and source-file checksums are therefore part of the evidence, not bookkeeping decoration.
- Born-digital PDFs need a separate text-layer check. If a tool such as Marker is lifting a damaged embedded text layer, fresh `force_ocr` may be appropriate: keep the lifted-text baseline, rerun only the affected born-digital files, and compare accent, math-wrapper, artifact, page, and extent diagnostics. Do not spend the same forced-render pass on ordinary image scans that already receive fresh OCR. The 2026-07-19 Deligne/Griffiths IAS receipt at `manifests/source-intake/20260719_claude_ias_force_ocr_deligne_griffiths.md` records this pattern. Even a dramatically cleaner rerun remains locator and completeness evidence until source-page review promotes a reading.
- Dense numeric tables need separate validation. For al-Battani, VLMs could help with Arabic descriptions at sufficient resolution but failed on tiny abjad numerals; printed critical tables with modern numerals were more authoritative for numerical values. For numbers, coordinates, regnal years, and table columns, use range checks, monotonicity checks, known bright-star or known-value checks, and direct page spot checks.
- High-resolution source matters. Cropped/downsampled public packages can make table reconstruction impossible even when the original scan is usable. Derivative PDFs may be only a convenience layer, not the real source; on Internet Archive, check for `_jp2.zip`, `raw_jp2`, and `scandata.xml` masters before treating a PDF as the authority. Always trace table work back to the highest-resolution source scan or a printed critical table before declaring a table missing or unreadable.
- Source-resolution wording must be literal. `600 ppi` in scandata, embedded `600 x 600 PixelsPerInch` in a raw TIFF, raw JP2 pixel geometry with undefined units, and a 1000dpi rasterized inspection crop are different evidence classes. Record which one you have. Do not turn high pixel geometry, derivative-PDF display metadata, or generic `72 dpi` metadata into an optical-DPI claim.
- Source-baseline choice can change the whole lane. A 2026-06-14 Gibbs/Gauss source-quality audit found that Gibbs work should continue from IA raw JP2/scandata sources, with a separate "Equilibrium of Heterogeneous Substances" witness, rather than relying only on derivative PDFs. The same audit found that future Gauss work should use the new GDZ Werke source baseline across Bands I-XII, while treating older IA/Rich/Google PDFs as redundant witnesses or fallback. This is a workflow rule, not a reader claim: changing the source baseline improves future auditability but does not certify older TeX without page-level comparison.
- Keep heavy OCR/ML tools isolated in reproducible environments. Several OCR stacks declare broad `torch` dependencies; unconstrained installation can silently replace an accelerator build with a CPU-only dependency.

When generating OCR, preserve the generation chain. A reproducible OCR witness should say: this source file and checksum were rasterized into these page images, at this DPI and color mode, using this command or script; these crops or preprocessing steps were applied; this OCR/model environment produced this raw output; this normalization script produced this comparison text or candidate TeX; and this recorded review either rejected it, kept it as a locator, or accepted a specific part after source comparison. Do not overwrite raw OCR with cleaned OCR. Keep both layers and make the accepted layer cite back to the raw witness.

The current best practice is conservative: use OCR/math-OCR to localize formulas, tables, diagram regions, and possible prose omissions; keep crops and candidate TeX as witnesses; promote only after visual comparison with the source scan and successful TeX compilation. For dense historical mathematics, a reliable package should include page/region IDs, witness crops, candidate TeX, accepted/rejected/uncertain status, and a short audit note. Candidate TeX should not be pasted silently into public editions.

## Zoom-First Source Adjudication

The 2026-07-01 SGA5 p234 workpass checkpoint sharpened a general rule: before changing a mathematical symbol, subscript, diagram edge, label, or suspicious word, inspect the exact source glyph at enough zoom to decide the discrepancy class. The main classes are editor/transcription error, copied source typo, faithful source oddity, false flag, and layout/cosmetic issue.

This matters because the right action differs. A source-faithfulness deviation should be fixed even if it is mathematically harmless. A copied source typo may need a note or a mathematically forced correction. A faithful oddity should remain. A false flag should be recorded so the same reviewer or future queue does not "fix" it later. OCR and model findings are finders, not judges.

The public-archive consequence is also important: a clean TeX build or compiled
PDF is not source certification, and an audit report with valuable fixes is not
automatically a promoted reader. Status notes should distinguish page-local
workpass evidence, source-audit/provenance, reader quality, and critical-edition
claims.

Standalone addendum queued for the workflow record: `workflow/workflow_addendum_20260701_sga5_zoom_first_source_adjudication.md`.

## Lean Library Candidate Notes

A Lean/Lake toolchain is useful as a selective library-growth lane, not as a bulk transcription verifier and not as certification of a scanned edition. The motivation is simple: Lean needs useful mathematical statements, examples, identities, and lemmas. The practical path is to create small Lean packets for stable theorem statements, definitions, examples, algebraic identities, or calculation lemmas that are useful in their own right and may later become Lean/mathlib-adjacent additions.

Do not use `lake build` success as evidence that a scanned work has been faithfully transcribed. Lean does not see page order, diagrams, typography, source omissions, historical notation, or prose-level mathematical intent unless those have been explicitly formalized. For this archive, Lean is a separate useful-mathematics side lane: TeX remains the reader/source-transcription layer, source scans remain the authority for transcription, and Lean files are candidate formal mathematics/library material.

A June 25–26 Lean side lane produced small buildable classical targets,
including Jordan affine-line group cardinality, Jordan primitive-root count, a
Steinitz perfect-field/Frobenius criterion, and a Weber cubic polynomial
identity. These are useful Lean/mathlib-style candidates, not evidence that the
historical transcription, scans, translations, diagrams, page order, or full
papers are correct. Select formalization targets from the public catalog or a
clear mathematical motivation, not from incidental folder discovery.

Publication policy: do not silently merge arbitrary Lean/library-candidate side material into author records, but do publish useful Lean work somewhere coherent when it is real. A separate Lean/formalization DOI is appropriate for coherent buildable Lean/library candidate material with Lean/Lake/Mathlib metadata, build logs, `#print axioms` logs where relevant, no unadvertised `sorry`, source or motivation anchors, and a theorem-map ledger. Lean files for the split-support/projectification side paper belong with that side DOI or a clearly labelled companion to it, not silently in the historical-transcription author archive unless explicitly cross-referenced.

Recommended use:

- attach Lean files to clearly scoped theorem/calculation IDs or to explicit standalone mathematical-library targets;
- record the Lean version, Lake version, dependencies, and build command;
- keep informal TeX statement, source page, and Lean theorem name linked in a small CSV or JSONL ledger;
- use Lean first on modern algebraic identities, elementary number-theory lemmas, matrix/calculation checks, and small structural statements where definitions are already available in Mathlib;
- avoid claiming large historical papers are "verified in Lean" unless every relevant theorem, definition, and dependency has actually been formalized and reviewed.

## Fabrication As A Source-Audit Failure Mode

The Weber p486-p497 audit added an important guardrail. A draft can contain plausible mathematical prose that is not merely compressed, modernized, or mistranscribed, but fabricated from nearby context. In Weber section 152, the audit replaced an unsourced generated body with the actual Weber source text; in section 153, a six-page permutation-decomposition section was held because the draft condensed, rewrote, and inserted plausible cycle-theory examples not present in Weber.

This is a separate failure mode from OCR noise. Treat fluent mathematical prose as untrusted until it is page-mapped against the scan. The repair rule is: source page first, current TeX second, candidate/OCR readings third. If a section-level rewrite is found, do not accept surgical patches that leave a fabricated frame in place; either re-transcribe the coherent section from source or hold it explicitly.

### Lean library-candidate lanes

Human or AI-assisted work may produce Lean side lanes for selected explicit statements from the transcription corpus or for nearby classical mathematics that would be useful to have in Lean. These lanes are useful Lean/mathlib-style candidate material; they are not archival source-fidelity evidence and not certification of the scanned editions/translations. A Lean lane is release-ready when it includes exact Lake/Lean/Mathlib toolchain metadata, clean build logs, `#print axioms` output where relevant, no `sorry` or failed batch files in the fronted surface, source or motivation anchors, and a human-readable statement distinguishing any historical source statement from the modern formal theorem. Failed files remain explicit adverse provenance rather than being discarded.

### Package-surface verification before upload

A package README can advertise artifacts that are not actually present in the package. Before any public refresh, inspect the archive contents, not just the README. If primary cumulative TeX/PDF files, ledgers, source witnesses, or checksums sit adjacent to a package rather than inside it, mark the package as source-intake/package-QA evidence and request or build a corrected rollup. Naming conflicts such as a Paper 37 README beside a `p35` standalone PDF must be resolved before public presentation.

### Survival Bridges And Source-Search Packets

A no-patch survival bridge is useful when a later cumulative branch should be checked against earlier accepted spans. It can prove that a prior span still survives byte-exactly or normalized-exactly, and it can prevent stale queue rows from being replayed. It does not prove fresh page-level source fidelity.

A source-search packet records which source witnesses were tried, which were rejected, and why a stronger source was or was not obtained. It is source-routing evidence, not a reader edition. If a raw IA/GDZ/JP2 archive is large, keep its checksum and stable source locator in the compact handoff and group the bulk source only in a deliberate source-support rollup.

Public metadata should say "no TeX body patch", "survival/stale-queue prevention", "source-quality blocked", or "source-routing" where appropriate. Do not let these packets become proof, certification, critical-edition language, or reader-facing editions by accident.

## Zenodo PDF-first file ordering

When a Zenodo record has a reader-facing PDF, put that PDF first in the uploaded file list and use a filename prefix such as `00_` if needed. Zenodo previews PDFs natively, so fronting a README/Markdown/status file makes the public surface harder to read. Put short warnings, caveats, or source-status notes in the record description unless the warning itself is the primary deliverable. ZIPs, TeX, ledgers, and audit notes should follow the PDF, not replace it as the first visible object.

A July 2 Weber/SGA status refresh adds another public-archive lesson.
Source-audit ledgers should distinguish the latest workpass cursor from the
scope of a promoted reader package. SGA5's ledger reached p.421 while its
compact promoted delta still stopped at pp.260–265; Weber's Phase 2 German
workpass reached §§167–183 and 410 compiled pages while remaining
unsynchronized with English and non-critical. Automated assistance located
severe failures but also proposed phantom-page fixes, so the safe pattern
remains: locate, inspect the actual scan, apply only source-confirmed edits,
compile, render-check, and publish the caveat with the status.
