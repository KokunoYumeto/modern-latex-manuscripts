[CmdletBinding()]
param(
    [string]$OutputPath = 'manifests/github-custody/20260806_links.json',
    [string]$ObservedDate = (Get-Date -Format 'yyyy-MM-dd')
)

$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false)
$repoRoot = [IO.Path]::GetFullPath((Get-Location).Path)

$documents = [string[]]@(
    '.github/ISSUE_TEMPLATE/correction.yml',
    '.github/ISSUE_TEMPLATE/rendering_problem.md',
    '.github/ISSUE_TEMPLATE/source-suggestion.yml',
    '.github/ISSUE_TEMPLATE/source_or_translation_correction.md',
    '.github/pull_request_template.md',
    'CONTRIBUTING.md',
    'docs/cayley-map.md',
    'docs/classical-map.md',
    'docs/cluster-map.md',
    'docs/dedekind-map.md',
    'docs/deligne-map.md',
    'docs/dirichlet-map.md',
    'docs/ega-map.md',
    'docs/fga-map.md',
    'docs/gauss-map.md',
    'docs/github-archive.md',
    'docs/github-maps.md',
    'docs/illusie-map.md',
    'docs/noether-map.md',
    'docs/non-european-map.md',
    'docs/riemann-map.md',
    'docs/steinitz-map.md',
    'docs/sylvester-map.md',
    'docs/tohoku-map.md',
    'docs/ukrainian-map.md',
    'docs/verdier-map.md',
    'docs/weber-map.md',
    'manifests/github-custody/README.md',
    'manifests/published-github/README.md',
    'reader-pdfs/README.md',
    'sources/README.md'
)
[Array]::Sort($documents, [StringComparer]::Ordinal)

function Get-Sha256 {
    param([byte[]]$Bytes)
    $sha = [Security.Cryptography.SHA256]::Create()
    try { return [Convert]::ToHexString($sha.ComputeHash($Bytes)) }
    finally { $sha.Dispose() }
}

function Get-GitBlobBytes {
    param([string]$Path)
    $oid = (& git rev-parse "HEAD:$Path").Trim()
    if ($LASTEXITCODE -ne 0) { throw "Cannot resolve committed document: $Path" }

    $startInfo = [Diagnostics.ProcessStartInfo]::new()
    $startInfo.FileName = 'git'
    $startInfo.UseShellExecute = $false
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $startInfo.CreateNoWindow = $true
    [void]$startInfo.ArgumentList.Add('cat-file')
    [void]$startInfo.ArgumentList.Add('blob')
    [void]$startInfo.ArgumentList.Add($oid)

    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $startInfo
    [void]$process.Start()
    $memory = [IO.MemoryStream]::new()
    try {
        $process.StandardOutput.BaseStream.CopyTo($memory)
        $errorText = $process.StandardError.ReadToEnd()
        $process.WaitForExit()
        if ($process.ExitCode -ne 0) { throw $errorText }
        return ,$memory.ToArray()
    }
    finally {
        $memory.Dispose()
        $process.Dispose()
    }
}

function Get-MissingGitPaths {
    param([string[]]$Paths)
    if ($Paths.Count -eq 0) { return @() }

    $startInfo = [Diagnostics.ProcessStartInfo]::new()
    $startInfo.FileName = 'git'
    $startInfo.UseShellExecute = $false
    $startInfo.RedirectStandardInput = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $startInfo.CreateNoWindow = $true
    $startInfo.StandardInputEncoding = $utf8
    $startInfo.StandardOutputEncoding = $utf8
    [void]$startInfo.ArgumentList.Add('cat-file')
    [void]$startInfo.ArgumentList.Add('--batch-check')

    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $startInfo
    [void]$process.Start()
    try {
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()
        foreach ($path in $Paths) {
            $process.StandardInput.WriteLine("HEAD:$path")
        }
        $process.StandardInput.Close()
        $process.WaitForExit()
        $output = $stdoutTask.GetAwaiter().GetResult()
        $errorText = $stderrTask.GetAwaiter().GetResult()
        if ($process.ExitCode -ne 0) { throw $errorText }

        $lines = @($output -split "`r?`n" | Where-Object { $_.Length -gt 0 })
        if ($lines.Count -ne $Paths.Count) {
            throw "Git batch check returned $($lines.Count) rows for $($Paths.Count) paths."
        }
        $missingPaths = [Collections.Generic.List[string]]::new()
        for ($i = 0; $i -lt $Paths.Count; $i++) {
            $line = $lines[$i]
            if ($line.EndsWith(' missing', [StringComparison]::Ordinal)) {
                $missingPaths.Add($Paths[$i])
            }
        }
        return @($missingPaths)
    }
    finally {
        $process.Dispose()
    }
}

function Get-MarkdownTargets {
    param([string]$Text)
    $targets = [Collections.Generic.List[string]]::new()
    for ($i = 0; $i -lt $Text.Length - 1; $i++) {
        if ($Text[$i] -ne ']' -or $Text[$i + 1] -ne '(') { continue }
        $start = $i + 2
        $depth = 1
        $angle = $false
        $escaped = $false
        for ($j = $start; $j -lt $Text.Length; $j++) {
            $char = $Text[$j]
            if ($escaped) { $escaped = $false; continue }
            if ($char -eq '\') { $escaped = $true; continue }
            if ($j -eq $start -and $char -eq '<') { $angle = $true; continue }
            if ($angle) {
                if ($char -eq '>') { $angle = $false }
                continue
            }
            if ($char -eq '(') { $depth++; continue }
            if ($char -eq ')') {
                $depth--
                if ($depth -eq 0) {
                    $targets.Add($Text.Substring($start, $j - $start).Trim())
                    $i = $j
                    break
                }
            }
        }
    }
    return @($targets)
}

function Get-Destination {
    param([string]$RawTarget)
    if ($RawTarget.StartsWith('<')) {
        $end = $RawTarget.IndexOf('>')
        if ($end -lt 1) { throw 'Malformed angle-bracket link destination.' }
        return $RawTarget.Substring(1, $end - 1)
    }
    $escaped = $false
    for ($i = 0; $i -lt $RawTarget.Length; $i++) {
        $char = $RawTarget[$i]
        if ($escaped) { $escaped = $false; continue }
        if ($char -eq '\') { $escaped = $true; continue }
        if ([char]::IsWhiteSpace($char)) { return $RawTarget.Substring(0, $i) }
    }
    return $RawTarget
}

$rows = [Collections.Generic.List[object]]::new()
$missing = [Collections.Generic.List[string]]::new()
$uniqueTargets = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$totalLocal = 0
$totalExternal = 0
$totalFragments = 0
$guardedTargets = 0

foreach ($document in $documents) {
    $bytes = Get-GitBlobBytes -Path $document
    $text = $utf8.GetString($bytes)
    $local = 0
    $external = 0
    $fragments = 0

    foreach ($rawTarget in (Get-MarkdownTargets -Text $text)) {
        $target = Get-Destination -RawTarget $rawTarget
        if ([string]::IsNullOrWhiteSpace($target)) { continue }
        if ($target.StartsWith('#')) { $fragments++; $totalFragments++; continue }
        if ($target -match '^[A-Za-z][A-Za-z0-9+.-]*:') {
            $external++
            $totalExternal++
            continue
        }

        $pathPart = ($target -split '#', 2)[0]
        $pathPart = ($pathPart -split '\?', 2)[0]
        $pathPart = [uri]::UnescapeDataString($pathPart)
        if ([string]::IsNullOrWhiteSpace($pathPart)) { continue }

        if ($pathPart.StartsWith('/')) {
            $fullTarget = [IO.Path]::GetFullPath((Join-Path $repoRoot $pathPart.TrimStart('/')))
        }
        else {
            $base = [IO.Path]::GetDirectoryName((Join-Path $repoRoot $document))
            $fullTarget = [IO.Path]::GetFullPath((Join-Path $base $pathPart))
        }
        $prefix = $repoRoot.TrimEnd('\') + '\'
        if (-not $fullTarget.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) {
            throw "Local link escapes the repository in $document."
        }
        $repoTarget = [IO.Path]::GetRelativePath($repoRoot, $fullTarget).Replace('\', '/')
        if ($repoTarget -match '(?i)(^|/)(sga|fac|gaga)(/|$)|erd[oő]s|erdos|es-fable-c123') {
            $guardedTargets++
            throw "A prohibited local target appears in scoped document $document."
        }

        $local++
        $totalLocal++
        [void]$uniqueTargets.Add($repoTarget)
    }

    $rows.Add([pscustomobject]@{
        path                = $document
        bytes               = $bytes.Length
        sha256              = Get-Sha256 -Bytes $bytes
        local_links         = $local
        external_links      = $external
        fragment_only_links = $fragments
    })
}

$targetPaths = [string[]]@($uniqueTargets)
[Array]::Sort($targetPaths, [StringComparer]::Ordinal)
foreach ($missingTarget in (Get-MissingGitPaths -Paths $targetPaths)) {
    $missing.Add($missingTarget)
}

$canonical = [Text.StringBuilder]::new()
foreach ($row in $rows) {
    [void]$canonical.Append($row.path)
    [void]$canonical.Append("`t")
    [void]$canonical.Append($row.bytes)
    [void]$canonical.Append("`t")
    [void]$canonical.Append($row.sha256)
    [void]$canonical.Append("`n")
}
$canonicalBytes = $utf8.GetBytes($canonical.ToString())

$result = [ordered]@{
    schema               = 'github-local-links/v1'
    observed_date        = $ObservedDate
    observed_commit      = (& git rev-parse HEAD).Trim()
    scope                = 'Committed Git-blob identities and inline local links in nineteen explicitly allowed coverage maps; the GitHub-only map, archive, reader, source, custody, and receipt landings; and six contributor entry points. External URLs are counted but never requested.'
    canonical_stream     = 'Ordinal document path order; path<TAB>bytes<TAB>SHA256<LF>; UTF-8 without BOM.'
    aggregate            = [ordered]@{
        documents              = $rows.Count
        document_bytes         = [int64](($rows | Measure-Object bytes -Sum).Sum)
        canonical_stream_bytes = $canonicalBytes.Length
        tree_sha256            = Get-Sha256 -Bytes $canonicalBytes
        local_links            = $totalLocal
        unique_local_targets   = $uniqueTargets.Count
        external_links         = $totalExternal
        fragment_only_links    = $totalFragments
        missing_local_links    = $missing.Count
        prohibited_targets     = $guardedTargets
    }
    documents            = @($rows)
    checks               = [ordered]@{
        documents_present                  = "$($rows.Count)/$($rows.Count)"
        local_links_resolved               = "$($totalLocal - $missing.Count)/$totalLocal"
        external_network_queried           = $false
        identity_surface                   = 'HEAD Git blobs'
        working_tree_content_read          = $false
        producer_files_mutated             = $false
        compile_render_or_ocr_run           = $false
        global_filesystem_search            = $false
        prohibited_or_revoked_roots_touched = $false
    }
}

if ($missing.Count -ne 0) {
    $missing | ForEach-Object { Write-Error $_ }
    throw "Missing local links: $($missing.Count)"
}

$json = (($result | ConvertTo-Json -Depth 7).Replace("`r`n", "`n")) + "`n"
[IO.File]::WriteAllText((Join-Path $repoRoot $OutputPath), $json, $utf8)

[pscustomobject]@{
    documents            = $rows.Count
    document_bytes       = $result.aggregate.document_bytes
    local_links          = $totalLocal
    unique_local_targets = $uniqueTargets.Count
    external_links       = $totalExternal
    fragment_only_links  = $totalFragments
    missing_local_links  = $missing.Count
    prohibited_targets   = $guardedTargets
    tree_sha256          = $result.aggregate.tree_sha256
} | ConvertTo-Json -Compress
