# Noether Paper 41 — mechanical build report

Claim class: **computation and compiler-driven TeX production only**. This is not source, semantic, translation-quality, visual, regional, human, or publication validation.

## Final outputs

Both targets completed two successful XeLaTeX passes using `xelatex -interaction=nonstopmode -halt-on-error`. XeTeX reports version `3.141592653-2.6-0.999998`, MiKTeX `26.5`.

### zh-Hans-CN

- TeX SHA-256: `97142978B30DC21C27D6C30A9CF18C0408F514C08D7A2CEF5649299D3B91E9F0`
- PDF SHA-256: `F7F6A8F50C781A73131E45B09D40EA89E84BAEE179FAE2E9A9BA1DAA9E5426A3`
- Log SHA-256: `157043663AFB5FEB5C662CC6CFA4D67978B4273177FDBB65D63756AB472EF6B7`
- Final transcript: exit code `0`; five pages; one unavailable italic font-shape warning plus the summary substitution warning; no fatal error and no undefined control sequence.

### controlled-generic zh-Hant

- TeX SHA-256: `C5EB70BF90AA824D9B8281BB68780B0BA7269D3A8BCD3CD30A3F1BBEB2AE5F23`
- PDF SHA-256: `209489E484DE479A1646530226AF7DB92A26F0B1D9A575EE928FCE5A39BD4C33`
- Log SHA-256: `935051CA44FB370E92E5C8F8E5EBE294E6F28CC32AD08069B998563496C70D5C`
- Final transcript: exit code `0`; five pages; one unavailable italic font-shape warning plus the summary substitution warning; no fatal error and no undefined control sequence.

The Hant artifact is controlled generic only and is explicitly not `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` localization.

## Compiler-blocking producer markup repairs

The first Hans build stopped at original producer line 38 because `a=b^{1-S}` appeared outside math delimiters. The immediate producer repair put the notation in inline math and rendered the adjacent prose as `$N(a)=1$` and `$a=b^{1-S}$`; it also delimited `$(p)$` in the same line. This is a producer formatting/editorial action and remains independently checkable.

The next build stopped on raw parenthesized TeX math such as `(\mathfrak G)`. The mechanical delimiter formatter changed 329 parenthesized math spans, output SHA-256 `46F63B97E81D770818397DA536D7F0A9802B5FC16440D4E161056ADF18D74EE2`. That first formatter result contained 38 nested inline-math delimiter pairs; a second mechanical pass flattened those 38 pairs, producing final Hans SHA-256 `97142978B30DC21C27D6C30A9CF18C0408F514C08D7A2CEF5649299D3B91E9F0`. No wording was reviewed during the bulk delimiter passes.

- `qa/INLINE_MATH_MARKUP_RECORD.json` SHA-256: `7B855C665512CBACD8DED78E55784C5D493C52840FD409790B6AA05F604A46B8`
- `qa/INLINE_MATH_NESTING_RECORD.json` SHA-256: `56A228BB473AE80DCA6446D773A418F20C187F73F85C0CB7174E501CA0AB963B`
- Formatter scripts SHA-256: `9CB6BF5E50165DB8CFA99C684ABB4947427DC8D236F0A2DD271AD8355EB79F55` and `F80575379EABF0A0BFC8518CBE48CD8F872E956B5FD76092ACF175147F089BD5`.

## Hant production custody

- Producer script SHA-256: `46A39415EBE1E3D85F85E1819791761D2F0F3E17AE01E1B28343A944E70D58CA`
- OpenCC producer record SHA-256: `6E0C16772164A49B1524AAFFC0EE5B912DF6972CE7E9216A9922410C2E74ADC5`
- Converter: `opencc-python-reimplemented` `0.1.7`, configuration `s2t`, followed by the recorded controlled normalizations.

## Required independent work

No PDF pages were rendered or visually inspected by this translation lane. Independent source, semantic, translation, terminology, mathematical, visual, and regional checking remains pending.
