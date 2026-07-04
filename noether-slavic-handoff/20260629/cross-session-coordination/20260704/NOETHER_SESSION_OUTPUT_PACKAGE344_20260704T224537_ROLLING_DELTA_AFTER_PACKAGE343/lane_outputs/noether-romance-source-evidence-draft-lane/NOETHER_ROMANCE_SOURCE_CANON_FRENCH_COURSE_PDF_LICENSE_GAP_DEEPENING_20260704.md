# Noether Romance Source-Canon French Course-PDF License Gap Deepening

Status: draft / non-canonical / provenance-only / not native reviewed / not approved.

Created: 2026-07-04.

Scope: source-canon maintenance for the two remaining weak French course-note PDF witnesses: FR-C-007 and FR-C-010. This note records evidence for the rights/license gap only. It does not clear licenses, approve terms, translate corpus prose, populate reviewer packets, promote gates, or authorize a Git push from this lane.

## Summary

- Updated base witness table: `NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_20260704.csv`.
- Regenerated required-shape table: `NOETHER_ROMANCE_SOURCE_CANON_WITNESS_TABLE_REQUIRED_SHAPE_20260704.csv`.
- Regenerated field audit: `NOETHER_ROMANCE_SOURCE_CANON_FIELD_COMPLETENESS_AUDIT_20260704.csv`.
- Created probe CSV: `NOETHER_ROMANCE_SOURCE_CANON_FRENCH_COURSE_PDF_GAP_PROBES_20260704.csv`.
- Created row-deepening CSV: `NOETHER_ROMANCE_SOURCE_CANON_FRENCH_COURSE_PDF_LICENSE_GAP_DEEPENING_20260704.csv`.
- Extracted PDF text and `mutool info` metadata into `outputs/source_canon_pdf_text_probe/`.

## Evidence Checked

| Row | Web evidence | Local probe | Result |
|---|---|---|---|
| FR-C-007 | Mourougane's 2024-25 ACGA course page links `Poly de cours`; the course page lists commutative algebra / algebraic geometry topics, including noetherian rings and Hilbert zero theorem contexts. | Local PDF hash `c3c2588f0ab62edcb4a8dbf2014afe5dc5f8b8fc1d54c595a29fdc016aa93dd6`; text probe hash `9854b597de38e39396a1119eed5e0175bc17278fd8f2eb2643f37b350d13f896`; metadata probe hash `6d0c425fad74a660d773b3f181e9894c027485d482852822648edcfc52cb497e`; rights-string hit count `0`. | Explicit rights/license gap retained. The PDF remains a local provenance and register witness only. |
| FR-C-010 | Marche's M2 teaching page links `Notes de cours` for `Theorie Geometrique des invariants`; the page also has a separate caution that some references used in the notes are not to be diffused. | Local PDF hash `8731e06f40b8354d58d6d938418d6e061a81af1efda2d4524dddaf1b6084c384`; text probe hash `1028b32b097e40ec12c8f7e66d8612beea1ae8d1f32b2fae6eb65a2953ea1f72`; metadata probe hash `7a509360abb0506913958969c0bac0a9b122d17a1ed9299f8e98f148c3cb3f87`; rights-string hit count `0`. | Explicit rights/license gap retained. The PDF remains a local provenance and register witness only. |

## Probe Pattern

The local text and metadata probes searched for rights-related strings including `license`, `licence`, `copyright`, `Creative Commons`, `CC-BY`, `droits`, `reproduction`, `diffusion`, `autorisation`, `usage`, `utilisation`, `tous droits`, `copie`, and `distribution`.

## Current Weak Rows

After this pass, the field audit still has four weak/gap license-access rows:

- FR-C-007: course PDF rights/license gap retained after web page, text, and metadata probe.
- FR-C-010: course PDF rights/license gap retained after web page, text, and metadata probe.
- ES-B-002: public TeX repository with no detected explicit license.
- ES-GAP-004: explicit license-gap row for ES-B-002.

## Boundary

This is a source-canon gap-deepening note. It makes the provenance record more precise, but it is not license clearance, native review, canonical approval, bridge promotion, gate completion, or a Git push.
