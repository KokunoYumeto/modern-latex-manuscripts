# SGA 6 English prefix repair: source comparison for source-PDF 14 and 141–150

Date: 2026-07-18

## Scope and authority

This comparison resolves the early-prefix gates identified by the prefix 001–525 audit. The edited production file is:

    SGA6_sourcePDF001_525_English_Inherited_PartiallySourceSynchronized_fragment.tex

Authority order used:

1. Original scan: C:\Users\Floris\Documents\Papors\OS\sga6.pdf
2. Current French control: C:\IL_GitHub\00_main_current\sources\sga\sga6-claude-workpass-source-rescribe-20260704\sga6_fr_workpass.tex
3. Inherited English repair108 prefix, used only as the text to be checked and repaired

The scan pages, printed volume pages, and current-rescribe indices are distinct. These pages precede the current-rescribe sequence: idx532 begins only at source-PDF 526. “Not assigned” below therefore does not mean “missing.”

| Source-PDF page | Printed volume page | Current-rescribe index | English post-repair line(s) | Finding and disposition |
|---:|---:|---|---:|---|
| 14 | 7 | not assigned; prefix before idx532 | 193–219 | Confirmed major compression. Restored the omitted definition of a perfect complex, local bounded-complex criterion, triangulated-subcategory and cone discussion, construction of K(C), distinguished triangle, global resolution statement, K(Parf(Y)) isomorphism, and class formula. Context pages 13 and 15 were also rendered because the paragraph crosses both page boundaries. |
| 141 | 134 | not assigned; prefix before idx532 | 3350, 3352 | Restored Exercise 5.7’s footnote defining S as the final object and repeated its marker at part b, as in the scan and French control. |
| 142 | 135 | not assigned; prefix before idx532 | 3388–3393 | Restored Lemma 5.8.2’s footnote defining S and the constant sheaf Z_S, with the marker on the displayed arrow’s target. |
| 143 | 136 | not assigned; prefix before idx532 | 3421 | Corrected “canonical arrows of (5.8.2)” to “canonical arrows of (3.17.1).” The later sentence saying that those arrows are isomorphisms by (5.8.2) remains unchanged and is source-correct. |
| 144 | 137 | not assigned; prefix before idx532 | 3440–3444 | Repositioned the distinguished triangle to the source orientation: E'' → E' → E'^m[-m] → E'', with the +1 label on the return arrow. No objects or morphism order were changed. |
| 145 | 138 | not assigned; prefix before idx532 | 3458 | Restored the source parenthesis and scare quotes in “(so that A ‘is’ an ordinary ring).” |
| 146 | 139 | not assigned; prefix before idx532 | 3486 | Adjudicated Im as an upright operator and normalized raw \Im(p') to \operatorname{Im}(p'), the dominant style elsewhere in this English prefix. Mathematical content is unchanged. |
| 147 | 140 | not assigned; prefix before idx532 | 3509–3513 | Repositioned Definition 6.1’s distinguished triangle to L' → L → L'' → L', and restored the dashed return arrow shown by the scan and French control. |
| 148 | 141 | not assigned; prefix before idx532 | 3531 | Restored the note about K(C) as a footnote attached to k(C) in §6.3. Removed its inherited reclassification as a standalone Remark after Lemma 6.4. |
| 149 | 142 | not assigned; prefix before idx532 | no edit | Clean control. The diagram and surrounding prose agree substantively with the scan and French control; retained unchanged. |
| 150 | 143 | not assigned; prefix before idx532 | 3617–3620 | Restored “(cf. (4.9))” alongside the displayed Proposition 6.7 morphism. |

## Source-PDF 14: confirmed compression and source-level caveats

The inherited English reduced a continuous source passage to one sentence. Direct visual comparison of source-PDF 13–15 and the French control confirms that the following material was absent:

- “to which one would not know how to associate a class in K^\bullet(Y)”;
- the fact that R^i f_*(F) are the cohomology sheaves of Rf_*(F);
- the full definition of “perfect” used here;
- the affine-local bounded complex of finite-type locally free modules;
- the homological-algebra comparison with locally free modules;
- closure under cones or “mapping cylinders”;
- the generators-and-relations definition of K(C);
- the distinguished triangle relation;
- the global-resolution consequence when Y has an ample invertible module;
- the canonical K^\bullet(Y) → K(Parf(Y)) isomorphism;
- the class and alternating-sum formulas.

Two source-level inconsistencies were not carried into English silently:

1. Source-PDF 13 and the French control mix E on the left and F on the right of the naïve direct-image formula. The surrounding prose consistently concerns F. The inherited English F/F normalization was retained and is now documented by a TeX comment at lines 188–189.
2. Source-PDF 14 literally prints:

       K^\bullet(X) ---> K(Parf(Y)).

   The surrounding assertion concerns perfect complexes on Y and calls the map an isomorphism. The typed domain is therefore provisionally rendered K^\bullet(Y), with a TeX provenance comment at lines 206–208. This remains pending Claude’s French-source adjudication.

A durable note was placed beside the French workpass:

    C:\IL_GitHub\00_main_current\sources\sga\sga6-claude-workpass-source-rescribe-20260704\HI_CLAUDE_CODEX_SGA6_NOTES_PREFIX014_141_150_20260718.md

The French TeX itself was not altered.

## Visual evidence

Full 240-dpi scan renders are in source_evidence:

- sourcePDF014.png and context pages sourcePDF013_context.png / sourcePDF015_context.png;
- sourcePDF141.png through sourcePDF150.png;
- sourcePDF014_formula_crop.png, an enlarged crop preserving the source-sic X-domain reading.

All full-page renders were visually inspected at original resolution. Page 149 was explicitly retained as the clean control.

## Residual ambiguity

The only unresolved textual judgment in this tranche is the source-sic domain X versus the mathematically typed domain Y on source-PDF 14. The English working edition uses Y transparently and marks it pending Claude. No ambiguity remains for the page-141–150 repairs.

## Build boundary

This subtask did not compile the whole reader, by assignment. The parent SGA 6 task will rebuild the complete layered edition and render the resulting English pages after integrating this fragment.
