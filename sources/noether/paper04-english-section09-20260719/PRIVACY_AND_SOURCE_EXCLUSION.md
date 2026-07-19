# Privacy and source-exclusion controls

The public self-validator checks generic absolute-path and UUID patterns in
textual payloads. A separate package audit must also scan every file as raw
bytes and decoded UTF-8, Latin-1, UTF-16LE, and UTF-16BE; normalize slash
direction; remove whitespace and line wrapping; inspect PDF internals; and
compare configured private-name and internal-routing strings without
embedding those comparison strings in this public set.

The intended exact set excludes:

- German authority bodies and the bounded German slice;
- the original scan and all scan-derived source images;
- inherited-English bodies and bounded comparison slices;
- external correction bodies and internal-routing filenames;
- raw build logs, auxiliaries, temporary files, and private validators;
- private absolute paths, task/thread/decision identifiers, workflow-owner
  names, secrets, reconstructable split literals, archives, symlinks,
  traversal paths, and disguised executables.

Typed receipts retain only public-safe hashes, byte counts, scopes, and
dispositions for excluded evidence. Exactly one English TeX, one English PDF,
two target-page renders, and one target contact sheet belong in the package.
