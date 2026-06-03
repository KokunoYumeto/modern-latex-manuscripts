# Paper 14 method and special-character note

Scope: Paper 14, `Die arithmetische Theorie der algebraischen Funktionen einer Veränderlichen in ihrer Beziehung zu den übrigen Theorien und zur Zahlkörpertheorie`, complete.

Source basis: the paper-level German edition, the paper-level English control translation, and the source scan `Noether_Paper14_Arithmetic_Theory_SOURCE_SCAN_collected_pdf_pages285-306_printed_pp271-292.pdf`. The scan/source/control all cover the eight numbered sections.

Translation policy: preserve the historical comparison among Riemann, Weierstrass, Brill--Noether, Dedekind--Weber, Hensel--Landsberg, Hilbert/Furtwängler, and class-field analogies. Do not modernize away the paper's vocabulary of `Polygon`/divisor, `Restgruppe`, `korresiduell`, `Führer`, `Differente`, and `absolute Riemannsche Fläche`; translate them consistently and add parenthetical bridges where the historical term could otherwise be obscure.

Macro policy: Paper 14 introduces local Fraktur and calligraphic notation (`\frp`, `\fra`, `\frb`, `\frf`, `\frD`, `\calA`, `\calB`, `\calN`). The cumulative TeX includes a small Paper 14 macro-support block immediately before the appended Paper 14 body, using `\providecommand` only, so it does not override prior cumulative definitions.

Audit flags: no translation gaps are declared. The Japanese standalone/cumulative use XeLaTeX/xeCJK. The Spanish standalone/cumulative use pdfLaTeX. Render checks were made for all standalone pages and for cumulative tails; Japanese cumulative tail pages were additionally rendered manually with `pdftoppm` after the wrapper hit the session time limit.
