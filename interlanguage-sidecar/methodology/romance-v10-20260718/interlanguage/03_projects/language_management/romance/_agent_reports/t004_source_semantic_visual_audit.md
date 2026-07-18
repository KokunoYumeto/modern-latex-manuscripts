# Independent source / semantic / visual audit — R823_HG_T004

Date: 2026-07-17  
Audit boundary: `R823_HG_T004` only; German authority lines 21117–21146 inclusive.  
Verdict: **PASS (bounded production gate)**. The source slice, clause map, controlled-Romance text, terminology/grammar ledgers, validator, clean build, warning scan, and both rendered pages satisfy the requested T004 checks. This is **not** native-speaker review, human intelligibility evidence, or promotion of any construction candidate.

## 1. Authority identity and clause completeness

- Authority: `Noether_R823_cum_de.tex`, SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- Exact inclusive slice: authority lines 21117–21146, reconstructed byte-identically as `source/R823_HG_T004_de_exact.tex`, SHA-256 `2D757BFD661CE638D41F593DF6636A939AA0042477B6169A38217CAD23FB71BF`.
- The numbered inspection copy has SHA-256 `C97FC627F77DCB0CF6100AFB916AFF7EC056BAF717C33080DB54545DAD5D4B5D`.
- Seven source ranges, S041–S047, cover the full bounded slice without an uncovered nonblank authority line. Their mapped target side contains 16 distinct target clause IDs, and every referenced target clause is present in the TeX.
- The source and target each contain three display-math blocks. No placeholder, TODO, or omitted-matter marker was found.
- The continuation cursor correctly starts after the bounded unit at authority line 21148; this audit does not extend the translation boundary.

## 2. Semantic fidelity checks

| Required check | Result | Evidence in the controlled-Romance text |
|---|---|---|
| Uniqueness scope | PASS | T-039 says that each representation module determines a unique **class of representations**. It does not collapse the claim to a uniquely determined individual representation. The direct/reciprocal branches are both retained. |
| Abbreviations | PASS | The source abbreviations are preserved explicitly and in the same pairings: `d. D. M. a d. D. K.; r. D. M. a r. D. K.` |
| Self-map without surjectivity | PASS | T-041/T-042 say that multiplication defines a homomorphism `de M a se mesme` and a linear transformation of M to itself. No positive claim of surjectivity appears. The editorial scope note expressly prevents reading “to itself” as surjectivity. |
| Mixed associativity | PASS | `(cm)\tau=c(m\tau)` is retained before the operator/linearity inference. |
| Linearity | PASS | The additivity and right-scalar compatibility formulas are retained with the same variables and primes. |
| Sum formula and order | PASS | The transformation sum remains tied to `(c_1+c_2)m`. |
| Product formula and order | PASS | The source convention is preserved through `m \mapsto (m'')'=c_1c_2m`; the construction does not silently reverse the factors under a modern function-composition convention. |
| Image object versus map | PASS | `imagine \overline{D}` names the resulting ring/object, while `homomorfism de anels` names the map. The final editorial note repeats this distinction rather than conflating the image with the homomorphism. |
| Basis–matrix correspondence | PASS | An arbitrary basis `x_1,\ldots,x_n`, the matrix equation `x'_j=cx_j=\sum_i x_i\gamma_{ij}`, and the general-element formula `x'=\sum_j x'_j\tau_j` are all present. |
| Mutual determination and final representation claim | PASS | Matrices and transformations are said to determine one another; the matrix ring is identified as isomorphic to `\overline{D}`, hence as a ring-homomorphic image and an `n`th-degree representation of the source ring. |

The two most dangerous semantic errors for this tranche—turning class uniqueness into representative uniqueness, and turning a self-map into a surjectivity assertion—are therefore absent from the production text.

## 3. Terminology and grammar status

The terminology delta contains 14 rows (HG58–HG71). Their statuses remain provisional:

| Status | Rows |
|---|---:|
| `analytic_construction_candidate` | 3 |
| `construction_candidate_scope_locked` | 2 |
| `source_order_candidate` | 1 |
| `construction_candidate` | 4 |
| `construction_candidate_order_locked` | 1 |
| `analytic_carried_candidate` | 1 |
| `construction_test_candidate_not_promoted` | 1 |
| `carried_construction_candidate` | 1 |

The grammar delta contains five rows, all marked `test_only`. No terminology row or grammar rule is presented as native-validated, human-validated, or promoted. The validator records zero human-observation rows and no pilot claim.

## 4. Validator and build reproducibility

Two independent replays were performed in an isolated copy, leaving production files untouched:

1. Running `validate_t004.py` against copied current artifacts returned PASS and regenerated a validation JSON byte-identical to production: SHA-256 `DB28DAD2D9C6C325DE439183A470A78B6C477B3D896E812E7B32E860C424DB43`.
2. A clean two-pass LuaLaTeX build followed by extraction, rendering, and validation also returned PASS. The fresh validation JSON had SHA-256 `8691FD5AA7B8C8A71A3BD1AC1967BA8DEA0E39D0CB448DEBB197D485B8C493D9` because the rebuilt PDF carried a new creation/modification timestamp.

The clean PDF is not bit-for-bit deterministic: production PDF SHA-256 is `3CAC96CD1305D55CBB11ED0AD8E079A62C634D64D08A585B2422AEC6BD3A9905`, while the clean rebuild is `A3148BA0B4D16ADE60278585B94AF38FBA5C8B7BD58BD2672DF3573C9F9C6672`. Both files are 102,624 bytes; `pdfinfo` differs only in `CreationDate`/`ModDate`. The semantically relevant outputs are reproducible:

- extracted text is byte-identical, SHA-256 `C81E8EEA675019BC6125BA3546BA9EB6840B2A859F25DD7578FE686643B91906`;
- page 1 render is byte-identical, SHA-256 `7E6E9456D9AACA6877DBECAA24B5351F3BB01F8BF4D7626B66FDA924AB4CB383`;
- page 2 render is byte-identical, SHA-256 `05C9581D2325D4446C4FF7736F888EE41BBE65E27C53737C89B01FD86C6F86F3`;
- both the production and clean final-pass logs produced zero hits for the warning/error scan.

The current validation JSON's declared hashes were independently recomputed and agree with the current production files. The validator therefore is not merely passing against stale artifact identities.

## 5. Final-pass warning scan

The production final LuaLaTeX log and the clean-build final log were scanned for layout and compilation failures, including overfull/underfull boxes, missing characters, undefined control sequences/references, LaTeX errors, emergency stops, and fatal errors. Result: **0 hits in each final pass**.

Production log identities:

- final TeX log: `C05A9006F3B7DF8C24967523F7EF8765BDBBA9CF02B6663C558EC62C2CD9E375`;
- final console log: `9C91BDEF99A667BD8F4D7D02AC86585DE96BCA826295BF8CE2309C983101537D`;
- pass-1 console log: `9C91BDEF99A667BD8F4D7D02AC86585DE96BCA826295BF8CE2309C983101537D`.

Clean-build log identities before removal of the isolated audit copy:

- final TeX log: `D19F22CBAA9C7D7C6FB5B405FC8E0BC7654EB716401AA26A527E282A62AFA9DC`;
- final console log: `DC00354496327D3B2318589173D0E83856B658B55A6559CE0AE0AF07121C838F`.

## 6. Rendered-page inspection

Both production PNGs were inspected at original detail.

- **Page 1: PASS.** The title, construction-status/source-boundary notice, section heading, numbered statement, prose, and all three formula blocks are legible. Fraktur characters, primes, indices, arrows, and summation notation render correctly. No clipping, overlap, margin escape, missing glyph, or obscured page number was found. Only ordinary line hyphenation is visible.
- **Page 2: PASS.** The continuation heading, editorial scope note, and boundary statement are fully legible. There is no top-edge clipping, overlap, missing glyph, or obscured page number. The large lower-page whitespace is a deliberate consequence of the bounded tranche, not missing content.

Visual inspection establishes render integrity only. It does not establish native linguistic quality or human intelligibility.

## 7. Current production SHA-256 register

| Artifact | SHA-256 |
|---|---|
| Authority `Noether_R823_cum_de.tex` | `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21` |
| `source/R823_HG_T004_de_exact.tex` | `2D757BFD661CE638D41F593DF6636A939AA0042477B6169A38217CAD23FB71BF` |
| `source/R823_HG_T004_de_numbered.txt` | `C97FC627F77DCB0CF6100AFB916AFF7EC056BAF717C33080DB54545DAD5D4B5D` |
| `source/R823_HG_T004_SOURCE_MANIFEST.json` | `8E5354B326F6C6EBE319584BB0C4CDCDA320E22A7B9D9EAED8C40F4DB6D097BE` |
| `semantic/R823_HG_T004_clause_map_seed.csv` | `9D9E890B381FA07A9D87C61DB6CAA0B3926B09C925E69839C85136A24932CD23` |
| `semantic/R823_HG_T004_clause_map.csv` | `14E24A14DE6628D9D0DC3379AD8D774949D10A51F731CF013EECA90F7E11AAD7` |
| `terminology/R823_HG_T004_TERMINOLOGY_v1.csv` | `FAF728886168DDC7713346E7E1B1EA37EA7EE2B57FF7F0E204DD1AD7C48FB00E` |
| `grammar/CONTROLLED_ROMANCE_GRAMMAR_T004_DELTA_v1.csv` | `62737A80381C0328CB3CD14EECCC6EBD03EE9988426D97176709B04335699CFF` |
| `tex/R823_HG_T004_romance.tex` | `92B99FB4F5613E1114E36DCEAA46D02705DBBA8FB76DF960D2DC4706E59C9538` |
| `build/R823_HG_T004_romance.pdf` | `3CAC96CD1305D55CBB11ED0AD8E079A62C634D64D08A585B2422AEC6BD3A9905` |
| `qa/R823_HG_T004_extracted.txt` | `C81E8EEA675019BC6125BA3546BA9EB6840B2A859F25DD7578FE686643B91906` |
| `qa/R823_HG_T004_pdfinfo.txt` | `76F303684C9D50787B4174DB56EC21C879C5F5AE17AC31733FE4663A4144A478` |
| `qa/R823_HG_T004_validation.json` | `DB28DAD2D9C6C325DE439183A470A78B6C477B3D896E812E7B32E860C424DB43` |
| `qa/R823_HG_T004_VISUAL_QA.md` | `F61E6D9AD3B7A1A9F11FB4369349BBD705700E83D6103D4E035E8ECD829468C4` |
| `qa/rendered/R823_HG_T004_page-1.png` | `7E6E9456D9AACA6877DBECAA24B5351F3BB01F8BF4D7626B66FDA924AB4CB383` |
| `qa/rendered/R823_HG_T004_page-2.png` | `05C9581D2325D4446C4FF7736F888EE41BBE65E27C53737C89B01FD86C6F86F3` |
| `scripts/prepare_source.py` | `B7C1BA10481E266EF418ECB5E1088C96407AEAAE05CC10D3EE2425958D2F0615` |
| `scripts/build_t004.ps1` | `452414C1FABD81ADC9525CAA4817337DFDF444A889CC3573328815353B225A99` |
| `scripts/validate_t004.py` | `BDF45EE198C86179AD216B71361F4D840952161935A5C95A189B9B828152E553` |
| `CONTINUATION_CURSOR.md` | `ED745611B61FB830103782DE90251EB26F69C234DB96CE4E1189CD0ECFD3EEA9` |

## 8. Audit conclusion

T004 is complete for this bounded source/semantic/build/visual gate. The clause coverage is complete for authority lines 21117–21146, the dangerous scope and order distinctions are preserved, current hashes are internally consistent, validator PASS is independently reproducible, and both rendered pages pass visual inspection. The only reproducibility qualification is timestamp metadata in a clean LuaLaTeX PDF; text and rendered pages are byte-identical. All controlled-Romance terminology and grammar remain construction/test candidates pending later human review.
