# Reproduce the exact admitted D019 transport PDFs

The portable entrypoint is `reassemble_verified_transport.py`. With Python 3 and `pypdf==6.12.2`, run it from any working directory with `--output-dir` pointing to a new directory. It writes both transport PDFs and a hash-verified replay receipt without modifying any supplied file.

The script obtains the exact canonical PDFs from `../canonical_build/output/pdf/`, the unchanged canonical final gate from `../receipts/`, the terminal acceptance receipt from `../transport_evidence/TRANSPORT_RESULT.json`, and all 144 verified image streams from `method03_zopfli/encoded_streams/`. Their hashes, dimensions, and native decoded pixels are checked before assembly. Each final PDF must match the accepted filename, byte count and SHA-256 exactly.

The original `produce_zopfli.py`, `resume_assembly.py`, `verify_zopfli.py`, and related scripts are preserved as historical method evidence. They refer to original operational cursors and method01 files; they are not the portable entrypoints for this extracted tree. The portable entrypoint above replaces only that operational setup, using the already validated completed cache; it does not rerun compression or change PDF contents. Canonical PDF/TeX/assets and the complete canonical source packet remain unchanged.

If the source tree was restored from a GitHub mirror with oversized files stored as release assets, first restore the exact canonical PDFs using the mirror's hash-verified restoration instructions. The complete `Deligne_Source.zip` already contains all required files. Archives are split only when a complete asset reaches the 2 GiB transport threshold; any such parts are explicitly listed with concatenation order and whole-archive hash.
