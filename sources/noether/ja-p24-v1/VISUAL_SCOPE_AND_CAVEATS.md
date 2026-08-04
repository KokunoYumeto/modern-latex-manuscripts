# Japanese Noether Paper 24 visual-evidence scope and caveats

## Indexed payload

- Tranche root: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\japanese\noether_paper24_ja_reconciliation_20260718`
- Image root: `render_check/`
- Accepted visual records: 16 target-render PNGs, one per page of the 16-page accepted Japanese PDF.
- Exact visual bytes: 14,459,676.
- Canonical image-set manifest digest: SHA-256 `B375A9BF0B90B8C52A79694DF4AD59F434B9961C9275A82D2B08EC8F87A569DD`, computed over UTF-8 without BOM, LF-separated `filename,sha256,bytes` lines sorted by filename, with no terminal newline.
- Machine-readable authority: `VISUAL_EVIDENCE_INDEX.jsonl`; ordinary inspection projection: `VISUAL_EVIDENCE_INDEX.csv`; row contract: `VISUAL_EVIDENCE_INDEX.schema.json`.
- Relative paths in the index resolve against the tranche root above.

Every PNG is 1654 × 2339 pixels. ImageMagick read the embedded PNG density as 78.74 pixels/cm in both axes, equivalent to 200 ppi; the accepted render record independently states 200 ppi. The parent PDF reports A4 pages of 595.28 × 841.89 points and page rotation 0. Each record uses a full-image `pixels_top_left` bounding box and does not invent a semantic crop.

## Parent and authority binding

The render parent is `output/pdf/Noether_Paper24_Japanese_SourceReconciled_v001.pdf`, SHA-256 `C1032A418366B61DCC9F7EC743FDA29E60C6CB2CB7032DA4AAC941D95820DBDB`. The linked target TeX is SHA-256 `E597F143D06B8EC4CD0CE5CBE42A1DB77C86D65FD080CDE6206C57379930704E`. The linked sealed German P31 whole-file SHA-256 is `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`; the Paper 24 source span, DE 13631–14119, is SHA-256 `CA71FFFDAB3CEEE3EC614AB30A13F26EEF7D12D95D13875B8613BFC6B8C77232`.

## QA, supersession, and exclusion

All 16 accepted page PNGs were inspected individually at original detail. `BUILD_AND_VISUAL_QA.md` records no clipping, collision, missing glyph, margin overflow, or Japanese lexical unit split in the accepted E597/C103 render. The accepted set supersedes every pre-E597 rejected pagination baseline listed there.

The historical `CONTACT_SHEET.png` was effectively blank, was rejected as visual authority, is absent from the accepted `render_check/` root, and is expressly outside this bounded 16-page retrofit. No contact-sheet binary is indexed or counted.

This index records internal model visual review, not independent human, community, native-language, publication, or source certification.

## Rights and publication disposition

All 16 files are project-generated target renders from the Japanese project TeX/PDF and contain no third-party scan pixels. Publication totals are:

- `open_payload`: 16
- `restricted_deposit`: 0
- `manifest_only_rights_blocked`: 0
- `excluded_nonproject`: 0

The PNGs, JSONL, CSV, schema, checksum ledger, package manifest, validation report, and this note are to enter the next exact handoff to the existing GitHub/Zenodo archive-maintenance task. This retrofit creates no competing Zenodo draft and no archive deposit itself.
