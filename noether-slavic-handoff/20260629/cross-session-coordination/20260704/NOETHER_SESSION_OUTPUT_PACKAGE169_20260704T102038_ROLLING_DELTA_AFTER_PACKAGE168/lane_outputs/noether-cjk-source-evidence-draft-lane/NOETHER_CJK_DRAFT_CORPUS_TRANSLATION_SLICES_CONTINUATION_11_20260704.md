# Noether CJK Draft Corpus Translation Slices: Continuation 11

Generated UTC: `2026-07-04T08:05:55.937993+00:00`

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

- tensor product: no German Tensorprodukt anchor; direct-product/direct-sum language in Paper 40 remains non-anchor evidence
- localization: Quotientenring candidates at 16223-16225 and 18467 but no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: source-shelf/course-register evidence only
- modern algebra: Moderne Algebra remains bibliographic only; Nichtkommutative Algebra remains a non-modern-algebra title/context

## cjk-continuation-11-001-extension-counts-and-maximal-subfield-theorem

Anchor: German baseline lines `19481-19520`; §6,3 Hilfssatz 2 and maximal-subfield formulation.

Source summary: Shows that every reciprocal isomorphism of an intermediate field T has at least as many extensions as the rank of S over T, then reformulates the main theorem via induced class partitions.

Japanese title: 同型の延長数と最大部分体

第二補題では、\(T\) が \(P\) と \(S\) の間の体で、\(S\) の \(T\) 上の階数を \(s\) とすると、\(T\) から \(A\) への任意の反対同型は少なくとも \(s\) 個の異なる延長を持つ、と述べる。

この反対同型を冪等元 \(E_i\) による分解 \(T_A=E_1T_A+\cdots+E_hT_A=E_1A+\cdots+E_hA\) で表し、右から \(S\) を掛けると \(S_A=E_1S_A+\cdots+E_hS_A\) となる。各 \(E_iS_A\) は階数 \(s\) を持ち、さらに \(s\) 個の単純右イデアルに分かれるので、それらが \(T\) の同じ表現の異なる延長を与える。

その後、\(T\) が誘導する \(S\) から \(A\) への反対同型集合の類分け \(\mathfrak I_T\) を定義する。同じ \(T\) 上の同型を誘導するものを同値とし、この類分けに関して \(T\) が最大部分体である、という形で主定理が表現される。

Simplified Chinese title: 同构延拓数与最大子域

第二引理说，若 \(T\) 是介于 \(P\) 与 \(S\) 之间的除环，且 \(S\) 在 \(T\) 上的秩为 \(s\)，则从 \(T\) 到 \(A\) 的任一反同构至少有 \(s\) 个不同延拓。

把这个反同构写成由幂等元 \(E_i\) 给出的分解 \(T_A=E_1T_A+\cdots+E_hT_A=E_1A+\cdots+E_hA\)，再右乘 \(S\)，得到 \(S_A=E_1S_A+\cdots+E_hS_A\)。每个 \(E_iS_A\) 的秩为 \(s\)，并进一步分解为 \(s\) 个单右理想，所以它们给出同一 \(T\)-表示的不同延拓。

随后定义由 \(T\) 诱导的从 \(S\) 到 \(A\) 的反同构集合的分类 \(\mathfrak I_T\)：在 \(T\) 上诱导同一同构者视为等价。主定理可表述为，相对于这个分类，\(T\) 是最大子域。

Script/codepoint and TeX/PDF notes:

- reziproker Isomorphismus remains 反対同型 / 反同构.
- Klasseneinteilung is rendered 類分け / 分类; maximaler Unterkörper as 最大部分体 / 最大子域.
- Keep \(T_A\), \(S_A\), \(E_iS_A\), and \(\mathfrak I_T\) in TeX.

Unresolved flags:

- Maximal-subfield and class-partition wording needs domain review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-11-002-brauer-group-of-similar-algebra-classes

Anchor: German baseline lines `19521-19535`; §7,1 class of similar algebras and Brauer group theorem.

Source summary: Restricts to finite-dimensional normal simple algebras over their center, defines classes of similar algebras, and states Brauer's theorem that these classes form an abelian group under direct product.

Japanese title: 相似代数類と Brauer 群

§7 からは、中心 \(P\) 上有限階数の体 \(A,\overline A\) と行列環 \(A_f\) だけを扱う。これは \(P\) 上の正規単純代数、短く \(P\) 上の代数であり、\(A,\overline A\) は除法代数になる。

同じ随伴除法代数 \(A\) を持つすべての \(A_f\) を、相似代数の一つの類にまとめる。二つの代数 \(A,B\) の積、すなわち \(P\) 上の直接積は、ふたたび中心 \(P\) をもつ単純代数の類を定める。

Brauer の定理は、相似代数類が直接積に関して可換群をなす、というものである。単位類は \(P\) 上の行列環からなり、類 \((A)\) の逆類は、\(A\) と反対同型な \(\overline A\) に相似な代数類で与えられる。

Simplified Chinese title: 相似代数类与 Brauer 群

从 §7 开始，只考虑在中心 \(P\) 上有限秩的除环 \(A,\overline A\) 及矩阵环 \(A_f\)。这些就是 \(P\) 上的正规单代数，简写为 \(P\) 上的代数，而 \(A,\overline A\) 是除代数。

所有具有同一伴随除代数 \(A\) 的 \(A_f\)，被归入一个相似代数类。两个代数 \(A,B\) 的积，即 \(P\) 上的直接积，又确定一个中心为 \(P\) 的单代数类。

Brauer 定理说，相似代数类在直接积下构成阿贝尔群。单位类由 \(P\) 上矩阵环组成；类 \((A)\) 的逆类由与 \(A\) 反同构的 \(\overline A\) 所相似的代数给出。

Script/codepoint and TeX/PDF notes:

- direct product is 直接積 / 直接积, explicitly not tensor product.
- Brauer group is kept as Brauer 群, matching Continuation 08.
- Keep \((A)\), \(A_f\), and \(A_r\times_P B_s=C_t\) contexts in TeX where used.

Unresolved flags:

- Direct-product wording must not promote tensor product.
- Brauer-group terminology remains draft-only.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-11-003-splitting-fields-of-algebra-classes

Anchor: German baseline lines `19537-19563`; §7,2 splitting fields of an algebra class.

Source summary: Characterizes splitting fields of an algebra class through irreducible embeddings as maximal commutative subfields of a matrix algebra.

Japanese title: 代数類の分解体

代数類の分解体の理論も、§5 冒頭の原理に基づく。可換な拡大体 \(Z/P\) は、\(A\) または \(\overline A\) の中に表現される。\(A\) の中心が \(P\) で \(Z\) が有限可換拡大体なら、\(A_Z\) は中心 \(Z\) をもつ単純代数となる。

拡大類 \((A)_Z\) に随伴する除法代数 \(D\) は、\(Z\) を \(A_f\) に既約に埋め込んだとき、\(A_f\) の中で \(Z\) と元ごとに可換な全体として得られる。可約な埋め込みでは、この可換全体は \(D\) 上の行列環になる。

有限可換拡大体 \(Z\) が類 \((A)\) の分解体であることは、\((A)_Z\) が \(Z\) 上の単位類、すなわち行列環の類になることと同値である。したがって、\(Z\) は既約埋め込みによって \(A_f\) の最大可換部分体を与えるとき、かつそのときに限り、分解体である。

Simplified Chinese title: 代数类的分裂域

代数类的分裂域理论同样基于 §5 开头的原则。交换扩域 \(Z/P\) 被表示在 \(A\) 或 \(\overline A\) 中。若 \(A\) 的中心为 \(P\)，而 \(Z\) 是有限交换扩域，则 \(A_Z\) 是中心为 \(Z\) 的单代数。

扩张类 \((A)_Z\) 的伴随除代数 \(D\)，在把 \(Z\) 不可约地嵌入 \(A_f\) 时，由 \(A_f\) 中与 \(Z\) 逐元可交换的全体给出。若嵌入可约，则这个可交换全体成为 \(D\) 上的矩阵环。

有限交换扩域 \(Z\) 是类 \((A)\) 的分裂域，当且仅当 \((A)_Z\) 是 \(Z\) 上的单位类，也就是矩阵环类。因此，\(Z\) 通过不可约嵌入给出 \(A_f\) 的最大交换子域时，并且只有此时，才是分裂域。

Script/codepoint and TeX/PDF notes:

- Zerfällungskörper follows established convention: 分解体 / 分裂域.
- maximal commutative subfield is 最大可換部分体 / 最大交换子域.
- Commutant language remains descriptive rather than a promoted glossary term.

Unresolved flags:

- Splitting-field terminology remains draft/non-canonical.
- No localization or tensor blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-11-004-rank-index-separable-splitting-fields

Anchor: German baseline lines `19564-19603`; §7,3-4 rank relations, index, and separable splitting fields.

Source summary: Derives square-rank and index relations for central simple algebras, then proves that every algebra class has separable splitting fields embeddable in the division algebra.

Japanese title: 階数・Schur 指数・分離分解体

階数関係から、中心上の単純代数の階数は平方数であることが従う。最大可換部分体 \(Z\subset A\) について \((Z:P)^2=(A:P)\) となり、\((A:P)=m^2\)、\((Z:P)=m\) と書ける。この \(m\) が Schur 指数であり、除法代数 \(A\) 自身に埋め込める分解体の次数でもある。

一般の分解体の次数 \(n\) は \(n=mr\) と書ける。より一般に \(A_L\sim D\) で、\(D\) の中心 \(L\) 上の階数を \(d^2\)、\(L/P\) の次数を \(l\) とすれば、\(ld=mr\) という関係が得られる。

さらに、任意の類 \((A)\) は分離分解体を持ち、しかも \(A\) 自身に埋め込めるものを持つ。特性 \(p\) の場合、指数 \(m=s p^f\) を使い、還元判別式と非零還元トレースを持つ元を選ぶことで、指数を真に下げる分離拡大を構成し、有限回の反復で分離分解体に到達する。

Simplified Chinese title: 秩、Schur 指标与可分分裂域

由秩关系可推出，中心上单代数的秩是平方数。对最大交换子域 \(Z\subset A\)，有 \((Z:P)^2=(A:P)\)，于是可写成 \((A:P)=m^2\)、\((Z:P)=m\)。这个 \(m\) 是 Schur 指标，也是可嵌入除代数 \(A\) 自身的分裂域次数。

一般分裂域的次数 \(n\) 可写为 \(n=mr\)。更一般地，若 \(A_L\sim D\)，\(D\) 在其中心 \(L\) 上的秩为 \(d^2\)，而 \(L/P\) 的次数为 \(l\)，则得到关系 \(ld=mr\)。

进一步，每个类 \((A)\) 都有可分分裂域，而且可以取为嵌入 \(A\) 自身的分裂域。在特征 \(p\) 的情形，将指标写为 \(m=s p^f\)，并借助约化判别式和具有非零约化迹的元素，构造使指标真下降的可分扩张，有限次重复后得到可分分裂域。

Script/codepoint and TeX/PDF notes:

- Index is rendered Schur 指数 in Japanese and Schur 指标 in Simplified Chinese to avoid the C08 Japanese double-指数 issue where possible.
- reduced trace/discriminant are 還元トレース・還元判別式 / 约化迹・约化判别式.
- Keep formulas \((A:P)=m^2\), \(n=mr\), and \(ld=mr\) in TeX.

Unresolved flags:

- Index terminology still needs reviewer attention across Japanese slices.
- Separable/inseparable terminology remains draft-only.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-11-005-commutative-splitting-and-one-factor-fields

Anchor: German baseline lines `19605-19622`; §8,1 splitting and Abspaltung fields of commutative simple systems.

Source summary: Defines splitting fields and one-factor splitting fields for commutative simple systems, characterizes them via isomorphic subfields and the Galois closure, and contrasts commutative and noncommutative uniqueness.

Japanese title: 可換単純系の分解体と一次因子切離し体

§8 では、中心上単純な系の分解体から任意の単純系の分解体へ進むため、まず可換の場合を扱う。可換単純系 \(Z\) は \(P\) 上の体であり、代数閉拡大体 \(\Omega\) に対し、\(Z_\Omega\) がラジカルを持たないのは、\(Z/P\) が分離的な場合、かつその場合に限られる。

拡大体 \(\Lambda/P\) は、\(Z_\Lambda\) が一次の組成因子へ分解するなら分解体と呼ばれる。拡大体 \(T/P\) は、\(Z_T\) が少なくとも一つの一次組成因子を切り離すなら、一次因子切離し体と呼ばれる。これは、少なくとも一つの絶対既約表現が \(T\) の中に存在する、という意味でもある。

特徴づけは明快である。\(T\) が一次因子切離し体であるのは、\(Z\) と同型な部分体を含むとき、かつそのときに限る。 \(\Lambda\) が分解体であるのは、\(Z\) に属する Galois 体と同型な部分体を含むとき、かつそのときに限る。

Simplified Chinese title: 交换单系统的分裂域与一次因子分出域

§8 为了从中心上单系统的分裂域转到任意单系统的分裂域，先处理交换情形。交换单系统 \(Z\) 是 \(P\) 上的域；对代数闭扩域 \(\Omega\)，\(Z_\Omega\) 无根基，当且仅当 \(Z/P\) 是可分扩张。

若扩域 \(\Lambda/P\) 使 \(Z_\Lambda\) 分解为一阶合成因子，则称 \(\Lambda\) 为分裂域。若扩域 \(T/P\) 使 \(Z_T\) 至少分出一个一阶合成因子，则称 \(T\) 为一次因子分出域。换言之，至少有一个绝对不可约表示已经存在于 \(T\) 中。

其刻画很直接：\(T\) 是一次因子分出域，当且仅当它含有一个与 \(Z\) 同构的子域。\(\Lambda\) 是分裂域，当且仅当它含有一个与属于 \(Z\) 的 Galois 域同构的子域。

Script/codepoint and TeX/PDF notes:

- Abspaltungskörper is rendered 一次因子切離し体 / 一次因子分出域, provisional from C09.
- Zerfällungskörper remains 分解体 / 分裂域.
- Do not conflate Abspaltungskörper with localization or tensor product.

Unresolved flags:

- Abspaltungskörper needs native/domain review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-11-006-commutative-galois-idempotents-complementary-bases

Anchor: German baseline lines `19623-19742`; §8,2-4 commutative Galois theory, idempotents, and complementary bases.

Source summary: Gives a hypercomplex proof of commutative Galois theory for separable fields, describes conjugate idempotents in Z_Omega, and relates them to complementary bases and trace.

Japanese title: 可換 Galois 理論・冪等元・補基

§8 の第二部は、分離拡大 \(Z/P\) に対し、§6,3 と平行な同型の理論を与える。分解体 \(\Omega\) の中で、\(Z_\Omega\) は \(e^{(1)}\Omega+\cdots+e^{(n)}\Omega\) という直和に分かれ、各 \(e^{(i)}\) が \(Z\) の異なる表現を生む。

中間体 \(T\) への同型は、\(Z\) の \(T\) 上の階数 \(s\) だけの延長を正確に持つ。このため、\(T\) が誘導する同型集合の類分けに関して \(T\) が最大部分体になる。\(Z\) が Galois なら、通常の自己同型群による定式化へ移ることができる。

さらに、\(Z_\Omega\) の \(n\) 個の冪等元 \(e^{(i)}\) は互いに共役である。基底 \(a_1,\ldots,a_n\) に対して \(e=a_1\beta_1+\cdots+a_n\beta_n\) と書くと、\(\beta_1^S,\ldots,\beta_n^S\) は、写像 \(e^S\) によって得られる補基の像を表す。跡による定義 \(\Sp(a_i b_i)=1\)、\(\Sp(a_i b_k)=0\) もここから得られる。

Simplified Chinese title: 交换 Galois 理论、幂等元与补基

§8 的第二部分对可分扩张 \(Z/P\)，给出与 §6,3 平行的同构理论。在分裂域 \(\Omega\) 中，\(Z_\Omega\) 分解为 \(e^{(1)}\Omega+\cdots+e^{(n)}\Omega\)，每个 \(e^{(i)}\) 产生 \(Z\) 的一个不同表示。

对中间域 \(T\) 的同构，恰有 \(s\) 个延拓，其中 \(s\) 是 \(Z\) 在 \(T\) 上的秩。因此，相对于由 \(T\) 诱导的同构集合分类，\(T\) 是最大子域。若 \(Z\) 为 Galois 域，则可转到通常的自同构群表述。

此外，\(Z_\Omega\) 的 \(n\) 个幂等元 \(e^{(i)}\) 互为共轭。若对基 \(a_1,\ldots,a_n\) 写 \(e=a_1\beta_1+\cdots+a_n\beta_n\)，则 \(\beta_1^S,\ldots,\beta_n^S\) 给出由映射 \(e^S\) 得到的补基的像。迹定义 \(\Sp(a_i b_i)=1\)、\(\Sp(a_i b_k)=0\) 也由此得到。

Script/codepoint and TeX/PDF notes:

- Komplementärbasis is rendered 補基 / 补基, provisional but shorter for repeated use.
- Trace notation uses source macro \Sp; keep as TeX.
- Large idempotent and matrix displays should remain TeX blocks in downstream TeX/PDF sidecars.

Unresolved flags:

- Complementary-basis terminology needs review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-11-007-splitting-and-one-factor-fields-arbitrary-systems

Anchor: German baseline lines `19743-19779`; §9 splitting and Abspaltung fields of arbitrary systems.

Source summary: Extends definitions of splitting fields and one-factor splitting fields to arbitrary hypercomplex systems, reduces to simple systems, and characterizes the separable-center case.

Japanese title: 任意の系の分解体と一次因子切離し体

§9 では、任意の超複素系 \(S\) に対して定義を拡張する。可換拡大体 \(\Lambda/P\) が \(S\) の分解体であるとは、\(S_\Lambda\) の一側イデアルによる組成列の組成因子が絶対単純になることであり、同値に、\(S\) の既約表現が \(\Lambda\) ですでに絶対既約になることである。

拡大体 \(T/P\) が一次因子切離し体であるとは、\(S_T\) が少なくとも一つの絶対単純な組成因子を切り離すこと、つまり \(T\) で既約な表現の少なくとも一つが絶対既約であることである。分解体は各 \(P\)-既約表現の分解体の合成体として得られ、一次因子切離し体はそのうち一つの \(P\)-既約表現の一次因子切離し体で足りる。

単純系 \(A\) の中心 \(Z/P\) が分離的なら、分解体や一次因子切離し体は、\(Z\) を含む最大可換部分体や、中心の分解体との合成によって特徴づけられる。非分離中心の場合にも、ラジカルで割った後の共役成分分解を用いて同じ型の結果が残る。

Simplified Chinese title: 任意系统的分裂域与一次因子分出域

§9 把定义推广到任意超复系统 \(S\)。交换扩域 \(\Lambda/P\) 是 \(S\) 的分裂域，意指 \(S_\Lambda\) 按单侧理想取合成列时，其合成因子都是绝对单的；等价地，\(S\) 的不可约表示在 \(\Lambda\) 中已经绝对不可约。

扩域 \(T/P\) 是一次因子分出域，意指 \(S_T\) 至少分出一个绝对单合成因子，也就是至少有一个在 \(T\) 中不可约的表示已经绝对不可约。分裂域由各个 \(P\)-不可约表示的分裂域合成得到；一次因子分出域则取其中一个 \(P\)-不可约表示的一次因子分出域即可。

若单系统 \(A\) 的中心 \(Z/P\) 可分，则分裂域和一次因子分出域可通过含 \(Z\) 的最大交换子域，以及与中心分裂域的合成来刻画。中心不可分时，也可在取根基商后用共轭成分分解保留同型结果。

Script/codepoint and TeX/PDF notes:

- absolutely simple composition factor is 絶対単純な組成因子 / 绝对单合成因子, provisional.
- inseparable center is 非分離中心 / 中心不可分.
- This section closes Paper 40 coverage through line 19779 but does not close lane blockers.

Unresolved flags:

- Abspaltungskörper and absolutely simple composition factor need native/domain review.
- Tensor product, localization, Harish-Chandra, abstract algebra, and modern algebra remain unresolved.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
