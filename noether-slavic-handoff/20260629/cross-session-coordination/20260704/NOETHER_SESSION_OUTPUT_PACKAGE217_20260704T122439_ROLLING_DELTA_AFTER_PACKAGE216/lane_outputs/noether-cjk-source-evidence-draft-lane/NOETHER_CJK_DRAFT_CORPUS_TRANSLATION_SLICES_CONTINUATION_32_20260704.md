# Noether CJK Draft Corpus Translation Slices: Continuation 32

Generated UTC: `2026-07-04T10:21:48.197734+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical Japanese and Simplified Chinese corpus slices. Not native reviewed. Not approved. No gate promotion.

Korean remains source-discovery/crosswalk only in this continuation.

## Metadata

- Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Coverage: Continuation 32 covers German baseline 23450-23465, completing Deuring lecture Chapter VI §29 before §30 begins at 23467.
- Slice count: `2`

## Slices

### cjk-continuation-32-001-main-genus-in-the-minimal-definition-and-theorem

- German anchor: `23450-23456`
- Source summary: Begins §29. For a crossed product R_r and the group of elements carrying the Galois field into itself by inner automorphisms, defines the main genus in the minimal as the group automorphisms of G* extending the identity of Z*. The theorem says every automorphism of the main genus has form u_S -> u_S b^S b^{-1} = u_S b^{S-1}, and conversely every such assignment gives one.
- Japanese title: 最小における主種とその自己同型
- Simplified Chinese title: 最小情形下的主属及其自同构

**Japanese Draft**

§29 は「最小における主種定理」を扱う。交叉積 \(\Re_r=\Im\cdot\Im\) を取り、内的自己同型によって \(\Im\) 全体を自分自身へ移す元全体の群 \(\Im^*\) を考える。

定義では、「最小における主種」\(\mathcal S\) を、\(\mathfrak G^*\) の群自己同型のうち、\(\mathfrak Z^*\) 上の恒等写像を延長するもの全体として定める。この名称の理由は、後の巡回体への特殊化で説明される。

定理は、主種の任意の自己同型が \(u_S\mapsto u_S\cdot b^Sb^{-1}=u_Sb^{S-1}\) の形であり、逆にこの形の対応は主種の自己同型を与える、という内容である。

**Simplified Chinese Draft**

§29 讨论“最小情形下的主属定理”。取交叉积 \(\Re_r=\Im\cdot\Im\)，并考虑所有通过内自同构把 \(\Im\) 整体变到自身的元素所成的群 \(\Im^*\)。

定义中，“最小情形下的主属”\(\mathcal S\) 是 \(\mathfrak G^*\) 的群自同构中，那些延拓 \(\mathfrak Z^*\) 上恒等映射者的全体。这个名称的理由将在后面对循环域的特殊化中说明。

定理说，主属的任一自同构都具有 \(u_S\mapsto u_S\cdot b^Sb^{-1}=u_Sb^{S-1}\) 的形式；反过来，每个这样的对应也给出主属的一个自同构。

**Script/TeX Notes**

- Preserve \(\mathcal S\), \(\mathfrak G^*\), \(\mathfrak Z^*\), and \(u_S\mapsto u_Sb^{S-1}\).
- Hauptgeschlecht im Minimalen is drafted as 最小における主種 / 最小情形下的主属; review required before canonical glossary use.
- The section points forward to §30 for motivation by cyclic fields.

**Unresolved Flags**

- Line 23452 has OCR-unstable \(\Im^*\) coset notation; source-image review needed.
- Main-genus terminology remains provisional and not native reviewed.

### cjk-continuation-32-002-proof-by-extension-to-inner-ring-automorphism

- German anchor: `23458-23465`
- Source summary: Proves the theorem. A group automorphism u_S -> v_S fixing every z in Z extends to a ring automorphism by mapping sums of u_S coefficients to sums of v_S coefficients; such automorphisms are inner. A generating element b commutes with all z and lies in beta, giving v_S = b u_S b^{-1} = u_S b^S b^{-1}. Conversely this formula with b in beta gives an automorphism of R_r preserving beta and hence G*.
- Japanese title: 環自己同型への延長による証明
- Simplified Chinese title: 通过延拓为内环自同构来证明

**Japanese Draft**

証明では、群自己同型が \(u_S\mapsto v_S\)、かつ各 \(z\in\mathfrak Z\) を固定すると仮定する。積も対応しているので、\(\sum u_Sc_{\lambda S}\mapsto\sum v_Sc_{\lambda S}\) により \(\mathfrak R_r\) の環自己同型へ延長できる。

このような環自己同型は内的である。したがって、ある生成元 \(b\) により \(v_S=bu_Sb^{-1}\)、また \(z=bzb^{-1}\) となる。\(b\) はすべての \(z\) と可換なので \(\beta\) に属し、そこから \(v_S=bu_Sb^{-1}=u_Sb^Sb^{-1}\) が従う。

逆に、\(b\in\beta\) に対して \(v_S=u_Sb^Sb^{-1}\) と置けば、これは \(\beta\) を元ごとに自分自身へ移す \(\Re_r\) の自己同型であり、定義により \(\Im^*\) 全体も保つ。従って主種の自己同型になる。

**Simplified Chinese Draft**

证明中假设群自同构给出 \(u_S\mapsto v_S\)，并固定每个 \(z\in\mathfrak Z\)。由于乘积也对应，它可通过 \(\sum u_Sc_{\lambda S}\mapsto\sum v_Sc_{\lambda S}\) 延拓为 \(\mathfrak R_r\) 的环自同构。

这样的环自同构是内的。因此存在生成元 \(b\)，使 \(v_S=bu_Sb^{-1}\)，且 \(z=bzb^{-1}\)。因为 \(b\) 与所有 \(z\) 可交换，所以 \(b\in\beta\)，于是得到 \(v_S=bu_Sb^{-1}=u_Sb^Sb^{-1}\)。

反过来，若 \(b\in\beta\) 并定义 \(v_S=u_Sb^Sb^{-1}\)，则这是 \(\Re_r\) 的一个自同构，并逐元素保持 \(\beta\)；按定义也保持整个 \(\Im^*\)。所以它给出主属的自同构。

**Script/TeX Notes**

- Preserve \(\sum u_Sc_{\lambda S}\mapsto\sum v_Sc_{\lambda S}\), \(v_S=bu_Sb^{-1}\), and \(v_S=u_Sb^Sb^{-1}\).
- Inner automorphism remains 内的自己同型 / 内自同构.
- The proof is short but symbol-sensitive around \(b^{S-1}\).

**Unresolved Flags**

- Lines 23458-23462 need source-image review for coefficient indices \(c_{\lambda S}\) and symbolic exponent placement.
- The phrase 'bekanntlich inner' relies on prior theory and is not independently verified here.
