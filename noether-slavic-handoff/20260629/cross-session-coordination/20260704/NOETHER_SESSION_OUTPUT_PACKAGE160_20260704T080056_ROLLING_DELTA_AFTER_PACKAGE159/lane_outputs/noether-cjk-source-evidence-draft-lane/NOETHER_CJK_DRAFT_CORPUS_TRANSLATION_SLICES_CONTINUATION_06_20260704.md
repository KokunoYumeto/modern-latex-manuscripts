# Noether CJK Draft Corpus Translation Slices: Continuation 06

Generated UTC: `2026-07-04T05:58:59.019547+00:00`

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

- tensor product: no German Tensorprodukt anchor; noisy otimes/product material remains non-anchor evidence
- localization: Quotientenring candidate at 16223-16225 but no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: source-shelf/course-register evidence only
- modern algebra: Moderne Algebra remains bibliographic only

## cjk-continuation-06-001-reducible-representations-composition-factors

Anchor: German baseline lines `17714-17777`; Reduzible Darstellungen.

Source summary: Describes reducible representations from submodules, block triangular matrices, composition series, irreducible diagonal factors, direct sums of representation modules, and complete reducibility.

Japanese title: 可約表現と組成因子

表現加群 \(\mM\) に部分加群 \(\mU\) があり、\(\mU\) の基底を全体の基底へ拡張できるなら、対応する行列表現はブロック三角形になる。右上のブロックは零で、下側のブロックは \(\mU\) が与える表現を、もう一つの対角ブロックは商加群 \(\mM/\mU\) が与える表現を表す。

逆に、このようなブロック三角形の行列表現が与えられれば、最後の基底要素たちが作る部分は表現加群の部分加群になる。組成列を選ぶと、行列はさらに上三角のブロック列に分かれ、対角ブロックは組成因子 \(\mU_{\nu-1}/\mU_\nu\) による既約表現になる。

表現加群が直和 \(\mA+\mB\) に分かれる場合、対応する行列は対角ブロックになる。加群が完全可約なら、各ブロックは一つの既約表現からなり、このとき表現も完全可約と呼ばれる。ここでの完全可約は表現論上の記述であり、承認済み用語ではない。

Simplified Chinese title: 可约表示与合成因子

若表示模 \(\mM\) 有子模 \(\mU\)，并且 \(\mU\) 的基可以扩充为整个模的基，则对应的矩阵表示呈块上三角形。右上块为零；一个对角块给出由 \(\mU\) 诱导的表示，另一个对角块给出商模 \(\mM/\mU\) 诱导的表示。

反过来，若给定这种块上三角形矩阵表示，则最后若干个基元素生成表示模的一个子模。选择合成列后，矩阵可进一步化为上三角块形，对角块由合成因子 \(\mU_{\nu-1}/\mU_\nu\) 给出，并且是不可约表示。

当表示模分解为直和 \(\mA+\mB\) 时，相应矩阵成为对角块形。若该模完全可约，则每个块只含一个不可约表示，此时表示也称为完全可约。这里的完全可约是表示论语境下的描述，不是已批准术语。

Script/codepoint and TeX/PDF notes:

- Japanese 可約表現/既約表現 and Simplified Chinese 可约表示/不可约表示 are draft renderings for reducible/irreducible representations.
- Composition series terminology follows Continuation 03: 組成列/合成列, 組成因子/合成因子.
- Direct-sum/block-matrix language is not tensor-product evidence.

Unresolved flags:

- Representation-theory register needs native/domain review.
- The tiny overlap at 17714-17718 with the earlier broad representation slice is intentional for source continuity.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-06-002-unit-and-two-sided-component-action

Anchor: German baseline lines `17778-17820`; Direkte Summenzerlegung von Darstellungsmoduln bei Ringen mit Einheitselement.

Source summary: Splits a module over a unital ring into the part where the unit acts as identity and the part where it acts as zero, then decomposes modules along two-sided ideal components.

Japanese title: 単位元の作用と両側成分による分解

単位元をもつ環の加群 \(\mM\) は、単位元が単位作用素として働く部分 \(\mM_e\) と、零作用素として働く部分 \(\mM_0\) との直和に分かれる。実際、任意の元 \(m\) は \(em+(m-em)\) と書ける。

表現加群の場合、\(\mM_0\) はすべての元を零行列へ送る自明な表現を生む。したがって、この零作用の成分を切り離せば、単位元が単位行列に対応する表現だけを考えればよい。

さらに環が両側イデアルの直和 \(\mo=\ma_1+\cdots+\ma_s\) に分かれ、単位元も \(e_1+\cdots+e_s\) に分かれるなら、加群も \(\ma_i\mM\) の直和として分かれる。このため、表現論ではしばしば両側分解不能な環に制限して議論できる。

Simplified Chinese title: 单位元作用与双边成分分解

有单位元的环上的模 \(\mM\)，可分解为单位元作为恒等算子作用的部分 \(\mM_e\)，以及单位元作为零算子作用的部分 \(\mM_0\)。事实上，任意元素 \(m\) 都可写成 \(em+(m-em)\)。

在表示模情形，\(\mM_0\) 产生把每个元素都送到零矩阵的平凡表示。因此，分离出这个零作用成分后，只需考虑单位元对应单位矩阵的表示。

进一步，若环分解为双边理想直和 \(\mo=\ma_1+\cdots+\ma_s\)，单位元也分解为 \(e_1+\cdots+e_s\)，则模也分解为各 \(\ma_i\mM\) 的直和。因此，在表示论中常可把讨论限制到双边不可分解的环。

Script/codepoint and TeX/PDF notes:

- Trivial representation is rendered 自明な表現/平凡表示; reviewer may choose a different register.
- The \(em+(m-em)\) formula should keep CJK punctuation outside inline math.
- 両側分解不能/双边不可分解 remains provisional.

Unresolved flags:

- Unit-action terminology requires review.
- No localization or tensor-product blocker is affected.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-06-003-modules-over-completely-reducible-rings

Anchor: German baseline lines `17821-17853`; Modul- und Darstellungstheorie vollständig reduzibler Ringe.

Source summary: Shows that finite modules over a two-sided simple completely reducible ring with unit are completely reducible, with simple constituents operator-isomorphic to simple left ideals, and identifies the induced matrix representation.

Japanese title: 完全可約環上の加群と表現

環 \(\mo\) が完全可約で両側単純であり、加群 \(\mM\) が有限で単位元を単位作用素として持つなら、\(\mM\) 自身も完全可約になる。その単純成分は、\(\mo\) の単純左イデアル \(\ml_i\) と作用素同型である。

証明では \(\mo=\ml_1+\cdots+\ml_n\) と書き、\(\mM\) を有限個の \(\mo m_k\) から生成されるものとして、\(\ml_i m_k\) という成分へ分ける。零でない成分は \(\ml_i\) と同型な単純加群であり、重複して含まれるものを捨てると直和分解が得られる。

直接分解不能な \(\mM\) は単純で、ある \(\ml_i\) と同型になる。したがって、その表現クラスを調べるには、単純左イデアルが自己同型体上で与える行列表現を見ればよい。行列単位を使うと、元 \(c=\sum c_{ik}\alpha_{ik}\) は行列 \((\alpha_{ik})\) で表される。

Simplified Chinese title: 完全可约环上的模与表示

若环 \(\mo\) 完全可约且双边单，有限模 \(\mM\) 又以单位元作为恒等算子，则 \(\mM\) 本身完全可约。它的单成分与 \(\mo\) 的单左理想 \(\ml_i\) 算子同构。

证明把 \(\mo\) 写成 \(\ml_1+\cdots+\ml_n\)，并把 \(\mM\) 看作由有限多个 \(\mo m_k\) 生成，再分解成 \(\ml_i m_k\) 这些成分。非零成分同构于 \(\ml_i\)，因而是单模；删去已包含在前面和中的重复成分后，得到直和分解。

直接不可分解的 \(\mM\) 因而是单的，并同构于某个 \(\ml_i\)。所以研究其表示类时，只需考察单左理想在其自同构体上给出的矩阵表示。用矩阵单位表示时，元素 \(c=\sum c_{ik}\alpha_{ik}\) 对应矩阵 \((\alpha_{ik})\)。

Script/codepoint and TeX/PDF notes:

- 完全可約/完全可约 is still source-era vollständig reduzibel and not a promoted modern bridge.
- Automorphism field remains 自己同型体/自同构体 as a draft rendering.
- Matrix-unit notation \(c_{ik}\) must remain separate from CJK punctuation.

Unresolved flags:

- Automorphism-field terminology remains unresolved.
- This strengthens representation-module coverage but does not affect retained blockers.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-06-004-simple-composition-factors-radical-quotient

Anchor: German baseline lines `17854-17864`; Die einfachen Kompositionsfaktoren bei Moduln und Darstellungsmoduln.

Source summary: Shows that the radical annihilates every simple module or representation module, so simple composition factors are generated by simple left ideals of the radical quotient.

Japanese title: ラジカル商と単純組成因子

単位元をもつ環 \(\mo\) のラジカルを \(\mc\) とする。任意の単純加群または単純表現加群では、\(\mc\) の元は零として作用する。なぜなら \(\mc\mM\) は再び加群であり、単純性により \(\mM\) か零のどちらかだが、前者は \(\mc\) の冪零性に反するからである。

したがって、任意の加群や表現加群の単純組成因子は、商環 \(\mo/\mc\) の単純左イデアルによって生成される。表現を組成列で還元すると、対角上に現れる非零表現は、\(\mo/\mc\) の単純左イデアルが与えるものだけである。

ここでは追加の有限性条件を \(\mo\) に課さない。表現の絶対乗法子領域は有限な行列環の逆像として有限 \(P\)-加群になり、許容イデアルが \(P\)-加群であるため最大条件と最小条件が使える。

Simplified Chinese title: 根基商与单合成因子

设有单位元的环 \(\mo\) 的根基为 \(\mc\)。在任一单模或单表示模中，\(\mc\) 的元素都作为零作用。因为 \(\mc\mM\) 仍是模，按单性只能等于 \(\mM\) 或零；若为前者，则与 \(\mc\) 的幂零性矛盾。

因此，任意模或表示模的单合成因子，都由商环 \(\mo/\mc\) 的单左理想生成。把表示按合成列约化时，对角线上出现的非零表示，只能是由 \(\mo/\mc\) 的单左理想给出的表示。

这里不再对 \(\mo\) 加额外有限性条件。表示的绝对乘子域作为有限矩阵环的逆像，是有限 \(P\)-模；又因为允许理想都是 \(P\)-模，所以可使用最大条件和极小条件。

Script/codepoint and TeX/PDF notes:

- Absolute multiplier ring is translated descriptively: 絶対乗法子領域/绝对乘子域, not promoted.
- Radical quotient \(\mo/\mc\) is quotient-ring evidence, not localization.
- Keep \(\mc\mM\) as math-adjacent TeX; no CJK character should split the macro pair.

Unresolved flags:

- Absolute multiplier terminology needs reviewer attention.
- Radical quotient prose remains draft-only.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-06-005-hypercomplex-systems-burnside-regular-representation

Anchor: German baseline lines `17865-17924`; Darstellungen von Gruppen und hyperkomplexen Systemen; Einbeziehung der hyperkomplexen Systeme.

Source summary: Applies the representation theory to hypercomplex systems over a commutative field, counts irreducible representations by two-sided simple summands of the radical quotient, states Burnside-type results, and relates group representations to group rings.

Japanese title: 超複素系・Burnside 型定理・正則表現

可換体 \(P\) に関する超複素系では、イデアルは \(P\)-加群であるものだけを数える。このため左右のイデアルに最大条件と最小条件が成り立ち、前章の非可換イデアル論を適用できる。既約表現は、ラジカル商 \(\mo_0=\mo/\mc\) の単純左イデアルによって与えられる。

\(\mo_0\) が両側単純成分 \(\ma_1+\cdots+\ma_s\) に分かれるなら、非同値な既約表現の数はその成分数に等しい。体 \(P\) が代数閉なら、各自己同型体は \(P\) 自身に戻り、Burnside の定理として、\(P\) 上の \(n\) 次既約表現は \(n^2\) 個の線形独立な行列を含む。

ラジカルをもたない超複素系の任意の表現は完全可約である。正則表現は系そのもの、つまり単位イデアルを表現加群として用いる表現であり、群環の場合には群元を基底に選ぶ。したがって群の行列表示は群環の表現の特殊な場合になる。

Simplified Chinese title: 超复系统、Burnside 型定理与正则表示

对于交换域 \(P\) 上的超复系统，只把同时是 \(P\)-模的对象计为理想。因此左右理想都满足最大条件和极小条件，前一章的非交换理想论可以适用。不可约表示由根基商 \(\mo_0=\mo/\mc\) 的单左理想给出。

若 \(\mo_0\) 分解为双边单成分 \(\ma_1+\cdots+\ma_s\)，则互不等价的不可约表示数等于这些成分的个数。当 \(P\) 是代数闭域时，各自同构体回到 \(P\) 本身，于是得到 Burnside 定理：\(P\) 上的 \(n\) 阶不可约表示包含 \(n^2\) 个线性无关矩阵。

无根基的超复系统的任意表示都是完全可约的。正则表示是把系统自身，即单位理想，用作表示模所得的表示；在群环情形中，通常选取群元素作为基。因此，群的矩阵表示只是群环表示的一个特殊情形。

Script/codepoint and TeX/PDF notes:

- Burnside remains Latin-script; do not force a CJK transliteration without review.
- Group ring is 群環/群环 here; group algebra remains a separate row where German explicitly says Gruppenalgebra.
- 正則表現/正则表示 is provisional and should be reviewed.

Unresolved flags:

- Hypercomplex system terminology needs review.
- Group-ring/group-algebra distinction remains explicit and draft-only.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-06-006-base-field-extension-center-representations

Anchor: German baseline lines `17926-17983`; Erweiterung des Grundkörpers; Die Darstellungen des Zentrums.

Source summary: Extends hypercomplex systems to a larger base field, defines absolute irreducibility, studies centers under extension, and relates absolutely irreducible representation classes to homomorphisms of the center.

Japanese title: 基礎体の拡大と中心の表現

超複素系 \(\mo=a_1P+\cdots+a_hP\) と基礎体 \(P\) の拡大体 \(\Omega\) があるとき、同じ基底元と同じ乗法規則を用いて \(\mo\Omega=a_1\Omega+\cdots+a_h\Omega\) を作ることができる。もとの表現は基底元の行列で決まるため、\(\mo\Omega\) の表現へ拡張される。

イデアル、表現加群、表現が代数閉体へ移っても既約であり続けるとき、それを絶対既約と呼ぶ。拡大後にラジカルがなければ元の系にもラジカルはないが、その逆は一般には成り立たない。

中心 \(\mZ\) の表現については、代数閉体 \(\Omega\) での可換超複素系の既約表現は一次であり、\(\mZ\) から \(\Omega\) への準同型に一致する。ラジカルをもたない場合、\(\mo\) の絶対既約表現クラスと中心の一次表現クラスは一対一に対応する。

Simplified Chinese title: 基域扩张与中心的表示

给定超复系统 \(\mo=a_1P+\cdots+a_hP\) 以及基域 \(P\) 的扩张域 \(\Omega\)，可用同一组基元素和同一乘法规则构造 \(\mo\Omega=a_1\Omega+\cdots+a_h\Omega\)。原来的表示由基元素的矩阵决定，因此会诱导出 \(\mo\Omega\) 的表示。

若理想、表示模或表示在过渡到代数闭域后仍不可约，则称为绝对不可约。若扩张后的系统无根基，则原系统也无根基；但反过来一般不成立。

对于中心 \(\mZ\) 的表示，在代数闭域 \(\Omega\) 上，交换超复系统的不可约表示都是一次的，并且正是从 \(\mZ\) 到 \(\Omega\) 的同态。无根基情形中，\(\mo\) 的绝对不可约表示类与中心的一次表示类一一对应。

Script/codepoint and TeX/PDF notes:

- Absolute irreducibility is 絶対既約/绝对不可约, provisional.
- Use 基礎体/基域 for Grundkörper in this slice; reviewer may prefer base field wording.
- The center correspondence is representation-source evidence only, not a glossary approval.

Unresolved flags:

- Base-field extension and absolute irreducibility terms need review.
- No Harish-Chandra anchor is present.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-06-007-abelian-groups-system-determinant

Anchor: German baseline lines `17984-18073`; Anwendung auf Abelsche Gruppen; Determinante eines hyperkomplexen Systems.

Source summary: Applies the preceding center theory to finite abelian groups and their group rings, identifies characters, and defines the system matrix/determinant for hypercomplex systems, including regular group matrices.

Japanese title: アーベル群・群環・系の判別行列式

有限アーベル群 \(G=G_1\times\cdots\times G_r\) を巡回群に分解し、体 \(P\) の標数が群の位数を割らないと仮定する。群環は多項式環 \(P[x_1,\ldots,x_r]\) の剰余として表され、拡大体では定義イデアルが互いに異なる素イデアルの積または交わりに分かれる。

この交わりに対応して、拡大した群環は一次の体成分の直和に分かれる。各成分は群元 \(a_i\) を根 \(\xi_i^{(\alpha_i)}\) へ送る表現を与え、これらがアーベル群の指標である。その個数は群の位数 \(h\) に等しい。

一般の超複素系では、未定元 \(x_i\) を用いて一般元 \(w=a_1x_1+\cdots+a_hx_h\) を作り、表現に対応する行列 \(W=A_1x_1+\cdots+A_hx_h\) を系行列と呼ぶ。その行列式が系判別行列式であり、群環の場合には群行列になる。可換系ではこの行列式が一次因子に分解し、それらが指標を与える。

Simplified Chinese title: 阿贝尔群、群环与系统行列式

把有限阿贝尔群 \(G=G_1\times\cdots\times G_r\) 分解为循环群，并假定域 \(P\) 的特征不整除群阶。群环可表示为多项式环 \(P[x_1,\ldots,x_r]\) 的剩余类；在扩张域中，定义理想分解为互不相同的素理想之积或交。

与这个交对应，扩张后的群环分解为一次域成分的直和。每个成分给出把群元素 \(a_i\) 送到根 \(\xi_i^{(\alpha_i)}\) 的表示，这些表示就是阿贝尔群的特征标；其个数等于群阶 \(h\)。

对于一般超复系统，引入不定元 \(x_i\)，形成一般元素 \(w=a_1x_1+\cdots+a_hx_h\)，并把表示对应的矩阵 \(W=A_1x_1+\cdots+A_hx_h\) 称为系统矩阵。它的行列式是系统行列式；在群环情形中就是群矩阵。交换系统的系统行列式分解为一次因子，而这些因子正给出特征标。

Script/codepoint and TeX/PDF notes:

- Abeleian/abelian group is アーベル群/阿贝尔群; character is 指標/特征标, both draft.
- Systemdeterminante is rendered 系判別行列式 in Japanese and 系统行列式 in Simplified Chinese; this asymmetry is flagged for review.
- Group ring stays 群環/群环; group algebra is not inserted unless German says Gruppenalgebra.

Unresolved flags:

- System determinant terminology needs native/domain review.
- This leads into the existing cjk-corpus-014 slice at line 18074; no duplicate trace/character slice is added here.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
