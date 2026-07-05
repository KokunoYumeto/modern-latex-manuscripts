# Request: other PC must upload raw source bodies

Date: 2026-07-05

Current local archive sweep fetched `origin/codex/noether-pc-20260629` through
package 619 and the source-canon sufficiency transition rule.

The branch delta from package 566 to package 619 contains 884 files:

- 297 CSV files
- 206 Markdown files
- 181 JSON files
- 171 TXT files
- 24 SHA256 files
- 5 JSONL files
- 0 TeX / LaTeX / BibTeX source-body files
- 0 PDFs
- 0 ZIP/TAR source payloads

This means the GitHub branch currently contains useful coordination, source
canon ledgers, witness tables, translation-choice notes, omission ledgers, and
run logs, but not the actual bulk source corpora needed by downstream Claude,
Web, or Codex sessions.

Action required for the other PC / branch-producing session:

1. Upload actual source-body payloads when found, not only ledgers.
2. Prefer compact ZIPs grouped by lane/language, containing `.tex`, `.ltx`,
   `.bib`, `.bbl`, `.sty`, `.cls`, `.pdf`, and other real source artifacts.
3. Include manifests and SHA256 files, but do not treat those as substitutes
   for the source bodies.
4. Keep generated translations separate from native/source-canon witnesses.
5. If a source body cannot be uploaded, record the concrete reason and the
   local path or upstream URL where it can be recovered.

Boundary: the current branch evidence is valuable, but it is not a raw source
corpus transfer for packages 567-619.
