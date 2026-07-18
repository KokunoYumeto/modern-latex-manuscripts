# SGA 6 English layered reader — successor build and validation receipt

Date: 2026-07-18  
Bounded promotion: **PASS for the idx663--684 reconciliation checkpoint**  
Whole-volume authority: **layered; not uniformly source-audited**

## Successor reader

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `SGA6_English_Complete_Layered_WorkingEdition.tex` | 5,034 | `239623A45FB1796CF41039CC408D6CA4D5F2419144CCB6BF7DB037E00E1EFEDA` |
| `SGA6_English_Complete_Layered_WorkingEdition.pdf` | 2,586,422 | `0F8D9777F81F72174844C31A105DC5ECA277451C5E2320B04054D9FECC9CB2E8` |

The PDF has 377 A4 pages. All fonts are embedded. It contains a metadata
stream and custom metadata; the title, subject, durable project author, and
creator are populated. It is not tagged for accessibility.

## Editable components

| Component | Bytes | SHA-256 | Role |
|---|---:|---|---|
| `SGA6_idx647_665_English_SourceChecked_fragment.tex` | 32,602 | `A9A0E1EDE6369D72DF529F791B09CE879326A5B76D10B99D42E473B56999377A` | privacy-clean public overlap/prefix of the current tail; includes idx663--665 |
| `SGA6_idx666_702_and_backmatter_English_SourceChecked_Draft_fragment.tex` | 86,044 | `FEAC33DDC5D8E2A8A40BA8B0330A44043B618147DA69CEDE887D9C12EC426F1B` | idx666--702 plus unindexed back matter; idx666--684 reconciled here |

The independently reviewed production copy of the idx647--665 fragment had
SHA-256 `B12855A1A04597839E1017C1481DA038F0BC49CE07A53D6228D92B39C82F7A80`
and 32,466 bytes.  The public copy differs only by privacy-safe comments.  A
fresh isolated rebuild of the twelve public TeX files produced text identical
to the frozen reader, so the comment sanitization does not alter reader
content or layout.

## Build evidence

The retained two-pass build was run after the final source/layout corrections
and after the classic PDF Author field was added.

| Evidence | Bytes | SHA-256 | Result |
|---|---:|---|---|
| `logs/COMPLETE_BUILD_PASS1.log` | 46,820 | `9333350D9C92E964E66A5A19DA43D13A5573186617CD0F67BF6B321F95DC87FB` | successful pass 1 |
| `logs/COMPLETE_BUILD_PASS2.log` | 46,820 | `355F0D4FF2C833C8AC0F44F2D408CBD7F761FC440072A5A119DB94E88F1F09F1` | stabilized pass 2 |
| `logs/COMPLETE_BUILD_VALIDATION.json` | 1,619 | `28A4D0492441C8F4444A969217EA2FB0AA61243F703BD631EC67515A4FE7C216` | validator PASS |

The stabilized log contains zero errors, warnings, overfull boxes, underfull
boxes, or undefined references. Validation finds exactly 171 unique
current-rescribe markers in the exact idx532--702 sequence and ten unindexed
terminal markers.

## Scope and continuation

This receipt promotes only the English reconciliation against current French
control for idx663--684 (printed 650--671; source-PDF 653--674;
high-resolution 664--685). The next French-controlled cursor is idx685 /
printed 672 / source-PDF 675 / high-resolution 686.

It does not upgrade the inherited source-PDF 001--525 prefix to a uniform
page audit, and it does not upgrade idx685--702 or the unindexed terminal
pages beyond their disclosed scan-checked draft status.

The 381-page predecessor PDF with SHA-256 `F8B1E157...` remains preserved in
the predecessor workspace as historical lineage and is superseded for this
bounded checkpoint.
