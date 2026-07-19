# Rendered visual QA - SGA2-VIII-C23

The direct compiled French source physical page 79 and target page 1 were
rendered at both 300 and 600 dpi and visually compared.

Checks passed:

- source header gives running page 71;
- Corollary 2.3 lies wholly before the marginal printed-page marker 90;
- target heading reads `Corollary 2.3`;
- item labels are exactly (i), (ii), (iii), and (iv), in source order;
- condition (i) retains strict `>` and `n-c(x)`;
- condition (ii) retains `c(x)=1` and weak `>=`;
- condition (iii) retains `i` in the integers, calligraphic sheaf local
  cohomology, and `i<=n`;
- condition (iv) visibly retains `R^i i_*`, restriction to `U`, and `i<n`;
- marker (4) precedes the terminal period and the full note remains on page 1;
- no clipping, collision, broken line, missing symbol, blank render, or proof
  text beyond the declared boundary is present.

The source renderer emitted font-lookup warnings for legacy reader font names,
but the 300 and 600 dpi images are visually complete. These warnings concern
the same-edition PDF rendering environment, not the target TeX or its fonts.

Render SHA-256 values:

- source 300 dpi: `413899C59819721F60C6C001CB14214BEABA84FC302835F69B14C66D72B65ED2`;
- source 600 dpi: `B1A0E57ED810AB3E7812AFE89CE50279D8EA74071F28B7E5B7041683E7DF79FD`;
- target 300 dpi: `78595CA8F9882C96AD25CB0A92CE1FAA53F2D27902077ABD3D26CBF93C59C9BF`;
- target 600 dpi: `5D38EDDB15B688257D1E2EC491D7E6227A0D5DAC5551F69092382B3EB1E7A5BD`.

The target renders above are the regenerated post-review versions and visibly
show lowercase `O_X-module` in the opening hypothesis.
