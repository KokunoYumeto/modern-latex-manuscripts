# OTHER AI: NATIVE TEX CORPUS REQUIREMENT

THIS IS THE CURRENT REQUIREMENT FOR THE INTERLANGUAGE / INTERSLAVIC SOURCE-CORPUS LANE.

DO NOT SATISFY THIS WITH LINKS ONLY.
DO NOT SATISFY THIS WITH PDF-ONLY WITNESSES.
DO NOT SATISFY THIS WITH GENERATED TRANSLATIONS.
DO NOT SATISFY THIS WITH MANIFESTS THAT SAY WHERE FILES MIGHT EXIST.
DO NOT SATISFY THIS WITH ONE OR TWO SAMPLE PAPERS PER LANGUAGE.

FOR EVERY LANGUAGE YOU ARE WORKING ON, COLLECT ACTUAL SOURCE FILE BODIES:

- `.tex`
- `.ltx`
- `.sty`
- `.cls`
- `.bib`
- `.bbx`
- `.cbx`
- `.dtx`
- `.ins`
- local macro/style files needed to compile or interpret the TeX
- README/build metadata when present

THE TARGET IS HUNDREDS OF REAL SOURCE-BODY FILES PER LANGUAGE OR LANGUAGE LANE WHERE POSSIBLE.

Priority languages/lanes currently under-served:

- Czech
- Polish
- Slovak
- Slovenian
- Croatian
- Serbian
- Bulgarian
- Macedonian
- Belarusian
- Upper Sorbian
- Lower Sorbian
- Interslavic / constructed Slavic apparatus
- Ukrainian
- Russian
- Chinese
- Japanese
- Arabic
- Persian/Farsi
- Spanish
- French

For each collected source-body bundle, include:

1. One ZIP per language or coherent language lane.
2. A CSV manifest with file path, source URL, repository/archive origin, license if known, language, subject/domain, and whether the file is native-authored, translated, generated, or unknown.
3. A README that says plainly what the bundle is and what it is not.
4. SHA256 checksums for the ZIP and, if practical, for individual files.

Classification rules:

- Native-authored mathematical or linguistic TeX is the preferred evidence.
- Public arXiv/GitHub/source-repository TeX is useful if the file body is included.
- PDF/web witnesses are useful provenance, but they are NOT a substitute for TeX source-body bundles.
- Generated Noether/Interlingua support TeX may be useful internally, but it is NOT native-source attestation.
- If a language has only PDF witnesses so far, say that explicitly and keep collecting.

Put the resulting bundles in the public repository under:

`interlanguage-sidecar/20260704/latex_source_body_bundles/`

Then update:

- `interlanguage-sidecar/20260704/latex_source_body_bundles/README_LATEX_SOURCE_BODY_BUNDLES_20260704.md`
- `interlanguage-sidecar/20260704/latex_source_body_bundles/LATEX_SOURCE_BODY_BUNDLES_MANIFEST_20260704.csv`
- `interlanguage-sidecar/20260704/latex_source_body_bundles/LATEX_SOURCE_BODY_BUNDLES_CONTENT_AUDIT_20260705.csv`

Current known gap as of 2026-07-05:

The repository has useful source-body bundles for Romance, Persian/RTL/Arabic, CJK, Slavic/Interslavic generated support, and a small Slavic linguistics arXiv source bundle. It still does NOT have the requested hundreds of independent native mathematical `.tex` source bodies for the non-Russian/non-Ukrainian Slavic lanes. That gap is live.
