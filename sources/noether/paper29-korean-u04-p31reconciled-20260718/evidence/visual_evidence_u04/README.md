# U04 visual-evidence archive

This directory is the machine-readable visual authority for the Korean Noether Paper 29 U04 checkpoint (full-Paper-29 lines 47--51).

- `VISUAL_EVIDENCE_INDEX.jsonl` is the private canonical index. It may contain the exact local path of a rights-blocked source page.
- `VISUAL_EVIDENCE_PUBLIC_SAFE.jsonl` is the publication-safe projection. Rights-blocked paths are null, but asset names, hashes, bytes, geometry, printed-page locators, bounding boxes, linked structures, QA state, and rights disposition remain.
- `VISUAL_EVIDENCE_INDEX.csv` is the flat inspection projection.
- `RIGHTS_BLOCKED_SOURCE_ROOT_MANIFEST.csv` inventories all eight source JPEGs in the private continuity root without exposing its filesystem path.
- `OPEN_PAYLOAD_VISUAL_MANIFEST.csv` binds the three project-generated renders included in the public ZIP.
- `VISUAL_EVIDENCE_METADATA.json` records private continuity totals; `VISUAL_EVIDENCE_METADATA_PUBLIC_SAFE.json` removes the private root path.
- `build_visual_evidence.py` deterministically rebuilds the projections and ZIP after checking pinned source, TeX, PDF, and PNG hashes.
- `validate_visual_evidence.py` validates schemas, relations, geometry, hashes, rights separation, checksums, ZIP totals, and leak exclusions.

The source pages are evidence, not publication-authorized images. The German control, preserved Korean draft, and accepted Korean final render are project-generated open-payload assets. All review labels are internal model/session QA; no human or external certification is claimed.
