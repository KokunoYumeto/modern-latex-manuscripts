# Independent final audit - SGA2 Expose X line 3542

Verdict: `PASS` for the bounded source-aligned unit. The unit may be treated as
independently sealed by the owning SGA2 lane, subject to its append-only status
and archive-custody procedures. This review itself performs no archive handoff,
shared-log write, French-source mutation, or public release.

## Scope and source control

- Sole editable authority: corrected arXiv French TeX
  `smf_doc-math_4_01.tex`, 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Bounded source: line 3542 only.
- Locators: original printed page 120; same-edition source-PDF physical page
  104; recomposed running page 96.
- Raw continuation cursor: line 3543, which is blank.
- Next substantive cursor: line 3544, the start of Lemma 3.9.
- The authority and producer target remained byte-identical throughout review.

The line is a complete transition sentence with a terminal colon. The target,
`The following lemma is the essential point in the proof of the purity
theorem:`, preserves the forward lemma reference, the importance qualifier,
the proof relationship, the theorem name, and the colon. Rendering
`demonstration` as `proof` is standard mathematical English. No formula,
cross-reference, footnote, or source emendation occurs in the bounded unit.
The jcreinhold e7a259f line is comparison-only and was not used as authority.

## Independent build and render

The exact 1,356-byte producer TeX input (SHA-256
`5B188F1951434DCCF7809CCFFEF0CCD0728231D1B8FD2B145F35471627771A89`)
was copied into an isolated review build directory. Three pdfLaTeX passes all
produced the same 136,849-byte, one-page A4 PDF, SHA-256
`DD4610237E4FE8D0CA8AD026BD24DD2228FCB87317AA4C7716779712BD0C664A`,
which is byte-identical to the producer PDF. No TeX error, warning, overfull
box, or underfull box was found. All five fonts are embedded, subset, and
Unicode-mapped. Fresh extracted text and target/source renders are byte-exact
with the producer evidence and passed original-detail visual inspection.

The bounded PDF is still an internal review artifact: it is untagged and has
no metadata stream. Those publication-structure limitations do not affect the
bounded translation seal, but they preclude presenting this one-page unit as a
standalone publication payload.

## Machine and custody gates

- Producer recursive manifest: 59 rows, 59 unique paths, contiguous ordinals,
  exact file identity closure, canonical CRLF, zero formula-safety hits, all
  rows `internal_not_for_release`.
- Producer machine evidence: 25 CSV rows x 26 columns and 25 JSONL records;
  unique stable IDs, required schema, hierarchy/revision fields, parent and
  reference closure, evidence identity closure, distinct source/target
  locators, and cursor state all pass.
- Independent Artifact Tool replay: 25 data rows x 26 columns, five visually
  inspected panels, zero formula errors, zero formula-safety triggers, and
  unique nonempty primary IDs. Receipt: 1,878 bytes, SHA-256
  `E3DBDC1F84348411B5AB797F6D875E537E22710A313C3D55A332AC6CF905FFCE`.
- The independent review's own stable-ID CSV is separately reloaded through
  Artifact Tool and rendered across the same five A:Z panels after generation;
  its receipt must bind the final CSV identity before manifest closure.
- Rights ledger: six rows; French slices, same-edition reader evidence, and the
  comparison slice remain excluded or rights-gated; every producer row is
  internal and not for release.
- Privacy replay: 48 text files scanned, 17 pattern rows, five distinct
  path-bearing producer files. Those files remain internal and must be excluded
  or sanitized from any later public payload.

Core independent validation completed 61 checks with zero errors. Its receipt
is 27,994 bytes, SHA-256
`D8AD6E10EEADDECEBC6E0553E1B0F4655F4138D525C516FF17869E3F48C929B1`.
The same-edition reader is manifestation and locator evidence only, not an
independent original-print witness. No source defect or ambiguity was found in
line 3542.
