# R3 Persianate Owner Policy Repair Sidecar

Created: 20260705T042425Z

Status: source-canon/provenance repair guidance only. This sidecar does not edit the Persianate/Tajik owner lane and does not publish source payloads.

## Purpose

The Persianate/Tajik owner witness table currently lacks explicit upload_policy/payload_policy/source_upload_policy fields on its rows. This sidecar supplies R3-derived suggested policy classes for those rows so the owner lane and B3 can repair metadata without treating R3 as a translation, review, license, or gate authority.

## Counts

- Owner rows inspected: 17
- Missing-policy rows: 17
- Repair rows emitted: 17
- Rows without policy suggestion: 0
- Rows using fallback derivation: 5

## Boundaries

- No owner-lane files were edited.
- No source bodies or payloads were downloaded or copied into this artifact.
- fa_IR, prs_AF/Dari, tg_Cyrl_TJ, Urdu, Hindustani, and Pan-Turkic remain separate gates.
- No translation, glossary expansion, bridge promotion, native review, canonical approval, license clearance, gate promotion, completion, package, or Git push claim is made.
