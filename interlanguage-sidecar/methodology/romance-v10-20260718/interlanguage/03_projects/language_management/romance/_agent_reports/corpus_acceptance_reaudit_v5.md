# Romance v5 Romansh-ingestion delta audit

Audit time: 2026-07-17 21:31 +02:00. Scope: current v5 artifacts only. Superseded and `PRE_*` preservation copies were excluded. Production files were not edited.

## Verdict

- **Real-source ingestion and requested count gate: PASS.** The new source is an authentic official German–Rumantsch Grischun school-mathematics exam; its hashes, corpus admission, coverage boundary, routing counts, and occurrence-review counts all verify.
- **V5 semantic/hash consistency gate: FAIL.** One T57 adverse relation points to the supported ordinary-direction sense rather than the algebraic sense for which the occurrence is adverse. The route note was corrected after the v5 gate was emitted, so the current route ledger also no longer matches the hash pinned by the v5 hash manifest/gate. These defects are to be superseded by a regenerated successor, not silently rewritten inside the audited v5 snapshot.

## 1. Curated source — PASS

`CURATED_EXTERNAL_SOURCE_MANIFEST_v1.csv` contains one RM row, `CURATED-RM-RG-GRCH-AP1G-2021-M1`:

- original PDF: 1,199,558 bytes; SHA-256 `388B920FC0B3D4D2B55F5157FB85ADE4A3F3B2032A9CB9D16FE1065F99B86ABE`;
- extracted search text: 15,991 bytes; SHA-256 `71668E44E9F00D7D0351DABB6F66FF8DFE9F149C968C1827915558AB68FBD4F2`;
- manifest SHA-256: `F5913F601981400D30F798261E52A0802273021D5E980DC1A4DB53A2312F440F`.

All paths exist and all recorded bytes/hashes match. Local Poppler inspection reports 15 A4 pages, matching both the manifest and the [official Canton of Graubünden PDF](https://www.gr.ch/DE/institutionen/verwaltung/ekud/ahb/mittelschulen/dienstleistungen/aufnahmepruefungen/pruefung1g/pruefungsbeispiele1gym/Documents/AP21_1G_M1_RG.pdf). The official URL currently serves the same 15-page title and German/Rumantsch content structure.

Direct inspection of rendered pages 1, 4, 8, and 13 confirms legible Rumantsch Grischun and German mathematics material: instructions, measurement conversion and arithmetic, parallelogram/angle/symmetry work, and a distance/time/speed word problem. The four PNG hashes match `RM_RG_SOURCE_VISUAL_QA_v1.md`. Full extracted text contains fractions, calculations, units, geometry, rates, and word problems in both languages. It does **not** establish specialist algebra terminology. The manifest correctly marks the license `unresolved_no_explicit_reuse_grant` and `term_promotion_eligible=false`.

## 2. Corpus, rejection boundary, and coverage — PASS

Independent recomputation of `ROMANCE_CONSOLIDATED_CORPUS_v2.csv` gives exactly:

- 146 representation rows;
- 140 primary-unique rows;
- 64 counting-eligible rows;
- one RM row, variety `rm-rg`, primary-unique and counting-eligible;
- zero duplicate record IDs.

The RM row points to the curated PDF/search text, both hashes match, and its tags are honestly limited to `arithmetic;fractions;geometry;measurement;solution_register;word_problems`. It is not tagged as algebra. Consolidated CSV SHA-256 is `6774E4D5F1718D38C127C3A21EC1E88E146718A00D7D9850D4C48C3700B8CAB2`, matching the JSON summary.

`ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v2.csv` reports RM exactly once, 1,199,558 bytes, one eligible source, no term promotion, the same school-mathematics tags, and `body_status=substantive_body_present`.

The four prior automatic-search false hits remain in `WIKIMEDIA_HTML_REJECTED_AUTOMATIC_SEARCH_v1.csv` (SHA-256 `FEEB65B804A5963AECDE0993C800621B25DB246EFF29F1D1881F804AF89BBCC9`). They produce no active corpus row and no occurrence. The only RM occurrences come from the curated source.

## 3. Route ledger — content/count PASS; v5 hash manifest stale

`ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv` has 61 unique routes, exactly **8 active and 53 explicit zero/gap routes**. Route R008 (`rm-rg`) correctly carries body count 1, bytes 1,199,558, the school-mathematics domains, unresolved-license status, `active_substantive_body_present`, and an accurate note that this is one general school-mathematics body with zero specialist-algebra bodies.

The corrected route CSV and its JSON summary agree at SHA-256 `7440CE0E6D4FB4CFDC33C30E704F41E301853BFC2E81E6D26550A4A6438767CF`. However, `SHA256SUMS_v5.csv` and `ROMANCE_ACCEPTANCE_GATE_v5.json` still pin the pre-correction route hash `D436E58B3580FDCBF4F6771767F9F0A1837D014D09DB175C238B738394A5F5F8` and the old byte size. The v5 package is therefore no longer self-hash-consistent after the legitimate route-note correction; the successor must regenerate the complete hash/gate set.

## 4. WordWeb v5 — count/mapping PASS; one relation target FAIL

`ROMANCE_TERM_OCCURRENCES_v1.csv` contains exactly two occurrences from the curated source:

- `OCC-8A2E8CACFACD2104`, `damai`, T45;
- `OCC-278E8BA674E87D7A`, `a dretg ora`, T57.

Both locators resolve against the 495-line Python `splitlines()` view of the extracted text; quote hashes match. `ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.csv` maps those two occurrences to exactly three sense judgments:

- T45-S1: accepted consequence connective;
- T57-S1: rejected/adverse for algebraic right-action;
- T57-S2: accepted ordinary directional sense.

The review CSV SHA-256 is `FD8CE36FFD479AB69D232EF8C6986D44CBF8E6F01CAA7521649FC3147305996A`; its JSON summary records the same hash and the correct source-occurrence hash. All three rows have `bridge_form_promotion_eligible=false` and `human_observation=false`.

`PAN_ROMANCE_WORDWEB_v5.json` independently recomputes to 60 core concepts, 106 senses, 402 relations, and 239 evidence records. It contains the two RM evidence records and three judgments, with zero core/bridge promotions. The RM forms `damai` and `dretg` remain explicitly `inherited_seed_form_not_native_canon`, so the reviewed strings were not silently promoted. WordWeb SHA-256 is `4B2B92D18F2823B1173AF6A9AD7F06FD990813452451F553F7623C300DDFFC5B`.

**Defect:** the audited `PAN_ROMANCE_WORDWEB_v5.json` has a T57 relation of type `corpus_adverse_evidence` with `target_id=T57-S2`, while its status and the authoritative judgment/sense arrays correctly say the occurrence is adverse to algebraic `T57-S1` and supportive of ordinary-direction `T57-S2`. The adverse edge must target `T57-S1` (or be split into distinct adverse/support edges). The builder source has since been corrected, but that does not repair the immutable v5 output hash audited here; the regenerated successor must prove the fix.

## Remaining acceptance blockers

For the successor to pass this narrow delta, regenerate the WordWeb with the T57 adverse edge targeting `T57-S1`, carry the corrected route ledger, regenerate all hashes/gates, and re-audit those links. For the full four-stage objective, the substantive gaps remain larger: this is one school-mathematics body, not specialist algebra; 53 routed varieties/layers remain zero-source; later human and native review is still absent.
