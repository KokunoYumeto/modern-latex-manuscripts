# Noether German canon control

This is the small project-level source and editorial control root for the
Noether German working corpus. It does not contain CJK translation work and it
does not claim to be a critical or canonical edition.

## Start here

1. `CURRENT_GERMAN_AUTHORITY_POINTER.json`
2. `CURRENT_GERMAN_AUTHORITY_POINTER.sha256`
3. `ledgers/DECISIONS.jsonl`
4. `ledgers/DEC_DETAIL.jsonl`
5. `ledgers/SOURCE_VERSION_LINEAGE.jsonl`
6. `ledgers/DEFECT_INTAKE_ADJUDICATION.jsonl`
7. `ledgers/DEF_EVIDENCE.jsonl`
8. `manifests/UNIT_INDEX.jsonl`
9. `manifests/STRUCT.jsonl`

The current pointer always identifies one exact default translation authority.
Immutable historical pointer snapshots live under `pointers/`. A change to the
current pointer requires a new snapshot and an append-only decision; old
snapshots are never overwritten.

## Directory roles

- `published/zenodo/`: authenticated Zenodo originals, metadata, inventories,
  hashes, and publication audit.
- `published/github/`: exact GitHub public objects and public-package control
  records.
- `candidates/`: local editorial successors and superseded experimental
  branches. A candidate is not public merely because it compiles.
- `evidence/`: primary-source witnesses and bounded audit evidence.
- `units/`: immutable exact logical-span snapshots used by bounded translation
  binders.
- `receipts/`: machine-readable binder, return, and readback receipts.
- `build_logs/`: serial build outputs and focused visual QA.
- `ledgers/`: append-only decisions, lineage, defects, failures, and returns.
- `schemas/` and `templates/`: checker packets and governance/index controls.
- `manifests/`: recursive project-control hashes and structural indices.

## Reading layers

The project keeps these concepts separate:

- **diplomatic reading**: what the original print visibly says, including an
  original-print error;
- **later transcription**: what a subsequent TeX witness says;
- **editorial reading**: an accepted correction with exact source evidence;
- **tooling state**: line endings, packaging, build metadata, and transport;
- **target-language state**: a translation decision, which is not German source
  evidence.

No reading is silently erased. A correction appends an adjudication and an
exact successor edge.

## Finding intake

A translator observation is not a German source defect. Submit only a packet
that conforms to `schemas/CHECKER_CONFIRMED_FINDING.schema.json` after a second,
independent checker has confirmed, rejected, or marked the finding unresolved.
The German owner deduplicates by paper, exact cursor, authority-span hash, and
observed/proposed pair before adjudication.

## Publication rule

Resolve the Zenodo concept DOI and declared public GitHub paths before local
disk or Google Drive archaeology. Local or Drive objects become authority
candidates only after exact bytes/hash, parent lineage, evidence, compilation,
and publication state are recorded.

## Current working layer

As of pointer `NOETH-DE-AUTH-v009-20260804`, the default working authority is
`NOETH-DE-ED-0002`, 2,153,554 raw bytes, SHA-256
`C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3`.
It is a compiled local editorial successor, not a published critical edition.
Always read the live pointer rather than copying this prose into downstream
custody records; later metadata-only pointer versions may preserve the same
authority bytes.
