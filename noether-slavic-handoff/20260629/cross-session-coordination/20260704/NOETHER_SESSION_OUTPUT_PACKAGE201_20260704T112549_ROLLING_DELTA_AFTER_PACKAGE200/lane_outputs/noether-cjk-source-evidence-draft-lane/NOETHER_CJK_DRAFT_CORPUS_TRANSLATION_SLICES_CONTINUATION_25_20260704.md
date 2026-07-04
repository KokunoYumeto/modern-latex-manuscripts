# Noether CJK Draft Corpus Translation Slices: Continuation 25

Generated UTC: `2026-07-04T09:25:48.467678+00:00`

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

- tensor product: no German Tensorprodukt anchor in 22285-22352; direct-product/class-product formulas are not tensor-product evidence
- localization: Quotientenring candidates remain 16223-16225, 18467, 20105, 20228, 20240, 20284, 20949, 20953, and 21009, plus Quotientenkörper at 20822; no direct Lokalisierung label in 22285-22352
- Harish-Chandra: no German corpus anchor
- abstract algebra: no direct abstract-algebra anchor in §22 lines 22285-22352
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in this continuation
- group algebra: no new group-algebra evidence; §22 concerns factor-system class products and fixed-center bodies

## cjk-continuation-25-001-factor-systems-chapter-and-direct-product-formation

Anchor: German baseline lines `22285-22289`; Kapitel V §22 fixed center and direct product formation.

Source summary: Opens Chapter V on factor systems and fixes a commutative base field P. Matrix rings whose automorphism fields have finite rank over P and center P form a multiplicatively closed system under direct product formation, though not yet a group.

Japanese title: 因子系の章と直接積による積構成

第 V 章は因子系へ移り、§22 では中心を固定した体の群を扱う。基礎として、可換体 \(P\) を一つ固定する。

考える対象は、自己同型体が \(P\) 上有限階数を持ち、かつ中心が \(P\) そのものであるような行列環 \(\mathfrak R_r\) 全体である。二つのそのような環 \(\mathfrak R_r\) と \(\mathfrak L_s\) の直接積は、\(\mathfrak R_r\) の基礎体を \(\mathfrak L_s\) へ拡大して得られる環 \(\mathfrak R_r\times\mathfrak L_s=\mathfrak R_r\cdot\mathfrak L_s\) として定められる。

この直接積は可換であり、ふたたび中心 \(P\) を持つ行列環を与えるので、全体は乗法的に閉じている。ただしこの段階では群ではない。なぜなら \(\mathfrak R_r\times\mathfrak L_s=\mathfrak R_m\) なら \(m\ge rs\) となり、任意に逆元を見つけられるわけではないからである。

Simplified Chinese title: 因子系一章与直接积构造

第 V 章转入因子系；§22 讨论具有给定中心的除环所形成的群。首先固定一个交换域 \(P\)。

考察的对象是那些自同构域在 \(P\) 上有限秩、且中心正是 \(P\) 的矩阵环 \(\mathfrak R_r\)。两个这样的环 \(\mathfrak R_r\) 与 \(\mathfrak L_s\) 的直接积，定义为把 \(\mathfrak R_r\) 的基域扩张到 \(\mathfrak L_s\) 后得到的环：\(\mathfrak R_r\times\mathfrak L_s=\mathfrak R_r\cdot\mathfrak L_s\)。

这种直接积是交换的，并且仍给出中心为 \(P\) 的矩阵环，所以这些对象构成一个乘法封闭系统。但此时还不是群；若 \(\mathfrak R_r\times\mathfrak L_s=\mathfrak R_m\)，则必有 \(m\ge rs\)，不能总是找到逆元。

Script/codepoint and TeX/PDF notes:

- Faktorensysteme is 因子系 / 因子系 in this draft.
- Preserve \(\mathfrak R_r\times\mathfrak L_s=\mathfrak R_r\cdot\mathfrak L_s\), \(\mathfrak R_r\times\mathfrak R_s=\mathfrak R_s\times\mathfrak R_r\), and \(m\ge rs\).
- Direkte Produktbildung is direct-product formation; it is not a Tensorprodukt/tensor-product source anchor.
- Line 22289 has OCR noise in `Automorphismenkörper Rörper`; draft records the intended role but flags source quality.

Unresolved flags:

- Direct product wording needs domain review because the construction resembles scalar extension in ring-theoretic notation.
- OCR at line 22289 needs source-image verification before canonical text.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-25-002-product-of-classes-independent-of-representatives

Anchor: German baseline lines `22291-22301`; §22 classes of matrix rings and representative independence.

Source summary: Groups all matrix rings with the same underlying body into a class {R}; if representatives are changed within their classes, the product class remains the same, as shown by matrix-ring computations.

Japanese title: 代表元によらない類の積

つぎに、同じ \(\mathfrak R\) に属するすべての \(\mathfrak R_r\) を一つの類 \(\{\mathfrak R\}\) にまとめる。もし \(\mathfrak R_r,\mathfrak R_{r'}\) が同じ類に属し、\(\mathfrak L_s,\mathfrak L_{s'}\) も同じ類に属するなら、\(\mathfrak R_r\times\mathfrak L_s\) と \(\mathfrak R_{r'}\times\mathfrak L_{s'}\) も同じ類に属する。

このことを示すには、\(\mathfrak R\times\mathfrak L=\mathfrak M_m\) の場合に、\(\mathfrak R_r\times\mathfrak L_s\) が \(\mathfrak M\) 上の行列環になることを確認すればよい。本文は \(\mathfrak R_r\times\mathfrak L=\sum_1^r\mathfrak M_m c_{ik}\) および \(\mathfrak R_r\times\mathfrak L_s=\mathfrak M_{mrs}\) という計算でこれを示す。

したがって、二つの類 \(\{\mathfrak R\}\) と \(\{\mathfrak L\}\) の積を、代表元の積の類として定めても、その定義は代表元の選び方に依存しない。

Simplified Chinese title: 与代表元选择无关的类乘法

接着，把所有属于同一个 \(\mathfrak R\) 的 \(\mathfrak R_r\) 合并为一个类 \(\{\mathfrak R\}\)。若 \(\mathfrak R_r,\mathfrak R_{r'}\) 属于同一类，而 \(\mathfrak L_s,\mathfrak L_{s'}\) 也属于同一类，则 \(\mathfrak R_r\times\mathfrak L_s\) 与 \(\mathfrak R_{r'}\times\mathfrak L_{s'}\) 也属于同一类。

要证明这一点，只需在 \(\mathfrak R\times\mathfrak L=\mathfrak M_m\) 时说明 \(\mathfrak R_r\times\mathfrak L_s\) 是 \(\mathfrak M\) 上的矩阵环。文本通过 \(\mathfrak R_r\times\mathfrak L=\sum_1^r\mathfrak M_m c_{ik}\) 以及 \(\mathfrak R_r\times\mathfrak L_s=\mathfrak M_{mrs}\) 的计算完成证明。

因此，若把两个类 \(\{\mathfrak R\}\) 与 \(\{\mathfrak L\}\) 的乘积定义为任意代表元乘积所属的类，这个定义与代表元的选择无关。

Script/codepoint and TeX/PDF notes:

- Preserve \(\{\mathfrak R\}\), \(\mathfrak R_r\times\mathfrak L_s\), and \(\mathfrak M_{mrs}\).
- Class product is 類の積 / 类乘法 in this draft.
- Line 22299 has a compressed formula with missing punctuation; draft follows the surrounding matrix-ring computation.

Unresolved flags:

- Representative-independence terminology needs native/domain review.
- Formula at 22299 needs source-image review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-25-003-class-group-identity-and-reciprocal-inverse

Anchor: German baseline lines `22303-22307`; §22 class group, identity, and reciprocal inverse classes.

Source summary: The map from matrix rings to their classes is a homomorphism onto a multiplicatively closed system K; this system is shown to be a group, with identity {P} and inverse {Rbar}, where Rbar is reciprocal-isomorphic to R.

Japanese title: 類群、単位元、反同型による逆類

\(\mathfrak R_r\mapsto\{\mathfrak R_r\}\) は、すべての \(\mathfrak R_r\) から類全体への準同型である。類全体 \(\mathscr K\) は乗法的に閉じており、ここでそれが群であることを示す。

単位元は明らかに \(\{P\}\) であり、\(\mathfrak R_r\times P=\mathfrak R_r\) である。残るのは各類の逆元の存在である。

\(\{\mathfrak R\}^{-1}\) は、\(\mathfrak R\) と反同型な体 \(\overline{\mathfrak R}\) の類 \(\{\overline{\mathfrak R}\}\) と置くべきである。つまり、\(\mathfrak R\times\overline{\mathfrak R}\) が \(P\) 上の行列環になること、または階数 \(t^2\) の \(\mathfrak R\) に対し、その積が \(t^2\) 個の単純左イデアルへ分解することを示せばよい。

Simplified Chinese title: 类群、单位元与反同构逆类

映射 \(\mathfrak R_r\mapsto\{\mathfrak R_r\}\) 是从所有 \(\mathfrak R_r\) 到类集合的同态。类集合 \(\mathscr K\) 乘法封闭，下面证明它 actually 是一个群。

单位元显然是 \(\{P\}\)，因为 \(\mathfrak R_r\times P=\mathfrak R_r\)。剩下只需证明每个类都有逆元。

\(\{\mathfrak R\}^{-1}\) 应取为与 \(\mathfrak R\) 反同构的除环 \(\overline{\mathfrak R}\) 的类 \(\{\overline{\mathfrak R}\}\)。换言之，需要证明 \(\mathfrak R\times\overline{\mathfrak R}\) 是 \(P\) 上的矩阵环，或者当 \(\mathfrak R\) 的秩为 \(t^2\) 时，该乘积分解为 \(t^2\) 个单左理想。

Script/codepoint and TeX/PDF notes:

- Preserve \(\mathscr K\), \(\{P\}\), \(\{\mathfrak R\}^{-1}=\{\overline{\mathfrak R}\}\), and \(t^2\).
- Reziprok isomorpher Körper is 反同型な体 / 反同构除环 in this draft.
- The product \(\mathfrak R\times\overline{\mathfrak R}\) is direct-product/class multiplication, not tensor-product evidence.

Unresolved flags:

- Japanese 反同型な体 and Chinese 反同构除环 terminology needs native/domain review.
- Class-group notation should be checked against any existing glossary bridge.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-25-004-simple-body-definition-and-decomposition-theorem

Anchor: German baseline lines `22309-22315`; §22 simple bodies and direct-product decomposition theorem.

Source summary: Defines a simple body as one with no intermediate body over P having center P, then states that every body is the direct product of simple subfields/bodies.

Japanese title: 単純体の定義と直接積分解定理

つづいて、\(P\) と \(\mathfrak R\) の間に、中心も \(P\) であるような体が存在しないとき、\(\mathfrak R\) を単純体と呼ぶ。

この用語で述べられる定理は、任意の体 \(\mathfrak R\) が単純部分体の直接積として表せる、というものである。

すなわち、\(\mathfrak R=\mathfrak R^{(1)}\times\cdots\times\mathfrak R^{(p)}\) という形の分解が存在する。

Simplified Chinese title: 单除环的定义与直接积分解定理

接着定义：若在 \(P\) 与 \(\mathfrak R\) 之间不存在中心仍为 \(P\) 的中间除环，则称 \(\mathfrak R\) 为单除环。

用这个术语，文本给出定理：每个除环 \(\mathfrak R\) 都可写成单子除环的直接积。

也就是说，存在分解 \(\mathfrak R=\mathfrak R^{(1)}\times\cdots\times\mathfrak R^{(p)}\)。

Script/codepoint and TeX/PDF notes:

- Preserve \(\mathfrak R=\mathfrak R^{(1)}\times\cdots\times\mathfrak R^{(p)}\).
- Einfacher Körper is drafted as 単純体 / 单除环; this is not a simple ring closure for a glossary gate.
- The direct product in this theorem remains distinct from tensor product.

Unresolved flags:

- Terminology for einfacher Körper needs native/domain review.
- The theorem is draft-only and not a gate promotion for simple ring.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-25-005-complement-subfield-proof-by-class-inverse

Anchor: German baseline lines `22317-22339`; §22 complement subfield proof using inverse classes.

Source summary: To prove the decomposition theorem it suffices to find, for a subfield R^(1) with center P, a complement S with center P such that R^(1) x S = R. The proof uses the inverse class {R^(1)bar}, rank inequalities, matrix-ring decomposition, and automorphism fields of simple left ideals.

Japanese title: 逆類を用いた補完部分体の構成

分解定理の証明では、中心 \(P\) を持つ部分体 \(\mathfrak R^{(1)}\subseteq\mathfrak R\) が与えられたとき、同じく中心 \(P\) を持つ部分体 \(\mathfrak S\) で \(\mathfrak R^{(1)}\times\mathfrak S=\mathfrak R\) を満たすものを見つければ十分である。

類の群構造から、\(\{\mathfrak S\}=\{\overline{\mathfrak R^{(1)}}\}\times\{\mathfrak R\}\) と取れる。そこで \(\overline{\mathfrak R^{(1)}}\times\mathfrak R=\mathfrak S_\lambda\) と置き、\(\mathfrak R^{(1)}\times\mathfrak S_\lambda\) を計算する。

\(\mathfrak R^{(1)}\) の階数を \(t^2\) とすると、階数比較から \(\lambda\le t^2\) が得られる。一方、\(\mathfrak S_\lambda\) は \(\mathfrak R\) 上階数 \(1\) の単純イデアルへ分解しなければならないので \(\lambda\ge t^2\) であり、従って \(\lambda=t^2\) となる。このため \(\mathfrak R^{(1)}\times\mathfrak S\) 自身が体になり、対応する行列環の分解を通じて \(\mathfrak R\) と同型になる。

Simplified Chinese title: 用逆类构造补子除环

为了证明分解定理，只需说明：给定中心为 \(P\) 的子除环 \(\mathfrak R^{(1)}\subseteq\mathfrak R\)，可以找到同样中心为 \(P\) 的子除环 \(\mathfrak S\)，使 \(\mathfrak R^{(1)}\times\mathfrak S=\mathfrak R\)。

由类的群结构，可取 \(\{\mathfrak S\}=\{\overline{\mathfrak R^{(1)}}\}\times\{\mathfrak R\}\)。于是令 \(\overline{\mathfrak R^{(1)}}\times\mathfrak R=\mathfrak S_\lambda\)，再计算 \(\mathfrak R^{(1)}\times\mathfrak S_\lambda\)。

若 \(\mathfrak R^{(1)}\) 的秩为 \(t^2\)，秩比较给出 \(\lambda\le t^2\)。另一方面，\(\mathfrak S_\lambda\) 必须分解为在 \(\mathfrak R\) 上秩为 \(1\) 的单理想，所以 \(\lambda\ge t^2\)，因此 \(\lambda=t^2\)。于是 \(\mathfrak R^{(1)}\times\mathfrak S\) 本身是除环，并通过相应矩阵环的分解与 \(\mathfrak R\) 同构。

Script/codepoint and TeX/PDF notes:

- Preserve \(\{\mathfrak S\}=\{\overline{\mathfrak R^{(1)}}\}\times\{\mathfrak R\}\), \(\lambda=t^2\), and \(\mathfrak R^{(1)}\times\mathfrak S=\mathfrak R\).
- Line 22333 has severe OCR/substitution in the displayed formula; draft follows the rank-comparison proof and flags it.
- Automorphismenkörper der einfachen Linksideale remains 自己同型体 / 自同构域 of simple left ideals, provisional.

Unresolved flags:

- Lines 22327-22339 need source-image review for hats/bars/lambda indices.
- Complement-subfield terminology needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-25-006-inner-automorphism-finishes-direct-product-decomposition

Anchor: German baseline lines `22341-22352`; §22 inner automorphism final step.

Source summary: Finishes the decomposition proof by applying an inner automorphism to arrange the isomorphic copy of R^(1) back onto R^(1), thereby obtaining R = R^(1) x conjugated S.

Japanese title: 内的自己同型による直接積分解の仕上げ

最後に、前段で得られた同型を内的自己同型で調整する。本文は \(\lambda\in\mathfrak R_{t^2}\) による共役で、\(\mathfrak R\) を \(\lambda^{-1}(\mathfrak R^{(1)}\times\mathfrak S)\lambda\) として書く。

\(\lambda^{-1}\mathfrak R^{(1)}\lambda\) は \(\mathfrak R^{(1)}\) と同型な部分体である。定理 7 により、さらに適当な \(\mu\in\mathfrak R\) を用いて、これをもとの \(\mathfrak R^{(1)}\) へ戻すことができる。

その結果、\(\mathfrak R=\mathfrak R^{(1)}\times\mu^{-1}\lambda^{-1}\mathfrak S\lambda\mu\) となり、必要な直接積分解が得られる。

Simplified Chinese title: 以内自同构完成直接积分解

最后，用内自同构调整前一步得到的同构。文本通过 \(\lambda\in\mathfrak R_{t^2}\) 的共轭，把 \(\mathfrak R\) 写成 \(\lambda^{-1}(\mathfrak R^{(1)}\times\mathfrak S)\lambda\)。

\(\lambda^{-1}\mathfrak R^{(1)}\lambda\) 是与 \(\mathfrak R^{(1)}\) 同构的子除环。由定理 7，可再取适当的 \(\mu\in\mathfrak R\)，把它送回原来的 \(\mathfrak R^{(1)}\)。

于是得到 \(\mathfrak R=\mathfrak R^{(1)}\times\mu^{-1}\lambda^{-1}\mathfrak S\lambda\mu\)，从而完成所需的直接积分解。

Script/codepoint and TeX/PDF notes:

- Preserve \(\lambda^{-1}(\mathfrak R^{(1)}\times\mathfrak S)\lambda\), \(\mu^{-1}\lambda^{-1}\mathfrak S\lambda\mu\), and the final direct-product formula.
- This closes §22; §23 Faktorensysteme begins at line 22354.
- No retained blocker changes: this is direct-product/class material, not Tensorprodukt or Lokalisierung.

Unresolved flags:

- Conjugation notation needs source-image review for exact hats/bars in the preceding display.
- Direct-product decomposition wording remains draft pending domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
