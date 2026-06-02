# Local agent handoff: dense TeX translation lane

Process one source file at a time. Do not broaden the source radar unless the file introduces a new mathematical object.

Next file order:
1. `03_source_context/sola_eskf_1711_02508/Noise.tex`
2. `03_source_context/sola_eskf_1711_02508/ErrorState.tex`
3. `03_source_context/sola_eskf_1711_02508/Quaternion.tex` sections: conventions, perturbations, derivatives, integration
4. `03_source_context/micro_lie_1812_01537/manifolds.tex`
5. `03_source_context/micro_lie_1812_01537/SO3.tex`
6. `03_source_context/micro_lie_1812_01537/SE3.tex`
7. Labbe notebooks 01-04 to TeX.

Rules:
- Translate prose to technical Ukrainian.
- Preserve LaTeX commands, labels, refs, citations, variable names, equations, and code identifiers.
- If a formula looks inconsistent, add `% CHECK_FORMULA:` rather than silently changing it.
- Build with XeLaTeX.
- Add a row to `translation_status.csv` for every processed source file.
