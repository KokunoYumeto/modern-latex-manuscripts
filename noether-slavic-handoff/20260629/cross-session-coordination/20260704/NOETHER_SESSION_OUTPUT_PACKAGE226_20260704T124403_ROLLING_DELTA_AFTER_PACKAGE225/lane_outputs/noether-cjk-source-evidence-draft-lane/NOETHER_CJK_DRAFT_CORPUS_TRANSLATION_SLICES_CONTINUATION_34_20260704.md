# Noether CJK Draft Corpus Translation Slices: Continuation 34

Generated UTC: `2026-07-04T10:40:26.680607+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical Japanese and Simplified Chinese corpus slices. Not native reviewed. Not approved. No gate promotion.

Korean remains source-discovery/crosswalk only in this continuation.

## Metadata

- Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Coverage: Continuation 34 covers German baseline 23531-23605, completing Deuring lecture Chapter VI §31 before the Kapferer/Noether next unit begins at 23606.
- Slice count: `5`

## Slices

### cjk-continuation-34-001-cyclic-special-case-finite-fields

- German anchor: `23531-23563`
- Source summary: §31 begins by using the cyclic crossed representation to reprove the §20 theorem that every finite field is commutative. The proof uses two facts about finite commutative fields: Galois fields are cyclic over every subfield, and every element of P is a norm from beta when beta is cyclic over P. For finite R with center P and cyclic splitting field I, K_I is isomorphic to P*/N I*, hence trivial, so no field different from P can have P as center.
- Japanese title: 巡回特殊例による有限体の可換性
- Simplified Chinese title: 由循环特殊情形证明有限域的交换性

**Japanese Draft**

§31 は、巡回的な交叉表示を使って、§20 で証明された定理をもう一度証明するところから始まる。第一の応用は、有限個の元から成る任意の体は可換である、という主張である。

証明は、可換な有限体、すなわちガロア体についての二つの既知事実に基づく。第一に、ガロア体はその任意の部分体上で巡回である。第二に、\(\beta\) が \(P\) 上巡回なガロア体なら、\(P\) のすべての元は \(\beta\) の元のノルムであり、\(P^*=N(\beta^*)\) となる。

いま \(\Re\) を有限体、\(\mathsf P\) をその中心、\(\Im\) を巡回分解体とする。§30 の結論と上の二事実から、\(\Im\) に対する類 \(\{\Re\}\) の群 \(\mathscr K_{\Im}\) は \(\mathsf P^*/N\,\Im^*\) と同型で、したがって単位類 \(\{\mathsf P\}\) に等しい。従って、中心を \(\mathsf P\) とする \(\mathsf P\) と異なる体は存在せず、\(\Re=\mathsf P\) となる。

**Simplified Chinese Draft**

§31 开始用循环交叉表示重新证明 §20 中的定理。第一个应用是：由有限多个元素组成的任一域都是交换的。

证明依赖关于交换有限域，也就是 Galois 域的两个已知事实。第一，Galois 域在其任一子域上都是循环的。第二，若 \(\beta\) 是 \(P\) 上的循环 Galois 域，则 \(P\) 的每个元素都是 \(\beta\) 中某个元素的范数，即 \(P^*=N(\beta^*)\)。

现在令 \(\Re\) 为有限域，\(\mathsf P\) 为其中心，\(\Im\) 为循环分裂域。由 §30 的结论和上述两个事实，关于 \(\Im\) 的类 \(\{\Re\}\) 所成的群 \(\mathscr K_{\Im}\) 同构于 \(\mathsf P^*/N\,\Im^*\)，因而等于单位类 \(\{\mathsf P\}\)。所以不存在以 \(\mathsf P\) 为中心但不同于 \(\mathsf P\) 的域，故 \(\Re=\mathsf P\)。

**Script/TeX Notes**

- Preserve \(\mathscr K_{\Im}\), \(\mathsf P^*/N\,\Im^*\), and \(P^*=N(\beta^*)\).
- Galoisfelder is drafted as ガロア体 / Galois 域.
- This is finite-field commutativity evidence, not tensor-product or localization evidence.

**Unresolved Flags**

- Line 23563 uses \(\Im\) and \(\mathscr K_{\Im}\); source-image review should confirm the splitting-field glyph.
- The phrase `Klassenkörpertheorie im Minimalen` is rendered descriptively here and needs domain review before glossary promotion.

### cjk-continuation-34-002-real-field-and-quaternion-extension

- German anchor: `23565-23573`
- Source summary: The second application says the only genuinely noncommutative field extension over the real field P is the quaternions. Since the complex field is the only commutative extension of P and is algebraically closed, only it can be the splitting field. Positive numbers are norms, so P*/N I* has degree two; besides {P} there is one class, the quaternions. The normal form comes from -1 as a normalized factor system: R = I + Iu, u^2 = -1.
- Japanese title: 実数体上の非可換拡大と四元数
- Simplified Chinese title: 实数域上的非交换扩张与四元数

**Japanese Draft**

第二の応用は、実数体 \(P\) 上の真に非可換な体拡大は四元数以外に存在しない、という §20 の定理である。

\(P\) は中心でなければならない。なぜなら、\(P\) の可換拡大としては複素数体 \(\Im\) しかなく、\(\Im\) は代数閉体なので、それを中心とする非可換体拡大は存在しないからである。従って分解体として問題になるのも \(\Im\) だけであり、しかも \(\Im\) は \(P\) 上巡回である。

さらに、任意の正数はノルムであるから、商群 \(P^*/N\Im^*\) の次数は 2 である。従って \(\{P\}\) のほかにはただ一つの類 \(\{\Re\}\) だけがあり、それが四元数である。正規形も同時に得られ、同伴類の中で \(-1\) を正規化因子系に取ると、\(\Re=\Im+\Im u\)、\(u^2=-1\) となる。すなわち \(\Re=P+Pi+(P+Pi)u\)、\(i^2=-1\)、\(u^2=-1\) と読める。

**Simplified Chinese Draft**

第二个应用是 §20 的定理：实数域 \(P\) 上唯一真正非交换的域扩张是四元数。

\(P\) 必须是中心。因为 \(P\) 的交换扩张只有复数域 \(\Im\)，而 \(\Im\) 代数闭，所以以 \(\Im\) 为中心不存在非交换的域扩张。因此唯一可能作为分裂域的也是 \(\Im\)，并且 \(\Im\) 在 \(P\) 上是循环的。

此外，每个正数都是范数，所以商群 \(P^*/N\Im^*\) 的阶为 2。于是除 \(\{P\}\) 以外只有一个类 \(\{\Re\}\)，这就是四元数。规范形也同时得到：若在同伴类中取 \(-1\) 为规范化因子系，则 \(\Re=\Im+\Im u\)，且 \(u^2=-1\)。也就是说，可读作 \(\Re=P+Pi+(P+Pi)u\)、\(i^2=-1\)、\(u^2=-1\)。

**Script/TeX Notes**

- Preserve \(P^*/N\Im^*\), \(\Re=\Im+\Im u\), and \(u^2=-1\).
- Line 23573 prints `\(1^2=-1\)`; draft reads this as likely OCR for \(i^2=-1\) and flags it.
- Quaternionen is 四元数 / 四元数.

**Unresolved Flags**

- Line 23573 needs source-image review for the likely `i^2=-1` glyph.
- The normal-form statement should be checked by a domain reviewer before canonical use.

### cjk-continuation-34-003-norm-theorem-counting-remark

- German anchor: `23575-23577`
- Source summary: A remark explains that the second known finite-field fact can also be proved from the end of §30. It identifies a group S as Z^{*S-1} and as Z*/P*, because exactly elements of P* induce the identity automorphism of the main genus. For finite Z, counting yields N(Z*) = Z*/S and therefore P* = N(Z*), with a comparison to the number of genera and ambiguous classes, always 'in the minimal'.
- Japanese title: ノルム事実の個数計算による再証明
- Simplified Chinese title: 用计数重新证明范数事实

**Japanese Draft**

第一の応用への注では、上で用いた既知事実 2 も §30 の結論から導ける、と説明する。

そこで現れる群 \(\mathscr S\) は、\(3^{*S-1}\) あるいは \(3^*/P^*\) と同型なものとして書かれている。主種の恒等自己同型を生むのはちょうど \(P^*\) の元であり、同じことは \(S-1\) を適用したとき単位に移る元としても表現される。

有限な \(3\) の場合、\(\mathscr S\) の元数は \(P^*\) の \(3^*\) における指数に等しい。従って \(3^*/\mathscr S\) の元数は \(P^*\) の元数に等しく、同じことが \(N(3^*)=3^*/\mathscr S\) にも成り立つので、\(P^*=N(3^*)\) が得られる。これは「種の数 = 不分岐的な曖昧類の数」という数論的表現に対応するが、ここでは常に「最小において」と補う必要がある。

**Simplified Chinese Draft**

关于第一个应用的注释说明，上面使用的已知事实 2 也可由 §30 的结论推出。

其中出现的群 \(\mathscr S\) 被写成同构于 \(3^{*S-1}\) 或 \(3^*/P^*\)。恰好 \(P^*\) 中的元素诱导主属的恒等自同构；同一事实也可表述为在作用 \(S-1\) 下进入单位元的那些元素。

当 \(3\) 有限时，\(\mathscr S\) 的元素数等于 \(P^*\) 在 \(3^*\) 中的指数。因此 \(3^*/\mathscr S\) 的元素数等于 \(P^*\) 的元素数；同理 \(N(3^*)=3^*/\mathscr S\)，于是得到 \(P^*=N(3^*)\)。这对应于“属数 = 歧义类数”的数论说法，但在这里处处都要补上“在最小情形下”。

**Script/TeX Notes**

- Preserve baseline glyph `3` in notes because it likely stands for a fraktur/splitting-field symbol.
- Preserve \(\mathscr S\), \(3^{*S-1}\), \(3^*/P^*\), and \(N(3^*)=3^*/\mathscr S\).
- Ambigen Klassen is drafted as 曖昧類 / 歧义类 but flagged for review.

**Unresolved Flags**

- Lines 23575-23577 have OCR-sensitive `3` glyphs that likely represent the splitting field; source-image review needed.
- The ambiguous-class/genus vocabulary needs native/domain review.

### cjk-continuation-34-004-p-adic-cyclic-case-and-hasse-note

- German anchor: `23579-23591`
- Source summary: The third application says that if P is a p-adic ground field and beta is cyclic of degree n over P, then the group K_beta of classes split by beta is isomorphic to the Galois group of beta. The text calls this a direct consequence of 'class field theory in the small'. A remark says the group order/exponent relation makes the exponent equal the index, and cites Hasse, Math. Ann. 104, for the statement that H_beta consists of all classes whose index divides n.
- Japanese title: p 進基礎体と巡回分解体
- Simplified Chinese title: p-adic 基域与循环分裂域

**Japanese Draft**

第三の応用は、\(P\) が \(p\) 進基礎体で、\(\beta\) が \(P\) 上 \(n\) 次の巡回拡大である場合を扱う。このとき、\(\beta\) によって分解される類 \(\{\Re\}\) の群 \(\mathcal K_{\beta}\) は、\(\beta\) のガロア群と同型である。

これは §30 の結論によって、「小さな類体論」が述べる \(P^*/N3^*\) 型の同型から直接従う、と説明されている。ただしこの箇所の記号には OCR らしい乱れがあり、特に \(3\) と \(\emptyset\) のように見える部分は原資料確認が必要である。

注では、\(\mathcal H_3\) の元の群位数、すなわち \(\{\Re\}\) の指数が、その指標に等しくなることが述べられる。生成元の指数は \(n\) であり、指標も \(n\) の約数かつ指数の倍数だからである。さらに H. Hasse, Math. Ann. 104 により、\(\mathcal H_3\) は指標が \(n\) の約数であるすべての類 \(\{\Re\}\) から成る、とされる。従って \(P\) 上 \(n\) 次の任意の巡回分解体は、同じ体類群 \(\mathcal H_3\) を与える。

**Simplified Chinese Draft**

第三个应用处理如下情形：\(P\) 是 \(p\)-adic 基域，\(\beta\) 是 \(P\) 上 \(n\) 次的循环扩张。此时由 \(\beta\) 分裂的类 \(\{\Re\}\) 所成的群 \(\mathcal K_{\beta}\) 同构于 \(\beta\) 的 Galois 群。

文本说明，这由 §30 的结论直接推出，是“小的类域论”中 \(P^*/N3^*\) 型同构的后果。不过这一处记号有明显 OCR 风险，尤其看作 \(3\) 和 \(\emptyset\) 的部分需要核对原图。

注释进一步说，\(\mathcal H_3\) 中元素的群阶，也就是 \(\{\Re\}\) 的指数，等于其指标。生成元的指数为 \(n\)，而指标既是 \(n\) 的因子又是指数的倍数。H. Hasse 在 Math. Ann. 104 中还证明，\(\mathcal H_3\) 由所有指标整除 \(n\) 的类 \(\{\Re\}\) 组成。因此，\(P\) 上任一 \(n\) 次循环分裂域都给出同一个域类群 \(\mathcal H_3\)。

**Script/TeX Notes**

- Preserve \(\mathcal K_{\beta}\), \(P^*/N3^*\), \(\mathcal H_3\), and H. Hasse, Math. Ann. 104.
- p-adisch is drafted as p 進 / p-adic to keep readability in JP/zh-Hans.
- Exponent and Index are kept distinct as 指数 / 指標 in Japanese and 指数 / 指标 in zh-Hans.

**Unresolved Flags**

- Line 23589 has probable OCR in \(P^*/N3^*\simeq\emptyset\); source-image review required before canonical formula transcription.
- Line 23591 uses `3` repeatedly for a likely field symbol; preserve as source-sensitive, not normalized.
- Hasse citation is source evidence only; no web verification was needed for this local draft.

### cjk-continuation-34-005-small-class-field-inverse-theorem-and-next-unit

- German anchor: `23593-23605`
- Source summary: The section closes by listing two facts as the essential content of the inverse theorem of class field theory in the small: the group of all classes over P whose index divides n is cyclic of degree n, and every cyclic splitting field of degree n over P generates the full group of classes. A clearpage follows; the next German baseline unit begins at line 23606 with Kapferer's paper on multiplicity conditions for Noether's fundamental theorem of algebraic functions.
- Japanese title: 小さな類体論の逆定理と次単位
- Simplified Chinese title: 小的类域论逆定理与下一单元

**Japanese Draft**

§31 は、二つの事実を「小さな類体論」の逆定理の本質的内容としてまとめて終わる。

第一に、\(P\) 上で指標が \(n\) を割るすべての類 \(\{\Re\}\) の群は、\(n\) 次の巡回群である。第二に、\(P\) 上 \(n\) 次の任意の巡回分解体は、類 \(\{\Re\}\) の全群を生成する。

23605 行の改ページで Deuring 講義のこの範囲は区切られ、次のドイツ語基準単位は 23606 行から始まる Kapferer 論文「代数関数の Noether 基本定理に対する必要十分な重複度条件」である。

**Simplified Chinese Draft**

§31 最后把两个事实概括为“小的类域论”逆定理的本质内容。

第一，在 \(P\) 上所有指标整除 \(n\) 的类 \(\{\Re\}\) 所成的群，是 \(n\) 次循环群。第二，\(P\) 上任一 \(n\) 次循环分裂域都会生成类 \(\{\Re\}\) 的整个群。

23605 行的换页结束了 Deuring 讲义的这一段；下一处德文基准单元从 23606 行开始，是 Kapferer 关于代数函数的 Noether 基本定理的必要且充分重数条件的论文。

**Script/TeX Notes**

- Preserve \(\{\Re\}\), `Index Teiler von n`, and `zyklisch n-ten Grades` in reviewer notes.
- Umkehrsatz der Klassenkörpertheorie im Kleinen is drafted as 小さな類体論の逆定理 / 小的类域论逆定理.
- Next cursor is line 23606; Noetherschen Fundamentalsatz is a title/context anchor, not a Noetherian-ring term closure.

**Unresolved Flags**

- Class-field-theory terminology needs native/domain review.
- Line 23606 opens a new paper/unit and should be handled as a separate next continuation.
