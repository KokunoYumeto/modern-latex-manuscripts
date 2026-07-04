# READ THIS FIRST: Interlanguage / Interslavic Source-Bundle Directive

You are working in the interlanguage / Interslavic / multilingual Noether lane.

Do not return only a ledger, checklist, or prose summary when asked for source support. Return a source bundle containing actual source files.

Current required behavior:

1. Read the sidecar files in `interlanguage-sidecar/20260704/`.
2. Treat `Interlanguage_All_Downloaded_Source_Anchors_20260704.zip` as the current concrete source-anchor bundle.
3. Treat `claude_interlingua_program_20260704_full.zip` as the local Claude methodology/data bundle.
4. Treat `web_noether_pc_interlanguage_interslavic_outputs_20260704.zip` as the web/other-Codex branch output archive.
5. For every language or constructed-language lane you touch, maintain a per-lane source bundle with actual downloaded source files plus a manifest.
6. If a lane already has enough source files, stop source-mining and do translation/terminology/concordance work. If it does not, fetch source files until it has a useful native baseline.
7. Keep generated Interslavic/Russian/Ukrainian/other draft translations separate from independent source witnesses.

Minimum acceptable source bundle shape:

- `sources/<language-or-lane>/` with PDFs, TeX, HTML captures, or source archives.
- `MANIFEST.csv` with title, URL, fetched file path, byte count, SHA256, and status.
- `STATUS.md` saying what is source-authoritative, what is generated/internal, and what remains missing.

Immediate gap noticed by archive-maintenance Codex: the broad non-Russian/non-Ukrainian Slavic baseline has real PDF anchors for Czech, Polish, Slovak, Slovenian, Serbian, Croatian, and Bulgarian. The underrepresented branch currently has Belarusian/Macedonian/Sorbian anchors, but Macedonian still has a failed UKIM PDF URL that needs an alternate source or manual retrieval.
