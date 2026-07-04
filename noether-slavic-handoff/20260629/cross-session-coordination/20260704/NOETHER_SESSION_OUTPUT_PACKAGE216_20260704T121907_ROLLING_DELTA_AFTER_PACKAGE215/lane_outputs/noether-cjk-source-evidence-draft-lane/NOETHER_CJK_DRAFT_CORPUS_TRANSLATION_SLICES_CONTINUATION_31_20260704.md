# Noether CJK Draft Corpus Translation Slices: Continuation 31

Generated UTC: `2026-07-04T10:17:25.543254+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical Japanese and Simplified Chinese corpus slices. Not native reviewed. Not approved. No gate promotion.

Korean remains source-discovery/crosswalk only in this continuation.

## Metadata

- Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Coverage: Continuation 31 covers German baseline 23325-23448, completing Deuring lecture Chapter VI §28 before §29 begins at 23450.
- Slice count: `6`

## Slices

### cjk-continuation-31-001-product-theorem-setup-and-claim

- German anchor: `23325-23337`
- Source summary: Begins §28. Two crossed products R_r and its barred counterpart are given with small factor systems a and b. Their product is rewritten over a common isomorphic Galois field, and the claim is that the resulting factor system c is the product of the corresponding a and b elements. The proof is reduced to automorphism rings of left ideals of absolute length n.
- Japanese title: 因子系の積定理の設定と主張
- Simplified Chinese title: 因子系乘积定理的设置与主张

**Japanese Draft**

§28 は因子系の積定理から始まる。二つの交叉積 \(\Re_r=\Im\cdot\Im=\Im u_E+\cdots+\Im u_T\) と \(\overline{\Re}_r=\overline{\Im}\,\overline{\Im}\) を取り、それぞれ \(u_Su_T=u_{ST}a_{S,T}\)、\(\bar u_S\bar u_T=\bar u_{ST}\bar b_{S,T}\) を満たすとする。

二つの Galois 体と群を対応させると、積 \(\Re_r\times\overline{\Re}_r\) は同じ型の交叉積として書け、そこに小因子系 \(\tilde c_{S,T}\) が現れる。主張は、\(\tilde c_{S,T}=\tilde a_{S,T}\tilde b_{S,T}\) である、というものだ。

証明は、絶対長 \(n\) をもつ左イデアルの自己同型環が、適切な交叉積と同型になることに基づく。まず便宜上、\(\Re_{rs}=\Re_r\times\mathsf P_s\) の中の絶対長 \(n\) の左イデアルについて、自己同型環が \(\Re_r\) と同型であることを示す。

**Simplified Chinese Draft**

§28 从因子系的乘积定理开始。取两个交叉积 \(\Re_r=\Im\cdot\Im=\Im u_E+\cdots+\Im u_T\) 与 \(\overline{\Re}_r=\overline{\Im}\,\overline{\Im}\)，分别满足 \(u_Su_T=u_{ST}a_{S,T}\)、\(\bar u_S\bar u_T=\bar u_{ST}\bar b_{S,T}\)。

把两个 Galois 域及其群对应起来后，乘积 \(\Re_r\times\overline{\Re}_r\) 可写成同类交叉积，并出现小因子系 \(\tilde c_{S,T}\)。主张是 \(\tilde c_{S,T}=\tilde a_{S,T}\tilde b_{S,T}\)。

证明依赖于这样一点：绝对长度为 \(n\) 的左理想的自同构环，与适当的交叉积同构。先为方便起见证明，在 \(\Re_{rs}=\Re_r\times\mathsf P_s\) 中绝对长度为 \(n\) 的左理想，其自同构环与 \(\Re_r\) 同构。

**Script/TeX Notes**

- Preserve \(\Re_r\times\overline{\Re}_r\), \(\tilde c_{S,T}=\tilde a_{S,T}\tilde b_{S,T}\), and \(\Re_{rs}=\Re_r\times\mathsf P_s\).
- Produktsatz is rendered as 積定理 / 乘积定理 in this factor-system context.
- The product/crossed-product material is not direct Tensorprodukt evidence.

**Unresolved Flags**

- Lines 23328-23335 contain OCR drift in \(\Im\), \(\tilde{\mathfrak J}\), and barred symbols; source-image review needed.
- Absolute length terminology is provisional: 絶対長 / 绝对长度.

### cjk-continuation-31-002-automorphism-ring-lemmas-for-left-ideals

- German anchor: `23341-23356`
- Source summary: Proves Satz 1 through three lemmas. Left ideals of absolute length n in R_rs are operator-isomorphic; the automorphism ring of a direct summand left ideal oe_1 is e_1oe_1; and for matrix units in P_s, the automorphism ring of R_tau x b is R_tau c_11, hence isomorphic to R_tau.
- Japanese title: 左イデアルの自己同型環に関する補題
- Simplified Chinese title: 左理想自同构环的补题

**Japanese Draft**

定理 1 の証明は三つの補題に分かれる。第一に、\(\Re_{rs}\) の中の絶対長 \(n\) の左イデアルはすべて作用素同型であり、したがってそれらの自己同型環は環同型である。

第二に、単位元を持つ環 \(o\) で、\(l=oe_1\) が冪等元 \(e_1\) による直和因子の左イデアルなら、\(l\) の自己同型環は \(e_1oe_1\) と同型である。実際、\(e_1re_1\) による乗法が \(l\) の作用素準同型を与え、すべての準同型がこの形で得られる。

第三に、\(P_s\) を行列単位 \(c_{ik}\) で書き、\(b=c_{11}P+\cdots+c_{s1}P\) と置くと、\(\Re_\tau\times b\) の自己同型環は \(\Re_\tau c_{11}\) になり、これは \(\Re_\tau\) と同型である。

**Simplified Chinese Draft**

定理 1 的证明分为三个补题。第一，\(\Re_{rs}\) 中绝对长度为 \(n\) 的左理想全都算子同构，因此它们的自同构环彼此环同构。

第二，若带单位环 \(o\) 中 \(l=oe_1\) 是由幂等元 \(e_1\) 给出的直和因子左理想，则 \(l\) 的自同构环与 \(e_1oe_1\) 同构。确实，乘以 \(e_1re_1\) 给出 \(l\) 的算子同态，而且每个同态都由这种方式产生。

第三，把 \(P_s\) 用矩阵单位 \(c_{ik}\) 表示，并令 \(b=c_{11}P+\cdots+c_{s1}P\)，则 \(\Re_\tau\times b\) 的自同构环为 \(\Re_\tau c_{11}\)，因此与 \(\Re_\tau\) 同构。

**Script/TeX Notes**

- Preserve \(l=oe_1\), \(e_1oe_1\), \(P_s=\sum c_{ik}P\), and \(c_{11}\Re_r\times\mathsf P_sc_{11}\).
- Automorphismenring is 自己同型環 / 自同构环.
- Matrizeneinheiten is 行列単位 / 矩阵单位.

**Unresolved Flags**

- Line 23349 has \(\Re_{\tau}c_n\) in the baseline but the proof formula uses \(c_{11}\); source-image review needed.
- Operator-isomorphic phrasing needs domain review.

### cjk-continuation-31-003-decomposition-of-product-crossed-products

- German anchor: `23358-23368`
- Source summary: Determines and decomposes R_r x barred R into left ideals of absolute length n. The product is expressed using Galois groups and a decomposition of the product field into idempotent components, and a specific left ideal I is fixed by choosing an isomorphism ze_1 = e_1 barred z.
- Japanese title: 積交叉積の絶対長 \(n\) 左イデアルへの分解
- Simplified Chinese title: 把乘积交叉积分解为绝对长度 \(n\) 的左理想

**Japanese Draft**

つぎに、\(\Re_r\times\overline{\Re}_{\overline r}\) を絶対長 \(n\) の左イデアルへ分解する。定義から、この積は \(\mathfrak Z\cdot\mathfrak G\) と \(\overline{\mathfrak Z}\cdot\overline{\mathfrak G}\) の積として見られ、バー付きとバーなしの成分は互いに元ごとに可換である。

さらに、\(\mathfrak J\times\overline{\mathfrak J}\) を冪等元 \(e_1,\ldots,e_n\) によって分解し、\(\mathfrak J e_i=\overline{\mathfrak J}e_i\) と見る。各和因子は \(\Im\) に関して同じ階数を持ち、全体の絶対長が \(n^2\) であるため、それぞれ絶対長 \(n\) を持つ。

以後の議論では、\(\mathbb I=(\mathfrak G\times\overline{\mathfrak G})\Im e_1\) を基礎に置く。ここで \(ze_1=e_1\overline z\) によって、\(\Im\) と \(\overline{\Im}\) の間の特定の同型を固定する。

**Simplified Chinese Draft**

接着，把 \(\Re_r\times\overline{\Re}_{\overline r}\) 分解为绝对长度为 \(n\) 的左理想。按定义，这个乘积可看作 \(\mathfrak Z\cdot\mathfrak G\) 与 \(\overline{\mathfrak Z}\cdot\overline{\mathfrak G}\) 的乘积，带横线和不带横线的部分逐元素可交换。

再用幂等元 \(e_1,\ldots,e_n\) 分解 \(\mathfrak J\times\overline{\mathfrak J}\)，并把 \(\mathfrak J e_i=\overline{\mathfrak J}e_i\) 看作对应关系。各个和因子关于 \(\Im\) 有相同秩，而整体绝对长度为 \(n^2\)，所以每个和因子绝对长度为 \(n\)。

之后固定左理想 \(\mathbb I=(\mathfrak G\times\overline{\mathfrak G})\Im e_1\)。其中通过 \(ze_1=e_1\overline z\) 选定 \(\Im\) 与 \(\overline{\Im}\) 之间的一个同构。

**Script/TeX Notes**

- Preserve \(\Re_r\times\overline{\Re}_{\overline r}\), \(\mathfrak A_{\mathfrak I}\), \(\mathbb I\), and \(ze_1=e_1\overline z\).
- This is direct/product crossed-product material, not a tensor-product anchor.
- Barred/unbarred glyphs must remain explicit in TeX.

**Unresolved Flags**

- Lines 23363-23368 have OCR drift in \(\mathfrak A_f\), \(\mathfrak A_{\mathfrak I}\), \(\mathfrak J\), and \(\Im\).
- The phrase 'Multiplikation eines Galoiskörpers mit sich' needs domain review.

### cjk-continuation-31-004-twisted-representation-proof-of-product-theorem

- German anchor: `23370-23407`
- Source summary: Uses a twisted representation of e_1 A_f e_1 to prove the product theorem. Satz 2 writes A as a crossed product with field Z~ and generators e_1 u_S barred u_S e_1. Three lemmas show the generators commute with e_1 correctly, induce the right substitutions, and yield factor system a_S,T e_1 times barred b_S,T e_1.
- Japanese title: 隅環の歪表示による積定理の証明
- Simplified Chinese title: 用角环的扭表示证明乘积定理

**Japanese Draft**

積定理の証明は、\(e_1\mathfrak A_f e_1\) の歪表示へ帰着される。前段までにより、\(\Re_r\times\overline{\Re}_{\overline r}\) の因子系は、\(\mathfrak A=e_1\mathfrak A_f e_1\) の歪表示の因子系と同型になる。

定理 2 は、\(\mathfrak A=\widetilde{\mathfrak Z}\cdot\widetilde{\mathfrak G}\) と書けることを述べる。ここで \(\widetilde{\mathfrak Z}=\mathfrak Ze_1=\overline{\mathfrak Z}e_1\) であり、生成元は \(e_1u_S\bar u_Se_1\) の形を持つ。

補題 1 は \(e_1u_S\bar u_S=u_S\bar u_Se_1\) を示し、補題 2 は \(ze_1\) と \(e_1u_S\bar u_Se_1\) の交換関係から正しい置換が誘導されることを示す。補題 3 では、得られる因子系が \(a_{S,T}e_1\cdot\bar b_{S,T}e_1\) に等しいことを計算し、これで因子系の積定理が証明される。

**Simplified Chinese Draft**

乘积定理的证明归结为 \(e_1\mathfrak A_f e_1\) 的扭表示。由前面的步骤，\(\Re_r\times\overline{\Re}_{\overline r}\) 的因子系与 \(\mathfrak A=e_1\mathfrak A_f e_1\) 的扭表示的因子系同构。

定理 2 说明 \(\mathfrak A=\widetilde{\mathfrak Z}\cdot\widetilde{\mathfrak G}\)。这里 \(\widetilde{\mathfrak Z}=\mathfrak Ze_1=\overline{\mathfrak Z}e_1\)，生成元形如 \(e_1u_S\bar u_Se_1\)。

补题 1 证明 \(e_1u_S\bar u_S=u_S\bar u_Se_1\)，补题 2 由 \(ze_1\) 与 \(e_1u_S\bar u_Se_1\) 的交换关系说明诱导了正确的代换。补题 3 计算出所得因子系为 \(a_{S,T}e_1\cdot\bar b_{S,T}e_1\)，从而证明因子系的乘积定理。

**Script/TeX Notes**

- Preserve \(e_1\mathfrak A_f e_1\), \(\widetilde{\mathfrak Z}\cdot\widetilde{\mathfrak G}\), \(e_1u_S\bar u_Se_1\), and \(a_{S,T}e_1\cdot\bar b_{S,T}e_1\).
- Corner ring/idempotent-corner prose is provisional.
- Line 23407 is the explicit proof closure for the factor-system product theorem.

**Unresolved Flags**

- Lines 23380-23382 contain OCR noise (`so da\beta`) and possible bar/tilde confusion.
- Line 23388 has exponent/index issues around \(e^{R^{-1}2}\); source-image review required.

### cjk-continuation-31-005-product-theorem-for-associated-classes

- German anchor: `23409-23422`
- Source summary: States the product theorem for associated factor-system classes: {a}·{b} = {a·b}. The proof follows from the preceding result because changing generators u and barred u to v and barred v also changes their product generators to v barred v e_1, yielding the corresponding associated transformation.
- Japanese title: 同伴因子系類の積定理
- Simplified Chinese title: 同伴因子系类的乘积定理

**Japanese Draft**

続いて、同伴因子系の類についての積定理が述べられる。すなわち \(\{a_{S,T}\}\cdot\{b_{S,T}\}=\{a_{S,T}\cdot b_{S,T}\}\) である。

これは前段の因子系の積定理から直接従う。生成元を \(u,\bar u\) から \(v,\bar v\) へ取り替えると、積側でも \(v\bar v e_1\) への取り替えが起こるからである。

式 \(u\bar u e_1=v c\cdot\bar v\bar d\,e_1=v\bar v\cdot c d\,e_1=v\bar v e_1\cdot c\bar d\,e_1\) は、同伴変換が積の類にも対応することを示している。

**Simplified Chinese Draft**

接着给出同伴因子系类的乘积定理：\(\{a_{S,T}\}\cdot\{b_{S,T}\}=\{a_{S,T}\cdot b_{S,T}\}\)。

这直接来自前面的因子系乘积定理。把生成元从 \(u,\bar u\) 换成 \(v,\bar v\) 时，在乘积一侧也相应换成 \(v\bar v e_1\)。

公式 \(u\bar u e_1=v c\cdot\bar v\bar d\,e_1=v\bar v\cdot c d\,e_1=v\bar v e_1\cdot c\bar d\,e_1\) 表明，同伴变换也对应于乘积类。

**Script/TeX Notes**

- Preserve \(\{a_{S,T}\}\cdot\{b_{S,T}\}=\{a_{S,T}\cdot b_{S,T}\}\) and \(u\bar u e_1\).
- Associated classes remain 同伴類 / 同伴类.
- Class product here is factor-system class product, not tensor-product evidence.

**Unresolved Flags**

- Line 23421 has possible \(cd\) vs \(c\bar d\) OCR/TeX inconsistency; source-image review needed.
- The generator-change prose needs domain review before canonical use.

### cjk-continuation-31-006-unit-class-consequences-and-section-29-boundary

- German anchor: `23424-23448`
- Source summary: Draws consequences. If {a} is a factor system of {R} and t is the index of {R}, then {a}^t is the unit class, using the irreducible twisted representation of degree t. There is an isomorphism between the group of classes split by the fixed field and classes of associated factor systems, and the unit classes correspond; a crossed product is equal to P, i.e. a matrix ring over the center, exactly when its factor system is associated with the unit system. §29 begins at line 23450.
- Japanese title: 単位類への帰結と §29 境界
- Simplified Chinese title: 单位类结论及进入 §29

**Japanese Draft**

帰結として、\(\{a\}\) が \(\{\Re\}\) の因子系で、\(t\) が \(\{\Re\}\) の指数なら、\(\{a\}^t\) は単位類になる。これは、\(\Im\) の既約歪表示の次数が \(t\) であることから従う。

さらに、固定した分解体 \(\Im\) を持つ類 \(\{\Re\}\) の群と、同伴因子系の類 \(\{a_{S,T}\}\) の群との間に同型がある。§27 の構成により一対一対応があり、前段の積定理により対応は準同型であるため、同型となる。

特に単位類同士が対応する。したがって、交叉積が \(P\) に等しい、すなわち中心上の行列環になるのは、その因子系が単位系に同伴である場合、かつその場合に限られる。§29 は 23450 行から始まる。

**Simplified Chinese Draft**

作为结论，若 \(\{a\}\) 是 \(\{\Re\}\) 的因子系，而 \(t\) 是 \(\{\Re\}\) 的指数，则 \(\{a\}^t\) 等于单位类。这由 \(\Im\) 的既约扭表示次数为 \(t\) 得出。

并且，固定分裂域 \(\Im\) 的类 \(\{\Re\}\) 所成的群，与同伴因子系类 \(\{a_{S,T}\}\) 所成的群同构。§27 的构造给出一一对应，而前面的乘积定理说明该对应是同态，所以得到同构。

特别地，单位类彼此对应。因此，交叉积等于 \(P\)，也就是成为中心上的矩阵环，当且仅当它的因子系同伴于单位系。§29 从 23450 行开始。

**Script/TeX Notes**

- Preserve \(\{a\}^t\), \(\mathcal K_3\), \(\{a_{S,T}\}\), and the footnote formulas at 23444-23446.
- Einheitsklasse is 単位類 / 单位类; Einssystem is 単位系 / 单位系.
- The matrix-ring conclusion is recorded as matrix ring over the center, not as a gate closure.

**Unresolved Flags**

- Line 23440 uses \(\mathcal K_3\) with OCR-like `3`; source-image review needed for the fixed splitting-field symbol.
- Footnote line 23446 is symbol-heavy and not normalized in draft prose.
