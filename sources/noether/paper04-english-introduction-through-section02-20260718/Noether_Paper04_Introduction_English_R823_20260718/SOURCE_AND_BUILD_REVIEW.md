# Noether Paper 4 Introduction — source and build review

Scope: R823 lines 3559–3589, comprising title apparatus, the complete
Introduction, and the complete `Nachbemerkung`. The next cursor is
R823 line 3591, section 1.

## Authority and correction

The original 1911 scan, SHA-256
`D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`,
governs printed framing and the opening five pages. R823 routes the editable
German body. The inherited English is comparison evidence only.

The searchable collected-work reproduction, SHA-256
`C7738FDD905B9AE9ACD5904EE07DA24B1262C41456B839947B48213ECB8EA0D7`,
is not the original: it adds collection number 4 and a citation and omits the
original byline. A first frozen package that misdescribed that reproduction
as the original has been put on explicit publication hold. It cannot supply
hashes or readiness evidence for a successor.

## Source review completed

- Original printed pages 118–122 were rendered and inspected in full.
- The journal prints an unnumbered title, a title note, a final title period,
  and `Von Frl. Emmy Noether in Erlangen.`
- The project number 4 and bibliographic line remain only as disclosed
  editorial navigation.
- All sixteen original page-local source-note identities and texts are
  represented by page-qualified target labels: two on p.118, seven on p.119,
  three on p.120, three on p.121, and one on p.122.
- The Study note visibly prints Transactions volume 1. Bibliographic control
  identifies volume 10 (1909), pages 1–49; the target corrects this while
  explicitly disclosing the source reading.
- All prose through the Postscript conclusion, section references 1–9,
  relevant formula references, and symbol families were checked against R823.
- Rows `s` are explicitly described as contragredient to
  `x`. `higher-grade` coheres with `grade 0`
  and avoids the invariant-theory collision of `higher-order`.
- The original p.122 emphasis on Grassmann–Müller and completeness is restored.
  Citation-title typography is otherwise normalized and disclosed rather than
  presented as a diplomatic facsimile.
- The target ends before section 1. The full article continues through R823
  line 4500; physical original page 38 starts Schur and is excluded.

## Build review

- The initial 2.4 cm-margin build produced a nearly empty third page with only
  the final three lines; that layout was rejected.
- The current 2.0 cm-margin source builds to two balanced A4 pages without
  changing translated content.
- Two canonical `pdflatex` passes succeeded.
- PDF metadata has nonblank title, author, subject, and keywords.
- The final log scan reports zero LaTeX/package warnings, overfull or
  underfull boxes, undefined controls, missing-math errors, emergency stops,
  or fatal errors.
- Both pages were rendered at 180 dpi and inspected in full; the complete
  note labels and note texts are legible.

Caveat: this is one bounded machine-assisted source-audited working unit. It
is not complete Paper 4, a critical edition, external peer review,
mathematical certification, community certification, or a rights
determination.
