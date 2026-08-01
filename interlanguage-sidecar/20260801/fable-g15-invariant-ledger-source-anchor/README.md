# Fable G15 invariant-ledger source anchor

## Purpose

The Fable interlanguage blocking directive requires archive maintenance to
locate `G15` / `15G` or record an exact failed search. The label is not the
name of a separate file. It is Gate 15 inside `INTERSLAVIC_GATE_MAP.md`.

This packet makes that existing source artifact directly discoverable without
requiring a reader to mine the 146 MB full-provenance archive. It does not
invent a replacement artifact or alter the archived Fable program.

## Exact source identity

- Public parent archive:
  `01_Claude_ChatGPT_Interlingua_Program_Full_Provenance_20260706.zip`
- Parent archive: 146,055,857 bytes
- Parent SHA-256:
  `2D587A77FCBDFB79EC949F8ED94B548CCAC2E311EB0990AB1E239945E9004A6B`
- Exact member: `INTERSLAVIC_GATE_MAP.md`
- Member: 7,691 bytes
- Member SHA-256:
  `E714C7A1EEED2DC5B3DD5C2F2AD9184521E14225B82DE1F9E563D1F93987A6F7`

The parent archive was already public in the Interlanguage Zenodo lineage
before this direct anchor was created. The copy in this packet is extracted
byte-for-byte from that canonical member.

## What G15 means

`INTERSLAVIC_GATE_MAP.md` identifies G15 as the invariant-ledger gate. It
requires the `INV-*` handoff table to cover script conversion and register
operations, with the existing script validator serving as the test for the
script invariant.

G15 therefore names a methodological gate, not a missing language corpus,
translation body, standalone ledger, or source document.

## Search and reconciliation

The reconciliation searched by filename and bounded text token across the
canonical unpacked Fable tree, the Interlanguage workspace, project chat-note
records, and Codex text records. No standalone file named `G15` or `15G` was
present.

Archive-member replay then opened 41 Fable/interlanguage ZIP candidates and
scanned 10,165 text members totaling 406,521,901 uncompressed bytes. It found
24 bounded `G15` references, all belonging to versioned copies of the same
gate map or indexes/status files describing that map. No ZIP member was named
`G15` or `15G`.

The result is therefore `FOUND_AS_GATE_IN_EXISTING_ARTIFACT`, not
`NOT_FOUND`. No not-found placeholder is warranted.

## Claim boundary

This packet resolves the identity and location of one Fable methodology
anchor. It does not claim that every `INV-*` row has been implemented, that
the global interlanguage ledgers are complete, or that any generated language
form has native-speaker or community approval.
