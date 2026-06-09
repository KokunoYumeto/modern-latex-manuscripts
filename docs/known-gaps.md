# Known Gaps

This page records the main incompleteness that a reader or contributor should know about before treating the archive as finished. The records are useful now, but they are working editions and translation drafts.

## Global

- The archive is a proof-of-concept working corpus, not a final critical edition.
- Most PDFs have passed technical opening/text-surface checks, but mathematical correctness, theorem numbering, cross-references, diagrams, and table fidelity still need human or model-assisted source comparison.
- Top-level PDFs are the public reading surface. Artifact ZIPs hold TeX, source witnesses, OCR, provenance, and repair material.
- Known recurring failure modes include source compression or omission in generated drafts, flattened or missing commutative diagrams, OCR-derived formula witnesses being mistaken for accepted TeX, and uneven language layers. These are repairable problems, but they should be visible to readers.

## EGA

Current record: <https://zenodo.org/records/20414353>

- EGA I and EGA II are largely inherited from the public community translation base.
- EGA 0_IV sections 15 through 23 are present as substantive working translations in the current 578-page build.
- EGA IV sections 1 through 3 are present as substantive working translations; EGA IV section 4 is included as the current partial/in-progress working file.
- EGA 0_III sections 12 and 13 remain placeholder files rather than substantive translations.
- EGA III and much of EGA IV remain far from complete as English translations beyond the currently represented material.
- The current build is useful for continuation and checking, not a proofread final edition.

## SGA

Current record: <https://zenodo.org/records/20616461> (concept DOI: <https://doi.org/10.5281/zenodo.20410947>)

- SGA 1, 2, and 3 have existing English/source snapshots.
- SGA 4 currently has a combined English working reader through Expose VI section 1.21, with Exposes I, II, and III complete as working drafts, Expose IV through section 14, and Expose V through section 8.
- SGA5 is now represented by a substantial cumulative French/English working surface, but it is not yet a scribe-grade complete edition. The latest `sga5_repair008_20260609.zip` closes targeted French diagram/formula issues on source pages 083, 095, 098, 100, 116, and 184; repair007 closed confirmed French gaps on source pages 177, 178, and 190; earlier repair006 closed confirmed French defects on source pages 174, 197, 326, 428, 438, 457, and 470. English remains an unsynchronized repair002 carry-forward, not a synchronized branch. Remaining risk is global rather than solved: the work still needs a full diagram/exact-symbol inventory, underlined-operator typography scan, diagram microgeometry checking, and English synchronization to the latest French repair state. The `SGA5_next_aid_manual_source_witnesses_20260609.zip`, `SGA5_repair006_next_aid_footnotes_diagrams_20260609.zip`, and `SGA5_r007_diag_aid_20260609.zip` files are witness/anchor aids, not promoted replacement text.
- SGA6 is structurally covered across source pages 001-702, but the 2026-06-08 nuclear audit found localized substantive compression/omission candidates. Confirmed/strong pages include 014, 431, 625, and 679; repair should start with p014 and clusters 423-454, 619-653, and 670-692.
- SGA7 material should be treated as especially provisional unless a specific packet says otherwise. The likely weak point is not just typography but source compression: sections can look readable while silently omitting local mathematical detail.
- SGA 4 Expose VI should continue from section 1.22.
- SGA 5, SGA 6, SGA 7-I, and SGA 7-II French reference PDFs are intentional image-based scans; they open and page-count correctly, but embedded text extraction is not expected to be reliable.

## Non-European Mathematical Classics

Current consolidated record: <https://zenodo.org/records/20410957>

- The current release is much more readable than the early path-dump stage: it has combined readers, work-level PDFs, source bundles, OCR notes, and page-image artifacts.
- It still needs source-faithfulness review, terminology checks, and mathematical proofreading work by work.
- Some language layers are uneven: several works have English translation, modern Chinese rendering, and original-language drafts; others have only part of that stack.

## Weber and Noether

Weber: <https://zenodo.org/records/20412153>

Noether: <https://zenodo.org/records/20412587>

- Weber currently has Volume I complete and current public Volume II German/English cumulative readers through §165. Older §143 reader PDFs remain as historical artifacts in the same record; use files prefixed `CURRENT` for the latest Volume II surface. The next continuation point is Volume II §166, source p.607.
- Weber continuation material is useful and often readable, but some batches have needed recursive audit/backfill for compression, omissions, and source alignment. Treat current Volume II/III continuation ranges as working drafts unless the packet declares a source-checked range and includes page-by-page display/prose audit material.
- Noether currently has the numbered German/English corpus and active Spanish/Japanese/French/Simplified-Chinese branches. The public Noether record is refreshed through `N_FRZH_Papers16_17_combined_20260609.zip`, which combines the original Paper 16 complete package, the original P17a package, and the original French/zh-Hans Paper 17 §§5-7 continuation package to stay within the Zenodo 100-file limit. Paper 17 §8 is the next FR/ZH continuation point. These FR/ZH files remain checkpoint streams, not complete corpora.
- Both author records need continued translation, source comparison, and final proofing.

## Classical Algebra and Arithmetic

Current record: <https://zenodo.org/records/20418609>

- This is an organized shelf of selected working drafts, not a complete author-by-author collected corpus.
- Gauss, Cayley, Dedekind, Dirichlet, Weber, and Noether material should be treated as staged working drafts unless a later author record marks a work as fully proofed.
- Cayley is specifically de-promoted as of 2026-06-09: current Cayley PDFs/TeX are retained as provenance and repair material, but a source comparison found substantial symbol/text mismatches in Volume I material. Do not treat Cayley filenames containing `Source-Checked` as current quality claims until a new per-page source audit re-promotes specific ranges. The current exception is the narrow `Cayley_V1_critical_p001_024_20260609.zip` restart packet for Volume I printed pp.1-24 / complete Papers 1-4.
- Gauss in particular still needs deeper repair and verification.

## Bianchi

Current dedicated record: <https://zenodo.org/records/20615949>

- Bianchi Vol. I is now split into its own reader-facing record, with Italian source transcription, corrected English translation working edition, source scan witness, and TeX/auditfix ZIP through source pdfpages 001-543.
- The 2026-06-09 auditfix repairs a small set of English cumulative defects: one control-character formula issue, nine source-notation `\sen` repairs, the section 186 displayed formula, and a section 189 anti-compression repair.
- The package audit treats p537-p543 as non-authorial digitization/provenance/back-cover material retained in source witnesses rather than normal reader flow.
- This is a package-audited working edition, not a final critical edition. Important formulas, references, and geometric terminology should still be checked against the source witness before scholarly citation.

## Gordan / Clebsch-Gordan

Current dedicated record: <https://zenodo.org/records/20616261>

- The dedicated Gordan/Clebsch-Gordan record is now the preferred surface for this lane. It includes Abelian-functions packages through source pp.001-121 / printed pp.001-099, plus the latest complete working packets for `De linea geodetica` and the staged `Formensystem` branch.
- These are package-audited, source-witnessed working drafts. OCR scaffolds are non-authoritative locator/check layers, and important formulas or table/section boundaries should still be checked against bundled source scans before citation-critical use.
- Some nested cumulative provenance notes inside Abel06/Abel07 carry stale older coverage wording; use the main READMEs, build checks, current/cumulative outputs, and ledgers for the current pp.001-121 coverage statement.

## Additional Author Cluster

Current record: <https://zenodo.org/records/20616046>

- This record keeps useful selected drafts for Minkowski, Hecke, Landau, Steinitz, Hensel, Oka, Hausdorff, Grassmann, Killing, and routed working packets for Poincare, Frobenius, Kneser, Picard, Kron/Kronecker, and related lanes while cleaner author pages are not yet warranted. Bianchi and Gordan now have standalone records; their files here are retained as backstop/provenance copies.
- Latest Poincare tranche v1_05 covers source PDF pages 63-85, beginning the thesis notice and `Premiere These`, and stops before source PDF page 86 / `PREMIERE PARTIE`. Treat package-level audit notes as authority for each tranche rather than assuming the whole mixed cluster is proofed.
- The 2026-06-09 routed sweep consolidation includes Poincare v1_05, Bianchi/Gordan backstop copies, Frobenius 061, and Steinitz 41, in addition to earlier Frobenius, Gordan, Kneser, Mikami, Kronecker/Kron, Picard, and related packets. These are package-audited working/source-checked tranches according to their own internal audits, not whole-cluster final editions. Prefer the dedicated Bianchi and Gordan records for their current public surfaces.

## Deligne

Current latest record: <https://zenodo.org/records/20615537> (concept DOI: <https://doi.org/10.5281/zenodo.20410853>)

- This is kept as a separate record so it can be revised independently.
- It is useful for access and translation work, but it is not proofread or legally curated to the same comfort level as the public-domain historical corpus.
- Diagram-heavy papers are a known weak point. Commutative diagrams and geometry displays may be flattened, omitted, or represented as inadequate OCR-derived displays until a source-crop audit rebuilds them.
- Deligne quality is uneven by range. The 2026-06-09 v2 public refresh publishes `95 Pierre Deligne - Update Packets 2026-06-09 v2.zip`, carrying `D001_D017_witness_pass_complete_seqcum.zip`, `D001_D017_equation_dense_math_audit_seqcum.zip`, and `D074_090dn_actualtriage4.zip`. The early sequential packets around D001-D017 and the later descending/letters packets around D074-D090+letters contain useful material and source/diagram witnesses, but not every paper there should be treated as equally polished. The D001-D017 witness pass includes a promoted D017 source-page-16 level-congruence square repair, and the equation-dense supplement adds formula/diagram/source-certification ledgers; many other diagram/witness rows still require source-crop comparison before promotion. The D074-D090 triage pass carries D075/D076 repairs/checks but still treats many D077-D090 geometry candidates as triage or false-positive filtering. Some material remains rough-draft or OCR/source-witness level rather than finished translation.
