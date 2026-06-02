# Cumulative translation method: Spanish/Japanese Noether lane

Scope through this packet: Spanish and Japanese translations through Paper 06, §15. This file is cumulative and should travel with later packets.

1. Base source and control. German TeX/source is treated as the governing text. English control TeX is used as a secondary witness only for sense checking and to stabilize long technical sentences. Where source/control anomalies appear, preserve the source reading and record the anomaly rather than silently normalizing.

2. Output standard. Deliver editable TeX and compiled PDF. Do not use screenshots as substitutes for tables, formulas, or difficult notation. Mathematical displays remain editable TeX.

3. Translation register. German `Körper` is translated as Spanish `cuerpo`, Japanese `体`; `System` as `sistema` / `系`; `lineare Schar` as `familia lineal` / `線形族`; `Integritätsbereich` as `dominio de integridad` / `整性領域`; `relativ-ganzer Bereich` as `dominio relativamente entero` / `相対的整領域`; `ganze rationale Funktion` as `función racional entera` / `整有理関数`; `ganzzahlig` in §§14-15 is translated with explicit integer/algebraic-integer language to distinguish it from ordinary integral-rational polynomial language.

4. Special-character policy. Preserve mathematical Greek, fraktur letters, primes, German names with diacritics, and formula punctuation. For Japanese, keep Latin technical names (Lüroth, Castelnuovo, Enriques, Hilbert, Kronecker, Galois) in Latin script unless an established Japanese rendering would materially improve clarity.

5. Build policy. Spanish is built with pdfLaTeX under UTF-8/T1. Japanese is built with LuaLaTeX and jlreq/luatexja. For very long cumulative Japanese files, if local compilation is brittle, assemble the verified previous cumulative PDF and verified current chunk PDF, while still shipping the full cumulative TeX for local Codex rebuild.

6. Packaging. One ZIP contains one root folder and only subfolders beneath that root.
