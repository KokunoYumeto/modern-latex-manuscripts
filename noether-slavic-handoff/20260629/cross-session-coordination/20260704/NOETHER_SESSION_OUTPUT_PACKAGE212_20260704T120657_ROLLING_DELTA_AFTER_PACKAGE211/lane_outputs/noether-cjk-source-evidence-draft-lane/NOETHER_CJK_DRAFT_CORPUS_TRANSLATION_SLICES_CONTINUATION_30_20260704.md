# Noether CJK Draft Corpus Translation Slices: Continuation 30

Generated UTC: `2026-07-04T10:04:09.940645+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical Japanese and Simplified Chinese corpus slices. Not native reviewed. Not approved. No gate promotion.

Korean remains source-discovery/crosswalk only in this continuation.

## Metadata

- Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Coverage: Continuation 30 covers German baseline 23193-23324, completing Deuring lecture Chapter VI §27 before §28 begins at 23325.
- Slice count: `6`

## Slices

### cjk-continuation-30-001-chapter-vi-crossed-products-and-satz-1

- German anchor: `23193-23203`
- Source summary: Opens Chapter VI on crossed products. The theory developed from factor systems in §24 is re-founded independently. Satz 1 says that if beta is a Galois splitting field/maximal commutative subfield of R_r with Galois group, then R_r is the crossed product; conversely every such crossed product yields an R_r. Definitions give the direct sum with relations z u_S = u_S z^S and u_S u_T = a_S,T u_ST, and the generating group G*.
- Japanese title: 交叉積としての第 VI 章の出発点
- Simplified Chinese title: 第 VI 章从交叉积出发

**Japanese Draft**

第 VI 章は「交叉積の理論」を扱う。§24 で因子系から展開された交叉積の理論を、ここではあらためて独立に基礎づける。重要なのは、Galois 体とその群を同時に \(\Re_\tau\) の中で記述する点である。

定理 1 は、\(\beta\) が \(\Re_r\) の Galois 的分解体、すなわち極大可換部分体であり、\(\Im\) がその Galois 群であるなら、\(\Re_r\) は交叉積 \(\Im\cdot\Im\) に等しい、という主張である。逆に、任意の交叉積 \(\Im\cdot\Im\) はこの種の \(\Re_r\) を生む。

定義では、\(\mathfrak K_r=\mathfrak J u_E+\cdots+\mathfrak J u_T\) と書き、関係式 \(zu_S=u_Sz^S\)、\(u_Su_T=a_{S,T}u_{ST}\) を置く。ここで \(a_{S,T}\) は小因子系である。また、\(\mathfrak G^*\) は、変換により \(\Im\) 全体を自分自身へ移す正則元全体として定義される。

**Simplified Chinese Draft**

第 VI 章讨论“交叉积理论”。§24 中从因子系发展出的交叉积理论，在这里重新作独立的奠基。其意义在于把一个 Galois 域及其群同时描述在 \(\Re_\tau\) 中。

定理 1 说：若 \(\beta\) 是 \(\Re_r\) 的 Galois 分裂域，即极大交换子域，而 \(\Im\) 是其 Galois 群，则 \(\Re_r\) 等于交叉积 \(\Im\cdot\Im\)。反过来，每个这样的交叉积都产生这种 \(\Re_r\)。

定义中写成 \(\mathfrak K_r=\mathfrak J u_E+\cdots+\mathfrak J u_T\)，并规定关系 \(zu_S=u_Sz^S\)、\(u_Su_T=a_{S,T}u_{ST}\)。其中 \(a_{S,T}\) 是小因子系。生成群 \(\mathfrak G^*\) 则定义为所有通过变换把 \(\Im\) 整体变到自身的正则元素。

**Script/TeX Notes**

- Preserve \(\Re_\tau\), \(\Im\cdot\Im\), \(zu_S=u_Sz^S\), and \(u_Su_T=a_{S,T}u_{ST}\).
- Verschränktes Produkt is drafted as 交叉積 / 交叉积; native/domain review required before canonical use.
- The baseline uses OCR-unstable field/group glyphs; draft keeps source TeX tokens in formulas.

**Unresolved Flags**

- Lines 23199-23203 contain OCR drift in \(\Im\), \(\mathfrak J\), and group-star notation; source-image review needed.
- Crossed-product terminology is provisional and not a glossary approval.

### cjk-continuation-30-002-direct-sum-rank-and-generating-group-quotient

- German anchor: `23205-23243`
- Source summary: Proves the representation as a crossed product. Elements u_E,...,u_T generate automorphisms, and the sum of beta u_S is direct; rank agreement then gives R_r. It also proves that the Galois group is isomorphic to the quotient of the generating group by the multiplicative group of the field: only field elements induce the identity by transformation.
- Japanese title: 直和性・階数計算・生成群の商
- Simplified Chinese title: 直和性、秩计算与生成群商

**Japanese Draft**

交叉積としての表示を示すため、まず自己同型 \(E,\ldots,T\) を生成する元 \(u_E,u_S,\ldots,u_T\) を取り、\(zu_S=u_Sz^S\)、特に \(u_E=e\) とする。示すべきことは、和 \(\mathfrak M=\{\mathfrak Z u_E,\ldots,\mathfrak Z u_T\}\) が直和であること、そして階数が一致するため \(\Re_r\) 全体に等しいことである。

この直和性は、\(\mathfrak M\) が \(\mathfrak Z\) の左右加群、すなわち \(\mathfrak Z\) の表現加群として \(n\) 個の異なる表現を生む、という階数の議論で説明される。

次に \(\mathfrak G\cong\mathfrak G^*/\mathfrak F^*\) を示す。すなわち、変換で基礎体に恒等写像を誘導するのは、その体の元だけである。\(t=z_0+z_1u_S+\cdots+z_{n-1}u_T\) と展開し、すべての \(z\) と可換であることから、非自明な係数が消える。

**Simplified Chinese Draft**

为了证明交叉积表示，先取生成自同构 \(E,\ldots,T\) 的元素 \(u_E,u_S,\ldots,u_T\)，使 \(zu_S=u_Sz^S\)，特别有 \(u_E=e\)。需要证明的是，和 \(\mathfrak M=\{\mathfrak Z u_E,\ldots,\mathfrak Z u_T\}\) 是直和；再由秩相同推出它等于整个 \(\Re_r\)。

直和性通过以下秩论证说明：\(\mathfrak M\) 是 \(\mathfrak Z\) 的左右模，也就是 \(\mathfrak Z\) 的表示模，并产生 \(n\) 个不同的表示。

随后证明 \(\mathfrak G\cong\mathfrak G^*/\mathfrak F^*\)：也就是说，通过变换在基域上诱导恒等映射的只有该域自身的元素。把 \(t=z_0+z_1u_S+\cdots+z_{n-1}u_T\) 展开，并利用它与所有 \(z\) 可交换，可推出所有非平凡系数都为零。

**Script/TeX Notes**

- Preserve \(\mathfrak M=\{\mathfrak Z u_E,\dots,\mathfrak Z u_T\}\), \(\mathfrak G\cong\mathfrak G^*/\mathfrak F^*\), and \(t=z_0+z_1u_S+\cdots\).
- Direkte Summe is rendered as 直和 / 直和; Rank as 階数 / 秩.
- The quotient-group notation has OCR drift but the structural statement is clear enough for draft prose.

**Unresolved Flags**

- Lines 23212-23216 and 23223 have mixed \(\mathfrak Z\), \(\mathfrak F\), and \(\Im\) glyphs needing source-image review.
- The Schwarz attribution at line 23214 is recorded only as source context.

### cjk-continuation-30-003-multiplication-laws-and-converse-crossed-product-ring

- German anchor: `23245-23289`
- Source summary: Shows the u elements satisfy multiplication laws u_S u_T = a_S,T u_ST and the twisted associativity relation for the small factor system. Then conversely declares the direct sum into a ring by the crossed relations; if the associativity relations hold, the result is an associative ring. Umkehrsatz 2 begins: the crossed product is two-sided simple with center P.
- Japanese title: 乗法法則と交叉積環の逆構成
- Simplified Chinese title: 乘法律与交叉积环的逆构造

**Japanese Draft**

第三に、元 \(u_S\) は \(u_Su_T=a_{S,T}u_{ST}\) という乗法法則を満たす。さらに小因子系 \(a_{S,T}\) は、\(a_{R,S}a_{RS,T}=a_{S,T}^{R-1}a_{R,ST}\) という歪んだ結合法則を満たす。

本文の該当箇所には長い OCR 重複があるが、構造的な議論は、\(u_Ra_{S,T}u_{ST}\) と \(a_{R,S}u_{RS}u_T\) を同じ \(u_{RST}\) の係数として比較するものである。

逆向きには、直和 \(\mathfrak M=\mathfrak Z u_E+\cdots+\mathfrak Z u_T\) に関係式 \(zu_S=u_Sz^S\)、\(u_Su_T=a_{S,T}u_{ST}\) を入れて環とする。\(a_{S,T}\) が歪結合法則を満たすなら、積は一意に定まり、\(\mathfrak M\) は結合的な環になる。続いて、交叉積が中心 \(P\) を持つ両側単純環であることを示す逆定理が始まる。

**Simplified Chinese Draft**

第三，元素 \(u_S\) 满足乘法律 \(u_Su_T=a_{S,T}u_{ST}\)。并且小因子系 \(a_{S,T}\) 满足扭结合法则 \(a_{R,S}a_{RS,T}=a_{S,T}^{R-1}a_{R,ST}\)。

该处正文有很长的 OCR 重复，但结构性论证是把 \(u_Ra_{S,T}u_{ST}\) 与 \(a_{R,S}u_{RS}u_T\) 都作为同一个 \(u_{RST}\) 的系数来比较。

反过来，把直和 \(\mathfrak M=\mathfrak Z u_E+\cdots+\mathfrak Z u_T\) 通过关系 \(zu_S=u_Sz^S\)、\(u_Su_T=a_{S,T}u_{ST}\) 定为一个环。若 \(a_{S,T}\) 满足扭结合法则，则乘法唯一确定，\(\mathfrak M\) 成为结合环。随后开始逆定理：该交叉积是中心为 \(P\) 的双侧单环。

**Script/TeX Notes**

- Preserve \(u_Su_T=a_{S,T}u_{ST}\) and \(a_{R,S}a_{RS,T}=a_{S,T}^{R-1}a_{R,ST}\).
- Line 23257 is heavily OCR-damaged with repeated \(\mathfrak Z^*\)-like tokens; draft keeps only the structural consequence.
- Zweiseitig einfach is drafted as 両側単純 / 双侧单.

**Unresolved Flags**

- Line 23257 needs source-image review before any exact symbolic transcription.
- The crossed-associativity formula should be checked against the original page for exponent placement.

### cjk-continuation-30-004-lemmas-on-centralizers-and-bimodules

- German anchor: `23291-23305`
- Source summary: Gives the first three lemmas for Umkehrsatz 2. Lemma 1: every element commuting elementwise with the maximal subfield belongs to that subfield. Lemma 2: every beta-bimodule double-isomorphic to beta u_S is identical with beta u_S. Lemma 3: every beta-bimodule in the crossed product is a sum of beta u_S terms for selected S.
- Japanese title: 中心化元と双加群に関する補題
- Simplified Chinese title: 关于中心化元素与双模的补题

**Japanese Draft**

逆定理 2 の証明は補題から始まる。補題 1 は、極大可換部分体と元ごとに可換な任意の元は、その部分体に属する、という内容である。展開 \(w=\sum c_{\lambda_S}u_S\) を用い、非恒等の \(S\) に対する係数が消えることを示す。

補題 2 は、\(\beta u_S\) と双同型な \(\beta\)-双加群は、実際には \(\beta u_S\) と同一である、という主張である。証明では、同型を表す元 \(a\) と関係 \(za=az^S\) を用い、補題 1 に帰着する。

補題 3 は、交叉積内の任意の \(\beta\)-双加群が、いくつかの異なる \(S\) に対する和 \(\beta u_{S_1}+\cdots+\beta u_{S_k}\) の形になる、という分解を述べる。これは完全可約性と、各和因子が異なる双同型類に属することから従う。

**Simplified Chinese Draft**

逆定理 2 的证明从几个补题开始。补题 1 说，凡与极大交换子域逐元素可交换的元素，都属于该子域。利用展开 \(w=\sum c_{\lambda_S}u_S\)，可证明非恒等 \(S\) 的系数全都消失。

补题 2 说，与 \(\beta u_S\) 双同构的 \(\beta\)-双模，实际上就等同于 \(\beta u_S\)。证明使用表示同构的元素 \(a\) 以及关系 \(za=az^S\)，并归结到补题 1。

补题 3 则说明，交叉积中的任一 \(\beta\)-双模都具有 \(\beta u_{S_1}+\cdots+\beta u_{S_k}\) 的形式，其中取若干个不同的 \(S\)。这是由完全可约性以及各直和因子属于不同双同构类得到的。

**Script/TeX Notes**

- Preserve \(w=\sum c_{\lambda_S}u_S\), \(za=az^S\), and \(\beta u_{S_1}+\cdots+\beta u_{S_k}\).
- Doppelmodul is drafted as 双加群 / 双模.
- Voll-reduzibel is drafted as 完全可約 / 完全可约.

**Unresolved Flags**

- Lines 23293-23305 contain mixed beta/\(\Im\)/\(\mathcal Z\) glyphs; source-image review needed.
- Double-isomorphism terminology needs domain/native review.

### cjk-continuation-30-005-two-sided-simplicity-center-and-infinite-galois-remark

- German anchor: `23307-23321`
- Source summary: Lemma 4: every ring containing the maximal subfield in the crossed product, especially the crossed product itself, is two-sided simple; subrings containing the field correspond to subgroups. Lemma 5: P is the center. Remark 1 says the theorem also holds for an infinite algebraic Galois field over P, with a finiteness condition on sums.
- Japanese title: 両側単純性・中心・無限 Galois 体への注
- Simplified Chinese title: 双侧单性、中心与无限 Galois 域情形

**Japanese Draft**

補題 4 は、\(\Im\) を含む交叉積内の任意の環、特に交叉積自身が両側単純である、と述べる。さらに、\(\Im\) を含む部分環は \(\Im\) の部分群と一対一に対応する。

補題 5 は、交叉積の中心が \(P\) であることを示す。交叉積全体と可換な元は、とくに \(\beta\) と可換なので補題 1 により \(\beta\) に属し、さらに \(wu_S=u_Sw^S\) からすべての \(S\) で不変、したがって \(P\) に属する。

注 1 では、この証明が \(\Im\) が \(\mathsf P\) 上の無限代数的 Galois 体である場合にも成り立つ、と述べる。ただしその場合、交叉積は有限和全体として扱われ、部分環については追加の仮定が必要になる。

**Simplified Chinese Draft**

补题 4 说，在交叉积中包含 \(\Im\) 的任意环，特别是交叉积本身，都是双侧单的。并且，包含 \(\Im\) 的子环与 \(\Im\) 的子群一一对应。

补题 5 证明交叉积的中心是 \(P\)。与整个交叉积可交换的元素，特别与 \(\beta\) 可交换，故由补题 1 属于 \(\beta\)；再由 \(wu_S=u_Sw^S\) 可知它对所有 \(S\) 不变，因此属于 \(P\)。

注 1 说明，这个定理在 \(\Im\) 是 \(\mathsf P\) 上无限代数 Galois 域时仍成立。但此时交叉积要作为所有有限和组成的系统来处理，对子环还需附加条件。

**Script/TeX Notes**

- Preserve \(wu_S=u_Sw^S\), \(w=w^S\), and finite-sum notation \(\sum_{S_i}u_{S_\lambda}c_{S_\lambda}\).
- Zentrum is 中心 in both languages; zweiseitig einfach remains 両側単純 / 双侧单.
- Do not normalize Krull Zahlringe citation or Math. Ann. reference beyond source note.

**Unresolved Flags**

- Lines 23307-23321 have severe OCR glyph substitutions for \(\Im\), \(\mathfrak Z\), and subgroup symbols.
- Subring-subgroup correspondence wording needs domain review.

### cjk-continuation-30-006-representation-theory-remark-and-section-28-boundary

- German anchor: `23323-23324`
- Source summary: Remark 2 connects the direct foundation back to the twisted matrix-representation theory of §§25/26. It notes that §28 uses the fact that the irreducible twisted representation has degree t, the absolute component number/index of R, and that this representation theory identifies the multiplication-constant factor systems with the standard literature concept. §28 begins at line 23325.
- Japanese title: 歪行列表現への接続と §28 境界
- Simplified Chinese title: 连接扭矩阵表示并进入 §28

**Japanese Draft**

注 2 では、直接的な基礎づけを行う場合にも、§§25/26 で展開された歪行列表現の理論を接続すべきことが述べられる。

以後、特に §28 の終わりで用いられるのは、\(\Im\) の既約歪表示の次数が \(t\) であり、この \(t\) が \(\Re\) の絶対成分数、すなわち指数である、という事実である。

また、この表現論によって、ここで乗法定数として導入された因子系が、文献で通常用いられる因子系の概念と同一であることが得られる。§28 は 23325 行から始まる。

**Simplified Chinese Draft**

注 2 说明，若作直接的奠基，也应接上 §§25/26 中发展的扭矩阵表示理论。

后文，特别是 §28 末尾，将使用这样一个事实：\(\Im\) 的既约扭表示次数为 \(t\)，而 \(t\) 是 \(\Re\) 的绝对分量数，即指数。

此外，这一表示论表明，这里作为乘法常数引入的因子系，与文献中通常使用的因子系概念相同。§28 从 23325 行开始。

**Script/TeX Notes**

- Preserve references to §§25/26, §28, degree \(t\), and absolute Komponentenzahl/Index.
- Absolute Komponentenzahl remains 絶対成分数 / 绝对分量数.
- This closes §27 and sets next cursor at `23325`.

**Unresolved Flags**

- Line 23323 should be checked against source page for the exact `§ 28 Schluß` reference.
- No canonical approval of 歪行列表現 / 扭矩阵表示 is implied.
