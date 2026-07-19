# Rendered visual QA - SGA2-VIII-L24

Directly compiled French source physical page 80 and target page 1 were
rendered at both 300 and 600 dpi and visually inspected at original resolution.

Checks passed:

- source header gives running page 72 and the in-scope text lies on printed
  page 90, above the later printed-page marker 91;
- target authority box distinguishes raw TeX cursor 2723 from substantive
  prose cursor 2725;
- the regular prescheme covering, `X` closed in regular `X'`, and immediate
  reduction remain legible;
- the causal affine reduction reads `by covering X with affine open subsets`;
- `F=tilde M` visibly retains the equality and tilde, and finite projective
  dimension is present;
- target heading reads `Lemma 2.4` and has a corresponding named destination;
- the lemma retains regular Noetherian prescheme, lowercase `O_X-module`, the
  universal `x in X`, projective dimension of `F_x`, and `bounded above`;
- no invented `pd` operator, displayed map, proof text, clipping, collision,
  broken line, missing symbol, or blank render is present.

Render SHA-256 values:

- source physical 80, 300 dpi:
  `3F7D8648A9D98CF406BE4A44B3B4BD2709AAB3B60730175CEFFEDA97ABFC95C4`;
- source physical 80, 600 dpi:
  `6525F602B43F2F00005D36F29D8F80BC55FE71813D7E9A0DDCF97A1C5EC1E85E`;
- target page 1, 300 dpi:
  `7D21010814FE54843EB064AD88FFC80188E9BDBCF20726825758163A6C4FBC89`;
- target page 1, 600 dpi:
  `390A5E8C42B0CDA838032190F2C81954A5B920232B9458B3D26EF4CA2FEEB2AC`.

The source renderer emitted legacy display-font lookup warnings, but the
source images are visually complete. The equation-counter reset at line 2723
has no visual page body and is controlled by TeX/ledger comparison.
