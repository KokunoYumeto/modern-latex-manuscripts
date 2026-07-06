# CJK and Arabic source-body fill pass v8.1

2026-07-05. This pass turns the raw probes into lane-facing fill tables. It still does not certify terms or edit text.

## CJK lane marker table

- Concepts in CJK marker table: 97. C2 rows: 67.
- Rows with at least one native CJK hit: 22.

Top rows by native hit count:

| concept            | C2   | ja_form      |   ja_hit_count | zh_hans_form   |   zh_hans_hit_count | ko_form     |   ko_hit_count |   total_native_hit_count |
|:-------------------|:-----|:-------------|---------------:|:---------------|--------------------:|:------------|---------------:|-------------------------:|
| group              | yes  |              |              0 | 群             |                 725 | 군          |              5 |                      730 |
| ring               | yes  | 環           |            111 | 环             |                 191 | 환          |             13 |                      315 |
| field              | yes  | 体           |            114 | 域             |                  70 | 체          |             41 |                      225 |
| isomorphism        | yes  | 同型         |             46 | 同构           |                 118 | 동형사상    |              0 |                      164 |
| homomorphism       | yes  | 準同型       |             36 | 同态           |                 111 | 준동형사상  |              0 |                      147 |
| representation     | yes  | 表現         |             28 | 表示           |                 100 | 표현        |             13 |                      141 |
| algebra            | yes  | 代数         |             81 |                |                   0 | 대수        |             15 |                       96 |
| ideal              | yes  | イデアル     |             84 | 理想           |                   1 | 아이디얼    |              0 |                       85 |
| module             | yes  | 加群         |             26 | 模             |                  20 | 가군        |              1 |                       47 |
| prime ideal        | no   | 素イデアル   |             35 | 素理想         |                   0 | 소 아이디얼 |              0 |                       35 |
| automorphism       | no   | 自己同型     |              7 | 自同构         |                  19 |             |              0 |                       26 |
| finite-dimensional | no   | 有限次元     |              1 | 有限维         |                  22 | 유한 차원   |              0 |                       23 |
| commutative ring   | no   | 可換環       |              7 | 交换环         |                  10 | 가환환      |              0 |                       17 |
| maximal ideal      | no   | 極大イデアル |             12 | 极大理想       |                   0 |             |              0 |                       12 |
| finitely generated | no   | 有限生成     |              3 | 有限生成       |                   2 |             |              0 |                        5 |
| quotient ring      | no   | 商環         |              5 | 商环           |                   0 | 몫환        |              0 |                        5 |
| free module        | no   | 自由加群     |              4 |                |                   0 |             |              0 |                        4 |
| Lie group          | no   | リー群       |              2 |                |                   0 | 리 군       |              0 |                        2 |
| endomorphism       | no   | 自己準同型   |              2 | 自同态         |                   0 |             |              0 |                        2 |
| submodule          | no   | 部分加群     |              1 | 子模           |                   0 |             |              0 |                        1 |

## Controlled Arabic C2 fill ledger

Status counts: {'witness_candidate': 8, 'ocr_candidate_needs_review': 1, 'gap_after_sourcebody_probe': 8, 'not_probed_no_ar_form': 13}

| concept_label              | stratum            | fill_status                | forms              | status_note                                                          |
|:---------------------------|:-------------------|:---------------------------|:-------------------|:---------------------------------------------------------------------|
| coefficient                | curriculum_algebra | witness_candidate          | ['معامل']          | native_sourcebody_candidate; native=16; ocr=62; files=13.            |
| decomposition              | curriculum_algebra | witness_candidate          | ['تحليل', 'تفكيك'] | native_sourcebody_candidate; native=20; ocr=304; files=18.           |
| finite                     | curriculum_algebra | witness_candidate          | ['منته']           | native_sourcebody_candidate; native=54; ocr=154; files=14.           |
| prime ideal                | curriculum_algebra | ocr_candidate_needs_review | ['مثالي أولي']     | ocr_or_extracted_witness_only; native=0; ocr=2; files=1.             |
| absolutely complete system | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| biquadratic form           | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| complete system            | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| contravariant              | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| elementary divisor         | noether_corpus     | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| form system                | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| ground form                | noether_corpus     | witness_candidate          | ['شكل أساسي']      | native_sourcebody_candidate; native=1; ocr=11; files=2.              |
| modulus                    | noether_corpus     | witness_candidate          | ['مودول']          | native_sourcebody_candidate; native=1; ocr=163; files=4.             |
| reduction                  | noether_corpus     | witness_candidate          | ['ردّ', 'اختزال']   | native_sourcebody_candidate; native=60; ocr=428; files=21.           |
| relatively complete system | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| resultant                  | noether_corpus     | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| ternary form               | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| transvection               | noether_corpus     | gap_after_sourcebody_probe | []                 | No hit in current Arabic source-body/OCR shelf.                      |
| assumption                 | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| conversely                 | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| equation                   | proof_grammar      | witness_candidate          | ['معادلة']         | native_sourcebody_candidate; native=40; ocr=299; files=12.           |
| exists                     | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| for all                    | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| formula                    | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| identity                   | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| if and only if             | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| proposition                | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| relation                   | proof_grammar      | witness_candidate          | ['علاقة']          | native_sourcebody_candidate; native=4; ocr=97; files=8.              |
| respectively               | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| statement                  | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |
| therefore                  | proof_grammar      | not_probed_no_ar_form      | []                 | No Arabic query form available in current marker table/curated list. |


## Arabic/Farsi/Persianate C2 fill ledger

Status counts: {'ocr_candidate_needs_review': 2, 'not_probed_no_ar_form': 14, 'witness_candidate': 2}

| concept_label      | stratum            | fill_status                | forms          | status_note                                                          |
|:-------------------|:-------------------|:---------------------------|:---------------|:---------------------------------------------------------------------|
| prime ideal        | curriculum_algebra | ocr_candidate_needs_review | ['مثالي أولي'] | ocr_or_extracted_witness_only; native=0; ocr=2; files=1.             |
| elementary divisor | noether_corpus     | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| resultant          | noether_corpus     | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| assumption         | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| conversely         | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| equation           | proof_grammar      | witness_candidate          | ['معادلة']     | native_sourcebody_candidate; native=40; ocr=299; files=12.           |
| exercise           | proof_grammar      | ocr_candidate_needs_review | ['تمارين']     | ocr_or_extracted_witness_only; native=0; ocr=1; files=1.             |
| exists             | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| for all            | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| formula            | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| identity           | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| if and only if     | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| notation           | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| proposition        | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| relation           | proof_grammar      | witness_candidate          | ['علاقة']      | native_sourcebody_candidate; native=4; ocr=97; files=8.              |
| respectively       | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| statement          | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |
| therefore          | proof_grammar      | not_probed_no_ar_form      | []             | No Arabic query form available in current marker table/curated list. |

## Important caveat

The CJK package contains two manifest-like tables with conflicting source-use labels. `manifest.csv` correctly separates generated-draft rows from native-source-body rows; `SOURCE_BODIES.csv` labels generated/audit files as native-source-body. This pass uses `manifest.csv`.