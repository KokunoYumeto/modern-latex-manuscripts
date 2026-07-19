# Publication readiness — SGA 2 Exposé V cumulative English checkpoint

Status: **READY FOR PUBLIC CURATOR HANDOFF — independent cumulative package audit passed on 19 July 2026; owner release decision remains pending.** This is not a critical edition, source certification, upload, or authorization to publish.

## Exact scope and cursor

- Complete Exposé V mathematical body from 14 independently source-reviewed and sealed bounded English units.
- Corrected French authority lines 1770–2136; printed-volume pages 60–71.
- Direct-PDF body mapping: physical source-PDF pages 55–63 / recomposed running pages 47–55.
- Context only: physical pages 52–54 / running pages 44–46; the earlier body shorthand using those context pages is rejected in the revision ledger.
- Continuation cursor: corrected French line 2139, where Exposé VI begins; line 2137 is blank and line 2138 is layout control.

## Authority and comparison basis

- Corrected arXiv French TeX: 586,789 bytes, SHA-256 C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042.
- Compiled French source PDF: 1,576,954 bytes, SHA-256 41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90.
- jcreinhold e7a259f Exposé V Markdown, comparison only: 23,145 bytes, SHA-256 5BDB135D6BCE0A601C266648448C899BDD40D8F4038A836AC4830AB70E289E17.

## Exact current artifacts

| Relative path | Role | Bytes | SHA-256 |
|---|---|---:|---|
| SGA2_Expose_V_English_SourceAligned_Cumulative_Checkpoint.tex | editable cumulative English TeX | 29399 | 812BE393E8DEC4BFB57268CCDFE92A233750A7B0E1101DD177FA22FF8CE1E46A |
| SGA2_Expose_V_English_SourceAligned_Cumulative_Checkpoint.pdf | built 9-page reader PDF | 424765 | 4B24E93C39D1B712D0F5B2C66534958AFDC720796A29D6E6D1DE1C1A59083097 |
| INDEPENDENT_PACKAGE_AUDIT_20260719.md | independent package-audit report | 4285 | B435D8023EF4BAB37436EE7E7CFF900A65D6803DBB3A27A31A89536A981D187C |
| ledgers/SOURCE_ALIGNMENT_COVERAGE.csv | source-alignment ledger; 139 records | 111859 | 01F64A91046F4EE6ABF8C6265F8D452227B339EE69A02944E6E081C7F70FB27D |
| ledgers/FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv | formula/symbol/note/structure ledger; 211 records | 174431 | FBF4FA3FA4A63F441C42542518C9073A5AE684F559BD75F7F2C10D1DD4729C88 |
| ledgers/TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv | terminology/adverse-choice ledger; 173 records | 135191 | F4A97E62C308A9848C2BE2339AF840169773F37012A786052AF7ADB2BFE4E361 |
| ledgers/AUTHORITY_ARTIFACT_HASHES.csv | authority/comparison controls; 3 records | 1733 | 33A2AA957822C1B588D99C93E73D9D8F0D7DE17DB38E8D99C2F784EB8B746991 |
| ledgers/COMPONENT_UNIT_INTEGRATION.csv | sealed-component integration ledger; 14 records | 15218 | EAC11C2942128C6806214601CDE51FE116BA5DA6AFADA11A6DA5A12CA056406E |
| ledgers/BUILD_RENDER_EVIDENCE.csv | current build/render evidence ledger; 28 records | 21845 | 96996680303B055ACC8063E2694767BCF8000896714B762010B4BBD13CF56B2F |
| ledgers/INDEPENDENT_PACKAGE_REVIEW.csv | independent package-review ledger; 17 records | 9821 | 33D5D22633947EC25BB564D23D7E5972C3995FA8227D25B652CB2CB52283D1A0 |
| ledgers/STRUCTURAL_INDEX.jsonl | hierarchical structural index; 16 records / 15 stable IDs | 16829 | C10B15870793A575EEBD00461BF2FDFE448043D314737C1CC92B5B77FF0F376E |
| ledgers/DIFFICULTY_REVISION_LEDGER.jsonl | difficulty/revision ledger; 8 records / 4 stable IDs | 7778 | 69DF1C1BF6C921DE891EB0921A1DD4FDB88EB94650B751191E0E095B906C45CE |
| ledgers/MACHINE_READABLE_VALIDATION.json | independent machine-validation receipt | 7611 | A9B75CF92EE856DAE61ACDCB7060842BA61C749B79B9074DC75145577ADF7D8F |
| ledgers/ARTIFACT_TOOL_QA.md | spreadsheet inspection/render receipt | 1817 | 301970DED96200F83E5807A749AA4823253D17F5511A7969D084A6410ECD8C87 |

## Evidence completed

- 14 cumulative mathematical segments and 42 sealed-unit TeX/PDF/review artifacts independently hash-reverified.
- Two successful pdfLaTeX passes; only the benign moved-margin-note warning remains, with page 6 independently inspected.
- Final reader: 9 A4 pages; all 30 reported fonts embedded, subset, and Unicode-mapped.
- Full 180-dpi visual QA: 9 final target pages, 9 Exposé V body source pages, and 3 predecessor-context pages.
- Six cumulative CSV ledgers: 568 records. Independent package-review CSV: 17 records. All pass UTF-8/no-BOM, rectangularity, primary-ID uniqueness, formula safety, complete Artifact Tool inspection, and bounded preview rendering.
- JSONL: 16 structural records / 15 stable IDs and 8 difficulty-revision records / 4 stable IDs; parse, duplicate-key, hierarchy, revision reciprocity, and reference closure pass.
- Recursive checkpoint-text privacy scan: 32 files, 0 private-root, coordination-inbox, or UUID-shaped task-ID hits.

## Caveats and owner decisions

- The PDF has descriptive document-information fields but no XMP metadata stream and is not tagged.
- Underlying French-source rights are not granted by this checkpoint. French source-page renders are local controls and are excluded from the proposed public payload.
- The jcreinhold repository's CC BY 4.0 declaration applies only to that comparison candidate; it does not license the French source or automatically license this new English work.
- Release license, attribution wording, metadata enhancement, and any public GitHub/Zenodo action require the archive owner.

## Archive state and supersession

- Current SGA-general successor surface noted in manager controls: DOI 10.5281/zenodo.21432714. Do not mint a duplicate record.
- No prior public Exposé V checkpoint was discovered. This package supersedes only the internal assembly self-gate closure SGA2-V-CUM-ASSEMBLY-SELF-GATE-20260718.
- No upload was performed. The public archive curator receives this bounded payload proposal and decides publication.
