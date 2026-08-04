# Noether P35 independent Chinese checker return

- Return: `ZHCHK-NOETHER-P35-RETURN-001`
- Result: **check complete; producer rebuild and new frozen handoff required**
- Release state: **not accepted** because `ZHCHK-P35-F001` is blocking
- Findings: 14 total — 11 target-translation defects, 2 tooling defects, 1 unresolved advisory; 0 producer defects and 0 checker-confirmed German-source defects
- Producer/German/SGA mutation: none

## Exact findings and corrections

The JSON receipt and append-only finding ledger carry full alternatives, evidence, uncertainty, and latest validation state. Coordinates below refer to the immutable selected German span and frozen producer targets.

| ID | Class / severity | Source coordinate | Target coordinate | Exact correction / disposition |
|---|---|---|---|---|
| `ZHCHK-P35-F001` | `target_translation_defect` / `blocking` | `source/current/Noether_P35_crosshead_LF.tex:1,13,15,23,43,78,80,191,243,250,252` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:47,59,61,69,89,124,126,236,288,295,297` | Use 极大整环 for Maximalbereich throughout (with its denominator-saturation definition at first use); 给定整环 for Z at line 59; 多项式环 at lines 69 and 89; 系数环 at line 236; and 整环/极大整环 in the Russian-summary translation at lines 288, 295, and 297. Retain genuine field terms such as 分式域, 有理数域, 代数闭域, and 系数域 P/Ω. |
| `ZHCHK-P35-F002` | `target_translation_defect` / `major` | `source/current/Noether_P35_crosshead_LF.tex:83,91,214` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:129,137,259` | At first use write 整性基（即有限代数生成组） and thereafter 整性基; line 129 should read ‘以 ... 为整性基（即有限代数生成组）；换言之，...’, line 137 should use 整性基, and line 259 remains 整性基. |
| `ZHCHK-P35-F003` | `target_translation_defect` / `major` | `source/current/Noether_P35_crosshead_LF.tex:87,89,91,157,159,212` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:133,135,137,202,204,257` | Use 代数无关系统 in the argument. At first use preserve the historical wording as ‘代数无关系统（原文称“不可约系统”；见注5）’; revise note 5 to state that the original calls such a system ‘不可约系统’ and that this translation uses 代数无关系统. |
| `ZHCHK-P35-F004` | `target_translation_defect` / `minor` | `source/current/Noether_P35_crosshead_LF.tex:23,30,40,55,61,66,87,89,91,153,229,231` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:69,76,86,101,107,112,133,135,137,198,274,276` | Use 雅可比矩阵 and 雅可比行列式 at all listed loci; the formulas themselves remain unchanged. |
| `ZHCHK-P35-F005` | `target_translation_defect` / `minor` | `source/current/Noether_P35_crosshead_LF.tex:15,19,23,83,89` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:61,65,69,129,135` | Delete the redundant German abbreviations and their nested parentheses; retain the Chinese 即, 或者, 例如, and 模 p. |
| `ZHCHK-P35-F006` | `target_translation_defect` / `major` | `source/current/Noether_P35_crosshead_LF.tex:157` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:202` | Write ‘并且包含于 c_p（即 a_p 是 c_p 的子理想）’ at first occurrence and ‘a_p 作为 c_p 的子理想’ at the second occurrence. |
| `ZHCHK-P35-F007` | `target_translation_defect` / `minor` | `source/current/Noether_P35_crosshead_LF.tex:130` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:175` | Replace ‘包括分数代数数’ with ‘也包括非整代数数’. |
| `ZHCHK-P35-F008` | `target_translation_defect` / `major` | `source/current/Noether_P35_crosshead_LF.tex:188` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:233` | Write ‘使每个 λ_i 均被一个例外素理想整除，但不被该素理想的平方整除，也不被其余例外素理想整除’. |
| `ZHCHK-P35-F009` | `target_translation_defect` / `minor` | `source/current/Noether_P35_crosshead_LF.tex:195` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:240` | Use 生成元: ‘λ_1,...,λ_s 为这些素理想在 R* 中的生成元’. |
| `ZHCHK-P35-F010` | `target_translation_defect` / `minor` | `source/current/Noether_P35_crosshead_LF.tex:153,180,210,221` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:198,225,255,266` | Line 198: ‘（参见注\textsuperscript{6)}）。’; line 225: ‘（见 \S\,3, 2. 的式 (1)），’; line 255: ‘（参见注\textsuperscript{3)}所引札记。）’; line 266: keep the entire substitution/proper-proof/Note-37 passage inside one balanced Chinese parenthesis, ending ‘参见该文注37）。’. |
| `ZHCHK-P35-F011` | `target_translation_defect` / `minor` | `source/current/Noether_P35_crosshead_LF.tex:76,99,110` | `build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex:122,144,155,156,158` | Line 122: start a normal new sentence ‘对于幂级数...’; line 144: ‘在第2点的附加假设下’; lines 155-159: ‘这意味着：’ followed by the display using ‘\hbox{在 }I\hbox{ 中}’ and ‘\hbox{在 }o\hbox{ 中}’. |
| `ZHCHK-P35-F012` | `tooling_defect` / `minor` | `—` | `build/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex:71,126,157` | Normalize 這隻會→這只會 and 幷→並; regenerate from the corrected Hans display so protected math contains 在...中 and no simplified 于. Preserve the explicit generic-Hant/nonregional claim limit. |
| `ZHCHK-P35-F013` | `unresolved_question` / `advisory` | `source/current/Noether_P35_crosshead_LF.tex:153,180,221` | `—` | No correction frozen; remains unresolved. |
| `ZHCHK-P35-F014` | `tooling_defect` / `minor` | `—` | `paper35/candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v001.tex:135,137,139,204,206` | Normalize every controlled-Hant occurrence 代數無關係統→代數無關系統 after OpenCC conversion, while leaving the Hans wording and all mathematics unchanged. |

## Final checker candidates

- Hans TeX: `paper35/candidate/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_checker_candidate_v001.tex` — 31293 bytes, `FD655556DD54B95200BC86B20F64374EC7DAC242A79E9ABB4815E4726F976EB1`
- Hans PDF: `paper35/build/candidate_hans/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_checker_candidate_v001.pdf` — 274157 bytes, `FC96D7A7524248828A12477A1D3AD22BBE1B3EF5386E80BAFBF719CA3AC4E5CD`
- Controlled-generic Hant TeX v002: `paper35/candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v002.tex` — 31555 bytes, `9E4CD793BC691B0B867F13CB9BA60A55A21DCC50ED5CF2D8B88F3CC33A6BEA1A`
- Controlled-generic Hant PDF v002: `paper35/build/candidate_hant_v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v002.pdf` — 306060 bytes, `25199DE577CA31AA995166010B84996566039A1E79EA98C4F33A2E6A82713875`

The Hant artifact is a controlled generic script transform only; it is not Taiwan, Hong Kong, or Macao localization.

## Validation result

All custody assertions passed. All 42 structural units were collated. The symbolic inventory preserves every source formula; structural TeX signatures match. Raw and corrected copies compiled serially in two passes. All pages were freshly rendered, and every raw/final-candidate page was inspected at original detail; producer render pages are byte-identical to their inspected fresh-raw counterparts. PDF text/metadata verification passes.

No German finding packet was frozen or sent. `F013` remains unresolved because the bounded active canon lacks the primary printed pages needed to confirm punctuation. German and SGA remain untouched.
