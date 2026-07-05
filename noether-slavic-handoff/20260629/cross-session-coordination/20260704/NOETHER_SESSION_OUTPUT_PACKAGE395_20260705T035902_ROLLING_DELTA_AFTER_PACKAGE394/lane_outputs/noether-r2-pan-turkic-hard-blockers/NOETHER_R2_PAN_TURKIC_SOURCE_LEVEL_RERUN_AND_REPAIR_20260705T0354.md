# R2 Pan-Turkic Source-Level Rerun And Repair

Prepared: 2026-07-05T03:54+02:00

Scope: clean metadata-only rerun for source-level TeX/LaTeX/arXiv/e-print/source-archive evidence after the 20260704T2324 markdown probe was found to contain literal placeholder paths and NUL-rendered zeros. The previous CSV/JSON rows remain structurally usable, but this artifact is the current clean source-level probe note. It records exact zero-result rows, broad false positives, GitHub rate-limit rows, moving package-frontier context, and one current-web false positive. It does not fetch or package raw source bodies and does not create translation, bridge, pilot, term, review, approval, license, gate, Zenodo, stage, commit, or push claims.

## Control State

- AGENTS.md SHA-256: EE41CF302952ADC624160B9A94CC5AE4CD3EB61B309115F61D1316D0EF039548.
- .github/copilot-instructions.md SHA-256: CBF1788357F102CE372EF35606FD931AE8A79F782C1B495C96B78351A93AE34A.
- Parent ledger SHA-256: 512C36564A65B56EFCE8A80383D36794298373174DD3C7F17ADFBCF9D01CD01E.
- Source-canon steering record SHA-256: 531B9E358E52BDE20F613E75B8DE33558C05301CA971639E727DD584B34205C4.
- R2 normalized register SHA-256: 5BFD1920A01B1079A1C1047553ABD4313276185B8EA4C7D26A809B22092A49D7.
- Git HEAD observed: 356baab417932e12b5a6883e2fc10c08cf5392ac.
- Git status observed as moving B3 frontier: ## codex/noether-pc-20260629...origin/codex/noether-pc-20260629 | ?? noether-slavic-handoff/20260629/cross-session-coordination/20260704/NOETHER_SESSION_OUTPUT_PACKAGE393_20260705T035632_ROLLING_DELTA_AFTER_PACKAGE392/.

## Findings

- R2 normalized register remains 61 rows, with 0 source-level TeX/LaTeX/arXiv/e-print/source-archive rows and 8 explicit hard-blocker gap rows.
- Local R2 outputs contain 0 TeX/LaTeX/BibTeX/archive payload files.
- Package 388 through 392 manifests were visible during the rerun and contained 0 R2 rows: 388=manifest_rows=7; r2_rows=0; 389=manifest_rows=3; r2_rows=0; 390=manifest_rows=2; r2_rows=0; 391=manifest_rows=5; r2_rows=0; 392=manifest_rows=8; r2_rows=0.
- Exact GitHub TeX queries for Kyrgyz, Tatar, Turkmen, and Uyghur language-marker plus algebra returned zero results before the later rate limit.
- Broader target-language-marker TeX queries reproduced false positives only: language-list TeX, generated documentation TeX, and font/sample TeX. These are not target-language mathematical source-level witnesses.
- Turkish/Kazakh/Uzbek expansion probes hit GitHub API rate limits and are recorded as rate-limited gap rows, not evidence.
- Current web search surfaced a Turkish GitHub profile result, not a source archive or target-language math source file.
- Outcome counts: false_positive_font_or_language_list_or_generated_doc=1; false_positive_non_math_language_list=2; false_positive_non_math_language_list_or_generated_doc=1; false_positive_profile_not_source_archive=1; no_source_level_payload_in_r2_outputs=1; observed=4; observed_no_r2_rows=5; rate_limited_no_result=4; superseded_due_placeholder_artifact_note=1; zero_results=4; zero_source_level_rows_remain=1.
- Evidence tiers: artifact_repair_context=1; control_hash=4; current_source_search_gap=4; false_positive_gap=4; local_inventory_gap=1; package_frontier_context=5; rate_limited_gap=4; register_gap_state=1; web_false_positive_gap=1.

## Machine Files

- outputs/NOETHER_R2_PAN_TURKIC_SOURCE_LEVEL_RERUN_AND_REPAIR_20260705T0354.csv
- outputs/NOETHER_R2_PAN_TURKIC_SOURCE_LEVEL_RERUN_AND_REPAIR_20260705T0354.json

## Boundary

No raw source body is uploaded or packaged here. No translation output, glossary/term promotion, Pan-Turkic bridge, pilot, native/community-review claim, canonical approval claim, accepted terminology claim, license-clearance claim, gate promotion, Zenodo action, canonical source edit, Git stage, Git commit, or Git push is made by this R2 lane.

