# Normalization batch 0 — orthography-only dry-run patch proposal

2026-07-05. This is a proposed unified diff for the narrowest orthography-only subset of the R1 normalization work. It does not edit source files. It intentionally excludes lexeme switches such as `odnovrěmenno -> jednočasno` and `sootvětstvovati -> odpovědati`, plus all human-review rows.

## Scope

- Latin v001 TeX files scanned: **395**.

- Files changed by dry run: **129**.

- Occurrences in patch proposal: **305**.

## Rule counts

| Rule | Occurrences |
| --- | ---: |
| take_vzeti_nasal: vzet->vzęt | 111 |
| obci_obsc: obšč->obć | 85 |
| length_orthography: dlugost->dolgost | 62 |
| obci_vobce: vobče/voobče->obće | 47 |

## Surface replacements

| Surface | Replacement | Count |
| --- | --- | ---: |
| `vzet` | `vzęt` | 111 |
| `obšč` | `obć` | 85 |
| `dlugost` | `dolgost` | 62 |
| `vobče` | `obće` | 31 |
| `voobče` | `obće` | 14 |
| `Vobče` | `Obće` | 2 |

## Apply rule

This batch is suitable only as a Codex dry-run input. Before applying, run TeX-aware exclusion for command names, labels, bibliography, source citations, and generated metadata. After applying, rebuild Latin/Cyrillic together and rerun the corpus coverage plus Cyrillic sync checks.
