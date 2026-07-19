# Independent review

Final disposition: PASS after one target note-marker repair.

The independent source pass checked corrected French lines 2751--2794,
printed pages 92--93, physical source-PDF pages 81--82, and running pages
73--74. It passed every quantifier and inequality in conditions (a'), (c'),
and (d); all three implication directions; equations (2.5) and (2.6); both
unnumbered displays; the immediate-specialization direction; Lemma 2.5, its
application, and its proof; the corrected line-2792 `Spec` branch; the
mid-line printed-page-93 marker; and continuation cursor 2796.

The first target used an ordinary footnote and therefore rendered source
editor note (6) as automatic footnote 1. This was the sole blocker. The target
now uses the established Exposé VIII marked-note convention. The callout and
footnote both display `(6)`, the automatic `1` is absent, and the French
authority is unchanged. The defect and repair remain visible in the CSV and
JSONL revision evidence.

Reviewed frozen identities:

- TeX: 4,219 bytes, SHA-256
  `ECAAC213067D97BE280748C63BB615AEAB343A9D6337D1AE90934105C3B22E0E`;
- PDF: 309,360 bytes, one A4 page, SHA-256
  `382660FC2890FA311B7DB0C7373440EAD1EBE23BC2FA9BDC98875BA845A9728E`;
- layout extraction: 3,338 bytes, SHA-256
  `2F8367B438F9070B6BFE394E82E5CF3D825163C266F8C540DC9BC6C2DC788CFA`;
- 300-dpi render: 559,524 bytes, SHA-256
  `BA08A647A2651A05177313117291682401150DBDF183B640714A085EE9ACB310`.

A fresh independent two-pass build in a separate temporary directory exited
zero. Its one-page PDF is 309,360 bytes with SHA-256
`77447AC2B1970E06FB32598D90DEE77071F76FBF4883E890055F5F78EA3C2FDF`.
The independent pass-1 and pass-2 logs have SHA-256
`28AE8FFC6E006DDA9C6B6FAACD62D6845FF81F8B438A29494C64A40D79838591`
and `1EADCD628B09619EB11A6CFB6FAFD951A5477E5E82A31E5A4D28910673078669`.
Pass 1 contains only the normal rerun request; stabilized pass 2 has zero
warning, error, overfull-box, or underfull-box hits.

The independent default text extraction is 3,061 bytes, SHA-256
`F2047C2851926A93038C354F1D18FCE77EE015A8E958B1FB4080BF9A76199D74`,
and is byte-identical to the same extraction from the frozen target. The
independent 300-dpi render is byte-identical to the frozen render. The two PDFs
differ in only 64 bytes, all attributable to creation/modification timestamps
and the derived trailer ID.

The jcreinhold snapshot remains comparison-only. Its literal `follows`, added
`trivial`, and misclassified running-page-74 locator were not promoted. This
review seals only the bounded unit; publication, remote archive acceptance,
and public readback remain unclaimed.
