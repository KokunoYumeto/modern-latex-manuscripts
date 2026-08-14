# Interlanguage CJK mathematical notation backend standard

Version 1.0.0. Normative words **MUST**, **SHOULD**, and **MAY** are used deliberately.

## 1. Scope and canonicality

The shared object is a document-mechanics backend, not a pan-CJK mathematical language. It can be project-canonical for formula serialization, source binding, note relations, assets, build reproducibility, extraction, and render validation. Terminology, grammar, morphology, punctuation, and prose remain locale-governed.

Canonicality states are typed:

- `shared_mechanical`: a language-neutral structure or mechanism whose validity does not depend on a target lexicon; its record MUST state whether it has one-lane replay, cross-lane replay, or general-standard support, and one-lane replay MUST NOT be described as cross-lane empirical validation;
- `locale_profile`: supported only inside the named language, variety, script, work, and sense window;
- `candidate`: useful comparison evidence without authorization for production;
- `absence`: a bounded search or corpus audit found no qualifying evidence;
- `rejected`: adverse evidence defeats the proposed rule.

No scalar readiness or majority vote is permitted. Human/community review is optional and nonblocking. It may change a claim's social-validation status, but its absence MUST NOT block publication or mechanical adoption and MUST NOT be disguised as certification.

## 2. Shared source and formula contract

Every admitted unit MUST bind:

- immutable source and target identities, byte counts, hashes, and exact unit loci;
- source authority/version and target language/profile;
- changed loci and their typed reasons;
- control-sequence, environment, label, reference, citation, and note relations;
- formula obligations by stable ID, not only aggregate counts;
- build, extraction, and visual evidence as separate states.

Formula comparison MUST preserve ordered operands, operator and relation kind, arrow direction, Greek-letter identity, Fraktur/Roman/calligraphic family, primes, bars, delimiters, subscript/superscript attachment and scope, quantifier scope, matrices, equation labels, and source-associated punctuation.

A formula-count match MUST NOT substitute for a token/tree comparison. Declared target repetitions, prose-bearing formula spans, and verified source corrections MAY differ, but each exception MUST have a stable ID, exact locus, rationale, and before/after evidence.

Math delimiter parsing MUST be escape-aware. In particular, the second backslash of `\\[0.6em]` MUST NOT be treated as a `\[` display opener. A protected-math scanner MUST expose the arguments of declared prose-bearing commands to the locale text layer without changing their surrounding mathematics. The replayed defect proves this requirement for `\hbox{...}`; an adapter SHOULD explicitly declare other supported commands such as `\text{...}` and `\mbox{...}` and test their nesting.

UTF-8 and NFC MUST be validated. NFKC or compatibility folding MUST NOT be run across mathematical or locale text, because it can erase character, width, and style distinctions. Unicode character identity and displayed glyph identity MUST be treated separately.

## 3. Source notes and exceptional glyphs

Source-note apparatus SHOULD be represented by three semantic operations:

- inline mark plus text;
- separated mark and text;
- source-numbered display or apparatus entry.

The ledger MUST state that every source note is retained exactly once and may record an edition-specific placement. A backend MUST NOT force one visual placement across languages.

An unsupported or historically specific printed glyph SHOULD be a hash-pinned asset behind one semantic macro when Unicode/font substitution is not faithful. The asset's source, crop/mask method, dimensions, and render tests MUST be recorded.

## 4. Build and accessibility contract

The backend MUST:

1. build serially with a pinned engine, font profile, inputs, and deterministic environment;
2. require stable late passes for the PDF and material auxiliary files;
3. reject fatal errors, undefined controls, missing characters, and undeclared layout drift;
4. inventory every embedded font and ToUnicode map;
5. extract with at least two independent engines;
6. reject NUL, U+FFFD, and disallowed internal C0 controls;
7. render every page and inspect all changed pages at original detail;
8. keep source, linguistic, build, extraction, and visual states distinct.

Where classic Type 1 math subsets render correctly but lack ToUnicode, a missing-only post-build CMap injection MAY be used. It MUST use pinned maps, fail on an unknown subset, never overwrite an existing map, be byte-deterministic, and preserve page contents, geometry, font programs, links/destinations, metadata, and rasters. The currently replayed maps are `oms.cmap`, `omx.cmap`, and `umsb.cmap`; their exact identities are in `evidence.jsonl`.

Compilation success, clean extraction, or clean rendering MUST NOT be promoted into a claim of linguistic correctness.

## 5. Locale profiles

### 5.1 Simplified Chinese, PRC-oriented (`zh-Hans-CN`)

The profile MUST use direct PRC-oriented evidence for terminology and prose. It SHOULD use fullwidth Chinese punctuation in prose, avoid spaces before punctuation, keep TeX in control of inline-math spacing, and treat mixed-script forms such as `A-模` as profile data.

Terms MUST carry a mathematical sense window and rejected senses. Examples supported in the audited corpus include `子集` for set-theoretic *partie*, `闭包` for topological closure rather than `整闭包`, `反序映射` rather than analytic `递减映射`, and `由同态 φ 导出的映射` rather than adjoint-language `伴随映射`.

`zh-Hans-CN` MUST NOT authorize Singapore usage. Controlled-generic Hant MUST NOT be called Taiwan-, Hong-Kong-, or Macao-localized.

### 5.2 Japanese

Japanese MUST be independently evidence-bound. The default mathematical prose profile MAY use plain assertive forms such as `…である`, `…とする`, and `…と書く`, but display punctuation MUST remain source-associated rather than globally normalized.

Mixed-script morphology, spacing, and hyphenation are term-specific: forms such as `素イデアル`, `準コンパクト`, `Zariski 位相`, and `pro-エタール` are not defects merely because a Han-only alternative exists. Japanese MUST distinguish look-alike terms by sense, for example `剰余体` versus `商体`; `標準的に` versus `自然に`; and `付随する写像` versus adjoint-language `随伴写像`.

Chinese or Korean forms MAY be comparison candidates but MUST NOT authorize Japanese wording.

### 5.3 South-Korean Korean (`ko-KR`)

Korean MUST declare regional and script policy. The active EGA profile is Hangul-first; Hanja MAY appear at first occurrence or in terminology metadata when it materially disambiguates. `ko-KP` MUST fail closed until direct evidence exists.

Particles MUST attach directly to an inline math span (`$X$가`, `$A$를`), with an explicit allomorph check. Compound spacing MUST be lexical/type-specific rather than globally collapsed. Formula operators remain symbolic even when prose has a Korean name, for example prose `대각합` while formulas retain `Sp`.

Type distinctions control terminology: `유리함수환 R(U)` is a ring while `유리함수층 \mathscr R(X)` is a sheaf; a stalk is `줄기`, not geometric `섬유`; torsion is governed by `\ker(F\to F\otimes_{\mathcal O_X}\mathscr R(X))`, with `꼬임` retained as a medium-confidence lexical choice. Chinese/Japanese cognates MUST NOT authorize these Korean forms.

## 6. Typed term and morphology records

Every term decision SHOULD include:

- concept ID and exact source unit;
- language, variety, script/profile, and register;
- exact form, pronunciation/Hanja metadata where useful, and morphology/spacing;
- intended sense and excluded senses;
- trap class and provisional lexical-attractor basin;
- support, candidate, competitor, adverse, absence, and veto channels kept separate;
- exact provenance and review/decision state;
- qualitative dominant-standard risk/debt;
- target loci and supersession state.

`term.schema.json` makes these fields machine-checkable while keeping support, candidate, competitor, adverse, absence, and veto channels separate.

Shared characters are locators, not semantic proof. A Sino-xenic resemblance can identify a comparison candidate; it cannot promote a term.

## 7. Decentralized adoption

Each translation lane MAY adopt this backend without writing into another lane or synchronizing its workflow. The common schema and validators are read-only inputs. A lane owns its terminology/profile and emits hash-pinned evidence. Canonical aggregation has one writer and consumes frozen returns only.

An adopting lane SHOULD implement five independently identified adapters:

1. source and formula projection;
2. source-note and apparatus projection;
3. locale terminology and prose profile;
4. font and script profile;
5. common build, extraction, and render validator.

Existing cumulative translations MUST be audited and rebased rather than discarded. Fresh translation is justified only after a hash-pinned finding that the inherited unit is unusable.

### 7.1 Concrete adoption sequence

For each bounded unit, a lane SHOULD perform these actions in order:

1. bind the exact authority and inherited target by stable ID, bytes, SHA-256, and unit boundary;
2. derive source formula, note, label, reference, and asset obligations;
3. enumerate authority deltas and confirmed target corrections before changing target bytes;
4. run the formula adapter and register every permitted exception by stable ID;
5. run the locale adapter only over prose-bearing nodes, including nested `\text`, `\mbox`, and `\hbox` spans;
6. apply the language-local terminology, morphology, punctuation, and font profile;
7. build serially, run two independent extractions, inventory fonts/ToUnicode, and render every page;
8. emit a report conforming to `report.schema.json`, with exact evidence for each independent state;
9. freeze the unit and make later corrections append-only supersessions.

The report states `source_binding`, `formula_projection`, `note_apparatus`, `locale_profile`, `build`, `extraction`, and `render` independently. These fields MUST NOT be collapsed into a scalar readiness value. A failed or unsupported field remains visible while unrelated passing evidence is preserved.

### 7.2 Sanitization matrix

The shared sanitizer MUST canonicalize UTF-8 encoding, NFC text, LF line endings, and exact manifest paths; it MUST validate and preserve declared TeX control sequences. It MUST parse math delimiters with escape awareness and recursively expose declared prose-bearing TeX arguments to the locale adapter.

The shared sanitizer MUST NOT perform NFKC, blind Simplified/Traditional conversion, global punctuation replacement, global whitespace collapse, cross-language term substitution, or undifferentiated regex replacement inside TeX. Those operations either belong to an independently evidenced locale adapter or are rejected entirely.

The locale adapter MAY normalize punctuation, spacing, script, and morphology only inside its declared profile and only while protected formula/control streams remain invariant. Every nontrivial replacement SHOULD have an exact precondition count and fail closed when that count changes.

### 7.3 Conformance fixtures

`tests.json` supplies reusable positive and negative fixtures for escaped delimiters, nested prose, Greek-token identity, declared repeats, missing ToUnicode, Chinese regional non-transfer, Japanese mixed-script morphology, Korean type resolution, and Unicode normalization. An implementation SHOULD run every applicable fixture and record its own adapter-specific fixtures beside them.

## 8. Limits

This release does not establish a universal CJK lexicon, mutual intelligibility, Japanese/Korean authorization by Chinese evidence, PRC authorization for other Chinese regions, North-Korean usage, or a Vietnamese/CJKV standard. It standardizes the evidence and mechanics required to investigate those questions safely.
