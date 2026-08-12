# Quality Rubric

This archive is a working corpus. A public file is useful enough to inspect and improve; it is not automatically a final scholarly edition.

## Critical Edition Rule

No public record in this archive is a critical edition, critically complete edition, or mathematically certified edition unless a future record explicitly says that the user/project maintainer has certified it at that level. Current records should be read as working drafts, source-witnessed tranches, translation drafts, OCR/witness layers, or repair packets according to their status notes.

Words such as `complete`, `source_checked`, `strict`, or `critical` in older filenames can be inherited package names or structural coverage labels. They do not override the record-level caveats. For serious use, verify important formulas, diagrams, tables, theorem statements, cross-references, and unusual notation against the bundled source witnesses.

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
| Source-checked range | More serious use for the declared page/range. | The declaration may be local and may still need mathematical proofreading; adjacent ranges can be weaker. |
| Multilingual working translation | Access where no convenient translation exists, especially for mathematical structure and terminology. | Check the original for important formulas and hard passages. |
| Proofread edition | Citation-level confidence if explicitly declared by the maintainer after source and mathematical review. | Not the default status of current records. |

## Review Levels

| Level | What It Means | What It Does Not Mean |
|---|---|---|
| Preserved | The file is archived and linked so work is not lost. | It may not be clean, complete, or easy to read. |
| Technically openable | Basic tools can open the PDF or ZIP and report plausible structure. | The mathematical content may still be wrong. |
| Readable draft | A human can browse the PDF and see coherent typeset text. | It may still contain OCR errors, formula mistakes, or missing diagrams. |
| Source-check candidate | Source witnesses and TeX/provenance are available for comparison. | It has not necessarily been checked page by page. |
| Source-checked | A contributor has compared the draft against a source witness for a named range. | Other ranges may still be unchecked. |
| Proofread edition | The work has sustained mathematical, typographical, and source review and has been explicitly certified as such. | Most current files are not at this level unless explicitly stated. |

## Dashboard Certification Tiers

For paper-level or page-range dashboards, use short tier labels only when the table also gives the source witness and caveat. These tiers are operational labels, not marketing claims.

| Tier | Meaning | Typical Required Evidence |
|---|---|---|
| Bronze | Compiles or opens, is readable enough to inspect, and has an identified source route. | Reader PDF/TeX plus source identity. |
| Silver | A named paper, page range, or section has been checked against a named source witness. | Page map, source witness, and audit note. |
| Gold | The declared range has formulas, footnotes, tables/diagrams, citations, headings, and boundaries checked. | Apparatus or audit CSV plus render/source checks. |
| Platinum | External review or maintainer certification has promoted the range as proofread or edition-grade. | Reviewer/maintainer note and explicit certification. |

Most current archive material should be described as Bronze, Silver, or untiered support material. Do not infer Gold or Platinum from old filenames containing words such as `complete`, `strict`, `critical`, or `source_checked`.

## Evidence-Level Vocabulary

Some newer audit and workflow notes use an L0-L6 ladder. These labels are operational shorthand and must still be tied to a named source witness, page range, and caveat.

| Level | Meaning | Public Use |
|---|---|---|
| L0 | Source map, page map, or source route only. | Intake/support evidence, not a draft. |
| L1 | Draft TeX compiles or opens but is not source-certain. | Working draft if clearly caveated. |
| L2 | A named page range or paper has been checked against at least one source witness. | Source-checked range, with witness named. |
| L3 | Formula, diagram, table, footnote, bibliography, heading, and boundary checks exist for the declared range. | Strong source-audit tranche, still not a critical edition. |
| L4 | Translation/glossary audit exists against the source branch for the declared range. | Translation-audited range, not proofread unless separately reviewed. |
| L5 | External or maintainer review exists for the declared range. | Review-backed subset; describe reviewer basis. |
| L6 | Benchmark-ready/proofread subset explicitly certified by the maintainer. | Only use when the maintainer explicitly certifies it. |

Do not describe a package as L4/L5/L6 because a sweep found no obvious defect. State the actual basis instead: source-certain patch applied, source-certain no-patch closure, current-base survival check, source-limited best-available closure, needs stronger source, or needs full page-by-page certification.

## Reader, Apparatus, Witness Layers

When packaging serious updates, separate the layers:

| Layer | Purpose |
|---|---|
| Reader | Clean TeX/PDF for reading in the original language or translation. |
| Apparatus | CSV/JSON/Markdown records of corrections, variants, unresolved issues, confidence, source decisions, and no-patch outcomes. |
| Witness | Source scans, page maps, OCR/model witnesses, crop references, hashes, and source-resolution notes. |

OCR, formula-recognition output, and LLM-generated text belong to the witness or candidate layer until source comparison promotes a patch. A "no patch promoted" result is valid and should be recorded rather than forced into the reader.

## Source Resolution And DPI Claims

Source-resolution claims are evidence claims, not decoration. Do not infer optical DPI from a filename, a PDF viewer, a derivative PDF, or generic `72 dpi` image metadata. Use the strongest available evidence and say exactly what it proves:

| Evidence | Public Wording |
|---|---|
| Scandata or source metadata says 600 ppi/dpi and raw page images match that route. | "Source metadata reports 600 ppi/dpi." |
| The raw TIFF/JPEG embeds `600 x 600 PixelsPerInch`. | "Sampled raw image embeds 600 x 600 PixelsPerInch." |
| ImageMagick or another tool reports geometry only, with undefined units. | Give pixel geometry only; do not claim optical DPI. |
| A raw JP2 has high pixel geometry but no embedded resolution units. | "High-resolution raw JP2 witness; no embedded optical DPI claim." |
| A derivative PDF or PNG reports 1000 dpi after rasterization/enlargement. | "1000dpi inspection/render crop," not "native 1000dpi source." |
| A source has `72 dpi` metadata but page geometry clearly came from a scanner/camera workflow. | Treat 72 as coordinate metadata unless independent evidence proves optical DPI. |

When source packages mix routes, state that plainly. For example, a package can be "GDZ600 full pages plus targeted 650dpi crops" or "native400 pages enlarged to 1000dpi inspection crops." Those are useful witnesses, but they do not equal strict native650/1000 source closure. If a page/image-count mismatch exists, such as a JP2 archive with missing or extra numbered leaves, put the mismatch in the public manifest rather than hiding it in scratch notes.

## Audit Claims

The public readability audit checks for configured metadata and filename problems such as stale record IDs, local paths, internal run labels, and rough placeholder wording.

The public PDF surface audit checks that top-level PDFs open and do not trip configured surface defects. It can classify known image-based reference scans as expected.

Neither audit proves mathematical correctness. The strongest review is still source comparison against scans, reference PDFs, or trusted existing TeX, followed by mathematical proofreading of the resulting TeX/PDF. Public completion labels should be revised from exact source/review evidence, not from optimistic filenames or older informal summaries. If an audit finds compression, symbol drift, diagram errors, stale language branches, or incomplete page coverage, the public description should say that plainly in human-facing language.

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
