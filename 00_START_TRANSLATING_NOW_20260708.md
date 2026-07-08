# START TRANSLATING NOW - OTHER-PC SIDE BRANCH DIRECTIVE

Timestamp: 2026-07-08 13:54 Europe/Berlin

This file is for the other-PC coordinator and every visible sibling session.

## Non-negotiable instruction

Stop treating source-body collection, route visibility, and acknowledgement files as the main task.

The branch already contains enough source-body/provenance material to begin production translation work. From this point, the primary task is **translation output**.

Do not merely read or acknowledge this file. Set the goal below exactly, then produce translated TeX/PDF artifacts.

## Set this as the active pursued goal

Produce actual mathematical translation draft packages from the existing source bodies and canonical project sources. Each active session must select a concrete language/tranche, translate real mathematical prose into the assigned target language, preserve TeX math/formula/table/diagram structure, compile the result where possible, render-check it, and package the outputs with source-use notes, Fable/branch-weight terminology notes where relevant, SHA256 checksums, and a short human-readable status file. Source-body collection is now secondary and should happen only when a missing source blocks a specific translation tranche.

## What counts as output

An acceptable next output contains at least one of:

- translated `.tex` source for a named paper, section, or tranche;
- compiled translated `.pdf` reader for that tranche;
- cumulative translated TeX/PDF update for an existing language branch;
- a package ZIP containing translated TeX, PDF, source-use notes, terminology ledger, compile/render logs, manifest, and SHA256 checksums.

CSV-only route packets, acknowledgement files, visibility reports, branch comparison reports, and "state unknown" dispatch boards are not sufficient by themselves.

## Current priorities

1. Interslavic / Slavic mathematical translation repair and production.
   - Use Fable/ChatGPT-Pro weighted automaton and marginal-intelligibility ledgers.
   - Avoid dominance collapse into Russian or Ukrainian.
   - Produce usable mathematical TeX/PDF drafts, not only source-canon reports.

2. Slavic non-RU/UK branches.
   - Use the existing `language-source-bodies/slavic-non-ru-uk-20260705` and Slavic source-canon material.
   - Translate a concrete tranche and package it.

3. Russian/Ukrainian/Interslavic Noether branches.
   - If prior translations exist, repair them using current Noether German/source-control head and Fable constraints.
   - Do not claim native review or final status.

4. Other language-family branches only after they produce actual translation drafts.
   - CJK, Arabic/RTL, Persianate/Tajik, Romance/Germanic, Pan-Turkic, Indigenous/creole/sign, Malay/SEA/Pacific.
   - For each, pick one concrete tranche and return a compiled or compile-attempted package.

## Required package shape

Each translation package should contain:

- `README.md` with scope, source base, target language, exact continuation point, and caveats;
- translated `.tex`;
- translated `.pdf` if compilation succeeds;
- compile log, render check, or failure log if compilation fails;
- source-use note naming the exact source/canonical input used;
- terminology ledger or glossary delta;
- Fable/branch-weight note if the language is part of the interlanguage/Interslavic system;
- `MANIFEST.csv`;
- `SHA256SUMS.txt`;
- `SESSION_LOGBOOK_YYYYMMDD.md` or a logbook excerpt.

## Claim boundary

These are draft translation outputs. Do not claim:

- native/community review;
- accepted terminology;
- final language approval;
- full corpus completion;
- source-fidelity certification;
- publication readiness;
- critical edition status.

Do claim exactly what exists: translated draft TeX/PDF for the named scope, with source-use and terminology notes.

## Next commit rule

The next meaningful commit on `codex/noether-pc-20260629` should contain real translation payloads, not just another routing/status packet. If a session cannot translate because a source is missing, it must name the exact missing source and route that as a blocker, then move to a different tranche that can be translated now.
