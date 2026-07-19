# Privacy and source-exclusion audit

The public self-validator checks only generic absolute-path and UUID patterns
in textual payloads. Binary-file scanning and configured private-name and
internal-routing comparisons were performed by a separate external audit.
Their comparison strings are intentionally not embedded, encoded, split, or
otherwise reconstructable from this public set.

The external scan inspected every proposed public file as raw bytes, UTF-8,
Latin-1, UTF-16LE, and UTF-16BE; normalized slash direction; removed whitespace
and line wrapping; and checked recomposed token streams. It reported zero
private-name, internal-routing, UUID, or absolute-path findings.

The exact-set audit also confirmed:

- no German authority body or bounded German slice;
- no original scan or source-derived scan image;
- no inherited-English body or bounded comparison slice;
- no external correction-alert body or internal-routing filename;
- no raw build log, build transient, or private validator;
- no archive, traversal path, symbolic link, executable payload other than the
  public self-validator, or disguised archive;
- exactly one English TeX, one English PDF, four target-page renders, and one
  target contact sheet.

The retained source, scan, comparison, and alert entries are typed hash-and-
scope receipts only. Their excluded bodies are not recoverable from the
package.
