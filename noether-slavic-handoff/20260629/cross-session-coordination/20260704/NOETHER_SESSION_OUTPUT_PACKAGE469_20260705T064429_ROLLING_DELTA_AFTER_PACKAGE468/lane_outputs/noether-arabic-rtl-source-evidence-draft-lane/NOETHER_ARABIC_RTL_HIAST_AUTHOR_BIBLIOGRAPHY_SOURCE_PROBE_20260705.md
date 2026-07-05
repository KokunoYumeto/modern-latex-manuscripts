# Noether Arabic RTL HIAST Author Bibliography Source Probe

Created: 2026-07-05

Status: draft source-canon/provenance bookkeeping only. Non-canonical, not native reviewed, not approved, not license-cleared, not a translation artifact, not a package, and not a completion claim.

## Purpose

This heartbeat continuation checks author/HIAST bibliography metadata after the official HIAST Algebra I/II PDF packet. It is a provenance-tightening pass: it records author-page DOI/direct-link signals and explicit source-package gaps. It does not add a new mathematical text body.

## Cached Metadata

| Row | Source | Hash | Use |
| --- | --- | --- | --- |
| `AR-HBIB-20260705-002` | Omran Kouba Google Sites Books page | `10F2F587A1018DD45F111E554BBC3A976AD8F5D62578E4D091F636F6B8BD32CD` | Author bibliography metadata for Algebra I/II and DOI/direct-link signals. |
| `AR-HBIB-20260705-003` | Author row `الجبر- مبادئ الجبر المجرّد` | same cached-page hash | Corroborates Algebra I topics and DOI `10.13140/RG.2.2.20526.82245`. |
| `AR-HBIB-20260705-004` | Author row `الجبر- الجبر الخطي` | same cached-page hash | Corroborates Algebra II topics and DOI `10.13140/RG.2.2.28915.43040`. |

## Source-Package Status

The cached author page exposes PDF/DOI/direct-link metadata only. No `LaTeX` literal appears in the captured HTML, and `tex` occurrences are Google Sites/JavaScript text flags rather than mathematical source files. No Arabic TeX/LaTeX/arXiv/e-print/source package was admitted.

## Blockers

The HIAST author tag page appeared in web search but timed out during direct GET and HEAD checks:

`https://hiast.edu.sy/ar/tags/%D8%B9%D9%85%D8%B1%D8%A7%D9%86-%D9%82%D9%88%D8%A8%D8%A7`

No payload or hash was captured for that tag page in this pass, so it remains a blocked row.

## Current Source-Canon Effect

- Adds author-page metadata corroboration for the already-cached official HIAST Algebra I/II witnesses.
- Records DOI signals for Algebra I and Algebra II.
- Records that no additional official Algebra III/source-package body was located in this bounded pass.
- Does not add a new mathematical text body.
- Does not close specialist invariant-theory, Artinian, direct ring-homomorphism, direct isomorphism, or source-package gaps.

## RTL / Layout Notes

The cached Google Sites page embeds Arabic text inside large LTR HTML/JavaScript structures. It is provenance metadata only and not an RTL reading/layout witness. No TeX reader, visual PDF QA, or formula-neighboring layout check was performed.

## Boundary

No raw source bodies are placed in `outputs`. Local cached HTML stays under `sources/...` for provenance hashing. This pass makes no translation, glossary, term approval, bridge promotion, native-review, canonical-approval, license-clearance, gate-promotion, reviewer-packet, package, Git staging, commit, or push claim.
