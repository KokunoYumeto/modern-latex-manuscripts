# Noether Source Canon Priority One Ledger

Generated UTC: 2026-07-04T16:40:40Z

Status: global steering ledger for source-canon acquisition and publication. This is not a translation, glossary, term ledger, bridge approval, review completion, pilot, or canonical edition.

## Priority Rule

Every language, standard, script, register, comparator, and constructed-language stream in the relevant Noether cluster must start with source canon before method output, translation output, glossary work, bridge construction, or reviewer authority claims.

Preferred witness order:

1. Source TeX, LaTeX, source repository, arXiv source bundle, e-print source archive, or equivalent editable source package.
2. Publisher, project, institutional, or author source archive with version and license signal.
3. PDF with stable URL, bibliographic provenance, page anchors, extraction state, local hash, and explicit note that editable source was not found.
4. DOCX, HTML, plain text, OCR text, scan, or manual transcription only when source/PDF witnesses are not available.
5. Metadata-only rows only as explicit source gaps, never as authority.

No lane may treat a row as ready for method construction or translation routing unless the source-canon record includes, or explicitly marks as missing:

- original URL or archival locator;
- source type and witness rank;
- license signal or license gap;
- local path for captured files;
- SHA-256 hash for captured files;
- version, publication date, retrieval date, or archive timestamp when available;
- page, theorem, section, or source-anchor fields when a usage claim depends on a location;
- extraction/render state;
- topic tags derived from the witness metadata or section, not invented from the route name;
- explicit gaps and rejected candidates.

## Publication Minimum

Source-canon publication for a lane must include:

- a source manifest in `.md` and `.json`;
- local captured source paths where allowed;
- hash index for every captured file;
- license and redistribution signal for every source row;
- URL and archival locator list;
- topic tags and page/section anchors;
- explicit source gaps;
- rejected-candidate table;
- no authority claim beyond source provenance.

## Global No-Go

- No accepted bridge surfaces.
- No promoted terms.
- No native, community, project, teacher, or learner consent claim.
- No external-review completion claim.
- No pilot readiness claim.
- No canonical translation or canonical edition claim.
- No Git push from this lane.

## Route Source-Canon Ledger

| Source-canon ID | Owner | Route IDs | Language/stream cluster | First source witness target | Required first output | Current gap to record |
| --- | --- | --- | --- | --- | --- | --- |
| SC-L-001 | Session L | L-001, L-002 | Interslavic/Panslavic; Slavic triangulation controls | Interslavic project/source documents, Slavic control witnesses, Latin/Cyrillic sidecar sources | `SESSION_L_SOURCE_CANON_MANIFEST_<timestamp>.md/json` | external/native review open; do not use controls as Interslavic authority |
| SC-ROM-001 | Romance split lane | ROM-001, ROM-002, ROM-003 | Pan-Romance, Neolatino/Romanica-style evidence, French/Spanish controls, fallback Romance rows | Romance source TeX/PDF/project archives per language or standard; French/Spanish control sources separated from bridge sources | `ROMANCE_SOURCE_CANON_MANIFEST_<timestamp>.md/json` | fallback rows and project math-literature gaps must be explicit |
| SC-E-001 | Session E / CJK split | E-001, E-002, E-003 | Simplified Chinese, Japanese, Korean-adjacent/CJK/Japonic/Koreanic source addendum | Chinese/Japanese source baseline files and Korean-adjacent exact source-status records | `CJK_SOURCE_CANON_BASELINE_<timestamp>.md/json` | no public signoff claim; no active Korean-school project without direct source |
| SC-F-AR-001 | Session F / Arabic split | F-AR-001, F-AR-002 | Controlled Technical Arabic and RTL/script governance | Arabic TeX/source/PDF witnesses, RTL render sources, script policy sources | `ARABIC_RTL_SOURCE_CANON_MANIFEST_<timestamp>.md/json` | exact sources and specialist reviewer route remain open |
| SC-F-PER-001 | Session F / Persianate split | F-PER-001, F-PER-002, F-PER-003, F-PER-004 | Farsi/Persian, Dari, Tajik Cyrillic, Persianate shared-register candidate | Separate fa_IR, prs_AF, and tg_Cyrl_TJ source witnesses; shared-register source only as research evidence | `PERSIANATE_PER_STANDARD_SOURCE_CANON_<timestamp>.md/json` | do not collapse Farsi, Dari, and Tajik authority |
| SC-G-001 | Session G | G-001, G-002, G-003 | Malay-Indonesian, Brunei/Singapore/DBP/MABBIM, Philippine/Tai/Hmong-Mien/Austroasiatic/Vietnamese/Khmer/Mon/Santali/Munda rows | Per-standard source archives, exact local content, reviewer-return source paths, weak-row retry sources | `MALAY_SEA_PACIFIC_SOURCE_CANON_<timestamp>.md/json` | title-only and weak rows remain gaps |
| SC-H-001 | Session H | H-001, H-002 | Hausa, Amharic, Afar, Somali, Oromo, Tigrigna/Tigrinya, Fulfulde, Mandinka, Akan/Twi, Wolof, Yoruba, Igbo | OCR/Unicode-ready source witnesses, variant-specific source ledgers, local script/source paths | `AFRICA_HORN_WEST_SOURCE_CANON_<timestamp>.md/json` | no pan-African, Manding, Akan, or West African bridge authority |
| SC-I-001 | Session I | I-001, I-002, I-003 | Indigenous, Creole/contact, and Sign access rows | Local source maps, accessibility/visual source witnesses, creole/Indigenous provenance and rejection records | `R6_ACCESS_SOURCE_CANON_<timestamp>.md/json` | access ethics and reviewer routes precede lexicon or pilot work |
| SC-J-001 | Session J | J-001, J-002, J-003 | Pan-Turkic hard rows, Common Turkic Alphabet, Ortaturk/Ozturkce-type proposals | Exact source retry witnesses for blockers, alphabet/script institutional sources, proposal corpus evidence | `PAN_TURKIC_SOURCE_CANON_BLOCKER_LEDGER_<timestamp>.md/json` | hard blockers prevent bridge work |
| SC-K-001 | Session K | K-001, K-002 | OLP/OpenTranslation relation/function support and reviewer forms | Slot-return source files, relation/function form sources, review-return provenance with zero defaults | `OLP_SOURCE_CANON_SLOT_RETURN_LEDGER_<timestamp>.md/json` | approval counts remain zero without real returns |
| SC-D-AUX-001 | Session D NOVEL/OWNERLESS | D-NOVEL-001 | Interlingua, Interlingue/Occidental, Elefen/LFN, Esperanto, Ido, Novial, Latino sine flexione, Latin | Project/source archives, math-register source witnesses where available, explicit comparator gaps | `NOVEL_AUXLANG_SOURCE_CANON_EXPANSION_<timestamp>.md/json` | current shelf is comparator-only and lacks full source-canon fields |
| SC-D-WORLD-001 | Session D NOVEL/OWNERLESS | D-NOVEL-002 | Pandunia and Globasa | Project source archives, versioned project docs, source-level math-register evidence or explicit gap | `NOVEL_WORLDLANG_SOURCE_CANON_EXPANSION_<timestamp>.md/json` | project URLs are not consent, review, or pilot readiness |
| SC-D-CTRL-001 | Session D NOVEL/OWNERLESS | D-NOVEL-003 | Controlled mathematical register | Source-fidelity proof grammar source anchors and child-lane source opt-in records | `CONTROLLED_REGISTER_SOURCE_CANON_CHECKLIST_<timestamp>.md/json` | method layer only; no community language representation |
| SC-D-COMP-001 | Session D NOVEL/OWNERLESS | D-NOVEL-004 | Computational interlingua / MT pivot | Corpus source manifests, model/tool provenance, alignment source paths, generated-text quarantine hashes | `COMPUTATIONAL_PIVOT_SOURCE_CANON_PROTOCOL_<timestamp>.md/json` | tooling output has no human language authority |
| SC-D-ACCESS-001 | Session D NOVEL/OWNERLESS | D-NOVEL-005 | Access-gain/intercomprehension method | Child-lane source manifests before access-gain scoring, local source maps, rejection/fork paths | `ACCESS_GAIN_SOURCE_CANON_WORKSHEET_<timestamp>.md/json` | no local-need or community-benefit claim without local source/review route |
| SC-D-QUAR-001 | Session D NOVEL/OWNERLESS quarantine | D-NOVEL-006 | Broad world-family bridge target index | Route-out source evidence per orphan row; quarantine source-gap records | `CROSS_FAMILY_SOURCE_CANON_QUARANTINE_LEDGER_<timestamp>.md/json` | no cross-family bridge surfaces |
| SC-CORR-001 | Correction record only | D-CORR-001 | SGA5 and Korean-school overfocus correction | Direct source evidence only if a new active lane is asserted | `SOURCE_CANON_FALSE_LEAD_CORRECTION_<timestamp>.md/json` | no resurrecting a stream from memory, method interest, or indirect mention |

## Continuation Rule

Future lane work should pick the first row in this ledger whose required source-canon output is missing or incomplete. Method/checklist artifacts may support source capture, but they do not outrank source-canon acquisition and publication.
