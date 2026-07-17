# Exposé III B semantic tranche — source/formula comparison

## Authorities

- French workpass: `sga5_fr_workpass.tex`, SHA-256 `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original LNM 589 scan: `SGA5 (1).pdf`, SHA-256 `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.
- Scan mapping: printed page = one-based scan PDF page minus 12.
- Pre-tranche English snapshot: SHA-256 `8322E14DAEBE5EDFF35FCF5A71BFB863DE5C8AACEF5F1106D8394C5FB4496F07`.
- Immediate reviewed/build English snapshot: SHA-256 `9D97AB94F341801EC8937BD407440B4AD98E8DDD17EDE27A8C90CD243CF390BB`.
- Earlier coordination cumulative after non-overlapping edits outside III B: SHA-256 `94FD91FD0EF018E95D0C9EE04A34B8DDABCF3F7D5DB224B9D5320FE479B3EC25`.
- Later coordination cumulative after further non-overlapping edits outside III B: SHA-256 `237ACFB99BBD51A83495662F9D56260768DB7CFB4F22AE132583B2A3D71EF978`.
- Final-package revalidation cumulative snapshot: SHA-256 `313435A40E17DF53DC9C86D271548EFCE1C27520662D609D05C4FB373211E4F2`.
- Stable live Exposé III B slice: SHA-256 `0405187228682396D5D78830868277F35B37B3036BDF6435C139145E84246CC5`.

The French TeX was compared line-by-line at every receipt anchor. The rendered original scan was then checked at every materially changed printed page. Formula edits were not inferred from matching counts.

## Formula and category decisions

| Receipt | Source location | Reviewed English result | Evidence and decision |
|---|---|---|---|
| `0130` | p.149 / FR 4512 | `$P,Q\in\Ob D_{\mathrm{ctf}}(Z)$` | The source has no superscript `b`; scan PDF p.161 confirms. |
| `0142` | p.149 / FR 4537 | `$P=DL\lten_SM$`, `$Q=L\lten_SDM$` | The scan prints base `S` and unprimed `M`. The inherited `$M'$` was not retained. |
| `0146` | p.176 / FR 5325–5337 | Square `(*)`, displays `(2)` and `(3)`, and exact cross-references restored | Scan PDF p.188 shows all three labels and the `(2)`/`(3)` dependency of the upper/lower arrows. |
| `0156` | pp.199–200 / FR 6488 | `$(fc_1)^{-1}(V)$` connected and `$d_1^{-1}(V)\subset d_2^{-1}(V)$` | Scan PDF pp.211–212 prints the two separate hypotheses across a page break. The inherited equality and an earlier audit shorthand that omitted the inclusion were both rejected. |
| `0411` | p.184 / FR 5581 | second argument `F_1\lten_{S,A_2}F_2` | French TeX and scan PDF p.196 agree. A smoother-looking inserted `p_1^*` was rejected. |
| `0415–0417` | p.184 / FR 5548–5571 | explicit left/right categories `${}_AX_2`, `${}_BY_C`, `${}_BX_{1A}`, `${}_AX_{2B}`, `${}_AY_2`, `${}_BY_{1A}`, `${}_AY_{2C}` | Each module side was checked against scan PDF p.196. These are mathematical variance data. |
| `0419` | p.186 / FR 5691 | `$\Tr_A:\delta^*\RHom_A(p_1^*L,p_2^!L)$` | Scan PDF p.198 confirms that `c_*` is absent at definition 6.5.3. |
| `0420` | p.188 / FR 5770–5774 | successive bases `\lten_A`, `\lten_{\Lambda}`, `\lten_A` | Scan PDF p.200 visibly distinguishes the three bases. |
| `0421` | p.188 / FR 5787 | final `$KA_{X_1}\lten_AKA_{X_2}$` | Only the final identification changes to base `A`; the preceding source occurrence remains over `\Lambda`. |
| `0429` | p.201 / FR 6557 | lower-left node `$p_2^!P'\lten_{\Lambda}Q$` | Already current at the pre-tranche snapshot; parent structural repair verified, not overwritten. |
| `0430` | p.201 / FR 6574 | footnote category `$D_{\mathrm{ctf}}({}_{\Lambda[G]}Y)$` | Already current; no source superscript `-`. |

## Structural and rendered cross-check

After the semantic edits and the source-presentation repair in §5.9, Exposé III B has exact coarse structural parity:

- TikZ commutative diagrams: `40 / 40` (French / English).
- TikZ pictures: `1 / 1`.
- Total diagram blocks: `41 / 41`.
- Footnotes: `7 / 7`.
- Equation environments: `145 / 145`.
- Unnumbered display openings: `240 / 240`.
- Explicit tags: `151 / 151`, with no III B tag multiset difference.
- Statements: `28 / 28`, with no III B statement-number multiset difference.

All materially changed English pages and the corresponding source scan pages are listed in `RENDER_QA.csv`. No unresolved source ambiguity remains in this tranche.

`REPAIR_EVIDENCE_LEDGER.csv` gives the printed source page, stable-live English line or statement, exact correction, authority/evidence, and disposition for every repair and preserved receipt. `ANCHOR_VALIDATION.csv` records the final stable-live anchor uniqueness audit.
