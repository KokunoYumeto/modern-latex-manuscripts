# SGA 1 I.9.2 working build/source/render summary

## Preserved rejected builds

- r1: `build/i9_2_working_r1_initial_20260719`, 10 files / 704,238
  bytes. The compiler wrote new auxiliaries in the output directory but read
  stale root auxiliary input, leaving false undefined-reference diagnostics
  after three successful exits. Pass-three log: 29,475 bytes, SHA-256
  `94986DDA6759B92005A1DAC98073515E7AE2E61647F36DED88D82C87E446F189`.
- r2: `build/i9_2_working_r2_isolated_source_20260719`, 5 files / 57,000
  bytes. A malformed PowerShell destination expression omitted every fragment;
  pass one stopped. Console: 7,836 bytes, SHA-256
  `295CEB7DBDBD382C33827C3D6D8446A2A192DF93803AF1C78354D375ECED14D3`.

Neither rejected build is a translation defect or a promotable surface.

## Rejected isolated r3 build

- Directory: `build/i9_2_working_r3_isolated_source_20260719`.
- The visible pages and ordinary LaTeX references looked clean, but an
  independent gate found a real `pdfTeX warning (ext4)` in passes two and
  three: both statements resolved to destination `proposition.1.9.2`.
- Pass-three log: 28,857 bytes, SHA-256
  `53A5FDDE5A52F9FBC26605F41DB81E6BAE9C85890FEE9A3F23CA68B4826E8B66`.
- PDF: 16 A4 pages / 545,835 bytes; SHA-256
  `658F8E130164B11676C45FFEA21B33D22AF712114B310FB0F542B01B9B58373B`.

r3 is rejected and must not be promoted. A successful compiler exit and a
clean visible render do not override a duplicate internal PDF destination.

## Clean isolated r4 successor

- Directory: `build/i9_2_working_r4_unique_hyperref_anchor_20260719`.
- The second statement receives a scoped internal destination
  `proposition.1.9.2.second`; the first remains `proposition.1.9.2` and both
  visible headings remain I.9.2.
- Pass-two and pass-three logs are each 28,556 bytes, SHA-256
  `0181AD5749C6BD3F9F76BED4ABAF49583FDFE928B5DA3109897355C04018E981`,
  with zero declared LaTeX/package/box/reference/PDF warnings.
- PDF: 16 A4 pages / 545,957 bytes; SHA-256
  `A5C59DB6149BA82A443F919DFCF5952277D994FFF07B2B614A34BB150525C904`.
- PDF metadata is populated; the file is unencrypted, has no form,
  JavaScript, or suspects, and has 30/30 embedded subset Unicode fonts.

## Render comparison

- r4 180-dpi render: 16 PNG / 6,346,588 bytes.
- Ordered `name|bytes|sha256` digest:
  `0DC7C1D8473EAF69860CF6C12F173CBE11D44078DE1C05B154A300A18339BB3B`.
- The r4 render is byte-identical on all 16 pages to the rejected r3 render;
  the repair changes only the internal destination structure.
- Pages 3--15 are byte-identical to the frozen public I.9.1-r2 render.
- Pages 1 and 2 changed only for the honest title/source-boundary update.
- Page 16 changed for the two new statements and visible duplicate-number
  note; it has no clipping, overlap, malformed glyph, or orphaned heading.

Independent final review and the terminal machine/reference-closure gate pass;
r4 is the locally sealed successor. r3 remains rejected history. The
workpass-root PDF intentionally remains the prior frozen public I.9.1-r2
evidence object; local I.9.2 closure references the isolated r4 PDF and does
not silently overwrite that historical locator.
