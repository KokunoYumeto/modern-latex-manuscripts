# Build and visual QA — Japanese Noether Paper 21

## Accepted exact build

- TeX: `Noether_Paper21_Japanese_SourceReconciled_v001.tex`, 11,566 bytes, SHA-256 `C8766BF85B516A356649AF5C72CC6B0C09FBDA00078C49DE4E47217907F15F42`.
- XeLaTeX pass 1 and pass 2 logs: 21,141 bytes each, identical SHA-256 `105819E3AE13C1D549A7AE62F7B50ECA5836F4E0FA4C92EA2D9E3228007B4F06`.
- PDF: `output/pdf/Noether_Paper21_Japanese_SourceReconciled_v001.pdf`, 175,540 bytes, SHA-256 `BC9F967A46E75BC905F2ED2BBA5F12634C1E62E05F5FFF5F6E941BB31D0E524F`.
- Layout-preserving extraction: `output/pdf/Noether_Paper21_Japanese_SourceReconciled_v001.txt`, 12,177 bytes, SHA-256 `336DC8BE58F5C557A97DED513642927E5B7A1FC4770E66B4E3B77D728D79B7DE`.

Both consecutive XeLaTeX builds exited successfully and produced three pages. Final logs have zero LaTeX/package/font warnings, missing-character notices, overfull or underfull boxes, undefined controls, emergency stops, fatal errors, or ordinary TeX errors. The output is an untagged PDF 1.5 with three A4 pages at 595.28 × 841.89 points and rotation 0.

Rendering and metadata inspection used the present native Poppler executables directly because the bundled override command shim pointed to an unavailable runtime path. MiKTeX `pdftotext.exe` produced the extraction. This tooling substitution changes no project content.

## Accepted rendered pages

All pages were rendered at 200 ppi to 1654 × 2339 PNGs and inspected individually at original detail. No contact sheet was created or used.

| Page | PNG SHA-256 | Bytes | Result |
|---:|---|---:|---|
| 1 | `7DCE1B9E70AD3504483E6EC2F52358CE94ECEC3571D9DCB90E9124BAEA8FCFFA` | 456,542 | accepted |
| 2 | `660DD9DFBDF43447E1DBAAF20D66973AB43956C8A925559DC4697923EB4E322E` | 861,907 | accepted |
| 3 | `1169CCECDA64E8CF352B4884A3067DFF8D7BB18AAC45B20722491C20F657784C` | 275,732 | accepted |

Accepted-set total: 1,594,181 bytes. Canonical sorted image-set digest: SHA-256 `CA8A29AF82BB9F043CD3C6BDDC149762DEB96565F6B85E9E790F61AE44CE73A7`.

The owning lane and independent reviewer found no clipping, collision, missing glyph, margin overflow, prohibited line-start small kana, or visible typography defect. Tags `(140)`–`(146)` each render once. Notes `149)`–`162)` are complete. Page joins are clean: page 1 ends after the complete geodesic sentence and page 2 begins with the complete covariant-derivative paragraph; page 2 ends after complete note 155 and page 3 begins with the complete final theorem paragraph. Page 3's larger lower whitespace is normal final-page composition.

Six minimal `ラグランジ\nolinebreak[4]ュ` controls keep `ジュ` joined; one `沿\nolinebreak[4]って` control eliminates the rejected line-start-small-kana defect. The accepted page 3 wrap `ラグ／ランジュ` is permissible because it does not split the small-kana pair.

## Rejected build history

The rejected `tmp/rejected/98A820B3_line_start_small_kana_candidate/` is excluded from the manifest. Its page 2 began a line with `って`, it retained six latent `ラグランジ／ュ` risks, and its semantic snapshot preceded the final normalization/order/punctuation corrections. The first attempt to build that candidate also created a literal generated `$tmp` directory because of a malformed PowerShell output argument; the exact workspace-local directory was verified and removed before the clean builds.

These are Japanese target/build defects. They are not German-source defects and do not trigger routing to `shared Noether authority review`.

## Claims boundary

This is internal source/build/render QA. It is not external/community certification, independent Japanese human-reader signoff, archive publication, or completion of the full Japanese Noether corpus.
