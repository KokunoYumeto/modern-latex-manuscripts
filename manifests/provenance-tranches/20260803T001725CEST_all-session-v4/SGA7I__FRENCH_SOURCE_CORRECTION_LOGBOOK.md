# SGA 7 I French/source-language correction logbook

## 2026-08-02 — layers established

- Frozen input preserved byte-for-byte outside this root.
- Diplomatic and corrected working layers were created from the seven-file frozen source closure.
- Diplomatic baseline reader built to 267 A4 pages before this repair pass.
- The first retrospective repair tranche covers Exposés I and II and is derived only from the lead's already completed direct authority-image comparisons recorded in `LOGBOOK.md`.

## Exposé I transcription repairs — both layers

| ID | Locator | Frozen TeX | Source-established TeX | Disposition |
|---|---|---|---|---|
| SGA7I-FR-I-T001 | 2.4 and following exact sequence | letter-form superscripts `o` | numerical degree `0` in `psi^0` and `phi^0` | applied to both layers |
| SGA7I-FR-I-T002 | 3.1 | `(0.2)` | `(0.0.2)` | applied to both layers |
| SGA7I-FR-I-T003 | 3.1 | `A[1/X]` | `A[1/x]` | applied to both layers |
| SGA7I-FR-I-T004 | 3.3 proof | `X_(x)` | `X_(bar x)` | applied to both layers |
| SGA7I-FR-I-T005 | 3.3 proof | `U_(n_t)` | `U_(eta_t)` | applied to both layers |
| SGA7I-FR-I-T006 | 3.5 proof | `psi_t^o` | `psi_t^0` | applied to both layers |
| SGA7I-FR-I-T007 | 4.5 proof | pseudo-accented `overset(sim)(H)` | reduced cohomology `widetilde H` | applied to both layers |

The previously reported missing bars on `bar j` and `bar x` were already present in the frozen 2026-07-31 source and therefore required no new edit.

## Exposé I corrected readings — corrected layer only

| ID | Locator | Printed/diplomatic reading | Corrected reading |
|---|---|---|---|
| SGA7I-FR-I-C001 | 0.3 | `phi_n(u)` | `phi_n(sigma)` |
| SGA7I-FR-I-C002 | Theorem 1.2 | `(1.1.1)`–`(1.1.5)` | `(0.1.1)`–`(0.1.5)` |
| SGA7I-FR-I-C003 | Variant 1.3 | `GL(H)` kernel | `GL(H_o)` kernel |
| SGA7I-FR-I-C004 | Variant 1.4 | `Gal(n,Q_l)` | `GL(n,Q_l)` |
| SGA7I-FR-I-C005 | 3.3 proof | `m=xd` | `m=nd` |
| SGA7I-FR-I-C006 | Corollary 3.4 | exponent `q'` | exponent `q'+1` |
| SGA7I-FR-I-C007 | Remark 3.6 | `A_eta` | geometric fibre `A_(bar eta)` |
| SGA7I-FR-I-C008 | Remark 3.7 | `Q` | `Q_l` |
| SGA7I-FR-I-C009 | Variant 4.8 | truncated `lieu de non de f` | `lieu de non-lissité de f` |
| SGA7I-FR-I-C010 | Proposition 4.10(b) | two occurrences of `d(g)` | `d(y)` |
| SGA7I-FR-I-C011 | stability condition 5.1(c) | singular point of `C_1` | singular point of the whole curve `C` |
| SGA7I-FR-I-C012 | Proposition 5.1.1 | normalization in `eta` | normalization in `eta'` |
| SGA7I-FR-I-C013 | Proposition 5.1.1 proof | self-intersection `two` | self-intersection `-2` |
| SGA7I-FR-I-C014 | exact sequence 5.2.1 | first connector printed as a rule | required arrow `0 -> pi_1` |
| SGA7I-FR-I-C015 | paragraph before 5.2.3 | exact sequence `(5.2.2)` | exact sequence `(5.2.1)` |
| SGA7I-FR-I-C016 | 5.3.1 descent | indexed target `X_(i bar eta)` | normalization map `X'_(bar eta) -> X_(bar eta)` |
| SGA7I-FR-I-C017 | Theorem 6.1 | `A_eta` | base-changed `A_(eta')` |
| SGA7I-FR-I-C018 | 6.1 notation | concatenated special-fibre subscripts | explicit `(S',s')` subscripts |
| SGA7I-FR-I-C019 | diagram 6.2.1 | unparenthesized quotient tensor | parenthesized quotient before tensor product |
| SGA7I-FR-I-C020 | 6.7 | first `S_i-D` | `S_i-D_i` |
| SGA7I-FR-I-C021 | terminal equality in 6.7 | `T_l(A^(I_i))` | `T_l(A)^(I_i)` |
| SGA7I-FR-I-C022 | bibliography [3] | `irreductibility` | article title `irreducibility` |

## Exposé II corrected readings — corrected layer only

| ID | Locator | Printed/diplomatic reading | Corrected reading |
|---|---|---|---|
| SGA7I-FR-II-C001 | Theorem 2.3.1 | `k=0` | `char k=0` |
| SGA7I-FR-II-C002 | descent reduction | `X' x_X S'` | `X' x_X X'` |
| SGA7I-FR-II-C003 | codimension display | codimension of the open complement | codimension of the finite exceptional set |
| SGA7I-FR-II-C004 | étale-depth display | base `S` | base `P^1` |
| SGA7I-FR-II-C005 | coinvariants | `x^{-1} q x` | `x^{-1} q(x)` |
| SGA7I-FR-II-C006 | isomorphism after (4.7.4) | missing coinvariant subscript | target subscript `K` |
| SGA7I-FR-II-C007 | bibliography [1] | `p=0` | `p != 0` |

## 2026-08-02 — Exposés I–II build checkpoint

- Both full-volume layers compile in three passes to 267 A4 pages.
- Passes 2 and 3 are byte-identical in each layer.
- No TeX errors, fatal diagnostics, missing characters, undefined references, or rerun requests occur. The retained box diagnostics are inherited elsewhere in the full-volume source and are identical across the two layers.
- Diplomatic PDF: `french_source_diplomatic_canon/build_tranche_exposes_I_II_r1/SGA7I_Fresh_Source_Transcription_Complete_Working.pdf`, SHA-256 `593C1C87E494EB56157A2D884506BBEC9E310D68D8B0AC3960B12ABF36F5BB7E`.
- Corrected PDF: `french_source_corrected_workpass/build_tranche_exposes_I_II_r1/SGA7I_Fresh_Source_Transcription_Complete_Working.pdf`, SHA-256 `5D356B9B82AA4087FD3BD107FDA93C48A8175F017293FDD84D086B5B99022418`.
- This is an intermediate source-layer checkpoint, not the final Tome-I French/source-language freeze; Exposés VII–IX remain to receive their recorded retrospective corrections.

## 2026-08-02 — Exposés VII–VIII retrospective propagation

- The direct authority-image decisions already recorded passage by passage in `LOGBOOK.md` were replayed into the two French layers. No new OCR was generated and the frozen 2026-07-31 input remained untouched.
- Exposé VII's scan-established transcription deviations were applied to both layers. Its printed/source-level mathematical and internal-reference defects were emended only in the corrected layer. Exact final TeX identities are:
  - diplomatic: 197,617 bytes, SHA-256 `6AA92125365BDDF05BD26DFAEC14BBF4E370E923DD036BE6FD3D6F6D8E47C2BF`;
  - corrected: 197,716 bytes, SHA-256 `18D8271E8AF4CFFEFEFF8694D7851B40EA74F1988F5700C85277E91059C43BB6`.
- Exposé VIII's two scan-established transcription repairs—the coefficient reading `E_\eta` in (7.3.4.1) and `paraître` in the bibliography—were applied to both layers. The remaining source-established corrections used in the English reader were confined to the corrected layer. Exact final TeX identities are:
  - diplomatic: 230,162 bytes, SHA-256 `233062C9176290927DECB71693A37BB4172A21170AC6640056EC89A1BF2FA451`;
  - corrected: 230,166 bytes, SHA-256 `4D3A57AD5DB09A057FF3525AAD2B7DC924DC63A53D3054E7743C402A88921AC3`.

## 2026-08-02 — Exposé IX deterministic correction replay

- `controls/apply_expose_ix_french_corrections.py` performs literal, count-checked replacements and aborts before writing if any precondition fails. Final script: 13,365 bytes, SHA-256 `D42847A43100B381C4601B26B701A1D9D3FA639E83EB54C22B53A23398EAEC77`.
- The final dry run and application each reported 118 layer operations from 94 recorded dispositions with zero precondition errors. These comprise 24 transcription dispositions applied to both layers and 70 corrected-layer source dispositions. `IX-SRC-019` records a confirmed already-correct identity and intentionally produces no byte change; the other dispositions are material.
- Representative transcription repairs include `t\in S`, `V^\perp`, the prime on `T'_o`, the missing outer parentheses in the Tate-module displays, `\varphi_{y_\lambda}`, and the restored graph branch product `\widetilde C_i\times_C\widetilde C_i`.
- Representative corrected-layer emendations include the reversed inclusion `V^\perp\subset V`, the restored filtration quotients, corrected Ext arguments and section references, `E_\eta`, `T_\ell(P_U)`, the missing tag `(12.3.8)`, the closed `Hom` parenthesis in (12.8.9), `A=A^o`, and projectivity over `\hat{\underline O}`.
- Exact final TeX identities:
  - diplomatic: 448,790 bytes, SHA-256 `415E7013F3F240CE53258C55A992DFE6C8740E3046B04FDDC91FE5EF391A6970`;
  - corrected: 448,908 bytes, SHA-256 `901F132257A8ED6EB55A68CEC622E09F1771D538C2F64B339CDF9996DE8A988F`.

## 2026-08-02 — complete Tome-I French/source-language build freeze

- Two failed invocation-only attempts are preserved in `build_full_tomeI_r1` and `build_full_tomeI_r2`: the first used the wrong engine and the second passed no filename because of PowerShell's reserved `$args` variable. Neither processed the body into a PDF. The current build is the no-overwrite `r3` successor using pdfLaTeX.
- Both complete layers build in three passes to 267 A4 pages. Passes 2 and 3 have byte-identical console output in each layer:
  - diplomatic console SHA-256 `F0A5F28D0A982A0E539475E47EC3EAA53132F3D16E99B83F349F220B3909688F`;
  - corrected console SHA-256 `70A8100303A9F5E436920476AF3CE4527E0C8839600DF0423C51286D36A4E08E`.
- No fatal error, undefined control sequence/reference, missing character, rerun request, multiply-defined label, or duplicate-destination diagnostic occurs. The same 20 inherited box diagnostics remain in each layer and are not correction-specific.
- Current diplomatic reader: `french_source_diplomatic_canon/build_full_tomeI_r3/SGA7I_Fresh_Source_Transcription_Complete_Working.pdf`, 2,002,348 bytes, SHA-256 `11512B3A3DDBF5901447E10DC6ACCF0FFD2634D617348ABC3AC7F1F030383528`.
- Current corrected reader: `french_source_corrected_workpass/build_full_tomeI_r3/SGA7I_Fresh_Source_Transcription_Complete_Working.pdf`, 2,003,271 bytes, SHA-256 `B3D09A409770CD4D3FF6B58EE5870BBFD1B18C01C5E64B084F07A505D77D76EF`.
- Lead visual QA rendered the corrected reader's pages 91, 106, 115–116, 160, 237–238, 253, and 267 at 300 dpi. These cover representative Exposé-VII formulas/diagram and the VII boundary, corrected VIII (7.3.4.1), corrected IX (12.3.3)–(12.3.14) including the restored `(12.3.8)`, the corrected late monodromy formulas, and terminal publisher matter. All inspected pages are legible and structurally sound.
- Literal `CONT` tokens are retained intentionally in both archival French layers where the frozen transcription marks print-page continuations, including split words and intervening footnotes. They are diplomatic page-seam controls, not polished English-reader prose; removing them mechanically would silently alter page-boundary structure.
- `FRENCH_SOURCE_LAYER_IDENTITIES_20260802.csv` contains 19 rows × 5 columns, replays all listed paths/sizes/SHA-256 values with zero errors, has no formula-unsafe cells, and has SHA-256 `9B57A8CB975624A2F8C93EA1ECBA356FBF70822B1055A3F60DF28AE545CCD8CC`.
