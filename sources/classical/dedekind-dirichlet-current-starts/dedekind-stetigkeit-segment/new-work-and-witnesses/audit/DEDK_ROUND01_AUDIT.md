# Dedekind Round 01 Audit Note

## Source and scope

This round works only on Dedekind, Band III, work L, `Stetigkeit und irrationale Zahlen`. The source base is the original scan included in the Dedekind/Dirichlet starter packet, not the previously generated public reader. The work produced here covers printed pages 315--328, corresponding to PDF pages 319--332 in the source scan.

## Output standard used

The output follows the packet's required structure: editable German source TeX, editable English translation TeX, rendered PDFs, a source scan slice, a cumulative folder, a manifest, and an explicit status note.

## Completion claim

`Complete for declared range` means that the title, dedication, contents fragment, preface, §§1--4 prose, footnotes, numbered roman lists, inequalities, cut notation, and formulas in the declared printed page range are present in editable TeX and render in the two PDFs. It does not claim completion of the entire work L.

## Editorial / fidelity notes

- The starter packet's fidelity audit already reported systematic `ß -> SS` rendering damage in the existing public readers. The new TeX avoids that failure by using normal UTF-8 plus T1 font encoding.
- The source scan OCR contains occasional recognition errors (`Bedekind`, `Grelles Journal`, spacing in names). These were corrected where the correction is clear. Ambiguous proper-name orthography is flagged in `status.md`.
- The irrational-square example in §4 is set as Dedekind's construction: positive non-square integer `D`, integer `\lambda` with `\lambda^2 < D < (\lambda+1)^2`, cut defined by whether rational squares are below or above `D`, descent contradiction using `t^2-Du^2=0`, and the standard rational-improvement formula
  `y=x(x^2+3D)/(3x^2+D)`.
- No screenshots were used as a substitute for text, formulas, tables, or diagrams. The scan slice is included only as a checking source.

## Remaining work on this item

Finish §§5--7:

- §5. Continuity of the domain of real numbers.
- §6. Calculations with real numbers.
- §7. Infinitesimal analysis.

Then merge the two installments into a single complete work-L German source TeX/PDF and English translation TeX/PDF, with the source scan range extended through printed p. 335.
