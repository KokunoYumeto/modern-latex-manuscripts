# OtherPC source-body work pass v8 — CJK / Arabic / OLP / Turkish block

2026-07-05. Intake and source-body probe pass over the laptop Codex drops. No term promotion, no production text edits, no external-review claim.

## Package audit

- Packages audited: 7; SHA256 ok: 7/7.

| package | entries | MB | sha ok | role |
|---|---:|---:|---|---|

| OtherPC_Arabic_RTL_SourceBodies_20260705.zip | 256 | 146.27 | True | Arabic RTL source-body shelf |

| OtherPC_CJK_Draft_SourceEvidence_20260705.zip | 46 | 17.24 | True | CJK draft/source-evidence split shelf |

| OtherPC_CJK_Native_SourceBodies_20260705.zip | 127 | 2.26 | True | CJK native source-body shelf |

| OtherPC_Fable_Ledger_Block_20260705.zip | 22 | 0.03 | True | Turkish Noether ledger block |

| OtherPC_Noether_SourceCorpus_Provenance_20260705.zip | 1363 | 140.65 | True | source-canon provenance |

| OtherPC_NonSlavic_Core_Coordination_20260705.zip | 15 | 0.05 | True | coordination state |

| OtherPC_OLP_Relation_Function_Support_20260705.zip | 229 | 26.79 | True | OLP/relation-function source support |


## CJK native source-body probe

- Scaffold rows probed: 81; native source-body attested: 39; no native hit yet: 42.

- Hits by lane:

  - japanese: 19/29 rows with native source-body hits.

  - korean_addendum: 7/23 rows with native source-body hits.

  - simplified_chinese: 13/29 rows with native source-body hits.


Top CJK hit rows:

| lane               | concept        | draft_target_rendering   |   native_hit_count |   native_file_hit_count | status                     |
|:-------------------|:---------------|:-------------------------|-------------------:|------------------------:|:---------------------------|
| simplified_chinese | group          | 群                       |                725 |                       8 | native_sourcebody_attested |
| simplified_chinese | ring           | 环                       |                191 |                      11 | native_sourcebody_attested |
| simplified_chinese | isomorphism    | 同构                     |                118 |                       7 | native_sourcebody_attested |
| japanese           | field          | 体                       |                114 |                      14 | native_sourcebody_attested |
| japanese           | ring           | 環                       |                111 |                      10 | native_sourcebody_attested |
| simplified_chinese | homomorphism   | 同态                     |                111 |                       4 | native_sourcebody_attested |
| simplified_chinese | representation | 表示                     |                100 |                      10 | native_sourcebody_attested |
| japanese           | ideal          | イデアル                 |                 84 |                      10 | native_sourcebody_attested |
| japanese           | algebra        | 代数                     |                 81 |                      13 | native_sourcebody_attested |
| simplified_chinese | field          | 域                       |                 70 |                       7 | native_sourcebody_attested |
| japanese           | isomorphism    | 同型                     |                 46 |                       5 | native_sourcebody_attested |
| korean_addendum    | field          | 체                       |                 41 |                       3 | native_sourcebody_attested |
| japanese           | homomorphism   | 準同型                   |                 36 |                       4 | native_sourcebody_attested |
| japanese           | prime ideal    | 素イデアル               |                 35 |                       5 | native_sourcebody_attested |
| japanese           | representation | 表現                     |                 28 |                       4 | native_sourcebody_attested |


Boundary: generated CJK draft scaffolds only supplied query forms; native source-body hits came from `source-files/` texts. SOURCE_BODIES.csv mislabels generated/audit rows as native-source-body; `manifest.csv` was used instead.


## Arabic RTL source-body probe

- Concepts/forms probed: 77; native source-body candidate hits: 49; OCR/extracted-only: 12; no hit: 16.

- Arabic source corpus scanned: 40 text-extractable files (native-source-body or OCR-witness; PDF source bodies skipped in this bounded pass; included OCR/extracted/native text/html witnesses used).


Top Arabic hit rows:

| concept         | stratum            | forms_probed                                                                                                                      |   native_hit_count |   ocr_hit_count |   file_hit_count | status                      |
|:----------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------|-------------------:|----------------:|-----------------:|:----------------------------|
| group           | curriculum_algebra | زمر | زمرة                                                                                                                        |                992 |             658 |               22 | native_sourcebody_candidate |
| algebra         | curriculum_algebra | جبر | جبور | الجبر | compound | بنية جبرية | الجبر التبديلي | الجبر التجريدي | object use: جبر | plural structures: جبور [review] |                377 |             584 |               33 | native_sourcebody_candidate |
| field           | curriculum_algebra | جسم | حقل | مجال | الحقل | حقل دوال | حقل عددي | الدوال الكسرية | الدوال الناطقة | حقل الدوال الكسرية                             |                168 |             564 |               22 | native_sourcebody_candidate |
| theorem         | proof_grammar      | نظرية | مبرهنة | مبرهنات                                                                                                          |                167 |             397 |               29 | native_sourcebody_candidate |
| set             | curriculum_algebra | مجموعة                                                                                                                            |                 84 |             540 |               27 | native_sourcebody_candidate |
| ring            | curriculum_algebra | حلقة | حلقات | مجال حلقي | نطاق حلقي | نطاق تكاملي | نظرية الحلقات | Ringbereich draft: نطاق حلقي [review]                        |                 74 |             491 |               25 | native_sourcebody_candidate |
| vector          | curriculum_algebra | متجه                                                                                                                              |                 74 |              43 |               12 | native_sourcebody_candidate |
| subset          | curriculum_algebra | جزئية | مجموعة جزئية                                                                                                              |                 63 |             255 |               21 | native_sourcebody_candidate |
| element         | curriculum_algebra | عناصر                                                                                                                             |                 62 |             207 |               19 | native_sourcebody_candidate |
| reduction       | noether_corpus     | ردّ | اختزال                                                                                                                       |                 60 |             428 |               21 | native_sourcebody_candidate |
| isomorphism     | curriculum_algebra | تماثل | متماثل | تماثل حلقي | إيزومورفيزم | ايزومورفيزم | تشاكل تقابلي | التطبيق التماثلي | حلقة التماثلات الذاتية                |                 60 |             158 |               16 | native_sourcebody_candidate |
| finite          | curriculum_algebra | منته                                                                                                                              |                 54 |             154 |               14 | native_sourcebody_candidate |
| map/application | non_c2_or_existing | تطبيق                                                                                                                             |                 50 |             648 |               22 | native_sourcebody_candidate |
| function        | curriculum_algebra | دالة                                                                                                                              |                 41 |             127 |               11 | native_sourcebody_candidate |
| equation        | proof_grammar      | معادلة                                                                                                                            |                 40 |             299 |               12 | native_sourcebody_candidate |
| basis           | curriculum_algebra | أساس | قاعدة                                                                                                                      |                 36 |             503 |               22 | native_sourcebody_candidate |
| matrix          | curriculum_algebra | مصفوفة                                                                                                                            |                 35 |             332 |               11 | native_sourcebody_candidate |
| definition      | proof_grammar      | تعريف                                                                                                                             |                 29 |             311 |               21 | native_sourcebody_candidate |
| representation  | curriculum_algebra | تمثيل                                                                                                                             |                 29 |             192 |               11 | native_sourcebody_candidate |
| factor          | curriculum_algebra | عامل                                                                                                                              |                 27 |             333 |               16 | native_sourcebody_candidate |


## OLP relation/function support

| concept    |   hit_count |   file_count | status                   |
|:-----------|------------:|-------------:|:-------------------------|
| function   |        8753 |           78 | source_support_candidate |
| relation   |        4649 |           70 | source_support_candidate |
| set        |        4503 |           85 | source_support_candidate |
| coordinate |        4054 |           40 | source_support_candidate |
| domain     |         782 |           53 | source_support_candidate |
| range      |         574 |           51 | source_support_candidate |
| proof      |         569 |           71 | source_support_candidate |
| graph      |         211 |           43 | source_support_candidate |
| definition |         170 |           39 | source_support_candidate |
| matrix     |          58 |           17 | source_support_candidate |
| polynomial |          58 |            4 | source_support_candidate |
| theorem    |          14 |            7 | source_support_candidate |


## Turkish Noether block

| concept          | draft_surface                                     | alternatives_retained                                |   max_branch_weight |   adverse_rows |   false_friend_rows | status                  |
|:-----------------|:--------------------------------------------------|:-----------------------------------------------------|--------------------:|---------------:|--------------------:|:------------------------|
| Noetherian ring  | Noether halkası                                   | Noetherian halka                                     |                0.62 |              2 |                   1 | draft evidence decision |
| polynomial ring  | polinom halkası                                   | none selected in this block                          |                0.83 |              1 |                   1 | draft evidence decision |
| ideal            | ideal family: ideal/ideali/idealler               | inflected forms retained instead of one flat surface |                0.76 |              1 |                   1 | draft support family    |
| theorem scaffold | IF R NOETH-RING -> R[x] POLY-RING ALSO NOETH-RING | not a Turkish surface                                |              nan    |              0 |                   0 | review scaffold only    |


## Next use

- Feed CJK hits into a CJK lane marker table as `native_sourcebody_candidate`, not as accepted terminology.

- Feed Arabic hits into the controlled-Arabic C2 ledger as `sourcebody_context_review`, keeping OCR-only rows separate.

- Feed Turkish block as a Pan-Turkic hard-blocker seed only for Turkish; do not export to other Turkic languages.

- Use OLP hits as source-side proof-literacy scaffolding; not target-language witness evidence.
