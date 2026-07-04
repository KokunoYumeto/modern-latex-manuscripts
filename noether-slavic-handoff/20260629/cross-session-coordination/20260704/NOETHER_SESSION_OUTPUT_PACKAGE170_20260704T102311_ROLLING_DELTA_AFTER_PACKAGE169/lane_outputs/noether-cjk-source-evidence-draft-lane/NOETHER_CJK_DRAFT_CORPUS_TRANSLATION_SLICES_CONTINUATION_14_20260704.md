# Noether CJK Draft Corpus Translation Slices: Continuation 14

Generated UTC: `2026-07-04T08:21:46.949107+00:00`

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

- tensor product: no German Tensorprodukt anchor; Paper 43 direct product/direct sum material is non-anchor evidence
- localization: Quotientenring candidates now include 16223-16225, 18467, 20105, 20228, 20240, and 20284, but no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: Paper 41 Theorie der Algebren remains contextual only; no new abstract-algebra anchor in Paper 43 20200-20464
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in Paper 43 20200-20464

## cjk-continuation-14-001-paper43-introduction-different-as-differential-quotient

Anchor: German baseline lines `20200-20224`; Paper 43 introduction, differential-quotient definition.

Source summary: Introduces the different as ramification ideal and defines it as a differential quotient of a defining ideal via a difference ideal and ideal quotient.

Japanese title: ディッフェレントを微分商として定義する導入

第43論文は、代数的数体の分岐理論における主定理から出発する。すなわち、ディッフェレント、別名分岐イデアルは、素イデアルが素数 \(p\) の中に \(\varrho\) 乗で現れるとき、少なくとも \((\varrho-1)\) 乗で割り切れる。

著者は、この事実を単なる形式的類似ではなく、多項式の微分商 \(f'(x)\) の性質と同じ構造に属するものとして説明する。ディッフェレントは、数体 \(K\) の定義イデアルの微分商として捉えられる。

具体的には、\(\omega_1,\ldots,\omega_n\) を \(K\) の整数全体、すなわち主整環 \(\mathfrak o\) の加群基底とし、関係をすべて含む定義イデアル \(\mathfrak M\) を考える。差分イデアル \(\mathfrak B=(x_1-\omega_1,\ldots,x_n-\omega_n)\) と差分商 \(\mathfrak A=\mathfrak M:\mathfrak B\) から、\(\mathfrak D=\mathfrak A[x\to\omega]\) によってディッフェレントを定める。

Simplified Chinese title: 把不同式定义为微分商的引言

第43篇论文从代数数域分歧理论的主定理出发：不同式，也就是分歧理想，在素理想以 \(\varrho\) 次幂进入素数 \(p\) 时，至少被该素理想的 \((\varrho-1)\) 次幂整除。

作者说明，这不只是形式类比，而是与多项式微分商 \(f'(x)\) 的性质属于同一结构。不同式可以理解为数域 \(K\) 的一个定义理想的微分商。

具体地，令 \(\omega_1,\ldots,\omega_n\) 为 \(K\) 中整数系统，即主阶 \(\mathfrak o\) 的模基，并令 \(\mathfrak M\) 为包含这些 \(\omega\) 之间全部关系的定义理想。由差分理想 \(\mathfrak B=(x_1-\omega_1,\ldots,x_n-\omega_n)\) 和差分商 \(\mathfrak A=\mathfrak M:\mathfrak B\)，通过 \(\mathfrak D=\mathfrak A[x\to\omega]\) 定义不同式。

Script/codepoint and TeX/PDF notes:

- Differente follows C07/C13: ディッフェレント / 不同式.
- Differentialquotient is 微分商 / 微分商; Differenzenideal and Differenzenquotient are 差分イデアル・差分商 / 差分理想・差分商.
- Keep \(\mathfrak M:\mathfrak B\) and \(\mathfrak D=\mathfrak A[x\to\omega]\) in TeX.

Unresolved flags:

- Different/Differente and order terminology remain native-review issues.
- No retained blocker closure.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-14-002-invariant-definition-complementary-module-quotient-rings

Anchor: German baseline lines `20226-20240`; Paper 43 invariant definition and structural overview.

Source summary: Replaces basis-dependent polynomial data by an invariant definition through direct products, connects the different to complementary modules, and notes quotient-ring passages for relative differents.

Japanese title: 不変的定義・補加群・商環言及

基底に依存しない定義を得るため、著者は主整環 \(\mathfrak o\) と同型な環 \(\mathfrak O\) を導入し、その係数環を \(\mathfrak o\) に拡張して \(\mathfrak O_{\mathfrak o}\) を作る。ここで差分イデアルは対応する元 \(x\) と \(\xi\) の差から作られ、差分商は零イデアルをこの差分イデアルで割ったものになる。

Galois 体 \(F\) に係数を拡張した \(\mathfrak K_F\) は、\(K\) の \(n\) 個の同型に対応する単純成分の直和になる。差分商は成分の単位 \(e^{(i)}\) とディッフェレント \(\mathfrak d\) を用いて \(\mathfrak d e^{(i)}\) と表される。

さらに \(e^{(i)}\) の係数は \(\mathfrak o\) の補加群の基底を与え、ディッフェレントは整環をその補加群で割ったものとして特徴づけられる。本文は相対ディッフェレントにも、一定の商環への移行によって同じ事実が成り立つと述べるが、これは `Lokalisierung' という直接ラベルではない。

Simplified Chinese title: 不变定义、补模与商环提法

为了得到不依赖基的定义，作者引入与主阶 \(\mathfrak o\) 同构的环 \(\mathfrak O\)，并把它的系数环扩张到 \(\mathfrak o\)，得到 \(\mathfrak O_{\mathfrak o}\)。此时差分理想由对应元素 \(x\) 与 \(\xi\) 的差生成，而差分商是零理想除以这个差分理想。

把系数扩张到 Galois 域 \(F\) 后，\(\mathfrak K_F\) 成为对应于 \(K\) 的 \(n\) 个同构的简单分量直和。差分商可用单位分量 \(e^{(i)}\) 和不同式 \(\mathfrak d\) 写作 \(\mathfrak d e^{(i)}\)。

此外，\(e^{(i)}\) 的系数给出 \(\mathfrak o\) 的补模基，而不同式被刻画为阶除以其补模。文本还说，相对不同式通过转到若干商环也满足同样事实；这仍不是带有 `Lokalisierung' 标签的直接 localization 锚点。

Script/codepoint and TeX/PDF notes:

- Records localization-adjacent Quotientenringen mentions at lines 20228 and 20240 without closing localization.
- Direkte Summenzerlegung is 直和分解 / 直和分解, not tensor product.
- Keep \(\mathfrak O_{\mathfrak o}\), \(\mathfrak K_F\), and \(e^{(i)}\) in TeX.

Unresolved flags:

- Localization remains blocked: quotient-ring passages are not direct Lokalisierung evidence.
- Complementary-module terminology remains draft-only.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-14-003-direct-product-definition-coefficient-extension

Anchor: German baseline lines `20242-20278`; §1.1 definition of direct product / coefficient extension.

Source summary: Defines the direct product of rings relative to a subring as coefficient extension, including commutation and formal equality conditions.

Japanese title: 直接積としての係数環の拡張

§1 では、乗法の可換法則を仮定しない一般の環を扱う。環 \(\mathfrak O\times\mathfrak o\)、または \(\mathfrak O_{\mathfrak o}\) は、\(\mathfrak h\) に関する \(\mathfrak O\) と \(\mathfrak o\) の直接積、あるいは \(\mathfrak O\) から係数環 \(\mathfrak h\) を \(\mathfrak o\) に拡張して得たもの、と呼ばれる。

定義では、\(\mathfrak O_{\mathfrak o}\) が \(\mathfrak O\) と \(\mathfrak o\) を部分環として含み、その交わりが \(\mathfrak h\) であり、両者の元が互いに元ごとに可換であることを要求する。したがって \(\mathfrak O_{\mathfrak o}\) は有限個の双線形結合 \(x_iy_i\) で表される。

さらに、等号関係は因子側の関係だけによって形式的に決まる。これにより、直接積の等号・加法・乗法の関係は因子環から一意に定められ、同型なデータからは同型な直接積が得られる。

Simplified Chinese title: 作为系数环扩张的直接积

§1 处理不预设乘法交换律的一般环。环 \(\mathfrak O\times\mathfrak o\)，或 \(\mathfrak O_{\mathfrak o}\)，称为相对于 \(\mathfrak h\) 的 \(\mathfrak O\) 与 \(\mathfrak o\) 的直接积，也称为由 \(\mathfrak O\) 把系数环 \(\mathfrak h\) 扩张到 \(\mathfrak o\) 所得。

定义要求 \(\mathfrak O_{\mathfrak o}\) 含有 \(\mathfrak O\) 与 \(\mathfrak o\) 作为子环，二者的交为 \(\mathfrak h\)，并且两者元素逐元可交换。因此 \(\mathfrak O_{\mathfrak o}\) 由有限个双线性组合 \(x_iy_i\) 构成。

此外，等号关系只由两个因子环中已有的关系形式地决定。这样，直接积中的等号、加法和乘法关系由因子环唯一确定；同构的数据给出同构的直接积。

Script/codepoint and TeX/PDF notes:

- Direct product is 直接積 / 直接积 and remains non-tensor evidence.
- Koeffizientenbereich is rendered as 係数環 / 系数环 for readability, flagged as provisional.
- Keep \(\mathfrak O_{\mathfrak o}\) notation intact.

Unresolved flags:

- Direct product does not close tensor product.
- Coefficient-domain terminology needs review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-14-004-existence-and-defining-ideals-of-direct-products

Anchor: German baseline lines `20279-20332`; §1.2-4 existence and defining ideals.

Source summary: Gives necessary and sufficient conditions for direct products, notes a quotient-ring uniqueness example, defines a ring's defining ideal, and identifies the defining ideal after direct product.

Japanese title: 直接積の存在条件と定義イデアル

直接積が常に存在するわけではないことを示すため、\(\mathfrak h[x]\) と \(\mathfrak h[y]\) に \(1-2x=0\)、\(1-2y=0\) を課した例が与えられる。固定された環の中の可換環の商環、ここでは \(1/2\) の添加、が一意であることが障害になる。

必要十分条件は、\(\mathfrak O\) と \(\mathfrak o\) を含み、交わりが \(\mathfrak h\) であり、両者が元ごとに可換になる環 \(R\) が少なくとも一つ存在することである。この条件のもとで、双線形結合から作った \(\mathfrak T\) が直接積を与える。

続いて、\(\mathfrak O\) を \(\mathfrak h\) と生成系 \(S\) から作るとき、非可換多項式環 \(\mathfrak h[\ldots Z\ldots]\) から \(\mathfrak O\) への準同型の核として定義イデアル \(\mathfrak M\) が定義される。直接積が存在するとき、\(\mathfrak O_{\mathfrak o}\) の定義イデアルは、\(\mathfrak M\) を \(\mathfrak o[\ldots Z\ldots]\) へ拡張した \(\mathfrak M_{\mathfrak o}\) になる。

Simplified Chinese title: 直接积的存在条件与定义理想

为了说明直接积并不总是存在，文本给出 \(\mathfrak h[x]\) 与 \(\mathfrak h[y]\) 并分别满足 \(1-2x=0\)、\(1-2y=0\) 的例子。固定环中的交换环商环，此处即添加 \(1/2\)，具有唯一性，这是障碍所在。

必要且充分条件是：至少存在一个包含 \(\mathfrak O\) 与 \(\mathfrak o\) 的环 \(R\)，使二者交为 \(\mathfrak h\)，并且二者逐元可交换。在这个条件下，由双线性组合构成的 \(\mathfrak T\) 给出直接积。

随后，在 \(\mathfrak O\) 由 \(\mathfrak h\) 和生成系 \(S\) 生成时，把定义理想 \(\mathfrak M\) 定义为非交换多项式环 \(\mathfrak h[\ldots Z\ldots]\) 到 \(\mathfrak O\) 的同态核。若直接积存在，则 \(\mathfrak O_{\mathfrak o}\) 的定义理想就是把 \(\mathfrak M\) 扩张到 \(\mathfrak o[\ldots Z\ldots]\) 后的 \(\mathfrak M_{\mathfrak o}\)。

Script/codepoint and TeX/PDF notes:

- Records Quotientenring at line 20284 as localization-adjacent but not Lokalisierung.
- Nichtkommutativer Polynombereich is 非可換多項式環 / 非交换多项式环, draft-only.
- Keep \(\mathfrak M_{\mathfrak o}\) and quotient-ring formulas as TeX.

Unresolved flags:

- Localization remains blocked despite new Quotientenring evidence.
- Noncommutative polynomial-ring wording needs review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-14-005-independent-module-bases-and-extension-contraction

Anchor: German baseline lines `20333-20402`; §2 independent module bases and direct-product construction.

Source summary: Constructs direct products for rings with independent module bases, defines extension and contraction modules, and states a sufficient criterion via an auxiliary extension ring.

Japanese title: 独立加群基底と拡大・縮小加群

§2 は、独立な \(\mathfrak h\)-加群基底をもつ環で直接積を構成する。単位元を含む独立加群基底を \(\mathfrak O\) が持つなら、\(\mathfrak h\) の任意の拡大環 \(\mathfrak o\) に対して、\(\mathfrak O_{\mathfrak o}\) が存在する。

構成は、基底元 \(t_i\) と \(\mathfrak o\) の係数 \(\gamma_i\) による線形結合 \(\gamma_1t_{i_1}+\cdots+\gamma_rt_{i_r}\) を全体として環 \(\mathfrak R\) を作る、というものである。このとき \(T\) は同時に \(\mathfrak O_{\mathfrak o}\) の \(\mathfrak o\)-基底になる。

また、\(\mathfrak O\) の \(\mathfrak h\)-加群 \(\mathfrak B\) の拡大 \(\mathfrak B_{\mathfrak o}\) と、\(\mathfrak O_{\mathfrak o}\) の \(\mathfrak o\)-加群 \(\mathfrak C\) の縮小 \([\mathfrak C,\mathfrak O]\) が定義される。補助的な拡大環 \(\mathfrak f\) で直接積が存在すれば、もとの直接積の存在も導かれる。

Simplified Chinese title: 独立模基与扩张、收缩模

§2 在具有独立 \(\mathfrak h\)-模基的环中构造直接积。若 \(\mathfrak O\) 有一个含单位元的独立模基，则对 \(\mathfrak h\) 的任意扩张环 \(\mathfrak o\)，\(\mathfrak O_{\mathfrak o}\) 都存在。

构造方法是取基元素 \(t_i\) 与 \(\mathfrak o\) 中系数 \(\gamma_i\) 的线性组合 \(\gamma_1t_{i_1}+\cdots+\gamma_rt_{i_r}\)，形成环 \(\mathfrak R\)。此时 \(T\) 也成为 \(\mathfrak O_{\mathfrak o}\) 的 \(\mathfrak o\)-基。

同时定义 \(\mathfrak O\) 中 \(\mathfrak h\)-模 \(\mathfrak B\) 的扩张 \(\mathfrak B_{\mathfrak o}\)，以及 \(\mathfrak O_{\mathfrak o}\) 中 \(\mathfrak o\)-模 \(\mathfrak C\) 的收缩 \([\mathfrak C,\mathfrak O]\)。若借助某个辅助扩张环 \(\mathfrak f\) 已有相应直接积，则原来的直接积也存在。

Script/codepoint and TeX/PDF notes:

- Erweiterungsmodul/Verengungsmodul is 拡大加群・縮小加群 / 扩张模・收缩模, provisional.
- Independent module basis is 独立加群基底 / 独立模基.
- Keep bracket intersection notation \([\mathfrak C,\mathfrak O]\) in TeX.

Unresolved flags:

- Module-basis terminology needs review.
- No retained blocker closure.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-14-006-different-and-defining-equation

Anchor: German baseline lines `20403-20464`; §3 different, differential quotient, and defining equation.

Source summary: Defines the different of a commutative ring over a subring through a difference ideal and shows that in the one-equation case it is generated by G'(xi).

Japanese title: ディッフェレントと定義方程式

§3 からは可換環だけを扱う。対応する同型な拡大 \(\mathfrak O\) と \(\mathfrak o\) に対し、すべての差 \(x-\xi\) から作られる両側イデアル \(\mathfrak B\) を差分イデアルとする。零イデアルを \(\mathfrak B\) で割った \(\mathfrak A=(0):\mathfrak B\) が差分商である。

\(\mathfrak o\) の \(\mathfrak h\) に関するディッフェレント \(\mathfrak d\) は、\(\mathfrak A[x\to\xi]\) と定義される。すなわち、\(\mathfrak A\) の元に現れる \(x\) を対応する \(\xi\) で置き換える。同様に \(\mathfrak O\) のディッフェレント \(\mathfrak D\) は \(\mathfrak A[\xi\to x]\) で定まる。

定義イデアル \(\mathfrak M\) を用いると、微分商 \(\mathfrak M'\) は差分商から定まり、\(Z\to\xi\) によって \(\mathfrak d\) へ移る。特に定義方程式 \(G(z)=0\) があり、最高次係数が単位なら、ディッフェレントは主イデアル \((G'(\xi))\) で与えられ、\(\mathfrak M'=(G'(Z),G(Z))\) となる。

Simplified Chinese title: 不同式与定义方程

§3 起只讨论交换环。对相应同构的扩张 \(\mathfrak O\) 与 \(\mathfrak o\)，由所有差 \(x-\xi\) 生成的双边理想 \(\mathfrak B\) 称为差分理想。零理想除以 \(\mathfrak B\) 得到的 \(\mathfrak A=(0):\mathfrak B\) 是差分商。

\(\mathfrak o\) 相对于 \(\mathfrak h\) 的不同式 \(\mathfrak d\) 定义为 \(\mathfrak A[x\to\xi]\)，也就是把 \(\mathfrak A\) 中出现的 \(x\) 替换为相应的 \(\xi\)。类似地，\(\mathfrak O\) 的不同式 \(\mathfrak D\) 定义为 \(\mathfrak A[\xi\to x]\)。

利用定义理想 \(\mathfrak M\)，微分商 \(\mathfrak M'\) 由差分商确定，并在 \(Z\to\xi\) 时变为 \(\mathfrak d\)。特别地，若存在定义方程 \(G(z)=0\)，且最高项系数为单位，则不同式是由 \(G'(\xi)\) 生成的主理想，并且 \(\mathfrak M'=(G'(Z),G(Z))\)。

Script/codepoint and TeX/PDF notes:

- Hauptideal is 主イデアル / 主理想.
- G'(xi) should stay TeX to avoid apostrophe/codepoint confusion.
- Keep \(\mathfrak d=(G'(\xi))\), \(\mathfrak D=(G'(z))\), and \(\mathfrak M'=(G'(Z),G(Z))\) in TeX.

Unresolved flags:

- Different and differential-quotient terminology needs native/domain review.
- No retained blocker closure.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
