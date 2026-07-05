# CJK Controlled Pre-Translation Register

Generated: 2026-07-05T18:44:17+00:00

Status: generated-draft / non-canonical / controlled pre-translation register only.

This packet is a data object for CJK pre-translation and interlinear comparison. It is not a finished independent interlanguage, not native review, not accepted terminology, and not translation completion.

## Use Classes

- `register_scaffold_candidate_tri_branch`: 22 rows
- `register_scaffold_candidate_gap_backfill_required`: 19 rows
- `do_not_use_for_translation_sparse_source`: 0 rows

| Register ID | Concept | Use class | JP | zh-Hans | ko source |
| --- | --- | --- | --- | --- | --- |
| `CJK-PRE::module` | module | `register_scaffold_candidate_tri_branch` | 加群 | 模 | 가군 |
| `CJK-PRE::simple_module` | simple module | `register_scaffold_candidate_gap_backfill_required` | 単純加群 | GAP | 단순 가군 |
| `CJK-PRE::free_module` | free module | `register_scaffold_candidate_gap_backfill_required` | 自由加群 | GAP | 자유 가군 |
| `CJK-PRE::submodule` | submodule | `register_scaffold_candidate_tri_branch` | 部分加群 | 子模 | 부분 가군 | 부분가군 |
| `CJK-PRE::lie_group` | Lie group | `register_scaffold_candidate_gap_backfill_required` | リー群 | GAP | 리 군 |
| `CJK-PRE::semisimple` | semisimple | `register_scaffold_candidate_tri_branch` | 半単純 | 半单 | 반단순 |
| `CJK-PRE::completely_reducible` | completely reducible | `register_scaffold_candidate_tri_branch` | 完全可約 | 完全可约 | 완전 가약 |
| `CJK-PRE::character` | character | `register_scaffold_candidate_tri_branch` | 指標 | 特征标 | 지표 |
| `CJK-PRE::irreducible_representation` | irreducible representation | `register_scaffold_candidate_tri_branch` | 既約表現 | 不可约表示 | 기약 표현 | 기약표현 |
| `CJK-PRE::group_ring_group_algebra` | group ring/group algebra | `register_scaffold_candidate_gap_backfill_required` | 群環／群代数 | GAP | 군환 | 군대수 |
| `CJK-PRE::representation` | representation | `register_scaffold_candidate_tri_branch` | 表現 | 表示 | 표현 |
| `CJK-PRE::representation_theory` | representation theory | `register_scaffold_candidate_tri_branch` | 表現論 | 表示论 | 표현론 | 표현 이론 |
| `CJK-PRE::artin_artinian` | Artin/Artinian | `register_scaffold_candidate_gap_backfill_required` | アルティン／アルティン的 | GAP | 아르틴 | 아르틴 환 |
| `CJK-PRE::artinian_artin` | Artinian/Artin | `register_scaffold_candidate_gap_backfill_required` | アルティン的／アルティン | GAP | 아르틴 | 아르틴 환 |
| `CJK-PRE::finite_dimensional` | finite-dimensional | `register_scaffold_candidate_tri_branch` | 有限次元 | 有限维 | 유한 차원 | 유한차원 |
| `CJK-PRE::finitely_generated` | finitely generated | `register_scaffold_candidate_tri_branch` | 有限生成 | 有限生成 | 유한 생성 | 유한생성 |
| `CJK-PRE::ideal` | ideal | `register_scaffold_candidate_tri_branch` | イデアル | 理想 | 아이디얼 | 이데알 |
| `CJK-PRE::semisimple_ring` | semisimple ring | `register_scaffold_candidate_gap_backfill_required` | 半単純環 | GAP | 반단순 환 |
| `CJK-PRE::principal_ideal` | principal ideal | `register_scaffold_candidate_tri_branch` | 主イデアル | 主理想 | 주 아이디얼 |
| `CJK-PRE::commutative_ring` | commutative ring | `register_scaffold_candidate_tri_branch` | 可換環 | 交换环 | 가환환 | 가환 환 |
| `CJK-PRE::quotient_ring` | quotient ring | `register_scaffold_candidate_tri_branch` | 商環 | 商环 | 몫환 | 상환 |
| `CJK-PRE::maximal_ideal` | maximal ideal | `register_scaffold_candidate_tri_branch` | 極大イデアル | 极大理想 | 극대 아이디얼 | 극대 이데알 |
| `CJK-PRE::ring` | ring | `register_scaffold_candidate_gap_backfill_required` | 環 | GAP | 환 | 환론 |
| `CJK-PRE::prime_ideal` | prime ideal | `register_scaffold_candidate_tri_branch` | 素イデアル | 素理想 | 소 아이디얼 |
| `CJK-PRE::algebra` | algebra | `register_scaffold_candidate_gap_backfill_required` | 代数 | GAP | 대수 | 대수학 |
| `CJK-PRE::basis_theorem` | basis theorem | `register_scaffold_candidate_tri_branch` | 基底定理 | 基定理 | 기저 정리 |
| `CJK-PRE::field` | field | `register_scaffold_candidate_tri_branch` | 体 | 域 | 체 | 체론 |
| `CJK-PRE::isomorphism` | isomorphism | `register_scaffold_candidate_tri_branch` | 同型 | 同构 | 동형 | 동형사상 |
| `CJK-PRE::homomorphism` | homomorphism | `register_scaffold_candidate_tri_branch` | 準同型 | 同态 | 준동형 | 준동형사상 |
| `CJK-PRE::automorphism` | automorphism | `register_scaffold_candidate_tri_branch` | 自己同型 | 自同构 | 자기동형 |
| `CJK-PRE::endomorphism` | endomorphism | `register_scaffold_candidate_tri_branch` | 自己準同型 | 自同态 | 자기준동형 |
| `CJK-PRE::norm` | norm | `register_scaffold_candidate_gap_backfill_required` | ノルム | GAP | 노름 | norm |
| `CJK-PRE::ring_of_integers` | ring of integers | `register_scaffold_candidate_gap_backfill_required` | 整数環 | GAP | 정수환 |
| `CJK-PRE::decomposition_of_primes` | decomposition of primes | `register_scaffold_candidate_gap_backfill_required` | 素イデアル分解 | GAP | 아이디얼의 소인수 분해 |
| `CJK-PRE::class_number` | class number | `register_scaffold_candidate_gap_backfill_required` | 類数 | GAP | 유수 |
| `CJK-PRE::right_module` | right module | `register_scaffold_candidate_gap_backfill_required` | GAP | 右模 | 오른쪽 가군 |
| `CJK-PRE::module_homomorphism` | module homomorphism | `register_scaffold_candidate_gap_backfill_required` | GAP | 模同态 | 가군 준동형 |
| `CJK-PRE::group_algebra` | group algebra | `register_scaffold_candidate_gap_backfill_required` | GAP | 群代数 | 군대수 |
| `CJK-PRE::ring` | ring | `register_scaffold_candidate_gap_backfill_required` | GAP | 环 | 환 | 환론 |
| `CJK-PRE::group` | group | `register_scaffold_candidate_gap_backfill_required` | GAP | 群 | 군 | 군론 |
| `CJK-PRE::division_ring` | division ring | `register_scaffold_candidate_gap_backfill_required` | GAP | 除环 | 나눗셈환 |
