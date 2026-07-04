# Noether CJK Draft Corpus Translation Slices: Continuation 15

Generated UTC: `2026-07-04T08:26:21.009489+00:00`

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

- tensor product: no German Tensorprodukt anchor; Paper 43 §4 direct sum/direct product material is non-anchor evidence
- localization: Quotientenring candidates remain 16223-16225, 18467, 20105, 20228, 20240, and 20284, but no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: no new abstract-algebra anchor in Paper 43 §4
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in Paper 43 §4

## cjk-continuation-15-001-different-of-direct-sum-theorem

Anchor: German baseline lines `20465-20488`; §4 theorem on the different of a direct sum.

Source summary: Assumes O is a direct sum of ideals with independent component bases and states that the different of O over h is the direct sum of the component differents.

Japanese title: 直和のディッフェレント定理

§4 は、\(\mathfrak O\) がイデアルの直和 \(\mathfrak O=\mathfrak R_1+\cdots+\mathfrak R_r=\mathfrak Oe_1+\cdots+\mathfrak Oe_r\) に分かれる場合から始まる。ここで \(e_i\) は単位元の成分である。

各 \(\mathfrak R_i\) は、\(\mathfrak h_i=\mathfrak h e_i\) に関する独立な加群基底 \(T_i\) を持ち、この基底は \(\mathfrak R_i\) の単位元 \(e_i\) を含む。また \([\mathfrak h,\mathfrak S_i]\) は零元になる。

この仮定のもとで、\(\mathfrak O\) の \(\mathfrak h\) に関するディッフェレントは、各 \(\mathfrak R_i\) の \(\mathfrak h_i\) に関するディッフェレントの直和になる。

Simplified Chinese title: 直和的不同式定理

§4 从 \(\mathfrak O\) 分解为理想直和 \(\mathfrak O=\mathfrak R_1+\cdots+\mathfrak R_r=\mathfrak Oe_1+\cdots+\mathfrak Oe_r\) 的情形开始，其中 \(e_i\) 是单位元的分量。

每个 \(\mathfrak R_i\) 都有相对于 \(\mathfrak h_i=\mathfrak h e_i\) 的独立模基 \(T_i\)，且该基包含 \(\mathfrak R_i\) 的单位元 \(e_i\)。同时要求 \([\mathfrak h,\mathfrak S_i]\) 为零元。

在这些假设下，\(\mathfrak O\) 相对于 \(\mathfrak h\) 的不同式，等于各 \(\mathfrak R_i\) 相对于 \(\mathfrak h_i\) 的不同式的直和。

Script/codepoint and TeX/PDF notes:

- Direct sum is 直和 / 直和; it is not tensor-product evidence.
- Component of unity is 単位元の成分 / 单位元的分量.
- Keep \(\mathfrak Oe_i\), \(\mathfrak h_i=\mathfrak h e_i\), and \([\mathfrak h,\mathfrak S_i]\) in TeX.

Unresolved flags:

- Different terminology remains draft-only.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-15-002-bases-and-sharpened-intersection

Anchor: German baseline lines `20490-20524`; §4 proof facts I-II.

Source summary: Shows that the union of component bases gives an independent h-basis of O and proves a sharpened intersection property inside O_o.

Japanese title: 成分基底と強化された交わり条件

証明の第一段階では、各成分 \(\mathfrak R_i\) の基底 \(T_i\) の合併 \(T\) が、\(\mathfrak O\) の独立な \(\mathfrak h\)-基底になることを示す。\(x=xe_1+\cdots+xe_r\) と各成分での展開を使うと、\(T\) が実際に基底になる。

独立性は直和から従う。\(T\) の元の間に関係があれば、各 \(T_i\) の元の間の関係に分かれ、係数 \(h e_i\) がすべて零になる。仮定 \([\mathfrak h,\mathfrak S_i]=0\) により、係数 \(h\) 自体が零になる。

第二段階では、\(\mathfrak O_{\mathfrak o}\) 内で、\([\mathfrak o,\mathfrak S_{i(\mathfrak o)}]=0\) というより強い交わり性が得られる。これは、基底表示における係数比較から \(\alpha=\alpha e_i\) が補成分側にあるなら \(\alpha=0\) と結論するものである。

Simplified Chinese title: 分量基与强化交条件

证明的第一步表明，各分量 \(\mathfrak R_i\) 的基 \(T_i\) 的并 \(T\)，给出 \(\mathfrak O\) 的独立 \(\mathfrak h\)-基。利用 \(x=xe_1+\cdots+xe_r\) 以及各分量中的展开，即可得到 \(T\) 确为基。

独立性来自直和。若 \(T\) 的元素之间有关系，就分解为每个 \(T_i\) 中的关系，所有系数 \(h e_i\) 都为零。由假设 \([\mathfrak h,\mathfrak S_i]=0\)，可推出系数 \(h\) 本身为零。

第二步在 \(\mathfrak O_{\mathfrak o}\) 中得到更强的交性质：\([\mathfrak o,\mathfrak S_{i(\mathfrak o)}]=0\)。这是通过基表示中的系数比较，推出若 \(\alpha=\alpha e_i\) 落在补分量侧，则 \(\alpha=0\)。

Script/codepoint and TeX/PDF notes:

- Vereinigungsmenge is rendered as 合併 / 并.
- Koeffizientengleichheit is 係数比較 / 系数比较, descriptive.
- Keep \(\mathfrak S_{i(\mathfrak o)}\) in TeX.

Unresolved flags:

- Intersection-property wording needs review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-15-003-component-isomorphisms

Anchor: German baseline lines `20525-20555`; §4 proof facts III-IV.

Source summary: Derives ring isomorphisms between o and its components oe_i, then adds corresponding component isomorphisms after decomposing o.

Japanese title: 成分環の同型

第三段階では、\(\mathfrak o\) が、\(\mathfrak O\) の分解に対応する成分 \(\mathfrak o e_i\) と環同型であることが示される。\(e_i^2=e_i\) で、\(e_i\) は \(\mathfrak o\) のすべての元と可換なので、\(\mathfrak o e_i\) は \(\mathfrak o\) の環同型像になる。

この対応は一対一である。なぜなら \(\alpha\ne0\) なら、前段の強化交わり条件から \(\alpha e_i\ne0\) だからである。この対応のもとで、部分環 \(\mathfrak h\) には成分 \(\mathfrak h_i=\mathfrak h e_i\) が対応する。

さらに \(\mathfrak o=\mathfrak r_1+\cdots+\mathfrak r_r=\mathfrak o\varepsilon_1+\cdots+\mathfrak o\varepsilon_r\) という対応する分解を用いると、\(\mathfrak o\simeq\mathfrak o e_i\)、\(\mathfrak O\simeq\mathfrak O\varepsilon_i\)、\(\mathfrak r_i\simeq\mathfrak r_i e_i\)、\(\mathfrak R_i\simeq\mathfrak R_i\varepsilon_i\) などの同型が得られる。

Simplified Chinese title: 分量环同构

第三步说明，\(\mathfrak o\) 与对应于 \(\mathfrak O\) 分解的分量 \(\mathfrak o e_i\) 环同构。由于 \(e_i^2=e_i\)，且 \(e_i\) 与 \(\mathfrak o\) 的每个元素可交换，\(\mathfrak o e_i\) 成为 \(\mathfrak o\) 的环同构像。

这个对应是一一的，因为若 \(\alpha\ne0\)，由前一步强化交性质可得 \(\alpha e_i\ne0\)。在此对应下，子环 \(\mathfrak h\) 对应于分量 \(\mathfrak h_i=\mathfrak h e_i\)。

进一步利用相应分解 \(\mathfrak o=\mathfrak r_1+\cdots+\mathfrak r_r=\mathfrak o\varepsilon_1+\cdots+\mathfrak o\varepsilon_r\)，得到 \(\mathfrak o\simeq\mathfrak o e_i\)、\(\mathfrak O\simeq\mathfrak O\varepsilon_i\)、\(\mathfrak r_i\simeq\mathfrak r_i e_i\)、\(\mathfrak R_i\simeq\mathfrak R_i\varepsilon_i\) 等同构。

Script/codepoint and TeX/PDF notes:

- Idempotent components \(e_i\), \(\varepsilon_i\) must stay visually distinct.
- Ring isomorphism is 環同型 / 环同构.
- Keep chained isomorphism displays as TeX if promoted to TeX sidecar.

Unresolved flags:

- No retained blocker changes.
- Component notation needs TeX/PDF review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-15-004-null-ideal-quotients-under-direct-sum

Anchor: German baseline lines `20556-20575`; §4 proof fact V.

Source summary: Shows that the quotient of the zero ideal by an ideal decomposes componentwise under a direct sum, and that the statement also applies in O_o.

Japanese title: 零イデアル商の成分分解

第五段階では、直和表示から、零イデアルをイデアル \(\mathfrak B\) で割った商 \(\mathfrak C=(0):\mathfrak B\) が成分ごとに分解することを示す。

\(\mathfrak B\mathfrak C=(\mathfrak B e_1)(\mathfrak C e_1)+\cdots+(\mathfrak B e_r)(\mathfrak C e_r)=0\) なので、直和性により各成分で \((\mathfrak B e_i)(\mathfrak C e_i)=0\) が成り立つ。

逆に、成分 \(\mathfrak R_i\) の元が \((\mathfrak B e_i)(r e_i)=0\) を満たせば、それは全体の商に属する。したがって \(\mathfrak C_i=\mathfrak C e_i\) は、\(\mathfrak R_i\) における零イデアルの \(\mathfrak B_i\) による商になる。同じ主張は \(\mathfrak O_{\mathfrak o}\) のイデアルにも成り立つ。

Simplified Chinese title: 零理想商的分量分解

第五步由直和表示推出，零理想除以理想 \(\mathfrak B\) 所得的商 \(\mathfrak C=(0):\mathfrak B\) 可逐分量分解。

由于 \(\mathfrak B\mathfrak C=(\mathfrak B e_1)(\mathfrak C e_1)+\cdots+(\mathfrak B e_r)(\mathfrak C e_r)=0\)，直和性给出每个分量上的 \((\mathfrak B e_i)(\mathfrak C e_i)=0\)。

反过来，若分量 \(\mathfrak R_i\) 中的元素满足 \((\mathfrak B e_i)(r e_i)=0\)，它也属于整体的商。因此 \(\mathfrak C_i=\mathfrak C e_i\) 是 \(\mathfrak R_i\) 中零理想除以 \(\mathfrak B_i\) 的商。同样的结论也适用于 \(\mathfrak O_{\mathfrak o}\) 中的理想。

Script/codepoint and TeX/PDF notes:

- Quotient here is ideal quotient, not quotient ring/localization evidence.
- Keep \((0):\mathfrak B\) in TeX.
- No new localization source anchor is recorded from this slice.

Unresolved flags:

- Ideal-quotient wording needs review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-15-005-component-representation-of-different

Anchor: German baseline lines `20577-20603`; §4 proof facts VI-VII.

Source summary: Represents the different componentwise and identifies D e_i with the different of R_i after passing through R_i r_i and corresponding difference quotients.

Japanese title: ディッフェレントの成分表示

第六段階では、定義 \(\mathfrak D=\mathfrak A[\xi\to x]\) から、\(\mathfrak D=\mathfrak D e_1+\cdots+\mathfrak D e_r\) という成分表示を得る。\(e_i\) は \(\mathfrak O\) の元で自分自身に対応し、\(\varepsilon_i\) は同型によって \(e_i\) に移る。

したがって \(\mathfrak A e_i\varepsilon_i\) は、成分 \(\mathfrak R_i\mathfrak r_i\) の零イデアルを \(\mathfrak B e_i\varepsilon_i\) で割った商になる。ここでは \(\mathfrak O_{\mathfrak o}\) が \(\sum\mathfrak R_i\mathfrak r_k\) という直和に分解されることを使う。

第七段階では、\(\mathfrak D e_i=\mathfrak A e_i\varepsilon_i[\xi\to x]\) が、\(\mathfrak R_i\) の \(\mathfrak h_i\) に関するディッフェレントになることを示す。対応する対称的な主張として、\(\mathfrak d\varepsilon_i\) は \(\mathfrak r_i\) のディッフェレントになる。

Simplified Chinese title: 不同式的分量表示

第六步从定义 \(\mathfrak D=\mathfrak A[\xi\to x]\) 得到分量表示 \(\mathfrak D=\mathfrak D e_1+\cdots+\mathfrak D e_r\)。\(e_i\) 是 \(\mathfrak O\) 中的元素并对应于自身，而 \(\varepsilon_i\) 在同构下转为 \(e_i\)。

因此 \(\mathfrak A e_i\varepsilon_i\) 是分量 \(\mathfrak R_i\mathfrak r_i\) 中零理想除以 \(\mathfrak B e_i\varepsilon_i\) 的商。这里使用 \(\mathfrak O_{\mathfrak o}\) 分解为 \(\sum\mathfrak R_i\mathfrak r_k\) 的直和。

第七步说明，\(\mathfrak D e_i=\mathfrak A e_i\varepsilon_i[\xi\to x]\) 是 \(\mathfrak R_i\) 相对于 \(\mathfrak h_i\) 的不同式。对称地，\(\mathfrak d\varepsilon_i\) 是 \(\mathfrak r_i\) 的不同式。

Script/codepoint and TeX/PDF notes:

- Component representation is 成分表示 / 分量表示.
- Direct product in this proof remains 直接積 / 直接积 and non-tensor.
- Keep \(\mathfrak A e_i\varepsilon_i[\xi\to x]\) in TeX.

Unresolved flags:

- Different component terminology needs review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-15-006-direct-product-and-final-component-different

Anchor: German baseline lines `20604-20631`; §4 proof facts VIII-XI.

Source summary: Completes the proof by identifying R_i r_i as a direct product, computing its difference ideal and quotient, and concluding D e_i and d epsilon_i are component differents.

Japanese title: 直接積から成分ディッフェレントへの結論

第八段階では、\(\mathfrak R_i\mathfrak r_i\) が \(\mathfrak h e_i\varepsilon_i\) に関する直接積 \(\mathfrak R_i\varepsilon_i\times\mathfrak r_i e_i\) であることを示す。これは、\(\mathfrak R_i\) の基底 \(T_i\) と、対応する成分の同型から従う。

第九段階では、この直接積の差分イデアルが \(\mathfrak B e_i\varepsilon_i\)、差分商が \(\mathfrak A e_i\varepsilon_i\) であることを確認する。第十段階では、\(\mathfrak R_i\varepsilon_i\) のディッフェレントが \(\mathfrak D e_i\varepsilon_i\) になる。

最後に同型を戻すと、\(\mathfrak R_i\) のディッフェレントは \(\mathfrak D e_i\) である。よって \(\mathfrak D=\mathfrak D e_1+\cdots+\mathfrak D e_r\)、かつ各 \(\mathfrak D e_i\) が \(\mathfrak R_i\) のディッフェレントである。対称的に \(\mathfrak d=\mathfrak d\varepsilon_1+\cdots+\mathfrak d\varepsilon_r\) も得られる。

Simplified Chinese title: 从直接积到分量不同式的结论

第八步证明 \(\mathfrak R_i\mathfrak r_i\) 等于相对于 \(\mathfrak h e_i\varepsilon_i\) 的直接积 \(\mathfrak R_i\varepsilon_i\times\mathfrak r_i e_i\)。这由 \(\mathfrak R_i\) 的基 \(T_i\) 以及对应分量同构推出。

第九步确认，这个直接积的差分理想是 \(\mathfrak B e_i\varepsilon_i\)，差分商是 \(\mathfrak A e_i\varepsilon_i\)。第十步说明，\(\mathfrak R_i\varepsilon_i\) 的不同式等于 \(\mathfrak D e_i\varepsilon_i\)。

最后通过同构返回，\(\mathfrak R_i\) 的不同式就是 \(\mathfrak D e_i\)。于是 \(\mathfrak D=\mathfrak D e_1+\cdots+\mathfrak D e_r\)，且每个 \(\mathfrak D e_i\) 是 \(\mathfrak R_i\) 的不同式。对称地，也有 \(\mathfrak d=\mathfrak d\varepsilon_1+\cdots+\mathfrak d\varepsilon_r\)。

Script/codepoint and TeX/PDF notes:

- Direct product is not tensor product; retain blocker.
- Difference ideal/difference quotient terms follow C14.
- Keep \(\mathfrak R_i\varepsilon_i\times\mathfrak r_i e_i\), \(\mathfrak D e_i\), and \(\mathfrak d\varepsilon_i\) in TeX.

Unresolved flags:

- No retained blocker changes.
- Component different terms need native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
