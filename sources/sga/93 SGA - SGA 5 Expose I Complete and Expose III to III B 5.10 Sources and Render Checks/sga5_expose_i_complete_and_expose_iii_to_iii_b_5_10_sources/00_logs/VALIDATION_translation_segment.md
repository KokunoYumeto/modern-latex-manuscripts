# Validation -- working draft section

Main PDF: `SGA5_Expose_I_complete_and_Expose_III_to_III_B_5_10_en.pdf`

Build results:

- `pdflatex` pass 1: success.
- `pdflatex` pass 2: success.
- PDF page count: 53.
- Render check: all 53 pages rendered to PNG at 140 DPI.

Visual checks:

- Page 1: title/opening and mathematical notation visible.
- Page 26: Expose I appendix source-fragment note visible and readable.
- Page 35: transition through Expose III cup-products/complements visible and readable.

Known caveats:

- The appendix source material in the supplied SGA5 packet is discontinuous. The translation records this as a source-fragment section.
- The compile log reports one tiny overfull box of 0.1642 pt. It does not create visible clipping in the rendered pages.
