# Romance v7 independent bounded acceptance re-audit

Audit time: 2026-07-17 22:26 +02:00. Scope: current bytes of `03_redo_ultra_20260717`, the manager control plane it names, and fresh local rendering of T002/T003. Production artifacts were not edited. The write-producing production validators were inspected but not rerun; their results were independently recomputed read-only. The only project write is this report.

## Verdict

- **Current hash-pinned v7 acceptance snapshot: PASS.** All requested byte, topology, semantic, evidence-status, control-hash, access-ledger, visual, pilot-boundary, and completion-boundary checks pass.
- **Validator logic: PASS for the current pinned snapshot, with regression-hardening observations recorded below.** The observations do not contradict any current artifact claim because the potentially underasserted facts were independently checked directly from bytes.
- **Overall four-stage objective: correctly `ACTIVE_NOT_COMPLETE`.** Stage A remains `NOT_COMPLETE`, Stage B is only `CURRENT_CORPUS_TRANCHE_PASS`, Stage C remains `PARTIAL`, and T001–T003 are explicitly not language-validated or a full-R823 translation.

## 1. V7 gate and complete 136-row hash surface — PASS

`SHA256SUMS_v7.csv` has exactly **136 rows and 136 unique relative paths**. Independent byte verification found 136 existing targets, zero size mismatches, zero SHA-256 mismatches, and no duplicate path. `ROMANCE_ACCEPTANCE_GATE_v7.json` has exactly the same 136 path/hash entries in `key_hashes`, with no missing or additional key.

- v7 gate JSON: `8DC965DE36B05EDE77A9BFD3166C09D8D1CA7BB7635930067B4A658426300724`
- v7 SHA manifest: `5DE7FA537695265AC6B3D0CF88C9F1B803A196E4F9E85BE37E5062DD5E565A16`
- manifest hash declared by gate: `5DE7FA537695265AC6B3D0CF88C9F1B803A196E4F9E85BE37E5062DD5E565A16`
- v7 validator source: `9B5271AACFDAC94DB6E5A2F1F129176DA3E7DAC7884FD79A1E433AC95723E900`
- v7 gate log: `53F18F975F043BC6D9157C18CFFD9C9A0E0C9B618B7587012A0D2BEE4476908C`
- v7 acceptance matrix: `4521DF52FCD072D2E4A2C489F884F553921E0AA4851571B03D03876688E43FDE`

The gate and manifest intentionally do not self-hash. The gate’s actual bytes and its declared manifest hash are mutually consistent.

## 2. Manager v2 topology and manifest linkage — PASS

The canonical tree (`9EBDEF5BE13B9BDBB0F1F2B718C2EE6583CF59F723C200E78668FC9CD9AD332C`) declares schema 2.0, artifact `ROMANCE_FAMILY_COHORT_TREE_v2`, root `romance_manager`, and exactly nine unique reader cohorts. The root has exactly the same nine unique leaves. The cohort IDs are:

`C-ES-STD`, `C-FR-STD`, `C-PT-STD`, `C-GL-STD`, `C-CA-STD`, `C-IT-STD`, `C-RO-STD`, `C-RM-RG`, `C-RM-ID`.

The Rumantsch Grischun and regional-idiom reader strata are distinct. Human observations are zero, scalar readiness is disallowed, and `MII_result_feeds_decisions=false`. V2 explicitly supersedes v1; v1 remains parseable historical evidence and is not operative.

Manager-manifest linkage is real rather than declarative:

- manager SHA manifest: `32665F611D13E2243C5DFD4B6A7B0FA80B8D5AF6CA9AE86130B17782FFC0138B`;
- manager validation JSON: `CB46C4F3B6DF89C8EBEF35B3DA282FAA742F41321F6881D0A936BD7794978F07`;
- manager validator: `67E274EF182DA9F6C8C506F4EC602C6B81F85853EE17BDD0EFC8AF26D4FDE51A`.

The manager manifest has nine unique managed artifacts and correctly excludes its own self-hash. Every managed file exists and independently matches its recorded size/hash. The v7 gate directly pins the manager manifest, validation JSON, validator, README, v1 tree, and v2 tree; the v7 validator then opens the manager manifest and rechecks all nine transitive targets from bytes. The manager validation’s managed-artifact list and the manifest row order are identical.

## 3. V6 bounded/noncurrent status — PASS

V6 is preserved at gate hash `B1D67C308CDF6DE3C8AAD7F26CAB1708DC66962B6F93182614623F9E47C97467` and manifest hash `821E6E609877A2BF80E41A3F3CC857B3A05207EB69CAF5F30397B210006D954B`. The v7 gate labels it `PRESERVED_BOUNDED_SNAPSHOT_NOT_CURRENT_LANE_GATE`.

`V6_SCOPE_CORRECTION_v7.md` hashes to `D673FD3A519AFE6FF28839D8B3E63EB6A08CA17C103CAE10693C58F247FDDF21` and explicitly says v6 is neither the current lane-wide gate nor a four-stage completion certificate. It records the prior manager-plane omission and the fact that current T002 controls changed after v6. The root README, cursor, v7 log, and validator use the same boundary. There is no ambiguous “v6 current” surface in the audited controls.

## 4. T01–T30 occurrence status math — PASS

Independent parsing of the four review layers gives:

- T01–T10: 117 unique occurrences = 84 accepted-support + 33 rejected/adverse;
- T11–T20: 111 unique occurrences = 90 accepted-support + 10 rejected/adverse + 11 held;
- opportunistic RM-RG: 2 unique occurrences but 3 sense judgments = 2 accepted-support + 1 rejected/adverse;
- T21–T30: 131 unique occurrences = 64 accepted-support + 58 rejected/adverse + 9 held.

The union contains exactly **361 distinct occurrence IDs**. Status events total **362**, specifically 240 support + 102 adverse/rejected + 20 held. The one-event excess is deliberate and uniquely explained by `OCC-278E8BA674E87D7A`: it supports ordinary-direction T57-S2 while being adverse to algebraic right-action T57-S1. `status_event_counts_nonexclusive=true` and the stored reason state exactly this.

All 361 occurrence IDs occur exactly once as evidence records in WordWeb v7 after the inherited 120-record prefix; all reviewed quote hashes verify. T21–T30’s 131 rows are unique, have zero promotions/human observations, and preserve the stated gaps T22-S2, T25-S2, and T26-S1. The contiguous cursor is T01–T30, next T31.

## 5. WordWeb semantics and evidence boundary — PASS

`PAN_ROMANCE_WORDWEB_v7.json` hashes to `A48BF8C89F252A0274D2FDE2FE8A2E6E6E3077AD81A4B60BFA0B5FFF44A1A366`. Independent reconstruction gives 60 unique concepts, 106 unique senses, 39 extension nodes, 481 evidence records, and 106 decisions.

Graph reporting is exact:

- 402 relation records;
- 27 relations with a valid target ID;
- 375 relations without a target ID;
- zero nonempty invalid target IDs;
- 106 unique concept-to-sense memberships, all resolving to a matching owner;
- 133 ID-resolved references when 27 targeted relations and 106 memberships are combined.

T57 has exactly one `straight_direction_not_algebraic_right_action` edge and it correctly targets **T57-S1**.

T51 has four explicit senses and four separate decisions: function domain (S1), integral domain (S2), generic domain/region (S3), and coefficient-domain linkage (S4). T60 likewise has four senses/decisions: neutral or identity element (S1), identity map (S2), algebraic identity (S3), and unit/invertible element (S4). Every one of these eight senses has nine access rows; all eight decisions are pilot-ineligible and require later human validation.

The first 120 evidence records are exactly 60 Spanish + 60 French unresolved-locator claims across all 60 concepts. All 120 quotations are null, and there is no further ES/FR `unresolved_locator` record outside that set. Core-form promotions, extension-to-core promotions, and human observations remain zero. The arithmetic `120 + 361 = 481` is exact.

## 6. Canonical 954-row access implementation — PASS

Access JSON hashes to `881034D4E707D89C55DCB1B4E4871DD3F2F317776463AF2A19108153B2CBD8FF`; its CSV mirror hashes to `6DF5E394885F939B197F8EFF7E3E9F0B676F221207D5ED13368DE94A75D673DC`.

Both contain exactly **954 rows = 106 senses × 9 cohorts**. There are 954 unique sense/cohort pairs, every sense has nine rows, every cohort has 106 rows, the JSON and CSV identity/order triples match, and their cohort order equals manager tree v2. In JSON, all seven human-result fields are null on all 954 rows; in CSV, the corresponding cells are empty. Every JSON/CSV pilot flag is false. Header human and pilot counts are zero.

## 7. T002 current controls and fresh page-2 render — PASS

All nine hashes embedded in current T002 validation independently match their current files: authority slice, source manifest, target TeX, PDF, clause map, terminology, extracted text, pdfinfo, and validator. T002 validation JSON is `C3664C04A86886D962C6BC4C5FE1BE17666ECC463348C01DADC65CB4FDB3DB09`; validator source is `CA48ED3FF1590A49BDDEADB149C6C72E552779EE407F0C14807FA729690F731E`.

Authority lines 21089–21097 reproduce the 973-byte exact slice byte-for-byte at `5F58DDE60BB8C34421D81E7A418BF712C3F2860DBF8E4F0C16007A1A2689E235`; the next cursor is 21099. The validator derives the source-coverage, c/C distinction, conjugation formula, historical regular-matrix warning, and equivalent/isomorphic distinction from the mapped target/control files rather than merely writing fixed true flags.

The current PDF is `1D8A7A28F05A0EEF665214BC458FF0CFF134B5AB300C41F041AED31D2A115E15`. A fresh Poppler render at 150 dpi reproduced both pages byte-for-byte. Page 2 matches `81E74EB9D99D573173BF5E9034B5FDDBF57F98343A9133FF5A88386C335949CA`, is 1241×1754, and has its first nonwhite row at **y=299**. Original-detail inspection shows full heading cap height, intact glyphs/formulas/page number, and no clipping or overlap.

## 8. T003 controls, grammar, and visual evidence — PASS

All ten hashes embedded in T003 validation independently match current files, including the grammar delta. T003 validation JSON is `69447F706D785DAB9FAE47066B5A9F939AE71CD487B99528D066CB41D4FC9735`; validator source is `FFA45F277B8695E9ADF03E5A61E5261E9B61EC8EBEE6F0789F0035851910C2EA`.

Authority lines 21099–21115 reproduce the 1,431-byte exact slice byte-for-byte at `73119810BF01CFD24D461C80A829C37326D814F217C3E4CBC2B358A1184B1D33`; the next cursor is 21117. The tranche has 10 accounted clause rows, 11 target IDs, and 12 terminology rows HG46–HG57.

The grammar delta hashes to `77B7B9D67C8BC79DB4D0BFE080A1A7896697B5B16132636844C1615D67159294`. It has exactly four unique, fully populated features—`side_actions`, `implication`, `paired_actions`, and `source_ambiguous_term`—all `test_only`. The T003 validator actually reads those rows and uses them to derive the operand-order and source-ambiguity checks; it also derives direct/reciprocal action order, both zero-annihilator conditions, the source x/x-star variation warning, and the held `einfach` sense from the TeX, clauses, terminology, and grammar.

The PDF hashes to `45399FC314B5337C3028EA473AE8D590FC303C41140DDC332AE6C7D822CC70A0`. Fresh 150-dpi renders exactly reproduce page 1 (`15B7DD9471FEB10819EE47D9C8A33AAD5E838A158F13AF44BF30D0E42B1F5053`) and page 2 (`0D3BEEEC4340AE63FC633ABEE90F23426E978EB8AF2B160E955601E8D1C004AA`). First ink is at y=161/y=299, side margins are at least 157 pixels, and all titles, status/source boxes, action/annihilator formulas, editorial notes, and page numbers are fully visible. No T001–T003 console log contains an overfull/underfull box, missing-character, LaTeX warning, or package-warning match.

The render verifier (`53DE89B50D08D483C2A463C8772AE78AE33CC0EAD40C434F78B4DFEA0389CA16`) genuinely invokes Poppler in a temporary directory and compares fresh/pinned hashes. Its result JSON is `7676C6FDD5962DA2D3F8753F300DB4EBD0210F1B82F3CBE323E27D0CD74B96D7`.

## 9. Pilot/completion boundary — PASS

The gate records `goal_status=ACTIVE_NOT_COMPLETE`, `pilot_claim=false`, `full_R823_romance_translation_claim=false`, zero human observations, and zero Stage-D human validation. All 106 WordWeb decisions have `pilot_eligible=false` and `human_validation_required=true`; all 361 reviewed evidence records have `human_observation=false`; all three tranche validations report zero human rows and no pilot claim.

A structured scan found no positive pilot, human-result, language-validation, full-R823, or overall-completion assertion in the current gate, WordWeb, access ledger, tranche validations, README, cursor, v7 matrix, method, or v6 scope correction. Scoped phrases such as completed source-keyed §1/§2/§3 tranche do not claim completion of the 466-page authority.

## Validator regression-hardening observations

These are not present-byte failures, but should be tightened in a future successor:

1. `graph_metrics()` counts valid targets but does not explicitly fail on a nonempty invalid target ID, and the global validator does not assert the declared 375 no-target count. The current WordWeb independently has zero invalid targets and exactly 375 no-target relations.
2. The global T51/T60 check asserts four senses, four decisions, and empty candidate surfaces, but not the exact sense labels or one-to-one sense/decision IDs. The current objects independently have all eight required distinct sense splits and mappings.
3. The global validator checks the 954-row JSON implementation but does not semantically compare the CSV mirror. The current CSV independently matches all 954 identity triples and all zero-human/pilot cells.
4. The 361/362 nonexclusive math is asserted from summaries/WordWeb boundary rather than rebuilt from all four review CSVs, and the global script does not explicitly assert the `status_event_counts_nonexclusive` flag/reason. The independent reconstruction above verifies the exact union and sole dual-use event.
5. Fresh rendering is performed by the separately pinned `verify_pdf_renders_v7.py`, not invoked inside `validate_romance_tranche_v7.py`. Independent rendering in this audit reproduced all four page hashes exactly.

## Remaining program blockers

The bounded v7 snapshot passes, but the program must continue: 53 source routes remain empty; Rumantsch Grischun still lacks specialist-algebra material; contiguous semantic review resumes at T31; inherited quotation/source work and human cohort validation remain undone; and controlled creation has advanced only through T003, with next authority line 21117 (§4).
