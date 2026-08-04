# Noether Paper 10 — Chinese producer status

## Current state

`translated/built; independent check pending`

The complete Paper 10 current-German slice was translated into editable PRC-oriented Simplified Chinese, assembled, and mechanically compiled. A controlled-generic Hant script artifact was mechanically derived and compiled. Neither PDF was opened, rendered, or visually inspected by this producer. No independent check, approval, archive handoff, publication, or certification has occurred.

Controlling human instruction:

> you do not check - you translate - other sessions CHEWCK

Active lane decisions: `ZH-D112` and `ZH-D113`. SGA remains held and untouched.

## Frozen custody

| Artifact | Bytes | SHA-256 | State |
|---|---:|---|---|
| Current-German Paper 10 slice, lines 7664–7864 | 28,142 | `4EDD9F5B95EE308344B11190088C6D864FB4456AC8AD20E152FA1254E5612234` | Translation authority at claim |
| Inherited Hans slice, lines 7467–7714 | 24,525 | `D74C8B835ADF307AAF4908551BA7C21806DC9772C5A187DD84506F982FAC674C` | Drafting witness only; unaudited |
| Final editable `zh-Hans-CN` TeX | 26,086 | `11C0543B7F90EF8B4E3B52AA727BC85930CDE7D78A0D53DDF3C0B698656C3C1C` | Producer translation; unchecked |
| Final `zh-Hans-CN` PDF | 244,645 | `80B8389139805FD9DB65A40EABB2DEE9704669A4C65FFFA92EA3E187E0201DCC` | Six pages reported by compiler; unviewed |
| Final Hans engine log | 21,151 | `78D7D318690ABC9268AFF1545443695C8ADD5EA12D2F423A70718CB1F687E3BE` | Mechanical build evidence |
| Final editable `zh-Hant-controlled` TeX | 26,428 | `B74A2EB8205168994F182D76A610E6B571A068F02D697E57AB9276439D5851BD` | Generic controlled script; unchecked |
| Final `zh-Hant-controlled` PDF | 254,093 | `239C81C6A6D860E4EC053B7C614C01A7F60105700EC59FE23E5DCAD8CB7868C0` | Six pages reported by compiler; unviewed |
| Final Hant engine log | 21,225 | `F31334F067CD7CDBCAF4EC3EEA952DEF925BB1D7DAC1F9827718A23C68222D3B` | Mechanical build evidence |

Segment outputs are frozen at A `CDB3B17739EFE4D9C41D08E8B642CC1771E842593BDC30E5C7CB2719A2D8A59F`, B `16CA30A47CF25E28038414705157E54112D74D4AAB1E27F9649A44C681426FA6`, and C `67D93BFFA16419E4A3E444C4AB9238B7E2A59E910889710A5BC36D93AA85F686`. Worker returns are frozen at A `0E17810F989496410C4B1A145D3424325009854B504024ED3C66CAC193DB9F25`, B `4CBEEEF476F04E079D0332BB1F155FC11C38CBADE283B9CFA7861BF1F07AC976`, and C `2FDCE8CB9A95CA70B7EA36E8B7BE47148464ACEEE7CE5AEE610DD35027B98020`.

## Adverse build history retained

1. Initial assembled Hans TeX SHA-256 `2955FFE8253E668BD0798A9F177FEF211F802334BC928B78FF4D2D38F471EC24`: pass 1 exited `1` on undefined `\Yreal` after producing an incomplete four-page PDF.
2. After adding only `\providecommand{\Yreal}{\mathfrak Y}`, assembled Hans TeX SHA-256 `77B0519A120CB0B556EA86C7F6BFB98E3EA8E32F2865292E3F060AFF95E8A05B`: pass 1 exited `1` on undefined `\Xreal` after producing an incomplete four-page PDF.
3. After adding only `\providecommand{\Xreal}{\mathfrak X}`, final preamble SHA-256 `E9A056D4020F0827CDBD9FC5C9486534B83DDE4B77C375CD1CE05F30401EC5C0` produced final assembled TeX SHA-256 `11C0543B7F90EF8B4E3B52AA727BC85930CDE7D78A0D53DDF3C0B698656C3C1C`; two final XeLaTeX passes exited `0` and reported six pages.

These macro-only standalone-package repairs are build-custody events, not source or formula checks. The two failed states remain part of the append-only history and are not silently replaced by the final success.

## Explicitly pending outside this producer

- Source and witness comparison; source, semantic, formula, apparatus, terminology, and translation-quality checking.
- Cross-segment terminology and prose harmonization.
- PDF rendering, visual inspection, and layout acceptance.
- Any Taiwan, Hong Kong, or Macao Traditional-Chinese localization. The present Hant artifact is controlled generic only and inherits Hans/PRC wording.
- Human or external validation, approval, registry promotion, archive handoff, publication, or certification.
- Any SGA work.

Producer proposals and adverse readings are exposed in `TRANSLATION_NOTES.md` and `qa/WORKER_RETURNS.md` for the separate checker.

## Routing rule

No producer source defect is claimed. If a separate checker returns a precise Noether source defect: deduplicate it first, then ensure `4 -nterslav` sees the precise checker finding. Undefined standalone macros are packaging events and must not be misreported as source defects.
