# Japanese Noether Paper 23 visual-evidence scope and caveats

## Indexed payload

- Tranche root: `evidence://local-workspace/interlanguage\03_projects\language_management\cjk\03_working_translations\japanese\noether_paper23_ja_reconciliation_20260718`
- Image root: `render_check/`
- Accepted visual records: four target-render PNGs, one per page of the accepted four-page Japanese PDF.
- Exact visual bytes: 3,371,449.
- Canonical image-set manifest digest: SHA-256 `6118ED10FBA7E73C280E502F8862ACC2E0F8303E23727CEAA292CB8469E400D5`, computed over UTF-8 without BOM, LF-separated `filename,sha256,bytes` lines sorted by filename, with no terminal newline.
- Machine-readable authority: `VISUAL_EVIDENCE_INDEX.jsonl`; ordinary inspection projection: `VISUAL_EVIDENCE_INDEX.csv`; row contract: `VISUAL_EVIDENCE_INDEX.schema.json`.
- Relative paths in the index resolve against the tranche root above.

Every PNG is 1654 × 2339 pixels. The embedded PNG density is 78.74 pixels/cm in both axes, equivalent to 199.9996 ppi and normalized to the accepted 200-ppi render record. The parent PDF reports A4 pages of 595.28 × 841.89 points and page rotation 0. Each record uses a full-image `pixels_top_left` bounding box and does not invent a semantic crop.

## Parent and authority binding

The render parent is `output/pdf/Noether_Paper23_Japanese_SourceReconciled_v001.pdf`, SHA-256 `2D39C6B9D9E81CC38E29A6FB9A354EC489BF13455CC5D96AAF67CAB9FCCEB748`. The linked target TeX is SHA-256 `758D36CA12EA463AD4DC23A04536E801FB9A6B190F8E79E87C668EDC15FEC6D9`; the layout-preserving extraction is SHA-256 `974C77BB552A106BDB8AF97C09B13D11189D7FE9CAB7E5A144AC13B0B332444B`. The linked sealed German P31 whole-file SHA-256 is `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`; the Paper 23 source span, DE 13507–13630, has raw SHA-256 `7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5`.

## QA, supersession, and exclusion

All four accepted page PNGs were inspected individually at original detail by the owning lane and an independent read-only reviewer. The accepted render has no clipping, collision, missing glyph, margin overflow, doubled equation labels, prohibited line-start small kana, or Japanese lexical page-boundary split. Equation labels render exactly once as `(1)`–`(5)`. Page 4 uses a minimal kinsoku control between `ジ` and small `ュ`; normal spacing is retained and the next line begins with regular `ジ`.

The accepted set supersedes the rejected candidates recorded in `BUILD_AND_VISUAL_QA.md`: the initial `有限個` and `その方法` split, the shifted `すなわ／ち` split, doubled display-label parentheses, line-initial small `ュ`, and the over-stretched full-name-box attempt. Rejected renders remain under `tmp/rejected/` as internal debugging evidence and are excluded from the publication manifest. No contact sheet was created or used; individual original-detail PNGs are the sole visual authority.

This index records internal model visual review, not independent human, community, native-language, publication, or source certification.

## Rights and publication disposition

All four files are project-generated target renders from the Japanese project TeX/PDF and contain no third-party scan pixels. Publication totals are:

- `open_payload`: 4
- `restricted_deposit`: 0
- `manifest_only_rights_blocked`: 0
- `excluded_nonproject`: 0

The PNGs, JSONL, CSV, schema, checksum ledger, package manifest, validation report, and this note are to enter the next exact handoff to the existing GitHub/Zenodo repository-custody task. This package creates no competing Zenodo draft and makes no archive deposit itself.
