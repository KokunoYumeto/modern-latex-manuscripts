# Known Gaps

This page records the main incompleteness that a reader or contributor should know about before treating the archive as finished. The records are useful now, but they are working editions and translation drafts.

## Global

- The archive is a proof-of-concept working corpus, not a final critical edition.
- Most PDFs have passed technical opening/text-surface checks, but mathematical correctness, theorem numbering, cross-references, diagrams, and table fidelity still need human or model-assisted source comparison.
- Do not treat any record as critically complete unless the maintainer explicitly certifies that status in a later release. Structural words such as "complete", "strict", or "source-checked" in filenames can mean a work/range is represented or locally compared, not that every symbol, diagram arrow, table entry, or translation choice has been proofread.
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

Current record: <https://zenodo.org/records/20673700> (concept DOI: <https://doi.org/10.5281/zenodo.20410947>)

- SGA 1, 2, and 3 have existing English/source snapshots.
- SGA 4 currently has a combined English working reader through Expose VI section 1.21, with Exposes I, II, and III complete as working drafts, Expose IV through section 14, and Expose V through section 8.
- SGA5 is now represented by a substantial cumulative French/English working surface, but it is not a scribe-grade or critical edition. The latest promoted repair package is `sga5_sga6_repair027_cumulative_20260613.zip`: repair027 is a compact cumulative French-output refresh containing SGA5/SGA6 French TeX/PDF only. It does not include the source-indexed/page-expanded SGA5 audit PDF or source-to-current-French-page map from repair025; those remain preserved in a previous Zenodo version and remain the relevant audit provenance for SGA5 source pp.160, 171, 174-177, and 180. SGA5 changes are small relative to repair026; SGA6 TeX/PDF are materially refreshed relative to repair026. English remains an unsynchronized carry-forward, not a synchronized branch. Remaining risk is global rather than solved: SGA6 still has substantial compression flags and open dense worklist rows, and SGA5/SGA6 still need full diagram/exact-symbol inventory, underlined-operator typography outside patched lanes, diagram microgeometry checking, and English synchronization. Subtle errors such as missing or reversed diagram arrows remain plausible outside patched lanes. The SGA witness-aid ZIPs are witness/anchor aids, not promoted replacement text.
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

Weber: <https://zenodo.org/records/20673435>

Noether: <https://zenodo.org/records/20673149>

- Weber currently has Volume I complete and current public Volume II German/English cumulative readers through §176. Older §143 reader PDFs remain as historical artifacts in the same record; use files prefixed `CURRENT` for the latest Volume II surface. Batch104-Batch132 cover Volume II §§169-176 plus recursive repairs, with Batch132 repairing Volume II §§120 and 128 and reporting the active 112-row ledger at 73 closed / 39 open. Larger compression clusters remain explicitly open. The next continuation point follows Volume II §176 at source p643 while the recursive repair lane remains active.
- Weber continuation material is useful and often readable, but some batches have needed recursive audit/backfill for compression, omissions, and source alignment. Treat current Volume II/III continuation ranges as working drafts unless the packet declares a source-checked range and includes page-by-page display/prose audit material.
- Noether now has a curated public surface: cumulative reader PDFs, 43 standalone English paper PDFs, compact German/source, Spanish, Japanese, French, and Simplified Chinese packages, plus the RA23 compact correction package and the RA25-RA33 Paper 02 source-critical symbol/body/table audit packages. RA28 validates the Greek-nu rebase and protects genuine Latin-v contexts; RA29 closes the Paper 02 body pp.23-90 at the current page-level standard; RA30 adds the final-summary/table-plate audit package; RA31 source-checks Tabelle I p.91; RA33 source-checks Tabelle II p.92 rows 0-7. Open items remain: Tabelle II rows 8-23 using p.92 slices 2-3, final Paper 02 tag/layout inventory, RA25-RA33 source-correction propagation across language branches, and a full symbol audit beyond Paper 01.
- Both author records need continued translation, source comparison, and final proofing. Noether should be treated as a curated working corpus, not a certified critical edition; scan-reading mistakes, subtle formula errors, and cross-language synchronization errors may remain.

## Classical Algebra and Arithmetic

Current record: <https://zenodo.org/records/20583048>

- This is an organized shelf of selected working drafts, not a complete author-by-author collected corpus.
- Gauss, Cayley, Dedekind, Dirichlet, Weber, and Noether material should be treated as staged working drafts unless a later author record marks a work as fully proofed.
- Cayley is specifically de-promoted as of 2026-06-09: current Cayley PDFs/TeX are retained as provenance and repair material, but a source comparison found substantial symbol/text mismatches in Volume I material. Do not treat Cayley filenames containing `Source-Checked` as current quality claims until a new per-page source audit re-promotes specific ranges. The current exception is the narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` restart packet for Volume I printed pp.1-45 / complete Papers 1-9; v2 fixes Paper 6 low-comma notation and removes forced source-page whitespace from the reader PDF.
- Gauss in particular still needs deeper repair and verification.

## Bianchi

Current dedicated record: <https://zenodo.org/records/20673425>

- Bianchi Vol. I is now split into its own reader-facing record, with Italian source transcription, corrected English translation working edition, source scan witness, and TeX/auditfix ZIP through source pdfpages 001-543.
- The 2026-06-13 public surface now includes `Bianchi_A2_core_p0001_0120_IT_EN_20260612.zip` as the latest compact/core A2 working package through source p0120. Earlier scan-heavy p0105 and repair packages remain provenance/backstop layers.
- The package audit treats p537-p543 as non-authorial digitization/provenance/back-cover material retained in source witnesses rather than normal reader flow.
- This is a package-audited working edition, not a final critical edition. Important formulas, references, and geometric terminology should still be checked against the source witness before scholarly citation.
- A2, `Lezioni sulla teoria dei gruppi continui finiti di trasformazioni`, now has an Italian/English working start through source p0001-p0105, about 14.36 percent of the 731-page source. It retains earlier packets plus the p0091-p0105 continuation; p0106 is the next handoff. A2 is not complete, and TeX build success is not glyph-level certification.

## Gordan / Clebsch-Gordan

Current dedicated record: <https://zenodo.org/records/20673409>

- The dedicated Gordan/Clebsch-Gordan record is now the preferred surface for this lane. The current top continuation package is `Gordan_Abel26_p332_342_DE_EN_20260612.zip`, extending `Theorie der Abelschen Functionen` through source pp.332-342 / printed pp.310-320 and cumulative German/English TeX/PDF through source p342. It completes §87 and §§88-90 and repairs a prior cumulative-inclusion bug. Earlier Abel tranches remain support/provenance layers. `Gordan_AllPrior_AuditFix01_20260610.zip` remains the consolidated checkpoint for De linea, theta, Formensystem, and earlier Abelsche support branches.
- These are package-audited, source-witnessed working drafts. OCR scaffolds are non-authoritative locator/check layers, and important formulas or table/section boundaries should still be checked against bundled source scans before citation-critical use.
- Some nested cumulative provenance notes inside older Abel packages carry stale older coverage wording; use the main READMEs, build checks, current/cumulative outputs, and ledgers for the current pp.001-217 coverage statement.

## Steinitz

Current dedicated record: <https://zenodo.org/records/20617915>

- The dedicated Steinitz record is now the preferred surface for current Steinitz work. It includes package-audited German/English working packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13.
- These are source-witnessed working drafts, not final critical editions. Use each package's internal README, progress ledger, source scans, and render/audit files as authority for its exact promoted scope.
- Known gaps remain explicit in the public metadata: 1908 Analysis Situs source unresolved; the remainder of 1916 Bedingt III, 1916/1922 polyhedron-space-division work, and 1927/1928 isoperimetric papers not completed.

## Additional Author Cluster

Current record: <https://zenodo.org/records/20672984>

- This record keeps useful selected drafts for Minkowski, Hecke, Landau, Steinitz, Hensel, Oka, Hausdorff, Grassmann, Killing, and routed working packets for Poincare, Frobenius, Kneser, Picard, Kron/Kronecker, and related lanes while cleaner author pages are not yet warranted. Bianchi, Gordan, and Steinitz now have standalone records; their files here are retained as backstop/provenance copies.
- Poincare now has a preferred dedicated record: <https://zenodo.org/records/20673462>. Latest local package is `poincare_v1_26.zip`, a Tome I FR/EN working package for source witnesses v1_0371-v1_0384 top. The record is explicitly non-continuous because local `poincare_v1_*` artifacts currently omit v1_03-v1_07 and v1_22-v1_23. Treat package-level audit notes as authority for each tranche rather than assuming the whole stream is proofed.
- Frobenius now has a preferred dedicated record: <https://zenodo.org/records/20673445>. The QA03 selected group-character package reports 10/10 selected items and 221/221 tracked source-intake pages, but remains a working/source-witnessed package rather than a certified critical edition.
- The 2026-06-12 routed sweep consolidation now includes `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip`, a selected Frobenius sequence cumulative/QA package, and `Kneser_LVR_p0206_0219_DE_EN_20260612.zip`, a Kneser LVR continuation for source p0206 lower-p0219 upper / sections 46-48 with Fig. 24 as a source-derived crop. Lower p0219 / section 49 is the next handoff; earlier p0158-p0177 and p0177-p0192 packages remain previous tranches/provenance. Older Zenodo versions retain superseded provenance. Prefer the dedicated Bianchi, Gordan, and Steinitz records for their current public surfaces.

## Deligne

Current latest record: <https://zenodo.org/records/20617786> (concept DOI: <https://doi.org/10.5281/zenodo.20410853>)

- This is kept as a separate record so it can be revised independently.
- It is useful for access and translation work, but it is not proofread or legally curated to the same comfort level as the public-domain historical corpus.
- Diagram-heavy papers are a known weak point. Commutative diagrams and geometry displays may be flattened, omitted, or represented as inadequate OCR-derived displays until a source-crop audit rebuilds them.
- Deligne quality is uneven by range. The 2026-06-09 v3 public refresh publishes `95 Pierre Deligne - Update Packets 2026-06-09 v3.zip`, carrying `D001_D017_witness_pass_complete_seqcum.zip`, `D001_D017_equation_dense_math_audit_seqcum.zip`, `D074_090dn_actualtriage4.zip`, and `D074_090dn_mathaudit_repairpass1.zip`. The early sequential packets around D001-D017 and the later descending/letters packets around D074-D090+letters contain useful material and source/diagram witnesses, but not every paper there should be treated as equally polished. The D001-D017 witness pass includes a promoted D017 source-page-16 level-congruence square repair, and the equation-dense supplement adds formula/diagram/source-certification ledgers; many other diagram/witness rows still require source-crop comparison before promotion. The D074-D090 repair pass records D074 completion and targeted D076 product-morphism/diagram repairs, but the D077-D090 geometry aids are still locator/check layers and may contain false positives. Some material remains rough-draft or OCR/source-witness level rather than finished translation.
