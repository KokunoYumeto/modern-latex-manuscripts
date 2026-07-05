# UPLOAD ALL LATEX SOURCE BODIES NOW

Date: 2026-07-05

This directive is intentionally duplicated across the repository for cross-session visibility.

Any Codex/AI/session working on the interlanguage, Noether, Slavic, non-Slavic, source-canon, or language-baseline lanes must upload every real source body it finds or generates for every language it touches.

Required upload scope:

- `.tex`, `.ltx`, `.sty`, `.cls`, `.bib`, `.bbl`, `.dtx`, `.ins`, MetaPost, diagrams, and any other TeX-adjacent source files.
- PDFs, ZIPs, TARs, downloaded source archives, and repository snapshots when those are the real provenance carrier.
- Source-canon language baselines, not only generated Noether drafts.
- All active language families and lanes: Slavic, Interslavic, Ukrainian, Russian, Polish, Czech, Slovak, South Slavic, Belarusian, Macedonian, Bulgarian, Slovenian, Croatian/Serbian/Bosnian, Romance, CJK, Arabic/RTL, Persianate/Farsi/Dari/Tajik, Turkic, African/Horn/West, Malay/SEA/Pacific, Indigenous/Creole/Sign, and any other lane touched.

Do not upload only manifests, checksum ledgers, access-boundary notes, omission ledgers, or run logs when source bodies exist. Those are useful, but they are not substitutes for the files downstream sessions need.

If a source file cannot be uploaded, record the exact reason, upstream URL, local path, filename, size, checksum if known, and the next recovery action.

Current finding from local archive sweep:

- `origin/codex/noether-pc-20260629` contains many older TeX payloads, including `noether-slavic-source-canon/20260704/.../latex_payload/...` and some `source_canon_repo_text_probe/...` material.
- Latest packages 620-626 added no `.tex`, `.pdf`, `.zip`, `.bib`, or other source-body payloads.
- Therefore the other PC must continue by uploading the actual source corpora for every lane, not just coordination artifacts.

This instruction is not advisory. The repository/archive maintainer needs the real source bodies on this machine and in GitHub-visible form so Claude/Web/Codex can reuse them without rediscovery.

## Critical clarification

Do not provide an index instead of the corpus. Do not provide a summary instead of the corpus. Do not provide only source-canon tables, hashes, manifests, or URL lists.

Upload the whole corpus as-is: the actual directory trees and all files inside them. If the corpus is large, split it into multiple ZIPs, but keep the original files and directory structure. The archive maintainer needs the real files on this machine, not a description of where they might be.
