# Build-log publication policy

The public package contains concise deterministic receipts for all three successful
build passes. Raw compiler logs are retained privately because TeX distributions
embed host-specific executable and package paths, sometimes across wrapped lines.
Each public receipt records the private raw-log SHA-256, byte count, exit status,
dependency set, and selected diagnostic count without redistributing host paths.
