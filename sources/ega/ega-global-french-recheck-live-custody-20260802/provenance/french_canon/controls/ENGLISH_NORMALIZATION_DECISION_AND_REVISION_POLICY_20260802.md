# EGA English normalization decision and revision policy

Date: 2026-08-02

Status: CONTROLLING for all remaining EGA French transcription and English
source-alignment work in this corpus.

## Rule

The French TeX is diplomatic: it records the bounded NUMDAM printing, including
source typos, without silently correcting it. The English may depart from that
printing only when the departure is individually justified. Translation order
does not matter; the terminal French and English artifacts must both be
canonical within their declared roles.

Every intentional English departure from the printed French must have one
stable, authority-bound decision record. A record is incomplete unless it
states:

1. the NUMDAM authority SHA-256, physical PDF page, printed page, and exact
   French locus;
2. the affected English source path, source identity, and exact prior wording;
3. the final English wording or the explicit decision to make no change;
4. the decision class: translation, grammatical normalization, notation
   normalization, mathematical/source correction, official erratum/addendum,
   or rejected candidate;
5. a short mathematical or linguistic rationale explaining why the departure
   is warranted;
6. whether a visible source note is required and whether it is present;
7. the complete set of standalone and cumulative English sources affected;
8. the initial judgment, final judgment, current status, and any predecessor or
   successor decision ID.

Routine idiomatic translation does not require a source-error note, but a
functional disagreement with the author or printed source does. Ambiguous
cases fail closed until the authority image and mathematical context decide.

## Reversal and error rule

No admitted decision may be erased or rewritten silently. If later evidence
shows that a decision was wrong, append a successor record that:

- names the superseded decision;
- says exactly what was wrong and why;
- records when and how it was caught;
- distinguishes a lead error, inherited error, rejected pre-admission
  candidate, and tooling/workflow error;
- identifies every affected source copy; and
- records the global repair and replay closure.

A reversal is not closed merely because one TeX file was edited. It is closed
only after every active standalone and cumulative English source carrying the
decision has been repaired, rebuilt where necessary, and identity-checked.
The diplomatic French remains unchanged unless the issue is a transcription
error relative to NUMDAM.

## Existing per-instance evidence and exact baseline

`ENGLISH_CORRECTION_RECHECK.csv` is the current per-instance rationale annex.
It contains 117 data rows through EGA I printed page 68. A direct CSV-field
replay, taking the final field as status for the five rows with an unquoted
comma in the rationale, gives this exact disposition split:

- 91 confirmed English translation/transcription/grammar/mathematical errors;
- 21 confirmed French source issues whose English disposition is individually
  reasoned;
- 2 official EGA II erratum/addendum decisions; and
- 3 external erratum additions absent from the bounded NUMDAM EGA I body and
  still requiring a separately bound authority.

Within those 117 rows, 10 decisions are presently marked as formally
source-justified (`JUSTIFIED`): eight French-source correction/normalization
decisions and two official erratum/addendum decisions. Thirteen additional
French-source correction/normalization rows remain pending a no-overwrite
English successor and/or visible-note closure. These status counts are not a
claim that all required mutations have already been applied.

`ENGLISH_CORRECTION_RECHECK_MASTER_QUEUE.csv` has 60 rows: 54 substantive
source readings still pending direct NUMDAM recheck and six structural
no-edit replay rows. The queue and the 117-row admitted ledger may overlap;
they must not be added together as a corpus-wide edit count.

The 117-row file is not strict RFC-style CSV in five rows because an unquoted
comma splits the rationale field. The historical file is preserved unchanged.
Any machine-facing successor must quote every field, preserve all stable IDs
and exact text, record reciprocal supersession, and replay 117/117 before it
becomes controlling.

## Known decision-error baseline

At this checkpoint:

- admitted English source-correction decisions later reversed: **0**;
- proposed mathematical correction candidates rejected before admission:
  **1** (the proposed 5.4.6 `m/n` exponent change; exact replay showed that the
  English already printed the source-correct exponent `m`);
- inherited non-diplomatic French normalizations reversed during authority
  replay: **2** (`A Oscar Zariski` and `A titre informatif`; these were in the
  inherited seed, not admitted lead decisions); and
- lead mathematical correction reversals known but not yet structurally
  logged: **0**.

The older logbook records several caught page-selection, source-placement,
rendering, and build-command errors, but it was not originally normalized into
a countable error taxonomy. Therefore no invented exact all-workflow-error
total is asserted. From this policy onward, every such incident receives an
append-only classified entry in `LOGBOOK.md`; any source-affecting incident
also receives a stable decision/revision record.

The known baseline instances have these stable IDs:

- `EG-EGA-FR-INTRO-A-OSCAR-INHERITED-NORMALIZATION-REV-001`: the inherited
  seed accented the printed capital `A` in `A Oscar Zariski`; direct authority
  replay restored the diplomatic source. This is an inherited deviation, not
  an admitted lead correction.
- `EG-EGA-FR-INTRO-A-TITRE-INHERITED-NORMALIZATION-REV-001`: the inherited
  seed accented the printed capital `A` in `A titre informatif`; direct
  authority replay restored the diplomatic source. This is an inherited
  deviation, not an admitted lead correction.
- `EG-EGA-I-P51-546-M-N-CANDIDATE-REJECTED-001`: a proposed exponent change
  was rejected before admission because exact replay showed that the current
  English already prints the source-correct
  `s_m\in\Gamma(X,\mathcal L^{\otimes m})`. No source mutation was made.
- `EG-EGA-CONTROL-CSV-UNQUOTED-COMMA-001`: five historical rationale rows are
  non-RFC CSV because an unquoted comma produces a fifteenth parsed field.
  The mistake was caught before reporting status counts, affects control
  serialization only, and does not alter any mathematical disposition.

These numbers are a checkpoint, not a final corpus total. They must be updated
as each new French range is transcribed and its English parallel is replayed.
