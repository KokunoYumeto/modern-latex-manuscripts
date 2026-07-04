# Noether CJK Draft Corpus Translation Slices: Continuation 13

Generated UTC: `2026-07-04T08:16:28.381095+00:00`

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

- tensor product: no German Tensorprodukt anchor; Paper 42 direct-sum/direct-product style wording is non-anchor evidence
- localization: Quotientenring candidates now at 16223-16225, 18467, and Paper 42 line 20105, but no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: Paper 41 Theorie der Algebren remains contextual only; no new abstract-algebra anchor in Paper 42
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in Paper 42

## cjk-continuation-13-001-paper42-introduction-split-crossed-products

Anchor: German baseline lines `19943-19953`; Paper 42 introduction.

Source summary: Introduces split crossed products, non-Galois splitting fields, maximal orders, their ideals, and the division into regions by intersection with the splitting field.

Japanese title: 分解する交差積と極大整環の導入

第42論文は、分解する交差積、すなわち分解する代数を与え、因子系が一に随伴する交差積から始める。この場合は、非 Galois の分解体、すなわち最大可換部分体を用いるときにも、状況をかなり明示的に追うことができる。

§1 では基礎的な代数的事実を扱い、§2 では基礎体が代数的数体の場合に、基礎となる分解体 \(k\) の加群と補加群によって、すべての極大整環とそのイデアルを明示的に表す。

さらに極大整環を領域に分ける。ある領域には、\(k\) との共通部分が同じ極大整環をすべて入れる。これにより領域は \(k\) の整環と一対一に対応し、主整環に対応する領域が主領域になる。

Simplified Chinese title: 分裂交叉积与极大阶的引言

第42篇论文从分裂交叉积开始，即从给出分裂代数、且因子系统与一相伴的交叉积开始。在这种情形下，即使使用非 Galois 的分裂域，也就是最大交换子域，结构仍可相当明确地追踪。

§1 处理相关的简单代数事实；§2 在基域为代数数域时，用基础分裂域 \(k\) 的模与补模，明确表示所有极大阶及其理想。

随后把极大阶分入各个区域：同一区域包含那些与 \(k\) 的交相同的极大阶。这样，区域与 \(k\) 中的阶一一对应，而主阶对应的区域称为主区域。

Script/codepoint and TeX/PDF notes:

- Maximalordnung is rendered provisionally as 極大整環 / 极大阶.
- Gebiet/Hauptgebiet is rendered provisionally as 領域/主領域 and 区域/主区域.
- Komplementärmodul is 補加群 / 补模, paired with C11's 補基 / 补基.

Unresolved flags:

- Maximal-order, order, and region terms need native/domain review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-13-002-matrix-units-complementary-bases

Anchor: German baseline lines `19955-20014`; §I matrix units and complementary bases.

Source summary: For split crossed products with factor system one, constructs matrix units from a basis and complementary basis of k/Omega using the trace element E_G.

Japanese title: 行列単位と補基

\(\Omega\) を任意の基礎体、\(k/\Omega\) を次数 \(n\) の分離 Galois 拡大とし、Galois 群を \(\Gg\) とする。因子系一の交差積、すなわち分解する代数は \(K=\Gg\times k=u_{S_1}k+\cdots+u_{S_n}k\)、\(u_Su_T=u_{ST}\)、\(zu_S=u_Sz^S\) と書かれる。

\(E_\Gg=\sum_{S\in\Gg}u_S\) とおくと、\(E_\Gg u_S=u_SE_\Gg=E_\Gg\)、さらに \(E_\Gg zE_\Gg=E_\Gg\Sp(z)\) が成り立つ。ここで \(\Sp(z)\) は \(k/\Omega\) の跡である。

基底 \(a_1,\ldots,a_n\) とその補基 \(\bar a_1,\ldots,\bar a_n\) に対して、\(c_{ik}=\bar a_iE_\Gg a_k\) は \(K\) の行列単位の系を与える。したがって \(K=kE_\Gg k=\sum_{i,k}(\bar a_iE_\Gg a_k)\Omega\) と表される。

Simplified Chinese title: 矩阵单位与补基

令 \(\Omega\) 为任意基域，\(k/\Omega\) 为 \(n\) 次可分 Galois 扩张，Galois 群为 \(\Gg\)。因子系统为一的交叉积，也就是分裂代数，可写作 \(K=\Gg\times k=u_{S_1}k+\cdots+u_{S_n}k\)、\(u_Su_T=u_{ST}\)、\(zu_S=u_Sz^S\)。

置 \(E_\Gg=\sum_{S\in\Gg}u_S\)，则有 \(E_\Gg u_S=u_SE_\Gg=E_\Gg\)，并且 \(E_\Gg zE_\Gg=E_\Gg\Sp(z)\)。这里 \(\Sp(z)\) 表示 \(z\) 作为 \(k/\Omega\) 元素的迹。

若 \(a_1,\ldots,a_n\) 是一个基，\(\bar a_1,\ldots,\bar a_n\) 是对应补基，则 \(c_{ik}=\bar a_iE_\Gg a_k\) 给出 \(K\) 的一组矩阵单位。因此 \(K=kE_\Gg k=\sum_{i,k}(\bar a_iE_\Gg a_k)\Omega\)。

Script/codepoint and TeX/PDF notes:

- Matrizeneinheiten is 行列単位 / 矩阵单位.
- Komplementärbasis reuses 補基 / 补基.
- Keep \(E_\Gg\), \(c_{ik}\), and \(\Sp\) as TeX macros; downstream TeX/PDF should not expand them as text.

Unresolved flags:

- Trace and complementary-basis wording remains draft-only.
- Direct sum of fields is not tensor-product evidence.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-13-003-nongalois-splitting-fields-idempotents

Anchor: German baseline lines `20015-20051`; §I non-Galois splitting fields via Galois closure.

Source summary: Extends the representation K=kE_G k to non-Galois splitting fields in characteristic zero by passing to the Galois closure and using subgroup idempotents.

Japanese title: 非 Galois 分解体と冪等元

\(\Omega\) が標数零の場合、分解する代数の表示 \(K=kE_\Gg k\) は、\(k\) が \(K/\Omega\) の非 Galois 分解体であっても成り立つ。そこで、\(k\) に属する Galois 体 \(\bar k\) とその群 \(\bar\Gg\) に移る。

\(k\) に対応する部分群を \(\Hh\) とし、\(E_\Hh=\frac1h\sum_{H\in\Hh}u_H\)、\(E_\Gg=\frac1hE_{\bar\Gg}\) と定める。すると \(E_\Hh\) は \(\Hh\) の単位表現を、\(E_\Gg\) は \(\bar\Gg\) の単位表現を生成する。

この構成により、\(E_\Gg\) と \(u_{S_i}=E_\Hh\bar u_{S_i}\) について必要な関係式が保たれ、上と同様に \(K=kE_\Gg k\) が得られる。非分解の場合にも、\(K\) は \(E_\Hh\bar K E_\Hh\) と同型になり、左イデアルの自己同型環を通じて \(\bar K\) と相似になる。

Simplified Chinese title: 非 Galois 分裂域与幂等元

当 \(\Omega\) 的特征为零时，即使 \(k\) 是 \(K/\Omega\) 的非 Galois 分裂域，分裂代数的表示 \(K=kE_\Gg k\) 仍然成立。于是转到属于 \(k\) 的 Galois 域 \(\bar k\) 及其群 \(\bar\Gg\)。

令 \(\Hh\) 为对应于 \(k\) 的子群，并定义 \(E_\Hh=\frac1h\sum_{H\in\Hh}u_H\)、\(E_\Gg=\frac1hE_{\bar\Gg}\)。这样，\(E_\Hh\) 生成 \(\Hh\) 的单位表示，而 \(E_\Gg\) 生成 \(\bar\Gg\) 的单位表示。

通过这个构造，\(E_\Gg\) 与 \(u_{S_i}=E_\Hh\bar u_{S_i}\) 保留所需关系，因而仍得到 \(K=kE_\Gg k\)。在非分裂情形，也有 \(K\) 同构于 \(E_\Hh\bar K E_\Hh\)，并通过左理想的自同构环与 \(\bar K\) 相似。

Script/codepoint and TeX/PDF notes:

- Use 冪等元 / 幂等元 for idempotent.
- Do not collapse Galois closure and splitting field terms; ̄ over k remains TeX.
- Keep \(E_\Hh\bar K E_\Hh\) and subgroup coset formulas in TeX.

Unresolved flags:

- Non-Galois splitting-field phrasing needs review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-13-004-maximal-orders-and-regions

Anchor: German baseline lines `20053-20096`; §II maximal orders of split crossed products.

Source summary: Describes maximal orders O_a, their left and reciprocal right ideals, exhausts all maximal orders, and groups them into regions by intersection with k.

Japanese title: 極大整環・左右イデアル・領域

§II では、\(\Omega\) を有限代数的数体、\(K\) を \(\Omega\) 上 \(n\) 次の分解する代数、\(k\) を最大可換部分体とする。\(a,\bar a\) を \(k\) の相補的な有限 \(\oo\)-加群の組とすると、\(\mathcal O_a=\bar aE_\Gg a\) は \(K\) の極大整環であり、特に \(\mathcal O=oE_\Gg o\) も極大整環になる。

\(\mathcal O\) から \(\mathcal O_a\) への変換は左イデアル \(\mathcal L=oE_\Gg a\) と、これに対応する相反的右イデアル \(\mathcal R=\bar aE_\Gg o\) によって行われる。さらに、すべての左右イデアルとすべての極大整環はこの形で尽くされる。

極大整環 \(\mathcal O_a\) を走らせると、交わり \([\mathcal O_a,k]\) は \(k\) のすべての整環を走り、各場合に \(a\) の整環と一致する。同じ \(k\) の整環に属する極大整環をまとめたものが領域である。

Simplified Chinese title: 极大阶、左右理想与区域

§II 中令 \(\Omega\) 为有限代数数域，\(K\) 为 \(\Omega\) 上 \(n\) 次分裂代数，\(k\) 为最大交换子域。若 \(a,\bar a\) 是 \(k\) 中一对互补的有限 \(\oo\)-模，则 \(\mathcal O_a=\bar aE_\Gg a\) 是 \(K\) 中的极大阶，特别地 \(\mathcal O=oE_\Gg o\) 也是极大阶。

从 \(\mathcal O\) 到 \(\mathcal O_a\) 的变换由左理想 \(\mathcal L=oE_\Gg a\) 及其相应的倒右理想 \(\mathcal R=\bar aE_\Gg o\) 给出。进一步，所有左右理想和所有极大阶都由这种形式穷尽。

当 \(\mathcal O_a\) 遍历全部极大阶时，交 \([\mathcal O_a,k]\) 遍历 \(k\) 中所有阶，并且每次都等于 \(a\) 的阶。把属于同一个 \(k\)-阶的极大阶合在一起，就得到一个区域。

Script/codepoint and TeX/PDF notes:

- Order/Ordnung is rendered 整環 in Japanese and 阶 in Simplified Chinese; both flagged.
- reciprocal right ideal is 相反的右イデアル / 倒右理想, provisional.
- Keep \(\mathcal O_a\), \(\mathcal L\), and \(\mathcal R\) in TeX.

Unresolved flags:

- Japanese Ordnung as 整環 risks confusion with domain; needs native/domain review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-13-005-local-components-and-quotient-ring-candidate

Anchor: German baseline lines `20098-20150`; §II theorem 4a and proofs via local components.

Source summary: Specializes to the main region, proves the maximal-order statements by passage to p-components and quotient rings, and characterizes links as extensions of k-ideals.

Japanese title: 主領域・局所成分・商環候補

主領域、すなわち \(k\) の主整環 \(o\) を含む極大整環全体からなる領域では、変換は \(aE_\Gg b\) の形のイデアルで行われる。ここで \(a,b\) は \(k\) のイデアルである。したがって、右整環に \(o\) を含む左イデアルは、\(o\)-イデアルの拡大になる。

証明は各素イデアル \(p\) における成分へ移ることに基づく。本文では `Quotientenring nach \(p\)' への移行が用いられ、\(\mathcal C\) がすべての拡大加群 \(\mathcal C_p\) の交わりであることが示される。

この商環の言及は局所成分の証明装置であって、未解決の localization 行に対する直接の `Lokalisierung' アンカーではない。成分がすべて極大整環なら全体も極大整環であり、補基から得られる行列単位を使って \(\mathcal O_{a,p}\) の極大性が出る。

Simplified Chinese title: 主区域、局部分量与商环候选

在主区域中，也就是在包含 \(k\) 的主阶 \(o\) 的所有极大阶所成区域中，变换由形如 \(aE_\Gg b\) 的理想给出，其中 \(a,b\) 是 \(k\) 的理想。因此，右阶中含有 \(o\) 的左理想，就是一个 \(o\)-理想的扩张。

证明依靠转到每个素理想 \(p\) 处的分量。文本使用了到 `Quotientenring nach \(p\)' 的过渡，并证明 \(\mathcal C\) 是所有扩张模 \(\mathcal C_p\) 的交。

这里的商环提法是局部分量证明的工具，并不是未解决 localization 行的直接 `Lokalisierung' 锚点。若所有分量都是极大阶，则整体也是极大阶；再由补基给出的矩阵单位推出 \(\mathcal O_{a,p}\) 的极大性。

Script/codepoint and TeX/PDF notes:

- Records a new localization-adjacent Quotientenring candidate at line 20105 without closing localization.
- Quotientenring is 商環 / 商环 here, not a promoted localization rendering.
- Keep \(p\), \(\mathcal C_p\), and \(\mathcal O_{a,p}\) in TeX.

Unresolved flags:

- Localization remains blocked: no direct German Lokalisierung label.
- Order/ideal terminology remains draft-only.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-13-006-arbitrary-crossed-products-main-regions-different

Anchor: German baseline lines `20152-20191`; §III maximal orders of arbitrary crossed products.

Source summary: Extends the main-region statements to arbitrary crossed products by refining regions using ramified p-adic components, and formulates results for ideals prime to the different.

Japanese title: 任意の交差積・主領域・ディッフェレント

§III では、分解する交差積について得た定理を、領域の分け方を細かくすることで一般の場合へ移す。最大可換部分体 \(k\) に関する領域には、\(k\) との共通部分が同じで、さらに \(K\) の分岐場所で同じ \(p\)-進成分をもつ極大整環を入れる。

主領域については、同じ主領域の極大整環が、\(k\) のイデアルの拡大イデアルによる変換で互いに移る。とくに、主領域の極大整環の左イデアルで、ディッフェレントと素であり、右整環に \(o\) を含むものは、\(k\) のイデアルの拡大である。

一般の領域でも、極大整環はディッフェレントと素なイデアルによって互いに移る。ただしそのイデアルは、各場所で §II の形に従う加群から作られる。最後に、分解体による算術的な領域分けがどの程度代数的分解体を特徴づけるか、という未解決の方向が示される。

Simplified Chinese title: 任意交叉积、主区域与不同式

§III 通过细化区域划分，把分裂交叉积中得到的定理移到一般情形。相对于最大交换子域 \(k\) 的一个区域，包含那些与 \(k\) 的交相同、且在 \(K\) 的分歧处具有相同 \(p\)-进分量的极大阶。

对于主区域，同一主区域中的极大阶通过 \(k\)-理想的扩张理想彼此变换。特别地，主区域中极大阶的左理想，如果与不同式互素，并且其右阶含有 \(o\)，就是来自 \(k\)-理想的扩张。

在任意区域中，极大阶也通过与不同式互素的理想彼此变换；这些理想在每个局部处由 §II 所述相关阶的模组合而成。结尾提出一个方向：这种按区域的算术划分在多大程度上能刻画代数上的分裂域。

Script/codepoint and TeX/PDF notes:

- Differente follows C07: ディッフェレント / 不同式, flagged.
- zur Differente prime Ideale is rendered descriptively as ideals prime to the different.
- Quaternionenkörper example is summarized only; no long source quotation copied.

Unresolved flags:

- Differente terminology still needs source cross-check and native review.
- No tensor product, Harish-Chandra, abstract algebra, or modern algebra closure.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
