# Source use — Noether Paper 33 Chinese rebase

The controlling source is the sealed P31 cumulative German TeX:

`C:/Users/Floris/Documents/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/cum_de_Local_20260718_P31.tex`

Whole-file SHA-256: `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`.

The ordinary half-open Paper 33 marker interval is P31 bytes `[1476314,1485795)`, physical lines 16235--16308, 9,481 raw bytes with SHA-256 `B46F187B68752277F80C70268F34EDA21534F08CE55A9E85AEE3A7C946E50189`. It is preserved byte-exactly as `source/Noether_Paper33_German_P31_section_interval_exact_CRLF.tex`.

That marker interval is not the semantic article boundary. After Paper 33's `\endgroup` and first `\clearpage`, it carries 20 `\providecommand` declarations, a second `\clearpage`, and Paper 34's footnote reset. The exact logical Paper 33 article, from its section line through the blank line after `\endgroup`, is P31 bytes `[1476314,1485030)`, 8,716 raw bytes, SHA-256 `A61962BD0D031352C9EB06FDD7A39813B49289B8361E22D5082F49B0AB0BD439`. It is the translation/build source; the standalone German control supplies the preceding local footnote reset.

Paper 33 is byte-identical in the later unsealed working candidate. R823 is textually identical after CRLF-to-LF normalization. This comparison does not promote the later candidate or R823 above sealed P31.

The inherited Simplified Chinese reader is a translation witness only. Its complete declared BEGIN/END block has SHA-256 `9D661343AF73F415ACB01685F0B1F14EF682A0F38C9006ED078F94BEF54010B6`; its logical article has SHA-256 `570456F74F69CAD41FC294782CB34FA50F20401C08D28DF0B15BC2D37C8BF042`. A section-to-section extraction that carries Paper 34 setup is retained as adverse evidence, SHA-256 `2A03AECA0B2EC4AE232836F8A413E89D45556E698D7AE47214A221CF6CB13E95`.

`03_projects/noether/00_current_german_authority` remains R821-labelled and is not used as current authority. This is pointer-update debt, not permission to substitute another head.

OCR, extracted text, and the inherited reader are locator/witness material only. SGA is held and untouched.
