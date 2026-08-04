$ErrorActionPreference = 'Stop'

$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$manifest = Join-Path $root 'SHA256SUMS.txt'
$lines = Get-Content -LiteralPath $manifest
$seen = @{}
$failures = [System.Collections.Generic.List[object]]::new()
$parsed = 0

foreach ($line in $lines) {
    if ($line -notmatch '^([0-9A-F]{64})  (.+)$') {
        $failures.Add([pscustomobject]@{ type = 'parse'; line = $line })
        continue
    }
    $parsed += 1
    $expected = $Matches[1]
    $relative = $Matches[2]
    if ($seen.ContainsKey($relative)) {
        $failures.Add([pscustomobject]@{ type = 'duplicate'; path = $relative })
        continue
    }
    $seen[$relative] = $true
    if ([System.IO.Path]::IsPathRooted($relative) -or $relative.Split('/') -contains '..') {
        $failures.Add([pscustomobject]@{ type = 'unsafe'; path = $relative })
        continue
    }
    $full = Join-Path $root ($relative.Replace('/', '\'))
    if (-not (Test-Path -LiteralPath $full -PathType Leaf)) {
        $failures.Add([pscustomobject]@{ type = 'missing'; path = $relative })
        continue
    }
    $actual = (Get-FileHash -LiteralPath $full -Algorithm SHA256).Hash
    if ($actual -ne $expected) {
        $failures.Add([pscustomobject]@{ type = 'hash'; path = $relative; expected = $expected; actual = $actual })
    }
}

$nonSelfFiles = (Get-ChildItem -LiteralPath $root -Recurse -File -Force |
    Where-Object { $_.FullName -ne $manifest }).Count

[pscustomobject]@{
    manifest = $manifest
    manifest_bytes = (Get-Item -LiteralPath $manifest).Length
    manifest_sha256 = (Get-FileHash -LiteralPath $manifest -Algorithm SHA256).Hash
    declared_entries = $lines.Count
    parsed_entries = $parsed
    unique_paths = $seen.Count
    non_self_files = $nonSelfFiles
    failure_count = $failures.Count
    failures = $failures
    all_pass = ($failures.Count -eq 0 -and $parsed -eq $lines.Count -and $seen.Count -eq $nonSelfFiles)
} | ConvertTo-Json -Depth 6
