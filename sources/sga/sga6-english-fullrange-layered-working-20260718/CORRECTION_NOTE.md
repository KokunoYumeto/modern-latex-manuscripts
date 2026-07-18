# Corrective release note

Zenodo version `10.5281/zenodo.21422245` corrects one TeX integration regression
in historical version `10.5281/zenodo.21421931`, under the same permanent SGA
concept DOI `10.5281/zenodo.20410947`.

- Prior reader SHA-256:
  `29CEEA7CE5ECBA9A8C36D34E170D19AAC8C014D64836FEAA77D723CB0F361939`.
- Corrected reader SHA-256:
  `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`.
- Corrected TeX/ledger/render-QA ZIP SHA-256:
  `42B9371BE6A031E459A2F77ED27C56F34A11C1E9BBC7B015DFB6DF2E4236F7E8`.
- Affected location: Lemma 5.8.2, physical PDF page 81.
- Prior behavior: marker 14 appeared, but the note text was lost because the
  footnote insertion was executed inside an `amsmath` display.
- Corrected behavior: marker 14, footnote number 14, and the complete note text
  all render on the page.

No mathematical prose, formula, symbol, authority boundary, or source-status
claim was changed by this correction. The exact sealed-to-final TeX diff and
independent review are in `correction_evidence/`.
