# Static TeX check

Target: `SGA6_sourcePDF001_525_English_Inherited_PartiallySourceSynchronized_fragment.tex`  
Target SHA-256: `6A6878FCE68050F797E1E4256D363D038A7BE0B4C8A00430195E268887391194`

After stripping unescaped TeX comments and ignoring escaped braces:

- final brace balance: 0;
- minimum running brace balance: 0;
- distinct `begin`/`end` environment kinds: 17;
- environment-count mismatches: 0.

Targeted text checks also confirmed:

- `gamma^k(N'_0)=0` at line 9213;
- Lemma 1.5.1 at line 10084 and Lemma 1.5.2 at line 10092;
- Propositions 1.6/1.7 and corrected downstream references;
- formulas (5.4.1)/(5.4.2) retain balanced display environments;
- repair105 normalized block hash remains exact.

This is a fragment-level structural check, not a substitute for the parent task's two-pass cumulative-reader compile.

