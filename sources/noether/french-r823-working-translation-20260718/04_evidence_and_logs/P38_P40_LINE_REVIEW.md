# Papers 38 and 40: source-keyed French line review

Date: 2026-07-17  
Status: **complete for the P38/P40 scope**

## Authority and preservation

- German authority: `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`
- Authority SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Preserved pre-review tree: `working/backups/p1_43_pre_rebase_audit_20260717/tex/`
- Live French sources: `working/r823_fr/tex/N38_fr_body.tex` and `working/r823_fr/tex/N40*_fr_body.tex`
- The backup was not altered. All production edits were made only in the live French tree.

## Orthography pass and manual review

The first pass restored visible French diacritics without touching TeX control sequences, mathematics, or German titles.

- Machine-readable record: `evidence/P38_P40_DIACRITIC_REWRITE.json`
- Record SHA-256: `A566B3676D385C810CB17E0445E1401D3B646BFF3C266C8A850DB7B011BB53FC`
- Total replacements: `1548`
- Per-file totals: P38 `399`; P40 introduction/§1 `235`; §2 `164`; §3 `47`; §4 `101`; §5 `89`; §6 `106`; §7 `137`; §8 `136`; §9 `134`.
- Generator: `tools/restore_ascii_french_diacritics.py`, SHA-256 `70418E99EF4CAF3DAF6827AD45E62E9221690D3777BAFA421CC33081B1832D7E`.

A second reviewed orthography list repaired only context-checked French words and protects German titles such as *Theorie*, *Systeme*, and *Probleme*.

- Tool: `tools/p38_p40_reviewed_orthography_pass.py`
- Tool SHA-256: `A5021F9E4DCD4EE47D37ED48ACF949D5234B3281B3DC426CADB8640F093DAB12`
- Reproducible dry run against `working/checkpoint/tex`: `480` replacements.
- Dry run against the final live sources: `0` replacements.

Every P38 and P40 body line was then read manually against the R823 German. Accent cleanliness was not treated as evidence of semantic or stylistic completion.

## Binding P38 dispositions

| Requested locus | R823 source | Disposition in live French |
|---|---|---|
| lines 12--25 | lines 18817--18830 | Recast the opening, dedication, three-reduction sentence, repeated wording in the long note, and the reduction criterion into idiomatic mathematical French. The theorem and logical scope are unchanged. |
| line 55 | line 18860, `vom Primzahlpotenzgrad p^e` | Repaired the ungrammatical phrase to `de degré \(p^e\), puissance d'un nombre premier`. |
| lines 57--60 | lines 18862--18865 | Recast the Albert priority note and the history of the third reduction without changing attribution, chronology, or mathematical claims. |
| line 109 | line 18919, `Des weiteren ermöglicht` | Replaced the literal transition by `En outre, l'assertion I permet de déterminer ...`. |
| line 192 | line 19002 | Replaced `De K≤K' suit trivialement` by `De \(K\leqq K'\), il résulte trivialement que ...`. The authority itself changes the split algebra from `A` to `A'`. This is a transparent source typo: extending the splitting field leaves the **same** algebra split. The French therefore keeps `A` in both clauses and records the editorial correction here. |
| lines 197--203 | lines 19007--19013 | Recast the Schur transition and replaced the false calque `anneau de groupe rationnel entier` by the exact modern object `algèbre de groupe \(G=\mathbb Q[\mathfrak G]\)`. |

The other specifically requested clusters (12--25, 57--60, 109, and 197--203) were checked sentence by sentence and are now explicitly disposed above; none was waived as merely stylistic.

## Binding P40 dispositions

| Requested locus | R823 source | Disposition in live French |
|---|---|---|
| introduction, lines 27--33 | lines 19138--19144 | Recast the overview into canonical French: theory *of representations*, module viewed over an extension ring, structural theorems, anti-isomorphic division ring, second proof, and passage to the commutative case. `corps de scission minimal` replaces the calque `corps minimal de rupture`. |
| introduction/§1, lines 80--103 | lines 19191--19209 | `kommutative Verbundenheit` is rendered by commutation of the two actions; `durchlaufendes Assoziativgesetz` is rendered `loi d'associativité mixte`. The formulas (2), (2*), (2a), and (2a*) remain unchanged. |
| introduction/§1, lines 110--130 | lines 19213--19231 | Recast the canonical maps into automorphism rings, with `homomorphisme d'anneaux`, `antihomomorphisme d'anneaux`, `anti-isomorphe`, and commuting images. Removed the literal `s'applique homomorphiquement`, `se laisse appliquer`, and `devient directement isomorphe` constructions. The historical label `représentation réciproque` is retained. |
| §2, line 29 | line 19265 | `car il en suit` became `car il s'ensuit, par définition,`. |
| §2, line 40 | line 19276 | `il en suit en outre` became `il s'ensuit en outre`. |
| §2, line 92 | line 19322 | `liés commutativement avec` became `commutent avec l'action de`; the final distinction is explicitly `anti-isomorphismes`, not merely `antihomomorphismes`. |
| §5, line 31 | line 19476 | `Il reste essentiellement seulement` became `Il ne reste essentiellement qu'à démontrer ...`. |
| §9, line 11 | line 19735 | `Des §§ ... il vient` became `Il résulte des §§ ... que ...`. |
| §9, line 21 | line 19739 | `devient isomorphe` became `est isomorphe à \(A\) comme anneau`. |
| §9, line 34 | line 19757 | The dangling `Exprimé pour ...` became `Formulés en termes de représentations irréductibles, ces résultats donnent ...`. |

The sense-specific choice is already present in `evidence/GERMAN_FRENCH_TERMINOLOGY_LEDGER.md` and `.csv`: `reziprok ringhomomorph` is `antihomomorphisme d'anneaux`; its bijective case is an `anti-isomorphisme`. `Représentation réciproque` remains available only as Noether's historical representation label. At review time the ledger hashes were:

- Markdown: `EA9A791356ADAB5B875087338C3FD44DC583CD22E6D2C6DFD84746434952F682`
- CSV: `435BFEBFB069488D27021AA6331F54B2FB2DADC4BFF56D7BEFA373E4815E1D93`

## Content-bearing parity corrections retained

The line review also rechecked and retained three earlier source-keyed repairs:

1. P40 §2 restores the four-step R823 matrix-composition calculation ending in `BA`; the recovered French had collapsed it into a false `AB=BA` statement.
2. P40 §8 restores the conjugate extension-system notation `Z_{Z^{(i)}}` rather than `Z\Omega`/`Z_{(i)}`.
3. P40 §9 uses `\mathfrak C` for the composition-series ideal, matching R823; the recovered French had `\mathfrak c`.

## Final source hashes

| Source | Preserved pre-review SHA-256 | Final live SHA-256 | Lines before/after |
|---|---|---|---|
| `N38_fr_body.tex` | `61E39D6EBA3B67A186DFA7684BE7EE4D9A83FA0A05930A1D48AFD5E4AC0CFD2A` | `CAA81796A80078E5877B1FEBED933BF27705B1159A3AF1BC3F2CF18463C41B18` | 213/213 |
| `N40_intro_s01_fr_body.tex` | `160690EE6080047539340F54C590886BBFF052DA72DABB5C5758991DC635BC7E` | `A91211BAB7081A923EAC1DDA39D2A614FA85DA7117DE9F6D565DF0F8EAA575EF` | 153/153 |
| `N40_s02_fr_body.tex` | `80F038E11C6657CEC0871E95F0963D3F19DCDE67C53890F2B221B4212A9EA2E4` | `CE4264FABA667EBCBE23C7AD86E9C7A2A4B8D6A9E07C9E0AACB22FAD35477116` | 108/109 |
| `N40_s03_fr_body.tex` | `0072F4145C1E557F352F4CE97E6F3C2DE4BEC51870B155802A033BC23FDB833C` | `D1B1A0B3A8ADC9DD2490422B49BB545094D623D0E16923E24F5593BF6C4AB04B` | 98/98 |
| `N40_s04_fr_body.tex` | `6BA7B54AD9C8C46726BEE3A55B52B9DB6F7960DD326AFD6FE650D87DED19C9FA` | `2C87568D450E9885E610AC2DF1B65CA157BD66E4E445A141E426A49B7F97306C` | 74/74 |
| `N40_s05_fr_body.tex` | `8F7C213D1C5D25174C40B8066E01333FA0F3EABBED7A155EC5DB4C620C6260AF` | `7B9FC44368805A7E3F1C6FBF55179EAE4A16137539F1C7B609DB1E5616763C8E` | 33/33 |
| `N40_s06_fr_body.tex` | `12B69A94658966688E1465FE225B57989A15A2FBFF6182E1A31AE4B91BE6BCA0` | `56C518161FE418EECE5DCBA0CF5821D2B0AC69312BC6D1D1659FD01AEAA66D6B` | 100/100 |
| `N40_s07_fr_body.tex` | `9B00D56A0ED5AB2380C32E3944918ABB9945F659011E819F98A62411E20D0169` | `9D696D6956330CC9C27C80481ECC90E20AE0D685E7E298FBC6D24F96A666FDA8` | 85/85 |
| `N40_s08_fr_body.tex` | `7361C469E790B7F40A47251A66DE375C187AA9350E346CF23CCC54887B0F45F7` | `37E3DF0F22268476270E6F66754B5EBCE77C0F2C096291A3CCAD91A078D6F859` | 142/142 |
| `N40_s09_fr_body.tex` | `805222CF048E8AC5EABEAD86495EF225F24216ECDA1BFD288938CE591E91DEBF` | `5894716801FD84010DA9555AF1E45EB9DD1079C7D619BDC57B5ADE5742794AFA` | 44/44 |

## Residual scans

The following case-sensitive scans over `N38_fr_body.tex` and all `N40*_fr_body.tex` returned zero hits:

- `a la`, unaccented `cite*`, `mentionnes`, lowercase `systemes`;
- common UTF-8 mojibake markers;
- `operator-`, `operatoriellement`;
- `réciproquement isomorphe`, `homomorphe réciproquement`, `isomorphisme réciproque`;
- every binding calque pattern: `de degré puissance`, `De ... suit`, `liés commutativement`, `associative traversante`, `il en suit`, `Des §§ ... il vient`, and `Exprimé pour`.

Every remaining plain `a` and `ou` encountered in the manual pass was checked as a verb/mathematical variable or conjunction, not a missing `à`/`où`.

## Build and visual QA

- Cumulative driver: `working/r823_fr/tex/cum_fr_P40_s09.tex`
- Driver SHA-256: `1C926C5F3016B0E871057A9A86DFFD9751EE89A38ED64D2865FED275A6BB4B25`
- Engine: pdfTeX 1.40.29, MiKTeX 26.5.
- Command: two passes of `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "-output-directory=<build>" cum_fr_P40_s09.tex` from the live TeX directory.
- Output: `build/p40_line_review_20260717/cum_fr_P40_s09.pdf`, 401 pages.
- PDF SHA-256: `1BC04506EFFA7992A3632FE964816F321037AC8C2A2C2B5B5B3450E42AE6E617`
- Final log SHA-256: `FBA9B24D3C7B568EB53401EC718DA908CF50E26D76777006B431A39B8C71904A`
- Pass-1 console SHA-256: `BA4831D301384C54EAEF67E477D8E00FA9492F99EFD07E514FB01D2752861474`
- Pass-2 console SHA-256: `E6109DF7DAA355D05CA8718DD5866B6879536A4A001F427A07C4F4801D1A1A26`
- Final log scan: zero LaTeX/package warnings, errors, undefined controls/references/citations, overfull boxes, and underfull boxes.

The final PDF was rendered with Poppler at 150 dpi. All 32 pages from the start of P38 through the end of P40 were inspected: P38 pp. 370--375, P39 pp. 376--379 as intervening continuity, and P40 pp. 380--401. The inspection found no clipping, collisions, broken equations, unreadable accents, missing glyphs, or header/footer/page-number defects.

Rendered directory: `tmp/pdfs/p38_p40_line_review_final_20260717/`  
Thirty-two page PNGs; SHA-256 over the ordered concatenation of their individual SHA-256 values: `0D42B021BC3AA202AE087BD0F9ABCC3A5B9DDAD77776364E77A762E0029336DC`.

| Contact sheet | SHA-256 |
|---|---|
| `sheet_370_373.png` | `2C2085E63C79CA023A59F41BCF31F825FBA14B1B23597770902930B71CB09EFA` |
| `sheet_374_377.png` | `8292C8098F347A292125E914D7DF7ED96248C2F8E1E68A7F8621CE33CB8C2726` |
| `sheet_378_381.png` | `A144AE4A50DB7492007ED9C94E91D3C2F13742795F2323CCF4F371F92913B9AA` |
| `sheet_382_385.png` | `F6CA86DFA30D7EF3C0908162E34D533BBCE6831891AD039059B1C13F8ECB67D6` |
| `sheet_386_389.png` | `CDA136CB20EF50DE6D28283E7FB2449C0200DEFBB632F4F48A6DBFE3B2EBB623` |
| `sheet_390_393.png` | `F73657A8B3EB37D4907A9C990327D177CBA27B191758167D8C6AA76A9EA95C20` |
| `sheet_394_397.png` | `330D319CEBBCB1885862D3A2B80AE627FFF3B559380E4AD1A161C98C750D44D6` |
| `sheet_398_401.png` | `FF3C7DEA39FB0918DDF25582698FB4DA35C815801FCC8B81A8CF308C9AB747AC` |

## Acceptance conclusion

Every binding P38/P40 language item has an explicit source-keyed disposition; the two content-bearing notation defects and the false matrix calculation are repaired; the live sources pass the residual scans; and the latest cumulative build and full changed-page visual inspection are clean. P38/P40 can therefore be cited as completed work in the P01--P43 reconciliation ledger, keyed to the final hashes above.
