# Known Gaps

This page records the main incompleteness that a reader or contributor should know about before treating the archive as finished. The records are useful now, but they are working editions and translation drafts.

## Global

- The archive is a proof-of-concept working corpus, not a final critical edition.
- Most PDFs have passed technical opening/text-surface checks, but mathematical correctness, theorem numbering, cross-references, diagrams, and table fidelity still need human or model-assisted source comparison.
- Top-level PDFs are the public reading surface. Artifact ZIPs hold TeX, source witnesses, OCR, provenance, and repair material.
- Known recurring failure modes include source compression or omission in generated drafts, flattened or missing commutative diagrams, OCR-derived formula witnesses being mistaken for accepted TeX, and uneven language layers. These are repairable problems, but they should be visible to readers.

## EGA

Current record: <https://zenodo.org/records/20454552>

- EGA I and EGA II are largely inherited from the public community translation base.
- EGA 0_IV sections 15 through 23 are present as substantive working translations in the current 578-page build.
- EGA IV sections 1 through 3 are present as substantive working translations; EGA IV section 4 is included as the current partial/in-progress working file.
- EGA 0_III sections 12 and 13 remain placeholder files rather than substantive translations.
- EGA III and much of EGA IV remain far from complete as English translations beyond the currently represented material.
- The current build is useful for continuation and checking, not a proofread final edition.

## SGA

Current record: <https://zenodo.org/records/20651984> (concept DOI: <https://doi.org/10.5281/zenodo.20410947>)

- SGA 1, 2, and 3 have existing English/source snapshots.
- SGA 4 currently has a combined English working reader through Expose VI section 1.21, with Exposes I, II, and III complete as working drafts, Expose IV through section 14, and Expose V through section 8.
- SGA5 is now represented by a substantial cumulative French/English working surface, but it is not yet a scribe-grade complete edition. The latest promoted repair package is `sga5_sga6_repair016_20260611.zip`: SGA5 carries the prior French repair state forward with an internal source-erratum comment for a blank citation, while SGA6 repair003 restores Expose VI source pp.372-387 in French from source scans. English remains an unsynchronized carry-forward, not a synchronized branch. Remaining risk is global rather than solved: SGA6 still has substantial late-region compression flags, dense-cluster lanes pp.388-460 and pp.571-680 remain open, and SGA5/SGA6 still need full diagram/exact-symbol inventory, underlined-operator typography outside patched lanes, diagram microgeometry checking, and English synchronization. The SGA witness-aid ZIPs are witness/anchor aids, not promoted replacement text.
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

Weber: <https://zenodo.org/records/20651306>

Noether: <https://zenodo.org/records/20651590>

- Weber currently has Volume I complete and current public Volume II German/English cumulative readers through §176. Older §143 reader PDFs remain as historical artifacts in the same record; use files prefixed `CURRENT` for the latest Volume II surface. Batch104-Batch120 cover Volume II §§169-176 plus recursive repairs including Vol. I §§124, 151, 183 and Vol. II §§20, 21, 52, 57, 58, 60, 61, 77, 99, 101, 106, 114, 118, 126. Batch121 corrects the Batch120 inspection package by splitting the non-contiguous §§106/114 repair artifacts and adding contiguous §§106-114 extracts confirming §§107-113 are present in order. The active repair ledger still reports 93 open priority repair rows. The next continuation point follows Volume II §176 at source p643 while the recursive repair lane remains active.
- Weber continuation material is useful and often readable, but some batches have needed recursive audit/backfill for compression, omissions, and source alignment. Treat current Volume II/III continuation ranges as working drafts unless the packet declares a source-checked range and includes page-by-page display/prose audit material.
- Noether now has a curated public surface: cumulative reader PDFs, 43 standalone English paper PDFs, and compact German/source, Spanish, Japanese, French, and Simplified Chinese packages. Known open items remain: RA20 fixes German/source Paper 02 p.63 display layout but non-German propagation is queued; RA10 restores scan-visible apparatus for Papers 40-43 but leaves inline body resynchronization open; the FR/ZH checkpoint is through Paper 19 §6 and its tau-exponent correction still needs EN/ES/JA propagation.
- Both author records need continued translation, source comparison, and final proofing.

## Classical Algebra and Arithmetic

Current record: <https://zenodo.org/records/20583048>

- This is an organized shelf of selected working drafts, not a complete author-by-author collected corpus.
- Gauss, Cayley, Dedekind, Dirichlet, Weber, and Noether material should be treated as staged working drafts unless a later author record marks a work as fully proofed.
- Cayley is specifically de-promoted as of 2026-06-09: current Cayley PDFs/TeX are retained as provenance and repair material, but a source comparison found substantial symbol/text mismatches in Volume I material. Do not treat Cayley filenames containing `Source-Checked` as current quality claims until a new per-page source audit re-promotes specific ranges. The current exception is the narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` restart packet for Volume I printed pp.1-45 / complete Papers 1-9; v2 fixes Paper 6 low-comma notation and removes forced source-page whitespace from the reader PDF.
- Gauss in particular still needs deeper repair and verification.

## Bianchi

Current dedicated record: <https://zenodo.org/records/20651036>

- Bianchi Vol. I is now split into its own reader-facing record, with Italian source transcription, corrected English translation working edition, source scan witness, and TeX/auditfix ZIP through source pdfpages 001-543.
- The 2026-06-11 public surface now includes `Bianchi_A2_cont_p0001_0066_IT_EN_20260611.zip` as the preferred A2 continuation layer through p0001-p0066. It restores the deferred section 10 opening on p0057 and completes sections 10-12. The p0001-p0057 audit-continuation and p0001-p0066 HQ package remain provenance/support layers.
- The package audit treats p537-p543 as non-authorial digitization/provenance/back-cover material retained in source witnesses rather than normal reader flow.
- This is a package-audited working edition, not a final critical edition. Important formulas, references, and geometric terminology should still be checked against the source witness before scholarly citation.
- A2, `Lezioni sulla teoria dei gruppi continui finiti di trasformazioni`, now has a promoted high-quality Italian/English working start through source p0001-p0066, about 9 percent of the 731-page source. It covers sections 1-12; section 13 starts at the lower part of p0066 and continues on p0067, so that handoff is deliberate. A2 is not complete.

## Gordan / Clebsch-Gordan

Current dedicated record: <https://zenodo.org/records/20650618>

- The dedicated Gordan/Clebsch-Gordan record is now the preferred surface for this lane. The current top continuation package is `Gordan_Abel16_p218_227_DE_EN_20260611.zip`, extending Abelsche Functionen through source p227 / printed p205. Abel13 p182-p193 includes the p190 continuation of equation (4), while Abel14 and Abel15 continue p194-p217. `Gordan_AllPrior_AuditFix01_20260610.zip` remains the consolidated checkpoint for De linea, theta, Formensystem, and Abelsche through p121, including the theta FIX05 correction for the `c^8=1` display and wide-display reflow.
- These are package-audited, source-witnessed working drafts. OCR scaffolds are non-authoritative locator/check layers, and important formulas or table/section boundaries should still be checked against bundled source scans before citation-critical use.
- Some nested cumulative provenance notes inside older Abel packages carry stale older coverage wording; use the main READMEs, build checks, current/cumulative outputs, and ledgers for the current pp.001-217 coverage statement.

## Steinitz

Current dedicated record: <https://zenodo.org/records/20617915>

- The dedicated Steinitz record is now the preferred surface for current Steinitz work. It includes package-audited German/English working packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13.
- These are source-witnessed working drafts, not final critical editions. Use each package's internal README, progress ledger, source scans, and render/audit files as authority for its exact promoted scope.
- Known gaps remain explicit in the public metadata: 1908 Analysis Situs source unresolved; the remainder of 1916 Bedingt III, 1916/1922 polyhedron-space-division work, and 1927/1928 isoperimetric papers not completed.

## Additional Author Cluster

Current record: <https://zenodo.org/records/20651148>

- This record keeps useful selected drafts for Minkowski, Hecke, Landau, Steinitz, Hensel, Oka, Hausdorff, Grassmann, Killing, and routed working packets for Poincare, Frobenius, Kneser, Picard, Kron/Kronecker, and related lanes while cleaner author pages are not yet warranted. Bianchi, Gordan, and Steinitz now have standalone records; their files here are retained as backstop/provenance copies.
- Latest Poincare tranche is `poincare_v1_20.zip`, a Tome I FR/EN working package through Chapters XII-XIII, with source witnesses v1_0263-v1_0273 and next continuation at v1_0274 / Chapter XIV. Treat package-level audit notes as authority for each tranche rather than assuming the whole mixed cluster is proofed.
- The 2026-06-11 routed sweep consolidation now includes `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip`, a selected Frobenius sequence cumulative/QA package, and `Kneser_LVR_hqfig_p0158_0177_DE_EN_20260611.zip`, a high-quality figure and scan-witness repair for the Kneser LVR pp.158-177 / §§37-39 tranche. The Kneser package keeps the text/math scope unchanged, removes visible AI/TikZ figure reconstructions, and is preferred over the earlier p0158-p0177 package for checking figures and scan witnesses. Older Zenodo versions retain superseded provenance. Prefer the dedicated Bianchi, Gordan, and Steinitz records for their current public surfaces.

## Deligne

Current latest record: <https://zenodo.org/records/20617786> (concept DOI: <https://doi.org/10.5281/zenodo.20410853>)

- This is kept as a separate record so it can be revised independently.
- It is useful for access and translation work, but it is not proofread or legally curated to the same comfort level as the public-domain historical corpus.
- Diagram-heavy papers are a known weak point. Commutative diagrams and geometry displays may be flattened, omitted, or represented as inadequate OCR-derived displays until a source-crop audit rebuilds them.
- Deligne quality is uneven by range. The 2026-06-09 v3 public refresh publishes `95 Pierre Deligne - Update Packets 2026-06-09 v3.zip`, carrying `D001_D017_witness_pass_complete_seqcum.zip`, `D001_D017_equation_dense_math_audit_seqcum.zip`, `D074_090dn_actualtriage4.zip`, and `D074_090dn_mathaudit_repairpass1.zip`. The early sequential packets around D001-D017 and the later descending/letters packets around D074-D090+letters contain useful material and source/diagram witnesses, but not every paper there should be treated as equally polished. The D001-D017 witness pass includes a promoted D017 source-page-16 level-congruence square repair, and the equation-dense supplement adds formula/diagram/source-certification ledgers; many other diagram/witness rows still require source-crop comparison before promotion. The D074-D090 repair pass records D074 completion and targeted D076 product-morphism/diagram repairs, but the D077-D090 geometry aids are still locator/check layers and may contain false positives. Some material remains rough-draft or OCR/source-witness level rather than finished translation.
