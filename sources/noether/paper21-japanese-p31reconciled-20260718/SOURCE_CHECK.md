# Source check — Japanese Noether Paper 21

## Exact authority and target

- Sealed German P31 SHA-256: `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`.
- German unit: lines `12583–12674`; raw CRLF slice 10,093 bytes, SHA-256 `21C8472242F1748C64E843DB028441C489D986AC8CA67590D470ABD4318FD8B6`; LF-normalized without terminal newline 10,001 bytes, SHA-256 `BFA5B55C28335C9A2E7078CC7BBEC3EAD9274E3DCCB98ABF2D0B486B1D0BBD85`.
- Independently audited semantic snapshot: TeX SHA-256 `98A820B396E593B13CBFB4333EC7B8265A061FAD439798F14684AF94D679011A`.
- Accepted source-reconciled target: `Noether_Paper21_Japanese_SourceReconciled_v001.tex`, 11,566 bytes, SHA-256 `C8766BF85B516A356649AF5C72CC6B0C09FBDA00078C49DE4E47217907F15F42`.

The final delta from the audited snapshot corrects the `\psi_i` normalization gloss, source-local Vermeil/Noether order, source exclamation, parallel-transport gloss, and checked display punctuation, then adds only minimal Japanese kinsoku controls. An in-memory inverse of exactly that delta reproduces `98A820B3…011A`; no unreviewed post-attestation mutation exists. The shared R821 pointer is excluded.

## Full structural and formula audit

| Control | Sealed source | Japanese target | Result |
|---|---:|---:|---|
| semantic source units | 6 | 6 | pass |
| display objects | 12 | 12 | pass |
| unnumbered displays | 5 | 5 | pass |
| numbered displays | 7 | 7 | pass; tags `(140)`–`(146)` |
| source notes | 14 | 14 | pass; `149)`–`162)` |
| independent external superscript references | 6 | 6 | pass |
| structural records | 26 | 26 | pass; 23 dependencies resolve |
| typed evidence graph | 33 nodes | 33 nodes | pass; all 59 edges resolve |

All display objects are individually mapped in `DISPLAY_CORRESPONDENCE.csv`; every note is mapped in `FOOTNOTE_CORRESPONDENCE.csv`. Title, publication citation, internal item heading, closing date, source group boundaries, clear page, and footnote reset are retained.

## Prime and neighboring-symbol guards

The p. 68 reading is deliberately nonuniform and was checked symbol by symbol:

| Locus | Accepted print/P31 reading | Rejected propagation |
|---|---|---|
| defining homogeneous form | `f'(dx)` | inherited Japanese `f(dx)` |
| adjacent Hessian | `\partial^2 f` | primed Hessian |
| display (140) integrand | `f(x')` | `f'(x')` |
| central identity | `\delta f'-df_\delta` | inherited `\delta f-df_\delta` |
| definition of `f_\delta` | `\partial f/\partial dx_i` | apparent but nonexistent numerator prime |
| following prose | `f` | mechanical prime propagation |

The native 1500×760 crop `tmp/source_inspection/P21_p405_fdelta_numerator_native_crop.png`, SHA-256 `02C6BA1556A8D96B1355D9B1E85AB1E29BC5B3547B1155A7A463D79F050D9CAD`, visibly shows no mark after the numerator `f`. It is diagnostic only, rights-unresolved, and excluded from the open payload.

## Material inherited repairs

- Restored Riemann reference `78)`, the opening and central primes, and Roman `II` in the Heun citation.
- Restored `h^{(1)}(dx,\delta x)`, five linked `\varrho` loci, and the missing Christoffel closing bracket.
- Restored source note scope, continuous `149)`–`162)` marker style, group closure, terminal clear page, and unit-final footnote reset.
- Preserved all twelve display objects, exact formula punctuation, variables, transformation laws, internal references, and six independent superscript references.

## Japanese terminology and adverse evidence

Thirteen terminology rows, eighteen adverse-evidence rows, and seven operational decision JSONs record Japanese sense windows, excluded senses, competitors, evidence locators, qualitative Mandarin-Simplified dominance debt, and provisional lexical-attractor basins. Draft 2020-12 validation with format checking returns zero errors. Four source-defined clusters remain held; transformation laws, covariant derivative, and parallel displacement are internally reviewed for use. External and human-comprehension gates remain pending.

High-risk controls include `反傾` for `kontragredient`, explicit `d`/`dx` と同じ変換則に従う for `kogredient`, `共変微分` only for the connection-dependent derivative, and a first-use statement that `\psi_i` is one half of the displayed Euler–Lagrange left side under the source normalization. Chinese and Korean evidence do not authorize Japanese; Mandarin-Simplified dominance is qualitative debt, never a readiness scalar.

## German-source disposition

No genuine German-source defect survives. Sealed P31 is byte-identical over this unit to the closed 2026-07-17 audited head. Two preliminary prime-family messages were sent to persistent task `shared Noether authority review` during the conflicting pixel reading, then explicitly superseded by a final closure instructing that no German edit be made. The user's duplicate-check-and-route rule remains active for future genuine Noether source defects.

## Final build and render disposition

- Two clean XeLaTeX passes; both final logs are 21,141 bytes and SHA-256 `105819E3AE13C1D549A7AE62F7B50ECA5836F4E0FA4C92EA2D9E3228007B4F06`.
- Three-page A4 PDF: 175,540 bytes, SHA-256 `BC9F967A46E75BC905F2ED2BBA5F12634C1E62E05F5FFF5F6E941BB31D0E524F`.
- Layout-preserving extraction: 12,177 bytes, SHA-256 `336DC8BE58F5C557A97DED513642927E5B7A1FC4770E66B4E3B77D728D79B7DE`.
- Three 200-ppi page PNGs were inspected individually at original detail by the owning lane and an independent read-only reviewer. No clipping, collision, missing glyph, overflow, prohibited line-start small kana, doubled label, or lexical page-boundary split remains.
- `VISUAL_EVIDENCE_INDEX.jsonl` and its CSV projection contain three schema-valid, hash-valid, structural-ID-resolved `open_payload` records.

Paper 21 is internally complete at `JA-D035`. External/community certification, independent Japanese human comprehension, archive publication, and completion of the full Japanese Noether corpus remain pending.
