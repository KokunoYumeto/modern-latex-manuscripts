# R9 P0 Timeout Retry: Tigrigna/Tigrinya Teacher Guide

Generated: 2026-07-05T13:38:00.740092+00:00 UTC

## Boundary

This artifact performs a targeted retry for the single non-2xx/error row from the full P0 source URL access-signal sweep: `R9-OCR-SO-0188`, the Tigrigna/Tigrinya Grade 8 math teacher guide. It records retry attempts, response headers, and a range-probe byte count only if needed. It does not save a source body, source text, translation, approved term, review claim, license clearance, gate promotion, package action, staging, commit, or push.

## Retry Summary

- Previous full-sweep result: `URLError(TimeoutError('timed out'))`
- Retry decision: `not_admitted_retry_access_signal_only`
- Chosen method: `HEAD`
- Chosen TLS mode: `unverified_after_tls_or_server_failure`
- HTTP status: `200`
- Content type: `application/pdf`
- Content length: `12415631`
- Content range: ``
- Range probe bytes read, not saved: `0`
- Local source path still present: `true`
- Local source SHA-256: `38842FD2E826B40F0D4695398ADA0031BB898C30C73C64A621D9E90C3DFF598A`

## Attempts

| method | TLS mode | result | status/error | bytes read |
|---|---|---|---|---:|
| HEAD | verified | error | URLError(SSLCertVerificationError(1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: Hostname mismatch, certificate is not valid for 'files.ethiopialearning.com'. (_ssl.c:1010)")) | 0 |
| HEAD | unverified_after_tls_or_server_failure | ok | 200 | 0 |

## Source-Gate Reading

The local teacher-guide body remains provenance only. A retry access signal does not clear source-owner, attribution, license/reuse, reviewer, OCR/register, or translation gates.

CSV: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\outputs\R9_P0_TIMEOUT_RETRY_TIGRIGNA_TEACHER_GUIDE_20260705.csv`
