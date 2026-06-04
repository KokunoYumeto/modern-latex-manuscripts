# Diagram quality audit

Scope: new Paper 081 and carried cumulative D082-D090.

Checks applied:
- clean PDFs are rendered from TeX, not scan crops;
- diagram environments are inventoried in both FR and EN TeX;
- new work uses the standardized lmodern/standard-math format;
- diagram quality is treated as a build criterion: diagrams must be legible, evenly spaced, and must not introduce accidental crossing/diagonal lines.

Result:
- D081 has no graphical diagrams.
- D082-D090 are carried forward with current accepted TeX diagrams; inventory is in `diagram_inventory.csv`.
- For subsequent papers, diagrams should be rebuilt with `tikz-cd` or deliberate `tikzpicture` geometry, with explicit row/column spacing and arrow styles matching the source.

Additional render audit artifacts:
- `QA/diag_contact/` contains compact full-document contact sheets for D081-D090 in both FR and EN. These are included specifically to catch janky diagram geometry, cramped labels, accidental crossing lines, and broken symbols at rendered-PDF level.
