# Interlanguage CJK Mathematical Notation Backend

Component version 1.0.0, published as an additive component of the existing Interlanguage methodology sidecar.

- Containing concept DOI: [10.5281/zenodo.21124403](https://doi.org/10.5281/zenodo.21124403)
- Containing version DOI: [10.5281/zenodo.21940307](https://doi.org/10.5281/zenodo.21940307)
- Repository: [KokunoYumeto/modern-latex-manuscripts](https://github.com/KokunoYumeto/modern-latex-manuscripts)

These are the DOI identities of the containing Interlanguage record, not a separate or exclusive CJK-backend DOI. The component has no competing Zenodo concept.

This sidecar defines the smallest evidence-supported mathematical notation and document-production backend shared by current Chinese, Japanese, and Korean work in the Interlanguage corpus. It does **not** define a merged CJK language, a shared lexicon, or a script-conversion shortcut.

The result has four layers:

1. a language-neutral formula, source-note, asset, and provenance contract;
2. independent locale profiles for `zh-Hans-CN`, Japanese, and South-Korean Korean;
3. a common deterministic build, extraction, and render-validator contract;
4. typed comparison records that never let one language authorize another.

Current negative scope is explicit: `zh-Hans-SG`, localized `zh-Hant-TW`, `zh-Hant-HK`, `zh-Hant-MO`, and `ko-KP` lack sufficient audited production evidence here. Controlled-generic Hant is a script projection, not regional prose.

Read [STANDARD.md](STANDARD.md) for the normative rules, [METHOD.md](METHOD.md) for the evidence method, [evidence.jsonl](evidence.jsonl) for hash-pinned findings, and [adverse.tsv](adverse.tsv) for failure cases. Evidence records validate against [schema.json](schema.json). An adopting lane can emit independently evidenced conformance states with [report.schema.json](report.schema.json), record locale-bound terminology with [term.schema.json](term.schema.json) and its [worked term example](term.example.json), and run the 21 positive/adverse fixtures in [tests.json](tests.json) through [fixture_runner.py](fixture_runner.py). The fixture contract itself validates against [tests.schema.json](tests.schema.json).

The concrete adoption unit is five hash-addressed adapters: source/formula projection, note/apparatus projection, locale terminology/prose, font/script, and build/extraction/render validation. Each report binds exact authority and target loci, formula and note obligations, changed-locus hashes, adapter identities, and separate evidence for every state; it never collapses them into a readiness score.

The release-integrity verifier is included. Replaying claims backed by `hash_only` project artifacts requires independently obtaining the exact cited corpus/checker bytes; those third-party or lane-owned artifacts are deliberately not redistributed here.

Human or community review may add evidence or justify a stronger social claim, but it is optional and never a publication gate. This release claims machine-checked research synthesis, not external certification.

Produced at Floris's direction by OpenAI Codex, GPT-5.6 Sol in Ultra mode.

All bundled component content is CC0-1.0. The Citation File Format schema used during development is hash-cited but not redistributed. See [LICENSE](LICENSE), [RIGHTS.md](RIGHTS.md), [rights.json](rights.json), and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
