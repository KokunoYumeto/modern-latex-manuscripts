# EGA IV Sections 16-21 live source custody snapshot

This directory preserves one exact, privacy-clean snapshot of the two active
source-alignment lanes for EGA IV Sections 16-21. It is a GitHub source-survival
checkpoint, not a completed translation, release reader, or Zenodo upload.

## Scope

- `lanes/sections16-18`: assigned Sections 16-18, hard stop before Section 19.
- `lanes/sections19-21`: assigned Sections 19-21, hard stop at the end of EGA IV.
- Controlling authority: `EGA_IV-4_PMIHES_tome32_1967.pdf`, 360 physical
  pages, SHA-256
  `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
- The authority PDF, authority-derived pixels, OCR bodies, build products, and
  private operational logs are excluded.

## Snapshot state

The files were copied while both producer lanes remained active. Their copied
status and logbook records therefore describe the latest formally recorded
cursor, while the copied source files can contain newer, unsealed edits. Exact
file identities in `SHA256SUMS.csv` control this snapshot; no later source
alignment or review claim should be inferred from file modification alone.

Notable copied source identities:

- `ega4-16.tex`: 177,054 bytes, SHA-256
  `FC4DFDC9A88A97B1920662496D61A43D6B95413CAF0AC9B2DFD1C83403009883`.
- `ega4-19.tex`: 169,911 bytes, SHA-256
  `BA36FA26C55DCE8F969F8C5E7DD9848E1ECC8A988EBC2CD6DF64EE5ECF6DDF8B`.

## Custody checks

Each copied build harness completed one isolated XeLaTeX pass without a hard
TeX error marker:

- Sections 16-18: 120 pages; transient validation PDF SHA-256
  `3F0A461F4EE5AF3847956E9F8DCF0B8735CB60A7D049CFE7D34593583CC1C7BD`.
- Sections 19-21: 100 pages; transient validation PDF SHA-256
  `83E251F27F7A49FD3897472EFB20502D817DF66EF42811C1F555DE51BED52064`.

The transient PDFs and logs were deleted after validation and are not part of
this custody package. Expected unresolved cross-volume references in the
partial harnesses are not promoted to release claims.

The public-surface privacy scan found no private absolute path, personal name,
task identifier, credential, or agent-workspace string. One broad keyword scan
matched only the mathematical prose phrase `by the same token`.

## Publication status

This snapshot is suitable for GitHub source custody. It is not a Zenodo
successor and must not displace the current cumulative EGA readers. A later
producer-sealed cumulative reader/package should supersede it for public
reading once source alignment, build, privacy, rights, and release checks close.

