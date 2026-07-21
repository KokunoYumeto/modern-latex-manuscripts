# Independent final audit PASS — SGA2 Exposé X, Corollary 2.6 statement R2

## Decision

**PASS.** The R2 producer successor correctly resolves the predecessor's sole
blocking evidence defect: the font-table count is 11, not 12. French source,
English target, formulas, build outputs, extracted text, raster, and the font
table are unchanged. The predecessor producer and its evidence-only
independent FAIL remain preserved. This PASS is an internal bounded review;
it is not a publication claim, archive handoff, or whole-exposé/volume seal.

## Exact scope and continuation

- Unit: complete Corollary 2.6 statement, French authority lines 3446–3453.
- Locator systems: printed page 117; physical source-PDF page 101;
  recomposed running page 93.
- Blank line 3454 is excluded. Raw cursor: 3454. Next substantive cursor:
  3455, the one-line derivation.
- Editable target units: 1 TeX file. Built target: 1 PDF page.
- French authority: 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Exact terminal-LF source slice: 517 bytes, SHA-256
  `61B57A0A871EAC4F2D19BFF482133A0F47ECB3DE80CBD877BD05878E9AD38B0E`.

Direct re-reading confirms that line 3444 closes Corollary 2.5, line 3445
is blank, lines 3446–3453 are Corollary 2.6, line 3454 is blank, and line 3455
is the next substantive sentence. No Corollary 2.5 proof exists at this
boundary, and none was invented. No `\pageoriginale` marker occurs in the
slice. The same-edition page image is locator/manifestation evidence only,
not independent original-print corroboration. No source defect or unresolved
mathematical ambiguity was found.

## Source/translation/formula audit

The target preserves marker (3); `Lef(X,Y)` and connectedness of `Y`; every
open neighborhood `U`; the surjection from `pi_1(Y)` to `pi_1(U)`; the
additional `Leff(X,Y)` hypothesis; the natural map from `pi_1(Y)` to the
inverse limit over `U` of `pi_1(U)`; its isomorphism status; and the literal
base-point convention choosing in `Y` and also using the point in `X`.
Directions, endpoints, subscripts, quantification, and mathematical status
all agree with the French TeX and page image. The editorial note body at line
3456 remains deferred.

The jcreinhold e7a259f chapter remains comparison-only. Its ordinary English
register and adjacency are useful; its plain-text Unicode inverse-limit code
block is rejected as reusable formula substrate. French authority controls.

Target identities are unchanged:

- TeX: 1,822 bytes, SHA-256
  `C9A674ED0B8D5E7237552AA471DC83E5FF51420389BCD507A580848648DAB927`;
- frozen producer PDF: 191,232 bytes, one page, SHA-256
  `266BD66E2A8464B7E31C533A81887C445950EC831AE09BE6BB991FF8409BA0A1`.

## Evidence-only successor and predecessor retention

The active audit, active JSONL render record, producer machine validation,
producer `PDFFONTS.txt`, and fresh independent font table all say exactly 11
font rows. All 11 are embedded, subsetted, and Unicode-mapped. Revision 1's
12-row audit/JSONL claim remains visible as history.

The unit, render, and review-defect families have reciprocal
`revision_of`/`supersedes`/`superseded_by` links between revisions 1 and 2.
The R2 target records explicitly state `target_changed=false`.

The 73-row predecessor identity manifest replays without error: 27 producer
files plus 46 prior independent-review files. It retains these exact controls:

- predecessor audit SHA-256
  `CAACB9F310F341AB009B85696C5ACD4B5617468F61AF02054D9A29E1CC8F1899`;
- predecessor JSONL SHA-256
  `E5CF11A0BA63E3658D3CD88107DC820899500A928E747AA5B1B13EFCAD663F39`;
- predecessor independent FAIL audit SHA-256
  `B1EEBE40CDEA502BA019B627CA1D2DDE744B80C08B7D32288646524C0D286BB8`;
- predecessor independent FAIL validation SHA-256
  `B9B0FBCAD774AA9F6E63F7A6CC12AA35A721F1068BF97DC35E5C6481E14B15E6`.

The separate 13-row unchanged-artifact ledger validates byte identity for the
source slice/page render, target TeX/PDF/render/text, build logs, font table,
PDF information, and TeX auxiliaries. Its SHA-256 is
`BB2A4E50F5F195759428472CEC91F02DE54354821C2286AFAD441080FD446B19`.

## Fresh isolated build and render

I copied the target TeX into `rebuild/` and ran three independent pdfLaTeX
passes. Pass 1 has only the expected rerunfilecheck warning; passes 2 and 3
have no warning/error matches. The fresh PDF is 191,232 bytes, SHA-256
`2AA737BB67EB01F0C284E81D27127F363C7207CDD0432913913E1EBB5FCD54FF`.
Its binary hash differs from the frozen producer PDF; `pdfinfo` differences
are confined to creation/modification timestamps, while extracted text,
150-dpi raster, font table, and all normalized non-time metadata are exact.
The raster has SHA-256
`72975B1C2C209A3140F04FB63B406BF19F96F43201B5C2F31E02B36F293BCA76`
and pixel absolute error `0 (0)` against the producer render.

Direct visual review at original detail passed for the source page, producer
target page, fresh target page, all three producer Artifact Tool panels, and
all three independent-evidence panels. Details are in
`INDEPENDENT_VISUAL_QA.md` (4,104 bytes; SHA-256
`3371B85F5BD6407902052978DCBC6A5851F6342A5F689AD19B67078F48BC2727`).

## Machine-readable gates

Independent replay results:

- producer CSV: 18 rows × 22 columns, 11,849 bytes, SHA-256
  `65AA5E44580CCF8F3ECDA9B60880B68794BF9160132A2AE0DD78ECE383A3DD38`;
  rectangular, CRLF-only, formula-safe, schema-valid, ID-unique,
  reference-closed, and supersession-consistent;
- producer JSONL: 18 records, 9,669 bytes, SHA-256
  `5AB290F0E140A53317B0AA0AC7B32EC66924B025C5019D06259ACA43DA6B5B82`;
  duplicate-key-safe parse/schema/ID/reference/supersession closure PASS and
  exact CSV ID parity;
- producer root manifest: ordinal 34 rows × 5 columns, exact identities and
  root-file coverage, SHA-256
  `B87E7DC017458C38C0C68067881E538BF488276F0319105332C9CC7B2ED60B27`;
- predecessor history manifest: ordinal 73 rows × 5 columns, SHA-256
  `21015C8864D04AACECC57AFCCD76A3735B2E58292665FF5CF8165D890C651EF6`;
- unchanged-artifact ledger: ordinal 13 rows × 8 columns, SHA-256
  `BB2A4E50F5F195759428472CEC91F02DE54354821C2286AFAD441080FD446B19`;
- independent review CSV: 18 rows × 25 columns, SHA-256
  `B2CD19090FE6AA83CAAE07D127E5A30A0584E2B91FEDA66FACC9181EBBE35902`;
- independent review JSONL: 18 records, SHA-256
  `D3D19E5DDCE190BBBC984864FB7C66479AE39F2542A7769E4064FE862C43A7A3`.

Artifact Tool 2.8.24 independently replayed the producer 18×22 CSV and the
review 18×25 CSV, with zero formula-error values and zero formula-trigger
values in both. Producer-panel replay is exact outside generated workbook
object IDs. The producer replay receipt SHA-256 is
`BA75A7C708E7A3C0951034160D6D4442D73AB4434B4FEC61167E59A27D48E885`;
the review-ledger receipt SHA-256 is
`6E154E9A00891FED44E20F72B82F893770354C8F48CFD3FBAD93922A487FC582`.

## Privacy and release disposition

The producer root has exactly three disclosed private-path text files:
`BUILD_PASS1.log`, `BUILD_PASS2.log`, and the final TeX engine `.log`. The
independent review has four path-bearing build/engine logs. They must be
sanitized or excluded before any public payload. All current artifacts remain
`internal_not_for_release`.

No producer byte was modified. No archive handoff was made. PASS authorizes
the parent/manager to treat this bounded R2 evidence defect as independently
resolved; it does not itself seal, publish, or upload the unit.
