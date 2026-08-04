# CJK Korean production lessons — evidence input for methodology synthesis

## Scope and evidence boundary

This retrospective covers Korean production of the complete Noether Paper 27 notice, `Hilbertsche Anzahlen in der Idealtheorie`, on 2026-07-18. The target was Korean (`ko-KR`, Hangul-first); the source was German. The controlling source was the sealed P31 cumulative TeX, SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`, at lines 14192-14200 and journal printed p. 101. The printed-page witness hashes to `B00824115997D651F5EAB48420D05E6E0E6D7DF0AAC2CCD69E0836B033BFD8EC`.

The evidence package is at `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718`. It contains editable German/Korean TeX, compiled PDFs, build logs, rendered PNGs, source and render checks, terminology/adverse ledgers, a Korean evidence slice, typed graph, CJKV crosswalk, decision JSON, manifest, and hashes. This retrospective does not treat internal model review as human or external validation.

## What materially worked

### Exact authority pinning before translation

Pinning an exact file, hash, and line cursor prevented three kinds of drift: using older R823 material, silently promoting the newer but unsealed `C2439618...` working candidate, or trusting the shared authority pointer that remained stale at R821. A byte comparison showed that the sealed and working candidates had identical P27 spans, so the later candidate could be used as a survival check without overstating its authority.

Transferable result: authority should be represented as `(path, hash, source coordinates, seal state)`, not a revision nickname alone. A shared pointer is convenient only after a freshness check.

### Complete-unit gating

Selecting the complete one-page P27 notice made it possible to satisfy every acceptance gate without presenting an excerpt as a work. Paper 28 was live when selection occurred and was therefore left untouched. The unit produced one editable Korean TeX and one one-page A4 PDF rather than stopping at translated prose.

Transferable result: choose the smallest complete non-colliding source unit, not simply the next ordinal number or the shortest arbitrary span.

### Independent internal review before final hashing

The first Korean draft weakened German `das Äquivalent für` to a generic “corresponding object.” A separate internal Korean review identified this as the only substantive fidelity defect and prompted the correction to `표현에 상응하는 대체물을 이룬다`. The corrected TeX was then rebuilt, re-extracted, rerendered, and reinspected before hashes were sealed.

Transferable result: an independent pass should occur before the immutable-hash step and should compare propositions and relation strength, not only terminology or fluency.

### Channel-separated terminology evidence

Exact Korean witnesses, near evidence, absence, adverse evidence, and vetoes were kept distinct. For example, `힐베르트 다항식` was classified as near Hilbert-family evidence, not support for `Hilbertsche Anzahlen`; group-theory `잉여류` was treated as near-context evidence for ideal residue classes; Chinese and Japanese forms were vetoed as Korean authority. This allowed `힐베르트 수` to remain usable with a visible German control while honestly retaining `held` status.

The final crosswalk contains 13 rows and all 18 required fields. Sense windows, excluded senses, trap classes, qualitative Mandarin-Simplified dominance debt, and provisional attractor basins were stored outside the typed JSON schema. This kept the operational decision JSON schema-valid while preserving additional CJKV controls.

Transferable result: semantic/evidentiary channels and transmission-history labels must remain separate. Neither near evidence nor a dominant neighboring standard should silently acquire support weight.

### Build plus extraction plus rendered-page QA

The acceptance build used two XeLaTeX passes. Final log scans found zero fatal errors, undefined controls, missing characters, overfull/underfull boxes, or font warnings. Korean PDF extraction returned 807 characters with zero U+FFFD replacement characters and zero U+25A1 square boxes. Both PDFs were rendered at 180 dpi to 1489 × 2105 PNGs and visually inspected at original resolution.

Transferable result: successful compilation is only one gate. Text extraction catches encoding/glyph failures, while rendering catches clipping, overlap, bad page boundaries, and visually unreadable mathematics.

### Machine-verifiable package integrity

The final sweep checked 27 manifest rows, 26 hash entries, JSON parsing, decision-schema validity, 47 graph nodes, 46 graph edges, duplicate IDs, unresolved endpoints, CSV parsing, required crosswalk fields, controlled basin values, and source-hash length. It passed with no missing manifest file, hash mismatch, duplicate node, unresolved edge, malformed source hash, or empty required crosswalk field.

Transferable result: the deliverable should end with a single reproducible integrity run that joins artifact existence, hashes, schema checks, graph referential integrity, and build diagnostics.

## What failed or caused rework

### Remembered coverage was not evidence

The remembered claim “Korean through Paper 28” was not supported by recovered files. Before new production, only Papers 26 and 36 were verified. Treating memory as a cursor rather than coverage prevented a false completeness claim.

Supported cause: the statement had not been tied to durable artifacts. General lesson: corpus coverage must be derived from files plus unit status, never recollection alone.

### No formal tranche-claim mechanism existed

Paper 28 was actively changing during the collision audit, while the registry had no owner, lease, or timestamp columns. The collision was avoided through live filesystem inspection, but that is fragile and requires repeated checking.

Supported cause: coordination state was descriptive rather than transactional. Recommended fix: add an append-only unit-claim ledger with work unit, language, source hash, session/owner, opened time, status, and closure evidence.

### Initial evidence records contained referential defects

The first evidence slice contained a 63-character SHA-256, the terminology ledger linked `다항식환` to unrelated evidence rows, and the initial graph left an adverse `특성 함수` node disconnected. Later review also exposed mismatched adverse IDs for generating function, irreducible components, and finite order. These defects did not corrupt the Korean text, but they made the provenance graph unreliable until corrected.

Supported cause: records were composed before a cross-file referential validator existed. Recommended fix: validate that every evidence ID resolves to the correct ledger row and concept, not merely that JSON and CSV parse.

### The first TeX preflight failed

Both standalone documents initially lacked the package defining `\mathfrak`. Adding `amssymb` fixed the failure, after which two-pass builds were clean.

Supported cause: the standalone extraction removed dependency context supplied by the cumulative source. This is not a translation failure. Transferable fix: compile the source-control skeleton before translation and compare its preamble against the last clean language template.

### Tool and patch assumptions created avoidable friction

- A guessed Korean corpus subdirectory was wrong; `rg --files` located the actual file.
- Bundled Python did not include `jsonschema`; PowerShell `Test-Json` provided schema validation, while Python handled graph/CSV checks.
- One oversized multi-file patch failed because a manifest line lacked a patch prefix. Smaller patches then succeeded.
- After the logging directive arrived, two attempts to send a corrective follow-up to archive maintenance returned `dynamic tool request failed`. The earlier P27 handoff had succeeded, and the handoff note was corrected locally, but delivery of that correction was not proved at that moment.

Supported causes: unverified path assumptions, undeclared runtime dependencies, an overly large manual patch, and transient connector/tool availability. Heuristic: discover paths first, preflight validator availability, keep patches reviewable, and retain a durable outbound-notification queue or retry condition.

### Decision logging began too late for exact historical timestamps

The meticulous logging directive arrived after the P27 handoff. The durable log could reconstruct choices, evidence, and consequences, but not exact decision minutes without inventing them. Entries therefore record the honest date and label themselves retrospective.

Supported cause: the earlier workflow treated the summary table and unit artifacts as sufficient. Methodology change: open the detailed decision entry when a choice is made, then append evidence and disposition before hashing or handoff.

## Non-generalizable local details

- P27 happens to be a one-page notice and is byte-identical between the sealed and newer working heads. That should not imply that short notices are generally safer or that later candidates can usually be ignored.
- Malgun Gothic, Noto Serif Italic, MiKTeX 26.5, and the local Poppler binaries were available on this Windows machine. Other environments need their own font and toolchain checks.
- The Hangul/Hanja and South-/North-Korean boundary is specific to Korean. Other lanes need analogous local-standard policies, not copies of these surface choices.
- `힐베르트 수`, `으뜸 아이디얼`, and the selected attractor-basin labels are work/language decisions, not universal terminology doctrine.
- The stale R821 pointer and exact P31/C243 hashes are temporary repository facts, not permanent workflow constants.

## Concrete methodology changes recommended

1. Add a mandatory pre-unit authority record containing exact path, hash, line/page cursor, seal state, and shared-pointer freshness.
2. Add an append-only tranche-claim ledger and require a claim/collision check before editing.
3. Start a detailed decision record at choice time; require classification as source fact, computation, editorial inference, model preference, or human/external validation.
4. Add a cross-file evidence validator that checks ID existence, concept match, channel consistency, hash format, and graph connectivity.
5. Compile the standalone source skeleton before translation to expose missing cumulative macros/packages.
6. Require an independent fidelity pass before final hashes, followed by rebuild, extraction, rerender, and reinspection after any accepted change.
7. Keep CJKV sense windows, dominance debt, and attractor basins in a schema-compatible crosswalk unless the shared schema is formally revised.
8. Make archive handoff validation reject notes lacking a decision-log path and latest relevant decision ID.
9. Add a durable outbound-handoff queue with attempted time, connector result, retry condition, and eventual acknowledgment.
10. Define corpus completeness as a set of file-backed closed units against a named authority, never as a remembered “through Paper N” statement.

## Open questions and remaining failure modes

- Will a Korean historical-algebra reviewer accept `힐베르트 수`, `잉여류체`, `기약 성분`, and `유한 오더`, or require different forms?
- What DPRK/North-Korean mathematical terminology and Hanja practices apply? No authoritative corpus was recovered.
- Does the provisional lexical-attractor classification remain stable under historical lexicographic evidence?
- Can the shared German-authority pointer be refreshed atomically so every lane observes the same sealed head?
- Will the proposed claim ledger prevent simultaneous edits under actual parallel load, or is a filesystem lock/transaction also needed?
- Can archive-maintenance messaging provide durable delivery acknowledgments and retry semantics rather than a successful call being the only proof?
- Do render checks need a second human/typesetter pass for publication-critical typography even when model visual QA and extraction pass?

## Structural reproducibility and hard-part artifacts

The complete P27 source/target structure is now represented by a hierarchical JSONL authority rather than inferred from PDF appearance or paragraph counts alone:

- Structural index: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\structural_index\STRUCTURAL_INDEX.jsonl`
- CSV projection: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\structural_index\STRUCTURAL_INDEX.csv`
- Schema: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\structural_index\STRUCTURAL_INDEX.schema.json`
- Coverage metadata: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\structural_index\STRUCTURAL_INDEX_METADATA.json`
- Validator: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\structural_index\validate_structural_index.py`

Latest structural ID: `NOE-P27-KO-MATH-005`; index authority ID: `NOE-P27-KO-STRUCTURAL-INDEX-001`. Validation returned 20 records with exact expected type counts, 20 matching CSV rows, and zero hierarchy, relation, artifact-hash, fragment-hash, locator, or projection errors. Formal per-record JSON Schema validation returned 20 valid and zero invalid records.

The structural pass exposed a methodological point that ordinary sentence counts would have hidden: one German sentence is legitimately realized as two Korean sentences. The index therefore records German main and subordinate clauses separately as `NOE-P27-KO-CPU-005` and `NOE-P27-KO-CPU-006`, with actual one-based character spans and hashes. A first global-prefix search for repeated Korean `이 수들은` selected the wrong occurrence and produced an empty/overlapping span. Sequential search plus explicit clause-to-sentence boundaries resolved it. Transferable lesson: source-target parity is a relation among units, not an expectation of equal counts.

The separate append-only difficulty authority preserves resolved and unresolved failures:

- Difficulty ledger: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\difficulty_ledger\DIFFICULTY_LEDGER.jsonl`
- CSV projection: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\difficulty_ledger\DIFFICULTY_LEDGER.csv`
- Schema: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\difficulty_ledger\DIFFICULTY_LEDGER.schema.json`
- Validator: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\difficulty_ledger\validate_difficulty_ledger.py`

Latest difficulty ID: `CJK-KO-P27-HARD-010`. The ledger has ten entries: five resolved, four workaround, and one held. Its validator returned ten matching CSV rows, resolved structural references, and zero errors; formal schema validation returned ten valid and zero invalid records. Particularly transferable hard-part records are `HARD-003` (standalone TeX dependency loss), `HARD-004` (semantic relation weakening), `HARD-005` (parse-valid but semantically wrong evidence links), `HARD-006` (non-isomorphic sentence boundaries), `HARD-009` (unproved external delivery), and `HARD-010` (lost timestamp precision from late logging).

The remaining index limitation is explicit: P27 contains no theorem, proof, display, diagram, table, or note. Five important inline formulas are indexed as equation units. Longer papers may require explicit many-to-many correspondence edge records when paragraphs, proof steps, or displays split or merge across languages; the current paired-unit model must not be generalized beyond what its metadata declares.

## Durable decision references

Primary append-only log:

`${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\CJK_DECISION_LOGBOOK_20260718.md`

Relevant IDs:

- `CJK-KO-P27-001`: non-overlapping complete-unit selection.
- `CJK-KO-P27-002`: exact sealed authority and stale-pointer handling.
- `CJK-KO-P27-003`: Korean script/standard and held terminology policy.
- `CJK-KO-P27-004`: final-clause fidelity correction.
- `CJK-KO-P27-005`: TeX dependency repair and acceptance QA.
- `CJK-KO-P27-006`: sense-window, dominance-debt, and attractor controls.
- `CJK-KO-P27-007`: bounded public payload and archive handoff.
- `CJK-KO-P27-008`: corrective archive-notification delivery failure and retry condition.
- `CJK-LOG-001`: adoption of meticulous append-only decision logging.
- `CJK-METH-001`: creation, validation, and routing of this lessons-learned evidence input.
- `CJK-KO-P27-009`: structural-index and append-only difficulty-ledger creation and validation.
- `CJK-METH-002`: lessons-file correction after adding reproducibility artifacts and hard-part findings.

These raw lessons are methodology evidence, not automatically public doctrine. Archive maintenance should sanitize private operational paths and internal identifiers before any public synthesis.

## Visual evidence, preservation, and rights separation

The P27 lane now has a schema-documented canonical visual authority rather than treating rendered PNGs and the source scan as disposable QA by-products:

- Canonical JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.jsonl`
- Canonical schema: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.schema.json`
- CSV projection: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.csv`
- Public-safe JSONL and schema: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\visual_evidence\VISUAL_EVIDENCE_PUBLIC_SAFE.jsonl` and `VISUAL_EVIDENCE_PUBLIC_SAFE.schema.json`
- Private-root manifest: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\visual_evidence\RIGHTS_BLOCKED_SOURCE_ROOT_MANIFEST.csv`
- Validator and report: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\visual_evidence\validate_visual_evidence.py` and `VISUAL_EVIDENCE_VALIDATION_REPORT.json`
- Public payload candidate: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper27_ko_tranche_001_20260718\evidence\visual_evidence\KO_NOETHER_P27_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip`

The canonical index has three records, ending at `VE-NOE-P27-KO-003`: one full GDZ source page and two project-generated target/control renders. Custom validation checked actual hashes, bytes, JPEG/PNG dimensions, bounding boxes, linked TeX/PDF hashes, structural-ID resolution, source-root totals, CSV/public projection parity, and disposition totals with zero errors; both JSONL forms also passed formal per-record schema validation. The open payload has two images totaling 494,873 bytes. The exact private source root contains three JPEGs totaling 8,895,904 bytes; only its P27 image was used in this lane.

The hard part was not image conversion but avoiding a false binary choice between discarding evidence and publishing pixels without permission. No documentary redistribution basis was recovered for the GDZ JPEG. Omitting it was rejected because the source page was genuinely used; assuming permission from age or accessibility was also rejected. The adopted workaround preserves the binary at its exact private root and publishes only safe filename/hash/dimension/DPI/page-coordinate/structure/QA metadata. This is recorded as held difficulty `CJK-KO-P27-HARD-011` and decision `CJK-KO-P27-010`.

Transferable heuristic: rights uncertainty controls publication disposition, not preservation. Every used visual still needs a stable identifier and reproducible relation to its parent and target; only the payload layer changes. A validator should also search public metadata for private-path leakage and verify that every `manifest_only_rights_blocked` record has `binary_included=false`. This method does not itself determine copyright status and is therefore not a substitute for archive or legal review. External Korean visual review also remains open.

## Delivery-state lesson after connector recovery

The earlier three connector failures remain evidence under `CJK-KO-P27-HARD-009`; they were not erased after a later successful call. The visual-evidence notification returned the exact archive target thread ID and is recorded as recovery `CJK-KO-P27-HARD-012` and decision `CJK-KO-P27-011`. What worked was requiring a machine-returned target identifier and already having a durable local outbound record. What failed was treating connector availability as stable. The transferable rule is to distinguish four states—local handoff prepared, delivery targeting evidenced, archive review acknowledged, and package incorporated/published—and never collapse one into the next. The current evidence proves only the second state.

## Paper 29 U01 evidence supplement — finite-generation ambiguity, typed parity, and rights-separated visual archive

### Scope and authority

This supplement covers Korean Noether Paper 29 unit `P29-KO-U01`: the title, publication/author apparatus, and complete introduction at exact full-Paper-29 source lines 1--24, through the boundary before `§ 1. Das Endlichkeitskriterium`. The controlling sealed P31 authority remains SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`; exact LF-normalized U01 German source is 3,933 bytes, SHA-256 `3C0A6DF0150F21977FA8FA7814C5B7D1761CE90A3A6C127AF532E110DE62AF09`. The accepted Korean TeX is SHA-256 `1781D71A7B4EE1643E402E72A0D9604D2DDA4CFC1A294FB594DE21299BCD338C`; its one-page PDF is `509AFF874A21B2FA0D4098330A80FF4FCB9800D84837C9BAF86A439777D2C676`.

U01 is a bounded checkpoint, not full Paper 29. U02 is active but excluded from the immutable 65-row U01 manifest. The precise production and archival decisions are `CJK-KO-P29-001` through `CJK-KO-P29-004` in `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\CJK_DECISION_LOGBOOK_20260718.md`.

### What worked and why

The strongest fidelity improvement came from treating trap-prone historical adjectives as proposition-level semantics rather than merely terminology-table entries. The first draft used `유한 정역` / `유한 부분환` for German `endlich` and `가군 기저` for `Modulbasis`. A later-source audit of full-Paper-29 lines 53--55 showed that `Modulbasis` supplies a finite module generating system through an expression of the form `f=A_1(g)h_1+\cdots+A_s(g)h_s`; no independence or freeness claim appears. An official Seoul National University Korean Algebra 2 description independently supplied the modern frame `유한생성 대수`, `가군`, and `정수확장`. The accepted target therefore says `유한 생성` in the criterion predicate and `가군 생성계`, while preserving conventional `유한성 정리` in the title and retaining German labels where historical compounds remain unsupported.

This worked because three evidence layers were kept separate: the German proposition fixed the mathematical sense; later German lines constrained the historical term's behavior; Korean institutional evidence supported the local modern register. The SNU page was not inflated into exact attestation of `Endlichkeitskriterium`, `Integritätsbasis`, or `Modulbasis`. Chinese and Japanese forms remained excluded as Korean lexical authority, and Mandarin-Simplified dominance debt stayed qualitative.

The pre-seal sequence also worked: revise Korean wording, rebuild twice with XeLaTeX, re-extract text, rerender, inspect at original resolution, refresh target-linked hashes, then regenerate structure, terminology graph, parity, difficulty, and visual evidence. The accepted extraction contains 2,307 PowerShell characters, 875 Hangul syllables, four footnotes, and the disambiguating phrases. Two underfull boxes remain, but the 1489 × 2105 render shows no visual defect.

Machine-verifiable parity improved the usefulness of the evidence shelf. The U01 terminology authority contains 16 decisions and 14 evidence records; the typed DAG contains 69 nodes and 176 resolved edges; source-target parity has 13 rows. The replay validator returned zero errors and explicitly distinguishes source fact, computation, editorial inference, model preference, external-source evidence, and absent human validation.

### What failed or remained hard

The initial lexical draft was fluent but mathematically risky: `유한` could be read as finite cardinality, and unqualified `기저` could imply a free-module basis. This was caught only after comparing the proposition with the later constructive representation. The rejected TeX, PDF, and render hashes remain in difficulty record `CJK-KO-P29-HARD-002`; they were not erased after repair.

Five exact historical compounds still lack independent Korean attestation: `Integritätsbasis`, `Rationalbasis`, `Teilerkettensatz`, `Wurzelring`, and `Galois'sche Resolvente`. Six decisions remain held overall. No DPRK shelf or reviewer was recovered. The source images for printed pp. 28--29 were genuinely used but have no proved redistribution basis; publishing them was therefore held while preservation and metadata continued.

The first validator replay in the parent session used the bundled workspace Python, which lacked `jsonschema`, and all four scripts stopped with `ModuleNotFoundError`. Replaying with the declared system/miniconda Python, where `jsonschema 4.26.0` is installed, produced zero errors. The failure was environmental, not a defect in the indices. Transferable lesson: every validator handoff should declare or probe its Python runtime and dependency set; a script path alone is not a reproducible execution environment.

### Structural-index and hard-part evidence

- Structural JSONL authority: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\structural_index\STRUCTURAL_INDEX.jsonl`, 13 records, SHA-256 `7841817EA4D0D10DAB5EA5C2D08D041A8FD0A8F3888A2F689D47E39F9918C21F`.
- Structural CSV projection: `...\evidence\structural_index\STRUCTURAL_INDEX.csv`.
- Structural schema: `...\evidence\structural_index\STRUCTURAL_INDEX.schema.json`, SHA-256 `317ABADBF06BEF5F06A4B195FA4D6A767C1B39D3B7479F673031E0E87B50FB98`.
- Structural validator: `...\evidence\structural_index\validate_structural_index.py`, SHA-256 `BD12D215852776EEB10922C3CE20C2B0F79C8E4DC317468C8DC6D15F9F649AE2`.
- Latest structural ID: `NOE-P29-KO-U01-NOTE-004`; types are one work, one section, one bibliography item, one apparatus block, four paragraphs, one theorem, and four notes; 13 CSV rows, zero schema errors, zero total errors.
- Difficulty JSONL authority: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\difficulty_ledger\DIFFICULTY_LEDGER.jsonl`, 7 chained records, SHA-256 `D9CB3B18E75719230AA3A192B24D8DF88ACC20ACB9088410DDDCC9399635ABBE`.
- Difficulty CSV projection: `...\evidence\difficulty_ledger\DIFFICULTY_LEDGER.csv`.
- Difficulty schema: `...\evidence\difficulty_ledger\DIFFICULTY_LEDGER.schema.json`, SHA-256 `66F7AC94E7CF1AC1D140251A85C025631281568B9A704405F3A80738E65AA678`.
- Difficulty validator: `...\evidence\difficulty_ledger\validate_difficulty_ledger.py`, SHA-256 `AED6DD4EB60553059F4CBC81A1C9D0BD69277C4050EBC9DAEC51B4D6AB5641E6`.
- Latest difficulty ID: `CJK-KO-P29-HARD-007`; states are 3 resolved, 3 held, and 1 workaround; chain head `FFAD106942C068F3CE6747BF655AE49B6FCE2B7354FDE4704CC1606A9A7F40C9`; zero validation errors.

The 13-record structure made a useful coverage distinction that prose counts would obscure: the criterion is a theorem object with four embedded note relations, while publication citation and author/presenter apparatus are independent structural units. This supports source-target parity without pretending that every visible block is an ordinary paragraph. The exact target hash and balanced footnote character locators prevent a later wording change from silently retaining stale note spans.

### Visual-evidence evidence and rights lesson

- Canonical visual index: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.jsonl`, 4 records, SHA-256 `92A25CF13B95AC79731D3A4C44E49973B1FC5488E4CA4EB7AF4CA77E53E6F01E`.
- Canonical schema and validator: `...\evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.schema.json` and `...\evidence\visual_evidence\validate_visual_evidence.py`.
- Public-safe JSONL: `...\evidence\visual_evidence\VISUAL_EVIDENCE_PUBLIC_SAFE.jsonl`, SHA-256 `2497EE07866DD7768E5BCDA33C8A101663EA7F9AA52E8C2AEE9587B8156B842A`.
- Private source-root manifest: `...\evidence\visual_evidence\RIGHTS_BLOCKED_SOURCE_ROOT_MANIFEST.csv`, SHA-256 `2A5766AB26FAD27FBD88F66272CEA7FB2B01E7A504CC86C375B142D7221D848B`.
- Public open ZIP: `...\evidence\visual_evidence\KO_NOETHER_P29_U01_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip`, 1,037,376 bytes, SHA-256 `061A0DBE6A5DA724B1E53B23F604EB33C4F46D6921A6967A5E4BDA70E977AE76`.

The four indexed visuals total 3,963,591 bytes: two open project renders (1,074,860 bytes) and two rights-blocked source pages (2,888,731 bytes). The exact private source root contains eight JPEGs totaling 11,431,303 bytes. Direct ZIP inspection found eight safe entries, no JPEG, and no private-path leakage. The full printed-p.29 page necessarily contains post-U01 source material below §1 because no derivative crop was created; declaring that scope in the public caveat is preferable to silently presenting a whole page as an exact U01 crop.

Transferable rule: rights uncertainty controls pixel publication, not whether the evidence relation exists. Public-safe hashes/page coordinates and private preservation can coexist. An open payload should also undergo a content scan for private paths and forbidden binary types, not merely checksum verification.

### Methodology changes recommended from P29 U01

1. Add a mandatory semantic-predicate check for trap-prone words such as `endlich`: the running translation, not only a hidden ledger, must block a materially false sense.
2. Permit later source lines to constrain historical terminology, but label this as same-work source evidence rather than local-language attestation.
3. Require validator runtime/dependency declarations and a preflight import check before calling a package reproducible.
4. Seal bounded-unit manifests separately from active continuation files so ongoing work cannot mutate an archive checkpoint.
5. Require public visual ZIP inspection for private paths, forbidden source binaries, entry count, and uncompressed byte total.
6. Keep held historical compounds visible with source labels and explicit revisit conditions; compilation does not promote them.

### Non-generalizable details and open failure modes

The one-page Korean layout, Malgun Gothic/Noto italic fonts, local MiKTeX 26.5, and the pp. 28--29 page boundary are local facts, not universal methodology. The specific choice `가군 생성계` is an evidence-backed editorial inference for this Noether context, not a universally certified Korean headword. External Korean algebra review may still prefer another historical label. DPRK terminology remains completely untested; source-image rights remain unresolved; and the public archive has not yet reviewed or incorporated this checkpoint.

The exact U01 manifest is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\MANIFEST_U01.csv`, 65 rows, SHA-256 `0BCFDC8D74380C71B929A9B5CE599562ADBD47585F9FB7EF7A10367CC37A670A`. Package validation is `...\qa\U01_PACKAGE_VALIDATION.json`, errors `[]`, SHA-256 `979D46C353A50982A1A0D024455EE4A8CEDCF5FCC06212DF73D874CE4B10CE00`. These lessons remain private methodology evidence pending archive synthesis and do not themselves establish public doctrine.

## Paper 29 U02 retrospective — theorem/proof structure, line-ending traps, and exact failure reconstruction

### Scope and evidence boundary

This supplement covers `P29-KO-U02`, the complete §1 item 1 rational-basis theorem, its two formulations, equivalence argument, proof, notes, and corollary at exact full-Paper-29 source lines 25--39. The sealed P31 authority is SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`; the exact LF-normalized unit is `B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC`. The accepted Korean TeX/PDF/render are `B694D05E57B58E1B0373D976356E6B3B3F4883D7CC9398081DB12111877B6A7C`, `EE0A0ED2E150A5EC48945EA7E47C3F394667F288FF5E933BB00DDF193FBE8988`, and `F2F772AE57371BA57020C4E816203D3DC154EB46186457846AE2DEBCBEC1FD9E`. Relevant decisions are `CJK-KO-P29-006`, `CJK-KO-P29-007`, and `CJK-KO-P29-008` in `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\CJK_DECISION_LOGBOOK_20260718.md`.

U02 is a closed bounded checkpoint, not Paper 29 completion. Line 40 is blank; line 41 begins item 2 and continues with its first proof sentence on that same physical line. No external Korean, DPRK, archive, or community validation is claimed.

### What worked and why

The post-build independent fidelity pass was the strongest semantic control. The pre-review target already compiled and rendered, but the separate pass improved the universal quantifier from the structurally looser `유리함수의 모든 계 S` to `임의의 계 S`, exposed the proof's implicit premise that `K` is algebraic over the smaller base before invoking transitivity, and kept the `P<K` footnote attached to the exact inline relation it explains. Every accepted change triggered rebuild, extraction, rerender, visual inspection, locator regeneration, and hash refresh. This sequence distinguishes mathematical/editorial review from compilation and catches defects that no TeX log can see.

The hierarchy-first structural model also worked. German lines 11 and 13 keep several relations inline, while Korean splits them into three displays. A flat line or paragraph alignment would lose displays or misattach the second note. The U02 index instead records proof-step parents, exact source substrings, target line spans, three display children, and two note objects. The result is a 16-record JSONL authority that validates with zero hierarchy, relation, locator, delimiter, hash, or projection errors.

Preserving failed output enabled an unusually strong before/after result. The prior Korean TeX was reconstructed byte-for-byte at SHA-256 `757942045B900ED62288C9B94986D4156114887A6C4A6E9C79FF79F57CBAD26D`; its 180-DPI render exactly reproduced the historical pixel hash `3745EE1BFA0551F4BE6F2681A966872AD0C65A2CD87057F3AB80915CB4DA3935`. The regenerated PDF differed from the unavailable historical PDF and was explicitly labeled reconstruction rather than recovery. This distinction is transferable: exact source and exact pixels do not imply exact intermediate PDF bytes.

The Korean terminology shelf benefited from separating four questions: what the German proposition means, what the current Korean target says, what independent Korean sources actually attest, and what remains only an editorial inference. Direct Korean publisher/university evidence supports `중간체`, field-extension register, `따름정리`, and core field vocabulary. It does not automatically certify `유리 기저`, Steinitz's `기약계`, `순수 초월 확대`, or the compositum sense of `합성체`. The 16 decisions therefore coexist with 10 adverse records and explicit held states. Qualitative Mandarin-Simplified dominance debt and lexical-attractor basins remain in CSV ledger/crosswalk controls; validators prohibit those fields from leaking into the typed JSON schemas.

### What failed, why, and how it was preserved

The fresh authority replay first returned zero occurrences in both cumulative heads. The unit file is LF-normalized while the cumulative TeX uses different line endings; raw multiline equality was therefore a representation false negative. Explicit CRLF/CR-to-LF normalization produced exactly one occurrence at normalized character offset `1219101` in sealed P31 and `1219565` in the compiled but unsealed candidate. The raw-zero result remains in `CJK-KO-P29-U02-HARD-008`; it was not replaced by an unexplained success.

The authority validator itself failed twice during development. A raw Windows-path string fragment ending in a backslash caused an unterminated-string `SyntaxError`. The next version then falsely rejected line 41 because it expected the whole physical line to equal only the item heading, whereas the source continues with proof prose on the same line. Python text-mode reading also silently normalized newlines, making a nominally raw scan non-raw. The final validator uses safe path literals, byte decoding for raw comparison, explicit normalized comparison, and a heading-prefix assertion while preserving the complete line. The failed script states were patched before hashing; their hashes are honestly unavailable. Their symptoms, approximate times, causes, rejected approaches, and repairs survive in `qa/U02_AUTHORITY_VALIDATOR_FAILURE_HISTORY.md` and `CJK-KO-P29-U02-HARD-009`.

Two visual/layout failures remain equally explicit. An early Korean display conversion stranded a footnote marker from the `P<K` relation; that earliest state was overwritten before hashing, so its visual record has null asset/hash/bytes rather than an invented digest. The first German standalone control compiled but put only one final line on page 2. Its two rejected page renders survive, and a wrapper-only 10pt/margin change produced the accepted one-page German control without changing the exact source unit.

Plain-text extraction drops overbars. Extraction can therefore make barred and unbarred fields look identical even when the PDF is correct. Render inspection—not extraction—is the controlling evidence for those marks. This failure mode recurs anywhere semantic distinction is carried by accents, bars, Fraktur, or other glyph-level notation.

### Exact structural and difficulty authorities

- Structural index: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\structural_index_u02\STRUCTURAL_INDEX.jsonl`, 16 records, SHA-256 `F6954C84D72F3E5C02DAEF3B7B1BFF239587A1ECEEA6D7472B8A6EC00C96B60A`.
- Structural CSV: `...\evidence\structural_index_u02\STRUCTURAL_INDEX.csv`.
- Structural schema: `...\evidence\structural_index_u02\STRUCTURAL_INDEX.schema.json`, SHA-256 `C574A34D79C8CA9FAB56EB84D5D0E37D45E336F30238ECC65D9D0A6B29B7A05D`.
- Structural validator: `...\evidence\structural_index_u02\validate_structural_index.py`, SHA-256 `F926BF7F46C21AD6302769BDF910490AE3C34E4120211A8214FF744B69FA2CA7`; zero errors. Latest structural ID: `NOE-P29-KO-U02-COR-001`.
- Difficulty ledger: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\difficulty_ledger_u02\DIFFICULTY_LEDGER.jsonl`, 9 chained records, SHA-256 `DC61B76D9A1F6DBA940CCC5D5219468473597304E3C89D231FFF89C41E7903B0`.
- Difficulty CSV: `...\evidence\difficulty_ledger_u02\DIFFICULTY_LEDGER.csv`.
- Difficulty schema: `...\evidence\difficulty_ledger_u02\DIFFICULTY_LEDGER.schema.json`, SHA-256 `8FB6C2825AE403F251A47D100E17C0E5B3538288A72E9E8B16F3B1AD770DEAB4`.
- Difficulty validator: `...\evidence\difficulty_ledger_u02\validate_difficulty_ledger.py`, SHA-256 `6CCDE7F07F6A4B6A53CE146B4D3360986D46408A8C4698E9109EC36D25DCAF97`; 7 resolved / 1 held / 1 workaround, zero errors. Latest ID `CJK-KO-P29-U02-HARD-009`; chain head `84579AD8AFD5199B1065EBA6106B1176BB0855107D39B4F3A7FB87F3A6039788`.

### Exact terminology, graph, parity, and visual authorities

- Korean example/evidence corpus: `...\evidence\KOREAN_NATIVE_EXAMPLE_CORPUS_U02.csv`, 8 rows, SHA-256 `0AD8037BDA90F5742A26061688C890924C758D1F6DF0FD245CF212ACBD3FD89D`.
- Terminology decisions/schema: `...\evidence\TERMINOLOGY_DECISIONS_U02.json` and `TERMINOLOGY_DECISIONS_U02.schema.json`, SHA-256 `F4302DB5229292777215BA284A261FFA52D15084A34617D98A5F063F64ABCB04` / `269AD763212D4B051A7B753399ABE49C770436856278600F100B4FBC69CD0AE1`. Latest decision ID `KO-P29-U02-D016`.
- Typed graph/schema: `...\evidence\TYPED_CONCEPT_EVIDENCE_GRAPH_U02.json` and `TYPED_CONCEPT_EVIDENCE_GRAPH_U02.schema.json`, 68 nodes / 124 edges, SHA-256 `C89E4809CAC0D64EC669DADAD7BB169DBB3B713DA1667A2377CB2665AF34B605` / `D92FAB92252C7B3557EFFB50237A2AED5E3279A6CE5F890040172E6CF47F6FCD`.
- Structural parity: `...\qa\SOURCE_TARGET_PARITY_U02.csv`, 16 rows, SHA-256 `CC0A635BE554382A8D9454A570547DF1A45C6F3B7E6DD9065486D96D1CC2DD57`.
- Terminology/graph/parity builder and report: `...\qa\build_validate_term_graph_parity_u02.py` and `TERM_GRAPH_PARITY_VALIDATION_U02.json`, SHA-256 `41044EA459FAC14630558C00DFC2CA6CFCB63943FC527F518DC8FA811346221E` / `D4B11A4CDD0EDC60C0D31E54B6C14D06035A41785A653BF34178A37047703058`; zero errors.
- Canonical visual index/schema: `...\evidence\visual_evidence_u02\VISUAL_EVIDENCE_INDEX.jsonl` and `VISUAL_EVIDENCE_INDEX.schema.json`, 8 records, SHA-256 `A5F85C5F85BE9EEEC4ABCE5C0567E2E78DF07547D8758702580FA8BD9D25D088` / `A0A3B049803AA333F847F361680B82A1BEE0905E7EAAB38132E9D7EDAA9C3CD8`. Latest visual ID `VE-NOE-P29-KO-U02-008`.
- Visual validator/report: `...\evidence\visual_evidence_u02\validate_visual_evidence.py` and `VISUAL_EVIDENCE_VALIDATION_REPORT.json`, SHA-256 `2B86A4332A7FF5F73B6381FE5636A445451ECE4CA49D63398C1B43A0C6540052` / `75D8866E271CA9160F39E09BBCF631D930EFA7890B38D44EB4BB48DEC2920624`; zero errors.
- Rights-blocked root manifest: `...\evidence\visual_evidence_u02\RIGHTS_BLOCKED_SOURCE_ROOT_MANIFEST.csv`, SHA-256 `A588817F3A223FB934803A022CA67F44F79947C09CEC8CD2B21CE628F306D13C`.
- Open visual ZIP: `...\evidence\visual_evidence_u02\KO_NOETHER_P29_U02_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip`, 12 entries / 2,173,339 bytes, SHA-256 `FA4015384D9F79F497809CCD189C7C0F6EEE5CDD0A9661613E8EBEEF68C5E821`; zero source JPEGs and private-path leaks.

### Transferable methodology changes

1. Every multiline authority-survival validator must declare byte encoding and newline normalization, preserve the raw result, and require exactly one normalized occurrence.
2. Cursor validation must distinguish a structural heading prefix from a physical-line equality assertion; source formatting can place heading and prose on one line.
3. Note anchors and the exact mathematical relation they annotate must move atomically when inline source mathematics becomes a target display.
4. A second source pass belongs after the first successful render, followed by complete downstream replay for every accepted change.
5. Preserve the pre-review artifact or a reconstructable change set before editing. If a state was overwritten before hashing, record the missing digest as unavailable rather than reconstructing certainty.
6. Typed structural parity should support one-to-many inline-to-display mappings; a flat CSV is a projection, never the hierarchy authority.
7. Keep local-language evidence, same-work semantic constraints, and CJK attractor information as separate evidence classes. No cross-language cognate should promote a Korean decision.
8. Make notation-aware visual checks mandatory whenever extraction can erase bars, accents, Fraktur distinctions, or other semantic glyph features.
9. Require package validation to prove that the previous sealed unit stayed byte-identical while the new unit was added separately.

### Non-generalizable details and open failure modes

The exact-pixel reconstruction succeeded because the three intervening Korean edits and original job-name/render settings remained recoverable; most lost states will not be reconstructable. The one-page German/Korean layouts, Malgun Gothic/Noto font behavior, MiKTeX/Poppler outputs, and printed pp.29--31 boundaries are local facts. The compact German control is a QA wrapper, not publication typography. `기약계`, `유리 기저`, and `합성체` are context-controlled Korean working decisions, not universal glossary entries.

Open risks remain: a Korean field-theory historian may replace several terms; no DPRK standard evidence exists; pp.29 and 31 include material outside U02; source-image redistribution rights remain unresolved; web evidence pages were not locally snapshotted; a future TeX/font/extractor change may alter pages or lose overbars; and archive maintenance has not yet reviewed or incorporated U02. The exact U02 manifest is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\MANIFEST_U02.csv`, 82 rows, SHA-256 `1C3173028AE2F8E583580B19C44B4D34BD5BC14AF5A27667D9BCDB1B0C9DCFEE`; package report `...\qa\U02_PACKAGE_VALIDATION.json` has errors `[]`, SHA-256 `9D1417B58D602C7A1B275EF5A92157C46070DCA6DFB86C83DA5029FBE3BF2E05`.

## Paper 29 U03 retrospective — sense-locked finiteness language, competing source witnesses, and visual-loss honesty

### Scope, authority, and validation boundary

This supplement covers `P29-KO-U03`, exact full-Paper-29 source lines 41--45: item 2, the necessity argument, the characteristic-dependent sufficiency hypothesis and target, the quotient-field argument, and the reduction to the relative integral-closedness of a finitely generated subring. It is a closed proof stage, not the completed proof. Full-Paper-29 line 46 is blank and line 47 begins the next construction. The authority is the sealed P31 cumulative German TeX at `${PUBLIC_DOCUMENTS_ROOT}\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex`, SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`; the shared `00_current_german_authority` pointer at R821 was not used because it is stale. The exact LF-normalized U03 source is SHA-256 `1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458`.

The accepted Korean TeX, PDF, and final 180-DPI render have SHA-256 `0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60`, `4E6DEC776EE572EFCC97138F21D0AE98ABA5A8F3DD4E3362E1BD2808A23D7A19`, and `42E78806891372C91FDB089A5374103B8BD8E4E7BECFC14D1C94C719F7911579`. The one-page target was compiled twice with XeLaTeX, has no selected warning-pattern hits, and was inspected at original render resolution for clipping, overlap, glyph loss, formula damage, and pagination. Two independent read-only model passes found no remaining mathematical or quantifier error after corrections. These are internal controls only: no Korean algebra specialist, DPRK reviewer, source owner, archive maintainer, or community reviewer has validated U03. Relevant append-only decisions are `CJK-KO-P29-010`, `CJK-KO-P29-011`, `CJK-KO-P29-012`, and this retrospective's `CJK-METH-005` in `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\CJK_DECISION_LOGBOOK_20260718.md`.

### What worked and why

Sense-locking the German adjective `endlich` before polishing Korean prose prevented a serious mathematical collapse. Within five source lines it denotes finite generation of a ring, finite degree of a field extension, and finite generation as a module. The accepted target therefore uses `유한 생성` for the first, `유한 확대` or `유한 대수적 확대체` for the second, and `유한 가군 생성계(Modulbasis)` for the third. The terminology controls store an explicit sense window and excluded senses for every trap-prone form. This was more reliable than treating a German lemma as one glossary entry.

The second source-fidelity pass also paid for itself. It rejected an ambiguous Korean equivalent of “these rings,” restored the source's inline containment chain after an unnecessary target-only display had been introduced, made the fraction-field antecedent explicit, and retained source labels for `근체(Wurzelkörper)` and `약수사슬정리(Teilerkettensatz)`. Compiling before that pass would have proved only TeX validity; rebuilding after it supplied the accepted semantic/layout evidence.

Keeping canonical TeX and printed scan as distinct witnesses made the footnote conflict auditable. The sealed TeX contains two identical `\footnote` calls; printed p.31 has two anchors sharing one marker and one note body. U03 follows the declared sealed TeX and translates two numbered notes, while the printed state remains held adverse evidence requiring source-owner adjudication. The earlier decision to mimic the printed shared note was not silently edited away: `CJK-KO-P29-011` explicitly supersedes that part of `CJK-KO-P29-010`.

The Korean evidence shelf also remained disciplined. Six locally relevant Korean institutional/publisher examples support the surrounding register, while exact historical terms without direct attestation remain held. Chinese and Japanese cognates did not authorize Korean. Mandarin-Simplified dominance risk is recorded only as qualitative evidence-shelf debt, never as a readiness scalar; lexical-attractor basin membership stays in the CSV ledger/crosswalk and is rejected from typed decision/graph JSON. The deterministic terminology/graph/parity replay verifies 14 decisions, 62 nodes, 65 edges, an acyclic graph, and 16 structural-parity rows with zero errors.

### What failed, why, and how the failure evidence survives

The most important failure was an overwritten first render. Refinement began before the initial PNG and PDF had been durably hashed. The exact initial TeX was recoverable at SHA-256 `379C3A064823F94FDACD2419F5BCF9DAA54002FC7AA99F99A231DA0DE5FBE877`, so a clearly labeled reconstruction was compiled and rendered; however, its PDF/PNG hashes (`F271C3B61FA32468C5B4313D1ED62C62613B3347A5947C53C73CB96050CD72DE` and `5103667C63B1CB8B114F28C1A3E5316B03B0B91E493FABB095E1382BBE0DDC6E`) are reconstruction hashes, not the missing originals. The visual index contains a metadata-only loss event rather than an invented original digest. A first reconstruction command also failed because a path segment was doubled; that rejected attempt survives as `CJK-KO-P29-U03-HARD-008`.

The initial Korean wording contained three non-render failures: `endlich` was not consistently disambiguated; the fraction-field pronoun had an unclear antecedent; and an inline source relation had drifted into a display. Independent comparison, not the compiler, found them. All were repaired before acceptance and remain in the difficulty history. This demonstrates that successful build, clean extraction, and attractive layout are orthogonal to source fidelity.

The local Poppler wrapper failed during rendering although direct Poppler invocation worked. The accepted render records the workaround and exact tool path; the wrapper failure is not generalized into a claim that Poppler itself was defective. Likewise, the printed/canonical footnote disagreement is held rather than “resolved” by editorial preference.

Source-image rights remain unresolved. Three used source JPEGs are indexed with page coordinates, dimensions, hashes, structural links, and `manifest_only_rights_blocked` disposition. The complete private source root contains eight JPEGs totaling 11,431,303 bytes and is represented by a SHA-256 manifest, not copied into the public ZIP. Three project-generated renders are open-payload material; the seventh visual record is the loss event. The public ZIP was inspected for source-image entries and private-path leakage, both zero.

### Exact structural, difficulty, and visual authorities

- Structural authority: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\structural_index_u03\STRUCTURAL_INDEX.jsonl`, 16 records, SHA-256 `B9301BEA16DC6D6FC0B0425080916A29FE0AC011C23CA0B2236675B887D0E380`; CSV projection `...\STRUCTURAL_INDEX.csv`; schema `...\STRUCTURAL_INDEX.schema.json`, SHA-256 `7583989710B438459DE3D74712464188C06347350D53976F9351BC7C68BEC99D`; validator `...\validate_structural_index.py`, SHA-256 `5C36494B1C3243C7020895F175B65988C84C796D1B7EA2A3148227D583ED5F50`; report `...\STRUCTURAL_INDEX_VALIDATION_REPORT.json`, errors `[]`. Latest structural ID: `NOE-P29-KO-U03-STEP-007`.
- Difficulty authority: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\difficulty_ledger_u03\DIFFICULTY_LEDGER.jsonl`, eight append-only hash-chained records, SHA-256 `90EDE7EA9052680E296A44BFA6445A3148B83C0F3BBCCDD6EA3936DEB4EDECC5`; CSV projection `...\DIFFICULTY_LEDGER.csv`; schema `...\DIFFICULTY_LEDGER.schema.json`, SHA-256 `378946828ABA54BF93C03DBB7BCFEDE57E47932875A1CB98E37B247785259020`; validator `...\validate_difficulty_ledger.py`, SHA-256 `D16D109A2A7C67DC86EFCC39D5121CAE1726F2868C1B9E5996622DA4B8CEEAB9`; report `...\DIFFICULTY_LEDGER_VALIDATION_REPORT.json`, errors `[]`. Latest difficulty ID: `CJK-KO-P29-U03-HARD-008`; chain head `7A0B79CE3360E7E64C1EE05B53B414E883C29E3BF68946FBBFBFC2293531207A`.
- Canonical visual authority: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\visual_evidence_u03\VISUAL_EVIDENCE_INDEX.jsonl`, seven records, SHA-256 `927BA1320175865ED838F22EBE6030581D8FE708E33C56B93660A8773EB2CB6E`; CSV projection `...\VISUAL_EVIDENCE_INDEX.csv`; schema `...\VISUAL_EVIDENCE_INDEX.schema.json`; validator `...\validate_visual_evidence.py`; report `...\VISUAL_EVIDENCE_VALIDATION_REPORT.json`, errors `[]`. Latest visual ID: `VE-LOSS-P29-KO-U03-001`. The public-safe JSONL is SHA-256 `82C667EE7B86C638DF759304D6DF5334666F35696B16F80C41B3366DA06D7486`; the source-root manifest is `ED29DEA579805E2E2064F957A61C775D78091CB2F233EBAAB0040C77C6E01991`.
- Public visual payload: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\visual_evidence_u03\KO_NOETHER_P29_U03_VISUAL_EVIDENCE_PUBLIC_PAYLOAD_20260718.zip`, 583,010 bytes, 11 entries / 678,652 uncompressed bytes, SHA-256 `71C211021F4ED2D3C422D88E2742B1B913096E2EA8D7A72C09FA8FDFAB7EE0AD`; zero forbidden source-image entries and zero private-path leaks.

### Transferable methodology changes

1. Type polysemous source terms by occurrence and mathematical role before choosing target wording; never let one source lemma imply one target lemma.
2. Preserve each source witness independently. When canonical editable source and printed scan disagree, select the declared authority for the target and retain the other witness as adverse evidence with an adjudication condition.
3. Hash every pre-review TeX/PDF/render before semantic editing. If a binary was lost, distinguish exact source reconstruction, pixel reproduction, and binary recovery; do not transfer a reconstructed hash to the missing artifact.
4. Run a source-fidelity pass after the first successful render, then replay build, extraction, visual inspection, structural locators, terminology probes, and manifests after every accepted change.
5. Keep source-image binaries and public-safe metadata as separable archival layers. Rights uncertainty blocks redistribution, not preservation or coordinate/hash indexing.
6. Require structural parity to cover every indexed object, including notes and equations, and require continuation cursors to identify the next substantive line rather than only a page.
7. Treat institutional/publisher terminology pages as linguistic evidence, not endorsement. Record Korean, DPRK, source-owner, archive, and community review as separate states.
8. Make wrapper failures and workaround success separate facts; do not misattribute a wrapper defect to the underlying renderer.

### Non-generalizable details and open failure modes

The exact two-footnote decision is specific to the sealed P31/printed-p.31 conflict. The U03 font stack, one-page layout, MiKTeX build, direct Poppler command, and 180-DPI raster are local implementation details. `근체(Wurzelkörper)`, `약수사슬정리(Teilerkettensatz)`, and the current relative integral-closedness phrasing are bounded editorial decisions, not universal certified Korean terminology. No DPRK evidence exists, and South-Korean register cannot be projected northward.

Open risks include source-owner resolution of the note mismatch; qualified Korean review of the held historical terms; later-corpus contradiction; font/toolchain drift; source-image rights determination; archive incorporation; and the unfinished proof beginning at line 47. The deterministic package authority is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\MANIFEST_U03.csv`, 82 rows, SHA-256 `3C99758568EF5C3995CCE9F4CB29852DF9156D5B1E9F270E1B51F7CF66CB4118`; checksums file SHA-256 `CC6DD5E4B9D9D99FF59AC36E23944566DF4C9F231DFB57FE3884861CD8E2D207`; package report `...\qa\U03_PACKAGE_VALIDATION.json`, errors `[]`, SHA-256 `068FE49805C88428314EC3B181E208F871D5688891A8616030268493B985D369`. U01 and U02 manifest/report hashes remain byte-identical. This retrospective is evidence for methodology synthesis, not a publication or certification claim.

## Paper 29 U04 retrospective — generic-to-specialization order, historical lexical attractors, and registry discipline

### Scope, authority, and validation boundary

This supplement covers `P29-KO-U04`, exact full-Paper-29 lines 47–51: the infinite-coefficient-field normalization construction, generic linear replacement, specialization of auxiliary indeterminates into \(P\), construction of \(\mathfrak T=P[g_1(x),\ldots,g_t(x)]\), and identification of the relevant ring of integral elements in \(\mathfrak L\). It is a closed proof stage, not completion of item 2. Line 52 is blank; line 53 begins the separate chain-condition/module-finiteness stage.

The sealed P31 authority is `${PUBLIC_DOCUMENTS_ROOT}\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex`, SHA-256 `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`. The stale shared R821 pointer was not used. The exact LF-normalized source is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\source\Noether_Paper29_German_P31_U04_InfiniteFieldNormalizationConstruction_exact_lf.tex`, 1,544 bytes, SHA-256 `4C1CE8C08942FBC5EC617F4B8B559092715236471D53183611E83A5748A04578`.

The exact preserved first-draft Korean TeX is SHA-256 `BF3A1427AF75CC37E7CB65FCF1FEDB5632FF6CECB2E66851C314F5136A7A8789`; its PDF and render are `189CEC31652D4ACCCF66D4B753838AF302F82C178565FA00051E1EA3F57969F2` and `748FD72C4E6A898DA1B2AF3CF9B305653442534941735D94BE7FF11E45458FCE`. The accepted Korean TeX, PDF, and 180-DPI render are `A967222517ABF3392BA10B2CF166EDCDF455F13E5D5C29A00A9A49E609ECE9A4`, `5AD0B7D710C82B686EA2F67820F2CA29400205E31CD7D7EA1169A530E46CC5DE`, and `E221443C62B0FDC7025A753884AAC3E10075F9173D069EDA518024824CCE46FD`. Relevant append-only decisions are `CJK-KO-P29-015` through `CJK-KO-P29-020` and methodology decision `CJK-METH-006` in `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\CJK_DECISION_LOGBOOK_20260718.md`.

All review described here is internal source, model, build, extraction, and visual QA. No Korean algebra specialist, DPRK reviewer, source owner, archive maintainer, rights reviewer, or community reviewer has certified U04.

### What worked and why

The bounded-unit choice worked because it used mathematical stage closure rather than page size or an arbitrary line count. Stopping at line 47 would have cut the generic replacement argument before its display and specialization; extending through line 53 would have mixed normalization with a distinct chain-condition/module-finiteness stage. Lines 47–51 complete the construction and final equality, line 52 is blank, and line 53 supplies an unambiguous continuation cursor. The structural index retains the higher-level state as `proof_continuation`, preventing local closure from being mistaken for a completed proof.

The strongest semantic control was preserving the order “generic indeterminates first, specialization second.” The source first treats `t_i` as `Unbestimmte`, proves integral dependence after the generic linear replacement, and only then uses the infinitude of \(P\) to choose suitable values in \(P\). The Korean target keeps `부정원` before \(P\)-valued `특수화`, and the structural relations preserve the direction between the stages. This is proof-bearing order, not stylistic sequence; compressing the clauses could falsely suggest that arbitrary specialization preserves integrality.

Explicit sense windows prevented two serious lexical-attractor errors. Bare `irreduzibles System` can attract the modern sense “system of irreducible polynomials,” while `Integritätsbasis` can attract number-field integral-basis or linear/free-basis senses. The accepted target therefore gives `기약계(irreduzibles System, 곧 P 위에서 대수적으로 독립인 함수계)` and `정수성 기저(Integritätsbasis, 곧 \mathfrak R를 P-대수로 생성하는 유한 집합)`. The historical labels remain visible, but the running prose—not merely a hidden glossary—blocks mathematically false readings. `유한 차수의 확대체` likewise distinguishes extension degree from the infinite cardinality of the coefficient field.

Preserving the exact first draft before revision worked better than reconstruction. The draft TeX, PDF, log, extraction, and render all survive under distinct `draft001` names. Consequently the visual archive contains genuine before/after evidence and correctly records no loss event. Independent source review found no quantifier, dependency-direction, specialization, notation, or final-equality defect; independent Korean review required the three sense disambiguations, after which the target was rebuilt, re-extracted, rerendered, and revalidated.

The registry transition was handled as structured spreadsheet data rather than unstructured prose. `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\CJK_WORK_REGISTRY_20260718.csv` parses as 12 data rows by 8 declared columns and contains exactly one `NOETHER-P29-KO-ACTIVE` row. At the claim-stage snapshot it records U01–U03 as closed, U04 lines 47–51 as the sole active Korean unit, and line 53 as the next substantive cursor; SHA-256 `B24C43E9010D505E94EA6E55C390C4B621074FDD7A93FA4E272B0D69DF800AF5`. The parallel active claim is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\KOREAN_NOETHER_P29_ACTIVE_CLAIM_20260718.md`, SHA-256 `CF907C986089C3374E5EF9EC2656B2F59C987A4DAE4A2774A6B9349BEBAB76EE`. Importing, inspecting, rendering, uniquely selecting the work row, previewing the edit, and rerendering before patching the original is a stronger control than blind textual replacement because it verifies header, dimensions, quoting, uniqueness, and unrelated-row preservation. These are mutable current-state projections; the append-only decision log remains the correction authority.

### What failed or remained hard, and why

The initial Korean draft was compilable and readable but left three high-risk distinctions implicit: the historical sense of `기약계`, the finite-algebra-generating sense of `정수성 기저`, and finite extension degree versus an infinite base field. Compilation could not detect any of these semantic risks. They were repaired only after a separate Korean terminology pass and remain visible through the draft/final hash pair. The transferable lesson is that compilation, semantic fidelity, terminology evidence, and reviewer-state closure are independent gates.

The printed witness splits `Integritätsbasis` across pp.31–32 as `Inte- / gritätsbasis`. Auditing only one page, OCR output, or a page-local crop could create two false tokens or lose the term entirely. Inspection of both pinned page images—SHA-256 `024008210DE649E1A452FBB9614DA4CE8453BC2B004233C79C9A8581951728BA` and `7244CB121A9199EB1388DBEC862D6894D09F80378EAB5F6FEE143F16BDC55AB0`—showed ordinary page-break hyphenation, consistent with the sealed TeX. This detail is resolved for U04 but remains a recurrence cue for OCR, corpus search, terminology extraction, and structural indexing.

The first Korean draft compiled successfully but emitted an underfull-box diagnostic with badness 2469. The final target has zero selected warning, error, overfull, underfull, or missing-character hits and no visible defect at 1489 × 2105, but this does not generalize to eventual full-reader geometry. Successful PDF production, clean-log compilation, local visual acceptance, and merged-reader typography must remain separate states.

The first authority-validator run was also wrong: it expected one occurrence of `\mathfrak T=P[g_1(x),\ldots,g_t(x)]`, while the faithful target contains two, at introduction and construction conclusion. The translation was not edited to satisfy the bad oracle. The expected multiplicity was corrected to two, the complete validator replayed, and the false failure retained in `CJK-KO-P29-U04-HARD-006`. The final authority validator/report hashes are `B74FECFE0BE3A186D1D4B7ED55BB68A408683CAC3A1C81C2E57FE5C05C073A9A` and `E5BF519DF1594CF02BF6DDEFF3F012C29B384FDA9C8001BB5174FE5877D0E1FA`, with errors `[]`. The transferable rule is to audit semantic multiplicity before changing a target to appease a failing test oracle.

Finally, spreadsheet parsing does not make the mutable registry an archival authority. At this retrospective snapshot its row intentionally still says U04 is in production. Package closure and archive delivery require a second logged state transition; silently leaving the row stale after delivery would recreate the cursor debt encountered earlier. A registry row is a routing projection, not proof of delivery, review, or publication.

### Exact structural and difficulty authorities

- Structural JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\structural_index_u04\STRUCTURAL_INDEX.jsonl`, 14 records, SHA-256 `CA0142AE4477F66B255B011C762906C85B215981AEB835DE8D2B4D365652813F`; latest ID `NOE-P29-KO-U04-STEP-009`.
- Structural schema: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\structural_index_u04\STRUCTURAL_INDEX.schema.json`, SHA-256 `F71535DDA4219877F339CFAC47924450CA654F66713ADB5C617FFBA8BCE9B171`.
- Structural validator/report: `...\evidence\structural_index_u04\validate_structural_index.py`, SHA-256 `47117817D89A758B6A658BF75C7DB4BB5AB63536811737F23A0211D76340963B`; `...\evidence\structural_index_u04\STRUCTURAL_INDEX_VALIDATION_REPORT.json`, SHA-256 `1213B7C19C19F4E2F545FB6017DB72CFB6A68F34208775C653E86C28E585B311`, errors `[]`. Types are one work unit, one proof continuation, one paragraph, nine closed prose units, one display, and one note.
- Difficulty JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\difficulty_ledger_u04\DIFFICULTY_LEDGER.jsonl`, six append-only chained records, SHA-256 `E4FA33B3B8B07EE64023F4CAB6EAA139A56955BF055941410E2CA2E96E6F7139`; latest ID `CJK-KO-P29-U04-HARD-006`; chain head `3E2D045081D4C837E69B529426C164A30529F5A2305183F107356EE2A0BA4CC6`.
- Difficulty schema: `...\evidence\difficulty_ledger_u04\DIFFICULTY_LEDGER.schema.json`, SHA-256 `ADB2327B92E41D717F995A8FA70DBFDB2BA45449489FB40E9FA22AB4AA0EBC04`.
- Difficulty validator/report: `...\evidence\difficulty_ledger_u04\validate_difficulty_ledger.py`, SHA-256 `63949B8D225A41B6BCD2B6B45AF3D7162FCEE98E2189202BC4C9850DCCFE5EB5`; `...\evidence\difficulty_ledger_u04\DIFFICULTY_LEDGER_VALIDATION_REPORT.json`, SHA-256 `FD7A0E48876CE0CB60623614D1CE5BC9499A909E60F2877BA7C123D9A9955E39`, six resolved records and errors `[]`.

### Exact terminology, graph, and parity authorities

The deterministic terminology replay contains nine Korean evidence records, 13 terms, four held terms, 14 adverse records, 13 typed decisions, a 63-node/99-edge acyclic graph, and 14 parity rows. Latest IDs are `KO-P29-U04-E009`, `KO-P29-U04-T013`, `KO-P29-U04-A014`, `KO-P29-U04-X013`, `KO-P29-U04-D013`, and `NOE-P29-KO-U04-STEP-009`. It records Mandarin-Simplified dominance risk qualitatively rather than as a readiness scalar, excludes attractor fields from typed JSON, uses no Chinese/Japanese form as Korean authorization, and leaves all ko-KP claims `unverified_do_not_claim`.

- Korean evidence, terminology, adverse, and crosswalk SHA-256: `7866268C1DC25BED5A997591439A4FF39BE7FDD37FE4C4C86D7793598FD4FA90`; `147A2F8709189334094D2563AB75F555823A95E1906CBCFCA0578AD9A04945B2`; `83E87A0B76FAC8F738AC23238E1DF355E7AB92483D49953C6006A722BE26539F`; `E01B9EC43725CA01B71D93DD9620C96F54555CDD9F88FB833D300E9259574D37`.
- Typed terminology decisions/schema SHA-256: `7511951A7654C63A9BB3EE5D1A4BFA889E60F70FF9389015BCB8FF48C0FB0773` / `C983F17BE8CF29E3B45F38AEB1CED0712C8165264DFAAD96E3D80928F9C1E634`.
- Typed graph/schema SHA-256: `703816AE29199DF7BB40FA5EB93FC095C8A0705F734874082C0E7AB97AF92F4B` / `0E57FA93E08604D42CF10ABF418A7171418C63C9E40F18F5519E80C5C3B8FDC7`.
- Source-target parity SHA-256: `02F549CB71F16C5387DC42EEF1CF6D6E140840F4F657479112787369FDA07DE6`.
- Builder/report SHA-256: `2A8B6C8E4F479AC94E2C0F5B7C0F95EF1E6970A423A4CED89FDBD436ABD2BC9E` / `E9D7570EFDAF2CFFA3F271307F1A17A324EA750C5D28EAA9DC4F7FE5BED847FE`, errors `[]`.

The held terms are `irreduzibles System`, `Integritätsbasis`, `Unbestimmte`, and the specialization phrase. Their explicit sense windows make them usable within this bounded target but do not promote them to certified corpus-wide Korean headwords.

### Exact visual authority and rights split

- Canonical visual JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\evidence\visual_evidence_u04\VISUAL_EVIDENCE_INDEX.jsonl`, five records, SHA-256 `B0A5743F3B5A1EF4B91D596703157ABEABBD26D9ECD96D7F269015F1A4189897`; latest ID `VE-NOE-P29-KO-U04-005`.
- Visual schema: `...\evidence\visual_evidence_u04\VISUAL_EVIDENCE_INDEX.schema.json`, SHA-256 `62BE321DAEFD7190B328510EB9F8748FA9007867B28255ABE2EF60B250556E9C`.
- Visual validator/report: `...\evidence\visual_evidence_u04\validate_visual_evidence.py`, SHA-256 `EF1754A13C31A44C5B916D983E0F9FC37F0FFB75F3E73FFB18BABDA95C78D13B`; `...\evidence\visual_evidence_u04\VISUAL_EVIDENCE_VALIDATION_REPORT.json`, SHA-256 `737288A9C655352C8D745370ED4D410AE5DF2E155E6B65BBBBD915A05880F4F3`, errors `[]`.

The visual authority records two rights-blocked source pages totaling 3,267,415 bytes and three open project renders totaling 615,145 bytes. The complete private source root remains eight JPEGs / 11,431,303 bytes. The public-safe JSONL hash is `41BC80FC6CBA00002398DE6B816FC7DE62C75D7D8F91569B4800FC7B73D66408`; the source-root manifest hash is `91626B85C598BE911EF811CF0E0E7284F95884A4A75784DB1408636E60058CD9`. The public visual ZIP is 551,141 bytes, 13 entries / 658,839 uncompressed bytes, SHA-256 `E131F6612312C9C6B7E385073F1380A6F61C2F6CF9967FD2616C5CD4BAADA4BA`, with zero source-raster, private-path, or unsafe-path leaks.

### Transferable methodology changes

1. Define bounded units by completed mathematical operation and a precise next-substantive cursor, while recording higher-level proof incompleteness separately.
2. Encode generic-construction and specialization stages as directed structural relations; sentence order alone is too easy to destroy during stylistic editing.
3. Require running-prose sense windows for historical terms whose modern lexical attractors would materially change the mathematics.
4. Preserve the first buildable draft before independent review. Genuine before evidence is methodologically stronger than later reconstruction.
5. Audit page-bottom hyphens with both adjacent source pages before terminology extraction, OCR acceptance, or structural indexing.
6. When a validator reports the wrong occurrence count, audit semantic multiplicity before changing the target. Test-oracle failures belong in the append-only difficulty ledger.
7. Distinguish successful compilation, clean-log compilation, correct source semantics, and visually acceptable rendering as separate gates.
8. Treat the work registry as a schema-controlled spreadsheet projection: parse it, require a unique work key, verify dimensions/cursor fields, render before and after, hash every state transition, and retain the append-only decision log as correction authority.
9. Require final package replay to prove earlier units remain byte-identical and exclude future-unit/cache/rights-blocked material.
10. Preserve source images privately and publish only their metadata/hash/coordinate layer until redistribution rights are documented.

### Non-generalizable details and open failure modes

The exact `Inte- / gritätsbasis` split, two-page source witness, one-page Korean layout, local font behavior, MiKTeX/Poppler output, and the two legitimate occurrences of the \(\mathfrak T\) formula are U04-specific facts. `기약계`, `정수성 기저`, `부정원`, and `특수화` are bounded editorial choices with explicit glosses, not universally certified Korean terminology.

Open risks remain: qualified Korean historical-algebra review may replace the four held terms; no DPRK evidence exists; merged-reader geometry may reintroduce line-box problems; OCR may recreate the cross-page token split; a later sealed authority may change the line-51/53 boundary; source-image rights remain unresolved; and archive maintenance has not yet reviewed or incorporated U04. Line 53 remains the next substantive production cursor, and item 2’s proof is unfinished.

The deterministic package authorities are `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper29_ko_tranche_001_20260718\MANIFEST_U04.csv`, 84 rows / 16,098 bytes, SHA-256 `2C3B9E0CB6F3210C449B8639A47A853A0641DCD397B2FAB2497F75EC40C1FEF4`; `...\SHA256SUMS_U04.txt`, 10,793 bytes, SHA-256 `63C3FAAB0266438E9C332017876575E6C113BA9E6906EC7614B2172E71146539`; and `...\qa\U04_PACKAGE_VALIDATION.json`, 17,262 bytes, errors `[]`, SHA-256 `9F180BBC0805FADABE052C1179C60038F1F34C29421C4BE355AD14844CC50C72`. Two consecutive post-wording package runs were byte-identical; a main-session replay returned the same hashes. U01–U03 manifest/report authorities remain byte-identical. This retrospective is methodology evidence, not publication, external certification, rights clearance, or completion of Paper 29.

## Translation-only P32 addendum — bounded production without self-checking (2026-07-22)

This addendum concerns the later role boundary under which the Korean lane translates and separate sessions check. Noether Paper 32 U01–U19 now have editable Korean draft-text coverage of the manager-routed substantive prose, but no source check, Korean review, compilation, rendering, assembly, packaging, certification, approval, or final-paper claim was made. Relevant production and handoff decisions are `CJK-KO-P32-001` through `CJK-KO-P32-036`, especially U17–U19 decisions `CJK-KO-P32-030`–`033`, transport corrections `034`–`035`, and metadata decision `036`.

### What worked

Small routed units with exact source lines, source-slice hashes, editable target hashes, translation-choice notes, and explicit checker handoffs allowed translation to continue without silently absorbing checker authority. The strongest linguistic control was the source-local sense window: inclusion-minimal `minimal` was kept distinct from minimum degree as `극소(極小)`, algebraic `Index` from character `지표` as `지수(指數)`, and algebraic `Einheitswurzel` from the statistical unit-root attractor through `원시 p차 단위근`. Hangul/Hanja metadata and the explicit ko-KR/ko-KP boundary made provisionality visible. Mandarin-Simplified dominance was recorded only as qualitative evidence debt; no Chinese or Japanese target authorized Korean.

The durable shared-file fallback also worked. Two background manager notifications returned task IDs but their immediate status snapshots reported `systemError` and no assistant response. Instead of claiming receipt, the lane retained `WORKER_RETURN_U17_U19.md`, SHA-256 `F591D672917B4257C4A4FE70922669F10987555EF454D3AF0E3AD4A43620C48F`, and appended the failure/cursor correction in `CJK-KO-P32-034`–`035`.

### What failed or remained hard

An initial delegated U13 draft selected the fluent but wrong-sense attractors `최소` and `지표`. They were rejected before durable delivery in favor of `극소` and `지수`, but the failed path is preserved in `CJK-KO-P32-HARD-001`. This shows that delegation can accelerate drafting but cannot replace a translator-owned sense window even when no self-review is authorized.

Machine structural extraction found different source and Korean blank-line/display segmentation. The index therefore retains 16 target-only `other` records and marks internal same-type ordinal correspondences medium rather than forcing the Korean TeX to satisfy a metadata oracle. These are checker cues, not defects or parity proof (`CJK-KO-P32-HARD-004`). A separate logging mistake also occurred: the first four difficulty records used a neat nominal `09:32:00` recorded-at value without a captured live-clock sample. `CJK-KO-P32-HARD-005` append-only-corrects their recording time to the actually observed interval; no substantive record was erased.

### Exact reproducibility authorities

- Structural JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper32_ko_translation_001_20260722\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 115 records, SHA-256 `9FAD66A5DC812CB0C65DA53B12527B3D65CF8338B3F914F3F8A69B258B2F7C56`; latest structural ID `NOE-P32-KO-U19-PARA-002`.
- Structural CSV projection: `...\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.csv`, SHA-256 `B2C9F003E4C5D721BB8F8974E72702E40C15C1787142DF38E2FBBFD31E5869B6`.
- Structural schema: `...\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.schema.json`, SHA-256 `63B7DE6DA62B6CF2EEF1D0C8E899DBACBB0245C0B331636FA52BAC4A799A177F`.
- Structural builder/validator and report: `...\evidence\structural_index\build_and_validate_producer_index.py`, SHA-256 `99281D43034A57061200DFE98878313B9DCC665ABC67073333545D5B15A16F11`; `...\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json`, SHA-256 `9FDF03E5FEF49FE7EE920A17C0783C361CEE56A2DEFA9CF8FEA273A210CF592C`, status `pass`, errors `[]`, with all machine-alignment warnings retained.
- Difficulty JSONL: `...\evidence\difficulty_ledger\DIFFICULTY_LEDGER.jsonl`, five append-only records, SHA-256 `3E1A446D929DBB0232ADA2D938D355513719F5D812DF7EC252387F566C74847E`; latest issue `CJK-KO-P32-HARD-005`.
- Difficulty schema: `...\evidence\difficulty_ledger\DIFFICULTY_LEDGER.schema.json`, SHA-256 `A033D3916671577B93C7ADCD9360153253E26583CA3D1083C05B3DE040962D8A`.
- Difficulty validator and report: `...\evidence\difficulty_ledger\validate_difficulty_ledger.py`, SHA-256 `3D5DE32F26FEAECEDFD41B05742D6F0E6B05BD824F1B4283E668F288117E1870`; `...\evidence\difficulty_ledger\DIFFICULTY_LEDGER_VALIDATION_REPORT.json`, SHA-256 `6F6A687B43EFE64332F40D90F1F08B396671736056DBB1E49DAE982121171A88`, status `pass`, errors `[]`.

No page image, crop, render, contact sheet, segmentation raster, before/after image, or model overlay was used or created for this translation-only route. The new visual-evidence count is therefore zero; no redistribution right or publication disposition is inferred.

### Transferable methodology changes and open failure modes

1. Require an explicit mathematical sense window before accepting any fluent CJK lexical attractor, even in a producer-only lane.
2. Keep unit-level routed pairing distinct from component-level parity: the former may be high confidence while the latter remains machine-derived and unreviewed.
3. Preserve unmatched target structures rather than editing translation text to make an extractor pass.
4. Treat a message tool's returned task ID as prompt acceptance, not receipt; inspect destination state once, retry once, then use a hashed shared-file return with explicit non-receipt language.
5. Capture append-only timestamps from a live clock. If precision provenance fails, append a correction with honest bounds instead of silently rewriting history.

Open risks are independent Korean algebra review of all provisional terms and clause structures, unresolved ko-KP standards, unproven manager receipt after transport failure, and checker adjudication of every medium or target-only structural correspondence. These P32 artifacts are methodology and translation-producer evidence only, not a final or reviewed Paper 32.

## Recovery-era translation-only P42 addendum — preserve the producer/checker/canon boundary (2026-08-04)

This addendum records lessons from recovering the Korean lane after broad project and machine disruption and then producing Noether Paper 42 as twelve closed Korean TeX units. The controlling state is deliberately narrow: all substantive wording in the preserved Paper 42 snapshot has Korean producer-draft coverage, while source checking, scan comparison, Korean review, compilation, rendering, assembly, packaging, certification, approval, and self-checking remain absent. The corresponding lane decisions are `CJK-KO-P42-001` and `CJK-KO-P42-002`; neither decision promotes draft coverage to checked or final state.

### What worked, with evidence

Reading the surviving EGA, SGA, Zenodo/GitHub, and Deligne task histories before resuming production supplied several controls that materially changed the work. First, the diplomatic source and any corrected reading must remain separately addressable; a translator must not silently turn an apparent German problem into a local source patch. Second, a coverage statement must name its gate: translation text, checker acceptance, build success, visual acceptance, corpus assembly, and publication are different states. Third, failed and superseded routes remain evidence. Fourth, stable semantic IDs and exact handoffs survive task loss better than a prose-only status report. Finally, bounded serial file operations are safer than broad searches and large archive inspection on a machine that has already suffered resource failures.

Those lessons produced a workable recovery route despite the disappearance of the former whole-authority path. The exact preserved German interval remained available as a 23,912-byte file with SHA-256 `B6BB3A6267BA8495FC19914A72768351E4923B13374634701AF3CBDE659883CC`; its earlier custody record binds it historically to whole-source lines 19863–20095, bytes `[1814639,1838551)`, and historical whole SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`. That is sufficient for an exact translation input, but not for this lane to certify present canon lineage. The missing current pointer was therefore logged as coordinate debt and sent to the one small-context German-canon owner, task `019fca5c-0e73-7c72-92fb-5b507b710598`. No duplicate canon task was created and no German text was inspected, adjudicated, or patched here.

The twelve-unit segmentation also worked. It preserved closed editable units, exact source-line slices, source and target hashes, an explicit `TRANSLATION-PRODUCER DRAFT — UNCHECKED` status, and one checker return rather than an assembled pseudo-final paper. `CHECKER_HANDOFF_U01_U12.md`, SHA-256 `8F8481987EEFD3041FE3328865D662A5254E5C125F586A86A5345F4610A41B98`, records every source/target pair and the prohibited in-lane gates. This makes the next actor's responsibility legible without asking the translator to become its own checker.

The Hangul-first terminology policy was similarly useful. It allowed provisional Korean wording while refusing to manufacture Hanja or ko-KP authority from Chinese, Japanese, or model familiarity. Trap-prone expressions were given explicit local sense windows, including crossed product, split algebra versus splitting field, order/maximal order versus ring of integers, trace-dual objects, localization, similarity, and historical endomorphism-ring language. Mandarin-Simplified dominance remains qualitative evidence debt rather than a readiness score, and no adjacent CJK target is treated as Korean evidence.

### What failed, why, and what remains held

The former exact whole-authority pathname no longer exists after corpus consolidation, while the shared current-authority pointer was known to be stale. This is a routing and lineage failure, not evidence that the preserved P42 bytes changed. The Korean lane cannot repair it without violating the producer/canon boundary. A replacement pointer and lineage receipt remain outstanding from the canon owner.

The Korean native/example-corpus junction is also broken after the cleanup. A narrow web probe did not produce authoritative primary Korean evidence for the most difficult historical algebra terminology, and secondary machine-generated search material was not accepted as validation. Consequently `오더`, `극대 오더`, `정수환`, `구역`, `주구역`, `자기준동형환`, `정칙인`, `디퍼런트(different)`, and `단순 정규대수(중심단순대수)` remain checker-facing producer choices. Their fluency is not evidence of Korean disciplinary acceptance. No DPRK standard claim is made.

Two tooling failures were retained rather than erased. The first PowerShell hash projection failed with `An empty pipe element is not allowed`; the corrected implementation uses an explicit output collection and is recorded as `CJK-KO-P42-HARD-007`. The first difficulty-ledger validator failed because `$lineNumber:` was parsed as an invalid variable reference; braced interpolation repaired it, with the failed attempt preserved in `CJK-KO-P42-HARD-009`. Neither failure changed translation text. They demonstrate that a validator's eventual pass proves metadata conformance only; it does not retroactively erase the failed route or validate Korean semantics.

The most important unresolved failure mode is organizational: there is not yet an independently identified Korean checker receipt for U01–U12. The producer handoff is durable, but dispatch or task creation is not checker acceptance. Likewise, the canon task has acknowledged the coordinate debt but has not yet returned a replacement current pointer. Until those receipts arrive, every Korean sentence, target formula transcription, terminology choice, structural pairing, and the substantive-coverage boundary remains unchecked.

### Exact structural, difficulty, and visual authorities

- Structural JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper42_ko_translation_001_20260804\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 91 records / 143,877 bytes, SHA-256 `8987DFDFFA4FDC53AC01E5961FC227463CD826F3ACE825642E04F20F5FC871E8`; latest ID `NOE-P42-KO-PLACE-DATE-001`.
- Structural CSV/schema/builder/report: `...\PRODUCER_STRUCTURAL_INDEX.csv`, SHA-256 `34FADA795BF19C90E85496061C33D4472126F7E09B805ACF9C160EAB03942C68`; `...\PRODUCER_STRUCTURAL_INDEX.schema.json`, SHA-256 `09DC18EF096A1BBC4C0275CD94933F246758FDA8F94AD388BBEFDFCFA37B567D`; `...\build_and_validate_structural_index.ps1`, SHA-256 `460CC3227911429981199D1C86D2D1D80D709412D922228254430471D86C1DE6`; `...\PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json`, SHA-256 `7966CE6845DCCF906A79F16D657F27E891A82BDFD59A893E0A7142966D430F45`, status pass and errors `[]`.
- Difficulty JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper42_ko_translation_001_20260804\evidence\difficulty_ledger\DIFFICULTY_LEDGER.jsonl`, nine append-only records / 27,330 bytes, SHA-256 `95BB2610CEAE9A19B3E9F7FC10BF1A8164C4D6A1D5784B055FA6BE7F0D783A0B`; latest ID `CJK-KO-P42-HARD-009`; states two resolved, six held, and one active control.
- Difficulty CSV/schema/validator/report: `...\DIFFICULTY_LEDGER.csv`, SHA-256 `09748E5C5287C84A20616CF2844782212357C05114BBC7DB3DCDC22E46DB47EC`; `...\DIFFICULTY_LEDGER.schema.json`, SHA-256 `21FC939E8CFF94AAD20CA774E8999D859ED4C65F23B15A20A6504CFDA9249704`; `...\validate_difficulty_ledger.ps1`, SHA-256 `7815ACAAA6ED28C753BF498BBC4A8EF3E0B4AFC704A19905E37502390B25F748`; `...\DIFFICULTY_LEDGER_VALIDATION_REPORT.json`, SHA-256 `708B83BCB8BDB69A1DC34A3A0FA7F043FEDCCD56ACD7D1FB40F883A4B86CCF37`, status pass and errors `[]`.
- Visual JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper42_ko_translation_001_20260804\evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.jsonl`, one record, SHA-256 `095F0D1DB460C61BEE2A23E63E89F04A14AE20CB3BA97ABD291F08CC84C3D351`; latest ID `CJK-KO-VIS-20260804-001`.
- Visual CSV/schema/validator/report/status: `...\VISUAL_EVIDENCE_INDEX.csv`, SHA-256 `7F9F1207A8C29912626EAA4A30B49E766DD9EB14252EBAE12D70C89ACA8F9E07`; `...\VISUAL_EVIDENCE_INDEX.schema.json`, SHA-256 `9076C65CC77CCB661EC79F38AD0EC23581FF142AF80632A656D033647AF81388`; `...\validate_visual_evidence.ps1`, SHA-256 `F8204219D3BBAA69C1FF29498271DF7ADED8F7654C78C169FE1E7B8AF0A32949`; `...\VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json`, SHA-256 `746E2383EAD5FA406DF08CF975AE64E178EAAFDC659B49EE9B9A458D3A2E57B4`; `...\VISUAL_EVIDENCE_STATUS.md`, SHA-256 `CB5C46945A6020744E3CF712556C5713ADCC63BF3926560EF80E6E14B5158238`.

The sole visual record is the user-supplied task-sidebar screenshot actually used to locate recovery histories: 34,480 bytes, 547 × 293, SHA-256 `D5B8D7C25A7C90E6515DF5C1DF63E8E4396EC9587B92BC96B0C0E28864DA716B`. It is private coordination evidence, not a Paper 42 source or render. Redistribution rights are not asserted, its publication disposition is exclude, and the count of Paper 42 equation crops, source-page images, target renders, contact sheets, before/after images, segmentation rasters, and model overlays is zero.

### Transferable methodology changes

1. Recover task history before resuming corpus production, then turn the recovered lessons into explicit state labels and routing controls rather than prose memory.
2. Permit translation from an immutable, hash-addressed preserved interval when the historical binding is documented, but record missing current-pointer lineage as debt and never describe it as current canon until the canon owner returns a receipt.
3. Keep exactly one small-context canon owner. Translators route only checker-confirmed defect packets and never patch or adjudicate German locally.
4. Separate full draft-text coverage from checker acceptance, compilation, rendering, assembly, and publication in every status field and handoff.
5. Split a paper into closed editable units with per-unit source and target hashes; do not make a monolithic assembled file in a producer-only lane.
6. Give every trap-prone term a source-local mathematical sense window and an adverse-evidence note. Adjacent CJK forms may describe lexical-attractor pressure but cannot authorize Korean.
7. Preserve failed scripts, bad oracles, transport ambiguity, and superseded routes as append-only difficulty evidence. A later green validator does not erase process failure.
8. Index hierarchy and cross-relations in JSONL and expose CSV only as a projection. Treat structural alignment as checker routing evidence, not semantic parity proof.
9. Inventory even coordination images that materially influenced research, but separate private custody from public disposition and never infer redistribution permission.
10. On resource-damaged machines, use exact paths and bounded serial reads. Avoid broad recursive searches, giant preservation ZIP inspection, and duplicate worker fan-out.

### Non-generalizable details and continuation conditions

The exact P42 interval hash, its historical whole-source coordinates, the twelve-unit boundary, the missing old path, the broken Korean junction, the 547 × 293 sidebar image, and the two PowerShell parser failures are recovery-specific details. The provisional Korean terms listed above are bounded producer choices, not corpus-wide prescriptions. The structural count of 91 and difficulty count of nine describe this snapshot only.

The next permissible state changes are receipts from an independent Korean checker and from the sole canon owner. Checker corrections must preserve the producer hashes and append supersession rather than silently replacing history. Only an independently confirmed German defect may be packaged for canon, using stable finding ID, exact work/unit/cursor, authority path/bytes/SHA-256, affected reading, proposed correction and alternatives, evidence, defect class, uncertainty, checker identity/status, and dedup state. No SGA scope is authorized. This addendum is methodology evidence and producer provenance, not review, canon adjudication, compilation evidence, archive handoff, publication approval, or completion of the Korean Noether corpus.

The durable methodology/handoff decision is `CJK-KO-P42-003`. Following that decision, the hash-pinned checker-assignment request was delivered to the active Chinese peer/coordinator task `019f757c-95a5-7030-8b00-38762b5cdbfc`, with an explicit prohibition on Chinese-lane Korean review, and the metadata-only/private-state notice was delivered to archive-maintenance task `019fc1e0-6261-72e0-8e16-1ec472b82f28`. Both connector returns establish destination task IDs only; neither proves reading, acceptance, checker assignment, archive incorporation, or publication.

## Paper 1 translation-only addendum — terminology clusters and byte-exact failure history (2026-08-04)

Paper 1 became the next non-overlapping Korean producer unit after Paper 42. The bounded lane search found one exact German custody snapshot and no Korean Paper 1 root. Three closed units now cover source lines 1--24, 25--59, and 60--80; Paper 2 is excluded. The controlling decisions are `CJK-KO-P01-001` through `CJK-KO-P01-003`. This is complete substantive producer-draft coverage of the preserved snapshot, not source checking, present-canon certification, Korean review, compilation, rendering, assembly, package readiness, or final-paper completion.

### What worked

Reusing the pre-existing custody segmentation was effective. It avoided inventing a new byte boundary while producing three mathematically coherent units: prior literature and the finite-system method; the module sequence and contraction theorem; and the form-series/reductant theorem with the final reduction methods. The exact German input is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper01_zh_translation_001_20260722\source\Noether_Paper01_CurrentGermanAuthority_interval.tex`, 8,082 bytes, SHA-256 `0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F`. Its historical binding is former whole-source lines 381--460 / bytes `[12505,20587)` / whole SHA-256 `443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27`; that binding remains pointer debt, not present-canon certification.

The strongest linguistic technique was to treat the historical invariant-theory vocabulary as a connected sense-window cluster rather than independent dictionary lookups. `Ordnung` and `Grad` were separated as `계수차수` and `변수차수` because the source itself defines their coefficient/variable roles. `Überschiebung` and `Faltung` were not collapsed: the first is provisionally `전이연산(Überschiebung, transvection)`, while the source-defined factor-pair replacement is provisionally `수축`. Historical `Modul` was retained visibly as `모듈` but explicitly held apart from later Noether `가군`, software modules, and modular arithmetic. `Formensystem`, `Bildung`, `Formenreihe`, and `Reduzent` were carried with local definitions and exact checker questions. This did not validate the choices; it made their risks reviewable.

The structural index also worked as intended. It records title, author, publication note, every paragraph and closed prose unit, six footnotes, five bibliography items, seven displays, three definitions, two theorems, two lists and four list items, transitions, units, and work hierarchy. Every record carries exact source and target line locators, file and LF-slice hashes, parent/order relations, cross-references, language, authority state, completion/review/publication state, and continuation cursor. The CSV is only a projection; JSONL remains the hierarchy authority.

The spreadsheet-artifact workflow improved the CSV projections without widening the claim. All three CSVs were imported through the bundled artifact runtime and checked for rectangularity, nonblank/unique headers, bounded region readability, and spreadsheet formula-error strings. Rendering was intentionally skipped because the controlling Korean role prohibits rendering. The result is a mechanical artifact-tool pass, not spreadsheet visual approval and certainly not translation review.

Finally, the external-state distinctions held. The Chinese peer explicitly confirmed it had no separately named Korean checker, performed no Korean review, and would not misuse the German canon task. Paper 42 therefore remains unchecked. Archive maintenance accepted Paper 42's metadata as pending/private and copied or published nothing; the durable receipts are recorded in `CJK-KO-P42-005`. That is a useful positive example of a real acknowledgment that still does not imply package or publication readiness.

### What failed, why, and how the failures were preserved

The first difficulty-ledger initializer failed before writing any ledger because multiline positional PowerShell calls lacked explicit continuation markers. That failure is `CJK-KO-P01-HARD-009`. Adding continuation markers allowed the one-time initializer to write nine chained records, but the first validator then rejected every record: the initializer had hashed each ordered object with a null `record_sha256` placeholder, while the validator removed the field. The 1,146-byte failed report, SHA-256 `9709B0CE22BC6AD0D88ED084A351930BE3C90CE6E99587C78686E51648896037`, is preserved and described in `CJK-KO-P01-HARD-010`.

The first hash-convention repair exposed a second problem. Parse-and-reserialize replay validated the original nine records but changed the canonical bytes of newly appended HARD-010. The second failed report is 732 bytes, SHA-256 `5169E6C2963EDEC3635AB7DB03C72E238FD4B225584D9BCADCD0D7A2A03EA0F0`, preserved under `rejected_attempts` and described in `CJK-KO-P01-HARD-011`. The final validator no longer assumes semantic JSON equivalence implies byte identity. It hashes each exact persisted UTF-8 JSONL line after replacing only the terminal self-hash value with `null`. No existing ledger line was rewritten.

This sequence matters methodologically. An eventual green validator did not make the first two validator designs retrospectively correct. Nor did it show that Korean mathematics was correct. It proved only that the final raw-byte chain, required fields, unique IDs, state controls, and CSV row projection are internally consistent.

The main substantive failures remain unresolved. The old whole-authority path is gone; no current pointer receipt exists for Paper 1. The Korean native/example corpus junction remains broken. There is no independently named Korean checker. Exact Korean historical invariant-theory evidence was not recovered, and neighboring Chinese/Japanese forms cannot fill that channel. `삼원 4차 형식`, `형식계`, `구성식`, `계수차수/변수차수`, `모듈`, `전이연산`, `수축`, `형식열`, `환원자`, and the nested reductant theorem clause therefore remain producer choices with explicit residual risk.

### Exact Paper 1 authorities

- Producer root: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper01_ko_translation_001_20260804`.
- Korean targets: U01 SHA-256 `48961F41A3C178968A5D2157F6FD5E756DAC7817555CAD07208C61E5A6643BE7`; U02 `52C02759CC6D08AA102DA366F7F148A4D148EC1066E2F81DE929CEE43A46DDDF`; U03 `ECEE0AB9E9D8C89D6A9B4FBBA63128FBE1990764847E01038AB894EF66C9DF54`.
- Checker handoff: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper01_ko_translation_001_20260804\CHECKER_HANDOFF_U01_U03.md`, 5,301 bytes, SHA-256 `13DFF87491574C2E8A1AB0F15D9DDDF3445CAD27E7FE14EC67CDB259349D7D52`.
- Structural JSONL: `...\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 45 records, SHA-256 `CAB2B7FF157B86AE9CD288A65FBF1B3F5149A19F540FB549A37B56761CCAF8F4`; latest `NOE-P01-KO-U03-LIST-ITEM-004`.
- Structural schema/builder/report: `...\PRODUCER_STRUCTURAL_INDEX.schema.json`, SHA-256 `E5761352D61341139AB23321420817E125371DB97E2E9C9F73516739D3D1CC12`; `...\build_and_validate_structural_index.ps1`, `C4DBC59A0378AFEA4C19407564293BD0AC51F850DB2C7B384CAAE757808E59DD`; `...\PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json`, `DB2535C47F5D1B6ABBF16FF9BD1E3D633AA43153B70C1744A874FC6F05B3B429`, pass/errors `[]`.
- Difficulty JSONL: `...\evidence\difficulty_ledger\DIFFICULTY_LEDGER.jsonl`, 11 records, SHA-256 `4B725D15BA858889C07E543FF29C2F12B22E24D03A846282CB8BB1E1E0C28D1E`; latest `CJK-KO-P01-HARD-011`; chain head `719892AD000C564729CF2B7856B210DDDD97C31FB26BD30390F0F3A35E2C71A0`.
- Difficulty schema/validator/report: `...\DIFFICULTY_LEDGER.schema.json`, SHA-256 `78C206B311DF7833E643989C731BDCF0605FA791D34C5601CAEE93E02C8A4DA0`; `...\validate_difficulty_ledger.ps1`, `45C62376F67054942C9256BE2BF15D9E33C0C87F6DD7B94403570F2EFF4A6548`; `...\DIFFICULTY_LEDGER_VALIDATION_REPORT.json`, `A58C41377BAC6BF5C979A3F048B7843F1223EC6BF3554BC6199CDE1EA346C59D`, pass/errors `[]`.
- Visual JSONL: `...\evidence\visual_evidence\VISUAL_EVIDENCE_INDEX.jsonl`, zero records / zero bytes / SHA-256 `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`; schema `1942DEFEE87DB627FA51FAE36596DB9214B9A0B7E29AD4A9ED463676A69EED76`; validator `81C18E336EB32CF18B21410859F5534B8E462B4DE02E70677EBDA73DAA5820AD`; report `4D12FBECEF4FD3AA4B5E89A51B2C5474927B83DF50FFCAD909273FE9E7C496E2`, pass/errors `[]`.
- CSV artifact-runtime report: `...\evidence\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json`, SHA-256 `5D058E8CF0CA1DA452D2FBE2283061F9971355462EA3ED6C7F5ADEFAC5A0A9D7`, pass. Structural/difficulty/visual CSV hashes are `7B5576B2E6C039F197AB5381A83B70B003D29D5A8F91CAD2A12F209FC1849969`, `39D295455DA354A844D143D23687911927DE73DB6AFDFBBB8E5C200C48A5FBF7`, and `3C951B6EEA7A4C640862D42134561550FC22C5DA0C40F83C4842372822D3E6E5`.

### Transferable methodology changes

1. Treat a historically dense terminology cluster as one graph of interacting decisions, not a list of isolated word substitutions.
2. When the source explicitly defines two false-friend terms, encode the distinction in the target and in a dedicated adverse-evidence record.
3. Keep historical `Modul` separate from later Noether module/`가군` language; same spelling across papers is not proof of same concept.
4. Preserve an operation-level distinction when the source separately introduces a general transvection and a factor-pair contraction process.
5. Make JSONL the authority for hierarchy/relations and CSV a checked projection only.
6. Specify append-only record hashing at the byte level. JSON object equivalence is not sufficient for reproducible evidence chains.
7. Preserve failed reports before changing validators, and append a failure record before claiming a green successor.
8. Use spreadsheet tooling for machine-readable projection checks only to the extent allowed by the controlling role; a CSV import pass is not a visual or semantic pass.
9. Let exact interval custody sustain translation during pointer recovery, but label the interval as preserved/historically bound until canon returns current lineage.
10. If no independent checker exists, keep the draft visibly unchecked and continue disjoint translation rather than fabricating reviewer independence.

### Non-generalizable details and open failure modes

The 8,082-byte P01 interval, its three inherited segment hashes, exact 1907 invariant-theory vocabulary, two explicit linear-relation displays, four Faltung classes, 45 structural records, 11 difficulty records, and PowerShell hashing failures are Paper 1/recovery-specific. They should not become universal Korean terminology or tool assumptions.

Open failure modes are an eventual canon binder that changes the historical interval's current status; a Korean checker preferring `쌍이차형식` or different classical-invariant terminology; clause-level error in the reductant theorem; formula or footnote topology defects invisible to producer hashing; later assembly macros differing from the uncompiled snippets; unresolved ko-KP standards; and a growing backlog of unchecked Korean papers. No Paper 1 visual exists, so no visual evidence is available to support layout claims. This addendum is methodology evidence only and does not promote Paper 1 or Paper 42 beyond their recorded producer/private states.

### Paper 1 authority-binder correction after the retrospective snapshot

The Paper 1 pointer debt described above is now coordinate-closed, but no Korean state changed. Canon receipt `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\noether\07_german_canon_control\receipts\KOREAN_P01_U01_U03_BINDER_20260804.json`, 6,558 bytes / SHA-256 `8CA3EBA2A4C766191614E94501E2D2A2242400ED2B3CD66401B20EB07E5EE66D`, independently classified the stored 8,082-byte LF interval as normalized-identical to the current 8,162-byte CRLF Paper 1 span. Decisions `CJK-KO-P01-007` and `CJK-KO-P01-008` preserve the distinction between immutable interval binding and live-pointer supersession. Pointer v002 operationally replaced v001 and registered the binder without invalidating it; later pointer v003 likewise changes routing metadata, not Paper 1 bytes. The methodology change is to bind preserved units by exact normalized content and retain pointer versions as immutable receipts instead of requiring a missing historical whole-file ancestry edge. Korean U01--U03 remain independently unchecked.

## Paper 41 translation-only addendum — coupled terminology, exact binders, and failure-chain repair (2026-08-04)

Paper 41 is now covered by twelve editable Korean producer units through all substantive snapshot lines 1--151. Lines 153--154 are TeX control matter. Every target remains `UNCHECKED`; no source/scan/Korean/formula review, compilation, rendering, assembly, package, certification, approval, or publication occurred. Controlling decisions are `CJK-KO-P41-001`--`004`; the latest difficulty record is `CJK-KO-P41-HARD-016`.

### What worked

The strongest authority control was obtaining a coordinate-only canon receipt without asking the translation lane to adjudicate German. The preserved P41 snapshot at `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper41_zh_translation_001_20260722\source\Noether_Paper41_CurrentGermanAuthority_interval.tex`, 27,110 bytes / SHA-256 `C265058425E5E2D1A2289CC03A9DDEDDDF4803A3215DC3F173B93E7AB69D60ED`, normalizes exactly to ED0001 lines 19789--19942. Canon receipt `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\noether\07_german_canon_control\receipts\KOREAN_P41_U01_U12_BINDER_20260804.json`, 9,522 bytes / `95D0E69B6D32FD93801C3FDC4C519FAA9AB7CA867538E1CD9E2096EFAB253A91`, closes coordinate debt while explicitly leaving Korean untouched. Pointer v003, 15,345 bytes / `932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197`, merely registers this binder. The R823 `Analogon` / later-layer `Anologon` difference remains lineage evidence, not a translator defect; this demonstrates why branch differences must not bypass an independent checker and the canon finding schema.

Closed-unit production also worked. U01--U12 retain exact source-slice and target identities and expose one continuation cursor. The checker request `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper41_ko_translation_001_20260804\CHECKER_HANDOFF_U01_U12.md`, 18,534 bytes / `430FAB4BF94DB1C4FA7B659E44B73DE714E2F56C608E6BD9716F66BCEEB40728`, carries the complete identity table, the canon receipt, the structural/difficulty/visual authorities, all known failed paths, and ten exact return requirements. It is a producer handoff rather than a reviewer receipt.

The useful linguistic method was to model related historical terms as families. `Hauptgeschlechtssatz`, `im Minimalen`, and `im Kleinen` share one scope window; `verschränktes Produkt`, `verschränkte Darstellung`, `Faktorensystem`, `assoziiert`, and `Transformationsgrößen` share a crossed-product/cohomological window; `Klasseneinteilung`, `Hauptklasse`, `Einsklasse`, `Hauptgeschlecht`, `ambig`, and `Basiselement` share an ideal-class window. The producer choices remain provisional, but grouping them prevents a reviewer from approving one fluent token while leaving its mathematical neighbors inconsistent. Mandarin-Simplified dominance remains a qualitative evidence-shelf risk only. Lexical-attractor basins are recorded in the lane ledger/crosswalk layer, not injected into the typed structural schema, and no Chinese or Japanese form authorizes Korean.

The structural index and zero-image visual index worked as bounded research evidence. The structural authority is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper41_ko_translation_001_20260804\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 129 records / 213,997 bytes / SHA-256 `D825FC810574A54CDD3B7C97370EC5FFCA8F21A567664D721C2C6FA8EFF021F7`; latest `NOE-P41-KO-U12-RECEIPT-001`. Its schema, builder, and PASS report hashes are `14800B151BC67B7E5E2CF6DD7DD3B5CE4C44DBFE860B4934473F02FD07575FDD`, `26F7DCBFE1F9D407A9845BD331F02B60D4D7026F5B389C130B4CC50F5852FC85`, and `38E0F3E3B5CC2552863F9A2970F5424F4E03D0059156F5DF4759242F5A06E751`. The visual authority `...\evidence\visual\visual_evidence_index.jsonl` is legitimately empty, SHA-256 `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`; its schema/validator/report hashes are `C1F066E21053961F3119A29FCDCA5F6A88808B1E168A2C57BA03EC134F0E5F60`, `D17340DC5A05FC04C3D3908D92EB49325C84C11B1E4BB4A211D735AE29CA47CB`, and `FEC4FB4D994532487290AF34E90AAC2F8B97E93C498EA4C2FFC1C55342599349`. Zero is evidence of non-use, not visual acceptance.

The three CSV projections were imported with `@oai/artifact-tool` and passed rectangularity, unique/nonblank header, bounded inspection, and spreadsheet formula-error scans. The exact report is `...\evidence\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json`, 2,731 bytes / `91C2B03308ACD722223B3CE2A909F62BA17C7DE2BAC1569CD541E7E2F02CDE3D`. Rendering was intentionally skipped. This validates metadata-table shape only.

### What failed, why, and what changed methodologically

The first U01--U04 producer write lost inline `\(` and `\)` delimiters because TeX was embedded in ordinary JavaScript strings. Those files were repaired before a failed-state hash existed, so the absence of a pre-repair identity is itself recorded adverse evidence. U05--U08 reproduced the same error but did have frozen damaged identities; the repair restored only missing delimiters and retained the before hashes. U09--U12 used doubled escaping and did not recur. A separate Markdown choices file lost TeX delimiters through the same mechanism. The transferable change is to treat every TeX-bearing transport surface—target TeX and Markdown evidence alike—as escape-sensitive, preserve first-return hashes when they exist, and never reconstruct a hash that was not captured.

The difficulty-ledger initializer then demonstrated why a self-hash is not a chain hash. Its first twelve records had valid self-hashes but records 002--012 all pointed to null predecessors because assignment inside `Add-Record` was function-scoped. The failed JSONL, CSV, and 1,155-byte FAIL report (`7852762AB945721AA34B812E1A6211C9DD5EFECE79A7B4D571ED15591BEFAD77`) were preserved. An attempted corrected rerun was properly blocked by the append-only guard; the invalid active files were moved rather than deleted. Later, a compact `Join-Path` array bound an object array to `AdditionalChildPath`, and the known direct `foreach`-to-pipeline parser error recurred in a parallel handoff sweep. All four events survive as `CJK-KO-P41-HARD-013`--`016`.

The current append-only difficulty authority is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper41_ko_translation_001_20260804\evidence\difficulty\difficulty_ledger.jsonl`, 16 records / 72,530 bytes / SHA-256 `4C5195896923C6816D695A0AA21107F9FD27B19EBAAC9DD61EDECDCDFADB8488`; chain head `DC6FA2D8B46A1C229AE42313D0198FBC8D4650D83ABA973EAC60167C888810B3`. Schema and validator hashes are `9E658939B2CE4317146B0381637934C870CFB8ED3AD5C217485687A9D4568312` and `4E1FC01DE3C0867FBF21AE30EF1CE3DC69BE7B2F216548A1E3D6111A88AEAEA8`; the 16-record PASS report is 603 bytes / `D02B4D228B5588C3E8BEFE17945D81391510470B72A744043DA06641266CD3EE`. A later green report proves exact-line self-hashes, chain linkage, required fields, and CSV identity only; it does not erase the failed build or validate translation.

One immutable structural-index limitation also remains visible: the index was frozen before the canon binder arrived and therefore carries the historical-pointer debt in its authority-state field. Rewriting all 129 records would destroy the producer snapshot. The binder note, mutable status, checker handoff, and decisions `CJK-KO-P41-003`--`004` supersede that one metadata state without pretending the index was created later. The general rule is to append or layer authority-state corrections around immutable evidence rather than silently refreshing historical records.

### Transferable heuristics and open failure modes

1. Obtain exact coordinate binders from the separate canon owner; do not let a translator adjudicate normalization, ancestry, or branch readings.
2. Translate coupled mathematical vocabularies as families with shared sense windows and checker questions.
3. Treat TeX delimiters as transport-critical bytes on every target and evidence surface; freeze genuine before identities whenever possible.
4. Validate record self-hashes and predecessor linkage separately, and preserve invalid initial ledgers before rebuilding an initialization artifact.
5. Keep append-only guards enabled. Move invalid artifacts to stable failure names instead of deleting or overwriting them.
6. Encode recurrent command failures even when the safe retry is already known; recurrence is evidence that the heuristic has not propagated.
7. Preserve immutable structural metadata and append an explicit authority-state supersession when a later binder arrives.
8. Record zero visual use with a validated zero-record index; never convert non-use into visual QA.
9. Keep CSV import validation, structural integrity, Korean review, compilation, rendering, and publication as distinct gates.

P41-specific details—the twelve-unit split, historical `im Minimalen`/`im Kleinen` wording, crossed-product vocabulary, R823 token divergence, the exact 154-line EOL delta, and the PowerShell/JavaScript failures—do not establish universal Korean terminology or tooling rules. Open risks include all Korean wording and formulas; the unresolved `극대차수` versus P42 `극대 오더` conflict; possible weakness of `연관된` for cohomological equivalence; `주류`/`일류` lexical ambiguity; no Korean-native historical corpus; no verified Hanja expansion; no ko-KP evidence; no independent Korean checker; and no compilation/render evidence. The exact `STATUS.md` snapshot is 8,380 bytes / SHA-256 `273E928AAAB7B1230BA5E7CF8E4AF85CEE97CB0BEDD859A057036E417E6D6EE0`. This addendum is methodology evidence and producer provenance only.

### Archive-disposition correction — unchecked mathematics is immediately publishable

PROJECT_COORDINATOR's later archive-wide instruction supersedes every generic Korean-lane `pending-private`, `public-excluded`, `not for publication`, or `not publication-ready` disposition insofar as it acted as a release hold. The exact durable receipt is `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\00_lane_control\KOREAN_ARCHIVE_PUBLICATION_POLICY_RECEIPT_20260804.md`, 2,552 bytes / SHA-256 `9BD4FEA2B6116896DDCAA0840F159965E5AD3AB478C37EF7EE99CA144B2D83AB`; decisions `CJK-KO-ARCH-001`--`002` apply it. Unchecked, incomplete, uncompiled, unrendered, and unreviewed remain mandatory factual labels, but none is a publication veto. Archive maintenance owns coherent snapshots, public projections, privacy/security remediation, and publication. The Korean lane still does not source-check, Korean-review, formula-check, compile, render, package, certify, approve, publish, or mutate GitHub/Zenodo. Publication permission and QA evidence are independent axes.

## Paper 5 translation-only addendum — direct current-authority slices and evidence-identity discipline (2026-08-04)

Paper 5 now has complete producer coverage in four editable units under `CJK-KO-P05-001`; the corrective metadata decision is `CJK-KO-P05-002`. The exact current-authority interval is ED0001 lines 4535--4573, 8,185 LF UTF-8 bytes / SHA-256 `99BD68A8DBD9861EFF0CDBE26CB365C3306EDF15BD93A6C4C10B9F25419D5CAE`; line 4573 is blank and line 4574 `\clearpage` is excluded. Targets U01--U04 remain `UNCHECKED`, with SHA-256 `EEB39C3A693410823F66A75BCE7DBB9906F35637BFFF87A55CE4A7B873A6F203`, `62D644153874FFE07C839102D5EF222BCED55F693C1BA6E8E9FF318A670F8DEA`, `2B7ADD81855DD9D06A1D2D17249F32F5D7BBDB458F7474E0BB7BC3F14A5FFA89`, and `8A50F7549C23A50A6A824C97763941535D12061EE08E32D2EC1D3F678FE4CA6B`.

The main translation lesson is that this short paper is lexically dense despite its size. `Zahlkörper` explicitly reaches all complex numbers and cannot automatically inherit the later number-field sense of `수체`; `Gattungsbereich` and `affektlos` are historical terms whose safest producer form retains the German witness; `Integritätsbasis`, `ganze rationale Verbindung`, `relativ ganze Funktionen`, and `Resultante` form an interdependent algebra/function-field cluster. Exposing those sense windows in `TRANSLATION_CHOICES_U01_U04.md`, SHA-256 `8C431205D0EED3A1500054B114947262D34E89AD688ABE253C3A51706C41ED3E`, worked better than silently selecting fluent modern Korean. The unresolved choices remain checker questions, not corpus-wide headwords.

Direct current-authority custody also worked without duplicating a source snapshot. `SOURCE_CUSTODY.md`, SHA-256 `8C3F5AF22CDBB334C987B3AD113402152246AA15C4894308DA9500F8ACA15896`, retains the exact whole path/hash, body interval, and four source-slice hashes. A later bounded lookup wrongly assumed a producer `source\` directory and failed. The missing duplicate is not a source defect: a direct, content-addressed authority locator can be sufficient if every slice remains reproducible. A coordinate-only canon binder remains desirable as an independent receipt.

Three tooling lessons were concrete. First, the helper name `H` resolved to PowerShell `Get-History`; task-specific function names avoid collisions with shell aliases. Second, two nested-interpolation patch attempts failed before file creation and remain in the six-record difficulty ledger. Third, the first retrospective log expanded abbreviated worker-return hash prefixes into plausible but fabricated full visual hashes. `CJK-KO-P05-002` appends the correction after direct local rehash; the correct visual schema and builder hashes are `7178A862A0ACD5D778E6FBD8B42611314BB8A516E14765A947681CC6A8D914F8` and `33A5A28D0E8099BD216FEF9CB68FFB5BEC4D76DF72FD6E95389115009455D1D0`. The methodology rule is absolute: never expand an abbreviated identity; rehash the artifact or leave it explicitly unknown.

Exact reproducibility authorities:

- Structural JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper05_ko_translation_001_20260804\evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 41 records / 68,902 bytes / SHA-256 `3731E3FC72CC773D75F7AC6681E2B55EB0EBF786A857F363D726E6D5F41D32B0`; latest `NOE-P05-KO-U04-PARA-003`. Schema/builder/PASS-report hashes: `F4FCBF4144A0E04670A63BC4CFAB66C3007AA5953A957475776E13F2335D296D`, `AD4A6880CC2E02555A29385DC80DABA2F8D4398CD1AA8BEAA71222D9F54CD9C6`, `77311B85095CC38E58F463D06B0554E6FDFFB98B99F97BC7A34C73417F6348E2`.
- Difficulty JSONL: `...\evidence\difficulty\DIFFICULTY_LEDGER.jsonl`, six append-only records / 19,327 bytes / `9BBC4D69CC597945B2A403165298BAB28D6DA9506388CA26D462FF479D556CFB`; latest `CJK-KO-P05-HARD-006`, chain head `020262B539E0D82FC1C9BAF9916E902465C6F755C3254FE888EDE54CEC42EF10`. Schema/builder/PASS-report hashes: `284C0CDF7295E7DD0D45371F2764A255DD8A76C62CB486CA1A291C194575A9E2`, `5ECC4AB413AE26679E6B1819BCE87B1320E9BB6E007BB961510F62ABD061D0D1`, `1FF2763A41C4C415EE7E7DA414656D2D813F735DA3A8ADD826236E8D4EAD23A7`.
- Visual JSONL: `...\evidence\visual\VISUAL_EVIDENCE.jsonl`, zero records / zero bytes / `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`; correct schema/builder/PASS-report hashes `7178A862A0ACD5D778E6FBD8B42611314BB8A516E14765A947681CC6A8D914F8`, `33A5A28D0E8099BD216FEF9CB68FFB5BEC4D76DF72FD6E95389115009455D1D0`, and `86F3CBD7D6BDF4B8BA84A9DC65F145A98711A22705F147D4E2CF90A2B5BAB692`.
- CSV artifact report: `...\evidence\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json`, 2,720 bytes / `D968079EC46718F85F4BFC1EC325B8FFFEBECE152D110B1F57DF27BE3C5A40E2`, pass with no rendering. Updated checker handoff: 4,980 bytes / `437EDE886B9CC81C1AF31D280069ED2AD4E5C47CAE83A293F8B2755EDBD94F4D`.

Open P5 failures are every translation/formula/note/bibliography claim, the historical vocabulary cluster, Hanja policy, ko-KP evidence, compilation/rendering, and independent checker return. Immediate archive publication must retain those labels. The exact four-unit split and PowerShell alias failures are P5-specific; the transferable rules are content-addressed direct custody, terminology-family review, task-specific helper names, and mandatory direct rehash of any abbreviated identity.

## Paper 7 translation-only addendum — do not invent failures; preserve dependency stalls (2026-08-04)

Paper 7 has complete producer coverage in eight units under `CJK-KO-P07-001`. The exact interval is ED0001 lines 5842--5954, 8,511 LF bytes / SHA-256 `8C5D6E8DDF24B33C5AF719F59C4CEFA0B9CEABB61960E2AC30F888CB1206AFBC`; blank line 5955 and `\clearpage` 5956 are excluded. The eight targets total 17,752 bytes, ordered-concatenation SHA-256 `35790D0EB6267A26A3F4A175DAF58E02279C9A54DF09CDA3A24547A547093673`, and remain `UNCHECKED`.

The most useful content method was to keep several invariant-theory false-friend families visible: `vollständiges Formensystem` versus generic completeness, historical `Modul` versus later module/`가군`, `Variablenreihe`, `einförmig`, `Galoissche Resolvente`, `Potenzsumme`, `rationale Darstellung`, and `Relative`. The handoff also isolates the recurring `ganze rationale` / `rationale` contrast. As with P41/P05, Hangul-first forms are producer choices; no Sino-xenic neighbor or Mandarin-dominant shelf authorizes Korean, and ko-KP remains unclaimed.

No P07 TeX-creation or target-write failure was observed, and the ledger did not invent one. That negative discipline matters: a difficulty ledger is not a quota. It still records 13 hard terminology/authority/locale/note/provenance risks. A real fourteenth failure occurred later when the official dependency locator stalled without a payload and was terminated; CSV validation then used the already-provisioned bundled-runtime junction. `NOE-P07-KO-HARD-014` preserves the failed route and recovery. The rule is to distinguish “no target failure observed” from “no production failure at all,” and to append later tooling failures without rewriting earlier claims.

Exact reproducibility authorities:

- Structural JSONL: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper07_ko_translation_001_20260804\reproducibility\structural\STRUCTURAL_INDEX.jsonl`, 59 records / 91,199 bytes / `B4A20A541AE3EDEA8FC29654D7D5A73EC0396A1C84C974A16F42F841E095FA6D`; latest `NOE-P07-KO-STR-059`. Schema/builder/validator/PASS report: `DE202CA1EC2F65CF6F99F30DE1313C15EEBBAC6265B8E025C2D6CB43B9CC2D4D`, `80A60B9138C316CFAFEC6740234D96C73294673F04B7142E09ACC9D61103C6B9`, `DC929565DD04DC2101883AA443B96C74AE79116B6E6578C752F78412BB1201C9`, `DF053054D166E3209B6615F46F7BCE53DCD2EAC20B5FAFF5E4B8D5F4E9896C21`.
- Difficulty JSONL: `...\reproducibility\difficulty\DIFFICULTY_LEDGER.jsonl`, 14 append-only records / 50,750 bytes / `441A403E59ECC44C9560EDC9A4A714C568199D7BF2D66832BB9ABB4CF4DA870A`; latest `NOE-P07-KO-HARD-014`, chain head `90700843478385C977DF7DBF8D95461BA47B04F43FC034188F3809C7B309D317`. CSV/schema/validator/PASS report: `BA2B2FD5BE2B4730EB1053DDA1858873BC44DE682810ADBC76F123F8B930C11D`, `FF51EAB3319E30B3421F5263095494CE6D549A35154495A952301FACB3577C8E`, `622D1BB0A27782EB771D8100F4CD67CCB661836A748D9E80328C5B5CE8D1CEDF`, `B5424228B24F48FA998C2416E1F1044597B9AFD37264F0D61A61281DB2EA072B`.
- Visual JSONL: `...\reproducibility\visual\VISUAL_EVIDENCE.jsonl`, zero bytes / `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`; CSV/schema/validator/PASS report: `A6DC57F88A034746480FA769D588E1F6247695AA5C252A9F41A127F40DD6B302`, `AC33A048E4A984EDD32BD13C15C2AE27E4AAF228AD1C734D1B6DA8B2C7E582C7`, `A53F8F7EFD8A456E4BEE0E3802A42F5ABCA92A89C793B7E03203D24BE8C33CA5`, `54D5244F75F57266413F73EDF34150797A76B0B22EEE23932721DF13BB9B94D0`.
- CSV artifact report: `...\reproducibility\csv_artifact_validation\CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json`, 2,728 bytes / `B2D87D6880252915EDD42B29E1F4B608CE5DE53F66109964F5804A6E46A11DC1`, pass/no render. Updated status and checker handoff hashes: `9A38AAFFC4619918956EFA37A72BDAA22307B08C652C8B222779DFB8557EA954` and `3B8155E63855D6F565BCFD9FD7E5F210A7263CC33778509E09D8C4FEAD2D8CD2`.

P07's exact eight-unit boundary, early invariant-theory vocabulary, and dependency-locator stall are non-generalizable details. Transferable rules are to preserve negative evidence honestly, append later failures, keep note/bibliography topology as checker work, and make immediate archive eligibility coexist with explicit missing review/build/render states. Coordinate-only canon binding and independent Korean review remain the next receipts.

## Paper 3 — deterministic evidence requires host control and semantic ledger validation

Relevant decisions: `CJK-KO-P03-001`, `CJK-KO-P03-002`. Authority interval: ED0001 whole lines 3573--3608, 8,277 LF bytes, SHA-256 `E600FD2A19ACA22F43D54FB65C61B79172B12FE5AB09446A2C9C9B8CACD26E7D`. Producer root: `${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper03_ko_translation_001_20260804`.

What worked was separating the three closed translation units from all mechanical evidence generation and then rehashing the targets after the evidence pass. U01--U03 stayed byte-identical and `UNCHECKED`; the structural builder could therefore be rerun repeatedly without creating a false target revision. The final hierarchy is `evidence\structural_index\PRODUCER_STRUCTURAL_INDEX.jsonl`, 148 unique records / 310,637 bytes / SHA-256 `F2D3B6D6FE6DE0837AFF24CF2A314B8A7F8C4F6DFE78D8E2D91E8AD5B052EAE0`, latest ID `NOE-P03-KO-U03-FORMULA-014`. Its schema, builder, validator, and PASS report are respectively `PRODUCER_STRUCTURAL_INDEX.schema.json` (`35D0A541A32F2334E39E6014E0324C6B7FCB79DAC6944AFCA4498ABFA4440E7B`), `build_structural_index.ps1` (`A1A097D8DEBFEA40B5BBC59F941600481ECD0D056CB720B79161295D7263C8BD`), `validate_structural_index.ps1` (`27042B5CE5027011EAE046E9CEA5569B7FF1946234EC1B834C009A5517068F77`), and `PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json` (`AA04DD48DED0E2D0233F9167275F8391B5AD3DEA3BBA9489D9959B71C1162E8E`). This is the exact index/schema/validator path set required for continuation.

The hard parts show why a green final report is not enough. The append-only ledger `evidence\difficulty\difficulty_ledger.jsonl`, 14 records / 57,815 bytes / SHA-256 `861F7C2B62696214AABAE435FCD3A97B77E291495BAB549F98DFEBDAC2803DF9`, ends at `CJK-KO-P03-HARD-014` with chain head `3CDDEDED77A410B39E35FDC8A0B221A5546512ADCC6EDAF70F478200B8EFDCA8`. `HARD-011` preserves an initializer `ReferenceError` before any patch. `HARD-012` preserves two bounded dependency-locator stalls. `HARD-013` is especially transferable: a syntactically valid, hash-valid record still carried semantically mangled fields, so chain validation alone could not authorize the metadata. The repair appended a corrective record instead of rewriting `HARD-011`. `HARD-014` then recorded the exact bundled Node/dependency paths and successful no-render CSV inspection. The schema/validator/report are `DIFFICULTY_LEDGER_SCHEMA.json` (`DCF582F0C91DDA02FC89F0E1E2D27D2F5FB5AEB714E7755CA091DBDD3696410C`), `validate_difficulty_ledger.ps1` (`024275130948CC2FD6F4A13740DD66EE37849671A7D043718A01991912D47402`), and `DIFFICULTY_LEDGER_VALIDATION_REPORT.json` (`489E8E4803CC3059D9A0DA3EE17C68BEE0A6C7A46E354D9C3F8FA4ADFDA8CC60`). The structural build notes also retain dependency-discovery, fragment-bound, scalar-count, null/empty serialization, and Windows PowerShell 5.1 host failures.

Transferable heuristic: pin the PowerShell major version for deterministic JSON/CSV generation, capture a pre-run target manifest, and make a second stable run the acceptance criterion after any host-induced projection mutation. Validate both syntax/hash topology and selected semantic invariants in difficulty records. Dependency discovery should be bounded; when it stalls, obtain the runtime from the workspace loader and record both the failed calls and the resolved exact paths. For Node ESM, `NODE_PATH` alone is insufficient for bare-import resolution; an in-memory mapping to the exact bundled artifact entry point can validate the unchanged script without adding a repository shim. No-render CSV validation is an integrity check, not visual QA.

What is non-generalizable is the Paper 3 vocabulary and topology: the three-unit segmentation, numeric-versus-Hangul arity variation, `Reihe` family, source-defined `Matrizenprodukt`, `Reduzent`, and `Normalform` choices require Korean specialist review and cannot be promoted from a mechanically valid index. The zero-visual evidence is exact but narrow: `evidence\visual\visual_evidence_index.jsonl` is zero bytes / SHA-256 `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855`; its schema/validator/report are `VISUAL_EVIDENCE_SCHEMA.json` (`090B4CB59AE72D59B4AA7E754B4CC35A80EAED41A83075F4EAC2653E812347AA`), `validate_visual_evidence.ps1` (`D3078D466402DD61288E741B32C4BD2AC051209CEA818AE8BA8E35D09BFC15DE`), and `VALIDATION_REPORT.json` (`FEC4FB4D994532487290AF34E90AAC2F8B97E93C498EA4C2FFC1C55342599349`). It proves only that this producer used or created no image.

Concrete methodology changes: add an explicit host/runtime field to future structural and CSV reports; make semantic spot assertions mandatory for append-only difficulty validators; always retain the first failed report beside the canonical successor; and include target byte-stability in the final evidence-freeze receipt. Open failure modes remain Korean terminology drift, formula transcription, source fidelity, missing independent checker, missing compilation/rendering, and the possibility that a structurally complete index misclassifies mathematical hierarchy. None is resolved by the 148/14/0 PASS counts.

## Immediate publication with honest incompleteness is a preservation control, not a quality claim

Relevant decision: `CJK-KO-ARCH-005`. Archive maintenance published bounded Korean P01/P05/P07/P41/P42 snapshots on the existing Noether concept as record `21783727`, version DOI `10.5281/zenodo.21783727`, concept DOI `10.5281/zenodo.20412587`, version index 172. The durable public-readback receipt is `${PUBLIC_DOCUMENTS_ROOT}\Codex\2026-05-26\there-is-currently-an-ongoing-process\wt-ega-p138-closeout-20260804\manifests\published-zenodo\20260804_korean_noether_p01_p05_p07_p41_p42_record_21783727_public_readback.json`, 72,424 bytes / SHA-256 `C2D55D8CFBF1076601783E44472859168BBD1F4F0642A5BBC801D6FFC79DA427`.

What worked was keeping publication state orthogonal to review state. The live surface retains `UNCHECKED`, uncompiled, unrendered, unassembled, and unreviewed labels; anonymous raw readback matched all 78 new direct files, all five snapshot ZIP member sets replayed, and no duplicate concept or live draft remained. Twenty inherited predecessor files remained byte-exact. The private P42 screenshot bytes stayed excluded while exact exclusion metadata was published. Thus immediate release improved preservation and reproducibility without manufacturing Korean or mathematical validation.

Transferable heuristic: archive a coherent bounded snapshot as soon as exact identities and honest state metadata exist; do not turn missing review into a release veto, and do not turn successful publication/readback into reviewer approval. Private/security-sensitive non-mathematical evidence should be represented by public-safe hash/coordinate/exclusion metadata while its bytes remain out of the public projection. Archive maintenance, not the translation producer, should own path normalization, public projection, existing-concept mutation, anonymous readback, and duplicate-draft checks.

The non-generalizable details are Zenodo record/version numbers, the inherited default preview, and the P42 screenshot exclusion. Open failure modes remain future-version lineage, independent Korean review, builds/renders, and ensuring that later incomplete snapshots continue to carry their state labels. Publication proves distribution and byte replay only.
