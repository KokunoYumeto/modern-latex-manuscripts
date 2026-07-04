# R9 Live GitHub/Hugging Face Source-Archive Probe - 2026-07-04

This artifact continues the R9 Africa/Horn/West Africa source-canon-first lane
after the required-field witness-table alignment. It records a live metadata
probe for additional GitHub and Hugging Face source/archive candidates for
Hausa, Amharic, Afar-adjacent gaps, Somali, Oromo, Tigrinya/Tigrigna, Twi,
Yoruba, Wolof, and related rows.

Boundary: this is source-canon/provenance/gap evidence only. It does not approve
translation, terminology, native/community review, canonical status, source
license clearance, gate promotion, completion, package upload, or Git push.

## Probe Method

- GitHub repository-search metadata was fetched through the GitHub API.
- Hugging Face dataset-search metadata was fetched through the Hugging Face API.
- Candidate repository/dataset metadata was captured when a result appeared.
- Raw dataset bodies, CSV contents, parquet shards, zip primaries, OCR caches,
  runtime files, and credentials were not captured.
- Every row in the CSV has `promotion_allowed=false`.

Machine-readable ledger:

`R9_LIVE_GITHUB_HF_SOURCE_ARCHIVE_PROBE_20260704.csv`

Local metadata root:

`work/source_canon_witnesses/20260704_r9_archive_probe/`

## Finds

### Amharic Candidate, Blocked

GitHub returned one candidate for `amharic math dataset`:

`https://github.com/Aman-byte1/amharic-conversation-and-math-dataset`

The repository page identifies it as an Amharic question-answer/conversation
dataset and exposes `README.md`, `conversations_amharic.csv`, and
`math_intelligence.csv`. The GitHub API reports `license=null`, and the root
contents metadata did not show a `LICENSE` file. The candidate is therefore
recorded as metadata-only and blocked pending license/source-owner return.

Local metadata hashes:

- Repository metadata:
  `DFD8231AF627823F3905EFC444E5A26BECEA3D682CB11E3EF9D29F9B80CD858D`
- Root contents metadata:
  `AEC0149E7CA3868524902F1B29416B21C14CB05C61BB320996B728BE6B13AA4F`

### Twi-Named Hugging Face Candidate, Blocked

Hugging Face returned one candidate for `twi math`:

`https://huggingface.co/datasets/qixiangbupt/mathvr_twi`

The API metadata reports dataset SHA
`5b7c56d32f5380d31410ad1352675806638c4087` and 35 parquet siblings, but
`cardData` was null and no license or language-evidence tag was available in
the captured metadata. The candidate is therefore blocked as ambiguous and
metadata-only.

Local metadata hash:

`847DF95F10B1F62AB39C2AD0219F86B017DEBC8A8E8FEF44AF46CC271129723F`

## Explicit Gap Rows

These live searches returned zero results and are recorded as explicit
source-archive gaps:

- GitHub: `amharic mathematics dataset`
- GitHub: `hausa math dataset`
- GitHub: `hausa lissafi mathematics`
- GitHub: `somali xisaab math`
- GitHub: `oromo herrega math`
- GitHub: `tigrinya numbers math`
- GitHub: `yoruba mathematics dataset`
- Hugging Face: `amharic math`
- Hugging Face: `hausa math`
- Hugging Face: `somali math`
- Hugging Face: `oromo math`
- Hugging Face: `yoruba math`
- Hugging Face: `wolof math`
- Hugging Face: `tigrinya numbers`

The zero-result metadata files are retained and hashed in the CSV so future
work can distinguish "not searched" from "searched and no metadata result under
this exact query."

## Next Source-Acquisition Moves

- Amharic: request or locate a license/source-owner return for the GitHub math
  dataset candidate before any body capture or source-canon use.
- Twi/Akan: inspect whether `mathvr_twi` has a hidden card, paper, or license
  outside the API metadata; until then keep it blocked and do not ingest parquet
  bodies.
- Hausa, Somali, Oromo, Yoruba, Wolof: broaden source-archive terms and prefer
  official school/university source repositories or source-owner files over
  generic dictionary/lexicon hits.
- Tigrinya/Tigrigna: keep the arXiv/GitHub number-verbalization source package
  as the only current source-level archive witness; it still does not close
  algebra/invariant-theory gaps.
