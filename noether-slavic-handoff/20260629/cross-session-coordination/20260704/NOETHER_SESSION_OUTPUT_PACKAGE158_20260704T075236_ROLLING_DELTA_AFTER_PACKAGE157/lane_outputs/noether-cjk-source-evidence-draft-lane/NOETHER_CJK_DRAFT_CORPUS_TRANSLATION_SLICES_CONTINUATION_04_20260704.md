# Noether CJK Draft Corpus Translation Slices: Continuation 04

Generated UTC: `2026-07-04T05:46:28.290862+00:00`

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

## Retained Blockers And New Candidate Evidence

- tensor product: noisy otimes/product material remains non-anchor evidence only
- localization: new candidate quotient-ring construction at lines 16223-16225, but no direct Lokalisierung/localization label; not closed
- Harish-Chandra: no German corpus anchor
- abstract algebra: source-shelf/course-register evidence only
- modern algebra: Moderne Algebra remains bibliographic only

## cjk-continuation-04-001-completely-reducible-rings

Anchor: German baseline lines `15843-15902`; Vollständig reduzible Ringe.

Source summary: Defines completely reducible rings via the primary decomposition of the zero ideal, equivalently as finite direct sums of fields, and compares first-kind reducibility after extension to an algebraically closed field.

Japanese title: 完全可約環と第一種

ここで環 \(\mR\) は、零イデアルの積表示に現れるすべての準素成分が素イデアルになるとき、完全可約であると呼ばれる。同値に、\(\mR\) は有限個の体の直和として表される。さらに、すべての素イデアルが第一種である場合を完全可約第一種とし、そうでない場合を第二種と区別する。

基礎体が完全体なら第二種は現れず、特に代数閉体上では常に第一種だけが問題になる。代数閉包から作った拡大環 \(\bR=\mR[\bP]\) が完全可約であることと、元の環 \(\mR\) が完全可約第一種であることが同値である、というのがこの節の中心的な判定である。

証明は、拡大環での零イデアルの素成分を交わりで戻す方向と、第一種の成分が多項式の一次因子分解で直和に分かれる方向を組み合わせる。第二種では、べきが零になる非零元が拡大環に現れ、完全可約性が失われる。

Simplified Chinese title: 完全可约环与第一类

这里称环 \(\mR\) 为完全可约，是指零理想的乘积分解中出现的所有准素成分都成为素理想。等价地，\(\mR\) 可以表示为有限多个域的直和。若所有素理想都是第一类，则称为第一类完全可约；否则称为第二类。

当底域是完美域时，第二类不会出现；特别是在代数闭域上，只会遇到第一类。由代数闭包构造的扩张环 \(\bR=\mR[\bP]\) 完全可约，当且仅当原环 \(\mR\) 是第一类完全可约，这就是本节的核心判别。

证明一方面把扩张环中零理想的素成分通过取交拉回，另一方面利用第一类成分中的多项式一次因子分解得到直和分解。若处于第二类，则扩张环中会出现非零而某个幂为零的元素，从而破坏完全可约性。

Script/codepoint and TeX/PDF notes:

- Japanese 完全可約環 and Simplified Chinese 完全可约环 are source-literal draft renderings for vollständig reduzible Ringe.
- This is a semisimple-ring evidence candidate only; do not mark the modern semisimple-ring row approved from this slice.
- Direct-sum wording is additive ring decomposition, not tensor product.

Unresolved flags:

- Relation between vollständig reduzibel and modern semisimple ring terminology needs domain review.
- First-kind/second-kind terminology is source-era specific and not approved for canonical glossary promotion.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-04-002-matrix-representations-trace-discriminant

Anchor: German baseline lines `15903-15997`; Matrizendarstellung, Spuren und Diskriminanten bei Ringen endlichen Ranges.

Source summary: Associates matrices to multiplication on ideal bases, identifies the resulting homomorphic matrix ring with a residue-class ring, and defines trace, norm, and discriminant ideals relative to ideal classes.

Japanese title: 有限階数の環の行列表現・跡・判別式

有限階数の環 \(\mR\) を、零因子をもたない環 \(\mZ\) の拡大環として扱い、イデアル \(\ma\) の線形独立な \(\mZ\)-加群基底を選ぶ。任意の元 \(\gamma\) による乗法は、この基底に関する係数行列 \(C\) を定める。

元 \(\gamma\) を走らせて得られる行列全体は、\(\mR\) に準同型な行列環をなし、剰余類環 \(\mR/((0):\ma)\) と同型になる。基底を変えると行列環は相似変換で置き換わるので、イデアル類と表現類が一対一に対応する。

この表現から、クラスに関する元の跡とノルムを定義し、さらに基底 \(\varrho_i\) に対する行列式 \(|S_{(\ma)}(\varrho_i\varrho_k)|\) を判別式として扱う。判別式そのものではなく、それが \(\mZ\) に生成する主イデアルが不変量として用いられる。

Simplified Chinese title: 有限秩环的矩阵表示、迹与判别式

把有限秩环 \(\mR\) 看作无零因子环 \(\mZ\) 的扩张环，并选取理想 \(\ma\) 的一个线性无关的 \(\mZ\)-模基。任意元素 \(\gamma\) 的乘法作用，都会相对于这个基给出一个系数矩阵 \(C\)。

当 \(\gamma\) 遍历 \(\mR\) 时，所得矩阵全体形成一个与 \(\mR\) 同态的矩阵环，并且同构于剩余类环 \(\mR/((0):\ma)\)。改变基只会把矩阵环变为相似的矩阵环，因此理想类和表示类之间有一一对应。

由这个表示可以定义相对于某个类的元素迹与范数，并把基 \(\varrho_i\) 给出的行列式 \(|S_{(\ma)}(\varrho_i\varrho_k)|\) 作为判别式来处理。真正作为不变量使用的不是判别式本身，而是它在 \(\mZ\) 中生成的主理想。

Script/codepoint and TeX/PDF notes:

- Japanese 跡 and Simplified Chinese 迹 are draft renderings for Spur; トレース/迹 may need reviewer preference.
- 判別式/判别式 and ノルム/范数 are kept source-local and not promoted.
- Matrix conjugation notation such as P^{-1}R P should keep ASCII math and CJK punctuation separated in TeX.

Unresolved flags:

- Trace/norm terminology needs native/domain review.
- Residue-class ring wording should remain distinct from the separate localization blocker.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-04-003-direct-sums-of-classes

Anchor: German baseline lines `15998-16070`; Direkte Summen der Klassen.

Source summary: Shows that direct sums of ideal classes correspond to direct sums of representation classes, with block diagonal matrices, additive trace behavior, product behavior for discriminant ideals, and compatibility under extension rings.

Japanese title: クラスの直和と判別式イデアル

イデアル \(\ma\) が \(\mb+\mc\) という直和になっているなら、同じイデアル類に属する任意のイデアルも対応する直和に分かれる。このため、イデアル類の直和と、その成分クラスを語ることができる。

対応する行列表現では、基底を直和に合わせて選ぶと行列はブロック対角形になる。したがって、イデアル類の直和には表現類の直和が対応し、成分ごとの行列環も同型に取り出される。

跡は成分クラスに関する跡の和になり、成分イデアルの判別式イデアルは成分クラスで取ったものと一致する。全体の判別式イデアルは、成分の判別式イデアルの積として表され、拡大環に移ってもこの対応は保たれる。

Simplified Chinese title: 类的直和与判别式理想

如果理想 \(\ma\) 是 \(\mb+\mc\) 的直和，那么同一理想类中的任意理想也会分解为相应的直和。因此可以谈论理想类的直和以及它的成分类。

在对应的矩阵表示中，只要按直和选取基，矩阵就呈块对角形。因此，理想类的直和对应于表示类的直和，而各个成分的矩阵环也能同构地取出。

迹等于相对于各成分类所取迹的和，成分理想的判别式理想也等于在成分类中计算得到的判别式理想。整体的判别式理想则表示为各成分判别式理想的乘积，并且这种对应在过渡到扩张环时仍然保持。

Script/codepoint and TeX/PDF notes:

- Direct sum is additive decomposition of ideals/classes; explicitly not tensor product.
- Use 判別式イデアル/判别式理想 consistently for Diskriminantenideal.
- Block matrix displays should remain in TeX math blocks; CJK prose should not be inserted inside matrix environments.

Unresolved flags:

- Representation-class terminology remains provisional.
- Discriminant-ideal product wording should be reviewed against modern notation.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-04-004-discriminant-criterion-first-kind

Anchor: German baseline lines `16071-16163`; Diskriminantenkriterium der vollständigen Reduzibilität erster Art.

Source summary: Proves that a finite-rank ring over a field is completely reducible of the first kind iff its discriminant is nonzero, and expresses trace, norm, and discriminant through conjugate components.

Japanese title: 第一種完全可約性の判別式判定

ここでは再び \(\mR\) を体 \(P\) の拡大環とし、第一種完全可約性の必要十分条件が判別式の非消滅であることを示す。まず準素環を取り上げ、付随する素イデアルで割り切れる元の跡が、主クラスに関して消えることを特殊な加群基底から読む。

代数閉な基礎体上では、零イデアルそのものが素イデアルである場合には判別式イデアルは単位イデアルになる。一方、真に準素な環では、単位元以外の基底積の跡が消えるため、判別式は零になる。

したがって、有限階数の環は、判別式イデアルが単位イデアルであるとき、すなわち判別式が零でないときに限って第一種完全可約である。完全可約第一種の場合には、跡・ノルム・判別式は、ガロア的な拡大体内の共役成分を用いる通常の表示に戻る。

Simplified Chinese title: 第一类完全可约性的判别式判据

这里重新把 \(\mR\) 看作域 \(P\) 的扩张环，并证明第一类完全可约性的充要条件是判别式不为零。先考察准素环；利用特殊的模基，可以看出凡被所属素理想整除的元素，其相对于主类的迹都为零。

在代数闭底域上，如果零理想本身是素理想，则判别式理想成为单位理想。相反，若环是真正准素的，除单位元以外的基元素乘积的迹都消失，于是判别式为零。

因此，一个有限秩环当且仅当判别式理想为单位理想，也就是判别式非零时，才是第一类完全可约。此时，迹、范数和判别式可通过位于同一个伽罗瓦扩张域中的共轭成分，恢复为熟悉的表示。

Script/codepoint and TeX/PDF notes:

- This slice supports a semisimple-ring-adjacent source note but still uses source-era 完全可約/完全可约 wording.
- Japanese 共役成分 and Simplified Chinese 共轭成分 should be kept distinct from Galois-group terminology unless the source says so.
- Nonzero discriminant is source evidence, not a gate approval for any CJK row.

Unresolved flags:

- Fully reducible first-kind terminology needs reviewer treatment before any canonical bridge to semisimple ring.
- Trace/norm/discriminant typography needs later TeX/PDF CJK QA.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-04-005-discriminant-theorem-orders

Anchor: German baseline lines `16164-16239`; Diskriminantensatz für Ordnungen und Relativkörper.

Source summary: States the discriminant theorem for orders in algebraic number or function fields, transfers to quotient/residue rings modulo prime data, and generalizes to relative discriminant ideals over multiplication rings.

Japanese title: オーダーの判別式定理

数体または関数体のオーダーを扱うため、主イデアル環 \(\mo\) とその商体 \(\Omega\)、有限第一種拡大 \(K\)、そして \(\mo\) に関して整である元全体の環 \(\mO\) を置く。\(\mO\) を含む部分環をオーダーと呼び、\(\mO\) 自身を主オーダーと呼ぶ。

オーダー \(\mT\) の判別式は零でなく、また \(\mT\) の非零イデアルは有限個の互いに素な準素イデアルの積として一意に分解される。素元 \(p\) で割った剰余類環 \(\mT/\mT p\) は有限階数の環になり、判別式とイデアル分解はこの準同型の下で対応する。

判別式定理は、素元 \(p\) が \(\mT\) の判別式に現れるのは、\(\mT p\) の分解に真の準素成分または第二種の素イデアルが現れる場合に限る、という形になる。相対体では乗法環を基礎に置き、商環 \(\mT_{\mP}\) を使って同じ判定を判別式イデアルへ移す。

Simplified Chinese title: 序的判别式定理

为了处理数域或函数域中的序，先取一个主理想环 \(\mo\) 及其商域 \(\Omega\)，再取 \(\Omega\) 的有限第一类扩张 \(K\)，并令 \(\mO\) 为 \(K\) 中相对于 \(\mo\) 整的所有元素组成的环。包含 \(\mo\) 的 \(\mO\) 的任一子环称为序，而 \(\mO\) 本身称为主序。

序 \(\mT\) 的判别式不为零，并且 \(\mT\) 的任一非零理想都唯一地分解为有限多个两两互素的准素理想之积。模素元 \(p\) 的剩余类环 \(\mT/\mT p\) 是有限秩环；判别式和理想分解都在这个同态下相互对应。

判别式定理说，素元 \(p\) 出现在 \(\mT\) 的判别式中，当且仅当 \(\mT p\) 的分解中出现真正准素成分，或出现第二类素理想。在相对域情形中，以乘法环为底，并借助商环 \(\mT_{\mP}\) 把同一判据转化为关于判别式理想的命题。

Script/codepoint and TeX/PDF notes:

- Ordnung is rendered as オーダー in Japanese and 序 in Simplified Chinese to avoid false approval of a canonical algebraic-number-theory term.
- Lines 16223-16225 define a quotient-ring construction with denominators prime to an ideal; this is localization-adjacent candidate evidence, but not a direct Lokalisierung anchor.
- Multiplikationsring is rendered 乗法環/乘法环 only in notes/prose context and remains provisional.

Unresolved flags:

- Order/Ordnung terminology requires native/domain review.
- Localization blocker is not closed: the source says Quotientenring and gives a denominator condition, but does not name Lokalisierung/localization.
- Relative discriminant vocabulary needs a TeX/PDF rendering pass and source-era review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
