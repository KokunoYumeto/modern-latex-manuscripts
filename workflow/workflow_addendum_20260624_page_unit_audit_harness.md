# Workflow Addendum 2026-06-24: Page-Unit Audit Harness Pattern

This addendum records a repeatable source-faithfulness workflow that emerged across the Noether, Weber, SGA6, and Steinitz lanes. It is meant for future local Codex / web Pro / other-agent collaboration and should be treated as workflow/methodology material, not as an author-specific reader edition.

## 1. The Pattern

A reliable audit harness has four layers:

1. **Canonical TeX candidate**: the current manuscript branch being checked, with path and lineage stated explicitly.
2. **Source witness inventory**: the best on-disk source scan(s), page maps, image DPI/size, and source identity.
3. **Audit manifest**: one JSON unit per source page or source object, linking source page, printed page, TeX file, approximate or exact TeX line anchor, and caveats.
4. **Chunk renderer**: a small script that renders only requested pages into overlapping high-resolution chunks for visual source comparison.

The harness is not the edition. It is the machine-readable checklist and routing layer used to find, verify, and fix the edition.

## 2. Exact Versus Approximate TeX Addressability

Public workflow notes must distinguish exact anchors from hints.

- Exact anchor: page-level TeX markers such as `\sourcepage{N}` or stable object IDs make a page directly auditable.
- Approximate anchor: `tex_line_hint` derived by linear interpolation or exposition/section span is only a starting point. The auditor must search nearby by source text.
- Missing anchor: if a cumulative file has no page/section anchors, the first improvement should be adding stable nonsemantic anchors before claiming page-level coverage.

Steinitz 1910 is a good exact-anchor example because the checked files contain `\sourcepage{N}`. Weber and Noether currently have many approximate anchors; they are audit-ready but not automatically page-certified.

## 3. Source Scans And DPI Floors

Record source quality in the manifest rather than hiding it in prose.

- 400ppi can support gross-gap/prose-anchor checking and many ordinary comparisons, but it is below the current strict dense-math floor.
- 600ppi is strong best-available evidence in many GDZ/IA lanes, but still below the local 650ppi strict threshold used for source-certification language.
- Dense formulas, diagrams, small subscripts, old typography, and footnotes may require 1000ppi or targeted native crops.
- If no better source exists, say **best available 600ppi source repair**, not **certified**.

The same page can be useful as a witness while still being too weak for symbol-by-symbol certification.

## 4. OCR And Kimi/Raw Drops

OCR and raw AI drops are locator layers unless visually checked.

Use OCR/raw drops to:

- find missing prose and suspicious compression;
- locate likely formula/table/diagram regions;
- narrow a TeX search window;
- build anti-omission ledgers.

Do not use OCR/raw drops to:

- override source-page images;
- declare exact symbols correct;
- certify diagrams or tables;
- become the basis when a better cumulative source-faithful TeX exists.

The SGA6 harness is explicit: Kimi pages are locator-only; the cumulative French `sga6_fr.tex` and original scan are the audit basis.

## 5. Render On Demand, Not Mass Render

High-resolution chunks are expensive in time, storage, and web-session context. The scalable pattern is to render only the source pages currently under audit.

Recommended chunk output:

- overlapping top/middle/bottom bands, usually capped around 2400px wide;
- optional full-page render and footer strip for page-number verification;
- stable filenames containing work, volume/expose/paper, printed page, and chunk position;
- one or two surrounding text lines around formula/table crops when possible.

Avoid dumping thousands of page images into every handoff unless the web session specifically needs them.

## 6. Page Maps And Offset Drift

Every source scan needs a page map. Constant offsets are useful but must be verified.

- Weber has stable printed-to-PDF offsets by volume.
- SGA6 has a drift in the back third, so the rendered footer must be checked before a finding is mapped to a TeX line.
- Steinitz 1910 is simpler because page images are named by printed page and GDZ scan index.

When an offset is uncertain, mark it as uncertain in the manifest and require visual footer confirmation.

## 7. Public Representation Rule

An audit harness can make work tractable without making the edition finished. Public records should say exactly which level is true:

- **audit-ready**: source/TeX/page maps exist and agents can check it;
- **source-witnessed**: source scans/crops/ledgers support a bounded range;
- **source-repaired**: specific loci were patched against named witnesses;
- **source-certified**: reserved for bounded ranges with adequate source quality and completed verification;
- **critical edition**: reserved for explicit human certification.

Do not call a work complete merely because it has a cumulative PDF, a compile log, or a full-page manifest.

## 8. Harnesses Observed In This Sweep

Local harnesses read during this sweep:

- Noether: `Noether Multilingual\_noether_audit\HARNESS_README.md`; 23 ready papers, 323 page units, source inventory with 400/600ppi tiers, PDF-only exclusions, and proportional line hints.
- Weber: `Weber semi-restard and fidelity pass\_audit\HARNESS_README.md`; 1720 audit-ready printed-page units across all three volumes, IA `weberich` scans around 500ppi, but line hints are interpolated because the cumulative TeX lacks per-page anchors.
- SGA6: `Kimi\_sga6_audit\HARNESS_README.md`; cumulative French TeX is the basis, Kimi drops are locator-only, and source PDF offset drifts late in the volume.
- Steinitz: `Steinitz\_audit\HARNESS_README.md`; only the 1910 `Algebraische Theorie der Koerper` work is true page-unit audit-ready because it has per-page TeX anchors and 600dpi page images.

## 9. Practical Next Improvement

When possible, retrofit current cumulative TeX files with stable invisible or comment-level page/object anchors. That makes future language propagation, OCR comparison, formula inventories, and web-session source audits cheaper and less error-prone.