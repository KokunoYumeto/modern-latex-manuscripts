# Project logbook methodology/replication DOI requirement

Date: 2026-08-02

Status: CONTROLLING archive-provenance requirement from Floris.

## Requirement

Every completed project or bounded publication handoff must include the
privacy-clean logbook surfaces that explain how the artifact was produced and
audited. This includes, as applicable:

- the chronological production logbook;
- per-decision normalization/correction rationales;
- append-only reversal and error history;
- exact authority/cursor and continuation handoff records; and
- the final identities and manifests needed to replay those records.

The archive/upload task must place these logbooks in **both** the methodology
DOI record and the replication DOI record. They need not be the first files
uploaded, and a record-size constraint may require a separately packaged but
exactly cross-linked archive object. They must not be omitted, retained only
on a private disk, or present only incidentally inside one unindexed source
bundle.

Every producer's handoff must bind the exact relative path, bytes, SHA-256,
privacy result, and supersession state of each logbook surface. The upload task
must return the corresponding deposited-file identity and public readback for
both DOI records when archive action is authorized.

Mutable or incomplete logbooks are not to be uploaded merely to satisfy this
rule. The producer first freezes a privacy-clean bounded or final snapshot;
the upload task then includes that exact snapshot. Later append-only changes
require an explicit successor, never silent replacement.

## Scope

This applies to the EGA, SGA, FAC, GAGA, Deligne, and related
interlanguage/transcription deliverables, including future successor packages.
It supplements rather than replaces source, privacy, rights, manifest,
publication, and readback gates.

## Coordination record

The requirement was relayed on 2026-08-02 to:

- replacement archive/upload task `<REDACTED_TASK_ID>`;
- production/management task `<REDACTED_TASK_ID>`; and
- production task `<REDACTED_TASK_ID>`.

The current EGA French producer records the requirement in its own logbook and
will bind immutable logbook identities only when a bounded/final archive
handoff is actually ready.

