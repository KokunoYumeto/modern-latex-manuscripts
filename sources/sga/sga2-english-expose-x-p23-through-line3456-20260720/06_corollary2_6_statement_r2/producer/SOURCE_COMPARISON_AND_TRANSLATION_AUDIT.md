# Source comparison: SGA2-X-COROLLARY2.6-STATEMENT R2 evidence successor

This is a no-overwrite append-only evidence successor. It preserves the
source slice, target TeX/PDF, build logs, extracted text, font table, and
renders byte-for-byte. It corrects only the predecessor's stale claim of 12
font rows: both the producer `PDFFONTS.txt` and the producer machine
validation establish exactly 11. The predecessor audit remains preserved at
SHA-256 `CAACB9F310F341AB009B85696C5ACD4B5617468F61AF02054D9A29E1CC8F1899`;
the independent fail audit remains preserved at SHA-256
`B1EEBE40CDEA502BA019B627CA1D2DDE744B80C08B7D32288646524C0D286BB8`.
This successor is not an independent seal, publication payload, archive
handoff, or volume-completion claim.

## Boundary correction and authority

- The preceding assignment expected a proof of Corollary 2.5 after line
  3444. No such proof exists in the admitted authority: line 3444 closes the
  corollary, line 3445 is blank, and line 3446 begins Corollary 2.6. No proof
  was invented or supplied. A separate evidence-only boundary page records
  that non-production finding.
- This producer unit therefore starts at the next real bounded source unit:
  the complete Corollary 2.6 statement, French lines 3446--3453 inclusive.
  Blank line 3454 is excluded; raw cursor 3454 and next substantive cursor
  3455, the one-line derivation.
- Authority: corrected French arXiv TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Source coordinates: original printed p. 117, physical source-PDF p. 101,
  and recomposed running p. 93. These locator systems are not conflated, and
  no `\pageoriginale` marker occurs within the slice.
- LF/terminal-EOL slice: 517 bytes, SHA-256
  `61B57A0A871EAC4F2D19BFF482133A0F47ECB3DE80CBD877BD05878E9AD38B0E`.
- LF/no-terminal-EOL slice: 516 bytes, SHA-256
  `C55CDDAA41EE8E5556061A322E52ED1100D0D597773CB8F616E9DE3697BC3A26`.
- CRLF/terminal-EOL slice: 525 bytes, SHA-256
  `30C42A525051EAC1C0A66C431C916F44B3100AB6A60EF5E09AEED8955FCE7726`.
- Same-edition physical-p. 101 render: 407,075 bytes, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.

The eight retained lines replay exactly against authority lines 3446--3453.
The same-edition PDF/render establishes manifestation, formula, marker, and
layout only; it is not independent original-print corroboration. No source
defect or unresolved mathematical ambiguity was found, and the French
authority remains byte-identical.

## Translation and mathematical comparison

The first assertion preserves the hypotheses `Lef(X,Y)` and connectedness of
`Y`, universal quantification over open neighborhoods `U`, connectedness of
`U`, and the direction and surjectivity of

`pi_1(Y) -> pi_1(U)`.

The second assertion preserves the additional `Leff(X,Y)` hypothesis, the
natural homomorphism from `pi_1(Y)` to the inverse limit over `U`, and its
isomorphism status. The inverse-limit subscript, both fundamental-group
subscripts, and arrow direction were checked directly against TeX and the
page image.

The parenthetical base-point convention is preserved: a base point is chosen
in `Y` and also used in `X` for defining the fundamental groups. The target
uses US `neighborhood` and the established register `natural homomorphism`,
`surjective`, `inverse limit`, and `isomorphism`.

The source heading carries `\ndemark`, rendered as editorial marker (3) on
the page. The target retains marker (3). Its long editor's note begins at
French line 3456 and is deliberately not imported into this statement-only
unit; line 3455 and line 3456 require separate bounded units.

Rejected choices include reversing either homomorphism, replacing
`surjective` with `injective`, flattening the inverse limit into a single
group, moving the base point from `X` to `U`, dropping marker (3), importing
the editor's note early, conflating the three page systems, or inventing a
proof for Corollary 2.5.

## External comparison candidate

The current jcreinhold chapter
`ii/10-application-to-the-fundamental-group.md` is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its corresponding Corollary 2.6 statement is at lines 256--268. It is one
LLM-generated comparison lineage, not authority or independent
corroboration. It confirms ordinary English register and the direct
Corollary 2.5-to-2.6 adjacency, but its wording and code-block formula were
not reused without direct French, formula, and page replay.

## Build and rendered QA

Two pdfLaTeX passes completed. Pass 1 contains only the expected
`rerunfilecheck` request; pass 2 has zero matched LaTeX/package warnings,
overfull or underfull boxes, undefined controls, emergency stops, or fatal
errors. The target is one A4 page. All 11 font rows are embedded, subsetted,
and Unicode-mapped.

The 150-dpi target and 200-dpi source renders were inspected at original
detail. The authority box, Corollary 2.6 marker (3), both hypotheses,
connectedness assertions, both homomorphisms, inverse-limit subscript,
surjectivity, isomorphism, and base-point convention are legible. There is no
clipping, overlap, broken glyph, black box, or missing text.

- Target TeX: 1,822 bytes, SHA-256
  `C9A674ED0B8D5E7237552AA471DC83E5FF51420389BCD507A580848648DAB927`.
- Target PDF: 191,232 bytes, SHA-256
  `266BD66E2A8464B7E31C533A81887C445950EC831AE09BE6BB991FF8409BA0A1`.
- Pass-1 log: 7,123 bytes, SHA-256
  `5FDCB34DCEC8829733542B2E768A6B8F46BE865631CC106AFD016684803FCF9B`.
- Pass-2 log: 7,003 bytes, SHA-256
  `66D9A8CB45AF0128E132DE5F8CB0A6AC071610060A4EDF7B3D35FF54F7E25A07`.
- Final engine log: 24,002 bytes, SHA-256
  `0CACD7925D53024D5C7742D444B869CF93BE014333E94C97C23717BCA831636C`.
- Target render: 117,486 bytes, SHA-256
  `72975B1C2C209A3140F04FB63B406BF19F96F43201B5C2F31E02B36F293BCA76`.

The R2 evidence successor remains `internal_not_for_release` until its
machine validation and a fresh independent review pass. The build logs and
final engine log contain local runtime paths and must be sanitized or
excluded from any public payload. Continue at raw line 3454 / substantive
line 3455.
