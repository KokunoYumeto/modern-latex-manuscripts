# Noether CJK Draft Corpus Translation Slices: Continuation 36

Generated UTC: `2026-07-04T10:56:49.196037+00:00`

Status: `draft/non-canonical/not native reviewed/not approved/not gate-promoted`.

Draft/non-canonical Japanese and Simplified Chinese corpus slices. Not native reviewed. Not approved. No gate promotion.

Korean remains source-discovery/crosswalk only in this continuation.

## Metadata

- Baseline SHA256: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Coverage: Continuation 36 covers German baseline 23743-23855, the joint E. Noether addendum through the received-date and bibliography boundary.
- Slice count: `5`

## Slices

### cjk-continuation-36-001-noether-addendum-residue-system-and-length

- German anchor: `23743-23751`
- Source summary: The addendum jointly with E. Noether says the equation system (1) also gives a rational method for determining a full residue system modulo q, meaning representatives of the finitely many residue classes linearly independent over the coefficient field P. This clarifies the steps in the main theorem and yields that the resultant multiplicity agrees with the length of the ideal q, equivalently the rank of the residue-class ring or the number of P-linearly independent residue classes. The ideal-theoretic interpretation is attributed to E. Noether, while the proof of later formulas is attributed to Kapferer.
- Japanese title: E. Noether 共同補遺: 完全剰余系とイデアルの長さ
- Simplified Chinese title: E. Noether 共同补遗：完全剩余系与理想长度

**Japanese Draft**

E. Noether と共同の補遺は、方程式系 (1) が \(q\) に関する完全剰余系を決定する有理的方法も与える、と述べる。ここで完全剰余系とは、係数体 \(P\) に関して、\(q\) を法として線形独立な有限個の剰余類の代表系を意味する。

これにより主定理の証明に現れる各段階が見通しよくなり、副産物として、結果式重複度 \(u\) がイデアル \(q\) の長さと一致することが得られる。この長さは、剰余類環の階数、あるいは \(P\) に関して線形独立な剰余類の数としても記述される。

脚注的な注記では、イデアル論的解釈は E. Noether に由来し、後続の式 (5) と (6) の基礎的証明は H. Kapferer による、とされる。

**Simplified Chinese Draft**

与 E. Noether 共同撰写的补遗说明，方程组 (1) 同时给出一种有理方法，用来确定模 \(q\) 的完全剩余系。这里的完全剩余系，是指相对于系数域 \(P\)，模 \(q\) 线性无关的有限多个剩余类的代表系。

这样，主定理证明中的各个步骤变得更透明；同时还得到一个副结果：结式重数 \(u\) 与理想 \(q\) 的长度一致。这个长度也可描述为剩余类环的秩，或相对于 \(P\) 线性无关的剩余类数。

脚注式说明中还指出，理想论解释出自 E. Noether，而后面公式 (5) 与 (6) 的基础证明出自 H. Kapferer。

**Script/TeX Notes**

- Preserve `volles Restsystem`, `Restklassenring`, `Länge des Ideals q`, and `Resultantenmultiplizität` as reviewer-visible terms.
- Restklassenring is drafted as 剰余類環 / 剩余类环.
- This is source/context evidence for ideal length and residue classes, not a localization or Noetherian-ring closure.

**Unresolved Flags**

- Line 23745 uses `u` for resultant multiplicity, likely \(\mu\); source-image review needed before formula normalization.
- Line 23763 has OCR-like `Plinear`; preserve as P-linear in draft notes only.

### cjk-continuation-36-002-satz-iv-full-residue-system-and-relations

- German anchor: `23767-23787`
- Source summary: Satz IV characterizes a full residue system modulo q using the h_i and powers of y. Each block h_i, h_i y, ..., h_i y^{(g_i)-1} gives a full residue system from q^{(i+1)} to q^{(i)}. Since q^{(i+1)}=(q^{(i)},h_i), it remains to prove relations (4), namely h_i x=0 and h_i y^{(g_i)}=0 modulo q^{(i)}, and relation (5), that h_i F(y)=0 modulo q^{(i)} implies F(y)=0 modulo y^{(g_i)}. Relations (4) exhaust residue classes and (5) expresses linear independence; finite ideal length then proves Satz IV and identifies the length of q with the sum of the g_i.
- Japanese title: 定理 IV: 完全剰余系と関係式 (4), (5)
- Simplified Chinese title: 定理 IV：完全剩余系与关系式 (4)、(5)

**Japanese Draft**

Satz IV は、(1) と Hilfssatz II の記号を用いて、\(q\) に関する完全剰余系を記述する。各段階で \(h_i, h_i y, \ldots, h_i y^{(g_i)-1}\) というブロックが現れ、それぞれが \(q^{(i+1)}\) から \(q^{(i)}\) への完全剰余系を与える。

定義から \(q^{(i+1)}=(q^{(i)},h_i)\) が従うので、Satz IV の証明は二種類の関係式に還元される。第一は \(h_i x\equiv0\) および \(h_i y^{(g_i)}\equiv0\pmod{\mathfrak q^{(i)}}\) であり、第二は \(h_iF(y)\equiv0\pmod{\mathfrak q^{(i)}}\) なら \(F(y)\equiv0\pmod{y^{(g_i)}}\) である。

関係式 (4) は、\(h_i, h_i y,\ldots,h_i y^{(g_i)-1}\) の線形結合が該当する剰余類を尽くすことを表し、(5) は線形独立性を表す。\(q^{(t+1)}\) が単位イデアルになることから、Satz IV と、\(q\) の長さが \((g_1)+\cdots+(g_t)\) に等しいことが従う。

**Simplified Chinese Draft**

Satz IV 用 (1) 和 Hilfssatz II 的记号描述模 \(q\) 的完全剩余系。在每一步中出现形如 \(h_i, h_i y, \ldots, h_i y^{(g_i)-1}\) 的块；每个这样的块都给出从 \(q^{(i+1)}\) 到 \(q^{(i)}\) 的完全剩余系。

由定义立刻得到 \(q^{(i+1)}=(q^{(i)},h_i)\)，因此 Satz IV 的证明化为两类关系。第一类是 \(h_i x\equiv0\) 与 \(h_i y^{(g_i)}\equiv0\pmod{\mathfrak q^{(i)}}\)；第二类是若 \(h_iF(y)\equiv0\pmod{\mathfrak q^{(i)}}\)，则 \(F(y)\equiv0\pmod{y^{(g_i)}}\)。

关系式 (4) 表示 \(h_i, h_i y,\ldots,h_i y^{(g_i)-1}\) 的线性组合穷尽相应剩余类，而 (5) 表示线性无关性。由于 \(q^{(t+1)}\) 成为单位理想，于是得到 Satz IV，并得到 \(q\) 的长度等于 \((g_1)+\cdots+(g_t)\)。

**Script/TeX Notes**

- Preserve \(h_i, h_i y, \ldots, h_i y^{(g_i)-1}\), \(q^{(i+1)}=(q^{(i)},h_i)\), and relations (4), (5).
- Einheitsideal is 単位イデアル / 单位理想.
- The displayed formula at line 23769 appears OCR-repetitive (`h_i, h_i, y`); draft normalizes only in prose and flags source review.

**Unresolved Flags**

- Line 23769 likely has repeated `h_i`/comma OCR noise in the full residue-system list.
- Line 23771 prints `q^{(i)}=(q^{(i+1)})`, likely incomplete or OCR-distorted; source-image review needed.

### cjk-continuation-36-003-proof-of-relations-four-and-five

- German anchor: `23789-23812`
- Source summary: The first relation (4) is read from (1); the second follows from h_i g_i=0 modulo q^{(i)}, hence h_i y^{(g_i)} is zero modulo q^{(i)} after dividing g_i(0,y) by y^{(g_i)}. For (5), f_i and g_i have only a common divisor d(y) not divisible by y; after removing it, q^{(i)} is the primary component at the origin. The proof multiplies by an auxiliary polynomial G(x,y) avoiding p and uses coprimality of the reduced f_i and g_i to conclude F(y)=0 modulo y^{(g_i)}.
- Japanese title: 関係式 (4) と (5) の証明
- Simplified Chinese title: 关系式 (4) 与 (5) 的证明

**Japanese Draft**

第一の関係式 (4) は、方程式系 (1) から直接読み取れる。第二の関係式は、\(h_i g_i\equiv0\pmod{\mathfrak q^{(i)}}\) から出発し、\(g_i(0,y)\) を \(y^{(g_i)}\) で割った因子を用いて、\(h_i y^{(g_i)}\equiv0\pmod{\mathfrak q^{(i)}}\) を導く。

(5) の証明の準備として、\(f_i\) と \(g_i\) の共通因子は \(y\) で割れない \(d(y)\) に限られる、と述べられる。これを取り除いた \(\bar f_i\) と \(\bar g_i\) は互いに素であり、\(\mathfrak q^{(i)}\) は \((\bar f_i,\bar g_i)\) の零点に対応する準素成分として扱われる。

さらに、原点以外の零点に対応する準素成分を避ける補助多項式 \(G(x,y)\) を作り、仮定 \(h_iF(y)\equiv0\pmod{\mathfrak q^{(i)}}\) を \((f_i,g_i)\) に関する恒等式へ移す。\(\bar f_i\) と \(\bar g_i\) の互いに素性から、最後に \(F(y)\equiv0\pmod{y^{(g_i)}}\) が従う。

**Simplified Chinese Draft**

第一条关系式 (4) 可直接从方程组 (1) 读出。第二条关系从 \(h_i g_i\equiv0\pmod{\mathfrak q^{(i)}}\) 出发，利用把 \(g_i(0,y)\) 除以 \(y^{(g_i)}\) 后的因子，推出 \(h_i y^{(g_i)}\equiv0\pmod{\mathfrak q^{(i)}}\)。

在证明 (5) 前，文本指出 \(f_i\) 与 \(g_i\) 的公共因子只能是一个不被 \(y\) 整除的 \(d(y)\)。去掉它之后，\(\bar f_i\) 与 \(\bar g_i\) 互素，而 \(\mathfrak q^{(i)}\) 被看作 \((\bar f_i,\bar g_i)\) 在原点对应的准素分量。

接着构造辅助多项式 \(G(x,y)\)，避开原点以外零点的准素分量，把假设 \(h_iF(y)\equiv0\pmod{\mathfrak q^{(i)}}\) 转化为关于 \((f_i,g_i)\) 的恒等式。由 \(\bar f_i\) 与 \(\bar g_i\) 互素，最后推出 \(F(y)\equiv0\pmod{y^{(g_i)}}\)。

**Script/TeX Notes**

- Preserve \(h_i g_i\), \(g_i(0,y):y^{(g_i)}\), \(d_i(y)\bar f_i\), \(d_i(y)\bar g_i\), and \(G(x,y)\).
- Primärkomponente is 準素成分 / 准素分量.
- This slice contains ideal components and divisibility, not localization evidence.

**Unresolved Flags**

- Lines 23791-23812 contain dense OCR-sensitive formulas, especially colon-division notation and barred symbols.
- Line 23793 breaks mid-sentence after `für jedes`; source-image review needed for exact continuity.

### cjk-continuation-36-004-ideal-quotients-and-hilfssatz-ii-proof

- German anchor: `23814-23843`
- Source summary: Remark I writes relations (4) and (5), together with Hilfssatz II, as reciprocal relations between ideal quotients: q^{(i)}:q^{(i+1)}=(q^{(i)},x)=(y^{(g_i)},x) and q^{(i)}:(q^{(i)},x)=q^{(i+1)}. The first summarizes (4) and (5); the second follows analogously. These relations give the necessity part of Hilfssatz II: from K_i=0 modulo q_i one gets (K_i)>=(g_i) and then K_{i+1}=0 modulo q^{(i+1)}. A footnote defines ideal quotient a:b as all polynomials c(x,y) with b c=0 modulo a, and references Macaulay for reciprocal relations in irreducible ideals.
- Japanese title: イデアル商と Hilfssatz II
- Simplified Chinese title: 理想商与 Hilfssatz II

**Japanese Draft**

Bemerkung I は、関係式 (4), (5) と Hilfssatz II を、イデアル商のあいだの相互的な関係として書き直す。中心となる形は、\(q^{(i)}:q^{(i+1)}=(q^{(i)},x)=(y^{(g_i)},x)\) および \(q^{(i)}:(q^{(i)},x)=q^{(i+1)}\) である。

第一の関係は (4) と (5) をまとめたものであり、第二の関係は同様の議論で得られる。これにより Hilfssatz II の必要性も示される。すなわち、\(K_i\equiv0\pmod{\mathfrak q_i}\) から \((K_i)\ge(g_i)\) が従い、さらに式 (3) と第二の関係により \(K_{i+1}\equiv0\pmod{\mathfrak q^{(i+1)}}\) が従う。

脚注では、イデアル商 \(\mathfrak a:\mathfrak b\) は、\(\mathfrak b c\equiv0\pmod{\mathfrak a}\) となる多項式 \(c(x,y)\) 全体として定義される。また、既約イデアルの一般理論では二つの相互関係の一方が他方を含意することが Macaulay によって参照される。

**Simplified Chinese Draft**

Bemerkung I 把关系式 (4)、(5) 连同 Hilfssatz II，改写为理想商之间的相互关系。核心形式是 \(q^{(i)}:q^{(i+1)}=(q^{(i)},x)=(y^{(g_i)},x)\)，以及 \(q^{(i)}:(q^{(i)},x)=q^{(i+1)}\)。

第一条关系概括了 (4) 和 (5)，第二条关系可由类似论证得到。由此也给出 Hilfssatz II 的必要性：从 \(K_i\equiv0\pmod{\mathfrak q_i}\) 可得 \((K_i)\ge(g_i)\)，再由式 (3) 和第二条关系推出 \(K_{i+1}\equiv0\pmod{\mathfrak q^{(i+1)}}\)。

脚注中，理想商 \(\mathfrak a:\mathfrak b\) 被定义为所有多项式 \(c(x,y)\)，使得 \(\mathfrak b c\equiv0\pmod{\mathfrak a}\)。文本还引用 Macaulay，说明在不可约理想的一般理论中，这两条相互关系中的一条蕴含另一条。

**Script/TeX Notes**

- Preserve colon notation \(\mathfrak a:\mathfrak b\) as ideal quotient / イデアル商 / 理想商.
- Do not treat `Idealquotienten` as `Lokalisierung`; it is colon-ideal material in this source.
- Preserve Macaulay, Modular Systems, Cambridge Tracts 19 (1916), Nr. 72 and 73.

**Unresolved Flags**

- Line 23821 uses bare `q` rather than consistently fraktur q; formula transcription needs source-image review.
- Line 23843 has escaped footnote markup `\&lt;sup\textgreater16)` and should be cleaned only in a canonical pass.

### cjk-continuation-36-005-sufficiency-iteration-and-bemerkung-ii

- German anchor: `23845-23855`
- Source summary: The text says sufficiency is read off directly; finite iteration of Hilfssatz II gives the main theorem, and iteration of the second relation (6) gives Zusatz I. Remark II states a further form for (K,q^{(i)}) when K is not divisible by q, reducing it to (h_i y^lambda, q^{(i)}) and identifying the lowest such power with (K). The paper is marked received 24 Oct. 1926, followed by clearpages and then the bibliography at line 23857.
- Japanese title: 十分性、反復、Bemerkung II と次境界
- Simplified Chinese title: 充分性、迭代、Bemerkung II 与下一边界

**Japanese Draft**

十分性は直接読み取れる、と本文は述べる。Hilfssatz II を有限回反復すると主定理が得られ、第二の関係 (6) を反復すると Zusatz I が得られる。

Bemerkung II では、\(q\) で割れない多項式 \(K\) についてさらに述べる。条件のもとで \((K,\mathfrak q^{(i)})\) は \((h_i y^\lambda,\mathfrak q^{(i)})\) の形に帰着され、そのような最小冪が \((K)\) と一致すると説明される。

論文は `Eingegangen am 24. 10. 1926` として受理日を記し、その後 23855 行の改ページを経て、23857 行から Bibliographie が始まる。

**Simplified Chinese Draft**

文本说，充分性可直接读出。对 Hilfssatz II 作有限次迭代得到主定理；对第二条关系 (6) 作迭代则得到 Zusatz I。

Bemerkung II 对不能被 \(q\) 整除的多项式 \(K\) 作进一步说明。在相应条件下，\((K,\mathfrak q^{(i)})\) 化为 \((h_i y^\lambda,\mathfrak q^{(i)})\) 的形式，并说明这种最低幂与 \((K)\) 一致。

论文最后标注 `Eingegangen am 24. 10. 1926` 作为收稿日期；随后在 23855 行换页，23857 行开始 Bibliographie。

**Script/TeX Notes**

- Preserve `q:a'`, `q:t`, `q®%`, and other noisy quotient/power glyphs only as unresolved source notes; do not canonicalize from OCR.
- Preserve \((K,\mathfrak q^{(i)})=(h_i y^\lambda,\mathfrak q^{(i)})\).
- Next cursor after this continuation is the bibliography at German baseline line 23857.

**Unresolved Flags**

- Lines 23845-23852 are heavily OCR-corrupted around powers and q-symbols; the prose records structure only.
- Bibliography is a different unit and should be handled separately from the addendum prose.
