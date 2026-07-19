# Privacy and payload hygiene

The production public-text surface is scanned in both ordinary and
whitespace-compacted form for drive-qualified user paths, private repository
root tokens, profile-data tokens, personal-name tokens, and unfinished-work
markers.
The current machine validation records zero hits.

Raw TeX build logs, generated auxiliary files, and the build/validation scripts
remain under `internal_private`. They are intentionally excluded from the
unit's proposed public manifest. Sanitized build transcripts at the unit root
are whitelist-constructed and contain no private dependency paths.

This hygiene check does not authorize publication or archive transport.
