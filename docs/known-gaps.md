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

Current record: <https://zenodo.org/records/20614598> (concept DOI: <https://doi.org/10.5281/zenodo.20410947>)

- SGA 1, 2, and 3 have existing English/source snapshots.
- SGA 4 currently has a combined English working reader through Expose VI section 1.21, with Exposes I, II, and III complete as working drafts, Expose IV through section 14, and Expose V through section 8.
- SGA5 is now represented by a substantial cumulative French/English working surface, but it is not yet a scribe-grade complete edition. The latest `sga5_repair007_20260609.zip` closes confirmed French gaps on source pages 177, 178, and 190; earlier repair006 closed confirmed French defects on source pages 174, 197, 326, 428, 438, 457, and 470. English remains an unsynchronized carry-forward, not a synchronized repair007 branch. Remaining risk is global rather than solved: the work still needs a full diagram/exact-symbol inventory, diagram microgeometry checking, and English synchronization to the latest French repair state. The `SGA5_next_aid_manual_source_witnesses_20260609.zip`, `SGA5_repair006_next_aid_footnotes_diagrams_20260609.zip`, and `SGA5_r007_diag_aid_20260609.zip` files are witness/anchor aids, not promoted replacement text.
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
- Noether currently has the numbered German/English corpus and active Spanish/Japanese/French/Simplified-Chinese branches. The public Noether record is refreshed through `N_FRZH_P17s05_07_20260609.zip`, which carries the French and zh-Hans checkpoint stream through Paper 17 §7; Paper 17 §8 is the next continuation point. These FR/ZH files remain checkpoint streams, not complete corpora.
- Both author records need continued translation, source comparison, and final proofing.

## Classical Algebra and Arithmetic

Current record: <https://zenodo.org/records/20418609>

- This is an organized shelf of selected working drafts, not a complete author-by-author collected corpus.
- Gauss, Cayley, Dedekind, Dirichlet, Weber, and Noether material should be treated as staged working drafts unless a later author record marks a work as fully proofed.
- Cayley is specifically de-promoted as of 2026-06-09: current Cayley PDFs/TeX are retained as provenance and repair material, but a source comparison found substantial symbol/text mismatches in Volume I material. Do not treat Cayley filenames containing `Source-Checked` as current quality claims until a new per-page source audit re-promotes specific ranges.
- Gauss in particular still needs deeper repair and verification.

## Additional Author Cluster

Current record: <https://zenodo.org/records/20614569>

- This record keeps useful selected drafts for Minkowski, Hecke, Landau, Steinitz, Hensel, Oka, Hausdorff, Grassmann, Killing, and routed working packets for Bianchi, Poincare, Gordan/Clebsch-Gordan, Kneser, Picard, Kron/Kronecker, and related lanes while cleaner author pages are not yet warranted.
- Latest Bianchi staging is through source pdfpage 504 of 543; latest Poincare tranche v1_04 covers source scan pages 46-62 and stops before thesis front matter p63. Treat package-level audit notes as authority for each tranche rather than assuming the whole mixed cluster is proofed.
- The 2026-06-09 routed sweep consolidation now includes Bianchi through p0504, Poincare v1_04, Frobenius 061, Gordan Abel05, and Steinitz 41, in addition to earlier Frobenius, Gordan, Kneser, Mikami, Kronecker/Kron, Picard, and related packets. These are package-audited working/source-checked tranches according to their own internal audits, not whole-cluster final editions.

## Deligne

Current latest record: <https://zenodo.org/records/20615161> (concept DOI: <https://doi.org/10.5281/zenodo.20410853>)

- This is kept as a separate record so it can be revised independently.
- It is useful for access and translation work, but it is not proofread or legally curated to the same comfort level as the public-domain historical corpus.
- Diagram-heavy papers are a known weak point. Commutative diagrams and geometry displays may be flattened, omitted, or represented as inadequate OCR-derived displays until a source-crop audit rebuilds them.
- Deligne quality is uneven by range. The 2026-06-09 public refresh publishes `95 Pierre Deligne - Update Packets 2026-06-09.zip`, now carrying `D001_D017_witness_pass_complete_seqcum.zip` and `D074_090dn_actualtriage4.zip`. The early sequential packets around D001-D017 and the later descending/letters packets around D074-D090+letters contain useful material and source/diagram witnesses, but not every paper there should be treated as equally polished. The D001-D017 witness pass includes a promoted D017 source-page-16 level-congruence square repair; many other diagram/witness rows still require source-crop comparison before promotion. The D074-D090 triage pass carries D075/D076 repairs/checks but still treats many D077-D090 geometry candidates as triage or false-positive filtering. Some material remains rough-draft or OCR/source-witness level rather than finished translation.
