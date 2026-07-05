# Noether CJK Draft Corpus Translation Slices: Continuation 09

Generated UTC: `2026-07-04T06:17:49.110011+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical sidecar only. Not native reviewed. Not approved. Not gate-promoted.

Baseline: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\tmp\zenodo_20836874_inspect\localcodex\Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624\tex\cum_de_R124plus_localcodex_current_candidate_20260624.tex`

Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`

## Review Boundaries

- `native_review_status`: `not_native_reviewed`
- `canonical_approval_status`: `not_approved`
- `gate_promotion_status`: `not_gate_promoted`
- `reviewer_packet_population_performed`: `False`
- `git_push_performed`: `False`
- `korean_corpus_prose_added`: `False`

## Retained Blockers

- tensor product: no German Tensorprodukt anchor; product-ring/Produktring material at 19115-19134 is not tensor-product evidence
- localization: Quotientenring candidates at 16223-16225 and 18467 but no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: source-shelf/course-register evidence only
- modern algebra: Moderne Algebra remains bibliographic only; Nichtkommutative Algebra at Paper 40 title is not a modern-algebra row anchor

## cjk-continuation-09-001-paper40-overview-splitting-fields-noncommutative-method

Anchor: German baseline lines `19009-19022`; 40. Nichtkommutative Algebra: overview after introduction.

Source summary: Explains the noncommutative route to structure theorems for matrix rings over division algebras, reciprocal representations, splitting fields, and crossed products.

Japanese title: 非可換的方法による分解体と表現論の概観

Paper 40 の導入では、可換代数の主定理が Galois 理論の中に含まれ、その前提として一次因子を切り離す体と全分解体の理論がある、と置かれる。Noether は対応する部分を非可換、特に超複素の場合に展開し、非可換体での表現を用いる。

ここでは、各部分環がその非可換体による表現、または反対同型な体による反表現を与える、という観察から、非可換体上の行列環の構造定理が導かれる。この反対同型な体は、可換の場合の最小の一次因子切離し体や分解体に対応する最初の類似物として扱われる。

同じ枠組みから、非可換体の Galois 理論、Brauer 群における逆類、可換な分解体の扱い、さらに交差積と因子系の数論的応用が接続される。ここでの「非可換代数」は論文題名由来であり、modern algebra blocker を解消するものではない。

Simplified Chinese title: 用非交换方法概观分裂域与表示论

Paper 40 的导言把交换代数的主定理置于 Galois 理论中，而在其前面有一次因子分出域和完全分裂域的理论。Noether 要把相应部分发展到非交换，尤其是超复情形，并使用非交换除环中的表示。

这里从一个观察出发：每个子环都给出由该非交换除环形成的表示，或者由反同构除环形成的反表示。由此可得到非交换除环上矩阵环的结构定理；这个反同构除环被看作交换情形中最小一次因子分出域和分裂域的第一个类似物。

同一框架还连接到非交换除环的 Galois 理论、Brauer 群中的逆类、交换分裂域的处理，以及交叉积和因子系统的数论应用。这里的“非交换代数”来自论文题名，并不解除 modern algebra 阻塞项。

Script/codepoint and TeX/PDF notes:

- Abspaltungskörper is rendered descriptively as 一次因子を切り離す体 / 一次因子分出域, not as an approved term.
- Körper in noncommutative context follows lane convention: 非可換体 in Japanese and 非交换除环 in Simplified Chinese.
- Crossed product/factor system follows 交差積・因子系 / 交叉积・因子系统 from Continuation 08.

Unresolved flags:

- Reciprocal representation and Abspaltungskörper wording require review.
- Modern algebra remains bibliographic only; this title is not a blocker-closing anchor.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-09-002-automorphism-rings-operators-homomorphisms

Anchor: German baseline lines `19024-19071`; §1 Automorphismen, Moduln und Doppelmoduln: multiplicative and operator-homomorphic maps.

Source summary: Sets up automorphism domains of groups with operators, multiplicative homomorphisms, reciprocal homomorphisms for left operators, and operator-homomorphic maps.

Japanese title: 作用素付き群と自己同型環

§1 は、表現加群に基づく表現論の準備として、作用素を持つ可換群の自己同型環を扱う。まず作用素を持たない群 \(\frG\) について、\(\frG\) から自身への準同型全体を絶対自己同型領域 \(\frA\) とし、積 \(\sigma\tau\) を \(g(\sigma\tau)=(g\sigma)\tau\) で定める。

次に、記号 \(O,H,\ldots\) からなる作用素領域 \(\frB\) が与えられ、各 \(gO\) が \(\frG\) の自己準同型を生む場合を考える。\(\frB\) から自己同型領域への写像が乗法的準同型となるのは、\(g(OH)=(gO)H\) という結合関係が満たされるとき、かつそのときに限られる。

左作用素の場合には、読む向きの反転によって反準同型が現れる。さらに作用素付き群の作用素準同型は、\((gO)\sigma=(g\sigma)O\)、または左作用素なら \((Og)\sigma=O(g\sigma)\) で定義され、二つの作用素領域が互いに自己同型を誘導する条件は、可換的な結合関係で表される。

Simplified Chinese title: 带算子群与自同构环

§1 为基于表示模的表示论作准备，讨论带算子的阿贝尔群的自同构环。先从没有算子的群 \(\frG\) 出发，把 \(\frG\) 到自身的同态全体记为绝对自同构域 \(\frA\)，并用 \(g(\sigma\tau)=(g\sigma)\tau\) 定义乘积 \(\sigma\tau\)。

随后考虑由符号 \(O,H,\ldots\) 组成的算子域 \(\frB\)，每个 \(gO\) 都给出 \(\frG\) 的自同态。由 \(\frB\) 到自同构域相应部分的映射为乘法同态，当且仅当满足结合关系 \(g(OH)=(gO)H\)。

在左算子情形，读法方向反转，因而出现反同态。进一步，带算子群的算子同态由 \((gO)\sigma=(g\sigma)O\) 定义；若为左算子，则用 \((Og)\sigma=O(g\sigma)\)。两个算子域相互诱导自同构的条件，可由可交换的结合关系表示。

Script/codepoint and TeX/PDF notes:

- Automorphismenbereich is rendered 自己同型領域 / 自同构域; Automorphismenring remains 自己同型環 / 自同构环.
- reziproker Homomorphismus is rendered 反準同型 / 反同态, flagged.
- Fraktur macros \(\frG\), \(\frA\), \(\frB\) and equation tags (1), (1a), (2a*) should stay in TeX.

Unresolved flags:

- Automorphism-domain versus automorphism-ring terminology needs reviewer attention.
- No tensor/localization blocker is affected by operator associativity formulas.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-09-003-product-ring-module-completion

Anchor: German baseline lines `19115-19134`; completion of §1,4 product-ring module transition.

Source summary: Completes the proof that the given double module extends to a module over a product ring via compatible homomorphisms into commuting automorphism subrings.

Japanese title: 積環上の加群への延長

既存の `cjk-corpus-016` が扱った右双加群から積環への移行の証明は、ここで具体的な式に帰着される。自己同型環の中で、可換な部分環 \(\overline{\frR}\) と \(\overline{\frS}\) が作る積環 \(\overline{\frT}\) は、\(\sum_i \bar r_i\bar s_i+\bar r+\bar s\) 型の元から成る。

対応する積環 \(\frT\) が \(\frR,\frS\) を可換な部分環として含むなら、\(\sum_i r_i s_i+r+s\) を \(\sum_i \bar r_i\bar s_i+\bar r+\bar s\) に送ることで、\(\frT\to\overline{\frT}\) の準同型が得られる。

その結果、\(m(\sum_i r_i s_i+r+s)=\sum_i(mr_i)s_i+mr+ms\) という作用が一意に定まり、もとの \(\frR,\frS\) 双加群を含む \(\frT\)-加群が得られる。これは積環であり、テンソル積の根拠ではない。

Simplified Chinese title: 向积环上模的延拓

既有 `cjk-corpus-016` 已处理右双模到积环的过渡；此处把证明落实到具体公式。自同构环中，可交换子环 \(\overline{\frR}\) 与 \(\overline{\frS}\) 生成的积环 \(\overline{\frT}\)，由 \(\sum_i \bar r_i\bar s_i+\bar r+\bar s\) 型元素组成。

若相应积环 \(\frT\) 包含 \(\frR,\frS\) 作为逐元可交换的子环，则把 \(\sum_i r_i s_i+r+s\) 送到 \(\sum_i \bar r_i\bar s_i+\bar r+\bar s\)，即可把原有同态延拓为 \(\frT\to\overline{\frT}\) 的同态。

于是作用 \(m(\sum_i r_i s_i+r+s)=\sum_i(mr_i)s_i+mr+ms\) 唯一定义，得到一个包含原 \(\frR,\frS\) 双模的 \(\frT\)-模。这是积环，不是张量积证据。

Script/codepoint and TeX/PDF notes:

- Produktring remains 積環 / 积环, matching cjk-corpus-016.
- Keep barred fraktur macros \(\overline{\frR}\), \(\overline{\frS}\), \(\overline{\frT}\) intact.
- Explicitly preserve tensor-product blocker: product ring is not tensor product.

Unresolved flags:

- Tensor product remains blocked; this is product-ring evidence only.
- Double-module/register choices remain draft-only.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-09-004-linear-form-modules-automorphism-ring

Anchor: German baseline lines `19135-19175`; §2,1 Linearformenmoduln and Satz 1.

Source summary: Defines linear-form modules over a unital ring and proves that their automorphism ring is reciprocally isomorphic to the full matrix ring.

Japanese title: 線形形式加群と自己同型環

§2 は、§1 の一般論を表現論へ移すため、加群を線形形式加群へ特殊化する。単位元をもつ環 \(\frS\) 上の右加群 \(\frM\) が、\(n\) 個の一項 \(\frS\)-加群の直和 \(\frM=m_1\frS+\cdots+m_n\frS\) と書け、各 \(m_i\frS\) が \(\frS\) と作用素同型なら、\(\frM\) を線形形式加群と呼ぶ。

Satz 1 は、このような \(\frM\) の \(\frS\)-自己同型環 \(\mA\) が、\(\frS\) の元を成分とする \(n\) 次全行列環 \(\mbarA\) と反対同型になる、と述べる。自己同型 \(\alpha\) は \(m_i\mapsto m_i\alpha\) によって完全に決まり、その像は行列 \(A\) で表される。

和については \(\alpha+\beta\mapsto A+B\) となり、積については順序が反転して \(\alpha\beta\mapsto BA\) となる。この順序反転が、ここでの「反対同型」という暫定訳の根拠である。

Simplified Chinese title: 线性型模与自同构环

§2 为把 §1 的一般理论转向表示论，先把模特殊化为线性型模。若有单位元环 \(\frS\) 上的右模 \(\frM\) 可写成 \(n\) 个单项 \(\frS\)-模的直和 \(\frM=m_1\frS+\cdots+m_n\frS\)，并且每个 \(m_i\frS\) 与 \(\frS\) 算子同构，则称 \(\frM\) 为线性型模。

Satz 1 说，这样的 \(\frM\) 的 \(\frS\)-自同构环 \(\mA\)，与所有 \(n\) 阶 \(\frS\)-矩阵组成的全矩阵环 \(\mbarA\) 反同构。自同构 \(\alpha\) 完全由 \(m_i\mapsto m_i\alpha\) 决定，其像可用矩阵 \(A\) 表示。

对加法有 \(\alpha+\beta\mapsto A+B\)，对乘法则顺序反转为 \(\alpha\beta\mapsto BA\)。这个顺序反转正是这里暂译为“反同构”的原因。

Script/codepoint and TeX/PDF notes:

- Linearformenmodul is rendered 線形形式加群 / 线性型模, provisional.
- reziprok isomorph is rendered 反対同型 / 反同构 to reflect reversed multiplication order.
- Macros \(\mA\), \(\mbarA\), \(\frM\), and matrix tuple formulas must stay in TeX.

Unresolved flags:

- Reciprocal-isomorphism terminology requires domain review.
- Matrix-ring terminology is draft/non-canonical.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-09-005-reciprocal-direct-representation-modules

Anchor: German baseline lines `19177-19203`; §2,2 Darstellung und Darstellungsmodul; §2,3 transition theorem.

Source summary: Defines reciprocal and direct representations through ring homomorphisms into matrix rings, defines the corresponding representation modules, and states the transition to modules over extension/product rings.

Japanese title: 反表現・直接表現と表現加群

環 \(\frR\) の \(\frS\) における \(n\) 次の反表現または直接表現は、\(\frR\) から \(\frS\) 上の \(n\) 次全行列環の部分環への反準同型または準同型として理解される。Satz 1' は、線形形式加群の自己同型環が全行列環による忠実な反表現を許す、と言い換えられる。

\(\frM\) が \(\frR\) と \(\frS\) の双加群で、同時に両方の右加群であるとき、\(\frM\) は \(\frR\) の \(\frS\) における反表現加群と呼ばれる。一方、\(\frR\)-左、\(\frS\)-右の双加群である場合は直接表現加群である。

任意の反表現加群または直接表現加群は、同値な表現の一つの類を生み、逆にすべての反表現または直接表現はこの形で得られる。さらに、\(\frR\) と \(\frS\) を可換な部分環として含む積環 \(\frT\) が存在する場合、反表現加群は \(\frT\)-加群として扱える。

Simplified Chinese title: 反表示、直接表示与表示模

环 \(\frR\) 在 \(\frS\) 中的 \(n\) 阶反表示或直接表示，可理解为从 \(\frR\) 到 \(\frS\) 上 \(n\) 阶全矩阵环某个子环的反同态或同态。Satz 1' 可表述为：线性型模的自同构环允许由全矩阵环给出的忠实反表示。

若 \(\frM\) 是 \(\frR\) 与 \(\frS\) 的双模，并且同时是二者的右模，则称 \(\frM\) 为 \(\frR\) 在 \(\frS\) 中的反表示模。若它是 \(\frR\)-左、\(\frS\)-右的双模，则称为直接表示模。

每个反表示模或直接表示模都产生一个等价表示类；反过来，所有反表示或直接表示也都由这种方式产生。进一步，若存在积环 \(\frT\) 含有逐元可交换的 \(\frR\) 与 \(\frS\)，则反表示模可视为 \(\frT\)-模。

Script/codepoint and TeX/PDF notes:

- reziproke Darstellung is rendered 反表現 / 反表示; direkte Darstellung as 直接表現 / 直接表示.
- Darstellungsmodul follows existing 表現加群 / 表示模 register.
- Produktring remains product ring, not tensor product.

Unresolved flags:

- 反表現 / 反表示 is a provisional CJK rendering for reziproke Darstellung.
- Tensor product remains blocked.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-09-006-commuting-matrices-operatorhomomorphic-extension

Anchor: German baseline lines `19205-19231`; consequence of transition theorem and theorem on commuting matrices.

Source summary: States that isomorphism of representation modules is equivalent to product-ring isomorphism, then describes matrices commuting with a reciprocal representation and the operator-homomorphic extension.

Japanese title: 可換行列と作用素準同型的な拡張

移行定理の帰結として、反表現加群 \(\frM\) が同時に積環 \(\frT\) の加群であるなら、\(\frR,\frS\)-同型と \(\frT\)-同型は同値になる。したがって、\(\frT\)-加群の同型類と、\(\frR\) の \(\frS\) における反表現類は一対一に対応する。

続く可換行列の定理では、\(\frR\to\frR^*\) を \(\frS\) における \(n\) 次反表現とし、\(\frB^*\) を \(\frR^*\) の各元と可換な \(n\) 次行列全体の環とする。この \(\frB^*\) は、生成する表現加群の \(\frR,\frS\)-自己同型、または積環が存在すれば \(\frT\)-自己同型を反対同型的に表現する。

最後に、\(\frR\) と \(\frS\) が決める \(\frT\) から行列への対応は、\(\frT\) 自身の表現ではなく、\(\frR\) の反表現を \(\frS\) に関して作用素準同型的に拡張したものだと注意される。

Simplified Chinese title: 可交换矩阵与算子同态式扩张

过渡定理的推论说，若反表示模 \(\frM\) 同时也是积环 \(\frT\) 的模，则 \(\frR,\frS\)-同构与 \(\frT\)-同构等价。因此，\(\frT\)-模的同构类与 \(\frR\) 在 \(\frS\) 中的反表示类一一对应。

随后的可交换矩阵定理设 \(\frR\to\frR^*\) 是 \(\frS\) 中 \(n\) 阶反表示，\(\frB^*\) 是所有与 \(\frR^*\) 中每个元素逐元可交换的 \(n\) 阶矩阵所成的环。这个 \(\frB^*\) 给出生成表示模的 \(\frR,\frS\)-自同构，或在积环存在时的 \(\frT\)-自同构的反同构表示。

最后源文强调，由 \(\frR\) 与 \(\frS\) 唯一定义的从 \(\frT\) 到矩阵的对应，并不是环 \(\frT\) 的表示，而是把 \(\frR\) 的反表示扩张为关于 \(\frS\) 的算子同态式表示。

Script/codepoint and TeX/PDF notes:

- vertauschbare Matrizen is rendered 可換行列 / 可交换矩阵.
- operatorhomomorph is rendered 作用素準同型的 / 算子同态式, provisional.
- Keep \(\frR^*\), \(\frB^*\), and \([\frR,\frS]\) TeX forms intact.

Unresolved flags:

- Operator-homomorphic extension wording needs domain review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
