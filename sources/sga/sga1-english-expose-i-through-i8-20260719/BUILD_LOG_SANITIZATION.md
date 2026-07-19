# Build-log sanitization

Each of the three private full compiler logs is represented by a public full
log in `evidence/build`. Any line containing an absolute local compiler path,
and each wrapped continuation of that path, is replaced by a fixed redaction
marker. All other compiler-log lines remain in order. Every public log records
the private raw-log bytes and SHA-256, redaction count, diagnostic count, and
final PDF identity. Concise receipts repeat the dependencies and hashes.

Pass 1 is a clean-directory bootstrap pass with 62 disclosed cross-reference
or rerun diagnostic hits and no fatal error. Passes 2 and 3 have zero actual
diagnostic hits. Public privacy scanning found no local absolute path, user
name, task/thread control, secret-like assignment, or source scan.