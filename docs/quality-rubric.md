# Quality Rubric

This archive is a working corpus. A public file is useful enough to inspect and improve; it is not automatically a final scholarly edition.

## Naming Rule

The filename should expose the quality layer. `OCR_candidate`, `formula_witness`, `crop_witness`, and `locator_aid` are checking aids, not editions. `working_draft`, `source_checked`, `reader`, and `cumulative` are reserved for compiled TeX/PDF surfaces with an explicit audit level. When in doubt, choose the lower-confidence name.

The practical distinction is important. OCR converted to TeX is usually not impressive by itself: it is a way to locate text, formulas, and possible omissions. A compiled source-aware working draft or multilingual translation is a different object. It may be genuinely useful for reading and research, provided important equations, tables, diagrams, theorem statements, and unusual terminology are checked against the source before being treated as authoritative.

## File Status Terms

| Term | Meaning |
|---|---|
| Reader PDF | The front-facing PDF to open first. It should be readable and named by author, work, language, or corpus. |
| Modern LaTeX Draft | A typeset draft produced from TeX. It may still need source comparison, formula checks, and layout repair. |
| English Translation Draft | A readable translation draft. It needs checking against the original language before being treated as authoritative. |
| Reference PDF | A source or witness PDF used for checking. Some reference PDFs are image-based scans and may not have useful embedded text. |
| Artifact ZIP | A working bundle containing TeX, source witnesses, component PDFs, OCR text, page images, render logs, and provenance. |
| Public Summary | A compact machine-readable or human-readable status file for a record. |

## Practical Use Levels

| Use Level | Good For | Main Caveat |
|---|---|---|
| OCR/candidate witness | Finding text regions, formula regions, diagram locations, and likely omissions. | Do not cite or rely on it as an edition. |
| Readable working draft | Reading a work in modern TeX form and continuing repair/translation. | May still include OCR mistakes, skipped details, or layout problems. |
| Source-checked range | More serious use for the declared page/range. | The declaration may be local; adjacent ranges can still be weaker. |
| Multilingual working translation | Access where no convenient translation exists, especially for mathematical structure and terminology. | Check the original for important formulas and hard passages. |
| Proofread edition | Citation-level confidence if explicitly declared. | Rare in the current archive. |

## Review Levels

| Level | What It Means | What It Does Not Mean |
|---|---|---|
| Preserved | The file is archived and linked so work is not lost. | It may not be clean, complete, or easy to read. |
| Technically openable | Basic tools can open the PDF or ZIP and report plausible structure. | The mathematical content may still be wrong. |
| Readable draft | A human can browse the PDF and see coherent typeset text. | It may still contain OCR errors, formula mistakes, or missing diagrams. |
| Source-check candidate | Source witnesses and TeX/provenance are available for comparison. | It has not necessarily been checked page by page. |
| Source-checked | A contributor has compared the draft against a source witness for a named range. | Other ranges may still be unchecked. |
| Proofread edition | The work has sustained mathematical, typographical, and source review. | Most current files are not at this level unless explicitly stated. |

## Audit Claims

The public readability audit checks for configured metadata and filename problems such as stale record IDs, local paths, internal run labels, and rough placeholder wording.

The public PDF surface audit checks that top-level PDFs open and do not trip configured surface defects. It can classify known image-based reference scans as expected.

Neither audit proves mathematical correctness. The strongest review is still source comparison against scans, reference PDFs, or trusted existing TeX.

## How To Review A File

1. Open the reader PDF.
2. Find the corresponding TeX or source witness in the artifact ZIP or same Zenodo record.
3. Check page order, section headings, theorem numbering, equation numbering, cross-references, formulas, diagrams, and tables.
4. Report the exact record, file, page or section, source witness, and proposed correction.
5. Keep corrections narrow unless the whole work is being deliberately re-staged.

## Priority Order

1. Availability: do not lose useful work.
2. Public clarity: present the cleanest readable material first.
3. Provenance: keep enough source material to verify and rebuild.
4. Source fidelity: repair content against the original witness.
5. Polish: improve typography, metadata, and repository navigation.
