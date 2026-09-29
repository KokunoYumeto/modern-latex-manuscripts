# D016 - The constants of functional equations of L-functions

Pierre Deligne, *Modular functions of one variable II*, Lecture Notes in
Mathematics349 (1973), pages501-597. The comparison witness has97physical pages,
including the later note reproduced on its final page.

Reading order: D016_EN.pdf, D016_EN.tex, then the complete source archive.
The French edition is D016_FR.pdf and D016_FR.tex. Both TeX files contain
the complete text, macros and TikZ diagrams; no unpublished chapter or missing
body input is needed.

Source-witness verification and editorial updates in this revision: OpenAI
Codex, GPT-6 Sol, Ultra effort. Earlier work retains its attribution in preserved
provenance. No human review is claimed. The edition distinguishes printed
readings, restorations and mathematical emendations. E01-E59 are editorial notes,
outside the author's text.

The cumulative comparison covers all97pages, the appendix, all20references,
SGA and the later note. Bibliography[12] now retains the printed1958; E59
separates the bibliographic1968 attestation. The original witness is unchanged.
SOURCE/D016_SOURCE_001_097.pdf supplies the full image fallback, kept separate
from the typeset readers.

## Reproduction

Extract into an empty directory. Python3 and a standard pdfLaTeX installation
are prerequisites. Do not enable automatic package installation during checking.
Required packages are fontenc, inputenc, lmodern, amsmath, amssymb, mathtools,
geometry, enumitem, tabularx and tikz-cd. Exact standard classes, styles and TeX
files opened in the reference build are supplied in TEX_DEPENDENCIES, with
portable names and hashes. The installed engine, format and standard fonts remain
runtime prerequisites; this is not a full TeX-distribution dump.

On Windows, run `python rebuild.py`. The script acquires the single
Global\InterlanguageTeXSlotV1 mutex with one30-second timeout, and uses a captured
job with a1GiB aggregate limit. It never touches another process. It creates only
rebuild/ in the extracted directory, runs three passes per language, checks logs,
convergence and exact target PDF hashes. Internal job names Deligne_FR.tex and
Deligne_EN.tex are needed for exact PDF identity; their source bytes equal the
direct D016 files. An occupied mutex produces one bounded failure, with no
repeated waiting or TeX process launched.

The reference toolchain is MiKTeX26.5, pdfTeX1.40.29, LaTeX2025-11-01,
SOURCE_DATE_EPOCH=946684800 and UTC. MANIFEST.json binds every member's portable
name, size and SHA256. AUDIT holds choices and checks, not a replacement for
editable text. Historical checks retain their exact scope. Local packet success
does not assert publication of a new cumulative corpus version.
