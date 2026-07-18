# Independent pre-freeze audit — SGA 5 English replacement

Audit completed: 2026-07-18, Europe/Berlin.

## Scope and independence boundary

Two separate read-only model review passes audited the same stable support-tree
snapshot after the production pass stopped editing it. Neither reviewer edited
the snapshot. This is operationally independent package, source-evidence,
privacy, and binary review. It is not independent human scholarly
certification, proof checking, a critical-edition claim, or a rights opinion.

Audited pre-freeze snapshot:

- files: 49;
- bytes: 13,901,515;
- exact snapshot-receipt SHA-256:
  `4F8FFD44993262F3BD7737A933ADBC123EB20104881730FD0D4EFD356C65434D`.

The later addition of this report and the two internal manifests is checked by
an enclosing frozen-payload receipt outside the ZIP. It does not alter the
audited TeX, PDF, logs, ledgers, renders, or publication-control content.

## Source and edition result

- TeX: 798,096 bytes, SHA-256
  `5A79546320606564E0FEF609A13E7F71D42487281325C4CCF97DC20990B7F4C4`.
- PDF: 2,060,055 bytes, 309 pages, SHA-256
  `0455F60C9318F0080A8ACFD4F307849F67E9C321A4C5FB9BB01A21E862721290`.
- PDF is unencrypted, all 309 pages extract without error or empty-page result,
  and Title, Author, Subject, and Keywords metadata are nonblank.
- The printed-p.14 editorial note and printed-p.43 ambiguity disclosure each
  occur exactly once in TeX and extracted PDF text; both focused renders were
  visually clean.
- The exact delta report limits the repaired TeX changes to metadata and those
  two disclosed editorial notes relative to the preserved pre-reopen body.

## Build and ledger result

Both bundled path-sanitized logs are 49,723 bytes with SHA-256
`4842DC57268881939F5565FCB6CC473DEBF4B245C16C500058B4C9CD95192946`.
Each contains 185 `<LOCAL_USER_ROOT>` placeholders and no private user path.
Each reports a 309-page output, zero fatal/undefined/package/pdfTeX errors,
nine disclosed overfull boxes, and zero underfull boxes; three separately
disclosed pre-existing font diagnostics remain outside the edited loci.

The reviewers parsed and reconciled:

- 432 exact formula-candidate rows;
- 432 final-resolution rows with identical unique candidate-ID set;
- 21 additional-repair groups;
- 10 structural-summary rows;
- 34 structural-difference rows;
- 9 representation-review rows;
- 40 terminology/adverse-choice rows;
- 2 reopened source-adjudication rows.

The Exposé-I English-only footnote delta is exactly +2 and is fully accounted
for by the p.14 and p.43 disclosures. The French-control contradiction and
missing local reader evidence are disclosed without adopting an independent
French-completeness certification.

## Render, privacy, and rights result

- Six focused 180-DPI English-reader renders are bundled.
- Sixteen sequential contact sheets cover PDF pages 1-309 without a gap.
- All sixteen contacts are PNG24, 8-bit sRGB and match the row-level
  compatibility-normalization receipt. The four sheets that had appeared
  blank in one viewer were independently opened and found populated.
- All 22 PNGs trace to the current English-reader QA tree. No image is a source
  scan derivative.
- The PDF contains zero embedded raster image objects.
- No private absolute path, user path, task/thread identifier, source scan,
  scan-derived file, French workpass copy, inherited English copy, or external
  English candidate copy is present.
- The rights file accurately states that no rights grant or critical-edition
  certification is established.

## Live-state result

The official Zenodo API independently returned current version
`10.5281/zenodo.21430393`, 17 files, open access, and `cc-zero` record metadata
at 2026-07-18T15:08:02Z. The older SGA 5 English PDF and 149,702,010-byte
scan-bearing support ZIP were unchanged. The bundle correctly treats older DOI
references as historical and `cc-zero` as metadata rather than proof of rights.

Because the concept can advance again, archive maintenance must requery the
official API immediately before any remote action.

## Verdict

**PASS for the exact pre-freeze support snapshot; no actionable finding.** The
support tree may be sealed with payload-scoped manifests and an enclosing ZIP,
provided the final verifier confirms every ZIP member, public-file hash,
exclusion rule, and current live-state reference. This verdict authorizes no
upload by the production task.
