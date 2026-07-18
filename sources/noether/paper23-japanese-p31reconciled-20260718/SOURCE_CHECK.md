# Source check — Japanese Noether Paper 23

## Exact authority and target

- Sealed German P31 SHA-256: `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`.
- German unit: lines `13507–13630`; raw CRLF slice SHA-256 `7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5`; LF-normalized without terminal newline SHA-256 `3EDAFB07A695FEC97AED9C318F2DCB601571D0B9F7D0B7E4DDA7DB554AF74C5A`.
- Semantically attested Japanese TeX SHA-256: `3531549A9E68BD23F07D2C291372933E9ACC9AF0EC93CE8A8ACDC336BA862D0E`; hard mathematics/source defects `0`, semantic defects `0`, terminology/style blockers `0`.
- Final source-reconciled Japanese TeX: `Noether_Paper23_Japanese_SourceReconciled_v001.tex`, SHA-256 `758D36CA12EA463AD4DC23A04536E801FB9A6B190F8E79E87C668EDC15FEC6D9`.
- Exact post-semantic delta: `\tag*`, two nonbreaking phrase boxes, and one minimal `\nolinebreak[4]` kinsoku control. Removing only those four layout controls reproduces semantic SHA `3531549A…62D0E` exactly.

The exact Paper 23 source unit is byte-identical in sealed P31, owner-current whole-file head `BDDEE79A…5895A8F`, and newer unsealed compiled working head `5D159B74…8C7AFD`. Sealed P31 remains the cited authority. The shared R821 pointer is excluded.

## Full structural and formula audit

| Control | Sealed source | Japanese target | Result |
|---|---:|---:|---|
| sections | 6 | 6 | pass |
| logical numbered items | 8 | 8 | pass; source hanging-item topology restored |
| numbered displays | 5 | 5 | pass |
| unnumbered displays | 5 | 5 | pass; inherited split Hilbert display recombined |
| footnotes | 15 | 15 | pass; reset, `)` numbering, order, anchor, and meaning checked |
| semantic emphasis loci | 27 | 27 | pass |
| source small-cap name loci | 48 | 48 | pass; exact 17-name multiset |
| bold section numerals | 6 | 6 | pass |
| primed sums | 3 | 3 | pass; inherited omissions restored |
| literal differential `d` tokens | 34 | 34 | pass; custom `\dd` count is zero |
| `g(y,d y)` loci | 2 | 2 | pass; inherited `\varphi` count is zero |
| delta family | 12 | 12 | pass |
| partial-derivative controls | 31 | 31 | pass |
| Omega family | 8 | 8 | pass |

All ten display objects are individually mapped in `DISPLAY_CORRESPONDENCE.csv`; all fifteen notes are individually mapped in `FOOTNOTE_CORRESPONDENCE.csv`. `STRUCTURAL_INDEX.csv` has 28 unique units covering the article, two apparatus units, introduction, six sections, eight logical numbered items, and ten equation objects. The target retains the source semicolon between the two independent-variable families and the terminal semicolon in the Omega display.

## Material inherited repairs

- Restored the complete repeated title, journal citation, Leipzig lecture/report line, author line, opening footnote group/reset/`)` numbering, received date, group closure, terminal clear page, and final note reset.
- Restored both primed sums in the algebraic form expansion and the primed sum with `j_1,\ldots,j_n` in the differential-form expansion.
- Restored both source `g(y,d y)` loci and removed inherited `\varphi`.
- Replaced all 34 inherited custom `\dd` tokens with the source's literal `d` notation.
- Recombined the two inherited Hilbert equalities into the source's one display.
- Restored the complete source emphasis scopes, including `指数`, both local `上界` spans, the four integer-coefficient spans, `還元できる`, and `接続を基礎に置く`.
- Restored all 48 source `\textsc` name loci and all source-specific hanging numbered items.

## Japanese terminology and adverse evidence

Nineteen explicit terminology rows and twelve adverse/negative-control rows record the Japanese sense windows, excluded senses, evidence locators, competitors, qualitative Mandarin-Simplified dominance risk/debt, provisional lexical-attractor basins, and review status. Six operational decision JSONs validate against `OPERATIONAL_DECISION_INTERFACE.schema.json` Draft 2020-12.

The high-risk distinctions are:

- `endlicher Integritätsbereich` → `有限生成整域`, never a finite-cardinality ring;
- `Integritätsbasis` → `整基底`, here the invariant ring's finite ring-generating set, not a number-field integral basis;
- `(endlichen) algebraischen Zahlkörpern` → `（有限次）代数体`;
- algebraic integrality → `J は J' 上整である`, distinct from section 5 `整数係数性`;
- `kontragredient` → `反傾変換`, while `kogredient zu den d x` is rendered explicitly as `d x と同じ変換則に従う`;
- `Galoissche Resolvente` → `ガロア分解式`, with operator-resolvent senses excluded;
- `Übertragung` / `kovariante Ableitungen` → `接続` / `共変微分`;
- `Lagrangesche Ableitungen` → provisional `ラグランジュの変分導関数`, still held because an exact independent Japanese historical compound was not recovered.

Chinese, Korean, and other CJK evidence do not authorize any Japanese choice. Mandarin-Simplified dominance is a qualitative retrieval-risk control only and is never converted into a readiness scalar.

## Source-defect disposition

The authoritative eight-page P23 audit found zero new German mathematical defects and independently confirmed the corrected `j`-index and `g(y,d y)` reading. Both full source-target QA passes found no German contradiction. Therefore no new duplicate check or route to `4 -nterslav` is due for Paper 23. JA-D025 remains active for any future genuine source defect.

## Final build and render disposition

- Two clean XeLaTeX passes; both final logs SHA-256 `E211ECFFE560CD1BA4147D0846903CC04706C4A310F8CE8832A9772C666C833E` and contain zero warnings, missing characters, over/underfull boxes, undefined controls, or errors.
- Four-page A4 PDF SHA-256 `2D39C6B9D9E81CC38E29A6FB9A354EC489BF13455CC5D96AAF67CAB9FCCEB748`.
- Layout-preserving extraction SHA-256 `974C77BB552A106BDB8AF97C09B13D11189D7FE9CAB7E5A144AC13B0B332444B`.
- Four 200-ppi page PNGs were inspected individually at original detail by the owning lane and an independent read-only reviewer. The accepted render has zero visible defects, exact single labels `(1)`–`(5)`, and clean page boundaries.
- `VISUAL_EVIDENCE_INDEX.jsonl` and its CSV projection contain four schema-valid, hash-valid, structural-ID-resolved `open_payload` records.

Paper 23 is internally complete at decision `JA-D031`. External/community certification, independent Japanese human comprehension, and completion of the full Japanese Noether corpus remain pending.
