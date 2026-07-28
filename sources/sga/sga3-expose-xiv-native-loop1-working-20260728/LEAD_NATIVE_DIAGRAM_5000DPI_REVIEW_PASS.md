# SGA 3 Exposé XIV — lead native-diagram review PASS

Date: 2026-07-28

Status: **PASS** for the complete four-row Dynkin-automorphism diagram
surface in this no-overwrite Exposé-XIV Loop-2 successor.

The top-level Session-C lead performed this review directly. No agent or
subagent made the mathematical or visual judgment.

## Controlling source and delivered reader

- Polo–Gille authority: `Expo14.pdf`, 376,258 bytes, 36 pages,
  SHA-256
  `467F03717A06F85DB3C1CAFB1D35E8A1E07247372717B94CD6E19F1EB114FEA1`.
- Authority locus: local page 34 / combined page 868.
- Delivered master:
  `tex\SGA3_Expose_XIV_English.tex`, 3,301 bytes, SHA-256
  `59D9FDB32AA981891BD807EF419D201C74A941E75A1FBAFA21F09C4C874CC9C1`.
- Native component:
  `tex\components\30_expose_XIV_appendix_lemma3_case3_end_en.tex`,
  4,918 bytes, SHA-256
  `2E209ABBE43B48E55D9CE2A670EEE43327A889AF7CF0BFB9372EC2C35B4357B9`.
- Delivered reader:
  `build_native_diagram_r1\SGA3_Expose_XIV_English.pdf`, 37 A4 pages,
  240,676 bytes, SHA-256
  `6CD0B985FE2F4D0C69A52ACCD0E766F3029B3E8E6A40AEB31B9E511C40E72EA0`.
- Converged log: 40,645 bytes, SHA-256
  `E8EBADF980B84B6FCFEDABE75E8EEDF1321DCE96E7D023D05DA753119606CA9C`;
  three XeLaTeX passes exit successfully with zero required diagnostic
  hits.

The delivered source contains no active `\includegraphics` call. The four
rows are editable native TikZ: odd \(A_n\), \(D_4\), \(D_n\) for
\(n\geq5\), and \(E_6\). The predecessor raster remains only as
unreferenced internal history and is not a delivery artifact.

## Evidence and direct comparison

The 600-dpi full-page images below are retained as legitimate locator and
layout context. They are not the basis of the new fidelity approval:

- `authority_p34_locator_600dpi.png`, SHA-256
  `F9C91CAB01311FE13CD8CD940DFE0166F08F604F48805E95D55D714534E8CEC6`;
- `delivered_p37_native_locator_600dpi.png`, SHA-256
  `E83527B82F3C4D82D0AC53D0DCCDDF62F42671B39D8FDB4708075AE06AD9B27E`.

The lead compared every source row and delivered row at a true 5000-dpi
regional render:

| Row | Authority evidence SHA-256 | Delivered evidence SHA-256 | Result |
|---|---|---|---|
| odd \(A_n\) | `A9326778CD3A444187A4EEA25AEFEBE834DDEB3E4F2A60B2707C220213D8BA6A` | `04308DD8F488E6D8BAE6BE31E2E80DBC89E675D7200C5481B7230391B1E3311E` | PASS |
| \(D_4\) | `0FF888C21DEB94E2E13CDF803B0B90C7C793FDE802389F3393FF1099BAA00677` | `309BE0445DFD430A36D75CD0EB3F4FFD530802542893DD1A79A217409F78EF0C` | PASS |
| \(D_n,\ n\geq5\) | `AAE0C2BB5DF3C2EDB3DF25319B3A2449F5BC190D4903517FBF26C0A45A3FA5C4` | `C891360093D0C0705AA94CEB9AEFF4756E25218C6F1103E5163F803E49270D0A` | PASS |
| \(E_6\) | `E1DBBFDE44654CE540067D17317DFEDDA7467DAF9637AED89BFD3470C712B2C1` | `D44C813F6FC55FB6E756D95FAA2860F051BD15E063E4F6573D5CD9939CB703D8` | PASS |

The first two attempted \(E_6\) crops were visibly misframed and have no
adjudicative force. The `authority_p34_E6_5000dpi_r3.png` identity in the
table is the corrected true source-region render.

The direct comparison checked node count and incidence, every straight
edge, every curved automorphism arrow, arrowhead direction and pairing,
attachment points, branch position, row label, subscripts, inequalities,
and punctuation. No discrepancy remains:

- odd \(A_n\): five-node chain with the outer and inner reflection pairs;
- \(D_4\): three outer vertices and the same directed three-cycle;
- \(D_n\): four-node stem, two terminal branches, and the same
  bidirectional terminal swap;
- \(E_6\): five-node chain with the central downward branch and the two
  reflection pairs.

Nothing was ambiguous after the 5000-dpi comparison, so a 9000-dpi
escalation was not required. Existing 600- or 1200-dpi evidence is not
invalidated by this review; only a 300-only fidelity approval would have
been insufficient.

## Disposition

The Exposé-XIV native diagram surface is locally closed and may feed the
later cumulative source tree. This receipt does not by itself claim
reference-v2 closure, a privacy-clean public package, archive transport,
publication, or public readback.
