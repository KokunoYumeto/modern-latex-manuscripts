# Noether Slavic Source-Canon First Status - 2026-07-04

This folder is the source-canon-first shelf for the Slavic target-language cluster.
It is support/provenance evidence only. It is not a translation-completion, native-review,
canonical-approval, terminology-promotion, or blanket-license-clearance claim.

## Scope

Target cluster: Polish, Czech, Slovak, Slovene, Serbian, Croatian, Bosnian,
Montenegrin, Bulgarian, Macedonian, Belarusian, Upper Sorbian, and Lower Sorbian.

Excluded from this source-canon target: Russian and Ukrainian.

## Published Artifacts

- `NOETHER_SLAVIC_SOURCE_CANON_ARXIV_20260704T184700Z`
  - arXiv/source-candidate sweep plus local Slavic math reference shelf index.
  - 1,353 arXiv metadata candidate rows.
  - 50 local reference-shelf rows.
  - 0 redistributable arXiv TeX/source payload files under strict license gating.
  - Includes explicit gap and blocked/not-uploaded manifests.

- `NOETHER_SLAVIC_SOURCE_CANON_GITHUB_TEX_20260704T190700Z`
  - GitHub TeX code-search sweep using one native math term per cluster language.
  - 225 target-language TeX candidate rows.
  - 96 repository license rows.
  - 0 uploaded TeX bodies because every hit in this wave lacked recognized open-source license metadata.
  - Includes blocked/not-uploaded manifests rather than raw unverified source dumps.

- `NOETHER_SLAVIC_SOURCE_CANON_GITHUB_TEX_20260704T192100Z`
  - GitHub TeX code-search sweep using two native math terms per cluster language after fixing license-key parsing.
  - 341 target-language TeX candidate rows.
  - 163 repository license rows.
  - 94 open-license TeX payload files in `payload_zips/NOETHER_SLAVIC_GITHUB_TEX_OPEN_LICENSE_PAYLOAD_20260704T192100Z.zip`.
  - Payload SHA-256: `14BE80F52F67E74A7F3CC791621E4C27432DCC3AFDC394B50CA161FECA4105BF`.
  - Payload QA: 94 zip entries, explicit TeX-family source extensions only, zero zero-byte entries.
  - Payload coverage by language: Polish 5, Czech 8, Slovak 9, Slovene 8, Serbian 9, Croatian 9, Bosnian 6, Montenegrin 6, Bulgarian 5, Macedonian 1, Belarusian 11, Upper Sorbian 3, Lower Sorbian 14.
  - 248 candidates remain blocked/not uploaded because license/provenance evidence was not sufficient for redistribution or because they were not admissible source-extension payloads.

## Current Hard Status

The first usable uploaded source-corpus payload now exists, but the corpus is still
incomplete. The current artifacts make the gap visible and searchable, but they do
not yet provide the requested hundreds of open-source source-level TeX witnesses per
language.

All downstream translation lanes should treat source-canon acquisition as priority one.
Generated Noether translations must remain separate from source-canon evidence.

## Next Required Work

1. Expand language-specific source searches with stricter native-language math terms.
2. Prefer source-level TeX/LaTeX and source archives with clear open-source redistribution evidence.
3. Add PDF/DOCX/text provenance where source TeX is unavailable, but keep those separate from TeX payloads.
4. Publish payload zips only when license/provenance gates allow redistribution.
5. Keep explicit missing/blocked rows for languages and sources that remain below target.
