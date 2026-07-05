# Noether CJK Draft Translation-Support Notes

Generated: 2026-07-04

Status: draft/non-canonical support notes only.

These notes are for future reviewer/source packets. They are not a translation patch, glossary promotion, native-review result, public signoff, interlanguage pilot, pan-CJK language, or Korean-school claim.

## Supportable Uses

- Cite `logs/CJK_INVARIANT_REPRESENTATION_CODEPOINT_REDO_CONTENT_CONFIRMATION_20260703T123013Z.md/json` for exact Unicode/codepoint-built Chinese and Japanese representation/invariant source evidence.
- Cite `logs/CJK_HARDTERM_SOURCE_REFRESH_20260703T105104Z.md/json` for the four fixed-commit Chinese/Japanese hard-term source files and the small Chinese source archive.
- Cite `logs/CHINESE_JAPANESE_LABEL_AND_SOURCE_BASELINE_REFRESH_20260703T155016Z.md/json` before describing the current Simplified Chinese or Japanese native-edition labels.
- Cite `logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260703T155415Z.md/json` as the current local CJK baseline after label and sidecar metadata refresh.
- Cite `logs/CJK_TIBETO_BURMAN_PACIFIC_LOCAL_STANDARD_DECISIONS_20260629T073000Z.md/json` when routing Korean material into CJK/Sino-Xenic crosswalk work.

## Non-Canonical Reviewer Packet Language

Allowed phrasing:

- "source-evidence strengthened"
- "content-confirmed TeX witness"
- "native-edition source-fidelity reader"
- "current local baseline"
- "crosswalk routing candidate"
- "draft/non-canonical support note"

Avoid phrasing:

- "approved term"
- "final CJK edition"
- "publicly signed off"
- "native-reviewed completion"
- "pan-CJK language"
- "Korean-school interlanguage"
- "Korean edition"

## Simplified Chinese Support Boundary

Use the current source-fidelity cumulative reader label only with its full caveat:

`native_edition_source_fidelity_cumulative_reader_papers01_43_post44_post45_postbibliography_current_local_internal_review_no_public_signoff`

When citing source state, pair the label with:

- Source TeX SHA256 `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`.
- PDF SHA256 `43B5490CE42640CF6F8322670E01FD535507DA6CB94131B25E1803EAA64E3D96`.
- July 3 Zenodo action `NO_SOURCE_REPLACEMENT_REQUIRED`.

Do not collapse this into public completion language.

## Japanese Support Boundary

Use the current source-fidelity cumulative reader label only with its full caveat:

`native_edition_source_fidelity_cumulative_reader_ra10_papers40_43_resynced_canonical_noto_validated_internal_review_closed_no_public_signoff`

When citing source state, pair the label with:

- Source TeX SHA256 `4A284DF3FAC4D53D305659B539AF2FEB17902BFB4C254A7DF62A155C6BC23131`.
- PDF SHA256 `5F9299F8D95D14EDBF8FE12332280CE024B26B15DDEA96FB4D9A96BE96F20920`.
- July 3 Zenodo action `NO_SOURCE_REPLACEMENT_REQUIRED`.

Do not collapse internal review closure into external/public signoff.

## Korean Addendum Boundary

Evidence exists for routing, not for a Korean edition:

- `ASIA-EAST-KO-01`: KAIST math notes, GitHub TeX notes repository, `171` source files, evidence class `strong_math_tex_source`.
- `ASIA-EAST-KO-02`: ko.TeX utilities, CTAN source package, evidence class `tex_infrastructure_no_term_hits`.
- R7 local-standard decision: CJK/Sino-Xenic work is controlled native editions plus crosswalks; no pan-CJK language.

Safe next note: "Korean rows may be added to a future CJK/Sino-Xenic term-crosswalk manifest as source-evidence rows only, after row-level term extraction."

Unsafe next note: "Korean is part of a CJK interlanguage edition."

## Draft Crosswalk Skeleton

Future crosswalk row fields should include:

- concept_id
- source_language
- source_register
- term_surface_or_codepoint_sequence
- evidence_artifact
- local_source_path
- source_sha256
- content_confirmed
- reviewer_status
- promotion_status
- notes

Default values for new rows:

- `content_confirmed`: false until checked against local source text.
- `reviewer_status`: `not_reviewed`.
- `promotion_status`: `draft_non_canonical`.
