# Noether Paper 4 §7 — confirmed R823 dotted-symbol source defects

Alert ID: `N04-S07-SOURCE-DEFECT-DOTTED-SYMBOLS-001`  
Recorded: 2026-07-18  
Status: confirmed against the original print; downstream source-control propagation required  
Classification: R823 mathematical-notation transcription defects, not target-language preferences

## Exact locus and four dispositions

- Work: Emmy Noether, Paper 4, §7, immediately after formula (52).
- R823 locator: lines 4181--4189.
- Original locator: printed page 143; physical source-PDF page 26.

The original print distinguishes complementary forms by dotted symbols. R823
does not preserve those distinctions at four exact occurrences:

1. In the double sum, the print has
   `\dot q_{\sigma-\beta}^{(i_1\ldots i_\beta)}`; R823 line 4183 has the
   undotted `q_{\sigma-\beta}^{(i_1\ldots i_\beta)}`.
2. In the same double sum, the print has
   `\dot p_{n-\tau-\beta}^{(i_1\ldots i_\beta)}`; R823 line 4183 has the
   undotted `p_{n-\tau-\beta}^{(i_1\ldots i_\beta)}`.
3. In the next displayed relation, the print again has
   `\dot p_{n-\tau-\beta}^{(i_1\ldots i_\beta)}`; R823 line 4187 instead has
   `p_{n-\tau-\beta}^{\prime(i_1\ldots i_\beta)}`. This is a dot-to-prime
   substitution, not merely omitted decoration.
4. In the following prose, the print again uses the dotted
   `\dot p_{n-\tau-\beta}^{(i_1\ldots i_\beta)}`; R823 line 4189 has the
   undotted symbol.

The inherited English comparison material also loses these distinctions, but
that is a downstream target regression. It is not independent evidence for
the German transcription and must be recorded separately.

## Authority and evidence

- R823 cumulative editable German:
  `private-source/Noether_R823_cum_de.tex`
  - SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
  - Complete §7 slice, lines 4112--4268: 13,024 bytes; SHA-256
    `6A693F9E3936CDD0EC07DE8B66C925839CA989FC5D80932D5D8916E5B1AD5CFA`
    (UTF-8 lines joined with CRLF plus terminal CRLF; no source-body slice file
    was created).
- Dedicated original 38-page journal scan:
  `private-source/paper_04_crelle139_pp118_154_ORIGINAL.pdf`
  - SHA-256: `D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`
- Complete 400-dpi physical-page-26 / printed-page-143 diagnostic render:
  `private-source/print-26.png`
  - 2,077,921 bytes; 2592 × 3766 pixels
  - SHA-256: `EA25F37D4CF564ED53D7BE44302A23FEEE4E00F9AF35C557525E0918CA08E991`
- Focused diagnostic crop containing the double sum, following display, and
  prose occurrence:
  `private-source/p143_formula_crop.png`
  - 293,150 bytes; 2200 × 900 pixels
  - SHA-256: `4AC719505A73943707CD5D16C9DFE4328781EEBC5BFE2D573C7447AF1585C4ED`
- Inherited English comparison control:
  `private-source/Noether_Paper04_English_Translation_4_On_the_Invariant_Theory_of_Forms_in_n_Variables.tex`
  - Complete file: 109,132 bytes; SHA-256
    `200C9F9115C22D93455A3B7AA372687059E539C6D01959D30EEB25BBEEFFE722`
  - Complete §7 slice, inherited lines 924--1083: 12,364 bytes; SHA-256
    `77B2F7FF212360F641C56056110E5166E6931584A87201E2AC68C14EAA343743`
    (same CRLF slice recipe; no slice file created).

The dot marks are visually unambiguous in the original scan. This alert does
not silently mutate R823 and does not claim that the rest of §7 has completed
source audit.

## Propagation rule

1. Record all four occurrences as German editable-source transcription
   defects under one grouped finding with four separately addressable rows.
2. Correct the German authority only through its owning source-governance
   workflow, preserving an append-only before/after record and new source hash.
3. Check every downstream Paper 4 §7 target so future R823-driven rebases do
   not erase the dotted complementary-symbol distinction again.
4. Keep the inherited-English omissions as separate target-regression records;
   agreement between R823 and inherited English is derivative dependence, not
   corroboration.
5. Return the corrected German/source-control hash and downstream disposition
   IDs after the authority owner acts.
