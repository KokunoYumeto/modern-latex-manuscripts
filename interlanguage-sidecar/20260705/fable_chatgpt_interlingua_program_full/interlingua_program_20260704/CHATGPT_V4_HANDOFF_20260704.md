# ChatGPT v4 round — handoff bundle
2026-07-04. Everything the next master-table/scores round needs, in one note. Files referenced are in the program folder / regenerate the zip on request.

## Corrections to carry into v4 (from my verification of your v3)
1. **Label/source-cue channel split at extraction time** (your v3 defect, my repair): ~25% of v3 label cells held sentence cues. v3.1_REPAIRED is the working master; V3_DEFECT_REPORT_FOR_CHATGPT has the root cause. For v4: a label is a lemma/citation form, never a sentence.
2. **Quotient-field forms**: corpus-internal ISV = `polje kvocientov` (p06/24/30 tex) + `kvocientno polje` (p09 tex, definitional footnote). The `polje častnikov?` placeholder is withdrawn everywhere. Your scores v3 already corrected this — keep.
3. **Over-stoplisting correction (accepted from you)**: proof connectives/modals are register vocabulary. proof_prose_lexicon_v2 (160 lemma groups, provenance-tagged) is the merged working lexicon — treat as the insertion ledger of record.

## New columns for the master table (native, dictionary-grade, concept-shelf level)
- **be (Belarusian)**: Minsk-1993 math dictionary; ring = кольца (51 compound entries); BNT-1922 historical context only (per its own lane_decision). → **East kolco-family coherence is 3/3 standards** (кільце/кольцо/кольца).
- **mk (Macedonian)**: UKIM trilingual lexicon; **MK_MARKER_COLUMN_v1_20260704.json = 39 core concepts decoded to Cyrillic** (прстен 172, множество 775, функција 911, количник 46, **поле на количници = quotient field**…). Legacy-font decode was mechanical (~ч {ш ж-backtick wњ) — spot-check the decoded lemmas before merge. 4 probe misses to look up in the lexicon text (noetherian, prime ideal, invariant, tensor product — cached txt on shelf).
- **hsb (Upper Sorbian): SOURCE DEFECT** — the "Domowina math terminology 2008" PDF is a publisher's catalog, not terminology; 1996 corpus PDF is a bibliography. hsb column stays EMPTY (honest gap); live leads: soblex, Serbski institut term databases.

## Consequences for scores v4
- **Ring row**: prsten coalition now **5 standards (pl+hr+sr+bg+mk)**, kolco-family = 3 East standards + community `koljce` entry (whose own W/S translation row is prsten-family) + Paper-25 internal prsten trace. Re-run the four weightings with mk in the South cohort; the dependence-corrected and equal-branch schemes will strengthen the coalition side; population weighting still favors East — sensitivity framing stands.
- **Quotient-field row**: add mk `количник / поле на количници` witness; West competitor evidence unchanged.
- Cohort model: add be to E (population ~9M L1-proxy — source-pin it), mk to S (~2M). hsb omitted (no witness).

## Insertion-grind state (for your parallel passes)
Coverage trajectory: 70.6 → … → 90.5% tokens / 61.5% types (lexicon 160; my per-pass deltas in STATUS). F13: the residue is variant scatter (obće/obču/vobče/voobče; mora/musi; togda/tada; pytanje/vprašanje…) — each lexicon group's variant list = a normalization decision for the review ledger. Suggested v4 grind: same backlog loop on YOUR stricter file set + a variant-normalization proposal table (lemma → preferred surface + variant policy), no promotions.
