# R9 OCR / Source-Owner Priority Queue

Generated: 2026-07-05T00:45:52.752079+00:00 UTC

## Boundary

This queue is derived from `R9_LOCAL_SOURCE_BODY_PROVENANCE_SPINE_20260705.csv`. It prioritizes OCR/Unicode, source-owner, licensing-signal, and reviewer-return work. It does not extract new source text, translate, approve terminology, clear licenses, claim native/community review, promote gates, package, stage, commit, or push.

## Priority Counts

| priority | lane | count |
|---|---|---:|
| P0 | source-owner/license/reviewer gate for text-layer body | 188 |
| P1A | Amharic OCR/font-map repair | 45 |
| P1B | Tigrigna/Tigrinya render/text-layer comparison | 29 |
| P1C | Latin-script weak/empty extraction repair | 25 |
| P2 | known-route capture retry | 4 |
| P3 | route metadata needs source body/reviewer return | 10 |
| P4 | context/nonbody needs exact target math transcript/source | 25 |

## Language / Priority Matrix

| row | P0 | P1A | P1B | P1C | P2 | P3 | P4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Afar/Qafar | 0 | 0 | 0 | 0 | 0 | 0 | 16 |
| Amharic | 3 | 45 | 0 | 0 | 0 | 0 | 0 |
| Hausa | 0 | 0 | 0 | 0 | 0 | 5 | 0 |
| Igbo | 0 | 0 | 0 | 0 | 0 | 5 | 0 |
| Oromo | 70 | 0 | 0 | 13 | 1 | 0 | 0 |
| Somali | 62 | 0 | 0 | 12 | 1 | 0 | 9 |
| Tigrigna/Tigrinya | 53 | 0 | 29 | 0 | 2 | 0 | 0 |

## First Closure Candidates

| priority | row | spine row | source | next action |
|---|---|---|---|---|
| P0 | Amharic | R9-LSB-0014 | Maths grade 2 in Amharic | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Amharic | R9-LSB-0045 | Math grade 6 in Amharic | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Amharic | R9-LSB-0048 | Math grade 6 in Amharic | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0050 | Math grade 1 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0064 | Math grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0065 | Math grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0066 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0067 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0068 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0069 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0070 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0071 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0072 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0073 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0074 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0075 | Maths grade 2 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0076 | Math grade 3 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0077 | Math grade 3 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0078 | Maths grade 3 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |
| P0 | Oromo | R9-LSB-0079 | Maths grade 3 in Oromo | Preserve hash/path/URL; request source-owner or reviewer source-return on language/variety, topic tags, attribution, and access/license signal before any use. |

## Notes

- `P0` rows are not accepted; they only have text-layer evidence and still need source-owner/license/reviewer closure.
- `P1*` rows should be repaired/audited before any text can be trusted.
- `P2`/`P3`/`P4` rows are source-return gaps, not translation evidence.
- Every row sets `promotion_allowed=false`.

CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\outputs\R9_OCR_SOURCE_OWNER_PRIORITY_QUEUE_20260705.csv`
