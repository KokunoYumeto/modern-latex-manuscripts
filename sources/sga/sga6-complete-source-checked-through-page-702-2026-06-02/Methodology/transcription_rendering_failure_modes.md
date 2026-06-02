# Transcription/rendering failure modes and fixes

## Failures observed

- OCR flattens or drops arrows in diagrams. Fix: inspect rendered source pages and reproduce diagrams in `tikz-cd`.
- OCR confuses `l` and `ell`. Fix: normalize all l-adic contexts to `\ell`.
- Old drafts condense proofs. Fix: source scans remain authority; drafts are only alignment aids.
- LaTeX may produce a suspicious PDF after a timeout or interrupted run. Fix: check page counts with PyMuPDF and recompile explicitly.
- Long formulas can produce overfull boxes. Fix: use display environments, `aligned`, `tikz-cd`, and `\emergencystretch`.
- Process chatter can leak into reader files. Fix: grep for `TODO`, `placeholder`, `screenshot`, local paths, and continuation language.

## Successful practices

- Stable package layout: `English/`, `French/`, `SourceScan/`, `RenderChecks/`, `CompileLogs/`, `Manifests/`, `Methodology/`.
- Include new-only and cumulative PDFs.
- Include exact source-scan slices and cumulative source scans.
- Keep SHA256 checksums and file lists.
