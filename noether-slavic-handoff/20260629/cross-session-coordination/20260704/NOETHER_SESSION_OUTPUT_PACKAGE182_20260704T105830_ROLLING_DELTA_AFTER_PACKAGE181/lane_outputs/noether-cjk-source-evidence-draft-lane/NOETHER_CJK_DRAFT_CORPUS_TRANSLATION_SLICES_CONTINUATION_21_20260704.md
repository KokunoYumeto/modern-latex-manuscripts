# Noether CJK Draft Corpus Translation Slices: Continuation 21

Generated UTC: `2026-07-04T08:57:04.091330+00:00`

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

- tensor product: no German Tensorprodukt anchor in 21532-21768; the next baseline otimes hit at 21847 remains outside this continuation and is not a tensor-product closure
- localization: Quotientenring candidates remain 16223-16225, 18467, 20105, 20228, 20240, 20284, 20949, 20953, and 21009, plus Quotientenkörper at 20822; no direct Lokalisierung label in 21532-21768
- Harish-Chandra: no German corpus anchor
- abstract algebra: no direct abstract-algebra anchor in Chapter III lines 21532-21768
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in this continuation
- group algebra: Chapter III supplies direct Gruppenring/group-ring evidence, not group-algebra evidence

## cjk-continuation-21-001-group-ring-and-reducibility-criterion

Anchor: German baseline lines `21532-21562`; Kapitel III §14 group ring.

Source summary: Defines the group ring of a finite group over a commutative field as a hypercomplex system and states the full reducibility criterion in terms of group order and field characteristic, with the radical/nonzero nilpotent ideal direction.

Japanese title: 群環と完全可約性の判定

第 III 章は Abel 群へ進むが、§14 ではまず有限群 \(\mathfrak G=\{a_1,\ldots,a_h\}\) と可換体 \(P\) から、群の積を乗法とする超複素系 \(\mathfrak{o}[\mathfrak G]=a_1P+\cdots+a_hP\) を作り、これを \(P\) における群環と呼ぶ。

問題は、この群環がいつラジカルを持つかである。一般定理として、群の位数 \(h\) が \(P\) の標数 \(p\) で割り切れないとき、かつそのときに限り、\(\mathfrak{o}[\mathfrak G]\) は完全可約であると述べられる。

まず \(h\equiv0\pmod p\) なら、\(\mathfrak a=P(a_1+\cdots+a_h)\) が非零の両側イデアルとなり、しかも冪零であるため、ラジカル \(\mathfrak C\) は零ではない。逆方向はここでは Abel 群についてだけ証明するとされる。

Simplified Chinese title: 群环与完全可约性判据

第 III 章进入 Abel 群；§14 先由有限群 \(\mathfrak G=\{a_1,\ldots,a_h\}\) 和交换域 \(P\) 构造超复系统 \(\mathfrak{o}[\mathfrak G]=a_1P+\cdots+a_hP\)，其乘法由群乘法给出，并称为 \(P\) 上的群环。

核心问题是这个群环何时有根基。一般定理说，当且仅当群阶 \(h\) 不被 \(P\) 的特征 \(p\) 整除时，\(\mathfrak{o}[\mathfrak G]\) 完全可约。

先证明若 \(h\equiv0\pmod p\)，则 \(\mathfrak a=P(a_1+\cdots+a_h)\) 是非零双侧理想，并且是幂零的，所以根基 \(\mathfrak C\) 非零。反方向在这里只对 Abel 群证明。

Script/codepoint and TeX/PDF notes:

- Gruppenring is 群環 / 群环. This is not a group-algebra row closure.
- Preserve \(\mathfrak{o}[\mathfrak G]=a_1P+\cdots+a_hP\), \(h\equiv0\pmod p\), and \(\mathfrak a=P(a_1+\cdots+a_h)\).
- Lines 21536-21542 and 21558-21562 are OCR-damaged; draft follows the mathematical structure and flags source quality.

Unresolved flags:

- Group ring/group algebra distinction remains unresolved for glossary promotion.
- OCR-damaged proof lines need source-image verification.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-21-002-abelian-group-rings-and-character-count

Anchor: German baseline lines `21564-21580`; §15 group rings of abelian groups, representation count.

Source summary: For an abelian group, applies commutative hypercomplex-system results to count h irreducible first-degree representations over an algebraically closed field when the characteristic does not divide h, using decomposition into cyclic groups and roots of unity.

Japanese title: Abel 群環と既約表現の個数

§15 では、\(\mathfrak A=\{a_1,\ldots,a_h\}\) を Abel 群とする。このとき群環は可換であるため、可換超複素系についての一般定理を適用できる。

標数 \(p\) が \(h\) を割り切らなければ、代数閉体 \(\Omega\) 上で群環はちょうど \(h\) 個の既約表現を持ち、それらはすべて一次である。したがってラジカル商はもとの群環と同じ階数を持ち、ラジカルは零になる。

証明では Abel 群を巡回群の直積 \(\mathfrak A=\mathfrak Z_1\times\cdots\times\mathfrak Z_t\) に分解する。各生成元は対応する表現で \(h_\nu\) 乗根へ写り、その選び方の総数が \(h_1\cdots h_t=h\) になる。

Simplified Chinese title: Abel 群环与不可约表示数

§15 令 \(\mathfrak A=\{a_1,\ldots,a_h\}\) 为 Abel 群。此时群环是交换的，因此可以应用交换超复系统的一般定理。

若特征 \(p\) 不整除 \(h\)，则在代数闭域 \(\Omega\) 上，群环恰有 \(h\) 个不可约表示，而且全都是一次表示。因此根基商与原群环秩相同，根基为零。

证明中把 Abel 群分解为循环群直积 \(\mathfrak A=\mathfrak Z_1\times\cdots\times\mathfrak Z_t\)。每个生成元在相应表示中映到一个 \(h_\nu\) 次单位根，而这些选择的总数为 \(h_1\cdots h_t=h\)。

Script/codepoint and TeX/PDF notes:

- Direct product of cyclic groups is 直積 / 直积; do not treat it as tensor-product evidence.
- Preserve \(\mathfrak A=\mathfrak Z_1\times\cdots\times\mathfrak Z_t\) and \(h=h_1\cdots h_t\).
- Lines 21572-21580 are OCR-heavy; characters and roots of unity are translated by mathematical context.

Unresolved flags:

- Root-of-unity and character phrasing needs domain review.
- OCR-damaged cyclic-factor proof needs source-image verification.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-21-003-principal-character-idempotent

Anchor: German baseline lines `21580-21610`; §15 principal character and idempotent summand.

Source summary: Names the h homomorphisms as characters, singles out the principal character, and computes the corresponding simple summand/idempotent E=(1/h)(a1+...+ah) when the group ring is fully reducible.

Japanese title: 主指標と冪等元成分

群環から代数閉体への \(h\) 個の準同型を、群に制限して見ると、単位根群への写像になる。これらが群の \(h\) 個の指標であり、すべての群元を \(1\) へ送る特別なものが主指標である。

主指標による表現は任意の群で可能であり、Abel 群に限られない。群環が完全可約であれば、この表現を与える単純成分が群環の中で分離するはずで、その成分を \(E\) として計算する。

計算から係数はすべて等しくなり、\(E^2=E\) の条件により、標数が \(h\) を割らない場合には \(E=\frac{1}{h}(a_1+\cdots+a_h)\) が得られる。標数が \(h\) を割る場合は \(E=0\) となり、完全可約性に反する。

Simplified Chinese title: 主特征标与幂等分量

从群环到代数闭域的 \(h\) 个同态，限制到群上就是到单位根群的映射。这些映射就是该群的 \(h\) 个特征标；其中把每个群元素都送到 \(1\) 的特殊特征标称为主特征标。

主特征标给出的表示对任意群都存在，并不只限于 Abel 群。若群环完全可约，则给出该表示的单分量应在群环中分离；文本把这个分量记为 \(E\) 并加以计算。

计算表明所有系数相等；再由 \(E^2=E\) 得到，当特征不整除 \(h\) 时，\(E=\frac{1}{h}(a_1+\cdots+a_h)\)。若特征整除 \(h\)，则 \(E=0\)，这与完全可约性相矛盾。

Script/codepoint and TeX/PDF notes:

- Hauptcharakter is 主指標 / 主特征标.
- Preserve \(E=\frac{1}{h}(a_1+\cdots+a_h)\), \(aE=E\), and \(E^2=E\).
- Line 21582 has OCR damage around the expression for E; the final formula at 21608-21609 is used as the stable anchor.

Unresolved flags:

- Principal-character wording needs native/domain review.
- Idempotent-component wording remains draft.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-21-004-character-relations

Anchor: German baseline lines `21611-21635`; §16 character relations.

Source summary: Derives the character relations from the principal-character idempotent: sums over all group elements vanish for non-principal characters and equal h for the principal character.

Japanese title: 指標関係式

§16 では、\(E=(1/h)\sum a_i\) が主指標を与えることから、指標関係式が直ちに導かれる。まず \(a\cdot e_i=e_i\cdot\Theta_i a\) とし、そこから \(\Theta_i e_j\) の値が Kronecker 型に決まる。

特に \(e_1=(1/h)\sum a_i\) を用いると、\(\sum_r \Theta_i a_r\) は、\(i=1\) すなわち主指標の場合には \(h\)、それ以外では \(0\) になる。

したがって、すべての群元にわたる一つの指標の和は、主指標を除いて零であり、主指標では \(h\) である。

Simplified Chinese title: 特征标关系式

§16 从 \(E=(1/h)\sum a_i\) 给出主特征标这一事实，直接推出特征标关系式。先有 \(a\cdot e_i=e_i\cdot\Theta_i a\)，继而 \(\Theta_i e_j\) 的取值呈 Kronecker 型。

特别地，由 \(e_1=(1/h)\sum a_i\) 可得，\(\sum_r \Theta_i a_r\) 在 \(i=1\)，也就是主特征标情形，等于 \(h\)；其他情形等于 \(0\)。

因此，一个特征标在所有群元素上的和，除主特征标外为零；对主特征标则为 \(h\)。

Script/codepoint and TeX/PDF notes:

- Charakterenrelationen is 指標関係式 / 特征标关系式.
- Preserve case formulas for \(\Theta_i e_j\), \(\Theta_i e_1\), and \(\sum_r\Theta_i a_r\).
- This character orthogonality relation is not a tensor-product or localization anchor.

Unresolved flags:

- Character-relation term needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-21-005-galois-theory-of-abelian-groups

Anchor: German baseline lines `21637-21683`; §17 Galois theory of abelian groups, character group.

Source summary: Builds an analogue of Galois theory for group rings of abelian groups: the homomorphisms/characters form a group isomorphic to the abelian group, and invariant subgroups/ranges are paired in a main theorem.

Japanese title: Abel 群の Galois 理論と指標群

§17 は、Abel 群の群環について、可換体の Galois 理論と似た定理が成り立つと述べる。Galois 理論で同型写像たちが群をなしたように、ここでも群環の準同型 \(\Theta_i\) たちを一つの群 \(\mathsf A\) にまとめる。

積を \((\Theta_i\Theta_k)(a)=\Theta_i(a)\Theta_k(a)\) で定めると、\(\Theta_i\) 全体は \(\mathfrak A\) と同型な \(h\) 元の群になる。巡回因子の生成元 \(z_\nu\) は原始 \(h_\nu\) 乗根 \(\varepsilon_{h_\nu}^{\varrho_\nu^{(i)}}\) へ写るため、各 \(\Theta_i\) に \(\prod_\nu z_\nu^{\varrho_\nu^{(i)}}\) を対応させられる。

さらに、\(\mathsf A\) の部分群 \(\mathsf B\) に対し、それに属する全 \(\Theta\) で \(1\) へ送られる \(\mathfrak A\)-元全体を不変領域と呼び、逆に \(\mathfrak A\) の部分群をすべて \(1\) へ送る \(\mathsf A\)-元全体を不変群と呼ぶ。主定理は、この二種類の部分群が一対一に対応するというものである。

Simplified Chinese title: Abel 群的 Galois 理论与特征标群

§17 说明，Abel 群的群环可建立与交换域 Galois 理论类似的定理。正如 Galois 理论中同构映射组成群，这里群环的同态 \(\Theta_i\) 也可合成为一个群 \(\mathsf A\)。

若定义乘积 \((\Theta_i\Theta_k)(a)=\Theta_i(a)\Theta_k(a)\)，则全部 \(\Theta_i\) 构成一个与 \(\mathfrak A\) 同构的 \(h\) 元群。循环因子的生成元 \(z_\nu\) 被映到原始 \(h_\nu\) 次单位根 \(\varepsilon_{h_\nu}^{\varrho_\nu^{(i)}}\)，所以可把 \(\Theta_i\) 对应到 \(\prod_\nu z_\nu^{\varrho_\nu^{(i)}}\)。

进一步，对 \(\mathsf A\) 的子群 \(\mathsf B\)，把所有被其中每个 \(\Theta\) 映到 \(1\) 的 \(\mathfrak A\)-元素组成的子群称为不变域；反过来，把把 \(\mathfrak A\) 的某个子群全都映到 \(1\) 的 \(\mathsf A\)-元素组成的子群称为不变群。主定理说，这两类子群一一对应。

Script/codepoint and TeX/PDF notes:

- Invariantenbereich is drafted as 不変領域 / 不变域 in this group-theoretic context, flagged because it is not a field here.
- Preserve \((\Theta_i\Theta_k)(a)=\Theta_i(a)\Theta_k(a)\), \(\Theta_i z_\nu=\varepsilon_{h_\nu}^{\varrho_\nu^{(i)}}\), and \(\prod_\nu z_\nu^{\varrho_\nu^{(i)}}\).
- This is group-ring/character material, not group algebra.

Unresolved flags:

- Invariantenbereich wording needs review; Chinese 不变域 may be misleading outside fields.
- Character-group duality passage needs domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-21-006-proof-and-dual-character-sum

Anchor: German baseline lines `21685-21768`; §17 proof and dual character relations.

Source summary: Proves the invariant subgroup/range correspondence using the general extension theorem, then swaps the roles of group elements and homomorphisms to derive the dual character sum over all characters.

Japanese title: 不変対応の証明と双対的指標和

主定理の証明では、まず不変群から不変領域が戻る方向を一般拡張定理に帰着する。不変群の元は、ある部分群を \(1\) へ送る準同型の全体拡張であり、不変領域へ制限すると拡張定理によって同値類へ分かれる。そこから指数が \(1\) になり、二つの部分群が一致する。

逆方向は、\(\mathfrak A\) の元 \(a\) を \(\mathsf A\) 上の準同型として見ることで、第一の方向へ帰着される。すなわち \(a\Theta=\Theta a\) と置けば、群積と準同型積が一致し、異なる群元は異なる準同型になる。

この双対的な見方により、すでに証明した主張を翻訳して、逆方向も得られる。最後に、\(\mathsf A\) に対する指標関係式として、\(\sum_{i=1}^{h}\Theta_i a_\nu\) は \(a_\nu\) が単位元なら \(h\)、そうでなければ \(0\) になる、と結論される。

Simplified Chinese title: 不变对应的证明与对偶特征标和

主定理的证明先把由不变群返回不变域这一方向归结为一般扩张定理。不变群的元素是把某个子群送到 \(1\) 的同态在整个群上的扩张；限制到不变域后，由扩张定理分成若干类，进而指数只能为 \(1\)，两个子群相等。

反方向通过把 \(\mathfrak A\) 的元素 \(a\) 看作 \(\mathsf A\) 上的同态而归结为第一方向。令 \(a\Theta=\Theta a\)，则群乘积与同态乘积一致，并且不同群元素给出不同同态。

在这种对偶观点下，把已证命题翻译回来，就得到反方向。最后得到关于 \(\mathsf A\) 的特征标关系式：\(\sum_{i=1}^{h}\Theta_i a_\nu\) 在 \(a_\nu\) 为单位元时等于 \(h\)，否则为 \(0\)。

Script/codepoint and TeX/PDF notes:

- Preserve \(a\Theta=\Theta a\), \(\Theta ab^{-1}=1\), and \(\sum_{i=1}^{h}\Theta_i a_\nu\).
- Lines 21709-21727 are OCR-damaged and have ambiguous subgroup symbols; draft follows the theorem structure only.
- No retained blocker changes; the \\otimes hit at line 21847 is outside this continuation and remains a later non-anchor to check in Chapter IV.

Unresolved flags:

- Subgroup symbol OCR in the proof needs source-image review.
- Dual character relation wording requires native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
