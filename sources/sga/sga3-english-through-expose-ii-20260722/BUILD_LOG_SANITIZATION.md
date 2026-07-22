# Build-log sanitization

The frozen producer log was 60,319 bytes with SHA-256
`F08D1DC1A02019B6ECDC756F335351EDFA0BE047BF951CEDD1FA10C13E8DDEFB`.
It contained 117 occurrences of the private home prefix in TeX installation,
font-cache, source, and output paths.

For the public projection, the private Windows home prefixes (backslash and
forward-slash forms) were replaced with `<USER_HOME>`. No diagnostics or other
log text were changed. The sanitized log is 59,851 bytes with SHA-256
`CCCC70E6433E6923454A5C712A904FCA45D676BD55F76494C1E677E08C3C3696`.
The original log identity remains bound by `ORIGINAL_HANDOFF_SHA256SUMS.csv`
but the path-bearing bytes are not redistributed.
