# Spark prompt: minimal LaTeX compile repair

You are repairing a Ukrainian XeLaTeX technical module after machine translation.

Constraints:

- Make the smallest possible changes.
- Do not delete equations, sections, figures, captions, bibliography calls, or labels to make compilation pass.
- Fix unmatched braces, broken environments, bad Unicode in math mode, missing packages, and obvious command typos.
- If a source macro is missing, add a compatibility macro in the preamble and report it.
- After repair, run `xelatex` twice or `latexmk -xelatex` if available.
- Return a repair report: errors found, changes made, unresolved warnings.
