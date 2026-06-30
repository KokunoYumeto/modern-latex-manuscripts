# Term ID registry seed - 2026-06-29

This artifact reserves stable term-ID namespaces for the Noether PC branch so reviewer-facing glossary tables and accepted-correction ledgers can refer to term-anchor rows without copying source text or confusing source anchors with approved terminology.

It is not a glossary and not a term-approval ledger. All current term IDs are unreviewed source-anchor handles unless a future accepted-correction ledger changes their state within a reviewed scope.

Companion machine-readable file: `TERM_ID_REGISTRY_SEED_20260629.json`

## ID Principles

- IDs refer to aggregate term-anchor rows in hashed source artifacts.
- IDs are 1-indexed by the row order defined in the corresponding source artifact and filter.
- ID assignment does not approve a term.
- ID assignment does not page-inspect a term.
- ID assignment does not transfer terms across languages, sublanes, or scripts.
- A future accepted correction may point to a term ID, but the accepted correction must carry reviewer scope and artifact hash.

## Reserved Ranges

| Lane / sublane | Prefix | Count | Range | Source artifact basis |
| --- | --- | ---: | --- | --- |
| Simplified Chinese | `term-zh-hans` | 34 | `term-zh-hans-0001` through `term-zh-hans-0034` | `SIMPLIFIED_CHINESE_TERM_ANCHOR_SEED_20260629.json` aggregate row order |
| French | `term-fr` | 21 | `term-fr-0001` through `term-fr-0021` | `ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json` rows where `language == French` |
| Spanish | `term-es` | 25 | `term-es-0001` through `term-es-0025` | `ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json` rows where `language == Spanish` |
| Japanese | `term-ja` | 41 | `term-ja-0001` through `term-ja-0041` | `JAPANESE_TERM_ANCHOR_SEED_20260629.json` aggregate row order |
| Iranian Persian | `term-fa-ir` | 22 | `term-fa-ir-0001` through `term-fa-ir-0022` | `PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json` rows where `sublane == fa_IR` |
| Dari / Afghan Persian | `term-prs-af` | 4 | `term-prs-af-0001` through `term-prs-af-0004` | `PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json` rows where `sublane == prs_AF` |
| Arabic | `term-ar` | 6 | `term-ar-0001` through `term-ar-0006` | `PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json` rows where `sublane == ar` |
| Tajik Cyrillic | `term-tg-cyrl-tj` | 0 | no current range | `PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.json` |

Total current reserved term IDs: 153.

## Source Artifact Hashes

| Artifact | SHA-256 |
| --- | --- |
| `SIMPLIFIED_CHINESE_TERM_ANCHOR_SEED_20260629.json` | `71AC5CA6B93547ACF08E4429E0BCC71B14D183D5AA5B9C9EE74994FC267E7018` |
| `ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json` | `095A4BD781ABF79481A59F3A67E75589B8F69DB72F09F401D2C5F8C541114B14` |
| `JAPANESE_TERM_ANCHOR_SEED_20260629.json` | `26D5D8C5D71093AB3D62408E7A21A457392459F48929DAE52F4DEDF1910DC662` |
| `PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json` | `CE57A11FCE790F3B97B68F1159DD7C274CF81261A525751FFB94490175D52038` |
| `PERSIAN_FAMILY_DARI_TAJIK_REGISTER_GAP_20260629.json` | `A1517654D918E01CA216B93FACE5EDE1B34AD2ACFA78C6609E4B98542ED882CF` |

## Registry Use

Use term IDs in:

- Reviewer-facing glossary tables.
- Review packet questions.
- Accepted-correction ledgers.
- Glossary/rationale updates.
- TeX/PDF rebuild notes.
- Visual inspection notes.
- Cumulative manifest updates.

Do not use term IDs as proof that a term is approved. A term ID is only a stable handle until a reviewer decision and accepted-correction ledger entry promote it.

## Immediate Next Gates

- Generate populated draft reviewer glossary tables using these ID ranges.
- Add `page_inspection_status` for each populated row.
- Connect future accepted corrections to term IDs and artifact hashes.
