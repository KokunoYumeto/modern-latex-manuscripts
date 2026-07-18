# Romance v6 bounded acceptance re-audit

Audit time: 2026-07-17 22:00 +02:00. Scope: the current `03_redo_ultra_20260717` v6 snapshot and the canonical cohort topology it names. This was a read-only production audit: no production file was edited and the write-producing validator was not rerun. Its claims were independently recomputed from the pinned artifacts. The only project write is this report.

## Verdict

- **Bounded v6 acceptance gate: PASS.** All requested v6 checks below pass with no hash, graph-target, cohort-topology, T001 binding, T002 visual, evidence-boundary, pilot-claim, or completion-claim defect found.
- **Overall four-stage objective: correctly NOT COMPLETE.** The machine gate says `ACTIVE_NOT_COMPLETE`; Stage A is `NOT_COMPLETE`, Stage B is `CURRENT_CORPUS_TRANCHE_PASS`, Stage C is `PARTIAL`, and Stage D is `T001_T002_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED`. This audit does not convert a sound bounded tranche into a corpus-completion, human-intelligibility, language-validation, or full-R823 claim.

## 1. Complete v6 hash surface — PASS

Independent verification of `qa/SHA256SUMS_v6.csv` found exactly **86 rows, 86 unique relative paths, 86 existing files, and zero byte-size or SHA-256 mismatches**. `ROMANCE_ACCEPTANCE_GATE_v6.json` contains exactly the same 86 path/hash pairs in `key_hashes`; there are no missing, additional, or divergent gate keys.

- SHA manifest: `821E6E609877A2BF80E41A3F3CC857B3A05207EB69CAF5F30397B210006D954B` (matches `hash_manifest_sha256` in the gate)
- acceptance gate JSON: `B1D67C308CDF6DE3C8AAD7F26CAB1708DC66962B6F93182614623F9E47C97467`
- acceptance gate log: `06E08A949C933D785D9556710EC577B09D75FE27B71FF11E251C8BBA67F58406`
- acceptance matrix: `1FFCD6CC9F0B5E1403C2122C7A7C85E2E860E238193E59787B68F919FE117FB5`
- v6 validator source: `12898B7F172CBA4D74BC3C2A3704EE008781DA8D911C388529BD0E94D6D23255`

The current branch-routing ledger is hash-current at `7440CE0E6D4FB4CFDC33C30E704F41E301853BFC2E81E6D26550A4A6438767CF`, exactly as pinned by v6. It has 61 routes, 8 active and 53 zero-source routes. R008 accurately says that Rumantsch Grischun has one general school-mathematics body and still lacks specialist algebra; the corrected note is no longer the stale v5 hash state.

## 2. WordWeb graph semantics and T57 — PASS

`PAN_ROMANCE_WORDWEB_v6.json` SHA-256 is `0D4B581A2CE3F6664B1A97A44AAD023ED1FDC6C023FED5ADE42677E445751AD4`. Independent reconstruction gives:

- 60 unique core term IDs, 106 unique sense IDs, 39 C2 extension IDs, 350 evidence records, and 106 decisions;
- 402 relation records total;
- 27 relations with a valid target ID;
- 375 descriptive relations without a target ID;
- zero nonempty invalid target IDs;
- 106 unique concept-to-sense memberships, all resolving to a sense whose `term_id` matches the owning concept;
- 133 total ID-resolved references when 27 targeted relations and 106 memberships are added.

Thus, **402 is a relation-record count, not a graph-edge count**. The v6 `relation_metrics` declaration is exact.

The repaired T57 `corpus_adverse_evidence` relation points to **`T57-S1`**, with evidence `E-OCC-278E8BA674E87D7A` and label `straight_direction_not_algebraic_right_action`. It no longer targets T57-S2. T57 has separate decisions for S1 and S2, both pilot-ineligible and human-validation-required, and the access ledger contains nine cohort rows for each sense.

## 3. Canonical cohort topology and access ledger — PASS

The canonical tree SHA-256 is `9EBDEF5BE13B9BDBB0F1F2B718C2EE6583CF59F723C200E78668FC9CD9AD332C`; the access-ledger JSON SHA-256 is `E16E57953B3F8825554AB89E0B6A59E757C4BF40F2CE8B025AC384110E4D93E4`.

The cohort order is identical in the tree, ledger declaration, gate, and ledger rows:

`C-ES-STD`, `C-FR-STD`, `C-PT-STD`, `C-GL-STD`, `C-CA-STD`, `C-IT-STD`, `C-RO-STD`, `C-RM-RG`, `C-RM-ID`.

The ledger contains exactly **954 unique sense/cohort pairs = 106 senses × 9 cohorts**. Every sense has nine rows; every cohort has 106 rows; there are no duplicate, missing, or foreign pairs. Across all 954 rows, `human_n`, correct/incorrect/abstention counts, latency, confidence, and effect interval are null; all 954 `pilot_eligible` values are false. Header counts are zero, and the gate explicitly records `MII_result_feeds_decisions=false`. The topology therefore implements design diagnostics only and does not fabricate a pilot or human result.

## 4. T001 source/control binding and validator dependency — PASS

The declared German authority exists and hashes to `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`. Independent byte extraction from that file reproduces both separately bound inputs exactly:

- body lines 21047–21087: `33E4D17FEC404CB5B5A7DF208EE1BC5855BB6B0F4091A04905B95B75C1D9AF64`;
- metadata lines 20985–20990: `D424D5D19D8B8E153B1DF736933F71B83098A5C54135646561B9E3E2C8519559`.

The five requested control inputs are all direct v6 hash targets and match the gate:

1. body slice: `33E4D17FEC404CB5B5A7DF208EE1BC5855BB6B0F4091A04905B95B75C1D9AF64`;
2. metadata slice: `D424D5D19D8B8E153B1DF736933F71B83098A5C54135646561B9E3E2C8519559`;
3. clause map: `1447F6B72DB1D5516405A9D37EFB6B4C1B447079F1C0730A71B1BB9147D4A01A`;
4. terminology ledger: `5B2DA488BBEE420B966F0E1EF4B1DF14127518D7B724E71B021DFCEB5D51DDB0`;
5. controlled grammar test: `01387F3DB1E3D7A6875BD094DBD8BED07BF0E3CE8163BE03C162998DA3461B7F`.

This is executable dependency, not metadata-only decoration. `validate_t001.py` opens the clause, terminology, and grammar CSVs; checks all 18 grammar rows for six nonempty audit fields; requires all 18 named grammar features; restricts status to `test_only`/`held`; hashes body and metadata separately; and binds their line ranges through the source manifest. The v6 global validator independently reads the grammar CSV, checks its row/status set, compares the hashes of clause/terminology/grammar and the source manifest, pins the T001 validator itself, and includes all five controls in the 86-target manifest. Validator SHA-256 is `80A5DAFB4E1641EC47BC1F01EE3C9833C0F57437D3A3F92B92C934BE1D7C5273`; validation JSON SHA-256 is `C63C850848DCD9FAF323F82486D1746FBBC4694F8C5AE2BCB25D9A22C49662D8`.

## 5. T002 page-2 top margin — PASS

The T002 TeX (`C4FBA6F03AFAFDCD9A71463FC96321871AF07CF5B2B3C06969485A2BECCAA84E`) contains the explicit `\vspace*{10mm}` successor fix. The PDF SHA-256 is `1D8A7A28F05A0EEF665214BC458FF0CFF134B5AB300C41F041AED31D2A115E15`.

I independently rendered page 2 from that PDF with Poppler at 150 dpi into an audit-temporary directory. The fresh 1241×1754 PNG is byte-identical to the pinned QA render at SHA-256 `81E74EB9D99D573173BF5E9034B5FDDBF57F98343A9133FF5A88386C335949CA`. Original-detail visual inspection shows the full heading cap height and ample white margin; the first significant ink row is y=299, about 50.6 mm below the physical top. There is no clipping, overlap, margin escape, or missing glyph.

The checked visual-QA note hashes to `191E41FB0C4AF8D1FA7BA0B6B6EB21E1627F694FFC6A756994FE9AA7134780C8`; T002 validation JSON hashes to `AA1698BEEA933A8E00B1A53468D0580C5AD78C8D529B56817064D1936A296D80` and records zero human rows and `pilot_claim=false`.

## 6. Inherited evidence and claim boundary — PASS

The inherited core is exactly **120 ES/FR records**: 60 Spanish and 60 French, covering all 60 core terms. All 120 have `acceptance=unresolved_locator`, all are quotation-free, and no additional ES/FR unresolved-locator record exists outside that set. Core-form promotions, extension-context-to-core promotions, and human observations are all zero.

A structured scan found no positive pilot, human-result, language-validation, full-R823, or overall-completion flag. All 954 access rows and all 106 WordWeb decisions are pilot-ineligible; the decisions correctly say human validation is still required. The root README and cursor explicitly deny a 466-page/full-R823 translation claim and keep the goal `ACTIVE_NOT_COMPLETE`. Local phrases such as “completed source-keyed test tranche” are bounded to the named §1/§2 slices and are not global completion claims.

## Remaining non-v6 blockers

The v6 snapshot passes this bounded gate, but the program must continue: Stage A still has 53 zero-source routes and no specialist-algebra Romansh body; Stage C’s contiguous occurrence review resumes at T21 and still lacks inherited quotations and human data; Stage D has only T001–T002 and no native/language validation. The next authority cursor is line 21099 (§3).
