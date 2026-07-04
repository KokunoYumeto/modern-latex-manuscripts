# Noether CJK Draft Corpus Translation Slices: Continuation 17

Generated UTC: `2026-07-04T08:35:20.603879+00:00`

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

- tensor product: no German Tensorprodukt anchor; Paper 43 §6 direct product language is non-anchor evidence
- localization: Quotientenring candidates now include 16223-16225, 18467, 20105, 20228, 20240, 20284, and 20949, plus Quotientenkörper at 20822; no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: no new abstract-algebra anchor in Paper 43 §6
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in Paper 43 §6

## cjk-continuation-17-001-orders-and-galois-extension-ring-of-order

Anchor: German baseline lines `20817-20831`; §6.1 underlying rings for the different of an order.

Source summary: Refines the field structure theorems to orders, assumes h is integrally closed in P with P its quotient field, and defines the Galois extension ring of an order.

Japanese title: 整環とその Galois 拡大環

§6 は、体とその Galois 拡大環についての構造定理を、整数性の方向へ強める。\(P\) の部分環 \(\mathfrak h\) を取り、\(P\) が \(\mathfrak h\) の商体であり、\(\mathfrak h\) が \(P\) の中で整閉であると仮定する。

\(\mathfrak O\) は \(\mathfrak K\) の中の \(\mathfrak h\)-整環である。すなわち \(\mathfrak h\) を含む部分環で、商体が \(\mathfrak K\) になり、有限な \(\mathfrak h\)-加群基底を持つ。\(\mathfrak o\) は \(K\) の中の対応する整環、\(\mathfrak o^{(i)}\) はその共役整環である。

§2 の十分条件により、直接積 \(\mathfrak O_{\mathfrak o}\) と \(\mathfrak O_{\mathfrak g}\) が存在する。ここで \(\mathfrak g\) は共役整環が \(\Gamma\) の中で生成する整環であり、\(\mathfrak O_{\mathfrak g}\) は整環 \(\mathfrak O\) の Galois 拡大環と呼ばれる。

Simplified Chinese title: 阶及其 Galois 扩张环

§6 把关于域及其 Galois 扩张环的结构定理，按整性加以强化。取 \(P\) 的子环 \(\mathfrak h\)，假设 \(P\) 是 \(\mathfrak h\) 的商域，并且 \(\mathfrak h\) 在 \(P\) 中整闭。

\(\mathfrak O\) 是 \(\mathfrak K\) 中的 \(\mathfrak h\)-阶，即含有 \(\mathfrak h\) 的子环，其商域为 \(\mathfrak K\)，并具有有限 \(\mathfrak h\)-模基。\(\mathfrak o\) 是 \(K\) 中对应的阶，\(\mathfrak o^{(i)}\) 是其共轭阶。

由 §2 的充分条件，直接积 \(\mathfrak O_{\mathfrak o}\) 与 \(\mathfrak O_{\mathfrak g}\) 存在。这里 \(\mathfrak g\) 是共轭阶在 \(\Gamma\) 中生成的阶，而 \(\mathfrak O_{\mathfrak g}\) 称为阶 \(\mathfrak O\) 的 Galois 扩张环。

Script/codepoint and TeX/PDF notes:

- Quotient field at line 20822 is recorded as 商体 / 商域, not localization closure.
- Order remains 整環 / 阶 per earlier draft convention.
- Keep \(\mathfrak O_{\mathfrak g}\), \(\mathfrak o^{(i)}\), and \(\mathfrak g_P=\Gamma\) in TeX.

Unresolved flags:

- Order terminology remains draft-only.
- Localization remains blocked: quotient-field wording is not Lokalisierung.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-17-002-difference-ideals-and-differents-of-conjugate-orders

Anchor: German baseline lines `20832-20861`; §6.1 definitions of difference ideals and differents of orders.

Source summary: Defines the difference ideals, difference quotients, and differents for O, o, and the conjugate orders o^(i), noting relative and function-field applicability.

Japanese title: 共役整環の差分商とディッフェレント

この設定で、\(\mathfrak O\) と \(\mathfrak o\) の \(\mathfrak h\) に関するディッフェレントが定義される。差分イデアル \(\mathfrak B=\{\ldots,y-\eta,\ldots\}\) は \(\mathfrak O_{\mathfrak o}\) の中で取られ、共役版 \(\mathfrak B^{(i)}\) は \(\mathfrak O_{\mathfrak o^{(i)}}\) の中で取られる。

対応する差分商は \(\mathfrak A^{(i)}=(0):\mathfrak B^{(i)}\)、特に \(\mathfrak A=(0):\mathfrak B\) である。これらから \(\mathfrak D=\mathfrak A[\eta\to y]\)、\(\mathfrak d^{(i)}=\mathfrak A^{(i)}[y\to\eta^{(i)}]\)、特に \(\mathfrak d=\mathfrak A[y\to\eta]\) が得られる。

注では、この仮定のもとで任意の整環のディッフェレントと相対ディッフェレント、さらに多変数の代数関数体におけるディッフェレントも定義できる、と説明される。

Simplified Chinese title: 共轭阶的差分商与不同式

在这个设置下，\(\mathfrak O\) 与 \(\mathfrak o\) 相对于 \(\mathfrak h\) 的不同式得以定义。差分理想 \(\mathfrak B=\{\ldots,y-\eta,\ldots\}\) 取在 \(\mathfrak O_{\mathfrak o}\) 中，共轭版本 \(\mathfrak B^{(i)}\) 取在 \(\mathfrak O_{\mathfrak o^{(i)}}\) 中。

相应差分商为 \(\mathfrak A^{(i)}=(0):\mathfrak B^{(i)}\)，特别地 \(\mathfrak A=(0):\mathfrak B\)。由此得到 \(\mathfrak D=\mathfrak A[\eta\to y]\)、\(\mathfrak d^{(i)}=\mathfrak A^{(i)}[y\to\eta^{(i)}]\)，以及 \(\mathfrak d=\mathfrak A[y\to\eta]\)。

注中说明，在这些假设下，可以定义任意阶的不同式和相对不同式，也可以定义多元代数函数域中的不同式。

Script/codepoint and TeX/PDF notes:

- Relative different is 相対ディッフェレント / 相对不同式.
- Difference quotient continues 差分商 / 差分商.
- Keep substitution notation \([\eta\to y]\) and \([y\to\eta]\) in TeX.

Unresolved flags:

- Relative-different terminology needs review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-17-003-structure-theorem-for-galois-extension-ring-of-orders

Anchor: German baseline lines `20863-20889`; §6.2 structure theorem for Galois extension rings of orders.

Source summary: Relates difference ideals and quotients for orders and fields, proving A = d e^(1) and characterizing d by membership of x e^(1) in O_o.

Japanese title: 整環の Galois 拡大環の構造定理

整環の Galois 拡大環についての構造定理は、整環の場合の差分イデアル・差分商と体の場合のそれらを結びつける。体での \(\mathfrak B_K\) は \(\mathfrak O_{\mathfrak o}\) の差分イデアル \(\mathfrak B\) の拡大であり、\(\mathfrak A_K\) も \(\mathfrak A\) の拡大である。

差分商、ディッフェレント、単位成分の間には \(\mathfrak A=\mathfrak d e^{(1)}\)、\(\mathfrak A^{(i)}=\mathfrak d^{(i)}e^{(i)}\) が成り立つ。したがって \(\mathfrak d=[\mathfrak o,\mathfrak A^{(1)}+\cdots+\mathfrak A^{(n)}]\) と表される。

さらに \(\mathfrak d\) は、\(x e^{(1)}\) が \(\mathfrak O_{\mathfrak o}\) に属するような \(K\) の元 \(x\) 全体である。これは零イデアルではなく、\(P\) に関して階数 \(n\) を持つ。

Simplified Chinese title: 阶的 Galois 扩张环结构定理

关于阶的 Galois 扩张环的结构定理，把阶情形中的差分理想、差分商与域情形中的对应对象联系起来。域中的 \(\mathfrak B_K\) 是 \(\mathfrak O_{\mathfrak o}\) 中差分理想 \(\mathfrak B\) 的扩张，\(\mathfrak A_K\) 也是 \(\mathfrak A\) 的扩张。

差分商、不同式与单位分量之间满足 \(\mathfrak A=\mathfrak d e^{(1)}\)、\(\mathfrak A^{(i)}=\mathfrak d^{(i)}e^{(i)}\)。因此 \(\mathfrak d=[\mathfrak o,\mathfrak A^{(1)}+\cdots+\mathfrak A^{(n)}]\)。

进一步，\(\mathfrak d\) 是 \(K\) 中所有使 \(x e^{(1)}\) 属于 \(\mathfrak O_{\mathfrak o}\) 的元素 \(x\) 所成的集合。它不是零理想，并且相对于 \(P\) 具有秩 \(n\)。

Script/codepoint and TeX/PDF notes:

- Component of unity is 単位成分 / 单位分量.
- Rang n is 階数 n / 秩 n.
- Keep \(\mathfrak A=\mathfrak d e^{(1)}\) and \(\mathfrak d=[\mathfrak o,\ldots]\) in TeX.

Unresolved flags:

- Structure-theorem terminology remains draft-only.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-17-004-complementary-module-and-trace-definition

Anchor: German baseline lines `20891-20917`; §6.3 sketch: complementary module and trace definition.

Source summary: In the sketch portion, relates the different to the quotient o:c by the complementary module and gives the trace-based definition of the complementary module.

Japanese title: 補加群と跡による定義

ここからは原稿で「スケッチ」とされる。独立な \(\mathfrak h\)-基底 \(t_1,\ldots,t_n\) が \(\mathfrak O\) にあるとき、補基の変換公式 \((S)=P^{-1}(T)\) により、補基は同じ \(\mathfrak h\)-加群を張る。この加群が \(\mathfrak O\) の補加群である。

構造定理の結論から、\(\mathfrak d\) は \(K\) における商 \(\mathfrak o:\mathfrak c\) になる。ここで \(\mathfrak c\) は補加群である。実際、\(e^{(1)}=A_1t_1+\cdots+A_nt_n\) とし、\(A_i\) が \(\mathfrak c\) の基底なら、\(\delta e^{(1)}\in\mathfrak O_{\mathfrak o}\) は \(\delta A_i\in\mathfrak o\) と同値である。

規則的な整環で \(e,z,\ldots,z^{n-1}\) が基底なら、\(\mathfrak d=\{f'(z)\}\) となる。さらに補加群は、任意の \(t\in\mathfrak O\) に対して \(\operatorname{Sp}(ct)\) が \(\mathfrak h\) に入るような \(c\in\mathfrak K\) 全体としても定義できる。

Simplified Chinese title: 补模与迹定义

从这里开始手稿标为“草略”。若 \(\mathfrak O\) 有独立 \(\mathfrak h\)-基 \(t_1,\ldots,t_n\)，则补基的变换公式 \((S)=P^{-1}(T)\) 表明，补基张成同一个 \(\mathfrak h\)-模；这个模就是 \(\mathfrak O\) 的补模。

由结构定理的结论，\(\mathfrak d\) 等于 \(K\) 中的商 \(\mathfrak o:\mathfrak c\)，其中 \(\mathfrak c\) 是补模。若 \(e^{(1)}=A_1t_1+\cdots+A_nt_n\)，且 \(A_i\) 是 \(\mathfrak c\) 的基，则 \(\delta e^{(1)}\in\mathfrak O_{\mathfrak o}\) 等价于 \(\delta A_i\in\mathfrak o\)。

在正则阶且 \(e,z,\ldots,z^{n-1}\) 为基的特例中，\(\mathfrak d=\{f'(z)\}\)。另外，补模也可定义为所有 \(c\in\mathfrak K\)，使得对任意 \(t\in\mathfrak O\)，\(\operatorname{Sp}(ct)\) 都落在 \(\mathfrak h\) 中。

Script/codepoint and TeX/PDF notes:

- The source marks this as a sketch; preserve that uncertainty.
- Komplementärmodul is 補加群 / 补模.
- Keep \(\mathfrak o:\mathfrak c\), \(\{f'(z)\}\), and \(\operatorname{Sp}\) in TeX.

Unresolved flags:

- Complementary-module and regular-order terminology needs review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-17-005-difference-quotient-as-intersection-of-other-difference-ideals

Anchor: German baseline lines `20919-20945`; §6.3 addendum on difference quotients as intersections.

Source summary: Adds that when an independent module basis exists, A^(i) is the intersection of all difference ideals except B^(i), after contraction from the Galois extension ring.

Japanese title: 差分商を他の差分イデアルの交わりとして見る補足

補足として、整環に独立な \(\mathfrak h\)-加群基底が存在するとき、差分商 \(\mathfrak A^{(i)}\) は \(\mathfrak B^{(i)}\) 以外のすべての差分イデアルの交わりとして表せる、と述べられる。

これは、\(\mathfrak B\) が \(\mathfrak B_K\) の縮小イデアルになること、さらに \(\mathfrak A_\Gamma\) が他の共役差分イデアルの交わりであることから従う。

したがって、\(\mathfrak A=[\mathfrak O_{\mathfrak o},\mathfrak B_\mathfrak g^{(2)},\ldots,\mathfrak B_\mathfrak g^{(n)}]\) という形で、整環側の差分商を Galois 拡大環側の差分イデアルの交わりから取り戻す。

Simplified Chinese title: 把差分商看作其他差分理想之交的补充

补充说明：当阶中存在独立 \(\mathfrak h\)-模基时，差分商 \(\mathfrak A^{(i)}\) 可表示为除 \(\mathfrak B^{(i)}\) 外所有差分理想的交。

这是因为 \(\mathfrak B\) 成为 \(\mathfrak B_K\) 的收缩理想，而 \(\mathfrak A_\Gamma\) 是其他共轭差分理想的交。

于是可写成 \(\mathfrak A=[\mathfrak O_{\mathfrak o},\mathfrak B_\mathfrak g^{(2)},\ldots,\mathfrak B_\mathfrak g^{(n)}]\)，从 Galois 扩张环中的差分理想交，恢复阶一侧的差分商。

Script/codepoint and TeX/PDF notes:

- Intersection brackets are dense; preserve TeX and avoid line wrapping inside macros.
- Use 縮小イデアル / 收缩理想 for Verengungsideal.
- Keep \(\mathfrak B_\mathfrak g^{(i)}\) notation in TeX.

Unresolved flags:

- No retained blocker changes.
- Dense intersection notation needs TeX/PDF review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-17-006-fundamental-equation-and-quotient-ring-caveat

Anchor: German baseline lines `20946-20950`; §6.4 fundamental equation and differential quotient.

Source summary: Relates the different to a fundamental equation after adjoining indeterminates and passing to a quotient ring by primitive polynomials, while recording a manuscript caveat about the exactness of G'(U).

Japanese title: 基本方程式と商環に関する留保

§6 の最後では、整環 \(\mathfrak O\) に不定元 \(u_1,\ldots,u_n\) を添加して直接積 \(\mathfrak O_U=\mathfrak O[u_1,\ldots,u_n]\) を作る場合を考える。

基本方程式が存在するとは、原始多項式 \(H(u)\) による商環へ移ったとき、\(e,U,\ldots,U^{n-1}\) が \(\mathfrak h\)-加群基底になる、ということである。このとき \(\mathfrak O_U\) には定義方程式 \(G(U)=0\) が存在し、\(G'(U)\) がディッフェレントの基底多項式になる。

ただし本文は、\((G'(U))\) が本当に \(\mathfrak D_U\) だけを与えるかは、さらに正確に示す必要がある、と留保する。この `Quotientenring' 言及は局所化 row の直接証拠ではなく、`Lokalisierung' ラベルもない。

Simplified Chinese title: 基本方程与商环留保

§6 末尾考虑给阶 \(\mathfrak O\) 添加不定元 \(u_1,\ldots,u_n\)，形成直接积 \(\mathfrak O_U=\mathfrak O[u_1,\ldots,u_n]\) 的情形。

所谓存在基本方程，是指在过渡到由原始多项式 \(H(u)\) 给出的商环后，\(e,U,\ldots,U^{n-1}\) 成为 \(\mathfrak h\)-模基。这时 \(\mathfrak O_U\) 中有定义方程 \(G(U)=0\)，而 \(G'(U)\) 成为不同式的基多项式。

不过文本保留说明：\((G'(U))\) 是否真的只给出 \(\mathfrak D_U\)，还需要更精确地证明。这里的 `Quotientenring' 提法不是 localization 行的直接证据，也没有 `Lokalisierung' 标签。

Script/codepoint and TeX/PDF notes:

- Records Quotientenring at line 20949 as localization-adjacent but not Lokalisierung.
- Fundamental equation is 基本方程式 / 基本方程, provisional.
- Keep \(G'(U)\), \(\mathfrak D_U\), and \(\mathfrak O_U\) in TeX.

Unresolved flags:

- Localization remains blocked despite this quotient-ring passage.
- The manuscript caveat about \(G'(U)\) should stay visible in downstream artifacts.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
