# Noether Paper 4 §6 — confirmed R823 word-break source defect

Alert ID: `N04-S06-SOURCE-DEFECT-001`  
Recorded: 2026-07-18  
Status: confirmed against the original print; downstream source-control propagation required  
Classification: R823 transcription/word-boundary defect, orthographic and terminological rather than mathematical

## Exact locus

- Work: Emmy Noether, Paper 4, §6 opening / Theorem IV.
- R823 locator: line 4048.
- Original locator: printed page 137; physical source-PDF page 20.

R823 reads:

```tex
Schlu\ss{} ausdr\"ucke
```

This typesets as the erroneous split form `Schluß ausdrücke`.

The original print clearly has the single compound word:

```text
Schlußausdrücke
```

The editable German should therefore read, for example:

```tex
Schlu\ss{}ausdr\"ucke
```

This correction restores the printed compound and does not change any formula or mathematical assertion.

## Authority and evidence

- R823 cumulative TeX:
  `private-source/Noether_R823_cum_de.tex`
  - SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Original 38-page scan:
  `private-source/paper_04_crelle139_pp118_154_ORIGINAL.pdf`
  - SHA-256: `D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`
- Complete 300-dpi printed-page-137 render:
  `private-source/physical-20.png`
  - 1,406,772 bytes
  - SHA-256: `0F4679043AD91CDE56603946C18B9D1C4E309D10FDFDB964067B5B1CDFDBD000`

The compound is visible in Theorem IV near the lower part of printed page 137.

## Propagation rule

1. Record this as a German editable-source transcription defect, not as a target-language preference.
2. Correct the German source authority only through its owning source-governance workflow; this alert does not silently mutate R823.
3. Check every downstream Paper 4 §6 target and source-error ledger so later R823-driven rebases do not preserve or reintroduce the broken word boundary.
4. Existing translations that already render the sense as “final expressions” or an equivalent target-language compound may need only a source-defect ledger entry, not a target-body change.
5. Return the corrected German/source-control hash and downstream disposition IDs when the authority owner acts.
