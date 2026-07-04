# Noether Persianate/Tajik Upload Policy Backfill Scaffold

Generated UTC: 2026-07-04T20:27:41Z

Status: Session D coordination scaffold for the Persianate/Tajik owner lane. This is not an edit to the Persianate/Tajik lane files, not a GitHub push, not source-license clearance, not native review, not community consent, not canonical approval, not term approval, not gate promotion, and not completion.

## Purpose

The Persianate/Tajik source-canon witness table has source URLs, hashes, license/access signals, topic/language tags, local paths, source types, explicit gaps, and non-claim boundaries. The remaining schema gap is an explicit `upload_policy` or equivalent per witness row.

This scaffold gives conservative proposed `upload_policy` values for the owner lane to adopt or revise. Until the owner lane publishes the repaired field, affected rows remain explicit source-canon gaps for Session D downstream consumption.

## Source Files Checked

| Source file | SHA-256 |
| --- | --- |
| `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_TABLE_20260704.json` | `C75EF869F9AF82C920975A4F0F3FB80C362178E8055C40E7EA007A6DDC7B14BB` |
| `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_WITNESS_TABLE_20260704.md` | `2AE8A8288EA2227AD293F4F38CB9A1CFE4C7CBF3ACFF339AC6B447DDB085EB87` |
| `NOETHER_PERSIANATE_TAJIK_SOURCE_CANON_HEARTBEAT_RECON_20260704T201937Z.md` | `8270689EB4CF37CF0A5E8FDFB26759CBF7ED0003EDCC79E93181815F96B374C4` |

## Proposed Field

Recommended field name:

`upload_policy`

Allowed values used in this scaffold:

- `manifest_only_no_payload_until_license_or_B3_review`
- `conditional_payload_requires_B3_license_attribution_review`
- `blocked_not_uploaded_failed_fetch`
- `gap_only_no_payload`

## Proposed Row Backfill

| Row | Lane | Source title | Source type | Proposed `upload_policy` | Reason |
| ---: | --- | --- | --- | --- | --- |
| 1 | `fa_IR` | Advanced Algebra course PDF | `pdf` | `manifest_only_no_payload_until_license_or_B3_review` | University-hosted PDF; no open license found; local hash supports provenance only. |
| 2 | `fa_IR` | PNU ring/module book preview | `pdf` | `manifest_only_no_payload_until_license_or_B3_review` | Publisher preview/PDF; license/access gap blocks redistribution. |
| 3 | `fa_IR` | Noncommutative prime ideals thesis PDF | `pdf` | `manifest_only_no_payload_until_license_or_B3_review` | University thesis PDF; provenance is strong, but license and review gates remain open. |
| 4 | `fa_IR` | Persian linear algebra TeX source archive | `zip_source_archive` | `manifest_only_no_payload_until_license_or_B3_review` | Source-level archive exists, but no standard open license was found and topic is adjacent rather than Noether algebra. |
| 5 | `fa_IR` | Persian Noether-topic TeX/arXiv source package | `gap` | `gap_only_no_payload` | No Persian-language TeX/arXiv/source archive found for the target Noether-style topic. |
| 6 | `prs_AF` | Algebra - Abdullah Momand | `pdf` | `manifest_only_no_payload_until_license_or_B3_review` | eCampus textbook PDF; no open license found; reviewer gate remains open. |
| 7 | `prs_AF` | eCampus 369 Afghan university textbook list | `html` | `manifest_only_no_payload_until_license_or_B3_review` | Catalog/source-routing only; page footer copyright noted; not a term anchor. |
| 8 | `prs_AF` | Dari TeX/arXiv/invariant-theory source packages | `gap` | `gap_only_no_payload` | No Dari/Afghan Persian TeX/source archive or direct invariant-theory witness found. |
| 9 | `tg_Cyrl_TJ` | Tajik linear algebra Wikimedia raw wikitext | `mediawiki_raw_wikitext` | `conditional_payload_requires_B3_license_attribution_review` | CC BY-SA signal exists, but any payload needs B3 license/attribution review; not blanket clearance. |
| 10 | `tg_Cyrl_TJ` | TNU 2017 conference proceedings | `pdf` | `manifest_only_no_payload_until_license_or_B3_review` | University PDF; no open license found; weak context only. |
| 11 | `tg_Cyrl_TJ` | TGPU ring/field PDF candidate | `failed_pdf_fetch_404_html` | `blocked_not_uploaded_failed_fetch` | URL returned 404 HTML; do not cite as source evidence or upload as source body. |
| 12 | `tg_Cyrl_TJ` | Tajik abstract algebra / TeX source package | `gap` | `gap_only_no_payload` | No reliable Tajik Cyrillic ring/module/ideal/Galois/representation source package isolated. |

## Owner-Lane Repair Instruction

The Persianate/Tajik owner lane should add one explicit upload/distribution field per row. Suggested names:

- `upload_policy`
- `payload_policy`
- `publication_policy`
- `manifest_payload_policy`

The field should make clear whether the row is:

- payload-eligible after B3 review;
- manifest-only;
- blocked/not uploaded;
- gap-only.

## Non-Claim Boundary

This scaffold does not claim source-license clearance, payload eligibility, native review, community/project consent, canonical approval, term approval, bridge approval, gate promotion, completion, or Git push authority.
