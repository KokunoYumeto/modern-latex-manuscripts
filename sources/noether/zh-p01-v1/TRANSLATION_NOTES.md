# Noether Paper 1 — Chinese producer translation notes

## Scope and producer boundary

This workspace contains the complete numbered Paper 1, *Über die Bildung des Formensystems der ternären biquadratischen Form.*, as a Chinese translation-production unit. It excludes Paper 2. The state recorded here is translation plus mechanical assembly, controlled script transformation, and compilation only.

Floris's controlling instruction remains: `you do not check - you translate - other sessions CHEWCK`.

Accordingly, this producer record does **not** assert source checking, German/scan collation, semantic checking, formula checking, terminology validation, rendered-page inspection, native-reader review, Singapore review, Taiwan/Hong Kong/Macao localization or review, external review, archive acceptance, publication readiness, or certification.

Decision anchors are `ZH-D079` and the corrected custody decision `ZH-D080`. The forthcoming producer-freeze decision is expected to be `ZH-D081`; this document does not itself create that freeze or a checker handoff.

## Exact authority custody

- Current authority pointer: `C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_P07_CurrentHead_SourceAdjudication_20260722/1/03_audit/NOETHER_CURRENT_AUTHORITY_POINTER_20260722.md`.
- Pointer SHA-256: `FAC89D076DCE1C24B534595595B75BA1C88A8956E370EF848B307E731633EED1`.
- Current whole German TeX: `C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_P07_CurrentHead_SourceAdjudication_20260722/1/01_current/Noether_P16_IndependentSecondPass_20260722_cum_de.tex`.
- Whole German SHA-256: `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`.
- Exact Paper 1 interval: whole-source lines 381--460; raw UTF-8 byte interval `[12505,20587)`.
- Local German interval: `source/Noether_Paper01_CurrentGermanAuthority_interval.tex`, 8,082 bytes, SHA-256 `0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F`.
- Custody narrative: `SOURCE_CUSTODY.md`, 2,837 bytes, SHA-256 `8AFE5BC676B48F76EE48F251F8E753B1ADCD6EA2500D1AD4927F4B531DD6F632`.
- Custody record: `qa/SOURCE_CUSTODY_RECORD.json`, 2,447 bytes, SHA-256 `819F9077DCD2F7BF095ED5D76A882EE6488C21D9DEA55DEA6F895CA694246F8C`.

The stale shared `03_projects/noether/00_current_german_authority` R821 pointer was not used.

## Inherited drafting witness

- Whole inherited Simplified-Chinese reader SHA-256: `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`.
- Exact witness interval: cumulative-witness lines 339--466; raw UTF-8 byte interval `[13119,21535)`, including the cumulative file's three-byte BOM in the byte coordinate.
- Local witness: `witness/Noether_Paper01_InheritedSimplifiedChinese_interval.tex`, 8,416 bytes, SHA-256 `566D05E74A03113F77EC75986115F2D7D71914E09B80C96AD5DF537D26F152E3`.
- Role: drafting witness only. It is neither current authority nor completeness or correctness evidence.

## Exact producer segments

The German interval was mechanically divided into three non-overlapping source segments; `qa/SOURCE_SEGMENTATION_RECORD.json` is 1,984 bytes, SHA-256 `896858043709B49C19CE3138D5BFF9F9FC7ABDF37979A7264BAA51D7E042C218`, and records exact concatenation back to the local German interval.

| Segment | Exact local source lines | German source bytes / SHA-256 | Hans producer bytes / SHA-256 |
|---|---:|---|---|
| A | 1--24 | 4,155 / `4FAFC711A18FBE0B9C328DB74E8FB8BD88D46B168F2446B84310222014409AAE` | 3,569 / `9A6C9A0EC1B1A84702749A07DD6BE4783EF25211FA700FD7CDBA67280E3E92E6` |
| B | 25--59 | 2,366 / `52BA4686D0C7DEBF68ECF9D4811971B31DA89E86369EB4DF1C010BFEF5AF67CA` | 1,990 / `0E821D958EDD6B38FC75B8B39E3E3E1B2C53EB33CFB8A24E49E7B01D29917EEE` |
| C | 60--80 | 1,561 / `5642B68567271B6E3236371ECDE02E67C514499AA53EBE728BCCDA47E5D38BF3` | 1,351 / `12569C913673D7DCBDA983D46F197560622A504C2C37757C7A46D9D4E7EE9A39` |

The mechanical Hans assembly record is `qa/HANS_ASSEMBLY_RECORD.json`, 3,783 bytes, SHA-256 `E2D759B3049ECB0464EB5E55C9DCE7006810238888164E4C65C0714AA0B4D278`.

## Producer terminology choices and exposed risks

The following are producer proposals, not checked or externally validated terminology:

- `Formensystem` → `型系统`.
- `ternäre biquadratische Form` → `三元双二次型`.
- `Bildung` in the title → `构成`; plural technical `Bildungen` → `构成式`.
- `Ordnung` → `阶` and `Grad` → `次数`, only within the explicit historical footnote sense window: coefficient dimension versus variable dimension. These forms must not be generalized outside that window without independent review.
- `Invariante`, `Kovariante`, `Kontravariante` → `不变式`, `协变式`, `逆变式`.
- `relativ vollständiges System`, `absolut vollständiges System` → `相对完备系统`, `绝对完备系统`.
- Historical invariant-theory `Modul` → `模`. This is a high-priority collision with modern algebraic `module`; context, not spelling, must carry the distinction.
- First `Überschiebung` → `换位运算（Überschiebung／transvection）`; later short forms remain producer terminology pending specialist review.

Additional producer risks:

- `型`, `型系统`, `构成`, and `构成式` form a dense historical invariant-theory cluster and may not match every modern Chinese specialist convention.
- The segment boundaries can conceal discourse or terminology drift across A/B/C even though mechanical ordering is fixed.
- Preserved structural `\srcspaced` calls around Chinese content may create typographic effects that no rendered-page inspection has assessed.
- Formula and symbolic strings were carried as TeX production content, but no formula comparison or mathematical validation occurred.
- The inherited witness is compressed and historically separate from the current authority; borrowing its diction cannot validate completeness.
- Mandarin-Simplified producer choices dominate the lexical base. This is qualitative evidence debt, never a readiness scalar.

## Hans and controlled-Hant targets

| Target | TeX bytes / SHA-256 | PDF bytes / SHA-256 | Final log bytes / SHA-256 | Compiler-reported pages |
|---|---|---|---|---:|
| `zh-Hans-CN` | 8,237 / `5C9B88F787C447E32B1CFDF6FCFC101A69C0CB87BC7B92F703AFAC9D4C618171` | 181,147 / `0B0EB73647981EB9FFC745C65A9AC29B0B4D1CE03C8F9BEB1D0D2E977E302303` | 20,889 / `F4C78F614B4395B2D0622ECCAB137A93339EDDD3C4AC5548E2834CD58E4758D7` | 2 |
| controlled-generic `zh-Hant` | 8,398 / `3659576C350D38F9CE2B682FB0E011A5547485A62CEEC544BAB3FA997CD0A082` | 188,709 / `838CBA98C6DB190C03522D1B60C39C863C18AF528D59A454984551EAC3CD6F83` | 20,963 / `98A3A99433210D8A1BCEF43342FCA5C6BBDBB8CC30EBEA1C53CA7D1135E4D729` | 2 |

The Hant target was derived mechanically from the Hans producer draft with `opencc-python-reimplemented` 0.1.7, configuration `s2t`, followed by recorded controlled character normalizations. `qa/OPENCC_PRODUCER_RECORD.json` is 3,132 bytes, SHA-256 `E4545BEA9028D74B9496994886ED3A6E5F31C28CD27B15E995DA07447483C1CF`.

Its status is **controlled-generic `zh-Hant` only**. It is explicitly not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO`, and it retains the PRC-oriented Mandarin lexical and syntactic base. No Singapore-specific `zh-Hans-SG` localization is claimed either.

## Mechanical build facts and limits

The producer build operation ran XeLaTeX twice for each final target. The final logs identify XeTeX 3.141592653-2.6-0.999998 / MiKTeX 26.5 and report two pages for each target. Mechanical final-log counts are zero for TeX `!` error lines, ordinary `LaTeX Warning` matches, overfull boxes, underfull boxes, and missing-character matches. Each log contains two `LaTeX Font Warning` matches: the unavailable italic CJK font shape and the summary substitution notice.

No PDF was opened or rendered for this documentation. Successful compilation and clean mechanical counts do not show that the translation, formulas, terminology, pagination, typography, or visual result are correct.

