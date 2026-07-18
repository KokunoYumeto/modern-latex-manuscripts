# Visual QA: Noether Paper 4 Introduction successor

The final English PDF contains two A4 pages. Both were rendered at 180 dpi
and inspected in full.

Final canonical hashes:

- TeX: `A86E1A0DA454AFEBED87E68475B88B008D145D3C1BD601ED99397CA13C9D0574`;
- PDF: `31D9FB108121A62174A808F3226F03723C8DF11D1CB7EF2B95A99B9BF2587C2F`;
- page 1: `C3A8758F6B74F23AC5B89CFE5DB819362FD466D3A40DEE0DBF64CED61D900C2A`;
- page 2: `0F96B944BB6B741720EFFCD1B3811F19DC17765E3422B7F0A174DF835DF496FC`.

PASS observations:

- title, byline, source line, editorial disclosure, and Introduction heading
  are legible and correctly separated;
- no clipped, overlapping, missing, or black-box glyphs;
- superscripts, subscripts, Greek rho, section signs, formula references,
  Grassmann-product notation, and dagger note marks render correctly;
- all sixteen page-qualified note calls and note texts are present;
- long labels including `[119:dagger dagger dagger]`,
  `[119:* dagger]`, `[120:***]`, and
  `[121:***]` are legible and unclipped;
- the Postscript begins visibly as a new paragraph on page 2;
- both pages have balanced usable content and visible page numbers;
- the final `higher-grade` wording causes no reflow defect;
- the rejected three-page orphan-line layout is absent.

An independent clean two-pass rebuild returned exit 0 and reproduced both
canonical render hashes. Its extracted text was byte-identical to the
canonical PDF, SHA-256
`073A12E95B9AEB4ECA035EF560A1B9955D78D72AC2E4CD16959AD771BE29400B`.
The rebuilt PDF differed only in creation/modification timestamps and trailer
ID.

The raw canonical MiKTeX log contains local paths and is not eligible for a
public package. This visual pass addresses rendering only; source fidelity is
supported by the separate source review and independent audit.
