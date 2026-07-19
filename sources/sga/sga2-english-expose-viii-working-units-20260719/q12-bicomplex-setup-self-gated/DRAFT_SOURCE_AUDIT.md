# Draft source audit - Expose VIII bicomplex setup equations 1.2-1.4

The bounded target translates corrected French lines 2597-2609 only. Direct
comparison against source-PDF physical page 77 confirms recomposed running page
69 and original printed page 87. The printed-page marker for page 88 occurs
only inside excluded line 2611. The next computation begins at that line after
blank line 2610 and is excluded.

The definition of `A^bullet`, both degree conditions, the direction and role of
`a`, all indices and argument nesting in `Q^{p,q}`, the labels (1.2), (1.3),
and (1.4), the first spectral-sequence statement, the underlined functor `F`,
and the complete definitions of `L'^bullet` and `P^bullet` were checked
individually.

French line 2600 contains an explicit correction branch. The current compiled
PDF prints `L^{-q}`; this corrected branch is therefore preserved. The
jcreinhold candidate agrees on the minus sign but remains one comparison-only
LLM lineage. Its `C_A` substitution, flattened functor typography, and code
display are rejected from the source-aligned body; the French `CA` notation is
retained.

The final target uses ordinary visible parentheses in equation (1.2). An
initial build's extensible closing delimiter rendered correctly but produced
one `U+0001` control character in extracted text. Rebuilding with ordinary
parentheses preserved the visible mathematics and eliminated it. The only
remaining control is the normal `U+000C` page break emitted by `pdftotext`.

Independent review confirmed every formula, sign, prime, bullet, argument,
label, page coordinate, and boundary. It also confirmed the automatic equation
counters produce distinct PDF destinations `equation.2`, `equation.3`, and
`equation.4`. The only substantive audit correction was the original printed
page envelope described above; no mathematical-body change was required.

Status: independently source-reviewed and sealed as this bounded unit after a
fresh isolated two-pass build, extraction check, 300/600-dpi source-target
review, and machine-evidence closure. Cumulative integration remains pending.
