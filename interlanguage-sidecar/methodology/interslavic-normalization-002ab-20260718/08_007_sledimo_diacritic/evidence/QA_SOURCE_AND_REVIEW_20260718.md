# `sledimo` diacritic correction — evidence and QA

- Canonical Latin Paper 17 section 11 changed once: `sledimo` -> `slědimo`.
- Authority: `isv_words_list.csv` line 14862, headword `slěditi`, sense “follow,” intelligibility `bg+ cs+ hr+ pl+ ru+ sk+ sr+ uk+`; the sentence means “here we follow/proceed a little further.”
- The paired Cyrillic source already has `следимо`; it required no textual edit.
- Build: Latin and Cyrillic both compiled successfully with XeLaTeX/latexmk, producing two 2-page PDFs (4 pages total).
- Logs: no LaTeX/package/missing-character/overfull findings. Existing underfull-box notices (Latin 1; Cyrillic 11) are line-breaking diagnostics in the unchanged layout, not introduced missing content.
- Render/review: all four pages rendered at 120 dpi and individually inspected; no clipping, missing glyphs, corruption, or layout regression.
- Final audit: the remaining five raw `sledi` substrings are embedded in `posledica/posledicami` and are false positives, not instances of the verb.

Limits: reviewed orthographic normalization only; not community certification, independent sentence-level source certification, or unified-v6.2 readiness.
