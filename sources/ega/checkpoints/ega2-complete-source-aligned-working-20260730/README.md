# EGA II complete source-aligned English working reader

This checkpoint preserves the complete source-aligned EGA II English reader.

## Scope

- Continuous authority coverage from the Chapter II opening through Section
  8.14, the bibliography, index of notation, terminological index, original
  table of contents, and the end of Errata and Addenda (List 1).
- Authority cursor: end of the 219-page NUMDAM EGA II reader; no remaining
  EGA II translation cursor.
- Fourteen-file editable TeX closure with no raster dependency.

The source-era mathematical and editorial content remains in the reader.
Project, model, workflow, source-status, comparison-lineage, and private-path
material is absent. This is a working scholarly translation, not a critical
edition, rights clearance, peer review, or whole-EGA completion claim.

## Direct files

- Reader: `00b_EGA2_English_Reader.pdf`, 165 pages, 1060715 bytes,
  SHA-256 `6CEB2FFBF3F364B8CCFE64698751C3DEAD7A8E3B3823680ECF4CBB5E8B5241BD`.
- Master TeX: `02b_EGA2_English_Master.tex`, 1799 bytes,
  SHA-256 `F4624484EE2C0A855952DC0B3D917085AEBC10F8B71E7F373D2B2574AA8D69C1`.
- Complete source package: `10b_EGA2_English_Source_20260730.zip`.

The source ZIP contains the master, both preambles, all eight chapter
components, all three backmatter components, the same reader PDF, and exact
public controls. It excludes the French authority, generated build files, raw
logs, rendered QA images, private paths, and transient intermediates.

The public successor removes four duplicate table-of-contents registrations
caused by explicit `addcontentsline` calls around AMS starred headings. It
also repairs the original-contents column layout, isolates two source-page
markers as table rows, and incorporates “(List 1)” directly into the
Errata/Addenda heading. No mathematical body text was changed.

The French NUMDAM reader is identified by SHA-256
`111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB`
but is not redistributed. Underlying rights remain with their holders; this
package asserts no new blanket license.
