# Weber literalness audit - emergency status
This audit was made after the user clarified the required standard: full literal translation, no cliff-notes, no omitted math, no omitted formulae, no explanatory replacement text.
## Finding
The Weber continuation material currently present in this workspace is not safe to treat as a full literal translation. It contains many mathematically useful paraphrases, but the files do not meet the standard of a line-by-line translation preserving all equations, tables, and wording.
## Concrete failure modes
- Some output explicitly substitutes summary/explanation for source text, e.g. phrases such as "The result may be summarized", "In modern language", "Weber records...", and "The important point ... is not the precise exponent".
- Some 50-page PDFs appear to have been page-count padded by large line spacing rather than representing 50 pages of literal translated source.
- The batch-to-source coverage is too broad for the word count in several cases; e.g. 30+ Weber sections reduced to about 10-13k English words is not credible as a complete literal translation.
- Some tables or long formula displays are described rather than reproduced.
- The cumulative PDFs should be marked draft/paraphrase until rebuilt from source.
## Batch metrics
| File | PDF pages | Weber sections | Approx English words | linespread | Suspect phrases found |
|---|---:|---:|---:|---:|---|
| weber_translation_batch13_vol2_sections58_69.tex | 25 | 13 | 9177 |  |  |
| weber_translation_batch14_vol2_sections70_105.tex | 50 | 37 | 13270 | 1.14 | Weber records; may be summarized |
| weber_translation_batch15_vol2_sections106_124.tex | 50 | 20 | 10623 | 1.36 | The full expression is lengthy; we shall not follow; The purpose is only; For brevity |
| weber_translation_batch16_vol2_sections125_154.tex | 53 | 31 | 10662 | 1.34 |  |
| weber_translation_batch17_vol2_sections155_168.tex | 52 | 21 | 9792 | 1.34 | may be summarized |
| weber_translation_batch17_vol2_sections155_174.tex | 52 | 21 | 9794 | 1.34 | may be summarized |
| weber_translation_batch17_vol2_sections155_175.tex | 50 | 22 | 7739 | 1.34 |  |
| weber_translation_batch18_vol2_sections176_192.tex | 51 | 18 | 7305 | 2.10 |  |
| weber_translation_batch18_vol2_sections176_194.tex | 51 | 20 | 7327 | 1.84 | not the precise exponent; In modern language; Weber records |
| weber_translation_batch19_vol2_sections195_206.tex |  | 13 | 4558 | 1.63 |  |
| weber_translation_batch19_vol2_sections195_207.tex | 50 | 14 | 7800 | 2.09 |  |
| weber_translation_batch19_vol2_sections195_207_addenda_I_II.tex |  | 14 | 6467 | 2.45 |  |
| weber_translation_batch19_vol2_sections195_207_and_addenda.tex | 62 | 16 | 9574 | 2.09 |  |
| weber_translation_batch19_vol2_sections195_207_and_supplements.tex | 52 | 16 | 6611 | 2.08 |  |

## Example: batch 18, section 176
Source section 176 contains exact discriminant/norm formulae near the end of the section. The batch 18 English file replaces part of this with the sentence: "The important point for what follows is not the precise exponent..." This is not acceptable under the literal standard.
## Required repair standard
1. Treat all existing Weber continuation PDFs as draft paraphrase unless audited section by section.
2. Restart from the scanned/OCR source at the verified continuation point.
3. For each paper/section: produce a source-faithful German transcription layer when required, and a separate literal English translation layer.
4. Preserve every displayed equation, numbered formula, table, list, figure, and footnote from the authorial text.
5. Do not include publisher title pages, front matter, AI/translators notes, TOCs, or progress chatter in public PDFs.
6. Any uncertain OCR/math must be flagged in a private audit file, not smoothed over in the translation.
7. Page-count targets are subordinate to literalness; do not inflate pages with line spacing.
