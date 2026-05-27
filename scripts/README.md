# Scripts

This repository intentionally does not vendor the full local Codex toolchain. Public scripts should be small, reproducible, and usable without private credentials.

Current scripts:

- `build_public_catalog.py`: rebuilds `manifests/public-file-catalog.csv` and `docs/public-file-catalog.md` from the public Zenodo records API. It does not need a token.

Useful future scripts:

- public metadata/name audit;
- PDF structural audit;
- TeX compile smoke test;
- source-scan provenance checker.
