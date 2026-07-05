# Noether CJK Draft Corpus Translation Slices

Generated UTC: `2026-07-04T04:23:38.648321+00:00`

Status: **draft/non-canonical/not native reviewed/not approved/not gate-promoted**.

These are draft Japanese and Simplified Chinese prose slices from the German baseline. They are not native reviewed, not approved, and not a reviewer packet.

## Inputs

- German baseline: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\tmp\zenodo_20836874_inspect\localcodex\Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624\tex\cum_de_R124plus_localcodex_current_candidate_20260624.tex`
- German baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Term sidecar: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-cjk-source-evidence-draft-lane\outputs\NOETHER_CJK_DRAFT_TRANSLATION_GLOSSARY_CONTEXT_SIDECAR_20260704.json`
- Term sidecar SHA256: `C2A41276F931268CC284460FA26157B682E3C92B678308A0C212F41B50FCD290`

## Coverage

- Corpus slices: `19`
- Exact blockers logged: `8`
- Lane row counts: `{"japanese": 41, "korean_addendum": 48, "simplified_chinese": 34}`
- Korean: addendum/source-discovery only; no Korean corpus prose in this artifact.

## Slice Index

| Slice | Anchor | Queue Terms | Flags |
| --- | --- | --- | --- |
| cjk-corpus-001-rational-function-bases | 4521-4588 — Körper und Systeme rationaler Funktionen; basis questions | algebra, basis theorem, field, finitely generated, basis, quotient field | Minimalbasis/Rationalbasis have several possible CJK registers; rendered descriptively rather than promoted as glossary entries. |
| cjk-corpus-002-integral-basis-number-field | 5658-5779 — integral elements and integrality bases over a number field | ring of integers, field, module, finite, integrality basis | The German passage says the totality of algebraic integers rather than a modern named ring of integers formula; glossary term is contextual. |
| cjk-corpus-003-finite-group-invariants | 5844-5876 — Der Endlichkeitssatz der Invarianten endlicher Gruppen | group, basis theorem, invariant, finite group, algebra | No native decision yet on translating Galoissche Resolvente; rendered descriptively. |
| cjk-corpus-004-hilbert-polar-reduction | 5960-6014 — Hilbert conjecture on invariants of arbitrarily many base forms | basis theorem, finitely generated, finite-dimensional, algebra, invariant | The finite-generation wording is conceptually close to Hilbert basis usage but not a direct Noetherian-ring assertion. |
| cjk-corpus-005-lie-variational-invariance | 8485-8644 — invariant variational problems and continuous groups in Lie's sense | Lie group, homomorphism, automorphism, invariant | Harish-Chandra has no direct baseline hit in the checked German source; kept in blocker ledger. |
| cjk-corpus-006-algebraic-functions-number-fields | 9132-9181 — algebraic functions, number fields, ideals, norms, class number | module, ideal, principal ideal, prime ideal, decomposition of primes, norm, class number, ring of integers | Decomposition of primes may be 素数の分解/素理想分解 depending on whether primes or prime ideals are foregrounded. |
| cjk-corpus-007-noncommutative-modules-intro | 10161-10285 — Moduln in nichtkommutativen Bereichen; introductory theory | module, submodule, simple module, semisimple, isomorphism, noncommutative ring | Chinese manual rows for module compounds remain manual-source-review rows despite this draft prose. |
| cjk-corpus-008-noncommutative-module-theorem-i | 10349-10363 — Theorem I on modules and decomposed residue groups | module, submodule, isomorphism, homomorphism, direct decomposition | Least common multiple of modules is rendered descriptively; native reviewer should decide compact term. |
| cjk-corpus-009-chain-condition-finite-module-basis | 14367-14401 — divisor chain condition and finite module bases | Noether/Noetherian, Noetherian, finitely generated, finite module basis, Artin/Artinian | No direct technical 'Noetherian' adjective occurs in this anchor; row rendering remains glossary-supported rather than corpus-promoted.; Artinian/Artin row is not resolved by proper-name Artin occurrences. |
| cjk-corpus-010-abstract-ideal-theory-integral-quantities | 14594-14635 — Abstrakter Aufbau der Idealtheorie; theory of integral quantities | ring, commutative ring, module, ideal, homomorphism, integral | Whether Bereich should be uniformly ring/domain is context-sensitive; left flagged for native/domain review. |
| cjk-corpus-011-splitting-fields-irrep | 16248-16318 — Brauer-Noether: minimal splitting fields of irreducible representations | irreducible representation, field, division ring, representation, finite-dimensional | Division ring terminology needs native/domain review in both languages for older German Körper usage. |
| cjk-corpus-012-groups-with-operators-modules | 16440-16616 — groups with operators; modules, submodules, bimodules | right module, submodule, module homomorphism, module, bimodule, representation | Tensor product remains without a direct German-baseline anchor in this pass. |
| cjk-corpus-013-representation-modules | 17591-17718 — Modul- und Darstellungstheorie; representations and representation modules | representation, representation theory, module, homomorphism, isomorphism, automorphism, endomorphism | Endomorphism appears via operator/action language, not as a standalone named term in the selected prose. |
| cjk-corpus-014-traces-characters-group-rings | 18074-18277 — traces, characters, discriminants, group ring | character, irreducible representation, semisimple, completely reducible, group ring/group algebra, class number, representation | Chinese group ring/group algebra distinction remains manual-review flagged.; Class number at this anchor is number of conjugacy classes/irreducible representations, not algebraic-number-theory class number. |
| cjk-corpus-015-galois-modules-artin-conductors | 18917-19008 — Galois modules, group rings, Artin L-series and conductors | module, group ring/group algebra, representation theory, character, Artin/Artinian | Artinian adjective remains unresolved; this slice only supports the proper-name Artin register. |
| cjk-corpus-016-right-modules-product-rings | 19072-19114 — right modules, double modules, product rings | right module, submodule, module homomorphism, homomorphism, isomorphism, module | Tensor product row remains source-shelf only; this anchor concerns product rings, not tensor products. |
| cjk-corpus-017-noncommutative-fields-automorphisms | 21774-22243 — Galois theory in noncommutative fields; automorphisms and representation modules | field, division ring, automorphism, isomorphism, irreducible representation, representation module | Older German Körper alternates between field and division ring; every occurrence needs context review. |
| cjk-corpus-018-quotient-rings-differents | 20226-20447 — different, quotient rings, direct product, defining ideals | quotient ring, commutative ring, principal ideal, ideal, ring, maximal ideal | Maximal ideal is not directly translated from this anchor; exact corpus hit not found in current pass. |
| cjk-corpus-019-crossed-products-norms | 23469-23573 — crossed representations, cyclic fields, norms, finite fields, quaternions | norm, field, division ring, representation, noncommutative field, quaternion | Crossed representation terminology needs domain/native review before any canonical use. |

## Draft Prose Slices

### cjk-corpus-001-rational-function-bases

- Slice family: `whole_lane_foundational_rows`
- Source anchor: `4521-4588` / Körper und Systeme rationaler Funktionen; basis questions
- Source summary: Defines rational function fields, rational bases, minimal bases, integrality bases, and explains the transfer from fields to arbitrary systems.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 有理関数体と基底問題**

ここで扱われる対象は、有理関数からなる体と、その中に含まれる有理関数または整有理関数の体系である。有限個の関数で体のすべての元を有理的に表せるとき、その有限系を有理基底と呼ぶ。
体の場合には有理基底の存在がまず示され、さらに代数的に独立な最小基底の問題へ進む。多項式からなる整域では整基底の問題が現れ、ヒルベルトの第十四問題に近い有限性の問いへ接続する。
任意の体系への移行では、その体系を含む最小の体を商体の一般化として用いる。これにより、個々の基底の特殊な選び方から来る分母や基本点の問題を、体系そのものの問題から切り離して扱える。

**Simplified Chinese: 有理函数域与基问题**

这里讨论的对象是由有理函数组成的域，以及其中由有理函数或整有理函数构成的系统。若有限个函数能够有理地表示该域的每一个元素，就称这个有限系统为有理基。
对于域，首先证明有理基的存在；随后讨论由代数无关函数构成的极小基问题。在由多项式组成的整域中，又出现整基问题，并与希尔伯特第十四问题附近的有限性问题相连。
推广到任意系统时，使用包含该系统的最小域，作为商域概念的推广。这样可以把由特殊基选择造成的分母和基本点困难，同系统本身的性质分开。

**Script/Codepoint/TeX Notes**

- Keep German Körper as Japanese 体 and Simplified Chinese 域 in commutative field passages.
- Use 整有理 in both languages as a draft register for ganze rationale; native review needed.

**Unresolved Flags**

- Minimalbasis/Rationalbasis have several possible CJK registers; rendered descriptively rather than promoted as glossary entries.

### cjk-corpus-002-integral-basis-number-field

- Slice family: `whole_lane_foundational_rows`
- Source anchor: `5658-5779` / integral elements and integrality bases over a number field
- Source summary: Treats an algebraic number field as coefficient domain, algebraic integers in it, and finite integrality bases for rational/integral function systems.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 代数的整数と整基底**

係数域を有限次の代数的数体とし、その中の代数的整数全体を基礎に置く。対象となる関数がこの係数域に関して整であるとき、それらを有限個の基礎的な整元によって表す問題が現れる。
ここでいう「整数環」は、文脈上、数体に含まれる代数的整数全体を指す。整基底は、任意の整関数を係数域からの係数を用いた整有理結合として表すための有限な支えである。

**Simplified Chinese: 代数整数与整基**

取一个有限代数数域作为系数域，并以其中全部代数整数为基础。若所研究的函数相对于这个系数域是整的，就出现用有限个基本整元表示它们的问题。
这里的“整数环”在语境上指该数域中全部代数整数的集合。整基是一个有限支架，使任意整函数都能用系数域中的系数作整有理组合来表示。

**Script/Codepoint/TeX Notes**

- Japanese 整数環 and Chinese 整数环 are safe only when the whole ring of algebraic integers is meant; this slice uses a descriptive phrase first.
- Avoid Traditional Chinese 整數環 in zh-Hans output.

**Unresolved Flags**

- The German passage says the totality of algebraic integers rather than a modern named ring of integers formula; glossary term is contextual.

### cjk-corpus-003-finite-group-invariants

- Slice family: `whole_lane_invariant_theory`
- Source anchor: `5844-5876` / Der Endlichkeitssatz der Invarianten endlicher Gruppen
- Source summary: Gives an elementary finiteness proof for invariants of finite linear groups using symmetric functions and Galois resolvent coefficients.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 有限群の不変式の有限性**

有限個の線形変換からなる群について、その絶対不変式が有限個の基本的な不変式から整有理に表されることを示す。通常の証明はヒルベルトの加群基底定理に依拠するが、ここでは対称関数の理論だけを用いて、完全な系を具体的に与える。
任意の不変式を群の各変換で動かした変数列に評価すると、それらの列に関する対称関数が得られる。したがって、その不変式はガロア分解式の係数によって整有理に表され、これらの係数が完全な不変式系を成す。

**Simplified Chinese: 有限群不变量的有限性**

对于由有限个线性变换组成的群，证明其绝对不变量都能由有限个基本不变量作整有理表示。通常证明依靠希尔伯特模基定理；这里则只用对称函数理论，并实际给出一个完全系统。
把任意不变量在群的各个变换后的变量列上取值，就得到这些列的对称函数。因此该不变量可由伽罗瓦预解式的系数作整有理表示，而这些系数构成一个完全的不变量系统。

**Script/Codepoint/TeX Notes**

- Japanese 群 and Chinese 群 are script-stable; leave formulas such as G_{...}(x) untouched in TeX.
- 整有理 remains a flagged historical register in both CJK drafts.

**Unresolved Flags**

- No native decision yet on translating Galoissche Resolvente; rendered descriptively.

### cjk-corpus-004-hilbert-polar-reduction

- Slice family: `whole_lane_invariant_theory`
- Source anchor: `5960-6014` / Hilbert conjecture on invariants of arbitrarily many base forms
- Source summary: Proves Hilbert's conjecture that invariants of systems with arbitrarily many base forms are generated by finitely many invariants and their polar derivatives.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 極化過程によるヒルベルトの予想の還元**

ヒルベルトは、任意個の基本形式からなる体系の不変式が、有限個の不変式とそれらに極化過程を施して得られる式によって整有理に表されると予想した。ここでは、その主張を還元定理から導く。
行数が変数の数を超える形式は、固定された行だけを含む形式の極化の和として表せる。したがって任意の同時不変式は、まず有限個の基本不変式の積へ還元され、さらに極化過程を施すことで求める整有理表示に到達する。

**Simplified Chinese: 用极化过程归约希尔伯特猜想**

希尔伯特猜想，任意多个基本形式所成系统的不变量，都能由有限个不变量以及对它们施加极化过程所得的式子作整有理表示。这里把这一命题归结为一个归约定理。
当形式的行数超过变量数时，它可以写成只含固定若干行的形式的极化之和。因此任意同时不变量先归约为有限个基本不变量的乘积，再施加极化过程，便得到所需的整有理表示。

**Script/Codepoint/TeX Notes**

- Polarprozess is drafted as 極化過程 / 极化过程; do not normalize to a modern differential-operator term without review.

**Unresolved Flags**

- The finite-generation wording is conceptually close to Hilbert basis usage but not a direct Noetherian-ring assertion.

### cjk-corpus-005-lie-variational-invariance

- Slice family: `whole_lane_row_family_expansion`
- Source anchor: `8485-8644` / invariant variational problems and continuous groups in Lie's sense
- Source summary: Introduces variational problems admitting continuous transformation groups and derives the Lie differential equations for invariant integrals.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: リーの意味での連続群と不変積分**

変分問題がリーの意味での連続変換群を許すとき、その不変性は対応する微分方程式に反映される。ここでは、変換群を、逆変換と合成に対して閉じた変換の体系として扱う。
不変積分に対して群の無限小変換を適用すると、被積分式の恒等的な消滅条件が得られる。この条件が、積分の不変性を表すリー型の微分方程式として書き直される。

**Simplified Chinese: 李意义下的连续群与不变积分**

当变分问题允许李意义下的连续变换群时，其不变性会反映在相应的微分方程中。这里把变换群看作对逆变换和复合封闭的变换系统。
对不变积分施加群的无穷小变换，会得到被积函数恒等消失的条件。这个条件可改写为表达积分不变性的李型微分方程。

**Script/Codepoint/TeX Notes**

- Japanese keeps リー群 in katakana; Simplified Chinese uses 李群.
- Do not conflate transformation group with representation-theory representation terms in this slice.

**Unresolved Flags**

- Harish-Chandra has no direct baseline hit in the checked German source; kept in blocker ledger.

### cjk-corpus-006-algebraic-functions-number-fields

- Slice family: `whole_lane_number_theory`
- Source anchor: `9132-9181` / algebraic functions, number fields, ideals, norms, class number
- Source summary: Compares algebraic number fields and one-variable algebraic function fields through modules, ideals, principal ideals, prime ideal factorization, discriminants, norms, and class number phenomena.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 数体・関数体におけるイデアルとノルム**

有限個の基底で係数環上線形に表せる加群を有限加群と呼び、その元が係数環自身に属する場合にはイデアルと呼ぶ。特に一つの基底元から生じるイデアルが主イデアルである。
代数的数体と一変数の代数関数体では、すべてのイデアルが素イデアルの冪積に一意に分解されるという基本定理を共通に扱える。分岐イデアルや差別はノルムを通じて記述され、素イデアル分解と密接に結びつく。
一方、関数体では定数が無限に存在するため、イデアル類数に関する問いは数体の場合とは異なる形になる。この差異が、類数・類体・点の算術的定義の役割を分ける。

**Simplified Chinese: 数域和函数域中的理想与范数**

若一个模能由有限个基元在系数环上线性表示，就称为有限模；若它的元素本身属于系数环，则称为该系数环中的理想。特别地，由一个基元生成的理想就是主理想。
在代数数域和一元代数函数域中，可以共同处理基本定理：每个理想唯一分解为素理想的幂的乘积。分歧理想和判别式通过范数来描述，并与素理想分解紧密相连。
另一方面，函数域中存在无限多个常数，因此关于理想类数的问题与数域情形不同。这一区别分开了类数、类域以及点的算术定义所起的作用。

**Script/Codepoint/TeX Notes**

- Japanese uses 類数; Simplified Chinese uses 类数. Keep these distinct from 'number of conjugacy classes' unless context says representation classes.
- Chinese 范数 is used for number-theory Norm in this slice; not 特征/范畴 usage.

**Unresolved Flags**

- Decomposition of primes may be 素数の分解/素理想分解 depending on whether primes or prime ideals are foregrounded.

### cjk-corpus-007-noncommutative-modules-intro

- Slice family: `whole_lane_module_theory`
- Source anchor: `10161-10285` / Moduln in nichtkommutativen Bereichen; introductory theory
- Source summary: Introduces modules whose elements are polynomials with noncommutative multiplication, residue classes, residue groups, least common multiples, and decomposition.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 非可換領域における加群と剰余類**

非可換な乗法をもつ多項式を元とする加群の理論を構成する。可換の場合と異なり、剰余類同士の積は一般には定義できないので、剰余類の加法と多項式による作用からなる剰余群を中心に据える。
互いに素な加群の最小公倍加群としての分解は、剰余群の直和分解に対応する。したがって、分解の一意性や既約性の問題は、剰余群の同型および成分の作用素同型の問題として扱われる。

**Simplified Chinese: 非交换区域中的模与剩余类**

这里建立一种模理论，其元素是乘法非交换的多项式。不同于交换情形，剩余类之间一般不能相乘，因此以剩余类的加法以及多项式对剩余类的作用所形成的剩余群为中心。
把一个模表示为两个互素模的最小公倍模，对应于把剩余群分解为直和。因此，分解的唯一性和不可约性问题转化为剩余群同构以及各成分的算子同构问题。

**Script/Codepoint/TeX Notes**

- German Moduln is rendered Japanese 加群 and Simplified Chinese 模.
- Residue class/group terms are descriptive drafts; not promoted glossary entries.

**Unresolved Flags**

- Chinese manual rows for module compounds remain manual-source-review rows despite this draft prose.

### cjk-corpus-008-noncommutative-module-theorem-i

- Slice family: `whole_lane_module_theory`
- Source anchor: `10349-10363` / Theorem I on modules and decomposed residue groups
- Source summary: States the equivalence between writing a module as least common multiple of two coprime proper divisors and decomposing its residue group into two corresponding subgroups.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 剰余群分解としての加群分解**

関係式から得られる剰余類の多項式を用いて、加群を二つの互いに素な真の約加群の最小公倍加群として表すことを考える。この表現は、剰余群を二つの部分群の和に一意に分解することと同値である。
二つの部分群はそれぞれ対応する約加群の剰余群と同型である。したがって、加群の可約性は、剰余群がそのような二つの部分群へ分解できるかどうかとして読める。

**Simplified Chinese: 作为剩余群分解的模分解**

利用由关系式得到的剩余类多项式，考虑把一个模写成两个互素真因子模的最小公倍模。这种表示与把剩余群唯一分解为两个子群之和等价。
这两个子群分别同构于相应因子模的剩余群。因此，模的可约性可以理解为其剩余群能否分解成这样的两个子群。

**Script/Codepoint/TeX Notes**

- Chinese 子群 is used for subgroup, but 子模 remains reserved for submodule.
- Japanese 部分群 vs 部分加群 distinction should be preserved near formulas.

**Unresolved Flags**

- Least common multiple of modules is rendered descriptively; native reviewer should decide compact term.

### cjk-corpus-009-chain-condition-finite-module-basis

- Slice family: `whole_lane_noetherian_finiteness`
- Source anchor: `14367-14401` / divisor chain condition and finite module bases
- Source summary: Uses a divisor-chain condition, finite extensions, integrality, and finite module bases; cites Artin and van der Waerden for a preceding note.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 鎖条件と有限加群基底**

有限性判定は、有理基底の存在と、有限拡大の整元へ移るとき除数鎖条件が保たれるという事実に基づく。ここでの鎖条件は、後のネーター的条件に近い役割を果たすが、本文ではその名称では述べられていない。
多項式環に同型な環では、イデアル全体について鎖条件が成り立ち、有限拡大へ移ると有限な加群基底が得られる。したがって、対象となる部分環も、上位の環に含まれる有限な加群として扱われる。

**Simplified Chinese: 链条件与有限模基**

这个有限性判据基于有理基的存在，以及在过渡到有限扩张中的整元时除子链条件仍然保持的事实。这里的链条件与后来的诺特条件作用相近，但正文并未用该名称表述。
在同构于多项式环的环中，所有理想满足链条件；过渡到有限扩张后得到有限模基。因此，所讨论的子环也可作为包含在上层环中的有限模来处理。

**Script/Codepoint/TeX Notes**

- Noetherian is not inserted as an explicit translation where the German only says Teilerkettensatz.
- Artin in this slice is a proper name citation, not Artinian; keep アルティン/阿廷 separate from Artinian conditions.

**Unresolved Flags**

- No direct technical 'Noetherian' adjective occurs in this anchor; row rendering remains glossary-supported rather than corpus-promoted.
- Artinian/Artin row is not resolved by proper-name Artin occurrences.

### cjk-corpus-010-abstract-ideal-theory-integral-quantities

- Slice family: `whole_lane_ring_ideal_theory`
- Source anchor: `14594-14635` / Abstrakter Aufbau der Idealtheorie; theory of integral quantities
- Source summary: Defines an R-module inside a ring-like domain T with unit and no zero divisors, then introduces divisibility via congruence modulo another module.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 抽象的イデアル論における加群の定義**

零因子をもたず単位元をもつ領域を固定し、その中の部分環を基準環とする。この基準環に関して、二つの元の差を含み、また任意の基準環の元による積を含むような元の体系を加群と呼ぶ。
この定義により、イデアル論の言葉を抽象的に扱える。ある加群が別の加群を法として零に合同であるという形で、加群間の割り切れ関係を記述する。

**Simplified Chinese: 抽象理想论中的模定义**

固定一个无零因子且有单位元的区域，并取其中一个子环作为基准环。相对于这个基准环，若一个元素系统含有任意两个元素的差，并且含有任意基准环元素与其元素的乘积，就称它为一个模。
借助这个定义，可以抽象地表述理想论。一个模相对于另一个模同余于零的说法，用来描述模之间的可除关系。

**Script/Codepoint/TeX Notes**

- Japanese 環 and Chinese 环 are used for Ring/Bereich only when the algebraic structure is ring-like; Bereich is otherwise left contextual.
- Chinese 同余于零 is preferred over a literal '模 N 为零' where prose clarity matters.

**Unresolved Flags**

- Whether Bereich should be uniformly ring/domain is context-sensitive; left flagged for native/domain review.

### cjk-corpus-011-splitting-fields-irrep

- Slice family: `whole_lane_representation_theory`
- Source anchor: `16248-16318` / Brauer-Noether: minimal splitting fields of irreducible representations
- Source summary: Characterizes minimal splitting fields for irreducible representations using associated noncommutative fields; uses quaternion fields as an example.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 既約表現の最小分解体**

有限群の既約表現が、ある基礎体の上では絶対既約成分へ分解しない場合、どの拡大体で分解するかが問題になる。最小次数の分解体は、対応する非可換体によって特徴づけられる。
一般の分解体は、行列環との直接積を用いて記述される。四元数体の例では、冪零でない冪等元やノルムの条件が、絶対単純なイデアルへの分解と結びつく。

**Simplified Chinese: 不可约表示的最小分裂域**

当有限群的不可约表示在给定基域上尚未分解为绝对不可约成分时，需要问在哪些扩域上会发生分解。最低次数的分裂域可由相应的非交换除环来刻画。
一般分裂域则通过与矩阵环的直接积来描述。在四元数除环的例子中，非平凡幂等元以及范数条件同分解为绝对单理想相联系。

**Script/Codepoint/TeX Notes**

- German nichtkommutativer Körper is historically 'noncommutative field'; Japanese 非可換体 and Chinese 非交换除环 are flagged as register-sensitive.
- Simplified Chinese uses 不可约表示, not 既约表示.

**Unresolved Flags**

- Division ring terminology needs native/domain review in both languages for older German Körper usage.

### cjk-corpus-012-groups-with-operators-modules

- Slice family: `whole_lane_module_representation_bridge`
- Source anchor: `16440-16616` / groups with operators; modules, submodules, bimodules
- Source summary: Relates groups with operators to ideals and modules, defines admissible subgroups as submodules, and introduces left, right, and double modules.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 作用素付き群から加群・双加群へ**

作用素付き群の枠組みには、加法群として見たイデアルや加群が含まれる。環の元による乗法を作用素と見れば、表現は表現加群によって生じ、同じ作用素同型類に属する表現加群は同じ表現を与える。
加群の許容部分群は部分加群と呼ばれる。さらに、左から一つの環、右から別の環が作用し、結合法則が両側の作用を結びつけるとき、その加群は双加群として扱われる。

**Simplified Chinese: 从带算子群到模与双模**

带算子群的框架包括把理想和模看作加法群的情形。若把环元素的乘法看作算子，则表示由表示模产生；同属一个算子同构类的表示模给出同一个表示。
模中的容许子群称为子模。进一步，若一个环从左作用、另一个环从右作用，并且结合律把两侧作用联系起来，这样的模就作为双模处理。

**Script/Codepoint/TeX Notes**

- Chinese right module row uses 右模 only where a right action is explicitly named; otherwise 模 is enough.
- Japanese 双加群 is used for Doppelmodul, but 双加群/両側加群 should be reviewed.

**Unresolved Flags**

- Tensor product remains without a direct German-baseline anchor in this pass.

### cjk-corpus-013-representation-modules

- Slice family: `whole_lane_representation_theory`
- Source anchor: `17591-17718` / Modul- und Darstellungstheorie; representations and representation modules
- Source summary: Defines a representation of a ring by matrices over a field, defines representation modules as bimodules, and relates basis change to equivalent matrices and operator-isomorphic modules.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 表現と表現加群**

環の次数 n の表現とは、その環を体上の n 次正方行列環へ準同型に写すことである。表現加群は、左から環が作用し、右から体が作用する双加群で、有限個の一元生成右加群の直和として表される。
任意の表現加群は、環の元の左作用を基底に関して行列で表すことにより表現を与える。逆に、行列表現が与えられれば、形式的な線形形式の加群を用いて表現加群を構成できる。
基底を取り替えると行列は相似変換で変わるだけなので、表現加群は一つの表現類を定める。作用素同型な表現加群は同じ表現類に対応する。

**Simplified Chinese: 表示与表示模**

环的 n 次表示，是把该环同态地映到某个域上的 n 阶方阵环中。表示模是一个双模：环从左作用，域从右作用，并且它可写成有限多个一元生成右模的直和。
任一表示模通过把环元素的左作用按基表示为矩阵而给出一个表示。反过来，给定一个矩阵表示，也可用形式线性型组成的模来构造相应的表示模。
改变基只会使矩阵发生相似变换，所以一个表示模确定一个表示类。算子同构的表示模对应同一个表示类。

**Script/Codepoint/TeX Notes**

- Chinese 表示 is representation-theory usage; avoid 表达 in this slice.
- Japanese 準同型/同型/自己同型/自己準同型 need map-vs-class disambiguation in reviewer pass.

**Unresolved Flags**

- Endomorphism appears via operator/action language, not as a standalone named term in the selected prose.

### cjk-corpus-014-traces-characters-group-rings

- Slice family: `whole_lane_representation_theory`
- Source anchor: `18074-18277` / traces, characters, discriminants, group ring
- Source summary: Defines traces and characters of representations, uses trace invariance under equivalence, relates discriminants to radicals, and treats group rings of finite groups.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 跡・指標・群環**

表現における跡は、対応する行列の跡として定義される。同値な表現は同じ跡をもち、可約な表現では跡が組成因子の跡の和として分解される。
根基を除いた体系の絶対既約表現における跡が指標である。中心の準同型と指標は互いに結びつき、跡の値は表現類を決定する。
有限群の群環では、体の標数が群の位数を割らない場合、正則表現の跡から判別式が零でないことが分かる。したがって根基は消え、群環は半単純な振る舞いを示す。

**Simplified Chinese: 迹、特征标与群代数**

一个表示中的迹定义为相应矩阵的迹。等价表示具有相同的迹；可约表示中的迹可分解为组成因子的迹之和。
去掉根基后的系统在绝对不可约表示中的迹就是特征标。中心同态与特征标相联系，而迹的取值能够决定表示类。
对于有限群的群代数，若基域的特征不整除群的阶，则由正则表示的迹可知判别式非零。因此根基消失，群代数表现为半单。

**Script/Codepoint/TeX Notes**

- Japanese 指標 and Chinese 特征标 are representation-character terms; do not use 性格/字符.
- German Gruppenring maps to Japanese 群環; Chinese queue has 群代数, but 群环 may be needed if strict group-ring wording is required.

**Unresolved Flags**

- Chinese group ring/group algebra distinction remains manual-review flagged.
- Class number at this anchor is number of conjugacy classes/irreducible representations, not algebraic-number-theory class number.

### cjk-corpus-015-galois-modules-artin-conductors

- Slice family: `whole_lane_number_representation_bridge`
- Source anchor: `18917-19008` / Galois modules, group rings, Artin L-series and conductors
- Source summary: Describes Galois fields as Galois modules, operator isomorphism with group rings/group algebras, and links Artin L-series and conductors with number theory and representation theory.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: ガロア加群と群環**

ガロア体を基礎体上の加群と見なし、ガロア群の置換を作用素として許すと、体と群環とのあいだに作用素同型が生じる。体の線形形式と群環の線形形式が対応し、体での置換は群環での乗法に対応する。
この見方は、ガロア理論と表現論を結ぶ。さらに、一般の群指標から作られるアルティンの L 関数と導手は、数論と表現論の最初期の接続点として位置づけられる。

**Simplified Chinese: 伽罗瓦模与群代数**

把伽罗瓦域看作基域上的模，并允许伽罗瓦群的置换作为算子，就得到域与群代数之间的算子同构。域中的线性型对应于群代数中的线性型，而域中的置换对应于群代数中的乘法。
这种观点把伽罗瓦理论同表示论联系起来。进一步，由一般群特征标构造的阿廷 L 函数和导子，被看作数论与表示论之间较早的连接点。

**Script/Codepoint/TeX Notes**

- Artin is rendered アルティン / 阿廷 as a proper name; do not infer Artinian here.
- Chinese 群代数 is used because the passage explicitly glosses Gruppenring/Gruppenalgebra together.

**Unresolved Flags**

- Artinian adjective remains unresolved; this slice only supports the proper-name Artin register.

### cjk-corpus-016-right-modules-product-rings

- Slice family: `whole_lane_module_theory`
- Source anchor: `19072-19114` / right modules, double modules, product rings
- Source summary: Defines right modules over rings, left modules, double modules, and the transition from right double modules to one-sided modules over product rings.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 右加群・双加群・積環**

環上の右加群とは、加法的アーベル群に環の元を右作用素として作用させ、結合法則と分配法則を満たすものである。左加群も同様に定義される。
同じ群が二つの環の右加群になり、二つの作用が互いに可換に振る舞うとき、それを双加群と呼ぶ。二つの環を含む積環が存在すれば、この双加群は積環上の一側加群として見直すことができる。

**Simplified Chinese: 右模、双模与积环**

环上的右模，是把一个加法阿贝尔群配上该环元素作为右算子，并满足结合律和分配律的结构。左模也以相应方式定义。
若同一个群同时是两个环上的右模，并且两种作用相互可交换，就称为双模。若存在包含这两个环的积环，则可把这个双模重新看作积环上的单侧模。

**Script/Codepoint/TeX Notes**

- Chinese 右模 is exact for Rechtsmodul in this anchor; Japanese uses 右加群.
- Produktring is not tensor product; do not translate as テンソル積/张量积 in this draft.

**Unresolved Flags**

- Tensor product row remains source-shelf only; this anchor concerns product rings, not tensor products.

### cjk-corpus-017-noncommutative-fields-automorphisms

- Slice family: `whole_lane_field_theory`
- Source anchor: `21774-22243` / Galois theory in noncommutative fields; automorphisms and representation modules
- Source summary: Defines invariant fields of automorphism groups, inner automorphisms, centers of noncommutative fields, and uses representation modules in the Galois theory of noncommutative fields.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 非可換体のガロア理論**

体 K とその自己同型群が与えられると、群のすべての自己同型で不変な元全体は部分体を成す。非可換体では、零でない元による共役から内的自己同型が得られ、その全体の不変体は中心になる。
中間体と自己同型群の対応を、可換体の場合に似た形で扱うために、表現加群と単純左イデアルが用いられる。非可換体における既約表現類の一意性が、この対応の構造を支える。

**Simplified Chinese: 非交换除环的伽罗瓦理论**

给定一个除环 K 及其自同构群，在群中所有自同构下保持不变的元素组成一个子域。在非交换除环中，由非零元素共轭得到内自同构；所有内自同构的不变域就是中心。
为了以类似交换域的方式处理子域与自同构群之间的对应，需要使用表示模和单左理想。非交换情形下不可约表示类的唯一性支撑了这种对应结构。

**Script/Codepoint/TeX Notes**

- Japanese 非可換体 versus 斜体 remains a style decision; draft keeps the historically transparent 非可換体.
- Simplified Chinese uses 除环 for division ring, but 子域 for commutative subfields.

**Unresolved Flags**

- Older German Körper alternates between field and division ring; every occurrence needs context review.

### cjk-corpus-018-quotient-rings-differents

- Slice family: `whole_lane_ring_ideal_theory`
- Source anchor: `20226-20447` / different, quotient rings, direct product, defining ideals
- Source summary: Defines the different through quotient/difference constructions, discusses commutative rings, residue class rings, defining ideals, and principal ideals in a structural treatment.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 商環・定義イデアル・ディファレント**

可換環を基礎に、同型な二つの拡大を直接積の中で比較し、対応する元の差から差イデアルを作る。零イデアルをこの差イデアルで割った商を用いて、ディファレントを不変的に定義する。
生成元系に関する関係式全体は定義イデアルを成し、剰余類環として環を表す。定義イデアルが主イデアルである場合には、基礎多項式による定義方程式が得られる。

**Simplified Chinese: 商环、定义理想与不同**

在交换环的基础上，把两个同构扩张放在直接积中比较，并由对应元素的差生成差理想。再用零理想对这个差理想作商，从而以不变量方式定义不同。
相对于一组生成元，所有关系式组成一个定义理想，并把环表示为剩余类环。若定义理想是主理想，就得到由基多项式给出的定义方程。

**Script/Codepoint/TeX Notes**

- Restklassenring is rendered 商環/剩余类环 depending on syntax; Chinese 商环 is reserved for quotient ring row.
- No exact maximal ideal anchor appears here; maximal ideal remains source-shelf/glossary-supported only.

**Unresolved Flags**

- Maximal ideal is not directly translated from this anchor; exact corpus hit not found in current pass.

### cjk-corpus-019-crossed-products-norms

- Slice family: `whole_lane_number_representation_bridge`
- Source anchor: `23469-23573` / crossed representations, cyclic fields, norms, finite fields, quaternions
- Source summary: Interprets norm theorems through crossed products and normalized crossed representations, then applies them to finite fields and quaternion extensions over the reals.
- Status: draft/non-canonical/not native reviewed/not approved/not gate-promoted

**Japanese: 交差積とノルム定理**

巡回体を用いた交差積を考えると、固定した分解体に属する類の群を、基礎体の乗法群をノルム全体で割った群として解釈できる。この証明は、正規化された交差表現と因子系の補題に基づく。
有限体ではすべての元が拡大体からのノルムとして現れるため、中心を同じくする非可換体は存在しないことが従う。実数体上では正の数が複素数体からのノルムとなり、残る非自明な類が四元数を与える。

**Simplified Chinese: 交叉积与范数定理**

考虑由循环域得到的交叉积时，具有固定分裂域的类群可解释为基域乘法群模去全部范数所得的群。证明依赖于规范化的交叉表示以及关于因子系统的引理。
在有限域情形，每个基域元素都是扩域元素的范数，因此不存在具有同一中心的非交换除环。实数域上，正数是复数域的范数，剩下的非平凡类给出四元数除环。

**Script/Codepoint/TeX Notes**

- Japanese 交差表現 and Chinese 交叉表示 are provisional for verschränkte Darstellung.
- Quaternion terms are contextual and not part of the current row glossary.

**Unresolved Flags**

- Crossed representation terminology needs domain/native review before any canonical use.

## Blocker Ledger

### cjk-blocker-harish-chandra

- Scope: Japanese representation-theory row term Harish-Chandra
- Evidence: Targeted German-baseline search for Harish found no hit.
- Decision: Keep glossary/source-shelf rendering only; no corpus prose translation inserted.

### cjk-blocker-localization

- Scope: Japanese and Simplified Chinese localization rows
- Evidence: Targeted German-baseline search for Lokalis/localization terms found no hit.
- Decision: Keep 局所化/局部化 in row sidecar only; do not fabricate a corpus segment.

### cjk-blocker-tensor-product

- Scope: Japanese tensor product and Simplified Chinese tensor product manual row
- Evidence: German baseline search found product/direct-product/product-ring contexts, but no Tensorprodukt anchor in selected baseline.
- Decision: Do not translate direct product/product ring as tensor product; leave tensor product row source-shelf supported only.

### cjk-blocker-maximal-ideal

- Scope: Japanese and Simplified Chinese maximal ideal rows
- Evidence: Search found maximal commutative subfields but no reliable maximal-ideal source anchor in this pass.
- Decision: Keep 極大イデアル/极大理想 glossary row; no corpus promotion.

### cjk-blocker-artinian

- Scope: Japanese Artin/Artinian rows
- Evidence: Baseline contains proper-name Artin and minimal-condition passages, but no direct Artinian-ring/module wording in selected anchors.
- Decision: Translate proper-name Artin only in prose; keep Artinian adjective flagged.

### cjk-blocker-course-scope-terms

- Scope: Simplified Chinese abstract algebra / modern algebra rows
- Evidence: These are source-shelf/course-register terms, not direct German corpus prose terms in the selected baseline anchors.
- Decision: Keep 抽象代数/近世代数 or 现代代数 in glossary sidecar; no corpus segment fabricated.

### cjk-blocker-korean-corpus

- Scope: Korean addendum
- Evidence: Korean work in this lane is source-discovery/crosswalk only; no row-level German-to-Korean corpus queue was established.
- Decision: No Korean corpus prose translation in this artifact; keep Korean in prior addendum/source-discovery sidecar.

### cjk-blocker-full-line-corpus-map

- Scope: Full Noether baseline line-by-line corpus translation
- Evidence: The active queue provides term/context rows and source shelves, not a complete approved chunk map for the entire 24k-line cumulative German baseline.
- Decision: This artifact completes row-triggered corpus-slice drafting for anchored CJK row families and records exact blockers for unanchored terms; full line-by-line translation requires a separate chunking ledger.

## Next Gates

- Resolve unanchored row terms one by one with local evidence first, web only when local evidence is insufficient.
- Create a full German-baseline chunk map before any claim of complete line-by-line corpus translation.
- Run native/domain review before promoting any Japanese or Simplified Chinese rendering.
- Perform TeX/PDF CJK rendering checks before any reviewer packet is assembled.
- Leave Korean as addendum/source-discovery unless a row-level Korean corpus queue is explicitly opened.
- Keep Git push/package coordination outside this lane.
