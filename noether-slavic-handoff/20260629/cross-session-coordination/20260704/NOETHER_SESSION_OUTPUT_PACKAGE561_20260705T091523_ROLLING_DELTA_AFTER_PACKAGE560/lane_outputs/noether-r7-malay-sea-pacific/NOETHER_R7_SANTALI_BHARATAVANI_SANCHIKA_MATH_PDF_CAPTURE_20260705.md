# Noether R7 Santali Bharatavani/Sanchika Math PDF Capture - 2026-07-05

Scope: source-canon/provenance only. This packet upgrades the Santali source-return shelf from listing/item metadata to an exact repository PDF witness for `BVP06068`, *A New Mathamatics in Olchiki*. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_SANTALI_BHARATAVANI_SANCHIKA_MATH_PDF_CAPTURE_ROWS_20260705.csv`
- Row count: 8
- Payload policy: no raw PDF/HTML/image/text/source bodies are stored in `outputs`; bitstreams were downloaded to temporary files, hashed, byte-counted, and deleted immediately.

## Findings

- Bharatavani listing and item pages are hashable and identify the Santali/Ol Chiki mathematics textbook `A New Mathamatics in Olchiki`.
- Bharatavani exposes a cover-image sidecar and a login route for book access.
- Bhasha Sanchika exposes a full item record for `BVP06068`, including a PDF bitstream and a license sidecar.
- The Sanchika PDF bitstream returned HTTP 200 as `BVP06068.pdf`, 288588 bytes, SHA-256 `735755BB0C932E5D8FBC376F23A3C10DD8314AF1307DF91EC0785E16C53A8020`.
- The Sanchika license sidecar returned HTTP 200 as `license.txt`, 14 bytes, SHA-256 `50EBB13755F5F4EA38090107E97DB0B6200B26094D477EE3EEB3CC837F585F1D`.
- The license sidecar is recorded as a rights signal only; no license clearance is claimed.

## Disposition

This is the strongest Santali mathematics source witness currently captured in this lane: exact PDF provenance with repository metadata and sidecar rights signal. It remains PDF fallback, not TeX/LaTeX/e-print/source archive material, and it does not support translation approval or accepted terminology claims.

Next source actions:

- Keep `BVP06068.pdf` as the primary Santali math source witness for this lane.
- Search separately for source-level TeX/e-print or higher-level algebra/STEM Santali materials.
- Preserve the license sidecar and no-clearance boundary whenever this witness is packaged.
