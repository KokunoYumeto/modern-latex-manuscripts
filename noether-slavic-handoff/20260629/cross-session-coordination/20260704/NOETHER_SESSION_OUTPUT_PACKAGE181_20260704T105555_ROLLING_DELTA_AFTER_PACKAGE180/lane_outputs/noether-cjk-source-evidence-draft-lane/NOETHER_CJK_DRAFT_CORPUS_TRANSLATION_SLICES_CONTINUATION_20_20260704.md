# Noether CJK Draft Corpus Translation Slices: Continuation 20

Generated UTC: `2026-07-04T08:51:56.296778+00:00`

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

- tensor product: no German Tensorprodukt anchor; line 21524 formula and noisy local otimes vicinity remain non-anchor evidence because no tensor-product term or explanation appears
- localization: Quotientenring candidates remain 16223-16225, 18467, 20105, 20228, 20240, 20284, 20949, 20953, and 21009, plus Quotientenkörper at 20822; no direct Lokalisierung label in 21278-21530
- Harish-Chandra: no German corpus anchor
- abstract algebra: no direct abstract-algebra anchor in Chapter II lines 21278-21530
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in this continuation

## cjk-continuation-20-001-coefficient-extension-hypercomplex-systems

Anchor: German baseline lines `21278-21300`; Kapitel II and §5 coefficient extension of hypercomplex systems.

Source summary: Opens Chapter II on Galois theory of commutative fields and defines coefficient extension for hypercomplex systems over a commutative field by formal sums and module/multiplication rules.

Japanese title: 超複素系の係数拡大

第 II 章は、これまで展開した表現論だけで Galois 理論を基礎づけられる、と述べて始まる。この方法では、特別な生成元系や不定元多項式に関する定理へ戻る必要がない点が利点とされる。

§5 では、可換体 \(P\) 上の超複素系を、\(P\) を中心に含む拡大環 \(\Omega\) へ係数拡大する。形式和 \(\sum c_i\omega_i\) を用い、和、左右からの \(\Omega\)-作用、および \(c_i\) の既存の積を使った乗法を定める。

こうして得られる拡大系は \(\Omega\)-加群として \(\mathfrak{o}_{\Omega}=c_1\Omega+\cdots+c_n\Omega\) と書け、基底の取り方に依存しないとされる。\(\Omega\) が可換体なら、この拡大系も \(\Omega\) 上の超複素系になる。

Simplified Chinese title: 超复系统的系数扩张

第 II 章开头说，前面建立的表示论已经足以奠定 Galois 理论；这种方法的优点是，不必诉诸特殊生成元系和关于不定元多项式的定理。

§5 把交换域 \(P\) 上的超复系统扩张到一个中心含有 \(P\) 的扩张环 \(\Omega\)。用形式和 \(\sum c_i\omega_i\)，并规定加法、左右 \(\Omega\)-作用以及由已有 \(c_i\) 乘法诱导的乘法。

所得扩张系统作为 \(\Omega\)-模可写为 \(\mathfrak{o}_{\Omega}=c_1\Omega+\cdots+c_n\Omega\)，且与所选基无关。若 \(\Omega\) 是交换域，则这个扩张系统也是 \(\Omega\) 上的超复系统。

Script/codepoint and TeX/PDF notes:

- Koeffizientenerweiterung is drafted as 係数拡大 / 系数扩张.
- Preserve \(\mathfrak{o}_{\Omega}=c_1\Omega+\cdots+c_n\Omega\), \(\sum c_i\omega_i\), and \(\Omega\)-module notation.
- Lines 21284-21298 contain OCR substitutions such as 2/Omega and dg/De; the draft follows the mathematical structure and flags the source quality.

Unresolved flags:

- Coefficient-extension wording needs native/domain review.
- OCR substitutions in §5 need source-image verification.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-20-002-irreducible-representations-commutative-systems

Anchor: German baseline lines `21302-21318`; §6 irreducible representations of commutative systems.

Source summary: Reduces representations of a commutative system over P to those of its coefficient extension over an algebraically closed field, then uses the radical quotient and complete reducibility to obtain t one-dimensional representation classes.

Japanese title: 可換系の既約表現

§6 では、可換系 \(\mathfrak Z=z_1P+\cdots+z_nP\) を、代数閉な拡大体 \(\Omega\) 上で表現する問題に移す。もとの表現は係数拡大 \(\mathfrak Z_\Omega=z_1\Omega+\cdots+z_n\Omega\) の表現を与え、逆も成り立つためである。

M.Z. の結果により、\(\mathfrak Z_\Omega\) の表現は正則表現に含まれ、さらにラジカル \(\mathfrak C\) で割った \(\mathfrak Z_\Omega/\mathfrak C\) を表現加群として見れば十分とされる。

この商は完全可約系であり、\(\Omega\) 上有限次数の体の直和になる。 \(\Omega\) が代数閉であるため、各成分は \(\Omega\) と同型で、\(e_1\Omega+\cdots+e_t\Omega\) と書ける。したがって一次の既約表現類がちょうど \(t\) 個ある。

Simplified Chinese title: 交换系统的不可约表示

§6 把交换系统 \(\mathfrak Z=z_1P+\cdots+z_nP\) 的表示问题转到代数闭扩张域 \(\Omega\) 上。原系统的表示给出系数扩张 \(\mathfrak Z_\Omega=z_1\Omega+\cdots+z_n\Omega\) 的表示，反过来也成立。

根据 M.Z. 的结果，\(\mathfrak Z_\Omega\) 的表示包含在正则表示中；进一步，只需把根基商 \(\mathfrak Z_\Omega/\mathfrak C\) 作为表示模来考察。

这个商是完全可约系统，因此是 \(\Omega\) 上有限次数域的直和。由于 \(\Omega\) 代数闭，每个分量都与 \(\Omega\) 同构，故可写成 \(e_1\Omega+\cdots+e_t\Omega\)。于是恰有 \(t\) 个一次不可约表示类。

Script/codepoint and TeX/PDF notes:

- Fully reducible is 完全可約 / 完全可约, kept provisional.
- Preserve \(\mathfrak Z_\Omega/\mathfrak C\), \(e_1\Omega+\cdots+e_t\Omega\), and \(\Theta_1,\ldots,\Theta_t\).
- Direct sum here is 直和, not tensor product evidence.

Unresolved flags:

- Fully reducible/regular representation terminology remains draft.
- No tensor-product blocker closure is inferred from direct-sum language.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-20-003-field-isomorphisms-splitting-field-and-galois-group

Anchor: German baseline lines `21319-21345`; §§7-10 field isomorphisms, splitting field, and Galois group.

Source summary: Describes isomorphic conjugate fields from homomorphisms, first and second kind field extensions, the minimal splitting field as compositum of conjugates, and the Galois group as automorphisms fixing P.

Japanese title: 体の同型・分解体・Galois 群

§7 では \(\mathfrak Z\) を体とする。各準同型 \(\Theta_i\) は、\(\mathfrak Z\) を \(\Omega\) の部分体 \(Z_i\) へ同型に写す。有限 \(n\) 次拡大では、そのような \(Z_i\) の数は \(\mathfrak Z_\Omega\) のラジカル商の階数 \(t\) に等しく、したがって高々 \(n\) である。

\(Z_i\) の数が \(n\) なら第一種、\(n\) より少なければ第二種と呼ぶ。この定式化では、共役体の個数が次数を超えないことが、正則表現に既約表現が含まれることから出るため、通常の Galois 理論のように原始元を使わずに済む。

§8 から §10 では、すべての共役体を含む最小の分解体を、それらの合成体として記述する。Galois 体の場合、対応する同型写像は、基礎体 \(P\) を固定する自己同型全体となり、これが \(P\) に関する Galois 群である。

Simplified Chinese title: 域同构、分裂域与 Galois 群

§7 令 \(\mathfrak Z\) 为域。每个同态 \(\Theta_i\) 都把 \(\mathfrak Z\) 同构地映到 \(\Omega\) 的某个子域 \(Z_i\)。若是 \(n\) 次有限扩张，则这类 \(Z_i\) 的个数等于 \(\mathfrak Z_\Omega\) 根基商的秩 \(t\)，因而至多为 \(n\)。

若 \(Z_i\) 的个数等于 \(n\)，则称为第一类；若少于 \(n\)，则称为第二类。在这种表述中，共轭域数目不超过次数这一事实来自不可约表示包含于正则表示，而不必像通常 Galois 理论那样使用本原元。

§8 至 §10 把包含所有共轭域的最小分裂域描述为这些共轭域的合成域。在 Galois 域情形，相应同构映射就是所有逐点固定基域 \(P\) 的自同构；它们构成关于 \(P\) 的 Galois 群。

Script/codepoint and TeX/PDF notes:

- Zerfällungskörper follows existing lane convention 分解体 / 分裂域.
- Compositum is translated descriptively as 合成体 / 合成域.
- Lines 21333-21341 are OCR-heavy; symbols such as Z;, J'', 37/C, ©; are not silently normalized into canonical formulas.

Unresolved flags:

- First/second-kind terminology needs review.
- Splitting-field passage has heavy OCR damage and needs source-image verification.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-20-004-main-theorem-galois-theory-and-extension-lemma

Anchor: German baseline lines `21347-21382`; §11 main theorem statement and extension lemma.

Source summary: States the fundamental theorem correspondence between intermediate fields and subgroups, then reduces the first direction to an extension lemma for isomorphisms of intermediate fields.

Japanese title: Galois 理論の主定理と拡張補題

§11 は、第一種の Galois 拡大 \(Z/P\) について Galois 理論の主定理を述べる。中間体 \(T\) と Galois 群 \(\mathfrak G\) の部分群 \(\mathfrak H\) が一対一に対応し、\(\mathfrak H\) は \(T\) を点ごとに固定する自己同型全体、\(T\) は \(\mathfrak H\) の全元で固定される \(Z\)-元全体である。

短く言えば、\(T\) の不変群が \(\mathfrak H\) なら \(T\) は \(\mathfrak H\) の不変体であり、逆に \(T\) が \(\mathfrak H\) の不変体なら \(\mathfrak H\) は \(T\) の不変群である。

第一の方向は補題に帰着される。すなわち \(P\subseteq\Sigma\subseteq T\subseteq Z\) で \(T/\Sigma\) の次数が \(t\) なら、\(\Sigma\) から共役体への任意の同型は、\(T\) から共役体への \(t\) 個の相異なる同型へ拡張できる。

Simplified Chinese title: Galois 理论主定理与扩张引理

§11 对第一类 Galois 扩张 \(Z/P\) 陈述 Galois 理论主定理：中间域 \(T\) 与 Galois 群 \(\mathfrak G\) 的子群 \(\mathfrak H\) 一一对应；\(\mathfrak H\) 是所有逐点固定 \(T\) 的自同构，而 \(T\) 是在 \(\mathfrak H\) 全部元素下保持不变的 \(Z\)-元素全体。

简言之，若 \(\mathfrak H\) 是 \(T\) 的不变群，则 \(T\) 是 \(\mathfrak H\) 的不变域；反过来，若 \(T\) 是 \(\mathfrak H\) 的不变域，则 \(\mathfrak H\) 是 \(T\) 的不变群。

第一个方向归结为一个引理：若 \(P\subseteq\Sigma\subseteq T\subseteq Z\)，且 \(T/\Sigma\) 的次数为 \(t\)，则任意从 \(\Sigma\) 到共轭域的同构，都可扩张为从 \(T\) 到共轭域的 \(t\) 个不同同构。

Script/codepoint and TeX/PDF notes:

- Invariant group/field are 不変群/不変体 and 不变群/不变域, draft only.
- Preserve \(P\subseteq\Sigma\subseteq T\subseteq Z\), \(\mathfrak G\), and \(\mathfrak H\).
- No localization evidence occurs in this Galois-theory theorem statement.

Unresolved flags:

- Invariant terminology needs native/domain review.
- The source uses mixed Fraktur/script letters; TeX readability needs reviewer attention.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-20-005-proof-by-idempotent-components-and-invariants

Anchor: German baseline lines `21384-21465`; §11 proof by components, ideals, and invariants.

Source summary: Uses decomposition into idempotent components over Omega, representation modules generating isomorphisms, and invariant idempotent sums to prove the subgroup/invariant-field direction.

Japanese title: 成分冪等元と不変元による証明

補題の証明では、第一種という仮定により \(\mathfrak S_\Omega\) が次数 \(s\) だけの体へ分解することを使う。各 \(E_\nu\Omega\) は表現加群として、\(\mathfrak S\) から部分体 \(\Sigma_i\) への同型を生む。

\(\mathfrak T_\Omega\) は \(E_1\mathfrak T_\Omega+\cdots+E_s\mathfrak T_\Omega\) に分解し、各 \(E_\nu\mathfrak T_\Omega\) は \(t\) 個の単純イデアルへ分かれる。これらの成分が \(\mathfrak T_\Omega\) の既約表現を与え、\(\mathfrak S_\Omega\) へ制限すると元の表現に一致する。

逆方向では、\(\mathfrak H\) に含まれない自己同型で固定されない \(T\)-元を作ればよい。Galois 群の元は成分 \(e_\nu\) を置換するので、\(\mathfrak H\) の軌道に沿った和 \(E_1=e_1+\cdots+e_h\) を作ると、これは \(\mathfrak H\) で不変だが、外の自己同型では不変でない。

Simplified Chinese title: 用幂等分量与不变量证明

引理的证明利用第一类假设：\(\mathfrak S_\Omega\) 分解为 \(s\) 个域。每个 \(E_\nu\Omega\) 作为表示模，产生从 \(\mathfrak S\) 到子域 \(\Sigma_i\) 的同构。

\(\mathfrak T_\Omega\) 分解为 \(E_1\mathfrak T_\Omega+\cdots+E_s\mathfrak T_\Omega\)，而每个 \(E_\nu\mathfrak T_\Omega\) 又分解为 \(t\) 个单理想。这些分量给出 \(\mathfrak T_\Omega\) 的不可约表示；限制到 \(\mathfrak S_\Omega\) 时，它们与原表示一致。

反方向只需构造一个 \(T\)-元素，使它在不属于 \(\mathfrak H\) 的自同构下不保持不变。Galois 群元素置换分量 \(e_\nu\)，因此沿 \(\mathfrak H\) 的轨道取和 \(E_1=e_1+\cdots+e_h\)，它在 \(\mathfrak H\) 下不变，但在外部自同构下不变。

Script/codepoint and TeX/PDF notes:

- Idempotent component is 成分冪等元 / 幂等分量, draft only.
- Preserve \(E_\nu\Omega\), \(E_\nu\mathfrak T_\Omega\), \(e_\nu^{(i)}\Omega\), and \(E_1=e_1+\cdots+e_h\).
- Direct-sum and ideal-decomposition language is not tensor-product evidence.

Unresolved flags:

- Some symbols in lines 21433-21445 are OCR-shifted; source-image review needed.
- Idempotent-component wording needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-20-006-components-complementary-basis-and-general-extension-theorem

Anchor: German baseline lines `21467-21530`; §§12-13 formal meaning of components and general extension theorem.

Source summary: Explains component idempotents via inverse matrices and complementary bases, notes their role in the different of a number field, and states the general extension theorem for irreducible representations of fully reducible commutative hypercomplex systems.

Japanese title: 成分の意味・補基・一般拡張定理

§12 は、\(\mathfrak Z\) の固定基底 \(z_1,\ldots,z_n\) を用いて、単位元の成分 \(e_j\) の形式的意味を説明する。同型 \(\Theta_i\) によって \(z_\nu\) は \(Z_i\) の基底 \(\zeta_\nu^{(i)}\) へ写り、逆に \(e_j=\sum_\nu \varrho_\nu^{(j)}z_\nu\) と表される。

そこから、\(\zeta\)-行列と \(\varrho\)-行列が互いに逆行列になることが従う。言い換えれば、\(\varrho_1^{(i)},\ldots,\varrho_n^{(i)}\) は \(\zeta_1^{(i)},\ldots,\zeta_n^{(i)}\) に対する補基であり、数体のディッフェレントの理論で役割を持つ。

§13 の一般拡張定理では、\(\mathfrak Z\) を可換・超複素・完全可約系とし、部分系 \(\mathfrak S,\mathfrak T\) を考える。各既約表現 \(H_i\) は、ちょうど \(t\) 通りに \(\mathfrak T\) の表現へ拡張できると述べられる。

Simplified Chinese title: 分量意义、补基与一般扩张定理

§12 用 \(\mathfrak Z\) 的固定基 \(z_1,\ldots,z_n\) 说明单位元分量 \(e_j\) 的形式意义。同构 \(\Theta_i\) 把 \(z_\nu\) 映到 \(Z_i\) 的基 \(\zeta_\nu^{(i)}\)，反过来 \(e_j=\sum_\nu \varrho_\nu^{(j)}z_\nu\)。

由此可知，\(\zeta\)-矩阵与 \(\varrho\)-矩阵互为逆矩阵。换言之，\(\varrho_1^{(i)},\ldots,\varrho_n^{(i)}\) 是 \(\zeta_1^{(i)},\ldots,\zeta_n^{(i)}\) 的补基，并在数域不同式理论中起作用。

§13 的一般扩张定理设 \(\mathfrak Z\) 为交换、超复、完全可约系统，并考虑其子系统 \(\mathfrak S,\mathfrak T\)。每个由同态 \(H_i\) 给出的不可约表示，都恰好可以以 \(t\) 种方式扩张为 \(\mathfrak T\) 的表示。

Script/codepoint and TeX/PDF notes:

- Complementary basis follows C11/C16 convention 補基 / 补基; Differente follows ディッフェレント / 不同式.
- Preserve \(e_j=\sum_\nu\varrho_\nu^{(j)}z_\nu\), inverse matrices, \(E\mathfrak T=a_1\mathfrak S+\cdots+a_t\mathfrak S\), and \(\mathfrak T_\Omega\cdot E\).
- Lines 21520-21530 are OCR-damaged. The line 21524 formula and previously noted noisy local \otimes vicinity are not treated as tensor-product source anchors because no Tensorprodukt term or tensor-product explanation appears.

Unresolved flags:

- General extension theorem passage needs source-image verification because of OCR damage around lines 21520-21530.
- Tensor product remains blocked despite noisy formula vicinity.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
