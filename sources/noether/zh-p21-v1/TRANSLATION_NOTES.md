# Noether Paper 21 — Chinese producer translation notes

## Scope and source custody

Complete Paper 21, `Formale Variationsrechnung und Differentialinvarianten`, is the active translation-only producer unit under `ZH-D096`. It was translated from the exact current-German interval at lines 12589–12680, raw UTF-8 bytes `[1001524,1011526)`, 10,002 bytes, SHA-256 `C91672CA4BB8EFEB092EDD278A4F97B6E3E94AE2059144F4FFDDA524AAF7FB96`.

The governing authority is:

- Authority pointer: `C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_P07_CurrentHead_SourceAdjudication_20260722/1/03_audit/NOETHER_CURRENT_AUTHORITY_POINTER_20260722.md`, SHA-256 `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- German whole: `C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_P07_CurrentHead_SourceAdjudication_20260722/1/01_current/Noether_P16_IndependentSecondPass_20260722_cum_de.tex`, SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Local exact snapshot: `source/Noether_Paper21_German_current_exact_CRLF.tex`, 10,002 bytes, SHA-256 `C91672CA4BB8EFEB092EDD278A4F97B6E3E94AE2059144F4FFDDA524AAF7FB96`.

The stale shared R821 pointer was not used.

The inherited cumulative Simplified-Chinese whole has SHA-256 `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`. `ZH-D096` first retained a marker-to-marker calculation for lines 13388–13504, raw bytes `[914741,924127)`, 9,386 bytes, SHA-256 `F708E570AA118F71552B44225ADEF607A90381A425158A312DD2E7251DCE44AE`. Under the append-only refinement `ZH-D097`, lines 13497–13504 were identified by explicit project comments as the next Paper 22 preamble, while line 13496 is the Paper 21 `END` comment. The effective local drafting snapshot therefore uses only Paper 21 content lines 13388–13495, 8,794 bytes, SHA-256 `75DB55DDA93F5C68C833D77C890DA0CAC6E7B22CB0769021799B5CAD335EAE41`, at `witness/Noether_Paper21_SimplifiedChinese_inherited_content_exact_CRLF.tex`.

This boundary refinement concerns witness custody only. It does not change the German authority or establish source fidelity. The inherited Chinese content remained drafting witness material and was not audited or compared as checking evidence. The existing Japanese Paper 21 package was not used as Chinese authority, evidence, or terminology support.

## Source-keyed production segments

The complete German interval was divided into three non-overlapping, source-ordered translation-production segments:

| Segment | German lines | German bytes | German SHA-256 | Witness lines | Witness bytes | Witness SHA-256 | Final Hans segment SHA-256 |
|---|---:|---:|---|---:|---:|---|---|
| A | 12589–12645 | 3,119 | `B6653D3F08C26A60A258BD31C21E8CC7334211D2AA20C2289272BFE49C61ED8F` | 13388–13451 | 2,826 | `C79F6D540EE5274545D580BC4426E18EAE8AFAF2877B26F65B34CDFB4A493D3B` | `6A15D0FF60A90B84545D35EC2A228EA96F9323F3EA1C84C469ABFC6CF8B64984` |
| B | 12646–12667 | 2,547 | `2CC054EA3471A2CA1755BF04B23C2451F708040B9A8F60B3F3B4753E445E26AA` | 13452–13483 | 2,310 | `3D96BDEB519CCEBBED2783C96A785A8095FEDF02322FB306C2979A9A91DE9FB3` | `5507F296C4AE65C5CDCF7CB452B08A5E015579A0FC506B09AF33A99E23F55383` |
| C | 12668–12680 | 4,336 | `CA8F97A2850467896E6ECC5717605B43E22C993B2D6BDB0BD863E915A7CF27FC` | 13484–13495 | 3,658 | `AE26DFF8AC4FAFCBD7DCADA7C6A6FDDA559E9ADBFC3163A54916559A0D350137` | `24AD7EC3BD1AFC99798C341876AC49525F5E44F817554187635B7CC442F7BA76` |

The assembly also used standalone preamble SHA-256 `5F5D7F157A011056E56B1E607EA7A9437D330E15250BD7F6E99DF16F9EE48BBB` and postamble SHA-256 `FEF19CA8785DCCB2AC8196AA06352453104F590D91C8CB59AA378391B023F093`. Assembly record SHA-256 is `22B1F82F9F74E169A2FC81FD5FC1ECF4FAC49F8C7CFD709B1851BDBC8B6ED14C`.

## Producer convergence in segment B

Segment B initially used `组量` for German `Reihen`. During producer assembly it was changed only to `变量组` for internal draft convergence. The initial segment-B SHA-256 was `DE08C37CA9387CD07F43710DED1446F38768ADB640EE3F6F0F28ABFDE79E3679`; the final segment-B SHA-256 is `5507F296C4AE65C5CDCF7CB452B08A5E015579A0FC506B09AF33A99E23F55383`.

This was a producer editorial choice, not an independent terminology decision. Whether `变量组` is the best historical or mathematical rendering remains pending for another session to check.

## Hans producer artifact and mechanical build

- Editable PRC-oriented Hans TeX: `zh-Hans-CN/Noether_Paper21_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex`, 9,793 bytes, SHA-256 `F4BCD4C27ED724EA4D79B1EAC0E427E370E2CB5BA1970200B1FD7A26D58E8235`.
- Mechanically compiled Hans PDF: 188,188 bytes, SHA-256 `A259BBC12868E9560D707CED9DB73E5BB48F77CB41B2688B33CC6CA1748232AB`.
- Final Hans compiler log: 20,705 bytes, SHA-256 `108CFC5514C5218A2A5C32BB175F259D6135954337265E08DDBA9057387F876E`.
- Two XeLaTeX (MiKTeX 26.5) producer passes exited `0`; the final log reports 3 pages.
- Mechanical log scans recorded zero matched error patterns, zero matched LaTeX font-warning lines, zero overfull matches, and zero underfull matches.
- The PDF was not opened, rendered to images, or visually inspected by this producer.

Compilation and pattern counts are mechanical computations only. They do not validate the source, Chinese translation, semantics, formulas, terminology, citations, footnotes, or page appearance.

## Controlled-generic Hant and producer evidence

- Hant TeX/PDF/log SHA-256: `09ECD8499AAF75027554FF51069E4C9D054D2D617A4176307F4E01000A81C9E4` / `66094E493F6A0C94C4A51DAF5785DCBCD91EBA7E5E8212A4C915FD57C5EDB194` / `38DA188AF8953D5220348E8AF1D6A4202681EEE9C9D88E56F8207D88D151BF09`.
- OpenCC/Hant-build record SHA-256: `FE7445CA1D2223DBB22DC77BBBF4FE6AD327EA5725C6B6C7FA56B3BB6967D04A` / `EC812A46AD2FE3A1C173D6F8BC21FA9C627604FB28589B3739565C8A4C47FCDF`.
- Two Hant XeLaTeX engine passes exited `0`, three pages each, with zero matched warning/overfull/underfull lines. Pass 1's wrapper stopped after successful compilation because an over-specific parser expected a byte count; only that parser was broadened before pass 2. Hant TeX was unchanged.
- Controlled Hant is a generic script derivative of the PRC-oriented Hans lexical base and is not Taiwan-, Hong Kong-, or Macao-localized prose.
- Terminology/adverse/CJKV CSVs: 20 rows each, SHA-256 `679184B13B168A580424E2ADF4A6F247A68A3BB92E3FCE0FBF5300697A81FDFF`, `924CFA1EC5E80E0115800F87BF4E65A4FC99E6AACE024FC8CE1E92D36AF990E8`, `00564117245C0D188DF98E01FE9FF15BB0C013F640FA7AE979DF7EE846E0776B`.
- Typed graph: 100 nodes / 100 edges, SHA-256 `D5F863120E65F360A44A1FB95800A800DD74ED6AE2C0171A6B51F389DAA10AA8`.
- Evidence generator SHA-256 `4C909C173FFBBB5F4D3BFCDE85FD984B1B40EA81BC1C37A41BE40D9E58B21CA2`; deterministic rerun stable. Japanese and Korean were unconsulted.

These evidence artifacts record producer sense windows, alternatives, provisional basins, and qualitative Mandarin-Simplified dominance debt. They do not validate correctness or readiness.

## Pending producer stages

- Producer freeze and decision-log append: pending root production.
- Checker handoff and transport: pending root production.
- Independent checking: absent and pending in other sessions.

## Producer/checker boundary

Floris's controlling instruction is: `you do not check - you translate - other sessions CHEWCK`.

This package records translation, assembly, and mechanical compilation only. It claims no source/apparatus collation, source correctness, semantic correctness, formula correctness, terminology correctness, translation-quality review, bibliography or footnote validation, native-reader review, rendered-visual QA, regional localization, approval, publication readiness, archive readiness, or certification. All such checking belongs to other sessions.

No source-defect claim was made by this producer. If an independent checker identifies a precise possible Noether-source defect, the finding must be deduplicated and routed so that `4 -nterslav` sees it; this producer does not adjudicate or duplicate-route it.

SGA remains held pending explicit Floris confirmation. No SGA work is authorized or recorded here.

Decision context: `ZH-D096` records the Paper 21 translation-only claim; `ZH-D097` append-only refines the inherited drafting-witness boundary without changing the German authority.
