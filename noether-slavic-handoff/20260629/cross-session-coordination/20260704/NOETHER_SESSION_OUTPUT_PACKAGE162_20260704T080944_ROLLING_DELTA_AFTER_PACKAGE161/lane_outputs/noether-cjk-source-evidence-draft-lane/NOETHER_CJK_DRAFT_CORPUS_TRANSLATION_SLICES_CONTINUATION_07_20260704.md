# Noether CJK Draft Corpus Translation Slices: Continuation 07

Generated UTC: `2026-07-04T06:06:48.950579+00:00`

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

- tensor product: no German Tensorprodukt anchor; noisy otimes hits around LocalCodex repair lines 21525/21582 and shifted primary lines 21847/21904 do not name or explain tensor product
- localization: Quotientenring candidates at 16223-16225 and 18467 but no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: source-shelf/course-register evidence only
- modern algebra: Moderne Algebra remains bibliographic only

## cjk-continuation-07-001-maximal-domains-denominator-primes

Anchor: German baseline lines `18289-18312`; 35. Über Maximalbereiche aus ganzzahligen Funktionen.

Source summary: Introduces maximal domains of integral functions in several variables, their integral extensions, denominator primes, and the relation to Hilbert's fourteenth problem.

Japanese title: 整係数関数から作る最大領域と分母の素数

この論文では、複数の変数 \(x_1,\ldots,x_n\) に関する整数係数関数から出発し、有限個の関数で生成される整域 \(I\) を考える。その商体の中で、\(I\) に対して整であるような関数をすべて加えたものを最大領域 \(M(I)\) と呼ぶ。

最大領域という語は、さらに分母を持つ整関数を加えても領域を広げられないという意味で使われている。有限な整域 \(I\) から出発すると、\(M(I)\) に現れる分母には、有限個の異なる素数だけが関わる。

分母に現れる各素数の指数が有界であることは、この最大領域が有限であることと同値であり、ここで Hilbert の第十四問題との接点が現れる。分母の素数は、法 \(p\) での関係式、すなわち素性の破れや超越次数の低下と結びつく。

Simplified Chinese title: 由整数系数函数形成的最大域与分母素数

本篇从若干变量 \(x_1,\ldots,x_n\) 的整数系数函数出发，考虑由有限个函数生成的整环 \(I\)。在其商域中，把所有对 \(I\) 整的函数加入后得到的对象，暂称为最大域 \(M(I)\)。

这里的最大域，是指再加入带分母的整函数也不能继续扩大的域。若从有限整环 \(I\) 出发，则 \(M(I)\) 中出现的分母只涉及有限多个不同素数。

各分母素数的指数有界，与这个最大域为有限对象等价，由此接上 Hilbert 第十四问题。分母素数对应于模 \(p\) 后出现的关系式，也就是素性失效或超越次数下降。

Script/codepoint and TeX/PDF notes:

- Maximalbereich is rendered provisionally as 最大領域 / 最大域; this must not be read as an approved field-theoretic term.
- ganzzahlige Funktionen is rendered descriptively as 整数係数関数 / 整数系数函数, with integral-function nuance flagged.
- Hilbert remains Latin-script; Japanese/Simplified Chinese punctuation stays outside inline TeX.

Unresolved flags:

- Maximalbereich and ganzzahlige Funktionen need native/domain review.
- This slice does not provide abstract-algebra or localization source closure.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-07-002-functional-determinants-characteristic-p

Anchor: German baseline lines `18316-18347`; Funktionaldeterminanten bei Funktionen von Charakteristik p.

Source summary: Uses functional matrices and determinants in characteristic p to detect algebraic dependence and to preserve algebraic independence under reduction modulo suitable primes.

Japanese title: 標数 \(p\) における関数行列式

標数 \(p\) の係数体をもつ関数 \(y_1,\ldots,y_t\) を考える。これらが代数閉包を含む拡大体上で代数的に従属するなら、対応する関数行列の階数は \(t\) より小さくなる。

この主張を用いると、整数係数関数 \(y_1,\ldots,y_t\) の関数行列が階数 \(t\) を持つ場合、有限個の分母や行列式を避ける素数 \(p\) について、法 \(p\) への還元後もそれらは代数的独立である。

したがって、分母やある関数行列式を消してしまう素数を除けば、標数 \(p\) での像は、元の独立性を反映する。この箇所は関数行列式の判定法であり、テンソル積の根拠ではない。

Simplified Chinese title: 特征 \(p\) 中的函数行列式

考虑系数域特征为 \(p\) 的函数 \(y_1,\ldots,y_t\)。若它们在含代数闭包的扩域上代数相关，则相应函数矩阵的秩小于 \(t\)。

利用这一点，若整数系数函数 \(y_1,\ldots,y_t\) 的函数矩阵具有秩 \(t\)，则对避开有限多个分母和行列式的素数 \(p\)，这些函数模 \(p\) 化后仍保持代数无关。

因此，除去那些消去分母或某个函数行列式的素数外，特征 \(p\) 中的像仍反映原有的独立性。本处是函数行列式判别，不是张量积来源。

Script/codepoint and TeX/PDF notes:

- Funktionaldeterminante is rendered 関数行列式 / 函数行列式; Funktionalmatrix as 関数行列 / 函数矩阵.
- Use 標数 for Japanese and 特征 for Simplified Chinese; both are draft register choices.
- TeX \(p\), \(t\), and \(y_i\) must stay ASCII inside math mode.

Unresolved flags:

- Characteristic-p terminology and functional determinant wording need reviewer attention.
- No retained blocker is closed by this determinant material.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-07-003-maximal-domain-theorem-mod-p

Anchor: German baseline lines `18350-18395`; Formulierung des Satzes über Maximalbereiche.

Source summary: States the maximal-domain theorem for a finite integral domain with integral basis, intermediate domains in the quotient field, and homomorphisms modulo primes.

Japanese title: 最大領域定理と法 \(p\) の準同型

有限な整域 \(I\) に整基 \(f_1,\ldots,f_\rho\) が与えられ、その商体の中に中間領域 \(Z\) があるとする。最大領域 \(M(I)\) を \(I\) に付随させると、例外的な有限個の素数を除いて、法 \(p\) の準同型はあるイデアル \(\ma_p\) を通じて媒介される。

この形で定理を読むと、もし \(p g(x)\) が \(I\) に属し、しかも \(g\) が中間領域 \(Z\) に属するなら、適切な例外を除き \(g\) 自身が \(I\) に属する。したがって、分母に現れる素数を有限に制御できる。

同じ議論は、素数 \(p\) を避ける整数 \(a\) についても繰り返される。ここでの商体・中間領域・最大領域の用語は、原典行に沿った暫定的な読みであり、局所化という承認済み橋渡しではない。

Simplified Chinese title: 最大域定理与模 \(p\) 同态

设有限整环 \(I\) 有整基 \(f_1,\ldots,f_\rho\)，并在其商域中取中间域 \(Z\)。把最大域 \(M(I)\) 赋予 \(I\) 后，除有限多个例外素数外，模 \(p\) 的同态都通过某个理想 \(\ma_p\) 来媒介。

按这种表述，若 \(p g(x)\) 属于 \(I\)，而 \(g\) 又属于中间域 \(Z\)，则避开适当例外后，\(g\) 本身属于 \(I\)。于是，分母中出现的素数可以被有限控制。

同一论证也可对避开素数 \(p\) 的整数 \(a\) 重复进行。这里的商域、中间域和最大域均为依照源行的暂译，不构成对局部化术语的批准桥接。

Script/codepoint and TeX/PDF notes:

- Integral basis is rendered 整基 / 整基; quotient field as 商体 / 商域.
- The German source uses homomorphism and quotient-field language, not a direct Lokalisierung label.
- Keep \(\ma_p\), \(M(I)\), and \(p g(x)\) in TeX; avoid inserting CJK characters into macro names.

Unresolved flags:

- Localization remains blocked despite quotient-field/denominator context.
- Maximal-domain theorem wording remains draft/non-canonical.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-07-004-absolute-prime-exceptional-prime-ideals

Anchor: German baseline lines `18398-18473`; Beweis; Algebraische Koeffizienten.

Source summary: Proves the theorem through absolute prime ideals, records finite exceptional-prime conditions, and extends the construction from rational integers to finite algebraic number fields.

Japanese title: 絶対素イデアルと例外素イデアル

証明の中心には、準同型を媒介するイデアル \(\ma\) が絶対素イデアルであるという補題が置かれる。そこから、満たすべき条件 I, II, III を列挙し、除外される素数が有限個であることを示す。

最後に、係数を有理整数から有限次代数的数体の整数へ拡張する。有限次拡大においては、素数の代わりに素イデアルを扱い、例外集合も有限個の素イデアルとして記録される。

行 18467 付近では、\((\ma)\) に素な分母を持つ商を加えて作る商環 \(R_\ma\) が現れる。これは局所化に近い候補として記録できるが、原典は `Lokalisierung' と名付けていないため、局所化ブロッカーは解除しない。

Simplified Chinese title: 绝对素理想与例外素理想

证明的核心是一个引理：媒介同态的理想 \(\ma\) 是绝对素理想。随后列出需满足的条件 I、II、III，并证明需排除的素数只有有限多个。

最后，系数从有理整数推广到有限代数数域的整数。在有限扩张中，讨论对象从素数改为素理想，例外集合也记录为有限多个素理想。

在 18467 行附近，源文构造了商环 \(R_\ma\)，方式是加入分母与 \((\ma)\) 互素的商。这可作为接近局部化的候选证据记录，但原文没有使用 `Lokalisierung' 名称，所以局部化阻塞项不解除。

Script/codepoint and TeX/PDF notes:

- absolute Primideal is rendered 絶対素イデアル / 绝对素理想 and remains provisional.
- The explicit line-18467 quotient-ring note is evidence metadata only; it is not promoted to a localization term.
- Use 素イデアル for Japanese and 素理想 for Simplified Chinese consistently in this slice.

Unresolved flags:

- Localization blocker retained: quotient-ring construction at 18467 lacks the German Lokalisierung label.
- Absolute-prime terminology requires native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-07-005-ideal-differentiation-different-note

Anchor: German baseline lines `18480-18490`; 36. Idealdifferentiation und Differente.

Source summary: Short note identifying the different of an algebraic number field as the differential quotient of a defining ideal, with a full Math. Ann. treatment announced.

Japanese title: イデアル微分とディッフェレント

この短い報告では、代数的数体のディッフェレントを、定義イデアルの微分商として捉える。通常の定義との一致は、Lagrange 補間に類似した構造定理から導かれる、と予告されている。

ここでの記述は要旨に限られ、完全な証明は Math. Ann. の続稿に委ねられている。したがって、イデアル微分・微分商・ディッフェレントの訳語は、後続資料での照合が必要な暫定案である。

Simplified Chinese title: 理想微分与不同式

这则短札把代数数域的不同式视为定义理想的微分商。它与通常定义一致这一点，源文说可由类似 Lagrange 插值的结构定理推出。

本处只是摘要性说明，完整证明留给 Math. Ann. 的后续论文。因此，理想微分、微分商、不同式这些译法，都只是待后续文献核对的暂译。

Script/codepoint and TeX/PDF notes:

- Differente is rendered ディッフェレント for Japanese and 不同式 for Simplified Chinese, both flagged.
- Lagrange remains Latin-script; Math. Ann. remains bibliographic.
- The short source note gives no tensor/localization/Harish-Chandra evidence.

Unresolved flags:

- Different/Differente terminology needs source cross-check and native review.
- This slice is an abstract note, not a full proof translation.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-07-006-normal-basis-introduction-group-ring-strategy

Anchor: German baseline lines `18494-18508`; 37. Normalbasis bei Körpern ohne höhere Verzweigung.

Source summary: Introduces normal bases for Galois number fields without higher ramification, links discriminants to group determinants, and sets up the group-ring ideal strategy.

Japanese title: 高次分岐のない体における正規基底

Galois 数体 \(K/k\) において、高次分岐がない場合を扱う。分岐した素点で、その素数が拡大次数を割らないなら、整数環の対応する \(p\) 進拡大には正規基底が存在する。

この条件の下では、判別式は群行列式の平方として表される。さらに Artin の導手に関する議論が背景にあり、証明は整数環 \(O/o\) を整数群環の一側イデアルに作用素同型にする方針で進む。

通常分岐の場所では整数群環が極大オーダーになり、\(p\) 進半単純系の極大オーダーにおけるイデアルが主イデアルであることを用いる。ここでも群環は Gruppenring の訳であり、群代数とは自動的に同一視しない。

Simplified Chinese title: 无高次分歧域中的正规基

这一节讨论 Galois 数域 \(K/k\) 没有高次分歧的情形。若在分歧素点处，相应素数不整除扩张次数，则整数环的相应 \(p\) 进扩张存在正规基。

在这个条件下，判别式可写成群行列式的平方。源文还以 Artin 导子为背景，证明策略是把整数环 \(O/o\) 作为 Galois 模，与整数群环中的一个单侧理想算子同构。

在普通分歧处，整数群环成为极大序，并使用 \(p\) 进半单系统中极大序的理想为主理想这一事实。这里的群环对应 German `Gruppenring'，不自动合并为群代数。

Script/codepoint and TeX/PDF notes:

- Normalbasis is rendered 正規基底 / 正规基; höhere Verzweigung as 高次分岐 / 高次分歧.
- Artin conductor is rendered Artin の導手 / Artin 导子 but remains unreviewed.
- Group ring remains 群環 / 群环; group algebra is not closed here.

Unresolved flags:

- Artin conductor and maximal-order terminology need native/domain review.
- This Artin occurrence does not address the Harish-Chandra blocker.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-07-007-p-adic-integer-group-ring-galois-modules

Anchor: German baseline lines `18510-18585`; Der p-adisch erweiterte ganzzahlige Gruppenring; Galoismoduln.

Source summary: Defines rational and integer group rings, proves maximal-order and principal-ideal statements away from the group order, and identifies Galois modules with group-ring modules via normal bases.

Japanese title: \(p\) 進整数群環と Galois 加群

群 \(G\) に対し、有理群環と整数群環を区別して導入する。群の位数 \(n\) を割らない素イデアル \(p\) について、整数群環を \(o_p\) へ拡大したものは極大オーダーになる。逆に \(p\) が \(n\) を割る場合、それは極大ではない。

この判定では、ラジカルをもたない系、すなわち半単純系の言葉が使われる。群環の判別式は群の位数の冪であり、\(p\nmid n\) の場合、整数群環に関する任意の整イデアルまたは分数イデアルは主イデアルになる。

次に、Galois 加群を導入する。体 \(K/k\) は体の正規基底を用いて群環と作用素同型になり、整数環 \(O/o\) は最大階数の群環加群と作用素同型になる。次数を割らない各場所では、\(O_p/o_p\) に正規基底が存在する。

Simplified Chinese title: \(p\) 进整数群环与 Galois 模

对群 \(G\)，源文区分有理群环和整数群环。若素理想 \(p\) 不整除群阶 \(n\)，则把整数群环扩张到 \(o_p\) 后得到极大序。反之，若 \(p\) 整除 \(n\)，它就不是极大序。

这一判定使用无根基系统，即半单系统的语言。群环的判别式是群阶的幂；当 \(p\nmid n\) 时，关于整数群环的任一整数理想或分式理想都是主理想。

随后引入 Galois 模。域 \(K/k\) 借助域的正规基与群环算子同构，而整数环 \(O/o\) 与最大秩的群环模算子同构。在每个不整除次数的地方，\(O_p/o_p\) 都有正规基。

Script/codepoint and TeX/PDF notes:

- p-adisch is rendered \(p\) 進 / \(p\) 进; keep p in math mode.
- Semisimple system language is connected to Continuation 05 evidence but remains draft/non-approved.
- maximal order/principal ideal are rendered 極大オーダー・主イデアル / 极大序・主理想 as provisional register choices.

Unresolved flags:

- Semisimple-ring evidence exists, but no native-review or approval claim is made.
- Integer group ring terminology needs reviewer confirmation.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-07-008-discriminant-as-group-determinant

Anchor: German baseline lines `18586-18671`; Die Diskriminante als Gruppendeterminante.

Source summary: Shows that discriminants of Galois fields without higher ramification are squares of group determinants and records factorization by absolutely irreducible representations and conductor ideals.

Japanese title: 群行列式としての判別式

高次分岐をもたない Galois 体について、各分岐場所での判別式は、正規基底の元を変数に代入した群行列式の平方になる。これは局所的な正規基底の存在と、群環のイデアルが主イデアルになることを使って得られる。

群行列式は、絶対既約表現に従って一般化された根数へ分解する。したがって判別式も、対応する指標体の中で因子分解される。ここでの既約表現・指標体の訳語は、前の表現論スライスと合わせた暫定訳である。

巡回素次数の場合には、判別式のイデアル分解が導手と結びつく。導手を含むこの記述は Artin 型の背景を持つが、Harish-Chandra には関係せず、未解決ブロッカーを動かさない。

Simplified Chinese title: 作为群行列式的判别式

对于没有高次分歧的 Galois 域，在每个分歧处，判别式都是把正规基元素代入群行列式后所得表达式的平方。这一结论使用局部正规基的存在，以及群环理想为主理想的事实。

群行列式按绝对不可约表示分解为广义根数。因此，判别式也在相应的特征标域中分解。这里的不可约表示、特征标域译法，与前面表示论切片保持一致，但仍为暂译。

在循环素次数情形，判别式的理想分解与导子相联系。含导子的这段说明有 Artin 型背景，但不涉及 Harish-Chandra，也不改变未解决阻塞项。

Script/codepoint and TeX/PDF notes:

- Gruppendeterminante is rendered 群行列式 in both Japanese and Simplified Chinese.
- Führer is rendered 導手 / 导子, flagged for domain review.
- Absolutely irreducible representation follows earlier 絶対既約表現 / 绝对不可约表示 usage.

Unresolved flags:

- Conductor/character-field terminology needs reviewer attention.
- Harish-Chandra, tensor product, abstract algebra, and modern algebra remain blocked.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
