# Noether CJK Draft Corpus Translation Slices: Continuation 23

Generated UTC: `2026-07-04T09:12:31.404049+00:00`

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

- tensor product: no German Tensorprodukt anchor in 22001-22158; no otimes hit in this continuation
- localization: Quotientenring candidates remain 16223-16225, 18467, 20105, 20228, 20240, 20284, 20949, 20953, and 21009, plus Quotientenkörper at 20822; no direct Lokalisierung label in 22001-22158
- Harish-Chandra: no German corpus anchor
- abstract algebra: no direct abstract-algebra anchor in §20 lines 22001-22158
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in this continuation
- group algebra: no new group-algebra evidence; §20 concerns noncommutative fields and splitting fields

## cjk-continuation-23-001-noncommutative-field-extensions-and-center-over-omega

Anchor: German baseline lines `22001-22023`; §20 noncommutative fields and center after algebraic closure.

Source summary: Introduces a noncommutative field R with center P, compares its scalar extension by a commutative field Z with earlier coefficient extension results, and states that over an algebraically closed extension field Omega the center of R_Omega is Omega.

Japanese title: 非可換体の係数拡大と \(\Omega\) 上の中心

§20 では、中心を \(P\) とする非可換体 \(\mathfrak R=y_1P+\cdots+y_mP\) を考え、可換な有限代数拡大体についての理論に類似した定理を展開する。

\(\mathfrak Z\) が \(P\) 上の可換体であれば、\(\mathfrak R\) と \(\mathfrak Z\) の二通りの拡大系は同じものになる。これは \(\mathfrak R\) の元 \(y_i\) と \(\mathfrak Z\) の元 \(\xi_j\) が中心 \(P\) 上で可換に扱われるためであり、したがって §19 の定理を適用できる。

特に、\(\Omega\) を \(P\) の代数閉な拡大体とすると、\(\mathfrak R_{\Omega}\) は両側単純であり、定理 1 はその中心が \(\Omega\) そのものになると述べる。証明は §19 の中心に関する定理へ帰着し、中心元の係数が生成する有限拡大体 \(\mathfrak Z\) を経由して \(\Omega\) に戻す。

Simplified Chinese title: 非交换除环的系数扩张与 \(\Omega\) 上的中心

§20 考察以 \(P\) 为中心的非交换除环 \(\mathfrak R=y_1P+\cdots+y_mP\)，并发展一组与交换有限代数扩域理论相类似的定理。

若 \(\mathfrak Z\) 是 \(P\) 上的交换域，则 \(\mathfrak R\) 与 \(\mathfrak Z\) 的两种扩张系统相同。这是因为 \(\mathfrak R\) 的元素 \(y_i\) 与 \(\mathfrak Z\) 的元素 \(\xi_j\) 在中心 \(P\) 上可交换，于是可以应用 §19 的定理。

特别地，若 \(\Omega\) 是 \(P\) 的代数闭扩域，则 \(\mathfrak R_{\Omega}\) 是双侧单的；定理 1 断言它的中心正是 \(\Omega\)。证明把中心元素的系数生成的有限扩域 \(\mathfrak Z\) 引入，再用 §19 关于中心的定理把该元素逼回 \(\Omega\)。

Script/codepoint and TeX/PDF notes:

- Preserve \(\mathfrak R=y_1P+\cdots+y_mP\), \(\mathfrak R_{\Omega}\), and \(\Omega\).
- German OCR at 22009-22023 substitutes several symbols (`€`, `&`, `2`, `Q`); target prose follows the stable mathematical context and flags source quality.
- Nichtkommutativer Körper remains 非可換体 / 非交换除环 in this lane.

Unresolved flags:

- OCR substitutions in the formulas for the two extended systems need source-image review.
- Choice between Chinese 非交换域 and 非交换除环 needs reviewer/domain decision.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-23-002-matrix-ring-over-omega-square-degree-and-component-number

Anchor: German baseline lines `22025-22039`; §20 two-sided simplicity, matrix ring over Omega, absolute component number.

Source summary: Proves R_Omega is two-sided simple, then concludes it is a matrix ring over Omega. Hence the degree of R over its center P is a square, and the number of right/left ideals in the Omega-decomposition is called the absolute component number.

Japanese title: \(\Omega\) 上の行列環、平方次数、絶対成分数

同じ方法で、定理 2 は \(\mathfrak R_{\Omega}\) が両側単純であることを示す。両側イデアルを有限個の係数で書き、それらの係数が生成する有限拡大体 \(\mathfrak Z\) へ下げれば、\(\mathfrak R_{\mathfrak Z}\) の両側単純性から、イデアルは \(0\) か全体に限られる。

この結果により、\(\mathfrak R_{\Omega}\) は中心 \(\Omega\) 上の行列環である。したがって \(\mathfrak R\) の中心 \(P\) 上の次数 \(m\) は平方数 \(m=t^2\) になる。

\(\mathfrak R_{\Omega}\) が分解する右イデアル、同じく左イデアルの個数 \(t\) を、\(\mathfrak R\) の絶対成分数と呼ぶ。

Simplified Chinese title: \(\Omega\) 上的矩阵环、平方次数与绝对分量数

用相同方法，定理 2 证明 \(\mathfrak R_{\Omega}\) 是双侧单的。把一个双侧理想用有限个系数写出，再降到这些系数生成的有限扩域 \(\mathfrak Z\)，由 \(\mathfrak R_{\mathfrak Z}\) 的双侧单性可知该理想只能是 \(0\) 或全体。

于是 \(\mathfrak R_{\Omega}\) 是以中心 \(\Omega\) 为基域的矩阵环。因此 \(\mathfrak R\) 在其中心 \(P\) 上的次数 \(m\) 是平方数 \(m=t^2\)。

\(\mathfrak R_{\Omega}\) 分解出的右理想个数，等同于左理想个数 \(t\)，被称为 \(\mathfrak R\) 的绝对分量数。

Script/codepoint and TeX/PDF notes:

- Preserve \(\mathfrak R_{\Omega}=\sum \Omega c_{ik}\) and \(m=t^2\).
- Absolute Komponentenzahl is drafted as 絶対成分数 / 绝对分量数 pending domain review.
- OCR at 22027-22039 repeatedly prints malformed \\mathfrak R/\\Omega symbols; draft uses the section context.

Unresolved flags:

- Absolute component-number term needs native/domain review.
- Matrix-ring formula needs source-image verification before canonical use.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-23-003-splitting-fields-and-automorphism-field-of-right-ideals

Anchor: German baseline lines `22041-22073`; §20 splitting fields and automorphism fields of right ideals.

Source summary: Defines a finite algebraic extension field Z of P as a splitting field of R when R_Z already splits into the absolute number of simple right ideals, then proves the equivalence with Z being the automorphism field of those right ideals.

Japanese title: 分解体と右イデアルの自己同型体

つぎに分解体を調べる。有限代数拡大体 \(\mathfrak Z/P\) について、\(\mathfrak R_{\mathfrak Z}\) がすでに絶対成分数 \(t\) と同じ個数の単純右イデアルへ分解するなら、\(\mathfrak Z\) を \(\mathfrak R\) の分解体と呼ぶ。

定理 4 は、\(\mathfrak Z\) が分解体であることと、\(\mathfrak R_{\mathfrak Z}\) の右イデアルの自己同型体が \(\mathfrak Z\) 自身であることが同値だと述べる。

証明では、分解体なら \(\mathfrak R_{\mathfrak Z}=\sum \mathfrak T c_{ik}\) と書き、さらに \(\Omega\) へ拡大してランクを比べる。ランクが \(t^2\) に等しいため \(\mathfrak T_{\Omega}\) のランクは \(1\) であり、\(\mathfrak T=\mathfrak Z\) が従う。逆方向も同じ行列単位 \(c_{ik}\) の数を数えることで分解体性を得る。

Simplified Chinese title: 分裂域与右理想的自同构域

接下来研究分裂域。对有限代数扩域 \(\mathfrak Z/P\)，若 \(\mathfrak R_{\mathfrak Z}\) 已经分解为绝对分量数 \(t\) 个单右理想，则称 \(\mathfrak Z\) 为 \(\mathfrak R\) 的分裂域。

定理 4 说，\(\mathfrak Z\) 是分裂域，当且仅当 \(\mathfrak R_{\mathfrak Z}\) 的右理想的自同构域等于 \(\mathfrak Z\) 本身。

证明中，若 \(\mathfrak Z\) 是分裂域，则可写 \(\mathfrak R_{\mathfrak Z}=\sum \mathfrak T c_{ik}\)，再扩张到 \(\Omega\) 后比较秩。由于总秩为 \(t^2\)，\(\mathfrak T_{\Omega}\) 的秩为 \(1\)，故 \(\mathfrak T=\mathfrak Z\)。反方向则通过同一组矩阵单位 \(c_{ik}\) 的个数得到分裂域条件。

Script/codepoint and TeX/PDF notes:

- Zerfällungskörper is 分解体 / 分裂域, matching earlier CJK sidecars.
- Preserve \(\mathfrak R_{\mathfrak Z}=\sum \mathfrak T c_{ik}\), \(\mathfrak R_{\Omega}=\sum \mathfrak T_{\Omega}c_{ik}\), and \(t^2\).
- The footnote at line 22047 is noted but not expanded; it references the earlier splitting-field notion.

Unresolved flags:

- Automorphismenkörper of ideals is drafted as 自己同型体 / 自同构域 pending domain review.
- OCR forms \\mathfrak A_7 and \\Re_7 need source-image verification.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-23-004-maximal-commutative-subfields-and-splitting-field-converse

Anchor: German baseline lines `22075-22104`; §20 irreducible representations and maximal commutative subfields.

Source summary: States that the irreducible representation of a splitting field Z in R is a maximal commutative subfield of a matrix ring R_r, and conversely that such a maximal commutative subfield condition makes Z a splitting field.

Japanese title: 極大可換部分体としての分解体表現

定理 5 は、\(\mathfrak R\) の分解体 \(\mathfrak Z\) を \(\mathfrak R\) の中で既約表現したものは、行列環 \(\mathfrak R_r\) の極大可換部分体になる、と述べる。ここで \(r\) は \(\mathfrak Z\) の既約表現の次数である。

分解体 \(\mathfrak Z\) の \(P\) 上の次数を \(n\)、絶対成分数を \(t\) とすると、既約表現の次数は \(r=n/t\) である。もし \(\mathfrak Z\subseteq\mathfrak Z^*\subseteq\mathfrak R_r\) というより大きな可換体があれば、その次数 \(n^*\) と既約表現次数 \(r^*\) について \(n\le n^*=r^*t\le rt=n\) となり、結局 \(n^*=n\) である。

逆に、可換拡大体 \(\mathfrak Z\) の既約表現が \(\mathfrak R_r\) の極大可換部分体なら、\(\mathfrak R_{\mathfrak Z}\) の単純イデアルの自己同型体 \(\mathfrak T\) は \(\mathfrak Z\) を含む。もし \(\mathfrak T\ne\mathfrak Z\) なら、\(\mathfrak R_r\) 内で \(\mathfrak Z\) の真の可換拡大体が得られ、極大性に反する。したがって \(\mathfrak Z\) は分解体である。

Simplified Chinese title: 作为极大交换子域的分裂域表示

定理 5 说，\(\mathfrak R\) 的分裂域 \(\mathfrak Z\) 在 \(\mathfrak R\) 中的不可约表示，是矩阵环 \(\mathfrak R_r\) 的极大交换子域；这里 \(r\) 是 \(\mathfrak Z\) 的不可约表示次数。

若 \(\mathfrak Z\) 在 \(P\) 上的次数为 \(n\)，绝对分量数为 \(t\)，则不可约表示次数为 \(r=n/t\)。若存在更大的交换域 \(\mathfrak Z\subseteq\mathfrak Z^*\subseteq\mathfrak R_r\)，其次数 \(n^*\) 与不可约表示次数 \(r^*\) 满足 \(n\le n^*=r^*t\le rt=n\)，于是 \(n^*=n\)。

反过来，若交换扩域 \(\mathfrak Z\) 的不可约表示是 \(\mathfrak R_r\) 的极大交换子域，则 \(\mathfrak R_{\mathfrak Z}\) 中单理想的自同构域 \(\mathfrak T\) 包含 \(\mathfrak Z\)。若 \(\mathfrak T\ne\mathfrak Z\)，就在 \(\mathfrak R_r\) 内得到 \(\mathfrak Z\) 的真交换扩域，违背极大性。因此 \(\mathfrak Z\) 是分裂域。

Script/codepoint and TeX/PDF notes:

- Maximaler kommutativer Teilkörper is 極大可換部分体 / 极大交换子域.
- Preserve \(n\le n^*=r^*t\le rt=n\), \(\mathfrak Z\subseteq\mathfrak Z^*\subseteq\mathfrak R_r\), and \(\mathfrak T=\mathfrak Z\).
- Line 22077 splits `Zerfällungskörper` across lines; draft rejoins it as splitting field.

Unresolved flags:

- Representation-degree notation and maximal-commutative-subfield wording need native/domain review.
- OCR in 22075-22104 requires source-image check before canonical use.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-23-005-maximal-commutative-subfields-skolem-noether-and-galois-group

Anchor: German baseline lines `22106-22124`; §20 maximal commutative subfields and inner automorphism theorem.

Source summary: Derives that maximal commutative subfields have degree t over P and are splitting fields, then states a Skolem-Noether-type theorem: any P-fixing isomorphism between two-sided simple subrings of a matrix ring is implemented by conjugation, yielding the Galois group as inner automorphisms.

Japanese title: 極大可換部分体、共役実現、Galois 群

定理 5 から、定理 6 として、\(\mathfrak R\) の極大可換部分体は \(P\) 上次数 \(t\) を持ち、しかも分解体であることが直ちに従う。

つづいて定理 7 は、行列環の中の、\(P\) を含む二つの両側単純部分環の間に \(P\) を点ごとに固定する同型があるなら、その同型は正則元 \(\tau\) による変換で実現される、と述べる。対応する元 \(\sigma_1,\sigma_2\) について、\(\tau^{-1}\sigma_1\tau=\sigma_2\) である。

この定理から定理 8 が得られる。すなわち、中心 \(P\) に関して \(\mathfrak R\) の \(P\) を点ごとに固定する自己同型群、つまり Galois 群は、\(\mathfrak R\) の内的自己同型群である。

Simplified Chinese title: 极大交换子域、共轭实现与 Galois 群

由定理 5 立刻得到定理 6：\(\mathfrak R\) 的极大交换子域在 \(P\) 上的次数为 \(t\)，并且都是分裂域。

随后定理 7 说，若矩阵环中两个包含 \(P\) 的双侧单子环之间有一个逐点固定 \(P\) 的同构，则这个同构由某个正则元 \(\tau\) 的共轭变换实现。对应元素 \(\sigma_1,\sigma_2\) 满足 \(\tau^{-1}\sigma_1\tau=\sigma_2\)。

由此推出定理 8：关于中心 \(P\)，\(\mathfrak R\) 的逐点固定 \(P\) 的自同构群，也就是它的 Galois 群，正是 \(\mathfrak R\) 的内自同构群。

Script/codepoint and TeX/PDF notes:

- Preserve \(\tau^{-1}\sigma_1\tau=\sigma_2\).
- Satz 7 is Skolem-Noether-like but the output does not label it canonically unless the source does so.
- Galoissche Gruppe is Galois 群 in both JP and zh-Hans draft text.

Unresolved flags:

- Whether to add an explicit Skolem-Noether glossary bridge requires reviewer decision.
- OCR substitutions for ring letters in lines 22110-22124 need source-image review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-23-006-real-center-quaternion-division-ring

Anchor: German baseline lines `22128-22153`; §20 noncommutative fields over the real numbers and quaternions.

Source summary: Proves that the only finite-degree noncommutative field with center the real numbers is the quaternion division ring, by using maximal commutative subfields isomorphic to the complex numbers and a conjugating element.

Japanese title: 実数を中心とする場合と四元数体

定理 9 は、中心が実数体 \(\mathbb R\) で有限次元の非可換体は、四元数体だけであると述べる。

\(\mathfrak R\) の中心を \(\mathbb R\) とすると、定理 6 により \(\mathfrak R\) の次数は極大可換部分体の次数の平方である。極大可換部分体は複素数体に同型な体しかありえないので、その次数は \(2\)、従って \(\mathfrak R\) は \(\mathbb R\) 上次数 \(4\) を持つ。

極大可換部分体を \(\mathbb R(i)\) とし、同型を共役で実現する定理 7 を用いて元 \(j^*\) を取る。すると \(\mathfrak R=\mathbb R+\mathbb Ri+\mathbb Rj^*+\mathbb Rij^*\) と書ける。さらに \(j^{*2}\) は中心に属し、正にはなりえないため、正規化して \(j^2=-1\) とでき、標準的な四元数単位が得られる。

Simplified Chinese title: 以实数为中心的情形与四元数除环

定理 9 断言：中心为实数域 \(\mathbb R\)、且在中心上有限维的非交换除环，只有四元数除环。

设 \(\mathfrak R\) 的中心为 \(\mathbb R\)。由定理 6，\(\mathfrak R\) 的次数是极大交换子域次数的平方。极大交换子域只能是与复数域同构的域，所以该次数为 \(2\)，从而 \(\mathfrak R\) 在 \(\mathbb R\) 上的次数为 \(4\)。

取极大交换子域为 \(\mathbb R(i)\)，再用定理 7 把相关同构实现为共轭，从而得到元素 \(j^*\)。于是 \(\mathfrak R=\mathbb R+\mathbb Ri+\mathbb Rj^*+\mathbb Rij^*\)。并且 \(j^{*2}\) 属于中心且不可能为正；经归一化可取 \(j^2=-1\)，得到标准四元数单位。

Script/codepoint and TeX/PDF notes:

- Quaternionenkörper is 四元数体 / 四元数除环.
- Preserve \(\mathfrak R=\mathbb R+\mathbb Ri+\mathbb Rj^*+\mathbb Rij^*\) and \(j^2=-1\).
- Lines 22130-22151 are heavily OCR-damaged (`i?`, `---`, `7*`, malformed signs); draft follows the quaternion proof structure and flags source-image review.

Unresolved flags:

- Conjugation equation at 22134-22136 appears OCR-corrupted and needs source-image review.
- Japanese 四元数体 versus 四元数除環 and zh-Hans 四元数体 versus 四元数除环 need reviewer choice.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-23-007-wedderburn-finite-division-ring-theorem

Anchor: German baseline lines `22155-22158`; §20 Wedderburn theorem for finite fields/division rings.

Source summary: States Wedderburn's theorem that every finite division ring is commutative and sketches the proof by maximal commutative subfields, finite-field isomorphisms, conjugacy, and the impossibility of covering the multiplicative group by conjugate proper subgroups sharing the identity.

Japanese title: Wedderburn の有限体定理

§20 の最後に、定理 10 として Wedderburn の定理が置かれる。有限個の元からなる体はすべて可換である。

証明では、有限体 \(\mathfrak R\) の中心を \(P\)、\(P\) 上の次数を \(t^2\) とする。極大可換部分体はすべて \(P\) 上次数 \(t\) で、従って同じ個数の元を持つ。Galois 体の理論によりそれらは同型であり、定理 7 によって互いに変換で移り合う。

\(\mathfrak R\) は、その極大可換部分体全体の合併である。零を除いた乗法群を見ると、ある部分群の共役部分群の合併で全体が覆われることになる。しかし \(t>1\) なら、これらの共役部分群は少なくとも単位元を共有するため、群全体をそのように尽くすことはできない。従って \(t=1\)、つまり \(\mathfrak R\) は可換である。

Simplified Chinese title: Wedderburn 有限除环定理

§20 末尾给出定理 10，即 Wedderburn 定理：由有限多个元素组成的除环必为交换的。

证明设有限除环 \(\mathfrak R\) 的中心为 \(P\)，在 \(P\) 上的次数为 \(t^2\)。所有极大交换子域在 \(P\) 上的次数都是 \(t\)，因而元素个数相同。由 Galois 域理论，这些子域同构；再由定理 7，它们可由变换互相得到。

\(\mathfrak R\) 是其所有极大交换子域的并。去掉零后看乘法群，就得到整个群是某个子群的共轭子群的并。但若 \(t>1\)，这些共轭子群至少共同含有单位元，无法以这种方式覆盖整个群而互不相交。故 \(t=1\)，\(\mathfrak R\) 是交换的。

Script/codepoint and TeX/PDF notes:

- Satz von Wedderburn is Wedderburn の定理 / Wedderburn 定理.
- The German heading says Körper from finitely many elements; target notes clarify finite division ring because the chapter is noncommutative.
- No tensor/localization evidence appears in lines 22001-22158.

Unresolved flags:

- Finite-field terminology should be checked by a native/domain reviewer.
- The group-covering argument is compressed in the source and remains draft prose.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
