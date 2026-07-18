# Paper 43 §§4--7 direct R823 rebuild: parity and smoke evidence

Date: 2026-07-17  
Status: **ready for integration** into the production `N43_fr_body.tex`; that active file was not edited in this task.

## Authority and exact boundaries

Authority:

`authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`

Full-authority SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`

The rebuild starts at R823 line 20416,
`\subsection*{\S{} 4. Differente einer direkten Summe.}`, and ends at line 20964, the `\end{center}` following `Eingegangen 25. Oktober 1949.` It excludes the long 31-section book, whose setup starts after this boundary.

Source-slice hashes below are SHA-256 of UTF-8 text normalized to LF, with one trailing LF:

| Scope | Inclusive R823 lines | Characters | UTF-8 bytes | SHA-256 |
|---|---:|---:|---:|---|
| §4 | 20416--20583 | 12,548 | 12,593 | `68F8373E6145548F83F6B117BD0DF51B73952A38A711FED41C15C28924207370` |
| §5 | 20584--20767 | 16,235 | 16,360 | `50F2EED693372CD61C9096AFADFA9CBF1BAEC7639CA3C70CF2BEF81B45CD53B5` |
| §6 | 20768--20901 | 12,944 | 13,021 | `4BFD333326B7EBD098E213356684F6FC592B5129F71A13B0218A4CC20F15E27F` |
| §7 | 20902--20964 | 4,216 | 4,249 | `6DBC4A52A2362E6790825AD0961235F07D2CF18538CD673F3D68F75C4C436B46` |
| Combined §§4--7 | 20416--20964 | 45,943 | 46,223 | `5F8A557B78D8795B5CBAC6060F9C7D82C7F81456479423E2ADF96DDC1F035445` |

## Target

Direct French fragment:

`working/r823_fr/tex/N43_rebuild_s04_s07_fr.tex`

SHA-256: `47989455C5B46A618C53257A064A0B83B6F647F8976B3A40B0FF159ADBA4651F`  
UTF-8 bytes: 48,984  
Characters: 48,037  
Character ratio, target/source: `1.045578`

The recovered `N43_fr_body.tex` was consulted only as translation memory. The fragment was rebuilt against the R823 slice without condensation. In particular it retains:

- all eleven proof components I--XI in §4;
- every theorem, proof, corollary, remark, special case, supplement, and numbered subpart in §§5--6;
- source notes 14)--21), with their assigned labels and full text;
- the §5 no. 5 manuscript lacuna as an explicit editors' note;
- the centered `À partir d'ici, esquisse.` status marker and the tentative/questioning prose thereafter;
- the closing receipt date.

## Structural and mathematical checks

Counts were made on the exact R823 slice and target with anchored LaTeX-token regexes:

| Token/block | R823 | French |
|---|---:|---:|
| `\subsection*` (§§4--7) | 4 | 4 |
| `\paragraph{...}` | 34 | 34 |
| `\srcfn` | 8 | 8 |
| source-note labels | 14)--21) | 14)--21) |
| `\[...\]` displays | 74 | 74 |
| `equation` environments | 4 | 4 |
| `align` environments | 2 | 2 |
| all display blocks | 80 | 80 |
| `\tag` | 6 | 6 |
| `enumerate` / `\item` | 1 / 3 | 1 / 3 |
| centered status/date blocks | 2 | 2 |

For all 80 display blocks, a sequential comparison removed whitespace and blanked only localized `\text{...}` payloads. Result: **0 differing mathematical display skeletons**. This check caught and removed a temporary continuation-line transcription artifact (`:=` in place of R823's `=`) before the final hash above was frozen.

A scan for unexpected German control prose and for `Ã`, `Â`, `â€`, or U+FFFD found none. The German article title in note 17 and the historical title `Zahlbericht` are intentionally retained bibliographic labels.

## Standalone build and visual smoke QA

Wrapper:

`working/r823_fr/tex/N43_rebuild_s04_s07_smoke.tex`  
SHA-256: `0A3568C6A8FB5784A4D8116B9703D19DCE48DEED6AE2CB69D9E2D7ACE9A75CF2`

Build command, run twice from `working/r823_fr/tex`:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "-output-directory=<workspace>\build\n43_s04_s07_rebuild" N43_rebuild_s04_s07_smoke.tex
```

Outputs:

- `build/n43_s04_s07_rebuild/N43_rebuild_s04_s07_smoke.pdf`
  - 11 A4 pages, 309,513 bytes
  - SHA-256 `C8D7E882BF417507F95B0BE27611F466A64417C1B773F8342896CA67962777FF`
- `build/n43_s04_s07_rebuild/N43_rebuild_s04_s07_smoke.log`
  - SHA-256 `664D6D400C0587FF5E669E98414346218E8F0B9B0548FD07809744E8CB636E64`
  - zero LaTeX/package warnings, overfull/underfull boxes, errors, or fatal stops under the production-like smoke preamble.

All 11 pages were rendered at 120 dpi with Poppler to `tmp/pdfs/n43_s04_s07_rebuild/page-01.png` through `page-11.png` and inspected. No clipping, overlap, malformed accents, mojibake, or displaced footnote blocks were found. The section transitions, note labels 14)--21), manuscript-lacuna note, centered sketch marker, and receipt date are visibly present.

## Integration cursor

Replace the old condensed §4-through-end block in production Paper 43 with the contents of `N43_rebuild_s04_s07_fr.tex`, immediately after the rebuilt §3 and before the long book. Recompile the complete Paper 43/cumulative and rerun the cumulative page-level visual QA; this smoke build proves the fragment itself compiles cleanly but does not substitute for the final integrated build.
