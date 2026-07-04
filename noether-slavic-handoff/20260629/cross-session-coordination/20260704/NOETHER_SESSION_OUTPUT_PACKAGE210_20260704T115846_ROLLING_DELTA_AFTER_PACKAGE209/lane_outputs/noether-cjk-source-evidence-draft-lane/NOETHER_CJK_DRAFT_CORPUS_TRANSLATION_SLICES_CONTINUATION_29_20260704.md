# Noether CJK Draft Corpus Translation Slices: Continuation 29

Generated UTC: `2026-07-04T09:58:25.481035+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical Japanese and Simplified Chinese corpus slices. Not native reviewed. Not approved. No gate promotion.

Korean remains source-discovery/crosswalk only in this continuation.

## Metadata

- Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Coverage: Continuation 29 covers German baseline 23141-23192, completing Deuring lecture Chapter V §26 before Kapitel VI begins at 23193.
- Slice count: `3`

## Slices

### cjk-continuation-29-001-twisted-representations-of-the-galois-group

- German anchor: `23141-23158`
- Source summary: Begins §26. Reinterprets twisted representations as representations of the Galois group by choosing u_S in R_r that generate each automorphism. Essential data are the algebra class and the associated class of small factor systems; a note connects this setup with Speiser's earlier factor-system definition.
- Japanese title: Galois 群の歪表示としての再解釈
- Simplified Chinese title: 作为 Galois 群扭表示的再解释

**Japanese Draft**

§26 では、これまで \(\mathfrak G^*\) の表示として扱っていた歪表示を、\(\mathfrak Z/\mathsf P\) の Galois 群 \(\mathfrak G\) の表示として見直す。各 \(S\in\mathfrak G\) に、変換 \(u_S^{-1}zu_S=z^S\) を生む \(\Re_r\) の元 \(u_S\) を選び、その行列 \(A_S\) を対応させる。

このような表示を特徴づけるには、どの \(\Re_r\) で取るか、どの \(u_S\) とどの基底を用いるかを指定する必要がある。ただし基底変更は同値表示を与え、\(u_S\) の変更は同伴な小因子系を与えるので、本質的なデータは同伴小因子系の類 \(\{a_{S,T}\}\) である。

Speiser の仕事に関する注では、同じ形の表示 \(S\mapsto A_S\) と積規則から因子系 \(a_{S,T}\) が定義され、ここで別の根拠から導入されたものと一致する、と述べられる。

**Simplified Chinese Draft**

§26 把此前作为 \(\mathfrak G^*\) 的表示来看的扭表示，重新看成 \(\mathfrak Z/\mathsf P\) 的 Galois 群 \(\mathfrak G\) 的表示。对每个 \(S\in\mathfrak G\)，选取 \(\Re_r\) 中产生变换 \(u_S^{-1}zu_S=z^S\) 的元素 \(u_S\)，并把它的矩阵 \(A_S\) 对应给 \(S\)。

要刻画这种表示，需说明它取在哪个 \(\Re_r\) 中、用了哪些 \(u_S\)、以及用了哪组基。但换基只给出等价表示，改变 \(u_S\) 则给出同伴小因子系，因此本质数据是同伴小因子系的类 \(\{a_{S,T}\}\)。

关于 Speiser 的注记说明，同样形式的表示 \(S\mapsto A_S\) 及其乘法规则曾被用来定义因子系 \(a_{S,T}\)，它们与这里从另一基础引入的因子系相同。

**Script/TeX Notes**

- Preserve \(S\mapsto u_S\mapsto A_S\), \(u_S^{-1}zu_S=z^S\), and \(\{a_{S,T}\}\).
- Verschränkte Darstellung remains 歪表示 / 扭表示 pending review.
- Speiser note is source evidence for factor-system lineage, not a reviewer approval.

**Unresolved Flags**

- Lines 23143-23158 include OCR noise in group symbols and a note marker; source-image review needed.
- The use of `reziprok`/transposed product at 23155-23158 needs domain review.

### cjk-continuation-29-002-kronecker-product-claim-for-twisted-representations

- German anchor: `23160-23175`
- Source summary: Defines the Kronecker product A x B of matrices entrywise as (a_ik b_mn). Claims that S maps to A_S x B_S is again a twisted representation and belongs to the product of the originating algebra classes.
- Japanese title: Kronecker 積による歪表示の積
- Simplified Chinese title: 用 Kronecker 积构造扭表示的乘积

**Japanese Draft**

本文は二つの行列 \(A=(a_{ik})\)、\(B=(b_{\mu\nu})\) の Kronecker 積を、成分 \(a_{ik}b_{\mu\nu}\) から成る行列 \(A\times B\) と定義する。

主張は、\(S\mapsto A_S\times B_S\) もまた \(\mathfrak S\) の歪表示であり、\(A_S\) が \(\mathfrak N_r\) から、\(B_S\) が \(\mathfrak L_s\) から来るなら、それは積 \(\mathfrak N_r\times\mathfrak L_s\) に属する、というものである。

証明の開始では、\(S\mapsto A_S\times B_S\)、\(T\mapsto A_T\times B_T\) と置き、\(ST\) に対応する行列を因子系 \(a_{S,T}\)、\(b_{S,T}\) を含む式で比較する。

**Simplified Chinese Draft**

文本把两个矩阵 \(A=(a_{ik})\)、\(B=(b_{\mu\nu})\) 的 Kronecker 积定义为由各成分 \(a_{ik}b_{\mu\nu}\) 组成的矩阵 \(A\times B\)。

命题是：\(S\mapsto A_S\times B_S\) 仍是 \(\mathfrak S\) 的扭表示；若 \(A_S\) 来自 \(\mathfrak N_r\)，\(B_S\) 来自 \(\mathfrak L_s\)，则该表示属于乘积 \(\mathfrak N_r\times\mathfrak L_s\)。

证明开头令 \(S\mapsto A_S\times B_S\)、\(T\mapsto A_T\times B_T\)，再把对应于 \(ST\) 的矩阵同含有因子系 \(a_{S,T}\)、\(b_{S,T}\) 的表达式比较。

**Script/TeX Notes**

- Preserve \(A\times B=(a_{ik}b_{\mu\nu})\) and \(S\mapsto A_S\times B_S\).
- Kroneckersches Produkt is recorded as Kronecker 積 / Kronecker 积, not promoted to tensor-product glossary closure.
- Line 23160 is source evidence for a matrix Kronecker product term, but it is not a direct `Tensorprodukt` or `\otimes` anchor.

**Unresolved Flags**

- Need reviewer decision whether Kronecker product should cross-reference tensor-product row without closing it.
- Line 23162 has OCR uncertainty in the group/ring symbols around \(\mathfrak S\), \(\mathfrak N_r\), and \(\mathfrak L_s\).

### cjk-continuation-29-003-matrix-unit-proof-and-chapter-vi-boundary

- German anchor: `23177-23192`
- Source summary: Proves the Kronecker product claim by representing A and B with matrix units c_ik and d_mn. Matrix multiplication corresponds to element multiplication in the direct product of the two matrix rings, making every A-matrix commute with every B-matrix and giving the desired relation. Chapter VI begins at line 23193.
- Japanese title: 行列単位による証明と第 VI 章への境界
- Simplified Chinese title: 用矩阵单位证明及进入第 VI 章

**Japanese Draft**

証明では、行列 \(A\) と \(B\) を、それぞれ本文の \(\Re_r\) や \(\Re_s\) の行列単位とは無関係な行列単位 \(c_{ik}\)、\(d_{\mu\nu}\) で表す。

すると \(A\times B\) は新しい行列単位 \(c_{ik}d_{\mu\nu}\) に関する行列として読める。したがって、\(A\)-行列と \(B\)-行列の乗法は、二つの行列環の直接積における元の乗法と一対一に対応する。

このため任意の \(A\)-行列は任意の \(B\)-行列と可換であり、その可換性が、\(a_{\mathcal S,T}^{-1}b_{\mathcal S,T}^{-1}\) を掛けた後に示すべき関係を与える。第 VI 章は次行、23193 行から始まる。

**Simplified Chinese Draft**

证明中用矩阵单位 \(c_{ik}\)、\(d_{\mu\nu}\) 分别表示矩阵 \(A\) 与 \(B\)；这些矩阵单位与正文中 \(\Re_r\) 或 \(\Re_s\) 的矩阵单位无关。

于是 \(A\times B\) 可看作关于新矩阵单位 \(c_{ik}d_{\mu\nu}\) 的矩阵。因此，\(A\)-矩阵与 \(B\)-矩阵的乘法，与两个矩阵环的直接积中的元素乘法一一对应。

所以每个 \(A\)-矩阵都与每个 \(B\)-矩阵可交换；这种可交换性在乘以 \(a_{\mathcal S,T}^{-1}b_{\mathcal S,T}^{-1}\) 后给出所需关系。第 VI 章从下一行，即 23193 行开始。

**Script/TeX Notes**

- Preserve \(c_{ik}\), \(d_{\mu\nu}\), \(A\times B\), and \(a_{\mathcal S,T}^{-1}b_{\mathcal S,T}^{-1}\).
- Line 23191 has an OCR typo `Foglich`; draft silently reads it as Folglich in prose.
- Direktes Produkt der Matrizenringe is direct product of matrix rings, not Tensorprodukt evidence.

**Unresolved Flags**

- Line 23191 has a possible OCR sign error in `c_{ik}d_{\mu\nu}-d_{\mu\nu}c_{ik}`; source-image review required.
- The transition to Kapitel VI at 23193 should be the next non-duplicative cursor.
