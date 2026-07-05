# Noether CJK Draft Corpus Translation Slices: Continuation 18

Generated UTC: `2026-07-04T08:41:16.641444+00:00`

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

- tensor product: no German Tensorprodukt anchor; Paper 43 §7 direct sum language is non-anchor evidence
- localization: Quotientenring candidates now include 16223-16225, 18467, 20105, 20228, 20240, 20284, 20949, 20953, and 21009, plus Quotientenkörper at 20822; no direct Lokalisierung label
- Harish-Chandra: no German corpus anchor
- abstract algebra: no new abstract-algebra anchor in Paper 43 §7
- modern algebra: Moderne Algebra remains bibliographic only; no modern-algebra anchor in Paper 43 §7

## cjk-continuation-18-001-ramification-theory-main-order-mod-pt

Anchor: German baseline lines `20951-20966`; §7 ramification theory of the main order mod p^t.

Source summary: Begins the ramification-theory section, passes through a quotient ring for relative fields, and reduces the different of the residue class ring to the components after p factorization.

Japanese title: 主整環 mod \(p^t\) の分岐理論

§7 は、数体の主整環を \(p^t\) で見た場合の分岐理論を扱う。相対体の場合には、素イデアルによる主整環の商環へ移ると述べられるが、ここでも `Lokalisierung' という語は現れない。

不定元 \(u_1,\ldots,u_n\) を添加すると、主整環と \(p^t\) による剰余環の双方が \(e,U,\ldots,U^{n-1}\) を \(\mathfrak h\)-加群基底として持つ。したがって、どちらの場合にも \(G'(u)\) がディッフェレントを与える。

\(p=\mathfrak p_1^{\varrho_1}\cdots\mathfrak p_r^{\varrho_r}\) と分解すると、\(p^t\) による剰余環は成分の直和になる。したがって、十分大きい \(t\) については、各成分のディッフェレントを調べればよく、\(\mathfrak p^{\varrho t}\) による剰余環へ問題が還元される。

Simplified Chinese title: 主阶模 \(p^t\) 的分歧理论

§7 讨论数域主阶模 \(p^t\) 时的分歧理论。相对域情形中，文本说要转到按素理想取的主阶商环；这里仍没有出现 `Lokalisierung' 一词。

添加不定元 \(u_1,\ldots,u_n\) 后，主阶和模 \(p^t\) 的剩余类环都以 \(e,U,\ldots,U^{n-1}\) 为 \(\mathfrak h\)-模基。因此在两种情形中，\(G'(u)\) 都给出不同式。

若 \(p=\mathfrak p_1^{\varrho_1}\cdots\mathfrak p_r^{\varrho_r}\)，则模 \(p^t\) 的剩余类环分解为分量直和。因此当 \(t\) 足够大时，只需研究各分量的不同式，问题化为模 \(\mathfrak p^{\varrho t}\) 的剩余类环。

Script/codepoint and TeX/PDF notes:

- Records Quotientenring at line 20953 as localization-adjacent but not Lokalisierung.
- Residue class ring is 剰余環 / 剩余类环.
- Keep \(p^t\), \(\mathfrak p_i^{t\varrho_i}\), and \(G'(u)\) in TeX.

Unresolved flags:

- Localization remains blocked despite quotient-ring passage.
- Ramification terminology needs native/domain review.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-18-002-basis-and-defining-equation-for-residue-class-ring

Anchor: German baseline lines `20967-20985`; §7 choice of xi, basis, and defining equation.

Source summary: Chooses xi satisfying Ore-style congruences, describes a basis by powers of xi and phi(xi), and gives the defining equation F(x)=phi(x)^rho+pM(x).

Japanese title: 剰余環の基底と定義方程式

\(\xi\) を、\(\varphi(\xi)\equiv0\pmod{\mathfrak p}\) かつ \(\varphi(\xi)\not\equiv0\pmod{\mathfrak p^2}\) となるように選ぶ。ここで \(\varphi(x)\) は \(p\) mod の次数 \(f\) の素関数である。

\(t\ge2\) では、\(\xi\) を冪等元 \(e_1\) によって \(\xi^*=\xi e_1\) に置き換え、\(\mathfrak p_1=(p,\varphi(\xi^*))\) とできる。基底は \(\xi^{\mu_0}\varphi(\xi)^{\nu_0}\)、\(\mu_0=0,\ldots,f-1\)、\(\nu_0=0,\ldots,\varrho-1\) で与えられる。

この基底に関する定義方程式は \(F(x)=\varphi(x)^\varrho+pM(x)\) であり、\(M(x)\) は mod \(p\) で \(\varphi(x)\) によって割り切れない。

Simplified Chinese title: 剩余类环的基与定义方程

选择 \(\xi\)，使 \(\varphi(\xi)\equiv0\pmod{\mathfrak p}\) 且 \(\varphi(\xi)\not\equiv0\pmod{\mathfrak p^2}\)。这里 \(\varphi(x)\) 是模 \(p\) 的 \(f\) 次素函数。

当 \(t\ge2\) 时，用幂等元 \(e_1\) 把 \(\xi\) 替换为 \(\xi^*=\xi e_1\)，从而可有 \(\mathfrak p_1=(p,\varphi(\xi^*))\)。基由 \(\xi^{\mu_0}\varphi(\xi)^{\nu_0}\) 给出，其中 \(\mu_0=0,\ldots,f-1\)，\(\nu_0=0,\ldots,\varrho-1\)。

相对于这个基，定义方程为 \(F(x)=\varphi(x)^\varrho+pM(x)\)，其中 \(M(x)\) 在模 \(p\) 下不能被 \(\varphi(x)\) 整除。

Script/codepoint and TeX/PDF notes:

- Prime function mod p is rendered descriptively, not promoted.
- Idempotent \(e_1\) remains 冪等元 / 幂等元.
- Keep \(F(x)=\varphi(x)^\varrho+pM(x)\) in TeX.

Unresolved flags:

- Ore terminology and prime-function wording need review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-18-003-independence-and-polynomial-differential-quotient

Anchor: German baseline lines `20986-21007`; §7 basis independence and Ore reduction.

Source summary: Proves independence by successive division by p and concludes that the different of the residue class ring is given by the polynomial differential quotient F'(xi), reducing to Ore's results.

Japanese title: 独立性と \(F'(\xi)\) によるディッフェレント

基底の独立性は、合同式を \(p\) で順次割っていく議論で示される。まず \(\mathfrak p\) mod で \(a_0(\xi)\equiv0\) を得て、そこから \(a_0(x)\equiv0\pmod p\) を導く。

同じ手順を繰り返すと、すべての \(a_i(x)\) がまず mod \(p\)、次に mod \(p^2\)、さらに mod \(p^t\) まで消えることが分かる。したがって、提示された元は独立な基底である。

これにより、剰余環のディッフェレントは多項式微分商 \(F'(\xi)\) によって与えられる。議論は Ore の結果に還元され、各 \(\mathfrak p\) について \(p^t=p^n\) で十分であること、さらに Supplementzahlen が得られることが述べられる。

Simplified Chinese title: 独立性与由 \(F'(\xi)\) 给出的不同式

基的独立性通过不断除以 \(p\) 的论证得到。先在模 \(\mathfrak p\) 下得到 \(a_0(\xi)\equiv0\)，进而推出 \(a_0(x)\equiv0\pmod p\)。

重复同一过程，可知所有 \(a_i(x)\) 先在模 \(p\) 下为零，再在模 \(p^2\) 下为零，一直到模 \(p^t\) 下为零。因此给出的元素确为独立基。

于是，剩余类环的不同式由多项式微分商 \(F'(\xi)\) 给出。整个论证归约到 Ore 的结果，并说明对每个 \(\mathfrak p\)，取 \(p^t=p^n\) 已足够，进而得到 Supplementzahlen。

Script/codepoint and TeX/PDF notes:

- Supplementzahlen is left as Supplementzahlen pending source review.
- Polynomial differential quotient follows C14/C17 terminology: 多項式微分商 / 多项式微分商.
- Keep \(F'(\xi)\) and congruence displays in TeX.

Unresolved flags:

- Supplementzahlen needs source and native/domain review.
- No retained blocker changes.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

## cjk-continuation-18-004-relative-differents-and-paper43-close

Anchor: German baseline lines `21009-21012`; §7 relative differents and received date.

Source summary: States that the same quotient-ring passage applies to relative differents and adds the product relation for upper-field, lower-field, and relative differents, then closes Paper 43.

Japanese title: 相対ディッフェレントと第43論文の終結

最後に、商環への移行によって、同じ議論が相対ディッフェレントにも成り立つと述べられる。この `Quotientenring' も、局所化 row を閉じる直接の `Lokalisierung' 証拠ではない。

追加されるのは、上体のディッフェレントが、下体のディッフェレントと相対ディッフェレントの積として表せる、という点である。

第43論文は、受理日として 1949 年 10 月 25 日を記して閉じる。

Simplified Chinese title: 相对不同式与第43篇论文收束

最后，文本说通过转到商环，同样论证也适用于相对不同式。这个 `Quotientenring' 仍不是关闭 localization 行的直接 `Lokalisierung' 证据。

需要补充的是，上域不同式可表示为下域不同式与相对不同式的乘积。

第43篇论文以收稿日期 1949 年 10 月 25 日结束。

Script/codepoint and TeX/PDF notes:

- Records Quotientenring at line 21009 as localization-adjacent but not Lokalisierung.
- Received date is rendered as an exact Gregorian date, not a translation claim.
- Paper 43 is complete through line 21012 in this continuation.

Unresolved flags:

- Relative-different product wording needs review.
- Localization remains blocked.

Status label: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.
