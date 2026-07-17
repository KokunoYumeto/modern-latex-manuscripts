# Papers 01–19 — R823 Spanish source-parity audit

Audit snapshot: 2026-07-17T21:51:16+02:00

## Outcome

Papers 01–19 have been reconciled directly, paper by paper, from the live German R823 source into the Spanish cumulative. The status `source-reconciled` in the v3 unit ledger is based on bilingual/source-delta review of the actual TeX spans, including formulas, source-note topology, titles, metadata, section order, and terminal matter; it is not inferred from display counts, length ratios, or similarity scores.

No open content-bearing R823 delta remains in Papers 01–19 at this handoff. An immutable P01–P19 snapshot compiles successfully after the final Paper 17 and Paper 19 register normalization. Overall R823 acceptance, including the root-owned final cumulative build, all later units, and the corpus-wide rendered-page visual gate, remains the root task's responsibility.

## Authority and reviewed target

- R823 package: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717_COMPLETE.zip`
- R823 package SHA-256: `7AFC1B865EC710F6BECE507260605CBA7C950E5CC089C7464F63CBC20A8BD738`
- R823 German TeX: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\authority_r823\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex`
- R823 German TeX SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Spanish cumulative TeX: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\work\spanish\cum_es.tex`
- Spanish cumulative TeX SHA-256 at final unit validation: `7B9097D657B6A39F9304197FA65A9A16BD5EAEAE190340EE735CD867EA8A7861`

The cumulative-file hash is a build snapshot and may change when the root task edits units after Paper 19. The unit hashes in the v3 CSV are the continuation-safe Papers 01–19 cursor.

## Unit-level evidence

- Required v3 review ledger: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\work\spanish\evidence\PAPERS_01_19_R823_REVIEW_V3.csv`
- Ledger SHA-256: `C54C6B3E6C0CA4430DC6F31C547195A8651805697B40E7234BD39CBD45149DA8`
- Earlier exact-hash manifest retained for provenance: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\work\spanish\evidence\PAPERS_01_19_R823_PARITY_MANIFEST.csv`

Combined exact and normalized scope hashes, formed by concatenating the live slices P01 through P19 in order:

| Scope | SHA-256 | Characters |
|---|---|---:|
| R823 P01–P19 exact | `DADFC84E020F7F10E04B007593B0E9B101659A94098AA6F6566D46A8CE85ACE7` | 955321 |
| Spanish P01–P19 exact | `44E8CFBB34EF93819DCA2C985E151F0F376EF467BD4A7F865B8B81478467F4A5` | 948516 |
| R823 P01–P19 normalized | `D4C9DD756908BA368478DAF91E39D68027CC3A8C9E8B7EDDD354F877C61770B7` | — |
| Spanish P01–P19 normalized | `E2076FAF6EEE40CF9F4A38A13E1A27DC40C0D32E4C46EA0FD2E3FF1ECB3E3243` | — |

The German and Spanish hashes necessarily differ by language. They identify the reviewed source/target slices and make later drift detectable; they are not equality claims.

## Reconciliation performed

- Papers 01–05: reconciled titles/authorship/metadata; restored Paper 02 Chapter II §4 with its formulas and notes; corrected Paper 03 formulas; corrected Paper 04 formulas including the source product-versus-pair structure at (33), and restored the four missing source notes.
- Papers 06–13: restored the Paper 06 Mertens note; corrected Paper 08 operators/formulas; restored the Paper 09 Steinitz note; corrected Papers 10 and 12 notation/formulas; propagated the Paper 13 R823 sum delta, restored two missing notes, and separated the two source notes that had been merged around formula (1).
- Papers 14–16: propagated every content-bearing R704-to-R823 delta in these spans, including Paper 14 equation structure, `B(z,s)\varphi(z,s)`, and Fuëter; and Paper 15 symbol, exponent, product, superscript, equality, and final-substitution distinctions. Paper 16 formulas and indices were checked and corrected against R823.
- Papers 17–19: corrected Paper 17 formulas and congruences (`t_{1\varkappa}a_\varkappa`, `t_{ii}a_i=a_i`, MQ/PQ/NP/QP, `\xi-(y/x)\eta`, and `F(\xi,\eta)`); normalized `Polynombereich` to `anillo de polinomios` and `Modulbasis` to `base del módulo`/`base como módulo`; checked the full Paper 18 congress unit; propagated the Paper 19 R823 notation through Definition I, Lemma III, and the final divisor system (`A_i`, `r_e`, `\varrho`, `L_i`, explicit products, and `B_e/B_{e+1}`); and completed the same ring-sense terminology normalization throughout Paper 19 while retaining true `dominio íntegro` and domain-of-values senses.

Actual source notes were reconciled by position and content. A naive regex count in Paper 06 also sees macro-definition artifacts from the cumulative's source machinery; those artifacts were excluded and the real notes were reviewed manually.

## Terminology decisions for this span

| German sense | Canonical Spanish in context | Decision |
|---|---|---|
| `Faltung` | `plegamiento` | Geometric/invariant-theory operation; do not substitute the modern analytic `convolución`. |
| `Reihe` | `fila`, `fila de formas` | In the invariant-theory passages it denotes an ordered row/family, not a numerical `serie`. |
| `Integritätsbasis` | `base íntegra` | Standard algebraic sense. |
| `Restklasse`, `Restgruppe` | `clase residual`, `grupo residual` | Retained consistently throughout the early corpus. |
| `kleinstes gemeinsames Vielfaches` | `mínimo común múltiplo` | Ideal/module divisibility sense. |
| `größter gemeinsamer Teiler` | `máximo común divisor` | Ideal/module divisibility sense. |
| `primär`, `Primideal` | `primario`, `ideal primo` | Preserve the primary/prime distinction. |
| `reduzierte Darstellung` | `representación reducida` | Canonical technical register. |
| `Polynombereich` | `anillo de polinomios`, `anillo polinómico` | Use ring terminology; avoid the calque `dominio polinómico` where the source denotes the ring. |
| `Modulbasis` | `base del módulo`, `base como módulo` | Avoid the calque `base modular`. |

The distinct source symbols `\rho`, `\varrho`, `e`, `\nu`, and `\varkappa` are sense-bearing notation and were preserved rather than homogenized.

## Isolated build evidence

The root task owns the only final cumulative build. To prevent concurrent post-P19 edits from invalidating this scoped evidence, the live P01–P19 content was copied into an immutable TeX snapshot and terminated immediately before Paper 20; the untouched continuation remains below that early `\end{document}` as provenance.

- Command: `latexmk -xelatex -interaction=nonstopmode -halt-on-error cum_es_p01_19.tex`
- Working directory: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\work\spanish\evidence\PAPERS_01_19_ISOLATED_BUILD`
- Result: success, 219 pages, XeLaTeX plus `xdvipdfmx`.
- Isolated TeX SHA-256: `8ADC3AEBFEF8FBE923C9560F88C04E66914E5D985ECE06C47E416CCC43CA17F8`
- Isolated PDF SHA-256: `CF611C45C58B67116DD956212C500B4457BEDCE7B6606345AC38DCF629CD2894`
- Isolated log SHA-256: `3364919266F5A3DC5AAB4CCF195DF8A166D5CF353C523A2418ABB7646128DA94`

The isolated log contains no TeX error, undefined control sequence, emergency stop, fatal error, overfull/underfull box, or missing-character message. Its nonfatal diagnostics are the XeLaTeX `inputenc` notice and the expected `mathrsfs` size substitutions.

## Rendered-page QA evidence

The final isolated PDF was rendered at 144 dpi. Pages 173–175 (Paper 17 title/introduction/general-polynomial-ring transition), 195–197 (Paper 19 title/introduction and register changes), 207, 210, 212, 214–217 (all later Paper 19 register-change pages), and 219 (formula-heavy terminal page) were visually inspected. The final images show consistent margins and hierarchy, legible formulas and footnotes, correct page numbering, and no clipped, overlapping, missing, or black-boxed content.

- Render directory: `C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\romance_rebase_20260717\work\spanish\evidence\visual_qa\PAPERS_01_19_FINAL_20260717`
- Contact sheet, pages 173–197: `contact_01_pages_173_197_FINAL.png`, SHA-256 `C6C4B24E69AE38964D242C8370BF18290409F7C0A3FE41ADCDA1F5DA53AEA5B8`
- Contact sheet, pages 207–219: `contact_02_pages_207_219_FINAL.png`, SHA-256 `64A144DF4CA26274A6DA49A5AF94EE16682DFE63062C5F58979C510E54E93F47`

This scoped inspection supplements, but does not replace, the root task's required corpus-wide changed-page and representative-spread QA.

## Continuation cursor

The next content-review cursor after this scope is Paper 20. Papers 01–19 have no known open R823 source delta at this handoff. Any later edit to one of these spans must update the corresponding target hash and review finding in `PAPERS_01_19_R823_REVIEW_V3.csv`, rebuild, and re-run the relevant rendered-page QA. The root task must combine this source/build evidence with its corpus-wide visual-QA evidence before claiming the full Spanish acceptance gate.
