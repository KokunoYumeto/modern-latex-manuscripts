# Korean Noether production corpus

This shallow directory is the clean-room Korean production root. It does not inherit approval, checking, or archive claims from older task prose.

## Authority frozen on 2026-08-04

- Current German TeX: `03_projects/noether/08_zenodo/r5/20-de.tex`
- Exact duplicate: `03_projects/noether/07_german_canon_control/candidates/ED0004/noether.tex`
- Bytes: 2,153,575
- SHA-256: `0CB422ECD397DD392A8625297A508DAEE3A5A934EA19EEEF49B47B319EA4F2BB`
- Mechanical XeLaTeX result: 466 pages. This is a build fact, not render or language checking.

The corpus contains 43 numbered Noether papers plus front matter, the separately bound post-numbered lecture *Algebra der hyperkomplexen Größen*, the Kapferer paper with its joint Noether appendix, and terminal bibliography/apparatus. `coverage.csv` records these scopes separately so that P43 is not made to absorb the post-numbered works: P43 is current lines 20177--21004, POST-A is 21005--23741, POST-B is 23742--23983, and BACK is 23984--24146 (the bibliography title begins at 23987). `frozen.csv` freezes the actual recovered files, control files, authority files, and the rejected non-Noether false lead by byte count and SHA-256.

## Recovery result

- Complete inherited Korean bodies reopened against the actual German source and consolidated: P01, P03, P05, P07, P08, P26, P27, P28, P29, P32, P33, P36, P41, P42.
- P18 had only its heading in inherited Korean; its missing ED0004 body has now been translated in this production root.
- P10, P11, P16, and P25 have been translated afresh as complete papers from the current ED0004 body.
- In P28, the inherited unsupported parenthetical modern gloss after `완전가약환` was removed; current German line 14236 contains no such addition.
- Substantial but not yet promoted candidate bodies: P02, P04, P06.
- Partial candidate body: P09, 75 units through old ED0002 line 7328. The P09 German body is byte-identical inside ED0004 apart from a one-line positional shift before the paper; the next untranslated current-authority line is 7330.
- No whole-corpus Korean Noether TeX or PDF was found in the local repository scan.
- The 264,890-byte `unified_master_ko.tex` (SHA-256 `159A51CCE825B07D151867F68F0DCB7B0EC136A938024BA11833387C1F0A18D6`) is unrelated Korean optics/QROP-Net material and is excluded.

These are producer recovery and assembly states only. Independent source, Korean-language, render, and certification work remains outside this task.
