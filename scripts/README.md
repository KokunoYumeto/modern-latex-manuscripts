# Scripts

This repository intentionally does not vendor the full local Codex toolchain. Public scripts should be small, reproducible, and usable without private credentials.

Current scripts:

- `build_public_catalog.py`: rebuilds `manifests/public-file-catalog.csv` and `docs/public-file-catalog.md` from the public Zenodo records API. It does not need a token.
- `build_record_pages.py`: rebuilds `docs/records/` from `manifests/public-file-catalog.csv`, grouping each Zenodo record into reader PDFs, artifact ZIPs, and status files.
- `check_markdown_links.py`: checks local Markdown links in the repository and ignores external URLs.

Useful future scripts:

- public metadata/name audit;
- PDF structural audit;
- TeX compile smoke test;
- source-scan provenance checker.
