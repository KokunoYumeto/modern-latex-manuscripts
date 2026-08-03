# FAC quality assessment: what happened and why this record exists

This record documents an accidental blind comparison between two English translations of Jean-Pierre Serre's 1955 article *Faisceaux algébriques cohérents* (FAC).

The project orchestrator did not know that Piotr Achinger and Łukasz Krupa had already translated FAC. They therefore asked an OpenAI Codex production session to translate the article from the French source. Codex had translated, compiled, and source-checked numbered units 1--79 before the orchestrator discovered the Achinger--Krupa PDF and, later, its editable source archive. That sequence was not planned as an experiment. Precisely because it was accidental, the already-frozen Codex work through no. 79 forms a useful held-out comparison: the external English could not have influenced its wording or formulas.

The project then compared all 79 blind-overlap units. Every disagreement was adjudicated from the French journal authority, not by majority vote between English versions. The comparison produced 79 unit reviews and 138 locator-bound findings. Twenty units showed substantive independent agreement without a material finding. Fifty-nine had at least one recorded difference worth discussing, ranging from harmless English variation to omitted hypotheses, symbol substitutions, lost indices, malformed maps, weakened wording, or TeX defects in the external lineage. None of the 138 findings required changing the already admitted Codex English or corrected French layer. That is a bounded result for this cohort, not a universal score.

The complete Codex English reader contains nos. 80--81 as well. Those two units were completed after the comparator was known and are explicitly excluded from blind-performance claims. The 74-page no. 79 reader is the chronology-bound blind artifact; the 78-page reader is the complete project translation.

## What this supports

This record is evidence that a carefully source-controlled contemporary model workflow can produce mathematically useful translation rather than opaque, unchecked prose. It makes the evidence inspectable: exact frozen inputs, unit-by-unit reviews, finding-level rationales, decision logs, self-corrections, source identities, and build artifacts are included.

The result is relevant when assessing the related SGA and EGA readers produced with the same source-first discipline. It gives a concrete reason to expect that those readers may be useful working tools, while still checking the original source for citation-critical or mathematically delicate passages.

## What this does not support

- No mathematician has peer-reviewed or certified the FAC translation.
- Neither English version is source authority.
- Agreement between translations does not prove correctness.
- This is not a critical edition, canonicity claim, benchmark leaderboard, or probability estimate.
- The 138 findings are heterogeneous and must not be read as a scalar quality score.
- Mistakes may remain. Important uses should keep the French authority beside the translation.
- The result does not prove that every other model, prompt, subject, or document will perform similarly.

## Who and what did what

- Jean-Pierre Serre's 1955 French article is the sole textual and mathematical authority.
- A French working transcription was initially produced in a Claude Opus 5 project lane, according to the orchestrator's provenance record. It remained a drafting layer and was subsequently checked and corrected against the journal authority.
- The English translation, source alignment, French correction layers, and blind comparison were produced in an OpenAI Codex 5.6 session using Ultra reasoning mode, according to the session/orchestrator record.
- The human orchestrator selected the work, discovered the external translation only after the no. 79 freeze, directed the comparison, and required append-only correction and rationale logs.
- The artifact hashes establish which bytes were compared. Hosted-model names and reasoning settings are project/runtime metadata; they are not cryptographically attested by the TeX or PDF bytes themselves.

## Recommended reading order

1. `00_READ_ME_FIRST.md` -- this short narrative and claim boundary.
2. `05_FAC_Quality_Assessment_Report.md` -- method, results, and interpretation.
3. `03_FAC_Blind_Comparator_Unit_Reviews.csv` -- one row for each blind unit.
4. `04_FAC_Blind_Comparator_Findings.csv` -- every selected/rejected reading and rationale.
5. `01_FAC_Codex_Blind_English_Reader_through_no79.pdf` -- the frozen blind artifact.
6. `02_FAC_Codex_Complete_English_Reader.pdf` -- the complete project English reader.
7. `07_FAC_Editorial_Decision_Logbook.md`, `08_FAC_Self_Correction_Ledger.csv`, and `09_FAC_Project_Logbook.md` -- the detailed provenance and adverse history.
8. `13_FAC_Blind_Comparator_Inventory.csv`, `14_FAC_Blind_Input_Identities.csv`, and `15_FAC_Blind_Comparator_Validation.json` -- the complete comparison universe and replay closure.
9. `16_FAC_Project_English_and_French_TeX_Source_Layers.zip` -- editable project source layers.

The Achinger--Krupa PDF and source are credited, URL- and hash-bound, but not redistributed because no explicit redistribution license was found in the acquired source tree.
