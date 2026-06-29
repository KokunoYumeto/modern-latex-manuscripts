# Source-Audited Edition Pipeline Addendum

Date: 2026-06-29

This addendum records an outside ChatGPT Pro review of the project strategy and folds the useful parts into the working method. The central point is accepted: the strongest public framing is not "AI transcribed pages", but a source-audited, citable, reusable edition/OCR pipeline.

The current archive already does some of this: source witnesses, SHA256 manifests, page/range ledgers, patch CSVs, rendered checks, GitHub mirrors, Zenodo records, caveats against critical-edition overclaiming, and no-screenshot/no-summary rules. The following items are adopted as additional workflow obligations.

## Adopted Direction

Noether should be treated as the flagship case for a general historical-mathematics pipeline:

- stabilize the original-language corpus before treating translations as final products;
- publish status by paper, page/range, and source witness;
- separate reader TeX from apparatus/provenance data;
- use OCR/model outputs as witnesses and disagreement detectors, not as authority;
- invite narrow external review tasks rather than asking for whole-corpus review;
- make small, citable, reviewable release packets instead of relying on giant opaque ZIPs as the public interface.

This does not mean older large preservation packets are bad. They remain useful raw/provenance archives. It means the reader-facing and reviewer-facing surface should be smaller, clearer, and status-driven.

## Workflow Tracking Is A Core Deliverable

The project already uses many of the recommended practices: source witnesses, hashes, patch ledgers, status notes, render checks, public caveats, and GitHub/Zenodo separation. The improvement is not to rediscover those practices, but to make them more systematic and easier for outsiders to follow.

Treat workflow tracking itself as a first-class output. For each serious lane, keep enough current public/private status that a later Codex, web session, reviewer, or human reader can answer:

- what is the current base file or branch;
- what was checked against which source witness;
- what was changed, and what was deliberately not changed;
- what is reader-facing versus support/control material;
- what confidence level applies to each paper, page range, language branch, formula queue, or source package;
- what should be done next without replaying stale or superseded work.

This is not bureaucracy for its own sake. It is the mechanism that prevents old optimistic filenames, compacted chat memory, duplicate web outputs, and stale support packets from misleading future work.

## Archive-Maintenance Responsibility Register

These are not just good ideas for other sessions. They are standing responsibilities of the Codex archive-maintenance lane.

### Already In Active Practice

- Preserve useful local/web/Claude/Codex work before it is lost.
- Sweep local drop folders, unpack or index new ZIPs, and identify high-signal author/work updates.
- Separate reader-facing files from raw provenance, support packets, OCR witnesses, and failed attempts where practical.
- Maintain GitHub as the forkable working mirror and Zenodo as the citable archival surface.
- Add caveats when files are working drafts, OCR/source-locator aids, no-patch audits, or support packets rather than editions.
- Keep SHA256 manifests, package inventories, public summaries, and pending-Zenodo manifests for serious updates.
- Avoid claims of critical-edition or proofread status unless explicitly certified by the maintainer.

### Not Yet Good Enough, Therefore Owned By Archive Maintenance

- Build compact current-state dashboards for major lanes, especially Noether, SGA, Weber, Cayley, Deligne, and non-European mathematics. These should say what the current base is, what is source-checked, what is only represented, and what is explicitly weak.
- Add status-tier fields where useful: Bronze/Silver/Gold/Platinum or equivalent conservative labels tied to named source witnesses.
- Maintain a disagreement/open-risk queue rather than only long narrative logs. High-risk loci include formulas, diagrams, tables, title blocks, footnotes, source conflicts, low-DPI witnesses, and known bad OCR/LLM failure patterns.
- Track no-patch outcomes as real outcomes. If a package inspects a source conflict and decides not to change the TeX, that needs to remain visible.
- Make reader/apparatus/witness separation more consistent in author packages and public descriptions.
- Turn source-image metadata into more regular CSV/JSON: source ID, institution, URL/IIIF if known, local file, page/canvas, resolution, crop coordinates, and hash.
- Create or maintain editorial-policy stubs for flagship lanes before they are described as near-final.
- Keep author pages ordered by real reader usefulness and confidence, not by upload date, local excitement, or old filenames.
- Prepare smaller, reviewable release/review packets instead of allowing large opaque ZIPs to be the only practical public interface.
- Record workflow lessons from local tools, OCR witnesses, Pro handoffs, and failed agents in public workflow notes when they are generalizable.

### Immediate Maintenance Behavior

When sweeping or staging updates, Codex should explicitly ask of each new artifact:

```text
Is this reader-facing, apparatus/control, witness/provenance, OCR locator, failed attempt, or private support?
What current base does it modify or inspect?
Does it apply a TeX/content patch, or is it no-patch evidence?
What source witness and source quality does it rely on?
Does public metadata need to change because this alters completeness/confidence?
Is it superseded by a newer package or dangerous because of an optimistic filename?
```

If those answers are not discoverable, the package should be staged as uncertain/support material rather than promoted.

## Certification Dashboard

Each serious author/work lane should grow a simple machine-readable status table, especially Noether. Minimum columns:

```csv
work_id,paper_or_section,language,reader_pdf,tex_source,source_witness,page_map,formula_audit,table_diagram_audit,external_review,status_tier,status_note
```

The `status_tier` values should be conservative:

- `bronze`: compiles or opens, readable enough to inspect, source route identified;
- `silver`: page/range checked against a named source witness;
- `gold`: formulas, footnotes, tables/diagrams, citations, and page boundaries checked for the declared range;
- `platinum`: externally reviewed and explicitly certified by the maintainer as proofread/edition-grade.

Most current files are below `gold`; many are merely useful working drafts or source-support packets. The public descriptions should keep saying this plainly.

## Disagreement Queue

Auditing should focus on likely-error loci rather than uniformly rereading everything forever. The pipeline should create or maintain queues for:

- formulas with many indices, stacked symbols, primes, Greek/Latin ambiguity, Fraktur, or old-style glyphs;
- tables, arrays, plates, foldouts, diagrams, and coefficient lists;
- footnotes, bibliography entries, title/author blocks, and article boundary material;
- locations where OCR/model witnesses disagree with current TeX;
- places where render output visibly diverges from page images;
- low-resolution witnesses and known prior correction sites.

Preferred queue row:

```csv
work_id,unit_id,source_page,current_tex,witness_a,witness_b,issue_type,confidence,next_action
```

The result may be "no patch promoted" if the source conflict cannot be decided. That is a valid scholarly outcome.

## Reader, Apparatus, Witness

Keep three layers distinct:

- reader layer: clean TeX/PDF for original language and translations;
- apparatus layer: CSV/JSON records of variants, corrections, source decisions, confidence, and unresolved issues;
- witness layer: source PDFs/images, IIIF-style references where available, crop references, page maps, OCR/model witnesses, hashes, and source-resolution notes.

Do not overload reader TeX with every uncertainty. Do not hide uncertainty either. Put it in the apparatus.

## Editorial Policy Work

Before any lane is described as near-final, it needs an editorial policy. At minimum:

- spelling modernization versus source spelling;
- treatment of obvious printer errors;
- collected edition versus original article authority;
- visual versus semantic formula transcription;
- policy for ambiguous glyphs such as `x`, `\chi`, `\kappa`, and `\varkappa`;
- Fraktur and historical-symbol macro policy;
- treatment of title pages, editor notes, acceptance lines, and corrections/errata;
- translator interventions and terminology decisions;
- definition of `source-certain`, `best-available`, and low-resolution fallback.

This policy should be short and practical. It should not delay preservation work, but it should govern claims of source-checked or edition-grade status.

## OCR/Model Witness Ensemble

The project should not use a single LLM or OCR engine as source authority. Better pattern:

1. current TeX candidate;
2. source page image/PDF;
3. OCR text witness;
4. formula/table/image witness where useful;
5. automatic or semi-automatic disagreement queue;
6. human/model adjudication only on disputed loci;
7. promoted patches only when source evidence is clear.

Specialist OCR and math-OCR tools are useful here as independent witnesses. Their outputs should be labelled `OCR_candidate`, `formula_witness`, `layout_witness`, or `locator_aid` unless source comparison promotes them.

## IIIF-Style Source Metadata

For each serious source witness, preserve enough metadata that another worker can reconstruct the checking context:

```csv
work_id,paper_or_section,source_id,institution,url,iiif_manifest,canvas_or_leaf,printed_page,volume_page,local_file,sha256,resolution_ppi,crop_id,crop_box,notes
```

Full IIIF conversion is not required immediately, but canvas/page/crop thinking should inform file names and manifests. Giant folders of images are less useful without stable page identities.

## Benchmark Dataset Track

Create a small benchmark only after a subset is genuinely source-checked. Do not dump the whole archive as a benchmark.

First benchmark candidate:

- 50-100 representative Noether page images or stable page references;
- ground-truth German TeX/transcription;
- formula crops with ground-truth LaTeX;
- source metadata and page maps;
- hard-glyph and historical-notation notes;
- baseline OCR/model outputs;
- evaluation script.

This would serve OCR/ML workers and also make the project more legible as a reusable research pipeline.

## Public Review Strategy

Ask for narrow review tasks:

- check one formula group;
- verify one title/author block;
- compare one page range against a source witness;
- review one terminology cluster;
- verify one table or diagram.

Record reviewers and decisions in contributor/review ledgers. Do not ask outsiders to review an entire corpus at once.

## Immediate Practical Changes

- Add status-tier columns where new dashboards or status CSVs are created.
- Prefer compact source-audit rollups over many loose micro-ZIPs, especially for Noether at the Zenodo file ceiling.
- Treat Noether German/source audit as the base branch; translations inherit from it and should not be represented as more reliable than the source branch they follow.
- Add apparatus/witness CSVs when packaging serious updates, even if minimal.
- Track "no patch promoted" as a first-class outcome.
- Keep public wording conservative: working scholarly archive, source-audit draft, witness packet, support/control packet, not critical edition unless explicitly certified.
