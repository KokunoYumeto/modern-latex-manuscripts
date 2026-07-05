# Noether CJK Draft Corpus Translation Slices Continuation 02

Generated UTC: `2026-07-04T05:36:12.680521+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical Japanese and Simplified Chinese prose only. Not native reviewed. Not approved. Not gate-promoted. No reviewer packet population and no Git push.

## Scope

This continuation adds three source-anchored draft slices from the abstract ideal-theory cluster of the German baseline. Korean remains addendum/source-discovery only.

Retained blockers unchanged: tensor product, localization, Harish-Chandra, abstract algebra, modern algebra.

## Slices

### cjk-continuation-02-001-finite-module-domains-chain-theorems

- Anchor: German baseline lines `14848-14920`; Abstrakter Aufbau der Idealtheorie; Kettensaetze in endlichen Modulbereichen.
- Source summary: Defines module domains over a ring, finite module domains, and transfers divisor/multiple chain conditions from ideals in the base ring to modules.
- Queue/context terms: `module, submodule, finitely generated, finite, Noetherian/Noether, Artinian/Artin, ideal`.
- Japanese title: 有限加群領域における鎖定理

**Japanese draft prose**

- ここでは、環に関する加群領域を、加法と環の元による乗法を備えた対象として置く。加法についてはアーベル群をなし、乗法は結合法則を満たし、二つの分配法則も成り立つ。
- 有限加群領域とは、有限個の元から作られるすべての線形形式で尽くされる加群領域である。基礎となる可換環が単位元をもち、そのイデアルに対して除数鎖条件または倍数鎖条件が成り立つなら、加群領域内の加群にも同じ鎖条件が移る。
- 証明は、各加群に有限個のイデアルを対応させ、真の除数または真の倍数が現れるたびに、そのうち少なくとも一つの対応イデアルも真に変化することを用いる。したがって、環側の鎖が有限で止まれば、加群側の鎖も有限で止まる。

- Simplified Chinese title: 有限模域中的链定理

**Simplified Chinese draft prose**

- 这里把相对于一个环的模域，定义为带有加法以及由环元素作乘法的对象。它在加法下成为阿贝尔群，乘法满足结合律，并且两个分配律也成立。
- 所谓有限模域，是指可由有限个元素生成的所有线性形式穷尽的模域。若底层交换环有单位元，并且其理想满足除子链条件或倍数链条件，那么模域中的模也满足相应的链条件。
- 证明的要点是给每个模配上有限个理想；每当模出现真除子或真倍数时，至少有一个对应理想也发生真变化。因此，只要环中的理想链在有限步停止，模中的相应链也必在有限步停止。

**Script/codepoint/TeX notes**

- Japanese uses 加群領域 as a literal draft for Modulbereich; Simplified Chinese uses 模域, both require native/domain review.
- Do not silently promote Teilerkettensatz/Vielfachenkettensatz to canonical Noetherian/Artinian adjectives in this slice.
- Keep CJK compounds intact around inline math; avoid splitting 鎖条件/链条件, 加群領域/模域, and イデアル/理想.

**Unresolved flags**

- Modulbereich has no approved CJK glossary entry in this lane; the rendering is descriptive and provisional.
- The source discusses chain conditions; modern Noetherian/Artinian labels remain contextual only.

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

### cjk-continuation-02-002-isomorphism-direct-sums-primary-ideals

- Anchor: German baseline lines `14998-15137`; Isomorphiesätze, direkte Summen, Primideale und Primärideale.
- Source summary: Defines module and ring homomorphisms/isomorphisms, residue-class modules/rings, isomorphism theorems, direct sums, prime ideals, primary ideals, and shortest primary decompositions.
- Queue/context terms: `homomorphism, isomorphism, quotient ring, module homomorphism, ideal, prime ideal, direct decomposition, ring`.
- Japanese title: 同型定理・直接和・素イデアルと準素イデアル

**Japanese draft prose**

- 二つの加群領域のあいだで、差と同じ環元による乗法が対応し、像が全体を尽くすとき、加群準同型が得られる。零元に対応する加群で合同を取ると剰余類加群が生じ、任意の準同型はこの剰余類加群への移行として表せる。
- 同じ構成は環とイデアルにも移される。イデアルで合同を取れば剰余類環が生じ、第一・第二同型定理が環同型の形で成り立つ。さらに、互いに素なイデアルの計算から、零イデアルの分解と環の直接和分解が対応することが示される。
- 続いて、剰余類環が零因子を持たない場合に素イデアルを定義し、零因子のべきが消える場合に準素イデアルを定義する。鎖条件のもとでは、各イデアルは有限個の最大準素成分による最短表示を持ち、対応する素イデアルは一意に定まる。

- Simplified Chinese title: 同构定理、直和、素理想与准素理想

**Simplified Chinese draft prose**

- 在两个模域之间，若差和同一环元素的乘法都相互对应，并且像覆盖整个目标，就得到模同态。以对应于零元的模取同余，便得到剩余类模；任意同态都可表示为向这种剩余类模的过渡。
- 同样的构造也适用于环和理想。按理想取同余得到剩余类环，第一、第二同构定理以环同构的形式成立。再由互素理想的计算，可知零理想的分解同环的直和分解相互对应。
- 随后，若剩余类环没有零因子，则相应理想称为素理想；若每个零因子的某个幂消失，则得到准素理想。在链条件下，每个理想都有由有限个最大准素分量构成的最短表示，并且相关的素理想唯一确定。

**Script/codepoint/TeX notes**

- Restklassenmodul/Restklassenring are rendered 剰余類加群/剰余類環 and 剩余类模/剩余类环 here to preserve the source wording; 商環/商环 remains an adjacent reviewer alternative for quotient-ring rows.
- Japanese 準素イデアル and Simplified Chinese 准素理想 are provisional for Primärideal.
- Use Japanese 同型/準同型 and Simplified Chinese 同构/同态 consistently; do not conflate module and ring homomorphisms.

**Unresolved flags**

- Primärideal terminology requires native/domain review in both lanes.
- Direct-sum decomposition is source-anchored, but no gate promotion is made for a direct-decomposition glossary entry.

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

### cjk-continuation-02-003-extension-rings-finite-rank-primary-sums

- Anchor: German baseline lines `15687-15843`; Erweiterungsringe von Körpern; Ringe endlichen Ranges; direkte Summe primärer Ringe.
- Source summary: Defines extension rings over fields, extension and contraction of ideals, finite-rank rings, double chain condition, decomposition into primary rings, and prime ideals of first and second kind.
- Queue/context terms: `field, ring, ideal, finite-dimensional, basis, module, prime ideal, quotient ring, direct decomposition`.
- Japanese title: 拡大環・有限階数の環・一次環への直接分解

**Japanese draft prose**

- 体を部分環として含む単位的な環を考え、上位の体を付け加えることで拡大環を作る。新しい元は、元の環の元を係数体の拡大で線形結合した形式として扱われ、線形独立性を拡大後にも保つように等号が定められる。
- 元の環のイデアルは拡大環の中で拡大イデアルになり、拡大環のイデアルを元の環と交わらせると縮小イデアルが得られる。拡大環の素イデアルを縮小すると、元の環でも素イデアルになる。
- 環が基礎体上有限階数であれば、イデアル全体に対して二重鎖条件が成り立つ。各イデアルは互いに素な準素イデアルの有限積として一意に表され、剰余類環は一次環の直接和として分解される。零イデアルの分解から得られる冪等元は、各成分を取り出す射影の役割を果たす。

- Simplified Chinese title: 扩张环、有限秩环与一次环的直和分解

**Simplified Chinese draft prose**

- 考虑含有一个域作为子环并带单位元的环；向其中添入一个上域，可以构造扩张环。新元素被看作原环元素在扩张系数域上的形式线性组合，并且等号的定义要求原有的线性无关性在扩张后仍保持。
- 原环中的理想在扩张环中给出扩张理想，而扩张环的理想同原环取交则给出收缩理想。扩张环中的素理想收缩以后，在原环中仍是素理想。
- 若该环在基域上有限秩，则所有理想满足双链条件。每个理想都可唯一表示为有限个两两互素的准素理想的乘积，剩余类环也相应分解为一次环的直和。由零理想分解得到的幂等元，起到投影到各个分量的作用。

**Script/codepoint/TeX notes**

- Japanese 拡大環 and Chinese 扩张环 are draft renderings for Erweiterungsring; source wording is structural, not a glossary approval.
- Japanese 有限階数 and Chinese 有限秩 are used for endlichen Ranges; distinguish from finite-dimensional vector-space wording where needed.
- Chinese 一次环 is provisional for primärer Ring; Japanese 一次環 is likewise provisional and should be checked against modern ring-theory register.

**Unresolved flags**

- Primärer Ring / rings erster und zweiter Art require native/domain review.
- Finite rank over a field is not automatically the same as finite-dimensional in every CJK sentence; the draft makes the base-field relation explicit.

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## Boundary

- No native review, approval, gate promotion, reviewer packet population, or Git push was performed.
- These slices extend draft corpus coverage but do not resolve the retained blockers.
- Full line-by-line CJK corpus completion still requires a separate full baseline chunk map and continued slice production.
