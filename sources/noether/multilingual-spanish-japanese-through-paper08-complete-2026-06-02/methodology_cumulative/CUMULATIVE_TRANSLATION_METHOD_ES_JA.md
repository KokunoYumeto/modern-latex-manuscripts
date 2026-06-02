# Cumulative translation method: Spanish/Japanese Noether lane

Scope through this packet: Spanish and Japanese translations through Paper 08 complete. This file is cumulative and should travel with later packets.

1. Base source and control. German TeX/source is treated as the governing text. English control TeX is used as a secondary witness only for sense checking and to stabilize long technical sentences. Where source/control anomalies appear, preserve the source reading and record the anomaly rather than silently normalizing.

2. Output standard. Deliver editable TeX and compiled PDF. Do not use screenshots as substitutes for tables, formulas, or difficult notation. Mathematical displays remain editable TeX.

3. Translation register. German `Körper` is translated as Spanish `cuerpo`, Japanese `体`; `System` as `sistema` / `系`; `lineare Schar` as `familia lineal` / `線形族`; `Integritätsbereich` as `dominio de integridad` / `整性領域`; `relativ-ganzer Bereich` as `dominio relativamente entero` / `相対的整領域`; `ganze rationale Funktion` as `función racional entera` / `整有理関数`; `ganz rational` as `racional entero` / `整有理`; `Polarprozess` as `proceso polar` / `極化過程`; `Grundform` as `forma fundamental` / `基本形式`; `vollständiges System` as `sistema completo` / `完全系`.

4. Special-character policy. Preserve mathematical Greek, fraktur letters, primes, German names with diacritics, and formula punctuation. For Japanese, keep Latin technical names (Lüroth, Castelnuovo, Enriques, Hilbert, Kronecker, Galois, Mertens, Capelli, Deruyts, Clebsch--Gordan, Fischer, Zermelo) in Latin script unless an established Japanese rendering would materially improve clarity.

5. Build policy. Spanish is built with pdfLaTeX under UTF-8/T1. Japanese had previously used LuaLaTeX and jlreq/luatexja. In this packet the Japanese chunk and cumulative PDF are built with XeLaTeX + xeCJK + Noto Serif CJK JP because the local LuaHBTeX/luaotfload run did not complete reliably; the text body remains ordinary UTF-8 TeX and can be adapted back to jlreq/luatexja by local Codex if desired.

6. Packaging. One ZIP contains one root folder and only subfolders beneath that root.
