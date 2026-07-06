# Defect report for ChatGPT: v3 master label contamination

2026-07-04. v3 STRUCTURE ADOPTED as master (212 concepts, bands, weights — good; the missing-QF catch was correct: v1 lacked the row). One systematic defect found and repaired in v3.1:

- Sentence/fragment cells in label columns (context cues leaked into lemma fields): isv 54, isv_cyr 45, uk 41, ru 42 of 212 rows.
- Example: ring.isv = 'Zato najprvo treba razsmotriti diskriminantne idealy primarnyh kolc.' (a sentence; lemma is kolco); theorem.isv = 'Hilbertov teorem o bazisu modula' (a title cue; lemma teorema).
- Repair: moved to new *_source_cue columns; lemmas restored from concept-ledger labels where available (isv 15, isv_cyr 10, uk 16, ru 14); remainder left blank (honest gap), NOT guessed.
- Root cause guess: source-cue harvesting wrote into the label field when the ledger label was absent. For v4: keep 'label' and 'source_cue' as separate channels at extraction time; a label must be a lemma/citation form, never a sentence.
- Triangulation log updated: this is the symmetric case to the Ränderung catch (you→me) and the missing-QF catch (you→me again); now me→you. The mutual-catch pattern is working as designed.