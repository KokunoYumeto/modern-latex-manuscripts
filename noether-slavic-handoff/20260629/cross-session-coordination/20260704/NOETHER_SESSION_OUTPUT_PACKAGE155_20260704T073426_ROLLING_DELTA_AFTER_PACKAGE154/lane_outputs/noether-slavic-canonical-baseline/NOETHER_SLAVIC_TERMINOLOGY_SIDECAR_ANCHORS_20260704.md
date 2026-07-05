# Noether Slavic Terminology Sidecar Anchors

Generated: 2026-07-04T07:29:44.0698458+02:00

Lane: Session L, Noether Slavic Canonical Baseline Support

Main tree: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical`

Status: stable sidecar anchor packet. This records current Ukrainian/Russian/Interslavic terminology infrastructure and does not claim external/native review completion.

## Decision

The current Slavic terminology sidecar layer is anchorable without rebuilding the released readers. The canonical glossary, terminology rationale logs, Interslavic logbook, and Interslavic Cyrillic transliteration reports now have explicit aggregate hashes that can be checked by the Slavic watcher.

This closes a watcher-boundary gap: previous watcher documentation named terminology/sidecars as a rebuild trigger class, but executable checks focused on packages, source inventory, cumulative readers, review returns, and Zenodo source fingerprints. The watcher can now detect direct glossary/logbook/transliteration drift.

## Stable Anchors

| Anchor | Count | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| Canonical glossary JSON sidecars | 214 | 2665586 | `5E5E8CFD145AD1B3CEE217F3ABB6CC99C05929FD3551FC89F673E3E2F5EA9F56` |
| Terminology rationale coverage JSON | 1 | 73283 | `1D38516CD5FE604ADF1C8DC246B130E238BADAE39564E93CD2CF991EB5F34574` |
| Terminology rationale coverage markdown | 1 | 765 | `332BADE6CCA20F1D54CBAC269D1AA35A8DFAA38E2BAF197D2529A9CB60383FD1` |
| Terminology decision logbook | 1 | 468170 | `134E02E2F0E80D707D3981539E73172D8067312E4F32BC138546331F28112465` |
| Interslavic logbook | 1 | 387565 | `84D19DE8E8D85734A5CC7EAB12B4BD855EABD533A52DAC5C862C57AF93EEA5C9` |
| Interslavic Cyrillic transliteration reports | 187 | 1502837 | `59931CEE832E9A2A7B709390D028AD70F2E47460E1DD1B074DC04B0CC06E0078` |

## Scope

Canonical glossary anchor scope:

- Include `glossary/noether_*_terms.json`.
- Exclude noncurrent repair backups, especially `*before_section09*`.
- Exclude working seeds, especially `*working*`.
- Exclude French/non-Slavic glossary sidecars from Slavic canonical anchoring.

Transliteration anchor scope:

- Include only reports under `translations/*/source_fidelity/interslavic-cyrillic/`.
- Hash preimage is sorted LF-joined `path|bytes|sha256` rows with forward-slash relative paths.
- This checks sidecar traceability only; it does not assert native authority approval.

## Transliteration Report Distribution

| Unit group | Reports |
| --- | ---: |
| endmatter | 3 |
| paper01 | 1 |
| paper02 | 26 |
| paper03 | 1 |
| paper04 | 10 |
| paper05 | 1 |
| paper06 | 16 |
| paper07 | 1 |
| paper08 | 1 |
| paper09 | 11 |
| paper10 | 4 |
| paper11 | 1 |
| paper12 | 1 |
| paper13 | 1 |
| paper14 | 1 |
| paper23 | 1 |
| paper24 | 7 |
| paper25 | 1 |
| paper26 | 1 |
| paper27 | 1 |
| paper28 | 1 |
| paper29 | 1 |
| paper30 | 11 |
| paper31 | 48 |
| paper32 | 11 |
| paper33 | 1 |
| paper34 | 14 |
| paper35 | 2 |
| paper36 | 1 |
| paper37 | 1 |
| paper38 | 1 |
| paper39 | 1 |
| paper40 | 1 |
| paper41 | 1 |
| paper42 | 1 |
| paper43 | 1 |

## Rebuild Triggers

A Slavic rebuild or targeted rerender is required if any of these occur:

- A canonical glossary file is added, removed, or hash-changed by an accepted terminology mutation.
- The terminology rationale coverage JSON loses required schema keys or changes without a logged accepted reason.
- `TERMINOLOGY_DECISION_LOGBOOK.md` or `INTERSLAVIC_LOGBOOK.md` changes as part of an unlogged terminology/legibility mutation.
- Interslavic Cyrillic transliteration report count, bytes, aggregate hash, or path set changes.
- A Latin/Cyrillic sidecar mismatch is confirmed.

Non-triggers:

- Additional broad Slavic references used only for review routing.
- arXiv/corpus method references.
- Non-Slavic discovery in other lanes.
- Blank review templates or review scaffolds.

External/native authority review remains incomplete until real Slavic returns are schema-valid, accepted corrections are applied, affected outputs are rebuilt, and independent validation passes.
