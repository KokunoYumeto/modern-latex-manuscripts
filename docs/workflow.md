# Workflow Notes

The project workflow is deliberately redundant: raw source packets are preserved, while clean public records present the best current reader PDFs and organized artifacts.

## Typical Path

1. Identify public-domain or otherwise suitable source material.
2. Download scans or source PDFs.
3. Produce initial TeX with automated transcription.
4. Compile and repair into readable PDFs.
5. Review against source scans.
6. Translate where useful.
7. Publish reader PDFs and artifact ZIPs to Zenodo.
8. Track corrections and future work in GitHub.

## Provenance Model

The archive is machine-assisted and source-checkable by design.

| Stage | Role |
|---|---|
| Work selection | Web review and project notes identify older works worth transcribing, translating, or rescuing from scan-only access. |
| Source acquisition | Codex downloads public scans, source PDFs, and existing open TeX where available, then indexes and hashes local copies. |
| Draft transcription | Automated transcription systems produce first-pass TeX, often in parallel across many sections or works. |
| Review and repair | ChatGPT/Codex and companion agents compile, inspect, repair, combine, rename, and compare outputs against source witnesses. |
| Translation | Translation drafts are produced when useful, then kept as front-facing reader PDFs if they are readable enough to inspect. |
| Publication | Codex stages reader PDFs, artifact ZIPs, manifests, summaries, and metadata, then publishes coherent Zenodo records through the API. |

This means a public PDF should be treated as a working scholarly draft unless its record explicitly says it has been proofread. The archive aims to make correction easy: every useful public reader should have TeX or source/provenance material nearby.

## Public File Roles

Reader PDFs are the public browsing surface. They should be named by author, work, language when helpful, and draft status when the text is not final.

Artifact ZIPs are not meant to be pretty. They preserve TeX, source witnesses, OCR text, render checks, source packets, and provenance so the reader-facing PDF can be checked and rebuilt.

Name files by role, not optimism. Use `OCR_candidate`, `formula_witness`, `crop_witness`, or `locator_aid` for machine-extracted or unpromoted material. Use `working_draft`, `source_checked`, `reader`, or `cumulative` only for TeX/PDF that has been compiled and checked to the declared level against source witnesses. A file named `reader` should be readable as an edition draft; a file named `OCR_candidate` should be understood as evidence for repair, not as a mathematical edition.

This distinction should also be reflected in Zenodo descriptions. Do not describe an OCR-derived TeX scrape as a working edition. Conversely, when a multilingual or source-checked reader is genuinely usable as a mathematical draft, say so plainly while preserving the caveat that important equations, tables, and diagrams should still be checked against the source.

Manifest/status files explain what is included, what passed technical checks, and what still needs review. They should be short enough to read and precise enough to act on.

For the vocabulary used to describe draft quality, see the [quality rubric](quality-rubric.md).

## Recovered Workflow Artifacts

Some earlier Codex-side workflow material lives in the repository as historical evidence rather than as a current public-edition claim. The recovered GitHub-side packet includes local OCR scripts under [`scripts/ocr`](../scripts/ocr/README.md), Cayley cost/coverage notes under [`workflow/audits`](../workflow/audits/cayley-raw-efficiency-note-20260603.md), non-European public-surface audit material under [`workflow/audits/non-european-public-surface-current`](../workflow/audits/non-european-public-surface-current/README_FOR_WEB_SESSION.md), and June 2026 status manifests under [`manifests`](../manifests/current_archive_status.md).

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
- OCR-generation log when OCR is used, including source PDF checksum, page range, rasterization command or settings, DPI, color mode, crop/preprocessing steps, OCR tool, model name, model version or commit when available, Python/conda environment, CPU/GPU mode, raw output path, normalized output path, and reviewer decision;
- explicit triage status such as `must_promote`, `check_current`, `already_confirmed`, `context_only`, `candidate_unfiltered`, `false_positive`, or `equation_symbol_detail`;
- current-render comparison where available;
- SHA256/provenance notes and method limits.

This structure emerged from SGA, Deligne, Gordan, Kneser, Weber, Sylvester, Cayley, and Maxwell repair work. It is especially important for diagram-heavy or formula-heavy pages: a full-page screenshot is context, but a labelled object crop plus a ledger row is actionable.

Witness packages should distinguish certified repairs from candidate evidence. Detector output and geometry candidates must be labelled as candidates until manually filtered; false positives should be recorded rather than silently removed.

For the object-level diagram/table promotion rule, see [Object-Level Diagram And Table Audit](workflow-addendum-20260612-object-level-audit.md). The short version is: full-page screenshots and contact sheets are orientation aids, not authority. Diagram/table promotion needs a source object witness, an output render witness, an object ID, and an explicit verdict in a ledger.

## Page-Unit Audit Harnesses

A reusable 2026-06-24 pattern is now visible across SGA6, Weber, and Steinitz: build a page-unit audit harness around the best cumulative TeX, not around raw OCR drops. The harness should declare the canonical TeX file, the source scan, the printed-page to PDF-page offset, any offset drift, and the exact scope of ready audit units.

Raw OCR drops can be valuable, but only as locator aids. In the SGA6 harness, Kimi OCR drops are explicitly not the transcription basis; the audit basis is the mature cumulative French `sga6_fr.tex`, while the original scan remains ground truth. In Weber, the useful scaffold is a 1720-page manifest across the three volumes with volume-specific source scans and offsets. In Steinitz, only the 1910 `Algebraische Theorie der Körper` pages with explicit `\sourcepage{}` markers are truly page-unit audit-ready; other works with good TeX but no page anchors are spot-audit ready until page markers are added.

The recommended harness contents are:

- one manifest row per audit unit, with work, source file, printed page, PDF page or scan image, TeX file, and TeX line/page anchor;
- a chunk-on-demand renderer that produces high-detail page crops only for requested pages;
- explicit source-quality notes, including DPI, scan class, and any drift in page offsets;
- a statement of which TeX branch is canonical and which older or OCR branches are superseded or locator-only;
- a caveat separating page-unit readiness from whole-work certification.

Do not mass-render thousands of pages unless the next stage actually needs them. Render only the pages or objects being audited, and keep the resulting crops keyed to the manifest row that requested them.

A June 25 SGA5 workpass snapshot adds a stricter find-verify-fix pattern for live source repair. Raw swarm passes can still discover likely defects, but the safer scalable unit is page-local discovery, independent source verification, deterministic old-string/new-string patching that refuses missing or non-unique matches, and a compile gate. That method snapshot is mirrored in `workflow/AI_Run_Workflow_SGA5_FindVerifyFix_Workpass_Method_20260625.zip` and queued for the workflow DOI; it is not a claim that SGA5 is complete.

A June 25 Weber adaptation shows how that method changes when the starting TeX is not a faithful transcription. The corrected priority is German transcription first: audit for omitted lines, compressed prose, missing formulae, and wrong symbols before treating English translation as a production axis. The local source measurement helper found no native Weber scan at or above the 650dpi trust line; the best on-disk sources are about 500-560dpi, so hard formula checks need tight crops and explicit uncertainty flags. The Weber packet is mirrored in `workflow/AI_Run_Workflow_Weber_FindVerifyFix_Audit_Method_20260625.zip` and queued for the workflow DOI. The refreshed GitHub packet now carries the certification/method logs through Band I p185, including p144-p167 small omissions, the p154 sign repair, p160-p161 prose fixes, rejected false/source-typo reversions at p147/p155/p158/p162, p168-p173 dropped-equation restoration/rejects, p174-p179 ratio/section-divider/index-order repairs, and p180-p185 clean/cosmetic/revert-reject evidence. It deliberately excludes bulky source chunks; those should be generated on demand from the page manifest.

## Failed-Web Salvage Packets

Failed or crashed web-review runs can still contain useful evidence, but they must be packaged as salvage and locator material, not as reader patches. The safe pattern is to preserve the transcript excerpts, source pointers, candidate TeX context, and next-action notes in a deliberately labelled packet with a README, `do_not_promote` or no-fix-trap ledger, salvaged-items ledger, source-quality note, and checksums where available.

The public rule is simple: a failed run may identify where to look; it does not itself certify what to print. OCR snippets, visual impressions, partial reconstructions, and crashed-response prose are locator evidence until a later pass checks the source scan, edits the TeX intentionally, records confirmed fixes, compiles the result, and states what remains open. This pattern is now used for Noether Paper 42 salvage material: the RA10/P42 package preserves useful scan and apparatus leads, while explicitly saying that Paper 42 remains open and that no cumulative patch is proposed.

When a salvage packet is useful, queue it as provenance or workflow evidence. Do not front it as a reader-facing edition, paper closure, or corpus certification. If the record is file-count constrained, fold the salvage into one compact source-support rollup instead of uploading many failed-run artifacts one by one.

## Local-To-Web Audit Workflow

The current scalable pattern is a two-lane workflow: local machines prepare source-faithful aid packets, while web-based Pro review threads use those packets to translate, repair, and audit against the source. The two lanes are different on purpose. The local lane is good at downloading, slicing, rasterizing, cropping, OCR, math-OCR witnesses, compilation, checksum manifests, and publication. The web review lane is good at high-context mathematical translation, prose completion, and self-audit when the evidence is packaged clearly. This became explicit in SGA and Deligne repair work: local Codex packets supplied page maps, high-detail diagram/formula crops, OCR prose witnesses, and current TeX anchors, while the review thread used those witnesses to locate compression, missing prose, flattened commutative diagrams, and symbol-level mismatches.

The local lane should therefore send compact, labelled evidence rather than indiscriminate image bricks. A good packet contains source PDF slices, full-page context images where needed, high-DPI crops for diagrams/formula regions, OCR prose witnesses, current TeX anchors, and a manifest that says exactly what each object is for. The receiving review thread should use OCR as a gap detector and source-level prose witness, not as authority. A prose OCR block can show that a draft has skipped a paragraph; the repair still has to be checked against the source image or scan before promotion.

High-DPI witness images are expensive in model context but often necessary. Commutative diagrams, cumulative diagram sequences, long arrows, small subscripts, accents, table rules, and dense symbolic displays can be misread at ordinary preview resolution. For these pages, a 150-200 dpi full-page image supplies orientation, while 400-600 dpi object crops supply the actual evidence. The packet should make clear which crops are mandatory repair targets, which are context only, and which are candidate detections.

Scan quality is a first-order method variable. Bad scans or overcompressed page images can create false confidence: a draft may look plausible while silently compressing text, flattening diagrams, or normalizing symbols that differ in the source. The Gordan repair lane showed the same lesson from the opposite side: OCR and source crops can be excellent gap detectors only when the underlying scan is good enough to support the claim. A later Cayley source audit added a concrete rule: Internet Archive derivative PDFs may be far lower resolution than the available `_jp2.zip` master image archives, so source-audit repair should verify the scan class and prefer master JP2 images plus scan-page maps where possible. When a repair lane stalls or produces inconsistent output, first check whether the source image is good enough. If not, obtain a better scan or use a higher-resolution source crop before asking for another translation pass.

This aid-packet method is not free, but it is cheaper and more reproducible than blind rereading. Local rendering, cropping, OCR, and TeX compilation cost CPU/GPU time rather than model tokens. The expensive part is making a model inspect many images. Use OCR/prose witnesses and object ledgers to reduce that cost: identify likely gaps locally, send only the relevant page/crop evidence, and require the review thread to return accepted/rejected/uncertain statuses with source-page references.

## Constructed And Semi-Constructed Language Lanes

The Noether Slavic/Interslavic lane adds a separate workflow lesson. Translation into Ukrainian and Russian can be checked against established mathematical registers, but Interslavic is both a mathematical translation branch and a linguistics/register-construction artifact. It should therefore be archived as the whole working apparatus, not only the rendered reader: TeX/PDF outputs, source-control notes, logbooks, glossaries, rejected or uncertain terms, script-conversion rules, and generalizability notes all belong in the package. Interslavic is better understood as constrained register construction: the AI is not an authority inventing a language, but a proposal, consistency, and audit engine for candidate technical terminology.

For semi-constructed-language work, keep the terminology trail as a first-class artifact. The package should include rendered PDFs, TeX, glossaries, term ledgers, script-conversion rules, review flags, and notes explaining why recurring technical terms were selected. Weak, coined, or institution-forming terms should be labelled for human/community review rather than silently frozen into the public record.

When a lane has multiple scripts, use one lexical authority branch and generate reader variants from it only when the transformation is explicit and auditable. In the Noether package, Latin Interslavic is treated as the working lexical authority, while Cyrillic Interslavic is a deterministic reader variant requiring separate visual and text-layer checks. Citation islands, proper names, Roman numerals, TeX commands, and mathematical identifiers must be protected from blind transliteration. Public metadata should say when such a package is a translation/register-construction checkpoint and should point readers to the included logbooks and term ledgers as part of the scholarly object.

Mathematics is a good pilot domain for this because formulas, theorem structures, and repeated proof patterns provide anchors. Those anchors do not eliminate responsibility: they make inconsistent terminology easier to find and review. Public descriptions should therefore describe such packages as translation/register-construction handoffs or checkpoints unless a later human review certifies the language branch.

The Noether Slavic lane is a representative example. The 2026-06-14 Papers 01-21 handoff showed why the whole apparatus matters: the rendered Ukrainian, Russian, Interslavic Latin, and Interslavic Cyrillic readers were useful translation artifacts, while the constructed-language reflection/logbooks exposed terminology and mojibake issues that reader PDFs alone would hide. The current public-safe checkpoint is file 117 on the Noether record, covering Papers 01-33 and Paper 34 section 02. It deliberately preserves TeX, cumulative readers, logbooks, terminology/provenance/audit material, and deterministic Latin/Cyrillic conversion tooling while excluding modern third-party reference PDFs. It still belongs in the archive as a translation/register-construction checkpoint with caveats, not as source-closed terminology data or a critical edition.

## Publication Rule

Availability and provenance matter, but the public surface should not look like a raw tool dump. When a source packet has internal run names, partial folders, or repair logs, keep those inside artifact ZIPs and give the Zenodo record a human title organized by author, work, corpus, or mathematical tradition.

Public-facing titles should name the author, work, language/status where needed, and role. Internal run names should stay inside raw provenance archives, not in Zenodo titles or top-level filenames.

For large, iterative translation projects, separate the workbench from the reader surface. A web-session or agent ZIP may contain audits, screenshots, source slices, failed attempts, render checks, and intermediate TeX. That is useful provenance, but it is not automatically a public reader artifact. The publication step should extract the actual mathematical deliverables: individual paper PDFs/TeX, cumulative language branches, source/witness ZIPs, concise correction ledgers, and a short status note that says what is source-checked, what is OCR-derived, and what remains provisional.

This is especially important for multilingual records. Do not make readers sort through dozens of audit bundles to find the translation. Put the clean language branch first, package each language or source branch coherently, and keep audit bundles as local QA evidence or deliberately labelled provenance. The Noether and SGA repair streams showed why this matters: raw audit bundles are essential for repair, but top-level records should foreground the usable German/source, English, Spanish, Japanese, French, Chinese, or other reader artifacts and their reliability labels.

For a standalone statement of this rule, see [Curated Public Surfaces](workflow-addendum-20260612-curated-public-surfaces.md).

## Current Review Loop

1. Run the public archive readability audit.
2. Run the public PDF surface audit.
3. Check the newest local source packets against the current public summaries.
4. Promote only the clearer or more complete surface material.
5. Preserve older material in artifacts or version history when it is useful for provenance.
6. Update the archive guide, file catalog, known gaps, and current-status manifest.

For the full publication pass, use the [release checklist](release-checklist.md).

## Local OCR And Math-Extraction Tooling Notes

The project workflow can use several open-source OCR/math extraction tools, but their outputs should be treated as witnesses unless a page-specific audit promotes them.

Current tool lessons:

- OCR can be useful as a prose-block comparator. In the Gordan Formensystem audit, OCR text was trimmed to article body, normalized against cumulative TeX, and used to search for likely prose omissions. Formula-heavy low-score blocks were then manually checked. This found no prose omission, and no OCR text was accepted as authority.
- OCR/math OCR is unreliable as insertion-grade TeX unless source checked. It may locate formulas, tables, and diagram regions, and it may provide candidate TeX, but the source scan remains authority.
- Pix2Text has produced useful LaTeX witnesses for modern mathematical display regions in local tests. Treat its formula output as a strong witness, not a final patch. Use visual source comparison before promotion.
- For multilingual text, route by content type. Math/formulas can go to Pix2Text/pix2tex-style tools; modern multilingual print can go to Surya/PaddleOCR-style tools; historical trainable scripts and unusual numeral systems may need Kraken/eScriptorium-style supervised data rather than generic OCR.
- In SGA-style French mathematical typescript tests on a local RTX-class GPU, Surya-style OCR was materially more useful than ordinary CPU OCR for page-level gap detection: prose was usable and formulas often came out LaTeX-like enough to preserve labels, arrows, and subscripts as locator evidence. RapidOCR-style output was still useful for anchors and formula numbers, but much weaker for math-bearing prose. Treat this as an engine-selection lesson, not as an authority claim.
- OCR generated from the wrong scan copy can be actively misleading. A whole-volume OCR layer may still answer "does this string occur somewhere in the source?", but if it came from a different PDF pagination, chunk/page names must not be used for source-page claims. Page maps and source-file checksums are therefore part of the evidence, not bookkeeping decoration.
- Dense numeric tables need separate validation. For al-Battani, VLMs could help with Arabic descriptions at sufficient resolution but failed on tiny abjad numerals; printed critical tables with modern numerals were more authoritative for numerical values. For numbers, coordinates, regnal years, and table columns, use range checks, monotonicity checks, known bright-star or known-value checks, and direct page spot checks.
- High-resolution source matters. Cropped/downsampled public packages can make table reconstruction impossible even when the original scan is usable. Derivative PDFs may be only a convenience layer, not the real source; on Internet Archive, check for `_jp2.zip`, `raw_jp2`, and `scandata.xml` masters before treating a PDF as the authority. Always trace table work back to the highest-resolution source scan or a printed critical table before declaring a table missing or unreadable.
- Source-baseline choice can change the whole lane. A 2026-06-14 Gibbs/Gauss source-quality audit found that Gibbs work should continue from IA raw JP2/scandata sources, with a separate "Equilibrium of Heterogeneous Substances" witness, rather than relying only on derivative PDFs. The same audit found that future Gauss work should use the new GDZ Werke source baseline across Bands I-XII, while treating older IA/Rich/Google PDFs as redundant witnesses or fallback. This is a workflow rule, not a reader claim: changing the source baseline improves future auditability but does not certify older TeX without page-level comparison.
- Keep heavy OCR/ML tools isolated in their own environments. Several OCR stacks declare broad `torch` dependencies; installing them into a working GPU environment can silently replace CUDA builds with CPU wheels.

When generating OCR, preserve the generation chain. A reproducible OCR witness should say: this source file and checksum were rasterized into these page images, at this DPI and color mode, using this command or script; these crops or preprocessing steps were applied; this OCR/model environment produced this raw output; this normalization script produced this comparison text or candidate TeX; and this human or agent audit either rejected it, kept it as a locator, or promoted a specific part after source comparison. Do not overwrite raw OCR with cleaned OCR. Keep both layers and make the promoted layer cite back to the raw witness.

The current best practice is conservative: use OCR/math-OCR to localize formulas, tables, diagram regions, and possible prose omissions; keep crops and candidate TeX as witnesses; promote only after visual comparison with the source scan and successful TeX compilation. For dense historical mathematics, a reliable package should include page/region IDs, witness crops, candidate TeX, accepted/rejected/uncertain status, and a short audit note. Candidate TeX should not be pasted silently into public editions.

## Lean And Formal-Checking Notes

A Lean/Lake toolchain is useful as a selective formal companion layer, not as a bulk transcription verifier. The practical path is to create small formalization packets for stable theorem statements, definitions, examples, algebraic identities, or calculation lemmas after the TeX/source branch is already source-compared. If the Lean file checks, it gives strong evidence that the formalized mathematical claim is internally coherent under the chosen definitions. If it fails, it may reveal a transcription error, a missing hypothesis, a wrong normalization of notation, or simply an incomplete formalization.

Do not use `lake build` success as evidence that a scanned work has been faithfully transcribed. Lean does not see page order, diagrams, typography, source omissions, historical notation, or prose-level mathematical intent unless those have been explicitly formalized. For this archive, Lean should be treated as another audit layer: TeX remains the reader/source-transcription layer; source scans remain the authority; Lean companion files can become machine-checkable witnesses for selected mathematical statements.

Recommended use:

- attach Lean files to clearly scoped theorem or calculation IDs from the TeX/unit ledger;
- record the Lean version, Lake version, dependencies, and build command;
- keep informal TeX statement, source page, and Lean theorem name linked in a small CSV or JSONL ledger;
- use Lean first on modern algebraic identities, elementary number-theory lemmas, matrix/calculation checks, and small structural statements where definitions are already available in Mathlib;
- avoid claiming large historical papers are "verified in Lean" unless every relevant theorem, definition, and dependency has actually been formalized and reviewed.

