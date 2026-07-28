# SGA 3 Exposé XXI — native-diagram/high-zoom lead PASS

Date: 2026-07-28  
Disposition: `PASS_LOCAL_NATIVE_DIAGRAM_CLOSURE`  
Archive/publication disposition: not dispatched; not claimed

## Scope and authority

This receipt closes the complete diagram set in Session C's
no-overwrite Exposé-XXI Loop-2 successor. The Loop-1 predecessor remains
unchanged.

- authority: `Exp21-13oct24.pdf`;
- authority size: 392,935 B / 46 pages;
- authority SHA-256:
  `1FB0720FFD496E6076DBEC3702CBD3CBA828C2BAAE0340A840855DF86A496284`;
- included scope: local pages 1–46 / combined-reader pages 1095–1140;
- hard stop: before Exposé XXII local page 1 / combined page 1141.

The exact machine inventory is:

`controls/SGA3_EXPOSE_XXI_NATIVE_DIAGRAM_INVENTORY_20260728.csv`

- 11 rows x 13 columns;
- 5,568 B;
- SHA-256:
  `64DBB705AAE1EF37F9CE56D4CC04236501A97C5AB4B84D10169C73FF20513F12`;
- rectangular and formula-safe;
- every row binds its source component/line, authority crop, delivered
  crop, evidence hashes, resolution, disposition, and any correction.

## Review method

The top-level session lead manually compared every one of the 11
diagrams directly against the authority at approximately 5,000 dpi.
No mathematical or visual judgment was delegated. No diagram required
an ambiguity escalation to 9,000 dpi.

The review checked:

- node identities and ordering;
- every arrow direction, head, attachment, and branch;
- labels, primes, stars, subscripts, superscripts, and label sides;
- isomorphism marks and punctuation;
- the full three-row canonical-isogeny grid;
- every Dynkin family from \(A_n\) through \(G_2\), including weights,
  branching, ellipses, and rank restrictions.

Existing 600-dpi and 1,200-dpi artifacts remain legitimate
history/context. They are not invalidated merely by their resolution.
Only 300-only diagram-fidelity approvals are insufficient. The PASS in
this receipt is supported by the new 5,000-dpi lead comparisons.

Raster crops are private witnesses only. The delivered source uses
native TeX throughout and contains zero active `\includegraphics`
calls.

## Findings and repairs

All 11 diagrams now pass. Two material discrepancies were found and
repaired before the final build:

1. `SGA3-XXI-D001`: the upper-right endpoint of the isogeny square was
   restored to \(M\), giving \(M'\xrightarrow{f}M\).
2. `SGA3-XXI-D005`: the bottom horizontal arrow was corrected so that
   \(f_0\) is above the arrow and the isomorphism tilde is below it,
   exactly as printed.

The remaining nine diagrams required no material correction after
native reconstruction.

The final D005 repair was rerendered from the final PDF at 5,000 dpi:

`qa/native_redo_20260728/final_r6_5000dpi/xxi_d005_final_repaired_5000dpi.png`

- 2,316,984 B;
- SHA-256:
  `AC42A8456EBB070BAF715C070F2AAE3488F2FA0BE7A995508A6D675AAFB06D13`.

The complete Dynkin plate was checked in two delivered 5,000-dpi
bands, including the terminal \(G_2\) row. Its native source is:

`tex/figures/xxi_p44_dynkin_classification_native.tex`

- 2,029 B;
- SHA-256:
  `09BC5BCC580DB5BBE9E4B18E4F2030E2ED6352AA340A16888239F59D1C5C8C00`.

## Final build

The first attempted final output directory, `build_native_r5`, is
preserved as adverse build history: it was launched one directory too
deep and stopped before producing a PDF because the master's deliberate
`tex/...` paths could not resolve. No source byte was changed by that
attempt.

The corrected no-overwrite final build is `build_native_r6`.

- three XeLaTeX passes: exit 0;
- all three console logs byte-identical:
  17,332 B / SHA-256
  `DA3748706B5D6EB78A6E8D8407BEBF81CFD0849EB6C40F1C03CCDFD630AED9C7`;
- fatal errors: 0;
- undefined control sequences/references: 0;
- multiply-defined labels/destinations: 0;
- duplicate destinations: 0;
- missing characters: 0;
- overfull boxes: 0;
- rerun diagnostics: 0;
- active `\includegraphics`: 0;
- active native diagrams: 11
  (nine `tikzcd` and two `tikzpicture`).

Final identities:

- master: 3,597 B / SHA-256
  `A0C8E0173AE0C6D620AE56F496FE58B067E29C8142B26614DED40BFA71C45F10`;
- PDF: 56 A4 pages / 295,395 B / SHA-256
  `CAB7DB1B5171E47E1458A8EF4CC9226D0D64506D9E154E7780C0D88039702971`;
- final log: 40,800 B / SHA-256
  `33D97F0BFBD158AABD02F3A98A1104B0370F9CEB54583A1E24533B6B487A8643`;
- AUX: 19,964 B / SHA-256
  `3D703FAC3D207DDF743494D5A05DBD63E89587B1095E26727A252F456D8BBD15`;
- TOC: 2,901 B / SHA-256
  `2FDBD92A2E6E744F2E345F2DB1C9BC2A08E8770AA2ACA0A5B2DCE1DA9B7070D8`;
- OUT: 5,852 B / SHA-256
  `C73EC2D93A8C35976EB5CB9EC4A0EB47D75C12710542F30A5D90E2F709A9C514`.

## Boundary

This closes Session C's local Exposé-XXI native-diagram obligation.
Reference-v2 closure, cumulative SGA3 integration, privacy-clean public
projection, independent release seal, archive transport, publication,
and readback remain separate and unclaimed.
