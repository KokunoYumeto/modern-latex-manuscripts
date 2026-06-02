# Special characters, glyphs, and macro conventions

| Source mark | TeX/rendering convention | Notes |
|---|---|---|
| é, è, à, ô, ï | UTF-8 with `\usepackage[utf8]{inputenc}` or TeX accents | Prefer UTF-8 in prose; TeX accents in macro-heavy contexts. |
| \(\ell\) | `\ell` | Avoid OCR's plain `l` in \(\ell\)-adic formulas. |
| \(\Pic\), \(\NS\), \(\Gr\), \(\ch\) | operator macros | Prevent inconsistent italicization. |
| \(\mathbf P^N_k\) | `\mathbf P^N_k` | Standard projective-space notation. |
| numerical pairings | `\langle ... \rangle` | Used for intersection forms and degrees. |
| diagrams | `tikz-cd` | Keeps commutative squares/exact diagrams auditable. |
| long exact sequences | displayed `aligned` or `tikz-cd` | Prevents overrun and preserves structure. |

Core macros carried forward:

```tex
\providecommand{\NS}{\operatorname{NS}}
\providecommand{\Pic}{\operatorname{Pic}}
\providecommand{\Tor}{\operatorname{Tor}}
\providecommand{\Gr}{\operatorname{Gr}}
\providecommand{\ch}{\operatorname{ch}}
```


## Final index macro additions

Confirmed index notations include `\Qcoh`, `\Coh`, `\Parf`, `\Lib`, `\Loclib`, `\Mod`, `\Proj`, `\parfamp`, `\toramp`, `\alg`, `\num`, and `\naif`. Preserve source-style references such as `II App. II`, `X App.`, and Roman numeral Exposé labels.


## Index-macro additions used in the complete SGA 6 wrap

The final index confirmed category macros (`\Qcoh`, `\Coh`, `\Parf`, `\Lib`, `\Loclib`, `\Mod`, `\Proj`), amplitude macros (`\parfamp`, `\toramp`), and algebraic/numerical/naive qualifiers (`\alg`, `\num`, `\naif`). Preserve source-style references such as `II App. II`, `X App.`, and Roman numerals in index tables.
