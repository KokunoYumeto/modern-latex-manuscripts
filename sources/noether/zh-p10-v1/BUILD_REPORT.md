# Noether Paper 10 — producer mechanical build report

## Claim boundary

This report records mechanical assembly, conversion, compilation, hashes, and compiler-reported page/warning counts. It does not claim source, semantic, formula-content, terminology, translation-quality, visual, regional, human, external, archive, publication, or certification validation.

Floris's exact boundary applies:

> you do not check - you translate - other sessions CHEWCK

Neither final PDF was opened, rendered, or visually inspected by this producer. Applicable append-only decision: `ZH-D113`.

## Hans assembly custody

Assembly order was preamble, segments A/B/C, then postamble.

| Input | Bytes | SHA-256 |
|---|---:|---|
| `segments/P10_STANDALONE_PREAMBLE.tex` | 1,580 | `E9A056D4020F0827CDBD9FC5C9486534B83DDE4B77C375CD1CE05F30401EC5C0` |
| `segments/zh-Hans-CN/P10_A_zh-Hans-CN.tex` | 9,275 | `CDB3B17739EFE4D9C41D08E8B642CC1771E842593BDC30E5C7CB2719A2D8A59F` |
| `segments/zh-Hans-CN/P10_B_zh-Hans-CN.tex` | 7,657 | `16CA30A47CF25E28038414705157E54112D74D4AAB1E27F9649A44C681426FA6` |
| `segments/zh-Hans-CN/P10_C_zh-Hans-CN.tex` | 7,559 | `67D93BFFA16419E4A3E444C4AB9238B7E2A59E910889710A5BC36D93AA85F686` |
| `segments/P10_STANDALONE_POSTAMBLE.tex` | 15 | `7C0796754F02F5FEB9AADD6A37D7145D65BD53DDB0779DBA48832B3BBB06FCB2` |

Assembly script SHA-256: `D121C68AAEF2AF9AC4009E6EE24F81B35FE63350F7C17F2552DFBB77DF0A4BA8`. Final assembly-record SHA-256: `2F6AEC122B49B8F82E569C74563C77A6C2F72FAEFAF86E8D43AF73BA2FD7E95F`.

## Append-only Hans macro/build history

| Sequence | Assembled TeX SHA-256 | Pass-1 outcome | Custody consequence |
|---:|---|---|---|
| 1 | `2955FFE8253E668BD0798A9F177FEF211F802334BC928B78FF4D2D38F471EC24` | Exit `1`; undefined `\Yreal`; incomplete four-page PDF written | Failed state retained; no prose/formula/source edit |
| 2 | `77B0519A120CB0B556EA86C7F6BFB98E3EA8E32F2865292E3F060AFF95E8A05B` | Exit `1`; undefined `\Xreal`; incomplete four-page PDF written | Failed state retained; only `\providecommand{\Yreal}{\mathfrak Y}` had been added |
| 3 | `11C0543B7F90EF8B4E3B52AA727BC85930CDE7D78A0D53DDF3C0B698656C3C1C` | Two final passes exited `0`; six pages reported | Final deliverable state after also adding `\providecommand{\Xreal}{\mathfrak X}` |

The final standalone preamble is SHA-256 `E9A056D4020F0827CDBD9FC5C9486534B83DDE4B77C375CD1CE05F30401EC5C0`. The two macro expansions were mechanically taken from the authority preamble (`\Xreal` at line 470 and `\Yreal` at line 471). This was a packaging repair only. The target segments, translated prose, formulas, and authority file were not changed by these repairs. No source defect is inferred.

## Final Hans build

- Compile script: `qa/compile_hans_producer.ps1`, SHA-256 `6AC86652A826BE4BFEDF7273B253CB5FAA7F27B98C70E5743949074811697B0B`.
- Compiler: XeLaTeX; final pass 1 exit `0`; final pass 2 exit `0`.
- Editable TeX: 26,086 bytes; SHA-256 `11C0543B7F90EF8B4E3B52AA727BC85930CDE7D78A0D53DDF3C0B698656C3C1C`.
- PDF: 244,645 bytes; SHA-256 `80B8389139805FD9DB65A40EABB2DEE9704669A4C65FFFA92EA3E187E0201DCC`; compiler log reports six pages.
- Final engine log: 21,151 bytes; SHA-256 `78D7D318690ABC9268AFF1545443695C8ADD5EA12D2F423A70718CB1F687E3BE`.
- Pass-1 and pass-2 captured stdout are each 4,017 bytes and SHA-256 `36364D117873E82B06C303C5000094627258369EF8544BCB13D09D50DA31E7D1`.
- Recorded final log counts: zero error-pattern matches, two warning lines, zero overfull matches, and zero underfull matches. These are mechanical pattern counts, not visual or linguistic findings.
- Mechanical-build record: `qa/HANS_MECHANICAL_BUILD_RECORD.json`, SHA-256 `A86D89AD80F9F16525529D633A4CCBA78E74D83F6349DB20A4B2187BAB488836`.
- Opened/rendered by producer: no.

## Controlled-generic Hant transport

- Conversion script: `qa/build_hant_producer.py`, SHA-256 `E09157C7F612C0A1DA2301140D581148068178E64B65DAAED02ACF9F425324DD`.
- Input Hans TeX: SHA-256 `11C0543B7F90EF8B4E3B52AA727BC85930CDE7D78A0D53DDF3C0B698656C3C1C`.
- OpenCC configuration: `s2t`, `opencc-python-reimplemented` 0.1.7.
- Raw OpenCC output SHA-256: `DC4230627C9900BA962854D242227356B0BFEEBEF031ED3614EAD2B7A694C059`.
- Final controlled-Hant TeX: 26,428 bytes; SHA-256 `B74A2EB8205168994F182D76A610E6B571A068F02D697E57AB9276439D5851BD`.
- Recorded mechanical invariants: 376 protected math spans unchanged; 1,443 TeX control sequences unchanged.
- Recorded controlled normalizations: font-name replacement 2; two producer-marker replacements 1 each; `爲→為` 53, `裏→裡` 8, `羣→群` 1, `衆→眾` 3, `纔→才` 1.
- OpenCC producer record: `qa/OPENCC_PRODUCER_RECORD.json`, SHA-256 `117246875438CFA4046225D6861C5691521CEEA88959F3EB6A17D11214607B45`.

This is controlled generic Hant only. It is explicitly not Taiwan-, Hong Kong-, or Macao-localized prose and inherits the PRC-oriented Hans lexical base.

## Final Hant build

- Compile script: `qa/compile_hant_producer.py`, SHA-256 `5B79B91E2A96A8D99BC3F3E868D2D7E782D2BECE2AFA00F278173105BBAD1261`.
- Compiler: MiKTeX-XeTeX 4.18 (MiKTeX 26.5).
- Pass 1: exit `0`; six pages; stdout SHA-256 `15629E3BE347B923D8FDEBEBAD1D45934985506BFAC18666DDEC3B00E7AD4EA0`; retained engine-log SHA-256 `9D31BC2925E82ED20C8CC3E14B4605EE5DD871A8C0005CD27800DC3DD4C4FDCC`; intermediate PDF SHA-256 `742BE2CC15D22409C7DFC0D95477BCF9B23E9D5E04C7359921874DDDCC84158A`.
- Pass 2: exit `0`; six pages; stdout SHA-256 `3C3F3ADB52576FB9C82498E48626F4D2073A595BBCB2479F073065F4C10C930A`; retained/final engine-log SHA-256 `F31334F067CD7CDBCAF4EC3EEA952DEF925BB1D7DAC1F9827718A23C68222D3B`.
- Final PDF: 254,093 bytes; SHA-256 `239C81C6A6D860E4EC053B7C614C01A7F60105700EC59FE23E5DCAD8CB7868C0`.
- Recorded counts on each pass: two font-warning lines; zero LaTeX/package-warning lines; zero overfull/underfull box lines.
- Hant build record: `qa/HANT_BUILD_RECORD.json`, SHA-256 `7193191A3385456318FA40583C1F173C2846E39319BD7781BCDBDA53553F602A`.
- Opened/rendered by producer: no.

## Required downstream treatment

Both targets remain `independent check pending`. Another session owns every check and visual inspection. If that checker identifies a precise Noether source defect, deduplicate the finding and ensure `4 -nterslav` sees the precise checker finding. Do not classify either undefined standalone macro as a source defect. No SGA action is authorized.
