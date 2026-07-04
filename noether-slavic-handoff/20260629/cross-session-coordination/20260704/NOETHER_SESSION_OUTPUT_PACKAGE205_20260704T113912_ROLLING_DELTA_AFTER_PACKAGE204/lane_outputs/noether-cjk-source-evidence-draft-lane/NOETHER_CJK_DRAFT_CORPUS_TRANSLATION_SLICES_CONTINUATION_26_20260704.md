# Noether CJK Draft Corpus Translation Slices: Continuation 26

Generated UTC: `2026-07-04T09:38:22.822113+00:00`

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

- tensor product: no German Tensorprodukt anchor in 22354-22473; no otimes hit in this continuation
- localization: Quotientenring candidates remain 16223-16225, 18467, 20105, 20228, 20240, 20284, 20949, 20953, and 21009, plus Quotientenkörper at 20822; no direct Lokalisierung label in 22354-22473
- Harish-Chandra: no German corpus anchor
- abstract algebra: no direct abstract-algebra anchor in §23 lines 22354-22473
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in this continuation
- group algebra: no new group-algebra evidence; §23 concerns factor systems and pseudomatrix units

## cjk-continuation-26-001-splitting-field-galois-extension-and-left-ideal-decomposition

Anchor: German baseline lines `22354-22380`; §23 factor systems: splitting field, Galois field, simple left ideals.

Source summary: Starts §23 by assuming P is perfect or an equivalent maximal-commutative-subfield condition, fixes a splitting field Z of the noncommutative body R, takes the Galois field Gamma of Z, and decomposes R_{r Gamma} into conjugate simple left ideals.

Japanese title: 分解体、Galois 体、単純左イデアル分解

§23 では因子系を本格的に導入する。以下では基礎体 \(P\) を完全体と仮定するが、より一般には、中心 \(P\) を持つ非可換体 \(\mathfrak R\) について、各 \(\mathfrak R_r\) が \(P\) 上第一種の極大可換部分体を含む、という仮定で足りると述べられる。

\(\mathfrak Z\) を中心 \(P\) を持つ非可換体 \(\mathfrak R\) の分解体とし、\(\mathfrak Z\) の \(\mathfrak R\) における既約表現 \(\beta\) の次数を \(r\) とする。この表現は \(\mathfrak R_r\) の極大可換部分体である。さらに \(\Gamma\) を \(\mathfrak Z\) の Galois 体として、\(\beta_\Gamma=e_1\Gamma+\cdots+e_n\Gamma\) と書く。

\(\Gamma\) へ拡大すると、\(\mathfrak R_{r\Gamma}\) は \(\mathfrak R_{r\Gamma}=\mathfrak l_1+\cdots+\mathfrak l_n\)、\(\mathfrak l_i=\mathfrak R_{r\Gamma}e_i\) と分解する。これらは単純左イデアルであり、\(\mathfrak Z\) が分解体なので \(\mathfrak R_{r\Gamma}\) は \(\Gamma\) 上次数 \(rt=n\) の行列環になる。

Galois 群の置換 \(S\) は \(\mathfrak R_r\) の元を固定するように \(\mathfrak R_{r\Gamma}\) へ作用させる。すると各 \(\mathfrak l_i\) は共役になり、\(S(\mathfrak l_j)=\mathfrak l_i\) となる。

Simplified Chinese title: 分裂域、Galois 域与单左理想分解

§23 正式引入因子系。下文先假定基域 \(P\) 是完美域；也可采用较一般的假定，即只考虑中心为 \(P\) 的非交换除环 \(\mathfrak R\)，并要求每个 \(\mathfrak R_r\) 都含有在 \(P\) 上第一类的极大交换子域。

令 \(\mathfrak Z\) 为中心为 \(P\) 的非交换除环 \(\mathfrak R\) 的分裂域，\(\mathfrak Z\) 在 \(\mathfrak R\) 中的不可约表示 \(\beta\) 的次数为 \(r\)。这个表示是 \(\mathfrak R_r\) 的极大交换子域。再令 \(\Gamma\) 为 \(\mathfrak Z\) 的 Galois 域，写作 \(\beta_\Gamma=e_1\Gamma+\cdots+e_n\Gamma\)。

扩张到 \(\Gamma\) 后，\(\mathfrak R_{r\Gamma}\) 分解为 \(\mathfrak R_{r\Gamma}=\mathfrak l_1+\cdots+\mathfrak l_n\)，其中 \(\mathfrak l_i=\mathfrak R_{r\Gamma}e_i\)。这些都是单左理想；因为 \(\mathfrak Z\) 是分裂域，\(\mathfrak R_{r\Gamma}\) 是 \(\Gamma\) 上次数 \(rt=n\) 的矩阵环。

Galois 群的代换 \(S\) 作用在 \(\mathfrak R_{r\Gamma}\) 上时固定 \(\mathfrak R_r\) 的元素。于是各 \(\mathfrak l_i\) 彼此共轭，并有 \(S(\mathfrak l_j)=\mathfrak l_i\)。

Script/codepoint and TeX/PDF notes:

- Vollkommener Körper is 完全体 / 完美域.
- Preserve \(\beta_\Gamma=e_1\Gamma+\cdots+e_n\Gamma\), \(\mathfrak R_{r\Gamma}=\mathfrak l_1+\cdots+\mathfrak l_n\), \(rt=n\), and \(S(\mathfrak l_j)=\mathfrak l_i\).
- Lines 22365-22371 contain OCR issues (`nist`, `Züber`, `Omega_tau`, and likely wrong group-letter substitutions); draft follows the stable decomposition structure and flags source quality.

Unresolved flags:

- Galoisscher Körper terminology needs domain review; draft uses Galois 体 / Galois 域.
- OCR at lines 22365-22371 needs source-image review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-26-002-composita-matrix-units-and-operator-isomorphisms

Anchor: German baseline lines `22382-22396`; §23 composita, matrix units, and the p_ik operators.

Source summary: Uses representation modules e_i Gamma to map Z to subfields Z_i of Gamma, takes composita {Z_i,Z_k}, splits two left ideals, introduces matrix units c_{lambda rho}^{(ik)}, and describes all operator isomorphisms by elements p_{ik}=c_{ik}^{(ik)} gamma_{ik}.

Japanese title: 合成体、行列単位、作用素同型

表現加群 \(e_i\Gamma\) により、\(\mathfrak Z\) は \(\Gamma\) の部分体 \(\mathsf Z_i\) へ写される。二つの部分体 \(\mathsf Z_i,\mathsf Z_k\) の合成体を \(\{\mathsf Z_i,\mathsf Z_k\}\) と書く。

\(\mathfrak R_{r\{\mathsf Z_i,\mathsf Z_k\}}\) は、対応する二つの左イデアル \(\bar{\mathfrak I}_i\) と \(\bar{\mathfrak I}_k\) を切り離す。これらは単純であり、\(\{\mathsf Z_i,\mathsf Z_k\}\) 上の行列単位 \(c_{\lambda\rho}^{(ik)}\) によって記述される。

\(\bar{\mathfrak I}_i\) から \(\bar{\mathfrak I}_k\) への、\(\mathfrak R_{r\{\mathsf Z_i,\mathsf Z_k\}}\) を作用素領域とする任意の同型は、\(e_i\mapsto p_{ik}\) で特徴づけられる。従って \(a_i=a_ie_i\) は \(a_ip_{ik}\) へ写り、可能な \(p_{ik}\) は \(p_{ik}=c_{ik}^{(ik)}\gamma_{ik}\)、\(\gamma_{ik}\ne0\) と書ける。

Simplified Chinese title: 复合域、矩阵单位与算子同构

由表示模 \(e_i\Gamma\)，\(\mathfrak Z\) 被映到 \(\Gamma\) 的子域 \(\mathsf Z_i\)。两个子域 \(\mathsf Z_i,\mathsf Z_k\) 的复合域记为 \(\{\mathsf Z_i,\mathsf Z_k\}\)。

\(\mathfrak R_{r\{\mathsf Z_i,\mathsf Z_k\}}\) 分离出相应的两个左理想 \(\bar{\mathfrak I}_i\) 与 \(\bar{\mathfrak I}_k\)。它们是单的，并由 \(\{\mathsf Z_i,\mathsf Z_k\}\) 上的矩阵单位 \(c_{\lambda\rho}^{(ik)}\) 描述。

从 \(\bar{\mathfrak I}_i\) 到 \(\bar{\mathfrak I}_k\) 的、以 \(\mathfrak R_{r\{\mathsf Z_i,\mathsf Z_k\}}\) 为算子域的任一同构，都由 \(e_i\mapsto p_{ik}\) 刻画。于是 \(a_i=a_ie_i\) 被送到 \(a_ip_{ik}\)，所有可能的 \(p_{ik}\) 都可写成 \(p_{ik}=c_{ik}^{(ik)}\gamma_{ik}\)，其中 \(\gamma_{ik}\ne0\)。

Script/codepoint and TeX/PDF notes:

- Kompositum is 合成体 / 复合域.
- Preserve \(\{\mathsf Z_i,\mathsf Z_k\}\), \(c_{\lambda\rho}^{(ik)}\), and \(p_{ik}=c_{ik}^{(ik)}\gamma_{ik}\).
- Lines 22384 and 22386 contain OCR/index damage in barred-ideal formulas; target prose keeps only the stable construction.

Unresolved flags:

- Exact barred-ideal formulas need source-image review.
- Operator-isomorphism wording needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-26-003-conjugacy-normalization-of-pseudomatrix-units

Anchor: German baseline lines `22398-22426`; §23 conjugacy condition for choosing p_ik.

Source summary: Defines the Galois action on indices by S(i)=k when S(Z_i)=Z_k, chooses representatives of conjugate index-pair classes, sets p_{1k}=c_{1k}^{(1k)} gamma_{1k}, and defines p_{nu mu}=S(p_{1k}) for conjugate pairs.

Japanese title: 共役条件による擬行列単位の選択

ここで、Galois 群の元 \(S\) が添字へ作用する仕方を、\(S(\mathsf Z_i)=\mathsf Z_k\) のとき \(S(i)=k\) と定める。

任意の添字対 \((\nu,\mu)\) について、それと共役な形 \(S(\nu,\mu)=(1,k)\) の対が少なくとも一つ存在する。各共役類から固定した対 \((1,k)\) を一つ選び、まず \(p_{1k}=c_{1k}^{(1k)}\gamma_{1k}\) と定める。

その後、\(S(1,k)=(\nu,\mu)\) なら \(p_{\nu\mu}=S(p_{1k})\) と置く。この \(p_{\nu\mu}\) は、対応する行列単位と非零係数の積という同じ形を保ち、\(\bar{\mathfrak l}_\nu\) から \(\bar{\mathfrak l}_\mu\) への同型 \(a_\nu\mapsto a_\nu p_{\nu\mu}\) を与える。

Simplified Chinese title: 用共轭条件选择伪矩阵单位

定义 Galois 群元素 \(S\) 在指标上的作用：若 \(S(\mathsf Z_i)=\mathsf Z_k\)，则令 \(S(i)=k\)。

对任一指标对 \((\nu,\mu)\)，至少存在一个与它共轭、且形如 \(S(\nu,\mu)=(1,k)\) 的指标对。每个共轭类中选定一个固定的 \((1,k)\)，先设 \(p_{1k}=c_{1k}^{(1k)}\gamma_{1k}\)。

随后，若 \(S(1,k)=(\nu,\mu)\)，就定义 \(p_{\nu\mu}=S(p_{1k})\)。这个 \(p_{\nu\mu}\) 保持为相应矩阵单位乘以非零系数的形式，并给出从 \(\bar{\mathfrak l}_\nu\) 到 \(\bar{\mathfrak l}_\mu\) 的同构 \(a_\nu\mapsto a_\nu p_{\nu\mu}\)。

Script/codepoint and TeX/PDF notes:

- Pseudomatrix units are drafted as 擬行列単位 / 伪矩阵单位.
- Preserve \(S(i)=k\), \(p_{1k}=c_{1k}^{(1k)}\gamma_{1k}\), and \(p_{\nu\mu}=S(p_{1k})\).
- Line 22416 writes \(\{\mathsf Z_\nu,\mathsf Z_\nu\}\), likely for \(\{\mathsf Z_\nu,\mathsf Z_\mu\}\); draft flags this instead of silently correcting the source.

Unresolved flags:

- Line 22416 compositum index likely has OCR/index error and needs source-image review.
- Pseudo-matrix-unit terminology needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-26-004-factor-system-alpha-from-pseudomatrix-unit-products

Anchor: German baseline lines `22428-22445`; §23 product relations and factor system alpha.

Source summary: Writes p_{nu mu} in terms of global matrix units, transfers matrix-unit multiplication relations to pseudomatrix-unit relations, and defines the n^3 quantities alpha as the factor system attached to R over Z and the chosen p_ik.

Japanese title: 擬行列単位の積から得られる因子系 \(\alpha\)

\(\mathfrak R_{r\Gamma}\) の行列単位系を \(c_{\lambda\varrho}\) とすれば、各 \(p_{\nu\mu}\) は \(p_{\nu\mu}=c_{\nu\mu}\bar\gamma_{\nu\mu}\) の形でも書ける。

通常の行列単位の関係 \(c_{ij}c_{1k}=0\) および \(c_{ij}c_{jk}=c_{ik}\) から、対応する擬行列単位の積関係が得られる。特に \(p_{ij}p_{jk}\) は、\(\Gamma\) の元 \(\alpha_{ik}^{(j)}\) を係数として \(\alpha_{ik}^{(j)}p_{ik}\) になる。

この \(n^3\) 個の量 \(\alpha\) が、\(\mathsf Z\) を基礎に置き、選ばれた擬行列単位系 \(p_{ik}\) に属する、\(\mathfrak R\) の因子系である。さらに、添字三つ組が \(S(i,k,j)=(\nu,\mu,\tau)\) に移るなら、対応する \(\alpha\) も \(S\) によって共役に移される。

Simplified Chinese title: 由伪矩阵单位乘积得到因子系 \(\alpha\)

若把 \(\mathfrak R_{r\Gamma}\) 的矩阵单位系记为 \(c_{\lambda\varrho}\)，则每个 \(p_{\nu\mu}\) 也可写成 \(p_{\nu\mu}=c_{\nu\mu}\bar\gamma_{\nu\mu}\)。

普通矩阵单位的关系 \(c_{ij}c_{1k}=0\) 与 \(c_{ij}c_{jk}=c_{ik}\)，转化为相应伪矩阵单位的乘法关系。特别地，\(p_{ij}p_{jk}\) 等于某个 \(\Gamma\) 中元素 \(\alpha_{ik}^{(j)}\) 乘以 \(p_{ik}\)。

这些 \(n^3\) 个量 \(\alpha\)，就是以 \(\mathsf Z\) 为基础、相对于所选伪矩阵单位系 \(p_{ik}\) 的 \(\mathfrak R\) 的因子系。并且，若三重指标由 \(S(i,k,j)=(\nu,\mu,\tau)\) 变换而来，相应的 \(\alpha\) 也在 \(S\) 作用下共轭变换。

Script/codepoint and TeX/PDF notes:

- Preserve \(p_{\nu\mu}=c_{\nu\mu}\bar\gamma_{\nu\mu}\), \(p_{ij}p_{jk}=\alpha_{ik}^{(j)}p_{ik}\), and \(S(\alpha_{ik}^{(j)})\).
- Line 22439 has collapsed relation formatting (`j + 1` likely for `j != 1`); draft summarizes the intended product relations and flags the source.
- Faktorensystem is 因子系 / 因子系; no canonical approval is implied.

Unresolved flags:

- Lines 22434-22445 need source-image review for exact zero-product and superscript indices.
- Factor-system term needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-26-005-associated-factor-systems-from-delta-rescaling

Anchor: German baseline lines `22448-22467`; §23 associated factor systems.

Source summary: Shows that any other pseudomatrix-unit system arises by rescaling initial p_{1k} by nonzero delta factors and extending by Galois conjugacy. The corresponding alpha* differs from alpha by a coboundary-like delta formula; such factor systems are called associated, forming a class {alpha}.

Japanese title: \(\delta\) による取り替えと同伴因子系

別の擬行列単位系 \(p_{ik}^*\) は、出発点となる \(p_{1k}\) に、合成体から取った任意の非零元 \(\delta_{1k}\) を掛けることで得られる。すなわち \(p_{1k}^*=p_{1k}\delta_{1k}\) とし、ほかの添字対には \(p_{\nu\mu}^*=S(p_{1k}^*)\) として共役に拡張する。

したがって一般に \(p_{\nu\mu}^*=p_{\nu\mu}\delta_{\nu\mu}\) であり、\(\delta_{\nu\mu}\) たちも Galois 共役条件を満たす。これに対応する因子系を \(\alpha^*\) とすると、\(\alpha^*\) は \(\delta\) の積と商によって \(\alpha\) から得られる。

このような \(\alpha^*\) と \(\alpha\) を同伴な因子系と呼び、同様に \(p_{ik}^*\) と \(p_{ik}\) も同伴と呼ばれる。固定した \(\mathsf Z\) を基礎にして得られる \(\mathfrak R\) のすべての因子系は、同伴因子系の一つの類 \(\{\alpha\}\) をなす。

Simplified Chinese title: 用 \(\delta\) 重新标定与同伴因子系

另一组伪矩阵单位 \(p_{ik}^*\) 可由原来的初始 \(p_{1k}\) 乘上取自复合域的任意非零元 \(\delta_{1k}\) 得到。也就是说，先令 \(p_{1k}^*=p_{1k}\delta_{1k}\)，再对其他指标对按 \(p_{\nu\mu}^*=S(p_{1k}^*)\) 共轭延拓。

于是一般有 \(p_{\nu\mu}^*=p_{\nu\mu}\delta_{\nu\mu}\)，而这些 \(\delta_{\nu\mu}\) 也满足 Galois 共轭条件。若相应因子系为 \(\alpha^*\)，则 \(\alpha^*\) 由 \(\alpha\) 乘以一个由 \(\delta\) 的乘积与商构成的因子得到。

这样的 \(\alpha^*\) 与 \(\alpha\) 称为同伴因子系；同样，\(p_{ik}^*\) 与 \(p_{ik}\) 也称为同伴。以固定的 \(\mathsf Z\) 为基础得到的 \(\mathfrak R\) 的所有因子系，组成一个同伴因子系类 \(\{\alpha\}\)。

Script/codepoint and TeX/PDF notes:

- Preserve \(p_{1k}^*=p_{1k}\delta_{1k}\), \(p_{\nu\mu}^*=p_{\nu\mu}\delta_{\nu\mu}\), and \(\{\alpha\}\).
- Line 22464 prints \(\alpha_{ik}^{(i)*}\) while the context suggests a \(j\)-indexed formula; draft flags this and does not silently correct the formula.
- Assoziiert is drafted as 同伴 / 同伴, provisional.

Unresolved flags:

- The delta transformation formula at line 22464 needs source-image review.
- Associated-factor-system terminology needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-26-006-representation-independence-and-section-24-transition

Anchor: German baseline lines `22469-22473`; §23 representation independence and transition to §24.

Source summary: States that the associated class {alpha} is independent of the chosen representation beta of Z in R_r, since a change of representation by conjugation with a G-invariant element leaves the factor system identical. A factor system is a multiplication table adapted to R; §24 on multiplication of factor systems begins next.

Japanese title: 表現からの独立性と §24 への移行

同伴因子系の類 \(\{\alpha\}\) は、その定義に用いた \(\mathfrak Z\) の表現 \(\beta\) の選び方に依存しない。別の表現 \(\beta'\) へ移るには、\(G\)-不変な元 \(\lambda\in\mathfrak R_r\) による変換を用いればよい。

\(\beta\) に属する \(p_{ik}\) から \(\lambda^{-1}p_{ik}\lambda\) を作ると、これは \(\beta'\) に属する擬行列単位系であり、対応する因子系は同一である。

したがって因子系とは、\(\mathfrak R_{n\Gamma}\) の乗法表にほかならないが、\(\mathfrak R\) の特別な代数的性質に合わせて作られた乗法表である。次の §24 は、この因子系の乗法を扱う。

Simplified Chinese title: 与表示选择无关及转入 §24

同伴因子系的类 \(\{\alpha\}\) 不依赖于定义时所选的 \(\mathfrak Z\) 在 \(\mathfrak R_r\) 中的表示 \(\beta\)。从一个表示 \(\beta\) 过渡到另一个表示 \(\beta'\)，可以通过一个 \(G\)-不变元素 \(\lambda\in\mathfrak R_r\) 的变换实现。

由属于 \(\beta\) 的 \(p_{ik}\) 构造 \(\lambda^{-1}p_{ik}\lambda\)，便得到属于 \(\beta'\) 的伪矩阵单位系；而二者对应的因子系相同。

因此，因子系不过是 \(\mathfrak R_{n\Gamma}\) 的乘法表，但它是适合 \(\mathfrak R\) 特殊代数性质的乘法表。下一节 §24 将讨论因子系的乘法。

Script/codepoint and TeX/PDF notes:

- Preserve \(\lambda^{-1}p_{ik}\lambda\), \(\{\alpha\}\), and \(\mathfrak R_{n\Gamma}\).
- Line 22469 writes `p_{ik} = lambda^{-1} p_{ik} lambda`; draft distinguishes the transformed system contextually.
- Line 22473 is included only as the §24 transition heading; new §24 content starts at 22475.

Unresolved flags:

- Transformation notation at line 22469 needs source-image review.
- Multiplication-table characterization is draft-only pending domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
